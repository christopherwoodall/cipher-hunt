## geometer: WO3 clerk simulation — no behavior reaches observed strength; column-geometry structurally falsified
- Context: generative verification of the "soft column-rotation through a
  multi-column table" leading hypothesis. Toy 3-column table (~90 groups),
  Tocqueville syllable streams (T=1847), 6 pre-registered clerk behaviors ×
  20 replicates, lane's Jaccard-k12 pipeline run on every simulated stream.
- Decision: NO behavior reaches observed strength (bars: derived M1≥200,
  z≥+3.0, M3<0.8, ARI≥0.5). Medians — B0: M1=6.5/z=-0.38; B1: 30.8/-0.47;
  B2: 16.0/-0.28; B3: 30.6/+0.55; B4: 0.8/-0.25; B5: 15.9/+0.05
  (observed: 366.3/+5.61). Post-hoc B6 deterministic rotation: ARI=0.000;
  B7 strong-soft: ARI=0.043.
- Why: two sharp sub-results. (1) A taboo-2 "don't reuse a column used in the
  last 2 steps" memory DOES make lag-3 z≈+8-class rhythm at the process level
  (B3 true columns) — pure first-order rotation does not (B2 true z≈0.3–0.8),
  so the observed z=+5.6 needs ≥2nd-order memory IF columnar at all.
  (2) Structural mismatch: contact clustering NEVER recovers
  linguistically-arbitrary columns — ARI≈0 from null through DETERMINISTIC
  rotation — because contact profiles are dominated by syllable linguistics.
  The observed phases WERE found by contact clustering, so they cannot be
  arbitrary table columns.
- Enlightenment: the simulation inverted the hypothesis — instead of
  reproducing the rotation, it proved the instrument (contact clustering)
  couldn't have seen it if it were arbitrary columns. The column-geometry
  hypothesis is cornered: needs phases contact-recoverable AND linguistically
  incoherent (T1–T4 killed) AND number-unstructured (WO1) AND period-3 —
  no tested mechanism produces this. Demote it from "leading" to "needs
  independent evidence". Narrow surviving refuge: columns = an untested
  linguistic class (e.g. onset/coda phonotactics) — needs key recovery.
- For the report: rotation section — "WO3: 8 clerk behaviors simulated, none
  reproduces chi²≈366/z≈5.6; contact clustering structurally cannot recover
  arbitrary columns (ARI≈0 incl. deterministic); taboo-2 memory is the only
  mechanism generating lag-3-class rhythm (true z≈+8)."
- Caveats: toy (45 syllables, random column assignment, crude syllabifier);
  ARI≈0 rests on linguistic bigrams dominating contacts — robust for
  natural-language-like streams but not a theorem. Seeds deterministic;
  Red Team can re-derive exactly (code/side-rotation/redteam/ is empty —
  coordinator to task re-derivation).
- Evidence: code/side-rotation/geometer/wo3.json, wo3_clerk_sim.py,
  wo3_exploratory.json, wo3_exploratory.py, GEOMETER-FINDINGS.md.
