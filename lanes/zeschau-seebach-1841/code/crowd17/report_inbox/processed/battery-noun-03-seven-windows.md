# Battery report: noun-03-seven-windows

Worker: c1f5e393-b9fc-4079-ab95-8a6f757d8578. Date: 2026-10-09.
Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` +
`data/upstream-ct_R5005.txt`), parsed per `code/side-keyhunt/repair_parse.py`
(upstream byte-exact tokenization, re-derived in-session).
`canonical.py` never used. R5005, sealed gates, red-team adjudication queue untouched.
`@i` = 0-based pair index. Asserts held: 1,847 pairs, 96 types.

## Bar (verbatim, pre-registered before testing)

"name 03's noun value iff one lexeme parses all six with zero kill-grade contradictions; else fence uniform-noun-03"

Numbered clauses (frozen before testing):
- C1 — name arm: one lexeme parses all six forced-nominal windows
  (@336/@674/@1645/@1014/@1790/@722) with zero kill-grade contradictions —
  name 03's noun value.
- C2 — fence arm: otherwise, fence uniform-noun-03 (the claim that one noun
  lexeme covers all six windows).

## Method

1. Read BATTERY-PROTOCOL.md (§1–§8) in full before testing.
2. Re-derived the repaired stream in-session; byte-confirmed all six windows
   contain 03 with ±6 context.
3. Fresh candidate-lexeme inventory: swept `code/crowd17/report_inbox/`
   (inbox + processed) and `code/side-keyhunt/report_inbox/` for any proposed
   03 noun lexeme (`03 = "..."` patterns), including everything filed after
   the val-03-noun sweep.
4. Graded inventory against the six windows under protocol §7 standing values.

## C0 — candidate inventory: still empty

The fresh sweep finds no new 03 noun lexeme proposed anywhere since val-03-noun
(2026-10-09). The only ever-proposed 03 lexeme remains:

- **"re-"** (bound prefix) — proposed in `battery-re-prefix-03-665`,
  **KILLED at kill grade** (three independent families). It was never a noun
  candidate; the kill is standing and is cited, not re-litigated (§7).

No letter content for 03 exists anywhere at battery grade, so no new lexeme
candidate can be generated without inventing (§3 forbids).

## Window-level evidence (@-offsets, standing values)

| window | row | frame (±6) | standing reading |
|---|---|---|---|
| @336 | a2_05 | `92 50 45 54 88 40 [03] 64 31 14 45 64 96` | "e [03] qui" — 40=e (pencil GT), 64=qui (granted). Nominal head of relative. |
| @674 | a5_00 | `20 67 11 86 24 80 [03] 64 37 77 45 23 09` | "[80] [03] qui [37-pred]" — 64=qui granted; 80=A8 verb-frame, 37=A1 predicative. Nominal relative head (R19-180 forced-nominal). |
| @1645 | a8_04 | `35 56 12 33 98 60 [03] 64 31 10 03 38 82` | "[60] [03] qui". Nominal relative head. |
| @1014 | a6_02 | `35 18 79 80 78 47 [03] 24 41 15 66 91 53` | "ce [03]" — 47=ce (granted A4). Determiner + nominal. |
| @1790 | a8_09 | `83 82 96 21 68 47 [03] 00 86 56 42 94 59` | "ce [03] pour" — 47=ce, 00=pour (granted A9). Determiner + nominal. |
| @722 | a5_02 | `86 01 02 21 80 77 [03] 91 65 64 11 00 86` | "le [03]" — 77=le (provisional). Determiner + nominal. |

All six force nominal readings for 03. R19-180 (nounfamily class grant) stands:
the nominal CLASS at these windows is banked; no noun VALUE was ever named.

## Clause results

- **C1: FAIL — untestable, not refuted.** The inventory is empty, so no lexeme
  can be put against the six windows. The name arm cannot fire on zero
  candidates; naming any lexeme would be invention. The "re-" kill is settled
  and is not re-litigated.
- **C2: DOES NOT FIRE.** The fence arm requires evidence that uniformity
  fails at kill grade. No kill-grade contradiction was demonstrated: with zero
  candidates tested, no window forces any uniform-noun claim false, and the six
  windows are themselves noun-compatible (R19-180 stands — they force the
  nominal CLASS, which is consistent with one lexeme and with several).
  Fencing uniform-noun-03 on an empty inventory would be an evidentiary claim
  with no evidence behind it.

## Verdict: NULL

The failure is epistemic, not substantive — identical in structure to
val-03-noun (2026-10-09): the bar's name arm needs a candidate inventory that
does not exist, and the fence arm needs kill-grade evidence that was not
demonstrated. The bar is untestable as written with an empty inventory
(protocol §2: recorded as a finding, counts as null per §4 — the bar is not
silently rewritten). This is NOT a proof that noun-03 has no uniform value,
and it does NOT fence uniform-noun-03; the six windows remain noun-compatible
and R19-180's class grant is untouched.

### Consistency check (protocol §5.2)

No standing red-team verdict is contradicted or downgraded. R19-178's
conditioned verb-stem scope, R19-180's nominal-class grant, the re- kill, and
the deferred 03/71 §7 split all stand. Sibling nulls `val-03-noun` and
`val-03-value-census` (both 2026-10-09) are consistent: none names a 03 value,
none fences uniform-noun-03. §7 intact. Canonical-stream caveat stands.

## Follow-ups proposed (all verified ABSENT from battery-queue.json)

The supervisor already queued val-03-noun's three follow-ups
(`val-03-letter-probe`, `noun-03-gender-test`, `noun-03-frame-extend`); the
targets below are new and do not duplicate them.

1. `noun-03-determiner-census` (P4) — full-stream census of the determiner
   frames licensing noun-03: every "47 03" ("ce [03]") and "77 03" ("le [03]")
   bigram with ±4 context, grouped by row and right-context class. Delivers
   the determiner-frame inventory future noun candidates must satisfy.
   Bar: produce the complete counted inventory with row/offsets; kill any
   claimed noun frame not attested in the stream.
2. `noun-03-qui-frame-census` (P4) — census all "[03] qui" windows (5: @31,
   @336, @674, @1645, @1649) with right-context readings under standing
   values; test whether the nominal-relative-head parse is frame-consistent
   across them. Bar: fence the claim "the nominal-relative parse is coherent
   across all five" iff any window kills it at kill grade; else report the
   coherent frame inventory.
3. `noun-03-context-split-census` (P4) — class census of all 20 03 windows by
   neighbor-frame class (nominal / verbal / other), gather-only. Feeds the
   red-team §7 split docket; a battery decides no split.
   Bar: produce the counted class-split table with window lists; no
   class-uniformity claim is decided.

## Bookkeeping

- Lock `code/crowd17/next-token/locks/noun-03-seven-windows.lock` created on
  start (2026-10-09T16:33:18Z, no stale lock present), deleted on completion.
- Queue: `noun-03-seven-windows` queued → verdict/null (pre-write assert
  passed — was queued/verdictless; temp-file + rename; own entry only;
  no downgrade; no existing verdict overwritten).
- R5005, sealed gates, red-team adjudication queue untouched.
