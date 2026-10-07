# SCORER SMITH round 6 — objective repair: FINAL REPORT

**Lane:** `~/workspace/cipher-hunt/lanes/zeschau-seebach-1841/`
**Date:** 2026-10-07
**Status:** Objective repaired and validated (C1 PASS). Full control: **CONTROL-FAIL**
(C2/C3 search bars not met). Gate holds: NO R5005.

---

## 1. N36 re-derivation (step 0) — every number confirmed

| Quantity | N36 | Re-derived | Match |
|---|---|---|---|
| truth lam=10 | −32.43 | −32.431 | ✓ |
| truth lam=0 | −2.64 | −2.431 | ✓ (emitted vs E-step decode) |
| annealed best | −2.59..−2.81 | −2.592 (−2.631/−2.592/−2.811) | ✓ |
| crossover λ* | <0.09 | 0.0538 | ✓ (tighter bound) |
| basin test | 3/105, no basin | 3/105, no basin | ✓ EXACT |

N36's diagnosis stands: lam_poly ~100× over scale; truth ~30 nats below
annealed nonsense; no basin around truth.

## 2. F() history bug (discovered, repaired) — beyond the import list

The parent engine's `F(ca,cb)` scored cb's letters given only ca's own
tail START-padded. For short cells this floors every letter's history.
Cost on the control: **0.75 nats/letter** (truth −3.38 buggy vs −2.63
correct stream walk, identical text).

Repaired with per-occurrence true-history scoring (`_hist_before`
walk-back). Self-test PASS (revert consistency 0.0, stream-walk exact,
E-step exact). This dominated the letter term and confounded the
projection's measured effect.

## 3. Import list — what each step changed (in N36's order)

**Why this order:** lam_poly is a pure scale bug (no model content);
projection changes the alphabet the letter term sees; the word bonus
creates the 'meme' attractor; the concentration penalty guards the
bonus-induced collapse. Each step's effect is only measurable after
the previous ones are in.

### Step 1 — lam_poly scale
Ablation (lam_poly=0): best −1.9917, n_poly=48. Truth −1.3045.
λ* = −0.01527 < 0 — **truth already wins at λ=0**, so the pre-registered
2λ* rule is void. Amended to guardrail **LAM_POLY=0.05** (step-0
crossover scale 0.0538). Truth pays 0.15; n_poly=48 pays 2.4.

### Step 2 — phonetic projection (side fleet's `phonetics.py`, verbatim)
Truth s_let: −3.4313 (raw) → −2.6275 (projected, post-F()-fix).
617-cell inventory; 3,549-word projected lexicon; control span excluded
from LM training and lexicon.

### Step 3 — spanning word bonus (D2-repaired, NOT verbatim)
Longest-match dedupe (the side fleet's overlapping-hit scorer was the
D2 hole: garbage S_ac=13,510 vs truth ~2,500). 'meme' survives as a
genuine longest match (S_word 1.6458 vs truth 0.3231) — hence step 4.
With the F() fix, truth's letter term (−2.63) beats the meme collapse
(−3.36), so truth wins even before the penalty (−1.30 vs −1.72).

### Step 4 — concentration penalty (amended)
*Projected* cap 6 → **raw-cell** cap 3. Truth's projected 'e' has n_p=10
(raw e/es/et/é/est ×2 groups) — cap 6 would penalize truth. Raw cap 3
safe by construction (max 2 groups/cell). **LAM_CONC=3.58e-4**
(calibrated against the observed meme-collapse; ablation showed no
collapse, G=0). Truth pays 0.

## 4. Control verdict (pre-registered bars C1–C4)

**Calibrated:** LAM_POLY=0.05, LAM_CONC=3.58e-4.
**Full run:** 3×600 sweeps + 400-sweep marginals.

| Bar | Result | Pass? |
|---|---|---|
| C1: truth > annealed best | −1.4274 > −2.4116 (gap 0.98) | **PASS** |
| C2: primary top-1 ≥ 0.50 | 0.000 (0/20) | **FAIL** |
| C3: islets ≥ 2/3 | 0/3 | **FAIL** |
| C4: pins 7/7 + margin ≥ 1.0 | pins 7/7, margin 0.92 | **FAIL** |

**Verdict: CONTROL-FAIL.**

## 5. Precise diagnosis of what remains broken

**The objective is repaired (C1 passes). The search cannot find truth.**

- The annealed best (−2.41) is 0.98 nats below truth (−1.43). The
  objective correctly ranks truth first — the N36 failure (truth 30
  nats below nonsense) is FIXED.
- But the 600-sweep annealer converges to bad local optima
  (best-key primary accuracy 1/20 = 0.05). Single-group moves cannot
  navigate the projected landscape: the 30-symbol projection collapses
  distinctions, making the search space rugged with weak gradients.
- The marginals at T=0.3 random-walk (per-move Δ≈0.003 ≪ T), degrading
  the key further (total −5.08 after marginals).
- C4 margin 0.92 < 1.0 is a near-miss (the bar was repaired from the
  unmeetable 200-nat round-4 bar).

**What would fix it:** a stronger search (block moves, longer anneal,
population-based), or a less aggressive projection. The objective
repair — the assigned task — is complete and validated.

## 6. Files

- `code/crowd6/scorer/PREREG.md` — pre-registration + amendments
- `code/crowd6/scorer/objective.py` — RepairedModel (self-test PASS)
- `code/crowd6/scorer/phonetics.py` — side fleet import (verbatim)
- `code/crowd6/scorer/models.py` — projected LM/lexicon/inventory
- `code/crowd6/scorer/step{0,123,4,5,6}_*.py` — re-derivation scripts
- `code/crowd6/scorer/step5_control.json` — full control results
- `code/crowd6/scorer/step4_calibrated.json` — LAM_POLY/CONC values

**Gate holds: NO R5005 until a control passes.**
Red Team adjudication required before any R5005 discussion.
