# Battery verdict: val-71-quant-nominal

**Bar (verbatim from battery-queue.json):** "decide if 71 is a section-7 split candidate or a single nominal with '65 71' forming a unit"

**Bar restated:**
- C1: Test whether 1b@925 ("71 fois") and 1b@1337 ("71 qui") force different classes for 71.
- C2: Test whether a "65 71" unit rescues a single-nominal reading at @925.
- C3: Decide: §7 split candidate vs single nominal + "65 71" unit.

**Adverses:** section 7 sole-polyvalence — battery gathers only, never declares.

## Method
Read BATTERY-PROTOCOL.md first. Created `locks/val-71-quant-nominal.lock` on start (agent id + UTC timestamp). Re-derived the repaired stream from `data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`: 1,847 pairs / 96 types verified. `canonical.py` never touched; R5005, sealed gates, red-team adjudication queue untouched. Offsets below are 1-based on the repaired stream.

Standing values used (table-registry.json): 12='n' (prom), 40='e' (gt), 48='e' (prom), 64='qui' (prom), 17='fois' (prom), 65=noun (cls), 86=INF (cls), 79='tout' (prom, A5).

## Census (byte-exact, re-derived)
71 n=7. Predecessors: 60 x2, 63, 48, 65, 86, 83. Successors: 51, 10, 12, 17, 64, 50, 48 (each x1).

| Window | Row | In-row | Context (±6) |
|---|---|---|---|
| 1b@234 | a2_01 | 16 | 98 83 82 96 21 60 [71] 51 70 98 41 17 11 |
| 1b@326 | a2_05 | 1 | 06 11 92 60 15 63 [71] 10 01 19 00 92 50 |
| 1b@712 | a5_01 | 17 | 66 21 35 53 12 48 [71] 12 63 00 66 86 01 |
| 1b@925 | a5_10 | **0** | 49 74 74 40 08 65 [71] 17 61 96 48 82 98 |
| 1b@1337 | a7_05 | 4 | 94 70 52 39 83 86 [71] 64 60 08 65 64 52 |
| 1b@1565 | a8_01 | 11 | 17 11 26 30 06 60 [71] 50 29 24 74 62 48 |
| 1b@1614 | a8_03 | 3 | 92 65 23 08 55 83 [71] 48 31 76 42 44 11 |

"65 71" bigram: exactly 1x stream-wide. "86 71": exactly 1x. "48 71": exactly 1x. "71 12": exactly 1x.

**Row-boundary finding:** 1b@925's 71 is at in-row position 0 of row a5_10 — it is the FIRST token of its row. The "65" in "65 71" is the LAST token of the preceding row a5_09. The "65 71" bigram therefore spans a row boundary.

## C1: Different classes forced — PASS

**@1337 forces nominal.** "83 86 71 64" with 86=INF (infinitive class, registry) and 64='qui' (prom). 71 sits between an infinitive and "qui". Exhausted alternatives:
- Quantifier/determiner: "INF quant qui" ("prendre chaque qui") — ungrammatical.
- Adverb: "INF adv qui" — ungrammatical.
- Preposition: "INF prep qui" — no French frame ("prendre à qui" incomplete).
- Verb: two verbs in sequence — ungrammatical.
- Nominal (noun/pronoun): "INF noun qui" ("prendre [X] qui...", X = direct object head of "qui"-relative) — grammatical. This is the ONLY viable class. 71 is standalone here (a following letter-group cannot compose with "qui", a complete grammatical word; a preceding letter-group cannot attach to a complete infinitive).

**@925 forces non-nominal.** 71 is row-initial (a5_10 inrow=0), standalone, followed by 17='fois' (prom): "71 fois". "NOUN fois" with a bare noun is ungrammatical in French at any period — "fois" takes determiners/quantifiers/numerals ("une fois", "chaque fois", "deux fois", "la première fois") or appears in fused adverbs ("toutefois", "quelquefois", "autrefois"). Therefore 71 is quantifier/determiner-like, or "71 17" is a fused adverb (71 then sub-lexical). Either way: NOT nominal.

**Result:** nominal@1337 vs non-nominal@925. Different classes forced.

## C2: "65 71" unit rescue — TESTED AND REFUTED

Three strikes against the unit rescuing single-nominal:
1. **Row boundary:** "65 71" spans the a5_09/a5_10 row break (65 ends a5_09, 71 starts a5_10). Word-internal bigrams do not straddle transcription rows without cause; no cause is evidenced.
2. **Grammar:** even granting the unit, "65-71" would be a nominal unit (65 is noun-class, 71 nominal under the hypothesis), and "nominal-unit fois" is exactly the ungrammatical "noun fois" configuration. The unit changes nothing.
3. **Class contradiction:** for "65-71" to precede "fois" grammatically it must be quantifier-like, but 65 is noun-class (battery-promoted) and 71 must be nominal (per @1337). No single-class "65-71" word satisfies both.

The unit does not rescue single-nominal. C2 fails as a rescue; the refutation itself passes.

## C3: Decision — 71 IS a §7 split candidate

No single standalone class covers @925 and @1337. The bound-morpheme rescue also fails: 86=INF cannot host inflectional morphology, and at @1337 a letter-group 71 could compose with neither the complete infinitive to its left nor the complete word "qui" to its right — 71 is standalone there, while @925 forces non-nominal. The apparent "quantifier vs nominal" contrast is a genuine class difference, not an artifact.

**Supporting (@712):** "48 71 12" = "e 71 n" with 48='e' and 12='n' both promoted letters. Neither 'e' nor 'n' stands alone as a French word, so 71 must compose sub-lexically here ("es" + "n", or "e" + "71n") — consistent with 71 being polyvalent across windows, inconsistent with uniform standalone-nominal.

Per §7 and the listed adverse, the battery does NOT declare a split — 67 et/veut remains the sole declared polyvalence. This report gathers the split-candidacy evidence for red-team adjudication.

## Standing-state check
No standing verdict on 71 exists; nothing contradicted or downgraded. name-71's NULL (fence) stands — this battery answers its follow-up #1. 71='tout' remains ruled out (79='tout', A5). §7 honored.

## Verdict: PROMOTE (finding grade — promotes no value, declares no split)

71 is a §7 split candidate: nominal@1337 vs non-nominal@925, with the "65 71" unit rescue refuted on row-boundary and grammatical grounds. Recommended venue: red-team adjudication (split declaration is a red-team act).

## Bookkeeping
- `battery-queue.json`: `val-71-quant-nominal` → status `verdict`, result `promote`, date 2026-10-09 (temp-file + rename, pre-write assert confirmed queued/verdictless, JSON re-validated post-write).
- Lock created on start, deleted on completion.
- `canonical.py` never used; R5005, sealed gates, red-team queue untouched; all numbers re-derived on the repaired 1,847-pair stream.
