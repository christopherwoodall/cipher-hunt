# Battery report: envoyer-1232-close

- Target id: `envoyer-1232-close`
- Claim: "Envoyer's @1232 conditional is closed once stem-85 / frame-qui-47 resolve."
- Date: 2026-10-09
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py`; asserts 1847/96 held in-session). `canonical.py` never used. R5005, sealed gate instances, red-team adjudication queue untouched.
- Offsets: 0-based pair indices. Lock: `code/crowd17/next-token/locks/envoyer-1232-close.lock` created on start, deleted on completion.

Terms (ASD-STE100): "doubly-conditional parse" = the "s'envoyer [85]" reading at @1232, which needs two things at once — 47 reading as "se" AND 85 noun-shaped. "Gate" = the two batteries this target waited on. "Kill stands regardless" = envoyer's @1477 kill is independent of both gates' outcomes.

## Bar (verbatim, pre-registered before testing)

"GATED on stem-85 and frame-qui-47 resolving - do not run before. Then: record the resolution outcome against the doubly-conditional parse (47='se' AND 85 noun); confirm it cannot resurrect envoyer (@1477 kill stands regardless)."

Numbered pass/fail clauses (restated before testing, not modified after):

1. **C1 (gate):** stem-85 and frame-qui-47 both have verdicts recorded in `battery-queue.json` → fire; otherwise the target is unrunable.
2. **C2 (47='se' leg):** the resolution kills or removes battery-grade support for 47='se' → the "se" arm of the doubly-conditional fails; else record its live status.
3. **C3 (85-noun leg):** stem-85's resolution is recorded as-is (named value, or NULL with its standing evidence noted) → the "85 noun" arm's status recorded, not decided.
4. **C4 (no resurrection):** @1477's envoyer kill is confirmed independent of both gate outcomes → the @1232 conditional cannot resurrect envoyer.

Adverses listed (queue): "GATED on stem-85 / frame-qui-47 - do not run before; owned by those batteries - coordinate, do not duplicate."

## Method

1. Read BATTERY-PROTOCOL.md first. Created `code/crowd17/next-token/locks/envoyer-1232-close.lock` on start (agent id + 2026-10-09T18:44:00Z); no stale lock; deleted on completion.
2. Re-derived the repaired stream byte-exact in-session (1,847 pairs / 96 types asserted). Re-derived @1232 and @1477 ±4 windows in-session (see below); did not take the parent's bytes on trust.
3. Read the three lane records before testing; adopted, never re-litigated:
   - `battery-rival-porter-envoyer.md` (NULL, 2026-10-08): @1232 window `82-48-29-47-33-29-85-56-10` = "[ce/se] [X]er [85] [56]"; the "s'envoyer [85]" rescue needs 47="se" (ungranted rival, frame-qui-47 owned) AND 85 noun-shaped (stem-85 owned). @1477 `53-60-06-67-33-29-82-16-98` = "veut envoyer me [16]" — kill grade, 16-class-independent, 85-independent. Clause 3 of its bar: "GATED-THEN-MOOT — conditional survival only under (47='se' AND 85 noun-shaped); kill is already secured at @1477."
   - `battery-frame-qui-47.md` (KILL, 2026-10-09): 76/68 verb-hood dead at battery grade; the "qui-47" x2 evidence does NOT support 47='se'; 47="ce" (A4 granted) stands undisturbed.
   - `battery-stem-85.md` (NULL, 2026-10-08): no verb-stem value nameable from bytes; the A3 frame grant's core (3 clean "en [85]" gerund legs) stands; the nominal F2 tension (granted 79="tout" + "tout [85]" x2) is recorded, polyvalence adjudication is red-team venue.
4. Coordination honored: neither gate battery's bar was re-run; only their recorded verdicts were consumed.

## Findings

### C1 — PASS (gate fired)

`battery-queue.json` (re-read in-session): `stem-85` → `status: verdict`, `result: null` (2026-10-08); `frame-qui-47` → `status: verdict`, `result: kill` (2026-10-09). Both gates have verdicts. The target was correctly queued/unrunable until now; it runs now.

### C2 — PASS (47='se' arm dead at battery grade)

The doubly-conditional's "se" arm needed 47 to read "se" — an ungranted rival reading whose only battery-grade evidence was the "qui se [76/68]" windows. frame-qui-47 KILL removes exactly that evidence: 76 is battery-promoted noun ("le [76]" x3), 68 has zero verb legs, so "qui se [verb]" is impossible at both windows. The kill verdict states the "qui-47" x2 evidence "does NOT support 47='se'". 47="ce" (A4, granted) stands undisturbed.

Result: 47='se' at @1232 has no battery-grade support — ungranted value, supporting evidence killed. The "se" arm of the doubly-conditional fails. Even in the best case for the other arm (85 noun-shaped), the conjunction (47='se' AND 85 noun) cannot be realized at battery grade.

### C3 — PASS (85-noun arm recorded, not decided)

stem-85 NULL: 85's value is unnamed. Standing evidence recorded as-is:
- Verb-stem frame evidence: 3 clean "en [85]" gerund legs (the A3 grant's corrected core).
- Nominal tension: "tout [85]" x2 under granted 79="tout" forces a nominal function (F2); any verb-stem naming without polyvalence adjudication contradicts a PROMOTED value's frame → red-team venue (§7, already in flight).

So 85 noun-shaped is neither named nor killed — it remains a live unadjudicated possibility, but with the "se" arm dead (C2), that possibility has no path to the "s'envoyer [85]" parse.

### C4 — PASS (@1477 kill stands regardless of both gates)

- In-session byte check: the @1477 window `53-60-06-67-33-29-82-16-98` contains **neither 47 nor 85** (both absent from @1473–1481). No outcome of stem-85 (85's value) or frame-qui-47 (47's reading) can alter a window that contains neither group.
- The parent battery derived the kill as 16-class-independent (clitic post-infinitive is ungrammatical for every non-causative -er verb in 1841 French under every 16-class) and 85-independent. Neither gate battery adjudicates 16's class.
- Corroboration: the 2026-10-09 `laisser-unique-sweep` battery independently re-confirmed that all seven -er rivals (porter, envoyer, donner, montrer, prouver, trouver, prononcer) die at @1477.
- Therefore the @1477 kill stands regardless; the @1232 conditional cannot resurrect envoyer.

### Per-clause results

- C1 (gate): PASS — both gates have verdicts (NULL + KILL).
- C2 (se arm): PASS — arm fails at battery grade (ungranted, evidence killed).
- C3 (noun arm): PASS — recorded as unadjudicated; no battery-grade path to the conjunction.
- C4 (no resurrection): PASS — @1477 kill confirmed gate-independent.

### Adverse disposition

- "GATED on stem-85 / frame-qui-47 - do not run before": answered — the target waited; gate fired; ran now.
- "owned by those batteries - coordinate, do not duplicate": answered — neither battery's bar was re-run; only recorded verdicts consumed.

### Standing-verdict check

No contradiction with any standing verdict: §7 values, A4 (47="ce"), A3 frame grant, the stem-85 NULL, and the frame-qui-47 KILL are all adopted as recorded. Nothing to escalate on contradiction grounds.

## Verdict: PROMOTE

Envoyer's @1232 conditional is closed at battery grade. The "s'envoyer [85]" rescue's 47='se' arm is dead (ungranted, supporting evidence killed), so the doubly-conditional parse cannot be realized; and the @1477 kill is confirmed independent of both gate outcomes, so no resolution could have resurrected envoyer. This closes the loop opened by rival-porter-envoyer clause 3. The broader rival-elimination ratification (`rival-elim-ratify`) remains red-team's venue.

## Scope

- This target closes the @1232 conditional only. It does not name 85's value, does not re-adjudicate 47's reading beyond the recorded kill, and does not re-litigate @1477 (adopted from rival-porter-envoyer with byte-independence confirmed in-session).
- No red-team verdict touched, downgraded, or contradicted. §7 intact.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-envoyer-1232-close.md` (this file).
- Queue: `envoyer-1232-close` → `status: verdict`, `result: promote`, 2026-10-09 (pre-write assert passed — was queued/verdictless; temp-file + rename; JSON re-validated from disk; own entry only; no downgrade).
- Lock `code/crowd17/next-token/locks/envoyer-1232-close.lock` created on start, deleted on completion (verified gone).
- R5005, sealed gate instances, red-team adjudication queue untouched.
- No follow-ups required (promote, not null). The already-queued `rival-elim-ratify` carries the red-team venue for the broader claim.
