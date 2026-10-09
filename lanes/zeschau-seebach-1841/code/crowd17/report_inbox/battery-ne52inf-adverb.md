# Battery report: ne52inf-adverb (NULL — {plus, jamais} tie unbreakable at battery grade)

**Target:** ne52inf-adverb — "name 52 across the three 'ne [52] [INF]' windows (@1294/@1736/@1807)"
**Worker:** 4517486b-5a58-4737-a49b-cb6af69b3e0b | **Date:** 2026-10-09
**Stream:** repaired 1,847-pair / 96-type parse (code/side-keyhunt/repaired_offsets.json + data/upstream-ct_R5005.txt, parsed per code/side-keyhunt/repair_parse.py; asserts re-verified in-session). Never canonical.py. No R5005 touched. No data invented.

## Bar (verbatim from battery-queue.json)

"name 52 with the frame parsing as 'ne [52] [INF]' under standing values, stating the §7 polyvalence tension for red team"

## Bar as numbered clauses (pre-registered restatement)

1. A single adverb value is NAMED for 52 such that 'ne [52] [INF]' parses at all three windows with ≤1 ungranted assumption.
2. The §7 polyvalence tension (adverb in ne-frames vs the adjective lead elsewhere) is stated for the red team.
3. No polyvalence is declared at battery level (§7 honored); no standing verdict contradicted or downgraded.

## Method

1. Re-derived the repaired stream byte-exactly (1,847 pairs, 96 types; n(52)=27).
2. Fixed the three windows on bytes (0-based; queue's "@1736" labels the window by its 12-48 "ne" — 52 itself sits at @1738):
   - W1 @1294 (a7_03): `35 94 52 80 04` = "[35] ne [52] [80-verb] [04]"
   - W2 @1738 (a8_07): `60 12 48 52 86 12` = "[60] ne(12-48 analytic) [52] [86-INF] …"
   - W3 @1807 (a8_10): `35 94 52 80 04` = byte-identical to W1
   Stream-wide: "94 52 80" occurs exactly 2x (@1293/@1806 starts); "12 48 52 86" exactly 1x (@1736 start). 80 = verb-frame (A8); 86 = INF-class (A9).
3. Tested adverb candidates {pas, plus, jamais, point, rien, guère, se, le} and the finite-modal class against the three windows (0 ungranted assumptions required) and against the global kill windows from battery-leftedge-52-86-1736 (adopted, not re-litigated): @571 "ce ne [52] ce", @482/@1308 "[X] [52] pas", @1007 "la [52]".
4. Adopted as standing context (not re-decided): leftedge-52-86-1736 NULL (frame real x3; 52 unnameable at battery grade); ni-1740-1742 KILL (clause boundary after @1739); rightedge-56-1745 NULL (@1742+ untouched here); 30='pas' battery-promoted; 94='ne' STRONG LEAD; 12-48 analytic 'ne' (R17 battery).

## Window-level evidence (@-offsets, 0-based)

**The frame (adopted from leftedge, re-verified on bytes):**
- W1 @1293–1296 = `94 52 80 04`; W3 @1806–1809 identical. W2 @1736–1739 = `12 48 52 86`.
- In all three, 52 sits strictly between 'ne' (94 or 12-48) and an infinitive (80-frame / 86-INF-class).

**Candidate matrix (three windows only):**
- 52='plus' → "ne plus [80/86]" at all three: PARSES, 0 ungranted assumptions. "ne plus [INF]" is clean 1841 French.
- 52='jamais' → "ne jamais [80/86]" at all three: PARSES, 0 ungranted assumptions. "ne jamais [INF]" is clean 1841 French.
- 52='pas' → BLOCKED: 30='pas' is battery-promoted and "52 30" x2 (@482, @1308) would read "pas pas" — ungrammatical. Not re-litigated.
- 52='point' → FAILS the assumption budget: corpus "de ne point [INF]" x10 always carries "de"; no "de" precedes 'ne' at any window (W1/W3 have 35, noun-class at battery grade; W2 has 60, open). Bare "ne point [INF]" is not 1841-grammatical.
- 52='rien' → same "de" requirement ("de ne rien [INF]") — fails identically.
- 52='guère' → "ne guère [INF]" is marginal (guère selects finite verbs/adjectives in 1841); strictly weaker than plus/jamais, no forcing evidence.
- 52='se' → "ne se [INF]" unattested in the lane corpus (leftedge); fails.
- 52='le' (object pronoun) → "ne le [52-ce]" dies at @571 ("ce ne le ce" ungrammatical); fails.
- 52=finite modal ("peut"-class) → "ne peut [INF]" parses the three windows but is kill-grade dead globally (@1007 "la peut"; @571 "ce ne peut ce"); fails uniformity, and frame-scoped modal naming is not forced over the adverb.

**The tie:** {plus, jamais} both parse all three windows with zero ungranted assumptions. No battery-grade discriminator exists: 80/86 values are open (poly-80-docket is red-team; 86 value open under A9 class grant), 60's value at W2's left edge is open (queued leftedge-60-value), 35's value at W1/W3's left edge is open (noun-class only), and neither distributional nor corpus evidence in the lane forces one. Per the stem-03-value precedent, battery grade needs FORCED, not compatible.

**Global uniformity is impossible at battery grade (the §7 tension, stated for red team):**
- Every adverb candidate dies outside the ne-frames: @571 "ce ne [ADV] ce" (@571 kills plus/jamais/pas/point/rien/guère alike); @482 "pour [13] [ADV] pas" / @1308 "[74] [ADV] pas" ("[ADV] pas" ungrammatical); @1007 "la [ADV]" (adverb after "la" ungrammatical).
- The adjective arm is live elsewhere: "la [52]" x3 (@1007/@1124/@1722), "52 37" x4 (@1124/@1129/@1356/@1722; adj-52-37-value NULL with a {même/seule} tie).
- Adverb (ne-frames) + adjective (la-frames) in one cell = polyvalence. 67 et/veut is the sole true polyvalence (§7). Declaring a second is a red-team act, not available here. The tension is escalated (F3), not resolved.

## Per-clause pass/fail

- **C1 (single adverb value named): FAIL at null grade.** The frame-scoped CLASS (negation adverb) is established — "ne plus/jamais [INF]" parses all three windows — but no single VALUE is forced: {plus, jamais} tie, unbreakable at battery grade (no discriminator in 80/86/60/35 values, distribution, or corpus). Not kill-grade: no window forces the adverb reading false; the failure is naming, not structure.
- **C2 (§7 tension stated): PASS** — stated above: negation-adverb in ne-frames x3 vs adjective lead in "la [52]"/52-37; uniform value impossible without a red-team §7 declaration.
- **C3 (§7 honored; standing state intact): PASS** — no polyvalence declared; 30='pas', 94='ne', A8, A9, ni-1740-1742, leftedge/rightedge standings all untouched; nothing downgraded.

## Adverses

- **"do not declare polyvalence at battery level (§7)"**: HONORED — none declared; the candidacy is packaged for red team (F3).
- **"clause boundary after @1739 adopted from ni-1740-1742"**: ADOPTED as standing context, not re-litigated; W2's right edge stops at @1741 in this analysis.
- **"coordinate with rightedge-56-1745 (@1742+), do not duplicate"**: HONORED — nothing at @1742+ examined; rightedge's NULL standing untouched.

## Verdict

**NULL.** The 'ne [52] [INF]' frame is real and 52 is negation-adverb-shaped inside it, but battery grade cannot NAME 52: {plus, jamais} tie with no forcing discriminator, and global uniformity needs a red-team §7 declaration (adverb vs adjective arms).

## Follow-up targets for the supervisor queue (null regeneration)

**F1. id: "plus-jamais-tiebreak" | priority: 3**
claim: "52 = 'plus' vs 'jamais' decided in the ne-frames"
bars: "name 52='plus' iff the landed 80/86 infinitive values (poly-80-docket / red-team 86) or 60's value at @1735 (leftedge-60-value) selects 'plus' with zero forced contradiction, else name 'jamais' under the same standard; if neither selects, fence the tie as unbreakable at battery grade"
evidence: "ne52inf-adverb null (2026-10-09): {plus, jamais} both parse W1/W2/W3 with 0 ungranted assumptions; no battery-grade discriminator"
adverses: "80 value open (poly-80 red-team); 86 value open (A9 class grant); 60 value open; §7 tension with adjective arm still live"

**F2. id: "seg-52-80-unit" | priority: 3**
claim: "'52-80' @1294/@1807 is one infinitive (52 = prefix syllable), dissolving the adverb naming"
bars: "unit reading holds iff 52-80 parses as one infinitive with zero contradiction under standing values (cf. queued seg-52-86-unit for the @1738 window); else kill the unit reading with the failing clause stated"
evidence: "parallel to seg-52-86-unit (queued); '94 52 80' x2 byte-identical; 80 verb-frame (A8)"
adverses: "do not duplicate seg-52-86-unit; A8 verb-frame grant must survive"

**F3. id: "split-52-redteam" | priority: 2**
claim: "52 is a §7 split candidate: negation-adverb in 'ne [52] [INF]' x3 vs adjective in 'la [52]' x3 / 52-37 x4"
bars: "package complete iff both arms are byte-cited with window tables and the polyvalence question is stated with the 67 et/veut sole-polyvalence rule cited; red team decides, battery declares nothing"
evidence: "ne52inf-adverb null (adverb arm: plus/jamais tie); adj-52-37-value null ({même/seule} tie, 2026-10-09); leftedge-52-86-1736 null"
adverses: "red-team docket item — do not adjudicate at battery level"

---
Lock: locks/ne52inf-adverb.lock created 2026-10-09T05:30Z, deleted on completion of this report. No R5005 touched. No sealed gates touched. No red-team verdicts modified. No promotions made.
