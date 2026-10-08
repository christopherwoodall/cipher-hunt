# Track D — PREREG-D-v3: judge-prompt repair ladder (re-registration)

**Status:** pre-registration. Written 2026-10-07 by the TRACK D PROMPT-REPAIR agent (text-only; this agent judged nothing and read no candidate text — variants are built from the R13 failure analysis, not tuned on the 18). **Red team must review this ladder doc before any trial runs.**

## 0. Background and strike accounting

- R13 (2026-10-07): the instrument acceptance test FAILED. Fresh cold judges collapsed truth and salad both to ~25 (mT−mS = 0–5 vs the ≥30 bar, 3/18 within ±3 of pilot medians). Mechanism: cold judges cannot segment words out of spaceless ear-noised text, so they fall back on holistic "coherent prose?" — everything spaceless scores ~25. The pilot operator read *through* the degradation; cold instances report "no coherent French words or phrases." Anchors also drift: the frozen prompt's own "adversarially constructed" low-end anchor is read as a description of the stimulus, dragging degraded text into the ~25 bucket.
- R13 ordered a repair ladder and recorded **strike one** (first failed substrate attempt per PREREG-D-v2 §9(b)).
- This document re-registers the ladder. **If all three rungs below fail, strike two is recorded and the SPS trigger (PREREG-D-v2 §9(b), condition (b): "no viable judge instrument after two substrate attempts") is MET** — the structural fallback (deterministic SPS scorer per council arch §7) begins, and SPS itself re-registers as an instrument (frozen spec + acceptance test) before touching any gate instance. Nothing in the funnel proceeds without a passing instrument (R13 final).

## 1. The ladder: sequential A → B → C, stop at first pass

**Rung A — prompt-v3A.txt (degradation-robust instructions, first choice).** Replaces holistic fluency scoring with countable evidence: the judge must first LIST the identifiable French words/phrases (including spaceless and by-ear forms), then score from the count and quality of recovered French. Band anchors: 0–15 none / 20–35 fragments / 40–55 isolated words / 60–75 words + phrases (degraded but French) / 80–90 long stretches / 95–100 clean. Output envelope: line 1 = integer 0–100 (mechanical first-line parse unchanged), line 2 = comma-separated word list (or NONE), line 3 = one-sentence justification. Attacks the observed segmentation failure head-on: cold judges collapse spaceless text to noise because they never attempt segmentation; the mandatory listing forces the attempt.

**Rung B — prompt-v3B.txt (anchored calibration).** The frozen v2 prompt verbatim (untouched wording, scale, and output format) PLUS three synthetic scored exemplars prepended, explicitly labeled as calibration anchors (not test items): ~21 salad-class (spaceless repetitive noise, scattered fragments), ~61 degraded-truth-class (spaceless ear-noised French), ~91 clean French. Exemplars are synthetic — written from the pilot's observed bands, never drawn from `candidates.json` — so no tuning on the 18. Attacks the observed anchor drift: cold judges set their scale from surface features (spacing → 100) and misread the "adversarially constructed" anchor.

**Rung C — prompt-v3C.txt (pairwise forced-choice).** Two blind decodes, forced choice of which contains more French (ties forbidden), plus confidence 0–100. Output envelope: line 1 = winning label verbatim (mechanical parse on label equality), line 2 = integer confidence, line 3 = one-sentence justification. Pairing: all 36 truth-vs-salad pairs; each pair judged 3 times with X/Y position randomized per pass; the 36 pairs split 12+12+12 across the 3 fresh judges (108 calls total). Aggregation: per-pair outcome = majority of 3; Bradley-Terry win-modeling permitted as a diagnostic only. Sidesteps absolute calibration entirely — discrimination is the actual requirement.

## 2. Trial protocol (identical across rungs, binding)

Each rung gets exactly one trial campaign. Per R13, **pilot and acceptance populations coincide**: the fresh judges' campaign IS both the pilot and the acceptance test — the pass criterion is applied to its results. No operator pilot, ever again.

1. **Fresh blind judges only.** Three fresh, lane-naive LM instances per rung. Never the prompt-repair agent, never the pilot operator, never any instance that has seen `candidates.json` plaintexts or the R13 key.
2. **Frozen prompt, sha256-pinned.** The variant's sha256 is asserted at judge startup; abort on mismatch. The frozen `judge_prompt.txt` (v2), PREREG.md, PREREG-D-v2.md, and PREREG-D-v2-branchB.md are not modified by this program.
3. **New blind labels per rung.** Fresh 8-hex labels regenerated per rung; zero old-label hits in packages/logs (verified mechanically, as in R13(d)). Packages precede the key temporally; logs reference nothing key-like.
4. **Three passes.** Rungs A/B: the frozen 18 × 3 passes = 54 calls, 6+6+6 per judge, fresh random order per pass. Rung C: the 36-pair schedule × 3 position-randomized passes = 108 calls, 12 pairs per judge.
5. **Full logging.** Every call logged (label, pass, prompt sha256, full raw response, extracted score/choice). A v3 logger replaces `judge_driver.log_judgment`'s single-line-justification assertion — line 2 evidence payloads must be stored, not dropped.
6. **Red-team review before verdict.** Red team audits each rung's campaign integrity (sha256 assertions, label blindness, temporal key ordering, exemplar provenance for B, position randomization for C) before the pass/fail verdict is declared.
7. **Deterministic; no R5005 contact.** Standing constraints hold for all rungs.

## 3. Pass criteria (binding, per rung — red team: negotiate the numbers now, not after)

**Rungs A and B (absolute 0–100):** PASS iff **mT−mS ≥ 30 on 6/6 AND median(truth) ≥ 50.**

- *Why ≥30 on 6/6:* the binding bar from PREREG-D-v2 §5. R13 voided the instrument, not the bar — transferability is the acceptance test's entire purpose, so the discrimination bar is unchanged.
- *Why median(truth) ≥ 50 (new):* the R13 failure signature was truth collapsing INTO the salad band (25 vs 25). A margin-only criterion admits a degenerate pass — e.g. truth 30 / salad 0 gives margin 30 while the instrument still cannot read degraded French. The ≥50 floor requires the actual mechanism repair: cold judges reading *through* degradation. 50 sits halfway between the observed salad band (~25) and the pilot truth band (61–64): a passing instrument must land closer to the pilot's reading than to the collapse state.
- *Void-probe diagnostic (non-binding, kept for symmetry with the pilot):* median(paraphrase) must not be ≤ median(salad); if paraphrase collapses too, the scale is broken even if the margin passes.

**Rung C (pairwise):** PASS iff **truth wins the per-pair majority on ≥35 of the 36 truth-vs-salad pairs** (≤1 flipped pair allowed as noise margin). This is the pairwise analogue of the 6/6 discrimination bar — full truth>salad separation with no systematic inversions. Diagnostic (non-binding): 6 truth-vs-paraphrase bouts — paraphrase is expected to win (clean French contains more identifiable French; the memorization worry is moot under blind forced choice); confidence calibration is recorded but not gated.

## 4. Sequence and strike resolution

- Run rung A. If PASS → strike one is cleared, the instrument is accepted, and step-4 clearance is re-requested on the accepted instrument. Stop.
- If rung A FAILS → run rung B (fresh judges, new labels, same criteria). If PASS → accepted, stop.
- If rung B FAILS → run rung C. If PASS → accepted, stop.
- **If all three rungs FAIL → strike two is recorded → the SPS fallback trigger is MET.** SPS (deterministic by-ear-normalize → DP word segmentation → UD dependency parse scorer) is constructed per council arch §7 and re-registers as an instrument before any gate-instance contact.
- Skipping a rung is forbidden; re-ordering is forbidden. Each rung's failure must be diagnosed in a rung report (judge justifications in their own words, as R13 did) before the next rung runs — the diagnosis informs whether the next variant is even plausibly different.

---
*Frozen assets untouched by this program: `judge_prompt.txt`, `PREREG.md`, `PREREG-D-v2.md`, `PREREG-D-v2-branchB.md`, the 18 frozen candidates, the sealed gate instances (184201–184204, 184206, 184207).*
