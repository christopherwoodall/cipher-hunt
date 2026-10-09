# Battery report: 24-nine-left-envelope

**Target:** `24-nine-left-envelope` (P2)
**Date:** 2026-10-09
**Verdict:** PROMOTE (census/record grade)

## Bar (verbatim from queue)

"envelope census with @-offsets; if \"24 @ i-9\" recurs at further infinitive windows, name the construction; if the two legs are the only hits, fence as a two-leg signature for the A7-L2 scope docket"

## Bar restated as numbered clauses

1. Envelope census: every "X 29" infinitive-shaped token lane-wide, with @-offsets and the token at i-9 (i = X-position).
2. If "24 @ i-9" recurs at further infinitive windows beyond the two A7-L2 legs (@1229/@1589), name the construction.
3. If the two legs are the only hits, fence the signature as a two-leg signature for the A7-L2 scope docket.

## Method

Read BATTERY-PROTOCOL.md first; created `locks/24-nine-left-envelope.lock` (deleted on completion).
Re-derived the repaired 1,847-pair / 96-type stream in-session
(`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`;
upstream tokenization `[s[i:i+2] for i in range(o, len(s)-1, 2)]`).
`canonical.py` never used. R5005, sealed gates, red-team queue untouched.
All @-offsets are 0-based repaired-stream pair indices.
Convention (matching the queue evidence field): i = position of X in each "X 29"
bigram; the envelope tests the token at i-9. Verified: the two A7-L2 legs are
0-based X-positions @1229 and @1589 (48 of "48 29" at @1229/@1589, 29 at @1230/@1590).

## Census: all 45 "X 29" windows

| X-pos | X | 24@i-9? | row |
|---|---|---|---|
| @21 | 43 | no | a1_00 |
| @61 | 34 | no | a1_01 |
| @77 | 11 | no | a1_02 |
| @95 | 46 | no | a1_02 |
| @111 | 93 | no | a1_03 |
| @146 | 84 | no | a1_04 |
| @217 | 46 | no | a2_01 |
| @273 | 33 | no | a2_03 |
| @290 | 64 | no | a2_03 |
| @373 | 63 | no | a2_06 |
| @421 | 36 | no | a2_08 |
| @431 | 86 | no | a2_09 |
| @499 | 11 | no | a2_11 |
| @540 | 44 | no | a3_01 |
| @596 | 01 | no | a4_00 |
| @617 | 10 | no | a4_00 |
| @626 | 33 | no | a4_01 |
| @684 | 64 | no | a5_00 |
| @688 | 94 | no | a5_00 |
| @757 | 34 | no | a5_03 |
| @779 | 08 | no | a5_04 |
| @813 | 14 | no | a5_05 |
| @1030 | 03 | no | a6_03 |
| @1037 | 34 | no | a6_03 |
| @1049 | 88 | no | a6_04 |
| @1051 | 40 | no | a6_04 |
| @1096 | 06 | no | a6_06 |
| @1142 | 16 | no | a6_08 |
| @1154 | 92 | no | a6_09 |
| @1199 | 64 | no | a7_00 |
| @1229 | 48 | YES | a7_01 |
| @1232 | 33 | no | a7_01 |
| @1257 | 31 | no | a7_02 |
| @1320 | 03 | no | a7_04 |
| @1375 | 86 | no | a7_06 |
| @1388 | 06 | no | a7_07 |
| @1391 | 86 | YES | a7_07 |
| @1424 | 33 | no | a7_08 |
| @1477 | 33 | no | a7_10 |
| @1565 | 50 | no | a8_01 |
| @1589 | 48 | YES | a8_02 |
| @1594 | 03 | no | a8_02 |
| @1709 | 06 | no | a8_06 |
| @1815 | 06 | no | a8_10 |
| @1825 | 86 | no | a8_11 |

No edge cases: every X-29 window has X-pos >= 9, so i-9 is defined for all 45.

## The three "24 @ i-9" windows (byte-exact)

**W1 @1229 (X=48, row a7_01)** — same-row envelope (i-9=@1220 also a7_01):
`@1219:61 @1220:24 @1221:48 @1222:30 @1223:09 @1224:20 @1225:57 @1226:64(qui) @1227:79(tout) @1228:82(m) @1229:48 @1230:29 @1231:47 @1232:33 @1233:29`
24@i-9 ✓, qui@i-3 ✓, "48 29 47" tail. Row-robust.

**W2 @1391 (X=86, row a7_07)** — crosses the a7_06→a7_07 row join (i-9=@1382 on a7_06):
`@1381:13 @1382:24 @1383:65 @1384:68 @1385:52 @1386:82 | @1387:16 @1388:06 @1389:29 @1390:67 @1391:86 @1392:29 @1393:89 @1394:16`
24@i-9 ✓, but no qui in span, no 48, no 47-tail; a second "86 29" infinitive sits at @1375-1376 on a7_06. Frame-dissimilar to W1/W3; phase-fragile.

**W3 @1589 (X=48, row a8_02)** — crosses the a8_01→a8_02 row join (i-9=@1580 on a8_01):
`@1578:47 @1579:98 @1580:24 | @1581:53 @1582:12 @1583:44 @1584:00 @1585:36 @1586:70 @1587:64(qui) @1588:65 @1589:48 @1590:29 @1591:47 @1592:08`
24@i-9 ✓, qui@i-2 ✓, "48 29 47" tail. Phase-fragile (cross-row).

## Key population fact

"48 29" occurs **exactly 2× stream-wide** (@1229-1230, @1589-1590) — the entire
population. Both carry 24 at i-9 AND qui at i-2/i-3. The A7-L2-specific
signature (24@i-9 of a 48-29 infinitive with qui at i-2/i-3) is a perfect 2/2
within the "48 29" family. qui@i-2/i-3 occurs at only 4/45 X-29 windows
(@21, @146, @1229, @1589); the 24+qui combo occurs only at the two A7-L2 legs.

## Distributional check

24 at i-9: 3/45 vs ~1.27 expected at 24's base rate (n(24)=52, p=0.0282).
Binomial P(>=3/45) ≈ 0.133 — below the lane's standard. Sensitivity: 24 at i-8
= 1/45, at i-10 = 1/45 (both ≈ base rate). The 9-offset does not clear the
lane's distributional standard as a lane-wide envelope.

## Per-clause pass/fail

1. **PASS.** Census complete: 45 windows, all @-offsets, i-9 tokens, rows.
2. **PASS (with fence).** "24 @ i-9" recurs at one further window (@1391), so the
   construction is named: **the "24-left-9 infinitive envelope"** — distributional
   label, two sub-signatures:
   - **Signature A (A7-L2):** 24 @ i-9 of a "48 29" infinitive with qui at i-2/i-3
     — 2 legs (@1229 row-robust, @1589 cross-row/phase-fragile). Fenced as a
     two-leg signature for the A7-L2 scope docket.
   - **Signature B:** 24 @ i-9 of an "86 29" infinitive — 1 leg (@1391,
     cross-row, frame-dissimilar, no qui). Fenced as a singleton below the
     lane's distributional standard (p≈0.13).

## Adverses

None listed.

## Verdict: PROMOTE (census/record grade)

The envelope is censused, named, and fenced. No standing or red-team verdict
contradicted or downgraded; §7 intact. The A7-L2 scope question itself stays
with the red-team docket; this battery only records the envelope's exact
extent and its row-fragility.

## Bookkeeping

- Lock `code/crowd17/next-token/locks/24-nine-left-envelope.lock` created
  2026-10-09T07:58:07Z, deleted on completion.
- `battery-queue.json`: `24-nine-left-envelope` queued -> verdict/promote
  (temp-file + rename; pre-write assert confirmed no prior verdict; only this
  entry touched; JSON re-validated).
- R5005, sealed gates, red-team adjudication queue untouched.
