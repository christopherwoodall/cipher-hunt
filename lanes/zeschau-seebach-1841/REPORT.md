# Seebach Cipher — Lane Report

**Status: UNSOLVED.** DECODE R5005 (18 Jan 1841), a two-digit French syllabary,
3,764 digits / **1,847 pairs (repaired parse)** / 96 groups. Fourteen values:
seven ground-truth pencil cribs + seven provisional lane-inferred values
(87=ce, 64=qui, 96=par, 94=ne, 06=verb-stem class, 67=veut class, 77="le"
conditioned) + leads (62="on" fenced-lead, 78="me"-syllable, 78={ver,er}
fork [was 78="ver" islet — F61], 52="pas", 24="en", 47="ce", 59="est"
strong-lead [pre-red-team], 00="pour" strong-lead [pre-red-team],
78-45="même", 84="en" vs 84=noun-class [unresolved conflict, both LEAD],
43="me" WEAK, 00="le" ×3 LEAD, "Mehemet-Ali" @8 LEAD, T4 (c)
"gouvernement" LEAD). No decryption;
three attempts, seven crowd rounds, and six side fleets have produced a repaired
canonical parse (bedrock-audited, F41), a second "la première" occurrence, a
quantified conditioned-polyvalence model, and thirty-two documented nulls.

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
(R5006–R5008, 1842–43) exist on DECODE but sit behind an authentication wall;
the operator registered a DECODE account (`alexrivers`) on 2026-10-07, but
full-size private-ciphertext images need admin elevation (see §7).

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
(Gutenberg 17489, 119,514 words — attempt 2; superseded) and Tocqueville,
*De la démocratie en Amérique* Tomes 1+2 (Gutenberg 30513/30514, 1835/1840,
214,861 words, formal political prose — attempt 3, era+register matched).

| file | sha256 |
|---|---|
| upstream-ct_R5005.digits.txt | `18d48ccdca83fe5133b840cd427d5b89046839c866441d1c7c06fc264493e73f` |
| upstream-ct_R5005.txt | `6db0807ff5b42f8bcc294409f99ca92f08e748dccb6c293c1a31bd766bc48069` |
| upstream-NOTES.md | `adc23d961e59a76a1040ae712f5b169720e7cf63eecd7f34c42` |
| upstream-offsets.json | `6abc844c805d9d16567153c293793b3cb2a6f84e83886c7f20b5b3cb2a6f84e83886c` |
| upstream-profile.json | `e4ad7f831744385f286bba9cb8ba9cb8dceb3d50f7cf769b8fd87ee3ee2ecea9e18ce6` |
| upstream-hsolve.py | `dae94eb60077a5cb3f383e0ce238d3f8c32a3804e3ba41f2ea1c24a2697fa1` |
| upstream-syll.py | `e4be9e77a7cadf610cae077e9a92a83813cf068857132ca3ccff95155cfceae1` |
| upstream-syll2.py | `6268c218f607143617c60d701f95c9103c88b59114aae0ae2306ec786cf2bfb9` |
| upstream-syll3.py | `ac94a73a3603ab8b665ce4b6e4e121ee527de9da55b40392ab1d8e513cdcee04` |
| french-quadgrams.json | `a7ef886356b67030d6984dca3556568a5551fc97833fda69438515b4d1de843f` |
| gutenberg-17489-miserables1.txt | `a5de514ba7b9f2e1790e7e259c4e8b7a35ae1d29e4bf9a5f8767039c58b80503` |
| gutenberg-30513-tocqueville-t1.txt | `fafebe4f69bc8e7abc6ed95bd10c2257bd26a307b2c1071056187ef76154aeaa` |
| gutenberg-30514-tocqueville-t2.txt | `20e46d72bc398f1c903449908a5f8767039c58b80503` |

(Full list in `data/SHA256SUMS.txt`. `attempt1_results.json` and
`attempt3_results.json` are lane outputs; their hashes are recorded on write.
**Note:** the last three rows above were transcription-corrupted in an
earlier draft of this report — the authoritative hashes are in
`data/SHA256SUMS.txt`, which the sweeper trusts over this table. The
`french-quadgrams.json` row above likewise is superseded by SHA256SUMS.txt.)

**The parse repair (F32; previously mislabeled F17 in this report).** The side-keyhunt red team killed the canonical
1,846-pair parse: the digit stream contains `117082342940` twice (raw
positions 1532, 2108); the a5_03 occurrence sits under the pencil "la
première" gloss, so pair-phase there must be even. Single-bit repair:
EM offset a5_03 1→0 (`code/side-keyhunt/repaired_offsets.json`,
`repair_parse.py`, spec in `methodology-ruling.md`).
**3,764 digits → 1,847 pairs; 96 groups unchanged; all other rows
byte-identical.** "la première" now occurs **twice**, 0-based @754 and @1034.
Old-parse pair indices ≥773 shift +1 (position map in
`code/crowd4/REINDEX.md`). Manuscript-image caveat: if the gloss line-tag
a5_03 is wrong, the canonical revives. Anything built on the old parse —
skeleton ledger (30.66% coverage on 1,846), tester harness, banked contactor
phases, this report's figures before regeneration — must be rebuilt or
re-derived.

**Instruments built this round (lane-local, all in `code/`):** a repaired
parse (`code/crowd4/repaired_parse.py`, `code/crowd4/phase_map_repaired.json`);
a 17-group applied-value ledger (`code/sidepath/skeleton.json`, built on the
old parse — **stale, rebuild queued**); an 11,870-word pattern lexicon with a
custom orthographic syllabifier
(`code/side-wordpattern/lexicon/`, `PROVENANCE.md`, `SELFTEST.md`);
a polyvalence-expanded index with gate verdict
(`code/side-wordpattern/polyvalence/POLYVALENCE_REPORT.md`); a synthetic
homophonic control suite (`code/side-homophonic/control/CONTROL-DESIGN.md`,
6 instances × 1,846 pairs); a pre-registered slide harness
(`code/sidepath/prereg_pass1.md`); a Petit-Chiffre key tester harness
(`code/side-keyhunt/test_table.py` — needs repair to the 1,847 parse before
it issues verdicts).

![Fig 1](report_assets/fig1_frequency.png)

*Fig 1 — Group frequency rank chart (repaired 1,847-pair parse). Green =
pencil-crib ground truth (7), amber = provisional values (6), gray =
unidentified/leads.*

---

## 3. Methodology

### Attempt 1 — crib-anchored attack (`code/crib_attack.py`)

Three phases. **Phase A (verification):** transcription loads to 70 lines,
3,764 digits, 96 groups — matches upstream's 96/100 claim.
All seven cribs present (repaired-parse counts; bedrock-verified):
11=la ×45, 70=pre ×15, 82=m ×39, 34=i ×11, 29=er ×45 (rank 4 on the
repaired parse — still a top French syllable), 40=e ×21, 46=que
×29. **Phase B (anchor-context profiling):** strongest bigram 82→16 in
11/39 cases (28.2% on the repaired parse); 87→11 in 7/32 (21.9%, "87 la").
Followers of 46=que diffuse.
**Phase C (function-word drag):** NULL (N1) — at 7-anchor sparsity every one
of 1,000+ (group, word) candidates scores exactly at the quadgram floor
(−7.714); zero discrimination. Shelved.

Attempt 1 also corrected two upstream claims: the "×5 / ×3" long repeats
are **2× and 0× at pair alignment** — the extra hits are odd-phase substring
artefacts across pair boundaries, not true group repeats (F3); and the
digit-count discrepancy (F4).

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

*Fig 2 — The four anchor-adjacency bigrams that drove attempts 2–3 (repaired
parse): 82→16 11/39=28.2%, 87→11 7/32=21.9%, 87→64 5/32=15.6%,
87→46 3/32=9.4%.*

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
  rank(64)=3 of 96 on the repaired parse (was 4 on the old); P(64|87)=0.1562 ≈ era P(qui|ce)=0.1878 — and "qui" is the
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

### Crowd rounds 1–5 (`code/crowd/`, `code/crowd2/`, `code/crowd3/`,
`code/crowd4/`, `code/crowd5/`)

Fanned out in parallel, each executor a different mind; each wrote only to
its own results files; the coordinator re-derived every merged number
against the lane data before recording it in NOTES.md. Round-1 verdicts are
kept (phonotactician NULL, crib surgeon LEADS, contactor STRUCTURAL FIND,
red team demotion, drag racer PARTIAL, historian KEY NOT FOUND, formula
hunter REPEAT CENSUS, annealer NULL control-proven, linguist HYPOTHESIS —
see fig 5). Round 2 adjudicated the crib surgeon's leads: **24="est"
REFUTED** on era rates (19.5× and 74× kills; the 24-87 predecessor
enrichment now points at the provisional 87=ce itself — exactly as the red
team suspected; inversion sweep over 45 words: empty intersection),
**96="par" CONFIRMED 4/4** (10th value, provisional, conditional on 87=ce),
**06="ne" REFUTED** (20.6× on the era conditional; 06→29(er) 5× vs era 0),
H5 "J'ai l'honneur de" killed structurally (82 is the GT 'm' cell — a
syllabary doesn't reuse the m-cell for "neur"), 9-mer drag NULL. Round 3
brought the ear: the frenchman found the encipherer spells by ear and cuts
inconsistently ("personne" as both per|so|nne and pers|on|ne; prend→pre;
première→pre|m|i|er|e), making **the ear the lane's primary instrument**
and killing rigid syllabification three ways (tuner LOO 2/34 vs 6/34,
calibration exclusion, ear-cutting). Round 3 red team (13 rulings): 2 kills
(the stem-hunter's 06=/mɑ̃/ CONFIRMED, killed by the GT mute-e in
"première"; 06="ent" general refuted), 7 demotions, zero new CONFIRMED
promotions. Round 4 re-battery on the repaired parse: **94="ne" holds
provisional-strong** on rebuilt legs (host odds 2.27:1, 641 "nement"-hosts
vs 282 "rement" disjoint, compositional frames ne 8/3 vs en 4/2 vs re 0/0),
94="re" disfavored (fenced on @578's unidentified trigram host), 94="en"
survives only as conditioned islets (pre=82 "m'en" ×3 or suc=87 "en ce"
×1), **47="ce" WORD is the lead** (B1 "ce que" 3/28=0.1071 vs era
122/1134=0.1076 — 1.00× exact; "par me" era n=0 kills the word reading),
**62="on" is a promotion candidate** (third leg: @848 fresh-window
subject-triangulation with 21="me" forcing a subject — zero
counterexamples in 34 windows), **78="me" survives as a LEAD** (the B-78b
repair flipped the headline leg 1.658 in-band → 2.259 OUT; the word-space
"le me" frames stay adverse).

Round 5 (adjudicated): **77="le" promoted → provisional (conditioned)** —
the lane's first promotion in five rounds; **62="on" promotion DENIED →
fenced-lead** (leg 1's subject premise is ear-derived and undisclosed;
Check C χ² struck — exact MC p=0.0450; profile fits "il" equally);
**78 split adjudicated** — "me"-word disfavored-strong, "me"-syllable
LEAD, "ver" LEAD conditioned islet, **coexist**; **@578 revival thread
buried** (sixmer ×2 @573/@1164 makes 94 a particle; 94="re" general stays
disfavored); **47="ce" strengthened LEAD** (C2 dissolved, Q1/Q2
conditions, promotion blocked on @148–152); **06 stem NULL** (honest —
single-stem killed 17.1×); **M1 accepted** (06/86 complementary
distribution, F33-grade); **joint-engine diagnosis REVERSED** — the
objective is wrong, not the search (truth −32.64 vs annealed −2.91 on the
configured objective; N19); **rotation linguistic mappings killed**
(morphological, polyvalence-conditioning, unit-size; syntactic NULL —
N20) with a period-3 rhythm lead (E1, F38); **87=ce new legs** (A1
"c'est" word-space, A3 24→87 ce-like, A2 47≠87's "ce" — F35); **@754 vs
@1034 compared** (different contexts, discourse-anaphoric reframe,
43="me" fenced — F36); **unit inventory consolidated** (24 units, 10
exclusions — F37). Red-team kill ledger: promotions 1, demotions 0, kills
0, fenced 1; armed baseline 29/29 PASS.

### Crowd round 6 (`code/crowd6/`) — EXECUTOR-GRADE, RED-TEAM-REVIEWED VIA ROUND 7

Round-6 red-team review landed through crowd7 (F61 — F26-17: 12/13 marks
upheld on 61/61 new + 49/49 inherited baseline checks; N44 corrected to net
0/2/0/1; T4 either/or adjudicated: (c) "gouvernement" LEAD, (a) disfavored).
The armed baseline was extended first: 30 inherited + 19 round-6 checks =
**49/49 PASS** against the repaired stream. Claims below are executor-graded
with red-team review where marked — F44/F45/F47/F48 stay LEAD (promotion
denied where noted), F26-17 review holds kill authority.

- **Bigram closer (exploit 77="le"):** 84 = masculine NOUN **LEAD-grade**,
  identity NULL (honest, register-robust — F46): article-frame ×8
  ("le 84" ×7, "la 84" ×1) + que-clause-subject ×3 ("que 84" ×2, "que le
  84 24" ×1); 84="fait" re-killed 6.75×, 84="gouvernement" 6.12×. The
  slot re-parsed: **84→59 is ×4, not ×2** (earlier undercount corrected),
  and 59→46 ×2 / 59→37 ×6 make 59="verb" a LEAD — so 64-77-84-59 ×2 =
  "qui le [noun] [verb]": **the verb slot is 59, not 84**. The "le me"×7
  DISSOLVES per-instance, both fences mapped, zero holdouts (2/7 the
  "ver"-islet inside the ×2 5-mer; 5/7 me-syllable frames; P(78|77)=0.159
  vs P(78|47)=0.179 — 77 is unremarkable, no special "le me" construction).
  45="me"-word **disfavored-strong** (unigram 9.14× out, "par me" ×2
  era-0, "me qui" ×3 era-0 fenced on 64="qui"); **78-45="même" LEAD**
  (0.57× in-band, "le même qui" lock @313 under 37="le"). Trace:
  `code/crowd6/bigram_closer/{closer6.py,closer6.md,closer6*.json}`,
  `report_inbox/bigram-closer-77le.md` (this sweep).
- **Closer WO-A (84 from the 87-side) + WO-B (00="pour"):** **84="en"
  LEAD** (sole survivor; promotion BLOCKED): unigram 1.10×, "qu'en"
  1.36× (GT-anchored), "n'en" common, "m'en" on GT 82=m; but "l'en"
  runs **141×/63× over era** under the standing 77="le" [prov] — kill-grade,
  blocks promotion; 24/25 windows read cleanly. Rival kills banked:
  84="plus" KILLED (via 59="est": "plus est" era ~0), 84="a" KILLED,
  84=verb-class KILLED. **DIRECT CONFLICT with the bigram closer** (84=noun
  vs 84="en"): untested resolution flagged for round 7 — conditioned
  polyvalence (84="en" iff pre∈{46,94,82}, 84=noun iff pre∈{77,11});
  9/25 predecessors unclassified, so a battery, not adjudication.
  **59="est" STRONG LEAD** (1.39×; "qui est" ✓; "n'est" at era P=0.238,
  n=324; fenced adverse: 59→37 ×6 reads 6.47× over era conditional on
  37="le" [MEDIUM]; interacts with the 01="est" lead — red-team call).
  **00="pour" STRONG LEAD**: M1 governor frame (00→86 ×12 "pour [inf]"
  vs 00→06 ×0) + conditional rates + full rival sweep all pass, but the
  unigram is 6.22× over era and "pour que" 3.85× — promotion blocked on
  rates. Elision discipline matters: the cipher writes UNELIDED
  ("c'est"=87-01), so cipher "que"+"en" compares to era "qu"+"en", not
  "que"+"en". Trace: `code/crowd6/closer/closer87_00.{py,md,json}`,
  `report_inbox/closer-87ce-00pour.md` (this sweep).
- **Frenchman (62="on" non-ear battery):** NO PROMOTION — 62="on" stays
  STRONG LEAD (fenced); honest null (N25): on≈il tie on clean pieces
  (joint −26.54 vs −26.82, Δ=+0.27 nats; "qui" weakly disfavored −6.2).
  Cipher-internal calibration **voids the old "il"-differential AND the
  merger corroboration**: the encipherer writes /k/+V SPLIT (46→29 ×2
  "qu'er", never before /i//e/), not merged. One caveated adverse datum
  for "on" under H-split (46→62=0/29, E=7.18, p=2.6e-4 — single,
  four-ways caveated, adverse not kill-grade). The profile route is proven
  unbridgeable with the current inventory; 59=verb banked (GT-anchored:
  11→59 ×1, 59→46 ×2, 59→37 ×6). Trace:
  `code/crowd6/frenchman62/{battery62.py,era_rates.py,qu_rates.py,que_contexts.py,windows.py,battery62_results.json,frenchman62_round6.md}`,
  `report_inbox/frenchman-62-non-ear.md` (this sweep).
- **Morphologist:** WO-A (96 conditioned-verb battery, the ranked-#1
  unblocker for 47="ce" promotion) = **UNVERIFIABLE — honest null** (N26):
  the "ce qui __ ce que" frame (87-64-X-47-46) is a hapax (1/1,847); 20/21
  other 96-frames are clean "par" (parce_que ×4 @150/@224/@952/@1526,
  par_43 ×2, par+NP ×14); era "ce qui"+verb 213/213 in Tocqueville.
  47="ce" promotion stays BLOCKED. WO-B (67 classification): et/veut fork
  **SUPPORTED as conditioned polyvalence (F33-form), NOT promoted** —
  19/38 classified with ZERO cross-contamination (et-side 8 kill "veut";
  veut-side 11 kill "et"; fork ratio 113.0); "la veut" @1044–1045 pins a
  3sg transitive verb, NOT uniquely "veut"; 19/38 open. **43="me"
  DOWNGRADED MEDIUM→WEAK** ("par 43"×2 n_eff=1, era "par me"=0). Trace:
  `code/crowd6/morphologist/{battery96_67.py,battery96_67_results.json}`,
  `report_inbox/morphologist-96-67.md` (this sweep).
- **Scorer (round 6):** repaired-objective re-run PRE-REGISTERED
  (`code/crowd6/scorer/PREREG.md`; `objective.py`, `phonetics.py`,
  `models.py`, `selftest_objective.py`, `step0_baseline.py`): frozen
  objective S = S_let_proj + LAM_WORD·S_word + LAM_ROT·S_phase + S_prior −
  LAM_POLY·n_poly + S_conc — phonetic projection, longest-match
  non-overlapping spanning word bonus (the side fleet's D2 overlapping-hit
  bug explicitly NOT imported), concentration penalty ON, LAM_POLY set by
  crossover calibration at 2× margin, LAM_ROT=0 held out, inventory top-600
  rule units + letters. Steps 0/0.5/1/2/3/4 ALL LANDED (executor-grade,
  F56 → F58 COMPLETE): lam_poly calibrated (LAM_POLY=0.05 guardrail),
  concentration penalty ON (LAM_CONC=3.58e-4, raw-cell cap 3); full
  control verdict landed: **CONTROL-FAIL** (C1 PASS — objective repaired,
  truth ranks first; C2/C3/C4 FAIL — search can't find truth) — gate
  holds, NO R5005. The side fleet's frozen control is failing (seed 184101: primary
  0.0000, secondary 0.1473 ≈ chance 0.1434; planted truth −6,959.9 vs
  annealed best +4,127.4 — the objective's optimum is at the wrong place),
  so their word bonus is imported D2-REPAIRED (longest-match dedupe,
  non-overlapping, spanning-only, per-letter), not verbatim — per their
  own repair direction (a). Their `phonetics.py` (30 classes, 42/42
  self-tests PASS) imported verbatim.

![Fig 5](report_assets/fig5_verdict_board.png)

*Fig 5 — Verdict board: attempts 1–3, crowd rounds 1–5, side fleets.*

### Sidepaths

- **sidepath (the Slider):** a pre-registered sliding-window instrument with
  frozen scorer (S=0.30·lex+0.25·cut+0.20·bound+0.25·len, ACCEPT S≥0.60,
  VOID iff real < 2× control mean), 147 windows, sidepath red-team SLA
  (kill bar ≥10× on calibrated legs; LEAD-when-in-doubt). Pass 1:
  **VOID** — 174 real accepts vs 208.3 control mean; loop stopped after
  1 of 5 passes per stop rule. The RIVAL-NOTE mechanism fired exactly once
  and correctly: top candidates "montrera" on W-S15/W-S18 require 94="re",
  emitted as forced-fail — independently replicating the main fleet's
  round-4 "re" disfavoring. Silence is data: all eight 62→94 "on ne" windows
  emitted nothing.
- **side-keyhunt:** Petit Chiffre de la Grande Armée transcribed (144
  groups, from the ARCSI reproduction of Bazeries 1901 pp. 275–277) as a
  family reference — **not the key** (0/7 anchors, anachronistic, 1–3-digit
  cells); clean negative on any published 1830s–40s French diplomatic
  syllabary (20 queries + 13 source checks, channel-caveated); and the
  **parse repair** (F32). Its table-tester harness carries a found bug
  (`crib_attack.py::qscore` nests the table under 'logp' and always returns
  the floor) and is asserted against the old parse — repair before it
  issues verdicts.
- **side-wordpattern:** 11,870-word lexicon with a custom orthographic
  syllabifier (pyphen rejected: glues mute-e; upstream-syll*.py rejected:
  annealers not syllabifiers). Pattern matcher: **honest NULL** — the
  ground-truth control fails: "première" tail @1035–1038 (four GT anchors)
  returns zero candidates at every tier; the encipherer's by-ear units
  aren't in the lexicon inventory. Polyvalence tester: gate verdict
  **VALID-WITH-RESTRICTIONS** (forward survival 0.995/0.834/0.38;
  smart-expansion inflation ≤6× vs dumb 202–2318×); the lane's red team
  flags one synthetic table as not reproducing from archived code — don't
  cite its K≥3 numbers.
- **side-homophonic:** a gating control suite — 6 synthetic instances ×
  1,846 pairs, planted keys, Les Mis plaintext, 6 polyvalent islets,
  ear-noise at/above crowd4 knobs — with pre-registered pass bars. First
  use of it as a detector-calibration: **the contactor's χ²=181.3 is a
  noisy detector** — the same pipeline on synthetic ground truth reads
  0.4–787 while the true rotation sits 181–272. The real 181.3 may itself
  be a lucky clustering. On top of it, Solver-Smith built the lane's
  joint-inference solver (`code/side-homophonic/solver/`): **simulated
  annealing over the full 96-group key** (EM would climb to the nearest
  mode of the multimodal discrete posterior; Gibbs mixes too slowly) with
  an exactly-per-move-decomposable objective (char-5-gram + spanning-only
  word bonus + contact Potts + soft priors + polyvalence penalty;
  `--self-test` proves incremental == full recompute, max err 1.7e-10).
  The pilot killed two degenerate attractors: the empty-projection exploit
  (80/89 groups → 'st') and frequent-word salad (the char-5-gram genuinely
  prefers tiled common words, −3.89/pair, over the true Les Mis decode,
  −4.44/pair — fixed by making the word bonus spanning-only). 7 pins never
  move; pre-registered gate bars proposed (PRIMARY ≥0.50, islets ≥4/6,
  best−random20 ≥200 nats, MRR ≥0.60); pilot PRIMARY was still TBD (run in
  flight) at note time. No R5005 execution — the gate stays closed.
- **side-rotation (rotation fleet):** prereg-first falsification battery for
  the column-geometry hypothesis H_col (K1 number-range, K2
  homophone-cycling, K3 clerk simulation [the hard DEAD gate], K4
  linguistic-coherence [strongest falsifier], K5 boundary-independence —
  written 16:55, before ANY executor result merged; binding rules R1–R6;
  red-team R-0 compliance). **Phonetician: NULL 6/6** (open/closed
  p=0.2500, tier p=0.3465, sonority p=0.7752, n=16; T-Pa2 p=0.0242 fails
  the pre-registered Bonferroni 0.0167; red-team independently re-derived
  all 6 to <1e-6 — R-1) — the third granularity where phases refuse
  linguistic meaning. **Rhythmicist:** WO1b labeling-robustness **FAILED
  as stated** — only 1/5 fresh-clustering variants survive (Jaccard k=16:
  chi²=354.9, z=+4.71, agree 0.948; cosine z=+0.51, k=8 z=+0.20, half1
  z=+0.28, half2 z=+0.23 all die; agreements 0.344–0.458 except k=16) —
  structure robust under one clustering, membership fragile (N30); WO3:
  **3-state HMM does NOT beat the 96-group bigram decisively** (held-out
  −4.2938 vs −4.3774/pos, bigram wins; ΔBIC=+59824.3 but the conjunction
  fails; second split −4.2356 vs −4.2638 replicates) — executor-grade;
  WO2 pre-registered tests **VOID by construction** (phase is a
  deterministic function of group; exact-repeat phrases share their start
  group — post-hoc salvage: 6 distinct formula starts all in {B,C},
  H1 p=0.0093 / H2 p=0.034 / H3 p=0.049, descriptive only, no claim);
  E1-pipeline refinement: the banked z=+5.6 reproduces on the
  ABC-restricted construction (obs=0.4219, exp=0.3505/0.3530, z=+5.6–5.8);
  the full 4-state pipeline gives z=+5.29 — significance stands, exact z
  is pipeline-dependent. **Segmenter thread-4 (executor-grade):** P2a
  momentum **SUPPORT** (after a cycle step, the cycle continues: r1=0.6327
  vs r0=0.4856, z=+4.77, one-sided p≈0 — moving-finger mechanism's
  sequential prediction holds); P2b **FALSIFIED** (2nd-order Markov no
  better than 1st-order on held-out: −1.2189 vs −1.2143/pos); P2c
  **FALSIFIED** ("one column order" — the dominant directed 3-cycle FLIPS
  across stream halves and clustering variants: halves rev/fwd, V_cos rev,
  V_half1/V_half2 rev — consistent with bedrock's labeling-relative
  ruling). **Geometer (executor-grade, pre-red-team):** WO1 number-range
  NULL (p=0.569/0.883, Cramér's V 0.14/0.09); WO2 homophone-cycling NULL
  (94 p=0.809 powered, 52 p=0.219, 06 untestable/vacuous; non-vacuous
  Fisher combined p~0.48 — the literal 3-way p=0.036 is manufactured by
  the vacuous 06 component and NOT claimed); WO3 clerk simulation 0/6
  behaviors pass the screening bars (no behavior reproduces the signature
  M1/chi²/M2z/M3/ARI; screening design per R-3, K3's joint bars untouched).
  **Label-agreement reconciled (R-4):** 69/96 best-permutation (27/96 =
  28% membership change); the naive-identity 61/96 figure retired as the
  fragility headline (overstated 2.3×). **FLEET SYNTHESIS (2026-10-07,
  coordinator verdict — red-team adjudication of the underlying executor
  results still pending): COLUMN-GEOMETRY IN ITS ARBITRARY-COLUMN FORM IS
  KILLED** (F54) — the pre-registered binding kill conditions fired on four
  independent legs: (1) WO3 generative: no clerk behavior reaches observed
  strength (best derived M1=30.8 vs 366.3; best derived z=+1.00 vs +5.61 —
  `GEOMETER-FINDINGS.md`); (2) K1 number-range: NULL — column-contiguous
  and row-major print layouts dead; (3) K2 homophone-cycling: NULL where
  powered; (4) the STRUCTURAL falsification: contact clustering can NEVER
  recover linguistically-arbitrary columns (B6 deterministic rotation
  ARI=0.000, B7 strong-soft ARI=0.043; ARI≈0 from null through
  deterministic — contact profiles are dominated by syllable linguistics),
  yet the observed phases WERE found by contact clustering — so they cannot
  be arbitrary table columns. Two sharp sub-results: a taboo-2 "don't
  reuse a column used in the last 2 steps" memory DOES make lag-3
  z≈+8-class rhythm at the process level (B3 true-col z=+8.34) while pure
  first-order rotation does not (z≈0.3–0.8) — the observed z=+5.6 would
  need ≥2nd-order memory IF columnar at all; and the 3-state HMM's EM
  recovers phase-like states unsupervised (state1: P(A)=0.719, state2:
  P(B)=0.597, state0: P(C)=0.437) — the one surviving thread. **Narrow
  surviving refuge (a DIFFERENT, weaker hypothesis):** columns = an untested
  linguistic class (e.g. onset/coda phonotactics) — testable only with key
  recovery, inherits none of the killed form's evidence. Honest statement
  of the rotation now: real (z≈+5.6, global, distributed, survives
  formula-masking), partition-dependent (Jaccard-k12/k16 only), no
  phase-free corroboration, no discourse coupling, no linguistic mapping at
  four granularities, no number structure, no homophone cycling, no
  simulable clerk process — UNEXPLAINED; a constraint on the key, not an
  explanation. Trace:
  `code/side-rotation/{FLEET-SYNTHESIS.md,prereg_falsification.md,
  geometer/{GEOMETER-FINDINGS.md,wo3_exploratory.{py,json}},
  redteam/RULINGS.md}`,
  `report_inbox/{geometer-wo1-number-range,geometer-wo2-homophone-cycling,
  geometer-wo3-clerk-simulation,rotation-fleet-synthesis-2026-10-07,
  overwatch2-status-2026-10-07}.md` (this sweep). Trace:
  `code/side-rotation/{prereg_falsification.md,prereg_{phonetician,geometer}.md,phonetician/,rhythmicist/,geometer/,redteam/RULINGS.md,redteam/agreement_reconciliation.md}`,
  `report_inbox/{phonetician-cv-structure,redteam-rotation-prereg-gate}.md`
  (this sweep); `code/crowd6/segmenter/{PREREG.md,rotation_r6.json,hmm_test.json}`.
- **bedrock (independent-verification lane):** two independent verifiers
  (separate code, no shared logic, no lane code imported) + a red-team
  adjudicator with a THIRD derivation from scratch — primary sources only
  (`upstream-ct_R5005.digits.txt`, `upstream-offsets.json`,
  `repaired_offsets.json`). **Foundation SOLID**: transcription (70
  lines, 3,764 digits), 1,847-pair parse, 96 groups, repair locality
  (exactly a5_03 1→0, all other rows byte-identical), crib positions
  @754/@1034, all windows/bigrams/trigrams (62→94 ×9, 24-87-64 ×3,
  64-96-43-87-01 ×2, 00→86 ×12 vs 00→06 ×0, 77→86 ×5, 94→82 ×4, 87-64-77-84
  @1800) — all PASS; chi²=366.3 reproduced to the decimal (df=4, p≈5e-78);
  an independent Hellinger-geometry k-means finds the 3-cycle independently
  (chi²=555.4/561.3). **Six stale counts corrected** (the lane updated
  n62/n06 after the repair but missed six — all six = the pre-repair
  1,846-parse values exactly): n64 46→**47**, n00 54→**55**, n11 44→**45**,
  n82 38→**39**, n34 10→**11**, n29 47→**45**. 13 downstream cites traced —
  **ZERO verdict flips**. Repair premise ruled **"conditionally canonical"**
  — VALID given the gloss-over-a5_03 premise, UNVERIFIABLE without
  manuscript images. **Cycle direction is labeling-relative** (independent
  cosine geometry flips the dominant direction — F11's fixed direction
  names dropped; only the 3-phase structure, suppressed self-transitions,
  and the chi² are robust). Lag-3 significance stands, decimals softened
  (z≈+5; verifier B gets 4.6–4.8 vs the lane's +5.6 on pipeline variants);
  **lag-2 z=−3.18 unchecked by any independent derivation** — flag, not
  refute. Verifiers agree on 100% of overlapping facts with zero
  disagreements — every mismatch is lane staleness, never derivation
  ambiguity. Required follow-ups banked: re-run
  `crowd4/closer64_87_results.json` and `crowd3/morphologist_results.json`
  on the repaired parse (both old-parse via `crib_attack.load_pairs`),
  pin a rank convention. Trace: `code/bedrock/{BEDROCK.md,
  verifier_a.{py,json},verifier_a_ledger.md,verifier_b.{py,json},
  verifier_b_ledger.md,redteam_adjudication.md}`,
  `report_inbox/bedrock-redteam.md` (this sweep).
- **side-homophonic (frozen control batch, run2):** prior pre-freeze batch
  VOID (inventory 288 ≠ frozen 291; removed `--chance` flag, rc=2);
  negative control OK (mean_primary=0.0412 ≈ chance 0.0216 — the dead
  annealer stays dead on the harder control). Frozen seeds:
  **184101: primary=0.0000 (0/89), proj_equiv=0.0, secondary=0.1473 ≈
  chance 0.1434, mrr=0.0262, islets 0/6, baseline margin +15050.3 nats** —
  DEAD; the frozen rerun of 184101 reproduces it EXACTLY (reproducibility
  datum); **frozen-ctl-184102: primary=0.0, proj_equiv=0.0225,
  secondary=0.1241, mrr=0.0169, islets 0/6** — DEAD; seeds 184103/184104
  still running. Diagnosis (sealed truth, control-only): **D1 objective
  misalignment** — planted truth scores −6959.9 nats under the solver's
  own objective vs annealed best +4127.4 (the true key is 11,087 nats
  WORSE than a completely wrong key — the optimizer works, the
  objective's optimum is at the wrong place); **D2 the word scorer is the
  hole** — S_ac=13,510 overlapping short-word hits on degenerate
  pseudo-French
  ("titdeemenirereiemeprendceemeniremeiiemeprendceemeetereiiimesleursquelqueemeetdtemeniremequeleurscrececemais...")
  vs ~2,500 on the true Les Mis decode (outscores real text 15× — no
  length/normalization penalty on overlapping substring hits); **D3
  polyvalence runaway** (n_poly 49–60 vs truth 6 — the penalty is dwarfed);
  **D4 inventory gap** (6/96 truth primaries absent from the 291-item
  inventory: 'vê'×2, 'té', 'né', 'vres', 'my' — true primary ceiling
  83/89=0.933). Repair list: longest-match dedupe + normalization for
  S_word, retune lambda_poly by marginal usage, extend Tier 1 with accented
  by-ear forms, re-run on FRESH seeds. Trace:
  `code/side-homophonic/runs/{RUN-REPORT.md,RUN2-BATCH.log,run2-184101/,
  run2-184102/,frozen-ctl-18410{1,2}/,frozen_batch.log}`.

### Standing methodology rules (red-team-hardened)

- **Rigid syllabification is dead as an instrument** (round 4+ rule): tuner
  NULL, calibration exclusion, encipherer ear-cutting — three independent
  kills. The ear is the primary instrument; word-space legs beat syllable
  legs for function words.
- **Instrument legality (F30):** word-space legs only; 29/82/34 excluded
  from ALL rate legs (29=er 182×, 82=m 60×, 34=i 3.3× over era — a
  morphological-syllabification calibration mismatch, not signal).
- **Kill bar:** ≥10× rate fail on a calibrated leg, a crib contradiction, a
  grammatical impossibility, or a structural break. The factor-2 band is
  uncalibrated — it may promote, never kill alone. "A wrong kill costs the
  loop a pass; a wrong lead costs nothing" (sidepath SLA).
- **Control-first gate:** no instrument touches R5005 before control
  validation (scorer-smith r2/r3 lesson); joint engine has an open R5005
  gate — it may run only when control passes.
- **Traceability:** red team recomputes from claimant JSON/code, never
  trusts .md prose (this caught its own stale-ledger error).
- **Red-team authority:** round-2/3/3b/4 rulings reviewed all promotions;
  no claim merges without its ruling.

![Fig 3](report_assets/fig3_position_map.png)

*Fig 3 — "la première" (11-70-82-34-29-40), green = ground-truth anchors,
amber = provisional, now **twice**: 0-based @754 (uncovered by the repair)
and @1034 (the lane's original @1033).*

![Fig 6](report_assets/fig6_contact_structure.png)

*Fig 6 — The 3-phase rotation on repaired phases (chi²=366.3, 4df, p≪1e-6;
1,514 ABC→ABC transitions of 1,846). Dominant cycle under the repaired
phases reads **C→A→B→C** (P: C→A 0.624, A→B 0.545, B→C 0.498; 1.60–1.71×
over independence) — the reverse of the old-parse A→C→B→A, likely a
label-permutation artifact of the Jaccard re-clustering (61/96 groups
changed phase), not a real rotation flip. Self-transitions suppressed
(0.36–0.55×); 29=er still anchors phase C. Phase clustering is fragile
while the transition structure is robust — treat rotation as a weak
transition prior, never a hard label.*

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
- **F5** — Bigram 82→16 in 11/39 (28.2%, repaired parse; 11/38 on the old)
  — strongest anchor-adjacent pattern.
- **F6 (revised)** — 87="ce": scored CONFIRMED 4/5 in attempt 2, then
  **demoted to provisional/plausible** by the red team (count-ratio
  scorecard — F13); re-validated 3/4 against era rates; crowd3 built a
  rival-elimination arc (full-vocabulary inversion: "ce" the only n>100 word
  fitting 87's {que,qui} profile in ~4,000 era words; syllabary-aware "parce"
  rate repair 0.1130 vs 0.1429 = 1.26×) but red-team-3 demoted again to
  PROVISIONAL (headline ratios don't reproduce from archived code; cela-leg
  fails era at 5–12×); round-4 register-matched subset FAILS its pre-stated
  bar (0.0398 vs 0.0418). **Final state: provisional, strengthened —
  ear-corroborated ×3 "parce que", ×5 "ce qui", ×7 "cela"; cela-leg dead;
  round-5 A1/A3 legs (F35); the lane's best-tested reading; kill authority
  held by the red team.**
  Trace: `code/attempt2.py`, `code/attempt3.py`, `code/crowd2/red_team.py`,
  `code/crowd3/closer.py`, `code/crowd3/red_team_results.json`,
  `code/crowd4/closer64_87.py`.
- **F7** — 82→16 as "ma" (16="a") not confirmed: PLAUSIBLE (1/4).
- **F8** — Erratum: "87→11 in 7/44" quoted P(87|11); correct rate
  P(11|87)=7/32=21.9%. Bedrock 2026-10-07: the P(87|11) gloss's denominator
  is the repaired n11=45 — the gloss reads "7/45".
- **F9 (revised)** — 64="qui": CONFIRMED 4/4 (attempt 3) → **DEMOTED to
  provisional** by red-team-2 (factor-2 band admits "qu'" 1.50 and "n'" 1.97
  — the band doesn't identify "qui"). Round-4 symmetric battery 6–1–1 for
  "qui" over "même" (L6: 87→64 ×5 vs era P(même|ce)=0.0159 → 9.84×,
  p=1.4e-4, conditional on 87=ce); 64="même" **disfavored, bounded not
  killed**. Re-promotion stays BLOCKED: new anomaly 64→77×3 turned out to
  be one phrase counted thrice (64-77-84 ×3 byte-identical, n_eff=1).
- **F10** — Era-matched reference corpus built (Tocqueville 1835/1840,
  214,861 words); the 6.7× "cela" register gap found.
- **F11 (revised)** — 3-phase rotational contact structure: rotation
  **re-verified on the repaired parse with recomputed phases,
  chi²=366.3** (old-parse banked phases: 181.3 — stale); bedrock
  2026-10-07 reproduces chi²=366.3 to the decimal (df=4, p≈5e-78), and an
  independent Hellinger-geometry k-means finds the 3-cycle independently
  (chi²=555.4/561.3 on 4df). **Cycle direction is labeling-relative — no
  fixed direction is cited** (the repaired-labels dominant cycle flips
  again under independent cosine geometry, and P2c falsified "one column
  order" — thread-4 F50): robust facts are the 3 phases, the dominant
  directed 3-cycle (1.60–1.71× over independence on banked labels),
  suppressed self-transitions (0.36–0.55×), and the chi². Label agreement
  banked vs old parse: **69/96 at best permutation (27/96 = 28% membership
  change)** — the naive-identity "61/96 changed" figure is retired as the
  fragility headline (overstated 2.3×; R-4). T0 verified: re-derived
  Jaccard-k12 phases match `phase_map_repaired.json` exactly (chi²=366.3
  reproduced). Linguistic mappings all killed or null (N20/N27); the live
  hypothesis is enciphering-process table geometry (F38/F50). **But phases
  are NOT word-position classes** (tuner LOO 2/34 vs unconstrained 6/34;
  0 of 4 A-phase anchors modal-medial). 29=er anchors phase C
  (word-final-ish). 87↔82 is the highest anchor-anchor Jaccard (0.423).
  Lag-3: significance stands, decimals pipeline-dependent (banked +5.6–5.8
  on the ABC-restricted pipeline; independent +4.6–4.8 on the 4-state
  pipeline); **lag-2 z=−3.18 UNVERIFIED** — unchecked by any independent
  derivation (flag, not refute). Trace: `code/crowd/contactor.py`,
  `code/crowd3/tuner.py`, `code/crowd4/phase_map_repaired.json`,
  `code/bedrock/`, `code/side-rotation/redteam/RULINGS.md`,
  `code/side-rotation/redteam/agreement_reconciliation.md`.
- **F12 (revised)** — **"la première" = 11-70-82-34-29-40 occurs TWICE:**
  0-based @754 (gloss line a5_03 — uncovered by the parse repair) and @1034
  (the lane's original @1033 on the old parse). Six consecutive
  ground-truth anchors, byte-level confirmed. The two windows are DIFFERENT
  grammatical contexts (F36): @754 a relative clause + negation matrix,
  @1034 "…c'est [03]er [80]le, la PREMIERE [17], le m[63]… la veut"; the
  "back-reference" reading is reframed as discourse-anaphoric "the first
  [one]" ("premier"/"premi-"/"pre-" occur nowhere else — no cipher
  antecedent). Chiasmus: 67→11 ("veut la") before @754 vs 11→67 ("la
  veut") after @1034.
- **F13 (revised)** — Attempt-2's "P(cela|ce)=0.278" was a count ratio, not a
  conditional; and the joint-contradiction "24-87-46 0/10 vs 87=ce"
  **DISSOLVED under era rates**: binomial P(0/10)=0.247 (was 9.1e-04 on
  Les Mis — a register artifact).
- **F14** — Repeat census: 13/16 long repeats (L≥5) are body/body;
  **no repeat is exclusive to the opening or closing 100 groups**.
  Longest: `56 69 26 00 33 21 64 37 01` ×2 @931/@1625 (old-parse positions —
  re-derive). `96 87 46` ×3 ("parce que"/"de ce que", unchecked).
  `24 87 64` ×3 ("[pour|en] ce qui"). `77 78 94 82 06` ×2 @1180/@1351
  (repaired parse; was @1179/@1350).
- **F15** — Register mismatch with Les Mis is more dangerous than era
  mismatch (first-person administrative French vs narration+dialogue+argot).
  Orthography post-1835/pre-1878 ("collége", "poëte", "asyle"); "cela":"ça"
  = 47:1 in 1835–1850 print. Syllable tiers from Meisel 1826 diplomatic
  corpus.
- **F16** — Identities: Heinrich Anton von Zeschau (1789–1870), Saxon
  finance minister / acting foreign minister; Albin Leo von Seebach
  (1811–1884), Saxon envoy in St Petersburg 1839–1852, Nesselrode's
  son-in-law.
- **F32** — **The parse repair** (previously mislabeled F17 in this report). `117082342940` twice in the digit stream
  (raw 1532, 2108); the a5_03 occurrence sits under the pencil "la
  première" gloss → pair-phase even there. Single-bit repair: EM offset
  a5_03 1→0 (`code/side-keyhunt/repaired_offsets.json`). 1,846 → **1,847
  pairs**; 25/1,847 pairs (1.4%) changed values; 3,764 digits and 96 groups
  unchanged; old positions ≥773 shift +1 (`code/crowd4/REINDEX.md`).
  Manuscript-image caveat: if the gloss line-tag a5_03 is wrong, the
  canonical revives. Trace: `code/side-keyhunt/repair_parse.py`,
  `methodology-ruling.md`, `code/crowd4/repaired_parse.py`.
- **F18** — 96="par" **CONFIRMED 4/4 → provisional** (10th value;
  conditional on 87=ce): compound P(87|96)=0.1429 vs era
  n(parce)/n(par)=0.1274 (1.12×); "parce que" frame 3/3 vs era 1.0000
  (qu-correction moved 0.3258→1.0000 — every "parce" in Tocqueville is
  followed by que/qu'); freq 1.37×; diversity 15/12. Trace:
  `code/crowd2/hypothesis_sweeper.py`.
- **F19** — 87="ce" status arc: attempt-2 CONFIRMED 4/5 → red-team demotion
  (count-ratio scorecard, F13) → attempt-3 era CONFIRMED 3/4 → crowd3
  rival-elimination → red-team-3 PROVISIONAL (archived-code ratios
  1.89×/1.98×, que-leg at band edge) → round-4 register subset FAIL
  (0.0398 vs 0.0418, cela-leg stays dead). Final state: **provisional,
  strengthened** — ear-corroboration "parce que"=96-87-46 ×3 byte-identical,
  "ce qui"=87-64 ×5, "cela"=87-11 ×7; round-5 adds the word-space "c'est"
  leg (A1: 3/958 words = 1.86× Tocqueville, in-band) and the 24→87
  ce-like-continuation leg (A3: Wilson [0.108,0.603] covers era 0.188);
  the best-tested reading.
- **F20** — 64="qui": CONFIRMED→PROVISIONAL (F9); 64="même" **disfavored**
  (bounded, not killed: L6 9.83×, p=1.43e-4, conditional on 87=ce —
  red-team-4 recomputed); re-promotion blocked; 64→77×3 is one trigram
  (64-77-84 ×3 @144/@1444/@1800, n_eff=1) — a discipline note for
  rate-arguments. Trace: `code/crowd4/closer64_87.py`,
  `code/crowd4/red_team_rulings.json`.
- **F21** — 94="ne" **provisional-strong** (rebuilt legs; old ones VOID per
  F30): host odds 2.27:1 (641 "nement"-hosts vs 282 "rement", disjoint —
  'gouvernement' is 475/641=74%); compositional frames ne 8/3 vs en 4/2 vs
  re 0/0 (35-94-52-80-04 ×2 byte-identical @1292/@1805 "ne pas [inf]";
  82-94-76 ×2 @650/@1574 + 82-94-74 @1100 "m'en"); P(94|62)=8/34=0.2353 =
  1.99× era P(ne|on) vs 15× P(en|on). 94="re" **disfavored** (old legs were
  rigid-syllabifier artifacts — the instrument was the rival; fenced on
  @578's unidentified trigram host). 94="en" survives as **conditioned
  islets** ("en" iff pre=82 "m'en" ×3 or suc=87 "en ce" ×1 — 4/4; "ne"
  everywhere else). @1741 unparsed under all three (true anomaly, 25% of
  the 94→82 family). 06="ent" **REFUTED as general**, restricted-plausible
  only on the three -ment trigrams (94-82-06 ×3 at 1.054× era). Trace:
  `code/crowd3/morphologist_results.json`,
  `code/crowd4/morph94_re_battery.json`, `code/crowd4/battery4.py`.
- **F22** — 06 = **verb-stem CLASS (provisional)**; the specific stem is NOT
  identified (06-verb ≈13.6/1000 vs era "demand*" 0.20/1000 — 66× gap).
  **New structure: 06 = finite/imperative stem, 86 = infinitive-complement
  stem** (00→86 ×12 vs 00→06 ×0; 06→{11,00} ×8 vs 86 ×0; the 06/86
  complementary distribution). 06="ne" REFUTED (P(77|06)=0.1304 vs era
  "ne pas" adjacency 0.0063 → 20.6×; 06→29(er) 5× vs era exactly 0).
  06's follower set reads as a verb stem (77 "pas" ×6, 29=er ×5 infinitive,
  11=la ×4 object, 30 distinct predecessors). Trace:
  `code/crowd2/hypothesis_sweeper.py`, `code/crowd4/stem47_06_final.py`.
- **F23** — **Conditioned polyvalence ledger** (red-team-4 adjudication):
  **4/25 identified groups (16.0%)** carry ≥2 live readings (06, 52, 94, 78), each with a
  verified conditioning rule** — 06: "ent" iff trigram-internal
  (06@[580,1183,1354] inside 94-82-06) vs verb-stem elsewhere (43/46);
  52: "pas" iff negation-frame (94_52 ×3 @571/1293/1806 + 94_70_52 @1331)
  vs "so" word-internal @160; 94: "ne" iff negation-frame (10/36) or
  word-internal (@161) vs "en" islets (note F21); 78: "me"-syllable vs
  "ver" conditioned islet (iff next=94; n_eff=1). **Zero free polyvalence.**
  Two nulls disagree honestly: kill-rate κ=12/37≈0.324 → P(all 6 extra
  readings survive | monovalent)≈0.095 (count alone does NOT reject the
  misreading null); direction null **rejects ear-cutting-alone** (15/16
  repeated-word instances byte-stable; doubles run 1 group→N sounds — the
  wrong direction for the encipherer's own allophonic noise). Key
  identification at 35.2% token coverage (8.4% in polyvalent groups).
  Falsifiers banked: a double with no statable rule, a re-segmentation
  dissolving a double, the @578 thread reviving "re". Trace:
  `code/crowd4/red_team_rulings.json`.
- **F24** — 47="ce" **LEAD** (polyvalent with 87): "me"-as-word KILLED
  ("par me" era n=0 — hard zero); B1 "ce que" **3/28=0.1071 vs era
  122/1134=0.1076 → 1.00× exact**; C1 "par ce" 2.85× (era n=13); 47→11 ×3
  reads "cela" (parallel to 87→11 ×7); @150–152 = 96-47-46 = "par ce que"
  (era n=13) — the jar's slot resolved; residual = verbless
  "ce qui __ par ce que" (64's problem). 47→78 ×5 joints force fragments
  ("ce"+"me" ungrammatical). Trace:
  `code/crowd4/stem47_06_final.py`, `code/crowd4/stem47_06_results.json`.
- **F25** — Formulas: **24→87→64 as a formula ×3** (24→87 = 10 of 32 "ce"
  predecessors, 31%; rank(24)=2 — the money was *before* "ce", not after
  "qui"; promoted as formula, no value for 24); 64-77-84 ×3 byte-identical
  (n_eff=1); 64 96 43 87 01 ×2 ("qui … ce"); "parce que"=96-87-46 ×3,
  "ce qui"=87-64 ×5, "cela"=87-11 ×7. Trace:
  `code/crowd2/context_miner.py`, `code/crowd4/closer64_87.py`.
- **F26** — Cipher model: **the encipherer spells by ear and cuts
  inconsistently** — "personne" as per|so|nne (93 52 94 @160) AND
  pers|on|ne (77 62 94 @508); "prend"→"pre" (silent d dropped, "pre"
  written by 70); "première"→pre|m|i|er|e (mute -e WRITTEN as 40 — the
  one-line kill of whole mute-e-unwritten edifices); **final "-er"
  systematically stripped** (corpus P(standalone "er")=0.0020 vs cipher
  0.0255, 13×; but P(unit ENDS in "er")=0.0211 ≈ cipher — parl|er).
  R1–R4 syllabary rules banked in `code/crowd4/syllabary4.py` (cells 1–4
  letters; ear-cuts; mute -e written by default; morphological endings are
  cells). Phonetic rules for the Slider: 11 rules (6 SOLID, 4 PROVISIONAL,
  1 SPECULATIVE) + an 11-item FORBIDDEN list
  (`code/sidepath/phonetic_rules.md`). Trace:
  `code/crowd3/frenchman_results.json`, `code/crowd2/scorer_smith_results.json`.
- **F27** — Key-hunt: Petit Chiffre de la Grande Armée transcribed (144
  groups, from the ARCSI reproduction of Bazeries 1901 pp. 275–277) —
  family reference, **not the key** (0/7 anchors; 11 absent; 70→ei, 82→es,
  34→at, 29→bi, 40→co, 46→1); clean negative on any published 1830s–40s
  French diplomatic syllabary (20 queries + 13 source checks — channel-
  caveated, Gallica/Hathi/archive.org variously blocked from the VM).
  Structural prior: ~100-cell petit-chiffre tier, sparse homophones
  (~10–20% of cells), no nulls. The 1690 royal mandate required
  homophones for high-frequency letters (mandated, not optional);
  null-free matches the upstream stream (no nulls detected); word-family
  packing in the table (e.g. gouvernement-adjacent cells) is consistent
  with the 06/86 allomorph reading (F33). Trace:
  `code/side-keyhunt/tables/petit-chiffre-grande-armee.json`,
  `code/side-keyhunt/search-log.md`, `code/side-keyhunt/verdict-petit-chiffre.md`.
- **F28** — DECODE access outcome: operator registered `alexrivers`
  (activation link clicked by the operator); **login succeeds but every
  full-size page image returns "Insufficient permissions to so see the full
  image"** — records still "Access mode: Authentication required" +
  "Private Ciphertext: True". Fresh accounts need admin elevation (or a
  provisioning delay — one retry warranted). The "DECODE unlocks R5006–
  R5008" plan is a null, not a blocker change. Trace:
  `report_inbox/processed/decode-access-2026-10-07.md` (this sweep).
- **F29 (instrument legality)** — Rate legs may only run in word-space;
  29/82/34 excluded from ALL rate legs (era-vs-cipher anchor calibration:
  29=er 182×, 82=m 60×, 34=i 3.3× over era — morphological syllabification
  mismatch, not signal; only 11/46/40/70 usable). Trace:
  `code/crowd3/bigram_closer_results.json`, `code/crowd3/red_team_results.json`.

### Round-5 addenda (2026-10-07, post-sweep batch)

- **F31** — 77="le" **PROMOTED LEAD → provisional (CONDITIONED)** — the
  lane's first promotion in five rounds. Legs (audit-verified): 77→86 ×5
  @430/798/877/950/1133 (1.15× recomputed — supersedes the worker note's
  1.02×, minor traceability flag); 86→29 @431 confirms the "le"+stem+"er"
  frame; diversity 20 followers/22 predecessors (structural); unigram
  1.152×. Adverses fenced: "ce le"×2 @515/@869 (on 87=ce-prov); "le
  me"×7 conditional on 78="me"-syllable; 4.07× rate overshoot reported
  (band uncalibrated). Caveat: 77="gou" word-internally @1180/@1351 →
  promotion CONDITIONED, the gou exception fenced (n_eff=1). Trace:
  `code/crowd5/redteam/rulings.md` Ruling 2,
  `code/crowd5/bigram78_77_578.{py,md,json}`, `audit_bigram78_77_578.py`.
- **F33** — M1: **06/86 complementary-distribution rule ACCEPTED**
  (F33-grade; allomorph = working hypothesis). 00→86 ×12 vs 00→06 ×0;
  Fisher 7.278e-06; binomial 6.292e-11; enrichment 12.59×; three
  falsifiers all zero (@889 86→06 fenced as clause-boundary). Tensions
  fenced: rate 79.4/1000w family vs ~40 era max; "donner et donner". Trace:
  `code/crowd5/morph47_06_results.json`, `audit_morph47_06.py`.
- **F34** — 47="ce" **strengthened LEAD** (promotion blocked): Q1
  qui/que complementarity (47→64=0/28, p=0.0029; Fisher one-sided 0.0476 —
  borderline, thin) + Q2 fragment rule (fragment iff suc==78 or pre==29;
  9/9; fragment sound unidentified) as F33-form conditions; **C2
  DISSOLVED** (the 12.6× was F29-void); unigram corrected 2.13
  (elision-corrected) / 1.446 (ce-proper) — the note's 4.11×/2.79× do NOT
  reproduce from JSON (traceability flag). Promotion blocked on @148–152
  (unresolved; ranked unblockers: 96 conditioned-verb battery, fragment
  sound, diplomatic corpus). Trace:
  `code/crowd5/morph47_06_results.json`.
- **F35** — 87=ce new legs (HOLD provisional-strengthened): **A1 "c'est"
  word-space** (87→01 ×2 + 47→01 ×1 = 3/958 words = 1.86× Tocqueville,
  0.90× Les Mis — in-band on both, joint with the 01="est" medium lead;
  n=3); **A3 24→87 ce-like continuations** (11×3 and 64×3; P(64|24-87)=0.3,
  Wilson [0.108,0.603] covers era 0.188; 24-87-46=0 re-verified —
  "whatever 24 is, 87 behaves exactly like 'ce' after it"); **A2 47≠87's
  "ce"** (Jaccard(87,47)=0.435 but P(64|47)=0/28 vs era 0.188, binom
  p=0.0030 — bounds 47 as the same reading). 84 bounded: 84="fait" KILLED
  on unigram (6.7×); thread refined to 64-77-84-59 ×2 (n_eff=1). Trace:
  `report_inbox/processed/closer-87-new-angles.md` (this sweep).
- **F36** — @754 vs @1034 window comparison (§7 step 10 DONE): DIFFERENT
  grammatical contexts, not formulaic repetition — @754: relative clause
  + negation matrix ("…qui [02-97-e] veut la PREMIERE [20], on ne
  [59]…"), fresh "on ne" @761-762 (9th of 9 on the repaired parse,
  P(94|62)=0.257 vs era 0.120); @1034: "…c'est [03]er [80]le, la PREMIERE
  [17], le m[63]… la veut" ("c'est" @1028-1029 feeds A1; unique "la
  veut" @1044-1045 supports 67="veut"). **Chiasmus:** 67→11 ("veut la")
  BEFORE @754 vs 11→67 ("la veut") AFTER @1034. F12 reframed:
  "premier"/"premi-"/"pre-" occur nowhere else → discourse-anaphoric "the
  first [one]", not back-reference. **43="me" BROKEN at @1034:** 96→43
  ×2 both inside 64-96-43-87-01; "par me" era-dead (n=0) → fenced
  (conditioned polyvalence iff pre≠96, or 43≠"me"). Leads: follow 59 for
  the 62 battery; pin 67="veut"; adjudicate 43 (fence pre=96); 17="fois"
  @1040 stays WEAK. Trace:
  `report_inbox/processed/closer-window754-1034.md` (this sweep).
- **F37** — Unit inventory: the lane's consolidated reference —
  **24 units in 4 tiers** (7 crib-PROVEN, 10 lane-inferred
  status-marked, 3→4 conditioned islets, R1–R4 cutting rules) + **10
  exclusions**; bare-consonant "m" phonotactically impossible in French but
  GT-proven; 29=er 2.44% vs era 0.038%; 35.2% token coverage. (Staleness
  caveat: the inventory's "3 islets" was written before 78 joined —
  F23 now counts 4.) Trace:
  `code/crowd5/unit_inventory.{py,md,json}`.
- **F38** — Rotation E1 (post-hoc, hypothesis not verdict): **period-3
  sequential rhythm** — P(same phase at lag 3)=0.4219 vs 0.3530
  Markov-expected (z=+5.6, p≈1e-8); lag-2 z=−3.18 BELOW expectation;
  persists under old-parse labeling (z=+3.27) and after masking all 157
  formula positions (0.4218). Leading hypothesis: enciphering-process
  geometry — a soft column-rotation through a multi-column syllabary table
  — which predicts the whole package (real rotation, fragile cluster
  assignment, linguistically arbitrary phases, tail-distributed signal).
  Trace: `code/crowd5/rotation_mystery.md` (pre-registered),
  `code/crowd5/segmenter-rotation.md` (inbox).
- **F39** — Round-5 red-team adjudications: 3 claims ruled — 62="on"
  DENIED → fenced-lead (instrument contamination; χ² misreported; recycled
  datum), bigram-closer WO1/WO2/WO3 adjudicated (1 promotion, 2 accepts),
  morphologist WO1 strengthened/WO2 null/WO3 accepted; kill ledger:
  promotions 1, demotions 0, kills 0, fenced 1. Armed baseline 29/29 checks
  PASS on the repaired 1,847-pair stream. Trace:
  `code/crowd5/redteam/rulings.json`, `verify_baseline.py`.
  *(The docket note is stale — its "zero rulings" text was written before
  the rulings; `rulings.md` also still carries the old docket-status prose
  under the new rulings — doc-hygiene flag for the coordinator.)*
- **F40** — @507 NULL reframed (micro-finding): the @507 77-62-94 NULL is
  **not a 77-datum** (explained by per|son|ne vs pers|on|ne cutting);
  cela+X NULLs = non-evidence. Trace:
  `code/side-wordpattern/redteam/ADJUDICATION.md`.

### Round-6 addenda (2026-10-07, this sweep)

- **F41** — **Bedrock foundation audit** (ground-truth-grade for the
  mechanical facts; value assignments remain manuscript/inference):
  two independent verifiers + a third from-scratch red-team derivation
  confirm the parse (1,847 pairs, 70 lines, 3,764 digits), the repair
  locality (exactly a5_03 1→0), crib positions @754/@1034, all
  windows/bigrams/trigrams, and chi²=366.3 to the decimal. **Six stale
  counts corrected**: n64 46→47, n00 54→55, n11 44→45, n82 38→39,
  n34 10→11, n29 47→45 (all six = the pre-repair 1,846-parse values —
  the lane updated n62/n06 post-repair but missed these; all six deltas
  confined to row a5_03). 13 downstream cites traced, **ZERO verdict
  flips**. Repair premise ruled **"conditionally canonical"** (VALID given
  the gloss-over-a5_03 premise, UNVERIFIABLE without manuscript images).
  Banked follow-ups: re-run `crowd4/closer64_87_results.json` and
  `crowd3/morphologist_results.json` on the repaired parse (both old-parse
  via `crib_attack.load_pairs`); pin a rank convention. Trace:
  `code/bedrock/{BEDROCK.md,verifier_a.{py,json},verifier_a_ledger.md,
  verifier_b.{py,json},verifier_b_ledger.md,redteam_adjudication.md}`,
  `code/bedrock/report_inbox/bedrock-redteam.md`.
- **F42** — **French petit-chiffre doctrine** (context, not a claim):
  the 1690 royal order *mandated* homophone use ("not always repeat the
  same cipher character") — F33's conditioned polyvalence is expected
  design, not anomaly; "free" polyvalence would violate the doctrine,
  independently supporting conditioned-not-free. Word-family packing (one
  group = stem + listed completions, e.g. petit-chiffre 39→
  al/Allemagne/aland/als/ales) explains the 06/86 complementary
  distribution as stem allomorphs and predicts some unidentified groups
  are family completions of held groups. R5005's 96-of-100 groups = the
  petit-chiffre tier (~100-cell routine class): design grammar for
  sanity-checking reconstructions — ≈100 cells, 10–20% homophone budget,
  no nulls, two-part tables. Caveats: Kahn via unofficial full text
  (verify against print); the petit-chiffre table is Napoleonic family
  reference (ruled out 0/7 as the key), not the 1841 table; no published
  1830–1848 French diplomatic table exists (clean negative).
  Trace: `data/historical-context/french-petit-chiffre-doctrine.md`,
  `report_inbox/doctrine-writeup-2026-10-07.md`.
- **F43** — **Label-agreement reconciliation (R-4, ground-truth-grade):**
  69/96 best-permutation agreement = **27/96 = 28% membership change** —
  the correct clustering-agreement number; the naive-identity 61/96
  "change" figure is arithmetically right but methodologically misleading
  (it counts the A→C→B→A vs A→B→C→A label-permutation flip as change) and
  is retired as the fragility headline. Fragility is real (28% ≫ the ~0%
  a stable clustering would show) but the naive figure overstated it
  2.3×. Inconsistencies across NOTES.md/rotation_mystery.md/
  unit_inventory/homophonic_synergy.md/scorer_identifiability.md/
  crowd5-redteam rulings should be corrected to the best-permutation
  figure. Trace:
  `code/side-rotation/redteam/agreement_reconciliation.md`.
- **F44** — **59="est" STRONG LEAD (executor-grade, red-team REVIEWED —
  F26-17: held at STRONG LEAD, promotion to provisional DENIED):**
  the unique rate-survivor for 84's top follower (1.39×); "qui est" ✓;
  "n'est" at era P=0.238 (n=324); "on n'est" ✓; "c'est" @824. Fenced
  adverse: 59→37 ×6 reads 6.47× over era, conditional on 37="le"
  [MEDIUM]. Interacts with the 01="est" lead (/ɛ/→{01,59} allophony vs
  01≠"est"; touches A1's "c'est" count) — a red-team call. Compatible with
  the bigram closer's 59="verb" [LEAD] — "est" is the specific form.
  Trace: `code/crowd6/closer/closer87_00_results.json`,
  `code/crowd6/closer/closer87_00.md`,
  `code/crowd6/report_inbox/closer-87ce-00pour.md`.
- **F45** — **00="pour" STRONG LEAD (executor-grade, red-team REVIEWED —
  F26-17 upheld; 00="le"×3 LEAD tensions it — F60):**
  the M1 governor frame (00→86 ×12 "pour [inf]" vs 00→06 ×0) + conditional
  rates + a full rival sweep (à/de/en/par/dans/sur/avec/avant/afin/pendant/
  sans/après/et all killed) all pass; promotion blocked on rates (unigram
  6.22× over era, "pour que" 3.85×). Needs the diplomatic corpus for the
  B1/B3 residuals. Trace: `code/crowd6/closer/closer87_00_results.json`,
  `code/crowd6/closer/closer87_00b.py`.
- **F46** — **84: unresolved executor conflict** — closer: 84="en" LEAD
  (sole survivor; E1 unigram 1.10×, E2 "qu'en" 1.36× on GT 46=que, E3
  "n'en" common, E5 "m'en" on GT 82=m; 24/25 windows read cleanly;
  promotion BLOCKED on "l'en" 141×/63× over era) vs bigram closer:
  84=masculine-NOUN LEAD-grade (identity NULL — honest, register-robust;
  "le 84" ×7, "la 84" ×1, "que 84 24" ×2, "que le 84 24" ×1; "fait"
  re-killed 6.75×, "gouvernement" 6.12×). Crux: noun fails "ne 84"/"m' 84"/
  "que 84" (grammatical zeros, n=1/1/2); "en" fails the "l'en" rate (141×,
  n=7). Untested resolution flagged for round 7: conditioned polyvalence
  (84="en" iff pre∈{46,94,82}, 84=noun iff pre∈{77,11}); 9/25 predecessors
  unclassified — a battery, not adjudication. NOTE: the two notes' 84
  counts cross-check (84→59 ×4; 59→46 ×2; 59→37 ×6). Trace:
  `code/crowd6/closer/closer87_00_results.json`,
  `code/crowd6/bigram_closer/closer6{,_era,_quesub}.json`,
  `code/crowd6/report_inbox/{closer-87ce-00pour,bigram-closer-77le}.md`.
- **F47** — **78-45="même" LEAD (executor-grade, red-team REVIEWED —
  F26-17 upheld):**
  0.57× in-band with era locks ("le même" 87×, "même qui" 11×); @313 =
  "le même qui" — a grammatical lock under 37="le" [MEDIUM]. The
  "même"=me|me reading implies 45/78 homophony for one syllable
  (F23-consistent, untested beyond the bigram). 45="me"-word
  disfavored-strong (unigram 9.14× out; "par me" ×2 era-0; "me qui" ×3
  era-0 fenced on 64="qui") — kill-shaped but fenced, not refuted. Trace:
  `code/crowd6/bigram_closer/closer6.json`,
  `code/crowd6/report_inbox/bigram-closer-77le.md`.
- **F48** — **67 et/veut fork: conditioned polyvalence SUPPORTED
  (executor-grade, red-team REVIEWED — F26-17 upheld), NOT promoted:** 19/38 classified
  with ZERO cross-contamination (F33-form: positional, falsifiable) —
  et-side 8 ("veut" killed in all 8: 67→64 ×2 "veut qui" impossible,
  06-29-67 ×2 "[inf] veut [inf]" impossible, pre∈{06,86} ×4 verb-verb
  kills "veut"; fork ratio re-derived 113.0) vs veut-side 11 ("et" killed
  grammatically in all 11; "veut" survives: "veut me [inf]" ✓, "la veut"
  ✓, era attestation thin n=52); 19/38 still open. "la veut" @1044–1045
  pins 67@1045 as a 3sg transitive verb (kills "et" there) — NOT uniquely
  "veut". 7/11 veut-frames rest on the pre=21 condition with a
  grammatical strain under the 21="me" lead ("me veut me" @1841 is broken)
  — this tensions 21's value, flagged not resolved. **43="me" DOWNGRADED
  MEDIUM→WEAK** ("par 43"×2 n_eff=1, era "par me"=0 — grammatical adverse;
  adverses outweigh supports; kill rule n≥3 not met). Trace:
  `code/crowd6/morphologist/battery96_67_results.json`,
  `code/crowd6/report_inbox/morphologist-96-67.md`.
- **F49** — **Side-rotation prereg-first gate (methodology finding):**
  the hypothesis-level falsification battery (K1–K5 with kill/strengthen
  thresholds + binding rules R1–R6) was written 16:55, BEFORE any executor
  result merged — prereg-first satisfied (R-0). The Phonetician's own
  pre-registered Bonferroni bar killed its T-Pa2 near-miss (p=0.0242 <
  0.05 but > 0.0167) before any red-team intervention — the bar did its
  job exactly as designed (R-1). Rhythmicist prereg PASS with a required
  R3 amendment (WO2 Test A must use an exact test — asymptotic chi² VOID
  at expected 4.68/4.29/3.67/1.36); Geometer prereg PASS with calibration
  notes (WO3 bars are screening-level, not K3-kill-level). Trace:
  `code/side-rotation/prereg_falsification.md`,
  `code/side-rotation/redteam/RULINGS.md`,
  `code/side-rotation/report_inbox/redteam-rotation-prereg-gate.md`.
- **F50** — **Segmenter thread-4 column-geometry probes (executor-grade,
  red-team REVIEWED — F26-17 upheld; P2c conflict resolved in favor of
  the rotation fleet, F54):** P2a momentum **SUPPORT** (on ABC-only triples:
  r1=P(continue cycle | prior step was a cycle step)=0.6327 (n=765) vs
  r0=0.4856 (n=383), one-sided two-proportion z=+4.77, p≈0 — the
  moving-finger sequential mechanism's concrete prediction holds);
  P2b **FALSIFIED** (held-out order selection: 2nd-order Markov
  −1.2189/pos vs 1st-order −1.2143/pos — no genuine memory-2); P2c
  **FALSIFIED** ("fixed column order": the dominant directed 3-cycle
  reads fwd in halves+variants selectively and rev in V_cos/V_half1/
  V_half2 — one global column order is dead, consistent with bedrock's
  labeling-relative ruling). Honest scope: these probe the SEQUENTIAL
  mechanism only; they cannot confirm table columns without key recovery.
  Trace: `code/crowd6/segmenter/{PREREG.md,rotation_r6.json,hmm_test.json}`.
- **F51** — **Scorer-smith identifiability FINAL (round 5, work order 7):**
  N30's "model-correct" framing is refuted — the joint engine's objective
  ranks truth ~30 nats below its own fluent nonsense. Route (a) better
  search: baseline 3×600 sweeps best −2.59..−2.81 / top1 0.00–0.10;
  parallel tempering (6 chains × 600) gbest −2.88 / top1 0.05; pool-copy +
  Gibbs proposals best −2.66..−3.05 / top1 0.00–0.10; islets 0/3
  everywhere — no variant beats the best baseline restart; **search is not
  the bottleneck**. Basin test: 9 descents (3 per k) walk AWAY from truth
  (ends −2.47..−2.90) — no basin around truth. Route (b) shrink space: b1
  (12 hard pins, 3 islets fixed, 301-cell inventory) reaches best
  −33.54..−33.56 vs the truth ceiling −33.43 (**within 0.13 nats** — the
  search DOES reach truth's neighborhood once the space is shrunk;
  top1 0.35–0.40 = 4× baseline, islets 1/3); b2 (conditioned polyvalence)
  0/15 verify, 0/3 islets — honest negative (control islets are
  unconditioned coins; documents a control-vs-reality gap); b3 (small
  inventory alone) top1 0.05 — no better. Model bugs (both load-bearing):
  (1) **lam_poly=10 is ~100× over scale** — truth beats the annealed best
  only at lam_poly < 0.09; at 10 the v2 machinery is dead by construction;
  (2) the raw-letter 7-gram alone prefers the annealed key (−3.11/letter)
  over truth (−3.64/letter); the E-step recovers only 42/63 of the truth's
  islet emissions. Control-design findings: 2/20 bar groups unidentifiable
  BY CONSTRUCTION (max achievable top1 = 0.90 — the control validates
  machinery, not the unit set; only 23/89 truth primaries are in the
  24-unit crib-derived set). Traceability flag: the .md's basin
  denominators ("3/105: 1/15, 2/30, 0/60") do NOT reproduce from the
  archived JSON (9 descents: 1/3, 2/3, 0/3; the .md's own line "all 9
  descents" agrees with the JSON) — numerators match, denominators flagged.
  Trace: `code/crowd5/{scorer_identifiability.py,scorer_identifiability.md,
  scorer_identifiability.json}`,
  `code/crowd5/report_inbox/scorer-smith-identifiability-final.md`.
- **F52** — **Side-homophonic frozen-control diagnosis D1–D4
  (control-only, never R5005):** D1 — objective misalignment: planted
  truth −6959.9 nats vs annealed best +4127.4 (true key 11,087 nats WORSE
  than a completely wrong key — optimizer works, objective's optimum is
  at the wrong place); D2 — the word scorer is the hole: Aho-Corasick
  counts thousands of OVERLAPPING short-word hits on degenerate
  repetition-garbage (S_ac=13,510) vs ~2,500 on the true Les Mis decode
  (outscores real text 15× — S_word has no length/normalization penalty);
  D3 — polyvalence runaway (n_poly 49–60 invented vs truth 6 — the
  penalty is dwarfed); D4 — inventory gap (6/96 truth primaries absent
  from the 291-item inventory: 'vê'×2, 'té', 'né', 'vres', 'my' — true
  primary ceiling 83/89=0.933). The side fleet independently found the
  same disease the main fleet's scorer-smith found (pilot: salad
  −3.89/pair beats truth −4.44/pair). Repair list: dedupe overlapping
  hits (longest-match), normalize S_word by stream length or gate on
  match length, retune lambda_poly by marginal usage, extend Tier 1 with
  accented by-ear forms, re-run on FRESH seeds per the freeze protocol.
  Trace: `code/side-homophonic/runs/{RUN-REPORT.md,RUN2-BATCH.log,
  run2-184101/control_report.json,frozen-ctl-18410{1,2}/control_report.json,
  frozen_batch.log}`.
- **F53** — **62="on" non-ear battery (round 6):** NO PROMOTION — stays
  STRONG LEAD (fenced); honest null (N25). On clean disjoint pieces the
  three-way likelihood is on≈il (joint −26.54 vs −26.82, Δ=+0.27 nats;
  "qui" −32.77 weakly disfavored −6.2); the unigram favors "il" +9.4 nats
  (granularity-hedged, already known). The H-split calibration (46 writes
  /k/ before vowel-initial 29=er ×2, never before /i//e/) **voids both**
  N35's "il"-differential (p=0.041) and the merger corroboration; under
  H-split, 46→62=0/29 is ADVERSE to "on" (E=7.18, p=2.6e-4 — single,
  four-ways caveated, adverse not kill-grade). The profile route is proven
  unbridgeable with the current inventory (no 62 cell is BOTH mappable AND
  discriminative with n≫2; all grammatical-asymmetry sub-routes blocked).
  Ranked unblockers: hunt the "qu'on" whole-word cell; identify the
  l'-cell ("l'on" test, era P=0.0619 vs 0); identify an impersonal-verb
  cell; identify 48/98/16. Enlightenment: the "qu'on"-merger was the
  by-ear model's "genuine predicted zero" — but the cipher's own habit
  (46-29 ×2, 87-01 ×2: monosyllabic /k/+V, /s/+V → two groups) points to
  over-splitting, not merging; merger premises need cipher-internal
  calibration, never phonetic assertion. Trace:
  `code/crowd6/frenchman62/{battery62.py,battery62_results.json,
  frenchman62_round6.md}`, `code/crowd6/report_inbox/frenchman-62-non-ear.md`.
- **F54** — **Column-geometry hypothesis (arbitrary-column form) KILLED
  — rotation-fleet synthesis 2026-10-07.** Four independent legs fired the
  pre-registered binding kill conditions: (1) **WO3 generative**: 8 clerk
  behaviors × 20 replicates, toy 3-column table (~90 groups), lane's own
  Jaccard-k12 pipeline on every simulated stream — NO behavior reaches
  observed strength (best derived M1=30.8 vs 366.3; best derived z=+1.00
  vs +5.61; `GEOMETER-FINDINGS.md` table, `wo3_exploratory.json` B6/B7
  post-hoc); (2) **K1 number-range**: NULL (p=0.569/0.883, V≤0.14, runs
  p=0.76 — column-contiguous and row-major layouts dead); (3) **K2
  homophone-cycling**: NULL where powered (94 p=0.809, 52 p=0.219); (4)
  **structural falsification**: contact clustering NEVER recovers
  linguistically-arbitrary columns (ARI=0.000 deterministic, 0.043
  strong-soft — contact profiles are dominated by syllable linguistics),
  yet the observed phases WERE found by contact clustering — so they
  cannot be arbitrary table columns. Sharp sub-results: taboo-2 memory
  (B3 true-col z=+8.34) is the only mechanism generating lag-3-class
  rhythm (pure first-order rotation: z≈0.3–0.8); the 3-state HMM's EM
  recovers phase-like states unsupervised (state1: P(A)=0.719, state2:
  P(B)=0.597, state0: P(C)=0.437). The period-3 rhythm itself (F38)
  stands: real, global, distributed, survives formula-masking, but
  partition-dependent (Jaccard-k12/k16 only), phase-free-null, UNEXPLAINED
  — a constraint on the key, not an explanation. **Narrow refuge** (a
  different, weaker hypothesis): columns = an untested linguistic class
  (e.g. onset/coda phonotactics) — testable only with key recovery,
  inherits none of the killed form's evidence. Caveats: toy simulation
  (45-syllable inventory, random columns, crude syllabifier); ARI≈0 is a
  toy result, not a theorem; the verdict is the FLEET COORDINATOR's —
  red-team adjudication of the underlying executor results is still
  pending (0/7 dockets), and the geometer's own note requests red-team
  re-derivation of WO3 (seeds archived). Two synthesis-only claims could
  NOT be traced to result files and are flagged claimed-not-verified:
  "block structure 366.3 vs max 63.3 over 2,000 label permutations" and
  "group lag-3 z=+0.15" — do not cite. Trace:
  `code/side-rotation/{FLEET-SYNTHESIS.md,prereg_falsification.md,
  geometer/{wo1.json,wo2.json,wo3.json,wo3_exploratory.json,GEOMETER-FINDINGS.md},
  redteam/RULINGS.md}`,
  `report_inbox/{rotation-fleet-synthesis-2026-10-07,
  geometer-wo1-number-range,geometer-wo2-homophone-cycling,
  geometer-wo3-clerk-simulation}.md` (this sweep).
- **F55** — **Inventorist pattern re-drive (round 6, executor-grade,
  pending red-team):** the word-pattern matcher re-driven on the round-5
  24-unit inventory (F37 — the note's "F44" is its own stale numbering),
  replacing the standard-French syllabification that killed the old
  instrument. **CONTROL PASSES — the alphabet is repaired** (the
  ground-truth control that killed the old version now works): C1 (full
  "première" [70,82,34,29,40], 5 GT anchors): "première" top-1
  (2 candidates: première, premières); C2 (tail [82,34,29,40] = m|i|er|e,
  4 GT anchors — the old zero): **"première" top-1** (5 candidates:
  première, lumières, premières, lumière, chaumière) — the old
  instrument's zero is repaired; C3 (specificity: contradictory GT anchor
  [11,34,29,40]): 0 candidates, "première" correctly excluded — the
  instrument is anchor-driven. **Proposals (2, NOT promoted — await
  red-team ruling):** (1) **"parmi" @1196–1198 [96,82,16]** — NEW:
  unique T3 survivor (only by-ear [par,m,?] in 11,870 words), era freq
  174, whole-word by-ear match [par,m,i] top-1 tiling score 9.0, 1 GT
  anchor (82=m) + 1 PROV-STRONG (96=par, CONFIRMED 4/4). Entails
  **16="i"** (n=1, new claim — 34=i is GT, so a second 'i' group, parallel
  to 87/47 for "ce"): 82→16 ×11 (29% of 82's followers) reads m|i, and
  16's top predecessor is 82=m. Needs its own battery — NOT established.
  (2) **"cela" @269–270 and @357–358 [47,11]** — 47→11 ×3 corpus-wide
  (@269/@357/@498), era freq 47, whole-word [ce,la]; anchors 47=ce
  (LEAD) + 11=la (GT). A **47="ce" corroboration**, not a new crib (the
  lane already banks 47→11 "cela"). Leads not proposed (<2 checks):
  "seulement" @1041/@1158 (freq 136, fragment "lement", 108 T3
  candidates), "donner" (freq 82, 0 GT anchors), "acquière" (hapax,
  Class-B shape), "ensemble", "général", "comparer", "confédération",
  "nationale", "circonstances", "établissements", "semble", "raison",
  "cinquième", "acquièrent". **Recommended KILL (register pollution,
  executor recommendation — NOT a red-team kill):** "meeting" ×2
  (@352/@819, English, freq 2), "maryland" (@376, US state, freq 11),
  "chancelantes" ×2 (@200/@1242, freq 2). Instrument numbers: by-ear
  tiler `byear.py` (20-string inventory, 1–4-letter cells, top-8 tilings;
  calibration: "première"→[pre,m,i,er,e] top-1, "cela"→[ce,la] top-1,
  "lumière"→[lu,m,i,er,e] rank 3 — limitation: unattested multi-letter
  cells like per/pers not generated); subsequence pattern index
  `build_index.py`: **846,748 subsequences, 7,297 keys**, smart
  polyvalence expansion only (3,451 extra filings vs 202×–2318× naive);
  sweep: 434 anchor-bearing viterbi words → 27 generator proposals →
  **2 survive the ≥2-check bar**. Enlightenment: the binding change is
  not just the 20 strings — it is the **unit SHAPES** (single letters
  legal, onset clusters atomic, mute-e written) plus **subsequence
  matching**; the old instrument failed on a single unit ('m'), the new
  passes because the tiler EMITS 'm' and the index tolerates the
  segmenter's mis-cut. The cost: fragment matches ("onner", "lement") —
  controlled by the whole-word/fragment distinction and the ≥2-check bar.
  Anchor tiers per the note: 77="le" PROV, 87=ce prov-strengthened,
  94="ne" prov-strong, 96="par" CONFIRMED-inheriting; 06 not an anchor.
  Trace: `code/crowd6/inventorist/{byear.py,build_index.py,
  byear_index.json,matcher.py,control.json,sweep.py,sweep_results.json}`,
  `code/crowd6/report_inbox/inventorist-pattern-redrive.md` (this sweep).
- **F56** — **Scorer objective repair (round 6, COMPLETE — see F58 for
  the landed control verdict, executor-grade):** N36's ordered import list executed per PREREG.
  **Step 0 — N36 re-derived EXACTLY:** truth lam=10 −32.431 (s_let
  −3.4313, n_poly 3) vs annealed best −2.592 (runs −2.631/−2.592/−2.811);
  crossover **λ*=0.0538** (N36's <0.09 tightened); basin test 3/105
  recovered (1/15, 2/30, 0/60) — all 9 low-T descents walk AWAY from
  truth. The full 105-descent battery was re-run and reproduces the
  .md's denominators — **the F51 traceability flag's denominator question
  is resolved in favor of the .md** (fresh run, executor-grade). Verdict:
  the objective is wrong, not the search. **Step 0.5 — F() history bug
  (discovered during re-derivation, repaired):** the parent engine's
  F(ca,cb) scored cb's letters given only ca's tail START-padded — cost
  truth 0.75 nats/letter (−3.38 buggy vs −2.63 correct stream walk,
  identical text); repaired to per-letter scoring with true rolling
  history (`_hist_before` walk-back); self-test PASS (revert consistency
  0.0, stream-walk exact, E-step history exact). **Step 2 — phonetic
  projection:** truth s_let raw −3.4313 → projected −2.6275; meme-collapse
  s_let_proj −3.3647 vs truth −2.6275 — the letter term now correctly
  penalizes degenerate repetition (the earlier +0.054 delta was confounded
  by the F() bug). **Step 3 — spanning word bonus (D2-repaired):**
  truth S_word 0.3231/letter; meme-collapse 1.6458/letter — dedupe halves
  the degenerate profit vs frozen overlapping-hit style (3.234 → 1.6458,
  2.0×) but 'meme' (wt 6.98, lexicon #1) IS a genuine longest match, so
  dedupe cannot kill it — this is why the concentration penalty is in the
  import list, ordered last. With the F() fix, truth total −1.3045 >
  meme-collapse −1.7189 even before step 4. **~~Pending:~~ SUPERSEDED —
  steps 1 and 4 have since landed and the control verdict is in: see
  F58 (repair COMPLETE, control verdict CONTROL-FAIL, gate holds).**
  PREREG AMENDMENT
  (pre-run): projected cap 6 → RAW-cell cap 3 — measured on the sealed
  control, truth's projected 'e' has n_p=10 (raw e/es/et/é/est ×2 groups
  each project to 'e'), so cap 6 would penalize truth itself; raw cap 3
  is safe BY CONSTRUCTION (build_codebook: every non-singleton cell has
  exactly 2 groups; petit-chiffre max quota 3–5). Control verdict
  (pre-registered bars C1–C4) landed in F58. Trace:
  `code/crowd6/scorer/{PREREG.md,objective.py,phonetics.py,models.py,
  step0_baseline.{py,json},step123_truth.json,selftest_objective.py}`,
  `code/crowd6/report_inbox/scorer-objective-repair.md` (this sweep).
- **F57** — **Segmenter rotation round-6 follow-ups (executor-grade,
  pre-registered PREREG.md, amendments A1–A3):** four verdicts.
  **(1) Labeling-robustness: FRAGILE by the pre-registered bar**, with a
  precise diagnosis: the gate reproduced F43's E1 EXACTLY (obs=0.4219,
  z=5.81 vs banked 5.6) ONLY after pinning the construction round 5 never
  archived — lag-3 pairs with BOTH endpoints in ABC (n=1,510), Markov
  expectation conditioned on endpoints-ABC. Battery: k=16 replicates
  z=+5.54, 91/96 agreement; cosine (z=−1.30), k=8 (+0.40), half-stream
  (−0.26/−0.28) all fail — but the failure mode is **LABELING DEGENERACY**
  (one mega-cluster: A=82/76/72), never excess-death under a valid
  3-block labeling. With FIXED full-stream labels the excess is GLOBAL —
  halves z=+3.49/+4.76, all four quarters z≥+2.00. Dominant directed cycle
  A→B→C→A everywhere measurable (ref 836/425; k=16 post-alignment
  786/392). **(2) HMM vs 96-group bigram: NO**, the 3-state HMM does not
  win held-out (−4.2638 vs −4.2356 testLL/trans; bigram wins by 0.028
  nats/trans despite 31× the parameters, 9,120 vs 293; BIC favors HMM
  12,009 vs 74,105 — the AND-bar fails). The unsupervised HMM's
  transition matrix is itself cyclic (S1→S0→S2→S1 dominant) — suggestive,
  not a finding; banked labels as observed states are worst (−4.5348).
  First attempt diverged numerically (emission collapse, −332); fixed with
  MAP-EM eps=1e-4 smoothing (A3). **(3) 69/96 vs "61/96 change":
  RECONCILED** — N30's "61/96" = naive label-name comparison (35/96
  agree), N37's "69/96" = best-permutation agreement (perm BACR =
  old-A↔new-B swap); cycle direction preserved under the permutation —
  no data contradiction (consistent with F43's retirement of the naive
  figure). **(4) Column geometry: MIXED, with an UNRESOLVED CONFLICT.**
  P2a momentum SUPPORT (after a cycle step the cycle continues 63.3%
  (n=765) vs 48.6% after non-cycle ABC steps (n=383), z=+4.77, p≈1e-6);
  P2b FALSIFIED (2nd-order Markov −1.2189 vs 1st-order −1.2143/pos on
  held-out — genuine second-order structure is concentrated in the
  cycle-continuation contrast; a full memory-2 model doesn't generalize).
  **P2c CONFLICT:** this thread reports one fixed column order
  A→B→C→A in both halves (422/198, 414/226), the variant leg void —
  while the side-rotation fleet reports P2c **FALSIFIED** (the dominant
  directed 3-cycle flips across stream halves and clustering variants,
  F50). The note carries its own OVERLAP FLAG: a parallel side-rotation
  fleet is running similar work
  (`code/side-rotation/rhythmicist/{hmm_compare.py,robustness.py}`,
  `geometer/wo2_homophone_cycling.py`) — **deconflict before merging
  conclusions**; the P2c question stays OPEN. Enlightenment: the round-5
  E-code was never archived and the headline number came from an
  undocumented endpoints-ABC restriction — the gate caught it (naive
  full-stream gives obs=0.3579, z=5.90: same z, wrong construction); the
  "fragile phases" story splits in two — the ASSIGNMENT is fragile
  (metric/cut/sample-size) but the EXCESS survives every labeling that
  recovers a real 3-block structure, and the rhythm is global under fixed
  labels. Fragility of the instrument ≠ fragility of the phenomenon.
  Caveat: the Viterbi/banked contingency doesn't map cleanly (states mix
  banked phases) — the HMM's cycle is in transition structure, not state
  identity. Trace: `code/crowd6/segmenter/{PREREG.md,rotation_r6.py,
  rotation_r6.json,hmm_test.py}`, `code/crowd6/report_inbox/
  segmenter-rotation.md` (this sweep).
- **F58** — **Scorer objective repair COMPLETE + control verdict
  CONTROL-FAIL (round 6, executor-grade; supersedes F56's pending):**
  N36's import list executed per PREREG + amendments; the assigned repair
  task is complete and validated. **Step 1 — lam_poly calibration:**
  ablation at lam_poly=0: annealed best −1.9917 vs truth −1.3045;
  λ*=−0.01527 < 0 — **truth already wins at λ=0**, so the pre-registered
  2λ* rule is void; amended to guardrail **LAM_POLY=0.05** (truth pays
  0.15; n_poly=48 pays 2.4). **Step 4 — concentration penalty (amended):**
  projected cap 6 → **raw-cell cap 3** (truth's projected 'e' has n_p=10 —
  cap 6 would penalize truth; raw cap 3 safe by construction, max 2
  groups/cell); **LAM_CONC=3.58e-4** calibrated against the observed
  meme-collapse (ablation showed no collapse, G=0; truth pays 0).
  **Full control (3×600 sweeps + 400-sweep marginals):** C1 PASS (truth
  −1.4274 > annealed best −2.4116, gap 0.98 — the objective now correctly
  ranks truth first; the N36 "truth 30 nats below nonsense" failure is
  FIXED); C2 FAIL (primary top-1 0.000 = 0/20); C3 FAIL (islets 0/3);
  C4 FAIL (pins 7/7, margin 0.92 < 1.0 — near-miss; the bar was repaired
  from the unmeetable 200-nat round-4 bar). **Verdict: CONTROL-FAIL.**
  Precise diagnosis: the objective is repaired, the search cannot find
  truth — single-group moves can't navigate the projected landscape
  (30-symbol projection collapses distinctions, weak gradients; best-key
  primary accuracy 1/20 = 0.05; T=0.3 marginals random-walk, total −5.08
  after marginals). What would fix it: stronger search (block moves,
  longer anneal, population-based) or a less aggressive projection.
  **Gate holds: NO R5005 until a control passes.** Trace:
  `code/crowd6/scorer/{PREREG.md,objective.py,models.py,step0_baseline.json,
  step123_truth.json,step4_calibrated.json,step5_control.json,step6_basin.py}`,
  `code/crowd6/report_inbox/scorer-objective-repair.md` (final, this sweep).
- **F59** — **Side-homophonic-rebuild closing verification (independent
  verifier, 2026-10-07):** pilot FAIL confirmed, stronger than reported.
  Verifier's own code (reimplemented E-step/CharLM/phonetics/phase from
  `REBUILD.md` §1, cross-checked against the library on 3,845 strings —
  zero mismatches; read-only, no R5005 contact). Morpheme-salad finding
  CONFIRMED: pilot winner (restart 199939, npoly=0) −2,352.3 vs planted
  truth −4,953.3 — **salad beats truth by 2,601 nats** (the Smith's quoted
  2,577 understated it; the recorded assignment is the post-refine state,
  +24 nats); every part matches the Smith's table to ≤0.1 nats. Primary
  recovery **1/89 = 0.0112 CONFIRMED** (chance level); morpheme composition
  CONFIRMED byte-exact (37 distinct raw values: tre×8, elle×7, ter×7,
  pre×7, me×6, gouverne×6, par×6, les×5, pro×4, ment×4, des×3, de×3…);
  all four restarts beat truth. **R2: direction CONFIRMED, attribution
  CORRECTED** — shipped config (word_minlen=6) flips the diagnostic
  optimum (+1,554.5 nats, degenerate −6,507.8 vs truth −4,953.3); but
  "reproduces exactly with word_minlen=0" is REFUTED as literally stated
  (word_minlen=0 gives degenerate −1,128.6 vs truth −4,460.7 — NOT R2's
  −4,585.6/−7,215.7); R2's numbers need the pre-gate code state {raw
  S_char + gate-off S_word + λ_poly=50}. R2's KILL verdict itself stands
  (gate-off degenerate still beats truth by 3,332 nats). **Goodhart
  assessment: narrow claim REFUTED, conclusion UPHELD** — 854/1152
  reweightings of the objective flip the pilot with truth still beating
  the frozen degenerate (e.g. M1=+809 at a=b=c=1, d=50, e=20, cap=2).
  **Aggregate gate CONTROL-FAIL** (6-instance): primary mean 0.0019
  (bars 0.20 / 0.10 / μ+5σ 0.098), secondary mean 0.1244 (bars 0.30 /
  0.22 / μ+5σ 0.227); pins 7/7 intact every instance; islets 0/6.
  Trace: `code/side-homophonic-rebuild/verifier/CLOSING-VERIFICATION.md`,
  `code/side-homophonic/runs/{AGGREGATE-GATE.txt,CONTROL-VERDICT.json}`,
  `code/side-homophonic-rebuild/pilot/rebuild-pilot-final/result.json`
  (sha256 d4e2dd6f728e3b9a56ea62b8269f13a54039c597ca5f17c122dc511ab7f1b70b).
  **Fresh-instance infrastructure (standing ready, unscored):** a fresh
  6-instance batch (seeds 184201–184204, 184206, 184207; 1,846 pairs, 96
  groups, crib 1× each) verified in-band — occurrence χ² 195.1 / 222.9 /
  183.2 / 245.3 / 242.3 / 285.3, all inside the pre-registered [181,320]
  band; 184205 QUARANTINED (χ²=329.5, +3% over the band ceiling — binding
  metrologist adjudication, replaced by 184207 @ 242.3, first in-band
  draw in seed order); a q_cycle=0 ablation set (184213–184218, χ²
  0.8–8.8, noise floor) built and scrub-verified with chance baselines.
  The fresh batch is NOT yet scored on the rebuilt objective — Smith
  re-delivery pending after the R2 kill; verifier concurs: DO NOT run on
  the current objective. Trace:
  `code/side-homophonic-rebuild/{PHASE1-VERIFICATION.md,
  metrologist/{FINDINGS.md,band_check_results.json,sealed-pclasses.json},
  control/{chance_baseline.json,instances-dropped/QUARANTINE-184205.md},
  redteam/RULINGS.md}`.
- **F64** — **Solver rebuild round-2 fleet CHARTERED (2026-10-07,
  pre-registered):** attacks the binding Goodhart-on-LM diagnosis — the
  independent verifier proved scorer reweighting within the 5-gram+lexicon
  family is EXHAUSTED (854/1152 reweightings flip the pilot statically,
  yet S_char itself favors salad by 1,540 nats and S_cov by 1,370 — no
  weighting makes truth the robust argmax); the failure is in the
  likelihood, not the weights. Three tracks, each with a numeric bar and
  red-team kill authority, R5005 strictly untouched: **A** (register-gap
  test — rescore truth vs frozen salad under a register-matched
  diplomatic-corpus reference vs Tocqueville; H0 iff truth beats salad
  ≥+500 nats under register-matched while salad wins under Tocqueville;
  H1 iff salad still wins ≥+500); **B** (neural char-LM — SUCCESS iff
  truth beats frozen salad ≥+1,000 nats AND an adapted salad ≥+300);
  **C** (boundary-aware rescore — PROMISING iff truth beats salad ≥+800
  nats). Status at charter: track A PREREG + reference build only
  (rescore written, NOT executed — awaits red-team sign-off); track B
  PREREG submitted, no code run; track C building decodes. Trace:
  `code/side-homophonic-rebuild2/{FLEET-CHARTER.md,redteam/RULINGS.md,
  track-a/PREREG.md,track-b/PREREG.md,track-c/PREREG.md}` (this sweep).
- **F60** — **Period-drag T1–T8 (round 6, executor-grade):** the 117
  red-team-adjudicated period crib cards dragged against the canonical
  1,847-pair repaired stream at 8 concrete targets, using the
  crib-learned F44 24-unit by-ear alphabet (inventorist tiler top-8 UNION
  manual fused/split variants); anchor-preserving nulls (N34: lexicon
  11,870 words, same window, same anchor set, anchors never shuffled);
  ≥2 independent checks per claim. **T4 ("le gouverment" @1180/@1351):
  HIT on the SHAPE, both windows** — three live tilings: (a)
  le|gou|ver|m|ent (94=ver, keeps 77=le, breaks 94=ne); (b)
  le|gouv|er|m|ent (94=er, collides with GT 29=er); (c) gouv|er|ne|m|ent
  = "gouvernement" proper (77=gouv, 78=er, 94=ne, 82=m, 06=ent — keeps
  94="ne" prov-strong + 06=ent restricted + 82=m GT; 77 free per F37
  fence). Checks: C1 exact by-ear fits at BOTH windows (82=m
  GT-anchored); C2 shape rarity — [le,?,?,m,ent] family 1/11,870
  ("légalement"), general null 289/11,870 = 2.43%/window; C3 94-reading
  among lexicon fitters: @T4 ne×10 / ver×0 / er×3, independent @578
  trigram ne×3 / ver×0 / er×17. **The either/or is resolved in F61.**
  Frame verification VOIDED two memo claims before any positions were
  cited: the memo's "R1a followed by 77=le (sentence break)" is a
  RAW-FRAME ARTIFACT (raw@884's 9-mer `...06 77 44 91 67` absent from
  every canonical parse); memo R2 `06 77 78 18 71 10 01` @raw1429 is
  0× in the repaired stream (0× in the old parse too) — the
  "06|77|78 = ent le gou" cross-check cannot run. Confirmed positions:
  "la première" @754/@1034 repaired (= memo raw 766/1054); R1
  `77 78 94 82 06` @1180/@1351 (= memo raw 884/1204); 94-82-06 trigram ×3
  @578/@1182/@1353 (the T4 windows ARE two of the three); 96=par ×21.
  **T5 LEAD: 96-00 "par le" ×3** (@47/@465/@960, consistent on 00="le";
  null 64/11,870 = 0.5% @465) — needs its own battery; **TENSIONS F40
  00="pour"** (flagged, not resolved). **T7 LEAD: "Mehemet-Ali" @8**
  [78,18,93,62,98] = me|he|met|a|li — anchor-bearing on the 78={me,ver}
  islet, null 33/11,870 = 0.28%, despatch-opening position; needs its own
  battery. T1/T2/T3/T6/T8 NULLs → N32. Methodology note: the memo's cut
  model needs hand variants (the tiler over-splits to 7–8 cells and never
  emits [le,gou,ver,m,ent]); provisional anchors propagate their status —
  nothing promoted. Trace:
  `code/crowd6/period_drag/{results.json,t7_anchored.json}`,
  `code/crowd6/report_inbox/period-drag-t1-t8.md` (this sweep).

### Round-7 addenda (2026-10-07)

- **F61** — **Crowd7 redteam: F26-17 review + T4 either/or adjudication:**
  the round-6 red-team session ended before adjudicating, so round 7's
  first work order was to review every "curator: …" mark (uphold/overturn)
  before other executors build on them. **F26-17: 12 of 13 marks UPHELD**
  — the coordinator's round-6 marks N39–N44 (nulls) / F45–F51 (findings)
  use the coordinator's own numbering, DISTINCT from this report's
  F-series: N39 NO PROMOTION, N40/N43 CONTROL-FAIL, N41 segmenter, N42
  period-drag, r6-F45 59="est" STRONG LEAD [= report F44; promotion to
  provisional DENIED], r6-F46 84 conflict, both LEAD [= report F46],
  r6-F47 00 conflict [= report F45 vs the F60 00="le"×3 LEAD], r6-F48
  "parmi"/"cela" LEAD [= §6 open hypotheses], r6-F50 "même" LEAD [=
  report F47], r6-F51 "le me" dissolved [= report F47] — all on
  independent re-derivation: 61/61 new checks PASS + 49/49 inherited
  baseline PASS. **N44 "0 promotions, 0 kills, 0 demotions" is wrong:
  corrected net = 0 promotions to provisional+, 2 LEAD-tier elevations
  (00="pour" lead→STRONG LEAD — the promotion N44 missed; 59="est" new
  at STRONG LEAD), 0 kills, 1 demotion (43="me" MEDIUM→WEAK,
  worker-decided).** Every stream-derived number re-derived
  on the repaired 1,847-pair stream. **T4: tiling (c) "gouvernement"
  SURVIVES as LEAD; tiling (a) DISFAVORED; the either/or is RESOLVED, not
  unresolvable. 94="ne" and 77="le": NO status change.** Why: (a) must
  OVERTURN F37's red-team fence (77="le" is fenced OUT at @1180/@1351 —
  it doesn't "keep" 77="le") AND demote 94="ne" prov-strong on an
  n_eff=1 unfalsifiable rule — doubly blocked. (c) preserves every banked
  value and CONFIRMS F37's fenced trigger ("gouv"). (c)'s only cost, F38's
  78="ver" islet, had contaminated "ver"-specific evidence: its 554
  "vernement" era tokens are ALL "gouvernement*" (the worker's own memo),
  morphemically gouv|erne|ment — the worker's ver+ne/ver+re binary never
  tested the live er+ne alternative. **F38's islet value is DOWNGRADED to
  a {ver, er} fork** (the "≠me" core stands). (c)'s 77="gouv"/78="er"
  islets are n_eff=1 LEADs needing independent support. Memo index
  hygiene: the coordinator's F46 "re-derived" positions are uniformly +1
  (successor indices, not bigram starts — correct:
  [145,259,1057,1446,1484,1763,1802]); same +1 slips in two worker memos
  (94→84 @1664 not @1665; 11→84 @1619 not @1620; F50 quad @312 not @313;
  77→62 starts @507 not @508) — counts were all right; the extension
  script supersedes the NOTES.md figures. Trace:
  `code/crowd7/{redteam/RULINGS.md,redteam/verify_f26_17.py,
  report_inbox/redteam-f26-17-t4.md}` (this sweep).
- **F62** — **Cross-fleet memo 3 — homophonic solver CONTROL-FAIL: two
  rotation findings for the main fleet:** (1) the contactor's unsupervised
  χ² is a **NOISY DETECTOR** (instrument flag): on 6 synthetic controls
  with TRUE occurrence-phase χ² of 181–272, the identical unsupervised
  pipeline (Jaccard clustering → phase labels → χ²) reads **36.6, 0.4,
  787.3, 375.5, 6.2, 2.9** — in-band on 0/6 (the design doc's own caveat:
  Jaccard clustering recovers planted phases at purity ~0.5, making its
  χ² a coin flip; the solver's χ²-gated prior was DEMOTED on this basis).
  Three-way scope for the main fleet: (a) rhythm EXISTENCE — confirmed by
  the label-free lag-3 test (z=+5.6, p≈1e-8; round-6 Segmenter) — NOT
  impugned; (b) exact χ² MAGNITUDE (181.3 original; 366.3 recomputed) —
  noisy, no main-fleet argument may lean on the value; (c) phase MAPPING
  (which group → A/B/C) — ~0.5 purity, coin flip; any per-group phase
  argument (e.g. "X is phase C, therefore word-final") stands on a noisy
  instrument and must be flagged/demoted unless independently supported.
  Null streams (uniform random) measure χ²∈[2,33]: "rhythm exists" does
  not imply "mapping is right." (2) **contact-coherent aliasing:**
  POSITIVE key-structure clue — the control generator proved by
  construction that uniform-random homophone aliasing fragments contact
  profiles and the rotation VANISHES (χ²=3.9); the rotation only survives
  when aliases are dealt phase-coherently (each cell's aliases
  round-robin to phases; emission picks the occurrence-phase primary).
  R5005 shows visible rotation ⇒ the real key-maker's aliasing is
  CONTACT-COHERENT, not uniform-random — consistent with F33's conditioned
  polyvalence (the conditioning rules ARE contact-coherence made
  explicit). Round-7 work order: invert the aliasing via phase-conditioned
  contact profiles to propose homophone sets; test whether merging
  candidate alias sets under F33 rules improves assignment coherence.
  Trace: `code/crowd6/report_inbox/crossfleet-memo3-homophonic-rotation.md`
  (this sweep), `code/side-homophonic/runs/RUN-REPORT.md`.
- **F63** — **Side-period corpus + red-team crib adjudication (2026-10-07):**
  period-appropriate reference corpus built (his methodological steer:
  ERA and REGISTER must match — 1830s–40s diplomatic French). Sources:
  Nesselrode correspondence v7–v10, Guizot memoirs t1–t3/t5–t6
  (Gutenberg), Talleyrand memoirs, Metternich papiere v4/v6, Revue des
  Deux Mondes 1841 Q1–Q4, Allgemeine Zeitung Augsburg 11–25 Jan 1841,
  Levant correspondence 1841, ADB Zeschau bio — each with PROVENANCE.
  The miner produced 121 crib cards (32 P0 / 55 P1 / 34 P2); red-team
  adjudication (kill rule: "Zeschau in Dresden on 18 Jan 1841 must
  plausibly KNOW and SAY it"): **117 survive** (31 P0 unique — 32 rows, 1
  duplicate merged — + 54 P1 + 32 P2), **3 killed**: "mon cher comte"
  (Seebach was a BARON in 1841 — the count era is later; a minister does
  not misaddress his own envoy), and two envoy-voice formulae with the
  direction reversed ("…m'indiquer la conduite que je dois suivre",
  "Votre Excellence vient de m'adresser…"). The miner's own demotions
  (Kossuth off-list; "A la première nouvelle que…" → P2; "J'ai l'honneur
  de …" → P2) re-checked and UPHELD. Verifications: Kossuth demotion
  VERIFIED (0 hits in all four 1841 RdM quarters; corpus hits are
  1849/1850s contexts); Hong Kong / Treaty of Chuenpi: 0 hits in all 25
  files — news-lag kill stands (Britain took possession 26 Jan 1841,
  Dresden on 18 Jan could not know); Ibrahim-at-Damascus VERIFIED (AZ
  11-Jan-1841: "Ibrahim Pascha befand sich am 13 Dec. noch zu Damaskus" —
  the freshest dated news in the corpus); "première" collision CONFIRMED
  HANDLED (only P2 "A la première nouvelle que…" flagged drag-with-care;
  background "premier" STRUCK from drag consideration — pre|m|i|er is
  already read); Mehemet-Ali spelling VERIFIED (RdM house "Méhémet-Ali"
  293×; Nesselrode "Mehemet-Ali"; AZ "Mehemed Ali" 8× — a live by-ear
  variant; drag accentless, all three surfaces); "la Sublime Porte" P1
  promotion UPHELD (157× French-article in the Levant correspondence).
  Register ruling (formulae): Nesselrode's signed hand "Recevez, Monsieur,
  l'assurance de ma considération distinguée" (late 1840) is the top
  authority; "considération distinguée" outranks "haute considération"
  for a baron-envoy — drag the Nesselrode form first. This corpus is the
  source behind the period drag (F60/F61). Trace:
  `code/side-period/{cribs-adjudicated.md,cribs.md,sources.md,
  corpus/PROVENANCE.md,work/*/mine.json}` (this sweep).

### Round-8 addenda (2026-10-07, crowd8 — 12/12 agents merged, adjudicated; NOTES.md F59–F63)

- **F59-AMENDED** — **RdDM "293×" VERIFIED (flag lifted):** exact clean-form
  count of 'Méhémet-Ali' = **293** in the full 1841 Revue des Deux Mondes
  run (4 tomes; 318 incl. variants; 7 unaccented attestations matching the
  cipher's accentless shape; zero 'mohamed'/'mehemed' — cite with OCR
  caveat). **"Mehemet-Ali" @8 DEMOTED LEAD→LEAD-weak** — 62-tension adverse
  (the me|he|met|a|li tiling needs 62='a' vs lane STRONG LEAD 62="on"; no
  alternative len-5 me-initial tiling in the by-ear top-8 avoids /a/ on
  62) + "mêleront" (me|le|r|on|t) is a fully 62-compatible common-word
  rival; M2 (spelling/topicality) stands, so demotion not kill. **16="i":
  position-conditioned alternative NOT SUPPORTED** — T1 Fisher p=0.9398 in
  the WRONG direction (S1 GT-only p=1.0); T2 "premier"/"première" frame
  vacuous (masculine frame 0 occurrences); 16 stays unconditioned LEAD.
  **M3 'he'-purity adverse STRUCK** (scoped German phonetics: AZ renders
  "Mehemed Ali" 75×, pronounced with /h/ — by-ear under the lane's
  German-thought premise; the general German-interference premise is NOT
  banked). Lesson: grep multibyte brackets fail under the C locale
  (7 near-false-refutation hits); recount multibyte text in Python. Trace:
  `code/crowd8/patternist/{round8.py,round8_results.json}`.
- **F60** — **48="ne"-allophone REFUTED (kill-grade):** H2 kill leg fires
  (merged word-rate **4.78×** > 3× bar; 94 alone already 2.36× — no room
  for a second "ne" group); H5 adverse ("ne ce que" @863 with 46="que" GT;
  "en ne ce" @1657–1660); H6 adverse (−0.585 nats predecessor fit). H1
  (F56 interchangeability template) does NOT fire — methodology finding:
  interchangeability is necessary but NOT sufficient for homophony. 48
  never enters the status line. Residual (untested here): 48 as
  verb/verb-stem. Trace: `code/crowd8/homophonist/`.
- **F61** — **{93,8}="l'" LEAD (unconditioned homophones):** joint
  n=32 vs E=31.26 dead-center (two-sided p 0.47–0.60, in-band all diplo
  slices); shared predecessors {67,85,45}/followers {52,29,62} freely
  intermixed (no complementary split); "ne l'est" @101–103 ("on ne l'" ×3
  era); fenced costs 93→52=2 ("l'pas", era-0 — needs a vowel-initial
  third reading of 52) and 87→8=1 ("ce l'"). 93="l'" ALONE rate-KILLED
  (**p=4.1e-4**, holds every diplo slice). N46's "shape-STRONG" does NOT
  reproduce (vow=1; archived `u2_lcell.json` lacks 93 — traceability flag).
  **62="on" +2 non-ear legs** (L_B: 46→62=0, LR=**21.3** for "on" via
  qu'-elision rate asymmetry; L_A conditional on M_hom, 4 windows vs diplo
  l'+il=0) — stays fenced STRONG LEAD; 62="il" → DISFAVORED-STRONG
  (conditional, not fully killed). **06="ent" iff pre=82 → conditioned
  LEAD** (n=4, n_eff=3, F33-form with stated falsifier — watch banked).
  Trace: `code/crowd8/frenchman/{s1_data.py,s2_allophony.py,s3_gouv.py,s4_verdicts.py,results.json}`.
- **F62** — **84 en-islet RE-SCOPED:** «qu'en» legs @310/@473 WITHDRAWN
  ("qu'en en" era-0 = 0/4,220,440; 24="en" holds locally); byte-identical
  5-gram 46-84-24-37-78 ×2 stays an open residual formula. Surviving islet:
  84="en" iff pre∈{82} (GT-anchored "m'en" @167, n_eff=1) ∪ pre∈{66,89}
  (conditional on 66/89 classes). **Noun identity NULL STANDS** — no
  candidate at era rate (best: pas 0.38×, fait 0.11×, 13×+ gaps); the
  «qui le 84 est» ×2 formula (@1447/@1803) is NOT article+noun ("qui le X
  est" 2/4.2M, both rescued/broken) — reads pronoun+verb → NEW LEAD
  **«qui le [verb=84-59]» ×2** (64-77-84-59, needs unbanked 59-as-syllable;
  referred, not claimed). 13 free windows: 4 EN-EXTENSION (conditional),
  9 RESIDUAL. Rate-model lesson: mixed-language reference pools inflate
  overs ~2× — B1 9.14×→**3.91×**, B3→**3.19×** French-only (residual
  floor 2.73×). Trace: `code/crowd8/conditioner84/{analyze84.py,analyze84b.py,conditioner84_results.json}`,
  `code/crowd8/ratemodel/`.
- **F63** — **WO-6 "second 64-96-47 window" criterion RETIRED** —
  impossibility proof: exactly ONE 64-96-47 window (@149–151) and exactly
  ONE 96 with suc==47 (@150) in the whole stream — singleton by
  construction, the promotion bar is logically unmeetable. 96=verb-stem
  stays LEAD at n_eff=1 (promotion must come from adjacent islets or
  corpus legs). NEW adjacent-islet lead: **qui-96-43 ×2 formula**
  (@341–345/@1025–1029 share 45-64-96-43-87-01, diverge 06-70 vs 03-29).
  Downstream-verb hunt: null again (@153–175 no verb cell). **Columns
  refuge: all 4 concretizations DEAD** (momentum z=−65…−112;
  lane-faithful k=12/top-96 ARI≈0 vs random nulls); schema survives only
  LOGICALLY-OPEN-NO-EVIDENCE; full kill needs key recovery (standing).
  Trace: `code/crowd8/morphologist/{prereg.md,results_r8.json}`,
  `code/crowd8/segmenter/{recoverability.json,diag_k12_top96.json}`.

### Round-9 addenda (2026-10-07, crowd9 — 10/10 agents merged, adjudicated; NOTES.md F64–F69)

**Net: 0 promotions — the bar held an eighth round.** Scoreboard 12
values (7 GT + 87=ce/64=qui/96=par/59=est provisional + 77="le"
provisional-conditioned). Baselines extended to 114/114 and 82/82 PASS;
7/7 battery preregs timestamp-audited (watch06 PASS WITH NOTE — disclosed
post-census addendum, no bar-fitting).

- **F64** — **H_verb (48 = conjugated verb) KILLED** — K2 fired per
  pre-registered terms: V2 ADVERSE (0/2 "48 pas" windows ne-licensed,
  span-robust to i−10) AND V3 predecessor verb-licensing 31.6% < 40% bar;
  steelman denied as post-hoc rescue. H_stem (96-family) UNTESTED
  (predecessor cosine 0.387 < 0.60, n96=21 underpowered — explicitly not
  adverse). **48 stays UNIDENTIFIED.** Datum correction: 48 has **29
  distinct/38** successors (not 19 — old-parse figure). "on 48"×6
  association real (E=0.72, p=**7.6e-05**) but carries no verbal
  signature; "48 pas"×2 not significant alone (E=0.555, p=0.106).
  Round-10 lead: frequent syllable cell ("on"+verb-initial syllable).
  Trace: `code/crowd9/successor48/{PRE-REGISTER.md,battery48_verb.py,battery48_verb_results.json}`.
- **F65** — **86=que-family REFUTED (kill-grade, 4 legs):** L2 «pour qu'»
  12/55=0.218 vs era 0.0104 (**21×** over); L5 elision kills «qu'»
  (86→70/52×2/56×4 = 7/32 consonant-initial successors); L6 77-86 ×5 at
  era P≈**0.00007**; L4 profile parity fails (Jaccard 0.33/0.25). B3
  dissolution caveat DEAD twice over (era number was 0.0343 French-only,
  not 0.31) — **B3 (3.19×) STANDS.** 86's value NULL (honest);
  F40 verb-stem-class stands as working hypothesis. **66-class CONFIRMED**
  (broadened {noun, infinitive, nous/vous-type} — all en-compatible) and
  **89 noun-class CONFIRMED** (77-89 ×2, 29-89 ×5, 89-48 ×3; fenced
  tension 52-89 ×2) — 84-islet's pre∈{66,89} dependencies hold.
  qui-96-43 ×2 formula HOLD (@341/@1025; **43="me" clitic-order adverse**
  banked in this frame — weak globally, not here). «qui le [verb=84-59]»
  REFINED: noun+"est" parse DEAD at @1447/@1803; 59="est"-as-word era-0
  there (fenced n=2 adverse) — bisyllabic-verb unit
  hypothesis-internal (needs unbanked 59 conditioned polyvalence). 84's 9
  residuals all classified RESIDUAL (no islet change; @857 lean withdrawn
  — depended on killed 48="ne"). **Islet registry built:** 9 conditioned
  islets with rules, n/n_eff, falsifiers, leftovers
  (`code/crowd9/conditioner/islet_registry.md`).
- **F66** — **@1351–1356 under TRIPLE FENCED PRESSURE** (top round-10
  watch): H1c ("on" in L1..L2 of "gouvernement" = **0/641** diplo; @1351
  has 62="on" STRONG LEAD at L2), H1d ("le qui" = **0/391,210** vs the
  right frame under banked 37="le" MEDIUM + 64="qui" prov), frenchman
  triple collision (06-islet "ne ment pas" era-good vs gouv
  "gouvernement pas" era-0 in 40 tokens vs 77="le" — mutually exclusive;
  era picks the 06-islet parse). 77="gouv" holds LEAD per the n≥3 rule.
  **H3a NEW WEAK LEG for fork-tine (c):** er|ne boundary productive (52
  tokens/22 types) vs ver|ne zero genuine common words (**10.4×**, Fisher
  p=**3.2e-11**; gouvernement-family excluded to avoid circularity) —
  lean (c) strengthened, fork unresolved. 06="ent" by-ear mixed: @1355
  clean, @580 fenced admissible, @1184 adverse-fenced ("ne
  mentent/entendent est" ungrammatical with 59="est"-as-word), @738
  fenced. The 06-islet survives watch06's hunt (all 3 falsifiers unfired;
  n_eff=3 fragility banked; post-hoc: both suc=6 windows are islet
  windows, p=0.0063 — possible 94-82-06-06 4-gram refinement for round
  10). Trace: `code/crowd9/{hunter7778,watch06,frenchman}/`.
- **F67** — **@1248 NEITHER-fence UPHELD** (new arm declined with
  evidence: "pour * que" middles {cela:3, empêcher:1}, no single-syllable
  X with era support; finite-verb arm vetoed by frenchman Gate 4).
  @199 NEITHER-fence CONDITIONAL on 08="l'". @630 et-CONDITIONAL (Bar E2,
  C1∧C2 explicit — not a classification). 6 open-residual (no ≥2-leg
  bar). **Fork stays SUPPORTED with amended scope (fenced n=2).**
  R_veut4 dropped at design time ("me veut"=0 voids the legs). 62-WO3
  blocker carried forward (no substantive 62-interaction found).
- **F68** — **germanist clearance + liaison:** M3's 'he'-cell adverse
  STRUCK (scoped German phonetics — AZ "Mehemed Ali" 75×, the h is
  pronounced; under the Zeschau-thought-in-German premise the 'he' cell
  is by-ear; the general interference premise is NOT banked). "Mohammed"
  15× = Dost Mohammed (Afghan emir) — formally excluded as a Mehemet-Ali
  variant. No German-interference vetoes on any live reading; watch-items
  banked as standing conditionals (standalone 78="er" → German "er"
  rival; 67@1248="cela/ça" → "dafür daß" calque test). Crib candidates
  banked with AZ provenance (Thiers 76×, "Ibrahim Pacha", Ponsonby 4×,
  "question d'Orient", Bugeaud 18×, Valée…). Liaison: rebuild2 healthy
  (red-team 0 KILL / 4 UPHELD / 6 CONCERN / 3 GO; tracks A/B/C executing
  per PREREG, no results yet); constraints memo banked
  (`code/crowd9/liaison/smith-constraints.md`): F33 rules, anchor set,
  5 discriminating windows, must-NOT-break list. Main-fleet search scope
  ZERO until C1. Trace: `code/crowd9/germanist/az_evidence.json`,
  `code/crowd9/liaison/`.
- **F69** — **62 on/il HONEST HOLD** — N35 independent-cell battery 0/4
  (C1 p_two_il=0.072 sub-bar lean, no quiet upgrade; C2/C3/C4 null).
  62="on" stays fenced STRONG LEAD; 62="il" stays DISFAVORED-STRONG (not
  killed). @100 "62 ne l'est" fenced n=1 descriptive, zero leg weight.
  C1–C4 banked tested-NULL. Mehemet-Ali/@1248 blocker NOT lifted.
- **Methodology (rounds 8–9, for the record):** the F56
  interchangeability template's NON-firing is itself a finding (necessary
  ≠ sufficient for homophony); mixed-language reference pools inflate
  era overs ~2× (B1/B3 correction); grep multibyte brackets fail under
  the C locale — recount multibyte text in Python (near-false-refutation
  on RdDM); phase-of-neighbor tests must control for the group's own
  phase (F4 lesson); **the over-splitting lens** (round-9 frenchman
  register gate: the cipher over-splits relative to spoken French —
  46=que writes /k/ as its own cell, 82|06 at @1355 writes one spoken
  syllable /mɑ̃/ as two cells — any by-ear argument treating a cipher
  cell as a spoken syllable assumes spoken-syllable alignment and is
  flagged); rate bars run Nesselrode-v8-strict (the {93,8} joint model
  is in-band at v8 E=32.9 but collapses to E=11.9 if levant is pooled —
  register heterogeneity, not one number); 7/7 round-9 battery preregs
  timestamp-audited (watch06 PASS WITH NOTE — disclosed post-census
  addendum, no bar-fitting).

### Round-10 addenda (2026-10-07, crowd10 — 10 agents, adjudicated; NOTES.md F70–F76)

**Net: 0 promotions — the bar held a ninth round.** 1 islet registered
(ISLET 10), 2 refutations (unconditioned-59 kill-grade; H4g kill-grade by
prereg literal formula), 1 window resolved (@1351–1356), 0 kills of
banked statuses. Baselines 132/132 + 89/89 PASS.

- **F70** — **@1351–1356 RESOLVED → R-c owns the window: «le [78] ne ment
  pas»** (byte-exact @1349–1362 = 62 48 | 77 78 94 82 06 52 | 37 64 35 13
  92 62). R-b ("gouvernement") OUT at @1351 HIGH: «gouvernement pas»
  0/40 and ungrammatical (needs intervening verb+ne); 52="pas" (STRONG)
  needs the negation frame only R-a/R-c supply via 94="ne"@1353 (no
  other 94 in @1340–1370). D3 fires 77="le" via F37's conditioned default
  (the fenced "gou" exception at @1351 existed only for the 5-mer). **77="le"
  GAINS @1351** (application, stays provisional-conditioned);
  **77="gouv"→@1180-only** (LEAD, n=2→1, no kill); 78="ver" by-ear gloss
  @1352 dies (positional membership kept — fork unresolved). The 06-islet
  loses NOTHING (membership is positional; n=4/n_eff=3; no registry
  edit — its by-ear gloss at @1355 is now "ne ment pas"). H1c MOOT; H1d
  NARROWS to {37="le" MEDIUM @1357, 64="qui" prov @1358} — "le qui"
  **0/391,210** survives the ruling, flagged for the 37/64 lanes (not
  adjudicated here). Caveat: the exact trigram «ne ment pas» is 0/92k
  v8 (grammatical, unattested — later attested 1/3.96M diplo, round-11
  watch). Trace: `code/crowd10/resolver1351/{PREREG.md,derive1351.py,derive1351.json}`.
- **F71** — **ISLET 10 REGISTERED (LEAD): 59=word-«est» iff
  pre∈{64,94,93}** («qui est»×3, «n'est»×2, «l'est»×1 — est-arm 6/6);
  **59=verb-final «-este» iff pre=84** (@1190/@1448/@1804 firm, @1291
  fenced — este-arm 4/4). Full census: **n59=27** (27/27 classified: 6
  EST + 1 NEUTRAL + 5 ESTE-firm + 2 frame-forced + 1 lean + 2 FENCED +
  10 LEFTOVER). The executor's proposed pre=06/{61,44}/86
  extensions EXCLUDED (post-hoc, F33) — banked as fenced LEAD sub-tiers,
  not rule members. **Unconditioned 59="est" REFUTED, kill-grade** (8
  adverses incl. @463 «la est» era-0, 0/3.96M). F52's provisional REFINED
  into the islet, not killed; F52 caveat-3 DISSOLVED (L2 honestly failed
  on S4#1 @216 — the «[06-59] que» verb parse supplies the structural
  explanation; the S4 "adverse" was never an «est que» datum). -este verb
  ID set-valued **{manifeste 131, atteste 35, proteste 20, conteste 19,
  déteste 23}**; reste EXCLUDED at «qui le» (intransitive). S1 preserved
  1.07× (the unigram was always a mixture). ISLET 8 follow-up banked;
  ISLET 1 @1189 re-read as @1190 verb-unit. Registry:
  `code/crowd9/conditioner/islet_registry.md` (ISLET 10 appended).
- **F72** — **H4g (94-82-06-06 4-gram refinement) REFUTED by the prereg's
  literal formula** — the executor's p_comb=0.0410 used an un-licensed
  method; recomputed under the PREREG's literal formula
  p_comb=**0.0508** > 0.05 → REFUTED per the pre-registered bar
  (knife-edge 0.0008 above — the bar is the bar). H4g closes as post-hoc
  coincidence, NOT "untestable-at-n=2". The 06-islet stands unchanged
  (all 3 falsifiers unfired; 82→06 census = [580,738,1184,1355] exactly
  as predicted; 94-82-06 trigrams islet-only; n_eff=3 fragility banked).
  Trace: `code/crowd10/watch06/{PREREG.md,fourgram_test.py,fourgram_test.log}`.
- **F73** — **@1248 NEITHER-fence STANDS (not lifted).** Non-finite arms
  built but thin: "peu" 2/4 legs (L2+L3; L1 fail hapax, L4
  indeterminate), infinitive-class "empêcher" 2/4 — banked as WEAK fenced
  arms. "cela" REFUTED on substance (v8 «pour cela que»×3 are
  clause-boundary artefacts or an unhostable cleft; bare-constituent
  «pour cela que»=0). Médiatrice-class DEAD (0 legs). Gate 4 REVISED:
  cela-class REMOVED (frenchman corroboration). **62-WO3 blocker REFUTED
  for @1248 only** (scoped: zero group-62 in ±6). Any @1248-scoped
  reading is n_eff=1. Trace:
  `code/crowd10/arm1248/{PREREG.md,arm1248.py,arm1248_results.json}`.
- **F74** — **0/6 67 residuals classified — all stay open-residual with
  explicit missing legs** (clean null). Fork stays SUPPORTED with
  amended scope; 29/36 classified. Decider named for @1450/@1623: **33's
  class** (infinitive → veut-arm lives; nominal → et favored). @1248
  counterdatum = scope amendment, not refutation. The bar held a ninth
  round.
- **F75** — **48 stays UNIDENTIFIED. S-word class KILLED for 30**
  candidates (report said 31 — "les" double-counted): the structural
  pincer ("la" GT takes nominals, "on" fenced STRONG LEAD takes verbs —
  no single French word at 2.06% follows both) kills 25/31 on S2 alone;
  S1+S3 corroborate; kill survives loss of 62="on". The **10 S-syl
  LEAD-weaks NOT granted as statuses** — banked as a rate-band shortlist
  datum (S1 was the selection criterion; zero discrimination). H_stem
  NULL, stays UNTESTED (the 0.40 signature bar is miscalibrated — the
  lane's own reference stem 06 scores 0.318). Follow-up: successor-word
  anchoring at the six "on 48" windows, or 82="m"×4 frames as a second
  syllable-discriminating leg. Trace:
  `code/crowd10/syllabicist48/{PREREG.md,battery48_syllable.py}`.
- **F76** — **14 era vetoes (EV1–EV14).** EV10 converges with ISLET 10
  (vetoes word-"est" @1447/@1803). **V1 GENERALIZED:** «X pas»-adverb
  without «ne» is era-0 for ALL word candidates X (sole exception «grand
  pas» noun); 48="de" CONDITIONAL (narrow pronoun+infinitive path:
  «de le»[art]=0 but 29 «de le» are pronoun+infinitive), 48="com"
  NEUTRAL (fragment), {en,nous,vous} die V1. Gate-4 revision banked
  (cela-class VOID). Key enlightenment: **read the hits, don't count
  them** («pour cela que»×3 never bare constituents; 29 «de le»/15 «à
  le» all pronoun+infinitive, never article). Trace:
  `code/crowd10/frenchman/{era_gates10.py,era_gates10_out.json}`.
- **Methodology:** the prereg literal-formula discipline paid twice this
  round (H4g overrule; ISLET-10 narrowing) — the bar is the bar, even at
  0.0008 over. Interchangeability ≠ homophony (F60) keeps paying. The
  unauthorized "finalizer" insertion into R10BANK was relabeled — no
  baseline insertions without red-team ruling (procedural case law).
  Liaison: round-10 constraints memo banked
  (`code/crowd10/liaison/smith-constraints.md`, supersedes round-9 memo);
  rebuild2 tracks executing per PREREG; scope-zero-until-C1 holds.

### Round-11 addenda (2026-10-07, crowd11 — executor-grade, LARGELY UNADJUDICATED)

**Red-team docket opened 2026-10-07 ~16:00 CDT EMPTY** — a full lane sweep
found no round-11 executor packages on disk; baselines re-verified
132/132 + 89/89 PASS green; audit bars pre-committed before any executor
data. Later rulings: **R1 GRANT** (watch06 — all three falsifiers
UNFIRED; ISLET 3 survives round 11 intact) and **R2 BANK**
(smith-liaison delta memo); no kills, no demotions, no promotions.
Register check bit twice, honestly: v8's 54 "ment" tokens are
archive.org OCR word-splits (v8 phrase zeros VOID as French
measurements); the clean 3.96M-token diplomatic corpus attests **«ne
ment pas»=1** — the F70 @1355 gloss is rare-but-real, matching the F31
genre reclassification. **No executor package below is adjudicated unless
stated — treat all verdicts as provisional recommendations.** Interim
kills: none. Five executors still running at R1/R2 time.

- **este-verb-id (WO1): H0 HOLDS — no promotion, no demotion, no kill.**
  The -este verb ID stays set-valued {manifeste, atteste, proteste,
  conteste, déteste}. Three non-discriminating checks by construction:
  (a) en-condition predecessor-gated (never fires at the este windows);
  (b) v8 rates descriptive-only (manifeste 1, proteste 1, déteste 2,
  atteste 0, conteste 0 — consistent with banked F-B era-neutrality);
  (c) all five grammatical at every firm window. Two real findings: (1)
  **a3-monovalence FAILS for every candidate** — @1190 (84 = middle
  syllable) requires stem fragments that never equal the first-syllable
  stems, so 84 is polyvalent across these windows OR @1190's verb ≠
  @1448/@1804's verb (pre-registered: not a kill; polyvalence live
  lane-wide); (2) **@1291 has a conditional discriminator** — @1291 and
  firm @1804 share the byte-identical 5-mer suffix [35,94,52,80,4];
  under the verb parse [35] is the «ne»-clause subject, so V must be
  objectless → {manifeste, proteste} survive (intransitive-capable),
  {atteste, conteste, déteste} excluded — CONDITIONAL (verb parse +
  35's role), fenced, no demotion. Tie-breakers that would work: (T1) an
  independent 84 stem ID outside the este frames; (T2) the «le»
  antecedent or 36/35 with selectional force; (T3) 06's ID at @1190;
  (T4) 17/35 resolving @1291; (T5) a second «qui le [84-59]» token.
  Trace: `code/crowd11/este_verb/{PREREG.md,este_verb.py,este_verb_results.json}`.
- **anchorer48 (WO2): 3 fences, 0 promotions, 0 kills.** PATH A (six "on
  48" → suc): FENCED — A1 ("on"+W+"le") 0/10 PASS (("on",*,"le")=11 v8,
  zero shortlist W; @1350's frame wants a VERB/"ne"/pronoun — but H_verb
  killed 48-as-verb and 48="ne" is killed); A2 8/10 PASS but 6 are
  word-driven. PATH B (four 82→48 under the mandated "m'"-premise):
  premise FENCED (v8 ("m'",W)=verbs+pronouns only; under 82="m'", 48's
  options collapse to killed classes). PATH D (48="de"-conditional):
  FENCED with explicit missing legs — **D1 LICENSED** ("de le"+INF
  29/29 hand-verified: faire×6, voir×4, …; "de la"+INF 13/439). @1350 OUT
  (R-c exclusion + "on de" 0/2 genuine), @126 OUT ([m]+"de la" 0/92,594),
  **@1076 IN-PENDING**. The narrow path has exactly 1 independent check
  (D1 era); promotion needs a cipher-side suc2=infinitive ID — missing.
  Out-of-scope observation (not a leg): @863 = 48-47-46 reads "de ce
  que" ("de ce que"=10× v8) — a SECOND "de"-word frame outside the
  narrow path; candidate follow-up. All fences conditional on non-GT
  premises (62="on" fenced LEAD etc.) — none kills any 48 value. Trace:
  `code/crowd11/anchorer48/{PREREG.md,anchor48.py,anchor48_results.json}`.
- **census33 (WO3): 33 = infinitive-class (C1 PASS) → lean-veut at
  @1450/@1623.** Census of 23 windows, all bars pre-registered: three
  independent infinitive kinds — I1 pre==00 "pour" ×8 (E=0.68, p≈0), I4
  suc==29 "-er" ×5 (E=0.56, p=0.0002), I2 pre==67-veut@1423 ×1; ZERO
  GT-anchored nominal hits (the 2 N3/N6 hits chance-consistent, p=0.17).
  The fork's own history corroborates unprompted: "et 33-er" ×2
  (@273,@1477 — et coordinating infinitives), "veut 33-er" (@1423–1425 —
  textbook modal+infinitive). Decider windows' own suc==46 ambiguous per
  prereg (anti-circularity held). Grade capped at LEAN — 67="veut" stays
  provisional, fork stays SUPPORTED, @1248 scope amendment untouched.
  Caveats: 33's specific value unverified; 9/23 windows unclassified
  (silence, not counterevidence); "pour" is lead-grade so I1 carries the
  mark. Trace:
  `code/crowd11/census33/{PREREG.md,census33_results.json}`.
- **finisher67 (WO4): 1 of 6 classifies — @633 → et-CONDITIONAL (C1∧C2).**
  New left-conditioned era frame "l' * et" vs "l' * veut" (conditions on
  08="l'" lead): v8 **92:2** (ratio 46:1; middles noun-dominant —
  "l'empereur et l'impératrice"-type coordination); L2 n(11→52)=3.
  Frenchman check: the *"je l' X veut"* split-pronoun reading is
  ungrammatical, so the veut-arm counts article-frames only — rate test
  stays honest. The other 5: @1519 null (31 contested, leaning verbal;
  V-1519b withdrawn — 08="l'" article/pronoun ambiguity voids it as an
  unconditional nominal licensor), @1372 null (no dense frame: "et pour"
  14<20), @902 null (92 contested: 00→92 ×6 verbal vs 11→92 ×3 nominal;
  16-as-word unmeetable), @1450/@1623 open with the WO-3 decider applied
  (33=C1-infinitive → veut-arm lives; no veut-arm bar exists — designing
  one now would fit known data — so both stay open-residual).
  Enlightenment: the productive move was left-conditioning — round 10
  only tried right-conditioned frames; GT-anchored "la" (11) remains the
  only clean nominal licensor. **Tally if granted: 29 classified + 2
  conditional (@630, @633) + 5 open + 2 fenced = 38.** All counts on the
  repaired 1,847-pair parse + Nesselrode v8 (NW=92,123). Trace:
  `code/crowd11/finisher67/{PREREG.md,score67_r11.py,results_r11.json}`.
- **arm1248 (WO5): "peu" STRENGTHENED 4/8; infinitive-class 3/7
  WEAK-FENCED.** P-A PASS: **13** genuine "pour peu que"+subjunctive in
  the new pool (11 RdM, 2 Guizot-DIP incl. Palmerston/Aberdeen
  contexts) — every hit constituency-read, 0 artefacts; no longer
  hapax-anchored in the broader 1841 record (v8 L1 stays failed). P-B
  PASS: clause-shape S=(verb-offset 3, clause-length 4); PA-5 "pour peu
  que cette lutte dure encore" matches exactly; modal offset-3 in 5/13.
  E-A PASS (massively): **28 DISTINCT** genuine infinitives in "pour INF
  que" (49/52 genuine); "empêcher" re-attested ×2 incl. EA-39 in
  Eastern-Question register (ne-explétif + subjunctive). Fails: E-B/E-C/P-D
  (0 everywhere). The sharper exposure: the double-pour stack "pour 33 16
  pour 67 que" has NO era license anywhere checked, for either arm; @471
  unhosted for both. The NEITHER-fence stands. Missing-leg inventory
  banked per arm (v8 L1, L4 closure, @471 host, stacked-pour license,
  n_eff=1). Trace:
  `code/crowd11/arm1248/{PREREG.md,arm1248_strengthen.py,arm1248_strengthen_results.json}`.
- **watch06 (WO6): all three falsifiers UNFIRED (round 11).** Census
  identical rounds 9–11 ([580,738,1184,1355]; n06=44, n82=39 — no parse
  drift). F66 @1184 fenced adverse re-audited, stays FENCED (both
  candidate parses require unbanked readings the islet excludes — a
  reminder that by-ear adverses must be checked against the conditioning
  they attack). FIRE-OUT coverage limitation honestly reported (1/40
  windows fully glossed — the ← leg is defended by anchor sparsity as
  much as by evidence). n_eff=3 fragility banked: one clean falsifier
  kills the islet. Trace:
  `code/crowd11/watch06/{PREREG.md,watch11.py,watch11.log}`.
- **smith-liaison (WO7): delta memo banked**
  (`code/crowd11/smith_liaison/smith-constraints-round11.md` — carries
  forward the round-10 memo, adds round-10 adjudication deltas). 3 GO /
  0 KILL / 0 scored comparisons (no results dirs on any track; no file
  newer than redteam/RULINGS.md); **10 islets in the registry**; 132/132
  R10BANK + 89/89 ROUND10-LEDGER PASS; main-fleet scope stays ZERO until
  C1.

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
  "première" anywhere (old parse; the repair later uncovered @754 — F12).
- **N10** — Scorer-smith r2 (syllable-level scorer): **BROKEN-ON-CONTROL** —
  tail-1200w Tocqueville t2, known random 96-cell syllabary, 9 anchors
  pinned: top-1 0.021 vs chance 0.076 (0.3×), MRR 0.133 vs 0.30 bar, 47 test
  words. Failure mechanism: placement ranking ties — every placement shares
  identical cells, only 1–2 edge bigrams differ; the language model itself is
  fine (true −3.12 vs shuffled −4.32). Trace:
  `code/crowd2/scorer_smith_results.json`.
- **N11** — Scorer-smith r3 (WO3 global-consistency redesign): **BROKEN-ON-
  CONTROL ×3 variants** — best top-1 0.091 (8.1× chance) MRR 0.165, best
  MRR 0.217 vs the 0.30 bar; real drag never ran. The consistency signal is
  REAL but USELESS (v1 median support(true)=1.00, yet wrong cells also hit
  1.00 — French bigram contexts underdetermine a cell). Joint engine
  control **FAILING** (annealed accuracy 0.05, islets 0/3 vs bars top-1
  ≥0.50 / islets ≥2/3 / margin ≥200 nats) — **identifiability problem, not
  model problem** (n=7 letter LM: truth −2.65 beats annealed −3.05). R5005
  gate holds — no real run. Trace: `code/crowd3/scorer_smith_results.json`,
  `code/crowd4/scorer-smith-joint.md` (inbox), `code/crowd4/run_r5005.py`.
- **N12** — Tuner (what do the contact phases mean): **NULL** — leave-one-out
  phase-constrained 2/34 vs unconstrained 6/34; phases are NOT word-position
  classes. The 'er' 67× segmentation mismatch (cipher 2.55% pairs vs corpus
  bare-'er' 0.038%) uncalibrates corpus-tuned "er"-rate ranking generally.
  Rotation itself re-verified (chi²=188.3, old parse; 366.3 repaired). Trace:
  `code/crowd3/tuner_results.json`.
- **N13** — 9-mer crib-drag (`56 69 26 00 33 21 64 37 01` ×2): **clean NULL**
  — top era candidate "seule différence qui existe" (×3) needs 00="fé", but
  00 is rank 1 (×54, 2.93%) vs era "fé" 0.19% → 15× too rare; also needs
  21="ce", colliding with provisional 87=ce. Trace:
  `code/crowd2/formula_tester_results.json`.
- **N14** — Slider pass 1 (sidepath): **VOID** — 174 real accepts vs 208.3
  control mean (801 control records); zero promotions, zero kills; loop
  STOPS after 1 of 5 passes per stop rule. Sharpest targets silent: all
  eight 62→94 "on ne" windows emit nothing; no W-47 sub-window clears
  S≥0.50. Control asymmetry noted: shuffling de-anchors windows, so controls
  accept MORE than real — conservative aggregate, weak for anchored
  windows. Trace: `code/sidepath/slide_pass1.json`,
  `code/sidepath/prereg_pass1.md`.
- **N15** — Pattern matcher (side-wordpattern): **HONEST NULL** — the
  ground-truth control fails: "première" tail @1035–1038 (FOUR GT anchors)
  returns ZERO candidates at every tier; the encipherer's by-ear units
  aren't in the lexicon inventory ('m' as syllable in 1/11,870 entries).
  "Unique survivors" are noise (0 with ≥2 GT anchors; only 4/11 survive the
  0.5→0.7 cut). The failure is the unit inventory, not the lookup —
  pattern-matching against French syllables is the wrong alphabet. Trace:
  `code/side-wordpattern/matcher/match_results.json`.
- **N16** — Polyvalence tester gate: **VALID-WITH-RESTRICTIONS** (forward
  survival 0.995 overall / 0.834 at-risk / 0.38 se-split; smart-expansion
  inflation ≤6× vs dumb 202–2318×; 52 at-risk words, 8 mechanisms; synthetic
  +30 islets repetition survival 0.879). Polyvalence is a scalpel, not a
  hammer — it distorts only where specific syllables co-occur in interacting
  positions (52/1,597 words). Trace:
  `code/side-wordpattern/polyvalence/POLYVALENCE_REPORT.md`.
- **N17** — Segmenter drag25: control PASSED (boundary recall@0.5=0.721≥0.60;
  internal<0.5=0.939≥0.70; mean diff 0.258≥0.10 — synthetic 621-word cipher
  with rotation + ear-cutting noise) → drag ran: **0 proposed, 25
  LEAD-held, 0 killed**. Under 62="on", zero era words fit any of the four
  62-touching MAP spans (12,108 Tocqueville words queried) — tension is
  likely MAP-span merge error (control M1=0.72 ⇒ ~28% miss), not a kill of
  62="on". Trace: `code/crowd4/drag25.py`, `code/crowd4/drag25_results.json`.
- **N18** — 87=ce register-matched subset FAILS its pre-stated bar
  (R=7/176=0.0398 vs A=40/958=0.0418 — the genre account doesn't close the
  cela gap inside Tocqueville; cela-leg stays dead); ci/te anchor scan NULL
  (34→G=0 for all 16 followers of 87). Trace:
  `code/crowd4/closer64_87.py`.
- **N19** — **Joint-engine objective bug (diagnosis reversed).** The
  "model-correct but search-broken" claim (N11) does not survive contact
  with the configured objective: truth key + E-step decode scores −2.65
  ONLY with lam_poly=0 (penalty disabled); on the actual search objective
  (lam_poly=10), **truth −32.64 vs annealed −2.91** — truth sits ~30 nats
  BELOW the "best" nonsense. The polyvalence penalty (10 nats/key-level vs
  per-letter-normalized letter term) makes v2 un-addable by construction
  (needs >~58,000 nats of letter improvement to pay for itself); annealed
  key ends n_poly=0, islet bar unmeetable. Even penalty-off, the letter
  7-gram alone prefers annealed (−3.11/letter) over truth (−3.64/letter).
  **The search optimizes correctly — the objective is wrong.** N11's
  framing compared truth-penalty-off vs annealed-penalty-on (apples to
  oranges). Second surprise: the round-4 control's own metric is partly
  unidentifiable BY CONSTRUCTION — lossy tail inheritance makes group 41's
  "true primary" 'ri' (emitted 1.8% of 274; modal 'mi' 2.2%, 160 distinct
  cells) unrecoverable by any likelihood method; max achievable top-1
  **0.90**; 2/20 bar groups are lottery tickets. Fix list: phonetic
  projection, spanning word bonus, concentration penalty ON (LAM_HOM is
  currently 0.0), homophone-pool/block proposals, per-stream chi2-gated
  phase, fix lam_poly scale first — model bug, not search tuning. Gate
  holds (no R5005). Trace:
  `code/crowd5/report_inbox/scorer-smith-identifiability.md`,
  `code/crowd5/scorer_identifiability*.py`.
- **N20** — Rotation linguistic mappings killed (all pre-registered,
  cipher-internal, F29-legal): morphological (T1b 13/38 formula edges
  on-cycle, binomial p=0.25; 06/86 mood contrast same phase B),
  polyvalence-conditioning (T2a p=0.44, T2d p=1.0, T2e p=1.0), unit-size
  (T3 p=0.80, direction reversed — phase-C cells LONGER); syntactic NULL
  (T4a 4/6 function words in phase B, p=0.0566 — misses the 0.05 bar,
  reported as null not support). Trace:
  `code/crowd5/rotation_mystery.md`.
- **N21** — 84="fait" KILLED on unigram (6.7×); 84 unresolved (bounded
  only); @1800 thread refined to 64-77-84-59 ×2 (n_eff=1). Trace:
  `report_inbox/processed/closer-87-new-angles.md` (this sweep).
- **N22** — 06 stem NULL (honest, accepted): 06→29 ×4 @1096/1388/1709/1815
  (verified); single-stem KILLED on rate — 45.98/1000w vs best "pri*"
  2.685 = 17.1× (audit-corrected); 67 et/veut fork: "et" beats "veut"
  114:1 post-infinitive in era → "veut" survives only as conditioned on
  67→78 "veut me" ×4 (unpromoted); "donner" conditional lead fenced (19×
  register inflation). Trace: `code/crowd5/morph47_06_results.json`,
  `audit_morph47_06.py`.
- **N23** — Side-homophonic frozen control (run2): solver **DEAD** —
  frozen seed 184101: primary=0.0000 (0/89), proj_equiv=0.0,
  secondary=0.1473 (≈ chance 0.1434), mrr=0.0262, islets 0/6, margin
  +15050.3 nats; frozen-ctl-184102: primary=0.0, proj_equiv=0.0225,
  secondary=0.1241, mrr=0.0169, islets 0/6. The frozen rerun of 184101
  reproduces 184101's numbers EXACTLY (reproducibility datum). D1–D4:
  objective misalignment (truth −6959.9 vs annealed +4127.4), the word
  scorer is the hole (overlapping hits outscore real text 15×),
  polyvalence runaway (n_poly 49–60 vs truth 6), inventory gap (6/96
  primaries absent; ceiling 0.933). Gate holds — no R5005. Trace:
  `code/side-homophonic/runs/{RUN-REPORT.md,control_report.json files,
  frozen_batch.log}`.
- **N24** — Scorer-smith identifiability FINAL: route (a) proves search is
  NOT the bottleneck — PT gbest −2.88/top1 0.05; basin test 9 descents all
  walk AWAY from truth (ends −2.47..−2.90) — no basin; route (b) proves
  the search works given constraints — b1 reaches truth's neighborhood
  (−33.54..−33.56 vs ceiling −33.43, within 0.13 nats; top1 0.35–0.40, 4×
  baseline); b2 (conditioned polyvalence) honest negative (0/15, 0/3
  islets — control-vs-reality gap documented). The disease: lam_poly=10 is
  ~100× over scale (truth beats annealed only at lam_poly < 0.09) and the
  letter 7-gram alone prefers annealed over truth (−3.11 vs −3.64/letter).
  Traceability flag on the .md's basin denominators (see F51).
  Trace: `code/crowd5/scorer_identifiability.{py,md,json}`.
- **N25** — 62="on" non-ear battery: NO PROMOTION — honest null: on≈il
  tie on clean pieces (Δ=+0.27 nats); H-split calibration VOIDS the old
  "il"-kill and the merger corroboration; one four-ways-caveated adverse
  datum for "on" (p=2.6e-4 — adverse, not kill-grade, not a demotion);
  the profile route is proven unbridgeable with the current inventory
  (no 62 cell both mappable and discriminative with n≫2). Ranked
  unblockers: qu'on whole-word cell, l'-cell, impersonal-verb cell,
  48/98/16. Trace: `code/crowd6/frenchman62/`.
- **N26** — 96 conditioned-verb battery: **UNVERIFIABLE** (honest null) —
  the "ce qui __ ce que" frame is a hapax (1/1,847); conditioned readings
  on n=1 are unfalsifiable (F33-grade conditioning requires a verified,
  falsifiable rule). 20/21 other 96-frames clean "par"; era "ce qui"+verb
  213/213. 47="ce" promotion stays BLOCKED. Trace:
  `code/crowd6/morphologist/battery96_67_results.json`.
- **N27** — Phonetician CV-structure: **NULL on all 6 subtests**
  (open/closed p=0.2500, tier p=0.3465, sonority p=0.7752, n=16; T-Pa2
  p=0.0242 fails the pre-registered Bonferroni 0.0167; T-Pa3 p=0.0687,
  T-Pc2 p=1.0 — red-team re-derived 6/6 to <1e-6, R-1). The third
  granularity where phases refuse linguistic meaning (position →
  morphology → fine phonetics); the null tightens the table-geometry
  fence, doesn't touch E1. Trace: `code/side-rotation/phonetician/`,
  `code/side-rotation/redteam/RULINGS.md`.
- **N28** — Geometer WO1/WO2: **NULL** (executor-grade, pre-red-team) —
  number-range (WO1a p=0.569, WO1b p=0.883, Cramér's V 0.14/0.09);
  homophone-cycling (94 p=0.809 powered, 52 p=0.219, 06
  untestable/vacuous, non-vacuous Fisher combined p~0.48; the literal
  3-way p=0.036 manufactured by the vacuous 06 component NOT claimed);
  WO3 clerk simulation **0/6 behaviors pass screening** (no behavior
  reproduces M1/chi²/M2z/M3/ARI — screening-level, K3's joint DEAD bars
  untouched). Trace: `code/side-rotation/geometer/wo{1,2,3}.json`.
- **N29** — Rhythmicist HMM-vs-bigram: **no decisive HMM win**
  (executor-grade) — held-out bigram −4.2938 vs HMM-3 −4.3774/pos (bigram
  wins; ΔBIC=+59824.3 but the pre-registered conjunction requires BOTH);
  a second split replicates (−4.2356 vs −4.2638). P2b FALSIFIED
  (2nd-order Markov −1.2189 vs 1st-order −1.2143/pos on held-out — no
  genuine memory-2). Trace: `code/side-rotation/rhythmicist/
  hmm_results.json`, `code/crowd6/segmenter/{rotation_r6.json,hmm_test.json}`.
- **N30** — Rhythmicist WO1b labeling-robustness: **FAILED as stated**
  (executor-grade) — only 1/5 fresh-clustering variants survive (Jaccard
  k=16: chi²=354.9, z=+4.71, agree 0.948); cosine, k=8, and both
  half-stream clusterings die (z=+0.51/+0.20/+0.28/+0.23; agreements
  0.344–0.458). The rotation's structure is robust under one clustering;
  its membership is fragile — as claimed, quantified. Trace:
  `code/side-rotation/rhythmicist/robustness_results.json`.
- **N31** — Rhythmicist WO2 pre-registered tests: **VOID by construction**
  (honest catch, pre-computation logic error): phase is a deterministic
  function of group, and exact-repeat phrases share their start group —
  "all occurrences start on the same phase" holds with probability 1, so
  Tests A/B/C test nothing. Post-hoc salvage (6 distinct formula starts
  all in {B,C}: H1 p=0.0093, H2 p=0.034, H3 p=0.049) is descriptive only —
  post-hoc, no claim, no promotion. Trace:
  `code/side-rotation/rhythmicist/phaselock_posthoc.{py,json}`.
- **N32** — Period-drag T1/T2/T3/T6/T8 NULLs + memo frame corrections
  (executor-grade, pre-red-team; all nulls anchor-preserving, N34): **T1**
  ("Monsieur le Baron"/"Mon cher Baron" @0): NULL — 47={ce} islet blocks
  cell4; releasing the islet makes the fit vacuous. **T2** ("Votre dépêche
  du"/"J'ai reçu votre dépêche du", 0–150): NULL — 25/7 windows fit but
  ALL anchor-free (nulls 0.68/0.32); unconstraining fits, not evidence.
  **T3** (é-noun after "la première" @754/@1034): NULL — entrevue 0 fits
  (killed @759 by 94="ne" prov-strong, killed @1039 by 77=le; survives IFF
  94≠ne — an override of prov-strong); expédition 0 fits (same two
  kills); épreuve fits @759 ONLY ([e,pre,uve]/[e,preu,ve], 244/11,870
  nulls — unconstraining), killed @1039 by 77=le; @1039 admits only
  [e,?,le] words (13 fitters: elle/égale/école…), none a memo candidate.
  Alignment-B inversions: @760 n_fit=4 (défense/dépense/dépensé/offensé —
  no discrimination), @1040 n_fit=7 (élément/parlement/nullement… — no
  grammatical noun phrase). **T6** (tail closings, 1800–1846): NULL — all
  candidates fit only at anchor-free windows (nulls 0.32–0.68); tail
  inversions: nothing closing-shaped ("considération/distinguée/Adieu/
  Tout à vous/haute considération" all vacuous). **T8** (treaty
  double-surface): NULL — "le traité de Londres" 8 windows (null
  30/11,870 = 0.25%), "le traité du 15 juillet" 6 windows (null
  21/11,870 = 0.18%); the two surfaces share 6 windows — not
  discriminated; no second anchor in any phrase window. Memo frame
  corrections: the memo's "R1a followed by 77=le (sentence break)" is a
  RAW-FRAME ARTIFACT (absent from every canonical parse); memo R2
  `06 77 78 18 71 10 01` @raw1429 is 0× in the repaired stream — the
  "06|77|78 = ent le gou" cross-check cannot run (VOID). **T5 phrase:
  NULL** — the full "par le dernier courrier" phrase fits @465/@914/@960
  but the placements imply MUTUALLY INCONSISTENT assignments (le→00 vs
  09; der→33 vs 02) — no joint phrase; structural datum: **96→77 is
  0/21** — the memo's 96|77|… shape never occurs. Trace:
  `code/crowd6/period_drag/{results.json,t7_anchored.json}`,
  `code/crowd6/report_inbox/period-drag-t1-t8.md` (this sweep).

**The red-team demotion (the lane's most consequential null).** Attempt 2
scored 87="ce" CONFIRMED 4/5. The red team reproduced every count, then
voided the scorecard: check (b)'s "P(cela|ce)=0.278" was **n_cela/n_ce — a
count ratio, not a conditional**. The honest syllable-level bound is
P("la"|"ce"-syllable) ≤ 0.1805, and the observed 0.2188 *exceeds* it
(check void); checks (a)/(d) also passed for the refuted de/à
(non-discriminating); check (c) is n=3. Demoted to provisional/plausible.
No alternative beats "ce" — the kill failed on alternatives and succeeded
on scorecard integrity. Round-2's F13 dissolution and round-3's rival
  elimination (F19) strengthened the reading without re-promoting it; round-4's
  register FAIL (N18) killed the last statistical leg (cela). The reading
  now stands on ear-corroboration and rival-exhaustion, with kill authority
  held by the red team.

### Rounds 8–10 kill batch (adjudicated 2026-10-07; NOTES.md F60–F76)

- **N33** — 48="ne"-allophone **REFUTED** (crowd8/homophonist, kill-grade
  F60): merged word-rate 4.78× > 3× bar; "ne ce que" @863 (46="que" GT)
  + "en ne ce" @1657–1660 adverses; −0.585 nats predecessor fit. 48 never
  enters the status line; H_verb/H_stem tested separately in round 9.
- **N34** — 93="l'" ALONE **rate-KILLED** (crowd8/frenchman, F61):
  n=14 vs diplo E=31.26, exact P(X≤14)=4.1e-4, holds in every diplo slice
  (v8 strict E=32.9, p=0.0003). Rescue: {93,8}="l'" unconditioned
  homophones → LEAD.
- **N35** — 86=que-family **REFUTED** (crowd9/conditioner, kill-grade
  F65): «pour qu'» 21× over, «pour que» 9.2× over, «qu'pre/qu'pas/qu'plus»
  impossible at 7/32 windows, 77-86 ×5 at era P≈0.00007, profile parity
  fails (Jaccard 0.33/0.25). 86's value NULL; F40 verb-stem-class stands
  as working hypothesis.
- **N36** — Unconditioned 59="est" **REFUTED** (crowd10/conditioner59,
  kill-grade F71): 8 independent adverses incl. @463 «la est» era-0
  (0/3.96M). F52's provisional REFINED into ISLET 10 (59=word-«est» iff
  pre∈{64,94,93}; 59=verb-final «-este» iff pre=84).
- **N37** — H4g 94-82-06-06 4-gram refinement **REFUTED by the prereg's
  literal formula** (crowd10/watch06, F72): executor p_comb=0.0410 used an
  un-licensed method; recomputed under the literal formula p_comb=0.0508
  > 0.05 → REFUTED (knife-edge 0.0008 — the bar is the bar). Closes as
  post-hoc coincidence, NOT "untestable-at-n=2".
- **N38** — 48=H_verb (conjugated verb) **KILLED** (crowd9/successor48,
  F64): K2 fired — 0/2 "48 pas" windows ne-licensed (span-robust) AND
  predecessor verb-licensing 31.6% < 40% bar; steelman denied as
  post-hoc rescue. H_stem UNTESTED (cosine 0.387 < 0.60, n96=21
  underpowered — explicitly not adverse).
- **N39** — 48=S-word class **KILLED for 30** (crowd10/syllabicist48,
  F75): structural pincer — "la" (GT) takes nominals, "on" (fenced
  STRONG LEAD) takes verbs; no single French word at 2.06% follows both;
  kill survives loss of 62="on". F76 EV1–EV9 individually veto
  48={à,a,es,et,il,les,te,un,se,des}; 48="de" CONDITIONAL (narrow
  pronoun+infinitive path); 48="com" NEUTRAL (fragment).
- **N40** — Refuge concretizations ALL DEAD (crowd8/segmenter, F63):
  four syllable classes run through signature + recoverability —
  momentum z=−65…−112, ARI≈0 vs random nulls; schema survives only
  LOGICALLY-OPEN-NO-EVIDENCE; full kill needs key recovery (standing).
- **N41** — 67@1248 finite-verb third arm **vetoed era-0** (frenchman Gate
  4, F67/F76): zero finite verbs in «pour X que» middles on every corpus
  (the lone «dit» 1/4.2M is a past participle). cela-arm REFUTED on
  substance (F73: v8 «pour cela que»×3 never bare constituents;
  bare-constituent count = 0). Médiatrice-class DEAD (0 legs).
- **N42** — **Honest-null battery:** 67's 6 residuals 0/6 classified
  (crowd10/finisher67, F74); 62 on/il battery 0/4 (crowd9/resolver62,
  F69); este-verb ID H0 holds (crowd11, round-11, unadjudicated).
  Round-8–10 net: 0 promotions, 3 lead-tier status refinements
  (Mehemet-Ali→LEAD-weak; 59 provisional→conditioned ISLET 10; 16="i"
  stays unconditioned LEAD, B1-redirect exhausted), scoreboard 12 values
  (7 GT + 4 provisional + 77="le"
  provisional-conditioned). Baselines: 132/132 + 89/89 PASS.

---

## 6. Open hypotheses (not promoted — each needs ≥2 independent checks)

- **62="on"** — FENCED-LEAD (STRONG LEAD, promotion DENIED by red team,
  Ruling 1; round-6 non-ear battery: NO PROMOTION, honest null — N25):
  leg-2 re-derivation 62→94 **×9/35=0.2571 (1.62× era with
  ne+n'-forms)** — supersedes the old ×8/34; third leg = fresh-window
  subject-triangulation @848 ("00 33 [par] e 62 21 67 91 51" → "…par
  écrit, on me [dit]…", 21="me" established without 62, no circularity);
  34/34 windows compatible, zero counterexamples. Denial reasons: leg 1's
  subject premise is ear-derived and undisclosed (instrument
  contamination); the il-differential p=0.041 is assumption-maximal (the
  same ear merges /kil/); unigrams favor "il" (1.50×) and "qui" (1.77×)
  over "on" (2.59×); Check C χ² **invalid as reported** (3/4 cells
  expected<5 — exact MC p=0.0450, 0.0675 minus recycled ne cell; profile
  fits "il" equally, exact p=0.0386). Round 6 tightens the fence: the
  cipher-internal H-split calibration (46→29 ×2 "qu'er", never before
  /i//e/) **VOIDS both the "il"-differential and the merger
  corroboration**; on clean disjoint pieces on≈il (joint −26.54 vs −26.82,
  Δ=+0.27 nats); one four-ways-caveated adverse datum for "on"
  (46→62=0/29, E=7.18, p=2.6e-4 — adverse, not kill-grade, not a
  demotion); the profile route is proven unbridgeable with the current
  inventory. New fence: "on-vs-il discrimination needs a non-ear
  resolution the current inventory cannot supply." Ranked unblockers:
  the "qu'on" whole-word cell, the l'-cell ("l'on" test), an
  impersonal-verb cell, 48/98/16. Round 8 adds two non-ear legs
  (crowd8/frenchman — F61): L_B 46→62=0 (LR=**21.3** for "on" via
  qu'-elision rate asymmetry, M_hom-independent) and L_A (conditional on
  M_hom: (93|8)→62 ×4 vs diplo l'+il=0); 62="il" → DISFAVORED-STRONG
  (conditional, not fully killed). Round 9 (crowd9/resolver62 — F69):
  N35 independent-cell battery **HONEST HOLD, 0/4** (C1 p_two_il=0.072
  sub-bar lean — no quiet upgrade; C2/C3/C4 null; C1–C4 banked
  tested-NULL); @100 "62 ne l'est" fenced n=1 descriptive, zero leg
  weight. The Mehemet-Ali/@1248 blocker is NOT lifted. Trace:
  `code/crowd5/frenchman62_leg3_results.json`,
  `code/crowd5/redteam/rulings.md`,
  `code/crowd6/frenchman62/battery62_results.json`,
  `code/crowd8/frenchman/results.json`, `code/crowd9/resolver62/`
  (this sweep).
- **78 three-way (WO1 adjudicated)** — "me"-WORD **disfavored-strong**
  (L1w 22.76×, audit-verified; no formal kill); "me"-SYLLABLE holds LEAD
  (L1s 1.131× in-band, F29-letter clear); **78={ver,er} fork**
  (downgraded from 78="ver" conditioned islet, crowd7 redteam — F61:
  the "ver"-specific evidence was contaminated; the 554 "vernement"
  era tokens are ALL "gouvernement*", morphemically gouv|erne|ment —
  the worker's ver+ne/ver+re binary never tested the live er+ne
  alternative; the "≠me" core stands; n_eff=1). **COEXIST —
  neither kills the other.** The N11/N14-era adverse (77→78 ×7) was a
  category error (word "me" tested against a syllable bigram) — dissolves
  under the syllable reading. **Round 9 (F66): H3a NEW WEAK LEG for
  tine (c)** — er|ne boundary productive (52 tokens/22 types) vs ver|ne
  zero genuine common words (**10.4×**, Fisher p=**3.2e-11**, pre-registered
  bar passed; gouvernement-family excluded) — lean (c) strengthened, fork
  unresolved, lean (c) now has lexicon-lean + H3a + H3b (crib-inventory:
  (c) needs 1 novel syllable {gouv}, (a2) needs 2 {gou,ver}). @1351–1356
  era-frame: @1180's frame is era-modal ("le"+gouvernement) but @1351's is
  era-anomalous both sides (H1c: "on" at L2 = 0/641; H1d: "le qui" =
  0/391,210). **Round 10 (F70): @1351–1356 resolved R-c** («le [78] ne
  ment pas») — the gouv parse is OUT at @1351; 78="ver" by-ear gloss
  @1352 dies (positional membership kept, next=94); fork {ver,er}
  UNRESOLVED. **Germanist watch-item (F68):** if a STANDALONE 78="er"
  window is ever found outside the formula, German "er" (= he/him)
  becomes a live rival to French er-final-syllable readings — flag then,
  not now. Trace: `code/crowd5/bigram78_77_578.py`,
  audit, `code/crowd7/report_inbox/redteam-f26-17-t4.md`,
  `code/crowd9/hunter7778/{h1_h2_h4.py,h3_fork.py,h3a_results.json}`,
  `code/crowd10/resolver1351/` (this sweep).
- **77="le"** — PROMOTED → **provisional (CONDITIONED)** (F31): 77→86 ×5
  object-pronoun frame + verb-stem; adverses fenced ("ce le"×2, "le me"×7
  conditional, 4.07× overshoot); "gou"@1180/@1351 exception fenced
  (n_eff=1). **Round 10 (F70): 77="le" GAINS @1351** — the fenced "gou"
  exception existed only for the 5-mer; with R-b dead at @1351, 77@1351
  falls back to F37's conditioned default; the "gou" exception shrinks to
  @1180-only (untouched, out of scope). No re-litigation of F56's killed
  unconditioned {77,00}="le" merger (distinct from the conditioned
  reading). Trace: `code/crowd5/redteam/rulings.md` Ruling 2,
  `code/crowd10/resolver1351/` (this sweep).
- **47="ce"** — LEAD strengthened (F34): B1 0.996× exact (Wilson
  [0.037,0.272]); Q1 qui/que complementarity + Q2 fragment rule as
  F33-form conditions; C2 dissolved (F29-void); unigram 2.13/1.446;
  promotion blocked on @148–152 (unblockers: 96 conditioned-verb battery,
  fragment sound, diplomatic corpus). Round-6 WO-A battery: the ranked-#1
  unblocker is **UNVERIFIABLE** (N26) — the "ce qui __ ce que" frame is a
  hapax (1/1,847), and conditioned readings on n=1 are unfalsifiable;
  the parenthetical reading ("ce qui, par ce que 66 84, [V]") survives
  unfalsified-but-unverified (era "par ce que"=0, downstream verb
  unidentified). Promotion stays BLOCKED. 47 is NOT 87's "ce"
  (Jaccard(87,47)=0.435 but P(64|47)=0/28 vs era 0.188, binom p=0.0030 —
  bounds the reading).
- **67="veut"** — provisional; et/veut fork: "et" beats "veut" 114:1
  post-infinitive in era → "veut" survives only as conditioned on 67→78
  "veut me" ×4 (unpromoted). "la veut" @1044-1045 supports the pin.
  Round 6 (executor-grade, F48): the fork is **SUPPORTED as conditioned
  polyvalence (F33-form), NOT promoted** — 19/38 classified with zero
  cross-contamination (et-side 8 kill "veut", veut-side 11 kill "et",
  fork ratio 113.0); "la veut"@1044 pins a 3sg transitive verb, not
  uniquely "veut"; 19/38 open. The 7/11 veut-frames' pre=21 condition
  has a grammatical strain under the 21="me" lead ("me veut me" @1841 is
  broken) — this tensions **21's** value, flagged not resolved.
- **43="me"** — **WEAK** (downgraded from MEDIUM, round-6 executor-grade,
  F48): "par 43"×2 is n_eff=1 (byte-identical formula 64-96-43-87-01),
  era "par me"=0 — grammatical adverse; full inventory: supporting
  "me le"×2 (@258/@1305, 77="le" prov) + weak "que me"×1 + weak "il me"×1
  (88="il" unestablished) vs adverse "me ce"×2/n_eff=1 (formula), "la me"×1,
  "ce me"×1, "le me"×3 (conditional on 37="le" [MEDIUM]). Kill rule n≥3
  not met → no kill; adverses outweigh supports → WEAK. Round-9 (F65):
  **43="me" suffers a clitic-order adverse IN THE qui-96-43 FRAME** («qui
  [V] me» ungrammatical — object clitics precede the verb) — banked
  datum; 43="me" WEAK stands globally, not here. qui-96-43 ×2 formula
  HOLD (@341/@1025; not @1024 — shift verified). Cleanest repair
  remains conditioned polyvalence (43="me" iff pre≠96) or 43≠"me".
- **24** — unidentified: "en" strong (24→87 ×10 at 26–31× over era
  P(ce|en); "en ce qui"=24-87-64 ×2 kills "de" there); "tout" 1.6× weak;
  "est" **REFUTED** (19.5×/74× era kills; inversion sweep over 45 words:
  empty intersection); rival "c'est"/"sont"/"ont"/"de"/"en" all killed.
- **52="pas"** — LEAD vs "se"/"so" rivals, polyvalent: "pas" iff
  negation-frame (94_52 ×3 @571/1293/1806 + 94_70_52 @1331) vs "so"
  word-internal @160 ("per|so|nne"); @1741 "i ne m que" the single worst
  "ne" window (1/36, unresolved).
- **67="veut"** — provisional (veut-class): 67→33→29 ×3 ("veut parler");
  "les veut" 21→67 ×8 → *vouloir*; red-team-3 demoted its CONFIRMED →
  provisional (circular compat: 06→77 counted while 77="pas" under test).
- **67 et/veut fork (round-8–11 state)** — **SUPPORTED, fenced scope**
  (F67/F74, adjudicated; round-11 finisher/census33 unadjudicated):
  round-9: 29/38 classified standing; @1248 NEITHER-fence UPHELD (option
  (c); new finite arm declined with evidence; "pour * que" middles
  {cela:3, empêcher:1}; finite-verb arm era-0 vetoed — Gate 4 revised:
  bound = {peu}-class + infinitive only); @199 NEITHER-fence CONDITIONAL
  on 08="l'"; @630 et-CONDITIONAL (C1∧C2 explicit — not a
  classification); 6 open-residual (no ≥2-leg bar); R_veut4 dropped at
  design time ("me veut"=0). **Round-10 (F74):** 0/6 residuals
  classified — clean null; 29/36 classified; **decider for
  @1450/@1623: 33's class.** **Round-11 (recommendations, red-team
  pending):** census33 finds **33 = infinitive-class** (C1 PASS: three
  independent kinds — I1 pre==00 "pour" ×8 E=0.68 p≈0; I4 suc==29
  "-er" ×5 E=0.56 p=0.0002; I2 pre==67-veut@1423 ×1; zero GT-anchored
  nominal hits) → **lean-veut at @1450/@1623** (67="veut" stays
  provisional; fork's own history corroborates unprompted: "et 33-er" ×2
  @273/@1477, "veut 33-er" @1423–1425); finisher classifies 1/6 — **@633
  → et-CONDITIONAL (C1∧C2)** on the new left-conditioned frame "l' *
  et" vs "l' * veut" (v8 **92:2**, ratio 46:1; L2 n(11→52)=3);
  @1519/@1372/@902 null (31 contested verbal-lean; 92 contested
  verbal/nominal; no dense frames); @1450/@1623 open with the decider
  applied. **Tally if granted: 29 classified + 2 conditional + 5 open +
  2 fenced = 38.** Round-8 morphologist note: @1248 is a genuine fork
  counterdatum (bound, not kill — "pour et que"/"pour veut que"
  double-zero across 4.2M tokens; fork not universal at @1248);
  red-team upheld the fence. Germanist watch-item: if @1248's X ever
  resolves to "cela/ça", that is a "dafür daß" calque (evidence FOR
  German interference). Trace: `code/crowd9/finisher67/`,
  `code/crowd10/finisher67/`, `code/crowd11/{census33,finisher67}/`
  (this sweep).
- **59 — ISLET 10 (conditioned polyvalence), LEAD (round-10, adjudicated
  F71; the provisional F52 is REFINED, not killed):** 59=word-«est» iff
  pre(59)∈{64,94,93} (est-arm 6/6: «qui est»×3, «n'est»×2, «l'est»×1;
  rates in-band on Nesselrode v8: P(59|64)=0.0638 vs P(est|qui)=0.0852);
  59=verb-final «-este» iff pre=84 (este-arm 4/4: @1190/@1448/@1804
  firm, @1291 fenced). Proposed pre=06/{61,44}/86 extensions EXCLUDED as
  post-hoc (fenced LEAD sub-tiers, not rule members). **Unconditioned
  59="est" REFUTED kill-grade** (8 adverses incl. @463 «la est» era-0,
  0/3.96M). F52 caveat-3 dissolved (S4#1 @216 = «[06-59] que» verb
  parse). -este verb ID set-valued {manifeste 131, atteste 35, proteste
  20, conteste 19, déteste 23} (diplo counts /3.96M); reste EXCLUDED at
  «qui le» (intransitive); round-11 (unadjudicated): H0 holds — a3
  monovalence fails for every candidate (84 polyvalent across @1190 vs
  @1448/@1804, or different verb there); @1291 has a conditional
  discriminator (shares byte-identical 5-mer suffix [35,94,52,80,4] with
  firm @1804 → {manifeste, proteste} if verb-parse + 35=subject holds).
  S1 unigram preserved 1.07× (mixture, not excess). Trace:
  `code/crowd9/conditioner/islet_registry.md` (ISLET 10),
  `code/crowd10/conditioner59/{PREREG.md,ISLET10-PROPOSAL.md,classification.json}`,
  `code/crowd11/este_verb/` (this sweep).
- **00="pour"** — STRONG LEAD (executor-grade, pending red-team — F45):
  M1 governor frame (00→86 ×12 "pour [inf]" vs 00→06 ×0) + conditional
  rates + full rival sweep (à/de/en/par/dans/sur/avec/avant/afin/pendant/
  sans/après/et all killed); promotion blocked on rates (unigram 6.22×,
  "pour que" 3.85× — needs the diplomatic corpus).
- **84="en" vs 84=noun-class** — RESOLVED toward conditioned polyvalence
  (crowd8/9, F62/F65, adjudicated): 84="en" iff pre∈{82} (GT-anchored
  "m'en" @167, n_eff=1) ∪ pre∈{66,89} (conditional on CONFIRMED 66-class
  {noun, infinitive, nous/vous-type} and 89 noun-class — F65); the
  «qu'en» core is DEAD («qu'en» legs @310/@473 withdrawn: "qu'en en"
  era-0 0/4.2M; 24="en" holds locally; F53's stated rule falsified).
  **Noun identity NULL STANDS** (not one era-rate masculine noun: best
  pas 0.38×, fait 0.11× — 13×+ gaps); «qui le 84 est» ×2
  (@1447/@1803) is NOT article+noun — reads pronoun+verb → «qui le
  [verb=84-59]» ×2 lead, refined round-9 (noun+"est" dead at @1447/@1803;
  59="est"-as-word era-0 there, fenced n=2; bisyllabic-verb unit
  hypothesis-internal, needs unbanked 59 polyvalence → became ISLET 10).
  13 free windows: 4 EN-EXTENSION (conditional), 9 RESIDUAL (classified,
  no islet change). 84="en" frame notes: @391 en-lean n=1; @788 «s'en»
  conditional on unadjudicated 65="se"; @857 adverse-lean withdrawn
  (depended on killed 48="ne"); @1501 adverse-lean fenced (74="te"
  LEAD); @1189/@1290 en-lean («en est» era-real but subjectless frame
  strained); @1418 plain. Trace: `code/crowd8/conditioner84/`,
  `code/crowd9/conditioner/{census_results.json,era9_results.json,islet_registry.md}`
  (this sweep).
- **78-45="même"** — LEAD (executor-grade, pending red-team — F47):
  0.57× in-band with era locks ("le même" 87×, "même qui" 11×); @313 =
  "le même qui" (grammatical lock under 37="le" [MEDIUM]); implies 45/78
  homophony for one syllable (F23-consistent, untested). 45="me"-word
  disfavored-strong (not refuted).
- **Medium leads:** 37="le", 01="est", 56="plus", 17="fois"
  (weak). 21="les" weakened (21→64×2 era-zero under both 64-reads).
  43="me" demoted MEDIUM→WEAK (F48/F61 — has its own entry above).
- **16="i" (second i-group)** — LEAD, unconditioned (executor-grade —
  F55; crowd8/patternist F59-amended, adjudicated GRANTED): the B1-redirect
  position-conditioned alternative is NOT SUPPORTED (T1 Fisher p=0.9398
  in the wrong direction — S1 GT-only p=1.0; T2 "premier"/"première"
  frame vacuous — masculine frame 0 occurrences). The redirect is
  exhausted; 16 stays unconditioned LEAD on its B2/B3 legs; no
  conditioned rule exists. Caveat: T1's WI set leans on provisional
  values (bounded by the GT-only sensitivity, which also fails).
- **00="le" ×3** — NEW LEAD (executor-grade — F60): 96-00 "par le" ×3
  (@47/@465/@960, mutually consistent on 00="le"; null 64/11,870 = 0.5%
  @465). **TENSIONS F40 00="pour"** (flagged, not resolved) — a dedicated
  battery must adjudicate 00="le" vs 00="pour". Trace:
  `code/crowd6/period_drag/results.json`.
- **"Mehemet-Ali" @8** — **LEAD-weak** (DEMOTED from LEAD, crowd8/patternist
  — F59-amended, adjudicated GRANTED): **62-tension adverse** — the
  me|he|met|a|li tiling needs 62='a' vs lane STRONG LEAD 62="on"; zero
  len-5 me-initial tilings in the by-ear top-8 avoid /a/ on 62
  (conditioned-62 polyvalence dissolves it only at the cost of a new
  posit); **"mêleront"** (me|le|r|on|t) is a fully 62-compatible
  common-word rival (33/33 @8 fitters reproduce exactly; only ONE
  compatible with 62="on"). M2 (spelling/topicality) stands — demotion,
  not kill. **RdDM "293×" VERIFIED exact** (F59 UNVERIFIED flag LIFTED):
  293 clean-form 'Méhémet-Ali' in the 1841 RdDM 4-tome run (318 incl.
  variants; cite with OCR caveat); AZ German "Mehemed Ali" 75×
  (pronounced /h/ — under the German-thought premise the 'he' cell is
  by-ear; M3's purity adverse STRUCK, scoped to German phonetics — the
  general interference premise is NOT banked); "Mohammed" 15× = Dost
  Mohammed (formally excluded). Promotion blocked on 62="on"
  resolution (F69 blocker NOT lifted). Trace:
  `code/crowd8/patternist/{round8.py,round8_results.json}`,
  `code/crowd9/germanist/az_evidence.json` (this sweep).
- **T4 (c) "gouvernement"** — LEAD (red-team adjudicated — F61): tiling
  (c) gouv|er|ne|m|ent SURVIVES, (a) le|gou|ver|m|ent DISFAVORED; 94="ne"
  and 77="le" keep their status. (c)'s 77="gouv"/78="er" islets are
  n_eff=1 and need independent support before any promotion.
  **Round-10 update (F70):** the @1351 leg is gone — 77="gouv" is now
  @1180-only (n=2→1, no kill); 78="ver" by-ear gloss @1352 died
  (positional membership kept). Trace:
  `code/crowd7/report_inbox/redteam-f26-17-t4.md`,
  `code/crowd10/resolver1351/` (this sweep).
- **48 UNIDENTIFIED** (rounds 8–11; F60/F64/F75/F76, adjudicated;
  round-11 anchorer unadjudicated): n48=38 confirmed (predecessors 19
  distinct, successors 29 distinct/38 — repaired-parse correction).
  KILLED: 48="ne"-allophone (F60), H_verb conjugated-verb (F64 — K2:
  0/2 "48 pas" ne-licensed, V3 31.6%<40%), S-word class for 30 (F75 —
  structural pincer; F76 EV1–EV9 veto 48={à,a,es,et,il,les,te,un,se,des}
  individually). LIVE-RESIDUAL: **10 S-syl LEAD-weaks NOT granted as
  statuses** (rate-band shortlist datum only — de 0.66× … com 2.37×;
  mutually exclusive; S1 cannot separate them; "de" carries @1525
  tension vs 96="par" prov); **48="de" CONDITIONAL** (narrow
  pronoun+infinitive path: «de le»+INF 29/29 hand-verified; @1350 and
  @126 OUT, @1076 IN-PENDING — round-11 recommendation); 48="com"
  NEUTRAL (fragment). H_stem (96-family) UNTESTED (cosine 0.387 < 0.60,
  n96=21 underpowered — explicitly not adverse; the 0.40 signature bar
  miscalibrated: lane's own reference stem 06 scores 0.318). "on 48"×6
  association real (p=7.6e-05) but no verbal signature; "48 pas"×2
  statistically null. V1 generalized: «X pas»-bare era-0 for ALL word X
  — 48's escape must be structural (52-polyvalence, ne-merger, or
  fragment), not lexical. Trace: `code/crowd8/homophonist/`,
  `code/crowd9/successor48/`, `code/crowd10/syllabicist48/`,
  `code/crowd10/frenchman/`, `code/crowd11/anchorer48/` (this sweep).
- **{93,8}="l'" LEAD (unconditioned homophones)** (crowd8/frenchman —
  F61, adjudicated GRANT): joint n=32 vs diplo E=31.26 dead-center
  (p 0.47–0.60 all slices); free intermixing (shared pre {67,85,45},
  shared fol {52,29,62}); "ne l'est" @101–103; both cells pass B1 shape.
  93="l'" ALONE rate-KILLED (p=4.1e-4). Fenced costs: 93→52=2 / 8→52=1
  ("l'pas", era-0 — needs a vowel-initial third reading of 52; the
  (93/8="l'")∧(52="pas") conjunction vetoed per-window), 87→8=1.
  Rate-saturation corollary: 32≈31.3 leaves no room for fused l'V
  cells — caps the model space. Trace:
  `code/crowd8/frenchman/{s1_data.py,s2_allophony.py,results.json}`,
  `code/crowd9/frenchman/` Gate 1 (this sweep).
- **06="ent" iff pre=82 — ISLET 3, conditioned LEAD** (crowd8/frenchman
  F61 → watch06 rounds 9–11, adjudicated R1s): n=4
  (@580/@738/@1184/@1355), n_eff=3; F33-form with a banked falsifier.
  FIRE-PART/FIRE-IN/FIRE-OUT all unfired three rounds running; census
  identical rounds 9–11 (no parse drift). Coincidence probe P(X≥4)=
  0.0138, 4.31× (honest middle band — neither adverse nor "selection
  real"; one window from the fence). **n_eff=3 fragility banked as a
  standing caveat: one clean falsifier kills the islet.** By-ear: @1355
  now glossed «le [78] ne ment pas» (F70); @580 fenced admissible; @1184
  adverse-fenced (argues against the islet with a reading the islet
  excludes); @738 fenced (lone 82-06, no 94 prefix). H4g 4-gram
  refinement REFUTED (F72, literal-formula). Post-hoc observation: both
  suc=6 windows are islet windows (not scored). v8 register caveat: v8's
  54 "ment" tokens are OCR word-splits (phrase zeros void); «ne ment
  pas»=1 on the clean 3.96M diplo corpus (round-11 register check —
  attested, rare-but-real). Trace:
  `code/crowd9/conditioner/islet_registry.md` (ISLET 3),
  `code/crowd9/watch06/`, `code/crowd10/watch06/`,
  `code/crowd11/watch06/` + `code/crowd11/redteam/RULINGS-ROUND11.md`
  (this sweep).
- **96=verb-stem iff pre==64 & suc==47, LEAD at n_eff=1**
  (F55/F63, adjudicated): the WO-6 "second window before promotion"
  criterion is RETIRED (impossibility proof — singleton by
  construction). Promotion must come from adjacent islets or corpus
  legs. Adjacent-islet lead: **qui-96-43 ×2 formula** (45-64-96-43-87-01
  @341/@1025, diverge 06-70 vs 03-29; HOLD — classification denied per
  F33's no-post-hoc-expansion rule). 96="par" stays provisional
  (F44); the verb-stem reading is distinct from it. Downstream-verb
  hunt for the @151 parenthetical: null (round-7 null stands; diplo's 5
  "ce qui __ ce que" frames all verb-led, but the cipher's downstream is
  unidentified). Trace: `code/crowd8/morphologist/{prereg.md,results_r8.json}`
  (this sweep).
- **REFUTED (closed):** 24="est", 06="ne", 06=/mɑ̃/ (killed by GT mute-e),
  06="ent" general, H5 "J'ai l'honneur de" (82 is the GT 'm' cell),
  96="de", 77="plus", 77="ne"-swap, 06="de"/"le", 96="pour", 96="a/à",
  41="ter"/"mer", 64="même" (bounded), 78="me" promotion (rejected → LEAD),
  47="me" (word reading, hard zero), 01="ci", 84="plus" (via 59="est"),
  84="a", 84=verb-class. **Added this sweep:** 48="ne"-allophone (F60,
  kill-grade); 93="l'"-alone (F61, p=4.1e-4); 86=que-family (F65,
  kill-grade); unconditioned 59="est" (F71, kill-grade); H4g 4-gram
  refinement (F72, literal-formula); 48=H_verb (F64, K2 fired);
  48=S-word class ×30 (F75, structural pincer);
  48={à,a,es,et,il,les,te,un,se,des} word-readings (F76 EV1–EV9);
  67@1248 finite-verb arm (Gate 4, era-0); «pour cela que»
  bare-constituent (F73, 0/3); médiatrice-class (F73, 0 legs);
  «qui le [V] est»-as-word @1447/@1803 (F76 EV10); R_veut4 (dropped at
  design time, F67); the «qu'en» core of 84's condition (F62 — 46-part
  falsified); WO-6 second-window criterion (retired, F63); refuge
  concretizations ×4 (F63 — schema open-no-evidence); refuge
  columns-coda concretization (N43-flagged); {77,00}="le" unconditioned
  merger (F56).

---

## 7. Next steps (from STATE.md, round-5 work orders + adjudications, round-6 sweep)

1. **Refresh fig5** — superseded by item 16 below (rounds 6–11 rows
   still queued).
2. **Rebuild the skeleton ledger and repair the tester harness** on the
   1,847 parse (`code/sidepath/build_skeleton.py` asserts the old 1,846;
   `code/side-keyhunt/test_table.py` likewise). Still not done. Bedrock
   adds two more stale artifacts to re-run on the repaired parse:
   `code/crowd4/closer64_87_results.json` and
   `code/crowd3/morphologist_results.json` (both old-parse via
   `crib_attack.load_pairs`) — plus pin a rank convention.
3. **62="on" — promotion DENIED → FENCED-LEAD** (red-team Ruling 1);
   round-6 non-ear battery: NO PROMOTION (honest null, N25). The fence:
   on-vs-il discrimination needs a non-ear resolution the current
   inventory cannot supply. Ranked unblockers: the "qu'on" whole-word
   cell, the l'-cell ("l'on" test, era P=0.0619 vs 0), an impersonal-verb
   cell, 48/98/16.
4. **M1 accepted** (06 finite/imperative vs 86 infinitive-complement); 06
   stem single-reading NULL (honest, N22); 67 et/veut fork SUPPORTED as
   conditioned polyvalence (executor-grade, F48) — 19/38 open; 67@1045
   pins a 3sg verb, not "veut".
5. **47="ce" promotion blocked** on @148–152: the ranked-#1 unblocker
   (96 conditioned-verb battery) is **UNVERIFIABLE** (N26 — hapax
   1/1,847); remaining unblockers: fragment sound (Q2), diplomatic
   corpus; or a second "ce qui __ ce que" frame.
6. @578 trigram host — **CLOSED** (revival thread buried; sixmer ×2
   @573/@1164 is a new prime crib-drag target, right edge {ne,en}).
7. **78="me" vs 78={ver,er}** — adjudicated: **COEXIST** (word reading
   disfavored-strong, syllable LEAD, {ver,er} conditioned fork —
   crowd7 redteam downgraded the "ver" islet: contaminated evidence,
   F61). Adjudication done. New: 78-45="même" LEAD (executor-grade, F47).
8. 77="le" — **DONE** (promoted → provisional, conditioned).
9. **Objective repaired, search broken — scorer repair COMPLETE, control
   FAIL** (F58): steps 0/0.5/1/2/3/4 all landed — N36 re-derived exactly,
   F() history bug repaired (0.75 nats/letter), lam_poly calibrated
   (LAM_POLY=0.05, guardrail), phonetic projection imported, D2-repaired
   spanning word bonus, concentration penalty LAM_CONC=3.58e-4 (raw-cell
   cap 3). Full control: C1 PASS (truth −1.4274 > annealed −2.4116, gap
   0.98 — the objective is repaired), C2/C3/C4 FAIL (primary top-1 0.000,
   islets 0/3, pins 7/7 margin 0.92<1.0). **Gate holds: NO R5005 until a
   control passes.** Next: stronger search (block moves, longer anneal,
   population-based) or a less aggressive projection — the search cannot
   navigate the projected landscape with single-group moves. The
   side-homophonic-rebuild closed independently (F59): pilot FAIL
   confirmed by an independent verifier (salad beats truth by 2,601
   nats; primary 1/89 chance-level), aggregate gate CONTROL-FAIL; its
   Goodhart narrow-claim is refuted but the conclusion stands — reruns
   only on FRESH seeds.
10. @754 vs @1034 — **DONE** (F36). Follow-ups: 59=verb banked
    (GT-anchored; now 59="est" STRONG LEAD, F44); pin 67="veut" → partial
    (verb pinned, not "veut" — F48); adjudicate 43 (fence pre=96) → 43
    downgraded MEDIUM→WEAK (F48); 17="fois" @1040 stays WEAK.
11. **87=ce new angles** — A1/A3 legs landed (F35); 84 split
    **UNRESOLVED** (84="en" vs 84=noun-class, both LEAD — F46); round-7
    work order: conditioned-polyvalence battery for 84 (pre∈{46,94,82}
    vs pre∈{77,11}); the "s'en" alternative — if 77 carries a "se"-islet
    in exactly the 77→84 frames, E4 falls to 2.70× instead of 141×
    (falsified by any 77→84 window incompatible with "se", or positive
    "le" evidence inside those windows); pursue the 01="est" joint (A1's
    "c'est" count touches both 01="est" and 59="est").
12. **Rotation mappings** — linguistic mappings killed/null (N20, N27);
    **column-geometry (arbitrary-column form) KILLED by the rotation-fleet
    synthesis** (F54 — four independent legs: WO3 generative 0/8, K1 NULL,
    K2 NULL where powered, contact-clustering structural falsification);
    red-team adjudication of the underlying executor results still pending.
    Surviving threads: the 3-state HMM's unsupervised phase-like states,
    the untested-linguistic-class refuge (needs key recovery). The rhythm
    itself stands — real, partition-dependent, unexplained: a constraint
    on the key, not an explanation. **Segmenter round-6 follow-ups (F57):
    labeling-robustness FRAGILE by bar but excess global under fixed
    labels; HMM loses held-out (−4.2638 vs −4.2356), wins BIC; 69/96 vs
    61/96 reconciled; the P2c CONFLICT is now resolved in favor of the
    rotation fleet — the segmenter's sequential-mechanism probes (P2a
    momentum support) stand, but "one global column order" is falsified.**
    Instrument flag from memo3 (F62): the unsupervised contactor χ² is a
    noisy detector (0/6 in-band on synthetic controls) — no argument may
    lean on the exact χ² magnitude; phase MAPPING is ~0.5 purity — per-group
    phase arguments demoted unless independently supported; rhythm EXISTENCE
    (label-free lag-3 z=+5.6) NOT impugned.
13. **Round-6 red-team review DONE via round 7 (F61)** — F26-17: 12/13
    marks upheld (61/61 new + 49/49 baseline checks PASS); N44 corrected
    (net 0/2/0/1: two LEAD-tier elevations, one demotion 43="me"→WEAK);
    T4 either/or RESOLVED ((c) "gouvernement" LEAD survives, (a)
    disfavored). Outstanding round-7 work orders: conditioned-polyvalence
    battery for 84 (pre∈{46,94,82} vs pre∈{77,11}) [item 11]; 00="le" vs
    00="pour" battery (F60 tensions F40); "Mehemet-Ali" @8 battery (F60);
    F38 {ver,er}-fork follow-up — test the live er+ne alternative the
    worker's binary never tested; aliasing inversion via
    phase-conditioned contact profiles (F62 round-7 work order); the
    rotation mystery inverts only with key recovery.
14. **Traceability flag RESOLVED (executor-grade)** — the round-6
    scorer re-ran the full 105-descent basin battery and reproduced the
    .md's denominators exactly (3/105: 1/15, 2/30, 0/60 — F56); the
    archived crowd5 JSON holds only 9 descents (1/3, 2/3, 0/3), which
    explains the original flag. The 105-descent record now rests on the
    round-6 re-derivation (`code/crowd6/scorer/step0_baseline.json`).
15. **Rounds 8–11 complete (2026-10-07)** — 0 promotions across all
    three rounds (bar held the 8th/9th/10th rounds); adjudicated net:
    ISLET 10 registered, 7 kill-grade refutations
    (48="ne", 93-alone, 86=que-family, unconditioned-59, H4g,
    48-H_verb, 48-S-word), @1351–1356 resolved R-c, refuge schema
    open-no-evidence. **Round-11 recommendations await red-team
    adjudication:** este-verb H0 (set stays), anchorer48's 3 fences
    (A/B/D with @1076 in-pending), census33's C1-infinitive (→ lean-veut
    at @1450/@1623), @633 et-CONDITIONAL, "peu" 4/8 strengthened /
    infinitive-class 3/7, watch06 all-unfired (granted R1). Round-12
    work orders: adjudicate the round-11 packages; tie-break ISLET 10's
    -este verb (T1–T5); cipher-side suc2=infinitive ID for the 48="de"
    narrow path (@1076); red-team-approved veut-arm bar for
    @1450/@1623; pool re-run of @471/P-C for @1248 arms; keep the 06
    falsifier watch standing (n_eff=3 — one clean falsifier kills the
    islet); Smith round 2 remains rebuild2-side (main-fleet scope ZERO
    until C1).
16. **Fig5 refresh still queued** — the board list in
    `code/make_report_figures.py` is hardcoded through crowd rounds
    1–5 + sidepaths; rounds 6–11 rows (62 battery, redteam F26-17, T4,
    bedrock, F60–F76, ISLET 10, @1351, @1248 arms) require editing the
    `board` list and re-running exactly as documented. **Not done this
    sweep: fig inputs in `data/` (attempt1–3_results.json, quadgrams,
    Gutenberg texts, upstream R5005 files — all mtime ≤12:32 today) are
    unchanged since the PNGs were built (16:09 today), so no figure was
    regenerated — the underlying data did not change.** Figs 1–4/6 are
    current; fig6's χ²=366.3 annotation carries the memo3
    noisy-detector caveat (F62).

**Blockers:** R5006–R5008 NOT obtainable (operator registered `alexrivers`
on de-crypt.org 2026-10-07, but full-size images need admin elevation —
**external acquisition ON HOLD per the operator's 2026-10-07 directive**;
no HStAD scan order, no DECODE elevation request without his word); no
1840s Saxon key published; the erased pencil decipherment needs
UV/multispectral imaging (physical access, HStAD); archive channels
(Gallica/Hathi/archive.org) variously blocked from the VM.

**Standing convention:** every executor leaves a report note at
`code/crowd<N>/report_inbox/<name>-<topic>.md` per REPORTING.md (swept into
REPORT.md every 2h). Red team reviews ALL promotions before merge — no
claim merges without its ruling. Do NOT promote anything without ≥2
independent checks.

---

## Appendix — file inventory

```
zeschau-seebach-1841/
├── REPORT.md                  ← this report
├── REPORTING.md               ← inbox convention
├── NOTES.md                   ← full methodology log
├── STATE.md                   ← status / checkpoint / next / blockers
├── report_inbox/              ← worker notes land here; processed/ after sweep
│   └── processed/             ← folded into REPORT.md (70 notes total:
│       63 prior + 7 rotation/doctrine/overwatch notes this
│       sweep, plus crowd-local processed/ dirs next to their inboxes)
├── report_assets/
│   ├── fig1_frequency.png         group frequency rank chart (1,847 pairs)
│   ├── fig2_bigrams.png           anchor-adjacency bigrams (repaired parse)
│   ├── fig3_position_map.png      "la première" ×2 (@754/@1034)
│   ├── fig4_era_comparison.png    era vs Les Mis rates
│   ├── fig5_verdict_board.png      attempts 1–3 + crowd 1–4 + sidepaths
│   └── fig6_contact_structure.png 3-phase rotation, repaired phases (chi²=366.3)
├── code/
│   ├── crib_attack.py             attempt 1 (3 phases)
│   ├── attempt2.py                bigram-hypothesis tests
│   ├── attempt3.py                era corpus + H3 64="qui"
│   ├── make_report_figures.py     figure generator (this report; 1,847-parse)
│   ├── crowd/                     round-1 executors (phonotactician … linguist)
│   ├── crowd2/                    round-2: closer, context_miner, formula_tester,
│   │                              hypothesis_sweeper, red_team, scorer_smith
│   ├── crowd3/                    round-3: bigram_closer, closer(87ce), frenchman,
│   │                              morphologist, red_team(+round3b), scorer3,
│   │                              segmenter, stem_hunter, tuner, battery
│   ├── crowd4/                    round-4: battery4, closer64_87, frenchman4_62,
│   │                              morph94_re_battery, drag25, stem47_06, red_team,
│   │                              repaired_parse.py, phase_map_repaired.json,
│   │                              REINDEX.md, joint_engine.py, syllabary4.py
│   ├── crowd5/                    round-5: bigram78_77_578, morph47_06,
│   │                              frenchman62_leg3, closer87_angles,
│   │                              window754_1034, scorer_identifiability
│   │                              (F51 FINAL), redteam/ (verify_baseline.py
│   │                              31/31, rulings, audits)
│   ├── crowd6/                    round-6 (EXECUTOR-GRADE, pre-red-team):
│   │                              bigram_closer (77="le" exploit: 84=NOUN,
│   │                              59=verb, 45, "le me"×7 dissolution),
│   │                              closer (WO-A 84="en", WO-B 00="pour"),
│   │                              frenchman62 (62="on" non-ear battery),
│   │                              morphologist (battery96_67: 96-battery,
│   │                              67 fork), scorer (PREREG repaired
│   │                              objective — results pending),
│   │                              segmenter (rotation_r6: thread-4 P2a/P2b/
│   │                              P2c, HMM thread-2), inventorist (by-ear
│   │                              word sweep: 434 spans, 27 crib-proposals),
│   │                              period_drag (T1–T8 117-card drag; T4
│   │                              shape HIT, T5 00="le"×3 LEAD, T7
│   │                              "Mehemet-Ali"@8 LEAD), redteam/
│   │                              (verify_baseline.py 49/49; F26-17 review
│   │                              landed via crowd7 — 12/13 upheld, N44
│   │                              corrected, T4 adjudicated)
│   ├── crowd7/                    round-7: redteam/ (RULINGS.md,
│   │                              verify_f26_17.py — F26-17 review + T4
│   │                              either/or: (c) "gouvernement" LEAD,
│   │                              (a) disfavored; F38→{ver,er} fork)
│   ├── crossfleet/                cross-fleet memos (memo2-oversplit,
│   │                              memo2-rotation-partition, memo2-conditional-
│   │                              canonical, memo2-period-corpus,
│   │                              memo3-homophonic-rotation-findings:
│   │                              χ² noisy-detector flag + contact-coherent
│   │                              aliasing, F62)
│   ├── side-period/                era/register-matched corpus
│   │                              (Nesselrode, Guizot, Talleyrand, Metternich,
│   │                              RdM 1841, AZ Augsburg Jan 1841, Levant);
│   │                              cribs.md (121 cards) +
│   │                              cribs-adjudicated.md (117 survive,
│   │                              3 killed — F63); miner.py, syllabify.py
│   ├── side-homophonic-rebuild/   sealed-control rebuild: control/
│   │                              (7 synthetic instances, chance baseline),
│   │                              solver/ (METHOD.md, REBUILD.md), metrologist/
│   │                              (FINDINGS.md, sealed-pclasses), pilot/
│   │                              (rebuild-pilot-final result.json), verifier/
│   │                              (CLOSING-VERIFICATION.md — pilot FAIL
│   │                              confirmed: salad beats truth 2,601 nats;
│   │                              R2 attribution corrected; Goodhart
│   │                              narrow-claim refuted/conclusion upheld;
│   │                              fresh 6-instance batch + q0 ablation
│   │                              standing ready, unscored)
│   ├── side-homophonic-rebuild2/  round-2 fleet (NEW, pre-registered):
│   │                              FLEET-CHARTER.md; track-a (register-gap,
│   │                              PREREG+ref built, rescore pending
│   │                              red-team sign-off), track-b (neural
│   │                              char-LM, PREREG submitted), track-c
│   │                              (boundary-aware, building decodes);
│   │                              redteam/ kill authority; NO R5005
│   ├── bedrock/                   independent verification lane: BEDROCK.md,
│   │                              verifier_a.{py,json}, verifier_a_ledger.md,
│   │                              verifier_b.{py,json}, verifier_b_ledger.md,
│   │                              redteam_adjudication.md
│   ├── side-rotation/             rotation fleet: prereg_falsification.md
│   │                              (K1–K5 battery, written before results),
│   │                              prereg_{phonetician,geometer}.md,
│   │                              phonetician/ (CV-structure NULL 6/6),
│   │                              rhythmicist/ (WO1b/HMM/WO2, redteam_verify),
│   │                              geometer/ (WO1/WO2/WO3 — unruled),
│   │                              redteam/ (RULINGS.md R-0..R-4,
│   │                              agreement_reconciliation.md)
│   ├── sidepath/                  Slider (pre-registered), skeleton ledger,
│   │                              phonetic_rules.md, redteam_sla.md
│   ├── side-keyhunt/              Petit Chiffre table, parse repair
│   │                              (repaired_offsets.json), tester harness
│   ├── side-wordpattern/          lexicon, pattern matcher, polyvalence tester
│   └── side-homophonic/           gating control suite (CONTROL-DESIGN.md);
│                                  runs/ (frozen batch: RUN-REPORT.md,
│                                  control_report.json per seed,
│                                  frozen_batch.log; AGGREGATE-GATE.txt +
│                                  CONTROL-VERDICT.json = CONTROL-FAIL,
│                                  primary mean 0.0019)
└── data/
    ├── upstream-*.{txt,json,py,md}   Bourdeau transcription + solvers (hashed)
    ├── french-quadgrams.json        letter-quadgram scorer (shelved)
    ├── gutenberg-17489-miserables1.txt   Les Mis reference (superseded)
    ├── gutenberg-30513/30514-tocqueville-t*.txt  era reference (current)
    ├── PROVENANCE-tocqueville.txt
    ├── SHA256SUMS.txt             authoritative hashes (trust over §2 table)
    ├── attempt1_results.json
    ├── attempt2_results.json
    ├── attempt3_results.json
    └── historical-context/
        └── french-petit-chiffre-doctrine.md  1690 homophone mandate,
            word-family packing, petit-chiffre tier grammar (F42)
```

Anchor key (ground truth vs provisional vs leads, used throughout):

| group | value | status |
|---|---|---|
| 11 | la | pencil crib (ground truth) |
| 70 | pre | pencil crib (ground truth) |
| 82 | m | pencil crib (ground truth) |
| 34 | i | pencil crib (ground truth) |
| 29 | er | pencil crib (ground truth) |
| 40 | e | pencil crib (ground truth) |
| 46 | que | pencil crib (ground truth) |
| 87 | ce | provisional — best-tested, cela-leg dead (F19); round-5 A1/A3 legs (F35) |
| 64 | qui | provisional — re-promotion blocked (F9/F20) |
| 96 | par | provisional — conditional on 87=ce (F18) |
| 94 | ne | provisional-strong — "re" disfavored, "en" islets (F21); @578 thread closed |
| 06 | verb-stem class | provisional — stem unidentified (F22/N22); M1 06/86 rule (F33) |
| 67 | veut-class | provisional — red-team-demoted; "et" rival 114:1 (F22) |
| 77 | le | provisional — CONDITIONED (gou exception fenced) (F31) |
| 62 | on | FENCED-LEAD — promotion denied (Ruling 1); ear-contingent gap |
| 78 | me (syllable) | lead — L1s 1.131×; "me"-word disfavored-strong (L1w 22.76×) |
| 78 | {ver, er} | lead — conditioned fork (downgraded from "ver" islet;
contaminated "ver"-specific evidence; "≠me" core stands; n_eff=1) (F61) |
| 52 | pas | lead — vs "se"/"so" rivals (F23/F26) |
| 24 | en | lead — strong; "est" refuted |
| 47 | ce | lead — polyvalent with 87; strengthened (F34); 47≠87's "ce" (F35); promotion blocked (N26) |
| 59 | est | STRONG LEAD — executor-grade, pending red-team (F44); 1.39×, "n'est" n=324; adverse 59→37 ×6 at 6.47× (fenced on 37="le") |
| 00 | pour | STRONG LEAD — executor-grade, pending red-team (F45); 00→86 ×12 governor frame; blocked on rates (6.22×, 3.85×) |
| 84 | en | LEAD — executor-grade, pending red-team (F46); sole survivor; promotion BLOCKED on "l'en" 141×/63× |
| 84 | masculine noun | LEAD-grade — executor-grade, pending red-team (F46); identity NULL; **conflicts with 84="en" — unresolved** |
| 78-45 | même | LEAD — executor-grade, pending red-team (F47); 0.57×, "le même qui" lock @313 |

Banned (asserted-absent, from the skeleton ledger + adjudications):
77=pas, 77=que, 06=ent general, 06=/mɑ̃/, 96="de", 47="me" (word reading),
01="ci", 84="plus" (via 59="est"), 84="a", 84=verb-class. Fenced
(conditioned-or-dead): 43="me" (downgraded MEDIUM→WEAK — 96→43 "par me"
era-dead; F48).

*Rank convention: figure labels use 1-based positions in the frequency-sorted
list; lane code and NOTES.md use 0-based indices (figure #N = code rank N−1).
Parse convention: 1,847-pair repaired parse; old-parse indices ≥773 shift +1
(see `code/crowd4/REINDEX.md`).*
