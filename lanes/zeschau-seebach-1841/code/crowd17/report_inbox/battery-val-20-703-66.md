# Battery verdict: val-20-703-66

- Target: `val-20-703-66` (battery-queue.json, priority 3, status queued)
- Claim: name 66's value at @705; arms the sole surviving leg toward a 20 discriminator
- Evidence: val-20-lettertier NULL
- Adverses: 66's value open

## Bar (verbatim, pre-registered)

"a place licenses 20='e' ('vient en [place]'), a count noun licenses 20='u' ('vient un [noun]'); name or fence at battery grade"

Numbered pass/fail clauses (restated before testing, not modified after):

1. **C1 (name as place):** PASS iff 66's value is named as a specific place at @705 with battery-grade evidence, licensing 20='e' ("vient en [place]").
2. **C2 (name as count noun):** PASS iff 66's value is named as a specific count noun at @705 with battery-grade evidence, licensing 20='u' ("vient un [noun]").
3. **C3 (fence):** if C1 and C2 fail, fence value-naming of 66 at @705 with stated cause.

## Method

1. Read BATTERY-PROTOCOL.md first. Created `locks/val-20-703-66.lock` on start (agent 749e1e56-dc30-4a3a-acc9-236f013b403e, 2026-10-09T20:39:00Z); no stale lock present; deleted on completion.
2. Re-derived the repaired stream in-session from `code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt` via `repair_parse.py`: 1,847 pairs, 96 types. `canonical.py` never used.
3. Byte-confirmed the locus (0-based, row a5_01): @701=12, @702=98, @703=20, @704=12, @705=66, @706=21, @707=35, @708=53, @709=12, @710=48, @711=71. Frame: "n [98-vient] [20] n [66] [21-noun] 35 53 n e 71".
4. Adopted (not re-litigated): 12='n' letter tier (R20-008); 98='vient' LEAD; 21=noun-class (registry); 29='er', 40='e' pencil GT; 94='ne' STRONG LEAD; the val-03-value-census precedent (parsing ≠ naming); poly-66-split's census (n(66)=19; @705 in the "no hypothesized class" group); subclass-66-98-noun PROMOTE (66 plain noun at @88/@123/@766, locus-level only); redteam-66-polyvalence P1 still queued.

## Findings

### Locus structure

The @703–705 window is "98 20 12 66" = "vient [20]n [66]". With 12='n' (letter tier), the "20 12" contact composes to "en" (20='e') or "un" (20='u') — the parent val-20-lettertier NULL's sole surviving leg. Naming 66's value would discriminate: a place forces 20='e' ("vient en [place]"); a count noun forces 20='u' ("vient un [noun]").

66's class at @705 is NOT established. Poly-66-split placed @705 (12-66-21) in the "no hypothesized class" group. The noun class is locus-level only (@88/@123/@766). The bar's dichotomy presupposes noun-class; I test both arms under that presupposition and report the class caveat.

### C1 — name as place: FAIL

No selective leg exists for any specific place at @705. The window "vient en [66] [21-noun]..." supplies zero selectional pressure for any particular place name: France, Paris, Rome, or any other place parses identically. Per the val-03-value-census precedent, parsing ≠ naming — naming any place would be arbitrary. Additionally, the right edge (@706=21, noun-class, value open) is unresolved under the place arm: "vient en [place] [bare-noun]" needs 21 to be an appositive, vocative, or clause-initial, an ungranted assumption. C1 fails.

### C2 — name as count noun: FAIL

No selective leg exists for any specific count noun at @705. The window "vient un [66] [21-noun]..." supplies zero selectional pressure: any masculine singular count noun parses identically. Naming any one would be arbitrary (parsing ≠ naming). The right edge is equally unresolved under this arm. C2 fails.

### C3 — fence: FIRES

66's value at @705 is fenced as unnameable at battery grade (evidentiary, not terminal — re-openable when a selective leg is banked). This is consistent with 66's standing: its exact noun value is unresolved stream-wide, and no standing value exists to transfer.

### Adverse honored

"66's value open" — no value is named or invented; the fence is explicit about the open status.

### Out-of-scope note (not tested, does not affect the fence)

A third arm exists outside the bar's dichotomy: "en [66-gerund]" ("vient en chantant"-shaped). 66's profile shows no gerund evidence (noun windows, non-finite 'pour' windows, finite-shaped 66-84 contacts), and the bar does not list it. It is recorded, not decided.

## Verdict: NULL (fence executed)

C1 FAIL / C2 FAIL / C3 FIRES. 66's value at @705 cannot be named at battery grade; the 20 discriminator stays armed but unfired.

## Scope

- Fences only value-naming of 66 at @705. Untouched: 20's letter-tier question, 66's class/value globally, the redteam-66-polyvalence P1 docket, subclass-66-98-noun's locus-level promotes, §7.
- No standing or red-team verdict contradicted, downgraded, or re-litigated. Canonical-stream caveat stands (row a5_01 offsets unvalidated).

## Follow-ups (for supervisor queuing; all verified ABSENT from queue)

1. `val-21-706-value` (P4) — name 21's value at @706; a named 21 (appositive, vocative, temporal, clause-initial) constrains the right edge and may discriminate the place arm from the count-noun arm.
2. `en-place-barenoun-corpus` (P4) — corpus census of "vient en [place] [bare-noun]" in 1841 French; a zero at scale kills the place arm at grammaticality grade.
3. `un-noun-barenoun-corpus` (P4) — corpus census of "vient un [N] [bare-noun]" in 1841 French; a zero at scale kills the count-noun arm at grammaticality grade.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-val-20-703-66.md`
- Queue: `val-20-703-66` queued → `verdict`/`null`, 2026-10-09 (pre-write assert passed — was queued/verdictless; target-id-unique tmp `battery-queue.json.val-20-703-66.tmp` + rename; disk re-validated; own entry only; no downgrade)
- Lock `locks/val-20-703-66.lock`: created on start, deleted on completion (verified gone). R5005, sealed gates, red-team adjudication queue untouched.
