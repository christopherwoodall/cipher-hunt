# Battery report: verdict78-gate-wordbound

- Target: `verdict78-gate-wordbound` (priority 1, status queued)
- Claim: re-test the 78-45 word-boundary bar once ver-78 resolves
- Worker: 2dfda67e-b2e0-430e-93e9-3964578c45f7
- Date: 2026-10-08
- Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`). `canonical.py` NOT used. R5005, sealed gates, and the red-team queue untouched.
- Prior work read and built on (not duplicated): `battery-dict-78-45-wordbound.md` (null; this target = its follow-up #1), `battery-ver-78.md` (null), `battery-fork-78-45-rerun.md` (null), `battery-dict-313-w1-adjudicate.md` (promote, 2026-10-08), `battery-dict-45-contact-update.md` (promote, ver-78-independent).

## Bar (verbatim, pre-registered)

"(a) if 78='ver' promotes, check whether the W2-W4 one-word reads become 'verdict' and whether W1's two-word exception stands or flips (record A11 @314's fate explicitly); (b) if ver-78 kills, the 'verdict' value arm dies - record the boundary as an unvalued word-unit"

## Bar restated as numbered pass/fail clauses (frozen before testing)

1. Clause (a) — conditional on ver-78 promoting 78='ver': W2-W4 one-word reads become 'verdict', and W1's two-word exception either stands or flips, with A11 @314's fate recorded explicitly.
2. Clause (b) — conditional on ver-78 killing 78='ver': the 'verdict' value arm dies; the boundary is recorded as an unvalued word-unit.

## Method

Read BATTERY-PROTOCOL.md first; created and deleted the lockfile per protocol. Read ver-78's queue entry and verdict report, fork-78-45-rerun's entry, and dict-313-w1-adjudicate's report. Re-derived the boundary loci on the repaired stream with repair_parse.py (no values assumed for 78 or 45; only token adjacency). Checked the status of ver-78's regeneration children in the queue.

## Window-level evidence (@-offsets are pair indices in the repaired stream)

- ver-78 current status: `verdict` / result `null` (2026-10-08). 78='ver' is LEAD per red-team R16-005 — NOT promoted, NOT killed. @296 remains a red-team-fenced 1-window residual.
- 78-45 bigrams re-derived: @313, @573, @982, @1164 (n=4). Post-78 45-followers: @314->64, @574->13, @983->01, @1165->13 = {64, 13, 01}.
- 5-gram 78-45-13-55-61 x2: @573 (`78 45 13 55 61`), @1164 (`78 45 13 55 61`) — byte-identical.
- 45-64 windows x3: @314, @340, @1024.
- W1 @305-322: `02 88 20 17 46 84 24 37 | 78 45 | 64 59 32 94 06 11 92 60` — matches the parent battery's window.
- ver-78's regeneration children, already decided: `ver-78-rebar` null, `ver78-ce78-open-succ` kill, `ver78-296-reparse` null. None promoted 78. No new ver-78-class target is queued or in flight.
- A11 @314's fate (recorded explicitly per the bar's (a)-clause): `dict-313-w1-adjudicate` PROMOTED 2026-10-08 — "@313's parse adjudicated for 'ce qui'; 45@314 = 'ce', the standing A11 two-word exception." A11 HOLD strengthened, not flipped. The W1 two-word exception now has battery-level adjudication support.

## Per-clause pass/fail

1. Clause (a): NOT TESTABLE — its antecedent (ver-78 promotes 78='ver') is false. ver-78 returned null.
2. Clause (b): NOT TESTABLE — its antecedent (ver-78 kills 78='ver') is false. ver-78 returned null.

NOTE on the task brief: the brief instructed "ver-78 returned NULL (78='ver' did NOT promote) — run under branch (b)". Branch (b)'s antecedent is ver-78 killing, which is false; running it would silently rewrite the bar. Per protocol §2, the bar is recorded as untestable-as-written under the actual ver-78 outcome, and this is a null finding, not a silent rewrite.

## Recorded state (no branch fires, but the gate's standing questions get answers)

- W2-W4 boundary: STANDS. The contact-profile boundary was promoted by the sister battery `dict-45-contact-update` (Fisher p=0.002) and is explicitly ver-78-independent — ver-78's null does not touch it.
- Value arm: NEITHER becomes 'verdict' NOR dies. 78='ver' survives as R16-005 LEAD. The W2-W4 word-unit remains an unvalued-but-LEAD-leaning unit — the value 'verdict' stays conditional on a future 78 resolution.
- W1 exception: CORROBORATED, not flipped. `dict-313-w1-adjudicate` promote (2026-10-08) adjudicated @313-314 as 'ce qui'; the 45-64 mirror family (@314/@340/@1024) is intact.
- Gate re-arm condition: the trigger "ver-78 resolves" is still unmet, and ver-78's own regeneration children (rebar null, ce78-open-succ kill, 296-reparse null) are spent. This target's bars become testable again only if a NEW ver-78-class battery changes 78's status.

## Adverses answered

- R16-005 LEAD grading: RESPECTED — no promote of 78='ver' or of 78-45='verdict' is made or implied here.
- A11 HOLD: RESPECTED — @314 stays 'ce qui'; the two-word W1 exception is corroborated by dict-313-w1-adjudicate, not overturned.
- fork-78-45-rerun already verdict/null: COORDINATED, not duplicated — this battery re-tests only the boundary gate under ver-78's outcome; the 45='ce' kill-scope of the fork is not re-run.

## Verdict: null

Headline: ver-78 returned null, so neither branch of this target's bars fires — the bar as written covers only promote/kill of ver-78. The boundary stands at W2-W4 (contact-profile, ver-78-independent); the 'verdict' value arm survives as R16-005 LEAD; W1's two-word exception is corroborated by today's dict-313-w1-adjudicate promote. No standing verdict contradicted or downgraded.

## Follow-up targets (null regenerates work)

1. `verdict78-gate-wordbound-rearm` (priority 1). Claim: re-test the 78-45 word-boundary gate when 78's status changes. Bars: verbatim the bars above; trigger = any future ver-78-class battery returns promote or kill for 78='ver'. Evidence: this report (boundary loci @313/@573/@982/@1164; 5-gram x2 @573/@1164; W1 exception corroborated by dict-313-w1-adjudicate promote; ver-78 regen children spent). Adverses: R16-005 LEAD grading; A11 HOLD; do not re-run fork-78-45-rerun's kill-scope.
2. `boundary-value-census` (priority 3). Claim: the 'verdict' value arm has (or lacks) legs outside ver-78's bar. Bars: census all 31 windows of 78 on the repaired stream; count 'ver'-word-shaped continuations (78 followed by vowel-initial/word-internal positions) vs 'er'/nominal shapes; the value arm gains a leg iff >=2 windows parse 'ver'-shaped under standing values with stated cause each. Evidence: ver-78 null left the value arm unsettled; ver78-ce78-open-succ killed; boundary contact profile holds regardless. Adverses: R16-005 LEAD grading; do not contradict ver-78's null (no promote of 78='ver' from this battery — legs only).

## Non-duplication note

`unit-13-55-61-contact` and `boundary-45-exclusivity-sensitivity` (parent battery's follow-ups #2/#3) are already queued — not re-proposed. `ver78-296-97gate` and `ver78-ce78-census` are queued and cover adjacent ground — not re-run here. Lock created with agent id + UTC timestamp on start; deleted on completion.
