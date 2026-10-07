# Hypothesis Sweeper — results (Work Order 5)

**Script:** `code/crowd2/hypothesis_sweeper.py` → `code/crowd2/hypothesis_sweeper_results.json`
**Reference:** era corpus only — Tocqueville 1835/1840, Tomes 1+2 (214,861 words).
Elision-aware: era "ne" = `ne`+`n'` (tokenizer splits `n'`→`n`); era "que" = `que`+`qu'`.
Small-n controls use a count rule (obs ≤ exp + 2√(exp+0.25) + 1), not a factor band.
Frequency checks are calibrated by an empirical syllable-vs-word inflation factor
from word-like anchors: la 0.77, que 1.18, ce 3.28, qui 2.27 → **median 1.72**
(pencil-only la/que: 0.97). A grammatical contradiction / lexical impossibility
is a hard fail → REFUTED outright (attempt-2 rule). Promotion bar: ≥2 checks, zero fails.

## (a) H2: 77 = "pas" — INCONCLUSIVE (4 pass / 3 fail / 3 info)

| # | check | cipher | era | result |
|---|-------|--------|-----|--------|
| 1 | freq (inflation-calibrated) | P(77)=0.0238 | 1.72×P("pas")=0.0079 | PASS (3.0×, 4x band) |
| 2 | ratio 06/77 | 46/44=1.045 | n(ne/n')/n(pas)=3156/984=3.207 | FAIL (3.07×) |
| 3 | bigram FWD P(77\|06) | 6/46=0.1304 | P(pas\|ne/n')=0.0063 | FAIL (**20.6×**) |
| 4 | bigram BWD P(06\|77) | 6/44=0.1364 | P(ne/n'\|pas)=0.0203 | FAIL (6.7×; same adjacency, other direction) |
| 5 | follower-anchor P(11=la\|77) | 1/44=0.023 | P(la\|pas)=0.0244 | PASS (1.06×) |
| 6 | joint "que→pas" | 46→77=1/29 | P(pas\|que)=0.00000 | PASS (count rule: exp 0.00, thr 2.0) |
| 7 | joint "que→ne" | 46→06=0/29 | P(ne/n'\|que)=0.00559 | PASS (exp 0.16, thr 2.4) |
| – | ce-leg of follower probe | 87→77? no: P(87=ce\|77)=1/44 | P(ce\|pas)=0.0020 | info only (n=1, count-consistent) |
| – | caveat | 67→77=6/37=16.2%, 67 unidentified | – | info |
| – | caveat | 77 heads r1 repeat 77-78-94-82(m)-06 ×2 | – | info (linguist H5 unscored) |

**Reading:** the 20.6× bigram miss is the diagnostic. Under 06="ne", 06→77 should be
≈ infinitival "ne pas" adjacency (≈0.6% era); 13% observed is irreconcilable with
"ne" — but it does NOT kill 77="pas" itself. Era top predecessors of "pas" are
verbs (est 163, a 102, sont 43, ont 41 …; "ne" only 20/984 = 2%), and the cipher's
top predecessors of 77 are 06 (6) and 67 (6) — a verb-stem profile, not a "ne" profile.
The la-follower leg passes almost exactly (0.023 vs 0.0244). Net: **"pas" stays the
best reading for 77, but its partner 06 is probably not "ne"** (see H3).

### Rivals for 77
- **77="que": INCONCLUSIVE (2/1).** Freq passes almost exactly (0.0238 vs 0.0230,
  1.03×). FAIL: 06→77=6/46 as "ne→que" vs era P(que|ne/n')=0.00000 (exp 0.00, thr 2.0) —
  restrictive "ne…que" is non-adjacent in prose. que→que control passes (1/29, count rule).
  The contradiction is conditional on 06="ne"; if 06 is revalued, this rival reopens.
- **77="plus": REFUTED (1/1).** Freq passes; 06→77 as "ne→plus": 6 vs exp 0.03 (thr 2.1),
  era P(plus|ne)=0.0006.
- **77="ne" (swap with 06): REFUTED (hard).** 06→77=6/44 as "pas→ne" vs era ~0 —
  ungrammatical.

## (b) H3: 06 = "ne" — INCONCLUSIVE (6 pass / 2 fail)

| # | check | cipher | era | result |
|---|-------|--------|-----|--------|
| 1 | freq (inflation-calibrated) | P(06)=0.0249 | 1.72×P("ne")=0.0144 | PASS (1.73×) |
| 2 | ratio 06/77 | 1.045 | 3.207 | FAIL (shared with H2, not independent) |
| 3 | dominance profile | top follower 77 at 13.0% | top follower of "ne" ("est"/n'est) at 10.3% | PASS (4x band) |
| 4 | predecessor diversity | 30 distinct | "ne" takes subjects/clause-initials freely | PASS |
| 5 | "ne→ce" | 06→87=0/46 | P(ce\|ne)=0.0000 | PASS (count rule) |
| 6 | "ne→que" | 06→46=0/46 | P(que\|qu'\|ne)=0.00000 | PASS (count rule) |
| 7 | **anomaly "ne→er"** | 06→29(er)=5/46=0.109 | P(word-initial "er"\|ne)=0.0000 | FAIL (exp 0.00, thr 2.0) |
| 8 | negative "que→ne" | 46→06=0/29 | P(ne/n'\|que)=0.00559 | PASS (exp 0.16) |

**Reading:** "ne" survives on frequency, profile, and all zero-controls, but carries
two unexplained bigram anomalies: 06→77 at 13% (should be ≈0.6% infinitival "ne pas")
and 06→29(er) at 10.9% (era: zero "ne"+er-initial words in 215k). Both are explained
at once by an unscored rival (see below). Not promoted.

### Rivals for 06
- **06="de": REFUTED (hard; 2/1).** Freq passes (0.0249 vs 0.0733, 2.9×); **de→pas:
  6/46 vs era 0.00000 — ungrammatical (hard fail)**; de→ce passes (0/46, exp 0.77).
- **06="le": REFUTED (hard; 1/1).** Freq passes (0.0249 vs 0.0367); **le→pas:
  6/46 vs era 0.00000 — ungrammatical (hard fail).**

### New lead (unscored, for next worker): 06 = verb stem
06's follower set reads as a verb-stem profile, not a particle profile:
06→77(pas)=6 ("X pas", finite negation — era est→pas 16.6%, a→pas 10.4%),
06→29(er)=5 (infinitive "X-er"), 06→11(la)=4 ("X-la", verb+object), 30 distinct
predecessors (subjects). This single rival explains both "ne" anomalies (the 13%
pas-adjacency and the 5× er-adjacency) that the "ne" reading cannot. Test: identify
06 via the 06→29 infinitive frame and 06→11 object frame against era verb-stem rates.

## (c) H4a: 96 = "par" — CONFIRMED (4 pass / 0 fail) ✅

| # | check | cipher | era | result |
|---|-------|--------|-----|--------|
| 1 | freq (inflation-calibrated) | P(96)=0.0114 | 1.72×P("par")=0.0083 | PASS (1.37×) |
| 2 | "parce" compound P(87=ce\|96) | 3/21=0.1429 | n(parce)/n(par)=132/1036=0.1274 | PASS (1.12×) |
| 3 | "parce que" frame P(46=que\|96,87) | 3/3=1.00 | P(que\|qu'\|parce)=1.0000 | PASS (n=3, weak) |
| 4 | function-word diversity | 15 preds / 12 followers | – | PASS |

**Reading:** the only promotion of this sweep. Check 3's era rate is 1.0000 only after
the qu-correction (v1's 0.3258 missed "parce qu'"; all 132 era "parce" tokens are
followed by que/qu'). Dependency: the compound/frame legs assume 87=ce (provisional);
if 87 falls, this falls with it. 96="par" joins as a **lane-inferred provisional
value** (not a pencil crib): 10 anchors/values total.

### H4b: 96 = "de" — REFUTED (1 pass / 3 fail)
- FAIL freq: 0.0114 vs 1.72×P("de")=0.0733 (**6.4×** — "de" would be rank ~1; 96 is rank 36)
- FAIL "de ce": P(87\|96)=0.1429 vs era P(ce\|de)=0.0167 (8.6×)
- FAIL "de ce que" frame: 1.00 vs era 0.1961 (n=153; 5.1×)
- PASS diversity (non-discriminating)

### Rivals for 96
- **96="pour": REFUTED (1/1).** Freq passes (0.0114 vs 0.0085); pour→ce: 0.1429 vs
  era 0.00567 — "pour ce" rare in formal prose.
- **96="a/à": REFUTED (hard; 0/1).** a→ce: 0.1429 vs era 0.01645 ~0 — "a ce" ungrammatical.

## (d) H4c: 41 = "der", 08 = "ni" — INCONCLUSIVE (2 pass / 1 fail / 1 info)

| # | check | cipher | era | result |
|---|-------|--------|-----|--------|
| 1 | positional frame | 41-08 @59, full 41-08-34-29-40 @59–63 ("-ière" tail anchored: 34=i,29=er,40=e) | – | PASS (byte-verified) |
| 2 | rate band | 41-08 pair rate 1/1845=5.42e-4 | "der*"-initial word rate 109/214861=5.07e-4 | PASS (**1.07×**) |
| 3 | continuation P(08\|41) | 1/19=0.053 | P("derni"\|"der*")=0.9083 | FAIL (vocabulary-sensitive: Tocqueville der*≈dernier*; a despatch may use derrière/déranger) |
| – | 08-follower probe | 34 (=i) ×1 among 08's followers | – | info only — 08="ni" is a common syllable (19×: venir/tenir/fini…), 34 need not dominate |

**Reading:** the rate coincidence (1.07×) and the anchored "-ière" frame are
suggestive but n=1; the continuation miss is real but vocabulary-sensitive. Not
promotable. Letter-accounting wrinkle: 41-08-34-29-40 spells "der-ni-i-er-e"
("derniiere", 9 letters vs "dernière" 8) — the cipher's "ière"=i+er+e spelling
matches "première" (11-70-82-**34-29-40**) exactly, so the frame is orthographically
consistent with the crib's own convention; still, "per/ber/ver"+"ni" families are
unscored rival onsets.

### Rivals for 41/08
- **41="ter"/08="ni": REFUTED (hard).** Frame would read "terniere" — not a French word.
- **41="mer"/08="ni": REFUTED (hard).** Frame would read "merniere" — not a French word.

## Nulls
- N-SW1: no hypothesis promoted below the ≥2-check bar except 96="par" (4/4).
- N-SW2: no rival reading outscores its primary except the unscored 06 verb-stem lead
  (flagged, not scored — needs its own ≥2-check work order).
- N-SW3: 77="que" survives at INCONCLUSIVE (2/1) — its one fail is conditional on
  06="ne"; if 06 is revalued, reopen.

## Method notes for the record
- v1 of this script compared rank ordinals across a 96-type vs 20k-type vocabulary
  and failed zero-count observations mechanically; v2 fixed both (inflation-calibrated
  freq checks; count-rule small-n controls) and added elision handling (n', qu').
  The elision fix flipped one check materially: era P(que|qu'|parce) 0.3258 → 1.0000.
- Era "ne" including n' moved the ne/pas ratio 1.822 → 3.207; the surgeon's LesMis
  ratio (0.959) is now a 3.3× register gap, same class as the F10 cela gap.
