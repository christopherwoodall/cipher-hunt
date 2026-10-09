# Battery verdict: val-16-187-bound

- Target: `val-16-187-bound` (battery-queue.json, priority 3, status queued)
- Claim: "Name 16's class at @187. If 16 licenses a clause break (conjunction/boundary-like), the stacked-'pour' problem dissolves and 'Pour [66]' can open a new sentence; re-test @189's left attachment."
- Parent: `pour-66-189-boundary` (NULL/fence, 2026-10-09) — follow-up #1.
- Evidence (queue): "Parent: pour-66-189-boundary (NULL, 2026-10-09): @187 16 class; @189 left attachment"
- Adverses (queue): "class-level only"

## Bar (verbatim, from battery-queue.json)

"name 16's class at battery grade; re-test @189's left attachment iff a clause break is licensed"

Numbered clauses (fixed before testing, not modified after):

1. **C1 (name class):** Name 16's class at @187 at battery grade (zero new assumptions, no contradiction of standing values).
2. **C2 (conditional re-test):** IFF a clause break is licensed for 16, re-test @189's left attachment ("pour [66]" opening a new sentence).
3. **C3 (fail-closed):** If C1 fails, fence class-naming at @187 with stated cause and propose follow-ups per §4.

## Method

1. Read BATTERY-PROTOCOL.md in full. Created `locks/val-16-187-bound.lock` on start (agent 592bf695-b1a3-4367-85d1-290c4a94112e, 2026-10-09T20:44:17Z); deleted on completion.
2. Re-derived the repaired stream in-session from `code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt` via `repair_parse.py`: 1,847 pairs, 96 types. `canonical.py` never used.
3. Byte-confirmed the locus: 0-based @185=00, @186=33, @187=16, @188=00, @189=66 (row a1_05; the target's "@187" matches 0-based here — prior batteries use 0-based).
4. Rendered 16's full distributional profile (n=28) and read the parent report plus the three standing 16-class batteries before testing:
   - `frame-82-16` (NULL, 2026-10-09): KILLED 16="mais" (conjunction); eliminated "même"/noun/infinitive.
   - `val-16-a-vs-est` (NULL/fence, 2026-10-09): fenced the 'a'/'est' value refinement; the finite-verb CLASS lead carries @1481 as an unresolved forced contradiction (red-team territory).
   - `gate-satisfiability-16-85` (PROMOTE, 2026-10-08): exhibited single-class assignment 16=infinitive under §7 sole-polyvalence; "the infinitive readings of 16 and 85 survive every banked-value frame."
   - `val-16-84-role` (NULL, 2026-10-09): locus-level role underdetermined; recorded the global finite-verb class fence.

## Window-level evidence

### The locus

`@185=00(pour,A9) @186=33 @187=16 @188=00(pour) @189=66(nonfin arm)` — the parent's stacked-`pour`: "pour [33] [16] pour [66]".

### 16's distributional profile (n=28, byte-confirmed)

- Predecessors: 82='m' ×11, 62 ×4, 12 ×3, 33 ×2, 42 ×2, 65/32/49/86/67/89 ×1.
- Followers: 00='pour' ×4, 24 ×2, 01 ×2, 76 ×2, 91 ×2, 14/56/52/78/08/77/92/88/29/96/64/02/06/97/98/59 ×1.
- The 11 "82 16" windows: @382, @434, @537, @1195, @1198, @1370, @1387, @1437, @1480, @1652, @1832 — 11/28 of 16's occurrences sit after the clitic pronoun 'm' (82, pencil GT).

### Arm-by-arm test at @187

**Conjunction / clause-boundary (the bar's target arm) — KILLED at kill grade.**

Two independent kills, both value-independent of 16:

- K1 (adopted, not re-litigated): `frame-82-16` killed 16="mais" via the doubled frame ("m[16] par m[16]" = "mais par mais qui", ungrammatical); no other window supports it.
- K2 (new, distributional): 11/28 of 16's windows are "82 16" — the elided object clitic 'm' (82, pencil GT) immediately precedes 16. French object clitics are strictly preverbal; a clause break or conjunction between a dangling clitic and its verb is ungrammatical at kill grade ("m et …" / "[m]. [New clause]" never occurs in 1841 French). A boundary-like 16 would strand 'm' in 11 windows. This is value-independent — it rests only on 82='m' (banked) and the proposed boundary role, never on 16's value.

The conjunction/boundary class is therefore dead for 16 globally, not just at @187. A locus-only boundary reading (16=conjunction at @187 only) would be a conditioned split — §7 red-team venue, which the battery cannot declare.

**Consequence for the parent's three stacking rescues:** rescue (a) ("16 = coordinator/comma licensing '[pour 33-inf] [16] [pour 66]'") is dead at kill grade. Rescue (c) (00@185 not "pour") is out of scope (00 is A9 class-level, not this target). Rescue (b) (sentence boundary before "Pour [66]") needed 16 to close a clause — also dead.

**Finite verb — FENCED (unnameable at battery grade), not kill-grade dead.**

- For: the verb-like profile ("m 16" ×11 clitic+verb shape; "16 pour" ×4 verb+infinitive-phrase shape); val-16-a-vs-est tested this locus (its 1-based @188 = my @187) and found 'a pour'/'est pour' both grammatical — CONDITIONAL on open 33, not forced-false.
- Against naming: the finite-verb CLASS lead carries @1481's unresolved forced contradiction ("m'a/m'est"+finite 98) per val-16-a-vs-est; val-16-84-role recorded the global finite-verb class fence. Naming finite-verb at @187 alone = a locus-level conditioned split — §7 red-team venue. Neither 'a' nor 'est' is selectable (no discriminator: 33's left edge open, 66's value open).

**Infinitive — FENCED (contradictory standing verdicts; battery cannot adjudicate).**

- `frame-82-16` (2026-10-09) eliminated infinitive; `gate-satisfiability-16-85` (2026-10-08, PROMOTE) exhibited 16=infinitive as the single-class assignment under §7 sole-polyvalence. These two battery verdicts contradict each other on 16's class. Per §5 (never downgrade an existing verdict) and the contradiction rule, a battery may not name either side. This is red-team territory. Recorded as headline fence, not re-litigated.

**Noun — KILLED (adopted from frame-82-16; not re-litigated).**

### C2's condition check

No clause break is licensed for 16 (conjunction/boundary killed at kill grade). **C2's re-test condition does NOT fire.** @189's left attachment is not re-tested here; the stacked-`pour` problem stands exactly as the parent left it (its fence cause remains "unresolvable at battery grade" pending red-team action on 24's class or the 16 contradiction).

## Per-clause pass/fail

1. **C1 (name 16's class at battery grade): FAIL.** Conjunction/boundary killed (K1+K2, kill grade). Finite-verb fenced (unnameable: forced @1481 contradiction on the class lead, no locus-level discriminator, locus-only naming = §7 split). Infinitive fenced (frame-82-16 kill vs gate-satisfiability-16-85 promote — genuine battery-level contradiction, red-team venue). Noun killed (adopted). No class nameable at battery grade.
2. **C2 (re-test @189 iff clause break licensed): MOOT — condition unfired.** No clause break licensed; @189's left attachment unchanged.
3. **C3 (fail closed): FIRES.** Verdict NULL with follow-ups below.

## Verdict: NULL (fence executed)

- The clause-break arm for 16 is fenced at **kill grade** (K1 adopted + K2 distributional), value-independently. The parent's rescue (a) and the sentence-boundary half of rescue (b) are dead. @189's stacking problem is not dissolved by 16.
- 16's class at @187 is fenced as unnameable at battery grade: the only live class arms (finite-verb, infinitive) are both blocked — one by an unresolved forced contradiction plus §7, the other by a genuine battery-verdict contradiction that only the red team can adjudicate.

## Scope

Class-level only (per adverses). Untouched: frame-82-16's eliminations, val-16-a-vs-est's fence, gate-satisfiability-16-85's PROMOTE, val-16-84-role's fence, the parent pour-66-189-boundary's fence, 33's open class, 24's contested class, 66's §7 split docket, §7 (no polyvalence declared). No standing or red-team verdict contradicted, downgraded, or re-litigated. Canonical-stream caveat stands (row a1_05 offsets unvalidated).

## Follow-ups (§4; all verified ABSENT from battery-queue.json)

1. `redteam-16-inf-contradiction` (P3, red-team venue) — package the battery-level contradiction: frame-82-16 (2026-10-09) eliminates infinitive for 16 while gate-satisfiability-16-85 (2026-10-08, PROMOTE) exhibits 16=infinitive as the single-class assignment. Only the red team can adjudicate; 16's class is blocked until then.
2. `reseg-187-33` (P4) — test 33's class at @186 (parent's "pour [33-inf]" premise; 33's class is open). If 33 re-tiers, @187's 16-class frame changes and the 'a pour'/'est pour' conditionality may resolve.
3. `subj-16-187` (P4) — name 16's subject at @187; a named subject selects the finite-verb class locus-locally and breaks the current fence.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-val-16-187-bound.md` (this file).
- Queue: `val-16-187-bound` queued → `status: verdict`, `result: null`, 2026-10-09 (pre-write assert passed — was queued/verdictless; target-id-unique tmp `battery-queue.json.val-16-187-bound.tmp` + atomic rename; disk re-validated; own entry only; no downgrade; no tmp leftover).
- Lock `locks/val-16-187-bound.lock`: created on start (2026-10-09T20:44:17Z, no stale lock), deleted on completion (verified gone).
- R5005, sealed gates, red-team adjudication queue untouched.
