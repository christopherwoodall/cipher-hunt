# Battery slot-1232-fence

- Target id: `slot-1232-fence`
- Claim: fence @1232's '47-33-29' contact as a 'ce' + verb residual under 33 = verb
- Date: 2026-10-09
- Worker: battery worker (agent b87622fa-545b-4f61-b27e-65f30079d5b0)
- Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json +
  data/upstream-ct_R5005.txt, parsed per code/side-keyhunt/repair_parse.py).
  `canonical.py` never used. R5005, sealed gates, red-team queue untouched.

## Bar (verbatim, pre-registered before testing)

"fence @1232 as 'ce' + verb contact residual (unparsed); record the residual
against 47's A4 allophone tier"

Numbered pass/fail clauses (restated before testing, not modified after):

1. Demonstrate that the @1232 contact parses under no licensed reading with
   standing values (33 as verb-frame/infinitive, 47='ce' A4-granted).
2. Fence the contact as a 'ce' + verb residual with stated cause.
3. Record the residual against 47's A4 allophone tier.
4. Adverse answered: A10 makes the infinitive reading explicit at @1232 —
   show why the infinitive reading does not license a parse either.

## Method

1. Re-derived the repaired parse in-session (1,847 pairs, 96 groups).
2. Located the '47-33-29' trigram: exactly 1 occurrence stream-wide,
   1-based @1232–1234, row a7_01 (@1220–1248 1-based).
   Window (1-based): `... 79(tout) 82(m) 48 29(er) 47(ce) 33 29(er) 85 56 10 03 40 67 77 81 87(ce) 11(la) 00(pour) 33 16 00(pour) ...`
3. Tested both licensed readings of 33 against standing values.
4. Phase check: re-parsed row a7_01 under its rival offset-1; pairing is
   byte-identical (row digit string is even-length), so the trigram survives
   on both phases. Fence holds on either phase.

## Window-level evidence

- **Left edge @1228–1231:** `82 48 29 47` = "m [48] er ce". "48 29" is one of
  the two A7-L2 exclusive legs ("tout me [48-verb]"), cited not re-run.
  48's left neighbor 82='m' (banked letter) is consumed by the A7-L2 frame;
  no finite verb governs the span.
- **The contact @1232–1234 = 47 33 29**, with 47='ce' (A4 allophone tier,
  granted) and 33-29 = "[33]er" (A10 hold; 29='er' banked pencil).
- **Right edge @1235–1236 = 85 56**: 85 = verb-stem (A3, value open),
  56 = whole-word (noun/verb class alternation). Neither can serve as
  governor for a "ce + infinitive" left span.

### Per-reading tests (standing values only)

- **R1: 33 = verb stem, "ce [33]" finite.** FAIL: no finite-verb frame is
  licensed. "ce [33-29]" under a finite reading needs a governing
  construction that is byte-unevidenced; the A10 hold is explicitly the
  infinitive frame, not finite.
- **R2: 33-29 = "[33]er" infinitive (A10, explicit at this window).**
  FAIL: "ce [33]er" = "ce" + bare infinitive. In 1841 French, "ce" cannot
  be the subject of a bare infinitive (no article, no "que"), nor can it
  be its object ("ce" is not an object clitic; cf. object-"le"/"cela" at
  87). No governor exists in ±8 tokens (@1220 = 24 finite modal is too
  far and already bound to its own frame).
- **R3: clause-boundary rescue.** FAIL: the lane-wide "clause boundary
  after an article" mechanism was killed by clause-boundary-precedent
  (battery KILL 2026-10-09); no byte-evidenced boundary splits the trigram.

## Per-clause pass/fail

1. **PASS** — R1/R2/R3 all fail at battery grade; no licensed reading parses.
2. **PASS** — @1232 fenced as a 'ce' + verb contact residual (unparsed).
   Cause: "ce" has no licensed grammatical role against a bare
   infinitive/stem at this contact; left edge belongs to the A7-L2 frame,
   right edge offers no governor.
3. **PASS** — residual recorded against 47's A4 allophone tier
   (47='ce' granted; nothing about the A4 grant is re-litigated).
4. **PASS** — adverse answered: A10's explicit infinitive reading makes the
   residual *fenced*, not parsed. The infinitive reading (R2) is precisely
   the one that fails hardest — "ce + bare infinitive" is ungrammatical in
   every register of 1841 French.

## Verdict: PROMOTE

The fence action succeeds: the @1232 contact is fenced as a 'ce' + verb
residual with stated cause, recorded against 47's A4 tier. No standing
red-team verdict contradicted; §7 intact.

## Follow-ups

None required — this is a fence-executed promote, not a null. Optional
re-open condition: if the red team adjudicates 33's frame differently
or licenses a new "ce + bare infinitive" construction (out of scope
for battery), the residual re-opens.

## Bookkeeping

- Lock: code/crowd17/next-token/locks/slot-1232-fence.lock
  (created 2026-10-09T07:00:22Z, deleted on completion).
- Queue: battery-queue.json → `slot-1232-fence` status `verdict`,
  result `promote`, date 2026-10-09 (temp-file + rename; pre-write
  assert confirmed queued/verdictless; JSON re-validated).
- No other queue entry touched. No verdict downgraded.
