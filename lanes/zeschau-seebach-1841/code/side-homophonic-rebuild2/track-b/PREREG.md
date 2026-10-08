# PREREG — Track B: neural character LM vs the Goodhart failure

**Status:** SUBMITTED for red-team review from disk (per `../redteam/RULINGS.md` R0;
no `subagent.send` exists at this depth). **No training, no scoring, no model
code has been run or written.** This directory contains only this file at
submission time. No scored comparison will run before a dated red-team GO in
`../redteam/RULINGS.md`.

**Track:** B (neural character LM replacing/augmenting the Tocqueville char-5-gram).
**Date:** 2026-10-07. **Author:** track-b subagent (depth 2/2, can_spawn=no).

## 0. Objective and hypothesis

The rebuilt solver's likelihood (Tocqueville char-5-gram S_char + lexicon
S_word) ranks adversarial morpheme-salad 2,601 nats above the planted truth on
seed 184101 (verifier: `side-homophonic-rebuild/verifier/CLOSING-VERIFICATION.md`).
The verifier proved no reweighting in the 5-gram+lexicon term family makes
truth the robust argmax — the failure is in the likelihood, not the weights.

**Hypothesis under test:** a neural character LM with longer effective context
than the 5-gram (full left-history LSTM state vs 4-char context), trained on
era/register-matched French (1841 diplomatic + 1835–40 formal prose), assigns
higher likelihood to the planted truth decode than to morpheme-salad decodes,
with a margin that survives adversarial re-tiling.

**This PREREG tests the likelihood term only** (S_char replacement), not a full
solver run. No annealer is executed in this track.

## 1. Decision rule (pre-registered, numeric, binary NOT-GO)

Let `S_neural(D)` = the neural-LM score of decode D (definition §5), and

- `M_frozen  = S_neural(truth_184101) − S_neural(frozen_salad_184101)`
- `M_adapted = S_neural(truth_184101) − S_neural(adapted_salad_184101)`

Reference (verifier, current objective): frozen salad total **−2,352.3**,
truth total −4,953.3.

| Verdict | Condition |
|---|---|
| **SUCCESS** | `M_frozen ≥ +1,000` **and** `M_adapted ≥ +300` **and** instrument gate (§7) passes **and** adapted salad passes the strawman check (§6). Claim: the neural likelihood fixes the Goodhart failure on 184101. |
| **FAIL** | Instrument gate passes **and** adapted salad is valid (not strawman) **and** (`M_frozen < 0` **or** `M_adapted < 0`). Claim: a trained neural char LM does **not** fix the likelihood — the failure is deeper than context width. |
| **INCONCLUSIVE** | Any of: instrument gate fails (weak instrument — no FAIL claim permitted); adapted salad is a strawman (voids the (b) comparison); margins positive-but-below-bar; training hits the 2h wall with no usable signal (NaN / no held-out eval). Below-bar-but-positive ⇒ **NO-GO** on the hypothesis. |

**Binary NOT-GO rule (red-team requirement):** below either bar, no claim is
made that the neural LM fixes anything. Sub-bar-but-positive means NO-GO;
the only path to a new claim is re-registration — there is no third option.
INCONCLUSIVE is a finding about the experiment, not a soft SUCCESS.

**Full-J substitution (only if SUCCESS):** report
`J_neural = S_neural + S_word + S_potts − 50·n_poly − 5·S_conc`
(verifier's J; S_soft excluded per the `--no-soft` pilot parity) for
truth / frozen / adapted, where the non-LM terms are computed by
`verifier/rescore.py` on the neural-E-step pcell (§5). Question answered:
does truth beat salad under the full J with the neural LM substituted?

## 2. Architecture (evidence-based choice; torch absent)

`python3 -c "import torch"` → **ModuleNotFoundError** (no torch on this VM).
Per the task brief the fallback is a from-scratch numpy LSTM or a
neural n-gram. Measured on this VM (2 CPU, numpy 1.26.4):

| model | config | measured fwd+bwd |
|---|---|---|
| numpy char-LSTM | h=128, T=100, batch=64, float64 | **2.0k chars/s** |
| numpy neural n-gram MLP | ctx=10, emb=32, hid=128, batch=8192, float32 | **1.5k chars/s** |

**Chosen: from-scratch numpy char-LSTM**, single layer:
- `h=96`, one-hot input over the 30-symbol projected alphabet (fixed —
  `solver/lm_ref/lm.json` meta; asserted at train time, fail-loud on
  violation), float32.
- Gates: `[i,f,g,o] = σ/σ/tanh/σ(W_xh·x + W_hh·h + b)` (forget bias init 1.0),
  `c = f⊙c_prev + i⊙g`, `h = o⊙tanh(c)`; output softmax `W_hy·h + b_y` over 30.
  ≈ 52k parameters. Xavier-uniform init, master seed **20261007**.
- BPTT `T=64`, batch `B=96` parallel streams, LSTM state carried across
  consecutive batches within an epoch (detached), reset at epoch boundary.
- Adam (lr=2e-3, β1=0.9, β2=0.999, eps=1e-8), global-norm clip 5.0; halve LR
  on held-out plateau (patience 1 eval), floor 2e-4.

**Throughput estimate (anchored, not guessed):** scaling the measured
2.0k chars/s by param ratio 0.60 and float32 ≈1.4× gives ≈ **4–5k chars/s**,
i.e. ≈ 30–36M chars in the 2h budget ≈ **2.5–3 epochs** over the ≈11.6M-char
projected stream (§4). Actual wall-time and chars consumed are logged; the
estimate does not gate anything.

**Correctness gate (before any training):** finite-difference gradient check
on a toy (H=8, T=5, B=2), central differences eps=1e-5; require max relative
error < 1e-4 on all parameter groups, else **halt — no training, report
blocked**. (Addresses the from-scratch-numpy correctness risk explicitly.)

**Why not the MLP:** slower measured throughput on this VM *and* fixed
10-char context; the LSTM tests the stronger "longer effective context"
hypothesis (streaming full-history state). The MLP remains the named
fallback if the LSTM gradient check fails.

## 3. Training manifest (file-by-file; Les-Mis-free by measurement)

Exclusion rule: **no Les Mis anywhere** — not in files, weights, or
validation splits. Les Mis scan rule (pre-registered, executed 2026-10-07):
normalize (NFD accent-strip, lowercase, `[a-z]+` words), build the set of
word-8-grams of `data/gutenberg-17489-miserables1.txt` **body** (Gutenberg
boilerplate excluded via `*** START/END ***` markers, exactly as
`build_lm.py` does), count hits on each candidate file's **trainable body**.
RdM reprints of Les Mis would count as Les Mis — chronology rules them out
(all corpus texts predate the 1862 novel), and every hit is individually
listed below for audit.

| # | file | bytes | sha256 | body words | LesMis-8gram hits | provenance |
|---|---|---|---|---|---|---|
| 1 | `code/side-period/corpus/guizot-memoires-t5-t6.txt` | 2,043,767 | `3b6f4c1e…a904a871` | 298,765 | 3 | `corpus/PROVENANCE.md` — Guizot, *Mémoires pour servir…*, publ. pre-1923, IA OCR |
| 2 | `code/side-period/corpus/nesselrode-v7.txt` | 533,520 | `6879f818…b784617d` | 79,026 | 1 | PROVENANCE.md — Nesselrode *Lettres et papiers* v7, 1904–12, IA OCR |
| 3 | `code/side-period/corpus/nesselrode-v8.txt` | 627,848 | `699d5af…f8a3301ca` | 92,677 | 1 | as above, v8 (full 1841 run) |
| 4 | `code/side-period/corpus/nesselrode-v9.txt` | 515,743 | `078a771c…1d5fd1997` | 85,338 | 1 | as above, v9 |
| 5 | `code/side-period/corpus/nesselrode-v10.txt` | 569,508 | `74dc194f…7fed1a5bd` | 82,495 | 0 | as above, v10 |
| 6 | `code/side-period/corpus/revue-deux-mondes-1841-q1.txt` | 3,087,127 | `6bb18f45…272d6bb3b` | 459,176 | 2 | PROVENANCE.md — RdM 1841 Q1, IA OCR |
| 7 | `code/side-period/corpus/revue-deux-mondes-1841-q2.txt` | 3,037,263 | `8f2b8c93…a3e5fe9ea` | 449,677 | 1 | RdM 1841 Q2 |
| 8 | `code/side-period/corpus/revue-deux-mondes-1841-q3.txt` | 3,129,322 | `14b46d9d…5e9806ea2` | 463,283 | 0 | RdM 1841 Q3 |
| 9 | `code/side-period/corpus/revue-deux-mondes-1841-q4.txt` | 3,244,434 | `b7204a2c…f4267d0dc` | 478,398 | 0 | RdM 1841 Q4 |
| 10 | `code/side-period/corpus/metternich-papiere-v4.txt` | 1,511,320 | `12416abf…8edbf89c6` | 216,832 | 1 | PROVENANCE.md — Metternich *Papiere* v4 (French diplomatic correspondence body; verified by sampling, FR-dominant 22.3% stopwords) |
| 11 | `code/side-period/corpus/metternich-papiere-v6.txt` | 1,755,063 | `12b8379d…0dea4a4f2` | 250,490 | 4 | as above, v6 |
| 12 | `code/side-period/corpus/talleyrand-memoires-v1.txt` | 954,364 | `1144d6e2…8d4187e4c` | 156,400 | 0 | PROVENANCE.md — Talleyrand *Mémoires* v1 |
| 13 | `data/gutenberg-30513-tocqueville-t1.txt` | 626,573 | `fafebe4f…76154aeaa` | 96,540 | 0 | `data/PROVENANCE-tocqueville.txt`, `data/SHA256SUMS.txt` — Tocqueville 1835 |
| 14 | `data/gutenberg-30514-tocqueville-t2.txt` | 745,227 | `20e46d72…21dbe33ee` | 118,321 | 0 | as above — Tocqueville 1840 |

(Full 64-hex sha256 recorded in `manifest.json` at train time; prefixes above
are the first/last 8 for readability.)

**Explicit exclusions (with measured reason):**
- `data/gutenberg-17489-miserables1.txt` (Les Mis) — **never trained on**;
  the synthetic truth plaintexts are Les Mis slices, and training on them
  would be in-distribution cheating against the register-gap design.
- `code/side-period/corpus/levant-correspondence-1841-p3.txt` — **excluded**:
  language assay (stopword ratios) gives EN 30.0% / FR 8.0% — English-dominant
  British parliamentary papers. Projecting English through French phonetics
  would corrupt the French char model. The task brief's "ALL French" premise
  is false for this file; measured, documented, excluded.
- `code/side-period/corpus/{guizot-memoires-t1..t3,pozzo-di-borgo,adb-zeschau,allgemeine-zeitung-*}` —
  not in the brief's manifest; not used (the allgemeine-zeitung files are
  German in any case).

**The 13 Les-Mis-8-gram hits are NOT Les Mis content** (all pre-1862 texts;
listed verbatim for red-team audit — generic French idioms, longest run 10
words):
`tant qu on n a pas vu de (ses propres yeux)` ×2 (guizot),
`sur ce qu il y avait a faire` (guizot), `tout ce qu il y a de plus` ×5
(nesselrode-v7, v9; RdM-q1; metternich-v6 ×2),
`ce que je puis dire c est que` (RdM-q1), `quoi qu il en soit il y a` (RdM-q2),
`de ce qu il y a de plus` (metternich-v4),
`ce qui est hors de doute c est que (la)` ×3 (metternich-v6, one 10-word run).
**Overlap with truth-slice content: 0** — no hit is distinctive Les Mis
prose; all are stock idioms Hugo also used. Verdict: manifest is Les-Mis-free;
no Les Mis enters files, weights, or validation splits. (If the red team
rules any hit disqualifying, the track self-KILLs rather than argues.)

**Cross-track contamination (Track A):** Track A's 2 new instances use
diplomatic-corpus slices as truth plaintext. Before training, this track
reads `track-a/PREREG.md` if present and **excludes any (file, line-span) it
claims** from the train stream (logged). If absent at train time: the full
(file, line-range) spans consumed are logged in `manifest.json`; the overlap
check is re-run before scoring; **overlap > 0 ⇒ run VOID**, retrain without
the spans (within remaining budget) or self-report KILL. (Note: this track
scores only 184101 — Les Mis truth — so Track-A slices cannot leak into this
track's verdict; the mechanism is prophylactic for model reuse.)

## 4. Data pipeline (parity with the 5-gram build)

1. Body extraction: Gutenberg files → between `*** START OF` / `*** END OF`
   markers (as `build_lm.py`); OCR files → whole file. (Measured: the
   PG-boilerplate scan artifact above is exactly why.)
2. Tokenize: `WORD_RE = [a-zàâäéèêëîïôöùûüÿçœæ]+` on lowercased text
   (byte-identical regex to `code/side-homophonic/solver/build_lm.py:54`).
3. Project every word with the library `phonetics.project`
   (byte-cross-checked vs the verifier's reimplementation on 3,845 strings;
   zero mismatches — `verifier/rescore.py`).
4. Concatenate projected words into a **spaceless stream** (no boundary
   marker — parity with the 5-gram's training stream; boundary-awareness is
   Track C's experiment, not this one's).
5. Shuffle **lines** with `numpy.random.default_rng(20261007)`; held-out =
   lines whose `(file_index, line_index)` hash mod 50 == 0 (≈2%), fixed
   **before** shuffling. Train stream = the rest, in shuffled order, LSTM
   state carried continuously, reset at epoch boundary.
6. Per-file projected-char counts and the held-out char count are logged in
   `manifest.json` (estimated total ≈ 11.6M projected chars).

## 5. Scoring protocol (the LM term swap)

**`F_neural` (replaces `CharLM.F`):** process the decode's projected pairs
left-to-right with carried LSTM state (`state_0 = 0`, the analogue of the
5-gram's `^` start). For pair `t` with projected value `v`:
`F_t = (Σ_{ch ∈ v} log p(ch | state)) / len(v)`, then advance state through
`v`. **`S_neural(D) = Σ_t F_t`** — the per-pair/per-char rate of REBUILD.md
§4, so decodes of different lengths compare fairly. Identical code path for
all three decodes ("identical decode tokenization" per RULINGS).

**Neural E-step** (needed only for truth: 6 secondaries; both salads have
n_poly=0): mirrors `verifier/rescore.py::_estep` — 10-sweep fixpoint, but the
choice score for reading `o ∈ {o1, o2}` at occurrence `t` is
`(Σ_{ch ∈ o} log p(ch | state_left)) / len(o) + log(w)` vs `+ log(1−w)`,
with `state_left` = LSTM state after the current choices for pairs `< t`
(left-to-right sweeps; unidirectional LM — left context only, noted as the
principled adaptation of the 5-gram's two-sided window). w2 init 0.5 for
truth's secondaries (verifier parity), recomputed post-fixpoint as
`(n2+1)/(occ+2)` (verifier parity; affects choices only, not the final sum).

**The three decodes (frozen pre-sign-off; scored only post-sign-off):**
- **Truth:** `verifier.load_truth('184101')` (sealed 184101 key; forensics-class
  — opened in round 1 per CLOSING-VERIFICATION caveats). Sanity gate: my
  5-gram E-step on this key must reproduce
  `track-c/decodes.json['truth']['text']` byte-exact before the neural swap;
  mismatch ⇒ halt.
- **Frozen salad:** the `npoly=0` restart of
  `pilot/rebuild-pilot-final/result.json` (sha256
  `d4e2dd6f…122dc511ab7f1b70b`) with the best recorded total; gate: its
  verifier-J parts must reproduce CLOSING-VERIFICATION §2
  (S_char=−3,325.7, S_word=+1,021.9, total=−2,352.3) within 0.1 nats;
  mismatch ⇒ halt.
- **Adapted salad:** constructed per §6, frozen to `adapted_salad.json`
  (assignment + sha256 + verification checklist) **before** neural scoring.

## 6. Adapted-salad construction (the adversary; T1 threat model)

The adapted salad is optimized under the **current** objective — the adversary
the verifier's proof contemplated (non-lexicon morphemes, all-distinct,
n_poly=0, all achievable from the inventory). Steps (all post-sign-off):

1. **Pool:** `load_inventory('crib', pins_184101, {}, lex_wt)` → **296 items
   (verified 2026-10-07)** → projected forms → keep non-empty forms **not**
   in the 3,546-word `lm_ref` lexicon → **189 distinct non-lexicon forms
   (verified)** → drop any equal to a pin's projected form.
2. **Assignment:** 89 free groups (96 − 7 hard pins; pins fixed — any valid key
   satisfies them). Deterministic first-improvement local search maximizing
   verifier-J (`S_char + S_word + S_potts − 5·S_conc`; `S_conc = 0` by
   all-distinct construction; `n_poly = 0`): greedy init (groups by occurrence
   desc × pool by 5-gram rate desc), moves = single-group reassignment to any
   unused pool form + pairwise swaps, fixed move ordering (no RNG). Cap:
   4,000 J-evaluations or 45 min wall, whichever first; logged.
3. **Verification checklist** (all must hold, else construction FAILED):
   every value ∈ the 296-item inventory; every projected form ∉ lexicon
   (byte check); 89 values pairwise distinct and distinct from pins;
   n_poly=0; pins byte-identical to the pilot's.
4. **Strawman check (red-team requirement):** report `J_current(adapted)`
   alongside the frozen salad's **−2,352.3**. If
   `J_current(adapted) < −2,552.3` (more than ~200 nats below the frozen
   salad), the adapted salad is a **STRAWMAN** → the (b) comparison is VOID →
   verdict capped at INCONCLUSIVE (the +300 bar is meaningless against a
   weak adversary). This is a kill-switch on the claim, not a tuning knob:
   the construction is frozen before neural scoring and never re-rolled to
   clear the bar.

## 7. Instrument gate (is the neural LM a fair replacement?)

On the **identical held-out slice** (§4.5): require
`heldout_logp_per_char(neural) ≥ heldout_logp_per_char(5-gram)`,
the 5-gram scored by `verifier/rescore.py::CharLM`. (The 5-gram's own
held-out was −1.8594 nats/char, ppl 6.42, on Tocqueville.) If the neural LM
cannot beat the model it is meant to replace, it is a **weak instrument**:
any FAIL verdict is downgraded to INCONCLUSIVE, stated explicitly. The gate
is one-sided — passing it does not inflate SUCCESS.

## 8. Compute budget, determinism, outputs

- **Hard stop: 2h wall-clock from first training update**, regardless of
  epoch/ convergence. Eval every 300 updates (full held-out pass); keep the
  best-by-held-out checkpoint. Train NLL + held-out NLL + LR logged per eval
  (`loss_curve.json`).
- Seeds: data shuffle **20261007**; weight init **20261007**; adapted-salad
  search deterministic (no RNG). `OPENBLAS_NUM_THREADS=2` (this VM has 2 CPU).
- Pins: python **3.12.3**, numpy **1.26.4** (no torch — verified absent).
- Outputs (all written post-sign-off): `train_lm.py`, `score_neural.py`,
  `build_adapted.py`, `manifest.json` (files + full sha256 + per-file char
  counts + held-out spec + Track-A exclusion log), `loss_curve.json`,
  `model.npz` (best checkpoint), `adapted_salad.json`, `RESULTS.md`
  (three-way table + full-J substitution + verdict).
- **R5005:** no contact, ever. Track code will be `grep -rniE 'r5005|ct_R5005'`-
  clean (the red-team's standing grep); any hit = self-KILL. Control/
  diagnostic only; nothing here changes the 6-instance gate.

## 9. Pre-registered post-sign-off order of operations

1. Red-team GO in `../redteam/RULINGS.md`. 2. Track-A exclusion check (§3).
3. Write `train_lm.py`; gradient-check gate (§2) — halt if failed. 4. Train
(2h hard stop), log `loss_curve.json` + `manifest.json`. 5. Instrument gate
(§7) — record pass/fail (fail ⇒ INCONCLUSIVE path, still complete scoring
for the record). 6. Sanity gates (§5: truth-decode reproduction, frozen-salad
parts reproduction) — halt on mismatch. 7. Build + verify + freeze adapted
salad (§6); strawman check. 8. Neural three-way rescore (§5); full-J
substitution iff SUCCESS. 9. `RESULTS.md` with the verdict table.

## 10. What this PREREG does not do

No solver runs, no annealer, no R5005 contact, no Les Mis training, no
scored comparison before sign-off. The verdict concerns the **likelihood
term on 184101 only** — it does not certify the control and does not
authorize the fresh batch. A SUCCESS here means "the neural likelihood
outranks both salads on 184101 with the pre-registered margins," nothing more.

## Amendment A1 (R5a, 2026-10-07) — Les Mis 8-gram hit reconciliation (non-blocking)

Red-team R5a: §3 text said 13 hits but the verbatim phrase list summed to 14.
Reconciliation — the per-file table is correct (13); the prose list
double-counted metternich-v6 (`tout ce qu il y a de plus` written ×2, actual
×1). Corrected phrase accounting (13 total):

- guizot-memoires-t5-t6: **3** — `tant qu on n a pas vu de` +
  `qu on n a pas vu de ses` (one 9-word run) + `sur ce qu il y avait a faire`
- `tout ce qu il y a de plus`: **4** — nesselrode-v7 ×1, nesselrode-v9 ×1,
  revue-deux-mondes-1841-q1 ×1, metternich-v6 ×1
- revue-deux-mondes-1841-q1: **1** — `ce que je puis dire c est que`
- revue-deux-mondes-1841-q2: **1** — `quoi qu il en soit il y a`
- metternich-v4: **1** — `de ce qu il y a de plus`
- metternich-v6: **3** — `ce qui est hors de doute c est` /
  `qui est hors de doute c est que` / `est hors de doute c est que la`
  (one 10-word run)

3+4+1+1+1+3 = **13**. nesselrode-v8: **0** (confirmed by the red-team's
independent scan, which also confirms metternich-v6: 4). The scan script is
preserved at `track-b/scan_lesmis_overlap.py` (deterministic; reproduces the
table from the trainable bodies). Substance unchanged: all hits generic
pre-1862 idioms; Les-Mis-free confirmed by two independent scans.

## Amendment A2 (R5b, 2026-10-07, BINDING) — Track-A exclusion, determinate

Exclude `guizot-memoires-t5-t6.txt` WORD offsets **[100000,104000)** and
**[200000,204000)** per Track A's tokenization (`build_ref.py` WORD_RE on
lowercased marker-stripped body), applied **PRE-tokenization** (before the
line-shuffle): the guizot body is lowercased and word-tokenized with WORD_RE,
the two ranges are dropped from the word list, and the remaining words are
re-chunked into 50-word pseudo-lines that enter the line pool (held-out
membership by the same `(file_index, line_index)` hash rule). `manifest.json`
logs: the ranges, pre/post word counts, a positive control (excluded ranges
are non-empty real text; used-word count = total − 8000; used ∩ excluded = ∅
by construction, asserted in code). **Overlap > 0 ⇒ run VOID.**

## Amendment A3 (2026-10-07, round-2 TRACK B EXECUTOR — pre-rescore, appended pre-registration)

**Changed facts since the original registration:**
- Pin set is now **8 strong** (7 pencil cribs + **46=que**, re-derived on ≥2
  independent legs → tested ground truth). The frozen salad and the adapted
  salad were both built under the 7-pin regime (adapted_salad.json assigns
  group 46 → 'ke'). Comparisons proceed as-is: the adversary does not know
  the 8th pin; truth's information advantage from 46=que is legitimate and is
  part of what the rescore measures, not a confound.
- **Adapted salad = STRAWMAN (confirmed from disk):**
  `adapted_salad.json`: `J_current=-4992.6`, `strawman: true`
  (floor −2,552.3 vs frozen −2,352.3; `adapted.log` verification checklist all
  true). Per §1's decision table the strawman kill-switch FIRES: this round's
  verdict is **capped at INCONCLUSIVE regardless of margins**. The M_adapted
  +300 bar is retained for the record and reported descriptively, but it
  cannot license a SUCCESS claim this round. This weakens the
  adversarial-transfer worry (the old-objective adversary could not even beat
  the frozen salad) while voiding comparison (b) as a claim vehicle.
- Round-13 registry restructure is background context for interpretation only
  (5 of 10 islets dissolved into word/frame rules; 67 et/veut sole true
  polyvalence; all four homophone sets SPLIT; 1690 uniformity is lane law).
  It does not change the scoring protocol.

**Pre-registered margin bar (the "survives adversarial re-tiling" bar):**
- **`M_frozen ≥ +1,000 nats` is the live numeric bar.** Rationale: the
  verifier's documented Goodhart failure is 2,601 nats under the old
  objective (frozen salad −2,352.3 vs truth −4,953.3). +1,000 nats is ~38% of
  that failure scale. A re-tiling adversary optimizing under the neural
  objective would have to recover >1,000 nats of likelihood advantage over
  the frozen salad — which was itself the product of an annealer search
  under the old objective. The lane's own adapted-salad search (4,037
  J-evaluations, deterministic local search) gained only ~900 nats over its
  greedy init and still finished 2,640 nats below the frozen salad: observed
  re-optimization gains at this search budget are below the bar. A margin
  ≥+1,000 is therefore not plausibly closable by re-tiling; below +1,000, no
  robustness claim is made.
- **Binary NOT-GO rule (unchanged from §1):** below-bar-but-positive M_frozen
  ⇒ NO-GO on the hypothesis ("the neural likelihood fixes the Goodhart
  failure"); INCONCLUSIVE is a finding about the experiment, not a soft
  SUCCESS. Because the strawman switch fired, the strongest claim available
  this round is "M_frozen clears/does-not-clear +1,000" — a SUCCESS verdict
  and the full-J substitution (§1) are unreachable and will not be run.

**Protocol change (documented here, pre-rescore):** the round-2 work order
supersedes §8's 2h hard stop and the 3-epoch cap: training continues to
**convergence** (held-out NLL plateau across 2+ eval checkpoints) or a
**6h wall** from the round-2 task issue (2026-10-07 23:57 UTC → 05:57 UTC),
whichever comes first. `train_lm.py`: `BUDGET_S` 2h→6h, epoch cap 3→12
(`max_updates = n_steps*12`). Everything else (architecture, seeds, data
pipeline, LR schedule, best-by-held-out selection) is unchanged. Rationale:
the 2h/3-epoch budget was a compute guard, not part of the hypothesis test;
stopping a still-improving LM at an arbitrary wall would manufacture a weak
instrument. Best-by-held-out selection makes extra epochs safe against
overfitting.
