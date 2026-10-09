# Battery report — poly-66-split (66 two-class split: evidence-gathering only)

Worker: poly-66-split battery. Date: 2026-10-08 (run 2026-10-09T01:58Z).
Lock: `code/crowd17/next-token/locks/poly-66-split.lock` created 2026-10-09T01:58:25Z
(no lock present); deleted on completion.
Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` +
`data/upstream-ct_R5005.txt`), parsed per `code/side-keyhunt/repair_parse.py`
(asserted 1,847 pairs / 96 groups before counting). `canonical.py` not used.
R5005 not touched. No invented numbers: every count re-derived in this run.
Coordination: inherits (not re-litigates) `orphan86-716` kill (2026-10-08),
`stem-86` null (2026-10-08), `stem-33-86` adjudication, `prof-65` promote
(2026-10-08). 63's class not named here (verb-63-frames queued).

## Bar (verbatim, from battery-queue.json)

"test the two-class split distributionally per the {33,86} precedent
(successor/predecessor permutation on the pour-governed x7 vs the "66-84" x2
vs the "X-66-98" x3); if the distributions split at lane standard, re-test
@716 under the pour-class alone (a resolve there flips stem-86's residual).
DECLARING a second polyvalence is a red-team act per §7 — this battery may
only gather evidence and state the conditional consequence, never declare
the split."

## Bar restated (numbered pass/fail clauses; frozen before testing)

1. Successor/predecessor permutation test on the three 66 subsets —
   pour-governed x7 (00@188/@245/@253/@714/@1108/@1493/@1532 → 66@189/@246/
   @254/@715/@1109/@1494/@1533), "66-84" x2 (66@153/@1150), "X-66-98" x3
   (66@88/@123/@766) — per the {33,86} precedent (Fisher/permutation at the
   lane's p<0.05 distributional standard). PASS iff the subsets' contact
   distributions split at lane standard.
2. If clause 1 passes: re-test @716 (86's window; the 00-66-86-01 window
   @714–717) under the pour-class alone (66 = non-finite). A resolve of
   86@716 flips stem-86's residual (4/32 → 3/32 = 9.375% orphan, meeting the
   ≤10% bar per orphan86-716's arithmetic).
3. Never declare a second polyvalence (§7: 67 et/veut is the sole true
   polyvalence). Evidence-gathering only; state the conditional consequence.

## Method

Re-derived 66's full census on the repaired stream (n=19; offsets
[88, 123, 140, 153, 189, 246, 254, 457, 705, 715, 766, 1018, 1109, 1150,
1346, 1459, 1494, 1533, 1622] — exact match to orphan86-716's re-derivation).
Predecessor distribution: 00 x7, 86 x2, 13 x2, 77/58/46/12/88/15/33/78 x1.
Successor distribution: 98 x3, 73 x3, 14 x2, 84 x2, 91 x2,
01/21/86/24/79/15/67 x1. (@-offsets are 0-based pair indices, same
convention as orphan86-716.)

Permutation test (the {33,86} precedent's instrument): null = random
permutation of the 19 predecessor (resp. successor) labels across 66's 19
windows; test statistic = count of the subset's defining contact in the
subset. Exact hypergeometric p-values computed, confirmed by 100,000-draw
Monte Carlo (seed 20261008). Lane standard: p < 0.05 (the precedent treated
Fisher p = 0.0219 and p = 0.0097 as significant); Bonferroni 0.05/3 = 0.0167
reported as well.

## Window-level evidence

### The three named subsets (re-derived)

| subset | 66 windows | predecessors | successors |
|---|---|---|---|
| pour-governed x7 | @189 (16-00-66-24-87), @246 (43-00-66-91-32), @254 (63-00-66-01-91), @715 (63-00-66-86-01), @1109 (63-00-66-73-41), @1494 (24-00-66-15-59), @1533 (63-00-66-73-41) | 00 x7 | 24/91/01/86/73/15/73 |
| 66-84 x2 | @153 (46-66-84-26) = "que [66] on [26]" (46=que banked GT, 84=on A15), @1150 (33-66-84-02) | 46, 33 | 84 x2 |
| X-66-98 x3 | @88 (77-66-98-19), @123 (58-66-98-82), @766 (88-66-98-80) | 77, 58, 88 | 98 x3 |

Remaining 7 windows (no hypothesized class): @140/@457 (13-66-14 x2),
@705 (12-66-21), @1018 (15-66-91), @1346/@1459 (86-66, post-infinitive x2),
@1622 (78-66-67).

### Clause-1 results

| subset | defining contact | exact p | Monte Carlo p (100k) | pairwise Fisher vs other named |
|---|---|---|---|---|
| pour-governed x7 | pred=00, 7/7 | 1.98e-05 | 1.0e-05 | 0.00126 |
| 66-84 x2 | succ=84, 2/2 | 5.85e-03 | 5.62e-03 | 0.0152 |
| X-66-98 x3 | succ=98, 3/3 | 1.03e-03 | 1.07e-03 | 0.00455 |

All three split at lane standard (p < 0.05; all < Bonferroni 0.0167).
Control on a non-defining feature — successor=73 in pour (2/7) vs rest of
stream (1/12): Fisher p = 0.26, no split — the separation is driven by the
governor features, as expected.

Caveat (recorded, not hidden): the subsets are defined by these governor
features, so separation on them is expected by construction; the
permutation test's non-trivial content is that the clusters are REAL
(not chance co-occurrence). The class-level inference (clusters = distinct
classes) rests on the grammatical incompatibility inherited from
orphan86-716's kill — group (a) demands non-finite ("pour"+finite
impossible), group (b) "que [66] on" demands finite-verb-shaped, empty
intersection under one class — not on the distributional test alone.

### Clause-2: re-test @714–717 under the pour-class alone

Window: `@713:63 @714:00 @715:66 @716:86 @717:01 @718:02`
= "[63] pour [66] [86] [01] [02]".

Assume 66@715 ∈ pour-class (non-finite). Then:
- 00 = "pour" (A9 class-level grant). 66 = modal infinitive
  ("pouvoir"-shaped) or adverb-before-infinitive — both shapes grammatical
  at this window (orphan86-716 window-level analysis, inherited).
- 86 = infinitive under its A9 INF-class grant: "pour [66-modal/adv]
  [86-inf] [01]" parses with zero contradiction from banked/promoted/
  granted neighbors. The [86][01] tail recurs at @948 ("par [86] [01] le"),
  a real constituent independent of 66; 01's value stays open with no
  banked neighbor forcing ungrammaticality.
- Left edge @713=63: open; under prof-65's lead-level 63-verb-shaped
  finding, "[V] pour [inf]" is a grammatical purpose clause.
- The 86=determiner alternative is dead: 86='le' as a global value was
  killed at kill grade (stem-86 battery: @175 "ce le", @671 "la le"
  ungrammatical). The infinitive resolve is the only live one.

**Resolve: 86@716 = infinitive (stem-life), zero contradiction at
@714–717 under the pour-class-alone assumption.** Conditional consequence:
IF the red team declares the 66 split (second polyvalence), THEN @716's
orphan resolves → stem-86's adjudication moves 4 orphans → 3, i.e.
3/32 = 9.375% ≤ 10%, meeting stem-33-86's clause-3 bar.

Caveat: pour-class internal unity is not fully established here — @189
("16 pour [66] 24 ce", 24 = finite modal per qui-2326-prefix battery
promote) resists every non-finite 66 value I can construct without an
unestablished clause boundary ("pour [66-nonfin]. [24] ce…"). Flagged as
follow-up #2; the @716 resolve does not depend on @189.

### X-66-98 allegiance (noted for the red team)

The claim says "two classes" but names three contexts. The X-66-98
nominal cluster ("le [66] [98]", 77='le' provisional) is noun-compatible,
and noun sits inside group (a)'s licensed set (orphan86-716: INF / noun /
adverb-before-INF / disjunctive pronoun) — so X-66-98 may side with the
pour-class rather than force a third class. Follow-up #3 owns this.

## Per-clause pass/fail

1. Distributional split at lane standard: PASS — all three subsets split
   (exact p = 1.98e-05 / 5.85e-03 / 1.03e-03; Monte Carlo confirms;
   pairwise Fisher 0.00126 / 0.0152 / 0.00455), with the stated
   circularity caveat; clusters are real, not chance.
2. Re-test @716 under pour-class alone: PASS (conditional) — 86@716
   resolves as infinitive with zero contradiction at @714–717; flips
   stem-86 to 3/32 = 9.375% iff the split is declared.
3. No polyvalence declared: COMPLIED — the split is fenced to the red
   team, not declared here.

## Adverses disposition

- "Declaring a second polyvalence is a red-team act per §7 (67 sole true
  polyvalence) — evidence-gathering only": ANSWERED by compliance. No
  second polyvalence is declared; the evidence package (distributional
  p-values, inherited grammatical empty-intersection, conditional @716
  resolve) is fenced to the red team as escalation #1.

## Standing-verdict check

No standing red-team or battery verdict contradicted. The §7
sole-polyvalence constraint is the reason this battery stops at
evidence-gathering: promoting the claim would itself be the forbidden
declaration. A9 grants (00="pour" class-level, 86 INF-class) untouched; no
window re-valued. stem-86's null confirmed, not contradicted; stem-33-86's
orphan arithmetic is stated conditionally, not decided.

## Verdict: NULL (battery-inconclusive by authority, not by evidence)

The evidence supports the split (clause 1 passes at lane standard; the
grammatical empty-intersection stands via orphan86-716; the @716 resolve
is demonstrated conditionally), but the decision — declaring a second
polyvalence — is a red-team act per §7. Per protocol §5.2 the result is
marked null with the authority tension as the headline and escalated to
the red team. Nothing is refuted; nothing is declared.

## Follow-ups (null regenerates work)

1. **redteam-66-polyvalence** (P1, red-team venue): decide whether 66's
   pour-governed non-finite (x7) vs finite-verb-shaped "66-84" (x2) split
   warrants declaring a second polyvalence per §7. Evidence package:
   permutation p = 1.98e-05 / 5.85e-03 / 1.03e-03 (Bonferroni-passing);
   grammatical empty-intersection (orphan86-716 kill, inherited);
   conditional @716 resolve → stem-86 3/32 = 9.375% (meets ≤10% bar).
2. **pour-66-189-boundary** (P2): @189 "16 pour [66] 24 ce" resists every
   non-finite 66 value without an unestablished clause boundary — test
   boundary vs value; decides pour-class internal unity.
3. **noun-66-98-side** (P3): test whether X-66-98's 66 sides with the
   pour-class (noun) or the 66-84 class — decides two-class vs three-way.

## Reproducibility

All censuses re-derived inline against the repaired stream only (asserted
1,847 pairs / 96 groups before each count). 66 offsets
[88, 123, 140, 153, 189, 246, 254, 457, 705, 715, 766, 1018, 1109, 1150,
1346, 1459, 1494, 1533, 1622] exact-match orphan86-716. Monte Carlo seed
20261008, 100,000 draws. No writes outside this report, the queue entry,
and the lockfile.
