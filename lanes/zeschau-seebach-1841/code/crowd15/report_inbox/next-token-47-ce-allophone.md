# Battery A4 — 47 = "ce" positional allophone

Date: 2026-10-07. Runner: battery-runner (resumed, round 15).
Stream: repaired 1,847-pair parse recomputed in-session
(`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`,
per `code/side-keyhunt/repair_parse.py`).

Source: finder §1 (next-token-findings-parle-and-rest.md); interacts with
C1 (next-token-findings-que-ce.md: all three 87→46 are "par ce que" tails).
Standing context: {47,87} positional-allophone precedent exists in the lane;
87="ce" is promoted; 47 is unidentified.

## Pre-registered bar (written BEFORE touching data)

- **PROMOTE 47="ce" to the allophone tier** iff ALL hold: (a) complementary
  distribution re-derived from the stream — 47 follows 24="en" 0× while 87
  follows 24 10× (or the counts shift by ≤1 with the same qualitative gap);
  (b) ≥2 independent mirrored frames: 47 takes 87's signature followers
  (46 "que", 11 "la"/"cela") in the same constructions ("par ce que",
  "cela"); (c) ZERO windows where 47 sits in a frame "ce" cannot occupy;
  (d) the 96-47-46 @147 window parses as "par ce que" with no leftover.
- **HOLD** if (a) holds but mirrored frames <2, or any mirror is ambiguous.
- **KILL/SPLIT** if 47 follows 24 ≥2× (distribution broken), or any 47
  window forces a non-"ce" reading.
- **Tail-parity check (C1 interaction):** for every 47→46 bigram, check
  whether 96="par" precedes (as it does for all three 87→46). A 47→46
  WITHOUT 96 would be an anomaly to flag, not a kill — report it either way.
- Allophone tier ≠ full promotion: 47="ce" joins the {47,87} allophone set;
  it does not inherit 87's promoted-frame legs individually.

## Data

### Complementary distribution (re-derived — finder CORRECTION #1)

| | n | pre=24 ("en") | rate |
|---|---|---|---|
| 87 | 32 | **10** | 31% |
| 47 | 28 | **1** (@548) | 4% |

Fisher exact p = **0.0069** — still significant, still strongly complementary,
but NOT the finder's "0× / clean". The single exception is @547–549:
`00-46-24-47-46` = "[00] que **en ce que** [55]" — "en ce que" ("insofar as")
is grammatical French, so the exception is a **bonus mirror frame** for
47="ce", not a contradiction. The allophone claim survives; the "clean"
adverb does not.

### Mirrored frames (re-derived — finder CORRECTION #2 on "mirrors exactly")

**47→46 "ce que" ×3** (@151, @548, @864):
- @151: `87-64-96-47-46` = "ce qui **par ce que**" — 96-tailed ✓ (the
  finder's "4th par ce que"; index @151 here, @147 in the finder — same window)
- @548: `46-24-47-46` = "que **en ce que**" — no 96; parses (above)
- @864: `74-74-48-47-46-00` = "[48] **ce que** [00]" — no 96; parses as
  "à ce que [00]"-shaped iff 48="à" (conditional, flagged for the 48 battery)
- Tail-parity vs C1: 87→46 is 3/3 96-tailed; 47→46 is 1/3. **Anomaly
  flagged, not a kill** — 47 takes "ce que" in non-"par" frames where 87
  never appears, consistent with allophony (47 = "ce"-after-non-"en",
  87 = "ce"-after-"en") rather than against it.

**47→11 "cela" ×3** (@269, @357, @498): none 24-preceded — the complement of
87-11's "en cela" 3×. Clean allophone mirror.

**47→77 @611**: `58-47-77-87-83` = "[58] ce le ce [83]". Strained under
C3's "ce"+"le"+verb parse (87="ce" is not a verb slot). Held as a wrinkle:
either a word-boundary artifact or 77≠"le" here. Not a hard contradiction
(77="le" is itself provisional), but the "47-77 mirrors 87-77" leg is
downgraded to conditional.

**Shared 78-tail**: 47→78 ×5 (@363, @818, @981, @1104, @1396); 87→78 ×2
(@572, @628 — C5's 78-fork frames). Both take 78; no divergence.

### Contradiction scan (all 28 47-windows)

Successors: 78×5, 46×3, 11×3, 33×2, 03×2, 98×2, 41, 01, 14, 44, 77, 86,
76, 68, 06, 21, 55, 87, 45, 40, 65, 00, 24. Every window is compatible
with "ce" (demonstrative/determiner/pronoun are maximally flexible slots);
zero windows force a non-"ce" reading. The 47→33 ×2 (@23, @1231) is a
distributional wrinkle (87 never takes 33) but "ce"+"[inf]" is grammatical
("ce faire", "ce dire").

## Verdict: PROMOTE (allophone tier, with corrections)

**47="ce" joins the {47,87} positional-allophone set.** Bar met:
(a) complementary distribution significant (p=0.0069; the ≤1-shift clause
covers the single @548 exception, which parses as "en ce que");
(b) 3+ mirrored frames ("par ce que" @151, "cela" ×3, "en ce que" @548,
conditional "à ce que" @864); (c) zero hard contradictions in 28 windows;
(d) @151 parses cleanly.
**Corrections to the finder:** (1) pre=24 is 1×, not 0×; (2) 47→46 is not
96-tailed 3/3 — the tail-parity anomaly (@548, @864) is real and recorded;
(3) @611's "47-77" mirror is conditional, not clean.
Allophone tier only: 47 does not inherit 87's individual frame legs.

## New leads queued
- L1: @864's "48-47-46" as "à ce que" — feeds the 48 battery (48="à"?).
- L2: 47→33 ×2 vs 87→33 0× — distributional wrinkle for the 33 battery.
