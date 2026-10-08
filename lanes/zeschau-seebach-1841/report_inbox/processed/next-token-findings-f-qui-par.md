# Finder report: f-qui-par full read (43/01 profiles)

Date: 2026-10-08. Beat: f-qui-par (wave 2). Finder worker.
Stream: repaired 1,847-pair parse (`data/upstream-ct_R5005.txt` +
`code/side-keyhunt/repaired_offsets.json`, parsed per
`code/side-keyhunt/repair_parse.py`). Never `canonical.py`. Offsets are
0-indexed pair positions. Standing constraints per BATTERY-PROTOCOL.md §7
apply (banked GT, grants, kills, holds). No re-litigation of settled kills.
No promotion by this report — ranked targets only.

## (a) Method

1. Extract every 43 (n=16) and 01 (n=28) occurrence ±3 groups from the
   repaired stream.
2. Cluster by follower pattern FIRST, then by predecessor pattern.
3. De-duplicate formula windows before counting productive frames: the
   byte-identical 6-gram `45-64-96-43-87-01` ×2 (@340, @1024) counts once;
   the byte-identical `la-52-37-43` 4-gram ×2 (@1123, @1721) counts once;
   the adjacent `43-21-43` doublet (@1303/@1305) counts once.
   Productive frames: 43 → 13; 01 → 26.
4. Predict plaintext from 1840s French diplomatic register.
5. Rank targets by confidence × testability. State cipher-testable
   consequences per target. Coordinate with queued `noun-43`,
   `ci-01-value`, `ce-frame-45-64-96-43-87-01` (feeder/narrower targets,
   no duplication, no preemptive value promotion).

## (b) Window census

### 43 — 16 occurrences

| @ | row | window (±3) |
|---|---|---|
| 21 | a1_00 | 82(m)-**43**-29(er)-47(ce) |
| 43 | a1_01 | 88-**43**-81-30(pas) |
| 244 | a2_02 | 56-**43**-00(pour)-66 |
| 258 | a2_02 | 32(pred)-**43**-77(le)-84(on) |
| 343 | a2_05 | 45-64(qui)-96(par)-**43**-87(ce)-01 [6-gram F1] |
| 386 | a2_07 | 37(pred)-**43**-91-36 |
| 439 | a2_09 | 46(que)-**43**-98-80(verb) |
| 563 | a3_02 | 11(la)-**43**-24-80(verb) |
| 1027 | a6_03 | 45-64(qui)-96(par)-**43**-87(ce)-01 [6-gram F2] |
| 1092 | a6_06 | 06-**43**-07-55 |
| 1126 | a6_07 | 11(la)-52-37(pred)-**43**-00(pour)-86(INF) |
| 1204 | a7_00 | 47(ce)-**43**-55-61 |
| 1303 | a7_03 | 08-**43**-21-**43**-77(le) [doublet, first] |
| 1305 | a7_04 | 43-21-**43**-77(le)-74 [doublet, second] |
| 1544 | a8_00 | 78-**43**-00(pour)-46(que)-70(pre) |
| 1724 | a8_07 | 11(la)-52-37(pred)-**43**-98-39 |

### 01 — 28 occurrences

| @ | row | window (±3) |
|---|---|---|
| 34 | a1_00 | 32(pred)-**01**-08-91 |
| 40 | a1_01 | 41-**01**-24-88 |
| 195 | a2_00 | 47(ce)-**01**-21-60 |
| 255 | a2_02 | 66-**01**-91-32(pred) |
| 295 | a2_03 | 16-**01**-11(la)-78 |
| 327 | a2_05 | 10-**01**-19-00(pour) |
| 345 | a2_05 | 43-87(ce)-**01**-06 [6-gram F1] |
| 409 | a2_08 | 33-**01**-02-53 |
| 484 | a2_11 | 30(pas)-**01**-19-64(qui) |
| 596 | a4_00 | 85(stem)-**01**-29(er)-40(e) |
| 717 | a5_01 | 86-**01**-02-21 |
| 828 | a5_06 | 82(m)-**01**-24-87(ce)-11(la) |
| 893 | a5_08 | 76-**01**-98-82(m) |
| 940 | a5_10 | 37-**01**-07-50 |
| 949 | a6_00 | 86-**01**-77(le)-86 |
| 970 | a6_00 | 76-**01**-98-48 |
| 976 | a6_01 | 08-**01**-00(pour)-92 |
| 984 | a6_01 | 45-**01**-24-89 |
| 988 | a6_01 | 48-**01**-76-49 |
| 1029 | a6_03 | 43-87(ce)-**01**-03 [6-gram F2] |
| 1255 | a7_02 | 46(que)-**01**-61-31 |
| 1261 | a7_02 | 88-**01**-09-11(la) |
| 1440 | a7_08 | 85(stem)-**01**-52-68 |
| 1462 | a7_09 | 17(fois)-**01**-21-62 |
| 1634 | a8_03 | 37-**01**-74-87(ce) |
| 1653 | a8_04 | 16-**01**-56-37 |
| 1731 | a8_07 | 15-**01**-56-30(pas) |
| 1818 | a8_10 | 29(er)-37-**01**-02-09 |

## (c) Follower/predecessor clustering

### 43 — follower clusters

| follower | n | windows |
|---|---|---|
| 87 (6-gram) | 2 | @343, @1027 — formula, `par-43-ce-01` |
| 00 (pour) | 3 | @244 `56-43-pour-66`; @1126 `37-43-pour-86(INF)`; @1544 `78-43-pour-que` |
| 98 | 2 | @439 `que-43-98-verb`; @1724 `37-43-98-39` |
| 77 (le) | 2 | @258 `32-43-le-on`; @1305 `43-21-43-le` |
| 29 (er) | 1 | @21 `m-43-er-ce` |
| 81 | 1 | @43 `88-43-81-pas` |
| 91 | 1 | @386 `37-43-91-36` |
| 24 | 1 | @563 `la-43-24-verb` |
| 07 | 1 | @1092 `06-43-07-55` |
| 55 | 1 | @1204 `ce-43-55-61` |
| 21 | 1 | @1303 `08-43-21-43` (doublet) |

Predecessor profile is flat (96×2, 37×2, rest ×1: 82, 88, 56, 32, 38, 46,
11, 06, 47, 08, 21, 78) — content-word shape, not function-word shape.
Determiner support for feminine noun: `la-43` @563; `la-52-37-43`
byte-identical ×2 (@1123, @1721). Predicative-adjacent: `37-43` ×3
(@385, @1125, @1723), `32-43` ×1 (@257) — predicative frames 37/32
directly precede 43 four times.

### 01 — follower clusters

| follower | n | windows |
|---|---|---|
| 24 | 3 | @40 `41-01-24-88`; @828 `m-01-24-ce-la`; @984 `ce-01-24-89` |
| 02 | 3 | @409 `33-01-02-53`; @717 `86-01-02-21`; @1818 `37-01-02-09` |
| 06 | 2 | @345, @1029 — both inside the 6-gram (`ce-01-06`) |
| 19 | 2 | @327 `10-01-19-pour`; @484 `pas-01-19-qui` |
| 21 | 2 | @195 `ce-01-21-60`; @1462 `fois-01-21-62` |
| 98 | 2 | @893, @970 — both `76-01-98` (same predecessor too) |
| 56 | 2 | @1653 `16-01-56-37`; @1731 `15-01-56-pas` |
| rest | ×1 | 08, 11(la), 91, 77(le), 00(pour), 76, 03, 61, 09, 52, 74, 07, 29(er) |

### 01 — predecessor clusters

| predecessor | n | windows |
|---|---|---|
| 37 | 3 | @940, @1634, @1818 — the `37-01` unit (A12); ×2 `qui-37-01`, ×1 `er-37-01` |
| 87 (ce) | 2 | @345, @1029 — 6-gram |
| 76 | 2 | @893, @970 — `76-01-98` ×2 |
| 16 | 2 | @295 `16-01-la`; @1653 `m-16-01-56` |
| 30 (pas) | 2 | @484 `pas-01-19`; @1731 `pas-15-01-56` |
| 86 | 2 | @717 `86-01-02`; @949 `86-01-le` |
| 47 (ce) | 1 | @195 `ce-01-21` |
| 45 (ce) | 1 | @984 `ce-01-24` |
| rest | ×1 | 32(pred), 41, 66, 10, 33, 82(m), 08, 48, 17(fois), 88, 46(que), 85(stem), 89 |

Key structural facts:
- **Triple-`ce` composition.** All three `ce`-values compose with 01:
  `87-01` ×2, `47-01` ×1 (@195), `45-01` ×1 (@984). Parallel to granted
  `cela` = 87+11. This is the strongest structural leg for 01=`ci`.
- **`01-24` ×3 is the hardest cluster.** Under 01=`ci`, `ci-24` needs
  24 ∈ {contre, après, joint, dessus, inclus}-family — but 24's contact
  profile (`24-ce` ×10, `ne-24-ce` ×2, `on-24-37` ×2, `la-24` ×4)
  rejects dessus/joint/inclus and strains contre/après.
- **`37-01` ×3 needs nominal-37 for `[37]-ci`** (ungranted; A1 grants only
  the predicative frame, value open). Rival local reading: 37-01 =
  `certain` (37=`cer`, 01=`tain`) — but `tain` has zero support outside
  37-01, and `87-01`/`47-01`/`45-01` cannot be `ce-tain`.
- **Outside the four `ce`-compositions, `ci` parses in ~0/24 remaining
  windows** (`m-ci-24`, `pas-ci-19`, `85-ci-er-e`, `fois-ci-21` all dead).
  `faisant` parses in `ce faisant` ×2–4 but dies on `37-faisant`,
  `01-24`, `85-faisant-52`. Neither rival is global.

## (d) Ranked battery targets

### T1 — feeder-ceci-47-45 (priority 2)
- **Claim:** `47-01` (@195) and `45-01` (@984) read `ceci`, doubling the
  `ceci`-composition evidence base from 2× to 4× for `ci-01-value`.
- **Bars:** promote-feed iff (a) @195 `47-01-21-60` parses as
  `ceci [21] [60]` with 21/60's slots stated; (b) @984 `45-01-24-89`
  parses as `ceci [24] [89]` with 24/89's slots stated; (c) neither
  window forces non-`ceci`. Null if either window resists with a stated
  cause (feeds back as adverse to `ci-01-value`).
- **Evidence:** `87-01` ×2 granted-parallel (`cela` = 87+11); 47=`ce`
  (A4), 45=`ce` (A11 HOLD) — all three `ce`-values take 01.
- **Adverses:** `01-24` @984 (`ceci-24` needs 24 named — see T2);
  `ceci [21]` @195 needs 21's slot (21→67 ×8).

### T2 — disc-01-24-ci-X (priority 2)
- **Claim:** `01-24` ×3 decides between 01=`ci` (then 24 ∈
  contre/après-family) and a non-`ci` 01 (then `ci-24` is dead and the
  `ceci` reading retreats to `ce`-compositions only).
- **Bars:** resolve iff (a) 24 is named with all three `01-24` windows
  parsing (`41-01-24-88` @40, `m-01-24-ce-la` @828,
  `ce-01-24-89` @984); (b) the named 24 coheres with its full contact
  profile (`24-ce` ×10, `ne-24-ce` ×2, `on-24-37` ×2, `la-24` ×4,
  `24-24` @806); (c) the verdict states the consequence for
  `ci-01-value` explicitly.
- **Evidence:** ×3 repetition of an otherwise flat-distribution bigram;
  @828 gives `01-24-ce-la-le` (`cela`=87-11 inside the window).
- **Adverses:** `24-ce` ×10 kills `ci-dessus`/`ci-joint`/`ci-inclus`;
  `m-01-24` @828 resists most 24 values; 24's class is open
  (`ne-24-profile` queued).

### T3 — rival-37-01-certain (priority 3)
- **Claim:** `37-01` ×3 is the local word `certain` (37=`cer`,
  01=`tain`), NOT evidence for a global 01 value.
- **Bars:** resolve iff (a) all three windows parse with `certain`
  grammatically integrated (`qui-certain-07` @940, `qui-certain-74`
  @1634, `er-certain-02` @1818 — state how `qui`+adjective and
  `er`+`certain` integrate); (b) the verdict states the consequence:
  either `tain` stays local (01 keeps `ci`/`faisant` globally) or
  `certain` is killed and `37-01` returns to the `ci-01-value` bar.
- **Evidence:** A12 promotes 37-01 as a unit; `21-qui-37-01`
  byte-identical ×2; `cer-tain` is phonotactically clean.
- **Adverses:** `qui certain` needs nominal-37 or `est`-ellipsis
  (ungranted); `tain` has no support outside 37-01; `87-01`/`47-01`/
  `45-01` cannot be `ce-tain` — a global 01=`tain` is already dead,
  only the local reading is live.

### T4 — frame-43-la-52-37 (priority 2)
- **Claim:** `la-52-37-43` byte-identical ×2 (@1123, @1721) is a
  determiner frame for noun-43; the divergent continuations
  (`pour-86-INF` @1126 vs `98-39` @1724) discriminate 43's value.
- **Bars:** resolve iff (a) 52 (or the 52-37 unit) is named with both
  windows parsing; (b) one 43 value satisfies BOTH continuations
  (`43-pour-[86-INF]` and `43-98-39`); (c) feminine agreement via
  `la` (11) holds.
- **Evidence:** byte-identical 4-gram ×2 (formula-grade); `86` is
  INF-class (A9-adjacent) so `pour-86` = purpose clause; feeds queued
  `noun-43` (candidates {suite, condition, maniere, mesure}).
- **Adverses:** 52's value open; 37 predicative-vs-nominal tension
  (A1 frame grant vs nominal slot here); none of the four queued
  candidates takes `pour`+INF naturally (`de`-government instead) —
  the frame may kill all four.

### T5 — frame-43-21-43-doublet (priority 3)
- **Claim:** `43-21-43-le` (@1303–1306) is a coordination/reduplication
  frame; both 43 slots must take the SAME value (same-word test).
- **Bars:** resolve iff (a) 21 is named (coordination vs preposition)
  with `08-43-21-43-77(le)-74` parsing; (b) both 43 slots take one
  value — if different values are needed, kill the coordination
  reading with cause; (c) the `pre-37-08` left edge (@1300–1302,
  70=`pre`) is parsed or fenced.
- **Evidence:** only same-group doublet of 43 in the stream;
  `le` (77) closes the frame; `pas` (30) follows at @1309.
- **Adverses:** 21's value open (21→67 ×8, 21→62 ×5); `43-21-43`
  has no second instance.

### T6 — frame-43-pour-que-1544 (priority 3)
- **Claim:** `78-43-pour-que-pre-n-ne` (@1544–1549) is the `pour que`
  discriminator for noun-43: name 43 or kill the queued candidates.
- **Bars:** resolve iff (a) 43 is named (from {suite, condition,
  maniere, mesure} or new) with `X pour que [subjunctive]` parsing;
  (b) 78's slot is stated (verb like `faire`? determiner?); (c) the
  parse is consistent with the prenne battery's finding (subject slot
  empty, 92 nominal — `battery-prenne-70-12-94`, null).
- **Evidence:** `00`=`pour` (A9), `46`=`que` (GT) — the `pour que`
  bigram is solid; `43-pour` ×3 total (@244, @1126, @1544).
- **Adverses:** `pour que` after a bare noun is unidiomatic for all
  four queued candidates; prenne battery found no licensable subject;
  78's value open (`ver-78` queued).

### T7 — frame-43-pred-37-32 (priority 3)
- **Claim:** predicative 37/32 directly precedes 43 four times
  (`37-43` ×3 @385/@1125/@1723, `32-43` ×1 @257) — adjective+noun or
  compound; constrains 43's class.
- **Bars:** resolve iff (a) all four windows parse under one
  structural reading (predicative-adjective + noun vs compound word
  vs 43-as-infinitive); (b) the reading coheres with A1's
  predicative-frame grant for 37/32 (frame only, value open —
  no re-litigation); (c) `43`'s noun-hood vs verb-hood is stated
  with the `la-43` frames as control.
- **Evidence:** ×4 same-slot adjacency; `32-43-le-on` @258 and
  `37-43-pour-INF` @1126 give two different right edges.
- **Adverses:** 37's value open (`frame-37-reexam` queued);
  `06-43-07` @1092 and `ce-43-55` @1204 lack predicative left edges.

### T8 — coll-76-01-98 (priority 4)
- **Claim:** `76-01-98` ×2 (@892, @969) is a same-cluster collocation
  (`le-76-01-98-m` / `le-76-01-98-48`).
- **Bars:** resolve iff (a) both windows parse under ONE reading
  (unit vs `le-[76] [01] [98]` composition); (b) the `le-76` left
  edge and the divergent right edges (`98-m` vs `98-48`) are stated.
- **Evidence:** identical predecessor AND follower (strongest
  same-group cluster for 01 outside the 6-gram).
- **Adverses:** 76's class open (`frame-76-tension` queued);
  only ×2.

## (e) Residual uncertainty

1. **01 has no global value.** `ci` wins the four `ce`-compositions
   (T1) but parses ~0/24 remaining windows; `faisant` wins `ce faisant`
   but dies on `37-01`, `01-24`, `85-01-52`. The honest state: 01's
   value is local to its frames until T2/T3 adjudicate. Polyvalence
   (per the 67 precedent) is NOT proposed — red-team call only.
2. **43's queued candidates are all adversed by `43-pour` ×3.**
   {suite, condition, maniere, mesure} govern `de`, not `pour`/`pour
   que`. T4/T6 may kill all four; the replacement must be a feminine
   noun taking `pour`+INF — or the `pour` frames need re-segmentation.
3. **Elision is invisible in the cipher.** `que-43`/`m-43`/`la-43`
   cannot test vowel-initial 43 (no elision marking) — do not propose
   elision-based bars.
4. **Formula de-dup applied:** 6-gram ×2 → 1; `la-52-37-43` ×2 → 1;
   `43-21-43` doublet → 1. Productive frames: 43 → 13, 01 → 26.
5. **Not touched:** R5005, sealed gates, red-team queue, settled kills
   (81=`prin`, 48-values, 09/92 `-ère`, 84=`fait`), `noun-43`/
   `ci-01-value`/`ce-frame-45-64-96-43-87-01` verdicts (feeder targets
   only, no preemptive promotion).
