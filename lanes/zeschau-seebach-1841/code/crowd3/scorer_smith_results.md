# SCORER SMITH ROUND 3 — global-consistency scorer (WO3)

**Verdict: BROKEN-ON-CONTROL (NULL — no real drag run, per the control-first rule)**

Design: for each candidate (group g, cell v), decode ALL occurrences of g
under the anchor table + {g:v}, keep only the bigrams TOUCHING a g-position
(the 1–4 bigrams that discriminate v), and score
fit_i(v) = s_i(v) − mean(background cells in the same window).
support(v) = fraction of informative occurrences with fit>0; rank by
(support, mean_margin). This was the N12 fix: the signal that tied inside one
placement window becomes decisive summed over all occurrences. Syllabifier +
two-tier cell model reused from round 2 (`code/crowd2/scorer_smith.py`).
Anchors: 7 ground truth (11=la 70=pre 82=m 34=i 29=er 40=e 46=que).

## Synthetic control (gate) — three variants, all FAIL

Control design (all variants): tail-1200w Tocqueville t2 → rule+encipher_split
cells → 96-cell inventory → random group mapping, 7 ground-truth anchors pinned
(seed 1841). Test = top-40 non-anchor groups by frequency (kept only if ≥8
informative occurrences). Candidates = all 89 non-anchor inventory cells
(chance top-1 = 0.0112). Worst-tie rank of the planted true value per group.
Pre-registered bar: n_test ≥ 10 AND top-1 ≥ 3× chance AND MRR ≥ 0.30
(the bar round 2 failed: top-1 0.021 < chance 0.076, MRR 0.133 < 0.30).

| variant | change vs previous | n_test (dropped) | top-1 | ×chance | MRR | median sup(true) | median sup(top-1) | verdict |
|---|---|---|---|---|---|---|---|---|
| v1 | baseline WO3 design (W=2, 8 random tier-matched background cells) | 22 (18) | 0.045 | 4.0 | 0.217 | 1.000 | 1.000 | FAIL |
| v2 | strong background (8 most-frequent cells/tier) + W=3 | 22 (18) | 0.091 | 8.1 | 0.165 | 0.823 | 1.000 | FAIL |
| v3 | v2 + SYL candidates scored only on SYL–SYL bigrams (drop lossy tier-crossing) | 14 (26) | 0.071 | 6.4 | 0.217 | 0.964 | 1.000 | FAIL |

Each repair was motivated by a diagnosed flaw in the previous variant, not by
tuning to the numbers — and each re-validation failed the pre-registered bar.

## Diagnosis (the N12-style finding)

The true planted value is CONSISTENT but not DISTINCTIVE. v1 showed median
support(true) = 1.00 — the true cell beats a random background at every
occurrence, so the global-consistency signal is REAL. But many wrong values
are equally consistent, and no aggregation separates them:

1. **Bigram contexts underdetermine the cell.** For single letters, the
   letter-bigram model cannot distinguish the true letter from other common
   letters — common-letter attractors (s, t, d, l) win by frequency. v1 LET
   ranks: [1,2,3,3,5,5,9,9,10,15,28]; v2 with a strong background made it
   worse (median 30): the true letter can't beat other common letters either.
2. **The tier-crossing approximation is lossy for identification.** Scoring a
   SYL candidate next to LET neighbors via edge letters lets single-letter
   impostors matching a true edge win ('s' for true 'les', 't' for true 't…').
   In v1/v2, LET impostors took top-1 for most SYL-tier groups.
3. **Clean-tier scoring starves the data.** v3's SYL–SYL-only bigrams dropped
   26/40 test groups below 8 informative occurrences (7 anchors give too few
   SYL adjacencies); LET-tier still failed (median rank ~14).
4. **The null is unfixable at the bigram level.** Support saturates at 1.0
   under a weak null (v1) and collapses under a strong null (v2, median
   sup(true)=0.82 while impostors hold 1.0). The likelihood P(context|v) is
   not discriminative — no per-occurrence aggregation can fix an
   uninformative likelihood.

The missing ingredient is JOINT inference: single-letter cells are emitted in
split pairs (d|e from "de"), and syllable identity needs syllable-level
neighbors — both require assigning multiple groups simultaneously, not
per-group scoring.

## Real drag: NOT RUN (control failed — WO3 gate)

No part of this scorer was run on R5005. No candidates reported, nothing
promoted.

## v3 per-group control detail (last run)

| group | n | n_info | true | tier | rank | sup(true) | top-1 |
|---|---|---|---|---|---|---|---|
| 57 | 114 | 21 | é | LET | 2 | 1.00 | p |
| 51 | 105 | 99 | d | LET | 12 | 0.83 | des |
| 28 | 90 | 74 | l | LET | 1 | 1.00 | l |
| 39 | 75 | 73 | t | LET | 14 | 1.00 | con |
| 17 | 56 | 51 | r | LET | 3 | 1.00 | des |
| 32 | 36 | 28 | n | LET | 6 | 1.00 | l |
| 09 | 33 | 14 | les | SYL | 7 | 0.93 | s |
| 90 | 25 | 10 | aux | SYL | 46 | 0.00 | s |
| 21 | 22 | 18 | a | LET | 51 | 0.44 | pu |
| 74 | 20 | 8 | à | LET | 42 | 0.25 | ce |
| 73 | 19 | 14 | s | LET | 28 | 1.00 | con |
| 99 | 18 | 10 | g | LET | 35 | 0.80 | con |
| 67 | 17 | 11 | v | LET | 9 | 0.82 | t |
| 98 | 16 | 9 | ma | SYL | 2 | 1.00 | con |

(Full per-occurrence fits in `scorer_smith_results.json` → `v3_rank_detail`.)

## Best next step

Abandon per-group scoring for cell identification. The validated direction is
**joint decipherment**: simulated annealing / EM over the full 96-group
substitution key, maximizing global bigram likelihood under the two-tier cell
model, with the 7 anchors pinned and split-pair structure (letter cells
emitted in adjacent pairs, per the pencil "pre|mi|er") as a structural prior.
Validate any such solver on this same synthetic control (planted-mapping
top-1/MRR vs chance) before touching R5005. The reusable pieces that survive:
`scorer3.ConsistencyScorer` (per-occurrence bigram machinery + API),
the rule syllabifier and two-tier `Scorer` from round 2.

_All numbers trace to `code/crowd3/scorer_smith_results.json` (v1 full detail in
the worker's backup; v2 summary from its run log). 87=ce, 64=qui, 96=par are
provisional lane-inferred anchors — not used in the control (7 ground-truth
anchors only)._
