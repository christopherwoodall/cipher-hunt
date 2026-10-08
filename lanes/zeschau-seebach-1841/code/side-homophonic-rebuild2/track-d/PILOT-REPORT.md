# Track D — PILOT REPORT (2026-10-07)

## Protocol compliance
- 54 judge calls logged to `judge_log.jsonl` (18 candidates × 3 passes, zero duplicates/missing).
- Prompt sha256 `390a1ec0bf1aa9e0e495a5fe98e65107c41025c954cd11b68d1931816c08e21d` in every log entry = frozen `judge_prompt.txt` (matches PREREG).
- Self-operator judge mode (no local LLM). Mechanical first-line-int extraction; no re-querying/steering. R7a: class blindness did not hold (formats class-identifiable); log auditability is the control — full text, scores, justifications retained.
- All 54 scores are integers in [19, 93]. Per-candidate cross-pass range ≤ 2 points (judge stable).

## Per-query table (medians of 3 passes)

| seed | truth (label, scores, median) | salad (label, scores, median) | paraphrase (label, scores, median) |
|---|---|---|---|
| 184101 | 1386766b [63, 64, 64] → **64** | d38a1821 [21, 21, 22] → **21** | fed88338 [90, 90, 91] → **90** |
| 184102 | c0733a7d [60, 61, 62] → **61** | 19f3bb19 [20, 20, 21] → **20** | ecf4db34 [90, 90, 91] → **90** |
| 184103 | fe847630 [61, 61, 62] → **61** | d24f0ea5 [22, 22, 23] → **22** | d666c7df [91, 91, 92] → **91** |
| 184104 | 2a87b7a9 [62, 63, 63] → **63** | a1cd2087 [20, 20, 21] → **20** | 7e5bbba0 [90, 91, 91] → **91** |
| 184105 | b1eee668 [61, 62, 62] → **62** | 1c2498b4 [21, 21, 21] → **21** | 5888ca6b [92, 92, 93] → **92** |
| 184106 | 99a93f79 [62, 62, 63] → **62** | fc12e892 [19, 20, 20] → **20** | 264710b9 [92, 92, 93] → **92** |

*Table corrected 2026-10-07 per red-team R8a: the original per-query table
scrambled the label↔seed assignment on 9/18 rows (labels+scores were correct;
only the row placement was wrong). This table is rebuilt mechanically from
`label_map.json` (authoritative) + `judge_log.jsonl`; all medians, margins
(43, 41, 39, 43, 41, 42) and void values (−26, −29, −30, −28, −30, −30)
are unchanged.*

Overall class medians: truth **62**, salad **20.5**, paraphrase **91**.

## Verdict

| check | result |
|---|---|
| PILOT BAR: median(truth)−median(salad) ≥ 15 on 6/6 | **PASS 6/6** — margins: 43, 41, 39, 43, 41, 42 (all ≥ 39) |
| VOID probe: median(truth)−median(paraphrase) ≥ 15 anywhere | **CLEAN** — actual values −26, −29, −30, −28, −30, −30 (paraphrase OUTSCORES truth by ~29) |
| ANOMALY: median(paraphrase) ≤ median(salad) anywhere | no — probe informative |

**PILOT PASS, clean memorization probe.** The LM-judge (self-operator) separates planted truth from salad-class decodes by ~40 points where the 5-gram objective failed by 2,601 nats in the wrong direction.

Note on the probe direction: paraphrase > truth by ~29 points. If memorization of Les Mis were driving the judge's preference, truth should match or exceed paraphrase. Instead the judge scores pure surface fluency and penalizes the truth's spaceless degraded surface. The void rule's ≥15-pt threshold is nowhere near tripped; any residual recognition boost (R7b caveat) is bounded well below what would matter for the truth>salad separation (39–43 pts).

## Standing caveats
- Salad sources for 184105/184106 substituted `run3-18410{5,6}` for the empty `frozen-ctl-18410{5,6}` dirs (documented in build provenance; same frozen instrument, verified degenerate-class). Red team to rule at post-pilot.
- Steps 4/5 (gate anneal + 360 calls) NOT run — require explicit step-4 clearance ruling per R7. This report requests that clearance.
- Fresh gate instances (184201–184204, 184206, 184207) remain sealed; never read by this track.
