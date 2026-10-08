# Solved-context inventory — anomalies & reconciliations (2026-10-07)

Re-derived from the repaired 1,847-pair stream
(`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`;
never the stale 1,846-pair `canonical.py`).

## Index-offset warning (applier MUST read)
Pre-repair (1,846-pair) lane artifacts are off by **−1 pair index** relative
to this inventory for every window at/after row `a5_03`. Example: F61's
este-arm `@1190/@1448/@1804 firm, @1291 fenced` = this inventory's
`@1189/@1447/@1803 firm, @1290 fenced`. Same windows, not new windows.

## Count discrepancies vs expectations
| context | expected | found | verdict |
|---|---|---|---|
| la-premiere 11-70-82-34-29-40 | 2 | 2 @754(a5_03), @1034(a6_03) | CONFIRM |
| par-ce-que 96-87-46 | 3 | 3 @224(a2_01), @952(a6_00), @1526(a8_00) | CONFIRM |
| par-le 96-00 | (none) | 3 @47, @465, @960 | matches F54 00="le" islet n=3 |
| m-en 82-84 | (none) | 1 @166 | — |
| ment 82-06 | (none) | 4 @579, @737, @1183, @1354 | matches F61 06="ent" iff pre=82 n=4 |
| en-ce 24-87 | (none) | 10 (incl. 24-87-64 @179, @1766, @1774) | — |
| l-est 93-59 | (none) | 1 @102 | part of "ne l'est" @101–103 (F61) |
| n-est 94-59 | (none) | **3 @558, @762, @1795** | **DISCREPANCY** (below) |

## DISCREPANCY: F71's est-arm count vs stream
F71 (crowd10/conditioner59, ISLET 10) records est-arm as 6/6:
«qui est»×3, «n'est»×2, «l'est»×1. The repaired stream has
64-59×3 (@315, @1209, @1776) + 94-59×**3** (@558, @762, @1795) + 93-59×1
(@102) = **7** est-arm windows, not 6. One of @558/@762/@1795 was fenced
or miscounted in F71's battery — the applier should reconcile before
treating all three «n'est» windows as est-arm.

## Competing readings the applier must know (not predictions, lane facts)
- **"m'en" two ways:** this inventory's 82-84 "m'en" occurs ONCE (@166;
  F53's 84="en" conditioned arm, pre∈{46,94,82}, n=4: 82-84@166,
  46-84@309/@472, 94-84@1664). Separately, N24 records a 94="en"
  conditioned islet (pre=82) covering **82-94 "m'en" ×3** @650, @1101, @1575
  (all verified present in the stream). The two bigram families do not
  overlap; both readings are live in the lane record.
- **"en ce" two ways:** 24-87 ×10 (this inventory) vs 94-87 ×1 @1169
  (N24's 94="en" islet, suc=87 arm). No overlap.
- **84 polyvalence:** 84="en" arm (pre∈{46,94,82}, n=4) vs 84=masc-noun arm
  (pre∈{77,11}, n=8: 77-84×7, 11-84×1 @1619 — all verified). 13 of 25
  84-windows are unclassified (F53 partial polyvalence, no partition).
- **59 arms:** est-arm 7 (discrepancy above), -este-arm 4 (pre=84:
  @1189/@1447/@1803 firm, @1290 fenced — fenced one marked in
  neighbor_notes via the raw note), **unclassified 16/27**. Unconditioned
  59="est" is kill-grade refuted (F71) — the 16 unclassified windows must
  NOT be read as "est".

## Positional notes
- «ne l'est» @101–103 = 94-93-59 (F61); the 93-59 inventory entry @102 is
  the tail of it.
- 64-77-84 trigram ×3 @144, @1445, @1801 (n_eff=1 per lane) and the
  87-64-77-84 quad @1800–1803 («ce qui [verbe] 84» frame) are verified
  present; they are NOT in this inventory (unbanked) but constrain the
  applier's 84/77 handling at those positions.
- en-ce windows where the 24="de" rival is scoped-killed (24-87-64):
  @179, @1766, @1774 — flagged in `frame_constraints`.
