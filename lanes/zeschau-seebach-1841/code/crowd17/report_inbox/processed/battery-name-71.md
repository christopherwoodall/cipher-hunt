# Battery verdict: name-71

**Bar (verbatim from battery-queue.json):** "resolve iff a value is attached with >=2 frame-legs; fence as residual if the data stays thin"

**Bar restated:**
- C1 (name): a value for 71 is attached with >=2 independent frame-legs parsing under standing values.
- C2 (fence): if the data stays thin, 71 is fenced as a residual.

**Adverses:** thin data; value fully open.

## Method
Read BATTERY-PROTOCOL.md first. Created `locks/name-71.lock` on start. Re-derived the repaired stream from `data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`: 1,847 pairs / 96 types verified. `canonical.py` never touched; R5005, sealed gates, red-team adjudication queue untouched. Offsets below are 1-based on the repaired stream.

## Census (byte-exact)
71 n=7. Predecessors: 60 x2, 63, 48, 65, 86, 83. Successors: 51, 10, 12, 17, 64, 50, 48 (each x1).

| Window | Row | Context (±5) |
|---|---|---|
| 1b@234 | a2_01 | 98 83 82 96 21 [60 71] 51 70 98 41 |
| 1b@326 | a2_05 | 06 11 92 60 15 [63 71] 10 01 19 00 |
| 1b@712 | a5_01 | 66 21 35 53 12 [48 71] 12 63 00 66 |
| 1b@925 | a5_10 | 49 74 74 40 08 [65 71] 17 61 96 48 |
| 1b@1337 | a7_05 | 94 70 52 39 83 [86 71] 64 60 08 65 |
| 1b@1565 | a8_01 | 17 11 26 30 06 [60 71] 50 29 24 74 |
| 1b@1614 | a8_03 | 92 65 23 08 55 [83 71] 48 31 76 42 |

Only two windows have a banked/granted contact: @925 (follower 17='fois', granted) and @1337 (follower 64='qui', granted).

## C1: FAIL — no value attaches with >=2 legs
Tested candidate shapes against the two banked-contact windows:
- @925 "65 71 17(fois)": the "X fois" frame wants a quantifier/determiner/numeral ("chaque fois", "une fois") or a fused "toutefois".
- @1337 "86 71 64(qui)": the "X qui" frame wants a nominal head.
- No single French word parses both: "chaque"/"une" die at "86 [X] qui"; any nominal head dies at "65 [X] fois" (71 is preceded by noun-class 65, not a determiner).
- The remaining five windows have no banked contact at all (60, 63, 48, 86, 83, 51, 10, 12, 50, 48 all open), so no third leg is even testable.
- 71='tout' ruled out: 79='tout' is granted (A5).

## C2: FIRES — 71 fenced as residual
The data is too thin to name 71 at battery grade. Fenced with cause: the two discriminating windows point at different classes (quantifier vs nominal head); if a single value covers both, it is a §7 split candidate — red-team territory, not declared here.

## Standing-state check
No standing verdict on 71 exists; nothing contradicted or downgraded. §7 honored.

## Verdict: NULL (fence executed)

## Follow-ups proposed (for supervisor queuing)
1. `val-71-quant-nominal` (P3) — test whether "71 fois" @925 and "71 qui" @1337 force different classes; decide if 71 is a §7 split candidate or a single nominal with "65 71" forming a unit.
2. `pre-71-60-class` (P3) — name 60's class at @234/@1565 ("60 71" x2); a nominal 60 reframes 71 as its complement/head-adjacent slot.
3. `suc-71-48-1614` (P4) — test "83 71 48" @1614 against the 12-48 "ne" letter reading once 83's value resolves.
