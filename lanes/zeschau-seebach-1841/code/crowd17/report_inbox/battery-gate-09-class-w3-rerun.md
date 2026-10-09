# Battery verdict: gate-09-class-w3-rerun

**Target:** `gate-09-class-w3-rerun` (P3)
**Date:** 2026-10-09
**Worker:** battery worker gate-09-class-w3-rerun (subagent b9977e3c-5788-4ab4-9438-d2a5fcd3598c)

## Bar (verbatim, pre-registered)

"Fire once a 09-class verdict lands from adv-09-1059-1766-value or nom09-open-windows (priority 2 if one promotes, priority 4 if they exhaust with null). Evaluate the dependency in the bar and fence if unmet."

Restated as numbered clauses before testing:
- **C1:** A 09-class verdict lands from adv-09-1059-1766-value or nom09-open-windows → PASS/FAIL.
- **C2:** Priority selection: promote → fire at priority 2; exhaust-with-null → fire at priority 4.
- **C3:** The composition test's own precondition — "09's class has now been granted" (the claim's assertion) — is evaluated; if unmet, the test is untestable as written (fence the gate's dependency, not W3).

## Method

Read BATTERY-PROTOCOL.md in full before touching anything. Created
`locks/gate-09-class-w3-rerun.lock` on start (agent id +
2026-10-09T21:04:12Z), deleted on completion per protocol. Re-derived the
repaired 1,847-pair / 96-type stream in-session from
`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`,
parsed exactly like `code/side-keyhunt/repair_parse.py` (asserts held: 1,847
pairs, 96 types). `canonical.py` never used. R5005, sealed gate instances,
and the red-team adjudication queue untouched. Pre-dispatch check: target had
no verdict and no lockfile.

Standing values used (§7): GT 11=la, 70=pre, 82=m, 34=i, 29=er, 40=e,
46=que; granted 87=ce, 64=qui, 96=par, 17=fois, 79=tout (A5), 00=pour (A9),
84=on (A15, conditions C1–C3), 47=ce (A4); provisional 59=est, 77=le.
Battery-grade (not standing): 98='vient', 94='ne' STRONG LEAD. Kills honored:
09/92 "-ère" value (A6), 09-verb (lon-09-verb), 09~92 hold (A6).

## Gate evaluation

- **adv-09-1059-1766-value** → `status: verdict`, `result: null`
  (report `code/crowd17/report_inbox/battery-adv-09-1059-1766-value.md`,
  2026-10-09). The gate's "exhaust with null" arm FIRES → this re-arm runs
  at priority 4, not priority 2.
- **nom09-open-windows** → still `queued`. The 09-class question is NOT
  exhausted stream-wide.

## Composition-test precondition check

The claim asserts "09's class has now been granted." Tested against the
queue audit (2026-10-09T21:04Z, after the adv landing):

- Every 09-class target with a verdict is `null` (hold-09-92, lon-09-verb,
  noun-09-916, rel-09-290, lon-09-reseg, doublet-589-09-role,
  noun-09-915-value, close-09-1767-rerun, adv-09-1059-1766-value).
- The single 09-related `promote` (split-09-redteam-input) packages split
  evidence and grants NO class.
- adv-09-1059-1766-value's null fenced the *value* ('y' vs 'en'); its class
  finding is that the adverbial-particle arm SURVIVES (not killed, not
  granted). Survival ≠ grant.
- No red-team verdict grants 09 any class (R20 latest; unchanged since the
  parent's 20:23Z audit).

→ **09's class remains ungranted. The composition test ("run the
composition test on '84 09 24' @1765-1767") is untestable as written: there
is no granted role to compose.** Per protocol §2 and the parent's own
precedent (close-09-1767-rerun NULL), recorded as a null finding.

## Window-level evidence (byte-exact, re-derived)

0-based @1764=84, @1765=09, @1766=24, @1767=87, @1768=64 — "on [09] [24] ce
qui [26] …" (1-based @1765-1767 = 84 09 24, row a8_08). 12 09-windows
stream-wide (0-based): [0, 173, 289, 518, 591, 680, 915, 1059, 1223, 1262,
1765, 1820] — unchanged from the parent's audit. No new byte facts.

## Dependency delta (new since the parent)

The parent's composition bar ("'on [09] [24]' closes with zero new
assumptions iff 09's granted role composes") omits a second, live
dependency: **24 is docketed** (24='en' vs finite-modal; `24-redteam-adjudication`
QUEUED). Under the 24='en' rival reading, @1764–1766 re-parses as
"l'on [09] ‖ en ce qui [26]…" (S3, lon-09-reseg; adopted from
adv-09-1059-1766-value F2) — the window is not even an "on [09] [24-fin]"
composition under that reading. So the composition test needs BOTH gates:
09's class granted AND the 24 docket resolved. The current re-arm sequence
(gate-09-class-w3-rerun → val-09-w3-compose) is missing the 24 contingency.
This is recorded as a queue-data note for the supervisor, not re-litigated.

## Scope

This NULL fences only the gate's dependency ("the fire does not supply a
class grant"); it does NOT fence W3 permanently — `fence-w3-terminal` (P4)
remains queued and is the authorized vehicle for the terminal fence once
nom09-open-windows and its spawned follow-ups exhaust. `val-09-w3-compose`
(P3) remains queued. No standing or red-team verdict contradicted,
downgraded, or re-litigated; §7 intact. Canonical-stream caveat stands
(row a8_08 offsets unvalidated).

## Per-clause result

- **C1 PASS.** adv-09-1059-1766-value landed a verdict (null, 2026-10-09).
- **C2.** Fire at **priority 4** (exhaust-with-null arm).
- **C3 FAIL (precondition).** 09's class is not granted; the composition test
  is untestable as written. Recorded per §2 (counts as null).

**Verdict: NULL.**

## Follow-ups proposed (per §4; all IDs verified ABSENT from battery-queue.json)

1. **`w3-composition-joint-gate`** (P4, gated): re-arm the '84 09 24'
   composition test ONLY when BOTH (a) 09's class is granted
   (nom09-open-windows or a later class-grant verdict) AND (b) the 24 docket
   resolves (24-redteam-adjudication); include the S3 "l'on [09] ‖ en ce
   qui…" contingency in the bar so the composition is tested under the
   correct parse of @1764–1766.
2. **`val-09-1060-indep`** (P3): composition test at the OTHER 'l'on [09]'
   window (@1059 0-based = "77 84 09 98…", "l'on [09] vient" under
   battery-grade 98='vient') — independent of the 24 docket, so the 09
   composition question is not held hostage by the 24 adjudication; pass iff
   a granted 09 role composes with zero new assumptions there.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-gate-09-class-w3-rerun.md`
- Queue: `gate-09-class-w3-rerun` → `status: verdict`,
  `verdict: {result: null, report: ..., date: 2026-10-09}` (pre-write assert:
  was queued/verdictless; target-id-unique tmp + rename; own entry only;
  no downgrade).
- Lock: created on start (agent id b9977e3c-5788-4ab4-9438-d2a5fcd3598c +
  2026-10-09T21:04:12Z), deleted on completion.
- R5005, sealed gate instances, red-team adjudication queue untouched.
