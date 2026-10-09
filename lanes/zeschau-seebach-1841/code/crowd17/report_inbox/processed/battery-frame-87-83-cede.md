# Battery `frame-87-83-cede` — verdict: NULL

Target: '87-83' x2 (@614, @1171) reads 'cède/cédé' (verb), fencing the 'ce de' adverse against 83='de'.
Date: 2026-10-09. Stream: repaired 1,847-pair parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`). `canonical.py` never used. R5005, sealed gates, red-team queue untouched. Lock created on start, deleted on completion.

## Bar (verbatim, pre-registered)

"(a) both windows parse with 87-83 as a 'céder'-shaped verb; (b) @614's left context '47 77' and '70 88' tail parsed or fenced with cause; (c) the consequence for the 83='de' lead stated (fenced adverse, not a kill)"

Numbered clauses:
- **C1:** both windows (@614, @1171) parse with 87-83 as a 'céder'-shaped verb.
- **C2:** @614's left context '47 77' and '70 88' tail parsed or fenced with cause.
- **C3:** the consequence for the 83='de' lead stated (fenced adverse, not a kill).

## Method

Re-derived the full stream independently (1,847 pairs / 96 types confirmed). Exhaustive census: '87-83' occurs exactly 2x stream-wide — 87@613/83@614 and 87@1170/83@1171 (the claim's @-offsets label the 83 position). '47 77' occurs exactly 1x (@611-612, immediately before the @614 window); '70 88' occurs exactly 1x (@615-616). Both neighbor clusters are hapax. French tested against 1841 diplomatic usage only.

Standings used: 47='ce' promoted (allophone tier); 77='le' provisional; 94='ne' STRONG LEAD (R17-001 declined the promote — the brief's "promoted" is overstated); 21=noun-class (registry); 61 class open; 83='de' lead only (not in registry).

## Window evidence

**@1171 — `55 61 94 87 83 21 85 36 74` (rows a6_09/a6_10): PARSES.**
`[55-61-94 word] cède [21]` — subject = the 55-61-94 word unit (open lead from battery-seg-61-94-word, stated assumption), 'cède' 3sg present of *céder*, [21] noun-class direct object. *Céder* in the "surrender" valence takes a bare direct object (*céder sa place*, *céder le pas*), so the complement is grammatical. Alternative parse `[61] ne cède [21]` under 94='ne' (STRONG LEAD) is available but weakened by battery-94-87's finding that 94 attaches leftward/syllabic at @1169 — recorded as caveat, primary parse is the word-unit one.

**@614 — `58 47 77 87 83 70 88 10 29 88` (rows a4_00/a4_01): DOES NOT PARSE at battery grade.**
The only syntactic parse is 'celle cède' (47-77 fusion on the granted 47-11/87-11='cela' dissolution precedent + 'cède' verb). That costs 2 ungranted assumptions, and the same-day battery-ce-le-verb-frame graded the 'celle' re-segmentation as failing at battery grade. No subject-bearing alternative parses: 'ce le cède' is ungrammatical, and 58's class is unknown (no "[58] … cède" rescue available). The 'ce le' contact itself was already fenced as a 77-value residual by battery-ce-le-verb-frame.

## Per-clause results

- **C1: FAIL.** @1171 parses cleanly; @614's parse needs 2 ungranted assumptions, one pre-graded failing by a sibling battery. The both-windows requirement is not met.
- **C2: PASS (fenced with cause).** '47 77' fenced — hapax cluster, already fenced as the ce-le residual by battery-ce-le-verb-frame (2026-10-09). '70 88' tail fenced — hapax, 88's value open, tail ('10 29 88' = '[10]er[88]') is 88-value-dependent.
- **C3: STATED.** 83='de' is a lead, never granted. The two '87 83' windows remain a standing adverse against it ('ce de' ungrammatical per parvenir-thirds T4). Had the verb rival held, 83='de' would be fenced (not killed) at these two windows — locus-level, exactly as the granted 'cela' dissolutions fence 87='ce'. Since the rival is unproven at @614, the fence is not established; 83='de' stands unthreatened, with the two windows recorded as its open adverse.

## Adverses answered

- **83='de' lead:** fenced, not killed — consequence stated under C3. No standing verdict contradicted.
- **70's frame at @614 unparsed:** fenced with cause (hapax, 88-value-dependent) under C2.
- **"'céder' takes 'à', not a bare complement":** answered — the surrender-valence (*céder sa place*) takes a bare direct object, and 21 is noun-class. Semantic caveat recorded: if 21='suite' (battery lead), "cède suite" is strained; the bar is syntactic and 21's value is open.

## Verdict: NULL

Not kill-grade: no window forces the claim false, and 'ce de' remains ungrammatical under 83='de', so the verb rival stays a live candidate. The failure is epistemic (@614 underdetermined), not falsifying.

## Follow-ups proposed (for supervisor queuing)

1. `cede-614-subject` (P2) — name 58's class at @610 (`64 39 64 02 58 47 77 87 83`); if 58 is noun-class, test '[58] … cède' against the 'celle' fusion; decides @614's subject.
2. `necede-21-semantic` (P3) — once 21's value resolves, test semantic fit of 'cède [21]' at @1171 (e.g. 'suite' strains the surrender-valence).
3. `de83-adverse-restock` (P3) — re-test the 83='de' lead on windows excluding @614/@1171 (locus-fenced), confirming the lead's independent legs.
