# v3 Logger Pin — Rung A Trial (R15a binding)

Pinned 2026-10-07 before the rung-A trial. This supplements (does not modify)
`PREREG-D-v3-ladder.md` §13 line 27.

## Output envelope (prompt-v3A.txt)
- Line 1: integer 0–100 (the score)
- Line 2: comma-separated French word/phrase list, or the literal token `NONE`
- Line 3+: one-sentence justification (may wrap; everything after line 2 is justification)

## Mechanical parse (no interpretation, no re-query)
- `extracted_score` = int(line 1 stripped) iff it matches `^\d+$` and 0 ≤ s ≤ 100, else `null`.
- `word_list` = line 2 stripped verbatim (may be `NONE`); `null` iff line 2 absent.
- `justification` = lines 3+ joined, verbatim.
- On `null` score: log and move on. No retries, no steering.

## Log schema
File: `track-d/instrument-acceptance-v3a/judge-log-rungA-agentN.jsonl`, one JSON
object per line, exactly these fields:
`timestamp, candidate_label, pass_no, prompt_sha256, raw_response, extracted_score, word_list, justification`
- `prompt_sha256` must equal `84393ae4c5f702f218841636871715e84f790be524d3e380bf4fb283f1fcd85e` on every record (asserted at startup; abort on mismatch).
- `raw_response` preserves the full multi-line response verbatim.

## Audit (red-team, per ladder §2(6))
For every record: `extracted_score == int(first line)` and `word_list == second line`
(or nulls where absent). Any mismatch = log VOID for that record.
