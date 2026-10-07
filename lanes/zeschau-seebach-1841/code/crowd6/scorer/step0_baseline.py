#!/usr/bin/env python3
"""STEP 0 — re-derive N36's baseline numbers on the CURRENT (old) objective.

Re-derives, before changing anything:
  (a) truth key vs annealed best on the old objective (lam_poly=10);
  (b) the lam_poly crossover (truth beats annealed only below lambda*);
  (c) the basin test (perturb truth, low-T descent, recovery count).

Writes step0_baseline.json. No repaired-objective code is touched.
"""
import collections
import json
import math
import os
import random
import sys
import time

LANE = os.path.expanduser('~/workspace/cipher-hunt/lanes/zeschau-seebach-1841')
for p in (os.path.join(LANE, 'code'),
          os.path.join(LANE, 'code', 'crowd2'),
          os.path.join(LANE, 'code', 'crowd4')):
    if p not in sys.path:
        sys.path.insert(0, p)
from scorer_smith import build_models  # noqa: E402
from joint_engine import (build_letter_ngram, build_inventory, JointModel,
                          PINS)  # noqa: E402

OUTD = os.path.join(LANE, 'code', 'crowd6', 'scorer')
SPAN = (40000, 41100)
SEED = 1841
OUTJ = os.path.join(OUTD, 'step0_baseline.json')
RES = {'SYNTHETIC': True, 'objective': 'OLD (raw letters, lam_rot=0)',
       'meta': {'seed': SEED, 'span': SPAN}}


def log(*a):
    print('[step0]', *a, flush=True)


def save():
    json.dump(RES, open(OUTJ, 'w'), indent=1)


log('loading control + era models...')
GT = json.load(open(os.path.join(LANE, 'code', 'crowd4',
                                 'control_ground_truth.json')))
GS, EMITTED, GI = GT['stream'], GT['emitted'], GT['group_info']
HINTS, ISLETS = GT['hints'], GT['islets']
M = build_models()
LP, _ = build_letter_ngram(M, n=7, exclude=SPAN)
CELLS, WEIGHTS = build_inventory(M)
CSET = set(CELLS)
BLOCK = {g: v['phase'] for g, v in GI.items()}


def make_model(lam_poly=10.0, seed=SEED):
    return JointModel(GS, BLOCK, LP, PINS, HINTS, CELLS, WEIGHTS,
                      0.0, lam_poly, 0.0, rng=random.Random(seed))


def truth_key(m, with_poly=True):
    for g in m.groups:
        m.v1[g] = GI[g]['primary']
        if with_poly and GI[g]['secondary']:
            m.v2[g] = GI[g]['secondary']
            m.w2[g] = GI[g]['w2']
        else:
            m.v2[g] = None
            m.w2[g] = 0.0
    m.pcell = list(EMITTED)
    m._refresh_scores()
    return m


def comps(m):
    return {'total': round(m.total(), 3),
            's_let': round(sum(m.lscore) / max(m.total_letters, 1), 4),
            'S_prior': round(m.S_prior, 2), 'n_poly': m.n_poly,
            'S_hom': round(m.S_hom, 2)}


# (a) truth vs annealed -------------------------------------------------------
log('(a) truth key components...')
m = make_model(10.0)
truth_key(m, True)
t10 = comps(m)
m0 = make_model(0.0)
truth_key(m0, True)
t0 = comps(m0)
log('truth lam=10:', t10)
log('truth lam=0 :', t0)

log('(a) annealing 3x600 sweeps (old objective, lam_poly=10)...')
t_start = time.time()
best_m, best_s, runs = None, float('-inf'), []
for rs in range(3):
    mm = make_model(10.0, seed=SEED + rs)
    res = mm.anneal(sweeps=600, T0=2.0, T1=0.02, seed=SEED + 100 + rs)
    runs.append({'restart': rs, 'best': round(res['best'], 3),
                 'acc': round(res['acc_rate'], 3),
                 'components': comps(mm)})
    log('  restart %d: best=%.3f' % (rs, res['best']))
    if res['best'] > best_s:
        best_s, best_m = res['best'], mm
RES['truth_vs_annealed'] = {'truth_lam10': t10, 'truth_lam0': t0,
                            'annealed_runs': runs,
                            'annealed_best': round(best_s, 3)}
save()

# (b) crossover ----------------------------------------------------------------
# s(truth; l) = T0 - 3*l ; s(abl; l) = A0 - n_abl*l
T0 = t0['total']
A0 = runs[0]['components']['total']  # placeholder, recompute properly below
# score the BEST annealed key at lam=0 for a clean A0
mA = make_model(0.0)
mA.v1, mA.v2, mA.w2 = dict(best_m.v1), dict(best_m.v2), dict(best_m.w2)
mA.pcell = list(best_m.pcell)
mA._refresh_scores()
A0 = mA.total()
n_abl = mA.n_poly
lam_star = (A0 - T0) / (n_abl - 3) if n_abl != 3 else float('nan')
RES['crossover'] = {'A0_annealed_lam0': round(A0, 4), 'n_poly_abl': n_abl,
                    'T0_truth_lam0': round(T0, 4), 'n_poly_truth': 3,
                    'lambda_star': round(lam_star, 4),
                    'interpretation': 'truth beats annealed best iff '
                                      'lam_poly < %.4f' % lam_star
                    if lam_star == lam_star else 'n/a'}
log('(b) crossover: lam* = %.4f (A0=%.3f n_abl=%d T0=%.3f)' % (
    lam_star, A0, n_abl, T0))
save()

# (c) basin test ----------------------------------------------------------------
log('(c) basin test: perturb truth, low-T descent...')


def descend(m, sweeps, T0_, T1_, seed):
    rng = random.Random(seed)
    m._recompute_all()
    for g in m.nonpin:
        if m.v2[g] is not None:
            m._rescore_group(g)
    m._refresh_scores()
    cur = m.total()
    best = cur
    cool = (T1_ / T0_) ** (1.0 / sweeps)
    T = T0_
    for _ in range(sweeps):
        order = m.nonpin[:]
        rng.shuffle(order)
        for g in order:
            mv, touched, snap = m.propose_move(g, rng)
            if mv == 'noop':
                continue
            new = m.total()
            d = new - cur
            if d >= 0 or rng.random() < math.exp(d / T):
                cur = new
                best = max(best, new)
            else:
                m.revert(snap)
        T *= cool
    return best


basin = []
for k in (5, 10, 20):
    for rep in range(3):
        mm = make_model(10.0, seed=SEED + 300 + rep)
        truth_key(mm, True)
        rng = random.Random(SEED + 400 + k * 10 + rep)
        pert = rng.sample([g for g in mm.nonpin if g not in ISLETS], k)
        for g in pert:
            mm._move_v1(g, mm.sample_cell(exclude=(mm.v1[g],)))
        end = descend(mm, 300, 0.3, 0.01, SEED + 500 + k * 10 + rep)
        got = sum(1 for g in pert if mm.v1[g] == GI[g]['primary'])
        basin.append({'k': k, 'rep': rep, 'recovered': got,
                      'end': round(end, 3)})
        log('  k=%d rep=%d: recovered %d/%d end=%.3f' % (k, rep, got, k, end))
tot_rec = sum(b['recovered'] for b in basin)
tot_pert = sum(b['k'] for b in basin)
RES['basin'] = {'detail': basin,
                'recovered': '%d/%d' % (tot_rec, tot_pert),
                'interpretation': 'basin EXISTS' if tot_rec / tot_pert > 0.5
                else 'NO basin around truth (landscape slopes away)'}
log('(c) basin: %d/%d recovered' % (tot_rec, tot_pert))
RES['meta']['elapsed_s'] = round(time.time() - t_start, 1)
save()
log('wrote step0_baseline.json')
