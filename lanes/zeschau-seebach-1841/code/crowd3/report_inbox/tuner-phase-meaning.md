## tuner: phase-meaning
- Context: I was the 7th executor ("the tuner") in round 3 — one job: find what
  the contactor's 3-phase rotation (A→C→B→A, chi²≈181) MEANS linguistically.
  Built an era "tune template" (Tocqueville T1+T2 syllabified, P(syllable |
  word-position)) under two documented syllabification rules, fixed the
  hypothesis C=final/B=initial/A=medial a priori, and ran leave-one-out
  ranking of each anchor's true value, phase-constrained vs unconstrained
  baseline. Recomputed every number from the pair stream and corpus myself.
- Decision: **NULL** — the phases are not word-position classes. No shortlists
  emitted. All material in `code/crowd3/tuner_results.{md,json}` (code:
  `code/crowd3/tuner.py`).
- Why: (1) LOO: phase-constrained top-10 hits 2/34 anchor-slots vs baseline
  6/34 across 4 configs (2 rules × GT7/ALL10) — never ahead in any single
  config. (2) Modal analysis: 0 of 4 A-phase anchors is modal-medial under
  either rule ('la'/'que' final-heavy, 'pre'/'i' initial-heavy) — A=medial
  falsified outright. (3) The tune disagrees with itself on flagship anchors
  across rules: 29=er modal-final (R1) vs modal-medial (R2); 40=e
  modal-initial (R1) vs modal-final (R2). (4) Segmentation mismatch: cipher 29
  is 2.55% of pairs (rank 3) but bare-'er' is 0.038% of corpus syllable tokens
  — infinitive mass syllabifies to ler/ner/etc, never bare 'er'; the tune's
  segmentation is uncalibrated vs the 1841 syllabary.
- Enlightenment: the rotation is real (my recompute: chi²=188.3, df=4;
  A→C 1.38×, C→B 1.625×, B→A 1.367×) but positional reading was a mirage —
  the anchor that "anchored" it, 29=er, is the very case where my
  segmentation provably diverges from the syllabary's. Also: 96=par sits in
  phase C yet 'par' is modal-initial under both rules (tension, flagged not
  killed); 40=e is the lone anchor where the positional reading helps
  (R1 rank 5 vs baseline 14).
- For the report: belongs in the contact-structure/methodology section as a
  falsification — "3-phase rotation confirmed (chi²=188.3) but NOT
  word-position classes (tuner LOO: phase-constrained 2/34 vs baseline 6/34;
  A=medial falsified at anchor level)". Numbers that matter: 188.3, 2/34 vs
  6/34, 2.55% vs 0.038% ('er' mismatch), 0/4 A-anchors modal-medial.
- Caveats: tune is my rule-based syllabification of Tocqueville, not the 1841
  segmentation (proven mismatch) nor despatch register; LOO n=7–10 is coarse
  (modal analysis corroborates independently); 82=m corpus support thin
  (elided m' rare in formal prose); nothing here confirms or kills 87=ce —
  kill authority stays with red team.
