# Battery report: le-par-distributional

- Worker: subagent d203bd85-ebff-4ef4-af54-cdeb2ef37950
- Lock created: 2026-10-08T19:19:00Z (no prior lock present)
- Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json +
  data/upstream-ct_R5005.txt, parsed per code/side-keyhunt/repair_parse.py)
- canonical.py was NOT used. R5005 NOT touched.
- Context read before testing: report_inbox/processed/battery-s5-foundation.md.
  This battery does NOT duplicate its kill-grade re-test of @913; it is the
  calibration census s5-foundation proposed as follow-up #2.

## Bar (verbatim, pre-registered before testing)

"scan the stream for other <article-candidate> 96 bigrams (e.g. 77-96 with
77='le' provisional) and calibrate whether the 'le par' violation is
systematic or isolated"

(Copied from the target's `bars` field in battery-queue.json before any
stream read.)

## Bar restated as numbered pass/fail clauses (fixed before testing)

Decomposition of the verbatim bar, no goalposts moved:

- Clause 1 (census completeness): every 96='par' occurrence in the 1,847-pair
  stream located; left-neighbor distribution recorded; article-candidate set
  {37, 77, 11} and determiner-candidates {47, 87, 45} checked exhaustively.
  PASS needs a complete, reproducible census.
- Clause 2 (per-instance classification): each <article-candidate>-96 bigram
  instance classified as ungrammatical-as-article+preposition or
  parsed/fenced, with the parse stated. Anchors used must be banked or
  promoted; provisional dependencies noted where they occur. PASS needs a
  classification for every instance found.
- Clause 3 (calibration): determine whether the @913 violation class recurs.
  PASS needs a verdict the data supports: >=1 additional same-class
  instance => systematic; zero => isolated.

## Method

Parsed the repaired stream exactly like code/side-keyhunt/repair_parse.py
(repaired_offsets.json row offsets + upstream-ct_R5005.txt). Sanity check:
@913=37, @914=96 (row a5_09) reproduces s5-foundation's anchor. @-offsets are
0-based pair indices.

96='par' (promoted) occurs 21 times in the stream, at:
@47, @131, @150, @224, @230, @342, @465, @602, @847, @914, @927, @947,
@952, @960, @998, @1026, @1063, @1196, @1213, @1526, @1786.

Left-neighbor distribution of all 21: 64 x3, 82 x3, 61 x2, 48 x2,
62 x1, 32 x1, 42 x1, 26 x1, 33 x1, 37 x1, 98 x1, 86 x1, 67 x1, 11 x1,
16 x1.

Article/determiner-candidate bigrams (X-96, X in {37,77,11,47,87,45}):
only two in the stream.

## Window-level evidence

### Instance 1 — @913-914: 37-96 (row a5_09)

Anchor instance. Local: `83 59 37 96 09` (@911-@915).
Under the S5 fence (37='le', disputed, red-team territory): "le par" =
article directly governing the preposition "par" (96 promoted).
s5-foundation already established: ungrammatical as article+preposition;
neighbors 83 and 09 (both ungranted) cannot rescue. That re-test is NOT
duplicated here. Classification for the census: same violation class,
anchor = provisional (37='le' is the S5 fence itself).

### Instance 2 — @997-998: 11-96 (row a6_02)

Recurrence of the same class. Full local (@995-@1001):
`60 67 11 96 82 33 00`.
Under banked 11='la' and promoted 96='par': "la par" = article directly
governing preposition "par". French has no article+preposition parse; an
article must head a nominal, and "par ..." is a prepositional phrase.
No rescue available:
- Left neighbor 67: per the standing positional rule, 67="et" here (67="veut"
  iff the follower is infinitive-shaped; 11 is not). "et" cannot repair an
  article+preposition sequence downstream of it.
- Right neighbors: 82='m' (banked), 33 (ungranted), 00='pour' (promoted,
  leg-1 class-level). "par m 33 pour" is a self-contained PP fragment; it
  is well-formed on its own and does not interact with the 11-96 boundary,
  which is where the violation sits.
- No standing unit covers 11-96; 96='par' is promoted and not available
  for re-read; 11='la' is banked.

Named parse: broken article phrase "et la par [PP m 33 pour]".
Ungrammatical. Anchors used: banked 11, promoted 96, promoted 00,
positional rule on 67 only. NO provisional values needed — this instance
carries the same violation class on strictly stronger anchors than @913.

### Absences (calibration negatives)

- 77-96: ZERO. 77 ('le' provisional) occurs 44 times; right-neighbor
  distribution = 78 x7, 84 x7, 86 x5, 81 x4, 76 x3, 44 x2, 89 x2, 82 x2,
  66/60/62/80/06/87/45/03/64/11/83/74 x1 each. 96 never follows 77.
- 47-96, 87-96, 45-96: ZERO each ('ce' determiners never precede 'par').
- 37-96: exactly the one instance (@913); no other 37 precedes 96.
- 11-96: exactly the one instance (@997).

### Out-of-scope context note (not adjudicated)

64='qui' precedes 96 three times (@131, @224, @342-class windows):
"qui par" parses as relative-pronoun + PP adjunct, a different,
grammatical class — not part of this battery's article-candidate scope.
82='m' precedes 96 three times; that is a pronoun+preposition class, also
outside this bar.

## Per-clause results

- Clause 1 (census completeness): PASS. All 21 occurrences of 96 located;
  full left-neighbor distribution recorded; candidate set checked
  exhaustively.
- Clause 2 (per-instance classification): PASS. Both instances classified
  as ungrammatical-as-article+preposition: @913 (provisional-dependent via
  the S5 fence) and @997 (banked/promoted anchors only). No parsed/fenced
  instances; no standing unit covers either bigram.
- Clause 3 (calibration): PASS — systematic. The violation class recurs:
  @997 "la par" is the same article+promoted-preposition violation as @913
  "le par", on strictly stronger (banked+promoted) anchors.

## Adverses

1. single-window datum: ANSWERED. The census widens the datum set from one
   window to two (@913 + @997). The @997 instance is anchored on banked 11
   and promoted 96/00 alone — it does not depend on the disputed S5 fence.

## Verdict: promote

Headline: 'ARTICLE + PROMOTED PREPOSITION' VIOLATION IS SYSTEMATIC —
RECURS AT @997 ON BANKED/PROMOTED ANCHORS.

All three bar clauses pass and the listed adverse is answered. The @913
"le par" pattern is not isolated: @997 "la par" (row a6_02, `60 67 11 96
82 33 00`) is the same violation class, ungrammatical under banked 11='la'
and promoted 96='par', with no neighbor rescue and no covering unit.

SCOPE LIMIT (explicit): this verdict promotes only the distributional
calibration claim — the violation class recurs in the stream. It does NOT
decide S5, does NOT assign any value to 37, does NOT touch the A1
predicative-frame dispute, and does NOT overturn any standing fence. Those
are red-team territory (s5-foundation-r2). The @913 classification above
remains provisional-dependent exactly because of the S5 fence.

## Follow-up targets for the supervisor (null-only section — not applicable)

None. Verdict is promote; the adverse was answered inside this battery.
A natural next step for a future battery (not pre-committed): calibrate the
adjacent 82-'m'+96 pronoun+preposition class the same way.
