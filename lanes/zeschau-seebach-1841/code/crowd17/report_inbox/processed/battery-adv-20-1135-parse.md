# Battery report: adv-20-1135-parse

- Target id: `adv-20-1135-parse`
- Claim: "GATED: re-test @1135's boundary-adverb parse once 86's INF-class arm is named"
- Date: 2026-10-09
- Worker: battery worker (subagent 74369004-4d22-45b9-9372-81be6b10d148)
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py`). Asserts held: 1,847 pairs, 96 types. `canonical.py` never used. R5005, sealed gate instances, red-team queue untouched.
- Lock: `code/crowd17/next-token/locks/adv-20-1135-parse.lock` created 2026-10-09T12:01:37Z; no stale lock existed; deleted on completion.

Terms (ASD-STE100): "boundary adverb" = a clause adverb that opens a new clause ("Alors, il vient" — "So, he comes"). "INF-class" = infinitive-class (a verb form that cannot stand as a finite clause verb). "battery grade" = forced with zero ungranted assumptions. "governed infinitive" = an infinitive licensed by a modal verb ("veut le laisser").

## Bar (verbatim, from battery-queue.json)

"hold until 86's INF-class arm is named; then parse @1135's boundary-adverb reading with zero ungranted assumptions; else fence"

Numbered pass/fail clauses (pre-registered before testing, not modified after):

1. **C1 (gate):** 86's INF-class arm is named at battery grade.
2. **C2 (parse):** @1135's boundary-adverb reading "…[86]. [20-adv] il(62) vient(98) pour(00)…" parses with zero ungranted assumptions under standing values + named INF-class 86.
3. **C3 (else-arm):** if C2 fails, fence @1135 with stated cause.

Adverses listed: none.

## Method

1. Read BATTERY-PROTOCOL.md first. Created the lock on start; deleted on completion.
2. Re-derived the repaired stream byte-exact. All @-offsets below are 0-based.
3. Adopted, never re-litigated: `infclass-86` PROMOTE (2026-10-07, A9 class-level: pre=00 x12, suc=29 x4, 33-parallel; stem/whole caveat = class-level only); R17-009 (24 = finite/modal-shaped verb class); 62='il' (battery promote); 98 finite verb-shaped (vient profile); 00='pour' (promoted); 77='le' (provisional); `conj-prep-20-wide` NULL (conjunction/preposition arms for 20 fenced); `adverb-20-wide` NULL (fence of the adverb arm globally; @1135 listed as compatible-not-forced); `poly-20-docket` (20's global class = red-team venue, NOUN vs DET/ADJ); §7 (67 et/veut sole true polyvalence).

## Window-level evidence

### The locus — @1125–1145 (rows a6_07/a6_08)

`@1130=37 @1131=86 @1132=24 @1133=77 @1134=86 |@1135=20| @1136=62 @1137=98 @1138=00 @1139=98 @1140=78 @1141=62`

The focal geometry: `…[24] [77] [86-inf] |20| il(62) vient(98) pour(00)…`

### Distributional facts (byte-exact, re-derived)

- n(86) = 32. 86 pre=00: 12x; 86 suc=29: 4x. Matches the A9 INF-class legs exactly.
- "86 20" bigram: 1x stream-wide (@1134–1135) — a hapax; zero repetition leverage.
- "24 77 86" trigram: 1x stream-wide (@1132–1134) — a hapax; no second exemplar of the exact modal+clitic+infinitive frame, but the composition rule (modal + clitic + infinitive) is period grammar, not a distributional claim.
- n(20) = 15; n(98) = 40.

### C1 — PASS (gate fires)

`infclass-86` → `status: verdict`, `result: promote`, 2026-10-07. The gate is satisfied; the test proceeds.

### C2 — FAIL (boundary-adverb not forced at battery grade)

The parent's hardening mechanism does not fire, and INF-class supplies no replacement mechanism:

1. **The parent's mechanism needed a FINITE 86** ("a finite reading of 86 forces the boundary and kills the noun rival"). The named arm is INF-class — non-finite. That mechanism is dead on arrival.
2. **INF-class binds 86 INTO the left clause, not out of it.** @1132=24 (R17-009 finite/modal class) + @1133=77 (le, provisional) + @1134=86 (INF-class) composes as modal + clitic pronoun + governed infinitive ("veut le laisser"-shaped) on standing values alone, zero new assumptions. A governed infinitive continues its clause; it does not terminate one. If 24 were read as plain finite (non-modal), "…[24-fin] le [86-inf]" would be ungrammatical in French — so the modal reading is the only licensed one. Either way, 86 does not force a clause boundary at @1134|@1135.
3. **The boundary must fall on one side of 20, but neither side is forced.** The new clause "il vient pour [98]" needs a boundary before "il" (@1136). Two grammatically licensed placements:
   - (a) @1134|@1135: "…le [86-inf]. [20-adv] il vient pour…" — the boundary-adverb parse.
   - (b) @1135|@1136: "…le [86-inf] [20-adv]. il vient pour…" — 20 as clause-final adverb of the modal clause ("…le laisser ainsi"-shaped), licensed period grammar.
   Both need exactly one unmarked-boundary assumption. Neither is forced. Compatible ≠ forced at battery grade.
4. **Rivals do not collapse to one.** The noun-20 rival stays live at red-team venue (`poly-20-docket`, NOUN vs DET/ADJ — not adjudicated). The subordinator rival is fenced (`conj-prep-20-wide` NULL), but fencing one rival does not force the adverb; (b) above remains.
5. **No repetition leverage.** "86 20" is a stream hapax; the frame has no second exemplar.

Conclusion: the boundary-adverb parse is possible but unforced. Battery grade (forced, zero ungranted assumptions) is not met. C2 FAILS.

### C3 — FIRES: fence @1135

Stated cause: the gate fired but the parent's finite-86 mechanism did not materialize — INF-class 86 is non-finite and is the governed complement of modal-24 ("[24] le [86-inf]"), so it binds into the left clause rather than terminating it; the clause boundary can fall on either side of 20 (boundary-adverb vs clause-final-adverb are equally licensed); the noun-20 rival stays live in red-team venue; the bigram is a hapax. Fence, not kill — the parse is possible, just not forced, and a future 20-class ruling or a licensed left-edge frame could re-open it.

## Adverses

None listed.

## Verdict: NULL (fence executed)

No standing or red-team verdict contradicted or downgraded: `infclass-86` PROMOTE adopted as the gate (not re-opened); R17-009 used as premise; `conj-prep-20-wide`, `adverb-20-wide`, and `poly-20-docket` untouched; §7 intact (no polyvalence declared). Canonical-stream caveat stands (rows a6_07/a6_08 offsets unvalidated).

## Follow-ups proposed (all verified ABSENT from battery-queue.json)

1. `adv-1135-leftward` (P3) — test 20 as clause-FINAL adverb of the modal clause at @1135 ("…le [86-inf] [20-adv]" = "…le laisser ainsi"-shaped): kill iff no licensed clause-final-adverb frame survives at this window; this is the surviving rival the boundary-adverb must beat.
2. `bound-1132-modal-edge` (P3) — test whether 24's value at @1132 (once named) fixes the modal clause's right edge: if the modal clause demonstrably ends at 86 (@1134), the boundary can only fall before 20 — re-test the boundary-adverb then.
3. `noun20-1135-gated` (P4) — gated re-test of the noun-20 rival at @1135 once the red team adjudicates `poly-20-docket` (20's global class); not dispatchable until then.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-adv-20-1135-parse.md` (this file).
- Queue: `adv-20-1135-parse` queued → verdict/null, 2026-10-09 (pre-write assert passed — was queued/verdictless; temp-file + rename; JSON re-validated; own entry only; no downgrade).
- Lock `locks/adv-20-1135-parse.lock`: created on start (no stale lock), deleted on completion (verified gone).
- R5005, sealed gate instances, red-team adjudication queue untouched.
