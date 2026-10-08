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
- For Track D: reviews the JUDGE PROMPT itself before the judge sees any candidate; prompt frozen at sign-off.
- Re-derives headline numbers with independent code (≤0.1 nat standard).
- Enforces: NO R5005 contact (instant kill), control/diagnostic only, deterministic seeds.
- Maintains numbered `RULINGS.md` with file+line citations.

## Track D (`track-d/`) — LM-JUDGE RERANKER [priority: cheap, reports first]
Operator's idea: skip training (Track B); use a frozen fluent French LM as a
reranking judge over the repaired-objective annealer's top-K=20 candidates.
Protocol: (1) freeze judge prompt, red-team reviews before any candidate is seen;
(2) PILOT: judge scores planted truth vs frozen salad on all 6 original instances —
bar is prefers-truth 6/6 by a pre-registered clear margin, else track DEAD;
(3) if pilot passes, annealer emits top-20 per fresh instance, judge reranks,
top-1 median is the answer; (4) full 6-instance gate per CONTROL-DESIGN.md §4
(primary mean ≥0.20/min ≥0.10; secondary mean ≥0.30/min ≥0.22).
Guardrails: judge is a fixed scorer (prompt frozen, 3 queries/candidate, median,
mechanical score extraction, full judge_log.jsonl); memorization probe required
(truth plaintexts are Les Mis — if the judge prefers truth via memorization the
pilot PASS is void); R5005 stays gated until a track passes all six checks.

### Step-4 revision (council solver-architecture.md, adopted 2026-10-07)
Plain rerank is SUPERSEDED for step 4. The architect's sharp point: the pilot
proved the judge *discriminates* truth from salad, not that the annealer
*generates* truth-adjacent candidates — under J truth loses by 2,601 nats, so
every restart converges to a salad basin and rerank picks the best salad.
Step 4 = **Experiment 0 → funnel (PREREG-D-v2)**:
- **Experiment 0 (basin probe, ~9 min, FIRST):** init the annealer AT the sealed
  truth key on the 6 ORIGINAL instances (keys already open — no new seal);
  40k iters under J; stay (Hamming ≤5) vs slide (final J > J(truth)+500 nats,
  primary <0.10). Gates the architecture: truth locally optimal → full funnel;
  truth NOT locally optimal → skip triage-as-designed, judge-driven ILS as the
  primary loop from lexicon starts (or SPS escalation).
- **Cell-space moves** replace group-space search: alias-reassign / cell-swap /
  alias-split+merge (+chg1/swap/poly for fine-tuning); DROP `block`
  (contact ≠ alias). The generator deals aliases per cell; the solver searches
  per cell. (~40 lines in solver.py; re-run one control instance to confirm.)
- **The funnel:** 200 diverse seeds (100 random + 60 lexicon-seeded + 40
  crib-extended) → 5k-iter climbs → judge triage (280 calls: 200×1 pass +
  top-40×2) → judge-guided ILS with cell-space mutations (170 calls) →
  winner. 450 calls/instance, 2,700 for the gate. J demoted to cheap smooth
  proposal engine; the frozen judge is the selection criterion.
- **#1 infrastructure prerequisite:** an AUTOMATED judge instrument (subagent-
  judges with frozen prompt sha256, blind labels, median-of-3, full logging —
  the french-blitz pattern — or a local/API endpoint). 2,700 calls is not
  hand-feasible. The instrument must satisfy Track D's §2 protocol or the
  gate is invalid. Prototype-validated before the gate runs.
- **Additive controls (bars do NOT move):** memorization probe re-run on GATE
  truths (36 calls) before unsealing — non-negotiable; 2 diplomatic-plaintext
  instances as secondary gate (require primary only, believe secondary);
  noise-mismatch ablation (2× ear noise, report-only); keep q_cycle=0 set.
- **R5005 "solved" = all 5 pre-registered criteria** (§6): board consistency
  (≥11/12 board values + islet rules); judge bar (≥ gate-winning mean −2σ,
  and ≥55); TOPIC CHECK — ≥3 independently verifiable period facts (the
  anti-salad tripwire; salad can't name the right Pasha); independent
  reproduction (separate agent, byte-exact decode); perturbation stability
  (topic survives ≥4/5 five-group swaps). "Looks like French" is not a
  criterion.
- **Fallback:** if the judge doesn't transfer pilot→gate, or the instrument
  proves infeasible → Segment-Parse-Score (structural: DP segmentation +
  word-LM + dependency parse; 10–100× cheaper, deterministic). Do NOT build
  speculatively while D is alive.

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

## Fleet status (2026-10-07, end of day)

| Track | Verdict | Detail |
|---|---|---|
| A (register gap) | **H1 — closed** | Salad beats truth by 2,201 nats even under register-matched reference (vs 2,601 Tocqueville). Register explains ~15%; the LM family is the blocker. |
| B (neural char-LM) | running | numpy char-LSTM training (≤2h); 9-step order under R5 GO. |
| C (word boundary) | **LINE CLOSED** | Four honest nulls, mechanism fully understood (R11): no additive per-word/per-transition statistical term can separate ear-noised truth from adversarial common-morpheme salad — the salad lives inside the model's vocabulary. §6 pilot stood down. Structural successor (dependency-parse/SPS) named, shelved while D lives. |
| D (LM judge) | pilot **PASS 6/6** → **Branch B** → **instrument FAIL** | Experiment 0: 6/6 SLIDE — truth not a local optimum under J; rerank dead. Judge instrument acceptance test: 3/18 medians within ±3 — fresh judges collapse truth AND salad to ~25 ("letter noise"); the pilot's 39–43-pt discrimination does not transfer across instances. R13 adjudication complete: pilot stands as within-operator proof, VOID as gate instrument. Prompt-repair ladder in flight (A: degradation-robust word-listing, B: anchored calibration, C: pairwise forced-choice) — sequential trial by fresh judges; R14 GO on Branch-B spec (R12a pinned) with binding R14e: exactly ONE further substrate attempt (the ladder IS that attempt — pre-registered as such); second failure fires SPS. Stage 2 needs: acceptance PASS + R14 clearance + grep self-check. |

**Answer to the fleet's core question:** it is the likelihood, not the register gap and not the weights. The live attack is the judge-driven funnel (Track D); the neural LM (Track B) is the remaining likelihood repair; the statistical boundary line is exhausted by proof, not by fatigue.

## STANDING DOCTRINE (operator order, 2026-10-07 — overrides any wind-down)
**A null result is not a stop condition.** If a track fails its pilot or gate,
the track DIAGNOSES the failure, REPAIRS the method/prompt/protocol, and
CONTINUES — it does not wind down. "Don't stop if the fleet returns a null
result — tell them to continue."
- Kill CLAIMS, never kill INQUIRY. The red team's KILL/VOID rulings terminate
  claims, not tracks. A killed claim becomes a repair work order.
- Every repair requires: (1) a written diagnosis of WHY the null happened
  (numbers, not narrative); (2) a repaired PREREG (re-registered bars —
  no moving the old bar after seeing the data); (3) red-team sign-off on
  the repair before the re-run. The prompt/method freeze rules still apply.
- Track D (LM-judge reranker) is the operator's personal priority: if its
  pilot fails, the first repair target is the judge PROMPT/PROTOCOL itself —
  find out exactly why the judge can't tell salad from truth (prompt
  wording? score scale? candidate presentation? memorization asymmetry?)
  and repair it rather than shelving the track.

## Fleet refresh — 2026-10-07 ~20:45 CDT (fresh coordinator, session 5ca520bb)
Previous coordinator died on a runtime hiccup after ~7h; mission inherited, workers not.
- **Rung-C clean re-run**: trial runner deployed (single coordinator, isolated dir
  `track-d/rerun-rungC-clean/`, hardening 1–8 confirmed in COORDINATOR-DESIGNATION.md).
  Red-team audit to follow before any verdict. Pre-cleared per R18(H).
- **Track B**: training live, held loss 2.11→2.054 and still declining at upd 8600/ep 4.
  Decision: CONTINUE on the numbers.
- **Workers**: (1) Experiment 0 completion — 5 pending runs; (2) memorization re-probe
  on gate truths (36 calls, pre-unsealing prerequisite); (3) cell-space solver moves
  implementation + smoke test; (4) funnel seed package with current priors
  (13 values incl. 17="fois", 47/79 PROMOTE-grade, 37 tension, 32/19, 00="pour").
- Track A closed (H1). Track C line closed (statistical boundary exhausted by proof).
  SPS remains shelved while D lives — NOT built speculatively.

## 2026-10-07 ~20:50 CDT — rung-C judges commissioned; memorization probe parked
- Rung-C clean re-run: build phase complete (prompt pinned d907c592, 84 fresh
  labels zero-overlap vs 138 used, 36 binding + 6 by-seed diagnostic pairs,
  key sealed, pre-judge tripwire clear). 3 fresh judges commissioned by the
  single coordinator. Scoring + red-team audit follow on judge completion.
- Memorization re-probe (36 calls): BLOCKED 0/36, INCONCLUSIVE. No probe inputs
  exist — only the key-holding Runner/coordinator may construct gate-truth
  paraphrases per R12e/R14f; a track worker cannot. Parked until (a) rung-C
  instrument acceptance resolves the judge-substrate question and (b) the
  key-holder constructs the blind paraphrase package. Pre-unsealing prerequisite
  remains unsatisfied; gate stays sealed regardless.

## 2026-10-07 ~20:52 CDT — cell-space moves verified; funnel re-dispatched
- Cell-space solver moves: already implemented in track-d/solver-cell/solver.py
  (sibling worker); audited spec-compliant (move distribution exact, block
  dropped, pins hard, J untouched); --self-test PASS (delta scoring exact to
  1e-10); smoke test on 184101 PASS (5k iters, +3,550.6 nat margin over random).
  NOTE: experiment_0.py imports the FROZEN solver, not solver-cell/ — the
  running Experiment-0 batch tests old moves per its pre-registration; repoint
  decision deferred to post-run analysis.
- Funnel seed package: first worker returned silently with no artifacts;
  re-dispatched with explicit end-to-end verification requirement.

## 2026-10-07 ~20:53 CDT — Experiment 0 closed (was already complete)
- Experiment 0: the "5 pending runs" premise was stale — all 6 runs already
  complete (experiment0.json/log, EXIT=0), verified line-by-line + reproducibility
  spot-check PASS (184106 byte-identical re-run). 6/6 SLIDE, 0/6 STAY → Branch B
  binding. No new runs executed (deterministic; re-run would overwrite).
  Runner config documented: frozen group-space runner (chg1/swap/poly/chg2/block),
  NOT the cell-space fork — basin probe under cell-space moves remains an open
  follow-up, not a pre-registration violation to pursue unilaterally.

## 2026-10-07 ~20:56 CDT — funnel seed package built
- track-d/funnel_seeds.py + funnel/seeds.json (200: 100 RND + 60 LEX + 40 CRB)
  + funnel/priors-manifest.json (21 priors). Validation PASS: 7 GT pins in
  200/200, 4 split sets exclusive, 67 never collapsed, alias cap 5 respected,
  deterministic (double-run byte-identical). 9 ambiguous encodings documented
  with resolutions. R5005 untouched, gate sealed. Ready for the funnel generator.

## 2026-10-08 ~01:56 UTC — RUNG C PASSES (clean re-run)
- Mechanical: 36/36 binding pairs truth-unanimous 3–0 (bar ≥35/36); 126/126 verified.
- Red-team audit: ADMISSIBLE (9/9). Confidence-uniformity concern assessed —
  judge 3's passes 2–3 were copies; choice data robust under strictest weighting.
- Documentation gap closed: COORDINATOR-ATTESTATION.md (single coordinator
  commissioned all 3 judges; fresh, brief-only).
- Ladder §4: strike one CLEARED, v3C instrument ACCEPTED, strike two not
  recorded, SPS trigger NOT met.
- Step-4 clearance re-requested: redteam/STEP4-CLEARANCE-REQUEST.md (Branch-B
  funnel on original instances; R5005 + gate instances stay sealed).
- Memorization re-probe still parked (needs key-holder's blind paraphrase package).
