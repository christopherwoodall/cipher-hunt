# CONTACTOR — contact-chain analysis (R5005, Zeschau/Seebach 1841)

Counts re-verified vs data/attempt1_results.json: 1846 pairs / 96 distinct groups — exact match. Pairing via load_pairs() from code/crib_attack.py, not re-derived.

## Method
PRIMARY similarity: Jaccard on top-10 contact sets (10 most frequent predecessors ∪ 10 most frequent followers, raw counts). No smoothing, so rare groups are not artificially inflated toward each other. SECONDARY: cosine on Laplace-smoothed predecessor+follower distributions (kept for comparison; its neighbor ranks for low-frequency groups are smoothing noise). Agglomerative average-linkage in both cases.

## Pre-registered predictions
### P1: FAIL

34=i and 40=e (the two anchored vowel syllables) share contact patterns: 40=e should rank among the top-10 Jaccard contact neighbors of 34=i, and they should sit in the same cluster at the Jaccard k=12 cut.

- rank of 40=e among 34=i's top-10 Jaccard neighbors: None
- same Jaccard k=12 cluster: False (34=i in cluster A, 40=e in cluster B)
- Jaccard(34=i, 40=e) = 0.241
- 34=i's anchor similarities (desc): 46=que(0.267), 40=e(0.241), 11=la(0.194), 82=m(0.129), 70=pre(0.121), 87=ce(prov.)(0.086), 29=er(0.057)
- 40=e's anchor similarities (desc): 11=la(0.276), 34=i(0.241), 46=que(0.188), 70=pre(0.156), 82=m(0.129), 29=er(0.121), 87=ce(prov.)(0.118)

### P2: FAIL

87=ce (provisional, 4/5 checks) is function-word-like: its top Jaccard contact neighbors should include other anchored function words (11=la, 46=que, 29=er), or it should sit in the same Jaccard k=12 cluster as at least one of them.

- function-word anchors in 87's top-10 neighbors: []
- function-word anchors sharing 87's k=12 cluster: []
- same k=12 cluster as 82=m: True
- 87's anchor similarities (desc): 82=m(0.423), 46=que(0.176), 70=pre(0.147), 11=la(0.147), 40=e(0.118), 29=er(0.114), 34=i(0.086)
- 87's top-10 Jaccard neighbors: 82(0.423), 37(0.393), 47(0.379), 48(0.345), 86(0.300), 66(0.300), 43(0.290), 17(0.290), 80(0.286), 31(0.280)

## Strongest structural clusters (Jaccard, k=12)
- size 30, total-freq 642, anchors: [11=la, 34=i, 46=que, 70=pre]
  members: 01 06 11 14 16 30 32 33 34 35 36 38 39 43 44 46 48 61 63 64 66 68 70 81 83 84 86 92 93 94
  top followers: 29x36, 00x33, 24x28, 21x24, 59x23, 52x22
  top predecessors: 00x46, 82x33, 62x25, 87x23, 77x23, 12x20
- size 26, total-freq 511, anchors: [40=e, 82=m, 87=ce(prov.)]
  members: 02 07 12 15 19 20 21 31 37 40 42 45 47 49 53 60 62 65 69 71 74 80 82 85 87 89
  top followers: 48x24, 64x23, 16x23, 94x21, 06x20, 67x18
  top predecessors: 29x42, 24x35, 74x20, 21x17, 76x16, 52x15
- size 23, total-freq 560, anchors: [29=er]
  members: 03 08 09 17 23 24 26 29 41 50 51 52 56 59 67 76 77 78 79 88 91 96 98
  top followers: 87x25, 82x23, 37x21, 40x17, 77x15, 47x15
  top predecessors: 64x24, 11x23, 06x21, 86x18, 48x18, 67x17
- size 4, total-freq 77, anchors: [none]
  members: 00 55 95 97
  top followers: 86x13, 33x8, 66x7, 92x6, 46x6, 81x6
  top predecessors: 81x5, 11x5, 06x5, 16x5, 43x4, 63x4
- size 3, total-freq 6, anchors: [none]
  members: 04 22 57
  top followers: 20x1, 62x1, 61x1, 94x1, 42x1, 64x1
  top predecessors: 80x3, 85x1, 64x1, 20x1
- size 2, total-freq 2, anchors: [none]
  members: 27 90
  top followers: 46x1, 19x1
  top predecessors: 60x2

## The 3-phase rotation (block transitions at k=12)
Clusters A(30 members: 11=la,34=i,46=que,70=pre), B(26: 40=e,82=m,87=ce?), C(23: 29=er); R = residual small clusters.

P(next block | block):
- A (n=641): {'A': 0.237, 'B': 0.261, 'C': 0.418, 'R': 0.084}
- B (n=511): {'A': 0.476, 'B': 0.145, 'C': 0.301, 'R': 0.078}
- C (n=560): {'A': 0.295, 'B': 0.45, 'C': 0.211, 'R': 0.045}
- R (n=133): {'A': 0.617, 'B': 0.135, 'C': 0.143, 'R': 0.105}

3x3 (A,B,C) chi-square vs independence: chi2=181.3, df=4 (p << 1e-6 — the rotation is not chance).
- A->C: obs 268 vs exp 199.0 (x1.35)
- C->B: obs 252 vs exp 165.6 (x1.52)
- B->A: obs 243 vs exp 165.6 (x1.47)

## Anchor block signatures — P(next/prev block | anchor)
- 11=la: next {'A': 0.25, 'B': 0.11, 'C': 0.52, 'R': 0.11}, prev {'A': 0.3, 'B': 0.34, 'C': 0.27, 'R': 0.09}
- 29=er: next {'A': 0.02, 'B': 0.89, 'C': 0.09}, prev {'A': 0.77, 'B': 0.09, 'C': 0.13, 'R': 0.02}
- 34=i: next {'A': 0.1, 'B': 0.3, 'C': 0.6}, prev {'B': 0.5, 'C': 0.2, 'R': 0.3}
- 40=e: next {'A': 0.14, 'B': 0.24, 'C': 0.52, 'R': 0.1}, prev {'A': 0.14, 'B': 0.05, 'C': 0.81}
- 46=que: next {'A': 0.28, 'B': 0.24, 'C': 0.41, 'R': 0.07}, prev {'A': 0.1, 'B': 0.45, 'C': 0.21, 'R': 0.24}
- 70=pre: next {'A': 0.27, 'B': 0.4, 'C': 0.33}, prev {'A': 0.6, 'B': 0.13, 'C': 0.2, 'R': 0.07}
- 82=m: next {'A': 0.87, 'C': 0.13}, prev {'A': 0.34, 'B': 0.03, 'C': 0.61, 'R': 0.03}
- 87=ce(prov.): next {'A': 0.72, 'B': 0.03, 'C': 0.25}, prev {'A': 0.19, 'B': 0.03, 'C': 0.78}

## Anchor contact neighbors (Jaccard, top-8)
- 11=la (freq 44): 68(0.348), 80(0.346), 86(0.310), 64(0.310), 43(0.300), 40(0.276), 33(0.276), 02(0.267)
- 29=er (freq 47): 52(0.357), 96(0.310), 50(0.310), 78(0.300), 67(0.267), 79(0.258), 77(0.258), 76(0.258)
- 34=i (freq 10): 06(0.321), 16(0.310), 94(0.286), 36(0.280), 93(0.276), 86(0.276), 46(0.267), 14(0.267)
- 40=e (freq 21): 62(0.321), 80(0.308), 60(0.286), 11(0.276), 63(0.250), 34(0.241), 20(0.241), 71(0.240)
- 46=que (freq 29): 86(0.444), 43(0.290), 14(0.290), 34(0.267), 36(0.259), 09(0.258), 63(0.233), 96(0.219)
- 70=pre (freq 15): 79(0.258), 78(0.258), 43(0.258), 01(0.258), 44(0.233), 71(0.231), 86(0.226), 62(0.226)
- 82=m (freq 38): 87(0.423), 32(0.360), 42(0.308), 89(0.292), 86(0.286), 37(0.286), 80(0.269), 74(0.241)
- 87=ce(prov.) (freq 32): 82(0.423), 37(0.393), 47(0.379), 48(0.345), 86(0.300), 66(0.300), 43(0.290), 17(0.290)

## Anchor-pair Jaccard (desc)
82-87=0.423, 11-40=0.276, 34-46=0.267, 34-40=0.241, 11-70=0.226, 11-46=0.219, 11-34=0.194, 29-70=0.188, 40-46=0.188, 29-46=0.182

## Class-level inferences (hypotheses, not values)
- The group stream has a 3-phase rotational contact structure (A→C→B→A cycle, all three edges 1.4–1.6x over independence, chi2=~181, df=4). Shape matches syllable/word-position alternation, e.g. word-medial → word-final → word-initial.
- 29=er anchors phase C and itself flows A→29→B (prev A 0.77, next B 0.89): consistent with C being a word-final-ish phase — 'er' is the classic French infinitive/final syllable, and C→B is the word-boundary edge.
- 82=m and 87=ce? share the same structural role (both C→X→A: prev C 0.61/0.78, next A 0.87/0.72) and are each other's nearest anchor by Jaccard (0.423, the highest anchor-anchor value by far). Hypothesis: both are proclitic/onset-position syllables. This neither confirms nor kills 87=ce — 'ce' IS proclitic — but P2's expectation (cluster with la/que) failed.
- 40=e behaves C-adjacent (prev C 0.81, dominated by 29→40 'er-e' x9; next C 0.52) despite clustering in B: likely a word-final vowel position.
- 34=i flows B→34→C (prev B 0.50, next C 0.60): a phase-boundary vowel.
- Top collocations to chase: 82→16 (11/38), 24→87 (10/32), 29→40 (9/47), 87→11 (7/32), 00→86 (12/54).

## Verification
- 1846 pairs / 96 groups re-checked against data/attempt1_results.json: exact match.
- Pair stream from load_pairs() (upstream offsets); no re-derivation, no invented ciphertext.
- P1/P2 were pre-registered before the Jaccard run; both FAIL as stated — reported as-is (null results are first-class).
