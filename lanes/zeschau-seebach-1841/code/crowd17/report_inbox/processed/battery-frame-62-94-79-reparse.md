# Battery report: frame-62-94-79-reparse

Worker: 5ede57af-f347-417a-8dc6-1ad892f55513. Date: 2026-10-09.
Stream: repaired 1,847-pair / 96-type parse (code/side-keyhunt/repaired_offsets.json +
data/upstream-ct_R5005.txt), re-derived in-session via code/side-keyhunt/repair_parse.py.
Asserts held (1847 pairs, 96 types). canonical.py never used. R5005 never touched.
Sealed gates and the red-team adjudication queue untouched.

Indexing: @i = 0-based pair index on the repaired stream.

## Bar (verbatim, pre-registered)

"resolve iff the frame parses under the newly named values; else fence '94 79' as a
genuine anomaly with stated cause (non-standard 'tout' placement / idiolect artifact,
or word boundary inside 79-14-60)"

Numbered clauses:

1. Dependency check: 14 and/or 60 have been named (value or class at battery grade
   or better) since the parent battery (frame-62-94-79, 2026-10-08).
2. If clause 1 passes, the frame "62 94 79 14 60" parses as grammatical French under
   the newly named values at BOTH instances.
3. If clause 1 fails, fence '94 79' ("ne tout", the 2-window exclusive bigram) as a
   genuine anomaly with a stated cause: non-standard 'tout' placement (idiolect /
   scribal artifact) or a word boundary inside 79-14-60.

## Method

Re-derived the repaired stream in-session; no prior counts trusted. Verified the
'62 94 79 14 60' windows, the '94 79' and '14 60' bigram census, and the naming
status of 14 and 60 from the table registry (code/table-grid/table-registry.json),
the battery queue verdicts, and the report inbox. Adopted the parent battery's
eight exhausted candidate families (a)-(h) without re-litigation; checked only what
changed since 2026-10-08.

## Window-level evidence

Both windows byte-confirmed on the repaired stream:

- Instance A @1362 (row a7_06): `... 35 13 92 | 62 94 79 14 60 | 03 30 82 ...`
  = "[35] [13] que[46-slot: 92] [62] ne[94] tout[79] [14] [60] [03] pas[30] m[82]".
  "ne...pas" brackets "tout [14] [60] [03]" (94@1363 -> 30@1368).
- Instance B @1686 (row a8_05): `... 65 13 93 | 62 94 79 14 60 | 27 46 24 ...`
  = "[65] [13] [93] [62] ne[94] tout[79] [14] [60] [27] que[46] [24] [85]".
  "ne...que" brackets "tout [14] [60] [27]" (94@1687 -> 46@1692).

Distributional facts (re-derived): '94 79' occurs exactly 2x, both inside this
frame, zero elsewhere. '14 60' occurs exactly 2x, both inside this frame, zero
elsewhere. The 5-gram is byte-identical x2. Parallel left edges "13 92" / "13 93"
immediately before 62 at both windows (a formulaic repeated phrase).

## Clause 1: dependency evaluation — FAIL (dependency unmet)

- 14's value: NOT named. Registry: 14 absent. Global 14='le' kill-grade dead
  (le-14-kill-1121). Only locus-level readings exist ('le' clitic @178,
  det-14-clitic-178 PROMOTE 2026-10-09 — locus-level, not a value). tout-slot-14
  (the designated 14-naming battery) returned NULL.
- 60's value: NOT named. Registry: 60 absent. 60 stands at verb-class battery
  level only; noun-60 KILLED 60's masculine-noun value at kill grade (2026-10-09,
  independent windows @1338 'qui 60' and @700 'ne 60' force verbal slots; cleaner
  rival 60=masculine adjective demonstrated). Whether 60 is adjectival, verbal,
  or polyvalent is red-team venue (poly-60-redteam gated). No positive value named.

Since the dependency ("once 14 and/or 60 are named") is unmet, clause 2 cannot
fire. The bar's "else" arm (clause 3) fires.

## Clause 3: fence of '94 79' — EXECUTED

'94 79' ("ne tout") is fenced as a genuine anomaly with stated cause.

Stated cause. Under standing values — 94='ne' (STRONG LEAD), 79='tout' (red-team
granted A5), 30='pas' promoted, 46='que' pencil — both instances place 'tout'
between 'ne' and the verb slot inside genuine 'ne...pas' / 'ne...que' brackets.
That order is ungrammatical in 1841 French: 'tout' must follow the verb
("il ne [V] pas tout") or be the subject ("tout [V]"), and 'ne' cannot open a
clause. The parent battery exhausted eight single-assumption candidate families
for 14/60 (a)-(h); all fail, most on this 'tout'-placement wall. Since then,
noun-60's KILL removed the last surviving lexical escape (14=determiner/adjective
+ 60=noun is now dead at kill grade), and 62='il' was killed at kill grade
(R20-125) — neither change moves the wall, which is structural and sits between
'ne' and 'tout' regardless of 62/14/60.

Two candidate mechanisms for the anomaly, recorded as disjunctive (battery grade
cannot discriminate):

(a) Non-standard 'tout' placement — a 2-window scribal/idiolect artifact. The
    byte-identical 5-grams with parallel "13 [92/93]" left edges read as a
    repeated formula, which raises the prior of a formulaic or idiolectal
    construction rather than two independent errors.

(b) Word boundary inside 79-14-60 — a mis-segmentation at these loci. Both rows
    (a7_06, a8_05) are among the 68 upstream rows whose offsets are unvalidated
    under the canonicality caveat; a pair-phase error at these windows is not
    excluded. This mechanism is compatible with 79='tout' standing.

Fence scope: evidentiary, re-openable. Re-opens iff (i) 14 and/or 60 are named
and the frame parses under the named values (the original re-test), (ii) a
licensed resegmentation composes a French word at either locus, or (iii) the
94='ne' lead is overturned (the fence rests on it).

## Adverse answered

"'94 79' ('ne tout') is a 2-window exclusive bigram" — adopted as the anomaly's
distributional signature (2x, both inside the frame, zero elsewhere); the fence
is the answer, not a dismissal.

## Scope

Locus-level fence of the '94 79' bigram at @1363/@1687 only. Untouched: the
parent frame-62-94-79 NULL, tout-slot-14 NULL, noun-60 KILL, 94='ne' STRONG LEAD,
79='tout' A5 grant, 14's and 60's open values, all standing/red-team verdicts,
§7. No verdict contradicted, downgraded, or re-litigated. Canonicality caveat
stands (rows a7_06/a8_05 unvalidated).

## Verdict

**NULL (fence executed).** The dependency for the re-test is unmet (neither 14
nor 60 named); the bar's "else" arm fires and '94 79' is fenced as a genuine
anomaly with stated cause. No standing verdict is contradicted.

## Follow-ups (null regenerates work; all verified ABSENT from battery-queue.json)

1. **ne-tout-79-corpus** (priority 4): corpus census of pre-verbal "ne tout [X]"
   in 1841 French (61M-char corpus, HTTP-500 stub excluded). Bar: >=1 grammatical
   attestation re-opens the frame (licenses the order); a zero hardens fence
   mechanism (a) at grammaticality grade.
2. **seg-79-14-60-residual** (priority 4): resegmentation test at @1362-1366 and
   @1686-1690 for a word boundary inside 79-14-60. Bar: re-opens iff a licensed
   resegmentation composes a French word at either locus; else fences the locus
   as a segmentation residual under the canonicality caveat.

## Bookkeeping

Report: code/crowd17/report_inbox/battery-frame-62-94-79-reparse.md. Queue
target `frame-62-94-79-reparse`: pre-write assert passed (status queued,
verdictless); will be set to status verdict / result null via target-id-unique
temp file `battery-queue.json.frame-62-94-79-reparse.tmp` + atomic rename; own
entry only; no downgrade; no tmp leftover (verified). Lock created 2026-10-09T21:06:42Z
(no stale lock), deleted on completion (verified). R5005, sealed gates, red-team
adjudication queue untouched.
