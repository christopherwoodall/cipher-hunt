# PREREGISTRATION — repaired joint objective, synthetic control re-run

**Lane:** zeschau-seebach-1841 · **Executor:** SCORER SMITH (round 6)
**Written:** 2026-10-07, BEFORE any repaired-objective number is computed.
**Control:** `code/crowd4/control_ground_truth.json` (sealed synthetic;
seed_gen=4107, Tocqueville t1 words [40000,41100), 96 groups, 7 pins,
3 polyvalent islets with unconditioned coins, phase-cycled encryption,
oracle phases). The control is NOT modified. The control's truth cells are
rule-syllabifier products: per §4 of scorer_identifiability.md, the control
validates MACHINERY, not the unit set — the inventory stays
`build_inventory` (top-600 rule units + letters), NOT the 24 crib-derived
units (those are for the gated R5005 rebuild only).

## Objective under test (frozen form)

S(K) = S_let_proj + LAM_WORD·S_word + LAM_ROT·S_phase + S_prior
       − LAM_POLY·n_poly + S_conc

- **S_let_proj**: era letter 7-gram log-probs over the PHONETICALLY PROJECTED
  decode (π from `code/side-homophonic/solver/phonetics.py`, imported
  verbatim with provenance — 42-case self-test passes), per-letter
  normalized. Letter 7-gram rebuilt on projected Tocqueville t1+t2 with the
  control span [40000,41100) EXCLUDED (control independence, same exclusion
  as the raw-letter build).
- **S_word**: spanning-only word bonus with LONGEST-MATCH dedupe (the D2
  repair — the side fleet's frozen S_word counts overlapping hits and is
  EXPLOITABLE: garbage S_ac=13,510 vs truth ~2,500; importing it verbatim
  would import the bug). Aho-Corasick over the projected lexicon (projected
  length ≥ 4, top 40,000 by freq, weight log(1+freq), built from the
  span-excluded corpus), greedy longest-match left-to-right, non-overlapping,
  only matches SPANNING ≥1 value boundary count. Per-letter normalized.
- **S_phase**: rotation-aware transition prior, per-position normalized.
- **S_prior**: BETA_PROV=0.2 per matched soft hint (5 correct hints, control
  design — same as round 5).
- **−LAM_POLY·n_poly**: polyvalence sparsity penalty (scale repaired, step 1).
- **S_conc**: −LAM_CONC·Σ_p max(0, n_p−6)², n_p = #groups whose PROJECTED v1
  is p (projection-collapsed, so accent variants collude — the side fleet's
  design). Cap 6: safe for the control truth (max quota 2: drivers/anchors/
  islet-primaries all have exactly 2 groups) and for the petit-chiffre
  family (max quota 3–5 by largest remainder).

## Frozen hyperparameters (no truth labels used)

- N_GRAM=7, ALPHA_NG=0.1, LAM_WORD=1.0 (imported value), LAM_ROT=0.0
  (phase term HELD OUT — same as round 5's baseline; the banked phase map is
  fragile post-repair and the control's oracle phases would flatter it;
  item 6 of the import list is out of scope for this round),
  BETA_PROV=0.2, CONC_CAP=6, inventory=top-600 rule units + letters (617),
  pins=7 pencil cribs, prov=5 control hints.
- Anneal: 3 restarts × 600 sweeps, T0=2.0 → T1=0.02 (round-5 baseline
  budget, for comparability). Marginals: 150 sweeps @ T=0.3 (round-5 idiom).

## Calibrated hyperparameters (rules frozen here; numbers filled after)

- **LAM_POLY (step 1):** ablation anneal with LAM_POLY=0, LAM_CONC=0 →
  best key K_abl (components C_abl, n_poly n_abl). Score truth key →
  C_truth, n_truth=3. Crossover λ* = (C_abl − C_truth)/(n_abl − 3)
  (the λ where truth ties K_abl; truth has fewer polyvalent groups, so
  truth wins iff λ > λ*). **Set LAM_POLY = 2·λ*** (2× margin above
  crossover). Rationale: a scale bug is fixed with a ruler, not a wish —
  the control is the ruler. The islet bar (C3) adjudicates whether 2×
  margin over-admits or over-penalizes.
- **LAM_CONC (step 4):** from the same ablation's K_abl (which exhibits the
  collapse): build K_decon by reassigning each over-cap group to a random
  other inventory cell (seed 7, one draw). G = (S_word(K_abl) −
  S_word(K_decon)) / Σ_p max(0, n_p−6)² (the word-bonus profit rate of the
  observed collapse; no truth labels). **Set LAM_CONC = 2·G** (2× margin —
  the penalty must dominate the word-driven part of the collapse
  incentive; the letter term already disfavors collapse on its own).

## Pass bars (frozen; same idiom as round 4/5)

- C1 (model ranking): s(truth_key) > s(best_annealed_key) on the repaired
  objective. [The diagnosed N36 failure was the reverse: truth ~30 nats
  below annealed nonsense.]
- C2 (search): marginal-argmax primary top-1 ≥ 0.50 on the 20 most frequent
  non-pin groups with truth primary in inventory. [Round-5 bar; max
  achievable is 0.90 — 2/20 bar groups are unidentifiable by construction
  (lossy tail inheritance).]
- C3 (islets): ≥ 2/3 islets with both true values in top-3 marginal AND
  true dominant ranked #1. [Adjudicates the LAM_POLY 2× margin.]
- C4 (sanity): 7/7 pins intact; annealed best beats best-of-20 random keys
  by ≥ 1.0 on the repaired normalized total. [The round-4 "≥200 nats" bar
  is UNMEETABLE-BY-CONSTRUCTION on the per-letter-normalized scale — a
  bar-scale bug of the same family as lam_poly; repaired to 1.0, which is
  decisive on a ≈−3-scale total. Documented here, not silently lowered.]
- **CONTROL-PASS iff C1∧C2∧C3∧C4. Else BROKEN-ON-CONTROL with diagnosis.**
  No R5005 run on failure. Gate holds either way until Red Team adjudicates.

## Conditional follow-up (pre-registered)

- Basin test re-derivation on the repaired objective (perturb truth by
  k∈{5,10,20} groups, 3 low-T descents each, no re-init; recovery =
  perturbed groups returning to truth primary): runs ONLY if C1 holds
  (if truth is not the optimum, no basin is expected — running it would
  be theater).

## Step attribution (what each import-list step must show)

1. lam_poly scale fix: re-derive N36's crossover on the CURRENT objective
   (truth −32.43 vs annealed −2.91; crossover λ*<0.09) BEFORE changing
   anything — every number re-derived.
2. Phonetic projection: Δs_let for truth key (expect ≈ +0.33/letter, the
   measured ear-noise cost) vs Δs_let for the annealed nonsense key.
3. Spanning word bonus: per-letter S_word on truth decode vs on annealed
   decode (longest-match deduped, spanning-only).
4. Concentration penalty: max projected n_p and Σmax(0,n_p−6)² with
   LAM_CONC=0 vs with calibrated LAM_CONC; truth's max quota unaffected.

## Why this order (for the report_inbox note)

1. **lam_poly first** — it is a pure scale bug, zero model-content change.
   Every number measured under lam_poly=10 is apples-to-oranges
   (N30 compared truth-with-penalty-off vs annealed-with-penalty-on);
   no later import can be evaluated until the ruler is fixed.
2. **Phonetic projection second** — it repairs the LETTER term, the
   objective's load-bearing likelihood. Round-5 route (b) proved the
   letter-model miscalibration (−3.11 nonsense beats −3.64 truth/letter)
   is independent of search and space size; the projection absorbs the
   ~0.33 nats/letter of ear noise that the raw 7-gram charges truth.
   It must precede the word bonus because the bonus scores projected text.
3. **Spanning word bonus third** — it adds the long-range coherence the
   7-gram cannot see (~7 chars), the side fleet's "salad beats truth"
   pilot and our annealer's "fluent nonsense" are the same failure
   family. It comes after the projection (it scans projected text) and
   with the D2 repair (longest-match dedupe), because the side fleet's
   frozen S_word is itself control-broken (primary 0.0000, secondary
   ≈chance) — importing it verbatim would import the exploit.
4. **Concentration penalty last** — it is a guardrail, not a signal term.
   The collapse it prevents is WORD-BONUS-driven (50+ groups → 'me'
   earning 'meme' spanning hits at every position); there is nothing to
   guard until the bonus exists. Calibrated on the observed collapse
   (no truth labels), after the bonus is in.
(Items 5–7 of homophonic_synergy.md — pool/block proposals, chi2-gated
phase, F34 inventory rebuild — are explicitly out of scope: proposals are
search, not objective; the phase map is fragile post-repair; the inventory
rebuild is for the gated R5005 run, and the control validates machinery,
not the unit set.)
