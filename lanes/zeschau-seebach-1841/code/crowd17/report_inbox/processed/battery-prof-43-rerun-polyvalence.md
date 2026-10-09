# Battery report: prof-43-rerun-polyvalence

- Target: `prof-43-rerun-polyvalence`
- Date: 2026-10-09
- Worker agent: 4cb2fd3b-c228-4a3c-be6a-948d30b1ae7e
- Stream: repaired 1,847-pair / 96-type parse (`code/side-keyhunt/repaired_offsets.json`
  + `data/upstream-ct_R5005.txt`, parsed per `repair_parse.py`). `canonical.py` not used.

## Gate check

- R19-064 decided redteam-43-polyvalence; R20-117 re-confirmed it.
- 43=["noun","cls"] stands. Gate satisfied. Re-run proceeds under the 43-nominal premise.
- Premise sanity-checked on the repaired stream: @563 `59 30 67 11 [43] 24 80 97`
  (row a3_02) and @1204 `29 45 58 47 [43] 55 61 21` (row a7_00) exist with the
  cited contexts. @439 `45 46 [43] 98 80 50` (row a2_09) and @1092
  `79 80 06 [43] 07 55 81` (row a6_05) also confirmed.

## Bar (verbatim)

"exact bar re-run conditioned on red-team 43-polyvalence verdict"

## Bar restated as numbered clauses

1. Re-run the '43 81' NP census conditioned on the red-team 43-polyvalence verdict
   (R19-064 / R20-117; 43=["noun","cls"] stands).
2. Decide whether '43 81' forms an NP with >=2 independent legs under the 43-nominal premise.
3. If it does not, fence the '43 81' NP arm (closing the ne-drop arm).

## Method

Bigram census of '43 81' on the repaired 1,847-pair stream; full follower census
of 43 (16 occurrences) and predecessor census of 81 (14 occurrences); locus
inspection of the single hit with a +/-8-pair 'ne' (94) check.

## Findings

- `count('43 81') = 1`, stream-wide. Hapax at stream index 43, row a1_01:
  `41 01 24 88 [43] [81] 30 62 96 00`.
- 43's 16 occurrences and their followers (index: follower):
  @21:29, @43:81, @244:00, @258:77, @343:87, @386:91, @439:98, @563:24,
  @1027:87, @1092:07, @1126:00, @1204:55, @1303:21, @1305:77, @1544:00, @1724:98.
  81 is a follower exactly once. No follower is a nominal-class cell; 43 never
  appears as a prenominal modifier/determiner in any frame.
- 81's predecessors: 55 x6, 77 x4 ('le 81' x4 — the only licensed 'X 81' NPs),
  43 x1, 98 x1, 39 x1, 08 x1. 55 is not a granted/licensed value, so its six
  '55 81' windows do not license an NP template for '43 81'.
- No 'ne' (94) within +/-8 pairs of @43 (window: `08 91 39 64 41 01 24 88 43 81
  30 62 96 00 92 79 37`); the ne-drop reading is independently unpromotable at
  this locus.

## Per-clause pass/fail

1. Condition (gate satisfied): PASS.
2. '43 81' forms an NP with >=2 independent legs: FAIL at kill grade — a hapax
   yields at most one leg, so two independent legs are structurally impossible.
   Zero prenominal-modifier legs for 43 exist anywhere on the stream, and 81's
   only licensed 'X 81' NP template ('le 81') excludes 43.
3. Fence the '43 81' NP arm: DONE. The ne-drop arm that depended on the
   '43 81' NP is permanently closed under the granted 43-nominal premise.

## Adverses

- None listed on the target.
- No contradiction with the standing red-team verdict: fencing the '43 81' NP
  does not conflict with 43=["noun","cls"] (a noun need not form an NP with 81),
  and it matches the pre-registered expectation in the target's own claim
  ("expected: still fails - zero modifier legs").

## Verdict: KILL

The '43 81'-NP sub-claim is killed: the distributional census on the repaired
stream rejects it at the lane's standard (hapax; zero modifier legs; 'ne'
absent at the locus). The ne-drop arm is closed. This does not touch the
43-nominal grant itself, which stands.

## Follow-ups

None required by §4 (verdict is kill, not null). The seg-81-30-boundary C2 arm
closure follows from this fence; no new battery target is proposed.
