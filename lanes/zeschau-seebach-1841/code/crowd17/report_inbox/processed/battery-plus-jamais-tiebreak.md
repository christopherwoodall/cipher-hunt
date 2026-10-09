# Battery report: plus-jamais-tiebreak (NULL — tie fenced as unbreakable at battery grade)

**Target:** plus-jamais-tiebreak — "52 = 'plus' vs 'jamais' decided in the ne-frames."
**Worker:** ff218a4e-0156-4f48-af60-ecf74f213ed8 | **Date:** 2026-10-09
**Stream:** repaired 1,847-pair / 96-type parse (code/side-keyhunt/repaired_offsets.json + data/upstream-ct_R5005.txt, parsed per code/side-keyhunt/repair_parse.py; asserts 1847/96 held in-session). Never canonical.py. No R5005 touched. No data invented.
**Offset convention:** lane @ = 0-based stream index.
**Parent:** ne52inf-adverb NULL (2026-10-09); this target is its F1 follow-up.

## Bar (verbatim from battery-queue.json)

"name 52='plus' iff the landed 80/86 infinitive values (poly-80-docket / red-team 86) or 60's value at @1735 (leftedge-60-value) selects 'plus' with zero forced contradiction, else name 'jamais' under the same standard; if neither selects, fence the tie as unbreakable at battery grade"

## Bar as numbered clauses (pre-registered before testing)

1. (C1) The landed 80/86 infinitive values (poly-80-docket / red-team 86) select 'plus' with zero forced contradiction → name 52='plus'.
2. (C2) 60's value at @1735 (leftedge-60-value) selects 'plus' with zero forced contradiction → name 52='plus'.
3. (C3) Else, 'jamais' is selected under the same standard (zero forced contradiction) → name 52='jamais'.
4. (C4) If neither 'plus' nor 'jamais' is selected, fence the tie as unbreakable at battery grade.

Note on C3: "under the same standard" is read as requiring selection — naming 'jamais' by mere default (because 'plus' was not selected) would be an arbitrary coin-flip, violating the lane's forced-not-compatible precedent (stem-03-value) and §5's promote requirements. C3 fires only if something selects 'jamais' with zero forced contradiction.

## Method

1. Re-derived the repaired stream in-session; asserted 1,847 pairs / 96 types.
2. Re-verified the three ne-frame windows on bytes (0-based):
   - W1 @1293–1296 = `94 52 80 04` (row a7_03)
   - W2 @1735–1739 = `60 12 48 52 86` (row a8_07); 52 itself at @1738
   - W3 @1806–1809 = `94 52 80 04` (row a8_10), byte-identical to W1
3. Audited the three premise batteries' current standing in battery-queue.json and the R20 red-team report — did NOT re-litigate their findings, only checked whether their promised values have landed.

## Window-level evidence (@-offsets)

**Premise audit (the bar's selection conditions):**

- **80's value:** poly-80-docket is `status: queued`, `verdict: null` in battery-queue.json — no value has landed. 80's value remains open at red-team venue. (Adverses field confirms: "80 value open (poly-80 red-team)".)
- **86's value:** R20-087 = DUPLICATE / CONFIRM STANDING of R15-A9 GRANT (86 INF-class, class-level); R20 line 100: "values not named" for the {92,33,86} substantivized-infinitive set. No red-team 86 value exists. (Adverses: "86 value open (A9 class grant)".)
- **60's value at @1735:** leftedge-60-value = `status: verdict`, `result: kill` (2026-10-09). Its C1 (name 60) FAILED at null grade: ent-60-verb-arm syllable unnameable, adjective licensed only at the four '21 60' windows, noun killed globally, 'de' killed. No value is nameable for 60 at @1735 under standing values.

**Consequence:** there are no "landed 80/86 infinitive values" and no "60's value at @1735". A non-existent value selects nothing. The bar's selection conditions have no input to operate on.

**Tie status (adopted from ne52inf-adverb, not re-litigated):** {plus, jamais} both parse all three windows with zero ungranted assumptions; no battery-grade discriminator exists in distribution or corpus; both seg-unit dissolution readings (seg-52-80-unit, seg-52-86-unit) returned KILL on 2026-10-09, so the adverb frame stands but the value tie is untouched.

## Per-clause pass/fail

- **C1 (landed 80/86 values select 'plus') — DOES NOT FIRE.** No 80 value landed (poly-80-docket queued); no 86 value landed (R20-087 class-level only). Nothing to select.
- **C2 (60's value at @1735 selects 'plus') — DOES NOT FIRE.** 60 is unnameable at @1735 (leftedge-60-value KILL, naming failed at null grade).
- **C3 ('jamais' selected under the same standard) — DOES NOT FIRE.** No evidence selects 'jamais' over 'plus'; the tie is genuine. Default-naming 'jamais' would be arbitrary, not forced.
- **C4 (neither selects → fence the tie) — FIRES.** Neither 'plus' nor 'jamais' is selected by any landed value. The tie is fenced as unbreakable at battery grade, conditional on the three value venues remaining open.

## Adverses

- "80 value open (poly-80 red-team)" — CONFIRMED still open; honored, not decided here.
- "86 value open (A9 class grant)" — CONFIRMED still open (R20-087); honored.
- "60 value open" — CONFIRMED: unnameable at @1735; honored.
- "section-7 tension with adjective arm still live" — UNTOUCHED; the §7 escalation from ne52inf-adverb stands; no polyvalence declared here.
- 52='pas' stays BLOCKED (not revived): 30='pas' promoted; "52 30" x2 = "pas pas".

## Verdict

**NULL.** The bar's decision procedure ran to completion: its selection conditions cannot fire because none of the three promised values (80, 86, 60@1735) has landed, and no evidence selects 'jamais' under the forced standard. Per the bar's own final clause, the {plus, jamais} tie is **fenced as unbreakable at battery grade** until one of the three value venues lands. The claim ("52 decided in the ne-frames") is neither achieved nor refuted — inconclusive, not killed. No standing or red-team verdict contradicted; §7 intact.

## Follow-up targets for the supervisor queue (null regeneration, all IDs verified ABSENT from battery-queue.json)

**F1. id: "plus-jamais-gate80-rerun" | priority: 3**
claim: "Re-run the plus/jamais tiebreak iff poly-80-docket lands a named 80 value"
bars: "GATE: poly-80-docket status == verdict with a named 80 value (verify before testing; if the gate is unfired, refuse and re-queue). If the gate fired, test whether the landed 80 value selects 'plus' or 'jamais' at W1/W3 ('94 52 80 04' @1293/@1806) with zero forced contradiction; name the selected value, else keep the fence."
evidence: "plus-jamais-tiebreak NULL (2026-10-09): tie fenced pending 80/86/60 values; poly-80-docket queued at fence time"
adverses: "gate trigger must be a red-team value grant, not a battery promote (gate-trigger rule 2026-10-09); §7 tension still live"

**F2. id: "plus-jamais-gate86-rerun" | priority: 3**
claim: "Re-run the plus/jamais tiebreak iff 86's value lands at red-team level"
bars: "GATE: a red-team verdict naming 86's value exists (verify before testing; if unfired, refuse and re-queue). If fired, test whether the landed 86 value selects 'plus' or 'jamais' at W2 ('12 48 52 86' @1736) with zero forced contradiction; name the selected value, else keep the fence."
evidence: "plus-jamais-tiebreak NULL (2026-10-09): R20-087 left 86's value unnamed (class-level grant only)"
adverses: "same gate-trigger rule; §7 tension still live"

**F3. id: "ne52-register-corpus" | priority: 4**
claim: "Corpus register evidence on 'ne plus [INF]' vs 'ne jamais [INF]' as red-team input (not a battery naming)"
bars: "In the period corpus, measure 'ne plus [INF]' vs 'ne jamais [INF]' rates in drama vs prose; package the rates as red-team input with stated confidence; do NOT name 52 — this is evidence-gathering only"
evidence: "plus-jamais-tiebreak NULL (2026-10-09): no stream-internal discriminator; register is the only untested dimension"
adverses: "corpus rates select nothing at battery grade; do not present as a naming"

## Bookkeeping

- Lock: code/crowd17/next-token/locks/plus-jamais-tiebreak.lock created 2026-10-09T17:13:24Z (agent ff218a4e-0156-4f48-af60-ecf74f213ed8), deleted on completion of this report.
- Queue: `plus-jamais-tiebreak` → `status: verdict`, `result: null` (pre-write assert: was queued/verdictless; temp-file + rename; own entry only; no downgrade).
- R5005 untouched. Sealed gate instances untouched. Red-team adjudication queue untouched.
