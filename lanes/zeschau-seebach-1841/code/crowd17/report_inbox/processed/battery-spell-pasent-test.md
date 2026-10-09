# Battery verdict: spell-pasent-test

**Target:** `spell-pasent-test` (priority 2)
**Date:** 2026-10-08 (CDT)
**Verdict: PROMOTE** — the four '30 06' windows are genuine residuals; the clerk single-consonant "pasent"-for-"passent" spelling hypothesis is killed at kill grade per the bar's iff condition (zero supporting instances stream-wide).

## Bar (verbatim from battery-queue.json)

> test ent-06's fenced "clerk-'passent'" hypothesis for the four '30 06' windows: census the stream's other 3pl '-ent' verbs for single-consonant clerk spellings; kill the spelling hypothesis iff zero supporting instances stream-wide

## Bar restated as numbered clauses (pre-registered before testing)

1. Census the stream's 3pl '-ent' verbs other than the four '30 06' windows, on the repaired 1,847-pair stream.
2. Count supporting instances of single-consonant clerk spellings among them (a supporting instance must be independent — a verb whose stem value is established on grounds other than the spelling hypothesis itself).
3. Iff the count is zero, kill the spelling hypothesis for the four '30 06' windows (they stand as genuine residuals).

## Method

- Parsed the repaired stream per `code/side-keyhunt/repair_parse.py` (`repaired_offsets.json` + `data/upstream-ct_R5005.txt`); `canonical.py` never touched. 1,847 pairs confirmed.
- Enumerated all 44 occurrences of 06 with ±2 context (full list in §Evidence).
- Ground values used: 30=pas (banked), 70=pre, 12=n, 82=m, 94=ne (pencil/granted tier). No other stem values assumed.
- Coordination with queued `spell-single-consonant` (global spelling battery): this battery is narrowed to the four '30 06' windows + the 3pl census only; the 'prenent' @1118 window is left to the global battery (not re-litigated, not duplicated).

## Evidence

### The four test windows (confirmed x4, byte-exact)

| # | 30@ | 06@ | context |
|---|-----|-----|---------|
| 1 | 1251 | 1252 | 26-30-06-65-46 |
| 2 | 1327 | 1328 | 56-30-06-62-94 |
| 3 | 1561 | 1562 | 26-30-06-60-71 |
| 4 | 1733 | 1734 | 56-30-06-60-12 |

All four read "pas"+"ent" = "pasent" under banked values. No fifth '30 06' window exists in the 44 06-occurrences.

### Census of the stream's other 3pl '-ent' verbs

Full 06 census (44 occurrences, @-offset of the 06): 6, 85, 184, 206, 215, 267, 271, 319, 346, 370, 399, 470, 522, 544, 580, 581, 666, 738, 773, 789, 890, 967, 1080, 1091, 1096, 1120, 1122, 1184, 1185, 1188, 1252, 1328, 1355, 1388, 1475, 1537, 1562, 1667, 1709, 1720, 1734, 1747, 1762, 1815.

Identifiable 3pl '-ent' verbs among them (stem value known or frame unambiguous):

1. **"mentent" x2** — 94-82-06-06 @578-581 (ctx 61-94-82-06-06-50-10) and @1182-1185 (ctx 78-94-82-06-06-59-42). Reads "ne"+"m"+"ent"+"ent" = "ne mentent", 3pl of mentir. Spelling is **standard**; the stem "ment-" contains no doubled consonant, so this window cannot test the single-consonant habit. Neutral control: shows the clerk spells standardly where no doubling is involved.
2. **"prenent" @1118-1120** — 70-12-06 = "pre"+"n"+"ent", one 'n' short of "prennent". This is the ent-06 battery's fenced, explicitly **unproven** single-n hypothesis (queued to `spell-single-consonant` for testing). Counting it as a supporting instance would be circular: it is the same hypothesis under test, not independent evidence for it. Fenced, not counted, not killed here (belongs to the global battery's scope).
3. **"entreprenne" @346** — 01-06-70 parses as "[01] entreprenne" per the ent-06 correction: subjunctive, not 3pl. Excluded from the census.

All remaining 06 windows have unknown stems or non-verbal frames (e.g. 11-06 "la ent", 64-06 "qui ent", 84-06 "on ent", 40-06 "eent", fenced junctions) — their French verbs cannot be identified, so no spelling assessment is possible. Stated as a limitation, not ignored.

### Supporting-instance count: **zero**

No independently identifiable 3pl '-ent' verb in the stream exhibits a single-consonant clerk spelling of a doubled stem. The only candidates are the unproven "prenent" (circular) and the standard-spelled "mentent" (neutral).

## Per-clause pass/fail

- **Clause 1 (census):** PASS. All 44 06-windows enumerated; every identifiable 3pl '-ent' verb classified with @-offsets.
- **Clause 2 (supporting-instance count):** PASS. Count = 0 independent supporting instances.
- **Clause 3 (iff → kill):** PASS. The iff condition fired: the clerk "pasent"-for-"passent" spelling hypothesis for the four '30 06' windows is **killed at kill grade**.

## Adverses

- **Coordinate with queued spell-single-consonant, do not duplicate:** answered. Scope held to the four '30 06' windows + 3pl census; 'prenent' @1118 explicitly left to the global battery; no window re-litigated.

## Verdict rationale

All bar clauses pass and the adverse is answered → **PROMOTE**. The claim's disjunction resolves to its second leg: the four '30 06' windows (@1251-1252, @1327-1328, @1561-1562, @1733-1734) are **genuine residuals** — hardened against the spelling-variant reading, not re-parsed as "passent". No standing verdict contradicted or downgraded. R5005, sealed gate instances, and the red-team adjudication queue untouched.

## Coordination note (not a verdict)

The global `spell-single-consonant` battery's bar requires its single-consonant rule to cover all 5 windows ('prenent' + 'pasent' x4) with zero contradiction. With the 'pasent' x4 leg killed here, that 5-window rule cannot be satisfied as stated — flagged for the global battery's re-test, no action taken here.

## Follow-ups

None required (promote). The four windows remain unparsed residuals; future re-parse work belongs to the normal queue, not this battery.
