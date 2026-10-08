# Islet Registry — round 14 (registry-restructured)

2026-10-07 · Owner: registry rewriter (red-team mandate R-IA1–R-IA7,
`code/crowd13/adjudicator/RULINGS-ROUND13.md`). Full rewrite; NOT a patch.
Status changes rule only through this file and the adjudicator's docket.

**Supersedes:** `code/crowd9/conditioner/islet_registry.md` (the round-9
"conditioned-polyvalence" registry — kept as the round-9 historical record;
do not edit). The compositional thesis is confirmed as the dominant
pattern: the old registry was modeling WORDS while believing it modeled
CELLS (F100). Of 10 islets: 5 dissolve into word/frame rules (1, 2, 3, 8,
10), 1 is true polyvalence (4: the 67 fork), 2 are class rules (6, 7), 1 is
an underpowered singleton (5), 1 is a confirmed kill (9). The
"conditioned-polyvalence" framing is RETIRED where dissolved; the 67 fork
keeps it.

Positions are 0-based repaired 1,847-pair starts, built from
`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`
(a5_03 flip). Loader: `code/crowd13/islet-audit/stream.py` (NEVER
canonical.py — it loads the obsolete 1,846-pair parse).

**Status vocabulary** (RULINGS-ROUND13 standing): GROUND TRUTH (pencil
cribs) · CONFIRMED · provisional (with conditions named) ·
provisional-conditioned · LEAD · STRONG LEAD · LEAD-fenced / fenced · WEAK
arms · INCONCLUSIVE · PLAUSIBLE · disfavored · REFUTED · KILLED ·
NEITHER-fence · UNIDENTIFIED · UNTESTED (NULL, not adverse). Provisional
anchors propagate their status to everything built on them.

---

## TIER 1 — WORD RULES (dissolved islets; compositional)

### W-est1 — 93-59 = «l'est» (orthographic single word)
- **Windows:** @103 (62-94-93-[59]: «[on] ne l'est»).
- **Status:** word rule. Dependencies: {93,8}="l'" LEAD; 94="ne"
  prov-strong; 62="on" fenced STRONG LEAD.
- **Battery (R-IA1):** lexical-bigram — 93-59=«l'est» is standard French
  orthography (no corpus needed).

### W-est2 — 94-59 = «n'est» (orthographic single word)
- **Windows:** @559 (86-94-[59]-30-67); @763 (62-94-[59]-39-88).
- **Status:** word rule. Dependency: 94="ne" prov-strong.
- **Battery (R-IA1):** lexical-bigram — 94-59=«n'est» is standard French
  orthography (no corpus needed).

### F-qui-est — 64-59 = «qui est» (two-word frame)
- **Windows:** @316 (45-64-[59]-32-94); @1210 (65-64-[59]-32-48);
  @1777 (87-64-[59]-19-48 «ce qui est»).
- **Status:** frame rule. Dependency: 64="qui" provisional (F20).
- **Battery (R-IA1):** lexical-bigram — 64-59=«qui est» frame; era
  «qui est»=66, «n'est»=139, «c'est»=352, «la est»=0/3.96M (6/6
  est-arm frames parse clean).

### W-este2 — [stem]-59 = -este verb unit (stem + syllable)
- **Windows:** firm @1190 (06-84-[59]-46-07: «[06-84-59] que», 3-cell verb
  + que-clause); @1448 (64-77-84-[59]-36-67: «[37] qui le [V-este]»);
  @1804 (64-77-84-[59]-35-94: «[ce] qui le [V-este]»); @1291 FENCED
  (11-17-84-[59]-35-94 — verb vs «la [17-84] est» ambiguous; needs 17/35).
- **Stems (fenced tier 15, R-IA1):** 84 / 06 / 61 / 44 / 86 with 59 —
  the pre=06 verb-unit (@216 «[06-59] que», @1186 «ne me [06-59] [42]»),
  frame-forced pre∈{61,44} (@448 «on [61-59] [32]», @1715 «ne [44-59] [30]»),
  pre=86 lean (@554 «[86-59] i», successor open).
- **n/n_eff:** este-arm n=4, n_eff=4 (all four ±3 7-mers distinct).
- **Status:** word rule. Era leg (R-IA1): stem+syllable of era-attested
  -este verbs — manifeste 130, atteste 35, proteste 19, conteste 19,
  déteste 15 on the auditor's v8-free pool. R-CRESTE tie-break: atteste
  FRAME-BEST LEAD — the ONLY candidate with the exact «qui le V» frame
  attested in-register ("c'est lord Beauvale qui l'atteste dans une
  dépêche", RDM-1841-q4) + 4× «le/l'»-government; the este-verb PROMOTE
  bar (≥2 independent legs + stem-ID) stays with the red team; LEAD, not
  a unique-ID promotion.
- **Banked falsifier:** F2 — a pre=84 window admitting NO era-real -este
  verb (none fired). Rests: reste EXCLUDED (intransitive; not in H0).

### 59 monovalent «est» syllable
- **Rule:** 59 reads «est» as a syllable inside the word rules above.
- **n/n_eff:** n59=27. Corrected partition (R-IA1, fences load-bearing):
  est=6 (@103/@316/@559/@763/@1210/@1777 + @1796 S5-fenced); este=4
  (@1190/@1448/@1804 firm + @1291 fenced); sub-tier=5
  (@216/@1186/@448/@1715/@554); leftovers=4 (@463/@834/@1511/@1833);
  S5-fenced=6 (@528/@624/@912/@1178/@1443/@1796 — not re-litigated);
  neutral/fenced=2 (@825 NEUTRAL per I3 RULINGS-ROUND7; @1496 FENCED:
  «[15] est en [89-noun]» vs «[15-59=reste] en [89]» — needs 15).
- **Status:** SUPPORTED. Legs: A — rates in-band on Ness v8:
  P(59|64)=3/47=0.0638 vs P(est|qui)=0.0852 (0.75×),
  P(59|94)=3/37=0.0811 vs P(est|n')=0.2298 (0.35×). C — set-valued
  -este verb ID (transitive-only; unique ID unattainable, 84 stem unknown).
  E — 27/27 census classified. S1 preserved: P(59)=0.01462 vs era
  P(est)+P(-este-verbs)=0.01369 → 1.07× (unigram was always a mixture).
- **Caveat recorded:** phonetic /ɛ/ vs /ɛst/ — the table may list two
  syllables; operationally word-membership either way.
- **Dependencies (carried):** 64="qui" prov; 94="ne" prov-strong;
  {93,8}="l'" LEAD; 86 verb-stem-class (F40 working); 62="on" fenced
  STRONG LEAD (@448); 46="que" GT; 11="la" GT (@463); 77="le"
  prov-conditioned. If any falls, the dependent arm re-opens.
- **Superseded falsifiers F1–F4** (content preserved): F1 — a pre∉{64,94,93}
  window REQUIRING word-«est» (none found; @1496 fenced-ambiguous,
  @1511/@1833 leftover). F2 — a pre=84 window admitting no era-real -este
  verb (none). F3 — a pre∈{64,94,93} window where «X est» is era-absent
  (none; @1796 «n'est le» is S5-fenced, fence stands). F4 — novel
  proclitic-«est» frame (fired once: {64,94}→{64,94,93} via @103 «l'est»;
  widening pre-registered).
- **Banked (settled, not re-litigated):** unconditioned 59="est" REFUTED
  kill-grade (8 adverses: @463 «la est» era-0, @1448/@1804 F65 + frenchman
  F-A 0/4.2M, @216 cleft-hostile, @1186, @1190, @448, @1715).
- **Reconciliation R-CD1 (recorded, not re-litigated):** ISLET-10's
  dissolution does NOT void the {52,59} SPLIT — frame premises re-anchor on
  the word rules (est-arm windows still read «qui est»/«n'est»/«l'est»; the
  -este exclusivity is about W-este2 verb-words). 52 stays UNIDENTIFIED
  with a WEAK est-arm lead (pre∈{64,94,93} only, never the este-arm;
  pre(59)=84 ×4 vs pre(52)=84 ×0, Fisher p=0.0555 marginal — the SPLIT rests
  on the linguistic principle as much as the statistic). Solver constraint:
  do NOT tie 52↔59 as homophones.

### F-qui-le — 64-77 = «qui le» (frame) + W-este1 — 84-59 = «[X]este» (word)
- **Windows (frame starts):** @1444 (37-64-77-84-59-36-67);
  @1800 (87-64-77-84-59-35-94). 84-59 is stem+syllable of one -este
  verb (W-este2).
- **Status:** frame rule + word rule. Dependencies: 64="qui" provisional;
  77="le" LEAD. ISLET 8's "UNBANKED — needs 59 polyvalence" dependency is
  now BANKED-AS-WORD (closed).
- **Battery (R-IA2):** F62's «qui le [verb=84-59]» bisyllabic-verb unit
  is the only viable parse: «qui le X» = verb-dominant frame (era «qui le X
  Y»: X=verb ~9-11/14 primary; noun+"est" parse dead — «qui le X est»
  2/4.2M, both rescued/broken; «ce qui le X est» 0/4.2M); 59="est"-as-WORD
  after 84 is era-absent («qui le [V] est» 0/4.2M for all verbs) — adverse
  datum for 59="est" at these two windows only (not globally).
- **Banked falsifier:** find «qui le [V] est» (V any) at era-nonzero in a
  second independent corpus → reopens 59="est"-word here and kills the
  syllable requirement. Auditor's «qui le X est» rescue count (2 on the
  auditor's pool, both rescued by constituency readings: «qui le
  concernent est effrayé de» — clause boundary; «qui le pain est une
  chose» — article not pronoun) recorded as the auditor's judgments.
- **Open:** identify the -este verb (84's first syllable vs era candidates);
  77="le" prov-conditioned at these frames.

### W-m'en — 82-84 = «m'en» (single word)
- **Window:** @166 (82-84 pair start). GT-anchored via 82="m" (pencil).
- **Status:** word rule (re-verified this round, R-IA3).
- **n/n_eff:** n=5, n_eff=5 for the old islet's envelope.

### F-en — 84="en" in «[noun] en [V]» frame arms (66 / 89)
- **Windows:** 66-84 ×2 @153/@1150 (84 at @154/@1151);
  89-84 ×2 @275/@1377 (84 at @276/@1378, with 29-89-84 ×2 recurrence).
- **Status:** frame rule. Dependencies: ISLET 6 (66-class) and ISLET 7
  (89 noun-class) — now class-tier (R-IA5). If either class falls, the
  corresponding arm reverts to conditional-unanchored.
- **Banked falsifier (carried):** any new pre∈{66,89} window breaking
  "en", or a 66/89 window breaking its class leg. @1665 (94-84-64) stays
  FENCED-ADVERSE. F62's re-scope fired on the qu'en arm: @310/@473
  (46-84-24 ×2 «qu'en en») WITHDRAWN, "qu'en en" era-0/4.2M (24="en"
  holds locally, no repair).
- **84 accounting (R-IA3, carried):** n84=25 = 5 arms (the registered
  frame/word arms) + 9 leftovers + 8 rescoped (84=noun rescoped — F62: not
  one era-rate masculine noun; L1 unigram fails 13×+ for every candidate;
  @1803 withdrawn, @1447 conditional; identity NULL STANDS) + 2 formula
  (46-84-24 ×2 @310/@473) + 1 fenced-adverse (@1665).
- **Leftovers (carried, unclassified):** @391 (91-84-73: RESIDUAL, en-lean
  n=1, 91 unknown); @788 (65-84-06: RESIDUAL; 65="des"/"se" REFUTED so the
  «s'en» conditional cannot fire); @412/@1021 (53-84 ×2: RESIDUAL;
  recurrence without class, 53 n=11); @857 (48-84-02: RESIDUAL; round-8's
  adverse-lean WITHDRAWN — was conditional on 48="ne", KILLED F60; 48's
  identity open); @1501 (74-84-33: RESIDUAL, adverse-lean — «te en»
  unelided strained, fenced on 74="te"-LEAD); @1189 (06-84-59: RESIDUAL —
  en-lean SUPERSEDED by the @1190 verb-unit re-read (W-este2); «en est»
  bigram era-real P=0.0156 but the subjectless «[V-stem] en est» was
  self-described strained); @1290 (17-84-59: RESIDUAL, en-lean — «fois en
  est» subject-strained, fenced on 17="fois"-WEAK); @1418 (32-84-79:
  RESIDUAL, plain, 32 unknown).
- **n/n_eff (arm):** n=5, n_eff=5.

### W-par-le — 96-00 = «par le» (single word)
- **Windows (96-positions):** @47, @465, @960 (00 at @48/@466/@961).
  Contexts: @47: 30-62-96-[00]-92-79-37 («par le [92]»); @465:
  59-42-96-[00]-33-79-80 («par le [33]»); @960: 20-67-96-[00]-86-56-41
  («par le [86]»).
- **Status:** word rule (re-verified byte-exact, R-IA4).
- **n/n_eff:** n=3, n_eff=3.
- **Dependency:** 96="par" provisional (F19) — if 96="par" falls, the rule
  breaks. "par pour" ungrammatical at all three windows.
- **Banked falsifier:** a 96-00 window where "pour" parses grammatically
  (none found). Residual: 00="pour" 52/55 (STRONG LEAD, B1/B3 blockers).

### W-ment — 82-06 = «ment» (word-final syllable unit)
- **Windows (06-positions):** [580, 738, 1184, 1355]; 82 at
  [579, 737, 1183, 1354] (verified this round on the repaired stream).
  @1351–1356 reads «le [78] ne ment pas», NOT "gouvernement".
- **Status:** word rule (re-verified byte-exact, R-IA4).
- **n/n_eff:** n=4, n_eff=3 (@1184/@1355 are the byte-identical 5-mer repeat
  77-78-94-82-06 @1180/@1351; R12 n_eff cap precedent).
- **Banked falsifier:** OWNED BY the 06-falsifier-watch agent (round 9) —
  FIRE-IN (pre=82 adverse inside domain) / FIRE-OUT (pre≠82 clean "ent") /
  FIRE-PART (W06 incomplete). See `code/crowd9/watch06/PREREG.md`.
  Status 2026-10-07: hunting; no finding reported yet.
- **Residual:** the other 40 06-windows are verb-stem-class (F21, general
  reading provisional).
- **Related (R-CRESTE):** T3 — 06="pro" stays LEAD-WEAK (proteste now
  doubly-weak but NOT killed — dictionary-transitive "protester sa bonne
  foi" keeps it alive).

---

## TIER 2 — SOLE TRUE POLYVALENCE (the 67 fork)

### ISLET 4 — 67 et/veut fork — SUPPORTED
- **Conditioning rules:** F33-grade R_et4/5/6 (morphologist round 7/8).
- **n/n_eff:** n=38; 29/38 classified (et=18, veut=11, open=9), ZERO
  BOTH-conflicts, 0/38 inside confirmed words (compositional dissolution
  fails). Open list: [199, 630, 633, 902, 1248, 1372, 1450, 1519, 1623].
- **Status:** SUPPORTED — the registry's ONLY genuine frame-conditioned
  polyvalence (R-IA6).
- **Era legs (v8-free pool, reproduced):** «et la»=4070 vs «veut la»=41
  (99:1); «et le»=3788 vs «veut le»=33 (115:1); «et par»=819 vs «veut
  par»=3 (273:1); «et qui»=2041 vs «veut qui»=2.
- **Banked falsifier + status:** @1248 NEITHER-class fenced counterdatum
  ("pour 67 que" — neither et nor veut, n=1, F63) STANDS as the bound.
  R-CR1248: @1248 NEITHER-fence STANDS (WO6 single-work-order bar; neither
  arm promotes). PC-1 granted as an attestation-breadth leg (peu arm 4/8
  → 5/9 — "craindre peu que" + subjunctive, new lemma in Guizot-DIP).
  DP-1 PERMANENT FENCE for both arms: the double-pour stack pairs
  [1244:1255] is UNLICENSED — zero genuine in ~22MB round-12 pool + the
  758k-token re-check; k-depth family absent at ALL depths k=1–5. Fence
  recorded as frame-unattested, NOT ungrammaticality evidence
  (pre-registered scope). Fork stays SUPPORTED; @1248 needs a new arm or
  fork re-scope with its own ≥2-leg bar.
- **Owner:** 67-finisher agent (round 9). Registry records bookkeeping
  only; no new 67 data touched by the conditioner this round.

---

## TIER 3 — CLASS CONSTRAINTS (out of polyvalence; specific values NULL)

### ISLET 6 — 66 word-class (F-en frame dependency)
- **Rule:** 66 ∈ {noun, infinitive, nous/vous-type pronoun} — a word-class
  after which "en" is grammatical (F62's dependency was stated as
  noun/infinitive-class; the nous/vous alternative noted honestly —
  «pour nous»/«pour vous» era-grammatical, 23/27 hits).
- **Legs:** (a) «pour 66» ×7 verified (@189/@246/@254/@715/@1109/@1494/
  @1533); era «pour»+subject-only-pronouns (il/on/ils/je/tu) = 0 — 66 is
  not a subject pronoun. (b) 66-84 ×2 windows grammatical under «[66] en
  [V]» (@154: «ce que [66] en [26]»; @1151). (c) 66's predecessor profile
  (00 ×7 dominant, then scattered) fits a content word, not a function
  word. 19/19 windows fit noun/infinitive/nous-vous-class frames; zero
  subject-pronoun-forcing windows; 0/19 inside confirmed words (R-IA5).
- **n/n_eff:** n66=19. Specific value NULL (honest).
- **Banked falsifier:** a 66-window forcing subject-pronoun or
  en-incompatible class (none found).
- **Role:** dependency of F-en (ISLET 1's 66 arm) and of the 82-arm's
  66/89-frame context.

### ISLET 7 — 89 noun-class (F-en frame dependency)
- **Rule:** 89 is noun-class.
- **Legs (re-verified on the repaired stream, R-IA5):** 77-89 ×2 («le
  [89]» @640/@871); 29-89 ×5 (infinitive-object @113/@275/@781/@1377/
  @1393, with 29-89-84 ×2 recurrence); 89-48 ×3 («[89] ne» subject
  @640/@871/@986); 24-89 ×3 («en [89]», 24="en"-STRONG, «en temps»-type).
  Full 14-window census: no kill-grade adverse. 29-89 never completes
  «premier»; 0/14 in words.
- **Fenced tension:** 52-89 ×2 («pas [89]» — bare «pas»+noun restricted;
  not kill-grade; 52="se"-rival would be worse).
- **n/n_eff:** n89=14. Specific value NULL (honest).
- **Role:** dependency of F-en (ISLET 1's 89 arm).

---

## TIER 4 — SINGLETON (underpowered; not a rule)

### ISLET 5 — 96=verb-stem iff pre==64 & suc==47 — INCONCLUSIVE
- **Window:** @149: 64-96-47 (ctx 29-87-64-96-47-46-66; «ce qui [V] ce que»
  frame; N47: diplomatic corpus yields 5 "ce qui __ ce que" frames, all
  verb-led).
- **n/n_eff:** n_eff=1. n96=21; 96-00 «par le» ×3 kills verb-stem
  elsewhere; no second window (F63's retired falsifier confirmed
  unmeetable).
- **Status:** INCONCLUSIVE (R-IA7). Standing LEAD keeps; no promotion
  case without v8.
- **Era caveat (honestly disclosed):** the 5-frame leg is v8-dependent
  (clean pool n=1, filler «arriva»); the «ce qui par ce que»=0 double-zero
  reproduces v8-free.
- **Extension test:** qui-96-43 ×2 (@341/@1025) — HOLD, not extended.
  96="par" provisional undisturbed elsewhere.

---

## TIER 5 — KILLS (retired; no re-litigation)

### ISLET 9 — 86 identity — que-family REFUTED (confirmed kill)
- **Verdict:** 86=que-family REFUTED (kill-grade, ≥4 legs).
- **Battery (pre-registered, all run):** L1 unigram P(86)=32/1847=0.0173
  vs era P("qu'")=0.00714 / P("que")=0.0114 — in-band, uninformative.
  L2 que-frame: 00→86 ×12 = «pour qu'» 12/55=0.218 vs era 0.0104
  (21× OVER); «pour que» 0.218 vs era 0.0238 (9.2× OVER) — ADVERSE.
  L3 finite-frame absence: consistent with "qu'" but also
  verb-stem-mood — weak, non-discriminating. L4 86-vs-46(que-GT) profile
  parity: predecessor Jaccard 0.33, successor 0.25, dominant contexts
  differ (86: 00→ ×12, 77→ ×5; 46: spread) — NO homophone support.
  L5 elision: 86→70 (70="pre"-GT, consonant), 86→52 ×2 (52="pas"-STRONG,
  consonant), 86→56 ×4 (56="plus"-MEDIUM, consonant) — «qu'pre»,
  «qu'pas», «qu'plus» impossible → 86="qu'" REFUTED (3–7/12 windows).
  L6 («le que» ×5): 77="le" banked at all five 77-86 windows
  (@431/@799/@878/@951/@1134); era P("que"|"le")=5/76261≈0.00007,
  P("qu"|"le")=2/76261 — «le que» ×5 at era-~0 is KILL-GRADE adverse for
  any que-family reading.
- **B3 correction (banked):** the ratemodel's caveat ("if 86 were
  que-family, B3 dissolves, 16/55=0.29 vs era 0.31") is WRONG on the era
  number: French-only Nesselrode gives que-family|"pour" = 0.0343, so
  86=que-family would make B3 16/55=0.2909 vs 0.0343 = 8.5× OVER — WORSE,
  not dissolved. And 86 isn't que-family anyway. **B3 STANDS** (3.19×).
- **Surviving working hypothesis:** F40's verb-stem-class STANDS
  (M1 F33-grade; @431 «[86]er» infinitive banked in F37); specific value
  NULL (honest).
- **Open threads:** 86-56 ×4, 86-52 ×2, 86-59 (@553), 77-86 non-29
  windows — 86's specific value needs a fresh battery beyond que-family.
- **Related (R-AB1):** {33,86} SPLIT — do NOT merge 33+86 windows in any
  downstream ID battery; 33's infinitive hunt proceeds on its 8 pour-frames
  alone; the reconstructor's §b {33,86} PROPOSE is RETIRED.

---

## Related banked solver constraints (round 13; not registry entries)

- **{48,94} SPLIT (R-AB2):** do NOT tie 48↔94 as homophones. 48 stays
  UNIDENTIFIED, constrained to a ne-class pre-verbal item ≠"ne"
  (48="ne" killed kill-grade, F60); the 48-specific "de ce que" islet
  (@863) survives untouched and counts as evidence FOR 48's own value.
  R-CR48: H_stem GAINS A LEG — 48 = vowel-initial verb-stem syllable cell
  (leg only, NOT a value promotion); @863 neither promoted nor killed.
- **{76,78} SPLIT (R-CD2):** do NOT tie 76↔78 as homophones. 76's ver-lead
  stays weak-local; the 78 fork unresolved — conditional on the 78 fork's
  er-lean; if the fork owner resolves 78="ver", the question re-opens.
- **52 unidentified (R-CD1):** WEAK est-arm lead (pre∈{64,94,93} only,
  never the este-arm).
- **74-class OPEN (R-CR48):** "74 is unlikely a verb" datum banked as
  adverse-grade, not kill-grade.
- **Missing-mass priors (R-MM1/R-MM2, PRIORS ONLY — anti-promotion fence:**
  no prior may serve as a promotion leg or status claim without a fresh
  pre-registered battery and a new ruling): 48→ne-class **P1c**;
  52→est-class **P1c**; 76→ver/er **P1**; de-pool **P2** =
  {01, 98, 14, 88, 16, 43, 44, 08, 37} (08 carries R-CC31's 08="l'" LEAD —
  the P2 contact prior and the value lead coexist as priors/leads, not
  value claims). Missing mass is in uncovered syllables (~17–20 cells
  among the 84 unidentified groups), not second cells for la/que/ce;
  identified cells run 2.9× hot in aggregate (register/granularity caveat
  carried). Digit hunt NEGATIVE → RETIRED (the 8 groups 04, 22, 27, 54,
  57, 90, 95, 99 — all phase R — are rare-vocabulary cells).
- **31=VERBAL (finite) provisional-conditioned CONFIRMED (R-CC31);**
  33 NULL constrained (R-CC33); 92 NULL constrained (R-CC92).

## Provisional anchor status carried into the registry's dependencies

- 82="m" GT; 46="que" GT; 11="la" GT; 34="i" GT; 70="pre" GT; 29="er" GT;
  40="e" GT.
- 96="par" provisional (F19); 64="qui" provisional (F20);
  77="le" provisional-conditioned; 59="est" provisional (HOLDS per
  round-12 R11 — W-est1/W-est2/F-qui-est are its word forms);
  87="ce" provisional; 24="en" STRONG (F31); 94="ne" prov-strong.

## Change log (this rewrite)

- 2026-10-07 — registry-restructured per red-team R-IA1–R-IA7 (GRANTED):
  ISLET 10 → W-est1 / W-est2 / W-este2 / F-qui-est + 59 monovalent «est»;
  ISLET 8 → F-qui-le + W-este1 (dependency BANKED-AS-WORD); ISLET 1 →
  W-m'en + F-en frame arms (66/89); ISLETS 2, 3 → W-par-le, W-ment;
  ISLETS 6, 7 → class tier; ISLET 4 → sole true polyvalence (SUPPORTED);
  ISLET 5 → INCONCLUSIVE (LEAD-singleton); ISLET 9 → kill. Conditioned
  F1–F4 falsifiers superseded by word rules (content preserved).
