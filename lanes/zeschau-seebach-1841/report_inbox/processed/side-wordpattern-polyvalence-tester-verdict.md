## polyvalence-tester: gate verdict — VALID-WITH-RESTRICTIONS
- Context: I gate the side fleet's Pattern Matcher: does repetition-pattern
  matching survive the cipher's polyvalence (06=/ɑ̃/ vs /mɑ̃/, 94=ne/en,
  52=pas/se, 59/52=se)? Exact-enumeration simulation over the 11,870-word
  Tocqueville lexicon, forward (recall) + reverse (precision), plus a
  synthetic "+30 islets" breakdown. Islet inventories re-derived from the
  pair stream and spot-checked vs NOTES.md (all match).
- Decision: **VALID-WITH-RESTRICTIONS** — the matcher may run, but NOT naive.
  Use the polyvalence-expanded index (each word filed under all its
  reachable cipher patterns; ≤6x precision cost, 100% recall on known
  islets). Never naive pattern-expansion (202x–2318x candidate inflation —
  e.g. 3|ABA: 23→4,659 — kills the instrument). Full restriction list
  (7 items) in `code/side-wordpattern/polyvalence/POLYVALENCE_REPORT.md` §5.
- Why: known islets cost the naive matcher <1% recall overall (0.995 at
  q=0.5) — patterns survive. Damage concentrates in 52 identifiable at-risk
  words (8 mechanisms enumerated; worst: se→52/59 split on
  "sérieuse"/"sérieusement", survival 0.38). Smart expansion inflation ≤6x
  (3|AAB 2→12); dumb expansion 200x+. Synthetic +30 rhyme-pair islets:
  graceful degradation (repetition recall 0.931→0.879), so unknown
  polyvalence "of the same shape" doesn't break it either.
- Enlightenment: polyvalence is a scalpel, not a hammer — it only distorts
  where specific syllables co-occur in interacting positions (52/1597
  words). The real threat isn't recall loss (tiny) but the temptation to
  recover it via whole-pattern-class expansion (fatal). The fix — filing
  words under reachable patterns — is cheap, exact, and already computed
  (`polyvalence_test.py` + `results.json`).
- For the report: Pattern-matcher gate section. Numbers: forward survival
  0.995 overall / 0.834 at-risk / 0.38 se-split at q=0.5; reverse smart
  inflation max 6.0x vs dumb 202x–2318x; 52 at-risk words, 8 mechanisms;
  synthetic K=30: repetition survival 0.879. Files:
  `code/side-wordpattern/polyvalence/` (report, code, results.json,
  synthetic_breakdown.json).
- Caveats: q (polyvalent-group penetration) unidentified — swept 0.05–0.9,
  verdict holds across it; se→52/59 0.6/0.4 rests on n=5; an→06/94 split
  assumed uniform; per-position independence assumed; systematic unknown
  polyvalence (06 verb-stem provisional) is the residual risk — re-run on
  model change (§5.6). Segmentation mismatch (F30) is a separate, larger
  threat to (n, pattern) lookup, independent of polyvalence.
  Note: the pattern-matcher sibling's HONEST NULL
  (`report_inbox/pattern-matcher-proposals.md`) is an ORTHOGONAL failure —
  lexicon unit inventory lacks the cipher's by-ear units (standalone m/i;
  4-anchor "première" tail unrecoverable) — and stands independently of
  this verdict. This gate covers polyvalence only; the inventory mismatch
  is the binding constraint. Fix inventory (round-4 WO5) first, then §5.
