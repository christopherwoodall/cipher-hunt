# Battery report: telle-52-37-rival (KILL — "telle" excluded)

**Target:** telle-52-37-rival — admit/exclude the marginal fourth candidate "telle" under the same bar
**Worker:** battery (agent ca1043c1-cc7d-441a-bdf8-6dd6a20964ef) | **Date:** 2026-10-09
**Stream:** repaired 1,847-pair / 96-type parse (data/upstream-ct_R5005.txt + code/side-keyhunt/repaired_offsets.json, parsed per repair_parse.py; asserts hold). Never canonical.py. No R5005 touched. No data invented. Every @-offset re-derived (0-based).

## Context (adopted, not re-litigated)

battery-adj-52-37-value (2026-10-08, NULL) tied {même, seule, dite} at the two Type-A 52-37 adjective windows; its F2 proposed testing the marginal fourth candidate "telle" (graded marginal by unit-52-37-name). This battery is that F2.

## Bar (verbatim from battery-queue.json)

> test "telle" against @1124/@1722 with <=1 ungranted assumption; exclude or record

Numbered clauses (pre-registered before testing):

1. @1124 (a6_07): "telle" parses as the Type-A 52-37 adjective unit with ≤1 ungranted assumption.
2. @1722 (a8_07): "telle" parses as the Type-A 52-37 adjective unit with ≤1 ungranted assumption.
3. Admit iff both pass; exclude with stated cause iff either fails.

## Method

1. Re-derived the repaired stream byte-exactly (1,847 pairs, 96 types; asserts hold). Never used canonical.py.
2. Located both Type-A windows: @1124 (a6_07) and @1722 (a8_07). Both carry the byte-identical 5-gram **"06 11 52 37 43"** at @1122–1126 / @1720–1724 — i.e. "…ent la [52-37] [43]…" with banked 11="la" immediately before the unit in both windows.
3. Tested the Type-A parse "[verb-ent] la [52-37='telle'] [43-head-noun]" under standing values only (no ungranted assumptions): 11="la" (banked GT), 06="ent" (promoted), 43 = noun (frame-43 battery; value open).

## Window-level evidence

- **@1124 [a6_07]:** `… 06 11 [52 37] 43 00 86 52 37 86 …` → "…ent la [telle] [43] pour [86-INF] …"
- **@1722 [a8_07]:** `… 06 11 [52 37] 43 98 39 88 24 …` → "…ent la [telle] [43] [98] a/a [88] …"

## Finding

**"telle" is EXCLUDED at kill grade at both windows.**

"telle" is a demonstrative adjective ("such"). French determiners do not stack: **"la telle [noun]" is ungrammatical** — the definite article "la" and the demonstrative "telle" cannot co-occur in the same NP. This is a period- and register-independent grammatical fact (it holds in Old, Classical, and 1841 French): "tel/telle" is determiner-like and excludes the article.

Rescue routes checked and closed:

1. **Clause boundary between "la" and "telle"** ("…ent la | telle [43]…"): impossible — "telle [43]" is then determiner-less and "la" is stranded with no head. No French parse exists.
2. **"telle" as a non-demonstrative form**: no French verb "teler"/"teller" exists, so no past-participle reading; no noun or adverb reading of "telle" fits prenominal position after "la". No compound "telle-X" is attested.
3. **43's value**: irrelevant. The failure is article-adjective incompatibility, reached before 43's head noun is ever consulted. This exclusion is therefore **43-independent** — unlike the triple's tie, which was conditional on 43 ∈ {condition, mesure}.

Because both windows share the byte-identical 5-gram, there is zero distributional variance: the same failure fires twice.

## Per-clause pass/fail

1. **@1124 — FAIL at kill grade.** "la telle [43]" ungrammatical under standing values; all rescues closed.
2. **@1722 — FAIL at kill grade.** Identical failure (byte-identical frame).
3. **Admit condition not met; exclude with stated cause: "telle" cannot follow banked "la".**

## Adverses

- None listed. The F2 adverse ("'telle' prenominal = 'such', archaic-leaning; 43's value open") is answered: the "such" reading is exactly what was tested, and the exclusion does not depend on 43's value.

## Verdict

**KILL.** The "telle" candidacy for the Type-A 52-37 adjective unit is excluded at kill grade at both windows. The candidate set reverts to {même, seule, dite} — this battery does not discriminate among the triple (adj-52-37-value-rerun and dite-52-37-anaphora remain the queued owners of that question). No standing or red-team verdict contradicted or downgraded; §7 intact.

**Caveat:** canonicality caveat stands — both windows sit on offset-0 rows with unvalidated upstream offsets; the kill holds on the canonical stream per protocol. The byte-identical 5-gram makes it robust to most phase perturbations short of dissolving the frame itself.

No follow-ups proposed (kill, not null — the F2 question is closed; the triple's question is already owned by queued targets).

## Bookkeeping

- Lock `code/crowd17/next-token/locks/telle-52-37-rival.lock` created on start (agent id + UTC), deleted on completion.
- Queue update: temp-file + rename on `battery-queue.json`, own entry only; pre-write assert confirmed queued/verdictless; JSON re-validated after write.
- No standing verdict contradicted or downgraded. R5005, sealed gates, red-team adjudication queue untouched.
