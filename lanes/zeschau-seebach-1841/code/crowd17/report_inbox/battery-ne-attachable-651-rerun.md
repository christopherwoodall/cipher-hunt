# Battery `ne-attachable-651-rerun` — verdict: NULL (fence executed)

## Bar tested (verbatim, pre-registered)

`once 76/49's roles are named.`

Numbered clauses (per §2, fixed before testing):

- **C1** — 76's role is named → PASS / FAIL
- **C2** — 49's role is named → PASS / FAIL
- **C3** — if the dependency is unmet, fence the re-test with stated cause (per the dispatch note: "Workers must evaluate the dependency in the bar and fence if unmet.")

## Method

Re-derived the repaired 1,847-pair / 96-type stream in-session via `code/side-keyhunt/repair_parse.py` (`load_rows` + `parse` with `code/side-keyhunt/repaired_offsets.json`); parsed 1,847 pairs — asserts hold. `canonical.py` never used. Checked 76/49 role status against `code/table-grid/table-registry.json` (single source of truth) and the latest red-team round report `code/crowd17/report_inbox/processed/next-token-redteam-r20.md` (Round 20).

## Findings

### Locus byte-confirmed (0-based)

`@651=94 @652=76 @653=49 @654=24 @655=26 @656=30` (row a4_02) = "ne [76] [49] [24-verb] [26] [30-pas]" — matches the queue evidence's "ne 76 49 24 26 pas".

### C1 — 76's role named → PASS

Registry: `76 -> ["noun", "prom"]`. 76's noun-class role is red-team promoted and registered. The queue evidence's "(noun-class PROMOTED … ungrammatical)" premise holds.

### C2 — 49's role named → FAIL

- **Registry: no 49 entry at all** (`cells.get('49')` → None; no `"49"` key in `table-registry.json`). 49 is unvalued.
- **Latest red-team word (R20-049, FENCE):** "49's class is still open; … If 49's class ever resolves to something licensable, re-run the license with a new census for the actual geometry." Surviving classes are adverb (strained) and noun (strained); verb, determiner, and relative/interrogative pronoun are kill-grade dead; adjective-49 was killed at kill grade by adj-49-420-366.
- The two battery-level 49 class verdicts (`noun-49-nonchain` PROMOTE, `adv-49-653-990` PROMOTE) are unratified — the registry carries neither, and per §7/pipeline convention a battery promote is not "named" until the red team ratifies it. R20-049 explicitly supersedes them as "still open."

### C3 — dependency unmet → FIRES

The re-test's own precondition ("once 76/49's roles are named") is half-met. 76 is named; 49 is not. **The re-test is fenced, not run.** This is not a re-litigation of @651's attachability — it is the bar's own gate refusing to fire.

## Scope

Fences only this re-test's execution. Untouched: 76's promoted noun class, the R20-049 49 fence, battery-pas-30's PROMOTE, the unratified 49 battery promotes, 94='ne' strong lead, 24/26/30 values, §7. No standing or red-team verdict contradicted, downgraded, or re-litigated. Canonical-stream caveat stands (row a4_02 offsets unvalidated).

Noted but out of scope: R20-049's fence record (b) — the @651–656 "ne"+N conflict between battery-pas-30's PROMOTE (counted "ne 76 49 24 26 pas" as a valid 'ne…pas' frame) and the 49 fence — is flagged as a dedicated open question in follow-up 2.

## Follow-ups (all verified ABSENT from battery-queue.json)

1. **`ne-attachable-651-rearm`** (P4, gated) — re-arm this exact re-test once 49's role is red-team ratified (registry carries a 49 entry). Precondition is explicit; do not dispatch until the registry entry exists.
2. **`ne-651-pas30-conflict`** (P4) — dedicated target for R20-049 fence record (b): adjudicate the "ne 76 49 24 26 pas" @651–656 conflict between battery-pas-30's PROMOTE and the 49 fence; decide which frame parses @651–656 correctly.
3. **`noun49-adv49-adjudicate`** (P4, red-team venue note) — adjudicate between the two unratified battery-level 49 class verdicts (noun-49-nonchain PROMOTE vs adv-49-653-990 PROMOTE); battery venue only — feeds the red-team 49 docket.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-ne-attachable-651-rerun.md`
- Queue: `ne-attachable-651-rerun` → `status: verdict`, `result: null`, 2026-10-09 (pre-write assert passed — was queued/verdictless; target-id-unique tmp `battery-queue.json.ne-attachable-651-rerun.tmp` + atomic rename; disk re-validated; own entry only; no downgrade; no tmp leftover)
- Lock created on start (agent f8b6df75-a746-45a7-b719-f7afa5bd49be, no stale lock), deleted on completion (verified gone).
- R5005, sealed gates, red-team adjudication queue untouched.
