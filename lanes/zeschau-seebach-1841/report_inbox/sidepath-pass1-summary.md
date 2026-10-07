## sidepath-coordinator: pass-1 synthesis — VOID, loop stalled honestly

- Context: rapid-iteration crib-bootstrap loop (skeleton→slide→sieve→promote), a
  speed-built side track separate from the main fleet's careful testing. Pass 1
  ran the full slide with a pre-registered control (3× seed-1841 shuffles).
- Decision: pass 1 is VOID (null) — 174 real accepts vs control mean 208.3;
  pre-registered rule (real < 2× control mean) fired. No claims merge, nothing
  reached the sieve or red team. Per the loop's stop rule (stop on a
  promotion-less pass), the loop STOPS after 1 of 5 passes. Zero promotions,
  zero kills. This is the control working as designed, not a failure of effort.
- Why: the fuzzy scorer cannot separate at 30.66% anchor sparsity — unanchored
  windows accept identically in real vs controls (105 vs 105/90/95); anchored
  windows show no separation either. The sharpest targets are silent under the
  frozen inventory: all eight 62→94 windows and all W-47 sub-windows emitted
  nothing. The candidate inventory doesn't capture what's actually there.
- Enlightenment: (1) the frame trap — naive concatenation parses 1,882 pairs,
  the canonical parse 1,846; the first slider's windows would have slid
  misaligned. Caught before any slide ran. (2) Control asymmetry: shuffling
  de-anchors windows, so controls accept MORE than real — the control is
  conservative but weak for anchored windows; future drags need anchor-preserving
  controls. (3) Silence is data: the inventory's best shots miss the highest-
  value windows, so the missing readings aren't in the frozen candidate set.
- For the report: new numbers section. Verified by coordinator re-derivation:
  skeleton 1,846 positions / 96 groups, sha256 18d48cc…, coverage 30.66%
  (566/1,846: GT 11.05%, leads 7.80%, provisional 8.13%, strengthened 1.73%,
  strong 1.95%). Canonical-frame recounts: 24→52 positions (was 42), 52→27
  (was 13), 62→34 (was 32) — the old counts were parse artifacts. 62→94 = ×8
  @ [100,508,839,1328,1361,1685,1703,1771] reconciles NOTES.md. W-47 formula
  87-64-96-47-46 @ 148–152 (not 150–154). la première @ 1033 confirmed in-frame.
  n87=32 / n64=46 / n96=21 match the Frenchman's independent reads.
- Best lead (NOT a promotion — voided pass): "montrera" (94="re") is the
  top-scoring anchored candidate (S=0.917 @W-S15 [62 94 88], 0.863 @W-S18),
  emitted forced-fail per RIVAL-NOTE. Independent replication of the main
  fleet's round-4 work order #3 (test 94="re" vs 94="ne").
- Caveats: by-ear pronounced form is approximate (no silent-t/d/p engine);
  era vocab contains English tokens from Tocqueville's quotations; the loop
  tested only the frozen inventory — a richer/different candidate set is
  untested, not refuted.
