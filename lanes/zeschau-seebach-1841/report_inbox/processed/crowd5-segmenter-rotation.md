## segmenter: what is the rotation (crowd5)
- Context: work order was the lane's biggest structural mystery — the 3-phase
  rotational contact structure (chi²=366.3, N30) is real but the tuner proved phases
  are not word-position classes (N15). I pre-registered falsification tests for five
  ideas (morphological, polyvalence-conditioned, unit-size, syntactic, carrier) with
  chance baselines stated first, in code/crowd5/rotation_mystery.md, then ran them
  all against the repaired 1,847-pair stream with independently re-derived phases.
- Decision: T0 verification PASS (re-derived Jaccard-k12 phases match the banked
  phase_map_repaired.json exactly; chi²=366.3 reproduced). Verdicts: morphological
  KILLED (T1b: 13/38 formula edges on-cycle, binomial p=0.25; 06/86 mood contrast
  same phase B/B); polyvalence-conditioning KILLED (T2a p=0.44, T2d p=1.0,
  T2e p=1.0 — phase conditions none of the three polyvalent readings);
  unit-size KILLED (T3 p=0.80, direction reversed: phase-C cells LONGER);
  syntactic NULL (T4a 4/6 function words in phase B, p=0.0566 — misses the 0.05 bar);
  carrier SUPPORTED (T5a: chi²=172 after masking top-10 groups — distributed, not
  hub-driven; T5b: both halves significant — global).
- Why: every test was cipher-internal (F30-legal, no era legs) with exact
  permutation/binomial baselines; the pre-registration (rotation_mystery.md) was
  written before any test ran, so the kills are honest.
- Enlightenment: the post-hoc lag analysis found what none of the five ideas
  predicted — the phase stream has genuine PERIOD-3 sequential structure:
  P(same phase at lag 3)=0.4219 vs 0.3530 expected under the fitted first-order
  Markov chain (z=+5.6, p≈1e-8), lag-2 is z=-3.18 BELOW expectation. It persists
  under the independent old-parse labeling (z=+3.27) and after masking all 157
  known-formula positions (0.4218). The rotation is a real process rhythm, not
  just bigram geometry — and no tested linguistic unit explains it. Leading
  hypothesis: enciphering-process geometry (soft column-rotation through a
  multi-column syllabary table), which predicts exactly this package — real
  rotation, fragile cluster assignment, linguistically arbitrary phases,
  tail-distributed signal.
- For the report: rotation section — headline numbers: chi²=366.3 (T0 verified);
  lag-3 excess z=+5.6 (E1); all four linguistic mappings killed/null with
  pre-registered p-values; rotation distributed (T5a chi²=172 post top-10 mask)
  and global (T5b 204.5/167.0). Evidence files: code/crowd5/rotation_mystery.py,
  rotation_mystery.json, rotation_mystery.md (pre-registration + results).
- Caveats: E1–E4 are POST-HOC (not pre-registered) — the table-geometry
  interpretation is a hypothesis, not a verdict. Discrepancy flagged: old-vs-new
  label agreement measured 69/96 here vs N30's "61/96 change" — needs
  reconciliation. T4a's p=0.0566 near-miss is reported as null per the
  pre-registered bar, not as support. 06/86 and 82/87 same-phase observations are
  single draws (chance P(same)=0.265) — consistency checks only.
