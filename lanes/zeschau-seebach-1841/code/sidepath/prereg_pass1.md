# PREREGISTRATION — slider pass 1 (FROZEN 2026-10-07 ~09:20 CDT)
Role: SLIDER, Seebach side-path fleet. This document is load-bearing: no threshold,
weight, window, or candidate list may change after this timestamp without a new
versioned file and invalidation of pass 1. Verification: sha256 of this file is
recorded before any slide runs; mismatch at slide time → pass VOID.

## Target recap (do not re-derive)
R5005, French two-digit syllabary, Zeschau→Seebach 18 Jan 1841. Transcription:
`data/upstream-ct_R5005.digits.txt`. **File-measured: 3,764 digits / 1,882 pairs
(0-based pair indices below; STATE.md says 1,846 — discrepancy flagged, file order
rules).** Era corpus: `data/gutenberg-30513-tocqueville-t1.txt` +
`data/gutenberg-30514-tocqueville-t2.txt` (1835/1840, 214,861 words).

## Pinned anchors (candidate may not contradict — contradiction = automatic FAIL)
Ground truth crib: 11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que.
Lane-inferred provisional: 87=ce, 64=qui, 96=par. Provisional-strong: 94=ne
(treated pinned for pass 1). `94="re"` and `64="même"` are live rivals — a
candidate that *requires* one of them fires rule RIVAL-NOTE but is not accepted
unless it separately satisfies all legs at S ≥ 0.85 (it won't be accepted in
pass 1; it will be emitted as fail-for-red-team only if S ≥ 0.70).

## Fuzzy-match scoring (PHONETIC/FUZZY; concrete rule implementations arrive
from the phonetician at GO — rule NAMES below are frozen, parameter values only)
For window W of n pairs and candidate reading R (French word string):
seg(R) = syllable segmentation per phonetician rules (by-ear spelling,
inconsistent cutting).

Components (each in [0,1]):
- lex_fit = (# words of R attested in era-corpus vocabulary) / (# words of R).
  Attestation = exact string or era-orthography normalization (ORTH-1835:
  collége/poëte/asyle spellings per linguist F15). "ça" banned outright.
- cut_fit = licit-assignment fraction over the n pairs. A pair scores 1.0 if it
  maps 1:1 onto one syllable of seg(R); 0.5 if it maps onto part of a syllable
  licensed by SPLIT-PAIR (split-pair emission prior, STATE next-item 9); 0.0 if
  it straddles a syllable boundary without licensing. cut_fit = mean.
- bound_fit = clamp(mean(flank_conf) + 0.25*B_align − 0.50*B_cross, 0, 1),
  where flank_conf = segmenter boundary confidences at the window edges;
  B_align = # window edges coinciding (±0 pairs) with an R→C or B→B phase
  transition (boundary-favoring: R→C +12.62, B→B +12.53 in
  `code/crowd3/segmenter_results.json` s_top_boundary); B_cross = # R→C or B→B
  transitions strictly inside the window that the candidate crosses with a
  within-word join.
- len_fit = 1.0 if syllable-count(seg(R)) == n; 0.5 if off by 1; else 0.0.

FROZEN weights (rationale frozen too — bound gets the LOWEST weight because the
phase instrument is VOID per red team F26; era lex attestation is the hardest
evidence per F15 register point; len/cut encode the per-syllable syllabary
structure per F30):
  S = 0.30*lex_fit + 0.25*cut_fit + 0.20*bound_fit + 0.25*len_fit

Rules that may fire (logged per candidate):
  MUTE-E (crib writes mute final -e as 40="e" per F26 — candidate mute -e must
    be assigned to a group, else −0.25 on the affected pair's cut_fit),
  ELISION (l'/d'/j' as single-letter units per linguist segmentation),
  SPLIT-PAIR, ORTH-1835, NASAL-VAR (by-ear nasal spelling; 06 polyvalence),
  DOUBLE-CONS (hon-neur split convention), VERB-STEM (06-class windows prefer
    verb forms per F21), RIVAL-NOTE (above).

## Acceptance (all must hold)
1. S ≥ 0.60 (FROZEN — no fitting to data)
2. lex_fit ≥ 0.50
3. len_fit ≥ 0.50
4. bound_fit ≥ 0.30
5. No pinned-anchor contradiction (above); 24/52/06/47/62/64-meme implications
   recorded as UNCONFIRMED hypotheses, never as accepted values.

Emission: top-5 candidates per window by S; every candidate with S ≥ 0.50 is
emitted with pass/fail flag and full component + rule-fire record. Failures
are first-class data (audit + red team).

## Pre-registered control (scorer lesson: N16/N5 — control-first)
Before judging pass 1, re-run the identical slide on 3 shuffled controls
(fixed seed 1841; preserve group frequencies; windows at same positions).
VOID CONDITION: if real-window accept count < 2× mean(control accept count),
pass 1 is VOID (null) — no claims merge.

## Window inventory (frozen positions; 0-based pair indices)
(a) W-S01..W-S25 — 25 segmenter crib-drag targets, in score order (from
`code/crowd3/segmenter_results.json`, crib_drag_targets_STRUCT):
  S01 1579-1580 [24 53] CB | S02 1552-1554 [99 13 93] RRA | S03 837-838 [98 20] CB |
  S04 453-454 [77 60] CB | S05 1566-1567 [24 74] CB | S06 1842-1843 [78 49] CB |
  S07 960-962 [00 86 56] RAC | S08 1670-1671 [55 81] RA | S09 1601-1602 [00 44] RA |
  S10 210-211 [88 19] CB | S11 478-481 [45 93 00 13] BARR | S12 407-408 [00 33] RA |
  S13 1110-1112 [41 65 38] CBA | S14 81-83 [51 62 16] CBA | S15 1703-1705 [62 94 88] BAC |
  S16 1-2 [00 97] RR | S17 1697-1699 [91 85 33] CBA | S18 507-509 [77 62 94] CBA |
  S19 1073-1076 [98 12 48 77] CBAC | S20 1538-1540 [62 93 88] BAC |
  S21 1758-1760 [41 15 93] CBA | S22 1844-1845 [74 93] BA |
  S23 1184-1187 [06 59 42 06] ACBA | S24 712-715 [12 63 00 66] BARA |
  S25 1581-1584 [12 44 00 36] BARA. flank_conf and phases carried from the JSON.
(b) W-47 — 47-neighborhood: pairs 146-157. Sub-windows: starts 146..153 ×
  lengths 3,4,5 (36 sub-windows). Contains 150-154 = 87 64 96 47 46
  ("ce qui par 47 que", provisional anchors 87=ce/64=qui/96=par/46=que pinned).
(c) W-62B — 62→94 bigrams @429, 517, 773, 1357, 1744, ±3 pairs each
  (5 windows). CALIBRATION FLAG: NOTES.md claims 62→94 ×8; file-measured ×5 —
  coverage via W-62C subsumes any missing positions; discrepancy reported.
(d) W-62C — remaining 62 positions (32), ±3 pairs each, overlapping merged.
(e) W-24 — all 42 24-positions (29,41,69,165,168,182,193,225,253,262,362,366,383,
  404,482,497,544,556,744,795,822,863,870,933,990,1104,1218,1246,1303,1347,1378,
  1439,1468,1517,1523,1602,1651,1691,1771,1778,1872,1873), ±3 pairs, overlaps merged.
(f) W-52 — all 13 52-positions (162,289,642,690,1076,1102,1122,1336,1446,1465,
  1471,1731,1816), ±3 pairs, overlaps merged.
Slide priority order: (a) → (b) → (c) → (d) → (e) → (f).

## Candidate inventory (frozen — built at GO, no additions after first slide)
1. ERA-VOCAB: unique word forms from the two Tocqueville files, 1–5 syllables,
   era orthography, attested ≥3× (cutoff frozen). Syllabified per phonetician rules.
2. SURVIVING FORMULAE (all "J'ai l'honneur d*" forms EXCLUDED — H5 DEAD per N11):
   - "Par ma dépêche du" (par-ma-dé-pê-che-du)
   - "En réponse à la dépêche de Votre Excellence du" (en-ré-pon-se-à-la-dé-pê-che-de-vo-tre-ex-cel-len-ce-du)
   - "Agréez, Monsieur, l'assurance de ma haute considération" (a-gré-ez-mon-sieur-l'-as-su-ran-ce-de-ma-hau-te-con-si-dé-ra-tion)
   - "Je renouvelle à V. Exe. l'assurance de ma considération distinguée"
     (je-re-nou-ve-lle-à-V-Exe-l'-as-su-ran-ce-de-ma-con-si-dé-ra-tion-dis-tin-gu-ée)
   - subjunctive triggers: "veuillez", "je vous prie de", "il est à désirer que"
3. 1841 COLLOCATIONS (frozen list): "ce qui", "parce que", "de ce que",
   "tout ce qui", "ne pas", "ne que", "que je", "je vous", "votre excellence",
   "monsieur", "par ma", "en réponse", "cela" (flagged register-dependent per F10),
   "on ne", "dont", "sans", "entre", "contre", "pour", "dans", "comme",
   "aussi", "très", "plus".

## Output
`code/sidepath/slide_pass1.json` at GO: per candidate — window_id, start_pair,
end_pair, groups[], candidate_reading, score, {lex_fit,cut_fit,bound_fit,len_fit},
rules_fired[], pass_fail, anchor_implications[] (all UNCONFIRMED), control_tag
(real|ctrl-1|ctrl-2|ctrl-3).

## Signed
slider, 2026-10-07 ~09:22 CDT. Nothing above may be tuned to fit slide output.
