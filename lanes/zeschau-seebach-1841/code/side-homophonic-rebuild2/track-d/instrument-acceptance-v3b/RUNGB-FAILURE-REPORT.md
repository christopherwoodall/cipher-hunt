# Rung B failure report (PREREG-D-v3 ladder, per protocol)

Rung B (prompt-v3B.txt, sha256 `92d2f3e6fa87f2ba6910824d05019f3bb542373e86ddeaab5eaca5a52bb7a1b1`:
frozen v2 prompt verbatim + three synthetic scored calibration exemplars ~21/~61/~91)
trial campaign complete 2026-10-07. 3 fresh blind judges × 18 calls (6 blind labels × 3 passes,
fresh random order per pass), 54 records, red-team campaign-integrity audit 7/7 PASS
(prompt pin on all 54 records, label blindness vs all 36 old labels, temporal key ordering,
schedule adherence, exemplar provenance synthetic, seal integrity, mechanical parse audit).
Key opened only after all 54 calls logged. R5005 and sealed gate instances
(184201–184204, 184206, 184207) never contacted (tripwire before/after: clean).

## Verdict: FAIL (against pre-registered criteria)

Binding bar (ladder §3 + task-carried stability bar): mT−mS ≥ 30 on 6/6 AND median(truth) ≥ 50
AND cross-pass range ≤ 2 on all 18 candidates.

| seed | truth median (3 passes) | salad median (3 passes) | margin | bar (≥30) |
|------|----------------------|----------------------|--------|-----------|
| 184101 | 55 [55,55,55] | 21 [21,21,21] | 34 | PASS |
| 184102 | 32 [32,32,32] | 24 [24,24,24] | 8 | FAIL |
| 184103 | 19 [19,19,19] | 20 [20,20,20] | −1 | FAIL (inversion) |
| 184104 | 20 [20,20,20] | 21 [21,21,21] | −1 | FAIL (inversion) |
| 184105 | 46 [46,46,46] | 16 [16,16,16] | 30 | PASS |
| 184106 | 18 [18,18,18] | 21 [21,21,21] | −3 | FAIL (inversion) |

- mT−mS ≥ 30 on 6/6: **FAIL — 2/6 seeds meet the bar** (observed margins −3…34).
- median(truth) ≥ 50: **FAIL — 26.0** (all 18 truth records: 18×3, 19×3, 20×3, 32×3, 46×3, 55×3).
- Cross-pass range ≤ 2 on all 18: **PASS — 18/18, every candidate range 0** (perfect self-consistency).
- Void-probe diagnostic (non-binding): median(paraphrase) = 92 vs median(salad) = 21 → scale intact.
- ±3 pilot-median reproduction (informational): truth 26 vs pilot 62 — NO; salad 21 vs pilot 20.5 — YES;
  paraphrase 92 vs pilot 91 — YES.
- Three truth<salad inversions (184103, 184104, 184106).

## Diagnosis (in the judges' own words)

The rung-B mechanism **fired at the wrong level**. The calibration anchors pinned the
endpoints exactly as designed — salad landed at ~21 (median 21.0) and paraphrase at 91–97
(median 92) for ALL three judges, with cross-pass range 0 on every candidate. The scale is
obeyed. But the frozen v2 prompt is holistic "reads as natural, fluent French prose" scoring,
and v3B dropped v3A's word-listing mechanism repair — so cold judges fell back on the R13
failure mode for degraded truth: "does it look like prose?" Spaceless ear-noised French does
not look like prose, so truth collapsed into the salad bucket (18–32 on 4/6 seeds).

The anchors taught the scale, not the skill. Segmentation remained per-judge variance:
- Judge 3 segmented and read through degradation — 184101-truth 55: "Substantially degraded
  spaceless text in which real French words like Capitre, premiere, une, visite, and livre
  remain identifiable throughout." 184105-truth 46: "Roughly half of this spaceless text
  resolves into real French words like je, sur, le, vu, dire, and ne pas while the rest is
  garbled." 184102-truth 32: "Heavily garbled spaceless text with scattered recognizable
  French words like visite, premier, lune, pour, and une embedded in mostly non-French noise."
- Judge 1 could not segment — all three of its truths scored 18–20: "Dense noise with
  scattered French-like fragments ('parler', 'la vie', 'parce', 'utilite') but no coherent
  phrases." / "Dense repetitive noise with scattered French fragments ('le', 'premiere',
  'parce', 'parle') but no reconstructible phrases." / "Dense garbled noise with scattered
  French fragments ('pur', 'premier', 'la vie', 'parce') but no coherent phrases."
- Note judge 1 listed real words ("parler, la vie, parce, utilite") and still scored 18:
  the words were legible but the holistic frame ("no coherent phrases") overruled them.

Net: **anchor compression is NOT resolved** — it changed shape. Rung A repaired the mechanism
(segmentation via word-listing) but compressed the scale (bands 40–55/60–75); rung B repaired
the scale (anchors 21/61/91) but abandoned the mechanism (holistic v2 scoring). Neither rung
did both. The one clean signal: cross-pass stability 18/18 — the anchors produced perfect
self-consistency; the failure is inter-judge mechanism variance, not scoring noise.

## Ladder consequence (per §4)

Strike count: R13 strike one stands; rung-A and rung-B FAILs add no strike (§4: strikes only
after all three rungs fail). **Proceed to rung C** (prompt-v3C.txt: pairwise forced-choice,
36 truth-vs-salad pairs × 3 position-randomized passes = 108 calls, 12 pairs per judge,
majority-of-3 per pair, PASS iff truth wins ≥35/36). Rung C is plausibly different per the
§4 requirement: it sidesteps absolute calibration entirely — the judges' own prose already
contains the discriminative signal (judge 3's "real French words remain identifiable
throughout" vs judge 1's "no coherent phrases"), and forced choice asks them to APPLY that
discrimination rather than map it onto an absolute scale. The absolute-scale mechanism is
what both failed rungs show to be unfixable: any absolute anchor scheme pins endpoints but
cannot standardize per-judge segmentation. If rung C FAILS → strike two is recorded → the
SPS fallback trigger is MET (PREREG-D-v3-ladder §0/§4).

## Campaign artifacts

- Re-registration: `instrument-acceptance-v3b/RUNGB-REREGISTRATION.md` (prompt delta, mechanism
  argument, acceptance criteria, audit-resolution note, integrity facts)
- Logs: `instrument-acceptance-v3b/judge-log-rungB-agent{1,2,3}.jsonl` (18 records each, fields
  per re-registration note)
- Packages: `instrument-acceptance-v3b/rungB-pkg-{1,2,3}.json`; schedules:
  `instrument-acceptance-v3b/rungB-schedules.json`
- Key: `instrument-acceptance-v3b/_KEY_V3B_DO_NOT_OPEN.json` (new→old labels; opened only
  after all 54 calls logged)
- Red-team audit: delivered to coordinator 2026-10-07 (7/7 PASS, no voiding findings)
