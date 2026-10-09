# Battery verdict: stem-03

## Bar (verbatim from battery-queue.json, pre-registered)
"promote iff >=2 verb-stem frames"

**Restated as numbered pass/fail clauses:**
- **C1:** At least two windows exist where 03 functions as a verb stem, on the repaired stream, under standing values.
- **C2:** No listed adverse. (Queue lists none.)

## Method
- Read BATTERY-PROTOCOL.md first; lock `locks/stem-03.lock` created on start, deleted on completion.
- Re-derived the repaired stream in-session from `data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `repair_parse.py` (pair up from row offset, drop trailing odd digit). Verified: **1,847 pairs, 96 groups**.
- `canonical.py` never used. R5005, sealed gates, red-team queue untouched.

## Census (1-based @, center = 03)
n(03) = 20:

| @ | left | right | row |
|---|------|-------|-----|
| 32 | 30 | 64 | a1_00 |
| 337 | 40 | 64 | a2_05 |
| 600 | 40 | 39 | a4_00 |
| 658 | 30 | 62 | a4_02 |
| 665 | 80 | 62 | a4_02 |
| 675 | 80 | 64 | a5_00 |
| 692 | 60 | 39 | a5_00 |
| 723 | 77 | 91 | a5_02 |
| 887 | 37 | 02 | a5_08 |
| 995 | 30 | 60 | a6_01 |
| 1015 | 47 | 24 | a6_02 |
| **1031** | 01 | **29** | a6_03 |
| 1238 | 10 | 40 | a7_01 |
| **1321** | 24 | **29** | a7_04 |
| 1368 | 60 | 30 | a7_06 |
| **1595** | 81 | **29** | a8_02 |
| 1646 | 60 | 64 | a8_04 |
| 1650 | 10 | 38 | a8_04 |
| 1676 | 60 | 39 | a8_05 |
| 1791 | 47 | 00 | a8_09 |

"03 29" bigram occurs **exactly 3x** stream-wide (@1031, @1321, @1595). "03 29 80" trigram exactly 3x, byte-identical loci.

## Verb-stem frames

29='er' is banked ground truth, so "03 29" = stem + infinitive ending, an infinitive frame. Three independent frames:

- **F1 — @1321 (a7_04):** "…15 **24 03 29** 80…" = "faire [03]er". 24='faire' is battery-promoted. Causative *faire* + infinitive is grammatical 1841 French. Verb-stem frame.
- **F2 — @1031 (a6_03):** "…87 **01 03 29** 80 77…" = "[ce] [01] [03]er! [80]-le…" — exclamatory infinitive + imperative with enclitic 'le' (per imp-80-set's byte-traced parse; 87='ce' promoted, 77='le' provisional). "03 29" infinitive unconditional under 29='er' GT. Verb-stem frame.
- **F3 — @1595 (a8_02):** "…08 **81 03 29** 80…" = "[81] [03]er…" — infinitive under the A8 80 verb-frame family. Verb-stem frame.

F1, F2, F3 are independent windows, independent rows, independent governors (faire / nominal / 80-frame). No window forces any of the three false under standing values.

## Per-clause pass/fail
- **C1: PASS** — 3 verb-stem frames, bar requires >=2.
- **C2: PASS** — no adverses listed.

## Verdict: PROMOTE (class-level)

03 = **verb stem** (class, not value). 03's value stays open. Battery grade; needs red-team ratification like every class promote.

**Note for the red team (not a finding, not a declaration):** the remaining 17 windows are not all verb-compatible ("[03] qui" x4, "pas [03]" x3, "ce [03]" x2, "[03] à" x3, "[03]e" x1 — per battery-stem-03-value's census). A single-valued stem under this class promote would need the noun-family to re-segment; otherwise this is a §7 split question. No polyvalence declared here. No standing verdict is contradicted or downgraded; battery-stem-03-value's NULL (value unnamed) and imp-80-set's NULL both stand untouched.
