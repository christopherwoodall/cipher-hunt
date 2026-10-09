# Battery verdict: gov-93-88-frame

- Target: `gov-93-88-frame` (battery-queue.json, priority 3, status queued)
- Claim: "Census whether 93's followers across all 14 windows are consistently infinitive-shaped; if yes, 93 = semi-auxiliary governor class candidate (class-level)."
- Bars (verbatim): "name the class iff all 14 windows agree at battery grade; fence iff a counterexample is kill-grade"

## Bar restated as clauses
- C1: All 14 windows of 93 have infinitive-shaped followers at battery grade → name the semi-auxiliary governor class.
- C2: A kill-grade counterexample exists → fence (kill the class candidacy).

## Verdict: KILL

C1 FAIL / C2 FIRES.

## Findings

Repaired 1,847-pair / 96-type stream re-derived in-session; asserts held; `canonical.py` never used. n(93)=14, all loci byte-confirmed.

Follower inventory (11 distinct + stream end):
- @10 → 62 (open)
- @102 → 59 ('est', provisional)
- @111 → 29 ('er', pencil GT — infinitive ending)
- @159 → 52 (open)
- @263 → 52 (open)
- @479 → 00 ('pour', granted — preposition)
- @604 → 54 (open)
- @734 → 76 (noun, PROMOTED)
- @1540 → 88 (governor, registry class-level)
- @1555 → 61 (open)
- @1685 → 62 (open)
- @1761 → 06 ('ent', PROMOTED — 3pl finite ending)
- @1812 → 50 (open)
- @1846 → stream end (no follower)

Kill-grade counterexamples (each a follower that cannot be infinitive-shaped under standing values):

1. **@734: follower 76 = noun (PROMOTED).** A semi-auxiliary governor takes an infinitive complement; a bare noun follower is not infinitive-shaped. Context: "la [24] 85 93 [76-noun] 18" — 93+nominal-object is a plain transitive frame, not a governor frame. Kill grade.

2. **@1540: follower 88 = governor class (registry).** A governor cannot be infinitive-shaped. Context (val-93-1540, NULL 2026-10-09): "[62] [93-V] [88-gov] le ver" — the slot admits the full open class of semi-auxiliary governors, but 93's own follower is a governor, not an infinitive. Kill grade.

3. **@1761: follower 06 = 'ent' (PROMOTED).** The 3pl finite verb ending — "93 ent" is finite-verb-shaped, not infinitive-shaped. Kill grade.

4. **@479: follower 00 = 'pour' (GRANTED).** A preposition — "93 pour [13]" has 93 followed by "pour", not an infinitive. Kill grade.

5. **@102: follower 59 = 'est' (provisional).** A finite verb; the provisional status makes this a battery-grade-conditional leg, but it points the same way as the four kill-grade cases.

The only follower windows compatible with the governor reading are the class-open ones (62×2, 52×2, 54, 61, 50) and @111 ("93 er" — 29 is the pencil-GT infinitive ending, compatible with a stem+ending infinitive composition, but 93's stemhood is unvalued). Compatibility of open windows cannot carry C1 — the bar requires ALL 14 to agree, and four (five) do not.

## Scope

Kills only the semi-auxiliary-governor class candidacy for 93. Untouched: 93's verb-class grant (R19-166 stands), val-93-1540's NULL (value fenced, unnameable), 98='vient' LEAD, 94='ne' STRONG LEAD, §7. No standing/red-team verdict contradicted, downgraded, or re-litigated. No follow-ups required (kill, not null).

## Bookkeeping

- Queue: `gov-93-88-frame` queued → `status: verdict`, `result: kill`, 2026-10-09 (pre-write assert passed — was queued/verdictless; target-id-unique temp file `battery-queue.json.gov-93-88-frame.tmp` + atomic rename; disk re-validated; own entry only; no downgrade).
- Lock `locks/gov-93-88-frame.lock`: created on start (2026-10-09T19:50:11Z, agent dba5478b), deleted on completion.
- R5005, sealed gate instances, red-team adjudication queue untouched.
