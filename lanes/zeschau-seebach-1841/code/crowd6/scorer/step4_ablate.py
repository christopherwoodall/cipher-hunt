#!/usr/bin/env python3
"""STEP 4a — ablation anneal: repaired objective, LAM_POLY=0, LAM_CONC=0.

Per PREREG.md: the unpenalized optimum K_abl calibrates both
  LAM_POLY = 2 * (C_abl - C_truth)/(n_abl - 3)   [truth wins iff lam > lam*]
  LAM_CONC = 2 * G, G = word-profit rate of the observed collapse
(no truth labels in either rule).

Writes step4_ablation.json with K_abl's key, components, and the
calibrated LAM_POLY / LAM_CONC values.
"""
import collections
import json
import os
import random
import sys
import time

LANE = os.path.expanduser('~/workspace/cipher-hunt/lanes/zeschau-seebach-1841')
sys.path.insert(0, os.path.join(LANE, 'code', 'crowd6', 'scorer'))
from models import get_models  # noqa: E402
from objective import RepairedModel, PINS, SEED  # noqa: E402

OUTD = os.path.join(LANE, 'code', 'crowd6', 'scorer')
OUTJ = os.path.join(OUTD, 'step4_ablation.json')
RES = {'SYNTHETIC': True,
       'design': 'repaired objective, LAM_POLY=0, LAM_CONC=0, LAM_WORD=1.0, '
                 'LAM_ROT=0.0; 3 restarts x 600 sweeps'}


def log(*a):
    print('[step4a]', *a, flush=True)


M = get_models(verbose=False)
GT = M['GT']
GS, EMITTED, GI = GT['stream'], GT['emitted'], GT['group_info']
HINTS, ISLETS = GT['hints'], GT['islets']
BLOCK = {g: v['phase'] for g, v in GI.items()}


def make(lam_poly=0.0, lam_conc=0.0, seed=SEED):
    return RepairedModel(GS, BLOCK, M['LP_PROJ'], PINS, HINTS, M['CELLS'],
                         M['WEIGHTS'], M['AC'], lam_word=1.0, lam_rot=0.0,
                         lam_poly=lam_poly, lam_conc=lam_conc,
                         rng=random.Random(seed))


t0 = time.time()
log('ablation: 3 x 600 sweeps, lam_poly=0, lam_conc=0 (first log after ~6 min)')
best_m, best_s, runs = None, float('-inf'), []
for rs in range(3):
    m = make(seed=SEED + rs)
    res = m.anneal(sweeps=600, T0=2.0, T1=0.02, seed=SEED + 100 + rs)
    c = m.components()
    runs.append({'restart': rs, 'best': round(res['best'], 4),
                 'acc': round(res['acc_rate'], 4), 'components': c})
    log('restart %d: best=%.4f n_poly=%d S_word=%.4f max_n_c=%d' % (
        rs, res['best'], c['n_poly'], c['S_word'],
        max(collections.Counter(m.v1.values()).values())))
    if res['best'] > best_s:
        best_s, best_m = res['best'], m
RES['runs'] = runs
RES['K_abl'] = {'total': round(best_s, 4),
                'components': best_m.components(),
                'n_poly': best_m.n_poly,
                'v1': dict(best_m.v1), 'v2': dict(best_m.v2),
                'w2': {g: round(w, 3) for g, w in best_m.w2.items()}}
n_c = collections.Counter(best_m.v1.values())
RES['K_abl']['raw_concentration_top10'] = n_c.most_common(10)
RES['K_abl']['sum_max0_n_minus_3_sq'] = sum(
    max(0, n - 3) ** 2 for n in n_c.values())

# truth components on the repaired objective (lam_poly=0 part)
t = json.load(open(os.path.join(OUTD, 'step123_truth.json')))
C_truth = t['truth_repaired_lam0']['total']  # lam_poly=0 -> C_truth
n_truth = t['truth_repaired_lam0']['n_poly']
C_abl = best_s
n_abl = best_m.n_poly
lam_star = (C_abl - C_truth) / (n_abl - n_truth) if n_abl != n_truth else float('nan')
lam_poly = 2 * lam_star
RES['lam_poly_calibration'] = {
    'C_abl': round(C_abl, 4), 'n_abl': n_abl,
    'C_truth': round(C_truth, 4), 'n_truth': n_truth,
    'lambda_star': round(lam_star, 5),
    'LAM_POLY': round(lam_poly, 5),
    'rule': 'LAM_POLY = 2*lambda_star (truth wins iff lam_poly > lambda_star)',
}

# LAM_CONC calibration: deconcentrate K_abl, measure the word-profit rate
log('deconcentrating K_abl for the LAM_CONC calibration...')
rng = random.Random(7)
decon_v1 = dict(best_m.v1)
over = [g for g in best_m.nonpin if n_c[best_m.v1[g]] > 3]
for g in over:
    decon_v1[g] = rng.choice(M['CELLS'])
m2 = make()
m2.v1, m2.v2, m2.w2 = decon_v1, dict(best_m.v2), dict(best_m.w2)
m2._recompute_all()
m2._refresh_scores()
# E-step for polyvalent groups (true-history decode with the new v1)
for g in m2.nonpin:
    if m2.v2[g] is not None:
        m2._rescore_group(g)
c2 = m2.components()
sw_abl = best_m.components()['S_word']
sw_decon = c2['S_word']
den = sum(max(0, n - 3) ** 2 for n in n_c.values())
G = (sw_abl - sw_decon) / den if den else 0.0
lam_conc = 2 * G
RES['lam_conc_calibration'] = {
    'n_overcap_groups_reassigned': len(over),
    'S_word_abl': round(sw_abl, 4), 'S_word_decon': round(sw_decon, 4),
    'denominator': den, 'G': round(G, 6), 'LAM_CONC': round(lam_conc, 6),
    'rule': 'LAM_CONC = 2*G, G = word-profit rate of the observed collapse',
    'decon_total': round(c2['total'], 4),
}
RES['meta'] = {'elapsed_s': round(time.time() - t0, 1)}
json.dump(RES, open(OUTJ, 'w'), indent=1)
log('LAM_POLY=%.5f LAM_CONC=%.6f' % (lam_poly, lam_conc))
log('wrote step4_ablation.json in %.0fs' % (time.time() - t0))
