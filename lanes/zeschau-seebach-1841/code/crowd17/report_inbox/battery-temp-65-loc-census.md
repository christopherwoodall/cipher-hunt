# Battery `temp-65-loc-census` — verdict: NULL (fence executed)

## Verdict
**NULL.** The census is complete and decisive as a negative: no window of 65 yields a temporal/locative/adverbial reading under standing values and 1841 French grammar. The bar's second arm fires — `98-65` is fenced terminally at @512, and 65's noun-class (R20-047) stands unconditioned.

## Bar tested (verbatim, pre-registered)
"≥1 frame leg with a time/locative reading under stated period evidence, or 98-65 is fenced terminally (this battery's fence becomes permanent and 65's noun-class stands unconditioned)."

Numbered clauses:
- C1 (leg arm): ≥1 of the 25 windows of 65 yields a temporal/locative reading with stated period evidence → PASS / FAIL.
- C2 (fence arm): if C1 fails, fence `98-65` terminally; 65's noun-class stands unconditioned → FIRES / does not fire.

## Method
- Stream: repaired 1,847-pair / 96-type parse re-derived in-session from `code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed like `repair_parse.py`. Asserts held: 1,847 pairs, 96 types. `canonical.py` never used.
- n(65) = 25, byte-exact. All 25 windows listed below with ±4 context (0-based @).
- Standing values applied: pencil GT (11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que); granted (87=ce, 64=qui, 96=par, 17=fois, 79=tout, 00=pour, 84=on, 47=ce); provisional (59=est, 77=le); 65 noun-class (R20-047 GRANT, gender deferred); 98=vient lead-grade (battery); 94=ne strong lead (R17-001); 24=en (R24).
- Period corpus check: `code/side-period/corpus` (whole-corpus regex census, 2,636 `vient+X` hits).

## Window-level evidence (all 25 windows)

| @ | row | window (±4) | temporal/locative/adverbial assessment |
|---|-----|-------------|----------------------------------------|
| 135 | a1_04 | 96 56 64 21 **65** 23 91 65 13 | "[21] [65] [23]…" — no temporal frame; 23 valueless |
| 138 | a1_04 | 21 65 23 91 **65** 13 66 14 74 | second 65 in same cluster; no temporal frame |
| 251 | a2_02 | 91 32 44 94 **65** 63 00 66 01 | "ne [65] [63] pour…" — clausal-ne frame, not temporal |
| 293 | a2_03 | 09 64 29 40 **65** 16 01 11 78 | "…ere [65]…" (29 40 65); no temporal frame |
| 372 | a2_06 | 70 17 06 21 **65** 63 29 85 82 | "21 65 63" cluster (×4 stream-wide); no temporal frame |
| 455 | a2_10 | 79 17 77 60 **65** 13 66 14 02 | "tout fois le [60] [65]…" — "tout"-frame, distributive not temporal |
| 512 | a3_00 | 62 94 64 98 **65** 88 56 87 77 | **THE 98-65 LOCUS** — "qui vient [65] [88-fin]"; see fence analysis |
| 687 | a5_00 | 92 64 29 40 **65** 94 29 60 03 | "…ere [65] ne…" (29 40 65); no temporal frame |
| 724 | a5_02 | 80 77 03 91 **65** 64 11 00 86 | "[91] [65] qui la…" — no temporal frame |
| 787 | a5_04 | 24 42 94 74 **65** 84 06 77 64 | "ne [74] [65] on…" — no temporal frame |
| 812 | a5_05 | 41 12 48 24 **65** 14 29 49 74 | **"en [65]"** — compatible with temporal/locative N, non-discriminating |
| 923 | a5_09 | 74 74 40 08 **65** 71 17 61 96 | "[65] [71] fois" — frequency frame; 65 noun-class blocks numeral reading |
| 1106 | a6_06 | 94 74 47 78 **65** 63 00 66 73 | "ce [78] [65] [63]…" — no temporal frame |
| 1112 | a6_06 | 00 66 73 41 **65** 38 30 69 11 | "[41] [65] [38] pas…" — no temporal frame |
| 1208 | a7_00 | 43 55 61 21 **65** 64 59 32 48 | "[21] [65] qui est…" — no temporal frame |
| 1253 | a7_02 | 46 26 30 06 **65** 46 01 61 31 | "…[06] [65] que…" — no temporal frame |
| 1340 | a7_05 | 71 64 60 08 **65** 64 52 38 47 | "[08] [65] qui…" — no temporal frame |
| 1383 | a7_06 | 92 69 13 24 **65** 68 52 82 16 | **"en [65]"** — compatible with temporal/locative N, non-discriminating |
| 1530 | a8_00 | 96 87 46 21 **65** 63 00 66 73 | "21 65 63" cluster; no temporal frame |
| 1588 | a8_02 | 00 36 70 64 **65** 48 29 47 08 | "qui [65] [48]…" — no temporal frame |
| 1608 | a8_02 | 70 39 11 92 **65** 23 08 55 83 | "la [92] [65]…" — no temporal frame |
| 1683 | a8_05 | 44 00 46 79 **65** 13 93 62 94 | "tout [65]…" — distributive "tout"+N, not temporal |
| 1712 | a8_06 | 12 06 29 40 **65** 94 44 59 30 | "…ere [65] ne…" (29 40 65); no temporal frame |
| 1748 | a8_08 | 46 56 40 06 **65** 34 07 28 89 | "…[06] [65] i…" — no temporal frame |
| 1781 | a8_09 | 59 19 48 74 **65** 23 98 83 82 | "[74] [65] [23] vient…" — no temporal frame |

Collocation summary: predecessors 21×4, 40×3, 74×3, 91/24/08/06×2, singles 94/60/98/78/41/64/92/79; followers 63×4, 23×3, 64×3, 13×3, 94×2, singles. `98 65` ×1 (@512 only). `24 65` ("en [65]") ×2 (@812, @1383). `29 40 65` ("ere [65]") ×3.

## Per-clause pass/fail

- **C1 — FAIL.** No window yields a temporal/locative reading:
  - The adverbial arm is excluded a priori: 65 is noun-class (R20-047), killing adverb-65.
  - The two `en [65]` windows (@812, @1383) are the only temporal/locative-*compatible* frames, but "en"+N is massively polysemous in 1841 French (manner, state, time, place) — compatibility is not a reading, and 65's value is open. Non-discriminating; not a leg.
  - `@923` ("[65] [71] fois") would need numeral-65, contradicted by the noun-class grant.
  - `@1683` ("tout [65]") is distributive ("tout homme"-type), not temporal.
  - All remaining 21 windows sit in non-temporal frames under standing values.
- **C2 — FIRES.** `98-65` fenced terminally at @512 ("qui vient [65] [88-fin]"):
  1. 98="vient" (lead-grade); 65 is noun-class → adverb-65 ("demain"-type) dead.
  2. Bare temporal/locative noun after "venir" is unlicensed in 1841 French — temporal complements need determiners ("venir le matin") or are adverbs ("venir demain"); locatives need prepositions ("venir à Paris").
  3. Corpus evidence: 0/2,636 `vient+X` instances in `code/side-period/corpus` take a bare temporal/locative noun (checked against {matin, soir, nuit, jour, lendemain, temps, moment, heure, minute, printemps, été, hiver, automne, France, Paris, ville, campagne, monde, lieu}).
  4. `98 65` is a hapax (1/1847) — no second window to rescue the reading.
  The fence is permanent: no future 65-value naming re-opens a temporal/locative reading at @512 (any noun value still faces causes 2–3). 65's noun-class stands unconditioned.

## Scope
Fences only the temporal/locative/adverbial reading of 65 (terminally at @512; unforced everywhere else). Untouched: 65's value, 65's noun-class (R20-047), gender (deferred), the `24 65` ×2 windows (compatible, unresolved), 98="vient" lead, and all standing/red-team verdicts. §7 intact. Canonical-stream caveat stands.

## Follow-ups proposed (all verified ABSENT from queue)
1. `temp-65-en-frame` (P3) — resolve the two `en [65]` windows (@812, @1383): name 65's value or class the "en"-complement; a temporal/locative value re-opens C1.
2. `val-65-value-census` (P4) — full 25-window value census for 65 under the granted noun-class; a named value settles the temporal/locative question as a corollary.
3. `temp-98-65-corpus-recheck` (P4) — replicate the "venir + bare noun" corpus check on a wider 19th-century corpus to harden the @512 fence; any genuine bare temporal/locative hit re-opens.

## Bookkeeping
- Report: `code/crowd17/report_inbox/battery-temp-65-loc-census.md` (this file).
- Stream re-derived in-session (`/tmp/t65_stream.json` scratch; asserts 1,847 pairs / 96 types held).
- Queue: `temp-65-loc-census` → `status: verdict`, `result: null`, 2026-10-09 (pre-write assert passed — was queued/verdictless; temp-file + rename; disk re-validated; own entry only; no downgrade).
- Lock created on start (2026-10-09T15:40:40Z), deleted on completion. R5005, sealed gates, red-team adjudication queue untouched. No standing/red-team verdict contradicted or downgraded.
