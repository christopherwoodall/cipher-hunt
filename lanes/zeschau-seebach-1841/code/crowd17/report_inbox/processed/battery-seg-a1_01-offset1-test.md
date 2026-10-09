# Battery verdict: seg-a1_01-offset1-test

**Target:** `seg-a1_01-offset1-test` (priority 2)
**Date:** 2026-10-08
**Worker:** session-12a40a4c (cron worker)

## Bar (verbatim from battery-queue.json)

> offset 1 dissolves the 'la tout' clash but must beat the +6.49 LOO bedrock grade - do not run as a single-window rescue

Numbered clauses:
1. Offset 1 dissolves the 'la tout' clash (the 11–79 @52–53 bigram on row a1_01) — verified on the full row, not just the clash window.
2. Offset 1 beats the +6.49 nats LOO bedrock grade for offset 0 with **independent evidence** (formula checks, crib-adjacent rows) across the full row.
3. The decision is not a single-window rescue: evidence must span the full 35-pair row, not rest on the @52–53 window alone.

Adverses: none stated. Context: s5-la-tout-adjudicate null (2026-10-08) — the 'la
tout' hapax @52–53 sits on a1_01 at PROBABLE offset 0; the alternative offset 1
must be tested against the full row with independent evidence. The sibling
red-team docket item `redteam-la-tout-fence` handles the venue; this battery is
the offset test only and does not decide banking.

## Method

Read `BATTERY-PROTOCOL.md` first; created
`code/crowd17/next-token/locks/seg-a1_01-offset1-test.lock` on start (agent id +
UTC timestamp), deleted on completion. All counts re-derived from the repaired
1,847-pair stream (`code/side-keyhunt/repaired_offsets.json` +
`data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`;
`canonical.py` never touched). R5005, sealed gates, and the red-team queue
untouched.

Row a1_01 raw digits (71 digits, odd length):
`08913964410124884381306296009279371179855835531241083429401294926913246`
Repaired offset: **0** (bedrock grade PROBABLE, LOO +6.49 nats).

Two full-row parses:
- off0 (35 pairs): `08 91 39 64 41 01 24 88 43 81 30 62 96 00 92 79 37 11 79 85 58 35 53 12 41 08 34 29 40 12 94 92 69 13 24`
- off1 (35 pairs): `89 13 96 44 10 12 48 84 38 13 06 29 60 09 27 93 71 17 98 55 83 55 31 24 10 83 42 94 01 29 49 26 91 32 46`

## Window-level evidence

### Clash dissolution (clause 1)
- Off0: `11 79` bigram present at in-row idx 17 (= global @52–53, the s5 window
  `92 79 37 11 79 85`); full-row scan finds this as the row's only 11–79 adjacency.
- Off1: **neither `11` nor `79` occurs anywhere in the 35-pair row** — the clash
  is dissolved, not relocated. Full-row verified.

### Independent evidence (clause 2)
1. **Formula checks — NEGATIVE.** None of the lane's three known formula/crib
   strings occurs in a1_01's raw digits at any phase:
   - `9883829621` (parvenir-stem, confirms a2_01/a6_04/a8_09): no raw occurrence.
   - `7778948206` (4× repeat): no raw occurrence.
   - `117082342940` (la-première crib): no raw occurrence.
   No formula repeat aligns pair-phase only under offset 1. Nothing in the
   bedrock's "formula evidence supersedes LOO" class supports offset 1 here.
2. **Crib-adjacent rows — NEGATIVE.** The crib occurrences live at raw 1532/2108
   (rows a5_03, a6_03), far from a1_01; the 3-occurrence formula standard gives
   no discriminating fact for this row.
3. **Distributional re-derivation (independent of the bedrock LOO number).**
   Bigram log-likelihood of the full row, trained leave-one-row-out on the
   repaired stream (all rows except a1_01, +0.5 smoothing over 96 groups):
   - off0: −251.69 nats; off1: −259.86 nats → **offset 0 favored by +8.17 nats.**
   - Unigram check: off0 −157.99 vs off1 −164.88 → offset 0 favored by +6.89.
   Same direction as bedrock's +6.49 LOO, slightly larger. Offset 1 does not
   beat the grade — it trails it by a ~14.7-nat swing.
4. **Banked-value density.** Off0 embeds 9/35 banked-valued groups
   (64=qui, 96=par, 00=pour, 79=tout, 37-frame, 11=la, 85-stem, 34=i, 29=er,
   40=e); off1 embeds 6/35 (96=par, 84=on, 29=er, 17=fois, 42-frame, 32-frame,
   46=que). Offset 1 is poorer in banked content, not richer.
5. **Novelty scan.** Both parses are hapax-rich at the bigram level (28/34
   bigrams under off1 and 25/34 under off0 have stream-wide count ≤1 outside
   the row) — a1_01 is an outlier row under either phase. Notable asymmetry:
   off0's novelties include the kill-grade `11 79` and `92 79 37` (92 x1 before
   79 elsewhere); off1's novelties are distributional-only, no
   banked-ungrammatical pair found.
6. **Row-end note (single-window, non-qualifying).** Off1 ends `...91 32 46` =
   `[91][32-predicative-frame]que`. A row ending in 46="que" is attested
   (a8_05, gloss-(ii)-confirmed; a8_07 under off 0). Recorded for completeness;
   per the bar it cannot carry the decision alone.

### No new kill-grade violation under offset 1 (constraint sweep)
- `84`="on" (promoted A15) at in-row idx 7, predecessor `48`: `48 84` occurs
  once elsewhere in the stream — not impossible, not clean.
- `96`="par" at in-row idx 2, follower `44`: stream-wide `96` followers are
  87/21/43/00/45/82; `96 44` is unattested (count 0). Suspicious but not
  kill-grade at battery level (96's follower set is small and unsystematic).
- No 67 (positional rule vacuous), no 48-value litigated (kills hold), no
  homophone-set claim made.

## Per-clause results

**Clause 1 (clash dissolves on the full row): PASS.** Offset 1 eliminates the
`11 79` "la tout" bigram entirely — verified by full-row scan, not one window.

**Clause 2 (beat +6.49 with independent evidence): FAIL.** Formula checks are
empty; crib-adjacent evidence is empty; the independent distributional
re-derivation favors offset 0 by +8.17 nats (bigram) / +6.89 (unigram),
confirming the bedrock grade rather than overturning it; banked-value density
favors offset 0 (9 vs 6 groups).

**Clause 3 (not a single-window rescue): FAIL.** The only evidence favoring
offset 1 is the clash dissolution itself. No independent full-row evidence was
found.

## Verdict: NULL

Offset 1 genuinely dissolves the 'la tout' clash (clause 1 holds), but the bar
demands it beat the +6.49 bedrock grade with independent evidence, and the
full-row battery finds none: the distributional margin confirms offset 0, and
no formula or crib evidence favors offset 1. This is **not a kill** of the
offset-1 hypothesis — the dissolution is real and the contradiction that
motivated it (s5 null) stands — but the bar as pre-registered is not met.

No standing verdict contradicted or downgraded. The bedrock ruling stands ("no
offset currently requires change" for a1_01); the s5 fence is untouched; the
red-team venue `redteam-la-tout-fence` remains the decision point for
banking-vs-segmentation.

## Follow-ups (null regenerates work)

1. `seg-a1_01-constraint-sweep` (P3): systematic check of all 35 offset-1 pairs
   against every granted/banked constraint (A15 C1–C3 on 84@in-row-7, 96=par
   follower set on `96 44`@2, predicative frames 42/32, 67 positional rule) to
   find a discriminating frame — does offset 1 introduce any NEW kill-grade
   violation, or is it constraint-clean across the full row?
2. `seg-a1_01-extrinsic-phase` (P3): extrinsic phase evidence — digit-count
   parity, row-boundary formulas with a1_00/a1_02, or manuscript/transcription
   facts that discriminate a1_01's phase from outside the statistical parse.
3. `seg-a1_01-hybrid-phase` (P3): test a transcription-error rival — the row is
   71 digits (odd) and hapax-rich under both phases; a single mid-row
   dropped/duplicated digit could explain BOTH the +8.2-nat distributional
   support for offset 0 AND the kill-grade 'la tout' clash. Bar: locate one
   candidate digit position where the hybrid parse removes the clash without
   degrading the bigram margin.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-seg-a1_01-offset1-test.md` (this file)
- Queue: `battery-queue.json` — target `seg-a1_01-offset1-test` → status
  `verdict`, result `null`, date 2026-10-08 (own entry only, temp-file +
  rename; no prior verdict existed, no downgrade)
- Lock `locks/seg-a1_01-offset1-test.lock` created on start with agent id + UTC
  timestamp, deleted on completion.
