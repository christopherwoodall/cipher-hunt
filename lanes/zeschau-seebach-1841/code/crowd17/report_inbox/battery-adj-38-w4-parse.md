# Battery adj-38-w4-parse — verdict: KILL (no parse survives; W4 fenced with stated cause)

**Target:** `adj-38-w4-parse` (P3)
**Date:** 2026-10-09
**Worker:** battery protocol §1–§8 followed. Lock `locks/adj-38-w4-parse.lock` created on start, deleted on completion. `canonical.py` never used. R5005, sealed gates, red-team adjudication queue untouched.

## Bar (verbatim, pre-registered)

> "Resolve W4's 'qui 52 38 ce 86' with 38's class open; fence W4 if no parse survives."

**Numbered clauses (fixed before testing):**
- C1: W4's 'qui 52 38 ce 86' resolves with 38's class open — at least one parse survives under standing values.
- C2: If no parse survives, W4 is fenced with stated cause.

## Method

Stream re-derived in-session from `code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py` (byte-exact `[s[i:i+2] for i in range(o, len(s)-1, 2)]`). Result: 1,847 pairs / 96 types. n(38) = 7, byte-confirmed at 0-based @384/@826/@1113/@1343/@1469/@1650/@1828 — matching the brief. All @-offsets below are 0-based queue convention.

Standing values used as premises only (never re-litigated): 11="la", 82="m", 29="er", 40="e", 46="que" (pencil GT); 87="ce", 64="qui", 96="par", 17="fois", 79="tout" (A5), 00="pour" (A9), 84="on" (A15), 47="ce" (A4 allophone tier); 59="est" provisional; 30="pas" battery-promoted; 86 INF-class (A9 class-level); 65="noun" class (R18-001 ratified); 38 = verb-form class-level (battery-noun26-38-profile, PROMOTE, 2026-10-09 — adopted as standing, not re-litigated). 52 is the §7 split candidate (adverb/adjective arms both live).

Scope note: the target brief predates battery-noun26-38-profile (2026-10-09, same day), which promoted 38=verb-form and fenced this window for verb-form and predicative classes. That promotion is adopted; the bar's "38's class open" is tested across the full candidate set anyway {finite verb, participle, modal, adjective, determiner, noun} so the fence is complete, not class-conditional.

## Window-level evidence

**W4 @1343 (a7_05, mid-row):** stream bytes @1341–1345 = `64 52 38 47 86` = "qui(64) [52] [38] ce(47) [86]". Census (re-derived, repaired stream):
- `64 52 38 47 86` x1 stream-wide (only here).
- `38 47` x1 stream-wide (only here).
- `47 86` x1 stream-wide (only here): "ce [86-INF]" is a hapax — no parallel "ce + INF-class-86" bigram exists anywhere else to license a parse.
- `52 38` x2: @383 (W1) and @1342 (W4). `64 52` x2.
- Left edge: @1337–1340 = `64 60 08 65` ("qui [60] [08] [65]"), a separate clause; W4's qui @1341 opens a new relative clause. No byte-level interference either way.

**Exhaustive parse test, per candidate class of 38** (standing values only; rival value assumptions that would contradict grants are excluded per bullet R, below):

1. **38 = finite verb** (promoted class), 52 = adverb: "qui [52-adv] [38-V-fin] ce [86-INF]" parses to the verb, then strands `ce 86`: 47='ce' granted, 86 INF-class — "ce" can be neither subject of a non-finite verb, nor post-verbal object ("ce" after a finite verb is ungrammatical outside imperatives), nor head of "ce [INF]" (ungrammatical). FAIL.
2. **38 = finite verb, 52 = adjective**: "qui [52-adj] [38-V]" — adjective immediately after qui with no head — ungrammatical. FAIL.
3. **38 = past participle**: "qui [52-adv] [38-pp]" — participial relative without auxiliary — ungrammatical in 1841 French. FAIL.
4. **38 = modal** (verb-form leg at W5): identical to (1) — the tail `ce 86` is class-independent of 38's inflection. FAIL.
5. **38 = adjective** (locus-level W2/W3 readings per parent NULL): "qui [52-adv] [38-adj] ce [86]" — adjective intervening between qui and the subject "ce" with no byte-evidenced parenthetical — ungrammatical; and qui is left verbless (86 INF-class cannot be the clause verb). FAIL.
6. **38 = determiner**: "qui [52] [38-det] ce…" — determiner before "ce" with no nominal — ungrammatical; determiner-38 is kill-grade dead at W3 in any case. FAIL.
7. **38 = noun**: "qui [52] [38-noun] ce…" — relative qui with no finite verb in the clause — ungrammatical. FAIL.
8. **52–38 as prenominal-adjective unit** (queued val-52-38-unit, not duplicated): as adjective — same failure as (5); as nominal — same failure as (7). FAIL.
9. **Clause-boundary rescues**: boundary at 52|38 strands "qui 52" verbless (neither 52 arm is a verb). Boundary at 38|47: "qui [52-adv] [38-V]." complete, then "Ce [86-INF]…" — subject "ce" with non-finite verb — ungrammatical. Boundary at 64|52 strands "qui" alone. All FAIL.

**R. Excluded rescues (would contradict standing grants — not battery work):** 47='se' (A4 grant stands; frame-qui-47 killed the qui-se alternative at those windows); 86 as finite verb (A9 INF-class grant stands); 64≠'qui' (promoted standing). Invoking any of these is inventing data, not parsing.

## Per-clause pass/fail

- **C1 — FAIL at kill grade.** Across all six candidate classes of 38 plus the 52–38-unit variant, plus every byte-plausible clause boundary, the window admits zero grammatical parses under standing values. The failure localizes to the `38 47 86` tail (both `38 47` and `47 86` are stream hapaxes): with 47='ce' granted and 86 INF-class, "ce" has no slot after any 38 reading, and non-verbal 38 leaves "qui" verbless. The window forces the resolve-claim false.
- **C2 — FIRES.** W4 is fenced with stated cause: no parse survives; the fence holds on the canonical (repaired) stream per protocol. The fence is consistent with both prior batteries — battery-adj-37-385-gate's NULL fenced W4 under determiner/adjective (its fence is not contradicted: those failures re-derive at bullets 5–6), and battery-noun26-38-profile's PROMOTE fenced W4 under verb-form/predicative (its fence re-derives at bullets 1–4). Nothing downgraded, nothing re-litigated.

## Verdict: KILL

The claim "W4's 'qui 52 38 ce 86' can be resolved with 38's class open" is falsified at this window — no parse survives with 38's class open under standing values. W4 @1343 is fenced with the stated cause above. No standing verdict contradicted or downgraded; no red-team escalation (no red-team verdict exists on 38 or on this window).

**Re-open conditions (not follow-ups — verdict is kill, not null):** the fence re-opens iff a standing grant changes underneath it — 52's class resolving (queued val-52-38-unit touches @1342; the unit variant is covered at bullet 8 but a full unit re-parse is its venue), 86's class resolving beyond INF-class, or 47's allophone tier adjudicated. Note: battery-noun26-38-profile proposed `w4-38-1343-revisit` (P4) as the conditional re-test; it is NOT yet in the queue as of this run — flagged to the supervisor for ingestion rather than duplicated here.

## Bookkeeping

- Lock `code/crowd17/next-token/locks/adj-38-w4-parse.lock` created on start, deleted on completion.
- Queue update: temp-file + rename on `battery-queue.json`, own entry only; pre-write assert confirmed queued/verdictless; JSON re-validated after write.
- Canonicality caveat stands (68 of 70 upstream row offsets unvalidated; verdict holds on the canonical stream per protocol).
