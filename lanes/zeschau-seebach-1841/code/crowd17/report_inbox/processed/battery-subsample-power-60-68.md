# Battery report — subsample-power-60-68 (n=7 power calibration for the {60,68} pair)

Worker: fd852974-fc6f-41a3-bfc0-5a2c627d7468. Date: 2026-10-08.
Lock: `code/crowd17/next-token/locks/subsample-power-60-68.lock` created
2026-10-08T20:10:06Z; no prior lock existed; deleted on completion.
Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` +
`data/upstream-ct_R5005.txt`), parsed per `code/side-keyhunt/repair_parse.py`.
`canonical.py` not used. R5005 not touched. Sealed gates, red-team
adjudication queue untouched. No invented numbers: every count below was
re-derived from the stream in this run (script: worker-local, seed 20261008).

## HEADLINE — predecessor p-value in the prior battery is miscomputed; escalated to red team

Re-deriving the thirds-60-68-pair battery's permutation test exposed a
cross-column threshold bug in that battery's predecessor p-value: the reported
predecessor p=0.0546 is P(null predecessor TV >= 0.9412) — i.e. it was computed
against the SUCCESSOR observed statistic (0.9412), not the predecessor observed
statistic (1.0000). Recomputed correctly, the predecessor p is ≈0.032
(0.0313–0.0330 across 5 seeds at B=20,000), which REJECTS at α=0.05. The
successor p re-derives clean (0.0517–0.0548 vs reported 0.0552; no bug there).
This correction undermines that battery's clause-1 pass ("meets the {33,86}
indistinguishability standard on successors AND predecessors") — the
predecessor side does not meet it. This report does NOT re-adjudicate the pair;
it escalates the correction to the red team and proposes a re-run follow-up
below (F1). This worker's own verdict stays null per its bar (see below).

## Bar (verbatim, from battery-queue.json)

"(a) 10,000 draws of 7 tokens from 60's 17 free tokens, each draw
permutation-tested against the remaining 60 tokens (same TV/B=20,000 method)
— report the rejection rate at α=0.05; (b) if >=80% of draws fail to reject,
the null is a power artifact and the pair stays null-but-live; if the draws
usually reject, 68 patterns genuinely differently from 60 -> kill-grade
against the pair."

Numbered clauses (pre-registered BEFORE testing, not modified after):

1. (a) 10,000 draws of 7 tokens from 60's 17 free tokens, each draw
   permutation-tested against the remaining 60 tokens with the same
   TV/B=20,000 method; report the rejection rate at α=0.05.
2. (b) If >=80% of draws fail to reject, the null is a power artifact and the
   pair stays null-but-live; if the draws usually reject, 68 patterns
   genuinely differently from 60 -> kill-grade against the pair.

Interpretation note (not a bar change): "the remaining 60 tokens" is read as
the 10 tokens of 60 not drawn (disjoint remainder); each draw is a 7-vs-10
label permutation test, the same test family as the original 17-vs-7.

## Method

Same stream and exclusions as the thirds-60-68-pair battery: 60's free tokens
are the 17 occurrences of "60" excluding formula-bound @232; windows quoted at
repaired-stream pair indices. Each draw: sample 7 of the 17 free-60 tokens
without replacement; the remaining 10 form the comparison group. Test: total
variation distance TV = 0.5*sum|p-q| on the successor empirical distributions
(resp. predecessor), labels permuted B=20,000 preserving cell counts (7/10),
p=(ge+1)/(B+1), α=0.05, fixed seed 20261008. A draw "rejects" if either side
rejects (mirrors the original bar's AND-logic: homophony needed both sides to
not reject). Equivalence used: conditional on the fixed pooled 17-token
multiset, the permutation reference distribution is IDENTICAL for every draw,
so one multivariate-hypergeometric reference per side is exact (equal to
re-permuting per draw). Sanity: the original 60-vs-68 successor test
re-derives to obs TV=0.9412, p≈0.052 (reported 0.0552); predecessor to obs
TV=1.0000, p≈0.032 (reported 0.0546 — the bug documented above).

## Window-level evidence (@-offsets, repaired stream)

60's 17 free windows (index: predecessor / successor):
@119: 21/90; @172: 21/09; @197: 21/08; @322: 92/15; @454: 77/65; @637: 46/67;
@690: 29/03; @700: 94/12; @995: 03/67; @1338: 64/08; @1366: 14/03;
@1474: 53/06; @1563: 06/71; @1644: 98/03; @1674: 92/03; @1690: 14/27;
@1735: 06/12.
Successor multiset: 03x4, 08x2, 67x2, 12x2, 90/09/15/65/06/71/27 x1.
Predecessor multiset: 21x3, 92x2, 14x2, 06x2, 77/46/29/94/03/64/53/98 x1.
68's 7 free windows (for the correction evidence): @114 (pred 89), @504 (pred
39), @884 (pred 79), @1286 (pred 55), @1384 (pred 65), @1442 (pred 52),
@1719 (pred 47) — seven disjoint singleton predecessors, zero type-overlap
with 60's predecessor set.

Exemplar draws:
- Reject-type draw #4972 (p_suc=0.0101, p_pre=0.0211): drawn @322 @454 @690
  @1366 @1644 @1674 @1690; drawn successors {03x4, 15, 27, 65}; drawn
  predecessors {14x2, 29, 77, 92x2, 98}. Rejection happens when a draw
  concentrates a repeated type (here all four 60->03 tokens).
- Typical draw #8740 (p_suc=0.1910, p_pre=0.8724): drawn @119 @454 @995 @1366
  @1474 @1644 @1674; successors {03x3, 06, 65, 67, 90}; predecessors
  {03, 14, 21, 53, 77, 92, 98}. Fails to reject on both sides.

## Results (10,000 draws, seed 20261008; robustness seeds 555, 987654321)

| metric | seed 20261008 | seed 555 | seed 987654321 |
|---|---|---|---|
| successor-side rejection rate | 2.27% (227) | 2.09% | 1.86% |
| predecessor-side rejection rate | 2.57% (257) | 2.96% | 2.55% |
| either-side rejection rate | 4.71% (471) | 4.95% | 4.29% |
| both-sides rejection rate | 0.13% (13) | — | — |
| fail-to-reject rate (either side) | 95.29% | 95.05% | 95.71% |

p-value quantiles (seed 20261008): successor 5/25/50/75/95 =
0.053/0.253/0.510/0.752/0.985; predecessor = 0.056/0.341/0.557/0.801/0.974.
The p-value distribution is near-uniform with mild conservatism (discrete
statistic), exactly the signature of a test with no power at this n.

## Per-clause pass/fail

1. **(a) PASS.** 10,000 draws executed per the bar; rejection rates reported
   above at α=0.05 with the same TV/B=20,000 method.
2. **(b) PASS — power-artifact arm.** Fail-to-reject rate 95.29% (robust:
   95.05–95.71% across 3 seeds) is far above the 80% bar. The n=7 sample
   cannot discriminate even 60's own tokens from the rest of 60: the test
   has essentially no power at this n. Per the bar, the null is a power
   artifact and the pair stays null-but-live.

## Adverses (fenced, never ignored)

- "subsample draws are not independent of the full set" — STATED as required.
  All 10,000 draws reuse the same fixed 17-token pool, so draws overlap heavily
  across iterations: the 95.29% rate is a descriptive Monte Carlo property of
  this pool, not an estimate from 10,000 independent samples, and its sampling
  uncertainty is understated if treated as i.i.d. Within each draw the 7/10
  groups partition the pool (negatively dependent by construction); the
  permutation reference conditions on exactly this structure, so per-draw
  p-values are valid — only the aggregate rate inherits the pool-reuse
  dependence. The rate is also conditional on 60's observed multisets: it
  measures "can n=7 detect 60's own internal structure," not "can n=7 detect
  68's difference from 60" (a different alternative).
- Scope fence: this battery calibrates power only; it does not re-adjudicate
  the {60,68} pair — the predecessor p-value correction above is escalated,
  not decided here.

## Verdict: NULL

The claim is supported for the successor side: the p≈0.053 successor
non-rejection is exactly what n=7 produces ~95% of the time even when the two
groups come from the same cell — a power artifact, not evidence about 68's
class. Per bar (b) the pair stays null-but-live on this battery's authority.
The predecessor side is a separate matter: correctly computed it rejects
(p≈0.032), which contradicts the prior battery's clause-1 basis — escalated
to the red team, not decided here. No red-team verdict is contradicted by
this battery's own verdict (the pair battery is battery-decided, and its
re-adjudication is proposed as F1).

## Follow-ups for the supervisor (nulls regenerate work)

### F1. pair-60-68-readjudicate — priority 1
- **claim:** "The {60,68} 2-cell homophone claim fails the {33,86}
  indistinguishability standard on predecessors (corrected p≈0.032 < 0.05)."
- **bars:** (a) re-run the thirds-60-68-pair bar (a) with the corrected
  predecessor p-value (obs TV=1.0000, p≈0.032, B=20,000, same method);
  (b) adjudicate: predecessor rejection at α=0.05 is kill-grade against the
  2-cell claim under that battery's own bar, or state the red-team reason it
  is not; (c) the successor side (p≈0.053) stands as a power-artifact
  non-rejection per this battery.
- **evidence:** predecessor p=0.0546 in battery-thirds-60-68-pair.md is
  P(null TV >= 0.9412) — the successor observed stat reused as threshold
  (verified across 5 seeds); correct threshold (obs 1.0000) gives p≈0.032.
- **adverses:** 68's predecessors are 7 disjoint singletons — state whether
  the rejection reflects class difference or singleton-pool structure.

### F2. singleton-68-predecessors — priority 2
- **claim:** "68's all-singleton predecessor profile is (or is not) anomalous
  against a matched low-n control."
- **bars:** (a) pick control cells with n in 6–10 on the repaired stream;
  (b) permutation-test each control's predecessor singleton-ness the same way;
  (c) report whether 68's zero-overlap profile is an outlier or typical of
  thin cells.
- **evidence:** 68's 7 predecessors (@114/@504/@884/@1286/@1384/@1442/@1719)
  are disjoint singletons with zero type-overlap to 60's.
- **adverses:** thin-cell controls are themselves low-power; do not over-read.

### F3. suc-60-68-standalone — priority 3
- **claim:** "On successors alone, the {60,68} pair is indistinguishable at any
  n the stream can supply (power-calibrated statement)."
- **bars:** (a) state the successor-side conclusion with the subsample
  calibration attached (95% fail-to-reject at n=7 within-cell);
  (b) record that no larger-n test is available (68 n=7 free is intrinsic).
- **evidence:** successor p≈0.053 (60-vs-68) sits inside the within-60
  subsample p-distribution (median 0.51, 5th pct 0.053).
- **adverses:** moot for the pair if F1 kills on predecessors; keep as a
  methods note for the lane.
