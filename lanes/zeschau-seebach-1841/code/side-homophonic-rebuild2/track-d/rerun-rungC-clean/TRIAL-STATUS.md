# Rung-C clean re-run — trial-runner status
Date: 2026-10-07 (UTC 2026-10-08). Trial runner session: d7b1c4f2-b47e-4593-b9a5-0f8acac3149b.

## Done (build phase, all mechanical)

1. Prompt pin verified: prompt-v3C.txt sha256 = d907c59202c9d38e5dfe10bf8048c869bcba2fb547631c02ceb34f93b5b2615e.
2. Candidates: 18 eternal IDs classed via pilot-key expected_median exactly as
   build_rungC.py (<=30 salad, <=75 truth, else paraphrase); 6/6/6. Cross-checked
   against label_map.json class+seed for all 18.
3. Blind labels: 84 fresh 8-hex, zero overlap with all 138 previously used
   (pilot 18 + v3A 18 + v3B 18 + voided-v3C 84). Void-v3C labels collected by
   key-only extraction (dict keys) from the quarantined v3c key file per the
   parent task spec; values never inspected; quarantined logs/packages unread.
4. Pairs: 36 binding truth-vs-salad (all 6x6, P01-P36) + 6 diagnostic
   truth_i-vs-paraphrase_i paired BY SEED (D01=184101 ... D06=184106).
   Assignment: 12 binding + 2 diagnostic per judge.
5. Schedules: 3 passes/pair, per-pass order + X/Y position randomized with fresh
   RNG (seed 20261008, logged in build.log); each label presented-first >=1 time
   per pair (asserted).
6. Key sealed: _KEY_V3C_CLEAN_DO_NOT_OPEN.json (label -> eternal_id, class, seed).
7. Tripwire PRE-judge: zero hits for R5005/r5005/ct_r5005 and gate IDs
   184201-184204, 184206, 184207 across all 3 packages + schedules.
8. Package-text integrity: every packaged text sha256 matches candidates.json.
9. Judge briefs written (judge-brief.md): hash-verify prompt at absolute path at
   startup, abort on mismatch; forbidden files incl. KEY; disk-first JSONL logs
   at judge-log-clean-agent{N}.jsonl; handoff = transport only (42-call
   confirmation + log sha256, no scores).
10. Scoring pipeline written and tested end-to-end on synthetic logs
    (score_and_aggregate.py): checksum-at-receipt, handoff<->disk cross-check,
    tripwire post-judge, mechanical parse (line1 label equality, line2 int),
    schedule<->log consistency, 126/126 completeness, label-blindness,
    key opened only after verification, mechanical aggregation JSON + summary,
    no verdict language. Test run exited 0 with all checks green.

## BLOCKED: judge commissioning

This session runs at depth 2/2 with can_spawn=no and is instructed to work
alone without spawning subagents. It therefore CANNOT commission the 3 fresh
lane-naive judge subagents, and it must NOT serve as a judge itself (it has
seen candidates.json, the key build, and the class mapping — hopelessly
contaminated for blind judging).

Required next step (parent/coordinator action): commission 3 fresh subagents
using judge-brief.md (fill in judge number N=1/2/3), each lane-naive and never
exposed to candidates.json or this lane. Each judge writes 42 JSONL lines to
its own judge-log-clean-agent{N}.jsonl and reports back only the log sha256.
Then: run score_and_aggregate.py from rerun-rungC-clean/ with a
handoff-checksums.json file mapping "1"/"2"/"3" to the judges' reported log
sha256 values.

## Anomalies encountered

None in the build phase. All build asserts passed; tripwire clear; no hardening
check has been failed. (Key-open and scoring steps not yet run — pending judges.)

## Verdict

NOT DECLARED (red-team audit pending, per design).
