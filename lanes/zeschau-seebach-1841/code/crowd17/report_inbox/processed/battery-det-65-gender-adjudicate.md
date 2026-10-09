# Battery verdict: det-65-gender-adjudicate

- Target: `det-65-gender-adjudicate`
- Claim: "65's gender adjudicated: the 'tout 65' masculine leg (@1683) vs the adj-32 feminine -e implication (@1211)."
- Date: 2026-10-09
- Worker: det-65-worker (uuid 30c05873-6cc5-44a3-a36c-fc37ccd25d37)
- Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`). `canonical.py` never used. All counts re-derived in-work. @-offsets are 0-indexed pair positions.

## Bar (verbatim from battery-queue.json)

"resolve iff a second gender-agreement window for 65 is found (a feminine 'toute'-cell contact, a gendered adjective/past participle agreeing with 65, or a second masculine determiner on 65) or one leg is killed (13's class kills the @1683 subject parse; or 32's duality resolution removes feminine -e at @1211)."

Restated as numbered pass/fail clauses (pre-registered before testing):

- **C1:** A second gender-agreement window for 65 is found: (a) a feminine 'toute'-cell in contact with 65, or (b) a gendered adjective / past participle agreeing with 65, or (c) a second masculine determiner directly on 65.
- **C2:** One leg is killed: (a) 13's class verdict kills the @1683 subject parse, or (b) 32's duality resolution removes the feminine -e at @1211.

Listed adverses: "Both legs conditional on unratified battery premises (13/93 classes for the masculine leg; 48='e' inflectional + 32's adjective arm for the feminine implication). Do not declare polyvalence; §7 (67 sole 'true polyvalence) binds."

## Method

Read BATTERY-PROTOCOL.md first. Created `locks/det-65-gender-adjudicate.lock` on start. Re-derived the stream in-work (1,847 pairs / 96 types asserted). Re-derived all 25 windows of 65 with ±8 context; byte-exact bigram census of 65's predecessors and followers; cross-checked every contact cell against standing class/value verdicts (protocol §7 + battery promotes/kills; unratified leads marked). Read the controlling downstream reports: battery-reseg-13-armA.md (PROMOTE), battery-fem-32e.md (NULL), battery-homophone-79-split.md (NULL), battery-stem48-65-value.md (NULL), battery-class-71-adjective.md (KILL). 1841 diplomatic French throughout. R5005, sealed gates, red-team queue untouched.

## Window-level evidence

### C1(a): feminine 'toute'-cell contact — NOT FOUND

- No cell with a standing feminine "toute" value exists in the lane. 79 = "tout" (A5-granted, masculine word). The 'tout'/'toute' allomorphy is the subject of the queued red-team docket `redteam-79-split-docket` (from battery-homophone-79-split NULL: @451/@1460 "tout fois" one 'e' from "toutefois", recorded as a red-team observation, not a finding). §7 binds: no split declared at battery level. Therefore no feminine 'toute'-cell can be put in contact with 65 at battery grade.
- Predecessor bigram census (byte-exact, all 25 windows): 21x4, 40x3, 91/74/24/08/06x2, 94/60/98/78/41/64/92/79x1. No feminine determiner (11=la, 47=ce, 87=ce) ever directly precedes 65: '11 65' x0, '47 65' x0, '87 65' x0.

### C1(c): second masculine determiner on 65 — NOT FOUND

- Determiner bigram census (byte-exact): '79 65' x1 (@1682, the leg under test); '77 65' x0; '11 65' x0; '87 65' x0; '47 65' x0.
- '21 65' x4 (@135/@372/@1208/@1530) cannot count: 21's value is unnameable at battery grade (w4-21-leftedge NULL) and 21's battery-grade value search is CLOSED (val-21-reopen KILL). No standing verdict names 21 a masculine determiner.
- No other predecessor cell has a standing determiner value. So the @1682 'tout 65' is the sole masculine-determiner contact in the stream.

### C1(b): gendered adjective / past participle agreeing with 65 — NOT FOUND

- Follower census (byte-exact, all 25 windows): 63x4, 23x3, 13x3, 64x3, 94x2, 16/88/84/14/71/38/46/68/48/34x1.
- Nameable followers: 63 = verb class (verb-63-frames PROMOTE); 13 = sub-lexical nominal-closing suffix (reseg-13-armA PROMOTE); 64 = qui (granted); 94 = ne (battery); 84 = on (A15 granted); 46 = que (GT); 38 = verb-form, finite forced at kill grade @1113 (noun26-38-profile PROMOTE); 71 ≠ adjective forced at kill grade (class-71-adjective KILL); 48 consumed by the promoted stem48-29 infinitive stem ("65 [STEM]er ce", stem48-65-value) — not an inflectional 'e' on 65.
- Open followers (23 x3 @135/@1608/@1781; 16 @293; 88 @512; 68 @1383; 34 @1748; 14 @812): no standing class verdicts; none nameable as a gendered adjective or past participle at battery grade. A post-nominal '65 14' (@812) has no licensed determiner/adjective parse under standing values.
- The one tempting feminine-inflection read — '65 48' @1588 as "65e" — is fenced: the battery-promoted stem48-29 reading consumes 48 into the infinitive stem, and re-litigating a promoted verdict is out of scope.

### C2(a): 13's class kills the @1683 subject parse — NO (leg survives)

- battery-reseg-13-armA PROMOTE (2026-10-09): at @1684, 13 closes the preceding nominal leftward as a suffix; the left leg "pour que tout [65]-13" (00=pour granted, 46=que GT, 79=tout granted, 65 promoted noun class) is the verdict's "strongest left leg"; the verb-class successor 93 starts the new clause.
- Consequence: the @1683 subject parse is CONFIRMED, not killed — "tout 65" remains the masculine subject NP of the pour-que clause (with 13 as its nominal-closing suffix). The masculine leg's 13-side condition is now battery-settled in its favor. (Caveat carried forward: the right-leg 93 = verb class is a promoted battery premise, unratified; 93 is unaffected by the 24='en' conflict.)

### C2(b): 32's duality resolution removes feminine -e at @1211 — NO (leg survives)

- battery-fem-32e NULL (2026-10-09): the @1211 window "65 64 59 32 48" = "qui est 32e par" parses CLEAN as a passive-shaped copula frame (C2 PASS); the closed set holds (exactly 4 '32 48' bigrams, zero '48 32'); the failure was epistemic (@855 unparseable, morphology intact), not kill-grade.
- Consequence: the feminine -e at @1211 is NOT removed. The duality resolution this bar route requires has not happened (adj-32 NULL stands; the resolution sits with the red team). The feminine leg's @1211 premise remains viable at battery grade.

### Adverses answered

- 13/93 classes (masculine leg): 13's side is now battery-promoted in the leg's favor (reseg-13-armA); 93's verb class is a promoted battery premise, unratified — recorded, not ignored.
- 48='e' inflectional + 32's adjective arm (feminine leg): 48='e' is letter-tier grant; the @1211 "est 32e" parse is clean (fem-32e C2); 32's adjective arm remains unresolved (adj-32 NULL) — recorded, not ignored.
- §7: no polyvalence declared. Both legs remain conditional; the tension recorded in battery-noun-65-value.md stands unchanged.

## Per-clause pass/fail

- **C1: FAIL.** No second gender-agreement window exists at battery grade: no feminine 'toute'-cell (allomorphy is red-team docket), no second masculine determiner (byte-exact: only '79 65' x1; 21 unnameable), no gendered adjective/PP agreeing with 65 (every nameable follower is verb/qu/que/ne/on/suffix; open followers unnameable).
- **C2: FAIL.** Neither leg is killed: the @1683 subject parse is confirmed by reseg-13-armA PROMOTE; the @1211 feminine -e is not removed (fem-32e NULL, @1211 parse clean).

## Verdict: NULL

65's gender remains unadjudicated at battery grade. Both legs survive the kill routes, and no second agreement window exists. The masculine leg ("tout 65" @1682–1683) is now the stronger of the two: its 13-side condition was battery-promoted in its favor (reseg-13-armA), it has zero counter-evidence across all 25 windows, and its only remaining threat is the 79 'tout'/'toute' value question — which is red-team docket. The feminine leg (@1211 "est 32e par") remains viable via the clean copula parse but is conditional on 32's unresolved adjective arm. Recorded as tension, not resolved. No standing verdict contradicted or downgraded; §7 intact.

## Follow-ups (null per §4 — for supervisor queueing)

### F1 id `toute-79-1682-retest` — priority 2
- claim: "79's value at @1682 ('79 65 13') re-tested once redteam-79-split-docket resolves the 'tout'/'toute' allomorphy: 'toute' kills the masculine leg; 'tout' records the leg's sole-determiner parse as red-team input."
- bars: "name 79's value at @1682 with <=1 ungranted assumption, conditioned on the red-team 79-split ruling; if 'toute', kill the 'tout 65' masculine leg; if 'tout', record the @1682 parse ('pour que tout [65]-13', reseg-13-armA) as the leg's red-team input. Do not re-declare the 79 split at battery level."
- evidence: "This report §§C1(a)/C1(c)/C2(a); battery-homophone-79-split NULL (@451/@1460 'tout fois' → 'toutefois' observation); battery-reseg-13-armA PROMOTE (@1684 left leg)."
- adverses: "Contingent on redteam-79-split-docket (queued); do not run before the ruling. §7 sole-polyvalence binds."

### F2 id `follower-65-adjclass-census` — priority 3
- claim: "Class census of 65's open adjective-position followers (23 x3, 88 @512, 16 @293, 68 @1383): any gendered adjective among them agreeing with 65 at its contact window supplies the second agreement window this bar needs."
- bars: "class each of {23, 88, 16, 68} with >=2 windows at battery grade; if any is a gendered adjective, test agreement with 65 at the contact window (@135/@1608/@1781, @512, @293, @1383); if none is gendered, fence the follower route with stated cause."
- evidence: "This report §C1(b): follower census 63x4/23x3/13x3/64x3/94x2 + singletons; nameable followers excluded (63 verb class, 13 suffix, 64=qui, 94=ne, 84=on, 46=que, 38 verb-form, 71≠adjective, 48 in stem48-29)."
- adverses: "34/14 followers already fenced (34=i letter; '65 14' @812 unlicensed under standing values). Do not re-litigate promoted verdicts (verb-63-frames, reseg-13-armA, stem48-65-value, class-71-adjective)."

### F3 id `fem32e-1211-redteam-input` — priority 2
- claim: "Ruling-ready red-team input packaging the @1211 feminine -e evidence for the 32-duality resolution: 'qui est 32e par' clean (fem-32e C2), closed set 4/4, morphology intact, @855 fenced with stated cause."
- bars: "produce the ruling-ready statement with @-offsets (449/855/1176/1211) and the three clean copula parses; no battery-level duality declaration; flag the 65-gender dependency (feminine 65 follows only via predicative agreement on 32's adjective arm)."
- evidence: "battery-fem-32e.md NULL §§Window-level evidence/Per-clause results; this report §C2(b)."
- adverses: "48='e' is letter-tier grant (R17); 32's adjective arm unresolved (adj-32 NULL). Coordinate with the red-team 32-duality docket; do not duplicate its bar."

## Provenance

n(65)=25, all bigram counts byte-exact on the repaired stream in-work. Lock `code/crowd17/next-token/locks/det-65-gender-adjudicate.lock` created 2026-10-09T07:22:38Z, deleted on completion. R5005, sealed gate instances, red-team adjudication queue untouched. `canonical.py` never used.
