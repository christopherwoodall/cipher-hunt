# Battery report: frame-43-pred-37-32

Worker: 53a98a2b-436a-4339-a271-1839c4470c62
UTC: 2026-10-09T06:16:25Z
Lane: zeschau-seebach-1841, crowd17 next-token pipeline
Stream: 1,847-pair repaired parse (repaired_offsets.json + upstream-ct_R5005.txt,
parsed like repair_parse.py). canonical.py NOT used. R5005 NOT touched.

## Bar (verbatim)

"resolve iff (a) all four windows parse under one structural reading
(predicative-adjective + noun vs compound word vs 43-as-infinitive); (b) the
reading coheres with A1's predicative-frame grant for 37/32 (frame only, value
open - no re-litigation); (c) 43's noun-hood vs verb-hood is stated with the
la-43 frames as control".

## Bar as numbered clauses

1. All four 37/32-43 windows parse under one structural reading.
2. The reading uses A1's predicative-frame grant for 37/32 only. 37's value
   stays open. No re-litigation of 37.
3. 43's noun-hood vs verb-hood is stated, with the la-43 frames as control.

## Method

1. Parsed the repaired stream. Counted every 37/32-43 adjacency.
2. Pulled a wide window (+/-6) around each of the four hits.
3. Pulled every la-43 frame in the stream (the control).
4. Pulled the two adverse frames: 06-43-07 and ce-43-55.
5. Tested the three rival readings against each window.

Terms: "predicative" = adjective in a predicate slot (frame granted by A1 for
37/32/42). "Noun-class" = 43 acts as a noun (head of a noun phrase), not as a
verb or infinitive. "Control" = the la-43 frame, used as a fixed reference for
43's class.

## Window evidence (@-offsets; 43 sits at offset+1)

Exactly 4 adjacencies 37/32-43 exist in the stream. Offsets name the 37/32
position.

- W-A: 32-43 @257 (row a2_02):
  `01@255 91@256 32@257 43@258 77@259 84@260 74@261 45@262`
  Right edge: 77=le (provisional), 84=on (promoted).
- W-B: 37-43 @385 (row a2_07):
  `82@381 16@382 52@383 38@384 37@385 43@386 91@387 36@388 62@389 91@390`
  Right edge unglossed. Left edge: 52-38 before 37.
- W-C: 37-43 @1125 (row a6_07):
  `14@1121 06@1122 11@1123 52@1124 37@1125 43@1126 00@1127 86@1128`
  Right edge: 00=pour (promoted, A9). Left edge: 11=la, 52.
- W-D: 37-43 @1723 (row a8_07):
  `68@1719 06@1720 11@1721 52@1722 37@1723 43@1724 98@1725 39@1726 88@1727 24@1728`
  Right edge unglossed. Left edge: 11=la, 52 (same as W-C).

Note: 43 occurs 16 times total. Other left neighbors: 96 x2; 82, 88, 56, 46,
11, 06, 47, 08, 21, 78 (x1 each). Right neighbors: 00 x3, 77 x2, 87 x2, 98 x2,
rest x1.

## Control: la-43 frames

One la-43 frame exists in the whole stream, @562-563 (row a3_02):

`59@559 30@560 67@561 11@562 43@563 24@564 80@565 97@566 13@567`

59=est (provisional). 80 is a granted verb-frame (A8). 67 is the sole
polyvalence (et/veut). The follower of 67 is 11=la, a banked value, not
infinitive-shaped. The standing 67 positional rule therefore gives 67=et.
Reading: "est 30 et la 43 24 [verb-frame 80]". This is determiner + noun +
verb clause. The rival parse (67=veut, la as object pronoun, 43 as verb or
infinitive) is blocked by the standing 67 rule. The control states 43 as
noun-class. Caveat: single instance.

## Adverses

AD-1: "37's value open (frame-37-reexam queued)". FENCED, cause: orthogonal.
The structural verdict uses only A1's frame grant for 37/32. It does not need
37's value. 37's value stays open. frame-37-reexam can later split the
adjective+noun vs compound sub-distinction, which is value-dependent.

AD-2a: "06-43-07 @1092 lacks predicative left edge". ANSWERED. Frame (row
a6_06): `80@1090 06@1091 43@1092 07@1093 55@1094 81@1095`. 80 is a verb-frame.
06-43-07 sits in post-verbal complement position. That is a normal object-noun
slot. 06 and 07 are unglossed, so no finer test is possible (fenced remainder).
Nothing here forces verb-hood on 43. The claim never required every 43 to be
predicative-led.

AD-2b: "ce-43-55 @1204 lacks predicative left edge". ANSWERED. Frame (row
a7_00): `45@1201 58@1202 47@1203 43@1204 55@1205 61@1206`. 47=ce (promoted,
A4). This is determiner + 43 + modifier: the same determiner-noun pattern as
the la-43 control. It supports noun-class 43. It does not contradict the
claim. The missing predicative left edge is scope, not a contradiction.

## Per-clause pass/fail

Clause 1 (one structural reading for all four windows): PASS.
The noun-class family parses all four windows:
- W-A: predicative-adjective (32) + noun (43), then new clause "le on" (84=on).
- W-B: predicative-adjective (37) + noun (43); right edge unglossed, no
  contradiction.
- W-C: predicative-adjective (37) + noun (43), then "pour 86": adjective +
  noun + pour + infinitive-slot is textbook French.
- W-D: same as W-B (shares the la-52 left edge with W-C).
The rival 43-as-infinitive reading FAILS on W-C (bare infinitive after an
adjective, followed by a pour-licensed second infinitive, is not French) and
on W-A (bare infinitive followed by "le on" is not French).
Unresolved sub-distinction: predicative-adjective + noun vs compound word.
Both are noun-class. The split needs 37's value, which is open (AD-1). Fenced.

Clause 2 (coheres with A1, 37's value open, no re-litigation): PASS.
The reading assigns 37/32 to the A1 predicative frame and nothing more. 37's
value is untouched and stays open. 52 precedes 37 in three of four windows
(and in frames @1129, @1356, @1416), but its role is not adjudicated here.

Clause 3 (43's class stated with la-43 as control): PASS.
43 = noun-class. Control: la-43 @562-563 reads as article + noun under the
standing 67 positional rule (67=et, follower la not infinitive-shaped).
The rival verb/infinitive parse of the control is blocked by that rule.
Adverse frames AD-2a/AD-2b are compatible with noun-43; AD-2b (ce-43)
repeats the determiner-noun pattern of the control.

## Verdict: PROMOTE (recommend ratification by the red team)

Proposed standing: 43 is noun-class. In the four 37/32-43 windows, 37/32
holds the A1 predicative frame (adjective) and 43 is the head noun (or 37-43
is a compound noun; the split awaits 37's value). 43-as-infinitive is
rejected on W-A and W-C.

This is a class promotion, NOT a value promotion. No value is assigned to 43,
37, or 32. No standing §7 value is contradicted. No red-team escalation.

Caveats recorded with the verdict:
- The la-43 control is a single instance (@562-563).
- The adjective+noun vs compound split is unresolved (value-dependent).
- W-C predicts 86 holds an infinitive slot ("pour 86"). This is a prediction,
  not a fact. A future battery can test it.
- W-A's "le" reading relies on provisional 77=le; the clause break on
  promoted 84=on holds without it.

## Numbers trace

All offsets index the 1,847-pair repaired stream. 37/32-43 count = 4
(@257, @385, @1125, @1723). la-43 count = 1 (@562-563). 06-43-07 count = 1
(@1091-1093). 47-43-55 count = 1 (@1203-1205). 43 total = 16. No invented data.
