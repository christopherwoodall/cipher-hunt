# Battery `de83-condition-set` — verdict: PROMOTE (package)

Target: enumerate the surviving parse set under a conditioned 83='de'
(11 non-contested windows), delivering the conditioned candidate for red-team
adjudication. This verdict promotes the PACKAGED CANDIDATE — it does NOT
promote the value 83='de'. The unconditioned kill-grade at @911 stays owned by
fence-911-de and escalated to the red team via queued escalate-83-de-kill.
Date: 2026-10-09. Stream: repaired 1,847-pair parse
(`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`).
`canonical.py` never used. R5005, sealed gates, red-team queue untouched.
Lock created on start, deleted on completion.

Source: de-83-sweep null (2026-10-09,
code/crowd17/report_inbox/battery-de-83-sweep.md) — 15-window census
independently re-derived here: 83 n=15, offsets and neighbors match exactly
([228, 614, 898, 907, 911, 931, 1061, 1161, 1171, 1217, 1334, 1612, 1784, 1840];
predecessors 98 x5, 87 x2, 55 x2, 44 x2, 64/77/39/38 x1).

## Bar (verbatim, pre-registered)

"state the parse set over the 11 non-contested windows (exclude @614/@1171
'ce de', @911 'qui de est', @1217 'le de'); deliver the conditioned candidate
for red-team adjudication"

## Bar restated as numbered pass/fail clauses (pre-registered before testing)

- **C1:** Each of the 11 non-contested windows (@228, @898, @907, @931, @1061,
  @1161, @1334, @1612, @1784, @1829, @1840) gets an explicit parse under
  83='de' with an epistemic grade (compatible / conditional with stated open
  neighbors / positive leg), and every parse is traceable to the repaired
  stream.
- **C2:** The 4 excluded windows (@614, @1171, @911, @1217) are named with
  their standing grades from the sweep (open adverse / locus-fenced /
  kill-grade escalated / formalized fence) — excluded, not silently dropped —
  and the 'cède' rival at @1171 is recorded as the fence cause.
- **C3:** A single conditioned candidate statement is delivered (83='de'
  conditioned on the 11 windows, with the 4 exclusions and their causes),
  ready for red-team adjudication; nothing is promoted at battery level — the
  unconditioned kill-grade at @911 (escalated by fence-911-de) is not
  downgraded or re-decided.

## Method

Loaded the repaired stream per repair_parse.py (offsets from
repaired_offsets.json, pairing `[s[i:i+2] for i in range(o, len(s)-1, 2)]`);
re-derived the 83 census independently (match exact). Window-level reads use
only granted/penciled/promoted values: 82='m' pencil; 86 INF-class granted
(A9); 39='a' battery-promoted / table-registry LEAD (a-39, "a/à"); 24='faire'
battery-promoted (ne-24-profile) / registry verb-class; 98's French is
unconfirmed (frame-vient-parvenir kill on the 98='vient' claim; the
98-83-82-96-21 formula is formula-bound, value open).

## Window-level evidence: the 11 non-contested windows under 83='de'

| # | @    | context (83 marked) | parse under 83='de'              | grade            |
|---|------|---------------------|----------------------------------|------------------|
| 1 | 228  | 98 >>83 82          | "[98] de m[e]" (formula head)    | compatible       |
| 2 | 898  | 98 >>83 86          | "[98] de [86-INF]"               | compatible       |
| 3 | 907  | 55 >>83 54          | "[55] de [54]"                   | conditional      |
| 4 | 931  | 98 >>83 56          | "[98] de [56]"                   | compatible       |
| 5 | 1061 | 98 >>83 82          | "[98] de m[e]" (formula)         | compatible       |
| 6 | 1161 | 44 >>83 21          | "[44] de [21]"                   | compatible       |
| 7 | 1334 | 39 >>83 86          | "[39] de [86-INF]"               | conditional      |
| 8 | 1612 | 55 >>83 71          | "[55] de [71]"                   | conditional      |
| 9 | 1784 | 98 >>83 82          | "[98] de m[e]" (formula)         | compatible       |
| 10| 1829 | 38 >>83 24          | "[38] de faire"                  | positive leg     |
| 11| 1840 | 44 >>83 21          | "[44] de [21]"                   | compatible       |

Window notes:
- **#1/#2/#4/#5/#9 (98-heads):** 98 n=5; three take 82 (formula head,
  "vient de m" shape), one takes 86 (A9 INF-class — "de [INF]"), one takes 56.
  98's value is open, but 'de' imposes no new demand: whatever 98 is, the
  'de'-slot parses. Compatible.
- **#3 (55-83-54) and #8 (55-83-71):** both neighbors open (54/55, 71).
  No standing value contradicts 'de' at either window. Conditional.
- **#6/#11 (44-83-21 x2):** byte-parallel; "[44] de [21]" parses under
  'de' with no standing-value conflict. Compatible.
- **#7 (39-83-86):** conditional with cause. 39='a' is battery-promoted but
  registry LEAD tier ("a/à"), and "/a/ de [INF]" would be ungrammatical as
  "à de" — a live collision point, not a contradiction, exactly as graded
  in the sweep. Covered by queued de83-39-1334; not re-decided here.
- **#10 (38-83-24):** the sole fresh positive leg. Under battery-promoted
  24='faire' (ne-24-profile; registry class verb), "de faire" is grammatical
  French. Battery-grade leg (not red-team-granted) — recorded, not banked.

## Excluded windows (C2)

- **@614 (87-83-70):** open adverse. 'ce de' vs the 'cède' verb rival;
  frame-87-83-cede left the rival unproven at this locus. Excluded, unresolved.
- **@1171 (87-83-21):** locus-fenced. 'cède' parses cleanly
  ([55-61-94 word] cède [21], surrender-valence) — the stated fence cause.
  Excluded as fenced, not ignored.
- **@911 (64-83-59):** kill-grade against UNCONDITIONED 83='de'
  ("qui de est" ungrammatical; cheapest fences rejected). Owned by
  fence-911-de (2026-10-08), escalated to the red team; coordinated here,
  never downgraded. Excluded.
- **@1217 (77-83-92):** formalized fence (fence-83-1217): "le de"
  ungrammatical; 83 designated the blocker with stated cause. Excluded.

## Conditioned candidate (C3)

**Candidate:** 83='de' conditioned on the 11 windows
{@228, @898, @907, @931, @1061, @1161, @1334, @1612, @1784, @1829, @1840},
with @614 excluded as an open adverse, @1171 excluded as locus-fenced via
the 'cède' rival, @911 excluded as the kill-grade cell (unconditioned 'de'
already escalated — the red team decides whether the conditioned reading
survives it), and @1217 excluded via the formalized 'le de' fence (83 is
the designated blocker there). Delivered to the red-team docket (queued
escalate-83-de-kill, coordinated, not duplicated).

## Per-clause pass/fail

- **C1: PASS.** All 11 windows stated with stream-traced parses: 7
  compatible, 3 conditional with cause, 1 positive leg (battery-grade).
- **C2: PASS.** All 4 exclusions named with standing grades and causes;
  the 'cède' rival recorded as @1171's fence cause.
- **C3: PASS.** Conditioned candidate delivered for red-team adjudication;
  no battery-level promotion of the value; the escalated kill-grade finding
  untouched.

## Verdict: PROMOTE (package)

The enumeration is complete and the conditioned candidate is delivered —
that is the package being promoted. The value 83='de' is NOT promoted;
unconditioned 'de' remains kill-grade at @911 under red-team escalation.
No standing verdict contradicted or downgraded.

## Follow-ups

None required by this verdict. Related live items (queued separately, not
duplicated): escalate-83-de-kill (P1, red-team docket), de83-39-1334 (P3,
@1334 collision), cede-614-subject / de83-adverse-restock (@614 adverse).

## Bookkeeping

- Report: this file.
- Queue: `de83-condition-set` -> status `verdict`, result `promote`,
  date 2026-10-09 (temp-file + rename; pre-write assert on queued status;
  JSON re-validated post-write; only this target's entry touched).
- Lock `de83-condition-set.lock`: created on start, deleted on completion.
