# Battery verdict: nece-1169-revisit

- Target: `nece-1169-revisit` (priority 3, battery-queue.json)
- Claim: Re-test ne-ce-1169's rescue inventory now that 61='pren' is killed.
- Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json + data/upstream-ct_R5005.txt, parsed per repair_parse.py). Never canonical.py.
- Date: 2026-10-09

## Bar (verbatim from dispatch brief)

"Its 'two grant-compatible rescues' were predicated on the live word-unit fork: re-derive with that fork dead; fence or keep at battery grade."

Numbered clauses:

1. Re-derive rescue (1) — leftward attachment 61-94 as word-final "...ne" (prenne/donne/vienne family) — with 61='pren' dead. Fence or keep at battery grade.
2. Re-derive rescue (2) — word-initial 94-87 = "néce-" (nécessaire/nécessité family) — with 61='pren' dead. Fence or keep at battery grade.

Adverses: 87='ce' granted; 94-87 hapax (stream-unique bigram); R17-001 (94='ne' STRONG LEAD) must not be overturned; no second 94 value declared (§7).

## Method

Re-derived the target window on the repaired stream (asserts held in-session); adopted (not re-litigated) the standing verdicts: seg-61-pren-polyvalence KILL (2026-10-08), nece-94-87-initial KILL (2026-10-08), seg-61-94-word NULL (2026-10-08), seg-61-94-word-adjudicate KILL (2026-10-09), val-61-premier PROMOTE locus-level (2026-10-09), val-61-contact KILL (any global 61 value).

## Window-level evidence

Target window byte-confirmed @1164–1173 (row a6_09):
`78 @1164, 45 @1165, 13 @1166, 55 @1167, 61 @1168, 94 @1169, 87 @1170, 83 @1171, 21 @1172, 85 @1173`.
61-94 bigram exactly 2x stream-wide (@577, @1168), both preceded by the 4-gram `78 45 13 55`.

## Per-clause pass/fail

1. **Rescue (1) — FENCED.** The rescue's demonstrated word was "prenne" via 61='pren': kill-grade dead (seg-61-pren-polyvalence: @1556 "prene fois" with banked 40='e'/17='fois' — "prene" is not a French word, no French word ends in "pren"; @367 "prenpre" unreadable). Its 55-61-94 prenne-family extension ("re-/com-/sur-prenne"): kill-grade dead (seg-61-94-word-adjudicate KILL, 2026-10-09; frame-restricted rescue would be §7 polyvalence). What survives is only the generalized leftward fork ("...ne" with 61 open) — grant-compatible in principle but with no French word demonstrated, and no battery-grade path to demonstrate one: val-61-contact KILLed any global 61 value, and the only named 61 value anywhere (val-61-premier, locus-level @1556 "première fois") does not transfer and does not yield a "...ne"-final word at @1168. The fork is a bare possibility, not a keepable rescue.
2. **Rescue (2) — KILLED (adopted).** nece-94-87-initial returned KILL on 2026-10-08; 61='pren' is irrelevant to it. Not re-litigated.

## Verdict: NULL (fence executed)

ne-ce-1169's rescue inventory is exhausted at battery grade: rescue (1)'s only demonstrated word is kill-grade dead and its extension adjudicated closed; rescue (2) was already killed. The @1169 bigram is now a pure segmentation residual — 94-87 unresolvable at battery grade pending 61's value or red-team §7 action (redteam-94-functional-split is already queued, P1). R17-001 untouched; §7 intact; no standing/red-team verdict contradicted or downgraded. Canonical-stream caveat stands.

## Proposed follow-up targets (null regenerates work; all verified ABSENT from battery-queue.json)

1. **seg-61-1168-lettertier** (P4). Claim: test 61 as letter/sub-lexical tier at @1168 — a "...ne"-final word needs 61 as the preceding syllable (donne/vienne/prenne family), and 61's global value is killed but a locus-level value is still nameable (cf. val-61-premier precedent). Bars: name a locus-level 61 syllable yielding a French "...ne" word with 94, or fence the letter-tier fork.
2. **nece-1169-residual** (P4, gather-only). Claim: package the @1169 residual (this report + ne-ce-1169 + seg-61-94-word-adjudicate + nece-94-87-initial) as red-team input feeding the queued redteam-94-functional-split P1. Bars: package delivered, no adjudication, no battery split declaration.

(A third candidate, re-testing 94's negator reading at @1169, is dropped — ne-ce-1169 already fenced it as ungrammatical, and R17-001 owns the question.)

## Bookkeeping

- Report: code/crowd17/report_inbox/battery-nece-1169-revisit.md
- Queue: `nece-1169-revisit` queued → `verdict`/`null` 2026-10-09 (pre-write assert passed — was queued/verdictless; target-id-unique temp file `battery-queue.json.nece-1169-revisit.tmp` + atomic rename; disk re-validated; own entry only; no downgrade).
- Lock `locks/nece-1169-revisit.lock`: created on start (agent 6e99b729-dc87-4491-8487-7010b844a550, 2026-10-09T19:29:11Z, no stale lock), deleted on completion (verified gone).
- R5005, sealed gates, red-team adjudication queue untouched.
