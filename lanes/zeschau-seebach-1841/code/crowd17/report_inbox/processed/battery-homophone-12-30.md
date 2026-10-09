# Battery verdict: homophone-12-30

## Target
- **id:** homophone-12-30
- **CLAIM:** 12~30 homophony (12/30 merge as homophones)
- **BARS (verbatim):** "merge iff successor/predecessor distributions indistinguishable (per {33,86} precedent, reversed)"
- **ADVERSES:** None
- **PRIORITY:** 4

## Numbered clauses (pre-registered BEFORE testing, not modified after)
1. **C1:** 12 and 30 meet the {33,86} indistinguishability standard on successors (permutation test, fail to reject at the lane's alpha).
2. **C2:** 12 and 30 meet the {33,86} indistinguishability standard on predecessors.

## Method
Read BATTERY-PROTOCOL.md first. Lock `locks/homophone-12-30.lock` created on start (agent id + 2026-10-09T04:28:00Z UTC). Fresh parse of the repaired stream per `repair_parse.py`: 1,847 pairs, 96 distinct groups, verified. `canonical.py` never touched. R5005, sealed gates, and the red-team adjudication queue untouched. Monte Carlo permutation test (5,000 permutations, chi-square homogeneity statistic, seed 1230) on predecessor and successor context distributions of 12 (n=23) and 30 (n=19).

The {33,86} indistinguishability standard (per battery-thirds-60-68-pair): fail to reject (p > 0.05) on BOTH successors and predecessors. Lane rejection yardsticks: 09/92 hold at p=0.256; 23~26 split at p=0.0029.

## Results
- **C1: FAIL at kill grade.** Successor distributions: chi2=36.62, permutation p=0.0002 — rejects. 12's successors are dominated by 48 (x5), 94 (x3), 16 (x3); 30's by 06 (x4), 03 (x3), 67 (x2). Only ONE successor key is shared (06) out of 22 distinct successor types.
- **C2: FAIL at kill grade.** Predecessor distributions: chi2=29.22, permutation p=0.0124 — rejects. Only three predecessor keys are shared (26, 56, 20) out of 21 distinct predecessor types.

Both p-values sit at or below the 23~26 split yardstick (p=0.0029), far from the 09/92 hold yardstick (p=0.256). The distributions are distinguishable at kill grade.

## Standing-verdict layer (independent of the distributional test)
A 12~30 merge would also contradict two standing red-team adjudications: 12='n' (letter-tier grant, round-17 adjudication) and 30='pas' (conditional promote, R17-011). Homophony requires the same plaintext; 'n' and 'pas' are incompatible. No standing verdict is overwritten (nothing is renamed); the claim is simply false.

Note: n(12)=23 vs n(30)=19 satisfies the frequency-uniformity necessary condition, but uniformity is insufficient for homophony (protocol §7) — and the distributional test rejects regardless.

## Verdict: KILL
Both bar clauses fail at kill grade: the predecessor/successor distributions of 12 and 30 are distinguishable (p=0.0124 / p=0.0002), rejecting the merge under the {33,86} standard. The claim independently contradicts standing adjudications on 12 and 30. No polyvalence declared (§7 intact). No follow-ups required (kill verdict, not null).

## Bookkeeping
- Report: `code/crowd17/report_inbox/battery-homophone-12-30.md`
- Queue: `homophone-12-30` → status `verdict`, result `kill`, date 2026-10-09 (temp-file + rename, pre-write assert confirmed queued/verdictless, JSON re-validated)
- Lock created on start, deleted on completion
