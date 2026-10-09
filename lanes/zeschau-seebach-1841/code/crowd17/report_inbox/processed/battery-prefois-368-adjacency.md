# Battery `prefois-368-adjacency` — verdict: KILL

## Pre-registered bar (verbatim from battery-queue.json)

"census '70 17' ('pre fois') adjacency stream-wide."

Numbered clauses:

- **C1.** Census every '70 17' adjacency on the repaired stream (byte-exact, ±context, row).
- **C2.** A licensed 1841-French collocation of a "pre"-final unit before "fois" re-opens the arm; confirmed absence at corpus grade kills the revival.

Bar copied before testing; not modified after seeing data.

## Claim

"census '70 17' ('pre fois') adjacency stream-wide; a licensed collocation revives the mid-clause."

## Method

Re-derived the repaired 1,847-pair stream in-session from
`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`,
parsed like `code/side-keyhunt/repair_parse.py` (asserts held: 1,847 pairs,
96 types). `canonical.py` never used. Corpus test over
`code/side-period/corpus` (76 texts, 34,526,989 chars; NFD-normalized,
accent-stripped, `[a-z]+` tokenization).

## Evidence

- **C1: '70 17' is a stream hapax.** Exactly 1×, 0-based @368 (1-based @368 for
  the 70 cell under the target's convention), row a2_06:
  `78 48 49 61 *70 *17 06 21 65 63`.
  70='pre' is pencil ground truth; 17='fois' is promoted. No other '70 17'
  adjacency exists in 1,847 pairs.
- **C2: corpus license test.** 3,129 'fois' tokens in 34.5M chars:
  - words ending in "pre" immediately before "fois": **0**
  - words ending in "pres" (e.g. "après") immediately before "fois": **0**
  - literal "prefois"/"pre-fois" tokens: **0**
  - "premiere" before "fois": 270 — the only licensed collocation, and it
    requires the "miè-re" syllables between "pre" and "fois" that the stream
    does not have at @368 (contrast the standing crib "11 70 82 34 29 40"
    = "la première", where 70 is followed by 82-34-29-40, not 17).

Per-clause: C1 PASS / C2 FAIL at kill grade — no licensed collocation exists;
the mid-clause stays closed. "préfois" is not a word, and no 1841-French
collocation licenses a bare "pre"-final unit before "fois".

## Verdict: KILL

Consistent with the standing `frame-367-la-pre` KILL (the five-cell
"première" crib kills the 70-as-"première" arm). No standing or red-team
verdict contradicted or downgraded; §7 intact; canonical-stream caveat
stands. Per §4, kills regenerate no follow-ups — none proposed.

## Adverses

None listed.

## Bookkeeping

- Queue: `prefois-368-adjacency` → `status: verdict`, `result: kill`,
  2026-10-09 (pre-write assert: was queued/verdictless; temp-file + rename;
  JSON re-validated from disk; own entry only; no downgrade).
- Lock created on start, deleted on completion (verified gone).
- R5005, sealed gate instances, red-team adjudication queue untouched.
