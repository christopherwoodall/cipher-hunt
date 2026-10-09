# Battery report: unit-13-55-61-contact

Target: `unit-13-55-61-contact`. Claim: 13-55-61 is a real unit riding the
boundary, not a coincidence.
Date: 2026-10-08. Worker: e6105541-d3c7-4d6d-8b04-1d3a8d6a1b78 (battery worker).
Lock `locks/unit-13-55-61-contact.lock` created 2026-10-09T02:06:11Z; deleted
on completion.

## Bar (verbatim, pre-registered)

"census all 13, 55, 61 contacts on the repaired stream; the unit is real iff
55-61 binds to 13 more tightly than chance (55-61 after non-13 tokens) and the
5-gram tail parses with the unit named"

## Bar restated (numbered pass/fail clauses; frozen before testing)

1. Census of all 13, 55, 61 contacts re-derived on the repaired 1,847-pair
   stream (predecessors, successors, @-offsets).
2. 55-61 binds to 13 more tightly than chance: among 55-61 bigrams, the share
   with predecessor 13 exceeds 13's share of 55's predecessors generally
   (55-61 after non-13 tokens rare).
3. The 5-gram tail (78-45-13-55-61 @573/@1164) parses with the unit named as
   one French word.

Offset convention: @n = 0-based pair index in the repaired stream.

## Method

Repaired 1,847-pair stream only: `code/side-keyhunt/repaired_offsets.json` +
`data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`
(stride-2 pairing per row offset). Verified 1,847 pairs / 96 types before
testing. `canonical.py` never used. R5005 untouched (read-only parse). No
sealed gates, no red-team contact. Every number traces to the stream.

Per the adverse, dict-frame-78-45-13-55-61's two clean windows are built on,
not re-run: W1's "61 94 82 06" = "ne mentent" frame (its clause 2, PASS
conditional on 94='ne' STRONG LEAD) and W2's "21 67" left-context fence (its
clause 3, PASS fenced) are cited as established, not re-derived here.

## Window-level evidence (re-derived)

Contact census on the repaired stream:

- 13, n=12 @ [68, 139, 456, 481, 567, 575, 822, 1166, 1360, 1381, 1554, 1684]
  pre {69x2, 65x3, 00, 97, 45x2, 95, 35, 99}
  suc {24x3, 66x2, 52, 76, 55x2, 92, 93x2}
  13->55 occurs ONLY @575/@1166 (the two 5-gram windows), nowhere else.
- 55, n=12 @ [25, 523, 550, 576, 906, 1085, 1094, 1167, 1205, 1285, 1611, 1671]
  pre {33, 06, 46, 13x2, 18, 02, 07, 43, 98, 08, 78} (11 distinct)
  suc {81x6, 61x3, 83x2, 68}
- 61, n=18 @ [223, 279, 281, 367, 447, 577, 645, 926, 1168, 1206, 1219, 1256,
  1281, 1429, 1455, 1510, 1556, 1810]
  pre {89, 37, 20, 49, 62x2, 55x3, 87, 17, 92, 01, 53, 91, 12, 93, 04}
  suc {96x2, 20, 42, 70, 59x2, 94x2, 88, 21x2, 24, 31, 56, 12, 40, 15}

Key n-grams:
- 55-61 bigram x3 @ [576, 1167, 1205]; predecessors [13, 13, 43];
  61's successors in these windows [94, 94, 21].
- 13-55-61 trigram x2 @ [575, 1166] — exactly the two 5-gram windows.
- 78-45-13-55-61 5-gram x2 @ [573, 1164] (rows a3_02, a6_09).
- 61->94 x2 = exactly the two 5-gram tails (@577->578, @1168->1169).
- Third 55-61 @1205 sits in "29 45 58 47 43 55 61 21 65" (row a7_00,
  pair 14/28 — mid-row, like the other two: a3_02 pair 17/32, a6_09
  pair 13/20; none is row-initial).

Binding test (Fisher exact, one-sided), 2x2 table over 55's 12 tokens:
rows = 55->61 yes/no, cols = predecessor 13 yes/no:
a=2 (prev13 & 55->61), b=0 (prev13 & 55-/->61), c=1 (prev!13 & 55->61),
d=9. p(X>=2) = 0.0455. 13 is 2/12 of 55's predecessors but 2/3 of 55-61's.

## Per-clause pass/fail

1. **PASS.** Full contact census re-derived above; all counts byte-traced.
2. **PASS (fragile).** 55-61 binds to 13 more tightly than chance: Fisher
   one-sided p=0.0455. Supporting asymmetries: 13->55 occurs nowhere outside
   the two 5-gram windows (13's 55-successor is exclusive to them), and
   13-55-61 is the only 13-55 context in the stream. Caveat stated: n=3
   bigram events; one non-13 instance (@1205, predecessor 43) exists, so the
   "unit" reading is distributional, not absolute.
3. **FAIL.** The 5-gram tail does not parse with the unit named as one French
   word. name-13-55-61 (verdict null) ran the full cross-window triangulation
   and rejected the trigram as unnameable with evidential support; that
   finding stands uncontradicted. Independently of naming: W2's right context
   "94 87" ("ne ce") is ungrammatical under 94='ne' STRONG LEAD + 87='ce'
   granted for ANY unit name (ne-ce-1169 returned null and fenced this as a
   94-segmentation problem, not a unit problem), and W1's "ne mentent"
   requires a 3pl subject the singular "ce verdict [X]" frame cannot supply.
   The tail parse fails on 94-grounds outside the unit's scope.

## Adverses answered

- "dict-frame-78-45-13-55-61 returned null on the unit-naming bar": answered
  — consistent with clause 3's FAIL here. Its two clean windows were built
  on, not re-run (cited above with clause references); this battery added
  only the distributional binding test, which that battery did not run.

## Verdict: null

Headline: the trigram is distributionally bound (clause 2 passes at
p≈0.046, 13->55 exclusive to the two 5-gram windows) but not French-nameable
(clause 3 fails; name-13-55-61's unnameable finding stands, and the tail
parse breaks on the 94-87 hapax regardless of the unit's name). No window
forces the claim false — the binding is real, so this is not kill-grade; the
residuals are 94-problems outside the unit's scope. No standing verdict
contradicted or downgraded (R17-001/R17-006/R17-007 scoping respected). No
red-team escalation: nothing here contradicts a red-team verdict.

## Follow-up targets (null regenerates work; all ids verified absent from the queue 2026-10-09)

1. **13-55-mutual-info** (priority 2). Claim: 13-55 is a mutual collocation,
   not just 13-driven. Bars: (a) full 2x2 contingency for 13-55 on the
   repaired stream; (b) G² or Dice for 13-55 vs the next-strongest
   13-successor pair (13-24 x3); (c) state whether the binding is mutual or
   asymmetric (13->55 exclusive vs 55's 11 distinct predecessors). Evidence:
   this report. Adverses: small samples (13 n=12, 55 n=12).
2. **61-94-rightedge** (priority 2). Claim: 94 binds to the [55-61] right
   edge specifically, not to 61 generally. Bars: (a) census 61's 18
   successors — 61->94 x2 = exactly the two 5-gram tails; (b) test whether
   94's rate after 55-61 (2/3) differs from 94's rate after 61 elsewhere
   (0/15) with a stated test; (c) coordinate with ne-ce-1169's null
   (94-segmentation problem) — do not re-litigate it. Evidence: this
   report. Adverses: 94='ne' STRONG LEAD caveats (R17-001).
3. **boundary-ride-position** (priority 3). Claim: the "riding the boundary"
   half of the claim is testable positionally. Bars: (a) row/clause position
   of 55-61 @576/@1167/@1205 (rows a3_02/a6_09/a7_00, mid-row pairs
   17/32, 13/20, 14/28); (b) compare against the positional distribution of
   55 and 61 generally — boundary-riding iff the trigram sits closer to
   row/clause edges than chance; (c) state the boundary definition used
   (row edge vs clause edge) before testing. Evidence: this report.
   Adverses: clause boundaries mostly open; row edges are a weak proxy.

## Reproducibility

All counts re-derived in-session from the repaired stream (1,847 pairs /
96 types asserted before testing). Analysis script: /tmp/unit135561.py
(session-local). No writes outside this report, the queue edit, and the
lockfile (deleted).
