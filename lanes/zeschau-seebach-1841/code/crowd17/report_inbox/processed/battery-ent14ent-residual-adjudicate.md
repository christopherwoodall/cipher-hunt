# Battery report: ent14ent-residual-adjudicate — the "06-14-06" residual @1121

Worker: d3373ac8-9840-4209-a2e0-65e8b89f72f3 | 2026-10-09T05:18Z.
Lock `locks/ent14ent-residual-adjudicate.lock` created on start (agent id + UTC),
deleted on completion. No prior/stale lock existed.

Target: `ent14ent-residual-adjudicate` (priority 2).
Claim: the "06-14-06" residual @1121 is resolvable.

## Bar (verbatim, pre-registered before testing)

"resolve iff a single segmentation of @1118-1127 parses fully under standing
values with at most 1 stated assumption naming 14's sub-word role; else confirm
as unresolvable residual and fence 14's @1121 window"

Numbered clauses (fixed before data examination):

- C1 (resolve): a single segmentation of the span @1118-1127 parses fully under
  standing values, with at most ONE stated assumption, that assumption naming
  14's sub-word role only. PASS iff the parse is grammatical 1841 diplomatic
  French end-to-end with no further open-value load.
- C2 (else): confirm the span as unresolvable residual at battery grade and
  fence 14's @1121 window with stated cause.

## Method

Repaired 1,847-pair stream only: `code/side-keyhunt/repaired_offsets.json` +
`data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`
(1,847 pairs / 96 types re-verified in-session). `canonical.py` never used.
R5005, sealed gates, red-team adjudication queue untouched. @-offsets are
0-based pair indices (queue convention): the brief's "@1121" = 14 at index
1121; the "06-14-06" trigram is @1120-1122; the test span @1118-1127 =
`70 12 06 14 06 11 52 37 43 00` = "pre n ent [14] ent la [52] [37] [43] pour".
Wider surface (0-based @1114-1133, row a6_07, mid-row throughout):
`30 69 | 11 88 70 12 06 | 14 | 06 11 52 37 43 00 86 52 37 86 | 24 77`.

Standing values used: banked 11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que;
granted 87=ce, 64=qui, 96=par, 17=fois, 79=tout, 00=pour (A9), 84=on (A15),
47=ce (A4); promoted 06=ent (ent-06 battery, letters tier), 94=ne, 30=pas,
12=n (letter tier); provisional 59=est, 77=le; 24=finite-verb class (R17-009);
37/32/42 predicative class grant (A1). 1841 diplomatic French throughout.

Standing premises used as premises (cited, not re-litigated):

- prennent-70-12-06 (KILL, 2026-10-08): subject-agreement reading of
  "11 88 70 12 06" forced false; the single-n "prennent" license is dead
  (spell-single-consonant / spell-pasent-test). So 70-12-06 cannot be the
  finite verb "prennent" at battery grade.
- souvent-14-06-retest (KILL, 2026-10-08): 14="sou" spelling-dead at @84 AND
  @1121 — "souent" != "souvent" under standing 06="ent".
- le-14-kill-1121 (KILL, 2026-10-09): 14='le' killed as a global value at @1121
  at kill grade; exhaustive enumeration of every "...ent le ent..." / boundary
  segmentation at this window died on closed grounds.
- stem-14-id (NULL/fence, 2026-10-09): verb-stem 14 fenced at @1121; the
  ent-06 battery's "@1122 parses ONLY as verb+object" leg superseded; the
  frame stands as a segmentation residual.
- ent-06-host-census (PROMOTE, 2026-10-09): 06 is a finite ending ("-ent", 3pl)
  iff its left neighbor is a verb stem, else a syllable; the finite fork at
  the @1121 06 is killed (single-n license dead) — the residual word is open.

Distributional facts (re-derived, byte-exact): "06 14 06" trigram unique
stream-wide (1x, this window); "14 06" bigram exactly 2x (@84, @1121); n(14)=15
at 72, 84, 117, 141, 178, 339, 424, 458, 586, 623, 813, 896, 1121, 1365, 1689
(matches tout-slot-14 census exactly).

## New work: exhaustive sub-word-role enumeration for 14 (C1's test)

The bar permits exactly one stated assumption: 14's sub-word role. No value
may be invented for 14; no other open group may be valued. Every role below is
tested against the full span `70 12 06 14 06 11 52 37 43 00`.

- Role A (14 = standalone word X): "...ent [X] ent la..." — X unnameable at
  battery grade ('le' killed, 'sou' killed, every other value invented).
  No parse statable. DEAD.
- Role B (14 = word-final letter/syllable, composing leftward):
  "70 12 06-14" = "pre-n-ent-[14]"; the span then reads "...[88] pre-n-ent-?
  ent la [52] [37] [43] pour". The stranded "ent" (@1122, 06) is not a French
  word, and no boundary rescue is byte-evidenced (mid-row a6_07; le-14-kill
  C2 exhausted the boundary branches). DEAD.
- Role C (14 = word-initial syllable, composing rightward): "[14]ent la" =
  "?ent la". With no value for 14 the parse cannot be completed; the only
  battery-named candidate ("souent") is spelling-killed; 'le' is kill-grade
  dead (elision defect). DEAD.
- Role D (14 = word-internal letter: "ent-[14]-ent" / "[14]-ent" inside a
  longer word spanning 06-14-06): no French word shape is statable with an
  unvalued 14, and the breaker-b4-1121 word-internal candidate ("[14]ent"
  inside "souvent") is dead via the spelling kill. DEAD.
- Role E (14 = elided 'l' before "ent"): "...ent l'ent la..." — "l'ent" is not
  a French word (le-14-kill noted this belongs to a different claim; tested
  here: no parse). DEAD.
- Role F (14 = object/clitic pronoun other than 'le'): no battery-grade value
  exists; inventing one exceeds the assumption budget. DEAD.
- Role G (clause boundary at 06@1120|14 or 14|06@1122): left strand "pre n ent"
  cannot be a finite verb (single-n license dead, C1 of prennent-70-12-06);
  right strand "ent la" is a non-word (le-14-kill branch 4, re-verified).
  DEAD.

No role yields a full parse. C1 FAILS at kill grade: the window forces the
claim ("the residual is resolvable") false under the bar's own budget, and
every escape route is closed by standing kills, not by open values. The kill
is antecedent-independent: it does not depend on 88, 16, 52, 37, 43, or 86.

## Adverses

- "88/16 open at left edge": answered — the role enumeration never loads 88's
  or 16's values; the kill holds for every 88/16 assignment.
- "52-37-43 open at right": answered — the kill is decided at the 06-14-06
  core; no 52/37/43 assignment rescues a dead 14 role.

## Verdict: KILL (of the resolvability claim) + FENCE

C1 fails at kill grade; C2 fires. The "06-14-06" residual @1120-1122 (0-based;
14 at @1121) is confirmed UNRESOLVABLE at battery grade, and 14's @1121 window
is FENCED with stated cause: every sub-word role for 14 dies under standing
values within the bar's one-assumption budget, and all four battery-named
escapes ('le', 'sou', verb-stem, single-n "prennent") are kill-grade or
fence-grade dead.

Scope (narrow): this kills RESOLVABILITY at battery grade, not 14 globally.
14's value stays open; the surviving 'le'-legs (@72/@117/@178) remain
homophony-question evidence for the red team (le-14-kill-1121 escalation,
untouched). No standing verdict contradicted or downgraded; §7 intact.

## Follow-ups proposed (kill — optional, 2 included)

1. `val-14-determiner-test` (P4): test 14='le' (determiner) at the surviving
   legs @72/@117/@178 under the A8 "ce le [verb]" frame; decides whether the
   homophony question has battery-grade legs before red-team escalation.
2. `leftedge-88-70-12` (P4): name 88's class at @1118 ("11 88 70 12 06") now
   that the "prennent" reading is dead — closes the left edge of the fenced
   residual.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-ent14ent-residual-adjudicate.md`
  (this file).
- `battery-queue.json`: `ent14ent-residual-adjudicate` set to status `verdict`,
  verdict `{"result": "kill", "report": "code/crowd17/report_inbox/battery-ent14ent-residual-adjudicate.md", "date": "2026-10-09"}` via temp-file +
  rename; pre-write assert confirmed `queued`/verdictless; post-write JSON
  re-validated.
- Lock `locks/ent14ent-residual-adjudicate.lock` deleted on completion.
- `canonical.py` never used; R5005, sealed gates, red-team adjudication queue
  untouched.
