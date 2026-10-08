# MEMO TO THE SMITH — word-boundary constraints for Track C (boundary-informed scoring)

**From:** WORD SEGMENTER, Seebach round 13 council (work order 5)
**Date:** 2026-10-07
**Artifact:** `code/crowd13/segmenter/word_boundaries.json` (machine-readable; this memo is the human-readable spec)
**Parse:** repaired 1,847-pair stream (`code/side-keyhunt/repaired_offsets.json`); positions 0-based; `start` inclusive, `end` exclusive.

---

## 1. What you're getting

32 confirmed multi-cell word segments, every position re-derived from the repaired stream (no banked positions trusted — all 8 words' counts and starts reproduced exactly). Each segment:

```json
{"start": 754, "end": 760, "word": ["11","70","82","34","29","40"],
 "gloss": "la première", "tier": "A+",
 "cells": "11=la(GT) 70=pre(GT) ...",
 "evidence": "...", "status": "live", "conflict_note": ""}
```

**Headline number: coverage is 72/1847 = 3.90%.** This is not a tiling — it is 32 anchor constraints. The value is boundary information at known-good points, not coverage. Do not penalize segmentations for cutting anywhere in the uncovered 96.1%; reward them for respecting the anchors.

## 2. Confidence tiers — how to consume each

| Tier | Meaning | Pairs | Track C treatment |
|---|---|---|---|
| **A+** | all cells GT ("la première" ×2) | 12 | **Hard constraint.** Veto any decode tiling that splits inside [s,e). |
| **A** | GT-anchored conditioned ("m'en" ×1, "ment" ×4) | 10 | **Hard constraint** on the segment interior. The *sound* is GT-grade; see §4 for the two `suspect` windows where only the word-edge is soft. |
| **B** | provisional-anchored ("par le" ×3, "en ce" ×10, "par ce que" ×3) | 35 | **Strong soft constraint.** Large bonus for cutting exactly at s and e; small penalty for splitting inside. |
| **B\*** | provisional, lane-standing ("cela" ×7, crowd5 unit_inventory — not council work, flagged honestly) | 14 | Same as B. |
| **C** | provisional + MEDIUM ("c'est" ×2; rests on 01="est" MEDIUM-confirmed, round-8 adjudicator GRANT) | 4 | **Bonus only, no penalty.** Weakest link; use as a nudge. |

Per-segment `status`: `live` (19) = clean; `live*` (8) = boundary stands, adjacency tension noted in `conflict_note` — do not let the *neighbor's* provisional value be forced by this boundary; `suspect` (2) = interior sound secure, word-edge soft (see §4); `superseded` (3) = boundary withdrawn — **do not use as constraints** (kept for audit; their pairs are covered by "cela").

## 3. The words (all board-anchored, none invented)

- **"la première"** 11-70-82-34-29-40 @754, @1034 — 7 pencil GT. A+.
- **"m'en"** 82-84 @166 — 82=m GT; 84="en" conditioned iff pre=82 (ISLET 1, adjudicator GRANT). A. Note: the *only* 82-84 in the stream (n=1) — the islet's GT arm is exactly this word.
- **"ment"** 82-06 @579, @737, @1183, @1354 — 82=m GT; 06="ent" iff pre=82 (ISLET 3, F33 biconditional, adjudicator GRANT). A. **The census is exhaustive: these are the only four 82-06 in the stream.** Do not generalize "ment" to any other 06 (elsewhere 06 is verb-stem class).
- **"par le"** 96-00 @47, @465, @960 — 96=par PROV; 00="le" iff pre=96 (ISLET 2, red-team GRANT). B. ("par pour" is ungrammatical at all three — the islet is load-bearing.)
- **"en ce"** 24-87 ×10 — 24="en" STRONG (F31); 87="ce" PROV (positional allophone; reframes the F56 merger kill as complementary distribution). B. 3 windows superseded (see §4) → 7 live.
- **"par ce que"** 96-87-46 @224, @952, @1526 — 96=par PROV, 87=ce PROV, 46=que GT. B. CONFIRMED formula (french-blitz formulae-inventory §5); the council drag's positive control re-found all three independently (drag_hits.json). (Crowd3's frenchman reads the same bytes as fused "parce que" — same cells either way.)
- **"c'est"** 87-01 @344, @1028 — 87=ce PROV, 01="est" MEDIUM-confirmed. C. (47→01 @194 is the 47="ce"-LEAD analog — excluded, see §5.)
- **"cela"** 87-11 ×7 — 87=ce PROV, 11=la GT. B\*. Crowd5 standing unit (frenchman-verified ear-spelling regularity), included for completeness.

## 4. Consistency adjudications (the falsifier pass — what broke and what survived)

1. **"en cela" kills "en ce" at 3 windows.** The stream has 24-87-11 at @73/@162/@829. Two candidate parses share cell 87: "en ce"+"la" vs "en"+"cela". Period-corpus check: "en cela" 8×, "en ce la" 0× — "en ce la" is ungrammatical (bare "la" after "en ce"). The "en ce" boundary is **withdrawn** at those 3 windows (status `superseded`); "cela" holds. Net effect on coverage: zero (same pairs, covered by "cela").
2. **"ment" word-edge soft at @579/@1183.** Both are 94-82-06-06 ("ne ment [06-stem]") with no "pas" after. Bare "ne ment" is 0× in the period corpus ("il ne ment pas" is attested, RdM). Competing parse: m|ent|[06-stem] ("m'entend"-type) — ISLET 3's "ent" reading at the first 06 stands; only the word boundary after it is suspect. By contrast "ment" is a secure complete word at @1354 ("ment pas" ✓, 52="pas" STRONG) and @737 ("ment pour", grammatical). Track C: enforce the 82-06 *sound* everywhere (A-grade); enforce the word-edge only at @737/@1354.
3. **"en ce" @823 vs 59="est"@825.** "en ce est" is ungrammatical ("ce est"=0; frame59-map already ruled this window UNCLASSIFIED). Symmetric tension — it constrains 59@825, it does not falsify "en ce". Do not let Track C's boundary bonus launder 59="est" at @825.
4. **"m'en" @166 vs 24="en"@165.** "en m'en" is 0× in the corpus. The word is GT-anchored and stands; the pressure falls on 24@165 (or the 94-24 junction), not on the boundary.
5. **No cross-tier overlaps.** The only overlaps are the three "en ce"×"cela" collisions (same-tier B/B\*), adjudicated in (1). "c'est", "par ce que", "par le", "la première" are overlap-free.

## 5. Deliberately excluded (do not promote without new evidence)

- **94-87 "en ce" @1169** — the conditioned-94 arm (ISLET 4). Real reading, but the word rests on a conditioned 94, not on the confirmed 24-87 bigram. Available as an optional soft constraint; not in the map.
- **47-01 "c'est"-analog @194** — rests on 47="ce" LEAD. Same treatment.
- **Council-drag leads** (drag_hits.json, landed mid-task): "tout ce qui" ×4 and "le prince" ×2 are **leads, not words** (null_report: FDR ≈ 1.41/9, real does not beat all 20 shuffles). Two interactions with the map: (a) "tout ce qui"@179/@1766/@1774 overlaps "en ce" but requires 24="tout", contradicting 24="en" STRONG (F31) — the drag oracle doesn't encode 24, so it scored neutral; the lead is dead at those windows and survives only @1799 (79-87-64, 79 unidentified). (b) "le prince"@1240/@1401 overlaps "cela"@1242/@1403 on cell 87 — genuine word-membership ambiguity ("le prince"+"la" vs "le [81]"+"cela"; both windows byte-parallel 67-77-81-87-11-00). Unresolvable at current board (81 unidentified); "cela" stands as the confirmed unit, 87@1242/@1403 flagged `live*`.

## 6. Numbers the Smith needs

- Segments: 32 (29 usable: 19 live + 8 live* + 2 suspect-edge; 3 superseded kept for audit only).
- Coverage: 72/1847 pairs = **3.90%** (A+ 0.65%, A 0.54%, B 1.89%, B\* 0.76%, C 0.22%).
- Hard (veto-split) budget: 22 pairs (A+/A interiors, minus the 2 suspect edges).
- Soft budget: 53 pairs (B/B\*/C).
- Every count and start was re-derived from the repaired stream in `segment.py` (re-run: `python3 code/crowd13/segmenter/segment.py`); all matched banked values — zero phantoms, zero missing.
- Consuming this in Track C's DP: add a boundary term that (i) vetoes tilings splitting inside A+/A segments (except the 2 suspect edges), (ii) bonuses tilings cutting exactly at segment edges for B/B\*/C, (iii) applies **no penalty** for cuts in the uncovered 96.1%. The anti-Goodhart point from the Table Reconstructor: morpheme-salad has no word structure — these 32 anchors are where the decode's word structure is *known*, so a decode whose best tiling violates them is suspicious regardless of its word-unigram score.

## 7. Caveats

- Coverage is low (3.90%) — this constrains 32 points, it does not segment the despatch. Say so in any writeup; don't let the number get rounded up into a claim.
- All conditioned words (m'en, ment, par le) are frame-bound by their islets; the map asserts nothing about those cells outside the listed windows.
- "cela" (B\*) is crowd5-standing, not round-13 council product — graded honestly, not smuggled.
- drag_hits.json was integrated mid-task per the work order; it contributed zero new confirmed words and one independent re-confirmation ("par ce que" positive control).
