# Battery verdict: 43-1126-1725-joint — joint continuation test of 43='condition' vs 43='mesure'

- Target: `43-1126-1725-joint`
- Claim: the byte-identical NP 'la [52] [37] [43]' (@1122/@1720, 5-gram '06-11-52-37-43' x2) takes 'pour [86-inf]' (@1126) and 'vient à [88]' (@1725); the JOINT continuations discriminate 43's value
- Worker: battery worker 43-1126-1725-joint (05ecc24a-932a-420e-b8bb-bb32e785e813)
- Date: 2026-10-09
- Verdict: **NULL** (else-branch: joint survivor set recorded)

## 1. Bar (verbatim from battery-queue.json)

"test 'condition' vs 'mesure' against both continuations jointly; select iff one value parses both and the other fails at least one at kill grade; else record the joint survivor set"

Numbered clauses:
1. Test 43='condition' against continuation A (43@1126, 00@1127='pour', 86@1128 INF-class) and continuation B (43@1724, 98@1725='vient' battery-grade, 39@1726='à', 88@1727 open).
2. Test 43='mesure' against both continuations.
3. Select one value iff it parses both continuations and the other fails at least one at kill grade; otherwise record the joint survivor set.

## 2. Method

- Stream: repaired 1,847-pair parse only (code/side-keyhunt/repaired_offsets.json + data/upstream-ct_R5005.txt, repair_parse.py tokenization). Verified 1,847 pairs / 96 types. canonical.py never used. R5005, sealed gates, red-team queue untouched. Lock created on start, deleted on completion.
- 0-based @-offsets throughout. The 5-gram '06-11-52-37-43' re-derived byte-identical x2 at pair indices [1122, 1720] (index of the 06):
  - Window 1 (row a6_07): `70@1118 12@1119 06@1120 14@1121 06@1122 11@1123 52@1124 37@1125 43@1126 00@1127 86@1128 52@1129 37@1130 86@1131 24@1132 77@1133`
  - Window 2 (row a8_07): `30@1716 64@1717 47@1718 68@1719 06@1720 11@1721 52@1722 37@1723 43@1724 98@1725 39@1726 88@1727 24@1728 30@1729 15@1730 01@1731`
- Standing values used (protocol §7 + red-team rounds): 11='la' (GT), 06='ent' (R17-007 grant, conditional), 00='pour' (A9), 86 INF-class, 98='vient' (battery-grade, cont98-43-value, zero contradictions), 39='a/à' (allophone tier; forced to 'à' after finite 'vient'), 47='ce' (A4), 64='qui' (granted), 30='pas'.
- Prior batteries adopted, not re-litigated: frame-43-la-52-37 (continuation A narrows 4→2: suite/manière killed, condition/mesure survive), cont98-43-value (continuation B under 98='vient' is "[43] vient à [88]", non-discriminating), noun-43-discriminator (KILL of 43='suite'; input candidate set {condition, mesure}).

## 3. Window-level evidence

### Clause 1 — 43='condition' against both continuations

Continuation A: `[06-ent] la [52] [37] condition pour [86-inf]` (@1126–1128).
"les conditions pour [inf]" / "la condition pour [inf]" is idiomatic 1841 French (prerequisite sense: "remplir les conditions pour partir"). The purpose adjunct "pour [inf]" attaches cleanly to the clause whose object is the NP. PASS.

Continuation B: `la [52] [37] condition vient à [88]` (@1724–1727).
Subject = the feminine NP "la [52-37] condition" (agreement via 11='la' holds); verb 98='vient'; "à [88]" with 39 forced to preposition 'à'. Under the live infinitive-88 hypothesis ("venir à + inf", transition: 'to come to do'), the frame is grammatical; 'condition' as subject is semantically strained (a static requirement undergoing transition) but no grammatical rule bars an abstract subject of "venir à" ("le temps vint à manquer" is good French). Not kill-grade. PASS (strained, not forced false).

### Clause 2 — 43='mesure' against both continuations

Continuation A: `[06-ent] la [52] [37] mesure pour [86-inf]`.
"prendre des mesures pour [inf]" / "la mesure pour [inf]" is idiomatic (peak diplomatic purpose). PASS.

Continuation B: `la [52] [37] mesure vient à [88]`.
Same frame as clause 1: grammatical under the infinitive-88 hypothesis; 'mesure' (a step taken) is equally (un)natural as a "venir à" subject as 'condition' — no idiomatic "mesure + venir à" collocation exists in 1841 French, and none exists for 'condition' either. The strain is symmetric. Not kill-grade. PASS (strained, not forced false).

### Joint assessment

Neither value fails either continuation at kill grade. The byte-identity of the NP adds no new constraint: both candidates are feminine singular nouns, both can head the subject NP of "vient" and the object NP of the "[verb-ent] … pour [inf]" clause, and the 52-37 modifier (value open) agrees with both. The joint requirement therefore does not break the tie that each continuation left individually.

## 4. Per-clause pass/fail

1. **PASS (both continuations parse; B strained).** 'condition' parses A idiomatically and B grammatically-under-open-88.
2. **PASS (both continuations parse; B strained).** 'mesure' parses A idiomatically and B grammatically-under-open-88.
3. **ELSE-BRANCH.** No selection: neither value fails any continuation at kill grade. Joint survivor set: **{condition, mesure}**.

## 5. Adverses answered

1. "52-37 unit value open" — CONFIRMED open (unit-52-37-name NULL). Not load-bearing here: both candidates are feminine, so la-agreement and the adjectival-modifier frame hold identically under either. Fenced with stated cause.
2. "88 value open" — CONFIRMED open (name-88-value KILLed the global naming claim). Continuation B tested under the live infinitive-88 hypothesis ("venir à + inf"); the @1706 finite-88 finding (finite-88-ne null follow-up) is a different window and does not transfer to @1727 at battery level. Fenced with stated cause.
3. "coordinates with (does not duplicate) noun-43-discriminator" — its KILL of 43='suite' and 'manière' adopted as the input set; its frames ('par [43]', '43 pour que', 'la 43') not re-run.

## 6. Caveat (not re-litigated)

@21's class pull ("82-43-29" = "m[V43]er", "mener"/"emmener"-family) threatens the noun premise of BOTH survivors (noun-43-discriminator §adverses). That question is owned by the queued targets `43-29-segment` and `at21-82-43-29-adjudicate`; the joint survivor set {condition, mesure} stands only within the noun hypothesis.

## 7. Verdict: NULL

The bar's selection condition does not fire: both 'condition' and 'mesure' parse both continuations, and neither fails any continuation at kill grade. Joint survivor set recorded: **{condition, mesure}**. No standing verdict contradicted or downgraded. R5005, sealed gates, red-team queue untouched.

## 8. Follow-up targets (null regenerates work)

F1. id: `cond-mesure-43full` | priority: 2
claim: "test 'condition' vs 'mesure' across all 16 of 43's windows; the two-continuation joint test ties, so the full distribution decides"
bars: "select iff one value parses all 16 windows with <=1 fenced residual and the other fails >=1 window at kill grade; else record the full-distribution survivor set"
evidence: "43 n=16 (@21/@43/@244/@258/@343/@386/@439/@563/@1027/@1092/@1126/@1204/@1303/@1305/@1544/@1724); this battery ties on the joint continuations; 'par [43]' x2 and '43 pour que' @1544 untested for condition-vs-mesure"
adverses: "@21's class pull — coordinate with queued 43-29-segment, do not duplicate; 52-37 unit open; 88 open"

F2. id: `venir-a-1841-corpus` | priority: 3
claim: "period-corpus check on 'venir à + inf' subject selection decides whether continuation B is live or strained for abstract subjects"
bars: "in Littré (art. 'venir') and TLFi, record whether 'venir à + inf' takes inanimate abstract subjects in 17th–19th c. French; if unattested, fence continuation B for both survivors with cause; if attested with a selection pattern, re-test condition vs mesure against it"
evidence: "cont98-43-value §3 clause-2; this battery §3: B is the only untested feature, strained symmetrically for both values"
adverses: "corpus attestation is compatibility evidence, not a naming bar; 1841 diplomatic French only"

F3. id: `88-1727-shape` | priority: 2
claim: "88's shape at @1727 specifically decides whether continuation B is live"
bars: "decide 88's shape at @1727 via the '39 88' x3 set (@765 'est à [88]', @1514 'à [81] [88]', @1727 'vient à [88]') with 88's local followers; infinitive-shaped keeps B live for both survivors, otherwise B is fenced for both"
evidence: "name-88-value kill (no global value); '39 88' x3; 88 article followers ('88 77' x3, '88 11' x2); finite-88-ne null (@1706 finite-88 is a different window)"
adverses: "no polyvalence declared at battery level (protocol §7); do not name 88 globally"
