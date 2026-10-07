## scorer-smith: identifiability attack FINAL (round 5, work order 7)

- Context: Follow-up to the swept interim note. Both routes are now COMPLETE
  on the sealed round-4 synthetic control. All numbers in
  `code/crowd5/scorer_identifiability.json`; narrative in
  `code/crowd5/scorer_identifiability.md`; side-fleet read in
  `code/crowd5/homophonic_synergy.md`.
- Decision: The headline stands and hardens — N30's "model-correct" is
  refuted; the joint engine's objective ranks truth ~30 nats below its own
  fluent nonsense. Repair the objective before any more search work.
- Why (final numbers):
  - Route (a) better search: baseline 3x600 sweeps best -2.59..-2.81 /
    top1 0.00-0.10; parallel tempering (6 chains x 600, swaps/10) gbest -2.88 /
    top1 0.05; pool-copy + Gibbs-conditional proposals 3x600 best -2.66..-3.05
    / top1 0.00-0.10; islets 0/3 everywhere (bar 0.50). No variant beats the
    best baseline restart. Search is not the bottleneck.
  - Basin test (decisive): perturb truth by k groups, low-T descent, no
    re-init — k=5: 1/15 recovered, k=10: 2/30, k=20: 0/60 (3/105). All 9
    descents walk AWAY from truth (end -2.47..-2.90, above truth's value).
    There is no basin around truth; the landscape slopes away from it.
  - Route (b) shrink space: b1 (12 hard pins, 3 islet (v1,v2) fixed,
    301-cell inventory) reaches best -33.54..-33.56 vs truth ceiling -33.43
    (within 0.13 nats) — the search DOES reach truth's neighborhood once the
    space is shrunk; top1 0.35-0.40 (4x baseline), islets 1/3. b2
    (conditioned polyvalence, R4/F33): 0/15 verify, 0/3 islets — honest
    negative (control islets are unconditioned coins; documents a
    control-vs-reality gap). b3 (small inventory alone): top1 0.05, no better
    than baseline.
  - Model bugs (both load-bearing): (1) lam_poly=10 is ~100x over scale —
    truth beats the annealed best only at lam_poly < 0.09; at 10 the v2
    machinery is dead by construction (annealed n_poly=0, islet bar
    unmeetable). (2) The raw-letter 7-gram alone prefers the annealed key
    (-3.11/letter) over truth (-3.64/letter); the E-step recovers only 42/63
    of the truth's islet emissions from the true key.
  - Control-design findings: 2/20 bar groups unidentifiable BY CONSTRUCTION
    (group 41: 'ri' emitted 1.8% of 274, modal 'mi' 2.2%, 160 distinct cells) —
    max achievable top-1 = 0.90. The control validates machinery, not the unit
    set (only 23/89 truth primaries are in the 24-unit crib-derived set).
- Enlightenment: The "identifiability problem" framing was wrong in the
  precise sense — it is not a flat landscape the search cannot cross, it is a
  miscalibrated objective whose optimum is not truth. Route (b) proves the
  search works fine given constraints; route (a) proves no search fixes the
  model. The side-homophonic fleet independently found the same disease (their
  pilot: salad -3.89/pair beats truth -4.44/pair) and their stack (phonetic
  projection + spanning word bonus + concentration penalty) is the concrete
  repair. Their positive control's first attempt was SIGTERMed mid-scoring
  (owner revised the harness); reruns in flight, no verdict — do not cite.
- For the report: round-5 scorer-smith section; methodology lessons (control-
  first held: the gate correctly refused R5005). The ordered fix list:
  lam_poly scale, phonetic projection, spanning word bonus, concentration
  penalty ON, homophone-pool/block proposals, per-stream chi2-gated phase,
  F34 inventory rebuild for the R5005 run.
- Caveats: All control-side. Nothing ran on R5005 — gate holds. The
  side-homophonic positive control has no verdict yet; the synergy doc's
  "if theirs passes and ours doesn't" branch is still open.
