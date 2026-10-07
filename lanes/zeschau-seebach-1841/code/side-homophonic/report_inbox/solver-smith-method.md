# Solver-Smith method note — Seebach homophonic joint-inference solver

## Context

R5005 (Zeschau→Seebach, 18 Jan 1841): French two-digit syllabary, **1,847 pairs**
(F32 repaired parse; was 1,846), 96 groups, 7 hard anchors, established
polyvalence, by-ear spelling, 3-phase contact rhythm. Round-1 (syllable annealer,
1/88 on control) and scorer3 (3× broken on control) both failed for the same
diagnosed reason: **no joint inference over the full key**. My brief: build the
joint-inference solver, validate it on the Control Designer's synthetic control,
never run on R5005.

Deliverable lives in `code/side-homophonic/solver/`:
`solver.py` (SA engine), `phonetics.py` (projection π), `build_lm.py`
(Tocqueville LM), `phase.py` (contact analysis), `control_harness.py`
(load_synthetic → run → score → gate_6instance), `ct_loader.py` (real-data
adapter, F32 repaired parse), `crib_inventory.py` (crib-derived inventory),
`config.json`, `METHOD.md` (full justification), `README.md`.

## Decision

**Simulated annealing over the full key**, not EM or Gibbs.

## Why

- The posterior is multimodal and discrete (96 groups × ~300 values, many-to-one
  + polyvalent v2). SA with restarts explores it; EM climbs to the nearest
  mode (fatal here — see below); Gibbs mixes too slowly across the
  96-dimensional coupling.
- The objective decomposes **exactly per move**: char-5-gram (local in t),
  spanning-only word bonus (windowed Aho-Corasick deltas), contact Potts
  (sparse adjacency), soft priors, polyvalence penalty, concentration penalty.
  No suffix rescoring, no approximations. `--self-test` proves incremental ==
  full recompute (max err 1.7e-10 over 300 random moves).
- It avoids the round-1 failure modes structurally: the round-1 annealer died
  because its syllable-bigram LM was uninformative (letters inexpressible);
  mine scores a **phoneticized char-5-gram** (letters project to phonetic
  classes) plus a word bonus, with restarts beating random by +16,000 nats.
- Polyvalence is explicit (v1 + optional per-occurrence v2 with hard E-step,
  20-nat prior against spurious splits); the 7 pins are never moved; phase
  rhythm enters as a gated contact Potts prior (gate from unsupervised χ²;
  DEMOTE-1: the gate is a noisy detector, OFF on 4/6 control instances —
  the Jaccard contact proposals are the validated machinery).

## Enlightenment

Three degenerate attractors found and killed by the pilot:

1. **Empty-projection exploit.** `project('st')` returned `''` (silent-final
   regex deleted the whole consonant cluster); empty scores exactly 0, better
   than any real text. The annealer mapped 80/89 groups → 'st'. Fix: silent
   finals delete **after vowels only**, plus never-empty guard.
2. **Frequent-word salad.** The char-5gram **genuinely preferred**
   frequent-word salad (−3.89/pair) to true Les Mis decode (−4.44/pair).
   Fix: word bonus is **spanning-only** — only words assembled from 2+ values
   count.
3. **Repetition exploit.** Mapping 50+ groups to 'me' so 'me'+'me'="meme"
   (spanning!) hits the lexicon at every position (+10,178 nats). Fix:
   **concentration penalty** −λ_conc·Σ max(0, n_p−6)² over PROJECTED values.

## For the report

- The solver is **control-ready**: `control_harness.py` implements §4
  (`load_synthetic` → `run` → `score` → `gate_6instance`), forces `--no-soft`,
  reads sealed key only at scoring. KILL-1: gate rewritten to §4 (primary
  mean≥0.20/min≥0.10; secondary mean≥0.30/min≥0.22; 6-instance aggregation).
  KILL-2: `truth['planted']` persisted to all 6 sealed keys (bit-identical
  rebuild verified); SECONDARY is true decode accuracy.
- **FIX A (parse repair):** `ct_loader.py` uses CANONICAL repaired parse
  (F32: a5_03 1→0). Verified: 1,847 pairs / 96 groups, "la première" @754
  and @1034 byte-level. Synthetics stay 1,846.
- **FIX B (crib inventory):** new `inventory_mode='crib'` (default) builds
  bottom-up: Tier 1 (7 cribs + by-ear personne + polyvalence islets, weight
  3.0), Tier 2 (by-ear extended, 2.0), Tier 3 (UNITS/top-200, 1.0, suspect
  per N29). Old 'extended' was MISSING 'nne' and 'pers' — gap closed.
  Control audit: DOES plant by-ear chunks ('m' on all 6) — NOT circular.
- **Soft anchors** (87=ce, 64=qui, 96=par) are priors (3 nats), forced OFF for
  controls.
- DEMOTE-1: phase gate restated honestly (noisy detector); `--no-contact`
  added for ablation. DEMOTE-2: projection-equivalent recovery reported
  (ceiling ~0.53–0.60). CONCERN-6: meta/ leak sealed.

## Caveats

- Pilot PRIMARY: 1/89 (method has never demonstrated above-chance recovery;
  CONCERN-2: FREEZE in effect, no more pilot-driven patches).
- The char-5gram's salad preference means the objective relies on the spanning
  word bonus + concentration penalty; `--no-word` ablation is critical.
- 25/67 pilot truth cells share a projected form (ceiling <1.0).
- No R5005 execution; `solver.py` has no real-data default path.
- Known limitations (METHOD.md §8): one secondary per group max; no
  position-conditioned readings; register gap (Les Mis vs Tocqueville).
