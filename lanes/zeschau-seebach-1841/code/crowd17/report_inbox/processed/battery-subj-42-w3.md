# Battery report: subj-42-w3 — harden @544's subject

Target: `subj-42-w3`. Claim: 44-29-48 = feminine-plural '-eres' noun ('manieres'/'matieres'-shaped) agreeing with 3pl '[42]ent'. Date: 2026-10-08.
Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` +
`data/upstream-ct_R5005.txt`), parsed like `code/side-keyhunt/repair_parse.py`.
Never used `canonical.py`. R5005 untouched. No invented data.
@-offsets are 1-based. Lock `locks/subj-42-w3.lock` held for this run only.

Dependency: stem-42-verb null (2026-10-08) follow-up #1. W3 @544 is the
strongest verb-class leg for 42 ("[42]ent pour que"). This battery tests the
proposed subject, not the verb reading.

## Bar (verbatim, pre-registered before testing)

"name the subject with agreement, or fence @544's left junction; either way @544's leg is adjudicated clean or conditional"

Numbered clauses (fixed before testing):

1. The subject of "[42]ent" @544 is named with agreement: 44-29-48 parses as
   a feminine-plural '-eres' noun that agrees with the 3pl verb.
2. OR @544's left junction is fenced with stated cause.
3. Either way, @544's verb-class leg is adjudicated clean (if clause 1) or
   conditional (if clause 2).

## Method

Full census of 44 on the repaired stream: 44 n=15. Predecessors and successors
counted. Determiner contacts verified pair by pair: "le 44" = 77-44,
"la 44" = 11-44, "44 pour" = 44-00. The @544 window re-derived with ±40
context (@505-544) to hunt for a plural determiner or clause boundary.
Standing values used: banked 11=la, 29=er, 82=m, 46=que; granted 00=pour,
64=qui, 47=ce; provisional 59=est, 77=le; battery-promoted 12=n, 48=e,
06=ent (pending ratification).

## Window-level evidence (@-offsets, 1-based)

**Target window @541-547** (row a3_01):
`@539 91 @540 12 @541 44 @542 29 @543 48 @544 42 @545 06 @546 00 @547 46`
= "[91] n(12) [44] er(29) e(48) [42] ent(06) pour(00) que(46) ..."

**Subject-candidate span @541-543 = "44-29-48":**
- Spelling layer works: 29='er' banked + 48='e' battery-promoted gives
  "[44]ere". But the 29-48 bigram is a hapax (1x in the whole stream, only
  @542-543), and the 44-29 bigram is also a hapax (only @541-542). The
  '-ere' suffixing is a single-window inference, not a pattern.
- Root gender is tense. "le 44" = 77-44 x2, verified: @208-209
  ("[42]ent le [44] [50]", 44 as direct object) and @1679-1680
  ("[74] le [44] pour que", clean noun + 'pour que' complement frame).
  "la 44" = 11-44 x1, verified: @1070-1071 ("[39] la [44] [74]").
  New finding: 44 takes both masculine and feminine articles.
- The '-ere'-feminine word families (maniere/matiere/lumiere/premiere/
  derniere-shaped) are feminine-only. They cannot host the two clean
  masculine "le [44]" uses. The '-er/-ere' pair families (premier/dernier)
  need '-er' on the masculine form, which is absent at both "le 44"
  windows. The root cannot be named as '-ere'-feminine without
  contradicting standing windows.

**Plural marking:** none found. A feminine-plural subject needs a plural
determiner ('les'/'des'/'ces' shape). Scan of @505-544 (36 pairs) shows no
determiner candidate: @540 = 12 = 'n' letter, @539 = 91. 91 cannot be a
determiner: it precedes articles elsewhere (91-11 x2 @1006/@1669, 91-77 x1
@521), and 'les la' / 'les le' are ungrammatical. A bare '-eres' noun as
subject is ungrammatical in French.

**Noun-shape cross-checks for 44 (support the noun class, not the gender):**
- "44 pour" = 44-00 x3, verified: @1312, @1584, @1680. Matches the
  noun-43/noun-81 "noun + pour [que/INF]" complement frame.
- 44->74 x2 (@1072, @802), 44->83 x2 (@1162, @1841): noun-like followers.
- 42->44 x2 (@1618-1619, @1839-1840): 44 in object slot after 42.

**Left-junction span @528-540** (for the fence):
`44 59 37 64 26 32 16 08 24 82 16 91 12`
= "[44] est(59) [37] qui(64) [26] [32] [16] [08] [24] m(82) [16] [91] n(12)".
No clause boundary is provable in-window; the subject of "[42]ent" cannot
be fixed to any token span with agreement.

## Per-clause pass/fail

- Clause 1 (name the subject with agreement): FAIL. Three blocks: (a) no
  plural determiner anywhere in @505-544, and a bare '-eres' subject is
  ungrammatical; (b) the 44 root carries unresolved gender tension
  ("le 44" x2 vs "la 44" x1), and no '-ere'-feminine word family hosts both;
  (c) the '-ere' suffixing itself is hapax (29-48 x1, 44-29 x1 stream-wide).
- Clause 2 (fence the left junction with stated cause): PASS. Fenced:
  @544's subject is unnameable — no plural determiner in a 36-pair scan,
  gender tension on the 44 root blocks the '-eres' naming, and the only
  other plural-subject candidate in reach ("qui" 64 @531 as relative
  subject) is untested (queued as follow-up, not decided here).
- Clause 3 (leg adjudicated): PASS. @544's verb-class leg stays
  CONDITIONAL — recorded, not forced, per the bar's adverse path.

## Adverses

The bar's adverse ("if no subject names cleanly, @544's leg stays
conditional") is ANSWERED, not ignored: the leg is conditional, the fence
is stated above, and the stem-42-verb null verdict stands unweakened.

## Verdict

**null** — Clause 1 fails. The '44-29-48' = feminine-plural '-eres' subject
hypothesis does not name cleanly: no plural determiner, gender tension on
the 44 root, hapax suffixing. @544's left junction is fenced with stated
cause. @544's "[42]ent pour que" leg stays CONDITIONAL (recorded, not
forced). Not kill: no window forces the subject claim false globally, and
44's noun class is independently supported ('le 44' x2, '44 pour' x3).
No standing red-team verdict is contradicted (42's value is open, the A1
frame grant untouched, 44's value open). Nothing here needs escalation.

## Follow-up targets (null regenerates work; 3 proposed)

1. **det-pl-544** (priority 2): Plural-determiner hunt for @544's subject.
   Sweep the repaired stream for a plural-determiner value candidate; test
   whether 12 @540 can be word-internal ('n[44]ere' one-word parse).
   Bar: name a grammatical plural subject with determiner, or confirm none
   exists in-window.
2. **gender-44** (priority 2): Adjudicate 44's gender. 'le 44' x2 (@209,
   @1680) vs 'la 44' x1 (@1071). Bar: one gender with all three determiner
   windows parsing, or a stated positional rule; gates any future '-ere'
   hypothesis for 44.
3. **subj-42-qui** (priority 3): Rival subject parse. Test 'qui' (64 @531)
   as the 3pl subject of '[42]ent' with the relative clause spanning
   @531-544 ('[44] est [37], qui ... [42]ent pour que ...'), which would
   make 44-29-48 clause-interior rather than the subject. Bar: parse
   @528-550 as one grammatical period with 'qui' as subject, or fence.
