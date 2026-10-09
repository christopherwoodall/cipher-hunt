# Battery report: suc-60-68-standalone

- Target id: `suc-60-68-standalone`
- Claim: "On successors alone, the {60,68} pair is indistinguishable at any n the stream can supply (power-calibrated statement)"
- Date: 2026-10-09
- Worker: battery worker (subagent c319dfd4-f6d5-495f-919b-d11859105ed1)
- Stream: repaired 1,847-pair parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed like `code/side-keyhunt/repair_parse.py`; n=1847 asserted, 96 types asserted).
  `canonical.py` never used. R5005, sealed gates, red-team adjudication queue untouched.
- Lock: `code/crowd17/next-token/locks/suc-60-68-standalone.lock` (created at start, deleted on completion; no prior lock existed).

## Bar (verbatim, pre-registered before testing)

"(a) state the successor-side conclusion with the subsample calibration attached (95% fail-to-reject at n=7 within-cell); (b) record that no larger-n test is available (68 n=7 free is intrinsic)"

Numbered pass/fail clauses (restated before testing, not modified after):

1. C1: the successor-side conclusion is stated with the subsample calibration attached — fail-to-reject rate at n=7 within-cell (both cells at n=7, 60 subsampled, 68 subsampled to 7 of 8), compared against the bar's 95% reference.
2. C2: it is recorded that no larger-n test exists for the smaller cell (68 n=7 free is intrinsic; all 8 observed successor windows are row-internal, so the supply ceiling is the queue's stated intrinsic n=7).
3. C3 (adverses answered): the mootness adverse is addressed — `pair-60-68-readjudicate` is verdict/kill, so the pair-level conclusion is moot per the adverse's own terms; the result is kept strictly as a methods note for the lane, not as a pair verdict.

## Method

1. Re-derived the repaired parse in-session: 1,847 pairs, 96 types. Never used `canonical.py`.
2. Enumerated all successors of 60 and 68 from the repaired stream (0-based @-offsets below; every 68-window's successor is row-internal).
3. Test: exact Monte Carlo permutation homogeneity test (H0: same successor distribution), chi-square-type statistic T = Σ (O−E)²/E over the union of observed successor supports, α=0.05. Full-sample test at (n60=18, n68=8) with 20,000 permutations. Calibration: 200 replicates at n=7 within-cell (60 subsampled 18→7 without replacement; 68 subsampled 8→7 without replacement per replicate), each replicate tested with 2,000 permutations at α=0.05; fail-to-reject rate recorded. Fixed seeds throughout (master 20261009; replicate seeds 1000+b); fully deterministic.
4. Checked `pair-60-68-readjudicate` in `battery-queue.json` for the mootness adverse: verdict `kill`.

## Window-level evidence

Successor draws (re-derived, 0-based @-offsets; successor = token at @+1):

**68 windows (n=8, all successors row-internal):**
- @114 (a1_03): 89 [68] 21
- @504 (a3_00): 39 [68] 21
- @884 (a5_08): 79 [68] 37
- @1286 (a7_03): 55 [68] 00
- @1384 (a7_06): 65 [68] 52
- @1442 (a7_09): 52 [68] 59
- @1719 (a8_07): 47 [68] 06
- @1788 (a8_09): 21 [68] 47

**60 windows (n=18):** @119 (a1_03)→90, @172 (a1_05)→09, @197 (a2_00)→08, @232 (a2_01)→71, @322 (a2_04)→15, @454 (a2_10)→65, @637 (a4_01)→67, @690 (a5_00)→03, @700 (a5_01)→12, @995 (a6_01)→67 (row boundary crossed — successor on a6_02), @1338 (a7_05)→08, @1366 (a7_06)→03, @1474 (a7_10)→06, @1563 (a8_01)→71, @1644 (a8_04)→03, @1674 (a8_05)→03, @1690 (a8_05)→27, @1735 (a8_07)→12.

Successor multisets:
- 60: {03:4, 08:2, 71:2, 67:2, 12:2, 90:1, 09:1, 15:1, 65:1, 06:1, 27:1}
- 68: {21:2, 37:1, 00:1, 52:1, 59:1, 06:1, 47:1}

Shared successor support: {06} only (60→06 ×1, 68→06 ×1).

## Per-clause results

- **C1 PASS.** At the bar's calibration level, n=7 within-cell: fail-to-reject rate = **0.955** (191/200 replicates at α=0.05), matching the bar's 95% reference. The p-value distribution across replicates: min 0.038, q25 0.203, median 0.236, q75 0.462, max 1.000. A (7,8) variant (68's full observed 8 draws) gives 0.935 fail-to-reject — same conclusion. Conclusion as the bar prescribes: **on successors alone, {60,68} is indistinguishable at any n the stream can supply for the smaller cell** (95.5% fail-to-reject at n=7 within-cell).
- **C2 PASS.** Recorded: no larger-n test exists. All 8 observed 68-successor windows are row-internal (see census above), so 68's supply is intrinsically capped at 8 draws; the queue's bar states the intrinsic free count as n=7, which is the level the calibration uses. 60's 18 draws cannot raise the test's cell size beyond 68's supply.
- **C3 PASS.** `pair-60-68-readjudicate` = verdict **kill** (confirmed in queue). The successor-side note is therefore moot for the pair per the adverse's own terms; this report is a lane methods note only. No pair-level claim is made, and no standing verdict is touched.

## Material caveat (stated, not hidden)

At the full asymmetric sample (n60=18, n68=8), the same permutation test **rejects** homogeneity: T=23.65, p≈0.019±0.001 (20,000 permutations) at α=0.05. The bar's calibrated conclusion holds at the prescribed n=7 within-cell level — 68's intrinsic supply — but a future lane use of this methods note must not cite it as "the successor test fails to reject at all n": at the larger asymmetric (18,8) it rejects. The power gap (reject at (18,8), 95.5% fail-to-reject at (7,7)) is itself the point: at any n the stream supplies for 68, the test has essentially no discriminating power.

## Verdict: PROMOTE (methods note, battery grade)

All bar clauses pass and the adverse is answered as the bar directs. Scope per the adverse: moot for the {60,68} pair itself (`pair-60-68-readjudicate` kill stands) — this promotes only as a lane methods note recording the successor-side power calibration. No red-team verdict contradicted; §7 intact.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-suc-60-68-standalone.md`
- Queue: `battery-queue.json` — `suc-60-68-standalone` status `queued`→`verdict`, result `promote`, date 2026-10-09 (pre-write assert passed: status `queued`, no prior verdict; temp-file + rename; JSON re-validated; only this entry touched)
- Lock created on start, deleted on completion.
