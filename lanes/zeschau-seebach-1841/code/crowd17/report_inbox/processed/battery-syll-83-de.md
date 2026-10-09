# Battery `syll-83-de` — verdict: NULL

Target: test 83 as syllabic '-de' (verb ending) across @614/@1171 (87-83, cf. 'cède') extended to @1334 (39-83).
Date: 2026-10-09. Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`), re-derived in-session. `canonical.py` never used. R5005, sealed gates, red-team queue untouched. Lock created on start, deleted on completion. All @-offsets 0-based.

## Bar (verbatim, pre-registered before testing)

"name the host verbs with 83='-de' parsing all three windows, or kill the syllable fork"

Numbered pass/fail clauses (restated before testing, not modified after):

1. C1: a host verb is named at @614 with 83='-de' as its final syllable, and the window parses under standing values.
2. C2: a host verb is named at @1171 with 83='-de' as its final syllable, and the window parses under standing values.
3. C3: a host verb is named at @1334 with 83='-de' as its final syllable, and the window parses under standing values.
4. C4: adverse answered — coordinate with frame-87-83-cede (owns the 'cède' fence); do not contradict its verdict.

## Method

Re-derived the repaired stream independently (asserted 1,847 pairs / 96 types). Census n(83) = 15. The three bar windows confirmed on the stream:
- @614: `58 47 77 87 [83] 70 88 10 29` (row a4_00) — left token 87.
- @1171: `55 61 94 87 [83] 21 85 36 74` (row a6_09) — left token 87.
- @1334: `94 70 52 39 [83] 86 71 64 60` (row a7_05) — left token 39.

Syllabic 83='-de' attaches leftward, so the host word is "[left-token]de". Hosts tested under standing values only: 87='ce' promoted/granted (A11 HOLD, allophone tier), 39='a'/'à' battery-promoted (pending ratification), 77='le' provisional, 47='ce' promoted. Adopted as premises (stated, not re-run): battery-frame-87-83-cede (2026-10-09, verdict NULL) on the two 87-83 windows; battery-de-83-residuals (2026-10-09, promote) for the @1334/'39-83' and @1829/'38-83' fork ownership.

## Window evidence

**@1171 — host "cède", PARSES (adopted premise).** frame-87-83-cede: `[55-61-94 word] cède [21]` — 3sg present of *céder*, subject the 55-61-94 word unit, [21] noun-class direct object (surrender-valence takes a bare object). C2: PASS.

**@614 — host "cède", DOES NOT PARSE at battery grade (adopted premise).** frame-87-83-cede: the only syntactic parse is 'celle cède' (47-77 fusion + 'cède'), costing 2 ungranted assumptions, and the 'celle' re-segmentation was graded failing at battery grade by battery-ce-le-verb-frame; 'ce le cède' ungrammatical; 58's class unknown (cede-614-subject already ran, verdict NULL — subject still unnameable). Compound hosts ending '...cède' ('intercède', 'précède', 'succède') are dead under granted 47='ce' / provisional 77='le' ('le'/'ce' cannot be 'pré'/'suc'). Under standing values "87de" = "cede" is the ONLY nameable host, and it does not parse. C1: FAIL — but at epistemic grade: the owning battery explicitly left the verb rival live ("Not kill-grade... the verb rival stays a live candidate"). This battery does not overrule that assessment.

**@1334 — NO HOST NAMEABLE at battery grade.** Under promoted 39='a'/'à', "[39]de" = "ade" — not a French word. Under open 39, no penultimate syllable is nameable (e.g. 39='gar' for "garde" is untestable — no contact-profile evidence). Additionally phase-fragile: under a7_05's rival offset the row re-parses as `23 98 38 67 16 46 00 86 56 45 23 84 78 66` and the 39-83 bigram dissolves entirely (verified in-session) — the window is a canonical-offset object. C3: FAIL — epistemic (39's value open; phase uncertainty).

**@1829 (fenced to this target by de-83-residuals, outside the three-window bar):** `86 29 82 38 [83] 24 82 16 59` — host "[38]de"; 38's value open, no host verb nameable at battery grade. Word-level 'de' already dead here (24 finite, promoted). Recorded as fenced, not resolved by this bar; covered by follow-up 2.

## Per-clause results

- C1 (@614): FAIL (epistemic) — only nameable host 'cède' unparseable at battery grade per owning battery, which leaves the rival live.
- C2 (@1171): PASS — 'cède' parses.
- C3 (@1334): FAIL (epistemic) — no nameable host under promoted values; bigram phase-fragile.
- C4 (adverse): ANSWERED — coordinated with frame-87-83-cede (verdict NULL, no longer queued): adopted its window findings as premises; this NULL does not contradict its "verb rival stays a live candidate" assessment. The 83='de' word-lead is untouched (only the syllabic fork was tested).

## Verdict: NULL

The bar's pass condition (hosts named and parsing at all three windows) is unmet — score 1/3. But neither failure is kill-grade: no window forces 83 ≠ '-de' (both failures are epistemic — unnameable subjects/hosts, open values, phase fragility), and no cleaner rival is demonstrated on these frames (word-level 'de' is ungrammatical at @614/@1171: 'ce de'). Killing the fork would overrule frame-87-83-cede's standing NULL, which explicitly keeps the 'cède' rival live at @614. The '-de' syllable fork remains unfalsified but undemonstrated at battery grade.

## Follow-up targets (null regenerates work)

1. **syll-39-de-host** (P3): name 39's syllable at @1334 as the penultimate of a French '-de'-final verb. Bar: host verb named and @1334 parsed under standing values, or the @1334 leg fenced. (39's value decides; phase-fragility noted.)
2. **syll-83-de-1829** (P3): the @1829 '-de'-final-word fork ("38"+"de") fenced to this target by de-83-residuals. Bar: host verb named and @1829 parsed, or fenced with cause.
3. **syll-83-phase-audit** (P4): re-run the three-window host test under each row's rival offset (a4_00, a6_09, a7_05). Bar: record which of @614/@1171/@1334 survive re-phasing; the fork's windows are canonical-offset objects until shown otherwise.

No standing red-team verdict is contradicted. No existing verdict downgraded. §7 intact (no new polyvalence declared; the fork is a positional/syllabic reading, not a second value).
