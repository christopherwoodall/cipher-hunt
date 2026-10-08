# rung-C clean re-run — mechanical summary (no verdict)
generated_utc: 2026-10-08T01:50:08.038615+00:00
prompt_sha256: d907c59202c9d38e5dfe10bf8048c869bcba2fb547631c02ceb34f93b5b2615e

## Completeness
- calls parsed: 126/126 (binding 108/108, diagnostic 18/18)

## Binding pairs (truth vs salad)
- truth majority-wins: 36/36

## Per-pair table (pair_id: bout, votes, majority class, confidences)
- D01: diagnostic, votes={'paraphrase': 3}, majority=paraphrase, conf=[99, 99, 99]
- D02: diagnostic, votes={'paraphrase': 3}, majority=paraphrase, conf=[98, 98, 98]
- D03: diagnostic, votes={'paraphrase': 3}, majority=paraphrase, conf=[95, 95, 95]
- D04: diagnostic, votes={'paraphrase': 3}, majority=paraphrase, conf=[95, 95, 95]
- D05: diagnostic, votes={'paraphrase': 3}, majority=paraphrase, conf=[95, 95, 95]
- D06: diagnostic, votes={'paraphrase': 3}, majority=paraphrase, conf=[95, 95, 95]
- P01: binding, votes={'truth': 3}, majority=truth, conf=[78, 78, 78]
- P02: binding, votes={'truth': 3}, majority=truth, conf=[78, 78, 78]
- P03: binding, votes={'truth': 3}, majority=truth, conf=[78, 78, 78]
- P04: binding, votes={'truth': 3}, majority=truth, conf=[78, 78, 78]
- P05: binding, votes={'truth': 3}, majority=truth, conf=[78, 78, 78]
- P06: binding, votes={'truth': 3}, majority=truth, conf=[78, 78, 78]
- P07: binding, votes={'truth': 3}, majority=truth, conf=[72, 72, 72]
- P08: binding, votes={'truth': 3}, majority=truth, conf=[75, 75, 75]
- P09: binding, votes={'truth': 3}, majority=truth, conf=[70, 70, 70]
- P10: binding, votes={'truth': 3}, majority=truth, conf=[75, 75, 75]
- P11: binding, votes={'truth': 3}, majority=truth, conf=[72, 72, 72]
- P12: binding, votes={'truth': 3}, majority=truth, conf=[75, 75, 75]
- P13: binding, votes={'truth': 3}, majority=truth, conf=[90, 88, 89]
- P14: binding, votes={'truth': 3}, majority=truth, conf=[90, 88, 89]
- P15: binding, votes={'truth': 3}, majority=truth, conf=[90, 88, 89]
- P16: binding, votes={'truth': 3}, majority=truth, conf=[90, 88, 89]
- P17: binding, votes={'truth': 3}, majority=truth, conf=[90, 88, 89]
- P18: binding, votes={'truth': 3}, majority=truth, conf=[90, 88, 89]
- P19: binding, votes={'truth': 3}, majority=truth, conf=[85, 88, 89]
- P20: binding, votes={'truth': 3}, majority=truth, conf=[85, 88, 89]
- P21: binding, votes={'truth': 3}, majority=truth, conf=[90, 88, 89]
- P22: binding, votes={'truth': 3}, majority=truth, conf=[90, 88, 89]
- P23: binding, votes={'truth': 3}, majority=truth, conf=[90, 88, 89]
- P24: binding, votes={'truth': 3}, majority=truth, conf=[90, 88, 89]
- P25: binding, votes={'truth': 3}, majority=truth, conf=[90, 90, 90]
- P26: binding, votes={'truth': 3}, majority=truth, conf=[90, 90, 90]
- P27: binding, votes={'truth': 3}, majority=truth, conf=[90, 90, 90]
- P28: binding, votes={'truth': 3}, majority=truth, conf=[90, 90, 90]
- P29: binding, votes={'truth': 3}, majority=truth, conf=[90, 90, 90]
- P30: binding, votes={'truth': 3}, majority=truth, conf=[90, 90, 90]
- P31: binding, votes={'truth': 3}, majority=truth, conf=[90, 90, 90]
- P32: binding, votes={'truth': 3}, majority=truth, conf=[90, 90, 90]
- P33: binding, votes={'truth': 3}, majority=truth, conf=[90, 90, 90]
- P34: binding, votes={'truth': 3}, majority=truth, conf=[90, 90, 90]
- P35: binding, votes={'truth': 3}, majority=truth, conf=[90, 90, 90]
- P36: binding, votes={'truth': 3}, majority=truth, conf=[90, 90, 90]

## Diagnostic bouts (truth vs paraphrase, by seed)
- D01 (seed 184101): majority=paraphrase, votes={'paraphrase': 3}
- D02 (seed 184102): majority=paraphrase, votes={'paraphrase': 3}
- D03 (seed 184103): majority=paraphrase, votes={'paraphrase': 3}
- D04 (seed 184104): majority=paraphrase, votes={'paraphrase': 3}
- D05 (seed 184105): majority=paraphrase, votes={'paraphrase': 3}
- D06 (seed 184106): majority=paraphrase, votes={'paraphrase': 3}

## Confidence distribution
- min=70 max=99 median=90 mean=86.4
- below_50=0 50-59=0 60-79=36 80-100=90

## Integrity checks
- handoff<->disk cross-check: OK (3/3)
- tripwire (R5005/gate IDs): CLEAR pre-judge and post-judge
- label blindness: OK (84 fresh labels, zero old-label hits, no eternal IDs)
- class-word scan of logs: []
- key opened: 2026-10-08T01:50:08.020943+00:00 (pre-open sha 3ef6e2e35b4ef1f5...)
- verdict: NOT DECLARED (red-team audit pending)
