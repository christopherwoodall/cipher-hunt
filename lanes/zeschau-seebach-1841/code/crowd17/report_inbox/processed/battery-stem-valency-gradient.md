# Battery report: stem-valency-gradient

- Target id: `stem-valency-gradient`
- Claim: "reframe the stem distinction as a distributional test: governor/complement divergence (33 vs 86) across the full census"
- Date: 2026-10-09
- Worker: battery worker (subagent 367ccf30-21d5-4998-9522-bc4b31ddf167)
- Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json +
  data/upstream-ct_R5005.txt, parsed per code/side-keyhunt/repair_parse.py).
  Re-derived in-session; asserted 1,847 pairs / 96 types. `canonical.py` never
  used. R5005 not touched. All @-offsets are 0-based repaired-stream indices.
- Lock: code/crowd17/next-token/locks/stem-valency-gradient.lock (created at
  start, deleted on completion; no prior lock existed).

## Bar (verbatim, pre-registered before testing)

"compute governor/complement distribution divergence across the full census
instead of strict set disjointness"

Numbered pass/fail clauses (restated before testing, not modified after):

1. (C1) Compute the governor-distribution divergence between the 33 stem
   cells (n=5) and the 86 stem cells (n=4) over the byte-exact full census,
   reporting the Jensen-Shannon divergence (bits) and an exact permutation
   homogeneity p-value (lane precedent: battery-suc-60-68-standalone).
2. (C2) Compute the complement-distribution divergence (post-29 groups)
   between the 33 and 86 stem cells over the same census, with the same
   statistics.
3. (C3) State the gradient reading at the lane's standard (alpha=0.05):
   whether the divergence test confirms the valency-gradient claim, and
   record the point estimates honestly either way.
4. (C4) Adverse answered: do NOT re-run stem-33-86's bar (stem-vs-whole
   adjudication per window with <=10% orphan rate). Only the 33-vs-86
   comparison is in scope; the stem-cell census is re-derived, not
   re-adjudicated.

## Method

1. Re-derived the repaired stream in-session (1,847 pairs / 96 types
   asserted). `canonical.py` never used. R5005, sealed gates, and the
   red-team adjudication queue untouched.
2. Defined "stem cell" exactly as battery-stem-class-split did: a group
   immediately preceding 29='er' (banked GT), i.e. the "[X]er" infinitive
   shape. For each window "pre X 29 post", governor = pre, complement = post.
3. Re-verified the full "X 29" census byte-exactly against
   battery-stem-class-split's bar cells: 33 x5, 86 x4, 06 x4, 34/64/03 x3,
   11/46/48 x2 — all match, plus 17 singleton X-29 cells (01, 08, 10, 14,
   16, 31, 36, 40, 43, 44, 50, 63, 84, 88, 92, 93, 94) that are not in the
   33/86 comparison.
4. Statistics, pre-registered shapes:
   - Jensen-Shannon divergence (base-2 bits, range [0,1]) over the union
     support of each distribution pair.
   - Exact permutation homogeneity test, chi-square-type statistic over the
     union of observed supports (lane precedent), enumerating ALL
     C(9,4)=126 label splits (n=5 vs n=4), so the p-values are exact, not
     Monte Carlo.
   - Supporting 2x2 arms (Fisher's exact, two-sided): the ce-complement
     asymmetry (33: 87 x2 / no-ce x3; 86: ce 0 / no-ce x4) and the
     veut/pour governor asymmetry (33: veut 3 / pour 0; 86: veut 1 / pour 2).
5. Standing values adopted as premises (not re-litigated): 29="er",
   87="ce", 47="ce" (A4), 00="pour" (A9), 67="veut" by the positional rule
   (follower infinitive-shaped at all four 67-governed stem windows),
   77="le" provisional, §7 sole polyvalence (67 et/veut).

## Census (byte-exact, re-derived)

### 33 (n=5)

| @ (0-based) | row   | window       | governor (pre) | complement (post) |
|-------------|-------|--------------|----------------|-------------------|
| 274         | a2_03 | 06 67 33 29 89 84 | 67 (veut) | 89 |
| 627         | a4_01 | 59 37 33 29 87 78 | 37 (open) | 87 (ce) |
| 1233        | a7_01 | 29 47 33 29 85 56 | 47 (ce)   | 85 |
| 1425        | a7_08 | 21 67 33 29 87 63 | 67 (veut) | 87 (ce) |
| 1478        | a7_10 | 06 67 33 29 82 16 | 67 (veut) | 82 (m, +16) |

- Governor distribution: {67:3, 37:1, 47:1}.
- Complement distribution: {89:1, 87:2, 85:1, 82:1}.

### 86 (n=4)

| @ (0-based) | row   | window       | governor (pre) | complement (post) |
|-------------|-------|--------------|----------------|-------------------|
| 432         | a2_09 | 63 77 86 29 82 16 | 77 (le, prov.) | 82 (m, +16) |
| 1376        | a7_06 | 98 00 86 29 89 84 | 00 (pour) | 89 |
| 1392        | a7_07 | 29 67 86 29 89 16 | 67 (veut) | 89 |
| 1826        | a8_11 | 97 00 86 29 82 38 | 00 (pour) | 82 (m, +38) |

- Governor distribution: {77:1, 00:2, 67:1}.
- Complement distribution: {89:2, 82:2}.
- @1392 is the single shared governor ("67 86 29"; the positional rule
  fires here — the window that killed stem-class-split's strict C1).

## Per-clause results

### C1 (governor divergence): PASS (computed)

- Union support: {00, 37, 47, 67, 77}.
- Jensen-Shannon divergence: **0.6286 bits** (max 1.0) — numerically
  substantial.
- Exact permutation homogeneity test: chi2 = 5.962, **p = 0.2698**
  (all 126 splits enumerated). Not significant at alpha=0.05.

### C2 (complement divergence): PASS (computed)

- Union support: {82, 85, 87, 89}.
- Jensen-Shannon divergence: **0.3958 bits**.
- Exact permutation homogeneity test: chi2 = 3.600, **p = 0.5714**.
  Not significant at alpha=0.05.

### C3 (gradient reading at the lane's standard): STATED

- The gradient claim is **not confirmed** by the distributional reframe at
  the lane's standard. Both divergence tests fail to reject homogeneity
  (p=0.27 governors, p=0.57 complements).
- Supporting 2x2 arms are directionally consistent but likewise
  underpowered: ce-complement Fisher p=0.4444 ([2,3;0,4]); veut/pour
  governor Fisher p=0.4000 ([3,0;1,2]).
- This is the power-gap phenomenon documented in
  battery-suc-60-68-standalone: at the n the stream supplies for these
  cells (5 vs 4), the divergence test has essentially no discriminating
  power. Failing to reject homogeneity is not evidence of uniformity.
- Consequence: the strict bar's single-window failure (governor 67 shared
  via @1392) is NOT rescued by the distributional reframe at battery
  grade. The sharpest arm of the distinction remains the ce-complement
  asymmetry in point estimates (33 takes 'ce' x2; 86 takes 'ce' 0/4 across
  87/47/45 per stem-class-split C2) — which is exactly the arm owned by
  queued ce-complement-86-negative, and the strict-bar fix owned by queued
  veut-86-1392-adjudicate. No duplication: those targets are not re-run.

### C4 (adverse): ANSWERED

stem-33-86's bar (stem-vs-whole adjudication per window, <=10% orphan
rate) was not re-run. The stem-cell census was re-derived byte-exactly;
no window's stem-vs-whole classification was re-adjudicated. §7 intact;
no polyvalence declared; no standing or red-team verdict contradicted or
downgraded.

## Verdict: PROMOTE (finding grade)

The divergence computation the bar asked for is complete, byte-exact, and
recorded with exact statistics:

- Governors (33 vs 86): JS = 0.6286 bits; exact permutation p = 0.2698.
- Complements (33 vs 86): JS = 0.3958 bits; exact permutation p = 0.5714.
- ce-complement Fisher p = 0.4444; veut/pour governor Fisher p = 0.4000.

Headline finding: the distributional gradient does not reach significance
at the lane's standard — the test is underpowered at n=5/4 (power gap).
The reframe delivers its numbers; they say the strict bar's @1392 failure
is not rescued here, and the live arms stay with the queued
ce-complement-86-negative and veut-86-1392-adjudicate targets. No
follow-ups proposed — this is a completed computation, not a null; the
regeneration paths above are already queued.

## Bookkeeping

- Lock created at start (agent id + UTC), deleted on completion.
- Queue: `battery-queue.json` `stem-valency-gradient` → status `verdict`,
  result `promote`, date 2026-10-09 (pre-write assert confirmed
  queued/verdictless; temp-file + rename; JSON re-validated; own entry
  only; no other entry touched; no downgrade).
- R5005, sealed gates, red-team adjudication queue untouched.
