# Battery report: enne-family-12-94

- id: enne-family-12-94
- date: 2026-10-09
- worker: 634bd19a-70e4-4318-8d6e-bf16bc4b6ef5
- lock: code/crowd17/next-token/locks/enne-family-12-94.lock created 2026-10-09T03:43:56Z; no prior lock existed (fresh take, not a stale re-dispatch).

## Bar (verbatim, pre-registered before testing)

"confirm iff @348-349 and @1548-1549 both parse with 12='n'+94='ne' as letters inside one word AND @64-65 stays the sole word-resistant '12 94' (already shown); else re-open the letter reading"

The bar was not modified after seeing data. Clause numbering fixed before testing:

- C1: @348-349 parses with 12='n' + 94='ne' as letters inside one word.
- C2: @1548-1549 parses with 12='n' + 94='ne' as letters inside one word.
- C3: @64-65 stays the sole word-resistant '12 94'.

("Confirm" maps to the protocol's promote verdict; "re-open the letter reading" would map to null with red-team escalation.)

## Method

Parsed exactly like code/side-keyhunt/repair_parse.py: code/side-keyhunt/repaired_offsets.json + data/upstream-ct_R5005.txt, upstream tokenization [s[i:i+2] for i in range(o, len(s)-1, 2)]. 1,847 pairs, 96 types. Never canonical.py. Never invented data. Every number below traces to this stream.

Tests: (a) full-stream census of the '12 94' bigram on the concatenated pair sequence (row-spanning bigrams included); (b) boundary analysis at both '70 12 94' windows (left fusion with 06/46, right edge at 74/92); (c) rival-segmentation sweep at both windows; (d) re-verification that @64-65 remains the only non-composing '12 94'.

Standing values used: 70='pre' (banked GT), 46='que' (banked GT), 34='i'/29='er'/40='e' (banked GT), 06='ent' (promoted), 12='n' (battery letter-tier promote, pending red-team ratification), 94='ne' (battery promote, pending ratification). 74 and 92: values/classes open.

## Window-level evidence

- W1 — '12 94' census: exactly 3 occurrences stream-wide: @64-65 (row a1_01), @348-349 (row a2_05), @1548-1549 (row a8_00). No row-spanning or additional hits. Confirms the enne-word-64 census byte-exactly.
- W2 — @347-349 (row a2_05): context @343-354 = '43 87 01 06 70 12 94 74 67 78 40 92'. Left of 70 is 06='ent' (promoted). Fusion check: no French word contains "entpre", so 70 cannot attach leftward; 70='pre' is word-initial. Letter composition: "pre"+"n"+"ne" = "prenne" (valid French word, prendre subjunctive).
- W3 — @1547-1549 (row a8_00): context @1543-1554 = '78 43 00 46 70 12 94 92 45 23 99 13'. Left of 70 is 46='que' (banked GT): "que prenne" parses cleanly; "quepre" is not a word, so 70 is word-initial. Same letter composition: "prenne".
- W4 — rival segmentations at W2/W3, all rejected: "pren"+"ne" ("pren" is not a French word); "pre"+"nne" ("nne" is not a word); "pre"+"n"+"ne" as separate words ("n" is not a word); 94 as standalone negator particle leaves "pre n" (ungrammatical). The only grammatical composition is the one-word "prenne".
- W5 — @64-65 (row a1_01): context @59-70 = '41 08 34 29 40 12 94 92 69 13 24 56'. Under banked GT the five pairs @61-65 spell "ierenne"; no French word contains that substring (enne-word-64 family sweep, kill grade, not re-litigated). @64-65 therefore cannot compose word-internally: it is the word-resistant '12 94'.
- W6 — right edges: @349=94 is followed by 74 (value open), @1549=94 by 92 (class open). The right edge of the "prenne" word is not independently fixed by standing values. This does not split the '12 94' pairing: no word boundary can fall between 12 and 94 under any rival composition (W4), so the pairing is word-internal regardless of where the word ends. Recorded as a caveat, not a failure.

## Per-clause pass/fail

- C1 — PASS. @348-349 parses as "prenne": 70 word-initial (W2), 12='n' + 94='ne' as letters inside one word, zero grammatical rivals (W4).
- C2 — PASS. @1548-1549 parses identically: "que prenne" with 70 word-initial (W3), same letter composition, same rival sweep.
- C3 — PASS. The '12 94' census is exactly 3 (W1); the two 'prenne' windows compose word-internally (C1, C2); @64-65 remains the sole window that resists composition (W5, standing kill).

## Adverse

"Conditional on 12='n' + 94='ne' promotions (pending ratification); a red-team overturn re-opens this battery's kill too." — Answered as a stated condition, not a contradiction: no red-team overturn of either promotion is on record (round-18 adjudication is in flight; nothing ruled). This confirm is conditional on both promotions standing, exactly as the bar's parent battery stipulated. If the red team overturns 12='n' or 94='ne', this confirm and enne-word-64's kill both re-open.

## Verdict: CONFIRM (promote)

All three bar clauses pass and the adverse is answered with stated cause. The '12 94' letter-pairing is word-internal ("nne") at both 'prenne' windows; @64-65 is the sole word-resistant '12 94'. Conditional on the pending 12='n' and 94='ne' promotions (adverse above).

## Standing constraints observed

Did not touch R5005, sealed gate instances, or the red-team adjudication queue. No standing red-team verdict contradicted or downgraded. No invented numbers: every offset verified on the repaired 1,847-pair stream.
