# Battery report: split-60-verbs

- Target id: `split-60-verbs`
- Claim: distributional split test — bare-60 verb (V1–V4) vs ent-60 verb (V5–V6) as two items sharing syllable 60
- Date: 2026-10-09
- Worker: battery worker (subagent 4e8fc514-57a4-402d-acb3-aa246e234a33)
- Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` +
  `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`;
  asserted 1,847 pairs / 96 types in-session). `canonical.py` never used. R5005,
  sealed gates, and the red-team adjudication queue untouched.
- Lock: `code/crowd17/next-token/locks/split-60-verbs.lock` (created at start,
  deleted on completion; no prior lock existed).

## Bar (verbatim, pre-registered before testing)

"split iff the predecessor/successor selectional profiles of 60 in {V1–V4} vs
{V5–V6} frames are distinguishable per the {33,86} split precedent (adapted);
merge iff indistinguishable"

Numbered pass/fail clause (fixed before data examination):

1. (C1) The predecessor and successor selectional profiles of 60 in the
   {V1–V4} frames vs the {V5–V6} frames are distinguishable per the adapted
   {33,86} criterion: the {33,86} stem-class-split precedent splits iff the
   governor (predecessor) sets are disjoint and the complement (successor) sets
   overlap only at a small shared set (there: [89]/m[16]). If distinguishable
   → split; if indistinguishable → merge.

Window definitions adopted from `battery-verb-60` (2026-10-08, null), all
re-verified on the repaired stream this run:
- V1 @1338 (row a7_05): `71 64 60 08 65` = '[71] qui[64] [60] [08] [65]'
- V2 @700 (row a5_01): `94 60 12 98` = 'ne[94] [60] n[12] [98]'
- V3 @995 (row a6_01): `03 60 67 11` = '[03] [60] et[67] la[11]'
- V4 @1474 (row a7_10): `53 60 06 67` = '[53] [60] ent[06] [67]'
- V5 @1563 (row a8_01): `06 60 71 50` = 'ent[06] [60] [71] [50]'
- V6 @1735 (row a8_07): `06 60 12 48` = 'ent[06] [60] n[12] e[48]'

Adverses (answered in §Adverses below): "n small (4 vs 2 windows) —
underpowered, grade accordingly; a split is two items, not polyvalence, so
§7 does not block the test".

## Method

1. Re-derived the repaired stream in-session; asserted 1,847 pairs / 96 types.
2. Verified all six windows byte-exactly (predecessor/successor pairs match
   battery-verb-60 exactly).
3. Ran the full 60 census (n=18): @119, @172, @197, @232, @322, @454, @637,
   @690, @700, @995, @1338, @1366, @1474, @1563, @1644, @1674, @1690, @1735.
4. Computed predecessor/successor sets for group A {V1–V4} and group B
   {V5–V6}; computed stream-wide bigram counts for '06 60', '60 06', and the
   trigram '06 60 06'.
5. Stress-tested against row-offset uncertainty: re-paired rows a7_05 and a7_10
   under their offset-1 flips and checked whether the V1/V4 windows survive
   (phase evidence: a7_05 at −0.85 nats rival-favored; a7_10 offset-1
   battery-grade constraint-clean per the reseg battery).

## Window-level evidence (canonical stream)

Predecessor sets:
- Group A (bare-60): V1←64, V2←94, V3←03, V4←53 → {64, 94, 03, 53}
- Group B (ent-60): V5←06, V6←06 → {06}

Successor sets:
- Group A: V1→08, V2→12, V3→67, V4→06 → {08, 12, 67, 06}
- Group B: V5→71, V6→12 → {71, 12}

Criterion check (adapted {33,86} stem-class-split):
- Predecessor sets DISJOINT: {64,94,03,53} ∩ {06} = ∅. Group B's predecessor
  is exclusively 06='ent' (promoted verb ending), 2/2 windows; group A's are
  verb-forcing/granted frames (64='qui' granted, 94='ne' battery-promoted)
  plus NP/verb-compatible frames (03, 53).
- Successor sets overlap at exactly ONE point: {12} ('n', promoted letter).
  V2 'ne [60]n' (stem-final letter) and V6 'ent[60]ne' (letter inside the
  ent-word) select the same letter — shared-syllable material, neutral to the
  test, exactly the "small shared set" the precedent allows.

Morphological partition (corroboration, full-census level):
- '06 60' bigram: x2 stream-wide, BOTH in group B (V5, V6). 'ent' is a PREFIX.
- '60 06' bigram: x1 stream-wide, ONLY in group A (V4). 'ent' is a SUFFIX.
- '06 60 06' trigram: x0 stream-wide. The ent-prefix and ent-suffix shapes
  never combine on one item.
- No single French verb has both "[X]ent" and "ent[X]" forms for one
  monosyllabic X (adopted from battery-verb-60's lexical sweep; [X]ent:
  "mentent"/"vendent"/"tendent"/"rendent"; ent[X]: "entre"/"entend"/"entonne";
  the X sets never coincide).

## Phase-stress check (stated caveat, not hidden)

- Row a7_05 (V1) under offset-1 re-pairs to
  `23 98 38 67 16 46 00 86 56 45 23 84 78 66 67 33 46 24 87 77 89 48 20 65 23 76 45`
  — the '71 64 60 08 65' window DISSOLVES (canonical-offset object).
- Row a7_10 (V4) under offset-1 re-pairs to
  `61 24 15 36 00 66 73 32 98 21 69 86 24 67 78 42 48 70 83 19 23 92 40 06 61 55 94`
  — the '53 60 06' window DISSOLVES (canonical-offset object).
- Reduced (phase-robust) group A = {V2, V3}: predecessors {94, 03},
  successors {12, 67}. Predecessor sets STILL disjoint ({94,03} vs {06});
  successor overlap STILL exactly {12}. The split pattern persists even after
  both phase-fragile windows are removed. The protocol's canonical stream is
  used for the verdict; this check bounds the downside.

## Per-clause pass/fail

1. (C1) PASS — the profiles are distinguishable per the adapted {33,86}
   criterion: predecessor sets disjoint, successor sets overlapping at
   exactly one point ({12}). Therefore: SPLIT, not merge. Two distinct
   verbal items share the syllable 60: a bare-60 verb (V1–V4) and an
   ent-60 verb (V5–V6).

## Adverses answered

- "n small (4 vs 2) — underpowered": graded accordingly. The finding is
  finding-grade (battery), not a strong distributional rejection; the
  reduced phase-robust group {V2,V3} vs {V5,V6} still splits, and the
  morphological impossibility argument ('06 60 06' x0; no verb with both
  [X]ent and ent[X]) carries the decisive weight. Recorded as
  finding-grade; red-team ratification required before banked use.
- "a split is two items, not polyvalence; §7 does not block": acknowledged
  and honored — this battery declares no polyvalence. Consistent with
  standing splits 20~17 and 23~26. The adjective-vs-verb question for 60 is
  already before the red team (poly-60-redteam, queued); this finding feeds
  it: the verbal side itself splits in two.
- Circularity note (not listed as an adverse, recorded honestly): the groups
  were defined by the ent prefix/suffix geometry, so predecessor
  disjointness is partly definitional. The independent signals are (a) the
  successor profiles (verb-endings {08,67,06} vs open {71}, overlapping at
  one letter), (b) the grammatical environments (verb-forcing qui/ne frames
  never co-occur with the ent-prefix), and (c) the morphological
  impossibility — none of which follow from the group definition alone.

## Standing-state check

- Consistent with `battery-verb-60` (null: one value could not cover all six;
  the bare/ent shape split proposed this target). Both naming follow-ups
  since returned null (`verb-60-bare`, `verb-60-ent`, 2026-10-09) — no value
  is nameable for either arm, which is consistent with, not contradictory
  to, this split finding.
- No standing red-team verdict contradicted or downgraded. §7 intact (no
  polyvalence declared).

## Verdict: PROMOTE (finding grade, battery-grade)

The distributional split holds: bare-60 verb (V1–V4) and ent-60 verb (V5–V6)
are two items sharing the syllable 60. Requires red-team ratification before
entering the banked map. No follow-ups proposed — the verb-naming follow-ups
(`verb-60-bare`, `verb-60-ent`) already ran to null; the value question stays
with `poly-60-redteam` (queued). If that docket resolves 60's verbal arm(s),
this split constrains it to two items.
