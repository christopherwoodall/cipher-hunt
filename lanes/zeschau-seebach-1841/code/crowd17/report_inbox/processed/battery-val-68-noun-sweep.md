# Battery report: val-68-noun-sweep

**Target:** `val-68-noun-sweep` (priority 3)
**Date:** 2026-10-09
**Worker:** 19f85588-29b1-431d-b8e5-4f09e10d60e6
**Verdict:** PROMOTE (nominal class; value unnamed)

## Bar (verbatim from queue)

"promote-nominal iff 68's class lands nominal with >=2 noun-frame legs at battery grade; if 68 resolves nominal, the adjective arm closes and the follower-65 fence hardens to kill"

## Bar restated as numbered clauses (frozen BEFORE testing, not modified after)

- (C1) 68's class lands nominal — not verb (already killed at battery level by battery-stem-68-id), not adjective, not polyvalent (§7: 67 is the sole true polyvalence).
- (C2) ≥2 noun-frame legs for 68 at battery grade (frame head granted/standing, 68 cleanly in the noun slot, no confound at battery level).
- (C3, consequence) If 68 resolves nominal: the adjective arm closes per §7, and the follower-65 fence (battery-follower-65-adjclass-census, NULL 2026-10-09) hardens to kill.

## Method

Read `BATTERY-PROTOCOL.md` in full. Created `locks/val-68-noun-sweep.lock` on start (agent id + 2026-10-09T09:45:42Z; no pre-existing lock, so no stale-lock note). Re-derived the repaired 1,847-pair / 96-type stream in-session from `code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt` parsed per `repair_parse.py` (asserts held: 1,847 pairs, 96 types). n(68) = 8, windows byte-identical to the standing census. `canonical.py` never used. R5005, sealed gate instances, and the red-team adjudication queue untouched. All @-offsets are 0-based pair indices on the repaired stream.

Standing premises cited (not re-litigated): 79="tout" (A5), 47="ce" (A4), 89 verb-host (A8), 37 predicative frame (A1), 06="ent" (ent-06), 21="suite" noun-class (N108), 59="est" provisional, 65=noun class, 00="pour" (A9), 11=la, 64=qui. battery-stem-68-id (KILL of 68 verb-hood, 2026-10-09): 68 leans nominal; no red-team verdict exists on 68's class.

## Window-level evidence (all 8 windows of 68)

- @114 (a1_03): `29 89 [68] 21 67` — "er [89-verb-host] [68] suite(noun) et/veut". 68 in verb-complement slot; "noun/adjective + suite" modifier frame. Nominal-leaning, weak — supporting only (complement class not granted).
- @504 (a3_00): `56 39 [68] 21 67` — "[39] [68] suite(noun) et/veut". Same modifier frame. Nominal-leaning, weak — supporting only.
- @884 (a5_08): `31 79 [68] 37 03` — "tout [68] [37-predicative]". **NOUN LEG 1 (battery grade).** Head 79="tout" granted (A5); A1 predicative frame granted with 37 as its value. Noun reading "tout N Adj-predicative" is grammatical. Adjective reading fails twice: "tout"+bare adjective with no head noun is ungrammatical (the lane's own exclusion, cf. follower-65 battery on "ce"+bare adjective), and the "tout"="very" intensifier alternative dies on the following 37 — "tout Adj predicative-Adj" with no noun is incoherent, while "tout N Adj" is clean. Pronoun reading fails the same way ("tout ça Adj" is ungrammatical). Only the nominal parse survives.
- @1286 (a7_03): `98 55 [68] 00 11` — "[98-finite] [55] [68] pour la fois". Object position after a finite verb — nominal-compatible, neutral (55's class open; not counted as a leg).
- @1384 (a7_06): `24 65 [68] 52 82` — "[65-noun] [68] [52]". The post-nominal "adjective arm". Post-nominal position is NOT a granted frame in §7, and no stated adjective value for 68 exists (battery-adj-68-postnominal is still queued, unrun). Not a battery-grade leg for either class; graded neutral.
- @1442 (a7_08/a7_09): `01 52 [68] 59 37` — "[68] est [37-pred]" (59="est" provisional). 68 in subject slot of the copula: anti-verb (forcing per battery-stem-68-id) and anti-adjective — a predicative adjective follows "est", it does not sit in its subject slot (substantivization would be nominal anyway). Pro-nominal.
- @1719 (a8_06/a8_07): `64 47 [68] 06 11` — "qui ce [68] ent la". **NOUN LEG 2 (battery grade).** Head 47="ce" granted (A4). Noun reading "ce [68ent] la" is grammatical (battery-stem-68-id's la-frame parse). Adjective reading needs a head noun after 68: 06="ent" is letters-tier (ent-06), not a noun; 11=la is a determiner — "ce Adj la" is ungrammatical. Only the nominal parse survives.
- @1788 (a8_09): `96 21 [68] 47 03` — "par suite [68] ce". Odd word order on both readings ("suite N ce" / "suite Adj ce"); graded neutral.

Distributional check: 68→48 occurs 0× (no feminine -e mark anywhere); 48→68 0×; no gendered value named in any window. 68's follower set: {21×2, 37, 00, 52, 59, 06, 47} — each a singleton except 21.

## Per-clause pass/fail

- (C1) 68's class lands nominal: **PASS.** Verb killed at battery level (battery-stem-68-id, forcing @1442 "[68] est", second @884 "tout [68]"). Adjective arm has zero battery-grade legs: post-nominal is not a granted frame, no stated adjective value exists, @1442 is anti-adjective (subject slot), @1788 is neutral. Two battery-grade noun legs land the class. §7 polyvalence bar (67 sole) not triggered — single nominal class.
- (C2) ≥2 noun-frame legs at battery grade: **PASS.** Leg 1 @884 ("tout [68]"+A1 predicative; granted heads A5/A1); Leg 2 @1719 ("ce [68]"; granted head A4; adjective alternative excluded by lane's own "ce"+bare-adjective rule). Supporting (non-leg): @114/@504 ("[68] suite" modifier frame), @1286 (object slot), @1442 (subject slot).
- (C3) consequence: **RECORDED.** Adjective arm closed per §7 (a landed noun does not coexist with the adjective arm). The follower-65 fence (battery-follower-65-adjclass-census) hardens from fence to kill: its only live adjective-arm candidate (68) is now nominal, and its C2a trigger (a gendered adjective among 65's followers) is permanently unfillable via 68.

## Adverses answered

- "Single value cannot be both noun and adjective under §7 (67 sole true polyvalence) — a landed noun closes the adjective arm, it does not coexist." **Answered:** this verdict lands nominal and closes the adjective arm explicitly; no coexistence claimed. The queued follow-up battery-adj-68-postnominal ("test 68 as post-nominal adjective") has its premise voided by this verdict — supervisor should kill/retire it rather than dispatch it. The queued battery-gender-65-independent probe is unaffected (it does not route through 68).

## Verdict rationale: PROMOTE (nominal class)

Both bar clauses pass at battery grade: 68's class lands nominal (C1) with two battery-grade noun legs (C2). No window forces the claim false at kill grade; no cleaner rival value is demonstrated on these frames (verb is killed, adjective has no stated value and no granted frame). No standing red-team verdict is contradicted — per battery-stem-68-id, no red-team verdict exists on 68's class, and this verdict agrees with the standing "leans nominal" battery finding. What is promoted is the CLASS claim (68 is nominal); the VALUE remains unnamed and open. Null follow-ups are not required (verdict is not null).

## Bookkeeping

- Queue: `val-68-noun-sweep` → status `verdict`, result `promote`, report `code/crowd17/report_inbox/battery-val-68-noun-sweep.md`, date 2026-10-09 (pre-write assert: was queued/verdictless; temp-file + rename; JSON re-validated; own entry only; no downgrade).
- Lock `locks/val-68-noun-sweep.lock` created on start, deleted on completion (verified gone).
- `canonical.py` never used; R5005, sealed gates, red-team adjudication queue untouched.
- Supervisor note: retire battery-adj-68-postnominal (premise voided by this verdict); follower-65 fence now hardens to kill per the bar's consequence clause.
