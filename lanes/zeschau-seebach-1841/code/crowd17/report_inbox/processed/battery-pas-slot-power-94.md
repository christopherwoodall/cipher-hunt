# Battery `pas-slot-power-94` — verdict: KILL (discriminator retired)

**Bar (verbatim, pre-registered):** "resolve iff the 'pas'-slot discriminator separates promoted 94='ne' from baseline; retire the discriminator if it cannot"

Numbered clauses:
- C1 (separation): 94's 6 downstream-30 frames show a pas-slot signature distinct from the baseline 30 census → resolve.
- C2 (retire): if C1 fails, retire the 'pas'-slot discriminator as non-separating.

Result: **C1 FAIL (kill grade), C2 FIRES.**

## Method

Stream re-derived in-session from `code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed per `repair_parse.py`. `canonical.py` never used. Asserts held: 1,847 pairs, 96 groups, n(94)=37, n(30)=19.

- Downstream-30 frame of a 94: nearest following 30 on the same row within ≤20 pairs (parent definition from `battery-ne-08-frames`).
- Baseline: all 19 30-windows; 30s with no 94 within 20 upstream on the same row.

## Window-level evidence (@-offsets, 0-based)

94's 6 downstream-30 frames (5 distinct 30s — @1705's 30 is @1713's):
1. @558 (a3_02): "94 59 30" — ne est pas
2. @651 (a4_02): "94 76 49 24 26 30" — ne [76] [49] [24] [26] pas
3. @1363 (a7_06): "94 79 14 60 03 30" — ne [79] [14] [60] [03] pas
4. @1701 (a8_06): "94 30" — ne pas
5. @1705 (a8_06): orphaned; its downstream-30 (@1716) is owned by @1713
6. @1713 (a8_06): "94 44 59 30" — ne X est pas

Baseline (14 30s with no 94 within 20 upstream, same row): @30, @45, @483, @742, @993, @1114, @1222, @1251, @1269, @1309, @1327, @1561, @1729, @1733.

Predecessor census:
- 94-owned 30s: 59 x2, 26 x1, 03 x1, 94 x1 — all immediate post-verbal slot.
- Baseline 30s: 24 x3, 26 x3, 52 x2, 56 x2, 81 x1, 20 x1, 38 x1, 48 x1 — all immediate post-verbal slot.

## Per-clause pass/fail

**C1 FAIL.** The pas-slot signature is identical with and without an upstream 94:
- "26 30" occurs in both sets (@656 94-owned; @993, @1251, @1561 baseline).
- The byte-identical 5-gram "76 49 24 26 30" occurs at @652–656 (row a4_02, 94 upstream @651) AND at @989–993 (row a6_01, no 94 within 20 upstream on the row). This minimal pair forces the claim false: the 30 slot licenses identically without 94.
- Tight "V 30" slots ("24 30" x3 at @30/@1269/@1733, "48 30" @1222) occur baseline-only; tight "59 30" occurs only 94-owned, but "59" is provisional 'est' and the slot is the same post-verbal position. Nothing in slot geometry distinguishes the sets.

**C2 FIRES.** The 'pas'-slot discriminator cannot separate promoted 94='ne' from baseline. **Retired.** Its remaining use is descriptive only (labelling "ne...pas" shapes), never as a discriminator.

## Verdict: KILL

Kill target is the discriminator heuristic, not any banked value: 94='ne' (R19-167) stands untouched; 30='pas' stands; the battery-ne-08-frames null finding (31/37 of 94 lacks downstream-30, so pas-absence is not kill-grade) is adopted, not re-litigated. No standing/red-team verdict contradicted or downgraded; §7 intact. Per §4, kills regenerate no follow-ups.

Adverses: none listed. R5005, sealed gate instances, red-team adjudication queue untouched.
