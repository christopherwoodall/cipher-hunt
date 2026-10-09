# Battery report: feeder-ceci-47-45

- Target id: `feeder-ceci-47-45`
- Claim: "47-01 (@195) and 45-01 (@984) read 'ceci', doubling the ceci-composition evidence for ci-01-value"
- Date: 2026-10-08
- Worker: battery worker (session 517ca5fd-9154-47cc-afbc-5730a96ca777)
- Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json +
  data/upstream-ct_R5005.txt, parsed per code/side-keyhunt/repair_parse.py).
  All @-offsets are 0-based repaired-stream indices of the 01 token.
  canonical.py never used. R5005, sealed gates, red-team queue untouched.
- Lock: code/crowd17/next-token/locks/feeder-ceci-47-45.lock (created at start,
  deleted at end; no prior lock existed).
- Scope note: this battery is a FEED for the bound '-ci' reading (ci-bound-01,
  verdict null). It does not re-litigate ci-01-value's kill (unconditioned
  01='ci'/'faisant' killed by battery-ci-01-value).

## Bar (verbatim, pre-registered before testing)

"promote-feed iff (a) @195 47-01-21-60 parses as ceci [21] [60] with 21/60's
slots stated; (b) @984 45-01-24-89 parses as ceci [24] [89] with 24/89's slots
stated; (c) neither window forces non-ceci. Null if either window resists with
a stated cause (feeds back as adverse to ci-01-value)"

Numbered pass/fail clauses (restated before testing, not modified after):

1. (a) The @194-197 window (01 at @195) parses as "ceci [21] [60]" with 21's
   slot and 60's slot both stated.
2. (b) The @983-986 window (01 at @984) parses as "ceci [24] [89]" with 24's
   slot and 89's slot both stated.
3. (c) Neither window forces non-ceci: no reading forces 47-01 or 45-01 to a
   non-ceci value.

## Method

1. Re-derived the repaired parse in-session (1,847 pairs confirmed).
   Window contents verified byte-level in-stream (not cited from memory):
   @194-198 = `47 01 21 60 08` (row a2_00); @983-987 = `45 01 24 89 48`
   (row a6_01). ce+01 bigram census re-derived: 87-01 x2 (@344, @1028),
   47-01 x1 (@194), 45-01 x1 (@983) — matches ci-bound-01 exactly.
2. Tested each window for a grammatical full-context parse under the bound
   reading (47='ce' A4 granted; 45='ce' A11 HOLD; 01 = bound '-ci' in
   ce-contexts, the hypothesis under feed), against standing verdicts only:
   21 = NOUN class (de-frame-21-class PROMOTE), 24 = finite modal verb
   (ne-24-profile PROMOTE, class-level), 89 = verb-frame (A8 grant),
   98 = 'vient' (vient-98-name PROMOTE), 60 adjective single-value KILLED
   (adj-60). 60's verbal arm is queued (verb-60); adjective/verb polyvalence
   is a red-team-only declaration per §7.
3. Checked the listed adverses against the same standing verdicts.

## Window-level evidence

### Clause 1 — @194-197: `47 01 21 60` (row a2_00)

Full ±10 context (@185-205):
`00 33 16 00 66 24 87 98 56 47 01 21 60 08 67 76 87 11 92 63 42`
= "[00-pour] [33] [16] pour(00) [66] [24-modal] ce(87) vient(98) [56]
ce(47) [01] [21] [60] [08] et/veut(67) [76] ce(87) la(11) [92] …".
Per ne-24-profile, 24-87 is a clause-final modal + "ce"-opener, so a clause
boundary sits after @190; the new clause opens "ce(87) vient(98) [56]
ceci(47-01) …".

Slots (standing verdicts):
- 21 = NOUN, class-level (de-frame-21-class PROMOTE 2026-10-08; value
  unnamed; 21-67 x8 explained by the §7 positional rule). 21 therefore
  CANNOT fill a verb slot. The provisional "[21] in the verb slot" reading
  that ci-bound-01's W2 left open is dead under the promotion.
- 60's slot at this window is undeterminable at battery grade: the
  single-value adjective claim is KILLED (adj-60: @1338 'qui 60 08' and
  @700 'ne 60 12' force 60 verbal); the verbal arm is queued (verb-60);
  the infinitive shape is attested only formula-bound ("vient de me
  parvenir" thirds, frame-vient-parvenir — and this @196-197 21-60 is
  NOT formula-bound: the formula is 98-83-82-96-21-third, here we have
  98-56-47-01-21-60); any adjective/verb polyvalence needs a red-team
  declaration per §7.

Candidate clause parses of "ceci [21-noun] [60]":
- 60 finite verb: "ceci [noun] [verb]" — wrong word order for a plain
  clause. Ungrammatical.
- 60 adjective: "ceci [21-N] [60-adj]" — a verbless NP fragment. The only
  rescue is dislocation + a later verb: "ceci, [21] [60] [08] veut [76]"
  needs (i) 60 adjectival (red-team polyvalence act), (ii) 08 as object
  (08's class open, stem-08 queued), (iii) 67='veut' (needs @200=76
  infinitive-shaped — 76's shape unknown), (iv) dislocation "ceci"
  without resumption (strained). Four unstated assumptions plus a
  red-team act: not battery grade.
- 60 infinitive: "ceci [noun] [inf]" — no governing verb; the
  exclamatory-infinitive reading needs "[inf] ceci" order. Ungrammatical.

Result: RESIST with stated cause. 21's promotion to NOUN kills the only
clause shape ("ceci [21-verb]") under which the bigram's downstream
context parsed; 60's slot cannot be stated at battery grade. The
resistance is localized to [21]/[60], downstream of the 47-01 bigram —
it does not force "ceci" false at the bigram itself.

### Clause 2 — @983-986: `45 01 24 89` (row a6_01)

Full ±10 context (@974-994):
`45 08 01 00 92 07 76 47 78 45 01 24 89 48 01 76 49 24 26 30 03`
= "ce(45) [08] [01] pour(00) [92] [07] le(77) ce(47) [78] ce(45) [01]
[24] [89] [48] [01] le(77) [49] [24] [26] pas(30) [03] …".

Slots (standing verdicts):
- 45 = 'ce' (A11 HOLD, allophone tier) — dependency stated, not hidden.
- 01 = bound '-ci' (the hypothesis under feed; 01 valueless elsewhere per
  ci-bound-01 clause 2).
- 24 = finite verb, modal-shaped (ne-24-profile PROMOTE, class-level;
  value unnamed). The 24-89 contact at @985 is one of the three
  modal+infinitive-frame contacts (@221/@985/@1497).
- 89 = verb-frame (A8 frames grant; value open) — infinitive-shaped
  complement.

Parse: "…ce(47) [78] ceci(45-01) [24-modal] [89-inf]…" = "ceci [modal]
[inf] …" ("ceci peut [inf]…"-shaped). Clean, grammatical, one clean
"ceci [verb]" window. The fork-78-45 watch item is vacuous here:
@982=78's 'ver' promotion is NULL, so clause (a)'s antecedent is false.

Result: PASS (conditional on the A11 HOLD, as in ci-bound-01 W1).

### Clause 3 — neither window forces non-ceci

- @194-195: 47='ce' is granted (A4); the rival "ce faisant [21]" is dead
  (01='faisant' killed generally by battery-ci-01-value); 01-valueless
  leaves "ce [01]" unparsed — an unparsed residue, not a forced rival
  value. Nothing forces 47-01 ≠ ceci.
- @983-984: rival 45='dict' is NULL (not promoted); nothing forces
  45-01 ≠ ceci.

Result: PASS.

## Per-clause pass/fail

1. (a) @195 parses as "ceci [21] [60]" with slots stated: RESIST.
   Stated cause: 21 = NOUN (promoted) cannot take the verb slot; 60's
   slot is undeterminable at battery grade (adjective killed
   single-value; verbal queued; infinitive formula-bound only;
   polyvalence red-team-only).
2. (b) @984 parses as "ceci [24] [89]" with slots stated: PASS
   (24 = finite modal verb, promoted class; 89 = infinitive verb-frame,
   A8; conditional on A11).
3. (c) Neither window forces non-ceci: PASS.

## Adverses

1. "01-24 @984 (ceci-24 needs 24 named - see disc-01-24-ci-X)": ANSWERED.
   24 named as finite verb, modal-shaped (ne-24-profile PROMOTE,
   class-level); at @985 it takes the infinitive-frame complement 89
   (one of x3 24->89 contacts). Compatibility note: ne-24-profile fenced
   "01 24" x3 to disc-01-24-ci-X as "nominal-01 + finite-24" — under the
   bound reading the subject is the composed "ceci" (45-01), not 01
   alone; 24's slot is unaffected either way. disc-01-24-ci-X is already
   queued; not duplicated here.
2. "ceci [21] @195 needs 21's slot (21->67 x8)": ANSWERED. 21's slot =
   NOUN (de-frame-21-class PROMOTE 2026-10-08, class-level; value
   unnamed). 21-67 x8 is explained by the §7 positional rule (noun
   subject + veut / noun + et coordination; @1423 'veut'+infinitive
   positively selects noun). Consequence: the verb-slot reading of [21]
   at @195 is dead — this is the stated cause of clause 1's resistance.

## Verdict: NULL

Per the bar's explicit null condition: clause (a) resists with a stated
cause. The resistance is downstream of the 47-01 bigram (at [21]/[60])
and does not force "ceci" false at the bigram, so this is not kill-grade
for the claim; but the bar's (a) is not met, so this is not a promote-feed
either. Feedback to the bound-ci reading: the @195 locus cannot serve as
a clean ceci+verb window while 21 is nominal and 60's slot is open; the
@984 locus stands as the one clean ceci+modal+infinitive window.

No standing red-team verdict is contradicted or downgraded: A4 (47='ce'),
A11 (45='ce' HOLD), A8 (89 verb-frame), the 21-noun promote, the 24-modal
promote, the 60-adjective kill, and the ver-78/fork-78-45 NULLs are all
relied on, not challenged. No escalation needed.

## Follow-up targets (nulls regenerate work)

None of these duplicate queued targets (checked: ceci-984-195-pair,
residual-345-06, residual-1029-infinitive, disc-01-24-ci-X, verb-60,
poly-60-redteam, stem-08 are all already queued).

1. **ceci-195-nounslot** (priority 3): re-test the @194-200 clause with 21
   fixed nominal (promoted). Bar: "resolve iff a full-clause parse of
   47-01-21-60-08-67-76 exists with 21 nominal and <=1 unstated
   assumption; else fence @195 as a [21]/[60]-driven residual with stated
   cause (not a 47-01 residual)." Adverses: 60's slot gated on verb-60 /
   poly-60-redteam; 08 open (stem-08); 67 positional needs 76's shape.
   Evidence: clause 1 of this report.
2. **bound-ci-984-standalone** (priority 2): narrow the bound-ci claim to
   the single clean locus @984. Bar: "promote-restricted iff @983-986
   parses as ceci [24-modal] [89-inf] with the A11 dependency stated and
   zero contradictions in ±10; the @195 leg stays fenced per this
   battery." Adverses: A11 HOLD; fork-78-45 watch item (vacuous while
   ver-78 NULL). Evidence: clause 2 of this report.
3. **slot-60-at-197** (priority 3): name 60's slot at the free
   (non-formula) 21-60 window @196-197. Bar: "resolve iff exactly one of
   verb/adjective/infinitive parses @194-200 with 21 nominal and <=1
   unstated assumption; coordinate with verb-60 and poly-60-redteam
   without duplicating their bars; if polyvalence-gated, fence with
   stated cause." Adverses: polyvalence is red-team-only per §7.
   Evidence: clause 1 of this report; adj-60 kill windows @1338/@700.
