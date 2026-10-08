# Next-token findings: n-e frames (12/48 followers)

Finder beat: n-e-frames (wave 2). Stream: repaired 1,847-pair parse
(`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`,
parsed like `repair_parse.py`; `canonical.py` never used; R5005 untouched).
All 12 (n=23) and 48 (n=38) occurrences extracted ±3 groups. Windows below use
@pair offsets.

Recovery note: the prior finder worker died at ~2026-10-08 04:26 UTC with no
report; its stale lock `code/crowd17/next-token/locks/n-e-12-48.lock` was
deleted on this restart. This report is a clean restart.

Standing constraints respected: 48="est"/"ne"/"de" are killed as WORD values —
this beat tests the LETTER reading (48="e", 12="n") only, which is distinct.
{48,94} homophone-set kill respected (no homophony claimed). GT banked:
11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que; provisional 59=est, 77="le".

## Correction to the beat brief

The brief claimed 'ne'=12-48 ×7. Measured: **×5** (@169, @709, @809, @1075,
@1736). The crowd16 forks finder independently measured ×5 — the brief's ×7
was wrong. All other brief counts verify: 'me'=82-48 ×4 ✓, 'en'=40-12 @64 ✓
(40 @63, 12 @64), 'ni'=12-34 @1740 ✓ (single).

## P1 (HIGH). 'me' = 82-48 ×4 — verified, one adverse noted

- @125 (a1_03): `98 82 48 11=la 02` — "**me la** 02". The me/la double clitic
  is clean diplomatic French ("il me la …"). Flagship frame.
- @397 (a2_07): `64=qui 79=tout 82 48 06 11=la` — "qui tout **me** 06 la".
- @1228 (a7_01): `64=qui 79=tout 82 48 29=er 47=ce` — "qui tout **me** er ce".
  ("qui tout me" ×2 is one frame type, de-duplicated.)
- @376 (a2_07): `85 82 48 00=pour 11=la` — "**me** pour la". ADVERSE to the
  pronoun parse: clitic "me" cannot precede "pour". The word-final "-me"
  parse fits better here ("même pour la", "…me pour la"). 48="e" still holds;
  the pronoun reading does not hold in all four.

Cipher-testable: @125 predicts 02 is verb-initial ("me la [verb]"); @397
predicts 06 is a verb taking "la" ("tout me [verb] la"); @1228's tail
(29=er 47=ce) is open — "me"+"er" has no clean parse, noted not forced.

## P2 (HIGH). 70-12 "pren" ×3 — GT-anchored both sides, composes with 94

- @348 (a2_05): `06 70=pre 12 94 74` — "06 **pren** 94".
- @1548 (a8_00): `00=pour 46=que 70=pre 12 94 92` — "pour que **pren** 94".
- @1119 (a6_07): `11=la 88 70=pre 12 06` — "la 88 **pren** 06".

"pre"+"n" is GT on both groups. The "pren 94" ×2 cluster (de-duplicated)
composes with the concurrent 94="ne" battery: 70-12-94 = "pre"+"n"+"ne" =
"prenne". But "pour/que prenne" needs a subject that is not visible
(@1548: 92 follows — possible inverted subject, unresolvable here). This is
a joint constraint on the 94="ne" battery, flagged below, not adjudicated.

## P3 (MEDIUM-HIGH). 'ne' = 12-48 ×5 — letter frame holds, 2/5 resist negation parse

- @1075 (a6_05): `98 12 48 77=le? 78 64=qui` — "98 **ne le** 78 qui".
  "**ne le** [verb]" with provisional 77="le" — the strongest negation-shaped
  window. Testable via 78's profile.
- @809 (a5_05): `41 12 48 24` — "41 **ne** 24".
- @1736 (a7_09): `60 12 48 52` — "60 **ne** 52".
- @169 (a1_05): `84=on 53 12 48 21` — "on 53 **ne** 21". ADVERSE-leaning: 53
  sits between "on" and "ne", which is ungrammatical for negation.
- @709 (a5_01): `35 53 12 48 71` — "35 53 **ne** 71". Same "53 ne" prefix
  (frame type de-duplicated with @169).

The "53-12" bond is real (53's top follower is 12, 4/11). Open alternative:
53="donn" + "ne" = "**donne**" ("on donne 21" @169, "35 donne 71" @709 —
both clean French). But 53-12-41 (@58) and 53-12-44 (@1582) break "donne"
("donn"+"n" is impossible), so 53's parse is unresolved and gates the "ne"
reading in 2 of 5 windows. 53-profile battery recommended.

No "ne … pas" closure anywhere: 48's followers are maximally scattered
(19 distinct followers / 38 windows) — consistent with a LETTER, not a word.
(Words have constrained followers; letters do not. This scatter is evidence
for the letter reading, not against it.)

## P4 (MEDIUM). 48-40 "ee" @1398 — double-e junction supports 48="e"

@1398 (a7_07): `76 47=ce 78 48 40=e 67=et/veut` — "ce 78 **ee** 67". Two
consecutive e-letters at a word junction is exactly what letter-"e" predicts;
no word-value of 48 predicts it. Boundary parse open ("ce 78"+"ée" needs a
feminine stem at 78; "78e"+"e 67" alternatives noted). Mild support, not a
proof frame.

## P5 (MEDIUM-LOW). 'en' = 40-12 @63 — single, but the "ière en" junction is elegant

@63 (a1_01): `08 34=i 29=er 40=e 12 94` — "…ière"+"en": GT "i"+"er"+"e"
("…ière" tail: "première/dernière/manière") followed by 40-12="en", with the
"e" shared at the junction (haplology of "…ière en" → "…ieren"). Both groups
GT-anchored. Followed by 94 — see the 94-battery flag below.

## P6 (LOW). 'ni' = 12-34 @1740 — single, null-leaning

@1740 (a8_07): `86 12 34=i 94` — "86 **ni** 94". French "ni" normally pairs
("ni … ni"); no second "ni" exists in the stream (12-34 occurs once total).
Consistent with 12="n" but proves nothing alone.

## P7 (LEAD). 26-12 ×4 and 12-16 ×3 — "26 n 16" ×2 mini-cluster

- @241: `11=la 26 12 16`; @843: `94 26 12 16` — "26 **n** 16" ×2
  (de-duplicated); @1471: "26 n 41"; @1708: "26 n 06".
- Feeds the noun26-frames beat: if 26 is a noun, 12="n" starts the next word
  ("n"+16 = "ne/nos/notre" candidates). @843's "94 26 n 16" needs a parse if
  94="ne" promotes (flagged below).

## Notes for the concurrent 94="ne" battery (flagged, NOT adjudicated)

1. @63 "en 94": if 94="ne", "**en ne**" is ungrammatical French. Either 94≠"ne"
   here or the boundary parse differs.
2. @348/@1548 "pre n 94": composes to "**prenne**" if 94="ne", but "que/pour
   prenne" then needs a subject (92 follows @1548 — possible, unresolvable).
3. @64/@348/@1548 (12→94 ×3): "n"+"ne" adjacency in all three — the 12 and 94
   readings interact and must be co-tested, not tested in isolation.
4. @842 "94 26 n 16": "ne [noun] ne…" needs a parse under 94="ne".

## Ranked battery targets

1. **48="e" letter battery** — 'me' ×4 (@125 flagship "me la"), "ee" @1398,
   "ne" ×5. Bar: 48 reads "e" in all 38 windows; adverses: the @376
   pronoun/word-final split, @1228's "me er" tail, scattered followers
   (expected under letter reading — state as control).
2. **12="n" letter battery** — "pren" ×3 (@348/@1548 flagship), "en" @63,
   "ni" @1740. Bar: 12 reads "n" in all 23 windows; adverses: 53-12 ×4 parse,
   26-12 ×4 (defer to noun26 beat).
3. **53-profile battery** — "53 ne" ×2 vs "donne" ×2 vs 53-12-41/44. Bar:
   single parse covering all 11 of 53's windows. Decides 2/5 "ne" windows.
4. **"prenne" composition test (joint with 94="ne" battery)** — 70-12-94 ×2:
   test "prenne" with subject-search at 92 (@1548) and 74 (@348) before either
   battery promotes.
5. **"ne le" frame test** — @1075 "ne le 78 qui": cross-check 78's verb/noun
   profile; if 78 cannot head a verb phrase here, the frame weakens.

## Honest nulls

- 'ni' @1740: single, unpaired — null-leaning, kept only as a consistency check.
- 12's follower distribution has no dominant frame (48 ×5, 94 ×3, 16 ×3) —
  12="n" rests on GT bigrams, not on follower clustering.
- "on 53 ne" ×2 resists the negation parse; the "donne" alternative is live.
- The "ee" @1398 and "par em 98" @928 ("96=par 48 82=m 98" — "par"+"em…",
  word-initial "em-" candidate) support 48="e" only mildly; both need word-
  boundary work the letter battery should own.

## Addendum (2026-10-07, written after the battery ran concurrently)

- The n-e-12-48 letter battery ran in parallel
  (`code/crowd17/report_inbox/battery-n-e-12-48.md`) and returned **promote**
  (C1/C2/C3 pass; ×7→×5 correction independently confirmed), pending red-team
  ratification. Ranked targets #1 and #2 above are therefore SUPERSEDED as
  new-battery proposals. Live follow-ups remaining: #3 (53-profile), #4
  ("prenne" joint test — the battery flagged the same 12/94 duality for
  red-team adjudication), #5 ("ne le" frame test).
- Missed frame (my gap, volunteered): **29-48 "ere" @541** (a3_01:
  `12 44 29=er 48 42`) — pencil-anchored "er"+"e", supports 48="e". The
  battery caught it; this finder did not. The P2/P4 evidence above stands but
  was incomplete by one frame type.
- Divergences the supervisor/red team should hold: the battery did not
  evaluate the @376 "me pour la" pronoun-vs-word-final adverse (P1) or the
  "53 ne"/"donne" tension at @169/@709 (P3). Open notes on the promoted
  claim, not kill-grade contradictions.

## Method

Repaired 1,847-pair parse; every 12 (23) and 48 (48→38) occurrence ±3 groups;
clustered by follower first (12: 48×5, 94×3, 16×3; 48: no dominant follower —
19 distinct); predictions from 1840s diplomatic French register; identical
repeats de-duplicated before counting ("qui tout me" ×2, "53 ne" ×2,
"pre n 94" ×2, "26 n 16" ×2). Full window inventory below.

## Window inventory (all 61 windows, ±3, glossed)

12-windows (23):
- @58 (a1_01) `58 35 53 [12] 41 08 34=i`
- @64 (a1_01) `34=i 29=er 40=e [12] 94 92 69`
- @169 (a1_05) `82=m 84=on 53 [12] 48 21 60`
- @241 (a2_01) `17=fois 11=la 26 [12] 16 56 43`
- @348 (a2_05) `01 06 70=pre [12] 94 74 67=et/veut`
- @539 (a3_01) `82=m 16 91 [12] 44 29=er 48`
- @701 (a5_01) `28 94 60 [12] 98 20 12`
- @704 (a5_01) `12 98 20 [12] 66 21 35`
- @709 (a5_01) `21 35 53 [12] 48 71 12`
- @712 (a5_01) `12 48 71 [12] 63 00=pour 66`
- @809 (a5_05) `24 24 41 [12] 48 24 65`
- @843 (a5_06) `62 94 26 [12] 16 00=pour 33`
- @1075 (a6_05) `42 98 98 [12] 48 77=le? 78`
- @1119 (a6_07) `11=la 88 70=pre [12] 06 14 06`
- @1430 (a7_08) `63 91 61 [12] 16 76 49`
- @1471 (a7_10) `62 38 26 [12] 41 53 60`
- @1509 (a7_11) `86 56 41 [12] 61 59=est? 39`
- @1548 (a8_00) `00=pour 46=que 70=pre [12] 94 92 45`
- @1582 (a8_02) `98 24 53 [12] 44 00=pour 36`
- @1641 (a8_04) `74 35 56 [12] 33 98 60`
- @1708 (a8_06) `94 88 26 [12] 06 29=er 40=e`
- @1736 (a8_07) `30 06 60 [12] 48 52 86`
- @1740 (a8_07) `48 52 86 [12] 34=i 94 82=m`

48-windows (38):
- @126 (a1_03) `66 98 82=m [48] 11=la 02 26`
- @170 (a1_05) `84=on 53 12 [48] 21 60 09`
- @283 (a2_03) `20 61 42 [48] 52 89 28`
- @361 (a2_06) `11=la 21 62 [48] 76 47=ce 78`
- @365 (a2_06) `76 47=ce 78 [48] 49 61 70=pre`
- @377 (a2_07) `29=er 85 82=m [48] 00=pour 11=la 50`
- @398 (a2_07) `64=qui 79=tout 82=m [48] 06 11=la 45`
- @426 (a2_09) `47=ce 14 62 [48] 76 42 63`
- @450 (a2_09) `61 59=est? 32 [48] 79=tout 17=fois 77=le?`
- @542 (a3_01) `12 44 29=er [48] 42 06 00=pour`
- @641 (a4_01) `67=et/veut 77=le? 89 [48] 20 24 87=ce`
- @710 (a5_01) `35 53 12 [48] 71 12 63`
- @729 (a5_02) `11=la 00=pour 86 [48] 88 11=la 24`
- @810 (a5_05) `24 41 12 [48] 24 65 14`
- @856 (a5_07) `51 64=qui 32 [48] 84=on 02 24`
- @863 (a5_07) `49 74 74 [48] 47=ce 46=que 00=pour`
- @872 (a5_07) `87=ce 77=le? 89 [48] 20 74 49`
- @928 (a5_10) `17=fois 61 96=par [48] 82=m 98 83`
- @972 (a6_01) `76 01 98 [48] 51 45 08`
- @987 (a6_01) `01 24 89 [48] 01 76 49`
- @1076 (a6_05) `98 98 12 [48] 77=le? 78 64=qui`
- @1177 (a6_10) `36 74 32 [48] 59=est? 37 77=le?`
- @1212 (a7_00) `64=qui 59=est? 32 [48] 96=par 45 36`
- @1221 (a7_01) `92 61 24 [48] 30 09 20`
- @1229 (a7_01) `64=qui 79=tout 82=m [48] 29=er 47=ce 33`
- @1276 (a7_03) `76 87=ce 76 [48] 56 85 48`
- @1279 (a7_03) `48 56 85 [48] 53 61 56`
- @1316 (a7_04) `36 74 62 [48] 98 15 24`
- @1350 (a7_05) `73 34=i 62 [48] 77=le? 78 94`
- @1398 (a7_07) `76 47=ce 78 [48] 40=e 67=et/veut 77=le?`
- @1465 (a7_09) `01 21 62 [48] 21 02 62`
- @1525 (a8_00) `24 11=la 11=la [48] 96=par 87=ce 46=que`
- @1570 (a8_01) `24 74 62 [48] 56 32 28`
- @1589 (a8_02) `70=pre 64=qui 65 [48] 29=er 47=ce 08`
- @1614 (a8_03) `55 83 71 [48] 31 76 42`
- @1658 (a8_04) `37 11=la 24 [48] 47=ce 98 98`
- @1737 (a8_07) `06 60 12 [48] 52 86 12`
- @1779 (a8_09) `64=qui 59=est? 19 [48] 74 65 23`
