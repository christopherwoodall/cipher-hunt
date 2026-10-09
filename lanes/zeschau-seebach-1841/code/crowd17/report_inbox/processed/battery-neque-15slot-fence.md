# Battery neque-15slot-fence — report

## Bar (verbatim, pre-registered)

> "slot-empty confirmed at each, else re-open."

## Bar restated (numbered, before testing)

- C1: at each of the 15 non-W3 nearest-46 '94...46' windows, the cell immediately
  after 94 (the 'ne...que' verb slot) is empty of a finite verb under standing values.
- C2: W03 (94@161, slot 24 under R24 finite/modal grant) is recorded as the exception;
  it is not fenced by this target.
- C3: any window whose slot is filled under standing values re-opens (not fenced).

Adverses: none listed.

## Method

Stream re-derived in-session: 1,847 pairs / 96 distinct cells from
`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`,
parsed via `repair_parse.py` (`load_rows` + `parse`). Asserts held
(1,847 pairs, 96 distinct cell values). `canonical.py` never used.

Each window: the distinct-46 bracket (nearest following 46 from each 94;
16 brackets stream-wide), re-verified byte-exact — 94 position, slot cell
(94+1), nearest-46 offset, and row spans all confirmed against the repaired
stream. Finiteness judged under standing law (§7): only 24 carries a general
finite grant (R24, red-team declared) except at the five declared 24-85 windows
(@732/@955/@1438/@1693/@1754) where 24='en'; all other verb cells (92/93
verb-class, 85 verb-stem, 86 INF-class, 80/89 A8 frames, 88 gov-class) carry no
general finite grant at battery grade.

## Window-level evidence (all 0-based, byte-exact)

| # | 94@ | 46@ | rows | slot | standing | finite under standing? |
|---|-----|-----|------|------|----------|------------------------|
| W01 | 65 | 95 | a1_01/a1_02 | 92 | verb-class | NO |
| W02 | 101 | 107 | a1_02/a1_03 | 93 | verb-class | NO |
| W04 | 250 | 309 | a2_02/a2_04 | 65 | noun-class | NO |
| W05 | 349 | 419 | a2_05/a2_08 | 74 | unvalued | NO |
| W06 | 509 | 546 | a3_00/a3_01 | 64 | qui (promoted) | NO |
| W07 | 578 | 636 | a3_02/a4_01 | 82 | m (ground truth) | NO |
| W08 | 688 | 694 | a5_00/a5_01 | 29 | er (ground truth, letter) | NO |
| W09 | 785 | 792 | a5_04/a5_04 | 74 | unvalued | NO |
| W10 | 841 | 865 | a5_06/a5_07 | 26 | noun (lead) | NO |
| W11 | 1182 | 1191 | a6_10/a7_00 | 82 | m (ground truth) | NO |
| W12 | 1363 | 1408 | a7_06/a7_07 | 79 | tout (promoted) | NO |
| W13 | 1576 | 1625 | a8_01/a8_03 | 76 | noun (promoted) | NO |
| W14 | 1664 | 1681 | a8_04/a8_05 | 84 | on (promoted) | NO |
| W15 | 1687 | 1692 | a8_05/a5_08→a8_05 | 79 | tout (promoted) | NO |
| W16 | 1742 | 1744 | a8_07/a8_07 | 82 | m (ground truth) | NO |

W03 exception (recorded, not fenced): 94@161 → 24@162 → 46@217 (a1_05/a2_01);
24@162 is finite/modal under R24 (follower 87 ≠ 85; 162 not among the five
24-85 windows). The 'ne...que' restrictive mold remains licensed there in
principle — that window's fate belongs to `neque-W3-parse` and
`val-24-162-modal`, not this fence.

## Per-clause results

- C1 PASS — 15/15 slots confirmed empty of a finite verb under standing values.
  No slot cell carries any finite grant at battery grade; the W03 slot (24)
  is the only one that does.
- C2 PASS — W03 recorded as the sole exception; all other windows fenced.
- C3 did not fire — no filled slot found, no re-open.

## Verdict: PROMOTE

The 15 '94...46' windows are individually fenced as 'ne...que'-incapable on
the empty-verb-slot ground, at battery grade. W03 (@161–217) stands as the
lone 'ne...que'-shaped window.

Scope: this fences the *frame shape* 'ne [slot] ... que' at these windows —
it does not kill any cell's value or class, and it does not decide the wider
'ne...que'-bracket family (which the W03 parse will settle one way or the
other). Re-open condition: a red-team finiteness grant to any slot cell
(most relevantly 74, the only unvalued slot cell) would re-open that window.

No standing/red-team verdict contradicted or downgraded (R24/R19-191, R19-167
94 single value, §7 sole polyvalence, all banked standing values adopted as
premises). §7 intact; no polyvalence declared. Canonical-stream caveat stands.

No follow-ups required per §4 (promote); §4's follow-up mandate applies to
nulls only.

## Bookkeeping

- Target: `neque-15slot-fence`, status queued → verdict at start of run.
- Lock: created 2026-10-09T13:41:51Z, deleted on completion.
- R5005, sealed gate instances, red-team adjudication queue untouched.
