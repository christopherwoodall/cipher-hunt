# Red-team round-8 report — baselines extended, bars pre-registered

2026-10-07 15:01 CDT · round-8 red-team adjudicator · kill authority over round-8 promotions.

## JOB 1 — baseline extensions (extended, not rebuilt; all checks on the repaired 1,847-pair stream)

- `code/crowd7/redteam/verify_f26_17.py`: 61/61 → **77/77 PASS**. R7BANK adds 16 checks:
  N45 62→98=5; bedrock-corrected n64=47; F52 leg rates P(59|64)=3/47=0.0638,
  P(59|94)=3/37=0.0811, P(59)=27/1847=0.01462; F56 M6 contacts n77=44/n37=28,
  37→77=2; F58 48-battery baseline (n48=38, 62→48=6, 48→46=0, 48↔94=0,
  successor ceiling 2); N46 n93=14; F59 Mehemet-Ali P[8:13]=[78,18,93,62,98]
  + M0 archive drift guards (null 33/11870, 10 bearing windows).
- `code/crowd7/redteam/verify_round7.py`: 45/45 → **58/58 PASS**. STATUS-LINE adds
  13 checks: 84 en-islet n/n_eff=4/3 (46-84-24 byte-identical ×2), noun-islet
  n/n_eff=8/6, 64-96-47 3-gram @149 only (96=verb n_eff=1), 00="le" islet 3 distinct
  windows; corpus-side banked values with provenance (L1 Guizot t5–t6 0.0213 /
  Nesselrode v8 0.0414 / aggregate 0.0249; 93 rate-kill n14/E32/p2.94e-4; RdDM 293×
  still UNVERIFIED flag guard); adjudication ledger == archived
  `code/crowd8/redteam/STATUS-LINE-round7.json` (all 25 statuses in vocabulary).
- Both scripts exit 0. Existing checks untouched.

## JOB 2 — pre-registered bars (written before any executor numbers arrived)

`code/crowd8/redteam/PREREG-ROUND8.md` holds the kill/confirm thresholds for all 12
work orders. Standing rules enforced verbatim: **≥2 independent legs for ANY promotion**
(hold the line); n≥3 kill rule; F33 conditioning (pre-register partitions, no post-hoc
fitting); no double-counting of banked legs; exact tests; era- and register-matched
corpus legs with dispersion; clean fails are fails. Key per-order bars:

- **48 battery:** CONFIRM→LEAD needs ≥2 independent positive legs (M1-template
  interchangeability vs 94, grammatical-cell n≥3, era corpus allophony); anything less
  stays FLAGGED-UNTESTED — 48 does not enter the status line on one leg.
- **59 consolidation:** CONFIRMED needs ≥2 NEW legs + a falsifiable account of the S4#1
  frame; no recycling S1–S5/L1–L5.
- **01 battery:** MEDIUM→provisional or →WEAK both need ≥2 independent legs with a
  pre-registered decision rule; the bar must fire on the register-best comparator
  (the round-7 I1 failure: Guizot fired, Nesselrode v8 didn't). "Mutual exclusivity
  (59 wins)" denied in advance — not an available conclusion here.
- **84 windows:** new islets pre-registered before classification; ≥3 windows, zero
  adverses → LEAD; conditions are not expanded after seeing data.
- **00 rate model:** 00="pour"→provisional needs B1 or B3 ≤2× on the register-best
  corpus with per-file dispersion (the friendliest file doesn't clear it).
- **47 second window:** a new byte-exact 64-96-47 3-gram → n_eff=2 (strengthens LEAD,
  doesn't promote); 47="ce"→provisional needs ≥2 NEW legs.
- **67×9:** rules pre-registered before classification; all 9 into {et, veut} with zero
  BOTH conflicts or the fork demotes; neither word promotes on this battery.
- **62/93 allophony:** M1 kill-shot template; CONFIRM needs the N35/N39 discrimination
  (n≫2 independent cells, grammatical asymmetry, or cipher-internal merger calibration);
  93's rate-kill is banked, not a positive leg.
- **77/78 support:** ≥2 independent legs; T4 5-mer is banked; honest NULLs keep LEAD.
- **16 position test:** position classes pre-registered from contact phases BEFORE the
  test; n_eff≥3 for promotion consideration; clean fail = fail.
- **Mehemet-Ali:** never score bearing counts on manual tilings (per-window nulls only;
  assert arity); RdDM 293× citation = traceability violation; CONFIRMED needs ≥2 NEW legs.
- **columns refuge:** concrete falsifiable class + pre-registered test, or the claim stays
  LOGICALLY-OPEN-NO-EVIDENCE; cite softened lag-3 numbers (z≈4.6–4.77), never 5.6.

## Rulings on promotion recommendations

**None received.** `code/crowd8/report_inbox/` is empty as of this report. Recommendations
will be reviewed FIRST on arrival and rulings appended to
`code/crowd8/redteam/RULINGS-ROUND8.md` with file+line citations. Any executor number that
fails independent re-derivation kills the claim, with the exact failed number named.

## Files

- `code/crowd8/redteam/PREREG-ROUND8.md` — the pre-registered bars (canonical)
- `code/crowd8/redteam/STATUS-LINE-round7.json` — machine-readable round-7 status ledger
- `code/crowd8/redteam/RULINGS-ROUND8.md` — ruling log (pre-registration recorded;
  rulings appended on arrival)
- `code/crowd8/report_inbox/redteam-round8.md` — this note
