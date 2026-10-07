# SOLVER REBUILD Round-2 Fleet — Charter (2026-10-07)

Deployed by coordinator (parent: main agent) to attack the binding diagnosis from
rebuild round 1: **Goodhart on the language model** — the Tocqueville char-5-gram
assigns better per-char rates to adversarial morpheme-salad (+1,540 nats) than to
register-gapped, ear-noised Les Mis truth, and the lexicon rewards morpheme tiling
(+1,370). Wrong key beats truth by 2,601 nats at chance primary recovery (1/89).
The independent verifier proved scorer reweighting within the 5-gram+lexicon family
is EXHAUSTED — the failure is in the likelihood, not the weights. Optimizer and
objective both exonerated. See `code/side-homophonic-rebuild/verifier/CLOSING-VERIFICATION.md`.

## Tracks (all in `code/side-homophonic-rebuild2/`)

| Track | Question | Method | Pre-registered bar |
|---|---|---|---|
| A (`track-a/`) | Is the register gap the blocker? | Rescore truth vs frozen salad under a register-matched (diplomatic-corpus) reference vs Tocqueville reference; short pilot anneal on 2 register-matched instances ONLY if diagnostic positive | H0 iff truth beats salad by ≥+500 nats under register-matched ref while salad wins under Tocqueville; H1 iff salad still wins by ≥+500 under register-matched |
| B (`track-b/`) | Does a neural char-LM fix the likelihood? | Train small char-level neural LM (<2h CPU) on diplomatic corpus + Tocqueville + RdM (NO Les Mis); rescore truth vs frozen salad vs adapted salad | SUCCESS iff truth beats frozen salad by ≥+1,000 nats AND beats adapted salad by ≥+300 nats |
| C (`track-c/`) | Does word-boundary structure separate truth from salad? | Boundary-aware rescore (lexicon-DP segmentation + word unigram rates + boundary prior); joint boundary-inferring pilot on 300-cell slice ONLY if promising | PROMISING iff truth beats salad by ≥+800 nats under boundary-aware score |

## Red team (`redteam/`)
- Holds KILL AUTHORITY over every track claim.
- Reviews each track's `PREREG.md` BEFORE it runs scored comparisons (falsifiability, leakage, precision).
- Re-derives headline numbers with independent code (≤0.1 nat standard).
- Enforces: NO R5005 contact (instant kill), control/diagnostic only, deterministic seeds.
- Maintains numbered `RULINGS.md` with file+line citations.

## Hard constraints (all tracks)
- Work ONLY in `code/side-homophonic-rebuild2/`. Frozen dir untouched.
- R5005 is NEVER touched — all tracks are control/diagnostic only.
- The 6-instance gate (`code/side-homophonic/control/CONTROL-DESIGN.md`, fresh seeds)
  must pass before ANY R5005 run.
- Ready infrastructure: fresh 6-instance batch 184201–184204, 184206, 184207
  (`code/side-homophonic-rebuild/solver_inbox/`, keys sealed); q_cycle=0 ablation set
  (184213–184218) with pre-registered rhythm-crutch criterion.

## Success criterion
A method that passes the 6-instance gate (then a gated R5005 run), or a third
honest FAIL with an even sharper diagnosis.
