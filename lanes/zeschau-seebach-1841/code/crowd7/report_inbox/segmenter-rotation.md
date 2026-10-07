## segmenter: rotation round 7 — flag application, label-free momentum, columns refuge

- Context: Round-7 work order 11. The Red Team adjudicated all round-6 marks
  (N41 UPHELD, N43 UPHELD — `code/crowd7/redteam/RULINGS.md`) and the N43
  noisy-detector flag now governs the rotation package: (a) existence confirmed
  by label-free lag-3, (b) exact χ² magnitudes (181.3/366.3) noisy — nothing
  may lean on them, (c) phase mapping ~0.5 purity — per-group phase arguments
  need independent support. Three threads, all pre-registered in
  `code/crowd7/segmenter/PREREG7.md` BEFORE any test ran. Deconfliction honored:
  side-rotation fleet's rhythmicist/geometer results cited, not re-derived.

- Decision (Thread A — flag audit of the round-6 package): gate E1 (z=+5.81)
  and P2a (r1=0.6327/r0=0.4856, z=+4.77) re-derived EXACTLY. Verdicts: T1
  labeling-robustness FRAGILE → SURVIVES* (failure mode is degeneracy, never
  excess-death; 91/96 k=16 agreement is instrument-consistency, not mapping
  truth). T2 HMM-vs-bigram → SURVIVES (no χ², no labels in fit; unsupervised
  cyclic A is label-free corroboration). T3 69/96-vs-61/96 → SURVIVES*
  (definitional metrology). P2b memory-2 null → SURVIVES. P2a momentum →
  SURVIVES* PENDING Thread B (population-level, not χ², not per-group;
  circularity caveat: labels fit on the same stream). **P2c fixed-column-order
  FALSIFIED → DOWNGRADED to INCONCLUSIVE**: variant direction flips are
  computed on degenerate partitions (V_cos C=1 group) and cannot falsify "one
  column order" under ~0.5 purity; halves-consistency (fwd/fwd) survives as an
  observation. Evidence: `code/crowd7/segmenter/flag_audit.json`.

- Decision (Thread B — label-free momentum): does P2a survive WITHOUT the
  fragile labels? Instrument: 3-state HMM fit on train pairs[0:1231] only
  (code copied verbatim from round-6; gate B0 PASS, A matches round-6 within
  4.3e-4), Viterbi-decode of the HELD-OUT test split, cycle from the frozen
  A (ratio 11.3, guard B1 PASS), no banked labels anywhere. Result:
  **INCONCLUSIVE** — the unsupervised process is nearly deterministic
  (S1→S0 prob 1.0), so the Viterbi path starves the test (n0=49<50 guard;
  r0=1.00 is pure re-sync artifact — the pre-registered conservativeness
  mechanism, confirmed empirically). Permutation p=1.0. The labeled momentum
  itself REPLICATES on the test split (r1=0.6245/r0=0.4656, z=+2.98,
  p=0.0014) — real within its instrument, but with no label-free confirmation
  or refutation. Evidence: `code/crowd7/segmenter/momentum_labelfree.json`.

- Decision (Thread C — columns refuge): arbitrary-column form stays KILLED
  (fleet's instrument-validity proof, cited). Concretized the refuge as
  3 columns × ~32 rows with columns = CODA-SONORITY class
  (OPEN/SON-closed/OBS-closed) — the natural 3-class form — with mechanism
  (French function-word/content-word coda alternation, F49 contact-coherent
  aliasing preserves the class sequence). **Verdict: WEAKENED.** Tocqueville
  coda stream: lag-3 z=+11.9 BUT flat profile (0.41–0.44, no spike vs the
  cipher's sharp 0.36 spike) — a different phenomenon (burstiness, not
  periodicity); momentum strongly ANTI (r1=0.27 vs r0=0.39, z=-65, both
  corpora agree); 50%-purity noise simulation attenuates anti-momentum
  (z -43→~-12) but NEVER flips its sign — the cipher's +4.77 cannot arise
  from this process through N43(c)-style noise. Onset-sonority variant dead
  outright (lag-3 z=-5.85). Anchor probe inconclusive (p=0.12, n=16).
  The general refuge ("some other untested class") remains logically open
  with no positive evidence; full KILL needs key recovery. Evidence:
  `code/crowd7/segmenter/columns_refuge.json`.

- Why: the flag's three-way scope decides each thread. (a) Existence was never
  at issue — the gate re-derives exactly. (b) Nothing in the surviving
  conclusions leans on 181.3/366.3 (P2c's downgrade is about (c), not (b)).
  (c) is the active blade: it downgrades P2c, fences the Viterbi contingency,
  motivates the label-free Thread B, and bounds the refuge (noise can't flip
  momentum sign under the purity model).

- Enlightenment: (1) The pre-registered conservativeness note for Thread B
  ("decoding noise inflates r0") turned out to be EXACTLY right — r0=1.00,
  all 49 blips re-sync. Pre-registration earned its keep. (2) French prose
  DOES have a coda-class lag-3 rhythm (z=+11.9) — the refuge's mechanism
  half is real — but with the opposite second-order sign (avoidance,
  echoing the geometer's B3 taboo finding) and the wrong shape. The rhythm
  is linguistic; the cipher's SHAPE of rhythm is not. (3) The unsupervised
  HMM's near-deterministic cycle vs the labels' stochastic cycle: momentum
  lives in the stochastic component that fragile labels resolve and MAP
  decoding suppresses — which is precisely why the flag can't settle it.

- For the report: rotation section. The 1-3 numbers that matter:
  flag audit 5×SURVIVES(*)/1×DOWNGRADED (P2c→INCONCLUSIVE);
  label-free momentum INCONCLUSIVE (n0=49<50; labeled replicates z=+2.98);
  coda-column refuge WEAKENED (plaintext momentum z=-65, noise-stable sign).

- Caveats: Thread B INCONCLUSIVE is not a falsification — a posterior-sampling
  (FFBS) or 4-state variant could revisit it (not run; would need re-registration).
  Thread C's corpus test is orthographic (phonotactician syllabifier) vs the
  encipherer's ear-spelled cuts (R2) — conservative by construction; diplomatic
  register could differ from Tocqueville/Les Mis (both corpora agree, limiting
  this escape). The noise non-flip result assumes random 50%-purity mislabeling;
  a systematic mislabeling story could in principle flip signs (none proposed).
  No per-group phase claim is made anywhere in this package.
