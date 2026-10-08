# Finder report: noun26-frames (26 noun-vs-verb war)

Date: 2026-10-08. Beat: wave-2 `noun26-frames`.
Stream: repaired 1,847-pair parse (`data/upstream-ct_R5005.txt` +
`code/side-keyhunt/repaired_offsets.json`, parsed like
`code/side-keyhunt/repair_parse.py`). Never canonical.py. Never R5005.

Purpose: INPUT beat for the queued `noun-26` battery (priority 2). This
report extracts every 26 window, clusters by follower FIRST, and ranks
frames by confidence x testability. It does NOT decide the war. It feeds
the battery narrower, pre-registered frame batteries.

Offsets: lane @-convention (report @ = 0-based stream index - 1; calibrated
against the 84-adjudication report's 20-62-94 trigram @759/@838/@1702).

Standing inputs respected: 11="la", 17="fois", 94="ne" (promoted), 30="pas"
(promoted), 12="n"/48="e" (promoted letters), 00="pour", 84="on" (A15),
87="ce", 64="qui", 46="que", 59="est" (provisional), 39="a/a" (allophone
tier). Kills hold: 20="fois", 48="est"/"ne"/"de". Splits hold: 23~26 (A2),
20~17. 67 is the sole true polyvalence. 37/32/42 predicative (A1) with
frame-37-reexam queued (37's value open, not decided here). 62="on"
unconditioned KILLED (collision-62-84); 62="il" is the demonstrated rival.

## Headline findings

1. **The war is real and countable: 17 windows of 26, split 8 verb / 3 noun /
   1 paradox / 5 ambiguous (after formula de-dup: 14 productive frame-types).**
   Follower census: 12 x4 | 30 x4 | 00 x3 | 32 x2 | 35, 96, 24, 37 x1.
   Predecessors: 69 x3 | 11 x2 | 64 x2 | 24 x2 | 02, 84, 39, 94, 46, 38, 88,
   89 x1.
2. **"26 pas" x4 (@654, @991, @1249, @1559) is the strongest verb frame.**
   A noun followed by "pas" is ungrammatical; a finite verb followed by
   "pas" is the standard negation frame. Correction to the queue: the
   queued `homophone-12-30` target says "26 30 x3" -- the repaired stream
   has x4 (positions above). The @654/@991 pair is one byte-identical
   6-gram ("76 49 24 26 30 03" x2, rows a4_02/a6_01), counted once.
3. **The "en ce qui" triple is real and decides @1768 by frame-type
   uniformity.** "24 87 64" occurs exactly 3x stream-wide; the slot after
   "qui" holds {23 @181, 26 @1768, 59="est" @1776}. 59="est" is verbal in
   the identical slot ("en ce qui est [19]"). 23~26 SPLIT is granted, so 23
   and 26 are two DIFFERENT verbs in the same formula slot -- the
   "concerne"/"regarde" family ("en ce qui concerne/regarde"). 26 = verb
   at @1768 follows from the triple, not from the single window.
4. **Three independent governors force verb-form, one window each:**
   @154 "66 84 [26]" = "[66] on [26]" (subject pronoun + finite verb);
   @600 "03 39 [26] 96" = "[03] a/à [26] par" (aux + past participle, or
   "à" + infinitive -- verb-form either way); @841 "62 94 [26]" =
   "[62] ne [26]" ("ne" + verb). Any ONE of these kills noun-26
   unconditioned; together they are the battery's hardest legs.
5. **The noun theory rests on exactly two "la 26" windows, and one of them
   is internally paradoxical.** "11 26" occurs exactly 2x: @239
   ("41 17 11 [26] 12 16") and @1559 ("40 17 11 [26] 30 06"). Both read
   "...fois, la [26]" (absolute "une fois la [N]"). But @1559 continues
   "[26] pas [06]" -- "la" forces the noun, "pas" forces the verb. @1559
   is the single crux window of the whole war. A third noun leg exists at
   @128 ("48 11 02 [26] 32 96"): "la [02] [26] [32]" = det-(adj)-noun-adj,
   ungrammatical under 26=verb -- with the "02-26" one-word composition as
   the live rival ("02 26" occurs exactly 1x stream-wide).
6. **"26 12" x4 has a live third reading: "26n" as one word.** 12="n" is a
   PROMOTED LETTER. "26 12" (@239, @841, @1469, @1706; next words 16, 16,
   41, 06) parses as (i) 26-word + "n"-initial word, (ii) "26n" one word
   (12 = final "n"), or (iii) "n'" elision. Reading (ii) is testable by
   contact and must appear in every 26 battery bar as the stated
   alternative. At @239 it would make "la [26n]" a feminine noun ending
   in -n.
7. **@1706 ("62 94 88 [26] 12 06") is a verb-chain leg, not a noun leg.**
   88's profile is verb-form ("a [88]" x2 @-anchored in census; "[88] le"
   x3 = 88-77). "ne [88-modal] [26-inf]" fits the 1840s bare-"ne" license
   for modals (cf. queued `ne-alone-02-74`): "ne peut [26-inf]". 88's value
   is open; the battery profiles it.
8. **@1559's "ne" belongs to "prenne", not to "26 pas".** Wide context:
   @1544-1548 = "00 46 70 12 94" = "pour que [70-12-94]". The 70-12-94
   trigram is the queued `prenne-70-12-94` composition. So @1559's
   "[26] pas" is BARE -- no "ne" in its clause. Bare "pas" is anomalous
   under the verb reading in 1840s French (flag for `ne-alone-02-74`);
   under the noun reading the anomaly is word order instead.
9. **"69 26 00 33" x3 is one frame-type; @933/@1627 extend to a
   byte-identical 8-gram** ("69 26 00 33 21 64 37 01" x2, rows a5_10/a8_03).
   Formula-bound: de-duplicate before counting. "[69] [26] pour dire" is
   genuinely ambiguous -- "[verb] pour dire" and "[noun] pour dire" are
   both strained. 69's class (n=12; followers 26 x3, 13 x2, 88 x2, 14, 24,
   11, 74, 64) is the discriminator. Null-acceptable frame.
10. **37's class is load-bearing for @1768 but NOT decided here.**
    "26 37 78" @1768-1770 vs "23 37 06" @181-183: the 37-followers diverge
    (78 vs 06). 37 = noun reads clean in both slots ("est [37-nominal]"
    per A1; "concerne [37-objet]"); 37 = verb breaks "est 37". Target 2
    names 37's slot and defers to queued `frame-37-reexam`.

## Census: 26 (17 occurrences)

| @ | window (-3/+3) | follower cluster |
|---|---|---|
| 128 | 48 11 02 [26] 32 96 56 | 32 (noun leg) |
| 154 | 46 66 84 [26] 35 58 35 | 35 ("on [26]") |
| 239 | 41 17 11 [26] 12 16 56 | 12 (noun leg, fois-la) |
| 405 | 53 34 69 [26] 00 33 01 | 00 ("[69] 26 pour dire") |
| 530 | 59 37 64 [26] 32 16 08 | 32 ("qui [26] [32]" crux) |
| 600 | 40 03 39 [26] 96 45 93 | 96 ("a/à [26] par") |
| 654 | 76 49 24 [26] 30 03 62 | 30 ("26 pas", formula x2) |
| 841 | 20 62 94 [26] 12 16 00 | 12 ("ne [26] n…") |
| 933 | 83 56 69 [26] 00 33 21 | 00 ("[69] 26 pour dire") |
| 991 | 76 49 24 [26] 30 03 60 | 30 ("26 pas", formula x2) |
| 1249 | 00 67 46 [26] 30 06 65 | 30 ("que [26] pas") |
| 1469 | 02 62 38 [26] 12 41 53 | 12 (ambiguous) |
| 1559 | 40 17 11 [26] 30 06 60 | 30 (noun+pas PARADOX) |
| 1627 | 46 56 69 [26] 00 33 21 | 00 ("[69] 26 pour dire") |
| 1706 | 62 94 88 [26] 12 06 29 | 12 (verb-chain) |
| 1752 | 07 28 89 [26] 24 85 58 | 24 (ambiguous) |
| 1768 | 24 87 64 [26] 37 78 62 | 37 ("en ce qui [26]") |

Followers: 12 x4 | 30 x4 | 00 x3 | 32 x2 | 35, 96, 24, 37 x1.
Follower+1: 16 x3 | 33 x3 | 06 x3 | 03 x2 | 96, 58, 45, 41, 85, 78 x1.
Predecessors: 69 x3 | 11 x2 | 64 x2 | 24 x2 | 02, 84, 39, 94, 46, 38, 88,
89 x1.

## Formula de-dup (applied before counting productive frames)

- "76 49 24 26 30 03" x2 (@654, @991; rows a4_02, a6_01): byte-identical
  6-gram. ONE productive frame-type, two instances. Left/right contexts
  differ ("...82 94" vs "...48 01"; "62 16..." vs "60 67...").
- "69 26 00 33" x3 (@405, @933, @1627); @933/@1627 extend to byte-identical
  8-gram "69 26 00 33 21 64 37 01" (rows a5_10, a8_03). ONE productive
  frame-type, three instances.
- "26 12 16" x2 (@239, @841): same trigram, different surrounds (fois-la
  vs 20-62-94). ONE frame-type, two instances -- not byte-formula.
- "26 30 03" x2 = the @654/@991 formula pair (same as first bullet).
  "26 30 06" x2 (@1249, @1559): one frame-type, two instances.

Productive frame-types: 14. Verb 7 (@154, @600, @654-type, @841, @1249,
@1706, @1768). Noun 2 (@239, @128). Paradox 1 (@1559). Ambiguous 4 (@405-type,
@530, @1469, @1752).

## Ranked frames (confidence x testability)

- **F1 "26 pas" x4 -- verb. Confidence HIGH, testability HIGH.** Four
  windows, one frame-type pair de-duplicated. "Ne"-audit: @654 has 94 four
  groups left ("82 94 76 49 24 26 30" = "ne [76] [49] [24] [26] pas" --
  clitic-chain-compatible); @991/@1249/@1559 have no 94 within +/-15
  (@1559's 94 belongs to "70-12-94" = "prenne"). Bare "pas" is the stated
  1840s tension. Noun-parse excluded per window or fenced with cause.
- **F2 "en ce qui [23/26/59]" triple -- verb. Confidence HIGH, testability
  HIGH.** "24 87 64" exactly 3x; X = 23 @181 / 26 @1768 / 59 @1776;
  fol2 = 37 x2, 19 x1. 59="est" verbal in the identical slot; 23~26 split
  granted. Value lead (not claim): "concerne"/"regarde" family. 37's slot
  named, value deferred to `frame-37-reexam`.
- **F3 governor frames -- verb-form. Confidence HIGH, testability MEDIUM.**
  Three independent governors, one window each: "on [26]" @154 (boundary
  after 66: "...que [66]. On [26] [35]"); "a/à [26] par" @600 (participle
  or infinitive -- verb-form either way; 03 named or fenced); "ne [26]"
  @841 ("[62] ne [26]"; 62's class cited from 84-adjudication, not
  re-derived). Plus the verb-chain "ne [88] [26]" @1706 (88 verb-form
  profiled in-bar).
- **F4 "la [26]" frames -- noun. Confidence HIGH (article forces noun),
  testability MEDIUM.** @239 "...fois, la [26] 12 16" (absolute "une fois
  la [N]"; tail "n[16]" named or fenced; "26n" reading tested). @128 "la
  [02] [26] [32]" (det-(adj)-noun-adj; "02-26" one-word rival tested --
  "02 26" is 1x stream-wide). @530 "qui [26] [32]" is the copula-shaped
  crux: "qui est 32" x2 (@316/@1210 per adj-32) is the control; 26="est"
  killed globally by @239 ("la est" ungrammatical) -- state it.
- **F5 "[69] 26 pour dire" x3 -- ambiguous. Confidence LOW either way,
  testability MEDIUM.** 69's 12-window profile is the discriminator.
  Null-acceptable: if neither class parses, record the selection puzzle
  ("pour dire" resists both verb and noun governors) with follow-ups.
- **F6 "26 12" x4 -- three readings.** (i) word + "n"-initial word; (ii)
  "26n" one word (12="n" final letter -- LIVE); (iii) "n'" elision.
  Cross-cutting alternative for every 26 battery; not its own target
  (no bar overlap with queued `homophone-12-30`, which asks about 12~30
  merge, not 26's class).

## Ranked battery targets for the supervisor

### T1. noun26-pas-frames (priority 1)
- **id:** noun26-pas-frames
- **claim:** 26 is verb-class: "26 30" x4 = "[verb] pas" kills noun-26
  unconditioned.
- **bars:** (a) all four "26 30" windows re-derived on the repaired stream
  (@654, @991, @1249, @1559; @654/@991 = one byte-identical 6-gram,
  counted once); (b) 30 = "pas"-negation in each (no rival parse);
  (c) noun-parse of "26 30" shown ungrammatical per window, or a clause
  boundary fenced with stated cause; (d) "ne"-audit: 94/12 positions
  within +/-15 recorded per window (present @654 only; @1559's 94 belongs
  to "70-12-94"); absent "ne" does NOT fail the bar but the bare-"pas"
  tension is stated and flagged to `ne-alone-02-74`; (e) @1559's "la [26]"
  parsed -- the crux: state exactly how "la [26] pas" reads under the
  winning class, or record @1559 as the residual that forces the
  positional rule.
- **evidence:** F1. "26 30" x4 (queue's "x3" corrected); "pas"-after-noun
  ungrammatical; "ne [76] [49] [24] [26] pas" clitic-chain-compatible
  @654.
- **adverses:** @1559's "la" (banked article) forces noun in the same
  window -- one reading must give, or a positional rule is stated;
  23~26 split granted (no homophone rescue via 23); "26n" one-word rival
  (12 = final "n") tested and excluded or fenced.
- **priority:** 1

### T2. noun26-encequi-triple (priority 1)
- **id:** noun26-encequi-triple
- **claim:** 26 = verb in the "en ce qui [verb]" formula slot, by
  frame-type uniformity across the "24 87 64" triple (X = 23 / 26 /
  59="est").
- **bars:** (a) triple re-derived: "24 87 64" exactly 3x (@178, @1765,
  @1773), followers 23/26/59, fol2 37 x2 / 19 x1; (b) @1768 "en ce qui
  [26] [37]" parses with 26 as verb; (c) 37's slot named (object nominal
  vs clause boundary -- coordinate with queued `frame-37-reexam`, do NOT
  decide 37's value); (d) 23~26 split respected: 23 = the other verb
  (value open); "concerne"/"regarde" family recorded as value LEAD, not
  claim; (e) the subject-reading rival ("qui [26-subject] [37-verb]")
  excluded via 59="est" in the identical slot.
- **evidence:** F2. @1776 "en ce qui est [19]" anchors the slot as verbal;
  @181 "en ce qui 23 37 06" parallels @1768 "en ce qui 26 37 78".
- **adverses:** 37's predicative grant (A1) vs object slot -- deferred to
  `frame-37-reexam`, not re-litigated; 37-follower divergence (06 vs 78)
  stated; single 26 window in the triple.
- **priority:** 1

### T3. noun26-gov-frames (priority 2)
- **id:** noun26-gov-frames
- **claim:** three independent governors force verb-form at @154
  ("on [26]"), @600 ("a/à [26]"), @841 ("ne [26]"), plus the verb-chain
  "ne [88] [26]" @1706.
- **bars:** (a) @154: "66 84 26" parses ONLY as clause boundary + "On
  [26-verb] [35]" (66 fenced or named; "on"+noun excluded); (b) @600:
  "03 39 26 96" parses as aux+participle ("a [26-part] par [45]") or
  "à"+infinitive (03 named or fenced; 39's "a/à" allophone tier stated);
  (c) @841: "62 94 26" parses as "[62] ne [26-verb]" (62's class cited
  from the 84-adjudication report, not re-derived); (d) @1706:
  "62 94 88 26" parses with 88's verb-form profile ("a [88]" x2, "[88]
  77='le'" x3) fixing 88 as modal/participle and 26 as infinitive or
  complement-verb ("ne peut [26]"-shaped; bare-"ne" license cited, not
  re-proved); (e) "26n" one-word rival excluded per window or fenced.
- **evidence:** F3. Three governors from three independent paradigms
  (subject pronoun, aux/prep, negation particle) converge on verb-form.
- **adverses:** one window per governor; 39's allophone tier; 62 = "il"
  rival (cited, not re-litigated); 88's value open (profiled, not named).
- **priority:** 2

### T4. noun26-la-frames (priority 2)
- **id:** noun26-la-frames
- **claim:** the noun legs survive: "...fois, la [26]" x2 + "la [02] [26]
  [32]" @128; 26 = feminine noun where "la" (banked) is the article.
- **bars:** (a) @239 "41 17 11 26 12 16" = absolute "une fois la [N]" with
  the "n[16]" tail named or fenced ("nommée"/"notée"-shaped or boundary);
  (b) @1559 "40 17 11 26 30 06": the "pas" resolved -- boundary, re-parse,
  or the noun claim FAILS at this window (stated, not smoothed);
  (c) @128 "48 11 02 26 32 96" parses as "la [02-adj] [26-noun] [32-adj]"
  (or "la [02-26-noun] [32-adj]" -- the composition rival tested: "02 26"
  is 1x stream-wide, neither confirmed nor excludable); (d) @530 "qui
  [26] [32]" addressed: "qui est 32" x2 is the control; 26="est" killed
  globally by @239 ("la est" ungrammatical) -- state the crux, do not
  force; (e) "26n" reading (12 = final "n") tested at @239.
- **evidence:** F4. "11 26" exactly 2x, both "...fois, la [26]"; verb-parse
  of "la [26]" ungrammatical under banked values.
- **adverses:** only 2-3 legs; @1559's internal "pas" contradiction (the
  war's crux); T1-T3's eight verb windows must be answered, not ignored --
  if they hold, this target records the positional rule ("26 = feminine
  noun iff preceded by 11='la', else verb") with its polyvalence cost
  stated for the red team.
- **priority:** 2

### T5. noun26-69-pour-dire (priority 3)
- **id:** noun26-69-pour-dire
- **claim:** "[69] 26 pour dire" x3 decides noun-vs-verb via 69's class.
- **bars:** (a) trigram "26 00 33" x3 re-derived (@405, @933, @1627;
  @933/@1627 = byte-identical 8-gram "69 26 00 33 21 64 37 01",
  formula-bound, counted once); (b) 69's class named from its full
  12-window profile (followers 26 x3, 13 x2, 88 x2, 14, 24, 11, 74, 64;
  predecessors scattered); (c) "26 pour dire" parses under exactly one
  class with 69 fixed -- or the frame is recorded NULL with the "pour
  dire" selection puzzle stated ("[verb] pour dire" and "[noun] pour
  dire" both strained) and 1-3 follow-ups proposed (null regenerates).
- **evidence:** F5. "00 33" = "pour dire" (00="pour" A9; 33 = dire/croire
  rival); tails "01" @405 vs "21 64 37 01" @933/@1627.
- **adverses:** formulaic 8-gram weakens independence; 69's "69 11"
  (@1114) and "69 64" windows pull both ways; 33's value open.
- **priority:** 3

## Nulls and non-findings (results, not gaps)

- N1: "11 26" = exactly 2x stream-wide, both "...fois, la [26]". The noun
  theory has no independent "la 26" legs beyond the fois frames (+@128's
  "la [02] 26").
- N2: "26 30" = x4 on the repaired stream (queue's `homophone-12-30`
  says x3 -- corrected with positions @654/@991/@1249/@1559).
- N3: the "en ce qui" triple (@178/@1765/@1773) is real: one frame-type,
  three instances, X in {23, 26, 59}.
- N4: 26 is not formula-bound elsewhere: no 26 in the "vient de me
  parvenir" thirds, no 26 in the 94-07-06-94 mirror, no 26 in known
  formula tails. The only byte-identical dups are the two de-duplicated
  above.
- N5: "02 26" = 1x stream-wide (@127-128). The one-word composition rival
  for @128 can neither be confirmed nor excluded at finder level.
- N6: no single verb VALUE is proposed for all eight verb windows at
  finder level. "concerne"/"regarde" leads the "en ce qui" slot only;
  cross-frame value unification ("on _", "_ pas", "a _ par", "ne _")
  is battery work.

## Coverage map (already-queued targets: joint, not duplicated)

- `noun-26` (queued, p2): the war itself. T1-T5 are feeder frame
  batteries with narrower bars; they do not re-state its bar.
- `homophone-12-30` (queued, p4): same "26 12"/"26 30" windows, different
  question (12~30 merge vs 26's class). Joint; no bar overlap. Count
  correction (x4 not x3) supplied above.
- `frame-20-62-94` (queued, p3): @841's left context "20 62 94". Joint.
- `frame-37-reexam` (queued, p2): 37's value. T2 names 37's slot only;
  defers.
- `adj-32` (queued, p2): 32 at @128/@530. Joint. `fem-32e` (queued, p3)
  touches the same windows.
- `ent-06` (queued, p2): 06 after "26 30" x2 (@1249/@1559) and after
  "23 37" (@181). Joint.
- `ne-alone-02-74` (queued, p3): bare-"ne"/bare-"pas" licensing. T1's
  ne-audit feeds it.
- `prenne-70-12-94` (queued, p1): @1559's left context "00 46 70 12 94".
  Joint -- @1559's 94 belongs to "prenne", not to "26 pas".
- 84-adjudication (complete): 62's class for @841/@1469/@1706. Cited,
  not re-derived.
- `nest-subject-86-62-42` (queued, p1): "62 n'est" frames -- distinct
  from @841's "62 ne 26". Noted, not touched.
- `lever-77-78`, `ver-78-*` (queued): 78 follows "26 37" @1767. Joint.
- `stem-85` (queued, p3): 85 follows 26 @1752 ("26 24 85"). Joint.

## Method note

Windows extracted ±3 (widened to ±8/±15 for clause audits) from the
repaired 1,847-pair stream; clustered by follower FIRST (12 x4 | 30 x4 |
00 x3 | 32 x2 | singletons); formula windows de-duplicated by
byte-identity before counting (two dups found); predictions from 1840s
diplomatic French register; ranked by confidence x testability. Standing
constraints (§7) respected throughout: no settled kill re-litigated
(20="fois", 48-values, 84="fait"), 23~26 split honored, 67 sole
polyvalence untouched, R5005 never read.
