# Battery ne-particle-ungrammatical-sweep

Target: `ne-particle-ungrammatical-sweep`. Priority 2. No adverses.
Evidence: battery-qui-94-syllabic-rival.md follow-up #2.

## Bar (verbatim)

produce the syllabic-vs-particle map for the red-team duality adjudication (94-87 "ne ce" known, 94-64 "ne qui" here)

## Bar restated as numbered clauses

- C1: census all 37 94-windows on the repaired stream; for each follower, state
  whether particle "ne" + follower is grammatical in 1841 French, ungrammatical
  (forcing the syllabic/word-final reading), strained, or conditional on an open
  value. Deliver the map. PASS/FAIL.

## Method

Re-derived the repaired 1,847-pair stream independently from
`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`
(upstream tokenization, byte-exact; `canonical.py` never used; R5005, sealed
gates, red-team queue untouched). Verified 1,847 pairs / 96 types; 94 occurs
37x, all 37 with a follower. @-offsets are 0-based pair indices.

Particle test: "ne" is grammatical iff followed (possibly across clitics
le/la/les/lui/leur/se/me/te/nous/vous/y/en) by a finite verb, "ne ... pas/
plus/jamais/que" frame, or elided "n'" + vowel-initial verb ("n'est"). It is
ungrammatical before: nouns, determiners, "qui" (relative), "ce"
(demonstrative), subject pronouns ("on"), adverbs in preverbal position
("tout"). "ne me X" needs a verb after the clitic; doubled verb endings with
no stem are strained (per red-team R17-001).

## The map (37 windows)

### A. PARTICLE-COMPATIBLE (8)

| @ | row | frame | reading |
|---|---|-------|---------|
| 161 | a1_05 | 94 24 87 11 | "ne [verb] ce la" — 24=verb class (granted) |
| 558 | a3_02 | 94 59 30 67 | "n'est pas" — canonical, elided; cf. R17-004 |
| 762 | a5_03 | 94 59 39 88 | "n'est [39] [88]" — elided |
| 1701 | a8_06 | 94 30 20 62 | "ne pas [20] [62]" — 30="pas" promoted |
| 1705 | a8_06 | 94 88 26 12 | "ne [88]" — 88 verb/governor frame (A8) |
| 1713 | a8_06 | 94 44 59 30 | "ne [44] est pas" — cf. R17-004 leg |
| 1773 | a8_09 | 94 24 87 64 | "ne [verb] ce qui" — 24=verb, 64="qui" GT |
| 1795 | a8_09 | 94 59 37 91 | "n'est [37]" — elided |

### B. PARTICLE-UNGRAMMATICAL → syllabic/word-final forced (9)

| @ | row | frame | reason |
|---|---|-------|--------|
| 250 | a2_02 | 94 65 63 00 | "ne [noun]" — 65 noun-class (battery-promoted; conditional on that standing) |
| 509 | a3_00 | 94 64 98 65 | "ne qui" — 64="qui" GT; the bar's headline case |
| 651 | a4_02 | 94 76 49 24 | "ne [noun]" — 76 masculine noun (battery-promoted; conditional) |
| 841 | a5_06 | 94 26 12 16 | "ne [noun]" — 26 noun lead (battery-level; conditional) |
| 1169 | a6_09 | 94 87 83 21 | "ne ce" — 87="ce" granted; the bar's known case |
| 1363 | a7_06 | 94 79 14 60 | "ne tout" — preverbal "tout" ungrammatical; no French word "netout" either (residual) |
| 1687 | a8_05 | 94 79 14 60 | same frame as @1363 ("62 94 79 14 60" x2) |
| 1576 | a8_01 | 94 76 47 98 | "ne [noun]" — 76 masculine noun (conditional, as @651) |
| 1664 | a8_04 | 94 84 64 06 | "ne on" — subject pronoun must precede "ne" ("on ne"); no "neon" word (residual) |

### C. PARTICLE-STRAINED (4)

| @ | row | frame | reason |
|---|---|-------|--------|
| 578 | a3_02 | 94 82 06 06 | "ne m'ent-ent" — doubled 06, no stem; cf. R17-001 "ne-me legs strained" |
| 1182 | a6_10 | 94 82 06 06 | same as @578 |
| 1353 | a7_05 | 94 82 06 52 | "ne m'ent [52]" — single 06, still stemless |
| 1742 | a8_07 | 94 82 46 56 | "ne m que" — 46="que" GT; "ne ... que" needs a verb between clitic and "que" |

### D. AMBIGUOUS — conditional on open values (16)

| @ | row | frame | condition |
|---|---|-------|-----------|
| 65 | a1_01 | 94 92 69 13 | 92's value (verb reading conditional on 83="de" lead) |
| 101 | a1_02 | 94 93 59 45 | 93's value |
| 318 | a2_04 | 94 06 11 92 | "ne en la [92]" — clitic order "en la" wrong; syllabic lean, not forced |
| 349 | a2_05 | 94 74 67 78 | 74's value |
| 494 | a2_11 | 94 02 79 88 | 02's value |
| 570 | a3_02 | 94 52 87 78 | 52's value; cf. @1736 "12 48 52" = "n e [52]" letter spelling |
| 688 | a5_00 | 94 29 60 03 | "n'erre" possible — 29="er" GT word-initial attested ("n'erre"); needs 60 to complete |
| 699 | a5_01 | 94 60 12 98 | 60 verbal (poly-60: verbal forced, no single value) |
| 771 | a5_03 | 94 07 06 94 | 07's value |
| 774 | a5_04 | 94 15 33 73 | 15's value |
| 785 | a5_04 | 94 74 65 84 | 74's value |
| 1102 | a6_06 | 94 74 47 78 | 74's value |
| 1293 | a7_03 | 94 52 80 04 | 52's value |
| 1330 | a7_04 | 94 70 52 39 | "ne pre[52]" — 70="pre" GT; "ne prenne" possible if 52 completes a verb |
| 1549 | a8_00 | 94 92 45 23 | 92's value (as @65); 45="ce" hold (A11) |
| 1806 | a8_10 | 94 52 80 04 | 52's value |

Counts: 8 + 9 + 4 + 16 = 37. All windows classified.

## Per-clause result

- C1: PASS — the full 37-window syllabic-vs-particle map is delivered above.

## Verdict

**PROMOTE (evidence-package grade).** The bar is fully met: the complete map is
produced with byte-exact @-offsets on the repaired stream, and there are no
adverses. Scope is explicit: this is an evidence package for the red-team 94
duality adjudication, not a value claim about 94. It does not promote 94="ne"
globally and does not contradict any standing red-team grading (R16-006's
decline of the 94="ne" promote is untouched; the B-group windows are new
byte evidence for the syllabic side, the A-group for the particle side).

Notes for the red team:
- The B-group includes the bar's two named cases (@1169 "ne ce", @509 "ne qui")
  plus seven more forced-syllabic windows, three of which load on battery-level
  (not yet ratified) standings (@250 on 65 noun-class, @651/@1576 on 76 noun,
  @841 on 26 noun lead) — flagged as conditional.
- The C-group ("ne m" + 06) matches R17-001's "strained" grading; no window
  shows a clean "ne me [verb]".
- Residuals with no good reading on either side: @1363/@1687 ("ne tout"),
  @1664 ("ne on") — ungrammatical as particle, no French word as syllabic.
- §7 intact: no polyvalence declared at battery level; the duality question
  stays with the red team.

## Bookkeeping

Lock created 2026-10-09T03:09:34Z, deleted on completion. `battery-queue.json`
updated via temp-file + rename (pre-write assert: status queued, no verdict).
