# Battery verdict: prenne-subject-S1545

Target: `prenne-subject-S1545` — the subject of 'pour que ... prenne' @1545 is found, or the clause is genuinely subjectless.
Worker: 7d189dd4-98c6-4028-ac98-b98cfdf6517f. Date: 2026-10-08.
Lock: created 2026-10-08T07:26:46Z. No prior lock existed (locks/ held only NOTE.md). No stale-lock note needed.

## Bar (verbatim, pre-registered before testing)

> resolve iff a subject parse is found under standing values with zero contradiction, else confirm subjectless with stated cause

Numbered pass/fail clauses:
1. A subject parse for the 'pour que ... prenne' clause @1545 is found under standing values with zero contradiction. Verdict: RESOLVE (subject found).
2. Else, the clause is confirmed genuinely subjectless, with a stated cause. Verdict: RESOLVE (subjectless).

## Method

Repaired 1,847-pair stream only: `code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed exactly like `code/side-keyhunt/repair_parse.py` (byte-exact `[s[i:i+2] for i in range(o, len(s)-1, 2)]`). Never `canonical.py`. No invented data. Offsets are 0-indexed pair positions. All counts below trace to the stream.

## Window-level evidence

### Target clause core — @1540-1552 (row a8_00, continuous, no row boundary)

```
@1540 93 | @1541 88 | @1542 77 | @1543 78 | @1544 43 | @1545 00 | @1546 46 | @1547 70 | @1548 12 | @1549 94 | @1550 92 | @1551 45 | @1552 23
```

= "... 93 88 77 78 43 pour que pre-n-ne 92 45 23 ..."
- 00='pour' (A9 class-level grant) + 46='que' (banked pencil GT) = 'pour que'.
- @1547-1549 = 70-12-94 = 'pre'+'n'+'ne' = 'prenne' (3rd-person subjunctive of 'prendre'; composition confirmed by the parent battery, clause 1 PASS, not re-litigated).
- The subject slot between 'que'(@1546) and the verb(@1547) is EMPTY: the two pair positions are adjacent, and 70 is word-internal ('pre' is banked GT, part of the verb word spanning @1547-1549).
- Left context @1532-1544: `00 66 73 41 62 06 21 62 93 88 77 78 43`. The first 'pour' @1532 heads matrix material; the subordinate clause starts at @1545. Nothing left of @1545 can serve as the subordinate subject (see grammar, below).

### Control: the '00 46' census (closed set, stream-wide)

Exactly 4 occurrences of adjacent '00 46' ('pour que'):

1. @(106,107) row a1_03: `00 46 | @108=11 @109=21 ...` = 'pour que la [21] ...'. Slot = 11='la' (banked article) -> overt nominal subject. CLEAN.
2. @(545,546) row a3_01: `00 46 | @547=24 @548=47 @549=46 ...` = 'pour que [24] ce que ...'. Slot OCCUPIED by 24; 24's class is open (gated to queued ne-24-profile) — the subject parse there is unresolved, but the slot is not empty. FENCED to ne-24-profile, not decided here.
3. @(1545,1546) row a8_00: `00 46 | @1547=70 ...` = 'pour que pre-n-ne 92 ...'. Slot holds 70, which is word-internal. The subject slot is EMPTY. THE TARGET.
4. @(1680,1681) row a8_05: `00 46 | @1682=79 @1683=65 ...` = 'pour que tout [65] ...'. Slot = 79='tout' (A5 grant) -> overt subject. CLEAN.

So 2 of 4 windows show a clean overt subject in the slot; 1 has an occupied-but-unresolved slot; the target is the ONLY window where the verb word abuts 'que' directly. The emptiness is anomalous against the construction's own distribution, not a cipher convention.

### Candidate sweep (every grammatical subject position, tested and closed)

- Post-verbal subject: ungrammatical. 'pour que' requires normal S-V order; inversion after 'que' is not licensed in French. The only post-verbal nominal, 92 (@1550), is direct-object-shaped: 'la 92' x3 (11='la' banked) and '92 qui' x2 (64='qui' banked; 92 heads a relative clause) -> noun in object position. CLOSED.
- Elliptical / dropped subject: unlicensed. French does not drop subjects; 'pour que' + subjunctive always takes an overt subject (PRO-control belongs to 'pour' + infinitive, a different construction). CLOSED.
- Subject borrowed from the matrix clause across the subordinator: impossible by definition of the construction — the subordinate subject is independent of the matrix subject. All left-context pairs (@1536-1544: '62 06 21 62 93 88 77 78 43') sit left of the @1545 subordinator and belong to the matrix clause. CLOSED.
- Impersonal 'il' reading of the verb: French impersonals still require an overt 'il' pair; none is present in the clause. (62='il' is demonstrated-not-promoted in any case.) CLOSED.
- 70 standing alone as a subject word: 'pre' is not a French word; 70='pre' is banked pencil GT as a syllable, and the parent battery confirmed the @1547-1549 composition. CLOSED.
- 12-94 re-split into subject material: they complete the verb word 'prenne' (parent clause 1 PASS); no French subject reading survives the split. CLOSED.
- 45 (@1551, 'ce' HOLD A11) as a postposed subject ('... prenne 92 ce'): V-O-S order is ungrammatical in French. CLOSED.
- A different clause boundary (e.g. subject = 43 @1544, '... 43 pour que prenne'): 43 would be the MATRIX subject; the subordinate subject after 'que' is still missing. CLOSED.
- Gapped/parallel subject from a nearby 'pour que' clause: no parallel clause exists nearby (nearest '00 46' is @1680, 135 pairs away); subject-gapping in subordinate clauses is ungrammatical in French regardless. CLOSED.

### '00 46' at @1545 is 'pour que' (over-determined)

00='pour' (A9 class-level grant) and 46='que' (banked GT) are among the most solid values; the verb 'prenne' is unambiguously subjunctive finite (not infinitive 'prendre'), which independently selects a 'que'-type trigger. No rival reading of the subordinator survives.

## Per-clause pass/fail

1. Subject parse found under standing values with zero contradiction: **FAIL** — exhaustive sweep above; every candidate position is closed by French grammar or by standing values.
2. Clause confirmed genuinely subjectless with stated cause: **PASS** — stated cause: (a) the subject slot between 'que'(@1546) and the verb(@1547) contains no pair (adjacent positions; 70 is word-internal); (b) 1840s literary French 'pour que' + subjunctive mandates an overt subject — no PRO, no ellipsis, no postposed/inverted subject, no cross-boundary borrowing, and impersonal readings need an overt 'il' (absent); (c) the only post-verbal nominal (92) is direct-object-shaped; (d) the stream control shows the slot is normally filled (@106 'pour que la [21]', @1680 'pour que tout [65]'), so @1545's emptiness is a genuine anomaly, not a cipher convention.

## Adverses

- "subject slot between 'que' and verb empty" — CONFIRMED as a stated fact, verified pair-adjacent on the repaired stream (@1546=46, @1547=70). Not ignored.
- "if none found, confirm subjectless with stated cause (strengthens the red-team fence)" — DONE. The fence is strengthened, not weakened: the 'prenne' composition spells a correct French word but cannot be integrated into a grammatical clause — exactly the condition the parent null fenced for red-team adjudication. No standing verdict is contradicted: the parent `prenne-70-12-94` null stands unchanged; this follow-up agrees with its subject-search FAIL and narrows the sub-question to a confirmed subjectless reading. No value is promoted by this battery (12='n', 94='ne', 77='le', 59='est' and the 12/94 duality keep their existing statuses).

## Verdict: PROMOTE (claim confirmed via second disjunct)

The bar resolves: the clause is genuinely subjectless with the stated cause above. No follow-up targets are needed — the bar is resolved, not left open. (The queued sibling follow-ups `prenne-92-noun` and `prenne-trigger-348` remain live on their own bars.)
