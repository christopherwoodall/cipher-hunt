# Battery report: order-control-08-62 — adjudicate '08 62' x2 for a grammatical '08 S V' frame

Worker: battery-worker-order-control-08-62 (1c303f0f-e4ce-4d6b-820a-17c1c0a6fb3a), 2026-10-09.
Lock: created fresh at 2026-10-09T13:18:12Z (no pre-existing/stale lock present).
Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json +
data/upstream-ct_R5005.txt), parsed per code/side-keyhunt/repair_parse.py
(replicated inline; 1,847 pairs asserted). canonical.py never touched. R5005,
sealed gate instances, and the red-team adjudication queue never touched.
All numbers trace to the stream.

Provenance: follow-up #2 of battery-ne-08-frames (null, 2026-10-09), which
fenced @1323's '08 62 98 56 30' as requiring ungrammatical 'ne il V pas'
order and proposed this target to test whether 08 ever grammatically
precedes a subject+verb frame.

## Bar (verbatim, pre-registered)

"resolve iff a grammatical '08 S V' frame parses both windows; fence with stated cause if not"

## Bar restated as numbered clauses (fixed before testing)

- C1: a grammatical '08 S V' frame (08 = word heading the frame, 62 = subject,
  98 = verb) parses W1 @944 under standing values/classes only.
- C2: a grammatical '08 S V' frame parses W2 @1323 under standing values/classes only.
- C3: resolve iff C1 and C2 both pass; else fence both instances with stated cause.

## Method

Byte-exact census of the '08 62' bigram stream-wide; ±8 context at both loci
with row-boundary check; '62 94' anchor census re-verified (subject-shape
premise adopted from ne-08-frames); each frame slot tested against standing
grants only (§7 protocol; R19 rulings adopted as premises; §3 bars inventing
values for unvalued cells).

## Window-level evidence (@-offsets, repaired stream)

'08 62' bigram: exactly x2 stream-wide — 0-based @944 (row a5_10) and @1323
(row a7_04); both same-row, no row join within ±8.

- W1 @944 (a5_10) [936..952]: `33 21 64 37 01 07 50 40 | 08 62 98 | 96 86 01 77 86 96`
- W2 @1323 (a7_04) [1315..1331]: `62 48 98 15 24 03 29 80 | 08 62 98 | 56 30 06 62 94 70`

'62 94' anchor: x9 at @100/@508/@761/@840/@1329/@1362/@1686/@1704/@1772
(re-verified byte-exact). 08's successor distribution: 62 x2 (joint max with
31 x3); n(08)=18, n(62)=35, n(98)=40.

Slot audit against standing grants:

- **V slot (98): licensed.** 98 = verb class (R19 promoted; value open, 'vient'
  a lead). Passes at both windows.
- **S slot (62): unlicensed.** 62 is unvalued. 62='il' was killed at kill grade
  (R19) — the only named subject value is dead. 62's class/split is red-team
  venue (redteam-62-split docketed). The '62 94' x9 'X ne' shape is
  distributional only: subject-SHAPE is not a licensed subject CLASS, and
  naming one at battery grade would invent a value (§3) and encroach on the
  red-team docket.
- **08 slot: unlicensed as a word.** 08 is letter-tier (battery-ne-08-frames
  sibling 08-letter-geometry: promote — letter-tier signature stated, adverse
  answered). Word-tier candidates exhausted: 'se' killed at kill grade,
  'on' fenced, 'ne' zero legs across all 18 windows, 'n'-sibling unsupported.
  08 has NO standing word value, so it cannot head a word-level '08 S V'
  frame. The only standing-compatible geometry is a word/clause boundary
  between 08 and 62 ('08 | 62 98'), with 08 attaching leftward as a letter —
  consistent with ne-08-frames' W2 parse ('08 | 62 98 56 30', pas-frame closed
  without 08).

## Per-clause pass/fail

- C1 (W1 @944): FAIL. 08 slot and S slot both unlicensed under standing
  grants; no grammatical '08 S V' parse nameable without inventing values.
- C2 (W2 @1323): FAIL. Same cause. Additionally, under any 08-as-negative
  hypothesis the window forces 'ne il V' order — ungrammatical in 1841 French
  (subject must precede 'ne'); adopted from ne-08-frames, re-verified.
- C3: FENCE EXECUTED with stated cause:
  1. 08 is letter-tier with no standing word value; it cannot occupy the
     word slot heading an S–V frame.
  2. 62 carries no standing subject class (value killed, class is red-team
     venue); the x9 '62 94' subject-shape is evidence, not a license.
  3. Order rule recorded as a standing fence on any future 08='ne' claim:
     '08 62 V' forces subject-after-ne order, which French forbids.

Not kill grade: both failures rest on unvalued cells (08's word value, 62's
class) — a naming act could revive the frame. No standing or red-team verdict
contradicted or downgraded (R19 62='il' kill, 98=verb grant, 94='ne' single
value, §7 sole-polyvalence all adopted as premises).

## Verdict

**null** — fence executed. No grammatical '08 S V' frame parses either window
under standing values/classes.

## Follow-ups (nulls regenerate work; all verified ABSENT from battery-queue.json)

1. **08-wordtier-rerun-gated** (P4) — gated re-fire of this target's C1/C2 iff
   the red team names any word value or class for 08.
2. **62-subject-shape-evidence** (P3) — byte-exact census of all 9 '62 94'
   windows with ±3 context and clause-boundary audit; bar: every window fits
   subject+'ne' with zero ungranted assumptions besides 62's class, else the
   shape is fenced as distributional-only. Evidence only for redteam-62-split;
   §7 — no class declared.
3. **08-leftattach-944-1323** (P3) — test 08 as word-final letter attaching
   leftward at both windows ('40 08' @944, '80 08' @1323); bar: name the host
   word with ≤1 ungranted assumption at both windows, else fence the
   left-attachment route.
