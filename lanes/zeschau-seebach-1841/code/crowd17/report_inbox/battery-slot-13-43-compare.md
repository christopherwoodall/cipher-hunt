# Battery verdict: slot-13-43-compare

## Bar (verbatim, pre-registered)

- CLAIM: 13 and 43 share a slot
- BARS: (a) state 13's (n=12) and 43's (n=16) full contact profiles; (b) same-slot iff successor-set overlap exceeds chance under a stated test; (c) if same slot, propose the shared class
- ADVERSES: both values open; small samples (n=12/n=16); section 7 sole-polyvalence (no value declared at battery level)

Restated as numbered pass/fail clauses:

1. **C1** — full contact profiles of 13 (n=12) and 43 (n=16) stated from the repaired stream.
2. **C2** — successor-set overlap of {13, 43} exceeds chance under a stated one-sided test (p < 0.05).
3. **C3** — if C2 passes, propose the shared class.

## Method

- Read BATTERY-PROTOCOL.md first. Lock `locks/slot-13-43-compare.lock` created on start
  (agent 8bf72f56-770e-40b4-9565-246f84455e81, 2026-10-09T05:03:59Z), deleted on completion.
- Re-derived the repaired stream in-session from `data/upstream-ct_R5005.txt` +
  `code/side-keyhunt/repaired_offsets.json` (parse per `repair_parse.py`):
  **1,847 pairs / 96 types verified**. `canonical.py` never used.
- R5005, sealed gates, red-team adjudication queue untouched. 1841 diplomatic French only.
- All @-offsets below are 1-based stream indices of the target token.

## Clause results

### C1 — PASS (profiles stated byte-exact)

**13 (n=12):**

| @ | window (pre, 13, suc) |
|---|---|
| 69 | 69 **13** 24 |
| 140 | 65 **13** 66 |
| 457 | 65 **13** 66 |
| 482 | 00 **13** 52 |
| 568 | 97 **13** 76 |
| 576 | 45 **13** 55 |
| 823 | 95 **13** 24 |
| 1167 | 45 **13** 55 |
| 1361 | 35 **13** 92 |
| 1382 | 69 **13** 24 |
| 1555 | 99 **13** 93 |
| 1685 | 65 **13** 93 |

- Predecessors (8 distinct): 65 x3, 69 x2, 45 x2, 00, 97, 95, 35, 99 — sums to 12.
- Successors (7 distinct): 24 x3, 66 x2, 55 x2, 93 x2, 52, 76, 92 — sums to 12.
- Read: 13 sits between nominal-adjacent predecessors (65 noun-class x3, 45 x2) and
  verb-heavy successors (24 x3 'faire'/verb-class, 93 x2 verb-class).

**43 (n=16):**

| @ | window (pre, 43, suc) |
|---|---|
| 22 | 82 **43** 29 |
| 44 | 88 **43** 81 |
| 245 | 56 **43** 00 |
| 259 | 32 **43** 77 |
| 344 | 96 **43** 87 |
| 387 | 37 **43** 91 |
| 440 | 46 **43** 98 |
| 564 | 11 **43** 24 |
| 1028 | 96 **43** 87 |
| 1093 | 06 **43** 07 |
| 1127 | 37 **43** 00 |
| 1205 | 47 **43** 55 |
| 1304 | 08 **43** 21 |
| 1306 | 43 **43** 77 |
| 1545 | 78 **43** 00 |
| 1725 | 37 **43** 98 |

- Predecessors (13 distinct): 37 x3, 96 x2, 82, 88, 56, 32, 46, 11, 06, 47, 08, 21, 78 — sums to 16.
- Successors (11 distinct): 00 x3, 77 x2, 87 x2, 98 x2, 29, 81, 91, 24, 07, 55, 21 — sums to 16.
- Read: 43 sits after prepositional/predicative frames (96 'par' x2, 37 predicative x3)
  and before nominal complements (00 'pour' x3, 77 'le' x2, 87/47 'ce' x2) —
  the noun-profiled distribution.

### C2 — FAIL at distributional grade (kill-grade, per §4)

Stated test: hypergeometric overlap of successor sets, one-sided.
Population N=96 types. |succ(13)|=7 drawn as the "success" set, |succ(43)|=11 drawn
as the sample.

- Observed overlap: **2** keys — {24, 55}.
- Expected under chance: 7 x 11 / 96 = 0.80.
- P(X >= 2) = **0.182** (scipy hypergeom; 20k-draw Monte Carlo = 0.186).
- P(X = 0) = 0.414, P(X = 1) = 0.404, P(X = 2) = 0.151.

Two shared successors out of 16 pooled distinct successors is ordinary under chance;
the bar's "exceeds chance" condition is not met (0.182 >> 0.05). The claim fails its
own discriminating test.

Supporting (not the bar): predecessor overlap is **0** shared keys
(13: {65,69,45,00,97,95,35,99} vs 43: {37,96,82,88,56,32,46,11,06,47,08,21,78}),
against 1.08 expected — the two groups' environments are actively disjoint.

Class-level read (context, no value declared): 43 is noun-profiled in the 43 docket
line (par-43 adverbials, "par 43" x2, "43 pour" x3); 13's successors are verb-heavy
(24 x3, 93 x2). The overlap sits exactly where two verb-adjacent nominal slots
would share governors — not evidence of one shared slot.

### C3 — NOT REACHED

C2 fails, so no shared class is proposed.

## Adverses answered

- Small samples: the hypergeometric test is exact for small n; the failure is a
  genuine no-signal result, not a power artifact (observed overlap sits at the
  distribution's center, not the margin).
- §7: no value or class declared for either group at battery level; nothing
  contradicts standing verdicts. No red-team verdict on 13/43 exists; nothing
  overwritten or downgraded.

## Verdict: KILL

The claim "13 and 43 share a slot" fails its pre-registered discriminating clause
at distributional grade: successor overlap does not exceed chance (p = 0.18), and
predecessor environments are fully disjoint. No window forces the claim false, but
the bar's stated test rejects the same-slot reading at the lane's standard.

## Bookkeeping

- `battery-queue.json` `slot-13-43-compare` → status `verdict`, result `kill`,
  date 2026-10-09 (temp-file + rename in the same directory, pre-write assert
  confirmed queued/verdictless, JSON re-validated post-write).
- Lock created on start, deleted on completion. No follow-ups owed (kill verdict).
