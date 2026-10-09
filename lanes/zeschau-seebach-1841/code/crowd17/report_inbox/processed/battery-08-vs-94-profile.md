# Battery report — `08-vs-94-profile`

- Target id: `08-vs-94-profile`
- Claim: "Test directly whether 08's successor profile matches 94='ne' closely enough to merit a value hypothesis, or is an independent letter-class signature."

## Bar (verbatim, pre-registered)

> Hypothesis merits iff distributional match supports a value claim at battery grade; else keep as independent signature.

Restated as numbered clauses:

- C1: the 08/94 distributional match is strong enough (at battery grade) to support a "ne"-type value hypothesis for 08.
- C2 (else-arm): 08 is kept as an independent letter-class signature with the match recorded as a distributional fact only.

## Method

Re-derived the repaired stream in-session: 1,847 pairs, 96 types, asserts held.
`code/side-keyhunt/canonical.py` never used. Successor and predecessor censuses
re-computed byte-exact for 08, 94, and 12; a null baseline (Jaccard similarity
over all 1,596 ordered pairs of distinct cells with n≥15) was built for
calibration. Adopted as premises (not re-litigated): ce-08-31-frame PROMOTE
(08 fills a word-initial-letter slot), homophone-08-12-n NULL, {48,94}
homophone-set kill (protocol §7).

## Findings

- Census: n(08)=18, n(94)=37, n(12)=23.
- Successors — 08∩94 = {24, 29, 52, 65} (4 shared; Jaccard 0.118, cosine 0.175).
  08∩12 = {34} (1 shared; Jaccard 0.040). 94∩12 = {06, 44} (Jaccard 0.059).
- Null calibration: median Jaccard 0.097, p90 0.222, max 0.692. The 08–94
  match sits at the **60th percentile** — barely above median, nowhere near the
  top decile. It is not a distinctive distributional signature.
- Predecessors — the match collapses from the other side: 08∩94 = {45} only
  (Jaccard 0.032). 94's dominant predecessor is 62 (x9, the "il ne" frame);
  08's dominant predecessors are {60, 67, 37, 40} (x2 each) — letter cells,
  consistent with a word-internal letter-class signature. 08∩12 predecessors =
  {40, 41, 60} (Jaccard 0.125), closer than 08–94, but 12="n" is a *granted*
  letter and this battery's bar names 94, not 12.

## Per-clause pass/fail

- C1: **FAIL** — Jaccard 0.118 at the 60th percentile of the null baseline does
  not support a value claim at battery grade; the predecessor side (Jaccard
  0.032, disjoint dominant populations) actively weakens the affinity.
- C2: **FIRES** — 08 kept as an independent letter-class signature. The 08–94
  successor overlap is recorded as a distributional fact only; no 08 value
  named, no value hypothesis declared.

## Adverse answered

Per the target's adverse: no "ne"-type read is declared here — a red-team
clearance under §7 would be required for any such read, and the distributional
evidence does not merit one in any case. Consistent with (not duplicating)
homophone-08-12-n's "n"-sibling rejection. No standing/red-team verdict
contradicted or downgraded; §7 intact; canonical-stream caveat stands.

## Verdict

**NULL** — bar's else-arm: 08 keeps its independent letter-class signature.
No value named for 08.

## Follow-ups proposed (all verified ABSENT from battery-queue.json)

1. `08-letter-geometry` (P3) — census 08's full predecessor/successor letter
   geometry at battery grade to state the letter-class signature positively
   (word-initial vs internal, letter-neighbor inventory).
2. `val-08-31-letter` (P3) — name 08's letter value inside the "87 08 31"
   word frames (@881/@1488/@1520) under the ce-08-31-frame PROMOTE.
3. `08-vs-94-census-gated` (P4) — gated re-run of this match once the red team
   adjudicates the 94 functional split (dual94-r17018-scope input pending),
   which may change 94's dominant frames.

(Already-queued `08-position-profile` covers the word-position census and is
not re-proposed.)

## Bookkeeping

- Lock created on start, deleted on completion (verified gone).
- Queue: `08-vs-94-profile` → `status: verdict`, `result: null`, 2026-10-09
  (pre-write assert passed — was queued/verdictless; temp-file + rename; JSON
  re-validated; own entry only; no downgrade).
- R5005, sealed gates, red-team adjudication queue untouched.
