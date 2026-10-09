# Battery `locus-368-fullparse` — verdict: NULL (fence executed)

## Bar (verbatim, pre-registered from battery-queue.json)

> "resolve iff one grammatical full-clause parse with <=1 ungranted assumption; else fence"

Restated as numbered clauses (before testing):
- C1: one grammatical full-clause parse of @362–376 parses with <=1 ungranted assumption → resolve (PROMOTE).
- C2: else → fence the window with stated cause (NULL).

Adverses: none listed.

## Method

Re-derived the repaired stream in-session: 1,847 pairs / 96 types from `code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed like `code/side-keyhunt/repair_parse.py`. Asserts held (1,847 pairs, 96 types). `canonical.py` never used. 1841 diplomatic French only.

## Locus (byte-confirmed, 0-based, row-validated)

Row a2_06, @362–375; @376 = 82 is the first pair of row a2_07 (row join at 375|376):

| @ | cell | row | standing |
|---|------|-----|----------|
| 362 | 76 | a2_06 | ["noun","prom"] (masculine) |
| 363 | 47 | a2_06 | "ce" (prom) |
| 364 | 78 | a2_06 | "ver" (lead) |
| 365 | 48 | a2_06 | "e" (prom, letter tier) |
| 366 | 49 | a2_06 | unvalued |
| 367 | 61 | a2_06 | unvalued |
| 368 | 70 | a2_06 | "pre" (gt) |
| 369 | 17 | a2_06 | "fois" (prom) |
| 370 | 06 | a2_06 | "ent" (prom) |
| 371 | 21 | a2_06 | ["noun","cls"] |
| 372 | 65 | a2_06 | ["noun","cls"] |
| 373 | 63 | a2_06 | ["verb","cls"] |
| 374 | 29 | a2_06 | "er" (gt) |
| 375 | 85 | a2_06 | unvalued (verb-stem cls A3) |
| 376 | 82 | a2_07 | "m" (gt; word-initial of following word, "me") |

The claim's load-bearing trigram "48 49 61" sits at @365–367.

## Findings

Eight parse routes tested; all fail. C1 FAIL, C2 FIRES.

1. **"ce vere" fusion (@363–365):** 47='ce' + 78='ver' + 48='e' would need "vere" to be a French word. It is not. Kill-grade dead at the word level.
2. **Bare-'e' standalone (@365):** 48='e' left unattached strands a bare "e", which French does not license (adopted from `conj-20-642-subordinator` C1: bare-"e" standalone impossible; an "e"-initial word contradicts 20's class). Kill-grade dead.
3. **Right-attachment "e[49]…":** 48='e' as word-initial of a word starting with 49. 49 is unvalued — the word's identity requires naming 49 (ungranted assumption 1), and 61 remains unvalued beside it (ungranted assumption 2). Over budget.
4. **"[61]pre" fusion (@367–368):** the word "[61]pre" needs 61's letter content; 61 is unvalued (ungranted assumption 1), and the following "pre fois" adjacency is itself unexplained (ungranted assumption 2, see 5). Over budget.
5. **"pré fois" adjacency (@368–369):** 70='pre' + 17='fois' cannot compose: "préfois" is not a word, and a word ending in "pre" followed by "fois" has no licensed reading (contrast the "la première fois" crib, where 70 is followed by 82-34-29-40, not 17). Needs its own license — an additional ungranted assumption.
6. **3pl "ent" host (@369–370):** 06='ent' as a 3pl ending needs a verb stem; its predecessor is 17='fois' (a noun). "foisent" is not a word. Kill-grade dead.
7. **"[65-noun] [63]er [85]" infinitive frame (@372–375):** 65 is noun-class, so a bare infinitive "[63]er" after it is ungrammatical without à/de; 63 is verb-class, not noun-class, so "[63]er" cannot be a noun either. No licensed parse. Kill-grade dead at this window.
8. **Full-clause completeness:** even setting all of the above aside, no finite verb exists in @362–375 — 63 is verb-class but "[63]er" is infinitive-shaped. The span cannot be a complete clause under any reading. Kill-grade dead as a clause.

**Assumption budget:** the cheapest surviving route (route 3) needs 49 named AND 61 named AND the "pre fois" adjacency licensed — ≥3 ungranted assumptions. The bar allows ≤1. No route is within budget.

Not kill grade: the failures rest on unvalued cells (49, 61, 85) — naming 49 and 61 (red-team/value acts) could revive routes 3–4, and a named finite 63 would supply the predicate. So the window is fenced, not killed.

## Verdict: NULL

C1 fails; C2 fires — @362–376 is fenced as an undecidable-at-battery-grade full clause with stated cause: the "48 49 61" trigram is unresolvable (48='e' forces left-fusion into the non-word "vere" or right-attachment into two unvalued cells), the "pre fois" adjacency is unlicensed, and no finite predicate exists.

## Follow-ups proposed (all verified ABSENT from battery-queue.json)

1. `val-49-61-pair` (P3) — name 49's and 61's classes at the @365–367 trigram; the load-bearing unknown for this window.
2. `prefois-368-adjacency` (P3) — census "70 17" ("pre fois") adjacency stream-wide; a licensed collocation revives the mid-clause.
3. `fin63-373-rerun` (P3) — test 63's finiteness at @373; finite-63 supplies the clause's missing predicate.

## Standing state

No standing/red-team verdict contradicted or downgraded (48='e' prom, 70/29/82 gt, 17='fois' prom, 76=[noun,prom], 06='ent' prom, 63=[verb,cls], 65/21=[noun,cls] all adopted as premises; §7 intact). Canonical-stream caveat stands (rows a2_06/a2_07 offsets unvalidated).

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-locus-368-fullparse.md`
- Queue: `locus-368-fullparse` → `status: verdict`, `result: null`, 2026-10-09 (pre-write assert passed — was queued/verdictless; temp-file + rename; JSON re-validated from disk; own entry only; no downgrade)
- Lock created on start, deleted on completion (verified gone). R5005, sealed gates, red-team adjudication queue untouched.
