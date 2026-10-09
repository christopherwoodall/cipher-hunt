# Battery report: de83-932-gate

- Target id: `de83-932-gate`
- Claim: "decide 83's value at @932 to close or re-open the W1 infinitive residual"
- Date: 2026-10-09
- Worker: battery worker (subagent 4af22a78-492f-4980-ac4f-9dab8286cf47)
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py`). Verified in-session: 1,847 pairs, 96 types. `canonical.py` never used. R5005, sealed gates, red-team queue untouched.

Terms (ASD-STE100): "gate" = the decision point. "residual" = the leftover infinitive reading of 56 at W1. "W1" = 0-based @932. "W2" = 0-based @1626. "kill grade" = evidence strong enough to close a reading.

## Parent context

Follow-up 2 of battery-form-56-1627 (PROMOTE, 2026-10-09): 56's form is 3sg finite ("crée"-shaped) at both formula windows @932 and @1626. The W1 residual: the only infinitive license would be 83='de' ("de [56]"), but 83='de' was not standing — le83-window NULL fenced 83 as the blocker, and the 'de' lead came from the KILLED frame-vient-parvenir. Per the parent: "if 83='de', the W1 infinitive residual re-opens under red-team eyes; else the W1/W2 form-identity stands closed."

## Bar (verbatim, pre-registered before testing)

"name 83's value at @932 with zero ungranted assumptions; fence if undecidable"

Numbered pass/fail clauses (restated before testing, not modified after):

1. **C1:** 83='de' at @932 is tested under standing values. Pass iff the 'de' arm is excluded at kill grade (closing the gate) or confirmed (re-opening the residual).
2. **C2:** 83's actual value is named at @932 with zero ungranted assumptions; fence if undecidable.

Adverses listed: none.

## Method

1. Read BATTERY-PROTOCOL.md first. Created `code/crowd17/next-token/locks/de83-932-gate.lock` on start; deleted on completion. No stale lock was present.
2. Re-derived the repaired stream in-session. All @-offsets below are 0-based.
3. Standing premises used, not re-litigated: form-56-1627 PROMOTE (56 = 3sg finite at @932/@1626); 29='er', 40='e', 46='que', 11='la', 70='pre', 82='m', 34='i' (pencil GT); 87='ce', 64='qui', 96='par', 17='fois', 79='tout', 00='pour', 84='on', 47='ce' (promoted/granted); §7 (67 et/veut sole true polyvalence); le83-window NULL (83 fenced as blocker at @1217); frame-vient-parvenir KILL (source of the 83='de' lead); kill-grade on unconditioned 83='de' owned by fence-911-de.

## Window-level evidence

**W1 locus byte-confirmed:** 0b@931-932, row a5_10:
`[928]48 [929]82 [930]98 [931]83 [932]56 [933]69 [934]26 [935]00(pour)`
= "...[48] m' [98] [83] [56-fin] [69] [26] pour..."

**83 full census (n=15, byte-exact):**
@228 `87 46 98 83 82 96 21 60` | @614 `47 77 87 83 70 88 10 29` | @898 `82 14 98 83 86 16 92 67` | @907 `88 18 55 83 54 49 64 83` | @911 `54 49 64 83 59 37 96 09` | @931 `48 82 98 83 56 69 26 00` | @1061 `84 09 98 83 82 96 21 62` | @1161 `77 82 44 83 21 67 78 45` | @1171 `61 94 87 83 21 85 36 74` | @1217 `45 36 77 83 92 61 24 48` | @1334 `70 52 39 83 86 71 64 60` | @1612 `23 08 55 83 71 48 31 76` | @1784 `65 23 98 83 82 96 21 68` | @1829 `29 82 38 83 24 82 16 59` | @1840 `22 42 44 83 21 67 78 49`

Predecessors: 98 x5, 87 x2, 55 x2, 44 x2, 64/77/39/38 x1. Followers: 82 x3, 21 x3, 86 x2, 70/54/59/56/92/71/24 x1.

### C1: 83='de' at @932 — EXCLUDED at kill grade

1. form-56-1627 (battery PROMOTE, adopted) names 56 as 3sg finite at @932: the cipher's infinitive shape 56-29 never occurs (0/23), the cipher's 3pl shape always spells the ending (absent here), and the 8-gram `56 69 26 00 33 21 64 37` is byte-identical at @932 and @1626 where 46='que' forces a finite verb. One number in byte-identical contexts carries one form (§7).
2. At @932 the sequence is `[98] [83] [56-fin]`. If 83='de', the local reading is "de [finite verb]" ("de crée"). In 1841 French, 'de' does not govern a finite verb — "*de crée" is ungrammatical in every clause position. The 'de' + infinitive license that le83-window tested at the 98-83 windows is exactly what finite-56 removes.
3. Polyvalence cannot rescue it: §7 bars a second true polyvalence at battery grade, so 83 cannot be 'de' at @898 ("de [86-inf]" would parse) while being something else at @932.
4. Consistent with standing kills: frame-vient-parvenir KILL (source of the 'de' lead); le83-window NULL (fenced, not promoted); fence-911-de owns kill-grade on unconditioned 83='de'. This battery adds an independent kill-grade exclusion at @932.

**The W1 infinitive residual does NOT re-open. The gate is CLOSED. The W1/W2 form-identity stands.**

### C2: 83's actual value at @932 — FENCED (bar's else-arm)

Every value-naming route at @932 needs ≥1 ungranted assumption:

- Pronominal ('y', 'en'): "98 [y/en] [56-fin]" needs 98's value as the subject or host — 98's value is open (queued stem-08 adjacency only). Ungranted.
- Adverbial: "98 [adv] [56-fin]" needs 98's class/value. Ungranted.
- Nominal subject: "98 [83-noun] [56-fin]" needs 98 as a determiner. Ungranted.
- No class-level leg either: the full 15-window profile admits nominal (e.g. @1217 "le [83] [92-verb]"), pronominal (e.g. @911 "qui [83] est [37]"), and prepositional-adjacent readings, but each window's parse is hostage to an open neighbor (98, 44, 38, 39, 55, 61). Nothing forces one class with zero ungranted assumptions.

Fence cause (stated): value-naming is blocked on 98's value (the "98-83" x5 predecessor block) and on open neighbors at every other window; zero-assumption naming is untestable at battery grade. Not a kill — no window forces every value false.

## Per-clause verdict

- C1: **PASS** — 83≠'de' at @932 at kill grade; residual closed.
- C2: **FENCE executed** — 83's value undecidable with zero ungranted assumptions; stated cause above.

## Verdict: NULL (fence executed)

The gate's purpose is fulfilled (residual closed, form-identity stands), but the bar's literal demand — name 83's value — is not met at battery grade, so the value question stays fenced. No standing or red-team verdict is contradicted: consistent with le83-window NULL (blocker at @1217, separate window), frame-vient-parvenir KILL, fence-911-de's kill-grade ownership, and form-56-1627 PROMOTE (adopted as premise). §7 intact — no polyvalence declared. Canonical-stream caveat stands (row a5_10 offset unvalidated).

## Follow-ups proposed (all verified ABSENT from battery-queue.json)

1. `val-98-subject` (P3) — name 98's value/class. If 98 names as subject-shaped or verb-shaped, the "98 83 [56-fin]" frame at @932 re-opens for 83 value-naming with the host granted. Bar: 98's class named at battery grade with ≤1 stated assumption; fence if undecidable.
2. `adv-83-932` (P3) — test 83 as clause-adverb at @932 once 98's value is named (gated on val-98-subject). Bar: adverb parse of "98 [83] [56-fin]" with ≤1 ungranted assumption, or fence the adverb arm.
3. `nom-83-1217` (P3) — test 83 as nominal at the fenced @1217 window ("36 77 83" = "...le [83-noun] [92-verb]..."). Bar: nominal-83 parses with zero ungranted assumptions, or the le83-window fence is confirmed as terminal.

## Bookkeeping

- Queue: `de83-932-gate` → `status: verdict`, `result: null`, 2026-10-09 (pre-write assert passed — was queued/verdictless; temp-file + rename; JSON re-validated; own entry only; no downgrade).
- Lock `locks/de83-932-gate.lock` created on start, deleted on completion (verified gone).
- R5005, sealed gates, red-team adjudication queue untouched.
