# Battery report: val-03-noun

Worker: 700eb03c-3a71-40a5-9d48-87ffc75e3be7. Date: 2026-10-09.
Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` +
`data/upstream-ct_R5005.txt`), parsed per `code/side-keyhunt/repair_parse.py`.
`canonical.py` never used. R5005, sealed gates, red-team adjudication queue untouched.
`@i` = 0-based pair index. Asserts held: 1,847 pairs, 96 types.

## Bar (verbatim, pre-registered before testing)

"Kill any candidate lexeme that fails to parse any of the forced-nominal windows @336, @674, @1645, @1014, @1790, @722."

Numbered clauses:
- C1 — enumerate the standing candidate-lexeme inventory for noun-03.
- C2 — test each candidate against all six forced-nominal windows; kill any candidate that fails to parse ≥1 window.
- C3 — if ≥1 candidate survives all six windows, name 03's noun value.

## Method

1. Re-derived the repaired stream in-session; byte-confirmed all six windows with ±6 context.
2. Swept all battery/red-team reports for any proposed 03 lexeme (`03 = "..."` patterns).
3. Tested each inventoried candidate against the six windows under standing values (§7).

## Findings

### C1 — candidate inventory: singleton, already dead

Exhaustive sweep of `code/crowd17/report_inbox/` (processed + inbox) for proposed
03 lexemes finds exactly one ever-proposed value:

- **"re-"** (bound prefix) — proposed in `battery-re-prefix-03-665`,
  **KILLED at kill grade** (three independent families: "03 29"="reer" nonexistent;
  "pas re" ungrammatical; "re-qui" morphologically impossible). It was never a
  noun candidate.

The two other regex hits ("03='39'", "03 = 'on est'") are false positives —
`@503='39'` offset notation and `'on est' x4` bigram counts, not 03 values.

R19-180 (stem-03-nounfamily, GRANT finding grade) states explicitly:
"No specific noun value is named — the bar asked for convergence on a noun/word
*reading*, not a lexeme. Naming the noun value is follow-up 1."
This battery IS that follow-up; the parent assumed candidates would exist. None do.

No letter content for 03 exists anywhere at battery grade (full 20-window contact
census re-derived: no GT-letter adjacency constrains 03's letters; @1237
"[10] [03]e" is the only letter-adjacent window and its 03 is outside both the
"03 29" stem scope and the nominal set — §7 split venue, not battery material).
Without letters, no new lexeme candidates can be generated without inventing.

### C2 — the sole candidate fails all six windows at kill grade

Test "re-" as noun-03 at each window (bound prefix as noun = morphological
impossibility, value-independent):

| window | frame (standing values) | "re-" test |
|---|---|---|
| @336 (a2_05) | `88 40 [03] 64` = "…e [03-N] qui…" | "re qui" impossible — prefix cannot head a relative clause. KILL |
| @674 (a5_00) | `80 [03] 64 37` = "[80] [03-N] qui [37-pred]" | same. KILL |
| @1645 (a8_04) | `60 [03] 64` = "[60] [03-N] qui" | same. KILL |
| @1014 (a6_02) | `47 [03] 24` = "ce [03-N] en" | "ce re en" not French; prefix cannot follow a determiner. KILL |
| @1790 (a8_09) | `47 [03] 00` = "ce [03-N] pour" | "ce re pour" not French. KILL |
| @722 (a5_02) | `77 [03] 91` = "le [03-N] [91]" | "le re" not French. KILL |

6/6 kill-grade failures. (Confirms, does not newly establish, re-prefix-03-665.)

### C3 — no value named

Zero candidates survive; the inventory is exhausted. No noun value for 03 can be
named at battery grade.

## Verdict: NULL

The failure is epistemic, not substantive: the candidate inventory is empty, so
the bar's kill arm fires on the singleton historical candidate and C3 cannot
proceed. This is NOT a proof that noun-03 has no value — the six windows remain
noun-compatible (R19-180 stands), and the 03/71 §7 split stays red-team venue
(R20 DEFER). Per §4, a null regenerates work; follow-ups below.

No standing/red-team verdict contradicted or downgraded; §7 intact.
Canonical-stream caveat stands.

## Follow-ups proposed (all verified ABSENT from battery-queue.json)

1. `val-03-letter-probe` (P3) — establish 03's letter content: probe @1237
   "[10] [03]e", the "40 03" junctions (@336/@599, word-internal vs boundary),
   and any other letter-adjacent 03 windows. Letter inventory is the prerequisite
   for generating lexeme candidates at battery grade.
2. `noun-03-gender-test` (P3) — test gender uniformity of noun-03: @722
   "le [03]" (77="le" provisional, masculine) vs "ce [03]" x2 @1014/@1790
   (47="ce" granted, epicene). A masculine-uniform result restricts the future
   candidate space to masculine nouns; a failure re-opens the uniformity
   assumption itself.
3. `noun-03-frame-extend` (P4) — fold the remaining noun-compatible 03 windows
   ("60 03 39" x3 @691/@1675, "pas [03]" x3 @31/@657/@994, "[03] 39" @599)
   into the noun-03 frame inventory; more frames tighten future candidate
   constraints once letters exist.

## Bookkeeping

- Lock `code/crowd17/next-token/locks/val-03-noun.lock` created on start
  (2026-10-09T15:40:28Z, no stale lock), deleted on completion.
- Queue: `val-03-noun` → `status: verdict`, `result: null` (pre-write assert
  passed — was queued/verdictless; temp-file + rename; own entry only; no downgrade).
- R5005, sealed gates, red-team adjudication queue untouched.
