# Battery `08-position-profile` — verdict: PROMOTE

## Bar (pre-registered verbatim)

"Position profile stated with byte evidence at battery grade."

Restated clauses:
- C1: all 18 08-windows censused byte-exact (predecessor, follower, row).
- C2: word-position signature (initial / internal / final) stated for each window at battery grade.

## Method

Re-derived the repaired 1,847-pair / 96-type stream in-session from
`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`
(asserts held: 1847 pairs, 96 types). `canonical.py` never used.

Position logic (battery-grade rules only):
- 08 is letter-tier (adopted `stem-08-letter-probe` PROMOTE); a single-letter
  standalone 08 is kill-grade dead (adopted `ce-08-31-frame`).
- A word boundary is forced after a banked/promoted free word
  (17=fois, 47=ce, 67=et/veut, 87=ce) and before one (67 after @198).
- A bound letter after 08 (34='i', 29='er') constrains 08 to
  initial-or-internal — never word-final.
- 40='e' (ground truth) has no battery-grade bound/free ruling, so the
  40|08 boundary is stated as boundary-dependent, not forced.

## Findings — full census (0-based, row-validated)

| @ | row | pre [08] fol | position reading |
|---|---|---|---|
| 35 | a1_01 | 01 [08] 91 | undetermined (both neighbors open) |
| 60 | a1_01 | 41 [08] 34 | initial-or-internal (before bound 'i') |
| 98 | a1_02 | 85 [08] 21 | undetermined |
| 198 | a2_00 | 60 [08] 67 | **word-final** — free 67 forces boundary after; standalone dead forces left fusion into [60 08] |
| 534 | a3_01 | 16 [08] 24 | initial-or-internal (fused with INF-16 left or 24 right) |
| 631 | a4_01 | 67 [08] 52 | **word-initial** (free 67 forces boundary before) |
| 779 | a5_04 | 37 [08] 29 | initial-or-internal (before bound 'er') |
| 881 | a5_08 | 17 [08] 31 | **word-initial** (free 17=fois; "08 31" word-initial-letter slot per PROMOTE) |
| 922 | a5_09 | 40 [08] 65 | boundary-dependent: initial iff 40|08 boundary, else internal |
| 944 | a5_10 | 40 [08] 62 | boundary-dependent: initial iff 40|08 boundary, else internal |
| 975 | a6_01 | 45 [08] 01 | initial conditional on A11 45='ce' (lead, not granted) |
| 1302 | a7_03 | 37 [08] 43 | undetermined |
| 1323 | a7_04 | 80 [08] 62 | undetermined |
| 1339 | a7_05 | 60 [08] 65 | undetermined |
| 1488 | a7_10 | 87 [08] 31 | **word-initial** (free 87=ce; PROMOTE) |
| 1520 | a7_11 | 67 [08] 31 | **word-initial** (free 67; PROMOTE) |
| 1592 | a8_02 | 47 [08] 81 | **word-initial** (free 47=ce; PROMOTE) |
| 1610 | a8_03 | 23 [08] 55 | undetermined |

18 = 18. n(08)=18 matches the adopted full census.

## Profile (battery grade)

- **Forced word-initial: 5** (@631, @881, @1488, @1520, @1592) — all three
  "08 31" windows plus @631. Skew is strongly initial.
- **Forced word-final: 1** (@198, "[60 08]" before free 67).
- **Initial-or-internal: 3** (@60, @534, @779).
- **Boundary/conditional: 3** (@922, @944 on the 40|08 boundary; @975 on A11).
- **Undetermined: 6** (@35, @98, @1302, @1323, @1339, @1610).

Headline: 08 is a letter-tier cell with an initial-skewed position signature,
but NOT uniformly word-initial — @198 gives a forced word-final case, so the
letter-probe's word-initial-letter slot is a [08][31]-window phenomenon, not a
global 08 property. No window forces standalone 08 (consistent with the
kill-grade standalone kill). No 08 value named; profile is position-only.

## Per-clause verdict

- C1 PASS — all 18 windows byte-exact in the table above.
- C2 PASS — position signature stated per window with battery-grade grounds.

**Verdict: PROMOTE.** No adverses listed. No standing/red-team verdict
contradicted or downgraded; §7 intact (no new polyvalence; the @198 final
letter is a letter position, not a second value). Canonical-stream caveat
stands (rows unvalidated except where the pencil gloss lands).

No follow-ups (promote per §4).
