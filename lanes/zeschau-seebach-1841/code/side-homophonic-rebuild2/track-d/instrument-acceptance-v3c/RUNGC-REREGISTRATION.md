# Track D — Rung-C re-registration note (PREREG-D-v3 ladder)

**Date:** 2026-10-07. Written BEFORE the rung-C trial campaign, per ladder §4
(diagnosis must precede the next rung).

## Exact prompt spec

`prompt-v3C.txt`, sha256 `d907c59202c9d38e5dfe10bf8048c869bcba2fb547631c02ceb34f93b5b2615e`
(matches v3c-logger-pin.md pin; asserted at judge startup; abort on mismatch).

Prompt: pairwise forced-choice. Two blind decodes (possibly spaceless,
by-ear-degraded). Judge must choose EXACTLY ONE label as containing MORE French
(more identifiable French words and phrases — "Do NOT choose the one that reads
more fluently as surface prose; choose the one with more French lexical
material recoverable inside it"). Ties forbidden. Then confidence 0–100
(50 = pure guess). Output envelope (exact): line 1 = winning label verbatim,
nothing else; line 2 = single integer 0–100, nothing else; line 3 = exactly one
sentence explaining the choice; no other text.

Pairing: all 36 truth-vs-salad pairs (6 truth × 6 salad). Each pair judged
3 times with X/Y position randomized per pass (each label appears first at
least once across the 3 passes of a pair — mechanical audit check). 36 pairs
split 12+12+12 across the 3 fresh judges: 108 binding calls. Diagnostic
(non-binding): 6 truth-vs-paraphrase bouts (truth_i vs paraphrase_i, i=1..6,
× 3 passes = 18 calls), 2 bouts per judge. Total campaign: 126 calls, 42 per judge.

Aggregation: per-pair outcome = majority of 3 passes. VOID records (choice not
verbatim one of the two labels; unparseable confidence) are logged and move on;
no retries, no steering.

## Why pairwise sidesteps absolute calibration (the A/B lesson)

Both failed rungs show the discriminative signal is PRESENT in the judges' own
reading but unmappable onto an absolute scale:

- Rung A (word-listing mechanism): truth 60–70, salad 35–52 — the classes do
  not overlap; discrimination EXISTS but the v3A band anchors compressed both
  classes toward the middle (margins 14–24 vs the ≥30 bar).
- Rung B (anchored calibration): Judge 3's prose shows the signal plainly —
  "Substantially degraded spaceless text in which real French words like
  Capitre, premiere, une, visite, and livre remain identifiable throughout"
  (55) — while Judge 1 listed real words ("parler, la vie, parce, utilite")
  and STILL scored 18: "the words were legible but the holistic frame
  ('no coherent phrases') overruled them." The absolute-scale mechanism is
  unfixable in this framing: any absolute anchor scheme pins endpoints but
  cannot standardize per-judge segmentation.

Pairwise forced choice removes the mapping step entirely. The judge never
reports a number on an absolute scale; it applies the discrimination its own
prose already performs — which passage contains MORE recoverable French —
and reports only relative rank + confidence. Calibration (anchors, bands,
endpoints) becomes irrelevant by construction. Bradley-Terry win-modeling is
permitted as a diagnostic only.

## The rung-A mechanism question (task-carried consideration)

The operator asked whether the rung-A mechanism repair (mandatory recovered-word
listing) could be combined INTO rung C: pairwise choice where each judge first
lists recovered French words, then chooses the more-French candidate.

**Decision: the pre-registered spec does NOT permit this.** prompt-v3C.txt is
sha256-pinned with a fixed 3-line envelope (v3c-logger-pin.md: assert at
startup, abort on mismatch; the mechanical parse pins line 1/2/3 semantics).
Adding a word-list line changes the prompt text and the output envelope, which
would void the pre-registration and the logger pin. Per ladder §2(2) the variant
must be frozen, and per the rung discipline, re-registration happens BEFORE the
trial, not during it.

Rung C runs EXACTLY as registered. The combination is recorded here as a
candidate for re-registration (a hypothetical rung D / prompt-v3D: pairwise +
mandatory word-listing), to be specified and pinned BEFORE any trial if the
ladder continues.

Note: the registered v3C prompt already carries a partial mechanism instruction
("Base the choice on the count and quality of the French words/phrases you can
identify in each passage") — guided, not enforced. This campaign will show
whether guidance alone suffices.

## Pre-registered acceptance (binding, ladder §3)

**PASS iff truth wins the per-pair majority on ≥35 of the 36 truth-vs-salad
pairs** (≤1 flipped pair allowed as noise margin). This is the pairwise
analogue of the 6/6 discrimination bar — full truth>salad separation with no
systematic inversions.

Non-binding diagnostics: (a) median(paraphrase) must not be ≤ median(salad) —
kept for symmetry; under blind forced choice the memorization worry is moot.
(b) 6 truth-vs-paraphrase bouts: paraphrase is EXPECTED to win (clean French
contains more identifiable French). An upset here does not void the verdict but
is recorded. (c) Confidence calibration recorded, not gated.

## Campaign integrity facts (on record before judges run)

- 3 fresh judges, lane-naive: never the prompt-repair agent, never the pilot
  operator, never any instance that has seen `candidates.json` plaintexts or
  the R13/v3A/v3B keys. Briefs contain only blind labels + texts + the prompt.
- 84 fresh 8-hex blind labels (72 pair slots + 12 diagnostic slots); zero hits
  against all 54 old labels (pilot 18 + v3A 18 + v3B 18), verified mechanically
  in packages and logs.
- Pair schedule: 36 pairs split 12+12+12 (pair index order, seed-ordered);
  diagnostic bouts 2+2+2. Fresh per-pass order + position randomization per
  judge (seeded, recorded in `rungC-schedules.json`); judges follow the message
  schedule.
- Prompt sha256 asserted at judge startup; abort on mismatch.
- Key `_KEY_V3C_DO_NOT_OPEN.json` opened only after all 126 calls logged.
- BEFORE-tripwire: clean — R5005 and sealed gate instances 184201–184204,
  184206, 184207 never enter this campaign (tripwire grep before and after).
- Logger: `instrument-acceptance-v3c/judge-log-rungC-agentN.jsonl`, fields
  `timestamp, pair_id, label_x, label_y, presented_first, pass_no,
  prompt_sha256, raw_response, choice, confidence, justification` per the v3C
  logger pin.
