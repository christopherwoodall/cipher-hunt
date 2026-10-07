# Verifier B ledger — independent re-derivation (2026-10-07)

Method: stdlib-only Python written from scratch; lane code never imported. Primary sources: data/upstream-ct_R5005.digits.txt, data/upstream-offsets.json, code/side-keyhunt/repaired_offsets.json. code/crowd4/phase_map_repaired.json used for comparison only. Offset convention C1 (per-row independent pairing, drop phase-inconsistent digit) is FORCED by (3764-2*1847)=70 and validated by exact positional reproduction; carry-over alternative falsified.
Clustering: k-means k=3 on concat(predecessor, successor) row-normalized contact profiles with HELLINGER geometry (euclidean on sqrt(p) — the natural metric for distributions); cosine variant as robustness. Plain euclidean on simplex vectors degenerates (documented). Seed 1841, 40 restarts, best inertia kept.

## repair_diff: PASS
- claimed: a5_03: 1->0 only
- computed: {'a5_03': (1, 0)}

## n_digits: PASS
- claimed: 3764
- computed: 3764

## dropped_distribution: PASS
- claimed: 70 dropped total (=> 1847 pairs)
- computed: {'total': 70, 'per_row_values': {0: 21, 1: 28, 2: 21}}
- notes: Per-row drops are NOT all 1: even-length rows with offset 0 drop 0, even-length rows with offset 1 drop 2, odd-length rows drop 1. Only the total (70) is constrained by (3764-2*1847).

## n_pairs: PASS
- claimed: 1847
- computed: 1847

## n_groups: PASS
- claimed: 96
- computed: 96
- notes: codes span 00..99; absent: [5, 25, 72, 75]

## alt_convention_pairs: PASS
- claimed: carry-over must NOT give 1847
- computed: 1866
- notes: carry-over gives 1866 pairs; only C1 reproduces 1847.

## rowspan_a5_03: PASS
- claimed: pair 754 lies on row a5_03
- computed: (748, 774)
- notes: F32: 754 is 'the manuscript gloss line a5_03' — validates row-id ordering.

## rowspan_a6_03: PASS
- claimed: pair 1034 lies on row a6_03
- computed: (1020, 1045)

## la_premiere_positions: PASS
- claimed: [754, 1034]
- computed: [754, 1034]
- notes: 0-based pair indices; exactly two occurrences in the stream.

## gt_all_six_at_both: PASS
- claimed: each of 11,70,82,34,29,40 at 754+i and 1034+i
- computed: all 12 positions hold
- notes: Positional claim verified. All six are ground-truth pencil anchors; the VALUE assignments (la/pre/m/i/er/e) rest on the manuscript, not on digit statistics.

## euclid_collapse_demo: INFO
- claimed: INFO: euclidean k-means on raw profiles degenerates
- computed: {'sizes': [2, 22, 72], 'chi2': 138.2}
- notes: Plain euclidean distance on simplex vectors lumps 94/96 groups into one cluster — wrong geometry for distributions. Documents a pitfall, not the structure.

## independent_3phase: PASS
- claimed: 3 clusters emerge with rotational transitions
- computed: {'sizes': [26, 26, 44], 'chi2': 555.4, 'df': 4, 'p': '6.92e-119', 'cycles': {'0->1->2->0': 1.766, '0->2->1->0': 0.696, 'self_mass': 0.538}}
- notes: Hellinger k-means (k=3, seed 1841, 40 restarts) finds balanced clusters with a dominant directed 3-cycle and suppressed self-transitions. df=(3-1)(3-1)=4, independence null on the 3x3 phase-transition table. Full table: {'P': [[0.166, 0.694, 0.14], [0.227, 0.297, 0.477], [0.596, 0.329, 0.075]]}

## independent_3phase_robustness: PASS
- claimed: cosine variant agrees
- computed: {'sizes': [27, 34, 35], 'chi2': 561.3, 'cycles': {'0->1->2->0': 0.71, '0->2->1->0': 1.766, 'self_mass': 0.524}}
- notes: Same features, cosine distance: independent geometry, same qualitative outcome.

## rotation_chi2_claimed: PASS
- claimed: 366.3 on 4df (repaired parse)
- computed: {'chi2': 366.3, 'df': 4, 'p': '5.18e-78', 'n_transitions': 1514, 'P': [[0.197, 0.545, 0.258], [0.315, 0.187, 0.498], [0.624, 0.269, 0.107]]}
- notes: Reproduced to the decimal under the lane's own labels (A/B/C groups only, n=1514 transitions). df=(3-1)(3-1)=4, independence null. Cycle under the lane's labels: A->B (0.545), B->C (0.498), C->A (0.624) — note this is A->B->C->A, whereas the OLD-parse F11 claim was A->C->B->A; direction labels are parse/labeling-relative.

## lag3_raw_index_autocorr: INFO
- claimed: INFO: raw group codes are arbitrary; rhythm is in phase space
- computed: {1: (0.0258, 1.11), 2: (-0.0283, -1.22), 3: (0.0025, 0.11), 6: (0.0094, 0.4)}
- notes: No lag-3 signal in raw code autocorrelation (z~0.1) — expected, since group numbers are arbitrary labels. The period-3 claim is about phases.

## lag3_samephase_independent: PASS
- claimed: period-3 rhythm: lag-3 z ~ +5
- computed: {'obs': 0.4344, 'exp_markov': 0.3824, 'z': 4.6}
- notes: Phases from MY independent hellinger clusters. z=(obs-exp)/se with binomial se under the fitted first-order Markov null.

## lag3_samephase_lane_labels: PASS
- claimed: 0.4219 vs 0.3530 Markov-expected, z=+5.6
- computed: {'obs': 0.4048, 'exp_markov': 0.3491, 'z': 4.77}
- notes: Diagnostic under the lane's labels (A/B/C positions only). Reproduces the significance (z~+5) but not the exact decimals (obs 0.405 vs 0.422); residual gap likely from R-class handling or label version. p~1e-6..1e-8.

## phase_agreement: INFO
- claimed: fraction of groups agreeing with claimed map
- computed: {'agree_all96': 0.594, 'agree_nonR_76': 0.75, 'align_perm': (1, 2, 0), 'R_split': {'C': 12, 'B': 3, 'A': 5}}
- notes: Permutation chosen to MAXIMIZE agreement — this inflates the fraction; read as an upper bound. R (20 groups) has no counterpart in a 3-cluster solution and counts as disagreement in all-96. Lane's own fragility flag: 61/96 groups changed phase between old and repaired parses.

## anchor_g11: PASS
- claimed: group exists (GT-pencil)
- computed: 45
- notes: Existence: verifiable above. Value 'la' rests on the erased pencil crib / lane inference — NOT independently verifiable from digit statistics.

## anchor_g70: PASS
- claimed: group exists (GT-pencil)
- computed: 15
- notes: Existence: verifiable above. Value 'pre' rests on the erased pencil crib / lane inference — NOT independently verifiable from digit statistics.

## anchor_g82: PASS
- claimed: group exists (GT-pencil)
- computed: 39
- notes: Existence: verifiable above. Value 'm' rests on the erased pencil crib / lane inference — NOT independently verifiable from digit statistics.

## anchor_g34: PASS
- claimed: group exists (GT-pencil)
- computed: 11
- notes: Existence: verifiable above. Value 'i' rests on the erased pencil crib / lane inference — NOT independently verifiable from digit statistics.

## anchor_g29: PASS
- claimed: group exists (GT-pencil)
- computed: 45
- notes: Existence: verifiable above. Value 'er' rests on the erased pencil crib / lane inference — NOT independently verifiable from digit statistics.

## anchor_g40: PASS
- claimed: group exists (GT-pencil)
- computed: 21
- notes: Existence: verifiable above. Value 'e' rests on the erased pencil crib / lane inference — NOT independently verifiable from digit statistics.

## anchor_g46: PASS
- claimed: group exists (GT-pencil)
- computed: 29
- notes: Existence: verifiable above. Value 'que' rests on the erased pencil crib / lane inference — NOT independently verifiable from digit statistics.

## anchor_g87: PASS
- claimed: group exists (provisional)
- computed: 32
- notes: Existence: verifiable above. Value 'ce' rests on the erased pencil crib / lane inference — NOT independently verifiable from digit statistics.

## anchor_g64: PASS
- claimed: group exists (provisional)
- computed: 47
- notes: Existence: verifiable above. Value 'qui' rests on the erased pencil crib / lane inference — NOT independently verifiable from digit statistics.

## anchor_g96: PASS
- claimed: group exists (provisional)
- computed: 21
- notes: Existence: verifiable above. Value 'par' rests on the erased pencil crib / lane inference — NOT independently verifiable from digit statistics.

## anchor_g77: PASS
- claimed: group exists (provisional-conditioned)
- computed: 44
- notes: Existence: verifiable above. Value 'le' rests on the erased pencil crib / lane inference — NOT independently verifiable from digit statistics.

## count_g87: PASS
- claimed: 32
- computed: 32

## count_g64: FAIL
- claimed: 46
- computed: 47
- notes: STALE-CLAIM: claimed value matches the OLD (pre-repair, 1846-pair) parse exactly (old n64=46); repaired parse gives 47. The lane's count claim was not re-derived after F32.

## count_g96: PASS
- claimed: 21
- computed: 21

## count_g11: FAIL
- claimed: 44
- computed: 45
- notes: STALE-CLAIM: claimed value matches the OLD (pre-repair, 1846-pair) parse exactly (old n11=44); repaired parse gives 45. The lane's count claim was not re-derived after F32.

## count_g46: PASS
- claimed: 29
- computed: 29

## count_g77: INFO
- claimed: no explicit n77 count claim found in NOTES.md
- computed: 44
- notes: Searched NOTES.md: only transition counts mention 77 (67->77 x6, 77->78 x7). n77=44 under both parses. 77=le is provisional-conditioned — value rests on lane inference, not verifiable here.

## a8_05_ends_46: PASS
- claimed: row a8_05 ends with group 46 at pair idx 1692
- computed: span=(1666,1693), last=46
