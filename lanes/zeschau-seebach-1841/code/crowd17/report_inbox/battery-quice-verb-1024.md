# Battery report: quice-verb-1024

Target: quice-verb-1024
Claim: find the verb for 'ce qui' @1024-1025.
Worker: subagent c99077f4-f0e0-490f-8630-8297746e3a9a
Date: 2026-10-09
Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json + data/upstream-ct_R5005.txt), parsed per code/side-keyhunt/repair_parse.py. Asserts re-run: 1,847 pairs, 96 types. canonical.py never used. R5005, sealed gates, red-team queue untouched.

## Bar (verbatim, pre-registered)

"name the verb in a grammatical 1841-French parse, or fence 'ce qui par [43]' as a verbless fragment"

## Bar restated as numbered pass/fail clauses

1. C1: name the finite verb of subject-'qui' @1025 in a grammatical 1841-French parse with zero new assumptions.
2. C2: otherwise, fence 'ce qui par [43]' @1024-1027 as a verbless fragment with stated cause.

## Method

Dumped @1020-@1050 on the repaired stream with standing values applied. Enumerated every verb-shaped cell after @1025 within clause range and tested each as the finite verb of 'qui' @1025 under banked/granted/provisional values only. Checked standing adjudications that constrain the locus: R19-142 (ce01-1029 package), Round-20 REJECT of ne-W6-pas-verb, R16 "@1034 clause boundary '[verb]-le. La première…'", edge-1024-clause-boundary KILL (2026-10-08), val-01-census NULL (2026-10-09).

## Window-level evidence

Row a6_03, 0-based (banked values in brackets):

```
@1020 53      [53]
@1021 84      on (A15)
@1022 92      [92]
@1023 64      qui
@1024 45      ce (A11 hold)
@1025 64      qui          <- subject needing its verb
@1026 96      par
@1027 43      [43] (noun class; value = noun-43's arm)
@1028 87      ce
@1029 01      [01] (no uniform value: val-01-census NULL 2026-10-09)
@1030 03      [03] (finite license dead: R20 REJECT ne-W6-pas-verb)
@1031 29      er (GT letter)
@1032 80      [80] (A8 verb-frame)
@1033 77      le (R16: promoted; enclitic object of 80)
@1034 11      la           <- R16 clause boundary between @1033 and @1034
@1035-1039    70 82 34 29 40 = "premiere" (pencil GT)
@1040 17      fois
@1041 77      le   @1042 82 m   @1043 63   @1044 11 la
@1045 67      et/veut ...
```

Read: "…[53] on [92] qui | ce qui par [43] ce [01] [03]er [80-V]-le. La première fois…"

'45 64' bigrams stream-wide: @314, @340, @1024 (3x). The @340 twin shares the 6-gram "45 64 96 43 87 01" but has different right context ("06 70 12 94…" = "[06] prenne…"); it is NOT adjudicated here.

## Candidate-verb tests (C1)

1. **80 @1032 (A8 verb-frame).** To serve 'qui', the parse must be "ce qui, par [43], ce [01] [03]er, [80-Vfin]-le". FAILS: "ce [01] [03]er" intervenes between subject-'qui' and verb with no grammatical license — 01 has no value at battery grade (val-01-census NULL: 01='en' dead at kill grade across 9 windows, 01='tain' dead, no uniform value nameable), and the sole candidate reading of "87 01 03 29" ("Ceci, [03]er!") is FENCED at R19-142 (01='-ci' unproven; demonstrative + bare exclamatory infinitive 0x in 24.4M chars). Reaching 80 needs >=1 ungranted assumption. INDEPENDENTLY: 80 is unavailable — R16 standing parse is "[verb]-le. La première…" with @1031 fenced as enclitic+break and a clause boundary at @1034; 80 heads its own clause with enclitic "le" and cannot simultaneously head the 'qui' clause across "ce [01] [03]er".
2. **03 @1030.** "[03]er" is infinitive-shaped; an infinitive cannot be the finite verb of subject-'qui'. 03's only finite license (W6 @1367) was REJECTED by Round 20 (ne-W6-pas-verb REJECT; W6 C1 does not re-open). DEAD.
3. **85 @1047 (A3 verb-stem), 88 @1049 (finite per pron730-clause-wide).** Both sit across the R16 @1034 clause boundary and the "La première fois…" clause — inaccessible to 'qui' @1025 at any standing license. DEAD.
4. **Boundary rescue.** KILLED at battery grade by edge-1024-clause-boundary (2026-10-08): no clause boundary between @1023 and @1024 rescues the verb-lessness.

C1: FAIL — no verb-shaped cell can serve 'qui' @1025 in a grammatical 1841-French parse with zero new assumptions.

## Fence (C2 fires)

'ce qui par [43]' @1024-1027 is FENCED as a verbless fragment under standing values. Stated causes:

- (a) 01 is valueless at battery grade (val-01-census NULL, 2026-10-09); every route from 'qui' to any verb crosses "87 01".
- (b) The "Ceci, [03]er!" skeleton for "87 01 03 29" is FENCED at R19-142.
- (c) 03's finite license is dead (Round-20 REJECT of ne-W6-pas-verb).
- (d) 80 is fenced into its own clause (R16 "[verb]-le. La première…", @1031 enclitic+break, boundary @1034).
- (e) No boundary rescue exists (edge-1024-clause-boundary KILL).
- (f) The next verb-shaped cells (85 @1047, 88 @1049) are across a clause boundary.

The fence claims only that the current value inventory cannot produce the verb — not that the manuscript is ungrammatical. It does not touch 45='ce' (A11 hold), 64='qui', 96='par', 87='ce', or noun-43's value arm.

## Per-clause pass/fail

1. C1 (name the verb): FAIL — exhausted above; every candidate needs an ungranted assumption or violates a standing fence.
2. C2 (fence as verbless fragment): PASS — fenced with six stated causes.

## Verdict: PROMOTE

The bar's second arm is the terminal resolution and it fires cleanly. The question "where is the verb for 'ce qui' @1024-1025?" is closed under standing values: there is none reachable; the locus is fenced pending the blockers below.

## Adverses

- None listed on the target. Standing verdicts adopted, none contradicted: R19-142, R16 77='le'/@1034-boundary, edge-1024-clause-boundary KILL, val-01-census NULL, Round-20 ne-W6-pas-verb REJECT. §7 intact.

## Scope

Fence covers the @1024 locus only. The @340 twin ("45 64 96 43 87 01" + "06 70 12 94 [74]…") shares the 6-gram but has different right context and is not adjudicated here — note "prenne" @347-349 sits 7 pairs downstream there, same intervention problem ("ce [01] [06]" crosses it). No value named; no registry change; no red-team act requested.

Re-arm conditions (not queued — verdict is promote): name 01's value; resolve 03's class; name 43's value; or overturn any of (b)-(e). Any one re-opens the verb search.

## Bookkeeping

- Report: code/crowd17/report_inbox/battery-quice-verb-1024.md
- Queue: `quice-verb-1024` -> status verdict / result promote (own entry only; pre-write assert passed: was queued/verdictless; temp-file + rename; disk re-validated)
- Lock: created 2026-10-09T15:24:00Z, deleted on completion.
