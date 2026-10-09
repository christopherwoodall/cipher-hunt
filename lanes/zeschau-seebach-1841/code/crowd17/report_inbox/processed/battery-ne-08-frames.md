# Battery report: ne-08-frames — "'pas'-slot audit across 08's 18 windows"

Worker: battery-worker-ne-08-frames (7260112a-8e2d-4c96-aed0-236780daa8d1), 2026-10-09.
Lock: created fresh at 2026-10-09T08:33:09Z (no pre-existing/stale lock present).
Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json +
data/upstream-ct_R5005.txt), parsed per code/side-keyhunt/repair_parse.py
(replicated inline; 1,847 pairs asserted; n(08)=18, n(94)=37, n(30)=19).
canonical.py never touched. R5005, sealed gate instances, and the red-team
adjudication queue never touched. All numbers trace to the stream.
Sibling context read first: battery-stem-08.md (null, 2026-10-09) — "se" killed
at kill grade, "on" fenced, "ne" zero legs, spelling-letter killed as
word-internal; this battery is its follow-up #3. battery-prefix-08-31.md
(null, 2026-10-09) — prefix parse survives but does not discriminate.

## Bar (verbatim, pre-registered)

"test whether 08 carries any 'ne' leg via 'pas'-slot analysis over all 18 windows; resolve or fence with stated cause"

## Bar restated as numbered clauses (fixed before testing)

- C1 (pas-slot audit over all 18 windows): every one of 08's 18 windows is
  checked for a "pas"-slot (30="pas", battery-promoted) downstream in a
  "ne...pas" configuration; the reverse audit (all 19 of 30's windows checked
  for a preceding 08) is run for symmetry.
- C2 (resolve or fence with stated cause): either a clean "08 ... 30"
  ne-frame is found (resolving toward ne-legs) or the absence/candidates are
  fenced with a stated grammatical cause.

Discriminator template: the "ne...pas" slot on promoted 94="ne". Calibration:
6 of 37 94-windows have a 30 within 20 pairs on the same row; the tight
grammatical slots are @558 "94 59 30" (n'est pas), @1701 "94 30" (ne pas),
@1713 "94 44 59 30" (ne X est pas). 31 of 37 94-windows have NO downstream 30 —
pas-absence is the norm even for true 'ne', so pas-absence alone is not
kill-grade.

## Method

Enumerated all 18 windows of 08 with same-row distance to the next 30
(max span 20). Enumerated all 19 windows of 30 with same-row distance to the
preceding 08 (max span 20). Parsed every 08...30 hit at slot grade (tight =
within 5 pairs, grammatical "ne S V pas"/"ne V pas" order required). Cross-
checked the @1488/@1520 windows against 24's promoted modal-verb class
(stem-08 follow-up 3 joint).

## Window-level evidence (@-offsets, repaired stream)

08→next-30 (same row, <=20): 15 of 18 windows have NO downstream 30 at all.
Three hits:

- @35 (a1_01): dist 10 — "08 91 39 64 41 01 24 88 43 81 30".
  Span crosses 64="qui" (subordinator, clause boundary) and 24 (promoted
  modal-verb class). Not a tight slot; the pas is three clauses downstream.
- @975 (a6_01): dist 18 — "08 01 00 92 07 76 47 78 45 01 24 89 48 01 76 49
  24 26 30". Span crosses 45="ce" (A11 hold) and 24 x2. Not a slot.
- @1323 (a7_04): dist 4 — "08 62 98 56 30" (tight; the ONLY tight candidate).
  Frame: 29 80 [08] 62 98 56 30 06 62 94 70 52. 62 is subject-shaped
  (62-94 x9 "il ne" anchor). A "ne"-reading requires "ne il <V> pas" —
  subject-after-ne order, ungrammatical. The grammatical parse is
  "08 | 62 98 56 30" = separate word + "il <V> pas". Pas-without-ne is
  well-attested: 24-30 x3, 26-30 x4, 59-30 x2 ("est pas"). So the pas frame
  is closed WITHOUT 08; 08 stands outside it.

Reverse audit (30←preceding-08, same row, <=20): only the same three hits
(@45←10, @993←18, @1327←4). Zero 08-30 direct adjacency (x0). Zero 08-X-30
(x0). No 30 window has 08 as predecessor (30's predecessors: 26 x4, 24 x3,
52 x2, 59 x2, 56 x2, 81, 20, 38, 48, 03, 94 — 08 absent).

Joint 24-class check (stem-08 follow-up 3):
- @1520 (a7_11): "67 [08] 31 24" — a "ne"-reading "et ne [31] pas" would need
  24="pas" to close the slot. 24 is promoted modal-verb class: contradiction
  with stated cause. No 30 downstream on row a7_11 either.
- @1488 (a7_10): "24 87 [08] 31 92 39 24 00" — no 30 on row a7_10.
  The "ne"-parse at the two previously flagged windows dies on the
  promoted 24 class, independent of the 30 census.

08's 18 windows, tight-slot (<=5) pas check, all: only @1323 hits (fenced
above). The other 17 windows have no 30 within 5 pairs downstream.

## Per-clause pass/fail

- C1 (audit over all 18 windows + reverse): PASS. All 18 08-windows and all
  19 30-windows audited. Result: zero clean "08...(V)...30" frames. 15/18
  windows have no downstream 30 within 20; the 3 hits are fenced, not legs.
- C2 (resolve or fence with stated cause): FENCED, not resolved. The single
  tight candidate (@1323 "08 62 98 56 30") requires subject-after-ne order
  ("ne il V pas"), which the language forbids; the grammatical parse leaves
  08 outside a closed pas-frame ("08 | 62 98 56 30", pas-alone attested).
  The two long-span hits cross subordinator/ce/modal material — not slots.
  At @1520, closing the slot needs 24="pas", contradicted by 24's promoted
  modal-verb class. Zero 'ne' legs: the sweep matches stem-08's zero-leg
  result on the anchor frames (62-08 x0, 12-08 x0, 82-08 x0, 08-59 x0,
  08-82 x0) with an independent discriminator.
- Kill grade not met: 31/37 of promoted 94="ne" itself have no downstream 30
  within 20, so pas-absence cannot falsify 'ne'. The discriminator has
  fencing power (the @1323 order inversion, the @1520 24-contradiction) but
  no kill power. Per §5.2 no standing verdict is contradicted.

## Verdict

**null** — the pas-slot audit finds zero 'ne' legs on 08 across all 18
windows: no clean "08...(V)...30" frame parses, the one tight candidate is
order-inverted and fenced with cause, and the @1520 slot-closer is blocked by
24's promoted class. This records the zero-leg sweep as the kill-grade
baseline stem-08's follow-up 3 requested, for any future "ne" claim on 08:
a future claim must produce >=2 clean "ne...(V)...pas" frames or explain
@1323's order inversion and @1520's 24-contradiction. No standing red-team
verdict is contradicted; no escalation. Sibling results ("se" killed, "on"
fenced, prefix null) preserved untouched.

## Follow-ups (nulls regenerate work)

1. **ne-08-verb-slot** — converse template: "ne" must sit immediately before
   its verb. Census 08's successor distribution (31 x3, 65 x2, 62 x2,
   singletons) against 94's verb-slot successors (82 x4, 74 x3, 59 x3, 52 x3,
   92 x2, 24 x2, 76 x2, 79 x2) with frame glosses. Note 65 is the single
   intersection (08-65 x2, 94-65 x1) — value unknown. Bar: resolve iff 08's
   successor class overlaps 94's verb class at >=2 glossed points; else record
   non-overlap as added kill-grade baseline data.
2. **order-control-08-62** — adjudicate "08 62" x2 (@944, @1323): if 62 is
   subject-shaped (62-94 x9), does 08 ever precede a subject+verb frame
   grammatically? Bar: resolve iff a grammatical "08 S V" frame exists;
   else fence both instances with the clause-boundary-before-subject parse and
   record the order rule as a standing fence on any 08="ne" claim.
3. **pas-slot-power-94** — calibrate the discriminator: full adjudication of
   94's 6 downstream-30 frames (clause boundaries, verb glosses) to publish
   the pas-slot power curve. Bar: resolve iff the discriminator separates 94
   from a random-frame baseline at the lane's standard; else retire "pas-slot"
   as a battery discriminator so future workers do not re-run a weak test.
