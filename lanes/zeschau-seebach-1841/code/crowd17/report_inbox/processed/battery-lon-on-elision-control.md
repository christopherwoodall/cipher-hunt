# Battery report: lon-on-elision-control (@508 elision signature vs granted 'on' legs)

Worker: 2a3276b0-2c96-4ffa-887a-cf747e93dbe2. Date: 2026-10-08.
Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json +
data/upstream-ct_R5005.txt, parsed per code/side-keyhunt/repair_parse.py).
canonical.py never used. R5005 never touched. Red-team queue never touched.
Lock: code/crowd17/next-token/locks/lon-on-elision-control.lock (created
2026-10-09T01:20:00Z, deleted on completion). No stale lock present.

## Bar (verbatim, pre-registered)

"resolve iff follower-signature parity (84's followers vs @508's 94='ne') and
left-edge parse parity under 77='le' provisional hold; else record the
discriminator that weakens the case"

Numbered clauses (stated BEFORE testing):

1. Follower-signature parity: the follower of @508's 62 under the
   conditioned-'on' reading (94, ='ne' pending ratification) belongs to the
   granted-'on' follower class signature — PASS iff 94 is distributionally
   on-par with 84's successors (no kill-grade rejection).
2. Left-edge parse parity under the 77='le' provisional hold: the 77->62
   left edge at @507->@508 parses identically to the granted 77->84
   'l'on' elision legs — PASS iff the elision mechanism is identical and
   the trigram reads clean French, with 77='le' provisionality fenced.

## Method

Fresh parse of the repaired stream; no prior counts trusted. Re-derived:
84's full successor census (n=25) and the granted elision-context subsets
(77->84 x7, 46->84 x2 with their followers); the @508 window at full
resolution (@503-@513); 94's predecessor/successor census (n=37); all nine
62->94 legs with their left neighbors; the 77->94-direct nil check; Fisher
exact on the ne-follower comparison (0/25 vs 1/1). Did not re-litigate
collision-62-84's kill, lon-62-on-conditioned's null, or lon-ne-77-62-94;
all were read and their @508 anchor verified.

## Window-level evidence (@-offsets, repaired stream)

@508 window (row a3_00), pairs 503-513:
@503='39', @504='68', @505='21', @506='67', @507='77', @508='62',
@509='94', @510='64', @511='98', @512='65', @513='88'.
The @508 leg under test: 77-62-94 = 'l''on'-'ne' (conditioned reading).

Granted-'on' follower signature (84, n=25). Successors: 59 x4, 24 x3,
02 x2, 92 x2, 09 x2, 29 x1, 26 x1, 53 x1, 74 x1, 91 x1, 73 x1, 51 x1,
06 x1, 79 x1, 33 x1, 78 x1, 64 x1. 84->94 x0. 84->48 x0. Zero
'ne'-items (94 or 48) follow granted 'on' in all 25 windows.

Granted elision-context legs and their followers:
- 77->84 x7 'l'on' (84 at @146, @260, @1058, @1447, @1485, @1764, @1803;
  i.e. 77 at @145, @259, @1057, @1446, @1484, @1763, @1802): followers
  09 x2, 59 x2, 29 x1, 74 x1, 24 x1. None is 94.
- 46->84 x2 'qu'on' (@310, @473): followers 24 x2. None is 94.
- 46->62 x0: no 'qu'on'-analog exists for 62 (per lon-62-on-conditioned).

94 census (n=37): predecessors 62 x9 (top), 12 x3, 42 x3, 82 x3, 61 x2,
65 x2, 22 x2, 78 x2; successors 82 x4, 74 x3, 59 x3, 52 x3, 92 x2,
24 x2, 76 x2, 79 x2, 64 x1. 94->64 x1 stream-wide — the @509->@510
'ne qui' singleton (already fenced, lon-94-64-rightedge queued).

62->94 legs (@=62 position): @100, @508, @761, @840, @1329, @1362,
@1686, @1704, @1772. Left neighbors: 21, 77, 20, 20, 06, 92, 93,
20, 78. @508 is the ONLY elision-context leg (77 x1 of 35
62-predecessors); 77->94-direct x0 stream-wide.

Fisher exact (ne-follower: 84's 0/25 vs @508's 1/1): one-sided
p = 1/26 = 0.038. Below the lane's distributional-rejection standard
(grants/kills in this lane rest on p ≈ 0.0029-0.0069); not kill-grade.

## Per-clause pass/fail

1. Follower-signature parity — FAIL (weakens, not kills). The 94 at
   @509 is outside 84's granted follower class signature: 84 never
   takes a 'ne'-follower (84->94 x0, 84->48 x0, n=25), and none of the
   7 granted 'l'on' legs' followers (09 x2, 59 x2, 29, 74, 24) is 94.
   Under the conditioned-'on' reading @508 is exactly 'on'+'ne' — a
   combination the granted corpus never shows for 'on'. This is the
   discriminator the bar asks to record.
2. Left-edge parse parity — PASS (conditional). Under the 77='le'
   provisional hold, 77->62@508 licenses elision identically to
   77->84: 'on' is vowel-initial, so 'l'' + 62 elides by the same
   mechanism as the 7 granted 'l'on' legs. The trigram reads
   "l'on ne" — clean French, and 'on ne' is a standard combination.
   Conditional on 77='le' (provisional, fenced) and 94='ne'
   (unratified, fenced).

## Verdict

**NULL — discriminator recorded, case weakened, not killed.** Clause 2
passes (elision mechanism identical under the 77='le' provisional
hold); clause 1 fails at weakening grade: granted 'on' legs show zero
'ne'-followers (0/25; the 7 'l'on' legs' followers are 09 x2, 59 x2,
29, 74, 24), while @508 under the conditioned reading is 'on'+'ne'.
Fisher one-sided p=0.038 does not reach the lane's rejection standard,
so this is not kill-grade; no window forces the conditioned-'on'
reading false, and the single-observation @508 side structurally
cannot reject at the standard. The standing red-team package from
lon-62-on-conditioned is unaffected: clause (a) still passes (elision
context unique to @508), clause (b) still deferred to the red team.

## Adverses (answered or fenced, never ignored)

- 77='le' provisional is the hinge: honored. Clause 2 is explicitly
  conditional; le-77's null (2026-10-07) leaves 77='le' provisional per
  §7. If 77 dies, the @508 elision context dissolves with it.
- 94='ne' unratified: honored. The ne-94 battery promote (2026-10-07)
  is pending ratification; clause 1's 'ne' labeling is conditional on
  that ratification.
- Does not declare polyvalence: honored. No value declared here — a
  distributional comparison only. Conditioned 62='on' admissibility
  remains the red team's act (lon-62-on-conditioned clause b, untouched).

## Null follow-ups (per §4 — work regenerates, never ends)

1. lon-on-elision-rerun-94-64 (priority 3): conditional re-test of this
   battery once the fenced 94->64 'ne qui' singleton resolves via the
   already-queued lon-94-64-rightedge (coordinate, do not duplicate).
   Bars: rerun follower-signature and left-edge parity with the right
   edge parsed; record whether the discriminator survives.
2. ne-follower-census-84 (priority 3): widen clause 1's discriminator.
   Bars: census 84's successors against ALL ne-candidates (94, 48,
   12='n') under alternate readings; if any 'on'+ne-contact exists
   under a rival reading, record the weakening of this report's
   discriminator.
3. elision-leftedge-62-gate (priority 3): conditional on lon-77-le-gate.
   Bars: if 77='le' promotes or dies, re-derive clause 2's left-edge
   parse parity under the new 77 status; report whether the parity
   holds or dissolves.

## Standing-constraint check

- No R5005 contact, no sealed gates, no red-team queue writes.
- No verdict overwritten; no promotion declared; no contradiction with
  any standing verdict (collision-62-84 kill, lon-62-on-conditioned
  null, lon-ne-77-62-94 null all stand beside this report).
- 67 remains the sole true polyvalence.
