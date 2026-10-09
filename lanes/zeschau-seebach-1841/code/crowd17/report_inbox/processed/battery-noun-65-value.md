# Battery verdict: noun-65-value

- Target: `noun-65-value`
- Claim: "Now that 65 is noun-class, test value hypotheses — candidates from 29 40 65 ('[X]ere 65': 65 as head noun after '-ere' word) and 65 64 59 32 ('65 qui est 32': predicative complement 32 constrains 65's semantics)."
- Date: 2026-10-09
- Worker: 54b66790-fd08-4676-aef0-d229ab379c7e
- Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`). `canonical.py` never used. All counts re-derived in-work. @-offsets are 0-indexed pair positions.

## Bar (verbatim from battery-queue.json)

1. "Value hypotheses grounded in the attested frames '29 40 65' and '65 64 59 32'."
2. "Do not re-litigate 65's noun-class (promoted); this is value discrimination only."
3. "Fail closed: if no hypothesis discriminates, null with follow-ups."

Restated as numbered pass/fail clauses (pre-registered before testing):

- **C1:** Value hypotheses are grounded in the attested frames '29 40 65' (x3) and '65 64 59 32' (@1208).
- **C2:** 65's noun-class (promoted, battery-prof-65) is used as premise only, never re-litigated.
- **C3:** If no hypothesis discriminates at promote/kill grade, verdict is null with 1–3 follow-up targets.

Listed adverses: none.

## Method

Re-parsed the repaired stream in-work. Re-derived: all 25 windows of 65 with ±8 context; predecessor/follower census of 65; the '29 40' x9 census; bigram checks '79 65', '87 65', '77 65', '11 65', '46 65'; all 13 windows of 32. Tested gender hypotheses (masculine vs feminine) and lexical-value discrimination against 1841 diplomatic French grammar. Standing values used as premises: banked GT (11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que); granted (87=ce, 64=qui, 96=par, 17=fois, 79=tout, 00=pour, 84=on, 47=ce); provisional (59=est, 77=le); battery-level, marked unratified where load-bearing (94=ne, 12=n, 48=e, 30=pas, 65=noun-class, 93=verb-shaped).

## Window-level evidence

### Frame inventory (re-derived on the repaired stream)

- n(65)=25. Predecessors: 21x4, 40x3, 91/74/24/08/06x2, 94/60/98/78/41/64/92/79x1. Followers: 63x4, 23x3, 13x3, 64x3, 94x2, 16/88/84/14/71/38/46/68/48/34x1.
- '29 40 65' x3 (65 at the right edge):
  - @291–293 (row a2_03): `89 28 00 97 09 64 29 40 [65] 16 01 11 78 40 97 86 91`
  - @685–687 (row a5_00): `23 09 07 00 92 64 29 40 [65] 94 29 60 03 39 74 46 02`
  - @1710–1712 (row a8_06): `62 94 88 26 12 06 29 40 [65] 94 44 59 30 64 47 68 06`
- '65 64 59 32' x1: @1208–1212 (row a7_00): `29 45 58 47 43 55 61 21 [65] 64 59 32 48 96 45 36 77` = "21 65 qui est 32 48…".
- Related bigrams: '65 64' (65 qui) x3 @724/@1208/@1340; '65 46' (65 que) x1 @1253; '65 94' x2 @687/@1712; '21 65' x4 @134/@371/@1207/@1529; '65 63' x4 @251/@372/@1106/@1530.
- Determiner check: zero of {11=la, 77=le, 87=ce, 47=ce} directly precede 65 in all 25 windows. '79 65' x1 @1682. '46 65' x0. 65 never takes an overt article/demonstrator — bare-NP distribution.

### Frame A: '29 40 65' x3 — the '-ère' word

- The word boundary after 40 is prior battery work (enne-word-64: "65=noun cls begins a new word" at all three windows); re-confirmed byte-identical here. The '-ère'-final word ends the prior clause/word; 65 opens the next.
- Left edges: `09 64 29 40` (@291), `92 64 29 40` (@685), `06 29 40` (@1710). The '-ère' word itself is unidentified in all three windows (syllable inventory open).
- Consequence for 65: in 2 of 3 windows 65 is followed by 94 ('65 94' @687/@1712). @1712 parses cleanly as "65 ne 44 est pas" = "65 n'est pas [44]" (59=est provisional, 30=pas battery-promoted; 44 in object-clitic slot between "ne" and "est", cf. "ne l'est pas"). @687's "65 94 29 60" does not parse under 94='ne' ("ne er" — fenced per prof-65, the lane-wide 12/94 duality). @293's "65 16 01" is open (16's class open). So: 65 = clause-initial subject of a negated verb in 1 clean window (@1712), 1 fenced (@687), 1 open (@293).
- Gender consequence: none. In @291/@685 the '-ère' word follows 64=qui, so "qui [adj]-ère 65" is ungrammatical — the '-ère' word cannot be a feminine adjective agreeing with 65. In @1710 ("06 [X]ère 65") no adjectival parse either. Frame A constrains 65's syntactic role, not its value or gender.

### Frame B: '65 64 59 32' @1208 — "21 65 qui est 32"

- "21 65" (noun-noun, cf. prof-65 L6) heads the qui-relative "qui est 32" (64=qui granted, 59=est provisional, 32 predicative per A1 frame grant).
- The predicative complement 32 cannot narrow 65's value: 32's own value is open (adj-32 verdict NULL; 32's verb/adjective duality @33/@855 is red-team-fenced). The only battery-level reading of "est 32 48" (feminine -e on 32, adj-32 clause 2) is conditional on 48='e' inflectional (battery-promoted, unratified) and on 32's adjective arm — see the tension recorded below.

### Gender test (the one discriminating attribute the frames yield)

- **H-masculine:** @1682–1685 (row a8_05): `03 39 74 77 44 00 46 79 [65] 13 93 62 94 79 14 60 27` = "…pour que tout 65 13 93…". 79="tout" (A5-granted masculine form) sits directly before 65 as determiner → 65 is masculine singular. "pour que" (00=que 46, A9) opens the subordinate clause, so "tout 65" is its subject NP; no clause boundary can intervene ("pour que tout" alone is ungrammatical). The parse needs 13 verb-capable ("tout 65 [13-verb] [93]") or 13="les"-pronoun + 93 verb ("tout 65 les [93-verb]"; 93 verb-shaped per battery-verb-93 promote 2026-10-09; 13's class open, queued). Single window; conditional on 13/93. **Zero counter-evidence in all 25 windows** (no feminine agreement on 65 anywhere).
- **H-feminine:** no positive leg. The only route — adj-32's feminine -e on 32 at @1211 forcing feminine 65 by predicative agreement — rests on a battery-level NULL verdict's sub-clause plus unratified premises (48='e' inflectional; 32's adjective arm). It cannot carry a gender claim; recorded as tension, not evidence.

### Lexical-value discrimination (attempted, fails)

- Tested whether any single French noun value is forced by, or selectable across, the frames. The full constraint set — masculine (1 conditional leg), bare-NP distribution (never articulated), subject of "est"/negated verbs, head of qui/que relatives, object of verbs (24, 63), "21"-compounds, "tout"-generic subject — is satisfied by an open class of masculine nouns (homme, peuple, roi, temps, bruit, …). "tout homme qui est 32", "l'homme n'est pas 44": all grammatical under standing values.
- The two predicative complements that could semantically narrow 65 are both value-open: 32 (adj-32 NULL, duality fenced for red team) and 44 (value open; queued pronoun-44-1714 — if pronominal, "n'est pas 44" constrains nothing).
- No lexical hypothesis can be promoted (no frame selects among candidates) and none can be killed at kill grade (no window forces a specific value false).

### Self-found tension (recorded, not adjudicated at battery level)

- The H-masculine leg (@1683 "tout 65") and the adj-32 feminine -e implication (@1211 "qui est 32[e]" → feminine 65 by agreement) are mutually inconsistent. Each is conditional on unratified battery-level premises (13/93 classes vs 48='e' inflectional + 32's adjective arm). This is a genuine standings tension for red-team / follow-up adjudication, not a battery-decidable conflict. Neither leg is ignored; neither is affirmed.

## Per-clause pass/fail

- **C1:** PASS — hypotheses (H-masculine, H-feminine, lexical-value field) grounded in the two frames plus the full 25-window census.
- **C2:** PASS — 65's noun-class used as premise only; no re-litigation (verb rival stays killed per prof-65).
- **C3:** TRIGGERED — no hypothesis discriminates at promote/kill grade → verdict null with follow-ups.

## Verdict: NULL

No value hypothesis for 65 discriminates on the attested frames '29 40 65' and '65 64 59 32'. Strongest lead, recorded not promoted: **65 = masculine** (single-window "tout 65" leg @1682–1683, conditional on 13/93's classes, zero counter-evidence across 25 windows). The frames pin down syntactic distribution strongly and gender weakly, but no lexical value. The masculine leg tensions the adj-32 battery's feminine -e implication at @1211 — both conditional, escalated via follow-ups. No standing red-team verdict contradicted; no battery verdict downgraded (94=ne, 48=e, 93=verb-shaped used as unratified premises, not re-litigated).

## Follow-ups (null per §4 — for supervisor queueing)

### F1 id `det-65-gender-adjudicate` — priority 2
- claim: "65's gender adjudicated: the 'tout 65' masculine leg (@1683) vs the adj-32 feminine -e implication (@1211)."
- bars: "resolve iff a second gender-agreement window for 65 is found (a feminine 'toute'-cell contact, a gendered adjective/past participle agreeing with 65, or a second masculine determiner on 65) or one leg is killed (13's class kills the @1683 subject parse; or 32's duality resolution removes feminine -e at @1211)."
- evidence: "This report §§Gender-test/Tension: '79 65' x1 @1682 ('pour que tout 65 13 93'); zero feminine agreement on 65 in 25 windows; adj-32 clause-2 feminine -e at @1211 ('65 64 59 32 48')."
- adverses: "Both legs conditional on unratified battery premises (13/93 classes for the masculine leg; 48='e' inflectional + 32's adjective arm for the feminine implication). Do not declare polyvalence; §7 (67 sole true polyvalence) binds."

### F2 id `val-44-1712-pronoun` — priority 2
- claim: "44 = pronominal at @1712 ('65 ne 44 est pas' = '65 n'est pas [le]'); if pronominal, the frame gives 65 no semantic constraint."
- bars: "name 44's class at @1712 iff '65 ne 44 est pas' parses with <=1 ungranted assumption; if pronominal, record 'n'est pas 44' as semantically empty for 65's value; if content noun/adjective, its value constrains 65."
- evidence: "@1710–1716 '06 29 40 65 94 44 59 30 64' (row a8_06); 44 in object-clitic slot between 'ne' (94) and 'est' (59 provisional); 30=pas battery-promoted."
- adverses: "44's value open lane-wide; coordinate with queued pronoun-44-1714 (this target is scoped to the @1712 window as input to noun-65-value, not a duplicate). 94='ne' battery-level."

### F3 id `ere-word-65-frames` — priority 3
- claim: "The '-ère'-final word(s) in the three '29 40 65' windows identified via syllable inventory; decides the '65 opens new clause as subject' parse."
- bars: "name the word(s) iff left-context syllables compose a French word ending '-ère' with the post-40 boundary (enne-word-64) holding at all three windows; else fence the window(s) with stated cause."
- evidence: "@289–295 '00 97 09 64 29 40 65 16 01'; @683–689 '07 00 92 64 29 40 65 94 29'; @1708–1714 '26 12 06 29 40 65 94 44'."
- adverses: "64=qui granted as word — a syllabic-'qui' reading inside the '-ère' word is untested against the grant's scope; 06/09/92 values open. Do not disturb the post-40 boundary (battery-held)."

## Provenance

R5005, sealed gate instances, and the red-team adjudication queue untouched. No invented data: every @-offset verified on the repaired 1,847-pair stream in-work. Lock `code/crowd17/next-token/locks/noun-65-value.lock` created 2026-10-09T06:14:13Z, deleted on completion.
