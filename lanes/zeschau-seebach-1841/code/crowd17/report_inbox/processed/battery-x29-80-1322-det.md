# Battery report: x29-80-1322-det

**Target:** `x29-80-1322-det` — "@1322 '80' tests determiner via 08's nominal compatibility".
**Worker:** battery worker x29-80-1322-det (session 2eab7d94-fdb9-4898-93d3-8e380efdeeac).
**Date:** 2026-10-09. **Verdict: NULL** (fence executed per the bar's else-arm).

## Bar (verbatim, pre-registered before testing)

"test the determiner-leaning reading of @1320-1323 ('faire [03]er [det] [N]') against 08's nominal compatibility; if 08 resists nominal, fence"

Restated as numbered clauses (fixed before testing, not modified after):

- **C1:** the determiner-leaning reading at @1320-1323 ('faire [03]er [80=det] [08=N]') parses with 08 as a licensed nominal complement at battery grade → land the reading.
- **C2 (else-arm):** if 08 resists nominal (no licensed standalone-nominal reading of 08), fence the determiner arm.

## Method

1. Read BATTERY-PROTOCOL.md first. Created `code/crowd17/next-token/locks/x29-80-1322-det.lock` on start (agent id + UTC timestamp); deleted on completion. No stale lock pre-existed.
2. Re-derived the repaired stream in-session from `code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`: **1,847 pairs / 96 types asserted**. `canonical.py` never used. R5005, sealed gate instances, red-team adjudication queue untouched. §7 standing constraints adopted, none re-litigated.
3. All @-offsets 0-based. Adopted (not re-litigated): stem-08-letter-probe PROMOTE (08 word-internal, 2026-10-09); x29-80-collocation NULL (parent; @1322 determiner-leaning, imperative fenced); pencil GT 29='er'.

## Window-level evidence (@-offsets, repaired stream)

- **Locus byte-confirmed:** 0b @1319–1323, row a7_04: `24 03 29 80 08` = "faire [03]er [80] [08]" (0b@1319=24, @1320=03, @1321=29('er'), @1322=80, @1323=08), followed by `62 98 56 30 06`.
- **08 census: n=18**, byte-exact (0-based): @35 (@34-37 '08 91 39' killed as three-word NP by stem-08-letter-probe), @60 ('41 08 34 29 40', crib-tail letter junction), @98, @198, @534, @631, @779, @881, @922 ('40 08' e-junction), @944 ('40 08' e-junction), @975, @1302, @1323 (locus), @1339, @1488 ('87 08 31', post-"ce"), @1520, @1592 ('47 08 81', post-"ce"), @1610.
- **Post-"ce" windows (parent's named test):** @1488 '87 08 31' and @1592 '47 08 81'. Both followers (31, 81) are value-open; neither window forces 08 standalone. Under adopted stem-08-letter-probe, 08 reads as word-internal/word-initial letter in both ("ce X…" with X a letter-headed word) — no nominal-standalone license.

## Per-clause results

- **C1 — FAIL.** The determiner arm needs 08 to stand as the nominal complement [N]. Adopted battery verdict stem-08-letter-probe PROMOTE names 08 word-internal: all three letter contacts (@60 junction 08→34='i', @922 40('e')→08, @944 40('e')→08) are segmentally licensed as French word-internal junctions, and no window forces a standalone-word reading of 08. Under §7 (67 et/veut the sole true polyvalence), a word-internal 08 cannot also stand as a word — its frame consequence already killed the '08 91 39' three-word NP. 08 therefore resists standalone-nominal at battery grade: it cannot fill the [N] slot of "faire [03]er [det] [N]". 08's value stays open; the class-level status is enough to block the frame.
- **C2 — EXECUTED.** Fence, per the bar's explicit else-arm. The imperative rival stays fenced per the parent (needs an ungranted clause boundary after 80); nothing in this battery revives it.

## Adverses answered

- **"08's value open (queued stem-08)":** honored — no value was named. Only class-level status (word-internal, value open) was used, which is sufficient for the frame test.
- **"imperative needs an ungranted boundary":** honored — the imperative arm is not revived; it remains fenced per the parent's reading.

## Verdict rationale

08 resists standalone-nominal at battery grade under the adopted stem-08-letter-probe promote, so the 'faire [03]er [det] [N]' reading cannot parse with 08 as [N]. The bar's else-arm fires: **fence** the determiner arm at @1322. Not kill-grade: the reading dies only on the adopted battery-level premise; a red-team ruling on 08's status could re-open it, and the '08 62' one-word rescue (08 as word-initial letter of the complement noun) was not in this bar's scope. No standing/red-team verdict contradicted or downgraded; §7 intact; canonical-stream caveat stands (row a7_04 unvalidated).

## Follow-ups proposed (all verified ABSENT from battery-queue.json)

1. `wordint-08-62-word` (P3) — test "08 62" as one noun at @1323–1324 (08 word-initial letter; "conseil"-shaped 'il'-final candidate via 62): if it parses as a licensed determiner complement, 80's determiner arm revives; else fence the det arm at @1322 permanently. Coordinates with stem-08-letter-probe, not re-litigated.
2. `ce-08-31-frame` (P3) — test "87 08 31" @1488 as "ce"+[word] vs standalone-08; discriminates 08's word status independent of the 80 frame.
3. `imp-80-1322-rerun` (P4) — gated re-test of the imperative-80 arm at @1322 if a licensed clause boundary ever lands after 80.

## Bookkeeping

- Queue: `x29-80-1322-det` → status `verdict`, result `null`, 2026-10-09 (pre-write assert passed — was `queued`/verdictless; temp-file + rename; JSON re-validated; own entry only; no downgrade).
- Lock `locks/x29-80-1322-det.lock` created on start, deleted on completion (verified gone).
- R5005, sealed gates, red-team queue untouched. `canonical.py` never used.
