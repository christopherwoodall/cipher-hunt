## morphologist: 47="ce" unblock leg + 67 classification completion (round 7)

- Context: Two work orders. WO-10: 47="ce" is BLOCKED on the @148–152 64-slot
  residual ("ce qui __ ce que" frame is a hapax, n=1) — deliver a second frame,
  the downstream parenthetical verb, or the frame's era rate from the period
  diplomatic corpus, or 47="ce" stays BLOCKED. WO-12: finish the 67 et/veut
  fork classification (19/38 open in round 6); "la veut" @1044–1045 pins
  67@1045 as 3sg transitive verb but not uniquely "veut". Code:
  `code/crowd7/morphologist/mine_cequi.py`, `battery67_r7.py`, `final67.py`;
  numbers in `cequi_diplomatic.json`, `battery67_r7.json`, `battery67_final.json`.
  Era for 67 legs: Tocqueville word-space ONLY (F30). Corpus for WO-10:
  `code/side-period/corpus/` (4,008,284 tokens, 34 files — Guizot, Nesselrode
  v7–v10 incl. the full 1841 run, Metternich, Pozzo di Borgo, Revue des Deux
  Mondes 1841, Allgemeine Zeitung Jan 1841).

- Decision (WO-10): **47="ce" UNBLOCKED — the @148–152 residual is resolved.**
  The period diplomatic corpus delivers the independent second leg: the frame
  "ce qui [X] ce que" is era-attested (5/4.0M tokens, rate 0.125/100k;
  Tocqueville 0) and **every filler is verb-led** — "est et" (Guizot,
  "ce qui est, et ce que j'ai à dire"), "est et attendons" (Nesselrode v9,
  "ce qui est, et attendons ce que l'avenir nous amènera"), "paraît certain"
  (RDM 1841-q2, "ce qui paraît certain, ce que la compagnie pouvait et devait
  éviter"), "renverse tout" (RDM 1841-q2, "ce qui renverse tout ce que dit
  Saint-Réal"), "arriva" (RDM 1841-q3, "ce qui arriva, ce que tout Nantes a
  vu"). **"ce qui par ce que" = 0 in 4.0M diplomatic + 0 in Tocqueville.**
  The residual's three alternatives adjudicate: (b) 96 = conditioned verb stem
  in "ce qui [verb] ce que" WINS (era verb-fillers, incl. gap-1 "renverse
  tout"/"arriva"); the "par"-reading at this slot has zero era support in
  either corpus; (a) parenthetical-verb-downstream is unfalsifiable and
  unneeded; (c) fragment substitution is excluded by Q2 (47@151 is a ce-frame:
  suc=46, pre=96 — neither fragment marker). The other two WO avenues are
  honest nulls: exhaustive cipher census finds NO second "ce qui __ ce que"
  frame (only three 47-46 in the whole stream: @151 residual, @548 pre=24,
  @864 pre=48; no 64 upstream of any 87-46; the two 64-47 @1271/@1717 are
  "qui ce", not "ce qui"), and the downstream window (@155–175) holds no
  identified verb cell. 47="ce" returns to LEAD (strengthened, +1 era leg);
  **promotion to provisional is NOT claimed here — it needs red-team
  adjudication.** New LEAD-grade conditioned reading banked: 96 = verb stem
  iff pre==64 & suc==47 (n_eff=1, F33-falsifiable; does not disturb 96="par"
  provisional elsewhere).

- Why (WO-10): The leg is independent three ways — new corpus (diplomatic,
  register-matched to a despatch; Tocqueville had 0), new instrument (gap
  1–3 frame mining, not cipher bigrams), new direction (it constrains the
  SLOT's filler class, not 47's value). The verb-filler unanimity (5/5) plus
  the double-zero on "par ce que" is the shape the WO asked for: an era rate
  for the frame. Caveats: n=5 is small (rate 0.125/100k — rare construction,
  consistent with a hapax in 1,847 pairs); OCR noise in djvu sources could
  hide a few more, but cannot manufacture the verb-filler unanimity; the
  "cela" ×2 @269/@357 corroboration (F48, red-team-verified) stands as
  corroboration only, per the WO.

- Decision (WO-12): **67 classification 29/38 (et=18, veut=11, open=9).**
  Three new F33-grade conditioning rules, each with ≥2 independent checks
  (era bigram + trigram spot + purity/BOTH audit):
  R_et4 (suc==11 → et): era "et la"=196 vs "veut la"=0 (kill); trigrams
  "et la première"=1/0, "et la"+INF=1/0; 4/4 frames clean (561, 669, 753, 996).
  R_et5 (suc==77 → et): era "et le"=185 vs "veut le"=2 — and both "veut le"
  are non-clitic ("veut le plus", "s'il le veut, le rejeter"), so the
  clitic reading "veut le [inf]" is era-0; 5/5 frames clean (638, 743, 1239,
  1400, 1597); FENCED not to fire when pre∈{21,11}. R_et6 (suc==96 → et):
  era "et par"=38 vs "veut par"=1 (the 1 is instrumental "par ses seuls
  soins", unfitting "par pour"); n=1 (@959), flagged thin. Falsifiers:
  any 67-11/67-77/67-96 frame carrying a veut pre-marker (pre∈{21,11}) —
  exactly one collision exists (@506, adjudicated below). **Zero BOTH
  conflicts** across 38 after fencing. "la veut" @1045 now triple-banked:
  (1) pre==11 veut-condition, (2) era "la et"=0 kills "et" / "la veut"=1
  attests ("on la veut forte"), (3) the given 3sg-transitive-verb pin —
  still not uniquely "veut", correctly.
  **No status change recommended: fork stays SUPPORTED** (strengthened:
  28/38 clean-classified under the fenced rules + 506 resolved, was 19/38).
  Neither "et" nor "veut" is promoted as a value — binarity IS the claim.

- Why (WO-12): The @506 collision (pre=21 AND suc=77) is adjudicated, not
  absorbed: under the standing 21="le/les" lead, "le et"/"les et"=0 is a
  GRAMMATICAL kill of et, outranking the statistical suc==77 leg (185:2);
  the fork is binary, so 506=veut (no status change vs round-6). Era joint
  "le veut le"=1 is boundary-mediated ("s'il le veut, le rejeter"), "le et
  le"=0, "les"-forms 0 — the residual trigram strain is a frame-parse
  problem (77/62/21 all provisional-or-lead), not a classification problem.
  The fence is placed on the NEW rule (R_et5), never the worker-converged
  old one. The 9 remaining open (199, 630, 633, 902, 1248, 1372, 1450,
  1519, 1623) share one property: every neighbor is value-unknown
  (08, 33, 63, 76, 16, 98, 91, 92) or the era leg is null ("pour et
  que"="pour veut que"=0 @1248). Notably @630/@633 are the doubled 67s in
  one formula "67 08 52 67 63 74 46 60" — under polyvalence the two 67s may
  differ (conditioning differs: pre 78 vs 52). Further classification waits
  on neighbor values, not on more rules.

- Enlightenment: the WO-10 leg came from register, not volume — Tocqueville
  (literary, 215k words) has ZERO "ce qui __ ce que"; the diplomatic corpus
  (4.0M) has five, all verb-filled. The cipher is a diplomatic despatch;
  the frame is a diplomatic-register construction. Era-matched corpora beat
  bigger mismatched ones — the same lesson as F10's "cela" register gap,
  now working in our favor. For 67: the "veut le" audit is a cautionary
  tale about bigram legs — both era hits were non-clitic, which is exactly
  the reading the rule needs dead; checking the INSTANCES, not just the
  count, is what makes R_et5 F33-grade rather than numerology.

- For the report: WO-10 — "47='ce': UNBLOCKED — diplomatic-corpus era leg
  (5 verb-filled 'ce qui __ ce que' frames, 'ce qui par ce que' double-zero);
  residual resolved toward 96-as-conditioned-verb; back to LEAD
  (strengthened); promotion needs red-team ruling." WO-12 — "67 fork:
  classification 29/38 (et=18, veut=11, open=9); three new F33 rules, zero
  BOTH, @506 collision adjudicated veut; fork stays SUPPORTED
  (strengthened); no value promotion."

- Caveats: (1) WO-10's n=5 era frames are few — the leg is qualitative
  (filler-class unanimity + double-zero), not a rate estimate. (2) R_et6
  rests on n=1 (@959); its "par pour" oddity under 00="pour" is cross-flagged
  to the 00-conflict executor (F47) — @959 mildly favors 00="le" at that
  window, not claimed here. (3) R_veut1 (pre==21) still rests on the 21=
  "le/les" round-2 LEAD — if that lead falls, 7 veut-frames reopen. (4) The
  96=verb conditioned reading is LEAD-grade at n_eff=1; it needs a second
  64-96-47 window or an independent 96-as-verb datum before promotion.
  (5) I did NOT re-derive the round-6 B4 numbers — I extended them; the
  extension script (`final67.py`) is the citation.
