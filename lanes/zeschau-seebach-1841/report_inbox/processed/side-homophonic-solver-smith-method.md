# Solver-Smith method note — Seebach homophonic joint-inference solver

## Context

R5005 (Zeschau→Seebach, 18 Jan 1841): French two-digit syllabary, 1,846 pairs,
96 groups, 7 hard anchors, established polyvalence, by-ear spelling, 3-phase
contact rhythm. Round-1 (syllable annealer, 1/88 on control) and scorer3
(3× broken on control) both failed for the same diagnosed reason: **no joint
inference over the full key**. My brief: build the joint-inference solver,
validate it on the Control Designer's synthetic control, never run on R5005.

Deliverable lives in `code/side-homophonic/solver/`:
`solver.py` (SA engine), `phonetics.py` (projection π), `build_lm.py`
(Tocqueville LM), `phase.py` (contact analysis), `control_harness.py`
(load_synthetic → run → score → gate), `ct_loader.py` (real-data adapter,
import-isolated), `config.json`, `METHOD.md` (full justification), `README.md`.

## Decision

**Simulated annealing over the full key**, not EM or Gibbs.

## Why

- The posterior is multimodal and discrete (96 groups × ~300 values, many-to-one
  + polyvalent v2). SA with restarts explores it; EM climbs to the nearest
  mode (fatal here — see below); Gibbs mixes too slowly across the
  96-dimensional coupling.
- The objective decomposes **exactly per move**: char-5-gram (local in t),
  spanning-only word bonus (windowed Aho-Corasick deltas), contact Potts
  (sparse adjacency), soft priors, polyvalence penalty. No suffix rescoring,
  no approximations. `--self-test` proves incremental == full recompute
  (max err 1.7e-10 over 300 random moves).
- It avoids the round-1 failure modes structurally: the round-1 annealer died
  because its syllable-bigram LM was uninformative (letters inexpressible);
  mine scores a **phoneticized char-5-gram** (letters project to phonetic
  classes) plus a word bonus, with 4 calibrated restarts × 15k iterations
  beating random by +16,000 nats on the pilot.
- Polyvalence is explicit (v1 + optional per-occurrence v2 with hard E-step,
  20-nat prior against spurious splits); the 7 pins are never moved; phase
  rhythm enters as a gated contact Potts prior (gate from unsupervised χ²,
  <0.02 on null streams, ≈1 at χ²=181).

## Enlightenment

Two degenerate attractors found and killed by the pilot (my own labelled
synthetic, Les Mis plaintext, 96 groups, 7 pins — the Designer's control was
not yet landed):

1. **Empty-projection exploit.** `project('st')` returned `''` (silent-final
   regex deleted the whole consonant cluster); empty scores exactly 0, better
   than any real text. The annealer mapped 80/89 groups → 'st'. Fix: silent
   finals delete **after vowels only** ("st"→"st", "les"→"le", "est"→"e"),
   plus a never-empty belt-and-braces guard. Lesson: *every* projection rule
   needs the "can this produce empty?" check.
2. **Frequent-word salad.** With the exploit fixed, the solver tiled the
   stream with common words ("leur même mais mes…") — and the char-5gram
   **genuinely preferred it** (−3.89/pair) to the true Les Mis decode
   (−4.44/pair). Maximum-likelihood under an n-gram does not recover real
   text when the key can choose word-sized values. Fix: the word bonus is now
   **spanning-only** — `S_word = AC_scan − Σ single_value_hits`; only words
   assembled from 2+ values ("cha"+"pi"+"tre"="chapitre") count. The perverse
   incentive is removed exactly, with exact incremental deltas.

Both fixes are validated by `--self-test` (bookkeeping) and the pilot
(recovery — result below).

## For the report

- The solver is **control-ready**: `control_harness.py` implements the agreed
  interface (`load_synthetic(path)` → `run` → `score` → `gate`), forces
  `--no-soft` on controls, and reads the sealed key only at scoring time.
- **Inventory conflict (flagged for the Designer):** the brief says draw values
  from UNITS (180 items), but the Control Designer plants from encipher_split
  cells; UNITS covers only 78–83% of the top encipher_split cells (measured).
  Default is UNITS ∪ top-200 encipher_split cells (~300); `--inventory-mode
  units` restores strict compliance for ablation. The harness reports per-group
  "truth in inventory" so a plant outside it reads as a design mismatch.
- **Soft anchors** (87=ce, 64=qui, 96=par) are priors (3 nats), forced OFF for
  controls — matches their provisional red-team status.
- Pre-registered gate bars (proposed, CONTROL-DESIGN.md finalizes): pins 7/7,
  PRIMARY ≥ 0.50, PRIMARY ≥ chance+0.30, islets ≥ 4/6, best−random20 ≥ 200
  nats, MRR ≥ 0.60.

## Caveats

- Pilot PRIMARY result: **[TBD — background run in flight]**.
- The char-5gram's salad preference (finding 2) means the objective relies on
  the spanning word bonus to pick real French over frequent-word tiling; the
  `--no-word` ablation on the control is the critical diagnostic.
- 25/67 pilot truth cells share a projected form with another truth cell
  (accent mergers); exact string recovery has a ceiling below 1.0 even for a
  perfect solver. PRIMARY should be read with this in mind.
- No R5005 execution performed; `solver.py` has no real-data default path.
- Known limitations (METHOD.md §8): no explicit homophone-profile prior;
  phase prior is a gate, not a transition model; v2 M-step is hard, not soft.
