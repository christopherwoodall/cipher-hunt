# The Solver That Works — R5005 attack plan

**Author:** Solver Architect (council, reporting to parent — no coordinator).
**Date:** 2026-10-07.
**Status:** Track D pilot PASSED 6/6 (truth–salad margins 39–43 pts, memorization
probe clean). This plan assumes red-team gate clearance and designs the full
pipeline from control to R5005. Nothing here touches R5005 until a track
passes all six control checks.

---

## 1. The core architectural claim (read this first)

Three things are true, and the pipeline is built on all three:

1. **The search must move in cell space, not group space.** The current
   annealer moves one group at a time in an 89-dimensional space, but the
   objective lives in the ~30-dimensional cell space and the projection is
   many-to-one and discontinuous under local moves: changing one group's
   cell alters all its occurrences at once (nonlocal in decode space),
   while the moves the landscape actually wants — reassigning a whole
   alias set — require dozens of coordinated group moves the annealer will
   never make together. This is the "30-symbol projection" problem, and no
   amount of restarts fixes it. The generator *built* the key by dealing
   aliases per cell; the solver must *search* per cell. Reparameterize:
   the key is a mapping cell → set of groups, and the move set operates on
   alias sets (reassign / swap / split / merge), with single-group moves
   kept only for fine-tuning.

2. **Rerank-only cannot beat the generator's bias.** Track D's pilot proved
   the judge *distinguishes* truth from salad. It did not prove the annealer
   *generates* truth-adjacent candidates. Under the repaired objective J,
   truth loses to salad by 2,601 nats — so every restart converges to a
   salad basin, and the judge just picks the best salad. Primary recovery
   stays at chance. For the gate to pass, the judge must influence *which
   regions get explored*, not just which final gets picked. The pipeline
   below puts the judge in the search loop via a bounded funnel +
   judge-guided iterated local search — not as a final filter.

3. **Fluency is the ground truth; the 5-gram is just a proposal engine.**
   J (Tocqueville char-5-gram + lexicon) is demoted to a *cheap smooth
   proposal distribution* for generating diverse candidates. The frozen
   judge is the *selection criterion*. These are different jobs and they
   must not be confused again: every Goodhart failure in this lane came
   from asking a statistical proxy to do a judge's job.

---

## 2. Experiment 0 — the basin probe (do this before building anything)

**Question:** under J, is the planted truth even a *local* optimum?

**Protocol (per control instance, cheap — 1 run each):** initialize the
annealer AT the sealed truth key, run 40k iters under J, record whether it
stays (final key within Hamming distance ≤ 5 of truth in group space) or
slides to a salad basin (final J > J(truth) by > 500 nats with primary
recovery < 0.10).

**Branch:**
- **Truth is locally optimal** → §3's funnel works: lexicon-seeded starts
  near truth-like regions survive under J, and the judge picks them out.
- **Truth is NOT locally optimal** → no restart-based method under J can
  work, period. Skip §3's Stage 2 as designed; go straight to judge-driven
  search (§3 Stage 4 as the *primary* loop, seeded from lexicon starts
  rather than J-climbs), or escalate to the SPS fallback (§7).

Cost: 6 runs × ~88 s ≈ 9 min. This is the highest-information experiment
in the plan. Do not skip it.

---

## 3. The funnel pipeline (pseudocode-level)

```
INPUT: ct pairs (1,846), crib JSON (7 pins), Tocqueville LM, inventory (296 cells)
OUTPUT: one 96-group → cell key per instance

PINS: 7 GT groups fixed forever. (R5005: + provisionals as STRONG soft
      constraints, NOT hard pins — a wrong provisional must be escapable.
      Restructured registry (code/crowd14/registry/REGISTRY.md) → word-rule
      and class-tier constraints, LEAD-grade and up; the 67 fork is the
      only conditioned-polyvalence mask. No reading merges 33+86, 48+94,
      76+78, or 52+59.)

STAGE 1 — diverse seeding (compute: trivial)
  seeds = []
  seeds += 100 × random keys (pins fixed, rest uniform over inventory)
  seeds += 60 × lexicon-seeded keys:
             for high-frequency windows, assign groups to cells that form
             real inventory words covering the window (crib-inventory drag);
             remainder random
  seeds += 40 × crib-extended keys:
             propagate pins via bigram constraints (if 11=la then probable
             neighbors get la-compatible cells), remainder random
  # 200 seeds spanning random / word-like / crib-consistent basins

STAGE 2 — cheap climb (compute: 200 × 5k iters ≈ 11 s each ≈ 37 min/instance,
          fully parallelizable across instances)
  for s in seeds:
      k_s = anneal(s, iters=5000, moves=CELL_SPACE_MOVES, objective=J)
  candidates = [k_s for s in seeds]   # 200 diverse local optima under J

STAGE 3 — judge triage (judge calls: 200 × 1 pass = 200;
          top-40 × 2 more passes = 80; total 280/instance)
  scores1 = judge_1pass(candidates)          # frozen prompt, blind labels
  top40 = argtop40(scores1)
  scores_med = median3(top40)                # 2 more passes, blind, new order
  parents = argtop5(scores_med)

STAGE 4 — judge-guided iterated local search
          (judge calls: 3 rounds × 5 parents × 10 neighbors = 150 (1 pass);
           final top-10 × 2 passes = 20; total 170/instance)
  for round in 1..3:
      neighbors = []
      for p in parents:
          for i in 1..10:
              n = cell_space_mutate(p)       # alias-reassign / cell-swap /
                                             # split / merge, 1–3 cells
              neighbors.append(n)
      s1 = judge_1pass(neighbors)            # blind labels
      pool = parents + neighbors
      parents = argtop5(median(pool_scores)) # keep medians where available
  finalists = argtop10(all judged)
  finalists_med = median3(finalists)
  WINNER = argmax(finalists_med)             # tie-break: higher J, then lower index

STAGE 5 — gate scoring
  emit WINNER's 96-group mapping → Runner scores PRIMARY/SECONDARY
  against sealed keys per CONTROL-DESIGN.md §4.
```

**Judge-call budget:** 280 + 170 = **450/instance**, **2,700 for the 6-instance
gate**. Annealer compute ≈ 40 min/instance wall (parallelizable to ~40 min
total). For R5005 (single instance): same per-instance budget.

**Judge instrument requirement:** the current judge is the operator by hand
(54 calls for the pilot). 2,700 calls is not hand-feasible. The gate REQUIRES
an automated judge instrument before it runs — either (a) subagent-judges:
fresh LM instances with the frozen prompt (sha256-pinned), blind labels,
median-of-3, full logging — the french-blitz pattern proves this works; or
(b) a local/API LM endpoint. Whichever substrate, the instrument MUST satisfy
Track D's §2 protocol (frozen prompt hash, blind labels, no re-query,
complete log) or the gate is invalid. This is the #1 infrastructure
prerequisite. The memorization probe (§4 of Track D's PREREG) must be re-run
on the gate truths before unsealing (36 calls) — the pilot's probe covered
the OLD instances; the gate uses FRESH slices.

---

## 4. The cell-space move set (the actual fix for the search)

The annealer keeps its existing single-group moves (chg1/swap/poly/chg2) for
fine-tuning, but the proposal distribution becomes:

| move | probability | definition |
|---|---|---|
| chg1 (single-group reassign) | 0.30 | as now |
| swap (two groups) | 0.10 | as now |
| poly (secondary toggle) | 0.10 | as now |
| **alias-reassign** | 0.30 | pick cell c in use, pick new cell c′; ALL groups with v1==c → c′ |
| **cell-swap** | 0.10 | swap the group-sets of cells c1, c2 |
| **alias-split/merge** | 0.10 | split: move random subset of c's groups to c′; merge: all of c2's groups → c1 |

`block` (contact-neighborhood) is dropped — contact ≠ alias, and the
rotation fleet proved contact clustering can't recover alias structure
anyway.

**Why this works where single-group moves don't:** the generator deals each
cell's aliases round-robin across groups. The natural "edit distance" of the
key space is in alias sets: the difference between a salad key and the truth
key is concentrated in a few dozen cell-level reassignments, each of which
costs the single-group annealer dozens of coordinated moves through
J-worse intermediate states. Alias-reassign crosses that valley in one step.
Expected effect: restarts land in *fewer, better* basins, and Stage 4's ILS
can actually climb the judge landscape instead of rattling inside one basin.

**Implementation note:** the solver already tracks `v1[g]` per group;
alias-reassign is `for g in groups_of(c): propose v1[g]=c′` applied as one
atomic move with a single delta computation. The `_region`/`snapshot`/
`revert` machinery handles multi-group touches already (the `block` move
uses it). ~40 lines.

---

## 5. The control — assessment and changes

The current 6-instance design is good. It discriminates "real signal" from
"chance" on: register gap (Les Mis vs Tocqueville, deliberate), homophony
density (frequency-weighted, ≥ round-1), polyvalence (2× known), rotation
(calibrated band), ear noise (at/above calibrated knobs), with computed
(not guessed) chance baselines and pre-registered bars. **Do not move the
bars** — they're registered.

Recommended changes (additive only):

1. **Re-run the memorization probe on gate truths** (36 judge calls) before
   unsealing. Non-negotiable: the pilot's probe covered old slices; the
   gate's slices are fresh.
2. **Add 2 diplomatic-plaintext instances as a secondary gate** (Track A's
   register-matched instances). The 6 Les Mis instances stay the primary
   gate (comparability). If the solver passes Les Mis but fails diplomatic
   French, it will not transfer to R5005 — report both, require the primary
   only, but *believe* the secondary.
3. **Noise-mismatch ablation** (2 instances, 2× ear noise; report-only).
   The Frenchman's H-split finding says the real encipherer over-splits
   beyond the generator's knobs. Graceful degradation here predicts R5005
   robustness; a cliff predicts failure.
4. **Keep the q_cycle=0 ablation set** (184213–184218) as the rhythm-crutch
   check — already built, already pre-registered. Any solver that collapses
   on the scrubbed set is leaning on rotation, not French.
5. **Do not add a "strong pass" tier to the control.** The R5005 criteria
   (§6) handle "solved vs signal" — the control stays a floor.

One honest limitation to log with the gate result: **the control has no
fluent-but-wrong decoys.** On synthetic instances the only fluent decode is
the truth, so the gate cannot test whether the judge would prefer a fluent
*incorrect* key. §6's topic check is the R5005-side mitigation.

---

## 6. R5005 success criteria — pre-registered, operational

"Looks like French" is not a criterion. An R5005 run is scored against all
five; **"solved" requires all five.** Register these BEFORE the run.

1. **Board consistency.** The winning key, restricted to board groups, must
   match ≥11 of the 12 board values (7 GT + 5 provisional), with every
   restructured-registry word/frame/class rule satisfied at its registered
   windows (67 fork per its banked arms; no 33+86 / 48+94 / 76+78 / 52+59
   merges). A
   "solution" that contradicts the board is a different hypothesis, not a
   solution. (One provisional may fall only with a red-team ruling citing
   the contradicting window.)
2. **Judge bar.** Judge-score the R5005 decode with the frozen gate prompt
   (3 passes, median). Bar: **≥ (mean gate-winning median − 2σ)**, and in
   any case **≥ 55** (gate truths scored ~62; salads ~20). Below bar =
   not solved, full stop.
3. **Topic check (the anti-salad tripwire).** The decode must contain ≥3
   independently verifiable period facts checkable against the period
   corpus (e.g., named entities: Méhémet-Ali, Treaty of London / 15 July,
   the Porte; date references; "par ce que"-class formulae in grammatical
   frames). A fluent-but-wrong decode cannot name the right Pasha. Each
   fact is cited to corpus + window. This is the strongest criterion —
   salad can't do it.
4. **Independent reproduction.** A separate agent, given ONLY the winning
   key (never the solver), reproduces the decode byte-exact with
   independent code and confirms it reads as coherent 1841 diplomatic
   French. (Catches implementation bugs masquerading as solutions.)
5. **Perturbation stability.** Swap 5 random non-pin groups in the winning
   key; the decode's topic content (criterion 3's facts) must survive in
   ≥4 of 5 perturbations. A real solution is robust; a salad shatters —
   this is the poor man's significance test for "the key is right" vs
   "the judge got lucky."

**What "solved" does NOT require:** 100% primary recovery (impossible to
verify without the key), every group identified, or the rotation explained.
It requires: board-consistent, judge-passing, topic-bearing, independently
reproducible, stable. That's shippable.

---

## 7. Fallback — if Track D's pilot had failed (it didn't, but the plan exists)

**Diagnosis of that world:** if a fluent French LM cannot distinguish
planted truth from morpheme salad, the failure is not in any scorer — it's
that *fluency statistics* (at every level: character, morpheme, holistic)
don't separate the classes. What separates them is **linguistic structure**:
the salad has no WORDS and no SYNTAX, by construction. No statistical
model of any family can see what isn't there statistically — you need a
structural one.

**Architecture: Segment-Parse-Score (SPS).** It makes explicit what the LM
judge does implicitly (implicit word segmentation + syntactic evaluation),
which is why it's the principled fallback rather than a different idea:

```
decode string (spaceless, ear-noised)
  → BY-EAR NORMALIZE (strip accents; apply the lane's 296-item by-ear
     inventory alternations: pre/prend, m'/me, mute-e, etc.)
  → SEGMENT: dynamic program over the string maximizing
       Σ [wordLM(w_i) + lexicon_bonus(w_i)] − γ·(#OOV)
     using a French word lexicon (diplomatic corpus vocabulary).
     The salad's "words" are overwhelmingly OOV or forced — its best
     segmentation is garbage by construction.
  → PARSE: French dependency parser (UD pipeline) over the word sequence;
     features: fraction of words with valid heads, mean arc confidence,
     root plausibility.
  → SCORE = α·wordLM + β·parse_confidence + γ·coverage − δ·OOV_rate
     (α,β,γ,δ pre-registered; tuned on a HELD-OUT slice, never the gate)
```

**Why it kills the salad dead:** "tre elle ter pre me gouverne" has no
lexicon words (OOV_rate ≈ 1) and no parse (no heads). Truth — even
ear-noised, even register-gapped — segments into real words that parse.
The margin isn't statistical, it's structural: it's the difference between
*has syntax* and *doesn't*. No reweighting can save the salad because
there is nothing to reweight toward.

**Cost:** the segmenter is O(n · maxwordlen) DP per decode — milliseconds.
The parser is the expensive piece (~seconds/decode with a UD pipeline),
but it's still 10–100× cheaper than an LM judge call, and it's
deterministic. SPS slots into §3's pipeline as a drop-in replacement for
the judge (Stages 3–4 unchanged, just cheaper and deterministic).

**When to trigger it:** if (a) Track D's gate fails despite the pilot
passing (judge doesn't transfer from pilot to gate), or (b) the automated
judge instrument (§3) proves infeasible. Do not build it speculatively
while D is alive — it's the contingency, and contingencies cost focus.

---

## 8. What I'd do Monday morning (prioritized)

1. **Run Experiment 0** (basin probe, 9 min). It gates the architecture.
2. **Stand up the automated judge instrument** (subagent-judges, frozen
   prompt hash, blind labels). Nothing downstream runs without it.
3. **Implement cell-space moves** (~40 lines in solver.py) + re-run one
   control instance to confirm the annealer still functions.
4. **Run the §3 funnel on the 6 fresh instances.** This IS the gate.
5. **In parallel:** Track A finishes the diplomatic-plaintext instances
   (secondary gate); red team pre-registers the §6 R5005 criteria.
6. **If the gate passes:** R5005 run under §6 criteria. If it fails:
   read the per-instance numbers — *where* it failed (coverage? judge
   transfer? ILS stuck?) dictates whether the fix is more seeds, more
   ILS rounds, or the SPS fallback.

---

## 9. Weakest load-bearing assumption of the current paradigm

The paradigm validates on synthetic Les Misérables instances and assumes the
result transfers to real 1841 diplomatic French — and three specific transfer
gaps are untested. First, register *direction*: the control preserves *a*
gap (Les Mis vs Tocqueville) as a stand-in for *the* gap (diplomatic French
vs Tocqueville), but narrative prose and diplomatic despatches differ in
kind, not just degree — formulaic frames, named entities, and topic
structure that the solver never sees in training. Second, ear-noise fidelity:
the generator's noise knobs are calibrated to a segmenter control, yet the
Frenchman's H-split finding says the real encipherer over-splits *beyond*
those knobs, so a solver tuned to synthetic noise may face a harsher real
distribution. Third, and sharpest: the control contains no fluent-but-wrong
decoys — on synthetic instances the only fluent decode is the truth, so the
gate cannot falsify "fluency implies correctness," which is precisely the
assumption an R5005 run leans on hardest, since there primary recovery can't
be measured at all. The control is excellent at discriminating chance from
signal; it is silent on whether the signal transfers. Track A's
register-matched instances and §6's topic check are the mitigations, but
until they run, transfer is faith, not evidence.
