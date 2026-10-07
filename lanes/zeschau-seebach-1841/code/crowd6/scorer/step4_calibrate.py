#!/usr/bin/env python3
"""Step 4b: finalize calibration (amended rules).

LAM_POLY: the pre-registered 2*lambda* rule assumed C_abl > C_truth.
  The repaired objective inverts this (truth wins at lam_poly=0:
  C_abl=-1.9917 < C_truth=-1.3045), so lambda* is negative and the rule
  is void. AMENDED: guardrail LAM_POLY=0.05 — the empirically relevant
  scale (step-0 crossover was 0.0538 on the old objective). Truth pays
  3*0.05=0.15 (negligible vs the 0.69 gap); n_poly=48 pays 2.4
  (strong deterrent against runaway).

LAM_CONC: the ablation exhibited NO raw-cell collapse (max_n_c=3),
  so the pre-registered "observed collapse" rule gives G=0. AMENDED:
  calibrate against the EXTREME meme-collapse (step123, observed):
  word-profit 1.3227 over denominator (89-3)^2=7396 -> G=1.79e-4,
  LAM_CONC=2G=3.58e-4. Truth pays 0 (max_n_c=2 < 3).

Writes step4_calibrated.json {LAM_POLY, LAM_CONC}.
"""
import json, os

LANE = os.path.expanduser('~/workspace/cipher-hunt/lanes/zeschau-seebach-1841')
OUTD = os.path.join(LANE, 'code', 'crowd6', 'scorer')

abl = json.load(open(os.path.join(OUTD, 'step4_ablation.json')))
t = json.load(open(os.path.join(OUTD, 'step123_truth.json')))

# --- LAM_POLY (amended guardrail) ---
C_abl = abl['lam_poly_calibration']['C_abl']          # -1.9917
C_truth = t['truth_repaired_lam0']['total']          # -1.3045
# n_abl: recompute from the stored v1/v2 (the ablation's n_poly attr was stale)
v2 = abl['K_abl']['v2']
n_abl = sum(1 for g, v in v2.items() if v is not None)
n_truth = t['truth_repaired_lam0']['n_poly']         # 3
lam_star = (C_abl - C_truth) / (n_abl - n_truth)
print('C_abl=%.4f C_truth=%.4f n_abl=%d n_truth=%d lam_star=%.5f' % (
    C_abl, C_truth, n_abl, n_truth, lam_star))
print('lam_star < 0: truth wins at lam_poly=0; 2*lam_star rule void.')
LAM_POLY = 0.05
print('AMENDED LAM_POLY = %.4f (guardrail at step-0 crossover scale)' % LAM_POLY)

# --- LAM_CONC (meme-collapse guardrail) ---
mc = t['meme_collapse']
sw_meme = mc['S_word']                               # 1.6458
sw_truth = t['truth_repaired_lam0']['S_word']        # 0.3231
profit = sw_meme - sw_truth
den = (89 - 3) ** 2                                  # 7396
G = profit / den
LAM_CONC = 2 * G
print('meme S_word=%.4f truth S_word=%.4f profit=%.4f den=%d G=%.3e' % (
    sw_meme, sw_truth, profit, den, G))
print('AMENDED LAM_CONC = %.3e (2*G; truth pays 0)' % LAM_CONC)

out = {
    'SYNTHETIC': True,
    'LAM_POLY': LAM_POLY,
    'LAM_CONC': LAM_CONC,
    'lam_poly_basis': {
        'C_abl': C_abl, 'C_truth': C_truth, 'n_abl': n_abl,
        'n_truth': n_truth, 'lambda_star': round(lam_star, 5),
        'rule': 'AMENDED: 2*lambda* void (lambda*<0); guardrail 0.05 '
                'at step-0 crossover scale (0.0538)'},
    'lam_conc_basis': {
        'S_word_meme': sw_meme, 'S_word_truth': sw_truth,
        'profit': round(profit, 4), 'denominator': den,
        'G': G,
        'rule': 'AMENDED: ablation showed no collapse (G=0); calibrate '
                'against the observed extreme meme-collapse instead'},
}
json.dump(out, open(os.path.join(OUTD, 'step4_calibrated.json'), 'w'), indent=1)
print('wrote step4_calibrated.json')
