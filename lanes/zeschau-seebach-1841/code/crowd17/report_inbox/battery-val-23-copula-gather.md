# Battery verdict: val-23-copula-gather

- Target: `val-23-copula-gather` (battery-queue.json, priority 3, status queued)
- Claim: gather the 1690 frequency-uniformity data for 23 vs 59 (homophony candidacy)
- Evidence field: battery-qui-fol-23-26-value NULL: 23/26 copula question; 1690 rule is the homophony gate
- Listed adverses: "62='il' kill-grade stands; polyvalence jurisdiction is §7/red-team"

## Bar (verbatim from battery-queue.json)

"corpus-rate comparison of 23 vs 59 under the 1690 rule; no naming, evidence only"

### Numbered clauses (operative)

1. Corpus-rate comparison of 23 vs 59 is delivered (stream rates + 1841-corpus 'est' rate).
2. 1690 frequency-uniformity data is delivered (runs test, follower/predecessor conditioning, frequency ratio).
3. No value is named; no adjudication is made (gather-only).

## Method

1. Read BATTERY-PROTOCOL.md in full before testing. Created `locks/val-23-copula-gather.lock` on start (agent 6ba9f833-86d4-4c89-8b41-75b2d406ff92, 2026-10-09T20:38:00Z); deleted on completion.
2. Re-derived the repaired stream in-session from `code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt` per `repair_parse.py`: 1,847 pairs, 96 types asserted. `canonical.py` never used.
3. Enumerated all 23-windows (n=8) and 59-windows (n=27) byte-exact with ±4 context; no prior counts trusted.
4. Corpus: `code/side-period/corpus/` — 97 files ≥500 bytes; 16 German-ish files excluded by und/et rate tag; 81 French files, 9,085,759 words, standalone "est" counted (elided forms c'est/n'est/s'est excluded by tokenization).
5. 1690 rule per lane law (BATTERY-PROTOCOL.md §7; homophone-86-split precedent): frequency uniformity is necessary but insufficient for homophony. Tests: runs test on the @-ordered 23/59 sequence (lane bar |z|>2), follower-profile comparison (A1={37,32,42} following rate, Fisher exact), predecessor conditioning (Fisher exact), and the 23:59 frequency ratio against petit-chiffre homophone-set practice (max observed imbalance 3:1, es×3).

## Evidence gathered

### Stream rates

- n(23)=8, n(59)=27, stream N=1,847 pairs.
- 23: 8/1847 = 0.43%; 59: 27/1847 = 1.46%; combined 23+59: 35/1847 = 1.90%.

### Corpus rate of 'est' (1841 French)

- 78,182 standalone "est" / 9,085,759 words = **0.86%** (81 French files).
- 59 alone (1.46% of pairs) already exceeds the corpus 'est' rate by 1.7×; combined 23+59 (1.90%) exceeds it by 2.2×.
- Caveat (directional): cipher pairs are not words — syllable groups inflate the pair denominator, so pair-fractions UNDERSTATE word-level rates; the true gap is likely wider. Not kill-grade: the letter is short and may be 'est'-heavy by topic; 59='est' is provisional standing.

### 1690 uniformity — runs test

- @-ordered combined sequence (23×8, 59×27): 11 runs vs 13.34 expected, z = -1.15, below the lane |z|>2 bar. No clumping detected — the necessary uniformity condition passes on ordering.

### 1690 uniformity — follower profiles

- 23 followers: {91×2, 37, 77, 09, 08, 99, 98}; 23→A1: 1/8 (12.5%, @182 only).
- 59 followers: {37×6, 35×3, 32×3, 42×2, 46×2, 36×2, 30×2, 39×2, 34, 38, 24, 45, 19}; 59→A1: 11/27 (40.7%).
- Fisher exact p = 0.216 — not significant; equal A1-following rates cannot be rejected (small n on the 23 side).

### 1690 uniformity — predecessor conditioning (HEADLINE)

- 23 predecessors: {45×3, 65×3, 64×1, 15×1}. 59 predecessors: {84×4, 94×3, 64×3, 44×2, 06×2, 61×2, …} — 45 and 65 never precede 59 (0/27 each).
- **45 precedes 23 in 3/8 windows vs 0/27 for 59: Fisher exact p = 0.0086 — significant.** The "ce [23]" context (45='ce' A11) is 23-exclusive; "ce [59]" never occurs.
- 65 ([noun,cls] registry) likewise precedes 23 in 3/8 vs 0/27 for 59.
- This is a genuine predecessor-conditioning signal: if 23 and 59 were freely interchangeable 'est' homophones per the 1690 order's vary-the-character rationale, the "ce _" slot should take both variants. The observed pattern is consistent with a positional convention (23 after 45/65, 59 elsewhere) — cf. the granted 23~26 positional split — or with 23 not being 59's homophone. Recorded as evidence; the interpretation is red-team venue.

### Frequency ratio

- 59:23 = 27:8 = **3.4:1**, at/beyond the edge of petit-chiffre homophone-set practice (max observed imbalance 3:1, es×3).

### 23 window inventory (re-verified byte-exact, 0-based)

| @ | window (±4) | note |
|---|---|---|
| 136 | `56 64 21 65 [23] 91 65 13 66` | — |
| 182 | `14 24 87 64 [23] 37 06 00 33` | copula leg (parent); 23→A1 |
| 679 | `64 37 77 45 [23] 09 07 00 92` | copula leg (parent) |
| 1056 | `29 74 74 45 [23] 77 84 09 98` | — |
| 1552 | `12 94 92 45 [23] 99 13 93 61` | — |
| 1609 | `39 11 92 65 [23] 08 55 83 71` | finite leg (parent) |
| 1697 | `24 85 58 15 [23] 91 85 33 94` | — |
| 1782 | `19 48 74 65 [23] 98 83 82 96` | — |

## Clause results

1. **C1 (corpus-rate comparison): PASS.** Stream rates (23: 0.43%, 59: 1.46%, combined 1.90% of pairs) and French-corpus 'est' rate (0.86%) delivered with stated caveats.
2. **C2 (1690 uniformity data): PASS.** Runs test (z=-1.15, passes), follower profiles (Fisher p=0.216, no rejection), predecessor conditioning (Fisher p=0.0086, significant — 45/65-predecessor is 23-exclusive), frequency ratio 3.4:1 delivered.
3. **C3 (no naming): PASS.** No value named for 23 or 59; no adjudication made. The homophony decision (polyvalence grant vs positional convention vs rejection) is §7 red-team jurisdiction exclusively. Listed adverses untouched: 62='il' kill-grade stands (not engaged by this gather); the 23~26 split holds; 59='est' stays provisional; no standing/red-team verdict contradicted or downgraded.

## Verdict: NULL (gather-only package)

Per the redteam-23-26-copula-input precedent, a gather-only null is a package, not an ending. The 1690 uniformity evidence for the 23-vs-59 homophony candidacy is assembled above: ordering uniform (passes), follower rates indistinguishable (weak, small-n), predecessor conditioning significant (p=0.0086, the one real tension), frequency ratio at the edge of period practice (3.4:1), corpus budget mildly negative (combined 2.2× the French 'est' rate pre syllable-adjustment).

## Follow-ups (for supervisor queuing; both verified ABSENT from queue)

1. `est-diplo-rate` (P4) — re-run the corpus 'est' rate on a diplomatic-letters-only subset of the corpus; sharpens the budget comparison for the red-team venue.
2. `hom23-59-pred-expand` (P4) — expand the predecessor-conditioning test: census all 45/65-preceded copula slots stream-wide; a single 59 after 45/65 would soften the p=0.0086 signal.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-val-23-copula-gather.md`
- Queue: `val-23-copula-gather` queued → `verdict`/`null`, 2026-10-09 (pre-write assert passed — was queued/verdictless; target-id-unique tmp `battery-queue.json.val-23-copula-gather.tmp` + rename; disk re-validated; own entry only; no downgrade; no tmp leftover)
- Lock `locks/val-23-copula-gather.lock`: created on start, deleted on completion (verified gone). R5005, sealed gates, red-team adjudication queue untouched.
