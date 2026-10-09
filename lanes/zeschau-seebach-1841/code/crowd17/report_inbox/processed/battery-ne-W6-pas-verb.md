# Battery `ne-W6-pas-verb` — verdict: PROMOTE (03 FINITE at @1367)

Follow-up #1 of `ne-scope-62-indet` NULL (2026-10-09). Worker: battery (subagent
8062a1ea-d4cc-4796-b846-66b857635a60). Date: 2026-10-09.
Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` +
`code/side-keyhunt/repaired_offsets.json`, parsed like `repair_parse.py`;
asserts 1847/96 held in-session). `canonical.py` never used. R5005, sealed
gates, red-team adjudication queue untouched.

## Bar (verbatim, pre-registered from battery-queue.json)

"name 03's finite/infinitive status with battery-grade evidence, else fence the W6 window"

Numbered clauses (fixed before testing):
- C1: 03's finite/infinitive status at @1367 (W6's ne...pas window) NAMED with
  battery-grade evidence (standing values/frame grants/battery verdicts/French
  syntax only; no ungranted value, class, or boundary assumption).
- C2 (else-arm): C1 fails → fence the W6 window with stated cause.

Adverses listed: none. One adverse adopted from the parent follow-up proposal
(67 @1390 "veut" must be shown not to be the ne-verb) — answered below.

## Locus (byte-exact, 0-based, row-validated)

Row a7_06: `... 62(1362) 94(1363) 79(1364) 14(1365) 60(1366) 03(1367) 30(1368)
82(1369) ...`
- 94@1363 = "ne" (single value, R19-167/168 closed).
- 30@1368 = "pas" (promoted R17-004).
- Ne-scope audit rule (94 → next 46/64/94; bound 46=que @1408) puts 30@1368
  inside the ne-scope; no 46/64/94 boundary cell between @1363 and @1368.
- 03@1367 immediately precedes 30@1368 ("V pas" contact).

## Method

Adopted as premises (not re-litigated): 94="ne" (R19-167); 30="pas" (R17-004);
79="tout" (A5); 14="en" (en14-value-tighten battery-promote, 15/15 census);
verb-14-rival KILL (14 not infinitive/verb-stem); 60=gérondif in the "79 14 60"
phrase at both stream windows (gerund-60-1688 battery-promote); 03 verb-stem
(stem-03 battery-promote; R19 verb-stem class scoped to the three "03 29"
windows @1030/@1320/@1594 — @1367 is outside that scope, so this battery is
window-level); 86 INF-class (registry standing); 67 et/veut positional rule
exceptionless (R19; 67="veut" iff follower infinitive-shaped); "V pas" contact
precedent (R19-74: 56's finiteness from "V pas" contact @1733); positive control
@559-560 "94 59(=est) 30" = "ne est pas" (finite verb immediately before pas).

## Per-cell elimination (the finite verb must sit in 1364–1367)

The ne...pas clause needs exactly one finite verb between ne and pas, and in
French the negated finite verb immediately precedes "pas".

- 79@1364 = "tout" (A5 granted): non-verbal. Excluded.
- 14@1365 = "en" (battery-promoted; verb-stem rival killed lane-wide):
  preposition/clitic, non-verbal. Excluded.
- 60@1366 = gérondif (battery-promoted at both "79 14 60" windows; "tout en" +
  present participle): non-finite by definition. Excluded. Note: even under the
  still-live R2 pronominal rival ("tout en dépend"-shaped, finite 60), 60
  cannot be the ne...pas verb — the negated verb must touch pas and 03
  intervenes; that rival would strand two finite verbs in one clause.
- 03@1367: the sole remaining verb-shaped cell, in "V pas" contact.

## C1 — PASS: 03 is FINITE at @1367

1. Positional: 03@1367 immediately precedes 30@1368="pas" inside the
   94@1363="ne" scope — the canonical finite-verb slot of "ne...pas"
   (positive controls: @559-560 "ne est pas"; R19-74 "V pas" contact @1733).
2. Elimination: every other cell in 1364–1367 is non-verbal or non-finite at
   battery grade (above); no finite rival exists within budget.
3. Infinitive rival fails: an infinitive directly before "pas" is
   ungrammatical in 1841 French, and it would strand the ne...pas clause
   with no finite verb. The "ne pas + INF" rival (cf. @1702 "94 30 20")
   requires "pas" immediately after "ne" — falsified here (four cells
   between).
4. No ungranted assumption: no value, class, split, or boundary is named.
   Finiteness is a window-level syntactic property, not a §7 naming act;
   03's value and global class stay open, and the "03 29" verb-stem class
   scope is untouched.

## Adverse answered

67@1390 = "veut" (67 positional rule, exceptionless; follower 86@1391 is
INF-class standing) is finite — but it post-dates pas@1368 and therefore
belongs to a later clause inside the scope. The ne...pas clause's verb must
precede "pas". 67@1390 is not a rival for the ne-verb.

## Consequence

Per `ne-scope-62-indet`'s bar ("≥1 window's verb named at battery grade
re-opens C1"), W6 @1362 now re-opens C1: its 94-scope's finite verb is named
(03@1367). W4/W5/W7/W8 verdicts from the parent battery are untouched.

## Scope (stated, not hidden)

- Window-level only: 03 is FINITE at @1367. No value named for 03; no class
  declared; §7 intact (67 sole polyvalence; no polyvalence declared here).
- 03's infinitive-shaped windows ("[03]er" x3 @1030/@1320/@1594; "pas [03]"
  x3 @31/@657/@994; "[03] qui" x4) are untouched — finiteness at @1367 does
  not constrain them.
- 14="en" and the gérondif reading are battery-grade (red-team ratification
  pending), which is exactly the bar's evidence standard; adopted as
  premises per pipeline convention.
- Canonical-stream caveat stands (row a7_06 offset unvalidated).

## Verdict: PROMOTE

No follow-ups required per §4 (promote). The C1 re-open consequence for
`ne-scope-62-indet` is automatic per that battery's bar.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-ne-W6-pas-verb.md` (this file).
- Queue: own entry only, temp-file + rename; pre-write assert confirmed
  queued/verdictless; JSON re-validated after write.
- Lock `code/crowd17/next-token/locks/ne-W6-pas-verb.lock` created on start
  (agent id + 2026-10-09T14:26:50Z), deleted on completion.
- No standing verdict contradicted or downgraded. No red-team escalation
  needed (§7: finiteness is not a class/value/split/polyvalence naming).
