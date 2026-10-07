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
