# Rung-C clean re-run — coordinator designation & hardening confirmation
Date: 2026-10-07. Author: Smith rebuild coordinator (session 5ca520bb-e126-4363-aaa3-30ccdb09096f),
subagent of main agent a16ea805-606d-4e53-9014-fb21959136f5.

## (i) Single-coordinator designation (R18 condition i)
The parent's tasking order designates THIS coordinator as the SINGLE Track D
coordinator for the rung-C clean re-run. No other coordinator, harness, or
parallel trial is authorized on track-d/ for the duration. The prior
dual-coordinator collision (INCIDENT-COLLISION-20261007.md) is the reason;
this re-run exists to replace the voided evidence with admissible evidence.

## (ii) Isolated trial directory (R18 condition ii)
`code/side-homophonic-rebuild2/track-d/rerun-rungC-clean/`
All trial artifacts are write-once, create-new, under this path only.
No shared log paths with any other writer. The voided
`instrument-acceptance-v3c/` artifacts are quarantined, not deleted, not read.

## (iii) Hardening rules 1–8 confirmed (R18 condition iii)
1. Checksum + back up every judge log immediately on receipt, before any scoring.
2. Mechanical handoff↔disk cross-check before scoring — ANY mismatch HALTS scoring pending investigation.
3. Score ONLY from checksummed disk copies. Never from handoff text.
4. Single coordinator (this document). Dual commissions barred.
5. Isolated per-trial directory (above). Write-once artifacts.
6. DISK-FIRST. Handoffs are transport, never evidence.
7. Only the red-team audit counts. No self-certified audits; the trial runner
   produces a mechanical aggregation, and a SEPARATE red-team agent audits
   campaign integrity before any verdict is declared.
8. Collision artifacts quarantined, not deleted (already done — ratified).

## Carry-forward (R19)
Diagnostic bouts pair truth_i × paraphrase_i BY SEED (the voided run's
cross-seed pairing deviated from spec — not repeated).

## Protocol
Ladder §2 verbatim: prompt-v3C.txt pinned at
sha256 d907c59202c9d38e5dfe10bf8048c869bcba2fb547631c02ceb34f93b5b2615e;
36 binding truth-vs-salad pairs × 3 position-randomized passes (108 calls);
6 diagnostic truth-vs-paraphrase bouts by seed × 3 passes (18 calls);
3 fresh judges, 12+2 pairs each; fresh 8-hex blind labels, zero old-label hits;
full logging (label, pass, prompt sha256, raw response, extracted choice);
R5005 grep tripwire before and after; gate instances 184201–184204, 184206–184207 sealed.
PASS iff truth wins per-pair majority on ≥35/36 binding pairs.
