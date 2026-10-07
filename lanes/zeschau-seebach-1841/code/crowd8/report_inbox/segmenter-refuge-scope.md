## segmenter: columns-refuge scoping (WO-13)

- Context: round-7 (N48) applied the N43 flag to the rotation package and
  weakened the columns refuge (coda-sonority concretization dead). WO-13
  asked: scope what's testable WITHOUT key recovery, state honestly what
  isn't — and run any genuinely new testable concretization.
- Decision: split the refuge into two claims — (i) LINGUISTIC (some syllable
  class X carries the period-3+momentum signature in French prose) and
  (ii) ARRANGEMENT (the table was physically arranged in columns=X).
  Claim (i) is testable via corpus signature + a NEW instrument-recoverability
  test (inverts the Geometer: a class the lane's contact-clustering can't
  recover can't be what the cipher's clustering found). Claim (ii) and five
  other items (per-group phase truth, encipherer's cuts, register, dealing
  policy, the bare unconcretized schema) are untestable without the key.
  Pre-registered in `code/crowd8/segmenter/PREREG8.md` before data.
- Why: four pre-registered syllable classes (X1 coda-sonority as calibration,
  X2 onset manner, X3 nucleus quality, X4 shape) run through signature
  (C1 construction) + recoverability (ARI vs 200 random partitions) on
  Tocqueville, Les Mis as register check. Result: X1/X3/X4 momentum strongly
  ANTI (z=−65…−112); X2 marginal on Tocqueville (+0.016 effect) but reversed
  on Les Mis (z=−7.03); ALL FOUR score ARI≈0 on the lane-faithful k=12/top-96
  pipeline (p_emp 0.21–0.94). Full numbers in
  `code/crowd8/segmenter/recoverability.json` and `diag_k12_top96.json`.
- Enlightenment: the k=3 cut degenerates at every scale tried (1524/1/1 on
  full inventory, 93/2/1 on top-96) — the Rhythmicist's "membership fragile"
  finding reproduces on corpus data, which is why the ARI leg needed the
  lane-faithful k=12 repair. Also: recoverability and signature dissociate
  exactly as designed (X1 was expected recoverable-but-signaturless; it came
  out dead on both — the instrument works, it just doesn't see coda classes).
- For the report: rotation/refuge section. The 4 numbers that matter:
  momentum z = −64.9 (X1), +8.6→−7.0 register-reversed (X2), −111.7 (X3),
  −100.2 (X4); ARI≈0 for all four vs random nulls. Refuge verdict: every
  concretization dead; schema survives only unconcretized; full kill needs
  key recovery (standing).
- Caveats: orthographic syllabification ≠ encipherer's cuts (R2 — tests are
  conservative); register proxy (no diplomatic French); top-96 covers 75.3%
  of tokens; S2 transition-matrix comparison was secondary/supporting-only;
  no per-group phase claim anywhere (N43(c) honored); the k=12 ARI rerun was
  a post-hoc diagnostic repair, labeled as such in `diag_k12_top96.py`.
