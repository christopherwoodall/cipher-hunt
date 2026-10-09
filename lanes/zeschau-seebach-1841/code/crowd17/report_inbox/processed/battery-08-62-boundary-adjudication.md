# Battery report: 08-62-boundary-adjudication — adjudicate the 08|62 word-boundary presupposition

Worker: subagent 7950a033-9070-4e14-87fe-fbb2965d7c45, 2026-10-09.
Lock: created fresh at 2026-10-09T13:42:00Z (no pre-existing/stale lock present).
Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json +
data/upstream-ct_R5005.txt), parsed like code/side-keyhunt/repair_parse.py
(replicated inline; asserts held: 1,847 pairs, 96 types). canonical.py never
touched. R5005, sealed gate instances, and the red-team adjudication queue
never touched. All numbers trace to the stream.

Provenance: follow-up #3 of battery-08-leftattach-944-1323 NULL (2026-10-09).
That battery fenced the 08-as-word-final-leftattach route partly because the
word-final geometry presupposes an 08|62 boundary with zero standing basis.
This target adjudicates that presupposition directly.

## Bar (verbatim, pre-registered)

"decide the 08|62 boundary at both windows at battery grade with stated
evidence; else fence the boundary question."

## Bar restated as numbered clauses (fixed before testing)

- C1: decide the 08|62 boundary at W1 (@944, row a5_10) at battery grade with
  stated evidence — BOUNDARY or NO-BOUNDARY on standing-licensed grounds.
- C2: decide the 08|62 boundary at W2 (@1323, row a7_04) at battery grade
  with stated evidence.
- C3 (else): fence the boundary question with stated cause.

Adverses: none listed.

Standing premises adopted (§7; battery premises, never re-litigated):
08 is letter-tier, value OPEN (stem-08-letter-probe PROMOTE;
08-letter-geometry PROMOTE); standalone 08 kill-grade dead
(ce-08-31-frame). Boundary rules battery-licensed: a word boundary is
forced after/before a banked/promoted free word (11=la, 64=qui, 96=par,
17=fois, 47=ce, 79="tout" A5, 00="pour" A9, 84="on" A15, 67=et/veut,
87=ce); a bound letter after 08 (34='i', 29='er' pencil GT) licenses
NO boundary between 08 and that letter (08-position-profile PROMOTE).
40='e' has no battery-grade bound/free ruling, so 40|08 is
boundary-dependent, not forced. 98 = verb class (R19) — class is not a
word; not a boundary licensor. 62 is unvalued: 62='il' killed at kill
grade (R19); 62's class/split is red-team venue (redteam-62-split);
'62 94' x9 subject-shape is distributional-only evidence, fenced as a
license (order-control-08-62). §3 bars inventing values for unvalued
cells; §7 sole-polyvalence (67) intact.

## Method

Re-derived the repaired stream in-session byte-exact per repair_parse.py.
Byte-exact bigram census for '08 62'; full 18-window census of 08's
right-neighbor boundary status using ONLY the standing boundary rules
above; full 35-window census of 62 (predecessor distribution,
free-word adjacencies). ±8 context at both loci with row-boundary check.
For each candidate decision route (boundary / no-boundary), tested
whether a standing-licensed ground exists, and whether adopting it would
contradict a standing verdict or encroach on the red-team docket.

## Window-level evidence (@-offsets, 0-based, repaired stream)

'08 62' bigram: exactly x2 stream-wide — @944 (a5_10) and @1323 (a7_04).
Both loci are row-internal at the boundary (locus, predecessor, follower
all in the same row).

- W1 @944 (a5_10) [936..952]:
  `33 21 64 37 01 07 50 40 | [08] 62 98 | 96 86 01 77 86 96`
  (a6_00 begins at @951, outside the tested boundary)
- W2 @1323 (a7_04) [1315..1331]:
  `62 48 98 15 24 03 29 80 | [08] 62 98 | 56 30 06 62 94 70`
  (single row throughout)

### 08 right-neighbor boundary census (all 18 windows, standing rules only)

| @ | row | pre [08] fol | boundary after 08 |
|---|---|---|---|
| 35 | a1_01 | 01 [08] 91 | UNDETERMINED (follower unvalued) |
| 60 | a1_01 | 41 [08] 34 | NO-BOUNDARY (follower 34='i' bound letter) |
| 98 | a1_02 | 85 [08] 21 | UNDETERMINED |
| 198 | a2_00 | 60 [08] 67 | FORCED-BOUNDARY (follower 67 free word) |
| 534 | a3_01 | 16 [08] 24 | UNDETERMINED |
| 631 | a4_01 | 67 [08] 52 | UNDETERMINED after; 08 word-initial (free 67 before) |
| 779 | a5_04 | 37 [08] 29 | NO-BOUNDARY (follower 29='er' bound letter) |
| 881 | a5_08 | 17 [08] 31 | UNDETERMINED after; 08 word-initial (free 17 before) |
| 922 | a5_09 | 40 [08] 65 | UNDETERMINED (follower unvalued) |
| **944** | a5_10 | 40 [08] 62 | **UNDETERMINED (follower 62 unvalued)** |
| 975 | a6_01 | 45 [08] 01 | UNDETERMINED |
| 1302 | a7_03 | 37 [08] 43 | UNDETERMINED |
| **1323** | a7_04 | 80 [08] 62 | **UNDETERMINED (follower 62 unvalued)** |
| 1339 | a7_05 | 60 [08] 65 | UNDETERMINED |
| 1488 | a7_10 | 87 [08] 31 | UNDETERMINED after; 08 word-initial (free 87 before) |
| 1520 | a7_11 | 67 [08] 31 | UNDETERMINED after; 08 word-initial (free 67 before) |
| 1592 | a8_02 | 47 [08] 81 | UNDETERMINED after; 08 word-initial (free 47 before) |
| 1610 | a8_03 | 23 [08] 55 | UNDETERMINED |

18 = 18. The census validates the adopted 08-position-profile: the two
'08 62' windows are the only windows whose follower is 62, and neither
standing boundary rule bites on an unvalued follower.

### 62 census (boundary evidence around 62, evidence only)

n(62) = 35. Zero windows with a free-word predecessor (no forced boundary
before 62 anywhere). One window with a free-word follower: @46 (a1_01),
fol=96='par' — a boundary is forced after 62 there, i.e. a word CAN end
at 62, but this is window-local and does not transfer to @944/@1323.
62 predecessor distribution: 21 x5, 20 x4, 74 x3, 08 x2, 93/03/78/92 x2,
rest x1 — '08' is a joint-second predecessor, but predecessor frequency
is distributional, not a boundary license.

### Decision routes tested

FOR BOUNDARY (08|62 = boundary):
1. Follower-is-free-word: FAIL — 62 is unvalued; 62='il' killed at kill
   grade; no standing free word stands at 62.
2. 08-is-word-final: FAIL — circular. A boundary after 08 makes 08
   word-final, which is exactly the route 08-leftattach-944-1323 fenced
   (host unnameable within budget). The route is FENCED (epistemic,
   resting on unvalued cells), not killed; a fence cannot license the
   boundary, and deciding FOR the boundary would require promoting that
   route — outside battery scope.
3. 62-as-subject forcing a pre-62 clause boundary ('62 94' x9 shape):
   REJECTED — the shape is fenced as distributional-only evidence
   (order-control-08-62); using it to force the boundary would name a
   class for 62, encroaching on redteam-62-split (red-team venue) and
   violating §3/§7.
4. The '08 | 62 98' geometry (order-control-08-62): REJECTED as a license
   — it is a conditional compatibility statement (given the left-attach
   reading), and the left-attach reading is fenced. Adopting it as the
   boundary decision would presuppose the claim under test.

FOR NO-BOUNDARY (08|62 internal):
1. Follower-is-bound-letter: FAIL — 62 is unvalued, not a bound letter.
2. 08-forced-word-initial at the window: FAIL — the adopted
   position-profile classifies @944 as boundary-dependent on the
   unresolved 40|08 question and @1323 as undetermined; neither window
   has 08 word-initial at battery grade.

No other standing boundary rule exists in the protocol or adopted
battery verdicts.

## Per-clause pass/fail

- C1 (W1 @944): FAIL. Follower 62 is unvalued; no standing rule forces or
  forbids a boundary between 08 and 62. All four candidate decision
  routes fail or are circular/off-limits (see above).
- C2 (W2 @1323): FAIL. Same cause; 08's position reading is
  "undetermined", so not even a conditional word-initial route exists.
- C3: FENCE EXECUTED with stated cause:
  1. No standing-licensed decider exists: boundary-forcing needs a
     free-word follower and no-boundary-forcing needs a bound-letter
     follower or a forced word-initial 08 — 62 is unvalued (62='il'
     killed; class is red-team venue) and neither window has 08
     word-initial.
  2. The adopted 08-position-profile (PROMOTE) already classifies both
     loci as undecided on the right side; deciding the boundary here
     would contradict that standing verdict.
  3. The only battery-compatible boundary geometry ('08 | 62 98') is
     conditional on the fenced left-attachment route and cannot license
     the boundary without circularity.
  4. Importing 62's subject-shape to force a pre-62 boundary would invent
     a class and encroach on the red-team docket (redteam-62-split) —
     barred by §3 and §7.

Not kill grade: the fence rests on unvalued cells (62's value/class,
40's bound/free status), not on a forced contradiction. A naming act on
62 or a resolution of 40's status would reopen the question. No standing
or red-team verdict is contradicted or downgraded; §7 intact;
canonical-stream caveat stands (rows a5_10/a7_04 unvalidated).

## Verdict

**null** — fence executed. The 08|62 boundary cannot be decided at
battery grade at either window: no standing-licensed ground forces a
boundary, and no standing-licensed ground forbids one.

## Follow-ups (nulls regenerate work; all verified ABSENT from battery-queue.json, 2026-10-09)

1. **08-62-boundary-rerun-gated** (P3) — GATED re-fire of this target's
   C1/C2 iff the red team names 62's value or class (redteam-62-split
   resolves) or a letter value for 08 is named (val-08-31-letter /
   syllable-08-letter-value). Bar: decide the 08|62 boundary at both
   windows on the new standing grounds; else re-fence. Evidence: this
   report; the fence rests purely on unvalued cells. Adverses: none.
2. **bound-40-boundary-resolve** (P3) — resolve 40='e' bound/free status
   stream-wide (pencil GT cell with no standing ruling). A forced 40|08
   boundary makes 08 word-initial at @944 (and @922), which licenses
   NO-boundary at 08|62 there (a word-initial letter fuses rightward).
   Bar: state 40's status with distributional byte evidence at battery
   grade; else fence. Evidence: '40 08' x2 (@922/@944); position-profile
   boundary-dependence note. Adverses: none.
3. **62-boundary-census** (P3) — full 35-window census of 62's boundary
   evidence (free-word adjacencies, '62 94' anchors, ±3 context) as an
   evidence package for redteam-62-split. §7 — gather only; no class
   declared. Bar: every boundary claim stated with standing-licensed
   grounds or marked undetermined. Evidence: this report's 62 census
   (n=35; 0 free-word predecessors; 1 free-word follower @46).
   Adverses: none.

## Bookkeeping

- Lock `locks/08-62-boundary-adjudication.lock` created on start (fresh,
  no stale lock), deleted on completion (verified below).
- Queue: `08-62-boundary-adjudication` -> `status: verdict`,
  `result: null`, `2026-10-09` (pre-write assert: was
  `queued`/verdictless; temp-file + rename; JSON re-validated from disk;
  own entry only; no downgrade).
- R5005, sealed gates, red-team adjudication queue untouched.
