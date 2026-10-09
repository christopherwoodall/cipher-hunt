# Battery verdict: val-26-copula-gather

- Target: `val-26-copula-gather` (battery-queue.json, priority 3, status queued)
- Claim: Gather the 1690 frequency-uniformity data for 26 vs 59 (homophony candidacy).
- Date: 2026-10-09.
- Stream: repaired 1,847-pair / 96-type parse (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`; asserts held: 1,847 pairs, 96 types). `canonical.py` NOT used. R5005, sealed gates, red-team queue untouched. All @-offsets 0-based.

## Bar (verbatim, pre-registered)

"tabulate the 8 legs' frames against 59's A1 'est [pred]' windows for distributional comparison; no naming, evidence only"

**Restated as numbered pass/fail clauses (frozen before testing):**
1. **C1 (tabulate):** the 8 legs' frames are tabulated against 59's A1 'est [pred]' windows with distributional comparison.
2. **C2 (no naming):** no value named, no adjudication made — evidence only.

Parent context: `battery-qui-fol-23-26-value` (NULL, 2026-10-09) found 26 carries 8 independent copula/verb legs, but the only nameable value is "est" — blocked by §7's sole-polyvalence rule (59=est provisional; 67 et/veut the only true polyvalence). This battery gathers the frequency/uniformity and frame evidence for the red-team homophony question.

## Evidence gathered

### 1. Frequencies

- n(26)=17, n(59)=27 (of 1,847 pairs). 59 provisional "est"; 26 class-open with 8 copula/verb legs.
- 26 loci: 129, 155, 240, 406, 531, 601, 655, 842, 934, 992, 1250, 1470, 1560, 1628, 1707, 1753, 1769.
- 59 loci: 103, 216, 316, 448, 463, 528, 554, 559, 624, 763, 825, 834, 912, 1178, 1186, 1190, 1210, 1291, 1443, 1448, 1496, 1511, 1715, 1777, 1796, 1804, 1833.

### 2. 1690 frequency-uniformity tests (26 vs 59)

- **χ² vs uniform on (17, 27):** χ²=2.2727, df=1, **p=0.1317** → fail to reject (bar p>0.05; the necessary uniformity condition passes).
- **Wald–Wolfowitz runs test on the despatch-order membership sequence** (n1=17, n2=27): observed runs=25, E[runs]=21.86, sd=3.10, **z=+1.01** → |z|<2, interleaved; no clumping (the cycling check passes).
- Sequence (6=26, 9=59): `96696969996996969996966999969996996669669999`.
- Note: uniformity is necessary but INSUFFICIENT per lane law (homophone-cd precedent: SPLIT on segregated frames even with uniformity).

### 3. The 8 legs' frames (adopted from battery-qui-fol-23-26-value, byte-verified)

| # | @ | frame | predecessor | successor | shape |
|---|---|---|---|---|---|
| L1 | 155 | `84 [26] 35` | 84=on (A15) | 35 | "on [X]" finite-verb |
| L2 | 406 | `69 [26] 00` | 69 noun-class (R19-109) | 00=pour | "[N] [X] pour" |
| L3 | 531 | `64 [26] 32` | 64=qui (granted) | 32 (A1 pred) | "qui [X] [pred-32]" copula |
| L4 | 601 | `39 [26] 96` | 39 | 96=par | "[X] par [Y]" |
| L5 | 842 | `94 [26] 12` | 94=ne (STRONG LEAD) | 12 | "ne [X]" |
| L6 | 934 | `69 [26] 00` | 69 noun-class | 00=pour | "[N] [X] pour" |
| L7 | 1628 | `69 [26] 00` | 69 noun-class | 00=pour | "[N] [X] pour" |
| L8 | 1769 | `64 [26] 37` | 64=qui (granted) | 37 (A1 pred) | "qui [X] [pred-37]" copula |

Leg predecessor set: {84, 69×3, 64×2, 39, 94}. Leg successor set: {35, 00×3, 32, 96, 12, 37}.

### 4. 59's A1 'est [pred]' windows (11 windows, byte-verified)

| @ | window | predecessor | successor | shape |
|---|---|---|---|---|
| 316 | `64 59 32` | 64=qui | 32 (A1) | "qui [X] [pred-32]" |
| 448 | `61 59 32` | 61 | 32 (A1) | "[X] [pred-32]" |
| 463 | `11 59 42` | 11=la | 42 (A1) | "la [X] [pred-42]" |
| 528 | `44 59 37` | 44 | 37 (A1) | "[X] [pred-37]" |
| 624 | `14 59 37` | 14 | 37 (A1) | "[X] [pred-37]" |
| 912 | `83 59 37` | 83 | 37 (A1) | "[X] [pred-37]" |
| 1178 | `48 59 37` | 48 | 37 (A1) | "[X] [pred-37]" |
| 1186 | `06 59 42` | 06 | 42 (A1) | "[X] [pred-42]" |
| 1210 | `64 59 32` | 64=qui | 32 (A1) | "qui [X] [pred-32]" |
| 1443 | `68 59 37` | 68 | 37 (A1) | "[X] [pred-37]" |
| 1796 | `94 59 37` | 94=ne | 37 (A1) | "ne [X] [pred-37]" |

59's other windows (non-A1, for distributional context): @103 `94 93 59 45 28`; @216 `78 06 59 46 29`; @554 `00 86 59 34 17`; @559 `86 94 59 30 67`; @763 `62 94 59 39 88`; @825 `24 87 59 38 82` ("[24] ce [59] [38]" — ce-frame, copula-shaped); @834 `77 76 59 35 56`; @1190 `06 84 59 46 07` ("on [59] que"); @1291 `17 84 59 35 94` ("on [59]"); @1448 `77 84 59 36 67` ("on [59]"); @1496 `66 15 59 24 89`; @1511 `12 61 59 39 81`; @1715 `94 44 59 30 64`; @1777 `87 64 59 19 48` ("ce qui [59] [19]" — third qui-frame); @1804 `77 84 59 35 94` ("on [59]"); @1833 `82 16 59 36 69`.

### 5. Distributional comparison: 26-legs vs 59-A1

**Shared frame shapes** (evidence for homophony candidacy):
- "qui [X] [pred-32]": 26 L3 (@531) || 59 ×2 (@316, @1210).
- "qui [X] [pred-37]": 26 L8 (@1769) || 59 A1 ×5 (@528, @624, @912, @1178, @1443) — same predicate cell, non-qui predecessors.
- "on [X]": 26 L1 (@155) || 59 ×4 (@1190, @1291, @1448, @1804; non-A1 windows).
- "ne [X]": 26 L5 (@842) || 59 @1796 (ne [59] [37], A1).

**Non-shared shapes** (evidence against; per the 47/87 precedent, segregated frames favor split/allophone readings):
- "[N] [X] pour": 26 ×3 (L2/L6/L7, all with 69-predecessor) || 59: 0 windows.
- "[X] par [Y]": 26 ×1 (L4) || 59: 0 windows.
- "la [X] [pred]": 26: 0 || 59 ×2 (@463, @825 including the ce-frame).
- 59-only A1 predecessors: {61, 11, 44, 14, 83, 48, 06, 68} — disjoint from 26's leg predecessors except {64, 94}.
- 59's A1 successor set is narrow {32×3, 37×6, 42×2} — all A1 cells. 26's leg successors {35, 00×3, 32, 96, 12, 37} overlap only on {32, 37}.

**Predecessor segregation note:** 26's verb legs are predecessor-concentrated (69×3, 64×2), while 59's A1 windows have 10 distinct predecessors across 11 windows. Neither the uniformity nor the cycling test rejects; the frame-overlap is partial (4 of 8 leg shapes shared, 2 of 26's leg shapes wholly absent from 59, and 59's la/ce-frames absent from 26).

### 6. Standing-context caveats (evidence only, no re-litigation)

- 59=est is provisional (§7); 67 et/veut is the sole true polyvalence — naming 26="est" needs a red-team polyvalence grant.
- 26's uniform verb-stem reading was KILLED today (battery-stem-26-nent-verb); the locus-level verb reading at @1707 survives only as a conditioned-split question for the red team. None of the 8 legs is @1707.
- The 23~26 split holds (§7) — 23's 3 legs are tabulated separately (sibling target `val-23-copula-gather`).

## Verdict: NULL (gather-only package delivered)

C1 (tabulate) PASS / C2 (no naming) PASS. No adjudication; no standing or red-team verdict contradicted, downgraded, or re-litigated; §7 intact. Per the gather-only precedent, no follow-ups proposed.

## Scope

- Frequency-uniformity + frame-distribution evidence only for the 26-vs-59 homophony candidacy.
- Untouched: 59's provisional value, 26's class/value, 23's legs, the §7 split/polyvalence venue, all standing/red-team verdicts. Canonical-stream caveat stands (row offsets unvalidated).

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-val-26-copula-gather.md`
- Queue: `val-26-copula-gather` queued → `verdict`/`null`, 2026-10-09 (pre-write assert passed — was queued/verdictless; target-id-unique tmp `battery-queue.json.val-26-copula-gather.tmp` + rename; disk re-validated; own entry only; no downgrade; no tmp leftover).
- Lock `locks/val-26-copula-gather.lock`: created on start (2026-10-09T20:39:18Z, no stale lock), deleted on completion (verified gone). R5005, sealed gates, red-team adjudication queue untouched.
