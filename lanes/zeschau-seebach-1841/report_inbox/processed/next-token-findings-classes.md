# Next-token findings: 31=VERBAL and 33=INF followers (finder: classes beat)

All counts byte-verified against the repaired 1,847-pair stream. 31: 8 occurrences. 33: 25 occurrences.

## RECORD CORRECTION
Round-11's "33 follows 67 ×1" is **×6** (byte-verified; bigram 67-33 occurs 6×). "33 precedes 29 ×5" confirmed. "33 follows pour(00) ×8" confirmed. "qui 33" occurs **0×** — 33 never follows "qui" (but precedes it twice inside "33 21 64 37").

## 33 = DIRE (lead, scored against {dire, penser, croire, savoir, vouloir})

**P1 (HIGH). 33="dire" is the clear leader.**
- "67 33 46" ×2 (@1450, @1623): "et/veut [inf] que". Idiomatic under BOTH forks of the 67 polyvalence: "et dire que" (the idiom) and "veut dire que" ("to mean that"). No other candidate is idiomatic under either fork.
- "47 33" ×2 (@22–24, @1230–1232): "er ce [inf]" → "47 33" = **"ce [inf]"**, preverbal demonstrative object + infinitive ("ce dire", "ce savoir", "ce croire" all grammatical). Preceded by an "-er"-tailed word (29) both times.
- "33 21" ×3, of which "33 21 64 37" ×2 (@936, @1630): 21 is noun-shaped ("par 21" ×3, "la 21" ×2 elsewhere), so "[inf] [noun] qui [verb]" — "pour dire [21] qui…" / "dire [N] qui [V]" is natural ("dire un mot qui…").
- "pour 33" ×8: no discrimination (purpose takes any infinitive), but all eight are consistent with "dire".
- KILLED: **vouloir** ("et vouloir que" ✗, "ce vouloir" ✗). WEAK: **penser** ("et penser que" marginal, "ce penser" ✗, "veut penser que" ✗). SURVIVE: croire (medium — "ce croire" ✓), savoir (medium-strong — "ce savoir" ✓✓, "pour savoir" ✓✓, but "et/veut savoir que" unidiomatic).

**P2 (HIGH, adverse). "33 29" ×5 is 29's #1 left context — and puzzles all five candidates.**
33→29 @273, @626, @1232, @1424, @1477 (29's top left bigram: 5/45). Followers: 29-89-84 ×2, 29-82-16 ×2 (both recur elsewhere: @1376, @432 — real word-shapes), 29-87-78, 29-87-63, 29-85-56 (singletons). If 29-8X = "erreur"-shaped, then 33 takes "erreur" as object — NONE of {dire, penser, croire, savoir, vouloir} does ("faire erreur" would fit but "33 que" ×2 kills "faire"). Either the candidate set is incomplete or 29-8X isn't "erreur". Battery must resolve the 29-89-84 / 29-82-16 word-shapes first — this is the top blocker on promoting 33="dire".

**P3 (MEDIUM). Byte-identical 5-gram repeats suggest 33 recurs as ONE infinitive in fixed phrases.**
- "00 33 79 80 06" ×2 (@467, @1088) — formula-grade; 79="tout" (PROMOTE-grade) gives "pour [inf] tout 80 06".
- "00 33 21 64 37" ×2 (@936, @1630) — formula-grade.
- "00 33 16 00" ×2 (@186: …66, @1245: …67) — "pour 33 16 pour [66|67]", 66/67 variation.
- "33 00 86 56" ×2 (@1000, @1504) — read as clause boundary: "[inf]. Pour 86 56…" (sentence-initial "pour" + NP), not "[inf] pour". Segmentation finding.
- Counter-note: "33 21 67 33" (@1421→@1424) and "33 42 33" (@1502→@1504) chain two 33s 2–3 groups apart — if both are "dire", that's awkward repetition; if 33 is a small set, they may differ. Unresolved: single-infinitive ("dire" everywhere) vs small-set.

**P4 (MEDIUM). "67 33" ×6 splits 3/2/1: "67 33 29" ×3, "67 33 46" ×2, "67 33 66" ×1.**
The "67 33 29" triple (@272, @1423, @1476) is "et/veut [inf] er…" — under 67="veut" + 33="dire": "veut dire er…" still needs the 29-word resolved (same P2 blocker).

## 31 = VERBAL class CONFIRMED by diversity (person: honest null)

**P5 (HIGH, class-level). 31's 8 followers are 8/8 DISTINCT — zero repetition.**
Followers: 14, 79, 29, 92, 11, 24, 76, 10. Lefts: 64("qui") ×2, 08 ×3, 11, 48, 61 — only repeat is the left bigram "03 64" ×2 (@338, @1647: "03 qui 31 …"). A single word would show formulaic repeats (cf. 33's three doubled 5-grams); 8/8 distinct followers is exactly the signature of a CLASS of finite verbs taking varied arguments. 31=VERBAL behaves distributionally as a class tier, not a value. This is confirmation, not a null.
- "31 79" @882: 79="tout" (PROMOTE-grade) → "[verb] tout" ("sait tout"/"dit tout"-shaped) — supports 79="tout".
- "11 31 11" @1516 ("la 31 la" sandwich) and "31 24" @1521 ("31 en"): flagged as anomalies for the battery — post-verbal "la"/"en" suggests imperative or a mis-segmented boundary. Do not force.
- Person: UNDETERMINED. No pronoun-shaped followers (no 82="m" adjacent; no clitic clusters), no tense-signal replication. "qui 31" ×2 implies 3rd person by syntax, but the verb itself is unnamed in all 8 windows. Honest null — the battery should attack via the "03" left-context (03 precedes "qui 31" twice; profile 03) rather than followers.

## Ranked battery targets
1. Resolve 29-89-84 / 29-82-16 word-shapes ("erreur"?). Blocks 33="dire" promotion.
2. 33="dire" idiom battery: "et dire que" / "veut dire que" / "ce dire" / "pour dire [N] qui [V]" frames vs the five candidates — expect dire ≫ savoir/croire ≫ penser, vouloir dead.
3. Single-vs-set test for 33: do the "33 21 67 33" and "33 42 33" chains force two different infinitives?
4. Profile 03 (the "03 qui 31" ×2 left frame) — only replicated context of the VERBAL class.
5. "11 31 11" / "31 24" anomaly battery: imperative reading vs boundary error.
6. "33 00 86 56" segmentation: confirm "Pour 86 56" as sentence-initial (86-56 bigram occurs 4× total — profile it).
