# Battery verdict: val-94-576-nem

- Target: `val-94-576-nem` (battery-queue.json, priority 3, status queued)
- Claim: test the formula's other window @576-580 ('94 82 06' as 'ne m'ent...' elision frame): does 'ne' parse there
- Adverses: 94='ne' STRONG LEAD intact
- Date: 2026-10-09. Worker: 4f999cca-7cc9-4740-8169-4dca332ed95d (battery worker).

## Bar (verbatim, pre-registered)

"decides whether any deviation cause is window-specific to @1167"

Numbered clauses (frozen before testing):
- C1: 'ne' parses at @576-580 (the '94 82 06' window) at battery grade under standing values.
- C2: The deviation cause is window-specific to @1167 iff the @1167-window anomaly (negator 'ne' without a following verb) does not occur at @576-580.

Offset convention: @n below = 0-based pair index in the repaired 1,847-pair stream. The queue's "@576"/"@1167" name the 55 position 1-based; stream 0-based positions are @576/@1167 for 55, @578/@1169 for 94.

## Method

1. Read BATTERY-PROTOCOL.md first. Created `locks/val-94-576-nem.lock` on start (agent 4f999cca-7cc9-4740-8169-4dca332ed95d, 2026-10-09T20:22:53Z); no pre-existing lock.
2. Re-derived the repaired stream in-session from `code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt` via `repair_parse.py`: 1,847 pairs, 70 rows. Asserts held. `canonical.py` never used.
3. Byte-confirmed both formula windows and all four stream "94 82" windows.
4. Adopted (not re-litigated): 94='ne' STRONG LEAD (R17-001); 82='m' pencil GT; 06='ent' granted-conditional in the "61 94 82 06 06" frame (R17-007, red-team re-derived); 55-61='prend' bare finite stem (seg-55-61-94-letters PROMOTE, 2026-10-09); 87='ce' granted; `nece-1169-revisit` NULL (2026-10-09, "...ne" rescue fenced); `battery-dict-frame-78-45-13-55-61` NULL (2026-10-08, W1 "ne mentent" subjectless / W2 "ne ce" hapax anomaly).

## Window-level evidence

**W1 — @576 window (row a3_02):**
`@575:13 @576:55 @577:61 |@578:94 @579:82 @580:06 @581:06| @582:50`
= "[13] prend(55-61) **ne(94) mentent(82-06-06)** [50] …"
- "mentent" = 82('m') + 06('ent') + 06('ent') = mentir 3pl present, a complete French word. No elision is needed: the claim's "'ne m'ent...' elision frame" phrasing is loose — the byte evidence supports the single-word "mentent" parse, which is the frame the question tests.
- Word-level parse is clean under standing values only: 94='ne' STRONG LEAD, 82='m' pencil GT, 06='ent' granted-conditional (R17-007) for exactly this "61 94 82 06 06" frame. The final 06 is genuinely the 3pl ending (consistent with the 06 promote); the first 06 is stem material.
- Clause-level residual (adopted, not re-litigated): "ne mentent" is subjectless — no banked 3pl subject in @565-578 ("prend" is 3sg; 45/87='ce' singular; 76/80/97/13/52 unbanked). This is W1's own distinct anomaly, not a 'ne'-frame failure.

**W2 — @1167 window (row a6_09):**
`@1166:13 @1167:55 @1168:61 |@1169:94 @1170:87| @1171:83`
= "[13] prend(55-61) **ne(94) ce(87)** [83] …"
- "ne ce" is ungrammatical under 94='ne' + 87='ce' (granted). The 94-87 bigram is stream-unique (1/1,847). The leftward "...ne" rescue ("prenne" via 61='pren') is kill-grade dead (nece-1169-revisit). 'ne' has no verb to negate here.

**Distributional control — all four stream "94 82" windows:**
- @578: 94 82 06 06 → "ne mentent" (3pl) — parses.
- @1182: 94 82 06 06 → "ne mentent" (3pl) — parses (37 77 78 | 94 82 06 06 59 42).
- @1353: 94 82 06 52 → "ne ment" (3sg, m+ent) — parses.
- @1742: 94 82 46 → "ne m que" — does NOT parse as a ne-frame (no verb between ne and 46='que'); a separate residual, out of this bar's scope, noted for the record.
- 3 of 4 "94 82" windows carry a clean "ne ment(ent)" word frame. The frame is productive, not a W1 one-off.

## Per-clause verdict

- **C1 — PASS.** 'ne' parses at @576-580: "ne mentent" is a complete negated finite verb at battery grade with zero ungranted assumptions (94='ne' STRONG LEAD + 82='m' GT + 06='ent' granted-conditional R17-007). The elision reading is unnecessary; the single-word parse is strictly better on the bytes.
- **C2 — PASS.** The deviation causes differ by window. W2's deviation cause — negator 'ne' with no following verb ("ne ce", hapax bigram, rescue fenced) — does not occur at W1, where 'ne' negates a complete finite verb. The "ne-without-verb" deviation cause **is window-specific to @1167**. (W1's own anomaly is clause-level and distinct: subjectless 3pl "mentent".)

## Adverse answered

- "94='ne' STRONG LEAD intact" — answered: intact. W1's parse has 'ne' as the negator (supporting); W2's anomaly is fenced with no rival 94 value posited (nece-1169-revisit); no §7 second value declared.

## Verdict: PROMOTE

Decision recorded: the @1167 deviation cause (ungrammatical "ne ce" — negator without a verb) is window-specific to @1167. The @576 window's 'ne' parses cleanly as "ne mentent"; its residual anomaly (subjectless 3pl verb) is a different, clause-level problem. The two formula windows share the "78 45 13 55 61 94" prefix but are not twins at the ne-frame.

## Scope

- Decides only the window-specificity question for the "94 82 06" vs "94 87" ne-frames at the two formula windows.
- Untouched: 55's/61's global values, the internal "prend" letter-split residual (§7), 94='ne' STRONG LEAD and its caveats, the W1 subjectless-clause problem (adopted NULL), the @1742 "94 82 46" residual (noted, not tested), §7 (no split or second value declared), all standing/red-team verdicts. No standing verdict contradicted or downgraded. Canonical-stream caveat stands (rows a3_02/a6_09 offsets unvalidated).

No follow-ups required (promote, not null).

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-val-94-576-nem.md`
- Queue: `val-94-576-nem` queued → `status: verdict`, `result: promote`, 2026-10-09 (pre-write assert passed — was queued/verdictless; target-id-unique tmp `battery-queue.json.val-94-576-nem.tmp` + atomic rename; disk re-validated; own entry only; no downgrade; no tmp leftover)
- Lock `locks/val-94-576-nem.lock`: created on start (no pre-existing lock), deleted on completion (verified gone). R5005, sealed gates, red-team adjudication queue untouched.
