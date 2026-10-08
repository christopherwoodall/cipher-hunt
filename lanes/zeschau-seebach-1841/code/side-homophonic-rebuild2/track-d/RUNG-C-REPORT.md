# Track D — Rung-C trial report (prompt-v3C, pairwise forced-choice)

> **EVIDENCE STATUS: WITHDRAWN — see INCIDENT-COLLISION-20261007.md.** The 36/36 result below was
> computed on data from a mid-trial filesystem collision with a second coordinator running an
> overlapping trial on the same directory (packages/key/logs rewritten 23:50–23:56Z; unauthorized
> RUNGC-REREGISTRATION.md / RUNGC-REPORT.md / rungC-schedules.json). Neither trial's evidence is
> certifiable. RUNG C is VOID and must be re-run cleanly under a single designated coordinator.
> The v3C pairwise DESIGN remains promising (both coordinators' data point the same way) but no
> trial evidence is admissible.

**Status:** trial VOID by collision. Red-team audits R18/R19 document the incident.
**Date:** 2026-10-07.

## Result: RUNG C PASSES — 36/36 truth-vs-salad pairs won by truth

- **Binding bar:** truth wins the per-pair majority (≥2/3 passes) on **36/36** pairs (bar: ≥35/36). **PASS.**
- **Diagnostic (non-binding):** paraphrase beats truth **6/6** bouts — as expected (clean French contains more identifiable French; the memorization worry is moot under blind forced choice).
- 126 records (42 pairs × 3 position-randomized passes), 0 VOID records, sha pins on all records.
- Position randomization: all 42 pairs had both labels presented first at least once across the 3 passes. No position-bias signal (winners identical regardless of order).
- Confidence: median 82, range 62–100 — judges were discriminating, not coin-flipping.
- Unanimity: 42/42 pairs decided 3/3 (consistent with deterministic judges; the choice did not depend on presentation order).

## Why it worked where A and B failed

Rungs A and B both required cold judges to place "degraded truth" and "clever salad" into absolute
bands on a 0–100 scale. Rung A compressed the margin (truth 62–68 vs salad 44–51); rung B made placement
judge-dependent (bimodal truth at ~20 vs ~55). Rung C never asks "how French" — only "which contains MORE
French," ties forbidden. The discriminative signal judges had already been reporting in prose
(truth: phrases like "la partie de la vie"; salad: isolated repeated tokens, "dominated by the repeated
word leurs") is inherently comparative, and forced choice queries it directly. The absolute scale was the
blocker in both failed rungs; removing it removed the failure.

## Strike accounting

Per PREREG-D-v3-ladder §0/§4: rung A FAILED (0/6, formally declared R16a), rung B's numbers are
WITHDRAWN under evidence-breach investigation (INCIDENT-RUNGB-20261007.md; R18 adjudication pending —
verdict direction FAIL is robust across both data versions), rung C PASSES. **Strike two is NOT met:**
the ladder's SPS trigger (condition (b): "no viable judge instrument after two substrate attempts")
requires all three rungs to fail. Rung C's pass means a viable judge instrument exists.

**Recommended next step:** accept the v3C pairwise instrument (pending R19 audit), re-register it as the
Branch-B funnel's judge (prompt_registry.json currently pins the forbidden v2 prompt — re-registration +
red-team clearance required before the instrument is used), and request step-4 clearance on the accepted
instrument per the ladder (§4: "If PASS → strike one is cleared, the instrument is accepted, and step-4
clearance is re-requested").

## Campaign artifacts (checksummed at receipt, before scoring)

- Logs: `instrument-acceptance-v3c/judge-log-rungC-agent{1,2,3}.jsonl` (42 records each, v3c-logger-pin.md schema)
- Packages: `instrument-acceptance-v3c/rungC-pkg-{1,2,3}.json` (14 pairs each: 12 binding + 2 diagnostic)
- Key: `instrument-acceptance-v3c/_KEY_V3C_DO_NOT_OPEN.json` (opened only for scoring, after all logs complete)
- Preserved copies + md5sums: `instrument-acceptance-v3c/EVIDENCE-PRESERVED-20261007/` (scoring ran on these copies)

## Builder-report discrepancy (documentation defect, not integrity defect)

The rung-C package builder's report claimed "18 fresh labels, one per candidate, stable across pairs" with
a mapping table; the disk has **84 fresh labels (2 per pair, unique per pair-slot)** and different label
values. The disk is fully self-consistent (verified by coordinator: 84/84 labels in key, 0 text mismatches
against candidates.json, 36/36 TS cross-product coverage, 6/6 within-seed TP bouts, key written after
packages). Per-pair unique labels are strictly better for blindness (prevents cross-pair candidate tracking).
Red team: audit the disk files, not the builder's table. This is the same builder-report staleness pattern
seen in rung B; future builders must have their reports mechanically cross-checked against disk before
judges are spawned.
