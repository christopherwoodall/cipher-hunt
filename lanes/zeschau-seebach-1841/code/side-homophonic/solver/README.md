# Seebach homophonic solver — solver-smith deliverable

Joint-inference (simulated annealing over the full key) solver for the
R5005 French two-digit syllabary. **Do not run on R5005 until the synthetic
control passes** (see `control_harness.py` gate).

## Files

| file | what |
|---|---|
| `solver.py` | the SA solver + CLI + `--self-test` |
| `phonetics.py` | phonetic projection π + evidence-graded rules + self-test |
| `build_lm.py` | Tocqueville → `lm.json` (char 1-5-grams, lexicon, stats) |
| `phase.py` | unsupervised contact analysis (Jaccard, k=12, χ² gate) |
| `control_harness.py` | `load_synthetic → run → score → gate` |
| `ct_loader.py` | **real-data adapter** (R5005 pairs); import-isolated, never used by the solver core or harness |
| `config.json` | default hyperparameters |
| `METHOD.md` | method justification (read this first) |

## Quick start (Runner)

```bash
cd code/side-homophonic/solver
# 1. build the reference LM (once; Tocqueville-only, ~10s)
python3 build_lm.py --out lm_ref
# 2. sanity: incremental-scoring self-test (must PASS before anything else)
python3 solver.py --pairs <pairs> --lm lm_ref/lm.json --out /tmp/st \
    --anchors '{"11":"la",...}' --self-test
# 3. control gate (truth enters only at scoring)
python3 control_harness.py --ct ../control/instances/SYNTHETIC-ct-184101.pairs.txt \
    --truth ../control/instances/SYNTHETIC-key-184101.json \
    --crib  ../control/instances/SYNTHETIC-crib-184101.json \
    --chance <analytic chance PRIMARY from chance_baseline.json> \
    --lm lm_ref/lm.json --out runs/ctl-184101
# 4. ablations (run on the control; freeze the winner for R5005)
for f in "" "--no-phase" "--no-word" "--no-poly"; do
  python3 control_harness.py --ct ... --truth ... --crib ... --lm lm_ref/lm.json \
      --out runs/ctl-184101$f $f
done
# 5. real run (ONLY after CONTROL-PASS)
python3 ct_loader.py /tmp/r5005.pairs.json   # real-data adapter, explicit step
python3 solver.py --pairs /tmp/r5005.pairs.json --lm lm_ref/lm.json \
    --out runs/r5005 --anchors '{"11":"la","70":"pre","82":"m","34":"i","29":"er","40":"e","46":"que"}' \
    --soft '{"87":"ce","64":"qui","96":"par"}'
```

`solver.py` reads `--pairs` as JSON `{"pairs": [...]}` or whitespace-separated
text (`#` comments allowed). Output `result.json`: best assignment (v1/v2/w2
per group), score parts, per-restart assignments, cross-restart marginals,
random20 baseline, phase diagnostics.

## For the Control Designer

- The solver consumes `SYNTHETIC-ct-<seed>.pairs.txt` (your current format) +
  anchors from the crib file. No other input.
- The sealed key is read **only** by `control_harness.score()`, never by the
  solver. Keep it that way.
- Proposed gate bars are in `control_harness.BARS` and `METHOD.md` §7;
  CONTROL-DESIGN.md finalizes them.
- Two flags for you: (a) per-position planted cells are not persisted by
  `write_instance`, so the harness scores a SECONDARY *proxy* (primary
  agreement per position) -- persist `planted` if you want the exact metric;
  (b) the solver's default inventory is UNITS ∪ top-200 encipher_split cells;
  the harness reports per-group "truth in inventory" so a plant outside it
  shows up as a design mismatch, not a solver failure.
- LM independence: reference LM is Tocqueville-only; your Les Mis plaintext
  is disjoint. The harness asserts this.

## Hyperparameters (config.json; CLI overrides)

`restarts` 12, `iters` 40000, `t0` 60.0, `tmin` 0.05, `lambda_word` 1.0,
`beta0` 2.0, `w_soft` 3.0, `lambda_poly` 20.0, `inventory_mode` extended,
`init` random, `refine` true. Every knob is defined in `METHOD.md`.
