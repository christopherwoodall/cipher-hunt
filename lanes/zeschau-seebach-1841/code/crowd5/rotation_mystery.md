# ROTATION MYSTERY — crowd5/segmeter: "What is the rotation?"

## Objective
The 3-phase rotational contact structure A→C→B→A is real and LOUD
(chi²=366.3 on the repaired 1,847-pair parse, N30). The tuner PROVED phases are
NOT word-position classes (N15: LOO phase-constrained 2/34 vs unconstrained 6/34).
Cluster assignments are fragile (61/96 change phase on recompute) but the transition
structure is robust. This work order tests falsifiable linguistic hypotheses for
what the rotation IS, using only the repaired stream and crib-learned units
(F30 — no era-syllable-conditional legs on fragments; no era leg at all is needed
here: every test is cipher-internal).

## Canonical inputs
- Pair stream: `code/side-keyhunt/repaired_offsets.json` → 1,847 pairs, 96 groups.
- Phases: recompute Jaccard-k12 (contactor's method, `synth_control.derive_phases`)
  independently on the repaired stream; verify == `phase_map_repaired.json` and
  chi²(3×3 ABC) ≈ 366.3 before any test (T0).
- Cycle edges: A→C, C→B, B→A. Off-cycle edges: everything else incl. self-transitions.
- Known cells (status-marked): GT {11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que};
  provisional {87=ce, 64=qui, 96=par, 94=ne, 06=verb-stem-class(unvalued), 67=veut?};
  STRONG LEAD 62=on; LEADs {78=me, 77=le, 47=ce}; 52=pas (STRONG-bounded);
  86=infinitive-complement stem (N29).
- R-handling: phase map has 20 R groups. All 3×3 tests use transitions where both
  endpoints ∈ {A,B,C} (matches the chi² construction). Formula edges touching R are
  listed, excluded from the binomial, count reported.

## PRE-REGISTERED TESTS (falsification-first; baselines stated BEFORE numbers)

### T0 — verification (gate)
Re-derive phases via Jaccard-k12 agglomerative (top-10 contact sets, avg-linkage,
k=12 cut, 3 largest = A/B/C). Must reproduce `phase_map_repaired.json` exactly and
chi²=366.3 ±1 on the ABC 3×3. If not, stop — instrument unreproduced.

### Idea 1 — MORPHOLOGICAL: do phase boundaries align with stem|suffix cuts?
- T1a (mood-contrast kill test): 06 (finite/imperative stem) vs 86 (infinitive-
  complement stem) is the lane's cleanest morphology-controlled contrast (N29:
  00→86 ×12 vs 00→06 ×0 — complementary distribution). If phase marks morphology,
  06 and 86 should sit in DIFFERENT phases. Chance baseline: two random groups
  share a phase with P = Σ p_i² (compute from marginals). Verdict: if same phase
  → FAILS TO SUPPORT (weak kill: P(same)≈0.25 under chance, so this is a
  one-draw honesty check, not a refutation).
- T1b (cut-alignment depletion test): collect UNIQUE directed edges that are
  KNOWN formula/word-internal (pre-registered list, ~35): "la première" 5 edges;
  "parce que" 96→87→46 (2); "ce qui" 87→64 (1); 24→87→64 (2); 77→78→94→82→06 (4);
  64→96→43→87→01 (4); 9-mer 56…01 (8); "on ne" 62→94 (1); 94→52 (1); 06→29 (1);
  77→86 (1); 78→40 (1); 47→78 (1); 37→78 (1); 94→59 (1); "cela" 87→11 (1);
  "personne" cuts 93→52, 52→94, 77→62, 62→94 (4). n = unique ABC-bounded edges.
  H0: on-cycle rate among these = global p_on (fraction of ABC transitions on
  {A→C,C→B,B→A}, computed WITH and WITHOUT the formula edges). Two-sided exact
  binomial, α=0.05. Falsification: p≥0.05 → the cut-alignment formulation of the
  morphological idea is KILLED (null). If depleted/enriched at p<0.05 → direction
  decides the interpretation (off-cycle enrichment = formulas AVOID cycle edges =
  rotation is a boundary rhythm, not word-internal morphology).
- T1c (subset): split T1b edges into word-internal (la|première 5 + personne 4)
  vs formula-cross-word (rest); same binomial per subset. Pre-register: if the
  word-internal subset rides off-cycle edges, the "phase=stem|suffix" reading
  is KILLED in its strong form.
- T1d (descriptive leg): 00→86 ×12 infinitive-complement frame: P(next=B|prev=C)
  for group 00 vs global P(B|C); binomial one-sided. If ≥chance → no support.

### Idea 2 — POLYVALENCE-CONDITIONED: is phase the hidden conditioner? (F33)
- T2a (06 "ent" vs stem): 06 occurrences classified: trigram-final (prev-pair
  = 94-82, i.e. -nement trigrams; expect ~3) vs free (~43). Test: phase(next)
  profile differs between the two classes. Statistic: χ² distance between the
  two next-phase distributions. Baseline: permutation of class labels among 06
  occurrences (10,000 shuffles), one-sided p. Pre-register: p<0.05 required to
  claim phase conditions 06's reading. Note phase(prev) is constant (A) for the
  trigram class — the test is on phase(next) only; stated so the null can't be
  gamed.
- T2b (94 "en"-islet vs "ne"): each 94 occurrence classified "en" iff
  prev-group=82 OR next-group=87 (F33's rule), else "ne". Test phase(prev)
  profile difference, same permutation design (10,000). Pre-register p<0.05.
- T2c (naked-adjacency falsifier): locate 06 occurrences within ±3 of another 06
  (F33: naked adjacency of the two readings). If a trigram-06 and a free-06 sit
  in identical phase environments (same prev/next phase), phase-as-conditioner
  for 06 is FALSIFIED (same conditioner value, different readings).
- T2d (52 "pas" vs "se/so"): 52 occurrences classified "pas"-candidate iff a 94
  (=ne) occurs in window −6..−1 (negation frame heuristic — F33's rule is
  "iff negation-frame"; heuristic stated as approximation). Same permutation
  test on phase(next) profile. Caveat pre-registered: frame heuristic is
  approximate; a null here is weak evidence.

### Idea 3 — UNIT-SIZE: does phase correlate with crib-learned cell lengths? (R1)
- Known cells (status-marked, lengths): la2, pre3, m1, i1, er2, e1, que3 (GT);
  ce2(87), qui3, par3, ne2 (provisional); on2 (STRONG LEAD); me2(78), le2(77),
  ce2(47), pas3 (bounded); veut4 (provisional). n=17, pre-registered WEAK BY DESIGN.
- T3a (directional): phase-C cells (suffix hypothesis) shorter than A/B cells.
  Statistic: mean(len|C) − mean(len|A∪B). Baseline: 10,000 phase-label
  permutations over the 17 cells, one-sided p.
- T3b (3-way): statistic = variance of the three phase means; same permutation
  baseline, one-sided p. Pre-register: p<0.05 to claim; expect low power, report
  honestly either way.

### Idea 4 — SYNTACTIC: phase vs function-word/content-word alternation
- T4a (function-word co-phase): function set F={la,que,ce,qui,par,ne} (all
  provisional-or-better). Count in modal phase; baseline binomial(n, p_modal)
  with p_modal = repaired-map marginal of the modal phase. Pre-register the
  modal phase as B (repaired map: la=B, que=B observed in code read; the test
  counts k=|{F in B}| vs binomial(6, p_B)). Also extended set F+={la,que,ce,qui,
  par,ne,pas,ce47} (8). Pre-register: need p<0.05 to claim.
- T4b (proclitic pair): 82=m and 87=ce both phase A (repaired map read in code).
  Baseline P(same phase)=Σ p_i². One draw — consistency check only, stated as such.
- T4c (fragment-side): GT fragments {pre(B), m(A), i(B), er(C), e(A)} — no
  coherent phase under the syntactic hypothesis; pre-register as the
  hypothesis's built-in tension: if T4a is null AND fragments scatter, the
  syntactic idea is KILLED.

### Idea 5 — ROTATION CARRIER: hub-driven vs distributed (table-geometry proxy)
- T5a (hub masking): recompute 3×3 chi² after masking the top-k groups by
  frequency (k=0..10 cumulative). Pre-register: if chi² stays >50 (df=4,
  p<1e-9) after removing the top-10 groups → rotation is DISTRIBUTED, not a
  hub artifact. If it collapses below chi²=20 (p>5e-4) → hub-driven, and the
  masking order names the carrier groups.
- T5b (temporal halves): chi² on pairs[0:923] vs pairs[923:1847] separately.
  Pre-register: both halves p<1e-3 → global rhythm of the enciphering process;
  else the rotation is a LOCAL artifact (one repetitive formula/region) and the
  "what is the rotation" answer must be regional.

## Decision rules
- supported: p<0.05 vs pre-stated baseline, effect in the pre-stated direction,
  survives the pre-stated robustness variant.
- killed: p≥0.05 on the pre-registered falsification test, OR a direct
  contradiction (T1a same-phase, T2c naked-adjacency).
- null: test executed, baseline not beaten — reported as null, never as support.

## Best-answer template (to fill after tests)
"WHAT IS THE ROTATION" gets exactly one of: (a) morphological-slot rhythm,
(b) polyvalence conditioner, (c) cell-size/granularity rhythm, (d) syntactic-slot
rhythm, (e) boundary rhythm (cycle edges = between-word, off-cycle = word-internal),
(f) table-geometry/hub artifact, (g) still unknown — with the test numbers attached.
