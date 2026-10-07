# METHOD — joint-inference homophonic solver (side fleet, solver-smith)

## 1. Method choice: simulated annealing over the full key

**Choice:** stochastic local search (simulated annealing, Metropolis moves,
geometric cooling, multiple restarts, best-key retention) over the complete
96-group → value assignment, maximizing a joint objective. Not EM, not Gibbs.

**Why SA, and why it fits this problem's structure:**

1. **The failure was the objective, not the sampler.** Round 1
   (`code/crowd/anneal.py`) already did joint SA and scored 1/88 ≈ chance on
   its control (`code/crowd/annealer_results.md`). Its SA explored fine
   (z = +17.7 vs baseline, stable modal assignments across 24 restarts) and
   converged *confidently to the wrong answer*. Swapping the sampler cannot
   fix an uninformative likelihood. The scorer-smith's diagnosis
   (`code/crowd3/scorer_smith_results.md`, "the N12-style finding") is
   precise: bigram contexts underdetermine each cell; the true value is
   *consistent but not distinctive*. What was missing is a **discriminative
   joint objective**, which is what this solver builds (Sections 3-5).
   SA is the minimal, lane-validated sampler for it.

2. **Discrete constrained space.** The key has hard pins (7 groups never move)
   and a sparse polyvalence penalty; values are strings from a ~300-item
   inventory. SA enforces hard constraints by construction (never propose a
   pinned move). EM wants a soft/probabilistic key plus a projection step;
   Gibbs wants carefully designed conditionals for the Potts term and the
   per-occurrence E-step. Both add machinery without adding escapes from the
   glassy landscape that trapped round 1.

3. **EM is greedier, Gibbs is richer but the lane needs a decision.** EM
   (deterministic hill-climbing on a soft key) is *more* prone than SA to the
   local optima that killed round 1 — it has no temperature. Gibbs with
   annealing is approximately SA with extra bookkeeping; its real advantage
   (posterior marginals) is recovered here more cheaply via cross-restart
   consensus (marginals = fraction of restarts agreeing), which is also the
   lane's established idiom (round-1 stability table).

4. **Validation protocol exists for SA.** Restarts / random-key baselines /
   modal votes / recovery rates are the lane's control idiom
   (`annealer_results.md`, `scorer_smith_results.md`, crowd4's `synth_control.py`
   PASS_BARS). The Runner reuses it unchanged. A new sampler would need new
   diagnostics and a new gate argument.

**How this SA avoids round-1's specific failure modes:**
- *Letters were inexpressible.* Round 1 scored letters as syllables in a
  syllable-bigram LM, so the true key (containing 82=m, 34=i, 40=e) could
  never win; everything collapsed to de/la/le. Here every value is a string
  and the LM is a **character** 5-gram over the concatenated decode: letters
  and syllables compete on equal footing, and the degenerate de/la collapse
  scores terribly ("dedede…" has no French 5-grams).
- *Single-group moves in a glassy landscape.* Added: swap moves, block moves
  over contact-neighborhoods (so Potts-coupled groups move together), and a
  homophone-pool proposal (20% of changes copy a contact-neighbor's value).
  Plus a greedy refine pass with the full objective.
- *Uninformative likelihood.* The objective (Sections 3-5) is built so the
  true key is *distinctive*, not merely consistent: character 5-grams over
  phoneticized French (local), word-salad bonus (long-range), contact Potts
  (structural). The control decides whether this is true; the pre-registered
  bars are in Section 7.

**Relationship to crowd4's joint engine** (`code/crowd4/joint_engine.py`,
same lane, parallel effort): that engine is also SA over the full key with a
letter n-gram + phase term + v1/v2 polyvalence, and its control run was still
in flight when this solver was written (early ablation: 0.05-0.10 recovery vs
a 0.50 bar). This solver differs in four load-bearing ways: (a) a **phonetic
projection** absorbs by-ear spelling noise (their engine scores raw letters,
so their own control's ear-substitutions cost likelihood); (b) a **word-level
term** adds long-range coherence beyond 5-grams; (c) the inventory defaults
to UNITS ∪ top encipher_split cells (~300) instead of top-600 corpus units
(tighter search, and it covers the Designer's planted inventory -- Section 6);
(d) the phase term is a chi2-gated **contact Potts** rather than a
cell-phase profile likelihood, with no R5005-banked phase map (recomputed
per stream, so it works on controls).

## 2. Key model

- `v1[g]`: primary value string per group. **Many-to-one allowed** (no
  injectivity constraint): this is the task's "polyvalence
  (many-groups→one-syllable)", i.e. homophony. The historical table spreads
  common cells over many groups; forbidding it would be a model error.
- `v2[g]` ∈ {None} ∪ inventory, `w2[g]` ∈ [0,1]: optional secondary value.
  Per-occurrence **hard E-step**: each occurrence decodes to
  argmax over {v1, v2} of local char-5-gram score + log weight, with a closed-
  form M-step for w2 after each move. This is the lane's R5 polyvalence
  (one group, several readings: 94=ne/en, 52=pas/so, 06=-ent/stem;
  `code/sidepath/phonetic_rules.md`), penalized by λ_poly = 20 nats per
  polyvalent group (sparsity; ablatable via --no-poly).
- **Hard pins** (never proposed, no secondary): 11=la, 70=pre, 82=m, 34=i,
  29=er, 40=e, 46=que -- the pencil-crib ground truth
  (`data/upstream-NOTES.md`, STATE.md).
- **Soft priors** (bonus w_soft = 3.0 nats each, NOT pins): 87=ce, 64=qui,
  96=par -- provisional lane inferences (red-team authority: provisional,
  `phonetic_rules.md` FORBIDDEN #10). 3 nats is ~7:1 odds: strong enough to
  bias, weak enough that ~5 occurrences of contrary evidence overturn it.
  **Disabled for synthetic controls** (--no-soft; the harness forces it):
  they are R5005-specific and would be false priors on a control. The
  control validates the method on 7 pins alone; the R5005 run enables them,
  with a with/without robustness check (mirroring scorer3's table10/table7).

## 3. Language model

**Character 5-gram LM over phoneticized French** (`build_lm.py`,
`phonetics.py`), trained on Tocqueville T1 (1835) + T2 (1840), Gutenberg
30513/30514 -- 214,861 words, 768,532 projected chars, 29-symbol alphabet,
134,855 distinct 5-grams, held-out perplexity 6.4/char (see `lm_stats.md`
from any build).

- **No syllabifier in the scorer.** Deliberate (F30 compliance):
  rigid syllabification is dead as an instrument (`phonetic_rules.md`
  FORBIDDEN #2; the encipherer cuts inconsistently, R2). The decode is scored
  as a **character stream**; cuts never enter the objective. The lane's rule
  syllabifier (`code/crowd2/scorer_smith.py`) is used only to build the
  *candidate inventory* (a word list, never a conditional model) -- same
  discipline as crowd4.
- **Spaceless training.** The corpus is projected word-by-word, then
  concatenated with no boundaries: the deciphered stream has no word
  boundaries either, so train and decode see the same object.
- **Smoothing:** interpolated (order-5 → unigram backoff, α = 0.5), cached.
- **Word-salad bonus** (λ_word = 1.0, ablatable): Aho-Corasick over the
  projected era lexicon (3,420 words, freq ≥ 3, projected length ≥ 4,
  weight log(1+freq), overlapping hits allowed). It is a *scoring function*,
  not a parse: it rewards long-range French-word coherence the 5-gram cannot
  see, and it degrades gracefully under by-ear spelling (unseen words just
  contribute nothing). **Spanning-only** (fixed 2026-10-07 after a 0/89 pilot):
  `S_word = AC_scan − Σ_t single_wt[pcell[t]]`, i.e. only hits SPANNING a
  value boundary count. A key whose VALUES are common words ("leur","mais")
  otherwise earns a hit at every occurrence without deciphering anything --
  and the char-5gram actively *prefers* frequent-word salad to real
  register-mismatched French (measured on the pilot: salad −3.89/pair vs
  truth −4.44/pair). Only words assembled from 2+ values
  ('cha'+'pi'+'tre'="chapitre") are evidence of correct decipherment.
  Exact windowed delta scoring, verified by `solver.py --self-test`
  (incremental vs full recompute: max err 1.7e-10 over 300 random moves).
- **Concentration penalty** (λ_conc = 5.0, conc_cap = 6; added 2026-10-07
  after pilot 2/89): `−λ_conc·Σ_p max(0, n_p−6)²`, n_p = #groups whose v1
  PROJECTS to p (over projected values, so 'me'/'mê'/'mè' collude -- the
  solver would otherwise evade the cap via accent variants). Kills the
  *repetition exploit*: mapping 50+ groups to 'me' so that 'me'+'me'="meme"
  (spanning!) hits the lexicon at every position, earning +10,178 nats of
  word bonus for a degenerate key. The true codebook spreads 89 groups over
  ~60 cells (max quota 3–5 by largest-remainder), so cap=6 is safe for the
  truth. This is the homophonic-cipher analogue of the one-to-one constraint
  that makes substitution-cipher SA work.
- **Register caveat** (standing): 1835-1840 formal prose vs an 1841
  diplomatic despatch. Function words and morphology transfer; content
  vocabulary does not. Both LM terms degrade gracefully (Section 1). The
  control is deliberately register-gapped (Les Mis 1862 vs Tocqueville),
  which tests exactly this.

## 4. Phonetic equivalence

`phonetics.py` implements the projection π (30 classes), applied identically
to corpus, lexicon, inventory values, and every decode. Each rule carries an
evidence grade (SOLID / PROVISIONAL / SPECULATIVE, per the
`phonetic_rules.md` legend):

- SOLID: lowercase; accent classes (é/è/ê/ë **merged** -- the crib writes
  plain 'e' for è inside "premiere", so the ear doesn't split e-open/e-closed);
  ç→S; h-deletion; digraphs eau,au→o, ai,ei→e, ou→u, ph→f, th→t, qu→k,
  ch→C, gn→N; geminate collapse (R8: "erre"→er|e), except ss→S (the /s/-/z/
  distinction is real: "poisson" vs "poison").
- PROVISIONAL: context-sensitive nasals (ain,ein,ien,yen,oin→I; an,en,am,em→A;
  on,om→O; in→I; un,um→U) **only when not followed by a vowel or n/m**.
  The guard is load-bearing: without it the ground-truth crib "première"
  mis-projects to "prAiere" ("ennemi"→enemi, "premier"→premier stay oral).
  y→i, w→v; final-x-after-vowel deletes ("deux"→deu), else x→ks.
- PROVISIONAL (R11 generalization): silent word-final d,t,s,x,p,b,g,z delete
  **after a vowel/nasal-class char only** (R3 SOLID for -d in "prend"→"pre").
  The vowel guard is load-bearing (fixed 2026-10-07): without it the real
  inventory value "st" projected to "" -- an empty projection scores exactly 0
  and became a degenerate attractor the annealer exploited (80/89 groups → 'st').
  Safe *because it applies to both sides*: it removes a spelling choice the
  by-ear encipherer makes inconsistently.
- NEVER: final -e (R1: 40="e" is written), -r (29=er), single-letter values.

**Deliberate non-modeling:** by-ear *losses* (dropped nasals: "prend"→"pre";
vowel confusions) are not imitated -- they are noise the 5-gram absorbs.
Modeling the encipherer's exact ear is a rabbit hole; tolerance beats
imitation. Self-test: `python3 phonetics.py` (42 anchored cases, all pass).

## 5. Phase rhythm as a structural prior

The A→C→B→A rotation is real (χ² = 181.3, df = 4; `code/crowd/
contactor_results.md`), but the tuner KILLED the word-position reading
(`code/crowd3/tuner_results.md`; red-team M1 VOID; FORBIDDEN #2). This solver
therefore makes **no linguistic claim** about the phases. It uses them twice:

1. **Homophone-pool graph.** Jaccard similarity on top-10 contact sets
   (contactor's PRIMARY similarity). Under uniform homophone emission,
   homophones of one cell have statistically identical contacts, so
   contact-similar groups are the natural homophone pool -- a claim about
   *table structure*, not word positions.
2. **Potts prior, chi2-gated:** β·Σ J(g,h)·[v1[g]==v1[h]] over pairs with
   J ≥ 0.1, β = 2.0·gate(χ²), gate = σ((χ²−80)/12). The χ² instrument is a
   **verbatim copy** of the control generator's `unsupervised_chi2`
   (`phase.py::reference_chi2`) -- the control is calibrated to χ²∈[181,320]
   by that exact function, so the gate is calibrated to the same ruler.
   Null streams (uniform random) measure χ²∈[2,33] → gate < 0.02; R5005 and
   the control → gate ≈ 1. On a stream without the rhythm the prior shuts
   itself off. It is also proposal-relevant (20% of change-moves copy a
   contact-neighbor's value) and fully ablatable (`--no-phase`).

The block labels (A/B/C/R) are recomputed from the input stream every run;
nothing is banked from R5005, so the same code runs on controls.

## 6. Inventory: a task-brief/control conflict, and its resolution

The task brief says: draw values from `data/upstream-syll.py` UNITS (180
items). The landed control generator (`code/side-homophonic/control/
generator.py`) plants from **encipher_split cells** (top-T + anchors,
T∈{48,56,64,72}). Measured overlap (lane instruments, Tocqueville
reference): UNITS covers only **78-83%** of the top-T encipher_split cells;
missing are high-frequency cells ('é', 'à', 'dans', 'est', 'pas', 'plus',
'tr', 'res', …). Strict UNITS would cap PRIMARY recovery at ~0.80 *by
construction* -- a false negative on the method.

**Resolution:** default inventory = UNITS ∪ top-200 encipher_split cells
(~300 items, deduped; pins/soft forced in). `--inventory-mode units` restores
strict task-brief compliance for ablation. The solver reports projection
collisions (values indistinguishable to the char LM, e.g. 'res'→'re' vs
're'→'re'): 65/180 in UNITS mode -- a known, quantified limitation; ties
break post-hoc by lexicon weight.

## 7. Coordination: the control interface

`control_harness.py` implements `load_synthetic(path) → run →
scored assignment`:
- `load_synthetic` parses the Designer's `SYNTHETIC-ct-<seed>.pairs.txt`
  (`#` comments skipped). Anchors come from the disclosed crib file
  (`--crib`) or `--anchors`.
- `run` calls `solver.run_restarts` with `--no-soft` forced. **The sealed
  key file is loaded only in `score()`, after solver output is written.**
- Metrics mirror the Designer's (`chance_baseline`): PRIMARY (exact primary
  recovery, 89 non-anchor groups), SECONDARY (frequency-weighted primary
  agreement per position -- proxy; per-position planted cells are not
  persisted by the generator, flagged to the Designer), ISLET secondaries,
  MRR over restart marginals, pins-intact, best-vs-random20 margin.
- **Proposed pre-registered bars** (CONTROL-DESIGN.md finalizes): pins 7/7;
  PRIMARY ≥ 0.50; PRIMARY ≥ chance+0.30; islets ≥ 4/6 (secondary found with
  primary ranked #1); best − random20.max ≥ 200 nats; MRR ≥ 0.60. All six →
  CONTROL-PASS, else BROKEN-ON-CONTROL. Ablation matrix for the Runner:
  {full, --no-phase, --no-word, --no-poly, --inventory-mode units} × control
  instances; the winning config is frozen for R5005.

LM independence: the reference LM is Tocqueville-only; the control
plaintext is Les Misérables -- disjoint by construction. The harness asserts
this. `build_lm.py --exclude-span A B` exists for any future control that
shares the reference corpus.

## 8. Known limitations

1. One-to-many polyvalence is limited to **one** secondary per group (the
   control plants one; the real cipher's extent is unquantified, R5).
2. Position-conditioned readings (R10: the conditioning variable is
   unidentified) are approximated by the local E-step only.
3. The word bonus allows overlapping hits and uses a fixed λ_word; it is a
   secondary term by design.
4. Annealing hyperparameters (T0=60, Tmin=0.05, 12×40k) are defaults from a
   toy pilot, not tuned on the control; the Runner should check acceptance
   traces (logged per restart) and scale restarts/iters with available
   compute.
5. The phonetic projection is a normalization, not a transcription: residual
   by-ear deviations are n-gram noise. If the control's ear noise is heavier
   than the Designer's documented rates, expect graceful degradation, not a
   cliff.
6. **Not run on R5005.** No real-data execution until the control passes;
   `solver.py` has no R5005 default input, and `ct_loader.py` (the real-data
   adapter) is import-isolated from the solver core and the harness.
