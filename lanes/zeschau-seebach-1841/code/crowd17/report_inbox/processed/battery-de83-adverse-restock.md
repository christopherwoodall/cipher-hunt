# Battery `de83-adverse-restock` — verdict: PROMOTE (independent legs confirmed)

Target: re-test the 83='de' lead on windows excluding @614/@1171 (locus-fenced), confirming the lead's independent legs.
Date: 2026-10-09. Stream: repaired 1,847-pair parse
(`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`).
`canonical.py` never used. R5005, sealed gates, red-team queue untouched.
Lock created on start (no fresh lock existed for this id — locks/ held only
NOTE.md, class-62-16-windows.lock, ent14ent-residual-adjudicate.lock,
sub02-wordinternal.lock).

Context: frame-87-83-cede null (2026-10-09) follow-up #3; de-83-sweep null
(2026-10-09) tested the full 15-window promote bar; de83-condition-set
(2026-10-09, PROMOTE-package) enumerated the 11-window conditioned parse set.
This battery does NOT duplicate either: it tests leg INDEPENDENCE — how many
distinct frame types on the locus-fenced set genuinely support 83='de' —
independently re-derived from the stream, fencing failing legs with stated
cause. The @911 'qui de est' kill-grade failure and the queued
escalate-83-de-kill red-team docket item are coordinated, never re-adjudicated.
Unconditioned 83='de' is never killed at battery level (§4 kill reserved to
red-team escalation standing).

## Bar (verbatim, pre-registered)

"confirm the lead's independent legs on the locus-fenced set; else fence with stated cause"

## Bar restated as numbered pass/fail clauses (pre-registered before testing)

- **C1:** The locus-fenced set is the full 83 census minus @614 and @1171;
  independently re-derived on the repaired stream (positions, predecessors,
  followers, counts); any deviation from the de-83-sweep census recorded.
- **C2:** Independent legs confirmed: each confirmed leg is a DISTINCT frame
  type on the locus-fenced set that parses under 83='de' with <=1 non-granted
  value assumption. Legs that fail are fenced with stated cause, not silently
  dropped and not counted as support.
- **C3:** Leg independence from the excluded locus: no confirmed leg borrows
  support from @614/@1171 parses (e.g. no '87-83' contact reuse, no
  cède-rival dependency).
- **C4:** @911 (kill-grade, escalated to red team) and @1217 (formalized
  fence, 83 designated blocker) are coordinated, not re-adjudicated, and do
  not count as legs.

Verdict mapping (per §4): all clauses pass -> PROMOTE (of the lead's
independent legs as confirmed — explicitly NOT a value promotion of 83='de';
the unconditioned kill-grade at @911 stays escalated to the red team).
Any clause fails -> NULL with the failure as headline and 1-3 follow-ups.
A failing leg is fenced with stated cause per the bar.

## Method (pre-registered)

Independent re-derivation: load `code/side-keyhunt/repaired_offsets.json`,
pair `data/upstream-ct_R5005.txt` per `repair_parse.py`
(`[s[i:i+2] for i in range(o, len(s)-1, 2)]`), locate all 83 positions,
extract +-2 contexts, build predecessor/follower census, detect byte-identical
formula repetitions among the 83 windows (frame-vient-parvenir's x3 formula).
Standings used: 82='m' pencil; 86 INF-class granted (A9); 24='faire'
battery-promoted (ne-24-profile); 39='a' battery-promoted / registry LEAD
("a/à"); 21 noun-class (registry). Windows are French-tested against 1841
diplomatic usage only.

## Window-level evidence (independently re-derived, written after testing)

83 census re-derived on the repaired stream (1,847 pairs / 96 types): n=15,
offsets [228, 614, 898, 907, 911, 931, 1061, 1161, 1171, 1217, 1334, 1612,
1784, 1829, 1840] — match de-83-sweep exactly. Predecessors {98 x5, 87 x2,
55 x2, 44 x2, 64/77/39/38 x1}; followers {82 x3, 21 x3, 86 x2,
70/54/59/56/92/71/24 x1} — exact match.

Locus-fenced set (excl @614/@1171): 13 windows. **Zero 87-contact at any of
them** — the excluded '87-83' locus is cleanly separated; no leg borrows the
'cède' rival or any @614/@1171 parse (C3 ground). The 98-83-82-96-21 formula
is byte-identical x3 at [227, 1060, 1783] with thirds 60/62/68 — so
@228/@1061/@1784 are one frame type x3 instances, not three independent legs.

### Leg verdicts on the locus-fenced set

**LEG-1 CONFIRMED — 'de' + infinitive-class follower (1 frame type, 3 instances).**
@898 '98-83-86' — clean: 86 is INF-class (A9 granted), 'de' + infinitive needs
0 non-granted assumptions. @1829 '38-83-24' — positive leg: under
battery-promoted 24='faire' (ne-24-profile), "de faire" is grammatical
French (1 stated battery-grade assumption). @1334 '39-83-86' — conditional
instance: 39='a' is battery-promoted / registry LEAD tier, so "à de [INF]"
is a live collision point, not a contradiction; owned by queued
de83-39-1334, not re-decided here. Frame type confirmed; 1 clean + 1
positive + 1 conditional instance.

**LEG-2 CONFIRMED — formula-bound '98 de 82' (1 frame type, 3 instances).**
@228/@1061/@1784 byte-identical '98-83-82-96-21' x3 formula heads. Under
pencil 82='m' (banked GT), "[98] de m[e]"-shaped; 'de' imposes no new demand
on open 98. Caveat: 98's value is open and frame-vient-parvenir KILLED the
'vient de me parvenir' French — this leg claims only the frame-type slot
parses as 'de', not the French sentence. Confirmed with that caveat.

**LEG-3 CONFIRMED — '98 de 56' @931 (1 frame type, 1 instance).**
Distinct from LEG-1/LEG-2 by follower class (56, open). "[98] de [56]" —
'de' faces zero constraints; compatible, weak. Confirmed as a compatible
frame-type instance, not as a positive leg.

**LEG-4 CONFIRMED — '44 de 21' (1 frame type, 2 instances).**
@1161/@1840 share the '44-83-21-67' 4-gram (wider contexts differ:
'77-82-44-83-21-67-78-45' vs '22-42-44-83-21-67-78-49'), so two instances of
one frame type. "[44] de [21]" with 21 noun-class (registry): natural
genitive slot, no standing-value conflict. Confirmed as a compatible leg.

**@907/@1612 FENCED WITH STATED CAUSE (not independent legs).**
Both '55-83-[54/71]' windows parse under 83='de' technically, but both
neighbors are open (54/55, 71), so 'de' is untested — any 83 value would
parse. Fenced with cause: open-neighbor compatibility, contributes zero to
the lead; NOT counted as legs. Reopen when 55/54/71 resolve. This is the
bar's "else fence with stated cause" applied.

### Coordinated, not re-adjudicated (C4)

- @911 '64-83-59' ("qui de est"): kill-grade against unconditioned 83='de',
  owned by fence-911-de (2026-10-08), escalated to the red team via queued
  escalate-83-de-kill. Not counted, not re-decided.
- @1217 '77-83-92' ("le de"): formalized fence (fence-83-1217); 83 is the
  designated blocker with stated cause. Not counted.

## Per-clause pass/fail

- **C1: PASS.** Locus-fenced set defined and independently re-derived; census
  matches de-83-sweep exactly (15 windows, offsets, pre/follower counts).
- **C2: PASS.** 4 independent frame types confirmed (LEG-1..LEG-4:
  de+INF / formula-'de m' / 98-de-56 / 44-de-21), each parses under 83='de'
  with <=1 non-granted assumption; @907/@1612 fenced with stated cause, not
  silently dropped, not counted.
- **C3: PASS.** Zero 87-contact at any locus-fenced window; the 'cède' rival
  and @614/@1171 parses used by no leg. Leg independence from the excluded
  locus verified stream-side.
- **C4: PASS.** @911 and @1217 coordinated with their standing verdicts
  (escalated kill-grade / formalized fence); neither re-adjudicated nor
  counted as legs.

## Verdict: PROMOTE (independent legs confirmed)

The lead's independent legs stand confirmed on the locus-fenced set: 4
distinct frame types (LEG-1 de+INF incl. the battery-grade "de faire" leg,
LEG-2 formula-'de m' x3, LEG-3 98-de-56, LEG-4 44-de-21 x2), all independent
of the excluded @614/@1171 locus. The two open-neighbor windows @907/@1612
are fenced with stated cause per the bar — they neither support nor oppose
the lead.

This PROMOTE is on the lead's independent legs only. It is NOT a value
promotion of 83='de' and does NOT touch the escalated kill-grade of
unconditioned 'de' at @911 (fence-911-de / queued escalate-83-de-kill —
red-team business). No standing verdict contradicted or downgraded. No
duplication of de-83-sweep (full 15-window promote bar, null) or
de83-condition-set (11-window conditioned package, promote).

## Follow-ups

None required by this verdict. Related live items (queued separately, never
duplicated): escalate-83-de-kill (P1, red-team docket), de83-39-1334 (P3,
@1334 collision), cede-614-subject (P2, @614 adverse subject),
de83-adverse-restock's fenced @907/@1612 windows reopen when 55/54/71
resolve (no new target needed — state recorded here).

## Bookkeeping

- Report: this file.
- Queue: `de83-adverse-restock` -> status `verdict`, result `promote`,
  date 2026-10-09 (temp-file + rename; pre-write assert on queued/verdictless
  status; JSON re-validated post-write; only this target's entry touched).
- Lock `de83-adverse-restock.lock`: created on start, deleted on completion.
