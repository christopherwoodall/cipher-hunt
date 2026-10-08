# Judge brief — Track D memorization re-probe (blind 0–100 French-fluency rating)

You are judge agent N of 3 (N = __1__ / __2__ / __3__ — fill your number in).
Your job is a blind text-rating task: for each presented passage, rate its French fluency 0–100.
You have NOT seen any other task materials. Work only from the files below.

## Files (absolute paths)

- PROMPT: `/home/hatch/workspace/cipher-hunt/lanes/zeschau-seebach-1841/code/side-homophonic-rebuild2/track-d/judge_prompt.txt`
- PACKAGE: `/home/hatch/workspace/cipher-hunt/lanes/zeschau-seebach-1841/code/side-homophonic-rebuild2/track-d/memorization-reprobe-run/pkg-N.json` (N = your judge number)
- YOUR LOG (create, write-only): `/home/hatch/workspace/cipher-hunt/lanes/zeschau-seebach-1841/code/side-homophonic-rebuild2/track-d/memorization-reprobe-run/judge-log-agentN.jsonl` (N = your judge number)

FORBIDDEN: every other file in the lane directory, especially any file whose name
contains KEY, any candidates file other than your package, and any schedules file.
Do not list directories. Do not open anything else. If any file above is missing
or unreadable, stop and report.

## Step 0 — startup verification (do this first)

1. Compute sha256 of the PROMPT file bytes. It MUST equal exactly:
   `390a1ec0bf1aa9e0e495a5fe98e65107c41025c954cd11b68d1931816c08e21d`
   If it does not match, STOP immediately and report a prompt-mismatch.
2. Read your PACKAGE. It has `prompt_sha256` — confirm it equals the same value.
   It has `order` (12 blind 8-hex labels) and `candidates` (label → passage text).

## Step 1 — judging (12 calls, in EXACT package order)

For each label in `order`, in order:
- Build the judge prompt by filling the PROMPT template with `{text}` = that label's passage.
- Act as the judge described by the prompt. Rate the passage's FRENCHNESS 0–100
  and emit EXACTLY the 2-line envelope the prompt specifies:
  - line 1: a single integer 0–100, nothing else;
  - line 2: exactly one sentence explaining the score, nothing else.
- Rate each passage INDEPENDENTLY: do not let earlier passages influence later ones.
  Base each rating only on the passage in front of you.

## Step 2 — logging (disk-first; your log is the evidence)

After EACH call, append ONE JSON line to YOUR LOG file with exactly these fields:
`call_id` (e.g. "N-01"), `label`, `pass` (your judge number N, acting as one of 3
independent passes), `prompt_sha256`, `raw_response` (the full 2-line response),
`extracted_score` (line 1 as integer, or null with `"extraction_failed": true` if
line 1 is not a bare integer 0–100 — log it, do NOT re-query).
Do NOT overwrite the log. Do NOT write scores anywhere else.

## Step 3 — handoff (transport only, not evidence)

When all 12 calls are logged, reply to your commissioner with ONLY:
(1) confirmation of 12 logged calls, (2) the sha256 checksum of your log file,
(3) any prompt/abort/extraction anomalies encountered. Do NOT report scores or
ratings in the handoff — the sealed scoring step reads only your checksummed disk log.

## Rules

- Never inspect or reference anything outside the three files above.
- If a passage seems malformed (missing text), log the anomaly as a JSON line
  with `"anomaly": true` and continue; do not improvise.
- You may not discuss the task with anyone else. Your log is your work product.
