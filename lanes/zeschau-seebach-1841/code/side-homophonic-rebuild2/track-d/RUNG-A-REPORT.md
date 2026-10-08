# Track D — Rung-A trial report (prompt-v3A, degradation-robust word-listing)

**Status:** trial complete, awaiting red-team campaign-integrity audit before formal verdict declaration (PREREG-D-v3-ladder §2.6).
**Date:** 2026-10-07. Prompt sha256 `84393ae4c5f702f218841636871715e84f790be524d3e380bf4fb283f1fcd85e` asserted PASS on all 54 log records.

## Result: RUNG A FAILS — 0/6 seeds pass the ≥30 margin bar

Per-seed margins (mT−mS, medians of 3 passes; each (seed, class) cell judged by exactly one fresh blind judge):

| seed | mT | mS | margin | bar (≥30) |
|------|----|----|--------|-----------|
| 184101 | 65 | 45 | 20 | FAIL |
| 184102 | 62 | 45 | 17 | FAIL |
| 184103 | 68 | 44 | 24 | FAIL |
| 184104 | 65 | 45 | 20 | FAIL |
| 184105 | 65 | 51 | 14 | FAIL |
| 184106 | 68 | 45 | 23 | FAIL |

- Overall median(truth) = 65 ≥ 50 → **the second pass clause PASSES.**
- Void-probe (non-binding): median(paraphrase) = 98 vs median(salad) = 45 → scale intact, no collapse.
- No truth<salad inversions on any seed; all 6 margins positive.

*Correction (R16): an earlier version of this table reported 1/6 (184106 margin 33). The red-team arithmetic audit
recomputed from the logs; the coordinator's independent recompute confirms the audit exactly. The table above is the
corrected version. Verdict direction unchanged.*

Verdict once re-audited: **RUNG A FAILS (0/6)**. Strike one stands; rung B sequenced per the ladder.

## Diagnosis (why the margin fails — judges' own words)

The v3A mechanism repair **worked at the level it targeted**: cold judges now read through degradation.
Median(truth) = 65 (vs 25/25 collapse in R13); truth word-lists are rich — judge-1 on 184106-truth:
"sure, cela, parle, vie, dire, deuil, parce, eau, **la premiere**, ceci, une, pur, utilite, **sa vie**"; justification:
"Many French words and short degraded fragments such as la premiere, parce, and sa vie are recoverable even though
full sentences cannot be reconstructed." Judge-2 on 184101-truth recovered "chapitre, Myriel, ... **la partie de la vie**".

The failure is one level up: **the absolute 0–100 score maps "how much French did you recover" to a count/quality
aggregate, and the adversarial salad is built out of exactly countable French morphemes.** The salad earns partial
credit for the same feature the repair forces the judge to count:

- Judge-1 on 184104-salad (44): "A handful of distinct French words are recoverable (dominated by the repeated word
**leurs**), but they appear only as isolated tokens" — words listed: "leurs, la, premier, etre, metre, la premiere".
- Judge-1 on 184105-salad (52): "More distinct French words than the pure-noise candidates, including notre, forme,
and forte, but still only isolated words."
- Judge-2 on 184101-salad (45, margin 20): "quelque, première, comme, être, mettre, de la, me, leurs, l'âme" —
salad at 44–51 across seeds sits just below truth's 62–68 band, compressing every margin to 14–24.

So the v3A band anchors (40–55 = "isolated words", 60–75 = "words + phrases, degraded") are the wrong cut for an
adversary that tiles real words. Truth lands at 62–68; salad lands at 44–51. The discriminative signal the judges
*report in prose* (phrases vs repeated isolated tokens — "la partie de la vie" vs "dominated by the repeated word
leurs") is compressed out of the numeric score. This is the same Goodhart structure as the 5-gram failure, one level
up the abstraction stack: any score that credits *recoverable French fragments* rewards the salad for being built of
fragments.

## Why rung B is still plausibly different (ladder §4 requirement)

Rung B (prompt-v3B) does not add more evidence — it attacks the **scale mapping**, which is the identified failure
point: frozen v2 wording + three synthetic anchors explicitly pinning salad-class ≈ 21 ("spaceless repetitive noise,
scattered fragments"), degraded-truth-class ≈ 61, clean ≈ 91. The v3A failure is judges placing "isolated words"
salads at 43–52; v3B's anchors name that exact stimulus class and anchor it ~25 points lower. If judges obey the
anchors, margins move from 6–28 toward 30–40. Plausibly different; run it.

## Campaign artifacts

- Logs: `instrument-acceptance-v3a/judge-log-rungA-agent{1,2,3}.jsonl` (18 records each, fields per v3-logger-pin.md)
- Seeds sidecar: `instrument-acceptance-v3a/rungA-agent3-seeds.json` (judges 1–2 logged presentation order inline)
- Key: `instrument-acceptance-v3a/_KEY_V3A_DO_NOT_OPEN.json` (new→old labels; opened only for scoring, after all logs complete)
- Scoring: per-seed medians computed independently (no track imports beyond the key); class mapping via `label_map.json`
