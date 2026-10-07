# RATE-MODELER — round-8 work order 5 — PRE-REGISTRATION (written BEFORE any new computation, 2026-10-07)

Standing: canonical parse repaired 1,847-pair (`code/side-keyhunt/repaired_offsets.json`);
positions per `code/crowd4/REINDEX.md`; n00=55 (bedrock-corrected); P(00)=55/1847=0.02978.
00="pour" STRONG LEAD with blockers B1 (unigram 6.22× Tocq / 9.14× despatches-primary)
and B3 ("pour que" 3.85× Tocq; diplomatic no better). Conditioned polyvalence stands
(F54): 00="le" iff pre=96 (3 windows @48/466/961), 00="pour" elsewhere (52 windows).
Tokenizer parity with conditioner: lower, '→space elision split, [a-zà-ÿ]+.

## Repair hypotheses (each a model change, not a re-description)

### H-LANG — language-purity repair (NEW, discovered in corpus audit)
The levant file (levant-correspondence-1841-p3.txt, British Parliamentary Papers) is
majority-ENGLISH (spot check: ~27.9k English markers vs ~1.7k French markers). The
conditioner's pooled "despatches-primary" denominator mixes English parliamentary
boilerplate into N while "pour" counts come only from French enclosures — mechanically
DEFLATING P("pour") and inflating r1. Model change: split despatches-primary into
natural documents, keep French-majority documents only, recompute r1/r3 on the French
pool.
- REPAIRED iff r1_french = P(00)/P_french("pour") ≤ 2× (lane band; raw ratios reported
  alongside per F20's uncalibrated-band rule). Partial credit: report Δr1 vs 9.14×.

### H-DISP-B1 — document-dispersion null for B1 (model change: point-rate → beta-binomial)
The point-rate null treats all tokens as i.i.d. draws with book-level p. A single
70-line letter is one document; the honest null lets p vary by document. Fit a
beta-binomial (method of moments) to per-document ("pour", N) counts over
French-majority despatches-primary documents (nesselrode-v8 letters +
French levant No.-documents). Test the cipher: P(X ≥ 55 | n=1847).
- REPAIRED iff p_value ≥ 0.05 (over not significant under document-level burstiness).
- Supporting: report observed max per-document P("pour") and cipher's percentile.

### H-DISP-B3 — document-dispersion null for B3
Same documents: per-document ("pour que", "pour") counts; beta-binomial test of
cipher k=4 "pour que" out of n=55 "pour" (parity with recorded B3; 4/52 pour-class
reported alongside).
- REPAIRED iff p_value ≥ 0.05.

### H-SYLL — syllable-mass repair (bounded expectation)
The cipher is a syllabary; if 00="pour" is a syllable-group, word-level P("pour")
undercounts the reference (pourquoi/pourtant/pourparlers…).
Recompute r1_syll = P(00)/P(token begins with "pour") on French despatches-primary.
- REPAIRED iff r1_syll ≤ 2×. (Prior: contributes ≤1.5× — expected to FAIL alone;
  measured to bound its contribution, not to carry the repair.)

### H-CLASS — conditioned-class numerator bookkeeping (not a repair)
Under F54 polyvalence the "pour"-class is 52 windows (drop 3 pre=96). Report
r1 on 52/1847. Expected movement 9.14×→~8.6×: bookkeeping, not a repair.

## Document definitions (fixed before fitting)
- levant: split on /^No\.\s*\d+/ markers → documents. Classify French-majority by
  stopword-marker vote (French set vs English set); ties/near-ties (ratio within
  2×) → excluded from fit, counted in report.
- nesselrode-v8: split on letter-header date lines (Saint-Pétersbourg/Berlin/Paris/
  Vienne + 1840–46 date pattern, OCR-tolerant); fallback: inspect and record the
  actual header pattern before splitting. Documents < 40 words excluded from the
  beta-binomial fit (reported).
- guizot/talleyrand/metternich/pozzo/revue volumes NOT in the fit (C1's primary is
  despatches-only; volumes are not letters).

## Cipher-side supporting check (not a repair)
Clustering of the 55 00-positions: index of dispersion across 20 equal blocks +
top-3 block concentrations. Bursty 00s support the dispersion story; uniform 00s
weaken it.

## Decision tree
- Any H REPAIRED ⇒ recommend the repaired model to red team (rate blockers
  dissolved under the repaired null; 00="pour" STRONG LEAD stands unblocked).
- H-LANG partial (moves r1 ≥ 2× toward 1 but not ≤2×) + H-DISP passes ⇒ recommend
  accepting the strong-lead ceiling with the residual quantified as document-level
  burst variance, not a point-rate over.
- All fail ⇒ recommend accepting the ceiling honestly: 00="pour" stays STRONG LEAD
  with B1/B3 standing as unexplained overs (residual: r1=9.14× point-rate,
  p_disp as measured).
No status change without red-team ruling. No claim without ≥2 independent checks.
