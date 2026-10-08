## red-team adjudicator, round 13 — second shift (docket closed)

- Context: second-shift adjudicator ruled the 4 packages that landed after the
  first shift (homophone-ab, carry-classes 31/33, carry-rest, missing-mass finals).
  Kill experiments KE1/KE2 untouched (red-team killer's jurisdiction).
- Decision: docket CLOSED — 21 rulings total, 0 pending.
  - R-AB1: {33,86} → SPLIT (GRANT). Joint frames 2/45 shared; depletion
    binomials p=0.00174/0.03131; pour-successor Fisher p=0.00072 (all
    re-derived). Reclassify as class-mates; §b {33,86} PROPOSE retired; do NOT
    merge 33+86 windows downstream. Phase A/B mismatch (both phase maps:
    33=A/86=B vs reconstructor's B,B) independently corroborates.
  - R-AB2: {48,94} → SPLIT (GRANT). Joint 1/67 shared; 48 depleted in 94's
    char frames 0/10, p=0.00085; marginals indistinguishable (p≈0.5) but
    F60 kills 48="ne". Ne-distributed class-mates, different values; do NOT
    tie 48↔94. 48 stays UNIDENTIFIED.
  - R-CC31: 31=VERBAL (finite) CONFIRM (GRANT) — byte-identical re-derivation,
    conservative audit disclosed; no status change beyond the round-12 grant.
  - R-CC33: 33 NULL constrained (GRANT) — T2 fired mechanically for "savoir"
    (n=2, unique argmax, pool∖v8) but LEAN blocked three ways; savoir
    forbidden under both forks; paradox sharpened, not resolved.
  - R-CR48: GRANT — 74-class OPEN (islet neither promoted nor killed; 74
    verb-adverse 2×, adverse-grade); H_stem GAINS A LEG (B1+B2, leg only;
    ne-marginals tension recorded open); second "48-47-46" CLEAN NEGATIVE
    (@863 only).
  - R-CR1248: GRANT-WITH-CONDITION — PC-1 GRANTED as leg (peu 5/9; craindre
    spot-checked genuine, OCR caveat); DP-1 PERMANENT FENCE both arms
    (frame-unattested ~22MB+758k, k=1–5 absent; NOT ungrammaticality
    evidence). @1248 NEITHER-fence stands.
  - R-CRESTE: GRANT-WITH-CONDITION — atteste FRAME-BEST LEAD (n=1 in-register
    «qui le V» trigram + 4× government; NOT a unique-ID promotion; fragility
    flagged). T1/T2/T4/T5 honest nulls; T3 06="pro" stays LEAD-WEAK;
    proteste doubly-weak but not killed; reste excluded (not in H0).
  - R-MM1: deficit arithmetic GRANT — 11 STRONG deficits sum 385.6 occ →
    20.0 cells naive; fragment-corrected ≈330 occ → ~17 cells (17–20) among
    the 84 unidentified groups; 0 for identified syllables. v8 sensitivity
    reproduces direction. Both prereg reservations discharged.
  - R-MM2: GRANT-WITH-MODIFICATION — priors BANKED AS PRIORS ONLY with an
    anti-promotion fence (48→ne P1c, 52→est P1c, 76→ver/er P1, de-pool P2);
    digit hunt NEGATIVE → retired (8 cells = rare-vocabulary).
- Why: every battery number was independently re-derived from the JSONs' own
  methods before ruling (Fisher one-sided-by-design accepted per prereg;
  binomials and z-scores exact; phase maps independently checked). The joint
  (pre,suc) frame battery is the round's discriminator — distribution-level
  agreement proved necessary-but-insufficient twice ({33,86}, {48,94}).
- Caveats: (1) Citation-convention corrections for first-shift rulings
  (substance unaffected): R-IA2 frame starts @1444/@1800 (not @1445/@1801);
  R-IA4 96-00 third window starts @960 (not @961); R-IA7 @150 indexes the 96
  cell (frame start @149). R13BANK uses corrected indices. (2) R-AB2's V1–V4
  substitution battery as named did not land — test 8 (joint-disjoint ⇒
  vacuous) is the honest equivalent. (3) H_stem's ne-marginals tension stays
  open — name the stem-before-verb construction or drop the leg. (4) atteste's
  LEAD rests on n=1 — PROMOTE bar (≥2 legs + stem-ID) stays red-team's.
- For the report: round-13 adjudication section. Evidence:
  `code/crowd13/adjudicator/RULINGS-ROUND13.md` (R-AB1/AB2, R-CC31/33,
  R-CR48/CR1248/CRESTE, R-MM1/MM2). Baselines: `verify_f26_17.py` 237/237
  PASS (R13BANK, 34 new checks); `verify_round7.py` 160/160 PASS
  (ROUND13-LEDGER, 27 new checks). Both exit 0.
