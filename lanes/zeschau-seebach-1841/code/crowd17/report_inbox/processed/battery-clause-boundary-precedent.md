# Battery `clause-boundary-precedent` — report

## Bar (verbatim, from `battery-queue.json`)

"survey all stream windows shaped 'X 77 [open-value]' (article + unresolved value); find >=2 windows where a clause boundary demonstrably resolves the adjacency with a complete clause on each side, or record the survey negative"

## Bar restated as numbered clauses (pre-registered before testing)

- **C1.** Census all stream windows shaped `X 77 [open-value]` (article + unresolved value).
- **C2.** ≥2 windows where a clause boundary between 77 and the open-value follower demonstrably resolves the adjacency with a complete clause on each side. (Demonstrable = left clause "...X le." complete under standing values with 77 as terminal clitic, AND right clause "Y ..." complete with Y classless-but-parsing as a clause opener under standing values — no ungranted assumptions on either side.)
- If C2 fails, the bar's negative arm fires: record the survey negative.

## Method

Stream re-derived in-session from `code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`: 1,847 pairs / 96 types / 70 rows confirmed. `canonical.py` never touched. Standing values from `code/table-grid/table-registry.json` plus BATTERY-PROTOCOL §7 (banked GT: 11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que; prom: 87=ce, 64=qui, 96=par, 17=fois, 79="tout", 00="pour", 84="on", 47="ce", 12='n', 06='ent', 48='e'; provisional: 59=est, 77="le"). Test run under provisional 77='le' (see Adverse).

## C1 — census

n(77) = 44 windows, 35 distinct `X 77 Y` shapes (0-based @, X, 77, Y, row):

| @ | X | Y | row | @ | X | Y | row |
|---|---|---|-----|---|---|---|-----|
| 7 | 06 | 78 | a1_00 | 968 | 06 | 76 | a6_00 |
| 87 | 88 | 66 | a1_02 | 1033 | 80 | 11 | a6_03 |
| 145 | 64 | 84 | a1_04 | 1041 | 17 | 82 | a6_03 |
| 207 | 06 | 44 | a2_00 | 1057 | 23 | 84 | a6_04 |
| 213 | 74 | 78 | a2_00 | 1077 | 48 | 78 | a6_05 |
| 259 | 43 | 84 | a2_02 | 1133 | 24 | 86 | a6_08 |
| 430 | 63 | 86 | a2_09 | 1158 | 17 | 82 | a6_09 |
| 453 | 17 | 60 | a2_10 | 1180 | 37 | 78 | a6_10 |
| 507 | 67 | 62 | a3_00 | 1216 | 36 | 83 | a7_00 |
| 516 | 87 | 80 | a3_00 | 1240 | 67 | 81 | a7_01 |
| 521 | 91 | 06 | a3_00 | 1306 | 43 | 74 | a7_04 |
| 612 | 47 | 87 | a4_00 | 1351 | 48 | 78 | a7_05 |
| 639 | 67 | 89 | a4_01 | 1401 | 67 | 81 | a7_07 |
| 647 | 88 | 78 | a4_02 | 1446 | 64 | 84 | a7_09 |
| 677 | 37 | 45 | a5_00 | 1484 | 46 | 84 | a7_10 |
| 721 | 80 | 03 | a5_02 | 1542 | 88 | 78 | a8_00 |
| 744 | 67 | 81 | a5_02 | 1598 | 67 | 81 | a8_02 |
| 790 | 06 | 64 | a5_04 | 1678 | 74 | 44 | a8_05 |
| 798 | 44 | 86 | a5_04 | 1763 | 06 | 84 | a8_08 |
| 832 | 11 | 76 | a5_06 | 1802 | 64 | 84 | a8_10 |
| 870 | 87 | 89 | a5_07 | 877 | 16 | 86 | a5_08 |
| 891 | 06 | 76 | a5_08 | 950 | 01 | 86 | a6_00 |

Follower standing tiers: prom/gt-value (excluded from survey): 84=on×7, 87=ce×1, 64=qui×1, 06=ent×1, 11=la×1, 82=m×2 → 13 windows. Unresolved-value set (OPEN + lead + class tier): **31 windows**. Strict-open subset (no registry entry at all): 12 windows (@87, @207, @453, @516, @721, @744, @1216, @1240, @1306, @1401, @1598, @1678).

## C2 — the mechanism test (0 demonstrable legs)

The mechanism requires: left "...X le." a complete clause (X a finite transitive verb taking clitic "le") AND right "Y ..." a complete clause. Tested every window of the 31-window unresolved set with ±6 context. Results by best candidate:

- @87 (`...14 06 88 | 77 66 | 98 19 41 98 81`, a1_02): X=88 (gov cls, not shown finite); left subjectless; right Y=66 open with no nameable role. Not demonstrable.
- @207 (`...42 06 | 77 44 | 50 88 19 74 77`, a2_00): X=06='ent'; left "…42 06 77" — 06 as finite ending would strand "le" after a finite verb with no object role available; 42 open. Not demonstrable.
- @453 (`...79 17 | 77 60 | 65 13 66 14 02`, a2_10): X=17='fois'; "...tout fois le" — no verb on the left. Not demonstrable.
- @516 (`...56 87 | 77 80 | 09 70 91 77 06`, a3_00): X=87='ce'; "ce le" cannot close a clause. Not demonstrable.
- @721 (`...21 80 | 77 03 | 91 65 64 11 00`, a5_02): X=80 open; "[21-noun] 80 le" — no verb. Not demonstrable.
- @744, @1240, @1401, @1598 (`...67 | 77 81 | ...`): X=67 → "et" by the §7 positional rule (follower 77 not infinitive-shaped); "et le" cannot close a clause. Not demonstrable (×4).
- @1216 (`...45 36 | 77 83 | 92 61 24 48 30`, a7_00): X=36 (noun cls); "…[36-noun] le" — no verb. Not demonstrable.
- @1306 (`...21 43 | 77 74 | 52 30 92 44 00`, a7_04): X=43 open; "[21-noun] 43 le" — no verb. Not demonstrable.
- @1678 (`...39 74 | 77 44 | 00 46 79 65 13`, a8_05): X=74 open; no verb. Not demonstrable.
- Best verb-X lead windows: @1133 (`...86 37 86 24 | 77 86 | 20 62 98 00 98`): left "…[24-verb-cls] le" lacks a subject (24's finiteness and transitivity unshown); right "86 [INF] …" cannot open a complete clause (bare infinitive-class group needs a governor). Not demonstrable. @647 (`...61 88 | 77 78 | 52 82 94 76 49`), @1542 (`...93 88 | 77 78 | 43 00 46 70 12`): 88 gov-cls not shown finite; right side "78 52…"/"78 43…" not a complete clause. Not demonstrable. @677, @1180 (X=37 open), @430 (X=63 open), @968 (`...19 24 06 | 77 76 | 01 98 48 51 45`): right "[76-noun-lead] [01] [98-fin]" is a fragment, not a complete clause. Not demonstrable.

Structural reason the count is zero: the left side fails in every window (X is never a standing-grade finite transitive verb in position to take clitic "le" as its complete object — X ∈ {06, 17, 87, 80, 67, 36, 43, 74, 37, 63, 88, 24, ...} supplies no complete "...V le." under standing values), and the right side is systematically unnameable because Y is open-valued by the survey's own definition.

**C2: FAIL — 0/31 windows demonstrate the mechanism. The bar's negative arm fires: survey negative.**

## Adverse answered

"77='le' provisional only" — the survey was run *granting* provisional 77='le'. The zero result is robust in the granting direction: even with 77 as an article, no precedent exists. If 77 resolves non-'le', the question is moot and the mechanism retires with it. Stated as caveat, not hidden.

## Verdict: KILL

The claim "a clause boundary after an article IS a precedented lane mechanism for 'X 77 [open-value]' adjacencies" is false at battery grade: exhaustive census (31 unresolved-value windows, 12 strictly open) finds zero demonstrable legs. Per the evidence field's own framing, the mechanism is retired: future (b)-path "clause boundary after the article" rescues (e.g. fence-83-1217's) have no lane precedent and must bring their own byte evidence. Kills the claim only; no standing verdict contradicted or downgraded; §7 intact. R5005, sealed gates, red-team queue untouched; `canonical.py` never used.

## Standing-state check

- No red-team verdict on 77, clause boundaries, or this mechanism exists; nothing contradicted or downgraded.
- fence-83-1217's (b)-path remains as previously recorded (null/fence, 2026-10-08) — this battery retires its mechanism's standing, it does not re-litigate that battery's window.

## Bookkeeping

- Lock `locks/clause-boundary-precedent.lock` created on start, deleted on completion.
- `battery-queue.json`: `clause-boundary-precedent` → `status: verdict`, `verdict: {result: kill, report: code/crowd17/report_inbox/battery-clause-boundary-precedent.md, date: 2026-10-09}` (temp-file + rename, pre-write assert confirmed queued/verdictless, JSON re-validated).
