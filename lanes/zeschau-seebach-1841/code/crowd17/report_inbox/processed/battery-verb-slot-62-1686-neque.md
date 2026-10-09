# Battery report: verb-slot-62-1686-neque

- Target id: `verb-slot-62-1686-neque`
- Claim: resolve the genuinely empty verb slot in the @1686–1694 "62 94 ... 46" (il ne ... que) bracket: name the verb or fence the slot
- Date: 2026-10-09
- Worker: battery worker (subagent df54da45-fd0f-4cee-abf4-54de4181ee09)
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` +
  `code/side-keyhunt/repaired_offsets.json`, parsed per
  `code/side-keyhunt/repair_parse.py`; asserts 1847/96 held in-session).
  `canonical.py` never used. R5005, sealed gate instances, red-team
  adjudication queue untouched.
- Prior: `battery-frame-1688-wide.md` NULL 2026-10-09 (window-level fence;
  follow-up 1 is this target).

Terms (ASD-STE100): "bracket geometry" = adjacent "62 94" followed by a
"46" within 12 groups (the ne...que-shaped span). "Licensed verb" = a
finite-verb value granted or provisional in a standing verdict. "Fence" = a
residual no battery route can close with standing values.

## Standing record adopted (not re-litigated)

- **62="il" is KILLED at kill grade** (R19-097/R19-106; confirmed R20-125).
  The claim's "(il ne ... que)" gloss is unlicensed. This census treats
  "62 94 ... 46" as a pure bracket SHAPE with 62's value/class open.
- **94="ne" is STRONG LEAD, not granted** (R17-001 rejected the promote;
  R19-167, R20-007 confirm). The "ne...que" reading of the span is
  conditional on a lead, not a standing value — recorded, not assumed.
- **59="est" is provisional** (R20-066; standing). The ONLY licensed
  finite-verb value in §7 (all other granted values are non-verbal).
- 46="que" pencil ground truth. 79="tout" granted (A5). 14="en" battery
  promote pending ratification (non-verbal either way). 60 value open;
  27 hapax, class open. §7 intact; no standing verdict contradicted.

## Bar (verbatim, pre-registered before testing)

"name the verb in the @1686-1694 bracket with zero ungranted assumptions;
fence as genuine residual if no clean parse"

Numbered pass/fail clauses (restated before testing, not modified after):

1. **C1 (name arm):** name the finite verb filling the @1686–1694 span using
   zero ungranted assumptions (standing values/frames only).
2. **C2 (fence arm):** else, fence the slot as genuine residual with stated
   cause.

Adverses: none listed. No adverse answers required.

## Method

1. Read BATTERY-PROTOCOL.md first. Created
   `code/crowd17/next-token/locks/verb-slot-62-1686-neque.lock` on start
   (agent id + 2026-10-09T17:06:51Z); no prior/stale lock; deleted on
   completion.
2. Re-derived the repaired stream byte-exact in-session.
3. Census: all 9 "62 94" loci; distance to next 46 (cap 24); distance to
   next 59 (cap 24); interior occupants of each bracket geometry.
4. Tested each bracket span for a licensed finite verb (59="est"
   provisional — the only licensed finite-verb value).

## Census (byte-exact, repaired stream)

All 9 "62 94" loci:

| locus | next 46 | next 59 | context |
|---|---|---|---|
| @100 | +7 | +3 | `62 94 93 59 45 28 00 46 11` |
| @508 | none | +20 | `62 94 64 98 65 88 56 87 77` |
| @761 | none | +2 | `62 94 59 39 88 66 98 80 10` |
| @840 | none | none | `62 94 26 12 16 00 33 96 40` |
| @1329 | none | none | `62 94 70 52 39 83 86 71 64` |
| @1362 | none | none | `62 94 79 14 60 03 30 82 16` |
| @1686 | +6 | none | `62 94 79 14 60 27 46 24 85` |
| @1704 | none | +11 | `62 94 88 26 12 06 29 40 65` |
| @1772 | none | +5 | `62 94 24 87 64 59 19 48 74` |

Bracket geometries ("62 94" + closing 46 within 12): exactly **2** — @100
and @1686.

- @100: `62 94 93 59 45 28 00 46`. Span occupants: 93 (open), **59**
  (provisional "est"), 45 (open), 28 (open), 00 ("pour", A9). A licensed
  finite verb (59="est") sits inside the span.
- @1686: `62 94 79 14 60 27 46`. Span occupants: 79 ("tout", granted,
  non-verbal), 14 ("en", battery promote pending ratification, non-verbal),
  60 (value open), 27 (hapax, class open). **No licensed finite verb.**

Kill check: no window forces the claim false at kill grade; no cleaner
rival value demonstrated on these frames. Not a kill.

## Per-clause pass/fail

1. **C1: FAIL** — no licensed finite verb occupies the @1686–1694 span.
   The only licensed finite-verb value (59="est" provisional) is absent
   from the span (next 59: none within 24). 60 and 27 have no licensed
   verb value; 79 and 14 are non-verbal. Naming one would need an
   ungranted assumption.
2. **C2: FIRES (executed)** — the slot is fenced as genuine residual.
   Stated cause: the @1686–1694 span holds no licensed finite verb under
   standing values. Additionally the bracket reading itself is conditional
   on ungranted 94="ne" (strong lead, R17-001) and the claim's "il" gloss
   is struck (62="il" killed R19-106/R20-125), so even the frame is a
   shape, not a licensed parse.

## Verdict: NULL (fence executed)

The bar's else-arm fired as designed. New finding vs the prior report:
the empty-verb-slot is **window-local, not geometry-wide** — @100's
bracket holds a licensed verb (59="est" provisional) inside its span, so
the geometry CAN host a verb; @1686 specifically cannot under standing
values. The prior report's follow-up-1 question is answered.

The residual re-opens when any of these land: a 60 verb value, 27's
class, 94="ne" moving lead -> grant (red-team decision), or a new
licensed finite verb elsewhere.

## Follow-ups proposed (all verified ABSENT from battery-queue.json)

1. `verb-slot-62-1686-cross100` (P3) — contrast parse: under provisional
   59="est", test whether @100's "62 94 93 59 45 28 00 46" parses cleanly
   as a ne...que bracket. Discriminates isolated-@1686 residual vs a
   geometry that fails even with its licensed verb present.
2. `dep93-102-bracket-role` (P4) — test 93 at @102 (the slot before 59 in
   the @100 bracket) for a licensed dependent role; makes @100 a control
   parse for the geometry.
3. `neque-94lead-gate` (P4) — GATE: re-open the @1686 bracket only when
   94="ne" moves from strong lead to grant (red-team decision). The
   bracket reading is conditional on the lead; do not dispatch until the
   gate fires.

Related already-queued work (not re-proposed): gerund-60-1688,
class-27-independent, neque-tail-24-85-clause, frame-62-94-79-reparse,
val-27-1691-np, 24-redteam-adjudication.

## Bookkeeping

- Report: this file.
- Queue: `verb-slot-62-1686-neque` queued -> `verdict`/`null`, 2026-10-09
  (pre-write assert passed — was queued/verdictless; temp-file + rename;
  JSON re-validated; own entry only; no downgrade).
- Lock created on start, deleted on completion (verified gone).
- R5005, sealed gate instances, red-team adjudication queue untouched.
