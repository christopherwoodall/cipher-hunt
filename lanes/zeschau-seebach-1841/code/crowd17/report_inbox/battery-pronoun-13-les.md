# Battery report: pronoun-13-les

Target: `pronoun-13-les`. Claim: 13 = 'les' object pronoun.
Date: 2026-10-09. Worker: a741e161-2dd3-4d6a-b3b3-df4f81d4c434 (battery worker).
Lock `locks/pronoun-13-les.lock` created 2026-10-09T04:46:02Z (no pre-existing
lock for this id); deleted on completion.

Offset convention: @n = 0-based pair index in the repaired 1,847-pair stream
(matches subj-13-value / subj-55-61-word convention).

## Bar (verbatim, pre-registered)

"(a) the five verb-follower windows (@68/@822/@1381 13->24, @1554/@1684
13->93) parse as pronoun+verb with stated glosses; (b) each nominal-follower
window (13->76 @567, 13->55 x2 @575/@1166, 13->66 x2, 13->52 @481, 13->92
@1360) adjudicated with stated cause - re-segmentation, or the pronoun arm
dies there; (c) coordinate with subj-55-61-word (if 13 is pronoun, 'les
[55-61]' is not a subject NP - state the consequence)"

## Bar restated (numbered pass/fail clauses; frozen before testing)

1. The five verb-follower windows (@68/@822/@1381 13->24, @1554/@1684 13->93)
   parse as pronoun+verb with stated glosses.
2. Each nominal-follower window (13->76 @567, 13->55 x2 @575/@1166, 13->66 x2
   @139/@456, 13->52 @481, 13->92 @1360) is adjudicated with stated cause:
   re-segmentation, or the pronoun arm dies there.
3. Coordination with subj-55-61-word is honored: the consequence of 13-as-
   pronoun for the "les [55-61]" subject-NP account is stated.

## Method

Read BATTERY-PROTOCOL.md first. Re-derived the repaired 1,847-pair stream
independently from `data/upstream-ct_R5005.txt` +
`code/side-keyhunt/repaired_offsets.json`, parsed per
`code/side-keyhunt/repair_parse.py` (asserted 1,847 pairs / 96 types before
testing). `canonical.py` never used. R5005, sealed gates, red-team queue
untouched. Every number traces to the stream (analysis script /tmp/pronoun13.py,
session-local).

Standing values used (protocol §7 + battery promotes): banked GT 11=la,
82=m, 29=er, 40=e, 34=i, 46=que, 70=pre; granted 87=ce, 47="ce" (A4), 00="pour"
(A9 class-level), 84="on" (A15), 79="tout" (A5); battery-promoted 24=finite-
verb class (ne-24-profile), 93=verb class (verb-93), 94="ne" (ne-94, pending
ratification), 06="ent" (conditional), 30="pas", 65=noun-class (prof-65),
76=noun masculine (battery-noun-76, never downgraded); provisional 59="est",
77="le"; leads 78="ver" (R16-005), 45="ce/dict" (A11 HOLD); 67 et/veut sole
true polyvalence with the positional rule.

## Window-level evidence (re-derived)

13, n=12 @ [68, 139, 456, 481, 567, 575, 822, 1166, 1360, 1381, 1554, 1684];
suc {24x3, 66x2, 55x2, 93x2, 52x1, 76x1, 92x1}; pre {65x3, 69x2, 45x2, 00, 97,
95, 35, 99}. Census matches subj-13-value exactly.

### Clause-1 windows (verb followers)

- @68 (a1_01): `08 34 29 40 12 94 92 69 [13] 24 56 87 14 24 87 11 00`
  Gloss: "[08]ieren (34=i, 29=er, 40=e, 12=n — banked/promoted letters) ne(94)
  [92] [69] les(13) [24-finite-verb] [56] ce(87) [14] [24] ce(87) la(11)
  pour(00)". Skeleton S + ne + les + V is grammatical. Caveat: the 92/69
  pre-clitic slots are unvalued (92-69 bigram x2 stream-wide, both in this
  exact 13-24 context — a fixed unit, value open). Weakest leg; no
  contradiction.
- @822 (a5_05): `40 95 [13] 24 87 59 38 82 01`
  Gloss: "e(40) [95] les(13) [24] ce(87) est(59, provisional) [38] m(82) [01]".
  24 is clause-final finite verb here per ne-24-profile's own parse of this
  window ("[95] [13] [24]. Ce est …"). Subject slot = 95 (n=2, class open).
  Structurally clean.
- @1381 (a7_06): `84 92 69 [13] 24 65 68 52 82 16`
  Gloss: "on(84, A15 granted) [92] [69] les(13) [24] [65] [68] [52] m(82)
  [16]". Firm subject "on"; S + clitic + V clean.
- @1554 (a8_01): `46 70 12 94 92 45 23 99 [13] 93 61 40 17 11 26`
  Gloss: "[99] les(13) [93-verb, verb-93 promoted] [61] e(40) fois(17,
  promoted) la(11) [26]". verb-93 parsed this exact window as "[13] [93]
  [61]e fois" — its parse already assumes 13-as-pronoun; consistent, not
  circular (93's verbhood was promoted on independent frames). Subject slot
  = 99 (hapax, open). Structurally clean.
- @1684 (a8_05): `39 74 77 44 00 46 79 65 [13] 93 62 94 79 14 60`
  Gloss: "[65-noun, prof-65 PROMOTED] les(13) [93-verb] [62] ne(94) tout(79)
  [14] [60]". Firm nominal subject; S + clitic + V clean.

### Clause-2 windows (nominal followers)

- @567 (a3_02): `11 43 24 80 97 [13] 76 45 94 52 87 78 45 13 55 61 …`
  "…[97] les(13) [76] ce(45) ne(94) [52] ce(87) verdict(78-45) les(13)…".
  76 = NOUN at battery-promote grade (battery-noun-76: "76 = noun,
  masculine"; re-confirmed by frame-qui-47, 2026-10-09: "76 verb-hood is
  kill-grade dead … never downgraded per protocol"). A preverbal object
  clitic "les" before a noun is categorically ungrammatical — "les" admits
  no verb to attach to here (76 is the immediate follower).
  Re-segmentation attempts, all tested and rejected:
  (i) 97 as affirmative imperative ("[97-imp.] les!"): fails — 00->97 x4
  ("pour [97]") forces 97 non-imperative under the §7 one-value rule, and
  97 has no verb profile (10 windows, all-hapax followers).
  (ii) 97-13 as one word: no evidential support, no lane mechanism.
  (iii) "les" attaching rightward past 76 to a later verb: clitics cannot
  skip an intervening noun; 45="ce" (A11 HOLD) intervenes in any case.
  **The pronoun arm dies at @567 at kill grade.**
- @575 (W1, a3_02): `87 78 45 [13] 55 61 94 82 06 06`
  "ce(87) verdict(78-45, one-word boundary promoted) les(13) [55-61-verb]
  ne(94) m(82)ent(06)ent(06, R17-007)". subj-55-61-word KILLED the 55-61
  plural-noun value at W3 (55-61 = "prend"-shaped verb per the promoted
  seg-55-61-21-stem discriminator); §7 one-value extends the verb shape to
  W1: "ce verdict les [prend]" = S(sg) + clitic + V(3sg) — clean.
  Adjudication: pronoun+verb PASS (re-segmentation of the old
  determiner+noun reading, forced by the standing kill).
- @1166 (W2, a6_09): `21 67 78 45 [13] 55 61 94 87 83 21`
  "[21] et(67 — 'et' by the §7 positional rule: 78 is noun-shaped)
  verdict(78-45) les(13) [55-61-verb] ne(94) ce(87) [83]…". The 13-55-61
  span parses as pronoun+verb, same as W1. The tail "94 87" ("ne ce") is the
  known stream-unique hapax fenced by dict-frame-78-45-13-55-61 / ne-ce-1169
  — a 94 problem, not a 13 problem. Adjudication: PASS on the span.
- @139 (a1_04): `65 [13] 66 14 74 67` and @456 (a2_10): `65 [13] 66 14 02 79`
  "[65-noun, prof-65 PROMOTED] les(13) [66] [14] …". Clean S + clitic + V
  IFF 66 is verb-shaped at these two windows. 66's class is genuinely open:
  poly-66-split (2026-10-09) gathered Bonferroni-passing distributional
  evidence for a pour-governed non-finite vs finite-verb-shaped split and
  fenced the declaration to the red team per §7; @139/@456 sit in 66's
  unassigned group (13-66-14 x2), and no standing verdict forces 66
  non-verbal here. Adjudication: CONDITIONAL PASS — rides the fenced 66
  question, stated cause, no contradiction.
- @481 (a2_11): `00 [13] 52 30 01 19`
  "pour(00, A9) les(13) [52] pas(30) [01] [19]". The canonical
  clitic-before-infinitive frame ("pour les [V-inf]") IFF 52 is infinitive;
  52's class is open (adj-52-37-value was scoped to the 52-37 unit, never
  global; 52 n=27 with mixed governors: 11->52 x3 nominal, 93->52 x2 verbal).
  The "pas" wrinkle (52->30 x2: @482 here, @1308 "74 52 30 92"): "pour les
  [V-inf] pas" is ungrammatical as one clause, so re-segmentation with a
  clause boundary — "pour les [52-inf]. Pas [01] [19]…" ("pas [X]" verbless
  clause) — is required and stated. Adjudication: CONDITIONAL PASS via
  clause-boundary re-segmentation; flips to kill at this window if 52's
  value battery names 52 non-infinitive.
- @1360 (a7_06): `35 [13] 92 62 94 79 14 60`
  "[35] les(13) [92] [62] ne(94) tout(79) [14] [60]". class-92 (2026-10-08,
  null) showed a genuinely tripartite governor profile with a real verbal
  subset ("pour [92]er" @1154 stem smoking gun; F1 verb-92-subset queued);
  @1360's 13-governor is a singleton that forces no class. Pronoun+verb
  parses IFF 92 rides its verbal subset here; subject slot = 35 (n=10,
  class open, no battery verdict). Adjudication: CONDITIONAL PASS — rides
  the queued verb-92-subset, stated cause, no contradiction.

## Per-clause pass/fail

1. **PASS** (clause a). All five verb-follower windows parse as pronoun+verb
   with stated glosses. Firm subjects at @1381 ("on", A15) and @1684
   (65=noun, prof-65); open-but-uncontradicted subject slots at @822 (95)
   and @1554 (99); @68 weakest (92/69 pre-clitic slots unvalued, fixed
   92-69 unit) but grammatically skeleton-clean. Confirms the queue's
   evidence note ("'les [verb]' parses all 5 verb-follower windows cleanly").
2. **FAIL at kill grade** (clause b). @567 forces the claim false: 13 stands
   before 76, a battery-promoted noun (never downgraded), with no
   grammatical pronoun parse and no surviving re-segmentation under standing
   values (imperative-97 fails on 00->97 x4; 97-13 unit unsupported;
   rightward clitic attachment impossible). Per the bar's own terms the
   pronoun arm dies there — and per §7 (67 the sole true polyvalence) a
   global value claim cannot survive one dead window. The other six
   nominal-follower windows adjudicate as stated (two clean passes at
   @575/@1166, three conditional passes riding fenced/open questions at
   @139/@456/@481/@1360) — none of them rescues @567.
3. **PASS** (clause c). Coordination with subj-55-61-word (verdict KILL,
   2026-10-09): that battery forced 55-61 verb-shaped at W3 ("prend" +
   noun object, promoted seg-55-61-21-stem discriminator), closing the
   "les [55-61]" 3pl-subject-NP route on the noun side. Consequence of
   13-as-pronoun: 13-55-61 re-segments as pronoun+verb ("ce verdict les
   [prend]"-shaped) — this CONFIRMS rather than contradicts
   subj-55-61-word's kill; the two batteries agree. W1's "ne mentent" 3pl
   subject remains unfound by any 13-route: the determiner route is dead
   (subj-13-value kill) and the pronoun route is dead globally (@567 kill
   here).

## Adverses answered

- "67 sole-polyvalence (§7) — pronoun vs determiner split may need red-team
  declaration if both arms hold locally": ANSWERED — the condition is not
  met. The determiner arm is already dead at kill grade (subj-13-value,
  2026-10-09: five verb windows force any plural determiner false). There is
  no second live arm, so no split exists to declare and no red-team
  declaration is needed. The pronoun arm's death at @567 is terminal for
  the 'les' value, not a split candidate.

## Standing-verdict check

No standing red-team verdict is contradicted (R17-001/R17-006/R17-007,
R16-005, A11 HOLD, A15, §7 banked/granted/promoted values all used as
premises, none challenged). Battery verdicts upheld, not downgraded:
76=noun (battery-noun-76 / frame-qui-47), 65=noun-class (prof-65),
55-61-verb (subj-55-61-word), 24/93 verb classes. Per protocol §5, no
escalation: nothing here contradicts a red-team verdict.

## Verdict: KILL

Headline: 13 = 'les' object pronoun is dead at kill grade. The five
verb-follower windows parse cleanly as pronoun+verb (clause a passes), but
@567 ("97 les [76-noun]") forces the claim false: 76 is a battery-promoted
noun that can never host a preverbal clitic, and every re-segmentation
fails under standing values. Under §7's one-value rule one dead window
kills the global claim. 13's value remains OPEN — both French "les" arms
(determiner, object pronoun) are now killed, so the next battery must test
a non-"les" value or re-examine the @567 segmentation.

## Follow-up targets (kill-grade; work regenerates — all ids verified absent from the queue)

1. **value-13-third-arm** (priority 2). Claim: 13 takes a non-"les" value
   (both French "les" arms are killed: determiner by subj-13-value,
   object pronoun by this battery). Bars: (a) census all 12 of 13's windows
   with predecessor/successor classes stated; (b) each candidate value
   tested against the verb-follower set (13->24 x3, 13->93 x2) AND the
   @567 hard constraint (13 before promoted noun 76); (c) kill the
   candidate iff it fails @567. Evidence: this report + battery-subj-13-value.md.
   Adverses: 76=noun promoted (never downgraded) — @567 is a hard wall;
   13's predecessor set is heterogeneous (65x3, 69x2, 45x2, 00, 97, 95, 35, 99).
2. **subj-w1-573-reroute** (priority 2). Claim: W1's "ne mentent" 3pl subject
   is found via a non-13 route. Bars: (a) parse "ce verdict [13] [55-61] ne
   mentent" with 13's value held open (neither determiner nor pronoun);
   (b) coordinate with subj-55-61-word's kill (55-61 verb-shaped) and this
   battery's 13 kill — no duplication; (c) name the 3pl subject with the
   clause boundary stated, or confirm W1 subjectless as a fenced residual.
   Evidence: this report + battery-subj-55-61-word.md + battery-w1-573-subject.md.
   Adverses: 94="ne" STRONG-LEAD caveats (R17-001); "94 87" hapax at W2.
3. **les567-imperative** (priority 3). Claim: @567 re-segments as
   "[97-imperative] les!" + new clause "[76] ce…", reviving a local
   pronoun parse. Bars: name 97's class independently (>=3 windows, zero
   contradictions); imperative iff 97 is verb-shaped — kill iff 97 is
   nominal/infinitive ("pour [97]" x4 is the standing counter-evidence).
   Evidence: this report (re-segmentation attempt (i) under @567).
   Adverses: 00->97 x4; §7 one-value rule bars a local imperative
   exception.

## Reproducibility

All counts re-derived in-session from the repaired stream (1,847 pairs /
96 types asserted before testing). Analysis script: /tmp/pronoun13.py
(session-local). No writes outside this report, the queue edit, and the
lockfile (deleted).
