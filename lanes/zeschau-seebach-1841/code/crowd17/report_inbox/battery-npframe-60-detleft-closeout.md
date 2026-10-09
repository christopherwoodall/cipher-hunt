# Battery report: npframe-60-detleft-closeout

Worker: battery subagent (session 364c467c-f53a-4bf9-a7ec-4c7a2acca26f).
Date: 2026-10-09.
Stream: repaired 1,847-pair parse (`data/upstream-ct_R5005.txt` +
`code/side-keyhunt/repaired_offsets.json`), parsed per
`code/side-keyhunt/repair_parse.py` (re-implemented inline; n=1847 asserted,
96 groups asserted). `canonical.py` never used. R5005, sealed gate instances,
and the red-team adjudication queue untouched. @i = 0-based pair index.
Lock: `code/crowd17/next-token/locks/npframe-60-detleft-closeout.lock`
created at start, deleted on completion.

Parent: `ledit-60-corrob` (NULL, 2026-10-09,
`code/crowd17/report_inbox/processed/battery-ledit-60-corrob.md`) —
the only determiner-shape-left-of-60 windows besides @454 are
@1366/@1690 ("79 14 60"); @1366 already closed (03=verb-stem promoted);
@1690's right neighbor 27 unresolved. Prior related work adopted, not
re-run: `dit-60-syncretic` (kill: 60 != "dit"), `frame-62-94-79`
(instance-B "ne...que" analysis), `ne-24-profile` (@1691 context).

## Bar (verbatim from battery-queue.json, pre-registered BEFORE testing)

"resolve iff 27's class is named and every '79 14 60' window (@1366/@1690)
fenced as non-participial; else state what remains open"

Numbered clauses (fixed before data examination):

1. (C1) Test 27's class under standing values (distributional + frame evidence).
2. (C2) If 27's class is named, fence both "79 14 60" windows (@1366, @1690)
   as non-participial with stated cause.
3. (C3) If the class cannot be named, state what remains open (fail closed,
   per the bar's else-branch).

## Findings

**C1 — 27's class cannot be named at battery grade.** n(27) = 1,
stream-wide hapax, single window at 0b@1691 (row a8_05):
`62 94 79 14 60 27 46 24 85` =
"...il[62] ne[94] tout[79] [14] [60] [27] que[46] [24] [85]...".
There is no distributional leverage (no other window tests any candidate
class against a second context), and the frame itself is grammatically
strained under every candidate class, per the adopted frame-62-94-79
analysis ("ne...que" brackets "tout [14] [60] [27]"; 79="tout" cannot sit
between the negator and the closer; the bracket's verb slot is empty).
Candidate arms exercised, none killable or landable:

- **Nominal:** possible ("tout [14] [60] [27]" as NP with apposition/modifier)
  but unproven; the frame strain means a noun-27 does not rescue the window.
- **Adverbial:** possible ("[27-adv] que [24]" as a modifier position) but
  unproven; no adverb profile to test against.
- **Verbal (stem/finite):** "[60] [27-verb] que[46] [24-verb]" would put two
  verb-class items adjacent with no boundary — hostile, but 60's class is
  open (noun-shaped @454 vs verb-forced @1338), so a 60-nominal + 27-verbal
  reading cannot be excluded at kill grade either.
- **Particle/preposition:** no licensed parse under standing values.

Conclusion: **27's class is open.** No kill-grade window rules out any of
the three live arms; no second window names any of them.

**C2 — does not fire.** 27's class is unnamed, so the brief's "if 27 is
non-nominal" condition cannot be established. The det-left 60 windows are
nevertheless non-participial on grounds independent of 27's class:

- @1366 ("79 14 60 03"): fenced by the parent (03=verb-stem battery-PROMOTED
  cannot follow a "ledit"-style participle).
- @1690 ("79 14 60 27"): no "ledit"-style participle reading is available
  because 60="dit" is kill-grade dead (`dit-60-syncretic`, adopted) and
  `ledit-60-corrob` C3 established that no other battery-available
  participial value for 60 survives (@1338 forces finite, @700 kills the
  -dre stem, @454's only value killed). The non-participial fence at @1690
  does not depend on 27's class at all.

So the NP-frame question for 60 stands fenced at battery level on the
60-value grounds — 27's class is the narrower open question this battery
leaves behind.

**C3 — what remains open (fail closed):**

1. 27's class: noun / adverb / verb arms all live, none provable from a
   single strained window. Any future named 60 value (verb-60/poly-60-redteam
   docket, red-team venue) re-tests the "14 60 27" geometry directly.
2. The whole instance-B "ne...que" frame ("il ne tout [14] [60] [27] que
   [24] [85]") remains a fenced residual: the bracket's verb slot is empty
   under standing values ("tout" cannot head it; "[27] que [24]" cannot
   open a new clause).
3. @1690's det-left geometry stays fenced-as-non-participial (value-driven,
   not class-driven) pending the red-team 60 docket.

## Verdict: NULL

C1 fails closed (hapax, class unnamed); C2's conditional does not fire;
C3 executed — what remains open is stated above. No standing or red-team
verdict contradicted or downgraded; §7 intact. Canonical-stream caveat
stands (row a8_05's upstream offset unvalidated).

## Follow-ups proposed (for supervisor queuing)

1. `val-27-1691-np` (P4) — once the red team resolves 60's class/value,
   test whether "14 60 27" parses NP-internal (modifier/apposition arm)
   under the named value; gates on the poly-60-redteam docket.
2. `neque-bracket-verb-search` (P3) — find the licensed verb for the
   instance-B "ne...que" bracket's empty verb slot ("il ne [V] tout que"),
   with "tout [14] [60] [27]" as its complement; if no verb is licensable
   under any battery-available class, fence the window as a permanent
   residual with the stated cause.
3. `hapax-27-syllabic` (P4) — letter-tier test: whether 27 composes
   syllabically with 60/46 once the 29/40/33 syllabary questions resolve;
   do not name without a second window.

## Bookkeeping

- Lock `code/crowd17/next-token/locks/npframe-60-detleft-closeout.lock`
  created on start, deleted on completion.
- Queue update: temp-file + rename on `battery-queue.json`, own entry only;
  pre-write assert confirmed the existing entry's status ("queued") and
  verdict (null) is not downgraded; JSON re-validated after write.
- R5005, sealed gate instances, and the red-team adjudication queue untouched.
