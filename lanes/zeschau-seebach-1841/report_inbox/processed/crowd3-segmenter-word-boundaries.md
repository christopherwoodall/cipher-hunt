## segmenter: word-boundary hypothesis (round 3, crowd3)

- Context: hypothesize word boundaries over the 1,846-pair stream to give
  round 4 crib-drag targets. Signals: (S1) rotation-break edge model —
  boundaries *break* the A→C→B→A rotation (never assuming phase = word
  position, per the tuner's NULL verdict); (S2) era word-length prior from
  Tocqueville 1835/1840 (221,188 words, R1 syllabifier, mean 1.75 syll/word);
  (S3) prior-only control. The structural model is unsupervised: per-row
  boundary rates pi_a fit by EM on forward-backward posteriors (14 iters,
  damped, converged, no degeneracy). Anchor spans used ONLY for validation
  (fully out-of-sample for the primary model). Anchor-trained FULL/STRICT
  variants shown for comparison (in-sample, circular).
- Decision: verdict PARTIAL. Ship the STRUCT-EM segmentation as a LEAD-grade
  hypothesis (segmenter_results.json: full 1,845-position confidence array,
  Viterbi bounds, 25 crib-drag targets). Do NOT promote to a decode map.
- Why: the only ground-truth checkpoint passes cleanly and out-of-sample —
  "la"+"premiere" @1033: boundary in 0.727, la|premiere split 0.937
  (the model discovered the two-word split unprompted), boundary out 0.608;
  3/3 GT boundaries >=0.5 (mean 0.757), 3/4 internals <0.5. MAP length
  distribution is sane: 958 words, mean 1.93 vs era 1.75, median 1 vs 1
  (chi2 121.8 vs 1446.2 for the degenerate prior-only control). EM found
  pi_C=0.578 highest — edges leaving C-phase groups are most often
  boundaries, matching 29=er as word-final-ish, without being told.
  BUT: boundary recall on the provisional anchor spans is 8/26 (mean 0.478),
  at/below the model's own 0.501 base rate — the segmentation does not
  confirm the cela/parce-que boundaries. Either the provisional reads
  (87=ce, 96=par) are off, or the rotation-break signal is too weak there.
  One internal false positive: pre|mi @1035 (0.654).
- Enlightenment: two things. (1) The naive mixture model over-joins badly
  (mean 3.7 syll/word); decontaminating the mixture via EM
  (M = (1-pi)*P_within + pi*P_boundary per row) fixed it with zero anchor
  data — the rotation really does carry boundary information. (2) Cela
  internals (87|11) all score <0.5 (mean ~0.40): the segmentation mildly
  favors "cela" as ONE word over the "ce la" two-word alternative.
- For the report: "Word-boundary hypothesis" section. Numbers that matter:
  GT checkpoint 3/3 boundaries (0.727/0.937/0.608), internals 3/4;
  all-spans 8/26 boundaries, 13/14 internals; MAP 958 words mean 1.93
  (era 1.75), chi2 121.8; EM pi = A .572 / B .537 / C .578 / R .493.
  Top crib-drag targets: @1110-1112 [41 65 38] and @81-83 [51 62 16],
  both clean C→B→A rotation words, flank conf ~0.93-1.0.
- Caveats: rotation-break is an assumption, unproven — the tuner NULL
  (phase != word-position) still stands and this does not rescue it.
  s=+12.5 for B->B / R->C is an EPS-floor artifact (the "B->B never occurs
  within a word" claim is qualitatively robust, its magnitude is not).
  Model over-produces 4-syllable words (14.2% vs era 6.5%). Weak
  provisional-word recall may indict the 87=ce/96=par reads rather than the
  model. Length prior is orthographic French; the cipher syllabary remains
  uncalibrated against it. A segmentation is a LEAD, not a promotion —
  no crack claim.
