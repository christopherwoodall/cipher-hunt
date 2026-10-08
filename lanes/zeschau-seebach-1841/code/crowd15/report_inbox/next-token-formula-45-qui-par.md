# Battery A11 — formula 45-qui-par-43-ce-01 ×2; 45="ce"?

Date: 2026-10-07. Runner: battery-runner (resumed, round 15).
Stream: repaired 1,847-pair parse recomputed in-session
(`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`,
per `code/side-keyhunt/repair_parse.py`).

Source: finder P4 (next-token-findings-qui.md).
Windows: @341 `31-14-[45-64-96-43-87-01]` and @1025 `92-64-[45-64-96-43-87-01]`
(+ an extra "qui" at 1023: "qui 45 qui par 43 ce").
Formula-grade: identical 6-gram ×2 + shared 45-predecessor + shared
01-successor — same species as "par ce que" ×3. French reading: explicit NULL.

## Pre-registered bar (written BEFORE touching data)

- **45="ce" allophone test:** run contact-similarity 45 vs 87 (the
  {47,87} precedent — now CONFIRMED by A4, so the bar is: complementary
  distribution vs 24 + mirrored "ce"-frames, same as A4's bar).
  - **PROMOTE** 45="ce" (allophone tier) iff A4-grade evidence: 45 follows
    24 ~0× AND ≥2 mirrored "ce"-frames AND zero contradictions.
  - **HOLD** if contact-similar but below the bar (allophone candidate,
    unconfirmed).
  - **KILL** the "45='ce'" hypothesis if 45's distribution contradicts
    (e.g. 45 follows 24 freely, or 45 never takes "ce"-slots).
- **Formula parse:** the 6-gram's French is NOT forced (finder's explicit
  NULL stands). Test 96's verb-stem candidacy cheaply: does 96 take
  verb-like successors elsewhere? If inconclusive, record NULL — do not
  force "parle ce" (the finder noted "parle ce 01" is strained French;
  the strain stays on the record).
- **87-01 "ceci":** 2× corpus-wide — WEAK per the finder. Do not build on it.

## Data

### 45 vs 87 contact comparison

| | n | pre=24 | top preds | top sucs |
|---|---|---|---|---|
| 45 | 22 | **0** | 78×4, 74×3, 76×2, 50×2, 96×2 | 93×3, 64×3, 23×3, 28×2, 13×2 |
| 87 | 32 | **10** | 24×10, 29×3, 96×3 | 11×7, 64×5, 46×3, 01×2, 77×2 |

Complementary distribution holds (0/22 vs 10/32) — 45 fits the
"ce"-after-non-"en" slot exactly as A4's 47 does.

### Mirrored "ce"-frames for 45

- **45-64 "ce qui" ×3** (@314, @340, @1024) — mirrors 87→64 "ce qui" ×5.
- **45-64-59 "ce qui est" @314** (`37-78-45-64-59-32` = "[78] ce qui est
  [32]") — parallels the banked "en ce qui est [32]" (@1774–1778).
  (Extension of the "X qui" frame, not fully independent.)
- No other 87-signature followers: 45→11 = 0, 45→46 = 0, 45→77 = 0.
- Zero windows forcing non-"ce" (45's slots are all "ce"-compatible).

### Adverse: co-occurrence in the formula

45 and 87 co-occur inside the SAME 6-gram ("45-qui-par-43-ce-01" ×2).
Allophones in complementary distribution can co-occur ("ce…ce" happens),
but a formula built on "ce … ce" 4 groups apart with no visible French
is a mild adverse — noted, not a kill.

### 96 verb-stem test (cheap)

96's sucs: 00×3, 87×3, 21×3, 43×2, 45×2, 82×2 — determiner/noun-like,
not verb-like. Round 13's "inconclusive" stands: **NULL confirmed**, not
forced. The finder's "parle ce 01 is strained" stays on the record.

### 87-01 "ceci"

87→01 ×2 corpus-wide. WEAK per the finder — stays weak, unbuilt.

## Verdicts

- **45="ce": HOLD** (allophone candidate, below the promotion bar).
  For: complementary distribution (0/22 vs 10/32) + "45 qui" ×3 mirror +
  "ce qui est" parallel + zero contradictions. Below bar: only ~1.5
  mirrored frame-types (need ≥2), plus the formula-internal co-occurrence
  mild adverse. Do not merge; do not kill. Re-test when 45's n grows or a
  second "ce"-frame appears.
- **Formula French: NULL** (finder's explicit NULL confirmed — the 6-gram
  is formula-grade real, French invisible).
- **96 verb-stem: NULL** (inconclusive stands).
