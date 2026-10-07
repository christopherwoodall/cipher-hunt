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

## RESULTS (2026-10-07, code/crowd5/rotation_mystery.py → rotation_mystery.json)

### T0 — VERIFICATION: PASS
Jaccard-k12 re-derived on the repaired 1,847-pair stream reproduces
`code/crowd4/phase_map_repaired.json` EXACTLY; 3×3 ABC chi²=366.3 (matches N30).
Phase sizes: A=32, B=27, C=17, R=20. Global on-cycle rate p_on=0.2807 (1,514 ABC
transitions). Chance P(two groups share a phase)=0.265.

### Idea 1 — MORPHOLOGICAL: KILLED
- T1a: 06=B, 86=B — the cleanest morphology-controlled contrast (finite/imperative
  vs infinitive-complement stem, N29) does NOT separate in phase. Fails to support
  (one draw; chance P(same)=0.265, so weak — but the direction is wrong for the idea).
- T1b: 38 unique known formula/word-internal edges, 13 on-cycle vs p_on=0.281:
  exact binomial P(≥13)=0.2495, P(≤13)=0.8468 (0.8443 on the exclude-formula
  baseline). NULL → the cut-alignment formulation is KILLED.
- T1c: word-internal subset 2/10 on-cycle (P(≤)=0.4358); cross-word 11/28 (P(≤)=0.9332).
  Both null → strong-form "phase=stem|suffix" KILLED.
- T1d: 00→86 ×12/55 vs global P(B|C)=0.2695, P(≥)=0.8439. Null.

### Idea 2 — POLYVALENCE-CONDITIONED: KILLED
- T2a: 06 trigram-final (n=3 @580/1184/1355) vs free (n=41): next-phase profile
  χ²-distance permutation p=0.4399. NULL.
- T2d: 94 "en"-islet (n=4 @651/1102/1169/1576 — three "m'en", one "en ce",
  matches F33's rule) vs "ne" (n=33): prev-phase profile permutation p=1.0000. NULL.
- T2e: 52 negation-frame (n=5) vs other (n=22): next-phase profile permutation
  p=1.0000. NULL.
- T2c: 4 near-06 pairs; 0 mixed-reading/same-phase-env pairs — no falsification,
  but note the naked adjacency itself: 2/3 trigram-06s (@580, @1184) are IMMEDIATELY
  followed by a free-06 ("-nement"+stem-06 adjacency). Phase does not condition any
  of the three polyvalent readings. KILLED.

### Idea 3 — UNIT-SIZE: KILLED
n=17 known cells: mean(C)=2.40 vs mean(not-C)=2.17 — direction REVERSED vs the
suffix-short hypothesis; directional permutation p=0.7979; 3-way variance-of-means
p=0.7766. KILLED.

### Idea 4 — SYNTACTIC: NULL (bar not met)
- T4a: function words {la,que,ce,qui,par,ne} → 4/6 in phase B; binomial(6, pB=0.281)
  P(≥4)=0.0566 — misses the pre-registered 0.05 bar. Extended set (+pas bounded,
  +ce47 LEAD) 4/8, P(≥)=0.1615. NULL by rule; the lean is noted, not claimed.
- T4b: 82=m/87=ce both phase A — consistent (chance 0.265), not evidence.
- T4c: GT fragments scatter across 3 phases of 5 — built-in tension stands.

### Idea 5 — CARRIER: SUPPORTED (distributed + global)
- T5a: masking top-k frequent groups (drop transitions touching them): chi² falls
  366.3 → 172.1 at k=10 (n_trans 1514→846) — still ≫50 (p≪1e-9). The rotation is
  DISTRIBUTED, not hub-driven. (k=7→8 flat: the 8th group is R-phase 98.)
- T5b: first half chi²=204.5, second half chi²=167.0 — both highly significant.
  GLOBAL, not a regional artifact.

### Exploratory (POST-HOC, not pre-registered — labeled as such)
- E1: lag-k same-phase rates: lag1=0.167, lag2=0.303, **lag3=0.4219**, lag4=0.287,
  lag5=0.353, lag6=0.336 vs chance 0.3366. Under the fitted first-order 3-state
  Markov chain the expected lag-3 rate is 0.3530; observed 0.4219 is z=+5.60
  (p≈1e-8) ABOVE it, while lag-2 is z=-3.18 below. The stream carries genuine
  PERIOD-3 sequential structure beyond what the block transition matrix explains.
- E2: persists under the INDEPENDENT old-parse labeling (contactor): lag3=0.3776
  vs Markov-expected 0.3386, z=+3.27 (p≈0.001). Not a labeling artifact of one
  clustering run.
- E3: unchanged (0.4219→0.4218) after masking 157 positions covering all known
  formulas (parceque ×3, 24-87-64 ×3, rep5 ×2, revjoints ×2, 9-mer ×2,
  lapremière ×2, cela ×7, on-ne ×9). Stream-wide, not formula-driven.
- E4: anchors' aggregate on-cycle rate 0.27 ≈ global 0.281 (per-anchor 0.135–0.455);
  anchor ablation chi²/n 0.2420→0.2054. Anchors are average participants, not
  rotation-breakers in aggregate (their single dominant edges are off-cycle because
  function words have diverse contacts — descriptive only).
- DISCREPANCY FLAG: old-vs-new label agreement measured here = 69/96 (27 change)
  at best permutation; N30 states "61/96 change phase on recompute". The 61/96
  figure may reflect a different recompute than the banked phase_map_repaired.json
  (which T0 reproduces exactly). Coordinator to reconcile.

## BEST CURRENT ANSWER to "what is the rotation"
A real, global, distributed, SEQUENTIAL period-3 rhythm in the group stream
(repaired labels: dominant edges A→B 0.545, B→C 0.498, C→A 0.624 — a label
permutation of the contactor's A→C→B→A). It is NOT word-position (N15), NOT
morphological slot (T1 killed), NOT the polyvalence conditioner (T2 killed), NOT
cell size (T3 killed), NOT syntactic class (T4 null). The lag-3 excess beyond
first-order Markov (z=+5.6, robust across labelings and formula masking) means it
is a genuine process rhythm, not just bigram-matrix geometry.
LEADING HYPOTHESIS (not a verdict): enciphering-process geometry — e.g. the
encipherer moving through a multi-column syllabary table with a soft column-rotation
habit (suppresses same-column repeats → self-transitions 0.51–0.74×; prefers
cycling → cycle edges 1.35–1.52×; 3-step memory → lag-3 excess). Predicts exactly
the observed package: real rotation + fragile cluster assignment (columns are
linguistically arbitrary → fragments scatter, T4c) + no linguistic mapping (all
killed) + tail-distributed (T5a). Falsifiable in round 6 — see below.

## BEST NEXT STEP (round 6 work order)
1. Labeling-robustness battery for E1: re-derive phases with cosine metric,
   k=8/k=16 cuts, and half-stream clustering; the lag-3 excess (z vs
   Markov-expected) must persist in all variants, else E1 is a labeling artifact.
2. Model comparison: 3-state HMM vs first-order 96-group bigram model, held-out
   log-likelihood / BIC on the 1,847-pair stream. If the HMM wins, the 3-state
   process is real; if the bigram model wins, "the rotation" is bigram-matrix
   shape and the phase labels add nothing.
3. Table-geometry mechanism test: as key recovery proceeds, test whether
   same-phase groups' plaintext values are linguistically arbitrary (table-column
   prediction) vs coherent (linguistic-slot prediction).
4. Word-length-rhythm alternative: needs boundary ground truth (more cribs/key);
   untestable with current instruments (segmenter is circular here — F26).
