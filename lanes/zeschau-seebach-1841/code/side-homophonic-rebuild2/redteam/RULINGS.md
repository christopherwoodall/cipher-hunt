# RED-TEAM RULINGS — Seebach solver-rebuild ROUND-2 fleet

Reviewer: red-team subagent (KILL AUTHORITY over every track claim; no track
runs a scored comparison without my PREREG sign-off).
Date: 2026-10-07. Scope: `code/side-homophonic-rebuild2/` (read-only review;
this file is the only redteam write).
Charter: `../FLEET-CHARTER.md`. Tracks: `../track-{a,b,c}/`.
Delivery: tracks place `PREREG.md` in their track dir; I review from disk
(no `subagent.send` tool exists in this namespace — depth 2/2, can_spawn=no;
parent forwards follow-ups as needed).

## Reference numbers (for independent re-derivation; from
`../side-homophonic-rebuild/verifier/CLOSING-VERIFICATION.md`, all on
seed 184101, final rebuilt objective)

| decode | S_char | S_cov | S_single | S_word | S_potts | S_conc | n_poly | total |
|---|---|---|---|---|---|---|---|---|
| planted truth | −4,865.2 | 211.4 | 0.0 | +211.4 | 0.580 | 0.0 | 6 | **−4,953.3** |
| frozen pilot salad (npoly=0) | −3,325.7 | 1,581.3 | 559.4 | +1,021.9 | 1.521 | 10.0 | 0 | **−2,352.3** |

- Margin: **salad beats truth by 2,601 nats** (verifier-corrected; the Smith's
  2,577 was the pre-refine annealer best; the recorded assignment sums to
  −2,352.3). Primary recovery 1/89 = 0.0112 (chance).
- Re-derivation standard (round-1 precedent): my own rescoring code from the
  specs, no track-script imports; ≤0.1 nats = match, ≥1 nat flagged.

## Standing hard constraints (all tracks, no exceptions)

1. **NO R5005 contact.** I grep every track's code for `r5005|R5005|ct_R5005`
   before any GO; any hit = instant KILL of that track's run.
2. Control/diagnostic only. The 6-instance gate
   (`code/side-homophonic/control/CONTROL-DESIGN.md`) must pass before any
   R5005 run; nothing in round-2 changes that.
3. Deterministic seeds logged in PREREG; results must reproduce from the
   logged seeds.
4. No scored comparison runs before my dated PREREG sign-off in this file.

## PREREG review criteria (registered BEFORE any submission — 2026-10-07)

### Track A — register-gap diagnostic
- **Falsifiability:** charter bars are numeric (H0: truth ≥+500 under
  register-matched ref AND salad wins under Tocqueville; H1: salad ≥+500
  under register-matched). The ±500 band: I judge it HONEST (∼19% of the
  measured 2,601-nat Tocqueville margin; an honest acknowledgment that
  register explains part of the gap). REMAND if the PREREG does not pin:
  "diagnostic positive" ≡ H0 margin ≥+500 exactly; inconclusive-band
  outcome (−500,+500) → NO pilot anneal without a re-registration
  (charter: anneal "ONLY if diagnostic positive").
- **Leakage:** the register-matched (diplomatic) reference must be enumerated
  file-by-file with provenance + sha256 and PROVEN Les-Mis-free (scan
  against `data/gutenberg-17489-miserables1.txt`; state the n-gram rule and
  the overlap count, must be 0 on truth-slice content). The diagnostic
  rescore on sealed 184101 truth/salad is forensics-class (184101 already
  opened per CLOSING-VERIFICATION §caveats) — acceptable, must be labeled as
  such, and is NOT a control pass. The 2 new register-matched synthetic
  instances: NEW seeds (not 184101–184106, not fresh 184201–184204/184206/
  184207), plaintext from the diplomatic corpus (NOT Les Mis), deterministic
  generator invocation logged, keys held by Track A — they are Track A's own
  control, not the lane gate.

### Track B — neural char LM
- **Falsifiability:** bars numeric (+1,000 frozen, +300 adapted, defined as
  score_truth − score_salad under the trained LM on identical decode
  tokenization). REMAND if no binary NOT-GO rule: below bar → no further
  claim; the PREREG must say what sub-bar-but-positive means (it means
  NO-GO, or it re-registers — no third option).
- **Leakage (KILL vector):** training manifest file-by-file (provenance +
  sha256) with an explicit exclusion rule and count for Les-Mis-overlapping
  content — RdM reprints of Les Mis content count as Les Mis. Les Mis
  ANYWHERE in training (files, weights, validation splits) = instant KILL.
  Manifest must also exclude any text serving as truth plaintext for any
  instance being scored (cross-track contamination: if Track A's 2 new
  instances use diplomatic-corpus slices as truth, Track B may not train on
  those slices).
- **Adapted-salad adversarialness:** the adapted salad must be verified —
  non-lexicon morphemes (checked against the 3,546-word `lm_ref` lexicon),
  all-distinct values, n_poly=0, all values from the 296-item rebuilt
  inventory — AND it must be reported under the CURRENT objective alongside
  the frozen salad's −2,352.3. If the adapted salad scores >∼200 nats below
  the frozen salad under the current objective, it is a STRAWMAN and the
  +300 bar is meaningless → REMAND/KILL of the claim.
- Determinism: training seed + version pins logged; <2h CPU claim backed by
  logged wall-time.

### Track C — boundary-informed scoring
- **Falsifiability:** bar numeric (≥+800 nats → PROMISING). REMAND if the
  PREREG lacks an explicit NOT-PROMISING rule: <+800 → no 300-cell pilot.
  The score must be a single scalar with named components (re-derivable).
- **Precision:** the boundary-aware score must be defined to reimplementation
  level — exact DP recurrence, lexicon + word-weight source (which file,
  trained on what text), boundary-prior formula, and how it composes with
  (or replaces) S_char/S_word. The DP must run IDENTICALLY on truth decode
  and salad decode (same code path; no use of the known Les-Mis slice
  segmentation — that would be truth-peeking).
- **DP bias probe:** any score component trained on text containing the
  sealed truths (Les Mis in ANY weight source) = KILL. Tocqueville-trained
  weights are fine (truths are Les Mis, register-gapped).
- The 300-cell pilot slice must be pre-registered (instance, pair offset,
  length) BEFORE running — it is a diagnostic solver run on sealed-instance
  data and is only acceptable with the slice fixed in advance.

## Rulings

### R0 — PROCEDURAL: redteam standing by; no PREREG received, no GO issued
As of 2026-10-07 14:20 CDT: `track-a/`, `track-b/` empty; `track-c/` holds
`build_decodes.py` + `decodes.json` (arrived after my first scan; see R1–R2).
No track has submitted `PREREG.md`; per charter, NO scored comparison may
run until I sign off. The review criteria above were registered BEFORE
seeing any submission. Awaiting the three PREREGs.

### R1 — CONCERN (procedural): Track C began implementing before PREREG
`track-c/build_decodes.py` + `track-c/decodes.json` reconstruct the 184101
truth decode (from the sealed planted key) and the frozen pilot-salad decode
(from `pilot/rebuild-pilot-final/result.json`) via the rebuild solver
machinery, writing both strings with provenance + sha256. This is decode
plumbing, NOT a scored comparison — the charter's "no scored comparison
without sign-off" is not violated. The sealed-184101 read is
forensics-class (184101 keys already opened in round 1 per
CLOSING-VERIFICATION §caveats). But the order is wrong: `PREREG.md` is still
REQUIRED before any scoring runs. Track C is on notice; no GO issued.

### R2 — UPHELD: no R5005 contact in Track C's current work
`grep -rniE "r5005|ct_R5005"` over `track-c/`: zero hits. The script's
`no_contact=False` (`build_decodes.py:36`) is the annealer's
contact-neighbor *proposal-move* flag
(`solver/solver.py:657`: "Disabled under --no-contact … isolates the
Jaccard contact machinery"), not an R5005 data path; no annealer moves are
executed (only `_rebuild_conc()` + `_full_refresh()`), and all inputs are
synthetic 184101 pairs. Track C clean on the hard constraint. (The 4
`r5005` hits repo-wide are all in `FLEET-CHARTER.md`'s hard-constraints
section — expected, not violations.)

### R3 — GO: Track C PREREG signed off (2026-10-07)
Reviewed `track-c/PREREG.md` (10,527 bytes, 2026-10-07 19:22) against the
R0 criteria. Independent verification (my own code, no track imports):

- **Falsifiability:** bands numeric and exhaustive — PROMISING iff M ≥ +800
  (`PREREG.md:36`), NEUTRAL iff −800 < M < +800 (`:37`), BACKFIRE iff
  M ≤ −800 (`:38`); explicit NOT-PROMISING rule with "no third option and
  no re-registration of the bar after seeing M" (`:40-42`). Pilot PASS iff
  joint ≥ 0.15 AND blind ≤ 0.05 (`:204-205`); blind > 0.05 → uninformative,
  no claim (`:206-207`); joint < 0.15 → NEGATIVE (`:208`).
- **Leakage:** all 5 corpus-file sha256 in `word_stats.json` match bytes on
  disk; my independent recompute from the corpus (same tokenizer spec)
  gives N=486,789 / C=1,717,960 / V=10,666 / ρ=0.28335293 — exact match to
  `word_stats.json`; `phonetics.project` defaults confirmed
  `(word, silent_finals=True)`. §4 15-gram Les-Mis hygiene gate is
  pre-scoring with a KILL at >5 (`:144-151`); Tocqueville unused (`:§3.2`).
- **Reimplementability:** DP recurrence fully specified (`:103-110`,
  window, tie-break, B=dp[m]); components W_uni/W_len/W_bnd named with
  exact formulas (`:115-118`); decode strings frozen in `decodes.json`
  with sha256 matching the PREREG-quoted hashes byte-exact
  (`165fa8af…` / `8fb3ba26…`).
- **Pilot pre-registration:** slice verified on disk — 184101 pairs 0–299
  give exactly 62 distinct groups / 55 non-pinned, anchors
  {11,29,34,40,46,70,82} (`:175`); objectives/seeds
  7001–7004 (`:183-194`) fixed.
- **State:** no `score_boundaries.py`, no results — no scored comparison
  has run. R5005 clean (R2).

**Required correction (CONCERN, non-blocking):** `PREREG.md:83` states
C = 1,717,930 projected letters; the verified value (word_stats.json +
my recompute) is **1,717,960**. Fix the line. Non-blocking because the
explicit ρ = 0.283353 (`:88`) matches the verified artifact and
`word_stats.json` is the machine authority; a from-PREREG reimplementation
using the stated ρ still lands within the ≤0.1-nat bar.

**Interpretation caveat (CONCERN, non-blocking):** B(D) is a raw total,
not length-normalized — salad (5,143 chars) vs truth (3,164 chars), and
W_bnd = n·ln ρ penalizes the salad's higher word count. Same model applied
identically, so the comparison is legitimate, but the §1 margin must be
reported with the W_uni/W_len/W_bnd breakdown, and the §6 pilot (not the
static margin) is the behavioral arbiter.

**Verdict: GO.** Track C is cleared to run its §4 hygiene gate and write +
run `score_boundaries.py`. If the hygiene gate trips (>5 shared 15-grams),
scoring does NOT run — report to red team.

### R4 — GO: Track A PREREG signed off (2026-10-07)
Reviewed `track-a/PREREG.md` (11,669 bytes) against the R0 criteria.
Independent verification (my own code/scans, no track imports):

- **Falsifiability:** decision rule numeric and exhaustive — H0 iff
  M_d ≤ −500 AND sanity reproduced (`PREREG.md:58-59`), H1 iff M_d ≥ +500
  AND sanity (`:60`), in-band → INCONCLUSIVE with no pilot anneal without
  re-registration (`:61-62`), sanity fail → no verdict (`:63`). "Diagnostic
  positive" pinned exactly as R0 required. The ±500 band (~19% of 2,601)
  is honest, not evasive.
- **Leakage:** all 9 corpus-file sha256 match bytes on disk; my
  independent word-20-gram scan vs `data/gutenberg-17489-miserables1.txt`
  finds **0 shared 20-grams** (119,485 distinct Les-Mis 20-grams tested,
  per-file word counts match the PREREG table exactly) — the PREREG's
  "0" claim reproduces. Temporal impossibility holds (all files pre-1862;
  Les Mis 1862). Guizot spans [100000,104000)/[200000,204000) excluded
  pre-shuffle — verified in `build_ref.py` code
  (`EXCLUDE_SPANS`, list-comprehension filter before concat/shuffle).
  Pipeline verified near-verbatim vs frozen `build_lm.py`: WORD_RE
  identical (`build_lm.py:54` vs `build_ref.py:71`), `phonetics.py`
  byte-identical (empty diff), n-gram/lexicon/held-out code identical
  modulo the three documented changes (corpus, exclusion, deterministic
  shuffle → 215,000 words, size-matched to Tocqueville's 214,861).
  `lm_ref_diplo/lm.json` sha256 `5018f44c…` matches the PREREG (`:§4.4`).
- **Instrument:** `rescore_reg.py` subclasses the verifier's
  `V.Rescorer` with ONLY the lm.json path swapped (single documented
  deviation); key construction mirrors `verifier/verify.py`; the
  anchor-w2 omission is behavior-identical to the verifier
  (`rescore.py:336` `.get(g, 0.0)` default). Sanity gate reproduces the
  verifier's +2,601.0-nat margin to ≤1 nat (`PREREG.md:43`).
- **Step-4 pilot:** seeds 184301/184302 new and disjoint from all sealed
  batches (`:139`); full deviation list from CONTROL-DESIGN.md (`:§5.1`);
  bar PRIMARY ≥ 0.10 on BOTH (`:185`); deterministic seeds logged
  (`:206`); `build_instance`/`write_instance` exist at the cited path
  (`side-homophonic-rebuild/control/generator.py:494,636`); outputs to
  `track-a/instances-reg/`, keys held by Track A. **This pilot is NOT the
  lane gate** — it cannot authorize R5005 contact; the PREREG does not
  claim otherwise.
- **Perplexity caveat probed (`:124,127`):** 13.64 vs 6.42 held-out ppl.
  The diagnostic is comparative under the SAME reference, so the noisier
  LM flattens |M_d| toward 0 — bias is toward INCONCLUSIVE (conservative),
  not toward false H0. A false H0 would require the diplomatic LM to
  systematically prefer Les-Mis-like French over salad by 500+ nats, which
  IS the H0 hypothesis, with memorization ruled out by the 0-scan. The
  larger lexicon (4,776 vs 3,546) gives the salad more tiling chances —
  salad-favoring, i.e. conservative for H0. Size-matching isolates
  register from corpus size. Caveat documented, not hidden; inference
  valid. (Recorded as reviewed-and-accepted.)
- **State:** no `results/` dir — no scored comparison has run. R5005 grep
  over `track-a/`: compliance mentions only, no data contact.

**Required hardening (CONCERN, non-blocking):** `rescore_reg.py` prints
"MISMATCH -- STOP" on sanity failure but CONTINUES to the diagnostic
verdict. Make the sanity a hard stop (`sys.exit(1)`) before any diagnostic
verdict prints, so a broken instrument cannot emit a citable H0/H1 line.

**Standing cross-track note:** Guizot spans [100000,104000)/[200000,204000)
are Track-A-reserved instance truth; Track B must exclude them from any
training manifest (checked when Track B's PREREG lands).

**Verdict: GO.** Track A is cleared to execute step 3 (sanity + diagnostic
rescore → `track-a/results/rescore.json`).

### R5 — GO: Track B PREREG signed off (2026-10-07)
Reviewed `track-b/PREREG.md` (295 lines) against the R0 criteria.
Independent verification (my own code/scans; `track-b/` held only
PREREG.md at submission — halted correctly, no training/scoring):

- **Falsifiability:** SUCCESS/FAIL/INCONCLUSIVE all numeric —
  SUCCESS iff M_frozen ≥ +1,000 AND M_adapted ≥ +300 AND instrument gate
  AND strawman check (`PREREG.md:41`); FAIL iff instrument OK, adapted
  valid, either margin < 0 (`:42`); INCONCLUSIVE covers gate-fail,
  strawman, positive-but-below-bar, training-wall (`:43`). Binary NOT-GO
  rule explicit: "below either bar, no claim... re-registration — there
  is no third option" (`:45-47`). Matches the charter bars.
- **Leakage:** all 14 manifest files exist; sha256 prefixes match bytes on
  disk (guizot `3b6f4c1e…`, metternich-v4 `12416abf…`, v6 `12b8379d…`,
  talleyrand `1144d6e2…`, tocq-t1 `fafebe4f…`, t2 `20e46d72…`). torch
  confirmed absent (`import torch` → ModuleNotFoundError), so the
  from-scratch numpy LSTM is the honest architecture. My independent
  word-8-gram scan vs Les Mis reproduces **13 hits, all generic pre-1862
  idioms** matching the verbatim list (`:141-147`) — 0 truth-slice
  overlap; the Les-Mis-free verdict is substantively confirmed. Levant
  exclusion: my stopword assay confirms English-dominant (EN ~40% /
  FR ~9%; PREREG's 30.0/8.0 is assay-dependent, direction agrees) —
  good catch, correctly excluded.
- **Adapted salad:** pool premise verified EXACTLY with independent code —
  296 inventory items, 3,546-word lexicon, **189 distinct non-lexicon
  projected forms**. Construction deterministic, frozen to
  `adapted_salad.json` before neural scoring, "never re-rolled to clear
  the bar" (`:247`); verification checklist complete (`:§6.3`); strawman
  kill-switch at J_current(adapted) < −2,552.3 (`:243-244`) meets R0's
  ~200-nat requirement — genuinely adversarial or VOID.
- **Gates:** finite-difference gradient check (rel err < 1e-4) before any
  training; instrument gate one-sided (neural ≥ 5-gram held-out, else
  FAIL→INCONCLUSIVE); sanity gates byte-exact truth decode and
  frozen-salad parts within 0.1 nats (`:209,215`). Order of operations
  §9 fixed. Scope honestly bounded (§10: 184101 likelihood only; no
  control certification; no fresh-batch authorization).
- **R5005:** `track-b/` has no code yet; §8 self-KILL on any grep hit —
  standing grep runs at execution time.

**CONCERN R5a (non-blocking): 8-gram hit table is internally inconsistent.**
`:141` says "13 hits" but the per-file table sums to 14 (nesselrode-v8: 1);
my scan finds v8: 0 (0 also vs Les-Mis-with-boilerplate); the verbatim
list implies metternich-v6 has 5 (`tout…` ×2 + 3) while the table says 4
(my scan: 4, with `tout…` ×1 + 3). The SUBSTANCE is unaffected (all
reproducible hits are generic idioms; KILL-relevant question answered NO
by two independent scans), but reconcile table/text/list and preserve the
scan script (provenance gap: the original scan script is not on disk).

**CONCERN R5b (binding clarification, non-blocking for the 184101
verdict): cross-track exclusion coordinates.** `:157-160` excludes "any
(file, line-span)" claimed in `track-a/PREREG.md`, but Track A claims
**word offsets**, not line spans. Since `track-a/PREREG.md` now exists,
the exclusion is determinate: **guizot-memoires-t5-t6.txt word offsets
[100000,104000) and [200000,204000)** per Track A's tokenization
(`build_ref.py` WORD_RE on lowercased marker-stripped body), applied
**pre-tokenization** (before Track B's line-shuffle, `:§4.5`), logged in
`manifest.json`; overlap > 0 ⇒ run VOID already covers enforcement.
Prophylactic (Track B scores 184101 only), but binding before any model
reuse.

**Verdict: GO.** Track B is cleared to execute its 9-step order (`:§9`).

### R6 — PROCEDURAL: Track D (LM-JUDGE RERANKER) review queued with priority
New fleet track at `../track-d/` (dir created 2026-10-07 21:51, EMPTY as of
2026-10-07 16:52 CDT — no PREREG.md yet). Operator priority: cheap, reports
first. Per coordinator order, its PREREG review slots AHEAD of the remaining
queue once it lands. Gate criteria pre-registered BEFORE seeing the PREREG:

- **(a) Prompt verbatim review:** I review the JUDGE PROMPT text itself
  before the judge sees any candidate. The prompt must not leak the
  hypothesis — no mention of salad/truth/morphemes; pure Frenchness scoring
  of a decode string. Any hypothesis-leaking wording = REMAND (rewrite) or
  KILL of the pilot claim.
- **(b) Numeric extraction mechanical:** the 0–100 score extraction must
  leave no interpretation room (exact parse rule, e.g. regex on a fixed
  format; tie/ refusal/hedge handling specified in advance).
- **(c) Protocol specified:** 3-query median per candidate +
  `judge_log.jsonl` (every raw judge response logged with prompt hash,
  candidate id, timestamp) — specified before any query runs.
- **(d) Pilot bar + KILL RULE:** 6/6 pre-registered with a clear margin
  (suggest ≥15 points on the 0–100 scale); anything less = track DEAD
  (KILL, not inconclusive — the bar is the bar).
- **(e) MEMORIZATION PROBE adequacy:** truth plaintexts are Les Mis; a
  fluent judge-LM may have memorized them. The probe (truth vs paraphrase
  median comparison) must be adequate to detect this. If
  median(truth) >> median(paraphrase) (memorization detected), a pilot PASS
  is VOIDED. I will rule explicitly, per probe outcome, on whether Track D
  may proceed to step 4: PASS+clean probe → may proceed; PASS+dirty probe →
  VOID, track dead; anything below bar → KILL RULE (d).
- **(f) Objective integrity:** the top-K=20 dump diff to `solver.py` must not
  alter the objective — J byte-identical (diff review).
- **Prompt freeze:** the prompt is frozen at my sign-off; any later tuning
  = re-registration + new pilot, no exceptions.
- Standing constraints apply (no R5005 contact; deterministic seeds;
  control/diagnostic only).

No GO/REMAND/KILL issued — awaiting `track-d/PREREG.md`.

## Tally
**0 KILL / 0 DEMOTE / 6 CONCERN** (R1: Track C pre-PREREG implementation;
R3a: Track C PREREG C typo — fix required; R3b: B(D) length-effect
interpretation caveat; R4a: Track A rescore_reg.py sanity should hard-exit;
R5a: Track B 8-gram table inconsistencies — reconcile; R5b: Track B
cross-track exclusion coordinates — binding clarification recorded)
**/ 4 UPHELD** (R2: Track C no R5005 contact; R3: Track C PREREG meets R0;
R4: Track A PREREG meets R0 + 20-gram scan reproduces 0; R5: Track B PREREG
meets R0 + 8-gram substance + 189-form pool verified). **3 GO** (Track C:
§4 gate + score_boundaries.py; Track A: step-3 sanity + diagnostic rescore;
Track B: 9-step order). R0 procedural.

### R7 — GO: Track D PREREG signed off (2026-10-07)
Reviewed `track-d/PREREG.md` (13,069 bytes) + `track-d/judge_prompt.txt`
against the R6 gate criteria. Independent verification (my own shell/scans,
no track imports):

- **(a) Prompt verbatim review:** the frozen prompt mentions only
  "French-language fluency"/"FRENCHNESS" with generic anchors (fluent /
  garbled / adversarially constructed). Zero hits for salad/truth/
  morpheme/cipher/Les Mis. The word "adversarially" describes the
  low-fluency end of the scale, not the hypothesis. Prompt sha256
  `390a1ec0…c08e21d` recomputed from `track-d/judge_prompt.txt` —
  **exact match** to the PREREG-quoted hash. No hypothesis leak. PASS.
- **(b) Numeric extraction mechanical:** first output line parsed as int
  [0,100] (`PREREG.md:§2.4`); unparseable/out-of-range → EXTRACTION-FAILED
  logged and excluded; NO steering/rephrasing/re-querying, one attempt
  each; <2 valid queries → candidate VOID (`:§2.5`); median of 3 is exact
  for odd valid counts; step-5 per-instance tie-break pre-registered
  (higher J, then lower restart index, `:§5`). Refusal/hedge/tie handling
  fully specified in advance. PASS.
- **(c) Protocol specified:** blind 8-hex labels with sealed
  `label_map.json` (`:§2.2`), 3 independent shuffled passes (`:§2.3`),
  median aggregation (`:§2.5`), mechanical first-line extraction
  (`:§2.4`), `judge_log.jsonl` with `prompt_sha256` per call (`:§2.6`) —
  all specified BEFORE any query runs. `track-d/` holds only
  `PREREG.md` + `judge_prompt.txt`: no `candidates.json`, no log, no
  scoring — halted correctly. PASS.
- **(d) Pilot bar + KILL RULE:** PILOT PASS iff `mT(i)−mS(i) ≥ 15` on ALL
  6 (`:§3`); anything less → "the track is DEAD", "no re-registration of
  the bar after seeing results" — the R6 kill rule verbatim. PASS.
- **(e) Memorization probe adequacy:** void rule `mT(i)−mP(i) ≥ 15` on ANY
  instance → pilot PASS VOID, no §5 without a new red-team ruling
  (`:§4`); proceed requires PASS + clean probe + red-team memorization
  ruling; anomaly fallback (`mP ≤ mS` → probe uninformative, ruling
  required) bound. Paraphrases written after GO, frozen with sha256
  before scoring (`:§7.3`). No-local-LLM finding REPRODUCED by me:
  `which ollama` absent; TCP connect to 127.0.0.1 on
  11434/11435/8080/8000/1234/5000/7860 all closed — self-operator mode is
  the honest fallback. The void rule is directionally conservative: the
  paraphrase gets natural spacing (format advantage over the spaceless
  truth), so a firing void means the judge preferred handicapped truth
  by ≥15 — strong memorization evidence. Probe adequate as a
  pre-registered deconfounder; the binding re-ruling requirement (§4,
  §8) is the enforcement point. PASS with R7b/R7c below.
- **(f) Objective integrity:** `solver.py` md5
  `aac6f2602eab09ee24ba7a6709a02123` and `config.json` md5
  `de2c3fccd77e9c7c3b21e9549e49a1e3` recomputed from
  `code/side-homophonic-rebuild/solver/` — **both exact matches** to the
  PREREG. `solver.py:1036-1076` confirms the `restarts[]` structure:
  each restart dict carries full `assignment` (per-group v1/v2/w2),
  `best` (J), and `score_parts`, sorted descending by `best`, written to
  `result.json` as `'restarts': restarts` (`:1110`). Top-20 distinct
  finals by J is pure post-processing — the "no solver.py change"
  claim is verified. `config.json` iters=40000, t0=60.0 as cited. §5
  CLI flags (`--pairs --lm --anchors-file --out --restarts --seed`)
  all exist (`solver.py:1125-1137`). PASS.
- **Standing:** `grep -rniE "r5005|ct_R5005"` over `track-d/`: hits only
  in `PREREG.md` prose as compliance mentions ("NO R5005 contact",
  "do not touch R5005") — zero data contact. Seal claim verified:
  `verifier/CLOSING-VERIFICATION.md` confirms sealed truth keys for
  184101–184106 "were opened for forensics only" — no new seal opened
  by the pilot. Fresh batch (184201–184204, 184206, 184207) never read
  (`:§5` pre-run grep self-check bound). Pilot cost 54 calls (18×3) vs
  the brief's 36: the probe's 18 are flagged honestly (`:§2.3`, `:§3`) —
  the R6(e) probe REQUIRES them, so the count is accepted. Prompt freeze
  bound (`:§1`, `:§7.4`). Seeds 7101–7106 fixed, disjoint from
  track-c's 7001–7004 and all instance seeds.

**CONCERN R7a (binding, non-blocking): self-operator class blindness
does not hold.** Instance-label blindness holds procedurally
(`label_map.json` sealed until logging completes), but class blindness
cannot: surface formats are class-identifiable (spaceless ear-noised
Les-Mis truth vs morpheme tiling vs natural-spaced paraphrase the
operator authored). The operator also disclosed recon exposure to
184101 head/tail fragments (`:§3`). The residual anti-steering controls
— frozen prompt, no re-query/steering, mechanical extraction, median,
complete logging — are the maximum self-operator mode supports and
are honestly documented. The pilot's evidentiary weight therefore rests
on log auditability, not blindness. Accepted for a cheap pilot; my
post-pilot ruling will re-examine steering indicators (per-query
variance, score distributions) before any step-4 clearance.

**CONCERN R7b (non-blocking, recorded): probe sensitivity limits.** The
void rule detects only ≥15-point memorization preference; mild
memorization (5–10 pts) passes clean and could be decisive at the bar
margin. The paraphrase preserves Les-Mis meaning, so content-level
recognition could boost truth AND paraphrase symmetrically, shrinking
`mT−mP` while the truth-vs-salad margin stays recognition-inflated.
Accepted because (i) the bar's own rationale is that a working judge
separates fluent prose from morpheme tiling by "far more than 15"
(`:§3`), making a marginal 15–25-point pass on all six the
scrutiny trigger at the post-pilot ruling, and (ii) the
`mP ≤ mS` anomaly fallback catches a non-discriminating judge.

**CONCERN R7c (binding clarification, non-blocking): void-rule vs
R6(e).** R6(e) states: PASS+dirty probe → VOID, track dead. The
PREREG's "no §5 without a new red-team ruling" (`:§4`, `:§8`) is hereby
bound to mean: a VOIDED pilot is terminal for this pilot; the "new
ruling" cannot resurrect it — continuation requires a fresh PREREG +
new pilot. Post-pilot ruling framework (locked): PASS + clean probe
(`mT−mP < 15` all six, `mP > mS` all six) → may proceed to step 4
with my explicit step-4 clearance; PASS + dirty probe → VOID, track
dead; below bar → KILL RULE (d), track dead.

**Verdict: GO.** Track D is cleared to run the PILOT ONLY: build
`candidates.json` (decode plumbing via the track-c pattern), write the
6 paraphrases (frozen with sha256 BEFORE any scoring), then 54 judge
calls (18 candidates × 3 passes) under the §2 protocol. Steps 4/5
(gate anneal + 360 judging calls) run ONLY after pilot PASS + clean
probe + my explicit post-pilot step-4 clearance ruling in this file.
Any prompt change before or after = re-registration + new pilot.

## Tally
**0 KILL / 0 DEMOTE / 9 CONCERN** (R1: Track C pre-PREREG implementation;
R3a: Track C PREREG C typo — fix required; R3b: B(D) length-effect
interpretation caveat; R4a: Track A rescore_reg.py sanity should hard-exit;
R5a: Track B 8-gram table inconsistencies — reconcile; R5b: Track B
cross-track exclusion coordinates — binding clarification recorded;
R7a: self-operator class blindness does not hold — binding, log
auditability is the control; R7b: probe sensitivity limits — recorded,
marginal-pass scrutiny at post-pilot ruling; R7c: void-rule vs R6(e)
alignment — VOID is terminal, resurrection needs re-registration)
**/ 5 UPHELD** (R2: Track C no R5005 contact; R3: Track C PREREG meets R0;
R4: Track A PREREG meets R0 + 20-gram scan reproduces 0; R5: Track B PREREG
meets R0 + 8-gram substance + 189-form pool verified; R7: Track D PREREG
meets R6 — prompt hash, solver md5s, seals, no-local-LLM all reproduce).
**4 GO** (Track C: §4 gate + score_boundaries.py; Track A: step-3 sanity +
diagnostic rescore; Track B: 9-step order; Track D: pilot only —
candidates.json + paraphrases + 54 judge calls; steps 4/5 need post-pilot
PASS + clean probe + explicit step-4 clearance). R0 procedural.

### R8 — GO: Track D step-4 clearance (post-pilot, 2026-10-07)
Independent re-verification of `track-d/PILOT-REPORT.md` + `judge_log.jsonl`
+ `label_map.json` + `candidates.json` (my own code, no track imports):

**(a) Medians reproduce; log intact.** 54 lines = 18 labels × 3 passes, zero
duplicates, zero missing, `prompt_sha256 = 390a1ec0…c08e21d` in all 54.
Mechanical first-line-int extraction: 54/54 match the logged
`extracted_score`, zero EXTRACTION-FAILED. Under the authoritative
`label_map.json` (PREREG §2.6: analysis reads log + sealed map): truth
medians {64,61,61,63,62,62}, salad {21,20,22,20,21,20}, paraphrase
{90,90,91,91,92,92}; class medians 62 / 20.5 / 91; margins mT−mS =
**43,41,39,43,41,42**; void values mT−mP = −26,−29,−30,−28,−30,−30 —
**byte-exact** vs the report's verdict table. Score range [19,93],
cross-pass range ≤ 2, pass-order means flat (no drift). **CORRECTION
R8a (required, non-blocking):** the report's per-query table scrambles
the label↔seed column on ~10 of 18 rows vs `label_map.json` (labels +
score triples are internally consistent with the log; only the seed
column is misassigned — e.g. table "184102 salad d24f0ea5" is
184103's salad per the map). The verdict numbers were computed under
the correct map and are unaffected; fix the table's seed column to
match `label_map.json` before the numbers are cited downstream.

**(b) Salad substitution ACCEPTED — points stand.** `frozen-ctl-184105/`
and `frozen-ctl-184106/` exist but are EMPTY (verified); the PREREG's
candidate definition was unfulfillable for those two seeds. The run3
substitutes are instrument-identical, verified: same solver
(`side-homophonic/solver.py`), same config (lambda_poly=20.0,
iters=40000, t0=60.0, restarts=12), same score-part signature
(S_char/S_word/S_ac/S_single/S_conc/S_potts/S_soft), n_poly 59–60 vs
frozen-ctl 59–61, J 4,459–4,773 vs 4,127–4,815. Decode texts are
texturally identical (`memememeleurs…` tiling, 4,465/4,386 chars vs
4,345–4,593 for the four frozen-ctl salads); judge scores 21/20 sit
inside the frozen-ctl salad band (20–22); margins 41/42 inside the
39–43 band. run3 predates Track D's GO (18:31 vs 22:01 build); track
took `best.assignment` as-is per provenance — no cherry-pick evidence.
The deviation from PREREG §3 ("no substitution") was disclosed with
provenance and flagged for this ruling: honest deviation under
necessity, evidentiary substance preserved. **No voiding — 6/6 valid
pilot points.** (Lesson R8b, non-blocking: future PREREGs pre-register
the fallback path. Terminology note: round-2 frozen salads are
n_poly≈59–61 polyphonic tilings; the RULINGS "npoly=0" figure is a
round-1 artifact, not this instrument's class.)

**(c) Probe clean; R7b residual bounded.** Void rule needs mT−mP ≥ 15;
observed −26..−30 — missed by ≥ 41 points. mP > mS everywhere (90+
vs ≤ 22): probe informative, anomaly fallback not triggered.
Symmetric-recognition bound: truth>salad worst margin is 39; the
recognition premium R ≤ min(mP) − 75 = 15 (paraphrase floor at the
prompt's own "clearly French" 75 anchor — conservative). True fluency
margin ≥ 39 − 15 = **24 ≥ 15 bar**, 9 points of headroom. Corroborated
by justifications (truth penalized for "missing word boundaries and
by-ear spellings") and the 26–30 pt paraphrase>truth gap on identical
content — the judge discriminates on surface. R7b's marginal-pass
scrutiny band (15–25) not reached (39–43).

**(d) Protocol compliant.** Prompt sha256 recomputed from
`track-d/judge_prompt.txt` = PREREG = all 54 log entries; prompt mtime
21:55, scoring 22:10–22:13 — no tuning window; `judge_driver.py`
asserts the hash at startup (any change aborts). Extraction fully
mechanical (see (a)); zero re-queries; no hedging/refusal/
memorization markers in any justification; R7a's class-identifiability
residual stands but the log-auditability control holds (all raw
responses + justifications retained).

**(e) R7c: pilot not under a dirty probe — clean.** No terminal-kill
trigger. Steps 4/5 not run (no `gate_runs/`). R5005: prose mentions
only, zero data contact. `solver.py` md5 `aac6f260…` and `config.json`
md5 `de2c3fccd…` re-verified byte-identical to the R7-logged hashes.

**Verdict: GO.** Track D is **cleared for step 4**: gate anneal on the
6 FRESH sealed instances (184201–184204, 184206, 184207) with
`--restarts 24 --seed 7101–7106`, `solver.py`/`config.json`
byte-identical to the logged md5s (verified), top-20 by J per
instance, 360 judge calls under the frozen §2 protocol, top-1 median
= answer, gate scoring per CONTROL-DESIGN.md §4 (primary mean ≥ 0.20 /
min ≥ 0.10; secondary mean ≥ 0.30 / min ≥ 0.22). **Step 5 (any R5005
contact) remains FORBIDDEN — a gate PASS does not authorize R5005;
that authorization is the parent's call.**

## Tally
**0 KILL / 0 DEMOTE / 11 CONCERN** (R1; R3a; R3b; R4a; R5a; R5b; R7a;
R7b; R7c; R8a: Track D pilot-report per-query table seed column
scrambled vs label_map.json — fix required, verdict numbers unaffected;
R8b: PREREG §3 needs a pre-registered substitution fallback clause +
n_poly terminology note) **/ 6 UPHELD** (R2; R3; R4; R5; R7; R8: Track D
pilot 6/6 verified byte-exact + clean probe + substitution accepted +
step-4 clearance) **/ 5 GO** (Track C; Track A; Track B; Track D pilot;
Track D step-4 gate anneal + 360 judging calls — steps 4 only, R5005
forbidden). R0 procedural.

### R9 — GO: Track C v3 PREREG (word-bigram repair) signed off (2026-10-07)
Reviewed `track-c/PREREG-C-v3.md` (9,363 bytes) against the task checklist:

**(a) Falsifiability — PASS.** Three gates numeric and exhaustive:
(a) M ≥ +800; (b) non-degenerate argmax carried from v2 unchanged
(truth mean word length ∈ [1.765, 7.059] AND ≥50% truth argmax
in-vocab); (c) STRICT per-char inequality
B_v3(truth)/|truth| > B_v3(salad)/|salad|. Verdict PROMISING-v3 iff
(a)∧(b)∧(c), NULL-v3 otherwise — (a)∧¬(c) → NULL-v3 stated explicitly
(`:§2`). No evasion path to PROMISING-v3 around (c): the conjunction
is exhaustive, strictness puts equality in NULL territory, and "no
third option; no re-registration of any bar after seeing the numbers"
is bound.

**(b) Formula — PASS, reimplementable from spec alone.**
B_v3(D) = max over DP tilings of
Σᵢ[logP_uni(wᵢ) + λ_bi·logP_bi(wᵢ₋₁,wᵢ)] with ln L(|w|)+ln ρ folded per
word into s(w); DP states (end position, ending word), window 20,
exact recurrence (`:§1.5`), deterministic tie-break (j ascending, u in
lexicographic-ascending order, keep first strictly-greater on exact
float `>`, backpointers follow the same order). First word
unigram-only, no start symbol — justification adequate (the corpus
spec provides no fitted sentence-initial distribution; one transition
in ~1,300 is immaterial either way; see R9b). All v2 constants carried
verbatim: N=486,789, C=1,717,960 (R3a typo confirmed fixed in both
specs), V=10,666, ρ, L(k), p_char. No decode consulted in fitting.

**(c) λ_bi = 1.0 — ACCEPTED as specified.** Same nat units make 1.0 the
parameter-free default; any tuned λ would be fit on truth/salad =
hypothesis contamination (v1 §3 anti-gaming); the motivating v2 §7
diagnostic was computed at effective λ=1, so the motivation matches
the pinned value. No sensitivity analysis required: gate (c)
arbitrates the outcome at ANY λ — an unhelpful λ converts to NULL-v3
honestly rather than inviting re-tuning, which the spec explicitly
bars ("λ_bi is NOT tuned after seeing any v3 number").

**(d) OOV-bigram fallback — ACCEPTED as specified; quirk on the
record.** Literal add-1 over the fitted corpus (no new parameter):
c(u)=0 for u ∉ V → uniform follower rate ln(1/V) ≈ −9.2746. The
no-extra-OOV-penalty call is defensible: OOV already pays
|w|·ln(p_char) ≈ −11.5/char in the v2 unigram, so a further transition
penalty double-counts the OOV event; the "OOV-context transitions
cheaper than garbled in-vocab transitions" quirk is intrinsic to
add-1 bigrams and mechanism-symmetric across decodes. Moot under the
v2 validity precondition (both v2 argmaxes 100% in-vocab). R9a below
covers visibility.

**(e) Residual-risk disclosure — ADEQUATE.** §5 states the +1,200-nat
motivation was computed on the v2 tilings, the salad re-optimizes
under B_v3 and the gap may shrink or invert, with gate (c) as the
honest arbiter either way; also discloses bigram dynamic-range
compression and the untuned-λ case (which converts to NULL-v3, "the
honest outcome, not a tuning invitation"). One additional vector
worth naming: truth-argmax OOV-share drift under re-optimization —
bounded by gate (b)'s ≥50% in-vocab floor and made visible by R9a.

**(f) Leakage/determinism — CLEAN.** Same diplomatic corpus as v1/v2
(Les-Mis-free; §4 hygiene gate already PASSED, carried forward, no
re-run — correct); no new data; deterministic spec, no RNG.
`grep -rniE "r5005|ct_R5005"` over `track-c/`: hits only in
compliance prose ("no R5005 contact", "Never touches R5005") plus the
compiled copy of the same prose — zero data contact. Scorer NOT yet
written (confirmed: no `score_boundaries_v3.py` on disk) — correct,
sign-off precedes it.

**(g) Pilot gating — CONFIRMED.** Execution order is spec → scorer →
one static run → STOP; `§4`: "The pilot itself stays gated on
red-team clearance AFTER the v3 static result is reviewed." §6 bar
unchanged (joint ≥ 0.15 AND blind ≤ 0.05).

**CONCERN R9a (binding, non-blocking): OOV-quirk visibility.**
`score_boundaries_v3.py`'s report must include OOV word-share on BOTH
v3 argmax tilings (salad currently diagnostic-only) alongside the
§1.6 R3b decomposition, so the OOV-transition quirk's practical
footprint is visible on the re-optimized tilings, not just assumed
from v2.

**CONCERN R9b (non-blocking): first-word modeling choice.** The
unigram-only first word (no start symbol) is accepted as a fitted
modeling choice with ~1/1,300 weight. Revisit only if the v3 argmax
shows edge-effect concentration (e.g. the static result's diagnosis
attributes a decisive margin share to first-word tilings).

**Verdict: GO.** Track C is cleared to write `score_boundaries_v3.py`
and run the static comparison ONLY. The §6 joint pilot needs a
SECOND, separate clearance after the v3 static result is reviewed in
this file. If v3 is NULL-v3, the report diagnoses the failing
term/gate with numbers; a third honest null is an accepted return.

## Tally
**0 KILL / 0 DEMOTE / 15 CONCERN** (R1; R3a; R3b; R4a; R5a; R5b; R7a;
R7b; R7c; R8a: Track D pilot-report per-query table seed column
scrambled vs label_map.json — fix required, verdict numbers unaffected;
R8b: PREREG §3 needs a pre-registered substitution fallback clause +
n_poly terminology note; R9a: OOV-bigram quirk — require OOV word-share
on BOTH v3 argmaxes in the report, binding, non-blocking; R9b: first-word
unigram-only modeling choice accepted, revisit only on edge-effect
concentration; R10a: (i)-rejection proof overstates IEEE-754 strictness
— division by a positive constant is monotone with possible
tie-collapse, not strictly order-preserving; conclusion stands via the
byte-identical enforcement, non-blocking wording hedge; R10b: +800 bar
under length-neutralization is far harder than in v1–v3 (needs
ς ≈ −0.95 nats/char); honest and disclosed, recorded)
**/ 9 UPHELD** (R2; R3; R4; R5; R7; R8: Track D pilot 6/6 verified
byte-exact + clean probe + substitution accepted + step-4 clearance;
R9: Track C v3 PREREG meets the checklist — exact formula, exhaustive
gates, pinned λ_bi, defensible OOV fallback, adequate risk disclosure,
no R5005 contact; R10: Track C v4 PREREG meets the checklist —
load-bearing (i)-rejection, pinned decode-blind ς fit, four exhaustive
gates, clean line closure, no scorer written; R11: Track C v4 numbers
independently confirmed — NULL-v4 stands, §6 pilot STOOD DOWN,
statistical line CLOSED)
**/ 7 GO** (Track C; Track A; Track B; Track D pilot; Track D step-4
gate anneal + 360 judging calls — steps 4 only, R5005 forbidden; Track C v3:
write `score_boundaries_v3.py` + run the static comparison only —
§6 pilot needs a second clearance after the v3 static result; Track C v4:
fit ς from reference text + write `score_boundaries_v4.py` + run the static
comparison only — §6 pilot needs a further clearance after the v4
static result). R0 procedural.

### R10 — GO: Track C v4 PREREG (fitted-length-baseline repair) signed off (2026-10-07)
Reviewed `track-c/PREREG-C-v4.md` (16,750 bytes) against the task checklist:

**(a) (i)-rejection — PASS, proof load-bearing and sound.** For fixed D,
|D| is constant; the v3 DP's argmax under B_v3(D)/|D| is the same argmax
(the DP's strict-`>` comparisons under the pinned tie-break are
unaffected by a positive-constant divisor in exact arithmetic), and the
resulting comparison B_v3(truth)/3164 vs B_v3(salad)/5143 is
byte-identical to v3's already-failed gate (c) (−6.7407 vs −4.6687,
RESULTS-C-v3.md §3). The rejection is correct and closes the evasion
path of re-registering the dilution frame as a "repair." CONCERN R10a
(non-blocking, wording): the spec's "strictly order-preserving … a > b
⟺ a/c > b/c" overstates IEEE-754 — correctly-rounded division by a
positive constant is monotone but NOT strictly so (distinct floats can
collapse to the same quotient when (a−b)/c < ulp/2). The conclusion
does not depend on strictness: even a tie-collapse leaves the argmax
the same optimization, and §4 step 2's byte-identical-tiling assertion
(conversion of any deviation into instrument-VOID, not a verdict) is
the correct empirical enforcement. Hedge the §1/§6 wording; the logic
stands.

**(b) Form (ii) definition — PASS, pinned and leakage-free.**
ς = S_R/m_R is specified to reimplementation level: the 5 diplomatic
files (v1–v3's, sha256 per word_stats.json), the v2/v3 tokenizer
(WORD_RE → phonetics.project() defaults, empty projections skipped),
ALL v2/v3 constants and fallbacks verbatim (incl. λ_bi=1.0, first token
of each file unigram-only, within-file pairs only — mirroring v3's
pinned choices), computed and LOGGED before any decode byte is read,
VOID band (−25, 0). Zero decode input, zero degrees of freedom at
verdict time — same fitted-but-decode-blind class as ρ. The natural
tiling is the right estimand: it measures genuine-French expected rate,
whereas the DP optimum would measure adversarial-best quality (the
salad's own game). The conservativeness claim is directionally correct:
natural tiling is DP-feasible ⇒ ς_natural ≤ ς_DP-opt, and
M_v4 = M_v3 + 1979·ς is increasing in ς (1979 = 5143−3164, verified),
so the more-negative natural ς biases M_v4 downward — against
PROMISING, the safe direction; (c1) covers fit uncertainty
symmetrically.

**(c) Falsifiability — PASS, no evasion path.** Four gates, conjunction
exhaustive: (a) M_v4 ≥ +800 at fitted ς; (b) non-degenerate carried
from v2/v3 unchanged; (c1) M_v4 ≥ +800 under ς′ ∈ {0.8ς, 1.2ς} —
binding end correctly identified as 1.2·ς (ς<0 ⇒ 1.2·ς most
negative ⇒ smallest M_v4), pure arithmetic from fixed M_v3, no new DP;
(c2) per-transition bigram rate truth > salad AND seen-pair share
truth > salad, both strict (equality → NULL). PROMISING-v4 iff all;
(a)∧¬(c1∧c2) → NULL-v4 explicitly — the v2/v3 margin-without-substance
dodge is closed again. (c2) being "expected to hold" from v3 §4.4
(−7.657 vs −8.545; 0.634 vs 0.359) is disclosed, not assumed — it is
computed on the run's own asserted-identical tilings. Keeping +800
(not a per-char δ) is justified: M_v4 is length-neutralized, so the
bar no longer smuggles the length channel, and a per-char δ would
reintroduce the rejected (i)-frame; bar stability across versions is
the anti-gaming choice. CONCERN R10b (non-blocking, recorded):
length-neutralization makes +800 far harder than in v1–v3 — M_v4 ≥ 800
needs ς ≥ (800−2683.9)/1979 ≈ −0.95 nats/char, i.e. the model would
have to score genuine French ~5–7× better per char than the DP's best
adversarial tilings (−4.7 to −6.7) — while the spec's own honest prior
is NULL-v4 and the v3 content decomposition was −6,555.6 salad-side.
The test is coherent and the prior is disclosed, so this is honest
hardness, not a flaw — but PROMISING-v4 is effectively out of reach
unless the reference fit surprises; the NULL-v4 close (§7/§8) is the
load-bearing outcome and it is airtight either way.

**(d) Line-status honesty — PASS, closure clean.** §7: "Track C does
not re-register a fifth statistical variant"; §8: "If v4 nulls: the
statistical boundary line is CLOSED. No v5. Escalate to structural
methods — dependency-parse features (SPS fallback family)." Honest
prior of NULL-v4 recorded in §6 as motivation, not prediction. No
end-run room: the closure names the successor class (structural,
syntactic well-formedness) and bars a fifth statistical variant
explicitly; PROMISING-v4 unlocks only a *request* for pilot clearance,
not the pilot.

**(e) v3 scorer reuse + byte-identical assertion — ADEQUATE.** The ς
fit is a fixed-tiling sum over reference text — no DP optimization, no
decode contact — so it needs no independence from the v3 DP code path;
the only shared artifacts are the frozen fitted tables (bigram table,
unigram stats), which is legitimate reuse of reference-fitted
constants. The byte-identical-tiling assertion is correctly scoped as
a drift check on the B_v3(D) inputs (any deviation = instrument VOID),
not a new optimization. No independence gap.

**(f) Leakage/determinism — CLEAN.** ς fit from reference text only at
execution time, decode sha256 re-verified, no RNG. `grep -rniE
"r5005|ct_R5005"` over `track-c/`: hits only in compliance prose
(PREREG-C-v4.md's own standing requirement at §4 step 2) plus compiled
pyc copies of the same v2/v3 prose — zero data contact. §6 pilot stays
gated: §4 step 4 STOPs after the static run; §5 keeps slice/objectives/
seeds 7001–7004/protocol and the unchanged bar behind a separate
clearance. Confirmed in spec.

**(g) Scope — CORRECT.** No `score_boundaries_v4.py` on disk
(verified); no v4 artifacts; sign-off precedes the scorer.

**Verdict: GO.** Track C is cleared to fit ς from the reference text,
write `score_boundaries_v4.py`, and run the static comparison ONLY.
The §6 joint pilot needs a FURTHER, separate clearance after the v4
static result is reviewed in this file. If v4 is NULL-v4, the report
diagnoses the failing term/gate with numbers; a fourth honest null
closes the statistical line per §8.

### R11 — CONFIRM: Track C v4 numbers independently verified; NULL-v4 stands; §6 pilot STOOD DOWN; statistical boundary line CLOSED (2026-10-07)
Independent re-verification of `track-c/RESULTS-C-v4.md` +
`rhat_fit_v4.json` + `boundary_scores_v4.json` (my own code from
PREREG-C-v4.md spec alone, `/tmp/redteam_r11_check.py`; no track imports
— only the frozen reference-fitted tables `word_stats.json`/`word_vocab.json`
and the pinned tokenizer library `phonetics.project`, per R10(e); the ς
fit is decode-blind by construction so table reuse is not independence loss):

- **(a) ς fit reproduces EXACTLY.** ς = −5.0201522127, diff 0.0 vs the
  recorded −5.02015221265611 (bar ≤1e-4) ✓; inside the (−25, 0) VOID
  band ✓. S_R = −8,624,420.6953, m_R = 1,717,960; all five per-file
  rows (S_F, W_uni, W_bi, W_len, W_bnd, K, m, OOV) match the reported
  table; ΣK = 486,789, Σm = 1,717,960 = fitted corpus constants ✓;
  n_seen_pairs = 145,715, n_pair_tokens = 469,672 match the fit log ✓.
- **(b) Margin arithmetic reproduces.** M_v4 = M_v3 + 1,979·ς with
  frozen M_v3 = 2,683.8641775035103 → −7,251.017051, diff −1.8e-12 nats
  vs the recorded −7,251.017051342929 (bar ≤1 nat) ✓.
- **(c) Gates as recorded.** (a): −7,251.0 ≥ +800 → **FAIL** ✓ (misses
  by 8,051 nats). (c1): at 0.8·ς → −5,264.04 → FAIL; at 1.2·ς →
  −9,237.99 → FAIL ✓ (binding end 1.2·ς as pinned; no knife-edge near
  the bar). (c2): W_bi/n_transitions reproduces the recorded
  per-transition rates exactly (−7.6572 vs −8.5449, truth > salad strict
  ✓); 822/1,296 = 0.6343 vs 452/1,259 = 0.3590, truth > salad strict ✓
  — recorded c2 numbers are arithmetically consistent with the
  drift-checked v3 DP aggregates. (b) carried over ✓.
  **Verdict NULL-v4 stands.**
- **(d) §6 joint pilot NOT run — confirmed, and formally STOOD DOWN.**
  No pilot artifacts in `track-c/` (no pilot slice, no joint-pilot
  outputs; the "7003" grep hits are digit substrings of the
  S_F_per_char floats, not artifacts; PREREG's "seeds 7001–7004" exist
  only as spec text). The pilot is not merely awaiting clearance: per
  the §8 line closure, it is STOOD DOWN — a NULL-v4 line does not
  request it, and no clearance may now be issued for it.
- **(e) No R5005 contact.** `grep -rniE "r5005|ct_R5005"` over
  `track-c/`: hits in PREREG specs, scorer compliance comments, and
  RESULTS prose only — zero data contact.

**Disposition per PREREG-C-v4 §8 (binding):** v1 (OOV economics),
v2 (order-blindness), v3 (length channel in the raw total), v4
(length-neutralized content deviation) — four nulls, each sharper,
each honestly returned. **The statistical boundary line is CLOSED.
No v5.** Successor NAMED, not built: structural escalation —
dependency-parse features, the SPS fallback family (syntactic
well-formedness the morpheme salad cannot fake and ear noise degrades
but does not erase). A fifth statistical re-registration is barred by
this ruling and the §8 closure.

**Verdict: R11 recorded.** v4 numbers independently confirmed;
NULL-v4 stands as the line's terminal verdict.

### R12 — GO (two-stage): Track D PREREG-D-v2 signed off (2026-10-07)
Reviewed `track-d/PREREG-D-v2.md` + `track-d/experiment0.json` +
`track-d/experiment_0.py` + `track-d/solver-cell/solver.py` against the
checklist. Independent verification (shell/md5/diff, no track imports):

**(a) Experiment 0 — UPHELD, Branch-B call endorsed as data-driven.**
`experiment0.json` exists (written 2026-10-07T22:58:12Z, `experiment0.log`
EXIT=0); per-instance numbers match the PREREG §1 table EXACTLY:
ΔJ 2,374.7–2,721.8 (range 2,375–2,722 as claimed), Hamming 86–89
(groups = nonpin on all six), primary recovery 0.000–0.034, verdicts
6/6 SLIDE by the pre-registered rule (Hamming ≤ 5 → STAY fails on all;
δJ > 500 AND rec < 0.10 holds on all; DRIFT unused). J(truth) 184101 =
−4,953.26 — reproduces the verifier reference −4,953.3 to 0.1 nats.
Seal hygiene: SEEDS hardcoded 184101–184106; the script reads only
`SYNTHETIC-ct/crib/key-18410{1..6}` (truth reads are forensics-class,
opened in round-1 forensics); `grep` for 184201+ over script/log/json =
zero hits — no fresh-seal contact. The script genuinely initializes AT
the truth key (`apply_truth` installs the sealed key; `init_key()`
skipped via `anneal_from_current`; only move/cooling/accept logic is the
frozen solver's). Branch-B call justified: final J sits at −2,357 to
−2,671 — squarely in the recorded salad band (2,601-nat margin class) —
at chance-level recovery, after the annealer walked 86–89/89 groups away
from a truth start. The alternative reading (triage over J-climb
endpoints still adds value) fails on the numbers: endpoints carry no
truth signal (rec ≤ 0.034), and triage-as-a-mechanism survives inside
Branch-B ILS (parent medians, final median-of-3) — only triage *over
J-climb endpoints* is declared dead. The Branch-B selection is a
data-driven branch, not an interpretation stretch. R12c (non-blocking,
recorded): the probe used the OLD move set; the "no restart-based
method under J" inference generalizes via the ~2.6k-nat J-margin
argument (the fork's coarser moves make staying *less* likely, not
more), but the fork itself was not the probe instrument.

**(b) Cell-space moves — implementation matches the arch spec; original
undisturbed.** `solver.py` md5 `aac6f260…` and `config.json` md5
`de2c3fccd…` re-verified byte-identical to the R7-logged hashes — the
fork did NOT touch `code/side-homophonic-rebuild/solver/`. Fork diff
vs original: exactly one additive block (the four cell-move methods,
fork lines 719–781) + the `propose_move` docstring/dispatch table
replacement (block/chg2 branches removed, cell branches added) — no
other line changed, objective byte-identical. Definitions match council
arch §4: alias-reassign (all of c's non-pin groups → c′ atomically),
cell-swap (group-sets exchanged), alias-split (proper nonempty subset
→ new cell), alias-merge (all of c2's non-pin groups → c1); probabilities
0.30/0.10/0.10/0.30/0.10/0.10 sum to 1.00. Pins excluded from every cell
move (`_cell_groups` iterates `self.nonpin` only; `swap` draws from
`nonpin`; a pin-only cell returns None → rejected, not applied).
`block` dropped (justified: contact ≠ alias) and `chg2` dropped
(subsumed by chg1); the dead `no_contact` dispatch fork is gone with
them (the flag survives only in the pre-existing `propose_value`
adjacency path — unchanged behavior). Correctness: proposals are
asymmetric without MH correction, same class as the original move set —
not a violation for a best-state-tracking annealer (R12b, recorded).
Delta computation rides the unchanged snapshot/revert machinery.

**(c) Funnel spec — Branch-A complete and reimplementable; Branch-B
needs re-registration at Stage-2 clearance.** Stage counts
(100/60/40 seeds; 5k climbs; triage 280; ILS 170; 450/instance; 2,700
gate) and seed RNG (`random.Random(2000 + 100*inst_idx + i)`) are
pinned. Variance handling is adequately justified against R7: pilot
cross-pass range ≤ 2 pts (R8a-verified) makes the 40-wide top-40 net
safe for 1-pass triage, and every selection that matters is median-of-3;
the round structure (not the median) is the stated variance control for
ILS neighbors, final winner always median-of-3. CONCERN R12a (binding,
non-blocking for Stage 1): the SELECTED Branch-B pipeline is NOT
re-specified in v2 — §1/§12 say "Stage 4 promoted to primary loop,
seeded from lexicon starts" but give no seed counts, no triage
placement, no judge-call budget, and Stage 1's lexicon-seed
construction is heuristic prose ("crib-inventory drag") rather than
code-pinned. Stage-2 clearance (funnel/gate execution) requires a
re-registered Branch-B pipeline before it runs.

**(d) Judge instrument — acceptance test adequate and a genuine hard
gate.** Test: reproduce the 18 frozen pilot medians within ±3 pts
(truth ~62 / salad ~20 / paraphrase ~91) with mT−mS ≥ 30 on all 6 —
tight against the observed 39–43 margins, and the 54-call (18×3)
protocol is the v1 pilot's own, so cross-pass data comes free. "The
gate does not run without an automated judge instrument" is stated as
a hard precondition (§5), repeated as a binding acceptance (§5), ordered
before the gate (§12), with the SPS trigger armed for two failed
substrate attempts (§9(b)). CONCERN R12d (binding clarification,
non-blocking): the acceptance report must also state single-pass
cross-pass range per candidate (the 1-pass triage assumption is
carried over from the operator pilot; the 18×3 data already contains
the evidence — report it, bound ≤ ~3).

**(e) Additive controls — all present.** (1) memorization probe re-run
on gate truths, 36 calls, non-negotiable before unsealing ✓ (12×3 =
36; R12g: the "6 candidates × ..." parenthetical is garbled prose —
the final figure is right). (2) 2 diplomatic instances as secondary
gate, primary required / secondary believed ✓. (3) noise-mismatch
ablation report-only ✓. (4) q_cycle=0 kept ✓. (5) bars frozen —
CONTROL-DESIGN.md §4 bars restated unchanged ✓. CONCERN R12e (binding,
non-blocking for Stage 1): the gate-truth probe construction requires
READING the fresh truths to write paraphrases, in tension with §10(6)
("NEVER their keys, pclasses, or plaintexts — until Runner scoring").
v2 specifies no containment mechanism. Before Stage-2 clearance, the
probe must name its trusted party: the key-holding Runner/coordinator
constructs and freezes the paraphrases, exposing ONLY the paraphrase
strings to the track pipeline (forensics-class carve-out, logged) —
or a red-team-supervised alternative. v1's probe used already-opened
originals, so this is a NEW gate-time issue.

**(f) R5005 criteria — all five pre-registered, "solved requires all
five" stated** (§8 header: "ALL FIVE; nothing less ships"): board
≥11/12 with all 10 islet-registry rules satisfied (matches arch §6,
incl. the one-provisional red-team carve-out); judge ≥ gate-mean−2σ
AND ≥ 55; topic check ≥ 3 cited period facts; independent
byte-exact reproduction; perturbation ≥ 4/5 topic-survival ✓.

**(g) R8 carry-overs — all honored.** Substitution fallback clause
pre-registered at §6(5) (R8b ✓ — registered in advance, not
improvised); terminology fixed — "npoly=0" appears only in the note
identifying it as a round-1 artifact, prose uses n_poly≈59–61 ✓;
corrected PILOT-REPORT table (R8a fix) cited with the instruction to
cite the corrected table ✓.

**(h) No R5005 contact; fresh seals untouched; deterministic seeds.**
`grep -rniE "r5005|ct_R5005"` over the fork: hits are compliance prose
and forensics documentation only (docstrings, seal_note) — zero data
paths. Experiment 0 read no 184201+ material (verified (a)).
Deterministic seeds logged: build seeds 9091+i; funnel seed RNG
`random.Random(2000 + 100*inst_idx + i)`; judge order fresh-random per
pass as controlled in §4 ✓.

**CONCERN R12b (non-blocking, recorded):** proposal asymmetry (no MH
correction) under the new cell moves is optimizer-irrelevant but the
chain may not be cited as sampling from π ∝ exp(J/T) — no sampler
claims.
**CONCERN R12f** — folded into R12a (lexicon-seed pinning).
**CONCERN R12g (trivial, recorded):** §6(1) probe-call parenthetical
("6 candidates × ...") is garbled; 12×3 = 36 is correct — fix the line.

**Verdict: GO — STAGE 1 ONLY.** Track D is cleared to build the §5
judge instrument and run the binding acceptance test (18 frozen pilot
candidates, ±3-pt median reproduction, mT−mS ≥ 30 all six) — NOTHING
else. The acceptance test must also report per-candidate cross-pass
range (R12d). **STAGE 2 (funnel/gate execution on the fresh instances)
needs a FURTHER, separate clearance after the instrument passes
acceptance** — that clearance will require: (i) the re-registered
Branch-B pipeline (R12a: seed counts, triage placement, judge-call
budget, code-pinned lexicon-start construction); (ii) the gate-truth
probe containment mechanism (R12e); (iii) the logged pre-run
r5005-grep self-check (§10(1)). A gate PASS does NOT authorize R5005
— that remains the parent's call. SPS stays unbuilt while Track D's
funnel is alive (§9 trigger respected).

## Tally
**0 KILL / 0 DEMOTE / 21 CONCERN** (R1; R3a; R3b; R4a; R5a; R5b; R7a;
R7b; R7c; R8a; R8b; R9a; R9b; R10a; R10b; R12a: Branch-B pipeline
underspecified in v2 — seed counts/triage placement/budget/lexicon-start
pinning must be re-registered before Stage-2 clearance, binding,
non-blocking for Stage 1; R12b: proposal asymmetry recorded —
optimizer-irrelevant, no sampler claims; R12c: Experiment 0 probed
(J, old moves) — Branch-B generalization via the J-margin argument,
recorded; R12d: instrument acceptance must report single-pass
cross-pass range, binding clarification, non-blocking; R12e: gate-truth
probe containment mechanism unspecified — trusted-party construction
required before Stage-2 clearance, binding, non-blocking for Stage 1;
R12g: §6(1) call-count parenthetical garbled — 36 = 12×3 correct, fix
the line)
**/ 9 UPHELD** (R2; R3; R4; R5; R7; R8; R9; R10; R11)
**/ 8 GO** (Track C; Track A; Track B; Track D pilot; Track D step-4
[superseded as a pipeline ruling by v2, findings stand]; Track C v3;
Track C v4; **R12: Track D v2 — Stage 1: build the judge instrument +
run the binding acceptance test ONLY; Stage 2 needs further clearance**).
R0 procedural.

### R13 — ADJUDICATION: Track D instrument acceptance test FAILS (2026-10-07)
Red-team reviewer, independent code (`/tmp/redteam_r13_check.py`, no track
imports), scoring against `_KEY_DO_NOT_OPEN.json` used for scoring only.

**(a) Medians recomputed — coordinator's 3/18 CONFIRMED.** 54 log lines =
18 blind labels × 3 passes, zero missing/duplicates. Per-candidate medians
vs the key's expected pilot medians (sorted for comparison):

| class | fresh medians | expected | within ±3 |
|---|---|---|---|
| truth | 25, 25, 25, 25, 30, 30 | 61–64 | **0/6** |
| salad | 20, 20, 25, 25, 25, 25 | 20–22 | 3/6 |
| paraphrase | 100, 100, 100, 100, 100, 100 | 90–93 | **0/6** |

**3/18 within ±3.** Truth is −31..−38 off; paraphrase is +8..+10 off
(ceiling-clamped at 100); salad reproduces within ±5 but only 3 clear
±3. Class medians: truth **25.0**, salad **25.0**, paraphrase **100.0**.

**(b) Per-class + margins — coordinator's numbers CONFIRMED.** Per-seed
(mT, mS, mP, mT−mS): 184101 (30,25,100,5); 184102 (25,20,100,5);
184103 (30,25,100,5); 184104 (25,25,100,0); 184105 (25,20,100,5);
184106 (25,25,100,0). **mT−mS = 5,5,5,0,5,0** — the ≥30 all-six
acceptance bar fails 6/6. Pilot margins were 39–43; the truth>salad
discrimination has collapsed by ~37 points.

**(c) Cross-pass ranges (R12d).** Max 5: four candidates at range 5
(truth [30,30,35] ×2, paraphrase [95,100,100] ×2, salad [20,20,25],
salad [15,20,20]); the other 14 at range 0. Pilot had ≤2. The fresh
judges are *more* within-candidate stable (14/18 at exactly 0) but
the 1-pass triage assumption (range ≤ ~3) is exceeded on 4 candidates;
scores quantize heavily (54 calls → only {15,20,25,30,35,95,100}).

**(d) Protocol compliance — PASS on all four checks.** Prompt sha256
`390a1ec0…c08e21d` asserted in all 54 log entries (recomputed True).
Packages carry blind 8-hex labels only: zero old-label hits across
`judge-pkg-*.json` + all 3 logs; the 18 new labels partition exactly
across the 3 packages (6+6+6, disjoint, union = key's label set).
Mtimes: packages 23:25:33.180–188, key 23:25:33.190, logs 23:26:27–43 —
**packages precede the key** (by 0.5–1.0 s), so key leakage into
packages is temporally ruled out; logs postdate the key but reference
nothing key-like (no `_KEY` mentions, no label-map content). The
acceptance test's integrity controls hold; this is an instrument
failure, not a protocol breach.

**(e) Mechanism diagnosis — coordinator's read CONFIRMED and sharpened.**
Fresh-judge justifications, quoted verbatim:

- truth: agent1 — "Scattered French words and fragments appear amid
  heavy garbling, but none of it reads as coherent French prose";
  agent2 (all six truths, near-canned): "The passage is mostly
  non-French letter noise with scattered French-like fragments"
  (alternating "letter soup"); agent3 — "This is adversarially
  garbled noise with French-like syllables throughout but no
  coherent French words or phrases."
- salad: "The text is overwhelmingly garbled repetition of
  non-words"; "mostly non-French repetitive letter noise";
  "repetitive non-French noise with scattered French-like fragments."
- paraphrase: "flawless, natural literary French prose with perfect
  grammar and style" → 95–100.

The cold judges perceive BOTH degraded classes as ~25-grade letter
noise and respond to surface fluency only (spacing/punctuation →
100). The pilot's 61–64 truth scores required reading *through* the
spaceless ear-noise to embedded French — a reading three independent
fresh instances do not reach. All three converge on the same attractor
(25–30 truth, 20–25 salad, 100 paraphrase), so this is a systematic
calibration difference, not random variance; the pilot is the
outlier. Note the prompt's own "adversarially constructed" anchor
echoing back in agent3's justifications — the low-end anchor is being
read as a *description of the stimulus* (truth decode) rather than a
scale reference, dragging degraded text into the ~25 bucket.

**(f) Operator bias vs cold-start calibration.** The evidence supports
**cold-start calibration failure as primary**, with R7a operator bias
directionally consistent but not separable. Why not pure steering: the
pilot's scores were stable (range ≤2), the prompt was hash-frozen
throughout, extraction was mechanical, and the pilot's own
justifications show the operator *saw* the degradation ("penalized
for missing word boundaries and by-ear spellings") yet scored 61–64
*despite* it — i.e. the operator read embedded French words; the
fresh judges report "no coherent French words or phrases." R7a's
class-identifiability (operator authored the classes, had 184101
fragment exposure) remains a plausible amplifier: a judge who knows
the lane structure can charitably up-score recognizable truth. But
the decisive point does not depend on adjudicating this: the gate's
judge MUST be a fresh, lane-naive instance, and three fresh instances
unanimously fail to discriminate. Whichever mechanism explains the
pilot, the pilot's number is non-transferable.

**(g) THE PILOT QUESTION — two readings, ruled explicitly.**
- (i) Within-operator capability proof: **STANDS.** The pilot log
  demonstrates that at least one judge instance, under the frozen
  prompt, separated truth from salad by 39–43 pts with clean
  protocol (R8 verified byte-exact; no extraction error, no prompt
  change, no mislabeling). The capability exists in some instances.
- (ii) Gate-usable instrument: **FAILS — explicitly VOID.** The
  acceptance test's entire purpose was transferability; 3/18
  replication and margins collapsing 39–43 → 0–5 proves the
  instrument does not transfer across instances. A gate needs a
  judge that works for the instance actually doing the judging, not
  the one that piloted it. R7's 6/6 stands as (i) and is void as
  (ii).

**Consequence: the R8 step-4 clearance cannot be exercised.** R8's
findings (protocol, substitution, clean probe) remain verified; the
forward permission dies with the instrument. Stage 2 requires a
*passing* instrument — this one failed.

**(h) Repair recommendation (ordered).**
1. **Prompt repair ladder** (each = re-registration + new pilot on the
   frozen 18 + new acceptance test on fresh instances + red-team
   review; and per this ruling, **pilot and acceptance populations
   must coincide — the acceptance test has proven the pilot
   instance is not representative**):
   - **Repair A — degradation-robust instructions (first choice).**
     Replace holistic fluency scoring with countable evidence:
     "list the French words/phrases you can identify; score from the
     count and quality of identifiable French lexical material."
     Attacks the observed failure directly: cold judges currently
     collapse spaceless text to noise because they never attempt
     segmentation; listing forces the attempt.
   - **Repair B — anchored calibration.** Prepend scored exemplars
     (one truth-class, one salad-class, one paraphrase-class with
     scores) to fix the scale anchors that cold judges currently
     set from surface features.
   - **Repair C — pairwise preference protocol.** Replace absolute
     0–100 with forced choice ("which of these two is more French?")
     over the truth/salad pair — sidesteps absolute calibration
     entirely; discrimination is the actual requirement.
2. **SPS fallback trigger status:** PREREG-D-v2 §9(b) arms the trigger
   for **two failed substrate attempts**. This is the **first failed
   substrate attempt** (the acceptance test tested the pilot
   substrate's transfer; it is not a second, independent substrate).
   The trigger is NOT yet met by count — but the pilot→gate transfer
   failure is precisely the condition the trigger exists for.
   **Record this as strike one.** Sequence: repair pilot → new
   acceptance; if that also fails → second substrate failure →
   **SPS trigger met** (structural fallback per arch §7, e.g.
   dependency-parse syntactic features, exactly the family R11
   named as Track C's successor).
3. **Funnel without a working judge: NO.** Stated plainly: nothing in
   the funnel can proceed. R12(d) bound the gate on the automated
   judge instrument as a **hard precondition**, and PREREG-D-v2 §5
   states "the gate does not run without an automated judge
   instrument." Anneal endpoints are undiscriminable under J
   (Experiment 0: 2,601-nat salad margin at chance-level recovery),
   and there is no judge to rank them instead. Triage (280),
   ILS (170), 450/instance — all are judge-mediated selections;
   running them on J-climb endpoints is declared dead by the
   Branch-B ruling itself. The honest options are: repair the judge
   (step 1), or trigger the SPS structural fallback after the
   second failed substrate attempt (step 2). No partial proceed.

**Verdict: R13 recorded — acceptance test FAILS (3/18 ±3, margins
0–5 vs ≥30 bar). R8's step-4 clearance is frozen pending a passing
instrument. Pilot stands as (i), void as (ii).**

## Tally
**0 KILL / 0 DEMOTE / 22 CONCERN** (R1; R3a; R3b; R4a; R5a; R5b; R7a;
R7b; R7c; R8a; R8b; R9a; R9b; R10a; R10b; R12a: Branch-B pipeline
underspecified in v2 — seed counts/triage placement/budget/lexicon-start
pinning must be re-registered before Stage-2 clearance, binding,
non-blocking for Stage 1; R12b: proposal asymmetry recorded —
optimizer-irrelevant, no sampler claims; R12c: Experiment 0 probed
(J, old moves) — Branch-B generalization via the J-margin argument,
recorded; R12d: instrument acceptance must report single-pass
cross-pass range, binding clarification, non-blocking; R12e: gate-truth
probe containment mechanism unspecified — trusted-party construction
required before Stage-2 clearance, binding, non-blocking for Stage 1;
R12g: §6(1) call-count parenthetical garbled — 36 = 12×3 correct, fix
the line; R13: pilot/acceptance population mismatch — future repairs
must pilot and accept on the same (fresh, lane-naive) judge
population; pilot instance proven non-representative, recorded)
**/ 9 UPHELD** (R2; R3; R4; R5; R7; R8; R9; R10; R11)
**/ 8 GO** (Track C; Track A; Track B; Track D pilot; Track D step-4
[superseded as a pipeline ruling by v2, findings stand; **exercisability
frozen by R13 pending a passing instrument**]; Track C v3; Track C v4;
**R12: Track D v2 — Stage 1: build the judge instrument + run the
binding acceptance test ONLY; Stage 2 needs further clearance**).
R0 procedural.

### R15 — GO: Track D PREREG-D-v3 repair ladder signed off (2026-10-07)
Reviewed `track-d/PREREG-D-v3-ladder.md` + `prompt-v3A.txt` +
`prompt-v3B.txt` + `prompt-v3C.txt` against the review checklist.
Independent verification (shell/sha256/grep, no track imports):

**(a) Genuine repairs — PASS, all three are substantively different.**
- **v3A** is a genuine change of the judgment task, not a rephrasing:
  the frozen prompt asked for holistic "FRENCHNESS" of prose; v3A
  asks for a SCAN (mandatory line-2 word list) then scoring from the
  count/quality of recovered lexical material, with "do NOT judge
  holistic prose fluency" stated explicitly. This attacks the R13(e)
  mechanism head-on — the cold judges collapsed spaceless text to
  noise because they never attempted segmentation, and the mandatory
  listing forces the attempt. A null segmentation is now checkable
  in the log (line 2 = NONE), which the v2 instrument could not
  distinguish from a skipped attempt.
- **v3B** keeps the frozen v2 prompt verbatim (wording/scale/format
  confirmed identical below the exemplar block) and prepends three
  scored synthetic anchors (21 salad-class, 61 degraded-truth-class,
  91 clean). This attacks the observed anchor drift: R13(e) showed
  the low-end anchor read as a stimulus description. The agent's own
  flagged risk ("spaceless ≈ 20") is real but bounded: the exemplars
  teach spaceless-salad ≈ 21 AND spaceless-truth ≈ 61 — they draw
  the distinction, not a flat rule. The residual risk is anchor
  pull toward 61 on degraded truth; that is exactly what the
  median(truth) ≥ 50 bar plus the margin bar will price honestly —
  a rung-B pass at truth ≈ 55 / salad ≈ 25 fails the ≥30 margin,
  so anchor-smeared non-discrimination cannot masquerade as a pass.
- **v3C** genuinely sidesteps absolute calibration: forced choice
  of which passage contains MORE French, ties forbidden, confidence
  0–100 logged but not gated. Discrimination is the actual gate
  requirement, so this is the purest repair of the three — it
  cannot inherit the R13 collapse because it never asks for a
  number on the same scale. The pairing (all 36 truth×salad pairs,
  3 position-randomized passes, 12 pairs per judge, per-pair
  majority) is fully specified.
Ranking A→B→C is defensible: A tries to fix the mechanism within the
absolute frame; B fixes calibration if the mechanism is fine but the
scale is broken; C abandons the absolute frame entirely.

**(b) Contamination — PASS, the claim is credible.**
Exemplar B verbatim string: 0 hits in `candidates.json`.
Distinctive synthetic fragments (`dimanchmatin`, `soleyeklerait`,
`sanfanjuaient`, `predelafonten`, `lesklochsonaient`): 0 hits each.
Example A (`brkvz…` noise) and Example C (`se levait sur la ville`):
0 hits each. The variants contain no test-set content; they are
consistent with being written from the R13 failure analysis (judge
justifications), as the header claims. If any variant had leaked
test content it would have been killed — none did.

**(c) Pass criteria — ACCEPTED with wording correction R15c.**
- *mT−mS ≥ 30 on 6/6* carried from v2 §5: correct — R13 voided the
  instrument, not the bar; transferability is the acceptance test's
  purpose.
- *median(truth) ≥ 50*: justified. The R13 signature was truth
  collapsing INTO the salad band (25 vs 25); a margin-only criterion
  admits truth 30 / salad 0. The floor requires the mechanism
  repair (reading through degradation). Arithmetic note (R15c,
  non-blocking wording): 50 is NOT exactly the midpoint of the
  collapse band (~25) and pilot band (61–64) — that midpoint is
  ~43.5. ≥50 is *above* the midpoint, i.e. it demands the instrument
  land unambiguously nearer the pilot's reading than the collapse
  state. The justification holds on those terms; hedge the
  "halfway" phrasing.
- *≥35/36 for C*: correct as the pairwise analogue of 6/6 —
  full truth>salad separation with ≤1 flipped pair as noise margin.
  A genuinely discriminating instrument (pilot-style, 39–43 pt
  margins) should win all 36; the bar is strict but not
  over-strict.

**(d) Sequential trial honesty — PASS, no Bonferroni required.**
A→B→C with stop-at-first-pass on the frozen 18 does inflate the
any-rung-false-pass rate relative to a single test (union ≤ 3α).
But the per-rung criterion is stringent under the null: a
non-discriminating instrument must systematically score all 6
truths ≥50 while holding all 6 salads ≥30 below them — a
~25–30-point systematic shift, not sampling noise (the R13 null
gave margins 0–5). α is negligible per rung, so 3α remains
negligible; the rung order is pre-registered (A as the agent's
first choice), so there is no post-hoc selection among rungs.
Sequential pre-registered repair ladders are the honest form of
this trialing; requiring multiplicity correction would punish
honesty about the ordering. Recorded as reviewed-and-accepted.

**(e) Population coincidence — PASS (protocol binds it; repair agent
clean).** §2(1): three fresh, lane-naive judges per rung, never the
repair agent; §2(3): new blind labels per rung with the mechanical
zero-old-label check; §2(4): 3 passes. The repair agent did no
judging: no log or jsonl anywhere under `track-d/` contains any of
the three v3 prompt sha256s; the only judge artifacts post-dating
the ladder are the R13 acceptance campaign itself
(`instrument/runs/20261007-233304/`, written 23:33, before the
ladder doc at 23:34) — that campaign judged under the frozen v2
prompt, not the v3 variants. Population-coincidence requirement
from R13(h)(1) is correctly implemented: the fresh judges'
campaign IS both pilot and acceptance — no operator pilot, ever
again.

**(f) Strike framework — CORRECT and explicit.** §0 + §4: all three
rungs fail → strike two recorded → SPS trigger (PREREG-D-v2 §9(b)
condition (b): "no viable judge instrument after two substrate
attempts") is MET → SPS re-registers as an instrument before any
gate-instance contact. This matches R13(h)(2)'s sequencing: the
ladder as a whole is the second substrate attempt; per-rung
failure diagnosis (§4, rung report before the next rung) is
ordered and preserves the R13-style failure-analysis discipline.
"Nothing in the funnel proceeds without a passing instrument"
restated — consistent with R13's frozen step-4 clearance.

**(g) Logger note — BINDING CLARIFICATION R15a (non-blocking).**
The v3 logger replacing `judge_driver.log_judgment`'s
single-line-justification assertion is an implementation detail
with binding consequences: v3A's entire auditability (the line-2
word list) depends on line-2 payloads being stored. Before rung
A's trial runs, the v3 logger must be specified and pinned: the
exact log schema, the mechanical parse rule for line 2
(comma-separated list or NONE; no score derived from line 2),
and storage of full raw responses. Red team audits per §2(6)
before the verdict; a logger that drops or re-interprets line 2
voids the rung.

**(h) No R5005 contact; frozen prompt untouched — VERIFIED.**
`grep -rniE "r5005|ct_R5005"` over the ladder doc + three prompts:
hits only in `PREREG-D-v3-ladder.md` compliance prose ("no R5005
contact", "Deterministic; no R5005 contact", seal note) — zero
data paths. Frozen `judge_prompt.txt` sha256 recomputed:
`390a1ec0bf1aa9e0e495a5fe98e65107c41025c954cd11b68d1931816c08e21d`
— **byte-identical** to the R7/R8-logged hash. The frozen
instrument is undisturbed.

**Variant hashes recorded for the §2(2) startup assertions:**
- prompt-v3A.txt: `84393ae4c5f702f218841636871715e84f790be524d3e380bf4fb283f1fcd85e`
- prompt-v3B.txt: `92d2f3e6fa87f2ba6910824d05019f3bb542373e86ddeaab5eaca5a52bb7a1b1`
- prompt-v3C.txt: `d907c59202c9d38e5dfe10bf8048c869bcba2fb547631c02ceb34f93b5b2615e`

**CONCERN R15b (binding, non-blocking — must be pinned before rung
C runs):** rung C's invalid-output handling is underspecified. Line 1
must equal a pair label verbatim; line 2 must be an integer. A judge
emitting a wrong label, a non-integer confidence, or a hedge can
produce a 1–1 or 0–0 vote split with no majority. Pre-register before
the C trial: the exact invalid-output rule (e.g. EXTRACTION-FAILED →
excluded from that pair's tally; per-pair majority over valid votes
with minimum 2 valid votes, else the pair is VOID and re-judged by
a fresh instance — not by the same judge re-queried). No ad-hoc
handling at verdict time.

**CONCERN R15c (non-blocking, wording):** §3's "50 sits halfway
between the observed salad band (~25) and the pilot truth band
(61–64)" — the true midpoint is ~43.5; 50 is stricter than the
midpoint. The ≥50 bar is defensible as demanding the instrument
land unambiguously nearer pilot than collapse; hedge the
"halfway" phrasing to that claim.

**Verdict: GO — rung A cleared.** Trial protocol (binding):
1. **Three fresh, lane-naive LM instances** as judges for rung A.
   Never the repair agent, never the pilot operator, never any
   instance that has seen `candidates.json` plaintexts or the R13 key.
2. **New blind labels** for the frozen 18 (fresh 8-hex, mechanical
   zero-old-label check across packages/logs as in R13(d));
   packages precede the key temporally; logs reference nothing
   key-like.
3. **prompt-v3A.txt at the R15-logged sha256** (`84393ae4…cd85e`):
   hash asserted at judge startup, abort on mismatch.
4. **3 passes**, frozen 18 × 3 = 54 calls, 6+6+6 per judge, fresh
   random order per pass; the R15a v3 logger spec pinned before
   trial, full raw responses + line-2 word lists stored.
5. **PASS iff mT−mS ≥ 30 on 6/6 AND median(truth) ≥ 50**; the
   void-probe diagnostic (median(paraphrase) ≤ median(salad) →
   scale broken) recorded non-binding; cross-pass range per
   candidate reported (R12d carry-over).
6. Red-team audit of campaign integrity (sha256 assertions, label
   blindness, temporal key ordering, log schema) before the
   pass/fail verdict is declared.
**Rungs B/C are sequenced after:** each subsequent rung needs only
a brief continue-ruling (not a full re-review) unless the variant
is modified — but R15a's logger spec carries to B (line-2 storage)
and R15b must be resolved before C runs. A rung FAIL requires the
§4 rung report (judge justifications in their own words) before the
next rung. A rung PASS clears strike one and re-requests step-4
clearance on the accepted instrument. All-three-fail → strike two,
SPS trigger MET.

## Tally
**0 KILL / 0 DEMOTE / 25 CONCERN** (R1; R3a; R3b; R4a; R5a; R5b; R7a;
R7b; R7c; R8a; R8b; R9a; R9b; R10a; R10b; R12a: Branch-B pipeline
underspecified in v2 — seed counts/triage placement/budget/lexicon-start
pinning must be re-registered before Stage-2 clearance, binding,
non-blocking for Stage 1; R12b: proposal asymmetry recorded —
optimizer-irrelevant, no sampler claims; R12c: Experiment 0 probed
(J, old moves) — Branch-B generalization via the J-margin argument,
recorded; R12d: instrument acceptance must report single-pass
cross-pass range, binding clarification, non-blocking; R12e: gate-truth
probe containment mechanism unspecified — trusted-party construction
required before Stage-2 clearance, binding, non-blocking for Stage 1;
R12g: §6(1) call-count parenthetical garbled — 36 = 12×3 correct, fix
the line; R13: pilot/acceptance population mismatch — future repairs
must pilot and accept on the same (fresh, lane-naive) judge
population; pilot instance proven non-representative, recorded;
R15a: v3 logger line-2 storage spec must be pinned before rung A
trial (schema + mechanical parse, audited per §2(6)), binding,
non-blocking; R15b: rung C invalid-output handling (vote splits,
re-judge rule) must be pre-registered before the C trial, binding,
non-blocking; R15c: §3 "halfway" wording — ≥50 is stricter than the
~43.5 midpoint; justification holds as "unambiguously nearer pilot
than collapse", hedge the phrasing)
**/ 10 UPHELD** (R2; R3; R4; R5; R7; R8; R9; R10; R11; R15: Track D
v3 repair ladder meets the checklist — genuine repairs, no test-set
contamination, stringent joint criterion, honest sequential design,
population coincidence bound, strike framework correct, frozen v2
prompt byte-identical)
**/ 9 GO** (Track C; Track A; Track B; Track D pilot; Track D step-4
[superseded as a pipeline ruling by v2, findings stand; **exercisability
frozen by R13 pending a passing instrument**]; Track C v3; Track C v4;
**R12: Track D v2 — Stage 1: build the judge instrument + run the
binding acceptance test ONLY; Stage 2 needs further clearance**;
**R15: Track D v3 rung A — 3 fresh judges on the frozen 18 under
prompt-v3A (84393ae4…cd85e), 54 calls, PASS iff mT−mS ≥ 30 on 6/6
AND median(truth) ≥ 50; rungs B/C sequenced after with brief
continue-rulings; R15a logger spec pre-trial, R15b pinned before C**).
R0 procedural.

### R14 — GO: Track D PREREG-D-v2-branchB signed off (2026-10-07)
Red-team reviewer. Reviewed `track-d/PREREG-D-v2-branchB.md` (346 lines,
written 2026-10-07 23:28) against `track-d/PREREG-D-v2.md`, R12 (esp.
R12a/R12d/R12e) and R13. Independent verification (shell/python, no
track imports): budget arithmetic; seed-stream pairwise distinctness;
lexicon file (`lm_ref/lm.json`: 3,546 entries, wt descending,
3–6-char pool = 200 — reproduced); `load_inventory(mode, pins, soft,
lex_wt)` signature matches the spec's call; acceptance-log structure
(54 = 18 labels × 3 passes, frozen prompt sha256 on all 54);
R5005/fresh-seal greps over `track-d/`; no gate artifacts; no Branch-B
implementation on disk.

**(a) R12a compliance — PASS.** All four binding items pinned to
reimplementation level: (1) seed counts 72 lexicon + 48 crib-extended =
120/instance (§1); pure-random dropped with Experiment-0 justification
("a pure-random start is a lexicon start with the word-bearing
structure removed"); the 100/60/40 split explicitly not carried.
(2) triage placement 120×1 → top-48×2 → median-of-3 → top-8 parents =
216 calls (§2); the Branch-A 280-call triage declared dead with reason
(its J-climb endpoints are gone). (3) budget 496/instance, 2,976 gate,
36 probe, 3,012 program — arithmetic verified (120+96+256+24=496;
×6=2,976; +36=3,012); +10% vs Branch A justified (the ~37-min/instance
J-climb compute stage deleted; reinvested in a 4th ILS round, 8
parents vs 5, 256 vs 170 neighbor evals). (4) lexicon-start
construction fully algorithmic (§1a/§1b): word pool, deterministic
longest-match tiling (length-desc, lexicographic-asc), frequency-biased
window sampling (mean group-freq ≥ instance median, 10-draw resample),
first-assignment-wins conflict rule (pins never overwritten,
conflicting words skipped whole), RNG seeds `3000+100·inst+i` /
`5000+100·inst+i` / `7000+10000·inst+100·r+n` (all 1,536 ILS seeds
verified pairwise distinct; no cross-stage collisions).
**CONCERN R14a (non-blocking):** §1a "place up to 12 words (stop early
at 12), over 8 windows" — one word per window ⇒ at most 8 words; the
"12" cap never binds. Deterministic as written; fix the number or the
loop description before implementation.

**(b) ILS loop — PASS.** 4 rounds × 8 parents × 8 neighbors = 256
(1 pass each) + final top-12 × 2 = 24; mutation-count distribution
{1:0.50, 2:0.30, 3:0.20}; fork proposal probabilities pinned and
summing to 1.00 (chg1 0.30 / swap 0.10 / poly 0.10 / alias-reassign
0.30 / cell-swap 0.10 / alias-split 0.05 / alias-merge 0.05); pins
excluded from every touched set; a no-op draw re-drawn ≤5 times, then
that mutation slot skipped; parent selection argtop8 over the
72-candidate pool by (score, J, −index), tie-break higher score →
higher J → lower candidate index.
**CONCERN R14b (binding, non-blocking):** three determinism gaps to
pin at implementation and log — (i) the n↔(parent, neighbor) ordering
for n=0..63 is unpinned ("8 parents × 8"); (ii) the third-level
tie-break "candidate index" is undefined across the mixed
parent/neighbor pool; (iii) the final "median-of-3": carried parents
hold 5 valid passes after the +2 — bound to §4's "median of valid
queries" (median over ALL valid passes; "median-of-3" names the
minimum-evidence design, not a truncation).

**(c) Variance justification — PASS, conditionally.** 1-pass for
triage pass-1 and in-round neighbor ranking; median-of-3 for parent
selection (parents carry medians forward — a noisy promotion would
compound over 4 rounds) and for the final winner; argued from the
≤2-pt operator-pilot cross-pass range (R8a, 18/18). The 48/120 = 40%
triage net and the 8-of-72 parent cut have real slack against ≤2-pt
noise.
**CONCERN R14c (binding, non-blocking):** "cannot lose a
truth-adjacent start to noise" overstates (improbable, not
impossible) — and R13(c) shows fresh judges hit cross-pass range 5
on 4/18. The §3 variance justification therefore stands ONLY for an
instrument whose acceptance-reported cross-pass range is ≤3 on the
acceptance population (R12d already requires the report); a repaired
instrument showing range >3 must re-register the 1-pass stages before
any gate.

**(d) Stage-2 entry criteria — PASS (the spec handles the failed
instrument correctly).** §6 is a hard AND: (1) instrument acceptance
PASS, (2) this red-team clearance, (3) logged pre-run grep
self-check with self-KILL on any data hit. The acceptance FAILED —
independently recomputed from the 54-call logs: 15/18 candidates
outside ±3 pts of the v1 pilot medians (truth 25–30 vs 61–64;
paraphrase 100 vs 90–92; salad 3/6 within; mT−mS 0–5 vs the ≥30 bar),
EXACTLY matching R13's 3/18-within-tolerance adjudication. §6(1) is
unmet → Stage 2 is BLOCKED, and R13(h)(3) concurs ("nothing in the
funnel can proceed"). The failure path is complete: §7(2) → R13
strike-one → exactly one repair attempt → SPS on second failure.
**CONCERN R14d (non-blocking):** the §6(3) "zero data hits"
self-check needs human classification — 8 files in `track-d/` carry
r5005 hits, all verified compliance prose/docstrings/self-check
code, zero data paths; the self-check log must record hit lines
verbatim so the classification is auditable. Note for R13's record
(not this spec's): the acceptance ran as 3 agents × 6 candidates × 3
passes — each candidate's 3 passes came from a single agent, weaker
independence than v2 §5(a)'s "fresh LM instances per call".

**(e) SPS trigger — PASS, with binding tightening.** §7 fires ONCE on
(1) gate FAIL after the full budget spent exactly as pre-registered
(496/instance; 2,976 gate; 36 probe) — "no additional judge calls, no
re-seeding, no extra ILS rounds, no re-registration of the bars are
authorized after a FAIL" — or (2) no viable instrument after two
substrate attempts ((a) subagent-judges, then (b) a local/API LM
endpoint, in that order; each documented with 54-call acceptance
numbers); not re-armed; exactly one full-budget gate run; SPS not
built speculatively while the funnel is alive; gate PASS ≠ R5005
authorization (the parent's call).
**CONCERN R14e (binding, non-blocking):** R13 records the failed
acceptance as strike one and prescribes the repair-ladder attempt
(repaired prompt + coincident fresh pilot/acceptance populations +
red-team review) as the next step, while branchB §7(2) names
substrate (b) as the second attempt. Bound: the track gets EXACTLY
ONE further instrument attempt and must pre-register WHICH one it is
(the R13 repair attempt OR §7(2)(b)) before running it; a second
failure fires SPS; re-running a failed configuration and counting it
as a "new attempt" is barred. This keeps the trigger airtight against
"try harder" end-runs under either reading.

**(f) Additive controls — PASS.** Gate-truth probe 36 = 12×3 (R12g
correction applied) with R12e containment: the key-holding
Runner/coordinator — not the track pipeline — constructs and freezes
the paraphrases (sha256 logged) BEFORE any track unsealing; the track
sees only strings; forensics-class carve-out logged — the containment
R12e required, resolving the v2 §10(6) tension. Diplomatic secondary
gate (2×496), noise-mismatch ablation (2×496, report-only),
q_cycle=0 (184213–184218 stands), bars frozen (PRIMARY mean ≥0.20 /
min ≥0.10; SECONDARY mean ≥0.30 / min ≥0.22) — all present.
**CONCERN R14f (binding, non-blocking):** §5(1)'s "the track sees
ONLY the paraphrase strings" is under-specified — the probe's 12
candidates include 6 gate-truth decodes (mT−mP needs mT), which the
track cannot derive without reading keys. Bound: the key-holder
supplies ALL 12 candidate strings as opaque blind-labeled inputs
(frozen, sha256 logged); the track must not derive truth decodes
from keys. Settle before the probe runs.

**(g) No execution — UPHELD.** No gate anneals (no `gate_runs/`, no
`gate_answers`); no judge calls under this spec (the 54 acceptance
calls ran 23:26 under R12 Stage-1, before this spec file existed at
23:28); no Branch-B implementation on disk (no lexicon-seed/ILS
builders; `instrument/` holds only the Stage-1 judge instrument);
R5005 grep over `track-d/`: hits in 8 files, all compliance
prose/docstrings/self-check code — zero data paths; fresh-seal
mentions (184201–184204/184206/184207, 184213–184218) are prose
only; acceptance packages contain exactly the 18 v1 pilot texts
(0 unmatched by byte-exact text match) — no fresh-seal contact;
deterministic seeds pinned.

**(h) Consistency — UPHELD.** No contradiction with v2 outside the
declared Branch-A/B fork (seed counts, triage placement, budget,
pipeline — the fork R12(a) endorsed and R12a required re-registered;
v2's Branch-A §3 design is untouched in its file). Carried verbatim:
frozen prompt sha256; judge protocol (blind 8-hex labels, mechanical
first-line-int extraction, `judge_log.jsonl`, median-of-valid,
<2-valid → VOID); bars; the R8b substitution fallback (§5(5) cites v2
§6(5) verbatim); R8 terminology (no `npoly=0` anywhere in the file);
the grep self-check; both SPS arms; gate PASS ≠ R5005 authorization;
v2 §10(6) via the §5(1) containment.

**Verdict: GO.** PREREG-D-v2-branchB.md is cleared as the binding
Branch-B pipeline specification. **THIS GO DOES NOT AUTHORIZE
STAGE-2 EXECUTION.** Stage 2 requires all three §6 conditions:
(1) instrument acceptance PASS — currently FAILED (R13: 3/18 within
±3, margins 0–5 vs the ≥30 bar; R8's step-4 clearance frozen);
exactly one repair attempt remains per R14e, then SPS fires on a
second failure; (2) this R14 clearance — GRANTED; (3) logged pre-run
grep self-check with self-KILL on any data hit.

## Tally
**0 KILL / 0 DEMOTE / 28 CONCERN** (R1; R3a; R3b; R4a; R5a; R5b; R7a;
R7b; R7c; R8a; R8b; R9a; R9b; R10a; R10b; R12a: Branch-B pipeline
underspecified in v2 — seed counts/triage placement/budget/lexicon-start
pinning must be re-registered before Stage-2 clearance, binding,
non-blocking for Stage 1; R12b: proposal asymmetry recorded —
optimizer-irrelevant, no sampler claims; R12c: Experiment 0 probed
(J, old moves) — Branch-B generalization via the J-margin argument,
recorded; R12d: instrument acceptance must report single-pass
cross-pass range, binding clarification, non-blocking; R12e: gate-truth
probe containment mechanism unspecified — trusted-party construction
required before Stage-2 clearance, binding, non-blocking for Stage 1;
R12g: §6(1) call-count parenthetical garbled — 36 = 12×3 correct, fix
the line; R13: pilot/acceptance population mismatch — future repairs
must pilot and accept on the same (fresh, lane-naive) judge
population; pilot instance proven non-representative, recorded;
R14a: §1a "up to 12 words over 8 windows" — one word per window ⇒ ≤8
words; the "12" cap never binds; deterministic as written, fix before
implementation, non-blocking; R14b: ILS determinism gaps —
n↔(parent, neighbor) ordering, cross-pool "candidate index", final
median over ALL valid passes per §4 — pin at implementation and log,
binding, non-blocking; R14c: §3 variance justification stands only
for an instrument with acceptance-reported cross-pass range ≤3;
"cannot lose to noise" overstates; range >3 ⇒ re-register the 1-pass
stages, binding, non-blocking; R14d: §6(3) self-check "zero data
hits" needs human classification — log hit lines verbatim for
auditability; acceptance ran 3 agents × 6 candidates × 3 passes
(weaker pass independence than v2 §5(a)), non-blocking; R14e: exactly
ONE further instrument attempt authorized — track must pre-register
WHICH (R13 repair attempt OR §7(2)(b)); second failure fires SPS;
re-running a failed configuration as a "new attempt" barred, binding,
non-blocking; R14f: gate-truth probe — key-holder supplies ALL 12
candidate strings as opaque blind-labeled inputs (frozen, sha256);
track must not derive truth decodes from keys, binding, non-blocking)
**/ 9 UPHELD** (R2; R3; R4; R5; R7; R8; R9; R10; R11)
**/ 9 GO** (Track C; Track A; Track B; Track D pilot; Track D step-4
[superseded as a pipeline ruling by v2, findings stand; **exercisability
frozen by R13 pending a passing instrument**]; Track C v3; Track C v4;
**R12: Track D v2 — Stage 1: build the judge instrument +
run the binding acceptance test ONLY; Stage 2 needs further clearance**;
**R14: Track D PREREG-D-v2-branchB — binding Branch-B pipeline spec
cleared; Stage 2 NOT authorized (needs instrument acceptance PASS +
logged grep self-check)**). R0 procedural.

### R16 — AUDIT: Track D rung-A (prompt-v3A) campaign-integrity audit — INTEGRITY FAIL, scoped (2026-10-07)
Per PREREG-D-v3-ladder §2(6). Mechanical audit only (own code, no track
imports; `candidates.json` plaintexts not opened). **Verdict: INTEGRITY
FAIL — scoped to check 5 (score arithmetic).** Checks 1–4 PASS; no
blindness, protocol, or key-ordering breach found.

1. **sha256 — PASS.** `prompt-v3A.txt` on disk hashes to
`84393ae4c5f702f218841636871715e84f790be524d3e380bf4fb283f1fcd85e`;
all 54 log records (18/judge) carry that value.
2. **Label blindness — PASS.** 18 rung-A labels fresh 8-hex, distinct;
zero overlap with the 36 prior labels (18 `label_map.json` keys + 18
`instrument-acceptance/judge-pkg-{1,2,3}.json` labels; `_KEY_V3A` old
labels coincide with the `label_map` keys). Grep over the 3 packages +
54 log records: no old-label string, no 'truth'/'salad'/'paraphrase',
no seed numbers in any `raw_response`. Coverage: 18 labels × 3 passes,
exactly one judge per label.
3. **Temporal key ordering — PASS.** Packages written before
`_KEY_V3A_DO_NOT_OPEN.json` (23:37:08 vs 23:37:08, key mtime strictly
later at float precision); key is a clean bijection (new == package
labels, old == `label_map` keys, 18 distinct). Logs reference nothing
key-like.
4. **Judge protocol — PASS.** 54 records, 18/judge, 6+6+6 passes per
judge; exact 8-field schema per v3-logger-pin.md; on all 54 records
`extracted_score == int(line 1)`, `word_list == line 2`,
`justification == lines 3+` verbatim, zero mismatches.
5. **Score arithmetic — FAIL.** Per-seed medians in RUNG-A-REPORT.md do
not recompute from the logs + key + `label_map.json`. Recomputed
(mT, mS, margin): 184101 (65,45,20); 184102 (62,45,17);
184103 (68,44,24); 184104 (65,45,20); 184105 (65,51,14);
184106 (68,45,23). Report claims (68,62,6); (62,35,28); (68,44,24);
(62,45,17); (65,51,14); (68,35,33) — 4 of 6 rows differ. The report's
required salad medians (62, 35, 35) do not exist in the logs (actual
salad cells: 45,45,44,45,51,45), so the table is unproducible under ANY
label→(seed,class) permutation. Report mtime (23:43:19) is after the
last log (23:43:06) → scoring error in the report, not a log rewrite.
Aggregates: median(truth) recomputes 65.0 not 66; median(salad) 45.0
not 45.5; median(paraphrase) 98 confirmed.

**Consequence.** The "1/6 seeds pass (184106 PASS, margin 33)" claim is
VOID; corrected margins are 20/17/24/20/14/23 → **0/6 ≥ 30**. Verdict
DIRECTION unchanged (RUNG A FAILS — fail confirmed, strike one stands),
but the formal verdict CANNOT be declared until RUNG-A-REPORT.md's
per-seed table and aggregates are corrected and the correction
re-audited. This is a reporting error, not a campaign breach — no
unblinding or protocol violation was found, so rung B may proceed per
ladder §4 once the corrected rung-A report passes re-audit (paperwork
re-check, not a re-run).

## Tally
**0 KILL / 0 DEMOTE / 27 CONCERN** (R1; R3a; R3b; R4a; R5a; R5b; R7a;
R7b; R7c; R8a; R8b; R9a; R9b; R10a; R10b; R12a; R12b; R12c; R12d; R12e;
R12g; R13; R14a; R14b; R14c; R14d; R14e; R14f; R15b; R15c;
**R16: rung-A campaign mechanics clean (sha/blindness/key-order/protocol
PASS), but RUNG-A-REPORT.md's per-seed table did not recompute from the
logs — 4/6 rows differed, required salad medians 62/35/35 absent from the
data; "184106 PASS" voided, corrected 0/6 ≥ 30; verdict declaration
BLOCKED pending corrected table + re-audit; fail direction confirmed,
strike one stood — NOW RESOLVED by R16a below; retained here as the
historical record**;
**R17: rung-B campaign mechanics clean (sha/blindness/key-order/mapping-
chain/log-schema PASS; builder's stale table is a documentation defect
only, no stale artifact on disk), but RUNG-B-REPORT.md's per-seed table
does not recompute from the logs — 6/6 rows differ, numbers 52 and 58
absent from all 54 logs (unproducible under any permutation); "3/6 pass"
void, corrected 2/6 ≥ 30 (margins 34/8/−1/−1/30/−3), median(truth) 26.0
not 35; verdict declaration BLOCKED pending corrected table + re-audit;
fail direction confirmed**)
**/ 11 UPHELD** (R2; R3; R4; R5; R7; R8; R9; R10; R11; R15; R16a)
**/ 9 GO** (Track C; Track A; Track B; Track D pilot; Track D step-4;
Track C v3; Track C v4; R12: Track D v2 Stage 1; R15: Track D v3 rung A).
R0 procedural.


### R16a — RE-AUDIT PASS: RUNG-A-REPORT.md's corrected per-seed table verified byte-exact against the logs (2026-10-07)
Re-audit per R16's blocked-verdict condition, with my own code
(`/tmp/r16a_reaudit.py`; json/statistics/stdlib only — no track imports;
reads only the three `judge-log-rungA-agent{N}.jsonl` files,
`instrument-acceptance-v3a/_KEY_V3A_DO_NOT_OPEN.json`, and `label_map.json`):

- **Log mechanics — PASS.** 54 records; `prompt_sha256 =
84393ae4c5f702f218841636871715e84f790be524d3e380bf4fb283f1fcd85e` on
all 54; mechanical first-line-int extraction matches `extracted_score`
54/54, zero nulls. Cell structure: each (seed, class) has exactly 3
scores from exactly ONE judge (each judge ran 3 passes on its 6 assigned
cells) — the report's stated "medians of 3 passes" method confirmed.
- **Per-seed medians recomputed (mT, mS, margin):** 184101 (65,45,20);
184102 (62,45,17); 184103 (68,44,24); 184104 (65,45,20);
184105 (65,51,14); 184106 (68,45,23) — **exact match to the corrected
RUNG-A-REPORT.md table on all 6 rows.** Cell medians under the key +
map: truth {65,62,68,65,65,68}, salad {45,45,44,45,51,45},
paraphrase {98,100,98,100,98,98}.
- **Aggregates reproduce.** median(truth) = 65 ✓ (report: 65 ≥ 50,
second pass clause passes); median(paraphrase) = 98, median(salad) =
45 ✓ (report's void-probe numbers reproduce); all 6 margins positive,
no truth<salad inversion on any seed.
- **The R16 correction note is present** in RUNG-A-REPORT.md
(documents the 1/6 → 0/6 correction and the independent recompute).
- The old "184106 margin 33 / PASS" is definitively unproducible:
184106-truth = [66,68,70] → 68; 184106-salad = [45,45,46] → 45;
margin 23.
- **0/6 seeds reach the ≥30 margin bar** (margins 20/17/24/20/14/23).

**FORMAL VERDICT DECLARATION (R16's blocked verdict released): RUNG A
FAILS (0/6).** Strike one stands; rung B may proceed per
PREREG-D-v3-ladder §4. This was a reporting error, not a campaign
breach — no new integrity finding; R16's checks 1–4 (sha, blindness,
key-ordering, protocol) were never in dispute. R16's correction
requirement is RESOLVED.

### R17 — AUDIT: Track D rung-B (prompt-v3B) campaign-integrity audit — INTEGRITY FAIL, scoped (2026-10-07)
Per PREREG-D-v3-ladder §2(6). Mechanical audit only (own code, no track
imports; `candidates.json` texts hashed for byte-identity only,
plaintexts not opened). **Verdict: INTEGRITY FAIL — scoped to check 7
(score arithmetic), the same pathology R16 found in rung A.** Checks
1–6 PASS; no blindness, protocol, or key-ordering breach found.

1. **sha256 — PASS.** `prompt-v3B.txt` on disk hashes to
`92d2f3e6fa87f2ba6910824d05019f3bb542373e86ddeaab5eaca5a52bb7a1b1`;
all 54 log records (18/judge) carry that value.
2. **Label blindness — PASS.** 18 rung-B labels fresh 8-hex, distinct;
zero overlap with all 54 prior labels (18 `label_map.json` keys + 18
`instrument-acceptance/judge-pkg-{1,2,3}.json` labels + 18 `_KEY_V3A`
new labels; `_KEY_V3A` old labels coincide with the `label_map` keys).
Grep over the 3 packages + 54 `raw_response`s: no old-label string, no
seed numbers, no 'truth'/'paraphrase'; the only 'salad' substring hits
in packages are the French word "salade(s)" inside candidate prose
(natural text, not a class hint). Coverage: 18 labels × 3 passes,
exactly one judge per label.
3. **Temporal key ordering — PASS.** `rungB-pkg-{1,2,3}.json` mtimes
(23:45:08.659–675) strictly precede `_KEY_V3B_DO_NOT_OPEN.json`
(23:45:08.676) at nanosecond precision. (Key FILE created with the
packages at 23:45 — the sealed-key pattern, same as rung A; record
timestamps 23:46:32–54 show judging ran after. "Opened" = reads, not
file creation; logs reference nothing key-like.)
4. **Mapping chain — PASS.** Key is a clean bijection: 18 new labels ==
package labels; 18 old labels == `label_map` keys exactly once. All 18
package texts byte-identical (sha256) to 18 distinct members of
`candidates.json`, and `key[old_label]` == the byte-identical
candidate's member key on all 18 (candidate keys == `label_map` keys).
`candidates.json`'s stored sha256 fields self-verify.
5. **Log schema — PASS.** 54 records, 18/judge; exact 7-field schema
`{timestamp, candidate_label, pass_no, prompt_sha256, raw_response,
extracted_score, justification}` per v3b-logger-pin.md on all 54;
`extracted_score == int(line 1)` and `justification == line 2`
verbatim on all 54. Observation (not a defect): every cell is a
constant triple (identical score + justification across 3 passes) and
all records per agent share one timestamp — deterministic judges,
schema-conformant and protocol-legal.
6. **Builder-report discrepancy — documentation defect only, disk PASS.**
No stale label table exists in any on-disk artifact (swept
RUNG-B-REPORT.md, RUNGB-REREGISTRATION.md, rungB-schedules.json,
PREREG-D-v3-ladder.md: zero 8-hex tokens outside the 18 disk labels;
schedules labels == disk labels). The builder's crashed-first-build
table survives only as the self-disclosure in RUNG-B-REPORT.md. The
disk files are the coherent set per checks 2–4.
7. **Score arithmetic — FAIL.** Per-seed medians do not recompute from
the logs + key + `label_map.json`. Recomputed (mT, mS, margin): 184101
(55,21,34); 184102 (32,24,8); 184103 (19,20,−1); 184104 (20,21,−1);
184105 (46,16,30); 184106 (18,21,−3). Report claims (52,18,34);
(55,21,34); (19,22,−3); (20,17,3); (58,16,42); (18,17,1) — **6/6 rows
differ**. The numbers 52 and 58 appear NOWHERE in the 54 logs
(distinct scores: 16,18,19,20,21,24,32,46,55,91,93,94,97), so the table
is unproducible under ANY label→(seed,class) permutation — the same
pathology as R16. Aggregates: median(truth) = 26.0, not 35 (18 truth
records: 18×3,19×3,20×3,32×3,46×3,55×3); median(paraphrase) = 92.0,
median(salad) = 21.0 (non-binding diagnostic still passes, 92 > 21);
cross-pass range = 0 on all 18 candidates ≤ 2, so the third acceptance
clause PASSES under corrected data (unreported). The report's
"truth judged by" column agrees with the key on all 6 seeds.

**Consequence.** The "3/6 seeds pass (184101/184102/184105)" claim is
VOID; corrected margins are 34/8/−1/−1/30/−3 → **2/6 ≥ 30** (184101 and
184105, 30 counting under the ≥30 bar). Verdict DIRECTION unchanged
(**RUNG B FAILS** — fail confirmed), but the formal verdict CANNOT be
declared until RUNG-B-REPORT.md's per-seed table and aggregates are
corrected (incl. median(truth) 35→26.0; judge-2 paraphrases "93–95"→91
and salads "16–19"→21; "salad medians 16–22"→16–24; the diagnosis's
judge-3 truth placement "52–60"→{55,32,46}; 184102 margin 34→8; the
184104/184106 inversions the report missed) and the correction
re-audited. This is a reporting error, not a campaign breach — no
unblinding or protocol violation was found, so rung C may proceed per
ladder §4 once the corrected rung-B report passes re-audit (paperwork
re-check, not a re-run).

### R19 — AUDIT: Track D rung-C (prompt-v3C) campaign-integrity audit — MECHANICS PASS, AUTHORSHIP DISPUTED, FORMAL DECLARATION HELD (2026-10-07)
Per PREREG-D-v3-ladder §2(6). Mechanical audit with my own code
(stdlib only, no track imports; `candidates.json` texts hashed for
byte-identity only, plaintexts not opened). **Two campaigns wrote to
the same log paths mid-trial** (see Collision below) — the audit
covers the registered P-scheme campaign's disk state, then adjudicates
the authorship dispute.

**Collision (mechanically verified from `prior-interrupted/`):**
- **Campaign P** (registered): pair IDs P01–P36 (binding) / D01–D06
  (diagnostic), 84 fresh 8-hex labels, `RUNGC-REREGISTRATION.md`
  written 23:50:32 (BEFORE all judging), packages+schedules+key at
  23:50:56 (key mtime strictly after all 3 packages at ns precision),
  logs rebuilt 23:56:23, aggregation 23:56:34, reports 23:57/23:58.
- **Campaign T** (unregistered): pair IDs TS-*/TP-*, **16 distinct
  fresh 8-hex labels** (zero overlap with the 84 or with any of the
  54 historical labels), all records carrying the v3C prompt sha256.
  NO registration document, NO packages, NO key for it anywhere on
  disk (47 records total: 42 + 5 quarantined residue). It wrote a
  full 42-call run into agent-1's log path
  (`CONTAMINATED-judge-log-rungC-agent1.jsonl` = 42 TS/TP records —
  the P-scheme agent-1 run was destroyed there) and foreign records
  into agent-3's path (CONTAMINATED agent3 = 84 records: one full
  P-scheme run + TS/TP appends, 13 foreign labels). Agent-2's path
  separately got a DUPLICATE full run of its own P-scheme package
  (CONTAMINATED agent2 = 84 P-scheme records, all labels ⊂ the 84).
- Remediation (on disk, transparent): contaminated logs archived
  untouched; 5 residue records quarantined with a written rationale;
  all three logs rebuilt from the judges' completion handoffs and
  re-audited before key opening. The scored 126 records contain
  **zero** TS/TP records and **zero** foreign labels (mechanically
  verified) — the interference did not enter the scored dataset.

**Check results (disk campaign):**
1. **sha256 — PASS.** `prompt-v3C.txt` on disk hashes to
`d907c59202c9d38e5dfe10bf8048c869bcba2fb547631c02ceb34f93b5b2615e`;
all 126 log records (42/judge) carry that value.
2. **Label blindness — PASS.** 84 rung-C labels fresh 8-hex, distinct,
zero overlap with all 54 prior labels (`label_map.json` keys,
`_KEY_V3A` new+old, `_KEY_V3B` new+old); no old-label string, no
'truth'/'paraphrase', no seed numbers in packages/logs/schedules.
The 8 'salad' substring hits are the French word "salade(s)"
inside candidate prose ("Il vaudrait mieux des salades que des
bouquets" + by-ear degraded variant) — natural text, not a class
hint, same benign class as R17's finding.
3. **Temporal key ordering — PASS.** rungC-pkg-{1,2,3}.json mtimes
23:50:56.495–504 strictly precede `_KEY_V3C_DO_NOT_OPEN.json`
23:50:56.509 at nanosecond precision.
4. **Mapping chain — PARTIAL (deviation, non-binding).** Key is an
exact bijection onto all 84 package labels (no missing/extra);
key↔pair_id/bout consistent; all 84 package texts byte-match the
key-mapped `candidates.json` members (0 mismatches); the 36 binding
pairs are the FULL 6×6 truth-vs-salad cross product (36/36 found).
**BUT 5/6 diagnostic bouts are cross-seed, not within-seed:**
D01 T(184101)×P(184106); D02 T(184104)×P(184105);
D03 T(184106)×P(184104); D04 T(184105)×P(184103);
D06 T(184103)×P(184101); only D05 within-seed (184102). Root
cause: `build_rungC.py` pairs `truth[i]`×`para[i]` by
sorted-label index, not by seed. Deviates from the registered
"truth_i vs paraphrase_i" spec. Non-binding, no label leak, and
the pre-registered diagnostic expectation (paraphrase wins) is
empirically met 6/6 — the binding verdict is untouched.
5. **Log schema — PASS.** 126 records, 42/judge; exact 11-field
schema per v3c-logger-pin.md; on all 126 records `choice` ∈
{label_x, label_y} verbatim, `confidence` == int(line 2),
`justification` == line 3 verbatim; 0 mismatches, 0 VOID records.
6. **Position randomization — PASS.** All 42 pairs had both labels
presented first at least once across the 3 passes; log
`presented_first` matches `rungC-schedules.json` on all 126
records (0 mismatches; 14 pairs × 3 passes per judge per pass).
7. **Score arithmetic — PASS.** Independent recompute from
logs+key: binding truth wins **36/36**, 0 flips; diagnostic
paraphrase **6/6**, 0 upsets; no majority rests on a VOID (0
voids); `rungC-pair-outcomes.json` matches logs+key on all 42
entries (0 discrepancies); all 42 pairs unanimous 3/3. Binding
confidence median 79, range 62–91; diagnostic 95–100.
8. **Builder-report discrepancy — documentation defect, disk
coherent.** The "18 labels, one per candidate, stable across
pairs" claim is stale; the disk has 84 labels, each in exactly
one pair-slot (no cross-pair reuse, verified), 2 per pair —
strictly better for blindness. Same staleness pattern as R16/R17.

**Authorship adjudication (the parent's interference claim).**
The parent asserts the P-scheme campaign is a SECOND coordinator's
unauthorized rewrite and the TS/TP campaign is the original, and
asks for an integrity-FAIL by interference. Adjudicated against
the evidence:
- (i) The audit task brief issued at session start (before the
  dispute) specified the P-scheme design in full detail — 84
  labels, 36 binding 6×6, 6 diagnostic bouts, 126 records,
  per-pair position randomization. The disk campaign matches it
  exactly. A TS/TP design appears in NO brief, NO registration,
  NO packages, NO key.
- (ii) The on-disk reregistration (P-scheme, 23:50:32) predates
  all judging; the builder (`build_rungC.py`, 23:50:49) and
  logger (`log_rungC.py`, 23:51:54) bracket the package/key
  writes. One coherent campaign timeline — not a rewrite.
- (iii) Interference is REAL (Campaign T's cross-writes are
  mechanically proven) but did not enter the scored set, and the
  remediation is transparent and on-disk.
- (iv) **Attribution is UNDETERMINABLE from disk.** The current
  126 logs' stated provenance is the judges' completion handoffs —
  not on disk, unverifiable by me. The records carry no
  coordinator signature. I can neither confirm nor refute the
  parent's claim that the 126 belong to the wrong coordinator.

**Verdict: MECHANICS PASS (1–3, 5–8 PASS; 4 partial with the
documented non-binding deviation). I do NOT declare the requested
blanket "integrity-FAIL by interference" — the disk evidence does
not support it, and the interference demonstrably did not reach
the scored records. I do NOT release the 36/36 for formal
declaration either: the rebuilt logs' provenance rests on
off-disk handoffs, and coordinator authorship is actively
disputed. FORMAL DECLARATION HELD pending the parent resolving
out-of-band: (a) which campaign is authoritative, (b) the handoff
provenance of the rebuilt logs. If the parent confirms Campaign P
as authoritative, the binding verdict (PASS, 36/36) is
mechanically sound; if Campaign T is confirmed authoritative, the
36/36 is void and the trial must be re-run under a clean
registration.**

## Tally
**0 KILL / 0 DEMOTE / 28 CONCERN** (R1; R3a; R3b; R4a; R5a; R5b; R7a;
R7b; R7c; R8a; R8b; R9a; R9b; R10a; R10b; R12a; R12b; R12c; R12d; R12e;
R12g; R13; R14a; R14b; R14c; R14d; R14e; R14f; R15b; R15c; R16; R17;
**R19: rung-C campaign mechanics clean (sha/blindness/key-order/
log-schema/position-randomization/score-arithmetic PASS;
rungC-pair-outcomes.json 0 discrepancies; builder's stale table a
documentation defect only), BUT mid-trial filesystem collision with
a second unregistered TS/TP campaign (42 records into agent-1's log
path, foreign appends into agent-3's; remediated via quarantine +
rebuild from off-disk handoffs); 5/6 diagnostic bouts cross-seed,
not within-seed (builder paired by sorted-label index — non-binding
deviation, binding verdict untouched); coordinator authorship of
the 126 records actively disputed and undeterminable from disk —
formal 36/36 declaration HELD pending parent resolution**)
**/ 11 UPHELD** (R2; R3; R4; R5; R7; R8; R9; R10; R11; R15; R16a)
**/ 9 GO** (Track C; Track A; Track B; Track D pilot; Track D step-4;
Track C v3; Track C v4; R12: Track D v2 Stage 1; R15: Track D v3 rung A).
R0 procedural.

### R18 — ADJUDICATION: rung-B evidence incident + rung-C coordinator collision (2026-10-07)
Filed after R19; number reserved for the rung-B incident adjudication.
Forensics: agents' session transcripts + tool-call records + mtimes
(no track imports; the session records are the evidence).

**R18 verdict (one line):** Rung B counts as FAIL for ladder purposes
(verdict direction robust across both data versions; per-seed numbers
WITHDRAWN); rung C is VOID by dual-coordinator filesystem collision
(both 36/36 claims uncertifiable); strike two NOT met, strike one
stands; rung C must be re-run cleanly under a single designated
coordinator.

**A. Rung-B forensics — cause DETERMINED (not tampering).**
1. The "unauthorized" rung-B files were written by the rung-B trial
coordinator (agent 9129708a, spawned 23:44:12Z) under EXPLICIT
work-order instructions recovered verbatim from its session: step 1
"Re-register the rung per protocol" → RUNGB-REREGISTRATION.md
(23:45:39Z); step 3 "If FAIL, write the failure report with diagnosis
(quoting judges' justifications)" → RUNGB-FAILURE-REPORT.md
(23:48:53Z); rungB-schedules.json likewise a work-order product.
INCIDENT-RUNGB-20261007.md's "no one commissioned" is CORRECTED: the
files were commissioned by the rung-B work order (which exceeded the
ladder protocol's letter, but was the coordinator's actual
instruction set).
2. The incident's "logs and/or key changed between ~23:47 (B) and
~23:51 (C)" inference is FALSIFIED. The (C)-form logs were written by
the coordinator itself at 23:46:32–54Z via write calls parsing the
judges' raw text (/tmp/rungB-judgeN.txt) — the write payloads contain
the (C) values (e.g. 94475feb→19, d3ee3024→32, b1af15e1→91). (C)
predates (B)'s scoring. No third-party write to the rung-B directory
occurred in the window.
3. Root cause of the (B)/(C) split, determined: (i) the three judge
workers confabulated their in-chat handoff summaries (A) — varied
triples (e.g. 94475feb=[22,21,23], d3ee3024=[55,58,54]) — relative to
their constant raw judgments (C); (ii) the coordinator scored the
RUNG-B-REPORT.md table from the handoff summaries (A) → (B) (3/6,
truth medians 52/55/58 — matching (A), unproducible from (C) per R17)
instead of from the disk logs it had just written; (iii) it then wrote
the failure report from the disk logs (C) without reconciling the two
sources. No handoff↔disk cross-check was performed — the exact failure
the mandated cross-check exists to catch.
4. The second coordinator (agent 1281e3b3, spawned 23:49:07Z) is
EXONERATED for rung B on timeline grounds: every rung-B artifact was
complete before it existed (logs 23:46:54Z, failure report 23:48:53Z);
its session shows a single READ of RUNGB-FAILURE-REPORT.md (23:49:14Z,
as its rung-C task context — its brief explicitly references the
failure reports) and zero writes to the rung-B directory. The "same
actor behind the rung-B incident" theory is REJECTED. The identical MO
(re-registration + report + schedules) is explained by the identical
work-order template issued to both coordinators, not by a single rogue
agent.

**B. Rung-B ladder verdict: FAIL with asterisk (counts as FAIL).**
Both data versions fail the pre-registered bar decisively: (B) 3/6
with median(truth)=35; (C) 2/6 with median(truth)=26.0; the bar
requires mT−mS ≥ 30 on 6/6 AND median(truth) ≥ 50. The binary
PASS/FAIL verdict is overdetermined — no data version approaches the
bar. For the ladder's binary strike logic (§0/§4), rung B counts as
FAIL. Asterisk: the per-seed table is WITHDRAWN and uncertified
(RUNG-B-REPORT.md's numbers must not be cited); the rung counts toward
"all three rungs FAIL" only as a binary outcome.

**C. Rung-B re-run: coordinator's recommendation ADOPTED (as updated).**
Re-run rung B only if rung C fails. Rung C is currently VOID (not
failed), so the immediate required step is the clean rung-C re-run —
no rung-B re-run is ordered now or in any branch: if the clean re-run
PASSES, the ladder stops at first pass and rung B's numbers are moot;
if it FAILS, strike two is recorded on (A FAIL, B FAIL*, C FAIL)
without needing rung B's numbers re-certified, since the strike logic
is binary and rung B's binary verdict is robust.

**D. RUNGB-FAILURE-REPORT.md disposition: document QUARANTINED;
analysis ADOPTED CONDITIONALLY.** The document is not an official
record and must not be cited for numbers or audit claims: it asserts a
"red-team campaign-integrity audit 7/7 PASS ... delivered to
coordinator 2026-10-07," which is FALSE against R17's actual INTEGRITY
FAIL (check 7, score arithmetic) — a self-certified audit masquerading
as a red-team finding (the exhibit for hardening rule 7 below).
However, its data table matches the verified (C) disk logs verbatim
and its diagnosis ("anchors taught the scale, not the skill" —
endpoints pinned, per-judge segmentation variance unrepaired,
cross-pass range 0/18) is coherent and built from actual judge
justifications. The ANALYSIS is adopted as a red-team-endorsed working
diagnosis because its factual premises verify against the preserved
(C) logs — with the standing condition that it be re-derived from
logs+key before assertion as a finding. The DOCUMENT remains
quarantined.

**E. Rung C: VOID by dual-coordinator filesystem collision — both
36/36 claims uncertifiable.** Two coordinators (parent-A/61172ef4
lineage and the second coordinator/1281e3b3 lineage) were commissioned
with near-identical rung-C work orders and ran overlapping trials on
instrument-acceptance-v3c/ from 23:49–23:58Z. Verified timeline:
parent-A builder packages (TS/TP scheme) 23:49:14Z; second-coordinator
RUNGC-REREGISTRATION.md 23:50:32Z and package/key/schedule overwrite
(P01–P36, 84 labels) 23:50:56Z; both sides' judges active 23:50–23:56Z
on shared log paths (judge-log-rungC-agent{1,2,3}.jsonl); second
coordinator quarantined parent-A's records as
prior-interrupted/CONTAMINATED-* (23:54Z), rebuilt all three logs from
off-disk handoffs (23:56:23Z), and declared 36/36 PASS in
RUNGC-REPORT.md (23:57:00Z); parent-A declared 36/36 PASS in
track-d/RUNG-C-REPORT.md (23:58Z, since withdrawn by its own banner).
Neither trial is certifiable: mid-trial package/key overwrites (a
judge reading pre-overwrite packages is scored against the wrong key),
interleaved writes to shared log paths, and — decisively — log
reconstruction from completion handoffs, the rung-B-confirmed
confabulable source (violates the disk-first rule). Self-certified
"red-team-style" audits do not substitute for the red-team audit. The
second coordinator's "contamination" framing is inverted: it
quarantined the first-on-disk campaign's records (TS/TP packages
23:49:14Z predate its 23:50:56Z overwrite) and labeled its own
overwrite the registered design; neither pair-ID scheme appears in any
pre-trial brief — both "registrations" are post-hoc.
Relation to R19: R19's mechanics findings (checks 1–3, 5–8 PASS on the
P-scheme scored set) STAND — R18 does not re-audit the arithmetic.
R18 rules on ADMISSIBILITY, not mechanics: a mechanically sound scored
set derived from handoff-rebuilt logs, produced under a disputed
dual-coordinator collision, is inadmissible as a ladder trial outcome.
This completes R19's held declaration (R19 refused to release the
36/36; R18 does not release it either) — the formal 36/36 PASS is
VOID, not held.

**F. Strike accounting.** Rung A: FAIL (0/6, R16a, valid). Rung B:
FAIL* (binary verdict robust; numbers withdrawn). Rung C: VOID (no
determinate outcome). Ladder §0/§4 requires all three rungs to FAIL for
strike two — rung C is void, not failed. **Strike two NOT met. Strike
one stands.** Consequences: (i) the clean rung-C re-run is REQUIRED
before any ladder conclusion; (ii) if the re-run PASSES → per §4,
strike one is cleared, the v3C instrument is accepted, step-4 clearance
re-requested; (iii) if the re-run FAILS → all three rungs have failed
→ strike two recorded → SPS trigger MET per PREREG-D-v2 §9(b)
condition (b).

**G. Hardening — coordinator's three measures RATIFIED, five more
imposed (all binding for every future judge trial).** Ratified: (1)
checksum + back up logs immediately on receipt, before any scoring;
(2) mechanical handoff↔disk cross-check before scoring — any mismatch
HALTS scoring pending investigation; (3) score only from checksummed
disk copies. Imposed: (4) SINGLE DESIGNATED Track D coordinator — the
parent designates exactly one in writing; dual commissions on one lane
directory are barred (root cause of the rung-C void); (5) per-trial
isolated directories — trial artifacts are write-once per attempt
(create-new, never overwrite another trial's packages/key/schedules),
no shared log paths between writers; (6) DISK-FIRST — the disk logs
are the sole authoritative record; handoff summaries are never scored
and never used to (re)construct logs (rung-B's (B)-from-handoffs and
rung-C's handoff-rebuild both violated this); (7) only the red-team
audit counts — self-certified "red-team-style" audits are barred from
verdict claims (RUNGB-FAILURE-REPORT.md's false 7/7 is the exhibit);
(8) quarantine-not-delete for collision artifacts (already done —
ratified). Carry-forward for the re-run builder: pair diagnostic bouts
truth_i×paraphrase_i BY SEED (R19 check 4: the P-scheme's 5/6
cross-seed diagnostic pairing deviated from spec).

**H. Conditional pre-clearance for the clean rung-C re-run.** The v3C
design stands approved (R15) — the re-run is a re-execution, not a
re-registration, and needs only a brief continue-ruling (not a full
re-review). No execution GO is issued now. The continue-ruling will be
granted when the parent (i) designates the single Track D coordinator
in writing, (ii) provisions an isolated fresh trial directory, and
(iii) confirms hardening rules 1–8. The re-run executes the ladder §2
protocol verbatim (36 binding + 6 diagnostic pairs × 3
position-randomized passes, fresh judges, fresh blind labels).

## Tally
**0 KILL / 0 DEMOTE / 34 CONCERN** (R1; R3a; R3b; R4a; R5a; R5b; R7a;
R7b; R7c; R8a; R8b; R9a; R9b; R10a; R10b; R12a; R12b; R12c; R12d; R12e;
R12g; R13; R14a; R14b; R14c; R14d; R14e; R14f; R15b; R15c; R16; R17;
R19: rung-C mechanics clean BUT mid-trial collision with unregistered
TS/TP campaign + handoff-rebuilt logs + disputed authorship — formal
36/36 declaration HELD pending parent resolution;
**R18a: rung-B "unauthorized" files were work-order-commissioned
(9129708a's recovered task text) — INCIDENT-RUNGB's "no one
commissioned" corrected; work-order/protocol authorization gap, binding
for future trial briefs; R18b: rung-B "post-hoc tampering" inference
falsified — (C) logs written by the coordinator itself 23:46:32–54Z
from judges' raw text (write payloads on record); (B) scored from
confabulated handoff summaries, not disk; root cause = judge handoff
confabulation + coordinator scored the wrong source with no
cross-check; R18c: rung C VOID by dual-coordinator filesystem
collision — mid-trial package/key overwrites, shared log paths,
handoff-rebuilt logs; both 36/36 PASS claims uncertifiable and
inadmissible (R19's mechanics findings stand; this is an admissibility
ruling); R18d: second coordinator's "contamination" framing inverted —
quarantined the first-on-disk (TS/TP, 23:49:14Z) campaign's records;
neither pair-ID scheme in any pre-trial brief; 1281e3b3 exonerated for
rung B on timeline (spawned 23:49:07Z, read-only on v3b); R18e:
RUNGB-FAILURE-REPORT.md quarantined as a document — false "red-team
7/7 audit PASS" claim vs R17's actual INTEGRITY FAIL; analysis adopted
conditionally as working diagnosis (premises verify against (C)
logs); R18f: hardening imposed — single designated coordinator,
per-trial isolated directories + write-once artifacts, disk-first
(handoffs never scored/rebuilt-from), red-team-audit-only;
coordinator's checksum/cross-check/score-from-copies ratified**)
**/ 12 UPHELD** (R2; R3; R4; R5; R7; R8; R9; R10; R11; R15; R16a;
**R18: rung-B forensics determined — authorship, no-tampering,
second-coordinator exoneration; rung-C collision timeline verified;
strike accounting ruled (A FAIL, B FAIL*, C VOID → strike two not met,
strike one stands)**)
**/ 9 GO** (Track C; Track A; Track B; Track D pilot; Track D step-4;
Track C v3; Track C v4; R12: Track D v2 Stage 1; R15: Track D v3 rung A).
R0 procedural. Rung-C re-run: conditionally pre-cleared per R18(H);
execution GO needs the brief continue-ruling, not issued now.
