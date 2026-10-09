# Battery report — wordinternal-41-census

Target: `wordinternal-41-census`
Date: 2026-10-09
Worker: 4ef555e7-c2c6-40ea-819a-e0fa111dfe40

## Claim (from queue)

census 41 19 windows for sub-lexical composition evidence; letter-tier leads are @59 ("41 08 34") and @237 ("70 98 41 17 11")

## Bar (verbatim, from queue)

state composition evidence with counts; fence iff none

Relayed brief phrasing ("Cover all 19 windows; feed the docket item") is consistent
with the queue bar and is recorded here for traceability.

## Bar as numbered clauses

1. State composition evidence with counts.
2. Fence 41's letter-tier arm iff there is no composition evidence.

## Method

Parsed the repaired 1,847-pair / 96-type stream exactly as
`code/side-keyhunt/repair_parse.py` does: rows from `data/upstream-ct_R5005.txt`,
offsets from `code/side-keyhunt/repaired_offsets.json`. All 19 occurrences of
group 41 were enumerated with @-offsets, row ids, and ±3 group context.
Neighbors were annotated with standing values (protocol §7; (p) = provisional).
No class claim about 41 is made: this is a census feeding the split-41-redteam
docket item.

## Findings

41 occurs 19 times across 17 rows (rows a1_01 and a7_11 each hold two).
@589 and @590 form one adjacent "41 41" doublet.

### Window table (@-offset | row | left3 | [41] | right3; values annotated)

| n | @ | row | left3 | right3 |
|---|---|-----|-------|--------|
| 1 | 5 | a1_00 | 97 51 47=ce | 06 77=le(p) 78 |
| 2 | 39 | a1_01 | 91 39 64=qui | 01 24 88 |
| 3 | 59 | a1_01 | 35 53 12 | 08 34=i 29=er |
| 4 | 91 | a1_02 | 66 98 19 | 98 81 97 |
| 5 | 237 | a2_01 | 51 70=pre 98 | 17=fois 11=la 26 |
| 6 | 444 | a2_09 | 80 50 78 | 10 62 61 |
| 7 | 489 | a2_11 | 64=qui 76 42 | 20 67 78 |
| 8 | 589 | a3_02 | 14 00=pour 97 | 41 09 00=pour |
| 9 | 590 | a4_00 | 00=pour 97 41 | 09 00=pour 92 |
| 10 | 808 | a5_05 | 69 24 24 | 12 48 24 |
| 11 | 964 | a6_00 | 00=pour 86 56 | 19 24 06 |
| 12 | 1016 | a6_02 | 47=ce 03 24 | 15 66 91 |
| 13 | 1048 | a6_04 | 67 76 85 | 88 29=er 40=e |
| 14 | 1111 | a6_06 | 00=pour 66 73 | 65 38 30 |
| 15 | 1472 | a7_10 | 38 26 12 | 53 60 06 |
| 16 | 1499 | a7_11 | 59=est(p) 24 89 | 74 84=on 33 |
| 17 | 1508 | a7_11 | 00=pour 86 56 | 12 61 59=est(p) |
| 18 | 1535 | a8_00 | 00=pour 66 73 | 62 06 21 |
| 19 | 1759 | a8_08 | 58 17=fois 78 | 15 93 06 |

### Composition counts

- Immediate left-neighbor distribution (19): 47×1, 64×1, 12×2, 19×1, 98×1,
  78×2, 42×1, 97×1, 41×1 (self, @589), 24×2, 56×2, 85×1, 73×2, 89×1.
- Immediate right-neighbor distribution (19): 06×1, 01×1, 08×1, 98×1, 17×1,
  10×1, 20×1, 41×1 (self, @590), 09×1, 12×2, 19×1, 15×2, 88×1, 65×1, 53×1,
  74×1, 62×1.
- No immediate neighbor is a GT letter cell (82=m, 34=i, 29=er, 40=e, 11=la,
  46=que, 70=pre, 64=qui, 96=par, 17=fois) in any of the 19 windows.
  Closest letter-cell adjacencies: 34=i at distance 2 (@59: "41 08 34"),
  29=er at distance 2 (@1048: "41 88 29"), 70=pre at distance 2
  (@237: "70 98 41"), 17=fois at distance 1 right (@237: "41 17"),
  11=la at distance 2 right (@237: "41 17 11").
- "00=pour" sits within 3 slots left of 41 in 6 windows (@589, @590, @964,
  @1111, @1508, @1535).
- 41 is flanked by granted/provisional word-sized units in 7 windows:
  @5 ("47=ce" left), @39 ("64=qui" left), @237 ("17=fois 11=la" right),
  @489 ("64=qui" left), @1016 ("47=ce" left), @1499 ("59=est(p)" left,
  "84=on" right), @1759 ("17=fois" left).
- One self-adjacency: "41 41" spanning @589–590, inside the run
  "00=pour 97 41 41 09 00=pour 92".

### Per-clause pass/fail

1. State composition evidence with counts — PASS. Evidence above, 19/19 windows
   covered.
2. Fence iff none — FAIL (fence not warranted). Composition evidence exists:
   letter-cell non-adjacency in all 19 windows, word-unit framing in 7,
   the "pour"-proximal cluster (6), and the self-doublet.

## Verdict

**NULL** — census-only per brief. No class decision about 41 is made; the
evidence is passed to the split-41-redteam docket item.

## Follow-ups (per §4)

1. `wordbound-41-pour-cluster` — test whether the 6 "00=pour"-proximal windows
   (@589, @590, @964, @1111, @1508, @1535) admit a uniform word boundary at
   "00 | ... 41"; pass iff a single boundary rule parses ≥5/6, else fence the
   cluster as coincidental.
2. `letter-41-dist2-tri` — extend the distance-2 letter-cell leads
   (@59 "41 08 34", @1048 "41 88 29", @237 "70 98 41") into word-internal
   readings; pass iff any window yields a kill-grade French word containing
   the granted letters, else keep 41 outside the letter tier.
3. `doublet-41-589` — resolve the "41 41" adjacency at @589–590 (doubled word,
   geminate boundary, or syllable doubling) using the "00=pour 97 ... 09
   00=pour" frame; feeds split-41-redteam.

## Scope

Repaired stream only (1,847 pairs, 96 types). Standing values per protocol §7.
No red-team docket item was decided by this census; all prior 41 battery
reports (letter-census, doubling-audit, seg-41-08-leftedge, etc.) were
treated as context, not inputs.

## Bookkeeping

- Lock created: `locks/wordinternal-41-census.lock` (agent id + 2026-10-09T17:06:36Z).
- Report: `code/crowd17/report_inbox/battery-wordinternal-41-census.md`.
- Queue: target `wordinternal-41-census` set to status `verdict` (NULL) —
  own-entry-only temp-file+rename write, pre-write assert queued/verdictless.
- Lock deleted on completion.
