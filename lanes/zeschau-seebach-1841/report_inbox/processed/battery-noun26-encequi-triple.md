# Battery report: noun26-encequi-triple (2026-10-08)

Target: `noun26-encequi-triple`. Lock: `code/crowd17/next-token/locks/noun26-encequi-triple.lock`.
Stream: repaired 1,847-pair parse (data/upstream-ct_R5005.txt + code/side-keyhunt/repaired_offsets.json, parsed per code/side-keyhunt/repair_parse.py). canonical.py never used. R5005 untouched.

## 1. Bar (verbatim, then numbered clauses)

Verbatim bar: "(a) triple re-derived; (b) @1768 'en ce qui [26] [37]' parses with 26 as verb; (c) 37's slot named (object nominal vs clause boundary — coordinate with queued frame-37-reexam, do NOT decide 37's value); (d) 23~26 split respected: 23 = the other verb (value open); 'concerne'/'regarde' family recorded as value LEAD, not claim; (e) the subject-reading rival ('qui [26-subject] [37-verb]') excluded via 59='est' in the identical slot"

Numbered pass/fail clauses (pre-registered before testing):
- (a) The '24 87 64' triple re-derives exactly 3x on the repaired stream with followers 23/26/59 and fol2 37 x2 / 19 x1.
- (b) The window 'en ce qui [26] [37]' (legacy @1768) parses with 26 as the verb of the formula slot.
- (c) 37's slot is NAMED (object nominal vs clause boundary); 37's value is NOT decided; coordination with frame-37-reexam (still queued) is verified.
- (d) The granted 23~26 split is respected: 23 is the other verb, value open; the 'concerne'/'regarde' family is recorded as a value LEAD, not a claim.
- (e) The subject-reading rival ('qui [26-subject] [37-verb]') is excluded via 59='est' in the identical slot.

## 2. Method

1. Re-parsed the repaired stream exactly as repair_parse.py does; forbade canonical.py.
2. Located every '24 87 64' occurrence (0-based stream index), recorded row ids, slot-1 (fol1) and slot-2 (fol2) cells.
3. Re-derived the same triple under the obsolete 1,846-pair parse (a5_03=1) to explain the legacy @-offsets in the queue evidence.
4. Checked slot-1 class by (i) the granted 23~26 split (§7), (ii) the ISLET-10 license for 59 (standing law; class(59)=EST iff pre in {64,94,93} — cited from classification.json and the est-reexam evidence, NOT re-litigated), (iii) the standing noun26-pas-frames PROMOTE (2026-10-08: 26 verb-class unless preceded by 11='la' — cited, not re-derived).
5. Cross-checked 26's class against no other window: this battery tests only the triple windows; 26 elsewhere is owned by queued noun26-gov-frames / noun26-la-frames.

## 3. Window-level evidence (@-offsets, 0-based, repaired stream)

Formula triple '24 87 64' = exactly 3x:

- W1 @179–184 (row a1_05): `24 87 64 23 37 06` — slot-1 = 23, fol2 = 37
- W2 @1766–1771 (row a8_08): `24 87 64 26 37 78` — slot-1 = 26, fol2 = 37
- W3 @1774–1779 (row a8_09): `24 87 64 59 19 48` — slot-1 = 59, fol2 = 19

fol1 distribution: 23 x1 / 26 x1 / 59 x1. fol2 distribution: 37 x2 / 19 x1. No other '24 87 64' exists in the 1,847-pair stream.

Legacy-offset note (no invented numbers): the queue evidence cites @178/@1765/@1773, @1768 (26-cell), @1776 (59-cell), @181 ('en ce qui 23 37 06'). Under the obsolete 1,846-pair parse the triple sits at @179/@1765/@1773, the 26-cell at @1768, the 59-cell at @1776 — i.e. the legacy W2/W3 offsets and slot cells match the OBSOLETE parse, not the repaired stream. Legacy W1 @178 matches NEITHER parse (both give @179); legacy @181 is W1's 64-cell, which is invariant between parses (W1 precedes a5_03). Substance re-derives exactly; only the indices were stale. All @-offsets in this report are repaired-stream 0-based.

Supporting windows (standing-law citations, not new tests):
- 59@1777: pre = 64 ('qui') -> class EST under ISLET-10 (classification.json; est-reexam evidence: "Both sides agree: 1 valid leg, HOLD"). Read: 'en ce qui est [19]'.
- 37 verb-class outside the triple (est-reexam TIER-2, unfenced): '64 37' @676 ('24 80 03 64 [37] 77 45 23 09'), @939 and @1633 (granted 37-01 unit, A12).
- Non-triple '87 64' heads (context only): '29 87 64' @148 (pre 29='er' pencil), '79 87 64' @1800 (pre 79='tout' A5, "tout ce qui"). Different heads, outside this battery's bar; do not force any reading of the triple.

## 4. Per-clause pass/fail

- (a) PASS. Triple re-derived exactly: 3x '24 87 64' (@179/@1766/@1774), fol1 23/26/59, fol2 37 x2 / 19 x1. Legacy @-offsets explained above as obsolete-parse indices; substance identical.
- (b) PASS. W2 = '24 87 64 26 37 78': 87='ce' and 64='qui' are granted, so the slot after 'ce qui' is filled by 23 (W1, verb-class per the granted 23~26 split) and by 59 (W3, licensed 'est' verb per ISLET-10). By frame uniformity across the triple the slot is verbal; 26 parses as the verb. The 'en' gloss of 24 is UNGRANTED working gloss — the slot argument rests on '87 64' ('ce qui') alone, not on 24's value.
- (c) PASS. 37's slot NAMED, value UNDECIDED. 37 immediately follows the verb slot in W1 ('23 37 06') and W2 ('26 37 78'); W3 substitutes 19 ('59 19 48'). Candidate names: (i) object nominal of the formula verb; (ii) clause boundary opening a new predicative clause (compatible with A1's granted predicative frame, value open). Coordination verified: frame-37-reexam is still status=queued, priority 2 — the decision is pending there; this battery names only.
- (d) PASS. The identical verb slot holds 23 once (W1) and 26 once (W2), never jointly — consistent with the granted 23~26 split (A2, §7). 23 = the other verb, VALUE OPEN (no value assigned). Value lead recorded (not claimed): the 'concerne'/'regarde' family is a LEAD for the formula verb slot, unattached — as recorded at finder level (report_inbox/processed/next-token-findings-noun26-frames.md:42,144,293: "leads the 'en ce qui' slot only"). No value claim made here.
- (e) PASS. Rival parse of W2: 'en ce qui [26=subject] [37=verb]'. In the IDENTICAL slot, W3 holds 59 with a licensed 'est' reading (pre=64, class EST — standing law, both sides agree per est-reexam evidence; cited, not re-litigated). A verb cannot fill a subject slot; W1 holds 23 (verb-class per split). If the three windows share one frame type — anchored by the identical 3-group head '24 87 64' — the slot is uniformly verbal and 26 cannot be the subject. The rival would require W2 to be a different construction from W1 and W3 despite the identical head; no evidence for that. Residual fenced: the est-finder's "qui 37" x3 verb-class evidence for 37 makes the rival's 37-as-verb half grammatically available in general, but it does not place 37 as the verb in THIS window.

## 5. Adverses (answered = re-parsed cleanly, fenced with stated cause, or shown a misread — none ignored)

1. 37's predicative grant (A1) vs object slot — FENCED with stated cause: deciding 37's value/slot-role is frame-37-reexam's job (verified still queued, priority 2); not re-litigated here per standing constraints.
2. 37-follower divergence (06 vs 78) — STATED: W1 '...37 06', W2 '...37 78'. FENCED with stated cause: the divergence bears on 37's role, which is deferred to frame-37-reexam; it is compatible with the clause-boundary candidate without deciding it.
3. Single 26 window in the triple — STATED: 26 observed once in the slot (W2). FENCED with stated cause: the claim is class-by-uniformity (3/3 formula windows hold a verb-class cell in the slot), not frequency-based for 26 itself. Independent support: the standing noun26-pas-frames PROMOTE (2026-10-08) places non-'la'-preceded 26 in verb-class; W2's 26 is preceded by 64='qui' (granted), i.e. the verb branch. The open red-team referral on the positional rule (tension with §7 "67 et/veut is the sole true polyvalence") is NOT declared or resolved here — that is red-team territory; noun26-la-frames (still queued) owns the 'la'-side resolution.

## 6. Verdict: PROMOTE

All five bar clauses pass; every listed adverse is fenced with a stated cause. No bar clause fails at kill grade; no window forces the claim false; no cleaner rival value is demonstrated on these frames. No contradiction with any standing verdict: noun26-pas-frames (promote, 2026-10-08) is consistent (W2's 26 takes its verb branch); noun26-la-frames remains queued and untouched; frame-37-reexam remains queued and untouched; the est-reexam's findings are cited, never re-litigated; 37's value, 23's value, and 24's 'en' gloss remain open.

Claim standing after this battery: 26 = verb-class in the '24 87 64' ("en ce qui") formula slot, by frame-type uniformity across the triple. Value of 26 remains open; 'concerne'/'regarde' remains a LEAD, not a claim.
