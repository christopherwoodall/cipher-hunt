# Red-team evidence package: 55's class

Target id: `redteam-55-class-input`. Claim: red-team evidence package for 55's class.
Date: 2026-10-09. Worker: battery subagent 30d92393-1292-4865-8534-451b04689c0c.
Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` +
`code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py`;
1,847 pairs / 96 types asserted in-session). `canonical.py` never used. R5005,
sealed gates, red-team adjudication queue untouched.
Lock: `code/crowd17/next-token/locks/redteam-55-class-input.lock` created
2026-10-09T17:06:56Z (no pre-existing lock); deleted on completion.
Offset convention: @n = 0-based pair index in the repaired stream.

## Bar (verbatim from battery-queue.json)

"gather only, red team decides: 'prend'-stem word-internal (55-61 x3,
seg-55-61-21-stem) vs 're'-prefix (55-81 x6, re81-stem-elim) vs determiner
hypothesis (class-55-det KILL)"

## Numbered clauses (pre-registered before testing)

1. Re-derive 55's full 12-window census byte-exact on the repaired stream
   (positions, rows, followers, predecessors, ±7 context).
2. Record the evidence for reading (a) "'prend'-stem word-internal at the
   55-61 x3 windows" from battery-seg-55-61-21-stem (PROMOTE, 2026-10-09) and
   battery-name-55-61-core (NULL, 2026-10-08).
3. Record the evidence for reading (b) "'re'-prefix at the 55-81 x6 windows"
   from battery-re81-stem-elim (NULL, 2026-10-09), battery-seg-55-re-prefix
   (NULL, 2026-10-09), battery-seg-55-61-94-word (NULL, 2026-10-09) and the
   kills of its rival legs (battery-re61-son-test KILL, battery-re83-gar-test
   KILL).
4. Record the evidence for reading (c) "determiner-shaped separate word"
   from battery-class-55-det (KILL, 2026-10-09), including its standing
   consequences (battery-pronoun-13-les KILL, battery-x-55-61-candidate-list
   KILL, battery-merge-gate-w1-x55-61 PROMOTE, battery-x-61-94-boundary PROMOTE).
5. State the open tensions for red-team adjudication with byte-level anchors.
6. No adjudication: no value, class, or polyvalence is promoted, killed, or
   declared in this package.

## Method

Read BATTERY-PROTOCOL.md first; created the lock on start. Re-derived the
repaired stream in-session (asserted 1,847 pairs / 96 types); every count below
was re-derived from the stream, including the window dumps. Prior reports were
read (not re-litigated, not downgraded); their verdicts are recorded with
dates. Standing values used only per protocol §7.

## Window-level evidence (re-derived, byte-exact)

### 55 census (clause 1: PASS)

55 n=12. Positions (0-based): 25, 523, 550, 576, 906, 1085, 1094, 1167, 1205,
1285, 1611, 1671.
- Followers: 81 x6, 61 x3, 83 x2, 68 x1.
- Predecessors (11 distinct): 13 x2, 33, 06, 46, 18, 02, 07, 43, 98, 08, 78.
- Contact check: 61->81 x0 and 81->61 x0 stream-wide (zero contact either
  direction between the two successor families).

### The three 55-61 windows (±7)

- @576 [a3_02]: `45 94 52 87 78 45 13 | 55 61 | 94 82 06 06 50 10`
- @1167 [a6_09]: `44 83 21 67 78 45 13 | 55 61 | 94 87 83 21 85 36`
- @1205 [a7_00]: `16 64 29 45 58 47 43 | 55 61 | 21 65 64 59 32 48`
- Predecessors: 13, 13, 43 (in window order). Successors: 94, 94, 21.
- 55-61-94 formula: the 6-gram `78-45-13-55-61-94` occurs exactly x2
  (@576, @1167) with identical left 4-gram `78-45-13-55`; only 94's follower
  differs (82 @576 vs 87 @1167).

### The six 55-81 windows (±7)

- @25 [a1_00]: `64 98 82 43 29 47 33 | 55 81 | 00 34 24 30 03 64`
- @523 [a3_00]: `77 80 09 70 91 77 06 | 55 81 | 97 47 44 59 37 64`
- @550 [a3_01]: `42 06 00 46 24 47 46 | 55 81 | 00 86 59 34 17 86`
- @1085 [a6_05]: `78 64 06 52 89 24 02 | 55 81 | 00 33 79 80 06 43`
- @1094 [a6_06]: `00 33 79 80 06 43 07 | 55 81 | 06 29 67 86 52 82`
- @1671 [a8_05]: `94 84 64 06 91 11 78 | 55 81 | 92 60 03 39 74 77`
- Trigram 55-81-00: 3x (@25, @550, @1085) — the earlier "x5" was a finder
  misread, corrected in battery-seg-55-61-94-word.

### The 55-83 x2 and 55-68 x1 windows (±7)

- @906 [a5_09]: `86 16 92 67 16 88 18 | 55 83 | 54 49 64 83 59 37`
- @1611 [a8_03]: `70 39 11 92 65 23 08 | 55 83 | 71 48 31 76 42 44`
- @1285 [a7_03]: `85 48 53 61 56 32 98 | 55 68 | 00 11 17 84 59 35`

## Reading (a): 'prend'-stem word-internal at 55-61 x3 (clause 2)

Source: battery-seg-55-61-21-stem (PROMOTE, 2026-10-09) + battery-name-55-61-core
(NULL, 2026-10-08). Standing values: 47=ce (granted), 21/65=NOUN class,
64=qui, 59=est (provisional), 32 predicative frame (A1).

- At @1205 the 7-gram `58 47 43 55 61 21 65` parses as
  "[58] ce(47) [43] prend(55-61) [21]. [65] qui(64) est(59) [32]e(48)
  par(96) [36]" — "this [43] takes [21]. [65], which is [32]ed by [36]."
- 55-61 is decided as the bare finite stem "prend" (indicative; no
  subjunctive trigger, so "prenne" would be ungrammatical; the missing 94 is
  the expected finite form, not a hole).
- Rival parses at this window ("prenne", infinitive "prendre", noun/adjective
  55-61, separate-word determiner/clitic readings) were killed or fenced with
  stated cause; the sole grammatical separate-word rival needs 43=finite verb,
  overturning 43's 15/16-window noun profile (red-team venue, not battery).
- At @576/@1167, 55-61 sits in the 78-45-13-55-61-94 formula; the unit
  55-61-94 stays live there with "prenne"-family compatibility
  (battery-seg-55-61-94-word NULL).
- Residual flagged by the report itself: letter segmentation is tensed
  ("reprenne" wants 55="re"+61="pren"+94="ne"; "prend" wants 55="pre"/"pr" +
  61="nd"/"end"). Both cannot hold; the UNIT survives, its internal letters
  do not. Red-team/§7 venue.
- battery-name-55-61-core (NULL): no French word X is nameable over 55-61
  alone with stated 13/43 slot values (13/43/55/61/21 values open under §7);
  its follow-up battery-x-61-94-boundary PROMOTE (61's right boundary real:
  61-94 x2 vs 61-21 x1) and battery-merge-gate-w1-x55-61 PROMOTE stand.

## Reading (b): 're'-prefix at the 55-81 x6 windows (clause 3)

Sources: battery-re81-stem-elim (NULL, 2026-10-09), battery-seg-55-re-prefix
(NULL, 2026-10-09), battery-seg-55-61-94-word (NULL, 2026-10-09),
battery-re61-son-test (KILL), battery-re83-gar-test (KILL).

- 81="prin" kill (§7) stands; "ven" is dead globally ("reven" is not a French
  word, kill grade).
- At W2 @523, the noun stems *repas*, *regard*, *retour* (all masculine)
  survive cleanly under the standing nominal-"55 81" parse
  (`87(ce) 77(le) 80 09 70(pre) 91 77(le) 06(ent) | 55 81 | 97 47(ce) 44
  59(est) 37 64(qui)`): "55 81" occupies the subject slot with 81 nominal
  (battery-nom-97-526-adverb PROMOTE). Follow-up battery-re81-W2-noun-discrim
  is QUEUED (discriminates the three stems; needs 97's value).
- At W1 @25, W3 @550, W4 @1085 (strained only), W5 @1094 (right edge kills
  all stems: "[W]ent er" ungrammatical; consistent with the standing "[81]ent"
  3pl hostile fence at @1096, red-team venue), W6 @1671 (gender clash: 11=la
  feminine vs masculine noun stems; DET+78+verb ungrammatical) — no stem
  survives cleanly.
- The word-unit lead (55-61-94 = "prenne"-family, formula x2) stays
  compatible-but-undemonstrated at @576/@1167 ("...prenne ce..." @1167-1170
  grammatical under the undemonstrated values). Rival fenced "prenne" encoding
  70-12-94 at @347/@1547 exists (battery-seg-55-61-94-word, fenced not killed).
- Rival legs killed: battery-re61-son-test (KILL: "re-son-ne-ment"/"résonne"
  rival for 55-61-94 dead), battery-re83-gar-test (KILL: 83="gar" dead).
- §7 tension recorded by battery-re81-stem-elim: 55="re" (55-81 windows) vs
  55="prend"-stem (55-61 windows) is the sole-polyvalence rule's red-team
  venue; neither promoted nor killed at battery grade.

## Reading (c): determiner-shaped separate word (clause 4)

Source: battery-class-55-det (KILL, 2026-10-09). Bar: determiner-shaped iff
>=2 clean pre-noun slots and no window forces word-internality.

- Only 1 of the 6 windows (@550, "ce que les [81] pour [86-inf]") parses as a
  clean pre-noun slot; the bar needed >=2. Five others fenced with stated
  cause (unlicensed left edges @25/@523/@1085; unexcluded word-internal rival
  on the right edge @1094; NP pile-up @1671). Census windows add no clean slot
  ("les [83]" x2: 83's class torn; "les [68]" x1: licensor 98 open).
- Kill grade: W3 @1205 forces 55 word-internal under the standing promoted
  "prend(55-61)" discriminator; under §7's sole-polyvalence rule, 55 cannot
  be a separate word at 11 windows and word-internal at 1.
- Standing consequences recorded:
  - battery-pronoun-13-les KILL: the W1 re-segmentation gate from this kill
    ("[13] [55=les] [61]" with 13=les) is dead at its 13 premise — 13=les is
    killed. No resurrection of the W1 re-segmentation under that premise.
  - battery-x-55-61-candidate-list KILL, battery-merge-gate-w1-x55-61 PROMOTE,
    battery-x-61-94-boundary PROMOTE: the 55-61 naming thread is closed except
    where 61's boundary and the W1 subject-merge were promoted.

## Open tensions for the red team (clause 5)

1. **The 11-vs-1 segmentation split.** Two standing battery verdicts point at
   a positional tension: class-55-det (KILL) forces 55 word-internal at W3
   @1205 only; seg-55-61-21-stem (PROMOTE) decides the one-word "prend" there;
   the other 11 windows are separate-word-shaped ("55 81" x6 nominal-adjacent,
   "55 83" x2, "55 68" x1). Under §7's sole-polyvalence rule this is a
   positional-polyvalence-shaped observation. Venue: red team.
2. **The letter-level residual.** "reprenne" (55="re"+61="pren"+94="ne") vs
   "prend" (55="pre"/"pr"+61="nd"/"end") cannot both hold at the letter level;
   the UNIT survives while its internal segmentation does not
   (battery-seg-55-61-21-stem, flagged).
3. **The pronoun-13-les kill consequence.** The "ne mentent" subject at
   @576-581 (`...55 61 94 82 06 06`) lost its "[13]=les" re-segmentation
   premise; W1's subject identification is not revived by reading (c).
4. **Pending discriminators already queued:** battery-re81-W2-noun-discrim
   (repas/regard/retour at @523; needs 97), battery-re81-W4-02-class
   (determiner-02 vs subject-02 at @1085).

## Per-clause pass/fail

1. PASS — census re-derived byte-exact (12/12 positions, followers 81x6/61x3/
   83x2/68x1, 11 distinct predecessors, 61<->81 zero contact).
2. PASS — reading (a) evidence recorded verbatim with anchors.
3. PASS — reading (b) evidence recorded verbatim with anchors.
4. PASS — reading (c) evidence recorded verbatim with anchors.
5. PASS — four open tensions stated with byte-level anchors.
6. PASS — no adjudication attempted anywhere in this package.

## Verdict: NULL (gather-only)

All six clauses pass. No promote, no kill, no value named, no polyvalence
declared. This package is input to the red-team docket, which decides.

## Follow-ups (verified absent from battery-queue.json)

1. `redteam-55-polyvalence` (P2) — the §7 venue question: whether 55 needs a
   second polyvalence ("prend"-stem @1205 vs "re"-prefix in the 55-81
   windows), a positional segmentation rule, or whether one class covers all
   12 windows. Gather-only evidence: this report plus
   battery-re81-W2-noun-discrim and battery-re81-W4-02-class when they return.
   Battery may gather; only the red team decides.

## Bookkeeping

- Queue: `redteam-55-class-input` queued -> verdict/null, 2026-10-09
  (pre-write assert: queued/verdictless; temp-file + rename; JSON
  re-validated from disk; own entry only; no downgrade).
- Lock created on start (agent id + UTC 2026-10-09T17:06:56Z), deleted on
  completion.
- `canonical.py` never used. R5005, sealed gates, red-team adjudication
  queue untouched. No standing or red-team verdict contradicted, downgraded,
  or re-litigated. §7 intact.
