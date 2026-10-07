## frenchman: 93="l'" allophony model + 77="gouv"/78="er" support hunt (round-8 WO 9–10)

- Context: Register specialist. Pre-registered bars before data
  (`code/crowd8/frenchman/PREREG.md`): any 93="l'" model needs explicit
  conditioning + F33-falsifiability; the 93→62 payoff leg is banked and
  may not identify 93 (B4). Corpi: full side-period diplomatic corpus
  (4,217,937 tok, elision-split) + Tocqueville sanity; cipher = repaired
  1,847-pair parse. Code: `code/crowd8/frenchman/s1_data.py`,
  `s2_allophony.py`, `s3_gouv.py`, `s4_verdicts.py`; numbers:
  `code/crowd8/frenchman/results.json`. The 48 battery is the
  homophonist's (WO-1) — not duplicated here.

- **Decision (a): 93="l'" ALONE is rate-KILLED (register-corrected);
  the rescue is M_hom {93,8}="l'" as unconditioned homophones → LEAD.
  93-alone: n=14 vs diplo E=31.26, exact P(X≤14)=4.1e-4 — kill holds in
  every diplo slice (v8 E=32.9, nesselrode-all E=33.6, guizot E=37.0).
  N46's "shape-STRONG" does NOT reproduce: fresh vow=1 (only 29=er×1);
  round-7's archived `u2_lcell.json` doesn't even contain 93, so the
  vow≥2 claim is irreproducible from archived artifacts (F26-class
  traceability flag — possibly 62="on" was smuggled in as vowel-initial,
  which would be circular). H_vow (front-vowel allophone, E=13.4 fit) is
  KILLED by 93→62=2 under fenced 62="on" ("on" is back-vowel-initial).
  H_euph (pronoun/article split) is UNTESTABLE on current anchors —
  stays hypothesis, not a model. H_null (diplo rate explains) is KILLED
  (p=4.1e-4). M_hom legs: joint n=32 vs E=31.26 dead-center (two-sided
  p 0.47–0.60, in-band in all four diplo slices); scale-free ratio test
  32/29 vs diplo P(l')/P(que)=1.48, p=0.15; cons-GT=0 across 32 windows;
  zero GT-determiner predecessors; "ne l'"×1 (93 @102: 94-93-59 =
  "ne l'est", grammatical); (93|8)→62=4 with free intermixing (shared
  pre {67,85,45}, shared fol {52,29,62} → unconditioned homophony, not a
  complementary split). Rival pairs eliminated: {93,8,3} P=3.8e-4;
  {3,8}/{3,93} need 4 exceptions to 64="qui" provisional (3→64=4,
  "l'qui"); {34,8}/{34,93} break prov-strong 94="ne" (34→94=1, "l'ne").
  Runner-up {8,14} (rate p 0.40–0.67) lacks the "ne l'" leg and costs two
  "ce l'" exceptions vs one. Rate-saturation corollary: 32≈31.3 leaves no
  room for fused l'V cells — caps the model space.

- **Why M_hom despite adverses:** the fenced costs are explicit and
  cheap. (i) 93→52=2 (@159/@263, "l'pas") needs a vowel-initial third
  reading of 52 — 52's polyvalence is K5-forced and F33's negation-frame
  rule already excludes "pas" at both windows (no "ne" before); the third
  value itself is unevidenced (honest cost, biggest adverse). (ii)
  87→8=1 @1487 ("ce l'") needs one 87-exception (87="ce" provisional) or
  one 8-exception. (iii) 8→21 @98 / 8→43 @1302 ("l'me") resolve against
  the "me"-readings: 21→62×5 already forces 21≠"me" elsewhere, and
  @1302's 43-21-43 ("me me me") independently forces 43≠"me" there.

- **Decision (a2): 62="on" gains two NON-EAR legs; 62="il" →
  DISFAVORED-STRONG.** L_A (conditional kill): M_hom ∧ (93|8)→62 ×4
  (@10/@944/@1323/@1685; E=1.6–3.45 under "on" across diplo slices, obs
  4 in-band) ∧ diplo l'+il = 0/4.2M (grammatical zero confirmed) → "il"
  killed conditional on M_hom (LEAD-grade condition, hence conditional).
  L_B (21:1 likelihood ratio, M_hom-independent): 46→62=0 with
  E["qu'on"→46-62]=1.77 (P0=0.170) vs E["qu'il"]=4.83 (P0=0.0080);
  LR=21.3 for "on" — the qu'-elision rate asymmetry N35 asked for
  (qu'il/qu'on = 2.7× full corpus, 2.19× in Nesselrode v8). Caveats:
  compositional qu'+pronoun assumption; whole-word rescue
  unfalsified-but-unevidenced (U1 NULL); single datum. 62="on" stays
  fenced STRONG LEAD; "il" not fully killed (L_A's condition is LEAD).

- **Decision (b): 77="gouv"/78="er" independent support NULL (7th
  consecutive null); the {ver,er} fork is a THREE-way tiling ambiguity,
  live fork (a2) vs (c) UNRESOLVED on data.** Tilings: (a1)
  le|gou|ver|m|ent [94="ver" — breaks prov-strong 94="ne", DEAD];
  (a2) gou|ver|ne|m|ent [78="ver", keeps 94="ne"]; (c)
  gouv|er|ne|m|ent [78="er", keeps 94="ne"]. (a2)'s F38 islet ("ver iff
  next=94") is circular — defined on the only windows it covers
  (n_eff=1) — and its "vernement 554" leg doesn't beat "ernement 478"
  (round-7's own corroboration numbers). Lean (c): crib "er"-unit habit
  (29="er" in "première"); counter-lean (a2): standard syllabification
  gou|ver, no "er"-homophony (weakened by M_hom demonstrating
  homophony). Both stay LEAD, n_eff=1. No 77-78-94 outside the 5-mer;
  gouvernement-family E<0.1/despatch (no independent occurrences
  expected); diplo "gouvernement" E≈1.05–1.67/despatch vs ×2
  byte-identical — rate-consistent, not independent support.

- **New (b): 06="ent" iff pre=82 conditioned islet → recommend LEAD.**
  n=4, n_eff=3 (@579 "ne-ment", @737, @1183/@1354 in T4); F33-form with
  stated falsifier (an 82-06 window in a verbal frame); shores the
  "-ment" leg both (a2) and (c) need. Conditional fork aid: IF 37="le"
  (MEDIUM; pre-support 59→37×6 "est le", 52→37×4 "pas le"; fol-tension
  37→11=2 *"le la"), then (a1) dies at @1180 ("le le") and @1180 reads
  "le gouvernement" — the modal diplo left-collocate (43.4%).

- Enlightenment: the diplo corpus did NOT dissolve the rate kill (E
  stayed ~31, kill p=4.1e-4) — the rescue was the homophone PAIR hitting
  dead-center, and the saturation then caps the model space (no fused
  l'V cells). The non-ear on/il discriminant N35 wanted was hiding in
  the 46→62=0 datum's qu'-elision rate asymmetry (21:1), not in a new
  cell hunt. And round-7's "93 shape-STRONG" evaporated on recompute
  (vow=1) — the archived JSON doesn't contain 93 at all.

- For the report: 93/62 section — M_hom 32 vs 31.26 (p 0.47–0.60),
  93-alone p=4.1e-4, L_B LR=21.3, L_A 4 windows vs diplo l'+il=0,
  93→52=2 adverse fenced. 77/78 section — support NULL, fork (a2)/(c)
  unresolved, 06="ent"-iff-pre=82 islet n_eff=3 → LEAD, @1351
  *"ne gouvernement pas"* tension (48="ne"-LEAD ∧ 52="pas"-STRONG ∧
  5-mer="gouvernement" can't all hold — weakest is 48, WO-1's).

- Caveats: M_hom is LEAD not provisional (shape legs weak-positive;
  52-third-reading cost unevidenced); L_A conditional on M_hom;
  L_B single-datum + compositionality assumption; 37="le" unresolved;
  @1351 tension unresolved (flagged for homophonist); 48 battery not
  attempted (WO-1); "Mehemet-Ali"/16/84/00/47/67 untouched (other WOs).
