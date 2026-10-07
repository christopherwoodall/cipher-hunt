# STANDING RULE T7-MANUAL-TILING: never score manual-tiling bearing counts

Origin: F59 (2026-10-07, crowd7/patternist; red-team: GRANTED HOLD/HOLD).
Enforced by: red team, on every claim touching a manual tiling.

## The rule (three clauses)

1. **Never score bearing counts on manual (hand-placed) tilings.** A
   bearing count is structurally determined by the tiling's own degrees of
   freedom, not by the data. Provenance: M1 VOID — the manual
   me|he|met|a|li tiling fits EVERY 78-window whose positions 1–4 carry no
   conflicting hard/islet anchor (verified: all 20 non-bearing 78-windows,
   each as a different common word — me-he-met etc., ×4 chains); the count
   "10 bearing windows" is structural, so it scores presence of nothing.
   Source: `code/crowd7/report_inbox/patternist-16-mehemet.md` (M1).

2. **Per-window nulls only.** A manual drag may be cited only through its
   per-window null — anchor-preserving, N34-style exact test on that
   window's own cells (e.g. T7 "Mehemet-Ali" @8: null = 33/11,870 = 0.28%;
   unaffected by the M1 void). No stream-wide excess test may be built on
   a manual tiling's bearing criterion.

3. **Recount assertion.** Every manual-tiling recount must
   `assert len(cells) == len(groups)` before scoring. Provenance: the T7
   drag's k=6 manual variant (me|h|me|t|a|li) was arity-dead — caught only
   by arity assertion, not by any score.

## Enforcement (red-team procedure)

- A claim whose numeric support is a manual-tiling bearing count is ruled
  VOID (not negative evidence — unscored, un-citable). The red team strips
  the bearing-count leg and re-rules the claim on the per-window null
  alone.
- Corroborating fits of the same manual tiling across other windows are
  "reported, not scored" — they may be logged as context (patternist M4
  pattern) but never as support legs toward promotion.
- A manual drag presented without the len(cells)==len(groups) assertion is
  returned unadjudicated.
- Any new null built on a manual tiling must reproduce the M0 template:
  anchor-preserving per N34, exact count, engine-matched — M0 REPRODUCE
  is a prerequisite, not a leg.

## Non-scope

This rule governs MANUAL tilings only. Machine-generated segmentations
with calibrated nulls (their own preregistered batteries) are unaffected.
