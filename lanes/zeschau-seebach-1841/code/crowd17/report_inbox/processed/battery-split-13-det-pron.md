# Battery report: split-13-det-pron

Target: `split-13-det-pron`. Claim: "13's contact profile splits
determiner-incompatible (verb followers) vs pronoun-incompatible (nominal
followers) windows".
Date: 2026-10-09. Worker: 4b942bcf-cea8-400b-8e06-ea282e78af0a (battery worker).
Lock `locks/split-13-det-pron.lock` created 2026-10-09T04:46:51Z (no
pre-existing lock for this id); deleted on completion.

Offset convention: @n = 0-based pair index in the repaired 1,847-pair stream
(1-based in parens).

## Bar (verbatim, pre-registered)

"(a) predecessor/successor-class contingency for all 12 of 13's windows
stated; (b) test for a positional separator (cf. 67's positional rule)
between the arms; (c) if no positional rule found, package for the red team
as a second-polyvalence candidate - battery gathers only, never declares
(protocol section 7)"

## Bar restated (numbered pass/fail clauses; frozen before testing)

1. For each of the 12 windows of 13 in the repaired stream, the
   predecessor and successor are stated with their standing class/value
   (protocol section 7 + standing battery promotes/leads; class-open
   values marked, not invented).
2. A positional separator between the two arms (verb-follower vs
   nominal-follower windows) is tested on the natural candidates:
   predecessor identity/class, row/section, row-local position,
   stream-index cut, and +/-2 slot classes — cf. 67's rule ("67='veut'
   iff follower infinitive-shaped").
3. If no separator is found, the report is packaged as a
   second-polyvalence candidate for the red team; the battery declares
   nothing (section 7: 67 et/veut is the sole true polyvalence).

## Method

Read BATTERY-PROTOCOL.md first. Re-derived the repaired 1,847-pair stream
independently from `data/upstream-ct_R5005.txt` +
`code/side-keyhunt/repaired_offsets.json`, parsed exactly per
`code/side-keyhunt/repair_parse.py` (asserted 1,847 pairs / 96 types
before testing). `canonical.py` never used. R5005, sealed gates, red-team
queue untouched. Every number traces to the stream.

Standing values used: banked GT 11=la, 70=pre, 82=m, 34=i, 29=er, 40=e,
46=que; granted 87=ce, 64=qui, 96=par, 17=fois, 79=tout, 00=pour (A9,
leg-1 class-level), 84=on (A15), 47=ce (A4 allophone tier); provisional
59=est, 77=le; promoted 24=finite verb class (ne-24-profile), 93=verb class
(verb-93); leads 94=ne (R17-001 STRONG LEAD), 06=ent (R17-007
conditional), 30=pas, 78=ver (R16-005); holds 45=ce (A11).

## Window-level evidence (re-derived, all 12)

Predecessor (-1) | successor (+1) per window. Arms defined by successor
class: Arm A = verb-class successor (24/93), determiner-incompatible
(class-level kill in battery-subj-13-value, any plural determiner);
Arm B = non-verb successor, pronoun-incompatible under nominal reading.

### Arm A — verb followers (determiner-incompatible), n=5
- @68 (69, a1_01, rowpos 33): pred **69** (class-open) | succ **24**
  (finite verb class). Context: `94 92 69 [13] 24 56 87 14 24`.
- @822 (823, a5_05, rowpos 22): pred **95** (class-open) | succ **24**.
  Context: `78 40 95 [13] 24 87 59 38 82` — 24 clause-final per
  ne-24-profile; 87=ce, 59=est follow.
- @1381 (1382, a7_06, rowpos 22): pred **69** (class-open) | succ **24**.
  Context: `84 92 69 [13] 24 65 68 52 82` — 84=on precedes.
- @1554 (1555, a8_01, rowpos 1): pred **99** (class-open) | succ **93**
  (verb class). Context: `45 23 99 [13] 93 61 40 17 11` — 45=ce at -3,
  40=e / 17=fois / 11=la after.
- @1684 (1685, a8_05, rowpos 18): pred **65** (class-open) | succ **93**.
  Context: `46 79 65 [13] 93 62 94 79 14` — 46=que, 79=tout at -3/-2.

### Arm B — non-verb followers (determiner-compatible), n=7
- @139 (140, a1_04, rowpos 6): pred **65** (class-open) | succ **66**
  (class-open). Context: `23 91 65 [13] 66 14 74 67 64`.
- @456 (457, a2_10, rowpos 5): pred **65** (class-open) | succ **66**
  (class-open). Context: `77 60 65 [13] 66 14 02 79 87` — 77=le at -3,
  79=tout, 87=ce after.
- @481 (482, a2_11, rowpos 4): pred **00=pour** (preposition, A9) |
  succ **52** (class-open). Context: `45 93 00 [13] 52 30 01 19 64` —
  30=pas follows 52.
- @567 (568, a3_02, rowpos 9): pred **97** (class-open) | succ **76**
  (class-open, nominal per subj-13-value). Context: `24 80 97 [13] 76 45
  94 52 87` — 24=verb at -3, 45=ce, 94=ne lead after.
- @575 (576, a3_02, rowpos 17): pred **45=ce** (A11 hold) | succ **55**
  (class-open, W1 nominal candidate). Context: `87 78 45 [13] 55 61 94
  82 06` — W1 "ne mentent" window; 82=m, 06=ent after.
- @1166 (1167, a6_09, rowpos 13): pred **45=ce** (A11 hold) | succ **55**.
  Context: `67 78 45 [13] 55 61 94 87 83` — W2 window; 67 et/veut at -3.
- @1360 (1361, a7_06, rowpos 1): pred **35** (class-open) | succ **92**
  (class-open). Context: `37 64 35 [13] 92 62 94 79 14` — 64=qui at -2,
  94=ne, 79=tout after.

Successor census (re-derived): {24x3, 93x2, 66x2, 55x2, 52x1, 76x1, 92x1}
— matches battery-subj-13-value exactly.

## Per-clause pass/fail

1. **PASS.** Predecessor/successor-class contingency stated for all 12
   windows above, with class-open values marked (65, 69, 95, 97, 99, 35,
   66, 52, 76, 55, 92) and no invented classes.
2. **TESTED — no separator found.** Results per candidate:
   - Predecessor identity: fails. Pred sets: A {65, 69, 95, 99},
     B {00, 35, 45, 65, 97}; intersection {65} (65-13-93 @1684 arm A
     vs 65-13-66 @139/@456 arm B).
   - Predecessor class (standing values): fails. Only 00 (arm B) and
     45 x2 (arm B) are class-known; 65 (both arms) is open, so no
     class rule separates.
   - Row/section: fails. Arms interleave across a1–a8; row a1 hosts
     both (a1_01 arm A, a1_04 arm B) and row a7_06 hosts both arms
     21 pairs apart (@1360 arm B, @1381 arm A).
   - Row-local position: fails. rowpos 1 occurs in both arms
     (@1554 arm A, @1360 arm B).
   - Stream-index cut: fails. Arm order by index:
     A B B B B B A B B A A A — no cut point separates the arms.
   - +2 slot values: fails (A {56,61,62,65,87} ∩ B {14,30,45,61,62}
     = {61, 62}: 93->61 @1554 arm A vs 55->61 @575 arm B).
   - -2 slot values: DISJOINT but class-open — A {23,40,79,92} vs
     B {60,64,78,80,91,93}. No class reading available (79=tout is
     the only class-known value there); recorded as a follow-up
     lead, not a rule.
   No positional separator exists at the resolution of standing values.
   The arms are separated only by the follower's class itself — which
   is the polyvalence question, not its answer.
3. **Packaged below.** No separator found → this report is the
   red-team package per the bar. Battery declares nothing (§7).

## Adverses answered

- **small n (12): FENCED.** With n=12, separator tests have low power;
  the disjoint -2 slot may be coincidence. Nothing below depends on
  the -2 slot as a rule.
- **66/52/92 class-open: ANSWERED-AS-FENCED.** Arm A's
  "determiner-incompatible" half is class-level (kill in
  battery-subj-13-value: any plural determiner before verb-class
  24/93 is ungrammatical) — solid. Arm B's "pronoun-incompatible"
  half is class-contingent for the 66/52/92 windows: it holds only if
  66/52/92 turn out nominal. Clean core: the 76 (@567) and 55 x2
  (@575/@1166) windows, where the nominal reading is standing.
  The split itself (verb-followers vs non-verb-followers) is observed
  fact, not class-contingent.

## Verdict: NULL (red-team package; second-polyvalence candidate)

Headline: the distributional split is real and unseparated. 13 has 5
windows before verb-class successors (24 x3, 93 x2) where ANY plural
determiner is class-level ungrammatical, and 7 windows before
non-verb successors (66 x2, 55 x2, 52, 76, 92) where a pronoun reading
is unavailable under the nominal reading. No positional separator was
found on any tested candidate (predecessor identity overlaps at 65;
rows interleave, including both arms on a7_06 @1360/@1381; no
stream-index cut; rowpos 1 in both arms; +2 slot overlaps at 61/62).
Per protocol §7 this battery never declares polyvalence — 67 et/veut
remains the sole true polyvalence until the red team says otherwise.

**Red-team package (bar c):**
- Fact: 13's 12 windows split 5/7 by successor class (verb vs
  non-verb), with determiner killed class-level on the verb arm and
  pronoun unavailable on the nominal core of the other arm.
- Missing piece: a positional resolution rule like 67's
  ("67='veut' iff follower infinitive-shaped"). Tested candidates:
  predecessor identity/class, row, row-local position, stream index,
  +/-2 slots — all fail (evidence above).
- If the red team holds §7's sole-polyvalence standing, the arms must
  be adjudicated by single-value rival: the pronoun rival
  (pronoun-13-les, LIVE — lock active, do not duplicate) owns arm A
  and must re-segment or die on arm B's nominal core (@567/@575/@1166);
  the determiner rival is dead class-level (battery-subj-13-value).
- Contradiction check: none with standing red-team verdicts
  (R17-001/R17-006/R17-007, R16-005, A11, §7 banked/granted/kills/
  splits/holds respected). No escalation beyond this package.

## Follow-ups proposed (null; narrow the gap)

1. **reseg-13-armA** (priority 3). Claim: arm A dissolves without
   polyvalence — 13 closes the preceding nominal leftward and the
   verb-class successor starts a new clause. Bars: (a) state the clause
   boundary per window (@68/@822/@1381/@1554/@1684) with standing
   values; (b) if any arm-A window admits no boundary, the arm stands.
   Adverses: n=5; predecessor classes open.
2. **split-13-secondleft** (priority 3). Claim: the -2 slot
   ({23,40,79,92} arm A vs {60,64,78,80,91,93} arm B, value-disjoint,
   n=12) carries the positional separator this battery could not read.
   Bars: (a) adjudicate those values' classes under standing values;
   (b) a class-level -2 separator promotes to red-team rule candidacy,
   else dissolve as coincidence. Adverses: small n; classes open.
3. **NOTE — no queue entry needed:** pronoun-13-les is QUEUED and LIVE
   (lock `locks/pronoun-13-les.lock` present); its bar (b) adjudicates
   this split's arm-B windows. Related queued tests: slot-13-43-compare
   (13 vs 43 distributional), leftedge-13-55 (13/55 classes).

## Reproducibility

All counts re-derived in-session from the repaired stream (1,847 pairs
/ 96 types asserted before testing); analysis ran session-local.
No writes outside this report, the queue edit, and the lockfile
(deleted).
