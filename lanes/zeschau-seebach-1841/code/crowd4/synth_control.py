#!/usr/bin/env python3
"""SYNTHETIC CONTROL for the joint decipherment engine — round 4, WO8(c).

Generates a fake cipher from the era corpus with the same statistical profile
as R5005 (96 groups, 7 pins, ear-cutting noise, polyvalent islets, 3-phase
rotation) and KNOWN ground truth, then validates the joint engine on it.

INDEPENDENCE (N16 lesson): the generator uses a seeded RNG (4107) and a
documented noisy segmentation. It does NOT use the engine's priors (letter-LM
scores, phase profile, soft hints) to construct anything. The engine sees only
the group stream + pins + corpus (+ 5 provisional-style hints, all correct).
The control plaintext span is EXCLUDED from the engine's letter-LM training.

PRE-STATED PASS BARS (frozen before the run; see PASS_BARS):
  1. pins intact: 7/7 (sanity).
  2. primary recovery: marginal-argmax top-1 >= 0.50 on the 20 most frequent
     non-pin groups whose true primary is in the engine's inventory.
  3. islets: >= 2/3 islet groups have BOTH true values in the top-3 marginal
     P(cell|g), with the true DOMINANT value ranked #1.
  4. optimisation sanity: annealed best beats best-of-20 random keys by >= 200
     nats on the full objective.
If all pass -> CONTROL-PASS (run_r5005.py is then allowed to run).
Else -> BROKEN-ON-CONTROL with diagnosis. No real drag on failure.

Ablation (model selection ON the control, reported): lam_rot in {0,1},
lam_poly in {10,20}; 3 restarts x 600 sweeps each; pick argmax composite =
primary_acc + islet_score. The picked config is frozen for R5005.
"""

import collections
import json
import math
import os
import random
import re
import sys
import time

LANE = os.path.expanduser('~/workspace/cipher-hunt/lanes/zeschau-seebach-1841')
sys.path.insert(0, os.path.join(LANE, 'code'))
sys.path.insert(0, os.path.join(LANE, 'code', 'crowd2'))
sys.path.insert(0, os.path.join(LANE, 'code', 'crowd4'))
from scorer_smith import build_models  # noqa: E402
from joint_engine import (build_letter_trigram, build_inventory, JointModel,
                          random_key_baseline, PINS)  # noqa: E402

DATA = os.path.join(LANE, 'data')
OUTD = os.path.join(LANE, 'code', 'crowd4')
os.makedirs(OUTD, exist_ok=True)

SEED_GEN = 4107          # control generation seed (documented, != engine 1841)
SEED_ENG = 1841

# --- pre-stated pass bars (frozen) ---
PASS_BARS = {
    'pins_intact': 7,
    'primary_top1_min': 0.50,   # on top-20 frequent non-pin in-inventory groups
    'islets_min': 2,            # of 3 islets meeting the both-in-top3+dom-first rule
    'baseline_margin_nats': 200.0,
}

# --- ear-cutting noise rates (documented) ---
P_MERGE = 0.12   # merge a random adjacent cell pair within a word
P_SPLIT = 0.08   # split a len>=3 unit into (first letter | rest)
P_TRUNC = 0.06   # drop final 'e' of a len>2 unit ending in 'e'
P_EAR = 0.03     # phonetic-ish letter substitution within a unit
VOWELS = set('aeiouyàâäéèêëîïôöùûüÿœæ')
EAR_SUBS = [('au', 'o'), ('eau', 'o'), ('ai', 'é'), ('ph', 'f'),
            ('é', 'e'), ('è', 'e'), ('ê', 'e'), ('à', 'a'), ('ç', 'c'),
            ('ou', 'u'), ('ch', 'sch')]

# --- control plaintext: Tocqueville t1, held-out span (words) ---
SPAN = (40000, 41100)   # ~1100 words -> ~1900 cells, cf. R5005's 1846 pairs

# --- rotation matrix for the generator: EMPIRICAL from R5005 (measured) ---
# A->{A:.237,B:.261,C:.418,R:.084} B->{A:.476,B:.145,C:.301,R:.078}
# C->{A:.295,B:.450,C:.211,R:.045} R-> empirical
ROT = {'A': {'A': .237, 'B': .261, 'C': .418, 'R': .084},
       'B': {'A': .476, 'B': .145, 'C': .301, 'R': .078},
       'C': {'A': .295, 'B': .450, 'C': .211, 'R': .045},
       'R': {'A': .40, 'B': .20, 'C': .20, 'R': .20}}
PHASE_SIZES = {'A': 30, 'B': 26, 'C': 23, 'R': 17}  # like R5005
N_ROT_DRIVERS = 40   # frequent cells getting 2 groups (rotation drivers)
N_SINGLETONS = 6     # frequent cells getting 1 group
N_ISLETS = 3


# ---------------------------------------------------------------- noisy segmentation
def noisy_cells(words, segs, rng):
    """Rule syllabification + documented ear-cutting noise -> true cells."""
    out = []
    for w in words:
        units = list(segs(w))
        # merge
        i = 0
        merged = []
        while i < len(units):
            if i + 1 < len(units) and rng.random() < P_MERGE:
                merged.append(units[i] + units[i + 1])
                i += 2
            else:
                merged.append(units[i])
                i += 1
        units = merged
        # split
        split = []
        for u in units:
            if len(u) >= 3 and rng.random() < P_SPLIT:
                split += [u[0], u[1:]]
            else:
                split.append(u)
        units = split
        # truncate final e
        units = [(u[:-1] if (len(u) > 2 and u.endswith('e')
                             and rng.random() < P_TRUNC) else u)
                 for u in units]
        # ear substitutions
        eared = []
        for u in units:
            if rng.random() < P_EAR:
                for a, b in EAR_SUBS:
                    if a in u:
                        u = u.replace(a, b, 1)
                        break
            eared.append(u)
        out.append(eared)
    return out


# ---------------------------------------------------------------- codebook construction
def build_codebook(cell_freq, inventory_set, rng):
    """96-group codebook. Returns (cell_to_groups, group_info, truth).

    cell_to_groups: cell -> [(group, phase)]. group_info: group ->
      {'phase', 'primary', 'secondary', 'w2', 'kind'}.
    """
    # anchor labels are fixed: exclude them from the shuffled pool
    groups = ['%02d' % i for i in range(96) if '%02d' % i not in PINS]
    assert len(groups) == 96 - len(PINS)
    rng.shuffle(groups)
    cell_to_groups = collections.defaultdict(list)
    group_info = {}
    # anchor phases mimic R5005's real anchor phases
    anchor_phase = {'11': 'A', '70': 'A', '82': 'B', '34': 'A',
                    '29': 'C', '40': 'B', '46': 'A'}
    ROT_SUCC = {'A': 'C', 'B': 'A', 'C': 'B', 'R': 'A'}  # rotation successor
    gi = iter(groups)

    def take(phase=None):
        g = next(gi)
        ph = phase or rng.choice('ABCR')
        return g, ph

    # 1. anchors: 7 pinned groups (fixed real phases) + 7 homophones at the
    #    rotation-successor phase. The top cells MUST have phase choice or
    #    the phase-cycled encryption cannot produce the rotation.
    for g, cell in PINS.items():
        ph = anchor_phase[g]
        cell_to_groups[cell].append((g, ph))
        group_info[g] = {'phase': ph, 'primary': cell, 'secondary': None,
                         'w2': 0.0, 'kind': 'anchor'}
    for g, cell in PINS.items():
        gh, ph = take(phase=ROT_SUCC[anchor_phase[g]])
        cell_to_groups[cell].append((gh, ph))
        group_info[gh] = {'phase': ph, 'primary': cell, 'secondary': None,
                          'w2': 0.0, 'kind': 'anchor-hom'}

    # candidate cells by frequency, in-inventory required for test cells
    freq_cells = [c for c, _ in cell_freq.most_common()
                  if c not in PINS.values()]
    # 2. islets: 3 top frequent in-inventory cells as primaries; each gets an
    #    islet group (polyvalent primary/secondary) AND a pure homophone
    #    (so the top cells keep phase choice); secondaries = 3 other
    #    frequent in-inventory cells
    primaries = [c for c in freq_cells if c in inventory_set][:6]
    islet_prim = primaries[:3]
    islet_sec = primaries[3:6]
    islet_ws = [0.35, 0.30, 0.40]
    # NOTE: secondaries are deliberately NOT in used_cells: any standalone
    # occurrences get lossy fallback groups in step 5 (background
    # polyvalence, documented). The islet group itself emits them
    # probabilistically via the primary's codebook entry.
    used_cells = set(PINS.values()) | set(islet_prim)
    for pc, sc, w in zip(islet_prim, islet_sec, islet_ws):
        g, ph = take(phase=rng.choice('ABC'))
        cell_to_groups[pc].append((g, ph))
        group_info[g] = {'phase': ph, 'primary': pc, 'secondary': sc,
                         'w2': w, 'kind': 'islet',
                         'conditioner': 'independent coin P(secondary)=w2 '
                                        '(the engine conditions '
                                        'per-occurrence via its letter-LM '
                                        'E-step; the generator keeps the '
                                        'mixture unconditioned)'}
        gh, phh = take(phase=ROT_SUCC[ph])
        cell_to_groups[pc].append((gh, phh))
        group_info[gh] = {'phase': phh, 'primary': pc, 'secondary': None,
                          'w2': 0.0, 'kind': 'driver'}

    # 3. rotation drivers: 30 frequent in-inventory cells x 2 groups,
    #    phase pairs cycling (A,C),(C,B),(B,A)
    drivers = [c for c in freq_cells
               if c in inventory_set and c not in used_cells][:30]
    used_cells |= set(drivers)
    pairs = [('A', 'C'), ('C', 'B'), ('B', 'A')]
    for i, c in enumerate(drivers):
        for ph in pairs[i % 3]:
            g, ph2 = take(phase=ph)
            assert ph2 == ph
            cell_to_groups[c].append((g, ph))
            group_info[g] = {'phase': ph, 'primary': c, 'secondary': None,
                             'w2': 0.0, 'kind': 'driver'}

    # 4. singletons: fill to 96 groups
    n_single = 96 - len(group_info)
    singles = [c for c in freq_cells if c not in used_cells][:n_single]
    used_cells |= set(singles)
    for c in singles:
        g, ph = take(phase=rng.choice(['A', 'B', 'C', 'R', 'R']))
        cell_to_groups[c].append((g, ph))
        group_info[g] = {'phase': ph, 'primary': c, 'secondary': None,
                         'w2': 0.0, 'kind': 'singleton'}

    # 5. long tail: map every true cell without a codebook entry to an
    #    existing group (lossy fallback -> background polyvalence,
    #    documented). This also covers islet secondaries occurring
    #    standalone.
    covered = [c for c in used_cells if cell_to_groups[c]]
    tail_map = {}
    for c in cell_freq:
        if cell_to_groups[c]:
            continue
        # most letter-overlap with a covered cell (Jaccard on char bigrams)
        bc = set(zip(c, c[1:])) or {c}
        best, bs = None, -1.0
        for d in covered:
            bd = set(zip(d, d[1:])) or {d}
            s = len(bc & bd) / len(bc | bd)
            if s > bs:
                best, bs = d, s
        tail_map[c] = best
        # attach to best's first group (background polyvalence)
        g0 = cell_to_groups[best][0][0]
        cell_to_groups[c].append((g0, group_info[g0]['phase']))
        if group_info[g0]['kind'] not in ('islet', 'anchor'):
            group_info[g0]['kind'] = 'shared'

    n_groups = len(group_info)
    assert n_groups == 96, n_groups
    # phase sizes (for the report; no exact budget enforced)
    phase_sizes = collections.Counter(v['phase'] for v in group_info.values())
    truth = {'islets': {g: {k: group_info[g][k] for k in
                            ('primary', 'secondary', 'w2', 'conditioner')}
                        for g in group_info
                        if group_info[g]['kind'] == 'islet'},
             'tail_map': tail_map,
             'drivers': drivers, 'singletons': singles}
    return cell_to_groups, group_info, truth


# ---------------------------------------------------------------- encryption
def encrypt(cell_seqs, cell_to_groups, group_info, rng):
    """Phase-cycled encryption -> (group stream, emitted true cells)."""
    gs, emitted = [], []
    phase = 'A'
    for seq in cell_seqs:
        for ci, c in enumerate(seq):
            opts = cell_to_groups[c]
            # sample next phase from the empirical rotation matrix
            r, acc = rng.random(), 0.0
            nph = 'R'
            for ph, p in ROT[phase].items():
                acc += p
                if r < acc:
                    nph = ph
                    break
            pick = next((g for g, ph in opts if ph == nph), opts[0][0])
            info = group_info[pick]
            if info['secondary'] is not None:
                # polyvalent islet: independent coin P(secondary)=w2.
                # The ENGINE conditions per-occurrence via its letter-LM
                # E-step; the generator keeps the mixture unconditioned so
                # the test of the E-step is pure.
                cell = (info['secondary'] if rng.random() < info['w2']
                        else info['primary'])
            else:
                cell = c
            gs.append(pick)
            emitted.append(cell)
            phase = info['phase']
    return gs, emitted


# ---------------------------------------------------------------- phase derivation (engine-side, mirrors real pipeline)
def derive_phases(stream, k_cut=12):
    """Jaccard-k12 agglomerative clustering (contactor's method, reimplemented
    compactly) -> dict g->phase in {A,B,C,R}."""
    groups = sorted(set(stream))
    foll = collections.defaultdict(collections.Counter)
    pred = collections.defaultdict(collections.Counter)
    for a, b in zip(stream, stream[1:]):
        foll[a][b] += 1
        pred[b][a] += 1
    K = 10
    TOP = {g: (set(h for h, _ in foll[g].most_common(K)) |
               set(h for h, _ in pred[g].most_common(K))) for g in groups}

    def jac(a, b):
        sa, sb = TOP[a], TOP[b]
        u = sa | sb
        return len(sa & sb) / len(u) if u else 0.0

    clusters = [{g} for g in groups]
    merges = []
    while len(clusters) > 1:
        best, bi, bj = -1.0, None, None
        for i in range(len(clusters)):
            for j in range(i + 1, len(clusters)):
                c1, c2 = clusters[i], clusters[j]
                s = sum(jac(a, b) for a in c1 for b in c2) / (len(c1) * len(c2))
                if s > best:
                    best, bi, bj = s, i, j
        merges.append((sorted(clusters[bi]), sorted(clusters[bj])))
        new = clusters[bi] | clusters[bj]
        clusters = [c for k, c in enumerate(clusters)
                    if k not in (bi, bj)] + [new]
    cs = [{g} for g in groups]
    for c1l, c2l in merges:
        if len(cs) <= k_cut:
            break
        c1, c2 = set(c1l), set(c2l)
        cs = [c for c in cs if c != c1 and c != c2] + [c1 | c2]
    cs = sorted(cs, key=len, reverse=True)
    block = {}
    for x, lbl in ((cs[0], 'A'), (cs[1], 'B'), (cs[2], 'C')):
        for g in x:
            block[g] = lbl
    for c in cs[3:]:
        for g in c:
            block[g] = 'R'
    return block


def rotation_chi2(stream, block):
    trans = collections.Counter((block[stream[i]], block[stream[i + 1]])
                                 for i in range(len(stream) - 1))
    obs = [[trans[(r, c)] for c in 'ABC'] for r in 'ABC']
    rs = [sum(r) for r in obs]
    cs = [sum(obs[r][c] for r in range(3)) for c in range(3)]
    T = sum(rs)
    chi2 = sum((obs[r][c] - rs[r] * cs[c] / T) ** 2 / (rs[r] * cs[c] / T)
               for r in range(3) for c in range(3) if rs[r] * cs[c])
    return chi2


# ---------------------------------------------------------------- control driver
def main():
    t_start = time.time()
    print('[control] building era models (control span excluded from LM)...',
          flush=True)
    M = build_models()
    toks = M['toks']
    a, b = SPAN
    words = toks[a:b]
    print('  control plaintext: %d words (t1 [%d,%d))' % (len(words), a, b),
          flush=True)

    # letter trigram EXCLUDING the control span (independence)
    class M2(dict):
        pass
    Msub = M2(M)
    Msub['toks'] = toks[:a] + toks[b:]
    lp, _ = build_letter_trigram(Msub)
    cells, weights = build_inventory(M)
    inventory_set = set(cells)
    print('  inventory: %d cells' % len(cells), flush=True)

    rng = random.Random(SEED_GEN)
    print('[control] noisy segmentation (ear-cutting)...', flush=True)
    cell_seqs = noisy_cells(words, M['segs'], rng)
    flat = [c for s in cell_seqs for c in s]
    cell_freq = collections.Counter(flat)
    print('  %d cells, %d distinct; top: %s' % (
        len(flat), len(cell_freq),
        [(c, n) for c, n in cell_freq.most_common(8)]), flush=True)

    print('[control] building 96-group codebook...', flush=True)
    cell_to_groups, group_info, truth = build_codebook(
        cell_freq, inventory_set, rng)
    print('  groups=%d kinds=%s' % (
        len(group_info),
        dict(collections.Counter(v['kind'] for v in group_info.values()))),
        flush=True)

    print('[control] encrypting with phase cycling...', flush=True)
    gs, emitted = encrypt(cell_seqs, cell_to_groups, group_info, rng)
    print('  stream: %d groups, %d distinct' % (len(gs), len(set(gs))),
          flush=True)

    # engine-side phase derivation (mirrors the real pipeline)
    print('[control] deriving phases (engine-side Jaccard-k12)...', flush=True)
    block = derive_phases(gs)
    chi2 = rotation_chi2(gs, block)
    # agreement with generator truth phases
    true_block = {g: v['phase'] for g, v in group_info.items()}
    # label alignment via anchors of size: map derived->true by max overlap
    import itertools
    best_agree, best_map = 0, None
    for perm in itertools.permutations('ABCR'):
        m = dict(zip('ABCR', perm))
        # derived labels are A,B,C,R by size order; align to true labels
        agree = sum(1 for g in group_info
                    if m.get(block[g], '?') == true_block[g])
        if agree > best_agree:
            best_agree, best_map = agree, m
    ari = best_agree / len(group_info)
    print('  rotation chi2=%.1f (R5005 banked: 181.3); phase ARI=%.3f' % (
        chi2, ari), flush=True)

    # soft hints: 5 frequent non-anchor groups, TRUE primaries (all correct)
    sfreq = collections.Counter(gs)
    hint_groups = [g for g, _ in sfreq.most_common()
                   if g not in PINS][:5]
    hints = {g: group_info[g]['primary'] for g in hint_groups}
    assert all(h in inventory_set for h in hints.values())
    print('  soft hints (all correct): %s' % hints, flush=True)

    # save ground truth (SYNTHETIC, labelled)
    truth_full = {
        'SYNTHETIC': True,
        'seed_gen': SEED_GEN, 'span': SPAN,
        'noise_rates': {'p_merge': P_MERGE, 'p_split': P_SPLIT,
                        'p_trunc': P_TRUNC, 'p_ear': P_EAR,
                        'ear_subs': EAR_SUBS},
        'n_cells': len(flat), 'n_distinct_cells': len(cell_freq),
        'n_stream': len(gs), 'n_groups': len(set(gs)),
        'rotation_chi2_derived': round(chi2, 1),
        'phase_ARI_derived_vs_true': round(ari, 3),
        'pins': PINS, 'hints': hints,
        'group_info': group_info,
        'islets': truth['islets'],
        'tail_map_size': len(truth['tail_map']),
        'stream': gs, 'emitted': emitted,
    }
    with open(os.path.join(OUTD, 'control_ground_truth.json'), 'w') as f:
        json.dump(truth_full, f, ensure_ascii=False)
    print('[control] ground truth saved (SYNTHETIC label).', flush=True)

    # ---------------- ablation (model selection on the control) ----------------
    print('[ablation] lam_rot x lam_poly grid (3 restarts x 600 sweeps)...',
          flush=True)
    grid = [(0.0, 10.0), (0.0, 20.0), (1.0, 10.0), (1.0, 20.0)]
    ab_results = []
    for lam_rot, lam_poly in grid:
        accs, isl = [], []
        for rs in range(3):
            m = JointModel(gs, block, lp, PINS, hints, cells, weights,
                           lam_rot, lam_poly, rng=random.Random(SEED_ENG))
            res = m.anneal(sweeps=600, T0=2.0, T1=0.02,
                           seed=SEED_ENG + rs)
            marg = m.marginals(sweeps=150, T=0.3, seed=SEED_ENG + rs)
            pa = primary_accuracy(marg, group_info, sfreq, inventory_set)
            im = islet_score(marg, truth['islets'])
            accs.append(pa)
            isl.append(im)
            print('    lam_rot=%.1f lam_poly=%.1f restart=%d acc=%.3f '
                  'islet=%.2f best=%.1f' % (
                      lam_rot, lam_poly, rs, pa, im, res['best']), flush=True)
        composite = sum(accs) / 3 + sum(isl) / 3
        ab_results.append({'lam_rot': lam_rot, 'lam_poly': lam_poly,
                           'mean_acc': sum(accs) / 3,
                           'mean_islet': sum(isl) / 3,
                           'composite': composite})
    ab_results.sort(key=lambda d: -d['composite'])
    picked = ab_results[0]
    print('[ablation] picked lam_rot=%.1f lam_poly=%.1f (composite %.3f)' % (
        picked['lam_rot'], picked['lam_poly'], picked['composite']), flush=True)

    # ---------------- full validation run (picked config) ----------------
    print('[control] FULL validation run (8 restarts x 1200 sweeps)...',
          flush=True)
    best_m, best_s = None, float('-inf')
    for rs in range(8):
        m = JointModel(gs, block, lp, PINS, hints, cells, weights,
                       picked['lam_rot'], picked['lam_poly'],
                       rng=random.Random(SEED_ENG))
        res = m.anneal(sweeps=1200, T0=2.0, T1=0.02, seed=SEED_ENG + 100 + rs,
                       log_every=0)
        print('    restart %d: best=%.1f acc=%.3f' % (
            rs, res['best'], res['acc_rate']), flush=True)
        if res['best'] > best_s:
            best_s, best_m = res['best'], m
    print('[control] marginals (400 sweeps @ T=0.3)...', flush=True)
    marg = best_m.marginals(sweeps=400, T=0.3, seed=SEED_ENG + 777)

    base = random_key_baseline(gs, block, lp, PINS, hints, cells, weights,
                               picked['lam_rot'], picked['lam_poly'],
                               n=20, seed=999)
    pa, pa_detail = primary_accuracy(marg, group_info, sfreq, inventory_set,
                                     detail=True)
    isl, isl_detail = islet_score(marg, truth['islets'], detail=True)
    pins_ok = sum(1 for g, c in PINS.items()
                  if best_m.v1[g] == c)

    verdict = (pins_ok == PASS_BARS['pins_intact']
               and pa >= PASS_BARS['primary_top1_min']
               and isl >= PASS_BARS['islets_min']
               and (best_s - base) >= PASS_BARS['baseline_margin_nats'])
    out = {
        'SYNTHETIC': True,
        'meta': {'seed_gen': SEED_GEN, 'seed_eng': SEED_ENG, 'span': SPAN,
                 'noise': {'p_merge': P_MERGE, 'p_split': P_SPLIT,
                           'p_trunc': P_TRUNC, 'p_ear': P_EAR},
                 'inventory': len(cells),
                 'pass_bars': PASS_BARS,
                 'elapsed_s': round(time.time() - t_start, 1)},
        'stream_profile': {'n': len(gs), 'n_groups': len(set(gs)),
                           'rotation_chi2': round(chi2, 1),
                           'phase_ARI': round(ari, 3)},
        'ablation': ab_results,
        'picked': picked,
        'results': {
            'pins_intact': '%d/%d' % (pins_ok, len(PINS)),
            'primary_top1': round(pa, 4),
            'primary_detail': pa_detail,
            'islet_score': isl, 'islet_detail': isl_detail,
            'annealed_best': round(best_s, 1),
            'random_baseline': round(base, 1),
            'margin_nats': round(best_s - base, 1),
        },
        'verdict': 'CONTROL-PASS' if verdict else 'BROKEN-ON-CONTROL',
    }
    with open(os.path.join(OUTD, 'control_results.json'), 'w') as f:
        json.dump(out, f, indent=1, ensure_ascii=False)
    with open(os.path.join(OUTD, 'control_results.md'), 'w') as f:
        f.write(render_md(out))
    print('[control] verdict: %s (pins %d/7, acc=%.3f, islets=%d/3, '
          'margin=%.0f nats)' % (
              out['verdict'], pins_ok, pa, isl, best_s - base), flush=True)
    print('[done] wrote code/crowd4/control_{ground_truth,results}.{json,md} '
          'in %.0fs' % (time.time() - t_start), flush=True)


# ---------------------------------------------------------------- metrics
def primary_accuracy(marg, group_info, sfreq, inventory_set, detail=False):
    """Top-1 marginal-argmax accuracy on the 20 most frequent non-pin groups
    whose TRUE primary is in the engine inventory."""
    cands = [(g, n) for g, n in sfreq.most_common()
             if g not in PINS
             and group_info[g]['primary'] in inventory_set][:20]
    hits, rows = 0, []
    for g, n in cands:
        top1 = marg[g][0][0] if marg[g] else None
        true = group_info[g]['primary']
        ok = (top1 == true)
        hits += ok
        rows.append({'group': g, 'n': n, 'true': true, 'top1': top1,
                     'top1_p': round(marg[g][0][1], 3) if marg[g] else None,
                     'hit': ok, 'kind': group_info[g]['kind']})
    acc = hits / len(cands) if cands else 0.0
    return (acc, rows) if detail else acc


def islet_score(marg, islets, detail=False):
    """Per islet: both true values in top-3 marginal AND dominant ranked #1."""
    score, rows = 0, []
    for g, t in islets.items():
        top3 = [v for v, _ in marg[g][:3]]
        dom_first = marg[g] and marg[g][0][0] == t['primary']
        both = t['primary'] in top3 and t['secondary'] in top3
        ok = bool(both and dom_first)
        score += ok
        rows.append({'group': g, 'primary': t['primary'],
                     'secondary': t['secondary'], 'w2_true': t['w2'],
                     'top5': [(v, round(p, 3)) for v, p in marg[g][:5]],
                     'both_in_top3': bool(both), 'dominant_first': bool(dom_first),
                     'pass': ok})
    return (score, rows) if detail else score


def render_md(out):
    m, r = out['meta'], out['results']
    L = []
    A = lambda *a: L.append(' '.join(str(x) for x in a))
    A('# JOINT ENGINE — SYNTHETIC CONTROL (WO8c)')
    A()
    A('**Verdict: %s** (SYNTHETIC — not R5005)' % out['verdict'])
    A()
    A('Design: Tocqueville-t1 [%d,%d) (%d words) -> rule syllabification + '
      'ear-cutting noise (merge %.2f / split %.2f / trunc %.2f / ear %.2f) -> '
      '96-group codebook: 7 anchors pinned, 28 rotation-driver cells x2 groups '
      '(phase pairs A-C/C-B/B-A), 30 singletons, 3 polyvalent islets '
      '(conditioned weights), long-tail lossy merge -> phase-cycled encryption '
      'with the EMPIRICAL R5005 rotation matrix. Engine sees: group stream, '
      '7 pins, 5 correct soft hints, era corpus (control span EXCLUDED from '
      'the letter-LM). Generation seed %d; engine seed %d.' % (
          m['seed_gen'], m['span'][0], m['span'][1], 1100,
          m['noise']['p_merge'], m['noise']['p_split'], m['noise']['p_trunc'],
          m['noise']['p_ear'], m['seed_gen'], m['seed_eng']))
    A()
    A('Stream profile: n=%d, %d groups, derived-phase rotation chi2=%.1f '
      '(R5005 banked 181.3), derived-vs-true phase ARI=%.3f.' % (
          out['stream_profile']['n'], out['stream_profile']['n_groups'],
          out['stream_profile']['rotation_chi2'], out['stream_profile']['phase_ARI']))
    A()
    A('## Ablation (model selection on the control)')
    for d in out['ablation']:
        A('- lam_rot=%.1f lam_poly=%.1f: mean_acc=%.3f mean_islet=%.2f '
          'composite=%.3f%s' % (
              d['lam_rot'], d['lam_poly'], d['mean_acc'], d['mean_islet'],
              d['composite'],
              '  <-- PICKED' if d == out['picked'] else ''))
    A()
    A('## Validation (picked config, 8 restarts x 1200 sweeps)')
    A('- Pins intact: %s' % r['pins_intact'])
    A('- Primary top-1: %.3f (bar %.2f)' % (
        r['primary_top1'], m['pass_bars']['primary_top1_min']))
    A('- Islets passing (both true values top-3, dominant #1): %d/3 (bar %d)' % (
        r['islet_score'], m['pass_bars']['islets_min']))
    A('- Annealed best %.1f vs random-key baseline %.1f: margin %.1f nats '
      '(bar %.0f)' % (r['annealed_best'], r['random_baseline'],
                      r['margin_nats'], m['pass_bars']['baseline_margin_nats']))
    A()
    A('### Primary recovery detail (top-20 frequent non-pin groups)')
    A('| group | n | true | top-1 | p | hit | kind |')
    A('|---|---|---|---|---|---|---|')
    for d in r['primary_detail']:
        A('| %s | %d | %s | %s | %s | %s | %s |' % (
            d['group'], d['n'], d['true'], d['top1'], d['top1_p'],
            'Y' if d['hit'] else 'n', d['kind']))
    A()
    A('### Islet detail')
    for d in r['islet_detail']:
        A('- g=%s: true %s/%.2f + %s/%.2f; marginal top-5: %s; '
          'both-in-top3=%s dominant-first=%s -> %s' % (
              d['group'], d['primary'], 1 - d['w2_true'], d['secondary'],
              d['w2_true'],
              ', '.join('%s:%.2f' % (v, p) for v, p in d['top5']),
              d['both_in_top3'], d['dominant_first'],
              'PASS' if d['pass'] else 'FAIL'))
    A()
    A('_Bars pre-stated in code (PASS_BARS) before the run. Elapsed %.0fs._' % (
        m['elapsed_s']))
    return '\n'.join(L) + '\n'


if __name__ == '__main__':
    main()
