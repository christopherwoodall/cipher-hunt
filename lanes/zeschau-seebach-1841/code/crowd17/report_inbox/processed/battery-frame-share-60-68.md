# Battery report — frame-share-60-68

Worker: fb75b723-e699-49a7-bb9c-0f03dd1881af. Date: 2026-10-08 (UTC 2026-10-09).
Lock: created on start, deleted on completion. No stale lock found.

## Bar (verbatim, copied from battery-queue.json before testing)

"(a) exhaustive shared-frame census over free tokens: shared successor types, shared predecessor types, shared trigrams centered on the cell; (b) each shared frame gets a window-level parse under stated values; (c) if zero shared frames exist, record that as the standing negative."

## Bar restated as numbered pass/fail clauses (pre-registered before testing)

1. Census lists every successor type shared by 60 and 68 over free tokens, with counts. (pass/fail)
2. Census lists every predecessor type shared by 60 and 68 over free tokens, with counts. (pass/fail)
3. Census lists every trigram context (pred, succ) centered on the cell shared by 60 and 68, with counts. (pass/fail)
4. Every shared frame found in clauses 1–3 gets a window-level parse under the stated banked/promoted values. (pass/fail)
5. If zero shared frames exist, the report records that as the standing negative. (pass/fail)

## Method

Stream: the repaired 1,847-pair parse. Source: `code/side-keyhunt/repaired_offsets.json`
+ `data/upstream-ct_R5005.txt`, parsed exactly like `code/side-keyhunt/repair_parse.py`
(pair phase per row from the repaired offsets; global @-offsets assigned in row order).
`code/side-keyhunt/canonical.py` was not used. R5005 was not touched.

Free tokens only: occurrences at global positions @227 and @1783 (both hold token
98, the 'parvenir' formula slots) are excluded as cells, predecessors, and successors.
Cells: 60 occurs 18 times (all free); 68 occurs 8 times (all free).
No 60 or 68 occurrence is adjacent to a formula slot.

Window parses use the stated values from protocol §7
(11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que, 87=ce, 64=qui, 96=par,
17=fois, 79=tout, 00=pour, 84=on, 47=ce, 59=est, 77=le).
60 and 68 themselves carry no stated value; they are glossed as their bare numbers.

## Census result

Shared successor types (clause 1): **{06}: 60→06 ×1, 68→06 ×1.**
Shared predecessor types (clause 2): **{21}: 21→60 ×4, 21→68 ×1.**
Shared centered trigrams (clause 3): **none.**

Full context distributions (free tokens only):
- 60 successors: 03 ×4, 08 ×2, 71 ×2, 67 ×2, 12 ×2, 90 ×1, 09 ×1, 15 ×1, 65 ×1, 06 ×1, 27 ×1 (18 total).
- 68 successors: 21 ×2, 37 ×1, 00 ×1, 52 ×1, 59 ×1, 06 ×1, 47 ×1 (8 total).
- 60 predecessors: 21 ×4, 92 ×2, 14 ×2, 06 ×2, 77 ×1, 46 ×1, 29 ×1, 94 ×1, 03 ×1, 64 ×1, 53 ×1, 98 ×1 (18 total).
- 68 predecessors: 89 ×1, 39 ×1, 79 ×1, 55 ×1, 65 ×1, 52 ×1, 47 ×1, 21 ×1 (8 total).

Discrepancy note: the target's evidence field says the earlier battery found
"shared pred empty". This census on the repaired stream finds 21→60 ×4 and
21→68 ×1, at rows a1_03, a1_05, a2_00, a2_01, a8_09 — none adjacent to a formula
slot and none inside repaired row a5_03, so the difference is not a repair
artifact. The earlier battery undercounted. This does not touch any standing
verdict (see verdict note below).

## Window-level evidence

### Shared successor frame 06 — cell 60 @1474 → 06 @1475 [row a7_10]

- @1468 62(62) [a7_09]
- @1469 38(38) [a7_09]
- @1470 26(26) [a7_10]
- @1471 12(12) [a7_10]
- @1472 41(41) [a7_10]
- @1473 53(53) [a7_10]
- @1474 60(60) [a7_10] <==CELL
- @1475 06(06) [a7_10]
- @1476 67(67) [a7_10]
- @1477 33(33) [a7_10]
- @1478 29(er) [a7_10]
- @1479 82(m) [a7_10]
- @1480 16(16) [a7_10]

### Shared successor frame 06 — cell 68 @1719 → 06 @1720 [row a8_07]

- @1713 94(94) [a8_06]
- @1714 44(44) [a8_06]
- @1715 59(est) [a8_06]
- @1716 30(30) [a8_06]
- @1717 64(qui) [a8_06]
- @1718 47(ce) [a8_06]
- @1719 68(68) [a8_07] <==CELL
- @1720 06(06) [a8_07]
- @1721 11(la) [a8_07]
- @1722 52(52) [a8_07]
- @1723 37(37) [a8_07]
- @1724 43(43) [a8_07]
- @1725 98(98) [a8_07]

### Shared predecessor frame 21 — 21→60 ×4

21 @118 → 60 @119 [a1_03]: ... @115 21(21), @116 67(67), @117 14(14), @118 21(21),
@119 60(60) <==CELL, @120 90(90), @121 19(19), @122 58(58), @123 66(66),
@124 98(98), @125 82(m).

21 @171 → 60 @172 [a1_05]: @166 82(m), @167 84(on), @168 53(53), @169 12(12),
@170 48(48), @171 21(21), @172 60(60) <==CELL, @173 09(09), @174 87(ce),
@175 86(86), @176 21(21), @177 69(69), @178 14(14).

21 @196 → 60 @197 [a2_00]: @191 87(ce), @192 98(98), @193 56(56), @194 47(ce),
@195 01(01), @196 21(21), @197 60(60) <==CELL, @198 08(08), @199 67(67),
@200 76(76), @201 87(ce), @202 11(la), @203 92(92).

21 @231 → 60 @232 [a2_01]: @226 46(que), @227 98(98, FORMULA SLOT — excluded
from census, shown for position), @228 83(83), @229 82(m), @230 96(par),
@231 21(21), @232 60(60) <==CELL, @233 71(71), @234 51(51), @235 70(pre),
@236 98(98), @237 41(41), @238 17(fois).

### Shared predecessor frame 21 — 21→68 ×1

21 @1787 → 68 @1788 [a8_09]: @1782 23(23), @1783 98(98, FORMULA SLOT —
excluded from census, shown for position), @1784 83(83), @1785 82(m),
@1786 96(par), @1787 21(21), @1788 68(68) <==CELL, @1789 47(ce), @1790 03(03),
@1791 00(pour), @1792 86(86), @1793 56(56), @1794 42(42).

### Centered trigrams

No (pred, succ) context is shared between 60 and 68. The 21-predecessor
occurrences pair with successors {90, 09, 08, 71} for 60 and {47} for 68 —
no overlap.

## Per-clause pass/fail

1. Shared successor census — PASS. Shared set {06}: 1×/1×.
2. Shared predecessor census — PASS. Shared set {21}: 4×/1×.
3. Shared centered-trigram census — PASS. Empty set, exhaustively checked.
4. Window-level parses of every shared frame — PASS. 2 successor windows + 5
   predecessor windows parsed under stated values above.
5. Zero-shared-frames negative — N/A. Shared frames exist.

## Verdict: PROMOTE (census fact only)

The positive disjunct of the claim is established: 60 and 68 share free frames —
successor frame 06 (1 occurrence each) and predecessor frame 21 (4× before 60,
1× before 68). No shared centered trigram exists.

Adverse answered (fenced, not ignored): "a single shared 06-token is thin; do
not over-read it." The 06 successor frame is one occurrence per cell — it cannot
support any interchangeability inference, and none is drawn. The 21 predecessor
frame (4×/1×) is likewise thin in absolute terms, and the lane's standing kill
from pair-60-68-readjudicate (predecessor distributional similarity rejected at
p≈0.05347) is not disturbed by this census: raw shared-type counts are not a
similarity test, and this report does not re-litigate that kill. Per the
thirds-60-68-pair null, distributions alone cannot demonstrate interchangeability;
this promotion covers the census fact only and makes no homophone claim.

No follow-up targets are required (verdict is not null).
