# REPORT — scorer objective repair (round 6, N36 ordered import list)

**Executor:** SCORER SMITH · **Date:** 2026-10-07 · **Status:** [IN PROGRESS]
**Code:** `code/crowd6/scorer/` · **Preregistration:** `code/crowd6/scorer/PREREG.md`
(frozen before any repaired-objective number was computed)

## Context

N36 refuted N30's "model-correct": the joint engine's polyvalence penalty was
~100× over scale (configured 10; truth beats the annealed best only below a
crossover λ*), truth sat ~30 nats below the annealed fluent nonsense on the
actual search objective, and the basin test was decisive — all 9 low-T
descents walked AWAY from truth (3/105 recovered). The ordered repair
(`code/crowd5/scorer_identifiability.md` §5, `homophonic_synergy.md`):

1. fix lam_poly scale · 2. import the side fleet's phonetic projection ·
3. spanning word bonus · 4. concentration penalty — in that order.

## Why this order (the import list is a dependency chain, not a preference)

**1. lam_poly first — it is a pure scale bug, zero model-content change.**
N30's "truth −2.65 beats annealed −3.05" was apples-to-oranges:
truth-with-penalty-off vs annealed-with-penalty-on. On the actual search
objective (lam_poly=10) truth (−32.43) sits ~30 nats BELOW the annealed
nonsense (−2.91). The penalty is 10 nats key-level against a per-letter-
normalized letter term — adding a v2 would need ~58,000 nats of letter
improvement to pay for itself, so the annealer ends at n_poly=0 and the
islet bar (≥2/3) is unmeetable BY CONSTRUCTION. No later import can be
evaluated until the ruler is fixed: every number measured under lam_poly=10
is contaminated. Re-derived here (step 0): [numbers below].

**2. Phonetic projection second — it repairs the load-bearing likelihood.**
Round-5 route (b) proved the letter-model miscalibration (−3.11 nonsense
beats −3.64 truth/letter) is independent of search and space size: the raw
7-gram charges truth ~0.33 nats/letter for by-ear spelling noise the
encipherer treats as identical (prend→pre, personne cut two ways, mute -e
written). The side fleet's `phonetics.py` (30 classes, evidence-graded,
42-case self-test) absorbs exactly this. It must precede the word bonus
because the bonus scans projected text — and because the letter term is the
term everything else is calibrated against, it comes before any new term
is added. Imported verbatim with provenance (their file stays canonical);
measured effect on truth vs nonsense: [numbers below].

**3. Spanning word bonus third — the long-range term the 7-gram cannot see.**
The side fleet's "salad beats truth" pilot (−3.89/pair vs −4.44/pair) and
our annealer's "fluent nonsense" are the same failure family: the n-gram
ranks non-truth above truth. The bonus rewards words assembled from 2+
values (spanning-only — a word inside one value is not decipherment
evidence). It comes after the projection (it scans projected text) and —
critically — with the D2 repair, NOT verbatim: the side fleet's frozen
S_word counts overlapping hits and is itself control-broken on the
diagnosed instance (primary 0.0000, secondary ≈ chance; garbage S_ac=13,510
vs truth ~2,500; their positive control is failing as of this writing).
Importing it verbatim would import the exploit. The repair: greedy
longest-match dedupe (non-overlapping) + spanning-only + per-letter
normalization. Measured: [numbers below].

**4. Concentration penalty last — it is a guardrail, not a signal term.**
The collapse it prevents is word-bonus-driven: 50+ groups → 'me' earns
'meme' (wt 6.98, the #1 lexicon word) spanning hits at every position.
There is nothing to guard until the bonus exists — ordering it earlier
would be tuning a guardrail against a threat that isn't in the objective
yet. Over PROJECTED values (accent variants collude), cap 6 (safe for the
control truth's max quota 2 and the petit-chiffre family's 3–5).
Calibrated on the observed collapse with no truth labels (pre-registered
rule). Measured: [numbers below].

Out of scope by design (items 5–7): homophone-pool/block proposals are
search, not objective; the chi2-gated phase prior needs the fragile banked
phase map replaced (held lam_rot=0.0, as round 5); the F34 inventory
rebuild is for the gated R5005 run — the control validates machinery,
not the unit set (§4).

## Coordination with the side-homophonic fleet (not duplication)

- Their `phonetics.py` imported verbatim (step 2) — 42/42 self-tests pass.
- Their word bonus NOT imported verbatim: their frozen positive control is
  failing (seed 184101: primary 0.0000, secondary 0.1473 ≈ chance 0.1434;
  planted truth −6,959.9 nats vs annealed best +4,127.4 — the objective's
  optimum is at the wrong place). Diagnosed causes: D2 (overlapping-hit
  word scorer — the hole), D3 (polyvalence runaway, n_poly 49–60 vs truth
  6; their λ_poly=20 nats dwarfed by degenerate S_word gains), D4
  (inventory gap, 6/96 truth primaries absent → ceiling 0.933). The D2
  repair (longest-match dedupe) is implemented here per their own repair
  direction (a); their RUN-REPORT's repair list is the shared reference.
- Their inventory rebuild (crib-derived, 291 cells) and repaired-parse
  adoption (ct_loader.py, canonical 1,847 pairs) noted — the control here
  keeps the control-consistent inventory deliberately (machinery, not
  unit set).
- If their control later passes with a repaired word scorer, the pass
  certifies the phonetics/word-bonus/concentration stack, not the unit
  alphabet (their control plants from encipher_split cells — same
  machinery-not-unit-set tension as ours).

## Step attribution (every number re-derived)

### Step 0 — N36 baseline re-derived on the CURRENT objective (no changes)
- truth (emitted decode): lam=10 → −32.431 (s_let −3.4313, n_poly 3);
  lam=0 → −2.431. [Reproduces N36's −32.43/−2.64 modulo E-step vs emitted
  decode variant.]
- annealed best (3×600, lam=10): −2.592 (runs −2.631/−2.592/−2.811).
  [Reproduces round-5's −2.59..−2.81 band.]
- crossover: λ* = 0.0538 — truth beats the annealed best iff lam_poly <
  0.0538 (N36's <0.09 on their key pair; same scale bug, tighter bound).
- basin test: 3/105 recovered (k=5: 1/15, k=10: 2/30, k=20: 0/60) — all 9
  low-T descents walk AWAY from truth. [Reproduces N36's 3/105 EXACTLY.
  No basin around truth; the landscape slopes away.]
- Verdict on N36: every number re-derived and confirmed. The objective is
  wrong (not the search).

### Step 0.5 — F() history bug (discovered during re-derivation, repaired)
- The parent engine's F(ca,cb) scored cb's letters given only ca's own
  tail START-padded — for short cells every letter got a floored
  START-padded history. Cost truth 0.75 nats/letter on the control
  (−3.38 buggy vs −2.63 correct stream walk, identical text).
- Repaired: per-letter stream scoring with TRUE rolling history
  (`_hist_before` walk-back). Self-test PASS (revert consistency 0.0,
  stream-walk exact, E-step history exact).
- Beyond the 4-item import list, documented as discovered — it
  confounded the projection's measured effect and dominated the letter
  term. With the fix, truth's s_let = −2.6275 (vs meme collapse −3.3647):
  the letter term now correctly penalizes degenerate repetition.

### Step 1 — lam_poly scale fix
[pending — calibrated on the repaired objective per the pre-registered rule]

### Step 2 — phonetic projection
- truth s_let: raw −3.4313 → projected −2.6275 (re-derived AFTER the F()
  history fix; the earlier +0.054 delta was confounded by that bug).
  [Cross-alphabet absolutes are confounded by the 30-symbol alphabet;
  ranking vs nonsense is the measure.]
- With the F() fix, the projected letter term correctly penalizes
  degenerate repetition: meme-collapse s_let_proj −3.3647 << truth
  −2.6275.

### Step 3 — spanning word bonus (D2-repaired)
- truth S_word: 0.3231/letter (longest-match deduped, spanning-only).
- meme-collapse S_word: 1.6458/letter — still beats truth's word term.
  The dedupe halves the degenerate profit vs the frozen overlapping-hit
  style (3.234 → 1.6458, 2.0×) but 'meme' (wt 6.98, lexicon #1) IS the
  longest match at its position — dedupe cannot kill a genuine longest
  match. This is why the concentration penalty (step 4) is in the import
  list and ordered last.
- With the F() fix, truth's letter term now outweighs the meme word
  bonus: truth total −1.3045 > meme-collapse −1.7189 even before step 4.
  The ablation will show whether a subtler annealed exploit still needs
  the penalty — the guardrail stays regardless (the extreme collapse is
  not the only attractor).

### Step 4 — concentration penalty
[pending — calibrated per the pre-registered rule]
- AMENDMENT (pre-run): projected cap 6 → RAW-cell cap 3. Measured on the
  sealed control: truth's projected 'e' has n_p=10 (raw e/es/et/é/est ×2
  groups each all project to 'e') — cap 6 would penalize truth itself.
  Raw cap 3 is safe BY CONSTRUCTION (build_codebook: every non-singleton
  cell has exactly 2 groups; petit-chiffre max quota 3–5). See PREREG.md.

## Control verdict
[pending — pre-registered bars C1–C4 in PREREG.md]

## What remains broken / open
[pending]
