# Battery report: s5-foundation

- Worker: subagent c752bc81-1e2f-4475-950f-93183ebd9148
- Lock created: 2026-10-08T08:08:17Z (no prior lock present)
- Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json +
  data/upstream-ct_R5005.txt, parsed per code/side-keyhunt/repair_parse.py)
- canonical.py was NOT used. R5005 NOT touched.

## Bar (verbatim, pre-registered before testing)

"(a) >=2 of 37's 28 windows where a 'le' reading forces ungrammatical French,
with named parses; (b) the @913 'le par' window re-derived with neighbor
analysis (83, 09); (c) ZERO windows requiring 37='le'"

## Bar restated as numbered pass/fail clauses (fixed before testing)

- Clause A: At least 2 of the 28 windows of 37 admit no grammatical French
  parse when 37 is read as article-'le'. PASS needs >=2 such windows, each with
  a named parse.
- Clause B: The @913 window ("37 96" = "le par" under S5) is re-derived from
  the repaired stream, with the left neighbor 83 and the right neighbor 09
  analyzed for any rescue of the 'le' reading. (Methodological clause.)
- Clause C: No window among the 28 has its grammaticality depend on 37='le'
  (no window is ungrammatical unless 37='le').

## Method

37 occurs at 28 pair-offsets in the repaired stream:
@51, @183, @278, @312, @385, @414, @475, @529, @620, @625, @676, @778, @796,
@885, @913, @939, @1125, @1130, @1179, @1301, @1357, @1444, @1633, @1655,
@1723, @1770, @1797, @1817.

Each window was read with its local neighbors. Only standing grammar was used
as anchors: banked (11=la, 82=m) and promoted (64=qui, 79="tout", 96=par,
47="ce"). Provisional values (59=est, 77="le") are noted where they appear
but the core findings do not depend on them.

## Window-level evidence

### Clause A — windows where 37='le' forces ungrammatical French

1. @51 (row a1_01). Local: `79 37 11 79` = "tout(79) 37 la(11) tout(79)".
   Under 37='le': "tout le la tout". The core "le la" is article followed by
   article (11='la' is banked). French has no article+article parse.
   The promoted 79="tout" on both sides cannot rescue the "le la" collision.
   Named parse: broken NP "tout le la tout". Ungrammatical. (Anchors used:
   banked 11, promoted 79 only.)

2. @1655 (row a8_04). Local: `56 37 11 24 48 47` = "56 37 la(11) 24 48
   ce(47)". Under 37='le': "56 le la 24 48 ce". Same "le la" article+article
   collision (11 banked). Neighbors 56, 24, 48 are ungranted and cannot
   repair an article-article sequence. Named parse: broken NP "le la".
   Ungrammatical. (Anchors used: banked 11, promoted 47 only.)

3. @529 (row a3_00). Local: `59 37 64 26` = "est(59, prov) 37 qui(64) 26".
   Under 37='le': "est le qui 26". "le qui" = determiner directly before the
   relative pronoun 'qui' (64='qui' promoted). French has no
   determiner+relative-pronoun parse. The 59='est' reading (provisional)
   does not affect the "le qui" core. Named parse: broken relative clause
   "le qui". Ungrammatical. (Anchors used: promoted 64 only.)

4. @1357 (row a7_05). Local: `52 37 64 35` = "52 37 qui(64) 35".
   Under 37='le': "52 le qui 35". Same "le qui" violation (64 promoted).
   Named parse: broken NP/relative "le qui". Ungrammatical. (Anchors used:
   promoted 64 only.)

5. @1444 (row a7_09). Local: `59 37 64 77 84 59` = "est(59, prov) 37
   qui(64) le(77, prov) on(84) est(59)". Under 37='le': "est le qui le on
   est". The "le qui" violation holds on promoted 64 alone (the provisional
   77='le' would add a second article, but is not needed for the kill).
   Named parse: broken "est le qui". Ungrammatical. (Anchors used:
   promoted 64, promoted 84.)

Supporting (provisional-dependent, not needed for the bar):
@676 "qui(64) 37 le(77, prov)" -> "qui le le" under 37='le' (double article);
@1179 "est(59, prov) 37 le(77, prov)" -> "est le le".

Clause A result: PASS. Five windows (bar needs >=2), each anchored only on
banked or promoted neighbor values.

### Clause B — @913 re-derived with neighbor analysis (83, 09)

@913 (row a5_09). Full local: `55 83 54 49 64 83 59 37 96 09 02 24 49 74 74`.
Core: `83 59 37 96 09` = "83 est(59, prov) 37 par(96) 09".
Under 37='le': "83 est le par 09". "le par" = article directly governing the
preposition "par" (96='par' promoted). French has no article+preposition
parse: an article must head a nominal, and "par 09" is a prepositional
phrase, not a nominal.

Left neighbor 83: value ungranted (no standing grant, promotion, or kill).
It appears twice in the window ("83 54 49 64 83 59"). No value of 83 can
rescue the "le par" core, because the violation sits at the 37-96 boundary,
downstream of 83.

Right neighbor 09: value ungranted. Standing holds: 09~92 (A6); the "-ere"
value for 09/92 is KILLED (standing). Even under the most favorable
assumption (09 = noun N), "est le par N" stays ungrammatical — the blocker
is "le par", not 09. "par 09" as preposition+complement is well-formed on
its own; the article "le" before "par" is what breaks.

Alternative parses checked and rejected:
- 96 re-read as non-'par': 96='par' is promoted. Not available.
- 37-96 as a standing unit: no unit grant covers 37-96.
- 37 as object-pronoun 'le' rather than article: an object pronoun needs a
  governing verb; the nearest verb-like item is 59='est' (copula,
  provisional), which cannot govern "*est le par 09".

Conclusion for Clause B: re-derived. S5's sole datum for 37='le', read
against the standing promoted grammar, does NOT support 37='le' — the 'le'
reading is ungrammatical at @913 and neither neighbor (83, 09) can rescue
it. 83 and 09 stay ungranted; no values proposed for them here.

### Clause C — survey for windows requiring 37='le'

Pro-'le' candidate classes in the 28 windows:

- 'qui 37' x3 (@676, @939, @1633): @676 is anti-'le' ("qui le le",
  provisional 77). @939 and @1633 are "qui 37 01" — covered by the A12
  37-01 unit frame (value open, 'certain' compatibility, not proof); under
  the unit reading 37 is sub-unit, not standalone 'le'. None requires 'le'.
- 37-78 x4 (@312, @414, @475, @1770): 78 is ungranted. "le 78" is possible
  only if 78 were nominal, but nothing forces that reading. Not requiring.
- 37-01 x3 (@939, @1633, @1817): A12 frame stands untouched (see Adverses).
  Not requiring.
- @913: ungrammatical under 'le' (Clause B). Not requiring.
- est-37 frames x6 (@529, @625, @913, @1179, @1444, @1797): predicative
  frames (A1, value open) admit many values; @529 and @1444 are anti-'le'
  via "le qui". Not requiring.
- Remaining windows (@183, @278, @385, @778, @796, @885, @1125, @1130,
  @1301, @620, @1723, @1770, @1797, @1817): no grammatical parse in any of
  them depends on 37='le'.

Clause C result: PASS. Zero windows require 37='le'.

## Adverses

1. S5 standing fence (37='le' MEDIUM, round-7): NOT answered by this
   battery. The re-derivation above CONTRADICTS it: S5's sole datum (@913)
   fails the 'le' reading under the standing promoted grammar, and five
   windows force ungrammatical French under 37='le' using only banked or
   promoted anchors. Per protocol §5 this contradiction is the verdict
   headline; the fence itself is left for the red team. This battery does
   not overturn S5.
2. A12 37-01 unit grant ('certain' compatibility, not proof): FENCED,
   untouched. The three 37-01 windows (@939, @1633, @1817) were used for
   neither promotion nor kill. The A1 predicative-frame dispute was not
   decided.

## Verdict: null

Headline: EVIDENCE CONTRADICTS S5 STANDING FENCE — ESCALATED TO RED TEAM.
All three bar clauses pass (A: 5 windows, needs >=2; B: @913 re-derived,
'le par' ungrammatical, neighbors 83/09 cannot rescue; C: zero windows
require 37='le'), but the resulting picture contradicts the standing S5
fence (37='le' MEDIUM, round-7). Per protocol §5 and the task constraints,
this battery gathers evidence only: it does not overturn S5, does not
decide the A1 dispute, does not promote any value. The contradiction is
escalated to the red-team adjudication queue. The A12 37-01 unit grant
stands untouched.

## Follow-up targets for the supervisor (null regenerates work)

1. s5-foundation-r2 (for red team): kill-grade re-test of 37='le' restricted
   to the five clean windows (@51, @1655, @529, @1357, @1444). Bar: all five
   ungrammatical under 37='le' using only banked/promoted neighbors
   (11=la, 64=qui, 79="tout", 47="ce"). If accepted, S5 downgrades.
2. le-par-distributional: distributional check of the "article + promoted
   preposition" violation — scan the stream for other <article-candidate> 96
   bigrams (e.g. 77-96 with 77='le' provisional) to calibrate whether the
   @913 "le par" violation is systematic or isolated.
3. qui37-rival-values: rank rival values for 37 in the three 'qui 37' verb
   frames (@676, @939, @1633) against the A8/A3 verb-frame grammar. The A1
   predicative frame is noted as context but NOT decided by this follow-up.
