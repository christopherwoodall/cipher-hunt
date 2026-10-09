# Battery `tail-89-16` — verdict: NULL (trigger unresolved; fence executed)

Target: re-test @1391's '[89] [16]' tail once frame-82-16 names 16's class.
Date: 2026-10-09. Stream: repaired 1,847-pair parse
(`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`,
parsed per `code/side-keyhunt/repair_parse.py`; re-derived in-session, 1,847
pairs / 96 types asserted). `canonical.py` never used. R5005, sealed gate
instances, red-team adjudication queue untouched. Lock
`code/crowd17/next-token/locks/tail-89-16.lock` created on start (agent-session
a4d4acbf-4321-4415-a0ff-0ad7b09cf23e); no prior/stale lock; deleted on
completion.

## Bar (verbatim from brief, pre-registered before data)

"FIRST check the trigger condition — has frame-82-16 named 16's class at
battery grade? If the trigger is still unresolved, verdict NULL (fence) with
stated cause and proposed follow-ups. Only if the trigger is met: resolve iff
the named 16 makes the '[89] [16]' tail parse under noun-89 ('veut [86]er [89]
[16-noun]') or demonstrates the tail as the residual that kills noun-89."

Numbered clauses (pre-registered):

- **C1 (trigger):** frame-82-16 has named 16's class at battery grade.
- **C2 (resolve, conditional on C1):** the named 16 makes 'veut [86]er [89]
  [16-noun]' parse under noun-89, or the tail is demonstrated as the residual
  that kills noun-89.
- **Else:** fence with stated cause (null).

## Method

1. Read BATTERY-PROTOCOL.md first; created and (on completion) deleted the lock.
2. Read `frame-82-16`'s verdict entry in battery-queue.json and its report
   (`report_inbox/processed/battery-frame-82-16.md`).
3. Re-derived the repaired stream in-session (byte-exact per repair_parse.py):
   verified the '[89] [16]' bigram and its locus context.

## Trigger evidence

- `frame-82-16` → `status: verdict`, `result: null` (2026-10-09).
  Bar was "resolve iff 16's class named with the doubled frame parsing":
  clause 1 (class named) FAILED at battery grade; clause 2 (doubled frame
  parses) FAILED (frame unparseable under every class).
- The report's strongest lead is 16 = finite verb, vowel-initial ("a"/"est"
  via "m'"/"n'" elision), but naming it would contradict the standing battery
  verdict `gate-satisfiability-16-85` (promote 2026-10-08, assigned
  16=infinitive); per §5.2 the contradiction was escalated, not overwritten —
  16's class is red-team venue, not battery-named.
- No other battery since has named 16's class: the only 16-class "promote" in
  the queue is `gate-satisfiability-16-85` ("the infinitive gates are
  satisfiable"), which is itself contradicted by frame-82-16's 62-16 x4
  evidence ("on/il [infinitive]" ungrammatical) and awaits red-team
  adjudication. Battery grade has no surviving uncontradicted class for 16.
- Therefore the trigger "frame-82-16 names 16's class" is **unresolved**:
  **C1 FAIL.**

## Locus (byte-verified, re-derived in-session)

- '89 16' bigram occurs exactly **1× stream-wide**: 0b@1393–1394 (row a7_07).
  The brief's @1391 label is window-level (±2 of the locus); the pair itself
  is byte-unique.
- Locus context 0b@1383–1401:
  `65 68 52 82 16 06 29 67 86 29 89 16 76 47 78 48 40 67 77`
  = "...[65] [68] [52] m(82) [16] [06] er(29) veut(67) [86] er(29) [89] [16]
  [76] ce(47) [78] ne(48) e(40)..."
- The bar's formula 'veut [86]er [89] [16-noun]' is the byte-anchored
  @1390–1394 slice `67 86 29 89 16` (veut-positional 67 per §7 rule, "er"
  = banked 29 GT, 16/89 open).

## Per-clause pass/fail

- **C1: FAIL** — trigger unresolved; 16's class unnamed at battery grade
  (red-team venue per §5.2).
- **C2: MOOT** — conditional never armed.
- **Else-arm: TAKEN — fence with stated cause.**

## Fence (stated cause)

The tail '[89] [16]' cannot be tested under the bar's noun-89 formula because
no battery-grade named class for 16 exists: the infinitive promote
(gate-satisfiability-16-85) and the finite-verb lead (frame-82-16) contradict
at the 62-16 x4 windows, and the doubling frame @1195–1198 is unparseable
under every class, so 16 cannot be set to "noun" — the one class the bar's
resolve arm requires. 89's own noun-vs-infinitive conflict is likewise red-team
venue (`class-89-adjudicate`, `noun26-89-class` both verdict/promote =
adjudications pending). No standing or red-team verdict contradicted or
downgraded by this verdict; §7 intact. Canonical-stream caveat stands (row
a7_07 offset unvalidated).

## Follow-ups proposed (all verified ABSENT from battery-queue.json)

1. `tail-89-16-rerun-gated` (P4) — re-run this bar once the red team
   adjudicates 16's class (gated; fires iff named 16 is noun-compatible).
2. `val-86-1391` (P3) — name 86's value at the @1391–1392 '[86]er' locus;
   its value constrains whether '[86]er' can license 89's slot at all.
3. `noun-89-status` (P3) — audit noun-89's standing legs independently of
   this tail; the bar's kill arm needs a residual demonstrated against a
   NAMED 16, which this audit supplies once 16 resolves.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-tail-89-16.md` (this file).
- Queue: `tail-89-16` queued → verdict/null via temp-file + rename, own entry
  only; pre-write assert confirmed no prior verdict; JSON re-validated
  post-write.
- Lock `tail-89-16.lock`: created on start, deleted on completion.
- R5005, sealed gate instances, red-team adjudication queue untouched.
