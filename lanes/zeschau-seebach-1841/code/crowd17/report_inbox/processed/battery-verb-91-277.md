# Battery verdict: verb-91-277

- Target: `verb-91-277` (battery-queue.json, priority 3, status queued)
- Claim: Test 91 as finite verb/copula at @277 ('on [91] [37-pred]'); name the value or fence.

## Bar (verbatim)

"name 91's value iff it parses as finite verb/copula with standing values and zero kill-grade contradictions; else fence verb-91 at the locus"

Numbered clauses:
- C1. Name 91's value: it must parse as finite verb/copula at @277 with standing values and zero kill-grade contradictions.
- C2. Else fence verb-91 value-naming at the locus.

## Method

1. Read BATTERY-PROTOCOL.md first. Created `locks/verb-91-277.lock` on start (agent a8653508-77ec-4e14-a620-68096f42474e, 2026-10-09T20:29:00Z); deleted on completion.
2. Re-derived the repaired stream in-session from `code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt` via the repair_parse.py tokenizer: 1,847 pairs, 96 types. `canonical.py` never used.
3. Byte-confirmed the locus: @275=89, @276=84, @277=91, @278=37, @279=61, @280=20, @281=61, @282=42, @283=48.
4. Tested the finite-verb/copula candidate set for selectability under standing values.

## Findings

**Frame (standing values):** `[89] on(84) [91] [37-pred] 61 20 61 42 48(e)`. Adopted from sibling `verb-91-277-frame` (PROMOTE, same locus, 2026-10-09): 91 = finite-verb CLASS at @277 (locus-level); the adverb arm is fenced. The '84 91' bigram is exactly 1x stream-wide; '91 37' is 1x; 91 is not in the registry (n(91)=21).

**C1 — value-naming FAILS: no candidate is selectable.**

Tested the copula/transitive 3sg candidates: est, fait, dit, peut, doit, veut, semble, reste. Every one parses the frame identically:

- Zero kill-grade contradictions for any candidate: 84="on" (A15) holds unconditioned at @276; 37 is class-open predicative (A1), 61/20/42 class-open, 48="e" letter tier. No agreement controller beyond 3sg, no object, no complement, no selectional restriction anywhere in the rightward tail.
- Zero selective legs: the tail `37 61 20 61 42 48` supplies no pressure that distinguishes est from fait, dit, peut, doit, or the rest. Copula "est" parses; transitive "fait" parses equally ("on fait [37-pred] [61]...").

Per the val-03-value-census precedent (parsing ≠ naming), a frame that parses every candidate identically cannot name any one of them. C1 fails.

**C2 — fence arm FIRES.** Verb-91 value-naming at @277 is fenced (evidentiary, not kill-grade: no window forces any specific value false; re-openable if a second selective leg is banked, e.g. 37's class or 61's class).

**Scope note:** this battery touches VALUE only. The CLASS (finite verb at @277) is the sibling's PROMOTE and is untouched. No standing/red-team verdict contradicted, downgraded, or re-litigated; §7 intact. The past-participle-vs-finite-verb tension across 91's windows remains the sibling's §7 red-team input. Canonical-stream caveat stands.

## Verdict: NULL (fence executed)

## Follow-ups (all verified ABSENT from queue)

1. `val-37-278-class` (P4) — name 37's class at @278; a valued predicative (noun phrase vs adjective) selects between copula candidates (est/semble) and transitive candidates (fait/dit).
2. `sel-61-verb-object` (P4) — name 61's class at @279; a verb-object role for 61 selects only transitive candidates and re-opens C1.
3. `val-20-280-constrain` (P4) — name 20 at @280; the `61 20` tail may add the missing selective leg.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-verb-91-277.md`
- Queue: `verb-91-277` queued → `verdict`/`null`, 2026-10-09 (pre-write assert passed — was queued/verdictless; target-id-unique tmp `battery-queue.json.verb-91-277.tmp` + atomic rename; disk re-validated; own entry only; no downgrade; no tmp leftover)
- Lock `locks/verb-91-277.lock`: created on start, deleted on completion (verified gone). R5005, sealed gates, red-team adjudication queue untouched.
