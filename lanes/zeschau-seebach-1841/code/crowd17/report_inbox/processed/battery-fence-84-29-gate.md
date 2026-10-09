# Battery report: fence-84-29-gate — 84-successor census evidence package (red-team adjudication only)

- Target: `fence-84-29-gate` (priority 2)
- Claim: Gated evidence package: @146 under a hypothetical non-'on' 84 reading (red-team adjudication only)
- Verdict: **promote** (evidence package complete; no value declared — this is NOT a value promotion)
- Date: 2026-10-08
- Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json +
  data/upstream-ct_R5005.txt, parsed like code/side-keyhunt/repair_parse.py).
  canonical.py never used. R5005 untouched. n(84)=25 re-derived this run;
  distinct tokens=96, n(29)=45.
- Lock: locks/fence-84-29-gate.lock (created on start, deleted on completion).
  No stale lock existed.

## 1. Pre-registered bar (verbatim)

> gather the 84-successor census evidence for red-team adjudication; no value declared

Numbered pass/fail clauses (frozen before grading; not modified after seeing data):

1. **C1 — full census**: all 25 occurrences of 84 in the repaired stream are
   enumerated with @-offsets, rows, and successors; the successor counts sum
   to 25.
2. **C2 — 'on'-compatibility grading**: each distinct successor is graded
   CLEAN / NO-CONTRADICTION / FENCED under standing values, with @-offsets
   cited; the grading must show whether 29 is the unique resisting successor
   (84->29 x1).
3. **C3 — §7 compliance**: no second polyvalence of 84 is declared; no value
   is proposed for 84 at @146 or anywhere else; the package is evidence-only
   for red-team adjudication.

Grading key (standing values, protocol §7): banked 11=la, 70=pre, 82=m,
34=i, 29=er, 40=e, 46=que; granted 87=ce, 64=qui, 96=par, 17=fois,
79=tout, 00=pour, 84=on, 47=ce (allophone tier); provisional 59=est,
77=le. CLEAN = window parses under 84='on' with no residual. NO-CONTRADICTION
= successor value unknown/open, nothing contradicts 'on'. FENCED = previously
fenced residual (A15-C3 R1/R2; lon-29-146 R3).

## 2. Method

Re-derived from the repaired stream in this run (python3 against
repaired_offsets.json + upstream-ct_R5005.txt). @-offsets are 0-based
repaired-stream pair indices. Successor = the pair immediately right of each
84 occurrence. Compatibility grading uses standing values only; where the
successor token's value is unsettled, 'on' is not contradicted, so the window
grades NO-CONTRADICTION (a claim about absence of contradiction, not a parse).

## 3. Census evidence (all 25 windows)

| @ | row | window (±3) | succ | grade |
|---|-----|-------------|------|-------|
| 146 | a1_04 | 67 64 77 **84** 29 87 64 | 29 | FENCED (R3, lon-29-146 null) |
| 154 | a1_04 | 47 46 66 **84** 26 35 58 | 26 | NO-CONTRADICTION |
| 167 | a1_05 | 11 24 82 **84** 53 12 48 | 53 | NO-CONTRADICTION |
| 260 | a2_02 | 32 43 77 **84** 74 45 93 | 74 | NO-CONTRADICTION |
| 276 | a2_03 | 33 29 89 **84** 91 37 61 | 91 | NO-CONTRADICTION |
| 310 | a2_04 | 20 17 46 **84** 24 37 78 | 24 | NO-CONTRADICTION |
| 391 | a2_07 | 36 62 91 **84** 73 34 67 | 73 | NO-CONTRADICTION |
| 412 | a2_08 | 01 02 53 **84** 51 37 78 | 51 | NO-CONTRADICTION |
| 473 | a2_10 | 06 67 46 **84** 24 37 78 | 24 | NO-CONTRADICTION |
| 788 | a5_04 | 94 74 65 **84** 06 77 64 | 06 | NO-CONTRADICTION |
| 857 | a5_07 | 64 32 48 **84** 02 24 49 | 02 | NO-CONTRADICTION |
| 1021 | a6_03 | 66 91 53 **84** 92 64 45 | 92 | NO-CONTRADICTION |
| 1058 | a6_04 | 45 23 77 **84** 09 98 83 | 09 | NO-CONTRADICTION |
| 1151 | a6_08 | 67 33 66 **84** 02 00 92 | 02 | NO-CONTRADICTION |
| 1189 | a6_10 | 59 42 06 **84** 59 46 07 | 59 | CLEAN ("on est") |
| 1290 | a7_03 | 00 11 17 **84** 59 35 94 | 59 | CLEAN ("on est") |
| 1378 | a7_06 | 86 29 89 **84** 92 69 13 | 92 | NO-CONTRADICTION |
| 1418 | a7_08 | 34 52 32 **84** 79 15 33 | 79 | CLEAN ("on tout") |
| 1447 | a7_09 | 37 64 77 **84** 59 36 67 | 59 | CLEAN ("on est"; sister of @146) |
| 1485 | a7_10 | 62 46 77 **84** 24 87 08 | 24 | NO-CONTRADICTION |
| 1501 | a7_11 | 89 41 74 **84** 33 42 33 | 33 | NO-CONTRADICTION |
| 1620 | a8_03 | 42 44 11 **84** 78 66 67 | 78 | FENCED (R1, A15-C3) |
| 1665 | a8_04 | 80 22 94 **84** 64 06 91 | 64 | FENCED (R2, A15-C3) |
| 1764 | a8_08 | 93 06 77 **84** 09 24 87 | 09 | NO-CONTRADICTION |
| 1803 | a8_10 | 87 64 77 **84** 59 35 94 | 59 | CLEAN ("on est"; sister of @146) |

Successor counts: 59 x4, 24 x3, 02 x2, 92 x2, 09 x2, 29 x1, 26 x1, 53 x1,
74 x1, 91 x1, 73 x1, 51 x1, 06 x1, 79 x1, 33 x1, 78 x1, 64 x1. Sum = 25.

Grade totals: CLEAN 5 windows (59 x4, 79 x1); NO-CONTRADICTION 17 windows
(24 x3, 02 x2, 92 x2, 09 x2, 26, 53, 74, 91, 73, 51, 06, 33 x1);
FENCED 3 windows (29 R3 @146; 78 R1 @1620; 64 R2 @1665).

Notes on grades:
- 92's value is unsettled (the 09/92 "-ère" value was killed); its two windows
  raise no 'on' contradiction.
- R1 (@1620, succ 78) and R2 (@1665, succ 64) are fenced residuals under the
  'on' reading itself (A15-C3), not alternative-reading candidates; only @146
  actively resists 84='on' (no placement of 29='er' covers the span —
  lon-29-146 §4).
- 78's value is open (ver78 frames), 64='qui' granted; neither fact alone
  forces or blocks a reading — recorded as-is for adjudication.

## 4. Per-clause verdict

- **C1 — PASS**: all 25 successors enumerated above with @-offsets and rows;
  counts sum to 25; n(84)=25 and n(29)=45 re-derived from the stream.
- **C2 — PASS**: every distinct successor graded with cited windows; 29 is the
  unique resisting successor (84->29 x1 stream-wide, @146, fenced R3).
- **C3 — PASS**: no value proposed for 84 at @146 or anywhere else; §7 sole
  polyvalence (67) untouched; adjudication left entirely to the red team.

Adverse "§7 sole-polyvalence law: this target never declares; red team
adjudicates" — ANSWERED by compliance (no declaration made, package is
evidence-only).

## 5. Verdict: promote — evidence package complete (NOT a value promotion)

The census package is complete: 25/25 windows graded, 29 confirmed as the sole
resisting successor, no value declared, §7 honored. The A15 grant of 84='on'
is untouched. The red team receives:

1. The full 84-successor census above (24/25 windows either parse under 'on'
   or raise no 'on' contradiction; @146 is the sole resister).
2. The structural frame at @146 for adjudication: left context '67 64 77'
   (67 polyvalent et/veut; 64=qui; 77='le' PROVISIONAL — itself unsettled,
   cf. lon-legs-census); right context '29 87 64' (29=er banked, word-final
   -er profile; 87=ce granted; 64=qui). Under standing values this reads
   "[67] qui le on er ce qui" and no parse covers it (lon-29-146 §4).
3. Caveat: any adjudicated reading must also survive the sister '64 77 84'
   windows @1447 and @1801, which parse cleanly as "qui l'on est" —
   the @146 anomaly is strictly local.

No follow-up targets are queued by this report (package complete; this is a
promote). Nothing is written to the red-team adjudication queue — package
only, per the brief.
