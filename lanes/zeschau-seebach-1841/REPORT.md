# Seebach Cipher — Lane Report

**Status: UNSOLVED.** DECODE R5005 (18 Jan 1841), a two-digit French syllabary,
3,764 digits / 1,846 pairs / 96 groups. Nine anchors: seven ground-truth pencil
cribs + two lane-inferred provisional anchors (87=ce, 64=qui). No decryption;
three attempts and a nine-executor crowd round have produced corrected data,
two new anchors, one structural discovery, and nine documented nulls.

Lane: `lanes/zeschau-seebach-1841/` · Report date: 2026-10-07 ·
Methodology log: `NOTES.md` · Checkpoint: `STATE.md`

---

## 1. Background

Heinrich Anton von Zeschau (Saxon finance minister, acting foreign minister
from 1835) wrote in cipher to his envoy in St Petersburg, Albin Leo von
Seebach, across 1841–43 (shelfmark: HStAD Dresden, 10731 Sächsische
Gesandtschaft in Russland, Nr. 12). The first despatch, R5005 (18 Jan 1841),
is a whole letter in a two-digit syllabary — letters and syllables mixed,
96 of 100 possible groups used, pairs only. Three sibling letters
(R5006–R5008, 1842–43) exist on DECODE but sit behind an authentication wall.

The catalogue page (Bourdeau, Sept 2026) lists the cipher as unsolved. A
rubbed-out pencil decipherment on the manuscript yielded seven cribs
(11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que — "la première … que").
Bourdeau tried every Dresden DECODE key (latest 1799–1806, none for this
fonds) and ran homophonic-letter and syllable solvers: the syllable solvers
"drift to fluent nonsense." Nobody had tried a **crib-anchored attack** —
pinning the seven known values and running constrained searches off them.
That is what this lane does.

Corrections this lane made to the catalogue one-liner before starting:
R5005 is **French, not German** (two sibling letters are German); there are
**seven** cribs, not three.

---

## 2. Data & provenance

All upstream files fetched 2026-10-07 ~06:10 UTC from
`github.com/dbourdeau/cyphersolver` (`targets/zeschau1841/`) via GitHub API
+ raw.githubusercontent.com. Reference corpora: Les Misérables Tome I
(Gutenberg 17489, 119,514 words — attempt 2) and Tocqueville,
*De la démocratie en Amérique* Tomes 1+2 (Gutenberg 30513/30514, 1835/1840,
214,861 words, formal political prose — attempt 3, era+register matched).

| file | sha256 |
|---|---|
| upstream-ct_R5005.digits.txt | `18d48ccdca83fe5133b840cd427d5b89046839c866441d1c7c06fc264493e73f` |
| upstream-ct_R5005.txt | `6db0807ff5b42f8bcc294409f99ca92f08e748dccb6c293c1a31bd766bc48069` |
| upstream-NOTES.md | `adc23d961e59a76a1040ae712f5b169720e7cf63eecd7fafe01df04ee7f34c42` |
| upstream-offsets.json | `6abc844c805d9d16567153c293793b3cb2a6f84e83886c7f20b5b3cb2a6f84e83886c` |
| upstream-profile.json | `e4ad7f831744385f286bba9cb8dceb3d50f7cf769b8fd87ee3ee2ecea9e18ce6` |
| upstream-hsolve.py | `dae94eb60077a5cb3f383e0c2ce238d3f8c32a3804e3ba41f2ea1c24a2697fa1` |
| upstream-syll.py | `e4be9e77a7cadf610cae077e9a92a83813cf068857132ca3ccff95155cfceae1` |
| upstream-syll2.py | `6268c218f607143617c60d701f95c9103c88b59114aae0ae2306ec786cf2bfb9` |
| upstream-syll3.py | `ac94a73a3603ab8b665ce4b6e4e121ee527de9da55b40392ab1d8e513cdcee04` |
| french-quadgrams.json | `a7ef886356b67030d6984dca3556568a5551fc97833fda69438515b4d1de843f` |
| gutenberg-17489-miserables1.txt | `a5de514ba7b9f2e1790e7e259c4e8b7a35ae1d29e4bf9a5f8767039c58b80503` |
| gutenberg-30513-tocqueville-t1.txt | `fafebe4f69bc8e7abc6ed95bd10c2257bd26a307b2c1071056187ef76154aeaa` |
| gutenberg-30514-tocqueville-t2.txt | `20e46d72bc398f1c903449908a35a691e0d32763234bc75b2376cd21dbe33ee9` |
| attempt2_results.json | `aa31e7398811e89af0c016059e7d5dcfac6aa4385dc16fe92a6dd3f6b88b349f` |

(Full list in `data/SHA256SUMS.txt`. `attempt1_results.json` and
`attempt3_results.json` are lane outputs; their hashes are recorded on write.)

**Pair segmentation.** ~1/3 of lines have odd digit counts, so groups run over
line breaks; upstream per-line offsets (32 lines offset 1) are applied.
Result: **3,764 digits → 1,846 pairs**, 96 distinct groups, group-stream
IC = 0.0142 (flat over 96 ≈ 0.0104 — mild structure, as expected for a
syllabary). **Discrepancy vs the catalogue page: the page claims 3,969
digits; the sha256-verified transcription files contain 3,764.** Recorded as
observed (F4).

![Fig 1](report_assets/fig1_frequency.png)

*Fig 1 — Group frequency rank chart. Ranks here are 1-based positions in the
frequency-sorted list; lane code and NOTES.md use 0-based indices (e.g.
rank(87)=15 in attempt 2 = #16 here).*

---

## 3. Methodology

### Attempt 1 — crib-anchored attack (`code/crib_attack.py`)

Three phases. **Phase A (verification):** transcription loads to 70 lines,
3,764 digits, 1,846 pairs, 96 groups — matches upstream's 96/100 claim.
All seven cribs present: 11=la ×44, 70=pre ×15, 82=m ×38, 34=i ×10,
29=er ×47 (rank 2 — consistent with 'er' as a top French syllable),
40=e ×21, 46=que ×29.
**Phase B (anchor-context profiling):** strongest bigram 82→16 in 11/38
cases (28.9%); 87→11 in 7/32 (21.9%, "87 la"). Followers of 46=que diffuse.
**Phase C (function-word drag):** NULL (N1) — at 7-anchor sparsity every one
of 1,000+ (group, word) candidates scores exactly at the quadgram floor
(−7.714); zero discrimination. Shelved.

Attempt 1 also corrected two upstream claims: the "×5 / ×3" long repeats
are **2× and 0× at pair alignment** — the extra hits are odd-phase substring
artefacts across pair boundaries, not true group repeats (F3); and the
digit-count discrepancy above (F4).

### Attempt 2 — bigram-hypothesis tests (`code/attempt2.py`)

Tested H1 (82=m → 16 as "ma") and H2 (87 → 11=la) against Les Mis rates,
each with 4–5 independent checks, promotion bar ≥2.

- **H1: PLAUSIBLE (1/4), not promoted.** rank(16) in the vowel band, but
  P(82|16)=0.39 (16 not bound to m), mi/me controls absent (82→34=1,
  82→40=0), and Les Mis P(a|m)=0.19 is not dominant in real French.
- **H2 (87="de"/"à"): REFUTED.** 87→46="que" occurs 3× — "de que"/"à que"
  are ungrammatical. Override applied even though two weaker checks passed.
- **H2b (87="ce"): CONFIRMED (4/5).** The refuting hits are what "ce"
  predicts: 87→11="cela" ×7 (P=0.219 ≈ Les Mis 0.278) and 87→46="ce que"
  ×3 (P=0.094 ≈ Les Mis 0.140); rank(87) common-word band; 14 distinct
  predecessors. The 24-87-46 "est-ce que" trigram missed (0×). 87=ce joined
  as a lane-inferred **provisional** anchor — 8 total.
- **Drag re-run (8 anchors): NULL** (N2) — still degenerate at the floor.

Erratum recorded (F8): attempt-1 prose "87→11 in 7/44" quoted P(87|11);
the hypothesis rate is P(11|87)=7/32=21.9%.

![Fig 2](report_assets/fig2_bigrams.png)

*Fig 2 — The four anchor-adjacency bigrams that drove attempts 2–3.*

### Attempt 3 — era-matched reference + H3 (`code/attempt3.py`)

Operator constraint: Les Mis (novel, 1862) mismatches an 1841 diplomatic
despatch in era **and** register. New reference: Tocqueville 1835/1840,
214,861 words of formal political prose. Method mirrors attempt 2.

![Fig 4](report_assets/fig4_era_comparison.png)

*Fig 4 — Four of five reference rates agree within factor 2 across the two
corpora; n("cela")/n("ce") disagrees 6.7× (0.041 vs 0.278) — a register gap,
not an era subtlety. Novels use "cela" in dialogue; formal prose almost
never does. The cipher's P(11|87)=0.219 sits with Les Mis, not Tocqueville —
itself a datum about the letters' register.*

- **H3 (64="qui"): CONFIRMED (4/4) → 9th anchor (provisional).**
  rank(64)=4 of 96; P(64|87)=0.1562 ≈ era P(qui|ce)=0.1878 — and "qui" is the
  #1 follower of "ce" in Tocqueville (213×, ahead of "que" at 122×);
  46=que→64 = 0 (no "que qui"); 28 distinct followers/predecessors, top
  share 0.07 — a free function word. Rival 64="ci" disfavoured
  (P(87|64)=0.109, not ceci-bound).
- **87=ce re-validated vs era: CONFIRMED (3/4).** The "cela"-rate leg now
  fails the factor-2 band against the era corpus and is downgraded to
  register-dependent; the confirmation stands on the other legs.
- **Drag re-run (9 anchors): NULL** (N3). The anchors-only baseline now
  lifts off the quadgram floor on some windows (density registering), but no
  (group, word) candidate separates. Window-quadgram scorer stays shelved;
  a syllable-level scorer is the candidate replacement.
- **Bonus datum:** 82→16 occurs 11× total, **0× within ±3 groups of 87=ce**
  — it avoids ce-windows entirely.

### Crowd round — nine executors, coordinator-curated

Fanned out in parallel, each a different mind; each wrote only to
`code/crowd/<name>_results.{md,json}`; the coordinator re-derived every
merged number against the lane data before recording it in NOTES.md.

| persona | angle | verdict |
|---|---|---|
| Phonotactician | constrained syllabary search, French syllable-structure scorer, 8 anchors pinned | **NULL** — optimizer beat baselines degenerately (4 syllables for all 88 free groups); scorer exploited, no signal |
| Crib Surgeon | positional attack on "la première" | **LEADS** — sequence occurs exactly once @1033; three hypotheses (24="est" strong/4 checks, 77="pas"/3, 06="ne"/3) |
| Contactor | contact-chain clustering of 96 groups | **STRUCTURAL FIND** — 3-phase rotation A→C→B→A, chi²=181.3 |
| Red Team | kill authority over 87=ce | **DEMOTED → PLAUSIBLE** — attempt-2 scorecard unsound (see §6) |
| Drag Racer | function-word drag v2, syllable-level scorer | **PARTIAL** — discriminates (54/55 distinct scores) but word-prior, not placement |
| Historian | archive-side research | **KEY NOT FOUND** — but concrete routes (see §8) |
| Formula Hunter | repeat census at pair alignment | **REPEAT CENSUS** — repeats are discourse set phrases; longest `56…01` ×2 @931/@1625 unread |
| Annealer | 24×60k stochastic hill-climb, 8 anchors pinned | **NULL, control-proven** — synthetic control recovers 1/88 (≈chance) |
| Linguist | 1841 French priors | **HYPOTHESIS** — ×5 repeat = "J'ai l'honneur de"; register mismatch > era mismatch |

![Fig 5](report_assets/fig5_verdict_board.png)

---

## 4. Verified findings (F-series)

- **F1** — Pair-of-digits unit; 96/100 groups occur; groups run over line
  breaks; division fixed by strongest pair statistics. (Upstream methodology,
  accepted.)
- **F2** — Seven pencil-crib values as ground-truth anchors.
- **F3** — Long repeats are **2×** (`77 78 94 82 06`) and **0×**
  (`06 77 78 18 71 10 01`) at pair alignment; upstream's ×5/×3 include
  misaligned substring artefacts.
- **F4** — Transcription holds **3,764 digits**, not the 3,969 claimed.
- **F5** — Bigram 82→16 in 11/38 (28.9%) — strongest anchor-adjacent pattern.
- **F6 (revised)** — 87="ce": scored CONFIRMED 4/5 in attempt 2, then
  **demoted to provisional/plausible** by the red team (see §6); re-validated
  3/4 against era rates in attempt 3. Best-tested reading; cela-leg
  register-dependent.
- **F7** — 82→16 as "ma" (16="a") not confirmed: PLAUSIBLE (1/4).
- **F8** — Erratum: "87→11 in 7/44" quoted P(87|11); correct rate
  P(11|87)=7/32=21.9%.
- **F9** — 64="qui" CONFIRMED (4/4) → provisional anchor 9.
- **F10** — Era-matched reference corpus built (Tocqueville 1835/1840,
  214,861 words); the 6.7× "cela" register gap found.
- **F11** — **3-phase rotational contact structure A→C→B→A**: P(A→C)=0.418,
  P(C→B)=0.450, P(B→A)=0.476 (1.35–1.52× over independence), chi²=181.3 on
  4 df (p≪1e-6), self-transitions suppressed (0.51–0.74×). 29=er anchors
  phase C (word-final-ish). 87↔82 is the highest anchor-anchor Jaccard
  (0.423) with identical C→X→A block signature.
- **F12** — **"la première" = 11-70-82-34-29-40 occurs exactly once @pair
  1033 (56.0%)** — six consecutive ground-truth anchors, byte-level
  confirmed, curator re-derived. The lane's first multi-group word read.
  Mid-letter back-reference context.
- **F13** — Attempt-2's "P(cela|ce)=0.278" was a count ratio, not a
  conditional; and P(46|87,pre=96)=3/3 vs P(46|87,pre=24)=0/10 — the "que"
  after 87 is licensed by predecessor 96, never 24.
- **F14** — Repeat census: 13/16 long repeats (L≥5) are body/body;
  **no repeat is exclusive to the opening or closing 100 groups**.
  Longest: `56 69 26 00 33 21 64 37 01` ×2 @931/@1625 (unread — top
  crib-drag target). `96 87 46` ×3 ("parce que"/"de ce que", unchecked).
  `24 87 64` ×3 ("[pour|en] ce qui"). `77 78 94 82 06` ×2 @1179/@1350.
- **F15** — Register mismatch with Les Mis is more dangerous than era
  mismatch (first-person administrative French vs narration+dialogue+argot).
  Orthography post-1835/pre-1878 ("collége", "poëte", "asyle"); "cela":"ça"
  = 47:1 in 1835–1850 print. Syllable tiers from Meisel 1826 diplomatic
  corpus.
- **F16** — Identities: Heinrich Anton von Zeschau (1789–1870), Saxon
  finance minister / acting foreign minister; Albin Leo von Seebach
  (1811–1884), Saxon envoy in St Petersburg 1839–1852, Nesselrode's
  son-in-law.

![Fig 3](report_assets/fig3_position_map.png)

*Fig 3 — The single "la première" occurrence and its ±10-pair window. Green
= ground-truth anchors, amber = provisional (87=ce, 64=qui).*

![Fig 6](report_assets/fig6_contact_structure.png)

*Fig 6 — The contactor's 3-phase structure, the cipher's first known
architectural property.*

---

## 5. Failures & null results (N-series)

Nulls are first-class in this lane. Every one below is a measured outcome,
not an absence of trying.

- **N1** — Function-word drag at 7-anchor sparsity: degenerate, all
  candidates at the quadgram floor (−7.714).
- **N2** — Drag re-run at 8 anchors: still degenerate.
- **N3** — Drag re-run at 9 anchors: baseline lifts off the floor on some
  windows, but no candidate separates. Window-quadgram scorer shelved.
- **N4** — Phonotactic syllabary search: optimizer exploited the scorer
  (4 syllables for 88 groups); 1/88 stable across restarts.
- **N5** — Syllable-bigram annealing: **method-broken-on-control.**
  Synthetic control (known random syllabary, 8 anchors pinned): 1/88
  recovered (≈chance); the planted true key scores −5.36/pair while the
  annealer's "best" nonsense scores −2.90 — the scorer's global optimum sits
  ~2.5 nats/pair *above* real French. Bourdeau's failure mode, now proven
  by control rather than inferred.
- **N6** — Syllable-level drag: discriminates (54/55 distinct scores) but
  the discrimination is word-prior, not placement; only exact multi-anchor
  placement is cela=87-11 ×7.
- **N7** — No 1840s Saxon cipher key in any published source or catalogue
  checked (DECODE Dresden keys stop at 1799–1806).
- **N8** — Both pre-registered contact predictions failed as stated.
- **N9** — No 46=que within ±10 of the "la première" crib; no second
  "première" anywhere.

**The red-team demotion (the lane's most consequential null).** Attempt 2
scored 87="ce" CONFIRMED 4/5. The red team reproduced every count, then
voided the scorecard: check (b)'s "P(cela|ce)=0.278" was **n_cela/n_ce — a
count ratio, not a conditional**. The honest syllable-level bound is
P("la"|"ce"-syllable) ≤ 0.1805, and the observed 0.2188 *exceeds* it
(check void); checks (a)/(d) also passed for the refuted de/à
(non-discriminating); check (c) is n=3. Demoted to provisional/plausible.
No alternative beats "ce" — the kill failed on alternatives and succeeded
on scorecard integrity. Everything downstream that used 87=ce (N2 drag)
inherits the uncertainty; attempt 3's era re-validation (3/4) keeps it as
the best-tested reading.

---

## 6. Open hypotheses (not promoted — each needs ≥2 independent checks)

- **24="est"** (crib surgeon, strong, 4 checks): rank-1 band;
  P(ce|24)=0.192 vs 1.7% base; "qu'est" elision ×3. Anomalies: "est-ce
  que"=0×; "est cela"×3. **If confirmed, the 24-87-46 0/10 becomes a hard
  joint contradiction for 87=ce (binomial p=9.1e-04) — either way it breaks
  the 87 deadlock.**
- **77="pas"** (3 checks; caveat: rival "ne"-like predecessor 67→77 ×6).
- **06="ne"** (3 checks: rank-3 band, ratio, bigram).
- **96="par"/"de"** (licenses 96-87-46 "parce/de ce que" ×3);
  **41="der"/08="ni"** ("dernière" @59–63).
- **×5 repeat 77 78 94 82 06 = "J'ai l'honneur de"** (linguist):
  5 syllable units (j'ai·l'·hon·neur·de); test the l'-position as a
  single-letter consonant; check hon–neur adjacency.

---

## 7. Next steps (from STATE.md)

1. **Resolve 24="est"** — the highest-leverage test on the board.
   Re-validate the "est cela"×3 anomaly against the era corpus.
2. **Test "J'ai l'honneur de"** on the ×5 repeat; crib-drag the unread
   9-mer `56…01` @931/@1625 against the era corpus.
3. **DECODE registration** (operator's word obtained 2026-10-07 — in
   progress) to unlock R5006–R5008 full images; **HStAD Dresden mail-in
   scan order** (`poststelle@sta.smi.sachsen.de`) for 10731 Nr. 12 and
   10717 Nr. 3332/3333 — the ministry-side correspondence and the
   key-candidate files.
4. Attempt 4 (queued): exploit 64=qui — the five "ce qui" contexts, joint
   87/64 windows, re-examine 82→16 in qui-anchored windows, syllable-level
   scorer.

**Blockers:** R5006–R5008 behind DECODE login (registration in progress);
no 1840s Saxon key published; the erased pencil decipherment needs
UV/multispectral imaging (physical access, HStAD).

---

## Appendix — file inventory

```
zeschau-seebach-1841/
├── REPORT.md                  ← this report
├── NOTES.md                   ← full methodology log, F1–F16, N1–N9
├── STATE.md                   ← status / checkpoint / next / blockers
├── report_assets/
│   ├── fig1_frequency.png         group frequency rank chart
│   ├── fig2_bigrams.png           anchor-adjacency bigrams
│   ├── fig3_position_map.png      "la première" @1033
│   ├── fig4_era_comparison.png    era vs Les Mis rates
│   ├── fig5_verdict_board.png      attempts 1–3 + crowd verdicts
│   └── fig6_contact_structure.png 3-phase rotation schematic
├── code/
│   ├── crib_attack.py             attempt 1 (3 phases)
│   ├── attempt2.py                bigram-hypothesis tests
│   ├── attempt3.py                era corpus + H3 64="qui"
│   ├── make_report_figures.py     figure generator (this report)
│   └── crowd/
│       ├── phonotactician.py / phonotactician_results.{md,json}
│       ├── crib_surgeon_results.{md,json}
│       ├── contactor.py / contactor_results.{md,json}
│       ├── red_team_results.{md,json}
│       ├── drag_racer_results.{md,json}
│       ├── historian_results.{md,json}
│       ├── formula_hunter_results.{md,json}
│       ├── anneal.py / annealer_results.{md,json}
│       └── linguist_results.{md,json}
└── data/
    ├── upstream-*.{txt,json,py,md}   Bourdeau transcription + solvers (hashed)
    ├── french-quadgrams.json        letter-quadgram scorer (shelved)
    ├── gutenberg-17489-miserables1.txt   Les Mis reference (superseded)
    ├── gutenberg-30513/30514-tocqueville-t*.txt  era reference (current)
    ├── PROVENANCE-tocqueville.txt
    ├── SHA256SUMS.txt
    ├── attempt1_results.json
    ├── attempt2_results.json
    └── attempt3_results.json
```

Anchor key (ground truth vs provisional, used throughout):

| group | value | status |
|---|---|---|
| 11 | la | pencil crib (ground truth) |
| 70 | pre | pencil crib (ground truth) |
| 82 | m | pencil crib (ground truth) |
| 34 | i | pencil crib (ground truth) |
| 29 | er | pencil crib (ground truth) |
| 40 | e | pencil crib (ground truth) |
| 46 | que | pencil crib (ground truth) |
| 87 | ce | lane-inferred, **provisional** (best-tested; cela-leg register-dependent) |
| 64 | qui | lane-inferred, **provisional** (CONFIRMED 4/4, attempt 3) |

*Rank convention: figure labels use 1-based positions in the frequency-sorted
list; lane code and NOTES.md use 0-based indices (figure #N = code rank N−1).*
