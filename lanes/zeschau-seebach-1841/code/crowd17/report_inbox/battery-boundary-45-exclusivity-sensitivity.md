# Battery report: boundary-45-exclusivity-sensitivity

- Target: `boundary-45-exclusivity-sensitivity` (priority 3, status queued)
- Claim: the {13, 01}-exclusivity survives leave-one-out
- Worker: 30a5a7ea-ebb5-4110-9772-4daa85d397c1
- Date: 2026-10-09
- Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`). `canonical.py` NOT used. R5005, sealed gates, red-team queue untouched.
- Prior work built on (not duplicated): `report_inbox/processed/battery-dict-45-contact-update.md` (PROMOTE, Fisher p=0.00205 full-profile / p=0.00260 exclusive-variant) and `report_inbox/processed/battery-dict-78-45-wordbound.md` (null, escalated). All counts below re-derived independently in this session.

## Bar (verbatim, pre-registered)

"recompute the Fisher table dropping each post-78 window in turn; the boundary is robust iff exclusivity holds (p<0.05) in all four leave-one-out tables; also test 13/01 against other word-final positions to rule out a global frequency artifact"

## Bar restated as numbered pass/fail clauses (frozen before testing)

1. Recompute the exclusive-variant Fisher table ({13,01} vs rest, rows post-78 / standalone) with each of the 4 post-78 windows dropped in turn; the boundary is robust iff p<0.05 (two-sided Fisher exact) in all four leave-one-out tables.
2. Artifact check: test 13/01 against other word-final positions — show the {13,01}-exclusivity is 45-specific and not a global frequency artifact.

## Method

Re-derived the full 45 census on the repaired stream (0-based pair indices used throughout, matching the contact-update report's convention). Split the 22 occurrences of 45 by predecessor = 78 vs != 78. Built the exclusive-variant 2x2 table: rows {post-78, standalone}, columns {follower in {13,01}, follower not in {13,01}}. Computed two-sided Fisher exact exactly (math.comb hypergeometric, P(tables) <= P(observed) convention), cross-checked against scipy.stats.fisher_exact (identical to 6 dp). For the artifact check: (a) measured the global follower base rate of {13,01}; (b) censused the full predecessor distributions of 13 and 01; (c) counted distinct predecessors of any {13,01} follower slot stream-wide.

## Window-level evidence (0-based @-offsets)

- 45 census re-derived: n(45)=22. Post-78 (n=4): 45@314 (row a2_04, fol=64), 45@574 (row a3_02, fol=13), 45@983 (row a6_01, fol=01), 45@1165 (row a6_09, fol=13). Byte-identical to the contact-update census. Standalone (n=18): followers {93x3, 23x3, 28x2, 64x2, 91, 54, 88, 46, 94, 08, 58, 36}.
- Exclusive-variant full table: post-78 [3,1] vs standalone [0,18]; two-sided p=0.002597 (matches contact-update's 0.00260; scipy cross-check 0.002597).
- n(78)=31 stream-wide, so the post-78 class (n=4) is a 45-co-occurrence property, not an artifact of 78's rarity.
- Global census: n(13)=12, n(01)=28. 13's predecessors: 65x3, 69x2, 45x2, 00, 97, 95, 35, 99 (10/12 non-45). 01's predecessors: 37x3, 16x2, 87x2, 85x2, 86x2, 76x2, 32, 41, 47, 66, 10, 33, 30, 82, 08, 45, 48, 46, 88, 17, 15 (21 distinct predecessors; evidence string said 22 — stale by one, immaterial). {13,01} appear as followers after 28 distinct predecessor groups stream-wide.

## Leave-one-out tables (exclusive variant {13,01})

| dropped window | table | two-sided p | scipy check |
|---|---|---|---|
| @314 (fol 64, the non-exclusive leg) | [[3,0],[0,18]] | 0.000752 | 0.000752 |
| @574 (fol 13) | [[2,1],[0,18]] | 0.014286 | 0.014286 |
| @983 (fol 01) | [[2,1],[0,18]] | 0.014286 | 0.014286 |
| @1165 (fol 13) | [[2,1],[0,18]] | 0.014286 | 0.014286 |

All four < 0.05. The tightest tables are the three that drop an exclusive leg (p=0.0143); the result survives every single-window deletion.

For completeness, the full-profile variant {13,01,64} leave-one-out also clears in all four tables: full p=0.002051; drop @314 p=0.007519; drop @574/@983/@1165 p=0.023923 each.

## Artifact check results

- Global base rate: {13,01} occupy 40 of 1,846 follower slots = 2.17%. Under this rate, 0/18 standalone-{13,01} has P=0.67 — unsurprising. The rarity works AGAINST the null, not for it: given only 3 {13,01} among 45's 22 followers, the chance all 3 land in the 4 post-78 slots by chance is C(4,3)/C(22,3)=0.0026 — exactly the Fisher result. The test already conditions on the margins, so no global-frequency correction is owed.
- Promiscuity: {13,01} follow 28 distinct predecessor groups stream-wide; 13 has 10/12 non-45 predecessors and 01 has 21 distinct predecessors. They are ordinary, widely-distributed tokens — there is no global restriction keeping them out of 45-like positions. The exclusivity is therefore 45-specific (post-78 conditioned), not a global frequency artifact.

## Per-clause pass/fail

1. Leave-one-out robustness: PASS. All four tables significant at p<0.05 (range 0.00075–0.01429).
2. Artifact check: PASS. 13/01 are ordinary tokens with 28 distinct predecessors; no global frequency artifact explains the 45-specific exclusivity.

## Adverses answered

- "small-n caveat": ANSWERED and fenced with stated cause. Fisher exact is exact for small n; the sensitivity analysis was the point of this battery. Noted: the result is one-window sensitive at the margins — dropping any one exclusive leg moves p from 0.0026 to 0.0143 — but it clears the pre-registered 0.05 bar in every leave-one-out table. Any future re-parse that moves a post-78 window re-opens this verdict (same caveat as the contact-update promote).

## Verdict: promote (narrow sensitivity finding)

Both bar clauses pass; the adverse is fenced with stated cause. The {13,01}-exclusivity is robust to single-window deletion: the contact-update boundary (promoted, ver-78-independent) survives leave-one-out at p<0.05 in all four tables, and the global-frequency artifact check finds no alternative explanation. This promotes no value and re-grades no lead — it hardens the contact-profile leg of the 78-45 boundary. No standing verdict contradicted or downgraded; no polyvalence declared (protocol S7 intact).

## Follow-ups

None required (verdict is promote, not null). One flag carried forward from the contact-update report: the post-78 class is n=4; any future re-parse that moves a single post-78 window re-opens this verdict.

## Bookkeeping

- Lock `locks/boundary-45-exclusivity-sensitivity.lock` created on start, deleted on completion.
- `battery-queue.json`: `boundary-45-exclusivity-sensitivity` queued -> verdict/promote via temp-file + rename (pre-write assert confirmed queued/verdictless, JSON re-validated post-write).
