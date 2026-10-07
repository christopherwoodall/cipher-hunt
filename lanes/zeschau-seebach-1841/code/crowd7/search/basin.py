#!/usr/bin/env python3
"""Basin test on the REPAIRED objective (diagnostic role — reads sealed key).

Re-derives N36's basin test, which step6_basin.py never actually ran
(and step6 has a bug: anneal() calls init_key(), wiping the perturbed
start). Here: perturb truth v1 at k groups, then run a fixed-T Metropolis
descent FROM the perturbed state (no re-init). Recovery = >=90% of non-pin
primaries match truth after the descent.

If descents return to truth: basin EXISTS -> the search problem is global
navigation (population/ILS territory). If they walk away: NO basin ->
graduated optimization / coarse-to-fine territory.
"""
import json
import math
import os
import random
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from harness import get_models, load_instance, make_model, FRESH_SEEDS  # noqa: E402
from objective import PINS  # noqa: E402

SEED = str(FRESH_SEEDS[0])
INST = os.path.join(HERE, 'fresh', 'instances')


def truth_maps(seed):
    d = json.load(open(os.path.join(INST, 'SYNTHETIC-key-%s.json' % seed)))
    key = d['key']
    tv1 = {g: key[g]['primary'] for g in key}
    tv2 = {g: (key[g]['secondaries'][0] if key[g]['secondaries'] else None)
           for g in key}
    tw2 = {g: 0.5 if tv2[g] else 0.0 for g in key}
    return tv1, tv2, tw2, d['planted']


def descent(m, sweeps, T, seed):
    """Fixed-T Metropolis descent from the CURRENT state (no init_key)."""
    rng = random.Random(seed)
    cur = m.total()
    acc, moves = 0, 0
    for _ in range(sweeps):
        order = m.nonpin[:]
        rng.shuffle(order)
        for g in order:
            mv, touched, snap = m.propose_move(g, rng)
            if mv == 'noop':
                continue
            new = m.total()
            d = new - cur
            moves += 1
            if d >= 0 or rng.random() < math.exp(d / T):
                cur = new
                acc += 1
            else:
                m.revert(snap)
    return {'final': cur, 'acc_rate': acc / max(moves, 1)}


def primary_match(m, tv1):
    return sum(1 for g in m.nonpin if m.v1[g] == tv1[g]) / len(m.nonpin)


def main():
    get_models(verbose=False)
    inst = load_instance(SEED)
    tv1, tv2, tw2, planted = truth_maps(SEED)
    cells = None

    # truth score (reference)
    m0 = make_model(inst['stream'], seed=0)
    for g in m0.groups:
        m0.v1[g] = tv1[g] if g not in PINS else PINS[g]
        m0.v2[g], m0.w2[g] = (tv2[g], 0.5) if tv2[g] else (None, 0.0)
    m0.pcell = list(planted)
    m0._refresh_scores()
    truth_total = m0.total()
    print('[basin] truth total=%.4f' % truth_total, flush=True)

    out = {'seed': SEED, 'truth_total': round(truth_total, 4), 'by_k': {}}
    for k in (5, 10, 20):
        rec, rows = 0, []
        for trial in range(3):
            rng = random.Random(7000 + k * 100 + trial)
            pv1 = dict(tv1)
            pert = rng.sample([g for g in tv1 if g not in PINS], k)
            m = make_model(inst['stream'], seed=8000 + k * 100 + trial)
            if cells is None:
                cells = m.cells
            for g in m.groups:
                m.v1[g] = pv1[g] if g not in PINS else PINS[g]
                m.v2[g], m.w2[g] = (tv2[g], 0.5) if tv2[g] else (None, 0.0)
            for g in pert:
                m.v1[g] = rng.choice(cells)
            m._recompute_all()
            m._refresh_scores()
            start_total = m.total()
            start_pm = primary_match(m, tv1)
            res = descent(m, sweeps=200, T=0.05,
                          seed=9000 + k * 100 + trial)
            end_pm = primary_match(m, tv1)
            ok = end_pm >= 0.90
            rec += ok
            rows.append({'trial': trial, 'start_total': round(start_total, 4),
                         'start_pm': round(start_pm, 4),
                         'end_total': round(res['final'], 4),
                         'end_pm': round(end_pm, 4),
                         'recovered': bool(ok)})
            print('[basin] k=%d trial=%d start=%.3f(pm=%.3f) -> '
                  'end=%.3f(pm=%.3f) %s'
                  % (k, trial, start_total, start_pm, res['final'], end_pm,
                     'RECOVERED' if ok else 'walked-away'), flush=True)
        out['by_k'][str(k)] = {'recovered': '%d/3' % rec, 'trials': rows}
    json.dump(out, open(os.path.join(HERE, 'basin.json'), 'w'), indent=1)
    print('[basin] wrote basin.json', flush=True)


if __name__ == '__main__':
    main()
