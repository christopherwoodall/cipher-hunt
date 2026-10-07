## control-designer: synthetic control for the homophonic solver

- Context: I built the adversarial synthetic control the new homophonic
  solver must pass before touching R5005 — 6 instances × 1846 pairs / 96
  groups, planted keys, Les Mis plaintext, polyvalent islets, phase rhythm,
  ear noise. Design brief: at least as hard as R5005 on every quantifiable
  axis, and harder than the round-1 annealer control (1/88 ≈ chance) and the
  round-3 scorer control (3 variants, all failed) that killed their solvers.

- Decision: (1) Plaintext = Les Mis T1, NOT Tocqueville — the scorer3 control
  used in-distribution Tocqueville-t2 vs a t1+t2 reference, which is easier
  than the real diplomatic-vs-Tocqueville register gap (F10). (2) Phase rhythm
  = diluted global cycle, calibrated to occurrence-phase χ² ∈ [181,320]
  (certified q_cycle=0.5 → pilot 257.0; per-instance 181–272). (3) 6
  polyvalent islets (2× the 3 established real ones). (4) Ear noise at/above
  crowd4's calibrated knobs. (5) Pass bar pre-registered: PRIMARY mean ≥0.20
  / min ≥0.10 (chance 0.0216); SECONDARY mean ≥0.30 / min ≥0.22 (chance
  0.143); both required over all 6 seeds.

- Why: every axis choice is comparative. The 7 anchors are pinned exactly as
  the real cribs (R1 pinned 8 — easier). Homophony is frequency-weighted
  (R1 uniform-random — easier). The phase models I tried first are documented
  in generator.py: positional classes unbalance masses (B→A edge flat at
  1.05× vs 1.47× real); morphological classes give a real rotation but
  Jaccard clustering recovers planted phases at purity ~0.5, making the
  contactor's χ² a coin flip (0–787 across seeds) — so I calibrated the
  occurrence-phase χ² (stable, monotonic in q_cycle) and report the
  unsupervised number with the caveat, rather than cherry-picking lucky
  clusterings. The bar (0.20) is 9.3× chance and 18× the R1 annealer's
  0.011 on an easier control.

- Enlightenment: the contactor's χ²=181.3 is a NOISY DETECTOR, not a clean
  phase measurement — on synthetic with known ground truth, the same
  pipeline reads 0.4–787 while the true rotation sits at 181–272. The real
  181.3 may itself be a lucky clustering (cluster purities unknowable
  without ground truth). Also: uniform-random homophone aliasing, the
  "obvious" generative choice, fragments contact profiles so badly that ALL
  frequent groups collapse into one Jaccard blob (χ²=3.9) — the real
  cipher's visible rotation constrains the aliasing to be contact-coherent,
  which is itself a clue about the real encipherer/key-maker.

- For the report: belongs in the side-homophonic solver section as the
  gating control. Numbers that matter: 6 instances, 1846 pairs / 96 groups
  each; occurrence χ² 181–272 (band [181,320], real 181.3); chance primary
  0.0216±0.0153 / secondary 0.143±0.017 (computed, `chance_baseline.json`);
  bar 0.20/0.10 and 0.30/0.22; oracle ceiling 0.90–0.93. Files:
  `code/side-homophonic/control/` (generator.py, CONTROL-DESIGN.md,
  instances/, chance_baseline.json, calibration.json, build_summary.json).

- Caveats: I did NOT run any key-recovery solver on these instances (per
  work order — Solver Smith builds it, Runner runs it); the "harder than
  prior controls" claim rests on axis-by-axis comparison, not on re-running
  old solvers. Synthetic `er` is rarer than real (corpus limitation);
  anchor coverage 13–17% vs real 11%. The `i`/`e` letter-cell rates differ
  from real (generative cuts ≠ real encipherer's — mirrors F30). The Runner
  must enforce key sealing; the protocol is in CONTROL-DESIGN.md §8. No
  GitHub push (lane-local only, per work order).
