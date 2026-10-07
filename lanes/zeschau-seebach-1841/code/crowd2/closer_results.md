# CLOSER verdict — crib-surgeon H1: 24 = "est" → **REFUTED**

Worker: closer (crowd round 2). Code: `code/crowd2/closer.py` (deterministic;
reuses `crib_attack.load_pairs`). Numbers: `code/crowd2/closer_results.json`.
Corpus (mandated): Tocqueville t1+t2 (1835/1840, 214,861 words, formal prose),
attempt-3 tokenizer. Les Mis figures are diagnostic only, to map the register gap.

## Verdict

**24="est" is REFUTED under the lane's era-matched standard.** It fails two of
its four original checks by more than an order of magnitude (B: 19.5×, C: 74×),
fails two further independent profile checks, and every named rival plus an
inversion sweep over 45 function words fails with it — the cipher's 24-profile
(no V with P(ce|V)≈0.19 ∧ P(V|que)≈0.10) matches nothing in the era corpus.
Two of the four refutation legs hold under *both* corpora, so the verdict does
not rest solely on the Tocqueville-vs-Les-Mis register choice. 24 stays
**unidentified**; "est" is out.

## The four original H1 checks, re-graded vs era

| # | Original check | Cipher (bytes) | Era rate | Grade |
|---|---|---|---|---|
| 1 | rank-1 frequency band | 24: freq 52, **rank 2/96** (1-based; H1's "rank 1" was 0-based), share 2.82% | "est": rank 15, share 1.08% | **DOWNGRADED** — rank 2 vs 15; share 2.6× |
| 2 | P(ce\|24)=0.192 vs 1.7% base | P(87\|24)=10/52=0.1923; base P(87)=32/1846=0.01733 (11.1×) ✓ cipher side reproduces | P(ce\|est)=23/2331=**0.0099** | **FAIL — 19.5×** outside factor-2 |
| 3 | "qu'est" elision ×3 (46→24) | 46→24 = 3/29 = 0.1034 @546,953,1691 ✓ | P(est\|que,qu)=7/5012=**0.0014** | **FAIL — 74×** |
| 4 | P(ce\|est) within 2× (was Les Mis 0.118) | same as #2 | era 0.0099 replaces Les Mis 0.118 | **FAIL** (see #2) |

(Cipher-side counts all reproduce the surgeon's: 10× 24→87, 3× 46→24,
0× 24-87-46, 3× 24-87-11, 3× 24-87-64, 0× 24→46.)

## The refutation — four independent legs

**Leg 1 (check B, follower rate).** Observed P(87|24)=0.1923 vs era
P(ce|"est")=0.0099 — 19.5× outside the factor-2 band. *Instrument-dependent:*
under Les Mis P(ce|est)=0.1177 it passes (1.6×) — the 11.9× Les-Mis/Tocqueville
register gap on this exact bigram is itself a finding (see below).

**Leg 2 (check C, predecessor rate) — instrument-INDEPENDENT kill.**
Observed P(24|46)=0.1034 vs era P(est|que,qu)=0.0014 — 74×; vs Les Mis
0.0156 — still 6.6×. Structural reason it can never close: "est" needs a
subject, so "que"+"est" adjacency is ungrammatical outside "qu'est-ce";
Tocqueville has "qu'est" 7× in 214,861 words (4× "qu'est-ce", 3×
"qu'est"+participle: "devenu", "né"). The cipher demands it at 10.3% of
"que". No register rescues this — even dialogue-heavy Les Mis is 6.6× short.
Kill-shot corollary: era "qu'est" is followed by "ce" 4/7; cipher 46-24 is
followed by 87 **0/3** (positions 546, 953, 1691 → followers 47, 85, 85).

**Leg 3 (predecessor profile) — instrument-INDEPENDENT kill.** Cipher's top
predecessor of 24 is **11=la ×4** (@164, 731, 781, 1655; 7.7% of 24's 52
occurrences). Era n("la","est")=**0**; Les Mis n("la","est")=**0**. ("là"+"est"
is 2 in both corpora — negligible.) No homophony rescue works: 11="là" gives
"là est" ≈ 0, 11="l'" gives "l'est" = impossible.

**Leg 4 (follower profile of 24-87).** Cipher: {11:3, 64:3, 98/61/59/08:1}.
Under 24=est,87=ce this is "est-ce"+{la:3, qui:3, que:0}. Era (n=23):
{qui:7, qu:4, que:3, même:2, point:2, la:1}. Les Mis (n=133): {que:67, qu:17,
pas:16 ("n'est-ce pas"), qui:15, la:0}. The cipher's profile — zero que/qu
where Les Mis expects ~63% (binomial P(0/10|p=0.63)≈5e-5), and 3× "est ce la"
where Les Mis has 0 and era has 1 — matches **neither** corpus.

## Rival scorecard (same 5-check battery: A unigram, B follower, C predecessor, D trigram-null, E negative control)

| rival | A | B: P(ce\|V) vs 0.1923 | C: P(V\|que[,qu]) vs 0.1034 | D: 0/10 vs P(que\|V,ce) | E: 24→46=0 | note |
|---|---|---|---|---|---|---|
| est | ✗ (rank 15, 2.6× share) | ✗ 0.0099 (**19.5×**) | ✗ 0.0014 (**74×**) | ✓ null (p=0.247) | ✗ | REFUTED |
| c'est | ✗ (share 0.17% vs 2.82%) | ✗ 0.0388 (5×) | ✗ 0.00349 (30×) | ✓ null | ✗ | grammatical fit ("c'est cela", "c'est ce qui", "que c'est") dies on rates |
| sont | ✗ | ✗ **0** (fatal) | ✗ 0 | – | – | "sont ce" ungrammatical |
| ont | ✗ | ✗ **0** (fatal) | ✗ 0.00279 | – | – | "ont ce" ungrammatical |
| de (closer's add) | ✓ (rank 1, share 4.25%) | ✗ 0.0167 (11.5×) | ✗ 0.0300 (3.4×) | ✓ null (p=0.331) | ✓ | + predecessor kill: era n("la","de")=0 vs cipher 11→24 ×4 |
| en (closer's add) | ✗ (rank 11, 2.2× share) | ✗ 0.0074 (26×) | ✗ 0.0217 (4.8×) | ✓ null | ✓ | elegant readings ("en ce qui", "qu'en", "l'en") all die on rates; n(en,ce,qui)=1 |

"en" and "de" were genuine contenders on grammar (formula-hunter's "[pour|en]
ce qui" for 24-87-64; "de" owns the rank-1 frequency the hypothesis claimed).
Both lose honestly on era rates. "c'est" read the trigrams beautifully
("c'est cela"×3, "c'est ce qui"×3, "que c'est"×3) and still lost 5×/30× —
grammar without rates is not evidence.

## Inversion: nothing fits (the strongest null in this report)

Swept 45 French function words in the era corpus for the two legs that define
24: B* = P(ce|V) ≈ 0.1923, C* = P(V|que,qu) ≈ 0.1034.
- Top B*: **tout 0.1172**, sur 0.0357, mais 0.0218 … est 0.0099 (7th).
- Top C*: **il 0.1045**, les 0.0846, on 0.0798, la 0.067, le 0.0617 …
- **Intersection: empty.** No era word is both followed by "ce" ~19% and
  follows "que" ~10%. "tout" (best B*, within 2×) fails C* ~10× and
  predecessors ("la tout" impossible). 24's profile is unattested in the era
  corpus — under 87=ce provisional. (If 87≠ce, legs B/D/E re-open; legs C and
  the predecessor kill do not depend on 87.)

## Joint contradiction recompute → DISSOLVED

Era P(que|"est ce")=3/23=0.1304 → binomial P(0/10)=**0.247**. The red-team's
Les-Mis-based p=9.1e-04 was a register artifact (Les Mis P(que|est,ce)=0.504,
dialogue-driven). **Meaning for 87=ce:** the 24-87-46 0/10 does not threaten
87=ce under era rates. 87=ce keeps its lane status — PLAUSIBLE/provisional,
3/4 on era re-validation (F6), with the red-team scorecard caveats intact.
The red-team reframing stands as datum: P(46|87,pre=96)=3/3 vs pre=24 0/10 —
"que" after 87 is licensed by predecessor 96, never 24.

## "est cela" anomaly → MOOT

With 24≠est there is no "est cela" to explain. For the record: the cipher's
3/10 "24-87-11" matches neither corpus under an "est ce" reading (era
"est ce la"=1/23, "est ce là"=0/23; Les Mis 0/133 and 1/133). Under the dead
"en" rival it would have read "en cela"×3 — noted and buried with that rival.

## Methodology finding: the register gap is bigger than F10 knew

F10 switched the lane to Tocqueville on a 6.7× cela gap. The "est ce" bigram
family has an **11.9×** Les-Mis/Tocqueville gap (0.1177 vs 0.0099) — and the
cipher's conditional rate (0.1923) sides with Les Mis while its absolute
density (~0.7% of bigrams) exceeds even Les Mis (~0.11%) by ~6×. Per-bigram
consequence: for dialogue-driven bigrams ("est-ce", "qu'est-ce",
"n'est-ce pas") *neither* corpus may match a ministerial despatch, and
Tocqueville's near-absence of them ("est-ce" 7×, "qu'est-ce" 4×, "n'est-ce"
0× in 214,861 words) is itself informative. The H1 refutation is engineered
to survive this: legs 2 and 3 hold under both corpora.

## Relation to round-2 red team

Convergent and stronger. Red team demoted 24=est to "weak open hypothesis" on
the era B-fail (19.4×) and dissolved the joint contradiction (0.247) —
both reproduce here. This close adds: the C-fail is 74× pooled (their 31×
was qu-only; either is fatal), C fails 6.6× under Les Mis too, the
"la"×4 predecessor kill (0 in both corpora), the dual-corpus follower-profile
mismatch, the full rival battery with two honest kills of my own candidates
("de", "en"), and the empty inversion intersection. Net: demotion → refutation.
No disagreement on 87=ce status or on 64=qui (not re-litigated here).

## Caveats

- Legs B, D, E assume provisional 87=ce; legs C and the predecessor kill do
  not (C uses only ground-truth 46=que).
- "c'est" rates via c+est bigram pseudo-counts (includes "c'était" etc.) —
  approximate, but a 5×/30× margin absorbs it.
- Era corpus is third-person essay prose, not a first-person despatch; the
  instrument-independent legs (C structural, predecessors) are the load-bearing
  ones for that reason.
- 24 remains unidentified — this is a refutation, not a solution. The 46-24-85
  ×2 collocation ("qu'est 85"?) and the 11→24 ×4 ("la"→24) are the two
  unexplained cipher-side facts the next hypothesis must explain.
- Elision handling: cipher treatment of que/qu' and la/l'/là as shared vs
  split groups is uncalibrated (red-team caveat inherited).

## Files

- `code/crowd2/closer.py` — deterministic; reuses `crib_attack.load_pairs`
- `code/crowd2/closer_results.json` — all counts, rates, scorecard, inversions, concordances
- `code/crowd2/report_inbox/closer-24-est-resolution.md` — report note
