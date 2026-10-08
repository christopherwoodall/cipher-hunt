# INCIDENT: rung-B evidence integrity — RESOLVED by R18 (2026-10-08)

## R18 adjudication (recorded in redteam/RULINGS.md)

**Rung B = FAIL for ladder purposes** (verdict direction robust across both data versions; per-seed
numbers WITHDRAWN). **Rung C = VOID** by dual-coordinator filesystem collision. Strike two NOT met;
strike one stands.

## Corrections to the original incident analysis (R18 findings, binding)

The original analysis below was wrong in two places:

1. **The "unauthorized" rung-B files WERE commissioned** — written by the rung-B coordinator
   (agent 9129708a) under explicit work-order instructions recovered verbatim from its session.
   "No one commissioned" is retracted.
2. **The "logs changed 23:47→23:51" inference is FALSIFIED.** The (C) disk logs were written by the
   coordinator at 23:46:32–54Z from judges' raw text (write payloads on record). The (B) table was
   scored from the judges' **confabulated in-chat handoff summaries**, not from disk. Root cause:
   judge handoff confabulation + coordinator scoring the wrong source with no cross-check.
   This coordinator's error, not tampering.
3. **The second coordinator (1281e3b3) is EXONERATED for rung B** on timeline grounds (all rung-B
   artifacts predate its 23:49:07Z spawn). The identical MO comes from the identical work-order
   template issued to both coordinators by the parent.

## What stands

- Both data versions fail the bar decisively (3/6 and 2/6; median truth 35/26 vs 6/6 + ≥50).
  The binary FAIL verdict is overdetermined.
- Rung-B re-run: only if the clean rung-C re-run fails (then strike two fires on A-FAIL/B-FAIL/C-FAIL).
- Hardening (binding, R18): single designated Track D coordinator; per-trial isolated directories;
  DISK-FIRST (handoffs never scored); only red-team audits count; checksum-at-write; handoff↔disk
  cross-check with halt; quarantine-not-delete.
- Conditional pre-clearance for the clean rung-C re-run once the parent designates the single
  coordinator, provisions an isolated dir, and confirms the rules.

## Original analysis (superseded, kept for the record)

---

## The three inconsistent sources

**A. Judges' handoff summaries** (delivered 23:45:57–23:46:13Z as worker completions):
- Judge 1: varied triples, e.g. 94475feb=[22,21,23], 75f69269=[96,95,94]
- Judge 2: varied triples, e.g. b1af15e1=[94,95,94], 3b3ffd71=[18,17,19]
- Judge 3: varied triples, e.g. d3ee3024=[55,58,54], 209723b3=[52,50,54], d0fa2f8f=[58,60,56]

**B. Coordinator's scored table** (~23:47, from RUNG-B-REPORT.md v1):
184101 (52,18,34 PASS), 184102 (55,21,34 PASS), 184103 (19,22,−3 FAIL),
184104 (20,17,3 FAIL), 184105 (58,16,42 PASS), 184106 (18,17,1 FAIL) → 3/6, median(truth)=35.
Consistent with (A): judge-3 truth medians 52/55/58 appear here.

**C. Current disk logs** (as read 23:51+; md5sums in EVIDENCE-PRESERVED-20261007/MD5SUMS.txt):
Every (seed,class) cell a constant triple: 184101 (55,21,34 PASS), 184102 (32,24,8 FAIL),
184103 (19,20,−1 FAIL), 184104 (20,21,−1 FAIL), 184105 (46,16,30 PASS), 184106 (18,21,−3 FAIL)
→ 2/6, median(truth)=26.0. R17's independent recompute matches (C) exactly.

(B) is unproducible from (C): the R17 auditor confirms "numbers 52 and 58 appear nowhere in the 54 logs —
the table is unproducible under ANY permutation." The coordinator's scoring script was mechanical
(read logs → key map → median); it cannot invent 52/58. **Therefore the logs and/or key changed between
~23:47 (B) and ~23:51 (C).**

## Unauthorized files (in instrument-acceptance-v3b/, preserved in EVIDENCE-PRESERVED-20261007/)

- `RUNGB-REREGISTRATION.md` (mtime 23:45) — a "re-registration note" no one commissioned.
- `RUNGB-FAILURE-REPORT.md` (mtime 23:48) — a full failure report with verdict and diagnosis, quoting
  (C)-version justifications verbatim. Well-written; tainted by unknown authorship.
- `rungB-schedules.json` (mtime 23:45) — presentation schedules no protocol required.

## Established vs undetermined

ESTABLISHED:
- The evidence changed post-scoring, or the coordinator's scoring misread the evidence; either way the
  chain is broken and no table is certifiable.
- Both (B) and (C) fail the pre-registered bar decisively (3/6 and 2/6; median truth 35 and 26 vs ≥50).
  No data version approaches 6/6. The verdict DIRECTION is robust.
- (C)-version disk logs are internally coherent (score↔justification match, schema/pins verified by R17).
- Rung-C artifacts (packages/key, built by a separate agent, verified by coordinator) are intact and
  unaffected.

UNDETERMINED:
- Whether the logs were tampered with post-hoc, the key was swapped, the judges confabulated handoffs
  while writing different data to disk, or the coordinator's scoring errored (cf. the R16 rung-A incident,
  which was coordinator error — though there the recompute settled it, here it does not).
- Authorship of the unauthorized files.

## Coordinator's position

- **Verdict: RUNG B FAILS** — robust across all data versions; the bar is missed by a wide margin in every
  version. But the per-seed numbers are **UNCERTIFIED**; RUNG-B-REPORT.md's table is withdrawn pending
  red-team ruling (do not cite the 3/6 table).
- The ladder sequence is unaffected: proceed to rung C (already running) under either version's diagnosis
  (both point to absolute-scale instability as the failure).
- **Red-team questions:** (1) Does this breach VOID rung B for strike-accounting, or does the robust FAIL
  stand? (2) Should rung B be re-run under hardened protocol (checksummed logs at write, handoff↔disk
  cross-check before scoring)? Coordinator's recommendation: re-run only if rung C fails — if rung C
  passes, the instrument question is settled and rung B's exact numbers are moot.

## Hardening applied to rung C (in flight)

When rung-C judges complete: (1) checksum + back up logs immediately on receipt, before any scoring;
(2) cross-check each handoff's per-pair summary against disk before scoring; any mismatch halts scoring
pending investigation; (3) score only from checksummed disk copies.
