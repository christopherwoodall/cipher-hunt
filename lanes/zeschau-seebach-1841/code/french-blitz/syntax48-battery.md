# 48 SYNTAX BATTERY — French-work agent report

2026-10-07 · Direct agent (no coordinator) · Lane: zeschau-seebach-1841
Read-only on the cipher. 48's ID is LEAD-grade at best.

## Standing context (not re-litigated)

- 48="ne"-allophone KILLED (F60): merged word-rate 4.78× > 3× bar + two adverses.
- H_verb (48 = conjugated verb) KILLED (F64): zero 94="ne" near either "48 pas" window; predecessor verb-licensing 31.6% < 40%.
- S-word class KILLED for 30 candidates (F75): structural pincer ("la" takes nominals, "on" takes verbs — no single French word at 2.06% follows both).
- 10 S-syl LEAD-weaks banked as rate-band shortlist (F75): à, et, de, a, es, il, les, te, un, com. Zero discrimination beyond rate.
- Path D (48="de"-conditional, pronoun+infinitive) FENCED (F83) with ML-1/ML-2 missing.
- n48=38, successors 29 distinct/38 (repaired 1,847-pair parse, re-derived this battery).

Grounding: corpus = primary diplomatic (nesselrode-v8 + levant-correspondence-1841-p3, 372,668 tokens, elision-split tokenizer per F53). Nesselrode v8 OCR word-splits VOID as French (F77).

---

## (a) 48 window table (38 windows, 0-based pair index)

Known: 11=la, 29=er, 40=e, 46=que, 47=ce(L), 77=le, 96=par, 0=pour, 59=est, 62=on, 82=m, 24=en, 64=qui, 87=ce, 70=pre (GT=ground truth, L=LEAD, no mark=provisional/strong).

| pos | pre | 48 | suc | frame (known gloss) | H_de_word |
|-----|-----|----|-----|---------------------|-----------|
| 126 | 82(m) | 48 | 11(la) | m-?-la | m-de-la OK (M. de la [name]?) |
| 170 | 12 | 48 | 21 | ?-?-? | neutral |
| 283 | 42 | 48 | 52 | ?-?-? ("48 pas" window) | neutral |
| 361 | 62(on) | 48 | 76 | on-?-? | on-de KILL (0 genuine) |
| 365 | 78 | 48 | 49 | ?-?-? | neutral |
| 377 | 82(m) | 48 | 0(pour) | m-?-pour | de-pour KILL (=0) |
| 398 | 82(m) | 48 | 6 | m-?-? | neutral |
| 426 | 62(on) | 48 | 76 | on-?-? | on-de KILL |
| 450 | 32 | 48 | 79 | ?-?-? | neutral |
| 542 | 29(er) | 48 | 42 | er-?-? | neutral (er sub-word) |
| 641 | 89 | 48 | 20 | ?-?-? | neutral |
| 710 | 12 | 48 | 71 | ?-?-? | neutral |
| 729 | 86 | 48 | 88 | ?-?-? | neutral |
| 810 | 12 | 48 | 24(en) | ?-?-en | de-en KILL (=0) |
| 856 | 32 | 48 | 84 | ?-?-? | neutral |
| 863 | 74 | 48 | 47(ce)→46(que) | ?-?-ce-que ("de ce que" frame) | de-ce-que OK (12×) |
| 872 | 89 | 48 | 20 | ?-?-? | neutral |
| 928 | 96(par) | 48 | 82(m) | par-?-m | par-de (partitive, ADJ only); de-m (=de M. +name) |
| 972 | 98 | 48 | 51 | ?-?-? | neutral |
| 987 | 89 | 48 | 1 | ?-?-? | neutral |
| 1076 | 12 | 48 | 77(le)→78→64(qui) | ?-?-le-?-qui (Path D window) | see ML-1/ML-2 |
| 1177 | 32 | 48 | 59(est) | ?-?-est | de-est KILL (=0) |
| 1212 | 32 | 48 | 96(par) | ?-?-par | de-par KILL (=0 as words) |
| 1221 | 24(en) | 48 | 30 | en-?-? | en-de (partitive only) |
| 1229 | 82(m) | 48 | 29(er) | m-?-er | neutral (er sub-word) |
| 1276 | 76 | 48 | 56 | ?-?-? | neutral |
| 1279 | 85 | 48 | 53 | ?-?-? | neutral |
| 1316 | 62(on) | 48 | 98 | on-?-? | on-de KILL |
| 1350 | 62(on) | 48 | 77(le) | on-?-le | on-de KILL (R-c exclusion also fires) |
| 1398 | 78 | 48 | 40(e) | ?-?-e | neutral (e sub-word) |
| 1465 | 62(on) | 48 | 21 | on-?-? | on-de KILL |
| 1525 | 11(la) | 48 | 96(par) | la-?-par | la-de KILL (=0); de-par KILL |
| 1570 | 62(on) | 48 | 56 | on-?-? | on-de KILL |
| 1589 | 65 | 48 | 29(er) | ?-?-er | neutral (er sub-word) |
| 1614 | 71 | 48 | 31 | ?-?-? | neutral |
| 1658 | 24(en) | 48 | 47(ce)→98 | en-?-ce-? ("de ce" frame) | en-de-ce: "en de ce"=0× |
| 1737 | 12 | 48 | 52 | ?-?-? ("48 pas" window) | neutral |
| 1779 | 19 | 48 | 74 | ?-?-? | neutral |

Predecessor census: 62×6, 12×5, 82×4, 32×4, 89×3, 78×2, 24×2, singletons(42,29,86,74,96,98,76,85,11,65,71,19).
Successor census: 21×2, 52×2, 76×2, 20×2, 47×2, 77×2, 96×2, 29×2, 56×2, singletons(11,49,0,6,79,42,71,88,24,84,82,51,1,59,30,31,74,53,98,40).

---

## (c) 48="de" — verdict: UNCONDITIONED DEAD, one conditioned frame survives

### H_de_word (48 = the word "de", all 38 windows): KILLED (kill-grade)

11 windows impossible on corpus word-bigrams (primary diplomatic):
- @377: "de pour" = 0× (ungrammatical).
- @810: "de en" = 0×.
- @1177: "de est" = 0×.
- @1212: "de par" = 0× (as words; "de par le roi" not in corpus).
- @1525: "la de" = 0× AND "de par" = 0× (double kill).
- @361/@426/@1316/@1350/@1465/@1570: "on de" = 0 genuine (2 corpus hits both non-genuine: OCR-name "bai on de werther", verb-inversion "dit on de devenir" — F83 D2a confirmed).

Note: "er"/"e" neighbors (@542, @1229, @1398, @1589) are sub-word units — NEUTRAL for the word hypothesis, not kills (my initial bigram script over-killed these; corrected by hand).

**Falsifier that would resurrect it:** none — 11 independent kill windows is kill-grade. Do not re-litigate.

### H_de_cond: 48="de" iff "de ce que" frame (suc=47, suc2=46): LEAD-WEAK (n=1)

- @863: 74-74-48-47(ce)-46(que)-0(pour). "de ce que" = 12× primary. Licensors in corpus: contente×2, piqué, heureux, courant, compte, contraire, opposé, fâchés (adjectives/participles/nouns). 74 (n=34) unidentified — licensor status untested.
- This is the ONLY clean "de" frame. Single window → LEAD-weak at best, needs a second "48-47-46" window or 74 identified as licensor-class.
- @1658 (24-48-47-98): "en de ce" = 0×. The "de ce" half is fine (133×; +noun: mois, pays, jour…), but the "en" (24) before "de" is unlicensed. Does NOT support H_de_cond. Either 24≠"en" here or 48≠"de" here.
- @126 ("m-de-la"): "m de" = 72× but ALL are "M. de" + name (m de sainte, m de brunnow, m de lamartine). Requires 82="M." abbreviation — 82 is GT as the LETTER "m", not "M.". Incompatible without polyvalence. NOT counted.
- @928 ("par-de-m"): "par de" = 6× but ALL partitive + adjective (par de fortes, par de pareilles). "m" is not an adjective. Incompatible.

**Falsifier:** identify 74 as a non-licensor (verb/noun incompatible with "de ce que"), or find that "de ce que" at @863 is ungrammatical in wider context. **Promoter:** a second 48-47-46 window, or 74 → adjective/participle.

---

## (b) Syllable-cell hypothesis — refined

F75's 10 LEAD-weaks (rate-selected): à, et, de, a, es, il, les, te, un, com. Zero discrimination beyond rate. New legs this battery:

### Leg S1 — "m-48" vowel-initial constraint (LEAD-grade, conditional)

82="m" is GT as the LETTER "m" (from "première" = pre|m|i|er|e, where "m" is syllable-initial). It precedes 48 ×4 (@126, @377, @398, @1229). French phonotactics: NO mC- onsets exist. IF "m-48" is within-word (the "première" precedent), 48 MUST be vowel-initial.

- FAVORED (vowel-initial): à, a, es, et, il, un.
- DISFAVORED (consonant-initial, need word boundary + word-final "m" — French words ending in "m" are vanishingly rare): de, les, te, com.

Condition: "m" syllable-initial. If "m" is a coda (em/am/om/im), the constraint lifts — but 82's GT context ("pre-m-i") has it syllable-initial.

**Falsifier:** find "m-48" where 48 is provably consonant-initial (kills the within-word premise), or show 82="m" is word-final in these frames.

### Leg S2 — "on-48"×6 problem (ADVERSE for clean syllable reading)

If 62="on" is the pronoun, 48 would be word-INITIAL syllable in six windows. F83 Path A tested single-syllable coherence at the "on" frames and FENCED all 10 S (no S coheres). The syllable hypothesis has no clean account of "on-48" under the pronoun reading. Under the syllable-"on" reading ("on" as nasal syllable), "on"+S within-word is phonotactically strained for all shortlist S.

**Falsifier (for the syllable hypothesis):** none needed — this is already adverse. **Repair:** 62 polyvalence (pronoun vs syllable) or 48 polyvalence.

### Leg S3 — "48-er"×2 / "48-e"×1 (NEUTRAL, recorded)

@1229 (m-48-er), @1589 (65-48-er), @1398 (78-48-e). If within-word, 48 must form valid contacts with "er"/"e". No shortlist S forms a clean French "S-er"/"S-e" word-medial contact (a-er, es-er, et-er, il-er, un-er all strained). Either these are across-boundary (48 word-final + "er"/"e" starting next unit — but "er"/"e" can't start words) or 48 is a verb stem + inflection (H_stem, still UNTESTED per F64/F75).

### Net syllable verdict

Shortlist refined to a vowel-initial tier (à/a/es/et/il/un) on the "m-48" leg, but the "on-48"×6 frames remain adverse for ALL candidates and "48-er"/"48-e" fit none cleanly. **No syllable promoted. The syllable hypothesis is LEAD-weak at best and has an unfixed adverse.** The frequent-syllable-cell lead from round 11 is NOT confirmed by this battery — it remains a direction, not a result.

**Falsifier for the whole syllable hypothesis:** identify 48's value as a WORD (not syllable) in any frame, or show the "m-48" windows are across word boundaries.

---

## (d) ML-1: infinitive at @1076's 78 slot — UNFILLED

Frame @1076: 98-98-12-48-77(le)-78-64(qui)-6. Under Path D (48="de", 77="le" pronoun), 78 must be infinitive-initial.

Corpus "de le + INF" (primary): faire×12, voir×5, prévoir×2, mettre×2, recevoir×2, modifier×2, contrecarrer×1, laisser×1, renouveler×1, défendre×1. First syllables: fai, voi, pré, met, re, mo, con, lai, dé.

- 78's standing identity ({ver,er} fork, gouv-adjacent) matches NONE of these first syllables. ("re" vs "er" is metathesis, not a match.)
- "de le [INF] qui" = 0× in 372K tokens — the "qui" (64) adjacency at pairs[1079] is unlicensed for an infinitive reading. Infinitives do not take "qui" complements.
- 78's own successor profile (45×4, 40(e)×3, 48×2…) shows no infinitive-completion signature.

**Verdict: ML-1 UNFILLED.** The infinitive cannot be identified; the frame's "qui"-adjacency is independently ungrammatical for the infinitive reading. This SUSTAINS (not lifts) the Path D fence.

**Falsifier:** find "de le [INF] qui" in era French, or re-identify 64 (if 64≠"qui" here the adjacency problem dissolves).

## (d) ML-2: pre=12's licensor class — UNFILLED

For @1076's Path D frame, 12 must be a "de le + INF" licensor. Corpus licensors (D1): adjectives (facile×2), participles (chargé×2), nouns (courage×2, plaisir×2). So 12 must be adjective/participle/noun WORD.

But 12 (n=23) is preceded by 70="pre" (GT bound syllable) ×3 (@348, @1119, @1548: "pre-12"). A standalone adjective/noun/participle cannot follow the bound syllable "pre-". 12 is therefore likely a SYLLABLE (in "pre-" words: premier, prendre, prévoir…), incompatible with the licensor-word requirement — at least in 3/23 windows, and there is no basis to split 12 by window.

**Verdict: ML-2 UNFILLED.** 12's class is incompatible with the licensor requirement. This SUSTAINS the Path D fence.

**Falsifier:** show 70="pre" is not the bound syllable in the three "pre-12" windows (e.g., 70 polyvalence), or find "pre-[adjective]" as a word sequence in era French.

---

## Banked falsifiers (summary)

| Hypothesis | Falsifier | Status |
|---|---|---|
| 48="de" unconditioned (word) | 11 corpus-bigram kill windows (@377, @810, @1177, @1212, @1525, 6× "on-48") | KILLED (this battery) |
| 48="de" iff "de ce que" | 74 = non-licensor; or @863 ungrammatical in wider context | LEAD-weak, n=1 |
| 48 = consonant-initial syllable | "m-48" within-word premise (82 GT "m" syllable-initial) | DISFAVORED (conditional leg) |
| 48 = clean word-initial syllable | "on-48"×6 Path A fence (F83) | ADVERSE, unfixed |
| Path D (48="de" pronoun+INF) | ML-1 unfilled (infinitive unidentifiable + "qui"-adjacency); ML-2 unfilled (12 = likely syllable) | FENCED (sustained) |
| 48 = verb stem (H_stem) | successor "er"/"e" contacts untested | UNTESTED (not adverse) |

---

## Ranked lead for 48's identity

1. **UNIDENTIFIED (null holds).** The battery killed unconditioned "de"-word, sustained the Path D fence via two unfilled MLs, and left the syllable hypothesis with an unfixed adverse ("on-48"×6). Nothing reaches LEAD.
2. **48="de" iff "de ce que" frame** — LEAD-weak, n=1 (@863). The only corpus-clean "de" frame. Needs a second window or 74's class.
3. **Vowel-initial frequent syllable** (à/a/es/et/il/un tier) — LEAD-weak, conditional on the "m-48" within-word premise. Discriminated from the F75 shortlist but not between members.
4. **H_stem (verb stem + "er"/"e")** — UNTESTED, worth a battery (the "48-er"×2 / "48-e"×1 contacts are its natural habitat).

## Recommended next batteries

- **74-class battery:** is 74 an adjective/participle/noun licensing "de ce que"? (Promotes or kills the only "de" islet.)
- **H_stem battery:** test 48 as monosyllabic verb stem against "48-er"/"48-e" with era verb lists.
- **62-polyvalence battery:** if 62 is syllable-"on" (not pronoun) in the six "on-48" windows, the syllable hypothesis's worst adverse dissolves. Test via 62's islet registry entry.
- **Second "48-47-46" hunt:** the "de ce que" islet needs n≥2.

## Files

- This report: `code/french-blitz/syntax48-battery.md`
- Stream: `code/crowd7/keystruct/aliasing.load_stream()` (repaired 1,847-pair; N, n48=38 re-derived)
- Corpus: `code/crowd9/frenchman/corpus9.py` ("primary": nesselrode-v8 + levant-1841-p3)
- Prior art: F60, F64, F75, F76, F83, `code/crowd9/conditioner/islet_registry.md`, `code/crowd10/syllabicist48/`, `code/crowd11/anchorer48/`
