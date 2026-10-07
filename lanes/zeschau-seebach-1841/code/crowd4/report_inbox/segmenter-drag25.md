## segmenter: round-4 control + drag of the 25 crib-drag targets
- Context: Work order 5 — drag the 25 STRUCT crib-drag targets from round 3
  (code/crowd3/segmenter_results.json), with a PRE-REGISTERED control first per
  scorer lesson N16 (no instrument touches R5005 before validating on a
  control). Spec written before any run: code/crowd4/segmenter_control.md.
- Decision: Control PASSED → drag ran. Verdicts: **0 proposed, 25 LEAD-held,
  0 killed.** The two priority targets (@1110-1112 [41 65 38], @81-83
  [51 62 16]) were dragged first, then the rest in STRUCT-score order, per the
  pre-registered protocol (code/crowd4/drag25.py, drag25_results.json).
- Why: The control is a synthetic 621-word / 900-group Tocqueville cipher with
  known boundaries, rotation cycle A→C→B→A, q_break=0.70, ear-cutting noise
  (p_merge=0.08, p_split=0.04, p_alt=0.06), era prior rebuilt minus the control
  slice. Metrics: M1 boundary recall@0.5 = 0.721 (≥0.60), M2 internal<0.5 =
  0.939 (≥0.70), M3 mean diff = 0.258 (≥0.10). Fitted s-values same ballpark
  as real (top boundary legs ~+11–12.5 both). On the drag, the protocol's
  check menu {G,L,F,X,I} was applied honestly: unconstrained top-frequency
  picks ('une'/'encore'/'gouvernement') carry no *discriminating* support —
  (F) frequency-rank fails on them (e.g. @1110-1112 'encore': 38-vs-'re'
  ratio 20.75), (I) absent, and (X) as first implemented was circular
  (unconstrained picks "confirming" each other) so it was restricted to
  slot-constrained partners. (G) is span-quality already baked into round-3
  target selection — counting it again as a reading check is double-counting.
  A first-pass "14 PROPOSED" output was vacuous and was corrected before
  reporting; the polyvalence kill of @1184-1187 was retracted (lane has
  polyvalence evidence: bigram_closer 'me' ×3 groups).
- Enlightenment: (1) Under the 62='on' lead, ZERO era-corpus words fit any of
  the four 62-touching MAP spans (@81-83, @1703-1705, @507-509, @1538-1540) —
  direct corpus query confirms: no 3-syllable middle-'on' word, no
  'on-ne-*' word exists in 12,108 distinct Tocqueville words. This sharpens a
  real tension: frenchman4_62 reads 62→94 ×8 as TWO words ('on'+'ne'), while
  the segmenter MAP spans merge them into single words. The likeliest story
  is MAP-span merge error (control M1=0.72 ⇒ ~28% boundary miss rate), not a
  kill of 62='on' — the lead's legs (ear lock + 8× 'on ne') are independent
  of these spans. (2) (F) is the only discriminating check and it works:
  it killed the 'onzième' hapax readings via 94-vs-'zie' 107×. (3) Gutenberg
  boilerplate ("online" ×10 from license headers) was polluting candidate
  enumeration — stripped via START/END markers before the final run.
- For the report: belongs in the Seebach "round 4 → segmenter" section.
  Numbers that matter: control PASS (0.721 / 0.939 / 0.258 vs 0.60 / 0.70 /
  0.10); drag 0/25/0 (proposed/held/killed); 62-touching spans: 0 corpus
  words fit under 62='on' (n=12,108 distinct).
- Caveats: The control tests segmentation *given correct phases* — it does
  not re-test the contactor's unsupervised k=12 clustering that produced the
  R5005 phase map. (F) assumes clean syllabification, but the cipher
  demonstrably ear-cuts ('première' → pre-m-i-er-e @1033), so (F) failures
  don't kill readings. 62='on' is lead-grade and 94='ne' provisional — the
  two 'onzième' non-verdicts inherit that uncertainty. Era corpus is
  Tocqueville, not diplomatic correspondence; proper nouns/terms may be
  absent. No GitHub push; R5005 only.
