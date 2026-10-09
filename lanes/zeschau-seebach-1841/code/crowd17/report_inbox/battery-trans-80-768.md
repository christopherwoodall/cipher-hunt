# Battery verdict: trans-80-768

- Target: `trans-80-768` (battery-queue.json, priority 3, status queued)
- Claim: Narrow 80's transitivity: test whether 50 (W1), 10 (W2), 22 (W3) can serve as direct objects via their other windows' class evidence; a forced-transitive or forced-intransitive 80 shrinks the infinitive candidate class.
- Parent evidence: val-80-768-inf (NULL, 2026-10-09): W1/W2/W3 object windows.

## Bar (verbatim, numbered)

"name 80 forced-transitive iff a direct object is forced at battery grade, forced-intransitive iff forbidden; else fence"

- C1. Name 80 forced-transitive iff a direct object is forced at battery grade.
- C2. Name 80 forced-intransitive iff a direct object is forbidden at battery grade.
- C3. Else fence.

## Method

1. Read BATTERY-PROTOCOL.md first. Created `locks/trans-80-768.lock` on start (agent 646365c5-4978-4b88-b798-3629e332d07c, 2026-10-09T20:29:00Z); deleted on completion.
2. Re-derived the repaired stream in-session from `code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt` via `repair_parse.py`: 1,847 pairs, 96 types. Asserts held. `canonical.py` never used.
3. Byte-confirmed the three loci and every cited window below. Rendered full distributional profiles: n(50)=11, n(10)=7, n(22)=3, n(80)=17.
4. Per the listed adverse, all class judgments derive from the candidates' OTHER windows only — never from 80's properties.

## Findings

### The three windows (byte-confirmed)

- W1 @441 (a2_09): `46 43 98 80 50 78 41` = "que [43-noun] [98] [80] **[50]** [78] [41]".
- W2 @768 (a5_03): `88 66 98 80 10 22 94` = "[88-gov] [66] [98] [80] **[10]** [22] [94-ne]".
- W3 @1662 (a8_04): `47 98 98 80 22 94 84` = "[47-ce] [98] [98] [80] **[22]** [94-ne] [84-on]".

### Candidate 50 (W1): nominal-capable, NOT forced

50's other-windows class evidence:
- Nominal legs (two, independent): @379-380 `00 11 50` = "pour la [50]" (a2_07); @1263-1264 `11 50 46` = "la [50] que" (a7_02). Determiner directly before 50 in both.
- Bigram check: "11 50" exactly 2x stream-wide (@379, @1263).
- Counter-evidence on uniformity: "50 29" x1 @1565 = "[71] [50]er [24]" (stem-shaped, hapax). 50's class is not uniformly nominal.

50 CAN serve as a direct object (nominal-capable), but is NOT forced at W1: the "[98] [80]" contact is itself unresolved (80 is infinitive-shaped after 98 in three windows with no selected value; "vient [80-INF]" without 'de' leaves the window parse conditional), 50 could attach to 78 or stand in another relation, and no battery-grade elimination of the alternatives exists.

### Candidate 10 (W2): class undetermined, object-worthiness not established

10's other-windows class evidence (n(10)=7):
- "10 29" x1 @617-618 = "[88] [10]er [88]" (a4_00) — stem-shaped, hapax, weak.
- No determiner+10 anywhere; no nominal slot in any of the 7 windows (@326 "71 10 01", @445 "41 10 62", @583 "50 10 19", @617 "88 10 29 88", @1236 "56 10 03", @1648 "31 10 03").
- Class genuinely open. 10's ability to serve as a direct object is UNDETERMINED — neither established nor ruled out.

### Candidate 22 (W3): verb-shaped, CANNOT serve as direct object

22's other-windows class evidence (n(22)=3):
- @1836-1837 `64 22` = "qui [22]" (a8_11). 64='qui' is granted; subject-relative 'qui' forces a finite verb. 22 is verb-shaped here.
- "64 22" exactly 1x stream-wide; 22's predecessors are {10, 80, 64}.
- A finite verb cannot be a direct object. On current class evidence, 22 CANNOT serve as direct object at W3. (A verb/noun polyvalence for 22 would be a new, ungranted assumption.)

### Per-clause results

- C1 (forced-transitive): FAIL. W1's 50 can serve but is not forced; W2's 10 is undetermined; W3's 22 cannot serve. No window forces a direct object at battery grade.
- C2 (forced-intransitive): FAIL. A direct object is not forbidden: 80 is verb-frame class (A8 granted) with open value, and at W1 a nominal 50 keeps transitivity live. Killing one candidate attachment (W3) does not forbid 80 from taking an object.
- C3 (fence): FIRES.

## Verdict: NULL (fence executed)

80's transitivity is unfixed by the W1/W2/W3 object candidates. 50 remains nominal-capable (object-viable, unforced); 10's class stays open; 22 is eliminated as an object candidate on verb-shaped class evidence.

## Scope

- Transitivity of 80 only. Untouched: 80's open value, the A8 verb-frame grant, 98='vient' LEAD, 50's/10's open classes, 22's class (verb leg noted, not banked), §7.
- No standing or red-team verdict contradicted, downgraded, or re-litigated. Canonical-stream caveat stands (row a2_09/a5_03/a8_04 offsets unvalidated).
- Adverse honored: every class judgment above comes from 50/10/22's other windows, never from 80.

## Follow-ups (for supervisor queuing; all verified ABSENT from queue)

1. `do-50-w1-attach` (P4) — resolve the "[98] [80]" contact at W1 (@441); if 80 is fixed as infinitive-shaped and 50 as nominal there, re-test whether "[80] [50]" forces verb+object with the window parse fixed.
2. `class-10-nominal-sweep` (P4) — full class census of 10 (n=7); a nominal leg revives W2's candidate, its absence fences it.
3. `poly-22-redteam-input` (P4, gather-only) — package 22's verb-forcing ("qui [22]" @1836) against its postverbal W2/W3 positions as red-team input on 22's class.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-trans-80-768.md`
- Queue: `trans-80-768` queued -> `verdict`/`null`, 2026-10-09 (pre-write assert passed - was queued/verdictless; target-id-unique tmp `battery-queue.json.trans-80-768.tmp` + atomic rename; disk re-validated; own entry only; no downgrade)
- Lock `locks/trans-80-768.lock`: created on start, deleted on completion (verified gone). R5005, sealed gates, red-team adjudication queue untouched.
