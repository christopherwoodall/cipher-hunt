#!/usr/bin/env python3
"""
SYNTHETIC CONTROL GENERATOR — Seebach homophonic-solver side fleet.

*** EVERYTHING THIS SCRIPT EMITS IS SYNTHETIC CIPHERTEXT (labelled as such). ***
This is the ONE sanctioned exception to the lane's "never invent ciphertext"
rule: a labelled adversarial control for the new homophonic solver.

Purpose: build N independent synthetic instances of a French two-digit
syllabary cipher that are AT LEAST AS HARD as R5005 (18 Jan 1841,
Zeschau->Seebach) on every quantifiable axis, with a planted ground-truth key.
The solver must pass the pre-registered bar (see CONTROL-DESIGN.md) on these
instances BEFORE touching R5005.

Adversarial design (each axis >= the real problem / >= prior-art controls):
  length            1846 pairs, 96 groups, 7 anchors pinned
                    (identical to R5005: data/attempt1_results.json)
  group labels      the SAME 96 labels as R5005 (00-99 minus 05/25/72/75)
  plaintext         Les Miserables T1 (1862) — register-GAPPED from the
                    solver's Tocqueville reference, mirroring the real
                    diplomatic-vs-Tocqueville register gap (F10: n(cela)/n(ce)
                    6.7x Les Mis vs Tocqueville). Deliberately NOT Tocqueville:
                    the round-3 scorer control used in-distribution Tocqueville
                    t2 plaintext vs a t1+t2 reference (easier than real).
  syllabification   the lane's own rule syllabifier + encipher_split
                    (code/crowd2/scorer_smith.py: syllabify, encipher_split) —
                    same instruments as the round-1 and round-3 controls.
  homophony         MANY groups -> ONE cell, frequency-weighted
                    (common cells get the most aliases): the historical
                    syllabary design and the worst case for frequency attacks.
                    R1 control used uniform-random mapping (easier).
  polyvalence       ONE group -> MANY cells (context-dependent islets),
                    n_poly=6 planted islets vs 3 established real ones
                    (06 /a~/ vs /ma~/, 94 ne/en, 52 pas/se — STATE.md F25/F31,
                    "established but unquantified"). Neither prior control
                    modelled polyvalence at all.
  phase rhythm      A->C->B->A rotation in group transitions, calibrated so the
                    UNSUPERVISED contactor pipeline (Jaccard k=12 -> 3x3 chi2,
                    code/crowd/contactor.py method) measures chi2 in
                    [181, 320] on the synthetic stream vs 181.3 real
                    (code/crowd/contactor_results.json). Neither prior control
                    modelled the rotation.
  ear noise         by-ear spelling noise: mute-e elision, adjacent-cell merge,
                    long-cell split, double-consonant simplification, at rates
                    >= the crowd4 segmenter control's calibrated ear-cutting
                    knobs (p_merge 0.08, p_split 0.04, p_alt 0.06 —
                    code/crowd4/control.py), which a real instrument survived.
                    Real-cipher analogues: "prend"->"pre" @1331 (silent d
                    dropped), "personne" in TWO spellings per|so|nne @160 vs
                    pers|on|ne @508 (code/crowd3/report_inbox/
                    frenchman-ear-check.md). R1 control had NO noise.
  anchors           7 pinned = exactly the real pencil-crib set
                    (11=la 70=pre 82=m 34=i 29=er 40=e 46=que); recoverable via
                    a planted "la premiere" crib reading exactly once at a
                    recorded pair offset (mirrors "la premiere" @pair 1033,
                    STATE.md). R1 pinned 8 (incl. provisional 87=ce: easier).

CLI:
  --calibrate   pilot T-sweep (inventory size) -> picks T landing chi2 in band
  --build-all   calibrate, then build all N_SEEDS instances + chance baseline
  --self-test   rebuild instance 184101 in /tmp and verify invariants

Writes (code/side-homophonic/control/):
  instances/SYNTHETIC-ct-<seed>.pairs.txt     synthetic pair stream
  instances/SYNTHETIC-key-<seed>.json         planted key  [SEALED: Runner only]
  instances/SYNTHETIC-crib-<seed>.json        crib facts disclosed to solver
  instances/SYNTHETIC-meta-<seed>.json        build provenance + diagnostics
  chance_baseline.json   analytic + Monte-Carlo chance for both metrics
  calibration.json       T-sweep table
  build_summary.json     per-instance measured numbers

The Runner's protocol (who sees what) is in CONTROL-DESIGN.md.
"""
import collections
import hashlib
import json
import math
import os
import random
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
sys.path.insert(0, os.path.join(LANE, 'code'))
sys.path.insert(0, os.path.join(LANE, 'code', 'crowd2'))
from crib_attack import load_pairs  # noqa: E402  (verified real-CT loader)
from scorer_smith import syllabify, encipher_split  # noqa: E402  (lane instruments)

DATA = os.path.join(LANE, 'data')
OUTD = os.path.join(HERE, 'instances')

# ------------------------------------------------------------------ parameters
# Difficulty knobs. Certified defaults are defended in CONTROL-DESIGN.md.
PARAMS = {
    'n_seeds': 6,
    'seeds': [184101, 184102, 184103, 184104, 184105, 184106],
    'slice_words': 4000,          # Les Mis words per instance (non-overlapping)
    'crib_word_offsets': [400, 800, 1200, 1600, 2000],
                                   # candidate "la premiere" insertion offsets;
                                   # first feasible one wins (recorded)
    'target_pairs': 1846,         # == R5005 pair count
    'p_mute_e': 0.15,             # mute-e elision ("prend"->"pre" analogue)
    'p_merge': 0.10,              # adjacent-cell merge (inconsistent cuts)
    'p_split': 0.05,              # long-cell split (inconsistent cuts)
    'p_alt': 0.08,                # double-consonant simplification
    'p_letter_split': 0.03,       # prob/word of encipher_split (rare letter
                                 # cells, like the real cipher: i=10, e=21)
    'p_er_free': 0.8,             # prob/word of re-syllabifying trailing -er
                                 # ("parler"->"parl|er"; real 29=er rank 3)
    'n_poly': 6,                  # polyvalent islet groups (real: 3 established)
    'p_poly_use': 0.5,            # secondary-cell emission rate per islet
    'p_emit_phase': 0.85,         # phase-biased emission fidelity
    'q_cycle': 0.55,              # occurrence-phase cycle purity (CALIBRATED)
    'q_cycle_candidates': [0.4, 0.5, 0.6],
    't_candidates': [48, 56, 64, 72],  # inventory-size sweep (phase knob)
    'chi2_band': [181.0, 320.0],  # unsupervised chi2 acceptance band
    'mc_draws': 2000,             # Monte-Carlo draws for chance baseline
}
ANCHORS = {'11': 'la', '70': 'pre', '82': 'm', '34': 'i',
           '29': 'er', '40': 'e', '46': 'que'}
ANCHOR_CELLS = set(ANCHORS.values())
CRIB_CELLS = ['la', 'pre', 'm', 'i', 'er', 'e']   # "la premiere" ear-cut

DOUBLES = ['nn', 'll', 'mm', 'ss', 'tt', 'pp', 'rr', 'ff', 'cc']

HEADER = ("# *** SYNTHETIC CIPHERTEXT — CONTROL FOR THE SEEBACH HOMOPHONIC SOLVER ***\n"
          "# This file is artificially generated. It is NOT R5005 and NOT real.\n"
          "# Generator: code/side-homophonic/control/generator.py\n")


def real_group_labels():
    """The exact 96 group labels used by R5005 (00-99 minus 05/25/72/75)."""
    pairs, _, _ = load_pairs()
    gs = sorted(set(pairs))
    assert (len(pairs), len(gs)) == (1846, 96)
    return gs


def load_lesmis_tokens():
    path = os.path.join(DATA, 'gutenberg-17489-miserables1.txt')
    txt = open(path, encoding='utf-8', errors='replace').read()
    m1 = re.search(r'\*\*\* START OF.*?\*\*\*', txt)
    m2 = re.search(r'\*\*\* END OF.*?\*\*\*', txt)
    if m1:
        txt = txt[m1.end():]
    if m2:
        txt = txt[:m2.start()]
    return re.findall(r"[a-zàâäéèêëîïôöùûüÿçœæ]+", txt.lower())


def ear_noise(cells, rng, p):
    """By-ear spelling noise. Anchor cells are NEVER altered (crib integrity)."""
    out = []
    for c in cells:
        if c in ANCHOR_CELLS:
            out.append(c)
            continue
        if c.endswith('e') and len(c) > 1 and rng.random() < p['p_mute_e']:
            c = c[:-1]                       # mute-e elision: "prend"->"pre"
        if len(c) >= 2 and rng.random() < p['p_alt']:
            for d in DOUBLES:                # double-consonant simplification
                if d in c:
                    c = c.replace(d, d[0], 1)
                    break
        out.append(c)
    # merge adjacent cells (inconsistent cuts: "per|so|nne" vs "pers|on|ne")
    i, merged = 0, []
    while i < len(out):
        if (i < len(out) - 1 and rng.random() < p['p_merge']
                and not (out[i] in ANCHOR_CELLS or out[i + 1] in ANCHOR_CELLS)):
            merged.append(out[i] + out[i + 1])
            i += 2
        else:
            merged.append(out[i])
            i += 1
    # split long cells
    final = []
    for c in merged:
        if (len(c) >= 4 and c not in ANCHOR_CELLS
                and rng.random() < p['p_split']):
            k = len(c) // 2
            final.extend([c[:k], c[k:]])
        else:
            final.append(c)
    return [c for c in final if c]


def _try_build(seed, tokens, group_labels, p, T, crib_word_offset,
               verbose=False):
    """One build attempt with a fixed crib offset. Returns None if the
    1846-pair window cannot jointly cover all 96 groups and the crib."""
    rng = random.Random(seed * 31 + crib_word_offset)
    sl = p['slice_words']
    idx = p['seeds'].index(seed)
    words = tokens[idx * sl:(idx + 1) * sl]
    # scrub natural "première" so the planted crib reads exactly once
    scrubbed = sum(1 for w in words if w == 'première')
    words = [w for w in words if w != 'première']
    # plant the crib phrase at the recorded word offset
    co = crib_word_offset
    words = words[:co] + ['la', 'première'] + words[co:]
    crib_word_idx = co  # index of "la"; "première" is co+1

    # ---- cell pipeline: syllabify -> (probabilistic) splits -> ear noise ----
    # The lane's encipher_split is applied probabilistically per word (rare
    # letter cells, matching the real cipher's i=10, e=21 — NOT the
    # always-on split that floods the stream with letters). Trailing -er is
    # re-syllabified with p_er_free ("parler"->"parl|er"; the lane
    # syllabifier traps -er inside "ler"/"ner", but real 29=er is rank 3,
    # 47x, so the real encipherer freed it). Anchor cells are never altered
    # by noise (crib integrity), but splits may CREATE them (that's natural).
    word_cells = []
    for wi, w in enumerate(words):
        if wi == crib_word_idx + 1:      # the planted crib: force the ear-cut
            cells = list(CRIB_CELLS[1:])  # pre|m|i|er|e (mirrors real @1033)
        else:
            if (len(w) > 3 and w.endswith('er')
                    and rng.random() < p['p_er_free']):
                cells = syllabify(w[:-2]) + ['er']
            else:
                cells = syllabify(w)
            if rng.random() < p['p_letter_split']:
                cells = encipher_split(cells)
            if wi != crib_word_idx:      # crib "la" also exempt from noise
                cells = ear_noise(cells, rng, p)
        if cells:
            word_cells.append((wi, cells))
    # (phases assigned after keep-filter, below)

    # ---- inventory: top-T non-anchor cells + force-included anchors ----
    # Fixpoint: drop inventory cells with zero kept occurrences (every word
    # containing them also contains another OOV cell), then re-filter.
    # Without this, tail cells' groups would never emit (unrepairable).
    cfreq = collections.Counter(c for _, cells in word_cells for c in cells)
    for a in ANCHOR_CELLS:
        assert cfreq[a] > 0, f"anchor cell {a} absent from stream"
    ranked = [c for c, _ in cfreq.most_common() if c not in ANCHOR_CELLS]
    inv_nonanchor = ranked[:T]
    for _round in range(10):
        inventory = set(inv_nonanchor) | ANCHOR_CELLS
        kept = []
        for wi, cells in word_cells:
            ok = all(c in inventory for c in cells) or \
                wi in (crib_word_idx, crib_word_idx + 1)
            if ok:
                kept.append((wi, cells))
        kc = collections.Counter(c for _, cells in kept for c in cells)
        drop = [c for c in inv_nonanchor if kc[c] == 0]
        if not drop:
            break
        inv_nonanchor = [c for c in inv_nonanchor if c not in drop]
    else:
        raise RuntimeError("inventory fixpoint did not converge")
    assert inv_nonanchor, "inventory emptied by fixpoint"
    keep_rate = len(kept) / len(word_cells)
    T_eff = len(inv_nonanchor)

    # GLOBAL DILUTED-CYCLE occurrence-phases over the kept cell stream:
    #   phase(t) = [B, A, C][t % 3] with prob q_cycle, else uniform-random.
    #   Gives the transition edges B->A, A->C, C->B = the A->C->B->A rotation.
    #   q_cycle is CALIBRATED so the occurrence-phase 3x3 chi2 lands in
    #   [181, 320] (the real cipher's measured 181.3). p_emit_phase controls
    #   how faithfully groups follow occurrence phases (encipherer noise).
    # Rationale (documented design changes): positional initial/medial/final
    # classes were tried first: French words are short (mean ~1.7 cells), so
    # masses unbalance (A 62%) and the B->A edge goes flat (1.05x vs 1.47x
    # real). Morphological proclitic/stem/suffix classes were tried next:
    # real rotation present (true chi2 262-314, A->C 1.6x, C->B 1.5x) but
    # B->A still flat (1.05x), and Jaccard clustering cannot recover the
    # planted phases (purity ~0.5) — the contactor's chi2 becomes a coin flip
    # (0-300 across seeds). The diluted cycle reproduces the OBSERVABLE the
    # lane measured (a 3-phase rotation in group transitions, chi2 ~= 181)
    # with direct, stable control over its strength. It is a control device
    # for the transition structure a bigram solver actually faces, not a
    # linguistic claim about the real cipher's phases (mechanism unknown).
    CYCLE = ['B', 'A', 'C']
    qc = p['q_cycle']
    kept_pos = []
    for t in range(sum(len(c) for _, c in kept)):
        if rng.random() < qc:
            kept_pos.append(CYCLE[t % 3])
        else:
            kept_pos.append(rng.choice('BAC'))

    # ---- planted key: anchors pinned; 89 groups -> T cells, freq-weighted ----
    labels = [g for g in group_labels if g not in ANCHORS]
    rng.shuffle(labels)
    kfreq = collections.Counter()
    for _, cells in kept:
        kfreq.update(cells)
    # >=1 group per cell, remainder by largest-remainder proportional to freq
    quota = {c: 1 for c in inv_nonanchor}
    rem = len(labels) - len(inv_nonanchor)
    tot = sum(kfreq[c] for c in inv_nonanchor)
    frac = []
    for c in inv_nonanchor:
        q = rem * kfreq[c] / tot
        quota[c] += int(q)
        frac.append((q - int(q), c))
    frac.sort(reverse=True)
    need = len(labels) - sum(quota.values())
    for _, c in frac[:need]:
        quota[c] += 1
    assert sum(quota.values()) == len(labels)
    cell_groups = {c: [] for c in inv_nonanchor}
    li = 0
    order = sorted(inv_nonanchor, key=lambda c: -kfreq[c])
    for c in order:
        for _ in range(quota[c]):
            cell_groups[c].append(labels[li])
            li += 1
    # PHASE-BIASED homophonic emission. Each cell's aliases are dealt
    # round-robin to phases (shuffled): alias i is primary for phases P with
    # 'BAC'.index(P) % k == i. Emission at occurrence-phase pc picks the
    # primary alias with prob p_emit_phase, else a random alias (encipherer
    # noise). Groups' contacts stay phase-coherent so the rotation is visible
    # to contact clustering (as in R5005); the 1-p_emit_phase noise is the
    # calibrated dilution knob. (Strict phase-specialization was tried: with
    # k=1 aliases the fallback impurity collapsed the group-level rotation
    # to true chi2=86 even at q_cycle=1.0. Uniform-random aliasing was tried
    # first: contact profiles fragment, rotation vanishes, chi2=3.9.)
    anchor_grp = {v: k for k, v in ANCHORS.items()}
    for c in inv_nonanchor:
        rng.shuffle(cell_groups[c])
    key = {g: {'primary': cell, 'secondaries': [], 'phase': 'B'}
           for g, cell in ANCHORS.items()}
    for c in inv_nonanchor:
        gs = cell_groups[c]
        for i, g in enumerate(gs):
            key[g] = {'primary': c, 'secondaries': [],
                      'phase': 'BAC'[i % 3]}
    assert len(key) == 96

    def emit_group(c, pc, rstream):
        """Group for cell c occurring at occurrence-phase pc: the first
        alias with primary phase pc, with prob p_emit_phase; else a random
        alias (encipherer noise). Falls back to a random alias when the cell
        has no pc-phased alias (k<3)."""
        gs = cell_groups[c]
        cands = [g for g in gs if key[g]['phase'] == pc]
        if cands and rstream.random() < p['p_emit_phase']:
            return cands[0]
        return rstream.choice(gs)

    # ---- polyvalent islets: 6 mid-frequency groups, 1 secondary cell each ----
    # (secondary emission deliberately ignores phase: that impurity is real)
    prng = random.Random(seed + 777001)   # dedicated stream for the pilot
    pilot = []
    for (_, cells), pstart in zip(kept, _cumlen([len(c) for _, c in kept])):
        for k, c in enumerate(cells):
            pc = kept_pos[pstart + k]
            pilot.append(anchor_grp[c] if c in ANCHOR_CELLS
                         else emit_group(c, pc, prng))
    gfreq = collections.Counter(pilot)
    cand_groups = [g for g in labels
                   if gfreq[g] >= 15 and key[g]['primary'] not in ANCHOR_CELLS]
    cand_groups.sort(key=lambda g: -gfreq[g])
    pool = cand_groups[3:20]                     # mid-frequency band
    rng.shuffle(pool)
    islets = pool[:p['n_poly']]
    used_sec = set()
    cell_list = [c for c in inv_nonanchor if c not in used_sec]
    for g in islets:
        pc, pf = key[g]['primary'], kfreq[key[g]['primary']]
        cands = [c for c in cell_list
                 if c != pc and c not in ANCHOR_CELLS
                 and 0.5 * pf <= kfreq[c] <= 2.0 * pf]
        if not cands:
            continue
        sec = rng.choice(cands)
        key[g]['secondaries'] = [sec]
        used_sec.add(sec)
    n_islets = sum(1 for g in key if key[g]['secondaries'])
    sec_of = {}
    for g in key:
        for s in key[g]['secondaries']:
            sec_of[s] = g

    # ---- emission with per-position ground truth (full slice) ----
    full_pairs, full_planted, full_pclasses = [], [], []
    word_spans = []          # (start_pair, end_pair) per kept word
    crib_abs = None          # absolute pair offset of crib "la"
    for (wi, cells), pstart in zip(kept, _cumlen([len(c) for _, c in kept])):
        s0 = len(full_pairs)
        for k, c in enumerate(cells):
            if wi == crib_word_idx and k == 0:
                crib_abs = len(full_pairs)
            pc = kept_pos[pstart + k]
            if c in sec_of and rng.random() < p['p_poly_use']:
                g = sec_of[c]                # polyvalent emission (no phase)
            elif c in ANCHOR_CELLS:
                g = anchor_grp[c]
            else:
                g = emit_group(c, pc, rng)
            full_pairs.append(g)
            full_planted.append(c)
            full_pclasses.append(kept_pos[pstart + k])
        word_spans.append((s0, len(full_pairs)))
    assert crib_abs is not None
    # ---- coverage repair: every planted group must occur >=1 (the real
    # R5005's vocabulary is 96 groups by definition, incl. freq-1 groups).
    # Reassign one occurrence of the missing group's primary cell to it.
    # Documented distortion: a handful of pairs per instance at most.
    have = set(full_pairs)
    missing = [g for g in group_labels if g not in have]
    n_repaired = 0
    if missing:
        occ = collections.defaultdict(list)   # primary-cell occurrences
        occ_any = collections.defaultdict(list)  # any occurrence of the cell
        for i, (g, c) in enumerate(zip(full_pairs, full_planted)):
            occ_any[c].append(i)
            if key[g]['primary'] == c:
                occ[c].append(i)
        for g in missing:
            c = key[g]['primary']
            if occ[c]:
                i = rng.choice(occ[c])
            else:
                # cell's occurrences all went polyvalent: flip one back
                i = rng.choice(occ_any[c])
            full_pairs[i] = g
            n_repaired += 1
    # ---- window: exactly 1846 pairs, covering all 96 groups + the crib ----
    # minimal covering window of all 96 labels (sliding window), then place
    # the 1846-pair window deterministically (earliest feasible start).
    target = p['target_pairs']
    need = set(group_labels)
    cnt, have, left, best = collections.Counter(), 0, 0, None
    for right, g in enumerate(full_pairs):
        cnt[g] += 1
        if cnt[g] == 1:
            have += 1
        while have == 96:
            if best is None or right - left < best[1] - best[0]:
                best = (left, right)
            gl = full_pairs[left]
            cnt[gl] -= 1
            if cnt[gl] == 0:
                have -= 1
            left += 1
    if best is None or (best[1] - best[0] + 1) > target:
        return None  # stream too sparse for a covering 1846-window
    a, b = best
    L = b - a + 1
    lo = max(0, b + 1 - target, crib_abs - (target - 6))
    hi = min(a, crib_abs)
    if lo > hi:
        return None  # infeasible crib offset; caller tries the next one
    w0 = lo
    pairs = full_pairs[w0:w0 + target]
    planted = full_planted[w0:w0 + target]
    pclasses = full_pclasses[w0:w0 + target]
    crib_pair_offset = crib_abs - w0
    # the window may end mid-word (like the real CT's unknown end condition)
    we = next(i for i in range(len(word_spans))
              if word_spans[i][1] > w0 + target)
    truncated_mid = word_spans[we][0] < w0 + target < word_spans[we][1]
    assert len(pairs) == target and len(set(pairs)) == 96, \
        f"window broken: {len(pairs)} pairs, {len(set(pairs))} groups"

    # ---- crib reads exactly once ----
    hits = [i for i in range(len(planted) - 5)
            if planted[i:i + 6] == CRIB_CELLS]
    assert len(hits) == 1, f"crib reads {len(hits)}x, expected 1"
    assert hits[0] == crib_pair_offset, "crib offset mismatch"

    # ---- unsupervised rotation check (contactor method, copied) ----
    chi2 = unsupervised_chi2(pairs)

    # group phase diagnostics (planted labels; the solver never sees these)
    group_phase = {g: key[g]['phase'] for g in key}

    anchor_freqs = {g: pairs.count(g) for g in ANCHORS}
    if verbose:
        print(f"seed {seed}: T={T}->T_eff={T_eff} "
              f"occ_chi2={occurrence_chi2(pclasses):.1f} "
              f"unsup_chi2={chi2:.1f} keep={keep_rate:.2%} "
              f"islets={n_islets} crib@{crib_pair_offset} "
              f"repaired={n_repaired}")
    return {
        'seed': seed, 'T': T, 'T_eff': T_eff, 'pairs': pairs,
        'planted': planted,
        'pclasses': pclasses, 'key': key, 'group_phase': group_phase,
        'chi2': chi2, 'keep_rate': keep_rate, 'n_islets': n_islets,
        'scrubbed_premiere': scrubbed, 'crib_word_offset': crib_word_idx,
        'crib_pair_offset': crib_pair_offset,
        'anchor_freqs': anchor_freqs, 'truncated_mid_word': truncated_mid,
        'slice': [idx * sl, idx * sl + sl],
        'cover_len': L, 'n_coverage_repaired': n_repaired,
    }


def build_instance(seed, tokens, group_labels, p, T, verbose=False):
    """Try candidate crib offsets in order; first feasible build wins."""
    tried = []
    for co in p['crib_word_offsets']:
        inst = _try_build(seed, tokens, group_labels, p, T, co,
                          verbose=verbose)
        tried.append(co)
        if inst is not None:
            inst['crib_offsets_tried'] = tried
            return inst
    raise RuntimeError(f"seed {seed}: no feasible crib offset in {tried}")


def _cumlen(ns):
    out, s = [], 0
    for n in ns:
        out.append(s)
        s += n
    return out


# ------------------------- contactor-method chi2 (copied) ---------------------
def unsupervised_chi2(pairs):
    """Jaccard top-10 contact sets -> agglomerative avg-linkage -> k=12 cut ->
    3 largest clusters as A/B/C, rest R -> 3x3 block-transition chi2 (df=4).
    Method copied from code/crowd/contactor.py (which must not be re-run)."""
    groups = sorted(set(pairs))
    N = len(pairs)
    freq = collections.Counter(pairs)
    pred = collections.defaultdict(collections.Counter)
    foll = collections.defaultdict(collections.Counter)
    for i in range(N - 1):
        a, b = pairs[i], pairs[i + 1]
        foll[a][b] += 1
        pred[b][a] += 1
    K = 10
    top = {g: (set(h for h, _ in foll[g].most_common(K)) |
               set(h for h, _ in pred[g].most_common(K))) for g in groups}

    def jac(a, b):
        sa, sb = top[a], top[b]
        u = sa | sb
        return len(sa & sb) / len(u) if u else 0.0

    clusters = [{g} for g in groups]
    merges = []

    def avg(c1, c2):
        return sum(jac(a, b) for a in c1 for b in c2) / (len(c1) * len(c2))

    while len(clusters) > 1:
        best, bi, bj = -1.0, None, None
        for i in range(len(clusters)):
            for j in range(i + 1, len(clusters)):
                s = avg(clusters[i], clusters[j])
                if s > best:
                    best, bi, bj = s, i, j
        merges.append((sorted(clusters[bi]), sorted(clusters[bj])))
        new = clusters[bi] | clusters[bj]
        clusters = [c for k, c in enumerate(clusters) if k not in (bi, bj)] + [new]
    cs = [{g} for g in groups]
    for c1l, c2l in merges:
        if len(cs) <= 12:
            break
        c1, c2 = set(c1l), set(c2l)
        cs = [c for c in cs if c != c1 and c != c2] + [c1 | c2]
    cs = sorted(cs, key=len, reverse=True)
    block = {}
    for x, lbl in zip(cs[:3], 'ABC'):
        for g in x:
            block[g] = lbl
    rest = set().union(*cs[3:]) if len(cs) > 3 else set()
    for g in rest:
        block[g] = 'R'
    trans = collections.Counter()
    for i in range(N - 1):
        trans[(block[pairs[i]], block[pairs[i + 1]])] += 1
    cnt = {(r, c): trans[(r, c)] for r in 'ABC' for c in 'ABC'}
    r3 = {r: sum(cnt[(r, c)] for c in 'ABC') for r in 'ABC'}
    c3 = {c: sum(cnt[(r, c)] for r in 'ABC') for c in 'ABC'}
    n3 = sum(cnt.values())
    chi2 = sum((cnt[(r, c)] - r3[r] * c3[c] / n3) ** 2 / (r3[r] * c3[c] / n3)
               for r in 'ABC' for c in 'ABC' if r3[r] * c3[c] > 0)
    return round(chi2, 1)


# ------------------------- chance baseline (computed) -------------------------
def chance_baseline(inst, p):
    """Chance = random permutation of the 89 non-anchor primary cells over the
    89 non-anchor groups (anchors pinned, as the solver receives them).
    Analytic mean + Monte-Carlo (mc_draws) mean/sd, per metric.
    Metrics: PRIMARY = exact primary-cell recovery (89 groups);
             SECONDARY = token decode accuracy (1846 pairs)."""
    key, pairs, planted = inst['key'], inst['pairs'], inst['planted']
    nag = sorted(g for g in key if g not in ANCHORS)      # 89 non-anchor groups
    prim = [key[g]['primary'] for g in nag]              # multiset, size 89
    cnt = collections.Counter(prim)
    # analytic PRIMARY: sum_g count(primary_g)/89 / 89
    an_prim = sum(cnt[x] for x in prim) / 89.0 / 89.0
    # analytic SECONDARY: anchor positions auto-correct (given); else count/89
    n = len(pairs)
    anchor_pos = sum(1 for g in pairs if g in ANCHORS)
    an_sec = (anchor_pos + sum(cnt[c] / 89.0 for g, c in zip(pairs, planted)
                               if g not in ANCHORS)) / n
    rng = random.Random(10_000_000 + inst['seed'])
    mp, ms = [], []
    for _ in range(p['mc_draws']):
        perm = prim[:]
        rng.shuffle(perm)
        guess = dict(zip(nag, perm))
        mp.append(sum(1 for g, x in zip(nag, prim) if guess[g] == x) / 89.0)
        hit = anchor_pos
        for g, c in zip(pairs, planted):
            if g not in ANCHORS and guess[g] == c:
                hit += 1
        ms.append(hit / n)

    def stats(xs):
        m = sum(xs) / len(xs)
        v = sum((x - m) ** 2 for x in xs) / len(xs)
        return {'mean': m, 'sd': math.sqrt(v)}

    # oracle ceiling: planted single-cell-per-group key decode accuracy
    single = {g: key[g]['primary'] for g in key}
    oracle = sum(1 for g, c in zip(pairs, planted)
                 if single[g] == c) / n
    return {
        'primary': {'analytic': an_prim, **stats(mp)},
        'secondary': {'analytic': an_sec, **stats(ms)},
        'oracle_decode_accuracy': oracle,
        'mc_draws': p['mc_draws'],
    }


# ------------------------- writers -------------------------
def sha256_of(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        h.update(f.read())
    return h.hexdigest()


def write_instance(inst, p):
    seed = inst['seed']
    os.makedirs(OUTD, exist_ok=True)
    ct_path = os.path.join(OUTD, f"SYNTHETIC-ct-{seed}.pairs.txt")
    with open(ct_path, 'w') as f:
        f.write(HEADER)
        f.write(f"# seed={seed} pairs={len(inst['pairs'])} "
                f"groups={len(set(inst['pairs']))} SYNTHETIC\n")
        f.write(' '.join(inst['pairs']) + '\n')
    key_path = os.path.join(OUTD, f"SYNTHETIC-key-{seed}.json")
    json.dump({'seed': seed, 'synthetic': True,
               'SEALED': 'Runner scoring only. Never show to the solver. '
                         'This is a synthetic planted key, not real.',
               'key': inst['key'],
               'group_phase_diagnostic': inst['group_phase']},
              open(key_path, 'w'), indent=1, ensure_ascii=False)
    crib_path = os.path.join(OUTD, f"SYNTHETIC-crib-{seed}.json")
    json.dump({'seed': seed, 'synthetic': True,
               'note': 'Crib facts disclosed to the solver (mirrors the '
                       'erased-pencil cribs of R5005).',
               'anchors': ANCHORS,
               'crib_phrase_cells': CRIB_CELLS,
               'crib_word_offset': inst['crib_word_offset'],
               'crib_pair_offset': inst['crib_pair_offset'],
               'natural_premiere_scrubbed': inst['scrubbed_premiere']},
              open(crib_path, 'w'), indent=1, ensure_ascii=False)
    meta = {
        'seed': seed, 'synthetic': True,
        'generator': 'code/side-homophonic/control/generator.py',
        'params': {k: v for k, v in p.items()},
        'anchors': ANCHORS,
        'slice_word_offsets': inst['slice'],
        'T_inventory_nominal': inst['T'],
        'T_inventory_effective': inst['T_eff'],
        'n_pairs': len(inst['pairs']),
        'n_groups': len(set(inst['pairs'])),
        'keep_rate': round(inst['keep_rate'], 4),
        'n_polyvalent_islets': inst['n_islets'],
        'polyvalent_groups': sorted(g for g in inst['key']
                                    if inst['key'][g]['secondaries']),
        'occurrence_chi2': occurrence_chi2(inst['pclasses']),
        'unsupervised_chi2': inst['chi2'],
        'anchor_freqs_synthetic': inst['anchor_freqs'],
        'anchor_freqs_real_R5005': {'11': 44, '70': 15, '82': 38, '34': 10,
                                    '29': 47, '40': 21, '46': 29},
        'truncated_mid_word': inst['truncated_mid_word'],
        'sha256': {},
        'provenance': {
            'plaintext': 'data/gutenberg-17489-miserables1.txt (Les Miserables '
                         'T1, 1862; sha256 in data/SHA256SUMS.txt)',
            'syllabifier': 'code/crowd2/scorer_smith.py syllabify + '
                           'encipher_split (lane instruments)',
            'group_labels': 'identical 96 labels to R5005 '
                            '(data/attempt1_results.json via load_pairs)',
        },
    }
    for path in (ct_path, key_path, crib_path):
        meta['sha256'][os.path.basename(path)] = sha256_of(path)
    meta_path = os.path.join(OUTD, f"SYNTHETIC-meta-{seed}.json")
    json.dump(meta, open(meta_path, 'w'), indent=1, ensure_ascii=False)
    return meta


# ------------------------- calibration + build -------------------------
def occurrence_chi2(pclasses):
    """3x3 chi2 (df=4) of the occurrence-phase transition matrix."""
    trans = collections.Counter()
    for i in range(len(pclasses) - 1):
        trans[(pclasses[i], pclasses[i + 1])] += 1
    cnt = {(r, c): trans[(r, c)] for r in 'ABC' for c in 'ABC'}
    r3 = {r: sum(cnt[(r, c)] for c in 'ABC') for r in 'ABC'}
    c3 = {c: sum(cnt[(r, c)] for r in 'ABC') for c in 'ABC'}
    n3 = sum(cnt.values())
    return round(sum((cnt[(r, c)] - r3[r] * c3[c] / n3) ** 2 /
                     (r3[r] * c3[c] / n3)
                     for r in 'ABC' for c in 'ABC' if r3[r] * c3[c] > 0), 1)


def calibrate(p, tokens, group_labels):
    """Pilot q_cycle sweep on seed[0] (T fixed): pick q with occurrence-phase
    chi2 in band [181, 320], closest to band midpoint; deterministic. The
    occurrence-phase chi2 is T-independent (diluted cycle over kept cells),
    so q calibrates separately from the inventory knob T."""
    lo, hi = p['chi2_band']
    mid = (lo + hi) / 2
    rows = []
    T = 56
    for qc in p['q_cycle_candidates']:
        p['q_cycle'] = qc
        inst = build_instance(p['seeds'][0], tokens, group_labels, p, T)
        oc = occurrence_chi2(inst['pclasses'])
        rows.append({'q_cycle': qc, 'T': T, 'occurrence_chi2': oc,
                     'unsupervised_chi2': inst['chi2'],
                     'keep_rate': round(inst['keep_rate'], 4),
                     'n_islets': inst['n_islets']})
        print(f"  q={qc}: occurrence_chi2={oc} unsupervised_chi2={inst['chi2']} "
              f"keep={inst['keep_rate']:.2%} islets={inst['n_islets']}")
    inband = [r for r in rows if lo <= r['occurrence_chi2'] <= hi]
    if inband:
        best = min(inband, key=lambda r: abs(r['occurrence_chi2'] - mid))
    else:
        best = min(rows, key=lambda r: min(abs(r['occurrence_chi2'] - lo),
                                           abs(r['occurrence_chi2'] - hi)))
        print(f"WARNING: no q_cycle in occurrence-chi2 band {p['chi2_band']}; "
              f"closest q={best['q_cycle']} chi2={best['occurrence_chi2']} — "
              f"control REJECTED, do not certify")
    print(f"certified q_cycle={best['q_cycle']} "
          f"(occurrence_chi2={best['occurrence_chi2']})")
    json.dump({'band': p['chi2_band'], 'rows': rows,
               'certified_q_cycle': best['q_cycle'], 'T': T,
               'in_band': bool(inband)},
              open(os.path.join(HERE, 'calibration.json'), 'w'), indent=1)
    if not inband:
        sys.exit(2)
    return best['q_cycle'], T


def build_all(p):
    tokens = load_lesmis_tokens()
    group_labels = real_group_labels()
    print(f"lesmis tokens={len(tokens)} real groups={len(group_labels)}")
    q_cycle, T = calibrate(p, tokens, group_labels)
    p['q_cycle'] = q_cycle
    summary, chance = {}, {}
    for seed in p['seeds']:
        inst = build_instance(seed, tokens, group_labels, p, T, verbose=True)
        meta = write_instance(inst, p)
        cb = chance_baseline(inst, p)
        chance[str(seed)] = cb
        summary[str(seed)] = {
            'T': T, 'q_cycle': q_cycle,
            'occurrence_chi2': occurrence_chi2(inst['pclasses']),
            'unsupervised_chi2': inst['chi2'],
            'keep_rate': round(inst['keep_rate'], 4),
            'n_islets': inst['n_islets'],
            'crib_pair_offset': inst['crib_pair_offset'],
            'chance_primary_mean': round(cb['primary']['mean'], 5),
            'chance_primary_sd': round(cb['primary']['sd'], 5),
            'chance_secondary_mean': round(cb['secondary']['mean'], 5),
            'chance_secondary_sd': round(cb['secondary']['sd'], 5),
            'oracle_decode_accuracy': round(cb['oracle_decode_accuracy'], 5),
        }
        print(f"  seed {seed}: chance_primary={cb['primary']['mean']:.4f}±"
              f"{cb['primary']['sd']:.4f} chance_secondary="
              f"{cb['secondary']['mean']:.4f}±{cb['secondary']['sd']:.4f} "
              f"oracle={cb['oracle_decode_accuracy']:.4f}")
    json.dump(chance, open(os.path.join(HERE, 'chance_baseline.json'), 'w'),
              indent=1)
    json.dump({'certified_q_cycle': q_cycle, 'T': T, 'params': p,
               'instances': summary},
              open(os.path.join(HERE, 'build_summary.json'), 'w'), indent=1)
    print(f"built {len(summary)} instances; "
          f"files in {OUTD}")
    return summary


def self_test():
    """Rebuild seed[0] pilot in-memory and verify structural invariants."""
    p = dict(PARAMS)
    tokens = load_lesmis_tokens()
    group_labels = real_group_labels()
    inst = build_instance(p['seeds'][0], tokens, group_labels, p, 64)
    assert len(inst['pairs']) == 1846 and len(set(inst['pairs'])) == 96
    assert all(inst['key'][g]['primary'] == c for g, c in ANCHORS.items())
    assert inst['n_islets'] == p['n_poly'], \
        f"islets {inst['n_islets']} != {p['n_poly']}"
    cb = chance_baseline(inst, p)
    assert 0.0 < cb['primary']['mean'] < 0.06, cb['primary']
    print(f"self-test OK: chi2={inst['chi2']} islets={inst['n_islets']} "
          f"chance_primary={cb['primary']['mean']:.4f}")


if __name__ == '__main__':
    if '--self-test' in sys.argv:
        self_test()
    elif '--calibrate' in sys.argv:
        calibrate(PARAMS, load_lesmis_tokens(), real_group_labels())
    elif '--build-all' in sys.argv:
        build_all(PARAMS)
    else:
        print("usage: generator.py --calibrate | --build-all | --self-test")
        sys.exit(1)
