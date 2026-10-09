# Battery verdict: ne-94-non12-prefamily

Worker: session f1e26749-7653-40b3-b578-41041aa41462. Date: 2026-10-09.
Target: `ne-94-non12-prefamily` (P3). Lock created 2026-10-09T04:24:29Z, deleted on completion.
Stream: repaired 1,847-pair / 96-type parse (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed per `repair_parse.py`). `canonical.py` never touched. R5005, sealed gates, red-team adjudication queue untouched.

## Bar (verbatim, pre-registered)

"if >=1 independent word-internal-94 window exists with stated boundaries, the @508 parse gains a family; else @508 stands alone as the sole non-12 pre-94 'ne'-final candidate"

Numbered clauses (stated BEFORE testing, unchanged after data):

1. >=1 independent word-internal-94 window exists with stated boundaries (French word named, 94's syllable role stated, pre-94 is a syllable-valued pair other than 12='n', and the window is not the @508 window itself) — then the @508 parse gains a family.
2. ELSE @508 stands alone as the sole non-12 pre-94 'ne'-final candidate.

Adverses (from brief): 94='ne' STRONG LEAD caveat (R17-001); §7 — no battery-level polyvalence declaration. Answered: no value named, no polyvalence declared, the 94='ne' standing untouched.

## Method

Re-derived the full 94 census on the repaired stream (94 n=37, verified). Enumerated every window where pre-94 != 12 (35 windows; the two excluded 12-94 windows are 1-based @350/@1550, the "prenne" family, battery-confirmed by enne-family-12-94 PROMOTE). For each non-12 window, asked whether a word-internal-94 parse with stated boundaries exists in the standing battery/red-team record — a boundary is "stated" only if the French word is named and 94's syllable role given under granted/promoted values, not open ones.

## Window-level evidence (1-based @, pre-94 -> 94)

Full non-12 set (35 windows): @102, @162, @251, @319, @495, @510, @559, @571, @579, @652, @689, @700, @763, @772, @775, @786, @842, @1103, @1170, @1183, @1294, @1331, @1354, @1364, @1577, @1665, @1688, @1702, @1706, @1714, @1743, @1774, @1796, @1807. (@510 is the target @508 window: 0-based @508=62, @509=94, row a3_00 "67 77 62 94 64 98 65".)

Closest family candidates, each tested:

1. **@579 and @1170 (pre-94 = 61):** "13 55 61 94 82 06 06" (@579) and "13 55 61 94 87 83 21" (@1170). The 55-61-94 word claim (seg-61-94-word) is verdict/**null** — neither demonstrated nor broken. A null claim supplies no established family member. Seg-55-61-21-stem (promote) further tensed the letter-level framing ("55='re'+61='pren'+94='ne'" conflicts with "pre"+"nd"). Not an established word-internal-94 window.
2. **@689 (1-based, "65 94 29 60"):** "n'erre" possible with 94 as letter **'n'** (29='er' GT), not 'ne'-final syllable; 65's value open, so no word is statable. Not a 'ne'-final candidate.
3. **@1331 ("62 94 70 52"):** the map's note "ne pre[52]" — if 52 completes a verb this is clausal 'ne' before "prendre"-family (70='pre' GT), not word-internal 94; a word-internal "[62]ne" cannot be stated (62's value open; sel-62-48-94 KILL confirms 62-94 is clausal). Not established.
4. **@571 ("45 94 52"):** 45='ce' under the A11 HOLD ("ce ne [52]" clausal); 45's pre-94 position is not 78, so the 'dict' lead is unavailable. Clausal, not word-internal.
5. **@1743 ("34 94 82"):** "i"+"ne"+"m" — no French word; strained arm of the 94-duality map.
6. **@772/@775 (pre-94 = 06='ent'):** "ent"+"ne" — no French word; 06's promoted 'ent' value gives no composition.
7. **@652/@1103/@1577 (pre-94 = 82='m'):** "m"+"ne" — no French word.
8. **@102/@763/@842/@1331/@1364/@1688/@1706/@1774 (pre-94 = 62):** all clausal 'il/on ne' per battery-collision-62-84 (8 clean windows + @508 fenced residual); sel-62-48-94 KILL closed the word-internal selector claim.
9. **@251/@319/@495/@786/@1796/@162/@559/@700/@1294/@1807/@1665/@1702/@1714/@1183/@1354/@1664 (pre in {44,32,42,52,86,28,35,22,33,65,78,07}):** every pre-94 value is open, noun-class-only, predicative-grant-with-open-value, or leads on open values; no French word can be stated at any of them without inventing data. None is an established word-internal-94 window.
10. **@1169 (0-based, 1-based @1170):** classified by the duality map as "ne ce" (particle-ungrammatical, 87='ce' granted); no word-internal "[61]ne"+"ce" composition is statable.

Standing-verdict sweep: the only PROMOTE-grade word-internal-94 evidence in the lane is the 12-94 "prenne" family (enne-family-12-94, pre=12, excluded by the bar) and the 12-94/94-'ne' letter claims. No standing promote, lead, or grant puts word-internal 94 after a non-12 syllable at any other window.

## Per-clause pass/fail

- **Clause 1 (family member found): FAIL.** Zero independent word-internal-94 windows with stated boundaries and non-12 pre-94 exist in the standing record. The only established word-internal-94 family is the 12-94 "prenne" pair, excluded by the bar.
- **Clause 2 (else-arm): FIRES.** @508 (0-based @509 94, 1-based @510) stands alone as the sole non-12 pre-94 'ne'-final candidate.

## Verdict

**NULL (fence executed).** The else-arm fires: @508 stands alone; the word-internal-94 family question closes at battery grade with no family found. No standing verdict contradicted or downgraded (94='ne' STRONG LEAD R17-001 untouched; ne-508-reseg's fence to the 12/94 duality adjudication untouched; §7 intact — no polyvalence declared).

## Follow-ups proposed (all verified absent from queue)

1. **seg-61-94-word-adjudicate** (P2): the 55-61-94 word claim (@579/@1170) is the only live non-12-pre-94 family candidate; it is NULL-standing. Bar: promote iff the red team ratifies a named French word with 61-94 as syllables at both windows; else the family candidacy closes.
2. **ne-1331-70-52-parse** (P3): decide "62 94 70 52" — clausal 'ne' before a "prendre"-family verb vs word-internal "[62]ne" — once 52's and 62's values resolve; gates on both.
3. **ne-319-32-06** (P3): "32 94 06" — test "[32]ne" word-internal once 32's predicative value resolves; gates on adj-32.

## Bookkeeping

`battery-queue.json` updated via temp-file + rename (`ne-94-non12-prefamily`: queued -> verdict/null, pre-write assert confirmed queued/verdictless, JSON re-validated post-write). Lock deleted. Report: code/crowd17/report_inbox/battery-ne-94-non12-prefamily.md.
