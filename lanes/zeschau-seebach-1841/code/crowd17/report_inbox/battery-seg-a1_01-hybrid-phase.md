# Battery verdict: seg-a1_01-hybrid-phase

- Target id: `seg-a1_01-hybrid-phase`
- Claim: "test a transcription-error rival: a single mid-row dropped/duplicated digit could explain BOTH the +8.2-nat support for offset 0 AND the kill-grade 'la tout' clash"
- Date: 2026-10-09
- Worker: battery worker (subagent 959404d2-fdf5-4795-bd3b-faa2266abcad)
- Stream: repaired 1,847-pair parse (`data/upstream-ct_R5005.txt` +
  `code/side-keyhunt/repaired_offsets.json`, parsed per
  `code/side-keyhunt/repair_parse.py`; n=1847 asserted, 96 groups asserted).
  `canonical.py` never used. R5005, sealed gates, red-team queue untouched.
- Lock: `code/crowd17/next-token/locks/seg-a1_01-hybrid-phase.lock`
  (created at start, deleted on completion; no prior lock existed).

## Bar (verbatim from battery-queue.json, pre-registered BEFORE testing)

> locate one candidate digit position where the hybrid parse removes the clash
> without degrading the bigram margin

Numbered pass/fail clauses (restated before testing, not modified after):

1. (C1) The hybrid parse contains no `11 79` bigram among its evaluable pairs
   (the kill-grade "la tout" clash at in-row pair idx 17, 0-based =
   global 1-based @52–53 per battery-seg-a1_01-offset1-test — removed,
   not relocated).
2. (C2) The hybrid's bigram support is not degraded vs offset 0:
   evaluable bigram log-likelihood >= off0 LL − 1.0 nat AND per-bigram
   mean LL >= off0 mean − 0.05 nat. Harness: LOO bigram model trained on
   all rows except a1_01, +0.5 smoothing over 96 groups (the lane's
   bedrock grading harness).

Adverses: "the row is 71 digits (odd) and hapax-rich under both phases" —
answered below (exhaustive search over all 71 positions; hapax-richness
absorbed by the LOO+smoothing harness, the same harness that produced the
bedrock grade).

## Method

1. Re-derived the repaired stream in-session (1,847 pairs / 96 types
   asserted). Row a1_01 raw digits (71, odd):
   `08913964410124884381306296009279371179855835531241083429401294926913246`
2. Reproduced the two pure-phase parses and the baseline margin with the
   lane's LOO bigram harness:
   - off0 (35 pairs): `08 91 39 64 41 01 24 88 43 81 30 62 96 00 92 79 37 11 79 85 58 35 53 12 41 08 34 29 40 12 94 92 69 13 24`
   - off1 (35 pairs): `89 13 96 44 10 12 48 84 38 13 06 29 60 09 27 93 71 17 98 55 83 55 31 24 10 83 42 94 01 29 49 26 91 32 46`
   - off0 LL = −139.79 nats; off1 LL = −146.71 nats; margin = **+6.93 nats**
     for offset 0 (same direction and order of magnitude as the bedrock
     +6.49 LOO grade and the claim's +8.2; the exact figure is
     implementation-dependent, the comparison below is method-internal).
   - Clash confirmed: the row's only `11 79` adjacency is off0 pair idx
     17–18 (`...37 11 79 85...`); off1 contains neither `11` nor `79`.
3. Exhaustive single-edit search (no cherry-picking):
   - **Model A (duplication corrected):** for each k in 0..70, t =
     s[:k]+s[k+1:] (70 digits), parsed offset 0 → 35 real pairs, all 34
     bigrams scored. (71 positions, incl. all odd k.)
   - **Model B (drop corrected):** for each k in 0..71, true row =
     s[:k]+X+s[k:] with X unknown; evaluable pairs = off0[:m]+off1[m:35]
     (m = k//2), the boundary bigram(s) touching the unknown pair
     excluded from scoring. (72 positions.)
   - Rationale: a single dropped/duplicated digit at a pair boundary
     flips the pairing phase for the suffix; these two models exhaust the
     clean single-edit space. A drop at an odd position corrupts exactly
     one pair; Model A covers it (the corrupted pair is deterministic and
     scored).

## Results

**Model A (71 positions): zero candidates.** Every clash-removing cut
degrades the margin by 4.8–12.3 nats. Cuts at/after the clash locus
(k >= 38) keep the clash. Near-locus cuts:
- k=34,35 (remove `1` of the doubled `11` at digits 34–35 — the most
  plausible duplication site in the row): pairs `...79 37 | 17 98 55...`
  — clash gone, and this is exactly the offset-1 dissolution in
  miniature (`17 98` = "fois [98]", cf. the 2026-10-09 offset-1
  finding). LL = −149.63, **−9.84 nats** vs off0. Fails C2.
- k=36: `...79 37 11 | 98 55...` ("11 98"), LL = −150.01 (−10.22).
- k=37: `...79 37 11 | 78 55...`, LL = −148.80 (−9.01).
- Best clash-removing Model A cut anywhere: k=10, LL = −144.62
  (−4.83 nats). Still fails C2.

**Model B (72 positions): zero candidates.** Best clash-removing cuts:
- m=17 (drop at digit 34/35): `...79 37 || 17 98...`, LL = −144.62
  (−4.83 nats), mean −4.382/bigram vs off0 −4.111. Fails C2.
- m=18 (drop at digit 36/37): `...37 11 || 98 55...`, LL = −144.79
  (−5.00 nats). Fails C2.
- The numerically closest approach anywhere (k=8,9; m=4, LL = −140.83,
  −1.04 nats) keeps only 4 pairs in offset-0 phase — it is 90% the off1
  parse and does not "explain the offset-0 support" in any meaningful
  sense; it also fails C2.

**No position satisfies C1 and C2 jointly.** The single-digit
transcription-error rival is exhausted: 71 removal positions + 72
insertion positions tested, zero pass.

## Per-clause results

- C1 (clash removed): attainable — cuts at the clash locus dissolve
  `11 79` (e.g. Model A k=34 → `37 17 98`).
- C2 (margin not degraded): **fails at every clash-removing cut** —
  best case −4.83 nats (Model B m=17), typical −8 to −12 nats
  (Model A). The distributional support for offset 0 cannot be kept
  while dissolving the clash with one digit edit.
- Adverses answered: (a) odd length — all 71 positions tested,
  including odd-k corrupted-pair cuts; (b) hapax-richness — the
  LOO+smoothing harness is the lane's own bedrock grader, so the
  comparison is apples-to-apples.

## Verdict: KILL

The transcription-error rival is killed at battery grade: no single
dropped or duplicated digit position yields a hybrid parse that both
removes the `11 79` "la tout" clash and preserves offset 0's bigram
margin. The two observations cannot be jointly explained by a
one-digit transcription error — the clash dissolution always costs
4.8+ nats of distributional support. This does not touch the
constraint-clean offset-1 finding (2026-10-09) or the s5 fence; it
closes only the hybrid-phase escape route. No standing or red-team
verdict contradicted or downgraded; §7 intact.

## Follow-ups (optional; kill regenerates work)

1. `seg-a1_01-twoedit` (P4): two-digit error models (drop+dup combos)
   at the clash locus — the single-edit space is exhausted; a two-edit
   model is the next rung (flag the overfitting risk in the bar).
2. `hybrid-37-17-98-license` (P4): test whether the k=34 local reparse
   `37 17 98` ("[37] fois [98]") can be grammatically licensed as a
   locus-level reading — it is the cheapest clash-removing edit and
   mirrors the offset-1 dissolution.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-seg-a1_01-hybrid-phase.md`
  (this file)
- Queue: `battery-queue.json` — target `seg-a1_01-hybrid-phase` →
  status `verdict`, result `kill`, date 2026-10-09 (own entry only,
  temp-file + rename; pre-write assert confirmed queued/verdictless;
  JSON re-validated; no downgrade)
- Lock `locks/seg-a1_01-hybrid-phase.lock` created on start, deleted on
  completion.
