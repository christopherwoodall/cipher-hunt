# Battery report: noun-43-1205-window

- Target: `noun-43-1205-window`
- Claim: narrowed 43-noun test on the @1200-1208 window using noun-43's candidate set + the 'pour que' discriminator
- Date: 2026-10-09
- Worker: battery worker noun-43-1205-window (subagent 5d860f34-4bc3-415a-8f78-f46638543af7)
- Stream: repaired 1,847-pair / 96-type parse (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py` — 1,847 pairs / 96 types asserted in-session). `canonical.py` never used. R5005, sealed gates, red-team adjudication queue untouched. No data invented. @-offsets are 0-based stream indices.
- Lock: `code/crowd17/next-token/locks/noun-43-1205-window.lock` created 2026-10-09T09:52:40Z, deleted on completion.

## Bar (verbatim from battery-queue.json)

"resolve iff 43 takes a noun value under noun-43's candidate set with the window parsing; else fence with stated cause"

Numbered pass/fail clauses (pre-registered, frozen before testing):

1. 43 takes a noun value drawn from noun-43's candidate set {suite, manière, condition, mesure}.
2. The window @1200-1208 (`29 45 58 47 43 55 61 21 65`, row a7_00) parses with that value — sketch: "er [45] [58] ce [43-noun] [55] [61] [21] [65]" under granted 47="ce".
3. Else: fence the window's 43-value question with stated cause.

## Method

- Re-derived the repaired stream in-session; asserts held.
- Coordinate with (not re-litigate) the standing verdicts: noun-43 (NULL, 2026-10-09), noun-43-discriminator (KILL, 2026-10-08), cond-mesure-43full (NULL, empty survivor set, 2026-10-09), par43-adverbial-attestation (PROMOTE, 2026-10-09), frame-1205-parse (NULL, 2026-10-09), 43-29-segment (PROMOTE, 2026-10-09), en43-wordinternal-census (PROMOTE, 2026-10-09). Checked for red-team overturns: none — `redteam-43-polyvalence` (RED-TEAM DECISION) and `noun43-redteam-escalate` are both still queued, untouched.
- The parent report's follow-up suggested running noun-43's 'pour que'-frame discriminator to select the candidate; I tested whether the discriminator's geometry exists at this window.

## Window-level evidence (re-derived)

- Window @1200-1208: `29 45 58 47 43 55 61 21 65`, 43 at @1204 (row a7_00), flanks `@1199=64` and `@1209=64`.
- Granted values inside: 29="er" (banked), 47="ce" (allophone tier). 45, 58, 43, 55, 61, 21, 65 open.
- 43 census: n=16 at [21, 43, 244, 258, 343, 386, 439, 563, 1027, 1092, 1126, 1204, 1303, 1305, 1544, 1724] — byte-identical to noun-43's census.
- 43 successors: {29:1, 81:1, 00:3, 77:2, 87:2, 91:1, 98:2, 24:1, 07:1, 55:1, 21:1}. **43→55 occurs exactly once stream-wide (@1204)** — the discriminator arm's bigram.
- **The 'pour que' discriminator geometry is absent here.** The discriminator frame is the trigram "43 00=pour 46=que". Census: `43→00` x3 (@244/@1126/@1544), but `00→46` x4 (@106/@545/@1545/@1680); the trigram "43 00 46" occurs **exactly once stream-wide, at @1544–1546** (@244's 00 is followed by 66; @1126's by 86). At @1204 the window reads `47=ce [43] 55 61 21 65` — no "pour", no "que", no subjunctive governor. The discriminator cannot select a candidate at this window; its only licensed firing site is @1544.

## Candidate-set exhaustion (adopted from standing verdicts)

noun-43's candidate set, current status:

| candidate | status |
|---|---|
| suite | KILLED — noun-43-discriminator (KILL, 2026-10-08); @21 forces V(43)!="suite" |
| manière | KILLED — noun-43-discriminator (KILL, 2026-10-08) |
| condition | KILLED at kill grade — cond-mesure-43full (fails par-43 x2 @343/@1027 and @21); the last escape (bare "par condition" adverbial) closed by par43-adverbial-attestation (PROMOTE, Littré/TLF negative result) |
| mesure | KILLED at kill grade — cond-mesure-43full (fails par-43 x2 and @21); last escape (bare "par mesure" adverbial) closed by par43-adverbial-attestation (PROMOTE) |

The set is exhausted: 0/4 survivors. The noun-43 NULL already recorded this closure ("the noun-43 line is closed at battery level pending red-team act"). No battery may name a value from an empty set.

## Per-clause pass/fail

1. **Clause 1 (value from the candidate set): FAIL.** The set is exhausted at kill grade by standing battery verdicts — suite/manière killed, condition/mesure killed with their last corpus escape closed. Nothing re-litigated; no verdict downgraded or contradicted.
2. **Clause 2 (window parses with the value): MOOT.** No surviving candidate exists to test; the 'pour que' discriminator cannot select one here anyway (geometry unique to @1544, absent at @1204). The window's only granted contact remains "ce [43]" (@1203–1204, 47="ce" allophone tier), which licenses no value.
3. **Clause 3 (fence with stated cause): EXECUTED.**

## Adverses answered

- "coordinate with noun-43's null": done — noun-43's NULL is adopted as premise. This battery does not re-name, re-litigate, or contradict it; the fence inherits its closure ("pending red-team act").
- "21/65 values open": both remain open throughout; the fence does not depend on their values. 21's nominality is assumed in the window sketch only as the parent report's frame; nothing hinges on it.

## Verdict: NULL (fence executed)

Headline: the resolve arm is unsatisfiable — noun-43's candidate set is empty at battery grade (all four killed, last escape closed by par43-adverbial-attestation's PROMOTE), and the 'pour que' discriminator's geometry is absent at @1204 (unique to @1544), so no candidate selection is possible at this window. This is null grade, not kill: the window itself forces nothing false under granted values (only 29="er" and 47="ce" are granted inside); the kill-grade deaths belong to noun-43's battery line, coordinated with here. No red-team verdict is contradicted — the sole surviving reopen path is the queued `redteam-43-polyvalence` adjudication on the @21 verb-stem shape, untouched here. The @1200–1208 window's 43-value question is fenced as dependent on the noun-43 line.

## Follow-up targets (nulls regenerate work; all ids verified absent from battery-queue.json 2026-10-09)

1. **noun43-1205-rerun-polyvalence** (P4) — re-run this exact bar (candidate set + 'pour que' discriminator at @1200–1208) once `redteam-43-polyvalence` adjudicates 43's nominality. Gated on that red-team ruling; do not run before.
2. **poly-43-21-split-1204** (P4) — if the red team declares 43 polyvalent (verb-stem at @21 per 43-29-segment's escalated question, noun elsewhere), test the noun arm specifically at @1204 with the discriminator set re-opened; coordinate with queued `noun43-redteam-escalate`.
3. **val-65-1204-rightedge** (P3) — name 65's value at the @1204 window (21→65 x4, @1207 contact): `bound-65-64-qui` (PROMOTE) fixes the @1208|@1209 right-edge boundary; a named 65 constrains "ce [43] [55] [61] [21] [65]" from the right edge under standing values. Coordinate with the 65-gender docket; do not re-litigate promoted verdicts.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-noun-43-1205-window.md` (this file)
- Queue: `noun-43-1205-window` → status `verdict`, result `null`, date 2026-10-09 (pre-write assert: queued/verdictless; temp-file + rename; JSON re-validated; own entry only; no downgrade)
- Lock deleted on completion.
