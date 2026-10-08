# RECONSTRUCT THE TABLE — attack plan from the Table Reconstructor

Date: 2026-10-07. Lane: zeschau-seebach-1841. Author role: senior historical-cryptanalyst mind, reporting direct (no coordinator).

## Thesis

Stop guessing values one cell at a time. R5005 is a 96-cell French petit-chiffre nomenclator built on known design grammar (homophone budget ~10–20%, stem+completion packing, no nulls, 1690 homophone discipline). The lane has 12 values, 10 conditioned islets, contact profiles for all 96 groups, and a phase map. That is enough to reconstruct the table's ORGANIZATION — which cells are homophones of which, which "conditioned readings" are actually multi-cell words, and where the missing cells must be. A reconstructed table turns the cipher from a 96-unknown substitution into a segmented word-level problem, which is exactly what the solver side needs (word boundaries kill the morpheme-salad).

## (a) The table's anatomy — 96-cell allocation model

Petit-chiffre design grammar (from `data/historical-context/french-petit-chiffre-doctrine.md`, Grande Armée reference: 144 cells, 10 homophone sets / 22 groups, all on frequent syllables):

| Tier | Cells | R5005 evidence |
|---|---|---|
| Ultra-frequent syllables WITH homophones | ~20–25 | Top-10 groups take only 24.3% of traffic (flat — see below); Grande Armée puts homophones on es/la/I,J/pu/ar/ca/di/fo/ga/in |
| Single-cell common syllables | ~30–35 | The n=10–20 middle band (35 groups) |
| Single letters for by-ear spelling | ~10–12 | 82=m, 34=i confirmed GT; needed for proper nouns (Mehemet-Ali) |
| Stem+completion family cells | ~10–12 | 06/86 complementary distribution (Fisher 7.3e-06): finite/imperative vs infinitive-complement = stem allomorphs, exactly like Grande Armée 22 → ar/arme/are/ars/armement |
| Digits 0–9 | ~8–10 | 8 groups have n<5 (1–6 occurrences); a despatch carries dates ("18", "janvier", "1841", "15 juillet"). UNTESTED — work order below |
| Nulls | 0 | Doctrine: petit-chiffre has none; upstream null tests showed no gain. Do not hunt nulls. |

**The flatness datum (computed this session, repaired 1,847-pair stream):** top group (00) is 2.98% of traffic; top-10 share 24.3%; top-20 share 42.0%; 39 groups have n≥20; 74 have n≥10. Natural French syllable Zipf would put the top 3–4 syllables at 15–20%+ combined. This flatness IS the 1690 order made visible: frequent syllables are split across homophone cells, and the clerk cycles ("not always repeat the same cipher character"). The distribution is already telling us the homophone budget is real and large.

## (b) Candidate homophone sets — with evidence

Method (this session): cosine similarity on concatenated predecessor+successor contact vectors, repaired stream; mutual nearest neighbors; same-phase filter (the homophonic fleet proved aliasing is contact-coherent — true homophones share phase); 1690 uniformity test (within-set frequencies must be roughly uniform: χ² vs uniform, ratio < 2).

| Set | n | Phase | Mutual sim | Uniform? | Proposal | Status |
|---|---|---|---|---|---|---|
| {33, 86} | 25, 32 | B, B | 0.70 ↔ 0.70 | ✓ χ²=0.86, p=0.35 | Infinitive/verb-stem homophones. 33 = infinitive-CLASS (round 11: follows "pour"×8); 86 = verb-stem-class (F40). Both live in "pour"-frames. | PROPOSE — strongest set |
| {48, 94} | 38, 37 | B, B | 0.64 ↔ 0.64 | ✓ near-perfect | Same contact class as 94="ne" (prov-strong) but 48≠"ne" (F60 killed it kill-grade). 48 is a ne-DISTRIBUTED syllable — same frames, different value. French blitz: vowel-initial candidate. | PROPOSE — constrains 48 |
| {47, 87} | 28, 32 | A, A | 0.50 ↔ 0.50 | ✓ ratio 1.14 | Both "ce"-valued; merger KILLED (F56) by interchangeability. Predecessors differ sharply: 87←24("en")×10 ("en ce" frames), 47←scattered. = POSITIONAL ALLOPHONES, not free homophones — "ce" after "en" vs elsewhere (cf. ce/cet split). | PROPOSE — explains the F56 kill |
| {52, 59} | 27, 27 | C, C | 0.56 ↔ 0.56 | ✓ identical | 59="est" provisional; 52 unidentified (F33 group). 52 is "est"-DISTRIBUTED. | PROPOSE — test 52 in "est" frames |
| {76, 78} | 21, 31 | C, C | 0.54 ↔ 0.54 | ~ ratio 1.5 | 78={ver,er} fork. 76 shares the value or a related cell. | PROPOSE — test 76 in ver/er frames |
| {12, 32} (+62) | 23, 13 | A, A | 0.52 ↔ 0.52; 12↔62=0.51 | ~ | "on"-class: 62="on" fenced strong. 12/32 are pronoun-adjacent cells. | WATCH — test frames |
| {82, 42} | 39, 20 | A, A | 0.55 ↔ 0.55 | ~ ratio 1.95 | 82=m GT. 42 is m-adjacent (m-initial syllable or spelling cell). | WATCH |
| {17, 67} | 15, 38 | A, A | 0.51 ↔ 0.51 | — | 17="fois"-WEAK; 67=et/veut fork. Shared "le"-adjacent contexts, probably not shared value. | WATCH only |
| {24, 79} | 52, 18 | C, C | 0.51 ↔ 0.51 | ✗ ratio 2.9 | FAILS uniformity. Similarity from shared contexts, not shared value. 79's 18 windows show no "en"-frames. | DEMOTE |
| {06, 44} | 44, 15 | B, B | 0.54 ↔ 0.54 | ✗ ratio 2.9 | FAILS uniformity. 44 is not a 06-homophone. | DEMOTE |
| {40, 80} | 21, 17 | A, B | 0.52 ↔ 0.52 | — | Phase mismatch (contact-coherent aliasing predicts same phase). | DEMOTE |
| {85, 87} | 14, 32 | R, A | 0.57 ↔ 0.57 | — | Phase mismatch. | DEMOTE |
| {66, 86} | 19, 32 | A, B | 0.60 ↔ 0.60 | — | Phase mismatch despite high sim. | DEMOTE |

**R-phase note:** 20 groups are contact-profile outliers (R = residual clusters beyond the top-3 Jaccard cut). R is not a phase — it's the "unclustered" bin. Do not treat R as linguistically meaningful; DO mine it for digit candidates and proper-noun spelling cells (outlier profiles are what rare-use cells look like).

## (c) Conditioned islets vs separate cells — the compositional test

**The paradigm question.** Every "conditioned islet" in the registry has the form G=V iff pre∈S. There are three logical possibilities:

1. **True conditioned polyvalence** — one cell, two readings, context decides. (Weird for a nomenclator; the table would list both and the clerk chooses.)
2. **Two homophone cells misidentified as one** — but then the 1690 order predicts UNIFORM cycling across contexts, not predecessor-segregation. Segregated-by-predecessor is evidence AGAINST free homophony.
3. **COMPOSITIONAL BIGRAM** — the "conditioning predecessor" is the other half of a multi-cell word. The cell may be monovalent; the "rule" is a WORD rule, not a cell rule.

**The three cleanest islets are all compositional (computed this session):**

- **84="en" iff pre=82** → 82-84 = "m'en" (82=m GT). The "condition" pre=82 is the "m". The 66/89 arms are "[noun] en [verb]" («ce que [66] en [26]») — also compositional pronoun frames.
- **06="ent" iff pre=82** → 82-06 = "m"+"ent" = "ment" (@1351: 78-94-82-06 = "[78] ne ment [pas]"). The "ent" is a verb ending; "m" is the stem's final consonant. Compositional.
- **00="le" iff pre=96** → 96-00 = "par le". Compositional. (00="pour" elsewhere may be genuine polyvalence — or "par le" may be the only "le" and 00 is otherwise "pour".)
- **87="ce" after 24** → 24-87 = "en ce" (24="en" precedes 87 ten times). Compositional — and this REFRAMES the F56 merger kill: 47 and 87 aren't failed homophones, they're positional allophones ("ce" after "en" vs elsewhere).

**THE TEST (for each islet G=V iff pre∈S):**
1. **Lexical-bigram check:** do the pre-G bigrams for pre∈S form lexical items with V? If yes → reclassify as WORD rule; reassess G's value on its NON-compositional windows only.
2. **Residual test:** on G-windows outside S, does V still parse? If yes → true polyvalence (keep the islet). If no → the "condition" was compositional; retire the islet as a cell rule.
3. **Forced-context test (killer):** find G after a predecessor outside S where V is FORCED by an independent anchor (crib, GT neighbor). If V parses → conditioning is false, cell is monovalent V.
4. **Homophone-cycling test:** if G really has homophones, they must show UNIFORM predecessor distributions (1690 cycling), not segregated ones. Compute P(pre|h₁) vs P(pre|h₂) for each candidate set — divergence kills the homophone claim.

**Falsifier for the compositional thesis:** a single islet where the conditioning predecessor is NOT part of a lexical bigram with V AND V parses in residual windows AND the predecessor distribution is uniform. The registry's islets should be re-audited against this battery before round 13.

## (d) What the 1690 order predicts about unidentified groups

"Use the homophones and not always repeat the same cipher character" makes four testable predictions:

1. **Uniformity within sets** (§b table): a frequent syllable's cells each carry ~1/k of its traffic. Any unidentified group with n≈25–40 and a contact profile matching a known value is a homophone candidate FIRST, a new value second. Priority queue from §b: 79 (test "en"-frames, though uniformity fails — deprioritize), 76 (test ver/er), 52 (test "est"), 42 (test m-frames), 44 (demoted — find its own value).
2. **No un-split giants:** no single cell should carry a full ultra-frequent syllable. Check: the top groups (00=55, 24=52, 64=47) — are their era-expected syllable rates HIGHER than observed? If "pour" should be ~5% but 00 is 3.0%, there is a missing "pour"-homophone among the unidentified. Compute era rate − observed rate = missing mass → predicts the COUNT of the missing cell(s).
3. **Cycling, not clumping:** within a homophone set, occurrences should be INTERLEAVED through the despatch, not clustered. Test: for {33,86}, {48,94}, {47,87} — runs test on set-membership sequence. Clumping would indicate positional/allophonic use (like 47/87), interleaving indicates true cycling.
4. **The missing-mass inventory:** sum era-expected rates for the top ~15 French syllables; subtract observed rates of their identified cells; the deficit, divided by ~30 (mean cell rate 1847/96≈19), predicts HOW MANY unidentified groups are homophones vs genuinely new values. First estimate: if the top-15 syllables should take ~45% of traffic but identified cells take ~30%, ~280 occurrences ≈ 14 cells are "missing homophones" hiding among the unidentified.

## Attack plan — concrete first steps

**Step 1 — Compositional audit of all 10 islets** (1 agent, 2h). Run the §c battery (lexical-bigram check, residual test, forced-context test) against every registry entry. Reclassify each as WORD-rule / TRUE-polyvalence / KILLED. Expected yield: 3–5 islets dissolve into bigrams (84/82, 06/82, 00/96, 87/24 already shown here); the survivors are the real polyvalence targets. Falsifier: an islet passing all three tests as true polyvalence.

**Step 2 — Word segmentation from confirmed bigrams** (1 agent, 3h). Take every confirmed multi-cell word (82-84="m'en", 82-06="ment", 96-00="par le", 24-87="en ce", 11-70-82-34-29-40="la première", 87-01="c'est") and segment the stream: mark word boundaries wherever a confirmed bigram/trigram occurs. Measure: what fraction of the 1,847 pairs fall inside confirmed words? Every boundary found is a constraint the solver can use. Falsifier: boundaries that force ungrammatical parses elsewhere.

**Step 3 — Homophone-set batteries** (3 agents, parallel). For {33,86}, {48,94}, {52,59}, {76,78}: pre-registered frame tests — does the unidentified member parse in the known member's frames? Uniformity χ² + runs test (cycling vs clumping). Each set gets PROMOTE (homophones confirmed) / SPLIT (positional allophones like 47/87) / KILL. Falsifier per set: predecessor-distribution divergence (for homophony) or a shared frame (for split).

**Step 4 — Missing-mass inventory** (1 agent, 2h). Era syllable rates (diplomatic corpus) vs observed cell rates for the top-15 syllables; compute the missing mass; name the unidentified groups that must be homophones by elimination. This turns "48 is unidentified" into "48 is the ne-class homophone" — a much smaller search space.

**Step 5 — Digit hunt** (1 agent, 1h). The 8 groups with n<5: test digit behavior (isolation, date contexts — look near the despatch's date references; "18", "janvier", "1841", "15", "juillet"). Petit-chiffre uses dedicated digit cells. Falsifier: the low-n groups show syllable-like contact profiles instead.

**Step 6 — Feed the solver.** Hand the word-segmentation + homophone sets to the Smith (side-homophonic-rebuild): word boundaries are the missing input to Track C (boundary-informed scoring), and confirmed homophone sets collapse the search space (96 unknowns → ~80 with 8 sets tied). The table reconstruction and the solver are not two projects — the table IS the solver's prior.

## What a reconstructed table unlocks

1. **Word boundaries** → the language model stops being fooled by morpheme-salad (salad has no word structure; real segmentations do). This is the direct fix for the Goodhart failure.
2. **Homophone sets** → the joint-inference search space collapses: tied cells move together, cutting ~15 unknowns.
3. **Positional allophones** (47/87, 06/86) → stop spending batteries on "mergers" that are really complementary distribution; test complementary pairs with Fisher tests, not interchangeability.
4. **The missing-mass list** → every unidentified group gets a prior (homophone-of-X vs new-value), replacing uniform ignorance.
5. **A falsifiable table** → the endgame: propose the full 96-cell table, then test it by deciphering forward from the cribs. A wrong table dies fast; the right one reads French.

## The paradigm's weakest load-bearing assumption

The lane's entire conditioned-polyvalence program — ten registered islets, the conditioner agent, the F33 case law, rounds of batteries — treats each group as an independent cell whose READING varies with context. But the three cleanest islets dissolve on inspection into multi-cell words: 82-84 is "m'en", 82-06 is "ment", 96-00 is "par le", and 87's "conditioning" predecessor 24 is the "en" in "en ce". The "conditioning rule" in each case is not a property of the cell at all — it is the other half of the word, misattributed to the cell because the lane scores groups instead of segmenting words first. If this compositional reframing generalizes, then a substantial fraction of the "conditioned polyvalence" infrastructure is modeling WORDS while believing it models CELLS: the islet registry would need re-auditing as a phrasebook, the merger-kills (F56) would need re-reading as complementary-distribution findings, and the correct next step is not more cell batteries but word segmentation of the stream — after which several "conditioned" values may turn out to be monovalent cells that were never polyvalent to begin with. The assumption holds up the most downstream work and has the most positive evidence against it; that is what makes it the weakest.
