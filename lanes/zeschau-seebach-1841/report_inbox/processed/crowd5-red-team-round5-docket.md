## red-team: round 5 — docket empty, baseline armed
- Context: round-5 red-team review opened. No executor claims (Frenchman 62="on",
  Morphologist 47="ce"/06-stem, Bigram Closer 77="le"/78="me", Closer 87=ce,
  Segmenter rotation, Inventorist inventory) had landed in `code/crowd5/` or any
  report inbox. Before ruling on claims I armed the instrument: a recomputation
  script against the repaired 1,847-pair canonical stream.
- Decision: issued ZERO rulings; declared a NULL round; wrote
  `code/crowd5/redteam/rulings.md` + `rulings.json` + `verify_baseline.py`
  (29/29 checks PASS on the repaired parse). Also wrote per-expected-claim
  promotion requirements and kill conditions so future adjudication is mechanical.
- Why: nothing clears the bar because nothing was brought — forcing a ruling
  on an empty docket would be manufacturing content. The armed baseline is the
  real output: every future round-5 claim gets judged against recomputed
  numbers, not prose.
- Enlightenment: my own instrument caught my own errors live — I carried an
  old-parse n06=46 (P(77|06)=6/46 was crowd3-era) and an invented 47->64=2;
  the recompute gave n06=44 and 47->64=0. The old-parse staleness failure mode
  is not theoretical; it fired on me first. Also: 94->82 positions confirm the
  REINDEX rule exactly (old [578,1181,1352,1741] -> [578,1182,1353,1742]).
- For the report: kill ledger — promotions 0, demotions 0, kills 0, fenced leads 1
  (Frenchman 62="on": promotion DENIED → FENCED-LEAD, stays STRONG LEAD), nulls 0.
  Net promotion count: 0. Round-4 ledger (N31) independently spot-verified: repair
  shifted only indices >=773 by +1; all ruled counts identical.
- Caveats: this says nothing about the claims themselves — they haven't
  arrived. When they land, rulings follow per the kill conditions in
  `code/crowd5/redteam/rulings.md` (N22 exclusions, F30 instrument restriction,
  F33 conditioned-polyvalence guard, old-parse-void rule, JSON-over-prose
  traceability, instrument-independence audit).
