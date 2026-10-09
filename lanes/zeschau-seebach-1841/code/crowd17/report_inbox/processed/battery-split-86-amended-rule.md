# Battery verdict: split-86-amended-rule — amended positional rule for 86

Date: 2026-10-08. Worker: 8abd8610-865b-4c84-ba68-7ba8f8c80ba7.

## Bar (verbatim from battery-queue.json)

"promote the amended rule iff it is exceptionless over all 32 windows and every non-conforming window is fenced with byte-level cause (no bare 'adverse' fences)"

Listed adverses: "coordinate with reseg-86-553-889; declaring the split is a red-team act (section 7), battery escalates only"

### Numbered clauses (operative)

1. The amended rule is exceptionless over all 32 windows: every 86-window is
   assigned a life with no leftover.
2. Every window non-conforming to the ORIGINAL rule (@553, @889) is fenced
   with byte-level cause. No bare "adverse" fences.

### The amended rule under test

86 = determiner-life iff follower in D =
{56,50,01,52,66,70,78,48,44,24,20,67,71,12,21,91,94,16,96};
86 = verb-adjacent life iff follower in V = {29,59,06}
(29=er banked, 06=ent granted, 59=est provisional — all verb-valued under
lane-granted values).

## Method

Parsed the repaired 1,847-pair stream exactly per
code/side-keyhunt/repair_parse.py (repaired_offsets.json +
data/upstream-ct_R5005.txt). Never used canonical.py. Never touched R5005,
sealed gate instances, or the red-team adjudication queue. Re-derived all
32 86-windows, follower census, predecessor census, bigram/trigram counts,
row positions, and same-row neighbor windows on bytes. No prior counts
trusted. @-offsets match battery-homophone-86-split exactly (32/32).

## Window-level evidence (all 32, @-offsets on repaired stream)

Notation: L1 [86] R1 R2; D = determiner-life, V = verb-adjacent life.

DETERMINER-LIFE (D), n=26:
- #0 @175 (a1_05): 87 [86] 21 69 — R1=21
- #1 @300 (a2_04): 97 [86] 91 18 — R1=91
- #4 @557 (a3_01): 17 [86] 94 59 — R1=94
- #5 @661 (a4_02): 00 [86] 50 80 — R1=50
- #6 @671 (a5_00): 11 [86] 24 80 — R1=24
- #7 @716 (a5_01): 66 [86] 01 02 — R1=01
- #8 @728 (a5_02): 00 [86] 48 88 — R1=48
- #9 @799 (a5_04): 77 [86] 44 74 — R1=44
- #10 @867 (a5_07): 00 [86] 70 87 — R1=70
- #11 @878 (a5_08): 77 [86] 78 17 — R1=78
- #13 @899 (a5_08): 83 [86] 16 92 — R1=16
- #14 @948 (a6_00): 96 [86] 01 77 — R1=01
- #15 @951 (a6_00): 77 [86] 96 87 — R1=96
- #16 @962 (a6_00): 00 [86] 56 41 — R1=56
- #17 @1002 (a6_02): 00 [86] 56 47 — R1=56
- #18 @1099 (a6_06): 67 [86] 52 82 — R1=52
- #19 @1128 (a6_07): 00 [86] 52 37 — R1=52
- #20 @1131 (a6_07): 37 [86] 24 77 — R1=24
- #21 @1134 (a6_08): 77 [86] 20 62 — R1=20
- #22 @1147 (a6_08): 98 [86] 67 33 — R1=67
- #23 @1335 (a7_05): 83 [86] 71 64 — R1=71
- #24 @1345 (a7_05): 47 [86] 66 73 — R1=66
- #27 @1458 (a7_09): 67 [86] 66 79 — R1=66
- #28 @1506 (a7_11): 00 [86] 56 41 — R1=56
- #29 @1739 (a8_07): 52 [86] 12 34 — R1=12
- #30 @1792 (a8_09): 00 [86] 56 42 — R1=56

VERB-ADJACENT LIFE (V), n=6:
- #2 @431 (a2_09): 77 [86] 29 82 — R1=29 (er, banked)
- #25 @1375 (a7_06): 00 [86] 29 89 — R1=29
- #26 @1391 (a7_07): 67 [86] 29 89 — R1=29
- #31 @1825 (a8_11): 00 [86] 29 82 — R1=29
- #3 @553 (a3_01): 00 [86] 59 34 — R1=59 (est, provisional)
- #12 @889 (a5_08): 00 [86] 06 77 — R1=06 (ent, granted)

Follower census (re-derived): 01:2, 06:1, 12:1, 16:1, 20:1, 21:1, 24:2,
29:4, 44:1, 48:1, 50:1, 52:2, 56:4, 59:1, 66:2, 67:1, 70:1, 71:1, 78:1,
91:1, 94:1, 96:1 — 22 distinct, n=32. Coverage: 26 D + 6 V = 32/32.

## Byte-level fences (the two original-rule violators)

### Fence F1 — #3 @553, row a3_01 (raw "2632160824821691124429484206004624474655810086593417862", offset 0)

1. Bigram "86 59" is a stream singleton (1 of 1,846 bigrams). Trigram
   "86 59 34" is a singleton. The anomaly is confined to these bytes;
   no systemic "86 takes est" pattern exists.
2. Same row holds a second 86 at @557 (4 pairs later, "17 [86] 94 59")
   with conforming follower 94. The deviation is slot-local to #3,
   not row-systemic.
3. Left context "00 86" occurs 12x stream-wide with followers
   56x4, 29x2, 50, 48, 70, 52, 59, 06 — 11 of 12 conform. The deviation
   is right-local to the follower slot.
4. Row position 22 (mid-row). No row-edge byte signature.
5. Follower 59 is verb-valued (est, provisional). Under the amended rule
   this window is V-life, not a violation.

### Fence F2 — #12 @889, row a5_08 (raw "77449167786781708317968370302008606777601988214988386", offset 1)

1. Bigram "86 06" is a stream singleton. Trigram "86 06 77" is a singleton.
2. Same row holds conforming 86s at @878 (follower 78, 11 pairs before)
   and @899 (follower 16, 10 pairs after). The violator is sandwiched
   between two conforming windows — deviation confined to one slot.
3. Same "00 86" conforming left context as F1 (see above).
4. Row position 15 (mid-row). No row-edge byte signature.
5. Follower 06 is verb-valued (ent, granted). Under the amended rule this
   window is V-life, not a violation.

Note: F1 and F2 are fenced, not resolved. The standing adverses they
coincide with (@552/@553, @888) keep their standing — the amended rule
assigns these windows to V-life, so the determiner-reading tension those
adverses record does not contradict the rule.

## Third-life candidacy branch: NOT SUPPORTED

Bytes do not support {59,06} as a third life distinct from the 29-class:
- Both windows share predecessor 00 with four conforming "00 86" windows
  (29 x2, 50, 48). No predecessor separation.
- n=2 windows total. Any distributional test is underdetermined.
- 59=est is provisional; the pair {59,06} (finite verb, verbal ending)
  has no byte-level binding beyond verb-valuedness, which it shares with 29.
Recorded as an open question for reseg-86-553-889, not a candidacy.

## Per-clause results

### Clause 1 (amended rule exceptionless over 32): PASS

26 D + 6 V = 32/32. Every window assigned. Mutual exclusivity holds:
no D-window takes a V follower; no V-window takes a D follower.
Caveat: the V-class label rests on lane-granted values, and 59=est is
provisional — if 59's value is revised, the class label weakens, but the
byte facts (singleton bigrams, same-row conforming neighbors) stand.

### Clause 2 (byte-level fences for both violators): PASS

F1 and F2 each cite stream-singleton bigrams/trigrams, same-row
conforming 86 neighbors, the shared conforming "00 86" left context,
mid-row positions, and value-grounded class membership. No bare
"adverse" fences.

## Adverses

- reseg-86-553-889 coordination: sibling has no lockfile and no report on
  disk at this run's dispatch time — did not block on it. If reseg
  demonstrates a cleaner multi-group parse for either window, these fences
  must be re-audited (the byte facts recorded here make that audit cheap).
- §7 respected: no polyvalence is declared. The battery promotes the
  amended RULE (test artifact); declaring the split is a red-team act and
  stays escalated.

## Verdict: PROMOTE (battery level)

The amended rule is exceptionless over all 32 windows and both
original-rule violators are fenced with byte-level cause. Third-life
candidacy is not supported. Declaration of the split remains a red-team
act per §7.

## Follow-ups (promote, so no null-regeneration needed)

1. `redteam-86-split-docket` — already queued by battery-homophone-86-split:
   package this amended rule (32/32 table, F1/F2 fences, z=-1.72 runs test,
   third-life rejection) for red-team adjudication. Declaration is theirs.
2. If reseg-86-553-889 returns a cleaner multi-group parse for @553 or
   @889, re-audit this promotion's fences against the new segmentation.
3. If 59=est is revised, re-audit the V-class label (fence F1 keeps its
   byte facts regardless).

R5005, sealed gate instances, and the red-team adjudication queue were not
touched. No standing verdict was contradicted or downgraded.
