# Battery report: val-01-rival-sweep

**Target:** `val-01-rival-sweep` — candidate-inventory sweep beyond en/tain/on for 01.
**Date:** 2026-10-09. **Verdict: NULL** (fence outcome per pre-registered bar; 'ein' killed at kill grade within).
**Worker:** 978f3d73-90f0-4e81-b0ae-3e0e327440ac.

## Bar (verbatim, pre-registered)

> test letter-cluster hypotheses ('ain'/'ein'/'in'/'an') against the 14 undetermined windows (@195,@255,@327,@409,@484,@717,@940,@1255,@1261,@1440,@1462,@1634,@1653,@1731,@1818); name iff one parses at all windows with zero kill-grade contradictions, else fence

Note: the bars field lists 15 @-offsets while saying "14 undetermined windows". All 15 listed windows were tested; the count discrepancy changes nothing.

Numbered clauses:
- **C1:** Test 'ain' at all listed windows; name iff it parses at every window with zero kill-grade contradictions.
- **C2:** Test 'ein' at all listed windows; name iff it parses at every window with zero kill-grade contradictions.
- **C3:** Test 'in' at all listed windows; name iff it parses at every window with zero kill-grade contradictions.
- **C4:** Test 'an' at all listed windows; name iff it parses at every window with zero kill-grade contradictions.
- **C5:** If no hypothesis meets the name condition, fence the hypotheses per the bar.

## Method

Re-derived the repaired 1,847-pair / 96-type stream in-session from
`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`
(asserts held: 1,847 pairs, 96 types). `canonical.py` never used. R5005,
sealed gates, and the red-team adjudication queue untouched.

For each window, 01's positional constraint (word-initial vs word-internal)
was fixed from standing values only (§7: GT pencil 11=la, 70=pre, 82=m,
34=i, 29=er, 40=e, 46=que; granted 87=ce, 64=qui, 96=par, 17=fois, 79=tout,
00=pour, 84=on, 47=ce, 06=ent, 45=ce; provisional 59=est, 77=le;
30=pas standing LEAD). French-plausibility of each cluster in the forced
position was checked against the lane period corpus
(`code/side-period/corpus/`, 33.6M chars French-only after excluding the
German allgemeine-zeitung, adb-zeschau, and metternich files).

## Window-level evidence (@-offsets, ±4 context, standing values substituted)

| @ | context (01 marked) | 01 position (from standing values) |
|---|---|---|
| 195 | ce [98] [56] ce \|01\| [21] [60] [08] | WORD-INITIAL (47=ce standalone) |
| 255 | [65] [63] pour [66] \|01\| [91] [32] [43] | undetermined (66 open) |
| 327 | [15] [63] [71] [10] \|01\| [19] pour [92] | undetermined (10/19 open) |
| 409 | [69-N] [26] pour [33] \|01\| [02] [53] on | undetermined (33/02 open) |
| 484 | pour [13] [52] pas \|01\| [19] qui [76] | WORD-INITIAL (30=pas LEAD) |
| 717 | [63] pour [66] [86] \|01\| [02] [21] [80] | undetermined (86/02 open) |
| 940 | [33] [21] qui [37] \|01\| [07] [50] e | word-internal/bound (A12 37-01 unit) |
| 1255 | pas ent [65-N] que \|01\| [61] [31] er | WORD-INITIAL (46=que word-final) |
| 1261 | [31] er [69-N] [88] \|01\| [09] la [50] | undetermined (88 open) |
| 1440 | m [16] [24] [85] \|01\| [52] [68] est? | undetermined (85/52 open) |
| 1462 | [86] [66] tout fois \|01\| [21] [62] [48] | WORD-INITIAL (17=fois standalone) |
| 1634 | [33] [21] qui [37] \|01\| [74] ce [74] | word-internal/bound (A12 37-01 unit) |
| 1653 | [03] [38] m [16] \|01\| [56] [37] la | undetermined (16/56 open) |
| 1731 | [88] [24] pas [15] \|01\| [56] pas ent | undetermined (15/56 open) |
| 1818 | [42] ent er [37] \|01\| [02] [09] [19] | word-internal/bound (A12 37-01 unit) |

No window forces 01 into a single-letter slot via GT-letter adjacency, so
the clusters cannot be killed on letter-tier grounds. The discriminating
test is word-initial position: a cluster that cannot begin a French word
dies at every word-initial window.

Corpus results (French-only, 33.6M chars):
- Words beginning with "ain": "ainsi" 3,816x, "ainée" 3x (OCR of "aînée"),
  "Ain" 9x (proper noun). → 'ain' word-initial is French-plausible (via "ainsi").
- Words beginning with "ein": 0 genuine French. Residual hits are German
  fragments ("ein" 9x, "eine" 5x) and OCR noise ("einpoisoiiiu", "eink",
  "eing"). → 'ein' word-initial is impossible in French.
- Words beginning with "in": "intérêt", "influence", "instant", … → plausible.
- Words beginning with "an": "an", "ans", "anglais", "année", … → plausible.
- ('ein' word-INTERNAL is French-plausible: "peine" 1,554x, "reine",
  "plein", "dessein" — so the kill is positional, not global.)

## Per-clause pass/fail

- **C1 ('ain'):** No kill-grade contradiction at any window. Word-initial
  windows admit "ainsi"; word-internal windows admit "-ain-" freely.
  Not positively parsed at all windows (neighbors mostly open) → NOT NAMED,
  **FENCED** per bar.
- **C2 ('ein'):** KILL-GRADE contradictions at @195, @1255, @1462 (01 forced
  word-initial; zero genuine French words begin with "ein" in 33.6M chars),
  with @484 as a fourth supporting window (30=pas LEAD). → hypothesis
  **KILLED**; not named.
- **C3 ('in'):** No kill-grade contradiction at any window. Not positively
  parsed → NOT NAMED, **FENCED** per bar.
- **C4 ('an'):** No kill-grade contradiction at any window. Not positively
  parsed → NOT NAMED, **FENCED** per bar.
- **C5:** No hypothesis met the name condition → fence outcome. 'ein' is
  dead at kill grade; 'ain'/'in'/'an' are shelved (re-openable when more
  neighbor values are banked — the fence is evidentiary, not terminal).

## Verdict: NULL

No candidate named. Per §4 the null proposes follow-ups (all verified
ABSENT from battery-queue.json; left for the supervisor to queue):

1. **`val-01-in-an-retest`** (P3) — Re-test 'in'/'an' at the word-initial
   windows (@195, @1255, @1462) once the right-neighbors (21, 61) are
   valued; a valued neighbor discriminates the parse and could promote.
2. **`val-01-ainsi-test`** (P4) — Test 'ain' specifically as "ainsi": check
   whether the followers at the word-initial windows admit "si"
   continuations; kill 'ain' iff no window admits it.
3. **`redteam-01-rival-input`** (P2, gather-only) — Package the 'ein' kill
   and the 'ain'/'in'/'an' fence as red-team input for the 01 docket
   (01 split/polyvalence); battery decides nothing.

## Scope

Does not name 01's value. Does not touch the standing 'en'/'on' readings
or the A12 37-01 frame. No standing or red-team verdict contradicted; §7
intact. The 'ein' kill is positional (word-initial windows only) and does
not affect 'ein' word-internal French plausibility elsewhere.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-val-01-rival-sweep.md`
- Queue: `val-01-rival-sweep` → status `verdict`, result `null`
  (pre-write assert passed: was queued/verdictless; temp-file + rename;
  own entry only; no downgrade; disk re-validated).
- Lock `code/crowd17/next-token/locks/val-01-rival-sweep.lock` created on
  start (agent 978f3d73-90f0-4e81-b0ae-3e0e327440ac, 2026-10-09T17:13:13Z),
  deleted on completion.
