# 48 syllable-cell battery — report (syllabicist48, round-10 WO3)

## Context
Work order 3: 48 is UNIDENTIFIED (n48=38; H_verb killed F64/K2; 48="ne"
killed F60). Round-10 lead: 48 as a frequent SYLLABLE cell. Pre-registered
bar in `code/crowd10/syllabicist48/PREREG.md` (v1.1, 2026-10-07T20:38:55Z;
v1.2 instrument repair 20:44Z — see Why). H_stem tested SEPARATELY per the
work order's option (contact-profile claim, cleaner instrument, no
double-counting with the syllable legs). Code:
`code/crowd10/syllabicist48/battery48_syllable.py`; results JSON alongside.
Era: Nesselrode v8 (86,636 tokens), repaired 1,847-pair parse.

## Decision
**48 stays UNIDENTIFIED.** No candidate clears the pre-registered LEAD bar
(≥2 of S1–S4 PASS, zero kills). Recommendation package for red team:
- **S-word class: KILLED.** All 31 word candidates (top-3 corpus unigrams
  et/il/les + 28 seeded incl. 7 nouns) die on ≥1 grammatical-zero leg.
  The kill is structural, not candidate-dependent (see Why), and survives
  the loss of 62="on".
- **S-syl class: 10 LEAD-weaks, mutually exclusive — no identification.**
  Each passes S1 (rate) only; S2–S4 are neutral by pre-registered design.
  Ten rate-compatible syllables ≠ an identity.
- **H_stem: NULL** (separate battery S6: cosine 0.387 < 0.60 bar; Fisher
  p=0.455; signature 0.158 < 0.40 bar). Explicitly not adverse per prereg
  (n96=21 underpowered) — with one calibration caveat below for red team.

## Ranked syllable candidates (for / against)
Rate P48 = 38/1847 = 0.02057. All S-syl verdicts LEAD-weak (S1 PASS only).

| rank | S | era syll rate | ratio P48/era | for | against |
|---|---|---|---|---|---|
| 1 | de | 0.0312 | 0.66 | closest rate; on-init words ×2 ("demande"-class), end-de+le ×4 | word-reading KILLED ("la de"=0); @1525 "la de|…" needs 96 non-word-initial (tension w/ 96="par" prov) |
| 2 | à | 0.0160 | 1.28 | rate in-band | word-reading KILLED ("la à"=0, "on à"=0); as syllable /a/ nearly vowel-only — weak cell shape |
| 3 | et | 0.0143 | 1.44 | rate in-band | word-reading KILLED ("la et"=0); syllable /e/ collides with GT 40="e" (needs conditioning) |
| 4 | a | 0.0123 | 1.68 | rate in-band; on-init ×38, end-a+le ×14 | inventory "a" is the word "a" (verb) — word-reading dies ("la a"=0, "que a"=0) |
| 5 | es | 0.0119 | 1.72 | rate in-band | diffuse fragment (-es endings); no corroboration |
| 6 | il | 0.0103 | 1.99 | rate in-band (band edge) | word-reading KILLED ("la il"=0) |
| 7 | les | 0.0103 | 2.00 | rate in-band (band edge) | word-reading KILLED ("la les"=0) |
| 8 | te | 0.0102 | 2.02 | rate in-band (band edge); end-te+le ×8 | — |
| 9 | un | 0.0099 | 2.07 | rate in-band (band edge) | nasal vowel cell; by-ear premise allows, no corroboration |
| 10 | com | 0.0087 | 2.37 | rate in-band; la-init ×56 ("la com…"-words) | — |

Against the class as a whole: the ten are mutually exclusive; S1 is the
only discriminating leg and it cannot separate them; no candidate has a
second independent leg. "de" is the rate-closest but carries the @1525
tension noted above.

## H_stem verdict (S6, separate instrument)
- (a) predecessor cosine(48,96) = **0.387** vs 0.60 bar → FAIL (floor median
  vs n≥20 groups = 0.119 — above floor, below bar; re-derives F64's number).
- (b) Fisher on shared top-follower cells: shared {21} only; table
  [[1,8],[5,82]]; p=0.455 → FAIL.
- (c) stem-signature (top-3 followers ≥40%): 48 = **0.158** → FAIL.
- **Calibration catch (for red team): the 0.40 bar is miscalibrated — the
  lane's own reference stem 06 scores 0.318** (top-3: 77×6, 0×4, 11×4;
  n=44), failing the bar it was meant to operationalize. 96 passes (0.429,
  n=21, noisy). So (c)'s FAIL is uninformative about stem-likeness, which
  supports the prereg's "failure never adverse" stance. Verdict: **NULL**.
  Unregistered observation (no kill claimed): 48's follower profile is
  strikingly flat (29 distinct/38, top cells all ×2) vs 96's concentrated
  one — shape-mildly-against, offered for adjudication.

## Why (leg detail)
- **S1 rate** (context): word candidates et/il/les/de/à PASS (0.42–1.74×);
  se/des/dans/plus NULL (3–4×); all nouns + most function words KILL
  (5–73×). Syllable candidates: the 10 above PASS (0.66–2.37×).
- **S2 "la 48" @1525 (GT, fresh question):** every function-word candidate
  scores n("la",S)=0 in 86,636 tokens — genuine grammatical zeros in French
  ("la de", "la et", "la il", "la les", "la à", "la se", "la des", "la dans",
  "la sur", "la sans", "la mais/car/donc/ni", "la y", "la leur", "la son",
  "la tout", "la encore/aussi", "la point"). KILL for 25/31. Nouns pass S2
  ("la lettre"×24, "la dépêche"×19, "la cour"×30) but die on S1-rate.
- **S3 "on 48" ×6 + "que 48"=0:** "on de"×2 / "on aussi"×1 are inversion
  artifacts ("dit-on de") — do not flip verdicts (those candidates die on
  S2 anyway). Genuine zeros kill the rest ("on sur", "on dans", "on plus",
  "on tout", "on bien", "on lettre/dépêche/…"). Every S2-killed candidate
  also fails S3 or S1 — no verdict rests on a single leg.
- **S4 "48 pas" ×2:** kills se ("se pas"=0), les ("les pas"=0),
  de ("de pas"=0); corroborates nothing (F64: the datum is null alone).
- **Structural pincer:** "la" (GT) takes nominals, "on" (fenced STRONG LEAD)
  takes verbs — no single French word at the required rate follows both.
  Noun/verb homographs ("porte", "garde") exist but none approaches 2.06%
  word-rate. The S-word kill survives even if 62="on" falls (S2+S1 suffice).
- **v1.0→v1.2 instrument repair:** the first by-ear rule split VV nuclei
  ("puis"→"pu|is"), and fragments ("qu","is","it","ur","us") dominated the
  shortlist. Repaired: VV = single nucleus (lane's own "qu'on"=/kɔ̃/
  premise). S-word battery unaffected (word-space legs). Both runs archived
  in the results JSON's selection record.
- **S5 diagnostic (T7, not scored):** 48→suffix{29,40}=3/38 (7.9%),
  48→word-boundary{11,77,46}=3/38 (7.9%) — flat, consistent with a frequent
  syllable's diverse contacts, consistent with nothing in particular.

## Enlightenment
The battery is a one-way instrument: it kills the word class cleanly but
cannot identify among syllables — S2–S4 are neutral for S-syl by the nature
of the claim (a syllable makes almost no grammatical predictions at frame
level). A second syllable-discriminating instrument is needed, e.g.:
successor-word anchoring (which identified successors license which
S-initial words at the six "on 48" windows), or the 82="m"×4 predecessor
frames ("m'"-elision licenses vowel-initial S). The ten LEAD-weaks are the
honest output of this round, not an identification. Nothing here disturbs
any banked value; the 48–96 contact datums were consumed by S6 only.
