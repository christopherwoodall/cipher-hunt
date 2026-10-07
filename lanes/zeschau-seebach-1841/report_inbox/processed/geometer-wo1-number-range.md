## geometer: WO1 number-range test — NULL
- Context: testing the column-geometry hypothesis for the period-3 rotation
  (F43). If phases = physical columns/blocks of a printed table, group numbers
  should correlate with phase under natural print layouts.
- Decision: NULL — no number↔phase association. Pre-registered exact tests:
  phase×tertile p=0.569 (V=0.142), phase×(n mod 3) p=0.883 (V=0.089),
  runs test p=0.76. Kills column-contiguous and row-major numbering layouts.
- Why: the contingency tables are flat (A=[12,12,8], B=[8,11,8], C=[5,4,8]
  across tertiles). A coherent column story needed V≥0.40; observed ≤0.14.
- Enlightenment: the phases are aggressively number-indifferent — if there is
  a table, its numbering carries zero column information.
- For the report: rotation section — "WO1: phase×number-tertile p=0.57,
  V=0.14; phase×n-mod-3 p=0.88 — naive column-numbering layouts ruled out."
- Caveats: a table numbered in a non-obvious order survives this test.
- Evidence: code/side-rotation/geometer/wo1.json, wo1_number_range.py;
  prereg code/side-rotation/prereg_geometer.md.
