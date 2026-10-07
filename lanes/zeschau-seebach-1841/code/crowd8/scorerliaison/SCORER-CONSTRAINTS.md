# Scorer-side constraints for the search designer (WO-8, scorer-liaison lane)

Lane: zeschau-seebach-1841. Status: crowd round 7 complete 2026-10-07; F57
(red-team: GRANTED) killed the search-family bake-off and scoped N40.
**Main-fleet search scope is ZERO until C1 passes on the register-gapped
family.** This memo banks the scorer-side constraints the search designer
builds on once the Smith (side-homophonic-rebuild, objective-repair round 2)
clears the gate. Do NOT duplicate the Smith's track (letter-term
backoff/interpolation, register-robust training, LAM_POLY rescale); bank
what it must deliver.

## 1. Entry gate: C1 on the register-gapped family (mandatory, non-waivable)

- **C1 definition:** truth total > max of **20** random-key totals on **every**
  tested fresh instance. Procedure is banked: `code/crowd7/search/diagnose.py`
  (C1-analog + truth component breakdown, writes `diagnose.json`) and
  `code/crowd7/search/c1x2.py` (multi-instance C1-analog, writes `c1x2.json`).
- **Observed failure the Smith must clear (the bar is in the files):**

  | instance | truth total | random max | gap |
  |---|---|---|---|
  | 184207 | −3.5269 | −3.2998 (n=20) | −0.2271 |
  | 184208 | −3.5818 | −3.3044 (n=5) | −0.2774 |
  | 184209 | −3.5727 | −3.3310 (n=5) | −0.2417 |

  3/3 FAIL; worst gap **−0.28 nats**. Sources: `code/crowd7/search/diagnose.json`,
  `code/crowd7/search/c1x2.json`.
- **Boundary condition on N40:** N40's C1 PASS (truth beats annealed best by
  0.98 nats) held ONLY on the crowd4 control (Tocqueville plaintext), which
  is **in-distribution** for the Tocqueville-trained letter model and
  lexicon. "Objective correct, search too weak" holds there; it does NOT
  transfer to the register-gapped family — which is the faithful one for
  R5005 (1841 diplomatic French is register-gapped from Tocqueville, F10;
  Les Mis preserves the gap deliberately, CONTROL-DESIGN.md §2.1).
- Search designer's move before C1: none. No bake-off, no prototype-vs-baseline
  run, no new search family.

## 2. Diagnosed scorer-side facts (Smith's track — banked here so the search designer does not re-litigate them)

- **Letter term register-saturated:** Tocqueville-trained projected 7-gram
  scores the true Les Mis projected stream at **−3.3521/letter** vs
  char-shuffled noise at −3.4427…−3.4486 (floor −3.4012). Truth sits only
  **+0.09 nats/letter above pure noise**. Crib decodes correctly, so this is
  the model, not a harness bug. Smith repair: backoff/interpolation instead
  of the add-alpha floor; register-robust training/corpus.
- **Word bonus register-blind:** truth S_word **0.111–0.127** vs random keys'
  max **0.087–0.123** — no separation (`c1x2.json`). The side-homophonic-rebuild
  fleet owns the word-bonus leg.
- **LAM_POLY=0.05 is the decisive anti-truth term:** −LAM_POLY·n_poly =
  **−0.30** for truth's 6 islets, while letter+word together give truth only
  **+0.12** over random. LAM_POLY=0.05 was calibrated on the in-distribution
  control where the letter advantage (+0.83) covered it; it does not transfer.
  Smith repair: rescale on the gapped family.
- **Transferring components (do NOT touch, do NOT "repair"):**
  - Concentration penalty: truth max_n_c=3 (cap is 3), S_conc=0 —
    calibration transfers cleanly (`diagnose.json` D2).
  - 617-cell inventory: covers truth primaries fully on 184207 (D3
    missing=0, groups_missing=0).
- **Objective form** (`code/crowd6/scorer/objective.py`, lines 18/223):
  S(K) = S_let_proj + LAM_WORD·S_word + LAM_ROT·S_phase + S_prior
         − LAM_POLY·n_poly + S_conc.
  Frozen harness config: prov={}, LAM_ROT=0.0 (`code/crowd7/search/harness.py`).
  Baseline argmax on the broken objective (3×600 sweeps, 8.1 min) reached
  **−3.2898 — ABOVE truth** — with PRIMARY 0.0112 (1/89), SECONDARY 0.1148
  (below chance 0.1434), islets 0/6 (`code/crowd7/search/runs/baseline_one/asg-184207.json`,
  scored by `score_fresh.py`). The objective's optimum is truth-orthogonal:
  "better search" on it produces more confidently wrong keys.

## 3. What the search designer may assume once C1 holds

- **Banked prototype:** `code/crowd7/search/prototype.py` — island-population
  SA (P=6 islands, 300 sweeps each, T0=2.0, T1=0.02) + alias-block moves
  (block 20%, merge 15%; single/swap/poly/chg2 remainder) + graduated λ_word
  ramp 0→1 over 100 sweeps; migration every 60 sweeps, PERTURB_K=8,
  BASE_SEED=918200. Budget: 6×300×89 = **160,200 proposals**, exactly the
  baseline's 3×600×89 — equal-budget by construction.
- **Prototype is UNRUN (deliberately).** It imports
  `from objective import RepairedModel` — the module must be supplied by the
  Smith's round-2 output on sys.path with the RepairedModel API:
  `total()`, `components()`, `anneal`, `snapshot`/`_move_v1`/`_rescore_group`/
  `sample_cell`, `nonpin`, `pcell`, `PINS`. As of 2026-10-07 the import
  FAILS — do NOT "fix" by re-pointing at the round-6 objective; the point is
  the new objective.
- **Comparison protocol when C1 holds:** run the banked prototype vs the
  frozen baseline (`code/crowd7/search/baseline.py`) at the equal 160,200
  budget; score both with the exact 6-check gate
  (`code/crowd7/search/score_fresh.py`). Adoption requires **PRIMARY ≥ 0.20**.
  Below that = failure (the gate's PRIMARY/SECONDARY definitions come from
  `control_harness.py`).
- **Banked diagnostics:** `basin.py` (correct basin test — the old
  `step6_basin.py` never ran and its `anneal()`→`init_key()` wiped the
  perturbed start, so it could not test basins); the `score_fresh.py` gate
  avoids step5's marginal artifact (chain sampled at T=0.3 for 400 sweeps
  AFTER the best state; best_m total −5.08 vs tracked best −2.41 — flat
  marginals were partly measurement artifact).
- **Hard rules:** never touch R5005; never read sealed keys — the fresh
  instances (seeds 184207–184212; 1846 pairs, 96 groups, 7 pins, 6 islets
  each; occurrence χ² 188–302 in the certified [181,320] band;
  `code/crowd7/search/fresh/instances/`) are diagnostic/sealed — only the
  scorer lane's diagnostic scripts (`diagnose.py`, `c1x2.py`) may read
  `SYNTHETIC-key-*.json`.

## 4. Threshold summary (the numbers the designer checks, not re-derives)

| # | Constraint | Value / threshold | File pointer |
|---|---|---|---|
| C1 | truth > max(random-20 totals), every gapped instance | 3/3 PASS required (currently 3/3 FAIL, worst gap −0.28) | `code/crowd7/search/diagnose.json`, `c1x2.json` |
| L | letter-term truth-vs-noise margin (diagnostic) | +0.09 nats/letter (register-saturated) | `search-family.md` report note |
| W | word-bonus truth vs random-max (diagnostic) | 0.111–0.127 vs 0.087–0.123 (no separation) | `code/crowd7/search/c1x2.json` |
| P | LAM_POLY anti-truth penalty on truth | −0.30 (n_poly=6) vs letter+word +0.12 | `code/crowd7/search/diagnose.json` |
| B | fair search budget | 160,200 proposals (prototype = baseline) | `code/crowd7/search/prototype.py`, `baseline.py` |
| G | 6-check gate for adoption | PRIMARY ≥ 0.20 | `code/crowd7/search/score_fresh.py` |
| S | scope | zero until C1 | F57 |

Full narrative: `code/crowd7/report_inbox/search-family.md` (search-designer
kill verdict, all numbers trace to lane files).
