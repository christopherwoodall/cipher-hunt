## rhythmicist: rotation recompute + robustness + phase-lock + HMM verdicts

- Context: I own recomputation and phase-lock for the rotation fleet. Work
  orders: (1) independently recompute phases/chi²/lag-3 with fresh code and run
  the labeling-robustness battery; (2) test whether anchor phrases phase-lock
  to the period; (3) 3-state HMM vs 96-group bigram, held-out BIC.
- Decision: WO1 VERIFIED (phase map exact, chi²=366.347, lag-3 z≈+5.3–5.8);
  WO1b battery FAILED (1/5 variants survive — only k=16); WO2 pre-registered
  tests VOID (design error: deterministic start-group→phase mapping), salvage
  INCONCLUSIVE lead (6/6 formula starts in {B,C}, null-dependent p=0.007–0.10);
  WO3 NO decisive HMM win (bigram wins held-out −4.2938 vs −4.3774; HMM wins
  BIC on parsimony only).
- Why: fresh code reproduced every banked number (T0 gate); the battery's 4
  failures all trace to degenerate partitions (giant cluster 55–82 groups)
  where "3 largest = ABC" is meaningless — only the k=16 refinement (agreement
  0.948) preserves the rotation; the HMM's hidden states recover A/B/C-like
  structure unsupervised yet still lose held-out to raw bigrams.
- Enlightenment: (1) the E1 "0.4219" construction needed pinning — it's lag-3
  pairs with BOTH ENDPOINTS in ABC (n=1,510), found independently 3 ways;
  (2) my own WO2 design was broken from the start and I caught it myself —
  exact repeats share start groups, so phase-lock-by-construction; (3)
  `np.argsort` tie-breaking silently breaks clustering reproduction —
  `Counter.most_common` insertion-order ties are required; (4) three
  phase-free memory tests all null (group lag-3 z=+0.15, trigram loses,
  skip-3 Δ=−0.0022) — the excess has no phase-free counterpart.
- For the report: rotation section. Numbers that matter: chi²=366.3 (perm max
  63.3); lag-3 z≈+5.3–5.8; battery 1/5 (k16 only); HMM held-out delta −0.0836
  (bigram wins), ΔBIC +59,824 (HMM); phase-lock inconclusive. Net implication:
  E1's "genuine process rhythm, not a labeling artifact" DOWNGRADED to
  partition-dependent structure — real given Jaccard-k12/k16, uncorroborated
  without it, no discourse coupling, not a better generative story.
- Caveats: battery instrument weakness (degenerate partitions) limits the
  "labeling artifact" reading — a better battery would test non-degenerate
  alternative partitions (bedrock's Hellinger k-means found the cycle
  independently); crowd6/segmenter thread 2 re-runs the HMM comparison with a
  different split — expect convergence; WO2 salvage is post-hoc, n=6.
