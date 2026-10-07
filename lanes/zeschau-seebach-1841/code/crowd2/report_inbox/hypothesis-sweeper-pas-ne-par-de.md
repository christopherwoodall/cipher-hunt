## hypothesis-sweeper: pas/ne/par/de

- Context: Work Order 5 told me to sweep the lane's remaining open hypotheses
  (H2 77="pas", H3 06="ne", H4 96="par"/"de", H4 41="der"/08="ni") with ≥2
  independent checks each, all rate checks against the era corpus (Tocqueville
  1835/1840 — Les Mis stays dead per F10), and to score a rival reading for
  every hypothesis rather than confirming. I chose the rival set to attack each
  hypothesis at its weakest joint: for 77, "que" (the other top-frequency
  particle), "plus" (the other negation particle), and the "ne"-swap; for 06,
  "de" and "le" (the two readings that survive on frequency); for 96, "pour"
  and "a/à" (both license a 96-87 frame); for 41/08, "ter" and "mer" (the other
  -er onsets that fit the @59 frame positionally). All numbers:
  `code/crowd2/hypothesis_sweeper_results.json` (script
  `code/crowd2/hypothesis_sweeper.py`, full scorecards
  `code/crowd2/hypothesis_sweeper_results.md`).

- Decision: (1) **Promote 96="par"** — CONFIRMED 4/4, the sweep's only
  promotion (joins as lane-inferred provisional value, 10th total; depends on
  87=ce). (2) **Refute 96="de"** (freq 6.4× miss — "de" would be rank ~1, 96 is
  rank 36), **77="plus"**, the **77="ne"-swap**, **06="de"**, **06="le"** (both
  on ungrammatical X→pas), **96="pour"**, **96="a/à"** (ungrammatical), and
  **41="ter"/"mer"** ("terniere"/"merniere" aren't words). (3) Leave
  **77="pas" INCONCLUSIVE** (4/3) and **06="ne" INCONCLUSIVE** (6/2) —
  unpromoted, with the evidence now pointing at a split: "pas" for 77 survives,
  "ne" for 06 probably doesn't. (4) Leave **41="der"/08="ni" INCONCLUSIVE**
  (2/1) — rate match 1.07× and anchored "-ière" frame vs a vocabulary-sensitive
  continuation miss, n=1. (5) Flag an **unscored lead: 06 = verb stem**
  (see Enlightenment).

- Why: the promotion bar is ≥2 independent checks with zero fails, and a
  grammatical contradiction is a hard fail (attempt-2 rule). 96="par" clears
  four genuinely independent legs: inflation-calibrated frequency (0.0114 vs
  0.0083, 1.37×), the "parce" compound rate (P(87|96)=0.1429 vs era
  n(parce)/n(par)=0.1274, 1.12×), the "parce que" frame (3/3 vs era 1.0000 —
  only after the qu-correction; v1's 0.3258 missed "parce qu'"), and
  function-word diversity (15/12). The kills are kills because the failing
  check is structural, not a rate wobble: de→pas and le→pas are ungrammatical
  (6 observed vs 0 era-expected), "de" fails frequency by 6.4×. For 77/06 I
  refused to promote despite 4–6 passes because the failing checks are the
  diagnostic ones: under 06="ne", P(77|06) should be ≈ infinitival "ne pas"
  adjacency (era 0.0063); observed 0.1304 is a 20.6× miss, and 06→29(er) is 5×
  against an era expectation of exactly zero. The one rival I could not kill,
  77="que" (INCONCLUSIVE 2/1), fails only on the ne→que count (6 vs 0
  expected) — conditional on 06="ne", so it reopens if 06 is revalued.

- Enlightenment: the aha was the era predecessor table for "pas": est 163, a
  102, sont 43, ont 41 … "ne" only 20/984 (2%, 7th place). In a syllabary, "ne"
  is followed by verb syllables, so a "ne" group should almost never sit
  directly before a "pas" group — the surgeon's original "06→77 13% vs 2.4%
  base (5×)" check compared against the wrong baseline (unigram base, not the
  era conditional), and the era conditional inverts it into a 20.6×
  contradiction. But the same table rehabilitates 77="pas" while executing
  06="ne": the cipher's top predecessors of 77 are 06 and 67 (6 each) — a
  verb-stem profile — and 06's own follower set (77 "pas" 6×, 29=er 5× as
  infinitive, 11=la 4× as object, 30 distinct predecessors) reads as a verb
  stem, not a particle. One rival hypothesis explains both of "ne"'s
  anomalies at once. Second surprise: the elision fix (n', qu') moved era
  P(que|parce) from 0.3258 to exactly 1.0000 — every "parce" in Tocqueville is
  followed by que/qu' — turning the weakest leg of 96="par" into its
  strongest, and moving the era ne/pas ratio 1.82 → 3.21 (the LesMis 0.959 is
  now a 3.3× register gap, same class as F10's cela gap).

- For the report: belongs in the hypotheses/findings section. The numbers
  that matter: **96="par" CONFIRMED 4/4** (compound 0.1429 vs 0.1274; frame
  3/3 vs 1.0000); **06→77 bigram 0.1304 vs era 0.0063 (20.6×)** — the joint
  "ne…pas" reading's central problem; **06→29(er) 5/46 vs era 0** — the
  second "ne" anomaly and the seed of the verb-stem lead.

- Caveats: (1) 96="par" depends on provisional 87=ce — if 87 falls, it falls.
  (2) The context-miner found a 64-96 window ("ce qui 96 47 que") where "par"
  doesn't parse but a verb does — tension noted, unresolved. (3) The 06
  verb-stem lead is unscored (no ≥2-check work order yet); the era verb-stem
  predecessor rates for "pas" (est→pas 16.6%, a→pas 10.4%) are suggestive, not
  checks. (4) H4c rests on n=1 with a vocabulary-sensitive continuation fail;
  the "derniiere" letter accounting (9 letters vs "dernière" 8) matches the
  crib's own "ière"=i+er+e convention from "première" but per/ber/ver onsets
  are unscored. (5) 67 (the other 6× predecessor of 77) is still unidentified —
  under the verb-stem theory it's the second stem; under "ne" it's unexplained.
