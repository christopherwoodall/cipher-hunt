## slider: pass-1 pre-registration (STEP 1 complete)
- Context: Seebach side-path fleet, SLIDER role. STEP 1 was to pre-register pass-1 match thresholds BEFORE any sliding, so thresholds can't be tuned to fit output. Skeleton file path + phonetic rules arrive from the coordinator at GO (STEP 2).
- Decision: Frozen pre-registration at `code/sidepath/prereg_pass1.md` (sha256 recorded; any mismatch at slide time → pass VOID). Scoring: S = 0.30·lex_fit + 0.25·cut_fit + 0.20·bound_fit + 0.25·len_fit; ACCEPT iff S ≥ 0.60 ∧ lex_fit ≥ 0.50 ∧ len_fit ≥ 0.50 ∧ bound_fit ≥ 0.30 ∧ no pinned-anchor contradiction. Emit top-5/window, all S ≥ 0.50 with pass/fail flag. Bound gets the lowest weight deliberately (phase instrument VOID per red team F26); era lex attestation the highest weight per F15 register point.
- Why: the lane's scorers keep dying on control (N5/N12/N16 — scorer exploited, placement ties, unvalidated). Pre-registered control: 3× seed-1841 shuffled controls, identical slide; pass VOID unless real accepts ≥ 2× control mean. Boundary signal from segmenter (R→C +12.62, B→B +12.53 boundary-favoring) constrains fits via bound_fit with crossing penalty.
- Enlightenment: file-measured pair count is 1,882 (3,764 digits), not STATE.md's 1,846 — window positions are 0-based file order, flagged in prereg. 62→94 is file-measured ×5, not NOTES.md's ×8 (calibration flag; coverage via all-62-contexts subsumes it). The 47 window is pairs 150–154 = 87 64 96 47 46 ("ce qui par 47 que"); sliding window 146–157 in 3/4/5-pair sub-windows.
- For the report: methodology section. Key numbers: threshold S ≥ 0.60 (frozen), weights (0.30/0.25/0.20/0.25), 25 segmenter targets + W-47 + 5 62→94 + 32 62-contexts + 42 24-contexts + 13 52-contexts. Formulae: 4 surviving diplomatic formulae + 3 subjunctive triggers; ALL "J'ai l'honneur d*" forms excluded (H5 DEAD, N11).
- Caveats: phonetic rule parameters arrive at GO — only rule NAMES are frozen; a param that contradicts the frozen score structure would need a new prereg version, not a silent edit. 94=ne treated pinned for pass 1 (provisional-strong). New implied values from candidates are UNCONFIRMED hypotheses, never accepted values. Awaiting coordinator GO (skeleton path + phonetic rules).

## slider: pass-1 slide complete — VOID (null), frame fixed via prereg v1.1
- Context: Ran the side-path crib-bootstrap slide per prereg_pass1.md as amended
  by prereg_pass1_v11.md (frame fix only). 147 windows (a–f) × candidate
  inventory (ERA-VOCAB 1–5 syllables ≥3× from Tocqueville t1+t2, 5,715 types;
  SURVIVING FORMULAE; 1841 COLLOCATIONS), fuzzy scoring at frozen weights
  (0.30/0.25/0.20/0.25) and thresholds (S≥0.60, lex/len≥0.50, bound≥0.30),
  then the identical slide on 3 shuffled controls (seed 1841). Output:
  `code/sidepath/slide_pass1.json` (977 records: 176 real + 801 control).
- Decision: **Pass 1 is VOID (null)** — the pre-registered VOID condition fired:
  real accepts 174 < 2 × mean(control accepts 223/179/223 = 208.3). No claims
  merge; nothing in slide_pass1.json promotes or demotes any value. Two
  implementation bugs were found and fixed mid-run (before the final run):
  (1) ERA-VOCAB pool briefly admitted >5-syllable words for long windows
  (junk "inconstitutionnelles" accepts) — re-cut to the frozen 1–5 bound;
  (2) the control initially reused real window groups (only bound_fit was
  perturbed) — fixed so control windows draw groups from the shuffled stream.
  Final run is clean; both fixes are compliance with the frozen prereg, not
  changes to it.
- Why: The VOID rule exists because scorers lie (N4/N5/N16). The slide proved
  it again: unanchored windows accept identically in real and controls
  (105 vs 105/90/95 — the same one-anchor words like "enfin"/"england's" all
  score S=1.0 on W-S01 [24 53] because the free pair is unconstrained), and
  even anchored windows show no separation (69 vs 69/39/64). The fuzzy
  scorer cannot distinguish candidates at this anchor sparsity — exactly what
  the control was built to detect.
- Enlightenment: Three things. (1) The frame fix mattered: v1.0's 1,882-frame
  had misplaced the 87-64-96-47-46 formula at 150–154 (canonical: 148–152),
  undercounted 62→94 as ×5 (canonical: ×8, reconciling NOTES.md), and listed
  42/13/32 positions for 24/52/62 (canonical: 52/27/34). (2) The two sharpest
  windows are dead under the frozen inventory: all eight 62→94 "on ne" windows
  (n=8 pairs) emit nothing — no 1–5-syllable era word spans them — and no
  W-47 sub-window covering 148–152 clears S≥0.50. The slide's best-constrained
  targets are silent. (3) The RIVAL-NOTE mechanism worked as designed: the
  highest-scoring anchored candidates in the whole slide are "montrera" on
  W-S15 [62 94 88] (S=0.917) and W-S18 [77 62 94] (S=0.863), both requiring
  94="re" — emitted as forced-fail for red team, i.e. the 94="re" rival
  outscores every 94="ne"-consistent reading at those windows.
- For the report: Side-path / slider section. Numbers that matter:
  **174 real accepts vs 208.3 control mean → VOID**; 147 windows;
  62→94 = ×8 @100/508/839/1328/1361/1685/1703/1771 (NOTES.md reconciled);
  prereg v1.0 sha256 `233ff426…11861a`, v1.1 `6d47674e…83bfad`.
- Caveats: (1) My by-ear pronounced form is approximate (drops final s/x/z,
  collapses doubles per R8; no silent-t/d/p engine) — alignment quality
  inherits that. (2) Era vocab contains English tokens ("the", "states") from
  Tocqueville's quotations — future passes should filter to French lexicon.
  (3) Control asymmetry (flag for red team): shuffling usually de-anchors
  windows, so controls accept MORE than real (223 vs 174) — the aggregate VOID
  comparison is conservative but the control is a weak instrument for anchored
  windows specifically. (4) bound_fit uses the phase instrument the red team
  voided (F26) at the frozen 0.20 weight — carried, not endorsed.
  (5) Candidate pool was restricted to len_fit≥0.5 by construction, so
  fail-records with len_fit=0 and S≥0.50 are absent from the audit tail.
