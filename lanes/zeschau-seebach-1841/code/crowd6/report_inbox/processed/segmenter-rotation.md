## segmenter: rotation round-6 follow-ups (threads 1–4)

- Context: Round 5 left the rotation as a genuine period-3 sequential rhythm
  (F43: lag-3 z=+5.6) with all linguistic meanings killed and column geometry
  as the leading hypothesis. Four pre-registered follow-ups, all run on the
  repaired 1,847-pair stream, cipher-internal only. Pre-registration (with
  amendments A1–A3): `code/crowd6/segmenter/PREREG.md`. Code:
  `rotation_r6.py` (threads 1/3/4), `hmm_test.py` (thread 2); results merged
  in `rotation_r6.json`.
- Decision: four verdicts —
  (1) labeling-robustness: FRAGILE by the pre-registered bar, with a precise
  diagnosis (below); (2) 3-state HMM vs 96-group bigram on held-out: NO, the
  HMM does not win (testLL/trans −4.2638 vs −4.2356; BIC 12,009 vs 74,105 —
  the AND-bar fails); (3) the 69/96 vs "61/96 change" discrepancy:
  RECONCILED, both numbers correct, different comparisons; (4) column
  geometry: MIXED — momentum SUPPORTED (P2a), full memory-2 null (P2b),
  fixed column order holds on reference labels (P2c).
- Why:
  - T1: gate reproduced F43's E1 EXACTLY (obs=0.4219, z=5.81 vs banked 5.6)
    only after pinning the construction round 5 never archived: lag-3 pairs
    with BOTH endpoints in ABC (n=1,510), Markov expectation conditioned on
    endpoints-ABC. Battery: k=16 replicates (z=+5.54, 91/96 agreement);
    cosine (z=−1.30), k=8 (+0.40), half-stream (−0.26/−0.28) all fail — but
    the failure mode is LABELING DEGENERACY (one mega-cluster: A=82/76/72),
    never excess-death under a valid 3-block labeling. Cut profile: the ABC
    blocks (32/27/17) emerge at k≥12 and plateau k=12–16; cosine collapse is
    the contactor's own documented metric pathology (smoothing inflates rare
    groups). E-a (exploratory): with FIXED full-stream labels the excess is
    global — halves z=+3.49/+4.76, all four quarters z≥+2.00 — so the
    half-stream collapse is clustering power, not evidence against the
    rhythm. Dominant directed cycle A→B→C→A everywhere it is measurable
    (ref 836/425; k=16 post-alignment 786/392).
  - T2: bigram wins held-out by 0.028 nats/trans despite 31× the parameters
    (9,120 vs 293); the HMM's unsupervised transition matrix is itself
    cyclic (S1→S0→S2→S1 dominant) — suggestive, not a finding. The banked
    labels as OBSERVED states (M_phm) are worst of the three on test
    (−4.5348): the fixed phases don't help prediction. First attempt
    diverged numerically (emission collapse, testLL/trans=−332); fixed with
    MAP-EM eps=1e-4 smoothing (A3), restart spread −4962…−5190 recorded.
  - T3: N30's "61/96 change" = naive label-name comparison, reproduced
    exactly (35/96 agree). N37's "69/96" = best-permutation agreement,
    reproduced exactly (perm BACR = old-A↔new-B swap). Cycle direction is
    preserved under the permutation (old A→C→B→A ≡ new A→B→C→A). No data
    contradiction — N30's comment just didn't permute-align.
  - T4: P2a momentum — after a cycle step the next step continues the cycle
    63.3% (n=765) vs 48.6% after non-cycle ABC steps (n=383), z=+4.77,
    p≈1e-6: SUPPORT. P2b — full 2nd-order Markov loses held-out to 1st-order
    (−1.2189 vs −1.2143/trans): null. Reading: genuine second-order
    structure concentrated in the cycle-continuation contrast; a full
    memory-2 model doesn't generalize (parameter noise). P2c — one fixed
    column order A→B→C→A in both halves (422/198, 414/226); the variant leg
    is void (degenerate labelings). Table columns per se still unconfirmed —
    needs key recovery (F43's deferred test stands).
- Enlightenment: the round-5 E-code was never archived and its headline
  number came from an undocumented endpoints-ABC restriction — the gate
  caught it (naive full-stream gives obs=0.3579, z=5.90: same z, wrong
  construction). Also: the "fragile phases" story splits in two — the
  ASSIGNMENT is fragile (metric/cut/sample-size), but the EXCESS survives
  every labeling that recovers a real 3-block structure, and the rhythm is
  global under fixed labels. Fragility of the instrument ≠ fragility of the
  phenomenon.
- For the report: rotation section. The 1–3 numbers per thread: T1 —
  "not robust by bar; k=16 z=+5.54/91% agree; degeneracy is the failure
  mode; global under fixed labels (halves +3.49/+4.76)"; T2 — "HMM loses
  held-out −4.2638 vs −4.2356, wins BIC 12k vs 74k; unsupervised cycle
  found"; T3 — "reconciled: 61-change = naive, 69-agree = perm-aligned";
  T4 — "momentum p≈1e-6 SUPPORT; memory-2 null; one column order".
- Caveats: P2a characterizes rather than independently confirms E1 (same
  sequential phenomenon, different slice). The Viterbi/banked contingency
  doesn't map cleanly (states mix banked phases) — the HMM's cycle is in
  transition structure, not state identity. OVERLAP FLAG: a parallel
  side-rotation fleet is running similar work right now
  (`code/side-rotation/rhythmicist/hmm_compare.py`, `robustness.py`;
  `geometer/wo2_homophone_cycling.py`) — deconflict before merging
  conclusions. First hmm run died silently (exit 2, no traceback) on the
  loaded VM; the rerun with A3 succeeded — treat thread-2 numbers as the
  rerun's.
