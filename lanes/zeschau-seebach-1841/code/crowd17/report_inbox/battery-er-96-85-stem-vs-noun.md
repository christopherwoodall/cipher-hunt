# Battery report: er-96-85-stem-vs-noun

- Target id: `er-96-85-stem-vs-noun`
- Claim: Narrower discrimination arm for the rerun: verb stem -> test stem-composition first ("que" + stem fit); noun -> check the @96 window for a determiner slot between 46 ("que") and 29.
- Date: 2026-10-09
- Worker: battery worker (subagent f54677cc-67e8-4f64-a8cc-346ba0a1cb1b)
- Stream: the repaired 1,847-pair / 96-type parse was re-derived in-session
  (`repair_parse.py` load_rows + parse with `repaired_offsets.json`); asserts
  held (1,847 pairs, 96 types). `canonical.py` never used. R5005, sealed
  gates, red-team adjudication queue untouched.
- Lock note: no lockfile existed at start (no stale lock). Created
  `code/crowd17/next-token/locks/er-96-85-stem-vs-noun.lock`
  2026-10-09T21:04:13Z; deleted on completion.

## Bar (verbatim, pre-registered before testing)

"One of the two arms dead at battery grade on the @96 window with the named value (missing article kills the noun arm before composition)"

Numbered pass/fail clauses (restated before testing, not modified after):

1. **C1:** 85's value is named by a standing verdict or registry cell
   (precondition — the bar's "with the named value" arm).
2. **C2:** With the named value, the @96 window is tested as verb-stem
   composition ("que" + stem fit) OR as the noun arm ("qu'erreur"), and
3. **C3:** one of the two arms is dead at battery grade on that window.

## Precondition check (the battery does not fire)

85's value is NOT named anywhere in the standing records (checked
2026-10-09T21:05Z):

- `code/table-grid/table-registry.json`: the `85` cell is **null** — no value
  cell exists.
- Queue scan of all `status: verdict` / `result: promote` targets: none names
  an 85 value (regex scan of all inbox reports for `85='<value>'` in PROMOTE
  reports: zero hits).
- The 85 promotes on record are frame/class-level only and explicitly name no
  value: `en85-gerund-reaudit` ("no value named for 85"),
  `neque-tail-24-85-clause` ("no value named for 85 or 27"),
  `contredire-85-33-vehicle` (evidence only), `gate-satisfiability-16-85`,
  `qui32e-855-reseg`, `class-37-06-185`, `er85-word-census` (census PROMOTE,
  zero composition under standing values, no value named).
- BATTERY-PROTOCOL.md §7: "85 verb-stem (A3)" is frames-granted, value open.
- 85-value-naming work is live but unresolved: `rival-85-stems`,
  `compound-85-33-scheme`, `en85-successor-constraint`,
  `stem-85-then-1700-rerun-gated`, `compound85-locus-reread` all still
  `status: queued`; `laisser-85-15window`, `val-85-narrow`,
  `stem-85-value-rerun` returned NULL. The parent's own re-arm,
  `er-96-85-value-rerun`, is queued (not fired).

The hook triage for this dispatch round classified this target as
battery-grade conditional test logic, not a hard gate, with the instruction:
"Workers must evaluate the dependency in the bar and fence if unmet." The
dependency is unmet: the bar's "with the named value" precondition fails.

## Window facts recorded for the rerun (value-independent, no test run)

Re-derived on the repaired stream (0-based): row a1_02,
`@95=46 @96=29 @97=85 @98=08 @99=21 @100=62`
("que" "er" [85] [08] [21] [62]). The parent report's "@96 window" is the
"46 29 85" contact: **46 is immediately followed by 29 — there is no pair
between them, so no determiner slot exists at the window under any reading.**
This is the "missing article" fact the noun arm's kill would rest on, recorded
here as window geometry, not as a verdict: the noun arm is conditional on 85's
value being a noun, which is undecided, so the arm cannot be killed yet.

## Per-clause results

- **C1 — FAIL (unmet precondition, stated cause).** No standing verdict or
  registry cell names 85's value. 85 is frame-granted (A3 verb-stem), value open.
- **C2 — UNTESTABLE.** Cannot test stem-composition without the stem's
  letters; cannot test the "qu'erreur" noun arm without the noun.
- **C3 — UNTESTABLE.** No arm can be killed at battery grade without the named
  value: the noun arm's kill is conditional on 85 being a noun (undecided).

No adverses were listed for this target (adverses: ""). None to answer.
No standing or red-team verdict contradicted, downgraded, or re-litigated;
§7 intact.

## Verdict: NULL — unmet precondition (fence)

**Headline:** the bar is untestable as written — its own "with the named
value" precondition is unmet, so the discrimination battery did not fire. The
target is fenced, not abandoned: it re-arms the moment a standing verdict
names 85's value. The @96 window geometry (no determiner slot between 46 and
29) is banked for the rerun.

## Follow-ups proposed (verified ABSENT from battery-queue.json on 2026-10-09T21:06Z)

1. `er-96-85-stem-vs-noun-rerun` (P3) — re-arm of THIS narrower
   discrimination battery once 85's value is named. Gate: fire only when 85's
   registry cell is non-null or a standing battery verdict names 85's value
   (watch the queued 85-value candidates: rival-85-stems,
   compound-85-33-scheme, en85-successor-constraint,
   stem-85-then-1700-rerun-gated, compound85-locus-reread). Bar: on the @96
   window (0-based @95=46 "que", @96=29 "er", @97=85, row a1_02) with the
   named value: if the value is a verb stem, test "que"+stem composition fit;
   if the value is a noun, the "qu'erreur" arm needs a determiner between 46
   and 29 — the rerun may adopt this report's window fact (46 immediately
   precedes 29; no determiner slot) to kill the noun arm before composition.
   Bar: one of the two arms dead at battery grade on the @96 window with the
   named value. (Not a duplicate of the queued `er-96-85-value-rerun`: that
   re-arms the parent's broader C1–C4 bar; this one carries the narrower
   determiner-slot discrimination and the banked window geometry.)

## Bookkeeping

- Queue: `er-96-85-stem-vs-noun` → `status: verdict`, `result: null`,
  report path, 2026-10-09 (pre-write assert: was queued/verdictless;
  target-id-unique temp file `battery-queue.json.er-96-85-stem-vs-noun.tmp`
  + atomic rename; only this target's entry touched; no downgrade).
- Lock `er-96-85-stem-vs-noun.lock` deleted on completion.
