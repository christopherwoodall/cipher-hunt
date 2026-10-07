## search-designer: joint-inference search family — verdict KILL (blocked by objective transfer)

- Context: Round-7 work order 8. N40 flipped the diagnosis to "objective
  correct, search too weak" (C1 PASS on the repaired objective: truth beats
  the annealed best by 0.98 nats) and ordered a different search family for
  joint inference — or an explicit scope-down. Constraints: search lane only
  (no scorer duplication), test ONLY on the side-homophonic control design
  with fresh seeds + the 6-check gate, never R5005. I built 6 fresh instances
  (seeds 184207–184212; occurrence χ² 188–302, all in the certified [181,320]
  band; 1846 pairs, 96 groups, 7 pins, 6 islets each) and verified the
  prerequisite C1-analog before designing any search.
- Decision: **KILL the search-family bake-off; do not adopt a new search.**
  The prototype (island-population SA + alias-block moves + graduated
  λ_word ramp, `code/crowd7/search/prototype.py`) is designed, implemented,
  and banked — but NOT run against the baseline, because the comparison is
  uninformative: on the mandated control family the objective is
  truth-anti-aligned, so "better search" means more confidently wrong keys.
  Scope-down delivered: scope search work to zero until the objective passes
  C1 on this family.
- Why (all numbers trace to lane files):
  - C1-analog FAILS on 3/3 fresh instances (`diagnose.json`, `c1x2.json`):
    184207 truth −3.5269 < random-20 max −3.2998; 184208 truth −3.5818 <
    random-5 max −3.3044; 184209 truth −3.5727 < random-5 max −3.3310.
  - The letter term is register-saturated: the Tocqueville-trained projected
    7-gram scores the true Les Mis projected stream at −3.3521/letter vs
    −3.4427…−3.4486 for char-shuffled noise — truth is **+0.09 nats/letter**
    above pure noise (floor −3.4012). Crib decodes correctly, so this is the
    model, not a harness bug.
  - The word bonus is register-blind too: truth S_word 0.111–0.127 vs random
    keys' max 0.087–0.123 — indistinguishable (`c1x2.json`).
  - The only truth-distinguishing term points AWAY: −LAM_POLY·n_poly = −0.30
    for truth's 6 islets, while letter+word give truth only +0.12 over
    random. The LAM_POLY=0.05 guardrail was calibrated on the in-distribution
    control where the letter advantage (+0.83) covered it.
  - Airtight argmax test: baseline SA on 184207 (3×600 sweeps, frozen config,
    8.1 min) reaches −3.2898 — ABOVE truth — with PRIMARY **0.0112 (1/89)**,
    SECONDARY **0.1148** (below chance 0.1434), proj_equiv 0.0112, islets 0/6
    (`runs/baseline_one/asg-184207.json` scored by `score_fresh.py`).
    The objective's optimum is truth-orthogonal. No search can pass the
    6-check gate (needs primary ≥0.20) against this objective.
  - Boundary of N40: its C1 PASS used the crowd4 control (Tocqueville
    plaintext, IN-DISTRIBUTION for the Tocqueville-trained letter model and
    lexicon). "Objective correct, search too weak" holds there; it does NOT
    transfer to the register-gapped family — which is the faithful one for
    R5005 (1841 diplomatic French is register-gapped from Tocqueville, F10;
    Les Mis preserves the gap deliberately per CONTROL-DESIGN.md §2.1).
- Enlightenment: I came in to fix the search and the first measurement
  killed the premise. The repaired objective's two signal terms are both
  Tocqueville-tuned; the control deliberately gaps the register; the result
  is an objective whose global optimum is fluent nonsense at primary≈0 —
  exactly the failure mode N40's gate ("would confidently return fluent
  nonsense") was built to catch. Two methodology bugs found en route:
  (1) `step6_basin.py` never ran AND has a bug — `anneal()` calls
  `init_key()`, wiping the perturbed-truth start, so it cannot test basins;
  (2) step5's C2/C3 marginals were sampled at T=0.3 for 400 sweeps AFTER the
  best state — the chain wanders off (best_m.components total −5.08 vs
  tracked best −2.41); flat marginals are partly measurement artifact. My
  gate (best-key PRIMARY/SECONDARY) avoids both.
- For the report: belongs in the round-7 joint-inference section. The 1–3
  numbers: truth < random on 3/3 fresh instances (worst gap −0.28 nats);
  baseline argmax primary 1/89, secondary 0.115; letter term +0.09/letter over
  noise. Recommendation: **KILL** (no new search now) → **ITERATE on the
  objective first** (Smith's lane): letter-term backoff/interpolation instead
  of the add-alpha floor, register-robust training/corpus, re-examine
  LAM_POLY on the gapped family; the side-homophonic-rebuild fleet owns the
  word-bonus leg. When C1 passes on this family, run the banked prototype vs
  baseline at equal proposal budget (160,200) — the harness, scorer, and
  fresh instances are ready (`code/crowd7/search/`).
- Caveats: I did NOT run the prototype-vs-baseline bake-off (deliberately —
  see Why). The prototype's block moves + island migration + ramp are
  untested against the baseline; they may still be the right search once the
  objective transfers, but that is unproven. The basin test (`basin.py`) was
  not run — correctly skipped, since PREREG conditions it on C1 holding.
  Concentration calibration transfers fine (truth max_n_c=3, S_conc=0) and
  the 617-cell inventory covers truth fully on 184207 — those Smith-side
  components are not the problem. R5005 untouched throughout.

## Files (all under `code/crowd7/search/`)
- `build_fresh.py` + `fresh/build_summary.json` + `fresh/instances/` — 6 fresh
  in-band instances (seeds 184207–184212); keys sealed (search never reads).
- `harness.py` — repaired-objective loader on fresh instances (frozen
  calibrated hyperparams; prov={}; LAM_ROT=0.0 per frozen config).
- `diagnose.py`/`diagnose.json`, `c1x2.py`/`c1x2.json` — C1-analog evidence.
- `basin.py` — correct basin test (no init_key wipe); not run (C1 fails).
- `baseline.py` — frozen SA replica; `runs/baseline/asg-184207.json`.
- `prototype.py` — BANKED island-population + alias-block-move + λ_word-ramp
  search (equal-budget design: 6×300×89 = 160,200 proposals); not run.
- `score_fresh.py` — exact 6-check gate scorer (PRIMARY/SECONDARY per
  control_harness.py definitions).
