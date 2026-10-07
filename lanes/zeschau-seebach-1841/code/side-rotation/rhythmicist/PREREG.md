# RHYTHMICIST pre-registration (2026-10-07, written BEFORE any computation)

Lane: `~/workspace/cipher-hunt/lanes/zeschau-seebach-1841/`. Worker: rhythmicist
(rotation fleet, coordinator rotation-fleet). Fresh code only — no imports from
`code/crowd5/rotation_mystery.py` (or `code/crowd/contactor.py`); the contactor's
published method description (Jaccard on top-10 contact sets, average-linkage
agglomeration, k=12 cut, 3 largest = A/B/C) is the spec I re-implement.

Canonical stream: `code/crowd4/repaired_parse.py::load_pairs_repaired`
(1,847 pairs, 96 groups). Reuse of the canonical *loader* is allowed; every
analysis function is written fresh.

## WO1 — independent recomputation

### T0 gate (must pass before any further claim)
1. Re-implement: for each group g, TOP[g] = {top-10 followers by raw count} ∪
   {top-10 predecessors by raw count} (set, ≤20); Jaccard similarity;
   agglomerative average-linkage (strictly-greater best-pair selection, first
   pair wins ties, merge appended at end); replay merges to k=12; 3 largest
   clusters → A/B/C by size, rest → R.
2. Phase map must EQUAL `code/crowd4/phase_map_repaired.json` on all 96 groups.
3. 3×3 ABC transition table (consecutive pairs t,t+1 with BOTH phases in
   {A,B,C}), chi² of independence on 4 df. Must equal **366.3 ± 1**.
4. Phase sequence s[0..1846] (labels A/B/C/R over all 1,847 tokens).
   rate(k) = #{i : s[i]=s[i+k]} / (1847−k).
   Target: rate(3) = 0.4219 (segmenter E1).
   Null: fitted first-order Markov chain over the 4 phase labels
   (P[b|a] from the 1,846 observed transitions; π = token marginals).
   Expected rate(3) = Σ_a π_a (P³)_{aa}. Target: 0.3530.
   z: 10,000 surrogate sequences (s_0 ~ π, then Markov(P)), rate(3) each;
   z = (obs − mean)/sd. Target: z ≈ +5.6. Also lag-2 z (target ≈ −3.18).
   DECISION: rhythm verified iff z_lag3 ≥ +3.5 (one-sided) AND |chi² − 366.3| ≤ 1
   AND phase map exact match.

### WO1b — labeling-robustness battery (segmenter's queued test #1)
Variants (each: fresh clustering → 3 largest = ABC, rest R → chi² on ABC 3×3
→ lag-3 rate + Markov z with the identical T0 pipeline):
- V1 cosine: contactor-style smoothed 192-dim contact vectors
  (pred+1)/(Σpred+96) ‖ (foll+1)/(·foll+96), L2-normalized; cosine similarity;
  same agglomeration, k=12.
- V2 k=8 Jaccard; V3 k=16 Jaccard (same pipeline as canonical).
- V4 first-half clustering (pairs[0:923]); V5 second-half (pairs[923:1847]).
  Groups with zero occurrences in the clustering half are forced to R after
  the cut. Labels evaluated on the FULL stream.
"Rotation survives" per variant: chi² > 30 (df=4) AND z_lag3 ≥ 3.0 with
obs > expected. DECISION: battery PASSED iff all 5 variants survive.
Membership fragility: best-permutation (6 ABC perms, R fixed) label agreement
of each variant vs canonical; "fragile" iff mean agreement < 0.85.
Claimed package = structure robust + membership fragile.

### Old-vs-new discrepancy reconciliation (side result)
Recompute old-parse (upstream offsets) Jaccard-k12 labels, best-permutation
agreement vs repaired labels. If 69/96 → N30's "61/96 change" is superseded;
if 35/96 → matches N30, E4's 69/96 needs explanation.

## WO2 — phase-lock test (segmenter's queued question; NEW)
Phrases (positions re-derived from the repaired stream; counts asserted):
L1 "la première" 11 70 82 34 29 40 ×2 (@754/@1034);
L2 96 87 46 ×3; L3 24 87 64 ×3; L4 77 78 94 82 06 ×2;
L5 64 96 43 87 01 ×2; L6 56 69 26 00 33 21 64 37 01 ×2.
p_i = token phase marginals (A/B/C/R) from the verified map. α=0.05.
- Test A (pooled, pre-registered decision test): 14 start phases; chi² GOF
  vs 14·p_i (df=3). p<0.05 → phrases lock to the rhythm.
- Test B (per-set, descriptive): for each set, P(all n starts same phase)
  = Σ_i p_i^n; report how many sets are all-same (no per-set decision).
- Test C (L1 exact 6-sequence lock): both 6-length phase strings identical?
  Chance = (Σ_i p_i²)^6. Report.
Pre-registered interpretation:
- Lock (A significant) → rhythm interacts with discourse units: either the
  encipherer aligned formula starts to a process cycle (table-rotation habit),
  or phases mark a linguistic unit the formulas respect. Process-vs-language
  reading must then be revisited.
- No lock → rhythm is discourse-independent: favors process geometry over
  language-driven explanations; the tuner NULL (N15) stands unchallenged.

## WO3 — 3-state HMM vs 96-group bigram (segmenter's queued test #2)
- Data: group token sequence t[0..1846]. Split (pre-registered, contiguous):
  train t[0:923] (923 tokens), test t[923:1847] (924 tokens).
- M1 HMM-3: Baum-Welch from scratch, 11 restarts (10 random with seed
  20261007+i, 1 phase-informed: emissions ∝ phase-cluster counts + ε),
  200 iters or ΔLL < 1e-6. ε-floor 1e-6 on A and B post-EM, renormalized.
  k_params = 2 + 6 + 3·95 = 293.
- M2 bigram-96: P(g'|g) = (count+1)/(row+96) Laplace α=1. k = 96·95 = 9120.
- Metrics: (i) held-out mean log-likelihood per next-token on test
  (HMM via forward algorithm); (ii) BIC on train: −2·LL_train + k·ln(922).
DECISION: "HMM wins decisively" iff held-out LL/pos(HMM) > held-out
LL/pos(bigram) AND ΔBIC = BIC_bigram − BIC_HMM > 10. Split outcomes reported
honestly, not rounded to a win.

## Amendment A1 (2026-10-07, during T0 — method discovery, no numbers changed by hand)

The segmenter's E1 headline numbers (lag3=0.4219, Markov-expected=0.3530,
chance=0.3366) do NOT reproduce under the primary full-sequence 4-state
pipeline: fresh recompute gives lag3=0.3579, expected=0.2953, chance=0.2839,
z=+5.29. The E1 numbers reproduce exactly under an ABC-restricted pipeline
(R-phase tokens dropped from the phase sequence before computing rates and
fitting the 3-state Markov chain): "chance 0.3366" = sum p_i^2 over the
ABC-restricted token marginals. Both pipelines show the same phenomenon
(z=+5.29 full-sequence, z=+5.6 E1-pipeline); the E1 pipeline compresses the
timeline by deleting R positions. Primary decision pipeline stays the
pre-registered full-sequence one; the E1 pipeline is reported as the
verification-of-E1 secondary. Red-team gate checks both.

## Amendment A2 (2026-10-07, after WO2 ran — design error found and disclosed)

WO2 Tests A/B/C as pre-registered are VOID: phase is a deterministic function
of group, and exact-repeat phrases share their start group, so "all
occurrences start on the same phase" holds with probability 1 BY CONSTRUCTION
(Test C's "identical 6-phase strings" likewise). The p=0.0007 Test A number is
discarded with the framing. Salvage (POST-HOC, exact tests per shared-redteam
ruling R-2): 6 distinct formula-initial groups start on B,C,C,C,B,C (6/6 in
{B,C}); uniform-group null p=0.0093 (exact GOF 0.0070), frequency-matched
permutation p=0.0490, token-marginal null p=0.0338 (exact GOF 0.1020) —
INCONCLUSIVE (null-dependent, post-hoc, n=6), lead-grade at best.

## Amendment A3 (2026-10-07, after WO1b ran — battery interpretation)

The pre-registered "3 largest clusters = ABC" convention is meaningless under
the degenerate partitions 4/5 variants produce (giant cluster 55–82 groups).
The battery as specified is a weak instrument; the informative residue is that
only partitions ≈ canonical (k=16, agreement 0.948) preserve the rotation.
Claimed package "transition structure robust, membership fragile" NOT
supported — the transition structure is partition-dependent. Converges with
crowd6/segmenter thread 1 (verdict_robust=false). Also adopted: shared-redteam
R-4 reconciliation (69/96 best-perm; N30's 61/96 = naive identity).

## Red-team gate
`redteam_verify.py` re-derives headline numbers via an independently written
code path (no shared functions with rhythm.py beyond the canonical loader):
parse asserts, phase-map equality, chi² via scipy.stats.chi2_contingency,
lag-3 rate via vectorized numpy. Any disagreement → investigate, never average.

## Status markings
GT anchors: 11=la,70=pre,82=m,34=i,29=er,40=e,46=que. All work here is
cipher-internal (F30-legal); no era corpus is used anywhere in this work order.
