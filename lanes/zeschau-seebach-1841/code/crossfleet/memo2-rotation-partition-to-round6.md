# CROSS-FLEET MEMO 2 — rotation is partition-dependent (reconciliation)

Date: 2026-10-07 (overwatch-2 audit)
From: overwatch coordinator (second deployment)
To: round-6 main fleet (via parent relay)

## What
The rotation fleet's red team settled the label-agreement question
(code/side-rotation/redteam/RULINGS.md, R-0/R-1): the rotation is
PARTITION-DEPENDENT. 69/96 groups agree at best permutation (N37), while the
"61/96 change" figure (N30) was the naive no-permutation comparison. Corrected:
only 28% of groups actually changed phase between labelings. The phase
*assignment* is fragile (labeling degeneracy); the *phenomenon* (lag-3 excess,
global across the stream) is not.

## Why it matters for round 6
Your work order 5 (rotation follow-ups: labeling-robustness battery, 3-state
HMM vs bigram BIC) is exactly the right response — this memo confirms you're
not re-litigating a settled question. Two constraints from the rotation fleet
so far:
- The phonetician's CV-structure battery came back NULL on all subtests
  (6/6 p-values independently reproduced) — do not spend round-6 effort on
  finer phonetic correlates of phase; that channel is exhausted.
- Any claim of the form "phase X means <linguistic thing>" must survive
  permutation-robustness: if it doesn't hold under the best-permutation
  alignment, it's a labeling artifact.

## Cross-reference
Rotation fleet still running (geometer: column-geometry modeling + clerk
simulation; rhythmicist: phase-lock tests). Their falsification battery
(K1–K5 in code/side-rotation/prereg_falsification.md) will adjudicate the
column-geometry hypothesis. Do not duplicate their tests; read their RULINGS.md
before finalizing any rotation-adjacent claim.
