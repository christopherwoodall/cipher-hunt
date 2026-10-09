# Battery report: inf-37-78-475

**Target:** inf-37-78-475 — 37-78 is the same stable infinitive word at @475, confirming 78 word-final
**Claim:** 37-78 is the same stable infinitive word at @475, confirming 78 word-final
**Date:** 2026-10-08
**Worker:** 134af7bc-4398-4ce7-9800-7929acc6c416. No stale lock existed at start; lock created 2026-10-09T02:26:06Z, deleted on completion.
**Stream:** repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json + data/upstream-ct_R5005.txt, parsed per code/side-keyhunt/repair_parse.py). Never canonical.py. No R5005, sealed gates, or red-team queue touched. All counts trace to the stream.
**@-convention:** 0-based stream indices; 37-78 occurrences are 37-anchored.

## Bar (verbatim, pre-registered BEFORE testing)

"(a) @474-482 parsed with 74's post-infinitive slot named or fenced; (b) 37-78 unit stability across all x4 stated - @414 and @1770 must not contradict the infinitive reading; (c) 78's 20-follower scatter cited against bound-'verdict' reading"

## Bar restated as numbered pass/fail clauses (not modified)

1. Clause (a): the @474-482 window parses grammatically with the slot occupied by 74 (immediately post-infinitive, @477) either named to a value or fenced with stated cause.
2. Clause (b): at the two non-84-24-37 windows (@414, @1770), no standing value forces 37 and 78 into separate words — i.e., neither window contradicts reading 37-78 as one infinitive word with 78 word-final.
3. Clause (c): 78's follower scatter is cited (re-derived) against the bound-'verdict' reading (78='ver'+45='dict' as one fixed word).

## Method

1. Reparsed the repaired stream byte-exactly per repair_parse.py (1,847 pairs, 96 unique groups confirmed).
2. Enumerated all 37-78 bigrams: x4 at @312, @414, @475, @1770 (37-anchored). 37-78-45 occurs x1 stream-wide (only W1 @312-314).
3. Re-derived 78's full follower census (31 windows) and 74's full census (34 windows, predecessors + followers).
4. Re-derived 51's census (6 windows) and 93's census (14 windows) for the @414 and @474-482 windows.
5. Tested each bar clause against the bytes; cited (not re-run) the w1-314-rebar PROMOTE for the two 84-24-37 windows.

Standing values used: banked 11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que; granted 87=ce, 64=qui, 96=par, 17=fois, 79=tout (A5), 00=pour (A9), 84=on (A15), 47=ce (A4); provisional 59=est, 77=le; A1 37/32/42 predicative frames; A11 45='ce' HOLD; 94='ne' STRONG LEAD (R17-001); 24=finite modal verb (ne-24-profile PROMOTE); 78='ver' LEAD only (R16-005, not granted).

## Window-level evidence

**W2 — the @475 window (row a2_10):**
`@472:46 @473:84 @474:24 @475:37 @476:78 @477:74 @478:45 @479:93 @480:00 @481:13 @482:52 @483:30`
= "que(46) on(84) [24-modal] [37] [78] [74] ce(45) [93] pour(00) [13] [52] pas(30)"
Byte-identical left context to W1 (84-24-37 @473-475 vs @310-312); 78@476 is followed by 74, not 45.

**Window A — @414 (row a2_08):**
`@411:53 @412:84 @413:51 @414:37 @415:78 @416:49 @417:74 @418:74 @419:46`
= "[53] on(84) [51] [37] [78] [49] [74] [74] que(46)"
78@415 followed by 49 (not 45). 74 doubled @417-418.

**Window B — @1770 (row a8_08):**
`@1768:64 @1769:26 @1770:37 @1771:78 @1772:62 @1773:94 @1774:24 @1775:87`
= "qui(64) [26] [37] [78] [62] ne(94) [24-modal] ce(87)"
78@1771 followed by 62 (not 45). Matches the "qui [23/26] 37" frame family (qui-2326-prefix PROMOTE: 26 in post-qui verb slot, 37 post-verbal predicative per A1).

**78's follower census (re-derived, 31 windows):** 21 distinct followers —
06 x1, 17 x1, 18 x1, 40 x3, 41 x2, 42 x1, 43 x1, 45 x4 (@313, @573, @982, @1164), 47 x1, 48 x2, 49 x2, 52 x1, 55 x1, 62 x2, 63 x1, 64 x1, 65 x1, 66 x1, 67 x1, 74 x1 (@476), 94 x2.
Correction to the bar text: the scatter is **21** distinct followers, not 20 (w1-314-ambig said 20; w1-314-rebar said 21 — rebar confirmed). 78→45 is 4/31.

**74's census (re-derived, 34 windows):** 19 distinct followers {67 x2, 77 x2, 45 x3, 74 x6, 46 x3, 65 x2, 62 x3, 47 x2, 48, 49, 40, 42, 32, 52, 34, 84, 87, 35, 93}, 20 distinct predecessors {49 x5, 94 x3, 74 x6, 39 x2, 44 x2, 36 x2, ...}. 74 is a free word, not a bound syllable. "74 45 93" trigram x2 (@261, @479). "ne(94) 74" x3 (@350, @786, @1103) puts 74 in verb position in those windows.

**51's census (6 windows):** followers {47, 62, 70, 37, 64, 45} — six distinct in six windows, no class signal; predecessors {97, 98, 71, 84, 91, 48}. 51→37 only at @413. Value open, unclassifiable at battery grade.

**93's census (14 windows):** "45 93" x3 (@263, @479, @604) — "ce(45) [93]" trigram. Value open.

## Per-clause pass/fail

**Clause (a) — PASS (fence arm).** @474-482 parses as:
"que(46) on(84) [24-finite-modal] [37-78-INF, one word, 78 word-final] [74: open word] ce(45) [93: open] pour(00) [13] [52]".
The modal+infinitive core is grammatical under standing values (rebar: 24 requires an overt infinitive complement; 37-78 is the only viable candidate, word-internal, ending at 78). 74's slot is **fenced with stated cause** rather than named: (i) preposition values are killed — 74→46 x3 against banked 46='que' ("de que"/"à que" ungrammatical); (ii) 'ne 74' x3 frames 74 in verb position elsewhere, but no standing value names it; (iii) 74-74 doubling x6 is an unanalyzed lead; (iv) 74's 34-window scatter (19 followers, 20 predecessors) marks it a free word, so it cannot be a bound continuation of 78. The claim (37-78 stability, 78 word-final) does not depend on 74's value.

**Clause (b) — PASS.** Neither window forces 37/78 apart:
- @414: no standing value occupies 51, 49, or the 37/78 slots. 78's follower is 49 (≠45), consistent with word-final 78. 37-78-45 as one word is independently refuted stream-wide (x1, only W1; no French X-verdict infinitive per rebar clause b). The infinitive reading requires only that 51 not force a split — 51's 6-window scatter forces nothing. Adverse "51's value open" fenced with that cause.
- @1770: "qui(64) [26] [37] [78]..." matches the promoted "qui [23/26] 37" frame (26 post-qui verb slot, 37 post-verbal predicative per A1). Noted tension: a *bare*-adjective reading of predicative-37 would split 37-78 — but no standing value forces the bare reading; a predicative **infinitive phrase** (37-78 as one word, cf. "sembler + INF" in French) satisfies the A1 frame with 26's value open. 78's follower is 62 (≠45; 62 a free word, n=35), consistent with word-final 78. No contradiction.
- Supporting: 78's followers across the four 37-78 windows are four distinct groups (45, 49, 74, 62) — no fixed rightward bond anywhere.

**Clause (c) — PASS.** 78 takes 21 distinct followers over 31 windows; 78→45 is 4/31. A bound "verdict" word (78='ver'+45='dict' fixed) predicts 78 overwhelmingly followed by 45. The scatter refutes bound status at distributional grade. (Count corrected from the bar's "20" to the re-derived 21; the conclusion is strengthened, not weakened.)

## Adverses

- **51's value open (@414):** fenced — see clause (b). 51 n=6, no class signal; nothing in its distribution licenses or forbids an infinitive complement, and the bar requires only non-contradiction.
- **74's value open:** fenced — see clause (a). Prepositions killed at 74→46 x3; verb-position suggested by 'ne 74' x3 but unnamed; doubling lead noted.

## Verdict: PROMOTE

All three bar clauses pass (two via the explicitly permitted fence arm, each with stated cause); both listed adverses are fenced, not ignored. **37-78 is the same stable infinitive word at @475 as at W1, and 78 is word-final in both windows.** No standing verdict is contradicted or downgraded: this battery names no value for 37 (the S5 fence on 37='le' is untouched), declares no polyvalence (§7: 67 et/veut remains the sole true polyvalence), and corroborates w1-314-rebar's W1 finding at the second 84-24-37 window without duplicating its structural work. R5005, sealed gates, and the red-team adjudication queue untouched.

## Leads for follow-up (observations, not required by this verdict)

- L1: name 74 — 'ne 74' x3 (verb-position) vs 74→46 x3 (kills prepositions) vs 74-74 x6 (doubling) is a tight discrimination set; 74's value would complete the @474-482 parse.
- L2: 51's class — 6 windows are thin; a 51-profile battery (predicated on more context) would firm up window A's left edge.
- L3: 26's value at @1769 — deciding 26 would resolve whether the @1770 predicative is an infinitive phrase (compatible) or forces re-analysis.
