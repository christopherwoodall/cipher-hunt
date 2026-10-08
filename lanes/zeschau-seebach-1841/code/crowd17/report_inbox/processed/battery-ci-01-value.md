# Battery report: ci-01-value

- Target id: `ci-01-value`
- Claim: "01 = 'ci' vs 'faisant' discriminator"
- Date: 2026-10-08
- Worker: battery worker (subagent e12d3e97-98ad-40e2-88b0-0264846cdc6d)
- Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json +
  data/upstream-ct_R5005.txt, parsed per code/side-keyhunt/repair_parse.py).
  All @-offsets are 0-based repaired-stream indices. n(01) = 28.
- Lock: code/crowd17/next-token/locks/ci-01-value.lock (created at start,
  deleted at end; no prior lock existed).

## Bar (verbatim, pre-registered before testing)

"name 01 iff '01 24' x3 and '37 01' x3 cohere under one value ('ci' vs
'faisant') with <=10% orphan"

Numbered pass/fail clauses (restated before testing, not modified after):

1. The three '01 24' windows cohere under ONE candidate value ('ci' or
   'faisant'): each of the three parses grammatically under that value.
2. The three '37 01' windows cohere under the SAME value as clause 1:
   each of the three parses grammatically under that value.
3. Over all 28 windows of 01, the named value leaves <=10% orphan
   (<=2 of 28 windows unparseable under the named value).
4. The rival value is killed or downgraded on at least one discriminator
   group (or the bar fails for both and no value is named).
5. Adverses answered: (a) "'ceci' vs 'ce faisant' both grammatical" --
   the tie at '87 01' must be broken by the discriminators, not by the
   bar's own window; (b) "37's value open" -- '[37]-ci' needs nominal-37,
   which is ungranted; any 'ci' naming must state 37's status.

Offset note: the brief's "'87 01' @1033" is the @1028-1033 region
(0-based: 87 @1028, 01 @1029, 77='le' @1033). Discriminator counts
re-derived on the repaired stream: '01 24' x3 = @40, @828, @984;
'37 01' x3 = @940, @1634, @1818; '87 01' x2 = @345, @1029;
'47 01' x1 = @195. Counts match the brief exactly.

## Method

1. Recomputed the repaired parse in-session (1,847 pairs, 96 groups).
   Never used canonical.py. R5005 not touched.
2. Enumerated all 28 windows of 01 with +-8 context; ran predecessor and
   successor censuses.
3. Tested each discriminator window under 01='ci' and under 01='faisant'
   against standing grants: 24 = finite verb, modal-shaped,
   infinitive-taking (ne-24-profile, battery-PROMOTE 2026-10-08,
   class-level); 87 = 'ce' (granted); 45 = 'ce' (A11 HOLD,
   allophone tier); 37 = predicative frames granted (A1) but value open
   and under red-team re-examination (frame-37-reexam NULL, escalated).
4. Swept the remaining 19 windows for any clean parse under either value
   (a clean parse would weaken a kill; none found).
5. Correction recorded: battery-le1033-imperative (2026-10-08) said
   "'01 24' x3 fits 'ci-[24]' compounds (ci-dessus / ci-apres / ...)"
   under 'ci'. That was written BEFORE ne-24-profile promoted 24 to
   finite verb. With 24 = finite verb, the ci-compound reading is dead:
   24 cannot be 'dessus'/'apres'/'joint'. The "both live" assessment is
   overturned by the 24 class grant. This correction is load-bearing for
   the kill below: if the 24 class grant is ever overturned, re-open.

## Window-level evidence

### Discriminator group 1: '01 24' x3 (24 = finite verb, granted)

W1 @40 (row a1_01): `64 32 01 08 91 39 64 41 01 24 88 43 81 30 62`
= "qui [32] [01] [08] [91] a(39) qui(64) [41] [01] [24] [88] [43]
[81] pas(30) [62]".
- Under 'ci': "[41] ci [24]" = "ci" directly before a finite verb.
  Ungrammatical in French: "ci" never heads a phrase and never
  precedes a finite verb (it occurs only bound: ceci, celui-ci,
  ci-dessus, par-ci par-la). FORCES 'ci' FALSE at this window.
  Word-internal escape ("[41]ci" = voici/merci) does not parse either:
  "qui voici [24]" / "qui merci [24]" are both ungrammatical
  ("voici" takes a noun, not a finite verb).
- Under 'faisant': "[41] faisant [24]" = participle + finite verb with
  no subject. Ungrammatical. FORCES 'faisant' FALSE at this window.

W2 @828 (row a5_06): `40 95 13 24 87 59 38 82 01 24 87 11 77 76 59`
= "e(40) [95] [13] [24] ce(87) est(59) [38] m(82) [01] [24]
cela(87-11) le(77) [76] est(59)".
- Under 'ci': "m(82) ci [24]" = "m' ci [24]". Un-grammatical
  (same rule as W1). FORCES 'ci' FALSE. No word-internal rescue
  ("m'ci" is not a French word).
- Under 'faisant': "m' faisant [24] cela" = participle + finite verb,
  no subject. FORCES 'faisant' FALSE.

W3 @984 (row a6_01): `01 00 92 07 76 47 78 45 01 24 89 48 01 76 49`
= "[01] pour(00) [92] [07] le(77) ce(47) [78] ce(45) [01] [24]
[89] [48] [01] le(77) [49]".
- Under 'ci': "ce(45)-ci [24]" = "ceci [24]". "ceci" as subject +
  finite modal verb: GRAMMATICAL ("ceci peut [89-inf] ...").
  PARSES (45='ce' is A11 HOLD, allophone tier -- stated, not hidden).
- Under 'faisant': "ce(45) faisant [24]" = absolute "ce faisant" +
  finite verb with no subject. Ungrammatical. FORCES 'faisant' FALSE.

Group 1 score: 'ci' = 1/3 (W3 only); 'faisant' = 0/3.

### Discriminator group 2: '37 01' x3 (37's value open)

W4 @940 (row a5_10): `56 69 26 00 33 21 64 37 01 07 50 40 08 62 98`
= "[56] [69] [26] pour(00) [33] [21] qui(64) [37] [01] [07] [50]
e(40) [08] [62] [98]".
- Under 'ci': "qui [37]-ci [07]" needs 37 nominal in a
  celui-ci-shaped construction. 37's nominal status is ungranted;
  A1 grants predicative frames only, and that grant is under
  red-team re-examination. Conditional orphan.
- Under 'faisant': "qui [37] faisant [07]" = "qui" + noun +
  participle. Ungrammatical without a verb for the "qui"-clause
  (absolute-phrase rescue needs a clause boundary and a main-clause
  subject; none visible). Conditional orphan at best.

W5 @1634 (row a8_03): `56 69 26 00 33 21 64 37 01 74 87 74 74 35 56`
= same byte-identical left 8-gram as W4
("56 69 26 00 33 21 64 37 01"), then "[74] ce(87) [74] [74]".
- Same verdict as W4 under both values: conditional orphan
  (needs nominal-37; 'faisant' additionally blocked by "qui").

W6 @1818 (row a8_10): `61 15 93 50 42 06 29 37 01 02 09 19 00 97 00`
= "[61] [15] [93] [50] [42] [06] er(29) [37] [01] [02] [09]
[19] pour(00) [97] pour(00)".
- Under 'ci': "[06]er [37]-ci [02]" needs nominal-37 in a
  demonstrative construction. Conditional orphan.
- Under 'faisant': "[06]er [37] faisant [02]" = reduced relative
  "[37] doing [02]" ("un homme faisant cela"-shaped). GRAMMATICAL
  IF 37 is nominal. Conditional parse (best 'faisant' window in
  the group, still gated on ungranted nominal-37).

Group 2 score: 'ci' = 0/3 clean (3 conditional on ungranted
nominal-37); 'faisant' = 0/3 clean (1 conditional @1818, 2 blocked).

### Bar's own windows: '87 01' x2, '47 01' x1

- @345: `... 96 43 87 01 06 70 12 94 ...` = "par(96) [43] ce(87)
  [01] [06] pre(70) n(12) ne(94)". "ceci" and "ce faisant" both
  parse at the bigram; the following "[06]" (verb ending 'ent',
  PROMOTE) leaves both strained in full context (stem missing).
  Tie not broken here -- consistent with adverse (a).
- @1029: `... 96 43 87 01 03 29 80 77 11 70 ...` = "par [43] ce
  [01] [03]er [80]-le la(11) pre(70)". Both "ceci" and "ce
  faisant" parse at the bigram; both strained by the following
  "[03]er [80]-le" (infinitive + imperative with no visible
  subject). Tie not broken here either.
- @195: `... 56 47 01 21 60 08 67 ...` = "[56] ce(47) [01] [21]
  [60] [08] et/veut(67)". "ceci [21]" parses at the trigram
  (subject slot); "ce faisant [21]" needs a subject. Soft edge
  to 'ci' at the bigram level only.

### Sweep of the other 19 windows

No window parses cleanly under either general value. Closest
approaches, both fenced: @295 "16 01 11 78 40" = "[16] faisant
la(11) [78]" ("doing the [78]") fails because 78's lead is 'ver'
(ver-78 NULL), not a noun; @596 "79 85 01 29 40" =
"tout(79) [85-stem] [01] er(29) e(40)" fails under both, but
"01-29" = "cier" is a word-internal '-cier' lead (see follow-up 2).
Generous orphan counts: 'ci' orphans >=24/28 (86%); 'faisant'
orphans >=23/28 (82%). Both far above the 10% bar.

## Per-clause pass/fail

1. '01 24' x3 cohere under one value: FAIL for 'ci' (1/3; W1 and W2
   force 'ci' false at kill grade -- "ci" before a finite verb is
   ungrammatical, and the 24 class grant kills the old ci-compound
   rescue). FAIL for 'faisant' (0/3; all three force 'faisant'
   false -- participle + finite verb with no subject).
2. '37 01' x3 cohere under the same value: FAIL for both (0/3 clean;
   every window needs ungranted nominal-37; W4/W5 additionally
   blocked by "qui" under 'faisant').
3. Orphan <=10% under the named value: MOOT -- no value named.
   (For the record: >=82% orphan under either value.)
4. Rival killed/downgraded: both candidates killed at the
   discriminator windows (see clause 1). No value named.
5. Adverses: (a) ANSWERED -- "'ceci' vs 'ce faisant' both
   grammatical" holds at the bigram level at all three ce-windows;
   the tie is NOT broken there (both strained in full context) and
   is broken instead by group 1, which kills both general values.
   (b) ANSWERED -- "37's value open" stands: '[37]-ci' needs
   nominal-37 (ungranted); 37's A1 predicative grant is under
   red-team re-examination (frame-37-reexam NULL) and is not
   decided here.

## Verdict: KILL

Both disjuncts of the claim are killed at the discriminator windows:

- 01 = 'ci' (general token value): KILLED by W1 @40 and W2 @828.
  "ci" before the granted finite verb 24 is ungrammatical; the
  pre-registered ci-compound rescue (ci-dessus/apres/...) is dead
  under the 24 class grant. Kill grade per protocol section 4
  (windows force the claim false).
- 01 = 'faisant' (general token value): KILLED by W1 @40, W2 @828,
  W3 @984. Participle + finite verb with no subject is
  ungrammatical in all three; no subject is recoverable in-window.

Explicitly NOT killed (fenced, narrower, for follow-up):

- "-ci" as a BOUND morpheme in "ceci": 87-01 x2 (@345, @1029),
  47-01 (@195), 45-01-24 (@984, the one clean "ceci [verb]" window).
  The cela = 87-11 structural parallel (le1033-imperative) is
  untouched by this kill; only the GENERAL value is dead.
- Word-internal readings: 37-01 as part of a "-faisant" compound
  adjective (satisfaisant/bienfaisant/malfaisant -- A12's "certain"
  note is the same family of hypothesis) and 01-29 = "-cier"
  (@596) are untested here.

No standing red-team verdict is contradicted: A12 granted 37-01 as
a UNIT (not a value) and is untouched; the le1033 "ceci" parse was
an adverse-answer, not a verdict, and is preserved above as the
fenced bound-morpheme hypothesis; 37's value question stays with
the red team (frame-37-reexam). No escalation needed.

Dependency note: the 'ci' kill is load-bearing on ne-24-profile's
class-level PROMOTE (24 = finite verb). If that grant is ever
overturned, re-open this target.

## Follow-up targets (kills regenerate work too)

1. **ci-bound-01** (priority 2): test "-ci" as a BOUND morpheme
   restricted to ce-contexts: 87-01 x2 (@345, @1029), 47-01 (@195),
   45-01 (@984). Bar: all four windows parse as "ceci" + the
   surrounding clause parses with 01 taking NO value outside
   ce-contexts (positional/bound reading, no general value named);
   kill iff any of the four forces "ceci" false in full context.
2. **wordinternal-37-01** (priority 3): test 37-01 as word-internal:
   "-faisant" compound adjective (satisfaisant / bienfaisant /
   malfaisant) vs "-ci"/"-tain" ending (A12's "certain" note).
   Bar: identify the host word via 37's contact profile; the three
   windows (@940, @1634, @1818) parse with <=10% orphan; coordinate
   with noun-43/frame-37-reexam (37's class decides).
3. **faisant-absolute-01** (priority 3): re-test 01='faisant' ONLY
   as the absolute "ce faisant" at 87-01 x2 + 47-01 x1, with full
   clause parses including subject recovery. Bar: >=2 of the 3
   windows parse as complete "ce faisant, [subject] [verb]"
   clauses; kill the absolute reading iff none does.
