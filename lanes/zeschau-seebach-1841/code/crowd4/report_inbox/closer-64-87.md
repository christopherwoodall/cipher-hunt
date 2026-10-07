## closer (crowd4): 64="même" vs "qui" adjudication + 87=ce register/ci-te legs

- Context: WO6+7, THE CLOSER round 4. (a) Adjudicate the stem-hunter's 64="même"
  rival against provisional 64="qui" with a symmetric battery — every leg scored
  on both hypotheses against the same cipher evidence, F30-legal only
  (word-space grammatical/rate legs; no era-syllable-conditionals on 29/82/34/40;
  era unigrams as context; provisional-conditioned legs marked as such).
  Attack from the 77-angle as ordered. (b) Advance 87=ce via the two WO routes:
  a register-matched corpus subset test with PRE-STATED falsification bars, and
  a ci/te anchor scan. The 87 leg does not recycle 24="est" (R1 void) and does
  not condition on 96="par" (N3 circular). ≥2 independent checks throughout;
  nulls first-class.

- Decision:
  1. **64: "qui" provisional-FAVORED, "même" DISFAVORED-but-live. 64="qui"
     re-promotion block STAYS (F27, F31) — "même" was bounded, not killed
     symmetrically.** Battery 6–1–1 for "qui" (details in Why).
  2. **87=ce: register-matched subset test FAILS its pre-stated bar; ci/te
     anchor scan NULL.** The cela leg stays dead. New conditional supporting
     observation: 87-64-77-84 @1799–1802 parses uniquely as «ce qui [verbe] 84».

- Why (64 battery; all cipher counts re-derived from
  `data/upstream-ct_R5005.txt` via `code/crib_attack.py::load_pairs`;
  era = Tocqueville t1+t2 word-space, attempt-3 tokenizer):
  - L1 unigram: cipher P(64)=46/1846=0.0249. Era P("qui")=0.0110 (2.27×),
    P("même")=0.00380 (6.56×). "qui" the closer rate match (band uncalibrated
    per F20 — ordinal signal only).
  - L2 rank: cipher rank(64)=5 (46×, tied 4th with 06). Era rank("qui")=14,
    rank("même")=40. "qui" closer.
  - L3 77-angle («qui [verbe]» vs «même [verbe]»): era P(verb|"qui")=0.171 vs
    P(verb|"même")=0.027 (24-verb probe set, pre-stated in
    `code/crowd4/closer64_87.py`), 6.3× gap — «qui [verbe]» is the canonical
    relative clause, «même [verbe]» ungrammatical. The «même si» escape hatch
    is quantitatively dead: era P("si"|"même")=1/816 vs observed P(77|64)=3/46,
    binomial p=2.7e-5. Under 64="même" no 77-identity survives (pas:
    disfavored-strong N21; si: dead; verb: ungrammatical). Conditional on the
    77=verb-adjacent lead (N21). Favors "qui".
  - L4 er-leg (64→29×3, 29=er ground truth): era-zero under BOTH —
    P(er-initial|"qui")=0/2360, P(er-initial|"même")=0/816; rule-of-three
    binomial excludes 3/46 under both (p=3.0e-5 / 6.7e-4). Shared anomaly;
    qualitative lean "même" («même erreur» is idiomatic; «qui»+er-word has no
    idiomatic reading) — but the ×2 continuation is 29→40 («er e», unparsed
    under both; @290/@684), so the idiom story is incomplete. Wash, slight
    "même" lean.
  - L5 que-negative-control (46→64=0, n(46)=29): era P("qui"|"que")=0,
    grammatical zero ✓ for "qui"; era P("même"|"que")=0.00035 → expected 0.01,
    0/29 chance-consistent, neutral for "même".
  - L6 87→64×5, conditional on provisional 87=ce: observed 5/32=0.156
    (Wilson [0.069,0.318]) vs era P("qui"|"ce")=0.188 (0.83× ✓) vs
    P("même"|"ce")=0.0159 (9.84×, binomial p=1.4e-4 ✗✗). Strongest
    quantitative anti-"même" leg — but conditional on a provisional, so a
    bound, not a kill. (This corrects the stem-hunter's "survives 87→64
    ('ce même')" — quantitatively it does not survive.)
  - L7 67→64×2, conditional on provisional 67="veut": «veut même»
    grammatical («il veut même…»), «veut qui» ungrammatical. Qualitative point
    for "même" (era n("veut")=52, both era rates 0 — weak).
  - L8 64→46×1 (@790: 64-46-07): «qui que» grammatical (concessive «qui que
    ce soit» family; 07 open), «même que» ungrammatical. Qualitative, n=1.
  - L9 determiner joint (note, not a 64 leg): 21→64×2 is era-zero under BOTH
    (21="les",64="qui") and (21="les",64="même") — reads as evidence against
    21="les" (unconfirmed lead), not against 64. 11→64=0 neutral under "même"
    (P(0/44)=0.45), clean under "qui".
  - New formula: **64-77-84 ×3 byte-identical @144/@1444/@1800** — one phrase
    type (n_eff=1 for rate legs). @1800 is preceded by 87 (see 87 below);
    @144 preceded by 67.
  - The bigram-closer's "même" joint (47→78×5, 37→78×4 = "me me") is a
    SEPARATE "même"-spelling observation about 78/47/37 — it does not involve
    64 and was not double-counted here.

- Why (87 legs):
  - (A) Register-matched subset, pre-registered design: first-person-singular
    reporter-voice sentences in Tocqueville (proxy: \bje\b|j'|moi|m'|mon|ma|mes;
    791/8633 sentences) vs the rest. Metric n("cela")/n("ce"); cipher target
    0.2188; era baseline 0.0414. Pre-stated bars: ≤0.08 FAIL, ≥0.11 revive.
    **Result: R = 7/176 = 0.0398, A = 40/958 = 0.0418 — the reporter-voice
    subset does NOT behave differently.** FAIL: the genre account does not
    close the gap inside Tocqueville; the cela leg stays dead. Informative
    null (R had n(ce)=176 — a 5× elevation would have shown ~35 cela).
  - (B) ci/te anchor scan: all 16 followers of 87 checked for an independent
    pin (34=i→G "ici" test; "te"-clitic V→G/G→Vfin test). **NULL: 34→G=0 for
    every G in fol87** (34 has only 9 followers — weak test, honestly noted);
    the "te" read of 78 (87→78×2="cette") is contested by the 78="me" LEAD and
    dies on 47→78×5/37→78×4 («me te»/«te me» ungrammatical). No group admits a
    unique ci/te reading adjacent to 87 with independent support.
  - (C) Supporting observation (conditional only): 87-64-77-84 @1799–1802 —
    under (87=ce ∧ 64=qui ∧ 77=verb-adjacent) the unique fully grammatical
    joint parse is «ce qui [verbe] 84»; under 64="même", «ce même [verbe] 84»
    is ungrammatical. Inherits all three provisional statuses; corroboration,
    not evidence.

- Enlightenment: two. First, the 64→77×3 "evidence" that has been argued over
  since round 3 is a single repeated trigram 64-77-84 — every rate argument
  either side built on P(77|64)=3/46 was counting one phrase three times.
  Second, the stem-hunter's «ce même» "survival" inverted on quantification:
  5/32 at 9.84× over era P("même"|"ce") is the single strongest anti-"même"
  number in the battery (p=1.4e-4) — the lead survived as prose, not as
  arithmetic. Both are now in the JSON.

- For the report: belongs in the 64="qui"/"même" adjudication section and the
  87=ce section. Numbers that matter: battery L6 9.84× (p=1.4e-4, conditional);
  L3 verb-gap 6.3× + «même si» dead at 2.7e-5; L1 2.27× vs 6.56×; L4 shared
  era-zero (both excluded, qualitative lean "même"); 87-subset 0.0398 vs 0.0414
  baseline (FAIL); ci/te scan NULL; new formula 64-77-84 ×3 @144/@1444/@1800.

- Caveats: L6/L7/L3 condition on provisional 87=ce / 67="veut" / the
  77=verb-adjacent lead — status propagates, none is a kill. The factor-2 band
  is uncalibrated (F20): L1/L2 are ordinal signals, not exclusions. The
  register proxy tests first-person voice *within a treatise*, not diplomatic
  reportage itself — the FAIL kills the Tocqueville-subset version of the
  genre account, not every possible genre story (no despatch corpus exists in
  the lane; external acquisition on hold). 64→29→40 ×2 (@290/@684) unparsed
  under both hypotheses. 78's identity (me/ci/te) is WO2-round-4's problem —
  not touched here. Block rule honored: no re-promotion of 64="qui" without a
  symmetric kill of "même"; none achieved. Evidence:
  `code/crowd4/closer64_87.py`, `code/crowd4/closer64_87_results.json`.
