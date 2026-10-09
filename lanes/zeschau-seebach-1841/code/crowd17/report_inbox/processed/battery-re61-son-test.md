# Battery report: re61-son-test

Target: `re61-son-test`. Claim: 61="son" — "resonnement" @576 (55 61 94 82 06
= re-son-ne-m-ent) and "resonne" @1167 (55 61 94 = "résonne", 3sg of résonner)
— against the full 61 census (n=18); decides whether 55-61-94 is a word unit.
Date: 2026-10-09. Worker: b2f63117-37b1-4735-9d76-fb5ee4116a89.
Lock `crowd17/next-token/locks/re61-son-test.lock` created 2026-10-09T07:53:48Z
on start; no fresh lock existed. Deleted on completion.

Stream: repaired 1,847-pair parse (`data/upstream-ct_R5005.txt` +
`code/side-keyhunt/repaired_offsets.json`, parsed per
`code/side-keyhunt/repair_parse.py`). `canonical.py` never used. R5005,
sealed gates, and the red-team queue untouched. All counts re-derived in
session; no prior counts trusted. @-offsets are 0-based pair indices.

## Bar

FINDING F1: the queue entry's `bars` field is null. The bar was unstated.
Per the dispatch brief, the worker states the bar here BEFORE testing and
does not change it after seeing data.

Worker-stated bar (frozen before testing):

- C1: a "son"-reading parses >=3 INDEPENDENT 61 windows, each with a stated
  gloss. (Two windows sharing one byte-identical formula count once.)
- C2: zero kill-grade contradictions — no window forces 61 != "son", and no
  parse contradicts a standing promote/kill.
- C3: the flagship 55-61-94 unit parses as "resonne"/"resonnement" with no
  leftover pairs and no conflict with standing verdicts.
- promote iff C1 and C2 and C3. Kill iff a window forces the claim false or
  a cleaner rival value is demonstrated on the same frames. Else null.

## Method

Re-derived the stream (1,847 pairs, 96 types). Built the full 61 census
(n=18, confirmed) and the 55 census (n=12, confirmed). Checked every 61
window for a "son"-shaped parse (syllable left/right attach, standalone
noun/possessive). Checked the two flagship windows against standing
promotes. Read the standing reports that occupy this ground before
deciding: `battery-seg-55-61-21-stem.md` (PROMOTE discriminator),
`battery-seg-61-94-word-adjudicate.md` (KILL), `battery-subj-55-61-word.md`
(KILL), `battery-seg-ceci-87-61.md` (PROMOTE locus), `battery-val-61-premier.md`
(PROMOTE narrow), `battery-seg-61-pren-polyvalence.md` (KILL),
`code/crowd17/report_inbox/processed/battery-ent-06.md` (PROMOTE),
`battery-seg-55-re-prefix.md` (NULL).

## Standing verdicts that bear on this target

- S1: `seg-55-61-21-stem` PROMOTE (2026-10-09): 55-61 = "prend" (finite 3sg
  of prendre) demonstrated at W3 (@1205-1206) with a full grammatical parse.
  Its clause 2 reads the two 94-carrying windows (@576, @1167) as
  "prenne"-compatible (subjunctive-frame) — the prendre family, not "re"+"son".
- S2: `seg-61-94-word-adjudicate` KILL (2026-10-09): the 55-61-94 word claim
  closed as a live non-12-pre-94 family candidate (kill-grade; terminal).
- S3: `subj-55-61-word` KILL: W3 forces 55-61 verb-shaped; section 7 bars a
  noun-at-W1/verb-at-W3 split at battery level.
- S4: `seg-ceci-87-61` PROMOTE (locus): 87-61 @644 = "ceci" (61="ci" there).
- S5: `val-61-premier` PROMOTE (narrow): 61-40-17 @1556 = "première fois"
  (61="premier" there).
- S6: `seg-61-pren-polyvalence` KILL: 61="pren" killed as a global value.
- S7: `ent-06` PROMOTE: F1 leg "@578-581: 94-82-06-06 = ne mentent"
  (negation + verb 3pl), load-bearing for 06="ent".
- S8: `seg-55-re-prefix` NULL: 55="re" could not be demonstrated in any
  window; "no window forces 55 != re" — untested, not granted.

## Census facts (re-derived)

- 61 n=18. 55 n=12 (followers: 81 x6, 61 x3, 83 x2, 68 x1).
- 55-61 bigram: exactly 3x — @576, @1167, @1205.
- 61-94 bigram: exactly 2x — @577-578, @1168-1169. The whole 61-94 population.
- 55-61-94 trigram: exactly 2x — @576, @1167. Never occurs outside the
  byte-identical 5-gram "78-45-13-55-61" (@573 and @1164, x2). The two
  flagship "legs" are one repeated formula, not two independent legs.
- Flagship 1 (0-based): @576-581 = 55 61 94 82 06 06; @582 = 50.
- Flagship 2 (0-based): @1167-1172 = 55 61 94 87 83 21.

## Window-level evidence (all 18, 61 marked)

- @223: `89 84 91 37 [61] 96 87 46 98`. "son"+"par" ungrammatical (96="par"
  standing). No clean "son" parse.
- @279: `89 84 91 37 [61] 20 [61] 42 48`. Sandwich; no clean parse.
- @281: `91 37 61 20 [61] 42 48 52 89`. No clean parse.
- @367: `47 78 48 49 [61] 70 17 06 21`. "son"+"pre" is not a word. No clean parse.
- @447: `78 41 10 62 [61] 59 32 48 79`. "62 son est 32" broken under every
  standing 62 value. No clean parse.
- @577 FLAGSHIP 1: `78 45 13 55 [61] 94 82 06 06`. The claim's "resonnement"
  = 55-61-94-82-06 (@576-580). KILLED at this locus, two ways: (a) it is
  mutually exclusive with the PROMOTED S7 leg "ne mentent" @578-581 —
  @578 cannot be both the noun's internal "ne" syllable and the negation
  particle governing "mentent"; per never-downgrade the promoted reading
  wins; (b) @581's second 06 ("ent") dangles after the noun with @582=50
  unexplained — the parse leaves a leftover pair.
- @645: `48 20 24 87 [61] 88 77 78 52`. "ce son" is excluded: S4 PROMOTED
  87-61 @644 = "ceci" (61="ci" locus-level). No "son" parse survives here.
- @926: `08 65 71 17 [61] 96 48 82 98`. "fois son par" broken (96="par"
  standing). No clean parse.
- @1168 FLAGSHIP 2: `78 45 13 55 [61] 94 87 83 21`. "résonne" needs 55="re",
  which S8 left untested and which 55's census (6/12 before the 81
  masculine noun, 3x "55-81-00=pour") does not support. Followers
  "ce 83 21" unparsed; left "78-45-13" unparsed. Not a clean parse. Same
  repeated formula as flagship 1 — not independent.
- @1206: `58 47 43 55 [61] 21 65 64 59`. S1 PROMOTED 55-61 = "prend" here
  ("prend [21]", full parse). "re"+"son" excluded by section 7 (S3 precedent).
- @1219: `36 77 83 92 [61] 24 48 30 09`. No clean "son" parse.
- @1256: `06 65 46 01 [61] 31 29 69 88`. No clean "son" parse.
- @1281: `56 85 48 53 [61] 56 32 98 55`. No clean "son" parse.
- @1429: `29 87 63 91 [61] 12 16 76 49`. "son"+"n"(12) = "sonn", incomplete;
  no clean parse.
- @1455: `33 46 92 62 [61] 21 67 86 66`. 61 without 55; no clean "son" parse.
- @1510: `86 56 41 12 [61] 59 39 81 88`. "n son est" broken. No clean parse.
- @1556: `23 99 13 93 [61] 40 17 11 26`. S5 PROMOTED 61="premier" here
  ("première fois"). Excluded.
- @1810: `94 52 80 04 [61] 15 93 50 42`. No clean "son" parse.

Clean "son" parses in the census: ZERO.

## Per-clause verdict

- C1 (>=3 independent "son" windows): FAIL. Zero clean legs. The two
  flagships are one repeated formula; flagship 1's parse is dead (see K1
  below); flagship 2 is not clean.
- C2 (zero kill-grade contradictions): FAIL. Two kill-grade conflicts:
  flagship 1 vs the promoted "ne mentent" leg; the "re"+"son" segmentation
  vs the promoted "prend" discriminator (section 7 bars the split, S3
  precedent).
- C3 (flagship parses cleanly): FAIL. See flagship-1 and flagship-2 notes.

## Verdict: KILL

Kill bases (each sufficient):

- K1: The claim's flagship-1 parse ("resonnement" = 55-61-94-82-06 @576-580)
  is mutually exclusive with the PROMOTED ent-06 F1 leg "ne mentent"
  (@578-581). @578-580 cannot serve as noun-internal "ne-m-ent" and as
  negation+verb at once. Never-downgrade decides it: the flagship parse is
  false at its own locus. A bar clause fails at kill grade.
- K2: A cleaner rival is demonstrated on the same frames. S1 PROMOTED
  55-61 = "prend" (demonstrated, full parse at @1205) and reads the two
  flagship windows as "prenne"-family. "re"+"son" vs "prend"/"prenne" are
  mutually exclusive segmentations of the same byte-identical bigram;
  section 7 (67 = sole true polyvalence) bars a son-syllable-at-flagships /
  prend-verb-at-W3 split at battery level — the exact pattern of the
  standing S3 kill.
- K3: 61 has no window left for "son". S4 (61="ci" @644), S5 (61="premier"
  @1556), S6 (61="pren" killed), S1 (55-61="prend"/"prenne"). The census
  yields zero clean "son" parses in 18 windows.

Relation to standing verdicts: this kill AGREES WITH and EXTENDS the
standing S2 kill (`seg-61-94-word-adjudicate`), which closed the 55-61-94
family candidacy on procedural grounds plus the "pren" kill. That battery
noted "no alternative named French word with 61-94 as syllables exists" —
the "son"/"resonne" sub-claim named here is that alternative, and it fails
on the evidence above. No standing verdict is contradicted or downgraded;
no red-team verdict is touched (section 5 escalation not triggered).

## Follow-ups

None. A kill closes the line; section 4 requires follow-ups only for
nulls (precedent: `battery-seg-61-94-word-adjudicate`). Re-open condition
(red-team calls, not battery calls): red-team ratification of a 61-94 word,
or red-team declaration of a second polyvalence covering 61.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-re61-son-test.md`
- Queue: `re61-son-test` -> status `verdict`, result `kill`, date 2026-10-09
  (fresh re-read at completion; pre-write assert: status still `queued`,
  verdict null; temp-file + os.rename; no other entry touched).
- Lock `crowd17/next-token/locks/re61-son-test.lock` deleted on completion.
