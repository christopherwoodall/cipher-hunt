# Battery report: coord-637-89gate

- Target id: `coord-637-89gate`
- Claim: Gated re-test of @637's coordinated-adjective parse once the red team rules on 89.
- Date: 2026-10-09
- Worker: battery worker (subagent e46633c6-a713-4bcd-99bd-0656cc86481c)
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py`; asserts 1847/96 held in-session). `canonical.py` never used. R5005, sealed gates, red-team adjudication queue untouched.

Terms (ASD-STE100): "gate" = a test that may run only after a named ruling fires. "LEAD" = red-team class/value finding below full grant. "coord-637" = the @637 coordinated-adjective hypothesis from the parent battery.

## Bar (verbatim, pre-registered before testing)

"resolve iff red team declares 89 adjective-compatible (or adjective/verb polyvalence with a positional rule); then re-parse 'que [60-adj] et le [89-adj]' @637 with zero contradictions."

Numbered pass/fail clauses (restated before testing, not modified after):

1. **C1 (gate trigger):** red team declares 89 adjective-compatible (or adjective/verb polyvalence with a positional rule) → the gate fires.
2. **C2 (re-parse):** iff C1 fires, re-parse 'que [60-adj] et le [89-adj]' @637 with zero contradictions → RESOLVE.

Adverses listed: "GATED on red-team ruling on 89's class - do not run before. A8 verb-frame stands until red team moves; do not re-litigate A8 at battery level."

## Method

1. Read BATTERY-PROTOCOL.md first. Created `code/crowd17/next-token/locks/coord-637-89gate.lock` on start (agent id + 2026-10-09T18:45:00Z); no prior/stale lock; deleted on completion.
2. Re-derived the repaired stream byte-exact in-session (1,847 pairs / 96 types asserted).
3. Checked the gate trigger against the latest red-team round reports (R19, R20) — per the GATE-TRIGGER RULE, a battery verdict alone cannot satisfy a gate; the red-team record is authoritative.

## Findings

### C1 — FAIL (gate trigger fired the opposite way)

The red team did not declare 89 adjective-compatible. It declared the opposite:

- **R19-161 (class-89-adjudicate — GRANT packaging; CLASS DECISION):** "89=noun LEAD (ratified); infinitive rival KILLED." The infinitive/verb rival is KILLED globally (@1375 "pour [86]-er [89] on": "[inf] [inf]" and "[inf] [finite]" both ungrammatical at kill grade). **A positional split is REJECTED under §7** (no kill-grade byte evidence for two classes). Registry: 89 stays ["noun","lead"] — red-team-ratified.
- **R20-084 (frames-80-89 — DUPLICATE / CONFIRM STANDING):** R15-A8 GRANT stands (80/89 verb-frames; 80-vs-89 DISTINCT granted). The task brief's gate note matches: "Gate satisfied: R19-161 ratified 89=noun LEAD, standing at R20-084."

Adjective-compatibility is not just absent — it is the ruled-out arm. The only rescue available to the '[89-adj]' arm would be a positional noun/adjective split at @637, and R19-161 explicitly rejects a positional split under §7. Nothing at battery level can overrule a red-team class decision; §5.2 requires escalation, not override.

### C2 — not executable

The gate trigger failed, so the conditional re-parse arm never engages. Recording the consequence instead:

### @637 window (byte-exact, repaired stream)

Pairs @630–650: `67 08 52 67 63 74 46 60 67 77 89 48 20 24 87 61 88 77 78 52`

The locus of the claimed parse: `@636=46(que) @637=60 @638=67(et) @639=77(le, provisional) @640=89`, i.e. **"que [60] et le [89]"**. The coordinated-adjective hypothesis reads this as 'que [60-adj] et le [89-adj]'. With 89 ratified as noun LEAD, the "[89-adj]" conjunct is ruled out — the same bytes parse cleanly as "le [89-noun]" (DET + noun), consistent with the ratified class.

### Adverses answered

- A8 verb-frame standing: not re-litigated at battery level. R20-084 confirms A8 frame-level (80-vs-89 DISTINCT); the noun LEAD is a class decision on 89's uniform value, and no A8 contradiction is claimed here.
- No red-team verdict contradicted or downgraded: this verdict records the red team's own ruling, it does not oppose it. §7 intact.

## Scope (stated, not hidden)

- This kills the @637 coordinated-adjective parse **via the 89-adjunct arm only**. It does not adjudicate 60's adjective candidacy at @637 or elsewhere (out of scope; belongs to the parent battery's 60 arm).
- 89's value remains unnamed (noun LEAD, not cls); the "89 48" x3 '[89]e' spelling-composition windows are outside this verdict.
- Canonical-stream caveat stands: rows around @637 unvalidated (68/70 offsets).

## Verdict: KILL

The gate trigger fired the opposite way. R19-161 ratified 89=noun LEAD, KILLED the infinitive/verb rival globally, and REJECTED a positional split under §7; R20-084 carries standing. The '[89-adj]' conjunct of 'que [60-adj] et le [89-adj]' @637 is ruled out at red-team grade — the coordinated-adjective parse is dead. No re-run can revive this arm unless a future red-team round re-opens 89's class.

No follow-ups proposed (kill verdict; nulls regenerate, kills close).

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-coord-637-89gate.md` (this file).
- Queue: `coord-637-89gate` queued → `status: verdict`, `verdict: {result: kill, report: code/crowd17/report_inbox/battery-coord-637-89gate.md, date: 2026-10-09}` (pre-write assert passed — was queued/verdictless; temp-file + rename; JSON re-validated; own entry only; no downgrade).
- Lock `code/crowd17/next-token/locks/coord-637-89gate.lock` created on start, deleted on completion (verified gone).
- R5005, sealed gate instances, red-team adjudication queue untouched.
