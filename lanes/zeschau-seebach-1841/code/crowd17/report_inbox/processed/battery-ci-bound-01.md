# Battery report: ci-bound-01

- Target id: `ci-bound-01`
- Claim: "`-ci` as bound morpheme restricted to ce-contexts (87-01 x2, 47-01, 45-01-24)"
- Date: 2026-10-08
- Worker: battery worker (session 0c4e7de0-1036-45fc-b7d3-2e1a06da02b8)
- Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json +
  data/upstream-ct_R5005.txt, parsed per code/side-keyhunt/repair_parse.py).
  All @-offsets are 0-based repaired-stream indices of the 01 token. n(01) = 28.
- Lock: code/crowd17/next-token/locks/ci-bound-01.lock (created at start,
  deleted at end; no prior lock existed).

## Bar (verbatim, pre-registered before testing)

"all four windows (87-01 x2, 47-01, 45-01-24) parse as 'ceci' with 01 valueless elsewhere"

Numbered pass/fail clauses (restated before testing, not modified after):

1. Each of the four ce-context windows parses as "ceci" in full context:
   87-01 @345, 87-01 @1029, 47-01 @195, 45-01 @984.
2. 01 is valueless outside the four ce-contexts: none of the other 24
   windows of 01 forces a token value on 01 (word-internal syllable and
   A12-unit readings do not name a token value).
3. Adverses answered: (a) "01 must stay valueless outside the ce-contexts";
   (b) "45='ce' is a HOLD (A11)" -- the @984 leg's dependency is stated,
   not hidden.

Ce-context census re-derived on the repaired stream (exhaustive):
87-01 x2 (@344, @1028), 47-01 x1 (@194), 45-01 x1 (@983).
Indices are the left token; 01 sits at +1 (@345, @1029, @195, @984).
Counts match the ci-01-value battery exactly. No other ce+01 bigram exists.

## Method

1. Recomputed the repaired parse in-session (1,847 pairs, 96 groups).
   Never used canonical.py. R5005 not touched.
2. Enumerated all 28 windows of 01 with +-8 context; verified the
   four ce-contexts are exhaustive (bigram census above).
3. Tested each ce-context window for a grammatical full-context parse
   under the "ceci" reading (87='ce' granted; 47='ce' granted A4
   allophone tier; 45='ce' A11 HOLD allophone tier), against standing
   values: 24 = finite verb modal-shaped (ne-24-profile PROMOTE),
   06 = 'ent' verb ending (ent-06 PROMOTE), 94 = 'ne' (battery-promoted),
   30 = 'pas' (battery-promoted), 70 = 'pre' / 82 = 'm' / 34 = 'i'
   (banked GT).
4. Swept the other 24 windows for any that forces a token value on 01.
5. Checked for contradictions with standing red-team verdicts
   (A11, A12, ver-78 NULL, fork-78-45 NULL, le1033-imperative NULL).

## Window-level evidence

### The four ce-context windows (clause 1)

W1 @984 (row a6_01): `01 00 92 07 76 47 78 45 01 24 89 48 01 76 49 24 26`
= "[01] pour(00) [92] [07] le(77) ce(47) [78] ce(45) [01] [24]
[89] [48] [01] le(77) [49] [24] [26]".
- Under the bound-morpheme reading: "ce(45)-ci [01]" = "ceci",
  then "[24]" = finite modal verb, "[89]" infinitive-shaped:
  "ceci [modal] [89-inf] ..." = "ceci peut [inf] ...". GRAMMATICAL.
  The one clean "ceci [verb]" window, as the brief states.
- Dependency (adverse b): the reading needs 45='ce', which is the
  A11 HOLD (allophone tier), not a promotion. Stated, not hidden.
- Watch item, not a contradiction: fork-78-45-adjudication clause (a)
  says IF 78='ver' promotes, 45='dict' applies at the four 78-45
  windows including this one (@982-983). ver-78 is NULL (not promoted),
  dict-45 is NULL (not promoted); the antecedent is false, so A11
  stands here. If ver-78 ever promotes, this leg must be re-examined.
  Result: PASS (conditional on A11).

W2 @195 (row a2_00): `16 00 66 24 87 98 56 47 01 21 60 08 67 76 87 11 92`
= "[16] pour(00) [66] [24]verb ce(87) [98] [56] ce(47) [01] [21]
[60] [08] et/veut(67) [76] ce(87) la(11) [92]".
- Under the bound-morpheme reading: "ce(47)-ci" = "ceci" as subject,
  "[21]" in the verb slot: "ceci [21] [60] [08] et/veut ...".
  [21]'s value is open, so the clause cannot be fully verified, but
  nothing contradicts it: the subject slot is available and
  grammatical. The rival "ce faisant [21]" is dead (01='faisant'
  killed generally by the ci-01-value battery), so "ceci" is the
  only available reading at the bigram.
  Result: PROVISIONAL PASS (bigram/trigram clean; full clause gated
  on [21]'s class, which is open).

W3 @345 (row a2_05): `64 31 14 45 64 96 43 87 01 06 70 12 94 74 67 78 40`
= "[64]qui [31] [14] ce(45) qui(64) par(96) [43] ce(87) [01]
[06]ent pre(70) n(12) ne(94) [74] et/veut(67) [78] e(40)".
- Under the bound-morpheme reading: "par [43] ceci [06-ent] ...".
  [06] = 'ent' verb ending (ent-06 PROMOTE) with NO stem between 01
  and 06. "ceci" followed by a bare verb ending is ungrammatical;
  no clause boundary can rescue it ([06] cannot start a clause).
  The '-ment' adverb fork for 06 does not help either ("ceci [adv]"
  still needs a verb). Note "06-70-12-94" = "entreprenne"
  (ent-06 battery leg): "... ce [01] entreprenne ..." -- "ceci"
  + subjunctive with no "que" is ungrammatical.
- Crucially, the breakage is NOT -ci-specific: the window is
  unparseable under every reading (any subject + bare 'ent' ending
  fails identically). It does not force "ceci" false specifically;
  it is a 06-driven residual.
- This analysis is load-bearing on ent-06's PROMOTE; if that grant
  is overturned, @345 re-opens.
  Result: FAIL as a "ceci" parse; FENCED as 06-driven residual
  (follow-up 2).

W4 @1029 (row a6_03): `84 92 64 45 64 96 43 87 01 03 29 80 77 11 70 82 34`
= "on(84) [92] qui(64) ce(45) qui(64) par(96) [43] ce(87) [01]
[03] er(29) [80] le(77) la(11) pre(70) m(82) i(34)".
- Under the bound-morpheme reading: "par [43] ceci [03]er [80]-le
  la pre-mi..." = "ceci" + infinitive [03]er + imperative [80]-le
  ("[80]-le" per the imp-80-set lead: '80-77' imperative+enclitic).
  "ceci" followed by a bare infinitive is ungrammatical
  (object-before-infinitive is the wrong order; no governing verb;
  the exclamatory-infinitive reading needs "[inf] ceci" order).
- Again not -ci-specific: the window is unparseable under every
  reading (infinitive + imperative with no visible subject). This is
  the same region le1033-imperative left NULL ("'87 01' = 'ce [01]'
  currently unparsed"). Fenced as a 03/80-driven residual.
  Result: FAIL as a "ceci" parse; FENCED as 03/80-driven residual
  (follow-up 3).

Clause 1 score: 1 clean pass (@984), 1 provisional (@195),
2 fenced residuals (@345, @1029). The bar's "all four parse" is NOT met.

### The other 24 windows (clause 2: 01 valueless elsewhere)

Sweep result: no window forces a token value on 01. Per-window notes
(context = +-8 around 01):

- @34 "32 01 08": no parse; no forced value.
- @40 "41 01 24": orphan under all values (ci-01-value W1); no forced value.
- @255 "66 01 91": no parse; no forced value.
- @295 "16 01 11": "[16] [01] la" -- no clean parse (ci-01-value
  fenced the 'faisant' attempt on 78's 'ver' lead); no forced value.
- @327 "10 01 19": no parse; no forced value.
- @409 "33 01 02": "[33] [01] [02]" -- no parse under the
  dire/[X]er set; no forced value.
- @484 "30 01 19": "pas [01] [19]" -- no clean parse under standing
  values; inventing an adjective value for 01 is not licensed.
  No forced value.
- @596 "85 01 29": "tout [85-stem] [01] er(29) e(40)" -- the "-cier"
  word-internal lead (fenced in ci-01-value). Syllable-level, not a
  token value. Consistent with valueless.
- @717 "86 01 02" and @949 "86 01 77": "[86] [01] ..." -- INF-class
  86; no clean parse; a word-internal "86-01" syllable reading is
  conceivable but untested and names no token value. No forced value.
- @828 "82 01 24": "m' [01] [24]" -- orphan (ci-01-value W2);
  no forced value.
- @893 "76 01 98" and @970 "76 01 98": no parse; no forced value.
- @940 "37 01 07", @1634 "37 01 74", @1818 "37 01 02": the A12 UNIT
  grant (37-01 as a unit, not a value). 01 carries no independent
  token value inside the unit. Consistent with valueless.
  Watch item: wordinternal-37-01 (queued) tests "-faisant" compound
  vs "-ci"/"-tain" ending; a "-ci" ending outcome there would extend
  bound -ci beyond ce-contexts and would need red-team eyes. Not
  decided; no contradiction now.
- @976 "08 01 00": "[08] [01] pour" -- no parse; no forced value.
- @988 "48 01 76": "[48] [01] le" -- no clean parse (48 = 'e' letter
  or verb-stem, both leave "[01] le" unparsed); no forced value.
- @1255 "46 01 61": "que [01] [61]" -- no parse; no forced value.
- @1261 "88 01 09": no parse; no forced value.
- @1440 "85 01 52": "[85-stem] [01] [52]" -- no parse; no forced value.
- @1462 "17 01 21": "fois [01] [21]" -- no clean parse; no forced value.
- @1653 "16 01 56": no parse; no forced value.
- @1731 "15 01 56": no parse; no forced value.

Clause 2: PASS. 01 takes no token value in any of the 24 non-ce
windows; the only structured readings (A12 unit, "-cier" syllable
lead) are sub-token and name no value.

## Per-clause pass/fail

1. All four ce-windows parse as "ceci" in full context: FAIL.
   @984 passes clean; @195 provisionally (gated on open [21]);
   @345 and @1029 do not parse -- but both are fenced as
   neighbor-driven residuals (06 bare 'ent' ending; 03-infinitive +
   80-imperative), not -ci-specific refutations. Neither window is
   grammatical under any reading, so neither forces "ceci" false
   specifically. By the parent battery's kill standard ("kill iff
   any of the four forces 'ceci' false in full context"), this is
   not kill-grade: the bar's "all four" is unmet, but the claim is
   under-evidenced rather than refuted. (Precedent: ce-45-mirror2
   NULL -- "bar needs >=2 frame-types, has ~1.5".)
2. 01 valueless outside the ce-contexts: PASS (24-window sweep; no
   forced value; A12 unit and syllable leads are sub-token).
3. Adverses: (a) ANSWERED -- clause-2 sweep shows 01 valueless
   outside the four ce-contexts. (b) ANSWERED -- @984's "ceci"
   parse is conditional on the A11 HOLD (45='ce', allophone tier);
   stated explicitly, with the fork-78-45/ver-78 watch item flagged
   (if ver-78 ever promotes, the @984 leg must be re-examined per
   fork clause (a); currently vacuous).

## Verdict: NULL

The bound-morpheme reading survives at @984 (clean "ceci [verb]")
and is compatible at @195, with 01 valueless everywhere else --
but the bar as pre-registered ("all four windows parse as 'ceci'")
is not met: @345 and @1029 are neighbor-driven residuals that do
not parse in full context. The failures are not -ci-specific, so
this is not a kill; the evidence is mixed, so this is not a promote.

No standing red-team verdict is contradicted: A11 (45='ce' HOLD)
is relied on, not challenged; A12 (37-01 unit) is preserved;
ver-78 NULL, fork-78-45 NULL, dict-45 NULL, and le1033-imperative
NULL are all consistent with the findings above (the @1029 strain
matches le1033's "'87 01' currently unparsed" adverse). No escalation
needed, but two watch items are flagged for the red team:
(i) wordinternal-37-01 could extend bound -ci beyond ce-contexts
if its "-ci"-ending arm lands; (ii) a future ver-78 promotion
threatens the @984 leg via fork-78-45 clause (a).

Dependencies: @345's residual-fencing is load-bearing on ent-06's
PROMOTE (06='ent'); @984's leg is load-bearing on the A11 HOLD.
If either is overturned, re-open this target.

## Follow-up targets (nulls regenerate work)

1. **ceci-984-195-pair** (priority 2): narrow the bound-morpheme
   claim to the two surviving loci. Bar: @984 AND @195 both parse
   as "ceci" in full context once [21]'s class resolves at @195;
   promote the restricted reading ("-ci bound, ce-contexts only,
   confirmed at 2 loci") iff both parse; kill the narrowed claim
   iff @195 forces "ceci" false once [21] resolves. Adverses: A11
   dependency at @984; fork-78-45 watch item.
2. **residual-345-06** (priority 3): resolve @345's "87 01 06 70 12 94".
   Bar: produce a full-context parse of "ce [01] entreprenne [74]..."
   (is "entreprenne" the verb with an elided "que"? can "ceci"/"ce"
   serve as its subject?); if the window parses with "ceci" intact,
   re-test ci-bound-01's clause 1; else fence @345 as a 06-driven
   residual with stated cause (not a -ci residual). Adverses:
   load-bearing on ent-06's PROMOTE.
3. **residual-1029-infinitive** (priority 3): resolve @1029's
   "ceci [03]er [80]-le". Bar: parse in full context once 03's class
   resolves (coordinate with queued imp-80-set and stem-03); test the
   exclamatory-infinitive reading against the word-order problem and
   the word-internal "01-03" lead; fence as a 03/80-driven residual
   with stated cause if unparseable. Adverses: 03 open, 80's mood open
   (red-team act per §7).
