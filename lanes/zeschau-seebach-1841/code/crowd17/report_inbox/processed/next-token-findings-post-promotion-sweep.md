# Next-token findings: post-promotion sweep (wave 2)

Finder beat: post-promotion-sweep. Date: 2026-10-08.
Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` +
`data/upstream-ct_R5005.txt`, parsed like `code/side-keyhunt/repair_parse.py`).
`canonical.py` never used. R5005 untouched. Sealed gates untouched.
Red-team adjudication queue untouched. No data invented. @-offsets are 0-based
stream indices.

## Ground rules used

Battery-promoted (pending red-team ratification): 94="ne", 12="n", 48="e".
Provisional (NOT ground truth): 77="le?" (battery NULL), 33 (dire-33 NULL;
33={dire,[X]er} set stands), 78="ver?", 30="pas?", 39="a?", 59="est?".
Banked pencil GT: 11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que.
Granted: 87=ce, 64=qui, 96=par, 17=fois, 79=tout, 00=pour, 84=on, 47=ce,
45="ce" (A11 HOLD). A1 (37/32/42 predicative) is a grant: 42 is never re-valued
in this report. Settled kills not re-litigated: 48 word-values, 81="prin",
84="fait", {48,94} homophone-set, 09/92 "-ère", 20="fois".
The ne-battery's fence of @65 as "'enne'-shaped, analytic duality" is
respected as a fence, not re-verdict; this report tests what the fence
did not name.

Goal of the beat: frames that newly parse, or newly clash, under the JOINT
94/12/48 promotions and were invisible or ambiguous before them.

## Method

All 37 windows of 94, all 23 of 12, all 38 of 48 extracted ±3 (wider where
needed), glossed with promoted + provisional values, clustered by follower
pattern first. Identical repeats de-duplicated before counting frame-types.
Predictions use 1840s diplomatic French. Prior wave-2 reports
(ne-frames, n-e-frames) and the three battery reports (ne-94, n-e-12-48,
le-77 NULL) were read first; nothing below duplicates a queued target --
coverage map at the end.

## Ranked frames (confidence x testability)

### F1 (HIGH). "n'est pas" triple @558-560 — direct, unrepeated

@558 (a3_02): `34=i 17=fois 86 [94=ne] 59=est? 30=pas? 67=et/veut`
= "…86 n'est pas et/veut". The ONLY "94 59 30" trigram in the stream (x1,
verified). Load-bearing on provisional 59="est?" and queued 30="pas?", but
the trigram is exactly what the joint promotions predict: "ne"+"est"+"pas".
Second-order routing (no new battery -- both batteries already queued):
supports pas-30; ADVERSE to est-59-frames' uniform "30/39/37 after n'est are
predicative" claim, because here 30 after "n'est" is "pas", not a predicative.
The est-59-frames battery must fence or absorb @558.

### F2 (HIGH). "42 ne" x3 cluster — two bare, one "n'est"

- @494 (a2_11): `67=et/veut 78=ver? 42 [94=ne] 02 79=tout 88` = "…42 ne 02 tout…"
- @785 (a5_04): `11=la 24 42 [94=ne] 74 65 84=on` = "…42 ne 74 65 on"
- @1795 (a8_09): `86 56 42 [94=ne] 59=est? 37` = "42 n'est 37" (parses clean)
The ne-finder listed @494/@785 as unresolved singles (A6); formed as a
cluster they are one frame-type x2 (+1 "n'est" control). Under promoted
94="ne" with A1-predicative 42, the bare two clash: "ne" needs its verb
immediately, and no "pas" follows in ±5. 1840s French allows bare "ne"
before modals (pouvoir, savoir, oser, cesser) -- predicts 02/74 verb-shaped.
New battery target ne-alone-02-74 below. 42 itself is NOT re-valued (A1 grant).

### F3 (MEDIUM-HIGH). "77 78" x7 = "lever" composition; "48 77 78" x2 = "élever"

- @7: `06 77 78 18` = "06 lever 18"
- @213: `74 77 78 06 59=est?` = "74 lever 06 est?"
- @647: `88 77 78 52 82=m 94=ne` = "88 lever 52 m' ne"
- @1077: `98 98 12=n 48=e 77 78 64=qui` = "98 n elever 64" ("élever", 48="e" new)
- @1180: `37 77 78 94=ne 82=m 06` = "37 lever ne m' 06"
- @1351: `62 48=e 77 78 94=ne 82=m 06` = "62 elever ne m' 06" ("élever", 48="e" new)
- @1542: `88 77 78 43 00=pour` = "88 lever 43 pour"
7/7 adjacent, never split. The "élever" readings (@1077, @1351) exist ONLY
because 48="e" promoted -- pure second-order. The le-77 NULL battery itself
blessed this alternative ("may alternatively be the word 'lever'/'élever'
spanning the boundary"). Rival reading is the NULL's F2 "le [78]" article
frame on the same windows. New battery target lever-77-78 below.

### F4 (MEDIUM-HIGH). "32 48" x4 = "32e" feminine-agreement candidate

- @449: `61 59=est? 32 48 79=tout 17=fois` = "61 est 32e tout fois"
- @855: `64=qui 32 48 84=on 02` = "qui 32e on 02" (ADVERSE -- needs boundary)
- @1176: `74 32 48 59=est? 37` = "74 32e est 37" (clean copula frame)
- @1211: `64=qui 59=est? 32 48 96=par 45` = "qui est 32e par ce" (soft)
Closed set (exactly 4 "32 48" bigrams; zero "48 32"). Under 48="e" + A1
predicative 32, "32e" reads as feminine agreement: "est 32e" x2, "32e est" x1.
Invisible before 48's promotion. Load-bearing on provisional 59="est?" in
two windows. New battery target fem-32e below. Note: adj-32 (queued) covers
32's predicative value; this target is the inflection follow-up, not a rival.

### F5 (MEDIUM). Noun frames for 44, with one lone adverse

- @207: `42 06 77=le? 44 50` = "06 le 44 50" (verb + article + noun)
- @527: `47=ce 44 59=est? 37` = "ce 44 est 37" (demonstrative + noun + copula +
  predicative -- flagship; load-bearing on 59="est?")
- @1678: `74 77=le? 44 00=pour 46=que` = "74 le 44 pour que" ("pour que" =
  pour+que, clean purpose clause)
- "44 00=pour" x3 (@1311, @1583, @1679) = "[noun] pour [inf]"
- "42 44" x2 (@1617, @1838) = pre-nominal-adjective-shaped
- ADVERSE @1714: `65 [94=ne] 44 59=est? 30=pas?` = "65 ne 44 est pas" --
  ungrammatical under noun-44 ("ne" + noun). Resolves only via a stated
  boundary parse (e.g. "…65ne" word-final + "44 est [30-predicative]" under
  est-59-frames' own 30-claim) or a 59/30 re-value.
Full 44 inventory (n=15): followers 00 x3, 59 x2, 74 x2, 83 x2, 94/29/77/70/11
x1; predecessors 77 x2 ("77 44" @207/@1678), 12 x2, 42 x2 ("42 44" @1617/@1838).
New battery target noun-44 below. No queued target covers 44.

### F6 (MEDIUM, clash). "12 94 92" x2 -- the joint promotions' hard frame

- @64-66 (a1_01): `34=i 29=er 40=e [12=n] [94=ne] 92 69` = "…er e n ne 92"
- @1548-1550 (a8_00): `00=pour 46=que 70=pre [12=n] [94=ne] 92 45` =
  "pour que prenne 92"
Closed set ("94 92" x2 in the whole stream). @1548 is covered by queued
prenne-70-12-94 ("pre"+"n"+"ne" = "prenne"). @64's "e n ne" is the hard case:
the ne-battery fenced it as "'enne'-shaped, analytic duality" WITHOUT naming
the word ("…erenne"/"…ierenne" has no French word on record yet). With both
promotions locked, the fence must cash out to a named word or become a
residual. New battery target enne-word-64 below (Priority 1 -- the sharpest
second-order test in this report).

## Nulls and non-findings (results, not gaps)

- N1. "toute"/"toutefois" hunt: ZERO "79 48" bigrams in the stream. The one
  "48 79 17" (@450: "32 e tout fois") is reversed order -- "etoutefois" is
  not a word. Null recorded; no battery.
- N2. No new "est-ce" frame: the only "59 45" bigram is @103-104
  ("…94 93 59 45 28" = "ne 93 est-ce 28"), the same window already queued as
  est-ce-104. Not duplicated.
- N3. "74-74" x6 self-loop (@417, @816, @861, @919, @1053, @1637; predecessors
  "49" x5) does not parse under any current 74 value; carried as an adverse
  inside ne-alone-02-74, not a separate target.
- N4. @1664 "22 ne on qui" ("94 84" adjacency) stays fenced to A15-C3
  (ne-finder A5); not adjudicated here.
- N5. @509 "67 77 62 94 64" ("on ne qui") stays a true anomaly (ne-finder A1);
  unchanged by the promotions.
- N6. 12="n" shows no dominant follower cluster (48 x5, 94 x3, 16 x3) --
  the letter reading rests on GT bigrams, confirmed again; no new frame-type.

## Ranked battery targets for the supervisor

### T1 id "enne-word-64" -- PRIORITY 1
- claim: "One French word covers @63-66 ('34 29 40 12 94' = 'i er e n ne')
  under 12='n' + 94='ne' as letters, consistent with 'prenne' @1548."
- bars: "(1) the named word spans the 'enne' letters with stated boundaries;
  (2) 'prenne' @1547-1550 ('70 12 94') is undisturbed; (3) 92's class is
  consistent across @66 ('ne 92') and @1550 ('prenne 92'); (4) the ne-battery's
  'enne'-shaped fence is either cashed to the word or converted to a
  residual with stated cause -- the battery verdict itself is NOT downgraded."
- evidence: "@63-66 '08 i er e n ne 92 69' (a1_01); @1547-1550 '46 que pre n
  ne 92 45' (a8_00); '94 92' x2 is a closed set (92's predecessors: 00 x6,
  11 x3, 94 x2, 84 x2)."
- adverses: "No '...erenne'/'...ierenne' French word identified yet
  ('pérenne' needs 're'+'nne', but 29='er' is banked GT and breaks the
  segmentation); 92's scattered follower profile (22 windows, no dominant
  follower)."

### T2 id "lever-77-78" -- PRIORITY 2
- claim: "'77 78' reads 'lever' (infinitive; '48 77 78' = 'élever') in all 7
  windows, not article 'le' + stem 'ver'."
- bars: "(1) all 7 windows parse with 'lever'/'élever' + complement-shaped
  follower (18, 06, 52, 64, 94, 43); (2) F5's 'lever ne m'' x2 (@1180, @1351)
  resolves via a stated clause boundary or the conditioned-94 'en' reading;
  (3) @1077 'ne lever qui' resolves via a stated boundary or 12-48 re-parse;
  (4) '77 78' adjacency holds 7/7 (control: the bigram never splits)."
- evidence: "@7 '06 lever 18'; @213 '74 lever 06 est?'; @647 '88 lever 52 m'
  ne'; @1077 '98 n elever 64=qui' (48='e' second-order); @1180 '37 lever ne
  m' 06'; @1351 '62 elever ne m' 06' (48='e' second-order); @1542 '88 lever
  43 pour'. The le-77 NULL battery explicitly blessed the 'lever'/'élever'
  alternative at @1077/@1351."
- adverses: "Rival reading is the le-77 NULL's F2 'le [78]' article frame on
  the same 7 windows; @647 'lever 52 m' ne' has 'm'+'ne' order strain;
  @1077 'ne lever' is ungrammatical as words; 77='le' stays provisional per
  the NULL (this target tests the composition, not 77 alone). Relation:
  complementary to queued ver-78 (78 alone) and ne-le-1075 ('ne le' @1075)."

### T3 id "noun-44" -- PRIORITY 2
- claim: "44 is a noun."
- bars: "(1) article/demonstrative frames hold: '77 44' x2 (@207, @1678) and
  '47 44 59 37' @527 ('ce 44 est 37'); (2) complement frames hold: '44
  00=pour' x3 (@1311, @1583, @1679); (3) @1714 'ne 44 est pas' resolves via
  ONE stated parse (e.g. '...65ne' word-final + '44 est [30-predicative]',
  or a 59/30 re-value); (4) '44 11' @1617 and '44 29 48' @540 ('44ere')
  resolve or are fenced with stated cause."
- evidence: "44 n=15. '77 44' x2 (@207 '06 le 44 50', @1678 '74 le 44 pour
  que'); @527 'ce 44 est 37 qui' flagship (load-bearing on 59='est?');
  '44 pour' x3; '42 44' x2 (@1617, @1838); followers 00 x3 / 59 x2 / 74 x2 /
  83 x2."
- adverses: "@1714 '65 ne 44 est pas' (lone hard adverse -- 'ne'+noun
  ungrammatical); @1617 '42 44 la' ('44 la' needs a boundary); @540 '91 n
  44 er e 42' ('44ere' feminine-stem sub-frame open)."

### T4 id "ne-alone-02-74" -- PRIORITY 3
- claim: "02 and 74 are the negated verbs in '42 ne 02' (@494) and '42 ne 74'
  (@785); bare 'ne' is licensed 1840s-style (modal or fixed frame)."
- bars: "(1) both windows parse as '[42] ne [verb]...' with 'pas' located
  downstream or 'ne'-alone justified against the 1840s modal list
  (pouvoir/savoir/oser/cesser); (2) 02/74 show verb-frame contact somewhere
  (A8 80/89-class, 29='er', 85-stem, or infinitive complement); (3) the
  '74 74' x6 self-loop (@417, @816, @861, @919, @1053, @1637) parses under
  the winning value or is fenced as formula; (4) @1795 '42 n'est 37' stays
  consistent. 42 is NOT re-valued (A1 grant holds)."
- evidence: "@494 '67 78=ver? 42 ne 02 tout 88'; @785 '11=la 24 42 ne 74 65
  84=on'; @1795 '42 n'est 37' control. '42 94' x3 is a closed set."
- adverses: "02's followers (79/24/00 x2...) and 74's followers (74 x6, 45,
  46, 62...) show no verb markers yet; '74 74' x6 resists verb-shape;
  A1-predicative 42 needs a clause/subject account for '42 ne'."

### T5 id "fem-32e" -- PRIORITY 3
- claim: "'32 48' x4 reads '32e', feminine agreement of predicative 32."
- bars: "(1) all 4 windows parse with '32e' as feminine predicative adjective;
  (2) copula frames @449/@1176/@1211 ('est 32e' x2, '32e est') are clean;
  (3) closed set verified: exactly 4 '32 48' bigrams, zero '48 32'."
- evidence: "@449 '61 est 32e tout fois' (load-bearing on 59='est?'); @855
  'qui 32e on 02'; @1176 '74 32e est 37' (load-bearing on 59='est?'); @1211
  'qui est 32e par ce'. A1 predicative-32 + promoted 48='e'."
- adverses: "@855 'qui 32e on' needs a clause boundary or re-parse ('qui'+
  adjective without copula is ungrammatical); @449's tail 'tout fois'
  ('79 17') vs A5 'tout' class-level grant (fence to A5, do not re-litigate).
  Relation: inflection follow-up to queued adj-32, not a rival."

## Coverage map (already queued -- NOT duplicated)

prenne-70-12-94 ("prenne" composition) | ni-1740-1742 ("86 12 34 94 82 46"
boundary) | ne-le-1075 ("ne le" @1075) | ne-24-profile ("ne 24 ce" x2) |
verb-93 (F7 consequence) | frame-62-94-79 ("62-94-79-14-60") |
formula-94-07-06-94 ("94 07 06 94" mirror) | prof-53 ("53 ne"/"donne") |
est-59-frames (30/39/37 after "n'est" -- receives @558 as adverse input) |
pas-30 (receives @558 "n'est pas" as support) | croire-33-compound85
("85 33 94 30" @1700) | ne-30-1700 ("n'importe" rival) | elision-77-84 |
lon-09-verb | lon-29-146 | nest-subject-86-62-42 | ver-78 | ent-06 | adj-32 |
noun-26 | frame-94-82-06-06 | le83-window | est-ce-104.

## Constraints respected

No settled kill re-litigated. 42 never re-valued (A1). @65's ne-battery fence
respected (T1 deepens it, never downgrades the promote verdict). R5005,
sealed gate instances, and the red-team adjudication queue untouched.
battery-queue.json and finder-beats.md not edited (supervisor ingests this
report next run).

## Bottom line

Five second-order battery targets, ranked: T1 enne-word-64 (P1 -- the joint
12/94 promotions' hardest open frame, fence must cash out to a named word);
T2 lever-77-78 (P2 -- "lever"/"élever" composition, blessed by the le-77
NULL, rival to its F2 article reading); T3 noun-44 (P2 -- "ce 44 est 37"
flagship, one lone adverse @1714); T4 ne-alone-02-74 (P3 -- "42 ne" x2
cluster vs A1); T5 fem-32e (P3 -- feminine agreement under 48="e").
Headline frame: "n'est pas" @558-560, the only direct "94 59 30" trigram,
newly visible under the joint promotions -- support for queued pas-30,
adverse input for queued est-59-frames. Two clean nulls recorded (N1
"toute/toutefois", N2 "est-ce").
