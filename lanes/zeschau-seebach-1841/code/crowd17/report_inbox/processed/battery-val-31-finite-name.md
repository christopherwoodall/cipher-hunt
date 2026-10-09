# Battery report: val-31-finite-name

- Target id: `val-31-finite-name` (P3)
- Claim: name 31's finite value from the two 'qui [31]' legs (@338 'qui [31] en ce que' with left 'e [03]', @1647 'qui [31] [10] [03] [38] m [16] [01]')
- Adverses: 64='qui' granted requires a finite verb; 31 standalone at both loci
- Date: 2026-10-09
- Worker: battery worker (subagent 73bfea7f-c403-4cea-a77b-b1cb76dd0a64)
- Stream: repaired 1,847-pair / 96-type parse (code/side-keyhunt/repaired_offsets.json + data/upstream-ct_R5005.txt, parsed per code/side-keyhunt/repair_parse.py). 1,847 pairs / 96 types re-derived in-session. `canonical.py` never used. R5005, sealed gate instances, red-team adjudication queue untouched.
- Lock: code/crowd17/next-token/locks/val-31-finite-name.lock (created on start 2026-10-09T16:33:25Z; no prior lock; deleted on completion).

## Bar (verbatim, pre-registered before testing)

"name iff one value parses both windows with zero new assumptions, else fence"

Restated as numbered pass/fail clauses (before testing, not modified after):

1. C1: One specific finite-verb value for 31 parses leg-1's window (1-based @338–346, row a2_05: "qui [31] [14] ce qui par [43] ce [01]" with left "e [03]" @337) with zero new assumptions.
2. C2: The same value parses leg-2's window (1-based @1647–1655, row a8_04: "qui [31] [10] [03] [38] m [16] [01]" with left "e [03]" @1646) with zero new assumptions.
3. C3: If no such value exists, the naming is fenced and the reason is stated.

## Adopted premises (not re-litigated, per §7)

- edge-340-31-14 (recorded verdict/kill, 2026-10-09): leg-1's window (0-based 337–345 = `64 31 14 45 64 96 43 87 01`) is kill-grade ungrammatical under EVERY 31/14 value, with no clause-boundary rescue; the break is the downstream "ce qui par" (@342–344 = 45 64 96 under standing values 45='ce' A11-hold, 64='qui' banked GT, 96='par' promoted), independent of 31's value.
- val-31-verb-test (recorded verdict/null, 2026-10-09): both "qui [31]" legs license finite-verb 31 at battery grade (C1 PASS); the "31 29" stem leg does not (C2 FAIL); no value named. This target is its follow-up #1.
- phase02-a2_05-reseg (recorded verdict/promote, 2026-10-09): the edge kill dissolves under offset-1, but offset-1 is NOT adopted; the canonical stream (offset-0) is the test stream per §3; row a2_05's phase is red-team venue.
- §7 standing values. No red-team verdict contradicted (§5.2 does not fire).

## Method

1. Re-derived the repaired stream in-session (1,847 pairs / 96 types asserted).
2. Byte-located both windows; confirmed "64 31" occurs exactly twice (0-based 337, 1646 → 31 at 1-based @339 and @1648).
3. Tested the bar's promotion condition: candidate finite-verb values against both windows with zero new assumptions.

## Window-level evidence

Leg-1, 1-based @337–@346, row a2_05 (mid-row): `03 64 31 14 45 64 96 43 87 01`
= "e [03] **qui [31]** [14] ce qui par [43] ce [01]".

Leg-2, 1-based @1646–@1655, row a8_04 (mid-row): `03 64 31 10 03 38 82 16 01 56`
= "e [03] **qui [31]** [10] [03] [38] m [16] [01] [56]".

## Per-clause pass/fail

1. **C1 — FAIL at kill grade.** Leg-1's window is a sub-window of the edge-340-31-14 killed window (`64 31 14 45 64 96 43 87 01`, 0-based 337–345). That kill is value-independent: no 31 value, no 14 role, and no clause-boundary placement parses the sequence, because the structural break ("ce qui par" at 0-based 340–342 under banked/promoted values) lies downstream of 31. Any parse of leg-1's claimed window must extend through this dead sequence. Therefore NO value of 31 parses leg-1's window — the bar's promotion precondition is forced false by the window itself.
2. **C2 — conditional pass, moot.** Leg-2's window shows no structural break under standing values and is consistent with finite-31 (adopted from val-31-verb-test C1 leg-2). But the bar requires the SAME value to parse BOTH windows; since C1 admits no value, C2 is moot.
3. **C3 — fires.** Naming is fenced: (a) no specific finite-verb VALUE for 31 is derivable with zero new assumptions — the only battery-grade material is the class-level finite-verb licensing (adopted, not renamed); naming e.g. "31 = fait/est/dit" would be a new assumption; (b) leg-1's window is value-independently dead, so the naming-from-both-legs target cannot promote on the canonical stream.

## Adverses

- "64='qui' granted requires a finite verb": answered — consistent with the adopted class-level finding (finite-verb 31 licensed at both legs, val-31-verb-test C1). The adverse does not supply a value.
- "31 standalone at both loci": answered — byte-confirmed: leg-1 neighbors `64 [31] 14`, leg-2 `64 [31] 10`; no standing verdict licenses a word-internal "31-X" reading at either locus.
- Task-brief framing note: the brief's "en ce que" reading of 14 45 64 contradicts granted 64='qui' — the correct reading is "en ce qui", which is exactly the material of the edge-340-31-14 kill. The claim's framing contains the dead trigram.

## Phase caveat (stated, not hidden)

This kill holds on the canonical repaired stream per protocol §3. Under offset-1 the edge kill dissolves (phase02-a2_05-reseg, promote, conditional), but offset-1 is not adopted and row a2_05's phase is red-team venue — the kill dissolves only if the red team re-phases a2_05. Same mechanism class as seg-a1_01 / reseg-1481-98.

## Verdict: KILL

No value parses both windows: leg-1's window forces the bar's precondition false at kill grade, value-independently (standing verdict edge-340-31-14, recorded). The finite-value naming is fenced; no value named. This does not contradict or downgrade any standing verdict — it rests on edge-340-31-14's kill and adopts val-31-verb-test's finite-class licensing.

## Follow-ups

None newly proposed: §4 mandates follow-ups for nulls only. The 31 program continues through already-queued siblings `val-31-1257-word` and `val-31-1516-finite` (both status queued in battery-queue.json). The "name 31's finite value from both legs" line is fenced on the canonical stream; the phase-dependent re-open is red-team venue (phase02-a2_05-reseg).

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-val-31-finite-name.md`
- Queue: `val-31-finite-name` → `status: verdict`, `result: kill`, 2026-10-09 (temp-file + rename; own entry only; pre-write assert: was queued, verdictless; no downgrade)
- Lock deleted on completion. R5005, sealed gates, red-team queue untouched. `canonical.py` never used. No invented numbers.
