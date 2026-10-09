# Battery report: cela-1117-frame-resume

- Target id: `cela-1117-frame-resume` (priority 1)
- Claim: Fire the pre-computed conditional branches of cela-1117-frame when the red team adjudicates battery-cela-69-11-word.
- Worker: battery worker (subagent e1482451-ba94-4cb9-af6f-a57f89117b4d)
- Date: 2026-10-09
- Stream: repaired 1,847-pair / 96-type parse (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`). `canonical.py` never used. R5005, sealed gates, red-team adjudication queue untouched. No invented numbers.

## Bar (verbatim, pre-registered)

"locate the red-team ruling in a processed adjudication doc; branch A (ratified): record noun-88-det's bar moot and shrink 88's determiner window set to {@402}; branch B (rejected): re-test noun-88-det clauses 2-4 carrying clause 3's gender clash as structural; the only new byte work permitted is citing the ruling"

Numbered pass/fail clauses (restated before testing, not modified after):

1. **C1:** Locate the red-team ruling on battery-cela-69-11-word in a processed adjudication doc → PASS iff an R19+ ruling exists with a ratify/reject disposition.
2. **C2 (branch A):** IF the ruling ratified, record noun-88-det's bar moot → PASS iff branch A fires with the pre-computed entailment.
3. **C3 (branch A):** IF the ruling ratified, shrink 88's determiner window set to {@402} → PASS iff recorded.
4. **C4 (branch B, alternate):** IF the ruling rejected, re-test noun-88-det clauses 2–4 with clause 3's gender clash carried as structural.
5. **C5 (adverse):** The only new byte work permitted is citing the ruling — no re-run of the 'cela' value test, no red-team queue edits.

## Method

1. Read BATTERY-PROTOCOL.md first. Created `code/crowd17/next-token/locks/cela-1117-frame-resume.lock` on start (agent id + 2026-10-09T18:45:00Z); no prior/stale lock; deleted on completion.
2. Read the parent battery `code/crowd17/report_inbox/processed/battery-cela-1117-frame.md` in full; adopted its pre-computed branches (§4), its window evidence (W1–W5, §3), and its locus fences. Adopted, never re-litigated.
3. Searched the processed adjudication docs for a ruling on `cela-69-11-word`: hit in `code/crowd17/report_inbox/processed/next-token-redteam-r19.md` (R19-108) and a standing-status confirmation in `code/crowd17/report_inbox/processed/next-token-redteam-r20.md` (R20-135).
4. Per C5 and the adverses ("do not re-run the 'cela' value test; the red-team ruling is the sole trigger; never touch the red-team adjudication queue"), no stream bytes were re-derived beyond the parent battery's adopted evidence; the ruling citations below are the only new evidence.

## Findings

**Ruling located (C1).** `next-token-redteam-r19.md` line 695:

> ### R19-108: cela-69-11-word — GRANT (locus-level finding)
> 69's global value stays open — homophony needs red-team authority. Registry: none.

R19-145 in the same doc deferred *this* resume target because the trigger was unfired at that round; that deferral was the trigger itself, not a ruling on the cela value. The R19-108 GRANT is the disposition this bar asks for.

**Ruling standing (per the bar's own gate text).** R20-135 (`next-token-redteam-r20.md`, "split-69-adjudicate — FENCE") re-derives @1115 as "38 30 69 11 88" and states:

> "the cela locus parse (R19-108, GRANT locus-level: '69 11'='cela' @1115-1116, clause boundary before 88) is the standing disposition, and the modal-inf reading ... has not displaced it."

The R19-108 GRANT is therefore ratified and standing at R20. **Branch A fires.** Branch B is moot (no rejection occurred); C4 untriggered.

**Branch A entailment (C2/C3), adopted from the parent battery §4 clause 2.** The parent battery byte-verified @1115=('69','a6_07'), @1116=('11','a6_07'), @1117=('88','a6_07'); under the ratified cela reading @1115-1116 is one word ("cela"), so @1116's 11 is a word-internal syllable and cannot simultaneously be the free determiner "la" governing 88. The "la [88]" determiner frame at @1117 dissolves. Consequently:

- noun-88-det's iff-bar ("name the noun value iff one noun parses both @402 and @1117") is **moot** — recorded here per the bar.
- 88's determiner-before-88 window set shrinks to **{@402}** — the only determiner-before-88 contact that survives is 45="ce" (granted A4) at @402. Recorded here per the bar.

No new value, class, or registry claim is made: 69's global value stays open per R19-108; 88's value/class unchanged; §7 intact.

## Scope

- This report fires a pre-computed conditional branch only; it adjudicates nothing new and touches no red-team material (read-only).
- Coordination note (not a queue edit — the supervisor owns queuing): `noun-88-epicene` remains `queued` with the bar "name a period-attested consonant-initial epicene noun parsing both @402 and @1117"; under branch A the @1117 determiner frame dissolves, so that bar's premise fails. Flagged for supervisor reconciliation; this battery did not touch its queue entry (verified still `queued`/verdictless).
- `noun-88-det` is `verdict`/`null` (2026-10-09) — no downgrade, no edit; the "moot" is recorded in this report, not on its entry.
- R20-135's FENCE on split-69-adjudicate (69 stays ["noun","cls"] with 'ce' value-lead) is consistent with branch A and untouched.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-cela-1117-frame-resume.md` (this file).
- Queue: `cela-1117-frame-resume` queued → `verdict`/`promote`, 2026-10-09 (pre-write assert passed — was queued/verdictless; same-directory temp-file + rename; JSON re-validated; own entry only; no downgrade).
- Lock `code/crowd17/next-token/locks/cela-1117-frame-resume.lock` created on start, deleted on completion (verified gone).
- R5005, sealed gates, red-team adjudication queue untouched.

## Verdict: PROMOTE

The red-team ruling is located (R19-108 GRANT, locus-level, standing at R20-135) and branch A fires: noun-88-det's bar is moot and 88's determiner window set shrinks to {@402}, exactly as pre-computed in the parent battery.
