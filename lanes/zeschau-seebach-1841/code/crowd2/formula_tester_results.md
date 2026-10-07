# Formula Tester — results (Work Order 2, crowd round 2)

Lane: `zeschau-seebach-1841`. Code: `code/crowd2/formula_tester.py`.
Numbers: `code/crowd2/formula_tester_results.json`.
All positions re-derived from `data/upstream-ct_R5005.txt` via `code/crib_attack.py::load_pairs` (1,846 pairs, 96 groups). Nothing invented.

Anchors used: 7 pencil-crib ground truth (11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que)
+ 2 provisional lane-inferred (87=ce, 64=qui). Provisional status marked everywhere.

---

## Test 1 — H5: `77 78 94 82 06` (2× @1179/@1350) = "J'ai l'honneur de"

Alignment under test (5 syllable units → 5 groups, in order):
**77=j'ai, 78=l', 94=hon, 82=neur, 06=de.**

Work-order correction (recorded in JSON): the brief wrote the l'-position as
"(94?)" and the hon–neur boundary as "78→94". Under the stated mapping the
l'-position is **78** (2nd unit) and the hon–neur boundary is **94→82**
(3rd→4th unit). Both 78 and 94 were profiled, so no test was lost.

Repeat positions re-derived: **[1179, 1350]** — matches formula-hunter.

### (a) l'-position (78) as a single-letter consonant

| cell | freq | rank | rate | distinct followers | top-follower share |
|---|---|---|---|---|---|
| 78 (l'?) | 31 | 17 | 1.68% | 21 | 0.129 |
| 82=m (known) | 38 | 10 | 2.06% | — | — |
| 40=e (known) | 21 | — | 1.14% | — | — |
| 34=i (known) | 10 | — | 0.54% | — | — |

Era reference (Tocqueville, heuristic syllabifier, 359,447 syllables):
proclitic **l' = 1.48%** of syllables. Observed 78 at 1.68% → **1.13×, in-band**
(generous 3× band: 0.74%–4.45%). Distribution is proclitic-like: 21 distinct
followers, no dominant follower (top share 0.129), 13 distinct predecessors —
a free function cell, not a fixed-phrase fragment. **Check PASSES** (weak: it
only says "78 could be a proclitic", shared with d'/s'/qu' readings).

Bonus: bigram **77→78 occurs 7×** @[7, 213, 647, 1076, 1179, 1350, 1541] —
5 occurrences outside the repeat. "j'ai l'" behaves as a bound 2-unit chunk
elsewhere. Consistent with the formula reading (weak: n small; any fixed
2-phrase fits).

### (b) hon–neur adjacency: 94→82 vs in-word control 70→82 ("pre-m" @1033)

- **94→82 occurs 4×** @[578, 1181, 1352, 1741]. Two are the in-repeat instances
  (1179+2=1181, 1350+2=1352); **two are independent** (@578, @1741). So the
  hon–neur-style boundary recurs outside the repeat — more than the known
  in-word control **70→82 (pre→m), which occurs exactly 1×** (@1033, inside
  "la première"). Contact-wise, 94→82 patterns as a genuine in-word boundary.
- **But the structural fact kills the reading anyway:** 82 is a ground-truth
  pencil anchor = the single letter **'m'**. H5 requires 82='neur', a 4-letter
  syllable. A syllabary that gives single letters their own cells does not
  reuse the m-cell for "neur". Independent rate argument: 82 at 2.06% (rank 10)
  vs era "neur" at 0.031% → **67× too frequent** for a tier-3 syllable
  ("neur" is below the Meisel tier-2 floor).
- Note for the rival: the 2 extra 94→82 instances (@578, @1741) are exactly what
  the formula-hunter R4 reading predicts — 94=**ne**, 82=**m** inside
  "-nement" words (gou-ver-ne-ment / dé-par-te-ment). R4 is structurally
  compatible with 82=m and inherits this repeat as its target.

### (c) Occurrence contexts @1179/@1350 — "de" + what?

| pos | line | idx-in-line | groups after repeat (06=de …) | anchor-decoded |
|---|---|---|---|---|
| 1179 | a6_10 | 7 | 06 59 42 06 84 59 | all unknown |
| 1350 | a7_05 | 19 | 52 37 64 37 … | ? ? **qui**(64) ? … |

Both occurrences are mid-line, mid-body (63.9% / 73.1% of the text) — no
paragraph-opening position, consistent with a per-paragraph discourse formula
(formula-hunter: repeats are discourse-level set phrases). The "de"+X
grammatical test is **inconclusive**: anchor density near the repeats is too
low (only 34=i before @1350 and 64=qui after @1350 decode). Neither confirms
nor denies de+infinitive/noun. The @1350 follower `… 64=qui …` is at least
compatible with "…de [ce] qui…" phrasing, but that is one unknown group away
from meaning anything.

### (d) Frequency tiers vs Meisel 1826 diplomatic syllable tiers

| group | required value | observed rate | era syllable rate | ratio | Meisel tier | verdict |
|---|---|---|---|---|---|---|
| 77 | j'ai | 2.38% (rank 7) | 0.051% | **47×** | je tier2 + 5–20× despatch boost | FAIL (above boost ceiling) |
| 78 | l' | 1.68% (rank 17) | 1.48% | 1.13× | single letter, tier1 | PASS |
| 94 | hon | 1.95% (rank 12) | 0.011% | **184×** | tier2 (0.08–0.35%) | FAIL |
| 82 | neur | 2.06% (rank 10) | 0.031% | **67×** | tier3 (<0.08%) | FAIL |
| 06 | de | 2.49% (rank 4) | 3.02% | 0.82× | tier0 (>1.5%) | PASS — conflicts with surgeon H3 (06=ne, 3 checks) |

Era rates from Tocqueville t1+t2 via heuristic vowel-group syllabifier
(359,447 syllables; ±10% noise per linguist's own caveat).

### H5 scorecard and verdict

FOR (4): 77→78 bound chunk 7× (5 outside repeat) · mid-body discourse
positions · 06=de tier-consistent · 78=l' tier-consistent with proclitic-like
distribution.

AGAINST (4, two kill-grade): **(1) STRUCTURAL — 82=m ground-truth anchor vs
required 82='neur'**; (2) rate: 82 at rank 10 is 67× too frequent for tier-3
"neur"; (3) rate: 94 at rank 12 is 184× too frequent for "hon"; (4) rate: 77
is 47× the era j'ai rate, above the 20× despatch-boost ceiling.

**VERDICT: H5 "J'ai l'honneur de" is REFUTED as stated — not promoted.**
The mapping requires 82='neur' while 82 is a pencil-crib anchor for the single
letter 'm'; the rate evidence independently buries it. Surviving sub-claims:
the 77→78 "j'ai l'" chunk and 78-as-proclitic stay live; the R4 '-ment' word
family (77=gou, 78=ver, 94=ne, 82=m, 06=ent) is structurally compatible with
82=m and is the live alternative for this repeat.

---

## Test 2 — crib-drag of the 9-mer `56 69 26 00 33 21 64 37 01` (2× @931/@1625)

Method: syllabified Tocqueville t1+t2; all 9-syllable windows with **"qui"**
(=64, provisional anchor) in 7th position, ranked by frequency.
931 = line a5_10 idx 8; 1625 = line a8_03 idx 16. Context @1625 is notable:
`… 46=que | 56 69 26 00 33 21 64=qui 37 01 | 74 87=ce 74 74` — the repeat sits
between "que" and "ce" anchors. Context @931: `… 82=m 98 83 | 9-mer |
07 50 40=e 08`.

Top era candidates (qui in slot 7):

| # | syllables | count | plain reading |
|---|---|---|---|
| 1 | seu le dif fé ren ce qui e xis | 3 | seule différence qui existe |
| 2 | ses ac ci den tel les qui peu vent | 3 | ses accidentels qui peuvent |
| 3 | 'un mou ve ment so cial qui vient de | 2 | un mouvement social qui vient de |

Candidate 1 mapped onto the cipher: 56=seu, 69=le, 26=dif, **00=fé**,
33=ren, **21=ce**, 64=qui, 37=e, 01=xis. Two independent cipher-side checks
kill it:

1. **00='fé' is impossible: 00 is the rank-1 group of the whole text
   (×54, 2.93%); era 'fé' = 0.19% — 15× too rare for the most frequent cell.**
2. 21='ce' collides with provisional anchor 87=ce (soft — homophones are
   possible — but 'ce' is ultra-frequent at 1.20% of syllables, unlikely doubled).

Candidate 2 has no cipher-side support (no anchor or rate leg). Era slot-8
followers of "qui" (se 147, ne 114, a 96, est 83, les 79…) give no purchase on
group 37 without a value hypothesis.

Inner structure: the 4-mer **69 26 00 33 occurs a 3rd time standalone @405**
(context `… 06 11=la 45 88 53 34=i | 69 26 00 33 | 01 02 …`) — a phrase-internal
fixed chunk, still unread, no anchor inside.

**VERDICT: NULL — the 9-mer stays unread.** The best corpus candidate fails
two cipher-side consistency checks; no candidate clears ≥2 independent checks.
Promotion rule not met.

---

## Promotion verdicts

| hypothesis | verdict | basis |
|---|---|---|
| H5 "J'ai l'honneur de" = 77 78 94 82 06 | **REFUTED as stated** | structural anchor contradiction (82=m vs 82=neur) + 67×/184× rate failures; 4 checks for do not survive the contradiction |
| 9-mer drag (56 69 26 00 33 21 64 37 01) | **NULL** | top candidate killed by 00=fé rank-1 impossibility + 21=ce collision; no ≥2-check candidate |
| R4 "-ment" word family (rival for the 5-mer) | not tested here — **referred**: structurally compatible with 82=m; 94→82 ×4 (2 outside repeat) fits 94=ne | needs its own work order |

## Caveats

- Era rates use a heuristic vowel-group syllabifier (±10% noise, per the
  linguist's own caveat); tier comparisons used a generous 3× band and the
  linguist's 5–20× despatch-boost ceiling for je.
- 87=ce and 64=qui are provisional lane-inferred anchors, not pencil cribs;
  everything downstream of them inherits that uncertainty.
- The (c) grammatical test was inconclusive for lack of anchor density, not
  because the grammar fit or failed.
- Line-start mapping replicates `load_pairs` pairing exactly; verified
  @1179→a6_10 and @1350→a7_05.
