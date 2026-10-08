# Track D — Rung-B re-registration note (PREREG-D-v3 ladder)

**Date:** 2026-10-07. Written BEFORE the rung-B trial campaign, per ladder §4
(diagnosis must precede the next rung).

## Exact prompt delta from v3A

`prompt-v3B.txt`, sha256 `92d2f3e6fa87f2ba6910824d05019f3bb542373e86ddeaab5eaca5a52bb7a1b1`.
Delta: **frozen v2 prompt verbatim** (wording, 0–100 scale, output envelope —
line 1 integer, line 2 one-sentence justification — all untouched) PLUS three
synthetic scored calibration exemplars prepended, explicitly labeled as
calibration anchors (not test items):

- Example A — score 21: spaceless repetitive noise with scattered French-like fragments
- Example B — score 61: spaceless by-ear degraded French, many identifiable words/phrases
- Example C — score 91: clean natural French prose

**Exemplar provenance (red-team §2.6 requirement):** mechanically verified —
no exemplar text is contained in any of the 18 frozen candidates, zero ≥50-char
fragment overlap with any candidate text. Synthetic from the pilot's observed
bands, never drawn from `candidates.json`. Verification script output is on
record with this note.

## Why the delta targets the anchor-compression mechanism

Rung-A diagnosis (audited, below): the v3A repair fixed segmentation —
truth 60–70, no collapse — but the v3A band anchors ("40–55 isolated words" /
"60–75 words+phrases, degraded") compressed BOTH classes toward the middle:
truth 60–70, salad 35–52, per-seed margins 14–24 against the ≥30 bar. The
residual failure is not segmentation; it is **anchor placement on the absolute
scale**. v3B attacks exactly that: the stimulus class rung-A judges scored
43–52 ("isolated real words in noise", e.g. 'me/leurs/se') is now NAMED and
anchored at ~21 — ~25 points lower. Degraded truth is pinned at ~61, clean at
~91. If judges obey the anchors, salad should drop from 35–52 toward ~21 and
margins should move from 14–24 toward 30–40, with truth staying 60–70.

## Audit-resolution note (RUNG-A-REPORT.md vs RUNGA-FAILURE-REPORT.md)

The two rung-A documents disagreed on seed 184106 (salad 35/margin 33 PASS vs
salad 45/margin 23 FAIL). Recomputed from the 54 raw log records against the
sealed key: **the failure report is correct — 0/6 seeds meet ≥30, margins
14–24.** The red-team audit evidently corrected 184106's salad median 35→45
[45,45,46]. Formal rung-A verdict: FAIL (0/6). Strike count: R13 strike one
stands; rung-A FAIL adds no strike (ladder §4).

## Pre-registered acceptance (binding, ladder §3 + task-carried bar)

PASS iff ALL of:
1. **mT−mS ≥ 30 on 6/6** (per-seed medians of 3 passes).
2. **median(truth) ≥ 50** (across all truth records).
3. **Cross-pass range ≤ 2 on all 18 candidates** (carried from rung A's added
   bar; rung A had 5/18 exceed with ranges 4–5).

Non-binding diagnostic: median(paraphrase) must not be ≤ median(salad).

## Campaign integrity facts (on record before judges run)

- 3 fresh judges, lane-naive, never saw `candidates.json` or the R13 key.
- 18 fresh 8-hex blind labels; zero hits against all 36 old labels (pilot 18 +
  v3A 18), verified mechanically in packages.
- 6+6+6 allocation (matches rung-A precedent; not class-stratified per §2(4)).
- Fresh random order per pass per judge (seeded, recorded in
  `rungB-schedules.json`); judges follow the message schedule.
- Prompt sha256 asserted at judge startup; abort on mismatch.
- Key `_KEY_V3B_DO_NOT_OPEN.json` opened only after all 54 calls logged.
- BEFORE-tripwire: clean except the protocol's own seal-list mention in the
  rung-A failure report (documentation, not contact). R5005 and sealed gate
  instances 184201–184204, 184206, 184207 never enter this campaign.
- Logger: `instrument-acceptance-v3b/judge-log-rungB-agentN.jsonl`, fields
  `timestamp, candidate_label, pass_no, prompt_sha256, raw_response,
  extracted_score, justification` (word_list n/a under the v2 envelope).
