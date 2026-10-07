# 62="on" — instrument-independent third leg (round 5, frenchman)

Work order: find a NON-ear third leg for 62="on" (STRONG LEAD, N28).
Legs 1 (ear lock) & 3 (ear subject triangulation) share the ear instrument;
red team denied promotion pending an instrument-independent leg.
All checks below run on the REPAIRED 1,847-pair parse
(`code/side-keyhunt/repaired_offsets.json`) with era legs in WORD SPACE only
(F30). No ear readings used. Code: `code/crowd5/frenchman62_leg3.py`;
numbers: `code/crowd5/frenchman62_leg3_results.json`.

## Re-derived baselines (repaired parse)
- f(62)=35/1847 = 1.8950%; 21 distinct predecessors, 13 distinct followers
  (free-function-word signature; cf. 87=ce 14/32).
- 62→94 ×9 = 0.2571. Era P(ne|on)=0.1584 (ne + n'-forms) → **1.62× in-band**
  (N28's 2.18× used ne-only 0.1179; both in band). 9th instance @761
  (`er e 20 62 94 59 39`) — the repaired a5_03 region.
- 46→62 = **0/29** (re-verified). 11→62 = 0, 96=[par]→62 = 0.
- 62→21 ×1 (@849: `33 96 40 62 21 67 91` — the N28 window, re-indexed +4).

## Check A — era word-space unigram subject battery (rival kill)
f(62) rate vs era unigram of every subject-position word (Tocqueville, 221,027 words):

| word | era P | cipher/era |
|---|---|---|
| on | 0.7311% | 2.59× |
| il | 1.2646% | 1.50× |
| qui | 1.0677% | 1.77× |
| ils | 0.4900% | 3.87× |
| je | 0.3027% | 6.26× |
| elle | 0.3547% | 5.34× |
| nous/vous/elles | … | 11–27× |
| cela/ceci | … | 57–89× |
| tu | 0.0005% | 4188× |

Grammatical (word-space) kills: **son/mon/nom/ont cannot be subjects**
(determiners/noun/verb) — the ear's /ɔ̃/ rival-kill re-derived without the ear;
ça register-killed (linguist 47:1). Rate-kills: cela, ceci, tu, nous, vous,
elles (≥11×). Survivors: **{on, il, qui}**. "qui" is blocked by provisional
64="qui" (would need polyvalence). "il" is the live rival.

## Check E — "on" vs "il" differential (the survivor)
- "on ne" rate cannot discriminate: obs 0.2571 vs era P(ne|on)=0.1584 (1.62×)
  vs era P(ne|il)=0.1896 (1.36×) — both in band.
- The 46→62 null DOES discriminate: under 62="il", "qu'il" is written
  que+il (no by-ear merger), era P(il|que) predicts E=3.03 over 29 trials;
  observed 0 → **binomial p=0.041**, a weak kill of "il". Under 62="on" the
  same null is the by-ear model's successful prediction (qu'on=/kɔ̃/ → one
  group; written-era E=2.31, p=0.090 — suggestive, not significant alone).
- Net of A+E: 62 is a subject-position word; every rival is killed, weakened,
  or blocked except "on".

## Check B — "qu'on"-null as corroboration
46→62 = 0/29 vs written-era E=2.31, binomial p=0.090. Not significant alone;
it is the QUANTIFIED form of N28's novel prediction (the ear model predicted
the absence before the count was checked). Corroboration-grade.

## Check C — mappable-cell follower/predecessor profile
Anchor-mappable cells vs era P(w|on), n=35:

| cell | obs | exp | era P | note |
|---|---|---|---|---|
| 94=[ne] prov-strong | 9 | 5.54 | 0.1584 | 1.62×, correct sign |
| 21=[me] LEAD | 1 | 0.17 | 0.0050 | correct sign, n=1 |
| 11=la GT | 0 | 0.41 | 0.0118 | correct sign |
| 46=que GT | 1 | 0.17 | 0.0050 | "on que" grammatical, n=1 |
| other | 24 | 28.70 | 0.8199 | — |

χ²=11.24, df=4, **p=0.024**. Negative grammatical cells: 11→62=0 and
96→62=0, both era-word-space 0 — consistent. (F30-legal: all era legs are
word-space; 40="e" fragment excluded.)

## Check D — 62→21 "on me" rate (corroboration; shares data with leg 3)
P(21|62)=0.0286 vs era P(me|on)=0.0050 → 5.77×, n=1. Correct sign, tiny n;
different instrument (rate) from leg 3's ear reading, but same window —
corroboration only, not counted as independent.

## Adverse datum (not buried)
"on" unigram is **2.59× over era** (1.895% vs 0.7311%). Genre-defensible but
untested: this lane has documented genre swings of 6.7× (cela, F10) and
11.9× ("est ce", N10) on function words between Tocqueville and other
registers; a diplomatic reporter's impersonal "on" plausibly exceeds
Tocqueville's. Granularity caveat: cipher groups ≠ words (segmenter: ~958
words provisional) — the 2.59× uses group denominator; the word-denominator
version is worse, so the genre explanation carries the weight. Flagged for
the red team, not hidden.

## Verdict
**STRONG LEAD (status unchanged) — promotion case assembled, red-team decision.**
The red team asked for an instrument-independent third leg; two are delivered:
(1) the A+E subject-battery rival kill (non-ear: word-space grammar + era
unigram rates + the "il"-differential on the 46→62 null), and (2) the Check C
mappable-cell follower profile (χ² p=0.024, all cells correct sign, non-ear).
Checks B and D corroborate. Per lane rule the promotion itself is the red
team's call — the adverse unigram datum above is part of the case file.
