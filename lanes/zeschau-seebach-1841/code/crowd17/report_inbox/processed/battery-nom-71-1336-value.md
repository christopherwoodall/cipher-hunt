# Battery report: nom-71-1336-value

- Target id: `nom-71-1336-value`
- Claim: "Name 71's nominal value at @1336 ('[86-INF] [71-noun] qui', direct-object head of 'qui'-relative)."
- Queue bars field: null — numbered bars derived from the worker brief before testing (protocol §2 permits pre-registered restatement when the queue field is empty).
- Date: 2026-10-09
- Worker: battery worker (subagent b35fe0e4-edfb-4e34-98b8-732d7640200c)
- Stream: repaired 1,847-pair / 96-type parse (re-derived in-session); `canonical.py` never used. R5005, sealed gate instances, red-team adjudication queue untouched.
- Lock: `locks/nom-71-1336-value.lock` created on start, deleted on completion.

## Bar (worker-brief, pre-registered before testing)

1. Re-derive the @1336 window byte-exact.
2. Name 71's nominal value iff it parses as direct-object head of the qui-relative with zero new assumptions.
3. Else fence with stated cause.

## Method

1. Read BATTERY-PROTOCOL.md first.
2. Re-derived the repaired stream from `data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`: **1,847 pairs / 96 types verified**.
3. Adopted standing premises (not re-litigated): 64='qui' (prom), 47='ce' (prom), 86=INF (cls), 65=noun (cls), 71 §7 split candidate nominal@1337 vs non-nominal@925 (battery-val-71-quant-nominal PROMOTE), uniform-71-adjective KILL, name-71 NULL (fence, thin data).
4. Registry checked live: 71 absent, 83 absent, 60 absent, 08 absent, 52 absent, 38 absent; 86=['INF','cls'], 65=['noun','cls'], 64=['qui','prom'].

## Window-level evidence (byte-exact, 1-based)

Locus window, row a7_05 (tokens 1333–1359):

`1333=52 1334=39 1335=83 1336=86 1337=71 1338=64 1339=60 1340=08 1341=65 1342=64 1343=52 1344=38 1345=47 1346=86 1347=66 1348=73 1349=34 1350=62 ...`

So: `83 [86-INF] [71-noun] qui [60] [08] [65-noun] qui ...` — mid-row (no row-boundary artifact).

Bigram census (stream-wide): '86 71' = **1x (stream hapax)**; '83 86' = 2x; '64 60' = 1x; '60 08' = 2x; '08 65' = 2x; '83 71' = 1x.

Banked values inside the row: 64='qui', 47='ce', 34='i', 48='e', 82='m', 77='le' (provisional). Every direct neighbor of 71 at @1337 (83, 86, 60, 08, 65, 52, 39, 38) is value-open.

## Per-clause pass/fail

- **C1: PASS** — window re-derived byte-exact; locus confirmed at @1336–1338 = `86 71 64` on row a7_05 mid-row.
- **C2: does not fire.** The parse '[86-INF] [71-noun] qui' = direct-object head of the qui-relative stands (adopted battery-grade reading, class-71-adjective C2). But no value attaches with zero new assumptions: every neighbor's value is open (86's infinitive value open, 60's value open, 08's value open, 65's value open, 83's value open). Only 64='qui' is banked. The frame licenses the nominal class but names nothing.
- **C3: FIRES — fence with stated cause.**

## Verdict: NULL (fence executed)

### Fence cause

1. **Zero-new-assumptions bar unmet:** naming 71's value requires a licensed value, and the entire locus frame consists of open values. 86=INF is class-only; 65=noun is class-only; 83/60/08/52/38 are fully open. Nothing in the window names 71.
2. **Distributional thinness:** '86 71' is a stream hapax (1x); no other 71 window supplies a nominal value leg — @925 forces non-nominal, @712 is sub-lexical ('e 71 n'), the remaining four windows have no banked contact. Confirms name-71's fence.
3. **§7:** 71 is an established split candidate (nominal@1337 vs non-nominal@925, val-71-quant-nominal PROMOTE). Naming a single nominal value at @1337 would pre-judge the red-team split adjudication — red-team venue, not battery.

No standing verdict contradicted or downgraded; §7 intact; canonical-stream caveat stands (row a7_05 offset unvalidated).

## Follow-ups proposed (all verified ABSENT from battery-queue.json)

1. `val-86-inf-locus` (P3) — name 86's infinitive value at @1336; the governing infinitive's value constrains its direct object's semantic field.
2. `val-60-qui-relative` (P3) — name 60's value at @1339 under 'qui' (finite-verb slot); constrains the relative clause and 71's antecedent role.
3. `antecedent-71-rerun-gated` (P4) — gated re-run of this bar once 86/60/08/65 values resolve; the boundary becomes testable with licensed neighbors.
