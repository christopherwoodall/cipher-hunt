# Next-token findings: followers of 29="er" (45 windows)

Beat: every 29 occurrence + 3 followers, clustered by follower pattern first. Stream: 1,847 pairs (repaired_offsets.json).

## P1 (HIGH). 47 = "se" after infinitives — positional allophone hypothesis
- 29 is the **joint-top predecessor of 47** (4/28, tied with 76). The four: @22 `43 29 47 33 55`, @422 `36 29 47 14 62`, @1230 `48 29 47 33 29 85`, @1590 `48 29 47 08 81`.
- Sharp sub-frame **29-47-33 ×2** (@22, @1230): "[inf] 47 [inf]" = "[inf] **se** [inf]" — causative-reflexive ("faire se + inf") or pronominal infinitive ("à demander se faire [85]"-shaped). "ce"+infinitive is ungrammatical; "se"+infinitive is not.
- Round 13 split {47,87} positionally (47 after "par", never "en"). This adds a second positional frame: **47="se" after infinitives, 47="ce" after "par"**. "se"/"ce" are homophones — the split may be positional allophony, not two values.
- TESTABLE: 47-predecessor battery (is 29/33/86 over-represented vs chance?); 47-33 bigram battery; check 47 after 86-29 too.

## P2 (HIGH). 29-40-65 ×3 = "[X]ère [65]" — finite -ER verbs
- @291 `64 29 40 65 16`, @685 `64 29 40 65 94 29`, @1710 `06 29 40 65 94 44`.
- Twice after 64="qui": "qui [V]**ère** [65]" — finite 3rd-sg -ER verb ("consid**ère**/préf**ère**/diff**ère**"-shaped), NOT an infinitive. 29-40 = stem-"er" + "e" inflection.
- 65 = direct-object slot after these verbs. TESTABLE: 65 contact profile (does 65 pattern as a direct object elsewhere?).
- Consequence: 29's followers split between infinitive frames AND finite-verb frames — the stem-finder must not assume every 29 is an infinitive ending.

## P3 (HIGH, fork). 29-80: determiner vs mystery — 80 is polyvalent or one reading is wrong
- @1155 `92 29 80 17 77 82` = "[inf] **[80] fois**, le m…" — 80 is a determiner/quantifier before "fois" ("plusieurs/chaque/cette fois"). Clean.
- @1031 `03 29 80 77 11 70` = "[inf] [80] **le la** pre…" — "[quant] le la" is broken. Either 80 ≠ quantifier here, or 77="le" fails here, or enclitic reading: "[verb]-le. La pre…" ("montre-le. La première…").
- 03-29-80 ×3 (@1031, @1321, @1595) — shared stem-03 frame. TESTABLE: 80-distribution battery (before 17 vs before 77 vs elsewhere).

## P4 (MEDIUM-HIGH). 67 fork corroborated in BOTH directions — polyvalence confirmed contextually
- @274 `67 33 29 89 84`: "**veut** [inf]" — "veut demander" is clean; "et demander" needs a parallel verb. → veut-reading.
- @1389 `06 29 67 86 29 89`: "[inf] **et** [inf]" — parallel infinitives ("parler et demander") clean; "veut" needs a subject. → et-reading.
- Round 13's "sole true polyvalence" verdict holds at byte level: the fork resolves per-window, not per-value.

## P5 (MEDIUM). 86 = infinitive stem (new stem for the stem beat)
- **86-29 ×4** (@432, @1376, @1392, @1826) — 86 takes "er" like 33 does.
- @1392 `67 86 29` = "et/veut [86]-er". Hand to the stem-finder: name the 86-verb.

## P6 (MEDIUM). 29-89-84 ×2 = "[inf] [89] [84]"
- @274 `33 29 89 84 91`, @1376 `86 29 89 84 92`. 89 = verb-stem target (que/ce finder: "ce le [80/89]"), 84 = clitic pronoun ("que 84-24-37"). "[inf] [verb]-[pron]"-shaped. TESTABLE: 89-84 bigram battery.

## P7 (MEDIUM). 29-87 ×3 = "[inf] ce", never "ce que"
- @147 `84 29 87 64 96` ("ce qui"), @627 `33 29 87 78 67`, @1425 `33 29 87 63 91`. 46 NEVER follows 87 here.
- Reading: demonstrative determiner "ce + noun" ("veut demander ce [63]" = "wants to ask for this [63]" — grammatical) or "ce qui" relative. Constrains 87's post-infinitive frames.

## P8 (MEDIUM). 29-82-16 ×2 = "[inf] m' [16]"
- @432 `86 29 82 16 78`, @1478 `33 29 82 16 98`. 82="m" as "m'" before vowel-initial 16. TESTABLE: 16's profile (vowel-initial verb?).

## P9 (FLAG). Null-stem anomaly: 46-29 and 11-29 — plus a finder discrepancy
- @96 `46 29 85` ("que-er"), @218 `46 29 42` ("que-er"), @78 `11 29 42` ("la-er"): "er" with NO stem. An infinitive needs a stem; these have none.
- Leading hypothesis: word-initial "er-" after elided determiner — 11-29-42 = "l'er[reur]" ("pour l'erreur [42]"-shaped). 46-29 ("que er-") stays ungrammatical — anomaly.
- **Discrepancy for the battery runner:** the que/ce finder reported "que [85]-er" (46-85-29) @95 as deliberative infinitive ×2. Byte data: **46-85-29 occurs 0×**. What is actually at @95-97 is 46-29-85. Do not test the finder's claim as stated.

## P10 (structural). No masculine "premier" exists
- 70-82-34-29 occurs 2× (@758, @1038), BOTH with 40 ("première"). The masculine "premier" (no 40) never occurs. "la première fois" is the only premier-frame in the cipher. (Consistent with the fois battery.)

## P11 (flag for red team). @1031 "80 77 11" adverse for 77="le"
- If 80 is a verb and 77="le", "80 77 11" = "[verb]-le la" — ungrammatical unless enclitic+sentence break. Either 77="le" is wrong at this window, 80 is polyvalent (P3), or the enclitic reading holds. Do not let 77="le" promote on evidence that includes @1031 unresolved.

## Honest nulls
- 29-85 ×3, 29-42 ×3: no shared frame beyond "[inf] [X]" — 85/42 need independent profiling first.
- Singletons (88, 60, 49, 74, 45, 48-as-follower): not battery-worthy.
- 29-40 "ere" beyond P2/P10: @62 "ière" ([08]-ière, feminine noun — "manière/lumière"-shaped, stem-finder's), @500 "ce la [X]ère" (ungrammatical as parsed — possible 47-frame tension, noted not forced), @597/@1050 singletons.

## Battery priority for the queue
1. P1: 47-predecessor battery + 47-33 bigram (the "se"-allophone is the biggest structural claim here)
2. P2: 65 contact profile (direct-object slot?)
3. P3: 80-distribution battery (before 17 / before 77 / elsewhere)
4. P6: 89-84 bigram
5. P8: 16 vowel-initial profile
6. P9: verify 46-85-29 = 0 (kill the mislabeled claim), then 29-after-determiners distribution
