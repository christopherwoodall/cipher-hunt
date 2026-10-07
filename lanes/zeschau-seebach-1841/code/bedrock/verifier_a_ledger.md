# VERIFIER A — Bedrock re-derivation ledger (2026-10-07)

Independent re-derivation of the Seebach lane's standing facts from primary sources only.
All parsing logic written fresh in `code/bedrock/verifier_a.py`; no lane code imported or copied.
Claimed values were extracted from `NOTES.md`, `STATE.md`, `code/crowd4/REINDEX.md`,
`code/side-keyhunt/repair_parse.py` (asserts only), and results JSONs (claimed numbers only).

**Score: 34 PASS / 6 FAIL / 7 N/A (47 facts). Every FAIL is diagnosed, none are ambiguous.**

## 1. Transcription — PASS

| fact | claimed | computed |
|---|---|---|
| digit rows | 70 | 70 |
| total digits | 3,764 | 3,764 |

Row order cross-checked across all three sources (`upstream-offsets.json` key order =
`upstream-ct_R5005.digits.txt` file order = `upstream-ct_R5005.txt` tag order); every row is
all-digits. (The DECODE web page's "3,969 digits" is not reproduced: the transcription is 3,764.)

## 2. Canonical parse — PASS

Pairing convention re-derived independently: each row paired on its own; offset=1 discards the
row's first digit; leftover trailing digit dropped on odd remainder; rows concatenated in tag order.

| fact | claimed | computed |
|---|---|---|
| repaired parse pairs | 1,847 | 1,847 |
| distinct groups | 96 | 96 (unobserved: 05, 25, 72, 75) |
| original-offset parse pairs | 1,846 | 1,846 |
| digit accounting (repaired) | 3,694 paired + 70 dropped | 3,694 paired + 70 dropped — **31 dropped by offset** (31 rows with offset bit 1) + **39 dropped by odd length** |
| repair locality | only row a5_03 changes; rows before/after byte-identical | a5_03 starts at pair 748 in both parses; a5_03 = 26 pairs repaired vs 25 original; pairs before 748 identical; pairs after identical in value (delta is even, downstream phases hold) |

Cross-check: my repaired pair stream is byte-identical to the lane's post-repair artifact —
all 35 `positions_62` in `code/crowd5/frenchman62_leg3_results.json` (npairs=1847) match exactly.

## 3. The repair's validity — PASS (with one indexing correction and one marked ambiguity)

| fact | claimed | computed |
|---|---|---|
| raw 12-digit crib `117082342940` occurrences | [1532, 2108] | [1532, 2108] (0-based, concatenated stream) |
| `11 70 82 34 29 40` in repaired stream | pairs 754 and 1034, rows a5_03 / a6_03 | pairs [754, 1034], rows {a5_03, a6_03} |
| `11 70 82 34 29 40` in original stream | "only at 1034" | **exactly 1 occurrence at old-index 1033** (= new-index 1034; the task text's "1034" is the new-index value) |
| a5_03 crib read off-phase under original offsets | `71 17 08 23 42 94 02` | `71 17 08 23 42 94 02` (row pairs 5–11, global old 753–759) |
| raw 1532 sits in row a5_03 at pair-start phase under repaired offsets | (REINDEX premise) | row a5_03, within-row index 12 (even) → pair start ✓; raw 2108 in row a6_03, within-row index 28 |

**Ambiguity, marked honestly:**
- **VALID given the gloss-line premise** — the crib occurs twice in the raw stream; the repaired
  parse puts `11 70 82 34 29 40` on rows a5_03 and a6_03 exactly; the original offsets put the
  a5_03 occurrence off-phase. The repair is internally consistent.
- **UNVERIFIABLE premise** — whether the erased pencil gloss ("la pre m i er e") really sits over
  row a5_03 cannot be checked from available sources (no manuscript images were re-examined by the
  lane; REINDEX.md records the same caveat). If the gloss line-tag is wrong, the old parse revives.

## 4. Group frequencies — 6 FAIL, all diagnosed as STALE PRE-REPAIR CLAIMS

Recomputed all 96 group counts from the repaired stream. The repair changes only row a5_03
(+1 pair, re-paired); the per-group delta (new−old) inside a5_03 is:

+1: 00, 64, 97, 67, 11, 82, 34, 20, 62, 94, 59, 39, 66, 80, 10, 22, 07 ·
−1: 02, 74, 71, 17, 08, 23, 42, 45, 93, 86, 69, 01 ·
−2: 29, 06 · 0: everything else (40, 70, 88, 98 unchanged)

| group | claimed | repaired (computed) | original-parse (computed) | verdict |
|---|---|---|---|---|
| 62 | 35 | 35 | 34 | PASS |
| 24 | 52 | 52 | 52 | PASS |
| 52 | 27 | 27 | 27 | PASS |
| 06 | 44 | 44 | 46 | PASS |
| 78 | 31 | 31 | 31 | PASS |
| 87 | 32 | 32 | 32 | PASS |
| **64** | **46** | **47** | 46 | **FAIL — stale** (claim = pre-repair count) |
| 96 | 21 | 21 | 21 | PASS |
| **00** | **54** | **55** | 54 | **FAIL — stale** ("00 leads at 54", F17) |
| **11** | **44** | **45** | 44 | **FAIL — stale** (Phase-A block) |
| 70 | 15 | 15 | 15 | PASS |
| **82** | **38** | **39** | 38 | **FAIL — stale** (Phase-A block) |
| **34** | **10** | **11** | 10 | **FAIL — stale** (Phase-A block) |
| **29** | **47** | **45** | 47 | **FAIL — stale** (Phase-A block) |
| 40 | 21 | 21 | 21 | PASS |
| 46 | 29 | 29 | 29 | PASS |

Every failing claimed value equals the **original 1846-pair parse count exactly** — the lane updated
some counts after the repair (n62 34→35, n06 46→44) but left these six at their pre-repair values.
Downstream notes that cite the stale numbers and need correction: NOTES Phase-A block
("11=la ×44, 82=m ×38, 34=i ×10, 29=er ×47" + their freq ranks), F17 ("00 leads at 54"),
the N-claim citing n64=46 (closer battery L1: P(64)=46/1846; also P(29|64)=3/46 is now 3/47).

Rank sanity on the repaired parse (competition ranking): 00 still rank 1 (55), 24 rank 2 (52),
64 rank 3 (47), 11/29 tied rank 4 (45), 06/77 tied rank 6 (44). So "24 is rank 2/96" still holds;
the Phase-A rank claims (11 rank 6, 70 rank 56, 82 rank 8, 34 rank 70, 29 rank 2, 40 rank 36,
46 rank 19) were computed pre-repair and should be rechecked.

No explicit unigram claims found in NOTES.md for n77/n47/n67/n43/n84/n59 (N/A — computed values
reported for the record): **n77=44, n47=28, n67=38, n43=16, n84=25, n59=27**.
Consistency note: pre-repair B_scan gave 77=44, 59=26; repaired deltas (77: 0, 59: +1) predict
exactly 44 and 27 ✓ — further confirmation the parse matches the lane's.

## 5. Windows / bigrams / trigrams — ALL PASS (one indexing ambiguity resolved)

All positions 0-based pair indices in the repaired stream.

| pattern | claimed | computed | verdict |
|---|---|---|---|
| 62→94 windows | 9 @ [100, 508, 761, 840, 1329, 1362, 1686, 1704, 1772] | identical | PASS |
| 24→87→64 | 3 @ [179, 1766, 1774] (index of the 24) | identical | PASS |
| 64 96 43 87 01 | 2 @ [341, 1025] | identical | PASS (F18's @341/@1024 was 1846-indexing; 1024 ≥ 773 → +1) |
| 06→29 | ×4 | 4 @ [1096, 1388, 1709, 1815] | PASS |
| 00→86 | ×12 | 12 @ [552, 660, 727, 866, 888, 961, 1001, 1127, 1374, 1505, 1791, 1824] | PASS |
| 00→06 | ×0 | 0 | PASS |
| 77→86 | ×5 @ [430, 798, 877, 950, 1133] | identical | PASS — the N25 text's "new" means new-indexing; original-parse positions are [430, 797, 876, 949, 1132], confirming the +1 shift |
| 77→78 | ×7 | 7 @ [7, 213, 647, 1077, 1180, 1351, 1542] | PASS (1180/1351 = REINDEX-remapped @1179/@1350 ✓) |
| 94→82 | 4 @ [578, 1182, 1353, 1742] | identical | PASS (F24's @[578,1181,1352,1741] was 1846-indexing; +1 for ≥773) |
| 87 64 77 84 | @ [1800] | [1800] | PASS |
| 11 67 ("la veut") | @ [1044], unique | [1044], unique | PASS |

## Bottom line for the parent

- **The parse itself is bedrock-solid**: transcription, 1,847 pairs, 96 groups, digit accounting,
  repair locality, crib positions, and every window/bigram/trigram claim re-derive exactly.
- **The repair is valid given its premise** (crib occurs twice raw; repaired parse lands the gloss
  on a5_03/a6_03); the premise itself (gloss-over-a5_03) is unverifiable without manuscript images.
- **Six frequency claims are stale pre-repair values** and must be corrected wherever cited:
  n64 46→**47**, n00 54→**55**, n11 44→**45**, n82 38→**39**, n34 10→**11**, n29 47→**45**.
  Anything downstream that divides by these counts (rates, P(x|64), rank claims, the Phase-A crib
  block) inherits the error.
- One task-text correction: the original-offset stream has the crib once at **old-index 1033**
  (the task text's "1034" is the new-index value after the +1 shift).
- No explicit NOTES.md claims exist for n77/n47/n67/n43/n84/n59; computed: 44/28/38/16/25/27.

## Artifacts

- `code/bedrock/verifier_a.py` — derivation script (fresh logic, asserts explicit, prints PASS/FAIL)
- `code/bedrock/verifier_a_results.json` — 47 facts, machine-readable
- `code/bedrock/verifier_a_ledger.md` — this file

## Full repaired-parse frequency table (96 groups, rank order)

00 55, 24 52, 64 47, 11 45, 29 45, 06 44, 77 44, 98 40, 82 39, 48 38, 67 38,
94 37, 62 35, 74 34, 86 32, 87 32, 78 31, 21 30, 46 29, 01 28, 16 28, 37 28,
47 28, 52 27, 59 27, 33 25, 65 25, 84 25, 12 23, 56 23, 88 23, 45 22, 92 22,
40 21, 76 21, 91 21, 96 21, 03 20, 42 20, 30 19, 41 19, 66 19, 08 18, 60 18,
61 18, 79 18, 02 17, 26 17, 80 17, 43 16, 14 15, 17 15, 20 15, 44 15, 70 15,
83 15, 85 15, 81 14, 89 14, 93 14, 32 13, 39 13, 09 12, 13 12, 49 12, 55 12,
63 12, 69 12, 34 11, 50 11, 53 11, 15 10, 35 10, 97 10, 19 9, 36 9, 07 8,
23 8, 31 8, 68 8, 10 7, 18 7, 38 7, 58 7, 71 7, 28 6, 51 6, 73 6, 04 3, 22 3,
54 3, 95 2, 27 1, 57 1, 90 1, 99 1
(unobserved: 05, 25, 72, 75)
