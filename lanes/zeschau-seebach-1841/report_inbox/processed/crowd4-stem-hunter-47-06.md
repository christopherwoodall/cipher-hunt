## stem-hunter: 47 resolution + 06 stem (round 4, crowd4)

- Context: WO4 tasked me with (a) resolving 47 — the @148–150 jar, the
  802× "par me" contradiction vs the "même" joint — (b) identifying the 06
  stem via the 06→29×5 infinitive frames, and (c) recovering the
  encipherer's syllabary from `data/upstream-syll*.py` as shared
  infrastructure (`code/crowd4/syllabary4.py`). All counts re-derived from
  the pair stream (R5005 only); era legs are word-space only (F30).
  Canonical numbers: `code/crowd4/stem47_06_results.json`.

- Decision:
  **47: "me"-as-word KILLED; 47="ce" WORD is the LEAD (polyvalent with
  87); the "même" joint survives as a FRAGMENT reading; the @148–150 jar
  is BOUNDED (not fully resolved). 06: verb-stem CLASS sustained
  (provisional); the specific stem ("demand-"/mɑ̃/) NOT revived —
  frequency refutes any single -er stem; new two-stem complementary
  distribution found (06 finite/imperative vs 86 infinitive-complement).**

- Why:
  *47.* All 28 windows enumerated. Raw word-space battery over 29
  candidates: **"ce" is the only survivor** — B1 "ce que": cipher 3/28 =
  0.1071 vs era 122/1134 = 0.1076 → **1.00× exact**; C1 "par ce":
  2.85× (era-attested, n=13); A unigram 2.87× (context). Every rival dies
  on ≥2 hard zeros: "me" — "par me" era n=0, "me que" era P=0, "me la"
  era P=0 (the 802× contradiction, hardened: word-space it's a hard zero,
  not 802×); "mes"/"met" ("mes que", "par met" ✗); "dans" ("dans que"
  ✗); "le"/"les" ("le/la que" ✗). 47→11 ×3 reads as "cela" (ce|la cut,
  R1-R4 legal; 87→11 ×7 is the parallel "cela" with 87). The ×5
  47→78 joints are FORCED fragments ("ce"+"me" ungrammatical as words;
  no era word contains "ceme" except -cement forms) → polyvalence:
  47=/sə/ word "ce" + /m/-fragment in "même"=me|me (37→78 ×4 convergent,
  era-coherent). @150–152 = 96-47-46 = **"par ce que"** ✓ (era n=13) —
  47's slot in the jar resolved; residual is the verbless "ce qui __ par
  ce que" = the 64 slot (WO-7's problem: 64="qui" re-promotion blocked).
  *06.* 06→29 ×5 confirmed (recount; a phantom 6th at @1391 was my
  misread of the @1390 window — corrected). Only viable parse of X+"er"
  is stem+infinitive: all 12 grammatical-particle candidates (de/re/le/
  ne/se/me/ce/que/te/on/en/y/à) die on X+"er". 06→11 ×4 = imperative+"la"
  (bigram-closer corroborated). 82→06 ×4 takes zero verb-continuations vs
  5/4/6 elsewhere → distinct value ("ent"), class holds. **New:**
  00→86 ×12 vs 00→06 ×0, and 06→{11,00} ×8 vs 86→{11,00} ×0 — 06 is the
  FINITE/imperative stem, 86 the INFINITIVE-complement stem ("de"+86-er);
  F31 two-stem system sustained with mechanism. **Specific stem NOT
  identified:** 06-verb ≈13 frames/958 words ≈13.6/1000 vs era "demand*"
  0.20/1000 (**66×**; even top era -er stems "donn"/"port" ~1.1/1000 are
  10×+ short) — no single -er stem fits; N17's crib contradiction stands
  (R2-inconsistency defense is LEAD-grade only); "[06-er] veut [86-er]" ×2
  (@1095, @1387) is ungrammatical as one clause under 67="veut" → the 5
  frames may span 2+ infinitives. "premier" killed (70→06 = 0×).
  *Syllabary (c).* `upstream-syll*.py` implements 180 units (24 letters +
  156 syllables); all three annealers failed → the off-the-shelf inventory
  is NOT the encipherer's table. Recovered rules banked in
  `code/crowd4/syllabary4.py`: **R1** cells are 1–4 letters, 1-letter cells
  exist (crib 82=m, 34=i); **R2** cuts are by-ear and inconsistent
  ("personne" = 93|52|94 per|so|nne @160 vs 77|62|94 pers|on|ne @507 —
  positions verified); **R3** mute -e is WRITTEN by default (crib
  "première" → er|e with 40="e"; "erre"=29|40 @684) — unwritten-mute-e
  models need their own evidence (N17); **R4** morphological endings are
  cells (29=er word-final-ish). Module also banks F30-legal instruments:
  era word unigrams/bigrams, P(w|prev-ends-in-X), and an R1–R4
  segmentation enumerator for fragment-leg testing.

- Enlightenment: the 802× "contradiction" dissolved on re-derivation —
  it was never 47's problem as a *fragment*; word-space shows "par me"
  is a hard zero (n=0), which kills "me"-as-word three ways independent
  while leaving the "même" joint untouched (different linguistic level).
  And the 06/86 complementarity (00→86 ×12 vs 00→06 ×0) fell out of a
  routine predecessor table — the two stems aren't just "two verbs",
  they're in different syntactic slots (finite vs infinitive-complement),
  which is a stronger claim than F31 and constrains both identifications.

- For the report: belongs in the 47 and 06/86 findings sections. Numbers
  that matter: 47="ce" B1 **1.00×** (3/28 vs 122/1134), "par me" era
  **n=0**; @150–152 "par ce que" era n=13; 06→29 ×5 / 06→11 ×4 /
  00→86 ×12 vs 00→06 ×0; era "demand*" 0.20/1000 vs 06-verb ~13.6/1000.
  Files: `code/crowd4/syllabary4.py` (shared), `code/crowd4/stem47_06_final.py`
  + `code/crowd4/stem47_06_results.json` (all numbers).

- Caveats: 47="ce" is LEAD, not promotion — needs C2 (..er→ce 12.6×)
  explained, the 64 adjudication (WO-7), and red-team review; polyvalence
  cost vs provisional 87="ce" unpriced. 06 stem unidentified (bounded);
  "[06-er] veut [86-er]" ×2 unresolved — could weaken the infinitive
  reading of those two frames. 77 ("pas"/"que") unresolved → 06→77 ×6
  treated as neutral. Era = Tocqueville essays, not despatches (register
  caveat stands; the 66× frequency gap is robust to it, the 2.85× C1 less
  so). No GitHub push. No crack claim.
