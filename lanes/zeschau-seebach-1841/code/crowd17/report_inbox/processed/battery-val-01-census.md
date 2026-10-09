# Battery report: val-01-census

## Bar (verbatim, pre-registered)

"Census and name 01's value across its windows; a landed 01 value re-opens whether '[41]en'-style composition or a 41|01 boundary constrains 41's verb value."

Numbered clauses:
- C1: census 01 across all its windows (byte-exact, ±context, predecessor/follower distributions).
- C2: name 01's value uniformly across the windows at battery grade.
- C3: if a value lands, re-open the '[41]en'-style composition vs 41|01 boundary question for 41's verb value at @40.

Adverses (pre-registered): "A word-internal composition '[41]en'/'[41]tain' is unforced at battery grade (no composition evidence; 01 as letter cluster conflicts with its independent grouphood); 24's finite-verb class has section-7 tension with 'en' (red-team venue, not engaged here)."

## Method

Re-derived the repaired 1,847-pair / 96-type stream in-session from
`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`,
parsed like `code/side-keyhunt/repair_parse.py`. Asserts held (1,847 pairs,
96 types). `canonical.py` never used. All offsets below are 0-based unless
marked 1-based. Tested only 1841 diplomatic French.

## Census (C1 — PASS)

n(01) = 28. All windows byte-exact:

| 0b | 1b | row | window (±4) |
|---|---|---|---|
| 34 | 35 | a1_00 | 30 03 64 32 **01** 08 91 39 64 |
| 40 | 41 | a1_01 | 91 39 64 41 **01** 24 88 43 81 |
| 195 | 196 | a2_00 | 87 98 56 47 **01** 21 60 08 67 |
| 255 | 256 | a2_02 | 65 63 00 66 **01** 91 32 43 77 |
| 295 | 296 | a2_03 | 29 40 65 16 **01** 11 78 40 97 |
| 327 | 328 | a2_05 | 15 63 71 10 **01** 19 00 92 50 |
| 345 | 346 | a2_05 | 64 96 43 87 **01** 06 70 12 94 |
| 409 | 410 | a2_08 | 69 26 00 33 **01** 02 53 84 51 |
| 484 | 485 | a2_11 | 00 13 52 30 **01** 19 64 76 42 |
| 596 | 597 | a4_00 | 00 92 79 85 **01** 29 40 03 39 |
| 717 | 718 | a5_01 | 63 00 66 86 **01** 02 21 80 77 |
| 828 | 829 | a5_06 | 87 59 38 82 **01** 24 87 11 77 |
| 893 | 894 | a5_08 | 86 06 77 76 **01** 98 82 14 98 |
| 940 | 941 | a5_10 | 33 21 64 37 **01** 07 50 40 08 |
| 949 | 950 | a6_00 | 62 98 96 86 **01** 77 86 96 87 |
| 970 | 971 | a6_00 | 24 06 77 76 **01** 98 48 51 45 |
| 976 | 977 | a6_01 | 48 51 45 08 **01** 00 92 07 76 |
| 984 | 985 | a6_01 | 76 47 78 45 **01** 24 89 48 01 |
| 988 | 989 | a6_01 | 01 24 89 48 **01** 76 49 24 26 |
| 1029 | 1030 | a6_03 | 64 96 43 87 **01** 03 29 80 77 |
| 1255 | 1256 | a7_02 | 30 06 65 46 **01** 61 31 29 69 |
| 1261 | 1262 | a7_02 | 31 29 69 88 **01** 09 11 50 46 |
| 1440 | 1441 | a7_08 | 82 16 24 85 **01** 52 68 59 37 |
| 1462 | 1463 | a7_09 | 86 66 79 17 **01** 21 62 48 21 |
| 1634 | 1635 | a8_03 | 33 21 64 37 **01** 74 87 74 74 |
| 1653 | 1654 | a8_04 | 03 38 82 16 **01** 56 37 11 24 |
| 1731 | 1732 | a8_07 | 88 24 30 15 **01** 56 30 06 60 |
| 1818 | 1819 | a8_10 | 42 06 29 37 **01** 02 09 19 00 |

Predecessors (21 distinct): 37×3, 16×2, 87×2, 85×2, 86×2, 76×2, 32/41/47/66/10/33/30/82/08/45/48/46/88/17/15 ×1.
Followers (20 distinct): 24×3, 02×3, 21×2, 19×2, 98×2, 56×2, 08/91/11/06/29/07/77/00/76/03/61/09/52/74 ×1.

'37 01' ×3 (@940, @1634, @1818 — A12 frame "37-01 unit", value open).
'01 24' ×3 (@40, @828, @984). '41 01' ×1 (@40).

## Naming (C2 — FAIL)

Standing live candidates per the queue (R17-015 KILL CONFIRMED killed 01='ci'
and 01='faisant' globally; `rival-37-01-certain` KILL killed the local
'certain' reading): **'en'** and **'tain'**. A third rival, **'on'**, was
tested as a new candidate below.

### 01='en' (preposition, needs nominal complement, no determiner)

Kill-grade deaths (9 windows):
- @40 (a1_01): fol=24, whose fol=88≠85 → R24 finite/modal verb. "en [V-fin]"
  ungrammatical. (Double death: clitic order also bars postverbal 'en' on 41.)
- @295 (a2_03): fol=11='la' (banked GT). "en la" ungrammatical. DEAD.
- @596 (a4_00): fol=29='er' (pencil GT). "en er" ungrammatical. DEAD.
- @828 (a5_06): fol=24, fol=87≠85 → finite/modal. "en [V-fin]". DEAD.
- @893 (a5_08): fol=98='vient' (battery-grade). "en vient". DEAD.
- @949 (a6_00): fol=77='le' (provisional). "en le" ungrammatical. DEAD.
- @970 (a6_00): fol=98='vient'. "en vient". DEAD.
- @976 (a6_01): fol=00='pour' (granted). "en pour". DEAD.
- @984 (a6_01): fol=24, fol=89≠85 → finite/modal. "en [V-fin]". DEAD.

Sole clean leg: @988 (a6_01): fol=76 (promoted masculine noun) → "en [N-masc]"
is licensed ("en France"-shaped). The other 18 windows are undetermined
(open-value neighbors) or hostile.

'en' cannot be the uniform value: 9 kill-grade deaths.

### 01='tain' (bound syllable)

For a uniform 'tain', every window needs a composing neighbor under standing
values. Zero windows have one:
- No predecessor or follower has standing letter content completing a
  "-tain" word. The '37 01' ×3 windows would need 37='cer' — killed by
  `rival-37-01-certain` (no standing 'cer' license).
- @988's prev=48 is a cell, not the value 'e'; naming 48='e' is §3-barred.
- Follower cells are words/letters (11='la', 29='er', 00='pour', 98='vient'),
  none of which 'tain' can compose with ("tainla"/"tainer"/"tainpour" are not
  French words).

'tain' has zero positive legs under standing values. Kill-grade empty.

### 01='on' (new rival tested)

'on' + finite verb is grammatical; tested against all 28 windows.
Deaths: @34 (fol=08 letter-tier), @596 ("on er"), @976 ("on pour"),
@988 ("on [76-N]" — 'on' needs a verb), @1029 ("on [03]er" infinitive);
plus the three '37 01' unit windows are hostile under the A12 frame.
Lives: @40 ("[41] on [24-fin]"), @893/@970 ("on vient"), @984 ("on [24-fin]").
Killed at 5+ windows; also creates an unlicensed homophone with promoted
84="on" (A15) — red-team venue, not named here.

### C2 result

No candidate survives: 'en' (9 kills), 'tain' (0 legs), 'on' (5 kills +
homophony problem). **No uniform 01 value can be named at battery grade.**
C2 FAILS.

## C3 — does not fire

No 01 value landed, so the @40 '[41]en'-style composition vs 41|01 boundary
re-open does not fire.

## Adverses answered

- '[41]en'/'[41]tain' composition at @40: 01='en' dies at @40 twice over
  (finite-24 follower; preverbal-clitic order), 01='tain' has no composition
  leg anywhere. The adverse is answered: composition is unforced at battery
  grade; the default 41|01 boundary holds.
- 24's §7 tension with 'en': not engaged — the @40 kill rests on standing
  R24 (finite/modal 24), independent of any tension.

## Verdict: NULL

C1 PASS / C2 FAIL / C3 does not fire. Inconclusive: the census is complete
and the standing candidate inventory is exhausted, but no 01 value is named.
No standing or red-team verdict contradicted or downgraded; R17-015,
rival-37-01-certain, A12, A15, R24 all adopted; §7 intact; canonical-stream
caveat stands. R5005, sealed gates, red-team adjudication queue untouched.

## Follow-ups (all verified ABSENT from battery-queue.json)

1. `val-01-rival-sweep` (P3) — candidate-inventory sweep beyond en/tain/on:
   test letter-cluster hypotheses ('ain'/'ein'/'in'/'an') against the 14
   undetermined windows (@195, @255, @327, @409, @484, @717, @940, @1255,
   @1261, @1440, @1462, @1634, @1653, @1731, @1818); name iff one parses at
   all windows with zero kill-grade contradictions, else fence.
2. `redteam-01-split-input` (P2) — red-team evidence package (gather only):
   'en' survives cleanly only at @988; 'on' at @893/@970/@40; the three
   '37 01' windows need word-internal 01 under A12. Uniform value impossible
   under standing values → split/polyvalence venue for 01. Do not declare.
3. `val-01-40-41-boundary` (P3) — with no 01 value landed, test the @40
   '64 41 01 24 88' segmentation directly: fence the '[41]en'/'[41]tain'
   composition arms terminally, or find the one composition frame with a
   standing license.
