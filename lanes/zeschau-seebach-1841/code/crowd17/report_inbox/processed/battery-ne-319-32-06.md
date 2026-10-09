# Battery report: ne-319-32-06

Target: `ne-319-32-06` — claim "'32 94 06' (@319) - test '[32]ne' word-internal once 32's predicative value resolves; gates on adj-32".
Worker: 1b9036f7-c9c3-41bd-97cc-71c45d94ff91. Date: 2026-10-09.
Stream: repaired 1,847-pair / 96-type parse (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py` via `load_rows` + `parse`). `canonical.py` never used. R5005, sealed gates, red-team adjudication queue untouched. No data invented. @-offsets below are 0-based pair indices unless marked 1-based. Asserts held: 1,847 pairs, 96 types.
Lock: `code/crowd17/next-token/locks/ne-319-32-06.lock` created 2026-10-09T21:04:19Z; no stale lock present.

## Bar (verbatim, pre-registered from battery-queue.json, BEFORE testing)

"resolve iff '[32]ne' parses word-internally at @319 once 32's value resolves; else fence"

Numbered pass/fail clauses (frozen before testing):

1. **C1 (resolve arm):** 32's predicative value resolves, and '[32]ne' parses word-internally at @319 under that value.
2. **C2 (fence arm):** else fence with stated cause.
3. **C3 (adverses):** no standing/red-team verdict contradicted; 94='ne' STRONG LEAD honored; A1 predicative grant for 32 and verb-32's single-lexeme PROMOTE respected, not re-litigated.

## Standing values used (protocol §7)

Pencil GT: 11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que. Granted: 87=ce, 64=qui, 96=par, 17=fois, 79=tout, 00=pour, 84=on, 47=ce. Provisional: 59=est, 77=le. Frames: A1 (37/32/42 predicative), A8, A9, A15. 94=ne STRONG LEAD (R17-001); 48=e letter tier (R17).

Adopted premises (not re-litigated): battery-val-32-narrow NULL (2026-10-09); battery-adj-32 NULL (2026-10-08); battery-adj-32-inflect-gate NULL (2026-10-09); battery-ne-94-non12-prefamily NULL (2026-10-09, parent of this target).

## Method

1. Re-derived the repaired stream in-session; byte-confirmed the locus and censused '32 94', '94 06', '32 94 06' stream-wide.
2. Checked 32's value-resolution status in battery-queue.json (all 32 value/value-class targets) — the bar's dependency.
3. Evaluated whether '[32]ne' word-internal is statable under standing values at the locus.

## Findings — window-level evidence

- Locus (0-based): `@315=64 @316=59 @317=32 @318=94 @319=06 @320=11 @321=92 @322=60 @323=15`, row a2_04. The claim's 1-based "@319" is the 06 pair; the '32 94 06' trigram sits at 0-based @317–319.
- Under standing values: `45 ce(?) 64=qui 59=est(prov) [32] 94=ne(STRONG LEAD) [06] 11=la [92] [60] [15]` — "… qui est [32] ne [06] la [92] [60] [15]".
- Census: '32 94' occurs exactly 1x stream-wide (@317); '94 06' exactly 1x (@318); '32 94 06' is a hapax. No family exists for this composition.

### C1 dependency: 32's value did NOT resolve

- `adj-32` → verdict/null (2026-10-08).
- `adj-32-inflect-gate` → verdict/null (2026-10-09).
- `val-32-narrow` → verdict/null (2026-10-09) with TWO independent value-independent blocks: (i) ~20 identical-parsing verb candidates (parsing ≠ naming); (ii) the @33 bare-3sg vs @855 '-e' 3sg finite-morphology contradiction — no French verb has both. Resolution belongs to the 32-duality docket, R20-DEFERRED red-team venue.
- `morph-32-finite-inconsistency` → still queued; `adj-32-inflect-gate-2` → still queued.
- The "once 32's value resolves" condition is therefore UNMET, and resolution is blocked at battery grade — not merely pending.

### The '[32]ne' composition itself is not statable

- The parent battery-ne-94-non12-prefamily (null) already classified this exact window (its 1-based @319, pre-94=32) in the "no French word can be stated without inventing data" family (item 9: every pre-94 in {44,32,42,52,86,28,35,22,33,65,78,07} is open, noun-class-only, or predicative-grant-with-open-value).
- val-32-narrow L3: the only letter-tier neighbor in direct contact with 32 stream-wide is 48='e' (inflectional, not lexical); "no '32+X' contact spells a French word stem."
- So '[32]ne' word-internal requires naming a French "[value]ne" word with 32's value open — unstatable. This is independent of the dependency: even if 32's class resolved, no composition leg exists under standing values today.

## Per-clause pass/fail

- **C1 (resolve arm): FAIL.** 32's predicative value did not resolve; value-naming is blocked at battery grade by a value-independent morphological contradiction (val-32-narrow), and the 32-duality docket is red-team venue (R20 DEFERRED).
- **C2 (fence arm): FIRES.** Fence with stated cause: (i) the bar's dependency (32's value resolves) is unmet and blocked at battery grade; (ii) '[32]ne' word-internal is not statable under standing values — parent census and val-32-narrow L3 both close it. Evidentiary fence, re-openable on 32's value resolution or a newly statable composition.
- **C3 (adverses): PASS.** The target's adverse enumeration is adopted as-is. 94='ne' STRONG LEAD untouched (the particle reading is not at issue); A1 predicative grant for 32 untouched; verb-32's single-lexeme PROMOTE not re-litigated; §7 intact. No standing or red-team verdict contradicted, downgraded, or re-decided.

## Verdict: NULL (fence executed)

## Follow-ups (verified ABSENT from battery-queue.json, left for supervisor)

1. `ne319-32-06-rearm` (P4) — re-run this target's bar once 32's value resolves; fires on `morph-32-finite-inconsistency` verdict or red-team 32-duality adjudication, whichever first names 32's predicative value at battery grade.
2. `ne94-06-rightedge-319` (P4) — test the rival composition direction at @318–319: 94='ne' eliding rightward ("n'") into 06 versus the leftward '[32]ne' tested here; determine whether "qui est [32] ne [06] la" admits any licensed parse under standing values, or fence the whole window as a segmentation residual.

## Bookkeeping

Queue `ne-319-32-06` → `status: verdict`, `result: null`, 2026-10-09 (pre-write assert passed — was queued/verdictless; target-id-unique tmp `battery-queue.json.ne-319-32-06.tmp` + atomic rename; disk re-validated; own entry only; no downgrade; no tmp leftover). Lock created on start (agent 1b9036f7-c9c3-41bd-97cc-71c45d94ff91, 2026-10-09T21:04:19Z), deleted on completion (verified gone). R5005, sealed gates, red-team adjudication queue untouched. Canonical-stream caveat stands (row a2_04 offsets unvalidated).
