# Battery report: faire-86-causative-test

- Target id: `faire-86-causative-test`
- Claim: "test 86 for causative 'faire'-shape (bare-infinitive-complement valency in its contact profile across its 32 windows)"
- Date: 2026-10-09
- Worker: subagent 4d87fa30-b3bd-4ff9-95be-ea263d9f09d7
- Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` +
  `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`).
  1,847 pairs / 96 distinct groups re-derived. Never used `canonical.py`.
  R5005 untouched. No invented data. No sealed gates, no red-team queue contact.
- Lock: `code/crowd17/next-token/locks/faire-86-causative-test.lock` created
  2026-10-09T10:16:19Z; no prior/stale lock existed; deleted on completion.

## Bar (verbatim, pre-registered from battery-queue.json BEFORE testing)

"iff 86 names a causative value taking bare-infinitive complements, @1376's
fenced conditional verb-89 parse ('pour faire [89-inf], on...') activates and
the conflict picture changes; else fence the conditional permanently"

Numbered pass/fail clauses (restated, not modified):

1. Iff 86's contact profile across its 32 windows shows bare-infinitive-
   complement valency (causative 'faire'-shape), the fenced conditional
   verb-89 parse of @1376 ('pour faire [89-inf], on...') ACTIVATES and the
   conflict picture changes.
2. Else (no such valency in 86's profile), the conditional is FENCED
   PERMANENTLY.

Adverses: none stated; 86's value open.

## Method

1. Replicated the repaired parse in Python (offsets + upstream text, same
   tokenization as `repair_parse.py`). Asserted 1,847 pairs; n(86) = 32
   re-derived (indices @175/@300/@431/@553/@557/@661/@671/@716/@728/@799/
   @867/@878/@889/@899/@948/@951/@962/@1002/@1099/@1128/@1131/@1134/@1147/
   @1335/@1345/@1375/@1391/@1458/@1506/@1739/@1792/@1825, 0-indexed).
2. Honored the stem-86 NULL's structural split (determiner-life vs stem-life)
   as a test boundary, not re-litigated: causative valency can only live in
   86's verb-life, so the discriminating census is the complement profile of
   the 86-29 infinitive subset plus every bare-86 complement position that
   could host a bare infinitive.
3. Values used (standing only): pencil 11=la, 70=pre, 82=m, 34=i, 29=er,
   40=e, 46=que; granted 87=ce, 64=qui, 96=par, 17=fois, 79=tout, 00=pour
   (A9), 84=on (A15, unconditioned), 47=ce; battery-promoted 24=modal,
   06='ent', 48='e' (letter), 94='ne', 30='pas'; provisional 59=est;
   86 INF-class (A9 class-level, value open); 67 et/veut positional rule
   (sole polyvalence, §7).

## Window-level evidence (repaired stream, @-offsets)

### 86's verb-life: the 86-29 infinitive subset (n=4) — the only windows that can carry causative valency

- @431 (row a2_09): `63 77 [86] 29 82 16 78` = "[63] le [86]er m[16] [78]".
  Infinitive of 86 followed by 82='m' (pencil): "[86]er m…". A postposed
  m-clitic after the infinitive is ungrammatical in French ("faire me X"
  impossible; correct order "me [86]er" = 82-86-29, absent here). Under
  causative 86: no bare-infinitive complement; the m-follower resists the
  reading. NOT a causative leg.
- @1375 (row a7_06): `98 00 [86] 29 89 84 92` = "[98] pour [86]er [89] on [92]".
  The conditional's own window. Bare-infinitive-complement reading of 89
  ("pour faire [89-inf]") requires 89 = infinitive here. 89's class is the
  known conflict (noun legs at 11/14 windows per val-89-mirror vs
  infinitive-slot legs @221/@985 under 24-modal), already escalated to the
  red team (class-89-adjudicate packaging PROMOTE). Under standing values,
  "pour [86]er [89-noun/adv], on…" parses cleanly with NO causative
  assumption (noun-89-1377-adjudicate: hard non-verb window, unkillable).
  The infinitive reading needs the very causative-86 this battery tests.
  CANDIDATE ONLY — class disputed, viable non-causative parse.
- @1391 (row a7_07): `29 67 [86] 29 89 16 76` = "[29] veut [86]er [89] m[16] [76]"
  (67='veut' by the positional rule: follower 86-29 is infinitive-shaped).
  "veut faire [89] m[16]" — same structure as @1375: infinitive-89 needs
  causative 86; noun-89 needs no extra assumption; @1391's tail is gated on
  16's open class (frame-82-16 queued). CANDIDATE ONLY — class disputed,
  gated on 16.
- @1825 (row a8_11): `97 00 [86] 29 82 38 83` = "[97] pour [86]er m[38] [83]".
  Same postposed-m shape as @431: resists the causative reading. NOT a
  causative leg.

Verb-life tally: 0 independent bare-infinitive-complement windows; 2
disputed candidates (@1375, @1391), both requiring 89 = infinitive, a class
that is independently conflicted with viable noun/adverb parses; 2 windows
(@431, @1825) whose postposed 82='m' actively resists the causative reading.

### Exhaustive complement sweep across all 32 windows

- Bare 86 followed directly by a verb-stem (89/85/03/76/68, the open
  verb-class inventory): ZERO occurrences in the entire stream.
- Causative-adjacent frames ("se 86", "on 86", "m' 86"): none. Only 47
  adjacent window is @1345 (`47 [86] 66`, determiner-life context, 47='ce').
- Preposition-mediated causative complements (86-46 'que', 86-39 'a'):
  86's successors include no 46 and no 39 (full successor census: 29 x4,
  56 x4, 24 x2, 01 x2, 52 x2, 66 x2, 21/91/59/94/50/48/44/70/78/06/16/96/
  20/67/71/12 x1). The 86-24 x2 windows (@671 '11 86 24', @1131 '[86] 24')
  are determiner-life ("la [86] [24-modal]") and cannot carry verb valency.
- '00 86 56' x4 formula (@962/@1002/@1506/@1792): "pour [86] [56]".
  56's census (n=23, mixed profile: pre {86 x4, 98 x2, 35 x2, 48 x2,
  46 x2, …}, suc {87 x2, 47 x2, 37 x2, 69 x2, 41 x2, 32 x2, 30 x2, …})
  is class-ambiguous, not infinitive-shaped. Under 86='faire' this is at
  best "pour faire [56]" (direct-object complement), never a bare
  infinitive complement. Consistent-with, not evidence-for.
- The remaining 28 bare-86 windows are the stem-86 determiner-life
  (pre=00 x12, pre=77 x5, etc.); a verb 'faire' cannot live there. The
  split is respected, not re-litigated.

### Coordination (not re-litigated)

- val-89-mirror (NULL, 2026-10-08): independently tested this window and
  found "86 is INF-class with no causative/perception evidence", killing
  infinitive-89 at @1375 on that premise. This battery is the independent
  test of that premise and CONFIRMS it on the full 32-window profile:
  no bare-infinitive-complement window for 86 exists outside the two
  class-disputed 89 candidates. No circularity: the conclusion rests on
  86's own census, not on 89's class verdict.
- noun-89-1377-adjudicate (NULL, 2026-10-08): "pour [86]er [89-noun/adv],
  on…" stands as a hard non-verb window; its follow-up list (this target
  #1, adv-89-1376, tail-1376-on92) is untouched by this verdict.
- stem-86 (NULL, 2026-10-08): determiner-life vs stem-life split and its
  three follow-ups (le-86-determiner-subset, homophone-86-split,
  reseg-86-problem-windows) untouched; no standing verdict contradicted.

## Adverses disposition

"None stated; 86's value open" — answered: 86's value remains open. The
structural adverse from stem-86 (determiner/stem split) was respected as a
test boundary — causative valency was tested only where a verb could carry
it (the 86-29 verb-life plus the full complement sweep). No value is named,
none promoted, none downgraded.

## Per-clause pass/fail

1. Bare-infinitive-complement valency for 86 across its 32 windows: **FAIL**.
   Exhaustive census: 0 independent bare-infinitive-complement windows.
   The only two candidates (@1375, @1391: 86-29-89 x2) both require
   89 = infinitive, a class that is independently conflicted (red-team
   docket) and has viable noun/adverb parses needing no causative
   assumption. The other two verb-life windows (@431, @1825) have
   postposed 82='m' followers that actively resist the causative reading.
   Clause 1 of the iff is false at the lane's distributional standard.
2. Fence the conditional permanently: **PASS** (consequence executes).
   The 'pour faire [89-inf], on…' verb-89 parse of @1376 is PERMANENTLY
   FENCED: no leg anywhere in 86's 32-window profile supports a
   causative-'faire' valency, and the two candidate windows parse cleanly
   without it.

## Verdict: KILL

Headline: 86's causative-'faire'-shape is excluded at battery grade, and
with it the fenced conditional verb-89 parse of @1376 ('pour faire
[89-inf], on…') is PERMANENTLY FENCED. This is not a null: the bar was
fully testable, the census exhaustive (all 32 windows, every complement
position enumerated), and the negative finding is decisive at the bar's
own terms — the iff's negative arm resolved. The 89 class conflict itself
is unchanged and stays with the red team (class-89-adjudicate, already
packaged PROMOTE); nothing is downgraded and no standing verdict is
contradicted.

Re-open condition (not a follow-up — kills close the avenue): if the red
team resolves 89's class conflict with an infinitive verdict at @1375 or
@1391 (polyvalence or otherwise), the causative premise changes and this
kill re-opens on that new evidence. Nothing else re-opens it.
