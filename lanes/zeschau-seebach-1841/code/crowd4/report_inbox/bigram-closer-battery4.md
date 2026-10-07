## bigram_closer: battery4 — B-78b repair + 77/78 re-adjudication

- Context: Round-3b red team found the promotion battery's L2 leg divided by the
  wrong marginal (B-78b: ePpre returned P(la|me) instead of P(me|la), flipping the
  78="me" headline leg from 2.26x-out to 1.66x-in-band) and that all L2prov legs
  were hand-computed, unverifiable from archived code. I rebuilt the battery as
  `code/crowd4/battery4.py` (crowd3 files untouched): marginal fixed, L2prov now
  machine-computed, new word-space era legs for function-word hypotheses
  (pas/que/le/me) per F30, N22 exclusions (29/82/34 all legs; 40 conditionals)
  enforced in code. Re-ran 77 three-way and 78 ("me" vs "e"); results banked in
  `code/crowd4/battery4_results.json`.

- Decision:
  - **78="me": promotion NOT granted on fixed legs — stays LEAD.** The repair
    confirms (not overturns) the red-team's rejection.
  - **77="pas": DISFAVORED-strong — unchanged.**
  - **77="que": DISFAVORED — unchanged** (closer's 3-check LEAD does not survive
    fixed legs).
  - **77="le": LEAD-weak -> LEAD** (one grade up, fenced — the only verdict
    movement in the round).

- Why (fixed-leg numbers; every ratio machine-computed, band 0.5-2.0
  uncalibrated = context only):
  - **B-78b before/after:** 11=la->78 x2: cipher P=0.0455. Before: era
    154/5617=0.02742 -> **1.658 in-band** (wrong marginal, P(la|me)). After: era
    154/7652=0.02013 -> **2.259 OUT of band** (correct P(me|la)). The headline
    GT leg flips against "me" — a promotion cannot stand on a battery whose
    anchor leg fails.
  - **78="me" fixed legs:** L1s 1.108 in-band / L1w 22.1 out (sense-mixed:
    era word "me" is pronoun-only); L2b 0.731 in-band (structural); L3aw clean;
    L3b "la meme"/"la mesure" n=154 coherent; rival "l'" killed (11->78 x2:
    58.0x, "la l'" ungrammatical — recompute matches red-team); rival "e" live
    (L1 1.044, fragment, untestable). Non-rate legs for "me": 2 (L3b coherence,
    "l'"-kill) — but the fixed GT rate leg fails and "e" is unkilled: no
    promotion. Net: LEAD.
  - **77="pas":** L1 5.205 (word) / 6.69 (syll) out; "ce pas" 57.5x/70.9x fail
    (n=2); **"qui pas" era-zero KILL n=3 PROV** (word-space, genuinely
    ungrammatical) — now in archived code, verifiable, but still conditioned on
    provisional 64=qui, so the grade cannot rise to REFUTED. DISFAVORED-strong
    stands; evidence strengthened (hand 16.5x/43.1x -> archived 57.5x/78.5x).
  - **77="que":** L1 1.789/1.645 in-band (context); "ce que" 1.319/0.581
    in-band PROV; "qui que" era-zero fail n=3 PROV (attestation-grade only —
    "qui que ce soit" is grammatical but absent in Tocqueville); L2b 1.783
    in-band (context); polyvalence cost (GT 46=que), cosine(77,46)=0.198, and
    the ear's @790 crown-example kill all stand. DISFAVORED stands.
  - **77="le":** L1 1.121/0.982 in-band; "ce le" fail (word era-zero,
    ungrammatical, n=2); "qui le" 4.133/4.16 out-of-band but attested 37x
    ("qui le [verbe]" x3 grammatical frame, PROV); L2b 3.021 fail. **New:**
    77->86 x5 = "le"+verb-stem (frenchman's 86 verb-stem class) — the canonical
    object-pronoun frame, a second grammatical leg (provisional-on-unconfirmed).
    2 grammatical observations + in-band L1 -> LEAD (fenced: provisional
    anchors, L2b fail, and the "le me" joint tension below).
  - **Joint frames (new, fenced on unconfirmed 78="me"):** 77->78 x7 under
    78="me": "pas me" era 0 (joint kill-grade), "que me" 455x fail, "le me"
    era 0 (joint kill-grade). 2/7 instances (@1179, @1350) sit inside the
    "77 78 94 82 06" trigram the frenchman reads as "gouvernement" — if that
    parse is right, 78="ver" there, word-internal, and the joint frames are
    contaminated. Either way it is adverse: joint tension for all three 77
    readings, or a "ver"-islet inside 78="me".

- Enlightenment: the bug's direction was load-bearing, not cosmetic — dividing
  by the hypothesis marginal instead of the context marginal turned the single
  GT anchor leg for 78 from a fail into a pass, and the promotion then rested
  on it. Fixing one denominator flipped the headline verdict leg. Second: the
  word-space instrument is merciless to function-word hypotheses in a way the
  syllable instrument was not ("la me", "ce le", "qui pas", "pas me" all
  era-zero as words while their syllable analogs were merely out-of-band) —
  because word bigrams can't hide behind sense-mixing. Third: 77's neighborhood
  is verb-saturated on both sides (pre: 06x6, 67x6 verb stems; fol: 86x5 verb
  stem), which is why "le" (pre-verbal pronoun) gained the most from the
  frenchman's 86 class while "pas"/"que" (post-verbal) kept their predecessor
  frames — the adjudication now hinges on word order, not rates.

- For the report: section "Round 4: battery repair". Numbers that matter:
  2.259 (fixed 11->78, was 1.658); 58.0 ("l'"-kill recompute, matches);
  "qui pas" word kill n=3 PROV (77="pas" stays DISFAVORED-strong);
  77="le" LEAD-weak -> LEAD (77->86 x5 "le"+verb-stem frame); 78="me" stays
  LEAD, promotion rejected on fixed legs. New adverse: "gouvernement"-trigram
  tension (78="ver" in 2 windows, fenced on provisional 94="ne").

- Caveats: all L2prov legs remain provisional-conditioned (87=ce, 64=qui);
  band uncalibrated (M3); 78="me" L1w 22.1x out is sense-mixed (pronoun-only
  era word rate vs possibly polyvalent cipher group), context not a kill;
  joint frames assume 78 is a standalone word in those windows (loose
  segmentation may contaminate); the "gouvernement" trigram parse itself
  conditions on provisional 94="ne"; 86 verb-stem class unconfirmed (reading
  unidentified); no GitHub push; R5005 only; crowd3 files untouched.
