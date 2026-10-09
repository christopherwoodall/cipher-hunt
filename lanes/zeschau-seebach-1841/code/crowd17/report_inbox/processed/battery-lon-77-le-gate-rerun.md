# Battery report: lon-77-le-gate-rerun

- Target id: `lon-77-le-gate-rerun`
- Claim: "re-fire the @508 discriminator bar the moment the red team adjudicates 77='le'"
- Date: 2026-10-09
- Worker: battery worker (subagent 50868c72-66e9-4314-aa5c-87b2c913e78c)
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py`; asserts 1847/96 held in-session). `canonical.py` never used. R5005, sealed gate instances, red-team adjudication queue untouched.

Terms (ASD-STE100): "gate" = a target that fires only on a named trigger condition. "FENCE" = the red-team ruling that keeps an item live but unresolved. "provisional" = a value held at working grade, not promoted.

## Bar (verbatim, pre-registered before testing)

"sole trigger: the red-team 77 ruling (provisional->promoted merge or overturn to a named value); record dissolution of both @508 readings iff 77 resolves non-'le'"

Numbered pass/fail clauses (restated before testing, not modified after):

1. **C1 (trigger):** the red team has ruled on 77's value as a provisional→promoted merge OR as an overturn to a named non-'le' value.
2. **C2 (action):** given C1 fired, record dissolution of both @508 readings iff 77 resolved non-'le' (no forcing).
3. The bar fires only on C1. If 77's value is still provisional, the re-test is not actionable — record the trigger as absent (per the parent battery `lon-77-le-gate`, 2026-10-09, §"Bar restated as numbered clauses" C3).

## Method

1. Read BATTERY-PROTOCOL.md first. Created `code/crowd17/next-token/locks/lon-77-le-gate-rerun.lock` on start (agent id + 2026-10-09T18:45:12Z); no prior/stale lock.
2. Re-derived the repaired stream byte-exact in-session (1,847 pairs / 96 types asserted).
3. Checked the gate trigger against the latest red-team round (R20, `code/crowd17/report_inbox/processed/next-token-redteam-r20.md`) — not against battery verdicts alone, per the lane's GATE-TRIGGER RULE.
4. Re-verified the @508 discriminator window byte-exact on the stream (parent's E1 adopted and confirmed, not re-litigated).

## Window-level evidence

**E1 — Gate check against the red-team record (R20, controlling round).**

- **R20-130: ceci-77-redteam — FENCE.** "The le/ci split is NOT declared." Ruling: `77=["le","prov"]`. Registry: none.
- **R20-131: le-77-residual-adjudicate — FENCE.** "77='le' provisional SURVIVES; the three 'ce'+77 windows (@515/@611/@869) stay fenced as residuals." "Neither merge nor split is declared now." Merge condition: the queued 80/89-verb battery (F104 docket linkage). Split condition: kill-grade "ci" evidence per R20-130. Ruling: `77=["le","prov"]`. Registry: none.

Both rulings are FENCE with the provisional surviving. Neither is a provisional→promoted merge; neither is an overturn to a named value.

**E2 — Discriminator window (byte-exact, re-derived).** 0-based @505–513, row a3_00: `21 67 77 62 94 64 98 65 88` = "[21-noun] et le [62][94] qui vient [65-noun] [88]". The 77-slot is @507; 62-94 at @508–509. Byte-identical to the parent battery's E1. The two readings of 62-94 — (a) two-word "il ne", (b) one-word "[noun]ne" ("trône", syllabic 94) — remain live only inside the "et le ___ qui vient" frame the provisional 77-slot builds. Adopted from the parent battery; not re-litigated (the re-test is not actionable).

## Per-clause pass/fail

1. **C1 (trigger): FAIL — not met.** The task brief asserted "Gate satisfied: red team adjudicated 77='le' at R20-130/131 (FENCE, provisional survives)." The rulings exist and are FENCE — verified verbatim above. But the bar's trigger is "(provisional->promoted merge or overturn to a named value)". A FENCE with the provisional surviving is neither a merge nor an overturn. The red team explicitly states "Neither merge nor split is declared now." 77's value is still provisional.
2. **C2 (dissolution recording): INAPPLICABLE.** The trigger (C1) has not fired; per the bar's own gating and the parent battery's C3, the re-test is not actionable. (77 also did not resolve non-'le', so no dissolution is recordable in any case.)
3. **Trigger recorded absent.** Not falsified — the gate is a live re-arm, not a dead target.

Adverses: none listed on the target. No standing or red-team verdict contradicted, downgraded, or re-litigated; §7 intact. Sibling gates with the same trigger (`inf89-rerun-77gate`, `77-ratify-noun86-gate`) remain queued — consistent with this verdict.

## Verdict: NULL

The @508 discriminator re-test cannot fire because its sole trigger — a red-team 77 ruling declaring provisional→promoted merge or overturn to a named value — has not occurred. R20-130/131 adjudicated 77='le' as FENCE with the provisional surviving. The gate stays armed.

Note for the supervisor: the dispatch brief's "Gate satisfied" line was checked against the red-team record and does not meet the bar as written (GATE-TRIGGER RULE). This is a triage-level overread of the same class documented in AGENTS.md — a red-team FENCE is not a merge or overturn.

## Scope (stated, not hidden)

- Gate-level verdict only. Both @508 readings survive unchanged under provisional 77='le' — nothing about 62-94's two readings is decided here.
- The re-test remains gated on the R20-131 merge condition (queued 80/89-verb battery) or the R20-130 split condition (kill-grade "ci" evidence).
- `f104-77-merge-input` (verdict/promote) and `le-77-residual-adjudicate` (queued) are not re-proposed.
- Canonical-stream caveat stands (row a3_00 offset unvalidated, 68/70).

## Follow-ups proposed (for supervisor queuing; both ids verified ABSENT from battery-queue.json)

1. `lon-77-le-gate-rerun-2` (P2) — third re-fire of this exact bar; fires ONLY on a red-team 77 ruling that declares provisional→promoted merge or overturn to a named value (per R20-131's merge condition or R20-130's split condition).
2. `ci-77-split-evidence-watch` (P4) — watch for kill-grade "ci" evidence at the three "ce"+77 contacts (@515/@611/@869); the split declaration is the non-'le' arm that would dissolve both @508 readings.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-lon-77-le-gate-rerun.md` (this file).
- Queue: `lon-77-le-gate-rerun` queued → `verdict`/`null`, 2026-10-09 (pre-write assert passed — was queued/verdictless; temp-file + rename; JSON re-validated; own entry only; no downgrade).
- Lock `code/crowd17/next-token/locks/lon-77-le-gate-rerun.lock` created on start, deleted on completion (verified gone).
- R5005, sealed gate instances, red-team adjudication queue untouched.
