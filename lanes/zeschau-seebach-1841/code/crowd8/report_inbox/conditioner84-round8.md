# 84-CONDITIONER report — round-8 WO-4: 13 free windows, noun identity, «que 84 24»

2026-10-07 · 84-conditioner agent · rules pre-registered in
`code/crowd8/conditioner84/PREREG84.md` BEFORE any new computation · evidence
`code/crowd8/conditioner84/conditioner84_results.json` + `analyze84.py` +
`analyze84b.py` · positions 0-based repaired 1,847-pair starts · era corpus =
`code/side-period/corpus` (despatches_primary: nesselrode-v8 + levant-1841-p3,
N=372,751; diplomatic_all N=4,220,440), elision-split tokenizer per F53.
**No status changes merged — verdicts below are recommendations for red-team
ruling.**

## (a) The 13 free windows — 4 classified (conditional), 9 honestly residual

Per-window verdicts (full table in `conditioner84_results.json`):

**EN-EXTENSION (conditional) — 4:**
- @154 (66-84-26) + @1151 (66-84-02): 66-84 ×2, n_eff=2. «que [66] en [26]» —
  cf. «ce que le roi en dit». Dep: 66 = noun/infinitive-class («pour 66» ×7;
  «pour» never takes subject pronouns). Successors 26/02 verb-compatible,
  nothing breaks «en».
- @276 (89-84-91) + @1378 (89-84-92): 89-84 ×2, n_eff=2, with 29-89-84 ×2
  recurrence. «[inf] [noun] en [X]» — cf. «le roi en parle». Dep: 89 =
  noun-class on THREE positional legs: 77-89 ×2 («le [89]»), 29-89 ×5
  (infinitive-object), 89-48 ×3 («[89] ne» subject). @1378: 00-86-29 =
  «pour [V-stem] er» (infinitive) immediately before 89 — converging leg.

**RESIDUAL — 9:**
- @391 (91-84-73): en-lean, n=1 — «on 91 en 73» cf. «on peut en douter», but
  91=modal unverified; singletons don't extend islets per prereg.
- @788 (65-84-06): en-lean conditional on 65="se" («s'en [V]»); 65="des"
  kills it («des en» ✗); 65's lead unadjudicated.
- @412 (53-84-51), @1021 (53-84-92): 53-84 ×2 recurs but 53 has no positional
  class signature → residual (contrast 66/89 above).
- @857 (48-84-02): adverse-lean — «ne en» unelided strained (should be
  «n'en»); 48="ne" unadjudicated (F58) so not callable adverse.
- @1501 (74-84-33): adverse-lean — «te en» unelided strained («t'en»);
  74="te" is a lead, not provisional.
- @1189 (06-84-59), @1290 (17-84-59): «[V-stem]/fois en est» — «en est» is
  common but the subjectless frame is strained; residual.
- @1418 (32-84-79): «pas [32] en [79]», 32 unknown; residual.

## (b) Noun identity — NULL STANDS (bounded, not named); islet needs re-scope

The ≥2-independent-leg naming bar is NOT met. Worse, the islet doesn't cohere
as one masculine noun:
- **L1 unigram: FAILS for every candidate.** P84=0.0135; best monosyllabic
  masculine nouns: pas 0.38×, fait 0.11×, roi/temps/point 0.08×. 84 is not an
  era-rate monosyllabic masculine noun word (13×+ gaps, beyond any calibrated
  register effect).
- **The ×2 formula «qui le 84 est» (@1447/@1803) is NOT article+noun.**
  Corpus: «qui le X est» = 2/4,220,440 — («pour qui le pain est…», oblique-qui
  rescue; «qui le concernent est…», agreement error). Neither covers
  «ce qui le [N] est» @1803 (no rescue — «ce qui» fixed) or @1447 («le qui»
  broken; rescue only iff 37=preposition, unbanked). Meanwhile «qui le X» =
  515, X overwhelmingly verbs (concerne, croirait, composent, rend, fait…) =
  77="le" PRONOUN + verb. **New lead: 64-77-84-59 ×2 = «qui le [verb=84-59]»**
  (needs 59-as-syllable, unbanked — referred, not claimed).
- **@1620 gender hole:** 11-84-78 = «la [84] [78]» — «la» + masculine noun
  ungrammatical.
- **@146/@260 syllable-successor strain:** «le [84] er/te» — successors
  29="er" (GT), 74="te" (lead) are syllables; no «le N er/te» word follows a
  monosyllabic noun, so the noun would have to span 84+suc differently per
  window — strains "one noun".
- Surviving: @1485 «le [84] en ce» compatible («le roi en fut instruit»);
  @1058/@1764 «le [84] [09]» neutral (09 unknown).
- **Recommendation:** re-scope the islet (it is not one era-rate masculine
  noun); withdraw @1803, conditionally @1447; keep the «qui le [verb]» lead
  open. Identity stays NULL.

## (c) «que 84 24» adjudicated — 84="en" REFUTED at @310/@473

- **Q1 — 24's identity holds:** 24="en" STRONG (F31); locally at @311/@474
  suc=37 («en le» = 252/4.2M, weak/likely noise but nonzero; «de le»→«du»
  contraction kills the only rival 24="de"). No kill-grade local adverse.
- **Q2 — «qu'en en» is era-absent:** «qu en en» = 0/4,220,440; «que en en» =
  0; «en en» = 0 in despatches_primary (N=372,751) and 72 noise-level in
  diplomatic_all (6× below independence; samples are OCR garbage like
  «en en en», «d entendre la messe en en trant»).
- **Q3 — adverse datum per B2:** the «qu'en» legs @310/@473 (n_eff=1) suffer
  an unrepairable break (24="en" holds; no alternative 24 reading) →
  **WITHDRAWN from en-islet support.**
- **Q4 — rivals:** 84=noun gives «que [N] en le» (still «en le»-weak);
  unresolved. The byte-identical 5-gram 46-84-24-37-78 ×2 stays an open
  residual — a repeated formula with no valid reading under banked values.

**En-islet re-scope (recommended):** F53's rule "84='en' iff pre∈{46,94,82}"
is falsified as stated (46's windows withdrawn here; 94's was already fenced
adverse). Surviving: @167 «m'en» (82=m GT, n_eff=1) + conditional extensions
66-84 ×2 + 89-84 ×2 (this report, n_eff=4). Recommend re-banking as
84="en" iff pre∈{82} (GT-anchored) or pre∈{66,89} (conditional), LEAD —
red-team to rule. The islet does NOT die; its «qu'en» core does.

## Net scoreboard deltas (recommended, not merged)
- 13 windows: 4 EN-EXTENSION (conditional), 9 RESIDUAL (2 en-lean, 2
  adverse-lean, 5 plain).
- Noun identity: NULL (bounded); islet re-scope recommended; new lead
  «qui le [verb=84-59]».
- «que 84 24»: 84="en" refuted at both windows; formula unresolved.
- Open threads for other lanes: 89 noun-class battery (3 legs banked here);
  66 class confirmation; 37's value at @1447 (preposition rescue?);
  59-as-syllable («qui le [verb]» lead); the 46-84-24-37-78 ×2 formula.
