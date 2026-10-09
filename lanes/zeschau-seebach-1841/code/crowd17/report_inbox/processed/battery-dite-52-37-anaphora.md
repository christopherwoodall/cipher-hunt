# Battery report: dite-52-37-anaphora (KILL — "dite" eliminated from the Type-A set)

**Target:** dite-52-37-anaphora — anaphora test: only "dite" (=ladite) requires an antecedent
**Worker:** 6b34c8ae-6ce9-481f-a36c-a2f0ba175b4d | **Date:** 2026-10-09
**Stream:** repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json + data/upstream-ct_R5005.txt, parsed per code/side-keyhunt/repair_parse.py). Never canonical.py. No R5005 touched. No data invented. Every @-offset re-derived from the stream.

## Bar (verbatim from battery-queue.json)

> check rows a6_07/a8_07 upstream of the @1124/@1722 windows for an antecedent; "dite" survives iff an antecedent exists

## Bar as numbered clauses (pre-registered before testing)

1. The upstream portion of row a6_07 (all pairs before the @1122 "06-11-52-37-43" 5-gram) is searched for an antecedent — a prior 43-token or its resolvent in the bar's scope.
2. The upstream portion of row a8_07 (all pairs before the @1720 "06-11-52-37-43" 5-gram) is searched for an antecedent.
3. "dite" survives iff an antecedent exists in the searched scope.

## Method

1. Reparsed the repaired stream byte-exactly per repair_parse.py (1,847 pairs; asserts hold).
2. Located the Type-A windows: @1124 (52) on row a6_07 (pairs 1113–1132), 5-gram "06-11-52-37-43" at @1122; @1722 (52) on row a8_07 (pairs 1719–1744), 5-gram at @1720.
3. Dumped the in-row upstream portions: a6_07 pairs 1113–1121; a8_07 pair 1719.
4. Ran the full-stream 43 census for the documented scope caveat (§"Scope-dependence caveat").

## Window-level evidence

**Row a6_07, upstream of @1122 (clause 1):**
- Pairs 1113–1121: `38 30 69 11 88 70 12 06 14` — **zero 43-tokens**.
- Row a6_07's only 43 is @1126, the window's own head noun. A noun cannot be its own anaphoric antecedent.
- Result: **no antecedent in scope.**

**Row a8_07, upstream of @1720 (clause 2):**
- Pair 1719: `68` — **zero 43-tokens** (a single pair precedes the window in this row).
- Row a8_07's only 43 is @1724, the window's own head noun — again, not a valid antecedent.
- Result: **no antecedent in scope.**

## Per-clause pass/fail

1. a6_07 upstream search — **FAIL (no antecedent).** 9 upstream pairs, no 43-token.
2. a8_07 upstream search — **FAIL (no antecedent).** 1 upstream pair, no 43-token.
3. "dite" survives — **FAIL.** The bar's survival condition ("iff an antecedent exists") is not met at either window.

## Scope-dependence caveat (documented, not verdict-driving)

The bar names rows a6_07/a8_07 as the search scope, and the verdict above follows that scope. Under a **whole-discourse** reading (entire stream upstream of each window), antecedents DO exist:
- Upstream of @1124: 10 prior 43-tokens (nearest @1092 in row a6_06, 30 pairs back: `…79 80 06 [43] 07 55 81 06…`).
- Upstream of @1722: 15 prior 43-tokens (nearest @1544 in row a8_00, 178 pairs back: `…88 77 78 [43] 00 46 70 12…`).

If the supervisor intended whole-discourse scope rather than row scope, this test does **not** eliminate "dite" — re-scope and re-run. The verdict below is for the bar as written.

## Kill-grade check

Kill grade met: the bar's survival condition fails decisively at both windows under the stated scope. "Dite" (= ladite, "the aforementioned") is the only one of {même, seule, dite} that requires an antecedent (même/seule do not — adj-52-37-value battery, 2026-10-08), and none exists where the bar looks. "Dite" is eliminated from the Type-A 52-37 candidate set. {même, seule} remain tied; that tie is owned by adj-52-37-value-rerun (gated on noun-43).

## Adverses answered

- **"37's sub-lexical value owned by S5/s5-foundation — do not decide 37":** honored. 37 untouched throughout; only the 52-37 unit's adjective candidacy was adjudicated. The S5 fence (round-7, 37="le" MEDIUM) was not litigated, not contradicted, not overturned.
- **"Resolvent" reading of antecedent:** fenced, not ignored. No other group has a granted value that could resolve to the 43-noun at battery grade: 87="ce" and 47="ce" are demonstratives, and French "ladite X" requires the noun X itself to have been previously mentioned — a bare demonstrative does not license it. The byte-grounded antecedent test is therefore prior 43-tokens, which is what was searched.
- **43's value open (condition vs mesure):** accepted as stated — the test is a 43-token identity test and holds under either survivor.
- **Red-team conflict check:** no standing red-team verdict touches dite/même/seule for 52-37. No existing verdict downgraded (this target had none).

## Verdict

**KILL** — "dite" is eliminated from the Type-A 52-37 adjective candidate set. No antecedent exists in either named row upstream of the @1124/@1722 windows, so "dite" (=ladite) fails the bar's survival condition. Surviving candidates: {même, seule} (tie stands, owned by adj-52-37-value-rerun pending noun-43).

---
Lock: locks/dite-52-37-anaphora.lock created 2026-10-09T02:59:37Z, deleted on completion of this report. No R5005 touched. No sealed gates touched. No red-team verdicts modified.
