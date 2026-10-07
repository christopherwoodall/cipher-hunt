#!/usr/bin/env python3
"""R5005 JOINT DECIPHERMENT RUN — round 4, WO8(d). CONTROL-GATED.

Refuses to run unless code/crowd4/control_results.json verdict is
CONTROL-PASS (N16 lesson: control-first is mandatory).

Uses the FROZEN config picked by the control ablation (lam_rot, lam_poly).
7 ground-truth pins hard; 5 provisionals as soft priors (87=ce, 64=qui,
96=par, 94=ne, 62=on). Banked Jaccard-k12 phases.

Outputs: r5005_results.json/.md with the best joint key, per-group marginals,
and LEADS (not promotions) for the contested groups
(62, 94, 06, 77, 78, 47, 64) with marginal confidences.
Promotion needs the >=2-check battery; the red team owns it.
"""

import collections
import json
import os
import random
import sys
import time

LANE = os.path.expanduser('~/workspace/cipher-hunt/lanes/zeschau-seebach-1841')
sys.path.insert(0, os.path.join(LANE, 'code'))
sys.path.insert(0, os.path.join(LANE, 'code', 'crowd2'))
sys.path.insert(0, os.path.join(LANE, 'code', 'crowd4'))
from repaired_parse import load_pairs_repaired  # noqa: E402
# REPAIRED canonical parse (2026-10-07): 1,847 pairs, offsets['a5_03'] 1->0
from scorer_smith import build_models  # noqa: E402
from joint_engine import (build_letter_ngram, build_inventory,
                          load_phase_map, JointModel, PINS,
                          PROVISIONAL)  # noqa: E402

OUTD = os.path.join(LANE, 'code', 'crowd4')
SEED = 1841
CONTESTED = ['62', '94', '06', '77', '78', '47', '64']
N_RESTARTS = 10
SWEEPS = 1500


def main():
    t0 = time.time()
    ctl = json.load(open(os.path.join(OUTD, 'control_results.json')))
    if ctl.get('verdict') != 'CONTROL-PASS':
        print('[GATE] control verdict is %r (need CONTROL-PASS). '
              'R5005 run REFUSED.' % ctl.get('verdict'))
        out = {'verdict': 'GATE-REFUSED',
               'control_verdict': ctl.get('verdict'),
               'note': 'Control did not pass; no R5005 run (WO8 gate).'}
        json.dump(out, open(os.path.join(OUTD, 'r5005_results.json'), 'w'),
                  indent=1)
        return
    lam_rot = ctl['picked']['lam_rot']
    lam_poly = ctl['picked']['lam_poly']
    print('[gate] control PASS; frozen config lam_rot=%.1f lam_poly=%.1f' % (
        lam_rot, lam_poly), flush=True)

    print('[models] building...', flush=True)
    M = build_models()
    lp, _ = build_letter_ngram(M, n=7)
    cells, weights = build_inventory(M, extra_cells=list(PROVISIONAL.values()))
    pairs, _, _ = load_pairs_repaired()
    assert len(pairs) == 1847 and len(set(pairs)) == 96
    phase = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                         'phase_map_repaired.json')))
    # RECOMPUTED Jaccard-k12 phases on the repaired 1,847-pair parse (2026-10-07).
    # Banked contactor phases (old parse) are stale: 61/96 groups change phase
    # under the repair (clustering sensitivity). Recomputed gives rotation
    # chi2=366.3 vs 178.8 banked — the repaired parse's rotation is STRONGER.
    print('  inventory=%d cells' % len(cells), flush=True)

    print('[anneal] %d restarts x %d sweeps...' % (N_RESTARTS, SWEEPS),
          flush=True)
    best_m, best_s = None, float('-inf')
    restarts = []
    for rs in range(N_RESTARTS):
        m = JointModel(pairs, phase, lp, PINS, PROVISIONAL, cells, weights,
                       lam_rot, lam_poly, rng=random.Random(SEED))
        res = m.anneal(sweeps=SWEEPS, T0=2.0, T1=0.02, seed=SEED + 1000 + rs)
        restarts.append({'restart': rs, 'best': round(res['best'], 1),
                         'acc': round(res['acc_rate'], 3)})
        print('    restart %d: best=%.1f acc=%.3f' % (
            rs, res['best'], res['acc_rate']), flush=True)
        if res['best'] > best_s:
            best_s, best_m = res['best'], m

    print('[marginals] 500 sweeps @ T=0.3...', flush=True)
    marg = best_m.marginals(sweeps=500, T=0.3, seed=SEED + 555)

    freq = collections.Counter(pairs)
    key = {g: {'v1': best_m.v1[g],
               'v2': best_m.v2[g],
               'w2': round(best_m.w2[g], 3)}
           for g in sorted(set(pairs))}
    n_poly = sum(1 for g in key if key[g]['v2'])

    def topk(g, k=6):
        return [(v, round(p, 3)) for v, p in marg[g][:k]]

    leads = {}
    for g in CONTESTED:
        leads[g] = {'n': freq[g], 'phase': phase[g],
                    'key_v1': key[g]['v1'], 'key_v2': key[g]['v2'],
                    'marginal_top6': topk(g),
                    'marginal_entropy': round(
                        -sum(p * __import__('math').log(p)
                             for _, p in marg[g] if p > 0), 3)}

    # full marginal table (compact): top-3 per group
    all_marg = {g: topk(g, 3) for g in sorted(set(pairs))}

    out = {
        'meta': {'seed': SEED, 'restarts': N_RESTARTS, 'sweeps': SWEEPS,
                 'lam_rot': lam_rot, 'lam_poly': lam_poly,
                 'pins': PINS, 'provisional_soft': PROVISIONAL,
                 'control_verdict': 'CONTROL-PASS',
                 'elapsed_s': round(time.time() - t0, 1)},
        'best_score': round(best_s, 1),
        'restarts': restarts,
        'n_polyvalent': n_poly,
        'key': key,
        'contested_leads': leads,
        'marginals_top3': all_marg,
        'note': ('LEADS ONLY — not promotions. Promotion needs the >=2-check '
                 'battery (red team). 87=ce, 64=qui, 96=par, 94=ne, 62=on '
                 'were soft priors, not pins.'),
    }
    json.dump(out, open(os.path.join(OUTD, 'r5005_results.json'), 'w'),
              indent=1, ensure_ascii=False)
    open(os.path.join(OUTD, 'r5005_results.md'), 'w').write(render_md(out))
    print('[done] wrote code/crowd4/r5005_results.{json,md} in %.0fs' % (
        time.time() - t0), flush=True)
    print('contested leads:', flush=True)
    for g in CONTESTED:
        d = leads[g]
        print('  g=%s (n=%d, phase=%s): key=%s%s marginal=%s' % (
            g, d['n'], d['phase'], d['key_v1'],
            ('/' + d['key_v2']) if d['key_v2'] else '',
            d['marginal_top6'][:3]), flush=True)


def render_md(out):
    L = []
    A = lambda *a: L.append(' '.join(str(x) for x in a))
    A('# JOINT ENGINE — R5005 RUN (WO8d, control-gated)')
    A()
    A('Control: **%s**; frozen config lam_rot=%.1f lam_poly=%.1f; '
      '%d restarts x %d sweeps; best score %.1f; %d polyvalent groups.' % (
          out['meta']['control_verdict'], out['meta']['lam_rot'],
          out['meta']['lam_poly'], out['meta']['restarts'],
          out['meta']['sweeps'], out['best_score'], out['n_polyvalent']))
    A()
    A('Pins (hard): 11=la 70=pre 82=m 34=i 29=er 40=e 46=que. '
      'Soft priors: 87=ce 64=qui 96=par 94=ne 62=on.')
    A()
    A('## Contested-group leads (LEADS ONLY — not promotions)')
    A()
    A('| group | n | phase | key v1/v2 | marginal top-6 (cell:prob) | entropy |')
    A('|---|---|---|---|---|---|')
    for g, d in out['contested_leads'].items():
        A('| %s | %d | %s | %s%s | %s | %.2f |' % (
            g, d['n'], d['phase'], d['key_v1'],
            ('/' + d['key_v2']) if d['key_v2'] else '',
            ', '.join('%s:%.2f' % (v, p) for v, p in d['marginal_top6']),
            d['marginal_entropy']))
    A()
    A('## Polyvalent groups in the best key')
    A()
    poly = [(g, k) for g, k in out['key'].items() if k['v2']]
    if poly:
        for g, k in sorted(poly):
            A('- g=%s: %s / %s (w2=%.2f)' % (g, k['v1'], k['v2'], k['w2']))
    else:
        A('(none — best key is single-valued throughout)')
    A()
    A('_Elapsed %.0fs. %s_' % (out['meta']['elapsed_s'], out['note']))
    return '\n'.join(L) + '\n'


if __name__ == '__main__':
    main()
