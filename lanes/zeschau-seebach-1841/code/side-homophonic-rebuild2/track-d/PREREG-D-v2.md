# TRACK-D PREREG v2 — council-revision (funnel + judge-in-the-loop)

**Track:** D (LM-judge, solver-rebuild round-2 fleet).
**Date:** 2026-10-07.
**Status:** PRE-REGISTERED (revision). The v1 PREREG (plain rerank: gate
anneal + top-20×3-pass rerank, R8 clearance) is **SUPERSEDED as a pipeline
ruling** — it is moot; the v2 funnel below replaces it. The v1 PILOT
(6/6, margins 39–43, clean probe) and R8's verification findings (R8a–d)
stand and carry over. Nothing here touches R5005.
**Author:** track-d revision agent (TRACK D REVISION, council architecture).

## 0. What changed and why (the architectural argument, registered)

The v1 pilot proved the judge **discriminates** truth from salad
(39–43 pts), not that the annealer **generates** truth-adjacent
candidates. Under the rebuilt objective J, truth loses to salad by
2,601 nats — so every restart converges to a salad basin, and a rerank
only picks the best salad. The judge must influence **which regions get
explored**. Two changes follow:

1. **Judge-in-the-loop:** bounded funnel (Stage 2: 5k-iter climbs) +
   judge triage (Stage 3) + judge-guided iterated local search
   (Stage 4) replace the plain rerank.
2. **Cell-space moves:** the annealer moved one group at a time in
   89-dim group space while the objective lives in ~30-dim cell space;
   the move set is reparameterized to alias sets (reassign/swap/
   split/merge) with single-group moves kept for fine-tuning.

## 1. Experiment 0 — the basin probe (gates the architecture)

Run FIRST, before any gate work. On the 6 ORIGINAL instances
(184101–184106; truth keys opened in round-1 forensics — NO fresh-seal
contact): initialize the frozen rebuild annealer AT the sealed truth
key, run 40k iters under the rebuilt J (Track-D §5 gate config,
`experiment_0.py`), and classify:

- **STAY:** final key within Hamming distance ≤ 5 of truth in group space
- **SLIDE:** final J > J(truth) + 500 nats AND primary recovery < 0.10
- **DRIFT:** neither (report-only)

**Branch A** — truth locally optimal on ≥4/6 (STAY count ≥ 4):
full §3 funnel as designed below.
**Branch B** — truth locally optimal on <4/6 (SLIDE/DRIFT on ≥3/6):
the rerank/triage-as-designed path is DEAD. §3 Stage 2 (J-climbs) is
dropped; Stage 4 (judge-guided ILS) is promoted to the PRIMARY loop,
seeded from lexicon starts rather than J-climb endpoints. The SPS
fallback (council arch §7) is flagged as the escalation candidate;
a one-paragraph trigger assessment is filed with the gate report.

**Results (filled 2026-10-07, `experiment0.json`, script
`experiment_0.py` — EXIT=0):**

| seed | J(truth) | final J (from truth start) | ΔJ (nats) | Hamming (groups/nonpin) | primary recovery | verdict |
|---|---|---|---|---|---|---|
| 184101 | −4,953.3 | −2,514.0 | +2,439.3 | 86 / 86 | 0.034 | SLIDE |
| 184102 | −4,925.5 | −2,458.7 | +2,466.8 | 87 / 87 | 0.022 | SLIDE |
| 184103 | −5,076.2 | −2,357.3 | +2,718.9 | 88 / 88 | 0.011 | SLIDE |
| 184104 | −5,278.4 | −2,556.5 | +2,721.8 | 88 / 88 | 0.011 | SLIDE |
| 184105 | −5,293.6 | −2,649.2 | +2,644.4 | 89 / 89 | 0.000 | SLIDE |
| 184106 | −5,046.0 | −2,671.2 | +2,374.7 | 89 / 89 | 0.000 | SLIDE |

**6/6 SLIDE, 0/6 STAY → BRANCH B.** Truth is not a local optimum under
J on any instance: initialized AT the truth key, the annealer abandons
it every time, landing 2,375–2,722 nats above J(truth) — within the
salad class (compare the recorded 2,601-nat salad>truth margin) — at
chance-or-below primary recovery (0.000–0.034 vs 1/89=0.0112 chance).
Consequences per the branch rule: the rerank/triage-as-designed path
(§3 Stages 2–3 as written) is DEAD; no restart-based method under J can
reach truth; the gate pipeline is re-scoped to **judge-driven ILS as
the primary loop seeded from lexicon starts** (Branch-A §3 Stage 2
dropped, Stage 4 promoted), with the SPS fallback (§9) as the
escalation candidate. A red-team review of this branch call is
requested before any gate work.

## 2. Instrument: the cell-space solver fork

`track-d/solver-cell/solver.py` — fork of
`code/side-homophonic-rebuild/solver/solver.py` (md5 `aac6f260…` at
fork time; the original dir is UNDISTURBED). Move distribution,
pre-registered (council arch §4):

| move | p | definition |
|---|---|---|
| chg1 | 0.30 | single-group reassign (as before) |
| swap | 0.10 | two groups swap v1 (as before) |
| poly | 0.10 | secondary toggle (as before) |
| alias-reassign | 0.30 | pick cell c in use, new cell c′; ALL non-pin groups with v1==c → c′ atomically |
| cell-swap | 0.10 | swap the group-sets of cells c1, c2 |
| alias-split | ⊂0.10 | move a proper nonempty subset of c's groups to a new cell |
| alias-merge | ⊂0.10 | all of c2's non-pin groups → c1 |

`block` (contact-neighborhood) is DROPPED — contact ≠ alias — and
`chg2` is dropped (subsumed by chg1). Multi-group touches ride the
existing `_region`/`snapshot`/`revert` machinery (~40 lines of new
code). Pins are excluded from every cell move's touched set; a move
that would touch nothing returns 0.0/None (rejected, not applied).

**Sanity check (one original control instance, 184101):** 3k-iter
anneal with cell-space moves — ran clean, J computed and climbed
(−8,630.6 → −3,456.7), accept rate 0.264, all four cell moves fire
with multi-group touches (1–6 groups/move). Functional pass, not a
quality bar.

## 3. The funnel (Branch A design)

INPUT per instance: ct pairs (1,846), crib JSON (7 pins), Tocqueville LM,
296-cell inventory. OUTPUT: one 96-group → cell key. PINS: 7 GT groups
fixed forever. No `SYNTHETIC-key-18420*.json`, `sealed-pclasses.json`,
or fresh plaintext is ever read (pre-run grep self-check, logged).

**STAGE 1 — diverse seeding (200 seeds):**
100 random (pins fixed, rest uniform over inventory) +
60 lexicon-seeded (high-frequency windows → groups assigned to cells
forming real inventory words covering the window; remainder random) +
40 crib-extended (propagate pins via bigram constraints; remainder
random). Seed RNG: `random.Random(2000 + 100*inst_idx + i)`; all logged.

**STAGE 2 — cheap climb:** each seed → 5k iters of the cell-space
solver under J (`iters=5000`, t0/tmin from config.json).
200 diverse local optima → `candidates[]`.

**STAGE 3 — judge triage:** 200 × 1 pass (blind labels, fresh random
order) → top-40 → 2 more passes → per-candidate median-of-3 →
top-5 parents. Judge calls: 200 + 80 = **280**.

**STAGE 4 — judge-guided ILS:** 3 rounds × 5 parents × 10 neighbors
(1 pass each, blind); neighbors = 1–3 cell-space mutations of the
parent (alias-reassign / cell-swap / split / merge / chg1).
pool = parents + neighbors; parents = argtop5 of median scores
(medians kept where available). Final: top-10 overall × 2 more
passes → median-of-3; WINNER = argmax. Tie-break: higher median,
then higher J, then lower candidate index. Judge calls: 150 + 20 = **170**.

**STAGE 5 — gate scoring:** WINNER's 96-group mapping → Runner scores
PRIMARY/SECONDARY per CONTROL-DESIGN.md §4.

**Judge-call budget: 280 + 170 = 450/instance → 2,700 for the 6-instance
gate.** Annealer compute ≈ 37 min/instance (200×5k, parallelizable
across instances). R5005 (single instance): same per-instance budget.

## 4. Judge-call protocol (carries R7/R8, extended for volume)

Frozen prompt sha256 `390a1ec0bf1aa9e0e495a5fe98e65107c41025c954cd11b68d1931816c08e21d`
(DO NOT MODIFY — any prompt change = re-registration + new pilot, not
the operator's call). Candidates = raw `join(pcell)` decode strings,
unmodified (spaceless, ear-noise spellings intact). Blind 8-hex labels;
label→(instance, stage) map sealed until logging completes. Mechanical
first-line-int extraction; EXTRACTION-FAILED logged, excluded, never
re-queried. Every call logged to `judge_log.jsonl`
(timestamp, label, pass_no, prompt_sha256, raw_response,
extracted_score).

**Aggregation rule (pre-registered):** per-candidate score = median of
its valid queries; fewer than 2 valid → VOID (reported, not claimed).
Stage-3 triage: 1 pass for all 200; median-of-3 only for the top-40.
Stage-4 ILS rounds: 1 pass per neighbor (fresh candidate each round, no
history to stabilize); median-of-3 only for the final top-10. Parents
carry their medians forward; neighbors are ranked on single-pass scores
within their round — the round structure, not the median, is the
variance control, and final selection always rests on median-of-3.

**Variance justification (against R7's 3-query pilot protocol):** the
pilot showed cross-pass range ≤ 2 pts per candidate (18/18 candidates),
i.e. single-pass scores are stable to ±1. Triage only needs to keep the
truth-adjacent candidates inside the top-40 — a 40-wide net over
≤2-pt noise — and every selection that matters (parents→finalists→
winner) is median-of-3. A top-40 candidate mis-ranked by 1 pass can
re-enter via ILS parents; a top-10 mis-rank is caught by the final
median-of-3. The 1-pass stages are throughput; the median-of-3 stages
are the gates.

## 5. The judge instrument (the #1 infra prerequisite — MUST exist before the gate)

2,700 hand calls are infeasible (the pilot's 54 took the operator ~3
min/call-batch; scale ×50). **The gate does not run without an
automated judge instrument.** Two acceptable substrates:

- **(a) Subagent-judges:** fresh LM instances per call, frozen prompt
  sha256-pinned and asserted at startup (abort on mismatch), blind
  labels, fresh random order per pass, median-of-3 where required,
  full `judge_log.jsonl` per Track D §2. The french-blitz pattern
  proves the mechanism works.
- **(b) Local/API LM endpoint:** any model endpoint the operator can
  hit; same protocol requirements (frozen prompt, blind labels,
  median-of-3, full logging). Substrate MUST NOT be fine-tuned on Les
  Misérables or on any truth-plaintext-adjacent text (same leakage
  standard as R0/R5).

**Acceptance test (binding, runs BEFORE the gate):** the instrument
must reproduce the pilot medians within ±3 pts on the 18 frozen pilot
candidates (6 truth / 6 salad / 6 paraphrase in `candidates.json`).
Truth band ~62, salad band ~20, paraphrase band ~91; margins mT−mS ≥ 30
on all 6. Failure → the instrument is not the judge; the gate does not
run. Cost: 54 calls, same protocol as the v1 pilot.

## 6. Additive controls (bars do NOT move)

1. **Memorization probe on GATE truths (non-negotiable, before
   unsealing):** re-run the v1 §4 probe construction on the 6 fresh
   instances' truth decodes — 6 fresh paraphrases + 36 judge calls
   (6 candidates × ... recorded under the §4 protocol: truth vs
   paraphrase, blind, median-of-3). Void rule unchanged: mT−mP ≥ 15
   anywhere → gate VOID. The v1 probe covered the OLD slices; the
   gate's slices are FRESH. (12 candidates × 3 passes = 36 calls.)
2. **Diplomatic-plaintext secondary gate:** Track A's 2
   register-matched instances (when built) run the same funnel as a
   secondary gate. The 6 Les-Mis instances stay the PRIMARY gate
   (comparability). Require the primary only; *believe* the secondary —
   pass Les-Mis + fail diplomatic = the solver won't transfer to
   R5005; report both.
3. **Noise-mismatch ablation (report-only):** 2 instances re-generated
   with 2× ear-noise knobs; run the funnel; report degradation vs the
   primary gate. The Frenchman's H-split finding says the real
   encipherer over-splits beyond the generator's knobs — a cliff here
   predicts R5005 failure, graceful degradation predicts robustness.
4. **q_cycle=0 rhythm-crutch check:** the existing ablation set
   (184213–184218) stands; any solver that collapses on the scrubbed
   set is leaning on rotation, not French (pre-registered, not moved).
5. **Substitution fallback clause (R8b — registered in advance, not
   improvised):** if any specified candidate source is empty or
   otherwise unfulfillable at gate time (as `frozen-ctl-184105/` and
   `frozen-ctl-184106/` were at pilot time), the track may substitute
   ONLY an instrument-identical source: same solver code, same config,
   same score-part signature, verified degenerate-class (judge-band
   consistent), taken as-is with provenance logged and the deviation
   disclosed to the red team BEFORE downstream numbers are cited. No
   re-rolling, no cherry-picking, no post-hoc invention. (Pilot
   precedent: `run3-18410{5,6}`, accepted under R8.)

**Terminology note (R8b):** round-2 frozen salads are **n_poly≈59–61
polyphonic tilings** — the "npoly=0" figure is a round-1 artifact and is
NOT cited in v2 prose or numbers.

## 7. Gate bars (unchanged from v1 PREREG §6 — NOT moved)

Per-instance winning key (96-group mapping) → `gate_answers.json`;
Runner scores against sealed keys per CONTROL-DESIGN.md §4:

| metric | definition | BAR |
|---|---|---|
| PRIMARY | exact recovery of planted PRIMARY cell, 89 non-anchor groups | mean ≥ 0.20, min ≥ 0.10 |
| SECONDARY | decode accuracy, all 1,846 pairs (anchors given) | mean ≥ 0.30, min ≥ 0.22 |

PASS = all four inequalities. Anything else = FAIL: stop, do not
touch R5005, report per-instance numbers. A gate PASS does NOT
authorize an R5005 run — that authorization belongs to the
parent/coordinator. Branch B (if selected) carries the same bars; the
only change is the pipeline that produces the winning key.

## 8. R5005 success criteria (council arch §6 — pre-registered BEFORE any R5005 run)

"Solved" requires ALL FIVE; nothing less ships:

1. **Board consistency.** Winning key, restricted to board groups,
   matches ≥ 11 of 12 board values (7 GT + 5 provisional), every
   islet-registry rule (10 islets) satisfied at its registered
   windows. (One provisional may fall only with a red-team ruling
   citing the contradicting window.)
2. **Judge bar.** Judge-score the R5005 decode with the frozen gate
   prompt (3 passes, median). Bar: ≥ (mean gate-winning median − 2σ),
   and in any case ≥ 55 (pilot truths ~62; salads ~20). Below bar =
   not solved, full stop.
3. **Topic check (the anti-salad tripwire).** The decode must contain
   ≥3 independently verifiable period facts checkable against the
   period corpus (named entities, date references, "par ce que"-class
   formulae in grammatical frames) — each cited to corpus + window. A
   fluent-but-wrong decode cannot name the right Pasha. This is the
   strongest criterion — salad can't do it.
4. **Independent reproduction.** A separate agent, given ONLY the
   winning key (never the solver), reproduces the decode byte-exact
   with independent code and confirms it reads as coherent 1841
   diplomatic French.
5. **Perturbation stability.** Swap 5 random non-pin groups in the
   winning key; the decode's topic content (criterion 3's facts) must
   survive in ≥ 4 of 5 perturbations. A real solution is robust; a
   salad shatters.

## 9. SPS fallback trigger assessment (one paragraph, per Branch-B contingency)

If the judge instrument (§5) proves infeasible OR the gate fails
despite a passing acceptance test, escalate to the Segment-Parse-Score
fallback (council arch §7): a deterministic structural scorer —
by-ear normalize → DP word segmentation over a diplomatic-French
lexicon → UD dependency parse → α·wordLM + β·parse_confidence +
γ·coverage − δ·OOV_rate — that kills the salad structurally (no words,
no syntax) instead of statistically. SPS slots into §3's Stages 3–4
as a drop-in judge replacement, 10–100× cheaper than an LM call and
deterministic. Trigger condition: (a) gate FAIL with judge-transfer
suspected (pilot passed, acceptance passed, winners still salad-class),
or (b) no viable judge instrument after two substrate attempts.
Do NOT build SPS speculatively while Track D's funnel is alive.

## 10. Hard constraints (all steps, no exceptions)

1. **NO R5005 contact.** A grep for `r5005|R5005|ct_R5005` over
   `track-d/` is logged before the instrument acceptance test and
   before the gate; any data hit = self-KILL of the run.
2. Control/diagnostic only. Nothing in this track touches real data.
3. The prompt is frozen at sha256 `390a1ec0…c08e21d`. Any change =
   re-registration + new pilot (not the operator's call).
4. Deterministic seeds everywhere except the judge instrument itself
   (controlled per §4). All seeds logged.
5. No cherry-picking: exactly the pre-registered query counts per
   candidate per stage, medians taken, all raw responses logged,
   extraction failures logged not hidden.
6. Fresh seals (184201–184204, 184206, 184207) are read ONLY as ct
   pairs + crib JSON — NEVER their keys, pclasses, or plaintexts —
   until Runner scoring. R5005 stays sealed and untouched.

## 11. Red-team lineage (carried forward)

- R6/R7/R8 (frozen prompt, blind labels, mechanical extraction,
  full logging, no R5005 contact) carry over unchanged.
- R8's plain-rerank step-4 clearance is SUPERSEDED by this revision
  as a pipeline ruling (moot); its verification findings stand:
  pilot 6/6 verified byte-exact (R8a–d), salad substitution for
  184105/184106 accepted under necessity (R8b), probe clean with
  bounded residual (R7b/R8c).
- R8a: the PILOT-REPORT per-query table's seed column has been fixed
  (rebuilt mechanically from `label_map.json`); medians/margins
  (39–43) unchanged — cite the corrected table, not the original.
- R8b: the v1 PREREG §3 "no substitution" clause is replaced by the
  §6(5) fallback clause above, registered in advance.

## 12. Outcome map

- Experiment 0 → Branch A (≥4/6 STAY): build the §5 instrument →
  acceptance test → memorization probe on gate truths (36 calls) →
  run §3 funnel on the 6 FRESH instances → §7 scoring.
- Experiment 0 → Branch B (<4/6 STAY): Stage 2 dropped; §3 Stage 4
  promoted to primary loop seeded from lexicon starts; file the §9
  trigger assessment; red-team review before the gate runs.
- Gate PASS → report; R5005 authorization is the parent's call.
- Gate FAIL → stop; report per-instance numbers incl. where it failed
  (coverage? judge transfer? ILS stuck?); do not touch R5005.
