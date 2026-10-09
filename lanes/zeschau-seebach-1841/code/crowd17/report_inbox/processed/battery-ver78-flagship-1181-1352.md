# Battery report: ver78-flagship-1181-1352 — confirm the 'le ver ne ment(ent)' flagship frame

- Target id: `ver78-flagship-1181-1352` (priority 2)
- Date: 2026-10-09
- Worker: f2c8cc06-c845-4220-93e9-c7cdfc67aa9e
- Stream: repaired 1,847-pair parse only (`code/side-keyhunt/repaired_offsets.json` +
  `data/upstream-ct_R5005.txt`, parsed exactly like `code/side-keyhunt/repair_parse.py`;
  1,847 pairs / 96 types asserted in-session). `canonical.py` never used. R5005 untouched.
- Lock: `code/crowd17/next-token/locks/ver78-flagship-1181-1352.lock` created
  2026-10-09T07:53:46Z (no prior lock); deleted on completion.

## Dependency (gate now cleared)

The target was gated on 94/06 settling. The gate is cleared at battery grade:
94='ne' battery-promoted 2026-10-07; 06='ent' battery-promoted 2026-10-08,
refined 2026-10-09 (ent-06-host-census: 06 is a finite 3pl ending iff its left
neighbor is a verb stem, else a syllable; single value, no polyvalence).
Both are pending red-team ratification. This report uses the battery-promoted
values and does not claim ratification.

## Bar (verbatim, pre-registered)

"confirm iff the flagship frame parses cleanly under the settled 94/06 values;
else fence with stated cause."

## Numbered pass/fail clauses (frozen before testing)

1. SETTLED VALUES: 94='ne' (battery-promote 2026-10-07) and 06='ent'
   (battery-promote 2026-10-08, rule refined 2026-10-09) hold in the queue
   with no red-team verdict contradicting; the pending-ratification
   dependency is stated explicitly. PASS iff verified in the queue.
2. @1181 (0-based, row a6_10): the span @1180–@1185 ('77 78 94 82 06 06')
   parses as 'le ver | ne mentent' (94='ne' + 82='m' + 06@1184='ent' syllable
   + 06@1185='ent' finite 3pl ending = mentir 3pl), with 'le ver''s clause
   role stated. PASS = parse stated; else fence with stated cause.
3. @1352 (0-based, row a7_05): the span @1351–@1356 ('77 78 94 82 06 52')
   parses as 'le ver | ne ment [52]' (94='ne' + 82='m' + 06='ent' syllable =
   mentir 3sg 'ment'), with 'le ver''s clause role stated. PASS = parse
   stated; else fence with stated cause.
4. LEFT EDGES fenced or parsed: @1181 left edge '32 48 59 37'
   (@1176–@1179; 59='est' battery-promoted); @1352 left edge '62 48'
   (@1349–@1350; 62='il' battery-promoted, 48='e' letter-promoted;
   lever 'elever'-overlap fenced to lever-77-78, not re-litigated).
5. ADVERSES ANSWERED: (a) 94/06 ratification pending — stated, not ignored;
   (b) 'ne mentent' 3pl @1181 with singular 'le ver' — role stated or fenced;
   (c) 'ne ment [52]' @1352: intransitive mentir + bare [52] — fenced with
   stated cause; (d) lever-77-78 rival (NULL 2026-10-08; '…lement' closed
   2026-10-09 by lever-lement-rival) — fenced, not re-litigated.

## Standing values used (§7 plus queue verdicts)

- Banked: 11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que.
- Promoted/granted: 87=ce, 64=qui, 96=par, 17=fois, 79=tout, 00=pour, 84=on,
  47=ce; 37/32/42 predicative frames (value open).
- Provisional: 59=est, 77=le. Battery-promoted: 94=ne, 06=ent, 59=est
  (est-59-frames), 62=il (il-62), 48=e (letter).
- 78='ver' is a red-team-graded LEAD (R16-005) — the claim under test, never
  used as granted. The ne-le-1075 KILL is respected (no verb-head claimed).
  Kills/splits/holds per §7 hold.

## Method

Re-derived both windows from the repaired stream in-session (0-based pair
indices; rows confirmed: @1181 on a6_10, @1352 on a7_05). Ran a stream-wide
census of the trigram '94 82 06' and the 5-gram '77 78 94 82 06'. Cross-checked
against the ent-06 F1/F2 frames, the host-census 06 rule, and the
lever-lement-rival census (2026-10-09).

## Window-level evidence (@-offsets are 0-based repaired-stream pair indices)

### @1181 (a6_10): `74 32 48 59 37 | [77]@1180 [78]@1181 | [94]@1182 82 06 06 | 59 42 06 84 59 46 …`

Re-derived in-session. The trigram '94 82 06' occurs exactly 3x stream-wide:
@578, @1182, @1353. At @1182 the next two pairs are '06 59': '94 82 06 06'
= 'ne' + 'm' + 'ent' + 'ent' = 'ne mentent' (mentir 3pl). This is ent-06's
promoted F2 frame (CLEAN), independently confirmed by lever-lement-rival
(2026-10-09): trigram @1182 = 'ne mentent', consistent with ent-06.

'le ver' = clean NP (77='le' provisional, 78='ver' LEAD under test).
Clause role: 'ne mentent' is 3pl, so 'le ver' (singular) cannot be its
subject. 'le ver' reads as a detached/topic NP; the verb carries an
unexpressed 3pl subject ('(ils) ne mentent'). Zero-subject clauses are
fenced lane-wide; the number mismatch is fenced here with that cause.

Left edge: '32 48 59 37' — with 59='est' (battery-promoted) and 37's
predicative frame granted, 'est 37' is at least partially parseable
(copula + predicative); 32/48/74 stay open. Fenced with cause.
Right edge: '…06 06 59…' = '…entent est…' — 'est' 3sg after 3pl 'mentent'
marks a clause boundary; 42 open. Fenced.
**PASS (clause 2): 'le ver | ne mentent' parses under the settled values,
with the stated fences.**

### @1352 (a7_05): `62 48 | [77]@1351 [78]@1352 | [94]@1353 82 06 52 37 64 35 …`

Re-derived in-session. The 5-gram '77 78 94 82 06' occurs exactly 2x
stream-wide: @1180 and @1351 (lever-lement-rival, 2026-10-09) — the two
flagship sites only. At @1353 the next two pairs are '52 37': '94 82 06'
= 'ne' + 'm' + 'ent' = 'ne ment'. Under the host-census 06 rule (2026-10-09),
06@1355's left neighbor is 82='m' (a letter, not a verb stem), so 06 is a
syllable here: 'ment' = mentir 3sg. 'le ver' (3sg) is then the grammatical
subject of 'ne ment' — number agrees: 'le ver ne ment' = 'the worm does not
lie'. **The flagship frame predicted 'ne ment(ent)' at this site and the
settled values deliver exactly 'ne ment'.**

Clause role of 'le ver': subject of 'ne ment' (agreement holds).
[52]: 'ment' + bare [52] is the known strain — mentir is intransitive, so
[52] as a direct object needs a rescue (elided 'a', or 52's class). 52 is
open but noun-profiled ('la 52' x3); the right edge '52 37 64' = '[52]
[37-predicative] qui…' (64='qui' promoted) gives an NP + relative-clause
shape. The object slot is fenced with stated cause; it does not touch the
flagship frame.
Left edge: '62 48' — with 62='il' (battery-promoted) and 48='e' (letter),
'il e' composes no word; the 'elever' overlap (48+77+78) is fenced to the
lever-77-78 NULL battery, not re-litigated. The '…lement' word-composition
is closed at battery grade by lever-lement-rival (no host for the
pre-syllable at 62@1349='il', with 48@1350 intervening).
**PASS (clause 3): 'le ver | ne ment [52]' parses under the settled values,
with the stated fences.**

## Per-clause pass/fail

1. SETTLED VALUES — **PASS.** ne-94 promote 2026-10-07 and ent-06 promote
   2026-10-08 verified in battery-queue.json; host-census rule (2026-10-09,
   promote) consistent with both windows; no red-team verdict on 94/06/78
   contradicts. Ratification pending stated explicitly.
2. @1181 'le ver | ne mentent' — **PASS** (fenced: detached-NP role for
   'le ver', unexpressed 3pl subject, left/right edges fenced).
3. @1352 'le ver | ne ment [52]' — **PASS** (fenced: [52] object strain,
   left edge fenced).
4. LEFT EDGES — **PASS.** @1181: 'est 37' partially parseable, remainder
   fenced; @1352: 'il e' fenced, lever-overlap fenced to lever-77-78 NULL.
5. ADVERSES — **ANSWERED.** (a) ratification pending stated; (b) 3pl number
   fence stated; (c) [52] strain fenced with stated cause; (d) lever-77-78
   NULL fenced, '…lement' closed by lever-lement-rival (promote, 2026-10-09),
   nothing re-litigated.

## Adverses answered

- Gate 'gated on 94/06 settling — do not run before': CLEARED at battery
  grade (ne-94 promote, ent-06 promote + host-census rule); red-team
  ratification remains pending and is stated, not hidden.
- lever-77-78 rival (NULL 2026-10-08): FENCED at both windows; the rival's
  strongest route ('…lever | ne me [06-verb]…') is consistent with the same
  settled values (lever-lement-rival clause 3) — coexistence fenced, not
  re-argued.
- '…lement' word-composition rival: CLOSED at battery grade today
  (lever-lement-rival PROMOTE, finding grade): no standing value at 59@1178
  ('est') or 62@1349 ('il') hosts the missing pre-syllable.

## Verdict: PROMOTE (finding grade)

Both flagship windows materialize the predicted French string under the
settled battery-promoted values, byte-exactly, at the two and only two
stream sites of the 5-gram '77 78 94 82 06' (census: x2 @1180/@1351):
'le ver ne mentent' @1181 (ent-06 F2 CLEAN frame) and 'le ver ne ment [52]'
@1352 (number-agreeing subject). All clauses pass; all adverses answered
(re-parsed cleanly or fenced with stated cause — never ignored). No red-team
verdict contradicted; ne-le-1075 KILL respected; §7 intact.

Scope: this promotes the finding only. No value or class is promoted or
killed: 78='ver' stays a red-team LEAD (claim under test, never granted),
94='ne' and 06='ent' stay battery-promoted pending red-team ratification.

## Constraints respected

R5005, sealed gate instances, and the red-team adjudication queue untouched.
§7 banked/promoted/provisional/killed/split/held values respected; 67 sole
polyvalence untouched; uniformity law and canonicality caveat noted (68 of
70 upstream row offsets unvalidated). canonical.py never used. No invented
numbers: every count re-derived from the repaired 1,847-pair stream
in-session (trigram '94 82 06' x3 @578/@1182/@1353; 5-gram x2 @1180/@1351).
