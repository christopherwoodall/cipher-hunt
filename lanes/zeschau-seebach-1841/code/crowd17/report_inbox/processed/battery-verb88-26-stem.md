# Battery report: verb88-26-stem

**Target:** `verb88-26-stem` (P2)
**Date:** 2026-10-09
**Verdict:** KILL

## Bar (verbatim from queue)

"Name the stem value iff one covers all 23 windows with zero hard contradictions."

## Bar restated as numbered clauses

1. One stem value (from the vient-family candidate set: viennent/tiennent/reviennent/deviennent, per the parent battery's @1706 fused-3pl read) covers all 23 windows of 88 with zero hard contradictions under standing values.
2. If clause 1 fails at kill grade (≥1 window forces the claim false), the uniform stem hypothesis is killed and no stem is named.

## Method

Read BATTERY-PROTOCOL.md first; created `locks/verb88-26-stem.lock` (deleted on completion).
Re-derived the repaired 1,847-pair / 96-type stream in-session from
`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`
(asserts hold: 1,847 pairs, 96 types). `canonical.py` never used.
R5005, sealed gates, red-team adjudication queue untouched.

88 occurs exactly 23× (0-based @42, @86, @210, @304, @306, @334, @402, @497,
@513, @616, @619, @646, @730, @765, @904, @1049, @1117, @1260, @1267, @1514,
@1541, @1706, @1727). The "88 26" bigram occurs exactly 1× stream-wide (@1706).

Standing values used as premises only: banked GT (11=la, 70=pre, 82=m, 34=i,
29=er, 40=e, 46=que); granted (87=ce, 64=qui, 96=par, 17=fois, 79=tout, 00=pour,
84=on, 47=ce); provisional (59=est, 77=le); 24=finite-modal (promoted;
`24-en-verb-conflict` live at red team); 88=verb class (battery-grade);
94=ne (R17-001 STRONG LEAD); 98=vient (battery-PROMOTE, vient-98-name);
30=pas (conditional promote); 06=ent standalone, no rightward attachment
(ent-right-attach-sweep KILL); 48=inflectional-'e' (promoted); 70-12="prenne"
family (distrib-12).

## Window-level evidence

Test: at each window, can 88 be read as the vient-family verb (finite
"tient/revient/devient" or verb stem in a longer word) with a grammatical
local parse under standing values? A hard contradiction = no grammatical
reading exists. Word-internal rescue (88+follower as one word) checked per
window; it requires a licensed French word and never materializes
("tient-le"/"tient-la" enclitics on a finite verb ungrammatical; "tienter",
"tiente", "tient-pre" not French; 43/10/18/66/01/24 followers supply no
licensed inflection).

**16 windows force hard contradictions:**

- @42 (a1_01) `01 24 88 43`: 24=finite-modal promoted; "24-fin tient" = two
  finite verbs, ungrammatical. FAIL.
- @86 (a1_02) `06 88 77`: 06="ent" standalone (rightward attachment killed);
  "ent tient le" ungrammatical. FAIL.
- @334 (a2_05) `54 88 40`: "tient"+"e" (40=e letter GT) = "tiente", not French;
  "ce [54] tient e" ungrammatical. FAIL.
- @513 (a3_00) `98 65 88 56`: 98=vient (promote) + 65=noun; "vient X tient"
  = two finite verbs, no conjunction. FAIL.
- @616 (a4_00) `70 88 10`: "pre-tient" not a French word; "ce [83] pre tient"
  ungrammatical. FAIL.
- @619 (a4_01) `88 10 29`: "[10]er" infinitive (29=er GT); "tient [inf] tient"
  ungrammatical. FAIL.
- @646 (a4_02) `24 87 61 88`: 24=finite-modal; "24-fin ceci tient" = two
  finites. FAIL (rests on promoted 24; red-team `24-en-verb-conflict` could
  re-open).
- @730 (a5_02) `48 88 11`: 00=pour (A9) governs infinitive; finite "tient"
  after "pour X" ungrammatical; vient-family has no infinitive shaped "tient".
  FAIL.
- @765 (a5_03) `59 39 88 66`: "n'est X tient" = two finites (59=est
  provisional, 98=vient context). FAIL.
- @904 (a5_09) `16 88 18`: 67=et/veut; "veut [16] tient" ungrammatical under
  both 67 arms and both 16 arms (infinitive vs locus-"a"). FAIL.
- @1049 (a6_04) `41 88 29`: "tienter" not French; "[88]er" infinitive
  impossible for vient-family. FAIL.
- @1117 (a6_07) `11 88 70`: "tient prenne" (70-12="prenne") = two verbs;
  "pas cela tient prenne" ungrammatical under both cela branches. FAIL.
- @1260 (a7_02) `69 88 01`: "[31]er ce tient" = infinitive + "ce tient"
  ungrammatical; 01 dead-general. FAIL.
- @1267 (a7_02) `69 88 24`: "que ce tient [24-fin]" = two finites. FAIL
  (rests on promoted 24).
- @1514 (a7_11) `81 88 11`: "est [39] [81] tient la" = two finites (59=est
  provisional). FAIL.
- @1727 (a8_07) `39 88 24`: "vient X tient" (98=vient upstream) = two finites.
  FAIL.

**7 windows admit a grammatical vient-family reading (no hard contradiction):**

- @210 `50 88 19`: "le [50] tient [19]" — NP subject + finite verb. CLEAN.
- @304 `89 88 02`: "[89-noun] tient [02]" — conditional on 89's noun arm
  (fenced split). CONDITIONAL.
- @306 `02 88 20`: "[02] tient [20]" — "X tient Y" shape. CLEAN.
- @402 `45 88 53`: "ce [88-verb]" per ce88-leftedge-402 PROMOTE
  ("ce tient" = demonstrative pronoun + finite verb). CLEAN.
- @497 `79 88 47`: "tout tient ce" — "tout" as pronoun subject. CLEAN.
- @1541 `93 88 77`: "[93] tient le [78]" — "X tient le Y". CLEAN.
- @1706 `94 88 26 12 06`: fused 3pl "ne viennent" (parent battery). CLEAN.

## Per-clause pass/fail

1. **FAIL at kill grade.** 16 of 23 windows force the vient-family stem false
   under standing values. The failures are structural (two-finite-verb
   sequences, bare stems with no licensed inflection, "pour"+finite) and
   prefix-independent — no member of the candidate set (viennent/tiennent/
   reviennent/deviennent) escapes them.
2. **Kill disjunct fires.** No stem value is named.

## Adverses

- Sibling `fuse-88-26-redteam` §7 conditioned-claims package (88-26-12-06
  fusion, 26 word-internal, 62 plural-subject): NOT duplicated — this battery
  tested only the uniform stem-value claim; the conditioned package remains
  red-team venue, untouched.
- Homophony note (moot): naming "vient" would collide with battery-promoted
  98="vient"; since no stem is named, no homophony is declared.
- 88=verb class (battery-grade) is NOT contradicted — the kill is of the
  specific uniform stem value, not of 88's verb class.

## Verdict: KILL

The uniform "88-26 as a verb stem" hypothesis (vient-family) is killed at bar
grade: 16/23 windows admit no grammatical parse under standing values. The
@1706 fused-3pl read remains a valid locus-level parse but does not
generalize. Three failing windows (@42, @646, @1267) rest on promoted
24=finite-modal and would re-open only if the red-team `24-en-verb-conflict`
docket resolves 24="en".

## Bookkeeping

- Lock `code/crowd17/next-token/locks/verb88-26-stem.lock` created
  2026-10-09T07:58:06Z, deleted on completion.
- `battery-queue.json`: `verb88-26-stem` queued -> verdict/kill
  (temp-file + rename; pre-write assert confirmed no prior verdict; own entry
  only; JSON re-validated).
- R5005, sealed gates, red-team adjudication queue untouched. §7 intact.
