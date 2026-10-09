# Battery report: ver78-non45-positive-leg — 78='ver' positive legs at non-45 windows

- Target id: `ver78-non45-positive-leg` (battery-queue.json, priority 2, status queued)
- Claim: test 78='ver' at >=1 non-45 window on granted/banked values only (R17-006's settle condition)
- Worker: d2245144-a1d9-4ad3-aab2-223206264190
- Date: 2026-10-09
- Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` +
  `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`;
  1,847 pairs re-derived in-session). `canonical.py` never used. R5005, sealed
  gate instances, red-team adjudication queue untouched.
- Lock: code/crowd17/next-token/locks/ver78-non45-positive-leg.lock (created at
  start, deleted at end). No pre-existing lock was present.

## Offset convention

All @-offsets are **0-based pair indices in the repaired stream** (the
convention of the verdict45-value and fork batteries).

## Bar (verbatim, pre-registered before testing)

"candidates @819 ('47 78 40' 'verre/verte'-shaped), @364 ('47 78 48'); breaks the
78<->45 mutual conditionality from the 78 side"

Numbered pass/fail clauses (frozen before testing, not modified after):

1. @819 ('47 78 40') parses as a 'verre/verte'-shaped composition ("ce verre"
   under 47='ce' A4-granted, 40='e' banked letter, 78='ver' under test) with
   zero hard contradictions, OR the window is fenced with stated cause.
2. @364 ('47 78 48') parses as a ver-shaped composition under standing values
   (47='ce' A4-granted, 48='e' battery-promoted letter per n-e-12-48, 78='ver'
   under test) with zero hard contradictions, OR the window is fenced with
   stated cause.
3. At least one of the two windows yields a positive 78='ver' leg at a non-45
   window on banked/granted values only (78 not 45-adjacent; the leg does not
   touch the 45='dict' lead) — breaking the 78<->45 mutual conditionality from
   the 78 side.

Adverse (from the queue entry, verbatim): "do not promote 78='ver' globally
from this battery -- legs only; R16-005 LEAD grading stands"

## Method

1. Re-derived the repaired stream in-session (1,847 pairs; row offsets from
   `data/upstream-offsets.json` with a5_03=0, byte-exact pairing per
   `repair_parse.py`). Asserted pair count = 1,847.
2. Extracted full row contexts for the candidate windows: row a5_05 (base
   @800, covers @819) and row a2_06 (base @351, covers @364), plus rows a2_04
   (@297), a6_06 (@1105), a7_07 (@1397) for the full '47 78 X' / '78 {40,48}'
   census.
3. Verified 45-proximity: census of 78 windows 45-adjacent on either side, and
   45-presence in rows a2_06 and a5_05.
4. Consistency scan over all five '78 {40,48}' windows and all five '47 78 X'
   windows for kill-grade contradictions (a window forcing 78='ver' false).
5. Standing values used: §7 banked (40='e', 11='la', 70='pre', 82='m', 34='i',
   29='er', 46='que'); granted (47='ce' A4 allophone tier, 87='ce'); 48='e'
   battery-promoted (n-e-12-48, 2026-10-07); 67 et/veut sole true polyvalence
   with positional resolution. 78='ver' is the value under test (R16-005 LEAD);
   45='dict' is an unsettled lead (deliberately not invoked anywhere here).

## Window-level evidence (0-based pair indices, re-derived)

### @819 — "ce verre" (positive leg, banked/granted values only)

Row a5_05 (0-based): `... @816:74 @817:74 @818:47 | @819:78 @820:40 |
@821:95 @822:13 @823:24 @824:87`

Under the standing set:
- @818 = 47 = 'ce' (A4 granted, allophone tier).
- @819 = 78 = 'ver' (value under test; syllable, established from the
  'verdict' analysis).
- @820 = 40 = 'e' (banked pencil letter).
- Composition: "ce" + "ver" + "e" = "ce verre" — demonstrative + masculine
  noun "verre" (glass): a grammatical French NP. The analytic
  syllable+letter composition is the lane's granted mechanism (cf. 'prenne' =
  70-12-94 pre+n+ne, 'ne' = 12-48 letter composition).
- 45-proximity: 78's neighbors are 47/40; row a5_05 contains NO 45 token at
  all (a 44 clitic is present at @800 — distinct token, the clitic-44 census
  subject, not 45). The 45='dict' lead is entirely uninvolved.

Zero contradictions. PASS.

### @364 — "ce ver e" (positive leg, second leg family)

Row a2_06 (0-based): `... @362:76 @363:47 | @364:78 @365:48 |
@366:49 @367:61 @368:70 @369:17 @370:06 ...`

Under the standing set:
- @363 = 47 = 'ce' (A4 granted); @364 = 78 = 'ver' (under test);
  @365 = 48 = 'e' (letter, battery-promoted 2026-10-07 by n-e-12-48,
  verdict "promote" in the queue).
- Composition: "ce ver e" — the same ver+e syllable composition as @819,
  "verre"-family shaped (cf. "ce verre").
- Byte-identical corroboration: the 4-gram '76-47-78-48' occurs TWICE
  (@362–@365 and @1395–@1398 in row a7_07), so this leg is not a singleton.
- 45-proximity: neighbors 47/48; row a2_06 contains NO 45 token at all.
  45='dict' uninvolved.

Zero contradictions. Dependency stated: this leg rides on 48='e', which is
battery-promoted (not red-team ratified). PASS (with stated dependency).

### Consistency scan (kill-grade check)

- All '47 78 X' windows stream-wide: followers 48 x2 (@364, @1397), 40 x1
  (@819), 45 x1 (@982, the known conditional verdict window — not re-litigated
  here), 65 x1 (@1105, 'ce ver [65]' with 65 value-open: neutral, no
  contradiction).
- All '78 {40,48}' windows: @297 ('78 40 97', row a2_04 start: "verre"-shaped
  clause opener, neutral-to-weak-positive, no contradiction), @352 ('67 78
  40': 67 followed by noun-shaped 78 fires the positional 'et' reading —
  "et verre", grammatical conjunction+NP; neutral, no contradiction), @364,
  @819, @1397 (see above).
- 78 windows 45-adjacent on either side: exactly @313, @573, @982, @1164 —
  the four known 78-45 windows. @819 and @364 are not among them.
- Result: ZERO windows force 78='ver' false. No distributional rejection at
  the lane's standard.

## Per-clause pass/fail

1. @819 '47 78 40' "ce verre": **PASS** — parses on strictly banked/granted
   values (47 A4-granted, 40 banked pencil), grammatical NP, no 45 in the
   window or the row, zero contradictions.
2. @364 '47 78 48' "ce ver e": **PASS** — parses under the standing set;
   byte-identical '76-47-78-48' x2 corroboration (@364, @1397); no 45 in the
   window or the row; dependency on 48='e' (n-e-12-48 battery promote)
   stated explicitly.
3. Positive leg at >=1 non-45 window on banked/granted values, breaking the
   78<->45 conditionality from the 78 side: **PASS** — @819 alone satisfies
   it on banked/granted values only; @364/@1397 add a second leg family.

Adverse "do not promote 78='ver' globally from this battery — legs only;
R16-005 LEAD grading stands": **answered by compliance** — this report
promotes only the LEGS. Global 78='ver' promotion is explicitly declined;
R16-005 LEAD grading stands unchanged. The two new positive legs are handed
to the red team as the R17-006 settle-condition contribution ("45='dict'
resolved, or a new positive leg on banked/granted values" — the second arm
is now met at battery grade, pending red-team ratification).

## Verdict

**promote** (legs only, per the adverse — not a global 78='ver' promotion).

## Handoff notes for the supervisor / red team

- R17-006's settle condition ("a new positive leg on banked/granted values")
  is satisfied at battery grade by @819 ('47 78 40' = "ce verre"). Ratification
  of the settle itself is a red-team act.
- Candidate follow-up the supervisor may wish to queue: the '76-47-78-48' x2
  leg family (@364, @1397) as its own leg target once 48='e' is ratified; and
  the row-a2_06 clause context (@364's followers 49-61-70-17-06 = "...pre
  fois [06]") for a clause-level read of the "ce verre" NP's dependents.
  (Suggested, not queued — the supervisor owns the queue.)
- No contradiction with any standing red-team verdict was found; nothing
  escalated beyond the ratification note above.
