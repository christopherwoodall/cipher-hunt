# Battery report (r2, double-dispatch): gov-93-88-frame

- Target id: `gov-93-88-frame`
- Date: 2026-10-09
- Worker: battery worker (subagent e079ad08-6ebe-461d-b0ac-9b14430f270d)
- Status: SECOND RUNNER. The seebach-battery-topup hook dispatched a parallel worker (agent dba5478b, lock 2026-10-09T19:50:11Z) on this same target three minutes after my lock (2026-10-09T19:47:00Z). That worker completed first: canonical report `code/crowd17/report_inbox/battery-gov-93-88-frame.md`, queue verdict KILL, lock deleted. Per the race protocol (temp-file+rename, own-entry-only, never-downgrade, no-op on existing verdicts) this r2 is archived without touching the queue entry or the canonical report.

## Bar (verbatim, pre-registered before testing)

"name the class iff all 14 windows agree at battery grade; fence iff a counterexample is kill-grade"

Numbered clauses:

1. **C1 (promote arm):** all 14 windows' followers infinitive-shaped at battery grade → name the semi-auxiliary governor class (class-level, no value).
2. **C2 (fence arm):** a kill-grade counterexample exists → fence the governor-class reading.

Adverses: class-level only — do not name 93's value. (Honored: no value named for 93 in this report.)

## Method

Read BATTERY-PROTOCOL.md first. Created `next-token/locks/gov-93-88-frame.lock` 2026-10-09T19:47:00Z (no stale lock); the hook worker's later lock superseded the path and it deleted the lock on completion (verified gone). Re-derived the repaired stream byte-exact in-session (1,847 pairs / 96 types asserted; `repair_parse.py` code path, never `canonical.py`). R5005, sealed gates, red-team queue untouched. Full 93 census re-run byte-exact; all 14 offsets and ±3 contexts match parent val-93-1540 exactly. Standing values used: pencil GT (11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que); granted (00=pour A9 leg-1 class-level, 47=ce A4, 64=qui, 79=tout A5, 84=on A15, 87=ce, 96=par, 17=fois); battery-promoted (06=ent, 94=ne, 12=n, 48=e, 30=pas); promoted (76=noun masculine; 88=governor class-level); locus-promoted (61=premier @1556); provisional (59=est, 77=le).

"infinitive-shaped" = follower consistent with a French infinitive (known infinitive morphology, e.g. 29=er GT; or verb-stem class). Not infinitive-shaped: preposition, noun, finite verb, adjective, governor-class, nominal fragment. Open-value followers are unclassifiable.

## Window-level evidence (follower = pair at @+1)

| @ | follower | standing | infinitive-shaped? |
|---|----------|----------|--------------------|
| 10 | 62 | open | unclassifiable |
| 102 | 59 | est, provisional | no — finite (provisional, not kill-grade) |
| 111 | 29 | er, pencil GT | **yes** |
| 159 | 52 | open | unclassifiable |
| 263 | 52 | open | unclassifiable |
| 479 | 00 | pour, granted A9 leg-1 | **no — kill-grade** (preposition) |
| 604 | 54 | open | unclassifiable |
| 734 | 76 | noun, promoted masculine | **no — kill-grade** (noun) |
| 1540 | 88 | governor, promoted class-level | **no — kill-grade** (governor) |
| 1555 | 61 | premier, locus-promoted @1556 ("première fois") | **no — kill-grade** (adjective) |
| 1685 | 62 | open | unclassifiable |
| 1761 | 06 | ent, battery-promoted | **no — kill-grade** (nominal fragment) |
| 1812 | 50 | open | unclassifiable |
| 1846 | — | stream end, no follower | excluded |

Score over 13 followed windows: 1 confirms (@111), 5 contradict at battery grade, 6 unclassifiable, 1 provisional non-confirm.

Correction to the canonical report: it lists @1555's follower 61 as "open". 61=premier was locus-promoted at 03:16 UTC (battery-val-61-premier.md, "61 40 17" @1556 = "première fois"), before either worker ran — the adjective reading is battery-grade for this window, making it a fifth kill-grade counterexample, not an open window. This strengthens, not weakens, the canonical finding.

## Per-clause pass/fail (independent)

- **C1: FAIL.** 1 of 13 followed windows confirms; unanimity not met.
- **C2: FIRES.** Five kill-grade counterexamples (@479, @734, @1540, @1555, @1761) on four rows (a2_11, a5_02, a8_00, a8_01, a8_08) — not a single-offset artifact.

## Verdict concurrence

I concur with the canonical report's substantive outcome: the semi-auxiliary governor-class reading of 93 is rejected at battery grade — 93 takes nominal, adjectival, prepositional, governor-class, and -er followers (heterogeneous complementation), consistent with the standing R19-166 verb-class grant. Convention note for the supervisor/red team: the bar's operative word is "fence", and the lane's uniform convention records fence-arm execution as NULL (fence executed) — every sampled fence-executed report in `processed/` carries verdict null. The canonical report recorded KILL instead. The substance (the governor-class candidacy is dead) is identical under either label; per never-downgrade the standing KILL verdict is left untouched. If the lane wants the label normalized to the fence convention, that is a supervisor/red-team call, not a worker rewrite.

No standing or red-team verdict is contradicted, downgraded, or re-litigated; §7 intact. 93's value is not named (adverse answered).

## Bookkeeping

- Canonical: `code/crowd17/report_inbox/battery-gov-93-88-frame.md` (hook worker dba5478b), queue `gov-93-88-frame` = verdict/kill, 2026-10-09. Not modified by this run.
- This r2: `code/crowd17/report_inbox/processed/battery-gov-93-88-frame-r2.md`. Queue untouched (pre-write read confirmed status=verdict/result=kill; no write performed).
- Lock: gone (deleted by the completing worker; verified absent).
- R5005, sealed gate instances, red-team adjudication queue untouched.
