# Battery report — pair-60-68-readjudicate ({60,68} predecessor p-value re-adjudication)

Worker: 1329907c-a6fb-4271-8553-8e1b93a7b69b. Date: 2026-10-08.
Lock: `code/crowd17/next-token/locks/pair-60-68-readjudicate.lock` created
2026-10-08T20:53:28Z; no prior lock existed; deleted on completion.
Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` +
`data/upstream-ct_R5005.txt`), parsed per `code/side-keyhunt/repair_parse.py`.
`canonical.py` not used. R5005 not touched. Sealed gates, red-team
adjudication queue untouched. No invented numbers: every count below was
re-derived from the stream in this run (two independent implementations plus
an exact combinatorial check).

## HEADLINE — the alleged predecessor p-value bug does NOT reproduce; the original 0.0546 was correct

`battery-subsample-power-60-68.md` headlined a cross-column threshold bug:
that the thirds battery's predecessor p=0.0546 was really
P(null predecessor TV >= 0.9412) (the successor stat reused as threshold),
and that the correctly computed value is p≈0.032 (reject at α=0.05).
Independent re-derivation refutes both halves of that claim:

- Correct predecessor p (obs TV=1.0000, B=20,000, same TV/permutation method):
  **p = 0.0535** — exact combinatorial value 18507/346104 = 0.05347;
  10 simulation seeds give 0.0523–0.0562. The thirds battery's reported
  0.0546 is consistent with the correct computation. **No bug exists.**
- The subsample battery's account of the bug is arithmetically impossible:
  P(null predecessor TV >= 0.9412) = 0.24 (re-derived), not 0.0546 —
  a lower threshold cannot produce a smaller tail probability.
  Its "corrected" 0.032 is not reproducible under the stated method
  (two independent implementations + exact enumeration all give ≈0.0535).

Consequence: the thirds-60-68-pair battery's clause-1 pass
("meets the {33,86} indistinguishability standard on successors AND
predecessors") stands on its original numbers. This battery's own claim —
that the 2-cell claim fails the standard on predecessors — is falsified.
The subsample battery's escalation to the red team rests on a miscalculation;
the supervisor should note the retraction (see § Follow-ups).

## Bar (verbatim, from battery-queue.json)

"(a) re-run the thirds-60-68-pair bar (a) with the corrected predecessor
p-value (obs TV=1.0000, p≈0.032, B=20,000, same method); (b) adjudicate:
predecessor rejection at α=0.05 is kill-grade against the 2-cell claim under
that battery's own bar, or state the red-team reason it is not; (c) the
successor side (p≈0.053) stands as a power-artifact non-rejection per
subsample-power-60-68"

Numbered clauses (pre-registered BEFORE testing, not modified after):

1. (a) Re-run the thirds-60-68-pair bar (a) with the corrected predecessor
   p-value (obs TV=1.0000, B=20,000, same method).
2. (b) Adjudicate: predecessor rejection at α=0.05 is kill-grade against the
   2-cell claim under that battery's own bar, or state the reason it is not.
3. (c) The successor side (p≈0.053) stands as a power-artifact non-rejection
   per subsample-power-60-68.

## Method

Fresh parse of the repaired stream (1,847 pairs, 96 distinct, verified).
Census re-derived and matching both prior batteries: 60 n=18 (free 17,
formula-bound @232 excluded), 68 n=8 (free 7, formula-bound @1788 excluded).
Test: total-variation distance TV = 0.5·Σ|pᵢ−qᵢ| on the predecessor
(resp. successor) empirical distributions; labels permuted B=20,000
preserving cell counts (17/7); p=(ge+1)/(B+1). Two independent
implementations (pure-Python Counter-based; numpy label-permutation) plus an
exact combinatorial enumeration of the predecessor null
(P(TV≥1.0) = P(a random 7/24 split yields disjoint supports) =
18507/C(24,7) = 0.05347). Windows quoted at repaired-stream pair indices.

## Census (re-derived, formula-bound excluded)

- 60 free predecessors (n=17): 21 x3, 92 x2, 14 x2, 06 x2,
  77/46/29/94/03/64/53/98 x1.
- 68 free predecessors (n=7): 89/39/79/55/65/52/47 x1 — seven disjoint
  singletons, zero type-overlap with 60's predecessor set.
- 60 free successors (n=17): 03 x4, 08 x2, 67 x2, 12 x2,
  90/09/15/65/06/71/27 x1.
- 68 free successors (n=7): 21 x2, 37/00/52/59/06 x1.

## Window-level evidence (@-offsets, repaired stream)

68's 7 free windows (predecessor / successor):
- @114 `93 29 89 68 21 67 14` — pred 89, succ 21 ("68-21-67")
- @504 `40 56 39 68 21 67 77` — pred 39, succ 21 ("68-21-67")
- @884 `08 31 79 68 37 03 02` — pred 79, succ 37
- @1286 `32 98 55 68 00 11 17` — pred 55, succ 00
- @1384 `13 24 65 68 52 82 16` — pred 65, succ 52
- @1442 `85 01 52 68 59 37 64` — pred 52, succ 59
- @1719 `30 64 47 68 06 11 52` — pred 47, succ 06

Observed statistics: predecessor TV = 1.0000 (disjoint supports — the maximum
achievable); successor TV = 0.9412. Shared types: predecessors ∅; successors
{06} x1/x1.

## Permutation results (B=20,000)

| side | obs TV | p (10 seeds, range) | exact |
|---|---|---|---|
| predecessor | 1.0000 | 0.0523–0.0562 | 0.05347 |
| successor | 0.9412 | 0.0508–0.0550 | — |

Cross-checks: P(predecessor null TV ≥ 0.9412) = 0.24 (refutes the "reused
threshold" account — a lower threshold gives a larger tail, not 0.0546);
the thirds battery's reported predecessor 0.0546 and successor 0.0552 both
reproduce under the correct method.

## Per-clause pass/fail

1. **(a) PASS with refutation.** The re-run is complete (obs TV=1.0000,
   B=20,000, same method), but the pre-registered premise "p≈0.032" does not
   reproduce: the correct predecessor p is 0.0535 (exact 0.05347). The thirds
   battery's 0.0546 was correctly computed; there was no threshold bug.
2. **(b) PASS — not kill-grade, with stated reason.** No rejection occurred:
   0.0535 > 0.05, so the bar's kill condition (rejection at the lane's
   standard) is not met. The 2-cell homophone claim is NOT killed by this
   re-adjudication, and the thirds battery's clause-1 pass stands. The reason
   it is not kill-grade is not a red-team exemption — it is that the premise
   (a rejection at α=0.05) is factually false. Caveat: the non-rejection is
   marginal (exact p=0.05347); at n=7 the outcome is fragile to single-token
   perturbations, which is why the structural question stays live for the
   queued singleton-68-predecessors battery.
3. **(c) PASS.** Successor p re-derives 0.051–0.055 (non-rejection, unchanged).
   The subsample-power-60-68 reading stands: 95% fail-to-reject at n=7
   within-cell makes the successor non-rejection a power artifact, not
   evidence about 68's class. The predecessor correction dispute does not
   touch this battery's own bar-(b) finding.

## Adverses (answered, never ignored)

- "68's predecessors are 7 disjoint singletons — state whether the rejection
  reflects class difference or singleton-pool structure" — ANSWERED with the
  premise voided: there is no rejection (p≈0.053 ≥ 0.05). On the structure
  question itself: the permutation null conditions on exactly the pooled
  singleton structure (the exact p enumerates every 7/24 split of the
  observed pool, singleton blocks included), so the p-value already accounts
  for it — the singleton structure sets the ceiling of achievable
  dissimilarity (TV=1.0000, disjoint supports: none of 68's 7 predecessor
  types ever precedes 60), and the p-value asks how often a random split
  reaches that ceiling (5.35%). The within-60 subsample calibration
  (predecessor rejection rate 2.57% ≈ nominal α) shows the test is not
  degenerate under singleton-heavy data. Whether 68's all-singleton profile
  is anomalous against matched thin-cell controls is the queued
  singleton-68-predecessors battery's bar — not duplicated here.

## Verdict: KILL (of this battery's claim)

The claim under test — "the {60,68} 2-cell homophone claim fails the
{33,86} indistinguishability standard on predecessors (corrected p≈0.032 <
0.05)" — is falsified by exact re-derivation: the correctly computed
predecessor p is 0.0535, not below 0.05, and the thirds battery's original
0.0546 was correct. The 2-cell claim survives this re-adjudication; the
thirds-60-68-pair null verdict's basis is intact. No red-team verdict is
contradicted (the pair's null was battery-decided; the subsample battery's
escalation was a proposal resting on a miscalculation, flagged for
retraction below).

## Follow-ups for the supervisor (kill verdict — none required; one retraction note)

No new battery targets are proposed: the thirds-60-68-pair null stands, and
singleton-68-predecessors plus suc-60-68-standalone are already queued with
non-overlapping bars.

**Supervisor note (retraction, not a target):**
`code/crowd17/report_inbox/battery-subsample-power-60-68.md` headlines an
escalation to the red team ("predecessor p-value miscomputed, p≈0.032").
That escalation's premise is refuted by this battery's exact re-derivation
(predecessor p = 0.05347; the 0.0546 was correct; the "reused threshold"
account gives 0.24, not 0.0546). The red-team escalation should be marked
retracted/superseded so the false "p≈0.032" value does not propagate into
later batteries' evidence fields. The subsample battery's own verdict
(null on its power-calibration bar) is unaffected and stands.
