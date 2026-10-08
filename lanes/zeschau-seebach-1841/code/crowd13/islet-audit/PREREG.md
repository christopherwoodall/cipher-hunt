# PREREG — round-13 islet-audit battery (council work order 1)

2026-10-07 · Islet Auditor → coordinator. Bars registered BEFORE any battery
runs. All counts re-derived by this auditor from
`code/side-keyhunt/repaired_offsets.json` (1,847 pairs). Corpus: clean
diplomatic pool (`code/side-period/corpus/`, nesselrode-v8 EXCLUDED from all
phrase queries, AZ German issues excluded). Only RECOMMENDATIONS — no status
changes; adjudicator rules. Settled kills are never re-litigated.

## The 4-part battery (adapted per islet form)

1. **Lexical-bigram:** do pre-G bigrams (pre∈S) form single orthographic
   words with V (or stem+syllable of one verb)? → supports WORD-RULE.
2. **Residual:** on G-windows outside S, does V parse? Yes → TRUE-POLYVALENCE
   leg. No → compositional; retire as cell rule.
3. **Forced-context killer:** G after pre∉S where V is FORCED by an
   independent anchor (crib, GT neighbor). V parses → conditioning false /
   cell monovalent V.
4. **Homophone-cycling uniformity:** if G has claimed homophones, χ² of
   P(pre|h₁) vs P(pre|h₂) must be uniform (p≥0.01); divergence kills the
   homophone claim.

## Verdict codes (recommendations only)

- **WORD-RULE** — the "condition" is the other half of a multi-cell word;
  give the re-banked word rule + G's residual value on non-compositional
  windows.
- **TRUE-POLYVALENCE** — cell genuinely carries >1 reading; context decides.
- **KILLED** — a banked falsifier fires, or a forced-context counterdatum, or
  era legs fail to reproduce.
- **INCONCLUSIVE** — battery underpowered (n_eff<2, no era leg); keep
  standing status, say so honestly.
- **CLASS-RULE** — out of battery form (class constraint, not a value
  reading); keep/re-scope on its own terms.

## Per-islet bars

### ISLET 4 — 67 et/veut fork (frame-conditioned, successor-based)
- TRUE-POLYVALENCE bar: re-derive ≥29/38 classified under fenced
  R_et4/5/6 + pre=11 veut-leg, ZERO BOTH-conflicts; era legs reproduce
  (et-la>0 & veut-la=0; et-le≫veut-le; et-par>veut-par); compositional
  overlap <10% of 67-windows inside confirmed multi-cell words;
  no forced-context counterdatum beyond the adjudicated @506.
- KILLED bar: a new BOTH-conflict, or an era leg failing (rate 0 on the
  "et" side), or a forced-context window where the successor rule's arm
  cannot parse while the other arm is anchored.
- Note: @1248 NEITHER-class is a fenced counterdatum needing a third arm —
  it does not kill the fork, it bounds it.

### ISLET 5 — 96=verb-stem iff pre==64 & suc==47 (n_eff=1)
- WORD-RULE bar: "64-96-47" is a single lexical item (it isn't —
  pre-registered expectation: FAIL).
- INCONCLUSIVE bar: census confirms exactly one 64-96-47 window on the
  repaired stream, no forced-context datum, verb-stem fails on residuals
  (96-00="par le" kills it elsewhere) → standing LEAD keeps, no promotion,
  honest singleton.
- KILLED bar: a second 64-96-47 window where 96≠verb-stem, or an
  independent anchor forcing verb-stem on 96 outside the frame.

### ISLET 6 — 66 word-class (noun/infinitive/pronoun)
- CLASS-RULE form. Keep-CONFIRMED bar: all 19 windows fit noun/infinitive/
  nous-vous-class frames; zero subject-pronoun-forcing windows; <10%
  inside confirmed multi-cell words.
- Re-scope bar: ≥1 window forcing a class outside the three (esp.
  subject pronoun), or a forced specific value by an independent anchor.

### ISLET 7 — 89 noun-class
- CLASS-RULE form. Keep-CONFIRMED bar: all 14 windows fit noun-class
  frames (incl. 24-89 «en [89]» ×3 under 24="en"-STRONG, 77-89 «le [89]»
  ×2, 89-48 «[89] ne» ×3); the 52-89 ×2 tension stays non-kill-grade.
- Re-scope bar: ≥1 window where 89 cannot be noun-class by an independent
  anchor (e.g. verb-forced by 29-89 compositional parse).

### ISLET 8 — 64-77-84-59 ×2 («qui le [V-este]»)
- WORD-RULE bar: 84-59 = stem+syllable of ONE verb at both windows
  (ISLET 10 este-arm dependent); era «qui le [V] est» = 0 (clean pool);
  «qui le X» frame verb-dominant.
- KILLED bar: «qui le [V] est» era-nonzero in the clean pool (reopens
  59="est"-word at these windows), or a banked-anchor failure at either
  window.

### ISLET 9 — 86 identity (que-family settled-KILLED; F40 verb-stem-class)
- Confirm-kill bar (re-derive, no re-litigation): 00→86 ×12 with
  P(que|pour) & P(qu|pour) era rates making «pour qu(') » adverse;
  86→consonant-initial successors (70,52,56) killing «qu'» elision;
  77-86 ×5 with «le que» era-~0.
- Part-4 bar for {33,86} homophone proposal: χ² uniformity of predecessor
  distributions p≥0.01 → survives this test (not proof); p<0.01 → kill the
  set. {66,86}: confirm phase mismatch (contact-coherent aliasing predicts
  same phase).

### ISLET 10 — 59 «est» iff pre∈{64,94,93} / «-este» iff pre=84
- WORD-RULE bar: 93-59=«l'est» and 94-59=«n'est» are single orthographic
  words (proclitic fusion); 84-59 (and the fenced 06/61/44/86-59 units)
  are stem+syllable of one verb; 64-59=«qui est» is frame (two words);
  residual word-"est" fails outside {64,94,93} (the 8 settled adverses);
  {52,59} homophone χ² p≥0.01 (uniformity survives).
- TRUE-POLYVALENCE bar: word-"est" parses in ≥1 window with pre∉{64,94,93}
  under an independent anchor (F1 unfired to date).
- Deep read: if the este-arm generalizes to "59=verb-final-syllable iff 59
  is inside a multi-cell verb word", then 59 is MONOVALENT («est» syllable)
  and the islet dissolves entirely into word-boundary placement — the
  strongest possible WORD-RULE outcome. Bar: the fenced sub-tier windows
  (@216/@1186/@448/@1715/@554) all read as verb-units with 59 as final
  syllable.

## Sanity checks (the three dissolved islets)
- ISLET 3: W06 windows at 06-positions [580,738,1184,1355] re-verified;
  82-06 reads «ment» in context; 06 residual = verb-stem-class (F21).
- ISLET 2: 96-00 at the three registered windows; 00 residual = «pour».
- ISLET 1: 82-84/66-84/89-84 windows re-verified; 84 residual open.
