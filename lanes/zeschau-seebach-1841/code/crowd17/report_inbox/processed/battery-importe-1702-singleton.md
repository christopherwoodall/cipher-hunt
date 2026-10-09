# Battery report: importe-1702-singleton

- Target id: `importe-1702-singleton`
- Claim: test whether the @1702 'n'importe' frame can ever grow beyond a singleton: sweep all 37 @94 windows for a second elision-licensed 94-30 adjacency.
- Date: 2026-10-09
- Worker: battery worker (subagent session 436d095f-4291-475e-aca9-6e7bfb21281f)
- Stream: repaired 1,847-pair / 96-type parse re-derived in-session from `data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed like `code/side-keyhunt/repair_parse.py` (asserts held: 1,847 pairs, 96 groups). `canonical.py` never used. R5005, sealed gate instances, and the red-team adjudication queue were not touched.

## Bar (verbatim, pre-registered before testing)

"test whether the @1702 'n'importe' frame can ever grow beyond a singleton: sweep all 37 @94 windows for a second elision-licensed 94-30 adjacency under any value assignment consistent with standing verdicts; if none, record @1702 as a terminal singleton (strengthens confinement, bounds the rival permanently)"

Numbered pass/fail clauses (restated before testing, not modified after):

1. **C1 (sweep):** every one of the 37 94-windows is inspected; every '94 30' adjacency is enumerated.
2. **C2 (second-instance test):** a second adjacency beyond the @1702 locus must be tested for elision-licensed 'n'importe' under value assignments consistent with standing verdicts.
3. **C3 (resolve):** if none exists, @1702 is recorded as a terminal singleton (confinement strengthened, rival bounded permanently).

## Method

1. Read BATTERY-PROTOCOL.md first. Created `code/crowd17/next-token/locks/importe-1702-singleton.lock` on start (agent id + UTC timestamp); deleted on completion.
2. Ran a byte-exact sweep script over the repaired stream: census of all 37 94-windows, their right neighbors, every '94 30' direct adjacency, and every '94 X 30' one-gap window.

## Window-level evidence

### C1 — full sweep (37/37 windows inspected)

- **n(94) = 37** (byte-confirmed).
- **Direct '94 30' adjacencies stream-wide: exactly 1** — 0b@1701, row a8_06: `91@1698 85@1699 33@1700 94@1701 30@1702 20@1703 62@1704 94@1705 88@1706`. This is the @1702 'n'importe' locus itself. No other direct adjacency exists.
- 94 right-neighbor census (all 37): 92 x2, 93 x1, 24 x2, 65 x1, 06 x1, 74 x3, 02 x1, 64 x1, 59 x3, 52 x3, 82 x4, 76 x2, 29 x1, 60 x1, 07 x1, 15 x1, 26 x1, 87 x1, 70 x1, 79 x2, 84 x1, 30 x1, 88 x1, 44 x1. 30 is a singleton follower of 94.

### C2 — second-instance test

- The sole non-locus candidate for an elision-bridged variant is the single **one-gap '94 X 30' window: 0b@558, row a3_02: `94 59 30`**.
- **Not elision-licensed under standing values:** 59='est' is provisional (§7). For the gap to bridge into an 'n'importe' frame, 59 would have to be vacuous or elidable; standing values give 59='est', a finite verb, forcing "ne est [30]" — incompatible with 'n'importe' ("ne"+"importe" requires the elision-licensed 'n'' before a vowel-initial verb, and no such form exists here). No value assignment consistent with standing verdicts licenses elision across 59.
- No other '94 X 30' pattern exists (only the one one-gap window).

### C3 — resolve

- **@1702 is a terminal singleton.** The 'n'importe' frame cannot grow beyond it: zero second direct adjacency, and the one gap-pattern is unlicensable under standing values.

## Per-clause pass/fail

1. Sweep 37/37, adjacencies enumerated (1): **PASS**
2. Second-instance test (one-gap candidate fails under standing values): **PASS**
3. Terminal singleton recorded: **PASS**

## Adverses answered

- "'importe' stays @1702-word-formation-confined; the rivalry is settled at battery level (0/19 discriminating windows)." — CONFIRMED and strengthened: this sweep adds the distributional fact that no second '94 30' adjacency exists anywhere, bounding the rival permanently at the word-formation level.

## Verdict: PROMOTE (confinement claim)

All bar clauses pass; adverses answered (confirmed, not ignored). @1702's 'n'importe' frame is a terminal singleton. No standing/red-team verdict contradicted or downgraded; §7 intact. Canonical-stream caveat stands (row a8_06 offset unvalidated). Per §4 a promote regenerates no follow-ups; none proposed.

## Bookkeeping

- `battery-queue.json`: `importe-1702-singleton` queued → verdict/promote via temp-file + rename, own entry only; pre-write assert confirmed no prior verdict; JSON re-validated.
- Lock `importe-1702-singleton.lock`: created on start, deleted on completion.
- R5005, sealed gate instances, red-team adjudication queue untouched.
