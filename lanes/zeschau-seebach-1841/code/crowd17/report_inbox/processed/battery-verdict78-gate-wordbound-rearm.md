# Battery report: verdict78-gate-wordbound-rearm

- Target id: `verdict78-gate-wordbound-rearm` (priority 1)
- Claim: re-test the 78-45 word-boundary gate when 78's status changes.
- Worker: c215ee6b-24bd-408e-9806-94fbc27230cc
- Date: 2026-10-09
- Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`; 1,847 pairs / 96 types re-derived in-session, asserts held). `canonical.py` never used. R5005, sealed gate instances, red-team adjudication queue untouched.
- Prior work read and built on (not duplicated): `battery-verdict78-gate-wordbound.md` (null, 2026-10-08 — the original gate battery; bar text quoted verbatim below), `battery-ver78-non45-positive-leg.md` (promote, 2026-10-09), `battery-dict-313-w1-adjudicate.md` (promote, 2026-10-08), Round 20 red-team report `next-token-redteam-r20.md` (2026-10-09).
- Lock: `code/crowd17/next-token/locks/verdict78-gate-wordbound-rearm.lock` (created on start with agent id + UTC timestamp; deleted on completion).

## Bar (verbatim, pre-registered — the original gate battery's bars)

"(a) if 78='ver' promotes, check whether the W2-W4 one-word reads become 'verdict' and whether W1's two-word exception stands or flips (record A11 @314's fate explicitly); (b) if ver-78 kills, the 'verdict' value arm dies - record the boundary as an unvalued word-unit"

## Bar restated as numbered pass/fail clauses (frozen before testing)

1. Clause (a) — conditional on 78='ver' promoting: W2-W4 one-word reads become 'verdict', and W1's two-word exception either stands or flips, with A11 @314's fate recorded explicitly.
2. Clause (b) — conditional on ver-78 killing 78='ver': the 'verdict' value arm dies; the boundary is recorded as an unvalued word-unit.

## Method

Re-derived the 78-45 boundary loci on the repaired stream (no values assumed for 78 or 45; token adjacency only). Checked the six post-gate ver-78-class returns named in the rearm trigger (ver78-ce78-census/promote, ver78-flagship-1181-1352/promote, ver78-1670-5581/promote, ver78-non45-positive-leg/promote, ver78-65-completion/kill, ver78-ce78-open-succ/kill) and the Round 20 red-team disposition of 78='ver'.

## Window-level evidence (@-offsets are 0-based pair indices in the repaired stream)

- 78-45 bigrams re-derived byte-exact: @313, @573, @982, @1164 (n=4) — identical to the original gate battery. n(78)=31 stream-wide.
- The six trigger returns, classified:
  - Promotes: `ver78-ce78-census` (determiner-profile frame), `ver78-flagship-1181-1352` ('le ver ne ment(ent)' flagship frame), `ver78-1670-5581` (55-class discriminator), `ver78-non45-positive-leg` (@819 'ce verre' positive leg on banked/granted values only — breaks the 78<->45 mutual conditionality from the 78 side). All four are LEG-GAINS for 78='ver', not a value promote. The non45 battery's own adverse states: "do not promote 78='ver' globally from this battery -- legs only".
  - Kills: `ver78-65-completion` (killed @1105's 'ce ver[65]' completion arm), `ver78-ce78-open-succ` (killed open-successor ver-word completions). Both killed specific ver-word COMPLETION arms — neither killed 78='ver' itself.
- Round 20 (2026-10-09, ratified): "78='ver': DEFERRED (R16-005 LEAD stands; @819 'ce verre' leg banked)." 78='ver' is LEAD — NOT promoted, NOT killed.
- R20-116 (@889 "pourvoient" one-word parse): locus re-derived at @889 = 86 on row a5_08; no 78 in the window — does not touch this gate.
- A11 @314 (dict-313-w1-adjudicate promote, 2026-10-08): standing, untouched by R20 or any trigger return.

## Per-clause pass/fail

1. Clause (a): NOT TESTABLE — its antecedent (78='ver' promotes) is false. The four ver-78-class promotes are leg-gains; 78='ver' remains LEAD/deferred per Round 20. Running (a) on leg-gains would silently rewrite the bar.
2. Clause (b): NOT TESTABLE — its antecedent (ver-78 kills 78='ver') is false. ver-78 returned null; the two kills killed completion arms, not the value. 78='ver' survives as R16-005 LEAD.

Per protocol §2, the bar is recorded as untestable-as-written under the actual 78 status, and this is a null finding — not a silent rewrite. This matches the original gate battery's own precedent (it returned null rather than running a branch whose antecedent was false).

## Recorded state (no branch fires, but the gate's standing questions get answers)

- 78-45 loci: UNCHANGED (@313/@573/@982/@1164).
- W2-W4 one-word boundary: STANDS. Contact-profile, ver-78-independent per the original gate battery; nothing in the six trigger returns contradicts it.
- 'verdict' value arm: NEITHER becomes 'verdict' NOR dies. It is STRICTLY STRONGER than at the original gate run: the @819 "ce verre" leg (banked/granted values only, now R20-banked) breaks the 78<->45 mutual conditionality from the 78 side, plus three further positive-leg frames. But the arm stays CONDITIONAL on a future 78 resolution — R20 deferred 78='ver' explicitly, and the non45 battery's adverse bars a global promote from legs.
- W1 two-word exception / A11 @314: CORROBORATED, not flipped (dict-313-w1-adjudicate promote stands; no trigger return touches it).
- Trigger accounting: the rearm trigger's letter ("any future ver-78-class battery returns promote or kill") is satisfied by the six returns, but its spirit (a change in 78's STATUS) is not — 78's status did not change. Future re-arms should key on red-team resolution of 78='ver', not on battery-class leg returns (see follow-up #1).

## Adverses answered

- R16-005 LEAD grading: RESPECTED — no promote of 78='ver' or of 78-45='verdict' is made or implied.
- A11 HOLD: RESPECTED — @314 stays 'ce qui'.
- fork-78-45-rerun's 45='ce' kill-scope: NOT re-litigated.

## Verdict: null

Headline: the trigger's six ver-78-class returns are leg-gains and arm-kills, not a promote or kill of 78='ver' — so neither branch of the original bar fires. 78='ver' stands at LEAD per Round 20; the W2-W4 boundary stands; the 'verdict' value arm survives, strengthened by the R20-banked @819 "ce verre" leg but still conditional. No standing red-team verdict contradicted or downgraded.

## Follow-up targets (null regenerates work; all verified ABSENT from the queue)

1. `verdict78-gate-wordbound-rearm2` (P1). Claim: re-arm the 78-45 word-boundary gate keyed on red-team resolution of 78='ver' (not on battery-class leg returns). Bars: (a) if the red team GRANTS 78='ver', check whether the W2-W4 one-word reads become 'verdict' and whether W1's two-word exception stands or flips (record A11 @314's fate explicitly); (b) if the red team KILLS 78='ver', the 'verdict' value arm dies — record the boundary as an unvalued word-unit; trigger = a red-team ruling changing 78's status. Evidence: this report (78-45 loci @313/@573/@982/@1164; six trigger returns classified as leg-gains/arm-kills; R20 deferred 78='ver'). Adverses: R16-005 LEAD grading; A11 HOLD; do not re-run fork-78-45-rerun's kill-scope.
2. `verdict-arm-819-strengthen` (P3). Claim: test whether the R20-banked @819 "ce verre" leg composes with the W2-W4 one-word reads — does 'verdict' gain a second independent composition leg outside 45-adjacency? Bars: name the composition with byte evidence at battery grade, or fence the cross-window composition arm. Evidence: ver78-non45-positive-leg promote; R20 banks the @819 leg. Adverses: legs only — no global 78='ver' promote from this battery; R16-005 LEAD grading.
3. `w2w4-boundary-78less` (P4). Claim: re-test the W2-W4 contact boundary with 78's value abstracted (shape-only contact profile), confirming the boundary's ver-78-independence against the strengthened value arm. Bars: boundary re-promotes on shape evidence alone, or the ver-78-independence claim fences. Evidence: original gate battery's contact-profile promote; this report's locus re-derivation. Adverses: do not touch 45's value.

## Non-duplication note

The original gate battery's follow-up #2 (`boundary-value-census`, P3) is already queued — not re-proposed. Lock created with agent id + UTC timestamp on start; deleted on completion.
