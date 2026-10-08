# Battery report: s5-foundation-r2

- Worker: subagent 4481bdf7-c6aa-48e8-a724-402bc92a4b0e
- Lock created: 2026-10-08T13:23:30Z (no prior lock present)
- Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json +
  data/upstream-ct_R5005.txt, parsed per code/side-keyhunt/repair_parse.py)
- canonical.py was NOT used. R5005 NOT touched. No invented numbers.

## Bar (verbatim, pre-registered before testing)

"kill-grade re-test restricted to the five clean windows: all five
ungrammatical under 37='le' using only banked/promoted neighbors (11=la,
64=qui, 79='tout', 47='ce'); if accepted, S5 downgrades"

## Bar restated as numbered pass/fail clauses (fixed before testing)

- Clause 1 (@51): the window is ungrammatical under 37='le', anchored only
  on banked 11 and promoted 79.
- Clause 2 (@1655): the window is ungrammatical under 37='le', anchored
  only on banked 11 (promoted 47 in window).
- Clause 3 (@529): the window is ungrammatical under 37='le', anchored only
  on promoted 64.
- Clause 4 (@1357): the window is ungrammatical under 37='le', anchored
  only on promoted 64.
- Clause 5 (@1444): the window is ungrammatical under 37='le', anchored
  only on promoted 64 (84 and provisional 77 present downstream, not
  needed).

## Method

37 has 28 windows in the repaired stream (verified independently):
@51, @183, @278, @312, @385, @414, @475, @529, @620, @625, @676, @778,
@796, @885, @913, @939, @1125, @1130, @1179, @1301, @1357, @1444, @1633,
@1655, @1723, @1770, @1797, @1817.

The five clean windows were re-derived from the repaired parse at the
exact claimed offsets. Standing anchors used: banked 11=la, 82=m, 70=pre,
34=i, 29=er, 40=e, 46=que; promoted 64=qui, 79="tout", 47="ce", 84="on".
No provisional value carries any clause.

## Window-level evidence

### Clause 1 — @51 (row a1_01). Local: `92 79 37 11 79`

`79 37 11 79` = "tout(79) 37 la(11) tout(79)". Under 37='le':
"tout le la tout". The core "le la" is article + article (11='la' banked).
French has no article-article parse. The promoted 79="tout" on both sides
cannot repair an article-article sequence: the violation sits at the
37-11 boundary. The 92 to the left is ungranted and upstream of the core.
Named parse: broken NP "tout le la tout". Ungrammatical.
Clause 1: PASS.

### Clause 2 — @1655 (row a8_04). Local: `01 56 37 11 24`

Core `37 11` = "37 la(11)". Under 37='le': "le la". Same article-article
violation as @51 (11 banked). Neighbors 56 (left), 24, 48, 47 (right,
47="ce" promoted) do not touch the 37-11 boundary: "56 le la 24 48 ce"
stays broken at "le la" whatever values the ungranted neighbors take.
Named parse: broken NP "le la". Ungrammatical.
Clause 2: PASS.

### Clause 3 — @529 (row a3_00). Local: `44 59 37 64 26`

Core `37 64` = "37 qui(64)". Under 37='le': "le qui". The relative
pronoun 'qui' (64='qui' promoted) must follow a nominal; a bare
determiner cannot serve as its antecedent. French has no
determiner+relative-pronoun parse ("*le qui"). The 59 (provisional
'est') and 26 (ungranted) sit outside the 37-64 boundary; no value of
either can repair it. The provisional 59 reading is not used for the
kill. Named parse: broken relative "le qui". Ungrammatical.
Clause 3: PASS.

### Clause 4 — @1357 (row a7_05). Local: `06 52 37 64 35`

Core `37 64` = "37 qui(64)". Under 37='le': "le qui", the same violation
as @529 (64 promoted). Neighbors 52 (left), 35 (right) are ungranted and
do not touch the 37-64 boundary. Named parse: broken NP/relative
"le qui". Ungrammatical.
Clause 4: PASS.

### Clause 5 — @1444 (row a7_09). Local: `68 59 37 64 77`

Core `37 64` = "37 qui(64)". Under 37='le': "le qui", same violation as
@529/@1357 (64 promoted). Downstream items 77 (provisional 'le') and 84
('on' promoted) cannot repair the 37-64 boundary; they are not needed for
the kill. Named parse: broken "le qui". Ungrammatical.
Clause 5: PASS.

### Adversarial check (red-team pass on the re-test)

- "le qui" as interrogative? "*le qui" is ungrammatical in interrogative
  use too; 'le' as object pronoun needs a governing verb, and 'qui'
  cannot follow it. No rescue.
- Could 11='la' or 64='qui' be mis-granted? Both are standing
  (banked/pencil and promoted). Re-granting either is outside this
  battery's scope.
- Offsets verified byte-exact against the repaired parse, not taken on
  trust from the prior report.

## Per-clause pass/fail

Clause 1 (@51): PASS | Clause 2 (@1655): PASS | Clause 3 (@529): PASS |
Clause 4 (@1357): PASS | Clause 5 (@1444): PASS

## Adverses

S5 standing fence (37='le' MEDIUM, round-7): NOT answered at battery
level. This re-test CONFIRMS the contradiction found by s5-foundation:
all five windows are ungrammatical under 37='le' on banked/promoted
anchors only. Per the task constraints this verdict goes to the red
team, not decided here. The A12 37-01 unit grant was not examined.

## Verdict: null

Headline: EVIDENCE CONTRADICTS S5 STANDING FENCE — RE-TEST CONFIRMED,
ESCALATED TO RED TEAM. All five bar clauses pass at kill grade, but the
result contradicts the standing S5 fence (37='le' MEDIUM, round-7). Per
protocol §5 and the task constraints, this battery gathers evidence only:
it does not downgrade S5, does not promote any value, does not decide
the A1 predicative-frame dispute. The S5 downgrade decision belongs to
the red team.

## Follow-up targets for the supervisor (null regenerates work)

1. s5-rival-five-windows: rival value for 37 restricted to the five clean
   windows (@51, @1655, @529, @1357, @1444). Bar: a single value for 37
   that yields a grammatical French parse in all five windows using only
   banked/promoted anchors. Kill-grade if found (the value that survives
   the kill field wins the frame).
2. le-qui-distributional: distributional calibration of the "le qui"
   violation — scan the repaired stream for other <article-candidate> 64
   bigrams (e.g. 77-64 with provisional 77='le'; 87-64 with promoted
   87='ce') to test whether the determiner+relative-pronoun violation is
   systematic or isolated to 37. (Distinct from queued
   le-par-distributional, which covers <article-candidate> 96.)

Note: follow-ups 2 and 3 from the s5-foundation report
(le-par-distributional, qui37-rival-values) are already queued in
battery-queue.json (priority 2); not re-proposed here.
