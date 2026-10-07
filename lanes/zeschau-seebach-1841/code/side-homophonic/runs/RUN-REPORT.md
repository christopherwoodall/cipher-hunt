# RUN-REPORT — Seebach homophonic solver, frozen-code control batch (run2)

**Runner dispatch:** 2026-10-07 (fresh re-dispatch; prior Runner's exec vanished to infra SIGTERM).
**Frozen code md5 (verified before any run):**
- solver.py d30dae03f22f060348ae29cbb7fc5096 ✓
- crib_inventory.py f7c10dff9052d323693fd19c05ad0e29 ✓
- ct_loader.py bc0c9622cc9ff3fec5886c947ddf27ed ✓
- config.json ecea1a49cd6604529e9941699f475179, inventory_mode='crib' ✓
- All other FREEZE.md md5s match the BATCH-TAG-frozen.md5.json record.

**Prior-attempt forensics (important):**
- The killed batch (ctl-184101/184102) ran PRE-FREEZE code: inventory=288 ≠ frozen 291;
  crib_inventory.py differed (old run missed accented by-ear forms).
  run_all_controls.sh passed a removed `--chance` flag (rc=2) for seeds 184103–184106.
  All pre-freeze numbers are VOID as control evidence.
- The NEGATIVE CONTROL is complete and valid (runs/negative-control/):
  negctrl_annealer.py (md5 aae48a4000128de6ea3dfaa7064b3a9e) reuses round-1
  anneal.anneal() + Tocqueville bigram model unchanged, 7 true anchors pinned,
  12 restarts × 60000 iters per instance, modal-vote recovery vs sealed truth.
  mean_primary=0.0412, max=0.0449 vs chance 0.0216±0.0153.
  Verdict: NEGATIVE-CONTROL-OK (≈chance). The dead annealer stays dead on the
  harder control. Deterministic (seeded) — not re-run.

## Per-instance control results (frozen code, one at a time)

### seed 184101 — COMPLETE (rc=0, wall 2326s)
- primary = **0.0000** (0/89) — bar min ≥ 0.10: DEAD
- proj_equiv = 0.0000
- secondary = 0.1473 — bar min ≥ 0.22: DEAD (≈ chance 0.1434)
- mrr = 0.0262, pins_intact = 7/7, islets = 0/6, baseline_margin = +15050.3 nats
- Report: runs/run2-184101/control_report.json

## Diagnosis (instance 184101, post-scoring, sealed truth used for diagnosis only)

**D1 — Objective misalignment (verdict B).** Planted truth scores **-6959.9 nats**
under the solver's own objective; the annealed best scores **+4127.4** — the true
key is 11,087 nats WORSE than a completely wrong key (primary=0.0). The optimizer
works (12/12 restarts converge, huge margins over random); the objective's optimum
is at the wrong place. Not an optimization failure.

**D2 — The word scorer is the hole.** Score parts, annealed best:
S_char=-6222.2, S_word=+11754.5 (S_ac=13510.2 − S_single=1755.7), n_poly=60.
Planted truth: S_char=-7608.6, S_word=+768.1, n_poly=6.
The annealed decode is degenerate pseudo-French
("titdeemenirereiemeprendceemeniremeiiemeprendceemeetereiiimesleursquelqueemeetdtemeniremequeleurscrececemais...")
— repetition of short fragments (eme, menire, mais, leurs, ce). The Aho-Corasick
lexicon scan counts thousands of OVERLAPPING short-word hits on the garbage
(S_ac=13,510), while the true Les Mis decode
("lesidesunchapitreimyrielchapileiimyrielchapitreiii..." — clean French,
crib 11-70-82-34-29-40 reads "la pre m i er e" @287) yields S_ac≈2,500.
The S_word term has no length/normalization penalty for overlapping substring
hits; degenerate repetition of high-weight short fragments outscores real text 15×.
S_single (1755.7) is far too weak a correction. This single term dominates the
objective: S_word contributes +11,754 of the +4,127 total.

**D3 — Polyvalence runaway.** Solver invents n_poly=49–60 secondaries vs truth 6.
The -lambda_poly*n_poly=-1000 penalty is dwarfed by degenerate S_word gains; the
polyvalence E-step machinery is being exploited, not used.

**D4 — Inventory gap (secondary, not the cause).** 6/96 truth primaries are absent
from the 291-item crib inventory: 'vê'×2, 'té', 'né', 'vres', 'my' (accented
by-ear chunks from the generator's ear-noise pipeline). 'vres'/'vre' has no
projection-equivalent either. True primary ceiling ≈ 83/89 = 0.933 even with a
perfect optimizer. proj_equiv=0.0 confirms the failure is not accent-level.

**Repair direction for the Smith (control-only, never R5005):**
(a) Fix S_word: dedupe overlapping hits (longest-match), normalize by stream
length, or gate on minimum matched-word length; (b) retune lambda_poly /
penalize polyvalence by marginal usage; (c) extend Tier 1 with accented by-ear
forms (vê/té/né/vres/my) or normalize accents at inventory build; (d) re-run
control batch on FRESH seeds (per freeze protocol, any patch faces new instances).
