# Battery verdict: val-61-925-timeunit

- Target: `val-61-925-timeunit` (battery-queue.json, priority 3, status queued)
- Claim: "Name 61's value at @925; a time-unit noun completes 'une fois [61] par' and hardens the @924 feminine leg to battery grade."
- Date: 2026-10-09
- Stream: repaired 1,847-pair / 96-type parse (repaired_offsets.json + upstream-ct_R5005.txt, re-derived in-session; asserts held: 1,847 pairs, 96 types). `canonical.py` never used.

## Bar (verbatim, pre-registered)

"name 61's value iff stated values license it at battery grade; else fence the time-unit leg"

Numbered clauses:
- C1: stated values license naming 61's value (as a time-unit noun) at battery grade → name it (PROMOTE).
- C2: else → fence the time-unit leg (NULL).

## Method

1. Byte-confirmed the locus on the repaired stream.
2. Adopted (not re-litigated) the standing battery verdicts: `val-61-participle` (verdict/null, 2026-10-09) and `un-71-gender-frame` (verdict/null, 2026-10-09, parent).
3. Ran an independent corpus spot-check on the claim's exact frame ("fois [time-unit] par") vs the idiomatic order ("fois par [time-unit]") over `code/side-period/corpus/`.

## Window (byte-exact)

0-based `@923=65 @924=71 @925=17 @926=61 @927=96 @928=48` (row a5_10)
= "[65-N] [71] fois [61] par e …" (17=fois granted, 96=par granted, 48='e' promoted letter tier).
The claim's "@925" is 1-based = 0-based @924 (the 71 pair); 61 sits at 0-based @926.

## Findings

### C1 fails on three independent grounds

**Ground 1 — word order: the claim's frame is not French.**
The French time-unit idiom is "une fois **par** [unit]" (par precedes the unit), not "une fois [unit] **par**".
Independent corpus check this session: "fois par [time-unit]" → 20 hits ("12 fois par semaine", "3 fois par jour", "1 fois par mois", "4 fois par an").
"fois [time-unit] par" (the claim's order) → **0 hits**. The frame "une fois [61] par" with 61 as a time-unit noun is ungrammatical.

**Ground 2 — slot class: no noun fits "fois _ par".**
Adopted from the standing battery verdict `val-61-participle` (2026-10-09, verdict/null): its corpus census of "fois X par" found **34 raw hits, all participles** ("révélée", "protégée", "consacrée", "établie", "reçu", …) — "the 'fois _ par' slot admits **only participles** (no noun/adjective/adverb/infinitive fits). Participle is the sole grammatical class for 61 at @926."
A time-unit noun is a noun. No noun can occupy the slot at corpus grade.

**Ground 3 — naming: no stated value selects one time-unit noun.**
Even setting Grounds 1–2 aside, the candidate set {jour, mois, an, semaine, année, heure, minute, seconde, siècle, quinzaine, …} parses identically — zero selectional pressure (parsing ≠ naming, per val-03-value-census precedent). No agreement controller or complement selects one.

### C2 fires

The time-unit leg is fenced with stated cause: the claim's frame is ungrammatical (Ground 1), and the slot is participle-only at corpus grade (Ground 2). The fence is near kill-grade in substance, but the bar's else-arm is fence, so the verdict is NULL per the bar as written.

## Adverse answered

"61's global value is killed - locus-level only": no value is named at any level, so the locus-level constraint is untouched. Consistent with `val-61-contact` KILL (no global 61 value), `val-61-premier` locus-level @1556, and `premier-61-admit-fence`.

## Per-clause pass/fail

- C1 (name 61's value at battery grade): **FAIL** — Grounds 1–3.
- C2 (fence the time-unit leg): **FIRES**.

## Verdict: NULL (fence executed per C2)

## Scope

Fences only the time-unit-noun leg at @926. Untouched: the @924 feminine leg recorded by `un-71-gender-frame` (the leg stands as recorded; only the time-unit completion route is fenced), `val-61-participle`'s participle-class finding at @926 (consistent — participle remains the sole grammatical class), `val-61-contact` KILL, `val-61-premier` @1556 locus-level, 48='e', 98='vient' LEAD, §7. No standing or red-team verdict contradicted, downgraded, or re-litigated. Canonical-stream caveat stands (row a5_10 offset unvalidated).

## Follow-ups proposed (§4; all verified ABSENT from battery-queue.json)

These were also proposed by `val-61-participle` but are still absent from the queue (pipeline gap noted for the supervisor):

1. `part-61-gender-ctrl` (P4) — determine 61's agreement controller at @926: does the participle agree with "fois" (feminine) or an implied subject (gender open)? A feminine controller names the feminine participle.
2. `par48-e-agent` (P4) — resolve "par [48]" at @927: test composition of 48 with following cells, or re-parse "par" as heading a non-agent constituent. A parsing agent re-opens the participle frame.
3. `fois-part-abs-frame` (P4) — corpus census of agentless "fois [part]" (absolute use, no "par"): if productive, the participle frame survives without the agent arm.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-val-61-925-timeunit.md`
- Queue: `val-61-925-timeunit` queued → `verdict`/`null`, 2026-10-09 (pre-write assert passed — was queued/verdictless; target-id-unique tmp `battery-queue.json.val-61-925-timeunit.tmp` + atomic rename; disk re-validated; own entry only; no downgrade; no tmp leftover)
- Lock `locks/val-61-925-timeunit.lock`: created on start (agent 5c2b957f-5937-418f-b3ee-178575a41e9a, 2026-10-09T21:30:00Z, no stale lock), deleted on completion (verified gone). R5005, sealed gates, red-team adjudication queue untouched.
