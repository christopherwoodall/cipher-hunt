# Battery inf-03-91-complement — verdict: NULL (fence executed)

## Bar (verbatim, pre-registered)
"needs 03's verb-stem value plus 91's class; else fence the verb-complement arm there"

Numbered clauses:
- C1: name 03's verb-stem value at the @722 window.
- C2: name 91's class.
- C3 (fence arm): if C1 or C2 fails, fence the verb-complement arm at @722–723 ("91 as complement/object of infinitive-shaped 03").

## Method
Re-derived the repaired 1,847-pair / 96-type stream in-session from
`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`
(parsed like `repair_parse.py`; asserts held: 1,847 pairs, 96 types).
`canonical.py` never used. Locus: row a5_02, @720–@726 =
`80 77 03 91 65 64 11` (64=qui granted, 11=la GT, 77="le" provisional,
80 verb-frame A8). Census of all 20 "03" windows and all 21 "91" windows.

## Findings

**C1 — 03's verb-stem value: FAIL.**
03's value is open; R20 deferred the 03/71 §7 split question, so no
uniform 03 value is namable at battery grade. 03 does have genuine
infinitive-shape legs elsewhere — "03 29" (stem + "er", 29=er GT letter)
at @1030 ("87 01 03 29 80"), @1320 ("15 24 03 29 80"), @1594
("08 81 03 29 80) — but none transfers to @722, where 03 sits in the
"77 03" frame (provisional "le" + 03), a determiner geometry that
disfavors rather than forces a verb-stem reading of 03 at this locus.
"03 91" is a stream hapax (1/1847). No standing license makes 03
infinitive-shaped at @722; assuming it would be a new assumption.

**C2 — 91's class: FAIL.**
n(91)=21. Predecessors scattered: 23×2, 66×2, 16×2, then 15 singletons
(45, 08, 01, 84, 86, 43, 62, 70, 03, ...). Followers equally scattered
(53×2, 65×2, 32×2, 11×2, 67×2, ...). Only 3 determiner predecessors
stream-wide; zero "64 91" windows. No class signature — 91's class is
not namable at battery grade from distribution. (The parallel
noun-91-det-frames battery is testing nominal-91 separately; its result
was not available to and was not used by this battery.)

**C3 — fence arm: FIRES.**
The "91 as complement/object of infinitive-shaped 03" reading at
@722–723 is FENCED at this locus: both premises the bar requires are
unavailable, and the local "77 03" determiner geometry actively
disfavors the verb-03 arm. This fence closes only the @722–723
verb-complement reading; it says nothing about 91's class elsewhere,
nothing about 03's infinitive-shape legs at @1030/@1320/@1594, and
names no value.

## Per-clause result
- C1: FAIL (03's verb-stem value not namable; R20 deferred the 03 split)
- C2: FAIL (91's class not namable; scattered 21-window profile)
- C3: FIRES — arm fenced at @722–723

## Verdict
**NULL — fence executed.** The verb-complement arm at @722–723 is closed.
No standing or red-team verdict contradicted or downgraded; §7 intact.
Canonical-stream caveat stands (row a5_02 offset unvalidated).

## Follow-ups proposed (all verified ABSENT from queue)
1. `val-03-value-census` (P3) — census all 20 "03" windows for a uniform
   verb-stem value; lead with the "03 29"=Xer infinitive-shape legs at
   @1030/@1320/@1594 and test whether the "77 03" windows break uniformity.
2. `seg-77-03-722` (P3) — decide the "77 03" frame at @722 directly:
   nominal-03 ("le [03-N]") vs nominalized infinitive ("le [03-INF]")
   vs word-boundary rival; byte evidence at battery grade.

## Scope
Locus-only fence. Untouched: 91's class/value everywhere else, 03's
value and the deferred 03 split, the "03 29" infinitive-shape legs,
provisional 77="le", 65's class, the "65 64 11" right context.

## Bookkeeping
- Worker: battery worker, 2026-10-09.
- Stream: repaired 1,847-pair parse, asserts held; `canonical.py` unused.
- Lock `inf-03-91-complement.lock` created on start, deleted on completion.
- R5005, sealed gates, red-team adjudication queue untouched.
