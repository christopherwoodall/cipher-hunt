# Battery verdict: ne-ce-1169

- Target: `ne-ce-1169` (priority 2)
- Claim: 94@1169 (stream-unique 94-87 bigram, 'ne ce') resolves
- Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json + data/upstream-ct_R5005.txt, parsed per repair_parse.py). Never canonical.py.
- Date: 2026-10-08

## Bar (verbatim)

"(a) census 94's 37 windows; state why 'ne' fails or parses at @1169; (b) resolve iff @1169 parses under 94='ne' STRONG LEAD with stated cause, or a rival 94-value is demonstrated at this window; (c) do not overturn R17-001 (94='ne' stays STRONG LEAD) and do not declare a second 94 value without red-team declaration (§7)"

Numbered clauses:

1. (a1) Census 94's 37 windows (re-derived on the repaired stream; count confirmed = 37).
2. (a2) State why 'ne' fails or parses at @1169, in 1841 diplomatic French.
3. (b) Resolve iff @1169 parses under 94='ne' STRONG LEAD with stated cause, or a rival 94-value is demonstrated at this window with byte evidence.
4. (c) R17-001 intact (94='ne' stays STRONG LEAD); no second 94 value declared (§7).

Adverses: 87='ce' granted; 94-87 hapax (stream-unique bigram).

## Method

Parsed the repaired stream; enumerated all 37 indices n with seq[n]='94'; recorded
±4 windows, predecessor/successor contact profiles; inspected raw bytes of row a6_09
(offset 0, 41 digits, 20 pairs — no phase anomaly). Grammar test: 1841 diplomatic
French — 'ne' is a preverbal negator clitic; 'ce' (87 granted) is a demonstrative
pronoun/determiner, not a preverbal clitic pronoun.

## Window-level evidence

Target window @1169 (row a6_09):
`@1162:21 @1163:67 | 78 45 13 55 61 | @1169:94 @1170:87 @1171:83 @1172:21 @1173:85`
Row a6_09 pairs: 00 92 29 80 17 77 82 44 83 21 67 78 45 13 55 61 **94 87** 83 21.
Raw bytes clean; the bigram is not an offset artifact.

Census of 94 (37 windows), ±4 context:

- @65 (a1_01): 34 29 40 12 **94** 92 69 13 24
- @101 (a1_02): 85 08 21 62 **94** 93 59 45 28
- @161 (a1_05): 58 35 93 52 **94** 24 87 11 24
- @250 (a2_02): 66 91 32 44 **94** 65 63 00 66
- @318 (a2_04): 45 64 59 32 **94** 06 11 92 60
- @349 (a2_05): 01 06 70 12 **94** 74 67 78 40
- @494 (a2_11): 20 67 78 42 **94** 02 79 88 47
- @509 (a3_00): 21 67 77 62 **94** 64 98 65 88
- @558 (a3_02): 59 34 17 86 **94** 59 30 67 11
- @570 (a3_02): 97 13 76 45 **94** 52 87 78 45
- @578 (a3_02): 45 13 55 61 **94** 82 06 06 50
- @651 (a4_02): 77 78 52 82 **94** 76 49 24 26
- @688 (a5_00): 64 29 40 65 **94** 29 60 03 39
- @699 (a5_01): 02 50 45 28 **94** 60 12 98 20
- @762 (a5_03): 29 40 20 62 **94** 59 39 88 66
- @771 (a5_03): 98 80 10 22 **94** 07 06 94 15
- @774 (a5_04): 22 94 07 06 **94** 15 33 73 37
- @785 (a5_04): 89 11 24 42 **94** 74 65 84 06
- @841 (a5_06): 17 98 20 62 **94** 26 12 16 00
- @1102 (a6_06): 67 86 52 82 **94** 74 47 78 65
- @1169 (a6_09): 45 13 55 61 **94** 87 83 21 85  ← target; unique 94-87 bigram
- @1182 (a6_10): 59 37 77 78 **94** 82 06 06 59
- @1293 (a7_03): 17 84 59 35 **94** 52 80 04 62
- @1330 (a7_04): 56 30 06 62 **94** 70 52 39 83
- @1353 (a7_05): 62 48 77 78 **94** 82 06 52 37
- @1363 (a7_06): 35 13 92 62 **94** 79 14 60 03
- @1549 (a8_00): 00 46 70 12 **94** 92 45 23 99
- @1576 (a8_01): 32 28 52 82 **94** 76 47 98 24
- @1664 (a8_04): 98 98 80 22 **94** 84 64 06 91
- @1687 (a8_05): 65 13 93 62 **94** 79 14 60 27
- @1701 (a8_06): 23 91 85 33 **94** 30 20 62 94
- @1705 (a8_06): 94 30 20 62 **94** 88 26 12 06
- @1713 (a8_06): 06 29 40 65 **94** 44 59 30 64
- @1742 (a8_07): 52 86 12 34 **94** 82 46 56 40
- @1773 (a8_09): 26 37 78 62 **94** 24 87 64 59
- @1795 (a8_09): 00 86 56 42 **94** 59 37 91 79
- @1806 (a8_10): 77 84 59 35 **94** 52 80 04 61

Contact profiles (re-derived): followers — 82x4, 74x3, 59x3, 52x3, 92x2, 24x2,
76x2, 79x2, 87x1 (only @1169), plus 17 singletons (93, 65, 06, 02, 64, 29, 60,
07, 15, 26, 70, 84, 30, 88, 44). Predecessors — 62x9 ("il ne" frames), 12x3,
42x3, 82x3, 61x2 (the two dict-frame windows), 65x2, 22x2, 78x2, 35x2, plus
singletons. Follower 87 occurs exactly once: @1169 is the sole 94-87 bigram
in 1,847 pairs. (Note: 94-24-87 occurs @161 and @1773 — 'ne' separated from
'ce' by a verb, which is the grammatical order; only the adjacent bigram is
a hapax.)

Grammar at @1169: under 94='ne' (negator) + 87='ce' (granted), the adjacent
sequence reads "ne ce". In 1841 diplomatic French this is ungrammatical:
'ne' is a preverbal negator clitic and must immediately precede the verb
(with only clitic pronouns between); 'ce' is a demonstrative
pronoun/determiner, never a preverbal clitic. No construction of the period
places "ne" directly before "ce" as two words (inversion "n'est-ce" puts the
verb between; the grammatical order is "ce ne"). Right context 83 (open,
'de' lead per R17) does not rescue it: "ne ce de" is no better.

Rescues considered and disposition:

1. Leftward attachment: 61-94 as a word-final "...ne" syllable (prenne/donne
   family) + 87='ce' ("...ne ce..."). Grant-compatible — the 94 value stays
   'ne' (syllabic, not the negator word), consistent with the 70-12-94
   "prenne" fence and the fenced 12/94 duality (R17-018). Undemonstrated:
   61's value is open; no byte evidence names the word.
2. Word-initial: 94-87 as "néce-" (nécessaire/nécessité family): "... [13-55-61]
   nécessaire [83 ...]". Grant-compatible (87='ce' as syllable). Undemonstrated:
   83's value open; agreement/frame unchecked.
3. Elision "n'" + vowel: dead — 87='ce' is consonant-initial.
4. "ne" as archaic "nor": dead — not 1841 diplomatic prose.
5. Discontinuous "ne...que" with 87 as subject: dead — the period order is
   "ce ne ... que", never "ne ce ... que".
6. Rival 94-value at this window: none demonstrated with byte evidence; any
   candidate would be invented. §7 independently bars declaring a second 94
   value without red-team declaration.

Relation to standing verdicts: R17-001 (94='ne' STRONG LEAD, promote rejected)
is NOT overturned — this window is an anomaly inside the lead's stated
caveats, not a contradiction of it. The dict-frame-78-45-13-55-61 null
already fenced this exact bigram as "a 94-problem outside the claim's scope";
this battery confirms the fence and narrows the question to segmentation.

## Per-clause pass/fail

1. (a1) **PASS.** Census complete: 37 windows, all @-offsets listed above;
   94-87 bigram confirmed stream-unique (1/1847).
2. (a2) **PASS.** 'ne' as negator fails at @1169: "ne ce" is ungrammatical in
   1841 diplomatic French (preverbal clitic 'ne' cannot directly precede
   demonstrative 'ce'); raw bytes and row offset confirm the bigram is real,
   not a phase artifact.
3. (b) **FAIL (inconclusive, not kill-grade).** No parse under 94='ne' STRONG
   LEAD is demonstrated with a stated cause — rescues (1) and (2) are live
   hypotheses, not byte-evidenced parses. No rival 94-value is demonstrated
   at this window. Kill grade not met: the window does not force the claim
   false, because re-segmentation (61-94 word-final, or 94-87 word-initial)
   keeps the 94='ne' value intact per the fenced 12/94 duality (R17-018) and
   the "prenne" precedent; and no cleaner rival value was demonstrated on
   the frame.
4. (c) **PASS.** R17-001 untouched (94='ne' stays STRONG LEAD); no second 94
   value declared (§7). No standing red-team verdict contradicted.

## Verdict: NULL

@1169 does not resolve: "ne ce" fails as negator + demonstrative, and no
grant-compatible parse is demonstrated. The bigram is a genuine 94-frame
anomaly (segmentation question), not an overturn of 94='ne' STRONG LEAD.
R5005, sealed gate instances, and the red-team adjudication queue untouched.
No standing verdict is overwritten.

## Proposed follow-up targets (null regenerates work)

1. **seg-61-94-word** (priority 2). Claim: 61-94 at @1169 (and @578) is a
   word with final "...ne" syllable (prenne/donne/vienne family), so 94
   attaches leftward and 87='ce' follows as the next word. Bars: (a) census
   61's 18 windows and triangulate 61's value via contact profiles; (b)
   demonstrate a French word 61-94 that yields a grammatical "...ne ce..."
   parse at @1169 with stated agreement; (c) keep 94='ne' value intact
   (§7 — no second value declared). Evidence: this report; 70-12-94
   "prenne" fence; R17-018 12/94 duality.
2. **nece-94-87-initial** (priority 2). Claim: 94-87 is word-initial "néce-"
   (nécessaire/nécessité family) at @1169. Bars: (a) profile 83's
   successors for 'ss'-shaped continuations of "nécessaire/nécessité";
   (b) parse "... [13-55-61] nécessaire [83 ...]" at @1164–1173 with stated
   agreement and frame; (c) do not disturb the 87='ce' grant (syllabic
   reading only). Evidence: this report; 87='ce' granted.
3. **redteam-94-functional-split** (priority 1, red-team venue). Question:
   does the red team sanction a declared positional/functional split of 94
   (preverbal negator vs word-final "...ne" syllable, à la 67 et/veut), or
   does the fenced 12/94 duality (R17-018) already cover @1169-type windows?
   Bars: (a) frame with @1169 evidence + 70-12-94 "prenne" + this report;
   (b) red-team ruling is final; no battery declares the split. Evidence:
   this report; R17-001; R17-018.
