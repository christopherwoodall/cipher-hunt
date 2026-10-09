# Battery report: merge-gate-w1-x55-61

Target: `merge-gate-w1-x55-61`. Claim: the w1-573-subject verdict decides
whether X merges with W1's "ne mentent" subject.
Date: 2026-10-09. Worker: 6b913f61-a0d1-4cc9-97e2-ed9282cb53a7 (battery worker).
Lock `locks/merge-gate-w1-x55-61.lock` created 2026-10-09T04:19:51Z (no prior
lock existed, stale or otherwise); deleted on completion.

Offset convention: @n below are the 0-based pair indices used in the source
reports (battery-w1-573-subject.md uses 1-based; conversions given inline).
All stream numbers come from the repaired 1,847-pair parse.

## Bar (verbatim, pre-registered)

"(a) once w1-573-subject returns, state whether its identified subject includes
55-61; (b) merge if 55-61 is the subject (X inherits the identification), else
kill the subject-reading of X and re-scope name-55-61-core to the W2/W3 frames
only"

## Bar restated (numbered pass/fail clauses; frozen before testing)

1. w1-573-subject has returned, and this report states whether its identified
   subject includes 55-61.
2. If 55-61 IS the identified subject, X merges with it (X inherits the
   identification). Otherwise, the subject-reading of X is KILLED and
   name-55-61-core is re-scoped to the W2/W3 frames only.

Adverses: none — pure gate.

## Method

Read BATTERY-PROTOCOL.md first, then battery-queue.json (target entry at
line 6014: priority 2, status queued, no lock). Read the gating report
`code/crowd17/report_inbox/battery-w1-573-subject.md` (verdict null,
2026-10-09; confirmed recorded in battery-queue.json with status "verdict")
and clause (c) of
`code/crowd17/report_inbox/processed/battery-name-55-61-core.md` (2026-10-08).
`canonical.py` never used. R5005, sealed gates, red-team adjudication queue
untouched. This is a coordination gate: the "test" is reading the gating
verdict and applying the bar logic. No numbers are invented here; every
window-level fact cited is carried over verbatim from the two source reports,
both of which re-derived their numbers from the repaired 1,847-pair stream
(`code/side-keyhunt/repaired_offsets.json` +
`data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`).

## Window-level evidence

Gating verdict (battery-w1-573-subject, 2026-10-09, null):

- W1 frame (row a3_02, 1-based @559-590 = 0-based @558-589): the
  '78-45-13-55-61' 5-gram sits at 1-based @574-578 (0-based @573-577); "ne
  mentent" = '94 82 06 06' at 1-based @579-582 (0-based @578-581). Second
  window at 1-based @1183-1186 (0-based @1182-1185).
- The verdict's clause 1 (subject named): FAIL (epistemic). Candidate audit:
  (1) "ce verdict" (@573-575, 1-based) — singular vs 3pl "mentent",
  REJECTED; (2) X = [13-55-61] (the only subject-shaped slot, immediately
  preverbal, "ce verdict, [X] ne mentent") — UNNAMEABLE: name-13-55-61
  (verdict null, 2026-10-09) rejected both H1 (one word over 13-55-61) and H2
  ("les [55-61]" 3pl-subject hypothesis); underdetermination structural
  (13, 55, 61, 43, 21 all open; dozens of plural nouns fit "les X ne
  mentent" equally); (3) "ce verdict de X" — still singular, REJECTED;
  (4) post-verbal 50 as inverted subject — no pronoun evidence, and W2's
  right context is "ne mentent est(59)", not a pronoun, FENCED; (5) pro-drop
  — ungrammatical French, REJECTED; (6) W2's "le ver[78]" — singular,
  disagreement (confirms the gap is systematic, not W1-local).
- The verdict's clause 2 (boundary stated): PASS (left @573 firm; right
  indeterminate past row end).
- The verdict's clause 3 (coordination with name-13-55-61): HONORED — merge
  cannot fire because name-13-55-61 is verdict/null.

name-55-61-core clause (c) (2026-10-08): coordinates exactly this gate
("merge if X is the subject"); names the three 55-61 windows
(W1: 13-55-61 before 94, W2: 13-55-61 before 94, W3: 43-[55-61]-21 at
1-based @1206-1207) and states the 55-61 census (predecessors 13,13,43;
successors 94,94,21).

## Per-clause pass/fail

1. **PASS.** w1-573-subject has returned (null, 2026-10-09, recorded in
   battery-queue.json). Its identified subject: NONE — clause 1 failed
   epistemically, and the verdict named no 3pl subject at either window.
   Therefore the identified subject does NOT include 55-61. The X=[13-55-61]
   slot spans 55-61, but the verdict explicitly judged X "structurally
   unnameable" and did not identify it as the subject; the merge condition
   ("merge if 55-61 is the subject") is not met. The verdict's own clause 3
   agrees: "merge cannot fire."
2. **PASS (else-branch executed).** Since 55-61 is not the identified
   subject, the else-branch fires:
   - The subject-reading of X — "X (55-61 within [13-55-61]) is W1's 'ne
     mentent' 3pl subject, inheriting the w1-573-subject identification" —
     is KILLED as a merge hypothesis. This is consistent with
     name-13-55-61's rejection of H2 ("les [55-61]" 3pl-subject hypothesis)
     and with w1-573-subject's clause 3. Nuance preserved: w1-573-subject's
     failure was epistemic, not kill-grade (X could still be some unnamed
     3pl NP like "les temoins"); what dies here is the MERGE, because there
     is no identification to inherit.
   - name-55-61-core is re-scoped to the W2/W3 frames only. The W1 window
     (the [13-55-61]-before-"ne mentent" subject-slot context) is no longer
     live scope for X's naming battery; the W2 window (0-based @1165-1169
     region, "13 55 61 94 82"-shaped) and the W3 window (1-based @1206-1207,
     "43 [55-61] 21", row a6_11) remain. (This is consistent with
     w1-573-subject's proposed follow-up `subj-55-61-word`, which already
     anchors on the W3 window and 55->81 x6 legs.)

## Adverse check

"none — pure gate": vacuously answered. No standing red-team verdict is
contradicted: R17-007's conditional "ne mentent" grant untouched;
collision-62-84's battery kill untouched (the slot-split batteries live on
other frames); the merge death is exactly what w1-573-subject's clause 3
already recorded.

## Verdict

**PROMOTE** — both bar clauses pass; adverses answered (none). The gate
fired per its bars: the merge condition failed (w1-573-subject identified no
subject, so 55-61 is not the subject), and the else-branch was executed —
the subject-reading of X is killed as a merge hypothesis and name-55-61-core
is re-scoped to the W2/W3 frames only.

## Follow-ups proposed

None. This is a pure gate: the bar's else-branch is the work product, and it
is fully executed above. (The gating verdict's own null already queued its
follow-ups — subj-13-value, subj-55-61-word, nementent-W2-subject — via the
supervisor's standing audit; subj-55-61-word is already W3-scoped and
consistent with this re-scope.)

## Bookkeeping

- Report: this file.
- `battery-queue.json`: `merge-gate-w1-x55-61` queued → verdict/promote via
  temp-file + rename (pre-write assert: queued, verdictless; JSON re-validated
  post-write; own entry only; no other entry touched; no downgrade).
- Lock created on start (agent id + UTC), deleted on completion.
- `canonical.py` never used. R5005, sealed gates, red-team queue untouched.
- No standing verdict contradicted or downgraded.
