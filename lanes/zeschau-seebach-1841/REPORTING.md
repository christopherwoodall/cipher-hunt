# Reporting convention — Seebach lane

REPORT.md is a living document. A scheduled job sweeps this lane every 2 hours
and folds new material into it. This file defines how workers leave material
for the report.

## The report inbox

Workers leave notes at `report_inbox/<worker-name>-<topic>.md`.
One note per meaningful unit of work. Short markdown, this shape:

```
## <worker>: <topic>
- Context: what I was trying and why I chose this angle
- Decision: the key decision I made (method, threshold, promotion, kill)
- Why: the reasoning behind it — what evidence tipped the decision
- Enlightenment: what surprised me / what changed my mind / the "aha"
- For the report: which section this belongs in + the 1-3 numbers that matter
- Caveats: what I could NOT verify
```

## What the report values (operator's standing order)

Methodology and decision rationale are first-class — not just what was run,
but WHY: why this angle, why this threshold, why a claim was promoted or
killed, and what caused the moment of insight. A null result with its
reasoning is worth more than a positive without it.

## Rules

- Every number must trace to a lane file (name it). No invented numbers.
- Mark provisional vs ground-truth everywhere.
- Figures: if you made a plot for your own analysis and it tells the story,
  drop the PNG in `report_inbox/` too and say where it belongs.
- The sweeper job (not you) edits REPORT.md. You only leave notes.
- Never put credentials or secrets in the inbox.
