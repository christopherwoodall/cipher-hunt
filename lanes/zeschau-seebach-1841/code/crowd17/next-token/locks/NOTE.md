# Lock semantics

A battery worker creates `locks/<target-id>.lock` when it starts a target
and deletes it when the verdict is recorded in `battery-queue.json`.

Lockfile content: `<agent-id> <UTC-timestamp>`, one line.

- One worker per target. Check `locks/` before taking a target.
- A lock older than 90 minutes is STALE: the worker died. A supervisor may
  re-dispatch the target; the new worker notes the stale lock in its report.
- Locks are never committed as "done" — only the verdict record in
  `battery-queue.json` + the report in `code/crowd17/report_inbox/` count.
- This NOTE.md is the only file that lives here permanently; real lockfiles
  are transient.
