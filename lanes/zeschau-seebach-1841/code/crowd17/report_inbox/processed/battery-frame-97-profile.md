# Battery report: frame-97-profile

Target: frame-97-profile | priority 2
Claim: "97's class is named from its contact profile"
Worker: e6e0ba9e-6f70-4ca5-999a-0c1a0f20c366 | 2026-10-08T23:54:00Z
No stale lock was present (locks/ held only NOTE.md).

## Bar (verbatim, pre-registered)

"(a) class named (infinitive? noun? verb?) with >=3 frame-legs from the 10-window census ('pour'+97 x4, 81-97 x2, 97-46 'que', 97@1823 'pour 97 pour 86er'); (b) the 97-86 @299 contact explained or fenced with stated cause"

## Bar restated (numbered pass/fail clauses; frozen before testing)

1. 97's class is named (infinitive, noun, or verb) with >=3 frame-legs drawn
   from the 10-window census.
2. The 97-86 contact @299 is explained, or fenced with a stated cause.

## Method

Parsed `data/upstream-ct_R5005.txt` with
`code/side-keyhunt/repaired_offsets.json` exactly like
`code/side-keyhunt/repair_parse.py` (stride-2 pairing per row offset).
Verified 1,847 pairs. `canonical.py` not used. R5005, sealed gates, and the
red-team queue untouched. Every number below traces to this stream.
@n = pair-index offsets on the repaired stream.

## 97 census (re-derived, n=10)

All 10 windows of 97, wide context (target bracketed):

- @2 (a1_00): `09 00 [97] 51 47 41` — "pour 97"
- @94 (a1_02): `41 98 81 [97] 46 29 85` — "81 97 que"
- @288 (a2_03): `89 28 00 [97] 09 64 29` — "pour 97"
- @299 (a2_04): `11 78 40 [97] 86 91 18` — "e 97 86" (clause-b window)
- @525 (a3_00): `06 55 81 [97] 47 44 59` — "81 97 ce"
- @566 (a3_02): `43 24 80 [97] 13 76 45` — "80 97"
- @588 (a3_02): `18 14 00 [97] 41 41 09` — "pour 97"
- @751 (a5_03): `64 02 [97] 40 67 11` — "02 97 e" (left edge: `00 64 02`)
- @1412 (a7_07): `52 42 16 [97] 69 74 34` — "16 97"
- @1823 (a8_11): `09 19 00 [97] 00 86 29` — "pour 97 pour 86er"

Predecessors: 00='pour' x4 (@2, @288, @588, @1823); 81 x2 (@94, @525);
40/80/02/16 x1 each. Successors: 10 distinct singletons
(51, 46='que', 09, 86, 47='ce', 13, 41, 40='e', 69, 00).
Census matches the bar's census exactly. No 97 battery exists in any crowd
inbox; no red-team ruling names 97's value, class, or frame.

## Frame-legs: 97 is infinitive-class

Standing values used (all granted/banked, none provisional):
00='pour' (A9), 46='que' (banked), 47='ce' (A4), 40='e' (pencil),
80 verb-frame (A8), 86 INF-class (A9, class-level), 17='fois' (promoted).

- L1–L4: "pour 97" @2, @288, @588, @1823. 00='pour' is granted (A9).
  97 sits in 00's infinitive-taking slot (00->86 x12, 00->33 x8),
  mirroring 86's own 'pour'+86 x12 pattern (noted in battery-ver78-296-reparse).
- Article discriminator (lane-internal): 00's nominal takes surface the
  article — 00->11 x4 = "pour la fois" @1287, "pour la [95] que" @1405,
  and two more. Bare "pour 97" x4 never takes an article, so 97 is not a
  determiner phrase. Finite verb is excluded ("pour"+finite is ungrammatical;
  no polyvalence rescue per §7, 67 sole).
- L5: @1823 "pour 97 pour 86er". Two "pour X" phrases in parallel position.
  86 is INF-class (A9) and here carries 'er' (86->29 x4), i.e. infinitive
  form. Parallel "pour X pour Y" phrases take the same class: 97 is an
  infinitive.
- L6: @94 "97 que" (46='que' banked). Que-valency infinitive. Direct
  precedent: 33-46 x2 "dire que" (A10 que-taking infinitives).
- L7: @566 "80 97". 80 is a granted verb-frame (A8, verb-locked).
  "[V] [INF]" adjacency (modal/causative + infinitive) is the natural read.

Rivals:
- Finite verb: killed by L1–L4 ("pour"+finite ungrammatical).
- Noun: zero positive legs anywhere in the 10 windows. It is merely
  compatible with each window ("pour [N]" bare, "[N] que" relative,
  "[V] [N]" object), never demonstrated, never cleaner. No kill.

Seven frame-legs over six distinct windows name the class INFINITIVE.
Zero contradictions in all 10 windows. Value is NOT named (class-level
claim only).

## Clause (b): 97-86 @299 fenced with stated cause

Window: `11 78 40 [97] 86 91 18` ("la [78] e 97 86 ...").
- The bigram 97-86 occurs exactly once in 1,847 pairs (re-derived;
  86-97 occurs x0). Confirmed hapax; no joint-frame precedent exists.
- 97's 10 successors are all distinct, so the single contact carries no
  frame weight. It is distributionally inert.
- Neighbors force no contradiction: 11='la' banked, 78 open ('ver' is a
  LEAD, not granted), 40='e' pencil, 91/18 open.
- Pair-level word-boundary underdetermination: "[whole-INF] [INF]" across a
  clause boundary (asyndeton; cf. R17-012, 86 has substantivized uses) vs
  word-internal composition — the pair cipher cannot decide.
- The class evidence (L1–L7) uses none of @299's pairs, so the contact is
  independent of the class claim either way.

Stated cause for the fence: hapax + full successor dispersion + boundary
underdetermination + independence from the class evidence. The contact is
recorded, not ignored.

## Per-clause verdict

1. Class named with >=3 frame-legs: PASS. Class = infinitive. Seven legs
   (L1–L7) over six windows; finite-verb rival killed; noun rival
   undemonstrated.
2. 97-86 @299 explained or fenced: PASS (fenced with stated cause above).

## Adverses answered

- n=10 (thin): answered. Census re-derived exhaustive on the repaired
  stream (indices match the bar exactly). Seven frame-legs, zero
  contradictions. Thinness is recorded as a precision caveat: the claim is
  class-level only; 97's value stays open and unnamed.
- 81's value open: answered. The 81-97 x2 legs (@94, @525) are not used to
  name the class; they are consistent-but-neutral. 81's own profile
  (pre: 55 x6, 77 x4; suc: 00 x3, 97 x2, 87 x2) forces no incompatible
  value: 81='prin' is KILLED, noun-81 is a queued hypothesis (not granted),
  77='le' is provisional-only. Fenced with cause, not ignored.
- 97-86 bigram is a hapax: answered via the clause-(b) fence above.

## Verdict: PROMOTE (class-level)

97 is infinitive-class. Class-level grant; value open, not named.
No standing red-team verdict is contradicted (no A-series ruling names 97;
§7 kills/splits/polyvalence untouched; A9/A10/A14 holdings used, not altered).

## Unlock note

The gated target ver78-296-97gate depends on this AND on stem-86 naming
97/86 VALUES. This verdict names 97's class only, so that gate stays gated
until stem-86 (still queued) runs.
