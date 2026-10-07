# HOMOPHONIC-FLEET SYNERGY — scorer-smith round 5 (2026-10-07)

Read-only review of `code/side-homophonic/` (independent solver, mid-flight).
Nothing duplicated; techniques assessed for import into the round-4 joint engine.

## Status read (all numbers from files actually read)

- **Negative control: PASS (~chance).** `runs/negative-control/negctrl_results.json`:
  round-1 annealer on the 6 synthetic instances, 12 restarts x 60k iters:
  mean PRIMARY 0.0412 (per-seed 0.0337-0.0449) vs chance 0.0206-0.0223.
  Verdict field: `NEGATIVE-CONTROL-OK`. The instances are not trivially solvable
  by the old method.
- **Positive control: IN FLIGHT, no verdict yet — first attempt ABORTED.**
  `runs/control_batch.log`: the 15:20Z batch ran seeds 184101/184102 for 1789s
  (184101 completed 12/12 restarts; 184102 reached 10/12), then both were
  SIGTERMed (rc=143) at 15:50:18Z before scoring; seeds 184103–184106 failed
  instantly (rc=2: the batch script passed `--chance`, which the harness no
  longer accepts). Root cause: the side-fleet owner edited
  `solver/control_harness.py` at ~15:42Z mid-batch (removed the `--chance` CLI
  flag; chance now internal via `chance_baseline.json`/BARS). A NEW run is in
  flight as of 15:54–15:55Z: `runs/run2-184101` and `runs/frozen-ctl-18410{1,2}`
  (three concurrent harnesses; "frozen" suggests the ablation winner config;
  run2 shows inventory=291 vs 288 before). No `control_report.json` exists for
  any instance yet — nothing is scorable. The pre-registered bars
  (`runs/score_control.py`: PRIMARY mean>=0.20/min>=0.10, SECONDARY
  mean>=0.30/min>=0.22) still govern the eventual verdict.
- **Config in flight** (`ctl-18410{1,2}.stdout.log`): restarts=12, iters=40000,
  t0=60, tmin=0.05, lambda_word=1.0, beta0=2.0, w_soft=3.0, lambda_poly=20.0,
  inventory=288, 143 projection collisions. **Phase gate nearly CLOSED on both
  running instances**: chi2=36.6 -> gate=0.0262 (beta=0.052) and chi2=0.4 ->
  gate=0.0013 (beta=0.003). The Potts phase prior is effectively OFF — the
  positive control is currently an unintended ablation of the phase term
  (CONTROL-DESIGN.md §3 documents the unsupervised chi2 as a noisy detector
  on synthetic: 0.4-787 across instances).

## What they do differently (METHOD.md + code)

1. **Phonetic projection** (`solver/phonetics.py`, 30 classes, evidence-graded
   rules): the char 5-gram scores phoneticized French, absorbing by-ear spelling
   noise. Their METHOD.md §1 names the difference explicitly: the round-4 joint
   engine "scores raw letters, so their own control's ear-substitutions cost
   likelihood."
2. **Word-salad bonus, spanning-only** (`build_lm.py` Aho-Corasick over projected
   lexicon): only words assembled from 2+ values count. Added after measuring
   that the char 5-gram PREFERS frequent-word salad to real register-mismatched
   French (pilot: salad -3.89/pair vs truth -4.44/pair).
3. **Concentration penalty ON** (lambda_conc=5.0, cap=6, over projected values):
   kills the repetition exploit (50+ groups -> 'me' earning word bonus via
   'me'+'me'="meme"). The round-4 engine has the analogous LAM_HOM penalty but
   it was OFF (0.0) in the control config.
4. **chi2-gated contact Potts** (`phase.py`): no banked phase map; block labels
   recomputed per stream; gate = sigmoid((chi2-80)/12) shuts the prior off on
   rhythmless streams. Verbatim copy of the generator's unsupervised chi2, so
   the gate is calibrated to the control's ruler.
5. **Proposals**: change/swap/poly + homophone-pool copy (20% of changes copy a
   contact-neighbor's value) + block moves over contact neighborhoods + greedy
   refine pass. No parallel tempering (12 plain restarts).
6. **Inventory 288** (UNITS + top-200 encipher_split cells) vs the joint engine's
   617. Tighter; they document the UNITS-vs-planted mismatch (78-83% coverage)
   and resolve it explicitly.
7. **Control design**: Les Mis plaintext (register gap preserved vs the
   Tocqueville reference — same gap the real R5005 has); frequency-weighted
   homophony (common cells get most aliases — the historical design and the
   hardest case); 6 polyvalent islets (2x the established real count);
   occurrence-phase chi2 calibrated to [181,320]. Bars at 9.3x chance (PRIMARY),
   far below the 0.90-0.93 oracle ceiling.

## Import-worthy techniques (for the joint engine)

- **Phonetic projection** — highest value. Round-5 measurement (this lane):
  truth s_let=-3.4313 vs annealed s_let=-3.1055 on the raw-letter 7-gram; the
  ear noise in the truth costs ~0.33 nats/letter. A projection layer would
  absorb exactly this. (Their 42-case self-test in `phonetics.py` is reusable.)
- **Spanning-only word bonus** — the long-range coherence term the joint engine
  lacks (its letter 7-gram sees ~7 chars). Their "salad beats truth" pilot is
  the same failure family as our annealer's fluent nonsense.
- **Concentration penalty ON** — turn on LAM_HOM (currently 0.0) with their
  cap-6 scale before any R5005 run; the joint engine's round-4 config had no
  anti-collapse guardrail active.
- **Homophone-pool + block proposals** — cheap to add; directly attacks the
  glassy landscape (their words: "single-group moves in a glassy landscape"
  was a round-1 failure mode).
- **Per-stream phase recompute, chi2-gated** — replaces the fragile banked
  phase map (61/96 groups changed phase under the parse repair; N30).

## Contradiction diagnosed: "model-correct" vs "degenerate optimum"

N30 (round-4 joint engine): "model-correct but BROKEN-ON-CONTROL — truth -2.65
beats annealed -3.05 ... identifiability problem (flat landscape), not a model
problem."

Side-homophonic METHOD.md §1 + pilot: the char n-gram LM's global optimum sits
ABOVE truth (salad -3.89/pair beats truth -4.44/pair) — a MODEL problem, fixed
by the spanning word bonus + concentration penalty.

**Round-5 recomputation (current `joint_engine.py`, same control) sides with
the side fleet — and sharpens N30's "model-correct" into an apples-to-oranges
comparison:**

| key | lam_poly | total | s_let (per-letter) | n_poly |
|---|---|---|---|---|
| truth key + model's own E-step decode | 0 (penalty off) | **-2.64** | -3.6395 | 3 |
| truth key + model's own E-step decode | 10 (as configured) | -32.64 | -3.6395 | 3 |
| truth key + emitted (data-generating) decode | 10 | -32.43 | -3.4313 | 3 |
| annealed best (600 sweeps, round-4 config) | 10 | **-2.91** | -3.1055 | 0 |

- N30's "truth -2.65" reproduces **only** as the truth key scored with
  lam_poly=0 — the polyvalence penalty disabled. N30's "annealed -3.05" was
  scored with lam_poly=10 (where the annealed key, n_poly=0, pays nothing).
  On the ACTUAL search objective (lam_poly=10), truth (-32.64) sits ~30 nats
  BELOW the annealed nonsense (-2.91). The search is optimizing correctly;
  the objective is wrong. "Model-correct" does not survive the penalty term.
- Even with the penalty off, the **letter term alone** prefers the annealed
  key (-3.11/letter) over the truth key's E-step decode (-3.64/letter). The
  raw-letter 7-gram ranks non-truth above truth — the same disease as their
  5-gram pilot, milder. (Their fix: phonetic projection + spanning word bonus
  + concentration penalty — the concrete repair this engine lacks.)
- The E-step itself recovers only 42/63 (0.667) of the truth's islet
  emissions: the model's per-occurrence mechanism cannot even re-derive the
  data-generating assignments from the true key.
- The **polyvalence penalty is on the wrong scale**: lam_poly=10 nats per
  polyvalent group vs a per-letter-normalized letter term (O(1)). Adding v2
  would need to improve the total letter sum by > lam_poly x total_letters
  (~58,000 nats) to pay for itself — so v2 is NEVER added (annealed n_poly=0).
  The islet bar (>=2/3) is unmeetable BY CONSTRUCTION at lam_poly in {10, 20}.
  This is a model bug, not a search failure.
- **Why the two diagnoses differed**: different LMs (their 5-gram+word-bonus
  vs our raw 7-gram), different penalties, different controls. The underlying
  agreement: BOTH engines' n-gram objectives rank non-truth keys above truth.
  Their fix (phonetics + spanning word bonus + concentration penalty) is the
  concrete repair our engine lacks.

**Caveat (mine, not theirs):** the two controls are not the same test. Their
control plants frequency-weighted homophony with well-defined per-group
primaries; my round-4 control's lossy tail inheritance makes 2/20 bar groups
unidentifiable BY CONSTRUCTION (group 41: truth primary 'ri' emitted 1.8% of
274 occurrences, modal emitted 'mi' 2.2%, 160 distinct cells; group 31:
'pas' 18% vs modal 'pa' 32%). Max achievable top-1 on my control's bar is 0.90,
and the "shared"-group labels are partly arbitrary. A control PASS on theirs
would not certify my engine, and vice versa.

## Cross-fleet intel (round-5 briefing) applied to the synergy read

- **F34 crib-derived inventory** applies to their solver as well: their 288-cell
  inventory (UNITS ∪ top-200 encipher_split) is rule-syllabifier-derived, and
  their control plants from encipher_split cells — self-consistent for the
  control, same machinery-not-unit-set tension as ours (their control cannot
  validate an F34-compliant inventory either). If their positive control passes,
  the pass certifies the phonetics/word-bonus/concentration stack, not the unit
  alphabet; their R5005 run would still need the 24-unit crib-derived rebuild
  (`code/crowd5/unit_inventory.json` + `code/side-wordpattern/lexicon/` under
  R1–R8). Note their inventory already includes single letters and their
  phonetic projection is the closest existing instrument to F34's by-ear
  requirement.
- **Anchor-preserving controls**: both controls are fully synthetic (no
  shuffling); the sidepath de-anchoring lesson does not apply to either.
- **No nulls**: neither solver models null groups — consistent with the
  petit-chiffre intel; no change needed on either side.

## Verdict on the positive control (pending)

Cannot score until all six instances land (est. 1.5-2.5h for the full batch at
current pace). Watch items for the final read:
1. Whether PRIMARY clears 0.20 mean / 0.10 min with the phase gate nearly
   closed — a pass would credit the phonetics+word-bonus+concentration stack;
   a fail near the bar may implicate the missing phase term (their ablation
   matrix {full, --no-phase, ...} will tell).
2. Their SECONDARY proxy (frequency-weighted primary agreement per position)
   vs our decode-agreement metric — compare apples to apples at scoring time.
3. If their positive control PASSES and our route-(a)/(b) still fails on our
   control: the difference is the model stack (phonetics/word-bonus), not the
   sampler — import it. If theirs FAILS too: the joint-SA family is
   control-broken twice independently; the next step is a different inference
   family or a redesigned control, not more annealing.

## Best next step (my recommendation)

Do not run R5005 on either engine yet. The joint engine needs, in order:
(1) fix the lam_poly scale bug (penalty must be commensurate with the
per-letter letter term, or un-normalize the letter sum); (2) import the
phonetic projection and spanning word bonus; (3) turn on the concentration
penalty; (4) re-run the control with the repaired objective — then judge
search vs identifiability. Route-(a)/(b) results (in
`scorer_identifiability.json`) quantify how much of the gap is search vs
model; the model bugs above bound what search alone can achieve.
