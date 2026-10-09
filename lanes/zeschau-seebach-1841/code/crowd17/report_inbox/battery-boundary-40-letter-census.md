# Battery report: boundary-40-letter-census

## Bar (verbatim from queue)

"use granted-value neighbours ('29 40' x9 analytic '-ere' as the word-internal control); yields a prior for 40|92 boundary placement, reusable for other segmentation targets"

## Bar restated as numbered clauses

- C1: Classify all 21 of 40's windows as word-final-letter vs word-internal-letter, using granted-value (ratified) neighbours only.
- C2: Characterize the '29 40' x9 control set (the bar's analytic '-ere' control).
- C3: Yield a reusable prior for 40|92 boundary placement.

## Method

- Re-derived the repaired 1,847-pair / 96-type stream in-session from
  `code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`
  (parse per `code/side-keyhunt/repair_parse.py`). n(40) = 21, byte-confirmed.
- `canonical.py` never touched. R5005, sealed gates, red-team queue untouched.
- Standing (ratified) values used as boundary evidence, verified against
  `code/table-grid/table-registry.json`:
  banked GT 29='er', 40='e', 64='qui', 11='la', 46='que';
  prom 17='fois', 96='par', 47='ce', 79='tout', 84='on';
  cls 65='noun', 92='verb' (subset-scoped), 36='noun';
  R17-003 letter tier 48='e'; 67=et/veut sole polyvalence with positional rule
  (67='veut' iff follower infinitive-shaped).
- Classification rule: 40 is word-final (W) iff a granted word-level group
  abuts it across the boundary (a word must end/start there); word-internal (I)
  iff letter-tier composition forces continuation on both sides; word-initial (B)
  iff a granted word ends immediately before 40; undecidable/fenced (U) iff all
  abutting groups are open at standing grade.
- Offsets below are 0-based stream indices of 40 ("0b"), with 1-based @ in
  parentheses. Context is ±3 pairs.

## Window-level evidence

| # | 0b (@1-based) | row | window | class | rationale |
|---|---|---|---|---|---|
| 1 | 63 (@64) | a1_01 | 08 34 29 40 12 94 92 | I | 12='n' letter-tier cannot stand alone and "nne" is not a French word onset; 40 composes into "…erne…"/"…enne…" mid-word. Canonicality caveat: row a1_01 offset-1 (seg-a1_01) is red-team territory. |
| 2 | 292 (@293) | a2_03 | 09 64 29 40 65 16 01 | W | 65=noun cls begins a new word. |
| 3 | 298 (@299) | a2_04 | 01 11 78 40 97 86 91 | U | 78, 97 open. |
| 4 | 335 (@336) | a2_05 | 45 54 88 40 03 64 31 | U | 88, 03 open at standing grade (battery verb-class / verb-stem-class unratified). Battery-tier note: under 03=verb-stem-class, 40 would be W. |
| 5 | 353 (@354) | a2_06 | 74 67 78 40 92 98 92 | W | 92=verb cls begins a new word. **This is the sole 40→92 window: the boundary falls between 40 and 92.** |
| 6 | 501 (@502) | a2_11 | 47 11 29 40 56 39 68 | U | 56 open (battery verb class-level unratified). |
| 7 | 598 (@599) | a4_00 | 85 01 29 40 03 39 26 | U | 03 open. |
| 8 | 686 (@687) | a5_00 | 92 64 29 40 65 94 29 | W | 65=noun cls begins a new word. |
| 9 | 752 (@753) | a5_03 | 64 02 97 40 67 11 70 | W | 67='et' (follower 11='la' not infinitive-shaped, positional rule); word-level, boundary after 40. |
| 10 | 759 (@760) | a5_03 | 82 34 29 40 20 62 94 | W | Pencil crib "la premiere": gloss-anchored word-final 'e'. |
| 11 | 820 (@821) | a5_05 | 74 47 78 40 95 13 24 | U | 78, 95 open. |
| 12 | 848 (@849) | a5_07 | 33 96 \| 40 62 21 67 91 | B | Row boundary a5_06/a5_07 falls between 96 and 40; 96='par' prom is a complete word; 40 is row-initial 'e' beginning a new word. |
| 13 | 921 (@922) | a5_09 | 49 74 74 40 08 65 71 | U | 74, 08 open. |
| 14 | 943 (@944) | a5_10 | 01 07 50 40 08 62 98 | U | 50, 08 open. |
| 15 | 1039 (@1040) | a6_03 | 82 34 29 40 17 77 82 | W | Pencil crib "la premiere"; 17='fois' prom word-level. |
| 16 | 1051 (@1052) | a6_04 | 41 88 29 40 29 74 74 | W | "29 40 29" = "ereer", not a French letter sequence (stated lexicon negative) → boundary "…ere \| er…". |
| 17 | 1238 (@1239) | a7_01 | 56 10 03 40 67 77 81 | W | 67='et' (follower 77 not infinitive-shaped). |
| 18 | 1399 (@1400) | a7_07 | 47 78 48 40 67 77 81 | W | 67='et'; 48='e' letter tier (R17-003). |
| 19 | 1557 (@1558) | a8_01 | 13 93 61 40 17 11 26 | W | 17='fois' prom forces boundary ("61 40 17" = "première fois" locus; boundary holds regardless of 61's battery-grade value). |
| 20 | 1711 (@1712) | a8_06 | 12 06 29 40 65 94 44 | W | 65=noun cls begins a new word. |
| 21 | 1746 (@1747) | a8_08 | 82 46 56 40 06 65 34 | U | 56, 06 open (06='ent' battery-promoted, unratified). |

## Census

- Word-final (W): 11 (windows 2, 5, 8, 9, 10, 15, 16, 17, 18, 19, 20)
- Word-internal (I): 1 (window 1)
- Word-initial (B): 1 (window 12)
- Fenced/undecidable (U): 8 (windows 3, 4, 6, 7, 11, 13, 14, 21)
- Total: 21. Cross-check: seg-92-354-356's null independently reported
  "8/21 have no clean word-final prior" — the same 8 windows fence here.

## Per-clause results

- **C1: PASS.** All 21 windows classified on ratified-value evidence; 8 fenced
  with stated cause (open neighbours at standing grade).
- **C2: PASS with headlined correction.** The '29 40' x9 control set
  (windows 1, 2, 6, 7, 8, 10, 15, 16, 20) is **word-final-dominant, not
  word-internal**: 6 W / 1 I / 2 U over the nine (decided: 6/7 W).
  The bar's parenthetical "as the word-internal control" is contradicted by the
  evidence and is corrected here, not hidden. The pencil-crib windows
  (@759/@1039, "premiere") anchor the W reading at gloss grade.
- **C3: PASS.** Reusable prior: **P(word boundary immediately after 40) =
  11/13 ≈ 0.85** over decided windows (8/21 fenced). For the 40|92 placement:
  the single 40→92 window in the stream (@0b353, a2_06) is itself W, so the
  prior resolves to **boundary between 40 and 92** — 40 does not compose
  rightward into 92's word. (Consistent with the standing kill of 92='-ère'.)

## Adverses

None listed.

## Verdict: PROMOTE (finding grade)

The census and the 40|92 prior are delivered as stated; the control-premise
correction above is the headline. Promotes no value, kills nothing, re-grades
no lead; §7 intact. No standing verdict contradicted or downgraded.
No follow-ups required (promote, not null).
