# Next-token findings: "que" (46) and "ce" (87) followers

Date: 2026-10-07. Beat: follower prediction for the two complementizer/demonstrative anchors.
Stream: repaired 1,847-pair parse. 46×29, 87×32. Three following groups recorded per window.

## Method notes (read first)

- **De-duplication rule:** formula tails are counted once. "par ce que" (96-87-46 ×3), "en ce qui" (24-87-64 ×3), "tout ce qui" (79-87-64 ×1) each generate phantom "87→" and "46→" windows that are the *same* formula viewed from a later cell. All clusters below are de-duplicated.
- **"cela" exclusion:** 7 windows of 87-11 are compositional "cela" (@74, @163, @201, @461, @830, @1242, @1403; "en cela" 3×). They are excluded from standalone-"ce" analysis — 87 there is the "ce" in "cela", not a "ce" taking followers.
- Board respected: 12 banked values + 17="fois" (newly promoted). No settled kills re-litigated.

---

## "que" (46) — predictions

### Q1. "que 84-24-37(-78)" — identical trigram ×2 + variant (HIGH, top target)
- @309 and @472: **byte-identical** `46-84-24-37-78` ("que [84] en [37] [78]"). @1485: variant `46-77-84-24-87` ("que le [84] en ce…").
- 24="en" is GT-strong. Prediction: **84 = clitic pronoun** (candidates: je/se/me/te/le/y — "que j'en [verb]", "que s'en…", "que l'en…"), **37 = verb**.
- Cross-construction check (independent leg): **37 is also the verb slot in "qui [23/26]-37"** (@179/@1766, the "en ce qui concerne" windows). Same group 37 as verb in two different frames = two-leg verb constraint on 37.
- Bonus: @310/@473 continue 37-78. If 78 resolves "er", 37-78 could be an infinitive ("en juger"-shaped: "que [84] en [37]er").
- Testable: 84 contact profile vs the 7 clitic pronouns; 37 vs verb frames in both constructions.

### Q2. "que" + infinitive ×2 (MEDIUM)
- @95: `46-29-85-08`, @217: `46-29-42-16` — 29="er" (verb ending) immediately after "que", two different stems (85, 42).
- Prediction: deliberative infinitives — "que faire/dire/penser"-shaped ("je ne sais que faire" family).
- Testable: 85 and 42 should show verb-stem contact profiles; check whether 85/42 appear as stems elsewhere.

### Q3. 00="pour" — second leg (MEDIUM, lead not promotion)
- "00 que" ×4 (@107, @546, @1546, @1681). 00 is the top-frequency group (55×, 2.98%) and still unidentified; "pour" is a top-10 French word and was already the standing "00 elsewhere" hypothesis (96-00="par le" being compositional).
- Best window @1546: `00-46-70-12` = "pour que pre[12]" — "pour que [prenne/prévienne]"-shaped (subjunctive after "pour que"). 
- Tension recorded honestly @107: `00-46-11-21-67` — 67=et/veut is not subjunctive, straining "pour que" there. Alternative for 00 stays open (dire/penser/croire + "que" also fit "00 que").
- Testable: "pour que"+subjunctive frames at the other three windows; frequency prior favors "pour" over verb candidates.

### Q4. 33's valency signature (MEDIUM-HIGH, narrows the infinitive paradox)
- `33-46` ×2 (@1452, @1625): 33 (INF class) directly takes a "que"-clause.
- This restricts 33 to **que-taking infinitives**: {dire, penser, croire, savoir, vouloir, falloir…}. Round 13 left 33's infinitive NULL with the paradox sharpened; valency is a new independent constraint on the candidate set.
- Both windows are preceded by 67 (the et/veut fork): `67-33-46`.

### Q5. "est que" ×2 (MEDIUM)
- @217: `59-46-29…` ("est que [42]er" — overlaps Q2's infinitive window), @1191: `59-46-07…`.
- Prediction: "c'est que" / "il est que" construction ("the fact is that…").

### Q6. "que la [21] [67]" (SPECULATIVE, single window)
- @107: `46-11-21-67` — "que la [noun] [67]". If 67="veut": "que la [Porte/cour] veut…". Clean French; needs 21 identified to test.

---

## "ce" (87) — predictions (standalone only, cela excluded)

### C1. "ce que" occurs ONLY as "par ce que" (HIGH, distributional)
- All three 87→46 windows (@225, @953, @1527) are tails of the three "par ce que" formulae (@224, @952, @1526). **Zero independent "ce que".**
- Constraint: parse any 87-46 bigram as expecting 96 ("par") before it. A future "ce"+"que" without "par" would be an anomaly worth flagging, not the norm.

### C2. "ce qui": 4/5 formulaic (HIGH, mostly de-duplicated)
- @180, @1767, @1775 are tails of "en ce qui" ×3; @1800 is the tail of "tout ce qui" @1799 (79-87-64-77: "tout ce qui le…").
- One standalone: @148 `29-87-64-96` = "[er] ce qui par [47]". ("par conséquent"-shaped, but 47 is a single group — held as unparsed, not forced.)

### C3. "ce le [verb]" ×2 — "this proves it" (MEDIUM-HIGH)
- @515: `87-77-80-09`, @869: `87-77-89-48` — "ce"+"le" twice with different verb slots (80, 89).
- Prediction: demonstrative "ce" (subject) + object pronoun "le" + verb — "ce le prouve/montre/démontre" ("this proves it"). Fully grammatical diplomatic French.
- **This supports 77="le"**: the "le la" tension that keeps 77 provisional does not apply here — "ce le" is clean. Two-leg frame for 80/89 as verb stems.
- Testable: 80/89 contact profiles vs verb-stem frames; compare 80 vs 89 (same slot, two windows — homophone/synonym check per the {33,86} split precedent).

### C4. @824 is NOT "c'est" (exclusion, recorded)
- @824's 87 is the tail of "en ce" @823; the follower is 59, but round-14 WO#7 already ruled word-"est" out at @825. So 59 has its third value here — do not parse as "c'est".

### C5. "ce [78]" ×2 (SPECULATIVE, target for the 78 fork)
- @572: `87-78-45-13`, @628: `87-78-67-08`. Whatever 78 resolves to (ver-initial vs er-final by position), these two windows are its test frames after "ce".

---

## Ranked testable consequences (for the battery runner)

1. **84 pronoun battery** — contact profile vs {je, se, me, te, le, la, y, en}; cross-check 37 as verb in "qui [23/26]-37" AND "que 84-en-37". (Q1)
2. **80/89 verb-stem battery** — "ce le [verb]" frames; 80-vs-89 same-slot comparison. (C3)
3. **00="pour" battery** — "pour que"+subjunctive frames at @546/@1546/@1681; resolve @107 tension. (Q3)
4. **33 que-valency battery** — restrict infinitive candidates to que-taking verbs; test top candidates in @1452/@1625 frames. (Q4)
5. **85/42 stem battery** — verb-stem profiles; "que [stem]er" deliberative frames. (Q2)
6. **78-after-"ce" frames** — feed @572/@628 to the round-14 78-fork resolution. (C5)

## Nulls and honest negatives

- No "ce"+"que" independent of "par ce que" exists (3/3 are formula tails) — the standalone-"ce"-takes-"que" prediction is dead on arrival; recorded as distributional fact, not a failure.
- "que" followers are otherwise singletons (no other cluster ≥2 beyond those listed) — the despatch's "que"-clauses are lexically diverse, as expected in running prose.
- 20 ("la première" @754 follower) remains NULL per the fois battery — untouched here.
