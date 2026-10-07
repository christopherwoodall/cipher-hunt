## red-team: kill-review (crowd round 2)

- Context: I am the round-2 red team with kill authority over new CONFIRMED
  claims. The Closer was about to promote 24="est" and the Formula Tester was
  circling "J'ai l'honneur de"; 64="qui" sat at CONFIRMED 4/4 from attempt 3
  without ever facing adversarial review. I re-derived every cipher count from
  `load_pairs()` and every rate from the Tocqueville corpus with attempt-3's
  tokenizer — trusting bytes, not prior prose — and scored the surgeon's four
  checks on the lane's own era standard instead of the Les Mis rates they were
  built on. Evidence: `code/crowd2/red_team.py`, `code/crowd2/red_team_results.{md,json}`.
- Decision: **DEMOTED** 24="est" (refuted as a 4-check confirmation case; stays
  a weak open hypothesis), **DEMOTED** 64="qui" from CONFIRMED to PROVISIONAL,
  **KILLED** "J'ai l'honneur de" outright, **DISSOLVED** the F13 "joint
  contradiction" framing, and ruled the factor-2 rate methodology
  **UNCALIBRATED**. Promoted nothing.
- Why: the promotion case for 24="est" was a corpus artifact — its central leg
  (Les Mis P(ce|est)=0.118 within 2× of observed 0.192) becomes a **19.4× fail**
  on era rates (0.0099; "est-ce" is dialogue, not despatch prose). The "qu'est"
  leg was never rate-checked and fails 31×; the "est cela" anomaly has era
  count exactly zero, which under the lane's own method is a refutation, not a
  lean; and the elision handling is internally inconsistent (split-elisions for
  "qu'est" but unsplit to excuse 87→24=0, where era "c'est" predicts ~29 hits
  and zero are seen). For 64="qui": the identifying check rests on provisional
  87=ce, and the factor-2 band admits two more readings ("qu'" ratio 1.50, "n'"
  ratio 1.97 — the latter essentially at the band edge), so the band does not
  identify "qui". "J'ai l'honneur de" died twice independently: the ×5 count it
  was built on is ×2 pair-aligned, and position 4 is 82="m" (ground-truth pencil
  crib) where the phrase needs "neur". The F13 "contradiction" (p=9.1e-04) was
  computed on Les Mis rates; era-matched binomial P(0/10)=0.247 — no
  contradiction at all.
- Enlightenment: the elision blindness surprised me most. The tokenizer erases
  c'/qu'/l' distinctions, so "c'est"→c+est and several checks were comparing
  things that cannot meet in the corpus — and nobody had noticed that the
  surgeon's check 4 *requires* the encoder to split elisions while the
  hypothesis *needs* it not to at 87→24. The moment the era corpus replaced Les
  Mis, three "confirmed" legs collapsed at once; the methodology was confirming
  the corpus, not the cipher. Also: no era French word explains P(87|24)=0.192
  under 87="ce" — the 11× enrichment is a genuine lead pointing back at the
  provisional anchor itself.
- For the report: sections on H1 (24="est") status and F9 (64="qui") status.
  The 1–3 numbers that matter: **19.4×** (check-3 fail, era-matched),
  **0.247** (joint-contradiction P, era-matched — dissolved), **1.97**
  (n'-rival band ratio — the band doesn't identify "qui"). Plus the kill:
  82="m" ground truth vs "neur" required.
- Caveats: elision handling of the cipher is uncalibrated (two branches, no
  test); injectivity (no homophones) is assumed — "qu'" vs 46=que is the
  concrete risk; ground-truth calibration is a single n=29 pair (inconclusive,
  not validating); Tocqueville is still essay-prose, not despatches; everything
  conditioned on 87=ce inherits its provisional status.
