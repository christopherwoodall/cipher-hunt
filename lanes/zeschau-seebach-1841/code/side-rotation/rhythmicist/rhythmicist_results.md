# RHYTHMICIST — results (2026-10-07)

Worker: rhythmicist (rotation fleet). Scope: `code/side-rotation/rhythmicist/`.
Pre-registration: `PREREG.md` (amendments A1–A3 appended there).
Red-team gate: `redteam_verify.py` — ALL PASS (independent code path).

## WO1 — independent recomputation: VERIFIED

Fresh re-implementation of the contactor's spec (Jaccard on top-10 contact
sets, average-linkage, k=12, 3 largest = A/B/C). No imports from
`rotation_mystery.py` or `contactor.py`.

- **Phase map: EXACT match** on all 96 groups vs
  `code/crowd4/phase_map_repaired.json` (sizes A=32/B=27/C=17/R=20).
- **chi² = 366.347** on the ABC 3×3 (n=1,514 transitions, df=4) — within ±1 of
  the banked 366.3. Table: A:[108,298,141] B:[163,97,258] C:[280,121,48]
  (rows from-A/B/C, cols to-A/B/C). Repaired labels: A→B 0.545, B→C 0.498,
  C→A 0.624.
- **Lag-3 excess verified under two null pipelines:**
  - Primary (pre-registered, full-sequence 4-state): obs=0.3579,
    Markov-exp=0.2953, z=**+5.29** (10,000 surrogates).
  - E1-exact construction (pinned independently — 3rd derivation after
    crowd6/segmenter A1 and the geometer): lag-3 pairs with BOTH ENDPOINTS in
    ABC (n=1,510): obs=**0.4219 exact**, exp≈0.349–0.353
    (residual conditioning ambiguity, disclosed), z=**+5.2–5.8**.
  - Lag-2: z=−2.62 (full-seq), same direction as banked −3.18.
- **Block structure is partition-real:** 366.3 vs max 63.3 over 2,000 random
  label permutations (sizes held) — the specific assignment matters.
- **Discrepancy reconciled** (adopts shared redteam R-4): N30's "61/96 change"
  = naive identity agreement (35/96); N37's 69/96 = best-permutation agreement
  (the correct clustering number). 28% membership change, not 63.5%.
- Methodology lesson: `np.argsort` (unstable quicksort) tie-breaking in top-k
  contact sets SILENTLY breaks exact reproduction; `Counter.most_common`
  (insertion-order ties) is required. A first battery run on the buggy
  pipeline was voided and re-run.

## WO1b — labeling-robustness battery: FAILED (1/5 survive)

Pre-registered rule: all 5 variants must show chi²>30 AND lag-3 z≥3.0.

| Variant | chi² | lag-3 z | agree | sizes (top) | Survive |
|---|---|---|---|---|---|
| V1 cosine k=12 | 12.9 | +0.51 | 0.344 | [82,4,1,…] degenerate | NO |
| V2 jaccard k=8 | 9.7 | +0.20 | 0.448 | [76,5,4,…] degenerate | NO |
| V3 jaccard k=16 | 354.9 | +4.71 | 0.948 | [32,23,16,…] | YES |
| V4 half-stream 1 | 84.8 | +0.28 | 0.406 | [55,6,6,…] degenerate | NO |
| V5 half-stream 2 | 16.2 | +0.23 | 0.458 | [64,8,4,…] degenerate | NO |

- **Converges with crowd6/segmenter thread 1** (independent battery,
  `verdict_robust=false`; their V_k16 agreement 91/96 = my 0.948; same
  degenerate sizes). Two independent derivations, same verdict.
- Interpretation (honest): 4/5 variants yield DEGENERATE partitions (one
  giant cluster), so the pre-registered "3 largest = ABC" convention tests a
  meaningless partition there — the battery as specified is a weak instrument.
  The informative residue: only partitions ≈ the canonical one (k=16,
  agreement 0.948) preserve the rotation. The claimed package — "transition
  structure robust while cluster membership is fragile" — is **NOT supported**:
  the transition structure is partition-dependent.
- **Phase-free corroboration (post-hoc, all null):** group-level lag-3
  same-group z=+0.15 (obs 0.0174 vs Markov-exp 0.0169); held-out trigram vs
  bigram: trigram LOSES (−4.4987 vs −4.2934); skip-3 predictive test
  (does g[t] help predict g[t+3] given g[t+1],g[t+2]): Δ=−0.0022. The excess
  has NO phase-free counterpart.
- Net: E1's "genuine process rhythm, not a labeling artifact" is **DOWNGRADED**
  to **partition-dependent sequential structure**. Real given the
  Jaccard-k12(/k16) partition; not corroborated without it.

## WO2 — phase-lock: PRE-REGISTERED TESTS VOID + post-hoc INCONCLUSIVE lead

- **Tests A/B/C are VOID (design error, retracted as tests):** phase is a
  deterministic function of group, and exact-repeat phrases share their start
  group, so "all occurrences start on the same phase" holds with P=1 BY
  CONSTRUCTION. Test C's "identical 6-phase strings" likewise. Caught and
  reported per lane honesty norms; the p=0.0007 Test A number is discarded
  with the framing.
- **Salvage (POST-HOC, exact tests per redteam R-2 amendment):** the 6
  DISTINCT formula-initial groups (11, 96, 24, 77, 64, 56) start on phases
  B,C,C,C,B,C — 6/6 in {B,C}, 0 in A/R. Positions re-derived from the
  repaired stream: L1 [754,1034], L2 [224,952,1526], L3 [179,1766,1774],
  L4 [1180,1351], L5 [341,1025], L6 [932,1626] (all consistent with the
  REINDEX.md +1 rule).
  - Uniform-over-groups null: p=0.0093 (all-same) / exact GOF p=0.0070.
  - Frequency-matched permutation: p=0.0490.
  - Token-marginal null: p=0.0338 / exact GOF p=0.1020.
  - **Verdict: INCONCLUSIVE** — signal is null-dependent, post-hoc, n=6.
  Lead-grade at best.
- Implication: NO evidence the rhythm interacts with discourse units. The
  tuner NULL (N15) stands unchallenged.

## WO3 — 3-state HMM vs 96-group bigram: NO DECISIVE HMM WIN

Pre-registered: contiguous split train pairs[0:923] / test pairs[923:1847];
11 restarts (10 random seed 20261007+i + 1 phase-informed); eps-floor 1e-6.

- Held-out LL/position: bigram **−4.2938** > HMM −4.3774 (bigram wins by
  0.0836/position).
- BIC (train, n=922): HMM 9,418.3 << bigram 69,242.6 (ΔBIC=+59,824 for HMM —
  pure parsimony bonus; bigram fits 9,120 params on 922 transitions).
- Pre-registered rule required BOTH → **no decisive HMM win**. The 3-state
  structure is NOT a better generative story than raw bigrams by held-out
  likelihood.
- Notable (non-verdict): Baum-Welch **recovers phase-like states
  unsupervised** — state1≈A (0.719 posterior mass), state2≈B (0.597),
  state0≈C (0.437). The partition captures real transition structure even
  though the HMM doesn't out-predict the bigram.
- Duplication note: crowd6/segmenter thread 2 runs the same comparison
  (split 1231/616, MAP-EM, +M_phm middle rung); their first attempt DIVERGED
  (testLL/trans=−332) and is being re-run — mine (eps-floor) converged.
  Complementary; expect convergence on "no HMM win."

## What the rhythm's structure implies (net)

1. The rotation is real **given** the Jaccard-k12(/k16) partition: chi²=366.3
   (permutation max 63.3), lag-3 excess z≈+5.3–5.8 under two null pipelines,
   momentum confirmed independently (crowd6 P2a: r1=0.6327 vs r0=0.4856,
   z=4.77).
2. It is **not labeling-robust** (battery 1/5), has **no phase-free
   corroboration** (three nulls), does **not interact with discourse units**
   (phase-lock void/inconclusive; N15 stands), and is **not a better generative
   story** than raw bigrams (HMM loses held-out).
3. The table-geometry hypothesis stays the live mechanism, now constrained:
   whatever the process is, it produces a **partition-dependent** period-3
   excess with momentum but no discourse coupling and no group-level memory.
   Bedrock's independent Hellinger k-means recovery (chi²=555.4, agree 0.75)
   shows a different geometry CAN find it — the degeneracy is specific to
   average-linkage under perturbed inputs, not proof of artifact.

## Files

- `code/side-rotation/rhythmicist/PREREG.md` (pre-registration + amendments)
- `code/side-rotation/rhythmicist/rhythm.py` (T0 fresh recompute)
- `code/side-rotation/rhythmicist/robustness.py` → `robustness_results.json`
  (+ `robustness_run2.log`)
- `code/side-rotation/rhythmicist/phaselock.py` → `phaselock_results.json`
  (void framing) ; `phaselock_posthoc.py` → `phaselock_posthoc.json`
- `code/side-rotation/rhythmicist/phasefree.py` → `phasefree_results.json`
- `code/side-rotation/rhythmicist/hmm_compare.py` → `hmm_results.json`
  (+ `hmm_run2.log`)
- `code/side-rotation/rhythmicist/redteam_verify.py` — ALL PASS
- `code/side-rotation/rhythmicist/rhythmicist_results.md` (this file)
- `code/side-rotation/report_inbox/rhythmicist-rotation-verdicts.md`
  (report-inbox note)
