# Battery report: on-08-homophony — "08='on' homophony under the full {33,86}-precedent bar"

Worker: battery-worker-on-08-homophony (79996a24-d112-43bf-9db3-d4c50b5aae1f), 2026-10-09.
Lock: created fresh at 2026-10-09T08:33:22Z (no stale lock present).
Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json +
data/upstream-ct_R5005.txt, parsed per code/side-keyhunt/repair_parse.py; 1,847
pairs asserted). canonical.py never touched. R5005, sealed gate instances, and
the red-team adjudication queue never touched. All numbers trace to the stream.
Sibling context read first: battery-stem-08.md (null — "se" killed, "on"
fenced, homophony with 84 needs the full bar) and battery-prefix-08-31.md
(null — 08-31 x3 parses but composition unforced). Per §7, 67 et/veut is the
sole true polyvalence: no second polyvalence may be declared at battery level.

## Bar (verbatim, pre-registered)

"resolve iff successor/predecessor distributions indistinguishable per the
{33,86} precedent; @1488 'ce on' boundary adjudicated with stated cause"

## Bar restated as numbered clauses (fixed before testing)

Precedent source: crowd13/homophone-ab/PREREG.md (Set A {33,86}, lane standard)
+ R-AB1 (GRANTED SPLIT, 2026-10-07): the {33,86} verdict killed homophony on
frame disjointness despite passing uniformity (p=0.354). The live bar:

- C1 (uniformity): 1690 χ² on (n08, n84) fails to reject uniform — p > 0.05.
- C2 (cycling): Wald–Wolfowitz runs on the despatch-order 08/84 membership
  sequence — |z| < 2 (interleaved; clumping kills at the lane standard).
- C3 (no segregation): predecessor and successor distributions
  indistinguishable — χ² on P(pre|08) vs P(pre|84) and P(suc|08) vs P(suc|84)
  fail to reject at p > 0.05; divergence at p < 0.01 kills free homophony.
- C4 (@1488 boundary adjudication): the "ce on" adjacency at @1488 parses
  with stated cause under the 08="on" reading — otherwise the claim forces a
  window.
- C5 (frame interchangeability): ≥2 legs — 08 attested in 84's signature A15
  frames AND/OR 84 attested in 08's characteristic frames at non-degenerate
  rates. Zero interchangeability kills (precedent KILL criterion verbatim).

## Method

Imported repair_parse.py's load_rows/parse (the repaired stream itself, not
canonical.py). Enumerated all windows of 08 (n=18) and 84 (n=25) with ±5
context. χ² tests via scipy.stats.chi2_contingency (pooled rare categories,
kept categories with pooled total ≥3). Fisher exact on the signature frames.
Frame census of 84's A15 anchor frames (77-84 "l'on", 46-84 "qu'on", 84-59
"on est", 82-84 elision) vs 08's characteristic frames (08-31, 40-08, 67-08,
37-08, 08-65, 08-62, 60-08).

## Window-level evidence (@-offsets, repaired stream)

n(08)=18, n(84)=25.

84's anchor frames (A15 grant evidence):
- 77-84 x7 ("l'on"): @146, @260, @1058, @1447, @1485, @1764, @1803
- 46-84 x2 ("qu'on"): @310, @473
- 84-59 x4 ("on est"): @1189 ("06 84 59 46"), @1290, @1447, @1803
- 82-84 x1 (elision contact): @167
- 08 in ANY of these 14 frames: ZERO (77-08 x0, 46-08 x0, 08-59 x0, 82-08 x0)

08's characteristic frames (from stem-08 + this census):
- 08-31 x3: @881, @1488, @1521(31) — 84-31 x0
- 40-08 x2: @922, @944 — 40-84 x0
- 67-08 x2: @198, @631 — 67-84 x0
- 37-08 x2: @779, @1302 — 37-84 x0
- 08-65 x2: @922, @1339 — 84-65 x0
- 08-62 x2: @944, @1323 — 84-62 x0
- 60-08 x2: @198 — 60-84 x0
- 84 in ANY of these 15 frames: ZERO

The decisive adjacency — @1485 (84) and @1488 (08) are THREE pairs apart in
one window (a7_10):
- @1485: "16 98 62 46 77 [84] 24 87 08 31 92" = 46='que' 77='le'(prov)
  84='on' 24 87='ce' [08] 31='[31-finite]'. Under the 08="on" reading this
  single window contains TWO "on"s in non-interchangeable frames ("le on 24"
  vs "ce on 31") — a second polyvalence inside one window, with zero shared
  frames to support it.

## Per-clause pass/fail

- C1 (uniformity): PASS. χ²=1.1395, p=0.2858. (Necessary but insufficient,
  per §7 doctrine — uniformity also passed for the SPLIT {33,86} set.)
- C2 (cycling): FAIL at kill grade. Membership sequence (n1=18, n2=25):
  14 runs vs E[runs]=21.93, z=-2.516 — clumped beyond the |z|<2 bar. 08 and 84
  cluster apart through the despatch; they do not 1690-cycle.
- C3 (segregation): FAIL. Predecessor sets are nearly disjoint — 08←{60, 67,
  37, 40, 01, 41, 85, 16, 17, 45, 80, 87}, 84←{77, 66, 89, 46, 53, 82, 91, 65,
  48, 06, 17, 32}; only 17 is shared. χ² p=0.0419 (sparse-pooled; the visible
  structure is segregation: 77→84 x7 vs 77→08 x0, Fisher p=0.030 — 08 is
  excluded from 84's signature frame at significance). Successor χ² p=0.056
  on sparse pools; the frame-level record is sharper: successors of 08
  {31, 65, 62, 91, 34, 21, 67, 24, 52, 29, 01, 43} vs 84
  {59, 24, 02, 92, 09, 29, 26, 53, 74, 91, 73, 51} — overlap {24, 29, 91}
  only, and 84's modal successor 59 x4 never follows 08.
- C4 (@1488 boundary): ADJUDICATED with stated cause — pass-with-fence.
  "87='ce' [08='on'] 31=[finite]" is ungrammatical as one clause ("ce on"
  adjacency); it parses only across a clause boundary:
  "...que l'on [24-modal] ce | on [31]..." — stated cause: 24's promoted
  modal-verb class governs "ce" as its object (cf. "24 ce <V>" frame, x9;
  @823 "24 87 59" = "24 ce est" requires ONE finite verb directly after
  "24 ce"), so 31 must start a new finite clause with 08 as its subject.
  FENCED, not clean: the fence is strained (load-bearing on 24's modal class)
  and it directly collides with the prefix-08-31 parallel — "24 ce [08-31]"
  patterns with "24 ce est" as ONE prefixed verb, which the separate-clause
  "on | 31" reading forbids. The boundary parse survives but does not
  discriminate; it cannot carry the claim.
- C5 (frame interchangeability): FAIL at kill grade. ZERO legs, both
  directions: 08 never appears in any of 84's 14 anchor frames; 84 never
  appears in any of 08's 15 characteristic frames. This is the precedent's
  KILL criterion verbatim ("zero frame interchangeability with similarity
  attributable to shared class alone" — here, even the class resemblance is
  absent: 08's frames are pre-verbal clitic/spelling contact, 84's are
  subject-verb A15 frames).

## Verdict

**kill** — 08 is not a homophone of granted 84="on". Uniformity holds (p=0.286)
but the lane-standard discriminators reject the merge: clumped cycling
(z=-2.516, kill-grade per the {33,86} precedent), predecessor segregation with
08 excluded from 84's signature "l'on" frame (Fisher p=0.030), and zero frame
interchangeability in either direction across 29 anchor frames. The @1488
"ce on" adjacency adjudicates only across a strained clause boundary and
cannot rescue the claim. Per §7, asserting 08="on" alongside granted 84="on"
would declare a second polyvalence at battery level — explicitly barred.
The claim fails; it is not inconclusive, so no follow-up targets are
regenerated from it. 08's own value remains open in the pipeline (prefix
productivity, syllable-letter ID, and 65-verb-shapeness targets queued by the
sibling nulls); this kill touches none of them.

Standing verdicts preserved, none contradicted: A15 (84="on") untouched;
battery-stem-08 null ("on" fenced, homophony needs the full bar — the bar has
now been run and it fails); battery-prefix-08-31 null untouched; sole
polyvalence (67 et/veut) untouched. No escalation — no red-team verdict is
overturned, and §5's no-downgrade rule is respected (the claim had no prior
verdict; its status moves queued → verdict).

## Adverse

"adverses: none listed" — none to answer. The queue note that "asserting it
would be forcing" is CONFIRMED: the bar had to be run, not asserted, and the
run kills the merge.
