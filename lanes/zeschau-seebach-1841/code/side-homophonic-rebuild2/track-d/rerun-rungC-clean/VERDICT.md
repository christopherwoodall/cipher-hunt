# RUNG-C CLEAN RE-RUN — VERDICT: PASS (declared 2026-10-08 ~01:56 UTC)

## Mechanical result
- 126/126 calls verified (108 binding + 18 diagnostic), all integrity checks pass.
- Binding: truth wins per-pair majority on **36/36** truth-vs-salad pairs (bar: ≥35/36).
  Every pair unanimous 3–0 across the three independent judges.
- Diagnostics: paraphrase wins 6/6 truth-vs-paraphrase (expected, non-binding).

## Admissibility
- Red-team audit (REDTEAM-AUDIT.md, independent recomputation): **ADMISSIBLE**,
  9/9 integrity checks pass.
- Confidence-uniformity concern (judge 3's passes 2–3 are copies): assessed —
  does not threaten choice data; every binding pair is truth-unanimous even
  under the strictest independence weighting (7 genuine votes/pair).
- Documentation gap (judge commissioning unattested): closed by
  COORDINATOR-ATTESTATION.md (single coordinator commissioned all 3 judges;
  fresh sessions, brief-only exposure).

## Ladder consequence (PREREG-D-v3-ladder.md §4)
- **RUNG C PASSES → strike one is CLEARED.**
- **The v3C pairwise instrument is ACCEPTED** as the Track D judge instrument.
- Strike two is NOT recorded. The SPS fallback trigger is NOT met.
- Next: step-4 clearance re-requested (see STEP4-CLEARANCE-REQUEST.md).

## What this unlocks
The 2,700-call gate funnel (Branch B: judge-guided ILS from lexicon starts,
cell-space moves, funnel seed package ready) may proceed to red-team
step-4 clearance on prompt-v3C. The memorization re-probe remains the
non-negotiable pre-unsealing prerequisite once the key-holder constructs
the blind paraphrase package.
