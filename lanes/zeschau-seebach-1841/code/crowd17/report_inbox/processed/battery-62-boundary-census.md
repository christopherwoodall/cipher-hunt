# Battery report: 62-boundary-census — full 35-window boundary census of 62

Worker: subagent 5e899087-9082-4265-b5cd-c09fcfa796f9, 2026-10-09.
Lock: created fresh at 2026-10-09T14:18:51Z (no pre-existing/stale lock present).
Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json +
data/upstream-ct_R5005.txt), parsed like code/side-keyhunt/repair_parse.py
(replicated inline; asserts held: 1,847 pairs, 96 types, n(62)=35).
canonical.py never touched. R5005, sealed gate instances, and the red-team
adjudication queue never touched. All numbers trace to the stream.

Provenance: follow-up #3 of battery-08-62-boundary-adjudication NULL
(2026-10-09). §7 adverse honored throughout: evidence only — no class,
split, value, or polyvalence declared or named anywhere in this report.

## Bar (verbatim, pre-registered)

"every boundary claim stated with standing-licensed grounds or marked
undetermined"

## Bar restated as numbered clauses (fixed before testing)

- C1: all 35 windows of 62 censused with ±3 context, row, and free-word
  adjacency status — every boundary claim grounded on a standing rule or
  marked UNDETERMINED.
- C2: the '62 94' anchors censused byte-exact; every anchor claim grounded
  or marked undetermined.
- C3 (§7 adverse): no class, split, or polyvalence declared — evidence
  package only.

## Standing boundary rules adopted (never re-litigated)

From battery-08-62-boundary-adjudication: a word boundary is FORCED
after/before a banked/promoted free word
(11=la, 64=qui, 96=par, 17=fois, 47=ce, 79="tout" A5, 00="pour" A9,
84="on" A15, 67=et/veut, 87=ce). A bound letter (34='i', 29='er' pencil GT)
licenses NO boundary between it and its neighbor. 40='e' has no standing
bound/free ruling — boundary-dependent, never a licensor. 46='que' is banked
pencil ground truth but is NOT in the standing boundary-licensing set (its
free-word status under the adopted rules was never granted; a bare "que"
does not force a word boundary). 77='le' is provisional, not a licensor.
59='est' is provisional, not a licensor. Class membership (98=verb class R19)
is not a boundary licensor. 62 itself is unvalued (62='il' killed at kill
grade, R19); no standing rule licenses or forbids a boundary at an
unvalued neighbor's side. §3 bars inventing values for unvalued cells.

## Method

Byte-exact bigram censuses for '62 94' and '94 62'; full predecessor and
follower distributions; per-window left/right boundary status under the
adopted rules; row-join check for every adjacency (pre|62 and 62|fol).

## Window-level evidence (@-offsets, 0-based, repaired stream)

### 35-window census: @ | row | ±3 (62 bracketed)

@11 a1_00: 78 18 93 [62] 98 76 45
@46 a1_01: 43 81 30 [62] 96 00 92
@82 a1_02: 42 98 51 [62] 16 14 06
@100 a1_02: 85 08 21 [62] 94 93 59
@360 a2_06: 47 11 21 [62] 48 76 47
@389 a2_07: 43 91 36 [62] 91 84 73
@425 a2_09: 29 47 14 [62] 48 76 42
@446 a2_09: 78 41 10 [62] 61 59 32
@508 a3_00: 21 67 77 [62] 94 64 98
@658 a4_02: 26 30 03 [62] 16 00 86
@665 a4_02: 50 80 03 [62] 06 00 20
@761 a5_03: 29 40 20 [62] 94 59 39
@802 a5_05: 86 44 74 [62] 98 53 69
@840 a5_06: 17 98 20 [62] 94 26 12
@849 a5_06: 33 96 40 [62] 21 67 91  (62|21 crosses the a5_06|a5_07 row join: 21 @850 is a5_07)
@945 a5_10: 50 40 08 [62] 98 96 86
@1065 a6_04: 82 96 21 [62] 18 70 39
@1136 a6_08: 77 86 20 [62] 98 00 98
@1141 a6_08: 00 98 78 [62] 16 29 42
@1297 a7_03: 52 80 04 [62] 16 02 70
@1315 a7_04: 00 36 74 [62] 48 98 15
@1324 a7_04: 29 80 08 [62] 98 56 30
@1329 a7_04: 56 30 06 [62] 94 70 52
@1349 a7_05: 66 73 34 [62] 48 77 78
@1362 a7_06: 35 13 92 [62] 94 79 14
@1454 a7_09: 33 46 92 [62] 61 21 67
@1464 a7_09: 17 01 21 [62] 48 21 02
@1468 a7_09: 48 21 02 [62] 38 26 12
@1482 a7_10: 82 16 98 [62] 46 77 84
@1536 a8_00: 66 73 41 [62] 06 21 62
@1539 a8_00: 62 06 21 [62] 93 88 77
@1569 a8_01: 29 24 74 [62] 48 56 32
@1686 a8_05: 65 13 93 [62] 94 79 14
@1704 a8_06: 94 30 20 [62] 94 88 26
@1772 a8_09: 26 37 78 [62] 94 24 87

### '62 94' anchors

'62 94' bigram: exactly x9 stream-wide — @100, @508, @761, @840, @1329,
@1362, @1686, @1704, @1772. Grounds: byte-exact bigram census.
'94 62' bigram: exactly x0 stream-wide. No predecessor 94 anywhere at 62.

### Free-word adjacency census (adopted rule set)

Free-word predecessors: ZERO. Grounds: no predecessor cell belongs to the
standing boundary-licensing set {11, 64, 96, 17, 47, 79, 00, 84, 67, 87}.
Closest misses, stated with cause:
- @508 pre=77 (provisional 'le', not a licensor — UNDETERMINED left).
- @849 pre=40='e' (no standing bound/free ruling — UNDETERMINED left).
- @1349 pre=34='i' (bound letter — this is the ONE decided left
  boundary: FORCED NO-BOUNDARY, standing-licensed by the bound-letter
  rule; not a free-word adjacency, so the "zero free-word predecessors"
  count stands).

Free-word followers: ONE — @46 (a1_01), fol=96='par': FORCED BOUNDARY
after 62 at @46, standing-licensed. Window-local; no transfer.
Closest miss, stated with cause:
- @1482 fol=46='que' — banked pencil GT but NOT in the standing
  boundary-licensing set, so right side is UNDETERMINED, not forced.
  (Not noted in the parent census; grounds for the gap recorded here.)

All other 34 windows: both sides UNDETERMINED under the adopted rules
(neighbors unvalued; §3 bars naming them; no rule bites).

### Predecessor distribution (byte-exact)

21×5, 20×4, 74×3, 08×2, 93×2, 03×2, 78×2, 92×2,
02/04/06/10/14/30/34/36/40/41/51/77/98 ×1. Total 35. Grounds: stream census.
Distributional only; frequency is not a boundary license (adopted premise).

### Follower distribution (byte-exact)

94×9, 48×6, 98×5, 16×4, 06×2, 61×2,
18/21/38/46/91/93/96 ×1. Total 35. Grounds: stream census.

### Row-join check on every adjacency (pre|62 and 62|fol)

34/35 windows have locus, predecessor, and follower in a single row.
The one exception: @849 — pre=40 (a5_06) and 62 (a5_06) are row-internal,
but fol=21 @850 sits in a5_07: the 62|21 adjacency crosses the a5_06|a5_07
row join. Grounds: byte-exact row mapping. Row joins are transcription
artifacts; under standing rules they neither license nor forbid a word
boundary — recorded for the package, undetermined for the boundary.

### '08 62' overlap (the two windows the parent target fenced)

'08 62' bigram: exactly x2 stream-wide — @945 (a5_10) and @1324 (a7_04).
Both windows: left side UNDETERMINED (pre=08, unvalued), right side
UNDETERMINED (fol=98, verb class, not a boundary licensor). Grounds: the
adopted rule set; corroborates the parent NULL at battery grade without
re-litigating it.

### 62-within-±3-of-62

@1536 and @1539 (a8_00): two 62s three pairs apart, both row-internal.
No standing rule bites on an unvalued neighbor; marked UNDETERMINED.
This is the only 62-proximity cluster stream-wide.

## Per-clause pass/fail

- C1: PASS. All 35 windows censused; every left/right boundary claim
  carries a standing-licensed ground or is marked UNDETERMINED:
  1 forced boundary (@46 right), 1 forced no-boundary (@1349 left),
  68 of 70 sides UNDETERMINED with stated cause.
- C2: PASS. '62 94' x9 (windows listed byte-exact), '94 62' x0 — both
  grounded on the stream census.
- C3: PASS. No class, split, value, or polyvalence declared anywhere in
  this report; the '62 94' x9 shape is presented as distributional
  evidence only (adopted fence from order-control-08-62), never used as
  a license.

## Verdict

**promote** — the evidence package is complete: every boundary claim is
stated with standing-licensed grounds or marked undetermined, the anchors
are censused, and the §7 evidence-only adverse is honored. This package
feeds redteam-62-split; it decides nothing.

New observations for the docket (beyond the parent census):
1. @1349 is the sole window with a standing-decided left boundary
   (FORCED NO-BOUNDARY via bound-letter 34='i') — 62 sits word-internal
   there under standing rules.
2. @1482's fol=46='que' does not force a boundary under the adopted set —
   a gap in the prior "one free-word follower" statement, now grounded.
3. @849's 62|fol adjacency crosses the a5_06|a5_07 row join — the only
   row-crossing 62 adjacency stream-wide.

No standing/red-team verdict contradicted or downgraded (62='il' kill,
R19-167/168, R24, §7 sole-polyvalence all adopted); canonical-stream
caveat stands (62 windows span 28 unvalidated rows).

## Bookkeeping

- Lock `locks/62-boundary-census.lock` created on start (fresh, no stale
  lock), deleted on completion (verified below).
- Re-open conditions are red-team venue only: a naming act for 62
  (redteam-62-split) or a resolution of 40's bound/free status would
  change the undetermined inventory. The gated re-fire target
  `08-62-boundary-rerun-gated` already covers the 08|62 windows.
