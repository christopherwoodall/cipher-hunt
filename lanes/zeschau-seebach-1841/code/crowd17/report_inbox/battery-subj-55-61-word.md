# Battery report: subj-55-61-word

Target: `subj-55-61-word`. Claim: name the 55-61 word via the W3 window
(@1206-1207 '43 [55-61] 21') and the 55->81 x6 noun-context legs.
Date: 2026-10-09. Worker: c46f79c6-e07d-4bde-9206-0e2cdc03b0b7 (battery worker).
Lock `locks/subj-55-61-word.lock` created 2026-10-09T04:19:43Z (no pre-existing
lock for this id); deleted on completion.

Offset convention: @n below = 0-based pair index in the repaired 1,847-pair
stream (matches battery-name-55-61-core and battery-seg-55-61-21-stem).
1-based equivalents: 55-61 = @1206-1207 at W3, @577-578 at W1, @1168-1169 at W2.

## Bar (verbatim, pre-registered)

"a plural-noun value ('temoins'/'hommes'/...) completes W1's subject slot"

## Bar restated (numbered pass/fail clauses)

Restatement is mechanical from the queue's bars/claim/adverses fields; the
bars text is unmodified.

1. A specific French plural-noun value for the 55-61 word is NAMED
   (e.g. 'temoins'/'hommes'/...), pinned by the W3 window
   (@1205-1206 '43 [55-61] 21') and/or the 55->81 x6 noun-context legs.
2. The named value completes W1's subject slot: 'ce verdict [13]
   [55-61=named-plural] ne mentent' parses with 55-61 as the 3pl subject
   (or head of the 3pl subject NP) of "ne mentent".
3. Coordination honored: no duplication of name-55-61-core's scope (verdict
   null, 2026-10-08) — this battery tests only the plural-noun value claim
   via the W3 / 55->81 route, not the general naming bar.

## Method

Read BATTERY-PROTOCOL.md and battery-queue.json first. Re-derived the repaired
1,847-pair / 96-type stream from `data/upstream-ct_R5005.txt` +
`code/side-keyhunt/repaired_offsets.json`, parsed per
`code/side-keyhunt/repair_parse.py` (byte-exact stride-2 pairing per row
offset); asserted 1,847 pairs / 96 types before testing. `canonical.py` never
used. R5005, sealed gates, red-team queue untouched. Every number below was
re-derived in-session (script /tmp/subj5561.py); no prior counts trusted.

Standing values used (protocol section 7): banked GT 11=la, 82=m, 29=er,
40=e, 46=que; granted 87=ce, 47="ce" (A4 allophone tier), 00="pour";
battery-promoted 94="ne" (STRONG LEAD), 06="ent" (conditional), 30="pas";
provisional 59="est", 77="le"; leads 78="ver" (R16-005), 45="dict" (R16-004);
67 et/veut sole true polyvalence. 21=NOUN class (registry, kept by
seg-55-61-21-stem). Values of 13, 43, 55, 61, 81 open.

## Window-level evidence (re-derived)

### 55-61 census: exactly x3 (matches name-55-61-core)

- W1 @576-577 (row a3_02): `...87 78 45 13 | 55 61 | 94 82 06 06...`
  pred 13, suc 94. Full row: `94 59 30 67 11 43 24 80 97 13 76 45 94 52 87 78
  45 13 55 61 94 82 06 06 50 10 19 18 14 00 97 41`
- W2 @1167-1168 (row a6_09): `...78 45 13 | 55 61 | 94 87 83 21...`
  pred 13, suc 94. Full row: `00 92 29 80 17 77 82 44 83 21 67 78 45 13 55 61
  94 87 83 21`
- W3 @1205-1206 (row a7_00): `...58 47 43 | 55 61 | 21 65 64...`
  pred 43, suc 21. Full row: `46 07 24 82 16 96 82 16 64 29 45 58 47 43 55 61
  21 65 64 59 32 48 96 45 36 77 83 92`

### W3 plural-noun parse test (the naming instrument)

W3 target span (0-based @1203-1209): `58 47 43 55 61 21 65`
= "[58] ce(47, granted) [43] [55-61] [21-noun] [65-noun] qui(64)...".

Every structural option for 55-61 = plural noun at W3 was tested:

- (a) Second NP after "ce [43]": 47="ce" (granted, singular) forces 43
  singular; a bare plural noun with no determiner after a complete singular
  NP is ungrammatical. DEAD.
- (b) Apposition to "ce [43]": appositives share the referent; "ce [43]"
  singular vs plural X mismatch. DEAD.
- (c) Adjective modifying 43: 43 singular (with "ce") vs plural X —
  number disagreement. DEAD (and then X is an adjective, not the noun).
- (d) Relative clause via 43="que": "ce que [55-61-pl] [21]..." — 21 is
  NOUN class (registry, battery-kept); no verb follows, clause ungrammatical.
  43's profile (suc 00x3, 77x2, 87x2, 98x2, ...) is noun-shaped, not
  relative-pronoun-shaped. DEAD.
- (e) 43 as preposition ("ce de/par [X]"): "ce" demonstrative takes no
  prepositional complement. DEAD.
- (f) 43-55-61 as one 3-syllable word: "ce [43-55-61]" singular under "ce"
  — not plural. DEAD.
- (g) "ce sont" frame: no "sont" present (43 is not "sont"; noun-shaped).
  DEAD.

The live W3 parse remains the promoted seg-55-61-21-stem discriminator:
"[58] ce(47) [43] prend(55-61, finite 3sg) [21-noun direct object]. [65] qui
est..." — "this [43] takes [21]". No plural-noun parse is grammatical at W3.

### 55->81 x6 legs (re-derived)

All six, 0-based with +/-6 context:
- @25 (a1_00): `98 82 43 29 47 33 | 55 81 | 00 34 24 30 03`
- @523 (a3_00): `80 09 70 91 77 06 | 55 81 | 97 47 44 59 37`
- @550 (a3_01): `06 00 46 24 47 46 | 55 81 | 00 86 59 34 17`
- @1085 (a6_05): `64 06 52 89 24 02 | 55 81 | 00 33 79 80 06`
- @1094 (a6_06): `33 79 80 06 43 07 | 55 81 | 06 29 67 86 52`
- @1671 (a8_05): `84 64 06 91 11 78 | 55 81 | 92 60 03 39 74`

81's profile: n=14; pred {55x6, 77x4, 43, 98, 39, 08}; suc {00x3, 97x2, 87x2,
30, 85, 06, 88, 03, 82, 92}. 81 is noun-shaped (77="le" x4 before it;
"81 pour[00]" x3). In the six legs, 55 sits directly before a noun in
determiner/particle-shaped slots (e.g. @550: "ce(47) que(46) [55] [81]
pour(00) [86-inf]" — "ce que les [81] pour [inf]"-shaped). 55's value is
open; the legs do not name it.

Decisive distributional point: the legs never implicate 61. 61's successor
census (n=18): {96x2, 59x2, 94x2, 21x2, 20, 42, 70, 88, 24, 31, 56, 12, 40,
15} — zero 81. In the six 55->81 windows the token after 81 is {00x3, 97,
06, 92} — never 61. The "noun-context legs" constrain 55's pre-noun
behavior; they cannot name the 55-61 word.

### W1 slot compatibility (for the record)

W1 @573-579 (1-based): `87 78 45 13 55 61 94` = "ce(87) verdict(78-45, LEAD)
[13] [55-61] ne(94)". With 13 as a plural determiner ("les"/"des" — value
open, queued subj-13-value), "les [X-pl] ne mentent" parses for ANY
2-syllable plural noun X. Compatibility holds; no specific X is forced —
the candidate space ({temoins, serments, ...}) remains structurally
underdetermined, as found by battery-name-13-55-61 and
battery-name-55-61-core.

## Per-clause pass/fail

1. **FAIL (kill grade).** No plural-noun value is nameable, and the naming
   instrument is broken at the window level: W3's 55-61 is verb-shaped
   ("prend" per the promoted seg-55-61-21-stem discriminator), and an
   independent seven-option parse check finds no grammatical plural-noun
   reading at W3 (the blockers are granted/battery-kept values: 47="ce"
   singular, 21/65 noun class). The 55->81 x6 legs never implicate 61 and
   name nothing. Under section 7's sole-polyvalence rule (67 et/veut; battery
   may not declare a second polyvalence), the 55-61 word takes one value —
   W3's verb reading forces the plural-noun value false at all windows.
2. **VACUOUS (no value named).** W1's slot is compatible with an unnamed
   plural noun, but compatibility is not completion by a named value. 13's
   determiner value stays open (queued subj-13-value).
3. **PASS (honored).** name-55-61-core (verdict null, 2026-10-08) consulted,
   not duplicated: its general-naming bar was not re-tested; this battery
   scoped strictly to the plural-noun value claim via the W3/55->81 route.

## Adverses answered

- "coordinate with queued name-55-61-core; do not duplicate": honored —
  name-55-61-core is verdict/null (its report lives at
  code/crowd17/report_inbox/processed/battery-name-55-61-core.md); its
  census (55-61 x3, pred 13/13/43, suc 94/94/21) was re-derived, not
  carried over; its naming bar was not re-run.

## Verdict: KILL

The plural-noun value for the 55-61 word is forced false: W3 (@1205-1206)
forces 55-61 verb-shaped, and section 7's sole-polyvalence rule bars a
noun-at-W1/verb-at-W3 split at battery level. A cleaner rival is
demonstrated on the same W3 frame ("prend" + noun object, promoted
discriminator seg-55-61-21-stem, 2026-10-09). No standing red-team verdict
is contradicted — this kill CONFIRMS seg-55-61-21-stem's W3 parse and
NARROWS (does not overturn) w1-573-subject's null: W1's 3pl-subject slot
stays open, but the 55-61-word-as-plural-noun route to it is closed.

Scope of the kill (narrow): the plural-noun VALUE for the 55-61 2-pair word
only. NOT killed: W1's subject being a 3pl NP under a different
segmentation (queued subj-13-value); 61 alone being nominal; 55 being
determiner/particle-shaped (the 55->81 legs lean that way: 55's value is
open, and "55-61" as a word unit is now suspect — see note below).

## Note for the supervisor (observation, not a target proposal)

The 55->81 x6 legs show 55 repeatedly in determiner-shaped pre-noun slots
(@550 "ce que [55] [81] pour [86]" the cleanest). If 55 is a separate
grammatical word (plural determiner "les"/"des"-shaped), the "55-61 word"
segmentation itself is suspect and W1's subject may be "[13] [55] [61]"
with 61 as the noun stem. 61's scattered profile (15 distinct predecessors,
14 distinct successors, max x2) neither confirms nor kills this. Deciding
55's class is the live adjacent question; subj-13-value (queued) owns the
13 side.

## Bookkeeping

- Report: this file.
- `battery-queue.json`: `subj-55-61-word` queued -> verdict/kill via
  temp-file + rename (pre-write assert confirmed queued/verdictless; JSON
  re-validated post-write). Own entry only.
- Lock created on start (agent id + UTC), deleted on completion.
- `canonical.py` never used. R5005, sealed gates, red-team queue untouched.
- No standing verdict contradicted or downgraded.
