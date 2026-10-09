# Battery verdict: val-81-55-collocation

## Bar (verbatim, pre-registered)

"resolve iff 81's class named at battery grade from the '55 81' collocation with stated values"

Restated as numbered clauses:
- **C1:** 81's class is named at battery grade, and the naming derives from the '55 81' collocation (not from other legs).
- **C2:** Only stated values are used (no invented values, no unratified extensions).
- **Adverses:** (a) 81's value must not be invented; (b) @1594 left-edge context fences as fallback.

## Method

1. Read BATTERY-PROTOCOL.md first. Created `code/crowd17/next-token/locks/val-81-55-collocation.lock` on start (agent id 934f8802-ef31-461e-bd3d-7ccb2cde2453 + UTC timestamp 2026-10-09T21:30:30Z); no pre-existing lock.
2. Re-derived the repaired stream in-session: `data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `repair_parse.py` (1,847 pairs / 96 types; asserts held).
3. `canonical.py` never used. R5005, sealed gates, red-team adjudication queue untouched.
4. Offsets below are 0-based unless marked 1-based (lane reports use 1-based; conversion stated).

## Window-level evidence

'55 81' bigram: exactly **6x** stream-wide (0-based 55-position; ±4 context):

| 55@ (0-based) | 55@ (1-based) | row | context |
|---|---|---|---|
| 25 | 26 | a1_00 | 47 33 **55 81** 00 34 24 30 |
| 523 | 524 | a3_00 | 70 91 77 06 **55 81** 97 47 44 59 |
| 550 | 551 | a3_01 | 46 24 47 46 **55 81** 00 86 59 34 |
| 1085 | 1086 | a6_05 | 89 24 02 **55 81** 00 33 79 80 |
| 1094 | 1095 | a6_06 | 80 06 43 07 **55 81** 06 29 67 86 |
| 1671 | 1672 | a8_05 | 06 91 11 78 **55 81** 92 60 03 39 |

## Standing values used (adopted, not re-litigated)

- **55 = verb-class** at @576/@1167 **within "prend"** (`val-52-55-class` PROMOTE, 2026-10-09; `seg-55-61-94-letters` PROMOTE: 55+61 = "prend"). The "prend" spelling is attested **only where 55+61 compose** (@576, @1167, @1205).
- **Uniform verb-class for 55 is FENCED at @523 and @1671** (2026-10-09, structural value-independent failures) — two of the six "55 81" windows. 55's uniformity is an open §7 split question ("55 'prend' verb windows versus other incompatible windows").
- **81 = masculine abstract noun, class-level, value open** (`noun-81` PROMOTE, battery grade, 2026-10-09). That report explicitly considered the "55 81" collocation and left it neutral: "55's value is open, so it neither supports nor contradicts the noun reading."

## Findings

**C1 — FAIL.** The collocation does not name 81's class at battery grade, on four independent grounds:

- **F1 — the "prend" value does not transfer.** The only route from "55 81" to a class naming is 55="prend" (transitive "takes") → 81 occupies the direct-object slot → noun. But "prend" is spelled only at 55+61 windows. At "55 81" windows 55 stands alone; extending the "prend" value there assumes 55's uniformity, which is the undecided §7 split. A battery worker cannot make that extension (§3/§7).
- **F2 — "V [81]" underdetermines the class.** Even granting 55=verb-class at the four non-fenced windows, a finite verb followed by a bare word admits noun (DO), adverb, predicative complement, and other roles. No unique class is forced without the specific transitive value — which F1 blocks.
- **F3 — the collocation has no uniform left element.** At @523 and @1671 (2 of 6 windows), 55's verb-class is fenced. The bigram "55 81" is therefore heterogeneous across its six occurrences; no single frame can be read off it.
- **F4 — the class is already named elsewhere.** `noun-81` (PROMOTE, same day) names 81 as masculine abstract noun on independent legs ("le [81]" x3, "81 pour [INF]" x2). This target's bar demands a naming *from the collocation*; the collocation supplies no independent leg, so there is nothing to resolve here that is not already standing.

**C2 — PASS (vacuous).** No values were invented; the test stopped at the standing values.

**Adverse (a) — honored.** No 81 value named or proposed.

**Adverse (b) — addressed.** The claim's payoff ("a standing 81 class may constrain the @1594 left edge") is already served by the standing `noun-81` PROMOTE: at 1-based @1593-1594 ("08 81" = "t [81-noun]"), the word-tier noun forces the "08 | 81" word boundary. This target adds no new constraint; the dedicated left-edge test is proposed as follow-up 1 rather than executed here (out of this bar's scope).

## Scope

Fences only the collocation-to-class route: "55 81" x6 is **consistent with but not probative of** 81's noun class at battery grade. Untouched: `noun-81`'s PROMOTE (81 = masculine abstract noun stands), `val-52-55-class`, `seg-55-61-94-letters`, the @523/@1671 verb-class fences, the 55-uniformity §7 split question, 81's open value, §7. No standing or red-team verdict contradicted, downgraded, or re-litigated. Canonical-stream caveat stands (rows unvalidated).

## Verdict: NULL

The '55 81' collocation does not name 81's class at battery grade. 81's class remains as standing: masculine abstract noun per `noun-81` (battery PROMOTE, red-team ratification pending).

## Follow-ups (all verified ABSENT from battery-queue.json; left for supervisor)

1. `leftedge-08-81-1594` (P4) — apply `noun-81`'s standing noun class to the "08 81" contact at 1-based @1593-1594 ("t [81-noun]"); decide whether the word boundary "08 | 81" is forced (the actual payoff this target's claim wanted).
2. `class-55-5581-windows` (P4) — name 55's class at the four non-fenced "55 81" windows (0-based @25, @550, @1085, @1094); if 55="prend" (transitive) is licensable there *without* assuming 81's class, 81=noun gains an independent leg.
3. `colloc-55-81-uniform-rerun` (P4, gated) — re-run this exact bar iff the red team resolves 55's uniformity (55="prend" globally); the bar then tests "prend [81]" x6 as DO frames.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-val-81-55-collocation.md` (this file).
- Queue: `val-81-55-collocation` → status `verdict`, result `null`, date 2026-10-09 (pre-write assert passed — was queued/verdictless; target-id-unique tmp `battery-queue.json.val-81-55-collocation.tmp` + atomic rename; disk re-validated; own entry only; no downgrade; no tmp leftover).
- Lock: `code/crowd17/next-token/locks/val-81-55-collocation.lock` created on start (no stale lock), deleted on completion (verified gone).
- `canonical.py` never used; R5005, sealed gates, red-team adjudication queue untouched.
