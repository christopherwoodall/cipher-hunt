## red-team: round-3 kill review
- Context: I held kill authority over every new CONFIRMED claim in round 3
  (closer, morphologist, stem hunter, scorer smith + the tuner's phase work).
  I re-derived every cipher count from `load_pairs()` and every era rate from
  Tocqueville t1+t2, attacked each methodology, and built the strongest rival
  reading I could for each claim. Full verdicts:
  `code/crowd3/red_team_results.{md,json}`.
- Decision: **2 KILL-grade actions, 7 demotions, 4 upholds.** KILLED:
  stem hunter's 06=/mɑ̃/ "demand-/command-" CONFIRMED — the phonetic mute-e
  model is contradicted by ground truth (the crib "première"=pre|m|i|er|**e**
  writes 40="e" for a mute final -e, so "demande pas"=?+06+77 is impossible;
  observed 06→40→77 is 0×). DEMOTED to PROVISIONAL: closer's 87="ce"
  CONFIRMED, morphologist's 94="ne" CONFIRMED, stem hunter's 06-verb-stem,
  06-polyvalent, 67="veut"-class, 77="pas", and the "tension DISSOLVED".
  77="que" REFUTED downgraded to DISFAVORED. UPHELD: morphologist's
  06="ent"-general REFUTED (two legs downgraded), the -ment family PLAUSIBLE,
  scorer BROKEN-ON-CONTROL, tuner NULL.
- Why: the two promotions that matter most both failed on their load-bearing
  legs. The closer's 87="ce" CONFIRMED rests on a .md whose headline ratios
  (1.15×/1.10×) don't reproduce from the archived code (JSON gives 1.89×/
  1.98×, que-leg at the band edge), recycles the dead 24="est" number as
  "independent" register corroboration, and carries the cela-leg (7/32, most
  distinctive) failing the era instrument at 5–12×. The morphologist's
  94="ne" CONFIRMED leans on a phase instrument the tuner falsified the same
  hour (A=medial: 0/4 anchors) and a trigram rate that equally fits the live
  rival 94="re" ("-rement": 1.28× vs "nement" 0.66× — both in-band). The
  stem hunter's four CONFIRMEDs were built on a contaminated V29 (4/10
  members are ground-truth non-stems), circular compat (06→77 counted as
  "verb continuation" while 77="pas" was under test), and unconfirmed bonus
  leads (21="les", 33="stem") used as confirmation legs.
- Enlightenment: two things. First, the **tuner falsified the phase→position
  mapping the same hour the morphologist used it** — LOO 2/34 vs baseline
  6/34, plus a 67× 'er' segmentation mismatch (cipher 29 is 2.55% of pairs,
  corpus bare-'er' 0.038%) that uncalibrates every "er"-based rate check in
  the lane. Second, the **crib kills cleanly**: "première" writing mute -e
  as 40 is a one-line refutation of the whole phonetic mute-e edifice — the
  strongest kills come from the seven pencil values, not from rates. Also:
  the 06-tension resolved by synthesis, not by killing a methodology — F21
  verb-stem (class-level, provisional) is the better general reading by
  worker convergence; "ent" survives only as restricted-PLAUSIBLE on the 3
  -ment trigrams.
- For the report: belongs in the round-3 red-team section. The numbers that
  matter: cela-leg 7/32 CI [0.110,0.388] vs era 0.018–0.040 (fail) / Les Mis
  0.131 (pass); trigram 3/1844=0.163% vs rement 0.128% / nement 0.246%;
  64→77×3 vs era P(pas|"qui")=0/2360 (new anomaly blocking 64="qui"
  re-promotion); 06→29×5 vs era ne+er-initial 0/1793 (ne-kill stands);
  tuner LOO 2/34 vs 6/34 and the 67× 'er' mismatch.
- Caveats: elision handling still uncalibrated; injectivity now questioned
  (no validated replacement model); 94="re" is red-team-constructed,
  not worker-tested; the closer's Les-Mis figures are the closer's inference
  (audited); era corpus remains Tocqueville, not despatches. No GitHub push
  (per WO). No crack claim.
