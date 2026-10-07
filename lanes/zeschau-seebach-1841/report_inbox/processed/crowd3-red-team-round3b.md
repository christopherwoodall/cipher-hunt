## red-team: round-3b review (bigram closer, frenchman, segmenter)
- Context: follow-up red-team pass on the three executors that finished after
  the round-3 kill review (13 verdicts in `code/crowd3/red_team_results.{md,json}`,
  all standing except as revised). I re-derived every cipher count from
  `crib_attack.load_pairs()` and every era rate from Tocqueville t1+t2 with the
  attempt-3 tokenizer, and attacked each newcomer's load-bearing legs. Full
  verdicts: `code/crowd3/red_team_round3b_results.{md,json}`.
- Decision: **78="me" promotion REJECTED → LEAD** (two load-bearing legs
  broken); **77="pas" REFUTED-claim downgraded → DISFAVORED (strong)**;
  **77="que" DISFAVORED stands** (closer's 3-check lead doesn't overturn);
  calibration exclusion **VALID** with blast radius named; frenchman K1/K2/K4/
  K5 accepted (K4 provisional, K2/K5 scoped+conditioned), K3 conditional-only,
  K7 rejected; ear-confirmations recorded as corroboration, no status changes;
  segmenter method accepted, 25 drag targets cleared LEAD-grade; **rigid
  syllabification dead as an instrument** — explicit lane rule for round 4+.
- Why: the closer's 78="me" promotion broke on recomputation — (B-78a) the
  "e"-rival kill via era ("e","e")=0 is a syllabifier artifact (the era
  tokenizer never emits a word-final bare 'e'; the cipher's 40 IS the
  word-final mute-e writer per the crib), and (B-78b) the headline L2 leg
  divided by the wrong marginal (claimed 1.66× in-band, true 2.26× out of
  band). The "l'"-kill survived, recomputed stronger (58×, not 40.4×). The
  closer's 77 L2prov legs were hand-computed and match no archived-code
  instrument (recomputed stronger: "ce pas" 57.5×, "qui pas" 78.5×, but
  provisional-conditioned). 77="pas" earns DISFAVORED (L1 5.2–6.7× out of
  band at both syllable and word level + grammatical "ce pas" ×2 under 87=ce),
  not REFUTED (no unconditional leg). The calibration exclusion reproduces
  (181.5×/61.1×/3.3×) and voids my own round-3 "ent|er strained" leg plus the
  06="ne" ne+er-initial leg — named, not hidden. The segmenter's 5/23
  provisional-boundary miss is metric muddling (cela-internal 7/7 correctly
  <0.5) plus model weakness, not anti-evidence.
- Enlightenment: the three newcomers jointly kill rigid syllabification three
  ways — tuner NULL (phase≠position), calibration (era maximal-onset ≠
  encipherer segmentation), and the frenchman's find that **the encipherer
  spells by ear and cuts inconsistently** ("personne" as "per|so|nne" AND
  "pers|on|ne", "prend"→"pre", "première"→"pre|m|i|er|e"). This explains the
  tuner's LOO failure: no fixed segmentation can be the comparison instrument
  against a cutter this loose. What survives: cipher-side geometry,
  word-space grammatical kills ("ce pas", "la l'", "de ce qui"), ear/formula
  locks — the ear is the *better* instrument here because it tolerates the
  looseness. Also: the frenchman's @790 "qui que" window kills the closer's
  77="que" lead at its own crown example ("que qui que" ungrammatical), and
  his "qui [verbe]" reading of 64→77×3 reclassifies the round-3 anomaly as a
  77-problem, not a 64-problem (64 re-promotion still blocked).
- For the report: belongs in the round-3 red-team section + a new
  "cipher-model position" methodology note. Numbers that matter: 78 L2 true
  ratio 2.26× (out) vs claimed 1.66×; 11→78 "l'"-kill 58×; 77="pas" L1
  6.69× syllable / 5.21× word-space; "ce pas" 57.5× / "qui pas" 78.5×
  (recomputed, provisional-conditioned); calibration 181.5×/61.1×/3.3×;
  62→94 "on ne" ×8 at 1.97× in-band (recomputed, verifiable); 24→87 ×10 at
  26–31× over era P(ce|en) — the sharpest ear-vs-stats tension (24="en"
  STRONG LEAD vs failed L2prov); segmenter GT 3/3 (0.727/0.936/0.608).
- Caveats: elision uncalibrated; injectivity questioned (polyvalence now the
  working assumption for 06/52/56/62); era corpus still Tocqueville essays,
  not despatches (the genre-reclassification of the cela gap is plausible,
  unmeasured); 94="re" still red-team-constructed; recompute script was
  ephemeral (/tmp) — numbers reproduce from `code/crib_attack.py` +
  `code/crowd3/battery.py` as documented. No GitHub push (per WO). No crack
  claim.
