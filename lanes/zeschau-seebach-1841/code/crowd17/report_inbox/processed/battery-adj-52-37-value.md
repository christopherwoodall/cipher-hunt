# Battery report: adj-52-37-value (NULL — three-way tie unbroken)

**Target:** adj-52-37-value — the Type-A 52-37 adjective is named (même vs seule vs dite discriminated)
**Worker:** b631bb67-9881-4673-b441-2733dda648a1 | **Date:** 2026-10-08
**Stream:** repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json + data/upstream-ct_R5005.txt, parsed per code/side-keyhunt/repair_parse.py). Never canonical.py. No R5005 touched. No data invented. Every @-offset re-derived from the stream.

## Bar (verbatim from battery-queue.json)

> decide among {même, seule, dite} using 43's resolved noun value and wider prenominal-adjective frames; name iff one candidate parses both @1124/@1722 with <=1 ungranted assumption

## Bar as numbered clauses (pre-registered before testing)

1. 43's resolved noun value is available for the decision (or exactly one stated assumption about 43 stands in for it, within the ≤1 budget).
2. Wider prenominal-adjective frames for the 52-37 unit (or 37) are examined for discriminating power among the three candidates.
3. Exactly one of {même, seule, dite} parses both @1124 and @1722 with ≤1 ungranted assumption while the other two fail under the same budget — that candidate is named.

## Method

1. Reparsed the repaired stream byte-exactly per repair_parse.py (1,847 pairs, 96 unique; asserts hold).
2. Re-derived the 52-37 bigram census: x4 at @1124, @1129, @1356, @1722 (@-offsets index the 52; the la-523743 battery indexes the preceding 11 at @1123/@1721 — same windows). Re-derived "11-52-37-43" 4-gram at @1123/@1721 and the byte-identical 5-gram "06-11-52-37-43" at @1122/@1720.
3. Adopted as verified (not re-litigated): Type-A parse "[verb-ent] la [52-37-adj-unit] [43-head-noun]" (la-523743-adjective battery, 2026-10-08); 43 = feminine head noun narrowed to {condition, mesure} (frame-43 battery, 2026-10-08; "suite"/"maniere" killed by the "pour [INF]" frame); unit-52-37-name battery (2026-10-08) split candidacy (Type A adjectival vs Types B/C) referred to red team.
4. Tested each candidate {même, seule, dite} at both Type-A windows under each 43 survivor, counting ungranted assumptions. Standing values used: 11=la, 00=pour, 06=ent, 64=qui (banked/granted/promoted); 43 ∈ {condition, mesure} per frame-43 battery (value itself open — used as the one allowed assumption).
5. Scanned for wider prenominal-adjective frames: all 52-37 windows, all 37-prenominal windows, and the 37 census from the la-523743 battery.

## Window-level evidence

**Type-A windows (re-derived):**
- @1124 [a6_07]: `… 06 11 [52 37] 43 00 86 52 37 86 …` → "…ent la [52-37] [43] pour [86-INF] …"
- @1722 [a8_07]: `… 06 11 [52 37] 43 98 39 88 24 …` → "…ent la [52-37] [43] [98] a/a [88] …"

**Candidate test matrix (1 ungranted assumption per row: 43 = the stated survivor):**

| candidate | @1124, 43=condition | @1124, 43=mesure | @1722, 43=condition | @1722, 43=mesure |
|---|---|---|---|---|
| même | "la même condition pour [inf]" ✓ | "la même mesure pour [inf]" ✓ | "la même condition [98] a" ✓ | "la même mesure [98] a" ✓ |
| seule | "la seule condition pour [inf]" ✓ | "la seule mesure pour [inf]" ✓ | "la seule condition [98] a" ✓ | "la seule mesure [98] a" ✓ |
| dite | "la dite condition pour [inf]" (= ladite) ✓ | "la dite mesure pour [inf]" ✓ | "la dite condition [98] a" ✓ | "la dite mesure [98] a" ✓ |

All three candidates parse both windows under both 43 survivors. Grammaticality does not discriminate: "même"/"seule"/"dite" all collocate naturally with "condition" and "mesure" in the "la [X] [N] pour [INF]" frame, and continuation B ("43-98-39") is compatible with all three under the open-98 copula-like reading ("la [X] mesure/condition est à [inf]"). The two Type-A tokens are byte-identical in the 5-gram — zero distributional variance between @1124 and @1722, so no within-pair discrimination is possible.

**Wider prenominal-adjective frames (clause 2):**
- 52-37 occurs x4 stream-wide (@1124, @1129, @1356, @1722). Only the two Type-A windows are prenominal-adjective. Type B @1129 ("43 pour 86 [52-37] 86 24 …") admits no adjectival parse under any candidate ("pour [inf] même/seule/dite [inf]" all ungrammatical; determiner-life 86 no better). Type C @1356 ("…06 [52-37] 64 35…") places the unit as bare antecedent of "qui" — "même/seule/dite qui" ungrammatical without a determiner for all three. Per the unit-52-37-name battery, Types B/C are split-candidacy for the red team, not adjective frames.
- 37 alone prenominal: @385 "52-38-37-43" (37 directly before the 43-noun) is the only candidate, but 38's class is fully open (n=7) — queued as adj-37-385-gate by the la battery; not decidable at battery grade.
- The la-523743 battery's full 37 census (n=28, 2026-10-08) found zero other adjective-slot confirmations: "qui 37" @676 and "23-37-06" @183 pull verb-shaped; the rest are undeterminable or S5-straining.
- Net: no wider frame discriminates among {même, seule, dite}.

**Assumption accounting:** the decision used exactly 1 ungranted assumption (43 = condition, resp. mesure — the frame-43 battery's two survivors; 43's value is open, noun-43 still queued priority 4). The tie holds under both survivors, so the assumption choice does not affect the outcome.

## Per-clause pass/fail

1. **43's resolved noun value — NOT AVAILABLE (fenced, not forced).** noun-43 is still queued (priority 4); frame-43 battery narrowed 43 to {condition, mesure} but named nothing. Proceeded under the bar's ≤1-assumption budget with one stated assumption (43 = condition / mesure, tested separately).
2. **Wider prenominal-adjective frames examined — DONE, no discriminating frame.** Only Type-A windows are adjectival; Types B/C admit no candidate; @385 gated on open 38; 37 census has no other adjective slots.
3. **Unique winner among {même, seule, dite} — FAIL (three-way tie).** All three parse both @1124 and @1722 with ≤1 ungranted assumption under either 43 survivor. The bar's "iff" condition is not met: no candidate is forced, and naming one would itself be a second ungranted assumption (a guess), exceeding the budget.

## Kill-grade check

Not kill: no window forces any of the three candidates false, and no distributional test rejects the triple at the lane's standard. The failure is inconclusive (tie under the available tools), not a forced-false — a narrower bar (e.g., the dite-anaphora test below) could still discriminate. No cleaner rival value demonstrated on these frames ("telle" was graded marginal by the unit battery; scoped as follow-up F2).

## Adverses answered

- **"37's sub-lexical value owned by S5/s5-foundation — do not decide 37; name the unit only":** honored. 37 untouched throughout; only the Type-A 52-37 unit's adjective value was tested. The S5 fence (round-7, 37="le" MEDIUM) was not litigated, not contradicted, not overturned.
- **Red-team conflict check:** no standing red-team verdict touches même/seule/dite (grep of code/crowd15/report_inbox/next-token-redteam.md: zero hits). The unit battery's split candidacy and the la battery's S5 escalation are adopted as standing context, not re-decided. No existing verdict downgraded (this target had none).

## Verdict

**NULL.** The bar's two discrimination tools are both unavailable at battery grade: 43's value is unresolved (noun-43 queued; assumption budget spent on the {condition, mesure} survivors, tie under both), and no wider prenominal-adjective frame discriminates. {même, seule, dite} remain a three-way tie at both @1124 and @1722. Work regenerates via the follow-ups below.

## Follow-up targets for the supervisor queue (null regeneration)

**F1. id: "dite-52-37-anaphora" | priority: 2**
claim: "'dite' (= ladite, 'the aforementioned') is confirmed or demoted by an anaphora test at @1124/@1722"
bars: "search rows a6_07 (upstream of @1124) and a8_07 (upstream of @1722) for a prior 43-token or its resolvent in the same document block; name 'dite' iff an antecedent is found at both windows; demote 'dite' to LEAD-minus iff absent at both; else record the split"
evidence: "adj-52-37-value null (2026-10-08): {même, seule, dite} three-way tie on grammaticality; only 'dite' carries an anaphora requirement (même/seule do not), which is the one linguistic asymmetry among the triple"
adverses: "document-block boundaries in the row stream unproven; 43's value still open (noun-43 queued) — antecedent search must accept either survivor"

**F2. id: "telle-52-37-rival" | priority: 3**
claim: "'telle' is admitted to or excluded from the Type-A candidate set"
bars: "test 'telle' at both @1124/@1722 under the same ≤1-assumption bar as adj-52-37-value; admit iff it parses both windows; exclude with stated cause iff it fails either"
evidence: "unit-52-37-name battery (2026-10-08) listed 'telle' as a marginal fourth candidate; adj-52-37-value's bar scoped only {même, seule, dite} — the set's exhaustiveness is unverified"
adverses: "'telle' prenominal = 'such', archaic-leaning; 43's value open"

**F3. id: "adj-52-37-value-rerun" | priority: 2**
claim: "the {même, seule, dite} triple re-tests cleanly once 43's value is named"
bars: "gated on noun-43's verdict: re-run the adj-52-37-value clause-3 matrix under 43's then-resolved value with ZERO ungranted assumptions; name iff a unique winner emerges, else confirm the tie as final at battery grade"
evidence: "adj-52-37-value null (2026-10-08): the bar's primary tool (43's resolved noun value) was unavailable — the one spent assumption may have masked a collocation asymmetry (e.g., 'la seule mesure' vs 'la dite condition' idiom weights)"
adverses: "do not dispatch before noun-43's verdict lands; 37's value stays with S5"

---
Lock: locks/adj-52-37-value.lock created 2026-10-09T02:48:34Z, deleted on completion of this report. No R5005 touched. No sealed gates touched. No promotions made. No red-team verdicts modified.
