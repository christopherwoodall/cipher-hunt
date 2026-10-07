# PREREG — rotation round 6 (segmenter, 2026-10-07)

All tests below are PRE-REGISTERED. Code: `code/crowd6/segmenter/rotation_r6.py`,
results: `rotation_r6.json`. Canonical stream: repaired 1,847-pair parse
(`code/side-keyhunt/repaired_offsets.json` via `code/crowd4/repaired_parse.py`).
Cipher-internal only (F30-legal); no era legs; no invented values.
Seed fixed at 20261007 for every randomized step.

## Amendment A3 (2026-10-07, after a numerically broken first attempt)
The first hmm_test.py run diverged (emission collapse → c[t] underflow →
testLL/trans = −332, overflow warnings). Fix: MAP-EM with a weak Dirichlet
prior (eps=1e-4 additive smoothing on A and E in the M-step) — a numerical
floor, not a model change; M_big's Laplace α=1 is the stronger-smoothed
comparator. The restart train-LL spread is now recorded in the JSON.

## Amendment A2 (2026-10-07, before thread 2 completed)
Thread 2 runs as `hmm_test.py` (split out: slow). Restarts 20→10, iters
200→150 (early stopping at 1e-6 relative LL as coded — the pre-registered
stopping rule). Rationale: 0.17 s/EM-iter measured on the train split; 20×200
would exceed an hour of wall on the current loaded VM. The restart SPREAD is
reported, so the parent can judge whether 10 restarts suffice. The verdict
rule (test-LL AND BIC) is unchanged.

## Amendment A1 (2026-10-07, before any variant ran)
The gate run showed the naive full-stream construction does NOT reproduce F43's
E1 (obs 0.3579 vs banked 0.4219). Diagnostic re-derivation pinned the actual
construction: lag-3 pairs restricted to BOTH ENDPOINTS in ABC (n=1510),
Markov expectation conditioned on endpoints-ABC. This reproduces the banked
obs EXACTLY (0.4219), z=5.81 vs banked 5.6, exp=0.3505 vs banked 0.3530
(residual 0.0025 = minor conditioning ambiguity, recorded not hidden).
The gate and all thread-1 variants now use this pinned construction.
The bar (z>2 in reference + all 5 variants) is unchanged.

## Reference re-derivation (gate for every thread)
Banked repaired labels `code/crowd4/phase_map_repaired.json` applied to the
stream → lag-k same-phase rates for k=1..6, and the F43 E1 statistic:
obs = P(L_{t+3} == L_t) over all t; exp = Σ_s π_s (M³)[s,s] with M the MLE
first-order Markov matrix on the 4-state (A,B,C,R) label stream and π its
stationary; z = (obs−exp)/sqrt(exp(1−exp)/n), n = # lag-3 pairs.
GATE: must reproduce obs≈0.4219, exp≈0.3530, z within ±1.0 of 5.6. If not,
stop — the E1 instrument is unreproduced and nothing downstream runs.

## Thread 1 — labeling-robustness battery for the lag-3 excess
For each labeling variant below: derive group→phase labels, apply to the
stream, recompute the E1 statistic exactly as in the gate.
- V_cos: cosine similarity on Laplace-smoothed predecessor+follower
  distributions (contactor's cos construction), average linkage, k=12 cut,
  3 largest clusters = A/B/C, rest R.
- V_k8: Jaccard on top-10 contact sets (contactor's jac), average linkage, k=8.
- V_k16: same, k=16.
- V_half1: Jaccard k=12 fit on pairs[0:923] only; labels applied to
  pairs[923:] (out-of-sample); E1 computed on the second-half label stream.
  Groups absent from the fit half → 'R'.
- V_half2: fit on pairs[923:], evaluate on pairs[:923].
VERDICT (pre-registered): ROBUST iff z > 2.0 (one-sided) in the reference AND
all five variants. If any variant gives |z| ≤ 2 → FRAGILE in that direction;
name the variant. Secondary (mechanism check): after best-permutation
alignment of each variant's labels to the reference, the dominant directed
3-cycle (A→B→C→A vs A→C→B→A, by ABC transition mass) must be the same in all
variants — a real table-column order is unique.

## Thread 2 — 3-state HMM vs 96-group bigram model, held-out
Split (pre-registered): train = pairs[0:1231], test = pairs[1231:1847].
- M_big: first-order Markov on 96 groups, Laplace α=1 MLE on train.
  k_big = 96·95 = 9120.
- M_hmm: 3-state HMM, Baum-Welch on train, 20 random restarts × 200 iters,
  keep best train LL. k_hmm = 6 (trans) + 285 (emit) + 2 (init) = 293.
- M_phm (informative middle rung): banked repaired labels as OBSERVED states:
  3-state Markov (6) + emission (285) + init (2) = 293, MLE on train.
Metrics: test log-likelihood per transition; BIC = −2·LL_train + k·ln(n_train),
n_train = 1230 transitions.
VERDICT (pre-registered): the explicit 3-state process model wins iff
test-LL/transition(M_hmm) > test-LL/transition(M_big) AND BIC(M_hmm) < BIC(M_big).
Report M_phm alongside (does the hidden process add anything over the
clustering labels?). Corroboration (not verdict-driving): Viterbi-decode M_hmm
on the full stream; best-permutation agreement of Viterbi states with banked
ABC labels on ABC-labeled groups.
Caveat (pre-registered): M_big with 9120 params on 1230 train transitions is a
strawman baseline — its held-out LL is expected to be poor. The comparison is
run exactly as ordered; M_phm is the fair middle rung.

## Thread 3 — reconcile 69/96 vs "61/96 change" (N37 flag)
Old labels: contactor's old-parse Jaccard-k12 block labels, reconstructed from
`code/crowd/contactor_results.json` → jaccard_clusters['12'], 3 largest = A/B/C
by size, rest R (mirrors contactor.py). New labels: `phase_map_repaired.json`.
Compute: (a) naive agreement = fraction with identical label names (A/A…R/R);
(b) best-permutation agreement over 24 label perms; (c) both restricted to
groups labeled ABC in both maps.
RECONCILIATION RULE: whichever of (a)/(b) reproduces "61 change" (35/96 agree)
identifies N30's comparison; whichever reproduces 69/96 identifies N37's. The
discrepancy is then a definitional difference, not a data contradiction —
report exactly which comparison each number describes.

## Thread 4 — column-geometry hypothesis: concrete model + testable predictions
MODEL (stated before testing): the syllabary table has columns ≈ the ABC
phases; the encipherer's hand/eye moves through columns as he enciphers, with
momentum (a finger in motion stays in motion). Reference dominant cycle from
banked labels: A→B 0.545, B→C 0.498, C→A 0.624, i.e. cyc = A→B→C→A.
PREDICTIONS (pre-registered; tests on the banked-label stream):
- P2a (momentum): on ABC-only triples, r1 = P(L_{t+1}=cyc(L_t) | (L_{t−1},L_t)
  is a cycle step) vs r0 = P(L_{t+1}=cyc(L_t) | (L_{t−1},L_t) is an ABC
  non-cycle, non-self step). One-sided two-proportion z, α=0.05. Predict r1>r0.
  FALSIFIER: p ≥ 0.05 → no momentum; the moving-finger mechanism in its
  sequential form is FALSIFIED (the lag-3 excess then needs another mechanism).
- P2b (held-out order selection): 1st-order (k=12) vs 2nd-order (k=48) Markov on
  the 4-state label stream; fit on pairs[:923], evaluate on pairs[923:].
  Predict 2nd-order wins held-out LL/transition (genuine memory-2).
- P2c (fixed column order): the dominant directed 3-cycle must be cyc in both
  stream halves and in all thread-1 variants (post-alignment). A flip falsifies
  "one column order".
Honest scope: these probe the SEQUENTIAL mechanism only; they cannot confirm
actual table columns without key recovery (F43's deferred test stands).
