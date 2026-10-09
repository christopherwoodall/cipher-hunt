# Battery report: 08-62-boundary-rerun-gated — re-fire of the 08|62 boundary C1/C2 on new standing grounds

Worker: subagent 65128fe3-9a2d-4e48-88b6-b267bf25dd19, 2026-10-09.
Lock: created fresh at 2026-10-09T21:19:19Z (no pre-existing/stale lock present).
Stream: repaired 1,847-pair / 96-type parse (code/side-keyhunt/repaired_offsets.json +
data/upstream-ct_R5005.txt), parsed via code/side-keyhunt/repair_parse.py
(load_rows + parse; asserts held: 1,847 pairs, 96 types). canonical.py never
touched. R5005, sealed gate instances, and the red-team adjudication queue
never touched. All numbers trace to the stream.

Provenance: follow-up #1 of battery-08-62-boundary-adjudication NULL
(2026-10-09), which fenced the 08|62 boundary question (C1/C2 fail, C3 fence)
because the fence rested purely on unvalued cells: 62's value/class, 08's
letter value, and 40's bound/free status.

## Bar (verbatim, pre-registered)

"decide the 08|62 boundary at both windows (@944/@1323) on the new standing
grounds; else re-fence"

## Bar restated as numbered clauses (fixed before testing)

- C1: decide the 08|62 boundary at W1 (@944, row a5_10) at battery grade on
  the new standing grounds — BOUNDARY or NO-BOUNDARY with stated evidence.
- C2: decide the 08|62 boundary at W2 (@1323, row a7_04) at battery grade on
  the new standing grounds.
- C3 (else): re-fence the boundary question with stated cause.

Adverses: none listed.

## Gate check (before testing)

The claim's gate: re-fire "iff the red team names 62's value or class
(redteam-62-split resolves) or a letter value for 08 is named
(val-08-31-letter / syllable-08-letter-value)". Gate status, verified in the
queue before testing:

- `val-08-31-letter` -> status verdict, result PROMOTE, 2026-10-09
  (report: code/crowd17/report_inbox/processed/battery-val-08-31-letter.md).
  Names 08='t' at battery grade with seven independent legs.
- `syllable-08-letter-value` -> status verdict, result PROMOTE, 2026-10-09
  (report: code/crowd17/report_inbox/processed/battery-syllable-08-letter-value.md).
  Corroborates battery-grade 08='t'.
- `redteam-62-split` -> still queued (red-team venue, unresolved).

The second gate arm fired (08='t' named at battery grade in both named
batteries). Both promotes are battery-grade and unratified; the claim names
them explicitly, so the gate is satisfied as written. Proceeding to C1/C2.

New standing grounds since the parent battery (adopted, never re-litigated):

1. 08='t' — battery-grade letter value (two PROMOTE verdicts, 2026-10-09).
2. 40='e' — PROMOTED FREE letter cell (bound-40-boundary-resolve, 2026-10-09);
   its downstream note is explicit: 40|08 is permitted but unforced at
   @921/@943, and "the parent battery's 08|62 fence stands" on 40's grounds.
3. 62-boundary-census — PROMOTE evidence package (2026-10-09), explicitly
   deciding nothing; feeds redteam-62-split. One new observation: @1349 is
   the sole window with a standing-decided boundary (FORCED NO-BOUNDARY at
   34|62, forced by bound letter 34='i' fusing rightward) — 62 sits
   word-internal there under standing rules.
4. 62's value/class remains open (62='il' killed at kill grade, R19-106/
   R20-125; class is red-team venue).
5. Adopted 08-position-profile (PROMOTE) still classifies both loci as
   undecided on the right side (position, not value — naming 't' does not
   move the profile).

Standing premises adopted (§7): pencil GT (11=la, 70=pre, 82=m, 34=i,
29=er, 40=e, 46=que); granted (87=ce, 64=qui, 96=par, 17=fois, 79="tout"
A5, 00="pour" A9, 84="on" A15, 47="ce" A4); provisional (59=est, 77="le");
boundary rules battery-licensed: a boundary is forced after/before a
banked/promoted free word; a bound letter after 08 licenses NO boundary
between 08 and that letter. §3 bars inventing values for unvalued cells;
§7 sole-polyvalence (67) intact.

## Method

Re-derived the repaired stream in-session byte-exact per repair_parse.py.
Byte-exact bigram census for '08 62'; ±6 context at both loci with
row-internal check; re-tested every candidate decision route from the
parent report against the new standing grounds, plus any route the new
grounds open.

## Window-level evidence (@-offsets, 0-based, repaired stream)

'08 62' bigram: exactly x2 stream-wide — @944 and @1323 (re-verified
byte-exact in-session; parent reported the same).

- W1 @944 (row a5_10, row-internal):
  `64 37 01 07 50 40 | [08] 62 98 | 96 86 01 77`
  (pre=40, fol=62, fol2=98)
- W2 @1323 (row a7_04, row-internal):
  `98 15 24 03 29 80 | [08] 62 98 | 56 30 06 62`
  (pre=80, fol=62, fol2=98)

With 08='t': W1 = "...50 40 t [62] 98 96..."; W2 = "...29 80 t [62] 98 56...".

### Decision routes re-tested on the new standing grounds

FOR BOUNDARY (08|62 = boundary):
1. Follower-is-free-word: FAIL — 62 still unvalued; 62='il' killed at kill
   grade; no standing free word stands at 62. 08='t' does not change the
   follower.
2. 08-is-word-final: FAIL (circular) — deciding the boundary via 08's
   word-finality presupposes the 08|62 boundary itself. The
   08-leftattach-944-1323 route stays fenced; naming 't' does not un-fence
   it (the fence rested on the boundary presupposition, not on 08's value),
   and invoking 't'-finality to decide would assume the claim under test.
3. 62-as-subject forcing a pre-62 clause boundary ('62 94' x9 shape):
   REJECTED — using the shape to force the boundary names a class for 62,
   encroaching on redteam-62-split (red-team venue); barred by §3 and §7.
   The 62-boundary-census kept the shape as distributional-only evidence.
4. The '08 | 62 98' geometry (order-control-08-62): REJECTED as a license —
   conditional on the fenced left-attachment route; adopting it as the
   boundary decision remains circular.

FOR NO-BOUNDARY (08|62 internal):
1. Follower-is-bound-letter: FAIL — 62 is unvalued, not a bound letter.
2. 08-forced-word-initial at the window: FAIL — @944: 40|08 is
   permitted-but-unforced (bound-40 downstream note, standing); @1323:
   pre=80 unvalued, no forced boundary before 08.

New routes the new grounds might open:
3. @1349 transfer (62 word-internal after bound 34='i'): REJECTED — that
   decision is window-local, forced by 34='i' being a BOUND letter (a bound
   letter fuses rightward). 08='t' is a FREE letter (word-edge-capable: 08
   word-initial at @881/@1488/@1520/@1592 per the adopted position census;
   bound letters never sit at word edges), so no analogous forced fusion
   exists at @944/@1323. Transferring a tier claim for 62 from @1349 would
   name 62's tier — red-team venue, barred.
4. French-word composition with 08='t': UNSTATABLE — NO-BOUNDARY would need
   "t"+"62..." inside a French word and BOUNDARY would need 't' word-final
   with 62 word-initial; 62's value/tier is unknown, and §3 bars inventing
   it. No composition test is statable at battery grade.

## Per-clause pass/fail

- C1 (W1 @944): FAIL. 08='t' resolves one unvalued cell but supplies no
  boundary decider: boundary-forcing needs a free-word follower (62
  unvalued) and no-boundary-forcing needs a bound-letter follower or a
  forced word-initial 08 (40|08 permitted-but-unforced). All routes fail
  or are circular/off-limits.
- C2 (W2 @1323): FAIL. Same cause; 08's position reading remains
  undetermined (pre=80 unvalued), so not even a conditional word-initial
  route exists.
- C3: RE-FENCE EXECUTED with updated stated cause:
  1. The gate's new ground (08='t') does not move the boundary: the parent
     fence's decider gap was the follower's status, and 62 remains unvalued
     (62='il' killed; class red-team venue, redteam-62-split queued).
  2. 40='e' FREE permits but does not force 40|08 (bound-40 downstream
     note, standing) — 08 is not word-initial at @944 at battery grade.
  3. @1349's word-internal-62 is window-local (forced by bound 34='i') and
     does not transfer without a tier claim for 62 (red-team venue).
  4. The adopted 08-position-profile (PROMOTE) still classifies both loci
     as undecided on the right side; deciding the boundary here would
     contradict that standing verdict.
  5. No standing-licensed decider exists on the new grounds, and no
     standing-licensed ground forbids the boundary either.

Not kill grade: the fence rests on unvalued cells (62's value/class/tier),
not on a forced contradiction. A naming act on 62 reopens the question. No
standing or red-team verdict contradicted, downgraded, or re-litigated; §7
intact; canonical-stream caveat stands (rows a5_10/a7_04 unvalidated).

## Verdict

**null** — re-fence executed. The gate fired (08='t' named at battery grade
in the two named batteries), but on the new standing grounds the 08|62
boundary still cannot be decided at battery grade at either window.

## Follow-ups (nulls regenerate work; all verified ABSENT from battery-queue.json, 2026-10-09)

1. **08-62-boundary-rerun-62value** (P3, gated) — re-fire this target's C1/C2
   once 62's value, class, or tier is named (redteam-62-split resolves, or
   any battery verdict names 62's tier/value). Bar: decide the 08|62
   boundary at both windows on the then-standing grounds; else re-fence.
   Evidence: this report; the fence rests purely on 62's open cells.
   Adverses: none.
2. **seg-80-08-1323** (P4) — test the 80|08 left edge at W2: 80 is 08's
   predecessor at @1322-1323 and is unvalued. A forced boundary at 80|08
   makes 08 word-initial at @1323, which licenses NO-boundary at 08|62
   there (a word-initial letter fuses rightward). Narrower than the whole
   boundary question; does not touch 62. Bar: state 80's class/tier with
   byte evidence, or fence the left-edge route. Evidence: this report's W2
   context. Adverses: none.
3. **t62-composition-inventory** (P4, gather-only) — census French t-initial
   word shapes ("t"+letter compositions) to bound what 62's tier/value
   would have to be under a no-boundary reading at @944/@1323; feeds the
   62-value docket without naming. Bar: evidence package only, no
   adjudication. Evidence: 08='t' battery verdicts. Adverses: none.

## Bookkeeping

- Lock `locks/08-62-boundary-rerun-gated.lock` created on start (fresh, no
  stale lock), to be deleted on completion.
- Queue: `08-62-boundary-rerun-gated` -> `status: verdict`, `result: null`,
  `2026-10-09` (pre-write assert: was `queued`/verdictless; target-id-unique
  temp file `battery-queue.json.08-62-boundary-rerun-gated.tmp` + atomic
  rename; disk re-validated; own entry only; no downgrade).
- R5005, sealed gates, red-team adjudication queue untouched.
