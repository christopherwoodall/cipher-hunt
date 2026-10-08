#!/usr/bin/env python3
"""Track B step 8: neural three-way rescore + verdict.

1. Sanity gates (5-gram, verifier code):
   a. truth 5-gram E-step decode == track-c/decodes.json['truth']['text'] (byte-exact)
   b. frozen salad verifier parts reproduce CLOSING-VERIFICATION §2 within 0.1 nats
   (halt on mismatch)
2. Instrument gate: neural held-out per-char logp >= 5-gram held-out per-char
   logp on the identical held-out stream.
3. Neural rescore: S_neural(truth) vs S_neural(frozen) vs S_neural(adapted);
   M_frozen, M_adapted; verdict per PREREG §1.
4. Full-J substitution iff SUCCESS.

Deterministic. NO R5005 contact.
"""
import json
import math
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
REBUILD = os.path.join(LANE, 'code', 'side-homophonic-rebuild')

sys.path.insert(0, os.path.join(REBUILD, 'solver'))
sys.path.insert(0, os.path.join(REBUILD, 'verifier'))
sys.path.insert(0, HERE)
from rescore import Rescorer, CharLM, project, load_pairs, load_truth  # noqa: E402
import train_lm  # noqa: E402 (data pipeline + model class)

SEED = '184101'


# ------------------------------------------------------------ neural scoring
def load_net():
    blob = np.load(os.path.join(HERE, 'model.npz'))
    V, H = int(blob['V']), int(blob['H'])
    net = train_lm.CharLSTM(V, H, seed=0)
    net.set_params({k: blob[k] for k in net.pnames})
    return net


def step_logps(net, ids, h, c):
    """Run ids (list of int) from (h,c); return (logps per char, h', c')."""
    x = np.array(ids, dtype=np.int32).reshape(-1, 1)
    logp, _, (h2, c2) = net.forward(x, h, c)
    lp = [float(logp[t, 0, ids[t]]) for t in range(len(ids))]
    return lp, h2, c2


def s_neural(net, pcell_ids):
    """S_neural = sum over pairs of per-pair per-char rate (streaming state)."""
    h, c = net.zero_state(1)
    # zero-state output distribution for the very first char
    z0 = net.by.astype(np.float64)
    z0 -= z0.max()
    e0 = np.exp(z0)
    logp0 = z0 - math.log(e0.sum())
    total = 0.0
    first = True
    for v in pcell_ids:
        if not v:
            continue  # parity with CharLM.F: empty cb contributes 0.0
        if first:
            lp = [logp0[v[0]]]
            _, h, c = step_logps(net, v[:1], h, c)
            if len(v) > 1:
                lp2, h, c = step_logps(net, v[1:], h, c)
                lp += lp2
            first = False
        else:
            lp, h, c = step_logps(net, v, h, c)
        total += sum(lp) / len(v)
    return total


def estep_neural(net, v1_raw, v2_raw, w2_init, groups, pairs, c2i):
    """Neural E-step: 10-sweep left-to-right fixpoint; choice by neural rate."""
    p1 = {g: project(v1_raw[g]) for g in groups}
    p2 = {g: (project(v2_raw[g]) if v2_raw.get(g) else None) for g in groups}
    i1 = {g: [c2i[ch] for ch in p1[g]] for g in groups}
    i2 = {g: ([c2i[ch] for ch in p2[g]] if p2[g] else None) for g in groups}
    pcell = [p1[g] for g in pairs]
    for _ in range(10):
        moved = False
        h, c = net.zero_state(1)
        new_cell = []
        for t, g in enumerate(pairs):
            if i2[g] is None:
                choice, ci = p1[g], i1[g]
            else:
                w = min(max(w2_init.get(g, 0.0), 1e-6), 1 - 1e-6)
                lp1, _, _ = step_logps(net, i1[g], h.copy(), c.copy())
                lp2, _, _ = step_logps(net, i2[g], h.copy(), c.copy())
                r1 = sum(lp1) / len(lp1) + math.log(1 - w)
                r2 = sum(lp2) / len(lp2) + math.log(w)
                choice, ci = (p2[g], i2[g]) if r2 > r1 else (p1[g], i1[g])
            if choice != pcell[t]:
                moved = True
            new_cell.append(choice)
            _, h, c = step_logps(net, ci, h, c)
        pcell = new_cell
        if not moved:
            break
    return pcell


# ------------------------------------------------------------ verifier parts on a pcell
def full_parts(r, cfg, pcell, v1_raw, v2_raw):
    s = ''.join(pcell)
    S_cov = r._cover_sum(s, cfg['word_minlen'])
    S_single = sum(r.lex_wt.get(p, 0.0) for p in pcell)
    cnt = {}
    for g in r.groups:
        f = project(v1_raw[g])
        cnt[f] = cnt.get(f, 0) + 1
    cap = cfg['conc_cap']
    S_conc = sum((n - cap) ** 2 for n in cnt.values() if n > cap)
    seen = set()
    S_potts = 0.0
    for g in r.groups:
        for hh, j in r.phase['adj'][g]:
            key = (g, hh) if g < hh else (hh, g)
            if key in seen:
                continue
            seen.add(key)
            if v1_raw[g] == v1_raw[hh]:
                S_potts += r.beta * j
    n_poly = sum(1 for g in r.groups if v2_raw.get(g) is not None)
    return {'S_cov': S_cov, 'S_single': S_single, 'S_word': S_cov - S_single,
            'S_potts': S_potts, 'S_conc': S_conc, 'n_poly': n_poly,
            'decode_len': len(s)}


def main():
    pairs = load_pairs(SEED)
    cfg = json.load(open(os.path.join(REBUILD, 'solver', 'config.json')))
    r = Rescorer(pairs, cfg)
    groups = r.groups
    lm_meta = json.load(open(os.path.join(
        REBUILD, 'solver', 'lm_ref', 'lm.json')))['meta']
    c2i = {ch: i for i, ch in enumerate(lm_meta['alphabet'])}

    # ---- load the three assignments ----
    truth_key = load_truth(SEED)
    v1_truth = {g: truth_key[g]['primary'] for g in groups}
    v2_truth = {g: (truth_key[g]['secondaries'][0]
                    if truth_key[g].get('secondaries') else None)
                for g in groups}
    w2_truth = {g: (0.5 if v2_truth[g] else 0.0) for g in groups}

    pilot = json.load(open(os.path.join(
        REBUILD, 'pilot', 'rebuild-pilot-final', 'result.json')))
    fr = [x for x in pilot['restarts'] if x['seed'] == 199939][0]
    assert all(a['v2'] is None for a in fr['assignment'].values()), 'not npoly=0'
    v1_frozen = {g: fr['assignment'][g]['v1'] for g in groups}
    v2_frozen = {g: None for g in groups}

    ad = json.load(open(os.path.join(HERE, 'adapted_salad.json')))
    v1_adapted = ad['v1']
    v2_adapted = {g: None for g in groups}

    out = {'sanity': {}, 'instrument': {}, 'margins': {}}

    # ---- sanity gate (a): truth 5-gram decode reproduction ----
    dec = json.load(open(os.path.join(
        LANE, 'code', 'side-homophonic-rebuild2', 'track-c', 'decodes.json')))
    res5 = r.score(dict(v1_truth),
                   {g: v2_truth[g] for g in groups},
                   dict(w2_truth), label='truth-5gram')
    match = res5['decode'] == dec['truth']['text']
    out['sanity']['truth_decode_byte_exact'] = bool(match)
    print(f"[sanity-a] truth 5-gram decode reproduces track-c: {match}",
          flush=True)
    if not match:
        print('[sanity-a] MISMATCH — halt', flush=True)
        sys.exit(11)

    # ---- sanity gate (b): frozen salad verifier parts ----
    f5 = r.score(dict(v1_frozen), dict(v2_frozen), {}, label='frozen-5gram')
    ref = {'S_char': -3325.69, 'S_word': 1021.91, 'total': -2352.3}
    got = {'S_char': round(f5['S_char'], 2), 'S_word': round(f5['S_word'], 2),
           'total': round(f5['total'], 1)}
    ok = all(abs(f5[k] - v) <= 0.1 for k, v in ref.items())
    out['sanity']['frozen_parts'] = got
    out['sanity']['frozen_parts_match'] = bool(ok)
    print(f"[sanity-b] frozen verifier parts: {got} match={ok}", flush=True)
    if not ok:
        print('[sanity-b] MISMATCH — halt', flush=True)
        sys.exit(12)

    # ---- instrument gate ----
    net = load_net()
    tr_lines, ho_lines, _, _ = train_lm.build_lines()
    Harr = train_lm.words_to_ids(ho_lines, c2i)
    i2c = {i: ch for ch, i in c2i.items()}
    chars = ''.join(i2c[int(i)] for i in Harr)
    clm = CharLM(json.load(open(os.path.join(
        REBUILD, 'solver', 'lm_ref', 'lm.json'))))
    tot5, n5 = 0.0, 0
    for i, ch in enumerate(chars):
        tot5 += clm.logp(ch, chars[max(0, i - 4):i])
        n5 += 1
    fivegram_held = tot5 / n5
    manif = json.load(open(os.path.join(HERE, 'manifest.json')))
    neural_held = -manif['training']['final_heldout_nll']
    gate = neural_held >= fivegram_held
    out['instrument'] = {'neural_heldout_logp': round(neural_held, 4),
                         'fivegram_heldout_logp': round(fivegram_held, 4),
                         'gate_pass': bool(gate)}
    print(f"[instrument] neural={neural_held:.4f} 5gram={fivegram_held:.4f} "
          f"pass={gate}", flush=True)

    # ---- neural three-way rescore ----
    def pcell_ids_of(pcell):
        return [[c2i[ch] for ch in v] for v in pcell]

    pc_truth = estep_neural(net, v1_truth, v2_truth, w2_truth, groups, pairs, c2i)
    pc_frozen = estep_neural(net, v1_frozen, v2_frozen, {}, groups, pairs, c2i)
    pc_adapt = estep_neural(net, v1_adapted, v2_adapted, {}, groups, pairs, c2i)
    S_truth = s_neural(net, pcell_ids_of(pc_truth))
    S_frozen = s_neural(net, pcell_ids_of(pc_frozen))
    S_adapt = s_neural(net, pcell_ids_of(pc_adapt))
    M_frozen = S_truth - S_frozen
    M_adapted = S_truth - S_adapt
    out['margins'] = {
        'S_neural_truth': round(S_truth, 1),
        'S_neural_frozen': round(S_frozen, 1),
        'S_neural_adapted': round(S_adapt, 1),
        'M_frozen': round(M_frozen, 1),
        'M_adapted': round(M_adapted, 1),
        'decode_lens': {'truth': len(''.join(pc_truth)),
                        'frozen': len(''.join(pc_frozen)),
                        'adapted': len(''.join(pc_adapt))}}
    print(f"[neural] truth={S_truth:.1f} frozen={S_frozen:.1f} "
          f"adapted={S_adapt:.1f}", flush=True)
    print(f"[neural] M_frozen={M_frozen:.1f} (bar +1000) "
          f"M_adapted={M_adapted:.1f} (bar +300)", flush=True)

    # ---- verdict (PREREG §1, exact) ----
    strawman = bool(ad['strawman'])
    if M_frozen >= 1000 and M_adapted >= 300 and gate and not strawman:
        verdict = 'SUCCESS'
    elif gate and not strawman and (M_frozen < 0 or M_adapted < 0):
        verdict = 'FAIL'
    else:
        verdict = 'INCONCLUSIVE'
    out['verdict'] = verdict
    out['strawman'] = strawman
    print(f'[verdict] {verdict} (gate={gate} strawman={strawman})', flush=True)

    # ---- full-J substitution iff SUCCESS ----
    if verdict == 'SUCCESS':
        J = {}
        for name, pc, v1r, v2r, Sn in (
                ('truth', pc_truth, v1_truth, v2_truth, S_truth),
                ('frozen', pc_frozen, v1_frozen, v2_frozen, S_frozen),
                ('adapted', pc_adapt, v1_adapted, v2_adapted, S_adapt)):
            fp = full_parts(r, cfg, pc, v1r, v2r)
            J[name] = round(Sn + fp['S_word'] + fp['S_potts']
                            - 50 * fp['n_poly'] - 5 * fp['S_conc'], 1)
            fp['S_neural'] = round(Sn, 1)
            out.setdefault('fullJ', {})[name] = fp
        out['fullJ']['J_neural'] = J
        print(f"[fullJ] truth={J['truth']} frozen={J['frozen']} "
              f"adapted={J['adapted']}", flush=True)

    json.dump(out, open(os.path.join(HERE, 'neural_rescore.json'), 'w'), indent=1)
    lines = ['# Track B neural rescore — RESULTS', '',
             f'verdict: **{verdict}**', '',
             '| decode | S_neural |',
             '|---|---|',
             f"| truth | {S_truth:.1f} |",
             f"| frozen salad | {S_frozen:.1f} |",
             f"| adapted salad | {S_adapt:.1f} |",
             f"| M_frozen (bar +1000) | {M_frozen:.1f} |",
             f"| M_adapted (bar +300) | {M_adapted:.1f} |",
             f"| instrument gate (neural {neural_held:.4f} vs 5-gram {fivegram_held:.4f}) | {gate} |",
             f"| adapted strawman | {strawman} |"]
    if verdict == 'SUCCESS':
        lines += ['', 'Full-J substitution (neural LM for S_char):',
                  f"truth {J['truth']}, frozen {J['frozen']}, adapted {J['adapted']}"]
    open(os.path.join(HERE, 'RESULTS.md'), 'w').write('\n'.join(lines) + '\n')
    print('[done] neural_rescore.json RESULTS.md written', flush=True)


if __name__ == '__main__':
    main()
