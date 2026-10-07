# RUN-PROTOCOL — Seebach homophonic solver (Runner)

Updated 2026-10-07 ~10:45 CDT after the canonical parse repair (F32, key-hunt
red team). Supersedes any earlier statement in runner notes that cites the
1,846-pair parse for real data.

## Real data (post-gate only) — REPAIRED PARSE

- Canonical parse version: `code/side-keyhunt/repaired_offsets.json`
  (md5 `40521e174deaa2bfbc179443283c615e`), superseding
  `data/upstream-offsets.json`. Full ruling: `code/side-keyhunt/methodology-ruling.md`;
  remap: `code/crowd4/REINDEX.md` (md5 `ecfcfccf54848edb83c89be14801620a`).
- The fix: flip `offsets['a5_03']` 1 → 0 (raw 12-digit crib `117082342940`
  starts at raw offset 1532 = even, so pair-phase there must be even).
- New canonical facts (0-based pair indices):
  - **1,847 pairs** (not 1,846); same 96 groups; same pair IC (0.0142).
  - `11 70 82 34 29 40` ("la première") at pairs **754** (row a5_03, the gloss
    line) AND **1034** (row a6_03). The despatch says "la première" twice.
- Post-gate run asserts: `len(pairs) == 1847`, `len(set(pairs)) == 96`,
  crib landmark `11-70-82-34-29-40` present at BOTH 754 and 1034,
  row a8_05 ends with `46`. Any violation → STOP, do not score, report.

## Loader gate (HARD)

- `solver/ct_loader.py` is currently STALE: it reads
  `data/upstream-offsets.json` and asserts 1846 pairs.
- The Solver Smith is repointing it at the repaired offsets.
- **DO NOT run the real-data adapter until the Smith confirms byte-level
  landmark re-verification** (crib @754 and @1034 verified in the adapter's
  actual output, not just claimed).

## Synthetics — UNCHANGED

- Control instances remain 1,846-pair, self-consistent, and byte-identical.
- No change to control scoring or the §4 bars.

## Verdict bookkeeping

- When re-deriving the gate verdict, record BOTH alongside the numbers:
  (a) frozen solver code md5, (b) parse version
  (`repaired_offsets.json` md5 above).
- The gate verdict is only registrable on frozen code AND the repaired parse.

## Demonstrated failure mode (do not forget)

- The key-hunt fleet's table-tester **false-negatived a true key under the
  old parse**. Any result produced under the 1,846-pair parse (old offsets)
  is suspect — including, retroactively, all of this lane's real-data work
  to date. Old-parse outputs are not evidence; do not cite them.
- Caveat recorded in REINDEX.md: the manuscript images were not re-examined.
  If the a5_03 gloss line-tag is wrong, the old parse revives — uncertainty
  recorded, not resolved.
