# Battery report: bound-40-boundary-resolve — resolve 40='e' bound/free status stream-wide

Worker: subagent 083d06ac-8093-46e1-91a4-140beba5f0f2, 2026-10-09.
Lock: created fresh at 2026-10-09T14:18:48Z (no pre-existing/stale lock present).
Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json +
data/upstream-ct_R5005.txt), parsed like code/side-keyhunt/repair_parse.py
(replicated inline; asserts held: 1,847 pairs, 96 types). canonical.py never
touched. R5005, sealed gate instances, and the red-team adjudication queue
never touched. All numbers trace to the stream.

Provenance: follow-up #2 of battery-08-62-boundary-adjudication NULL
(2026-10-09). That battery fenced the 08|62 boundary question partly because
40's bound/free status had "no battery-grade ruling". The downstream hope:
a forced 40|08 boundary would make 08 word-initial at @922/@944 and license
NO-boundary at 08|62 there. This target resolves 40's cell-level status.

## Bar (verbatim, pre-registered)

"state 40's status with distributional byte evidence at battery grade; else fence"

## Bar restated as numbered clauses (fixed before testing)

- C1: state 40='e' bound/free status with distributional byte evidence at
  battery grade.
- C2 (else): fence the status question with stated cause.

Adverses: none listed.

Standing premises adopted (§7; never re-litigated): 40='e' is pencil ground
truth (registry: 40=["e","gt"]); the standing PROMOTE census
(boundary-40-letter-census, 2026-10-09) classified all 21 40-windows as
word-final (W) / word-internal (I) / word-initial (B) / fenced (U) on
granted-value neighbours only — adopted as the classification framework;
34='i' and 29='er' are the reference BOUND letters (08-position-profile
PROMOTE: a bound letter after 08 licenses NO boundary between 08 and that
letter); a word boundary is forced after/before a banked/promoted free word;
67 et/veut sole polyvalence.

## Method

Re-derived the repaired stream in-session byte-exact per repair_parse.py.
Byte-exact census: n(40), predecessor/follower distributions, all 21
windows with ±3 context, the '40 08' bigram, the '29 40' bigram, and the
'82 34 29 40' ("pre m i er e") crib. Bound/free defined distributionally:
BOUND = the cell never occurs at a word edge (always word-internal);
FREE = the cell occurs at word edges. Kill-grade test for BOUND: a single
standing-grade word-edge attestation of 40 falsifies it.

## Window-level evidence (@-offsets 0-based = 0b, 1-based in parentheses)

n(40) = 21, byte-confirmed in-session.

Predecessors: 29 x9, 78 x3, 88/97/96/74/50/03/48/61/56 x1 each.
Followers: 12 x1, 65 x3, 97 x1, 03 x2, 92 x1, 56 x1, 67 x3, 20 x1, 95 x1,
62 x1, 08 x2, 17 x2, 29 x1, 06 x1.

'40 08': exactly x2 — @921 (@922, row a5_09, ctx `49 74 74 40 08 65 71`)
and @943 (@944, row a5_10, ctx `01 07 50 40 08 62 98`).
'29 40': x9. '82 34 29 40' ("pre m i er e") crib: x2 — @759 (@760, row
a5_03, ctx `82 34 29 40 20 62 94`) and @1039 (@1040, row a6_03, ctx
`82 34 29 40 17 77 82`).

Adopted classification of the 21 windows (boundary-40-letter-census,
PROMOTE, verified against in-session bytes):
- Word-final (W): 11 windows (2, 5, 8, 9, 10, 15, 16, 17, 18, 19, 20) —
  including the two crib windows and 65=noun-cls, 67='et', 17='fois',
  92=verb-cls follower windows.
- Word-internal (I): 1 window (1: @63, `08 34 29 40 12 94 92` — 40 fuses
  rightward into letter-tier 12='n', "…erne…/…enne…" mid-word).
- Word-initial (B): 1 window (12: @848, `33 96 40 62 21 67` — forced
  boundary after promoted free word 96='par', so 40 begins a new word).
- Fenced (U): 8 windows (3, 4, 6, 7, 11, 13, 14, 21) — open neighbours at
  standing grade, including both '40 08' windows (@921/@943).

Decided windows: 11 W + 1 I + 1 B = 13. Edge rate: 12/13 ≈ 0.92.

Correction to the standing census (headline, no downgrade): its window-12
rationale says "row boundary a5_06/a5_07 falls between 96 and 40".
Re-derived row map shows a5_06 spans 1-based 826–850 and a5_07 starts at
851, so 0b848 (1-based 849) is a5_06-internal, not row-initial. The B
classification still holds on the standing "forced boundary after a free
word" rule (96='par' promoted), independent of the row-boundary claim.
The census's verdict (PROMOTE, finding grade) is unaffected: its material
deliverables (the 21-window classification, the 40|92 prior, the
word-final-dominance correction) stand.

## Per-clause results

- **C1: PASS.** 40='e' is a **FREE letter cell** — word-edge-capable,
  word-final-dominant — stated with distributional byte evidence:
  1. The BOUND hypothesis is dead at kill grade: the gloss-anchored pencil
     crib "la pre m i er e" over groups "11 70 82 34 29 40" on row a5_03
     places 40 word-final in "premiere" at 0b759 (@760) — manuscript
     ground truth, not a battery inference. A bound letter (never at a
     word edge) cannot be word-final.
  2. The second "premiere" crib at 0b1039 (@1040, a6_03) independently
     places 40 word-final before 17='fois' (prom, word-level): boundary
     "…40 | 17…" is standing-forced.
  3. Distributional: 12 of 13 decided windows put 40 at a word edge
     (11 W + 1 B); only 1 of 13 is word-internal (window 1, fusing
     rightward into 12='n'). P(edge | 40, decided) = 12/13 ≈ 0.92 —
     the opposite signature of the reference bound letters 34='i' /
     29='er'.
  4. Edge capability spans both edges: word-final (x11) and word-initial
     (x1, forced by 96='par'); internal capability exists (x1) — 40 is
     genuinely free, not forced-final.
- **C2 (else): does not fire.**

## Downstream consequence for the parent battery (08-62-boundary-adjudication)

The parent's downstream hope — "a forced 40|08 boundary makes 08
word-initial at @944 (and @922)" — is NOT established by this finding.
Free-40 **permits** a word boundary at 40|08 but does not **force** one:
the two '40 08' windows (@921/@943) have no standing-licensed ground
forcing a boundary in either direction (neighbours 74/50/08/62 open at
standing grade; consistent with the standing census's U classification of
both). Therefore 40's status does NOT license NO-boundary at 08|62: the
08|62 boundary question remains fenced exactly as the parent battery left
it. Re-open condition for the 40|08 boundary: a standing-licensed naming
act on 74, 50, 62, or 08, or a red-team value for 40's neighbours —
red-team/battery venue, not this target.

No standing or red-team verdict contradicted or downgraded; §7 intact
(67 sole polyvalence); canonical-stream caveat stands (rows a5_03/a5_09/
a5_10 unvalidated). R5005, sealed gates, red-team adjudication queue
untouched. No value named, no class declared, no kill executed.

## Verdict

**promote** (finding grade): 40='e' is a FREE letter cell —
word-edge-capable, word-final-dominant (12/13 decided windows at an edge;
11 W, 1 B, 1 I; 8 fenced). The BOUND hypothesis is dead at kill grade via
the gloss-anchored "premiere" crib. The 40|08 boundary at @922/@944 is
permitted but unforced; the parent battery's 08|62 fence stands.

## Bookkeeping

- Lock `locks/bound-40-boundary-resolve.lock` created on start (fresh, no
  stale lock), deleted on completion (verified below).
- Queue: `bound-40-boundary-resolve` -> `status: verdict`,
  `result: promote`, `2026-10-09` (pre-write assert: was
  `queued`/verdictless; temp-file + rename; JSON re-validated from disk;
  own entry only; no downgrade).
- R5005, sealed gates, red-team adjudication queue untouched.
