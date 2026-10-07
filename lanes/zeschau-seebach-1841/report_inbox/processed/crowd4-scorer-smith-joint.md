## scorer-smith: joint engine + parse-repair adoption

- Context: WO8 — build a JOINT decipherment engine (annealing/EM over the full
  96-group key) with polyvalent emission, validated on a synthetic control
  BEFORE touching R5005. Control-first is mandatory (N16 lesson). On 2026-10-07
  the lane's canonical parse was repaired (key-hunt side fleet, red-team
  verified): offsets['a5_03'] 1→0, 1,846→1,847 pairs. I adopted the repaired
  parse before finalizing.
- Decision: ADOPTED the repaired parse (code/crowd4/repaired_parse.py,
  run_r5005.py updated). RECOMPUTED the Jaccard-k12 phases on the repaired
  stream (code/crowd4/phase_map_repaired.json) — the banked contactor phases
  are stale. Control verdict: FAILING (below pre-stated bars); R5005 gate
  holds (no R5005 run).
- Why: The repaired parse is canonical (supersedes data/upstream-offsets.json).
  Pair values are identical except 25 re-paired in row a5_03; indices shift +1
  for old ≥773. My engine's R5005 path now loads 1,847 pairs and asserts the
  "la première" (11-70-82-34-29-40) anchors at pairs 754 AND 1034. For phases:
  the banked contactor phases were derived from the old parse; recomputing on
  the repaired stream, 61/96 groups change phase (Jaccard clustering is
  sensitive to the 1.4% data change). The recomputed phases give rotation
  chi²=366.3 on the repaired stream vs 178.8 with banked phases — the repaired
  parse's rotation is STRONGER, confirming the recomputed phases are correct
  for the canonical data. The engine uses the recomputed phases (weak prior,
  lam_rot=0.5).
- Enlightenment: Two surprises. (1) The parse repair UNCOVERED a second "la
  première": the despatch says it twice (pairs 754 in the repaired row a5_03,
  and 1034 in row a6_03). The lane had been anchored on the second occurrence
  all along. (2) The Jaccard phase clustering is FRAGILE: 25 changed pairs
  (1.4%) flip 64% of phase assignments, yet the rotation chi² nearly doubles
  (178.8→366.3) with the recomputed phases. The transition STRUCTURE
  (A→C→B→A) is robust; the CLUSTER ASSIGNMENTS are not. This validates using
  rotation as a weak transition prior (not a hard label) — the tuner NULL
  (phases are not word-position classes) was the right call.
- For the report: Methods/Parse section. Numbers: 1,847 pairs (not 1,846);
  96 groups unchanged; 25/1,847 pairs (1.4%) changed values; "la première" at
  754 AND 1034 (0-based); rotation chi²=366.3 (recomputed) vs 178.8 (banked);
  61/96 groups change phase under repair. Engine status: control FAILING —
  best annealed accuracy 0.05 (top-20 frequent non-pin groups), islets 0/3,
  vs pre-stated bars (pins 7/7 ✓, primary top-1 ≥0.50, islets ≥2/3, margin
  ≥200 nats). The model is CORRECT (n=7 letter LM: truth −2.65 beats annealed
  −3.05), but the SEARCH cannot find truth's basin — many near-optimal wrong
  keys (identifiability problem, not a model problem).
- Caveats: (1) I could NOT verify the manuscript images; if the a5_03 gloss
  line-tag is wrong, the old parse revives (per REINDEX.md). (2) The control
  uses synthetic "ear-cutting" noise (29% token perturbation); if the real
  encipherer's inconsistency is lower, the control may be pessimistically hard.
  (3) The phase recomputation uses my reimplementation of the contactor's
  Jaccard-k12 (validated: exact match on old parse); the contactor has not
  re-run on the repaired parse. (4) No R5005 run — the gate correctly held.
  Outputs are LEADS, never promotions.
