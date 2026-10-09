# Battery report: er-45-1200-rerun

- Target id: `er-45-1200-rerun`
- Claim: test "qui er[45]" at @1200 once 45's value names; the "qui [article] [noun]" frame needs the article between "qui" and the noun — if absent, the one-word route dies.
- Date: 2026-10-09
- Worker: battery worker (subagent e5458670)
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, re-parsed in-session per `code/side-keyhunt/repair_parse.py`). Verified in-session: 1,847 pairs, 96 types, gloss-(i) crib "la premiere" (11 70 82 34 29 40) at 754 (a5_03) and 1034 (a6_03). `canonical.py` never used. R5005, sealed gates, red-team queue untouched.
- Lock note: no lockfile existed at start (no stale lock). Created `code/crowd17/next-token/locks/er-45-1200-rerun.lock` 2026-10-09T20:23:32Z; deleted on completion.

Terms (ASD-STE100): "one-word route" = reading "er[45]" as one word (the parent battery's "erreur" candidate: "er"+"reur"). "article" = a determiner licensed between "qui" and the noun. Offsets below are 0-based.

## Bar (verbatim, pre-registered before testing)

"If no article is licensed between 'qui' and the noun, the one-word route dies."

Numbered pass/fail clauses (restated before testing, not modified after):

1. **C1 (fire condition):** 45's value is named in the registry.
2. **C2:** An article is licensed between "qui" (64 at @1199) and the noun position (29 at @1200).

## Method

1. Read BATTERY-PROTOCOL.md first. Re-read battery-queue.json fresh before locking; target was `queued`, verdictless, lockless. Created the lock on start; deleted on completion.
2. Re-derived the repaired stream byte-exact per `code/side-keyhunt/repair_parse.py`. All @-offsets below are 0-based pair indices.
3. Standing premises used, not re-litigated: 29="er" (pencil GT); 64="qui" (promoted); 45="ce" (A11 HOLD, §7); 47="ce" (A4); 82="m" (pencil); 96="par" (promoted). French: 1841 diplomatic prose.

## Window-level evidence (byte-confirmed on the repaired stream)

- **@1195–1206** (row a7_00): `16 96 82 16 64 |29| 45 58 47 43 55 61` → "...(96) m(82) ...(16) qui(64) er[ce(45)] ...(58) ce(47) ...(43) ...(55) ...(61)".
- The "qui er[45]" window matches the parent report byte-for-byte: 64 at @1199, 29 at @1200, 45 at @1201.
- **64 and 29 are adjacent.** No token sits between "qui" and "er". The only determiner in the window is 45="ce" at @1201 — after 29, not between "qui" and the noun. 47="ce" at @1203 is two positions right.

## Per-clause results

- **C1 — fire condition: PASS.** 45="ce" is named in the registry under the A11 hold (§7: "Holds hold: ... 45='ce' (A11)"). The brief's gate is met; the test fires.
- **C2 — article licensed between "qui" and the noun: FAIL.** Nothing stands between 64 (@1199) and 29 (@1200). French grammar needs the determiner before the noun ("qui l'erreur", "qui cette erreur"); 45="ce" follows the noun and cannot license it from the right. The bar's antecedent is satisfied: no article is licensed between "qui" and the noun.
- **Independent kill arm (value contradiction):** the one-word route needs 45 to supply the "reur" syllable ("erreur" = "er"+"reur"). 45="ce" under the standing A11 hold contradicts this at battery level; the "dict" syllable rival for 45 does not supply "reur" either. "er"+"ce" = "erce", not a word. Re-reading 45 as "reur" would downgrade the A11 hold — barred under §7 and never-downgrade.
- **Rival one-word checks (same window):** *errer* infinitive ("qui erre") is the verb-lexeme arm, not the one-word noun route; the parent battery's strong positives for "qui erre" belong to the *errer* lexeme family and are untouched by this verdict (this battery kills only the noun "one-word route" at @1200).

## Verdict: KILL

The one-word route for "er[45]" at @1200 is dead. The bar's kill clause fired (no article between "qui" and the noun), and independently the named value 45="ce" contradicts the "reur"-syllable the route needs. No red-team verdict contradicted or downgraded; the A11 hold (45="ce") is affirmed, not weakened; §7 intact; canonical-stream caveat stands (row a7_00 unvalidated). Adverses: none listed on the target (queue `adverses: null`) — nothing to answer.

## Follow-ups proposed

None. This is a kill verdict; per BATTERY-PROTOCOL §4 the mandatory follow-ups apply to nulls only. The sibling follow-ups from the parent battery (`val-42-erreur`, `er-96-85-value`) stand on their own and are unaffected by this kill.

## Bookkeeping

- Queue: `er-45-1200-rerun` → status `verdict`, result `kill`, 2026-10-09 (pre-write assert passed — was `queued`/verdictless; target-id-unique temp file + atomic rename; JSON re-validated; own entry only; no downgrade).
- Lock `locks/er-45-1200-rerun.lock`: created on start (no stale lock existed), deleted on completion (verified gone).
