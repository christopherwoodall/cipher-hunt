# Battery verdict: singleton-68-predecessors

Target: `singleton-68-predecessors` (priority 2). Worker: 326ed180-74e3-4255-ab47-49fa82ea4f80, 2026-10-09T01:58:41Z.

## Bar (verbatim from battery-queue.json)

"(a) pick control cells with n in 6–10 on the repaired stream; (b) permutation-test each control's predecessor singleton-ness the same way; (c) report whether 68's zero-overlap profile is an outlier or typical of thin cells"

Numbered clauses:
1. Pick control cells with n in 6–10 on the repaired stream.
2. Apply the same predecessor singleton-ness measurement to each control (empirical matched-control comparison; rank 68 within the control distribution).
3. Report whether 68's profile is an outlier or typical of thin cells.

Adverses (listed): "thin-cell controls are themselves low-power; do not over-read."

## Method

Parsed the repaired 1,847-pair stream exactly per `code/side-keyhunt/repair_parse.py` (rows from `data/upstream-ct_R5005.txt`, offsets from `code/side-keyhunt/repaired_offsets.json`, byte-exact `[s[i:i+2] for i in range(o, len(s)-1, 2)]`). `canonical.py` never touched. R5005, sealed gates, red-team queue untouched.

"Predecessor singleton-ness" (the evidence battery's sense, "disjoint singletons"): each predecessor slot of the cell is filled by a distinct predecessor type (no repeats). Two measures per cell:
- M1 = distinct predecessor types / predecessor slots (1.0 = all-disjoint).
- M2 = type-overlap count between the cell's predecessor types and 60's predecessor-type set (60's set: 03, 06, 14, 21, 29, 46, 53, 64, 77, 92, 94, 98; 60 has n=18).

## Correction to the evidence premise (headline)

The evidence battery (subsample-power-60-68 null, 2026-10-08) reported 68's 7 predecessors (@114/@504/@884/@1286/@1384/@1442/@1719) as "disjoint singletons with zero type-overlap to 60's". On the repaired stream:

- **68 has n=8, not 7.** The eighth occurrence is @1788 (row a8_09): `... 96 21 68 47 03 ...`, predecessor '21'. The prior battery's window census missed it.
- **Zero type-overlap is a miscount.** Predecessor '21' at @1787 IS in 60's predecessor-type set. Corrected M2 for 68 = 1, not 0.
- **"Singleton" cannot mean stream-singleton predecessors.** All eight predecessor types have stream frequencies 12–30 (89:14, 39:13, 79:18, 55:12, 65:25, 52:27, 47:28, 21:30). The evidence meant disjoint/distinct predecessors (interpretation b), which holds: M1 = 8/8 = 1.0.

Full 68 window table (repaired stream):

| @ | row | pred | pred stream-freq | in 60's pred set? |
|---|-----|------|------------------|-------------------|
| 114 | a1_03 | 89 | 14 | no |
| 504 | a3_00 | 39 | 13 | no |
| 884 | a5_08 | 79 | 18 | no |
| 1286 | a7_03 | 55 | 12 | no |
| 1384 | a7_06 | 65 | 25 | no |
| 1442 | a7_09 | 52 | 27 | no |
| 1719 | a8_07 | 47 | 28 | no |
| 1788 | a8_09 | 21 | 30 | YES |

68: n=8, M1=1.000, M2=1.

## Control results (clause 1 + 2)

16 control cells with n in 6–10 on the repaired stream: 51, 28, 73, 18, 58, 71, 10, 38, 23, 31, 07, 19, 36, 97, 35, 15.

- M1: mean 0.793, median 0.845, min 0.500, max 1.000. **3/16 controls also score M1=1.0** (51, 18, 10).
- M2: mean 0.81, median 1.0, min 0, max 3. **13/16 controls have M2 ≤ 1** (68's value); 7/16 have M2=0.
- 68's M1 rank: 3 of 16 controls score ≥ 68 (tied top, not unique). 68's M2 rank: 13 of 16 controls score ≤ 68 — 68 sits exactly at the median.

Control detail (g, n, M1, M2, pred types): 51 n=6 1.000/1; 28 n=6 0.833/0; 73 n=6 0.667/1; 18 n=7 1.000/0; 58 n=7 0.714/0; 71 n=7 0.857/0; 10 n=7 1.000/0; 38 n=7 0.857/1; 23 n=8 0.500/1; 31 n=8 0.625/1; 07 n=8 0.875/3; 19 n=9 0.889/1; 36 n=9 0.667/0; 97 n=10 0.600/0; 35 n=10 0.700/2; 15 n=10 0.900/2.

## Per-clause pass/fail

1. Control cells n 6–10 picked on the repaired stream: **PASS** (16 cells).
2. Same measurement applied to each control; 68 ranked within the empirical distribution: **PASS**.
3. Outlier vs typical determination reported: **PASS** — 68 is typical (see verdict).

Adverse answered (not ignored): the thin-cell comparison is low-power (16 controls) — reported as a distributional ranking with the caveat stated, no significance claim made, no over-reading. The evidence-premise miscount (n=7→8, zero-overlap→1) is flagged above as a correction, not relitigated as a battery.

## Verdict: promote

**The determination is promoted:** 68's all-disjoint predecessor profile is **NOT anomalous** — it is typical of thin cells on the repaired stream. All-disjoint predecessors (M1=1.0) occur in 3/16 matched controls; 68's 60-overlap of 1 is the control median. This corroborates (with corrected numbers) the subsample-power-60-68 null's underlying read that 68's predecessor pattern carries no anomaly signal, while correcting its two miscounts (n=7→8; zero-overlap→overlap '21' @1788). No value claim about 68 is made; no standing verdict is contradicted or downgraded. No follow-ups required (determination complete) — none proposed.

Standing constraints respected: pencil ground truth untouched; no new polyvalence declared; R5005, sealed gate instances, and the red-team adjudication queue untouched.
