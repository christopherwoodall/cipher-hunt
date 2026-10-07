# PREREGISTRATION AMENDMENT v1.1 — slider pass 1 FRAME FIX (2026-10-07 ~09:45 CDT)

Amends `prereg_pass1.md` (sha256
`233ff426b04e5163cffde15e9dc25a1f7f2460c2da23b79644be1d84a11861a`).
**Scope of this amendment: frame correction ONLY.** Weights, thresholds,
acceptance criteria, rule names, candidate inventory (ERA-VOCAB + SURVIVING
FORMULAE + 1841 COLLOCATIONS), and control design are UNCHANGED. No threshold,
weight, window, or candidate list changed — only the pair-frame in which the
frozen window positions are expressed.

## What was wrong

v1.0 §"Target recap" measured the transcription by naive concatenation of
`data/upstream-ct_R5005.digits.txt` (3,764 digits / 2 = 1,882 pairs) and wrote
the (c)/(d)/(e)/(f) window inventories in that 1,882-frame. The lane-canonical
parse — `data/upstream-ct_R5005.txt` + `data/upstream-offsets.json`, identical
to `code/crib_attack.py::load_pairs` (per-line offset-1 drops on 32 lines,
trailing-digit drops on odd-digit lines) — yields **1,846 pairs / 96 distinct
groups**, byte-identical to `code/sidepath/skeleton.json`'s 1,846 positions
(verified: my parse == skeleton positions, all 1,846). The (a) S01–S25 list in
v1.0 was already in the canonical frame (it came from
`code/crowd3/segmenter_results.json`, whose builder asserts N==1846; all 25
re-verified byte-exact against the canonical parse, groups + phases + flank_conf).

## Verified frame asserts (v1.1)

- `data/upstream-ct_R5005.digits.txt`: 3,764 digits, sha256
  `18d48ccdca83fe5133b840cd427d5b89046839c866441d1c7c06fc264493e73f`
  (matches `data/SHA256SUMS.txt`, NOTES.md:807, REPORT.md:50).
- Canonical parse: **1,846 pairs, 96 distinct groups** (asserts pass).
- Spot-checks (all PASS): [24 53] @ pairs 1579–1580; [41 65 38] @ 1110–1112;
  [51 62 16] @ 81–83; "la première" 11-70-82-34-29-40 @ pair 1033.

## Re-derived position lists (canonical frame — these REPLACE v1.0's lists)

- **24-positions (52):** 29, 41, 69, 73, 162, 165, 179, 190, 221, 311, 474, 535,
  547, 564, 643, 654, 672, 732, 782, 805, 806, 810, 822, 828, 858, 916, 954, 965,
  984, 990, 1014, 1082, 1131, 1192, 1219, 1267, 1318, 1381, 1437, 1485, 1491,
  1496, 1521, 1566, 1579, 1656, 1692, 1727, 1753, 1765, 1773, 1829.
  (v1.0 listed 42 in the wrong frame; skeleton-keeper's independent count is 52.)
- **52-positions (27):** 160, 264, 284, 383, 482, 571, 632, 649, 1006, 1080,
  1099, 1123, 1128, 1293, 1307, 1331, 1341, 1355, 1384, 1408, 1415, 1434, 1440,
  1573, 1721, 1737, 1806. (v1.0: 13.)
- **62-positions (34):** 11, 46, 82, 100, 360, 389, 425, 446, 508, 658, 665,
  801, 839, 848, 944, 1064, 1135, 1140, 1296, 1314, 1323, 1328, 1348, 1361,
  1453, 1463, 1467, 1481, 1535, 1538, 1568, 1685, 1703, 1771. (v1.0: 32.)
- **62→94 bigrams (8):** @ 100, 508, 839, 1328, 1361, 1685, 1703, 1771.
  **Reconciles with NOTES.md's ×8** — v1.0's ×5 was a parse artifact of the
  1,882-frame (three bigrams fell on frame-shifted boundaries and were missed).

## Corrected window inventory (replaces v1.0 §"Window inventory" (b)–(f))

- (a) W-S01..W-S25 — UNCHANGED (already canonical; re-verified).
- (b) W-47 — pairs 146–157; sub-windows starts 146..153 × lengths 3,4,5 =
  **24 sub-windows** (v1.0 said 36 — arithmetic slip: 8×3=24).
  **Correction:** the anchored formula 87 64 96 47 46 sits at **148–152**,
  not 150–154 (verified `pairs[148:153] == ['87','64','96','47','46']`).
  Grid unchanged — it still covers the formula.
- (c) W-62B — 8 bigrams above, ±3 pairs → windows [p−3, p+4] (8 pairs each),
  ids W-62B-100 … W-62B-1771. (v1.0: 5 windows in wrong frame.)
- (d) W-62C — 26 remaining 62-positions, ±3, overlaps merged → 22 windows:
  (8,14) (43,49) (79,85) (357,363) (386,392) (422,428) (443,449) (655,668)
  (798,804) (845,851) (941,947) (1061,1067) (1132,1143) (1293,1299)
  (1311,1317) (1320,1326) (1345,1351) (1450,1456) (1460,1470) (1478,1484)
  (1532,1541) (1565,1571).
- (e) W-24 — 52 positions, ±3, overlaps merged → 44 windows:
  (26,32) (38,44) (66,76) (159,168) (176,182) (187,193) (218,224) (308,314)
  (471,477) (532,538) (544,550) (561,567) (640,646) (651,657) (669,675)
  (729,735) (779,785) (802,813) (819,831) (855,861) (913,919) (951,957)
  (962,968) (981,993) (1011,1017) (1079,1085) (1128,1134) (1189,1195)
  (1216,1222) (1264,1270) (1315,1321) (1378,1384) (1434,1440) (1482,1499)
  (1518,1524) (1563,1569) (1576,1582) (1653,1659) (1689,1695) (1724,1730)
  (1750,1756) (1762,1768) (1770,1776) (1826,1832).
- (f) W-52 — 27 positions, ±3, overlaps merged → 24 windows:
  (157,163) (261,267) (281,287) (380,386) (479,485) (568,574) (629,635)
  (646,652) (1003,1009) (1077,1083) (1096,1102) (1120,1131) (1290,1296)
  (1304,1310) (1328,1334) (1338,1344) (1352,1358) (1381,1387) (1405,1418)
  (1431,1443) (1570,1576) (1718,1724) (1734,1740) (1803,1809).
- **Total: 147 windows** (25 + 24 + 8 + 22 + 44 + 24).

Slide priority order unchanged: (a) → (b) → (c) → (d) → (e) → (f).

## Frozen and untouched

S = 0.30·lex + 0.25·cut + 0.20·bound + 0.25·len; acceptance S≥0.60,
lex≥0.50, len≥0.50, bound≥0.30, no pinned-anchor contradiction; rule names
MUTE-E, ELISION, SPLIT-PAIR, ORTH-1835, NASAL-VAR, DOUBLE-CONS, VERB-STEM,
RIVAL-NOTE; candidate inventory (ERA-VOCAB 1–5 syllables ≥3×, SURVIVING
FORMULAE, 1841 COLLOCATIONS); control (3 shuffles, seed 1841, same positions);
VOID condition (real accepts < 2× mean control accepts → VOID).

## Signed

slider, 2026-10-07. v1.0 remains on disk for audit; v1.1 governs the slide.
