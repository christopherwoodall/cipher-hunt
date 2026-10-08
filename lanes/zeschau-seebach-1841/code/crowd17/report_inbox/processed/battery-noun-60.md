# Battery report: noun-60 (60's masculine-noun value)

Worker: a1d2abb9-4a3c-4b84-b6eb-3754fc8a2907. Date: 2026-10-08.
Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json +
data/upstream-ct_R5005.txt), parsed per code/side-keyhunt/repair_parse.py.
canonical.py never used. R5005 never touched. @i = 0-based pair index.
No red-team verdict on 60 exists (checked next-token-redteam.md and
next-token-redteam-r17.md) — no contradiction, no escalation.

## Bar (verbatim, pre-registered before testing)

"promote iff 'le [60]' plus >=2 '60 03' NP-frames cohere under one nominal value"

Numbered clauses (fixed before data examination):

1. (C1) 'le [60]' @454 parses as article + masculine noun with 60 taking
   one nominal value (77='le' provisional per §7).
2. (C2) At least 2 of the 3 non-frame-family '60 03' windows (@690, @1644,
   @1674) parse as NP-frames with 60 taking the SAME nominal value as in
   C1, zero contradictions. (@1366 '14 60 03' excluded: it belongs to the
   frame-62-94-79 family whose bar is owned by queued
   frame-62-94-79-reparse — not duplicated here.)
3. (C3) Adverse answered: "value unnamed" — a value is named, or the
   bar's coherence is established and the unnamed-value residual is
   fenced with stated cause. (Per protocol, promote requires every
   listed adverse answered, not ignored.)
4. (C4, kill-check) No window of 60 forces the nominal claim false, and
   no cleaner rival class is demonstrated on the same frames.

## Method

Fresh parse per protocol; no prior counts trusted. All 18 windows of 60
scanned (n=18: @119, 172, 197, 232, 322, 454, 637, 690, 700, 995, 1338,
1366, 1474, 1563, 1644, 1674, 1690, 1735). Predecessor census: 21 x4,
92 x2, 14 x2, 06 x2, 77, 46, 29, 94, 03, 64, 53, 98. Successor census:
03 x4, 08 x2, 71 x2, 67 x2, 12 x2, 90, 09, 15, 65, 06, 27.
'60 03' x4 (@690, @1366, @1644, @1674). Standing values used: banked
11=la, 29=er, 46=que; granted 64=qui, 47=ce (A4); provisional 77=le,
59=est; battery-promoted 94=ne, 39=a/a (allophone tier), 12=n (letter).

Offset correction to queue evidence: the queue cites '60 03' at
@1644/@1675/@691 — on the repaired stream the 60-positions are @1644,
@1674, @690 (@1675/@691 are the 03 positions, not the 60 positions).
Attribution correction to the frame-62-94-79 battery: its "'ce [03]'
@1014/@1790" is via 47='ce' (granted A4), not 87='ce' — '87 03' occurs
x0 on the repaired stream. The 03=noun support itself stands:
'le [03]' @722 (77='le' provisional) + 'ce [03]' x2 @1014/@1790
(47='ce' granted).

## Window-level evidence

W1 — 'le [60]' @454 (row a2_10):
@448 59 @449 32 @450 48 @451 79 @452 17 @453 77 @454 60 @455 65 @456 13
@457 66 @458 14 @459 02 @460 79 @461 87 @462 11 @463 59 @464 42
Reads: "...est[59] [32] e[48] tout[79] fois[17] le[77] [60] [65] [13]..."
Under 60 = masculine noun: "le [N] [65]" requires 65 to be adjectival
or a complement — unattested. 65's profile (n=25): '65 qui' x3 (@724,
@1208, @1340 — nominal antecedent of relative 'qui'), '29-40-65' x3
direct-object slot (per queued prof-65). 65 is noun-shaped, not
adjective-shaped. Under rival 60 = masculine adjective: "le [adj]
[65-N]" parses cleanly with supported values.

W2 — '60 03' @690 (row a5_00):
@684 64 @685 29 @686 40 @687 65 @688 94 @689 29 @690 60 @691 03 @692 39
@693 74 @694 46 @695 02
Reads: "...qui[64] [29-er] e[40] [65] ne[94] [29-er] [60] [03] a[39] [74]
que[46]..." Local frame: "[60] [03] a [74] que". Under 60=noun:
"[N] [03] a [74] que" requires 03 adjectival — unattested; 03 is
noun-shaped ('le [03]' @722, 'ce [03]' x2) and verb-stem-shaped
('[03]er' @1030/@1320/@1594, per queued stem-03). Under rival
60=adjective: "[adj] [03-N] a [74] que" parses cleanly.

W3 — '60 03' @1644 (row a8_04):
@1640 56 @1641 12 @1642 33 @1643 98 @1644 60 @1645 03 @1646 64 @1647 31
@1648 10 @1649 03
Reads: "...n'[12] [33-inf] [98] [60] [03] qui[64] [31]..." Local frame:
"[60] [03] qui [31]". Under 60=noun: "[N] [03] qui [V]" requires 03
adjectival — unattested (same 03 profile as W2). Under rival
60=adjective: "[adj] [03-N] qui [31-V]" parses cleanly.

W4 — '60 03' @1674 (row a8_05):
@1670 78 @1671 55 @1672 81 @1673 92 @1674 60 @1675 03 @1676 39 @1677 74
@1678 77 @1679 44
Reads: "...[92] [60] [03] a[39] [74] le[77] [44]..." Local frame:
"[60] [03] a [74] le". Same verdict as W2: needs unattested 03=adj
under the noun claim; clean under 60=adj + 03=noun.

K1 — kill window @1338 (row a7_05):
@1334 83 @1335 86 @1336 71 @1337 64 @1338 60 @1339 08 @1340 65 @1341 64
Reads: "...[86-inf] [71] qui[64] [60] [08] [65] qui[64]..." — "qui [60]
[08]". 64='qui' is red-team granted. A subject relative 'qui' must be
followed by a verb (finite, or verb+clitics); 60 is not a clitic. With
60 nominal, "qui [60-noun]" is ungrammatical — 60 is forced into a verb
slot. The only rescue is 60 noun/verb polyvalence, which per §7 is a
red-team declaration (67 et/veut is the sole true polyvalence), not
available at battery level. Kill-grade.

K2 — kill window @700 (row a5_01):
@696 50 @697 45 @698 28 @699 94 @700 60 @701 12 @702 98 @703 20
Reads: "...[28] ne[94] [60] n[12] [98]..." — "ne [60] n [98]". 94='ne'
battery-promoted; 'ne' must be followed by a verb. With 60 nominal,
"ne [60-noun]" is ungrammatical — 60 forced verbal (12='n' letter reads
as the verb's final: "ne [V-60]n [98]"). Kill-grade, independent of K1.

Other 60 windows scanned for class evidence (no additional kill-grade
hits, none rescue the nominal claim): @119/@172/@197 '21 60' x3 + @232
'21 60' (vient-parvenir formula third — thirds question owned by queued
frame-vient-parvenir); @322 '92 60 15'; @637 '46 60 67' ("que [60]
et[67]"); @995 '03 60 67'; @1366/@1690 '14 60' (62-94-79 family,
14's value owned by queued tout-slot-14 — not touched); @1474
'53 60 06'; @1563/@1735 '06 60' x2 ('06 60 71', '06 60 12').

## Per-clause pass/fail

- C1: FAIL at promote grade. "le [60] [65]" under 60=noun needs
  unattested 65=adjectival; 65 is noun-shaped ('65 qui' x3,
  direct-object slot x3). The frame parses cleanly only under the
  rival 60=adjective reading.
- C2: FAIL. 0 of 3 '60 03' frames cohere under 60=noun without the
  unattested 03=adjectival assumption. All 3 parse cleanly under the
  rival 60=adjective + 03=noun reading with independently-supported
  values.
- C3: FAIL (unanswered). No nominal value can be named; coherence
  itself fails, so there is nothing to fence.
- C4: KILL GRADE MET on both prongs. (a) Two independent windows
  force the nominal claim false: @1338 "qui [60]" and @700 "ne [60]"
  both place 60 in a verb-only slot. (b) A cleaner rival class is
  demonstrated on the bar's own frames: 60 = masculine adjective,
  03 = masculine noun — W1 "le [adj] [65-N]", W2/W4 "[adj] [N] a
  [74] que", W3 "[adj] [N] qui [V]" — all with zero unattested
  assumptions, versus two (03=adj, 65=adj) required by the noun claim.

## Verdict

**kill** — 60's masculine-noun value is killed. The bar's coherence
fails on all four frames under the nominal reading (C1, C2), the
adverse is unanswerable (C3), and two independent windows force 60
into verb slots (@1338 'qui 60', @700 'ne 60'), which is kill-grade
per the protocol. A cleaner rival class (60 = masculine adjective;
03 = masculine noun) is demonstrated on the same frames.

Note for the red team (not an escalation — no standing verdict is
contradicted): if 60 is adjectival in the NP frames but verbal at
@1338/@700, that is a second polyvalence claim and needs red-team
declaration per §7. Alternatively the verbal windows may re-parse
under a single verbal value for 60 (see follow-up 2).

## Follow-ups (work regenerates)

1. **adj-60** (priority 2): battery for 60 = masculine adjective.
   Bar: "promote iff 'le [60-adj] [65-N]' @454 plus >=2 of the
   @690/@1644/@1674 '[60] [03-N]' frames cohere with 65 and 03
   nominal (both independently supported: '65 qui' x3 @724/@1208/
   @1340; 'le [03]' @722, 'ce [03]' @1014/@1790 via 47='ce') and
   zero contradictions." Kill-check must include @1338/@700.
2. **verb-60** (priority 2): class 60's verbal windows — @1338
   'qui 60 08', @700 'ne 60 12', @995 '03 60 67', @1474 '53 60 06',
   @1563 '06 60 71', @1735 '06 60 12'. Bar: "resolve iff one verbal
   value (or stated positional rule) covers all six windows; if the
   NP-frame adjective reading also holds, frame the polyvalence
   question for red-team declaration per §7 (67 sole true
   polyvalence)."
3. Coordination notes (no new targets): 14's value at @1366/@1690
   belongs to queued **tout-slot-14** (untouched); the 60/62/68
   thirds question at @232 belongs to queued **frame-vient-parvenir**
   (untouched); the @1366 '60 03' instance belongs to queued
   **frame-62-94-79-reparse** (untouched).
