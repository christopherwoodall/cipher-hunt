# Battery report: le611-reparse — @611 '47 77 87 83 70' under 77='le'

- Target id: le611-reparse
- Worker: bc8ed16f-2972-4000-b987-b30260d3e5f4
- Date: 2026-10-08
- Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`). `canonical.py` not used. R5005 not touched.

## Bar (verbatim, pre-registered from battery-queue.json before testing)

"resolve iff ONE parse is grammatical with <=1 non-granted value assumption; else confirm as genuine residual"

Numbered pass/fail clauses:

1. **(C1)** There exists exactly-or-at-least one grammatical French parse of the
   @611 window ('47 77 87 83 70', row a4_00) under the test assumption 77='le',
   using granted/banked values freely plus at most ONE further non-granted
   value assumption. PASS = claim resolves (re-parse succeeds).
2. **(C2)** If C1 fails, the window is confirmed as a genuine residual: the
   ungrammaticality is attributable to tokens other than 77 (strain localizes
   to 47/87/83), both listed adverses are tested and fail to rescue the parse,
   and 77='le' is not contradicted by the window. PASS = residual confirmed,
   claim killed.

## Method

1. Rebuilt the repaired stream in Python per `repair_parse.py` (1,847 pairs verified).
2. Located the window: @611=47, @612=77, @613=87, @614=83, @615=70 on row a4_00.
   Left context @605–610: 54 64('qui') 39 64('qui') 02 58. Right context
   @616–618: 88 10 29('er').
3. Census: the 5-gram '47 77 87 83 70' occurs exactly ONCE in the stream
   (@611). Sub-grams '47 77 87 83', '77 87 83 70', '87 83 70' also unique to
   @611–613. Single-window test, no corpus cross-check possible.
4. Enumerated candidate parses under standing values:
   47='ce' (granted, A4 allophone tier), 77='le' (provisional, test assumption),
   87='ce' (granted), 83 open, 70='pre' (banked pencil).
   Non-granted-assumption budget for the test: 1 (the 77='le' assumption itself
   is the thing under test and is not charged to the budget).
5. Tested each listed adverse as a rescue candidate.

## Window-level evidence (@-offsets)

- @611 47 (row a4_00) — value 'ce' granted (A4); rival 'se' ungranted (frame-qui-47).
- @612 77 — 'le' provisional (test assumption).
- @613 87 — 'ce' granted.
- @614 83 — open; 'de' lead from '98-83' x5 vient-parvenir formula (ungranted).
- @615 70 — 'pre' banked (pencil ground truth).
- Base reading (0 new assumptions): "ce le ce [83] pré…" — the sub-sequence
  "ce le ce" (@611–613) is ungrammatical in French for every possible 83:
  "ce" (demonstrative) + "le" (article) admits no following second "ce".
- P2 rescue (83='de', 1 assumption): "ce le ce de pré…" — ungrammatical.
  The 'de' lead does not interact productively with this frame.
- P3 rescue (47='se', 1 assumption): "se le ce [83] pré…" — "se le" is a legal
  double-clitic order only before a verb; @613 87='ce' (granted) is not a verb.
  Ungrammatical. The 47='se' rival does not rescue the window.
- P4 (47='se' + 83='de', 2 assumptions): over budget and still ungrammatical.
- P5 (87='cède' as verb): "ce le cède [83]…" WOULD parse ("this yields it"),
  but it requires reassigning 87, which is GRANTED as 'ce'. That is not a
  "non-granted value assumption" — it is anti-grant, out of battery scope.
  Fenced for the red team (see below), not tested.
- Control: even with 77 re-valued (e.g., as a verb), "47 77 87 83 70" cannot
  parse while 87='ce' stands ("ce [V] ce" — 'ce' cannot be a direct object).
  The blocker is @613 (87), not @612 (77).

## Per-clause pass/fail

- **C1: FAIL.** No grammatical parse exists within the budget. Every
  ≤1-assumption candidate (P1–P3) is ungrammatical; the only grammatical
  rescue (P5) requires ungranting 87='ce', which the bar does not permit.
- **C2: PASS.** @611 is confirmed as a genuine residual:
  (a) strain localizes to @613 (87='ce' grant), not to 77='le';
  (b) both adverses tested and fenced — 47='se' fails (P3), 83='de' fails (P2);
  (c) the window does not contradict 77='le' (the blocker persists under any
  77 value); (d) the 5-gram is unique in the stream, so the residual is
  window-local, not a distributional contradiction.

## Verdict

**kill** — the claim "@611 '47 77 87 83 70' re-parses under 77='le'" is forced
false by the window at kill grade. Scope of the kill: the re-parse claim only.
Untouched: 77='le' provisional standing (battery-le-77 verdict stands),
47='ce' (A4 grant), 87='ce' grant. No standing red-team verdict is
contradicted, so no null-escalation is triggered.

Adverses answered (none ignored):
- 47='se' rival (frame-qui-47): tested as P3, fails to rescue; fenced with
  cause ('se le' needs a verb at 87; 87='ce' granted blocks it).
- 83='de' lead: tested as P2, fails to rescue; fenced ('ce le ce de' still
  ungrammatical; the vient-parvenir 'de' lead does not transfer to this frame).

Red-team note (fenced, not decided): the sole grammatical rescue of @611 is
87='cède' (verb), which collides with the standing 87='ce' grant. Whether
87='ce' is absolute or admits a verb allophone is a red-team question; this
battery does not touch it.

## Optional follow-up leads (not queued — kill verdict, for supervisor awareness)

1. Red-team adjudication: is 87='ce' absolute, or does 87 admit a verbal
   allophone ('cède') in "ce le [87]" frames? Discriminator: other "X le 87"
   windows (@1216 '36 77 83' is adjacent territory; see le83-window).
2. 83 value battery remains open (le83-window queued); @614 83 here is
   uninformative beyond "not the rescuer".
