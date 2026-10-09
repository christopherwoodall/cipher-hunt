# Battery report: w1-342-tail-parse

- Target id: `w1-342-tail-parse`
- Claim: "full-context parse of W1 tail "87 01 06 70 12 94 74 67 78" (0b@344-352); coordinate with (do not re-litigate) the killed 06 "entreprenne" leg and ci-bound-01 @345 fence"
- Date: 2026-10-09
- Worker: battery worker (subagent 6d1d1874-7630-41ea-b572-23f6dd7281c8)
- Stream: repaired 1,847-pair / 96-type parse re-derived in-session from `data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json` (parsed per `code/side-keyhunt/repair_parse.py`); asserts held (1,847 pairs, 96 types). All @-offsets 0-based. `canonical.py` never used. R5005, sealed gates, red-team adjudication queue untouched.
- Lock: `code/crowd17/next-token/locks/w1-342-tail-parse.lock` (created at start, deleted on completion; no prior lock existed).

## Bar (verbatim, pre-registered before testing)

"(a) produce a grammatical parse with <=1 unstated assumption, or (b) fence W1 87-scope as a 06-driven residual with stated cause"

## Bar restated as numbered pass/fail clauses

- **C1 (grammatical parse):** produce a grammatical parse of the full tail "87 01 06 70 12 94 74 67 78" using at most one unstated assumption (no invented values, no re-litigation of standing kills/grants). PASS iff the parse closes grammatically.
- **C2 (06-driven residual fence):** if C1 fails, fence W1's 87-scope as a 06-driven residual with stated cause — show the window breaks on the 06 cell under every licensed 01 reading (free 'ce' / bound 'ceci' / open), so 87's scope is undecidable at battery grade from this window. PASS iff the fence's cause is stated and 01-value-independent.

## Standing state adopted (not re-litigated)

- 87='ce' granted; 06='ent' single value (ent-06 PROMOTE; 06-forces-84; ent-06-host-census decision rule: finite -ent ending iff left neighbor is a verb stem, else syllabic 'ent').
- The 06 "entreprenne" leg is KILLED (spell-06-entre, 2026-10-09): 06-70-12-94 spells "entprenne" under every licensed value (06='ent' + 70='pre' pencil GT + 12='n' promoted letter + 94='ne' R17-001 STRONG LEAD) — not French, kill grade. "06-70" is stream-hapax.
- ci-bound-01 (NULL): @345 (0b) "87 01" fenced as 06-driven residual ("ce [01] entreprenne [74]..." does not parse); breakage NOT -ci-specific.
- residual-345-06 (NULL): @345 fenced as 06-driven residual — stemless 'ent' + "pre"+"n"+"ne" complex, no "que"-governor in ±20, kill-grade-dead "ce qui par" left edge (edge-340-31-14), failure 01-value-independent.
- 67='et'/'veut' polyvalence with §7 positional rule (67="veut" iff follower infinitive-shaped); 78 open here → 67='et' default.
- 01 general 'ci' killed (ci-01-value); 31=verb class, 14 verb candidacy fenced lane-wide (edge-340-31-14).

## Method

1. Read BATTERY-PROTOCOL.md in full first; created lock on start.
2. Re-derived the repaired stream in-session; byte-verified the tail: 0b@344–352 = `87 01 06 70 12 94 74 67 78` exactly (row a2_05 pos 19–26 through 74, then a2_06 `67 78 40 92 98 ...`); wider context 0b@338–358 = `31 14 45 64 96 43 | 87 01 06 70 12 94 74 | 67 78 40 92 98 92 47 11`.
3. Verified the "06-70-12-94" 4-gram is stream-hapax (@346 only, 0-based) — no distributional license for any alternative segmentation.
4. Exhausted grammatical-parse candidates (P1–P8 below) against standing values only; counted unstated assumptions.

## Window-level evidence (0-based @)

0b@344–352: `87(ce) 01 06(ent) 70(pre) 12(n) 94(ne) 74 67(et) 78`
= "ce [01] ent pre-n-ne [74] et [78]"
Left context: @338–343 = `31 14 45(ce) 64(qui) 96(par) 43` ("[31] [14] ce qui par [43]", left edge kill-grade-dead per edge-340-31-14, adopted).
Right context: @353–358 = `40(e) 92 98 92 47(ce) 11(la)`.

Note: @346's left neighbor (01 @345) is open, not a verb stem → per the 06-attachment rule 06 is syllabic 'ent' here, not a finite ending. This window's 06 reading is therefore exactly "entprenne" — the killed verb-ID leg's non-word — with no finite-ending alternative available.

## C1: grammatical parse — FAIL

Candidate parses tested against standing values:

- **P1 (free 'ce' + syllabic 'ent'):** "ce [01] entprenne [74] et [78]" — "entprenne" is not French (kill grade, spell-06-entre C3). Dead.
- **P2 (bound "ceci"):** "par [43] ceci entprenne [74] et [78]" — non-word in the verb slot; plus "ceci" + bare 'ent' is independently ungrammatical (ci-bound-01 W3, adopted). Dead.
- **P3 ("ce qui par" left-edge rescue):** kill-grade-dead per edge-340-31-14 (adopted, residual-345-06 Attempt B). Dead.
- **P4 (elided-"que" subjunctive governor):** requires the verb leg, which is killed; byte sweep @320–370 shows zero 46='que' cells (adopted from residual-345-06). Dead.
- **P5 ("ent | prenne" word split):** "ent" is not a French word (spell-06-entre, adopted). Dead.
- **P6 ("01-06" unit, 01="entr"/06="e"):** contradicts promoted 06='ent' single value; pure invention (spell-06-entre, adopted). Dead.
- **P7 ("74 et 78" fragment tail):** "[74] et [78]" is only grammatical inside a clause whose left side parses; the left side contains the 06-driven non-word. Even as a fragment it needs licensed values for 74 and 78 (both open) — and the parse as a whole needs 01's value plus a licensed 06-70-12-94 reading.
- **P8 (row boundary as clause boundary):** rows are upstream artifacts, not clause boundaries; nothing grammatical emerges on either side of the a2_05/a2_06 seam.

Assumption count: any grammatical parse requires a licensed value for 01, a licensed value for 74, a licensed value for 78, and a licensed reading of 06-70-12-94 — ≥4 unstated assumptions, and the last is kill-grade-barred rather than merely unstated. C1 fails at kill grade on the 06-70-12-94 non-word; the bar's ≤1-assumption budget is exceeded by every surviving candidate before grammar is even reached.

## C2: 06-driven residual fence — PASS

Fence: W1's 87-scope (free 'ce' vs bound 'ceci') is undecidable at battery grade from this window. The window breaks on the 06 cell under every licensed 01 reading:

1. **Cause (post-spell-06-entre-kill):** 06-70-12-94 = "entprenne", a non-word under every licensed value (06='ent' PROMOTE single value; 70='pre' pencil GT; 12='n' promoted letter; 94='ne' STRONG LEAD). The "entreprenne" verb-ID leg is killed (do not re-litigate). 06's left neighbor (01) is open → syllabic 'ent' per the attachment rule; no finite-ending reading is available at @346. The "06-70" bigram is stream-hapax, so no distributional rescue exists.
2. **01-value-independence:** the breakage is identical under 01='ceci', 01='ce', and 01=open — a non-word in the verb slot kills every reading identically (adopted from residual-345-06's value-independence check). The "ce qui par" left edge is kill-grade-dead and the ±20 window contains no 46='que' governor (both adopted).
3. **87-scope consequence:** because the failure is 06-driven and 01-independent, nothing in this window discriminates 87='ce' (free demonstrative) from 87-01="ceci" (bound). 87's scope at W1 is fenced — not as a -ci residual (ci-bound-01's fence stands), but as a 06-driven residual whose cause is the "entprenne" non-word, the dead left edge, and the absent governor.

Dependency note: the fence uses 06='ent' and the 06-attachment rule throughout. If ent-06's grant is ever overturned, @345 re-opens (same dependency as ci-bound-01's and residual-345-06's fences).

## Per-clause results

- **C1 (grammatical parse, ≤1 unstated assumption): FAIL** — kill-grade on the 06-70-12-94 non-word (P1–P6 dead; P7/P8 exceed the assumption budget before closing).
- **C2 (fence 87-scope as 06-driven residual): PASS** — cause stated: "entprenne" non-word at @346–349 (syllabic 'ent', no finite-ending reading available) + kill-grade-dead "ce qui par" left edge + zero 46='que' in ±20; failure 01-value-independent, so 87's scope is undecidable from this window.

## Verdict: NULL (fence executed per the bar's else-branch)

Precedent: residual-345-06 (NULL) executed the same else-branch on the shorter @345 window; this target's deliverable is the fence with the cause updated for the spell-06-entre kill (the residual is now a bare non-word, not a stemless-'ent'-before-"prenne" verb frame). No standing or red-team verdict contradicted or downgraded; §7 intact (67='et' at @351 by the positional rule, unneeded for the fence).

## Adverses

None listed. Adopted without re-litigation: spell-06-entre (KILL), ci-bound-01 (NULL), residual-345-06 (NULL), edge-340-31-14 (left-edge kill), 06-forces-84 / ent-06-host-census (06='ent' single value + attachment rule), ci-01-value (01 general 'ci' killed).

## Follow-ups proposed (both verified ABSENT from battery-queue.json)

1. `ci345-fence-refresh` (priority 3) — refresh ci-bound-01's @345 fence statement-of-cause post-spell-06-entre-kill. That report's W3 mechanism ("ceci" + bare '-ent' verb ending) is stale: with the verb-ID leg killed and 06's left neighbor open, 06 at @346 is syllabic 'ent' per the attachment rule and no finite-ending reading is available — the cause is now the "entprenne" non-word, not a stemless ending. Battery-grade bookkeeping; the fence's verdict stands, only its stated mechanism needs updating. Bars: (a) re-state the @345 fence cause using only standing values post-kill; (b) confirm the fence's 01-value-independence is preserved under the new mechanism; (c) flag any dependency change for the red-team docket.
2. `tail-74-78-frame` (priority 3) — test whether the post-residual tail "74 [et] 78" (0b@350–352) is salvageable as a fragment: 74's follower profile (n=34), 78's predecessor profile (n=31), and any window where 74 takes a verb or noun class that could license a fragment after the 06-driven break. Discriminating test: if a licensed "74 et 78" frame exists, the W1 fence's scope narrows to @344–349; if none exists, the residual extends to @352. Bars: (a) full 74/78 contact census with class assignments; (b) state whether the tail survives the residual independently; (c) fence with stated cause if untestable.

(phase02-a2_05-reseg, the third natural candidate, is already queued — not duplicated.)

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-w1-342-tail-parse.md` (this file).
- Queue: `w1-342-tail-parse` queued → verdict/null via temp-file + rename, own entry only; pre-write assert confirmed no prior verdict; JSON re-validated post-write.
- Lock `code/crowd17/next-token/locks/w1-342-tail-parse.lock`: created on start, deleted on completion.
- R5005, sealed gate instances, red-team adjudication queue untouched.
