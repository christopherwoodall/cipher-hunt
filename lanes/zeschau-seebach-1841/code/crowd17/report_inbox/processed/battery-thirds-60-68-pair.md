# Battery report — thirds-60-68-pair ({60,68} 2-cell homophone set; 62 excluded)

Worker: 1915a2a4-a9cc-4896-adc2-d34e40b3b5ee. Date: 2026-10-08.
Lock: `code/crowd17/next-token/locks/thirds-60-68-pair.lock` created
2026-10-08T19:26:00Z; no prior lock existed; deleted on completion.
Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` +
`data/upstream-ct_R5005.txt`), parsed per `code/side-keyhunt/repair_parse.py`.
`canonical.py` not used. R5005 not touched. Sealed gates, red-team
adjudication queue untouched. No invented numbers: every count below was
re-derived from the stream in this run.

## Bar (verbatim, from battery-queue.json)

"(a) re-derive the {60,68} permutation test on the repaired stream
(formula-bound tokens excluded) and meet the {33,86} indistinguishability
standard on successors AND predecessors; (b) the two formula slots @227/@1783
parse as 'venir'-tails; (c) 62's exclusion cites the collision-62-84 kill and
the 62->94 x9 vs 60->94 x0 / 68->94 x0 asymmetry — no re-litigation of 62's
value"

Numbered clauses (pre-registered BEFORE testing, not modified after):

1. (a) The {60,68} permutation test is re-derived on the repaired stream with
   formula-bound tokens excluded, and meets the {33,86} indistinguishability
   standard on successors AND predecessors.
2. (b) The two formula slots @227 and @1783 parse as 'venir'-tails.
3. (c) 62's exclusion cites the collision-62-84 kill and the 62->94 x9 vs
   60->94 x0 / 68->94 x0 asymmetry; 62's value is not re-litigated.

## Method

Fresh parse of the repaired stream (1,847 pairs, 96 distinct, verified).
Thirds census re-derived: 60 n=18, 62 n=35, 68 n=8. Formula-bound tokens
excluded per §7 de-duplication: @232 (60), @1065 (62), @1788 (68) — the three
byte-identical "98-83-82-96-21-[third]" windows at @227/@1060/@1783.
Free counts: 60 x17, 62 x34, 68 x7. Permutation test: total-variation distance
summed over cell pairs on the successor (resp. predecessor) empirical
distributions; labels permuted B=20,000 preserving cell counts; p=(ge+1)/(B+1);
fixed seed. Lane yardsticks: 09/92 HOLD — successor p=0.256 (held);
23~26 SPLIT — successor p=0.0029 (split granted). Windows quoted with
±3 context at repaired-stream pair indices.

## Census (re-derived, formula-bound excluded)

- 60 free n=17. Successors: 03 x4 (@690, @1366, @1644, @1674), 08 x2, 67 x2,
  12 x2, 90/09/15/65/06/71/27 x1; 94 x0. Predecessors: 21 x3, 92 x2, 14 x2,
  06 x2, 77/46/29/94/03/64/53/98 x1.
- 68 free n=7. Successors: 21 x2 (@114, @504, both "68-21-67"), 37/00/52/59/06
  x1; 94 x0, 03 x0. Predecessors: all singletons — 89, 39, 79, 55, 65, 52, 47.
- 62 free n=34. Successors: 94 x9, 48 x6, 98 x5, 16 x4, 61/06 x2,
  96/91/21/38/46/93 x1; 03 x0.

## Permutation test (re-derived)

| cells | side | n | stat | p |
|---|---|---|---|---|
| 60, 68 | successor | 17/7 | 0.9412 | 0.0552 |
| 60, 68 | predecessor | 17/7 | 1.0000 | 0.0546 |
| 60, 62 | successor | 17/34 | 0.9412 | <0.0001 |
| 62, 68 | successor | 34/7 | 0.9118 | 0.0020 |
| 60, 62, 68 | successor | 17/34/7 | 2.7941 | <0.0001 |
| 60, 62, 68 | predecessor | 17/34/7 | 2.6471 | 0.0116 |

Matches the finder (parvenir-thirds T3) to the third decimal. 3-way homophony
rejected at kill grade on successors. Every pair involving 62 rejected.

## Window-level evidence (@-offsets, repaired stream)

Formula slots (clause 2):
- @227 (a2_01): `87 46 98 83 82 96 21 60 71 51 70`. 87="ce" (granted),
  46="que" (banked), 96="par" (granted), 82="me" (banked). 21-60 = "ve-nir":
  the slot is a venir-tail. Follower 71 opens a clause-level tail
  ("71 51 70", 70="pre" banked) — not formula-internal.
- @1783 (a8_09): `65 23 98 83 82 96 21 68 47 03 00`. 21-68 = "ve-nir": the slot
  is a venir-tail. Follower 47="ce" (A4 allophone tier) + 03 + 00="pour" (A9)
  is clause-level ("...parvenir ce [03] pour...").
Caveats (not this bar's scope): 83='de' is lead-level (fencing owned by queued
T2/T4 fence-911-de and frame-87-83-cede); 98's French head stays unconfirmed
(standing adverse).

60 free windows (±3), all 17: @119 `67 14 21 60 90 19 58`; @172 `12 48 21 60 09
87 86`; @197 `47 01 21 60 08 67 76`; @322 `06 11 92 60 15 63 71`; @454 `79 17 77
60 65 13 66`; @637 `63 74 46 60 67 77 89`; @690 `65 94 29 60 03 39 74`; @700 `45
28 94 60 12 98 20`; @995 `26 30 03 60 67 11 96`; @1338 `86 71 64 60 08 65 64`;
@1366 `94 79 14 60 03 30 82`; @1474 `12 41 53 60 06 67 33`; @1563 `26 30 06 60
71 50 29`; @1644 `12 33 98 60 03 64 31`; @1674 `55 81 92 60 03 39 74`; @1690 `94
79 14 60 27 46 24`; @1735 `56 30 06 60 12 48 52`.
68 free windows (±3), all 7: @114 `93 29 89 68 21 67 14`; @504 `40 56 39 68 21
67 77`; @884 `08 31 79 68 37 03 02`; @1286 `32 98 55 68 00 11 17`; @1384 `13 24
65 68 52 82 16`; @1442 `85 01 52 68 59 37 64`; @1719 `30 64 47 68 06 11 52`.

Frame-sharing (free text): shared successor types = {06} only (60->06 x1 @1474
`53 60 06 67`; 68->06 x1 @1719 `47 68 06 11`). Shared predecessor types = NONE.
68's only contact with 21 is formula-bound (finder's note confirmed: 21-68 n=1
globally, @1788). 60's "21-60" contact is free x3 (@119/@172/@197) + formula.

62 exclusion asymmetry (clause 3): 62->94 x9 re-derived @100/@508/@761/@840/
@1329/@1362/@1686/@1704/@1772; 60->94 x0 (n=17 free); 68->94 x0 (n=7 free).

## Per-clause pass/fail

1. **(a) PASS — marginal.** Successor p=0.0552, predecessor p=0.0546 (B=20,000,
   n=17/7). Both above the lane's rejection cutoff (yardsticks: 09/92 hold at
   p=0.256; 23~26 split at p=0.0029) — the test fails to reject on both sides,
   meeting the {33,86} indistinguishability standard as written. Margin noted:
   both p-values sit ~0.005 above α=0.05; the predecessor non-rejection is
   low-power (68's 7 predecessors are disjoint singletons — no type overlap
   with 60's — so the test cannot reject regardless of the true state).
2. **(b) PASS.** Both slots parse as venir-tails: @227 `...96 21 60 71...`
   ("par-ve-nir [71]", clause-level tail); @1783 `...96 21 68 47 03 00...`
   ("par-ve-nir ce [03] pour", clause-level tail). 96="par" granted, 82="me"
   banked; the third cells are syllable-shaped ("nir"-shaped) as required.
3. **(c) PASS.** 62's exclusion cites the standing battery KILL
   (collision-62-84, 2026-10-08): unconditioned 62='on' killed, 62='il'
   battery-demonstrated on the nine 62->94 windows; per §7, 67 is the sole
   true polyvalence, so 62 cannot share a syllable value with 60/68. The
   distributional asymmetry (62->94 x9 vs 60->94 x0 / 68->94 x0) is re-derived
   above and consistent with that kill. No 62 window re-read, no rival
   proposed — 62's value not re-litigated.

## Adverses (answered, never ignored)

- "68 n=7 is thin" — FENCED with stated cause. All 7 free tokens used; 68
  occurs 8x in the whole stream (1 formula-bound). The thinness is intrinsic
  to the data, not a misread; it caps the test's power, which is recorded,
  not wished away.
- "p≈0.055 is marginal, not a positive demonstration" — STANDS; blocks
  promote. Failing to reject difference at p≈0.055 is absence of rejection,
  not a demonstration of homophony. The predecessor p-value in particular is
  a low-power artifact (disjoint singleton supports), not evidence of
  interchangeability.
- "60-03 x4 vs 68-03 x0 not tested for significance" — ANSWERED by testing.
  Fisher exact (60->03 4/17 vs 68->03 0/7): p=0.224 — non-discriminating.
  The 60->03 x4 sub-pattern (@690/@1366/@1644/@1674) does not distinguish
  60 from 68.
- "uniformity 17:7 skewed (necessary-but-insufficient per lane law)" —
  STANDS; blocks promote. χ²=4.167 on 17:7 vs 12:12, p≈0.041: exact
  uniformity rejected at α=0.05. Per lane law uniformity is necessary for
  homophony; the skew is a live caveat against the 2-cell claim.

## Verdict: NULL

All three bar clauses pass (clause 1 marginal), but promote is not earned:
two adverses stand unanswered — the p-values are a marginal non-rejection,
not a positive demonstration, and the 17:7 split violates the lane's
uniformity-necessary law. There is no positive interchangeability evidence in
free text: zero shared predecessor types, one shared successor type at 1 token
each. Kill is not earned either: no clause fails at kill grade, no window
forces the 2-cell claim false, and no cleaner rival value is demonstrated on
the same frames (60 and 68 share exactly one structural fact — the formula's
21-[third] slot). The data cannot distinguish "60~68 homophones" from "60 and
68 are distinct cells that happen to share the formula slot." Inconclusive —
null, with follow-ups.

## Follow-ups for the supervisor (nulls regenerate work)

### F1. subsample-power-60-68 — priority 1
- **claim:** "The p≈0.055 non-rejection is a power artifact of n=7, not evidence about 68's class."
- **bars:** (a) 10,000 draws of 7 tokens from 60's 17 free tokens, each draw permutation-tested against the remaining 60 tokens (same TV/B=20,000 method) — report the rejection rate at α=0.05; (b) if ≥80% of draws fail to reject, the null is a power artifact and the pair stays null-but-live; if the draws usually reject, 68 patterns genuinely differently from 60 → kill-grade against the pair.
- **evidence:** 68's 7 predecessors are disjoint singletons (zero type-overlap with 60's); the predecessor p=0.0546 cannot reject by construction.
- **adverses:** subsample draws are not independent of the full set; state the dependence caveat in the report.

### F2. frame-share-60-68 — priority 2
- **claim:** "60 and 68 share at least one free (non-formula) bigram or trigram frame, or none exists."
- **bars:** (a) exhaustive shared-frame census over free tokens: shared successor types, shared predecessor types, shared trigrams centered on the cell; (b) each shared frame gets a window-level parse under stated values; (c) if zero shared frames exist, record that as the standing negative (this battery found: shared succ {06} x1/x1, shared pred ∅).
- **evidence:** interchangeability is the positive content of a homophone claim; distributions alone cannot demonstrate it.
- **adverses:** a single shared 06-token is thin; do not over-read it.

### F3. nir-value-60-68 — priority 3
- **claim:** "60 and 68 both parse as 'nir' in their free windows."
- **bars:** (a) every free 60 window (x17) and 68 window (x7) parsed with the cell as 'nir' under standing values with zero hard contradictions; (b) kill iff any window forces non-'nir' or a cleaner rival value is demonstrated on the same frames; (c) the formula slots @227/@1783 cited, not re-proved.
- **evidence:** the 2-cell hypothesis exists to serve the "parvenir" reading (96="par" granted, 82="me" banked); the value claim is the testable core.
- **adverses:** 68's "68-21-67" x2 (@114/@504) must parse under 'nir' or be fenced with cause; 60->03 x4 (03 verb-stem, queued stem-03) constrains 60's right edge.
