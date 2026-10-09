# Battery verdict: frame-464-fullparse — full-window parse of @464 ("59 42 96 00")

Date: 2026-10-09. Worker: f70191af-67e5-4aee-b245-9da1d2235f03.

## Bar (verbatim from battery-queue.json)

`one grammatical full-window parse with <=1 ungranted assumption, or fence @464 as a 96/00-driven residual`

## Bar restated as numbered clauses (pre-registered before testing)

- C1: produce ONE grammatical full-window parse of the @464 locus ("59 42 96 00", 1-based @464–467, row a2_10, with ±context) under standing values with ≤1 ungranted assumption. PASS iff the whole window parses.
- C2 (else-arm): fence @464 as a 96/00-driven residual with stated cause — the window's unparseability is driven by the independently fenced "96 00" collocation, not by a new local problem.

## Method

Re-derived the full 1,847-pair / 96-type stream from `data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json` (parse per `code/side-keyhunt/repair_parse.py`; asserts re-run: 1,847 pairs, 96 types). `canonical.py` never touched. R5005, sealed gates, red-team adjudication queue untouched. Lock created on start with agent id + UTC timestamp.

Window byte-exact (1-based), row a2_10:

```
461 79 tout | 462 87 ce | 463 11 la | 464 59 est* | 465 42 [42] | 466 96 par |
467 00 pour | 468 33 [33] | 469 79 tout | 470 80 [80] | 471 06 [06] |
472 67 [67] | 473 46 que | 474 84 on | 475 24 [24] | 476 37 [37] | 477 78 [78]
```

## Leg-by-leg parse attempt

- **L1 "tout(79) ce(87) la(11) est(59) [42]"** = "tout cela est [42]" — predicate-noun frame. Standing: 79=tout (A5 granted), 87=ce (granted), 11=la (pencil), 59=est (provisional, standing battery status), 42 noun-class (promoted 2026-10-08). Ungranted assumptions: **0**. PASS.
- **L2 "[42] par(96) pour(00) [33]"** — the seam. "par pour" has no grammatical reading under standing values. Sibling battery `seg-par-pour-96-00` (NULL, fence executed) tested five rescues at all three "96 00" windows (@47/@465/@960) and rejected each at battery grade: (1) ellipsis of par's complement — ungranted; (2) "par" as passive agent attaching left — left elements are not passive participles (42 noun-class); (3) "pour" as the noun "le pour" — needs ungrammatical article ellipsis; (4) clause boundary between 96 and 00 — "par" still complement-less; (5) re-segmentation — groups fixed by the repaired parse. 00="contre" parses all three windows cleanly ("par contre") but was escalated to red team (`contre-00-three-windows` NULL) and killed globally (`contre-00-global-census` KILL); the positional post-96 "contre" reading is red-team venue (`redteam-contre-00` queued P1). At battery grade: **FAIL — inherited fence**.
- **L3 "pour(00) [33] tout(79) [80]"** — purpose infinitive "pour [33-inf] tout [80]". 33 verb-stem (A10), 00=pour (A9 class-level). Grammatical modulo 80's open value. PASS.
- **L4 "[80] [06] [67] que(46) on(84) [24] [37] [78]"** — "et(67) que on [24] [37] [78]" clause continuation. 67=et by the positional rule (follower 46 is not infinitive-shaped). 84=on under conditions C1–C3 (noted, not re-litigated). PASS.

## C1: FAIL — C2: EXECUTED

No grammatical full-window parse exists under standing values. The **only** unparseable seam is the "96 00" collocation, which is an independently fenced systematic residual (3 windows, all within-row, same shape: complement-less "par" + "pour" + verbal element). Everything left and right of the seam parses with zero ungranted assumptions. Per the bar's else-arm, @464 is fenced as a **96/00-driven residual**: its residual status is inherited from the collocation fence, not a new independent problem. 42's right edge is therefore unconstrained by this window beyond the already-known leftward predicate-noun frame ("tout cela est [42]", adopted from `val-42-estframes`).

Fence scope: the @464 window only. The "96 00" collocation itself stays in its standing venues (`par-pour-redteam` queued P2, `redteam-contre-00` queued P1); this verdict preempts neither.

Adverses: none listed.

## Verdict: NULL (fence executed per the bar's else-arm)

No standing verdict contradicted or downgraded. §7 intact (67 sole polyvalence untouched; no polyvalence declared). Canonical-stream caveat stands (row a2_10 offset unvalidated).

## Follow-up targets (null regenerates work; all verified ABSENT from battery-queue.json)

1. `par-42-complement` (P3) — test whether 42's noun value can license a "par"-complement in 1841 diplomatic French, dissolving the seam leftward ("est [42] par …"). Bar: name one 42 value with a battery-grade-attested "par"-complement at this window, else fence the leftward route.
2. `toutesfois-452` (P4) — test "79 17" @452–453 as the adverb "toutesfois" (however, 1841 spelling); cleans the @464 window's left edge. Bar: promote iff it parses @452–453 with zero contradiction on banked neighbors.
3. `locus-464-rerun-gated` (P4) — gated re-run of this bar once the red team adjudicates the "96 00" collocation (`par-pour-redteam` / `redteam-contre-00`); converts the fence to a parse or a kill.

## Bookkeeping

- Report: this file.
- battery-queue.json: `frame-464-fullparse` → status `verdict`, result `null`, date 2026-10-09 (temp-file + rename; own entry only; pre-write assert confirmed queued/verdictless; JSON re-validated after write).
- Lock `locks/frame-464-fullparse.lock`: created on start, deleted on completion.
