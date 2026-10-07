# side-keyhunt — TESTER harness

Tests candidate key tables against the canonical R5005 ciphertext.

## Files
- `test_table.py` — the harness. CLI: `python3 test_table.py --table table.json [--out report.json] [--name label]`. Table format: JSON object, two-digit group → syllable, e.g. `{"11": "la", "70": "pre", ...}`.
- `canonical.py` — the canonical 1,846-pair sequence (self-validating on load: 3,764 digits / 1,846 pairs / 96 groups / anchor run at pair 1033 exactly once). Import `load_canonical_pairs()`; do not hand-roll a parse.
- `build_syll_model.py` — builds `syll_bigram.json`, a French syllable-bigram reference from Tocqueville 1835–1840 (same era/register as the 1841 French despatch). Secondary score only.
- `syll_bigram.json` — the built model (449,727 syllables, 41,357 bigrams).
- `dummies/` — validation fixtures: `dummy_wrong.json` (must MISS), `dummy_anchors7.json` (NEAR-MISS, partial), `dummy_full_random.json` (NEAR-MISS, low score).
- `report_inbox/tester.md` — report-inbox note for the 2-hour report sweeper.

## Verdicts
- HIT: 7/7 ground-truth anchors + exact "la première" at pair 1033 + all 96 groups mapped + quadgram ≥ −5.5/char.
- NEAR-MISS: no contradiction, but partial table or non-French score. **Not a hit.**
- MISS: anchor contradiction, broken "la première", or quadgram < −6.5/char.

87=ce / 64=qui / 96=par are provisional secondary checks only — they never gate a verdict.

Note: `code/crib_attack.py::qscore` always returns floor (it scores against the dict that nests the real table under `'logp'`); this harness scores against `logp` directly. Do not reuse that function for table scoring.
