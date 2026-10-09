# Battery report: val-92-93-equivalence

- Target id: `val-92-93-equivalence` (priority 3)
- Claim: "distributional equivalence test of 92~93 under the lane homophony standard (contact-profile overlap, n=22/14, current sole shared context ('13','62'))"
- Date: 2026-10-09
- Worker: battery worker (subagent 61cf502c-c50c-4e49-9f47-07ccd49e4349)
- Stream: repaired 1,847-pair / 96-type parse re-derived in-session from
  `data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`,
  parsed per `code/side-keyhunt/repair_parse.py` (asserts held: 1,847 pairs,
  96 types). `canonical.py` never used. R5005, sealed gate instances, and the
  red-team adjudication queue untouched. @-offsets are 0-based pair indices.
- Parent: `neque-79-twin-frame` (NULL, 2026-10-09), follow-up 1.

Terms (ASD-STE100): "homophony standard" = the lane's four-part test for two
groups being homophones (frequency uniformity + despatch-order cycling +
contact-distribution overlap + frame interchangeability), documented in
`code/crowd13/homophone-ab/PREREG.md` SET A bar and the 1690 cycling
doctrine. "Resolve" = the equivalence meets the standard at battery grade
(the homophone license itself is red-team venue per §7). "Kill the 7-gram
frame claim" = the parent claim "'13 {92|93} 62 94 79 14 60' is one frame"
dies; the repetition reduces to the 4-gram "94 79 14 60".

## Bar (verbatim from battery-queue.json, pre-registered BEFORE testing)

"resolve iff 92~93 meet the lane homophony standard; kill the 7-gram frame
claim iff rejected"

## Numbered pass/fail clauses (fixed before data examination)

The lane homophony standard (grounded in `code/crowd13/homophone-ab/PREREG.md`
SET A; the 1690 royal order's cycling doctrine). PROMOTE requires ALL of:

- **(a) Uniformity:** χ² vs uniform on (n92, n93); bar p > 0.05 (fail to reject).
- **(b) Cycling:** Wald–Wolfowitz runs test on the despatch-order 92/93
  membership sequence; bar |z| < 2 (interleaved; clumping kills).
- **(c) No predecessor segregation:** χ² on P(pre|92) vs P(pre|93) (pooled
  rare predecessors); bar p > 0.05. (The standard's kill clause for this
  sub-test is p < 0.01.)
- **(d) ≥2 frame-interchangeability legs**, positive and independent: each
  group attested in the other's signature frames at parallel rates, frames
  era-licensed; legs are per-frame-window, never the phenomenon under test
  itself.

Verdict rule:

- **C1 (resolve arm):** PASS iff 92~93 meet ALL of (a)–(d) → RESOLVE the
  equivalence at battery grade (the homophone license itself is red-team
  venue under §7, recorded as a package, not declared).
- **C2 (kill arm):** FIRES iff the standard rejects 92~93 — uniformity fails
  (p ≤ 0.05), or runs show clumping (|z| ≥ 2, clumped direction), or
  predecessor/successor segregation significant (p < 0.01), or zero frame
  interchangeability with similarity attributable to shared class alone →
  KILL the 7-gram frame claim; the twin reduces to the 4-gram "94 79 14 60".

## Method

1. Read BATTERY-PROTOCOL.md first. Created
   `code/crowd17/next-token/locks/val-92-93-equivalence.lock` on start
   (agent id + 2026-10-09T18:52:00Z); no stale lock present.
2. Re-derived the repaired stream byte-exact in-session (asserts 1,847/96
   held); `canonical.py` never touched.
3. Re-ran the parent battery's census independently (counts, indices,
   contact profiles, shared contexts) — all byte-confirmed.
4. Applied the four standard tests: χ² uniformity (df=1), Wald–Wolfowitz
   runs on the sorted 92/93 membership sequence (n1=22, n2=14), χ²
   predecessor/successor segregation with rare-cell pooling at two
   thresholds (pool<3, pool<4), and a window-complete frame-interchangeability
   audit of both groups' signature frames.
5. Checked for standing/red-team verdicts on 92~93 before testing: R20
   defers 93's value with cause (R20-039–047; R19-166's class grant stands);
   no ruling touches 92~93 equivalence or the 7-gram frame claim (the
   parent was a battery NULL). No §5.2 contradiction exists for either arm.

## Window-level evidence (all byte-exact, re-derived)

### Counts and loci

- n(92)=22 @ 49, 66, 203, 321, 330, 354, 356, 593, 683, 901, 978, 1022,
  1154, 1218, 1310, 1361, 1379, 1453, 1490, 1550, 1607, 1673.
- n(93)=14 @ 10, 102, 111, 159, 263, 479, 604, 734, 1540, 1555, 1685, 1761,
  1812, 1846.

### Contact profiles (full censuses)

- pre(92): 00×6, 11×3, 94×2, 84×2, 13×1, 16×1, 30×1, 31×1, 40×1, 46×1,
  81×1, 83×1, 98×1.
- fol(92): 79×2, 69×2, 60×2, 64×2, 62×2, 07×1, 29×1, 39×1, 44×1, 45×1,
  47×1, 50×1, 61×1, 63×1, 65×1, 67×1, 98×1.
- pre(93): 45×3, 13×2, 15×2, 94×1, 18×1, 35×1, 62×1, 67×1, 74×1, 85×1.
- fol(93): 62×2, 52×2, 00×1, 06×1, 29×1, 50×1, 54×1, 59×1, 61×1, 76×1, 88×1.
- Shared (pre,fol) contexts: exactly ONE — ('13','62') (the twin loci
  themselves: @1361 "13 92 62", @1685 "13 93 62"). Confirmed the parent's
  finding.

### Criterion (a) — uniformity

- χ²=1.7778 on (22,14) vs uniform, df=1, **p=0.1824** → PASS (p > 0.05).

### Criterion (b) — cycling

- Despatch-order membership sequence (92=A, 93=B):
  BAABBBABAAAABABABAAAAAAAAAABABAABBBB.
- 17 runs; E[runs]=18.111, sd=2.807, **z=-0.396**, |z| < 2 → PASS
  (interleaved; no clumping).

### Criterion (c) — predecessor segregation

- pool<3 table: 92=[6,3,1,0,2,10], 93=[0,0,2,3,1,8] on
  {00, 11, 13, 45, 94, POOLED}: χ²=11.6883, df=5, **p=0.0198**.
- pool<4 table: 92=[6,16], 93=[0,14] on {00, POOLED}: χ²=4.5818, df=1,
  **p=0.0323**.
- Successor segregation (control): χ²=0.3198, df=1, p=0.5718 — no
  successor segregation.
- The result is pooling-robust (p≈0.02–0.03 under both thresholds).
  → **FAILS the p > 0.05 bar** (but does not reach the standard's
  p < 0.01 sub-test kill clause — reported honestly as the marginal zone).

### Criterion (d) — frame interchangeability (window-complete audit)

- 92's signature frames vs 93's windows: 93 appears in 00-pre ×0, 11-pre
  ×0, 84-pre ×0, 79-fol ×0, 69-fol ×0, 60-fol ×0, 64-fol ×0. Sole partial
  hit: 94-pre ×1 at 93's @102 ('94 93 59') — but 92's 94-pre windows are
  '94 92 69' and '94 92 45': different followers, not the same frame.
- 93's signature frames vs 92's windows: 92 appears in 45-pre ×0, 15-pre
  ×0, 52-fol ×0. Sole partial hit: 13-pre ×1 — the twin locus itself.
- **Zero positive independent legs.** The sole shared context ('13','62')
  is the phenomenon under test (circular; the standard's legs must be
  independent of the claim being licensed). The residual overlaps
  (generic 62-follower ×2 each, one mismatched 94-pre window) are
  similarity attributable to shared class alone.
- → The standard's kill clause **fires**: "zero frame interchangeability
  with similarity attributable to shared class alone."

## Per-clause pass/fail

- **C1 (resolve arm): FAIL.** (a) passes, (b) passes, (c) fails the bar
  (p≈0.02–0.03 ≤ 0.05), (d) fires the standard's kill clause. The
  equivalence does not meet the lane homophony standard.
- **C2 (kill arm): FIRES.** 92~93 are rejected under the lane standard
  → KILL the 7-gram frame claim "'13 {92|93} 62 94 79 14 60' is one frame".

## Adverses answered

- **Marginal predecessor p (0.02–0.03, not <0.01):** recorded, not hidden.
  The equivalence standard requires ALL four criteria; (c) fails its
  p > 0.05 bar regardless, and (d)'s kill clause fires independently — so
  the rejection stands outside the marginal zone.
- **94='ne' interplay:** no 94-value claim made, ratified, or
  contradicted; 94's battery-promoted status adopted as given per the
  parent, untouched.
- **Circularity:** the ('13','62') shared context cannot serve as an
  interchangeability leg — it is the data the claim is meant to explain.

## Verdict: KILL (the 7-gram frame claim)

92~93 do not meet the lane homophony standard: predecessor distributions
diverge (χ² p≈0.02–0.03, pooling-robust) and, decisively, there is zero
frame interchangeability between the groups — their contact profiles are
segregated except for the twin phenomenon itself (00/11/79/69/60/64/52/45/15
frames are each group-exclusive; the single shared '94'-pre window is a
different frame). The 7-gram "one frame" claim "'13 {92|93} 62 94 79 14 60"
is therefore KILLED at battery grade, exactly as the parent's follow-up
anticipated. The genuine distributional observation reduces to the 4-gram
"94 79 14 60" (2× stream-wide, @1363 and @1687) — byte-confirmed, preserved.

## Scope (stated, not hidden)

- This kill applies ONLY to the 7-gram "one frame" claim. It names no
  value and kills no value/class for 92 or 93 individually. R19-166's
  class grant for 93 stands (R20 defers its value with cause); the
  09~92 (A6) hold stands; no standing or red-team verdict contradicted,
  downgraded, or re-litigated; §7 intact (no polyvalence declared or
  needed — the equivalence was rejected, not licensed).
- Canonical-stream caveat stands: rows a7_06/a8_05 offsets unvalidated
  (68/70). The twin loci sit on those rows; a future offset adjudication
  could re-open the contact geometry, not the equivalence test.
- No follow-ups required (kill verdict). Optional re-arm: `neque-79-rerun-gated`
  (already queued by the parent) covers the 4-gram's grammatical future.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-val-92-93-equivalence.md`
  (this file).
- Queue: `val-92-93-equivalence` queued → `verdict`/`kill`, 2026-10-09
  (pre-write assert passed — was queued/verdictless; temp-file + rename;
  JSON re-validated; own entry only; no downgrade).
- Lock `code/crowd17/next-token/locks/val-92-93-equivalence.lock` created
  on start, deleted on completion (verified gone).
- R5005, sealed gate instances, red-team adjudication queue untouched.
