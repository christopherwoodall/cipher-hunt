# Battery report: governor-88-value

- Target id: `governor-88-value`
- Claim: "name 88's class from its 23-window profile"
- Date: 2026-10-08
- Worker: agent 859a3a1b-983b-4108-bb9f-1c2ffbf6a9ae
- Lock note: locks/ held only NOTE.md at start; created locks/governor-88-value.lock 2026-10-08T17:54:36Z, deleted on completion.

## Bar (verbatim from battery-queue.json)

"name 88's class (verb-governor vs preposition vs other) with its full 23-window profile; own the preposition rival and the @334 '88-40' word-internal question; >=2 frame-legs for the named class"

## Numbered clauses (fixed before testing)

1. 88's class is named (verb-governor vs preposition vs other) with the full 23-window profile re-derived by this worker.
2. The preposition rival is owned: 88-as-preposition is tested against the stream and either demonstrated or rejected with evidence.
3. The @334 '88-40' question is owned: word-internal ('[88]e') vs word boundary is decided with evidence.
4. >=2 frame-legs for the named class are shown on the repaired stream.

## Method

Repaired 1,847-pair stream only: code/side-keyhunt/repaired_offsets.json over
data/upstream-ct_R5005.txt, parsed exactly like
code/side-keyhunt/repair_parse.py (byte-exact
`[s[i:i+2] for i in range(o, len(s)-1, 2)]`). code/side-keyhunt/canonical.py
never used. R5005 untouched. All @-offsets are 0-based repaired-stream pair
indices. Standing values used: banked 11=la, 70=pre, 82=m, 34=i, 29=er,
40=e, 46=que; promoted 87=ce, 64=qui, 96=par, 17=fois, 79=tout (A5),
00=pour (A9, class-level), 84=on (A15), 47=ce (A4, allophone tier), 39=a/a;
provisional 59=est, 77=le; battery-promoted pending ratification 94=ne
(ne-94), 12=n + 48=e (n-e-12-48), 06=ent (ent-06), 30=pas (pas-30);
class-level promotes 24=finite verb (ne-24-profile), 86 INF-class (A9).
Every count below is re-derived from the stream, not copied from the
lever-88-governor null or the queue gloss.

## 88's full 23-window profile (re-derived)

88 occurs x23 at @42, @86, @210, @304, @306, @334, @402, @497, @513, @616,
@619, @646, @730, @765, @904, @1049, @1117, @1260, @1267, @1514, @1541,
@1706, @1727.

Successors: 77 x3 (@86/@646/@1541), 11 x2 (@730/@1514), 24 x2
(@1267/@1727), and x1 each: 43 (@42), 19 (@210), 02 (@304), 20 (@306),
40 (@334), 53 (@402), 47 (@497), 56 (@513), 10 (@616), 37 (@619), 66 (@765),
18 (@904), 29 (@1049), 70 (@1117), 01 (@1260), 26 (@1706).

Predecessors: 39 x2 (@765/@1727), 69 x2 (@1117/@1267), and x1 each: 24
(@42), 06 (@86), 50 (@210), 89 (@304), 02 (@306), 54 (@334), 45 (@402),
79 (@497), 65 (@513), 70 (@616), 29 (@619), 61 (@646), 48 (@730), 16
(@904), 41 (@1049), 11 (@1117), 81 (@1514), 93 (@1541), 94 (@1706).

Corrections to the prior partial profile (lever-88-governor null): the
null listed only 10 singleton successors and 10 singleton predecessors;
the full census adds successors 37/66/18/29/70/01/26 and predecessors
29/61/48/16/41/11/81/93/94. The null's claim "88 never directly precedes
29" is REFUTED: 88->29 x1 at @1049 ('85-41 [88] 29-40-29').

Window contexts (±2):
- @42 (a1_01): 01-24 [88] 43-81-30
- @86 (a1_02): 14-06 [88] 77-66-98
- @210 (a2_00): 44-50 [88] 19-74-77
- @304 (a2_04): 18-89 [88] 02-88-20
- @306 (a2_04): 88-02 [88] 20-17-46
- @334 (a2_05): 45-54 [88] 40-03-64
- @402 (a2_08): 11-45 [88] 53-34-69
- @497 (a2_11): 02-79 [88] 47-11-29
- @513 (a3_00): 98-65 [88] 56-87-77
- @616 (a4_00): 83-70 [88] 10-29-88
- @619 (a4_01): 10-29 [88] 37-76-82
- @646 (a4_02): 87-61 [88] 77-78-52
- @730 (a5_02): 86-48 [88] 11-24-85
- @765 (a5_03): 59-39 [88] 66-98-80
- @904 (a5_09): 67-16 [88] 18-55-83
- @1049 (a5_09): 67-76-85-41 [88] 29-40-29-74 (wider)
- @1117 (a6_07): 69-11 [88] 70-12-06
- @1260 (a7_02): 29-69 [88] 01-09-11
- @1267 (a7_02): 46-69 [88] 24-30-20
- @1514 (a7_11): 39-81 [88] 11-31-11
- @1541 (a8_00): 62-93 [88] 77-78-43
- @1706 (a8_06): 62-94 [88] 26-12-06
- @1727 (a8_07): 98-39 [88] 24-30-15

## Preposition rival: tested and rejected (distributional)

Controls: the two granted prepositions 00='pour' (n=55) and 96='par'
(n=21), successor profiles re-derived.

- R1: 88->77 x3/23 vs 00->77 x0/55 and 96->77 x0/21 (pooled 0/76).
  Fisher exact p=0.0113. The known prepositions never take 77 in this
  corpus; 88 takes it three times. Significant at the lane's standard.
  Conditional on 77='le' (provisional): if 77 is not 'le', this test
  dissolves, but R2 stands alone.
- R2: 88 takes zero infinitive-class followers (86 x0, 33 x0; 0/23) vs
  00='pour' taking 86 x12 + 33 x8 (20/55). Fisher exact p=0.0004.
  Highly significant. 88 does not select infinitives the way 'pour'
  does. (96='par' also lacks 86/33 followers, so R2 alone does not kill
  every preposition; R1 is the sharper test.)
- R3 (shared ground, not discriminating): 88->11 x2/23 vs 00->11 x4/55,
  Fisher p=1.0. Article-taking per se is shared; the divergence is
  specific to 77 and to infinitive selection.
- R4: @1705-1706 '94 [88]' with 94='ne' (battery-promoted): 'ne' +
  preposition is ungrammatical in French under the word-boundary
  reading. (The word-internal reading, '[88][26]nent', avoids this;
  both readings are verb-compatible.)

Result: the preposition rival is rejected on distributional grounds.
No preposition frame for 88 is demonstrated on any window.

## @334 '88-40': owned — word-internal '[88]e'

Window: @332-337 '92-50-45-54 [88] 40-03-64'. 40='e' is a banked LETTER.
40's profile (n=21): predecessors 29 x9 ('er'+'e' = word-final '-ere',
as in the 'la premiere' crib 11-70-82-34-29-40), 78 x3, then singles
(88/97/96/74/50/03/48/61 x1). So 40 is word-final 'e' in 9/21 windows
and always letter-grade (word-internal or word-final, never
word-initial in any evidenced parse).

- Word-internal reading: '[88]e' = a word ending in -e whose stem is 88
  (verb 3sg 'il [88]e', 'semble'-shaped, or a nominal stem), then 03
  starts a new word. Consistent with 40's profile and with 88 as a stem.
- Word-boundary reading: 88-word + 'e[03...]'-word. Fails: no French
  word has the shape 'e'+[03] (03 is verb-stem-shaped per stem-03:
  '[03]er' infinitive frame, '03 qui 31' x2 verbal context). The only
  other 40-03 window (@598) shows the same 'e'+[03] adjacency, keeping
  the boundary reading word-shape-less in both cases.

Decision: @334 is word-internal '[88]e' + new word 03. 88 behaves as a
STEM here, not a standalone word. This does not name 88's value; it is
compatible with a verb stem (3sg inflection) and rules out the
boundary parse.

## Frame legs for verb-class

- L1 @497 '79 [88] 47' = 'tout [88] ce' (79='tout' granted A5).
  Nominal 88 fails ('tout [noun] ce' needs an article); adjectival 88
  fails ('tout [adj] ce' bare is ungrammatical); adverbial 88 fails
  ('tout [adv] ce' has no parse). Verb (infinitive) survives:
  'tout [inf]' is the live frame. Soft: 79 is polyvalent in French
  (determiner/adverb/pronoun), so this is elimination, not a direct
  positive.
- L2 @765 '59-39 [88]' = 'est a [88]' (59='est' provisional, 39='a'
  promoted). 'etre a' + infinitive is the grammatical frame ('c'est a
  faire', 'reste a voir'). Nominal 88 has no parse here. Soft:
  conditional on provisional 59='est'.
- L3 @646/@1541: 88 in the governor slot directly before 77-78 with a
  nominal object after (52 at @646 via 'la 52' x3; 43 at @1541 via
  'par 43' x2 / '43 pour' x3). Same slot twice (parent null, soft;
  composition not re-litigated per brief).
- L4 @86 '14-06 [88] 77-66': '88 le [66]' transitive frame under
  77='le' provisional (soft; 06@85 contact fenced per parent null).
- L5 @1049 '[88] 29-40': 88+'er' infinitive-shaped (29='er' banked;
  corrects the null's 'never precedes 29'). Soft: 40='e' after gives
  the '[88]ere'-word rival ('maniere'-shaped); stem evidence either way.
- L6 @1706 '[88] 26-12-06': 12-06 ('n'+'ent' = 3pl ending,
  battery-promoted) occurs exactly x2 in the stream (@1119, @1708),
  and BOTH have 88 immediately before (88-70-12-06, 88-26-12-06).
  Readings: (a) word-internal 3pl verbs '[88]prennent' /
  '[88][26]nent' with 88 stem-initial; (b) boundary 'ne [88]
  [26nent]' with 88 in the preverbal clitic/adverb slot. Both are
  verb-adjacent. Soft: n=2.
- L7 @1267/@1727 '[88] 24-30': 88 before 24 (finite verb,
  class-level promote) + 30='pas' (battery-promoted) x2:
  '[88] [24] pas' / word-internal '[88][24] pas' (negated verb,
  lone-'pas' parallel to the lane's lone-'ne' norm). Verb-adjacent x2.

'Other'-class elimination: noun fails L1/L2; adjective fails L1 and
'88 le' x3; adverb fails L1 and '88 le' x3; conjunction/pronoun have no
parse at any window. Verb-class is the last class standing.

## Per-clause pass/fail

1. Class named with full profile: PASS. 88 = VERB-CLASS
   (verb stem/governor). Full 23-window census re-derived above; two
   corrections to the prior partial profile recorded.
2. Preposition rival owned: PASS. Rejected distributionally (R1
   p=0.0113, R2 p=0.0004; R1 conditional on 77='le' provisional, R2
   independent). No preposition frame demonstrated.
3. @334 owned: PASS. Word-internal '[88]e' decided; boundary parse
   rejected on word-shape grounds.
4. >=2 frame-legs: PASS. L1, L2, L5, L6, L7 are independent of the
   77-78 composition; L3, L4 corroborate (soft).

## Adverses answered

- '77 takes 15 predecessor types, keeping 88 le class-neutral':
  CORRECTED and answered. Re-derived: 77 n=44 with 22 predecessor
  types (not 15). The class-neutrality point stands on its own, but
  the verdict does not rest on '88 le' alone: the preposition
  rejection uses the 00/96 control comparison, and the positive legs
  (L1, L2, L5, L6, L7) do not assume 77='le'.
- '88 value fully open': RESPECTED. No value is named or promoted.
  Class-level claim only, per the ne-24-profile precedent
  ('promote — class-level').
- 'preposition rival open': ANSWERED — tested and rejected (see R1-R4).

## Tensions fenced (not kills)

- T1 @304/@306: 88 doubled within 4 pairs (@304 after 89 verb-frame A8
  fits '[verb] [88-inf]'; @306 '[88] 20-17-46' = '[88] [20] fois que'
  admits a determiner-shaped rival reading if 20='une', 20's value
  open). Clause boundary possible. Fenced.
- T2 @1117 '69-11 [88] 70-12-06' = 'la [88] prennent': nominal-shaped
  'la [88]' + new clause ('[ils] prennent', subject unexpressed, cf.
  lone-'ne' norm) is available; the word-internal '[88]prennent'
  ('comprennent'-shaped) would force 88='com' prefix, conflicting
  with standalone-88 and barred by §7 sole-polyvalence. Neither
  forced. Fenced as genuine tension.
- T3 @730 '86-48 [88] 11': 48-88 contact unresolved ('[86]e[88]'
  word-internal vs boundary). Fenced; 88->11 = article contact either
  way.
- T4 @616 '70 [88] 10-29 [88] 37': doubled 88 with '[10]er'
  (10-29 x1 stream-wide) between; '88 [10]er' reads as governor +
  infinitive (modal-shaped) but 10 is open. Recorded as possible
  fifth leg, not asserted.
- T5: 77='le' provisional — L4 and R1 are conditional on it; stated.

## Verdict: PROMOTE (class-level)

88's class is VERB-CLASS (verb stem/governor). All four bar clauses
pass; all three adverses are answered. No value is named or promoted;
88's value stays open for a future value battery. No standing red-team
verdict is contradicted (R16-005's 78='ver' LEAD untouched; the
lever-77-78 composition not re-litigated; the lever-88-governor null
not downgraded — its 'not kill' finding is consistent with this
class-level promote). §7 respected: no new polyvalence declared
(88-as-stem is cipher granularity, parallel to 29='er' and 40='e',
not a second lexical value); 67 et/veut sole polyvalence untouched;
canonical.py never used; R5005 untouched.

Downstream consumers: finiteness-88-86 (queued), governor-88-rerun
(queued); a future 88-value battery (unnamed value) is the remaining
work. No follow-ups required by a promote; none proposed.
