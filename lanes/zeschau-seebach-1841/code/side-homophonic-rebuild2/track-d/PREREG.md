# TRACK-D PREREG — frozen French-LM rerank judge

**Track:** D (LM-judge reranker), solver-rebuild round-2 fleet.
**Date:** 2026-10-07.
**Status:** PRE-REGISTERED — no judge scoring has run. Awaits red-team dated GO in `../redteam/RULINGS.md`.
**Author:** track-d subagent (self-operator judge).

## 0. Question

The rebuilt objective's likelihood (Tocqueville char-5-gram + lexicon) is
Goodharted by morpheme salad: salad beats planted truth by 2,601 nats at
chance primary recovery, and the verifier proved reweighting within the
5-gram+lexicon family is EXHAUSTED (failure is in the likelihood, not the
weights). This track tests the search-then-rerank pattern: the annealer
keeps the cheap smooth objective for search; a FROZEN fluent French LM,
used ONLY as a reranking judge over the annealer's top-K, decides the
winner. Nothing is trained.

**Falsifiable claim under test:** a frozen French-fluency judge prefers
planted truth over the frozen salad-class decode on all 6 original control
instances, by a clear margin — i.e., the judge succeeds where the 5-gram
likelihood failed.

## 1. Judge instrument

**Endpoint check (2026-10-07, before registration):** no local LLM on the
VM. `which ollama` → absent; TCP connect to 127.0.0.1 on
11434/11435/8080/8000/1234/5000/7860 → all closed. Per the track brief,
the track operator serves as the judge (self-operator mode).

**The judge is a FIXED scorer:** the prompt below is frozen at red-team
sign-off. No tuning on candidates afterward; any prompt change =
re-registration + new pilot.

### Frozen prompt (verbatim; `judge_prompt.txt`, sha256 `390a1ec0…c08e21d`)

```
You are a judge of French-language fluency. You will be shown a passage of text. Some passages are fluent French; others are degraded, garbled, or adversarially constructed.

Rate the passage's FRENCHNESS — how much it reads as natural, fluent French prose — on a 0–100 scale:

- 100: flawless, natural French prose (any era)
- 75: clearly French, with minor errors or oddities
- 50: fragmented French; roughly half is broken or non-French
- 25: mostly non-French, with scattered French-like fragments
- 0: not French at all

Judge ONLY fluency as French. Do not reward or penalize subject matter, era of style, or passage length.

Output format (exact): the first line is a single integer from 0 to 100 and nothing else. The second line is exactly one sentence explaining the score. No other text.

PASSAGE:
---
{text}
---
```

Full sha256: `390a1ec0bf1aa9e0e495a5fe98e65107c41025c954cd11b68d1931816c08e21d`.

**Design notes (registered, not tuned later):**
- The prompt deliberately does NOT mention Les Misérables, memorization,
  or "famous works" — priming the judge about memorization would distort
  the instrument; the memorization question is handled empirically by the
  §4 probe.
- The prompt demands a single number + one justification sentence. The
  track records the NUMBER only, never reinterprets it; the sentence is
  logged for audit.
- No pairwise comparison anywhere: every candidate is scored
  independently (no ordering bias).

## 2. Judge-call protocol (binding)

1. **Candidates** are the raw `join(pcell)` decode strings, unmodified
   (spaceless, with the encipherer's ear-noise spellings intact). No
   re-segmentation, no added spaces — truth, salad, and paraphrase
   classes all face the identical surface format (paraphrase
   normalization: §4).
2. **Blind labels:** each candidate gets a random 8-hex label; the
   label→(instance, class) map is written to `label_map.json` and NOT
   consulted until all queries are logged.
3. **Three passes:** the 18 pilot candidates are scored in three
   independent passes; each pass uses a fresh random order of the same
   blind labels. A "query" = one pass × one candidate (54 pilot queries).
   Passes are issued as standalone evaluations; no cross-referencing
   prior scores.
4. **Extraction (mechanical):** the score is the first output line,
   parsed as an integer in [0,100]. Unparseable/out-of-range first line →
   query logged as EXTRACTION-FAILED and excluded. **No steering, no
   rephrasing, no re-querying** — one frozen prompt, one attempt each.
5. **Aggregation:** per-candidate score = MEDIAN of its valid queries.
   Fewer than 2 valid queries → candidate VOID (reported, not claimed).
6. **Logging:** every call appended to `judge_log.jsonl` with:
   `timestamp, candidate_label, pass_no, prompt_sha256, raw_response,
   extracted_score`. The log is the instrument record; the analysis reads
   only the log + the sealed label map.
7. **Determinism note (honest):** the operator's judgments are not
   seeded. The controls are: frozen prompt, blind labels, fixed 3-pass
   order randomization, median aggregation, no re-query, complete
   logging. Variance across the 3 passes is reported per candidate.

## 3. Pilot design

**Candidates (18 = 6 truth + 6 salad + 6 paraphrase):**

- `truth_<seed>`: planted-truth decode for seeds 184101–184106, built
  from `code/side-homophonic/control/instances/SYNTHETIC-key-<seed>.json`
  via the rebuild solver machinery (`build_solver` + key assignment +
  `_rebuild_conc` + `_full_refresh`, decode = `join(pcell)` — the
  track-c `build_decodes.py` pattern). **Seal status: NO new seal is
  opened.** All six original-instance keys were already opened in round 1
  for forensics (`verifier/CLOSING-VERIFICATION.md:8` — "Sealed 184101
  truth opened for post-diagnostic forensics only"; `:139` — "Sealed
  truth keys for 184101–184106 were opened for forensics only"). The
  FRESH gate instances (184201–184204, 184206, 184207) remain sealed and
  are never read by this track.
- `salad_<seed>`: the frozen salad-class decode = `best.assignment`
  from `code/side-homophonic/runs/frozen-ctl-<seed>/result.json`
  (seeds 184101–184106), same decode construction. Taken AS-IS; no
  substitution if one looks "less salad-like" — any anomaly is reported,
  not repaired.
- `para_<seed>`: memorization-probe paraphrase (§4).

All frozen to `candidates.json` with per-string sha256 + provenance
before any scoring. Expected lengths: truth ~3.1–3.2k chars, salad
~5.1k chars (184101 measured).

**Disclosure:** during recon the operator saw a head/tail fragment of
184101's truth and salad strings (in `track-c/decodes.json` output).
This is logged here; the blind-label + 3-pass protocol (§2) is the
bias control. No other candidate text has been viewed.

**Salad-class sanity check (reported with the pilot, not a gate):**
top-10 value-frequency concentration per salad decode; if any salad
decode scores primary recovery > 0.10 against the (already-opened)
planted truth, it is flagged as a comparator anomaly.

### Pilot bar (binding)

Let `mT(i) = median judge score of truth on instance i`,
`mS(i) = median judge score of salad on instance i`.

**PILOT PASS** iff for ALL 6 instances: `mT(i) − mS(i) ≥ 15` points on the
0–100 scale.

**KILL RULE:** anything less than 6/6 → the track is DEAD. Report the
per-instance medians, margins, and per-query variance honestly with the
numbers. No re-registration of the bar after seeing results; a dead
track stays dead.

(15 points ≈ the "clear margin" unit: the salad and truth are
categorically different texts — fluent prose vs morpheme tiling — so a
working judge should separate them by far more than 15.)

### Pilot cost

18 candidates × 3 queries = **54 judge calls**. Fine.

## 4. Memorization probe (binding)

**Risk:** the truth plaintexts are Les Misérables slices; a fluent French
LM (including the operator) may have memorized Les Mis. A judge that
prefers truth because it RECOGNIZES Les Mis is not measuring fluency —
and recognition does not transfer to the real R5005 (1841 diplomatic
French, not Les Mis).

**Probe construction:** for each instance, the operator produces
`para_<seed>`: the truth decode's meaning reworded into fresh French
prose of comparable length — one fixed pass per instance, written BEFORE
any scoring, frozen into `candidates.json` with sha256. Mechanical
normalization: natural French spacing/punctuation as written (NOT
spaceless) — this gives the paraphrase a surface-format advantage over
the spaceless ear-noised truth decode, making the void rule below
conservative (it fires only if the judge prefers the handicapped truth
anyway).

**Void rule (binding):** let `mP(i)` = median judge score of the
paraphrase on instance i. If on ANY instance
`mT(i) − mP(i) ≥ 15`, memorization is driving the preference →
**the pilot PASS is VOID**. Report to the red team; step 5 does NOT run
without a new red-team ruling.

**Proceed condition:** pilot bar (§3) met AND `mT(i) − mP(i) < 15` on all
6 AND red-team memorization ruling. (If both truth and paraphrase clear
salad by ≥15 with |mT − mP| < 15, the preference is fluency-driven.)

**Probe anomaly fallback:** if on any instance the paraphrase scores
at/below the salad (`mP(i) ≤ mS(i)`), the probe is uninformative for that
instance (bad paraphrase, not evidence about memorization) → report the
anomaly; step 5 requires a red-team ruling rather than the automatic
proceed condition.

## 5. Rerank pipeline (conditional on §3 PASS + §4 proceed + red-team GO)

**Annealer runs (6 FRESH sealed instances 184201–184204, 184206, 184207):**

- Code: `code/side-homophonic-rebuild/solver/solver.py`
  (md5 `aac6f2602eab09ee24ba7a6709a02123`) + `config.json`
  (md5 `de2c3fccd77e9c7c3b21e9549e49a1e3`) — **byte-identical to the
  frozen rebuild; the objective is untouched.**
- NO solver.py change: top-K is extracted by post-processing each run's
  `result.json` `restarts[]` list (every restart's final assignment is
  already recorded). K = 20 distinct final assignments per instance,
  ranked by J (the rebuilt objective). If fewer than 20 distinct finals,
  take all distinct.
- Invocation per instance:
  `python3 solver.py --pairs solver_inbox/SYNTHETIC-ct-<seed>.pairs.txt
  --lm solver/lm_ref/lm.json
  --anchors-file solver_inbox/SYNTHETIC-crib-<seed>.json
  --out track-d/gate_runs/<seed>/result.json
  --restarts 24 --seed <7101..7106>`
  (iters=40000, t0=60 from config.json; all other flags default).
- Seeds 7101–7106: fixed, logged, disjoint from all other tracks' seeds
  (track-c pilot used 7001–7004) and all instance seeds.
- Inputs per CONTROL-DESIGN.md §8.1 ONLY: ct pairs + crib JSON +
  Tocqueville lm. **The track never reads
  `SYNTHETIC-key-18420*.json`, `sealed-pclasses.json`, or any fresh
  plaintext.** A pre-run grep self-check is logged.
- Wall estimate: ~88 s/restart (pilot-measured) × 24 ≈ 35 min/instance,
  ≈ 3.5 h total, backgrounded.

**Judging (360 calls):** 120 candidates × 3 passes under the §2 protocol
(frozen prompt, blind labels, median). Per-instance answer = candidate
with the highest median judge score; tie-break: higher J, then lower
restart index (pre-registered).

## 6. Gate scoring (conditional on §5)

Per-instance winning key (96-group mapping) → `gate_answers.json`.
**Scoring against the sealed keys is done by the Runner/parent per
CONTROL-DESIGN.md §8; Track D never opens the fresh keys.**
Report per-instance PRIMARY and SECONDARY per §4:

| metric | definition | BAR |
|---|---|---|
| PRIMARY | exact recovery of planted PRIMARY cell, 89 non-anchor groups | mean ≥ 0.20, min ≥ 0.10 |
| SECONDARY | decode accuracy, all 1846 pairs (anchors given) | mean ≥ 0.30, min ≥ 0.22 |

**Verdict rule:** PASS = all four inequalities hold. Anything else =
FAIL: stop, do not touch R5005, report per-instance numbers.
A gate PASS does NOT authorize an R5005 run by this track — that
authorization belongs to the parent/coordinator, not to Track D.

## 7. Hard constraints (all steps, no exceptions)

1. **NO R5005 contact.** A grep for `r5005|R5005|ct_R5005` over
   `track-d/` is logged before the pilot and before the gate runs; any
   hit = self-KILL of the run.
2. Control/diagnostic only. Nothing in this track touches real data.
3. No judge scoring (pilot or gate) before the red-team dated GO in
   `../redteam/RULINGS.md`. Decode plumbing (`build_candidates.py`,
   `candidates.json`) may be built after GO; the paraphrases are written
   after GO, before scoring.
4. The prompt is frozen at GO. Any change = re-registration + new pilot.
5. Deterministic seeds everywhere except the judge instrument itself
   (controlled per §2).
6. No cherry-picking: exactly 3 queries per candidate, median taken, all
   raw responses logged, extraction failures logged not hidden.

## 8. Outcomes

- **Pilot 6/6 (≥15 each) + probe clean + red-team memorization
  clearance →** build §5 pipeline, run §6 gate, report per-check numbers.
- **Pilot <6/6 →** track DEAD; honest negative with medians, margins,
  and per-query variance.
- **Probe void (mT − mP ≥ 15 anywhere) →** pilot PASS void; report to
  red team; no §5 without a new ruling.
- **Gate PASS →** report; R5005 authorization is the parent's call.
- **Gate FAIL →** stop; report per-instance numbers; do not touch R5005.
