# Battery report: en14-value-tighten

- Target: `en14-value-tighten`
- Verdict: **PROMOTE** (battery grade; red-team ratification of 14=`en` still pending)
- Date: 2026-10-09
- Stream: repaired 1,847-pair / 96-type parse from `code/side-keyhunt/repaired_offsets.json`
  + `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`
  (asserts held: 1847 pairs, 96 types). `canonical.py` never used.
- French frame: 1841 diplomatic French.

## Bar (verbatim)

"fence global 'en' iff any window forces 14 ≠ 'en' value-independently"

## Bar restated as numbered clauses

- (C1) Full 14-window census (n=15) examined window-local.
- (C2) Fence global 'en' iff any window forces 14≠'en' value-independently
  (i.e., under granted standing values alone, with no open-value or
  battery-level premise required).
- (C3) No standing or red-team verdict contradicted or downgraded.

## Method

All 15 14-windows extracted byte-exact from the repaired stream (1-based @,
row, left-3 | right-3, with granted glosses substituted only for readability):

1. @73  a1_02  "24 56 ce | 14 | 24 ce la"
2. @85  a1_02  "51 62 16 | 14 | 06 88 77"
3. @118 a1_03  "68 21 67 | 14 | 21 60 90"
4. @142 a1_04  "65 13 66 | 14 | 74 67 qui"
5. @179 a1_05  "86 21 69 | 14 | 24 ce qui"
6. @340 a2_05  "03 qui 31 | 14 | ce qui par"
7. @425 a2_09  "36 er ce | 14 | 62 e 76"
8. @459 a2_10  "65 13 66 | 14 | 02 tout ce"
9. @587 a3_02  "10 19 18 | 14 | pour 97 41"
10. @624 a4_01  "37 76 m | 14 | 59 37 33"
11. @814 a5_05  "48 24 65 | 14 | er 49 74"
12. @897 a5_08  "01 98 m | 14 | 98 83 86"
13. @1122 a6_07  "pre 12 06 | 14 | 06 la 52"
14. @1366 a7_06  "62 94 tout | 14 | 60 03 30"
15. @1690 a8_05  "62 94 tout | 14 | 60 27 que"

For each window I tested whether, under GRANTED values only
(pencil: 11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que;
promoted/granted: 87=ce, 64=qui, 96=par, 17=fois, 79=tout, 00=pour,
84=on, 47=ce; provisional 59=est, 77=le), the clitic-'en' reading of 14
is grammatically impossible AND 14 is forced to another value.
A "forced" result requires a licensed full-window parse that excludes 'en'.

## Window-level results

- @73: "ce en [24]" — clitic before open 24. No force. PASS.
- @85: all neighbors open. No force. PASS.
- @118: "[68 21] et/veut en [21]" — "et en" is grammatical French
  (67's sole polyvalence covers both arms). No force. PASS.
- @142: open neighbors. No force. PASS.
- @179: "en [24] ce qui" — clitic before relative clause. No force. PASS.
- @340: "qui [31] en ce qui par" — "en ce" is a clean French shape
  ("en ce qui"). No force. PASS.
- @425: "ce en [62]e" — 62 open, 48='e' letter grant (R17). No force. PASS.
- @459: "en [02] tout ce" — the "tout ce" oddity is a 79/87 issue, not
  a 14 issue. No force. PASS.
- @587: "[18] en pour [97]" — closest call. Adjacent prepositions
  "en pour" are strained, but 18 is open and a clitic-licensor for "en"
  cannot be ruled out under granted values alone. NOT a value-independent
  kill (would need 18's class fixed). Recorded as the noted tension, fenced
  as the one window needing an 18-class battery. PASS.
- @624: "m en est [37-pred]" — canonical clitic cluster "m'en est"
  (the already-promoted @622 core uses the same shape). Positive leg. PASS.
- @814: "[65] en er[49]" — "en" + infinitive shape ("en [inf]").
  No force. PASS.
- @897: "[01] 98 m en 98 de 86" — "m'en" cluster again. Positive leg
  (note: the @894 "vient m'[14-inf]" conditional parse is already dead
  under the lane-wide 14-verb NULL fence; the clitic arm is untouched).
  PASS.
- @1122: "pre[12] [06] en [06] la" — open neighbors. No force. PASS.
- @1366: "[62] 94 tout en [60]" — "tout en [60]" frame (corroborated by
  the two tout-en windows at battery grade). Positive leg. PASS.
- @1690: same "tout en [60]" frame. Positive leg. PASS.

Score: 15/15 pass, 0 windows force 14≠'en' value-independently.

## Per-clause verdict

- (C1) PASS — full 15-window census, byte-exact, all windows examined.
- (C2) PASS — the fence antecedent is false on the complete census;
  no fence triggered. The four positive legs (@624 "m'en est", @897 "m'en",
  @1366/@1690 "tout en [60]") corroborate the clitic arm.
- (C3) PASS — no standing verdict contradicted. Standing kills on 14 are
  only "uniform 14 verb stem" (this is a clitic, not a verb stem); the
  lane-wide 14-verb NULL fence (stem-14-84-retest) is battery-level and
  untouched; the red-team 14=`en` ratification docket is untouched and
  still the venue for the value decision.

## Verdict: PROMOTE

Global 14='en' survives the kill-grade tighten at battery grade: zero of
15 windows forces a value-independent contradiction. This hardens the
14=`en` red-team input; it does not adjudicate 14's value.

## Adverses

None listed.

## Caveats

- Value-independence cuts both ways: the positive legs rest on
  battery-level/provisional neighbors (94='ne' lead, 98='vient' battery,
  62='il' battery, 30=pas red-team-promoted, 59=est provisional) — they
  corroborate, they do not grant.
- Canonicality: several windows sit on rows whose upstream offsets are
  unvalidated (68/70 rows); this is a canonical-stream verdict per protocol.
- @587's "en pour" strain is the residual watch-item for a future 18-class
  battery; it does not reach kill grade under current grants.
