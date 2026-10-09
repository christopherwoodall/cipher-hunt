# Battery report: participle-60

Worker: participle-60 subagent (session d3c94950-259c-42ca-b867-507ffaed44e2).
Date: 2026-10-08.
Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json +
data/upstream-ct_R5005.txt), parsed per code/side-keyhunt/repair_parse.py
(re-implemented inline; n=1847 asserted, 96 groups asserted). canonical.py
never used. R5005, sealed gates, and the red-team adjudication queue untouched.
@i = 0-based pair index.
Lock: code/crowd17/next-token/locks/participle-60.lock created at start,
no prior lockfile (no stale-lock note needed). No red-team verdict on 60
exists — no contradiction, no overwrite. The P1 poly-60-redteam target is
queued; this battery feeds it (see Verdict), does not duplicate it.

## Bar (verbatim, pre-registered from battery-queue.json BEFORE testing)

"resolve iff one stated verbal value (e.g. present participle / verb stem)
parses all six windows (@454/@690/@1644/@1674 + @1338/@700) with <=1 unstated
assumption; else confirm the polyvalence question"

Numbered clauses (fixed before data examination):

1. (C1) ONE verbal value is STATED (a specific class + representative form,
   e.g. present participle or finite verb stem).
2. (C2) The stated value parses ALL SIX windows — @454, @690, @1644, @1674
   (NP frames) and @1338, @700 (verb slots) — grammatically in 1841
   diplomatic French, using only banked/granted/promoted/provisional values,
   with @-offsets cited.
3. (C3) The total number of unstated assumptions across all six parses is
   <= 1. (An unstated assumption = any value, boundary, or re-segmentation
   not in the banked/granted/promoted/provisional set.)
4. (C4) Adverses answered: verb-60-bare / verb-60-ent findings cited, not
   re-run; the '21 60' x4 formula thirds (@119/@172/@197/@232) stay fenced
   to frame-vient-parvenir (no overlap with the six windows — verified).

Standing values used: banked 11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que;
granted 87=ce, 64=qui, 96=par, 17=fois, 79=tout, 00=pour, 47=ce (A4),
84=on (A15), 12=n, 48=e, 30=pas, 06=ent; provisional 59=est, 77=le;
94=ne STRONG LEAD (R17-001); 65=noun-class (prof-65, 2026-10-08).

## Method

Fresh parse per protocol; no prior counts trusted. All six windows
re-derived on the repaired stream. Two candidate verbal values tested:
(V1) present participle (the battery's headline rescue candidate — one
verbal class covering adjective-position and verb-position uses);
(V2) finite -dre verb stem (cited from verb-60-bare for @1338/@700, which
its bar covered; newly tested here on the four NP frames, which it did
not cover). 1841 diplomatic French for all grammaticality judgments.

## Window-level evidence (re-derived on the repaired stream)

W1 — @454 (row a2_10):
@451 79 @452 17 @453 77 @454 60 @455 65 @456 13 @457 66 @458 14 @459 02
@460 79 @461 87 @462 11
Reads: "...tout[79] fois[17] le[77] [60] [65-noun] [13] [66] [14] [02]
tout[79] ce[87] la[11]..."
- V1 (participle): "le [participle] [noun]" as pre-nominal epithet.
  In 1841 French, present participles in epithet position are
  post-nominal ("le jour suivant", "un homme charmant" is adjectivized).
  Pre-nominal bare participle ("le venant [noun]") is ungrammatical.
  FAIL.
- V2 (finite stem): "le[77] [finite-verb] [65]" — "le" + finite verb is
  ungrammatical. Rescue requires 77 != "le" (77 is provisional, so this
  is 1 unstated assumption) with 77 as subject: "[77-subj] [60-verb]
  [65-obj]". Possible only at the cost of the assumption. STRAINED
  (fails without spending the budget).

W2 — @690 (row a5_00):
@682 00 @683 92 @684 64 @685 29 @686 40 @687 65 @688 94 @689 29 @690 60
@691 03 @692 39 @693 74 @694 46
Reads: "...pour[00] [92] qui[64] er[29] e[40] [65-noun] ne[94] er[29] [60]
[03] [39] [74] que[46]..."
- The critical span is "65 94 29 60 03" = "[65-noun] ne[94] er[29] [60]
  [03]".
- V1 (participle): "ne [X]er [participle] [03]" — "ne" does not negate
  an infinitive, and no grammatical "[noun] ne [inf] [participle]"
  construction exists. FAIL.
- V2 (finite stem): "ne[94] er[29] [60-finite]" — 29="er" is banked
  pencil ground truth; "ne" + "er"-form + finite verb has no parse
  without contradicting 29 or positing an unevidenced boundary.
  FAIL (a rescue here would contradict ground truth, not merely spend
  an assumption).

W3 — @1644 (row a8_04):
@1639 35 @1640 56 @1641 12 @1642 33 @1643 98 @1644 60 @1645 03 @1646 64
@1647 31 @1648 10 @1649 03
Reads: "...[35] [56] n[12] [33-INF] [98] [60] [03] qui[64] [31] [10] [03]..."
- V1 (participle): "[98] [participle] [03] qui" — no grammatical parse.
  FAIL.
- V2 (finite stem): "[98-subj] [60-verb] [03-obj] qui[64]..." parses
  ONLY if 98 is a nominal subject — 98's class is open, so this is 1
  unstated assumption. STRAINED (possible, at budget cost).

W4 — @1674 (row a8_05):
@1669 11 @1670 78 @1671 55 @1672 81 @1673 92 @1674 60 @1675 03 @1676 39
@1677 74 @1678 77 @1679 44 @1680 00
Reads: "...la[11] [78] [55] [81] [92] [60] [03] [39] [74] le[77] [44]
pour[00]..."
- V1 (participle): participial phrase "[participle] [03]" modifying the
  "la"-NP requires an unevidenced detachment; 03 unknown. STRAINED.
- V2 (finite stem): "la [78 55 81 92] [60-verb] [03]" needs the four
  open groups to form a subject NP — 1+ unstated assumptions.
  STRAINED.

W5 — @1338 (row a7_05):
@1333 39 @1334 83 @1335 86 @1336 71 @1337 64 @1338 60 @1339 08 @1340 65
@1341 64
Reads: "...[71] qui[64] [60] [08] [65-noun] qui[64]..."
- This window forces 60 VERBAL (cited: battery-adj-60 KILL, C4 — @1338
  with red-team-granted 64='qui' forces 60 verbal at kill grade).
- V1 (participle): a present participle CANNOT head a "qui" relative
  clause — "qui" requires a finite verb ("*l'homme qui venant" is
  ungrammatical in every period of French). This is a CLASS-level
  exclusion, independent of segmentation or assumptions. The only
  rescue (60 as subject with 08 as the finite verb) makes 60 nominal,
  abandoning the verbal claim. FAIL AT CLASS LEVEL.
- V2 (finite stem): parses — cited verb-60-bare V1 ("qui [60-dre]
  [08] [65-noun]"). PASS (by citation).

W6 — @700 (row a5_01):
@694 46 @695 02 @696 50 @697 45 @698 28 @699 94 @700 60 @701 12 @702 98
@703 20
Reads: "...que[46] [02] [50] ce[45] [28] ne[94] [60] n[12] [98] [20]..."
- This window forces 60 VERBAL (cited: battery-adj-60 KILL, C4 — @700
  with battery-promoted 94='ne' forces 60 verbal at kill grade).
- V1 (participle): "ne" + present participle is ungrammatical ("ne"
  is a preverbal negator clitic requiring a finite verb). FAIL AT
  CLASS LEVEL.
- V2 (finite stem): excluded by verb-60-bare's impossibility proof
  (cited, §"V2 is ungrammatical under EVERY French verb"): (a) no
  French verb form — finite, subjunctive, imperative, infinitive, or
  participle — ends in bare -n, so "[60]n" is impossible; (b) all
  "n[98]" word-initial options fail (double-"ne", or need new values
  for 98); (c) no tested re-segmentation of 94 rescues it. FAIL
  (under the standing segmentation; re-segmentation is follow-up
  work, cf. ne-ce-1169's 94-segmentation findings).

## Assumption budget audit (C3)

Most charitable rescue attempt (V2 finite stem):
- W6 needs a 94 re-segmentation: assumption 1.
- W1 needs 77 != "le" (provisional): assumption 2.
- W2 needs 29 != "er" or an unevidenced boundary: contradicts banked
  pencil ground truth — not an available assumption at any budget.
Total: >= 2 assumptions, one contradicting ground truth. EXCEEDS budget.

Participle attempt (V1): dead at W5 on class grounds with zero
assumptions available to fix it (making 60 finite abandons the
participle). No budget can rescue it.

No single unstated assumption rescues all six windows for either
candidate value.

## Per-clause pass/fail

- C1: PASS. Two verbal values stated and tested: (V1) present
  participle, (V2) finite -dre verb stem.
- C2: FAIL. V1 fails W1/W2/W3 (strained-to-ungrammatical) and W5/W6
  (class-level). V2 fails W6 (impossibility proof, cited), W1 (needs
  77 re-value), W2 (needs 29 contradiction). Neither value parses all
  six.
- C3: FAIL. Cheapest rescue needs >= 2 assumptions, one against
  ground truth; participle needs a class change, not an assumption.
- C4: PASS. verb-60-bare (NULL: -dre family fits V1/V3/V4, V2
  ungrammatical under every verb — findings cited, bars not re-run)
  and verb-60-ent (NULL: no ent-prefixed verb nameable — cited, not
  re-run) coordinated. '21 60' x4 formula thirds verified at
  @119/@172/@197/@232 (rows a1_03/a1_05/a2_00/a2_01) — none overlaps
  the six windows; thirds question stays fenced to frame-vient-parvenir.

## Verdict

**NULL** — the single-class rescue fails: no stated verbal value
parses all six windows within the assumption budget. The present
participle, the battery's headline rescue candidate, is excluded at
@1338 on class grounds (a participle cannot head a "qui" relative),
and every verbal value is excluded at @700 under the standing
segmentation (cited impossibility proof). The NP frames independently
resist finite verbs (@454 "le [verb]", @690 "ne er [verb]" against
banked 29="er").

**The polyvalence question is CONFIRMED** (per the bar's else-branch):
@1338 and @700 force 60 verbal (standing adj-60 kill), while no single
verbal value covers 60's distribution — 60's class assignment needs
red-team adjudication under §7 (67 et/veut is currently the sole true
polyvalence; this battery declares no new polyvalence). This finding
feeds the existing P1 target poly-60-redteam (queued) — no duplicate
escalation created.

Not kill-grade for the existential: @700's segmentation caveat stands
(94's segmentation problems are documented across ne-ce-1169,
verb-60-bare (c), and the @841 "94 26 12" twin anomaly) — a future
re-segmentation could in principle reopen the rescue. Hence NULL, not
KILL. No standing verdict contradicted or downgraded.

## Follow-ups (null regenerates work)

1. `reseg-700-verbal` (P2): narrow re-segmentation test at @694–706 —
   can 94 attach leftward (28-94 span) or 12 rightward such that a
   verbal 60 parses @700 grammatically? Cite verb-60-bare (c) and
   ne-ce-1169's seg-61-94-word; do not duplicate their bars. Success
   reopens the finite-stem rescue; failure hardens the @700 exclusion.
2. `npframe-60-454` (P2): class adjudication at @454 — does
   "le[77] [60] [65-noun]" admit ANY verbal 60 (finite or participle)
   under <= 1 unstated assumption? If no, @454 forces non-verbal 60;
   combined with @1338 forcing verbal, 60's polyvalence is proven
   pending red-team ratification (feed poly-60-redteam).

## Files

- Report: code/crowd17/report_inbox/battery-participle-60.md (this file)
- Queue: battery-queue.json `participle-60` → status `verdict`, result
  `null` (own entry only, temp-file + rename; pre-write assert: no
  prior verdict existed)
- Lock: locks/participle-60.lock created at start with agent id + UTC
  timestamp, deleted on completion
- R5005, sealed gate instances, and the red-team adjudication queue
  untouched throughout
