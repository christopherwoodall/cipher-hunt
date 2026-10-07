# SEGMENTER — word-boundary hypothesis (round 3, crowd3)

Semi-Markov forward-backward. score(j->i) = logP_len(k) + sum within-edge weights + rotation-break bonus on the word-final edge.

Counts: 1846 pairs / 96 groups; era corpus 221188 words (mean 1.75 syll/word); cela x7, parce-que x3.

## Rotation-break edge signal (STRUCT, unsupervised)
- R->C: s=+12.62 (boundary-favoring)
- B->B: s=+12.53 (boundary-favoring)
- R->B: s=+4.12 (boundary-favoring)
- C->R: s=+1.98 (boundary-favoring)
- A->A: s=+1.36 (boundary-favoring)
- C->C: s=+1.27 (boundary-favoring)
...
- C->B: s=-0.90 (within-favoring)
- R->A: s=-0.90 (within-favoring)
- R->R: s=-0.70 (within-favoring)
- A->C: s=-0.63 (within-favoring)
- B->A: s=-0.58 (within-favoring)
- A->R: s=-0.35 (within-favoring)

## Validation: boundary precision on anchor spans
- STRUCT vs ground-truth spans: boundary 3/3>=0.5 (mean 0.757); internal 3/4<0.5 (mean 0.412)
- STRUCT vs all anchor spans: boundary 8/26>=0.5 (mean 0.478); internal 13/14<0.5 (mean 0.380)
- ANCHOR-FULL (in-sample): boundary 18/26>=0.5 (mean 0.616); internal 12/14<0.5 (mean 0.222)
- ANCHOR-STRICT (in-sample): boundary 3/3>=0.5 (mean 0.802); internal 4/4<0.5 (mean 0.337)
- PRIOR-ONLY: boundary 26/26>=0.5 (mean 0.571); internal 0/14<0.5 (mean 0.571)

## la premiere checkpoint @1033 (STRUCT)
- in @1033: 0.7266, la|premiere @1034: 0.9365
- premiere internals @1035-1038: [0.6536, 0.3837, 0.3426, 0.2677]
- out @1039: 0.6079

## Implied word-length distribution (MAP) vs era
- era: mean 1.75, dist(1..6)=[124031, 49637, 29897, 14325, 2956, 325]
- STRUCT_MAP: n=958, mean 1.927, median 1, chi2 121.8, dist(1..6)=[513, 148, 156, 136, 5, 0]
- ANCHOR_FULL_MAP: n=1351, mean 1.366, median 1, chi2 206.2, dist(1..6)=[985, 237, 129, 0, 0, 0]
- ANCHOR_STRICT_MAP: n=959, mean 1.925, median 1, chi2 65.2, dist(1..6)=[490, 214, 130, 87, 38, 0]
- PRIOR_ONLY_MAP: n=1846, mean 1.0, median 1, chi2 1446.2, dist(1..6)=[1846, 0, 0, 0, 0, 0]

## Top unread high-confidence words (STRUCT MAP — crib-drag targets)
- @1579-1580 (2g): 24 53 [CB] flank=[0.914, 1.0] inner=0.269 score=0.6685
- @1552-1554 (3g): 99 13 93 [RRA] flank=[0.979, 0.934] inner=0.285 score=0.6679
- @837-838 (2g): 98 20 [CB] flank=[0.903, 1.0] inner=0.265 score=0.663
- @453-454 (2g): 77 60 [CB] flank=[0.902, 1.0] inner=0.265 score=0.6626
- @1566-1567 (2g): 24 74 [CB] flank=[0.9, 1.0] inner=0.265 score=0.6618
- @1842-1843 (2g): 78 49 [CB] flank=[0.902, 1.0] inner=0.268 score=0.6604
- @960-962 (3g): 00 86 56 [RAC] flank=[0.976, 0.935] inner=0.295 score=0.6592
- @1670-1671 (2g): 55 81 [RA] flank=[0.974, 0.919] inner=0.283 score=0.6588
- @1601-1602 (2g): 00 44 [RA] flank=[0.974, 0.914] inner=0.28 score=0.6579
- @210-211 (2g): 88 19 [CB] flank=[0.899, 1.0] inner=0.268 score=0.6578
- @478-481 (4g): 45 93 00 13 [BARR] flank=[1.0, 1.0] inner=0.346 score=0.654
- @407-408 (2g): 00 33 [RA] flank=[0.973, 0.908] inner=0.28 score=0.6531
