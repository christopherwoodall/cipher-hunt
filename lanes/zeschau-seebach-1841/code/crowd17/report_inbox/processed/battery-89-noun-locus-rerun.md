# Battery report: 89-noun-locus-rerun

- Target id: `89-noun-locus-rerun`
- Claim: "Re-test Arm A iff 77's value ever resolves non-'le' or 77='le' promotes; kill the noun arm iff 'le [89]e' fails under the new value."
- Date: 2026-10-09
- Worker: battery worker
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py`). Verified in-session: 1,847 pairs, 96 types. `canonical.py` never used. R5005, sealed gates, red-team queue untouched.
- Offset note: all @-offsets below are 0-based (queue convention).

Terms (ASD-STE100): "Arm A" = the noun arm of 89 ("le [89]e", determiner + noun with -e ending, conditional on provisional 77='le'). "Arm B" = the infinitive arm of 89 (modal + infinitive under R17-009's 24 class grant). "provisional" = an adopted value not yet promoted or ratified. "fence" = stop at battery grade with the cause stated; the question stays open.

## Bar (verbatim from battery-queue.json)

"conditioned re-test"

Restated before testing as numbered pass/fail clauses (not modified after):

1. **C1:** The trigger condition has fired since the parent Arm A battery — 77's value has resolved (a non-'le' value named at battery grade, or 77='le' promoted/ratified past provisional).
2. **C2** (conditional on C1): re-test Arm A loci (@640, @871) under the resolved 77 value; promote iff the re-test parses.
3. **C3** (conditional on C1): kill the noun arm iff 'le [89]e' fails under the resolved value.
4. **C4:** If C1 does not fire, the conditioned re-test does not fire; fence the target as-is with the trigger unmet (per the bar's conditional design; no re-litigation of Arm A).

Adverses listed: 77's value open (le-77 null); marginal value, likely stands/fences as-is.

## Method

1. Read BATTERY-PROTOCOL.md first. Created `locks/89-noun-locus-rerun.lock` on start; deleted on completion. No stale lock was present.
2. Re-derived the repaired stream byte-exact in-session. All asserts held.
3. Audit trail for C1: scanned `battery-queue.json` for every target touching 77 (24 targets) and every verdict dated after the parent Arm A battery, plus protocol §7's standing list. The trigger question is "has 77's value resolved" — that is decided by verdicts and standing, not by re-running the loci.
4. Byte-grounded the parent loci (0-based, row-validated) so the report stands on the repaired stream.

## Window-level evidence (parent loci, byte-exact)

- **@640 (row a4_01):** `…46 60 67 [77] [89] [48] 20…` — 89 sits between 77 and 48: the "le [89]e" shape ("[77] [89]e" = determiner + noun with -e ending), conditional on provisional 77='le'.
- **@871 (row a5_07):** `…86 70 87 [77] [89] [48] 20…` — same shape, second locus.
- **"77 89 48" trigram:** exactly **2x** stream-wide (89 at 0b@640 and 0b@871). Both parent loci are the full trigram population; zero repetition leverage beyond them.
- Arm B loci (byte-confirmed for context): **@222 (row a2_01)** `…42 16 [24] [89] 61 96…` = modal 24 + infinitive 89; **@986 (row a6_01)** `…45 01 [24] [89] [48] 01 76…` = "[89]e" word-internal -re-shaped infinitive. Both hold under standing R17-009 and are unaffected by 77's status.

## Per-clause pass/fail

- **C1 — FAIL (trigger not fired).** 77's value is unresolved today:
  - `le-77` → **null** (2026-10-07): 77='le' neither promoted nor rejected; no non-'le' value named.
  - Protocol §7 standing: 77='le' remains **provisional** (not promoted).
  - Red-team 77 adjudication items all still queued, none decided: `le-77-residual-adjudicate` (RED-TEAM DECISION), `ceci-77-redteam`, `lon-77-le-gate-rerun`, `77-ratify-noun86-gate` (fires once provisional 77='le' ratifies — the ratification has not happened).
  - Later 77-adjacent verdicts that touch but do not resolve 77's value: `elision-77-84` PROMOTE (77='le' elision leg — supports the provisional reading, does not promote it); `seg-77-62-singleton` PROMOTE (singleton resolution, names no value); `frame-qui-77-84` PROMOTE (frame re-valued, names no value); `head-77-62-94-noun` NULL; `lever-77-78` NULL; `lon-ne-77-62-94` NULL; `clitic-86-77-windows` KILL (kills 86-as-clitic, says nothing about 77's value); `celle-7780-fusion-515-869` KILL (kills the 87-77 fusion reading, leaves 77's value open).
  - No battery named any value for 77; no promote of 77='le'; no non-'le' resolution anywhere in the lane.
- **C2 — MOOT.** The re-test is conditional on C1 by the bar's own design.
- **C3 — MOOT.** The noun-arm kill is conditional on C1.
- **C4 — FIRES.** The conditioned re-test does not fire. Fence with stated cause: the trigger (77's value resolving) has not fired since the parent battery, exactly the outcome the adverse expected ("marginal value, likely stands/fences as-is").

## Verdict: NULL (fence executed)

The bar is a conditioned trigger, and the condition is false: 77='le' is still provisional (protocol §7), `le-77` is null, and all four red-team 77-adjudication items remain queued. The parent Arm A evidence (@640/@871, "77 89 48" 2x) is re-verified byte-exact on the repaired stream but is not re-litigated — the re-test is armed, not run. No standing/red-team verdict contradicted or downgraded; §7 intact (67 et/veut sole polyvalence untouched); canonical-stream caveat stands (rows a4_01/a5_07/a2_01/a6_01 unvalidated).

## Follow-ups proposed (all verified ABSENT from battery-queue.json)

1. `89-noun-locus-rearm` (P4) — gated re-fire of this bar's C2/C3 once the red team adjudicates 77 (`le-77-residual-adjudicate` / `ceci-77-redteam` / `77-ratify-noun86-gate`). Bar: re-test @640/@871 under the adjudicated 77 value; kill the noun arm iff 'le [89]e' fails under it. This is the trigger's re-arm, not a duplicate of the @508-focused `lon-77-le-gate-rerun`.
2. `inf-89-222-value` (P3) — name 89's infinitive value at @222 (`42 16 24 89 61`, row a2_01, byte-exact): 24=modal (R17-009) + infinitive 89 under standing values, independent of the 77 gate; Arm B's value is the unblocked half of the conditioned two-way split. Bar: one value for 89 parsing @222 with ≤1 ungranted assumption; kill the infinitive-value route iff no value does.

## Bookkeeping

- Queue: `89-noun-locus-rerun` → `status: verdict`, `result: null`, 2026-10-09 (pre-write assert passed — was queued/verdictless; temp-file + rename; JSON re-validated post-write; own entry only; 1,164 targets total; no downgrade).
- Lock `locks/89-noun-locus-rerun.lock` created on start, deleted on completion (verified gone).
