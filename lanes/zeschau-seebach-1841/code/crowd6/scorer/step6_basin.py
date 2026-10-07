#!/usr/bin/env python3
"""Step 6 (CONDITIONAL on C1): basin test on the REPAIRED objective.

Re-derives N36's basin test: low-temperature descents from perturbed
truth keys. If truth has a basin, descents return; if the landscape
slopes away, they don't.
"""
import sys, os, json, time, random, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from models import get_models
from objective import RepairedModel, PINS, LAM_WORD, LAM_ROT, BETA_PROV, CONC_CAP, N_GRAM

t0 = time.time()
def log(*a):
    print('[step6]', *a, flush=True)

M = get_models(verbose=False)
GT = M['GT']
GS = GT['stream']
HINTS = GT['hints']
BLOCK = {g: v['phase'] for g, v in GT['group_info'].items()}
GI = GT['group_info']

CAL = json.load(open('step4_ablate.json'))
LAM_POLY = CAL['LAM_POLY']
LAM_CONC = CAL['LAM_CONC']
log('LAM_POLY=%.4g LAM_CONC=%.4g' % (LAM_POLY, LAM_CONC))

def truth_key():
    v1 = {g: v['primary'] for g, v in GI.items()}
    v2 = {g: (v['secondary'] if v['secondary'] is not None else None)
          for g, v in GI.items()}
    w2 = {g: (v['w2'] if v['secondary'] is not None else 0.0)
          for g, v in GI.items()}
    return v1, v2, w2

def make_from_key(v1, v2, w2, seed):
    m = RepairedModel(GS, BLOCK, M['LP_PROJ'], PINS, HINTS, M['CELLS'],
                      M['WEIGHTS'], M['AC'], lam_poly=LAM_POLY,
                      lam_conc=LAM_CONC, lam_word=LAM_WORD, lam_rot=LAM_ROT,
                      beta_prov=BETA_PROV, conc_cap=CONC_CAP, n=N_GRAM,
                      rng=random.Random(seed))
    for g in GI:
        m.v1[g] = v1[g]
        m.v2[g] = v2[g]
        m.w2[g] = w2[g]
    m._recompute_all()
    m._refresh_scores()
    return m

def primary_match(m):
    """Fraction of non-pin groups where v1 == truth primary."""
    tv1, _, _ = truth_key()
    return sum(1 for g in m.nonpin if m.v1[g] == tv1[g]) / len(m.nonpin)

# low-T descents from perturbed truth
tv1, tv2, tw2 = truth_key()

def _nonpin():
    return [g for g in GI if g not in PINS]

rec_by_k = {}
for k in (5, 10, 20):
    n_trials = {5: 15, 10: 30, 20: 60}[k]
    rec = 0
    for trial in range(n_trials):
        rng = random.Random(7000 + k * 100 + trial)
        pv1 = dict(tv1)
        for g in rng.sample(_nonpin(), k):
            pv1[g] = rng.choice(M['CELLS'])
        m = make_from_key(pv1, tv2, tw2, seed=8000 + k * 100 + trial)
        # low-T descent: 200 sweeps at T=0.05
        m.anneal(sweeps=200, T0=0.05, T1=0.05, seed=9000 + k * 100 + trial,
                 log_every=0)
        pm = primary_match(m)
        # recovered if >= 90% of non-pin primaries match truth
        if pm >= 0.90:
            rec += 1
    rec_by_k[k] = {'recovered': rec, 'trials': n_trials}
    log('k=%d: %d/%d recovered' % (k, rec, n_trials))

total_rec = sum(v['recovered'] for v in rec_by_k.values())
total_n = sum(v['trials'] for v in rec_by_k.values())
has_basin = total_rec / total_n >= 0.5
OUT = {
    'SYNTHETIC': True,
    'by_k': rec_by_k,
    'total_recovered': '%d/%d' % (total_rec, total_n),
    'interpretation': ('Basin EXISTS around truth' if has_basin
                       else 'NO basin around truth (landscape slopes away)'),
    'elapsed_min': round((time.time() - t0) / 60, 1),
}
json.dump(OUT, open('step6_basin.json', 'w'), indent=1)
log('basin: %s | %s' % (OUT['total_recovered'], OUT['interpretation']))
