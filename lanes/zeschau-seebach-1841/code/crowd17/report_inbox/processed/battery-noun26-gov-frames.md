# Battery report: noun26-gov-frames

Date: 2026-10-08. Target id: `noun26-gov-frames` (priority 2).
Stream: repaired 1,847-pair parse (`data/upstream-ct_R5005.txt` +
`code/side-keyhunt/repaired_offsets.json`, tokenized exactly like
`code/side-keyhunt/repair_parse.py`; 96 distinct pairs). Never
canonical.py. Never R5005.
Lane @-convention: report @ = 0-based stream index - 1.

## Bar (verbatim, pre-registered)

"(a) @154 '66 84 26' parses ONLY as clause boundary + 'On [26-verb]
[35]' (66 fenced or named; 'on'+noun excluded); (b) @600 '03 39 26 96'
parses as aux+participle ('a [26-part] par [45]') or 'a'+infinitive
(03 named or fenced; 39's 'a/à' allophone tier stated); (c) @841
'62 94 26' parses as '[62] ne [26-verb]' (62's class cited from the
84-adjudication report, not re-derived); (d) @1706 '62 94 88 26'
parses with 88's verb-form profile ('a [88]' x2, '[88] 77=le' x3)
fixing 88 as modal/participle and 26 as infinitive or complement-verb
('ne peut [26]'-shaped; bare-'ne' license cited, not re-proved); (e)
'26n' one-word rival excluded per window or fenced"

## Bar restated as numbered clauses

1. @154: "66 84 26" admits only the parse [clause boundary] + "On
   [26-verb] [35]". 66 is fenced or named. The "on"+noun reading is
   excluded.
2. @600: "03 39 26 96" parses either as aux + past participle ("a
   [26-part] par [45]") or as "à" + infinitive. 03 is named or fenced.
   39's "a/à" allophone tier is stated.
3. @841: "62 94 26" parses as "[62] ne [26-verb]". 62's class is cited
   from the 84-adjudication/collision-62-84 battery, not re-derived.
4. @1706: "62 94 88 26" parses with 88's verb-form profile ("a [88]"
   x2, "[88] 77='le'" x3): 88 fixed as modal/participle, 26 as
   infinitive or complement-verb ("ne peut [26]"-shaped). Bare-"ne"
   license cited, not re-proved.
5. The "26n" one-word rival (12="n" promoted letter) is excluded per
   window or fenced.

## Method

Re-built the stream from the two primary sources with the repair
script's byte-exact tokenizer (offset flip a5_03 1->0, 1,847 pairs).
Re-derived all four windows by content match; ran full censuses of
66 (n=19), 03 (n=20), 39 (n=13), 88 (n=23), 62 (n=35) for
naming/fencing support. Cited the standing verdicts: battery
`collision-62-84` (processed) for 62's class; queued `ne-alone-02-74`
for bare-"ne" licensing; A15 grant for 84="on"; banked 46="que",
94="ne" (promoted), 96="par" (granted), 77="le" (provisional),
45="ce" (A11). Checked no standing value exists for 66 or 03 (none on
record; both fenced).

## Window-level evidence

### @154 — row a1_04. Stream: `96 47 46 [66]@152 84@153 26@154 35 58 35`

Left: 47="ce" (A4 allophone tier), 46="que" (banked) -> "ce que [66]"
is a complete subordinate clause; the parse posits the clause boundary
between 66 and 84, exactly as the bar requires. Right: 84="on" (A15
grant) as subject pronoun of a new clause -> "On [26-verb] [35]".
"66 84" occurs 2x stream-wide (@152, @1149); at @1149 "66 84 02 00"
the follower 02 likewise sits in the verb slot after "on" --
independent consistency. "on"+noun excluded: "on" is a subject pronoun;
a bare noun cannot follow it in any 1840s register. 66: no standing
value, n=19, clause-final slot after "que" -- FENCED (value open, not
needed for the 26 verdict). No rival parse of the trigram survives:
boundary-before-84 with 26 clause-initial would leave "On." bare
("on" with no verb), ungrammatical.

### @600 — row a4_00. Stream: `29 40 [03]@598 39@599 26@600 96@601 45 93`

39 = "a/à" allophone tier (finder standing input). Parse (i) "a":
"[03] a [26-part] par [45=ce]" = aux + past participle + par-phrase
(96="par" granted). Parse (ii) "à": "[03] à [26-inf]", with
"96 45 93" = "par [45] [93]" opening the next phrase. Both allophones
put 26 in verb-form (participle or infinitive). 03: no standing value,
n=20, clause-initial element -- FENCED (its value is irrelevant to
26's class). No rival parse makes 26 a noun: under "a" a noun cannot
follow the auxiliary; under "à" a noun cannot follow the preposition
in this slot.

### @841 — row a5_06. Stream: `17 98 [20]@838 62@839 94@840 26@841 12 16 00`

62's class cited from battery `collision-62-84` (processed, verdict
KILL): 62="on" unconditioned ELIMINATED by the §7 polyvalence rule
against the A15 grant; 62="il" DEMONSTRATED as the rival (not
promoted). That battery's own reading of this window: "20 62 94 26
12" = "[20] il ne [26] n..." Clean. Under 62="il": "il ne [26-verb]".
Under a conditioned 62="on": "on ne [26-verb]". Both rivals force
26 verb-form. Not re-litigated here.

### @1706 — row a8_06. Stream: `[20]@1702 62@1703 94@1704 88@1705 26@1706 12 06 29`

88's verb-form profile re-derived on the repaired stream: "39 88" x2
(@763, @1725) = "a [88]" (aux + participle); "88 77" x3 (@85, @645,
@1540) = "[88] [77='le']" (verb + object clitic "le", provisional).
88 is verb-class (modal or participle) with value OPEN (profiled, not
named). "[62] ne [88] [26]" = "ne [modal] [inf]"-shaped ("ne peut
[26]"); 26 is infinitive or complement-verb. Bare-"ne" license cited
to queued `ne-alone-02-74`, not re-proved. The collision battery reads
this window "[20] il ne [88]..." Clean. No rival parse makes 26 a noun:
"ne" + verb + bare noun is ungrammatical (a modal takes an
infinitive; a participle cannot sit bare under "ne" in a finite
clause).

### Clause 5 — "26n" rival, per window

- @154: 26 followed by 35 (no 12 adjacency) -- excluded by contact.
- @600: 26 followed by 96 (no 12 adjacency) -- excluded by contact.
- @841: "26 12 16" -- contact-live, but "94 [26n]" = "ne [noun]" is
  ungrammatical; "ne" must precede a verb -- excluded by window.
- @1706: "26 12 06" -- contact-live, but "62 94 88 [26n]" puts a bare
  noun after a verb-form 88 under "ne"; a modal takes an infinitive,
  and "ne [participle] [noun]" is ungrammatical -- excluded by window.

## Per-clause pass/fail

1. @154 "66 84 26": PASS. Boundary + "On [26-verb] [35]" is the only
   surviving parse; 66 fenced (value open, clause-final after "que");
   "on"+noun excluded by subject-pronoun grammar.
2. @600 "03 39 26 96": PASS. Both "a/à" allophone parses give
   verb-form (participle or infinitive); 03 fenced; 39 tier stated.
3. @841 "62 94 26": PASS. "[62] ne [26-verb]" under either 62 rival;
   62's class cited from battery-collision-62-84 (KILL on 62="on"
   unconditioned; 62="il" demonstrated, not promoted), not re-derived.
4. @1706 "62 94 88 26": PASS. 88's profile re-derived ("39 88" x2,
   "88 77" x3) fixes 88 as modal/participle; 26 infinitive or
   complement-verb ("ne peut [26]"-shaped); bare-"ne" license cited to
   `ne-alone-02-74`.
5. "26n" rival: PASS. Excluded by contact at @154/@600, by "ne"-window
   grammar at @841/@1706.

## Adverses

- One window per governor: ANSWERED. The claim is convergence of three
  INDEPENDENT governors (subject pronoun, aux/prep, negation particle),
  each independently forcing verb-form; frequency is not the bar.
- 39's allophone tier: ANSWERED -- both allophones handled in clause 2.
- 62="il" rival: CITED (collision-62-84 verdict), not re-litigated.
- 88's value open: PROFILED, not named.

## Verdict

**PROMOTE.** All five bar clauses pass on the repaired stream and every
listed adverse is answered (re-parsed cleanly or cited, never ignored).
Three independent governors (84="on", 39="a/à", 94="ne") plus the
"ne [88] [26]" verb-chain converge on verb-form for 26 in these four
windows. This does NOT grant 26=verb globally -- the "la [26]" noun
legs (@239, @128) and the @1559 crux belong to battery `noun26-la-frames`
(T4), which must answer this verdict; a standing "noun-26" verdict is
not touched (none exists). No red-team contradiction: no standing
red-team verdict constrains these windows.
