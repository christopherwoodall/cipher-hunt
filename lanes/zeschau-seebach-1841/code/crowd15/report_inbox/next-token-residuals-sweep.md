# Battery A16 — residuals sweep (Q5, Q6, §7) + ingestion close-out

Date: 2026-10-07. Runner: battery-runner (resumed, round 15).
Stream: repaired 1,847-pair parse recomputed in-session
(`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`,
per `code/side-keyhunt/repair_parse.py`).

Sources: Q5/Q6 (next-token-findings-que-ce.md), §7
(next-token-findings-parle-and-rest.md), plus no-battery items
(C2, C4, C5, P9, P10, P11, §8, §9) closed here by ingestion.

## Pre-registered bar (written BEFORE touching data)

- **Q5 "est que" ×2** (@217: 59-46-29; @1191: 59-46-07): PROMOTE the
  "c'est que"/"il est que" frame iff both windows parse with no
  contradiction; else HOLD as unconfirmed.
- **Q6 "que la [21] [67]"** (@107): single speculative window — HOLD
  unless 21/67 resolve; do not spend more than a parse check.
- **§7 "le m…"** (@1033: 17-77-82-63-11-67; @1157: 17-77-82-44-83-21):
  "fois le m" ×2 ("le même"/"le monsieur"/"le ministre" candidates).
  PROMOTE a 63/44 continuation iff their contact profiles show
  m-initial-word continuation (shared pre=82 frame); else HOLD.
- **No-battery items** (per finder instructions): C2 (distributional fact),
  C4 (exclusion, lane record), C5 (78-fork's target — not mine), P9
  (corroborative — ingested as +2 legs for 31=VERBAL), P10 (slot-pairs
  listed for future), P11/@791 & §8/@790 (red-team only — not pursued),
  §9 (boundary artifacts — no batteries). Closed by ingestion note, not
  re-tested.

## Data

### Q5 "est que" ×2

- @217: `06-59-46-29-42-16` = "[06] est que [42]er [16]" — parses ONLY with
  a clause boundary: "[06] est. Que [42]er…" ("it is. What to [42]…",
  Q2's deliberative infinitive). No "c'est" (no "ce" before 59).
- @1191: `84-59-46-07-24` = "[84=on] est que [07]…" — "on est que [07]"
  does not parse as "c'est que"/"il est que".
→ Neither window cleanly shows the construction. **HOLD** (unconfirmed).

### Q6 "que la [21] [67]" @107

Single speculative window; 21/67 unresolved; already fenced in A9
("pour que la [21] [67]", 67-fork-conditional). **HOLD**. No more spent.

### §7 "fois le m" ×2

17-77-82 ×2: @1040 (`…40-17-77-82-63-11-67` = "…e fois le m[63] la [67]",
the crib extension) and @1157 (`…17-77-82-44-83-21` = "fois le m[44]…").
The trigram unit is solid (2× identical). Continuation test:
- 63 (n=12): pre=82 ×1 (this window only); sucs 00×4, 42, 71, 29, 77, 45.
- 44 (n=15): pre=82 ×1 (this window only); sucs 00×3, 59×2, 74×2, 83×2.
Each follows 82 exactly once — "même"/"monsieur"/"ministre"
indistinguishable at n=1. **HOLD** (unit solid, value unknown).

### Ingestion close-out (no batteries, per finder instructions)

- **C2** ("ce qui" 4/5 formulaic): distributional fact — confirmed in
  passing (A4/A11/A13 all hit "ce qui" frames). Ingested, no battery.
- **C4** (@824 NOT "c'est"): exclusion, lane record (round-14 WO#7).
  Ingested, not re-litigated.
- **C5** ("ce [78]" ×2 @572/@628): queued for the round-14 78-fork —
  not this pipeline's. Ingested, forwarded.
- **P9** ("qui 31 [VERBAL]" ×2 @337/@1646): corroborative — ingested as
  +2 legs for 31=finite-verbal (no new value).
- **P10** (doublet slots 02/52/06/47/98 ×2): listed for future batteries.
  Ingested, not run.
- **P11** (@791) / **§8** (@790 "le qui que"): red-team-only oddities —
  explicitly not pursued. Ingested, flagged.
- **§9** (boundary artifacts @997/@868/@1050/@554/@499/@61/@684/@290):
  explicitly no batteries. Ingested.

## Verdicts

- **Q5: HOLD** — "c'est que"/"il est que" unconfirmed (0/2 clean windows).
- **Q6: HOLD** — single speculative window, parked.
- **§7: HOLD** — "fois le m" ×2 unit solid; continuation value unknown
  (63/44 at n=1 each, indistinguishable).
- All no-battery items ingested and closed with their finder-stated
  dispositions. Queue empty.
