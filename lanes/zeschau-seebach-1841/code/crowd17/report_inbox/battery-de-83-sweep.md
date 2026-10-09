# Battery `de-83-sweep` — verdict: NULL

Target: 83='de' across all 15 windows (promote bar).
Date: 2026-10-09. Stream: repaired 1,847-pair parse
(`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`);
1,847 pairs / 96 types re-derived independently. `canonical.py` never used.
R5005, sealed gates, red-team queue untouched. Lock created on start, deleted
on completion.

## Bar (verbatim, pre-registered)

"promote 83='de' iff all fenced adverses stay fenced with cause AND zero new
contradictions across the 15 windows"

## Bar restated as numbered pass/fail clauses (pre-registered before testing)

- **C1:** All fenced adverses against 83='de' stay fenced with cause
  (the three fenced cells: @614/@1171 'ce de', @911 'qui de est', @1217 'le de').
- **C2:** Zero NEW contradictions across the 15 windows under 83='de'
  (contradictions already recorded by the gate batteries are not new).

## Gate verdicts (standing, read from processed reports)

- **fence-911-de** (2026-10-08): verdict **null**, with a **kill-grade failure of
  unconditioned 83='de' recorded at @911** ("qui de est" ungrammatical, no parse
  with <=1 non-granted assumption; cheapest fences rejected). Escalated to the
  red team. Battery-level kill explicitly declined (lead shared with le83-window).
- **frame-87-83-cede** (2026-10-09): verdict **null**. The 'cède' verb rival
  parses @1171 cleanly ([55-61-94 word] cède [21], surrender-valence) but does
  NOT parse @614 at battery grade ('celle cède' needs 2 ungranted assumptions,
  one pre-graded failing). Consequence stated: the two '87 83' windows remain
  83='de''s **open adverse**; the locus-level fence is not established at @614.
- **fence-83-1217** (2026-10-08): verdict **null**, fence formalized: '36 77 83'
  @1215-1217 ("par ce [36] le [83]") — 'le de' ungrammatical, 83 fenced as the
  designated blocker with stated cause.
- **le83-window** (2026-10-08, background): 12-13/15 windows de-compatible;
  the three fenced cells are @613/@1170 ('ce de'), @911 ('qui de est'),
  @1217 ('le de').

## 83 census (re-derived on the repaired stream)

83 n=15. Offsets below are this script's numbering (0-based pair index), which
matches the queue evidence numbering used by fence-83-1217's census.

| @   | context (83 marked)            | reading under 83='de'              | grade            |
|-----|--------------------------------|------------------------------------|------------------|
| 228 | 98 >>83 82                     | "vient de m" (formula head)        | compatible       |
| 614 | 87 >>83 70                     | "ce de pre..."                     | open adverse     |
| 898 | 98 >>83 86                     | "vient de [86-INF]"                | compatible       |
| 907 | 55 >>83 54                     | "[55] de [54]"                     | conditional      |
| 911 | 64 >>83 59                     | "qui de est"                       | KILL-GRADE       |
| 931 | 98 >>83 56                     | "vient de [56]"                    | compatible       |
| 1061| 98 >>83 82                     | "vient de m" (formula)             | compatible       |
| 1161| 44 >>83 21                     | "[44] de [21]"                     | compatible       |
| 1171| 87 >>83 21                     | "ce de [21]"                       | fenced (locus)   |
| 1217| 77 >>83 92                     | "le de [92]"                       | fenced w/ cause  |
| 1334| 39 >>83 86                     | "[39] de [86-INF]"                 | conditional      |
| 1612| 55 >>83 71                     | "[55] de [71]"                     | conditional      |
| 1784| 98 >>83 82                     | "vient de m" (formula)             | compatible       |
| 1829| 38 >>83 24                     | "[38] de [24]" ("de faire")        | compatible       |
| 1840| 44 >>83 21                     | "[44] de [21]"                     | compatible       |

Predecessor distribution (matches fence-83-1217's census exactly):
98 x5, 87 x2, 55 x2, 44 x2, 64/77/39/38 x1. Followers: 82 x3, 21 x3, 86 x2,
70/54/59/56/92/71/24 x1.

Window notes:
- @1829 "38 83 24": under 24='faire' (battery-promoted), "de faire" is
  grammatical — a fresh positive leg, not a contradiction.
- @907/@1334/@1612 (conditional): all neighbors open (54/55, 39, 71); no
  standing value contradicts 'de' at these windows. 39='à' is NOT granted
  (39 absent from table-registry.json), so @1334 "39 de [86-INF]" is not a
  battery-grade contradiction — but it is a pre-registered collision point
  if 39='à' ever promotes (see follow-up 2).
- @614: "ce de" remains an open adverse per frame-87-83-cede (the 'cède'
  rival is unproven there; the '47 77' contact fenced as a ce-le residual).
- @1171: 'cède' parses cleanly — locus-level fence with cause for 83='de'.
- @1217: fence formalized with stated cause (fence-83-1217).
- @911: kill-grade for unconditioned 'de' (fence-911-de), escalated to red team.

## Per-clause pass/fail

- **C1: FAIL.** "All fenced adverses stay fenced with cause" is not met:
  (i) @911 was never fenced with cause — fence-911-de recorded a kill-grade
  failure of unconditioned 83='de' and escalated it; (ii) @614 has no fence
  with cause at all — frame-87-83-cede left the 'ce de' windows as an open
  adverse. Only @1171 (locus-level 'cède' fence) and @1217 (formalized fence)
  satisfy the clause. A battery promote of 83='de' across all 15 windows —
  i.e. unconditioned — would overwrite fence-911-de's escalated kill-grade
  finding without red-team adjudication, violating protocol §5 (never
  downgrade an existing verdict / do not overwrite escalated decisions).
- **C2: PASS.** No NEW contradictions: every window not already accounted for
  parses compatibly or conditionally under 83='de'; the census matches the
  standing records exactly. @1829 even adds a positive leg ("de faire").

## Verdict: NULL

The promote bar is not earned (C1 fails). This is not a battery-level kill:
kill-grade on unconditioned 83='de' is owned by fence-911-de and already
escalated to the red team — duplicating it here would double-count. The
red team decides whether unconditioned 'de' dies at @911 or survives via a
conditioned reading; this battery's evidence set (8 compatible, 3
conditional, 2 fenced, 1 open adverse, 1 kill-grade) is packaged below for
that adjudication.

No standing verdict contradicted or downgraded.

## Follow-ups proposed (for supervisor queuing)

1. `de83-condition-set` (P2) — enumerate the surviving parse set under a
   conditioned 83='de' (the 11 non-contested windows: exclude @614/@1171
   'ce de', @911 'qui de est', @1217 'le de'), so the red team adjudicates
   with a clean conditioned candidate in hand.
2. `de83-39-1334` (P3) — pre-register the 39-value collision check at @1334:
   if 39='à' ever promotes, "39 83 86" = "à de [INF]" becomes a new
   contradiction; test 39's open values against 'de' compatibility now.
3. Cited, not queued (no duplicates): `cede-614-subject` (P2) and
   `de83-adverse-restock` (P3) were already proposed by frame-87-83-cede
   and address the @614 open adverse.

## Bookkeeping

- Report: this file.
- Queue: `de-83-sweep` -> status `verdict`, result `null`, date 2026-10-09
  (temp-file + rename; pre-write assert confirmed queued/verdictless;
  JSON re-validated post-write; only this target's entry touched).
- Lock `de-83-sweep.lock`: created on start, deleted on completion.
