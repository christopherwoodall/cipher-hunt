# Battery report: gender-44 — 44's gender adjudicated

Target: `gender-44` | Claim: 44's gender is adjudicated ('le 44' x2 vs 'la 44' x1)
Worker: 0274e077-c4e3-480e-88ba-cdbee61ffe15 | Date: 2026-10-08
Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json + data/upstream-ct_R5005.txt), parsed like code/side-keyhunt/repair_parse.py. canonical.py NOT used. R5005 NOT touched.

## Bar (verbatim from battery-queue.json)

> one gender with all three determiner windows parsing, or a stated positional rule

Restated as numbered pass/fail clauses (fixed before testing, not modified after):

1. **Clause 1** — 'le 44' @208-209 parses as masculine article + noun (77='le' provisional standing).
2. **Clause 2** — 'le 44' @1679-1680 parses as masculine article + noun.
3. **Clause 3** — @1070-1071 '11-44' is resolved without a feminine determiner: either it parses under the masculine gender, or a stated positional/structural rule removes it as a determiner window.

## Method

Re-derived all determiner windows on the repaired stream from scratch (1-based lane @-offsets).
Offsets from the queue's evidence gloss verified exactly: @208-209 = 77-44, @1679-1680 = 77-44,
@1070-1071 = 11-44. Full census: 44 occurs n=15; '77-44' x2, '11-44' x1 — no other
le/la-class determiner precedes 44 (predecessor census: 77x2, 32, 47, 12x2, 37, 86, 11, 82, 92, 00, 42x2, 94).

## Window-level evidence

### W1 — @208-209: 77-44 ('le 44')

Context @200-217: `67 76 87 11 92 63 42 06 | 77 44 | 50 88 19 74 77 78 06 59`
Left bigram 42-06 occurs x5 stream-wide (word-internal "[42]ent"-shaped; 06='ent' promoted).
Parse: `...[42]ent le [44] [50]...` — adverb/verb-form + masculine article + noun.
Grammatical under 77='le' (provisional). **PASS (masculine).**

### W2 — @1679-1680: 77-44 ('le 44')

Context @1671-1688: `78 55 81 92 60 03 39 74 | 77 44 | 00 46 79 65 13 93 62 94`
Right context is decisive: 00='pour' (granted A9), 46='que' (banked GT):
`le [44] pour que [79 65 ...]` = "the [44] so that ..." — masculine article + noun
governing a purpose clause. Fully grammatical. Left: `...03 a/à [74]` then a clause
boundary before 77 (one boundary assumption; 74's value open but any nominal/verbal
74 closes the clause). **PASS (masculine).**

### W3 — @1070-1071: 11-44 ('la 44' per the finder)

Context @1062-1079: `83 82 96 21 62 18 70 39 11 | 44 | 74 42 98 98 12 48 77 78`
The trigram 70-39-11 ("pre-a-la") occurs exactly x2 stream-wide:
@1068 `70-39-11-44` and @1605 `70-39-11-92` (context: `...00 44 | 70 39 11 92 | 65 23...`).
The flat determiner reading "pré à la [X]" is ungrammatical as a sequence at both
sites (no clause boundary available; "pré" as standalone meadow-noun is unmotivated
in both contexts). The word-internal reading is "préalable"-shaped (70='pre' banked,
39='a', 11='la' as syllables — lane precedent: the a-39 battery already recorded
"'pre-a-la' x2 = word-internal 'a' ('prealable'-shaped, completion unverified)").
@1068-1071 = "préalable" with 44 as the 'ble' syllable; @1605-1608 the same
"préala-" prefix with a different completion (92). "Préalable" is épicène
(identical masculine/feminine), so this window contributes ZERO gender information.
**W3 is not a determiner window.** Clause 3 **PASS** via the stated structural rule:
@1070-1071 is word-internal, not 'la'+noun.

### Corroborating distributional facts

- **Elision test**: 77 elides to "l'" before vowel-initial 84 ('l'on' x7, A15) but
  never before 44 (77-44 x2 unelided) → 44 is consonant-initial. Consistent with
  masculine "le [44]" (not "l'[44]") and with 44='ble' at @1070 ("préalable").
  A feminine vowel-initial host would have forced elision; not observed.
- **Feminine alternative costed and rejected**: making 44 feminine requires
  overturning 77='le' at BOTH @208 and @1679 (no independent evidence; 77='le' is
  load-bearing provisional for A8/A13/A15) or two clause boundaries leaving 'le'
  dangling (ungrammatical). Two ad-hoc escapes vs one parallel-supported
  re-analysis → feminine rejected at kill grade for this battery's scope.
- **'94-44' verb-frame note** (@1714-1715: `40-65-94-44`, "e [65] ne [44]"): 44 takes
  a verb-shaped frame here. This does not disturb the gender verdict: if 44 is an
  infinitive, 'le 44' is a substantivized infinitive — invariably masculine in
  French ("le manger", "le dire"). 44's class/value is NOT promoted here; it stays
  open for its own battery. No §7 polyvalence is declared (one lexeme, grammatical
  nominal use — same mechanism as the lane's analytic/syllabic readings).

## Per-clause verdict

1. Clause 1 (@208-209 'le 44' masculine): **PASS**
2. Clause 2 (@1679-1680 'le 44' masculine): **PASS**
3. Clause 3 (@1070-1071 resolved, word-internal "préalable"): **PASS**

## Verdict: PROMOTE — 44's gender is masculine

Both true determiner windows parse as masculine article + noun; the sole apparent
feminine window dissolves into word-internal "préalable" (épicène, gender-neutral).
Stated rule: 44 = masculine, consonant-initial; @1068-1071 is the syllabic
occurrence "pré-a-la-[44]" ('ble'-shaped), parallel to @1605-1608 "pré-a-la-[92]".

## Adverses

- "gates any future '-ere' hypothesis for 44" — **ANSWERED**: the gate holds.
  A feminine '-ère' word-family host for 44 is killed by the masculine
  adjudication (consonant-initial, masculine article x2, zero feminine windows).
  The 09/92 '-ère' kill is untouched; 44 is not an '-ère' host.
- No standing red-team verdict is contradicted: 77='le' (provisional) used as-is,
  11='la' (banked GT) used as-is, 70='pre' used as-is. 44's VALUE is not named;
  no promotion beyond gender.

## Open threads (not followed up here; for future batteries)

- 44's class/value: verb-shaped '94-44' vs nominal '44-59' x2 / '44-00' x3 /
  '00-44' — a verb-44 / infinitive battery should test the substantivized-
  infinitive reading (predicts masculine everywhere, consonant-initial).
- @1605-1608 '70-39-11-92' completion: if "préalable", 92='ble' at that window
  (92's value open; '-ère' killed — compatible).
- '12-44' x2 (@541, @1584): not "n'" elision (44 consonant-initial per elision
  test); word-internal "n"+44 or boundary — for the 12/44 contact battery.
