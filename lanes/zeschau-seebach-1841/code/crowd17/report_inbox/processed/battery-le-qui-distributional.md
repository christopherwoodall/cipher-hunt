# Battery report: le-qui-distributional

- Worker: subagent aa022f3c-5987-4193-9563-f14f0de2b2f7
- Lock created: 2026-10-09T01:19:40Z (no prior lock present)
- Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json +
  data/upstream-ct_R5005.txt, parsed per code/side-keyhunt/repair_parse.py)
- canonical.py was NOT used. R5005 NOT touched.
- Context read before testing: battery-le-par-distributional.md (mirror
  battery on the 96 axis — this battery does NOT duplicate it, and does NOT
  duplicate qui37-rival-values' rival ranking, per the adverses).
- Anchors: 64='qui' promoted; 87='ce' promoted; 45='ce' held (A11);
  11='la' banked; 77='le' provisional. 37='le' is the S5 fence (red-team
  territory) — the three 37-64 anchor windows are NOT re-adjudicated here.
- Canonicality caveat stands (68 of 70 upstream row offsets unvalidated).

## Bar (verbatim, pre-registered before testing)

"resolve iff a census of <article-candidate> 64 bigrams shows the 'le qui'
violation is systematic (not isolated to 37), with counts stated; else
record isolated"

(Copied from the target's `bars` field in battery-queue.json before any
stream read.)

## Bar restated as numbered pass/fail clauses (fixed before testing)

Decomposition of the verbatim bar, no goalposts moved:

- Clause 1 (census completeness): every 64='qui' occurrence in the 1,847-pair
  stream located; left-neighbor distribution recorded; article-candidate set
  {37, 77, 11} and determiner-candidates {47, 87, 45} checked exhaustively.
  PASS needs a complete, reproducible census with counts stated.
- Clause 2 (per-instance classification): each <article-candidate>-64 bigram
  instance classified as ungrammatical-as-article+relative-pronoun or
  parsed/fenced, with the parse stated. Anchors used must be banked or
  promoted; provisional dependencies noted where they occur. PASS needs a
  classification for every instance found.
- Clause 3 (calibration): determine whether the @529/@1357/@1444 "37 64"
  violation class recurs on another article candidate. PASS needs a verdict
  the data supports: >=1 additional same-class instance on a different
  article candidate => systematic; zero => isolated.

## Method

Parsed the repaired stream exactly like code/side-keyhunt/repair_parse.py
(repaired_offsets.json row offsets + upstream-ct_R5005.txt). Sanity check:
1,847 pairs, 96 unique groups, crib "11 70 82 34 29 40" at @754 (a5_03) and
@1034 (a6_03) — the repaired parse reproduces. @-offsets are 0-based pair
indices; reported @-offsets for bigrams denote the FIRST pair of the bigram.

64='qui' occurs 47 times in the stream, at:
@18, @32, @38, @133, @144, @149, @181, @290, @315, @337, @341, @395, @486,
@510, @530, @606, @608, @675, @684, @725, @749, @791, @794, @854, @910,
@938, @1023, @1025, @1079, @1199, @1209, @1226, @1271, @1337, @1341, @1358,
@1434, @1445, @1587, @1632, @1646, @1666, @1717, @1768, @1776, @1801, @1836.

Left-neighbor distribution of all 47: 87 x5, 03 x4, 37 x3, 65 x3, 45 x3,
39 x2, 67 x2, 92 x2, 49 x2, 21 x2, 17 x1, 56 x1, 09 x1, 19 x1, 94 x1,
54 x1, 00 x1, 77 x1, 07 x1, 51 x1, 78 x1, 16 x1, 57 x1, 20 x1, 71 x1,
70 x1, 84 x1, 30 x1, 69 x1.

## Window-level evidence

### Instance class A — 37-64 x3 (anchors, not re-adjudicated)

- @529 (row a3_00): `44 59 37 64 26 32 16` (@527-@533)
- @1357 (row a7_05): `06 52 37 64 35 13 92` (@1355-@1361)
- @1444 (row a7_09): `68 59 37 64 77 84 59` (@1442-@1448)

Under the S5 fence (37='le', disputed) + 64='qui' promoted: "le qui",
ungrammatical as determiner + relative pronoun (s5-foundation-r2).
Classification for the census: violation class, provisional-dependent via
the S5 fence itself. No re-test performed.

### Instance class B — 77-64 x1 (recurrence)

- @790 (row a5_04): local @788-@794 = `84 06 77 64 46 07 64`.

Under provisional 77='le' + promoted 64='qui': "le qui" — the same
determiner+relative-pronoun violation class as class A. No rescue available:
- Left neighbors 84='on' (promoted, A15) and 06 (ungranted): no standing
  unit covers 84-06-77 or 06-77; nothing re-parses the 77-64 boundary.
- Right neighbors 46='que' (banked) and 07 (ungranted): "que" after "qui"
  does not repair an article+relative-pronoun sequence upstream of it.
- No standing unit covers 77-64 (granted frames list has no 77-64 entry).

Classification: same violation class as A, anchor dependency = provisional
77='le' (noted) + promoted 64='qui'. Anchors used: provisional 77,
promoted 64/84, banked 46. This is the recurrence: the class is NOT
confined to the 37 axis.

### Instance class C — 87-64 x5 and 45-64 x3 (parsed, not violation)

- @148 (a1_04): `84 29 87 64 96 47 46`
- @180 (a1_05): `14 24 87 64 23 37 06`
- @1767 (a8_08): `09 24 87 64 26 37 78`
- @1775 (a8_09): `94 24 87 64 59 19 48`
- @1800 (a8_10): `91 79 87 64 77 84 59`
- @314 (a2_04): `37 78 45 64 59 32 94`
- @340 (a2_05): `31 14 45 64 96 43 87`
- @1024 (a6_03): `92 64 45 64 96 43 87`

Under 87='ce' (promoted) / 45='ce' (held, A11) + 64='qui' (promoted):
"ce qui" — grammatical French demonstrative-pronoun + relative pronoun
(e.g. "ce qui est vrai"). These 8 instances are parsed/fenced as a
grammatical class, NOT the violation class. They are the calibration
negative: determiners that take 64 grammatically, proving the violation
class is specific to the article candidates (37/77), not to any X-64 bigram.

### Absences (calibration negatives)

- 11-64: ZERO. 11='la' (banked) never precedes 64. The feminine article
  provides no recurrence.
- 47-64: ZERO. 47='ce' (A4 allophone tier) never precedes 64.
- 77-64: exactly the one instance (@790); no other 77 precedes 64.
- 37-64: exactly the three anchor instances; no other 37 precedes 64.

## Per-clause results

- Clause 1 (census completeness): PASS. All 47 occurrences of 64 located;
  full left-neighbor distribution recorded; candidate set {37,77,11,47,87,45}
  checked exhaustively; counts stated.
- Clause 2 (per-instance classification): PASS. Every instance classified:
  37-64 x3 = violation class (provisional-dependent via S5 fence, not
  re-adjudicated); 77-64 x1 (@790) = same violation class (provisional
  77='le' + promoted 64, no neighbor rescue, no covering unit); 87-64 x5
  and 45-64 x3 = parsed as grammatical "ce qui"; 11-64 x0, 47-64 x0.
- Clause 3 (calibration): PASS — systematic. The violation class recurs at
  @790 "le qui" (row a5_04, `84 06 77 64 46 07 64`) on a different article
  candidate (77), beyond the three 37-axis anchors.

## Adverses

1. "single-value kill already demonstrated at three windows; this is the
   calibration battery — do not duplicate le-par-distributional (96 axis)
   or qui37-rival-values (rival ranking)": ANSWERED. The census widens the
   datum set from the three 37-axis windows to four windows by adding @790
   (77-64). The @790 instance does not depend on the disputed S5 fence
   (its article anchor is the independent provisional 77='le'). The 96
   axis was not re-tested; no rival value for 37 was ranked.

## Verdict: promote

Headline: 'LE QUI' VIOLATION IS SYSTEMATIC — RECURS AT @790 ON THE 77 AXIS.

All three bar clauses pass and the listed adverse is answered. The 37-64
"le qui" pattern is not isolated: @790 "77 64" (row a5_04,
`84 06 77 64 46 07 64`) is the same determiner+relative-pronoun violation
class on a different article candidate, with no neighbor rescue and no
covering unit. The eight "ce qui" instances (87/45 x64) are grammatical
calibration negatives, and 11='la' never takes 64.

SCOPE LIMIT (explicit): this verdict promotes only the distributional
calibration claim — the violation class recurs in the stream. It does NOT
decide S5, does NOT assign any value to 37, does NOT adjudicate 77='le'
(provisional — the @790 classification is conditional on it), and does NOT
overturn any standing fence or red-team verdict. The three 37-64 anchor
classifications remain provisional-dependent exactly because of the S5
fence. A future battery could test whether 77='le' survives its own
distributional check independent of this census.

## Follow-up targets for the supervisor (null-only section — not applicable)

None. Verdict is promote; the adverse was answered inside this battery.
