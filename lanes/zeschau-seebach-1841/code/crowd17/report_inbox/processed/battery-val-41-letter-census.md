# Battery verdict: val-41-letter-census

- Target: `val-41-letter-census` (battery-queue.json, priority 3, status queued)
- Claim: census 41's 19 windows for letter-cell vs word-cell behavior; a letter-cell 41 re-opens the @59 onset arm.
- Worker: 3d1ee4c4-e289-437a-8870-182f2d6d90c9. Date: 2026-10-09.
- Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`). Asserts held: 1,847 pairs, 96 types. `canonical.py` never used. R5005, sealed gates, red-team queue untouched.
- All @-offsets are 0-based pair indices in the repaired stream.

## Bar (verbatim, pre-registered)

"name 41's letter content iff a uniform letter parses with byte evidence at >=2 windows; else fence letter-cell-41."

**Restated as numbered pass/fail clauses (frozen before testing):**
1. **C1 (name arm):** a uniform letter for 41 parses with byte evidence at >=2 windows.
2. **C2 (fence arm):** if C1 fails, fence letter-cell-41 (the claim that 41 behaves as a letter cell).

## Method

1. Read BATTERY-PROTOCOL.md in full before testing.
2. Re-derived the repaired stream in-session; byte-exact census of all 19 windows of 41 with ±4 context.
3. Tested each window for letter-cell signatures: direct adjacency to banked GT letter cells (70=pre, 82=m, 34=i, 29=er, 40=e, 46=que), word-internal position, letter-doubling patterns.

## Findings

n(41)=19. All windows with ±4 context:

| @ | row | context |
|---|---|---|
| 5 | a1_00 | 00 97 51 **47 41 06** 77 78 18 |
| 39 | a1_01 | 08 91 39 **64 41 01** 24 88 43 |
| 59 | a1_01 | 58 35 53 **12 41 08** 34 29 40 |
| 91 | a1_02 | 77 66 98 **19 41 98** 81 97 46 |
| 237 | a2_01 | 71 51 70 **98 41 17** 11 26 12 |
| 444 | a2_09 | 98 80 50 **78 41 10** 62 61 59 |
| 489 | a2_11 | 19 64 76 **42 41 20** 67 78 42 |
| 589 | a3_02 | 18 14 00 **97 41 41** 09 00 92 |
| 590 | a4_00 | 14 00 97 **41 41 09** 00 92 79 |
| 808 | a5_05 | 53 69 24 **24 41 12** 48 24 65 |
| 964 | a6_00 | 96 00 86 **56 41 19** 24 06 77 |
| 1016 | a6_02 | 78 47 03 **24 41 15** 66 91 53 |
| 1048 | a6_04 | 11 67 76 **85 41 88** 29 40 29 |
| 1111 | a6_06 | 63 00 66 **73 41 65** 38 30 69 |
| 1472 | a7_10 | 62 38 26 **12 41 53** 60 06 67 |
| 1499 | a7_11 | 15 59 24 **89 41 74** 84 33 42 |
| 1508 | a7_11 | 33 00 86 **56 41 12** 61 59 39 |
| 1535 | a8_00 | 63 00 66 **73 41 62** 06 21 62 |
| 1759 | a8_08 | 85 58 17 **78 41 15** 93 06 77 |

**C1 FAIL — no letter can be named:**

1. **41 is never directly adjacent to a banked GT letter cell.** The adjacency scan over all 19 windows returns zero windows where 41's immediate neighbor is one of {70, 82, 34, 29, 40, 46}. No byte evidence exists for any letter content.
2. **@59 ("41 08 ière") is the only letter-shaped window, and it is already fenced.** 41's neighbors there are unvalued 12 and 08; the GT "ière" bytes sit two slots right. Naming any concrete onset (première, dernière, entière, lumière…) needs BOTH 41's and 08's letter content = 2 new assumptions. seg-41-08-leftedge (NULL, 2026-10-09) fenced @59 as residual on exactly this budget argument.
3. **"41 41" doubling (@589/@590) is non-discriminating.** `[97] 41 41 [09]` admits a doubled letter OR a doubled word ("très très" pattern); nothing names the letter.
4. **@5 ("ce [41] [06]") is stem-shaped at best, not letter evidence.** Even under the syllable-tier reading of 06 attaching left ("-ent"), 41 would be a stem, not a named letter — and that reading was established for the five '42 06' windows, not for '41 06'.
5. **Word-cell legs are abundant and clean:** @39 "qui [41]" (64=qui granted requires standalone), @91 "[19] [41] vient", @237 "[98] [41] fois", @808/@1016 "en [41] X" (24=en battery-grade). Nothing in the census forces 41 letter-cell anywhere.

**C2 FIRES: letter-cell-41 is fenced.** The census finds zero windows where 41 must be a letter cell, zero byte evidence for any letter content, and the single letter-shaped locus (@59) is already fenced as residual. The §7 split venue (R20-108/R20-082) is untouched — this fence covers the letter-cell arm only, not 41's split candidacy.

Adverses answered: 41's letter content remains non-standing (confirmed — nothing namable); the split question stays red-team venue per §7, not decided here. No standing/red-team verdict contradicted or downgraded; canonical-stream caveat stands.

## Verdict: NULL (fence executed)

C1 fails (no uniform letter namable at battery grade); C2 fires — letter-cell-41 fenced. The fence does not close word-cell-41, the §7 split, or 41's value.

## Follow-ups proposed (all verified ABSENT from battery-queue.json)

1. `val-41-word-census` (P3) — test word-cell-41: census which windows force standalone-word 41 (@39 "qui [41]", @808/@1016 "en [41]") vs merely admit it; name 41's word-class with standing values.
2. `seg-41-41-double` (P4) — decide the "41 41" doubling @589/@590: word repetition vs doubled letter; byte-evidence test.
3. `reseg-41-06-05` (P4) — test the @5 "47 41 06" window: does 06's syllable-tier "-ent" attach left, making 41 stem-shaped there (stem-42-verb analog)?

## Bookkeeping

- `battery-queue.json`: `val-41-letter-census` queued → verdict/null (temp-file + rename, own entry only; pre-write assert confirmed queued/verdictless; JSON re-validated; no downgrade).
- Lock `locks/val-41-letter-census.lock`: created on start, deleted on completion.
- R5005, sealed gates, red-team adjudication queue untouched.
