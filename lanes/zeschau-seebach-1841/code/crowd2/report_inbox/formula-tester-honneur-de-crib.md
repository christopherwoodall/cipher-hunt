## formula-tester: "J'ai l'honneur de" crib test + 9-mer drag

- Context: Work Order 2 gave me the linguist's H5 — the pair-aligned repeat
  `77 78 94 82 06` (2×, @1179/@1350) read as "J'ai l'honneur de"
  (j'ai·l'·hon·neur·de) — plus a crib-drag of the longest unread repeat, the
  9-mer `56 69 26 00 33 21 64 37 01` (2×, @931/@1625), against the era corpus.
  I chose this angle because H5 was the highest-value untested crib in the
  lane and it makes *falsifiable positional predictions*: the l'-slot must
  behave like a single-letter proclitic cell, hon–neur must look like an
  in-word boundary, and all five group rates must sit in the Meisel 1826
  diplomatic syllable tiers. A crib you can't kill is a crib you can't trust,
  so I built the test to kill it.
- Decision: **H5 REFUTED as stated — kill, do not promote.** Separately, the
  9-mer drag is a **clean NULL** (best corpus candidate killed by two
  cipher-side checks). Method decisions: (1) tier comparisons against
  Tocqueville syllable rates with a deliberately generous 3× acceptance band
  and the linguist's own 5–20× despatch-boost ceiling for je — I wanted H5 to
  survive if it possibly could; (2) promotion bar held at ≥2 independent
  checks per lane rule; a grammatical contradiction or structural anchor
  conflict counts as a kill by itself.
- Why: the kill does not come from the rates — it comes from a structural
  fact that no rate argument can rescue. H5 needs group **82 = "neur"**, but
  82 is a ground-truth pencil-crib anchor for the single letter **'m'**. A
  syllabary that gives single letters their own cells does not reuse the
  m-cell for a 4-letter syllable. The rates then independently bury it: 82 at
  2.06% (rank 10) is 67× too frequent for tier-3 "neur" (era 0.031%), and
  94 at 1.95% (rank 12) is 184× too frequent for "hon" (era 0.011%). Two of
  the five slots actually passed their tier checks (78=l' at 1.68% vs era
  1.48%, proclitic-like distribution with 21 distinct followers; 06=de at
  2.49% vs era 3.02%), and 77→78 co-occurs 7× as a bound chunk — but partial
  passes don't survive a structural contradiction. For the 9-mer, the top era
  candidate "seule différence qui existe" (×3) dies on cipher-side facts:
  it needs 00="fé", yet 00 is the rank-1 group of the entire text (×54,
  2.93%) while era "fé" is 0.19% — 15× too rare for the most frequent cell —
  and it needs 21="ce", colliding with provisional 87=ce.
- Enlightenment: two things changed my mind mid-run. First, the work order's
  own test spec had the positions off by one (it called the l'-slot "94?"
  and the hon–neur boundary "78→94"); under the stated 5-unit mapping the
  l'-slot is 78 and hon–neur is 94→82. Profiling both groups anyway is what
  surfaced the real story: **94→82 occurs 4×, twice outside the repeat**
  (@578, @1741) — more than the known in-word control 70→82 "pre-m" (1×).
  That recurrence is exactly what the formula-hunter's rival R4 predicts
  (94="ne", 82="m" inside "-nement" words like gouvernement/département),
  which is structurally compatible with 82=m. So killing H5 didn't just
  remove a hypothesis — it promoted R4 from "weak alternative" to the live
  reading for this repeat, and R4 now has a concrete next test (does 06="ent"
  behave as a word-final cell?). Second: the 9-mer sits between two anchors
  at @1625 (`…46=que | 9-mer | 74 87=ce 74 74`) — the drag target is real,
  the corpus just doesn't hand us a clean phrase, and the honest answer is
  null rather than the least-bad candidate.
- For the report: belongs in **Open hypotheses → H5**, recorded as refuted,
  and in **Null results** as a new N-entry for the 9-mer drag. The 1-3
  numbers that matter: (1) **82=m is ground truth; H5 needs 82="neur"** —
  structural kill, no rate debate needed; (2) **94 at rank 12 is 184× the era
  "hon" rate** (1.95% vs 0.011%); (3) **00 is rank 1 (×54) and cannot be
  "fé"** (15× rate mismatch) — this kills the best 9-mer drag candidate.
  Suggested follow-up for the report's next-steps: test R4 (94="ne",
  06="ent") as the live reading of the 77 78 94 82 06 repeat.
- Caveats: era syllable rates come from my own heuristic vowel-group
  syllabifier (±10% noise, per the linguist's caveat) — the 184×/67×/15×
  margins are far outside any syllabifier noise, but the 77=j'ai 47× figure
  leans on the 20× despatch-boost ceiling, which is the linguist's inference,
  not a measurement. 87=ce and 64=qui are provisional lane anchors, so the
  21="ce" collision is a caution, not a hard kill. The "de"+X grammatical test
  at @1179/@1350 was inconclusive for lack of anchor density — it neither
  confirms nor denies anything. All counts trace to
  `code/crowd2/formula_tester_results.json` (script:
  `code/crowd2/formula_tester.py`); full write-up in
  `code/crowd2/formula_tester_results.md`.
