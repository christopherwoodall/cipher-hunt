# FRENCHMAN round-10 — era/register gates on all round-10 live questions

Role: 1841-diplomatic-French authority. Era standard: **Nesselrode v8 strict**
(92,594 tokens, elision-split tokenizer per F53); dispersion on primary
(372,668), diplo set (ness8 + guizot-mémoires-t5-t6 = 391,210), diplomatic_all
(4,218,106). Code: `code/crowd10/frenchman/era_gates10.py` (+
`era_gates10_out.json`). All other executors' round-10 packages landed during
this sitting and are ruled on below (resolver1351, conditioner59,
syllabicist48, arm1248, finisher67, watch06). Red team adjudicates every
status change; vetoes below are era rulings with corpus counts, not taste.

## Q1 — @1351 triple collision: era grades CONFIRMED (counts re-derived)

Window (repaired parse): @1349=62 @1350=48 @1351=77 @1352=78 @1353=94 @1354=82
@1355=06 @1356=52 @1357=37 @1358=64.

- **06-islet «ne ment pas»: CONFIRM — by-ear ADMISSIBLE, grammatical 1841
  French.** Exact trigram: 0/92,594 v8; 0/372,668 primary; **1/4,218,106
  all** («il ne ment pas aussi», non-diplomatic slice — negligible revision
  to round-9's "unattested"). Frame «ne [V] pas» productive: 242 v8
  trigrams. Grade stands: admissible, attestation gap noted, not kill-grade.
  (Converges with resolver1351 D2i.)
- **Gouv «gouvernement pas»: CONFIRM era-0.** 0/641 adjacent (diplo set);
  5/641 within-3 tokens ALL interpose ne+verb («gouvernement n' a pas
  donné», «gouvernement ne soit pas», «gouvernement n' était pas»,
  «gouvernement ne peut pas», «gouvernement ne seraient pas»). Kill-grade
  adverse for the gouv parse at @1351. (Converges with D2i.)
- **77="le": COMPATIBLE with the 06-islet parse** (94 as negation — 94 cannot
  be both negation and syllable). «le [78]» frame grammatical; the 78 value
  decides: «le ver» 0 v8/diplo (9/4.2M, worm-register — adverse for
  78="ver"-noun); «le»+article («le le») 0. Era verdict: **94-as-negation
  beats 94-as-syllable**; R-c («le [78] ne ment pas») is era-clean on the
  left. H1c («on» at L2 of gouvernement = 0/641, re-derived 0/40 v8) is MOOT
  (target reading dead). **H1d NARROWED: «le qui» = 0/391,210 re-derived
  (0/92,594 v8 + 0/298,616 guizot) — the fenced tension now sits solely on
  {37="le" MEDIUM @1357, 64="qui" prov @1358}, independent of the left
  parse**; flagged for the 37/64 lanes, not adjudicated here.

## Q2 — 59 conditioned frames: era grades

- **F-A 59="est"-word at @1447/@1803 («qui le 84 59»): era-ABSENT —
  VETO-grade at those two windows.** «qui le [V] est» grammatical
  **0/4,218,106** (2 raw hits both broken: «qui le concernent est»
  number-mismatch, «pour qui le pain est» different parse). Banked adverse
  CONFIRMED.
- **F-B 59=verb-final fragment (-este) in the 84-59 unit:
  FRAME-LICENSED, value cipher-side.** «qui le [V]» = 515/4,218,106,
  bisyllabic verbs common in-frame («qui le menaçait/menace/distinguent/
  nomma/remplace…»). Specific -este value: era-NEUTRAL — -este verbs exist
  (déteste 17, conteste 19, atteste 35, proteste 20, manifeste 131, reste
  1251, all-corpus) but «qui le [V-este]» = **0/4,218,106 for every -este
  word**. Caution: most -este inventory is nominal (majesté 220, funeste
  145, modeste 114, céleste 48) — a VERB-«-este» claim must draw from the
  verb list. The -este verb ID is the conditioner59's cipher-side job; era
  licenses the frame only.
- **F-C 59="est"-word elsewhere, by predecessor:** «n'est» 139 v8 (94 —
  ADMISSIBLE with elision caveat: cipher writes unelided «ne»+«est»; by-ear
  /nɛ/ over-split is lens-consistent); «qui est» 66 v8 (64) ✓; «c'est» 352
  v8 (87) ✓; «l'est» 6 v8 (93) ✓; «la est» **0** v8 (11 — needs unbanked
  11=«l'» respell) era-0 as stated; «est que» 51 v8 (@1190 84-59-46 and @216
  06-59-46 frames) ✓. Predecessors {06,61,44,86,48,68,15,16,76,83}
  unidentified → frames ungradeable, pending.

## Q3 — 48 syllable candidates: era battery + vetoes

- **V1 GENERALIZED (the round's strongest era ruling): «X pas»-adverb
  without «ne» is era-0 for ALL word-candidates X, not just verbs.**
  Battery over 28 candidates on v8 strict: every «X pas»-bare = 0/92,594;
  sole exception «grand pas» 1 («à pas lents» ×2 — «pas»=NOUN "step").
  Gate-5 census stands: all 28 bare-«pas» in v8 are non-verbal (noun or
  ellipsis). **Consequence: ANY 48=X-word at @283/@1737 (42/12-48-52) needs
  (a) 52≠adverb-«pas» there, or (b) a ne-account (48=ne-merger?
  42/12=ne-carrier?), or (c) 48 word-internal (fragment).** The standing V1
  veto extends from verb readings to all word readings.
- **Syllabicist lead-weaks — era rulings (v8 strict):**
  - 48="à": VETO — «on à» pre-verbal 0/92,594 (the 1 hit is inversion
    «consentirait on à»); «à le»[article] 0 (the 15 «à le» are
    pronoun+infinitive: «à le faire/dire/poursuivre»); «à pas»-bare 0.
  - 48="a" / 48="es": VETO — H_verb standing kill, no re-litigation.
  - 48="et": VETO — «on et» 0/92,594. («et le» 67 is real but the «on»
    frame kills it at all six 62→48 windows.)
  - 48="il": VETO — «on il» 0/92,594.
  - 48="les": VETO — «les le»[article] 0/92,594.
  - 48="te": VETO — «on te» 0/92,594 (7/4,218,106 below any bar).
  - 48="un": VETO — «on un» 0/92,594 (14/4,218,106 below bar).
  - 48="se": VETO — «se le» 0/92,594 (clitic order).
  - 48="des": VETO — «on des» 0/92,594.
  - 48="de": CONDITIONAL (their kill stands on the article reading) —
    «on de» 2/92,594 marginal; «de le»[article] 0 (the 29 «de le» are
    pronoun+infinitive: «de le voir/faire/mettre»); survives ONLY via
    77="le"-pronoun ∧ 78=infinitive-initial («de le [inf]») — narrow,
    unbuilt path.
  - 48="com": NEUTRAL — fragment; no era frame testable until composed.
    (If word-internal, V1's frame moves to the host word — cipher-side.)
- Frame-passing word-candidates for the record — {en, nous, vous} pass
  both «on/il X» («on en» 11/«il en» 26; «on nous» 11/«il nous» 16; «on
  vous» 7/«il vous» 21) and «X le» («en le» 6; «nous le» 12; «vous le» 35)
  — **but all die V1** («en/nous/vous pas»-bare 0). No word-candidate
  survives all three frames; only V1's escape hatches (a/b/c) keep 48
  alive as a word.
- H_stem: NULL (underpowered, F64) — no era ruling. F68 German-thought
  by-ear: no German-spelled 48 candidate proposed this round; standing
  rule holds (AZ attestation required for by-ear German forms; the
  'he'-cell precedent = neutral, never vetoed).

## Q4 — @1248 Gate 4 compliance

- **CONFIRM arm1248's C1 («cela») refutation with era-constituency
  evidence:** «pour cela que» ×3 v8 = 2× clause-boundary («il faut pour
  cela | que je tire/voie» — the que-clause belongs to «il faut») + 1×
  cleft («c'est pour cela que», which the cipher window cannot host:
  needs 87-01-00 contiguous, window has 87-11-00). **Bare-constituent
  «pour cela que» = 0. 67="cela" era-UNLICENSED.** REVISION to Gate 4:
  the cela-class leg is VOID — bound amended to {peu}-class + infinitive.
- C2 «peu»: LICENSED — «pour peu que l'hiver soit rigoureux» (levant,
  +subjunctive «soit») is a genuine construction; n=1 primary (2 diplo,
  16 all). Thin. («peu» = 3 letters ✓ R1.)
- C3 infinitive («empêcher»): LICENSED — «pour empêcher que
  l'alliance… redevînt» (v8, subjunctive imparfait) genuine; n=1 v8
  (6 all). Thin. Cell-size tension noted («empêcher» 8 letters vs R1
  1–4) — cipher-side call.
- **Gate 4 veto RESTATED: finite-verb arms era-0.** Zero finite verbs in
  «pour X que» middles on every corpus (the lone «dit» 1/4.2M = «tenez
  vous pour dit que», past participle, not finite).
- Wider-corpus licensed non-finite inventory (for future ≥2-leg work):
  stressed pronouns {moi 15, nous 14, lui 12, vous 6, eux 5, elle 5},
  «certain» 13, infinitives {prouver 10, établir 7, empêcher 6, croire 5,
  montrer 5, savoir 4, déclarer 4, demander 3, dire 2, reconnaître 2,
  obtenir 2, rappeler 2, constater 2, agir 2, admettre 2, éviter 2…};
  single-cell-sized (≤4 letters): peu, moi, nous, vous, lui, eux, elle,
  agir, dire. Fenced artefacts (NOT licensed without individual vetting):
  «tous» 3 (clause-boundary like cela), «médiatrice», «egypte»,
  «avoirquel» (OCR), proper nouns. 62-WO3 blocker: no era stake;
  arm1248's refutation (no 62 in ±6) noted.

## Q5 — other executors: no new readings needing veto

finisher67 = clean null (0/6 classified, no new readings); watch06 =
NULL (4-gram untestable-at-n=2; islet stands; content leg self-declared
weak — no era ruling needed); liaison-smith = constraints memo, no
readings; germanist = no round-10 package. Germanist standing
conditionals unchanged (standalone 78="er" → German "er" test;
67@1248 «dafür daß» calque test if a German-shaped arm appears).

## Veto ledger (era vetoes, with evidence)

- EV1 48="à": «on à» pre-verbal 0/92,594; «à le»[art] 0; «à pas»-bare 0.
- EV2 48="a"/"es": H_verb standing kill (no re-litigation).
- EV3 48="et": «on et» 0/92,594. EV4 48="il": «on il» 0/92,594.
- EV5 48="les": «les le»[art] 0/92,594. EV6 48="te": «on te» 0/92,594.
- EV7 48="un": «on un» 0/92,594. EV8 48="se": «se le» 0/92,594.
- EV9 48="des": «on des» 0/92,594.
- EV10 59="est"-word @1447/@1803: «qui le [V] est» grammatical 0/4,218,106.
- EV11 67="cela": bare «pour cela que» 0/3 v8 constituents.
- EV12 finite-verb 67@1248: 0 finite verbs in «pour X que» middles, all corpora.
- EV13 gouv parse @1351: «gouvernement pas» 0/641 adjacent (adverse, value-neutral).
- EV14 (generalized V1): 48=X-word ∧ 52="pas"-adverb @283/@1737: «X pas»-bare
  era-0 ∀X (v8 census: 28/28 bare-«pas» non-verbal).

## Enlightenment

Two constituency findings do the heavy lifting this round, both from
*reading the hits instead of counting them*: (1) «pour cela que» ×3 are
never a bare constituent (arm1248's L2 — voids a Gate-4 leg I myself
wrote in round 9); (2) the 29 «de le» / 15 «à le» are ALL
pronoun+infinitive, never article — which downgrades 48="de" from dead to
narrowly conditional and kills 48="à" outright. Rate tables would have
licensed both. And V1's generalization is the round's sharpest blade:
the missing-«ne» was framed as a verb problem, but «X pas»-bare is
ungrammatical for *every* word X — so 48's escape must be structural
(52-polyvalence, ne-merger, or fragment), not lexical.

Evidence: `code/crowd10/frenchman/era_gates10.py`,
`code/crowd10/frenchman/era_gates10_out.json`; round-9 gates
`code/crowd9/frenchman/`; AZ evidence `code/crowd9/germanist/az_evidence.json`.
