# Battery report — doublet-41-589

Target: `doublet-41-589` (priority 3)
Date: 2026-10-09
Worker: 4b4d53bb-2717-4c99-a2a9-638a1cc15482 (session 2022d7ab-416a-4e66-bd09-f51b2c2f577c)

## Claim (from queue)

resolve the "41 41" adjacency at @589–590 (doubled word, geminate boundary, or syllable doubling)

## Bar (verbatim, from queue)

use the '00=pour 97 ... 09 00=pour' frame; feeds split-41-redteam

## Bar as numbered clauses (pre-registered before testing)

- C1: The frame is byte-exact in the repaired stream: @587..592 reads
  "00 97 41 41 09 00", with the row break falling between @589 and @590.
- C2: H1 (doubled word) — the frame admits "41 41" as two tokens of one
  word; tested via in-text word-doubling precedent and the tier of the
  "00 97 X" slot.
- C3: H2 (geminate boundary) — a word boundary falls between @589 and
  @590 with gemination across it; tested via boundary forcing at
  589|590 and cross-word gemination precedent/mechanism.
- C4: H3 (syllable doubling) — "41 41" is a word-internal geminate (one
  reduplicated-syllable word); tested via in-text geminate precedents
  and 41's sub-word behavior elsewhere.
- C5: A frame-level resolution is delivered that feeds split-41-redteam
  without deciding the docket item.

## Method

Re-derived the repaired 1,847-pair / 96-type stream in-session from
`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`,
parsed exactly like `code/side-keyhunt/repair_parse.py` (asserts held:
1847 pairs, 96 types; 0-based @-offsets). `canonical.py` never used.
R5005, sealed gate instances, and the red-team adjudication queue
untouched. No invented numbers: every count below is from the stream.

Adopted premises (not re-litigated): protocol §7 standings
(00="pour" granted A9 leg-1 class-level; 11="la", 17="fois", 47="ce",
64="qui", 79="tout", 84="on", 87="ce", 96="par" granted; 06="ent"
bound ending promoted; 09/92 "-ère" value killed; 67 sole true
polyvalence); `battery-wordinternal-41-census` NULL (19 windows of 41
re-verified in-stream; its "no immediate letter-cell neighbor" line is
corrected below to 2/19 — @39 "64=qui 41", @237 "41 17=fois");
`battery-41-05-class` PROMOTE (41 composes leftward with 06="ent" at
@5, i.e. 41 can be sub-word/stem); `battery-41-808-role` PROMOTE (41
standalone-word at @808); @237 determiner arm PROMOTE. 41's split
candidacy is red-team venue (`split-41-redteam`) — untouched here.

## Window-level evidence (byte-exact, 0-based)

### The frame

@583..596 = `10 19 18 14 | 00 97 41 41 09 00 | 92 79 85 01`
(rows: @583–589 = a3_02, @590–596 = a4_00).

- @587=00 ("pour"), @588=97, @589=41, @590=41, @591=09, @592=00 ("pour").
- The row break falls exactly between the two 41s: @589 is the last
  pair of row a3_02 (offset 31 of 32), @590 the first pair of row a4_00.
- "97 41" (@588) and "41 09" (@590) are hapax bigrams — their only
  stream occurrences are inside this frame. "41 97" = 0, "09 41" = 0.

### The "00 97 X" slot (all 4 frames)

| @ | frame | X |
|---|---|---|
| 1 | 09 00 97 51 47=ce 41 06=ent 77=le | 51 |
| 287 | 00 97 09 64=qui 29=er 40=e | 09 |
| 587 | 00 97 41 41 09 00=pour 92 | 41 41 (doubled — only one) |
| 1822 | 09 19 00 97 00 86 29=er 82=m | 00 |

X-slot occupants 51 / 09 / 00 are word-tier cells: 09 (n=12) has
7/24 neighbor-slots on granted word cells and precedes 87="ce",
70="pre", 64="qui", 11="la", 00="pour" (×2); 51 (n=6) precedes
47="ce", 70="pre"; 00="pour" granted. The slot after "00 97" is a
word-tier slot in all 4 frames.

97 (n=10): follows 00=pour 4× (@1, @287, @587, @1822); precedes
46="que" (@94), 47="ce" (@525), 51, 09, 86. Word-tier.

### Self-adjacency census (all "X X" in 1847 pairs: 14 total, 6 values)

| @ | cells | rows | straddles row break |
|---|---|---|---|
| 417 | 74 74 | a2_08/a2_08 | no |
| 580 | 06 06 | a3_02/a3_02 | no — ctx "82=m 06 06" = "mentent" |
| 589 | 41 41 | a3_02/a4_00 | YES |
| 806 | 24 24 | a5_05/a5_05 | no |
| 816 | 74 74 | a5_05/a5_05 | no — ctx "49 74 74 47=ce" |
| 861 | 74 74 | a5_07/a5_07 | no — ctx "49 74 74 48" |
| 919 | 74 74 | a5_09/a5_09 | no — ctx "49 74 74 40=e" |
| 1053 | 74 74 | a6_04/a6_04 | no — ctx "29=er 40=e 29=er 74 74 45" |
| 1073 | 98 98 | a6_05/a6_05 | no — ctx "42 98 98 12" |
| 1145 | 98 98 | a6_08/a6_08 | no — ctx "42 98 98 86" |
| 1184 | 06 06 | a6_10/a6_10 | no — ctx "82=m 06 06" = "mentent" |
| 1523 | 11 11 | a7_11/a7_11 | no — 11="la" granted: "la la" |
| 1637 | 74 74 | a8_03/a8_04 | YES — ctx "01 74 87 74 74 35" |
| 1660 | 98 98 | a8_04/a8_04 | no — ctx "47=ce 98 98 80" |

Precedents:
- Word-doubling: "11 11" @1523–1524 (11="la" granted) — word-tier
  doubling happens in this text.
- Word-internal/morpheme geminates: "82 06 06" ×2 ("mentent":
  stem-final "ent" + inflectional "-ent"); "49 74 74" ×4
  (stereotyped: left context fixed at 49, right ∈ {46="que",
  47="ce", 48, 40="e"}); "42 98 98" ×2 (right neighbors include
  82="m"). 74 (n=34) and 98 (n=40) are productive geminate cells.
- 41's doubling is NOT stereotyped: single occurrence, unique frame,
  no letter-cell anchor (unlike "82 06 06", "98 98 82",
  "74 74 40=e"). 41's GT letter/syllable neighbor rate is 2/19
  (@39: 64="qui" left; @237: 17="fois" right) vs 06: 18/44,
  98: 11/40, 74: 6/34, 11: 12/45, 24: 14/52.

### Row-break controls

- 70 rows, 69 breaks. Row starts carry a clause/PP/DP starter
  ({00,47,64,96,84}) at rate 0.072 vs baseline 0.095 — row breaks do
  NOT align with word boundaries. The 589|590 straddle is therefore
  uninformative about boundary placement.
- Line-start == previous line-end: 2/69 (@589: 41|41; @1637: 74|74)
  vs ~0.72 expected at 1/96 chance (binomial p≈0.17, not significant).
  Scribal line-break dittography is NOT established as a process;
  both straddles are consistent with chance.

### Frame rarity

"00 ... 00" gaps ≤5 cells: 4/54 gaps — (185,188): "00 33 16 00";
(1244,1247): "00 33 16 00" (exact repeat); (1822,1824): "00 97 00";
(587,592): ours, the longest (gap 5) and the only one containing a
doubled cell. "09 00" occurs 2× (@0 stream-start, @591).

## Per-clause pass/fail

- C1 (frame byte-exact): PASS. @587..592 = "00 97 41 41 09 00";
  row break between @589 (a3_02 end) and @590 (a4_00 start).
- C2 (H1 doubled word): INCONCLUSIVE — admissible, not forced. FOR:
  in-text precedent "11 11" ("la la", granted word doubled); the
  "00 97 X" slot is word-tier in all 4 frames, so "41 41" as two
  word-cells fits the slot; 41-as-word is established at @808/@237/@5
  (split candidacy). AGAINST/NOT-FORCED: no French doubled-word
  construction is forced by "pour 97 W W 09"; "97 41"/"41 09" hapax.
- C3 (H2 geminate boundary): FAIL — fenced at frame level. No boundary
  is forced between @589/@590 (row-break straddle uninformative per
  the alignment control); no in-text precedent for cross-word
  gemination ("06 06" is word-internal "mentent"; "11 11" is
  same-word doubling); French has no productive cross-word geminate
  mechanism. A "41|41" word-boundary geminate has no mechanism and no
  forcing here.
- C4 (H3 syllable doubling): INCONCLUSIVE — admissible, not forced.
  FOR: productive in-text geminates ("82 06 06"×2, "49 74 74"×4,
  "42 98 98"×2); 41 is sub-word/stem at @5 (41+06="ent"); "pour 97
  [reduplicated-syllable word] 09" (e.g. "papa"-type "S S") is
  ordinary French syntax. AGAINST/NOT-FORCED: 41's doubling is
  unstereotyped (single, unique frame, no letter-cell anchor);
  41's letter-neighbor rate (2/19) is the lowest of the doubler cells.
- C5 (frame-level resolution feeding the docket, docket not decided):
  PASS — this report.

## Verdict

**NULL** — H2 (geminate boundary) is fenced at frame level, but the
frame does not discriminate between H1 (doubled word) and H3
(syllable doubling): both have in-text precedent and both fit the
word-tier "00 97 X" slot. The "41 41" adjacency at @589–590 remains
unresolved between those two; the split-41-redteam docket item is not
decided here.

## Follow-ups (per §4)

1. `doublet-589-97-role` — pin 97's class from its 10 windows (follows
   00="pour" 4×; precedes 46="que", 47="ce", 51, 09, 86). If 97 heads
   the pour-complement, "41 41 09" follows the head, constraining the
   H1/H3 parse geometry. Pass iff ≥2 independent legs name one class
   (verb/noun/other) with zero kill-grade contradictions; feeds the
   doublet resolution.
2. `doublet-589-09-role` — pin 09's class from its 12 windows
   (precedes 87="ce", 70="pre", 64="qui", 11="la", 00="pour" ×2;
   follows 84="on" ×2). Determines whether the frame re-parses as
   "pour 97 41 41 | 09 pour 92" with 09 heading the second pour's
   left edge. Pass iff ≥2 independent legs name one class; fence iff
   unclassifiable.
3. `linebreak-repeat-audit` — test the scribal-dittography rival:
   rate of line-start == previous line-end across all 69 row breaks
   vs 1/96 chance (binomial, lane standard), including the
   line-start == line-end-minus-1 variant. Both straddling doublets
   (@589, @1637) fit the pattern; current count 2/69 (p≈0.17) does
   not establish it. Pass iff enriched → reclassify both as
   candidate scribal repeats; fail → fence dittography for both.

## Bookkeeping

- Lock: `code/crowd17/next-token/locks/doublet-41-589.lock` created at
  start (agent id + 2026-10-09T17:20:42Z); no stale lock present.
  Deleted on completion per §6.
- Report: `code/crowd17/report_inbox/battery-doublet-41-589.md`.
- Queue: target `doublet-41-589` set to status `verdict` (NULL) —
  own-entry-only temp-file+rename write, pre-write assert
  queued/verdictless, JSON re-validated after write.
- No red-team docket item touched; no R5005/sealed-gate contact.
