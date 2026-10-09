# Battery verdict: phase-likelihood-row-sweep

## Bar (verbatim, pre-registered)
"all-70-row sweep; outlier test; flag for red-team review if weak"

Restated as numbered clauses:
- C1: run the leave-one-out pair-likelihood comparison for all 70 rows (same
  method as doubled-1195-offset-audit).
- C2: outlier test — determine whether a7_00's +8.4-nat delta is an outlier
  against the row population.
- C3: flag for red-team review if a7_00's phase support is weak.

## Verdict: PROMOTE (sweep finding)

## Method

Read BATTERY-PROTOCOL.md first. Created
`locks/phase-likelihood-row-sweep.lock` on start (agent id + UTC timestamp).
Re-derived the repaired stream in-session from `data/upstream-ct_R5005.txt` +
`code/side-keyhunt/repaired_offsets.json` (70 rows, 1,847 pairs, 96 types;
`canonical.py` never touched). R5005, sealed gates, red-team adjudication
queue untouched.

Per row: built leave-one-out unigram pair frequencies from the other 69 rows
(all under their repaired offsets), Laplace add-1 smoothing over the 100
possible two-digit pairs, then computed log-likelihood of the row's pairs
under its repaired offset (chosen phase) vs the rival offset. delta =
loglik(chosen) - loglik(rival); positive delta favors the repaired phase.

Method calibration: reproduces doubled-1195-offset-audit's a7_00 numbers
byte-exact: offset=1 loglik -123.53, offset=0 loglik -131.94, delta +8.40.

## Results

70/70 rows swept (C1 PASS).

- 50 rows favor their repaired offset (delta > 0); 20 favor the rival phase.
- Population: mean delta +3.26, median +4.33, stdev 4.56, range -7.54 to +12.95.
- a7_00: delta +8.40, z = +1.13, rank 7/70 (descending). Its support is
  ordinary-to-strong for the population — **not an outlier** (C2 answered).
- C3 does not fire: a7_00's phase support is not weak.

Phase-by-group asymmetry (structural, stated not hidden):
- Repaired offset=1: 31 rows, mean delta +6.54, median +6.36, **zero** negative.
- Repaired offset=0: 39 rows, mean delta +0.65, median -0.11; all 20
  rival-favoring rows sit in this group.
Total pair counts are identical in both phases (1,847 each), so this is not a
length artifact: offset-1 pairings genuinely consist of higher-frequency pairs.

Rows where the rival phase wins the criterion (negative delta, 0-based
@-stream starts; rival = offset 1 for all): a8_08 -7.54, a5_03 -7.17,
a8_06 -4.55, a8_09 -4.21, a2_04 -3.99, a2_09 -3.85, a2_05 -3.35, a8_10 -3.03,
a3_02 -2.36, a4_00 -1.69, a5_02 -1.63, a8_02 -1.48, a2_02 -1.46, a5_04 -1.13,
a7_05 -0.85, a7_07 -0.50, a8_11 -0.42, a2_06 -0.26, a7_11 -0.21, a3_00 -0.11.

Phase-tie rows (weakest positive support): a7_04 +0.07, a2_11 +0.18,
a6_08 +0.99, a8_07 +1.22.

Re-segmentation rows: a1_01 (repaired offset 0, delta +6.49 — the criterion
favors offset 0 there, in tension with seg-a1_01's constraint-clean offset-1
re-parse); a7_10 (repaired offset 0, delta +4.66 — criterion favors offset 0,
in tension with reseg-1481-98's constraint-clean offset-1 re-parse).
Statistical preference and constraint-cleanliness measure different things;
both results are reported, neither is hidden.

**Critical guardrail on the 20-row list (not a re-parse recommendation):**
a5_03's offset=0 is gloss-mandated by red-team finding R1 (delta -7.17 favors
the old offset 1 there). Statistical preference loses to byte evidence.
The same applies anywhere a gloss, crib, or formula anchors a row.

## Headline for the red team

a7_00's phase support is not an outlier and needs no flag — but the sweep
shows the same likelihood criterion leaves 20 offset-0 rows
locally-suboptimal, which is exactly the soil where the two offset-1
re-segmentations (a1_01, a7_10) grew. Phase uncertainty is concentrated in the
offset-0 row group. The a5_03 case proves the criterion is fallible against
byte evidence.

## Standing-state check

No standing verdict contradicted or downgraded. §7 intact. No polyvalence
declared. The a5_03 gloss-mandated offset (R1) is honored as a premise.

## Adverses

None listed on the target.

## Bookkeeping

Report filed at `code/crowd17/report_inbox/battery-phase-likelihood-row-sweep.md`;
queue entry `phase-likelihood-row-sweep` set to status `verdict`, result
`promote`, date 2026-10-09 (temp-file + rename, pre-write assert confirmed
`queued`/verdictless, post-write JSON re-validated); lock deleted.
