# Next-token pipeline — crowd17 (durable infrastructure)

Direct French-intuition prediction, tested against the cipher at byte level.
No training step: predict from 1840s diplomatic register, pre-register bars,
test against the repaired 1,847-pair stream, verdict.

## File layout

```
code/crowd17/next-token/
  README.md              this file
  battery-queue.json     single source of truth: every target, queued or verdict
  build_queue.py         rebuilds battery-queue.json from spec (idempotent,
                         never downgrades existing verdicts)
  BATTERY-PROTOCOL.md    worker brief: bars, stream, verdicts, locks, constraints
  finder-beats.md        wave-1 registry (complete) + wave-2 proposed beats
  locks/                 <id>.lock per running worker; stale after 90 min
code/crowd17/report_inbox/
  battery-<id>.md        one verdict report per tested target
  next-token-findings-<beat>.md   finder reports (wave 2+)
```

## How a supervisor resumes this (from disk alone)

1. Read `battery-queue.json`. Count `status: "queued"` by priority.
2. Check `locks/`: any lock older than 90 minutes is stale — its target is
   re-dispatchable (note the stale lock in the new worker's brief).
3. Spawn one battery worker per queued target, highest priority first, each
   with BATTERY-PROTOCOL.md as its brief. Never reduce worker count on nulls.
4. As `battery-<id>.md` reports land in `code/crowd17/report_inbox/`, verify
   each updates `battery-queue.json` (status → verdict, verdict filled).
5. Null verdicts MUST carry 1–3 follow-up targets: add them to the queue
   (priority ≤ the parent's, usually +1).
6. Promote-verdicts go to the red team for adjudication before the board changes.
7. When wave-2 beats complete, ingest their battery targets into the queue.
8. Update `code/table-grid/table-registry.json` only on red-team grants, then
   regenerate the grid (`python3 code/table-grid/generate.py`).

## Standing rules

- Nulls regenerate work; they never end it. Never reduce worker count.
- Red-team adjudicates promotions. Battery workers never overwrite a standing
  red-team verdict — contradictions escalate as nulls.
- Bars are pre-registered before testing, never rewritten after seeing data.
- Adverses are answered or fenced, never ignored.
- Stream discipline: repaired 1,847-pair parse only; never
  `code/side-keyhunt/canonical.py` (obsolete 1,846-pair parse); never R5005.
- Every number traces to a lane file. Nothing is invented.

## Current state (2026-10-07, at build)

56 targets: 24 verdicts (15 promote / 4 kill / 2 split / 3 null-hold),
32 queued (8 per priority 1–4). Priority-1 queue: 94="ne", 12="n"+48="e",
77="le", 33="dire" (29-blocker noted), 78="ver", 30="pas", 39="a/à",
62/84 "on" collision. Round-15 red-team adjudications (A1–A16) are the
standing law; the crowd16 est-finder's challenge to A1's 37 frames is
queued as `frame-37-reexam` for red-team re-adjudication.
