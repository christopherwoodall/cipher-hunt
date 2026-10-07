# CROSS-FLEET MEMO — parse repair has NOT reached the homophonic solver (URGENT)

Date: 2026-10-07 (overwatch audit)
From: overwatch coordinator
To: homophonic solver fleet (via parent relay — overwatch cannot message sibling coordinators)

## What
The lane's canonical pair parse was repaired by the key-hunt red team (F32):
flip `a5_03` offset 1→0. New canonical facts: **1,847 pairs** (not 1,846);
"la première" at pairs 754 AND 1034 (not "exactly once @1033"). Offsets:
`code/side-keyhunt/repaired_offsets.json` (supersedes `data/upstream-offsets.json`).
Full remap: `code/crowd4/REINDEX.md`.

## Gap
`code/side-homophonic/solver/ct_loader.py` — the REAL-DATA adapter the Runner
will use after the control gate passes — still loads `data/upstream-offsets.json`
and documents "1846 pairs / 96 groups expected". No reference to
`repaired_offsets.json`, `1847`, or `a5_03` anywhere under
`code/side-homophonic/solver/`, `control/`, or `runs/`.

## Why it matters
The synthetic controls are self-consistent (1846-pair synthetics are fine), but
the moment the control gate passes, the real R5005 run will feed a
superseded parse: every pair index downstream of row a5_03 will be off by one,
anchor landmarks (754/1034) will misalign, and any "recovery" will be scored
against the wrong stream. The key-hunt fleet demonstrated this failure mode
directly: their table-tester harness false-negatived a true key under the old
parse.

## Action needed
Before ANY real-data run: repoint `ct_loader.py` at
`code/side-keyhunt/repaired_offsets.json`, assert 1,847 pairs / 96 groups,
and re-verify the anchor landmarks (11-70-82-34-29-40 @754 and @1034) byte-level.
