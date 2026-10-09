# Battery report: premier-61-flank-census

- Target id: `premier-61-flank-census`
- Claim: "'Premier' is 61's conditioned value (or a one-off locus) - census all 18 61-windows for 'premier'-admission to decide and sharpen the val-61-premier locus promote."
- Date: 2026-10-09
- Worker: battery worker (subagent d289a0a6-4410-4ae7-a526-701aa223facb)
- Stream: repaired 1,847-pair / 96-type parse, re-derived in-session from `data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json` (asserts held: 1847 pairs, 96 types). `canonical.py` never used. R5005, sealed gate instances, and the red-team adjudication queue untouched.
- Lock: `code/crowd17/next-token/locks/premier-61-flank-census.lock` created on start, deleted on completion. No stale lock present.

## Bar (verbatim from battery-queue.json, pre-registered before testing)

"Census all 18 61-windows for 'premier'-admission (determiner/article/preposition left-adjacency, noun/verb right-adjacency). Decides whether 'premier' is 61's conditioned value or a one-off locus; sharpens the val-61-premier locus promote."

Numbered pass/fail clauses (restated before testing, not modified after):

1. **C1:** All 18 windows of 61 censused byte-exact, with left and right adjacency stated against standing values.
2. **C2:** 'premier'-admission tested per window: 61="premier" (masculine singular ordinal, licensed as prenominal adjective or nominalized noun) requires determiner/article/preposition left-adjacency OR noun/verb right-adjacency under standing values; each window graded admitted / flank-supported / excluded.
3. **C3:** Decide: if ≥2 independent windows admit 'premier' at proven battery grade, 'premier' is 61's conditioned value; if only @1556 admits, it stays a one-off locus (val-61-premier sharpened by the census); if a window actively excludes 'premier' under standing values, record it.

Verdict rule: **promote** iff C1–C3 pass with a conditioned-value decision; **kill** iff a window forces 'premier' false at @1556 (it does not); **null** iff the census yields no second proven admission (per the adverse: flank-supported-but-unproven = fence, not kill).

## Standing values used

- Pencil GT: 11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que.
- Granted: 87=ce, 64=qui, 96=par, 17=fois, 79=tout, 00=pour, 84=on, 47=ce (allophone).
- Provisional: 59=est, 77=le.
- Battery-grade (adopted, not re-litigated): 88=VERB class (2026-10-09); 55=verb class; 62='il' (il-62 promote); 21 noun-class (R18); 65 noun-class (R18); 24 finite-verb class-level (R17-009; 24="faire" value rejected at R18-008).
- Kills honored: 20 value search (closed); val-61-contact KILL of any global 61 value (no global claim made here); reseg-367-4961-bound ("premier pre fois" ungrammatical, adopted).

## Census (all 18 windows, ±4 context, center marked)

| @ | row | window | left-61 | right-61 | admission |
|---|---|--------|---------|----------|-----------|
| 223 | a2_01 | 42 16 24 89 **[61]** 96 87 46 98 | 89 (class open) | 96=par | EXCLUDED — 89 not det/article/prep; "premier par" unlicensed |
| 279 | a2_03 | 89 84 91 37 **[61]** 20 61 42 48 | 37 (predicative A1) | 20 (value-search killed) | EXCLUDED — 37 not det/article/prep; 20 unnameable |
| 281 | a2_03 | 91 37 61 20 **[61]** 42 48 52 89 | 20 (value-search killed) | 42 (predicative A1) | EXCLUDED — neither side licenses |
| 367 | a2_06 | 47 78 48 49 **[61]** 70 17 06 21 | 49 (open) | 70=pre (pencil) | EXCLUDED — "premier pre fois" ungrammatical (standing anti-leg) |
| 447 | a2_09 | 78 41 10 62 **[61]** 59 32 48 79 | 62 ('il') | 59=est (provisional) | EXCLUDED — "il premier" not an NP; bare "premier est" needs determiner |
| 577 | a3_02 | 78 45 13 55 **[61]** 94 82 06 06 | 55 (verb-class) | 94 ('ne' lead) | EXCLUDED — no licensed frame |
| 645 | a4_02 | 48 20 24 87 **[61]** 88 77 78 52 | 87=ce (granted) | 88 (verb-class) | FLANK-SUPPORTED — "ce premier [88]" licenses iff 88 finite (1 unstated assumption) |
| 926 | a5_10 | 08 65 71 17 **[61]** 96 48 82 98 | 17=fois (granted) | 96=par | ACTIVELY EXCLUDED — "fois premier" gender clash (fois feminine, premier masculine) |
| 1168 | a6_09 | 78 45 13 55 **[61]** 94 87 83 21 | 55 (verb-class) | 94 ('ne' lead) | EXCLUDED — same as @577 |
| 1206 | a7_00 | 58 47 43 55 **[61]** 21 65 64 59 | 55 (verb-class) | 21 (noun-class R18) | EXCLUDED — prenominal "premier [21-N]" needs a determiner; 55 is verb-class, not article |
| 1219 | a7_01 | 36 77 83 92 **[61]** 24 48 30 09 | 92 (open) | 24 (finite-verb class) | EXCLUDED — bare "premier [24-V]" needs determiner |
| 1256 | a7_02 | 06 65 46 01 **[61]** 31 29 69 88 | 01 (open; 01-verbclass NULL) | 31 (open) | EXCLUDED — 01 not det/article/prep at standing grade |
| 1281 | a7_03 | 56 85 48 53 **[61]** 56 32 98 55 | 53 (open; 53-split) | 56 (verb-class Xeent) | EXCLUDED — no licensed frame |
| 1429 | a7_08 | 29 87 63 91 **[61]** 12 16 76 49 | 91 (open) | 12=n (spelling letter) | EXCLUDED — neither side licenses |
| 1455 | a7_09 | 33 46 92 62 **[61]** 21 67 86 66 | 62 ('il') | 21 (noun-class R18) | EXCLUDED — "il premier" not an NP (same as @447) |
| 1510 | a7_11 | 86 56 41 12 **[61]** 59 39 81 88 | 12=n (spelling letter) | 59=est (provisional) | EXCLUDED — bare "premier est" ungrammatical; val-61-contact Frame C forces non-nominal here |
| 1556 | a8_01 | 23 99 13 93 **[61]** 40 17 11 26 | 93 (open) | 40=e (pencil GT) | ADMITTED — the val-61-premier locus ("première fois", PROMOTE) |
| 1810 | a8_10 | 94 52 80 04 **[61]** 15 93 50 42 | 04 (open) | 15 (open) | EXCLUDED — neither side at standing grade |

## Per-clause pass/fail

1. **C1: PASS** — all 18 windows censused byte-exact; n(61)=18 confirmed against the 1,847-pair stream.
2. **C2: PASS** — graded per window (see table): 1 admitted (@1556, the promoted locus), 1 flank-supported (@645), 15 excluded, 1 actively excluded (@926, gender clash).
3. **C3: FAIL (decide) → NULL** — no second window admits 'premier' at proven battery grade. @645's admission is flank-supported only (needs the unstated assumption that 88 is finite at @645); per the adverse, flank-supported-but-unproven = fence, not kill, and no global claim is made.

## Verdict: NULL (fence executed)

'Premier' is NOT 61's conditioned value: the census gives exactly one proven admission (@1556, the val-61-premier locus) and one flank-supported candidate (@645). It remains a one-off locus. The val-61-premier locus promote is sharpened: the census confirms its uniqueness across the full 61 population (no other window admits at proven grade), and @645 is now the named flank lead instead of an unsearched possibility. No standing or red-team verdict contradicted or downgraded; val-61-contact's KILL of any global 61 value stands and is not re-litigated; §7 intact. Canonical-stream caveat: 68 of 70 upstream row offsets unvalidated (rows listed above carry it).

## Adverse answered

"The 'premier' extension at the sandwich is flank-supported but not proven at this window (hence fence, not kill); no global claim is made per the standing val-61-contact KILL." — honored exactly: the one extension candidate (@645) is graded flank-supported, not promoted; no global 61 value claimed.

## Follow-ups proposed (all verified ABSENT from battery-queue.json on 2026-10-09)

1. `fin-88-645` (P3) — test 88's finiteness at @645 ("ce premier [88-V]"); a forced finite-88 upgrades @645 from flank-supported to proven and gives 'premier' its second locus.
2. `det-55-1206` (P3) — test 55's class at @1206; a non-verbal (article/determiner-shaped) 55 re-opens "55 premier [21-N]" as a prenominal-adjective frame.
3. `gender-61-926` (P4) — the @926 "fois premier" gender clash excludes masculine-'premier'; test whether any gendered adjective reading for 61 survives anywhere, constraining 61's class independent of the 'premier' question.
