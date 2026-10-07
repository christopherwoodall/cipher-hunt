# ISLET 10 (PROPOSED) — 59 conditioned «est» / verb-final — for red-team ruling

**Status:** PROPOSAL by 59-conditioner (round 10, WO2). NOT appended to the
shared registry — status changes need red-team ruling. Pre-registered as
`code/crowd10/conditioner59/PREREG.md` (2026-10-07 20:37 UTC) before data touch.

## Conditioning rule (exact)

- **59 = word-«est» iff pre(59) ∈ {64, 94, 93}** — proclitic-licensed frames:
  «qui est» (64), «n'est» (94), «l'est» (93).
- **59 = verb-final syllable («-este» family) iff pre(59) ∈ {06, 84}**
  (banked tiers) **or pre(59) ∈ {61, 44} frame-forced** («on»/«ne» frames where
  word-«est» is ungrammatical; stem identity open, reading analogy-dependent)
  **or pre(59) = 86 lean** (verb-stem-class F40, successor open).
- All other predecessors → UNCLASSIFIED (no claim).

Pre-reg narrow form {64,94} died on banked F4 (@103 «l'est» — F4 fired as
designed); widened to the natural proclitic class {qui, ne, l'}. The «c'est»
candidate @825 stays OUT (I3 hostile-neutral, RULINGS-ROUND7 — respected).

## n/n_eff

- est-arm: n=6, n_eff=6 — @103 («on ne l'est [45]»), @316/@1210/@1777
  («qui est» ×3: «qui est [32]» ×2, «ce qui est [19]»), @559/@763 («n'est» ×2:
  «n'est [30]», «on n'est [39]»). No byte-identical ±3 7-mers (census).
- este-arm firm: n=5, n_eff=5 — @216 («[06-59] que», que-clause),
  @1186 («ne me [06-59] [42]»), @1190 («[06-84-59] que», 3-cell verb),
  @1448/@1804 («qui le [84-59]», ISLET-8 frames).
- este-arm frame-forced: n=2, n_eff=2 — @448 («on [61-59] [32]»),
  @1715 («ne [44-59] [30]»).
- este-arm lean: n=1, n_eff=1 — @554 («[86-59] i», successor open).

## Supporting windows (positions = the 59-cell's 0-based repaired index; 59 bracketed)

(F65 cites these ISLET-8 windows at the 84-positions @1447/@1803; the 59s sit at
@1448/@1804. Same windows.)

- @103: 62-94-93-[59]-45-28-00 — «[on] ne l'est [45]»
- @316: 78-45-64-[59]-32-94-06 — «[45] qui est [32] ne [06]»
- @1210: 55-61-21-65-64-[59]-32-48-96 — «[65] qui est [32] [48] par»
- @1777: 62-94-24-87-64-[59]-19-48-74 — «[ce] qui est [19] [48]»
- @559: 59-34-17-86-94-[59]-30-67-11 — «[86] n'est [30] [et/veut] la»
- @763: 29-40-20-62-94-[59]-39-88-66 — «[on] n'est [39] [88] [66]»
- @216: 77-78-06-[59]-46-29-42 — «le [78] [V-este] que er[42]…» («que er»
  wrinkle noted: clause after «que» unparsed; core «[V] que» grammatical).
  **Resolves F52's caveat 3:** L2 honestly FAILED on S4#1 (@216) —
  «[06] est que» had no licensed frame; the verb+que-clause parse supplies it
  (06 non-nominal kills the cleft per L2's own bar).
- @1186: 78-94-82-06-06-[59]-42 — «ne m[e] [V-este] [42]» ([42]=pas? open)
- @1190: 06-59-42-06-84-[59]-46-07-24 — «[06]-[84]-este … que [07]…»
  (proposed re-read of ISLET-1's RESIDUAL en-lean «[V] en est», strained)
- @1448: 64-77-84-[59]-36-67-33 — «[37] qui le [V-este] [36] [et/veut]»
- @1804: 79-87-64-77-84-[59]-35-94-52 — «[ce] qui le [V-este] [35] ne pas»
- @448: 78-41-10-62-61-[59]-32-48-79 — «[on] [V-este] [32]»
- @1715: 29-40-65-94-44-[59]-30-64-47 — «ne [V-este] [30]» ([30]=pas? open)
- @554 (lean): 46-55-81-00-86-[59]-34-17-86 — «[86-59] i» (34=i successor open)

## Legs (pre-registered; ≥2 independent required)

- **Leg A (rates, Ness v8):** P(59|64)=3/47=0.0638 vs P(est|qui)=0.0852
  (0.75× ✓); P(59|94)=3/37=0.0811 vs P(est|n')=0.2298 (0.35× ✓). In-band ≤2×.
- **Leg B (frames):** 6/6 est-arm windows parse as clean proclitic-«est»
  («qui est» ×3, «n'est» ×2, «l'est» ×1); «l'est» era 6, «c'est» 352,
  «la est» 0/3.96M (Ness v8 + diplomatic aggregate).
- **Leg C (verb ID, set-valued):** -este verb inventory on 3.96M diplomatic
  tokens: manifeste 131, atteste 35, proteste 20, conteste 19, déteste 17+6,
  reste 1246. «qui le» windows (@1448/@1804): transitive-only →
  {manifeste, atteste, proteste, conteste, déteste}; reste EXCLUDED
  (intransitive — «qui le reste» impossible). que-clause windows (@216/@1190):
  era-attested {manifeste, atteste, proteste}, grammatical {déteste,
  conteste}. «on» (@448): attested {reste, conteste, déteste}. «ne…pas»
  (@1715): attested {reste, conteste, proteste}. UNIQUE ID NOT attainable:
  84/06/61/44 stem values unknown; «qui le»+specific-verb = 0/3.96M for all
  (rare-verb expectation, not a kill).
- **Leg D (residual 84-59s):** @1190 admits the verb parse (3-cell +
  que-clause); @1291 admits a verb parse («la [17] [V-este] [35]») → banked
  F2 does NOT fire. @1291 stays FENCED (ambiguous vs «la [17-84] est [35]»).
- **Leg E (census):** 27/27 windows classified
  (`classification.json`): 6 EST + 1 NEUTRAL + 5 ESTE-firm + 2 frame-forced
  + 1 lean + 2 FENCED + 10 LEFTOVER (incl. S5-fenced ×6, not re-litigated).
- **S1 preserved:** cipher P(59)=27/1847=0.01462 vs era
  P(est)+P(-este-verbs)=0.01369 → 1.07× (the unigram was always a mixture).

## Banked falsifier

- **F1:** a pre∉{64,94,93} window REQUIRING word-«est» (none found;
  @1496 fenced-ambiguous, @1511/@1833 leftover-not-required).
- **F2:** a pre∈{06,84} window admitting NO era-real -este verb (none;
  every window admits ≥1).
- **F3:** a pre∈{64,94,93} window where «X est» is era-absent/ungrammatical
  (none; @1796 «n'est le» is S5-fenced, era 10/3.96M — fence stands).
- **F4:** a new proclitic-«est» frame on a novel predecessor (widens the
  rule, doesn't kill it — fired once already: {64,94}→{64,94,93}).

## Dependencies

64="qui" prov, 94="ne" prov-strong, {93,8}="l'" LEAD, 06 verb-stem-class
(F21 prov), 86 verb-stem-class (F40 working), 62="on" fenced STRONG LEAD
(@448), 46="que" GT, 11="la" GT (@463), 77="le" prov-cond (ISLET-8 frames).

## Leftover unclassified (10)

- @463: «la/cela [59]» — «la est» era-0/3.96M ⇒ 59≠word-«est» here (hard
  anti-unconditioned datum); value open (verb parse has clitic-order problem).
- @825: NEUTRAL per I3 (RULINGS-ROUND7) — not counted either way.
- @834: «[76] [59] [35]» — no licensed frame.
- @1511: «[12] [61] [59] [39]» — «[61] est [39]» vs «[61-59] [39]» open.
- @1833: «i [59] [36]» — 16="i" LEAD interaction; patternist lane owns 16.
- @1291: FENCED (verb vs «la [17-84] est [35]»; needs 17/35).
- @1496: FENCED («[15] est en [89-noun]» vs «[15-59=reste] en [89]»; needs 15).
- S5-fenced ×6 (@528, @624, @912, @1178, @1443, @1796) — NOT re-litigated.

## Status-change proposals (for red-team ruling)

1. **Unconditioned 59="est" REFUTED** (kill-grade, 7+ independent adverses):
   @463 («la est» era-0), @1448/@1804 (F65), @216 (cleft hostile),
   @1186 («ne me [stem] est» ungrammatical), @1190, @448, @1715.
   F52's provisional promotion is REFINED (not killed): the est-arm (S2/S3 +
   new «l'est» @103) stands inside the conditioned islet.
2. **ISLET-1 residuals @1189/@1290 re-read:** «[V] en est» en-lean was
   self-described strained; propose verb-unit re-read (@1190 firm ESTE,
   @1291 FENCED). No change to the en-islet rule itself.
3. **@825 stays NEUTRAL** (I3 respected); the 01-«est» interaction is
   untouched by this battery.

## Verdict

**Conditioned polyvalence for 59 CONFIRMED at LEAD** (pre-registered bar met:
F1–F3 unfired; F4 fired once → rule widened to the natural proclitic class;
Legs A–E pass). Recommend ISLET 10 entry as above. Red team adjudicates.
