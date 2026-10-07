# SCORER SMITH — syllable-level cell scorer (work order 4)

**Verdict: BROKEN-ON-CONTROL**

Anchors: 11=la 70=pre 82=m 34=i 29=er 40=e 46=que 87=ce* 64=qui* (*provisional, lane-inferred).
Corpus: Tocqueville t1+t2 (1835/1840), 215246 tokens, 2201 syllable units (rule-based segmenter, documented in scorer_smith.py).
Calibration: corpus P("er"-unit)=0.0020 vs cipher P("er"-cell)=0.0255; corpus P(unit ends in letters "er")=0.0211.

## Synthetic control (gate)
- Design: tail-1200w Tocqueville-t2, rule+encipher_split cells, 96-cell inventory (9 anchors pinned), random mapping seed=1841
- Stream: 1815 pairs, 93 groups, anchor coverage 0.288; elision rate 0.322 (814/1200 words kept); kappa=0.911
- Candidates: 198, test words: 47, median placements/word: 84.0
- Recovery: top-1 accuracy 0.021 vs chance 0.076 (x0.3); MRR 0.133
- Bar: top1 >= 3x chance AND mrr >= 0.30 AND n_test >= 10 → **BROKEN-ON-CONTROL**
- Model check (true vs shuffled 50-cell runs): -3.123 vs -3.915 — model prefers true French runs; failure is in placement ranking, not the language model

## Real drag: NOT RUN (control failed — work order 4d)

Control FAILED: the scorer does not recover planted assignments above the pre-registered bar. Real drag NOT run (work order 4d). Do not use this scorer on the cipher.
