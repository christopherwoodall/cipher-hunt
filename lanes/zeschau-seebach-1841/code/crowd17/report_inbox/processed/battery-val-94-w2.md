# Battery report: val-94-w2

- Target id: `val-94-w2`
- Claim: test 94=non-'ne' value at the @1167 hapax window ('94-87')
- Date: 2026-10-09
- Worker: battery worker (subagent ef5bb459-dca5-4b73-b4d6-8364522f8592)
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py`; asserts 1847/96 held in-session). `canonical.py` never used. R5005, sealed gates, red-team adjudication queue untouched.

Terms (ASD-STE100): "joined '55-61-94'" = the three groups read as one word, 94 contributing the word-final material. "Deviation" = any reading where 94 is not 'ne' at this window.

## Bar (verbatim, pre-registered before testing)

"name 94's value iff one non-'ne' value parses the @1167 window with the joined '55-61-94' and stated cause for the deviation from 94='ne'"

Numbered pass/fail clauses (restated before testing, not modified after):

1. **C1:** One non-'ne' value V for 94 parses the @1167 window under the joined '55-61-94' word reading → name V.
2. **C2:** A stated cause for the deviation from 94='ne' exists ('ne' fails to parse the window even in the joined reading).
3. **C3 (adverse):** Naming must not declare a second 94 value at battery level — 94='ne' is STRONG LEAD (R17-001); a second value is §7 territory (red-team venue: `redteam-94-functional-split`, queued P1).

Adverses (from queue): 94='ne' is battery-promoted (pending ratification); deviation needs red-team tolerance.

## Method

1. Read BATTERY-PROTOCOL.md first. Created `code/crowd17/next-token/locks/val-94-w2.lock` on start (agent id + 2026-10-09T18:26:36Z); no prior/stale lock; deleted on completion.
2. Re-derived the repaired stream byte-exact in-session (1,847 pairs / 96 types asserted).
3. Adopted (not re-litigated): `ne-ce-1169` NULL (2026-10-08), `w2-5561-nece-frame` KILL (2026-10-09), `seg-55-61-94-word` NULL (2026-10-09), `seg-61-pren-polyvalence` KILL (2026-10-09), `nece-94-87-initial` KILL, R17-018 fenced 12/94 duality.
4. Standing values used: 87='ce' granted (A4); 45='ce' (A11 hold); 21 noun class; 67 et/veut sole polyvalence; 94='ne' STRONG LEAD. 1841 diplomatic French throughout.

## Window-level evidence (re-derived)

Target window, 0-based @1167–1172, row a6_09:

```
@1163:67 @1164:78 @1165:45 @1166:13 | @1167:55 @1168:61 @1169:94 @1170:87 | @1171:83 @1172:21
```

- "94 87" occurs exactly **1x stream-wide** (@1169–1170; re-verified 1/1847).
- The triple "55 61 94" occurs exactly **2x**: @576–578 (row a3_02, follower 82) and @1167–1169 (row a6_09, follower 87).

### Non-'ne' candidate inventory (exhaustive against the lane record)

1. **94 = 'n' (letter).** No joined-word parse is demonstrable: 55 and 61 are both unvalued, so no French word of shape [55][61]'n' can be exhibited; a "repren"-shaped word is not French. The 61-"pren" anchor this fork would need was KILLED today (`seg-61-pren-polyvalence`: 61="pren" impossible as a global value — @1556 "prene" and @367 "prenpre" unreadable with banked neighbors). No independent leg.
2. **94-87 word-initial ("néce…" shape).** KILLED (`nece-94-87-initial`). Out.
3. **Any other non-'ne' syllable.** No lane record exists; with 55/61 unvalued no candidate is demonstrable. Out.

**C1: FAIL** — no non-'ne' value parses the window under the joined reading at battery grade. (Vacuous "any V fits unvalued 55/61" is speculation, not a demonstration; the lane's naming standard is ≥2 independent legs.)

### Deviation-cause test

- The keep-'ne' fork is alive: 94='ne' as word-final syllable of the joined word is grant-compatible (R17-018 12/94 duality; fenced 70-12-94 "prenne" precedent). `seg-55-61-94-word` found "…prenne ce…" grammatical conditional on 55/61 values.
- The 61="pren" kill removes the "reprenne"-family *content* of that fork but does not rule out 94='ne' as the word-final syllable of an undemonstrated word.
- The two-word "ne ce" reading is ungrammatical (adopted from `ne-ce-1169` / `w2-5561-nece-frame`), but that is not the joined reading the bar tests.

**C2: FAIL** — 'ne' is not ruled out at this window, so no cause for deviation can be stated.

**C3: PASS (vacuous)** — no value is named, so no §7 declaration is made. Recorded for the record: naming any non-'ne' 94 would be a second 94 value and belongs to the red team (`redteam-94-functional-split`), not to a battery worker.

## Verdict: NULL

The iff fails on both arms: no non-'ne' value is demonstrated (C1), and no deviation cause exists because the keep-'ne' syllabic fork is unforsfalsified (C2). The non-'ne' fork is undemonstrated, not disproven — the window's ultimate cause stays with the fenced "ne ce" residual (`w2-5561-nece-frame`) and the red-team split docket. No standing or red-team verdict contradicted, downgraded, or re-litigated; 94='ne' STRONG LEAD intact; §7 intact.

## Follow-ups proposed (all verified ABSENT from battery-queue.json on 2026-10-09)

1. `redteam-94-split-input` (P2, gather-only) — package this null's negative result plus the 61="pren" kill's consequence for the 55-61-94 family as ruling-ready input to `redteam-94-functional-split`. (`poly-94-r17018-input` covers only the [42ne]/[62ne] family; the formula family is distinct.) No battery-level duality declaration.
2. `val-94-576-nem` (P3) — test the formula's other window @576–580 ("94 82 06" as "ne m'ent…" elision frame): does 'ne' parse there? Decides whether any deviation cause is window-specific to @1167.
3. `nece-1169-revisit` (P3) — re-test `ne-ce-1169`'s rescue inventory now that 61="pren" is killed; its "two grant-compatible rescues" were predicated on the live word-unit fork.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-val-94-w2.md` (this file).
- Queue: `val-94-w2` queued → `verdict`/`null`, 2026-10-09 (pre-write assert passed — was queued/verdictless; temp-file + rename; JSON re-validated; own entry only; no downgrade).
- Lock `code/crowd17/next-token/locks/val-94-w2.lock` created on start, deleted on completion (verified gone).
- R5005, sealed gate instances, red-team adjudication queue untouched.
