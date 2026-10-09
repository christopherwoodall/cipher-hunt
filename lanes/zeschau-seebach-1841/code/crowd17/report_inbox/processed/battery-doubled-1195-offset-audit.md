# Battery verdict: doubled-1195-offset-audit

## Bar (verbatim, pre-registered)
"resolve iff row a7_00's offset/pairing verifies; a mispaired row dissolves the doubled frame and makes clause 1 testable"

Restated as numbered clauses:
- C1: row a7_00's offset/pairing VERIFIES at battery grade (independent byte evidence).
- C2: else, if the row is shown mispaired, the doubled frame dissolves and clause 1 (of the parent 16-class target) becomes testable.

## Verdict: NULL

Row a7_00's pairing can be neither verified nor falsified at battery grade. The
doubled frame "82 16 96 82 16 64" at 1-based @1195-1200 survives as a
battery-grade object, but it sits on one of the 68 unvalidated row offsets
(the canonicality caveat) — it is not independently anchored.

## Method

Read BATTERY-PROTOCOL.md first. Created `locks/doubled-1195-offset-audit.lock`
on start. Re-derived the repaired stream in-session from
`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`
(1,847 pairs / 96 groups verified; same totals as repair_parse.py).
`canonical.py` never touched. R5005, sealed gates, red-team queue untouched.

## Byte-level audit

Row a7_00 digit string (58 digits):
`7460724821696821664294558474355612165645932489645367783926`

Repaired offset: **1** (identical to upstream's EM choice; the a5_03 1->0 flip
does not touch this row). Row starts at stream index 1191 (0-based).

Under offset=1 (28 pairs):
`46 07 24 82 16 96 82 16 64 29 45 58 47 43 55 61 21 65 64 59 32 48 96 45 36 77 83 92`
The doubled frame "82 16 96 82 16 64" is 1-based @1195-1200, fully inside the row.

Under offset=0 (rival, 29 pairs):
`74 60 72 48 21 69 68 21 66 42 94 55 84 74 35 56 12 16 56 45 93 24 89 64 53 67 78 39 26`
The doubled frame disappears entirely (digit substring "821696821664" re-pairs as
"69 68 21 66 42").

## Why C1 (verify) fails — no independent byte evidence exists

1. **No gloss on a7_00.** The two pencil-gloss anchors are a5_03 (la premiere)
   and a8_05 (46=que). Upstream notes list untied traces ("pour","a","ex","ce",
   "ne") with no row attribution. No full-size manuscript scans exist
   (thumbnails only: data/manuscript/TH_P1..P6.jpg), so no new gloss evidence
   is obtainable.
2. **No crib in the row.** The "117082342940" crib digit string does not occur
   in a7_00's digits.
3. **No formula repeat in the row.** None of upstream's long repeats
   (7778948206 x5, 06777818711001 x3, 2437784 x3, 00866) occurs in a7_00's
   digit string.
4. **Parity cannot decide.** 58 digits is even; both offsets are legal.
5. **No neighbor constraint.** Pairs never span rows in the parse, so adjacent
   rows impose nothing.

## Why C2 (falsify) also fails — the EM choice is locally optimal and clean

Leave-one-out pair-likelihood test (global pair frequencies from the repaired
stream excluding a7_00, add-alpha smoothing over 100 possible pairs):
- offset=1: loglik -123.53
- offset=0: loglik -131.94
- delta: **+8.4 nats in favor of offset=1**

This is the same criterion that chose the offset (circular as *independent*
evidence), but it does confirm the offset is the model's genuine local
optimum, not a configuration artifact. Under offset=1 the row produces no
novel groups (all 28 pairs in 00-99, all previously attested) and no
contradiction with any standing banked/promoted value.

## Standing-state check

No standing verdict contradicted or downgraded. The frame-82-16 and
laisser-gate-16 verdicts (both NULL) stand untouched: their "universal killer"
characterization of the doubled frame is conditional on the pairing, and that
condition is now documented as unvalidated, not as verified. No red-team
verdict on a7_00's offset exists. No polyvalence declared (S7 intact).

## Headline for the red team

The doubled frame at @1195-1200 is a statistical-offset object, not a
byte-anchored one. It cannot be dissolved at battery grade, but it also cannot
be trusted the way gloss-anchored windows are. Any argument that depends on it
(e.g. the finite-verb vs infinitive adjudication for 16) should carry the
canonicality caveat explicitly.

## Follow-ups proposed (for supervisor queuing)

1. `phase-likelihood-row-sweep` (P3) — run the leave-one-out pair-likelihood
   comparison for all 70 rows; if a7_00's +8.4 delta is an outlier (weak
   support vs the row population), flag the offset for red-team review.
2. `letter-boundary-1195` (P3) — once letter values are named inside the frame
   region (16, 64, or neighbors), re-test the phase via letter-level
   composition; a forced letter boundary would break the offset tie.
3. `gloss-hunt-a7-fullscan` (P4) — if full-size manuscript scans ever arrive,
   inspect the a7_00 region for pencil traces anchoring pair phase.
