# Context Miner — Work Order 3: exploit 64=qui

**Lane:** zeschau-seebach-1841 · **Executor:** context-miner (crowd round 2) · **Date:** 2026-10-07
**Code:** `code/crowd2/context_miner.py` · **Data:** `code/crowd2/context_miner_results.json`
**Status of inputs:** 64="qui" provisional (F9, confirmed 4/4); 87="ce" provisional (revalidated 3/4, attempt 3).
Era reference: Tocqueville t1+t2 (`data/gutenberg-30513/30514-tocqueville-t*.txt`),
221,059 tokens by this script's tokenizer (attempt 3 counted 214,861 — same
texts, tokenizer differs; rates are the comparable quantity, not raw counts).
**Les Mis was NOT used** (F10 register ruling).

## (a) The five 87→64 ("ce qui") contexts, ±6 groups

Positions (0-indexed pair slots): **148, 180, 1766, 1774, 1799**. Anchors shown
as `group=value`; unassigned groups bare.

| # | pos | window (−6 … +7) |
|---|-----|------------------|
| 1 | 148 | 74 67 64=qui 77 84 29=er **87=ce 64=qui** 96 47 46=que 66 84 26 |
| 2 | 180 | 87=ce 86 21 69 14 24 **87=ce 64=qui** 23 37 06 00 33 16 |
| 3 | 1766 | 93 06 77 84 09 24 **87=ce 64=qui** 26 37 78 62 94 24 |
| 4 | 1774 | 26 37 78 62 94 24 **87=ce 64=qui** 59 19 48 74 65 23 |
| 5 | 1799 | 42 94 59 37 91 79 **87=ce 64=qui** 77 84 59 35 94 52 |

**Predecessors of 87** (immediate): 29=er ×1, **24 ×3**, 79 ×1.
Global predecessors of 87: 24×10, 29×3, 96×3, 56/76/43/79/81 ×2.
→ **24→87 is 10 of 32 (31%) of all "ce" predecessors.**

**Immediate followers of 64** in the five: **96, 23, 26, 59, 77 — all distinct.**
Era expectation: "ce qui" is overwhelmingly followed by a verb/reflexive
(era top followers of "ce qui": est×32, se×28, a×11, ne×10, n'×9, fait×6) —
a verb slot *should* show varied followers, so all-distinct is consistent, not
anomalous. Era "qui err*": 0 — the global 29=er→after-64 (×3) never occurs in a
"ce qui" window, consistent with 64="qui".

**Richest window — #1 @148:** `…64=qui 77 84 29=er 87=ce 64=qui 96 47 46=que…`
A qui…ce-qui sandwich, and "ce qui" is followed two groups later by 46=que.
Era check: "ce qui" → "que" within 2–3 words occurs 8/213 = 0.038 in
Tocqueville — rare but attested (e.g. "ce qui fait que"; "fait" is era's #8
follower of "ce qui", ×6). **Tension for H4:** 96="par"/"de" does not parse in
"ce qui 96 47 que" — neither "par" nor "de" fits before "que"; a verb ("fait")
does. Not a kill of H4 (47 is unidentified; 96 may be polyvalent), but the
verb-hunters should own this window.

### The 24 → 87 → 64 formula

- Bigram 24→87: **10×** (of 32 occurrences of 87). Trigram 24→87→64: **3×**
  (occurrences #2, #3, #4 — all three have 24 immediately before "ce").
- freq(24)=52, **rank(24)=1** (0-indexed; the #2 most frequent group of 96).
- Cipher: P(87|24) = 10/52 = **0.192**; P(64 | 24→87) = 3/10 = **0.30**.

Era candidate checks for 24 (≥2 independent checks required to promote):

| candidate | P(ce\|w) era | vs 0.192 | P(qui\|w ce) era | vs 0.30 | era rank | vs 1 | verdict |
|---|---|---|---|---|---|---|---|
| tout | 0.117 | ✓ 1.6× | 0.667 | ✗ 2.2× | 76 | ✗ | 1/3 — not promoted |
| de | 0.017 | ✗ 11.5× | 0.177 | ~1.7× | 0 | ✓ | 1/3 — not promoted |
| est | 0.010 | ✗ 19× | **0.304** | ✓ exact | 14 | ~ | killed on bigram rate |

**Decision: promote the FORMULA (24→87→64 ×3, 24→87 = 31% of ce's
predecessors), withhold any VALUE for 24.** The "est" trigram-rate match
(0.304 vs 0.30, exact) is striking but the bigram rate kills it 19× over;
"tout" clears the bigram check (1.6×) but fails rank and trigram. The
syllable-vs-word ambiguity (24 may be a multi-use syllable, not a word)
means word-level rate comparisons are necessary but not sufficient — stated
as a caveat, not a promotion.

## (b) Joint 87/64 windows (|87−64| ≤ 4)

10 joint events → 10 windows (9 distinct regions; regions @148 counted twice
with shifted frames):

| region | 87@ | 64@ | window |
|---|---|---|---|
| 140–154 | 148 | 144 | 66 14 74 67 64 77 84 29 87 64 96 47 46 |
| 144–154 | 148 | 149 | 64 77 84 29 87 64 96 47 46 66 |
| 176–186 | 180 | 181 | 21 69 14 24 87 64 23 37 06 00 |
| 337–349 | 344 | 341 | 64 31 14 45 64 96 43 87 01 06 70 12 |
| 1020–1032 | 1027 | 1024 | 84 92 64 45 64 96 43 87 01 03 29 80 |
| 1266–1278 | 1273 | 1270 | 88 24 30 20 64 47 76 87 76 48 56 85 |
| 1627–1640 | 1635 | 1631 | 26 00 33 21 64 37 01 74 87 74 74 35 56 |
| 1762–1772 | 1766 | 1767 | 77 84 09 24 87 64 26 37 78 62 |
| 1770–1780 | 1774 | 1775 | 78 62 94 24 87 64 59 19 48 74 |
| 1795–1805 | 1799 | 1800 | 59 37 91 79 87 64 77 84 59 35 |

Groups co-occurring ≥2× (excluding 87/64): 74×5, 84×5, 77×4, 96×4, 24×4,
37×4, 14×3, 29×3, 47×3, 01×3, 59×3, 66/46/21/06/00/45/43/76/48/56/26/35/78/62 ×2.
(Caveat: 74/84 counts are inflated by the double-counted overlapping @148
frames; true region count is 4 and 4.)

**Reverse-order formula:** `64 96 43 87 01` occurs **twice, exact**
(@341–345 and @1024–1028: "…64 96 43 87 01…" both times, each also preceded
by another 64 within 4). Under 87="ce", 64="qui": "qui 96 43 ce 01". The two
87→01 bigrams in the whole text are exactly these two — 01 follows "ce"
*only* inside this formula. Flagged as a formula-grade repeat for the
formula-hunter; no value proposed.

Other reverse joints (64 before 87): @1270 "64 47 76 87", @1631 "64 37 01 74 87".
Shape is consistently **64 X Y (Z) 87** — "qui … ce" with 2–3 intervening
groups, never adjacent.

## (c) 82→16 vs ce/qui windows

11 total 82→16 bigrams (29% of 82's followers; positions in JSON).
Distance measured from the 82 slot to the nearest 87 / 64 slot.

| target | within ±3 | within ±5 | min distances |
|---|---|---|---|
| 87=ce (32 occ) | **0** | **0** | 8, 10, 15, 17, 21, 24, … |
| 64=qui (46 occ) | 2 | 5 | 2, 2, 5, 5, 5, 6, … |

Poisson baselines (11 bigrams × window slots × target density / 1846):
- vs 87, ±5: λ = 2.10 → P(0) = **0.12** (suggestive avoidance, not significant)
- vs 64, ±5: λ = 3.02 → obs 5, P(≥5) = 0.19 (null)
- vs 64, ±3: λ = 1.92 → obs 2, P(≥2) = 0.60 (null)

**Verdict: 82→16 does not cluster near 64=qui (null result, both radii).
It avoids 87=ce windows mildly (0 vs 2.1 expected) — same direction as
attempt 3's 0/11 within ±3, still below significance. Datum: 16 is neither
ce-like nor qui-like.**

The 5 near-64 windows (annotated):
- @1193: 59 46=que 07 24 82=m 16 96 82=m 16 64=qui
- @1196: 24 82=m 16 96 82=m 16 64=qui 29=er 45 58 (overlaps @1193)
- @1435: 76 49 64=qui 52 82=m 16 24 85 01 52
- @1650: 31 10 03 38 82=m 16 01 56 37 11=la
- @1830: 82=m 38 83 24 82=m 16 59 36 69 64=qui

Note @1193/1196: `82 16 96 82 16 64` — "m 16" twice with 96 between, then
"qui". The only doubled 82→16 in the text, and it sits next to 64.

**16's own profile:** freq 28; predecessors 82×11, 62×4, 12×3, 33×2, 42×2;
followers 00×4, 24/01/91/76 ×2. Hypothesis 16="a" (elided m'a): era
followers of m' — a×18, de×10, exprimer×9… ("a" leads but only 14% of 125;
tokenizer splits "m'exprimer" etc., and the corpus has OCR noise like
"story"/"duponceau"). **One weak check only — 16="a" is NOT promoted**
(requires ≥2). 16 remains unidentified; what is established is what it is
not: not ce-like, not qui-like.

## Nulls and non-promotions (first-class)

1. No "ce qui est" verb identified: the five followers of 64 in ce-qui
   windows are all distinct — consistent with a verb slot, yields no value.
2. 24="tout"/"de"/"est": each clears at most one of three checks — no value
   promoted, formula only.
3. 16="a": one weak era check — not promoted.
4. 82→16 shows no qui-clustering — the hypothesized "verb near qui" angle
   for 16 is closed; the avoidance-of-ce angle stays open but sub-significant.
5. H4 tension noted ("ce qui 96 47 que" vs 96="par"/"de") but not a kill.

## Files

- `code/crowd2/context_miner.py` — this analysis (deterministic; run with
  `python3 code/crowd2/context_miner.py` from the lane dir)
- `code/crowd2/context_miner_results.json` — all counts, windows, era tables
- `code/crowd2/report_inbox/context-miner-qui-windows.md` — report-inbox note
