# Battery verdict: laisser-85-gate-status — NULL (fence: gates unmet)

- Target: `laisser-85-gate-status` (battery-queue.json, priority 3, status queued)
- Claim: "check whether the 'laisser' lead's gates moved (16's class via frame-82-16; 33's dire/croire tie); if both resolve favorably, re-run the naming bar"
- Parent: none
- Adverses: "'laisser' is LEAD; gates may be open"

## Bar (verbatim, from battery-queue.json)

"name 'laisser' for 85 iff both gates resolve favorably and the value parses across windows with zero kill-grade contradictions"

Numbered clauses (fixed before testing, not modified after):

1. **C1 (gate 1):** 16's class resolves favorably (via frame-82-16 or later 16-class batteries) — i.e. 16's class is nameable at battery grade without contradiction of standing verdicts.
2. **C2 (gate 2):** 33's dire/croire tie resolves favorably — i.e. one of dire/croire is named or the tie is broken at battery grade.
3. **C3 (dependency):** IFF C1 and C2 both hold, re-run the 'laisser'-for-85 naming bar ("the value parses across windows with zero kill-grade contradictions"); ELSE fence the naming re-run with stated cause.

## Method

1. Read BATTERY-PROTOCOL.md in full. Created `locks/laisser-85-gate-status.lock` on start (agent 530d4613-d742-412b-bef0-d0f4bfcf456a, 2026-10-09T21:04:05Z); deleted on completion.
2. Pre-write assert on battery-queue.json: `laisser-85-gate-status` was queued/verdictless. Target-id-unique tmp write.
3. `canonical.py` never used. Repaired stream referenced only for gate-state checks; the core test is a gate-status comparison against the standing battery verdicts (byte-level locus work belongs to the gate batteries themselves, not re-litigated here).
4. Read the current queue verdicts and the following reports in full before deciding:
   - `processed/battery-frame-82-16.md` (NULL, 2026-10-09)
   - `battery-val-16-187-bound.md` (NULL, 2026-10-09)
   - queue verdicts: `gate-satisfiability-16-85` (PROMOTE, 2026-10-08), `dire-33` (NULL), `dire-33-set` (NULL), `croire-33-tiebreak` (NULL), `croire-33-residuals` (PROMOTE, 2026-10-09), `dire-33-asymmetry-no21` (NULL, 2026-10-09)

## Findings

### Gate 1: 16's class — NOT resolved favorably. C1 FAILS.

- `frame-82-16` (NULL, 2026-10-09): killed 16="mais" (conjunction); eliminated "même"/noun/infinitive. The live lead is **16 = finite verb, vowel-initial ("a"/"est" family)** with shape-clean legs (82-16 ×11 "m'a"/"m'est"; 12-16 ×3 "n'a"/"n'est"). BUT it **contradicts the standing battery verdict** `gate-satisfiability-16-85` (PROMOTE, 2026-10-08: single-class assignment 16=infinitive). §5 forbids overwriting — recorded as a class LEAD with escalation, **not a naming**.
- `val-16-187-bound` (NULL, 2026-10-09): conjunction/clause-boundary arm **KILLED at kill grade** (two independent value-independent causes: frame-82-16's "m[16] par m[16]" doubled-frame kill, plus 11/28 "82 16" windows stranding the clitic 'm'); noun KILLED; finite verb FENCED (unnameable, @1481 contradiction unresolved); infinitive FENCED (battery-verdict contradiction — red-team venue).
- **Net:** 16's class is not nameable at battery grade. The frame-82-16 lead (finite "a"/"est") is positive evidence, but it cannot be promoted over the standing `gate-satisfiability-16-85` infinitive verdict without red-team adjudication. Gate 1 has NOT resolved favorably.

### Gate 2: 33's dire/croire tie — NOT resolved favorably. C2 FAILS.

- `dire-33` (NULL, 2026-10-07), `dire-33-set` (NULL, 2026-10-08), `croire-33-tiebreak` (NULL, 2026-10-08), `dire-33-asymmetry-no21` (NULL, 2026-10-09): four NULLs, zero naming.
- `croire-33-residuals` (PROMOTE, 2026-10-09): resolved only the two windows that were ungrammatical under both croire and dire — a residual cleanup, not a tie-break.
- **Net:** neither "dire" nor "croire" is named; the tie is unbroken. Gate 2 has NOT resolved favorably.

### C3 — condition unmet: naming re-run FENCED.

Both gates stand open. The 'laisser'-for-85 naming bar is fenced (evidentiary, re-openable) — the dependency in the bar is unmet, so the naming re-run was not attempted. This fence does not downgrade anything: 'laisser' remains LEAD, and the gate batteries' verdicts stand as recorded.

## Adverses disposition

- "'laisser' is LEAD": HONORED — LEAD untouched, not confirmed or weakened by this battery.
- "gates may be open": CONFIRMED — both gates stand open.

## Scope

Gate-status check only. No 16-class claim, no 33-value claim, no 85-value claim; the frame-82-16 vs gate-satisfiability-16-85 contradiction was adopted (not re-litigated) as the headline fence. §7 intact; no standing/red-team verdict contradicted, downgraded, or overwritten. Canonical-stream caveat stands.

## Follow-ups (§4 — both verified ABSENT from battery-queue.json, left for supervisor)

1. `laisser-85-gate-rerun` (P4) — re-check both 'laisser'-lead gates once either moves: re-arm the naming bar iff 16's class is ratified and/or 33's dire/croire tie breaks at battery grade.
2. `gate-16-class-laisser` (P4, red-team venue note) — feed the frame-82-16 finite-"a"/"est" LEAD vs gate-satisfiability-16-85 infinitive PROMOTE contradiction to the red-team docket; its resolution is the single event that moves gate 1.
3. `gate-33-tie-laisser` (P4) — re-test the dire/croire tie-break at battery grade once `croire-33-noun21-redteam-gated` resolves (queued, red-team venue); its resolution moves gate 2.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-laisser-85-gate-status.md`.
- Queue: `laisser-85-gate-status` → `status: verdict`, `result: null`, 2026-10-09 (pre-write assert passed — was queued/verdictless; target-id-unique tmp `battery-queue.json.laisser-85-gate-status.tmp` + atomic rename; disk re-validated; own entry only; no downgrade; no tmp leftover).
- Lock created on start (no stale lock), deleted on completion (verified gone).
- R5005, sealed gate instances, red-team adjudication queue untouched.
