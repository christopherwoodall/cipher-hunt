#!/usr/bin/env python3
"""BASELINE search: the frozen round-6 annealer on fresh control instances.

Replicates code/crowd6/scorer/step5_control.py's search exactly:
  3 restarts x 600 sweeps, T0=2.0 -> T1=0.02 (geometric), single-group
  moves via the parent propose_move (chg1/swap/poly/chg2), best-state
  retention. Frozen objective hyperparameters from step4_calibrated.json.

Usage: python3 baseline.py <seed>   (one instance per process)
Output: runs/baseline/asg-<seed>.json  {v1, v2, best, seed, ...}
The key files are NEVER read here.
"""
import json
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from harness import get_models, load_instance, make_model  # noqa: E402

OUTD = os.path.join(HERE, 'runs', 'baseline')
os.makedirs(OUTD, exist_ok=True)

SWEEPS, RESTARTS = 600, 3
T0, T1 = 2.0, 0.02
BASE_SEED = 184100  # same restart seeds as step5 (comparability)


def run(seed):
    t0 = time.time()
    get_models(verbose=False)
    inst = load_instance(seed)
    best_m, best_s, runs = None, float('-inf'), []
    for rs in range(RESTARTS):
        m = make_model(inst['stream'], seed=BASE_SEED + rs)
        res = m.anneal(sweeps=SWEEPS, T0=T0, T1=T1, seed=BASE_SEED + rs)
        runs.append({'restart': rs, 'best': round(res['best'], 4),
                     'acc_rate': round(res['acc_rate'], 3)})
        print('[baseline %s] restart %d: best=%.4f acc=%.3f (%.0fs)'
              % (seed, rs, res['best'], res['acc_rate'], time.time() - t0),
              flush=True)
        if res['best'] > best_s:
            best_s, best_m = res['best'], m
    # exact resync before reading the best key (paranoia about drift)
    best_m._refresh_scores()
    exact = best_m.total()
    out = {'method': 'baseline-SA-3x600', 'seed': str(seed),
           'SYNTHETIC': True,
           'anneal_restart_seeds': [BASE_SEED + r for r in range(RESTARTS)],
           'sweeps': SWEEPS, 'restarts': RESTARTS, 'T0': T0, 'T1': T1,
           'runs': runs, 'best_tracked': round(best_s, 4),
           'best_exact_resync': round(exact, 4),
           'components': best_m.components(),
           'v1': dict(best_m.v1),
           'v2': {g: v for g, v in best_m.v2.items() if v is not None},
           'elapsed_min': round((time.time() - t0) / 60, 1)}
    json.dump(out, open(os.path.join(OUTD, 'asg-%s.json' % seed), 'w'))
    print('[baseline %s] wrote asg-%s.json best=%.4f exact=%.4f in %.1f min'
          % (seed, seed, best_s, exact, out['elapsed_min']), flush=True)


if __name__ == '__main__':
    run(sys.argv[1])
