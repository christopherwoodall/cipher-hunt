# Battery report: dwindow-voisin-family

**Target:** `dwindow-voisin-family` (P3)
**Date:** 2026-10-09
**Verdict:** NULL (fence executed)

## Bar (verbatim from queue, pre-registered before testing)

"resolve iff the 'vois-'-prefix arm parses with a named neighbor value; fence with stated cause otherwise"

## Bar restated as numbered clauses

1. RESOLVE (promote): at least one D-window parses 86 as the "vois-" prefix of a real French word, with the completing neighbor's value NAMED at battery grade or above, every group in the word assigned, and the clause grammatical.
2. ELSE: fence with stated cause (which naming acts would re-open the arm).

Bar not modified after seeing data.

## Method

Read BATTERY-PROTOCOL.md first; created `locks/dwindow-voisin-family.lock` on start (deleted on completion).
Re-derived the repaired 1,847-pair / 96-type stream in-session from `code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt` (parsed per `code/side-keyhunt/repair_parse.py`; asserts 1847/96 held). `canonical.py` never used. R5005, sealed gates, red-team queue untouched.

Adopted frame (verified, not assumed): D-life = 86-windows whose follower is not in {29,59,06}. Re-derived n(86)=32, n(D-life)=26 — matches the parent composition battery exactly. Neighbor values read live from `code/table-grid/table-registry.json` (post-R19 state).

Scope note: the claim is 86 as 'vois-' PREFIX, so only the follower can complete the word. Left neighbors are clause context, not word material. Real 1841 French words beginning "vois-": voisin, voisine, voisins, voisines — the completing suffix must be "in"/"ine"/"ins"/"ines" (no other "vois-*" headword exists).

## D-window census (re-derived, 0-based, ±3 context)

| idx | row | ctx | follower | follower value |
|---|---|---|---|---|
| 175 | a1_05 | 60 09 87 86 21 69 14 | 21 | noun (class only) |
| 300 | a2_04 | 78 40 97 86 91 18 89 | 91 | unvalued |
| 557 | a3_01 | 59 34 17 86 94 59 30 | 94 | ne (lead) |
| 661 | a4_02 | 62 16 00 86 50 80 03 | 50 | unvalued |
| 671 | a5_00 | 20 67 11 86 24 80 03 | 24 | verb (class only) |
| 716 | a5_01 | 63 00 66 86 01 02 21 | 01 | unvalued |
| 728 | a5_02 | 64 11 00 86 48 88 11 | 48 | e (prom) |
| 799 | a5_04 | 37 44 77 86 44 74 62 | 44 | unvalued |
| 867 | a5_07 | 47 46 00 86 70 87 77 | 70 | pre (gt) |
| 878 | a5_08 | 49 16 77 86 78 17 08 | 78 | ver (lead) |
| 899 | a5_08 | 14 98 83 86 16 92 67 | 16 | unvalued |
| 948 | a6_00 | 62 98 96 86 01 77 86 | 01 | unvalued |
| 951 | a6_00 | 86 01 77 86 96 87 46 | 96 | par (prom) |
| 962 | a6_00 | 67 96 00 86 56 41 19 | 56 | unvalued |
| 1002 | a6_02 | 82 33 00 86 56 47 91 | 56 | unvalued |
| 1099 | a6_06 | 06 29 67 86 52 82 94 | 52 | unvalued |
| 1128 | a6_07 | 37 43 00 86 52 37 86 | 52 | unvalued |
| 1131 | a6_07 | 86 52 37 86 24 77 86 | 24 | verb (class only) |
| 1134 | a6_08 | 86 24 77 86 20 62 98 | 20 | unvalued |
| 1147 | a6_08 | 42 98 98 86 67 33 66 | 67 | unvalued |
| 1335 | a7_05 | 52 39 83 86 71 64 60 | 71 | unvalued |
| 1345 | a7_05 | 52 38 47 86 66 73 34 | 66 | unvalued |
| 1458 | a7_09 | 61 21 67 86 66 79 17 | 66 | unvalued |
| 1506 | a7_11 | 42 33 00 86 56 41 12 | 56 | unvalued |
| 1739 | a8_07 | 12 48 52 86 12 34 94 | 12 | n (prom) |
| 1792 | a8_09 | 47 03 00 86 56 42 94 | 56 | unvalued |

## Per-window 'vois-'-composition test (86="vois" + named follower)

Every named-follower window composes a non-word:
- @557: "vois"+"ne" = "voisne" — not a French word.
- @867: "vois"+"pre" = "voispre" — not a French word.
- @878: "vois"+"ver" = "voisver" — not a French word.
- @951: "vois"+"par" = "voispar" — not a French word.
- @728: "vois"+"e" = "voise" — not a French word.
- @1739: "vois"+"n" = "voisn" — not a French word. (§3 bars inventing 12="in".)

Class-only followers (@175 21=noun-class, @671/@1131 24=verb-class) carry no named value; nothing nameable to compose. All 18 unvalued-follower windows likewise have no nameable completion.

Follower census: 56 x4, 52 x2, 01 x2, 66 x2, 24 x2, 21/91/94/50/48/44/70/78/16/96/20/67/71/12 x1. Named values present: ne, pre, ver, par, e, n, noun-class, verb-class. None is "in"/"ine"/"ins"/"ines" or any other real "vois-" suffix.

## Per-clause verdict

1. RESOLVE: FAIL — 0/26 D-windows parse a 'vois-'-prefixed word with a named neighbor value.
2. FENCE: FIRES.

**Verdict: NULL — fence executed.** The 'voisin'/'voisine'-family arm is not dead (no window forces it false), but it has zero battery-grade legs: no D-window follower has a named value completing "vois-" into a real French word. This converges with, and is independent of, the parent `voi-86-dwindow-composition` NULL.

Re-open condition (red-team venue or battery naming act): any D-window 86-follower value named to "in"/"ine"/"ins"/"ines" — candidates: 56 (x4, modal follower), 52, 01, 66, 24, 21, 91, 16, 20, 44, 50, 67, 71. Also `redteam-86-split-docket` (P1 queued) owns the split; a polyvalence split of 86 could put 'vois-' on a second arm.

## Adverses

- None listed in queue.

## Follow-up targets (for supervisor queuing; all verified ABSENT from battery-queue.json)

1. `vois-suffix-watch` (P4): gated re-fire of this target's C1 iff any D-window 86-follower value names to "in"/"ine"/"ins"/"ines" at battery grade or above.
2. `vois-follower-56-value` (P3): name 56's value — 56 is the modal 86-follower (4/26 D-windows); its value decides the largest single sub-block of the voisin-family test.
3. `voisin-corpus-suffix` (P4): corpus check — enumerate real French "vois-*" words attested in 1841 diplomatic French (voisin/voisine/voisins/voisines) to bound the suffix space future naming acts must hit.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-dwindow-voisin-family.md`
- Queue: `battery-queue.json` → `dwindow-voisin-family` status `verdict`, result `null`, date 2026-10-09 (pre-write assert: was `queued`, `verdict: null`; temp-file + rename; only this entry touched; JSON re-validated)
- Lock `code/crowd17/next-token/locks/dwindow-voisin-family.lock` created on start, deleted on completion.
- R5005, sealed gates, red-team adjudication queue untouched. No standing or red-team verdict contradicted or downgraded; §7 intact.
