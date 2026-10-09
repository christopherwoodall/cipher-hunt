# Battery report: name-55-61-core

Target: `name-55-61-core`. Claim: X names as one French word over the 55-61
bigram alone, with 13/43 as a detachable preceding slot.
Date: 2026-10-08. Worker: 131af2da-8f41-431c-968d-0f83d2d8d558 (battery worker).
Lock `locks/name-55-61-core.lock` created 2026-10-09T03:17:21Z (no pre-existing
lock for this id); deleted on completion.

Parent null: `name-13-55-61` (2026-10-08). This battery is its follow-up #1:
it tests only the narrowed 2-pair reading (X over 55-61 alone, 13/43 as a
detachable slot). It does not re-litigate the parent's H1 rejection or
ne-ce-1169's null.

## Bar (verbatim, pre-registered)

"(a) 55-61 bigram census stated x3 (predecessors 13,13,43; successors 94,94,21);
(b) name X iff one French word fits all three 55-61 windows with stated,
consistent 13/43 slot values; (c) coordinate with w1-573-subject (merge if X
is the subject); do not re-litigate ne-ce-1169's null."

## Bar restated (numbered pass/fail clauses; frozen before testing)

1. The 55-61 bigram census matches the bar's figures exactly: exactly x3
   occurrences, with predecessors (13,13,43) in order and successors
   (94,94,21) in order.
2. A single French word X is named if and only if one French word fits all
   three 55-61 windows with stated, consistent 13/43 slot values (the slot
   VALUES must be statable, not just the positions).
3. Coordination with `w1-573-subject` is recorded (merge if X is W1's "ne
   mentent" subject), and ne-ce-1169's null is not re-litigated.

Offset convention: @n = 0-based pair index in the repaired 1,847-pair stream.

## Method

Repaired 1,847-pair stream only: `code/side-keyhunt/repaired_offsets.json` +
`data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`
(stride-2 pairing per row offset). Asserted 1,847 pairs / 96 types before
testing. `canonical.py` never used. R5005 untouched (read-only parse). No
sealed gates, no red-team contact. Every number below was re-derived in-session;
no number is carried over from the parent report.

Standing values used (protocol §7): banked GT 11=la, 82=m, 40=e, 46=que;
granted 87=ce, 47="ce" (allophone tier), 00="pour"; battery-promoted 94="ne"
(STRONG LEAD), 06="ent"; leads 78="ver" (R16-005), 45="dict" (R16-004);
provisional 59="est". 67 et/veut sole true polyvalence with the positional
rule. Values of 13, 43, 55, 61, 21 are open (no battery has named them; §7
grants none).

## Window-level evidence (re-derived)

The 55-61 bigram occurs exactly x3 (full-stream scan):

W1 — 55-61 @576-577 (row a3_02), predecessor @575:13, successor @578:94:
`@572:87 @573:78 @574:45 @575:13 | 55 61 | @578:94 @579:82 @580:06 @581:06
@582:50` = "ce(87) verdict(78-45, LEAD) [13] X ne(94, STRONG LEAD)
mentent(82-06-06, conditional)".

W2 — 55-61 @1167-1168 (row a6_09), predecessor @1166:13, successor @1169:94:
`@1162:21 @1163:67 @1164:78 @1165:45 @1166:13 | 55 61 | @1169:94 @1170:87
@1171:83 @1172:21` = "... 21 et(67, positional) verdict [13] X ne(94)
ce(87)...". The 94-87 "ne ce" bigram is the stream-unique hapax fenced by
ne-ce-1169's null (2026-10-08) — not re-litigated here; it sits outside X's
span.

W3 — 55-61 @1205-1206 (row a7_00), predecessor @1204:43, successor @1207:21:
`@1199:64 @1200:29 @1201:45 @1202:58 @1203:47 @1204:43 | 55 61 | @1207:21
@1208:65 @1209:64 @1210:59` = "... 29 45 58 ce(47, granted) [43] X 21 65 64
est(59, provisional)...". Completely different left frame from W1/W2; this is
the detachable-slot window.

Slot profiles (re-derived):
- 13, n=12: pred {65x3, 69x2, 45x2, 00, 97, 95, 35, 99}; suc
  {24x3, 66x2, 55x2, 93x2, 52, 76, 92}. 13->55 only at W1/W2.
- 43, n=16: pred {37x3, 96x2, 82, 88, 56, 32, 46, 11, 06, 47, 08, 21, 78};
  suc {00x3, 77x2, 87x2, 98x2, 24, 29, 81, 91, 07, 55, 21}. 43->55 only at W3.
- 55, n=12: 11 distinct predecessors ({13x2, 33, 06, 46, 18, 02, 07, 43, 98,
  08, 78}); suc {81x6, 61x3, 83x2, 68}.
- 61, n=18: 15 distinct predecessors ({55x3, 62x2, 89, 37, 20, 49, 87, 17,
  92, 01, 53, 91, 12, 93, 04}); 14 distinct successors, max x2 ({96x2, 59x2,
  94x2, 21x2, 20, 42, 70, 88, 24, 31, 56, 12, 40, 15}) — scattered.
- 21, n=30: top successors 67x8, 62x5, 60x4, 65x4.

## Naming attempt

Clause (b) is a biconditional: name X iff one French word fits all three
windows WITH STATED 13/43 SLOT VALUES. The values are the blocker:

- 13's value is open: 13 occurs 10x without 55, so it is not bound to X; no
  battery has named it; §7 grants nothing. A plural-determiner reading ("les")
  is grammatical under W1 ("ce verdict, les X ne mentent") but unsupported by
  any contact evidence.
- 43's value is open: successor set {00x3, 77x2, 87x2, 98x2, 24, 29, 81, 91,
  07, 55, 21} diverges from 13's (only 24 and 55 overlap). No allophone
  evidence links 43 to 13; §7 grants no 13/43 value; declaring one is a
  red-team act. The slot VALUE therefore cannot be stated, only the slot
  POSITION.
- 55 and 61 values are open; 21's value is open. With all five values open,
  any 2-syllable French plural noun (témoins, hommes, serments, ...) fits the
  frames equally — the candidate space is structurally underdetermined, not
  merely unexplored.

A number-agreement constraint was checked as a possible discriminator: if X
is W1's "ne mentent" subject, X is plural, forcing 13 and 43 to be
number-agreeing determiners in W1/W2 vs W3. Both are grammatical as open
values, so the constraint narrows the future search space but does not force
a candidate — no kill-grade contradiction exists, and none is claimed.

Consequence: the "iff" fails in the naming direction — no French word X is
nameable with evidential support. Not kill-grade: no window forces the claim
false (the frames are consistent with a common X under open values), and no
cleaner rival value was demonstrated on the frames.

## Per-clause pass/fail

1. **PASS.** Census matches exactly: 55-61 x3 (@576, @1167, @1205);
   predecessors (13, 13, 43) in window order; successors (94, 94, 21) in
   window order. All re-derived on the repaired stream.
2. **FAIL (null grade).** No French word X can be named: the 13/43 slot values
   cannot be stated (both values open, no allophone evidence, §7 grants
   nothing), so the biconditional's naming condition is unsatisfied. The
   candidate space is structurally underdetermined. Not kill: no window
   forces the claim false.
3. **PASS.** Coordination recorded: `w1-573-subject` is queued ("W1's 'ne
   mentent' subject identified"); X is unnamed, so no merge is possible now —
   the merge decision is gated on that target's return (see follow-up 2).
   `unit-13-55-61-contact` (verdict null, 2026-10-08) was consulted, not
   duplicated: it tested the unit-level claim, this battery the naming claim.
   ne-ce-1169's null was not re-litigated.

## Adverses answered

- "55's 11 distinct predecessors (weak unit)": confirmed and stated (11
  distinct predecessors listed above); it is the mechanism of the null, not
  an ignored adverse — the scatter blocks value assignment to 55.
- "W2 'ne ce' hapax": fenced with stated cause — 94-87 is a stream-unique
  bigram outside X's span; ne-ce-1169's null (2026-10-08) stands; not
  re-litigated per bar clause 3.
- "61 profile scattered": confirmed (14 distinct successors, max x2) — the
  scatter is what blocks naming X from 61's contacts.
- "coordinate with queued w1-573-subject and queued unit-13-55-61-contact, do
  not duplicate": done — w1-573-subject stays queued (merge gated on its
  verdict); unit-13-55-61-contact is verdict-null and its scope (unit vs
  coincidence) was not re-tested.

No standing red-team verdict is contradicted (§7 values honored; no 13/43/55/
61/21 value declared) — no escalation.

## Verdict: null

Headline: clause 1 passes (census exact); clause 2 unsatisfiable — the 13/43
slot values cannot be stated under §7, so no French word X is nameable over
the 55-61 bigram alone; clause 3 coordinated (merge gated on w1-573-subject).
The detachable-slot reading stays live but unnameable.

## Follow-up targets (null regenerates work; all ids verified absent from the queue 2026-10-08)

1. **x-55-61-candidate-list** (priority 3). Claim: the French candidate space
   for X is enumerable and rankable under the detachable-slot reading. Bars:
   (a) state the grammatical constraints each window imposes on X (number,
   gender if determinable, part of speech); (b) enumerate the candidate
   space with per-window exclusion criteria, killing candidates that fail any
   window's agreement test; (c) if the space collapses to one candidate with
   stated slot values, name X. Evidence: this report (W1/W2: 13+X before 94;
   W3: 43+X before 21; 13/43 values open). Adverses: all five values open;
   ne-ce-1169's null (94-87 frame outside X's span).
2. **merge-gate-w1-x55-61** (priority 2). Claim: the w1-573-subject verdict
   decides whether X merges with W1's "ne mentent" subject. Bars: (a) once
   w1-573-subject returns, state whether its identified subject includes
   55-61; (b) merge if 55-61 is the subject (X inherits the identification),
   else kill the subject-reading of X and re-scope name-55-61-core to the
   W2/W3 frames only. Evidence: this report, clause (c). Adverses: none —
   pure gate.
3. **x-61-94-boundary** (priority 3). Claim: 61's right boundary is tested by
   its 94-successors (2/3 windows). Bars: (a) state 61's successor census
   (94x2 @578/@1169 vs 21x1 @1207, max x2 overall); (b) test whether X should
   be fenced at 61 with 94="ne" as an external negation frame in W1/W2, or
   whether W3's 61-21 break shows the 61 boundary is real; (c) record which
   reading the slot-13-43-compare result supports. Evidence: this report.
   Adverses: 94-87 "ne ce" hapax at W2 (fenced to ne-ce-1169); 21's value
   open.

## Reproducibility

All counts re-derived in-session from the repaired stream (1,847 pairs /
96 types asserted before testing). Analysis script was session-local
(/tmp/n5561c.py); the window dumps and censuses above are the record. No
writes outside this report, the queue edit, and the lockfile (deleted).
