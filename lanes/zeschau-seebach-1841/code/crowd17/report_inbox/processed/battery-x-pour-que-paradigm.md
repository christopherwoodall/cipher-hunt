# Battery verdict: x-pour-que-paradigm

## Bar (verbatim from battery-queue.json, pre-registered)
"Census 'X 00 46' trigrams stream-wide to build the corpus-internal paradigm of values preceding 'pour que'; discriminates donc/bien/aussi/encore/la by distribution."

**Restated as numbered pass/fail clauses:**
- **C1:** The stream-wide 'X 00 46' census is executed on the repaired stream, with all windows byte-traced.
- **C2:** The census yields a corpus-internal paradigm of values preceding 'pour que' (a pattern — a dominant class, a closed set, or anchored X's whose known values constrain what X can be).
- **C3:** That paradigm discriminates among 28's candidate values {donc, bien, aussi, encore, la} by distribution.

Verdict rule: **promote** iff C1–C3 pass. **kill** iff a distributional test rejects the claim at the lane's standard (no discriminating pattern). **null** otherwise, with 1–3 follow-ups.

## Method
- Read BATTERY-PROTOCOL.md first; created `code/crowd17/next-token/locks/x-pour-que-paradigm.lock` on start (agent id + 2026-10-09T10:22:28Z); no stale lock present.
- Re-derived the repaired 1,847-pair / 96-type stream in-session from `data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json` (upstream byte-exact tokenization). Asserted: 1,847 pairs, 96 types.
- `canonical.py` never used. R5005, sealed gates, red-team adjudication queue untouched.
- Standing values held fixed per §7: 00='pour' (A9, leg-1 class-level), 46='que' (pencil ground truth), 45='ce' (A11 hold).

## Window-level evidence

### C1 — 'X 00 46' trigram census (PASS)
Exactly **4** 'X 00 46' windows stream-wide, each X distinct and each n=1:

| @ (0b) | row | trigram | left context | right context |
|---|---|---|---|---|
| 105 | a1_03 | **28 00 46** | 100:62 101:94 102:93 103:59 104:45 | 108:11 109:21 110:67 111:93 112:29 |
| 544 | a3_01 | **06 00 46** | 539:12 540:44 541:29 542:48 543:42 | 547:24 548:47 549:46 550:55 551:81 |
| 1544 | a8_00 | **43 00 46** | 1539:62 1540:93 1541:88 1542:77 1543:78 | 1547:70 1548:12 1549:94 1550:92 1551:45 |
| 1679 | a8_05 | **44 00 46** | 1674:60 1675:03 1676:39 1677:74 1678:77 | 1682:79 1683:65 1684:13 1685:93 1686:62 |

All four are genuine 'X pour que' frames under standing values. 00->46 occurs only 4x stream-wide (n(00)=55, n(46)=29), so the census is complete — no 'X 00 46' window is missing.

### C2 — paradigm test (FAIL)
- The four X's are {28, 06, 43, 44}: **all four value-open**, four distinct groups, each singleton. No X has a named value or a landed class; no two windows share an X; no dominant class; no closed set with a licensing rule.
- Broader check ('X 00' bigrams, 00='pour'): 55 windows, **25 distinct X** — the distribution is flat and heterogeneous: 11 x4, 06 x4, 16 x4, 63 x4, 81 x3, 96 x3, 28 x3, 43 x3, 26 x3, 98 x3, 44 x3, then 09/19/02/33 x2 each and 11 singletons. No class pattern emerges among the four trigram X's relative to this background either.
- A "corpus-internal paradigm" requires a pattern that constrains what X can be. Four singleton, all-open X's provide zero distributional constraint. **C2 FAIL.**

### C3 — discrimination among {donc, bien, aussi, encore, la} (MOOT/FAIL)
C3 is moot because C2 failed: with no paradigm, no candidate can be separated from any other by distribution. Observed: 28's only 'pour que' window is @105 (n(28)=6 total: 105, 286, 698, 747, 1573, 1751; only @105 abuts 00-46). The other three X's (06, 43, 44) are value-open and contribute nothing. The distribution among the five candidates is 1 : 0 : 0 : 0 : 0 — a single observation of one unknown, which discriminates nothing.

## Adverses
- "28 is unknown — no battery has named 28 (the three '28=' grep hits are offset artifacts, not value claims)": **answered.** No value was named for 28 here; the verdict concerns the census method, not 28's value. Nothing in this report names or fences a 28 value.

## Verdict: KILL

The claim's operative part is discrimination by distribution. The stream-wide census is complete (4 windows, all genuine 'X pour que' frames) and rejects the claim at the lane's distributional standard: four singleton, all-value-open X's, against a flat 25-class background for bare 'X 00', yield no paradigm and separate none of {donc, bien, aussi, encore, la}. The 'X 00 46' census route to 28's value is closed at battery grade. Scope: only the methodological claim dies — no 28 value is named, killed, or fenced; the four windows remain licensed 'pour que' frames for any future value work; no standing/red-team verdict contradicted; §7 intact.

## Follow-ups (kill per §4 does not regenerate work; supervisor observations only)
- 28's value remains open and unaddressed; its best lead is distributional from its other five windows (286/698/747/1573/1751), not the 'pour que' frame.

## Bookkeeping
- `battery-queue.json`: `x-pour-que-paradigm` queued → verdict/kill (temp-file + rename, own entry only, pre-write assert confirmed no prior verdict, JSON re-validated).
- Lock created on start, deleted on completion. No standing verdict contradicted or downgraded. R5005, sealed gates, red-team queue untouched.
