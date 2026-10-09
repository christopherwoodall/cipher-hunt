# Battery report: val-65-1204-rightedge

- Target: `val-65-1204-rightedge`
- Claim: name 65's value at the @1204 window (21->65 x4 contact); constrains 'ce [43] [55] [61] [21] [65]' from the right edge
- Date: 2026-10-09
- Worker: battery worker val-65-1204-rightedge (subagent 94227e1c-ac93-4016-bf3c-457aea0a8cac)
- Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py` — 1,847 pairs / 96 types asserted in-session). `canonical.py` never used. R5005, sealed gate instances, red-team adjudication queue untouched. No data invented. @-offsets are 0-based stream indices.
- Lock: `code/crowd17/next-token/locks/val-65-1204-rightedge.lock` created 2026-10-09T10:16:19Z, deleted on completion. No prior lock existed.

## Bar (verbatim from battery-queue.json)

"name 65 iff one value covers the @1204 right edge with <=1 non-granted assumption; coordinate with the 65-gender docket; do not re-litigate promoted verdicts"

Numbered pass/fail clauses (pre-registered before testing, frozen):

1. **C1 (naming):** One French lexical value is named for 65.
2. **C2 (coverage):** That value makes the @1204 right-edge window (@1203–@1208: `47 43 55 61 21 65`) parse grammatically under standing values.
3. **C3 (assumption budget):** The C2 parse uses <=1 non-granted assumption in total.
4. **C4 (gender-docket coordination):** The naming does not assume or re-decide 65's gender; coordinates with the 65-gender docket (`det-65-gender-adjudicate` NULL adopted; `gender-65-independent` remains queued).
5. **C5 (no re-litigation):** No promoted verdict is re-litigated — `prof-65` (65=noun), `bound-65-64-qui` (@1208 qui-relative on 65, no clause boundary), `noun-43-1205-window` (43's value fenced) are adopted as premises.

## Method

- Read BATTERY-PROTOCOL.md first. Re-derived the repaired stream in-session; asserts held (1,847 pairs, 96 types).
- Pulled the @1204 window ±14 and re-derived the byte sequence directly (not copied from prior reports).
- Adopted standing verdicts as premises: prof-65 PROMOTE (65=noun, battery-grade), bound-65-64-qui PROMOTE (@1208: qui-relative "65, qui est [32]-e" under provisional 59='est'; boundary REJECTED), noun-43-1205-window NULL (43's candidate set exhausted at battery grade; the @1204 window's 43-question fenced), noun-65-value NULL (full 25-window constraint set leaves an open lexical class — input evidence, not re-run), det-65-gender-adjudicate NULL (gender unadjudicated, both legs conditional).
- Standing values used: banked GT (11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que); granted (87/47=ce, 64=qui, 96=par, 17=fois, 79=tout, 00=pour, 84=on); provisional (59=est, 77=le). Constituents 43/45/55/58/61 value-open; 21=noun class (battery-promoted).

## Window-level evidence (re-derived)

- Chain @1200–@1208: `29 45 58 47 43 55 61 21 65` (row a7_00; row offsets for a7_00/a6_10 unvalidated — canonicality caveat stands per §7).
- Flanks: @1199=64 (qui), @1209=64 (qui), @1210=59, @1211=32, @1212=48.
- Under standing values: `qui [29]er [45] [58] ce [43] [55] [61] [21-noun] [65-noun], qui est [32]-e …` — the @1203–@1208 locus is "ce [43] [55] [61] [21] [65]" with five value-open constituents (43 fenced by noun-43-1205-window; 55/61/21/65 value-open, 21 and 65 noun-class).
- `21->65` x4 (@134/@371/@1207/@1529) and `65->64` x3 (@724/@1208/@1340): byte-exact, matching prof-65 and bound-65-64-qui. No determiner directly precedes 65 at @1207 (bare-NP distribution holds here too; 21 is noun-class, not a licensed determiner — val-21-reopen KILL).
- Lexical discrimination attempt: the full constraint set on 65 (masculine-leaning bare-NP noun, subject of negated/copula verbs, head of qui/que relatives, verb object, "21"-compounds, the @1204 "21 65 qui est 32e" parse) is satisfied by an open class of French nouns (homme, peuple, roi, temps, bruit, … — the noun-65-value battery's field). No frame selects among candidates; no window at @1204 forces any specific value false.
- The @1204-specific material beyond noun-65-value's two grounding frames is the `47=ce [43] [55] [61]` span — whose constituents are value-open and whose only standing characterization is the noun-43-1205-window fence. It adds syntactic shape, not lexical selection.

## Per-clause pass/fail

1. **C1: FAIL.** No single value discriminates: the @1204 window's five open constituents admit an open class of French nouns; nothing selects one (the noun-65-value NULL's finding is corroborated at this locus).
2. **C2: MOOT.** No candidate value exists to test coverage on.
3. **C3: FAIL in principle.** Any naming needs >=2 non-granted assumptions: (a) 65's gender (unadjudicated at battery grade — det-65-gender-adjudicate NULL, both legs conditional), and (b) lexical selection from the open class. Two non-granted assumptions exceed the <=1 budget. This failure is structural, not an artifact of this worker's search.
4. **C4: PASS.** No gender assumed anywhere in this verdict; the gender question is left entirely to the queued `gender-65-independent` probe and the standing det-65-gender-adjudicate NULL.
5. **C5: PASS.** Nothing re-litigated: prof-65, bound-65-64-qui, noun-43-1205-window, noun-65-value, det-65-gender-adjudicate all adopted as premises; no standing verdict contradicted or downgraded.

## Adverses answered

- "coordinate with gender-65-independent (queued)": ANSWERED — this verdict uses zero gender assumptions and proposes a gated follow-up (F1) that runs only after the queued probe adjudicates, so no pre-emption and no duplicated work.

## Verdict: NULL

Headline: the naming bar is unsatisfiable at battery grade — the @1204 right edge admits an open class of French nouns (no frame selects, no window forces a specific value false), and any naming would need >=2 non-granted assumptions (gender + lexical selection) against a budget of 1. This is null grade, not kill: a kill would require showing no value could cover the window, which is unprovable with five value-open constituents. No red-team verdict contradicted; no battery verdict downgraded. The §7 gender polyvalence rule is untouched.

## Follow-up targets (null per §4 — all ids verified absent from battery-queue.json 2026-10-09)

1. **val-65-1204-rerun-gender** (P3) — re-run this exact naming bar at @1204 once `gender-65-independent` adjudicates 65's gender: a gender verdict supplies the currently-missing non-granted assumption, halves the lexical field, and removes the structural C3 block. Gated: do not run before the gender ruling. Bars: "name 65 iff one value covers the @1203–@1208 window under standing values plus the adjudicated gender, with <=1 further non-granted assumption." Coordinate with the 65-gender docket; do not re-litigate.
2. **val-65-32-constraint** (P3) — once the red team resolves 32's duality and names 32's value, re-test 65's value via the @1208 "65 qui est [32]" predicative: a named predicative 32 semantically selects among 65's candidates ("65, qui est [32]" narrows the open class). Gated on the red-team 32-duality ruling. Do not re-declare 32's duality at battery level.
3. **val-65-21-unit** (P4) — test whether "21 65" x4 (@134/@371/@1207/@1529) is a fixed lexical unit (compound/appositive): if the unit is lexicalized, 65's value can be approached via the unit's distribution and 21's value once 21's value search re-opens. Coordinate with queued `reopen-21-65-ratified`; do not force a value on either member. Bars: "decide unit-vs-compositional for '21 65' iff the four windows share a distributional signature (shared follower class or formula-bound context) at battery grade; else fence."

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-val-65-1204-rightedge.md` (this file)
- Queue: `val-65-1204-rightedge` → status `verdict`, result `null`, date 2026-10-09 (pre-write assert: queued/verdictless; temp-file + rename; JSON re-validated; own entry only; no downgrade)
- Lock deleted on completion.
