# PRE-REGISTRATION — 67-FINISHER round 10 (residuals)
**Timestamp: 2026-10-07 20:39:15 UTC** (written before any round-10 data computation)

Task: STATE.md round-10 WO-5 — classify the 6 open-residual 67 windows
(@633, @902, @1372, @1450, @1519, @1623); rule on the @1248 counterdatum's
weight; close or explicitly residual-list each window.

Standing record (not re-derived): windows from
`code/crowd8/morphologist/results_r8.json['open67']`, byte-verified in round 9
against the repaired 1,847-pair parse (re-verify F0 here). Standing rules
R_et1..6 / R_veut1..3 (`code/crowd7/morphologist/battery67_final.json`) fire
on NONE of the 6 (round-9 recheck). n67=38: 29 classified (et 18 / veut 11),
@1248 NEITHER-fenced, @199 NEITHER-fenced-conditional-on-08="l'",
@630 et-CONDITIONAL(C1∧C2), 6 open-residual.

Board (standing): GT 11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que;
provisional 87=ce, 64=qui, 96=par, 59=est; 77="le" provisional-conditioned;
leads {93,8}="l'", 06="ent"-iff-82, 00="pour" (strong), 16="i", 78="er".

Era: Nesselrode v8, lane tokenizer verbatim (vendored copy of the
round-9 `score67_r9.py` tokenizer; 97 dateline-split docs, NW=92,123).
Rate bars use Nesselrode v8 only. Never score manual-tiling bearing counts.

## Classification bar (general, fixed now)

A window classifies as **et-CONDITIONAL** iff ALL pass:
- **F0**: window byte-verified in the repaired 1,847-pair parse
  (`load_pairs_repaired`), pre/suc/pre2/suc2 match the standing record.
- **L1 (era, conditioned frame)**: E_et = n(era frame with "et"),
  E_veut = n(era frame with "veut"), frame conditioned ONLY on
  board GT/lead/provisional readings named in the per-window bar.
  Pass iff E_et ≥ 20 AND E_veut ≤ 3 AND (E_veut == 0 OR E_et/E_veut ≥ 10).
  (Same leg-kind and thresholds as round-9 bar E2-L1.)
- **L2 (cipher, GT-anchored nominal contact)**: n(11→W) ≥ 2 where 11="la"
  is pencil GT and W is the frame's unknown content word (nominal evidence;
  same leg-kind as round-9 bar E2-L2).
- Verdict carries **C1** (lead-condition, where the frame conditions on a
  lead) and **C2** (67 is a standalone word at the window: pre does not
  merge with 67; no clitic interference) — explicit, for red-team
  adjudication. A conditional is NOT a classification.

A **NEITHER** bar needs F1 byte-verify + F2 both arms era-zero in a
board-conditioned frame + F3 no new arm fires (round-9 bar N1 design).

## Per-window bars (fixed now)

- **E3 — @1519** (win 11-91-67-08-31; frame "X l' 31", C1: 08="l'" lead at
  @1520): L1 = n("et l'") vs n("veut l'") (expect ≈63:1, recompute);
  L2 = n(11→31) ≥ 2. Verdict if pass: et-CONDITIONAL(C1∧C2).
- **E4 — @1372** (win 16-91-67-98-00; frame "X 98 pour", C1': 00="pour"
  strong lead at @1374): L1 = n("et * pour") vs n("veut * pour");
  L2 = n(11→98) ≥ 2. Verdict if pass: et-CONDITIONAL(C1'∧C2).
- **E7 — @1450** (win 59-36-67-33-46; frame "X 33 que", 46=que GT at
  @1452): L1 = n("et * que") vs n("veut * que"); L2 = n(11→33) ≥ 2.
  Verdict if pass: et-CONDITIONAL(C2). (No C1 — 46 is GT.)
- **E7 — @1623** (win 78-66-67-33-46; frame "X 33 que", 46=que GT at
  @1625): same L1/L2 as @1450. Verdict if pass: et-CONDITIONAL(C2).

## Design-time nulls (not attempted)

- **@633** (08-52-67-63-74): no ≥2-leg bar designable. 52/63 have no
  board reading; no era frame is conditionable ("52 67 63" both unknown);
  the 11→52 ×3 nominal contact is a single leg with no independent second.
  → open-residual by design. Missing: a board-grade reading for 52 or 63
  (nominal class for 52 is 1 leg; needs an independent second leg), or an
  era-conditionable frame.
- **@902** (16-92-67-16-88): no ≥2-leg bar designable. Era frame blocked:
  "i"-as-word for 16 is a lead, not established (round-9 prereg: the
  n("et i")=n("veut i")=0 observation cannot fence without it). 92 has no
  board reading. → open-residual by design. Missing: 92's class, or
  establishment of 16 as the word "i".
- **NEITHER bars for the 6**: none live by design. Every conditionable
  frame ("et * que", "et * pour", "et l'") is era-common, so bar-N1-style
  F2 (both arms exactly zero) cannot pass. Recorded as a design-time null,
  not attempted per-window.

## Lean census (unscored — leans are not classifications)

For each of the 6, record as single-leg leans only: pre-contact census
(other pre=P 67-windows and their standing classes) and suc-contact census
(other suc=S 67-windows and their standing classes). The suc==33 contact is
NOT a leg candidate (design-time: @1423 veut vs @272/@1148/@1476 et —
classifications track pre-side rules, not suc; confounded, excluded).

## @1248 counterdatum weight (ruling; no new-arm work here)

- Standing: F67 (adjudicator GRANT) — @1248 NEITHER-fence UPHELD, new arm
  declined with evidence ("pour * que" middles {cela:3, empêcher:1}, no
  single-syllable X with era support; finite-verb arm vetoed by frenchman
  Gate 4). Round-10 WO-4 (arm-builder) owns any new-arm census at @1248.
  **This executor does not re-run the "pour * que" census** (no duplication).
- Pre-registered weight ruling: @1248 is fenced n=1 with both fork arms
  era-zero and no era-supported new arm. Its weight against the fork is
  **scope amendment only**: the fork stays SUPPORTED over the fenced domain
  (36 in-scope windows: 29 classified + @630 conditional + 6 residual;
  2 fenced out). It is a genuine fenced exception, not a refutation of the
  conditioned fork claim. If WO-4's arm-builder produces a ≥2-leg
  non-finite arm, the fork re-scopes per that bar; until then the fence
  holds and the amended scope stands. 62-WO3 blocker noted as carried
  forward (no 62-interaction found in round 9).

## What counts as "closed"

All 6 classified via the bars above, or an explicit residual list naming,
per window, the exact missing leg(s). Single-leg leans stay unscored.
Red team adjudicates every status change — this package is a
recommendation, not a merge.
