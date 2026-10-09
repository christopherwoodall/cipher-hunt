# Battery report: er-word-lexicon

- Target id: `er-word-lexicon`
- Claim: identify the "er"-initial word at the positional positives @78/@96/@218/@1200 — is it "erreur"?
- Date: 2026-10-09
- Worker: battery worker (subagent)
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py`). Verified in-session: 1,847 pairs, 96 types. `canonical.py` never used. R5005, sealed gates, red-team queue untouched.
- Lock note: no lockfile existed at start (no stale lock). Created `code/crowd17/next-token/locks/er-word-lexicon.lock` 2026-10-09T12:04:23Z; deleted on completion.

Terms (ASD-STE100): "er"-initial word = the word beginning with the "er" syllable (29="er", pencil ground truth). "positional positive" = a 29-window where the left neighbor is a complete word (forcing a word boundary before 29), from parent battery `profile-29-left` (2026-10-08). "battery grade" = the evidence standard of this pipeline. Offsets below are 0-based.

## Bar (verbatim, pre-registered before testing)

"name the word iff it explains all four positional positives"

Numbered pass/fail clauses (restated before testing, not modified after):

1. **C1:** The named word explains the @78 window ("pour la"+"er[42]").
2. **C2:** The named word explains the @96 window ("que"+"er[85]").
3. **C3:** The named word explains the @218 window ("est que"+"er[42]").
4. **C4:** The named word explains the @1200 window ("qui"+"er[45]").
5. **C5 (adverse check):** 42/85/45 values re-checked. If still blocking the naming, fence with stated cause (target brief's own else-arm).

## Method

1. Read BATTERY-PROTOCOL.md first. Created the lock on start; deleted on completion.
2. Re-derived the repaired stream byte-exact per `code/side-keyhunt/repair_parse.py`. All @-offsets below are 0-based pair indices.
3. Standing premises used, not re-litigated: 29="er" (pencil GT); 11="la" (GT); 46="que" (GT); 64="qui" (promoted); 59="est" (provisional); 00="pour" (promoted); 42 = noun class, value open (registry: `['noun','cls']`); 85 = verb-stem class A3, value open (no registry cell); 45 = "ce/dict" lead (A11 hold); §7 (67 et/veut is the sole true polyvalence). French: 1841 diplomatic prose.
4. "erreur" is the candidate word named in the claim. A single "er"-word spelling "er"+"[follower]" requires the follower to supply the second syllable "reur" (or equivalent). One word explaining all four windows therefore requires 42, 85, and 45 to all mean the same second syllable.

## Window-level evidence (byte-confirmed on the repaired stream)

- **@78** (row a1_02): `87 11 00 11 |29| 42 98 51 62 16` → "pour(00) la(11) er[42]".
- **@96** (row a1_02): `98 81 97 46 |29| 85 08 21 62 94` → "que(46) er[85]".
- **@218** (row a2_00): `78 06 59 46 |29| 42 16 24 89 61` → "est(59) que(46) er[42]".
- **@1200** (row a7_00): `96 82 16 64 |29| 45 58 47 43 55` → "qui(64) er[45]".

## Per-clause results

- **C1 — @78 "erreur": PASS (grammatically).** "pour la er[42]" = "pour l'erreur" — article present (11="la"), elision licensed, 42's noun class compatible with "erreur". The only window where "erreur" parses.
- **C2 — @96 "erreur": FAIL.** "que er[85]" = "qu'erreur" — "erreur" is a noun requiring a determiner; none is present ("*qu'erreur" is ungrammatical in every period). Independently, 85 is verb-stem class (A3) — "reur" is not a verb stem, and adopting it as one would contradict the standing class grant.
- **C3 — @218 "erreur": FAIL.** "est que er[42]" = "est qu'erreur" — same article defect as @96.
- **C4 — @1200 "erreur": FAIL.** "qui er[45]" = "qui erreur" — article defect; plus 45 is lead-grade "ce" under the A11 hold, so the "reur"-syllable reading would contradict the standing lead.
- **Rival single-word checks (same lexeme family):** *errer* infinitive ("er"+"rer") — "que errer" (@96), "est que errer" (@218), "qui errer" (@1200) are all ungrammatical. Archaic noun "erre" — needs follower 40="e" (banked), which none of these windows has. No single "er"-word parses all four.
- **Homophony route: BLOCKED.** One word explaining all four requires 42 = 85 = 45 = "reur" — a three-cell homophony declaration. §7 bars this at battery level (67 is the sole true polyvalence; lane naming standard needs FORCED, not compatible). It also collides with 85's verb-stem class and 45's "ce" hold. §3: naming three unvalued cells to fit the claim is invention.
- **Lexeme-family note:** the parent's strong positives establish the *other* "er"-family as the verb *errer* ("qui erre", "l'on erre", "cela erre", "n'erre") — a different lexeme from the noun "erreur". The positional windows and the strong positives are not even family-identical.
- **C5 — the adverse is LIVE.** 42's value is open (noun class only); 85's value is open (verb-stem class only); 45's value is lead-grade (A11 "ce" hold). The naming requires the follower's value — exactly the blocked values the adverse named. No red-team adjudication of 42/85/45 has landed since the parent report. The target brief's own instruction fires: fence with stated cause.

## Verdict: NULL (fence executed)

The adverse's block stands: 42/85/45 are still unvalued, and "erreur" explains only @78 of the four windows (the one window where an article precedes). No word explains all four without (a) declaring three-cell homophony barred at battery level (§7), and (b) inventing three values barred under §3. The fence is stated, not silent: the four windows need 42/85/45's values before any naming, and even with them, the article defect at @96/@218/@1200 bars "erreur" as the uniform answer. The parent's positional-positive finding is untouched (this battery decides nothing about it); §7 intact; no standing/red-team verdict contradicted or downgraded; canonical-stream caveat stands (rows a1_02, a2_00, a7_00 unvalidated).

## Follow-ups proposed (all verified ABSENT from battery-queue.json)

1. `val-42-erreur` (P3) — test 42="reur" at @78 once 42's value names: "pour l'erreur" parses iff 42's other windows admit the "reur" syllable; bar: land at battery grade or fence the homophony cost.
2. `er-96-85-value` (P3) — once 85's value is named, test "qu'er[85]" as "qu'erreur" vs stem-composition; the A3 verb-stem class predicts the composition arm is dead.
3. `er-45-1200-rerun` (P3) — test "qui er[45]" at @1200 once 45's value names; the "qui [article] [noun]" frame needs the article between "qui" and the noun — if absent, the one-word route dies.

## Bookkeeping

- Queue: `er-word-lexicon` → status `verdict`, result `null`, 2026-10-09 (pre-write assert passed — was `queued`/verdictless; temp-file + rename; JSON re-validated; own entry only; no downgrade).
- Lock `locks/er-word-lexicon.lock`: created on start (no stale lock existed), deleted on completion (verified gone).
