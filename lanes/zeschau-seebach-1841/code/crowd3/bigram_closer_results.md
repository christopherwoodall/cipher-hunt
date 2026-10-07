# Bigram Closer — anchor factory results (round 3, crowd3)

**Worker:** bigram_closer · **Date:** 2026-10-07 · **Corpus:** 1,846 pairs / 96 groups; era = Tocqueville t1+t2 (214,861 words, 370,748 syllables, maximal-onset orthographic syllabifier reproducing the morphologist's spec)

**Battery:** (1) frequency/rank band [context only — UNCALIBRATED], (2) conditional bigram rates vs era, (2b) follower-concentration structure, (3a) grammatical attestation kills, (3b) hand grammatical coherence, (4) rival negative controls. Promotion needs ≥2 independent checks.

## Calibration (read first)

Era-vs-cipher anchor check exposed a **syllabification mismatch**: 29=er is 182x and 82=m is 60x over era — the cipher's syllabification is morphological (keeps `-er`), the era model's is maximal-onset. **29/82/34 are excluded from all rate/attestation legs.** Usable GT anchors for rate legs: 11=la (1.15x), 46=que (1.08x), 40=e (0.71x), 70=pre (1.88x). Provisional flags: 64=qui 3.84x (suspect), 96=par 1.81x, 87=ce 1.40x.

## PROMOTED (candidate, pending red-team)

### 78 = "me" ✅ candidate
| check | result |
|---|---|
| L1 rate | 0.01679 / 0.01515 = **1.108** in band |
| L2 | 11=la→78 x2: 0.0455 vs era P(me\|la)=0.0274 → **1.66x** in band |
| L2b concentration | cipher top3 0.29 vs era 0.397 → **0.73x** in band |
| L3a attestation | clean, no kills |
| L3b grammatical | "la me" = **"la même" / "la mesure"** (era n=154) |
| rival "e" | **KILLED** — 78→40=e x3 but era ("e","e") unattested (n=0) |
| rival "l" (l') | **KILLED** — 11→78 x2: 40.4x over era P(l\|la); "la l'" ungrammatical |

Joint note: 47→78 x5 and 37→78 x4 read as "me me" = "même" — consistent with polyvalent "me" (47/37 also me-band), not conflicting.

## LEADS (check counts, not promotions)

- **77 = "que"** — LEAD (3 checks): L1 1.645; L2prov 87=ce→77 x2 r=1.54 ("ce que" ✓); L2b 1.78. Caveats: polyvalence with GT 46=que; contact cosine(77,46)=0.198 argues against.
- **77 = "le"** (own best) — LEAD-weak (1 check): L1 0.982; L2prov fails (ce→77 r=8.9 "ce le" bad; qui→77 r=15.4).
- **77 = "pas"** (incumbent) — **REFUTED**: L1 6.69x out of band; L2prov fails (16.5x, 43.1x).
- **67 = "re"** — LEAD (1 independent leg; stem-hunter overlap noted): L1 1.017; 67→46=que x2 r=1.95; rival "les" killed by 67→11=la (35.5x). Joint: 67→77 x6 = "re que" = "[verb] que" ("dire que") under joint 77="que"-lead.
- **74 = "te"** — LEAD (2): L1 0.964; self-loop 74→74 x6 = "tête".
- **21 = "me"** — LEAD (3): L1 1.073; 11→21 r=1.66; L2b 1.43. **Caveat:** 96=par→21 x3 → 802x ("par me" bad) — provisional-on-provisional, flagged for red team.
- **59 = "se"** — LEAD (~3, provisional-flavored): L1 1.147; 64=qui→59 r=1.98; 94=ne→59 r=1.48 ("ne se" ✓). L2b 3.29 out.
- **52 = "se"** — LEAD (~2, provisional-flavored): L1 1.191; 64=qui→52 r=1.32.
- **48 = "les"** — LEAD-weak (2 weak): L1 1.026; L2b 1.33; followers maximally flat.
- **92 / 76 = "se"**, **79 = "au"** — LEAD-weak (1.5 checks each, via provisional 94=ne→X "ne se"/"ne au" frames).
- **86** — class LEAD = verb stem (86→29=er x4, V29); reading unidentified ("te"+"er" impossible).

## REFUTED readings (rival-kill table)

| group | reading | killed by |
|---|---|---|
| 77 | pas (incumbent) | L1 6.69x; L2prov 16.5x/43.1x |
| 41 | der / ni (lane INCONCLUSIVE n=1) | L1 13.58x / 5.07x as general readings (f=19) |
| 24 | c'est (new) | L1 28.9x (era P(c-est unit)=0.00097) |
| 78 | e | L3a: 78→40 x3, era ("e","e")=0 |
| 78 | l (l') | 11→78 r=40.4x; "la l'" ungrammatical |
| 47 | l | L3a: ("l","la") and ("l","que") unattested vs 47→11/46 x3 |
| 65 | des / se | L3a: 40=e→65 x3, era ("e","des")/("e","se") unattested |
| 12 | se / en | L3a: 70=pre→12 x3, era ("pre","se")/("pre","en") unattested |
| 00 | de / a / le | 00→46=que 40.8x / 11→00 128x / all L2 out |
| 24 | est / en / de / tout | standing red-team kills (not re-run) |

## INCONCLUSIVE (all others tested)

00, 01, 03, 08, 09, 12, 16 (1 check: "me" L1=1.001 perfect, no anchor legs — "m'a"/"M." frames noted), 17, 23, 24, 26, 30, 33, 37 ("me" LEAD-weak), 42, 45, 47, 50, 51, 56, 60, 62 ("te" killed by 62→94=ne x8 r=32.4), 65, 66, 76, 79, 84, 86 (reading), 88, 91, 92, 98 ("les" L1 only).

## Single legs (scope-limited by task)

- **06 (verb-stem, stem hunter's lane):** ONE leg — 06→11=la x4 (0.087) = imperative+object ("donnez-la"); era-attested ("faites-la"→("tes","la")=15). Corroborates verb-stem alongside V29; no conflict with 06="ent"-restricted (polyvalence). Overlap noted, not duplicated.
- **94="ne" (morphologist's battery under review, not re-run):** ONE new leg — ne+pronoun frame: 94→52 x3 + 94→59 x2 = "ne se" (5/36) vs era P(se|ne)=0.0255; 94→11=la x0 consistent with era P(la|ne)=0.0079 (exp. 0.28). Supporting only. (A 94→82 "ne m'" leg was voided: 82 calibration-excluded.)

## Best next step

1. Red-team the **78="me"** promotion (rival kills are the load-bearing evidence).
2. Adjudicate the **77** three-way: "que"-lead (polyvalence cost) vs "le"-weak vs new data; the 67→77 "re que" joint frame is the sharpest new evidence.
3. The **"ne se" cluster** (94→52/59 + 59/52="se" leads) is mutually reinforcing — test jointly.
4. 00 and 24 remain the top-frequency unknowns; 24's P(87|24)=0.192 still unexplained under 87="ce".

Raw numbers: `code/crowd3/bigram_closer_results.json` · battery code: `code/crowd3/battery.py`
