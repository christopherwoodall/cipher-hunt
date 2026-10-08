# Prior interrupted session residue — quarantined

On 2026-10-07 the rung-C trial coordinator found these files in
`instrument-acceptance-v3c/` from a prior interrupted session:
- `gen_prompts.py`, `log_pass.py` (scratch harness scripts)
- `judge-log-rungC-agent1.jsonl` (2 records), `judge-log-rungC-agent3.jsonl`
  (3 records) — partial campaign, pair IDs `TP-s1`, `TP-s6`, `TS-t4-s2`,
  `TS-t2-s3`, `TS-t5-s3` (a foreign pairing scheme, not the registered
  P01–P36 / D01–D06 scheme)

**Decision: quarantined, excluded from the registered campaign.** Rationale:
(1) 5 records of an incomplete, non-registered design cannot form a trial;
(2) zero label collisions with the registered fresh 84-label set (verified
mechanically), so no blindness risk; (3) the registered campaign uses a
different pair scheme and fresh judges. These records are NOT counted toward
the 126-call budget and are never opened against the v3C key.

Kept here for provenance, not for analysis.
