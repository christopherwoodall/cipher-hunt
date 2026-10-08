# PREREG — missing-mass inventory (council work order 6), 2026-10-07

## Objective
Turn "48 is unidentified" into "48 is the ne-class homophone" — priors by
elimination. Compute era syllable rates on the clean diplomatic corpus, compare
to observed rates of the 12 identified cells, and name the unidentified groups
that must be homophones by elimination (contact-profile match, ranked).

## Identified-cell inventory (fixed before any computation)
7 pencil GT: 11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que.
5 provisional: 87=ce, 64=qui, 96=par, 59=est, 77=le (conditioned).
Conditioned islets (84="en" iff pre=82, 06="ent" iff pre=82, 00="le" iff pre=96)
are WORD rules per the table-reconstructor §c — NOT counted as identified
cells in the observed sums.

## Method (pre-registered)
1. Repaired 1,847-pair stream via repair_parse.py logic (base offsets, a5_03=0).
2. French-only corpus files (German: metternich v4/v6, adb-zeschau, AZ x15;
   English: levant-correspondence excluded). French: guizot t1/t2/t3/t5-t6,
   nesselrode v7/v8/v9/v10, pozzo-di-borgo v1, revue-deux-mondes q1-q4,
   talleyrand v1.
3. Syllabifier: lane-established `code/side-keyhunt/build_syll_model.py::syllabify`
   (vowel-nucleus maximal-onset) — NOT hand-rolled; same segmentation the lane
   already uses. Top-15 syllables by era unigram rate.
4. Value→syllable keys: la→la, pre→pre, er→er, que→que, ce→ce, qui→qui,
   par→par, est→est, le→le. By-ear letter cells (m, i, e) map to standalone
   single-letter tokens in the corpus (low-confidence comparators, flagged).

## Pre-registered thresholds
- Mean cell rate: 1847/96 = 19.24 occurrences (fixed, computed from the stream).
- **FLAG threshold:** a syllable S is flagged as "missing homophone mass" iff
  (a) D_occ = (era_rate − observed_rate) × 1847 ≥ 19.24 (≥1 mean cell), AND
  (b) z = (obs − 1847×era_rate)/sqrt(1847×era_rate×(1−era_rate)) < −2.0
      (observed significantly BELOW era expectation).
- **STRONG threshold** (needed before naming ranked candidates): D_occ ≥ 38.5
  (≥2 cells) OR z < −3.0.
- Candidate ranking method (fixed): cosine similarity of the known cell's
  concatenated predecessor+successor contact vector vs every UNIDENTIFIED
  group's vector (recomputed from the repaired stream by this script — no
  values reused from prior agents' JSON). Phase coherence checked but not
  gating at this stage; reported per candidate.
- Negative/deficit-negative syllables (observed > era): report as "surplus"
  — possible causes (by-ear spelling inflation, value-specific frame
  concentration); NOT evidence of homophones.

## Digit hunt (secondary)
8 groups with n<5. Tests (pre-registered): (T1) digit-digit adjacency rate vs
  null (random-permutation control); (T2) contact with top-20 syllable cells —
  digits should show LOW mutual contact with the frequent-syllable core
  (dates sit outside grammatical frames); (T3) positional clustering in the
  first/last 5% of the stream (despatch date/salutation); (T4) contact-profile
  uniformity vs syllable-like profiles (the falsifier: syllable-like contact
  profiles ⇒ digit hypothesis fails).

## What this does NOT do
No value assignments. Output = ranked candidate lists (PRIORS), not promotions.
No coordinator bars applied; no adjudication — the red team owns verdicts.
