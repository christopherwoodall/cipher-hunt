# Battery report: croire-33-noun21

- Target id: `croire-33-noun21`
- Claim: "33-21 x3 asymmetry for dire/croire once 21's value resolves"
- Date: 2026-10-09
- Worker: battery worker (subagent e5fed4fa-5554-4ebc-8bae-5bf3f06860e2)
- Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json`
  + `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`;
  1,847 pairs / 96 types). `canonical.py` never used. R5005, sealed gate
  instances, and the red-team adjudication queue untouched. Lock
  `code/crowd17/next-token/locks/croire-33-noun21.lock` created on start,
  deleted on completion.

## Bar (verbatim, pre-registered before testing)

"re-test '33-21' x3 for a dire/croire asymmetry once 21 resolves; record as gate"

Restated as numbered pass/fail clauses (fixed BEFORE checking data, not
modified after):

- **C1 (trigger):** 21's value has resolved at standing or battery grade.
- **C2 (test):** if C1 holds, re-test '33-21' x3 (@937/@1422/@1631) for a
  dire/croire asymmetry and record the result as a gate.
- **Resolve-arm:** C1 met AND the re-test resolves → resolve. **Else-arm:**
  trigger unmet → NULL with stated cause.

## Method

1. Read BATTERY-PROTOCOL.md first; created/deleted the lock.
2. Checked the standing record on 21's value before touching the stream:
   standing values (§7: 21's class = noun, battery-promoted de-frame-21-class)
   and the most recent 21-value battery.
3. Since the trigger fails (below), no stream re-test was run — C2 is moot,
   not silently rewritten.

## Evidence

### C1: FAIL — 21's value is unresolved, and the battery-grade value search is closed

Standing §7: 21 = noun (class-level, de-frame-21-class promote). Value-level:

- `code/crowd17/report_inbox/processed/battery-val-21-reopen.md` (2026-10-09),
  verdict **KILL**: "The proposition 'a battery-grade value for 21 exists'
  fails at kill grade: @134 forces every noun value false, @109/@359 force
  every masculine value false, and non-noun values contradict the
  battery-promoted noun class. **The battery-grade value search for 21 is
  closed.** This is a search closure, not a class downgrade: 21=noun
  (de-frame-21-class) stands."

So 21's value is not merely open — the battery-grade search that would name
it is closed at kill grade. The target's trigger "once 21 resolves" cannot
fire at battery level. Naming a 21 value now would be a red-team act (naming
a value whose battery search is kill-closed), which per §7 is red-team venue,
not battery venue.

No standing/red-team verdict is contradicted or downgraded; §7 intact.

## Per-clause results

- **C1: FAIL** — trigger unmet; 21's value unresolved and its battery search
  kill-closed (val-21-reopen, 2026-10-09).
- **C2: MOOT** — the re-test is conditional on C1; running it on an unnamed
  21 would re-litigate the closed search, not test the bar.
- **Resolve-arm: not met. Else-arm: TAKEN — verdict NULL (fence with stated
  cause).**

## Fence (stated cause)

The '33-21' x3 dire/croire asymmetry gate is permanently gated at battery
grade: its trigger ("once 21 resolves") is unsatisfiable because 21's value
search is kill-closed. The gate re-opens only if the red team names 21's
value (red-team venue — follow-up 2). The '33-21' x3 windows
(@937/@1422/@1631) remain as evidence; the asymmetry claim itself is neither
promoted nor killed.

## Adverses

- "21's value open - gated, not forced": confirmed and hardened — the value
  search is not just open, it is closed at kill grade. Adverse answered.

## Follow-ups proposed (nulls regenerate work)

1. `dire-33-asymmetry-no21` (P3) — test the dire/croire asymmetry at 33's
   full window set without 21's value: census 33 (n=? on the repaired
   stream), name which windows force dire-shaped vs croire-shaped frames
   independent of 21. If the asymmetry lands without 21, the gate resolves
   anyway; if it is 21-load-bearing, fence it.
2. `croire-33-noun21-redteam-gated` (P4) — gated re-run of THIS bar once the
   red team names 21's value; red-team venue, do not run before.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-croire-33-noun21.md` (this file).
- Queue: `croire-33-noun21` queued → verdict/null, 2026-10-09 (temp-file +
  rename, own entry only; pre-write assert confirmed no prior verdict; JSON
  re-validated post-write).
- Lock created on start, deleted on completion. R5005, sealed gates, red-team
  adjudication queue untouched. No standing verdict contradicted.
