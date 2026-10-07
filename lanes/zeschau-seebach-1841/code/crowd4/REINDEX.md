# REINDEX — canonical parse repair (2026-10-07, key-hunt side fleet R1, red-team verified)

## The bug
The lane's canonical 1,846-pair parse contradicted manuscript gloss (i): the erased
pencil "la pre m i er e" sits over groups `11 70 82 34 29 40` on row a5_03, and the
raw 12-digit crib `117082342940` starts at raw offset 1532 (even) — so pair-phase at
1532 must be EVEN. Upstream's EM choice `offsets['a5_03'] = 1` made it ODD, splitting
the crib off-phase (`71 17 08 23 42 94 02`). The lane had been anchored on the
crib's SECOND raw occurrence all along.

## The fix
Flip `offsets['a5_03']` 1 → 0. This removes 2 dropped digits inside row a5_03 (an
even count): every row after a5_03 keeps its exact pair sequence; only a5_03's
internal pairing changes; total goes 1,846 → 1,847 pairs.
Repair code + asserts: `code/side-keyhunt/repair_parse.py` (all passing).
Canonical offsets: `code/side-keyhunt/repaired_offsets.json` (NOW CANONICAL —
supersedes `data/upstream-offsets.json` for all future work).
Full ruling: `code/side-keyhunt/methodology-ruling.md`.

## New canonical facts (0-based pair indices)
- **1,847 pairs** (not 1,846); same 96 groups; same pair IC (0.0142)
- `11 70 82 34 29 40` ("la première") at pairs **754** (row a5_03 — the actual
  gloss line) AND **1034** (row a6_03). The despatch says "la première" TWICE.
- Row a8_05 still ends with `46`; all other 69 rows byte-identical.
- Caveat: the manuscript images were not re-examined. If the a5_03 gloss
  line-tag is wrong, the old parse revives — this uncertainty is recorded, not
  resolved.

## Re-indexing rule (0-based pair indices, old → new)
- old n < 748 → new n (UNCHANGED — everything before row a5_03)
- 748 ≤ old n ≤ 772 → REPAIRED REGION (row a5_03 re-paired; values changed —
  do not shift, re-examine)
- old n ≥ 773 → new n+1 (values identical, index shifted)

## Remap table — every @-citation in code/crowd4/ (old → new)
No cited position falls in the repaired region.

| old | new | old | new | old | new |
|-----|-----|-----|-----|-----|-----|
| 0 | 0 | 507-509 | 507-509 | 1292 | 1293 |
| 1 | 1 | 508 | 508 | 1293 | 1294 |
| 1-2 | 1-2 | 509 | 509 | 1314 | 1315 |
| 46 | 46 | 571 | 571 | 1328 | 1329 |
| 73 | 73 | 578 | 578 | 1329 | 1330 |
| 81-83 | 81-83 | 650 | 650 | 1331 | 1332 |
| 144 | 144 | 665 | 665 | 1348 | 1349 |
| 148 | 148 | 684 | 684 | 1350 | 1351 |
| 150 | 150 | 712-715 | 712-715 | 1387 | 1388 |
| 160 | 160 | 790 | 791 | 1390 | 1391 |
| 161 | 161 | 801 | 802 | 1391 | 1392 |
| 210-211 | 210-211 | 837-838 | 838-839 | 1444 | 1445 |
| 290 | 290 | 848 | 849 | 1463 | 1464 |
| 291 | 291 | 960-962 | 961-963 | 1535 | 1536 |
| 295 | 295 | 1033 | 1034 | 1538 | 1539 |
| 360 | 360 | 1064 | 1065 | 1538-1540 | 1539-1541 |
| 407-408 | 407-408 | 1073-1076 | 1074-1077 | 1552-1554 | 1553-1555 |
| 453-454 | 453-454 | 1095 | 1096 | 1566-1567 | 1567-1568 |
| 478-481 | 478-481 | 1100 | 1101 | 1574 | 1575 |
| 507 | 507 | 1110-1112 | 1111-1113 | 1575 | 1576 |
| 1140 | 1141 | 1579-1580 | 1580-1581 | 1799 | 1800 |
| 1168 | 1169 | 1581-1584 | 1582-1585 | 1800 | 1801 |
| 1178 | 1179 | 1601-1602 | 1602-1603 | 1805 | 1806 |
| 1179 | 1180 | 1670-1671 | 1671-1672 | 1806 | 1807 |
| 1181 | 1182 | 1697-1699 | 1698-1700 | 1842-1843 | 1843-1844 |
| 1183 | 1184 | 1703-1705 | 1704-1706 | 1844-1845 | 1845-1846 |
| 1184 | 1185 | 1741 | 1742 | | |
| 1184-1187 | 1185-1188 | 1758-1760 | 1759-1761 | | |

Key landmarks: old "pair 1033" (the crib) → **1034**; old a8_05-end 1691 → **1692**;
old 77-78-94-82-06 ×2 @1179/@1350 → **@1180/@1351**; old @1741 (94-82-46) → **1742**;
old 87-64-77-84 @1799–1802 → **1800–1803**.
