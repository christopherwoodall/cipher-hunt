# Battery report: voi-86-dwindow-composition

**Target:** `voi-86-dwindow-composition` (P2)
**Date:** 2026-10-09
**Verdict:** NULL

## Bar (verbatim from queue, pre-registered before testing)

"Kill the global-"voi" hypothesis iff any D-window forces a determiner-exclusive parse; else promote window-local "voi" readings."

## Bar restated as numbered clauses

1. KILL the global-"voi" hypothesis iff at least one D-window of 86 forces a determiner-exclusive parse using only ratified neighbor values.
2. Otherwise, PROMOTE the window-local "voi"-family readings that parse cleanly with ratified-only neighbor values.

## Method

Read BATTERY-PROTOCOL.md first; created `locks/voi-86-dwindow-composition.lock` on start (deleted on completion).
Re-derived the repaired 1,847-pair / 96-type stream in-session from `code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt` (parsed per `code/side-keyhunt/repair_parse.py`; asserts 1847/96 held). `canonical.py` never used. R5005, sealed gates, red-team queue untouched.

Adopted test frame (coordinate, not duplicate): D-life = 86-windows whose follower is not in {29,59,06}. Independently re-derived: n(86)=32, n(D-life)=26, n(V-life)=6 — matches the partition batteries exactly.

Ratified values used (kill-grade): pencil (11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que) + red-team granted (87=ce, 64=qui, 96=par, 17=fois, 79=tout, 00=pour, 84=on, 47=ce). Battery-level values (24=verb class, 77='le', 65=noun, 94='ne', 06='ent', 39='a', etc.) cited as caveated where relevant, never as kill-grade force.

## D-window census (re-derived, ±3 context, 0-based)

| idx | row | context |
|---|---|---|
| 175 | a1_05 | 60 09 87 [86] 21 69 14 |
| 300 | a2_04 | 78 40 97 [86] 91 18 89 |
| 557 | a3_01 | 59 34 17 [86] 94 59 30 |
| 661 | a4_02 | 62 16 00 [86] 50 80 03 |
| 671 | a5_00 | 20 67 11 [86] 24 80 03 |
| 716 | a5_01 | 63 00 66 [86] 01 02 21 |
| 728 | a5_02 | 64 11 00 [86] 48 88 11 |
| 799 | a5_04 | 37 44 77 [86] 44 74 62 |
| 867 | a5_07 | 47 46 00 [86] 70 87 77 |
| 878 | a5_08 | 49 16 77 [86] 78 17 08 |
| 899 | a5_08 | 14 98 83 [86] 16 92 67 |
| 948 | a6_00 | 62 98 96 [86] 01 77 86 |
| 951 | a6_00 | 86 01 77 [86] 96 87 46 |
| 962 | a6_00 | 67 96 00 [86] 56 41 19 |
| 1002 | a6_02 | 82 33 00 [86] 56 47 91 |
| 1099 | a6_06 | 06 29 67 [86] 52 82 94 |
| 1128 | a6_07 | 37 43 00 [86] 52 37 86 |
| 1131 | a6_07 | 86 52 37 [86] 24 77 86 |
| 1134 | a6_08 | 86 24 77 [86] 20 62 98 |
| 1147 | a6_08 | 42 98 98 [86] 67 33 66 |
| 1335 | a7_05 | 52 39 83 [86] 71 64 60 |
| 1345 | a7_05 | 52 38 47 [86] 66 73 34 |
| 1458 | a7_09 | 61 21 67 [86] 66 79 17 |
| 1506 | a7_11 | 42 33 00 [86] 56 41 12 |
| 1739 | a8_07 | 12 48 52 [86] 12 34 94 |
| 1792 | a8_09 | 47 03 00 [86] 56 42 94 |

## Clause 1: does any D-window force a determiner-exclusive parse? NO (0/26)

A determiner-exclusive parse requires "86 [noun]" with the follower a ratified noun — but no D-window follower is a ratified value. Follower census across the 26 windows (re-derived): 56 x4, 52 x3, 66 x2, 21/24/44/78/20/91/94/48/70/16/67/71/12/50/01 x1 each — zero followers in the ratified set {la, pre, m, i, er, e, que, ce, qui, par, fois, tout, pour, on}. With ratified-only values, every window admits non-determiner readings (noun-class per the battery-promoted subsets, word-internal, verb-class) that are not kill-grade dead:

- @671 is the mirror image of the test: "11 [86]" = "la [86]" — 11='la' is pencil, so a determiner reading of 86 is what dies here ("la" + determiner is ungrammatical), not forced.
- @175/@1345 ("ce [86]"): a noun reading parses; determiner is not forced (the voir-sweep already showed this window is dead even under a determiner reading: "ce"+determiner is ungrammatical).
- @951 ("[77] [86] par"): 96='par' is granted, killing the clitic reading — but a noun reading survives on ratified-only values (provisional 77='le' is the battery-level leg, not kill-grade). Determiner-exclusive is not forced.
- @728/@867/@962: orthogonal granted-defects ("la pour", "que pour", "par pour" are ungrammatical under granted values regardless of 86's value — adopted from the partition battery). They discriminate nothing about 86.
- The remaining windows (open neighbors: @300/@557/@716/@799/@878/@899/@948/@1002/@1099/@1128/@1131/@1134/@1147/@1335/@1458/@1506/@1739/@1792) admit open readings under ratified values.

Clause 1: **FAIL (kill arm does not fire).** The global-"voi" hypothesis is not killed by this battery.

## Clause 2: clean window-local "voi" readings under ratified-only values: 0/26

The "voi"-family compositions were attempted at every D-window under the rule (a) real 1841 French word, (b) every group in the word assigned, no residue, (c) grammatical clause, with neighbors restricted to ratified values:

- **"pourvoi" family** (@661/@962/@1002/@1506/@1792 "00 [86] X"): "pour"(00 granted) + 86="voi" gives the real noun "pourvoi" — but the follower (50/56) is unvalued at ratified grade, so no licensed clause exists. Undemonstrable, not clean.
- **revoir/prévoir/entrevoir/apercevoir family:** requires ratified left neighbors meaning "re"/"pré"/"entre"/"aper" — no D-window left neighbor is in the ratified set. None demonstrable.
- **"voisin"-family:** no "vois-" contact exists at any D-window. None demonstrable.
- **"voix" whole-word:** @175 "ce voix" and @1345 "ce voix" are ungrammatical ("ce" + feminine noun); @671 "la voix" parses its left edge but 24 is open, so no clean full window under ratified-only values.

Clause 2: **0/26 clean readings** — the promote arm has zero legs.

## Per-clause verdict

1. Kill: does not fire (0/26 windows force determiner-exclusive).
2. Promote: no clean window-local "voi" reading under ratified-only values (0/26).

**Verdict: NULL.** The global-"voi" hypothesis is not killed on the D-partition, but nothing on the D-partition promotes it either. This is consistent with (not a duplicate of) the earlier voir-86-sweep NULL: that battery used all standing values and found "0/26 D-windows compose"; this battery is an independent ratified-only re-derivation with a different bar (determiner-exclusive force test), and converges on the same outcome.

## Adverses

- "Depends on red-team adjudication of the 86 split (redteam-889-pourvoient P1 must adjudicate before any 'voi'-family promotion)": ANSWERED — no promotion is declared at any level; nothing here pre-empts the red-team venue. A null does not promote.
- "reseg-553-retry owns the @553 residual": ANSWERED — @553 is V-life (follower 59), not a D-window; untouched, not re-litigated.
- §7 intact: no polyvalence declared (the noun-class arms live at battery level on subsets per the partition battery; this null does not merge them).

## Follow-up targets (for supervisor queuing; all verified absent from battery-queue.json)

1. `dwindow-voisin-family` (P3): test the "voisin"/"voisine"-family (86 as "vois-" prefix) at D-windows once at least one neighbor value names — the only "voi"-family arm not testable with ratified-only neighbors.
2. `pourvoi-56-frame` (P3): test "pourvoi" (noun) at the five "00 86 56/50" windows (@661/@962/@1002/@1506/@1792) once 56's value names; discriminates the noun-"pourvoi" locus.
3. `dwin-671-la-noun` (P4): re-test "la [86]" at @671 once 24's class is named (red-team venue) — the strongest window-local "voix" frame, conditional on a following verb.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-voi-86-dwindow-composition.md`
- Queue: `battery-queue.json` → `voi-86-dwindow-composition` status `verdict`, result `null`, date 2026-10-09 (pre-write assert: was `queued`, `verdict: null`; temp-file + rename; only this entry touched; JSON re-validated)
- Lock `code/crowd17/next-token/locks/voi-86-dwindow-composition.lock` created on start, deleted on completion.
- R5005, sealed gate instances, red-team adjudication queue untouched. No standing or red-team verdict contradicted or downgraded.
