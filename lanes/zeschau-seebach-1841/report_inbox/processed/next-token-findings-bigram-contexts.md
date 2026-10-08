# Next-token findings: bigram-contexts ("le fait" vs "l'[84]", "ne m'", "n'est")

Finder beat: bigram-contexts (wave 2). Date: 2026-10-08.
Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` +
`data/upstream-ct_R5005.txt`, parsed like `code/side-keyhunt/repair_parse.py`).
`canonical.py` never used. R5005 untouched. No data invented.
All @-offsets are 0-based positions of the TARGET group in the repaired stream.

Standing constraints respected (BATTERY-PROTOCOL.md §7): 84="on" granted (A15,
C1–C3) is used, not re-litigated; 84="fait" kill holds; 94="ne" promoted
(pending red-team) is used as frame input, not verdict here; 77="le"
provisional; {48,94} homophone-set kill holds; 62="on" strong lead vs 62="il"
rival is the collision battery's property (queued as collision-62-84) — this
report supplies frames, not the adjudication.

## Method (beat method, followed exactly)

1. Extracted every 84 (n=25), every 94-82 (n=4), every 94-59 (n=3) ±3 groups.
2. Clustered by follower pattern FIRST, then by predecessor (elision is a
   predecessor phenomenon).
3. De-duplicated byte-identical formula windows before counting productive
   frames (5 repeats found, §3).
4. Predicted plaintext from 1840s French diplomatic register; elision facts
   are about the French word-pair the bigram encodes (obligatory written
   elision: le→l', que→qu', ne→n', me→m' before vowel-initial words).
5. Ranked by confidence × testability. Checked queued targets
   collision-62-84, prenne-70-12-94, ne-le-1075, ent-06, est-59-frames,
   frame-94-82-06-06 — no bar duplicated (scoping notes in §7).

## Window inventory

### 84-windows (all 25, ±3, target cited)

| @ | row | window | pre→suc |
|---|---|---|---|
| 146 | a1_04 | 67 64 77 84 29 87 64 | 77→29 |
| 154 | a1_04 | 47 46 66 84 26 35 58 | 66→26 |
| 167 | a1_05 | 11 24 82 84 53 12 48 | 82→53 |
| 260 | a2_02 | 32 43 77 84 74 45 93 | 77→74 |
| 276 | a2_03 | 33 29 89 84 91 37 61 | 89→91 |
| 310 | a2_04 | 20 17 46 84 24 37 78 | 46→24 |
| 391 | a2_07 | 36 62 91 84 73 34 67 | 91→73 |
| 412 | a2_08 | 01 02 53 84 51 37 78 | 53→51 |
| 473 | a2_10 | 06 67 46 84 24 37 78 | 46→24 |
| 788 | a5_04 | 94 74 65 84 06 77 64 | 65→06 |
| 857 | a5_07 | 64 32 48 84 02 24 49 | 48→02 |
| 1021 | a6_03 | 66 91 53 84 92 64 45 | 53→92 |
| 1058 | a6_04 | 45 23 77 84 09 98 83 | 77→09 |
| 1151 | a6_08 | 67 33 66 84 02 00 92 | 66→02 |
| 1189 | a6_10 | 59 42 06 84 59 46 07 | 06→59 |
| 1290 | a7_03 | 00 11 17 84 59 35 94 | 17→59 |
| 1378 | a7_06 | 86 29 89 84 92 69 13 | 89→92 |
| 1418 | a7_08 | 34 52 32 84 79 15 33 | 32→79 |
| 1447 | a7_09 | 37 64 77 84 59 36 67 | 77→59 |
| 1485 | a7_10 | 62 46 77 84 24 87 08 | 77→24 |
| 1501 | a7_11 | 89 41 74 84 33 42 33 | 74→33 |
| 1620 | a8_03 | 42 44 11 84 78 66 67 | 11→78 |
| 1665 | a8_04 | 80 22 94 84 64 06 91 | 94→64 |
| 1764 | a8_08 | 93 06 77 84 09 24 87 | 77→09 |
| 1803 | a8_10 | 87 64 77 84 59 35 94 | 77→59 |

Predecessor distribution: 77 ×7, 66 ×2, 89 ×2, 46 ×2, 53 ×2,
82/91/65/48/06/17/32/74/11/94 ×1.
Follower distribution: 59 ×4, 24 ×3, 02 ×2, 92 ×2, 09 ×2,
29/26/53/74/91/73/51/06/79/33/78/64 ×1.

### 94-82 "ne m'" windows (all 4)

- @578 (a3_02): 13 55 61 94 82 06 06 — "61 ne m' 06 06" (formula)
- @1182 (a6_10): 37 77 78 94 82 06 06 — "le 78 ne m' 06 06"
- @1353 (a7_05): 48 77 78 94 82 06 52 — "le 78 ne m' 06 52"
- @1742 (a8_07): 86 12 34 94 82 46 56 — "86 [12] i ne me que"

### 94-59 "n'est" windows (all 3) + indirect

- @558 (a3_02): 34 17 86 94 59 30 67 — "86 n'est 30"
- @762 (a5_03): 40 20 62 94 59 39 88 — "62 n'est 39"
- @1795 (a8_09): 86 56 42 94 59 37 91 — "42 n'est 37"
- @101 (a1_02): 08 21 62 94 93 59 45 — indirect "62 ne 93 est" (no elision at 94)

### Analytic "ne" (12-48) control: zero

- 12-48-82: 0. 12-48-59: 0. 12-48-84: 0.
- The letter-spelled "ne" NEVER takes "me"/"est"/"on" followers. The
  syllable-spelled "ne" (94) takes 82 ×4, 59 ×3. The two spellings are in
  complementary distribution on exactly the elision-frame followers. This
  distributional split supports the analytic/syllabic duality (not a new
  value claim).

### Byte-identical repeats de-duplicated before counting

- "46 84 24 37 78" @309–313 and @472–476 → "qu'on en" = 1 frame-type.
- "77 78 94 82 06" @1180–1184 and @1351–1355 → "le 78 ne m' 06" = 1 frame-type.
- "84 59 35 94 52 80 04" @1290–1296 and @1803–1809 → "on est 35 ne pas [inf]"
  formula = 1 frame-type (an "on est" leg, not a new "n'est").
- "45 13 55 61 94" @574–578 and @1165–1169 → formula prefix; continuations
  differ (82-06-06 vs 87-83). The "61 94" cluster is formulaic.
- "62 94 79 14 60" @1362–1366 and @1686–1690 → 1 frame-type (F9, ne-frames).

## Elision-frame clusters

### E1. "l'[84]" = "l'on" ×7 — the elision cluster (A15-C1 legs, re-derived)

All seven 77-84 windows. Followers: 29, 74, 09, 59, 24, 09, 59.

- E1a @1447 "37 64 77 84 59 36 67" = "qui l'on est [36]" — CLEAN.
- E1b @1803 "87 64 77 84 59 35 94" = "qui l'on est 35 ne [pas]" — CLEAN
  ("l'on est" ×2, one frame-type).
- E1c @1485 "62 46 77 84 24 87 08" = "[62] que l'on en ce [08]" — CLEAN
  ("qu'on"/"l'on" unify; "en ce" = prepositional).
- E1d @260 "32 43 77 84 74 45 93" = "l'on 74 ce" — 74 verb-LEANING
  (74→46="que" ×3, 74→62 ×3 support verb; 74→45="ce" ×3 needs a parse;
  74-74 ×6 self-loops are formula-shaped, de-duplicated). Open, not clean.
- E1e @1058 "45 23 77 84 09 98 83" = "l'on 09 [98]" and E1f @1764
  "93 06 77 84 09 24 87" = "l'on 09 en ce" — "l'on 09" ×2, one frame-type.
  09 verb-LEANING (09→00="pour" ×2, 09→24="en"; n=12, thin). Open.
- E1g @146 "67 64 77 84 29 87 64" = "qui l'on 29 ce qui" — WEAKEST LEG.
  29="er" is heavily syllabic (29→40="e" ×9, the "premiere" tail; 29→87
  only ×3 stream-wide). "l'on" + syllabic "er" resists the verb parse:
  rival parses are "l'on erre"-shaped (grammatical but odd) vs within-word
  "onner" (77 not elided, 84-29 = "on"+"er" syllables). Unresolved —
  proposed as battery target T2. ("qui l'on" ×3: @144/@1445/@1801 share the
  "64 77 84" prefix; frame-qui-77-84 is PROMOTED — this target is a residual
  on it, not a re-litigation.)

Score: 3 clean, 2 leaning (×2 frame-types), 1 weak, 1 open sub-type.
The "l'on" frame-type stands; E1g is its honesty tax.

### E1x. 77-elision exclusivity — new supporting leg for 77="le" (C1)

77's followers over all 44 windows: 78 ×7, 84 ×7, 86 ×5, 81 ×4, 76 ×3,
44 ×2, 89 ×2, 82 ×2, 66/60/62/80 ×1.
Among KNOWN vowel-initial cells (59="est", 94="ne", 46="que", 40="e",
34="i", 47="ce", 17="fois"-consonant): 77→{59,94,46,40,34,47,17} = **0**.
84 is the ONLY known vowel-initial cell 77 ever precedes — 7/7.
The l'-elision of the article fires exclusively at 77-84. Under 77="le"
(provisional), this proves 84 is vowel-initial by an independent mechanism
from the corpus-frequency legs, and it is exactly the C1 inheritance made
testable: if 77 falls, these 7 legs fall with it — but while 77 stands,
no other vowel-initial cell competes for the elision. Caveat: 77's unknown
followers (86/81/76/44/89) could in principle be vowel-initial — stated as
the open condition in target T3.

### E2. "qu'[84]" = "qu'on en" ×2 → 1 frame-type

@310 "20 17 46 84 24 37 78" and @473 "06 67 46 84 24 37 78", byte-identical
"46 84 24 37 78" = "qu'on en [37-verb] [78]". Elision qu' before "on".
Discriminates vs "en" ("qu'en en" ungrammatical) and vs noun; does NOT
discriminate vs "il" ("qu'il en" is grammatical) — the "l'on" ×7 does that
work instead ("l'il" impossible, per red-team A15).

### E3. "[82]-[84]" = "mon" ×1

@167 "11 24 82 84 53 12 48" = "la en mon 53 ne" — possessive, no elision
involved; 82="m" GT-anchored. Single leg, kept.

### E4. "ne m'" = 94-82 — split by elision

- E4a @1742 "86 12 34 94 82 46 56" = "[86] [12] i ne me que" — the clean
  UNELIDED frame: "me" before consonant-initial "que" needs no elision.
  34="i" and 46="que" both GT. This is the flagship "ne m'" bigram.
  ADVERSE (fenced, not resolved): 12@1740 + 34@1741 = the SAME "12-34"
  the n-e-frames finder read as 'ni' (P6, @1740, null-leaning single).
  "ni ne me que" is ungrammatical; "n i ne me que" dissolves P6's 'ni'.
  The two readings share 34 and cannot both hold — this is the 12/94
  analytic/syllabic duality at one window. Flagged for the duality
  adjudication (prenne-70-12-94 owns the duality; T4 below is scoped to
  this window only, no bar overlap).
- E4b "ne m' 06" ×3 → 2 frame-types after de-dup: "61 ne m' 06 06" @578
  (formula) and "le 78 ne m' 06" @1182/@1353. The m'→elision holds IFF 06
  is vowel-initial. 06's profile (n=44): pre {42 ×5, 82 ×4, 30 ×4},
  suc {77 ×6, 00 ×4, 11 ×4, 29 ×4} — verb-shaped ("06 le/la", "06 pour").
  06-77 ×6 = "06 le" kills the "06=en" rival ("en le" bad), so the F10
  "en"-islet reading does not extend here. Elision consequence for the
  QUEUED targets ent-06 (06="ent/ment" — "ent" IS vowel-initial, elision
  holds) and frame-94-82-06-06: if 06 is consonant-initial, E4b reads
  "ne me 06" unelided — the frame survives either way; only the apostrophe
  is conditional. No new 06 target proposed (would duplicate).
- 82's clitic/word-final duality (n-e-frames @376 "me pour la" adverse):
  in E4 the clitic parse is forced by 94="ne" + verb-shaped 06 / "que" —
  no E4 window admits the word-final-"m" rival cleanly. Fenced, noted.

### E5. "n'[94]" = "n'est" ×3 — elision REQUIRED in all three, holds in all three

- @558 "34 17 86 94 59 30 67" = "i fois 86 n'est 30 [67]"
- @762 "40 20 62 94 59 39 88" = "e [20] 62 n'est 39 [88]"
- @1795 "86 56 42 94 59 37 91" = "86 56 42 n'est 37 [91]"
Three independent predecessors (86, 62, 42); 59="est" provisional and
vowel-initial, so "ne"→"n'" elision is obligatory — and all three read
cleanly. The indirect @101 "62 94 93 59" ("on ne 93 est") needs no elision
at 94 (93 consonant-initial) — consistent, bonus frame.
Subject slot (86/62/42) is UNEXPLORED: 86 is "pour"-governed ×12
("pour 86" — infinitive/noun pull) yet sits in subject position here;
62 is the collision cell ("il"/"on"); 42 is A1-predicative. Proposed as
battery target T1. (Queued est-59-frames covers the FOLLOWERS 30/39/37 —
no overlap.)

### E6. "ne pas" = 94-52 ×3 — elision n/a

@570, @1293, @1806 ("35-94-52-80-04" byte-identical @1292/@1805,
"ne pas [inf]"). "pas" consonant-initial; no elision question. Completeness
only.

### E7. "ne [84]" = "ne on" — the elision that must NOT happen, doesn't

@1665 "80 22 94 84 64 06 91" = "22 ne on qui" (A15-C3 R2, fenced).
"ne"+"on" cannot elide ("n'on" is not French) — and indeed no elision is
available; the window stays fenced as a 1/25 residual. Consistent with the
fence, not a contradiction. 12-48-84 = 0 (analytic "ne" also never
precedes "on").

## "le fait" vs "l'[84]" — verdict-frame

"le fait"-shaped (77/11 + 84-as-noun) productive frames: **zero**.
- 77-84 ×7: all seven read "l'on" (3 clean, rest leaning/weak — none
  "le"-noun-shaped).
- 11-84 ×1 (@1620 "42 44 11 84 78 66 67" = "44 la [84] 78"): fenced R1,
  "la on" ungrammatical — the sole "la [84]" window, and it does NOT read
  "le fait"-shaped either.
- No other article-like predecessor of 84 exists.
"l'[84]" wins 7–0 among article contexts. The killed 84="fait" value has
no surviving elision-frame refuge. (Null result, reported as such.)

## 62/84 complementarity (frame input to queued collision-62-84 — no bar overlap)

- 62→94 ×9 (@100, @508, @761, @840, @1329, @1362, @1686, @1704, @1772);
  62→59 = 0. 84→59 ×4 (@1189, @1290, @1447, @1803); 84→94 = 0.
- 62→84 = 0; 84→62 = 0. The two "on" candidates never appear in each
  other's signature slot in EITHER direction. Clean distributional
  complementarity, re-derived from the stream. The adjudication itself
  belongs to collision-62-84 (queued, p1); this report only banks the
  zero-crossover counts.

## Ranked frames (confidence × testability)

1. "n'est" ×3 (E5) — three independent subjects, obligatory elision holds
   in all three. HIGH.
2. "l'on" ×7 (E1) — 3 clean legs, elision-exclusivity (E1x) as independent
   mechanism; E1g the honest weak leg. HIGH (frame-type), MEDIUM per-leg
   for E1d–E1g.
3. "ne me que" @1742 (E4a) — GT both sides, no elision needed. HIGH,
   with the @1740 'ni' adverse fenced.
4. "qu'on en" ×2→1 frame-type (E2) — byte-identical, rare frame. HIGH.
5. "ne m' 06" ×3→2 frame-types (E4b) — elision conditional on 06's
   initial; feeds queued ent-06 / frame-94-82-06-06. MEDIUM-HIGH.
6. "l'on 09" ×2 (E1e/f), "l'on 74" (E1d) — verb-leaning followers, thin
   profiles. MEDIUM-LOW.
7. "mon" @167 (E3) — single, GT-anchored. MEDIUM-LOW.

## Ranked battery targets for the supervisor

### T1. "n'est" subject-slot battery (86/62/42) — priority 1
- claim: 86, 62, 42 are subject-shaped before "n'est" at @558/@762/@1795.
- bars: resolve iff each of {86, 62, 42} takes a subject parse consistent
  with its contact profile with zero forced contradiction; else fence the
  failing slot.
- evidence: three independent predecessors; "86 n'est 30", "62 n'est 39",
  "42 n'est 37" all parse; 42 A1-predicative, 62 the collision cell.
- adverses: 86 is "pour"-governed ×12 ("pour 86") — infinitive/noun pull
  vs subject position here; 59="est" provisional (inherited).
- note: queued est-59-frames covers the FOLLOWERS (30/39/37) — no overlap.

### T2. "l'on 29" @146 disambiguation — priority 2
- claim: @146 "64 77 84 29 87 64" resolves to exactly one of {"l'on erre"-
  shaped (l'on + er-verb), within-word "onner" (77="le" unelided, 84-29 =
  "on"+"er" syllables)}.
- bars: resolve iff one parse covers 77-84-29-87 with 29's syllabic
  profile (29→40="e" ×9 vs 29→87 ×3) and zero contradiction; else fence.
- evidence: weakest of the 7 "l'on" legs; "84 29" unique stream-wide;
  "64 77 84" ×3 (@144, @1445, @1801).
- adverses: 29 rarely word-initial (pre {33 ×5, 86 ×4, 06 ×4, 34 ×3});
  frame-qui-77-84 is PROMOTED — this is a residual on it, not re-litigation.

### T3. 77 elision-exclusivity leg (A15-C1 support) — priority 2
- claim: 77="le" elides to l' exclusively before vowel-initial 84:
  77→{59,94,46,40,34,47,17} = 0 vs 77→84 = 7.
- bars: promote-LEG iff the zero-counts re-derive on the repaired stream
  AND no other 77 follower is shown vowel-initial; else record as
  provisional-only.
- evidence: full 44-window 77-follower scan; 84 the sole known
  vowel-initial follower (7/7).
- adverses: 77's unknown followers (86/81/76/44/89) could be vowel-initial
  (open condition); 77="le" itself provisional (le-77 null) — this target
  is a SUPPORTING leg, not a 77 promotion; does not duplicate le-77's
  FU1–FU3 bars (@1033/@611/@1216).

### T4. "ni" @1740 vs "i ne me" @1742 boundary test — priority 2
- claim: exactly one boundary parse covers "86 12 34 94 82 46"
  (@1739–1744): {"ni"+"ne me" (12-34="ni"), "n"+"i ne me" (34="i" GT)}.
- bars: resolve iff one parse holds with banked values and zero
  contradiction; else fence BOTH readings for the 12/94 duality
  adjudication (red team).
- evidence: the two readings share 34="i"; "ni ne me que" ungrammatical;
  n-e-frames P6 'ni' is a null-leaning single.
- adverses: prenne-70-12-94 owns the 12/94 duality — this target is
  frame-scoped to @1739–1744 only, no bar overlap.

### T5. "l'on 09" verb-shape battery — priority 3
- claim: 09 is verb-shaped in "l'on 09" ×2 (@1058, @1764).
- bars: resolve iff 09's 12-window profile supports verb
  (09→00="pour" ×2, 09→24="en", 09→87/64/70) with zero noun-forcing
  window; else fence.
- evidence: "l'on 09" one frame-type ×2; 09's top predecessor is 84 (2/12).
- adverses: n=12 thin; 09's killed "-ère" value is NOT re-litigated
  (verb-shape is a distinct claim).

## Elision consequences for already-queued targets (inputs, not new targets)

- ent-06 (queued, p2) and frame-94-82-06-06 (queued, p4): if 06="ent/ment"
  (vowel-initial "ent"), the m'-elision in E4b "ne m' 06" HOLDS and the
  frame reads "ne m'ent…". If 06 is consonant-initial, E4b reads unelided
  "ne me 06" — frame survives either way. 06-77 ×6 ("06 le") kills the
  "06=en" rival independently of those batteries.
- collision-62-84 (queued, p1): zero-crossover counts banked above
  (62→59=0, 84→94=0, 62→84=0, 84→62=0).
- ne-le-1075 (queued, p2): E4b's "77 78 94 82" ("le 78 ne m'") windows
  @1182/@1353 share the "77 78" cluster with @1075's neighborhood —
  noted as shared context, not adjudicated here.

## Nulls and anomalies (results, not gaps)

- N1 "le fait"-shaped frames: ZERO productive. The killed 84="fait" has
  no elision-frame refuge; "l'[84]" wins 7–0.
- N2 Analytic "ne" (12-48) never takes "me"/"est"/"on" followers (0/0/0)
  while syllabic "ne" (94) takes 82 ×4, 59 ×3 — complementary
  distribution on the elision followers. Distributional null for any
  "12-48 = 94" interchangeability on these frames.
- N3 @146 (E1g): weakest "l'on" leg — follower 29 resists the verb parse
  (T2).
- N4 Unclassified 84-windows (R4-type, consistent with "on"-syllable in
  other words, not contradictions): 66-84 ×2 (@154, @1151), 89-84 ×2
  (@276, @1378), 53-84 ×2 (@412, @1021), 91-84 @391, 65-84 @788,
  48-84 @857, 06-84 @1189, 32-84 @1418, 74-84 @1501. None article-shaped;
  none elision-relevant. Count check: 10 frame-leg windows + R1/R2 + 12
  unclassified + @1290 (formula-dupe of @1803, counted once) = 25.
- N5 @1742's 12-adjacency (E4a adverse): the 'ni'/"n"+"i" tension — fenced
  for duality adjudication (T4).
- N6 @1288 "00 11 17 84 59" = "pour la fois on est": the "84 59 35 94 52
  80 04" formula's second instance has 17="fois" where @1803 has 77="l'on"
  — "pour la fois, on est [35] à ne pas [inf]"-shaped; 35's value decides.
  Formula finder's property; de-duplicated here.

## Cipher-testable consequences

1. E1x predicts: if 77="le" promotes, its l'-elision must occur ONLY
   before vowel-initial cells — any future vowel-initial value assigned
   to 86/81/76/44/89 must then show 77→X elision frames or explain their
   absence (T3's open condition).
2. E4b predicts 06 vowel-initial IFF the m'-elision is real — testable via
   ent-06's outcome (queued).
3. E5 predicts the "n'est" subject slot is a subject position: 86 must
   resolve its "pour 86" ×12 pull vs subject use (T1).
4. E2+E1 predict 84's elision hosts are exactly {77, 46} (l', qu') — any
   new "84=on" window with a non-eliding host before vowel-initial 84
   would be an anomaly; none found in 25 windows.

## Bottom line

Elision behavior CONFIRMS the standing grants and sharpens them: "l'[84]"
beats "le fait" 7–0 with a new exclusivity mechanism (77 elides only
before 84 among known vowel-initial cells); "n'est" ×3 all REQUIRE the
n'-elision and all three hold with independent subjects (subject slot
unexplored → T1); "ne m'" splits into clean unelided @1742 (with a fenced
'ni' adverse → T4) and elision-conditional "ne m' 06" ×3 (→ queued
ent-06). Five battery targets proposed (T1 p1; T2–T4 p2; T5 p3), zero bars
duplicated with queued targets. Three honest weak/open points: @146
(E1g), @260's 74-tail, @1058/@1764's 09. No settled kills re-litigated.
R5005, sealed gates, red-team queue untouched. No locks written, no queue
edits.
