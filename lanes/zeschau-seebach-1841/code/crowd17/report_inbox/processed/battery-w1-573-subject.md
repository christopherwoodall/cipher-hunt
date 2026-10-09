# Battery report: w1-573-subject

Target: `w1-573-subject`. Claim: W1's 'ne mentent' subject identified.
Date: 2026-10-09. Worker: 884fa4c5-5407-4dbe-ad60-5b0573aaaa0c (battery worker).
Lock `locks/w1-573-subject.lock` created 2026-10-09T03:51:27Z (no stale lock);
deleted on completion.

Offset convention: @n below = 1-based pair index in the repaired 1,847-pair
stream. The target brief's "@573" is the 0-based index; the '78 45 13 55 61'
5-gram is at 1-based @574, and "ne mentent" = 1-based @579-582
('94 82 06 06'). The second "ne mentent" window is at 1-based @1183-1186.

## Bar (verbatim, pre-registered)

"(a) parse 'ce verdict [13-55-61] ne mentent [50] …' with the 3pl subject named
and the clause boundary stated; (b) coordinate with name-13-55-61 (merge if X
is the subject)"

## Bar restated (numbered pass/fail clauses; frozen before testing)

1. The frame 'ce verdict [13-55-61] ne mentent [50] …' parses with the 3pl
   subject of "ne mentent" NAMED (a specific group span with a justified value
   or forced class/number).
2. The clause boundary of the "ne mentent" clause is stated.
3. Coordination with name-13-55-61: merge performed iff X is the subject.

## Method

Read BATTERY-PROTOCOL.md first. Re-derived the repaired 1,847-pair stream
independently from `data/upstream-ct_R5005.txt` +
`code/side-keyhunt/repaired_offsets.json` (parsed per
`code/side-keyhunt/repair_parse.py`; verified 1,847 pairs / 96 types).
`canonical.py` never used. R5005, sealed gates, red-team queue untouched.
Every number traces to the stream.

Standing values used (protocol §7 + post-R17/18): banked GT 11=la, 82=m,
29=er, 40=e, 46=que; granted 87=ce, 47="ce" (A4 allophone tier);
promoted 06="ent" (R17-007, conditional on 94="ne" STRONG LEAD), 30="pas";
provisional 59=est, 77="le"; leads 78="ver" (R16-005), 94="ne" STRONG LEAD
(R17-001), 45="ce/dict" (A11 HOLD + R16-004 lead), 76=noun (battery lead);
24=verb class; 67 et/veut sole true polyvalence with the positional rule.

## Window-level evidence (re-derived)

W1 — row a3_02 = 1-based @559-590 (full row, 32 pairs):
`94 59 30 67 11 43 24 80 97 13 76 45 94 52 | 87 78 45 13 55 61 | 94 82 06 06 | 50 10 19 18 14 00 97 41`
= "ne(94) est(59) pas(30) et(67, positional: follower 11 not infinitive-shaped)
la(11) [43] [24=verb] [80] [97] [13] [76=noun] [45] ne(94) [52] | ce(87)
verdict(78-45, LEAD) [13-55-61] | ne(94) mentent(82-06-06, R17-007 conditional)
| [50] [10] [19] [18] [14] pour(00) [97] [41]"

The '78 45 13 55 61' 5-gram census is exactly x2 stream-wide (1-based @574,
row a3_02; @1165, row a6_09). The '94 82 06 06' ("ne mentent") census is
exactly x2 (1-based @579, row a3_02; @1183, row a6_10).

W2 — "ne mentent" @1183-1186 (row a6_10), wide context 1-based @1177-1194:
`32 48 59 37 77 78 | 94 82 06 06 | 59 42 06 84 59 46 07 24`
= "[32] [48] est(59) [37] le(77) ver[78] | ne(94) mentent(82-06-06) | est(59)
[42] [06] on(84) est(59) que(46) [07] [24]"

94-duality evidence (battery-ne-particle-ungrammatical-sweep, evidence-package
grade): BOTH "ne mentent" windows (0-based @578/@1182) are classified
C. PARTICLE-STRAINED — "ne m'ent-ent", doubled 06, no stem; cf. R17-001
"ne-me legs strained". The R17-007 conditional grant of "ne mentent"
(= "ne" + "ment"+"ent", 3pl of mentir) is therefore strained-but-granted;
this battery does not re-litigate the grant.

## Subject hunt

"ne mentent" = negated 3pl verb ("they do not lie"). 1841 French requires an
overt 3pl subject. Candidates in the W1 clause:

1. **"ce verdict" (@573-575)** — singular noun ("verdict" LEAD). Number
   disagreement with 3pl "mentent". REJECTED.
2. **X = [13-55-61] (@576-578)**, the only subject-shaped slot (immediately
   preverbal): "ce verdict, [X] ne mentent" (topic + comment). But X is
   unnameable: name-13-55-61 (verdict null, 2026-10-09) tested H1 (one word
   over 13-55-61) and H2 ("les [55-61]" 3pl-subject hypothesis) — both
   rejected; the underdetermination is structural (13, 55, 61, 43, 21 all
   open; dozens of plural nouns fit "les X ne mentent" equally: témoins,
   hommes, serments, …). No value is forced. UNNAMEABLE — merge cannot fire.
3. **"ce verdict [de X]"** (X complementing "verdict") — subject would be
   "ce verdict de X", still singular. REJECTED on number.
4. **Post-verbal 50 as inverted subject** ("ne mentent-[50=ils]?", interrogative
   inversion): 50 n=11, pre {11x2, 44, 92, 80, 06, 86, 02, 07}, suc {45x2, 88,
   82, 78, 10, 80, 40, 46} — no pronoun evidence; and W2's right context is
   "ne mentent est(59)", not a pronoun, so inversion cannot be the general
   account of the x2 frame. FENCED as unsupported.
5. **Pro-drop / implicit subject** — ungrammatical in French. REJECTED.
6. **"le ver[78]" as W2's subject** (cross-check): singular ("le" provisional)
   vs 3pl verb — disagreement. W2 likewise has NO overt 3pl subject. This
   confirms the gap is systematic across both "ne mentent" windows, not a
   W1-local accident.

"pas" (30) check: the row's only 30 is @561 ("n'est pas", different clause).
No 30 follows "ne mentent" in its clause (row ends @590; next row a4_00 opens
"41 09 00 …"). The bare-"ne" question is red-team territory (R17-007's
conditional grant stands); not re-litigated here.

## Clause boundary (stated per bar)

Left: @573 (87='ce') opens a new nominal clause; it follows the fragment
"@570-572 = 45 94 52" ("[45] ne [52]", verb never arrives) and the complete
"n'est pas" clause @559-561. Right: the clause runs through row end @590
("…[14] pour(00) [97] [41]") into row a4_00 (@591: "41 09 00 92 …"); no
sentence terminator is visible in the window — right boundary indeterminate
at battery grade.

## Per-clause pass/fail

1. **FAIL (epistemic, not kill-grade).** The parse is coherent, but the 3pl
   subject cannot be NAMED: "ce verdict" disagrees in number, X=[13-55-61] is
   structurally unnameable, and no other 3pl NP exists in the clause at either
   window. X *could* be 3pl (e.g. "les témoins"), so the parse is not forced
   false — the failure is lack of evidence, not contradiction.
2. **PASS.** Clause boundary stated above (left @573 firm; right indeterminate
   past row end).
3. **HONORED.** name-13-55-61 coordinated: it is verdict/null, so the merge
   cannot fire. This battery's finding is consistent with (inherits) that null;
   it does not duplicate or overwrite it.

## Adverse

"94='ne' STRONG LEAD caveat (R17-001)" — HONORED. 94='ne' is used throughout;
the duality map's STRAINED classification of both windows is recorded as a
caveat on the frame, not a challenge to the lead. No standing red-team verdict
is contradicted: R17-007 granted 06="ent" (conditional), never the subject;
this null leaves that grant untouched.

## Verdict

**NULL** — W1's "ne mentent" 3pl subject is structurally unidentifiable at
battery grade. The only viable subject slot (X=[13-55-61]) is unnameable, and
the cross-window check (W2 @1183) shows the same subject gap, so this is a
property of the frame, not a W1-local miss. Packaged for the red team: the
R17-007 conditional "ne mentent" grant rests on two clauses with no overt 3pl
subject, and both windows are particle-STRAINED per the 94-duality map.

## Follow-ups proposed (for supervisor queuing)

1. `subj-13-value` (P2) — name 13's value/class (n=12; 13->24 x3 verb-contact
   vs 13->76 noun-contact). A plural-determiner value ("les"/"des") turns W1's
   X into a 3pl NP ("les [55-61] ne mentent") and finds the subject.
2. `subj-55-61-word` (P2) — name the 55-61 word via the W3 window (1-based
   @1206-1207: "43 [55-61] 21", row a6_11) and the 55->81 x6 noun-context legs;
   a plural-noun value ("témoins"/"hommes"/…) completes W1's subject slot.
3. `nementent-W2-subject` (P3) — W2's "ne mentent" (@1183) likewise lacks a 3pl
   subject ("le ver[78]" singular; right context "est [42]"). Decide whether
   both windows share one subject account or the frame needs re-segmentation;
   feed the red-team 94-duality adjudication.

## Bookkeeping

- Report: this file.
- `battery-queue.json`: `w1-573-subject` queued → verdict/null via temp-file +
  rename (pre-write assert confirmed queued/verdictless; JSON re-validated
  post-write). Own entry only.
- Lock created on start (agent id + UTC), deleted on completion.
- `canonical.py` never used. R5005, sealed gates, red-team queue untouched.
- No standing verdict contradicted or downgraded.
