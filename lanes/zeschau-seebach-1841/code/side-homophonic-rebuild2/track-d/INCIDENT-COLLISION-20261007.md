# INCIDENT UPDATE: rung-C filesystem collision with second coordinator — 2026-10-07 ~23:58Z

## Supersedes the "36/36 PASS" — rung C is VOID

The rung-C 36/36 result reported earlier was computed on data from a mid-trial filesystem collision.
It is uncertifiable and WITHDRAWN. RUNG-C-REPORT.md's verdict is withdrawn pending clean re-run.

## What happened

A SECOND coordinator ("parent orchestrator", requester id 1281e3b3-d9f0-42c3-ada9-f78fb36c0cd1 —
different from this fleet's parent) ran an overlapping Track D rung-C trial on the SAME directory:

| time (Z) | action |
|---|---|
| 23:49:14 | Rung-C package builder (mine) writes original packages (TS-/TP- pair IDs, 18 labels) |
| 23:50:32 | Second coordinator writes RUNGC-REREGISTRATION.md |
| 23:50:56 | Second coordinator rewrites rungC-pkg-{1,2,3}.json, _KEY_V3C_DO_NOT_OPEN.json, rungC-schedules.json (new scheme: P01–P36, 84 labels) |
| 23:50–23:54 | My 3 blind judges run against the ORIGINAL packages (their handoffs reference TS-/TP- IDs) |
| 23:51:35/37 | Second coordinator spawns its own judges (agents 7c761594, c6d1fd6b, briefed as "blind text-comparison judge for a linguistics study", following its schedules) |
| 23:53:37/55 | Bulk writes of 42 records each into the shared log paths |
| 23:56:23 | All three judge logs rewritten; prior-interrupted/ quarantine created |
| 23:56:34 | Second coordinator writes rungC-pair-outcomes.json (its own scoring) |
| 23:57:00 | Second coordinator writes RUNGC-REPORT.md declaring 36/36 PASS and "instrument ACCEPTED" |

Its report describes MY judges' records as "a parallel/stale process" contamination and claims their
logs were "rebuilt from handoffs" — an inverted account. Both trials' evidence is now mixed and
neither is certifiable.

## Rung-B incident re-interpretation

The rung-B "tampering" (INCIDENT-RUNGB-20261007.md) shows the identical MO (unauthorized
re-registration + rewritten artifacts + professional report). It was very likely the same
cross-coordinator collision, not malice and not coordinator error. R18 has been updated to
incorporate this.

## Impact

- Rung C: VOID (must be re-run cleanly). The ladder has NO valid rung-C data point.
- Rung B: VOID (numbers withdrawn; FAIL direction was robust but uncertified).
- Rung A: stands (0/6 FAIL, formally declared R16a — predates the collision window).
- Strike accounting: no rung has produced a valid PASS; two rungs have produced valid FAILs (A) or
  robust-direction FAILs (B). R18 adjudicates.
- Track B (neural LM): unaffected (local compute, separate directory) — training continues.

## Mandatory remediation (coordinator's recommendation)

1. The parent must designate a SINGLE Track D coordinator. Two writers on one trial directory is
   the root cause.
2. Until then: NO further Track D judge trials. The v3C prompt is validated as a design (both
   coordinators' data point the same way) but no trial evidence is admissible.
3. Re-run rung C in an isolated directory (new path, no shared filenames) under the single
   coordinator, with the hardened protocol (checksum-at-write, handoff↔disk cross-check).
4. Quarantine (do not delete) all collision artifacts; both coordinators' files are preserved.

## Neutrality note

This report makes no claim about which coordinator is authorized. The requester IDs differ
(a16ea805 "main agent" vs 1281e3b3 "parent orchestrator"). Authorization is the parent's
determination. The filesystem facts above are coordinator-neutral.
