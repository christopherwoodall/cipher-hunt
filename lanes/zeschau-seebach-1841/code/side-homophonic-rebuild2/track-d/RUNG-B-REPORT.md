# Track D — Rung-B trial report (prompt-v3B, anchored calibration)

> **EVIDENCE STATUS: WITHDRAWN — see INCIDENT-RUNGB-20261007.md.** The per-seed table below is
> inconsistent with the current disk logs; the judges' handoff summaries are inconsistent with the
> disk logs; unauthorized files were written to the trial directory. The verdict DIRECTION (FAIL)
> is robust across all data versions (3/6 and 2/6 — neither approaches the bar), but no numbers
> in this report are certified. Red-team ruling pending on VOID-vs-FAIL for strike accounting.

**Status:** trial complete; campaign-integrity audit R17 returned INTEGRITY FAIL (check 7: score arithmetic).
**Date:** 2026-10-07. Prompt sha256 `92d2f3e6fa87f2ba6910824d05019f3bb542373e86ddeaab5eaca5a52bb7a1b1` asserted PASS on all 54 log records (mechanically re-verified by coordinator, including extracted_score == int(line 1) on all 54).

## Result: RUNG B FAILS — 3/6 seeds pass; 184103 INVERTS (truth < salad)

Per-seed margins (mT−mS, medians of 3 passes):

| seed | mT | mS | margin | bar (≥30) | truth judged by |
|------|----|----|--------|-----------|-----------------|
| 184101 | 52 | 18 | 34 | PASS | judge 3 |
| 184102 | 55 | 21 | 34 | PASS | judge 3 |
| 184103 | 19 | 22 | −3 | FAIL (inversion) | judge 1 |
| 184104 | 20 | 17 | 3 | FAIL | judge 1 |
| 184105 | 58 | 16 | 42 | PASS | judge 3 |
| 184106 | 18 | 17 | 1 | FAIL | judge 1 |

- Overall median(truth) = 35 < 50 → **the floor clause FAILS too.**
- The salad band DID move down as designed: salad medians 16–22 (vs 35–62 in rung A). The ~21 anchor worked for salad.
- No nulls, no retries; all three judges protocol-compliant.

Verdict once audited: **RUNG B FAILS (3/6, with inversion)**. Proceed to rung C per the ladder sequence.

## Diagnosis (why the anchors backfired)

The anchors did not calibrate judges to a common scale — they made truth placement **bimodal across judges**:

- **Judge 3** (truths 184101/184102/184105) placed truth at 52–60 — the degraded-truth anchor band (B ≈ 61). Margins 34–42. The intended behavior.
- **Judge 1** (truths 184103/184104/184106) placed truth at 18–22 — the *salad* anchor band (A ≈ 21). Margins −3 to 3. The anchors actively dragged degraded truth DOWN.

The synthetic ~61 "degraded truth" exemplar did not transfer: whatever surface features it carried, cold judges
pattern-matched real spaceless ear-noised truth to the ~21 "spaceless repetitive noise, scattered fragments" exemplar
instead. The two anchor classes are not separable by the stimulus features judges actually use — both exemplars are
"spaceless degraded French-ish text," and which one a judge reaches for is judge-dependent, not stimulus-dependent.
Judge 2's package contained no truth candidates (3 paraphrase + 3 salad: paraphrases 93–95, salads 16–19 — clean
separation, but no truth signal).

So rung B replaced rung A's reliable compression (truth 62–68 vs salad 35–62, always truth > salad) with an
unreliable scale: direction of error now varies by judge, including a full inversion. The absolute-score approach is
the problem — not the anchor values. Any fixed numeric scale requires judges to place "degraded truth" and "clever
salad" in absolute bands, and the evidence of two rungs is that cold judges cannot do this stably: v3A compressed
the margin, v3B randomized the placement.

## Why rung C is still plausibly different (ladder §4 requirement)

Rung C (prompt-v3C, pairwise forced-choice) sidesteps absolute calibration entirely — the failure point of both
rungs. The judge never assigns "how French" a number; it picks which of two passages contains MORE French, ties
forbidden. Concretely:

1. **No bands to place.** The bimodality that killed rung B (anchor-A vs anchor-B placement) has no expression in a
   forced choice. Both candidates can be "degraded" — the judge only reports the direction of the difference.
2. **The prose signal is comparative.** In their justifications, judges already report the discriminative feature
   comparatively: truth has "words and short phrases such as la premiere, parce, and sa vie" / "la partie de la vie"
   while salad has "isolated tokens... dominated by the repeated word leurs" with "no reconstructible phrases."
   Forced choice asks exactly this question.
3. **Inversions become measurable noise, not scale artifacts.** 36 cross-seed truth-vs-salad pairs × 3
   position-randomized passes, majority aggregation; the bar (≥35/36) tolerates ≤1 flipped pair.

Risk carried forward: if judges cannot tell the difference at all, pairs go to chance (confidence ~50, ~18/36) —
which is itself the honest measurement the ladder wants.

## Campaign artifacts

- Logs: `instrument-acceptance-v3b/judge-log-rungB-agent{1,2,3}.jsonl` (18 records each, v3b-logger-pin.md schema)
- Key: `instrument-acceptance-v3b/_KEY_V3B_DO_NOT_OPEN.json` (opened only for scoring, after all logs complete)
- Note: the rung-B package builder's report table listed stale labels from its crashed first run; the on-disk
  artifacts were independently re-verified by the coordinator (18 fresh labels, zero collision vs 54 historical,
  key↔label_map exact cover, all 18 texts byte-identical to candidates.json). Red-team: audit the disk files,
  not the builder's table.
