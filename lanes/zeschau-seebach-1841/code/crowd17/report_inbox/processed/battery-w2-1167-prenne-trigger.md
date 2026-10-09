# Battery report: w2-1167-prenne-trigger

Target: `w2-1167-prenne-trigger` (P3). Claim: "resolve W2's (@1167)
subjunctive trigger, or fence 'prenne'".
Date: 2026-10-09. Worker: battery worker (agent
50d82c3e-bffa-46d2-833c-9c1e2226f3a9, supervisor dispatch).
Lock `locks/w2-1167-prenne-trigger.lock` created 2026-10-09T10:45:32Z
(no pre-existing lock); deleted on completion.

Offset convention: @n = 0-based pair index in the repaired 1,847-pair stream
(matches battery-leftedge-13-55).

## Bar (verbatim from battery-queue.json, pre-registered before testing)

"resolve iff a subjunctive trigger is located for the joined '55-61-94'
'prenne' reading at @1167 with zero contradictions; else fence 'prenne' at
W2 with stated cause"

Numbered clauses (frozen; not modified after seeing data):

1. A subjunctive trigger is located for the joined '55-61-94' = 'prenne'
   reading at @1167.
2. The located trigger has zero contradictions.
3. (else-branch) If no such trigger is locatable, 'prenne' is fenced at W2
   with a stated cause.

Adverses: "13's class unresolvable at battery level (section-7 split or
sub-lexical - red-team territory)."

## Method

Read BATTERY-PROTOCOL.md and battery-queue.json first. Re-derived the
repaired 1,847-pair stream from `data/upstream-ct_R5005.txt` +
`code/side-keyhunt/repaired_offsets.json`, parsed per
`code/side-keyhunt/repair_parse.py` (byte-exact stride-2 pairing per row
offset); asserted 1,847 pairs and 96 distinct groups before testing.
`canonical.py` never used. R5005, sealed gates, red-team queue untouched.
Every count below re-derived in-session; no prior counts trusted.

## Window-level evidence

### The W2 window (byte-verified)

Formula `78-45-13-55-61-94` @1164-1169 (row a6_09), left context and right
context:

- @1161-1163: `83 21 67`
- @1164-1169: `78 45 13 55 61 94` (78@1164, 45@1165, 13@1166, 55@1167,
  61@1168, 94@1169)
- @1170-1176: `87 83 21 85 36 74 32` (87='ce' promoted)

Trigger space = every element that can precede the verb in its clause:
@1161-1166 plus any distant 'que'-class element upstream.

### Distributional re-verifications (in-session)

- `94-87`: exactly 1x stream-wide (@1169) — hapax confirmed. (W2's
  `94 87` = "ne ce" ungrammatical per leftedge-13-55; 94 != 'ne' here.)
- `55-61`: exactly 3x stream-wide (@576 W1, @1167 W2, @1205 W3) — confirmed.
- 13: n=12; followers 24x3, 66x2, 55x2, 93x2, 52x1, 76x1, 92x1 — matches
  the leftedge profile; preverbal particle, class open.
- French grammar premise: 'prenne' is an unambiguous present-subjunctive
  form (1st/3rd sg of prendre; no indicative reading). French present
  subjunctive requires a 'que'-class licensor. No non-'que' trigger exists
  outside fixed expressions.

### Trigger-candidate enumeration (clause 1)

1. **13@1166 (immediate pre-verbal).** The positional candidate. 13='que'
   is §7-blocked (46='que' banked, pencil). Blocked at battery level.
   Not available.
2. **67@1163 (et/veut — sole polyvalence).** As 'et': no trigger. As
   'veut': licenses subjunctive only via 'veut que' — no 'que' between 67
   and the verb (78, 45, 13 intervene). Excluded.
3. **78-45@1164-1165.** Noun-shaped (78='ver'-family lead; 45='ce' HOLD
   per A11). Nominals do not license subjunctive. Excluded.
4. **83@1161, 21@1162.** No 'que'-class standing; a second 'que' value
   would be a homophone set, which needs the 1690-uniformity machinery
   (adjudication venue, not battery). Position is wrong regardless (67,
   78, 45, 13 intervene between 21 and the verb). Excluded.
5. **Distant 46 ('que', banked).** Nearest upstream 46 is @954 — 213
   pairs before @1167. The span @955-1167 contains 7 finite verbs (24,
   promoted), 6 verb frames (80/89), 3 'on' subject pronouns (84), and
   zero 46. A single "que"-clause spanning 213 pairs across 7 promoted
   finite verbs contradicts the battery's clause-level frames. Not
   "located with zero contradictions" — excluded.
6. **00 ('pour', promoted) compounds.** "pour que" needs adjacent 46;
   the four `00-46` bigrams stream-wide are at @106, @545, @1545, @1680
   — none near W2. Excluded.
7. **Sub-lexical 13 / §7-split 13.** Red-team territory by the adverse
   itself. Not usable at battery level; reserved, not denied.

Result: the finite trigger space is exhaustively empty at battery level.
No candidate survives.

### Clause 2

Moot — no trigger was located.

## Per-clause pass/fail

1. Subjunctive trigger located for '55-61-94'='prenne' at @1167 —
   **FAIL** (kill grade; see below). Every element of the finite trigger
   space is excluded by standing verdicts (§7) or French grammar; the
   sole stream 'que' (46) is 213 pairs upstream behind 7 promoted finite
   verbs.
2. Located trigger has zero contradictions — **moot** (no trigger).
3. Else-branch: fence 'prenne' at W2 with stated cause — **EXECUTED**.

## Verdict: KILL

Clause 1 fails at kill grade: the W2 window forces the bar's resolve-arm
false. The trigger search is not inconclusive — it is exhaustive over the
finite trigger space (@1161-1166 plus the upstream 'que' scan), and every
candidate is excluded with stated cause. Per the bar's else-branch,
'prenne' is FENCED at W2:

**Fence (stated cause):** no subjunctive trigger for the joined
[55-61-94]='prenne' reading at @1167 is locatable at battery level.
13='que' is §7-blocked (46='que' banked); the sole polyvalence 67
(et/veut) cannot license subjunctive without 'que'; 78-45 is nominal;
83/21 have no 'que'-class standing; the nearest 'que' (46@954) is 213
pairs upstream across 7 promoted finite verbs. Since 'prenne' is an
unambiguous subjunctive form requiring a 'que'-class licensor, the
joined reading at @1167 is unlicensable. The fence is scoped to battery
level: a sub-lexical-13 or §7-split-13 trigger remains red-team venue.

No standing verdict contradicted, none downgraded, none re-litigated
(§7 blocks, the 46='que' bank, and the leftedge window reads used as
premises only).

### Adverse answered

13's class is NOT resolved here. The adverse ("13's class unresolvable
at battery level") is respected: 13='que' is used only as the standing
§7-block premise, and the fence explicitly reserves the sub-lexical /
§7-split 13 space to the red team. Nothing about 13's class is decided
at battery level.

### Follow-ups

None newly queued. The bar's surviving arm is `val-94-w2` (94 = non-'ne'
X at @1169) — already present in battery-queue.json. The red-team
residual (sub-lexical-13 trigger) belongs to the red-team adjudication
queue, which this worker does not touch.

## Bookkeeping

- Report: this file
  (`code/crowd17/report_inbox/battery-w2-1167-prenne-trigger.md`).
- `battery-queue.json`: `w2-1167-prenne-trigger` queued -> verdict/kill
  via temp-file + rename (pre-write assert confirmed queued/verdictless;
  JSON re-validated post-write). Own entry only.
- Lock `locks/w2-1167-prenne-trigger.lock` created on start, deleted on
  completion.
- `canonical.py` never used. R5005, sealed gates, red-team queue
  untouched.
- Standing §7 constraints respected throughout; 67 et/veut remains the
  sole polyvalence; no new value declared.
