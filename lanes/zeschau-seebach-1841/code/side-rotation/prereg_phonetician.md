# PRE-REGISTRATION — Phonetician CV-structure tests (side-rotation)

**Role:** PHONETICIAN, rotation-fleet. **Date:** 2026-10-07.
**Rule:** this file was written BEFORE any test statistic was computed.
If anything below was violated in execution, the deviation is noted in the results JSON.

## Context
The rotation (chi²=366.3, repaired 1,847-pair parse, phases in
`code/crowd4/phase_map_repaired.json`; T0-verified exact) has killed every
coarse linguistic mapping: NOT word-position (tuner, N15), NOT morphological
slot (segmeter T1, F43), NOT polyvalence conditioner (T2), NOT unit size
(T3), NOT syntactic class (T4). This work order tests FINER phonetic
structure among anchored + high-confidence groups using the crib-learned
inventory (F44) — not standard French syllabification.

## Test set (n=16, statuses marked — per the work order's exact list)

Phase assignments read from `code/crowd4/phase_map_repaired.json` (A=32, B=27, C=17, R=20;
all 16 anchors are in A/B/C; no R exclusions needed).

| group | value | status | phase | phonetic (crib-learned, F44) | open/closed | sonority |
|---|---|---|---|---|---|---|
| 11 | la | GT pencil crib | B | /la/ CV whole word | open | balanced (1C1V) |
| 70 | pre | GT pencil crib | B | /pʀe/ onset-cluster syllable | open | **heavy** (2C1V) |
| 82 | m | GT pencil crib | A | /m/ bare consonant | closed | **heavy** (1C0V) |
| 34 | i | GT pencil crib | B | /i/ bare vowel | open | light (0C1V) |
| 29 | er | GT pencil crib | C | /eʀ/ ending (frenchman: "qui erre" er\|e) | closed | balanced (1V1C) |
| 40 | e | GT pencil crib | A | /ə/ mute -e written | open | light (0C1V) |
| 46 | que | GT pencil crib | B | /kə/ (46→62=0×: "qu'on" one syllable) | open | balanced (1C1V) |
| 87 | ce | PROVISIONAL (red team demoted) | A | /sə/ proclitic | open | balanced |
| 64 | qui | PROVISIONAL | B | /ki/ whole word | open | balanced |
| 96 | par | PROVISIONAL (CONFIRMED 4/4, inherits 87's provisionality, F28) | C | /paʀ/ | closed | **heavy** (2C1V) |
| 94 | ne | PROVISIONAL-strong (cond. "en" /ɑ̃/ — also vowel-final) | B | /nə/ | open | balanced |
| 77 | le | LEAD | C | /lə/ | open | balanced |
| 62 | on | STRONG LEAD | A | /ɔ̃/ nasal monosyllable | open | light (0C1V) |
| 78 | me | LEAD (rival word-internal "ver" /vɛʀ/ noted in inventory) | C | /mə/ **primary** | open | balanced |
| 47 | ce | LEAD | A | /sə/ | open | balanced |
| 52 | pas | STRONG-bounded (cond. "so" /so/, "se" /sə/ — ALL phonetically open) | C | /pa/ (silent s) | open | balanced |

**Phonetic-value source rule:** the crib-learned inventory shapes
(`code/crowd5/unit_inventory.json`) plus Frenchman ear checks
(`code/crowd3/frenchman_results.md`: er\|e segmentation, by-ear "pre" for
"prend", /kɔ̃/ fusion). Spelling does NOT decide: "pas"=/pa/ is open despite
CVC spelling; "er"=/eʀ/ is closed despite being a single syllable.

**Exclusions (pre-registered):** 06/86 (verb-stem-class, class-level, NO single
phonetic value — unassignable); 67=veut (not in the work-order's list).

**Sonority rule (pre-registered):** consonant-heavy = C-count > V-count
({70 pre, 82 m, 96 par}); all others vowel-like/balanced. (82 is the only 1C0V;
"er" is 1V1C → balanced, NOT heavy.)

**Tier rule (pre-registered):** Tier0 = 7 pencil cribs; Provisional = {87, 64, 96, 94};
Lead = {62, 78, 47, 77, 52}.

## Pre-registered tables (before computation)

- **Test A — open/closed × phase (2×3):** A: open 4 / closed 1; B: open 6 / closed 0; C: open 3 / closed 2. n=16.
- **Test B — tier × phase (3×3):** Tier0: A2/B4/C1; Prov: A1/B2/C1; Lead: A2/B0/C3. n=16.
- **Test C — sonority × phase (3×3):** light: A2/B1/C0; balanced: A2/B4/C4; heavy: A1/B1/C1. n=16.
  (Correction, pre-execution: the T-Pc table was mis-tabulated by hand in the
  first draft as "light A4/B5/C4"; the correct pre-registered table is the one
  above. No statistic had been computed when this was caught — the script
  asserts the table before testing.)

## Tests

1. **T-Pa (open vs closed):** Freeman-Halton exact (full enumeration of fixed-margin
   tables, Fisher probability-definition), two-sided, α=0.05.
2. **T-Pb (tier):** same exact 3×3 test, α=0.05.
3. **T-Pc (sonority):** same exact 2×3 test, α=0.05.
4. Baseline = independence with fixed margins (lane convention).

## Robustness variants (pre-registered)

- **T-Pa2:** open/closed × phase on GT+provisional only (n=11; exclude LEADs 62, 78, 47, 77, 52).
- **T-Pa3:** sensitivity — recode 78 as the rival word-internal "ver" (/vɛʀ/, closed); recompute T-Pa.
- **T-Pc2:** sonority × phase on GT+provisional only (n=11).
- No robustness variant for T-Pb (the tiers are the test).

## Multiple comparisons

Three primary tests. Report raw exact p-values. **Any survival claim must also
pass Bonferroni α/3 ≈ 0.0167 AND Red Team re-derivation** before merging.

## Power (honest, stated before running)

- n=16 (n=11 in variants). Power is poor by construction — stated in the work order.
- I will report the minimum p attainable under the observed margins (how extreme
  the table would need to be) and simulation-based power for a strong alternative
  (all 3 closed/heavy units in one phase; and Cramér's V≈0.6 alternatives).
- Expectation: NULL — which is informative (constrains what the phases are NOT).

## Decision rule

- p ≥ 0.05 → killed/null for that subtest; report exact p, table, n.
- p < 0.05 → survives to RED TEAM re-derivation; NOT merged until the Red Team
  independently re-derives it from the raw files.
