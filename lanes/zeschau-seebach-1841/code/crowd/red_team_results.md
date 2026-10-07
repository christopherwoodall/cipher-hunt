# RED TEAM vs 87=ce — attempt 2's "CONFIRMED 4/5"

## VERDICT: WEAKENED (demote to PLAUSIBLE/provisional; kill the "CONFIRMED" label)

The claim under kill authority — "87=ce CONFIRMED 4/5" — does not survive. The
hypothesis 87=ce is **not refuted** (it remains the best-tested reading of the
follower pair la×7 / que×3), but the 4/5 scorecard is unsound: one check is
computed from a mislabeled quantity, two are non-discriminating, one is an n=3
comparison, and the fifth tests an unconfirmed premise while missing the real
conditional structure in the data. The active contradiction is joint
(24=est ∧ 87=ce), not isolable to 87 alone.

All numbers below re-derived from lane data via `load_pairs()` (code/crib_attack.py)
and the lane-local Les Mis copy. Attempt-2's raw counts reproduce exactly.

## Check-by-check

- **(a) rank(87)=15 < 25** — REPRODUCED (15, n=32). NON-DISCRIMINATING: the same
  check passed for the refuted de/à hypothesis. Says "frequent", says nothing
  about *which* word. Threshold 25 is arbitrary.
- **(b) P(11|87)=0.2188 ≈ P(cela|ce)=0.2778** — REPRODUCED numerically, **reference
  MISCOMPUTED**. 0.2778 is `n_cela/n_ce` = 295/1062, a *word-frequency ratio*,
  not P(cela|ce). True word-bigram P("cela"|"ce") = 0/1062 = **0.000000**
  ("ce cela" never occurs as two words). Honest syllable-level reference —
  P("la"-syllable follows "ce"-syllable) ≤ 295/1634 = **0.1805** (upper bound;
  denom = word-`ce` 1062 + demonstratives 529 + recevoir-family 43) — and the
  observed 0.2188 *exceeds* that bound. Still inside the arbitrary 2× gate, but
  the gate is meaningless (P(la|de)=0.131 passes it too) and the check's stated
  logic is void.
- **(c) P(que|87)=0.0938 ≈ P(que|ce)=0.1403** — REPRODUCED. Legitimate level
  (cross-word bigram on both sides). But n=3: Wilson 95% CI **[0.032, 0.242]** —
  weak evidence, not confirmation. Does discriminate vs pour/sans (below).
- **(d) 14 distinct predecessors ≥ 8** — REPRODUCED
  (24×10, 29×3, 96×3, 56/76/43/79/81×2, six ×1). NON-DISCRIMINATING: identical
  check passed for de/à.
- **(e) trigram 24-87-46 = 0** — REPRODUCED (bigram(24,87)=10, trigram=0).
  **Tests an unconfirmed premise: 24=est is NOT in ANCHORS** (candidate-list
  only). If 24=est holds: Les Mis P(que|"est","ce")=67/133=0.504 →
  binomial P(0/10 "que") = **9.1e-04**, an active joint contradiction. Worse,
  non-"que" followers of "est ce" in Les Mis are qu'×17 / pas×16 / qui×15, but
  the cipher's 10 followers are 11×3 / 64×3 / 98 / 61 / 59 / 08
  (cela/ceci-shaped) — matching *neither* "est-ce que" *nor* "est-ce pas/qui".
  Sentence-boundary rescue ("est. Cela"): 0/8 such sentences in Les Mis.
  **Unreported reframing:** P(46 | 87, pre=96) = **3/3** vs P(46 | 87, pre=24) =
  **0/10** vs 0/19 otherwise — the "que" after 87 is perfectly licensed by
  predecessor 96 (n=21, rank 35), never by 24. Attempt-2 never reported this
  conditional structure.

## Unexplained under 87=ce

- **87→64 ×5 (15.6% of followers):** the natural "ceci" rescue fails — 64≠"ci":
  34→64 ("ici") = 0 and P(87|64) = 5/46 = 0.109 ("ci" almost always follows ce-).
  64 (n=46, rank 4) is an independent frequent group with no reading under "ce".
- **87→24 = 0** ("c'est" never, if 24=est) — secondary.
- **Downstream payoff zero:** drag re-run with provisional 87=ce yields only
  invalid-French best windows ("vousla", "votree", "toutee", …). A "confirmed"
  anchor that unlocks nothing.

## Best alternative reading tested

- **87="pour"**: P(la|pour)=0.0548 in Les Mis — observed 0.219 is 4.0×, outside
  the 2× gate; P(que|pour)=0.0145 — outside the Wilson CI [0.032, 0.242].
  **Worse than ce** on both discriminating checks (Les Mis register; a 4–6×
  diplomatic-register shift is implausible but not quantified — register caveat).
- **87="sans"**: P(la|sans)=0 in Les Mis and no within-word "sansla" exists →
  **REFUTED** by 87→11 ×7.
- **87="de"/"à"**: refutation upheld (87→46 ×3 ungrammatical).
- même/plus/bien/tout: fail la- or que-follower grammar.
- **No tested alternative beats ce.** The kill fails on the alternative-reading
  front; it succeeds on the scorecard-integrity front.

## What would settle it

1. Independently establish or kill **24=est** ("la 24"×4, "que 24"×3 support it;
   decisive: identify 24 via followers 85×5, 82×4). If 24=est firms up, the 0/10
   "que" becomes a hard problem for 87=ce.
2. Identify **group 96** (n=21, rank 35): 96="tout" → "tout ce que"×3 **locks**
   87=ce; 96="de" → "de ce que"×3 also locks it. 96's reading decides the
   que-licensing question.
3. Identify **group 64** (n=46, rank 4): 16% of 87's followers unexplained.
4. Era/register-matched reference (1840s diplomatic French) for honest
   P(la|ce-syllable), P(que|ce) — Les Mis 1862 novel is the wrong register, and
   reference quantities must match the cipher's level (syllable vs word).
5. More text: n=32 makes every honest check wide-CI.

## Method notes for the curator

- Reference quantities must match the cipher's level: group bigrams spelling
  within-word ("cela") need *syllable*-level references; cross-word bigrams
  ("ce que") need *word*-level references. Attempt-2 mixed them (check b).
- The 2× factor gate against 1862-novel rates cannot "confirm" anything about
  1841 diplomatic French. Recommend retiring factor-gate confirmations until an
  era/register-matched corpus exists.
- Report conditional structure (P(next | group, predecessor)), not just marginal
  follower counts — the 96-vs-24 licensing split was invisible in the marginals.
