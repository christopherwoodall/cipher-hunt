# Battery report: fin24-1486-parallel

- Target id: `fin24-1486-parallel`
- Claim: force finite-24 at the parallel 'que l'on [24] ce' window @1486 where the subject is available.
- Evidence: battery-form-24-643.md NULL 2026-10-09, follow-up 2.
- Date: 2026-10-09
- Worker: battery worker (subagent e813f846-b512-4d83-859a-8875d30d2e76)
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py`, re-derived in-session; asserts held: 1,847 pairs, 96 types). `canonical.py` never used. R5005, sealed gates, red-team queue untouched.

Terms (ASD-STE100): "finite" = a verb with a person/number (il fait, qu'on fasse). "subject" = the doer of the verb. "non-finite" = infinitive or participle, no person/number. "zero ungranted assumptions" = every value used is banked, promoted, or provisional standing; period grammar does the work.

## Bar (verbatim, pre-registered before testing)

"finite-24 forced at @1486 with zero ungranted assumptions; kill iff forced non-finite; else fence"

Numbered pass/fail clauses (restated before testing, not modified after):

1. **C1:** finite-24 is forced at @1486 with zero ungranted assumptions.
2. **C2 (kill arm):** kill iff the window forces 24 non-finite.
3. **C3 (fence arm):** else fence with stated cause.

Adverses listed: none.

## Method

1. Read BATTERY-PROTOCOL.md first. Created `code/crowd17/next-token/locks/fin24-1486-parallel.lock` on start (agent id + UTC timestamp); deleted on completion. No stale lock was present.
2. Re-derived the repaired stream in-session. Offsets below are 0-based stream indices, the queue @-convention (verified: the "46 77 84 24 87" window lands at 0-based index 1486 exactly, matching the brief's @1486).
3. Standing premises used, not re-litigated: 46='que' (banked pencil GT), 77='le' (provisional), 84='on' (A15 grant), 87='ce' (granted), R17-009 (24 = finite/modal-shaped verb class, value open), R18-008 (24='faire' rejected, demoted to conditional lead; {faire, laisser} open).

## Window-level evidence

- **Locus byte-confirmed:** 0-based @1483–1491, row a7_10: `98 62 | 46(que) 77 84(on) [24] 87(ce) 08 31 92 39`. So `@1483=46 @1484=77 @1485=84 @1486=24 @1487=87 @1488=08 @1489=31 @1490=92 @1491=39`.
- **"que l'on" forced:** 46-77-84 parses as "que l'on" — the established 77-84 'l'on' slot (finder census: 77-84 x7 'l'on'; 46-84 x2 'qu'on'). With 77='le' provisional, "l'" is the only grammatical elision before 'on'; the alternatives ("que le on", "*m'on" under the rival 77='m') are ungrammatical every period. No new assumption: this reading uses banked 46, provisional 77, granted 84.
- **The slot forces a finite verb:** "que" + subject "on" requires a finite verb (indicative or subjunctive) in the slot @1486. Finite includes the modal arm (R17-009) — a modal here is still finite, so the force holds without naming 24's value.
- **Non-finite arms dead at grammar level:**
  - Infinitive: "*que l'on [inf]" is ungrammatical in French of every period.
  - "en"-residual: "que l'on en" — the clitic 'en' needs a finite verb host; with 24='en' the 'que'-clause has no verb at all. Ungrammatical.
- No third rival shape survives the frame.

## Per-clause pass/fail

- **C1 — PASS.** 24 is forced finite at @1486 with zero ungranted assumptions: banked 46, provisional 77, granted 84, granted 87, plus period grammar. Nothing assumed about 24's value, nothing about 08/31/92/39.
- **C2 — does not fire.** No reading forces 24 non-finite; both non-finite arms die at grammar level.
- **C3 — moot.**

## Verdict: PROMOTE (window-level)

24 is finite at @1486 — the 'que l'on [24] ce' window forces it with zero ungranted assumptions. This is the parent `form-24-643`'s missing leg: where the subject ("l'on") is available, 24 is finite. Scope is @1486 only; no 24 value is named (consistent with R18-008; {faire, laisser} stays open). No standing or red-team verdict is contradicted or downgraded: the result agrees with R17-009 (24 = finite/modal-shaped verb class). §7 intact — no polyvalence declared.

## Caveats (stated, not hidden)

- Canonical-stream caveat stands: row a7_10's offset is one of the 68 unvalidated rows.
- The "l'on" reading leans on provisional 77='le' and the A15 grant; both are standing per BATTERY-PROTOCOL.md §7.

## Follow-ups proposed

Promote needs none. One narrow continuation (verified ABSENT from battery-queue.json):

1. `fin24-643-comparison` (P4) — compare the forced-finite @1486 window with the fenced @643 window: isolate exactly which neighbor (20's class vs 24's own frame) blocked the force at @643, now that the @1486 force is proven.

## Bookkeeping

- Queue: `fin24-1486-parallel` → status `verdict`, result `promote`, 2026-10-09 (pre-write assert passed — was `queued`/verdictless; temp-file + rename; JSON re-validated; own entry only; no downgrade).
- Lock `locks/fin24-1486-parallel.lock` created on start, deleted on completion (verified gone).
