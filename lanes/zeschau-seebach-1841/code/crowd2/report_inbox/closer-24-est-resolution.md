## closer: 24="est" resolution (crowd round 2)

- Context: I was handed the crib-surgeon's H1 (24="est", "strong, 4 checks")
  with orders to resolve it AND try to refute it — re-validating every rate
  check against the era-matched Tocqueville corpus (never Les Mis), scoring
  the named rivals ("c'est", "sont", "ont") honestly, and recomputing the
  24-87-46 joint contradiction under era rates. I chose a five-slot battery
  (A unigram, B follower bigram, C predecessor bigram, D trigram que-rate,
  E negative-control bigram) because the slots share no counts and are
  therefore independent, and I added two rivals of my own — "de" (demanded by
  the rank-1 frequency the hypothesis claimed) and "en" (the formula hunter's
  "[pour|en] ce qui" for 24-87-64) — plus a 45-word inversion sweep, because a
  refutation that never auditioned replacements is just a complaint.
  Evidence: `code/crowd2/closer.py`, `code/crowd2/closer_results.{md,json}`.

- Decision: **REFUTED** 24="est" (not merely demoted). Killed all five rivals
  too — including my own "en", whose readings ("en ce qui", "qu'en", "l'en")
  were grammatically perfect and died 26×/4.8× on era rates. **DISSOLVED** the
  F13 joint contradiction under era rates (binomial P(0/10)=0.247, was
  9.1e-04 on Les Mis — a register artifact). Promoted nothing; 24 stays
  unidentified.

- Why: two checks fail by more than an order of magnitude — P(87|24)=0.1923
  vs era P(ce|"est")=0.0099 (**19.5×**) and P(24|46)=0.1034 vs era
  P(est|que,qu)=0.0014 (**74×**) — and two independent profile checks convict
  without needing any rate: the cipher's top predecessor of 24 is 11=la ×4,
  but "la"+"est" occurs **zero** times in both corpora, and the 24-87
  follower profile ({la:3, qui:3, que:0}) matches neither Tocqueville nor Les
  Mis (Les Mis expects ~63% que/qu there; P(0/10)≈5e-5). The C-check is the
  load-bearing leg because it is structural, not statistical: "est" needs a
  subject, so "que"+"est" adjacency is ungrammatical outside "qu'est-ce" in
  *any* register — it fails 6.6× even under dialogue-heavy Les Mis. I
  deliberately engineered the verdict to survive the register question, since
  check B's failure is instrument-dependent (Les Mis passes it at 1.6×).

- Enlightenment: two surprises. First, the beautiful readings all lied:
  "c'est cela"×3 / "c'est ce qui"×3 / "que c'est"×3 and my "en ce qui"×3 /
  "qu'en"×3 / "l'en"×4 are *grammatically* flawless and *quantitatively*
  dead — grammar without rates is not evidence, and I had to kill my own
  favorite. Second, the inversion sweep found the intersection **empty**: no
  era French word both follows "que" ~10% and precedes "ce" ~19% ("tout" is
  closest on the second at 0.117 and fails everything else). So either the
  despatch's "est-ce" density exceeds even novel dialogue by ~6×, or — more
  likely — the provisional 87=ce is wrong in the 24-87 positions, and the
  11× enrichment is a lead pointing back at the anchor, exactly as the red
  team suspected. Also: H1's "rank 1" was 0-based — 24 is actually the *2nd*
  most frequent group (00 is first at 54).

- For the report: H1 status section (24="est" → REFUTED, with the per-check
  table) and the F13 joint-contradiction section (dissolved under era rates;
  87=ce keeps PLAUSIBLE/provisional — the 0/10 no longer threatens it).
  Methodology note for F10: the "est ce" bigram family has an **11.9×**
  Les-Mis/Tocqueville register gap, larger than the 6.7× cela gap that
  motivated the era switch — "Tocqueville supersedes Les Mis" needs a
  per-bigram caveat for dialogue-driven bigrams. The 1–3 numbers that matter:
  **74×** (C-check fail, instrument-independent kill), **19.5×** (B-check
  fail, era-matched), **0.247** (joint P, era-matched — dissolved).

- Caveats: B/D/E legs assume provisional 87=ce (C and the predecessor kill
  do not — C uses only ground-truth 46=que). "c'est" rates are c+est-bigram
  approximations. Tocqueville is essay prose, not a despatch — which is why
  the verdict leans on the instrument-independent legs. 24 is unidentified;
  the unexplained facts the next hypothesis must cover are 46-24-85 ×2 and
  11→24 ×4.
