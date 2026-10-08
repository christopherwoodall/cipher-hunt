# Red-team audit — Track D rung-C clean re-run (campaign integrity only)
Date: 2026-10-07 (UTC 2026-10-08). Auditor: Smith red-team auditor (session c960149b-0489-4e8f-bc5b-8771931a6628), independent of trial runner session d7b1c4f2-b47e-4593-b9a5-0f8acac3149b.
Scope: CAMPAIGN INTEGRITY of the mechanical result in `rerun-rungC-clean/`. No choice re-scoring, no instrument verdict declared here.

## VERDICT: ADMISSIBLE

All 9 mechanical checks pass on independently recomputed evidence. One substantive observation (check 10: judge-3 pass duplication) and one documentation gap (judge-commissioning provenance) are recorded below as concerns; neither changes any choice in the aggregation, so neither blocks admissibility. The trial's own verdict remains correctly NOT DECLARED pending this audit.

## Per-check results

### 1. Prompt pin — PASS
- `sha256sum ../../track-d/prompt-v3C.txt` → `d907c59202c9d38e5dfe10bf8048c869bcba2fb547631c02ceb34f93b5b2615e` (exact match to the pinned value in COORDINATOR-DESIGNATION.md).
- All 126 log records (42 × 3 files) carry exactly one distinct `prompt_sha256`, equal to that value.

### 2. Label blindness — PASS
- 84 distinct blind labels across all 3 logs; log label set == schedule+package label set == key label set (84/84/84, exact equality).
- Zero overlap against every prior key file, recomputed independently:
  - pilot `instrument-acceptance/_KEY_DO_NOT_OPEN.json` (18 labels): 0
  - v3A `instrument-acceptance-v3a/_KEY_V3A_DO_NOT_OPEN.json` (18): 0
  - v3B `instrument-acceptance-v3b/_KEY_V3B_DO_NOT_OPEN.json` (18): 0
  - voided v3C `instrument-acceptance-v3c/_KEY_V3C_DO_NOT_OPEN.json` (84): 0
- `void-v3c-labels-collected.json` label set == voided v3C key label set (confirms key-only extraction was faithful).
- No eternal IDs (`18[45]xxx`) and no class words (`truth|salad|paraphrase`) in any of the 3 packages, the schedules, or the 3 logs (independent grep, 0 hits each).

### 3. Temporal key ordering — PASS
- Key file mtime: 2026-10-08 01:44:33 UTC (sealed by build). Log mtimes: 01:49:19 / 01:49:36 / 01:49:52. Aggregation (which opens the key): 01:50:08.
- Log records carry no timestamp field; file mtime is used as proxy — key sealed ≥4.5 min before first log write.
- Key sha256 now (`3ef6e2e3…6e66`) == pre-open sha in INTEGRITY-MANIFEST.json: the key was never rewritten between sealing and opening.
- `score_and_aggregate.py`: completeness assert halts at line 117–118 (`len(records) != 126`), key is opened only at line ~148, after all verification gates. `key_opened_utc` recorded in aggregation-clean.json as 2026-10-08T01:50:08.020943+00:00, matching artifact mtime.

### 4. Position randomization — PASS
- For all 126 records: `label_x` == schedule `presented_first` for the record's (judge, pair, pass) — 0 mismatches; label pairs per record match the package's pair label set exactly.
- 7 spot-checks across judges/passes (P09-j1-p1, P19-j2-p1, P28-j3-p1, D01-j1-p2, D04-j2-p3, P25-j3-p3, plus one attempted on an unassigned pair) all match schedule order.
- Note: judges 1 and 2's justifications correctly re-anchor to X/Y after position swaps (evidence the randomized presentations were genuinely re-read — see check 10).

### 5. Disk-first — PASS
- Recomputed sha256 of the 3 logs independently:
  - `aa3d25fbc8…af`, `3f8b04788…a11`, `412a9251e…c5eb`
  - match INTEGRITY-MANIFEST.json AND handoff-checksums.json byte-for-byte.
- `score_and_aggregate.py` reads the disk logs and HALTS on any handoff↔disk mismatch (lines 38–53); scoring parses only disk lines.

### 6. Pair construction — PASS (verified via the opened key)
- 36 binding pairs: all {truth, salad} — 0 mismatches.
- 6 diagnostic pairs: all truth_i vs paraphrase_i with matching seeds, mapping verified across all 3 packages: D01=184101, D02=184102, D03=184103, D04=184104, D05=184105, D06=184106 (by-seed, per the R19 carry-forward — the voided run's cross-seed deviation was not repeated).

### 7. Tripwire — PASS
- `R5005|r5005|ct_r5005`: 0 hits in packages, schedules, or logs. The only hits in the directory are in docs/scripts (COORDINATOR-DESIGNATION.md, TRIAL-STATUS.md, MECHANICAL-SUMMARY.md, build/score scripts) as tripwire protocol language, not trial content.
- Gate-instance IDs (184201–184204, 184206, 184207): 0 hits in packages, schedules, logs, build.log, judge-brief.md.

### 8. Completeness — PASS
- 126 records / 126 unique `call_id`s, 0 duplicates, 42 per judge.
- Each judge covers exactly 14 pairs × 3 passes (binding 108 + diagnostic 18 = 126).
- Judge pair partition: j1 = D01–D02 + P01–P12; j2 = D03–D04 + P13–P24; j3 = D05–D06 + P25–P36.

### 9. Single-coordinator — PASS (with a documentation-gap note)
- File mtimes are monotonic and role-coherent: build artifacts 01:42–01:44 → judge-brief 01:45 → scoring pipeline 01:45:44 → judge logs 01:49:19–52 → handoff-checksums 01:50:07 → aggregation 01:50:08. No interleaved writes, no second-trial-writer signatures, no modifications to sealed build artifacts.
- NOTE (process anomaly, not integrity failure): TRIAL-STATUS.md (written 01:46 by runner session d7b1c4f2) states judge commissioning was BLOCKED at that session's depth. The judge logs exist at 01:49, so the three judges were commissioned after the status file was written — presumably by the coordinator/parent. **No artifact documents who commissioned the judges, when, or attests their lane-naivety/freshness.** The COORDINATOR-DESIGNATION.md designates a single coordinator, and there is no evidence of a second *trial* writer; but the commissioning provenance is unattested in the record. Recommend the coordinator attest it in writing before any verdict is declared.

### 10. Confidence uniformity (integrity assessment) — CONCERN RECORDED, does not threaten the choice data
Findings (recomputed from disk logs):
- Confidence is anchored per pair for all three judges (e.g., judge 1: P01–P06 all [78,78,78] across passes; judge 3: every pair [90,90,90]).
- Deeper: **judge 3's `raw_response` is byte-identical across all 3 passes for 14/14 pairs**, including passes where the schedule swapped X/Y presentation (e.g., P25 pass2 presented X=cf360844 vs pass1 X=5f78436d — response text identical). A genuine independent LLM call does not produce byte-identical output on position-swapped prompts 14 times; judge 3's passes 2–3 are almost certainly copies of a single judgment, not independent evaluations.
- By contrast judges 1 and 2 genuinely re-reason each pass: 0/14 pairs with identical raw_response; justifications re-anchor correctly to the swapped X/Y positions while choosing the same label. Their fixed per-pair confidence is benign anchoring to a repeated judgment.
- Does this threaten the CHOICE data? No, for three reasons:
  1. The rung-C criterion (PREREG-D-v3-ladder.md §3) is on choices: truth wins the per-pair majority on ≥35/36 binding pairs. Confidence is explicitly recorded but not gated.
  2. Judge 3's pass-1 judgments are position-plausible (label-referenced justifications, consistent with presentation) and unanimously agree with the genuinely independent votes; even under the strictest independence weighting (judges 1+2 at 3 passes each + judge 3 at 1 vote per pair = 7 independent votes), every binding pair is truth-unanimous.
  3. The duplication is transparent in the logs — it alters no choice, and the mechanical aggregation would be identical if judge 3's duplicate passes were removed.
- What it does degrade: the "3 position-randomized passes" design intent for judge 3 (no independent position-bias check). Recommendation: future campaigns should reject byte-identical pass responses or require per-pass fresh reasoning evidence.

## Concerns that should block a verdict (none on the mechanical result)
None. The mechanical result is ADMISSIBLE. Before any instrument verdict is declared, recommend:
1. Coordinator attests judge commissioning provenance (who/when, 3 fresh lane-naive judges).
2. TRIAL-STATUS.md's "BLOCKED" section is stale — append a dated addendum recording that commissioning proceeded.
3. Record judge 3's pass-duplication as a methodology note for future rungs (verbatim-response check in the scoring pipeline).
