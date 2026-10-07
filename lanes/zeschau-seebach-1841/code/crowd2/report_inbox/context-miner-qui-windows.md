## context-miner: qui-windows

- Context: Work Order 3 told me to exploit the two provisional anchors
  87="ce" and 64="qui" (F9). The obvious angle — "what verb follows 'ce qui'"
  — was a dead end by construction: the five immediate followers of 64 in
  the ce-qui windows (96, 23, 26, 59, 77) are all distinct, and era
  Tocqueville says the "ce qui" slot is a verb slot (est×32, se×28…), so
  variety is expected, not signal. I pivoted to the *other* side of the
  bigram: what precedes "ce". That found the real structure — 24→87 is 10 of
  32 "ce" predecessors (31%), and the trigram 24→87→64 occurs 3×. I also
  swept joint 87/64 windows (±4) and tested the 82→16 bigram (11×) against
  qui-windows, since attempt 3 had shown it avoids ce-windows. Era rates
  throughout are Tocqueville 1835/1840 only (F10 killed Les Mis for this).
  All numbers: `code/crowd2/context_miner_results.json`
  (script `code/crowd2/context_miner.py`).

- Decision: (1) Promote **24→87→64 as a formula** (trigram ×3, bigram
  24→87 = 31% of ce's predecessors, rank(24)=1) but **withhold any value
  for 24** — "tout" clears only the bigram-rate check (1.6×), "de" only
  rank, and "est" matches the trigram rate exactly (0.304 vs 0.30) yet is
  killed 19× over on the bigram rate. (2) Report **82→16 vs qui as a null**:
  2 within ±3 / 5 within ±5 of 64, both chance-consistent (P≥0.19); the
  ce-avoidance (0 within ±5 vs 2.1 expected, p≈0.12) stays suggestive but
  sub-significant. (3) Flag the exact 5-group repeat **64 96 43 87 01 ×2**
  as a formula-grade reverse joint ("qui … ce"), no value proposed.
  (4) Note — not kill — a tension for H4: window #1 reads
  "ce qui 96 47 que", where 96="par"/"de" doesn't parse but a verb
  ("ce qui fait que", era-attested) does.

- Why: the promotion bar is ≥2 independent checks per value, and none of
  the 24 candidates cleared two — promoting "tout" on the bigram rate
  alone would repeat the register-gap mistake F10 just corrected, because
  the rank check (era rank 76 vs cipher rank 1) and the trigram check
  (0.667 vs 0.30) both fail. The formula promotion rests on three
  independent legs instead: exact-trigram repetition (×3), predecessor
  share (31%), and top frequency rank. For 82→16 I used Poisson baselines
  (11 bigrams × window × target density / 1846) rather than eyeballing —
  the "5 near qui" that looks suggestive is λ=3.02-expected noise, and
  saying so plainly is the honest call.

- Enlightenment: the surprise was that the money was *before* "ce", not
  after "qui" — I'd gone in hunting relative-clause verbs and the verb
  slot gave nothing, while the preceding slot handed me the lane's
  strongest new formula. The second surprise was the "est" near-miss:
  era P(qui|"est ce") = 0.304 against cipher P(64|"24 87") = 0.30 is an
  *exact* match that still dies on the very next check — a clean
  demonstration of why the two-check rule exists. It also made me
  suspicious of word-level rate comparisons in general here: if 24 is a
  multi-use syllable rather than a word, every word-level P(ce|X) I
  computed is comparing apples to oranges, which is exactly why the
  formula (order + repetition, no semantics) is promotable and the value
  isn't.

- For the report: belongs in the **anchors/formulas section** as
  "24→87→64 ('? ce qui') ×3; 24→87 = 10/32 of ce's predecessors;
  rank(24)=#2 overall" — the three numbers that matter are **3 / 10-of-32 /
  rank 1**. Secondary, for the 82→16 thread: "0 within ±5 of ce (exp 2.1),
  no qui clustering (null)". Tertiary, for formula-hunter: the
  "64 96 43 87 01" ×2 exact repeat.

- Caveats: (1) Everything downstream of 87="ce"/64="qui" is provisional —
  if either anchor falls, the formula readings ("? ce qui", "qui … ce")
  fall with them, though the raw group-level counts (24→87 ×10,
  64-96-43-87-01 ×2) stand regardless. (2) Era rates are word-level;
  the cipher is syllabic — 24 may be a syllable, making P(ce|X)
  comparisons approximate. (3) My tokenizer counted 221,059 Tocqueville
  tokens vs attempt 3's 214,861 (same files); rates agree, raw counts
  differ slightly. (4) Joint-window co-occurrence counts (74×5, 84×5)
  are inflated by two overlapping frames at region @148 — true region
  counts are 4 and 4. (5) The H4 tension ("ce qui 96 47 que") is one
  window; 47 is unidentified and 96 may be polyvalent — noted, not a kill.
