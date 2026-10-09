# Battery report: conj-20-642-subordinator

- Target id: `conj-20-642-subordinator`
- Claim: "the one live subordinator-shaped window: test \"[48] [20] [24-fin]\" once 48's class at @641 is named."
- Date: 2026-10-09
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py`). Verified in-session: 1,847 pairs, 96 types. `canonical.py` never used. R5005, sealed gates, red-team queue untouched.

Terms (ASD-STE100): "letter tier" = a cipher number that writes a single letter inside a word (not a standalone word). "word-internal" = inside one word. "subordinator" = a conjunction that introduces a subordinate clause (example: "que"). "fence" = the route is suspended with a stated cause, not killed. "battery grade" = the evidence standard of this pipeline.

## Bar (verbatim, pre-registered before testing)

"name 48's class; a nominal/verbal 48 + finite-24 + forced subordinating slot revives the conjunction arm at this window alone; else fence @642 too"

Numbered pass/fail clauses (restated before testing, not modified after):

1. **C1:** 48's class at @641 is named with byte evidence at battery grade.
2. **C2:** the conjunction arm revives iff 48 is nominal/verbal standalone at @641 AND 24 is finite at @643 AND a subordinating slot for 20 is forced at @642.
3. **C3:** else fence @642 (the conjunction arm at this window is suspended with stated cause).

Adverses listed: none.

## Method

1. Read BATTERY-PROTOCOL.md first. Created `code/crowd17/next-token/locks/conj-20-642-subordinator.lock` on start (2026-10-09T11:56:15Z); will delete on completion. No stale lock was present.
2. Re-derived the repaired stream in-session. All @-offsets below are 0-based pair indices.
3. Adopted, never re-litigated: 48='e' promoted (banked map, letter tier); 20's class at @642 = post-nominal adjective (battery PROMOTE `subj-20-642`, window-level); 77='le' provisional; 24 finite/modal class (R17-009); subj-20-642's consequence that form-24-643's C2 blocker is removed (24-finite at @643 stands free of the 20-class block). §7 intact — no polyvalence declared.

## Window-level evidence

The locus (byte-confirmed, row a4_01/a4_02 boundary):

- 0b@630–652: `67 08 52 67 63 74 46(que) 60 67 77(le) 89 48(e) 20 24 87(ce) 61 88 77(le) 78 52 82(m) 94(ne) 76`
- Focal geometry: @639=77, @640=89, **@641=48**, @642=20, @643=24, @644=87 — `…le [89]e |20| 24 ce [61]…`

48's distributional profile (byte-exact):

- n(48) = 38. "89 48" occurs 3x stream-wide (@641, @872, @987); the trigram "89 48 20" occurs 2x (@641, @872).
- Twin window @872: `…87 77 89 48 20 74…` — same `le [89]e [20]` geometry.
- 48 has apparent word-initial loci elsewhere (@1525 "11 48 96" = "la [48] par"; @928 "96 48 82" = "par [48] m"), but neither bears on @641's class.

## Per-clause pass/fail

- **C1 — PASS.** 48's class at @641 is named: **letter tier, word-final 'e'**, part of the single word "[89]e". Grounds: (a) 48='e' is promoted in the banked map (letter tier, not a standalone word); (b) at @641 it sits inside the `le [89]e` NP frame that `subj-20-642` reads as noun-forced (arm A); (c) no battery-grade arm makes 48 a standalone word here — a bare-"e" standalone word is impossible in French, and an "e"-initial word would need 20 to supply its letter, which contradicts 20's window-level adjective class at @642 (adopted standing verdict). 48 is not nominal/verbal standalone at @641.
- **C2 — does not fire.** The revive clause needs 48 nominal/verbal; C1 names it letter-tier and word-internal. The other two legs are also hostile: 20's slot is occupied by the standing post-nominal-adjective reading at this exact window (`subj-20-642` PROMOTE) — 20 cannot simultaneously introduce a subordinate clause; there is no forced subordinating slot.
- **C3 — FIRES (fence).** @642's conjunction/subordinator arm is fenced with stated cause: 48 is a word-internal letter (not a clause-hosting standalone word), and 20's slot at @642 is class-named as post-nominal adjective. This completes the profile fence started by `conj-prep-20-wide` (NULL): @642 was its one live window, and it is now fenced at window level too. Fence, not kill: a red-team ruling on 20's global class (`poly-20-docket`, queued) or a 48 polyvalence could re-open the route.

No standing/red-team verdict contradicted or downgraded. §7 intact (67 et/veut sole polyvalence). Canonical-stream caveat stands (rows a4_01/a4_02 unvalidated).

## Verdict: NULL (fence executed per the bar's else-arm)

## Follow-ups proposed (all verified ABSENT from battery-queue.json; `poly-20-docket` is already queued — noted, not re-proposed)

1. `val-48-initial` (P3) — name 48's value at the two apparent word-initial loci (@1525 "la [48] par", @928 "par [48] m"); closes whether 48 has any standalone word-arm or is letter-tier everywhere. Bar: one value parsing both windows, or fence the initial-locus question.
2. `subj-20-872` (P3) — re-run the `subj-20-642` method at the @872 twin (`87 77 89 48 20 74`); tests whether 20's post-nominal-adjective class replicates at the second "89 48 20" window, or whether the twin keeps the @642 fence company. Bar: class named with zero ungranted assumptions, or fence @872.

## Bookkeeping

- Queue: `conj-20-642-subordinator` -> status `verdict`, result `null`, 2026-10-09 (pre-write assert passed — was `queued`/verdictless; temp-file + rename; JSON re-validated; own entry only; no downgrade).
- Lock `locks/conj-20-642-subordinator.lock` created on start, deleted on completion (verified gone).
