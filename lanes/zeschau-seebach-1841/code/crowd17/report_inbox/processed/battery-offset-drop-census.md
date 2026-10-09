# Battery verdict: offset-drop-census

- Target: `offset-drop-census` (battery-queue.json, priority 4, status queued)
- Claim: Census all 28 odd-length rows: does the EM's drop-end choice (first vs last digit) correlate with row-label order or page runs?
- Evidence: Complements (does not duplicate) queued seg-a1_01-hybrid-phase, which owns the transcription-error rival itself; this is the process-level complement.

## Bar (verbatim, numbered)

C1. The census is complete and byte-exact: all 28 odd-length rows identified from the raw transcription; the EM's drop-end choice recorded per row.
C2. At least one association test fires at the lane's standard (|z|>2 for the runs test; Fisher p<0.05 for the halves and line-start contrasts; permutation p<0.05 for page heterogeneity).
C3. The pattern, if found, is stated in a form usable as an extrinsic process prior for a1_01's phase.

## Method

1. Read BATTERY-PROTOCOL.md first. Created `locks/offset-drop-census.lock` on start (agent 77bf5fd9-a9da-430c-af4a-bdc799ee32ca, 2026-10-09T20:50:00Z); deleted on completion.
2. Loaded rows from `data/upstream-ct_R5005.txt` (70 rows, 3,764 digits) and offsets from `data/upstream-offsets.json` (the EM's choices). Cross-checked against `code/side-keyhunt/repaired_offsets.json`: the only upstream/repaired difference is a5_03 (1 -> 0), and a5_03 is even-length (52 digits), so the census is identical under both. `canonical.py` never used.
3. Drop-end semantics for odd-length rows, per the parse `[s[i:i+2] for i in range(o, len(s)-1, 2)]`: offset 0 drops the LAST digit; offset 1 drops the FIRST digit. Verified on the bytes (odd L: offset 0 covers digits 0..L-2; offset 1 covers digits 1..L-1).
4. Ran the association tests in-session: Wald-Wolfowitz runs test on the 28-row label-ordered sequence; Fisher exact (two-sided) for first-half vs second-half, for first-odd-row-per-page vs rest, and for a1-page vs rest; permutation test (200,000 draws) for page heterogeneity with the chi-square statistic.

## Findings

### Census (all 28 odd-length rows, row-label order)

| row | digits | EM offset | drop end | page |
|-----|--------|-----------|----------|------|
| a1_01 | 71 | 0 | last | a1 |
| a1_02 | 65 | 0 | last | a1 |
| a1_03 | 63 | 0 | last | a1 |
| a1_05 | 59 | 1 | first | a1 |
| a2_00 | 55 | 0 | last | a2 |
| a2_06 | 51 | 0 | last | a2 |
| a2_10 | 53 | 0 | last | a2 |
| a2_11 | 51 | 0 | last | a2 |
| a3_01 | 55 | 0 | last | a3 |
| a4_02 | 51 | 0 | last | a4 |
| a5_00 | 53 | 1 | first | a5 |
| a5_01 | 55 | 1 | first | a5 |
| a5_08 | 53 | 1 | first | a5 |
| a5_10 | 49 | 0 | last | a5 |
| a6_04 | 51 | 1 | first | a6 |
| a6_07 | 41 | 0 | last | a6 |
| a6_09 | 41 | 0 | last | a6 |
| a7_02 | 57 | 0 | last | a7 |
| a7_04 | 55 | 0 | last | a7 |
| a7_05 | 55 | 0 | last | a7 |
| a7_06 | 57 | 1 | first | a7 |
| a7_09 | 57 | 1 | first | a7 |
| a7_10 | 55 | 0 | last | a7 |
| a8_01 | 57 | 0 | last | a8 |
| a8_03 | 57 | 1 | first | a8 |
| a8_04 | 57 | 1 | first | a8 |
| a8_05 | 55 | 1 | first | a8 |
| a8_11 | 51 | 0 | last | a8 |

Totals: 10 first-drops, 18 last-drops.

### C1 — census complete: PASS

All 28 odd-length rows found (42 even-length rows excluded by byte count). Each drop-end choice derives directly from the EM offset with the semantics verified above. Upstream and repaired offsets agree on all 28 rows.

### C2 — association tests: FAIL (no test fires)

1. **Runs test on the label-ordered sequence** (L,L,L,F,L,L,L,L,L,L,F,F,F,L,F,L,L,L,L,L,F,F,L,L,F,F,F,L): 11 runs; E[runs]=13.857; sd=2.376; **z=-1.20**. Lane bar |z|>2 not met. No order clustering.
2. **First half (rows 1-14) vs second half (rows 15-28)**: F=4/10 vs F=6/8; Fisher exact **p=0.6946**. The bar's example pattern ("leading-digit drops clustering at line starts") is absent.
3. **First odd row of each page vs the rest**: F=2/6 vs F=8/12; Fisher exact **p=0.6692**. No line-start clustering.
4. **Page heterogeneity** (a1:1/3, a2:0/4, a3:0/1, a4:0/1, a5:3/1, a6:1/2, a7:2/4, a8:3/2): chi-square=7.529, df=7; permutation test (200,000 draws) **p=0.4025**. The descriptive F-heaviness of pages a5 and a8 is consistent with chance under the page sizes.
5. **a1's page (a1_01's page) vs the rest**: F=1/3 vs F=9/15; Fisher exact **p=1.0**. Even the page-local evidence carries nothing.

### C3 — pattern for a1_01's phase: moot

No pattern exists at the lane's standard, so there is nothing to state as a prior. Recorded for the venue: a1_01's own EM choice is offset 0 (drop LAST digit, 71-digit row). Nothing in this census supplies an extrinsic process prior for or against that choice.

### Verdict: NULL

The census is byte-exact (C1 passes) and the position tests have no power problem at this n — they simply find nothing. This is an evidentiary negative, not a kill-grade result: it says no POSITION-based transcription-process pattern exists at battery grade; it does not rule out a content-based pattern (e.g. the dropped digit's value) or a pattern in the even rows' two-digit drops. The bar's promote condition (a usable pattern) is not met.

## Scope

- Position-based tests only (row order, halves, line starts, pages). The dropped digits' VALUES were not tested.
- Even rows (42) excluded by design: their offset-1 choice drops two digits, a different process question.
- Untouched: seg-a1_01-hybrid-phase (owns the transcription-error rival), the repaired offsets themselves, R5005, sealed gates, red-team adjudication queue. No standing or red-team verdict contradicted.
- Canonical-stream caveat stands (68 of 70 upstream row offsets unvalidated).

## Follow-ups (for supervisor queuing; all verified ABSENT from battery-queue.json)

1. `offset-drop-content` (P4) — content-based process test: does the dropped digit's value (e.g. leading 0 vs other) predict the drop end across the 28 odd rows? A content pattern would supply the extrinsic prior the position tests failed to find.
2. `even-row-offset2-audit` (P4) — census the EM's offset-1 choices on the 42 even rows (each drops 2 digits: first+last): do they cluster by page or row order? More power than the odd-row census; tests the same process hypothesis.
3. `a101-phase-extrinsic` (P4, gather-only) — package this negative result as explicit red-team input for the a1_01 phase venue: no extrinsic position-based process prior exists at battery grade; the phase question rests on intrinsic evidence.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-offset-drop-census.md`
- Queue: `offset-drop-census` queued -> `verdict`/`null`, 2026-10-09 (pre-write assert passed: was queued/verdictless; target-id-unique tmp `battery-queue.json.offset-drop-census.tmp` + atomic rename; disk re-validated; own entry only; no downgrade; no tmp leftover)
- Lock `locks/offset-drop-census.lock`: created on start (2026-10-09T20:50:00Z, no stale lock), deleted on completion (verified gone). R5005, sealed gates, red-team adjudication queue untouched.
