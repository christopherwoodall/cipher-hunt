# Step-4 clearance request — Track D gate funnel on the accepted v3C instrument
Date: 2026-10-08 ~01:56 UTC. From: Smith rebuild coordinator (session 5ca520bb).
To: solver-side red team.

## Request
Clearance to execute the Track D step-4 gate funnel (Branch B) using the
accepted v3C pairwise judge instrument (prompt-v3C.txt,
sha256 d907c59202c9d38e5dfe10bf8048c869bcba2fb547631c02ceb34f93b5b2615e).

## Basis
1. Rung-C clean re-run: PASS (36/36, unanimous), red-team audit ADMISSIBLE
   (rerun-rungC-clean/VERDICT.md, REDTEAM-AUDIT.md, COORDINATOR-ATTESTATION.md).
2. Strike one cleared per ladder §4; instrument accepted.
3. Funnel machinery ready: cell-space moves implemented + smoke-tested
   (track-d/solver-cell/), 200-seed package built with current priors
   (track-d/funnel/), Experiment 0 closed 6/6 SLIDE (Branch B binding).
4. Track B neural LM training continues independently (held loss still declining).

## Scope of the cleared run (if granted)
- Branch-B funnel per PREREG-D-v2-branchB.md: 200 seeds (funnel package) →
  5k-iter climbs → judge triage → judge-guided ILS with cell-space mutations →
  winner, on the 6 ORIGINAL control instances only.
- Judge calls via the accepted v3C instrument (pairwise, frozen prompt,
  blind labels, full logging, same hardening as the re-run).
- R5005 stays sealed. Gate instances 184201–184204/184206–184207 stay sealed
  until the SEPARATE gate-clearance (which additionally requires the
  memorization re-probe once the key-holder constructs the blind package).

## Explicitly not requested
- No R5005 contact. No gate-instance unsealing. No prompt modification.
