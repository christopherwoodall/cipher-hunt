#!/usr/bin/env python3
"""C1-analog on two more fresh instances (diagnostic role — reads sealed keys).

Truth total vs 5 random-key totals on the repaired objective, with the
S_word component broken out (is the word bonus also register-blind?).
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from harness import get_models, load_instance, make_model, FRESH_SEEDS  # noqa: E402
from objective import PINS  # noqa: E402

INST = os.path.join(HERE, 'fresh', 'instances')
out = {}


def truth_total(seed):
    inst = load_instance(seed)
    K = json.load(open(os.path.join(INST, 'SYNTHETIC-key-%s.json' % seed)))
    key, planted = K['key'], K['planted']
    m = make_model(inst['stream'], seed=0)
    for g in m.groups:
        prim = key[g]['primary']
        m.v1[g] = prim if g not in PINS else PINS[g]
        secs = key[g]['secondaries']
        m.v2[g], m.w2[g] = (secs[0], 0.5) if secs else (None, 0.0)
    m.pcell = list(planted)
    m._refresh_scores()
    return m.total(), m.components()


def main():
    get_models(verbose=False)
    for seed in [str(s) for s in FRESH_SEEDS[1:3]]:
        tt, tc = truth_total(seed)
        rnd = []
        for i in range(5):
            mb = make_model(load_instance(seed)['stream'], seed=31000 + i)
            mb.init_key()
            rnd.append((mb.total(), mb.components()['S_word']))
        print('[c1x2] seed %s: truth=%.4f (S_word=%.4f, n_poly=%d) | '
              'random5 max=%.4f mean=%.4f (S_word max=%.4f)'
              % (seed, tt, tc['S_word'], tc['n_poly'],
                 max(r[0] for r in rnd), sum(r[0] for r in rnd) / 5,
                 max(r[1] for r in rnd)), flush=True)
        out[seed] = {'truth': round(tt, 4), 'truth_S_word': tc['S_word'],
                     'truth_n_poly': tc['n_poly'],
                     'random5_max': round(max(r[0] for r in rnd), 4),
                     'random5_mean': round(sum(r[0] for r in rnd) / 5, 4)}
    json.dump(out, open(os.path.join(HERE, 'c1x2.json'), 'w'), indent=1)


if __name__ == '__main__':
    main()
