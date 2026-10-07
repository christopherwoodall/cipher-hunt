#!/usr/bin/env python3
"""Step 5: full synthetic control on the REPAIRED objective (pre-registered bars C1-C4).

Uses calibrated LAM_POLY/LAM_CONC from step4_ablate.json.
"""
import sys, os, json, time, math, random, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from models import get_models
from objective import (RepairedModel, PINS,
                       CONC_CAP, N_GRAM)
LAM_WORD, LAM_ROT = 1.0, 0.0

t0 = time.time()
def log(*a):
    print('[step5]', *a, flush=True)

M = get_models(verbose=False)
GT = M['GT']
GS = GT['stream']
HINTS = GT['hints']
BLOCK = {g: v['phase'] for g, v in GT['group_info'].items()}
GI = GT['group_info']
sfreq = collections.Counter(GS)
inv_set = set(M['CELLS'])

CAL = json.load(open('step4_calibrated.json'))
LAM_POLY = CAL['LAM_POLY']
LAM_CONC = CAL['LAM_CONC']
log('calibrated: LAM_POLY=%.4g LAM_CONC=%.4g' % (LAM_POLY, LAM_CONC))
assert LAM_POLY > 0 and LAM_CONC > 0, 'calibration failed'

def make(seed):
    return RepairedModel(GS, BLOCK, M['LP_PROJ'], PINS, HINTS, M['CELLS'],
                         M['WEIGHTS'], M['AC'], lam_poly=LAM_POLY,
                         lam_conc=LAM_CONC, lam_word=LAM_WORD,
                         lam_rot=LAM_ROT,
                         conc_cap=CONC_CAP, n=N_GRAM,
                         rng=random.Random(seed))

# truth on the repaired objective
# NOTE: pcell = EMITTED (actual plaintext), NOT [v1[g]].
# v1 holds codebook primaries (covered cells after tail inheritance);
# the truth DECODE is the emitted sequence. (step123_truth.py §truth.)
mt = make(0)
for g, v in GI.items():
    mt.v1[g] = v['primary']
    if v['secondary'] is not None:
        mt.v2[g], mt.w2[g] = v['secondary'], v['w2']
    else:
        mt.v2[g], mt.w2[g] = None, 0.0
mt.pcell = list(GT['emitted'])
mt._refresh_scores()
# E-step for polyvalent groups (true-history decode of the truth key)
for g in mt.nonpin:
    if mt.v2[g] is not None:
        mt._rescore_group(g)
truth_total = mt.total()
truth_c = mt.components()
log('truth on repaired objective: total=%.4f' % truth_total, truth_c)

# full anneal: 3 x 600 sweeps
best_m, best_s, runs = None, float('-inf'), []
for rs in range(3):
    m = make(184100 + rs)
    res = m.anneal(sweeps=600, T0=2.0, T1=0.02, seed=184100 + rs)
    runs.append({'restart': rs, 'best': round(res['best'], 4),
                 'acc_rate': round(res['acc_rate'], 3)})
    log('restart %d: best=%.4f acc=%.3f' % (rs, res['best'], res['acc_rate']))
    if res['best'] > best_s:
        best_s, best_m = res['best'], m

# marginals on the best
log('marginals (400 sweeps @ T=0.3)...')
marg = best_m.marginals(sweeps=400, T=0.3, seed=184877)

# C2: primary top-1 on 20 most frequent non-pin in-inventory groups
cands = [(g, n) for g, n in sfreq.most_common()
         if g not in PINS and GI[g]['primary'] in inv_set][:20]
hits, det = 0, []
for g, n in cands:
    top1 = marg[g][0][0] if marg[g] else None
    true = GI[g]['primary']
    ok = (top1 == true)
    hits += ok
    det.append({'group': g, 'n': n, 'true': true, 'top1': top1,
                'top1_p': round(marg[g][0][1], 3) if marg[g] else None,
                'hit': ok, 'kind': GI[g]['kind']})
pa = hits / len(cands)

# C3: islets — both true values in top-3 AND dominant #1
isl, isl_det = 0, []
for g, t in GT['islets'].items():
    top3 = [v for v, _ in marg[g][:3]]
    dom_first = bool(marg[g] and marg[g][0][0] == t['primary'])
    both = t['primary'] in top3 and t['secondary'] in top3
    ok = bool(both and dom_first)
    isl += ok
    isl_det.append({'group': g, 'primary': t['primary'],
                    'secondary': t['secondary'], 'w2_true': t['w2'],
                    'top5': [(v, round(p, 3)) for v, p in marg[g][:5]],
                    'both_in_top3': bool(both),
                    'dominant_first': dom_first, 'pass': ok})

# C4: pins intact + annealed beats random-20 baseline by >= 1.0
pins_ok = sum(1 for g, c in PINS.items() if best_m.v1[g] == c)
log('random-20 baseline...')
base_scores = []
for i in range(20):
    mb = make(9000 + i)
    mb.init_key()
    base_scores.append(mb.total())
base = sum(base_scores) / 20
margin = best_s - base

C1 = truth_total > best_s
C2 = pa >= 0.50
C3 = isl >= 2
C4 = (pins_ok == 7) and (margin >= 1.0)
verdict = C1 and C2 and C3 and C4

OUT = {
    'SYNTHETIC': True,
    'lam_poly': LAM_POLY, 'lam_conc': LAM_CONC,
    'runs': runs,
    'truth_total': round(truth_total, 4),
    'truth_components': truth_c,
    'annealed_best': round(best_s, 4),
    'annealed_components': best_m.components(),
    'random_baseline': round(base, 4),
    'C1_truth_beats_annealed': {'pass': bool(C1),
        'truth': round(truth_total, 4), 'annealed_best': round(best_s, 4),
        'gap': round(truth_total - best_s, 4)},
    'C2_primary_top1': {'pass': bool(C2), 'acc': round(pa, 4),
        'hits': '%d/%d' % (hits, len(cands)), 'detail': det},
    'C3_islets': {'pass': bool(C3), 'score': isl, 'detail': isl_det},
    'C4_pins_and_baseline': {'pass': bool(C4), 'pins': '%d/7' % pins_ok,
        'margin': round(margin, 4)},
    'verdict': 'CONTROL-PASS' if verdict else 'CONTROL-FAIL',
    'elapsed_min': round((time.time() - t0) / 60, 1),
}
json.dump(OUT, open('step5_control.json', 'w'), indent=1, ensure_ascii=False)
log('verdict: %s  C1=%s C2=%s(%.3f) C3=%s(%d/3) C4=%s(pins %d/7, margin %.2f)' % (
    OUT['verdict'], C1, C2, pa, C3, isl, C4, pins_ok, margin))
log('wrote step5_control.json in %.1f min' % OUT['elapsed_min'])
