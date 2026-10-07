# Unit inventory — Seebach cipher (INVENTORIST, crowd round 5)

Learned bottom-up from the cipher's own ground truth, not imported from French
syllabification. Every unit traces to a crib, an islet, or a cutting rule;
proof vs inference is marked per unit. All positions are on the canonical
repaired parse (`code/side-keyhunt/repaired_offsets.json`, 1,847 pairs, 96
groups; F32). Recompute everything: `python3 code/crowd5/unit_inventory.py`
(which asserts every evidence claim and emits `unit_inventory.json`).

## 1. The ground-truth nucleus: "la première" = 11-70-82-34-29-40 @754/@1034

Six groups, seven pencil cribs, every one proven. This is the entire alphabet
of the cipher's design philosophy:

| group | value | shape | n (rate) | what it proves |
|---|---|---|---|---|
| 11 | la | CV, whole function word | 45 (2.44%) | whole-word CV units exist |
| 70 | pre | CCV onset-cluster syllable | 15 (0.81%) | onset clusters are single units; ALSO writes "prend" (silent d dropped) @1329 — units follow pronunciation, not spelling |
| 82 | m | **bare consonant, single letter** | 39 (2.11%) | **the kill of rigid syllabification**: standalone `m` is phonotactically impossible in French but GT-proven. Era lexicon has "m" as a syllable in exactly 1 of 11,870 words. |
| 34 | i | **bare vowel, single letter** | 11 (0.60%) | cuts go below the phonological syllable ("mi" → m\|i) |
| 29 | er | morphological ending, word-final-ish | 45 (2.44%) | endings are units; phase-C anchor (prev-A 0.77, next-B 0.89, F11). Cipher 2.44% vs era bare-"er" 0.038% (N15; 182× bigram-closer N22) — the rate gap that voids all era-syllable-conditional legs |
| 40 | e | **mute -e WRITTEN** | 21 (1.14%) | R3: mute -e gets its own group. Kills every phonetic model needing mute-e unwritten (N17: 06→40 = 0×, re-verified this round) |
| 46 | que | whole function word (C+schwa) | 29 (1.57%) | elided compounds are ONE spoken-syllable unit: 46→62 = 0× ("qu'on" = /kɔ̃/ → one group; the by-ear model PREDICTED this zero, N28) |

The lexicon's "standard" segmentation of the same word: pre|mi|è|re (4).
The cipher's: **pre|m|i|er|e (5)**. The word-pattern fleet's ground-truth
control (82-34-29-40 tail) returns **zero lexicon candidates at every tier**
(matcher/README.md: HONEST NULL). The lexicon's unit alphabet cannot express
the cipher's units. That is the whole of the F30 verdict, reduced to one word.

## 2. Cutting rules (R1–R4; banked in `code/crowd4/syllabary4.py`)

- **R1 — cells are 1–4 letters; 1-letter cells exist.** Proven by 82=m, 34=i
  in a single word. No unit inventory may exclude single letters.
- **R2 — cuts are by ear and INCONSISTENT.** "personne" = 93|52|94
  (per|so|nne @159) vs 77|62|94 (pers|on|ne @507): same word, two cuts, one
  cipher. No fragment leg may require a unique segmentation; test the SET of
  plausible cuts. (R2 also explains the tuner NULL and F22: the encipherer's
  segmentation is inconsistent, so positional-syllable statistics skate.)
- **R3 — mute -e is WRITTEN by default.** "première" → …|er|e; "erre" =
  29|40 ×9 (@62/291/500/597/685/758/1038/1050/1710). Unwritten-mute-e
  readings need their own positive evidence.
- **R4 — the table mixes letters, syllables, endings, and whole function
  words.** 11=la and 46=que are whole words; 29=er is a morphological ending.

Ear-spelling regularities (beyond cutting, all frenchman-verified):
- silent consonants dropped by pronunciation: "prend"→"pre" (70) @1329
  ("on ne prend pas" lock);
- monosyllabic elisions fused: "qu'on" → one group (46→62 = 0×);
- compounds from word-units: "cela" = 87-11 ×7; "parce que" = 96-87-46 ×3.

## 3. Lane-inferred units (status-marked; the 10 valued groups)

| group | value | status | n | key behavior |
|---|---|---|---|---|
| 87 | ce | PROVISIONAL-strengthened (F27) | 32 | 87→11 "cela" ×7 (P=0.219); 87→46 "ce que" ×3; 87→64 ×5; 14 distinct predecessors. cela-leg register-dependent (N27). Everything downstream inherits this status. |
| 64 | qui | PROVISIONAL, re-promotion BLOCKED | 47 | 24-87-64 ×3 formula (value withheld, F17); rival 64="même" demoted→disfavored (N27); 64-77-84 ×3 is one byte-identical trigram (n_eff=1) |
| 96 | par | CONFIRMED 4/4 on repaired C1 leg; inherits 87=ce provisional status (F28) | 21 | P(87|96)=0.1429 vs syllabary-aware predicted 0.1130 (1.26×); 96="de" REFUTED |
| 94 | ne | PROVISIONAL-strong (F24, N24) | 37 | era syllable rate 1.025×; 94-82-06 ×3 with GT 82=m centered; "on ne prend pas" lock @1329; rival 94="re" demoted→disfavored (word-space host odds 2.27:1) |
| 06 | verb-stem-class | PROVISIONAL (F25, N29) | 44 | 06→77 ×6, 06→29 ×4 (infinitive frames), 06→11 ×4, 06→00 ×4; 30 predecessors. Specific stem NOT identified; 06=/mɑ̃/ KILLED (N17); 06="ent" general REFUTED (N19) |
| 67 | veut | PROVISIONAL (demoted CONFIRMED, N18) | 38 | modal-governor + 06 lexical-stem = the live verb-system picture |
| 62 | on | STRONG LEAD (N28; promotion held for an instrument-independent 3rd leg) | 35 | 62→94 "on ne" ×9 @0.2571 (2.18× era, repaired; a5_03 region contributes a 9th @761); pers\|on\|ne @507; fresh-window subject triangulation zero-counterexample |
| 78 | me | LEAD (promotion REJECTED, N20; B-78b fix verified N25) | 31 | rival "l'" killed (58×); rival "e" LIVE (the "e"-kill was a syllabifier artifact); 2/7 of 77→78 ×7 sit inside the "gouvernement" trigram → 78="ver" word-internal there |
| 77 | le | LEAD (promoted LEAD-weak→LEAD, N25; ACCEPT fenced) | 44 | 77→86 ×5 (object-pronoun frame); 77="pas" DISFAVORED-strong; verb-adjacent ("qui [verbe]" + 06/67 predecessors) |
| 47 | ce | LEAD (N29; polyvalent with 87) | 28 | 47="me" KILLED (3 independent); 47→46 "ce que" ×3 @0.1071 vs era 0.1076 → **1.00× exact**; "par ce" 2.85×; 47→11 ×3 "cela" |

## 4. Polyvalence islets (F33 — CONDITIONED, not free)

3 of 25 identified groups (12.0%) carry ≥2 live readings, each with a verified
conditioning rule. **Zero cases of free polyvalence.** The code is
information-lossless in principle; recoverability is bounded only by key
identification. Falsifiable: one verified unconditioned 1-group→2-sounds case
breaks it.

- **06 — trigram-internal "ent" vs verb-stem class.** 06="ent" survives ONLY
  inside 94-82-06 ×3 (@578/1182/1353) — PLAUSIBLE, fenced; everywhere else 06
  is a verb stem (finite/imperative: 06→77 ×6, 06→29 ×4, 06→11 ×4, 06→00 ×4).
  **06/86 complementary distribution** (N29): 00→86 ×12 vs 00→06 ×0 —
  86 = infinitive-complement stem, 06 = finite/imperative stem. The inventory
  distinguishes MOOD.
- **52 — "pas" iff negation-frame, else "so"/"se".** 52="pas": 94→52 ×3
  ("ne pas"), 70→52 ×1 ("prend pas" @1329), "on ne prend pas" lock, ne-pas-inf
  ×2. 52="so": word-internal @159 (93-52-94 "per|so|nne", the K5 scoped kill
  that FORCES polyvalence). 52="se": LEAD (94→52 ×3 also reads "ne se").
  Conditioning rule: **52 = "pas" iff immediate predecessor ∈ {94, 70}; else
  "so"/"se".**
- **94 — "ne" vs "en" islets.** 94="en" iff pre=82 ("m'en": 82-94-76 @1576)
  or suc=87 ("en ce": 94-87-83 @1169); 4/4 conditioned (N24); co-value
  promotion DENIED only on independence (N31). Conditioning can be lexical
  (idiom frames), not just positional.
- **47/87 — "ce" = {87, 47}:** first verified 1-sound→2-groups allophony at
  the function-word level (N29). The noise direction is always allophony
  ("personne" keeps 94 for the unchanged /n/ across both cuts), never
  unconditioned 1 group→2 sounds.

## 5. Shape regularities of the inventory

- 96 groups; ~72 syllable slots + ~24 letter slots (analyze_polyvalence.py
  estimate); units 1–4 letters.
- Proven shapes: 1-letter (m bare consonant, i bare vowel, e mute vowel),
  2-letter (la, er), 3-letter (pre, que). 4-letter units (ment/tion family)
  are in the upstream inventory but NOT proven here.
- Whole function words as single units: la, que, ce, qui, par, ne, on, me,
  le — the table's backbone is grammatical, not phonological.
- Endings as units: er (word-final-ish, phase-C). The encipherer strips
  final "-er" morphologically (F22: corpus P(unit ends in "er")=0.0211 ≈
  cipher 29 rate 0.0244 vs standalone "er" 0.0020).
- A→C→B→A contact rotation is real (chi²=366.3 on repaired parse, N30) but
  phases are NOT word-position classes (tuner N15); cluster assignments are
  fragile (61/96 change phase).
- Token coverage of identified groups: 35.2% (STATE.md). Unidentified head:
  00 (n=55, rank 1), 24 (n=52, rank 2), 98 (n=40), 48 (n=38), 74 (n=34) —
  the inventory's empty slots.

## 6. What the inventory RULES OUT

1. **The 180-unit upstream inventory** (`data/upstream-syll*.py`: 24 single
   letters + 156 French syllable/function-word units) as the encipherer's
   table — DEAD: all three off-the-shelf annealers "still no French"; N29
   records it as NOT the encipherer's table. It is one hypothesis among
   others, never the default.
2. **Standard French syllabification as the unit set** — DEAD by
   ground-truth control: the 4-GT-anchor "première" tail returns zero
   lexicon candidates at every tier; 'm' as a syllable exists in 1 of
   11,870 era words vs GT-proven here.
3. **Era-syllable-conditional rate legs on fragments** — VOID (F30): the
   29/82/34 exclusions (182×/61×/3.3× overages, N22) and 40-conditionals
   (era tokenizer almost never emits word-final bare "e", N20).
4. **Rigid syllabification as an instrument** — DEAD (F30): tuner NULL
   (N15), calibration mismatch (N22), by-ear enlightenment (frenchman).
5. **Phonetic models needing mute-e UNWRITTEN** — KILLED (N17): the crib
   writes 40="e" for mute final -e; 06→40 = 0×.
6. **Unique segmentation** — KILLED (R2): "personne" cut two ways.
7. **"J'ai l'honneur de" = 77 78 94 82 06 (H5)** — KILLED (N11): position 4
   is 82='m' (GT) vs needed "neur"; 67×/184×/47× rate failures.
8. **Free (unconditioned) polyvalence** — zero verified cases (F33).
9. **"ment"-family instruments needing 82 as "neur"-position** — dead with
   H5; 94-82-06 is "ne|m|ent" (conditional 06) or "gouvernement"-family.
10. **The sweeper's "parce" rate (132/1036)** — miscomputed, repaired (F28):
    true word-space 13/1036 (11.4× fail); syllabary-aware repair 1.26×.
    96="par" stands on the repaired leg only.

## 7. Status legend

- **PROOF**: pencil crib or lane-verified structural kill; not overturned by
  corpus choice.
- **PROVISIONAL(-strengthened)**: ≥2 independent checks, no surviving rival;
  register/corpus caveats fenced.
- **LEAD / STRONG LEAD**: live working hypothesis; one check from promotion.
- **PLAUSIBLE**: survives a kill, needs more evidence.

## 8. Best next step

Two, in order:

1. **Mine the SECOND "la première" window (@754, row a5_03).** It was
   off-phase before the repair and never examined (round-5 work order 8).
   Its surroundings (`…40 67 11 70 82 34 29 40…`) are a fresh by-ear
   inventory read — new hyper-fine units may sit adjacent to the one
   proven word we fully understand.
2. **Re-drive the pattern matcher on the cipher's own unit alphabet.**
   The polyvalence gate (POLYVALENCE_REPORT §8) says: fix inventory first,
   then apply the polyvalence restrictions. This inventory IS the fixed
   unit set — the matcher's `(n, pattern)` lookup must be rebuilt on it
   (bare-letter units allowed; inconsistent cuts tolerated as n-mismatch),
   not on the lexicon's syllabary.
