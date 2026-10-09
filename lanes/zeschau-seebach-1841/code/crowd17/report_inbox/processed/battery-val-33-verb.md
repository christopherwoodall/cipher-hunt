# Battery verdict: val-33-verb

**Target:** `val-33-verb` (priority 2)
**Date:** 2026-10-08
**Stream:** repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed per `repair_parse.py`). `canonical.py` never touched. R5005, sealed gates, red-team queue untouched.

## Bar (verbatim from battery-queue.json)

> name 33's verb value iff >=2 independent frames parse under it with zero forced contradiction

**Numbered clauses:**
1. Name 33's verb value only if ≥2 independent frames parse under the named value.
2. Zero forced contradiction: no window may force the named value false (ungrammatical with no rescue under 1841 diplomatic French and standing/granted values).

**Adverses:** coordinate with croire-33-tiebreak / croire-33-noun21, do not duplicate their bars.

## Method

Re-derived the full 33 census on the repaired stream: **n=25** windows. Confirmed the claim's counts byte-exact:
- `00 33` x8 @186, @408, @467, @846, @936, @1088, @1245, @1630
- `67 33` x6 @273, @1149, @1424, @1451, @1477, @1624
- `33 29` x5 @273, @626, @1232, @1424, @1477
- `67 33 46` x2 @1451, @1624

Frame inventory:
- **F1** `00 33` — 00="pour" granted (A9): infinitive slot → 33 must be infinitive-capable.
- **F2** `67 33` — 67=et/veut positional: infinitive slot ("veut [inf]" / "et [inf]").
- **F3** `33 29` — 29="er" pencil ground truth: A10 holds 33+29 as stem/whole; stem reading = [stem]+"er" infinitive formation.
- **F4** `67 33 46` — 46="que" pencil: "et/veut [33] que" → 33 must be a verb taking a direct `que`-complement (dire/croire/penser class).

Five candidates tested against all four frames: dire, croire, penser, laisser, faire.

## Window-level evidence

**F1 `00 33` x8** — "pour [33]": all 8 parse at frame level under any infinitive candidate (followers 16/79/21/01/96 are open complement slots; no forced contradiction for any candidate).
- @186 `37 06 00 33 16 00 66`, @408 `69 26 00 33 01 02 53`, @467 `42 96 00 33 79 80 06`, @846 `12 16 00 33 96 40 62`, @936 `69 26 00 33 21 64 37`, @1088 `55 81 00 33 79 80 06`, @1245 `87 11 00 33 16 00 67`, @1630 `69 26 00 33 21 64 37`

**F2 `67 33` x6** — three instances overlap F3 (@273, @1424, @1477) or F4 (@1451, @1624); the clean instance @1149 `98 86 67 33 66 84 02` ("veut/et [inf] [66] on…") parses under any infinitive candidate.

**F3 `33 29` x5** — stem face:
- @273 `11 06 67 33 29 89 84`, @626 `14 59 37 33 29 87 78`, @1232 `48 29 47 33 29 85 56`, @1424 `33 21 67 33 29 87 63`, @1477 `60 06 67 33 29 82 16`
- Under whole-word value V: "[V] er" — forced ungrammatical for dire ("dire er"), croire ("croire er"), penser ("penser er"), faire ("faire er"). No rescue: no 1841 construction places bare "er" after an infinitive; followers (89/87/85/82) admit no "er+X" word.
- Under stem value: only -er verb stems survive — 'laiss-'+"er", 'pens-'+"er" ✓; 'di'+"er"✗, 'croi'+"er"✗, 'fai'+"er"✗.

**F4 `67 33 46` x2** — the discriminator:
- @1451 `59 36 67 33 46 92 62`, @1624 `78 66 67 33 46 56 69`
- "et dire que" ✓✓ (idiomatic), "et croire que" ✓, "et penser que" ✓ / "veut penser que" ✓, "et désirer que" ✓.
- "et/veut laisser que" ✗✗ — **kill grade for 'laisser' as whole-word value** (laisser takes infinitive complements, never bare `que`).
- "et/veut faire que" ✗✗ — **kill grade for 'faire'** ("faire que" is not a construction).

## Per-clause pass/fail

**Clause 1 (≥2 independent frames parse):** No candidate clears all four frames.
| candidate | F1 pour+inf | F2 et/veut+inf | F3 stem+er | F4 [V]+que | result |
|---|---|---|---|---|---|
| dire | ✓ x8 | ✓ | ✗ forced ("dire er"; not an -er stem) | ✓✓ | FAIL |
| croire | ✓ x8 | ✓ | ✗ forced ("croire er"; not an -er stem) | ✓ | FAIL |
| penser | ✓ x8 | ✓ | ✗ forced as whole word ("penser er"); ✓ as stem ('pens'+'er') | ✓ | FAIL (single-string) |
| laisser | ✓ x8 | ✓ | ✓ ('laiss'+'er'; erstem valency) | ✗✗ KILL ("laisser que") | FAIL |
| faire | ✓ x8 | ✓ | ✗ (not -er) | ✗✗ KILL ("faire que") | FAIL |

**Clause 2 (zero forced contradiction):** FAIL for every candidate — each has ≥1 forced contradiction (F3 kills dire/croire/penser-whole/faire; F4 kills laisser/faire-whole).

## Key finding (for the red team)

**'penser' is the unique lexeme bridging both faces as ONE word**: whole-word 'penser' clears F1/F2/F4; stem 'pens-'+"er" clears F3. Every rival needs two different strings ({dire, X-er} per the tiebreak's dire-33-set; {laisser-stem, ?-whole} per erstem). So the duality collapses from "two values" to "one lexeme, two segmentations" — but promoting it still requires a ruling on whether 33 may be 'penser' in F1/F2/F4 positions and 'pens-' in F3 positions. That is a segmentation/polyvalence question, and §7 reserves polyvalence to the red team (67 et/veut is the sole true polyvalence). The bar's "zero forced contradiction" therefore fails at battery grade: **no single-string value can be named**.

Note on the erstem 'laisser' LEAD: it was a **stem-face** lead (conditional on 16/85). My F4 kill applies to 'laisser' as the **whole-word** value only — the stem-face lead stands uncontradicted. As a global hypothesis, penser now dominates laisser (penser explains all 25 windows as one lexeme; laisser leaves the 20 whole-word windows unexplained), but neither is nameable here.

## Adverses disposition

- **croire-33-tiebreak (null, dire/croire tie): COORDINATED, not duplicated.** Its bar tested dire-vs-croire discriminators; my bar tests the broader set (adds penser/laisser/faire). Its tie stands: dire and croire both still survive the whole-word frames. My F4 discriminator is new (it kills laisser/faire, which the tiebreak never tested) and consistent with its recorded tie.
- **croire-33-noun21 (queued): NOT TOUCHED.** Owns the `33 21` x3 asymmetry; none of my frames overlap its bar.
- The tiebreak's fenced residuals @1502/@1642 (fenced to 84/12): not re-litigated.

## Standing-verdict check

No contradiction with any standing verdict. A10 HOLD ("33+29 stem/whole", both faces retained) is **reinforced**, not challenged — my result is evidence for why the hold exists. croire-33-tiebreak null and erstem-33-id null both stand. Nothing escalated on contradiction grounds; the red-team follow-up below is a ruling request, not a contradiction.

## Verdict: NULL

No verb value satisfies the bar: every candidate carries a forced contradiction. The stem face and whole-word face select disjoint single-string values; 'penser' uniquely bridges them as one lexeme but needs a segmentation/polyvalence ruling the battery cannot give.

## Follow-ups (null regenerates work)

1. **`poly-33-redteam`** (P1, red-team venue): 33's faces select disjoint single-string values; 'penser' uniquely bridges as one lexeme (penser / pens-er). Rule: segmentation variance, homophone split, or polyvalence declaration (§7 — 67 et/veut is currently the sole true polyvalence).
2. **`val-33-penser-whole`** (P2, contingent on red-team face-split): test 33='penser' on whole-word frames (F1 x8, F2, F4 x2) for promotion; current lead exemplar of the -er+que class (penser/désirer/souhaiter).
3. **`stem-33-er-lexeme`** (P2): constrain the stem face — enumerate -er lexemes fitting the @1232/@1477 valency intersection (erstem's laisser-LEAD vs penser) once 16 and 85 resolve.
