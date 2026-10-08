# Battery report: fence-83-1217 — '36 77 83' @1215-1217 parses with 83 as designated blocker

- Target: fence-83-1217 (priority 2)
- Date: 2026-10-08
- Worker: 7fa4411f-8b57-4555-ba54-0804b33ad822
- Verdict: **null** (localized residual confirmed with stated cause; fence formalized)

## Bar (verbatim, pre-registered)

"resolve iff ONE grammatical parse of the window with 83 unfixed (name 36 or place a clause boundary), or confirm the localized residual with stated cause"

## Bar restated as numbered pass/fail clauses (pre-registered before testing)

1. (C1) ONE grammatical parse of '36 77 83' @1215-1217 (a7_00) exists with 83
   unfixed (its value never fixed; 'de' lead not re-litigated), achieved by
   either (a) naming 36 (value or class) or (b) placing a clause boundary in
   the window, using <=1 non-granted assumption.
2. (C2) If no such parse exists, the localized residual is confirmed with a
   stated cause (which cell blocks, why, and why the failure is not shared
   with 36 or 77).

## Method

Parsed the repaired stream per code/side-keyhunt/repair_parse.py
(code/side-keyhunt/repaired_offsets.json + data/upstream-ct_R5005.txt):
1,847 pairs, 96 symbols. Never used canonical.py. Never touched R5005.
Standing values per BATTERY-PROTOCOL.md §7: 45='ce' (HOLD, A11),
77='le' (provisional), 96='par' (promoted). 83's value kept unfixed
throughout; 'de' lead cited only as cited-direction evidence, never re-litigated.
83 stayed the designated blocker.

## Window evidence (with @-offsets)

Window on row a7_00 (row pair-index range 1191-1218, 28 pairs):

- @1213: 96 ('par', promoted)
- @1214: 45 ('ce', HOLD)
- @1215: 36 (unnamed)
- @1216: 77 ('le', provisional)
- @1217: 83 (blocker, unfixed)
- @1218: 92 (open; '-ere' value killed)
- @1219: 61 (start of row a7_01)

So: '... par ce [36] le [83] [92] |' — the 77-83 bigram is unique
stream-wide (77-83 x1), and '36 77' x1 is also unique.

36 census (re-derived): n=9 at @388, @421, @740, @1174, @1215, @1313,
@1449, @1585, @1834. Predecessors: 00 x3 ('pour'), 59 x2 ('est'
provisional), 91/49/85/45 x1. Successors: 74 x2, 62/29/20/77/67/70/69 x1.
Contact profile spans determiner-position (45-'ce'), 'pour'-frames (00 x3),
'est'-frames (59 x2): no single class is granted for 36, and no window
names its value.

83 census (re-derived, matches battery-le83-window): n=15; predecessors
98 x5, 87 x2, 55 x2, 44 x2, 64/77/39/38 x1; followers 82 x3, 21 x3,
86 x2, 70/54/59/56/92/71/24 x1. 12-13/15 windows de-compatible; the three
fenced cells are @613/@1170 ('ce de', owned by frame-87-83-cede),
@911 ('qui de est', owned by fence-911-de), @1217 ('le de', this window).

## Per-clause pass/fail

### C1: no qualifying parse — FAIL

Two resolution paths were available under the bar; both tested.

(a) Naming 36. The most grounded class assignment is 36 = noun, forced by
'ce [36]' under the 45='ce' HOLD ('ce' takes nominals). But every 36-name
leaves 'le [83]' untouched with 83 unfixed, and 'le' + value-unknown 83
is only grammatical if 83 itself is noun/adjective-shaped — which is a
second non-granted assumption, and worse, it assigns a shape to the
designated blocker, violating the target's own designation (adverses:
"83 fenced-blocker, not 77"). Naming 36 cannot carry the window: the
blockage is at 83, not 36. No 36 value/class rescues the adjacency
77-83, because the adjacency is the blocker.

(b) Clause boundary placement. Candidate placements tested:
- Between 77 and 83 ('...ce [36] le | [83]...'): rejected — 'le.'
  terminates an article with no head; 77-83 is adjacent in the stream,
  and 'le' cannot end a clause.
- Between 36 and 77 ('ce [36]. Le [83] [92]...'): the left fragment
  'ce [36]' is an NP fragment (needs 36=noun, one non-granted assumption);
  the right fragment 'Le [83] [92]...' is a would-be subject NP that
  requires BOTH 83 noun-shaped AND 92 attaching grammatically (two more
  non-granted assumptions, one of them on the blocker itself).
- Between 45 and 36 ('...ce. [36] le [83]...'): rejected — bare 'ce.'
  is ungrammatical as a standalone clause.

The only superficially grammatical placement (after 36) needs >=2
non-granted assumptions and shapes the blocker — it fails the bar's
<=1 non-granted-assumption standard and the designated-blocker
constraint. There is no precedent on-stream for a clause boundary
rescuing an adjacent article+open-value bigram (survey-ready; see
follow-up 3).

**C1 FAILS.** No single parse covers the window with 83 unfixed at
<=1 non-granted assumption.

### C2: localized residual confirmed — PASS

The failure localizes to 83 at @1217 with stated cause:
- Left edge parses cleanly under standing values: 'par ce [36]'
  (96='par' promoted, 45='ce' HOLD; 36 class-unresolved but NP-position
  coherent). Nothing left of 77 strains.
- The strain is exactly the adjacency 77-83: under provisional 77='le',
  'le [83]' with 83 unfixed has no grammatical reading, and no clause
  boundary can sit inside the adjacent 77-83 pair to split it (the
  le83-window battery's finding, re-derived here).
- 77 is not downgraded: the parse failure is fully absorbed by 83's
  unknown value. This matches the bar's pre-commit ("83 fenced-blocker,
  not 77").

**C2 PASSES**: residual confirmed, localized to 83 @1217, cause stated.

## Verdict

**null** — per the task brief this result counts as null, NOT kill
(the 'de' lead itself is judged by de-83-sweep; kill-grade on
unconditioned 83='de' is owned by fence-911-de). The fence is now
formalized: '36 77 83' @1215-1217 is a localized 83-blocker residual,
83 unfixed, 77='le' not downgraded, 36 unnamed. No standing red-team
verdict is contradicted: this confirms (does not overwrite) the
battery-le83-window null, and the 83='de' promotion question remains
with de-83-sweep (queued, priority 3, gated on this target).

## Follow-up targets (null regenerates work)

1. **class-36-profile** — 36 n=9 is the nearest unresolved cell left of
   the fence. Bar: assign 36 ONE class (noun? infinitive? adjective?)
   with >=3 independent frame-legs, using the 00 x3 'pour'-frames,
   59 x2 'est'-frames, and 45-'ce' contact. Discriminates whether the
   left edge can ever parse independently of the 83 fence.
2. **fence-92-1218** — the right edge: '83 [92]' @1217-1218 with 83
   fenced as blocker. Bar: name 92's class/value such that the fenced-83
   edge parses or fences cleanly (92 open, '-ere' value killed).
   Constrains any clause-boundary-after-83 reading.
3. **clause-boundary-precedent** — survey: all stream windows shaped
   'X 77 [open-value]' (article + unresolved value). Bar: find >=2
   windows where a clause boundary demonstrably resolves the adjacency
   with a complete clause on each side, or record the survey negative.
   Gives the (b)-path mechanism a precedent base or retires it.

## Lock note

locks/fence-83-1217.lock created 2026-10-08T21:37:54Z, deleted on completion.
No stale lock encountered.
