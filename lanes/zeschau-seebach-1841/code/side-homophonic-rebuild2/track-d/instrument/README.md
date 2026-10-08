# Track D — Automated Judge Instrument

## What this is

The mechanical scoring pipeline for Track D's LM-judge. It fans judge
calls out to worker subagents (fresh LM instances), each instructed
with the FROZEN prompt, and aggregates their scores with zero
discretion: first-line-int extraction, median-of-3, cross-pass range
checks, full audit logging.

**The prompt is frozen.** `prompt_registry.json` pins sha256
`390a1ec0…c08e21d`. The runner verifies the hash before every batch
and aborts on mismatch. Any prompt change = re-registration + new
pilot + red-team clearance. Not the operator's call to waive.

**R5005 never enters.** The prepare phase greps every candidate text
for `r5005|R5005|ct_R5005` and aborts on any hit. Control instances only.

## Integrity contract (prompt hash)

Three independent checkpoints, all must pass:

1. **Runner prepare:** verifies sha256 of `../judge_prompt.txt`
   against `prompt_registry.json`. Abort on mismatch.
2. **Worker startup:** each worker hashes the prompt FILE at the
   absolute path in its brief (shared filesystem) and compares to
   the expected sha256 in the brief. Abort on mismatch. This
   catches file mutation between prepare and execution.
3. **Runner collect:** re-verifies the file hash; asserts every
   worker return's `prompt_sha256_computed` equals the frozen hash.
   Abort on mismatch.

The brief embeds the prompt text for reference, but the FILE is
authoritative — workers never parse the brief to reconstruct the
prompt bytes (too fiddly to do reliably). Registry hash covers the
file bytes verbatim.

## Files

| file | role |
|---|---|
| `prompt_registry.json` | frozen hash, single source of truth |
| `judge_runner.py` | orchestrator: `prepare` / `collect` |
| `worker_brief_template.md` | exact brief text for judge workers |
| `aggregate.py` | mechanical aggregation + verification |
| `runs/` | per-run dirs: manifest, briefs, results, logs |

## Operating procedure

### 1. Prepare a run

```bash
cd code/side-homophonic-rebuild2/track-d/instrument
TS=$(date -u +%Y%m%d-%H%M%S)
python3 judge_runner.py prepare \
  --package ../candidates.json \
  --outdir runs/$TS \
  --passes 3 --batch-size 1 --seed 9001 \
  --mode-label "acceptance-test"
# dry-run: add --labels 1386766b,d38a1821,fed88338 (1 truth/1 salad/1 paraphrase)
# resume:  add --resume-from runs/$TS/judge_log.jsonl
```

Prepare does: prompt-hash verification (abort on mismatch) →
package load → R5005 self-check grep (abort on hit) → seeded work
items (fresh random order per pass) → resume filtering → worker
briefs in `runs/$TS/briefs/`. It prints the spawn instructions.

### 2. Spawn workers (operating agent does this)

For each brief in `runs/$TS/briefs/`: spawn ONE worker subagent
whose task IS the brief text (verbatim). Workers are independent;
run them in parallel batches. **Pacing: do not hammer.**
Recommended: ≤12 concurrent workers, ~30–60s stagger between
spawn waves. Each worker returns the JSON specified in its brief.

Save each worker's return JSON to `runs/$TS/results/<worker_id>.json`.

### 3. Collect

```bash
python3 judge_runner.py collect --rundir runs/$TS --results runs/$TS/results
```

Collect does: prompt re-verification → worker-hash assertion per
return (abort on mismatch) → mechanical first-line-int extraction →
append to `runs/$TS/judge_log.jsonl` in the pilot's EXACT format
(timestamp, candidate_label, pass_no, prompt_sha256,
raw_response, extracted_score). Duplicates skipped.
EXTRACTION-FAILED entries are logged to stdout, EXCLUDED, and
NEVER re-queried (protocol).

### 4. Aggregate + verify

```bash
python3 aggregate.py --log runs/$TS/judge_log.jsonl \
  --expect runs/$TS/work_batches.json \
  --out runs/$TS/aggregation_report.json
# acceptance: add --pilot-medians <{label:median}> --label-classes <{label:[seed,class]}>
```

Reports: per-candidate median/range (flags range > 2),
completeness (expected vs logged, missing/unexpected),
hash uniformity, and optionally the acceptance check
(all medians within ±3 of pilot; all mT−mS ≥ 30).

## Log format (pilot-exact)

```json
{"timestamp": "2026-10-07T22:10:04+0000", "candidate_label": "5888ca6b",
 "pass_no": 1,
 "prompt_sha256": "390a1ec0bf1aa9e0e495a5fe98e65107c41025c954cd11b68d1931816c08e21d",
 "raw_response": "92\nFluent, well-formed French prose ...",
 "extracted_score": 92}
```

## Throughput model (gate: 2,700 calls)

| stage | calls | workers (batch=10) | waves @12 parallel | time @~45s/wave |
|---|---|---|---|---|
| triage (1-pass) | 200/inst × 6 | 20/inst → 120 | 10 | ~8 min |
| triage top-40 (2 more) | 80/inst × 6 | 8/inst → 48 | 4 | ~3 min |
| ILS (1-pass) | 150/inst × 6 | 15/inst → 90 | 8 | ~6 min |
| final top-10 (2 more) | 20/inst × 6 | 2/inst → 12 | 1 | ~1 min |
| **total** | **2,700** | | | **~20 min + spawn overhead** |

Measured dry-run timings calibrate the per-wave cost; the table
above is the planning figure. The bottleneck is subagent spawn
latency, not scoring — batch aggressively (batch-size 10) for
1-pass stages, batch-size 1 for median-of-3 stages.

## Red-team hooks (all automatic)

- `manifest.json`: mode, timestamps, package path+abspath, prompt
  sha256, order seed, batch size, labels, R5005 self-check result.
- Every log entry carries prompt_sha256; `aggregate.py`
  re-derives every score and checks hash uniformity.
- Worker returns are archived verbatim in `runs/$TS/results/`.
- Resume mode never rewrites history: skips logged (label, pass)
  pairs, appends only new ones.
- No prompt tuning, no steering, no re-querying — hardcoded in
  runner (extraction failures excluded, never retried) and brief
  (first honest judgment stands).

## Protocol gaps found during construction

1. **Worker hash verification: SOLVED via file path.** First design
   had the worker parse the brief to reconstruct prompt bytes — too
   fiddly (my own test extraction dropped a trailing newline).
   Workers now hash the prompt FILE directly. The runner's
   pre-batch verification remains the primary check; the worker
   assertion catches inter-phase mutation. Both logged.
2. **"Fresh LM instances per call" is approximated.** One worker
   per (candidate × pass) would be 2,700 spawns; the instrument
   defaults to one worker per candidate (3 passes) or per batch
   for triage, with explicit independence instructions + blind
   labels + random order. The pilot's own precedent (one operator,
   54 sequential judgments) bounds the anchoring risk, and worker
   IDs are logged per judgment for audit. If the red team demands
   stricter freshness, set `--batch-size 1` and spawn per pass
   (3× the spawns).
3. **R5005 grep is a tripwire, not a proof.** It catches literal
   markers; a determined leak wouldn't use them. The real control
   is package provenance (only control-instance packages are
   ever passed to prepare). Both are logged.
