# Rung C report (PREREG-D-v3 ladder) — VERDICT: PASS

Rung C (prompt-v3C.txt, sha256 `d907c59202c9d38e5dfe10bf8048c869bcba2fb547631c02ceb34f93b5b2615e`:
pairwise forced-choice, ties forbidden, confidence 0–100)
trial campaign complete 2026-10-07. 3 fresh blind judges × 42 calls
(14 pairs × 3 position-randomized passes), 126 records, red-team-style
campaign-integrity audit 7/7 PASS (prompt pin on all 126 records, registered
pair-ID scheme, mechanical choice/confidence/justification parse, schedule
adherence, per-pair position randomization with each label first ≥1×,
label blindness vs all 54 old labels). Key opened only after all 126 calls
logged and verified. R5005 and sealed gate instances
(184201–184204, 184206, 184207) never contacted (tripwire before/after: clean).

## Verdict: PASS (against pre-registered criteria)

Binding bar (ladder §3): truth wins the per-pair majority on ≥35/36 pairs.

| measure | observed | bar |
|---|---|---|
| binding pairs, truth wins | **36/36** | ≥35/36 |
| flipped pairs | 0 | ≤1 |
| unanimous 3–0 majorities | 36/36 | — |
| void records | 0 | — |
| confidence (binding) | median 79, range 62–91 | not gated |

- Diagnostic (non-binding): 6 truth-vs-paraphrase bouts — paraphrase won 6/6,
  confidences 95–100, exactly as pre-registered (clean French contains more
  identifiable French; memorization worry moot under blind forced choice).
- Void-probe symmetry: n/a under forced choice; the diagnostic bouts serve it.

## Why it worked (in the judges' own words)

The pairwise frame did what rungs A and B could not: it let judges apply the
discrimination their own reading already performs, without mapping it onto an
absolute scale. All three judges spontaneously did the rung-A mechanism work —
listing recovered French words — WITHOUT being required to:

- Judge 1: "Text A offers a varied French lexicon including chapitre, livre,
  visite, depart, Pierre, partie, parle and premiere while Text B repeats one
  by-ear word..." (P03, conf 82)
- Judge 2: "The winning passage contains more distinct identifiable French
  words — dire, première, ne pas, être, visite, vu, sur le — while the other
  is a repetitive syllable soup..." (P23, conf 62)
- Judge 3: "The 8b84c240 passage is saturated with recoverable by-ear French
  throughout (de, ne, il, une, la, se, premier, visite, dire, parle), while
  the other passage is mostly meme-noise with only sparse French islands."
  (P26, conf 90)

Notably, judge 2's lowest-confidence wins (62–66) came with the richest word
lists — the discriminative signal was present even where the judge felt least
certain. The A/B lesson is confirmed empirically: the problem was never the
signal, it was the absolute-scale mapping. Pairwise forced choice removes the
mapping, and discrimination goes to ceiling (36/36, all unanimous).

On the task-carried mechanism+scale combination question: the registered v3C
design did NOT enforce word-listing (the pre-registered spec forbids altering
the pinned prompt/envelope), yet the mechanism appeared behaviorally in all
three judges' justifications. The combination was thus achieved in effect if
not in structure. The hypothetical v3D (pairwise + mandatory listing) is no
longer needed for acceptance and is retired as a candidate.

## Campaign-integrity incident (documented per doctrine)

During the trial, the log files were contaminated by a parallel/stale process
running an older harness design against the same lane directory: foreign-scheme
records (pair IDs `TS-*`/`TP-*`, its own label set, zero collisions with the
84 registered labels) were appended to the agent-1 and agent-3 log paths, and
a second judging run of the agent-2 package (different confidences/
justifications, word-count-aid methodology) was appended to the agent-2 log.
Prior-interrupted-session residue (5 records, foreign scheme) had already been
quarantined before the trial.

Remediation: the contaminated logs were archived untouched to
`prior-interrupted/CONTAMINATED-*` with this note; all three logs were rebuilt
from scratch SOLELY from the three judges' completion handoffs (their reported
42 responses each — the authoritative record of what the judges said); the
7/7 audit was run against the rebuilt logs immediately before key opening,
and aggregation refused to proceed below 126 verified records. No foreign
record entered the analysis. The parallel writer's identity is unknown (no
matching process in ps; the sibling may belong to another session); flagged
to the parent as an open question.

## Ladder consequence (per §4)

**The instrument is ACCEPTED. Strike one is cleared. Stop — no further rungs.**
Step-4 clearance (red-team review of the accepted instrument + the full
sealed-instance gate) may now be re-requested on prompt-v3C. The gate funnel
(2,700-call budget) is unblocked at the instrument level.

## Campaign artifacts

- Re-registration: `instrument-acceptance-v3c/RUNGC-REREGISTRATION.md`
  (prompt spec, pairwise rationale, acceptance criteria, integrity facts —
  written BEFORE the trial)
- Logs: `instrument-acceptance-v3c/judge-log-rungC-agent{1,2,3}.jsonl`
  (42 records each, rebuilt from handoffs; fields per v3c-logger-pin.md)
- Packages: `instrument-acceptance-v3c/rungC-pkg-{1,2,3}.json`;
  schedules: `instrument-acceptance-v3c/rungC-schedules.json`
- Key: `instrument-acceptance-v3c/_KEY_V3C_DO_NOT_OPEN.json`
  (84 fresh labels → old label/class/pair; opened only after 126 verified)
- Pair outcomes: `instrument-acceptance-v3c/rungC-pair-outcomes.json`
- Contaminated logs archived: `instrument-acceptance-v3c/prior-interrupted/CONTAMINATED-*`
- Builder: `build_rungC.py`; logger/aggregator: `log_rungC.py`
