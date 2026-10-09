# Battery report: class-55-det

Target: `class-55-det`. Claim: 55 is a determiner-shaped particle (a separate
grammatical word), not a word-internal prefix to 61.
Date: 2026-10-09. Worker: 626275f2-a724-4ff3-899a-ef33f745afab (battery worker).
Lock `locks/class-55-det.lock` created 2026-10-09T04:46:02Z (no pre-existing
lock for this id); deleted on completion.

Offset convention: @n = 0-based pair index in the repaired 1,847-pair stream
(same convention as battery-subj-55-61-word and battery-seg-55-61-21-stem).

## Bar (verbatim, pre-registered)

"decide 55's class from the '55 81' x6 windows (@25/@523/@550/@1085/@1094/@1671)
plus a stream-wide successor/predecessor census of 55: determiner-shaped iff
>=2 clean pre-noun slots parse with stated glosses and no window forces
word-internality; state the W1 re-segmentation consequence ('[13] [55] [61]'
with 61 as noun stem) if 55 is a separate word"

## Bar restated (numbered pass/fail clauses; frozen before testing)

1. At least 2 of the '55 81' x6 windows parse as CLEAN pre-noun slots
   (55 = determiner-shaped particle before noun 81) with stated glosses.
2. No window in the stream forces 55 to be word-internal (all 12 of 55's
   windows admit a separate-word parse at battery grade).
3. The W1 re-segmentation consequence is stated: '[13] [55] [61]' with 61
   as noun stem, if 55 is a separate word.

## Method

Read BATTERY-PROTOCOL.md first, then battery-queue.json (target entry:
priority 2, status queued, no lock). Re-derived the repaired 1,847-pair /
96-type stream from `data/upstream-ct_R5005.txt` +
`code/side-keyhunt/repaired_offsets.json`, parsed per
`code/side-keyhunt/repair_parse.py` (byte-exact stride-2 pairing per row
offset); asserted 1,847 pairs / 96 types before testing. `canonical.py`
never used. R5005, sealed gates, red-team queue untouched. Every number
below re-derived in-session (script /tmp/cls55.py, session-local); no prior
counts trusted. Standing values used per protocol section 7 (banked GT,
granted/promoted/provisional as listed there); 81's battery-promoted
masculine-abstract-noun value (noun-81, 2026-10-09) and 06='ent'
conditional promote used where stated.

## Stream-wide census of 55 (re-derived)

- 55 n = 12. Positions (0-based): 25, 523, 550, 576, 906, 1085, 1094, 1167,
  1205, 1285, 1611, 1671.
- Successors: 81 x6, 61 x3, 83 x2, 68 x1.
- Predecessors: 13 x2, 33 x1, 06 x1, 46 x1, 18 x1, 02 x1, 07 x1, 43 x1,
  98 x1, 08 x1, 78 x1 (11 distinct).
- The six '55 81' indices verified: stream[i]='55' and stream[i+1]='81'
  at all of @25/@523/@550/@1085/@1094/@1671.
- 61 census (adverse check, re-derived): n=18; 15 distinct predecessors
  (55 x3, 62 x2, rest x1); 14 distinct successors (96/59/94/21 x2, rest x1);
  max successor count x2. 61->81 x0 and 81->61 x0 stream-wide (zero contact
  either direction, confirming the target brief's distributional point).

## Window-level evidence

### The six '55 81' windows (+/-6 context, 0-based)

- @25 (a1_00): `98 82 43 29 47 33 | 55 81 | 00 34 24 30 03`
  = "...m(82) [43]er(29) ce(47) [33] | [55] [81] | pour(00) i(34)..."
  The "les [81]" slot is determiner-shaped, but the left edge "ce [33]"
  does not license it cleanly: 33 is the "dire"-lead (noun "dire" exists,
  "le dire"), giving "ce dire les [81]" — an asyndetic double NP with no
  independently established clause boundary. FENCED, not clean.
- @523 (a3_00): `80 09 70 91 77 06 | 55 81 | 97 47 44 59 37`
  = "...[80] [09] pre(70) [91] le(77) [06] | [55] [81] | [97] ce(47)..."
  "77 06" occurs x1 stream-wide (@521); "06 55" x1 (@523). The left edge
  "le"+"ent" resists a clean word parse either way ("le"+"ent" elision
  leaves the word incomplete; "…91-77" cannot supply a verb stem ending
  in "le"). The slot "…ent les [81]" is plausible (transitive verb +
  "les [noun]") but the verb is unparsed. FENCED, not clean.
- @550 (a3_01): `06 00 46 24 47 46 | 55 81 | 00 86 59 34 17`
  = "...[06] pour(00) [24] ce(47) que(46) | [55] [81] | pour(00) [86] est(59)..."
  Gloss: "ce que les [81] pour [86-inf]" — "que les [81]" is a clean
  determiner slot; 81 = masculine abstract noun (promoted noun-81, whose
  flagship is 'le [81] pour [INF]' @1086 — the same "pour [inf]"
  complement shape recurs here); 86 = INF-class (A9). CLEAN. PASS.
- @1085 (a6_05): `64 06 52 89 24 02 | 55 81 | 00 33 79 80 06`
  = "...[89-verbframe] [24] [02] | [55] [81] | pour(00) [33]..."
  The licensor "24 02" does not cleanly license "les [81]": 24's class
  (verb/preposition per ne-24-profile) leaves "24 02" unparsed as a unit,
  and 02 (n=17, scattered) supplies no determiner-licensing role.
  FENCED, not clean.
- @1094 (a6_06): `33 79 80 06 43 07 | 55 81 | 06 29 67 86 52`
  = "...[43] [07] | [55] [81] | [06] er(29)..."
  Left licenses: 07 is verb-shaped ("que [07]" x2 via 46, "ne [07]" x1
  via 94 — verb-selecting predecessors), so "[07-verb] les [81-noun]"
  parses ("[verb] the [81]"). BUT the right edge "81 06 29" admits an
  unexcluded word-internal rival ("[81]ent[er]"-shaped: 06='ent' x1 after
  81 stream-wide, 29='er'); excluding it needs letter-level reanalysis
  of 06/29, beyond battery grade. FENCED, not clean.
- @1671 (a8_05): `84 64 06 91 11 78 | 55 81 | 92 60 03 39 74`
  = "...la(11) [78-ver] | [55] [81] | [92]..."
  "la [78]" is a complete NP; "les [81]" after it is NP pile-up unless
  an unmarked clause boundary is posited ("…la [78]. Les [81] [92]…"),
  which is not independently established here (92's class open;
  "pour [92]" x6 suggests infinitive, which cannot follow "Les [81]").
  "78 55" also admits an unexcluded word-internal rival. FENCED.

Clause-1 tally: 1 clean (@550), 5 fenced. The bar needs >=2.

### Census windows beyond the six (successors 61/83/68)

- '55 61' x3: @576 (a3_02) `...87 78 45 13 | 55 61 | 94 82 06 06...`;
  @1167 (a6_09) `...78 45 13 | 55 61 | 94 87 83 21...`;
  @1205 (a7_00) `...58 47 43 | 55 61 | 21 65 64...`.
- '55 83' x2: @906 (a5_09) `...88 18 | 55 83 | 54 49...`;
  @1611 (a8_03) `...23 08 | 55 83 | 71 48...`. 83's class is torn
  ("98 [83]" x5 de-position vs "ce [83]" x2 nominal vs "les [83]" x2) —
  "les [83]" cannot be graded a clean pre-noun slot. FENCED.
- '55 68' x1: @1285 (a7_03) `...32 98 | 55 68 | 00 11 17 84...`.
  68 is nominal (predecessors "a(39)/tout(79)/ce(47) [68]"), so "les [68]"
  is determiner-shaped; but the licensor 98 (n=40, 26 distinct
  successors) is class-open and licenses nothing cleanly here.
  FENCED, not clean.

### W3 @1205 — the word-internality test (clause 2)

W3 span: `58 47 43 55 61 21 65` = "[58] ce(47) [43] [55] [61] [21] [65]".
Standing battery verdict seg-55-61-21-stem (PROMOTE, 2026-10-09) decides
this window as the bare finite stem: "ce [43-noun] prend(55-61)
[21-noun]. [65] qui(64) est(59)…" — 55-61 ONE word ("prend"), 55
word-internal ("pre"/"pr" + "nd"/"end" per that report's flagged
segmentation residual).

Separate-word rival parses of 55 at W3, tested:
- (a) 55 = determiner ("les"/"des"): "ce [43] les [61] [21]" — complete
  NP "ce [43]" followed by two more NPs; ungrammatical. DEAD.
- (b) 55 = object clitic ("les"): "ce [43] les [61-verb] [21]" — "les"
  as DO plus a second DO "21"; ungrammatical. DEAD.
- (c) 55 = determiner, 61 = adjective: "ce [43] les [61-adj] [21]" —
  same NP pile-up. DEAD.
- (d) 43 = "que" (relative): "ce que les [61-verb] [21]" — 43's profile
  is noun-shaped 15/16 windows ("par [43]" x2 ungrammatical under
  "que"); and the parse still strands two objects. DEAD.
- (e) 55 = "les" (determiner), 43 = finite verb: "ce [43-verb] les
  [61-noun]" — "this [verbs] the [61]" — grammatical ONLY IF 43 is a
  3sg finite verb here. 43 is noun-shaped in 15/16 windows; the single
  non-noun window (@22, "[43]er" infinitive) is already a fenced
  conditioned-split residual. A noun-15x/finite-verb-1x class split for
  43 is positional polyvalence, which a battery may not declare (§7;
  red-team venue only). NOT battery-available.

Every battery-available separate-word parse of 55 at W3 is
ungrammatical; the one-word "prend" parse is promoted and standing.
W3 FORCES word-internality of 55.

## Per-clause pass/fail

1. **FAIL.** Only 1 of the 6 windows (@550) parses as a clean pre-noun
   slot with a stated gloss; the bar needs >=2. The five others are
   fenced with stated cause (unlicensed left edges @25/@523/@1085,
   unexcluded word-internal rival on the right edge @1094, NP pile-up
   vs unestablished boundary @1671). Census windows add no clean slot
   ("les [83]" x2: 83's class torn; "les [68]" x1: licensor 98 open).
2. **FAIL (kill grade).** W3 @1205 forces 55 word-internal: the standing
   promoted discriminator (seg-55-61-21-stem) decides 55-61 as the
   one-word bare stem "prend", and no battery-available separate-word
   parse survives (the sole grammatical rival needs 43=finite verb,
   overturning 43's 15/16-window noun profile — red-team venue, not
   battery). Under §7's sole-polyvalence rule, 55 cannot be a separate
   word at 11 windows and word-internal at 1. A cleaner rival value is
   demonstrated on the same frame ("prend(55-61)", promoted).
3. **PASS (stated with fences).** IF 55 were a separate word, W1
   (0-based @576-577, row a3_02: `87 78 45 13 | 55 61 | 94 82 06 06`)
   re-segments as "[13] [55-det] [61-noun-stem] ne(94) mentent":
   "ce(87) verdict(78-45, LEAD) [13] les [61] ne mentent" —
   "this verdict: the [61] don't lie", with 61 as noun stem
   (compatible with "61 59" x2 = "[61] est", and with 61's scattered
   profile: 15 distinct predecessors / 14 distinct successors, max x2,
   which neither confirms nor kills nominal-61). FENCES (per the
   adverses): (i) subj-13-value KILLED 13's determiner arm at kill grade
   and queued pronoun-13-les — the "[13]" slot's value is owned by that
   lane, and under 13=pronoun-"les" the "[13] [55=les]" adjacency is
   ungrammatical, so this re-segmentation is gated on pronoun-13-les's
   adjudication of its "13->55 x2" windows; (ii) W3's promoted "prend"
   makes 61 verb-stemmed there vs noun-stemmed here — a positional
   polyvalence question for the red team (§7), not decidable at battery
   level.

## Adverses answered

- **subj-13-value owns the 13 side:** honored — 13's value not decided
  here. Used only its standing verdicts: determiner arm KILLED at kill
  grade (battery-subj-13-value, 2026-10-09); pronoun-13-les queued (its
  bars explicitly cover the "13->55 x2" @575/@1166 windows). The W1
  consequence above is stated conditionally and gated on that lane.
- **61's scattered profile neither confirms nor kills:** re-derived —
  n=18, 15 distinct predecessors (55 x3, 62 x2, rest x1), 14 distinct
  successors (96/59/94/21 x2, rest x1), zero 81-contact either direction
  (61->81 x0, 81->61 x0). "61 59" x2 ("[61] est") leans nominal; nothing
  in the profile confirms or kills 61-as-noun-stem. Adverse sustained
  as stated.
- **'55-61 word' segmentation now suspect:** sharpened, not just
  suspected — at W3 the word segmentation is PROMOTED ("prend(55-61)",
  seg-55-61-21-stem), while at the other 11 windows 55 is
  separate-word-shaped. The segmentation is window-dependent, which is
  a §7 second-polyvalence-shaped observation packaged below for the
  red team; it is not decided here.

## Verdict: KILL

Clause 2 fails at kill grade: W3 (@1205) forces the claim false — 55 is
word-internal there under the standing promoted "prend(55-61)"
discriminator, and §7's sole-polyvalence rule bars a
separate-at-11 / word-internal-at-1 split at battery level. (Clause 1
also fails: 1 clean pre-noun slot of the required >=2.) The cleaner
rival on the same frame is demonstrated and standing ("prend").
No standing verdict is contradicted or downgraded — this kill CONFIRMS
seg-55-61-21-stem's W3 decision and agrees with subj-55-61-word's kill
logic (W3's verb-shaped 55-61 forcing the uniform claim false
stream-wide).

## Observation for the supervisor / red team (not a queued target)

The 11-vs-1 segmentation split (separate-word 55 everywhere except W3's
promoted one-word "prend") is a positional-polyvalence-shaped tension
between two standing battery verdicts (this kill + seg-55-61-21-stem's
promote). If the red team ever declares a second polyvalence or a
positional segmentation rule, the '55 81' x6 determiner-shaped legs
(@550 clean, @1094 left-licensed) are the live evidence for the
separate-word arm. No target proposed — supervisor's call.

## Bookkeeping

- Report: this file.
- `battery-queue.json`: `class-55-det` queued -> verdict/kill via
  temp-file + rename (pre-write assert confirmed queued/verdictless;
  JSON re-validated post-write). Own entry only.
- Lock created on start (agent id + UTC), deleted on completion.
- `canonical.py` never used. R5005, sealed gates, red-team queue untouched.
- No standing verdict contradicted or downgraded.
