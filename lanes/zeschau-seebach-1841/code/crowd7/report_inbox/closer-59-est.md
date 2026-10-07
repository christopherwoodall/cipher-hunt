## closer: 59="est" promotion battery (round-7 work order 7)

- Context: 59="est" sat at STRONG LEAD (F45) with red-team DENIAL of
  provisional on two genuine blockers: (a) S4 "est que" 5.41× adverse (n=2,
  59→46 @216/@1190); (b) the 01="est"-lead interaction (87→59 @824 "c'est"
  vs 01="est" MEDIUM + A1's "c'est"×3 count). Battery pre-registered at
  `code/crowd7/closer/PRE-REGISTER.md` BEFORE running (legs L1–L5, I1–I3,
  verdict rule). Corpus: `code/side-period/corpus/` French files,
  elision-split tokenization; primaries Guizot t5–t6 (his 1840–42 despatches)
  and Nesselrode v8 (actual 1840–46 correspondence, full 1841 run).
  Script: `code/crowd7/closer/diplomatic_rates.py` → `diplomatic_rates.json`.
  Cipher facts re-derived from the repaired 1,847-pair parse
  (`verify_baseline.load_stream`); positions per `verify_f26_17.py` (61/61).

- Decision: **PROMOTE 59="est" to provisional** — recommendation; red-team
  sign-off required (kill authority over round-7 promotions; this is not a
  merge). Both blockers resolved; 4 independent legs pass (need ≥2).

- Why — blocker (a) S4, resolved as small-sample artifact (L1 PASS):
  diplomatic P(que|est) = 0.0213 Guizot t5–t6 / 0.0414 Nesselrode v8 / 0.0249
  aggregate — 1.5–3× Tocqueville's 0.0137, driven by "c'est que" /
  "ce n'est que" / "NP est que" clefts (51 hits Nesselrode v8, 40 Guizot;
  sampled: "c' est que l' empereur", "ce n' est que depuis cinq",
  "ma conviction est que lord normanby"). Binomial: P(X≥2|n=27) = 0.11
  (Guizot) / 0.31 (N8) / 0.14 (all) — none < 0.05, NOT a significant
  contradiction. Ratio shrinks 5.41× → 3.48× / **1.79×** / 2.97×; cipher
  95% CI [0.009, 0.243] contains Guizot's rate. The "5.4×" was a
  point-estimate on n=2 against the wrong register.
  L2 (structural) FAILS as pre-registered — S4#2 (84-59-46-07) admits the
  cleft frame only conditioned on 84=noun (live LEAD, work-order-1
  territory); S4#1 (06-59-46-29) admits no licensed frame under banked
  values. Rate-resolved, not frame-resolved; verdict rule needed L1 OR L2.

- Why — blocker (b) 01-interaction, resolved as mutual exclusivity (59 wins):
  I1: joint (27+28)/1847 = 0.02978 → 2.24×–4.73× over diplomatic P("est")
  (2.24× N8 / 4.73× Guizot / 3.72× agg; pre-reg bar >3× rejects
  both-hold-as-same-word on Guizot+aggregate, borderline on N8).
  I2: 01's profile IS verb-shaped (37→01 ×3 "l'est"?, 87→01 ×2 "c'est",
  47→01 ×1; followers 11/77 "la"/"le") — not profile-killed. But
  qui/ne+"est" frames go 6/6 to 59, 0/6 to 01 (p=0.014 under the observed
  27:28 usage split), and 01/59 share 6 predecessors (15,16,48,76,86,87)
  and 2 followers (19,24) — overlapping, not complementary, distributions:
  no clean conditioning rule, so unconditioned both-hold = free allophony
  plus a joint-unigram over plus two coincidences (S1's rate match, the 6/6
  split). F33 tolerates allophony as a class but the conjunction disfavors
  it. I3: @824 frame hostile under banked values ("en ce est"/"en c'est"
  under 24="en" STRONG) — @824 neither corroborates nor refutes; the
  allophony claim there is unsupported (caveat: rides on 24="en", a lead
  with its own rate tension). 59's legs are 01-independent, so 59's
  promotion is not blocked by 01 either way.

- Why — re-verification legs all hold on diplomatic rates:
  L3 (S2): 64→59 ×3/47 = 0.0638 vs P(est|qui) 0.026/0.085/0.033 →
  2.45×/0.75×/1.92×, P(X≥3) = 0.12–0.78 n.s. PASS.
  L4 (S3): 94→59 ×3/37 = 0.0811 vs diplomatic P(est|n') 0.134/0.230/0.192 →
  0.35–0.61× in-band low. PASS.
  L5 (rivals re-killed): doute 40.4× / dit 16.5× / fait 9.1× / veut 50.9× /
  peut 12.6× away from cipher P(59) = 0.01462 — kills STAND (stronger than
  Tocqueville's 7–45×); "est" unique survivor at 1.10× vs Nesselrode v8
  (S1 refreshed: 1.10× N8 / 1.83× agg — actual 1841 correspondence is the
  right comparator, not memoir narrative).

- Enlightenment: the S4 "adverse" dissolved the moment the register was
  right — diplomatic French says "est que" 1.5–3× more than Tocqueville
  because despatches are built out of "c'est que / ce n'est que" pivots.
  And the 01/59 overlap killed the comfortable "conditioned allophony"
  story: they share "c'est"-frames (87→both), so any split rule would be
  post-hoc on n=3. Parsimony says one of them isn't "est", and 59 holds
  three banked legs against 01's single ear window.

- For the report: 59="est" → provisional (pending red-team sign-off).
  The 4 numbers: S4 P(X≥2) = 0.11–0.31 n.s.; S1 1.10× vs Nesselrode v8;
  rivals dead 9–51×; 01/59 mutual-exclusivity (joint 2.2–4.7× over,
  qui/ne 6/6→59 p=0.014).

- Caveats / remaining blockers:
  1. Red-team sign-off REQUIRED before any status change (kill authority).
  2. S5 (59→37 ×6 "[c']est le", 6.47× over) stays fenced on 37="le" MEDIUM —
     not re-litigated here.
  3. S4#1's frame (06-59-46-29) remains structurally unexplained; the
     blocker is resolved statistically, not grammatically.
  4. RECOMMEND 01="est" MEDIUM → WEAK/disputed (red-team call): consequence
     is A1's "c'est"×3 (87→01 @344/@1028 + 47→01 @194) needing re-reading
     if 01 falls — flagged for 87=ce, not adjudicated here.
  5. L2's failure is on record: no licensed "NP est que" frame for S4#1
     under banked values (06 = verb-stem class, not noun-typed).
  6. Factor-2 band still uncalibrated (F26-1); raw ratios reported
     throughout. Guizot t5–t6 mixes memoir narrative with printed
     despatches — Nesselrode v8 (actual letters) is the cleaner comparator.
