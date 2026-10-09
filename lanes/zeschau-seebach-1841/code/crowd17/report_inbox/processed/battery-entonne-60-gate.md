# Battery report — entonne-60-gate

- Target: `entonne-60-gate` (priority 3)
- Claim: "if 60 names as 'on', '06 60 12 48' @1734-1737 = 'entonne' (ent+on+ne) gives Arm A a real word at W5; re-run the W5 parse under '...[56] pas | entonne | ...'"
- Evidence parent: `battery-reseg-3006-w35.md` (null, 2026-10-09) follow-up #3
- Date: 2026-10-09
- Worker agent id: 3b549721-4a22-43fb-8728-30d8705c599d
- Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`), per BATTERY-PROTOCOL.md §3. `canonical.py` not used. R5005 not touched.

## Bar (verbatim)

`'entonne' parses as a verb (3sg or imperative) with its argument frame, or the gate closes`

Numbered clauses:

1. The gate condition is met: 60 is named as 'on' in the current registry
   (a standing verdict promoting 60 = 'on', or the red team ruling 60's value).
2. Under that naming, '06 60 12 48' @1734-1737 decomposes as 'ent' + 'on' + 'ne'
   = 'entonne' (i.e. 06 = 'ent', 60 = 'on', 12+48 = 'ne'-shaped).
3. 'entonne' parses as a verb (3sg or imperative) with a licensed argument frame
   in the W5 window ('...[56] pas | entonne | ...').

## Method

1. Re-read `battery-queue.json` fresh and `locks/` before creating
   `locks/entonne-60-gate.lock` (no verdict present, no fresh lock; lock created
   2026-10-09T20:22:30Z with agent id + UTC timestamp).
2. Checked the registry for any standing verdict naming 60's value as 'on':
   scanned all targets whose claims touch cell 60 (noun-60, adj-60, verb-60,
   verb-60-bare, verb-60-ent, participle-60, participle-60-newvalue,
   dit-60-syncretic, dre-60-rerun, leftedge-60-value, slot-60-at-197,
   sixty-*-census targets, poly-60-redteam, pasde60-redteam-gate, adj-14-tout-gate,
   le14-dependency-rearm, val-27-1691-np, neque-79-rerun-gated, adjudicate-1560-fence).
3. Read the W5 window @1730-1744 from the repaired stream to ground the frames
   the bar would operate on.

## Gate-condition audit

Cell 60 has NO named value in the current registry:

- Kills hold: `noun-60` (kill, 2026-10-08, masculine-noun claim),
  `adj-60` (kill, 2026-10-08, masculine-adjective claim),
  `participle-60-newvalue` (kill, 2026-10-09), `dit-60-syncretic` (kill, 2026-10-09).
- Nulls: `verb-60`, `verb-60-bare`, `verb-60-ent`, `participle-60`,
  `pre-71-60-class`, `val-60-qui-relative`, `seg-94-60-12`, `mood-60-700`,
  `ledit-60-corrob`, `npframe-60-454/690/1674/1366/322`,
  `trans-60-995`, `complement-14-60-27-head`, `ne-scope-62-W7-residual`.
- Promotes do NOT name a value: `split-60-verbs` (distributional split only),
  `slot-60-at-197` (slot naming, value open), `adj-60-2160` (adjective leg at
  '21 60' windows — a parse promote, not a value name), `framecensus-60-redteam-pack`
  (evidence package), `adj-frame-995-solo` (postnominal parse leg).
- The class/value docket `poly-60-redteam` is still `queued` — the red team has
  NOT ruled on 60's class or value.
- The promoted 'on' value in the standing constraints is cell **84** = 'on'
  (A15, conditions C1–C3), not cell 60. No transference is licensed.

Headline: **the gate condition "60 named as 'on'" is not met in the current
registry. The bar cannot be fired — clause 1 fails as a precondition, so
clauses 2–3 are never reached.** Per worker orders: record null, fence the
target.

## Window evidence (for the re-arm)

Repaired stream, row a8_07:

| offset | cell | row |
|---|---|---|
| 1730 | 15 | a8_07 |
| 1731 | 01 | a8_07 |
| 1732 | 56 | a8_07 |
| 1733 | 30 | a8_07 |
| 1734 | 06 | a8_07 |
| 1735 | 60 | a8_07 |
| 1736 | 12 | a8_07 |
| 1737 | 48 | a8_07 |
| 1738 | 52 | a8_07 |

'06 60 12 48' is exactly @1734-1737 as claimed. The sibling W5-adjacent window
under reseg-3006-w35 sits at @1561-1578 ('30 06 60 71 50 29 24 74 62 48 56 32 28
52 82 94 76 76...', row a8_01) — noted for follow-up #3 below. Nothing about
these offsets invents a 60 value; they are reported only so the gated re-arm
can fire on the same frames without re-parsing.

## Per-clause pass/fail

1. Gate condition (60 named 'on'): **NOT TESTABLE / FAILED as precondition** —
   no standing verdict names 60's value; the 'on' promotion belongs to cell 84.
2. '06 60 12 48' = ent+on+ne: **NOT REACHED** (gate closed).
3. 'entonne' verb parse with argument frame: **NOT REACHED** (gate closed).

## Verdict

**null** — gated target, gate closed. This verdict does not contradict any
standing red-team verdict (none exists on 60's value) and is never an
endorsement or rejection of any 60-value candidate.

## Follow-ups (1–3, verified absent from battery-queue.json)

1. `entonne-60-rerun-gated` — re-arm of this exact bar; fires iff the red team
   rules `poly-60-redteam` naming 60's class/value AND the ruled value is 'on'
   or licenses an 'on'-shaped reading of 60. Same frames @1734-1737,
   clauses 2–3 of this bar.
2. `entonne-rival-0660` — fence the fusion: test whether '06 60' @1734-1735
   composes as one word ('en'+'on') under ANY currently ruled standing value
   for 06/60; a negative result under the ruled values kills the entonne
   decomposition even if the gate re-opens.
3. `entonne-sibling-1561` — discriminating frame: re-test the sibling W5 window
   @1561-1578 ('30 06 60 71...') under the 'pas 06 60' boundary shift for a
   competing real-word candidate; if a competing word parses there but nothing
   parses @1734-1737, the entonne arm is unfalsifiable window-shopping rather
   than a word find.

## Anomalies

None. Lock discipline held; queue read fresh at lock time, re-read fresh at
record time; update restricted to this target's own entry via unique tmp name.
