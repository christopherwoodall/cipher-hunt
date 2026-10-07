# RATE-MODELER report — round-8 WO5 (00="pour" rate blockers B1/B3)

**Verdict: accept the strong-lead ceiling.** No rate-model repair reaches the bar.
One genuine partial repair found (H-LANG, language purity) that halves the reported
overs and should replace the standing figures. Residual quantified below.

## What was tried (all pre-registered in `code/crowd8/ratemodel/PREREG.md`)

| Repair | Model change | Result |
|---|---|---|
| H-LANG | French-only reference (drop English dilution) | r1 9.14×→**3.91×**, r3→**3.19×**. PARTIAL (bar was ≤2×) |
| H-SYLL | syllable-mass reference (pourquoi/pourtant/…) | r1_syll=**3.19×**. Contributes 1.23×. Not a repair |
| H-CLASS | pour-class numerator 52/1847 (drop 3 pre=96 le-windows) | 3.70×. Bookkeeping |
| H-DISP-B1 | point-rate → beta-binomial over 97 Nesselrode letters | rho=0.000, P(X≥55\|1847)≈**0.0**. FAILS decisively |
| H-DISP-B3 | same for 4/55 "pour que" | p=**0.0494** (< 0.05 bar). FAILS, borderline |
| n_eff | trigram-duplication collapse (F33 B5 style) | 47 distinct → floor 3.34×. Not a repair |

Combined floor (French pool + syllable ref + 52-class + trigram n_eff): **2.73×** —
still above the lane's 2× band.

## Key numbers

- Cipher: P(00)=55/1847=0.02978; pour-class 52/1847=0.02815.
- H-LANG French pool (97 Nesselrode-v8 letters + 746 levant French paragraphs):
  N=155,794, P("pour")=0.00761 → r1=**3.91×**; P("que"|"pour")=0.0228 → r3=**3.19×**.
- The 9.14× was ~57% English-dilution artifact: levant-correspondence-1841-p3 is
  majority-English (Parliamentary Papers); its English tokens inflated the
  denominator while "pour" counts came only from French enclosures. Tokenizer
  parity verified: my pipeline reproduces the conditioner's 9.14×/6.22×/3.85× exactly.
- French diplomatic "pour" rate is stable across independent sources:
  Nesselrode letters 0.00724 vs levant French paragraphs 0.00814 (within 12%).
- H-DISP-B1: 97 letters show ZERO overdispersion (rho=0.000); per-doc max
  P("pour")=0.0201 < cipher 0.0298; cipher at 100th percentile.
- Exploratory: 2,102 cipher-length (1847-token) chunks across all French
  diplomatic/literary files — **zero** reach 55 "pour"; max is 27.
- Cipher-side: 00s are UNDER-dispersed (index 0.47, uniform spread, not bursty);
  top repeated windows 63-00-66 ×4, 26-00-33 ×3 — mild formula repetition only.

## Recommendation

1. **Replace the standing blocker figures**: B1 9.14×→**3.91×**, B3→**3.19×**
   (French-only reference). The English-dilution component is dead.
2. **Accept the ceiling**: 00="pour" stays STRONG LEAD with B1/B3 standing as a
   real ~3-4× unigram over and a marginal ~2σ "pour que" excess (p≈0.036–0.049).
   The identification rests on the conditional-profile legs (B2a/B2b/B4/B5, all
   rivals dead), which are independent of the unigram rate — the residual is an
   unexplained over, not a kill-grade adverse.
3. **Do not pursue further rate-model repairs** on this lead without a new idea:
   the empirical chunk scan (0/2102) says no reference-tuning will close the gap.

## Caveats / follow-ups for other lanes

- B3's numerator (00→46 ×4) assumes 86∉que-family. If 86 were que-family,
  B3 dissolves (16/55=0.29 vs era 0.31). 86's identity is a closer-lane question.
- The lane's pairs↔words unit comparison is CONSERVATIVE: if cipher groups are
  sub-word (crib shows 6 groups/2 words), the true word-level over is LARGER
  than 3.91×. No repair hides in the unit conversion; it cuts the other way.
- PREREG deviations (recorded honestly): levant No.-documents abandoned as
  documents (mixed-language; replaced by 746 French-majority paragraphs in the
  pool only); dispersion fit uses the 97 Nesselrode letters alone.

## Artifacts

- `code/crowd8/ratemodel/PREREG.md` — pre-registration
- `code/crowd8/ratemodel/ratemodel.py` — battery (tokenizer parity-verified)
- `code/crowd8/ratemodel/ratemodel_results.json` — numbers
