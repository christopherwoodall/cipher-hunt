# Battery report: subj-13-value

Target: `subj-13-value`. Claim: name 13's value/class (13->24 x3 verb-contact
vs 13->76 noun-contact).
Date: 2026-10-09. Worker: b5de188e-07a8-4ad5-9257-553a40d07914 (battery worker).
Lock `locks/subj-13-value.lock` created 2026-10-09T04:19:50Z (no pre-existing
lock for this id); deleted on completion.

Offset convention: @n below = 0-based pair index in the repaired 1,847-pair
stream (matches name-13-55-61 / unit-13-55-61-contact); 1-based in parens.

## Bar (verbatim, pre-registered)

"a plural-determiner value ('les'/'des') turns W1's X into a 3pl NP
('les [55-61] ne mentent') and finds the subject"

## Bar restated (numbered pass/fail clauses; frozen before testing)

1. 13's value IS a plural determiner ('les' or 'des'), consistent with 13's
   full contact profile (n=12) — a value claim is global in this lane (§7:
   67 et/veut is the sole true polyvalence).
2. Under that value, W1's '13-55-61' parses as a grammatical 3pl NP
   ('les/des [55-61]') that is the subject of 'ne mentent' — i.e. the subject
   is found.

## Method

Read BATTERY-PROTOCOL.md first. Re-derived the repaired 1,847-pair stream
independently from `data/upstream-ct_R5005.txt` +
`code/side-keyhunt/repaired_offsets.json`, parsed per
`code/side-keyhunt/repair_parse.py` (asserted 1,847 pairs / 96 types before
testing). `canonical.py` never used. R5005, sealed gates, red-team queue
untouched. Every number traces to the stream.

Standing values used (protocol §7 + battery promotes): banked GT 11=la, 82=m,
29=er, 40=e, 46=que; granted 87=ce, 47="ce" (A4 allophone tier); promoted
24=finite verb class (ne-24-profile, 2026-10-08), 93=verb class (verb-93,
2026-10-09), 06="ent" (R17-007 conditional), 30="pas"; provisional 59=est,
77="le"; leads 78="ver" (R16-005), 94="ne" STRONG LEAD (R17-001), 45="ce/dict"
(A11 HOLD).

## Window-level evidence (re-derived)

13, n=12 — all windows (0-based; 1-based in parens):
- @68 (@69, a1_01): `... 92 69 [13] 24 56 87 14 24 87 ...` — 13->24
- @139 (@140, a1_04): `... 65 [13] 66 14 74 67 ...` — 13->66
- @456 (@457, a2_10): `... 65 [13] 66 14 02 79 ...` — 13->66
- @481 (@482, a2_11): `... 00 [13] 52 30 01 19 ...` — 13->52
- @567 (@568, a3_02): `... 97 [13] 76 45 94 52 87 78` — 13->76
- @575 (@576, a3_02): `... 45 [13] 55 61 94 82 06 06` — 13->55 (W1)
- @822 (@823, a5_05): `... 95 [13] 24 87 59 38 82 01` — 13->24
- @1166 (@1167, a6_09): `... 45 [13] 55 61 94 87 83 21` — 13->55 (W2)
- @1360 (@1361, a7_06): `... 35 [13] 92 62 94 79 14 60` — 13->92
- @1381 (@1382, a7_06): `... 69 [13] 24 65 68 52 82 16` — 13->24
- @1554 (@1555, a8_01): `... 99 [13] 93 61 40 17 11 26` — 13->93
- @1684 (@1685, a8_05): `... 65 [13] 93 62 94 79 14 60` — 13->93

Successor census matches name-13-55-61 exactly: {24x3, 66x2, 55x2, 93x2,
52x1, 76x1, 92x1}.

The five verb-follower windows, parsed under the standing promotes:

1. @68: `12 94 92 69 13 24 56 87 ...` — "n'(12) ne(94) [92] [69] [13]
   [24-verb] [56] ce(87) ...". 24 is the promoted finite verb
   (ne-24-profile: "que 24" x3 subordinate slots, infinitive complements).
   "les/des [24-finite-verb]" is categorically ungrammatical; no clause
   boundary rescues a stranded determiner.
2. @822 (= ne-24-profile's @823 1-based): `95 13 24 87 59 ...` — that battery
   parsed this exact window as "[95] [13] [24]. Ce(87) est(59) ..." with 24 as
   absolute clause-final verb. Determiner "les/des" before it is stranded and
   ungrammatical; pronoun "les [24]" ("[95] les [verb]") is clean.
3. @1381: `84 92 69 13 24 65 68 ...` — "on(84) [92] [69] [13] [24-verb] ...".
   Same verdict: determiner stranded, pronoun clean.
4. @1554 (= verb-93's @1555 1-based): `99 13 93 61 40 ...` — verb-93 parsed
   this window with 93 as verb ("[13] [93] [61]e fois"). "les/des [93-verb]"
   ungrammatical; "les [93]" pronoun+verb clean.
5. @1684 (= verb-93's @1685 1-based): `65 13 93 62 94 ...` — verb-93 parsed
   "[13] [93] | [62] ne tout [14]". Same verdict.

The determiner-compatible windows (13->76 x1, 13->55 x2, 13->66 x2, 13->52 x1,
13->92 x1) cannot save the value: 66/52/92 are class-open (66 has a queued
split battery), and 76/55 are nominal — but a global determiner value is
already forced false at the five verb windows above.

'des' dies by the same mechanism ('des' + finite verb is ungrammatical), plus
at W1/W2 'des' would need 45='ce' to yield "ce des" — ungrammatical under the
A11 HOLD reading (fenced, not needed for the kill).

## Per-clause pass/fail

1. **FAIL (kill grade).** Five windows force the plural-determiner claim
   false: 13->24 x3 and 13->93 x2 place a determiner directly before a
   promoted finite-verb class (24: ne-24-profile; 93: verb-93), which is
   categorically ungrammatical in French — a stranded determiner admits no
   clause-boundary rescue. The kill is class-level: it holds for ANY plural
   determiner ('les', 'des', or other), not just the two named values.
2. **MOOT (antecedent false).** With no determiner value available for 13,
   nothing turns W1's X into a subject NP via this route. Noted: W1-locally
   "les/des [55-61] ne mentent" parses cleanly ("the/some [55-61] do not
   lie") — the failure is global (13's other windows), not W1-local. W1's
   subject remains unfound by this battery.

## Adverses answered

- "coordinate with queued unit-13-55-61-contact": ANSWERED — that target has
  since returned verdict/null (2026-10-08, processed). Its findings (13->55
  exclusive to the two 5-gram windows; 55-61 binds to 13 at p≈0.046) are
  consistent with this kill: the 13->55 x2 windows ARE determiner-compatible,
  but the value is untenable globally. No conflict; nothing duplicated.

No standing red-team verdict is contradicted (R17-001/R17-006/R17-007,
R16-005, A11 scoping, §7 banked/granted/killed values all respected — 24 and
93 are battery promotes used as premises, not challenged). No escalation.

## Verdict: KILL

Headline: the plural-determiner hypothesis for 13 is dead at kill grade —
five windows (13->24 x3, 13->93 x2) force a determiner before a promoted
finite-verb class, which is categorically ungrammatical. The kill is
class-level (any plural determiner). W1's "ne mentent" subject is NOT found
by this route; the "les/des [55-61]" subject account via 13 is closed.

Note for the supervisor: the queued sibling `subj-55-61-word` sought "a
plural-noun value ('temoins'/'hommes'/...) completes W1's subject slot" —
its subject-NP route via 13-as-determiner is now closed; it should coordinate
on a non-13 determiner account or a re-segmentation, not "les [55-61]".

## Follow-ups proposed (kill-grade; the work regenerates via the live rival)

1. **pronoun-13-les** (priority 2). Claim: 13 = 'les' OBJECT PRONOUN.
   Bars: (a) the five verb-follower windows (@68/@822/@1381 13->24,
   @1554/@1684 13->93) parse as pronoun+verb with stated glosses; (b) each
   nominal-follower window (13->76 @567, 13->55 x2 @575/@1166, 13->66 x2,
   13->52 @481, 13->92 @1360) adjudicated with stated cause —
   re-segmentation, or the pronoun arm dies there; (c) coordinate with
   queued subj-55-61-word (if 13 is pronoun, "les [55-61]" is not a subject
   NP — state the consequence). Evidence: this report.
   Adverses: §7 sole-polyvalence (67 et/veut) — pronoun vs determiner split
   may need red-team declaration if both arms hold locally.
2. **split-13-det-pron** (priority 2). Claim: 13's contact profile splits
   determiner-incompatible (verb followers) vs pronoun-incompatible (nominal
   followers) windows. Bars: (a) predecessor/successor-class contingency for
   all 12 of 13's windows stated; (b) test for a positional separator (cf.
   67's positional rule) between the arms; (c) if no positional rule found,
   package for the red team as a second-polyvalence candidate — battery
   gathers only, never declares (§7). Evidence: this report.
   Adverses: small n (12); 66/52/92 class-open.

## Reproducibility

All counts re-derived in-session from the repaired stream (1,847 pairs /
96 types asserted before testing). Analysis script: /tmp/subj13.py
(session-local). No writes outside this report, the queue edit, and the
lockfile (deleted).
