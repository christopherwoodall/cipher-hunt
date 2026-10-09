# Battery verdict: reseg-a2_03-a2_04-97gate

- Target id: `reseg-a2_03-a2_04-97gate`
- Claim: "offset-1 constraint sweep of rows a2_03/a2_04 — the 5-gram straddles a row boundary and is phase-fragile"
- Date: 2026-10-09
- Worker: battery worker (subagent 6951afba-253a-4418-8aa8-b82943649bdc)
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py`; asserts 1847/96 held in-session). `canonical.py` never used. R5005, sealed gates, red-team adjudication queue untouched.
- Parent: follow-up #2 of `ver78-296-97gate` (NULL 2026-10-09), which proposed this sweep to test its phase caveat. Third candidate of the mechanism family seg-a1_01 / reseg-1481-98 / frame-43-21-43-doublet.

Terms (ASD-STE100): "phase" = the digit offset (0 or 1) that pairs a row's raw digits. "Rival phase" = the legal alternative offset of an adjacent row. "Contact" = the straddling 5-gram as paired under the canonical offsets. "Novel group" = a pair type outside the 96-type canonical inventory. "Fence" = the contact is marked phase-fragile; arguments leaning on it must carry the canonicality caveat.

## Bar (verbatim, pre-registered before testing)

"clean across the full window iff the rival phase preserves every pair with zero novel groups; fence iff the contact dissolves or a novel group appears"

Numbered pass/fail clauses (restated before testing, not modified after):

1. **C1 (clean arm):** the rival phase preserves EVERY pair of the full window AND introduces zero novel groups → CLEAN.
2. **C2 (fence arm):** the contact dissolves under the rival phase OR a novel group appears → FENCE.

Adverses (queue): none.

## Method

1. Read BATTERY-PROTOCOL.md first. Created `code/crowd17/next-token/locks/reseg-a2_03-a2_04-97gate.lock` on start (agent id + 2026-10-09T18:26:42Z); no prior/stale lock; deleted on completion.
2. Re-derived the repaired stream byte-exact in-session (1,847 pairs / 96 types asserted).
3. Re-paired rows a2_03 and a2_04 under their rival offsets (a2_03: 1→0; a2_04: 0→1), tested both single-row rivals and the combined rival on the two straddling 5-gram windows, and ran the novel-group inventory check across both full rival rows.
4. Adopted, not re-litigated: 11='la', 40='e' (banked GT pencil); 78='ver' LEAD (R16-005); 97 infinitive class (frame-97-profile PROMOTE); stem-86 NULL; the R16-005 @296 residual fence; orphan86-300 KILL. Row-offset adoption is a red-team adjudication act — this battery tests phase-robustness only.

## Window-level evidence (all byte-traced)

Rows (raw digits, 54 each):

| row | repaired offset | canonical pairs |
|-----|----------------|-----------------|
| a2_03 | 1 | `06 67 33 29 89 84 91 37 61 20 61 42 48 52 89 28 00 97 09 64 29 40 65 16 01 11` (26) |
| a2_04 | 0 | `78 40 97 86 91 18 89 88 02 88 20 17 46 84 24 37 78 45 64 59 32 94 06 11 92 60 15` (27) |

- Row boundary: a2_03 ends at global @296; a2_04 starts at global @297.
- W1 @295–299: `01 11 78 40 97` (a2_03 @295–296 | a2_04 @297–299).
- W2 @296–300: `11 78 40 97 86` (a2_03 @296 | a2_04 @297–300) — the ver78-296 one-word candidate.
- Seam digit fact: a2_03's dropped trailing digit is `7`; a2_04's first digit is `7` (doubled `7` at the seam: `...111 7 | 7 78...`).

Rival re-pairings (novel-group check against the 96-type inventory):

| phase | pairs | novel groups |
|-------|-------|--------------|
| a2_03 offset 0 (27 pairs): `00 66 73 32 98 98 49 13 76 12 06 14 24 85 28 92 80 09 70 96 42 94 06 51 60 11 17` | 27 | 0 |
| a2_04 offset 1 (26 pairs): `84 09 78 69 11 88 98 80 28 82 01 74 68 42 43 77 84 56 45 93 29 40 61 19 26 01` | 26 | 0 |

Window outcomes under each rival phase:

| window | canonical | a2_03-rival | a2_04-rival | both-rival |
|--------|-----------|-------------|-------------|------------|
| W1 | `01 11 78 40 97` | `11 17 78 40 97` | `01 11 84 09 78` | `11 17 84 09 78` |
| W2 | `11 78 40 97 86` | `17 78 40 97 86` | `11 84 09 78 69` | `17 84 09 78 69` |

- W1: the full 5-gram survives under NEITHER single-row rival (a2_03-rival keeps `78 40 97` but `01 11`→`11 17`; a2_04-rival keeps `01 11` but `78 40 97`→`84 09 78`). The contact dissolves in every rival phase.
- W2: the boundary bigram `11 78`→`17 78` under a2_03-rival; the whole window re-pairs under a2_04-rival. The `97 86` hapax contact dissolves under a2_04-rival. The contact dissolves in every rival phase.
- Novel groups in every rival window: 0/5, all four cases. No novel group appears anywhere.

## Per-clause pass/fail

### C1 (clean arm): FAIL

No rival phase preserves every pair of either 5-gram window — each rival phase re-pairs at least 2 of the 5 pairs. The zero-novel-groups half holds (0/27 and 0/26 full-row; 0/5 in all rival windows), but the conjunction requires preservation, which fails. The window is not phase-robust.

### C2 (fence arm): FIRES

The contact dissolves under every tested rival phase: W1's `01 11 | 78 40 97` is intact under no single-row rival; W2's `11 | 78 40 97 86` likewise. No novel group appears, but the fence arm's first disjunct is met. The 5-gram is phase-fragile.

## Verdict: NULL — fence executed

The straddling 5-gram contact (`01 11 | 78 40 97` @295–299; `11 | 78 40 97 86` @296–300) is phase-fragile: it dissolves under either adjacent row's legal rival offset, with zero novel groups in all rival phasings. It is a canonical-offset object, not a byte-anchored one — the same pattern as seg-a1_01 (a1_01), reseg-1481-98 (a7_10), and frame-43-21-43-doublet §4 (a7_03/a7_04).

Scope (stated, not hidden):
- This fences the CONTACT as evidence. Any argument leaning on the `01 11 | 78 40 97` or `11 | 78 40 97 86` contact — the ver78-296 residual family, orphan86-300's window, the `97 86` hapax adjacency — must carry the canonicality caveat (68 of 70 upstream row offsets unvalidated).
- It does NOT adjudicate the row offsets (a red-team act), does not touch 78='ver' LEAD, frame-97-profile's 97-infinitive PROMOTE, stem-86's NULL, the R16-005 @296 residual fence, or orphan86-300's KILL. §7 intact.
- The doubled `7` at the digit seam is recorded as a byte fact for the follow-up, not as evidence for either phase.

## Follow-ups (null regenerates work; both verified ABSENT from battery-queue.json)

1. `off-phase-a2-sweep` (P4) — seg-a1_01-style full-row constraint sweep under a2_03 offset-0 and a2_04 offset-1 (kill-grade scan across all 27/26 rival pairs, per the seg-a1_01-constraint-sweep standard); if constraint-clean, package for red-team offset adjudication alongside a1_01/a7_10/a7_03/a7_04.
2. `seam-77-doublet-check` (P4) — byte-level audit of the doubled `7` at the a2_03|a2_04 digit seam (`...111 7 | 7 78...`): transcription artifact or coincidence; decides whether the seam itself carries byte evidence favoring either phase.
3. `rere-296-residual` already queued (owns the residual's future) — not re-proposed.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-reseg-a2_03-a2_04-97gate.md` (this file).
- Queue: `reseg-a2_03-a2_04-97gate` queued → `verdict`/`null`, 2026-10-09 (pre-write assert passed — was queued/verdictless; temp-file + rename; JSON re-validated; own entry only; no downgrade).
- Lock `code/crowd17/next-token/locks/reseg-a2_03-a2_04-97gate.lock` created on start, deleted on completion (verified gone).
- R5005, sealed gate instances, red-team adjudication queue untouched.
