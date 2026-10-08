# Battery report: tout-slot-14 — 14's class from the post-'tout' slot

Worker: fe5fa41b-ae9a-4b9c-9947-e9b58e86d54b | 2026-10-08T21:38:08Z–21:55Z
Target: `tout-slot-14` (priority 2). Lock `locks/tout-slot-14.lock` created on
start, deleted on completion. No prior lock existed.

## Bar (verbatim, pre-registered before testing)

"name 14's class iff 'tout [14]' parallels 'tout [82]' under one stated value
AND the four breaker windows resolve or fence with stated cause"

Numbered clauses (fixed before testing):
- C1: 'tout [14]' parallels 'tout [82]' (= A7-L2 'tout me [48-verb]') under one
  stated value V for 14. PASS iff 'tout [V] [60]' is grammatical with V a
  function word in a class parallel to 'me', with no untestable assumption.
- C2: Breaker B1 @424 ('47 14 62 48') resolves (clean parse under standing
  values + V) or fences with stated cause.
- C3: Breakers B2 @623 ('82 14 59') and B3 @896 ('82 14 98') resolve or fence
  with stated cause.
- C4: Breaker B4 @1121 ('06 14 06') resolves or fences with stated cause.
- C5: Adverses adjudicated — exactly one of {clitic, determiner} holds across
  14's windows, or the tie is recorded with a stated discriminator.

## Method

Repaired 1,847-pair stream only: `code/side-keyhunt/repaired_offsets.json` +
`data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`
(1847 pairs, 96 distinct — verified). `canonical.py` never used. R5005
read-only. Offsets below are 0-indexed pair positions; @N marks 14's own index
(matches the queue's convention: queue '@1365' = 14 at index 1365). Every number
traces to the stream. Standing values used: 82='m', 79='tout' (A5), 47='ce'
(A4), 06='ent' (promoted), 94='ne' (battery-promoted), 48='e' (letter),
59='est' (provisional), 77='le' (provisional), 24=finite verb (class-level
promote), 67='et' here (positional rule: 14 not infinitive-shaped).
62's value is OPEN ('il' demonstrated as rival by collision-62-84, not
promoted). 60's and 98's values are OPEN (noun-60, frame-vient-parvenir queued).

## Window evidence (all 15 windows of 14; n=15 confirmed)

- @72 [a1_02]: `13 24 56 87 14 24 87 11` — 'ce [14] [24-verb] cela'. Under
  14='le': 'ce le [verb]' = the A8-granted 'ce le [verb]' frame (24=finite verb
  now promoted class-level). RESOLVES under 14='le'.
- @84 [a1_02]: `62 16 14 06 88 77` — '[16] [14] ent [88]'. No clean word-level
  parse ('[16] le ent' / '[16] l'ent' both strained). Fenced: 16 open.
- @117 [a1_03]: `21 67 14 21 60 90` — 'et [14] [21]' (67='et' by positional
  rule). Under 14='le': 'et le [21]' — grammatical shape. Supports determiner.
- @141 [a1_04]: `66 14 74 67 64` — '[66] [14] [74]'. Neutral (66 open).
- @178 [a1_05]: `21 69 14 24 87 64` — '[69] [14] [24-verb] ce qui'. Under
  14='le' as CLITIC: '[69] le [verb]' needs 69 subject-capable (69 open).
  Fenced; this window is the clitic reading's best leg.
- @339 [a2_05]: `31 14 45 64 96` — '[31] [14] ce qui par'. 'le ce' ungrammatical
  both readings. Fenced: 31 open, 45='ce' HOLD.
- B1 @424 [a2_09]: `29 47 14 62 48 76` — 'er ce [14] [62] e [76]'. No stated
  value parses ('ce le [62] e' with 62 open; 62='il' rival gives 'ce le il e').
  FENCED: gated on 62's value battery ('62 48' x6 unresolved).
- @458 [a2_10]: `66 14 02 79 87` — '[66] [14] [02] tout'. Neutral (66, 02 open).
- @586 [a3_02]: `18 14 00 97 41` — '[18] [14] pour [97]'. 'le pour'
  ungrammatical both readings. Fenced: 18 open (possible clause boundary).
- B2 @623 [a4_01]: `76 82 14 59 37 33` — '[76] m [14] est [37-pred] [33]er'.
  'me le est' ungrammatical; "m'en est" marginal ('il m'en est resté' is
  literary). Cleanest fence: clause boundary '[76] me' | '[14] est [37]'
  ('[noun] est [predicative]', A1-shaped) with 76 open.
- @813 [a5_05]: `24 65 14 29 49 74` — '[24-verb] [65] [14] er [49]'. '14 29' =
  '[14]er' infinitive-shaped — the verb-rival's best leg. Fenced: 65 open.
- B3 @896 [a5_08]: `98 82 14 98 83 86` — '[98] m [14] [98] de [86]'. Under
  98='vient' (UNCONFIRMED lead, frame-vient-parvenir queued) + 14=infinitive:
  'vient me [inf]' — clean ('vient me dire/voir'). FENCED: load-bearing on
  open 98; pulls toward the verb rival, against B2.
- B4 @1121 [a6_07]: `12 06 14 06 11 52` — 'n ent [14] ent la [52]'. 06='ent'
  PROMOTED on both sides. No word-level function-word value parses between
  two finite 3rd-plural verb endings ('ent le ent', 'ent en ent' all
  ungrammatical). FENCED: requires an unmarked clause boundary or a
  non-word-level (syllabic) 14 — structural anomaly, flagged below.
- @1365 [a7_06]: `94 79 14 60 03 30` — inside '62-94-79-14-60': 'ne tout [14]
  [60] [03] pas'. See C1.
- @1689 [a8_05]: `94 79 14 60 27 46` — inside '62-94-79-14-60': 'ne tout [14]
  [60] [27] que'. See C1.

Contact profile (n=15): successors 24 x2, 06 x2, 60 x2, 21, 74, 45, 62, 02,
00, 59, 29, 98 (6/15 verb-adjacent: 24 x2 finite verb, 06 x2 'ent', 59 'est',
29 'er'); predecessors 66 x2, 82 x2, 79 x2, 87, 16, 67, 69, 31, 47, 18, 65, 06.
79-14 x2 (both frame-exclusive, zero elsewhere); 82-14 x2; 47-14-62 x1;
06-14-06 x1. A7-L2 reference verified: 79-82 x2 @396/@1227, both '79 82 48'
('tout m [48]').

Prior battery constraint (not re-litigated): frame-62-94-79 (null,
2026-10-08) already killed 14='me' ('ce me il', "m'me", 'ent me ent'),
14='est' (zero of 59's predicative concentration), and 14=verb inside the
'tout' frame ('tout' before the verb). Those kills stand and are used as
premises.

## Per-clause pass/fail

- C1 (parallelism under one stated value): FAIL. The only viable function-word
  value is 14='le'. As determiner, 'tout le [60]' ('tout le X') is grammatical
  and slot-parallel to 'tout me [48-verb]', but (a) the parallelism is
  slot-level, not class-level (determiner+noun vs clitic+verb — the adverses'
  own distinction); (b) it is load-bearing on 60's nominal slot, which is
  noun-60's queued, untested bar — establishing it here would duplicate that
  bar; (c) '79 14' is frame-exclusive to '62-94-79-14-60', where the determiner
  reading was already killed on SVO order ('il ne tout le [60] [03] pas').
  As clitic, 'tout le [60-verb]' needs 60 verb-shaped, contradicting 60's
  observed noun profile ('77 60' @454; '60 03' x4). No stated value yields a
  clean parallel. Not kill-grade: the parallelism is underdetermined (the
  bigram never occurs outside the unparsed frame), not forced-false.
- C2 (B1): FENCE with stated cause — gated on 62's value battery (62 open;
  'il' rival unpromoted; '62 48' x6 unresolved). No overwrite of the
  collision-62-84 verdict.
- C3 (B2/B3): FENCE with stated cause — B2/B3 pull opposite ways (B3 favors
  14=infinitive under unconfirmed 98='vient'; B2 resists every stated value,
  cleanest fence is a clause boundary with 76 open). The '82 14' pair is
  compatible with 14='le' ('me le') and 14='en' ("m'en") but neither extends
  to a full-window parse.
- C4 (B4): FENCE with stated cause — strongest breaker: no word-level value
  parses in 'ent [14] ent' (06='ent' promoted both sides). Requires an
  unmarked clause boundary or non-word-level 14; recorded as a structural
  anomaly, not a kill (a boundary cannot be excluded at battery level).
- C5 (adverses): TIE RECORDED. Determiner legs: @72 (A8 'ce le [verb]' frame),
  @117 ('et le [21]'), 'tout le [60]'. Clitic legs: @178 ('[69] le [verb]',
  69 open), B2's 'me le'/'m'en' shapes. Successor profile mixed (6/15
  verb-adjacent). Discriminators are both queued elsewhere: 69's class
  (subject-capable? favors clitic) and 60's class (noun? favors determiner).

## Verdict

**null.** No class can be named: C1 fails (parallelism underdetermined), and
all four breakers fence rather than resolve. No red-team verdict is
contradicted (no red-team ruling touches 14; the frame-62-94-79 battery kills
are used as premises, not re-litigated). No standing §7 rule is violated
(14='le' was not promoted, so no second polyvalence and no 77~14 homophony
claim is created; both are flagged below as open questions).

Notes for the record: (1) If 14='le' ever promotes, the 77='le' provisional
needs a homophony battery (77 n=44 vs 14 n=15). (2) B4 @1121 is the strongest
breaker in the set and may be a genuine word-boundary residual. (3) The
14=infinitive rival (B3, @813) is live but not demonstrated (fails @72, @178,
B1, B4 as a verb).

## Follow-ups (null regenerates work)

1. `tout-14-rerun` — Re-test C1 once noun-60 lands. Bar: "name 14='le'
   (determiner) iff 'tout le [60-noun]' parallelism holds AND the
   '62-94-79-14-60' SVO wall falls; coordinate with frame-62-94-79-reparse,
   do not duplicate noun-60's bar."
2. `breaker-b4-1121` — Resolve '06 14 06' @1121. Bar: "resolve iff a clause
   boundary is demonstrated with punctuation-independent evidence, or 14
   takes a value grammatical between two promoted 'ent' verb-endings; else
   confirm as a genuine word-boundary residual."
3. `verb-14-rival` — Test 14=infinitive/verb-stem (B3 'vient me [14]' under
   98='vient', @813 '[14]er', B2 '[14] est [37]'). Bar: "name 14=verb iff B2,
   B3, @72, @178, B1, B4 all parse as verb frames with <=10% orphan; else
   kill the rival."
