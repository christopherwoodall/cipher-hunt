# Battery report — x-33-laisser-test (X = 'laisser' discriminator for 33={dire,[X]er})

Worker: battery-worker-967acee4. Date: 2026-10-08.
Lock: `code/crowd17/next-token/locks/x-33-laisser-test.lock` created
2026-10-08T14:08:42Z, no prior lock existed; deleted on completion.
Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` +
`data/upstream-ct_R5005.txt`), parsed per `code/side-keyhunt/repair_parse.py`
(replicated, not `canonical.py`). R5005 not touched. Every count below
re-derived from the stream in this run.

Coordination: this battery is dire-33-set's follow-up #1 (null, 2026-10-08)
and consumes erstem-33-id (null, 2026-10-08) as prior evidence. It does NOT
re-run the valency/candidate sweep — it tests ONLY the two infinitive gates
(16, 85) and the zero-contradiction condition. No duplication.

## Bar (pre-registered verbatim, from battery-queue.json)

`name X='laisser' iff 16/85 resolve as infinitives in the stem frames with zero contradiction; else name X from profile or record as family`

Numbered clauses (pre-registered BEFORE testing, not modified after):

1. 16 resolves as an infinitive in the stem frame @1480 (`33-29-82-16`).
2. 85 resolves as an infinitive in the stem frame @1234 (`33-29-85`).
3. Zero contradiction: no window contradicts the infinitive readings.
4. If clauses 1-3 hold, name X='laisser'; else name X from its contact
   profile, or record X as a family.

## Method

Re-parsed the repaired stream (assert 1,847 pairs). Re-derived: the five
`33-29` stem windows; a stream-wide X-29 stem census; the full 28-window
profile of 16 and the full 15-window profile of 85; the 62-16 / 12-16 /
16-00 / 79-85 bigram sets. Checked queue state for frame-82-16 and stem-85
(both still `queued`). Checked ver-78's recorded verdict for the prononcer
trigger.

Standing values used: 29="er", 82="m", 12="n" (banked); 87="ce", 46="que",
00="pour" (A9), 79="tout" (A5), 47="ce" (A4 allophone tier), 84="on" (A15),
94="ne" (promoted); 67 et/veut positional rule; 62="on" cited as STRONG
LEAD only (collision-62-84 queued, not promoted); §7 sole-polyvalence law
throughout. A10 (33+29 stem/whole HOLD) respected.

## Window-level evidence (@-offsets are repaired-stream pair indices)

Stem windows re-derived (identical set to the three prior batteries):
- @273 (a2_03) `11-06-67-33-29-89-84` — "veut [X]er [89] on"
- @626 (a4_01) `14-59-37-33-29-87-78` — "[37] [X]er ce [78]"
- @1232 (a7_01) `48-29-47-33-29-85-56` — "ce/se [X]er [85] [56]"
- @1424 (a7_08) `33-21-67-33-29-87-63` — "dire [21], veut [X]er ce [63]"
- @1477 (a7_10) `60-06-67-33-29-82-16-98` — "veut [X]er m[16] [98]"

Context claims verified fresh: 33-29 x5 is the corpus's top -er stem
(next 86/06 at 4x); the only 47-governed stems stream-wide are 11 and 33;
`67-33-29` x3 and `33-29-87` x2 byte-identical; 33 is the only stem taking
87="ce" directly after "-er".

16's profile (n=28): stem-frame occurrence @1480 (a7_10)
`33-29-82-16-98-62-46` = "[X]er m[16] [98] [62] que"; control parallel
@434 (a2_09) `86-29-82-16-78-63-45` (86 stem). Class signals:
- `62-16` x4 (@83, @659, @1142, @1298): 62="on" is a standing STRONG LEAD
  (on-84 adverse, collision-62-84 queued) → subject + 16 = finite-verb shape.
- `12-16` x3 (@242, @844, @1431): 12="n" BANKED → "n'[16]" = literary
  negation, which selects a finite verb.
- `16-00` x4 (@187, @659, @844, @1246): 00="pour" A9 → "[16] pour [inf]"
  is noun-shaped (noun + pour + infinitive).
- `82-16` x11: 82="m" banked → "m'[16]" needs 16 verb-shaped
  (vowel-initial; a noun after "m'" is ungrammatical).

85's profile (n=15): stem-frame occurrence @1234 (a7_01)
`47-33-29-85-56-10-03` = "ce/se [X]er [85] [56]". Class signals:
- `79-85` x2 (@54, @595): 79="tout" PROMOTED (A5) → "tout [85]" is
  noun-shaped (bare "tout + infinitive" is ungrammatical French).
- `24-85` x5 (@733, @956, @1439, @1694, @1755): 24's class open; recorded,
  not adjudicated.
- Stem-adjacent `29-85` x3 (@97, @375, @1234) — consistent with 85 as a
  post-"-er" complement of either class.

Gate owners' state: frame-82-16 `queued` (16's value open); stem-85
`queued` (85's value open). Neither has resolved.

## Per-clause pass/fail

1. 16 = infinitive in the stem frame: NOT MET (gated). 16's value is open.
   Worse than open: active contradictions. The `62-16` x4 frames
   (62="on" strong lead) and `12-16` x3 frames (12="n" banked) are
   finite-verb-shaped, while `16-00` x4 frames are noun-shaped. Under the
   §7 sole-polyvalence law these cannot all be true of one value; the
   infinitive reading has no positive frame anywhere in 16's 28 windows.
2. 85 = infinitive in the stem frame: NOT MET (gated). 85's value is open.
   The `79-85` x2 frames (79="tout" promoted) are noun-shaped and
   contradict the infinitive reading.
3. Zero contradiction: FAILS at current evidence. Both gates carry
   observed contradictions (clause 1 and 2 findings above). The
   contradiction is not merely "unresolved" — it is affirmative and must
   be adjudicated by the gate owners (frame-82-16, stem-85) before the
   laisser lead can proceed.
4. Fallback — name X from profile / record as family: FAMILY RECORDED.
   @1477's post-verbal "me" frame (82="m" banked) forces X into the
   causative -er class independent of 16's class: "veut [X]er me [V/N]"
   is ungrammatical for every non-causative -er verb under every
   16-class assumption (clitic "me" cannot follow a non-causative
   infinitive; "m'" + noun is ungrammatical). Adopting erstem-33-id's
   valency sweep (not re-run): the French -er causative class is uniquely
   {laisser} ('faire' excluded: not -er; donner/montrer/envoyer/prononcer
   die at the V+me+order frame). X is therefore recorded as the
   causative -er family — 'laisser' at LEAD strength, gated, NOT named at
   promotion grade. No window forces X='laisser' false; no cleaner rival
   is demonstrated.

## Adverses disposition

- "needs 16/85 = infinitives": NOT answered — both values open, both
  gates still queued; contradictions recorded above for the gate owners.
- "'prononcer' rival if ver-78 lands 'verdict'": FENCED with cause.
  ver-78 returned NULL (2026-10-08); R16-005 grades 78='ver' LEAD,
  not settled — the revival trigger did not fire. Independently,
  prononcer dies at @1477's V+me+order frame under every 16-class
  assumption (82="m" banked), so the rival is fenced regardless of
  ver-78's future.
- "erstem-33-id still queued - coordinate": COORDINATED — erstem-33-id is
  decided (null, 2026-10-08); its windows, census, and candidate sweep
  were adopted as prior evidence; this battery ran only the gate test.

## Standing-verdict check

No contradiction with any standing verdict: A10 HOLD respected (both 33
faces retained); §7 banked/promoted values and the sole-polyvalence law
untouched; 62="on" cited as lead-grade only (its collision battery is
queued); the dire-33-set / croire-33-tiebreak / erstem-33-id nulls are
not re-litigated. Nothing to escalate on contradiction grounds.

## Verdict: null

The bar's naming condition cannot be evaluated (gates open) and its
zero-contradiction condition currently fails on affirmative evidence.
Per the task brief the gate is recorded, not forced. X is recorded as
the causative -er family ('laisser' at LEAD strength, gated on 16/85 and
on adjudication of the contradictions below). Not a kill: no window
forces the stem reading false and no cleaner rival is demonstrated.

## Follow-ups (null regenerates work)

1. **laisser-gate-16** — claim: the laisser lead is re-testable once
   frame-82-16 names 16's class. Bars: (a) 16's class named with all 28
   windows parsing; (b) the `62-16` x4 / `12-16` x3 finite-verb signals
   vs `16-00` x4 noun signals adjudicated without lane-illegal
   polyvalence (§7); (c) @1480 parses as "[X]er me [inf]" with zero
   contradiction. Evidence: 16's profile in this report. Adverses: 62=
   "on" is lead-grade only (collision-62-84 queued); 16's class is
   frame-82-16's lane — coordinate.
2. **laisser-gate-85** — claim: the laisser lead is re-testable once
   stem-85 names 85. Bars: (a) 85 named with all 15 windows parsing;
   (b) `79-85` x2 (79="tout" promoted) and `24-85` x5 adjudicated;
   (c) @1234 parses as "se laisser [85=inf]" with zero contradiction.
   Evidence: 85's profile in this report. Adverses: stem-85 owns the
   value — coordinate, do not duplicate.
3. **gate-satisfiability-16-85** — claim: the infinitive gates are
   satisfiable at all. Bars: (a) every window of 16 (28) and 85 (15)
   assigned noun / finite-verb / infinitive under the §7
   sole-polyvalence law; (b) banked-value frames listed separately from
   lead-grade frames; (c) binary verdict: gates satisfiable (follow-ups
   1-2 proceed) or unsatisfiable — if a banked-value frame forces a
   non-infinitive class, the laisser lead is KILLED cleanly and X must
   be re-profiled. Evidence: this report's profiles. Adverses: duplicates
   neither frame-82-16 nor stem-85 (those name values; this tests gate
   satisfiability).
