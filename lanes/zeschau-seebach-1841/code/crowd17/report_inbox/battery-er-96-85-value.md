# Battery report: er-96-85-value

- Target id: `er-96-85-value`
- Claim: Once 85's value is named, test "qu'er[85]" as "qu'erreur" vs stem-composition.
- Date: 2026-10-09
- Worker: battery worker (subagent 2b804519-590b-4df8-bbad-3c2002c011fe)
- Stream: not touched. The bar's own precondition ("Once 85's value is named") is
  unmet, so the battery did NOT fire — no test ran, no numbers were read, no data
  was invented. R5005, sealed gates, red-team queue untouched.
- Lock note: no lockfile existed at start (no stale lock). Created
  `code/crowd17/next-token/locks/er-96-85-value.lock` 2026-10-09T20:22:59Z; deleted
  on completion.

## Bar (verbatim, pre-registered before testing)

"The A3 verb-stem class predicts the composition arm is dead."

Numbered pass/fail clauses (restated before testing, not modified after):

1. **C1:** 85's value is named (precondition — the claim's "once" arm).
2. **C2:** The @96 window ("que(46)" + "er[85]") is tested as "qu'erreur" with the named value.
3. **C3:** The same window is tested as stem-composition with the named value.
4. **C4:** The A3 verb-stem class prediction ("composition arm is dead") holds or fails at battery grade.

## Precondition check (no test fired)

85's value is NOT named. Evidence:

- BATTERY-PROTOCOL.md §7: "85 verb-stem (A3)" is a frames-granted entry — frame
  granted, value open. 85 is listed nowhere among banked, promoted, or provisional values.
- Parent report battery-er-word-lexicon (2026-10-09, the target's own
  source_report): "85 = verb-stem class A3, value open (no registry cell)."
- 85-related batteries since: stem-85 → NULL; stem-85-value-rerun → NULL;
  val-85-narrow → NULL; val-85-1700-compound → NULL; role-85-postfinite → NULL;
  laisser-85-1699 → KILL (laisse arm dead); en85-gerund-reaudit → PROMOTE but
  explicitly frame-level ("no value named for 85"); neque-tail-24-85-clause →
  PROMOTE with "no value named for 85 or 27"; contredire-85-33-vehicle → PROMOTE
  of the evidence-gathering bar only ("No value named, nothing promoted"). No
  standing verdict anywhere names 85's value.
- Candidate batteries still in flight: rival-85-stems, compound-85-33-scheme,
  en85-successor-constraint, laisser-85-15window, stem-85-then-1700-rerun-gated,
  compound85-locus-reread — all status "queued", none a verdict.

Per §4: the bar is untestable as written — its own precondition is unmet.
This counts as a null. The target is fenced, not abandoned.

## Per-clause results

- **C1 — FAIL (unmet precondition, stated cause).** 85's value is open; no registry
  cell, no standing promote names it.
- **C2 — UNTESTABLE.** Cannot test "qu'erreur" against a value that does not exist.
- **C3 — UNTESTABLE.** Cannot test stem-composition against a value that does not exist.
- **C4 — UNTESTABLE.** The A3 prediction cannot be checked without the value.

No adverses were listed for this target (adverses: null) — none to answer.
No stream data was touched; every statement above traces to standing lane records.
No red-team or standing verdict contradicted or downgraded.

## Verdict: NULL — unmet precondition (fence)

**Headline:** 85's value is not named — the battery's own "once" condition is
unmet, so the test did not fire. This target regenerates work when 85's value
lands; it does not end the line of inquiry. The @96 "qu'erreur" question stays
open and returns with a named 85.

## Follow-ups proposed (both verified ABSENT from battery-queue.json on 2026-10-09T20:22Z)

1. `er-96-85-value-rerun` (P3) — re-arm of this battery once 85's value is named.
   Gate: fire only when a standing verdict (any battery) names 85's value; watch
   the queued 85-value candidates (rival-85-stems, compound-85-33-scheme,
   en85-successor-constraint, laisser-85-15window, stem-85-then-1700-rerun-gated).
   Bar: run C1–C4 verbatim from this report against the named value.
2. `er-96-85-stem-vs-noun` (P3) — narrower discrimination arm for the rerun.
   Once 85's value names: if the value is a verb stem, test stem-composition first
   ("que" + stem fit); if the value is a noun, "qu'erreur" needs a determiner
   between 46 ("que") and 29 — check the @96 window for a determiner slot. The
   missing article kills the noun arm before composition is tried. Bar: one of the
   two arms is dead at battery grade on the @96 window with the named value.

## Bookkeeping

- Queue: `er-96-85-value` → `status: verdict`, `result: null`, report path, 2026-10-09
  (pre-write assert: was queued/verdictless; temp-file
  `battery-queue.json.er-96-85-value.tmp` + atomic rename; only this target's entry touched).
- Lock `er-96-85-value.lock` deleted on completion.
