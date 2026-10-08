# v3C Logger Pin — Rung C Trial (pairwise forced-choice)

Pinned 2026-10-07 before the rung-C trial. Supplements PREREG-D-v3-ladder.md §13 line 27.

## Output envelope (prompt-v3C.txt)
- Line 1: exactly the winning label, verbatim, nothing else
- Line 2: a single integer 0–100 (confidence; 50 = pure guess)
- Line 3: exactly one sentence explaining the choice
- No other text

## Mechanical parse (no interpretation, no re-query)
- `choice` = line 1 stripped verbatim; must equal one of the two presented labels, else `null` (VOID record).
- `confidence` = int(line 2 stripped) iff `^\d+$` and 0 ≤ c ≤ 100, else `null`.
- `justification` = line 3 verbatim (`null` iff absent).
- On `null` choice: log and move on. No retries, no steering. Ties are forbidden by the prompt; a tie response is a VOID record.

## Log schema
File: `track-d/instrument-acceptance-v3c/judge-log-rungC-agentN.jsonl`, one JSON object per line, exactly these fields:
`timestamp, pair_id, label_x, label_y, presented_first, pass_no, prompt_sha256, raw_response, choice, confidence, justification`
- `prompt_sha256` must equal `d907c59202c9d38e5dfe10bf8048c869bcba2fb547631c02ceb34f93b5b2615e` on every record (assert at startup by hashing ../prompt-v3C.txt; abort on mismatch).
- `pair_id` = stable id from the package; `label_x`/`label_y` = the two blind labels as presented in the prompt; `presented_first` = which label appeared first in this pass (position randomization is per-pass).
- `raw_response` preserves the full response verbatim.

## Audit (red-team, per ladder §2(6))
For every record: `choice` ∈ {label_x, label_y} (verbatim), `confidence` == int(line 2), `justification` == line 3. Any mismatch = record VOID.
Position randomization: across the 3 passes of each pair, each label must appear first at least once (mechanical check).
