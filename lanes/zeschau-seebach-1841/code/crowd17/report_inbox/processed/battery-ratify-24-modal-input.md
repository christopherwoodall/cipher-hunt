# Battery report: ratify-24-modal-input (RED-TEAM INPUT)

- Target id: `ratify-24-modal-input` (priority 2)
- Claim: RED-TEAM INPUT — consolidate the five legs depending on 24=modal plus the queue's own adverse, to adjudicate whether class-level R17-009 suffices to ratify modal-24. Evidence only, no adjudication.
- Evidence (queue): battery-inf-80-89-ratify.md NULL 2026-10-09, follow-up 3 (red-team input)
- Adverses (queue): RED-TEAM INPUT: red-team decision target - do not dispatch as a battery
- Date: 2026-10-09
- Worker: battery worker (subagent)

Terms (ASD-STE100): "leg" = one window supporting the frame. "load-bearing" = the derivation fails without it. "modal-shaped" = a finite verb taking bare verb-stem complements (like "pouvoir"). "red-team grade" = a decision in code/crowd17/report_inbox/processed/next-token-redteam-r17.md or next-token-redteam-r18.md. "battery grade" = a battery promote, below red-team grade.

## Bar (verbatim, pre-registered before testing)

"input package for the red team"

Numbered pass/fail clauses (restated before testing, not modified after):

1. **C1:** the five legs depending on 24=modal are consolidated with byte-exact evidence on the repaired stream.
2. **C2:** the queue's own adverse is stated verbatim and answered with what it implies for the adjudication.
3. **C3:** the package is delivered for red-team adjudication — evidence only, no value named, no adjudication performed here.

## Method

Read BATTERY-PROTOCOL.md first. Created `locks/ratify-24-modal-input.lock` on start; no stale lock present. Pre-write assert: queue entry was `queued` with no prior verdict — held.

The repaired stream was re-derived in-session from `data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json` per `code/side-keyhunt/repair_parse.py`: 1,847 pairs, 96 types. `canonical.py` never used. R5005, sealed gate instances, and the red-team adjudication queue untouched.

Source records: `code/crowd17/report_inbox/processed/battery-inf-80-89-ratify.md` (NULL, 2026-10-09), `code/crowd17/report_inbox/processed/battery-modal24-windows-no24.md` (PROMOTE, 2026-10-09), `code/crowd17/report_inbox/processed/battery-frames-80-89-indep.md` (NULL, 2026-10-08), the red-team adjudication records `next-token-redteam-r17.md` (R17-009, L105-111) and `next-token-redteam-r18.md` (R18-008, L104-110).

## C1 — the five legs, consolidated (all byte-verified in-session)

The legs were first derived by `frames-80-89-indep` (2026-10-08) under the battery-grade ne-24-profile "24=modal" (unratified), then re-derived by `modal24-windows-no24` (2026-10-09) under ONLY standing values (R17-009 class-level + A8 verb-frames). In-session byte verification on the repaired stream confirms every index and context:

| Leg | 24 index (0-based) | Locus context (24-3..24+2) | Row |
|---|---|---|---|
| 80 @564 | 564 | `67 11 43 | 24 80 97` | a3_02 |
| 80 @672 | 672 | `67 11 86 | 24 80 03` | a5_00 |
| 89 @221 | 221 | `29 42 16 | 24 89 61` | a2_01 |
| 89 @985 | 985 | `78 45 01 | 24 89 48` | a6_01 |
| 89 @1497 (weak) | 1497 | `66 15 59 | 24 89 41` | a7_10/11 |

Each leg's inference: 24 is a modal-shaped finite verb; a modal cannot govern a finite verb ("*il peut il vient" is ungrammatical every period); 80/89 sit in the infinitive slot under the A8 verb-frame grant. @985's 48-junction resolves right ("e[01]") on standing 48='e' (§7). @1497 keeps its weak grade under provisional 59='est' (untouched). Inherited residual (priced in by the parent): vouloir/savoir-shaped modals can also take nouns, so the legs are frame-grade, not deductive.

The key consolidation finding (from `modal24-windows-no24`): **the battery-grade "24=modal" label was load-bearing in name only.** R17-009 grants at red-team class level "24 = finite verb, modal-shaped" **with** "infinitive-taking complements (24->85 x5, 24->89 x3, 24->80 x2)". The distributional grounding — 24->85 x5 (A3 85=verb-stem) at @732 (a5_02), @955 (a6_00), @1438 (a7_08), @1693 (a8_06), @1754 (a8_08) — was re-derived byte-exact in-session and is **independent of 80/89 and of the dropped battery-grade label**. 24->89 x3 @221/@985/@1497 and 24->80 x2 @564/@672 confirmed byte-exact in-session. Every one of the five derivations consumes only the R17-009 license; dropping the unratified label changed zero inferences.

## C2 — the queue's own adverse, stated verbatim

From `inf-80-89-ratify`'s queue entry (2026-10-09), verbatim:

> "24=modal is battery-grade (ne-24-profile promote, unratified) — load-bearing for all five legs; A8's conditional grant untouched"

What the adverse implies for the adjudication, post `modal24-windows-no24`:

- The adverse's load-bearing claim is now **empirically false**: the five legs survive identically on R17-009 alone, so they were never load-bearing on the unratified label.
- The adverse's *trigger concern* (whether the unratified premise can carry a ratify-grade inference) therefore no longer applies to the legs themselves — but it does NOT by itself satisfy `inf-80-89-ratify`'s trigger clause, which names **ratification of the modal-24 premise** (red-team grade), not mere survival of the legs.
- R17-009 is a **class-level** grant ("finite verb, modal-shaped"; value unnamed: "peut"/"sait"/"doit" all open). The red team must decide whether class-level sufficiency is what "ratified" means here. R18-008 (24="faire" REJECTED; survivor set {faire, laisser} open; 24="faire" lead-grade only) constrains the value side; the modal-class side is what is live.
- Blocking counter-evidence that remains even if modal-24 is ratified (from `frames-80-89-indep`, untouched): @1155 (80=determiner, "pour [92]er [80] fois") and @1376 (89=noun/adverb) block 80/89 **frame independence**; those live in the queued `det-adj-80-adjudicate` / `noun-89-1377-adjudicate` venues. Ratifying modal-24 does not resolve those.

## C3 — package delivered

All numbered clauses pass. This is an evidence package only: no cipher value is named, no class/value is adjudicated, no standing or red-team verdict is contradicted or downgraded (R17-009, R18-008, A8, A3, A9, §7 intact; no polyvalence declared; `inf-80-89-ratify`'s NULL verdict stands and is not re-opened here). §7 intact. Canonical-stream caveat stands (68/70 row offsets unvalidated). Verdict for this packaging target: **PROMOTE** (input package delivered).

## For the red team

The adjudication question in its sharpest form: **does class-level R17-009 suffice to ratify the modal-24 premise, or does "ratified" demand a named value or a fresh round's act?** The legs no longer need the answer — they stand on R17-009 regardless — but `inf-80-89-ratify-rerun-gated`'s trigger (gated on ratification) and `inf-80-89-ratify`'s C1 remain the queue's official gatekeepers.

## Bookkeeping

- Queue: `ratify-24-modal-input` → status `verdict`, result `promote`, 2026-10-09 (pre-write assert passed — was `queued`/verdictless; temp-file + rename; JSON re-validated post-write; own entry only; no downgrade).
- Lock `locks/ratify-24-modal-input.lock`: created on start (no stale lock existed), deleted on completion (verified gone).
- R5005, sealed gate instances, red-team adjudication queue untouched.
