# Battery report: fence-92-1218 — '83 [92]' @1217-1218 right edge

- Target: `fence-92-1218` (priority 2)
- Date: 2026-10-08
- Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed exactly like `code/side-keyhunt/repair_parse.py`). `canonical.py` NOT used. R5005 NOT touched.
- Lock: `code/crowd17/next-token/locks/fence-92-1218.lock` (created on start, deleted on completion; no stale lock)

## Bar (verbatim, pre-registered before testing)

"name 92's class/value such that the fenced-83 edge parses or fences cleanly; resolve or fence the window with stated cause"

Numbered clauses:

- **C1**: name 92's class/value such that the fenced-83 edge @1217-1218 parses.
- **C2**: otherwise, fence the window cleanly with stated cause.

## Window evidence (re-derived on the repaired stream)

Row a7_00/a7_01 boundary:

- @1213: 96 ('par', promoted)
- @1214: 45 ('ce', HOLD A11)
- @1215: 36 (unnamed)
- @1216: 77 ('le', provisional)
- @1217: 83 (designated blocker, value unfixed)
- @1218: 92 (open; '-ère' value killed)
- @1219: 61 (unnamed)
- @1220: 24 (finite modal verb class)

So the right edge is `'le [83] [92] | [61] [24-finite]...'` — 83-92 is a
**hapax** (83's followers: 92 x1 of 15 windows), and 92-61 is a **hapax**
(61's predecessors: 92 x1 of 18 windows). No parallel contact data exists
for either adjacency. 92 n=22 confirmed on the repaired stream.

## Coordinated batteries (not duplicated)

- **prenne-92-noun** (kill, 2026-10-08): 92 as global feminine noun killed
  at kill grade — 5 kill-grade fails (@1154 'pour [92]er' with 29='er'
  banked; @1379 'on [92]' with 84='on' unconditioned; @66 'ne [92]';
  @1310 'pas [92]'; @1453 'que [92]'). Its @1218 entry
  (`77 83 92 61 24`) was fenced as "depends on 83" — owned by this target.
- **verb-92-subset** (promote, subset-scoped, 2026-10-08): 92=verb on its
  8 verbal-governor windows (00 x6, 94, 84, 46). @1218's governor is 83 —
  **outside the subset**; the promote makes no claim here. @1154 shows
  92 can be stem-shaped ('pour [92]er'), but that frame is 00-governed,
  not 83-governed.
- **fence-83-1217** (null, 2026-10-08): 83 designated blocker; '36 77 83'
  localized residual. 83's value stays unfixed here — the 'de' lead is
  owned by de-83-sweep (queued, gated on this target).
- **split-92-adjudication / split-92-redteam-evidence / class-92**:
  all verdict null — no standing global-class verdict for 92 to contradict.

## Resolution attempts

**Attempt 1 — 92 = verb (INF) governed by 83.** For '83 [92]' to parse as
preposition + infinitive (parallel to 00='pour' + verb), 83 must be an
infinitive-governor. The only grounded candidate is the 83='de' lead —
but 83='de' is NOT granted; de-83-sweep owns that adjudication, and
assigning 83 any value here would violate the designated-blocker fence
from fence-83-1217 and duplicate de-83-sweep's bar. **Conditional only:**
IF de-83-sweep promotes 83='de', THEN 'de [92-verb]' parses per the
verb-92-subset promote generalized to prepositional governance. Not
decidable at battery grade now.

**Attempt 2 — 92 = noun after 83.** The noun arm is dead at kill grade
(prenne-92-noun). A noun reading at @1218 would require 92 noun-shaped
here while verb-shaped at @1154 — that is polyvalence, which is red-team
business (§7; 67 et/veut is the sole true polyvalence). **Dead without
red-team action.**

**Attempt 3 — clause boundary after 83** ('...83. [92] 61 24...'). 92
clause-initial: 92 verb-shaped gives "V [61] V-finite" (two finite verbs,
ungrammatical); 92 noun-shaped is killed; any other class is unanchored
(92-61 hapax, 61 unnamed, @1220=24 finite). **Cannot parse; fenced.**

**Attempt 4 — word-internal 83-92.** 92 can be stem-shaped (@1154), but
attaching it to value-unknown 83 is speculation with no anchor — 83-92
hapax, no parallel. **Fenced as speculation.**

**Attempt 5 — governor-class generalization.** 92's predecessors are
dominated by verbal governors (00 x6, 84 x2, 94 x2, 46 x1 = 11/22), but
the verb-92-subset promote is explicitly scoped to those governors. 83
is a singleton governor with unknown class. Nothing licenses extending
the verb reading to @1218 without 83's class.

## Per-clause pass/fail

- **C1 (name 92's class/value so the edge parses): FAIL.** 92=verb parses
  only conditionally on ungranted 83='de' (owned by de-83-sweep);
  92=noun is killed globally (would need red-team polyvalence); every
  other class is unanchored (both adjacencies hapax).
- **C2 (fence cleanly with stated cause): PASS.** The residual localizes
  fully to 83's unknown value: 83 is the designated blocker
  (fence-83-1217), 83-92 and 92-61 are both hapax (no parallel to
  anchor any reading), and the two candidate 92-classes at this window
  are verb-conditional (on de-83-sweep) or noun-killed. The fence does
  not downgrade any standing verdict: prenne-92-noun's kill, the
  verb-92-subset promote, and the split nulls all stand untouched.

## Verdict

**null** — the '83 [92]' @1217-1218 edge fences cleanly: resolution is
blocked on 83's class (designated blocker), with the conditional recorded
that 83='de' + 92=verb parses per the verb-92-subset promote. No standing
verdict contradicted or downgraded. R5005, sealed gates, and the red-team
adjudication queue untouched.

## Follow-up targets (null regenerates work)

1. **edge-83-92-retest** (P2): re-test '83 [92]' @1217-1218 once de-83-sweep
   names 83's class. Bar: if 83 is an infinitive-governor ('de'-shaped),
   confirm '83 [92]' parses with 92=verb per the subset promote; if 83 is
   nominal/adjectival, re-derive the edge under that class. Gate: fires
   only after de-83-sweep verdicts.
2. **verb-92-prep-governor** (P2): test whether the verb-92-subset promote
   generalizes to prepositional governors beyond {00, 94, 84, 46}. Bar:
   survey all 92 windows with preposition-class governors (00 x6 already
   covered; 83 is the only other candidate once classed) and state
   whether 92 is uniformly verb-shaped under prepositional governance.
   Narrows whether Attempt 1's conditional is an instance of a general rule.
3. **clause-init-92-61** (P3): test the clause-boundary-after-83 reading
   once 61's class is named. Bar: with 61's class fixed, does
   '[92] [61] [24-finite]...' parse as a clause-initial frame under any
   92-class, or does the boundary reading die? Gate: fires only after 61
   is classed (61 open, 18 windows).
