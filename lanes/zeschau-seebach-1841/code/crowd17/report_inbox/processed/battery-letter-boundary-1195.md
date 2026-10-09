# Battery verdict: letter-boundary-1195

Worker: agent 958b8359-9e76-4d6a-a43c-ebf03d6f9a87. Date: 2026-10-09.
Lock: `code/crowd17/next-token/locks/letter-boundary-1195.lock` created 2026-10-09T21:04:15Z;
no prior lock existed; deleted on completion.
Stream: repaired 1,847-pair / 96-type parse (`code/side-keyhunt/repaired_offsets.json` +
`data/upstream-ct_R5005.txt`), parsed per `code/side-keyhunt/repair_parse.py`
(re-derived in-session: 1,847 pairs, 96 types; same totals as repair_parse.py).
`canonical.py` never touched. R5005, sealed gate instances, red-team adjudication
queue untouched. No observed values redacted.

## Bar (verbatim, pre-registered, from battery-queue.json)

"letter values named; composition test at the tie"

Numbered clauses (pre-registered BEFORE testing, per §2; hook brief adds the
dependency rule, quoted verbatim: "Workers must evaluate the dependency in the
bar and fence if unmet"):

1. Letter values are named inside the frame region (16, 64, neighbors).
2. A forced letter boundary breaks the offset tie at @1195-1200.
3. If clause 1's dependency is unmet, fence the locus-level test.

## Method

Byte-confirmed the locus on the repaired stream: 1-based @1195-1200 =
`82 16 96 82 16 64` = "m [16] par m [16] qui" (row a7_00, 0-based @1194-1199).
Neighbors: 1-based @1194 = 24, @1193 = 07, @1201 = 29, @1202 = 45.
The "offset tie" is the one recorded by battery-doubled-1195-offset-audit (NULL):
under offset 1 the doubled frame exists; under offset 0 the digit substring
"821696821664" re-pairs as "69 68 21 66 42" and the frame disappears entirely.
Row a7_00's offset is upstream EM choice, unvalidated (canonicality caveat).

Dependency audit: searched battery-queue.json (1,728 targets), the report inbox,
processed reports, and the claim/adverses history for any named letter value
for 16, 64, or any neighbor (24, 07, 45) inside the frame region.

## Findings

**C1: FAIL — the dependency is unmet.**

- 16: no letter value has been named anywhere in the pipeline. Standing
  battery results: val-16-a-vs-est NULL (16='a' vs 16='est' unresolved);
  val-16-187-bound NULL (16's class fenced at @187; clause-break arm killed at
  kill grade); w2-16-class NULL; val-16-84-role NULL; est-16-877-confirm KILL
  (16='a' at @877 dies if 77='le' holds). frame-82-16 (PROMOTE) eliminated
  16="même"/"ême" at kill grade, killed 16="mais" via the doubled frame, and
  eliminated infinitive — but named no value. No letter candidacy for 16 is
  even on the docket; letter-tier-16 has never been tested at battery grade.
- 64: promoted value "qui" (word tier, R15/R20 standing grant). Splitting 64
  into letter tier would contradict the standing grant — excluded, not
  available as a letter value.
- Neighbors: 24 has verb-class granted (24='en' @1693 is a red-team-docket
  item, not a battery fact); 45 = "ce" hold (A11, word tier); 07 has no value;
  29 = "er" is pencil ground truth (syllable tier, banked since before this
  target — not a newly named letter value that could arm the re-test).
- The long-banked 82 = m (pencil ground truth, letter tier) predates this
  target and does not, by itself, arm the bar: the bar's arming event is a
  named letter value *for 16, 64, or a neighbor* that would force a letter
  boundary across the phase tie, and no such naming exists.

**C2: MOOT — cannot fire while C1 fails.**
A letter-level composition test at the tie needs at least one letter-tier
item with a named value inside the frame region to force a boundary. The only
letter-tier items present (82 = m, banked; 29 = "er", banked) are phase-neutral:
under offset 0 they re-pair away, and no composition over them can force the
phase because forcing the phase is what the test would need to assume.

**C3: FIRES — the locus-level test is fenced with stated cause.**
Fence: evidentiary, re-openable. Cause: the bar's dependency (a named letter
value inside the frame region) is unmet as of 2026-10-09; no letter value for
16 has ever been named, 64 = "qui" is grant-blocked from letter tier, and no
neighbor carries a named letter value. This fence dissolves the moment a
letter value names for 16 (or 64, or a neighbor) at battery grade or higher.

## Scope

Fences only the locus-level letter-boundary test at @1195-1200. Untouched:
the doubled-frame object (doubled-1195-offset-audit NULL stands), row a7_00's
unvalidated offset, all 16 class/value verdicts, 64 = "qui", the banked letter
tier (82 = m, 40 = e, 34 = i, 29 = "er"), §7. No standing or red-team verdict
contradicted, downgraded, or re-litigated. Canonical-stream caveat stands.

## Verdict: NULL (fence executed — dependency unmet)

## Follow-ups proposed (all verified ABSENT from battery-queue.json; left for supervisor)

1. `letter-16-doubled-frame` (P4) — test whether any single French letter
   composes as 16 in the 11 "82 16" windows (byte census with ±2 context) so
   that a real French word forms at battery grade; a named letter for 16
   re-arms this target.
2. `tier-16-1195-audit` (P4) — tier-level census of 16 at @1195/@1198 under
   banked values, mirroring the val-74-letter locus-by-locus method: can
   letter-tier 16 be excluded at battery grade at the tie itself? A
   battery-grade exclusion narrows the tie's degrees of freedom even without
   a naming.
3. `offset-a7_00-16-value-gate` (P4) — re-arm letter-boundary-1195 once 16's
   value is named at battery grade or higher; composition test at the phase
   tie under the named value.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-letter-boundary-1195.md`.
- Queue: `letter-boundary-1195` -> `status: verdict`, `result: null`, 2026-10-09.
  Pre-write assert passed (was queued/verdictless). Wrote through
  `battery-queue.json.letter-boundary-1195.tmp` + atomic rename; no tmp
  leftover; disk re-validated; own entry only; no downgrade.
- Lock created 2026-10-09T21:04:15Z (no stale lock), deleted on completion
  (verified gone).
