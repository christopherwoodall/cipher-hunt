# Battery verdict: ce-complement-86-negative

**Target:** sweep ALL 86 windows stream-wide for any 'ce'-group complement (87/47/45).
**Date:** 2026-10-09

## Bar (verbatim from battery-queue.json)

"a clean negative hardens the '86 never ce' arm"

**Numbered clauses:**
1. PASS/FAIL — the stream-wide sweep of 86's windows finds zero 'ce'-group (87/47/45) complements of 86 → clean negative, hardening the arm.

## Method

- Read BATTERY-PROTOCOL.md first; created `locks/ce-complement-86-negative.lock` on start.
- Re-derived the repaired 1,847-pair / 96-type stream in-session from
  `data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`,
  parsed per `code/side-keyhunt/repair_parse.py` (1,847 pairs verified).
- `canonical.py` never used. R5005, sealed gates, red-team queue untouched.
- "Complement" = direct successor (offset +1) of 86. A ce-group at +2 with a
  non-ce intervening group is not a complement; fenced with cause below.

## Sweep (1-based @-offsets, all 32 windows of 86)

| @ | row | window | direct follower |
|---|---|--------|-----------------|
| 176 | a1_05 | 87 86 21 | 21 |
| 301 | a2_04 | 97 86 91 | 91 |
| 432 | a2_09 | 77 86 29 | 29='er' (banked GT) |
| 554 | a3_01 | 00 86 59 | 59 |
| 558 | a3_01 | 17 86 94 | 94 ('ne' lead, not a ce-group) |
| 662 | a4_02 | 00 86 50 | 50 |
| 672 | a5_00 | 11 86 24 | 24 |
| 717 | a5_01 | 66 86 01 | 01 |
| 729 | a5_02 | 00 86 48 | 48 |
| 800 | a5_04 | 77 86 44 | 44 |
| 868 | a5_07 | 00 86 70 | 70='pre' (banked GT); 87 at +2 |
| 879 | a5_08 | 77 86 78 | 78 |
| 890 | a5_08 | 00 86 06 | 06 |
| 900 | a5_08 | 83 86 16 | 16 |
| 949 | a5_10 | 96 86 01 | 01 |
| 952 | a6_00 | 77 86 96 | 96='par' (banked GT); 87 at +2 |
| 963 | a6_00 | 00 86 56 | 56 |
| 1003 | a6_02 | 00 86 56 | 56; 47 at +2 |
| 1100 | a6_06 | 67 86 52 | 52 |
| 1129 | a6_07 | 00 86 52 | 52 |
| 1132 | a6_07 | 37 86 24 | 24 |
| 1135 | a6_08 | 77 86 20 | 20 |
| 1148 | a6_08 | 98 86 67 | 67 |
| 1336 | a7_05 | 83 86 71 | 71 |
| 1346 | a7_05 | 47 86 66 | 66 |
| 1376 | a7_06 | 00 86 29 | 29 |
| 1392 | a7_07 | 67 86 29 | 29 |
| 1459 | a7_09 | 67 86 66 | 66 |
| 1507 | a7_11 | 00 86 56 | 56 |
| 1740 | a8_07 | 52 86 12 | 12 |
| 1793 | a8_09 | 00 86 56 | 56 |
| 1826 | a8_11 | 00 86 29 | 29 |

**Result: 0/32 windows have a ce-group (87/47/45) as direct successor of 86.**
Direct followers observed: {21, 91, 29, 59, 94, 50, 24, 01, 48, 44, 70, 78,
06, 16, 96, 56, 52, 20, 67, 71, 66, 12} — no 87, no 47, no 45.

## Fenced with cause (not complements)

- **@868:** "00 86 70 87" = "pour [86] pre ce". 70='pre' banked GT intervenes;
  87 is the follower of 70, not of 86.
- **@952:** "77 86 96 87" = "le [86] par ce". 96='par' banked GT intervenes.
- **@1003:** "00 86 56 47" = "pour [86] [56] ce". 56 (value open) intervenes.
- Predecessor ce-groups are not complements: @176 "87 86 21" ('ce' before
  86 = determiner/subject slot, 86 is the governed element) and @1346
  "47 86 66" (same geometry). The arm is "86 never *takes* ce", so these are
  out of scope, noted for completeness.

## Clause results

1. **PASS — clean negative.** 0/32 windows show 86 with a ce-group complement.
   The three +2 contacts are each broken by an intervening granted/banked group
   (70='pre', 96='par') or an open-value group (56).

## Verdict: PROMOTE (finding grade)

The '86 never ce' arm is hardened at battery grade: no ce-group complement
attaches to 86 anywhere in the stream. Promotes no value, kills nothing,
declares no polyvalence (§7 intact). No standing verdict contradicted or
downgraded. No red-team verdict on 86's complements exists.

## Bookkeeping

`battery-queue.json`: `ce-complement-86-negative` → status `verdict`,
result `promote`, date 2026-10-09. Lock created on start, deleted on
completion. No follow-ups required (promote, not null).
