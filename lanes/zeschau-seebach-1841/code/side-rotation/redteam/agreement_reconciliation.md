# Label-agreement reconciliation: N37 (69/96) vs N30 (61/96 change)
2026-10-07, red team, rotation fleet. Re-derived independently from the two
banked label maps — no new clustering run.

## The two maps
- OLD: contactor's k=12 Jaccard clusters on the 1,846-pair parse
  (`code/crowd/contactor_results.json`, key `jaccard_clusters.12`): 12 clusters,
  sizes [30,26,23,4,3,2,2,2,1,1,1,1] (sum 96). Contactor's phase convention
  (`code/crowd/contactor.py`): 3 largest → A/B/C by size (A=30: 11=la,34=i,46=que,
  70=pre; B=26: 40=e,82=m,87=ce; C=23: 29=er), remainder → R (17 groups).
- NEW: `code/crowd4/phase_map_repaired.json` (Jaccard-k12 on the repaired
  1,847-pair parse; T0-verified exact): A=32, B=27, C=17, R=20.

## The numbers (independent re-derivation)
- Best-permutation agreement (6 ABC permutations, R fixed — the standard for
  comparing clusterings, since cluster labels are arbitrary up to permutation):
  **69/96 agree, 27 change.** Winning permutation old→new: {A→B, B→A, C→C, R→R}.
  This is N37's figure. ✓
- Naive identity agreement (no permutation): **35/96 agree, 61 change.**
  This is N30's "61/96 change" figure. ✓

## Why both appear
The contactor's old A/B/C letters sit in a different permutation than the
repaired map's letters — the cycle itself reversed (old A→C→B→A, repaired
A→B→C→A; F43 notes the relabeling). Comparing labels by identity therefore
counts the permutation flip as "change." N30's 61/96 is the identity figure
(arithmetically correct, methodologically misleading as a fragility headline);
N37's 69/96 is the best-permutation figure (the correct clustering-agreement
number). No different recompute is involved — both figures derive from the same
two banked maps.

## Corrected figure to bank
**69/96 agree at best permutation → 27/96 = 28% membership change.**
The "61/96 change" headline (run_r5005.py:68 comment; N30-derived prose in
NOTES.md, rotation_mystery.md, unit_inventory, homophonic_synergy.md,
scorer_identifiability.md, crowd5/redteam/rulings.md) should be corrected to the
best-permutation figure. Cluster fragility is real (28% is far above the ~0%
a stable clustering would show) but the naive figure overstated it by 2.3×.
