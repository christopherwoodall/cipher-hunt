## red-team: word-pattern side fleet adjudication — fleet verdict
- Context: kill-authority review of the two side-fleet executors (pattern-matcher
  HONEST NULL + polyvalence-tester VALID-WITH-RESTRICTIONS). I re-derived the
  matcher's ground-truth control from the lexicon directly, re-ran both tester
  scripts, rebuilt the canonical 1,847-pair stream to re-check islet counts, and
  enumerated all 26 stamped proposals from `match_results.json`.
- Decision: (1) the matcher's control failure is SOUND — the diérèse attack fails
  (lexicographer uses maximal i|è splitting and still never yields m|i; standalone
  'm' is phonotactically impossible in French; the gap is proven by the pencil cribs,
  not the syllabifier). Scope note: it is effectively a single-unit ('m') test, not a
  4-anchor test. (2) All 26 proposals stay DEAD — 7 quiconque = provisional-64=qui
  echo, hapax accidents (freq ≤17, zero with ≥2 GT anchors), variant artifacts;
  the tester verdict resurrects none (it governs recall; restriction 4 kills
  "pionnier" harder via 06="ni" inconsistency). (3) Tester verdict stands as
  VALID-WITH-RESTRICTIONS with amendments: R1 strengthened (expanded index
  unconditional — the swallow-loss alternative fails under determinism), R3 demoted
  to instrument-level recommendation (over-restrictive as a gate), R6 extended to
  parse/inventory changes (islet spot-checks are old-parse; se weight basis went
  n=5→n=6, 0.6/0.4→0.5/0.5 — verdict robust: 0.380→0.375), R7 fenced as
  non-implementable scope delimiter, new R8 (prefer orth alphabet for
  repetition patterns — orth survival 1.000). Traceability flag: the §6 synthetic
  table's K≥3 repetition-survival numbers (0.914/0.891/0.879) do NOT reproduce from
  archived code (code: ~0.93–0.94/~0.93–0.94/~0.90–0.93) — regenerate, don't cite.
  (4) @507 NULL reframed: zero constraint on 77∈{pas,le,que} — fully explained by
  per|son|ne vs pers|on|ne cutting mismatch; corroborates F30. cela+X NULLs:
  non-evidence, open segmentation question (Viterbi itself glues; miss rate ~28%).
- Why: every headline number was re-derived, not trusted. Tester §2 table and §3b
  smart-expansion (3|AAB 2→12 = 6.00x; 5|ABCDA 4.33x; 3|ABA 1.13x) reproduce exactly;
  the control (m|i|er|e → 0 hits both alphabets) reproduces; the lone-'m' entry is
  the elision token itself. The two verdicts compose exactly as the tester claimed:
  inventory mismatch is the binding constraint, polyvalence is gated but orthogonal.
- Enlightenment: the fleet's most valuable output is not a reading but a proven
  negative with a reusable gate — the honest null plus 8 adjudicated restrictions is
  the instrument spec for round-4 WO5. And the WO5 pointer needs correcting:
  `data/upstream-syll*.py` is suspect per N29; the inventory must be LEARNED from
  cribs + recovered readings, not adopted upstream.
- For the report: Pattern-matcher section. Numbers that matter: control 0 candidates
  (both alphabets, all tiers); 'm' in 1/11,870 entries (the token itself); 26
  proposals = 12 unique words, 0 with ≥2 GT anchors, max freq 17; forward survival
  0.995 / at-risk 0.834 / se-split 0.38 (q=0.5, reproduced); smart ≤6.0x vs dumb
  202x–2318x (reproduced); 52 at-risk words verified. Merge: N32 (matcher null),
  N33 (polyvalence gate), F34 (@507 reframe), F35 (old-parse staleness), R1–R8
  adjudicated. Full rulings: `code/side-wordpattern/redteam/ADJUDICATION.md`.
- Caveats: matcher ran on old 1,846-parse (positions old-parse); I did not re-run
  the matcher's full 367/301-word sweep; re-running `synthetic_breakdown.py`
  overwrote its archived JSON (code is source of truth); tester q unidentified
  (swept) — verdict holds across the sweep.
