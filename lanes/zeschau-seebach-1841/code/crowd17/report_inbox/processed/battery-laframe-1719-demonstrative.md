# Battery report: laframe-1719-demonstrative

**Target:** `laframe-1719-demonstrative` (priority 3)
**Date:** 2026-10-09
**Worker:** 4efd1ef5-19ea-4339-84c5-5c26e9cca94d
**Verdict:** PROMOTE

## Bar (verbatim from queue)

"(a) the frame parses cleanly with 68 nominal; (b) 06='ent' composing noun-finally does not violate the ent-06 letters-tier promote"

## Bar restated as numbered clauses (frozen BEFORE testing, not modified after)

- **C1:** "ce [68ent] la" at @1718–1721 parses cleanly as a demonstrative+noun frame with 68 nominal, under standing values, with zero new assumptions.
- **C2:** 06='ent' composing noun-finally does not contradict the ent-06 promote's letters-tier license.

Verdict rule: promote iff C1 and C2 both pass; kill iff a window forces the frame false; null otherwise.

## Method

Read BATTERY-PROTOCOL.md first. Created `code/crowd17/next-token/locks/laframe-1719-demonstrative.lock` on start (agent id + 2026-10-09T10:32:20Z); no stale lock present. Re-derived the repaired 1,847-pair / 96-type stream in-session from `data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py` (asserts held: 1,847 pairs, 96 types). `canonical.py` never used. R5005, sealed gate instances, red-team adjudication queue untouched.

Standing values used (not re-litigated): pencil 11=la, 29=er, 40=e, 46=que, 70=pre, 82=m, 34=i; granted 87=ce, 64=qui, 96=par, 17=fois, 79="tout" (A5), 00="pour" (A9), 84="on" (A15), 47="ce" (A4, allophone tier); provisional 59=est, 77="le"; battery-promoted 98="vient" (finite clause-head), 06="ent" (ent-06, letters/syllable tier), 68 nominal-class (val-68-noun-sweep, battery grade).

## Window-level evidence (byte-exact, 0-based @)

Locus @1718–1721, row a8_06/a8_07:

| @ | group | row | value |
|---|-------|-----|-------|
| 1717 | 64 | a8_06 | qui (grant) |
| 1718 | 47 | a8_06 | ce (A4 grant) |
| 1719 | 68 | a8_07 | nominal class (battery promote) |
| 1720 | 06 | a8_07 | "ent" (ent-06 letters tier) |
| 1721 | 11 | a8_07 | la (pencil GT) |
| 1722 | 52 | a8_07 | open |
| 1723 | 37 | a8_07 | predicative frame (A1) |
| 1724 | 43 | a8_07 | open |
| 1725 | 98 | a8_07 | vient (battery promote) |

Distributional facts (re-derived):
- "47-X-06-11" frames stream-wide: exactly **1** (@1718, X=68). One-window parse test, as the bar's note anticipates.
- "68-06" bigram: exactly **1** (@1719).
- "11-52" bigram: **3×** (@1006, @1123, @1721) — "la [52]" is recurrent, not a rescue.
- "11-52-37-43" 4-gram: **2×** byte-identical (@1123, @1721) — 'la' as determiner of a recurrent formula.

## C1: the frame parses cleanly with 68 nominal — PASS

Parse: "qui(64) ce(47) [68ent], la(11) [52] [37] [43] vient(98) [39] [88]..."

1. "ce [68ent]" — demonstrative (47, A4 grant) + noun (68, nominal-class battery promote) with "-ent" ending. French -ent nouns are a licensed class ("moment", "accident", "serment"). Clean.
2. "la [52] [37] [43]" — "la" (pencil GT) as determiner of the recurrent "11-52-37-43" formula (byte-identical at @1123; "11-52" 3× stream-wide). Clean, formula-supported, zero new assumptions.
3. Junction "ce [68ent] | la [52]...": the demonstrative NP closes (dislocated topic or clause constituent); "la [52] [37] [43]" heads the subject NP of finite "vient" @1725. No ungrammatical junction anywhere in the window.
4. The rival verb+object parse ("[68]ent la" as verb+object) is void, not merely unlicensed: battery-stem-68-id killed its condition (68 verb-stem dead at kill grade via @1442 "[68] est" and @884 "tout [68]"), and it would need 47='se' against the A4 'ce' grant. The demonstrative+noun parse is the unique survivor.

## C2: noun-final 06='ent' vs the ent-06 promote — PASS (no violation)

The ent-06 promote licenses 06 as the letters/syllable "ent" (fork V; also used word-initially in "entreprenne" @346). Noun-final composition ([68]+ent) uses the same letters value in a different compositional role — the promote establishes the VALUE, not a verb-only role. Its @1719 leg was explicitly conditional on 68=verb stem, which failed at battery grade (stem-68-id), so the promote makes no claim at @1719 that noun-final composition could contradict. No standing verdict is contradicted or downgraded.

## Per-clause results

- C1 (clean demonstrative+noun parse, 68 nominal): **PASS**
- C2 (no ent-06 violation): **PASS**

Adverses: none listed. §5 check: no red-team verdict on 68's class or 06's value exists (R18-023/R18-024 are census/typicality findings with no value claims); the battery-grade 68-nominal promote (val-68-noun-sweep) is adopted as the bar's stated premise, not re-litigated. §7 intact (68 is not 67; no polyvalence declared).

## Verdict: PROMOTE

The rival parse "ce [68ent] la" at @1718–1721 is a clean demonstrative+noun frame under 68 nominal, and 06='ent' composing noun-finally is consistent with the ent-06 letters-tier promote. 68's VALUE remains open (this battery names no value); the "47-?-11" frame is a stream singleton, so no distributional generalization is claimed.

## Supervisor note (not a finding)

`noun-68-value-id` (proposed by battery-stem-68-id): name 68's nominal value from the "-ent" noun candidate pool, using @1442 "[68] est [37]" and @114/@504 "[68] suite" legs. Still the sharpest next step on 68.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-laframe-1719-demonstrative.md` (this file).
- Queue: `laframe-1719-demonstrative` queued → verdict/promote via temp-file + rename, own entry only; pre-write assert confirmed no prior verdict.
- Lock `laframe-1719-demonstrative.lock`: created on start, deleted on completion.
- R5005, sealed gate instances, red-team adjudication queue untouched.
