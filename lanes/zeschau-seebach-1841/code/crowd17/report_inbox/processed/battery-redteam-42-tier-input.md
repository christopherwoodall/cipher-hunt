# Battery report: redteam-42-tier-input — verdict: NULL (gather-only package delivered)

- Target id: `redteam-42-tier-input`
- Claim: gather-only: package the letter-tier results as red-team input for 42's tier adjudication.
- Date: 2026-10-09
- Worker: battery worker (subagent 37439406-6bd4-478e-a477-5705dec61a40)
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py`). `canonical.py` never used. R5005, sealed gates, red-team adjudication queue untouched.

## Bar (verbatim, pre-registered before testing)

"deliver the package (42-06 escalated, 42-94 killed, 29/33 compositions fail at battery grade, 40 vacuous, 42-48 deferred to val-42-282-fem); gather only, no adjudication"

Numbered pass/fail clauses:

1. **C1:** Package delivered covering all five named components with their verdicts and report references → NULL.
2. **C2:** No adjudication — no tier named, no split declared, §7 intact.

## Package contents

Standing baseline: 42 = noun, class-level (registry `["noun","cls"]`). n(42)=20. No tier value named anywhere. The red-team adjudication question: which tier(s) does 42 occupy — noun-word, letter/syllable, verb-stem — and under what conditioning.

### 1. 42-06: ESCALATED (red-team venue, §7)

"42 06" x5 (06="ent" battery-grade). The verb-stem contact: noun/verb-stem polyvalence reading ESCALATED to the red team by `battery-stem-42-verb` per §7 — only the red team can declare a positional/polyvalence reading (67 et/veut is the sole true polyvalence). A battery may not name a syllable value at this contact. The escalation stands unadjudicated.

### 2. 42-94: KILLED (letter composition arm)

- `battery-val-42-ne-noun` — **KILL** ([42ne]-noun has no compatible value): corpus-wide computation over 41,923 word types — exactly one stem S ("re") satisfied the joint constraints, and S was already tested and killed in `battery-noun-42-value` ("erre/re": @79 "l'erre" fits, all 16 standalone windows fail; score 1/20).
- Adopted by `battery-val-42-lettertier` (2026-10-09) as killed.
- Residual note: `battery-frame-42-94-leftward` returned NULL (live conditioned hypothesis, docket-gated at W2) and `battery-subj-42-ne-frame` NULL — the kill above is the letter-composition "[42]ne"-as-one-word arm; the clause-level "42 ne X" frame (94='ne' STRONG LEAD as negator, R17-001) is separate and untouched.

### 3. 29/33 compositions: FAIL at battery grade

From `battery-val-42-lettertier` (NULL, 2026-10-09), all byte-exact on the repaired stream:

- "33 42" x2 (@265/@1502): 33's value is open (33 ∈ {dire, [X]er}); identifying any one-word "33"+"42" spelling requires naming 33's value first — a new assumption. Arguendo with 33='dire': no French word ("dire"+X finite verb doesn't exist); arguendo with 33=[X]er stem: needs both 33's stem and 42's piece named. **FAIL.**
- "29 42" x3 (@79/@219/@1144; 29="er" pencil GT): French 2-syllable "er"+X words (erreur, ermite, errer, ergot) — no single word parses all three windows (@219 "que"+noun ungrammatical); selecting per-window words is a §7 split declaration. **FAIL.**
- "42 33" x1 (@1503): "redire" candidate fails — "on [33]" fenced to 84 (orphan-1502). **FAIL.**

### 4. 40 arm: VACUOUS

40 (='e' pencil GT) never occurs within ±2 pairs of any 42 window stream-wide. No composition exists to test. The 40 arm of the syllabary is vacuous, not negative.

### 5. 42-48: deferred to val-42-282-fem — KILL

`battery-val-42-282-fem` — **KILL**: "61 42 48" @282 as "[61] [42]e" with 48="e" killed. The "42 48" feminine-"e" composition arm is closed.

## Per-clause results

- **C1: PASS.** All five components packaged with verdicts and report references.
- **C2: PASS.** No adjudication performed: no tier named, no value named, no §7 split declared.

## Verdict: NULL (gather-only package delivered)

## Scope (stated, not hidden)

- 42's NOUN class grant untouched; 94='ne' STRONG LEAD untouched; 67 sole polyvalence untouched.
- No standing or red-team verdict contradicted, downgraded, or re-litigated. §7 intact.
- No follow-ups proposed (gather-only precedent, R19-182): the red team adjudicates 42's tier from this package.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-redteam-42-tier-input.md` (this file).
- Queue: `redteam-42-tier-input` queued → `verdict`/`null`, 2026-10-09 (pre-write assert passed — was queued/verdictless; target-id-unique temp file `battery-queue.json.redteam-42-tier-input.tmp` + atomic rename; JSON re-validated from disk; own entry only; no downgrade).
- Lock `code/crowd17/next-token/locks/redteam-42-tier-input.lock` created on start (agent 37439406, 2026-10-09T20:01:56Z; no stale lock), deleted on completion (verified gone).
- R5005, sealed gate instances, red-team adjudication queue untouched.
