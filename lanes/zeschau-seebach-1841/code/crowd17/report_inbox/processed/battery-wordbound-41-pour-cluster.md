# Battery report — wordbound-41-pour-cluster

Target: `wordbound-41-pour-cluster` (priority 3)
Date: 2026-10-09
Worker: badc83af-2e9d-4cbf-ad64-124de83e669f

## Claim (from queue)

test whether the 6 "00=pour"-proximal windows (@589/@590/@964/@1111/@1508/@1535)
admit a uniform word boundary at "00 | ... 41"

## Bar (verbatim, from queue)

pass iff a single boundary rule parses ≥5/6, else fence the cluster as coincidental

## Bar as numbered clauses

1. A single boundary rule parses ≥5 of the 6 pour-proximal windows at "00 | ... 41".
2. If clause 1 fails, the cluster is fenced as coincidental (no promotion).

## Method

Parsed the repaired 1,847-pair / 96-type stream exactly as
`code/side-keyhunt/repair_parse.py` does: rows from `data/upstream-ct_R5005.txt`,
offsets from `code/side-keyhunt/repaired_offsets.json`.
(`canonical.py` was not touched.)
All 55 occurrences of group 00 ("pour", standing A9 leg-1) and all 19 of group 41
were enumerated; gap from each 00 to its next 41 was measured; exact
"00 … 41" 4-grams were counted stream-wide. No claim is made about 41's value:
this tests only word-boundary structure. §7 standings respected; no red-team
docket item touched.

## Window-level evidence (@-offsets, ±7 context, repaired stream)

| n | @41 | row | segment 00 … 41 | middle | 00→41 gap |
|---|-----|-----|-----------------|--------|-----------|
| 1 | 589 | a3_02 | 14@586 00@587 97@588 41@589 41@590 09@591 | 97 | 2 |
| 2 | 590 | a4_00 | 00@587 97@588 41@589 41@590 09@591 00@592 | 97 41 | 3 |
| 3 | 964 | a6_00 | 04@957 20@958 67@959 96@960 00@961 86@962 56@963 41@964 | 86 56 | 3 |
| 4 | 1111 | a6_06 | 47@1104 78@1105 65@1106 63@1107 00@1108 66@1109 73@1110 41@1111 | 66 73 | 3 |
| 5 | 1508 | a7_11 | 84@1501 33@1502 42@1503 33@1504 00@1505 86@1506 56@1507 41@1508 | 86 56 | 3 |
| 6 | 1535 | a8_00 | 46@1528 21@1529 65@1530 63@1531 00@1532 66@1533 73@1534 41@1535 | 66 73 | 3 |

Right context after each closing 41 (word after): 09 / 09 / 19 / 65 / 12 / 62 —
all differ, consistent with a boundary after 41 (not tested as part of the bar).

## Distributional findings (stream-wide, repaired parse)

- 55 occurrences of 00=pour total. Only 6 have a 41 within the next 4 slots
  (gap distribution: d=2:1, d=3:4, d=4:1; every other pour's next 41 is ≥6 slots
  away or absent). The 6 are exactly the census windows — no missed window, no
  extra window.
- Exact 4-gram counts: "00 86 56 41" occurs 2× (@961, @1505); "00 66 73 41"
  occurs 2× (@1108, @1532); "00 97 41 41" occurs 1× (@587). Two distinct
  pour-led, 41-closed phrases each repeat verbatim — phrase-shaped, not noise.
- Windows n1/n2 overlap: the run @587–592 reads "00 97 41 41 09 00 92",
  pour-bracketed on both ends; the 41-41 doublet is read as a word-internal
  geminate, the word closing at 41@590.

## Candidate boundary rule (single, applied identically to all 6)

**R: place a word boundary immediately after 00=pour; the pour-headed word
closes at the nearest following 41 (41 word-final; a 41-41 geminate closes at
its second member).**

Per-window parse under R:

1. @589: word "97 41" — 41-final ✓ (or geminate-part of the word closing at @590 ✓)
2. @590: word "97 41 41" — 41-final (geminate close) ✓
3. @964: word "86 56 41" — 41-final ✓
4. @1111: word "66 73 41" — 41-final ✓
5. @1508: word "86 56 41" — 41-final ✓
6. @1535: word "66 73 41" — 41-final ✓

**6/6 parse.** No window forces the claim false: every pour-headed segment is
41-closed, the two exact phrase repeats hold the frame, and no pour-proximal
41 exists outside the six windows.

## Per-clause pass/fail

1. Single boundary rule parses ≥5/6 — PASS. Rule R parses 6/6.
2. Fence-as-coincidental fallback — not triggered (clause 1 passed).

## Adverses

None stated in the queue entry. Honest fences (not kill-grade):
- 41's own value is unvalued: R establishes boundary structure only, not what
  41 means. Compatible with standing 41 verdicts (battery-41-05-class noun-stem
  at @5; battery-41-808-role standalone-word at @808) — no contradiction, no
  standing verdict overwritten.
- Pour-led word length varies (2–4 groups) and middle groups are unvalued; R
  is a local boundary pattern, not a general pour rule (49 of 55 pours are not
  41-closed).
- Windows n1/n2 share one pour phrase; counted as 2 windows, 1 distinct phrase.
  Even treating them as one, the rule parses 5/5 distinct phrases — the bar is
  met either way.

## Verdict

**PROMOTE** — the 6 "00=pour"-proximal windows admit the uniform word boundary
"00 | … 41" under rule R (6/6 parse, exact phrase repeats "00 86 56 41" ×2 and
"00 66 73 41" ×2). The cluster is not coincidental; it is a repeated
pour-headed, 41-closed word frame. Follow-up: the middle groups (97 / 86 56 /
66 73) are now worth their own batteries, and the post-41 boundaries
(right context 09/09/19/65/12/62) are untested.

## Bookkeeping

- Lock created: `locks/wordbound-41-pour-cluster.lock` (agent id + 2026-10-09T17:20:00Z);
  no stale lock was present for this target.
- Report: `code/crowd17/report_inbox/battery-wordbound-41-pour-cluster.md`.
- Queue: target `wordbound-41-pour-cluster` set to status `verdict` (PROMOTE) —
  own-entry-only temp-file+rename write, pre-write assert queued/verdictless,
  JSON re-validated after write.
- Lock deleted on completion.
