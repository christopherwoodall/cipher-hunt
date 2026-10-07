# SEGMENTER control — results (code/crowd4/control.py, control_results.json)

Pre-registered spec: code/crowd4/segmenter_control.md (written before the run).

## Build
- Synthetic cipher from Tocqueville t1 words 50000–51100 (1,100-word slice),
  syllabified with crowd/anneal.py `syllabify_word` (R1 maximal-onset).
- 96 most frequent slice syllables → 2-digit-style code inventory; words with
  out-of-top-96 syllables dropped → **621 words, 900 groups, 271 codes**.
- Rotation: within-word track cycle A→C→B→A; word boundary breaks rotation
  (jump to R variant) with q_break=0.70; spurious mid-word break q_mid=0.04.
- Ear-cutting noise: p_merge=0.08, p_split=0.04, p_alt=0.06.
- Era word-length prior rebuilt from corpus MINUS the control slice
  (220,106 words, era_mean 1.750). RNG seed 20261007.
- Control phase map = synthetic track labels (KNOWN GAP: does not re-test the
  contactor's unsupervised k=12 clustering that produced the R5005 phases).

## Verdict: PASS
| metric | value | threshold |
|---|---|---|
| M1 boundary recall @conf≥0.5 | 0.721 (447/620) | ≥ 0.60 |
| M2 internal positions conf<0.5 | 0.939 (262/279) | ≥ 0.70 |
| M3 mean(boundary)−mean(internal) | 0.258 (0.526 vs 0.268) | ≥ 0.10 |

## Sanity side-note (not pass/fail)
Control fitted s-values: boundary-favoring C->A +12.49, A->A +12.49, R->C
+11.87; within-favoring C->B −2.35, A->C −1.72. Real R5005 STRUCT s-values:
R->C +12.62, B->B +12.53, R->B +4.12. Same order of magnitude (~11–13 for the
top boundary legs) — the control is not trivially easy, and the EM recovered
the true cycle structure (cycle-following edges A->C, C->B, B->A correctly
within-favoring).

Gate outcome: control PASSED → drag of the 25 targets is authorized per the
pre-registered protocol.
