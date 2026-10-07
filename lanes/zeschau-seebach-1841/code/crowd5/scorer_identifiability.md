# SCORER IDENTIFIABILITY — round 5, work order 7 (scorer-smith)

Lane: zeschau-seebach-1841. Engine: `code/crowd4/joint_engine.py` (round-4 joint
SA: letter 7-gram + phase term + polyvalence E-step, 7 pins). Control:
`code/crowd4/control_ground_truth.json` (synthetic Tocqueville cipher, 1,947
pairs, 96 groups, 7 pins, 3 islets, sealed truth). Gate stands: no R5005 run.

## 0. The N30 "model-correct" claim does not survive re-derivation

N30: "model-correct but BROKEN-ON-CONTROL — truth −2.65 beats annealed −3.05."
Recomputed in the current engine on the sealed control:

| key | lam_poly | total | s_let/letter | n_poly |
|---|---|---|---|---|
| truth key + model's own E-step decode | 0 (penalty off) | **−2.64** | −3.6395 | 3 |
| truth key + model's own E-step decode | 10 (as configured) | −32.64 | −3.6395 | 3 |
| truth key + emitted (data-generating) decode | 10 | −32.43 | −3.4313 | 3 |
| annealed best (600 sweeps, round-4 config) | 10 | **−2.91** | −3.1055 | 0 |

- N30's "truth −2.65" reproduces only with lam_poly=0 (penalty disabled); the
  annealed number was scored with lam_poly=10 (where n_poly=0 pays nothing).
  Apples-to-oranges. On the actual search objective, truth (−32.64) sits ~30
  nats BELOW the annealed nonsense (−2.91).
- The polyvalence penalty is on the wrong scale: 10 nats key-level vs a
  per-letter-normalized letter term. Adding v2 needs Δ > lam_poly ×
  total_letters ≈ 58,000 nats of letter improvement to pay for itself —
  impossible. The annealed key ends n_poly=0; the islet bar (≥2/3) is
  unmeetable BY CONSTRUCTION at lam_poly ∈ {10, 20}. Model bug, not search.
- Even with the penalty off, the letter 7-gram alone prefers the annealed key
  (−3.11/letter) over truth (−3.64/letter). The E-step recovers only 42/63
  (0.667) of the truth's islet emissions from the true key.
- The search is optimizing correctly. The objective is wrong. This confirms
  the side-homophonic fleet's independent pilot (degenerate salad −3.89/pair
  beats truth −4.44/pair on their char 5-gram).

## 1. Identifiability analysis (control, pre-registered bar groups)

Bar: marginal-argmax top-1 ≥ 0.50 on the 20 most frequent non-pin groups with
truth primary in inventory.
- 2/20 bar groups are unidentifiable BY CONSTRUCTION (lossy tail inheritance):
  group 41 (n=274, most frequent): truth primary 'ri' emitted 1.8%, modal
  emitted 'mi' 2.2%, 160 distinct emitted cells, entropy 4.9. Group 31 (n=22):
  'pas' 18% vs modal 'pa' 32%. No likelihood method can top-1 these.
- Max achievable top-1 on the bar: **0.90**. The bar (0.50) is reachable in
  principle, but 10% of it is lottery.

## 2. Route (a): better search

(a0) Baseline — current engine, 3 restarts × 600 sweeps: [in flight]
(a1) Parallel tempering — 6 chains × 600 sweeps, swaps every 10 sweeps,
     geometric ladder 2.0→0.02: [in flight]
(a2) Smarter proposals — homophone-pool copy (contact-Jaccard neighbors) +
     Gibbs-conditional cell sampling, 3 restarts × 600 sweeps: [in flight]
(a3) Basin test — perturb truth key by k∈{5,10,20} groups, low-T descent
     (no re-init), measure recovery to truth: [in flight]

Prediction from §0: since the objective ranks truth ~30 nats below the
annealed optimum, no search improvement can "reach truth's basin" — there is
no basin. Route (a) is expected to find *better-scoring* nonsense, not truth.
Its value is bounding the search contribution after the objective is repaired.

## 3. Route (b): shrink the space (F33 operationalized)

F33: polyvalence is CONDITIONED (06: trigram-internal "ent" vs verb-stem;
52: "pas" iff pre∈{94,70} else "so"/"se"; 94: "en" iff pre=82/suc=87);
35.2% token coverage from identified groups.
(b1) Hard-known: 5 correct hints → hard pins (12 pins); 3 islet (v1,v2)
     hard-coded (E-step still per-occurrence); inventory top-300 + known
     cells (312). [in flight]
(b2) Conditioned polyvalence: v2 admitted only where a pre/suc-group
     conditioning rule verifies (χ², p<0.01). The control's islets are
     unconditioned coins → honest expectation is REJECTION — documenting the
     control-vs-F33 gap, not a failure. Implements the word-pattern fleet's
     R4 tightening. [in flight]
(b3) Small inventory alone (7 pins, 312 cells): is the shrink enough without
     hard readings? [in flight]

## 4. Cross-fleet intel folded in (round-5 briefing)

**Anchor-preserving controls (sidepath lesson).** The round-4 control is fully
synthetic — no stream shuffling, so no de-anchoring. Principle ADOPTED for any
future shuffled-null control: anchored positions stay fixed, shuffle only the
rest. (The sidepath pass-1 VOID — 174 vs control 208.3 — is the cautionary
case; not applicable to the current runs.)

**Crib-derived inventory (F34; Inventorist `code/crowd5/unit_inventory.json`,
24 units).** Measured against the engine's 617-cell rule-syllabifier inventory:
- 18/18 concrete crib-derived values present EXCEPT 'veut' (provisional 67):
  the top-600 rule-unit cutoff drops it. Single letters (m/i/e) present via
  the letter backfill — R1 satisfied in the letter case.
- Control/inventory tension (honest negative): the synthetic control's truth
  cells are rule-syllabifier products; only 23/89 (0.258) of its non-pin truth
  primaries are in the 24-unit crib-derived set. An F34-compliant inventory
  would cap control recovery at ~26% — **the control validates machinery, not
  the unit set.** Do not "fix" the control's inventory to the 24 units; do not
  claim control passage certifies the R5005 inventory.
- Prescription for the (gated) R5005 run: rebuild the inventory on the 24
  crib-derived units + the 11,870-word pattern lexicon
  (`code/side-wordpattern/lexicon/`) with the polyvalence-expansion method
  under red-team restrictions R1–R8 (`code/side-wordpattern/redteam/
  ADJUDICATION.md`) — NOT the top-600 rule units, NOT `data/upstream-syll*.py`
  (N29: not the encipherer's table). R6 extended: re-derive on parse/inventory
  change (canonical 1,847-pair parse).

**No nulls (petit-chiffre intel).** The joint engine models no null groups
(every group maps to a cell; no null unit in the inventory) — consistent with
the petit-chiffre table having no nulls and the lane's null-digit negative.
No change needed. The 1690 homophone mandate (sparse homophones on frequent
syllables) corroborates F33's conditioned-polyvalence picture and supports
turning on a concentration-style prior (currently LAM_HOM=0.0) rather than
free polyvalence.

## 5. Import list for the engine (from side-homophonic; see homophonic_synergy.md)

In order: (1) fix lam_poly scale (penalty commensurate with the letter term);
(2) phonetic projection (absorbs ear noise: truth loses ~0.33 nats/letter to it
on the raw 7-gram); (3) spanning-only word bonus (long-range coherence the
7-gram cannot see); (4) concentration penalty ON; (5) homophone-pool + block
proposals; (6) per-stream chi2-gated phase prior (drop the banked phase map —
61/96 groups changed phase under the repair); (7) F34 inventory rebuild for
the R5005 run.

## 6. Verdict (pending route-a/b completion)

[To be filled when `scorer_identifiability.json` stages complete.]
Best next step regardless: repair the objective (§0, §5) BEFORE judging
search vs identifiability — the current objective's optimum is not truth, so
no search result on it can pass the control.
