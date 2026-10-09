# Battery report — linebreak-repeat-audit

Worker: battery-worker-linebreak-repeat-audit (agent 70a2bc1d-aa6c-44f8-bc12-25848e6e5398).
Date: 2026-10-09.
Lock: `code/crowd17/next-token/locks/linebreak-repeat-audit.lock` created
2026-10-09T18:02:10Z, no prior lock existed; deleted on completion.
Stream: repaired 1,847-pair / 96-type parse (`code/side-keyhunt/repaired_offsets.json` +
`data/upstream-ct_R5005.txt`), parsed per `code/side-keyhunt/repair_parse.py`
(asserts re-run in-session: 1847 pairs, 96 types, 70 rows). `canonical.py` never
used. R5005, sealed gate instances, and the red-team adjudication queue untouched.

## Bar (pre-registered verbatim, from battery-queue.json)

"rate of line-start == previous line-end across all 69 row breaks vs 1/96 chance
(binomial, lane standard), including the line-start == line-end-minus-1 variant.
Pass iff enriched -> reclassify both as candidate scribal repeats; fail -> fence
dittography for both"

Numbered clauses (fixed before testing):
- C1 (main): rate of `first(row N+1) == last(row N)` across all 69 breaks is
  enriched vs binomial(n=69, p=1/96) at lane standard (one-sided p < 0.05).
- C2 (variant): rate of `first(row N+1) == second-to-last(row N)` across all 69
  breaks is enriched vs binomial(n=69, p=1/96) at lane standard (one-sided
  p < 0.05).
- C3 (decision): pass iff C1 or C2 enriched → reclassify @589 and @1637 as
  candidate scribal repeats; fail → fence scribal dittography for both loci.

## Method

Re-derived the repaired stream in-session (asserts held). Enumerated all 69 row
breaks independently. For each break recorded the main trial
(`new[0] == old[-1]`) and the variant trial (`new[0] == old[-2]`). Binomial
p-values computed analytically at p=1/96 (lane standard). For the combined
main-OR-variant pattern, empirical p-values from 100,000 Monte Carlo replicates
under two nulls: uniform-over-96 and empirical marginal cell frequencies, with
the observed row-length structure preserved.

## Window-level evidence (@-offsets are repaired-stream 0-based pair indices)

Main hits (2/69):
- break#20, a3_02|a4_00, new row @590: old row ends `...97, 41`; new row starts
  `41, 09`. Straddling doublet @589|590 = 41|41 (the doublet-41-589 locus).
- break#61, a8_03|a8_04, new row @1638: old row ends `...87, 74`; new row starts
  `74, 35`. Straddling doublet @1637|1638 = 74|74.

Variant hits (1/69):
- break#49, a7_03|a7_04, new row @1305: old row ends `...43, 21`; new row starts
  `43, 77`. `new[0]=43 == old[-2]=43`. Neither of the two straddling doublets
  fires the variant trial (@589: 41 != 97; @1637: 74 != 87).

## Per-clause pass/fail

- C1 (main enrichment): FAIL. 2/69 vs 0.72 expected; P(X≥2 | n=69, p=1/96) =
  0.1618. Not enriched at lane standard. (Independently replicates the parent
  battery's 2/69 count and p≈0.17.)
- C2 (variant enrichment): FAIL. 1/69 vs 0.72 expected; P(X≥1 | n=69, p=1/96) =
  0.5145. Not enriched.
- C3 (decision): FAIL arm fires → scribal dittography FENCED for both loci.
  Combined main-OR-variant: 3/69 breaks; empirical P(C≥3) = 0.1749
  (uniform-96 null) and 0.3277 (marginal-frequency null) — consistent with
  chance under both nulls.

## Verdict: KILL

The scribal-dittography rival for the two straddling doublets is rejected at
the lane's distributional standard. The line-break repeat rate is not enriched
(main p=0.16, variant p=0.51, combined empirical p=0.17–0.33); both straddles
(@589|590 = 41|41, @1637|1638 = 74|74) are consistent with chance and must be
read as genuine stream content, not scribal error. The variant trial surfaced
one new line-start repeat (break#49, 43-pattern) that is likewise
chance-consistent; it is recorded, not pursued.

## Scope

Kills only the dittography reading of the two straddling doublets. Does not
decide what @589|590 or @1637|1638 ARE (word doubling, geminate boundary, and
syllable-doubling readings for 41|41 remain the doublet-41-589 NULL's live
options); it only removes the "the scribe repeated a group across the line
break" escape hatch. No standing or red-team verdict contradicted; §7 intact.
Adverses: none listed on target.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-linebreak-repeat-audit.md`
- Queue: `linebreak-repeat-audit` → `status: verdict`, `result: kill`, 2026-10-09
  (pre-write assert passed — was queued/verdictless; temp-file + rename; disk
  re-validated; own entry only; no downgrade)
- Lock created on start, deleted on completion (verified gone).
- Analysis script: inline in this report's Method (re-runnable from the lane's
  data + repaired_offsets.json).
