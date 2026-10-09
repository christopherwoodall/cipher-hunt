# Next-token findings: neque-instance-sweep (finder, wave 3)

- Beat: `neque-instance-sweep` (wave 3, was queued). Parent: battery-neque-bracket-verb-search NULL (2026-10-09).
- Finder: 36de584d-d65a-42ab-ada1-e2a24a835721. Date: 2026-10-09.
- Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json + data/upstream-ct_R5005.txt, parsed like code/side-keyhunt/repair_parse.py). canonical.py never touched. R5005 never touched. No numbers invented.
- Question from the brief: is the @1687 empty-slot anomaly a singleton, or part of a wider 94→79 adjacency pattern?

## Headline

NOT a singleton. The @1687 anomaly has an exact structural twin at @1363. Both windows open with the byte-identical 4-gram `94 79 14 60` and share the near-identical pre-context `13 {92|93} 62`. The string `79 14 60` occurs exactly twice stream-wide, and both times it stands directly after `13 {92|93} 62 94`. The @1687 empty-verb-slot is therefore one close of a repeated frame, not an isolated accident. The @1687 close is the short variant (4-pair interior); the @1363 close is the long variant (44-pair interior).

## Beat method, step by step

1. Extracted every 94 occurrence ±3 groups (37 instances) and every 94…46 window (nearest 46 before the next 94: 16 windows).
2. Clustered by follower pattern first. The six tight bracket windows (interior ≤ 8, no formula text) match the parent battery's census exactly.
3. Predicted plaintext from 1840s French diplomatic register under standing values.
4. Stated cipher-testable consequences; ranked battery targets by confidence × testability.
5. Respected §7 throughout: 94='ne' (battery-promoted, pending ratification) and 79='tout' (granted A5) used as given; 82='m', 46='que' banked; kills and holds not re-litigated.

## The six bracket windows (interior ≤ 8)

Follower-first clusters:

**79-cluster (the beat's target):**
- @1687 (a8_05): pre=[13 93 62] 94 79 14 60 27 46@1692 post=[24 85 58]. Interior 4.
- (twin, extended frame) @1363 (a7_06): pre=[13 92 62] 94 79 14 60 03 30 82 16 … 46@1408 post=[52 42 16]. Interior 44.

**82-cluster (same-group cluster = top target per beat method):**
- @1182 (a6_10): pre=[59 37 77 78] 94 82 06 06 59 42 06 84 59 46@1191 post=[07 24 82]. Interior 8.
- @1742 (a8_07): pre=[52 86 12 34] 94 82 46@1744 post=[56 40 06]. Interior 1.

**Singletons (one window each, no cluster):**
- @101 (a1_02): pre=[08 21 62] 94 93 59 45 28 00 46@107 post=[11 21 67]. Interior 5.
- @688 (a5_00): pre=[29 40 65] 94 29 60 03 39 74 46@694 post=[02 50 45]. Interior 5.
- @785 (a5_04): pre=[11 24 42] 94 74 65 84 06 77 64 46@792 post=[07 64 56]. Interior 6.

## Twin evidence (@1363 vs @1687)

- `94 79` direct adjacency occurs exactly twice stream-wide: @1363 and @1687. `79 14 60` occurs exactly twice stream-wide: @1364 and @1688 — both directly after `13 {92|93} 62 94`.
- Pre-contexts: `13 92 62 94` occurs exactly once stream-wide (@1360); `13 93 62 94` occurs exactly once (@1684). 92/93 differ by one group, and 09~92 is a standing hold — the pre-contexts are near-identical, not two random strings.
- Post-46 contexts differ (@1363: 52 42 16; @1687: 24 85 58), so the shared frame is the opening, not the tail.
- @1363's 44-pair interior is formula-contaminated: its last pairs are `87 11 00 11 95 46` (@1403–@1408), matching the cela-formula tail region (formula-tails finder T1). Per the beat method's de-duplication rule, @1363 counts as discriminating context for the frame, not as a second productive bracket instance.
- Nested-94 chain: @1353 opens `94 82 06 52 37 64 35 13 92 62` and runs into @1363's 94. So the @1363 twin is itself preceded by a `94 82` window — the 79-frame and the 82-frame touch at exactly one point stream-wide.

## Wider 94 context (all 37 94s)

- Follower distribution: 82 ×4 (@578, @1182, @1353, @1742 — top follower), 74 ×3, 59 ×3, 52 ×3, 79 ×2 (@1363, @1687), 92/24/76 ×2, rest singletons.
- One-gap pattern `94 X 79`: exactly one instance, @494 (`94 02 79`), a singleton — no wider pattern there.
- `79 94` direct adjacency: zero instances.
- Verdict on the brief's second question (does slot length predict which battery-available verb class fills the slot): no. In none of the six bracket windows is the position after 94 filled by a battery-available verb class (80/89 A8, 85 A3, 48-verb A7-L2, 37/32/42 A1). The followers are 79, 82, 93, 29, 74. Slot-length distribution (1, 4, 5, 5, 6, 8) does not map to any verb-class fill. This sub-question is a clean null: the 'ne…que' bracket never licenses a verb-class group adjacent to 94 in the tight-frame set.

## French register prediction

Under standing values the shared frame reads `ne tout [14] [60] … que`. In 1840s diplomatic French, `ne … que` = "only / nothing but". `tout [14]` is either a determiner phrase ("all [14] / every [14]", 14 = collective noun) or adverb + adjective ("entirely [14]"). Candidate shapes: "ne tout [14] [60] … que" = "not all of [14] [60] … that/but"; or restrictive "ne [tout [14] [60]] que" = "only all of [14] [60] …". 14 is unresolved (15/1847) and 60's NP-frame was closed out NULL by the parent battery — the complement stays open, as the parent found.

## Cipher-testable consequences

1. If the 79-frame is real, 14 and 60 must carry the same values at @1364–@1365 and @1688–@1689 (same frame position, same register role). Any 14/60 battery must pass on both windows or fail on both.
2. If the 82-frame is a licensed `94 82` ("ne m…") frame, the two tight brackets (@1182, @1742) must parse as the same construction under 82='m' (banked), with slot length 8 vs 1 giving the discriminating test.
3. The 92/93 alternation in the twin pre-contexts predicts 92 and 93 are frame-equivalent at that slot (one-group substitution inside an otherwise byte-identical frame).

## Ranked battery targets (confidence × testability)

1. **neque-79-twin-frame** (priority 3, battery). Claim: `13 {92|93} 62 94 79 14 60` is one licensed repeated frame; @1687 is its short close. Bars: (a) the same plaintext shape parses at both @1363 and @1687 under standing values with the same 14/60 readings; (b) the @1363 44-pair interior contains a licensed verb or clause head that the @1687 close lacks — the short close must be consistent with the long close's structure, not with an invented verb. Adverses: @1363's interior is formula-contaminated (cela tail @1403–@1407) — fence, do not ignore; 94='ne' stays battery-promoted pending ratification, this target does not ratify it.
2. **neque-82-frame-family** (priority 3, battery). Claim: `94 82` ("ne m…", 82='m' banked) is a distinct licensed frame family, 4× stream-wide. Bars: (a) @1182 (slotlen 8) and @1742 (slotlen 1) parse as the same frame under standing values; (b) the @578 57-pair window and the @1353 nested window (which runs into the 79-twin) carry the same `94 82` opening signature. Kill if the four instances force incompatible readings of the slot after 82.
3. **neque-14-frame-value** (priority 4, battery). Claim: 14 has one value, fixed by its frame slot in `tout [14]` at both twins. Bars: (a) a single 14 value parses `tout [14] [60]` at @1364–@1366 and @1688–@1690 under standing values; (b) the value stays consistent with 14's other 13 occurrences (null if a frame forces a split — splits need red-team ratification, fence and escalate).

Null recorded honestly: the 93/29/74-follower bracket windows are singletons with no cluster; the one-gap `94 02 79` @494 is a singleton; slot length does not predict verb-class fill in the bracket set. These stay as residuals, not battery targets.

## Adverses fenced (not ignored)

- Census-rule difference: this sweep's full scan finds 16 nearest-46 windows; the parent battery's six are the tight frames (interior ≤ 8, no formula text). The other 10 (interiors 16–69) are multi-clause runs, not 'ne…que' brackets — excluded from the productive-frame count per the de-duplication rule, with @1363 kept as discriminating context.
- @1363's formula contamination (cela tail) is fenced as the stated cause for not counting it as a second productive instance.
- 94's promotion status is unchanged: used as given, never ratified or re-litigated here.
