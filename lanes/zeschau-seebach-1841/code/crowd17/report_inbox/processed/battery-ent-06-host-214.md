# Battery `ent-06-host-214` — report

Target: `ent-06-host-214` (P3). Worker: 815b3552-b63d-426b-a69b-18bdb546288b. Date: 2026-10-09.

## Bar (verbatim, pre-registered before testing)

"'ent' binds only to licensed verbal / 94-82 frames; if no host class covers '[noun] ent [est] que', fence the span as residual."

Restated as numbered clauses:
- **C1** — 06's host classes are named across all 44 06-windows with byte evidence: 'ent' binds only to licensed verbal / 94-82 frames.
- **C2** — if no host class covers the '[noun] ent [est] que' span, the span is fenced as residual with stated cause.

Adverses: none listed.

## Method

Repaired 1,847-pair / 96-type stream re-derived in-session from `code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt` (parse logic per `code/side-keyhunt/repair_parse.py`; asserts held: 1,847 pairs, 96 types). `canonical.py` never used. Positions are 0-based. Registry classes from `code/table-grid/table-registry.json` (post-R19: 62 unvalued after 'il' kill; 78=ver/lead value open; 59=est/prov).

## The '[noun] ent [est] que' locus

Byte-confirmed: `@214=78 | @215=06 | @216=59 | @217=46`, row a2_00 ("…[19] [74] le ver ent [59=est/prov] [46=que/gt]…"). The 06 in question is at **0-based @215** (earlier batteries' "@214" labels the 78 head). pre=78 (ver/lead, value open), fol=59 (est/prov).

## Census: all 44 06-windows

| pos | row | pre (cls) | fol (cls) | host class |
|-----|-----|-----------|-----------|------------|
| 6 | a1_00 | 41 (?) | 77 (le/prov) | none |
| 85 | a1_02 | 14 (?) | 88 (gov/cls) | none |
| 184 | a1_05 | 37 (?) | 00 (pour/prom) | none |
| 206 | a2_00 | 42 (noun/cls) | 77 (le/prov) | none |
| 215 | a2_00 | 78 (ver/lead) | 59 (est/prov) | **none → fenced (C2)** |
| 267 | a2_02 | 42 (noun/cls) | 73 (?) | none |
| 271 | a2_03 | 11 (la/gt) | 67 (?) | none |
| 319 | a2_04 | 94 (ne/lead) | 11 (la/gt) | none |
| 346 | a2_05 | 01 (?) | 70 (pre/gt) | none |
| 370 | a2_06 | 17 (fois/prom) | 21 (noun/cls) | none |
| 399 | a2_07 | 48 (e/prom) | 11 (la/gt) | none |
| 470 | a2_10 | 80 (?) | 67 (?) | none |
| 522 | a3_00 | 77 (le/prov) | 55 (?) | none |
| 544 | a3_01 | 42 (noun/cls) | 00 (pour/prom) | none |
| 580 | a3_02 | 82 (m/gt) | 06 (ent/prom) | **F61 94-82 "ment"** |
| 581 | a3_02 | 06 (ent/prom) | 50 (?) | doubling, outside F61 scope |
| 666 | a4_02 | 62 (?) | 00 (pour/prom) | none |
| 738 | a5_02 | 82 (m/gt) | 00 (pour/prom) | **F61 94-82 "ment"** |
| 773 | a5_03 | 07 (?) | 94 (ne/lead) | none |
| 789 | a5_04 | 84 (on/prom) | 77 (le/prov) | none |
| 890 | a5_08 | 86 (INF/cls) | 77 (le/prov) | none |
| 967 | a6_00 | 24 (verb/cls) | 77 (le/prov) | none (no named stem) |
| 1080 | a6_05 | 64 (qui/prom) | 52 (?) | none |
| 1091 | a6_05 | 80 (?) | 43 (noun/cls) | none |
| 1096 | a6_06 | 81 (?) | 29 (er/gt) | none |
| 1120 | a6_07 | 12 (n/prom) | 14 (?) | none |
| 1122 | a6_07 | 14 (?) | 11 (la/gt) | none |
| 1184 | a6_10 | 82 (m/gt) | 06 (ent/prom) | **F61 94-82 "ment"** |
| 1185 | a6_10 | 06 (ent/prom) | 59 (est/prov) | doubling, outside F61 scope |
| 1188 | a6_10 | 42 (noun/cls) | 84 (on/prom) | none |
| 1252 | a7_02 | 30 (pas/prom) | 65 (noun/cls) | none |
| 1328 | a7_04 | 30 (pas/prom) | 62 (?) | none |
| 1355 | a7_05 | 82 (m/gt) | 52 (?) | **F61 94-82 "ment"** |
| 1388 | a7_07 | 16 (?) | 29 (er/gt) | none |
| 1475 | a7_10 | 60 (?) | 67 (?) | none |
| 1537 | a8_00 | 62 (?) | 21 (noun/cls) | none |
| 1562 | a8_01 | 30 (pas/prom) | 60 (?) | none |
| 1667 | a8_05 | 64 (qui/prom) | 91 (?) | none |
| 1709 | a8_06 | 12 (n/prom) | 29 (er/gt) | none |
| 1720 | a8_07 | 68 (noun/cls) | 11 (la/gt) | none |
| 1734 | a8_07 | 30 (pas/prom) | 60 (?) | none |
| 1747 | a8_08 | 40 (e/gt) | 65 (noun/cls) | none |
| 1762 | a8_08 | 93 (verb/cls) | 77 (le/prov) | none (no named stem) |
| 1815 | a8_10 | 42 (noun/cls) | 29 (er/gt) | none |

Totals: **44 = 4 F61 + 2 doubling-out-of-scope + 38 unhosted.** 38+2+4=44 ✓.

## Host-class findings

**F61 94-82 frame (4 windows, licensed):** @580, @738, @1184, @1355 — "82 06" = "m"+"ent" = "ment" under banked 82='m'. Adopted from `f61-06-scope-precise` PROMOTE (cited, not re-litigated); the four positions re-verified byte-exact here. No row-join artifact (the four row-straddling 06 windows @271/@399/@773/@1091 are all unhosted — the F61 set is row-internal).

**Licensed verbal-stem host (0 windows):** the only verbal-class predecessors are @967 (pre=24, verb/cls, R24: finite/modal, value unnamed), @1762 (pre=93, verb/cls, value open), @890 (pre=86, INF/cls — "[inf] ent" has no licensed morphology). A bound 3pl 'ent' needs a named stem; none exists at battery grade, and §3 bars inventing one. No named verb stem precedes any 06 stream-wide (no 85-stem predecessor anywhere).

**Doubling seconds (2, outside scope):** @581, @1185 — per standing `seg-94-82-06-f3` / `second-06-nonent`: first 06 covered by F61, second outside scope. Untouched.

**Unhosted (38):** noun predecessors (42×5, 68×1), function words (11, 30×4, 17, 48, 40, 12×2, 94), unvalued cells (41, 14×2, 37, 01, 80×2, 62×2, 07, 81, 16, 60), verb-class without stem (above), ver/lead heads (78 @215, 64×2), le-provisional (77 @522), on (84 @789). In none of these is 'ent' bound to anything — the ent-06 PROMOTE value stands globally, but no morphological host is licensed. No window binds 'ent' to an unlicensed frame; 'ent' is simply unbound at these positions.

## C2: the @215 span — FENCED

No host class covers "ver ent est" at @215:
1. "verent" is not a French word and "entest" is not a French word (converges with `ver78-rerun-214-1543` NULL's L3, adopted).
2. 78's value is open (ver-78 LEAD, red-team R16-005 venue); 'ent' cannot bind as a 3pl ending to an unnamed stem at battery grade (§3).
3. Freestanding 'ent' is not a French word; the clerk single-consonant license is dead at kill grade (`spell-single-consonant`).
4. The wider @206–216 span has no licensed verbal host either (@206 pre=42 noun).

**Fence:** the @215 "ver ent [est]" continuation is fenced as a genuine residual with stated cause above. Fence, not kill: a red-team naming of 78's value (R16-005) could re-open it. The "le ver" NP itself is untouched (not kill grade).

## Per-clause results

- **C1 PASS** — all 44 windows classified with byte evidence: licensed hosts are the F61 94-82 "ment" frame (4 windows); the licensed verbal-stem class is empty at battery grade (0 windows); no window binds 'ent' to an unlicensed frame.
- **C2 FIRES (else-arm)** — @215 fenced as residual with stated cause.

No standing/red-team verdict contradicted or downgraded (ent-06, F61 scope, second-06 fences, R24, ver-78 LEAD all adopted as premises); §7 intact; no polyvalence declared. Canonical-stream caveat stands (rows a2_00 offsets unvalidated).

## Verdict: PROMOTE

The bar's census deliverable is complete (44/44, byte-exact) and the designed else-arm executed for the one span the claim names. No follow-ups required per §4 — the natural re-opens (78 value naming) are already red-team venue (R16-005); no new battery target is live on current premises.

## Bookkeeping

- Queue: `ent-06-host-214` → `status: verdict`, `result: promote`, 2026-10-09 (pre-write assert passed — was queued/verdictless; temp-file + rename; JSON re-validated; own entry only; no downgrade).
- Lock created on start, deleted on completion (verified gone). R5005, sealed gates, red-team adjudication queue untouched.
