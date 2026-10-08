# Judge brief — rung-C clean re-run (pairwise forced-choice text comparison)

You are judge agent N of 3 (N = __1__ / __2__ / __3__ — fill your number in).
Your job is a blind text-comparison task: for each presented pair of passages,
decide which contains more French lexical material, and log the result.
You have NOT seen any other task materials. Work only from the files below.

## Files (absolute paths)

- PROMPT: `/home/hatch/workspace/cipher-hunt/lanes/zeschau-seebach-1841/code/side-homophonic-rebuild2/track-d/prompt-v3C.txt`
- PACKAGE: `/home/hatch/workspace/cipher-hunt/lanes/zeschau-seebach-1841/code/side-homophonic-rebuild2/track-d/rerun-rungC-clean/rungC-clean-pkg-N.json` (N = your judge number)
- SCHEDULE: `/home/hatch/workspace/cipher-hunt/lanes/zeschau-seebach-1841/code/side-homophonic-rebuild2/track-d/rerun-rungC-clean/rungC-clean-schedules.json` (use only the entry for judge "N")
- YOUR LOG (create, write-only): `/home/hatch/workspace/cipher-hunt/lanes/zeschau-seebach-1841/code/side-homophonic-rebuild2/track-d/rerun-rungC-clean/judge-log-clean-agentN.jsonl` (N = your judge number)

FORBIDDEN: every other file in the directory, especially any file whose name
contains KEY. Do not list the directory. Do not open anything else. If any
file above is missing or unreadable, stop and report.

## Step 0 — startup verification (do this first)

1. Compute sha256 of the PROMPT file bytes. It MUST equal exactly:
   `d907c59202c9d38e5dfe10bf8048c869bcba2fb547631c02ceb34f93b5b2615e`
   If it does not match, STOP immediately and report a prompt-mismatch.
2. Read your PACKAGE. It has `prompt_sha256` — confirm it equals the same
   value. It lists 14 pairs, each with `pair_id`, `bout`, `label_a`, `text_a`,
   `label_b`, `text_b`.
3. Read the SCHEDULE entry for judge "N": 3 passes, each a list of
   `{pair_id, presented_first}`. You will judge pairs in EXACTLY the listed
   order, pass 1 then pass 2 then pass 3.

## Step 1 — judging (42 calls: 14 pairs x 3 passes)

For each schedule entry in order:
- Look up the pair in your package by `pair_id`.
- Build the judge prompt by filling the PROMPT template with:
  - X = the passage whose label equals `presented_first` (label + its text);
  - Y = the other passage (label + its text).
  X/Y positions are randomized per pass by the schedule — follow it exactly.
- Act as the judge described by the prompt. Read both passages, decide which
  contains MORE French (more identifiable French words and phrases), and emit
  EXACTLY the 3-line envelope the prompt specifies:
  - line 1: exactly the winning label, verbatim, nothing else;
  - line 2: a single integer 0–100 (confidence), nothing else;
  - line 3: exactly one sentence explaining the choice, nothing else.
- Ties are FORBIDDEN by the prompt — you must choose one label.

Judge each of the 3 passes INDEPENDENTLY: do not let earlier passes influence
later ones. Base each decision only on the two passages in front of you.

## Step 2 — logging (disk-first; your log is the evidence)

After EACH call, append ONE JSON line to YOUR LOG file with exactly these fields:
`call_id` (e.g. "N-pass1-P01"), `pair_id`, `pass`, `prompt_sha256`,
`label_x`, `label_y`, `raw_response` (the full 3-line response),
`choice` (line 1 verbatim), `confidence` (line 2 as integer),
`justification` (line 3).
Do NOT overwrite the log. Do NOT write scores anywhere else.

## Step 3 — handoff (transport only, not evidence)

When all 42 calls are logged, reply to your commissioner with ONLY:
(1) confirmation of 42 logged calls, (2) the sha256 checksum of your log file,
(3) any prompt/abort anomalies encountered. Do NOT report choices or scores
in the handoff — the sealed scoring step reads only your checksummed disk log.

## Rules

- Never inspect or reference anything outside the four files above.
- If a passage pair seems malformed (missing text, identical labels), log the
  anomaly as a JSON line with `"anomaly": true` and continue; do not improvise.
- You may not discuss the task with anyone else. Your log is your work product.
