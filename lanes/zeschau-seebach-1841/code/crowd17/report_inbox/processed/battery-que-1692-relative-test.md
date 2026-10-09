# Battery verdict: que-1692-relative-test

- Target: `que-1692-relative-test` (battery-queue.json, priority 3, status queued)
- Claim: "Test whether 'que [24] [85]...' at @1692 parses as a relative clause (24 finite + mood; 85/58 as its dependents). A relative reading forces 27 nominal (antecedent) - the forcing leg this battery could not supply"
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py`; re-derived in-session, asserts held). `canonical.py` never used.

## Bar (verbatim, pre-registered BEFORE testing)

> Relative iff the clause parses with zero ungranted assumptions besides 27's class

Numbered clauses (fixed before testing, not modified after):

- **C1:** 27's class (nominal antecedent) is the ONLY assumption used.
- **C2:** The clause "que [24] [85] [58]..." at @1692 parses as a relative clause with zero additional ungranted assumptions.

## Window (byte-exact, asserts held in-session)

0-based @1689–1699, rows a8_05/a8_06:

`14(?) 60(?) [27(?)]@1691 [46=que]@1692 [24=verb-cls]@1693 [85=verb-stem]@1694 [58=nominal]@1695 15(?) 23(verb) 91(?) 85(?)`

Full tail: `... 85 33(INF) 94(ne-lead) 30(pas) 20(?) 62(?) 94(ne) 88(gov) 26(noun-lead) 12(n) 06(ent)`.

27 is hapax (n=1 stream-wide). '24 85' bigram is 5x (@732/@955/@1438/@1693/@1754); '85 58' is 3x (@54/@1694/@1755).

## Findings

**C1 — PASS (by grant).** 27 nominal taken as the bar's single allowed assumption. (27's class is otherwise live work: `dep27-1691-role-narrow` queued, `val-27-1691-np` queued/gated on poly-60-redteam, `class-27-independent` NULL — none contradicted here.)

**C2 — FAIL.** The relative parse needs TWO further assumptions, both ungranted:

1. **24 finite at @1693 — red-team venue, not grantable.** 24's class is under a standing mutual-kill escalated to the red team: `battery-24-en-verb-conflict` (2026-10-09) returned NULL/escalate — 6 windows kill 24='en', 4 windows kill 24=verb, §7 bars the polyvalence synthesis. Neither the finite-modal-verb class (`ne-24-profile` promote) nor the 'en' gerund frame (`en85-gerund-reaudit` promote) is usable as a premise at @1693. "24 finite" is therefore an ungranted assumption, and the claim's "24 finite + mood" framing cannot even start — mood is moot with the class unresolved.

2. **85's role after a finite 24 — ungranted.** Even hypothetically granting finite-24, "que [24] [85] [58]" does not parse: 85 is verb-stem (A3 frame); a bare stem cannot follow a finite verb in French. The escape routes are (a) 85 as a non-finite dependent (infinitive/participle — unlicensed; the licensed infinitive shape is "85 33", seen x1 elsewhere, not here), or (b) 85+58 composing as one word (no segmentation license in standing record). Both are ungranted assumptions.

Corroborating negatives:
- 'que' as subject relative pronoun is ungrammatical in French (subject = 'qui'); the object reading is required, which needs 24 finite AND transitive — compounding blocker (1).
- The @954 '46 24 85' parallel ("96 87 46 24 85 04...") does not transfer a relative parse: there 'que' is the complementizer after 'ce' ("ce que"), a complement clause, not a relative.
- The @1754 '24 85 58' twin ("89 26 24 85 58 17...") has no 'que' at all, confirming "24 85 58" is a freestanding frame whose parse does not depend on a relative 'que'.

## Verdict: NULL (epistemic, not substantive)

The relative reading is NOT established — C2 fails on two ungranted assumptions. This is not a KILL: no window forces the relative reading false. Blocker (1) is red-team venue (24's class genuinely open); if the red team adjudicates 24 as finite verb AND 85's post-finite role resolves, the relative parse re-opens. The null regenerates as the follow-ups below.

Adverses: none listed on the target. The discovered adverse — the 24-class mutual kill — is answered as red-team venue (adopted, not re-litigated).

## Follow-ups proposed (both verified ABSENT from battery-queue.json)

1. `rel-1692-24finite-revisit` (P4) — re-arm gated on red-team resolution of 24's class (24-en-verb-conflict escalation): revisit the relative parse of "27 que [24] [85] [58]..." with 24's adjudicated class; 27 nominal remains the only other assumption.
2. `role-85-postfinite` (P3) — name 85's grammatical role after finite-verb-shaped 24 across all five '24 85' windows (@732/@955/@1438/@1693/@1754): non-finite dependent vs composition with follower vs re-segmentation. Discriminates blocker (2) independently of 24's class.

## Scope

Window-level only. Untouched: the 24-class conflict (red-team venue, not re-litigated), 27's class (live queued targets), 85's frame (A3), 58's nominal class, §7 (no polyvalence declared). Canonical-stream caveat stands (rows a8_05/a8_06 offsets unvalidated; pencil gloss is on a5_03).

## Bookkeeping

- Queue: `que-1692-relative-test` queued → `verdict`/`null`, 2026-10-09 (pre-write assert passed — was queued/verdictless; target-id-unique temp file `battery-queue.json.que-1692-relative-test.tmp` + atomic rename; disk re-validated; own entry only; no downgrade).
- Lock `locks/que-1692-relative-test.lock`: created on start (agent 3ec980ed-d3c3-48f0-86ce-0dd88ceadc25, 2026-10-09T19:20:00Z; no stale lock), deleted on completion (verified gone).
- R5005, sealed gates, red-team adjudication queue untouched. No standing/red-team verdict contradicted or downgraded.
