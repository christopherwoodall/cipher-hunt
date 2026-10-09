# Battery report: bound-1132-modal-edge

- Target id: `bound-1132-modal-edge`
- Claim: "test whether 24's value at @1132 fixes the modal clause's right edge."
- Bars (verbatim, from battery-queue.json): "if the modal clause demonstrably ends at 86 (@1134), re-run the boundary-adverb test with the right edge fixed; else fence with stated cause."
- Date: 2026-10-09
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py`). Asserts held: 1,847 pairs, 96 types. `canonical.py` never used. R5005, sealed gate instances, red-team queue untouched.
- Lock: `code/crowd17/next-token/locks/bound-1132-modal-edge.lock` created 2026-10-09T13:02Z on start; no stale lock existed; deleted on completion.

Terms (ASD-STE100): "modal clause" = a clause built around a modal verb governing an infinitive ("veut le laisser"). "Right edge" = the position where the clause demonstrably ends. "Battery grade" = forced with zero ungranted assumptions.

Numbered pass/fail clauses (pre-registered before testing, not modified after):

1. **C1 (gate):** 24's value at @1132 is named at battery grade, so it can fix the modal clause's right edge.
2. **C2 (re-test):** iff the modal clause demonstrably ends at 86 (@1134), re-run the @1135 boundary-adverb test with the right edge fixed (boundary can only fall before 20).
3. **C3 (else-arm):** if C1/C2 do not fire, fence with stated cause.

Adverses listed: none.

## Method

1. Read BATTERY-PROTOCOL.md first. Created the lock on start; deleted on completion.
2. Re-derived the repaired stream byte-exact. All @-offsets below are 0-based.
3. Adopted, never re-litigated: `infclass-86` PROMOTE (86 = INF-class, A9); R17-009 (24 = finite/modal verb class); R19/R24 (24="en" iff follower is 85 — five windows; elsewhere finite/modal verb; the old {faire, laisser} value route dead globally); 77="le" (provisional); 62="il" (promoted); `adv-20-1135-parse` NULL (2026-10-09, the parent battery that queued this target); §7 (67 sole polyvalence).

## Window-level evidence

The locus — @1128–1142 (rows a6_07/a6_08, byte-confirmed):

`@1128=86 @1129=52 @1130=37 @1131=86 @1132=24 @1133=77 @1134=86 |@1135=20| @1136=62 @1137=98 @1138=00`

The focal geometry: `…[86-inf] [24-fin/mod] le [86-inf] |20| il vient pour…`

### C1 — FAIL (gate does not fire)

24's value at @1132 is **unnamed**:

- R24 names only the class at this window: @1133=77 (≠85), so 24@1132 is finite/modal **class**, not "en", and the global {faire, laisser} value route is dead. No spelling value has been named for 24 at any window at battery grade or above.
- Queue audit: the only value-bearing 24 targets are `24-en-verb-conflict` (null), `24-nine-left-envelope` (promote — distributional, names no value), and `24-redteam-adjudication` (queued, RED-TEAM DECISION — red-team venue, not battery work).
- The claim's own evidence concedes this: "@1132=24 carries R17-009 finite/modal class; naming its value **would** fix the modal clause's right edge" — naming has not happened.

C1 fails, so the re-test cannot fire on the gate as written.

### C2 — does not fire (and would fail even with a named value)

Even hypothetically naming 24's value does not fix a right edge at 86, for two byte-grounded reasons:

1. **The geometry binds 86 INTO the clause, not out of it.** `[24-fin/mod] le [86-inf]` composes as modal + clitic pronoun + governed infinitive ("veut le laisser"-shaped) on standing values alone, zero new assumptions — adopted verbatim from `adv-20-1135-parse` C2 finding 2. A governed infinitive continues its clause; it does not terminate one. A modal clause can host a clause-final adverb after the infinitive ("veut le laisser ainsi"-shaped). So 20 remains licensable **inside** the modal clause as a clause-final adverb — the surviving rival the boundary-adverb must beat, already queued as `adv-1135-leftward`.
2. **Naming 24's value changes nothing about the right edge.** The clause-final-adverb reading ("…le [86-inf] [20-adv]") stays grammatical under every licensed candidate 24 value (vouloir, pouvoir, devoir, venir de — all take bare infinitive complements and admit clause-final adverbs). The re-test's premise — "the boundary can only fall before 20" — is therefore **not demonstrable** from a named 24 alone; it would need a licensed left-edge frame or a red-team class ruling on 20.

### C3 — FIRES: fence with stated cause

Stated cause: the gate fails — 24's value at @1132 is unnamed (R24 grants class only; the value naming sits in queued red-team venue `24-redteam-adjudication`); and even a named value would not fix the right edge, because modal + clitic + governed infinitive binds 86 into the clause and 20 remains licensable as a clause-final adverb ("…le laisser ainsi"-shaped). The fence stands until either (a) 24's value is named at battery grade or above, AND (b) a licensed mechanism forces 20 outside the modal clause.

Not kill grade: naming 24's value could still materially change the analysis (a value without a governed-infinitive government, e.g. a plain finite reading, would break the "binds into the clause" arm — though it would then face the ungrammaticality of "[24-fin] le [86-inf]").

## Adverses

None listed.

## Verdict: NULL (fence executed)

No standing or red-team verdict contradicted or downgraded: `infclass-86` PROMOTE adopted as gate premise; R17-009, R24, `adv-20-1135-parse` NULL, `poly-20-docket` untouched; §7 intact (no polyvalence declared). Canonical-stream caveat stands (rows a6_07/a6_08 offsets unvalidated).

## Follow-ups proposed (all verified ABSENT from battery-queue.json)

1. `val-24-1132-name` (P3) — name 24's value at @1132 with battery-grade evidence; its promote fires this target's C1.
2. `bound-1132-modal-edge-rerun` (P4) — gated re-fire of this target once 24's value is named (battery grade or red-team ruling), to re-test the @1135 boundary-adverb with the right edge re-examined.
3. `modal-clausefinal-adv-corpus` (P4) — corpus check: does "modal + clitic + governed infinitive + adverb" occur in 1841 prose as a closed modal clause? Confirmed zero hardens the clause-final-adverb rival at @1135; ≥1 genuine attestation licenses it.

Notes on scope: `adv-1135-leftward` (clause-final-adverb rival at window level) is already queued by the parent battery — not re-proposed. `noun20-1135-gated` (noun rival, red-team gated) likewise present.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-bound-1132-modal-edge.md` (this file).
- Queue: `bound-1132-modal-edge` queued → verdict/null, 2026-10-09 (pre-write assert passed — was queued/verdictless; temp-file + rename; JSON re-validated; own entry only; no downgrade).
- Lock `locks/bound-1132-modal-edge.lock`: created on start (no stale lock), deleted on completion (verified gone).
- R5005, sealed gate instances, red-team adjudication queue untouched.
