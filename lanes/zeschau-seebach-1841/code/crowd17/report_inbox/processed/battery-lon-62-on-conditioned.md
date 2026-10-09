# Battery report: lon-62-on-conditioned (conditioned 62='on', elision-context only)

Worker: 82af7b05-4a67-4594-90ef-fc74d052fbfd. Date: 2026-10-08.
Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json +
data/upstream-ct_R5005.txt, parsed per code/side-keyhunt/repair_parse.py).
canonical.py never used. R5005 never touched. Red-team queue never touched.
Lock: code/crowd17/next-token/locks/lon-62-on-conditioned.lock (created
2026-10-09T00:20:41Z, deleted on completion).

## Bar (verbatim, pre-registered)

"(a) no other 62 window admits an elision read (62->59 x0, no other
vowel-context predecessor); (b) red-team decision: conditioned 'on' is
admissible or dies with the unconditioned kill. Battery gathers the
evidence; it does not declare polyvalence"

Numbered clauses (stated BEFORE testing):

1. No other 62 window admits an elision read: 62->59 x0, and no 62
   predecessor other than 77@508 is vowel/elision-context (elision-capable
   standing values: 77='le' provisional, 46='que' banked, 47='ce' granted
   allophone, 11='la' banked).
2. Red-team decision: conditioned 62='on' is admissible or dies with the
   unconditioned kill. This battery gathers the evidence and hands clause
   (b) to the red team untouched; it does not declare polyvalence.

## Method

Fresh parse of the repaired stream; no prior counts trusted. Ran the full
62 predecessor census (n=35) and successor census, the elision-capable
predecessor inventory for 62, the 62->59 nil check, the 62->94 window list,
the granted-'on' control censuses (77->84, 46->84, 84->59), and the 94->64
right-edge singleton check. Did not re-litigate collision-62-84's kill or
lon-ne-77-62-94's null; both were read and their anchor (@508) verified.

## Window-level evidence (@-offsets, repaired stream)

62 census (re-derived): 62 occurs x35. Predecessors: 02x1, 03x2, 04x1,
06x1, 08x2, 10x1, 14x1, 20x4, 21x5, 30x1, 34x1, 36x1, 40x1, 41x1, 51x1,
74x3, 77x1, 78x2, 92x2, 93x2, 98x1. Successors: 06x2, 16x4, 18x1, 21x1,
38x1, 46x1, 48x6, 61x2, 91x1, 93x1, 94x9, 96x1, 98x5.

Elision inventory for 62:
- 77->62 x1: @508 ONLY. Sole elision-context predecessor of 62.
- 46->62 x0. 47->62 x0. 11->62 x0. 94->62 x0. No other elision-capable
  standing value precedes any 62. (Banked predecessors 34='i', 40='e' are
  letter values, not eliding words.)
- 62->59 x0. No 'on est'-analog window for 62.
- 62->94 x9: @100, @508, @761, @840, @1329, @1362, @1686, @1704, @1772
  (collision-62-84 re-read: 8 clean under 62='il' rival + @508 fenced;
  not re-litigated here).

@508 window (a3_00), pairs 505-511: @505='21', @506='67', @507='77',
@508='62', @509='94', @510='64', @511='98'.

Granted-'on' control (elision context, for the red-team package):
- 77->84 x7: @145, @259, @1057, @1446, @1484, @1763, @1802 = 'l'on' x7.
- 46->84 x2: @309, @472 = 'qu'on' x2.
- 84->59 x4: @1189, @1290, @1447, @1803 = 'on est' x4.
- 94->64 x1 stream-wide: @509->@510 only. The @508 right edge 'ne qui'
  is a singleton anomaly under BOTH rivals (64='qui' granted).

## Per-clause pass/fail

1. No other 62 window admits an elision read — PASS. 77 is 62's sole
   elision-context predecessor (x1 of 35, @508); 46/47/11/94 never
   precede 62; 62->59 is x0. Every other 62 window lacks an
   elision-triggering left neighbor and lacks the 'on est'-analog
   follower.
2. Red-team decision — NOT DECIDED HERE (by design). The evidence package
   is complete and handed over untouched (see below).

## Verdict

**NULL — complete evidence package, open question packaged for the red
team.** Clause (a) passes fully: @508's elision context is unique to 62
(77 x1/35 predecessors; 62->59 x0; no other vowel-context predecessor).
Clause (b) is not a battery-decidable clause — conditioned 62='on'
admissibility is the deferred red-team act from collision-62-84 (protocol
§7: 67 is the sole true polyvalence; this battery declares none). This
battery does not contradict any standing verdict: collision-62-84's
unconditioned kill stands; lon-ne-77-62-94's null stands beside it.

## Adverses (answered or fenced, never ignored)

- collision-62-84 KILL: honored, not re-litigated. The unconditioned
  62='on' kill stands; this report tests only the conditioned
  (elision-context-only) admissibility clause (a), and defers clause (b).
- §7 sole-polyvalence law (67 et/veut): honored. No second polyvalence
  is declared, proposed, or implied here — admissibility is the red
  team's to grant or refuse.
- 'ne qui' right edge (94->64 x1): fenced as the standing independent
  blocker — the window cannot be settled at battery level even if clause
  (b) is granted. lon-94-64-rightedge is already queued; not duplicated.
- 77='le' provisional (C1): fenced as conditional. If 77 resolves
  non-'le', the @508 elision context dissolves. lon-77-le-gate is
  already queued; not duplicated.

## Red-team package (clause b, untouched)

- Claim: a conditioned 62='on' in elision-context only (@508) is
  admissible without declaring a second polyvalence.
- For: @508 is 62's sole elision-context predecessor; 'l'on ne' parses
  at trigram level (lon-ne-77-62-94 clauses 1-2 PASS); the granted 84
  legs show elision-context 'on' is a live corpus pattern (77->84 x7,
  46->84 x2); clause (a) above shows no other 62 window could absorb
  the reading, so the conditioning is exact, not leaky.
- Against: collision-62-84 fenced @508 as residual anomalous under both
  rivals; the 'ne qui' singleton right edge is anomalous regardless of
  rival; A15's C1 (77='le' provisional) is the hinge the elision reading
  hangs on.
- Decision needed: is conditioned 'on' admissible as an elision-context
  resolution, or does it die with the unconditioned kill? Battery takes
  no position.

## Null follow-ups (per §4 — work regenerates, never ends)

1. lon-on-elision-control (priority 2): discriminating battery comparing
   the granted elision-context 'on' windows (77->84 x7 'l'on', 46->84 x2
   'qu'on') against the @508 trigram. Bars: follower-signature parity
   (84's followers vs @508's 94='ne') and left-edge parse parity under
   77='le' provisional. Claim: @508's elision signature is
   distributionally identical to granted 'on' legs. Strengthens or
   weakens the conditioned-'on' case without declaring polyvalence.
2. lon-62-59-nil-gate (priority 3): conditional re-test. Bars: re-census
   62->59; the standing nil (x0) holds unless a 62->59 frame appears or
   59='est' provisional changes status. A future 62->59 hit re-opens the
   'on est'-analog leg for conditioned 62='on'.

## Standing-constraint check

- No R5005 contact, no sealed gates, no red-team queue writes.
- No verdict overwritten; no promotion declared. 67 remains the sole
  true polyvalence.
