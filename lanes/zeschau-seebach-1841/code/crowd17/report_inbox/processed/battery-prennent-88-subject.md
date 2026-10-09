# Battery report: prennent-88-subject — name 88's class for the 'prennent' subject slot

Worker: 6e157c79-0596-4bf7-bd51-97eb748d4302 | 2026-10-09T03:01Z–03:12Z
Target: `prennent-88-subject` (priority 2). Lock
`locks/prennent-88-subject.lock` created on start, deleted on completion. No
prior lock existed.

## Bar (verbatim, pre-registered)

"88 takes a plural subject value making '[88] prennent souvent la...' grammatical at @1117-1123 with <=1 ungranted assumption, or the plural-pronoun arm is killed on 88's distributional profile (n=23; anchors: 'tout [88]' @496, 'est a [88]' @765, '88 le' x3 @86/@646/@1541, 'ne [88]' @1705)"

Numbered clauses (fixed before verdict; bar text unmodified):
- C1 (promote): 88 takes a plural subject value; "[88] prennent souvent la..."
  is grammatical at @1117-1123; total ungranted assumptions <= 1.
- C2 (kill): the plural-pronoun arm is killed on 88's distributional profile
  (n=23) — a profile window forces 88 != plural pronoun under battery
  monovalence (§7: 67 et/veut is the sole true polyvalence; no new
  polyvalence may be declared at battery level).

## Method

Repaired 1,847-pair stream only:
`code/side-keyhunt/repaired_offsets.json` +
`data/upstream-ct_R5005.txt`, parsed per
`code/side-keyhunt/repair_parse.py` (1,847 pairs verified; `canonical.py`
never used). R5005 untouched. @-offsets are 0-indexed pair positions (queue
convention). Standing values used: 11=la (banked), 79=tout (granted A5),
70=pre (banked), 12=n (granted), 06=ent (promoted), 30=pas (promoted),
47=ce (granted). 1841 diplomatic French throughout.

Standing battery correction carried in (not re-litigated): the ent-06
battery refuted "prennent" as spelled — 70-12-06 = "pre"+"n"+"ent" =
"prenent", one 'n' short of "prennent"; it reads "prennent" only under the
unproven clerk single-n spelling (queued `spell-single-consonant`, P3). The
3rd-plural -ent marking itself is not in doubt, so the verb at @1118-1120
still demands a 3rd-plural subject.

Note on anchor offsets: the bar's anchors are bigram starts. Byte-exact:
'tout [88]' @496-497; 'est 39 [88]' with 88 at @766 ("est" at @764, bar says
@765); '88 le' x3 with 88 at @86/@646/@1541 (exact); '94 88' with 88 at
@1706 ("ne" at @1705, bar says @1705). n(88)=23 re-derived — matches the bar.

## Window evidence

Target window, row a6_07 (mid-row, no boundary rescue):
@1114-1123 = `30 69 11 88 70 12 06 14 06 11`
Under standing values: `pas [69] la [88] pre-n-ent [14]-ent la`
= "pas [69] la [88] prennent souvent la ..."

C1 window test: with exactly ONE ungranted assumption — 69-11 = "cela"
(one word; this is precisely what in-flight `cela-69-11-word` tests, so it
is ungranted) — the window reads "Pas cela. Ils prennent souvent la ...",
which is grammatical French with 88 = "ils". The C1 window condition is
therefore satisfiable with <= 1 ungranted assumption. C1's local condition
passes.

Distributional profile test (C2): all 23 windows re-derived; the decisive
anchor is @496-497 on row a2_11 (mid-row):
`... 94 02 79 88 47 11 29 ...` = "[94] [02] tout [88] ce la er ..."
79 = "tout" is GRANTED (A5) — bedrock, not provisional. In French of any
period, including 1841 diplomatic French, no plural pronoun can follow
"tout": "tout ils", "tout elles", "tout eux", "tout ceux", "tout nous",
"tout vous" are all ungrammatical (the demonstrative needs "tous":
"tous ceux"). The only values that survive "tout [88]" are nominal
("tout [noun]", e.g. "tout homme") or adjectival — never pronominal.

Therefore a monovalent 88 = plural pronoun ("ils"/"elles") is forced false
at @496-497. Per §7 no new polyvalence may be declared at battery level, so
88 cannot be "ils" at @1117 and non-pronominal at @496. The plural-pronoun
arm is killed at kill grade: a window forces the claim false.

Other anchors (for the record, none overturn the kill):
- '88 le' x3 (@86/@646/@1541): "[88] le" with 77="le" provisional —
  "ils le" is grammatical (subject + object clitic). This is the strongest
  support the pronoun arm ever had, and it is why the arm was worth testing.
  It does not survive @496.
- 'est 39 [88]' (88 at @766): "est à [88]" — "est à ils" ungrammatical;
  compatible with 88="eux" (disjoint, not a subject) or a noun. Neutral to
  negative for the subject arm.
- '94 88' (88 at @1706): "ne [88]" — particle-"ne" + pronoun is
  ungrammatical, but 94's documented syllabic/word-final duality leaves this
  anchor inconclusive. Not used for the kill.

Adverses: none listed. No standing verdict contradicted or downgraded.
R5005, sealed gates, and the red-team adjudication queue untouched.

## Per-clause verdict

- C1: window-local condition PASS ("Pas cela. Ils prennent souvent la ..."
  with 1 ungranted assumption), but a promote would assert 88="ils" as
  88's value, which C2 refutes globally. C1 cannot carry a promote past C2.
- C2: PASS at kill grade — "tout [88]" @496-497 forces
  88 != plural pronoun under §7 monovalence.

## Verdict: KILL

The plural-pronoun arm for 88 is dead: banked 79="tout" at @496 cannot
precede any plural pronoun, and battery level cannot split 88 into
pronominal and non-pronominal readings. 88's "88 le" x3 frames keep a
plural-NOUN subject reading alive, but that is a different arm (see
follow-ups), not this bar.

## Follow-ups (kill residue — the noun arm survives)

1. `noun-88-subject` (P2): test 88 as a plural NOUN subject at @1117.
   "tout [88]" @496, "est à [88]" @766, and "88 le" x3 are all
   noun-compatible. Bar: name a plural noun value (or noun class with two
   independent frame legs) that parses @1117 "@1114-1123" and @496-497 with
   zero contradiction on banked neighbors; else fence 88's class as open.
2. `tout-88-frame` (P3): characterize the "tout [88]" frame at @496-497 —
   under granted 79="tout", enumerate the classes 88 can take there
   (noun/adjective/adverb) and kill the ones the 23-window profile excludes.
   Constrains all future 88 value claims.
