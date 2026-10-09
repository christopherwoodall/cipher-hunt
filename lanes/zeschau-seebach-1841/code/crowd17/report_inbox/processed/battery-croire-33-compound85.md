# Battery verdict: croire-33-compound85

- Target: `croire-33-compound85` (battery-queue.json, priority 2, status queued)
- Claim: dire-only compound at @1700 (85-33-94-30) once 85's value is named
- Worker: 7407c25d-ebb9-4a24-991a-c90a82774ed0. Date: 2026-10-09.
- Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`; assert 1,847 pairs). `canonical.py` NOT used. R5005, sealed gates, red-team queue untouched.
- Lock: `code/crowd17/next-token/locks/croire-33-compound85.lock` created on start (no stale lock present); deleted on completion.

## Bar (verbatim, pre-registered)

"FIRST check the trigger condition — has 85's value been named at standing/battery grade? If the trigger is still unresolved, verdict NULL (fence) with stated cause and proposed follow-ups. Only if the trigger is met: promote dire iff 85's named value forms a dire-only compound (contredire/medire/redire) with '94-30' parsing; kill the lead iff 85 compounds with neither."

Numbered clauses (fixed BEFORE data):

- **C1:** 85's value is named at standing or battery grade (the trigger).
- **C2:** If C1 passes, promote "dire" iff the named 85 forms a dire-only compound (contredire/médire/redire) with '94-30' parsing.
- **C3:** If C1 passes and C2 fails, kill the lead iff 85 compounds with neither.
- **Gate rule:** If C1 fails, verdict is NULL (fence) with stated cause and 1–3 follow-ups — no promotion/kill attempted.

## Method

1. Read BATTERY-PROTOCOL.md §1–§8 in full before testing.
2. Checked the trigger: scanned `battery-queue.json` (1,012 targets) for any verdict (promote or otherwise) naming a specific value for group 85, and read the standing `stem-85` verdict report (`code/crowd17/report_inbox/processed/battery-stem-85.md`).
3. Byte-verified the locus on the repaired stream (indices below are 0-based pair indices; the brief's "@1700" is index 1699).

## Window-level evidence

### The trigger (C1)

- `stem-85` → **verdict: null** (2026-10-08). Its report exhaustively re-derived all 15 windows of 85 and tested every dire-only compound candidate against them; result: no value named. Key kills inside that report: the "-cier" family (13 stems) died at @97; no surviving candidate reached naming bar.
- Queue-wide scan: **zero** verdicts of any result type (`promote`, `kill`, `null`) in all 1,012 targets name a specific value for 85. A JSON dump scan for `85='...'`/`85="..."`/named-compound patterns in promote verdicts returned the empty set.
- §7 standing values do not include any 85 value; A3 grants only the verb-stem *class* frame for 85, value open.

**C1: FAIL — the trigger is unresolved.** 85's value is unnamed at every grade.

### The locus (byte check, informative only — no bar clause fired)

Index 1699 (row a8_06): `23 91 | 85 | 33 94 30 | 20` — i.e. "85-33-94-30" geometry confirmed byte-exact at indices 1699–1702. The compound geometry exists; the value to insert into it does not. No further testing was attempted per the gate rule.

## Per-clause results

- **C1: FAIL** — 85's value unnamed at standing and battery grade (stem-85 NULL, 2026-10-08; no later naming).
- **C2: MOOT** (trigger-gated).
- **C3: MOOT** (trigger-gated).
- **Gate rule: EXECUTED.**

## Verdict: NULL

The trigger condition fails exactly as the brief's gate anticipated: this is a fence, not a kill — nothing about the dire-only compound geometry is refuted, and no new value was invented to fill it. No standing verdict contradicted or downgraded; §7 intact; canonical-stream caveat stands.

## Adverses

None listed.

## Follow-ups proposed (for supervisor queuing)

1. `val-85-narrow` (P3) — narrower naming battery for 85's value: re-test only the surviving stem candidates from stem-85's report against the 6 surviving A3 frame legs ("en [85]" ×3 clean gerunds + others), with the "que er [85]" order-inconsistency fence honored. Bars: promote iff a value names with ≥2 independent verb-stem frames; kill iff the candidate set empties.
2. `compound85-locus-reread` (P4) — gated re-read of the @1699 locus once follow-up 1 (or `stem-85-then-1700`) names 85: test the full "85-33-94-30" window under the two 30 values. Bars: resolve @1700 iff the named 85 yields a grammatical clause under exactly one of the two 30 values.
3. `ne94-30-frame` (P4) — independent battery on the '94-30' unit at @1701–1702: does "94-30" parse as "ne [30]" (negation + inflected verb) or as part of a compound ending? Bars: decide with ≥2 independent windows; the decision fixes the right half of the @1700 compound geometry.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-croire-33-compound85.md` (this file).
- Queue: `croire-33-compound85` queued → verdict/null via temp-file + rename, own entry only; pre-write assert confirmed no prior verdict; JSON re-validated post-write.
- Lock `croire-33-compound85.lock`: created on start, deleted on completion.
- R5005, sealed gate instances, red-team adjudication queue untouched.
