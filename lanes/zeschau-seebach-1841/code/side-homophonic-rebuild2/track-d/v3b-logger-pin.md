# v3B Logger Pin — Rung B Trial (anchored calibration)

Pinned 2026-10-07 before the rung-B trial. Supplements PREREG-D-v3-ladder.md §13 line 27.

## Output envelope (prompt-v3B.txt = frozen v2 wording + 3 synthetic calibration exemplars)
- Line 1: integer 0–100 (the score), nothing else
- Line 2: exactly one sentence explaining the score
- No other text

## Mechanical parse (no interpretation, no re-query)
- `extracted_score` = int(line 1 stripped) iff it matches `^\d+$` and 0 ≤ s ≤ 100, else `null`.
- `justification` = line 2 verbatim (`null` iff absent).
- On `null` score: log and move on. No retries, no steering.

## Log schema
File: `track-d/instrument-acceptance-v3b/judge-log-rungB-agentN.jsonl`, one JSON object per line, exactly these fields:
`timestamp, candidate_label, pass_no, prompt_sha256, raw_response, extracted_score, justification`
- `prompt_sha256` must equal `92d2f3e6fa87f2ba6910824d05019f3bb542373e86ddeaab5eaca5a52bb7a1b1` on every record (assert at startup by hashing ../prompt-v3B.txt; abort on mismatch).
- `raw_response` preserves the full response verbatim.

## Audit (red-team, per ladder §2(6))
For every record: `extracted_score == int(first line)` and `justification == second line` (or nulls where absent). Any mismatch = log VOID for that record.
