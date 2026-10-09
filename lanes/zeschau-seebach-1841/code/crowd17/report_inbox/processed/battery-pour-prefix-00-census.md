# Battery verdict: pour-prefix-00-census — rescue 2c closed terminally

Target: `pour-prefix-00-census` (priority 3).
Parent: `battery-par-pour-962-adjudicate.md` (NULL), follow-up item 2.
Date: 2026-10-09.

## Bar (verbatim, pre-registered)

"Close rescue 2c terminally."

Numbered clauses:
- C1: census all 55 windows of cell 00 on the repaired stream, each with its
  follower cell and the follower's standing content.
- C2: test every window for a battery-licensable syllabic "pour-" composition
  ("pourvoir"/"pourtant"/"pourquoi"-shaped) using only standing named values.
- C3: if zero windows compose, rescue 2c is closed terminally; state the
  re-open condition explicitly.

Rescue 2c (parent definition): 00 read as the word-internal syllable "pour-"
(prefix of "pourvoir"/"pourtant"/"pourquoi"), offered as a general rescue for
the "96 00" adjacency. The parent killed it as a general rescue and queued
this census to close it terminally across all 00 windows.

## Method

Re-derived the repaired 1,847-pair / 96-type stream in-session from
`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`,
parsed like `code/side-keyhunt/repair_parse.py`. Asserts held
(1,847 pairs, 96 types). `canonical.py` never used. R5005, sealed gate
instances, and the red-team adjudication queue untouched.

Offsets below are 0-based indices of the 00 cell. Standing content used
(BATTERY-PROTOCOL.md §7): pencil GT 11=la, 70=pre, 82=m, 34=i, 29=er, 40=e,
46=que; granted 87=ce, 64=qui, 96=par, 17=fois, 79="tout", 00="pour", 84="on",
47="ce"; provisional 59=est, 77="le". Battery-grade leads: 86="entr",
98="vient", 06="ent".

Composition test: "pour" + follower's named content must spell a real French
word beginning "pour-". Words checked: pourpre, pourquoi, pourvoir, pourtant,
pourvu, poursuite, pourboire, pourchasser, pourtour, pourri, pourcent,
pourparler, pourfendre, pourlécher, pourpoint, pourceau.

## Census: all 55 windows

n(00) = 55, byte-confirmed. Follower distribution:

| follower | standing content | "pour"+content | windows (0-based) | n |
|---|---|---|---|---|
| 86 | "entr" (lead; rival "voi" unratified) | "pourentr-" no word | 552, 660, 727, 866, 888, 961, 1001, 1127, 1374, 1505, 1791, 1824 | 12 |
| 33 | open | n/a (no named content) | 185, 407, 466, 845, 935, 1087, 1244, 1629 | 8 |
| 66 | open | n/a | 188, 245, 253, 714, 1108, 1493, 1532 | 7 |
| 92 | open | n/a | 48, 329, 592, 682, 977, 1153 | 6 |
| 97 | open | n/a | 1, 287, 587, 1822 | 4 |
| 11 | la | "pourla" no word | 76, 378, 1287, 1405 | 4 |
| 46 | que | "pourque" no word | 106, 545, 1545, 1680 | 4 |
| 36 | open | n/a | 739, 1312, 1584 | 3 |
| 34 | i | "pouri" no word | 27 | 1 |
| 64 | qui | "pourqui" no word | 748 | 1 |
| 67 | et/veut | "pouret"/"pourveut" no word | 1247 | 1 |
| 98 | "vient" (lead) | "pourvient" no word | 1138 | 1 |
| 13 | open | n/a | 480 | 1 |
| 20 | open | n/a | 667 | 1 |
| 44 | open | n/a | 1602 | 1 |

Total: 12+8+7+6+4+4+4+3+1+1+1+1+1+1+1 = 55. ✓

Window contexts (±3), 0-based, for the record:

- @1 (a1_00): 09 | 00 | 97 51 47
- @27 (a1_00): 33 55 81 | 00 | 34 24 30
- @48 (a1_01): 30 62 96 | 00 | 92 79 37
- @76 (a1_02): 24 87 11 | 00 | 11 29 42
- @106 (a1_03): 59 45 28 | 00 | 46 11 21
- @185 (a1_05): 23 37 06 | 00 | 33 16 00
- @188 (a1_05): 00 33 16 | 00 | 66 24 87
- @245 (a2_02): 16 56 43 | 00 | 66 91 32
- @253 (a2_02): 94 65 63 | 00 | 66 01 91
- @287 (a2_03): 52 89 28 | 00 | 97 09 64
- @329 (a2_05): 10 01 19 | 00 | 92 50 45
- @378 (a2_07): 85 82 48 | 00 | 11 50 82
- @407 (a2_08): 34 69 26 | 00 | 33 01 02
- @466 (a2_10): 59 42 96 | 00 | 33 79 80
- @480 (a2_11): 74 45 93 | 00 | 13 52 30
- @545 (a3_01): 48 42 06 | 00 | 46 24 47
- @552 (a3_01): 46 55 81 | 00 | 86 59 34
- @587 (a3_02): 19 18 14 | 00 | 97 41 41
- @592 (a4_00): 41 41 09 | 00 | 92 79 85
- @660 (a4_02): 03 62 16 | 00 | 86 50 80
- @667 (a4_02): 03 62 06 | 00 | 20 67 11
- @682 (a5_00): 23 09 07 | 00 | 92 64 29
- @714 (a5_01): 71 12 63 | 00 | 66 86 01
- @727 (a5_02): 65 64 11 | 00 | 86 48 88
- @739 (a5_02): 18 82 06 | 00 | 36 20 30
- @748 (a5_03): 81 85 28 | 00 | 64 02 97
- @845 (a5_06): 26 12 16 | 00 | 33 96 40
- @866 (a5_07): 48 47 46 | 00 | 86 70 87
- @888 (a5_08): 37 03 02 | 00 | 86 06 77
- @935 (a5_10): 56 69 26 | 00 | 33 21 64
- @961 (a6_00): 20 67 96 | 00 | 86 56 41
- @977 (a6_01): 45 08 01 | 00 | 92 07 76
- @1001 (a6_02): 96 82 33 | 00 | 86 56 47
- @1087 (a6_05): 02 55 81 | 00 | 33 79 80
- @1108 (a6_06): 78 65 63 | 00 | 66 73 41
- @1127 (a6_07): 52 37 43 | 00 | 86 52 37
- @1138 (a6_08): 20 62 98 | 00 | 98 78 62
- @1153 (a6_09): 66 84 02 | 00 | 92 29 80
- @1244 (a7_01): 81 87 11 | 00 | 33 16 00
- @1247 (a7_01): 00 33 16 | 00 | 67 46 26
- @1287 (a7_03): 98 55 68 | 00 | 11 17 84
- @1312 (a7_04): 30 92 44 | 00 | 36 74 62
- @1374 (a7_06): 91 67 98 | 00 | 86 29 89
- @1405 (a7_07): 81 87 11 | 00 | 11 95 46
- @1493 (a7_10): 92 39 24 | 00 | 66 15 59
- @1505 (a7_11): 33 42 33 | 00 | 86 56 41
- @1532 (a8_00): 21 65 63 | 00 | 66 73 41
- @1545 (a8_00): 77 78 43 | 00 | 46 70 12
- @1584 (a8_02): 53 12 44 | 00 | 36 70 64
- @1602 (a8_02): 81 82 98 | 00 | 44 70 39
- @1629 (a8_03): 56 69 26 | 00 | 33 21 64
- @1680 (a8_05): 74 77 44 | 00 | 46 79 65
- @1791 (a8_09): 68 47 03 | 00 | 86 56 42
- @1822 (a8_11): 02 09 19 | 00 | 97 00 86
- @1824 (a8_11): 19 00 97 | 00 | 86 29 82

## Per-clause findings

**C1 — PASS.** All 55 windows censused byte-exact with follower cells.

**C2 — PASS (zero legs).**
- 12 windows have followers with named non-composing content: 11=la (×4),
  46=que (×4), 34=i (×1), 64=qui (×1), 67=et/veut (×1), 98="vient" (×1 lead).
  "pourla", "pourque", "pouri", "pourqui", "pouret"/"pourveut", "pourvient"
  are not French words. The syllabic reading is excluded at these windows at
  kill grade.
- 29 windows have followers with open values (33 ×8, 66 ×7, 92 ×6, 97 ×4,
  36 ×3, 13 ×1, 20 ×1, 44 ×1). A composition claim here would need a value
  invented at battery grade — barred by §3. No leg.
- 12 windows have follower 86 ("00 86"). Under the standing lead 86="entr",
  "pourentr-" starts no French word. The only compositional rival is the
  unratified 86="voi" ("pourvoir"/"pourvoient"), which belongs to the standing
  `voir-86-sweep` NULL verdict — cited, not re-litigated here.
- Three-cell shapes checked for all named followers ("00 11 29", "00 34 24",
  "00 46 70", "00 64 02", "00 67 46", "00 98 78", "00 86 70", "00 86 06",
  "00 86 56", "00 86 50", "00 86 48", "00 86 52", "00 86 29"): none composes
  a French word ("pourceau" would need a "00 87/47" window; zero exist).
- The single strongest possible leg, "00 70" = "pourpre" (70="pre" pencil GT),
  has **zero windows** stream-wide.

**C3 — FIRES.** Zero battery-licensable syllabic "pour-" compositions across
all 55 windows. Rescue 2c is closed terminally as a general rescue.

## Verdict: KILL (rescue 2c)

Rescue 2c is dead at kill grade under all standing values. Scope and
carve-outs:

- Killed: 00 as the syllabic prefix "pour-" anywhere in the stream. The
  "96 00" adjacency cannot be rescued by a prefix reading of 00.
- Not re-litigated: the "00 86" ×12 family is owned by the standing
  `voir-86-sweep` NULL (86="voi" rival) and the red-team 86 docket
  (`redteam-889-pourvoient`, P1, queued). A standing naming act on 86 (or on
  any other 00-follower) as a pour-compatible syllable would re-open only
  that window family, not the general rescue.
- Untouched: 00="pour" (A9, leg-1 class-level); all standing values, splits,
  holds, and kills. No standing or red-team verdict contradicted or
  downgraded. §7 intact. Canonical-stream caveat stands.

Per §4, kills regenerate no follow-ups.

## Bookkeeping

- Stream: repaired 1,847-pair parse, asserts held; `canonical.py` never used.
- Lock created on start, deleted on completion. R5005, sealed gates, red-team
  adjudication queue untouched.
