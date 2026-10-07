#!/usr/bin/env python3
"""Diagnostic (runner/scorer role — READS the sealed planted key).

On ONE fresh instance (seed 184207):
  D1: truth's repaired-objective score vs 20 random keys (C1-analog setup).
  D2: truth's concentration profile (does truth violate the raw-cell cap 3?).
  D3: inventory coverage of truth primaries (D4-analog: which truth cells
      are absent from the 617-cell inventory).
  D4: truth components (s_let_proj, S_word, n_poly, ...).
  D5: quick SA (1 x 200 sweeps) best vs truth — the search gap preview.
"""
import collections
import json
import os
import random
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from harness import get_models, load_instance, make_model, FRESH_SEEDS  # noqa: E402
from objective import PINS  # noqa: E402

SEED = str(FRESH_SEEDS[0])
INST = os.path.join(HERE, 'fresh', 'instances')


def planted_key(seed):
    d = json.load(open(os.path.join(INST, 'SYNTHETIC-key-%s.json' % seed)))
    return d


def main():
    M = get_models(verbose=False)
    inst = load_instance(SEED)
    K = planted_key(SEED)
    key, planted = K['key'], K['planted']
    prim = {g: key[g]['primary'] for g in key}
    secs = {g: key[g]['secondaries'][0] if key[g]['secondaries'] else None
            for g in key}

    # truth model
    m = make_model(inst['stream'], seed=0)
    for g in m.groups:
        m.v1[g] = prim[g] if g not in PINS else PINS[g]
        s = secs[g]
        m.v2[g], m.w2[g] = (s, 0.5) if s else (None, 0.0)
    m.pcell = list(planted)  # per-position planted cells (KILL-2 field)
    m._refresh_scores()
    truth_total = m.total()
    truth_c = m.components()
    print('D4 truth components:', json.dumps(truth_c))

    # D2: concentration on truth
    n_c = collections.Counter(m.v1.values())
    print('D2 truth max_n_c=%d; over-cap cells: %s'
          % (max(n_c.values()),
             {c: n for c, n in n_c.items() if n > 3}))
    print('D2 truth S_conc=%.4f (must be 0 for the calibration to transfer)'
          % truth_c['S_conc'])

    # D3: inventory coverage
    inv = set(M['CELLS'])
    missing = sorted(set(prim[g] for g in m.nonpin if prim[g] not in inv))
    print('D3 truth primaries missing from inventory: %d %s'
          % (len(missing), missing))
    nmiss_groups = sum(1 for g in m.nonpin if prim[g] not in inv)
    print('D3 groups affected: %d/89' % nmiss_groups)

    # D1: 20 random keys
    base = []
    for i in range(20):
        mb = make_model(inst['stream'], seed=9000 + i)
        mb.init_key()
        base.append(mb.total())
    print('D1 truth=%.4f random20: max=%.4f mean=%.4f'
          % (truth_total, max(base), sum(base) / len(base)))

    # D5: quick SA preview
    mq = make_model(inst['stream'], seed=4242)
    res = mq.anneal(sweeps=200, T0=2.0, T1=0.02, seed=4242)
    print('D5 quick SA (1x200 sweeps): best=%.4f acc=%.3f  gap_to_truth=%.3f'
          % (res['best'], res['acc_rate'], truth_total - res['best']))

    json.dump({'seed': SEED, 'truth_total': round(truth_total, 4),
               'truth_components': truth_c,
               'truth_max_n_c': max(n_c.values()),
               'truth_S_conc': truth_c['S_conc'],
               'missing_primaries': missing,
               'groups_missing': nmiss_groups,
               'random20_max': round(max(base), 4),
               'random20_mean': round(sum(base) / len(base), 4),
               'quick_sa_best': round(res['best'], 4),
               'gap': round(truth_total - res['best'], 4)},
              open(os.path.join(HERE, 'diagnose.json'), 'w'), indent=1)


if __name__ == '__main__':
    main()
