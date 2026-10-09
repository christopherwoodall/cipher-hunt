# Seebach Cipher — Lane Report

**Status: UNSOLVED.** DECODE R5005 (18 Jan 1841), a two-digit French syllabary,
3,764 digits / **1,847 pairs (repaired parse)** / 96 groups. Banked values:
seven ground-truth pencil cribs (11=la, 70=pre, 82=m, 34=i, 29=er, 40=e,
46=que) + ten red-team-promoted (87=ce, 64=qui, 96=par, 17=fois, 79=tout,
00=pour banked; 12="n", 48="e" letter-tier; 30="pas", 06="ent" conditional)
+ class-tier grants (31 VERBAL, 33 INF, 86 INF, 24 finite-verb, 32
verb-lexeme); provisional (59="est", 77="le"); leads (94="ne" strong,
78="ver", 39="/a/" allophone, 62="il" battery-level, 76=noun
battery-level, 52="pas"-old superseded, 43="me" WEAK). No decryption;
three attempts, eighteen crowd rounds, and six side fleets have produced a repaired
canonical parse (bedrock-audited, F41; offset-validated, 6 confirmed / 24
probable / 15 probable-weak / 25 unresolved, 2 flagged), a second "la
première" occurrence, a quantified conditioned-polyvalence model, and one hundred seventy-four
documented kills and nulls (N-series, plus grouped null blocks).

Lane: `lanes/zeschau-seebach-1841/` · Report date: 2026-10-08 ·
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

**19th-century French drama/comedy corpus (2026-10-09).** The lane
previously held zero drama texts — a corpus gap flagged by the
dislocated-demonstrative battery chain (see the corpus-linguistics
census program, wave-14 addenda). 29 new .txt files commissioned and
ingested 2026-10-09: Hugo ×4, Dumas ×5, Labiche ×13, Musset ×1, Scribe
×5, Vigny ×1 = 28 distinct plays (Hernani in two editions), 661,743
words (count computed at sweep time, not a PROVENANCE.md figure).
Provenance in `code/side-period/corpus/PROVENANCE.md` (families 9 +
wikisource-drama + comedy-extension + comedy-widercorpus): archive.org
scans via `curl -sSL` (plain curl returns zero bytes on the
dn*.archive.org redirect), fr.wikisource MediaWiki parse API
(transclusions expanded server-side), both with sha256 per file; raw
API JSON archived (`goals/cipher-hunt-cracking-lanes/hidden_files/`
for the drama and comedy-extension ingests;
`code/crowd17/next-token/widercomedy-ingest-raw/` for the wider comedy
ingest). Caveats: mostly post-1841 reprint editions (textual variance
vs 1841 performance texts unexamined); `scribe-verre-d-eau.txt` is a
1861-edition substitution (the 1841 subpage does not exist on
fr.wikisource); census runs must use one Hernani edition per play to
avoid double-counting (validated non-load-bearing by the edition-delta
battery). All works public domain.

---

END DRAFT

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

### Round-11 addenda (2026-10-07, crowd11 — executor-grade, ADJUDICATED 2026-10-07: docket CLOSED 7/7; net **0 promotions, 0 kills, 0 demotions**)

**Red-team docket closed 2026-10-07 (R1–R7, three sequential independent
adjudicators, no coordinator-applied bars).** Baselines extended in place:
132/132→**148/148** (R11BANK, 16 cipher-side checks), 89/89→**100/100**
(ROUND11-LEDGER, 21 status entries + 6 corpus drift guards). Grants:
**F77** (ISLET 3 survives; falsifiers unfired; census [580,738,1184,1355]
exact; n_eff=3 fragility banked; v8's 54 \"ment\" tokens are archive.org
OCR word-splits — v8 phrase zeros VOID; clean 3.96M corpus: «ne ment
pas»=1, rare-but-real); **F78** (smith-liaison delta memo BANKED);
**F79** (33=infinitive-class — I1 pre==00 ×8, I4 suc==29 ×5, I2 pre==67
×1; nominals ~zero; grade LEAN for 67=\"veut\" @1450/@1623; fork
SUPPORTED); **F80** (-este verb stays set-valued; a3-monovalence banked;
T1–T5 tie-breakers named); **F81** (\"peu\" strengthened 4/8 —
13/13 genuine \"pour peu que\"+subjunctive; \"empêcher\" weak-fenced 3/7;
double-pour stack era-0 in ~16.5MB); **F82** (@633→et-CONDITIONAL,
round's only classification; 38 tally; fork SUPPORTED); **F83** (48 stays
UNIDENTIFIED — three fences; ML-1/ML-2 missing legs explicit; @863 \"de
ce que\" follow-up pointer). Case law: caught prereg flaw disclosed with
the conservative outcome stands (R6); Watch06 H4g case law applied
twice more; @1244–1254 label correction (R5's \"@1244–1256\" was +2).
Honest instrumentation: 48 executor's v1 heuristic wrongly excluded
\"faire\" — caught, disclosed, repaired with an assert-enforced
hand-verified lexicon. Executor packages below were recommendations at
write time; the Rulings-Round-11 verdicts above supersede their
provisional language. Trace:
`code/crowd11/report_inbox/curator-round11-merge.md`.

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

### Round-12 addenda (2026-10-07, crowd12 — 13/13 ruled, docket CLOSED 2026-10-07)

**Red-team docket closed 2026-10-07 ~21:55 UTC (R1–R7) and REOPENED
~22:05 UTC for French-blitz R9–R13; 13/13 landed and ruled, no interim
kills, independent adjudication, no coordinator-applied bars.** Net:
**1 provisional-conditioned classification (31=VERBAL finite), 2 kills,
1 demotion, 1 permanent retirement.** Trace:
`code/crowd12/redteam/RULINGS-ROUND12.md`, `code/crowd12/report_inbox/`.

- **R1 identifier33 (WO1) — GRANT. Overall NULL: 33's specific infinitive
  cannot be named.** F-A FENCED (double-pour frame unlicensed; pool
  sharpening: second \"pour\" always infinitival in-pool vs cipher's
  67 et/veut-fork ⇒ \"pour 33 16 pour 67\" unlicensed); F-D FENCED-strong
  conditional on 96=\"par\"-prov (\"pour INF par [e-word]\" 0/3.96M pool;
  N28's \"par écrit, on me\" parse chunk-short 5-for-4); F-B/F-C/F-E NULL
  (F-E's v8 L-failure underpowered — P(v8-zero)≈0.44 under H0 is noise,
  not a fence). **The 33-value paradox is RECORDED as structural tension**
  (F79's I1×8 \"pour 33\"⇒infinitive vs I4×5 \"33 29\"⇒stem,
  unreconcilable under fixed substitution + F22 granularity; class grant
  survives either fork; resolution paths banked: stem/whole-word
  discriminator, suc-homophone hypothesis). Lead banked: **21=\"ce\"**
  (post-hoc, 1 check; F-E W-slot \"ce\" 14/29, demonstratives 62%;
  homophonic collision with 87=\"ce\"-prov allowed; rival 21=\"me\"
  ungranted). F-C \"00 33 79 80 06\" ×2 (@467/@1088) banked as
  replication datum (same unknown infinitive ×2), not an ID.
- **R2 veutleg (WO2) — GRANT. Second leg NULL — clean null at both
  windows.** 36 UNRESOLVED (0 nom / 1 vrb, bar needs ≥2; F72 case law),
  66 UNRESOLVED (1 weak nom / 0 vrb); era E1 PASS (31/59=0.5254≥0.50,
  independently re-derived byte-exact). **lean-veut stays LEAN; 67
  provisional; fork SUPPORTED.** The veut-arm subject bar
  (CLASS(P)≥2 distinct licensor legs; era subject-license ≥0.50) is now
  BANKED and reusable. Leads banked: L1 (\"pour 66\"×7, p=4.945e-07
  re-derived, zero article contacts), L2, L3.
- **R3 class3192 (WO3/WO4) — GRANT. 31=VERBAL (finite),
  provisional-conditioned** — 3 disambiguated verbal windows
  (@338/@1647 qui-relative + @1489 D-ce with est-ce confound killed
  window-locally at pre(87)=24≠59); conditional on C1 provisionals
  64=\"qui\"/87=\"ce\" + 08=\"l'\" lead; era leg E31-1 VOID (honestly
  disclosed). 92 **H-pre REFUTED** (mechanical: @683 cross-signature —
  NOUN-strong inside the POUR-arm); 92 **H-presuc FENCED** (n_eff=1 <
  ISLET-3 precedent); VERB-arm RECORDED as datum (92=finite verb iff
  pre∈{94,46}, n=3); \"-quière\" tension FENCED on 64=\"qui\"-word
  @290/@684 (cross-lane flag; 64=\"qui\" stays provisional-FAVORED).
- **R4 followup48 (WO5.5) — GRANT.** @1077→**@1078** prose label
  correction accepted (byte-exact: 77@1077, 78@1078). ML-1 OPEN —
  both sub-readings adverse under banked 64=\"qui\" (ML-1b/ML-1c=0 in
  v8+Levant); new missing leg ML-1' (identify @1079=64's value under
  \"de le voir ___\"; era 0 in both). ML-2 scope correction: verb-only
  framing too narrow — era L1 adj/noun/participle 16/29 (55%) majority;
  12 stays OPEN; ML-2' registered. @863 POINTER-ONLY for uniform
  48=\"de\"; **BANK-AS-LEAD: 48=\"de\"-cell in 48→47 (\"de ce\") frames**
  (F33-style, 10 genuine ≥ 2-bar). 48 stays UNIDENTIFIED; no fence
  lifted; no kill.
- **R5 rerun1248 (WO6) — GRANT. PC-1: new attestation-breadth leg —
  peu 4/8→5/9**: third distinct-lemma bare verb host \"il craignait peu
  que\" +subjunctive (\"craindre\"). **DP-1: EXPLICIT FENCE** — the
  double-pour stack is unlicensed in ~22MB era French at BOTH arms;
  stacked-pour family absent at ALL depths k=1..5 (one artefact
  corrected). @1248 NEITHER-fence stands; the asymmetry sharpens —
  \"peu\" keeps getting MORE productive the harder we look while the
  frame around it is unattested.
- **R6 este T1–T5 (WO7) — GRANT. H0 holds — the set does not narrow.**
  T1: no independent 84 stem ID (@146 «qui le 84-er»: \"conter\" is a
  different lexeme from contester; \"atter\"/\"déter\" are OCR/fragments
  non-words); T2 inconclusive (both «le» antecedents unidentified); T3
  COMPATIBLE-UNCONFIRMED (06=\"pro\"⇒proteste; @1190 not an ISLET-3
  window; @346 \"propre\" leg fails; global 06 screen rules out
  global-06=\"pro\"); T4 stays FENCED (17=\"fois\" strained, 35 role
  unresolved); T5 clean negative (second «qui le [84-59]» absent).
  @1291 stays fenced; conditional {manifeste, proteste} discriminator
  stays conditional. The executor declined a LEAD its bar would have
  allowed (@346) — conservative direction endorsed.
- **R8 French-blitz Mehemet-Ali — GRANT in part.** Variant PINNED as an
  adjudicated datum (the French house form); reading holds LEAD-weak,
  no upgrade; 62=\"on\"/62='a' tension FENCED (not a kill-threat);
  \"mêleront\" rival warrants a round-13 battery.
- **R9 gouvernement re-reader — GRANT in part. The
  \"gouvernement\"/\"gouvernent\" READINGS are KILLED at all 7 windows**
  (\"gouvernement\" thread DEAD); **77=\"gouv\" DEMOTED→disfavored**;
  78 fork leans \"er\" (corroboration); ISLET 3 corroborated (no
  upgrade); new 06-«ne»-allophone lead; @647 OPAQUE.
- **R10 première-noun hunter — GRANT. é-initial-noun theory RETIRED
  permanently** (dead twice over); \"la première fois\" @1034 GRANTED
  LEAD (three legs); 20=\"fois\" homophone battery warranted for
  round 13.
- **R11 59-frame mapper — GRANT. ISLET 10's rule HOLDS with no
  widening** (est-arm 6/6 clean); 59 provisional HOLDS; S5 adverses
  banked (1 full, 1 corrected — \"n'est le\"=8/10 the idiom, 2 genuine
  counterexamples, banked at reduced weight); F1-WATCH recorded with
  exact trigger; @825 candidate-grade; `code/side-keyhunt/canonical.py`
  tooling bug CONFIRMED but CONTAINED (obsolete 1,846-pair parse; zero
  round-12 or French-blitz contamination; round-13 WO: fix or retire).
- **R12 formulae miner — GRANT in part. \"par ce que\"×3 is
  corroboration-grade** (named GT-anchored formula — a single
  corroboration, NOT a second promotion leg; strict no-double-count);
  \"par le\"×3 corroborates (not strengthens) the 00=\"le\" islet;
  head/tail nulls recorded; @998 → round-13 conditioner WO.
- **R13 48 syntax battery — GRANT. Unconditioned 48=\"de\" KILLED
  (kill-grade, 10 clean kill windows — author claimed 11, @1212 demoted;
  v8-excluded verified)**; conditioned \"de ce que\" islet stays LEAD
  (R4×R13 convergence is corroboration, NOT a second leg — strict
  no-double-count); vowel-initial conditional constraint banked;
  ML-1/ML-2 unfilled, Path D fence sustained; 48 stays UNIDENTIFIED.

**Round-12 methodology case law (all binding):** est-ce confound repair
(consequency-read bigram attestations; kill the confound at the
window — the pre(87)=24≠59 pattern); v8 power (v8's 149 \"pour INF\"
underpowers rare-shape fences — pre-register pool-level license checks);
n_eff bar (islet claims cap at FENCED below ISLET-3's n=4/n_eff=3
precedent); veut-bar banked; stacked-pour family absence
(ALL depths k=1..5, ~22MB); label correction (@1078, not @1077);
French-blitz methodology caveat (R8–R10 ran without PREREG/bars/code —
computational claims need round-13 re-runs; only red-team-verified
items banked; replication/honesty are signals, not substitutes for
prereg); strict no-double-count (one observation is one leg);
v8 phrase-zero caveat (F77 re-verified v8-excluded — future phrase-zero
claims on v8-inclusive corpora must be re-verified before banking);
arm-membership correction (@1276/@1034/@1030 not 59 positions;
est-arm @103/@316/@559/@763/@1210/@1777; este-arm
@1190/@1448/@1804); tooling bug contained (canonical.py).

---

### Round-13 addenda (2026-10-07, crowd13 — council round; **ADJUDICATED:
docket CLOSED 2026-10-07 23:59 UTC — 21/21 rulings, 0 pending**;
KE1/KE2 kill experiments out of scope, adjudicated by the red-team
killer; all executor recommendations below were ruled before merge)

`code/crowd13/` — adjudicator/ + 7 executor dirs
(carry-classes, carry-rest, homophone-ab, homophone-cd, islet-audit,
kill-experiments, liaison, missing-mass, segmenter). All batteries
pre-registered before computation; counts re-derived from the repaired
1,847-pair stream; era on clean-diplo v8-VOID pools. **No verdict below
is merged until the red team rules.**

- **Systematic drag (council WO, `code/council/drag/`) — executed,
  executor-report filed.** Pre-registered (`code/council/
  systematic-drag.md`); tractable: inventory 66 s (3.45M pool tokens →
  45,060 candidates → 37,418 → 555 phrases + 55 seeds, 1,127 variants),
  main drag 4.4 s (555×≤3 variants × 1,847 positions), shuffle null
  88 s (20 seeded replicates), **total ~95 s** (plan said ~2 h).
  Positive control PASS: \"par ce que\" reproduced at @224/@952/@1526
  exactly (par=96✓ ce=87✓ que=46✓). Main drag: **9 hits, 0
  veto-sensitive** — 3 control + 6 new: \"le prince\" ×2
  (@1240/@1401, le=77✓ prin=81? ce=87✓), \"tout ce qui\" ×3 →24
  (@179/@1766/@1774), \"tout ce qui\" →79 (@1799, clean). Nulls: shuffle
  null [17,24,13,7,18,9,5,14,10,10,15,14,13,7,12,14,15,19,14,4], mean
  13.1, std 5.2 — **real (9) does NOT beat all 20 shuffles**
  (pre-registered bar not met; real 0.8σ below null mean); decoy null
  (122 anachronistic phrases) 0 hits — the bar is tight. **FDR estimate
  13.1/9 ≈ 1.4** → the 6 new hits are consistent with chance:
  **LEAD-grade docket items, not discoveries.** Tensions: \"tout ce
  qui\"→24 incompatible with 24=\"en\" STRONG lead (F31) — those 3 hits
  dead if 24=\"en\" holds; @1799 (→79) clean; \"le prince\" →81 no
  tension — 81=\"prin\" is a new lead. 0 hits contra any GT/provisional/
  islet. Register caveat banked: the remaining plaintext avoids the
  top-500 formulaic phrases, so \"pour [inf]\" rates from the
  formula-heavy pool may be register-biased (direction unknown —
  flagged, not corrected). Trace: `code/crowd13/../council/drag/
  {common.py,build_inventory.py,run_drag.py,drag_hits.json,
  null_report.json,inventory.json}` + `report_inbox/
  council-systematic-drag-report.md`.
- **carry-classes (round-13 class batteries for 33/31/92 + drag
  integration) — recommendations.** 33: **NULL (constrained)** — T2
  fires mechanically for \"savoir\" (n=2, unique argmax, pool∖v8
  3,867,332 tokens) but LEAN blocked three ways (savoir ∉ R top-10,
  bisyllabic + fork-incompatible under Fork-W, suc=21=\"ce\"-banked
  can't be \"-oir\" under Fork-S); F-D fence re-confirmed 0 on the
  disjoint pool∖v8 (conditional on 96=\"par\"). 31: **CONFIRM 31=VERBAL
  (finite) provisional-conditioned** — independent re-derivation
  byte-identical to round-12 (3 verbal / 0 nominal; D-ce=[1488];
  qui-relative @338/@1647). 92: **NULL (constrained)** — J-POUR fails:
  T_683 (\"pour X W qui\", v8)=0 ⇒ POUR-arm is not one whole-word
  infinitive; @683 corroborates the round-12 NOUN-islet verdict. Drag
  integration: no hit contradicts GT/provisional/islet (0 contra);
  banked — 81=\"prin\" carries a post-context adverse at BOTH windows
  (\"la pour\" ungrammatical after \"le prince\" — chance or a forced
  GT/strong-lead re-read); 79=\"tout\" (@1799, clean) is the first
  tail-gloss candidate for the \"pour X tout W\" F-C battery
  (round-14, gated on promotion). All status-neutral — adjudicator
  rules. Trace: `code/crowd13/carry-classes/`.
- **Homophone batteries (council WO2, Table Reconstructor sets) —
  recommendations; adjudicator has not ruled. F60's lesson held:
  contact similarity necessary, not sufficient.**
  - Set A {33,86}: **SPLIT — same class (verb stems), different
    values.** Distribution tests all pass (uniformity p=0.354
    re-derived exact; runs z=−0.29; marginals p=0.16/0.41) but joint
    (pre,suc) frames 95.6% disjoint (2/45 shared); interchangeability
    rejects both ways (86-in-33's-frames 1/11 p=0.0017; 33-in-86's
    0/6 p=0.031); pour-frame successors fully disjoint (p=0.0007).
    Under Fork-S: disjoint completions = different infinitives.
    Implication: 33's infinitive hunt runs on its 8 pour-frames alone;
    do not merge 33+86 windows. Contact sim 0.70 mutual.
    Trace: `code/crowd13/homophone-ab/` + `report_inbox/
    homophone-ab-setA.md`.
  - Set B {48,94}: **SPLIT (class-level) — same pre-verbal-monosyllable
    class, different values.** Marginally indistinguishable
    (uniformity p=0.908 near-perfect; runs z=−0.35; marginals p≈0.5;
    mutual NN) yet joint frames 98.5% disjoint (1/67 shared); 48
    depleted in 94's characteristic frames (0/10, p=0.00085); neither
    follows \"pour\" (0× both). The @863 \"de ce que\" islet is
    48-SPECIFIC (94 never precedes 47 in 37 windows) — evidence FOR
    48's own value, not against the split. 48 stays constrained to the
    ne-class, ≠ne. Trace: `code/crowd13/homophone-ab/` +
    `report_inbox/homophone-ab-setB.md`.
  - Set C {52,59}: **SPLIT.** -este arm (pre=84) exclusive to 59
    (0/27 vs 4/27, Fisher p=0.0555); 52's \"est\" frame battery 1/7
    clean (@1342 «qui est», era 904/3.6M), 2/7 ambiguous
    («n'est/pas [80]» @1294/@1807, pas-favored), 4/7 strained-or-fail.
    52 stays UNIDENTIFIED (weak est-arm lead only).
  - Set D {76,78}: **SPLIT.** 76 fits only the ver-INITIAL tine
    («le ver[…]» @833/@892/@969 — «le vers/verre»-type; 76→94=0×,
    zero er-support); 4/21 windows fail both tines («ne 76»
    @652/@1577, «ce 76 ce» @1273/@1275 opaque). 76 stays UNIDENTIFIED
    (weak ver-initial lead); 78 fork unresolved by this battery —
    but the «le»-frames favor ver-INITIAL for *both* 76 and 78,
    in direct tension with the er|ne diagnostic leaning 78=\"er\";
    possible 78 polyvalence (ver-initial / er-final by position),
    flagged, not tested. Solver constraint: do NOT tie 52↔59 or
    76↔78 as homophone pairs. Trace: `code/crowd13/homophone-cd/` +
    `report_inbox/homophone-battery-cd.md`.
- **islet-auditor (round-13 compositional battery — recommendations).**
  All 10 registry islets audited against the compositional thesis
  (4-part battery: lexical-bigram, residual, forced-context killer,
  homophone-cycling uniformity; islets 1–3 sanity re-verified).
  Recommendation: **5 of 10 islets dissolve into word/frame rules**
  (recommend WORD-RULE re-banking); **the 67 fork is the registry's
  ONLY true polyvalence** (keep SUPPORTED — 29/38 clean, zero BOTH,
  0/38 inside confirmed words, era et:veut 99–273:1); 66/89 are class
  rules, never polyvalence; 96-verb-stem an honest singleton
  (INCONCLUSIVE, keep LEAD); 86 que-family kill confirmed on the
  repaired stream (kill legs 12–16× adverse + 7 elision kills). 59:
  **monovalent «est»** — 93-59=«l'est» and 94-59=«n'est» are single
  orthographic words, 84-59 stems+syllable of one verb; word-«est»
  fails in every residual (settled); 84-59 at both ISLET-8 windows is
  one -este verb; the banked «qui le [V] est» falsifier did NOT fire.
  Numbers: 27 windows est=6/este=4/subtier=5; full 84 accounting
  25=5+9+8+2+1; naive classifier over-counts (est=7/subtier=7 — the S5
  and frame-forced fences are load-bearing). Enlightenment: ISLET 5's
  era leg is v8-dependent (clean pool: n=1 «ce qui X ce que») while
  its «ce qui par ce que»=0 double-zero reproduces without v8 — cipher
  evidence stands, era leg can't be re-verified in the clean pool:
  exactly why it stays LEAD. Trace: `code/crowd13/islet-audit/` +
  `report_inbox/islet-auditor-round13.md`.
- **missing-mass (round-13 WO-6 — inventory complete,
  recommendations).** Era syllable rates on the clean diplomatic corpus
  (14 French files, 3.21M words, 6.6M syllables, lane syllabifier
  reused) vs observed rates of the 12 identified cells on the repaired
  1,847-pair stream. **Decision: (1) NO identified syllable clears
  the flag bar — the missing mass is in uncovered syllables, not
  second cells for la/que/ce.** Deficit table: 11 strong deficits,
  all in zero-coverage syllables (u 3.0 cells, de 2.9, a 2.8, qu
  2.5→1.0 corrected, en/ne/les/te/et/ti ~1.1–1.3); identified cells
  run 2.9× hot in aggregate vs era. **~17 missing cells (range
  17–20) among the 84 unidentified groups, 0 for identified
  syllables.** (2) All 13 reconstructor §b sets re-verified as mutual
  nearest neighbors — but {33,86}'s phase column disagrees with both
  lane phase maps (reconstructor B,B vs maps A,B) → **{33,86} demoted
  to WATCH; {76,78} becomes the strongest surviving set.**
  (3) **Digit hunt: NEGATIVE — recommend retire** (0/8 digit-shaped).
  48 sim-to-94 = 0.643 (#1 unidentified neighbor, B/B); 52→59 = 0.557
  (C/C, n 27/27). Enlightenment: the 1690 splitting budget is NOT
  hiding behind la/que/ce — identified syllables are oversupplied, not
  undersupplied; unidentified groups are mostly FIRST cells for
  de/en/ne/les/te/et/ou/tion. Trace: `code/crowd13/missing-mass/`.
- **smith-liaison round-13 (WO8 — liaison only).** Round-13 DELTA memo
  banked (`code/crowd13/liaison/smith-constraints.md`): 12 board values
  (7 GT + 5 provisional; 77=\"gouv\" demoted; 59 provisional holds;
  77=\"le\" conditioned), the 10-islet registry UNDER-AUDIT flag,
  the 5 discriminating windows with round-12 amendments (@1351
  resolved to the 06-islet parse; @1248 NEITHER-fence + peu leg 5/9 +
  double-pour stack ERA-VETO; \"par ce que\"×3 GT-anchored formula),
  and the must-NOT-break list (unconditioned-48=\"de\" KILLED,
  gouvernement KILLED at all 7 windows, v8 phrase-zero VOID rule,
  strict no-double-count). **Rebuild-fleet execution state:**
  (1) **Track A H1 SUPPORTED — M_d=+2,200.68 nats, sanity +2,601.0
  exact**: register-matched training does NOT rescue truth; the LM
  family is the blocker, not the register. (2) **Track C v3 NULL-v3** —
  per-char gate failed (truth −6.74/char < salad −4.67/char): the
  salad's tiles are adversarially French word-forms; bigram terms can't
  see adversarial placement of real words (third honest null; SPS
  fallback logic corroborated). (3) **Track D Experiment 0 running —
  184101 SLIDE (dJ=+2,439.3 nats, hamming=86, rec=0.034)**: truth is NOT
  a local optimum under J with single-group moves; first datum favors
  Branch B (drop Stage 2, judge-guided ILS primary). The night
  converged three independent nulls onto one lesion: the objective
  LIKELIHOOD rewards the salad structurally (F57's \"failure is in the
  likelihood, not the weights\" — now triply confirmed). Track B
  training at upd=1950, held_ema=2.2655 (in progress); Track D step-4
  GO cleared (R8) but not executed; automated judge instrument NOT
  stood up (2,700-call gate blocked). Scope stays ZERO until C1 passes
  on the gapped family. Trace: `code/crowd13/liaison/` +
  `report_inbox/smithliaison-round13.md`.
- **word-segmenter (round-13 WO5 — executed).** Table Reconstructor
  Step 2: segment the repaired 1,847-pair stream with confirmed
  multi-cell words. **8-word list** (7 council + \"cela\" as flagged
  crowd5-standing bonus); all 8 banked counts/positions reproduced
  exactly (zero phantoms). **Coverage 72/1847 = 3.90%** (honest low —
  anchor points, not a tiling; must not be presented as segmenting the
  despatch). 32 segments, 29 usable (19 live + 8 live* + 2
  suspect-edge); hard veto-split budget 22 pairs (A+/A), soft 53 pairs
  (B/B*/C); tier split A+ 12 / A 10 / B 35 / B* 14 / C 4 pairs.
  Enlightenment: the consistency pass KILLED things — \"en cela\"
  (corpus 8× vs \"en ce la\" 0×) supersedes \"en ce\" at 3 of its 10
  windows; \"ment\" is a complete word only at @1354 (\"ment pas\") and
  @737 (\"ment pour\"); the drag's \"tout ce qui\" lead dies at 3
  windows against 24=\"en\" STRONG; \"le prince\"×2 vs \"cela\"×2 is a
  genuine unresolvable 87-membership ambiguity (byte-parallel windows).
  Trace: `code/crowd13/segmenter/` + `report_inbox/
  word-segmenter-round13.md`.

- **Carry-forwards (`code/crowd13/carry-rest/`, recommendations).**
  (1) **@1248 verdict**: PC-1 spot-check on `rerun1248_raw.json`
  re-reads genuine — "il craignait peu que M. Thiers se livrât…"
  (\"craindre peu que\" + subjunctive, new lemma beyond {importer, se
  soucier\}, OCR interruption doesn't obscure the frame); DP-1
  re-verified on 758k independent tokens (RDM-1841-q1 459k + Guizot-DIP
  299k): 0/0 both strict patterns — **recommend PERMANENT FENCE on the
  double-pour stack (both arms)**; the k=5 \"hit\" was \"être pour X …
  pour dire que\" (a purpose marker colliding with a different \"pour\"),
  which is why constituency-reading carries the fence. @1248
  NEITHER-fence STANDS. Evidence: `dp_verify_raw.json`,
  `carry_results.json` §D.
  (2) **48 follow-ups**: 74-class battery → OPEN (74 unlikely a verb:
  74→77 \"le\" ×2 @212/@1677 is a genuine verb-adverse, but
  provisional-conditioned-dependent; noun/adj/participle all
  compatible); **H_stem GAINS A LEG** — B1: all three
  stem+inflection windows (@1229/@1589 48→29, @1398 48→40) compatible
  on banked values, @1229 actively friendly (82=\"m\" elision forces a
  vowel-initial stem); B2: 13.3% (11,509/86,527) of clean-diplo -er
  infinitives parse by-ear as exactly [stem]["er"] (bar was 5%) —
  the two-cell split is a real French class; second "48-47-46" hunt:
  CLEAN NEGATIVE (@863 only; @1658=48-47-98). @863 islet stays
  conditioned-syllable LEAD. 48 remains UNIDENTIFIED — a leg, not a
  value. Evidence: `{a74,hstem,frame2}_raw.json`, `carry_results.json`.
  (3) **-este transitivity battery**: clean-diplo 3.6M census
  («le/l'»+V3sg, \"qui le/l'\"+V, V+\"que\", \"le\"+Vinf), every hit
  constituency-read — **atteste FRAME-BEST LEAD** (\"l'\"-object ×4
  genuine PLUS the only in-register «qui le V» token in the set:
  \"c'est lord Beauvale qui l'atteste dans une dépêche\", RDM-1841-q4);
  conteste licensed («ne le conteste [pas]» ×3); manifeste weak-for-frame
  (all 8 «le manifeste» are the NOUN; 3sg «le»-object = 0); proteste
  doubly-weak («le» 0/19; all diplomatic uses intransitive; dictionary-
  transitive + T3's «pro» lead keep it alive); déteste weak
  (masculine-«le» 0/11); **reste EXCLUDED** (intransitive; all 218
  «le reste» are the noun). T1/T2/T4/T5 → nulls; T3 → 06=\"pro\" stays
  LEAD-WEAK. H0 stays set-valued — the atteste lead rests on n=1 for
  the exact trigram (fragile); no second independent discriminator
  fired, so this is a LEAD, not a tie-break. Evidence:
  `frenchman_este_raw.json`, `carry_results.json` §E. Enlightenment:
  raw bigram counts nearly lied twice — «le manifeste»×8 were all the
  noun, «le reste»×218 all the noun — constituency-reading every hit
  is what made the battery work.
- **Round-13 red-team adjudication (docket CLOSED — 21 rulings, 0 pending).**
  Two sequential adjudicators ruled all 7 executor packages; every
  battery number was independently re-derived from the JSONs' own
  methods before ruling (Fisher one-sided-by-design accepted per
  prereg; binomials and z-scores exact; phase maps independently
  checked). Trace: `code/crowd13/adjudicator/RULINGS-ROUND13.md` +
  `report_inbox/redteam-round13-shift2.md`.
  - **First shift** — R-DRAG: GRANT-WITH-MODIFICATION (the 6 new hits
    are consistent with chance, FDR≈1.4 — recorded as items, not
    discoveries; "le prince" ×2 @1240/@1401 banked as one leg each
    toward 81="prin", new lead). R-CD1: GRANT — {52,59} SPLIT
    (class-mates, different values; 52 stays UNIDENTIFIED, weak
    est-arm lead only). R-CD2: GRANT-WITH-CONDITION — {76,78} SPLIT
    (76 stays UNIDENTIFIED, weak ver-INITIAL lead; 78 fork unresolved
    by this battery; possible 78 polyvalence ver-initial/er-final
    flagged, not tested). R-IA1–R-IA7: all GRANT — islets 10, 8, 1,
    2, 3 dissolve into word/frame rules (registry polyvalence entries
    retired; ISLET 1's 82-arm WORD, 66/89 arms FRAME); islets 6, 7 →
    class-constraint tier; **ISLET 4 (the 67 fork) is the registry's
    ONLY true polyvalence — SUPPORTED**; ISLET 5 INCONCLUSIVE (keep
    LEAD). R-CC92: GRANT-WITH-MODIFICATION — 92 NULL (constrained):
    J-POUR fails, T_683=0 on v8 ⇒ POUR-arm is not one whole-word
    infinitive; @683 corroborates the round-12 NOUN-islet verdict.
  - **Second shift** (4 packages that landed after first shift) —
    R-AB1: GRANT — **{33,86} SPLIT**: class-mates, different values
    (joint frames 2/45 shared; depletion binomials p=0.00174/0.03131;
    pour-successor Fisher p=0.00072); §b {33,86} PROPOSE **retired**;
    do NOT merge 33+86 windows downstream — 33's infinitive hunt runs
    on its 8 pour-frames alone. R-AB2: GRANT — **{48,94} SPLIT**:
    ne-distributed class-mates, different values (joint 1/67 shared;
    48 depleted in 94's char frames 0/10, p=0.00085); do NOT tie
    48↔94; 48 stays UNIDENTIFIED. R-CC31: GRANT — **31=VERBAL
    (finite) CONFIRMED** (byte-identical re-derivation; no status
    change beyond the round-12 grant). R-CC33: GRANT — **33 NULL
    constrained**: T2 fires mechanically for "savoir" (n=2, unique
    argmax, pool∖v8) but LEAN blocked three ways; savoir forbidden
    under both forks; the paradox is sharpened, not resolved.
    R-CR48: GRANT — 74-class OPEN (islet neither promoted nor
    killed; 74 verb-adverse 2×, adverse-grade); **H_stem GAINS A LEG**
    (B1+B2, leg only; ne-marginals tension recorded open — name the
    stem-before-verb construction or drop the leg); second
    "48-47-46" CLEAN NEGATIVE (@863 only). R-CR1248:
    GRANT-WITH-CONDITION — PC-1 GRANTED as leg (peu 5/9; craindre
    spot-checked genuine, OCR caveat); DP-1 PERMANENT FENCE on both
    arms (frame-unattested ~22MB+758k, k=1–5 absent — permanent,
    framed as unattestedness not ungrammaticality); @1248
    NEITHER-fence stands. R-CRESTE: GRANT-WITH-CONDITION — **atteste
    FRAME-BEST LEAD** (n=1 in-register «qui le V» trigram + 4×
    government; NOT a promotion — fragility flagged; PROMOTE bar
    stays ≥2 legs + stem-ID); T1/T2/T4/T5 honest nulls; T3 06="pro"
    stays LEAD-WEAK; proteste doubly-weak but not killed; reste
    excluded (not in H0). R-MM1: GRANT — **deficit arithmetic**: 11
    STRONG deficits sum 385.6 occ → 20.0 cells naive;
    fragment-corrected ≈330 occ → **~17 cells (17–20) among the 84
    unidentified groups, 0 for identified syllables**; v8
    sensitivity reproduces the direction; both prereg reservations
    discharged. R-MM2: GRANT-WITH-MODIFICATION — reconstructor priors
    **BANKED AS PRIORS ONLY** with an anti-promotion fence (48→ne P1c,
    52→est P1c, 76→ver/er P1, de-pool P2); **digit hunt NEGATIVE →
    RETIRED** (8 cells = rare-vocabulary).
  - **Baselines at close (both exit 0):**
    `code/crowd7/redteam/verify_f26_17.py` **237/237 PASS** (203
    pre-round + 34 R13BANK checks behind every round-13 adjudicated
    fact); `code/crowd7/redteam/verify_round7.py` **160/160 PASS**
    (133 pre-round + 27 ROUND13-LEDGER checks, status deltas + drift
    guards). Earlier BANK/LEDGER blocks untouched.
  - Caveats: (1) citation-convention corrections for first-shift
    rulings (substance unaffected): R-IA2 frame starts @1444/@1800
    (not @1445/@1801); R-IA4 96-00 third window starts @960 (not
    @961); R-IA7 @150 indexes the 96 cell (frame start @149). R13BANK
    uses corrected indices. (2) R-AB2's V1–V4 substitution battery as
    named did not land — test 8 (joint-disjoint ⇒ vacuous) is the
    honest equivalent. (3) H_stem's ne-marginals tension stays open.
    (4) atteste's LEAD rests on n=1.
  - Enlightenment (second-shift adjudicator): the joint (pre,suc)
    frame battery is the round's discriminator — distribution-level
    agreement proved necessary-but-insufficient twice ({33,86},
    {48,94}); contact similarity alone cannot carry a merge.
- **Kill experiments KE1/KE2 (`code/crowd13/kill-experiments/`;
  adjudicated by the red-team assumption-killer).**
  (1) **KE2-A: 46=que RE-DERIVED — adjudicated, 46=que keeps GT.**
  Gate met: 87=ce keeps ≥2 independent non-46 legs; 64=qui holds on 3
  non-46 legs. R1 follower-profile: cipher ranks (excl. banked cela
  bigram) 64→1, 46→2 vs era qui→1, que→2 — exact match; P(46|87)=0.094
  vs era P(que|ce)=0.117. R2 predecessor-profile: era \"ce\" is the #1
  predecessor of \"que\"; cipher 87 is #2 predecessor of 46; rate ratio
  1.85×. Two independent legs, nothing assumed — **the re-derivation
  is STRONGER than the lane's original case** (the predecessor leg was
  never run before). ISLET 10's dependency on 46=que STANDS (not
  conditional). Adjudicator's note: three pre-registered bars encoded
  false premises (the brief omitted the 11×7 cela follower; 64's
  28/28 diversity misattributed to 87; exact-zero rival rates came from
  the smaller Tocqueville corpus) — corrected transparently
  (documented in `ke2a_results.json` → `adjudication`); pre-registration
  doesn't protect against encoding the brief's omissions, which is
  exactly what the adjudicator's job is to catch.
  (2) **KE2-B: @1034 two-occurrence claim ROBUST** (first formal
  statement): no crib group has a banked conditioned reading; F33
  battery promotes nothing (best candidates n=1 singulars — @1034
  \"le la\", @1524 \"la la\"); 70/82/34/29 have byte-identical ±1
  contexts at @1034 and @754. The \"le la\" tension at @1034 is real
  (pool hits are OCR noise — \"bverrt\", \"uappelez\", \"conluli sion\")
  but n=1 and implicates 77=\"le\" (provisional-conditioned), not
  11=\"la\".
  (3) **KE1: INCONCLUSIVE — no STOP.** Adversarial M1+1flip over all 25
  boundaries in (2108,3453): max gold=2, never reaches the ≥3 reject
  bar (winner b*=2130: gold=2, implausible=0). The 68-offset model
  stands as a permanent caveat; the parsimony rider (70 params vs 1)
  still favors M1+1flip. **STATE.md conditionality (verbatim):
  "canonical parse is conditionally canonical on (a) the gloss
  line-tag AND (b) upstream's 70 EM offsets, 68 unvalidated."**
  The 68 unvalidated offsets remain the lane's largest unpriced risk.
  Caveats: clean pool is 3.45M tokens, not 3.96M (v8 excluded,
  tokenizer differences); KE2-B is structural-tested, not proven.

### Round-16 addenda (2026-10-08 UTC, crowd16 — next-token program; **16/16
beats merged, battery-adjudicated; 32 notes ingested**)

`code/crowd16/next-token/` — method: `streamkit.py` (canonical 1,847-pair
stream via `code/crowd6/redteam/verify_baseline.load_stream`; start-index
convention), contexts from `mk_context.py`. Each beat = one finder census +
one battery runner with pre-registered bars; all counts re-derived from
bytes. Ingestion log: `code/crowd16/next-token/seen-findings.txt`. Notes:
`code/crowd16/report_inbox/next-token-findings-*.md` (finder) +
`code/crowd16/report_inbox/next-token-*.md` (battery verdict). Status key:
GT = ground truth (pencil crib, banked); LEAD = ≥2 legs, not promoted;
fenced = kept as a residual, not allowed to spread; est-arm = the
"est" reading of 59; allophone = same value in different positions;
frame = a fixed word-slot pattern. Round-15 batteries (A1–A15) enter here
as status-from-notes — they were not yet in REPORT.md.

- **tout (79) — banked CONFIRMED.** n79=18. 4 compositional legs re-derived
  exact: @451/@1460 "toutefois" (17=fois banked), @460 "tout cela est"
  (87=ce, 11=la banked; 59=est provisional-conditioned — weakest leg, the
  only 59-dependent one), @1799 "tout ce qui [le…]" (`test_tout.py`).
  "tous"-range: 5-gram 00-33-79-80-06 byte-identical ×2 @466/@1087 (finder
  wrote 33-00 first — transcription error, corrected); lead-grade
  (rests on the 06="ent" LEAD, not a banked value). Inflection ≠
  polyvalence — the 67-sole-polyvalence law is undisturbed. Adverse
  weighed and fenced: 79-82-48 ×2 (@396/@1227) — the m-finder's "qui"+"tout"
  double-subject point is valid; A7's boundary parse is strained at both
  (qui-clause verbless). **2 fenced residuals for 79="tout" (2/18)**;
  banked value stands on the 4 compositional legs. Weak leg @496
  (79→88-47-11) HELD. @50 "tout [37]" feeds the 37 verb/adj fight.
  79→24=0, 79→46=0 (no "tout en"/"tout que" — determiner/adverb profile).
  Trace: `code/crowd16/report_inbox/next-token-{findings-,}tout.md`.
- **formula-tails (F-qui-par / cela / par-ce-que / toutefois tails) — F1
  strengthen; F3 12-lead; new 84 residual.** "cela pour" ×3
  (87-11-00 @74/@1242/@1403) — CONFIRMED as strengthening for banked
  00="pour" (no double-promotion). 84 hub: "le 84" ×7 legs are A15's own
  legs; **@146 is a NEW fenced residual (R3) for 84="on"** ([64,77,84,29,
  87,64,96] = "qui l'on er[29]…" — ungrammatical under "on"; joins R1 @1619
  "la on" and R2 @1664 "ne on"; 3/25, fence-grade). "entrepre[12]" LEAD —
  tail @340 [6,70,12] exact, 06-70 singleton @346, CONDITIONED on the
  06="ent" LEAD; 12's battery = verbal continuation of "entrepre-".
  20-paradox feed: @754 "la première [20]" (feminine-noun leg; with @667
  "pour [20]" from the pour-beat — two legs now). Nulls verified as
  stated (toutefois tails distinct; par-ce-que tails 4 windows, 4
  distinct tails — "parce que [clause]" too open to cluster). Trace:
  `code/crowd16/report_inbox/next-token-{findings-,}formula-tails.md`
  (`test_formulatails.py`).
- **ce47 (47="ce" positional allophone) — verification HOLDS; no value
  break.** Full 28-window census re-derived exact (`test_ce47.py`).
  Mirrors 87's frame inventory: 47→11 "cela" ×3 [269,357,498]; 47→46
  "ce que" ×3 [151,548,864]; 47→78 "ce [78]" ×5 [363,818,981,1104,1396]
  (+87→78 ×2 → "ce [78]" ×7 total — the 78-fork battery's frame).
  @548 positional break CONDITIONED (24="en" is a lead; "en ce que"
  parses; settled ground, re-flagged). @611 "ce le ce" stays FENCED
  (no second instance — no escalation). **29-47 ×4 CONFIRMED systematic**
  [22,422,1230,1590] — queued battery, not a break ("[stem]erce"
  word-internal test). **qui-47 ×2 → "se"-rival: strongest 47-rival on
  the board** [1271,1717]; "qui se [76/68]" natural IF 76/68 are verbal —
  if so, a "47='se' before verbs" positional amendment would be a
  second polyvalence → immediate red-team escalation (lane law: 67 is
  sole). 47→64 = 0/28 vs 87→64 ×5 CONFIRMED — recorded as a positional
  restriction ("never before 64"); the spec now has two exceptions and
  must NAME the conditioning rule next round, not list exceptions
  (weakest leg, self-critique). @864 "à ce que pour [86]" is a REAL
  adverse — against 00="pour", not 47 — handed to the pour battery.
  Queued: B1 76/68 verb-hood; B2 77 re-profile in 47-77 vs 87-77; B3
  29-47 boundary; B4 name the allophone rule. Trace:
  `code/crowd16/report_inbox/next-token-{findings-,}ce47.md`.
- **e (40="e" — GT; followers = word-boundary onsets) — E1/E2/E3
  confirmed; new battery targets.** "e 65 94" ×2 @686/@1711,
  byte-identical, and 65-94 occurs NOWHERE else ([687,1712] —
  exclusive collocation): "…ère 65 94…" ×2. **65 is the single
  highest-value unknown** (top "-ère" follower 3/9, "65 qui" ×3,
  "21 65" ×4 — full-profile battery queued, priority 1). "20 62 94"
  ×3 @760/@839/@1703 ("la première [20-62-94] est…"); **62's dual
  selection: 62-94 ×9 AND 62-48 ×6** — 62 takes BOTH members of the
  ne-distributed {48,94} pair ("on ne" ×9, "on [48]" ×6; load-bearing
  for the 62/84 collision battery). "67 77 81" ×4 @743/@1239/@1400/@1597
  CONFIRMED — fork-conditional 67="et" vote (4/4 read "et le [noun]";
  "veut" strained), not a global fork resolution; 81's "prin" reading
  dead, 81 returns to NULL. 08 battery queued (08-31 ×3 @881/@1488/@1520
  "08 [verb]" vs @60 "[08]ière" spelling-letter pull — genuine fork,
  not forced). @848 fenced mild adverse for 96="par" ("par e", 96-40
  ×1 globally). Trace:
  `code/crowd16/report_inbox/next-token-{findings-,}e.md`
  (`test_e.py`).
- **er (29="er" — GT; 45 windows) — "se"-allophone LEAD; discrepancy
  KILLED; 86-stem LEAD.** 29 is joint-top predecessor of 47 (4/28,
  tied with 76); 29-47 ×4 [22,422,1230,1590], 29-47-33 ×2 [22,1230]
  re-derived. **47="se" after infinitives — LEAD, competing frame for
  the 47 battery**: "se"+infinitive ("faire se + inf", pronominal
  infinitive) beats "ce"+[inf] head-to-head, but both strained.
  Taxonomy refined (corrects ce47's escalation clause): "se"-after-
  infinitives vs "ce"-after-par are COMPLEMENTARY (disjoint contexts) =
  allophony species — NOT polyvalence; the 67-sole law is not violated.
  **E9 discrepancy KILLED:** 46-85-29 = 0 globally; @95 is 46-29-85 —
  the que/ce finder's "46-85-29 deliberative infinitive @95" is VOID,
  do not cite. 29-40-65 ×3 [291,685,1710] LEAD: finite-verb frames
  ("qui [V]ère [65]", "considère/préfère"-shaped) — the stem battery
  must not assume every 29 is an infinitive ending. 29-80: fork
  CONFIRMED (@1155 determiner-clean vs @1031 "[inf] [80] le la" broken;
  80-distribution battery queued); **@1031 fenced adverse for 77="le"**
  ("[verb]-le la" unless enclitic+break — 77's promotion battery must
  resolve it). 86-29 ×4 [431,1375,1391,1825] — **86 infinitive-stem
  LEAD**. 67 fork corroborated both directions (@274 "veut demander",
  @1389 "[inf] et [86]-er"). No masculine "premier" (0× — consistent
  with the i-beat). Null-stem anomaly queued: 46-29 ×2 [95,217]
  ("que-er" stays anomalous), 11-29 ×2 ("l'er[reur]"-shaped lead for
  11-29). Trace:
  `code/crowd16/report_inbox/next-token-{findings-,}er.md`
  (`test_er.py`).
- **est (59="est" — provisional, ISLET-10 conditioned) — headline
  correction CONFIRMED: 37 and 42 predicative frames DEMOTED→HOLD;
  32 frame stands (3→2 legs); 30="pas" NEW LEAD.** The round-15 A1
  battery never checked its legs against
  `code/crowd10/conditioner59/classification.json` (kill-grade ISLET-10:
  59="est" iff pre∈{64,94,93}) — this battery enforces A1's own bar
  against standing law. Leg audit: 37 claimed 6 (+1) → **0 valid** (all
  six LEFTOVER; @1795/@1796 are ONE physical window [42,94,59,37] —
  "6+1" was 6 unique) → DEMOTE; 42 claimed 2 → 0 (LEFTOVER+ESTE) →
  DEMOTE; **32: @316/@1210 EST → frame STANDS (3→2)**, @448 ESTE
  correctly excluded; 19: @1777 EST → HOLD confirmed. **"37 has 6
  adjective legs" is VOID; "est 37" ×6, "est 35" ×3, "est 42" ×2, "est
  que" ×2, "est 32" @448 all VOID as est-legs** — none of 35/42 has an
  est-arm leg. **30="pas" NEW LEAD**: @559 EST "n'est 30" + @1715 ESTE
  "ne [44-59] [30]" — the two canonical "pas" slots (19-window census
  queued). 39/45: single-leg predicative holds (@763 "on n'est 39",
  @103 "on ne l'est 45"). 37 TIER-2 (verb-stem/syllable, "cern"-family
  from "en 37-78"/"qui 37-01"/"pre-37"/"er-37") recorded as LEAD;
  count corrections: **37-01 ×3** (@939/@1633/@1817, not ×2),
  **37-78 ×4** (@312/@414/@475/@1770, not ×2). 32 keeps live tension
  (64→32 direct ×2, 26→32 ×2, 56→32 ×2, 91→32 ×2 — class battery).
  Weakest leg: the 32 frame stands on exactly 2 legs, both leaning on
  provisional 94/48 followers. Trace:
  `code/crowd16/report_inbox/next-token-{findings-,}est.md`
  (`test_est.py`).
- **fois (17="fois" — PROMOTED; first systematic pass over 17's 15
  windows) — absolute construction CONFIRMED; @369 escalated.**
  "17 11 26" ×2 @238/@1558 and "17 77 82" ×2 @1040/@1157 re-derived;
  77-82 frozen (×2, both post-17). **12~30 same-slot pair: 26-12 ×4 +
  26-30 ×4 = 8 windows** (finder said ×3 — corrected; homophone
  battery queued). 44~63 same-class: 5 shared followers
  {0,74,11,77,29}; "le même [44/63]" hypothesis flagged with its
  polyvalence caveat (82="même" word vs "m" letter — red-team call,
  NOT assumed). "20 62 94" ×3 sharpens the 20-paradox (determiner slot
  @307 vs noun slot @760 — two minimal pairs). 01-24 ×3 [40,828,984]
  ("il/on en" — 01 pronoun battery queued). **@369 anomaly VERIFIED**:
  [61,70,17,6,21,65,63] sole "pre+fois" junction (70-17 ×1 [368]);
  options ranked (a) undiscovered idiom/boundary, (b) 70-polyvalence —
  AGAINST lane law, **ESCALATED to red team**, (c) misassignment.
  20's paradox now one-sided (feminine-noun window solid; "[20] fois"
  @309 needs re-examination). Trace:
  `code/crowd16/report_inbox/next-token-{findings-,}fois.md`
  (`test_fois.py`).
- **forks (67/78/48/94) — 67 RESOLVED positionally (LEAD); 78="er"
  KILLED; 45="ce" DEMOTED→HOLD.** 67: 8 "veut" [110,272,1148,1390,1423,
  1450,1476,1623] vs 30 "et", zero adverses, re-derived — rule:
  **67="veut" iff the follower is infinitive-shaped** (33 ×6, stem+29
  ×2); else "et". Circularity caveat recorded (follower-defined rule);
  independent test = the 93/86 infinitive-stem predictions (@110: 93-er,
  @1390: 86-er). **78 "er" — KILLED distributionally**: determiner-
  predecessors 78 16/31 vs 29="er" 2/45; after 33=INF: 78 0 vs 29 5
  (odds ratio ~22.9) — near-complementary distributions; no positional
  split needed. **78="ver" LEAD** (surviving arm, unproven; "verdict" ×4
  word-level support). **45 "dict" vs "ce" adjudicated: 45="ce"
  DEMOTED from PROMOTE to HOLD** — "ce verdict" ×2 @573/@982 (87/47="ce"
  banked + 78-45) FORCES 45="dict" there; "par ce" ×2 @602/@1213 FORCES
  45="ce"; @314 contested — two values in complementary distribution
  ("dict" only after 78; "ce" elsewhere) = positional allophony,
  lane-precedented. **45 "ce/dict positional allophones" LEAD**
  (conditional on 78="ver"). 94="ne" STRONG LEAD (corroborated): "n'est"
  ×3 @558/@762/@1795, "ne me/m'" ×4 @578/@1182/@1353/@1742; 48/94
  complementary distribution quantified (62: 6/9, 12: 5/3, 82: 4/3,
  78: 2/2, 32: 4/1 — same slots, divergent followers). 48's value open
  ("pas" a guess from ne-adjacency). Adjective keyhole queued ("est 32
  48" ×3, "est 32 94" @318, "32 48 est" @1177, "est 19 48" @1779).
  Trace: `code/crowd16/report_inbox/next-token-{findings-,}forks.md`
  (`test_forks.py`).
- **i (34="i" — GT; 11 windows) — "la première" ×2 CONFIRM;
  "-quière" ×2 LEAD + 2 NEW 00-adverses.** 11-70-82-34-29-40
  byte-identical @754/@1034; 82-34 ("mi") ONLY in these 2 windows;
  70-82-34-29 without 40 (masculine "premier") 0×. **20-constraint:**
  "la première [20]" forces 20 = feminine singular noun — fed to the
  20 battery (3rd leg via @667 "pour [20]"). 9-64-29-40 @291
  ("acquière"-shaped) + 92-64-29-40 @685 ("requière"-shaped) — 64="qui"
  compositional inside the verb, LEAD; **the left-context adverse is
  REAL and fenced: @291 "pour [97] acquière", @685 "pour [92] requière"
  — 2 new fenced adverses for 00="pour"** (docket now: @1247 strong,
  @864/@291/@685 fenced; "pour"+subjunctive pattern now 3 windows).
  @595 "tout entière" (79-85-1-29-40) — new compositional leg for
  banked 79="tout" (5th leg family); stem 85-1="enti" LEAD. 73="lu"
  LEAD (73-34 ×2 @393/@1348, "lui" ×2). 20's paradox one-sided
  CONFIRM. Nulls held (@28 boundary, @555 "est-i-fois" unparsed).
  Trace: `code/crowd16/report_inbox/next-token-{findings-,}i.md`
  (`test_i.py`).
- **la (11="la" — GT) — de-dup CONFIRMED (load-bearing); 06="ent/ment"
  LEAD; "la 52-37-43" ×2 LEAD; @108 "veut" vote REJECTED.**
  n11=45; 87-11 ×7 ("cela", established) and 47-11 ×3 (allophone) excluded
  before clustering — standalone 35 (`test_la.py`). **06="ent/ment"
  LEAD**: 3 "[X]-06 la [NOUN]" windows re-derived (@320/@1123/@1721);
  06→77 ×6, 06→11 ×4; verb-ending vs adverb-ending fork queued (stem
  battery). **"la 52-37-43" ×2 LEAD**: byte-identical @1123/@1721; no
  finite-verb parse in the slot → 37 adjectival-or-nominal here (2
  tokens, 1 phrase type — does NOT restore the demoted est-frame;
  first multi-leg adjective-frame evidence for 37 outside the est
  family). 78 fork votes: @296 "la 78-40" ("l'ère"-shaped → "er") vs
  @1669 "la 78-55-81" ("la vérité"-shaped → "ver") — positional-
  allophony hypothesis QUEUED (seed minimal pair). "l'en-X" ×3
  @731/@782/@1656 — LEAD conditioned on 24="en" ("l'en-85/42/48":
  envoi/entrée/enquête-class; 48 tension flagged). 26-noun ×2 @239/@1559
  LEAD — tensions 26=verb ("en ce qui 26-37") and the dead 23/26 pair.
  **@108 vs @106 — CONTRADICTION ADJUDICATED**: one physical window
  [0,46,11,21,67,93,29,89]; the "veut" vote requires unbanking 00="pour"
  at @106 — REJECTED as a fork datum (banked wins ties); recorded as a
  conditional, handed to the forks battery. Anomalies verified, not
  forced: A1 "la la" @1523 (queued: 48's word-second-syllable profile);
  A2 @1288 "pour la fois" (fenced; cross-ref to the pour battery's @1287
  tension); A3 @997 "la par" (96-profile battery queued — "la par"
  parses under no reading of banked 96="par"). @499 "cela 29-40" strain
  fenced (47-11 "cela" clean at @269/@357 only). Trace:
  `code/crowd16/report_inbox/next-token-{findings-,}la.md`.
- **le (77="le" — provisional) — adverse DISSOLVED; 77="le" PROMOTE;
  84="fait" REJECTED; CORRECTION to A15.** All three "le/la"
  co-occurrences re-derived with natural parses (@832 = 87-11 "cela"
  boundary; @1034 clause boundary "[verb]-le. La première…"; @1042
  article+pronoun "le m[63] la [76]"). **77="le" PROMOTED**
  (provisional → promoted): (a) adverse dissolved; (b) three
  independent legs on banked values (@516/@870 "ce le [verb]" on 87="ce"
  banked, @832 "En cela, le [76]"); (c) zero clean contradictions
  (@1031 fenced as enclitic+break). Caveat: @516/@870 lean on
  80/89 verb-frames — the independent anchor is banked 87="ce" + the
  "ce le" shape. **CORRECTION TO A15 (major): the "84→59 ×4 (on est)"
  legs are VOID as "est" readings** — 59@1190/@1448/@1804 are ESTE,
  59@1291 FENCED per `code/crowd10/conditioner59/classification.json`
  (scope gap: the round-15 battery and red team never checked 59-class).
  **84="on" STANDS but is WEAKENED** — keeps the 59-independent legs
  ("qu'on en" ×2 @309/@472, "mon" @166, "l'on" ×7, 84→24 ×3) but loses
  the whole "on est" family; NEW red-team tension: the ESTE verbs
  CONTAIN 84 ([06-84-59], [84-59] as 3-syllable verbs) — a verbal-
  syllable use conflicting with pronominal "on". 81 = masculine abstract
  noun LEAD (77-81 ×4: @1086 "le [81] pour [33-INF]", @1240/@1401 "le
  [81]. Cela", candidates motif/moyen/dessein). 86-29 substantivized-
  infinitive LEAD (@430 "et/veut le [86]-er" → "le devoir/pouvoir"-shaped;
  converges with "par le [86]"). 76 gender tension queued ("le [76]" ×3
  vs "la [76]" @1046). Trace:
  `code/crowd16/report_inbox/next-token-{findings-,}le.md`
  (`test_le.py`).
- **m (82="m" — GT; 39 windows) — "vient de me parvenir" VERIFIED;
  79-adverse adjudicated; 84-noun REJECTED as overtaken.**
  98-83-82-96-21 byte-identical ×3 @227/@1060/@1783 (finder cited
  82-cells; convention note); **96-21 occurs NOWHERE else globally**
  — formula-bound. "vient de me parvenir" is perfect dispatch French
  in exact order. **98="vient" and 83="de" word-anchored LEADS** (1
  phrase type ×3 tokens — not cell-value promotions). 60/62/68 thirds
  homophone-set NOT granted by assertion — needs the {33,86}-precedent
  standard (queued). **M5 (79-adverse) ADJUDICATED: @396/@1227 are
  FENCED as strained residuals for 79="tout" (2/18)** — the m-finder's
  double-subject point is valid for the single-clause parse (corpus:
  zero "qui tout/tous m'" in Nesselrode v8 + Guizot t1–t3); A7's
  boundary parse is strained at both (qui-clause verbless). This
  REVISES the tout battery's B4 ("narrow/reducible" under-weighted the
  "qui"). A7's L2 (48=verb-stem) untouched. **84-noun REJECTED**: @166 =
  [24,87,11,24,82,84,53,12] is 82-84 = "mon" (A15 established) — the
  finder's "m'84 elision ⇒ vowel-initial" premise misreads the trigram.
  82-40 = 0 (bare-82 model: the vowel is unwritten). 94-82-06-06 ×2
  @578/@1182 (06 key; feeds the 06 battery and the 94="ne" lead);
  52-82-94 ×3 (52 paradox queued); 82-16 ×11 (16-91 ×2 sub-cluster);
  @20 "…m'[43]-er ce [33]" — 43 verb-stem lead. Trace:
  `code/crowd16/report_inbox/next-token-{findings-,}m.md`
  (`test_m.py`).
- **par-rest (96="par" — PROMOTED; 14 remainder windows) — 45="ce"
  PROMOTED then REVISED (see forks).** 45-64 ×3 (@314/@340/@1024),
  "par 45" ×2 @602/@1213, 45-46 @437 — par-rest battery PROMOTED
  45="ce" on the second frame-type; the forks battery REVISED to HOLD
  (value bipartite — see above). 98-83-82-96-21 ×3 formula CONFIRM
  (corroborates the m-beat). 43 = feminine noun of means/purpose LEAD
  ("la 43" @562, "43 pour que" @1544, "43 le" ×2 — suite/condition/
  manière/mesure candidates; "pour que"-frame discriminates). @947
  fenced ("par 86" — the 86=infinitive class's 12× "pour 86" is
  PROTECTED). @1196 doubled 82-16 frame — red-team anomaly (boundary
  misread possible). @927 fenced (48's value vs ne-reading). Singletons:
  09 ("09 qui" frame), 56 ("56 ce" ×4 lead frame), "par e-62" @847
  (folded into e-beat E7). Trace:
  `code/crowd16/report_inbox/next-token-{findings-,}par-rest.md`
  (`test_parrest.py`).
- **pour (00="pour" — BANKED, round-15 A9) — CONFIRM; @107 addressed
  fork-conditional; adverses fenced; RATE adverse weighed.** Follower
  census re-derived exact: 86×12, 33×8, 66×7, 92×6, 97×4, 11×4, 46×4,
  36×3 + singletons {13,20,34,44,64,67,98} (finder missed 67 — the @1247
  adverse itself) (`test_pour.py`). ~50/55 clean-or-neutral. @1545
  flagship [0,46,70,12,94] "pour que pre[12]…" and the twice-identical
  infinitive phrases (00-33-16 ×2, 00-33-21-64-37 ×2, 00-33-79-80-06 ×2)
  all re-derived. **@107 tension ADDRESSED**: [0,46,11,21,67] verified —
  UNDER 00="pour" the window votes 67="et" (pour que demands
  subjunctive); recorded as a FORK-CONDITIONAL datum, handed to the
  forks battery — NOT used to promote 00 (circular). **@1247 (strongest
  single adverse) FENCED**: second 00 gives "pour [33-16] pour [et/veut]
  que" — ungrammatical under both fork values; 54/55 others clean;
  split hypotheses queued (lane-law cost: 00-polyvalence would be a
  second polyvalence — must clear that bar or find word-internal).
  **@864 FENCED** (cheapest decisive test of 00 on the board — one
  clean re-parse kills or confirms it). **RATE adverse (new,
  run in-battery): 00 = 2.978% of pairs vs Nesselrode-v8
  "pour"-syllables ≈0.592% — ~5× the register rate** (Guizot t1–t3
  0.77–0.79% of words). MODERATE — does not kill, but joins @1247 in
  the split battery's docket. 86's value NOT named (three adverses
  indict 86="le" specifically, not 00). Feeds: @667 "pour [20]" →
  20-paradox; "l'er" noun ×3 (@76/@1374/@1824); @1545's 12
  cross-confirms "entrepre[12]"; @1680 predicts 65 subjunctive-shaped.
  Weakest leg: rate + @1247 — if the split battery finds 00's ~5
  adverse windows share a distinct contact profile, the grant's
  "preposition-like profile" leg must be re-weighted. Trace:
  `code/crowd16/report_inbox/next-token-{findings-,}pour.md`.
- **pre (70="pre" — GT) — 94="ne" STRONG LEAD; 12="n" LEAD;
  48="e"-letter DECLINED; 39="a/à" LEAD.** All frames re-derived but
  none both independent and clean for promotion: 94="ne" — 62-94 ×9
  (conditional on 62="on" strong lead), 94-59 ×3 "n'est" (conditional
  on 59="est" provisional), 94-82 ×4 "ne m'" (82="m" banked but
  continuations strained), 70-12-94 ×2 "prenne" (conditional on 12="n")
  → STRONG LEAD, promotion DECLINED (needs an independent clean leg).
  **12="n" — LEAD**: 12-48 = **×5 not ×7** ([169,709,809,1075,1736] —
  finder count error, material); 40-12 "en" @64 ambiguous; 12-34 "ni"
  @1740 clean n=1; "prenne/prennent" compositional (conditional, cannot
  self-promote). **48="e"-letter DECLINED**: no independent legs — the
  whole case re-reads A7's 4 granted "me [48]" windows and parses WORSE
  (1/4 possible, 3/4 broken vs 4/4 verb-slot recurrence) — re-litigation
  without new evidence. "prenne"/"prennent" compositional LEAD @1547
  (@1547 [0,46,70,12,94,92] = "pour que prenne [92]" — beautiful) /
  @347 / @1118 — supports the leads, cannot promote them. **39="a/à"
  LEAD**: 64-39 = **×1 @606** (finder implied a frame — corrected);
  70-39-11 ×2 word-internal "pré-a-la" (composes with P8's "préalable"
  @1067 — 44="ble" LEAD, @1604's 92 divergent); **59-39 ×2: @763 is
  "n'est [39]"** (finder mislabeled "est à" — corrected), @1511
  LEFTOVER. P5: dual-spelling "première" (analytic 70-82-34-29-40 vs
  syllabic 70-98-41 @235) — genuine architectural finding. P6: 91="va"
  LEAD ("prévalent" @519 + "va la" ×2). P7: 88="s"/10="s" LEAD
  ("presser" @615; "présenter" alternative live). Trace:
  `code/crowd16/report_inbox/next-token-{findings-,}pre.md`
  (`test_pre.py`).
- **classes (31/33) — record correction CONFIRM; 33="dire" LEAD;
  31=VERBAL class CONFIRMED.** **67-33 = 6×** [272,1148,1423,1450,1476,
  1623] (round-11's "×1" VOID — byte-verified; propagates to "67 33 29"
  ×3, "67 33 46" ×2, "67 33 66" ×1). **33="dire" LEAD** (promotion
  blocked by P2): "67 33 46" ×2 @1450/@1623 idiomatic under BOTH 67
  forks ("et dire que" the idiom; "veut dire que" = "to mean that");
  "47 33" ×2 @23/@1231 ("ce [inf]", preverbal demonstrative object);
  "33 21 64 37" ×2 ("dire [N] qui…"). Vouloir KILLED ("et vouloir que"
  ✗, "ce vouloir" ✗); penser WEAK; croire/savoir survive (finder's
  French judgment — frames verified, idiomaticity not re-derived).
  **P2 blocks promotion**: "33 29" ×5 (@273/@626/@1232/@1424/@1477,
  29's #1 left context) puzzles all five candidates — 29-89-84 /
  29-82-16 word-shapes ("erreur"?) must resolve first. **31=VERBAL
  class CONFIRMED**: 8 followers, 8/8 distinct
  {10,11,14,24,29,76,79,92} — class-tier signature (a single word
  would show formulaic repeats, cf. 33's doubled 5-grams); lefts
  08×3, 64×2 ("qui 31" ×2), 11/48/61. "31 79" @882 = "[verb] tout" —
  new compositional support for 79="tout" (6th leg family). Person
  UNDETERMINED (honest null — attack via "03 qui 31" ×2 @336/@1645,
  not followers). Trace:
  `code/crowd16/report_inbox/next-token-{findings-,}classes.md`
  (`test_classes.py`).

### Round-17 addenda (2026-10-08 UTC, crowd17 next-token — batteries
adjudicated; **red-team ratification pending**)

- **F85 — 12="n" battery-PROMOTE** (battery session-911ceab9, bar:
  ≥2 GT-anchored frames + zero contradictions; all clauses PASS).
  Three frame types, five occurrences: "en" 40-12 @63, "ni" 12-34
  @1740, "pren" 70-12 ×3. Zero forced alternative letters. Trace:
  `code/crowd17/report_inbox/battery-n-e-12-48.md`.
- **F86 — 48="e" battery-PROMOTE** (same battery, same bar). Two frame
  types, five occurrences: "me" 82-48 ×4 (@126/@377/@398/@1229),
  "ere" 29-48 @541 (single — a second occurrence would harden the
  leg). Trace: same note. **Enlightenment**: the letter tier explains
  the word-tier kills — 48="est"/"de"/"ne"-word readings failed
  because 48 is a letter, not a word. "prenne" = 70-12-94 ×2 is the
  analytic (12-48) vs syllabic (94) spelling of "ne".
- **F87 — 94="ne" battery-PROMOTE** (battery d6cab360, bar: ≥2
  independent "ne"-frames + zero board contradictions + n'-elision
  frames hold; all clauses PASS). Four frame types: 94-59 "n'est" ×3
  (@558/@762/@1795), 94-82 "ne me/m'" ×4, 62-94 ×9, 70-12-94
  "prenne" ×2. 37-window census, zero hard contradictions; single
  tension @1664 "22 94 84" ("ne on") fenced per A15-C3 with stated
  cause. Trace: `code/crowd17/report_inbox/battery-ne-94.md`.
- **Independent frame verification of F85–F87** (crowd17 finder beats,
  finder-grade, no verdicts):
  `next-token-findings-n-e-frames.md` — 23 12-windows + 38
  48-windows; 'ne' = 12-48 ×5 (corrects the brief's ×7, matching
  crowd16's count); flagship @125 "me la" clean double clitic; 'pren'
  70-12 ×3 GT both sides; 48's followers maximally scattered (19
  distinct/38 windows) — the scatter is evidence FOR the letter
  reading. `next-token-findings-ne-frames.md` — 37 94-windows; six
  clean "ne" frame-types, 12 instances; "n'est" ×3 holds (correction:
  the third is @1795, not @101); the morphologist's conditioned
  "ne"/"en" split re-derived from frame extraction alone.
  `next-token-findings-bigram-contexts.md` — every 84-window (n=25),
  every 94-82 (n=4), every 94-59 (n=3): "l'[84]" beats "le fait"-shaped
  7–0; "n'est" ×3 all REQUIRE n'-elision and all hold; 62/84 clean
  complementarity banked for collision-62-84; E1x: 77's l'-elision
  fires EXCLUSIVELY before 84 among known vowel-initial cells
  (77→{59,94,46,40,34,47,17} = 0) — an independent mechanism proving
  84 vowel-initial.
- **Registry consequence**: 12 and 48 are absent from
  `code/table-grid/table-registry.json`; the 12="n", 48="e", 94="ne"
  promotions and the 77="le" provisional→promoted merge are pending
  the coordinator's next merge (registry file unchanged this sweep —
  grid NOT regenerated).

### Round-17 wave-2 addenda (2026-10-08 UTC, crowd17 next-token — batteries
adjudicated; **red-team ratification pending**)

- **F88 — 39="a/à" battery-PROMOTE** (battery a-39, bar: ≥2 frames parse
  cleanly as "a"/"a" + zero contradictions; both clauses PASS). 13
  occurrences scanned; three clean frames: "a qui" @37 (follower 64="qui"
  promoted), "est a" @764, "est a" @1512 (@1512 load-bearing on provisional
  59="est"). 12/13 windows consistent with 39=/a/; the one resistant
  window @607 ("qui ? qui") fenced as adverse A1 with stated cause
  (word-boundary underdetermined; 39 has a demonstrated word-internal
  class in 70-39-11 "pre-a-la"). All determinate word-parses are the
  preposition "a" — zero parse as the verb "a"; the /a/ tier is ONE
  value per the allophone doctrine, not a second polyvalence. Trace:
  `code/crowd17/report_inbox/battery-a-39.md`.
- **F89 — 30="pas" battery-PROMOTE** (battery pas-30, bar: both ne-frames
  parse as "ne...pas" + ≥1 more independent ne-frame + zero
  contradictions; all four clauses PASS). @558 ("n'est pas", canonical
  order), @1713 ("ne 44 est pas"), plus two independent ne-frames
  @651→656 and @1363→1368. All 19 @30 windows scanned; none forces
  30≠"pas"; the one bracket-dependent rival frame (@1700/1702
  "n'importe") fenced to the queued ne-30-1700 battery. Trace:
  `code/crowd17/report_inbox/battery-pas-30.md`.
- **F90 — 59-frames battery-PROMOTE (frames)** (battery est-59-frames, bar:
  ≥2 independent "n'est"-follower frames parse as predicative +
  @1795 "42 n'est 37" parses cleanly + zero hard contradictions;
  verdict PROMOTE (frames)). The "n'est" universe is exactly three
  frames, all 94-59 elision: @558, @762, @1795; no analytic spellings
  exist (0/0/0). @762 (predicative-PP, "n'est à [88]"; 39=/a/
  allophone-tier) and @1795 ("42 n'est 37" copular) parse predicative;
  @558 is the "ne...pas" negation frame — the uniform-predicative claim
  is dead at the 30 leg, killed by the pas-30 battery (F89), not by
  this verdict. Trace: `code/crowd17/report_inbox/battery-est-59-frames.md`.
- **F91 — collision-62-84 kill-grade resolution: 84="on" unconditioned
  holds; 62="on" KILLED** (battery collision-62-84, bar: exactly one of
  {62,84} holds "on" unconditioned + loser's frames re-read cleanly;
  both clauses PASS). Zero crossover re-derived on the repaired stream:
  62→94 x9 vs 84→59 x4, with 62→59 x0 and 84→94 x0. 84's "on" lives in
  the post-clitic elision slot ("l'on" 77→84 x7; "qu'on" 46→84 x2);
  62's "on" lived in the pre-"ne" subject slot. The loser's nine 62-94
  frames re-read as "il ne": 8 clean, @508 fenced as residual with
  stated cause — @507 ("21-67-77-62-94-64-98") is the kill-grade
  discriminator: "l'on ne" reads iff 62="on"; under 62="il" it is
  "le il ne", which has no clean French parse (conditional on
  provisional 77="le" and battery-promoted 94="ne"). Stale counts
  corrected on the repaired stream (20-62-94 x4, not x3; the "@762
  62 n'est 39" window is @760). Trace:
  `code/crowd17/report_inbox/battery-collision-62-84.md` and finder
  input `next-token-findings-84-adjudication.md`.
- **F92 — enne-word-64: one-word "ierenne" claim KILLED at kill grade**
  (battery enne-word-64, C1 FAIL kill grade): the @61-65 window
  "34 29 40 12 94" forces the letter string "ierenne" (34="i", 29="er",
  40="e" banked GT; 12="n", 94="ne" promoted) and no French word
  contains it. 94="ne" is NOT downgraded — the kill targets word
  composition only; residual R-enne-61 recorded (word-segmentation
  residual). C2/C3/C4 PASS: "prenne" @1547-1549 undisturbed; 92's class
  stays OPEN (the only two "94 92" bigrams stream-wide, no class
  conflict). Trace: `code/crowd17/report_inbox/battery-enne-word-64.md`.
- **Wave-2 finder beats (finder-grade, no verdicts)**:
  `next-token-findings-post-promotion-sweep.md` — F1 "n'est pas"
  @558-560, the only "94 59 30" trigram stream-wide (support for F89,
  adverse input for F90); F2 "42 ne" x3 cluster (bare "ne" needs
  modals — predicts 02/74 verb-shaped; target ne-alone-02-74);
  F3 "77 78" x7 = "lever" composition, "48 77 78" x2 = "élever";
  F4 "32 48" x4 = "32e" feminine-agreement candidate; F5 noun frames
  for 44 with one lone adverse; F6 "12 94 92" x2 = the joint
  promotions' hard frame; ranked targets T1–T5 (enne-word-64,
  lever-77-78, noun-44, ne-alone-02-74, fem-32e); two clean nulls
  recorded (N1 "toute/toutefois", N2 "est-ce").
  `next-token-findings-noun26-frames.md` — the 26 verb/noun war: 17
  windows, 14 productive frame-types after formula de-dup; "26 pas"
  x4 (@654/@991/@1249/@1559) is the strongest verb frame; @1559 is
  the crux ("la [26] pas" — noun and verb readings clash in one
  window); "en ce qui" triple decides @1768 as verb by frame-type
  uniformity; three independent governors force verb-form (@154
  "66 84 [26]", @600, @841). Correction to the queue: "26 30" is x4,
  not x3.
  `next-token-findings-parvenir-thirds.md` — input for queued
  frame-vient-parvenir (thirds permutation test + 83="de"
  cross-checks, claim narrowed to the 60/68 pair); 92's nominal
  profile ('la 92' x3, '92 qui' x2) noted for the prenne battery.
- **Registry consequence (wave 2)**: 39 and 30 are also absent from
  `code/table-grid/table-registry.json`; the a-39 and pas-30
  promotions join the pending merge. Registry file unchanged this
  sweep — grid NOT regenerated.

### Round-17 wave-3 addenda (2026-10-08 UTC, crowd17 next-token — batteries
adjudicated; **red-team ratification pending**)

- **F93 — nest-subject-86-62-42 battery-PROMOTE** (bar: resolve iff
  each of {86, 62, 42} takes a subject parse with zero forced
  contradiction; all three clauses PASS). The three "X n'est ..."
  frames are the ONLY "X 94 59" trigrams in the 1,847-pair stream
  (closed-set census): @558 "86 n'est pas" (86 INF-class, "le 86"
  x5 noun face), @762 "62 n'est 39" ("il n'est a"; conditional on
  the collision battery's demonstrated-not-promoted 62="il"), @1795
  "42 n'est 37" (copular, predicative 37 per A1). All three windows
  parse subject-cleanly under standing values. **Enlightenment**:
  the claim is not "subject-shaped" from grammar intuition but from
  a closed-set census — these three are ALL the "n'est" frames, so
  there is no un-examined fourth frame that could break the rule.
  Conditional on provisional 59="est". Trace:
  `code/crowd17/report_inbox/battery-nest-subject-86-62-42.md`.
- **F94 — noun26-pas-frames battery-PROMOTE (frame-level, with
  recorded positional exception)** (bar: all four "26 30" windows
  re-derived; 30="pas" in each; noun-parse excluded per window;
  ne-audit; @1559 parsed or recorded as residual; all clauses PASS,
  clause 5 on the residual disjunct). 26 is verb-class: "26 30" x4
  = "[verb] pas" at @654/@991/@1249 (@654/@991 share the byte-
  identical 6-gram "76 49 24 26 30 03", counted once); noun-parse
  ("[noun] pas") is ungrammatical at all four; @1559's banked 11=
  "la" forces nominal 26, so the clause boundary between 26 and 30
  is fenced with stated cause. **The recorded positional rule —
  "26 = feminine noun iff immediately preceded by 11='la', else
  verb-class" — is the lane's second positional-polyvalence-shaped
  finding; it is RECORDED, not declared (declaring it is a red-team
  act per S7).** @991/@1249/@1559 carry the bare-"pas" 1840s
  tension, flagged to queued ne-alone-02-74. Trace:
  `code/crowd17/report_inbox/battery-noun26-pas-frames.md`.
- **F95 — noun26-encequi-triple battery-PROMOTE** (bar: triple
  re-derived; @1768 parses with 26 as verb; 37's slot named; 23~26
  split respected; subject-rival excluded; all five clauses PASS).
  The '24 87 64' formula triple re-derives exactly 3x
  (@179/@1766/@1774; fol1 23/26/59, fol2 37 x2/19 x1): slot-1 holds
  verb-class cells in all three windows (23 by the granted 23~26
  split, 59 as ISLET-10-licensed "est"), so 26 parses as the verb by
  frame-type uniformity at @1766-1771 ("24 87 64 26 37 78"). 37's
  slot is NAMED (object nominal vs clause boundary — value
  undecided, decision owned by queued frame-37-reexam). 23's value
  stays OPEN; "concerne"/"regarde" is a value LEAD, not a claim.
  Correction recorded: the queue's legacy @-offsets were stale
  (obsolete 1,846-parse indices); substance re-derives exactly.
  Trace: `code/crowd17/report_inbox/battery-noun26-encequi-triple.md`.
- **F96 — prenne-subject-S1545 battery-PROMOTE (claim confirmed via
  the bar's second disjunct)** (bar: subject found with zero
  contradiction, or subjectless confirmed with stated cause;
  clause 1 FAIL, clause 2 PASS). The "00 46" ('pour que') census is
  closed stream-wide at exactly 4 windows: @106 (overt subject,
  "pour que la [21]"), @545 (slot occupied by 24, fenced to
  ne-24-profile), @1545 (TARGET), @1680 (overt subject, "pour que
  tout [65]"). @1545 is the ONLY window where the verb word
  (70-12-94 = "prenne", @1547-1549) abuts "que" directly: the
  subject slot between @1546 and @1547 is EMPTY (pair-adjacent, 70
  word-internal). Exhaustive candidate sweep closed every
  alternative (post-verbal, ellipsis, matrix borrowing, impersonal,
  70-alone, re-splitting 12-94, 45-as-postposed-subject, parallel
  gapping): 1840s "pour que" + subjunctive mandates an overt
  subject. **Enlightenment**: the emptiness is anomalous against the
  construction's own distribution (2/4 windows show a clean overt
  subject) — it is not a cipher convention. No value promoted.
  Trace: `code/crowd17/report_inbox/battery-prenne-subject-S1545.md`.
- **Wave-3 finder beats (finder-grade, no verdicts)**:
  `next-token-findings-f-qui-par.md` — full 43/01 read: 43 n=16 (13
  productive frame-types after formula de-dup), 01 n=28 (26
  productive). **Strongest structural leg for 01="ci": the triple-
  "ce" composition** — all three "ce"-values compose with 01
  (87-01 x2, 47-01 @195, 45-01 @984), parallel to granted "cela" =
  87+11. Hardest cluster: "01-24" x3 (under 01="ci", 24 must be
  contre/apres-family; 24's contact profile strains both). 43:
  content-word shape, "la-43" @563 + "la-52-37-43" x2 support
  feminine noun; predicative 37/32 precede 43 x4; all four queued
  noun-43 candidates ({suite, condition, maniere, mesure}) are
  adversed by "43-pour" x3 (they govern "de", not "pour"). Eight
  ranked targets: T1 feeder-ceci-47-45, T2 disc-01-24-ci-X, T3
  rival-37-01-certain, T4 frame-43-la-52-37, T5 frame-43-21-43-
  doublet, T6 frame-43-pour-que-1544, T7 frame-43-pred-37-32, T8
  coll-76-01-98 (all queued). 01's honest state: no global value —
  "ci" wins only the four "ce"-compositions, "faisant" wins only
  "ce faisant"; both die outside their frames.
  `next-token-findings-est-reexam.md` — the evidence base for N59
  below: both sides' window counts re-derived exact on the repaired
  stream (59->37 x6 at @528/624/912/1178/1443/1796; classification.
  json EST keys exactly {103,316,559,763,1210,1777}; n59=27);
  A1's "+1 negated leg @1795" is a double-count (6 unique windows);
  "52-37" is x4, not x3 (minor, no verdict effect). The red team's
  decision points D1–D3 are stated in the battery's verdict (N59).
- **Registry consequence (wave 3)**: the coordinator merged the
  registry (2026-10-08 ~07:21 UTC) — 12="n" lead, 30="pas" lead,
  39="a/a" lead, 45="ce/dict" lead, 48="e" lead, 94="ne" lead,
  06="ent/ment" lead, 00="pour" prom, 77="le" prov (demoted from
  prom), 78="ver" lead (78="er" KILLED). `generate.py` printed
  UNCHANGED — the grid was already current; no figure regenerated.
- **Wave-4 bookkeeping**: the supervisor regenerated
  `code/crowd17/next-token/battery-queue.json` (176 targets; mtime
  2026-10-08 11:13 UTC) after ingesting the wave-4 verdicts.
  Separately, the 18 texts under `code/side-period/work/mine-v3/
  corpus/` present at the last sweep are absent now; the same
  filenames exist in `code/side-period/corpus/` — observed as a
  cleanup of duplicates, not a data loss (the working corpus is
  unchanged). The mine-v3 mentions below predate that cleanup.

### Round-17 wave-4 addenda (2026-10-08 UTC, crowd17 next-token —
12 batteries adjudicated; **red-team ratification pending**)

- **F97 — ent-06 battery-PROMOTE: 06="ent"** (bar: stem-
  classification of the 94/14/68 followers decides verb-vs-adverb +
  ≥3 clean frames; both clauses PASS). Full census: 06 n=44 on the
  repaired stream. Clean frames: F1 @578-581 "94-82-06-06" = "ne
  mentent" (82="m" + 06="ent" ×2 = "mentent", 3pl of mentir, clean
  negated verb phrase); F2 @1182-1185 the second "ne mentent"
  instance; F3 @346-349 "06-70-12-94" = "entreprenne" (3sg
  subjunctive; 70-12-94="prenne" established). The "[X]-06-11"
  la-frames: @1121-1123 "14-06-11" and @1719-1724 "68-06-11" parse
  ONLY as verb+object (adverb+"la" is ungrammatical) — conditional
  on 14/68 = verb stems (both open). The adverb fork is decided at
  battery level: "-ment" = 82+06 compositional, not a standalone 06
  value. No standing red-team verdict contradicted. **Registry
  note**: the registry already carries 06="ent/ment" as a lead from
  the 07:21 UTC merge; this battery promotes 06="ent" and closes
  the fork — the change stands queued for the next coordinator
  merge (registry file itself unchanged this sweep). Trace:
  `code/crowd17/report_inbox/processed/battery-ent-06.md`.
- **F98 — verb-32 battery-PROMOTE: 32 = one verb lexeme** (bar: 32
  as verb stem across all 13 windows; all clauses PASS, all
  adverses answered). All 13 windows parse under a single lexeme:
  finite 3sg forms ("qui 32" @33; "qui [32]e" @855),
  past-participle forms ("est [32](e)" @317/@449/@1211),
  participle modifier/passive (@130/@532/@1176/@1283/@1572),
  finite-or-participle (@248/@257/@1417). Epistemic grading for the
  red team: 6/13 windows strong, 1 medium (@1176), 1 medium-gated
  (@532, on noun-26's pending rule), 5 weak (neighbor-class
  assumptions stated). **The adj-32 dual-behavior question
  ("adjective/verb needs a red-team polyvalence adjudication",
  N56) is DISSOLVED at battery level — the adjectival function is
  the participle of the same verb lexeme, so no second polyvalence
  is required.** Pending red-team ratification. Trace:
  `code/crowd17/report_inbox/processed/battery-verb-32.md`.
- **F99 — ne-24-profile battery-PROMOTE (class-level): 24 = finite
  verb** (bar: 24's class named verb-or-preposition + "ne 24 ce" ×2
  parse + 24→87 ×10/52 explained; all clauses PASS). 52 windows
  scanned. Finite-verb slots: @547 ("que [24]"), @955/@1693 ("que
  [24] [85-stem]"), @311/@474 ("qu'on [24] [37]"), @1486 ("que
  l'on [24] ce"). Infinitive-taking: 24→85 ×5 (85=verb-stem, A3),
  24→89 ×3, 24→80 ×2, 24→82→16 ×2 ("peut me [dire]"-shaped modal).
  The VALUE is NOT named — it belongs to a future value battery.
  Consequence for the value board: the old "24 = en (strong lead)"
  reading is excluded by the verb class; the value arm is now open.
  Downstream consumers: disc-01-24-ci-X, w1-314-ambig. No standing
  red-team verdict contradicted. Trace:
  `code/crowd17/report_inbox/processed/battery-ne-24-profile.md`.
- **F100 — ci-01-value KILL: 01="ci" and 01="faisant" both killed
  as general values** (bar: "01 24" ×3 and "37 01" ×3 cohere under
  one value with ≤10% orphan; the discriminator windows kill both
  disjuncts at kill grade). W1 @40, W2 @828: "ci" directly before
  the granted finite verb 24 is ungrammatical; the pre-registered
  ci-compound rescue (ci-dessus/ci-apres) is dead under the F99
  24-class grant. W1/W2/W3 (@40/@828/@984): participle + finite
  verb with no recoverable subject → "faisant" ungrammatical at
  all three. Generous orphan counts: "ci" ≥24/28 (86%),
  "faisant" ≥23/28 (82%) — far above the 10% bar.
  **Explicitly NOT killed (fenced)**: "-ci" as a BOUND morpheme in
  "ceci" (87-01 ×2 @345/@1029, 47-01 @195, 45-01-24 @984 — the one
  clean "ceci [verb]" window); word-internal readings (37-01 as
  part of a "-faisant" compound adjective; 01-29="-cier" @596)
  untested. Dependency: the "ci" kill is load-bearing on F99's 24
  class grant — if that grant is ever overturned, re-open. Trace:
  `code/crowd17/report_inbox/processed/battery-ci-01-value.md`.
- **Registry consequence (wave 4)**: registry file unchanged since
  the 07:21 UTC coordinator merge — grid NOT regenerated. Pending
  for the next merge: 06="ent" (F97, fork closed — supersedes the
  "ent/ment" dual lead), 39="/a/" (F88), 30="pas" (F89), 24 =
  finite-verb class (F99, value open), 32 = verb lexeme (F98).
  None of the wave-4 battery verdicts was contradicted by a
  standing red-team ruling.

### Round-17 red-team adjudication addenda (2026-10-08 UTC — 25 batteries
adjudicated; red-team ruling AUTHORITATIVE)

Adjudicator: red team, kill authority. Scope: 20 batteries in
`code/crowd17/report_inbox/processed/battery-*.md` + 5 in
`report_inbox/processed/battery-*.md` (ne-94, n-e-12-48, dire-33,
le-77, lon-ne-77-62-94). Stream: repaired 1,847-pair parse. Every
number below is the red team's own re-derivation from
`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`
(anchors: 1,847 pairs / 96 types; 94-59 ×3 @558/@762/@1795; 12-48 ×5
@169/@709/@809/@1075/@1736; 62→94 ×9, 84→59 ×4, 62→59 ×0, 84→94 ×0;
77-84 ×7; 78: n=31, det-pred 16/31, pred-33 0/31; 29: n=45, det-pred
2/45, pred-33 5/45, OR=22.93). Trace:
`code/crowd17/report_inbox/processed/next-token-redteam-r17.md`.

- **F101 — GRANTS (R17-002…R17-013):** 12="n" letter-tier (three
  pencil-anchored frames: 40-12 "en" @64 [40="e" GT], 12-34 "ni" @1740
  [34="i" GT], 70-12 "pren" @347/@1118/@1547 [70="pre" GT]; zero
  contradictions in the 23-window census; upgrades R16-010 LEAD);
  48="e" letter-tier (38-window sweep: "ne" ×5 via 12-48, "me la"
  @126 [82="m" GT], feminine/mute-"e" ×5, "[89]-e" verb+ending ×3;
  the R16-007 decline is OVERTURNED); 30="pas" (conditional); 06="ent"
  (conditional — verb/adverb fork closed at battery level, F97
  ratified); 32 = one verb lexeme (class-tier); 24 = finite verb
  (class-tier); 59 "n'est" frames (frame); nest-subject-86-62-42
  (frame); noun26 "[verb] pas" ×4 + noun26 'en ce qui' slot
  (frame-level ×2). Lead: 39="/a/" allophone (three /a/ frames, zero
  forced contradictions; R16-011 HYPOTHESIS upgraded). Findings:
  prenne-subjectless (genuine fenced residual @1545); noun-26
  positional rule (16/17 windows cleanly; HELD from declaration —
  declaring it would be the lane's second polyvalence, §7: 67 only);
  12/94 "ne" duality FENCED as compatible (analytic 12-48 vs
  syllabic 94 is the homophonic cipher's ordinary mechanism, not a
  contradiction — neither 12="n" nor 94="ne" is downgraded).
- **F102 — REJECTS (R17-001, R17-006, R17-011):** 94="ne" promote
  REJECTED (no new byte evidence beyond R16-006; legs remain
  conditional — stays STRONG LEAD); ver-78-rebar implicit promote
  DECLINED (would contradict R16-005; the battery itself correctly
  NULLed — 78="ver" stays LEAD); noun26 unconditioned verb-class
  REJECTED (three windows force noun under banked 11="la").
- **KILLS CONFIRMED (R17-014…R17-025):** 78="er" (78 0/31 pred-33 vs
  29 5/45, OR=22.93; @296 fenced 1-window residual); 01="ci" and
  01="faisant" as general values ('01 24' ×3 @40/@828/@984 —
  ungrammatical under the granted 24 class; the kills are
  load-bearing on R17-009's 24 grant — re-open if it falls; bound
  "-ci" in "ceci" [87-01 ×2, 47-01, 45-01] and word-internal 37-01
  readings fenced, not dead); "enne" one-word composition
  (34-29-40-12-94 @61 = "ierenne" admits no French word; 94="ne"
  and 12="n" are NOT downgraded by the kill); 62="on"
  UNCONDITIONED (62→94 ×9 vs 84→59 ×4, zero crossover; §7 forbids a
  second unconditioned "on" against the A15 84="on" grant —
  62="il" stays demonstrated-not-promoted at red-team level);
  ne-06-317 gate (naming 06 did not resolve the @317 hapax; all
  three readings fail at kill grade; @317 stays a fenced residual).
- **SCOPE RULINGS (R17-019, R17-023, R17-024):** frame-37 A1 STANDS on
  6 windows (the "7th window" claim corrected to 6 —
  @528/@624/@912/@1178/@1443/@1796; the est-finder VOID claim does
  not overturn A1 without kill-grade evidence); 77="le" stays
  PROVISIONAL UNCONDITIONED (no new evidence; R16-001 docket
  unchanged — 76-noun + 80/89-verb batteries must resolve, then two
  of @832/@516/@870/@1042 upgrade to clean legs); A7-L2 NARROWED to
  its exclusive legs @1229/@1589 (48="e" is the general value; the
  "[48]er ce" windows are ungrammatical under 48="e" — a conditioned
  frame, lane-precedented like 47/87, not a second polyvalence).
- **Corrections accepted into the record:** 12-48 ×5 (not ×7 — both
  batteries agree; the finder overcount is corrected; supersedes the
  old ×7 gloss and corrects downstream citations); 06→77 ×7 (not
  ×6); "prennent" (70-12-06) refuted as stated, "concernent"
  unverified; 94-24-87 @161/@1773 (battery said @162/@1774, same
  frames); @508 anchor (62's offset; was @507 in queue evidence).

### Round-17 wave-5 addenda (2026-10-08 UTC, crowd17 — 13 battery notes;
red-team ratification pending)

All notes trace: `code/crowd17/report_inbox/processed/`.

- **F103 — battery-PROMOTE: 62="il" (subject pronoun)**
  (battery-il-62; bar: split of the 35 windows by subject function —
  32/35 subject, 2/35 word-internal @46/@1482, 1/35 fenced residual
  @508 per R17-022). Combines with the R17-017 kill of unconditioned
  62="on": the "il" reading is now the live one. Registry lead,
  pending red-team ratification.
- **F104 — battery-PROMOTE: 76 = noun, masculine** (battery-noun-76;
  bar all clauses PASS, all adverses answered). The R16-001 docket
  condition is SATISFIED: the 'le [76]' ×3 legs resolve in favor —
  77="le" is now re-evaluable by the red team against its bar. This
  battery does NOT itself promote 77; 77 stays provisional until the
  red team rules. Registry lead.
- **F105 — battery-PROMOTE: A15-C1 support leg (77="le" elides to l'
  exclusively before vowel-initial 84)** (battery-elision-77-84;
  re-derived on the repaired stream: 77→84 ×7, all intra-row
  @145/@259/@1057/@1446/@1484/@1763/@1802; 77→{59,94,46,40,34,47,17}
  = 0 each; every established other-follower value is
  consonant-initial — 11="la", 45="ce", 64="qui", 82="m", 87="ce").
  The 77="le" VALUE itself is NOT promoted — it stays provisional;
  the open followers (86/81/76/44/89, plus 78 ×7 and the small
  unknowns) carry no established value and stay open surface, with
  81's "prin" claim under the standing kill. Nothing in the verdict
  touches R5005, sealed gates, or the adjudication queue.
- **KILL (wave-5):** the 'ne le [78=verb-head]' frame KILLED
  (battery-ne-le-1075): its resolution condition (78 heading a verb
  phrase after 'ne le') is blocked by standing lane law (R16-005
  noun-syllable LEAD + §7 sole polyvalence) and the measured 0/31
  verb-slot rate; the kill agrees with R16-005 and contradicts no
  standing verdict.

### Round-17 wave-6 addenda (2026-10-08 UTC, crowd17 — 10 battery notes;
red-team ratification pending)

All notes trace: `code/crowd17/report_inbox/processed/`.

- **F106 — battery-PROMOTE: 45's post-78 follower profile**
  (battery-dict-45-contact-update; full census: all 22 of 45's windows,
  pre=78 n=4 vs standalone n=18; post-78 followers = {13, 01, 64},
  4/4 in-profile; {13, 01} exclusive to post-78, 0/18 standalone;
  Fisher two-sided p=0.00205 < 0.05). Establishes the syllable-rival
  contact profile as a real, ver-78-independent boundary (conditions on
  78's occurrence only, never 78's value). Does NOT promote 45="dict":
  contact-profile leg only, to adjudicate with dict-frame-78-45-13-55-61
  and fork-78-45-adjudication. Caveats fenced: post-78 class is n=4
  (one-window sensitive); 64 shared with standalone (profile-neutral
  A-list function word). Pending red-team ratification.
- **F107 — battery-PROMOTE: 26 verb-form via three independent
  governors** (battery-noun26-gov-frames; @154 "66 84 26" = clause
  boundary + "On [26-verb] [35]", 66 fenced; @600 "03 39 26 96" =
  aux+participle "a [26-part] par [45]" or "à" + infinitive, 03
  fenced, 39 tier "a/à"; @841 "62 94 26" = "[62] ne [26-verb]" under
  either 62 rival; @1706 "62 94 88 26" = "ne [88] [26]" with 88's
  verb-form profile re-derived ("39 88" x2, "88 77" x3); "26n" rival
  excluded per window). Does NOT grant 26=verb globally: the "la [26]"
  noun legs (@239, @128) and the @1559 crux belong to battery
  noun26-la-frames (T4), which must answer this verdict. Pending
  red-team ratification.
- **F108 — battery-PROMOTE: W2 @573 boundary gate — 78-45 is one word,
  ver-78-independent** (battery-verdict-w2-574-gate; 78-45 bigrams
  exactly 4x: @313/@573/@982/@1164; 13-55-61 2/2 after 78-45, 0x
  elsewhere; {13, 01} exclusive post-78 followers). Under 78='ver'
  (LEAD, unsettled) the one word reads "ce verdict [13-55-61] ne m'"
  — the gate does NOT promote 78='ver'. The two-word parse is
  impossible under 78='ver' ("ce ver ce" = demonstrative doubling)
  AND under every non-ver 78 value ("ce [X] ce" ungrammatical for all
  X). Kill-scope for 45='ce': exactly 1/22 windows (@574); A11 HOLD
  stands on the remaining 21. Fork routing: fork-78-45-rerun clause (a)
  consumes W2 as settled; clause (b) keeps the boundary with 78's
  value open. Pending red-team ratification.
- **F109 — battery-PROMOTE: 62/84 conditioned slot split (not free
  homophony)** (battery-slot-split-62-84; 62 n=35: pre-'ne'-partner
  62->94 x9 + 62->48 x6 = 15/35; 84 n=25: post-clitic 77->84 x7 +
  46->84 x2 = 9/25; crossover 62->59 x0, 84->94 x0, 84->48 x0 — zero
  both directions; single slot-type crossover @508 fenced to queued
  sister lon-62-on-conditioned). DISTRIBUTIONAL ONLY: does not name
  62's value, does not promote 62='il', declares no polyvalence.
  Adverses: @390 parsed (double-"on" exists only under the killed
  unconditioned 62='on'); @1188 fenced to 06-forces-84; @1417 fenced
  (ambiguous singleton). A15, the collision-62-84 KILL, and §7 intact.
  Pending red-team ratification.
- **F110 — battery-PROMOTE: 45->93 x3 cluster under one parse — 45="ce"
  + nominal 93** (battery-frame-74-45-93; indices 261/477/602:
  GOVERNOR + "ce" + NOUN — W1 "on [gov] ce [N93] 52", W2 "[pred] 74 ce
  [N93] pour 13", W3 "par ce [N93] 54 qui"); distributional support:
  93 article-governed at index 9 (provisional 77="le" slot), "93 est"
  at index 101. Covers the three windows only; 93's global class
  fenced to the verb-93 discriminator battery (priority 3, queued).
  Tripwire: if verb-93 finds 93 verb-shaped elsewhere, bar (b)
  converts to a kill-grade adverse for A11. Pending red-team
  ratification.
- **F111 — battery-PROMOTE: @1502 orphan confirmed — the 33-set orphan
  guard holds** (battery-orphan-1502; @1501-1507: "on [33]" —
  "on"+infinitive ungrammatical under the granted-unconditioned
  84="on"; orphan fenced to the neighbor 84, 84-driven not 33-driven;
  full 25-window census: 5 stem + 18 whole 'dire' + 2 orphans (@1502,
  @1642) = 25; orphan rate 2/25 = 8%, at/under the 10% threshold; no
  third orphan anywhere). Guard-battery success, not a value
  promotion. **ANOMALY FLAGGED:** the queue cites the parent set
  report at `code/crowd17/report_inbox/battery-dire-33-set.md`, but the
  file lives at `report_inbox/processed/battery-dire-33-set.md` (wrong
  path in the queue, file present; data chain intact via
  battery-erstem-33-id). Supervisor: correct the queue citation.
- **KILL (wave-6):** the ver-78 successor-completion claim KILLED
  (battery-ver78-ce78-open-succ): @364 "ce vere[49]" and @1397
  "ce veree" force "the open successors after 'ce 78' complete French
  ver-words" false under standing values (47="ce" granted, 48='e'
  R17-promoted, 40='e' banked; no lane-legal re-parse); the >=3-of-4
  bar is unreachable (1 clean word-level read @629 "ce ver"+67, 1 open
  @1105 awaiting 65). Scope fenced: kills the successor-completion
  claim only — 78="ver" LEAD untouched (R16-005), the 'ce verdict' x2
  positives (@573/@982) and the 78='er' distributional kill untouched.
  Residue: ver78-65-completion (p2), ver78-ce78-census (p3),
  verdict45-value (p3).

### Round-17 wave-7 addenda (2026-10-08 UTC, crowd17 — 8 battery notes;
red-team ratification pending)

All notes trace: `code/crowd17/report_inbox/processed/`.

- **F112 — battery-PROMOTE: the infinitive gates are satisfiable**
  (battery-gate-satisfiability-16-85; gate-audit scope only — 16's and
  85's values NOT named). Every one of the 28 windows of 16 and 15
  windows of 85 assigned a class (noun / finite-verb / infinitive)
  under the §7 sole-polyvalence law. Banked-value frames listed
  separately from lead-grade frames: `82-16` x11 ("m'[16]" — "m'"+verb
  fine, finite OR infinitive; 4 INF-clean @434/@1370/@1480/@1832, 7
  INF-admissible or fenced, none forces finite-verb), `12-16` x3 ("n'"+
  infinitive grammatical — "n'avoir pas"; double-"ne" at @844
  disfavors the negation parse there), `16-29` x1 (@1142 fenced
  residual — ungrammatical under all assignments, forces nothing).
  Lead-grade tension `62-16` x4 (finite-verb shape; 62 lead-grade
  subject pronoun), promoted-tier `16-00` x4 and `79-85` x2 (noun
  shape) tiered, not decided. **Binary verdict PASS: gates
  SATISFIABLE — no banked-value frame forces a non-infinitive class
  for 16 or 85. The laisser lead (X-33, LEAD strength) is NOT killed;
  laisser-gate-16 and laisser-gate-85 PROCEED.** Consistent with the
  x-33-laisser-test null (2026-10-08) that chartered exactly this
  gate. Pending red-team ratification.
- **F113 — battery-PROMOTE: 26 = feminine noun under "la"-headed
  determiner phrase** (battery-noun26-la-frames; all five bar clauses
  pass on the repaired stream). @239 "41 17 11 26 12 16" = absolute
  "une fois, la [26]" with 41="une" coherent (18/19 windows consistent;
  only stated residual "47 41 06" @4 resists); "26 12 16" tail fenced
  (three live readings, none forced; "26n" reading specifically
  tested). @1559 "40 17 11 26 30 06": 26 forced nominal by banked
  11="la" ("11 26" exactly 2x, both "...17 11 26"); the "pas" resolved
  by a CLAUSE BOUNDARY between 26 and 30 ("[noun] pas" ungrammatical;
  re-parse rival "l'a"+participle rejected — contradicts banked
  11="la"). @128 "48 11 02 26 32 96" = "la [02-adj] [26-noun]
  [32-adj]" (composition rival "02 26" 1x stream-wide, neither
  confirmed nor excludable). @530 addressed: "qui est 32" x2 is the
  control; 26="est" killed globally (by @239's "la est"). Eight verb
  windows stand alongside via a **refined positional rule: 26 =
  feminine noun iff its determiner phrase is headed by 11="la"
  (immediate "11 26" x2, or via intervening 02 "11 02 26" x1);
  elsewhere verb-class.** POLYVALENCE COST stated for the red team: a
  second positional polyvalence, in tension with §7 (67 the sole true
  polyvalence); this battery declares no polyvalence, overwrites no
  verdict. Caveats: 30/94/12/48/06 battery-promoted (pending
  ratification); 59="est", 77="le" provisional; 02/32/60/61 open. No
  standing red-team verdict contradicted; answers the F107 verb-26
  adverse (wave-6) at the frame level. Pending red-team ratification.
- **KILL (wave-7): "44 is a noun" KILLED at @1714** (battery-noun-44):
  '94 44 59 30' ("65 94 44 59 30", a8_06) forces 44 into a
  non-noun (clitic/pronoun) slot — under standing values a lexical
  noun can never intervene between 'ne' and the finite verb. All
  escapes tested: the bar's '65ne'-word-final + '44 est
  [30-predicative]' needs overturning pas-30's clause-2 leg and ne-94's
  promotion (escalation, not resolution); the bar's 59/30 re-value is
  structurally insufficient; clitic readings ("n'en est pas" /
  "ne l'est pas") are grammatical but kill the noun claim as stated
  (a second value needs a red-team polyvalence declaration; §7: 67
  the sole true polyvalence). The other frames hold: '77 44' x2,
  '47 44 59 37' @527 (clause 1 PASS), '44 00' x3 (clause 2 PASS);
  @1618 ('la on' right-edge anomaly, independent of 44) and @540
  ('44ere' word-internal feminine-stem composition, parallel to '82 44'
  = "m[44]") fenced with stated cause. Conditional epistemic status:
  kill stands on 94='ne' (battery-promoted, 6 legs) and 59='est'
  (provisional) — if the red team rejects either, revisit. No cleaner
  global rival demonstrated. Follow-ups: pronoun-44-1714 (p2),
  stem-44-nominal (p2), escalate-1714-ne44 (red team).

### Round-17 wave-8 addenda (2026-10-08 UTC, crowd17 — 12 battery notes;
red-team ratification pending)

All notes trace: `code/crowd17/report_inbox/processed/`.

- **F114 — battery-PROMOTE (packaging only): 89's noun-vs-infinitive
  class-conflict evidence package is complete for red-team adjudication**
  (battery-class-89-adjudicate). 89 n=14 re-derived (census:
  [113, 222, 275, 285, 303, 640, 781, 871, 986, 1082, 1377, 1393, 1498,
  1752]). Window table: noun-clean 11/14 + infinitive-slot 3
  (@221/@985/@1497, all pre=24-modal, 77-independent — preserves the
  frames-80-89-indep leg). The @1375 kill-grade infinitive exclusion is
  stated: after "pour [86]-er" (86 INF-class, A9 granted class-level) 89
  cannot be a verb — "[inf] [89-finite] on" and "[inf] [89-infinitive]
  on" are ungrammatical. No class is named for 89; no polyvalence is
  declared (§7: 67 et/veut is the sole true polyvalence — adjudication
  is the red team's act alone). WHY: the battery is barred from
  declaring a second polyvalence, so it gathered and handed over the
  conflict raw. Provisional markers: 24-modal is battery-promoted
  (ne-24-profile); @1391's tail is gated on 16's open class
  (frame-82-16 queued); @1497's left junction is fenced on provisional
  59='est'. No standing verdict contradicted.
- **F115 — battery-PROMOTE (evidence-gathering only): the 85-33
  'contredire' compound evidence package is complete**
  (battery-contredire-85-33-vehicle). 85 n=15 re-derived (predecessors:
  24 x5, 29 x3, 79 x2, 81/76/21/56/91 x1); 85→33 exactly x1 (@1699,
  hapax); 33→85 x0. Compound plausibility: SUPPORTS — "contredire" is a
  real French word ("contre-" + "dire"; "contrecroire" is not a word,
  so the compound would be dire-only, touching the croire/dire tie);
  compositional multi-group words are established lane devices
  (87+11 = "cela" A-grant; 70+12+94 = "prenne" battery-tested).
  Limits: STRONG — both halves are open values (85 unpromoted, A3 frame
  grant only; 33 tied dire/croire, both null), so the compound has zero
  granted legs; it is conditional on two future promotions. WHY the
  package-level verdict: the bar was gathering, not resolution —
  nothing named, nothing declared, per §7. Red-team questions stated,
  not decided: (1) whether 85's load (verb-stem 'en [85]' x5 under the
  A3 grant; noun-shaped 'tout [85]' x2 under 79='tout' promoted;
  bound "contre-" prefix at @1699) is one value, allomorphy, or a
  second polyvalence; (2) whether the @1699 compound, if adopted, breaks
  the croire/dire tie; (3) whether it closes the @1700 'n'importe'
  complement at 20 (still open). No standing verdict contradicted.
- **F116 — battery-PROMOTE: both hostile 83 cells fenced under
  conditioned 83='de'** (battery-de-83-residuals; 83 n=15 re-derived,
  both targets mid-row — no row-boundary artifact). @1334 ('39-83-86',
  a7_05): hostility dissolved via the DEMONSTRATED word-internal-39
  fork — 39=/a/ is promoted at the allophone tier (a-39 battery:
  70-39-11 "pre-a-la" x2), so "pre[52]a" + 'de'+INF reads clean; the
  residual is the named open host word (52, n=27), not a
  contradiction. @1829 ('38-83-24', a8_11): OUT-OF-CLASS for any
  word-level 'de' — 24 is class-level promoted finite verb
  (ne-24-profile), and 'de' + finite verb is ungrammatical in French
  under ANY 'de' hypothesis; clause-boundary and quantifier-ellipsis
  fences were tested and broken; the syllabic '-de'-final fork is
  owned by queued syll-83-de, not duplicated here. WHY the promote:
  both windows parse or are fenced with stated cause; no standing
  verdict contradicted; the queued escalate-83-de-kill owns the
  UNCONDITIONED lead and is untouched. Epistemic: the @1334 fence is
  conditional on the word-internal-39 fork (follow-up:
  profile-52-host-word, p3).
- **F117 — battery-PROMOTE: no plural-determiner subject exists in
  @505-544 for @544's '[42]ent'** (battery-det-pl-544; confirm-absence
  promote on the orphan-1502 precedent). 91's determiner reading KILLED
  stream-wide (91 n=21: 91-11 x2 @1006/@1669 and 91-77 x1 @521 — "les
  la"/"les le" ungrammatical; 91 is word-final, an independent word);
  12 is a letter, not a determiner (battery-promoted 12='n', pending
  ratification); every other determiner-headed NP in @505-544 is
  singular (77='le' provisional, 87/47='ce' granted). The only
  subject-adjacent NP ("91 12 44 29 48") has no determiner and no
  plural marking. The queue's adverse answered two ways: 91|12
  boundary established (mid-word "91n" unsupported — 91 never precedes
  any letter in 21 windows); "n[44]ere" one-word parse allowed but
  determiner-free. WHY: the claim "found, or confirmed absent" is
  satisfied by confirmed absence. Caveats: 06='ent' and 12='n' are
  battery-promoted pending ratification; 77='le' and 59='est'
  provisional. The 3pl subject of "[42]ent" stays open — follow-ons:
  subj-42-qui (queued) and gender-44 (this wave, F118).
- **F118 — battery-PROMOTE: 44's gender is masculine** (battery-gender-44;
  44 n=15). Both true determiner windows parse as masculine article +
  noun: 'le 44' @208-209 ("[42]ent le [44]") and @1679-1680 ("le [44]
  pour que [79...]" — governing a purpose clause under granted
  00='pour' and banked 46='que'). The sole apparent feminine window
  @1070-1071 dissolves into word-internal "préalable": 70-39-11 occurs
  exactly x2 stream-wide (@1068 and @1605), ungrammatical as flat
  "pré à la [X]" at both sites; "préalable" is épicène
  (gender-neutral), contributing zero gender information — clause 3
  passes via the stated structural rule. Elision test: 77 elides to
  "l'" before vowel-initial 84 (x7, A15) but never before 44 → 44 is
  consonant-initial, consistent with "le [44]" and with 44='ble' at
  @1070. The feminine alternative is costed and rejected at kill grade
  (needs overturning 77='le' at both windows, with no independent
  evidence). WHY: two clean masculine windows + one
  parallel-supported re-analysis; one lexeme, grammatical nominal use
  (no §7 polyvalence declared — the lane's analytic/syllabic readings
  cover it). Gates any future '-ère' hypothesis for 44. Caveat:
  77='le' is provisional. 44's VALUE is not named.
- **F119 — battery-PROMOTE (class-level): 88 is VERB-CLASS
  (verb stem/governor)** (battery-governor-88-value; 88 n=23, full
  census re-derived, two corrections to the prior partial profile).
  The preposition rival is tested and REJECTED distributionally
  against the granted preposition controls 00='pour' (n=55) and
  96='par' (n=21): 88→77 x3/23 vs 0/76 pooled (Fisher p=0.0113 —
  conditional on provisional 77='le'); 88 takes zero infinitive-class
  followers (86 x0, 33 x0) vs 00's 20/55 (Fisher p=0.0004,
  77-independent). The @334 '88-40' question is owned: word-internal
  '[88]e' decided (40='e' is a banked LETTER, word-final 9/21) — the
  boundary reading is word-shape-less, since no French word has the
  shape 'e'+[03] (03 is verb-stem-shaped per stem-03). Frame legs:
  L1 'tout [88] ce' @497 (79='tout' granted A5); L2 'est a [88]' @765
  ('être à' + infinitive frame; conditional on provisional 59='est');
  L5 @1049 '[88] 29-40' ('er' banked — this refutes the parent null's
  "88 never directly precedes 29"); L6 @1119/@1706 '88 … 12-06'
  ('n'+'ent' 3pl, battery-promoted); L7 @1267/@1727 '[88] 24 30'
  (24 finite verb class-promoted; 30='pas' battery-promoted).
  Noun/adjective/adverb/conjunction/pronoun are eliminated in turn;
  verb-class is the last class standing. WHY the promote: class-level
  claim only (no value named), per the ne-24-profile precedent; §7
  respected — 88-as-stem is cipher granularity (parallel to 29='er',
  40='e'), not a second polyvalence. No standing verdict contradicted
  (R16-005 untouched; the lever-88-governor null's 'not kill' stands).
- **F120 — battery-PROMOTE: all 7 'l'on' legs re-derived under 84='on'**
  (battery-lon-legs-census). 77-84 bigrams stream-wide are exactly 7:
  @145/@259/@1057/@1446/@1484/@1763/@1802 — matching the A15 re-
  derivation byte-for-byte. 6 legs read 'l'on' cleanly; @146 is fenced
  as R3 alongside R1 (@1619 "la on", 11-84 unique x1) and R2 (@1664
  "ne on", 94-84 unique x1): 84-29 is unique x1 of n(84)=25 — 29='er'
  can neither attach left to 'on' nor open a word before 'ce', and no
  parse covers 77-84-29-87 without contradiction. Twin legs @1446 and
  @1802 share the '64 77 84 59' frame ("qui l'on est", tails 36/35).
  WHY: the census confirmed the collision-free legs on the repaired
  stream. Dependence graded per A15-C1: every leg's "l'on" reading
  inherits provisional 77='le' — no 77 promotion made; the 84='on'
  grant does not rest on this census (77-independent legs "qu'on en"
  x2, "mon"@166, 82-84 @166 carry the value). No value promoted, no
  standing verdict changed.
- **F121 — battery-PROMOTE: 42 takes the nominal class NOUN across the
  nominal frames** (battery-val-42-nominal; 42 n=20, all counts
  re-derived). T1 '42 ne' subject-slot x3 (@494/@785/@1795 — "[56]
  [42] n'est [37]" the strongest leg, under battery-promoted 94='ne');
  T2 'est [42]' x2 (@465/@1188 — the A1 predicative frame grant,
  used not re-litigated); T4 76->42 x3 (@429/@489/@1618 —
  class-level: "76 42" is word+word under every open 76-value); T3
  29->42 x3 FENCED (the one fence, one stated cause: segmentation
  rival — "laer"/"quer" are not French words, so 29 cannot be
  word-final there; the word-internal "er[42]" rival stays live).
  4/4 frame types covered with exactly 1 fence. Class choice NOUN over
  adjective by economy (bare subject slot needs no substantivization
  machinery). WHY: all bar clauses pass; the A1 adverse is answered.
  Escalation (red team): nominal-42 here plus the stem-42-verb null's
  genuine verb-class contact on "42ent" at @206 ("[42]ent le [44]",
  transitive) and @544 = a polyvalence question — only the red team
  can declare a second polyvalence per §7. The simple verb-stem
  reading (no polyvalence) is now fenced on both sides. Caveat:
  94='ne' is battery-promoted pending ratification.
- **KILL (wave-8): the "exactly one boundary parse" claim KILLED at
  @1739-1744** (battery-ni-1740-1742): '86 12 34 94 82 46' admits ZERO
  clean parses, not one. Reading P1 ("ni" word): fenced — 12-34 is a
  hapax with no 'ni...ni' partner stream-wide (single "ni" is
  ungrammatical); banked 82='m' kills "ne me" (needs the absent 48;
  elision blocked by consonantal 46='que'); "ni ne" is ungrammatical.
  Reading P2 ("n"+"i" letter split): fenced — "n"/"i" stranded as
  non-words; the word-internal variants leave "ne m que" verbless.
  Both readings are fenced for the red-team 12/94 duality adjudication
  (prenne-70-12-94's general ownership untouched — scope kept to
  @1739-1744). @1742 is the odd one out among the four 94-82 windows
  (the other three are "ne m'entent" 94-82-06-06, R17-007) — this
  independently confirms R17-001's "verbless 'ne me que'" strain note.
  R17-001 (94='ne' STRONG LEAD) and R17-002 (12="n" LETTER-tier grant)
  are NOT contradicted: the kill is at word level, on French grammar
  and banked 82='m'. Follow-ups: rightedge-56-1745 (p2),
  leftedge-52-86-1736 (p2).

### Round-17 wave-9 addenda (2026-10-08 UTC, crowd17 — 12 battery notes;
red-team ratification pending)

All notes trace: `code/crowd17/report_inbox/processed/`.

- **F122 — battery-PROMOTE (class-level): 21 = NOUN**
  (battery-de-frame-21-class; 21 n=30, full window set re-derived). The
  'la [21]' frames x2 (@109/@359) are the categorical discriminator:
  "la" + infinitive is ungrammatical in French, so the infinitive rival
  is excluded at window level. Zero infinitive-forcing predecessors
  across all 30 21s; 21-67 x8 all noun-consistent under the §7
  positional rule; @1423 actively selects noun over infinitive ("veut"
  + infinitive-shaped 33). WHY: the la frames alone force the class —
  no other grammar parses them. No value named (class only), per the
  ne-24-profile precedent; §7 respected. Caveats: @171 ("ne [21]")
  fenced on the unratified 12+48 "ne" composition (battery-promoted,
  pending ratification) — conditional evidence, not a contradiction;
  @176's 86-contact rides on the pending 86-INF promote. Follow-ups:
  none proposed — fenced adverses routed to frame-87-83-cede and the
  86-INF ratification path.
- **KILL (wave-9): 43="suite" KILLED; "maniere" dies with it**
  (battery-noun-43-discriminator; 43 n=16, full 16-window census).
  @21's "82-43-29" trigram forces V(43)≠"suite": "msuiteer"/"suiteer"/
  "erce" are not French words under the non-negotiable values 82="m",
  29="er", 47="ce" — only "mener"/"emmener"/verb-stem parses survive
  (43="en" or stem at @21). The discrimination table kills "maniere"
  too (fails "par 43" like "suite"; both fail "43 pour que").
  Survivors: {condition, mesure} — independently confirmed by
  battery-frame-43-la-52-37's clause-(b) narrowing ("suite pour
  [inf]" and "maniere pour [inf]" are not French; condition/mesure
  spared). Enlightenment: the same @1544 "43 pour que" frame that
  kills "suite" nominates its rivals — "prendre des mesures pour que"
  is peak diplomatic-purpose French. No standing verdict
  contradicted. Follow-ups: at21-82-43-29-adjudicate (pri 1 — decide
  whether 43 at @21 is word-internal "en", verb-stem, or noun, and
  reconcile with the "par [43]" noun frames; petitions red team on §7
  if split), frame-43-pour-que-1544 (boundary alternative — purpose
  clause after clause-final noun, under which all four candidates
  pass; adjudication owned there).
- **KILL (wave-9): orphan-86 @300, @716, @1131, @1147 CONFIRMED**
  (batteries orphan86-300, orphan86-716, orphan86-1131-1147). @300:
  no stated 97-class exists anywhere in the lane (naming is queued
  frame-97-profile); the only stated 78-value is the unsettled "ver"
  lead (R16-005) and it cannot parse the window; the 86-as-letter
  rescue fails behaviorally — 86 takes 29="er" compositionally in 4
  stem windows, letter-adjacency only 2/32 — and would need letter
  status for 97, which 97's pour-distribution (pre=00 x4) forbids.
  @716: all six tested 66-class candidates carry ≥1 hard
  contradiction — group (a) pour-governed x7 demands non-finite,
  group (b) "66-84" x2 demands finite-verb-shaped ("que [66] on"
  with banked 46 + granted 84); the intersection is empty; the only
  rescue is a second 66 class — a §7 red-team act. @1131: 37-86
  bigram x1 stream-wide; the only newly-stated neighbor class
  (24=modal, promoted pending ratification) cannot place a bare 86
  before it; 37's class is open (red-team territory). @1147: 98-98
  doubling x3 (@1073/@1145/@1660) with divergent right edges 12/86/80
  — no stated 98-pattern exists to resolve against. 86 orphan rate
  holds at 4/32 = 12.5% (overall 6/57 = 10.5%); the ≤10% bar stays
  unmet — any single resolve would have flipped it to 3/32 = 9.4%.
  Each battery routes its blocker onward without duplicating queued
  work (frame-97-profile, ver78-296-97gate, poly-66-split, prof-98).
- **KILL (wave-9, meta): the subsample battery's p≈0.032 "threshold-bug"
  escalation REFUTED** (battery-pair-60-68-readjudicate). Both halves
  of the bug claim are dead: exact enumeration gives predecessor p =
  0.05347 (18507/C(24,7)); 10 seeds 0.0523–0.0562 — the thirds
  battery's 0.0546 was correct all along. The claimed error mechanism
  is arithmetically impossible: P(null predecessor TV ≥ 0.9412)
  re-derives to 0.24, not 0.0546 — a lower threshold cannot produce a
  smaller tail. Supervisor retraction already recorded on the
  subsample-power-60-68 queue entry (2026-10-08) — cite 0.05347, not
  0.032. Housekeeping: the pair-60-68-readjudicate queue entry keeps
  its original claim text (the false 0.032) as history; its verdict
  record (kill, 2026-10-08) supersedes it. The thirds null stands;
  non-rejection stays marginal (~0.003 above α=0.05; n=7 is fragile
  to single-token perturbations) — the structural question stays
  live for queued singleton-68-predecessors.

### Round-17 wave-10 addenda (2026-10-08 UTC, crowd17 — 11 battery notes;
red-team ratification pending)

11 notes trace: `code/crowd17/report_inbox/` (3 new this sweep:
battery-donne-168-708-leg.md, battery-noun-89-1377-adjudicate.md,
battery-stem-44-nominal.md) and `code/crowd17/report_inbox/processed/`
(8: battery-adj-60.md, battery-at21-82-43-29-adjudicate.md,
battery-fence-83-1217.md, battery-noun-60.md, battery-tout-14-rerun.md,
battery-tout-slot-14.md, battery-verb-60.md, battery-vient-98-name.md).
1 promote, 2 kills, 8 nulls.

- **F123 — battery-PROMOTE: 98='vient' (finite semi-auxiliary)**
  (battery-vient-98-name; 98 n=40, all 40 windows re-derived and
  scanned). All seven pre-registered bar clauses pass (2–5 via the
  explicit fencing the bar itself permits): two 'vient de' frame-types
  hold — formula 98-83-82-96-21 x3 byte-identical (@227/@1060/@1783)
  and @897 '14 98 83 86' = '[14] vient de [86-inf]'; doubled-98 x3
  (@1073/@1145/@1660), @702 ("12 98" = "n'vient"), @1139
  ('00 98' = 'pour [98]'), @930 ('82 98 83 56'), @1601 ('82 98 00 44')
  each fenced or resolved with stated cause; zero board contradictions.
  No standing red-team verdict contradicted (no A-item covers 98;
  checked `code/crowd15/report_inbox/next-token-redteam.md`). WHY:
  the two independent 'vient de' frame-types plus the 40-window sweep
  with zero contradictions earn battery grade — provisional,
  red-team ratification pending. Caveats: clause 1 rests on the
  83='de' lead (le83 null — ratifying 83='de' hardens this promote);
  the doubled-98 x3 cause is unknown (if the red team declares a
  second value for 98, clauses 2/4 re-open); 62='il'
  (demonstrated-not-promoted) underwrites four '[62] vient' windows.
  Follow-ups: none required (promote); residuals routed outward —
  doubled-98 cause (red team), 83='de' ratification (le83 line),
  48-slot residuals @124/@971/@1317 (verb-48 line).
- **KILL (wave-10): 60 = masculine noun KILLED** (battery-noun-60;
  60 n=18, full 18-window census, all counts re-derived). The bar's
  coherence fails on all four frames under the nominal reading (C1
  'le [60]' @454; C2 at least 2 of the 3 non-frame-family '60 03'
  windows @690/@1644/@1674 as NP-frames — offset correction recorded:
  the queue's @1675/@691 are the 03 positions; the 60 positions are
  @1674/@690 on the repaired stream), the "value unnamed" adverse is
  unanswerable (C3), and two independent windows force 60 into verb
  slots — @1338 'qui 60' and @700 'ne 60' — kill-grade per protocol.
  A cleaner rival class (60 = masculine adjective) stood as the
  demonstrated rival. Correction to the lane record: '87 03' occurs x0
  — the 'ce [03]' @1014/@1790 support is via 47='ce' (granted A4), not
  87='ce'; the 03-noun support itself stands ('le [03]' @722).
  Follow-ups: adj-60, verb-60 (both done this wave).
- **KILL (wave-10): 60 = masculine adjective, single-value KILLED**
  (battery-adj-60). The four bar frames DO cohere under the adjective
  reading (C1–C3 pass — 'le [60-adj] [65-N]' @454; 65 nominal via
  '65 qui' x3 @724/@1208/@1340; 03 nominal via 'le [03]' @722 and
  'ce [03]' @1014/@1790 — the adjective is the confirmed cleaner
  rival to the killed noun claim on those frames), but C4 fails at
  kill grade: two independent windows force 60 verbal — @1338
  'qui 60 08' and @700 'ne 60 12' under red-team-granted values. Both
  single-value claims for 60 are dead; the live result is the bare-60
  vs ent-60 verbal shape split (see N100). Follow-ups:
  poly-60-redteam (p1, red-team adjudication packet — queued),
  adj-frames-995-637 (p2 — queued), participle-60 (p2 — queued).

### Round-17 wave-11 addenda (2026-10-08/09 UTC, crowd17 — 21 battery notes;
red-team ratification pending)

21 notes trace: `code/crowd17/report_inbox/` (all new this sweep — 21
files: adj-frames-995-637, dict-45-ce-rival-1165, dict-45-w3-ceci,
dict-78-45-wordbound, disc-01-24-ci-X, feeder-ceci-47-45,
frame-97-profile, la-523743-adjective, le-par-distributional,
lon-62-on-conditioned, lon-94-64-rightedge, name-21-obj,
prenne-92-noun, prenne-trigger-348, qui-2326-prefix,
qui37-rival-values, suite-21-qui-que, ver78-la78-census,
verb-92-subset, w1-314-ambig, w1-314-rebar). 7 promotes, 3 kills,
11 nulls — verdict tags in `code/crowd17/next-token/battery-queue.json`
match 21/21 (326 entries total: 152 verdict, 174 queued).

- **F124 — battery-PROMOTE: 24="faire" (verb lexeme); 01="en" LOCAL**
  (battery-disc-01-24-ci-X). 24="faire": finite "fait", infinitive
  "faire", participle "fait" — decided across the three 01-24 windows
  (@40/@828/@984). 01="en" LOCAL to those three windows only. Two
  standing kills mechanically explained, not reopened: general 01="ci"
  stays KILLED ("ci" never precedes a finite verb @40/@828; no
  ci-compound hosts a verb @984); 01="faisant" stays KILLED
  (participle + finite "fait" with no subject is ungrammatical at all
  three windows). WHY: the discriminator decided on non-'ci' 01 — the
  three windows parse fully only under 01="en" + finite-24. Provisional
  (battery grade), red-team ratification pending. Note: this promote
  fires the never-downgrade rule — dict-45-w3-ceci's 01='-ci' at @984
  was held at null because it would downgrade this verdict (N111).
- **F125 — battery-PROMOTE (class-level): 97 = infinitive-class**
  (battery-frame-97-profile). Class-level grant; value open, not
  named. No standing red-team verdict contradicted (no A-series
  ruling names 97; §7 untouched). Unlock note: the gated target
  ver78-296-97gate still needs stem-86 to name 97/86 VALUES — this
  class promote does not clear it (queued, verified in queue.json).
- **F126 — battery-PROMOTE (distributional calibration): 'ARTICLE +
  PROMOTED PREPOSITION' violation is systematic**
  (battery-le-par-distributional). @913 "le par" is not isolated:
  @997 "la par" (row a6_02: `60 67 11 96 82 33 00`) is the same
  violation class — ungrammatical under banked 11='la' and promoted
  96='par', no neighbor rescue, no covering unit. Promoted scope is
  the distributional claim only: it does NOT decide S5, does NOT
  assign any value to 37, does NOT touch the A1 predicative-frame
  dispute. Natural next step (not pre-committed): calibrate the
  adjacent 82='m'+96 pronoun+preposition class the same way.
- **F127 — battery-PROMOTE: 24=finite modal verb (class), 87=ce, 64=qui
  in the "qui [23/26] 37" frames** (battery-qui-2326-prefix). Both
  windows parse with 24/87 named; the frames stay in verb-position
  after naming (23/26 post-qui verb slot; 37 post-verbal predicative
  per A1). All listed adverses answered; §7 respected, no new
  polyvalence; R5005, sealed gates, and the red-team queue untouched.
- **F128 — battery-PROMOTE: the 37 rival-value RANKING**
  (battery-qui37-rival-values). The ranking is promoted as
  battery-decided; NO value for 37 is named/granted/promoted; the A1
  predicative-frame grant is not decided (red-team re-adjudication
  stands); no second polyvalence declared (§7). Both adverses fenced
  with stated cause (A1 deferred to red team; A12 unit grant
  untouched).
- **F129 — battery-PROMOTE: 92=verb on its verbal-governor subset**
  (battery-verb-92-subset; stem/inf/fin per governor). All bar clauses
  pass; every listed adverse answered (fenced with stated cause). The
  split/polyvalence consequence for 92's global class is ESCALATED to
  the red team — subset-scoped only, no polyvalence declared here.
- **F130 — battery-PROMOTE: W1 decides for CE under the corrected
  mapping** (battery-w1-314-rebar; W1 = 78@313, @307-321, row a2_04).
  All four bar clauses pass: (a) 37-78 is word-internal as the complete
  infinitive complement of modal-24 (84-24-37-78 x2 re-derived
  @310/@473; 24->37 x2 = exhaustive, both inside the 84-24-37
  windows); (b) "37-78-45" single-word refuted — no French
  "X-verdict" infinitive exists, and the @475 control (byte-identical
  left context 84-24-37, 78@476 followed by 74, not 45) strands 78
  word-final; (c) the CE parse is grammatical with zero non-granted
  assumptions beyond provisional 59='est' ("qu'on [modal]
  [infinitive]. ce qui est [32-predicative] ne [06-ent] la [92]…");
  (d) all three dict parses shown ungrammatical with stated cause
  each. Forced word boundary before 45 → 45@314 is word-initial 'ce'
  (A11 HOLD; the 45-64 mirror leg stays intact). Scope: W1 and the
  84-24-37 family only (W2/W3/W4 untouched; dict-78-45-wordbound owns
  the global boundary, rpos-w1-exception owns the refined positional
  rule — both queued). Enlightenment: W1 falsifies unconditioned
  R-pos (45='dict' iff preceded by 78 — 45@314 is preceded by 78 yet
  parses 'ce', because 78 is word-final here); R-pos was never adopted,
  and the sibling w1-314-ambig (N119) recorded the bar's original
  consequence mapping as inverted — this rebar promote is under the
  corrected mapping.

### DECODE R5005 render (2026-10-08 — new render files, not a new decode)

`decode-current.txt` and `decode-sidebyside.txt` — the lane's current
best decode rendered from the 1,847-pair repaired stream.
Notation: plain = banked/promoted; `?` = provisional or battery-lead;
`[NN]` = unknown group; `<X>` = class only. Header self-reports ~1/3
of groups readable, the rest holes — visible as dense `[NN]`
brackets even in heavily-banked rows. Status markers encode this
wave's verdicts: `ce/dict?` = the unresolved 78-45 fork (R-pos
falsified at W1 by F130/N119), `le?` = the S5-fence under red-team
pressure (N114), `ver?` = the 78='ver' LEAD (R16-005), class tags
(`<INF>`, `<verb>`, `<noun>`) = this wave's class promotes (97,
92-subset, 21).

### Round-17 wave-11 mid-sweep arrivals (7 battery notes landed during this
sweep, folded here to close the gap; red-team ratification pending)

Notes trace: `code/crowd17/report_inbox/` (dict-45-circle-break,
importe-30-elision-test, le-qui-distributional, lon-on-elision-control,
prenne-R3-relative-341, stem-44-1839, w3-01-adjudicate). 3 promotes,
1 kill, 3 nulls — verdict tags in
`code/crowd17/next-token/battery-queue.json` match 7/7 (335 entries:
154 verdict, 181 queued).

- **F131 — battery-PROMOTE (distributional census): the 'le qui'
  violation class is systematic** (battery-le-qui-distributional; the
  mirror battery to F126 on the 64 axis — does not duplicate F126 or
  F128). Census of article-candidate + 64 bigrams: the violation
  recurs, not isolated to 37. Anchors: 64='qui' promoted, 87='ce'
  promoted, 45='ce' held (A11), 11='la' banked, 77='le' provisional.
  SCOPE LIMIT (explicit): does NOT decide S5, does NOT assign any
  value to 37, does NOT adjudicate 77='le' (the @790 classification is
  conditional on it), and the three 37-64 anchor windows stay
  provisional-dependent exactly because of the S5 fence (not
  re-adjudicated here). No standing fence or red-team verdict
  overturned. Follow-ups: none (promote; adverse answered inside the
  battery).
- **F132 — battery-PROMOTE: 01@984 = 'en' (the never-downgrade
  adjudication)** (battery-w3-01-adjudicate). The bar's discriminator
  fired: R2 ("en" reading) parses with no extra assumptions beyond
  standing verdicts; R1 (01='-ci') needs >=1 extra assumption (novel
  un-named '-ci' environment + NULL-conditional 'dict' leg +
  mutual-conditionality re-count + load-bearing NULL 78='ver'). The
  loser, '-ci' demonstrative suffix at @984, is FENCED with stated
  cause: '-ci' un-named at every grade; ci-bound-01 restricts bound
  '-ci' to ce-adjacent positions; the post-nominal demonstrative
  environment is new and untested (ci-demonstrative-census queued).
  R1's 'verdict' composition is load-bearing on unsettled 78='ver'
  and re-counts a window already conditionally counted by
  ver-78-rebar (the dict-45-w3-ceci circularity finding) — no
  independent leg added. This CONFIRMS F124's standing battery promote
  of 01="en" — the adjudication the never-downgrade rule required
  before either value could promote. Scope: 01@984 only; 01='en' stays
  local to the three 01-24 windows; 01@988 not named; fenced ceci
  frames untouched. No queue verdict downgraded (A4, A11, A8 relied
  on; R16-005 LEAD, ver-78-rebar NULL, ci-01-value kill all left
  standing).
- **F133 — battery-PROMOTE (instance-scoped): whole-word nominal-head
  44 at @1839** (battery-stem-44-1839). Decides the @1839 instance
  only — names no value for 44, takes no position on @1714. The
  global question (whether whole-word nominal-head status at @1839
  and the other 12 whole-word windows, together with the clitic-slot
  forcing at @1714, requires a second value/polyvalence declaration
  for 44 under §7) is already owned by the red-team docket
  (poly-44-docket, escalate-44-deframe — regenerated by N104 and
  de-frame-44-83-21): flagged here, not decided, not re-litigated,
  not contradicted; no standing verdict downgraded. All numbers
  re-derived from the repaired 1,847-pair stream in-work (n(44)=15,
  n(42)=20, '42 44' x2 @1617/@1838, 42 censuses, window bytes
  @1830–1846/@1615–1621).

### Housekeeping (this sweep, continued)

- The 18 mine-v3/corpus copies recorded as removed in the wave-6
  deltas were RE-DOWNLOADED by the corpus miner during this sweep
  (all 14× Allgemeine Zeitung 1841-01-12..25 + Guizot t1–t3 +
  Talleyrand v1 present again) — noted here so the record stays
  honest; the corpus worker owns that directory.
- Push note: the first push attempt raced a transient lock file
  (`locks/stem-44-1839.lock` deleted between listing and upload);
  the re-run pushed clean — commit `86c4e659` (main), 34 blobs
  uploaded, 1,737 reused.

---

### Offset-validation (crowd18, 2026-10-08 UTC — bedrock validation of
the 70 row offsets)

Independent bedrock validation of
`code/side-keyhunt/repaired_offsets.json` (70 binary pair-phase
offsets): **STANDS WITH CAVEATS** — the 1,847-pair stream does NOT
require rebuild. Mechanics verified, concurring with the
`code/bedrock/` fleet: 70 rows, 3,764 digits, 1,847 pairs, 96 groups;
the C1 convention is forced by (3764−2·1847)=70; the carry-over
alternative is falsified at 1,866 pairs; no offset is definitively
falsified. Grades: **CONFIRMED 6** (a5_03 gloss-i, a8_05 gloss-ii,
a6_03 crib repeat, a2_01/a6_04/a8_09 formula repeat), **PROBABLE 24**
(LOO margin >+5 nats), **PROBABLE-WEAK 15** (+2..+5), **UNRESOLVED
25** (15 weak + 8 LOO-negative + 2 flagged). The strongest
independent check is the 3-occurrence formula `9883829621`: one
10-digit string, three rows, three offsets (1,1,0), all pair-aligned
as the same five groups 98-83-82-96-21 ("vient de me parvenir" stem
+ homophone) — P(chance) ≈ 0. **Two offsets FLAGGED for red-team
adjudication (do NOT flip without adjudication):** a4_01 and a5_07 —
repeat `7778948206` (4×) is pair-aligned as 77-78-94-82-06 in
a6_10/a7_05 but not here; two coherent readings exist (one formula
4× → off 0; two formulas 2× each → off 1 stands); LOO supports off 1
(+7.02/+6.51). Consequences: "68 of 70 offsets unvalidated" is
SUPERSEDED; LOO is proven unreliable for overturning (it
contradicts formula-confirmed a8_09 at −4.21 nats; the gloss
overruled EM on a5_03 at −7.17); EM error rate = 1 proven error in
70 (a5_03, corrected by gloss) — do not re-run EM flips without
manuscript evidence. Notes for downstream: the 21 even-length rows
with offset 1 are NOT transcription errors (the formula repeat
forces a2_01=1 and a6_04=1 on even-length rows — even+1 is a real
phenomenon in this transcription); within-block phase propagation
holds for only 33/62 consecutive line pairs (≈ chance) — lines are
pair-phase independent, do not assume reading order from file
order. `repaired_offsets.json` left untouched (a4_01/a5_07 remain 1;
this sweep verified the file still carries 70 binary offsets, 39×0 /
31×1 — a same-day re-write was content-identical). Trace:
`code/crowd18/report_inbox/processed/offset-validation.md`.


- **Housekeeping:** `repaired_offsets.json` rewritten 2026-10-09 09:12
  UTC — content-neutral. Re-verified 70 offsets, 39×0 / 31×1,
  byte-matching the record above (a4_01/a5_07 still 1 and
  flagged-but-unflipped per the red-team adjudication rule; a5_03=0;
  formula-confirmed a2_01=1, a6_04=1, a8_09=0). No byte-diff possible
  (the lane keeps no git history); verification rests on the exact
  match to every named special case.

### Smith rebuild2 status (2026-10-08 UTC — rung-C clean re-run PASS;
memorization re-probe CLEAN)

`code/side-homophonic-rebuild2/track-d/rerun-rungC-clean/` —

- **RUNG-C CLEAN RE-RUN — VERDICT: PASS** (declared 2026-10-08 ~01:56
  UTC; `VERDICT.md`, `MECHANICAL-SUMMARY.md`). 126/126 calls verified
  (108 binding + 18 diagnostic). Binding: truth wins per-pair majority
  on **36/36** truth-vs-salad pairs (bar ≥35/36); every pair unanimous
  3–0 across the three independent judges. Diagnostics: paraphrase
  wins 6/6 truth-vs-paraphrase (expected, non-binding).
- **Red-team audit: ADMISSIBLE** (`REDTEAM-AUDIT.md`, 9/9 integrity
  checks pass — prompt pin d907c592…020ceb, label blindness, temporal
  key ordering, position randomization, disk-first, pair construction,
  tripwire, completeness, single-coordinator). Confidence-uniformity
  CONCERN RECORDED: judge 3's passes 2–3 are byte-identical copies of
  pass 1 (14/14 pairs) — not independent; choice data is robust even
  under the strictest independence weighting (7 genuine votes/pair —
  every binding pair still truth-unanimous). Documentation gap (judge
  commissioning unattested) closed by `COORDINATOR-ATTESTATION.md`
  (single coordinator commissioned all 3 judges; fresh, brief-only
  sessions).
- **Ladder consequence** (PREREG-D-v3-ladder.md §4): strike one
  CLEARED; the v3C pairwise instrument is ACCEPTED as the Track D
  judge instrument; strike two NOT recorded; SPS fallback NOT met.
  Next: step-4 clearance re-requested
  (`redteam/STEP4-CLEARANCE-REQUEST.md` — Branch-B funnel on the 6
  ORIGINAL control instances only; R5005 and the 6 gate instances
  184201–184204/184206–184207 stay sealed). Charter updated
  (`FLEET-CHARTER.md`, 01:53 UTC — the "2026-10-08 ~01:56 UTC — RUNG C
  PASSES" entry; note its last line says the probe is "still parked"
  — STALE relative to the jsonl below).
- **Memorization re-probe — seal paradox RESOLVED, verdict CLEAN.**
  Red-team ruling (a) (`redteam/RULING-MEMORIZATION-REPROBE-SEAL.md`,
  binding): the key-holding trusted party (fresh, track-isolated)
  decodes the 6 fresh instances for the SOLE purpose of building the
  12 probe candidates — this is the protocol's prescribed containment
  (R12e/R14f), not unsealing. Key-holder delivered the frozen 12-string
  package (`track-d/memorization-reprobe-candidates.json` track-visible,
  `track-d/memorization-reprobe-key.json` sealed); the
  `no_probe_inputs` blocker CLEARED. Probe ran 36/36 valid calls:
  **verdict CLEAN** — 12 labels accounted (6 truth + 6 paraphrase),
  margins mT−mP −77..−85 per seed (void rule ≥15 NOT tripped)
  (`track-d/memorization-reprobe-20261007.jsonl`, 2026-10-08
  seal_status + sealed_scoring records). No memorization signature on
  the gate truths.

### crowd15/next-token calibration + track-b training (2026-10-08 UTC)

- **models rebuilt**: `code/crowd15/next-token/models/seebach_nexttoken.db`
  (1001.1 MB, built 1101s, EXIT=0 — `build.log`): standard
  4,037,445 cells / 1,561,980 ngrams / 16,742 unigrams; byear
  4,136,570 cells / 1,589,159 ngrams / 16,754 unigrams (11 corpus
  texts: Guizot t1/t3/t5–t6, Nesselrode v7–v10, Pozzo, RDM 1841 q1–q3).
- **Calibration LANDED** (2026-10-08 ~05:03 UTC — `calibrate.json`
  was EMPTY at the last sweep, now complete): held-out = 3 whole
  documents (Guizot t2, RDM 1841 q4, Talleyrand v1 — `heldout_files`).
  **A. Global next-cell accuracy**: standard n=19,998 — top-1 0.3207,
  top-3 0.4584, top-5 0.5218, MRR 0.4183; by-ear n=19,999 — top-1
  0.3342, top-3 0.4718, top-5 0.5366, MRR 0.4318. **B. Solved-context
  ranks** (standard; cell top-1/top-5): "la première" (198 occ)
  0.263/0.419; "par ce que" (77) 0.130/0.519; "par le" (820)
  0.245/0.354; "qui" (7359) 0.106/0.307; "que" (17027) 0.175/0.421;
  "ce qui" (637) 0.141/0.342; "en ce" (117) 0.299/0.547; "m'en" (95)
  0.084/0.242; "ne" (12585) 0.320/0.484. **C. Verb-stem ranks**
  banked in `calibrate.json` (verb_stems: 12 standard, 12 by-ear).
  **D. By-ear mismatch quantification** (200k-word sample): word
  disagreement rate 0.1107; cells/word 1.659 (standard) vs 1.700
  (by-ear); vocab jaccard 0.887; 1006 by-ear-only cells, 994
  standard-only cells. Banked-cell ranks diverge hard on vowel-splits:
  "er" rank 731 (std, count 544) vs 14 (byear, 48759); "m" 71 vs 18;
  "i" 82 vs 16; "e" 9 vs 2 — the by-ear mode splits vowel clusters
  the standard mode glues. Trace:
  `code/crowd15/next-token/calibrate.json`.
- **track-b neural LM** (`track-b/train.log`, mtime 2026-10-08
  ~05:10 UTC — running live): update 14,100, epoch 7, train EMA
  ~2.014, best heldout **2.0138 @upd 14,100** (`ckpt.json`;
  86,630,400 chars seen). Held loss still declining (2.0198→2.0138
  over updates 13,200–14,100).
- **Period corpus expansion** (side-period lane): 18 new texts in
  `code/side-period/work/mine-v3/corpus/` — 14× *Allgemeine Zeitung*
  (Augsburg) 1841-01-12 through 1841-01-25, Guizot *Mémoires* t1–t3
  (Gutenberg), Talleyrand *Mémoires* v1. Era- and register-matched
  reference material for the H3 program (not yet wired into any
  calibration run — provisional until measured). **Cleanup
  2026-10-08: those 18 mine-v3/corpus texts are absent since the last
  sweep; the same filenames exist in `code/side-period/corpus/` — the
  working corpus is unchanged.**

### table-grid registry (2026-10-08 07:21 UTC — coordinator merge)

`code/table-grid/table-registry.json` — coordinator source of truth for
the R5005 key-table grid; status set: gt (pencil ground truth), prom
(promoted), prov (provisional), cls (class), lead (battery-level,
red-team ratification pending). **Coordinator merge 2026-10-08 ~07:21
UTC** — the registry now carries the round-17 battery verdicts as
leads: 12="n" lead, 30="pas" lead, 39="a/a" lead, 45="ce/dict" lead,
48="e" lead, 94="ne" lead, 06="ent/ment" lead, 00="pour" prom
(banked, round-16); 77="le" DEMOTED prom->prov (round-16); 78="ver"
lead (78="er" KILLED round-16); standing 11/29/34/40/46/70/82 gt,
17/47/79/64/87/96/84 prom, 31/33/86 cls, 59="est" prov. Full cells:
00="pour" prom, 06="ent/ment" lead, 11="la" gt, 12="n" lead,
17="fois" prom, 29="er" gt, 30="pas" lead, 31=VERBAL cls, 33=INF cls,
34="i" gt, 39="a/a" lead, 40="e" gt, 45="ce/dict" lead, 46="que" gt,
47="ce" prom, 48="e" lead, 59="est" prov, 64="qui" prom, 70="pre" gt,
77="le" prov, 78="ver" lead, 79="tout" prom, 82="m" gt, 84="on" prom,
86=INF cls, 87="ce" prom, 94="ne" lead, 96="par" prom. `generate.py`
ran 2026-10-08 (this sweep): printed **UNCHANGED** — the coordinator
had already regenerated the grid HTML/PNG at merge time; the periodic
table grid is current. Registry is coordinator-owned; batteries keep
feeding it via the adjudication queue.

**Coordinator merge 2026-10-08 13:13 UTC** — the registry is
reconciled against the round-17 red-team adjudication
(`code/crowd17/report_inbox/processed/next-token-redteam-r17.md`): 12="n",
48="e", 30="pas", 06="ent" PROMOTED; 32/24 class grants; 39="/a/"
lead; 94="ne" and 78="ver" stay lead (promote rejected); 62="il"
(F103) and 76=noun (F104) as battery-level leads; 77="le" stays
prov; 84="on" prom, 06 fork closed (supersedes "ent/ment" dual
lead). Grid HTML/PNG regenerated at merge time; `generate.py` ran
2026-10-08 13:14+ UTC (this sweep): printed **UNCHANGED** — the
periodic table grid is current.

**Coordinator merge 2026-10-08 18:27 UTC** — the registry records
the wave-7/8 battery verdicts (36 cells): 26=["noun","lead"] (F113,
conditional on the 11="la" determiner phrase), 42=["noun","cls"]
(val-42-nominal), 88=["gov","cls"] (governor-88-value), 89=["noun",
"lead"] (class-89-adjudicate packaging; infinitive killed by
val-89-mirror); 44 skipped — noun-killed (wave-7 battery-noun-44)
but gender-44 (F118) adjudicates masculine: unresolved tension,
recorded in `_meta.note` for the red team. The grid HTML/PNG carry
the merge-time regeneration (mtime 18:27:41 UTC); `generate.py` ran
this sweep (per coordinator): printed **UNCHANGED** — the periodic
table grid is current.

**Coordinator merge 2026-10-08 21:25 UTC** — the registry records
the wave-9 F122 battery-PROMOTE: cell **21=["noun","cls"]** added
(`_meta.note`: "F122 (2026-10-08): 21=NOUN class battery-promote").
All other cells unchanged from the 18:27 merge. The grid HTML/PNG
carry the merge-time regeneration (mtime 21:25:41 UTC); `generate.py`
ran 2026-10-08 ~23:16 UTC (this sweep): printed **UNCHANGED** — the
periodic table grid is current. Registry is coordinator-owned;
batteries keep feeding it via the adjudication queue.

**Sweep 2026-10-09 ~11:20 UTC** — `code/table-grid/table-registry.json`
unchanged since the watermark (mtime 03:03:21 UTC); the grid HTML/PNG
are the coordinator's 03:03 UTC regeneration. `generate.py` ran this
sweep: printed **UNCHANGED** — the periodic table grid is current.

**Round-19 red-team merge 2026-10-09 12:16 UTC** —
`_meta.round19`: 11 new cells — 68=[noun,cls] (R19-107),
69=[noun,cls] (R19-109; 'ce' value-lead R19-110),
63=[verb,cls] (R19-102), 38=[verb,lead] conditional (R19-029),
35=[noun,cls] (R19-050), 43=[noun,cls] (R19-045; @21
excluded/fenced R19-064), 83=[de,lead] conditioned 11-window scope
(R19-128), 93=[verb,cls] (R19-166), 98=[verb,cls] (R19-171/176;
'vient' value-lead R19-172), 03=[verb-stem,cls] scoped to '03 29'×3
(R19-178), 58=[nominal,cls] (R19-185). 76 lead→prom, masculine
(R19-111). 62 ['il','lead'] REMOVED ('il' killed at kill grade
R19-106). 24 DECLARED as S7 exception: 24='en' iff follower=85,
verb elsewhere (R19-191); R_et3 retired. 43 and 44 polyvalence
declarations REJECTED (R19-064, R19-066); 94 split rejected/CLOSED
(R19-167); 89 infinitive rival killed, noun lead ratified (R19-161);
corpus-search rule: whitespace-normalized search required for corpus
zeros (R19-063). Registry is now 50 cells (7 gt, 13 prom, 20 cls,
8 lead, 2 prov). The grid HTML/PNG carry the merge-time
regeneration (mtime 12:16 UTC); `generate.py` ran this sweep: printed
**UNCHANGED** — the periodic table grid is current.

**New asset `key-table-history.gif`** (136 KB, 560×709, 8 frames,
2026-10-09 13:00 UTC): an animation of the R5005 key-table grid from
2026-10-08 01:35 UTC ("16/96 cells banked") through the round-19
red-team state at 2026-10-09 12:18 UTC ("50/96 cells banked");
captions quoted from the file. Maker not recorded in the lane
(provenance unknown — no generating script found in `code/`).

### Round-18 red-team adjudication addenda (2026-10-08 UTC — 29 batteries
adjudicated; red-team ruling AUTHORITATIVE)

Adjudicator: red team, kill authority. Scope: 29 unprocessed promote
verdicts (all queue targets with status=verdict/result=promote not
adjudicated in rounds 15/16/17). Stream: repaired 1,847-pair parse.
Ten review lanes ran in parallel (9 claim-family adjudicators + 1
pure attacker); the undersigned red-team adjudicator is the sole
conflict-resolver. Every number below is the red team's own
re-derivation from `data/upstream-ct_R5005.txt` +
`code/side-keyhunt/repaired_offsets.json` (anchors: 1,847 pairs /
96 types). Trace:
`code/crowd17/report_inbox/processed/next-token-redteam-r18.md`.

- **F123 — GRANTS (R18-001, R18-022, R18-027 — registry cells):**
  65="noun" CLASS-tier (R18-001; qui-relative head @1208 with
  verb-65 kill-grade ungrammatical, que-relative @1253, post-verb DO
  @812/@1383; @724 struck as anomaly; conditional on 59="est"
  provisional; participle rival fenced as caveat — value open);
  92="verb" CLASS-tier, SUBSET-SCOPED (R18-022; 8/8 verbal-governor
  windows @49/@66/@330/@593/@978/@1154/@1379/@1453 parse with zero
  new forced contradictions; @1154 "pour [92]er [80] fois" the
  smoking gun; 'la'-governed ×3 + @683/@1022 residuals fenced;
  global class HELD pending the §7 split question); 36=NOUN
  CLASS-tier (R18-027; "par ce [36]" @1215 forces nominal on
  A11-hold + promoted 96; "pour [36-ADJ]" ×3 ungrammatical;
  infinitive/adjective excluded as single-class readings; "est
  [36]" legs honestly marked provisional-59-dependent). Registry:
  +36=["noun","cls"], +65=["noun","cls"], +92=["verb","cls"]
  (subset note in `_meta`); 40/96 cells now represented.
- **F124 — GRANTS, frame/finding/evidence tier (no registry cells):**
  86 residual disposition (R18-002: both residuals take verb-valued
  followers, fenced with byte-level cause — the AMENDED RULE itself
  is RECORDED AS PROPOSAL, not promoted; self-grading bar; §7
  declaration HELD); 37-78 conditional unit/frame (R18-003; 37-78
  ×4, followers four distinct groups, 78 word-final at W1 via the
  exclusive 24→37 frame — bar-calibration warning recorded; does not
  weaken R16-005); noun26 fragment constructional (R18-004; @1733
  parallel proves "30 06 60" left-independent; "pas" heads RIGHT of
  the forced 26|30 boundary — R17-011 re-scoped ×4→×3 with NEW byte
  evidence, declaration stays HELD); le-par calibration (R18-005:
  article+promoted-preposition violation ×2 — @913 S5-conditional,
  @997 S5-independent on banked 11 + promoted 96; prejudgment warning
  logged); le-qui calibration (R18-006: "le qui" on 37 ×3
  S5-conditional + 77 ×1 doubly-conditional; @790 logged as potential
  adverse for provisional 77="le"); ceci @983-986 restricted frame
  (R18-007: "ceci [24-modal] [89-inf]", A11-conditional; wins the
  @984 triple-count); 44="l'" window-local @1714 (R18-010;
  conditional; 44 NOT promoted globally); 44@1839 whole-word
  segmentation (R18-011; "42 44" two-token adjacency); 29
  word-initial finding (R18-012: "qui erre" @291/@685, "cela erre"
  @500 — the @146 un-fence KILLED, @147 parse invalid); 84-successor
  census evidence package (R18-013; 84→29 ×1 @146 unique resister);
  W1 "ce qui" fork-window adjudication (R18-014; corrected 2-vs-3
  assumption count; installs 45="ce" at @314 — NOT 45="dict");
  W1 conditional structural (R18-015; clause (c) corrected to
  {78="ver" LEAD, 59="est" provisional}); 37 value-race ranking
  (R18-016: verb > adjective > "le" > stem > noun; no value named);
  24-87-64 formula frames (R18-017); "pasent"-spelling kill-grade
  (R18-018: "30 06" ×4 hardened genuine residuals); lever era gate
  (R18-020: zero absolute-"lever"="rise" attestations in 17th–19th
  c. authorities, with corpus-count + Acad.-6e caveats); 94
  verbless-family census (R18-021: 9/28 reproduced exactly; @508
  re-framed as non-particle candidate); 68-predecessor typicality
  (R18-024: M1=1.0 typical of thin cells, not anomalous); 37-11
  window-disposition (R18-025: @51/@1655 fenced as genuine
  S5-straining residuals; does NOT preempt the "la tout" docket);
  rpos refined-rule candidate (R18-026: 45="dict" iff 78 word-MEDIAL
  — §7-docket evidence only, no declaration); 45→93 ×3 frame
  (R18-028: governor + "ce" + nominal head); @995 postnominal frame
  (R18-029: "[03-N][60-adj] et[67] la[11]").
- **F125 — LEADS granted (R18-008, R18-023; `_meta` only):**
  24="faire" value-candidate (conditional on R17-009; rival
  "laisser" LIVE — the uniqueness proof is broken); 01="en" local
  to @40/@828 only; 60~68 shared free frames (census fact — NOT a
  homophone claim; the pair-60-68 kill and thirds-60-68 null stand).
- **F126 — REJECTS (R18-008, R18-009, R18-019, R18-023):**
  disc-01-24-ci-X promote REJECTED (salvaged as the F125 leads +
  byte-verified findings); w3-01-adjudicate promote REJECTED —
  01@984="en" FENCED as the adjudicated loser (wrong rival tested;
  destroys the R17-015-fenced 45-01 "ceci" frame); en85-gerund
  REJECTED (undeclared overwrite attempt of standing R17-009 on
  identical windows — "A3 ground truth 24=en" overstates the
  record); frame-97-profile REJECTED (INF/N tie at the R17
  class-promote standard; finite-verb kill + @299 fence stand as
  sub-findings).
- **Standing revisions with new byte evidence:** R17-011 "'26 30'
  [verb] pas" re-scoped ×4→×3 (@1560 excluded — the @1733 parallel
  is new); noun26-1560-pas residual RESOLVED. @146 un-fence attempt
  KILLED (@147 parse double-consumes granted 87="ce").
- **Docket notes (NOT resolved):** @997 "la par" joins "la tout"
  @52-53 as a banked-value contradiction; @790 as potential adverse
  for provisional 77="le"; the 86 amended-rule and 26 positional-rule
  declarations remain HELD under §7 (67 sole polyvalence).

### Round-17 wave-12 addenda (2026-10-08/09 UTC, crowd17 — 85 battery notes;
red-team ratification pending)

85 notes trace: `code/crowd17/report_inbox/` (all new this sweep — 85
files, incl. 11 that landed while the sweep ran). 17 kills, 3 promotes,
65 nulls — verdicts entered in `code/crowd17/next-token/battery-queue.json`
(465 entries: 267 verdict, 198 queued at read time; the fleet is
adding follow-up targets in real time).

- **F134 — battery-PROMOTE (locus-level): "69 11" @1115–1116 = one word,
  "cela"-shaped** (battery-cela-69-11-word). The locus parses as one word
  with 69 in the "ce"-class; no conflict with standing verdicts, no
  adverses listed. Global 69 value stays OPEN — not banked, not promoted.
- **F135 — battery-PROMOTE (locus-level): "61 40 17" @1556 reads "première
  fois"** (battery-val-61-premier). 61 = "premier"-stem at this locus
  only; the global-61 value question is DEAD at the same wave
  (val-61-contact, N139) — locus promote and global kill coexist,
  no downgrade either way.
- **F136 — battery-PROMOTE (evidence-package grade): byte-exact map of
  ungrammatical-"ne" windows** (battery-ne-particle-ungrammatical-sweep).
  The complete map is produced with byte-exact @-offsets on the repaired
  1,847-pair stream, no adverses. Scope explicit: an evidence package for
  the red-team 94 duality adjudication, NOT a value claim — it does not
  promote 94="ne" globally.

Methodology notes (this wave, first-class per REPORTING.md): every worker
re-derived counts on the repaired 1,847-pair stream (`repair_parse.py`);
`canonical.py` never touched; R5005 and sealed gates untouched; bars were
pre-registered with numbered clauses, frozen before data examination, never
modified after; value status was marked on every use (pencil/granted/
promoted/provisional/battery-promoted-unratified); kill grade means a
window forces the claim false — not just "no evidence"; conditioned splits
need red-team approval (§7 sole-polyvalence law) — batteries package,
never grant; residuals fenced with stated cause and a named venue, never
ignored. Enlightenment moments: spelling repair can fit perfectly and
still die distributionally (14="souv" gives exact "souvent" at both
windows, but @586 kills it — N136); the mannequin letter-family died on a
concrete dictionary fact — 62-48 ×6 reads "mane", which is not a French
word ("crinière" is) (N130); a value verdict can die while its class
verdict stands (the suite-21 value kill vs the untouched 21=NOUN class
verdict, wave 11).

### Round-17 wave-13 addenda (2026-10-09 UTC, crowd17 — 100 battery notes;
red-team ratification pending)

100 notes trace: `code/crowd17/report_inbox/` (75 new) and
`code/crowd17/report_inbox/processed/` (25, verdicts never folded before
this sweep). 17 kills, 36 promotes, 47 nulls — verdicts entered in
`code/crowd17/next-token/battery-queue.json` (548 targets: 363 verdict,
185 queued at read time).

- **F137 — battery-PROMOTE (battery grade): preposition-vs-verb decided
  for VERB on 88** (battery-88-prep-rival). Six independent frame-legs
  decide verb ("à [88]" x2, "[88]er" @1050, "ne [88]" @1707,
  "faire [88]" @43, "la [88]" @1118, "ce [88]" @403); zero legs for the
  preposition reading — the prep rival is dead by census exhaustion.
  Dependency: legs C/D/F ride on battery-promoted 24="faire", the
  R17-001 94="ne" STRONG LEAD, and the A11 45="ce" HOLD — all unratified.
- **F138 — battery-PROMOTE (frame-leg finding): 60 as postposed adjective
  at all four "21 60" windows** (@119/@172/@197/@232)
  (battery-adj-60-2160). Adjective is the unique surviving class at each;
  noun killed globally (standing), verbal fails at all four. No value
  named, no polyvalence declared — evidence arm for queued pri-1
  poly-60-redteam.
- **F139 — battery-PROMOTE (locus-level): the lone "-ment" adverb
  "[18]ment pour [36]" @737** (battery-adv-18-ment). 18 forced to
  adjective-stem by elimination (five rival functions dead); "82 06" n=4,
  three verbal — this is the sole adverbial window. No global naming
  of 18.
- **F140 — battery-PROMOTE (census-finding package): the 22-window
  positional account of 45** (battery-allophone-45-scoping). 18 "ce"
  windows (incl. the three "ce qui" mirror legs @315/@341/@1025), 3
  "dict"-syllable windows at post-78 positions (the certified "verdict"
  host set), exactly 1 fenced residual (@315). {13,01}-exclusivity
  byte-exact. Gather-only: the positional declaration stays escalated to
  the red team.
- **F141 — battery-PROMOTE (narrow sensitivity finding): the
  {13,01}-exclusivity survives leave-one-out at p<0.05 in all four
  tables** (battery-boundary-45-exclusivity-sensitivity). Hardens the
  contact-profile leg of the 78-45 boundary; promotes no value.
- **F142 — battery-PROMOTE (census finding): the 78-45 "verdict" value
  arm has exactly one conditional leg** (@574, "ce verdict")
  (battery-boundary-value-census). The other three loci are accounted for
  (@314 = A11 "ce" resolved; @983 fenced neutral; @1165 double-residual).
  "Four 78-45 windows = four legs" is retired at battery grade.
- **F143 — battery-PROMOTE (finding grade): the "86 never ce" arm
  hardened** (battery-ce-complement-86-negative). No ce-group complement
  attaches to 86 anywhere in the stream; promotes no value, kills
  nothing.
- **F144 — battery-PROMOTE (guard success): the 59-cell partition
  re-derives 26/27 from pre/successor cells alone**
  (battery-classification-sweep). Single disagreement (@826) explained by
  standing red-team ruling I3, not a data error.
- **F145 — battery-PROMOTE (census finding): the complete 44 slot
  census** (battery-clitic-44-census). Sole clitic-slot window @1715;
  14 whole-word nominal, 2 word-internal stem — all on standing values.
  Names no value.
- **F146 — battery-PROMOTE (package): the conditioned 83="de" candidate
  packaged for red-team adjudication** (battery-de83-condition-set).
  11 non-contested windows with 4 exclusions and causes; does NOT promote
  83="de" — the unconditioned kill at @911 (fence-911-de) stays owned.
- **F147 — battery-PROMOTE: 06's left-attachment bimodality resolved as a
  census** (battery-ent-06-host-census). States per-window whether 06 is
  a finite ending or a syllable across 06's 44 windows (28 preceder
  groups); coordinates with the ent-06 06="ent" promote.
- **F148 — battery-PROMOTE (function-scoped): 48 as feminine/inflectional
  "-e" in the 32-48 x4 and 19-48 x1 frames** (battery-fem-e-48). Promotes
  48's function at these frames only, on top of the R17-003 48="e"
  letter-tier grant; names no value for 32 or 19.
- **F149 — battery-PROMOTE: the 12-48 "ne" census restated and
  byte-confirmed — exactly 5 windows** (successors 21/71/24/77/52)
  (battery-ne-census-1248).
- **F150 — battery-PROMOTE (class-level): 81 = masculine abstract noun**
  (battery-noun-81). Legs: "le [81]" x3 (@1242/@1403/@1600) inside the
  "67 77 81" x4 frame; "81 pour [INF]" x2 purpose-complement diagnostic.
  Value open. 81="prin" kill (§7) untouched.
- **F151 — battery-PROMOTE: the trigram minimal pair confirms both
  branches of the noun-26 positional rule**
  (battery-noun26-trigram-minimal-pair). Same surface string is
  verb-phrase-internal where the rule says verb, noun-boundary-crossing
  where it says noun. Packages R18-004 + rescoped R17-011.
- **F152 — battery-PROMOTE: the par-43 kill is terminal**
  (battery-par43-adverbial-attestation). The last escape — bare "par
  mesure"/"par condition" adverbials — is closed by the lane's corpus bar
  (Littré + TLF). Pending only the @21 polyvalence adjudication (red-team
  territory; battery-43-29-segment, F166).
- **F153 — battery-PROMOTE (class-level): 35 = noun** (battery-prof-35).
  Value open, number undetermined.
- **F154 — battery-PROMOTE (profile grade): the full 28-occurrence
  neighbor profile of 37 published**
  (battery-s5-37-distributional-profile). Bounds the rival-value search
  space; no value declared.
- **F155 — battery-PROMOTE (discriminator success): the @1205 7-gram
  decided as bare stem — 55-61 = "prend" + noun object**
  (battery-seg-55-61-21-stem). Promotes no value, kills no value; the 61
  internal letters ("re"+"pren"+"ne" vs "pre"+"nd") are tensed, not
  declared — a §7/red-team segmentation question.
- **F156 — battery-PROMOTE (sweep finding): offset-1 is constraint-clean
  across all 35 pairs of row a1_01** (battery-seg-a1_01-constraint-sweep).
  Zero new kill-grade violations; dissolves the "la tout" banked
  contradiction. Adopting it is a red-team act — not declared here.
- **F157 — battery-PROMOTE (class-level): 03 = verb stem**
  (battery-stem-03). Value stays open. Standing note: 17 windows are not
  all verb-compatible (stem-03-value NULL stands) — a single-valued stem
  needs the noun-family to re-segment, else a §7 split question.
- **F158 — battery-PROMOTE (finding grade): W1's "ne mentent" clause is
  confirmed subjectless as a fenced residual**
  (battery-subj-w1-573-reroute). Non-13 routes exhausted; closes the
  subject hunt at battery level; the strained frame belongs to the
  red-team 94-duality adjudication.
- **F159 — battery-PROMOTE (finding grade): 71 is a §7 split candidate —
  nominal@1337 vs non-nominal@925** (battery-val-71-quant-nominal). The
  "65 71" unit rescue refuted on row-boundary and grammatical grounds.
  Split declaration is a red-team act.
- **F160 — battery-PROMOTE (census finding): determiner-profile is the
  frame's surviving content for the 78-83-cede frame**
  (battery-ver78-ce78-census). The successor-completion formulation
  retires; 78="ver" stays LEAD, 45="dict" stays lead.
- **F161 — battery-PROMOTE: two positive "ce ver e" legs for 78=@364/@819,
  one byte-identical** (battery-ver78-non45-positive-leg). The 4-gram
  "76-47-78-48" occurs twice (@362–365, @1395–1398); 45 uninvolved at
  both. Dependency: one leg rides on battery-promoted (unratified) 48="e".
- **F162 — battery-PROMOTE (finding grade): the pas-30 "Parses." marks
  mechanized** (battery-w2-pas-nelicense). Audit of the 4 ne-less "pas"
  windows: no rival mechanism covers ≥2; confirmed precedent — bare "pas"
  carries negation, "ne" is dropped as the cipher's normal habit (16/19
  "pas" windows lack "ne").
- **F163 — battery-PROMOTE: the W4 determiner gap is lane-law over the
  decidable set** (battery-w4-det-gap-census). 38 67-loci: 9 are 67="veut";
  of 29 et-loci, 9 decidable, all nine compose non-noun ("et la" x4, "et
  que" x2, "et qui" x2, "et par" x1); the sole granted noun 17="fois"
  never follows 67.
- **F164 — battery-PROMOTE (finding grade): 56 is the finite verb negated
  by bare-"pas" @1733** (battery-w5-pas-verb). Class-level, value open.
- **F165 — battery-PROMOTE (gate fired): the merge condition failed —
  55-61 is not the W1 subject** (battery-merge-gate-w1-x55-61).
  Else-branch executed: the subject-reading of X is killed as a merge
  hypothesis; name-55-61-core re-scoped to the W2/W3 frames only.
- **F166 — battery-PROMOTE (segmentation only): @21 "43 29" is
  word-internal "[43]er" — "qui vient me [43]er", an infinitive in the
  "vient me + INF" frame** (battery-43-29-segment, processed). 43 keeps
  noun standing in 15/16 windows; the @21 verb-stem shape is escalated to
  the red team (redteam-43-polyvalence, P1), not banked.
- **F167 — battery-PROMOTE (locus-level): 88 is infinitive-shaped @1727**
  (battery-88-1727-shape, processed). Continuation B ("vient à [88]")
  stays live for both condition/mesure survivors.
- **F168 — battery-PROMOTE (guard/dispositional): the two 33 orphans
  (@1502/@1642) are disposed to their neighbors (84/12)**
  (battery-croire-33-residuals, processed). The 33 set's 8% orphan rate is
  intact; no third orphan exists; 33 needs no defense under any candidate
  value.
- **F169 — battery-PROMOTE (narrow): "verdict" (78-45) is the sole host
  of 45="dict"** (battery-dict-45-host-inventory, processed). No non-78
  window of 45 parses as a French dict-word. Certification is conditional
  on 74 staying non-"ver"; does not by itself promote 45="dict".
- **F170 — battery-CONFIRM (promote): the "12 94" letter-pairing is
  word-internal ("nne") at both "prenne" windows**
  (battery-enne-family-12-94, processed). @64–65 remains the sole
  word-resistant "12 94". Conditional on the pending 12="n" and 94="ne"
  promotions.
- **F171 — battery-PROMOTE (class-level): 98 = finite verb, decided by its
  follower census** (battery-prof-98, processed). Weaker than the standing
  battery promote 98="vient"; 62-side strain fenced as 62-residuals.
- **F172 — battery-PROMOTE (verb class): 93 = verb** (battery-verb-93,
  processed). Class-level, value open.

Methodology notes (this wave, first-class per REPORTING.md): every worker
re-derived counts on the repaired 1,847-pair stream (`repair_parse.py`);
`canonical.py` never touched; R5005 and sealed gates untouched; bars were
pre-registered with numbered clauses, frozen before data examination,
never modified after; value status was marked on every use
(pencil/granted/promoted/provisional/battery-promoted-unratified); kill
grade means a window forces the claim false — not just "no evidence";
conditioned splits need red-team approval (§7 sole-polyvalence law) —
batteries package, never grant; residuals fenced with stated cause and a
named venue, never ignored; epistemic failures were fenced with stated
cause instead of forced — fence-executed nulls make up a large share of
the live batch (52/75 live notes mention fenced residuals; fences
outnumber kills where evidence is epistemic, never forced).
Enlightenment moments: the same wave can kill a global value and promote
its locus twin (61="pren" global kill, N149, coexists with the F135
locus-level "première fois" promote — no downgrade either way); a value
can die at the very windows that motivated it — 60="dit" parsed @454 and
@1338, its two founding windows, but "ne er dit" @690 killed it (N155);
"par pour" x3 turned a one-window fence into a systematic anomaly once
all three windows were tested; the 13 program collapsed in one wave —
both French "les" arms dead (object pronoun @567, plural determiner
before promoted verb class), closing the uniform-value question
entirely; 44's clitic reading is singleton-grade (1 clitic-slot window
of 16); a near-miss promote can be the kill's confirmation — the
58="ant" promote side reached 2/3 legs but the one kill-grade window
still fired (N141).

**Next-token battery, wave-5 (2026-10-09): 105 verdict notes folded**
(`code/crowd17/report_inbox/battery-*.md`; all dated 2026-10-09; battery
protocol: pre-registered bars, numbered pass/fail clauses, locks
created/deleted, temp-file+rename queue updates of each worker's own
queue entry only, stream re-derived in-session each time — 1,847
pairs / 96 types; `canonical.py` never used; R5005, sealed gates,
red-team queue untouched; no standing verdict contradicted or
downgraded by any note):

- **F173 — battery-PROMOTE (locus-level): 38 adjective-shaped at W2/W3**
  (battery-adj-37-385-gate); determiner arm kill-grade dead at one
  window, so the class question is narrowed, not named.
- **F174 — battery-PROMOTE (locus-level): adj-91-723-03-gate**
  (battery-adj-91-723-03-gate).
- **F175 — battery-PROMOTE: bound-65-64-qui** (battery-bound-65-64-qui).
- **F176 — battery-PROMOTE (finding grade): boundary-40-letter-census**
  (battery-boundary-40-letter-census).
- **F177 — battery-PROMOTE: ce28-contact** (battery-ce28-contact).
- **F178 — battery-PROMOTE (finding grade): class-62-16-windows**
  (battery-class-62-16-windows).
- **F179 — battery-PROMOTE: comp-61-12-leftward** — hardens the @1430
  leg (battery-comp-61-12-leftward).
- **F180 — battery-PROMOTE (finding grade): de83-39-1334** —
  conditional-collision pre-registration for the 39="à" collision
  ("à de [INF]" is ungrammatical in 1841 French).
- **F181 — battery-PROMOTE: de83-adverse-restock** — independent legs
  confirmed.
- **F182 — battery-PROMOTE (finding grade, locus-level): 14 is
  determiner-shaped @117** (battery-det-14-census): "et le
  [21-noun]", row a1_03; class-level determination, value 'le'
  leading. det14-elsewhere (N, below) fences 14's determiner value
  to the frame-tail window.
- **F183 — battery-PROMOTE (census deliverable): distrib-12-
  wordinitial-stream** (battery-distrib-12-wordinitial-stream).
- **F184 — battery-PROMOTE: 31 = VERB class** (battery-edge-340-31-14):
  three frame-legs — "qui [31]" x2 (@338, @1647), "[31]er"
  word-internal infinitive @1257, "e [31-verb] [76-noun]"
  verb+object @1615; value open. The one-run parse of the
  '@337–345 "qui 31 14 ce qui par [43] ce [01]" edge is KILLED
  (N164) — the break lies downstream of both cells.
- **F185 — battery-PROMOTE (finding grade): the 'en' arm for 14 is
  kept at battery grade** (battery-en14-three-window): 14="en" is
  the only letter-strict "m'"+clitic value still viable.
- **F186 — battery-PROMOTE: en43-wordinternal-census**
  (battery-en43-wordinternal-census).
- **F187 — battery-PROMOTE (finding grade, locus-level): erce-1590**
  (battery-erce-1590).
- **F188 — battery-PROMOTE (census/record grade):
  faire-complement-field** (battery-faire-complement-field).
- **F189 — battery-PROMOTE (relational decision, no value named):
  finiteness-88-86** (battery-finiteness-88-86).
- **F190 — battery-PROMOTE: fois-corpus-article-audit**
  (battery-fois-corpus-article-audit).
- **F191 — battery-PROMOTE (recommend ratification by the red team):
  frame-43-pred-37-32** (battery-frame-43-pred-37-32).
- **F192 — battery-PROMOTE (record/feed grade): laisser-89-impact**
  (battery-laisser-89-impact).
- **F193 — battery-PROMOTE (finding grade): lever-lement-rival**
  (battery-lever-lement-rival).
- **F194 — battery-PROMOTE: the 84 ne-follower discriminator holds
  against the widened census** (battery-ne-follower-census-84):
  zero 84→94, 84→48, 84→12 across all 25 granted-"on" windows.
- **F195 — battery-PROMOTE (packaging complete): noun-44-legs-package**
  (battery-noun-44-legs-package).
- **F196 — battery-PROMOTE (finding grade): noun26-38-profile C2** —
  finite-verb-38 is forced at kill grade @1113–1114 ("[65-noun]
  [38-V] pas cela"); C3 and W4 remain open (follow-ups below).
- **F197 — battery-PROMOTE (finding grade): noun26-89-class** —
  fenced split recorded, battery-grade, needs red-team ratification
  (battery-noun26-89-class).
- **F198 — battery-PROMOTE (record grade): par-96-complement-census**
  — the "96 [43]" complement-less windows tabulated (@1026 and
  others); 43's noun readings stay dead per par-43 kill.
- **F199 — battery-PROMOTE (sweep finding):
  phase-likelihood-row-sweep** (battery-phase-likelihood-row-sweep).
- **F200 — battery-PROMOTE (finding grade, evidence package):
  poly-80-x29-frame** — re-segmentation audit of the @1032/@1156
  split packaged for the poly-80-docket.
- **F201 — battery-PROMOTE: pour-00-leftedge-census** — nothing
  re-opens the fenced "96 00" arm (battery-pour-00-leftedge-census).
- **F202 — battery-PROMOTE (finding grade, battery-grade): prof-92**
  — 92's class profile (n=22): "00 92" x6, 92→64 x2; resolves
  npframe-60-1674's budget blocker.
- **F203 — battery-PROMOTE: reseg-13-armA** (battery-reseg-13-armA).
- **F204 — battery-PROMOTE (sweep finding): reseg-1481-98** —
  promotes no value, kills nothing (battery-reseg-1481-98).
- **F205 — battery-PROMOTE (finding grade): seg-77-62-singleton** —
  the @507-only 77-62 stream singleton resolved
  (battery-seg-77-62-singleton).
- **F206 — battery-PROMOTE (locus-level composition): "ceci" = 87+61
  @644**, compositional, parallel to promoted "cela" = 87+11
  (battery-seg-ceci-87-61).
- **F207 — battery-PROMOTE: slot-1232-fence** (battery-slot-1232-fence).
- **F208 — battery-PROMOTE (finding grade, battery-grade): the 60
  verb split holds** — bare-60 verb (V1–V4) vs ent-60 verb (V5–V6)
  are two items sharing the syllable 60 (battery-split-60-verbs);
  needs red-team ratification before it counts as a split.
- **F209 — battery-PROMOTE (finding grade, evidence package):
  stem-03-nounfamily** — stem-vs-noun split evidence package,
  battery-grade (battery-stem-03-nounfamily).
- **F210 — battery-PROMOTE: 56 is whole-word** — 56's A10
  stem/whole status adjudicated: uniform whole-only (bare-56)
  carries 1 orphan in 23 (battery-stem-56-whole).
- **F211 — battery-PROMOTE (battery-grade): stem48-65-governor** —
  needs red-team ratification (battery-stem48-65-governor).
- **F212 — battery-PROMOTE (fencing finding, promotes no value):
  stem48-scope-fence** (battery-stem48-scope-fence).
- **F213 — battery-PROMOTE: subj-62-06-1537** — adopts the
  conditional determiner leg of val-41-det-windows (F217)
  (battery-subj-62-06-1537).
- **F214 — battery-PROMOTE (finding grade): subject-1186-est42**
  (battery-subject-1186-est42).
- **F215 — battery-PROMOTE (methods note, battery grade):
  suc-60-68-standalone** (battery-suc-60-68-standalone).
- **F216 — battery-PROMOTE (function-scoped, conditional): 94 at
  @508 (0b@509) is word-final "ne"** — the unique surviving parse
  anchors it as 62's word-final syllable
  (battery-syll-94-508-verify).
- **F217 — battery-PROMOTE: val-41-det-windows** — conditional
  determiner leg for 41 (adopts class-41-contact's NULL)
  (battery-val-41-det-windows).
- **F218 — battery-PROMOTE (finding grade, locus-level): val-91-
  pp-adj** (battery-val-91-pp-adj).
- **F219 — battery-PROMOTE (finding grade): venir-a-1841-corpus**
  (battery-venir-a-1841-corpus).
- **F220 — battery-PROMOTE (class-level): 55 = verb class,
  battery-grade** — value open ('pren'-shaped stem implied by
  "prend"); @1670 fenced with stated cause
  (battery-ver78-1670-5581).
- **F221 — battery-PROMOTE (finding grade, class level):
  verb-63-frames** (battery-verb-63-frames).
- **F222 — battery-PROMOTE (class level): verb19-lexeme-test**
  (battery-verb19-lexeme-test).
- **F223 — battery-PROMOTE: verbless-ne-family**
  (battery-verbless-ne-family).
- **F224 — battery-PROMOTE: w5-enter-junction**
  (battery-w5-enter-junction).
- **F225 — battery-PROMOTE (narrowed, battery-level, unratified):
  37-01 is word-internal** — one word, a "faire"-compound 3sg
  finite verb (37 = compound stem, 01 = "fait")
  (battery-wordinternal-37-01). This is the live reading that
  replaces the killed "certain" (N159).

Methodology notes (wave-5, first-class per REPORTING.md): every
worker re-derived counts on the repaired 1,847-pair stream in-session
and byte-verified its windows; `canonical.py` never touched; R5005
and sealed gates untouched; bars were pre-registered with numbered
clauses, frozen before data examination, never modified after;
value status marked on every use
(pencil/granted/promoted/provisional/battery-promoted-unratified);
kill grade means a window forces the claim false — not just "no
evidence"; conditioned splits need red-team approval (§7
sole-polyvalence law) — batteries package, never grant; residuals
fenced with stated cause and a named venue, never ignored; epistemic
failures fenced with stated cause instead of forced. This wave is
fence-heavy by design: nulls escalate rather than force — to the red
team (24-en-verb-conflict, ce01-slot-1029), the poly-80-docket
(x29-80-collocation), or named follow-up targets recorded in §6.
Enlightenment moments: byte-verification caught a briefing error —
ce01-slot-1029's brief said @1028–1038 but listed all 13 groups; the
true span is @1028–1040, and the note's erratum says so (briefing
errors are evidence, not noise); rival-37-01-certain exposed a stale
premise in the lane's own notes — 'tain' was believed local to the
three 37-01 windows, but the kill shows it dead everywhere, with
wordinternal-37-01 (F225) supplying the live reading 01="fait";
contre-00-global-census killed a global value with four byte-exact
"contre que" windows yet deliberately refused to promote the "96 00"
positional replacement — §7's sole-polyvalence law held under
pressure (the fenced positional lead was packaged for the red
team instead); 14's program shows how a wave narrows by fencing —
verb class fenced lane-wide (stem-14-84-retest), 14=verb killed
(N163), while the determiner arm promotes at one locus @117 (F182)
and the 'en' arm survives at battery grade (F185), none of them
contradicting each other.


### Round-17 wave-14 addenda (2026-10-09 UTC, crowd17 — 139 battery notes;
red-team ratification pending)

139 notes trace: `code/crowd17/report_inbox/` (all new since the wave-13
sweep): 94 cipher-side next-token batteries (28 promotes, 30 kills,
35 nulls, 1 mixed-partition) + 45 corpus-linguistics census notes
(9 promotes, 2 kills, 34 nulls — the dislocated-demonstrative /
governed-exclamatory / reinforced-pour-inf register program).
Verdicts entered in `code/crowd17/next-token/battery-queue.json`
(955 targets: 628 verdict, 327 queued at read time — +407 targets /
+265 verdicts / +142 queued since the wave-13 read of 548/363/185).
Supervisor 2026-10-09 ingestion audit
(`code/crowd17/next-token/ingest-2026-10-09.json`): 214 reports read,
0 new ingested, 276 follow-ups proposed (209 mandatory / 67
non-mandatory), 50 queued, 50 gaps, 140 flags — the follow-up sections
are queued per the standing supervisor directive. No note contradicts a
standing red-team verdict; two conditional risks flagged below.

- **F226 — battery-PROMOTE: the nine-window envelope of 24 closed**
  (battery-24-nine-left-envelope). The envelope is fully censused, named,
  and fenced with zero standing-verdict conflicts — census/record grade.
- **F227 — battery-PROMOTE: 98's distributional function at @838/@839
  named** (battery-boundary-98-839). Clause-terminal function at @838
  hardens the @839 clause boundary and a particle fork; @1137–1146
  doubled-98 cluster stays fenced.
- **F228 — battery-PROMOTE (finding grade): 69="ce" global support at
  battery level** (battery-ce69-global). The actual global promotion is
  red-team venue, not a battery act.
- **F229 — battery-PROMOTE: "53 34" @403–404 is one word "[53]i", no
  word boundary** (battery-ce88-53-wordbound). 88's complement stays
  53-headed; 53's value open (the "don" lead would read "doni").
- **F230 — battery-PROMOTE: the "ce [88-noun]" determiner frame FALLS
  at @402** (battery-ce88-leftedge-402). 45 at @401 is a
  non-determiner — the "ce" demonstrative pronoun — killing the
  determiner reading of 45 there. Residual @400 "la" unparsed under
  standing values.
- **F231 — battery-PROMOTE: 53 as 88's complement/object at @402–403
  with zero standing-value contradiction** (battery-ce88-pronoun-frame),
  cross-checked at @86/@646/@1541. 88's class stays battery-grade.
- **F232 — battery-PROMOTE: 37's class at @185 is the predicative
  adjective** (battery-class-37-06-185; A1's "est 37" frame stands).
  "37ent" @183–184 is one adjective word with promoted 06="ent" as its
  final "-ent" — not 37's finite verb ending. MATERIAL GLOSS
  CORRECTION (recorded, not hidden): the claim was queued before
  06="ent" promoted, when it glossed 06 as word-initial; under the
  promote, 06 at @184 is word-FINAL and word-initial "ent" is
  positionally impossible before promoted standalone "pour". Class
  decision unaffected.
- **F233 — battery-PROMOTE (finding grade): 14="en" clitic at @622–626
  banked** (battery-core-14-622-bank). The core parses as
  "[76-noun] m'en est [37-pred]" with zero new assumptions,
  independently corroborated by the "79 14" ×2 "tout en [60]" frames.
- **F234 — battery-PROMOTE: 14="en" tightened by value-independence
  legs** (battery-en14-value-tighten). Legs rest on battery-level /
  provisional neighbors (94="ne" lead, 98="vient" battery, 62="il"
  battery, 30="pas" promoted, 59="est" provisional) — corroboration,
  not grant. @587's "en pour" strain is a residual watch-item.
- **F235 — battery-PROMOTE (ruling-ready input package): the 77="le"
  package merged with F104** (battery-f104-77-merge-input). All bar
  clauses pass with zero adverses; evidence for the red-team 77 docket
  — not a ruling.
- **F236 — battery-PROMOTE: 86 as feminine noun at @671** (class-level
  only, value unnamed; battery-fem-noun-86-frames). Two distinct frames
  (F1 determinative licensing, F2 subject licensing).
- **F237 — battery-PROMOTE (ruling-ready input package): fem-32e @1211
  packaged for the red-team docket** (battery-fem32e-1211-redteam-input).
  Constraints: 32's adjective arm unresolved (adj-32 NULL), @855
  unresolved.
- **F238 — battery-PROMOTE (finding grade): fem-32e is not
  gender-conditioned at battery grade** (battery-fem32e-subject-gender).
  No forced masculine subject exists at any of the three copula frames;
  subject identity itself undecided.
- **F239 — battery-PROMOTE: 67="et" (not "veut") at both 67–76 windows
  (@1045/@199)** (battery-frame-76-67). The "veut" condition is not met
  under the standing positional rule; 76 fails every
  lane-operationalized infinitive test. 76's class fork stays open, no
  value assigned.
- **F240 — battery-PROMOTE: 94's right-context census discriminates its
  function** (battery-ne-94-right-context). Verbal-negator is the
  majority function (7 clean + 8 conditional windows); minority windows'
  functions unverified.
- **F241 — battery-PROMOTE: the (c2) loophole closed, hardening
  inf-20-nepas's verbal-slot forcing at @1703 to unconditional**
  (battery-nepas-20-adverb-gate). 20's value unnamed; 88's verb class
  stays battery-grade but is not needed by the kill.
- **F242 — battery-PROMOTE (structured evidence package): the 53
  "don"-vs-"doni" irreconcilability packaged for the red-team §7
  docket** (battery-poly-53-redteam-package). The conditioned-split vs
  re-parse question is venue-only; no adjudication here.
- **F243 — battery-PROMOTE: 88 = VERB at battery grade** (battery-prof-88).
  Seven independent frame-legs, zero hard contradictions across all 23
  windows; consistent with governor-88-value, finiteness-88-86,
  88-prep-rival, ce88-pronoun-frame, and the noun-88-subject kill
  (N-below). No value named (verb88-26-stem's stem kill stands);
  @1706 fused-3pl locus stays red-team venue.
- **F244 — battery-PROMOTE (scoped): word-final-"ne" segmentation for
  the 6 D3-un-attachable 62–94 windows** (battery-seg-62-94-wordless6).
  Adopts (not duplicates) the seg-62-94-wordfinal KILL below — the x9
  claim is dead at @1772; this promotes the scoped residue, superseding
  its own "donne"-verb weak pass at @1363/@1687. 62's value: syntactic
  class only.
- **F245 — battery-PROMOTE: the imp-80-set skeleton revised to "Ceci,
  [03]er! [80]-le, la première fois!"** (battery-skeleton-1032-revise).
  @1028–1040 re-parsed with zero reliance on the killed bare-"ce"-topic;
  87's role open (87="ce" stands; role fenced).
- **F246 — battery-PROMOTE (slot verdict): 60 at @196–197 parses
  verb-class** (battery-slot-60-at-197; queue result=promote). Value
  unnamed — consistent with verb-60's value-open null. Single
  assumption (01 = determiner/adjective) is a hapax with no
  distributional support.
- **F247 — battery-PROMOTE: 44 is the object clitic "l'" at @1712–1714**
  (battery-val-44-1712-pronoun). The gate parses with zero ungranted
  assumptions and the pronominal branch fires on "65 ne l'est pas";
  the frame is anaphoric, so @1712 contributes NO constraint on 65's
  value. CONDITIONAL TENSION (the note itself flags it): conditional on
  94="ne" (battery-promoted) and 59="est" (provisional); if the red
  team ratifies escalate-1714-ne44 (queued), this promote AND the
  standing noun-44 kill must both be revisited — the two cannot both
  survive ratification.
- **F248 — battery-PROMOTE (finding grade): the predicted string
  "le ver ne ment(ent)" materializes byte-exactly at @1181 and @1352**
  (battery-ver78-flagship-1181-1352) — the two and only two loci —
  under settled battery-promoted values.
- **F249 — battery-PROMOTE (of the confirmation claim): 98="vient"
  SURVIVES stem-14-84-retest's lane-wide 14-verb fence**
  (battery-vient-98-894-reaudit). All clauses hold without the @894
  conditional parse; the fence adds no new contradiction. 98="vient"
  itself stays battery-promoted — ratification is red-team venue.
- **F250 — battery-PROMOTE (locus-level word name): the @508 62–94 word
  named "trône"** (battery-w508-noun-ne). Resolves R17-022's fenced
  residual: "et le trône qui vient". Naming rests on 2 "et le trône"
  frame attestations + genre fit; "le trône qui vient" is semantically
  strained; 14 at @896 stays a residual on the "en"-clitic arm.
- **F251 — battery-PROMOTE (same-X demonstrated): both 33–29–87 crux
  windows' stems take the identical complement class** (87="ce" as
  direct object; battery-x-33-626-identity). Five-window stem census:
  one valency class, 0% orphan. X's value open (class-level:
  transitive "ce"-DO stems); left-context classes differ (predicative
  37 vs volitional "veut" 67).
- **F252 — battery-PROMOTE (audit battery): the adv-62 count corrected
  and the prior fence stands** (battery-audit-adv62-count). Numerical
  correction of a prior battery null — not inferential; the fence is
  untouched.
- **F253 — battery-PROMOTE (of the fence): the 48–32 @855 residual is
  not killed — 48 is word-final/stem-bound at kill grade, and the
  verb-32 conditional leg "51 qui [32-V]e" parses with zero new
  assumptions beyond battery-promoted 32-verb-class**
  (battery-qui32e-855-reseg). No value named; 32's adjective/verb arms
  stay unresolved at battery level; the "on 02 24…" right edge fenced.

### Corpus-linguistics census program (2026-10-09 UTC, disloc-demonstrative /
governed-exclamatory / reinforced-pour-inf register study — 45 notes:
9 promotes, 2 kills, 34 nulls; no standing verdict contradicted)

*Why this program exists:* several cipher-side value batteries hinge on
whether candidate plaintext constructions are grammatical in 1841
French — e.g. a dislocated demonstrative licensing an exclamatory
infinitive ("celui-là, pour rire !" shape) or "pour + infinitive" in
exclamatory fragments. The lane held 27.66M chars of French with zero
drama texts (Hugo/Dumas/Scribe/vaudeville absent) — a corpus gap the
battery itself flagged (battery-disloc-demonstrative-drama: bar
untestable, fence-executed null per BATTERY-PROTOCOL.md §2 — §7
forbids inventing "zero attestations"). The program commissioned a new
register-matched corpus and censused the construction family across
registers instead of asserting it.

**Corpus commission.** `code/side-period/corpus/PROVENANCE.md` (rewritten
2026-10-09 09:02 UTC) now documents four drama families: **Family 9**
(archive.org, 4 files): `hugo-hernani-1870.txt`,
`dumas-mariage-louis-xv-1841.txt` (1841 edition — contemporary with the
R5005 letter), `vigny-chatterton-1835.txt`,
`musset-comedies-proverbes-1850.txt` — 1,598,104 bytes / 1,569,886
chars, Internet Archive OCR of named scans, sha256 per file, `curl -sSL`
required (plain curl returns zero bytes on the dn*.archive.org
redirect). **Wikisource drama** (11 files): Hugo ×3 (Hernani, Ruy Blas,
Burgraves), Dumas ×4 (Antony, Tour de Nesle, Henri III, Kean), Scribe ×2
(Bertrand et Raton, Verre d'eau), Labiche ×2 (Chapeau de paille,
Martin-la-poudre-aux-yeux) — 1,658,808 bytes / 1,573,255 chars via
fr.wikisource MediaWiki parse API, raw API JSON archived off-lane;
UA `cipher-hunt-lane/1.0 (research corpus ingest)`. **Comedy extension**
(6 files, 465,525 chars): Scribe ×2 (Le Savant, Le Lorgnon),
Labiche ×4 (Voyage de Perrichon, La Cagnotte, 29 degrés d'ombre,
Affaire rue Lourcine) — `comedy_extension_ingest.py/.json`. **Comedy
wider corpus** (8 files, 565,307 chars): Scribe's Charlatanisme +
Labiche ×7 — `code/crowd17/next-token/widercomedy_ingest.py` with
`widercomedy-ingest-raw/manifest.json` (8 entries, all "ok", sha256 per
file). On-disk: 29 new .txt files — Hugo ×4, Dumas ×5, Labiche ×13,
Musset ×1, Scribe ×5, Vigny ×1 = 28 distinct plays (Hernani in two
editions), 661,743 words (count computed at sweep time, not a
PROVENANCE.md figure). **Caveats (PROVENANCE.md states these):**
Hernani appears twice (1889 Hetzel + 1870 Jenkins) — census runs must
use ONE edition per play to avoid double-counting (the edition-delta
battery below validates this rule as non-load-bearing);
`scribe-verre-d-eau.txt` is a SUBSTITUTION (the 1841 edition subpage
does not exist on fr.wikisource — 1861 edition used); editions are
mostly post-1841 reprints (Calmann-Lévy 1898, Hetzel 1889) — textual
variance vs 1841 performance texts unexamined; all works public domain.

**The headline finding (KILL-grade): pronoun-only licensing.**
`disloc-topic-inventory-excl-inf_census.json`: 27.66M chars → 341,564
topic-comma hits → 3,310 exclamatory candidates; pronoun class 53
reviewed, demonstrative 10 reviewed, 100 noun-topic hits reviewed → 2
genuine only: "Moi, voler !" and "Lui, ...s'opposer... !". The
demonstrative gap is a genuine topic-licensing restriction, not sampling
noise — only personal tonic pronouns license the bare exclamatory
infinitive. Watch item (the note's own): if drama yields noun-headed
bare exclamatory infinitives, the pronoun-only claim is
register-specific. Enlightenment: the kill converts every sibling
null's "zero is an absence" into a positive distributional finding.

**Drama confirms the pronoun class (battery-PROMOTE).**
`disloc-tonic-personal-census.json` (2,969,582 drama chars): 1,986
pronoun-comma hits → 427 exclamatory → 153 infinitive-shaped →
21 genuine (moi 14, toi 2, elle 3, vous 1, lui 1) across 8 of 14 plays.
"Moi, voler !" generalizes — the positive class is pronoun-headed,
which explains why every demonstrative-headed census zeroes out. No
adverses were pre-registered; promotion is battery-grade pending
red-team adjudication.

**The governed variant lives in elliptical dramatic dialogue, never
under a dislocated topic (battery-PROMOTE).**
`gov-excl-inf-register-drama_census.json`: 839 candidates (524 tight /
315 wide) → 1 genuine: Scribe's *Bertrand et Raton*, "Pour conspirer
!" — a dialogue-anaphoric fragment completing the Queen's previous turn
("vous me refusez [pour conspirer]!"), not a conventionalized
standalone. Thin by the note's own caveat (n=1, dialogue-anaphoric).
Pair with the comedy sibling
(`disloc-comedy-governed-inf_census.json`, 465,531 chars, 217 candidates
→ 1 genuine: Labiche's *Voyage de Perrichon* "Pas pour être témoin !…"
— Majorin's negated purpose exclamation, zero topic, no finite matrix):
the governed shape lives in elliptical zero-topic turns, same texture as
drama. Print-prose absence (0 in 27.66M chars) is absence of habitat,
not of grammar — the `gov-excl-inf-register` null's explanation reframed
as print-register specific.

**Head-local fencing, validated by recall.** The whole
tonic-demonstrative + bare-infinitive family is fenced in drama
(`disloc-demonstrative-drama-reinforced_census.json`: 2,969,582 chars,
41 reinforced-head-comma hits, 0 genuine — head reinforcement buys
nothing) and in prose (`disloc-demonstrative-reinforced_census.json`:
27.66M chars, 231 hits, 0 genuine). The fence is not a separator
artifact: drama covers comma AND non-comma separators
(`disloc-demonstrative-drama-pausemark-recall_census.json`: 307
separator hits → 120 hand-classified → 0 genuine); prose covers all
seven pause-mark classes plus 929 zero-pause windows
(`disloc-reinforced-pausemark-prose-recall_census.json` and
`reinforced-pour-inf-zeropause_census.json` — the latter's script had a
`\s*` backtracking bug caught in review; all reported numbers come from
the fixed manual-skip version). The fence is not a word-order artifact:
postposed "[inf] !, cela/ceci/ça" zeroes at full-corpus level
(`disloc-demonstrative-inversion-fullcorpus_census.json`:
12,197,541 chars of *Revue des Deux Mondes* 1841 q1–q4, 57 candidates,
0 genuine) and in quoted dialogue with spaCy POS reconciliation
(`disloc-demonstrative-inversion-verbtags_census.json`,
fr_core_news_sm-3.8.0, rule-based and statistical instruments agree on
the same 37-candidate universe). The fence is not an edition artifact:
`disloc-demonstrative-drama-edition-delta_census.json` — excluded vs
main Hernani editions → 0 genuine in both — validates the
one-edition-per-play rule as non-load-bearing (battery-PROMOTE, method).
The 2,733 classified candidates under the gov-excl-inf zero
(859 parent + 1,874 recall) is the largest classified base in the
family.

**Corpus-side KILLs (2).** (a) **Sampling-noise KILL** — the
topic-inventory census above kills the "demonstrative gap = sampling
noise" hypothesis at KILL grade. (b) **59-hardening KILL**
(battery-est-59-frame-census): byte-exact follower census — 20/27 =
74.1% of 59's windows parse as copular, with 4 kill-grade residuals and
3 fenced windows — the 80% harden antecedent fails, so the harden claim
dies at battery grade while 59="est" survives as provisional standing
(the known genuine residual "59 34 17" @554 counted inside the 20).
Re-open conditions named: any kill-grade residual re-parsing.

**Remaining corpus-side PROMOTEs.** (a) **No bare-"ce" dislocation,
register-wide** (battery-dislocation-ce-sweep; `/tmp/ce_census.py`,
dump `/tmp/ce_census_full.json` — lane-external scratch, noted as
such): 27.7M chars (1841 corpus + Tocqueville 1835/1840 + Hugo 1862) →
23 Tier-A + 2 Tier-B bare-"ce," hits, all classified, zero topics; the
fronted-demonstrative topic slot is owned by tonic forms (cela ×320,
ceci ×45, ça ×17). The ce87-topic-licensing KILL stands, confirmed at
register level. (b) **The 20-window census** (battery-census-20-open-windows,
PROMOTE method): 9 unexamined windows of 20 on the repaired 1,847-pair
stream (`data/upstream-ct_R5005.txt` +
`code/side-keyhunt/repaired_offsets.json`): verbal ×2 (@703 licensed
infinitive "vient [20-INF]"; @873 finite via "le [89]e [20] 74" S-V-X),
unforced ×7. Enlightenment: @668 is a clean noun/infinitive tie under
"pour [20]" — the lane's cleanest future discriminator for 20's value.
(c) **syl79 word-name** (battery-syl79-wordname, PROMOTE): 4 S-windows —
@451 and @1460 named "toutefois" (79+17); "toutefois" occurs 318× in the
1841 corpus (22× in RDM 1841-q1), a common diplomatic-prose adverb, not
an invention; @53 and @1419 fenced (85/58 and 15 open). No polyvalence
declared (§7: inflectional allomorphy of the banked lemma). The 79-split
declaration stays red-team venue; rows a2_10/a7_09/a1_01/a7_08 carry
unvalidated upstream offsets (canonicality caveat).

**Lane infrastructure from this wave.** `repaired_offsets.json`
rewritten 2026-10-09 09:12 UTC — content-neutral: re-verified 70
offsets, 39×0 / 31×1, byte-matching the offset-validation section
(a4_01/a5_07 still 1 and flagged-but-unflipped per red-team rule;
a5_03=0; a2_01=1, a6_04=1, a8_09=0); no byte-diff possible (no lane git
history), verification rests on the exact match. `table-registry.json`
unchanged since 2026-10-09 03:03 UTC and the table-grid was regenerated
at the same time — `generate.py` NOT re-run. `decode-current.txt` /
`decode-sidebyside.txt` (R5005 render) already documented at the DECODE
R5005 render section — no new decode. `comedy_extension_ingest.json` /
`.py` document the 6-file comedy ingest (file/desc/wikisource-URL/
chars/sha256/raw-API-JSON path).

---


### Round-17 backlog fold (2026-10-09 UTC — 26 pre-wave-13 notes whose
verdicts were never folded: 8 promotes, 8 kills, 10 nulls; battery
grade, red-team ratification pending)

These 26 notes sat in `code/crowd17/report_inbox/` from earlier waves
and were never folded nor moved. This sweep folds their verdicts now
(trace: each note name below) and moves them to `processed/` alongside
the wave-14 batch.

- **F254 — battery-PROMOTE: 26's class at @1754 is verb-class**
  (battery-26-class-1754). Resolves the window's 3-way ambiguity to one
  surviving parse — the gerund "[26] en [85] [58]" ("[89-S?]
  [26-V] en [85-gérondif] [58]"); the modal and pronoun+finite parses
  both need 26 nominal and die. @1756's 58 sits in the complement slot
  of the resolved gerund frame. Caveat: load-bearing on a positional
  rule awaiting red-team §7 declaration; 58's complement role is
  consistent-but-unadjudicated (a concurrent battery's domain).
- **F255 — battery-PROMOTE: 58 = nominal, noun-class**
  (battery-58-complement-1695). All bar clauses pass at @1695 and
  sibling windows (@1202/@122/@157/@1754/@1756); @55 fenced on the
  banked "la tout" contradiction; all adverses answered. Exact noun
  value unnamed (beyond battery grade); zero determiner predecessors is
  distributional, not forced.
- **F256 — battery-PROMOTE: the "elision x4" lead is really x1**
  (battery-elision82-48-x1). At @1229, "82 48" is necessarily "m'"
  before the vowel-initial infinitive [48]er; the other three 82-48
  windows (@126/@377/@398/@1589 checked) are not elision legs. All
  three bar clauses pass, adverse answered.
- **F257 — battery-PROMOTE (finding grade): "[69] 26 pour dire" decides
  26 = VERB** (battery-noun26-69-pour-dire). 2 independent attestations,
  3 trigram tokens: 26 = VERB via 69's nominal (subject) class — the
  noun arm for 26 is dead in this frame. And 69 = noun (10–11/12
  windows) with @1115 ("pas [69-modal-inf] la [88-inf]") as a live
  verbal leg → §7 split candidate for the red team. Caveat: 33's
  word-vs-stem split ("00 33" never +29, 0/8; "33 29" never after 00)
  packaged for red team — conditional only for the "pour dire" gloss,
  not for 26's class.
- **F258 — battery-PROMOTE (finding grade): the stem-valency
  divergence computation, byte-exact** (battery-stem-valency-gradient).
  Governors (33 vs 86) JS = 0.6286 bits, exact permutation p = 0.2698;
  complements (33 vs 86) JS = 0.3958 bits, p = 0.5714; ce-complement
  Fisher p = 0.4444; veut/pour governor Fisher p = 0.4000. Headline:
  the gradient does not reach significance at the lane's standard —
  underpowered at n=5/4 (power gap); the strict bar's @1392 failure is
  not rescued. Live arms stay with the queued ce-complement-86-negative
  and veut-86-1392-adjudicate targets.
- **F259 — battery-PROMOTE (finding grade): the subject of "que
  [56]ent" @1744–1747 is 65 in postverbal position**
  (battery-subj-1744-que). "que [56]ent [65]" parses as a
  que-subordinate clause with 3pl verb and postverbal plural subject
  under the single stated assumption that 65 is plural. The subject
  gap is closed; the @1742–1744 red-team fence keeps only left-edge
  debris. Caveat: the "65 is plural" assumption is stated, not proven;
  red-team ratification required before any registry change.
- **F260 — battery-PROMOTE (census finding): the 38-window 48-boundary
  census is byte-exact — 29/38 admit stem-internal 48 (76.3%)**
  (battery-w48-boundary-census). Below the 80% bar, so the A7-L2
  stem-frame does NOT generalize to 48 and is scoped to its exclusive
  legs @1229/@1589 (narrow-vs-retire ratification: red team). Residuals:
  @1525 ("la e par" — stranded word-initial "e"); @365/@1398 (78-48,
  indeterminate — 78's value ungranted); @542 (sole 29-48, residual per
  fem-e-48).
- **F261 — battery-PROMOTE: the 06-forces-84 gate resolves cleanly**
  (battery-06-forces-84). 06 = "ent" (promoted, single value); under it
  @1188's "06-84" parses as "ent"+"on" with a word boundary, so the
  feared "en on est" contradiction never fires and unconditioned
  84="on" at @1189 survives the 06-class gate. The NULL/escalation
  branch (06="en") is closed. Control @1289 confirms the
  clause-initial-"on" mechanism. Caveat: the -este verb-unit rival (84
  as middle syllable of 06-84-59) remains live at the red-team venue
  per este-verb-id's pre-registered not-a-kill — fenced here, not
  adjudicated. (REPORT.md's prior sole mention, F109's "@1188 fenced to
  06-forces-84", was a fence routing, not a fold of this verdict —
  this fold completes it.)

### Round-17 wave-14 mid-sweep arrivals (2026-10-09 UTC — 8 battery notes
landed during this sweep: 4 cipher-side, 4 corpus-side; battery grade)

Two carry substantive register consequences. **(1) The @508 "trone"
locus promote (F250) is under red-team escalation**
(battery-regne-trone-tiebreak). The one frame where "regne" and
"trone" make different predictions ("le [62]ne qui vient") favors
"regne": "regne" as subject of "venir" is selectionally licensed
("l'annee qui vient"-class) and attested once, while "trone" as
subject of lexical "venir" has 0 attestations in 31,662,737 chars of
1841-register French (the sole "trone"+"venir" collocation is "venir
de" recent-past + passive participle, a different construction) and is
selectionally strained — exactly the strain F250 itself recorded.
Below battery-grade naming confidence (corpus n=1 vs n=0), so the tie
is NOT broken; per battery-protocol section 5 a battery cannot
downgrade a standing battery verdict — the package (frame +
selectional asymmetry + corpus census) is escalated to the red team:
downgrade the @508 "trone" promote and ratify "regne", or keep the tie
fenced pending 65's value at @508 (the keyhole follow-up: a landed 65
value creates the selectional pressure this battery lacks). **(2)
Avenue A (01 as infinitive governor at @1029) is RE-OPENED, not
killed** (battery-01-verbclass-probe). 28-window census of 01 for
finite-verb/modal shape: exactly 1 verb-shaped window (@1256/P1:
"[65-N] que [01-V-finite] [61-S]", subject-verb inversion in the
"que"-relative, "le livre que lit Marie"-shaped) fires C3, so the
@1028-1031 fence is NOT hardened. The P1/P2 section-7 tension (01
cannot be both verbal and nominal — 67 is the sole polyvalence) is
red-team venue; the TLFi "ce"+lexical-verb archaism constraint will
bite at @1029 if avenue A is pursued. The other two cipher-side nulls:
the @1585-1588 "36 70 64 65" 4-gram is a syntax orphan
(battery-stem48-qui-65-hapax — "pour [36-noun]" closes cleanly, so the
breakage localizes to the stranded word-initial "pre" (70) at the
70|64 boundary; every rival "qui"-role dies at kill grade; the fence
is phase-conditional on row a8_02's unvalidated upstream offset); the
fin-41-lexicon bar is untestable-as-written (no finite-verb candidates
for 41 on the lane record; the "qui [41]" frame is a singleton with a
hapax antecedent — an epistemic null, not a refutation). The four
corpus-side nulls (nulled in the section-5 batch below):
inverted-order zero confirmed in drama dialogue (490 candidates, 0
genuine); the head-inventory census (0 genuine demonstrative-headed
bare exclamatory infinitives in drama dialogue vs 5 genuine
tonic-pronoun heads — the arm-(a) fence holds exactly at the
demonstrative head); inverted-order zero in prose (146 candidates in
27.66M chars, 0 genuine — both word orders, all three registers); the
dialogue-scoped pausemark zero (128 candidates in 2,539,841 scoped
chars, 0 genuine — arm (a) now fenced at seven levels).

---

### Round-17 late-inbox arrivals (2026-10-09 UTC — 80 battery notes +
1 wave-3 finder; battery grade)

**The neque finder loop closed end to end.** Wave-3 finder
`next-token-findings-neque-instance-sweep` (spawned from the
neque-bracket-verb-search NULL) classified all six 94…46 windows: the
@1687 empty-slot anomaly is NOT a singleton — @1363 is its structural
twin (byte-identical `94 79 14 60` occurs exactly 2× stream-wide, both
times directly after `13 {92|93} 62`; the `79 14 60` string occurs
exactly 2× as well). The follow-up battery `neque-79-twin-frame`
returned NULL: the distributional twin is real, but the frame is not
grammatically licensed at either locus (the "ne"-bracket's verb slot
is empty at both; the long @1363 interior's licensed verbs head other
clauses). This CONFIRMS the npframe-60-detleft-closeout fence of the
instance-B "ne…que" frame as a residual — it does not overturn it.
14 and 60 stay open. **Kill in the same family**:
`neque-82-frame-family` — the "94 82" 4× is NOT one licensed "ne m…"
frame (@1742's banked "que" breaks elision). **Boundary promote**:
`x-61-94-boundary` — 61 | 94 is a forced two-word boundary; 94
("ne", battery-promoted) stands independent, not bound to 61.

**The word-initial arm's licensed inventory is complete**
(`29-initial-word-census`, PROMOTE): census of all 45 29-occurrences
on the repaired stream — 9 word-initial windows, 6 shapes, **0 named
French words**. W3 has a twin: W-C @147 ("on er ce qui") — a second
bare-"er" word-initial window, unparseable at battery level for the
same cause as W3. The only live naming prospects are gated on one
open group each: [29 42] ×2 (@78/@218), [29 85] @96, [29 60] @689.
The "…èrent" 3pl past-historic shape ([29 40 65] @291/@685, the
W1/W2 trigram) is a licensed shape with an unnameable word.

**Kill: 21's battery-grade value search is dead**
(`croire-33-noun21`): @134 kills all noun values, @109/@359 kill all
masculine values. This resolves the reopen condition on the
`dire-33-asymmetry-no21` fence (it was "21-load-bearing") — that
fence is now a revisit candidate for the supervisor.

More verdicts of note. `tense-24-311-formclass` PROMOTE: 24 is
finite-verb at @311 and @474 (twin windows); the 24="en" residual arm
is dead. `det-80-1156-1011` PROMOTE (reading-level): 80's
determiner/quantifier reading is licensed ("[80-quant] fois" @1156,
"tout autre [78]" @1011) — input to the poly-80 docket.
`laframe-1719-demonstrative` PROMOTE: the rival parse "ce [68ent] la"
is a clean demonstrative+noun frame — 06="ent" confirmed
noun-finally. `seg-528294-word` PROMOTE (word-unit only): "52 82 94"
= "amnestie"/"amnestier" with one new assumption (52="a").
`seg-62-48-word` KILL: the one-word "62e" reading is false — 62="il"
is a free word at all 35 windows; the six "62 48" instances are two
words. `x-33-37-licensing` PROMOTE (parse-level): 37 does not license
bare infinitive — "[33]er ce [78-N]" is self-licensed.
`premier-61-flank-census` NULL: "premier" is NOT 61's conditioned
value — exactly one proven admission (@1556, the val-61-premier
locus) and one flank-supported candidate (@645). The locus promote is
sharpened: @1556 is unique on the full 61 population; no global 61
value is claimed (val-61-contact's kill stands).

Bar quality: workers now formally reject untestable-as-written bars
(`inf-80-89-ratify` is the second such rejection — the asserted
precondition "MET" was disproved by the records themselves), and one
worker corrected a parent brief's Littré premise
(`xeent-register-tiebreak`: maugréer is v.n., not marked "fam.").

The 48 nulls of this batch are nulled as N267–N314 in section 5
below. The supervisor has queued their follow-ups (queue meta
followups_queued_p16–p22, 2026-10-09): the three finder-proposed
targets neque-79-twin-frame, neque-82-frame-family, neque-14-frame-value
are now all verdict-bearing.

### Round-17 wave-15 arrivals, post-sweep batch (2026-10-09 UTC —
26 battery notes landed after the ~11:20 UTC sweep: 11 promotes,
3 kills, 12 nulls; battery grade)

**58-det-numeral-tension is resolving.** Frame B of `58-value-name`
is confirmed collapsed: at @1696, under 15=adverb, rescue (a)
clause-boundary-after-58 fails (no nameable subject) and rescue (b)
verb+object+adverb fails under R24 — the surviving parse is the
inversion "que en [85-fin] [58-subj-noun] [15-adv]" with one
ungranted assumption (85 finite). 24@1693='en' per R24 ("24 85"
bigram exactly 5× stream-wide: @732/@955/@1438/@1693/@1754).
(**F217**, battery-1696-reparse-adverb PROMOTE; n(58)=7.) The numeral
case now rests solely on frame A @1756 "[58] fois". Frame C
("ce [58]" @1201-1202) stands — 45='dict' fails all 4 documented
mechanics, 45='ce' parses with zero hard contradictions — hardening
the 58-value-name NULL fence (**F218**, battery-58-a11-hold-test
PROMOTE; "45 58" hapax bigram; scope is frame-level only, 45='ce'
remains an ungranted A11 HOLD). At @1691–1695 the tail
"[27] que(46) [24] [85] [58]" yields the licensed clause
"que en [85-verb] [58-noun]" with zero new assumptions (46='que' is
pencil ground truth) (**F219**, battery-neque-tail-24-85-clause
PROMOTE; no value named for 85 or 27).

**The bare-"ne" locus at @1330 resolves at construction level.**
32,895,030 chars over 71 files of `code/side-period/corpus` yield
2,229 strict bare-"ne" candidates (a line-wrap artifact class —
6,096 raw — was caught and fixed in the census); the licensed class
is pouvoir/savoir/oser/cesser/falloir/vouloir/devoir (1,307/2,229),
and the exact "ne [finite] de [INF]" shape the locus needs is
attested ("ne cesse de rapprocher") — the finite-verb arm at @1334
stays unstrained (**F220**, battery-ne-1330-bare-corpus PROMOTE).
Sharpening: targeted search for "ne/n'" governing
prescrire/préserver/prévoir finds zero in 32.9M chars (the two
"ne prescrivent" hits carry partners) — the three cipher candidates'
verbs sit outside the licensed class; the strain is lexical, not
constructional (`ne-1330-lexical-trio` queued). The "ne mentent"
(3pl) rival at "94 82 06 06" is forced false at both windows
(@578/@1182): no 3pl subject licensed, preverbal slots positively
filled by singular determiners, and a 12-rescue audit at @1182 finds
no grammatical rescue — recorded as N327/N328 in section 5; 06="ent"
and 94="ne" are untouched. The cross-window comparison delivers a
red-team evidence package: both windows share ONE subject account —
the gap is systematic, a property of the x2 frame (**F221**,
battery-nementent-W2-subject PROMOTE; consistent with the closed
R19-167 94-split record, no new red-team act requested). The particle
"ne" control paradigm is delivered as a 6-window clean core
(@65/@161/@774/@1330/@1705/@1773, byte-exact; @651 contradicts the
parent census's own "no non-clitic intervener" definition)
(**F222**, battery-ne-attachable-paradigm PROMOTE).

**The governed exclamatory infinitive is drama-wide.** 7 new
non-comic plays (1,206,208 chars, 5,102 bangs; 371 candidates all
hand-classified) yield 4 genuine attestations (Hugo *Le Roi s'amuse*
×2, *Lucrèce Borgia* ×1, Dumas fils *La Dame aux camélias* ×1;
census `code/crowd17/next-token/gov-excl-inf-drama-comedy-skew_census.json`).
Cumulative drama state: 35 files, ~5.2M chars, 10 genuine —
6 comedy, 4 drame. The comedy-skew hypothesis is falsified at its
stated standard (≥1 genuine in a non-comedy play); dialogue-elliptical
fragment grade predicts the construction, not the genre label
(**F223**, battery-gov-excl-inf-drama-comedy-skew PROMOTE).
Caveat: tragédie proper still zero.

**08's letter-tier signature is positively stated.**
n(08)=18: 5 word-initial-letter (@631/@881/@1488/@1520/@1592),
4 internal junctions, 1 word-final (@198); letter-neighbor inventory
delivered (predecessor 40='e' ×2, successor 34='i' ×1, successor
29='er' ×1; 82='m' 0/36 contacts). The spelling-vs-clitic adverse is
answered as two positional flavors of the landed spelling-letter
reading, so promote rather than fence (**F224**,
battery-08-letter-geometry PROMOTE, signature-level; the
`stem-08` NULL stands untouched — no 08 value named). The "[08][31]"
word is complete in all 3 windows but unnameable at battery grade
(08's letter open; 31 is class-only `["VERBAL","cls"]` in the
registry) — recorded as N319 in section 5.

**89/97 word-class ties tighten.** At @639–642 ("le [89]e [20]"),
the adjective arm is agreement-admissible: once 89's value resolves
here it must be a masculine singular noun (89 census n=14;
77='le' provisional — the premise moves if 77 resolves otherwise)
(**F225**, battery-agr-89-642-adj PROMOTE). At @524–526, 81 is
NOMINAL (10/14 windows sit after determiner-position cells) —
adverbial-81 dead at this window, the infinitive-topic revival route
closed; NOM-97 hardened at @526 (window-level, no registry change;
the global INF/NOM tie survives via the four "pour [97]" windows)
(**F226**, battery-nom-97-526-adverb PROMOTE). The @65 word-final
fence hardens: 4,913,029 tokens over 32,547,082 bytes of
`code/side-period/corpus` yield 0 genuine "erenne"/"ierenne"/"enne"
word forms (14 raw, all adjudicated hyphenation/OCR artifacts)
(**F227**, battery-enne-65-lexicon-tighten PROMOTE; consistent with
the "enne-word-64" KILL).

The 12 nulls of this batch are nulled as N315–N326 in section 5
below; the 3 kills as N327–N329. No follow-ups are requested in
this sweep — all belong to the supervisor's battery queue.

### Round-17 wave-16 arrivals, post-sweep batch (2026-10-09 UTC —
10 battery notes landed after the 13:30 UTC sweep: 3 promotes,
1 kill, 6 nulls; battery grade)

**The @730 clause parses as a full French clause.** `pron730-clause-wide`
PROMOTE resolves both open items of the parent `objpron-88-77-11` C4: at
@729–735, `[48-S] [88-fin] la en [85-93-V] [76-voc]` is a grammatical
French clause ("On veut l'en informer, monsieur!"). The proof is by
exclusion: with "la en" proclitic to the composed [85-93] verb (standing
A3/"en [85]" frame, R24 declaring 24@732="en"), 88 cannot be infinitive
(no licensed structure before a clitic+verb complex) or imperative
(imperatives take enclitics, not proclitics) — only finite survives. And
85+93 cannot be two separate verbs within the ≤1-assumption budget (every
split geometry fails grammatically or costs 2+ assumptions), so 93 is the
inflectional ending of 85's stem ("85 93" is a stream hapax — expected
for a single composed word, not a recurring frame). Exactly one ungranted
assumption: 48=subject (48's class is open). The parent's conditional
"la en" survival is now unconditional within that budget. The @736–740
tail ("18 82 06 00 36") is fenced as open post-clausal adjunct material,
not kill-grade; the @728 (86) left edge belongs to the preceding "la
pour [86]" purpose clause. Scope is window-local: 48's value beyond
subjecthood, the tail's internal classes, 85's stem value, and 76's noun
stay open; this is not a global promotion of 88's finiteness.
(**F230**, battery-pron730-clause-wide PROMOTE.) The animated decode —
green = confirmed on the stream, amber = grammatical shape (wording
illustrative):

![Fig 7 — clause @729–735 animated decode](clause-730-decode.gif)

**Tragédie proper attests the governed exclamatory infinitive.**
`gov-excl-inf-tragedy-n2` runs the P1/P2 design VERBATIM on 3 new
Delavigne tragédies (322,004 chars, 987 bangs, 75 candidates, all
hand-classified; corpus + provenance under `code/side-period/corpus/`;
census `code/crowd17/next-token/gov-excl-inf-tragedy-n2_census.json`):
one genuine — *Une famille au temps de Luther* @70173, "Ou plutôt à
revoir !" — an à+infinitive fragment with no finite verb in the unit,
the same dialogue-elliptical fragment grade as all prior genuine cases.
The other 74 candidates are excluded with cause. C1 fires; C2's
antecedent is false: the tragédie-zero is dead on four data points
(Ponsard *Lucrèce* ×0, Delavigne *Vêpres siciliennes* ×0, *Le Paria* ×0,
*Une famille au temps de Luther* ×1). The Round-20 red team confirms the
full inventory at 13/13 genuine: comedy 8 / drame 4 / tragédie 1
(**F228**, battery-gov-excl-inf-tragedy-n2 PROMOTE; R20-057 GRANT).
Cumulative drama state per R20: 38 files, ~5.5M chars, 13 genuine.
Genre label does not predict the construction.

**The pour-governor question re-opens at drama level.**
`personal-tonic-pour-only-drama-recall` widens the sibling's net
(400-char windows, '!' or '?' termination) over the 14-play drama corpus
(2,969,582 chars; 75 candidates, 37 strict + 38 loose-only, all
hand-classified; census
`code/crowd17/next-token/personal-tonic-pour-only-drama-recall_census.json`):
one genuine — Dumas *Henri III* @86308, "Moi, monsieur, et pour écrire à
qui ?" — left-dislocated tonic topic + pour-governed self-contained
interrogative infinitive, no finite verb in the turn. C1 fires; the
pour-governor question is re-opened. Scope is narrow: the genuine is
interrogative, not the '!' exclamatory shape — the parent's fence against
the exclamatory variant stands unrefuted. Headlined disagreement: the
sibling recall battery held this same window and reported 0 genuine
overall; its per-candidate ground is unrecoverable from its report
(stricter exclamatory-only gate, or the cross-turn "et" read) — a
red-team item, not a rewrite of the sibling verdict. (**F229**,
battery-personal-tonic-pour-only-drama-recall PROMOTE.)

### Round-20 red-team adjudication addenda (2026-10-09 UTC — 136 rulings;
red-team ruling AUTHORITATIVE)

Adjudicator: red-team coordinator, sole conflict-resolver. Scope: 108
unruled battery promotes (every queue target with
status=verdict/result=promote not adjudicated in R15–R19) + 28 priority-1
RED-TEAM DECISION targets. All numbers below are the adjudicators' own
fresh re-derivations from the repaired stream (anchors: 1,847 pairs / 96
types). Trace:
`code/crowd17/report_inbox/next-token-redteam-r20.md`.

- **Tally: 136 rulings — GRANT 65, GRANT-WITH-CORRECTIONS 16,
  DUPLICATE/CONFIRM 31, REJECT 10, FENCE 13, CLOSED 1.** 108/108 promotes
  covered; 28/28 P1 decisions covered; 0 orphans. **Registry: 0 changes —
  50/96 cells stand.** §7 intact: 67 et/veut remains the sole true
  polyvalence; R24 the sole declared exception.
- **SOLE standing revision: R20-116.** The @889 clause-boundary fence is
  LIFTED with new byte evidence: "00 86 06" reads as ONE WORD,
  "pourvoient" (00='pour' A9-granted + 86='voi' + 06='ent' R17-007).
  86='voi' is grounded twice independently ("86 29" ×4 = "le voir"/
  "pour voir"/"veut voir"; @886–892 = "pourvoient le [76]").
  The queued val-86-728-entr ('entr' hypothesis) is untested and does not
  contradict the local 'voi' composition; 86's global value stays open.
- **Fresh promote→REJECT (4):** ne-1331-70-52-parse (arm A loads on the
  unstated 52 prendre-family role), ne-W6-pas-verb (the load-bearing
  particle reading of 94@1363 is ungranted), residual-1029-infinitive
  (the bar's A/B race never tested; reading R19-142-fenced), and
  adv-1135-leftward (premise "62='il'" killed by R19-106 — permanent).
- **Fresh promote→FENCE (1): formula-76-49-24** (coordinator override of
  FAM-G's grant). The N-ADJ-Vfin license is vacuous: the promote's scope
  tied the license to the adjective-49 leg, and adj-49-420-366 KILLED
  adjective-49 at kill grade. 49's surviving classes (adverb, noun —
  both strained per N333 above) instantiate no census-licensed geometry.
  The ×2 byte-identity ("76 49 24 26 30 03" @652/@989) is real and
  unexplained; the census (65/66 clean) stays a valid resource. Census
  backing: `code/crowd17/next-token/formula-76-49-24_census.json`.
- **Ratified kills:** modal-80 (17-window census; the @567 INF reading
  now KILLED, R20-121); "ne mentent" one-word rival at both windows
  (@578/@1182; R20-120, R20-105); the 94 functional-split question stays
  CLOSED. 62='il' stays KILLED at kill grade, permanent (R20-125).
- **Governed-exclamatory-infinitive family (FAM-E): all 11 corpus
  batteries GRANT.** Inventory confirmed 13/13 genuine (comedy 8 / drame
  4 / tragédie 1); no cherry-picking (shared exclusion taxonomy); the
  construction is licensed, no value named. This is the authority behind
  F228 above.
- **Ne-1330 closure (R20-030):** the 7-verb licensed class is closed at
  construction level (5,032 of 5,435 bare candidates; the 391 "other"
  dissolved; 13 doubtful, none trio-related); 0 genuine bare-"ne" +
  prescrire/préserver/prévoir in 207.1M chars. Backing:
  `ne1330_trio_1841.json` (28/0 in 34,525,238 chars), `ne1330_trio_modern.json`
  (406/0 in 172,572,549 chars), `ne1330_lexclass_modern.json`.
- **Poly-20 docket (R20-126):** particle-20-value-rivals NULL — no
  battery-grade left-context frame separates 'mais'/'or'/'donc'/
  'cependant' at @760/@839 (the exact ordinal-ellipsis frame favors
  'mais' 5-0-0-0 but is underpowered). 'mais' stays the routed
  candidate; the value is unnamed. Backing: `particle20_rivals_census.json`
  (diplomatic: 9 files; full French: 59 files),
  `particle20_shortprev_diplomatic.json` (or 150 / mais 2,372 /
  cependant 186 / donc 44 hits), `particle20_verbless2_diplomatic.json`
  and `particle20_verbless3_diplomatic.json` (350/240 examples),
  `ordinal_particle_boost.json` (mais 6, cependant 1).
- **Pas-bare census backing the 58 family:**
  `pasbare_candidates.json` (75 files, 34,525,238 chars, 32,095 'pas'
  tokens, 2,611 bare candidates) and `pasbare_adj.json` (269 classified
  windows) feed the gov-excl-inf register venue (R20-094: 13 genuine
  free-bare of 1,938 nominal complements — 0.7% vs 97.0% determined).
- **Carry-forward:** 78='ver' DEFER with cause (R16-005 LEAD stands; the
  @819 "ce verre" leg banked for the settle decision); 98='vient' KEEP
  AT LEAD, DO NOT GRANT; 93 value DEFER; 65 gender DEFER; "values for 88"
  OPEN (@1706 constrains 88 to compose a 3pl "-nent" verb with
  word-internal 26 — R20-114 locus parse; the uniform vient-family stem
  is KILLED). "la tout" exits FENCED; 62 split package FENCED (candidacy
  as framed dead on arrival; strain evidence banked).
- **Pipeline flags for the supervisor** (not acted on here): (1)
  det-87-644-function's queue entry still reads promote against the
  standing R19-138 FENCE; (2) a-39's queue verdict reads promote vs
  R17-005 LEAD — do not upgrade; (3) ne-94's queue verdict reads promote
  vs R17-001 REJECT (STRONG LEAD) — not ratified; (4) ne-1331-70-52's
  REJECT withdraws the @1331 resolution claim; (5) ne-W6-pas-verb's REJECT
  withdraws the W6 C1 re-open; (6) doubled report-path metadata
  (`code/crowd17/code/crowd17/...`) on several queue entries — harmless,
  worth a one-line repair; (7) byte-identical sibling pair
  seg-81-30-trepas-kill / seg-81-30-trépas-kill — consider merging.

The 6 nulls of the wave-16 batch are nulled as N330–N334 in section 5
below; the 1 kill as N335. No follow-ups are requested in this sweep —
all belong to the supervisor's battery queue.

---

### Round-17 backlog fold, second batch (2026-10-09 UTC — 53 battery notes
read: 39 pre-wave-13 processed notes (one already folded as N334, see
MANIFEST) + 14 fresh inbox arrivals; 16 battery-grade promotes, 7 kills,
27 nulls, 2 gather-only red-team inputs; NOTHING here is red-team ratified)

All F-numbers below are battery grade. Provisional tier inherited from
standing leads; no registry change is claimed by any battery.

**39 is nominal at @37.** `nominal-39-37` PROMOTE (locus-level): with
granted 64="qui" at @38, French grammar forces 39 nominal — any "qui"
needs a nominal antecedent, so no new assumption is needed and 91's class
need not be named for the parse. Compatible with R17-005 (39="/a/"
allophone LEAD, R20-010 confirmed); verb-39 is already dead (see N340
below). (**F262**, battery-nominal-39-37 PROMOTE; battery grade,
locus-level only — 39's class elsewhere stays open.)

**"59 30" is "[n']est pas" at both windows.** `pasX-leftverb-59` PROMOTE:
the "59 30" bigrams occur exactly ×2 stream-wide (@559, @1715;
byte-exact, repaired 1,847-pair stream); both parse as "ne est pas" with
the verb host left-adjacent, on 10+ independent "est" legs (n(59)=27).
Period check: "est pas" ×33 in one file of `code/side-period/corpus`
(77 files, ~35M chars); "pas qui ce" geometry 0 hits. The left neighbor
was the verb all along — the whole "verbless" premise was an artifact of
not looking left. W2's post-"pas" continuation is strained (corpus-unattested)
but not kill-grade (appositive reading survives) — a fenced residual for
the 43-family batteries. Provisional tier inherited: 59="est" provisional,
94="ne" STRONG LEAD (R17-001), 30="pas" conditional on those two (R20).
(**F263**, battery-pasX-leftverb-59 PROMOTE.)

**The premier-admitting 61 windows fence into a principled set.**
`premier-61-admit-fence` PROMOTE: the ordinal-slot condition (left-adjacent
determiner 87/37, or right-adjacent noun-class 42 / the "61 40 17"
feminine construction) admits exactly the four premier-admitting windows
(@279, @281, @645, @1556) and none of the other 14: 18/18 windows
discriminated, zero false positives, zero false negatives (n(61)=18,
re-derived repaired stream). @279/@281 are one sandwich locus counted
twice. Condition: @279's left-det leg rides on 37='le' (S5, fenced under
red-team venue, not granted) — if the red team kills 37='le', the set
shrinks to three windows; the condition itself still discriminates. No
global 61 value is named (val-61-contact's KILL of any global 61 value
stands unchallenged). (**F264**, battery-premier-61-admit-fence PROMOTE,
conditional on the S5 37='le' venue.)

**@1024 fences as a verbless fragment.** `quice-verb-1024` PROMOTE (of the
locus characterization — names no value): 3 stream-wide "45 64" ('ce
qui') bigrams (@314, @340, @1024); 4 finite-verb candidates tested and
failed (80 @1032, 03 @1030, 85 @1047, 88 @1049) on six stated causes;
every route crosses "87 01" and 01 has no battery-grade value
(val-01-census NULL). The bar's fence arm fired: @1024–1027 ('ce qui par
[43]') is a verbless fragment. Re-arm conditions stated (name 01's value,
resolve 03's class, name 43's value, overturn any of causes b–e). Adopted
without re-litigation: R19-142, R16, edge-1024-clause-boundary KILL,
Round-20 ne-W6-pas-verb REJECT. (**F265**, battery-quice-verb-1024
PROMOTE; battery grade, no value named, no registry change.)

**The quoted-drama null is OCR-noise-robust.** `quoted-dialogue-goldset`
PROMOTE (corpus deliverable): a hand-verified 248-genuine-span dialogue
goldset (340 reviewed, 73% yield) from `revue-deux-mondes-1841-q1..q4`
(3,590 spans total), saved at
`code/crowd17/next-token/quoted_dialogue_goldset.json`. 441 runaway-quote
"monster" spans (12.3% of spans) hold 83.3% of dialogue chars
(8,589,618 / 10,315,830) and 72% (122/169) of dem-comma hits — all OCR
artifacts swallowing whole articles (5k–72k chars each). Re-running the
census verbatim on the goldset and the de-monstered corpus (3,149 spans,
1,726,212 chars): 0 genuine dislocated-demonstrative + bare exclamatory
infinitive anywhere — the same 3 candidates as the parent's 6 (3 were
duplicates). The noise inflates hits but never fabricates candidates.
(**F266**, battery-quoted-dialogue-goldset PROMOTE.)

**The comedy dislocation gap is syntactic, not lexical.**
`reinforced-head-frequency-comedy` PROMOTE: 19 comedy + 19 drama files,
5,528,632 chars total. Head base rates near-identical (comedy 5.28 vs
drama 5.55 per 100k), but dislocation propensity 17.2% vs 27.7% and the
dislocation rate 0.906 vs 1.538 per 100k chars (exact binomial two-sided
p = 0.0398) — the deficit is syntactic rarity in comedy, not a
head-frequency artifact. The "never license infinitives" leg holds in both
registers (0 genuine bare-exclamatory-infinitive in 5,528,632 chars).
Caveat: the propensity-given-head difference is marginal (p=0.0688) and
the comedy P1 sample is small (n=23) — the exact locus share between
constructional choice and chance stays open. (**F267**,
battery-reinforced-head-frequency-comedy PROMOTE.)

**The reinforced-head + governed-infinitive fence now covers '?' too.**
`reinforced-pour-inf-interro` PROMOTE: the parent census verbatim on
~34.7M chars (60 files of `code/side-period/corpus`, 32,706,795 chars +
3 wider files, 1,987,682 chars), changing only the P2 terminator '!'→'?':
304 dem-comma hits, 2 '?' candidates (both hand-classified), 0 genuine —
the '?' windows are ordinary interrogative clauses, never exclamatory
infinitives under a dislocated head. (**F268**,
battery-reinforced-pour-inf-interro PROMOTE.) **Wording conflict
recorded:** the sibling topology null (N350) rejects this fence's
phrasing "reinforced heads govern infinitives" — 0/41 windows show a head
governing an infinitive; heads occur only as the infinitive's resumed
object. The fence stands; its wording needs a rephrase (see §6 item for
the supervisor's call).

**Register triangulation of the pour-inf fence: comedy says zero.**
`reinforced-pour-inf-widercorpus` PROMOTE: 14 vaudeville comedies (11
Labiche + 3 Scribe), 1,030,838 chars — the natural habitat of exclamatory
syntax — 6 dem-comma hits, 0 governed-inf exclamatory candidates; not one
window even contained a head-governed infinitive. Inventory check (6/1.03M
= 5.8 hits per 1M vs 231/27.66M = 8.4 per 1M in the diagnostic corpus):
same order of magnitude — a genuine absence, not an empty-search artifact.
Fence triangulated: 1841 register 0/4 (27.66M chars) + comedy 0/6 (1.03M).
(**F269**, battery-reinforced-pour-inf-widercorpus PROMOTE.)

**20 is a relative adverb at @1703 — exact word still open.**
`reladv-20-1703` PROMOTE (locus-level): at the @1703 locus ("[33]
n'importe [20] [62] ne [88-fin]"), French grammar alone kills noun, verb,
adjective, and general clause-adverb roles for 20 ("n'importe [noun]" is
ungrammatical); the "quel"/"qui/quoi" arms fence on ungranted assumptions.
Only the relative-adverb subclass (où/quand/comment) parses with zero new
assumptions. "n'importe" is a fused lexical item over the unique
stream-wide '94 30' adjacency (R20-029(b) adopted). The exact word stays
red-team venue (poly-20-docket, R20-126). (**F270**,
battery-reladv-20-1703 PROMOTE; battery grade, locus-level.)

**The @1049 segmentation resolves: [88 29 40] | [29 74 74].**
`seg-88er-1049` PROMOTE: nine "29 40" bigrams (@62/@291/@500/@597/@685/@758/
@1038/@1050/@1710) vs "40 29" ×1 stream-wide; the trigram 29 40 29 =
"er"+"e"+"er" (banked GT letters) forces the boundary at @1051|@1052 —
no-boundary or boundary-before-40 yields "eer"-initial words, unattested in
~34.5M chars of period French (`code/side-period/corpus`; zero genuine
"eer"-initial common words; "erreur" ×314, "erreurs" ×165, "errer" ×23 are
"err-" words). Matches 40's word-final-'e' profile (the "la première"
crib). Option A dies at kill grade. 88's and 74's values both unnamed;
the @729–735 battery's "88-infinitive" naming is constrained at this
window — recorded, not litigated. (**F271**, battery-seg-88er-1049
PROMOTE; battery grade.)

**88 is polyfunctional-looking; any uniform verb-88 claim must split.**
`tout-88-frame` PROMOTE (characterization, no value): under granted
79="tout", the @496-497 "tout [88]" frame admits noun, adjective, adverb —
finite verb and bare infinitive are dead there by grammar. The 23-window
profile (n(88)=23; 21 distinct predecessors, 19 distinct followers)
excludes none of the three surviving classes; 88 is verb-forced at @730,
@1049, and the '88 77' ×3 windows (@86/@646/@1541). Constraint: a uniform
verb-88 claim must declare a split at @496-497 — red-team venue, not a
battery call. (**F272**, battery-tout-88-frame PROMOTE; locus-level,
names no value or class.)

**17 is uniformly standalone.** `x17-wordbound-audit` PROMOTE: 15/15 X-17
windows audited (n(17)=15, repaired stream); zero force word-internal 17;
three force standalone (@308 split, @369 literal-route kill, @1289
11="la" determiner); positive legs ("première fois" @1040, "la fois"
@1289) confirm. Fois-slot typing may treat the 17 slot as a word boundary
on both sides. The inviting "tout fois" one-word reading at @452/@1461
("toutefois") is fenced at battery grade — A5 fixes 79="tout" as a whole
word, and revisiting needs red-team venue. Numbering note: the bar cited
@1038/@367; the actual 17 loci are @1040/@369 (recorded, not litigated).
(**F273**, battery-x17-wordbound-audit PROMOTE; audit deliverable;
17="fois" value already standing.)

**41 is noun-class at @5 — the parent census never tested 06's wordhood.**
`battery-41-05-class` PROMOTE (locus-level): @1–9 = `00 97 51 47 41 06 77
78 18`. 06='ent' is a bound ending: it cannot stand alone and cannot
compose rightward ("entle" is not a French word), so it must compose
leftward — 41 is word-internal in "41+ent" at @5, vacating the parent
census's "STANDALONE forced" (a same-day worker judgment, corrected with
cause — not a standing). Class enumeration: verb (number clash),
adjective, det/numeral/adverb (dead per grammar) all fail; only noun
("ce [N-ent] le [V-ver…]", "ce moment le verra"-shaped) parses. Corpus
leg: "ce [Xent] le [Y]" 5/5 nouns, 0 adjectives (~27.7M chars period
French). Provisional: load-bearing on provisional 77='le' and R16-005
78='ver' LEAD; the leg is delivered to the split-41-redteam docket.
(**F274**, battery-41-05-class PROMOTE; battery grade, @5 only.)

**41 is a standalone word at @808.** `battery-41-808-role` PROMOTE
(locus-level): the @804–812 frame `53 69 24 24 41 12 48 24 65` is
byte-exact; finite-verb 24@807 (standing R24) forces a word boundary
before 41; 12 attaches rightward ('12 48' ×4 independent @169/@709/@1075/
@1736 vs '41 12' ×1 @1508); the @1508 letter-tier rival differs on both
discriminating features and stays local — the same bigram parses
differently in the two frames, provably. Three independent legs converge
on standalone-word 41 at @808. 41's global tier stays red-team venue
(split-41-redteam); no polyvalence claimed. (**F275**,
battery-41-808-role PROMOTE; battery grade, @808 only; n(41)=19.)

**The modifier leg for 80 at @469 promotes — its gate was properly
satisfied.** `battery-adj-80-469-ratify` PROMOTE: "tout [80]ent" is the
core French intensifier frame ("tout + adjective"); -ent adjectives are
productive (différent, présent, prudent); the byte-identical frame "33 79
80 06" recurs at @469 and @1089 (06 census: 44 occurrences). Gate VERIFIED
and satisfied at red-team level: 06='ent' = R17-007 GRANT, re-confirmed
R20-011 and R20-064. Verb rivals all killed: 80|06 strands "ent" (not a
word), right-attachment forms no French word, left-attachment kills the
infinitive (never ends -ent) and 3pl finite (number clash with "tout").
Enlightenment: adjective vs adverb cannot be discriminated here ("tout +
adverbe" is as grammatical as "tout + adjectif", needs 33's value) — the
promoted leg is the modifier class, not the adjective subclass. 80's
global class stays verb-frame (A8/R20-121); no second polyvalence claimed.
@1090 fenced on the open 43 value. (**F276**, battery-adj-80-469-ratify
PROMOTE; battery grade — gate satisfied per the gate rule since its
premise is red-team-ratified.)

**@1556 stays the sole complete spelling anchor for 61.** `spell-61-anchor-
census` PROMOTE (of the fence): all 18 windows of 61 censused byte-exact
(n(61)=18, repaired stream); "61 40" ×1 stream-wide (@1556); @1556 ("61
40 17" = "première fois") is the sole complete spelling-composed window;
the 5 other letter-adjacent windows fail with stated causes
(ungrammatical, lead-only, non-word, fenced class). Any 61 extension
needing a spelling anchor is permanently blocked. Adopts standing without
re-litigation: val-61-premier's locus PROMOTE, val-61-contact's KILL of any
global 61 value, F264's conditioned ordinal-slot set. Cross-link: the
three ordinal-slot admissions (@279/@281/@645) have zero letter-valued
neighbors — ordinal admission does not create a spelling anchor; the two
fences coexist without conflict. (**F277**, battery-spell-61-anchor-census
PROMOTE; battery grade.)

**Follow-ups proposed by these batteries (all verified absent from the
queue by the workers; queueing is the supervisor's):** tonic-66-rearm
(gated), chain-follower-class, val-53-15-frame, val-52-1005-frame,
personal-tonic-governed-interr-drama, personal-tonic-interr-inf-negation-
prose, gov-interr-inf-ellipsis-shape, procreer-littre-absolute-date,
procreer-absolute-drama-corpus, procreer-56-semantic-reweight,
seg-77-03-722 / val-03-value-census, verb-91-277, syllable-91-pre-word,
participle-91-extend, adj-80-1090-43-rearm, poly-31-docket-input,
locus-1257-reseg, ne-508-reseg-rearm (armed only on red-team 62-value
grant), s5-37-385-adjudicate (P2 red-team escalation), neque-94lead-gate
(P4 — armed only when 94='ne' moves lead→grant at red-team level),
redteam-01-split-docket, redteam-55-polyvalence.

### Round-17 backlog fold, third batch (2026-10-09 UTC — 10 battery notes
read: 2 battery-grade promotes, 7 nulls, 1 gather-only red-team input;
NOTHING here is red-team ratified)

All F-numbers below are battery grade. Provisional tier inherited from
standing leads; no registry change is claimed by any battery.

**76=noun no longer rides on 77='le'.** `val-76-class-census` PROMOTE
(class-level): two granted "ce [76]" legs (@1273 via granted 47=ce, @1275
via granted 87=ce) license nominal-76 with zero new assumptions — the
evidential basis no longer depends on provisional 77='le' (R19-111's
original legs were all 'le'-conditional). n(76)=21, full
predecessor/successor census (predecessors: 77 ×3, 67 ×2, 48 ×2, 94 ×2,
16 ×2, 98/64/13/37/93/07/01/47/87/31 ×1; successors: 47 ×4, 42 ×3,
49 ×3, 45 ×2, 87 ×2, 01 ×2, 82/18/59/85/48 ×1). Verbal legs recorded as
sub-bar residuals: "qui [76]" ×1 @487, "ne [76]" ×2 @652/@1577 —
present but below the bar, not refutations. Downstream: the class block
on the @12 inversion route is removed; the trigger block remains, so the
98-76 fence narrows to trigger-only. Ground-truth anchors: granted
47/87 = ce; provisional 77='le' demoted to supporting legs only. (**F278**,
battery-val-76-class-census PROMOTE; no registry change — it strengthens
the existing R19-111 grant; red-team verdicts untouched.)

**The pour-proximal 41 cluster is phrase-shaped, not noise.**
`wordbound-41-pour-cluster` PROMOTE (boundary rule, local): of 55
occurrences of 00=pour, only 6 have a 41 within the next 4 slots
(@589/@590/@964/@1111/@1508/@1535, gap distribution d=2:1, d=3:4,
d=4:1). Rule R — boundary immediately after 00=pour; the pour-led word
closes at the nearest following 41 (a 41-41 geminate closes at its
second member) — parses 6/6 (≥5/6 bar passed; 5/5 as distinct phrases).
Two exact 4-gram repeats pin the frame: "00 86 56 41" ×2 (@961/@1505)
and "00 66 73 41" ×2 (@1108/@1532); "00 97 41 41" ×1 @587. Windows n1/n2
overlap in one pour-bracketed run ("00 97 41 41 09 00 92") with the
41-41 doublet reading as a word-internal geminate. Caveat carried: R is
local — 49 of 55 pours are not 41-closed; middle groups (97 / 86 56 /
66 73) are explicitly unvalued; no value claim is made. (**F279**,
battery-wordbound-41-pour-cluster PROMOTE; boundary structure only,
no contradiction with standing 41 verdicts.)

### Round-17 backlog fold, fourth batch (2026-10-09 UTC — 6 battery notes
read: 2 battery-grade promotes, 2 nulls, 2 kills; NOTHING here is red-team
ratified)

All F-numbers below are battery grade. Provisional tier inherited from
standing leads; no registry change is claimed by any battery.

**08 is word-internal 't', never a particle — and its five followers' classes
are named.** `val-08-successor-class` PROMOTE (n(08)=18, full follower census:
31×3, 65×2, 62×2, 91/34/21/67/24/52/29/01/43 ×1): 31 SPLIT — finite VERB on
two "qui [31]" legs (@338 a2_05 `64 31 14`, @1647 a8_04 `64 31 10`) vs
word-internal SYLLABLE on three "t[31]" legs whose complete-word left
neighbors force right-attachment (17=fois @881, 87=ce @1488, 67="et" @1520);
62 NOUN ("et [62] vient" @944, "[62] vient" @1324 — 'il' killed at kill
grade, noun-root règn-/trôn- tie open); 65 NOUN (R20-047 grant + "et [65]"
@922, "[65] qui" @1339); 21 NOUN (battery grade, 5 legs: "par [21]" ×3
@231/@1064/@1787, "[21] qui" ×2 @937/@1631); 43 NOUN (R19-064/R20-117 grant,
@1302 consistent). The frame test kills the particle hypothesis: bidirectional
attachment is proven (left "40 08"="et" @922/@944, right "08 31"
@881/@1488/@1520) and 08's right-neighbors are heterogeneous (nouns, verbs,
conjunction, GT letters) — a particle selects one complement class; 08
selects none. Corroborating 't' compositions: "45 08" @975 and "47 08" @1592
parse as "cet"; "37 08 29" @779 gives the "ter" syllable contact. Fenced
tension, not resolved: @134 "qui 21 65" forces a verb reading on a single
leg — below the split-declaration bar, needs a second verb-frame leg.
Ground-truth anchors: granted 64=qui, 96=par, 87=ce; provisional tier from
standing leads only. (**F280**, `val-08-successor-class` PROMOTE; no registry
change; red-team verdicts untouched.)

**52 is non-verbal and sub-lexical at @630 — the "et 08 [52-V]" frame is dead
there.** `val-52-630-frame` PROMOTE (n(52)=27): locus bytes @628–636 (row
a4_01) read "ce [78] et 08 52 et [63] [74] que". Frame-leg 1: 08="t" is a
bound letter on 4+ independent byte-exact windows ("40 08"="et" @921–922 and
@943–944, "[41]tire" @59–61, "[37]tre" @778–780) — a letter cannot be a
clausal subject, so "t52" is word-internal and Arm A is impossible at @630.
Frame-leg 2: @1332 "pre 52" (70=pre is pencil ground truth, a bound prefix;
unaccented "pre" is not a French word) independently forces 52 into
sub-lexical composition. Distributional corroboration independent of 08's
value: 08 is never a standalone word-sized unit in 18/18 windows — the
"standalone 08" premise has zero support. Adverses answered, not ignored:
"qui 52" verb legs (@1342, @1435, n("64 52")=2), "ne 52 [INF]" adverb legs
(@1294/@1807, n("94 52")=3), "la 52" superlative legs (@1006/@1123/@1721,
n("11 52")=3) are accepted as genuine at OTHER loci — 52 is split-shaped
across loci (like 88, `tout-88-frame`); this verdict is locus-level only.
The "08 52" bigram is a stream hapax (n=1) and the "et _ 52 et" frame is
unique to @630–633. Caveat carried: 08="t" is battery-grade, NOT red-team
ratified — stated as conditional premise. (**F281**,
`val-52-630-frame` PROMOTE; locus-level only, no 52 value named; no registry
change.)

### Round-17 backlog fold, fifth batch (2026-10-09 UTC — 1 battery
note; battery grade)

No promotes in this batch.


### Round-17 backlog fold, sixth batch (2026-10-09 UTC — 8 battery
notes; battery grade)

Notes trace: `code/crowd17/report_inbox/` (doublet-589-97-role,
en-988-standalone-leg, laisser-unique-sweep, adj-37-independent-slot,
det-385-leftedge, residual-86-finer, un-71-det-census,
redteam-55-polyvalence). 3 promotes, 0 kills, 4 nulls, 1 gather-only
red-team input — verdict tags in
`code/crowd17/next-token/battery-queue.json` match 8/8 (1,468 entries:
1,028 verdict, 440 queued/other).

- **F282** — doublet-589-97-role PROMOTE (class-level): 97 = VERB class.
  Bar ("≥2 independent legs name one class with zero kill-grade
  contradictions") passed on all 10 windows of 97 in the repaired
  1,847-pair / 96-type stream (`data/upstream-ct_R5005.txt` +
  `code/side-keyhunt/repaired_offsets.json`, parsed per
  `code/side-keyhunt/repair_parse.py`). Four clean "pour"-infinitive legs
  at independent loci (@2, @288, @588 — the doublet locus, @1823), each
  `00=pour [97] X` under granted 00="pour" (A9); three verb-consistent
  supporting legs (@94 with 46="que" pencil GT, @525 with 47="ce" granted
  A4, @1412 with 69 noun-class grant R19-109). Noun rival dead (zero
  determiner precedes 97 in any window). @751 forces letter-tier ("97e",
  40="e" pencil GT cannot stand alone) — resolved as a positional split
  (mirroring the established 88/52 non-uniformity), not a kill-grade
  contradiction; @299/@566 stay ambiguous. Scope: class, not value; any
  formal split declaration is red-team venue (suggested docket:
  split-97). PROVISIONAL, battery grade — red-team ratification pending,
  and against the live record: frame-97-profile's infinitive-class
  promote (F125) was REJECTED at R18-009/R18-023; this battery's broader
  VERB-class framing honors but does not re-litigate that rejection —
  whether it evades the rejection's logic is a red-team call. Follow-ups:
  split-97 docket (red-team venue); doublet-589-09-role (already queued
  per N381; 97's verb class now constrains the "41 41 09" resolution).
- **F283** — en-988-standalone-leg PROMOTE (locus-level): 'en'-local
  reading at @988 — "48 [en] [76-N]". Both bar legs passed on the
  repaired stream. Right edge: @988 = 01 with follower 76 (`01 76`
  stream-unique at @987–988, row a6_01); 76 a promoted masculine noun
  (R19-111, confirmed by battery-val-76-class-census "ce [76]" legs
  @1273/@1275, no longer dependent on provisional 77="le") — licenses
  "en [N-masc]". Left edge: 48 takes prepositional complements at @377
  ("m [48] pour la"), @1212, @1525 under standing values (82='m' GT,
  00='pour' granted, 11='la' GT, 96='par' granted, 45='ce' A11) —
  licenses "48 [prep] [nominal]" with 01 in the preposition slot. Legs
  independent (neither assumes 01='en'). Rivals dead at this locus:
  uniform-'on' kill-grade dead at @988 (battery-val-01-census); 28
  01-windows censused, no other offers a nominal follower under standing
  values. Scope: locus only — does NOT name uniform 01='en' (dead at 9
  windows); does NOT touch R20-016 ('en'-local LEAD at the 01-24 windows
  — redteam-01-split-docket venue). PROVISIONAL, battery grade —
  red-team ratification pending; the reading confirms at battery grade
  evidence the redteam-01-split-docket already gathered (no adjudication
  yet). No standing verdict contradicted; §7 intact. Follow-ups: none at
  battery level (docket already open).
- **F284** — laisser-unique-sweep PROMOTE (candidate-elimination claim
  only; NOT a 33="laisser" value promote — registry unchanged).
  Re-derived the repaired stream (1,847 pairs / 96 types) and re-tested
  all 7 erstwhile -er candidates for 33 (donner, montrer, prouver,
  trouver, porter, envoyer, prononcer) against the @1477 discriminator
  frame ("veut [X]er m[16]" = `53 60 06 67 33 29 82 16 98`), byte-exact at
  the 5 re-derived 33-29 windows (@273/@626/@1232/@1424/@1477). All 7 die
  at kill grade, 16-class-independent: with 82="m" banked, @1477 is a
  post-infinitive clitic licensed in French only by the causative class
  and imperatives; all 7 candidates are non-causative. Independent corpus
  check (56 French files, 29,487,677 chars): genuine "V(-er,
  non-causative) + me + INF" post-infinitive = 0 hits (worker-reported,
  not independently re-read). Uniqueness extends from tested to ALL -er:
  the French causative periphrastic class is closed {faire, laisser},
  faire is not -er, so 'laisser' is the sole -er verb that can occupy
  @1477. The 33="laisser" identification stays UNGATED-OPEN: gated on
  16=inf (frame-82-16) and 85=inf (stem-85), both provisional. Scope
  fence: under the whole face 33="dire", "dire" is likewise
  non-causative but out of scope (A10 HOLD untouched). Gate: R19-188
  SATISFIED and supported by the red-team record
  (`code/crowd17/report_inbox/processed/next-token-redteam-r19.md` line
  1193: RATIFY the porter+envoyer eliminations, conditioned on the "82
  16" segmentation — condition checked against frame-82-16, null
  2026-10-09). No standing/red-team verdict contradicted. Follow-ups:
  16=inf discriminator (frame-82-16); 85=inf (stem-85); a7_10 offset
  validation (canonicality caveat stands — a re-pairing could dissolve
  @1477).

## 5. Failures & null results (N-series)

"Nulls are first-class in this lane. Every one below is a measured outcome,
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
- **N43** — Unconditioned 48="de" **KILLED** (round-12/R13, French-blitz
  syntax48 battery, kill-grade): 10 clean kill windows (author claimed
  11 — @1212 demoted on re-read); verified v8-excluded (Levant-only)
  per the round-12 v8 phrase-zero caveat. Conditioned "de ce que" islet
  (@863) stays LEAD; vowel-initial conditional constraint banked.
  48 stays UNIDENTIFIED; ML-1/ML-2 missing legs unfilled.
- **N44** — "gouvernement"/"gouvernent" readings **KILLED at all 7
  windows** (round-12/R9, French-blitz gouvernement re-reader); **77=
  "gouv" DEMOTED→disfavored**; 78 fork leans "er" as corroboration
  (no status change); ISLET 3 corroborated (no upgrade); @647 recorded
  OPAQUE; new 06-«ne»-allophone lead.
- **N45** — é-initial-noun theory (entrevue/expédition/…) **RETIRED
  permanently** (round-12/R10): dead twice over — first by round-9/10
  refutation, second by the première-noun hunter's independent
  re-derivation. "la première fois" @1034 GRANTED LEAD (three legs);
  20="fois" homophone battery warranted for round 13.

### Round-16 kill batch (crowd16, battery-adjudicated 2026-10-08 UTC)

- **78="er" — KILLED distributionally** (round-16 forks battery,
  `test_forks.py`): determiner-predecessors 78 16/31 vs 29="er" 2/45;
  after 33=INF: 78 0 vs 29 5 — near-complementary distributions (odds
  ratio ~22.9). If 78="er" it would pattern like 29; it patterns like
  a noun-syllable. "ver" LEAD survives (un-killed, not proven).
  ver-78 status round-17 wave-6: 'ver' LEAD stands (R16-005, ratified
  R17-006); the successor-completion arm is KILLED ('ce ver[48/65]' —
  @364/@1397 force false); @296 stays the fenced 1-window residual
  (N78); W2 @573's one-word boundary is ver-78-independent (F108).
- **37 and 42 predicative est-frames — DEMOTED from GRANT to HOLD**
  (round-16 est battery, `test_est.py`): 37's "6 adjective legs" VOID
  (all six 59-cells class LEFTOVER in
  `code/crowd10/conditioner59/classification.json`; @1795/@1796 are
  ONE physical window — "6+1" was 6 unique); 42's 2 legs void
  (LEFTOVER + ESTE). Zero windows satisfy ISLET-10 conditioning for
  either — the frame is unanchored, not killed (round-15 A1's
  successor-profile compatibility survives as unanchored evidence).
  "est 35" ×3 → 0 est-arm legs; "est que" ×2 → [V-este] que
  (verb+que-clause); "est 32" @448 → ESTE.
- **45="ce" — DEMOTED from PROMOTE to HOLD** (round-16 forks battery):
  "ce verdict" ×2 (@573/@982, on banked 87/47="ce") FORCES 45="dict"
  there; "par ce" ×2 (@602/@1213, on promoted 96="par") FORCES 45="ce";
  @314 contested — the value is bipartite (positional allophony, not
  one value). The round-16 par-rest PROMOTE is superseded by its own
  round's forks adjudication. W2 @573 gate (F108): 78-45 is one word
  (ver-78-independent); kill-scope for 45='ce' is exactly 1/22 windows
  (@574); A11 HOLD stands on the remaining 21. The @602 'par ce' leg is
  now the 45->93 x3 cluster (F110), 93 nominal there, global class
  fenced to verb-93.
- **A15's "on est" legs — VOID** (round-16 le battery): 59@1190/
  @1448/@1804 are ESTE, 59@1291 FENCED — the round-15 A15 battery and
  red team never checked 59-class (scope gap). 84="on" stands
  weakened; new tension for red team: the ESTE verbs CONTAIN 84.
- **46-85-29 deliberative-infinitive claim — KILLED**: 46-85-29 = 0
  globally; @95 is 46-29-85 (que/ce finder mislabel; do not cite).
- **84="fait" — REJECTED** (round-16 le battery): re-litigates A15
  without new evidence; flagships don't parse (@1189 = 06-84, not
  77-84; @1447/@1803 "qui le fait est" ungrammatical; 59 ESTE).
- **84-noun ("l'[84] est") — REJECTED as overtaken** (round-16 m
  battery): @166 is 82-84 = "mon" (A15 established) — the finder's
  elision premise misreads the trigram.
- **48="e"-letter — DECLINED** (round-16 pre battery): no independent
  legs; re-reads A7's 4 granted "me [48]" windows and parses worse
  (1/4 possible vs 4/4 verb-slot recurrence) — re-litigation without
  new evidence. 48 stays open (verb-stem candidate stands).
- **@108's "veut" fork vote — REJECTED** (round-16 la battery): one
  physical window [0,46,11,21,67,93,29,89]; the reading requires
  unbanking 00="pour" at @106 — banked wins ties; recorded as a
  conditional only.
- **70-polyvalence option (b) for @369 — not assumed** (round-16 fois
  battery): against lane law (67 sole); ESCALATED to red team.
- Record corrections (all byte-verified, re-derived): **67-33 ×1→×6**;
  12-48 ×7→**×5** ([169,709,809,1075,1736]); 26-30 ×3→**×4**; 64-39
  frame → **×1 @606** (singleton); 59-39 @763 = **"n'est [39]"**
  (mislabeled "est à"); 37-01 ×2→**×3**; 37-78 ×2→**×4**; 33-00-79-80-06
  → **00-33-79-80-06** (transcription order); @396 order is 67-64-79,
  not 64-67-79.
- 33-candidate **vouloir KILLED** ("et vouloir que" ✗, "ce vouloir" ✗);
  penser WEAK (round-16 classes battery, finder French judgment —
  frames verified).

### Round-17 null/kill batch (crowd17, 2026-10-08 UTC)

- **N46 — single-value 33="dire" KILLED** (battery 4acdfc83): orphan
  rate 5/25 = 20% > 10% bar (5 stem windows need `[33]er` under
  banked 29="er"); croire ties "dire" on every whole-frame (C2 FAIL);
  "erreur" word-shapes dissolved 4 ways (needs 84="ur" vs granted
  84="on"); @1421-24 chain needs BOTH values in one window. Trace:
  `code/crowd17/report_inbox/battery-dire-33.md`.
- **N47 — 33="croire" vs "dire" tiebreak NULL, 33 stays OPEN** (battery
  da6545e4): all 25 windows grammatically symmetric under both
  hypotheses ("pour [inf]" ×8, "veut [inf] que" ×2); C1 (croire-only
  frame) and C2 (dire-only) both FAIL. Honest cost: shared residuals
  @1502 ("on"+infinitive) and @1642 ("n'" before consonant-initial
  verb) fail under BOTH and implicate neighbors 84/12, not 33.
  Trace: `code/crowd17/report_inbox/battery-croire-33-tiebreak.md`.
- **N48 — 33={dire, X-er} 2-member set UNFALSIFIED but unpromoted**
  (battery 783d6363): X identified via contact profile but NOT named
  (family: donner/montrer/prouver/trouver/porter/envoyer/laisser/
  prononcer…) — identification required by the bar, not achieved;
  orphans 2/25 = 8% (@1502-first-33, @1700) inside the 10% tolerance;
  stem windows cohere (one governor set {veut ×3, ce/se, 37}). The
  "croire ties dire" adverse NOT answered; 89/16 open block X's
  discriminating complements. Trace:
  `code/crowd17/report_inbox/battery-dire-33-set.md`.
- **N49 — @611 re-parse under 77="le" KILLED (claim-grade)** (follow-up
  bc8ed16f): no grammatical parse of "47 77 87 83 70" within the
  ≤1-assumption budget ("ce le ce" never grammatical); the sole
  grammatical rescue (87="cède") requires ungranting 87="ce" — fenced
  to red team. Control: the blocker persists under ANY 77 value, so
  77="le" provisional standing is untouched. Trace:
  `code/crowd17/report_inbox/battery-le611-reparse.md`.
- **N50 — 77="le" battery NULL, stays PROVISIONAL** (battery 7b91f7ab,
  44 windows, 20 distinct followers): Clause 2 PASS (seven frame
  families: "l'on" ×7, "le [78]" ×7, "et le" ×6, "[verb]-ent le" ×6,
  "ce le [verb]" ×2, "le [81]" ×4, "le [86]" ×5); Clauses 1 and 3 FAIL
  (@611 unparseable — see N49; @1033 "80-77" escalated — 80's
  inflectional mood alternation is red team's call per §7, evidence
  passes on 17 windows of 80). Trace:
  `code/crowd17/report_inbox/battery-le-77.md` and
  `battery-le1033-imperative.md`.
- **N51 — ce45 second mirror frame-type NOT FOUND** (finder beat, 22
  45-windows, 14 distinct successors, scatter 0.64): 45 needs ≥2
  mirror frame-types, has ~1.5 ("45-46" @437 "ce que" ×1 stays the
  half-mirror); A11 HOLD stands, never re-litigated as value claim.
  Live fork: 78-45 ×4 reads "verdict [13-55-61]" under 78="ver"+45=
  "dict" and ungrammatically under 45="ce". Genuine residuals @678/
  @401 ("le/la ce" ungrammatical under both live claims), @332
  unparsed under everything. Trace:
  `code/crowd17/report_inbox/next-token-findings-ce45-frames.md`.
- **N52 — 62="on" unconditioned KILLED** (collision-62-84, §7 polyvalence
  rule): with zero crossover re-derived (62→94 x9 vs 84→59 x4;
  62→59 x0; 84→94 x0) the two "on" claims lived in different slots,
  and 62's claim failed the kill-grade discriminator at @507 ("l'on
  ne" iff 62="on"; "le il ne" unparseable under 62="il"). 62's nine
  62→94 frames re-read as "il ne" (8 clean, @508 fenced residual);
  62="il" is now the demonstrated side, 84="on" the unconditioned
  holder. Trace: `code/crowd17/report_inbox/battery-collision-62-84.md`.
- **N53 — "34 29 40 12 94" one-word composition KILLED** (enne-word-64):
  the forced letter string "ierenne" admits no French word (kill
  grade); the analytic readings of the five pairs hold individually —
  only their one-word composition fails. Residual R-enne-61 recorded
  with stated cause. Trace:
  `code/crowd17/report_inbox/battery-enne-word-64.md`.
- **N54 — 78="ver" battery NULL, escalated to red team** (ver-78-rebar;
  the first ver-78 battery's bar was lane-illegal, the rebar is
  lane-legal): all three clauses re-derived clean on the repaired
  stream — determiner predecessors 78: 16/31 vs 29="er" control 2/45,
  predecessor==33 78: 0/31 vs 29: 5/45 (OR=22.93, corrected
  attribution — the queue's evidence gloss transposed 29/78, now
  fixed), "ce verdict" x2 @573/@982 (+x2 @313/@1164), "ce 78" x7 all
  exclude "er" — but promote would contradict standing red-team
  grading R16-005 (bundle graded LEAD, not settled), and the positive
  "verdict" legs are conditional on the un-granted 45="dict" lead
  (R16-004). NULL recorded per protocol §5; red-team question:
  ratify NULL→promote with @296 as fenced residual, or require the
  R16-004 45="dict" dependency to resolve first? Follow-ups queued:
  ver78-la78-census (P2), ver78-45-dependency-gate (P3). Re-derivation
  script `code/crowd17/next-token/ver78_battery.py` (outputs matched
  the prior report's offsets/counts exactly). Trace:
  `code/crowd17/report_inbox/battery-ver-78-rebar.md`
  (supersedes `battery-ver-78.md`).
- **N55 — prenne-70-12-94 battery NULL, fenced for red team**
  (battery prenne-70-12-94): composition "pre"+"n"+"ne" PASS at both
  windows (70-12-94 occurs exactly 2x stream-wide, closed set), but
  the subject search FAILed at both — @1548 (92 nominal: "la 92" x3,
  "92 qui" x2; empty slot after "que", no licensed post-verbal or
  elliptical subject) and @348 (no trigger, no subject-shaped
  candidate; the "prennent" 74="nt" re-parse is unpromoted
  speculation). 12="n"/94="ne" duality UNRESOLVED: per the joint
  constraint neither side may advance on THIS evidence — F85/F87 are
  not downgraded. Trace:
  `code/crowd17/report_inbox/battery-prenne-70-12-94.md`.

### Round-17 null batch, wave 3 (crowd17, 2026-10-08 UTC)

- **N56 — adj-32 battery NULL** (bar: est-frames hold + 94/48
  followers resolve + verb-tension adjudicated; clause 1 PASS,
  clause 2 FAIL, clause 3 FENCED). The three 59->32 est-frames
  (@317/@449/@1211, repaired-stream offsets) hold and the 48
  followers resolve as feminine "-e" on 32 ("est [adj]e toutefois"),
  but @317's "94 06" does NOT resolve: 94-06 is a hapax (1/37
  94-followers), 06 is not finite-verb-shaped (bare-"ne" fails),
  and no expletive-"ne" frame is established (FAIL). Clause 3:
  @33 and @855 force verb-shaped 32 ("qui 32" / "qui [32]e, on"),
  while the predicative frames show adjective/participle-shaped
  32 — the needed dual behavior is a second polyvalence, a
  red-team act per S7, not a battery declaration. Not promote
  (clauses 2–3 unmet); not kill (no predicative-frame window
  forces a non-adjective 32). 32 census: n=13. Follow-ups queued:
  verb-32 (narrower verb-stem battery), ne-06-317-gate (gated on
  ent-06), fem-e-48 (48 as inflectional "-e"). Trace:
  `code/crowd17/report_inbox/battery-adj-32.md`.
- **N57 — fork-78-45-adjudication NULL** (bar: (a) joint-with-ver-78
  conditional, (b) positional rule; clause (a) VACUOUS — ver-78's
  verdict is null, so the antecedent "78='ver' promotes" is false —
  clause (b) PASS). The four 78-45 windows (@313/@573/@982/@1164)
  cannot adjudicate while ver-78 is unsettled; 45="ce" is NOT
  killed, 45="dict" is NOT promoted. Positional rule R-pos stated:
  45="dict" iff immediately preceded by 78 (the single word
  "verdict"), else 45="ce" — per-window parses recorded — but
  declaring it is a red-team act per S7 (67 is the sole true
  polyvalence). Evidence owned by follow-ups: fork-78-45-rerun
  (P1, gated on ver-78), dict-78-45-wordbound (P2), w1-314-ambig
  (P2). Trace:
  `code/crowd17/report_inbox/battery-fork-78-45-adjudication.md`.
- **N58 — dict-45 battery NULL** (bar: "verdict" frames parse +
  45's contact profile matches the "-dict" syllable; clause (a)
  INCONCLUSIVE-conditional, clause (b) FAILS as a general value).
  Under 45="dict", 18/22 windows are ungrammatical (a bound
  syllable predicts a near-deterministic "ver" predecessor; the
  general reading is distributionally rejected — implicitly by the
  standing A11 HOLD, never the live claim). The claim survives only
  as the positional reading (45="dict" iff pre=78 — the four
  78-45 loci all consistent), which needs the red-team declaration.
  The A11 45="ce" HOLD stands untouched; its mirror legs (45-64 x3
  @314/@340/@1024) re-derive on the repaired stream. 'ce verdict'
  x2 confirmed (87-78-45 @572-574, 47-78-45 @981-983). Follow-ups:
  dict-45-w3-ceci, dict-45-ce-rival-1165, dict-45-host-inventory.
  Trace: `code/crowd17/report_inbox/battery-dict-45.md`.
- **N59 — frame-37-reexam NULL — ESCALATION, red-team
  re-adjudication required** (escalation battery: bar = re-derive
  fencing evidence only; all 5 evidence clauses PASS). The
  est-finder's fencing arithmetic is confirmed exact on the
  repaired stream: under standing ISLET-10 law, five of the six
  59->37 legs are unlicensed-pre LEFTOVER (VOID) and the sixth
  (@1796, pre=94) is licensed but S5-fenced on 37="le" MEDIUM.
  **The round-15 A1 battery and its red team never checked the six
  legs against classification.json — a scope gap; whether it voids
  A1's clause (a) (37 legs 6->0, 42 legs 2->0) is the red team's
  call (D1).** A1's "+1 negated leg @1795" is a double-count
  (stream[1794:1798] = [42,94,59,37] — one physical window; 6
  unique windows, not 7). Controls: 32 keeps 2 valid legs (@316,
  @1210); 42 has 0; 59->19 is 1 HOLD window (the "x2" was one
  physical window). Live 37 evidence outside the est fight
  re-derived: "qui 37" x3 verb frames, "la 52-37-43" x2, "que
  84-24-37" x2, 37-01 x3 (A12), 37-78 x4, 52-37 x4. No verdict
  downgraded here. Trace:
  `code/crowd17/report_inbox/battery-frame-37-reexam.md` and
  `next-token-findings-est-reexam.md`.
- **N60 — s5-foundation battery NULL — ESCALATION: evidence
  contradicts the S5 standing fence** (bar: (a) >=2 windows where
  37="le" forces ungrammatical French, (b) @913 re-derived with
  neighbors, (c) zero windows requiring 37="le"; all three PASS,
  but the result contradicts round-7 S5 (37="le" MEDIUM)). Five
  windows force ungrammatical French under 37="le" using only
  banked/promoted anchors: @51 and @1655 ("le la" article+article),
  @529/@1357/@1444 ("le qui" determiner+relative-pronoun). @913
  re-derived: "le par" (37-96, the ONLY 37-96 adjacency
  stream-wide; 96="par" promoted) is ungrammatical — an article
  cannot govern a preposition; neighbors 83/09 cannot rescue it.
  Zero windows require 37="le". S5's sole datum fails the "le"
  reading; S5 stands only as a fence pending red-team
  re-adjudication (follow-up s5-foundation-r2 proposed). Trace:
  `code/crowd17/report_inbox/battery-s5-foundation.md`.
- **N61 — lon-ne-77-62-94 battery NULL — standing-verdict
  contradiction escalated to red team** (bar: kill 62="il" on this
  frame iff "le il ne" is unparseable AND "l'on ne" parses;
  clauses 1 and 2 both PASS at trigram level — the discriminator is
  real: "et le il ne" has no clean French parse; "et l'on ne"
  reads clean on "l'on" x7 corpus support). The kill conclusion
  would install 62="on" at @508, which DIRECTLY contradicts the
  standing collision-62-84 KILL (F91/N52) that fenced this window
  as residual anomalous and deferred a conditioned 62="on" to the
  red team as a second-polyvalence act (S7). Per S5.3 the battery
  does not overwrite the verdict; the contradiction is queued as a
  red-team decision item (lon-62-on-conditioned). The "94-64" =
  "ne qui" right edge is a singleton (x1 stream-wide) and a second
  independent reason the window cannot settle at battery level.
  Trace: `code/crowd17/report_inbox/battery-lon-ne-77-62-94.md`.
- **N62 — stem-33-86 battery NULL** (bar: stem-vs-whole adjudicated
  per window with <=10% orphan rate; clauses 1–2 PASS, clause 3
  FAIL — 6/57 = 10.5% > 10%). 33: 5 stem / 18 whole / 2 orphans
  (8.0% — meets the bar alone). 86: 4 stem / 23 whole / 4 orphans /
  1 fenced (@1739, ni-frame; 12.5%). Orphans: @1502 ("on"+
  infinitive), @1700 ("dire ne [30]" order), @300, @716, @1131,
  @1147. **Data-quality note**: the queue's "12 windows of 86" was
  the pre=00 SUBSET, not the total — repaired-stream truth is 86
  n=32; any battery scoping 86 to 12 windows undercounts 20.
  (stem-86's bar must be re-barred before dispatch.) The set model
  (33 = {"dire" whole, X-er stem}; 86 = {whole infinitive, [86]er
  stem}) is unfalsified; follow-ups: orphan86-300, orphan86-716,
  orphan86-1131-1147. Trace:
  `code/crowd17/report_inbox/battery-stem-33-86.md`.

### Round-17 null batch, wave 4 (crowd17, 2026-10-08 UTC)

- **N63 — ce-frame-45-64-96-43-87-01 battery NULL** (bar: (a) both
  windows parse with 43 named, (b) the "qui ce qui" left edges
  parsed or fenced; clause (a) CONDITIONAL-pass only, clause (b)
  FENCED). The byte-identical 6-gram "45-64-96-43-87-01" occurs
  exactly ×2 (@340, @1024). Both windows read "ce qui par [43] ce
  [01]" iff 43="suite" — the sole candidate of noun-43's set
  {suite, condition, maniere, mesure} grammatical after "par" ("par
  condition/maniere/mesure" are not French); 43's value arm is
  noun-43's, so the clause cannot pass unconditionally. Left
  edges fenced with stated cause: @340's "64-31-14" (31/14
  value-open) and @1024's "53-84-92-64" (53/92 open; whether a
  clause boundary falls between @1023 "qui" and @1024 "ce" is
  undecidable until 92's class resolves — gates on N64). Not kill:
  neither window forces the reading false. Follow-ups queued:
  noun-43-discriminator, edge-1024-clause-boundary,
  edge-340-31-14. Trace:
  `code/crowd17/report_inbox/processed/battery-ce-frame-45-64-96-43-87-01.md`.
- **N64 — class-92 NULL** (bar: ≥3 of 92's 22 windows parse under
  the named class + zero forced contradiction). Full 22-window
  profile re-derived on the repaired stream (n(92)=22 confirmed;
  predecessor/follower counts match the queue exactly). The
  profile forces disjoint classes at disjoint governor sets: "pour
  [92]er" @1154 (92 takes the -er infinitive ending — the
  strongest single window, verb-stem-shaped); "la [92]" ×3
  (article+noun/adj or clitic+verb); "on [92]" ×2 (forces verbal);
  the only true ne-governor is @60-66 (the @1549 94 is word-internal
  to "prenne"). No standing red-team verdict contradicted: A14
  granted 92 only set-level INF-signal ("genuinely ambiguous");
  A6's "-ere" value kill untouched (@683 fenced, never re-valued);
  the 09~92 HOLD untouched. Escalated to the red team. Trace:
  `code/crowd17/report_inbox/processed/battery-class-92.md`.
- **N65 — erstem-33-id NULL (conditional lead)** (bar: name X iff
  its contact profile matches a real -er infinitive's valency). The
  5-window profile of the 33 stem (33-29 ×5 @273/@626/@1232/
  @1424/@1477; governors {67 ×3, 47 ×1, 37 ×1}; complements {87
  ×2, 89 ×1, 85 ×1, 82-16 ×1}) is distinctive and selects
  "laisser" uniquely among candidate -er infinitives — but the
  selection is conditional on two open values (16, 85) and two
  adverses stand unanswered. This is a red-team LEAD, not an
  identification. Not kill: no window forces the stem reading
  false. Coordination: x-33-laisser-test (queued) owns the 16/85
  infinitive gates. Trace:
  `code/crowd17/report_inbox/processed/battery-erstem-33-id.md`.
- **N66 — le83-window NULL (bar's fence path)** (bar: resolve iff
  ONE 83 value parses both "le [83]" @1216 and the 98-83 ×5
  "vient de" windows; else fence 83 as the blocker, not 77).
  C2 PASSES under 83="de": all five 98-83 windows parse as "vient
  de [X]" — load-bearing on the unconfirmed 98="vient" reading
  (frame-vient-parvenir adverse). C1 FAILS: "36 77 83" @1215-1217
  = "le de" is ungrammatical in every clause position; no elision
  rescue ("de" is consonant-initial). No other single value
  satisfies both clauses. 83 is fenced as the blocker; 77="le"
  provisional is not blamed. Trace:
  `code/crowd17/report_inbox/processed/battery-le83-window.md`.
- **N67 — ne-06-317-gate KILL (gate claim falsified)** (bar:
  discriminate bare-ne + finite 06 vs elided "n'[06]" vs
  adverb-06; gates clause 2 of a future 32-value promotion). Naming
  06 (F97 "ent") did NOT resolve the @317 "94 06" hapax: all three
  pre-registered readings fail at kill grade ("ne ent la" —
  ending without stem; "n'ent" is not a word; no stem for the
  adverb reading). @317 stands as a fenced residual. This does not
  downgrade adj-32 (N56 already records @317 fenced); the gate is
  closed and the follow-up retired. Trace:
  `code/crowd17/report_inbox/processed/battery-ne-06-317-gate.md`.
- **N68 — noun-26 NULL (umbrella adjudication)** (bar: 26 assigned
  one class with all 17 windows parsing, or a positional rule
  stated). One-class resolution is FALSIFIED at kill grade on both
  sides (Clause 1 FAIL). The positional rule is stated with full
  evidence — "26 = feminine noun iff immediately preceded by
  11='la', else verb-class" — and Clause 2 passes as a finding, but
  declaring it would be the lane's second polyvalence, a red-team
  act per S7, so the battery cannot promote it. Headline for the
  red team: the umbrella resolves to a positional noun/verb rule
  with @1560's "pas" as the residual; adjudication required.
  (Closes the dedicated noun-26 battery queued in wave 2.) Trace:
  `code/crowd17/report_inbox/processed/battery-noun-26.md`.
- **N69 — stem48-exclusive-legs NULL** (bar: retire-frame iff zero
  windows require the stem reading; hold-frame iff ≥1 requires it
  AND letter-"e"-required windows stay below 10%). Full 38-window
  sweep of 48 under 48="e" vs 48=verb-stem: the verb-stem frame has
  exactly two exclusive legs (@1229/@1589, "…[48]er ce" ×2,
  byte-identical trigram) — it cannot retire — but letter-"e" is
  required at 14/38 windows (36.8% floor) — the frame cannot hold
  as a general claim about 48 either. The standing battery-
  promoted 48="e" and the red-team-granted A7-L2 verb-stem frame
  are now explicitly in tension under the §7 sole-polyvalence rule
  (67 et/veut only); A7-L2 is NOT overwritten here — its live
  scope is its two exclusive legs unless the red team narrows or
  retires it. Escalated. Trace:
  `code/crowd17/report_inbox/processed/battery-stem48-exclusive-legs.md`.
- **N70 — verb-48 NULL (escalation)** (escalation battery: the
  A7-L2 verb-stem frame vs the standing battery-promoted 48="e").
  The grant's 7 legs are not falsified (@1229/@1589 favor the stem
  reading and strain under 48="e"), but the full 38-window contact
  profile does not match verb stems: 12/38 windows are better
  explained as word-final letter-"e", and the profile's boundary
  rate (0.263) matches function cells, not the clean stem 85
  (0.000). Not kill: no window forces 48≠stem. Per §7 the A7-L2
  grant is not overwritten; the red team adjudicates
  narrow-to-exclusive-legs vs retire. Trace:
  `code/crowd17/report_inbox/processed/battery-verb-48.md`.

### Round-17 null batch, wave 5 (crowd17, 2026-10-08 UTC)

- **N71 — fork-78-45-rerun NULL** (bar's conditionals key on a
  ver-78 resolution that never happened): ver-78 and ver-78-rebar
  are both null (R16-005 LEAD, unsettled). The fork stays open
  exactly as the earlier adjudication left it: what-if parses
  recorded, R-pos positional rule awaiting red-team declaration
  per protocol §7. No contradiction with any standing verdict
  (A11 HOLD and R16-005 LEAD both untouched) — nothing to
  escalate. Trace: `code/crowd17/report_inbox/processed/battery-fork-78-45-rerun.md`.
- **N72 — frame-62-94-79 NULL** (frame-type real, parse fails): the
  frame-type "62-94-79-14-60" is real (byte-identical ×2, two
  frame-exclusive bigrams, parallel "13 [92/93]" left edges,
  genuine "ne...pas"/"ne...que" closers) but does not parse under
  standing values or with one stated new-value assumption for
  14/60. The blocker is the position of 79="tout" (red-team granted
  A5) between "ne" and the verb slot. No red-team verdict is
  contradicted: A5 (79="tout"), the il-62 promotion (which read
  these windows as "il ne tout" only for 62's subject slot), and
  the pas-30 promotion (which used "94→30" only as a "ne...pas"
  leg) all stand untouched. Trace:
  `code/crowd17/report_inbox/processed/battery-frame-62-94-79.md`.
- **N73 — frames-80-89-indep NULL** (independence arms fail):
  77-independent verb legs EXIST for both cells (infinitive-slot
  via 24-modal: 80 @564/@672, 89 @221/@985), so the frames do not
  fully collapse without 77="le" — BUT hard non-verb
  contradictions BLOCK independence: @1155: 80=determiner ("pour
  [92]er [80] fois"); @1376: 89=noun/adverb ("pour [86-inf] [89],
  on..."); @468 adjective-shaped for 80 conditional on 06="ent".
  A8's condition (77="le") remains load-bearing for A8's cited
  frames (C3 fenced unfixed; 'tout [80]' re-parsed; 29-frames
  tense), while the new infinitive-slot legs do not need 77 at
  all. Trace:
  `code/crowd17/report_inbox/processed/battery-frames-80-89-indep.md`.
- **N74 — ne-30-1700 NULL (fenced)**: @1700 FENCED — neither
  30="pas" nor 30="importe" yields a clean clause-level parse
  under standing values. "pas" is excluded by word order;
  "importe" survives only as a well-formed word ("n'importe",
  elision-licensed, stream-unique 94-30 adjacency) awaiting 85's
  value and the 33 tiebreak. Fencing is the bar's instructed
  outcome, not a failure to test. Trace:
  `code/crowd17/report_inbox/processed/battery-ne-30-1700.md`.
- **N75 — split-92-adjudication + split-92-redteam-evidence NULL**
  (evidence-package null, per bars): the bar is
  red-team-adjudication-only — split vs second polyvalence
  declaration vs governor misread is undecidable at battery level
  under §7 (67 sole true polyvalence). The tripartite governor
  profile is real on the repaired stream and independently
  verified. The re-derivation did not fail — it succeeded with ONE
  package correction (follower scatter: five 2× pairs, not one),
  carried to red-team adjudication. Traces:
  `code/crowd17/report_inbox/processed/battery-split-92-adjudication.md`,
  `code/crowd17/report_inbox/processed/battery-split-92-redteam-evidence.md`.
- **N76 — prof-53 NULL** (no single parse covers all 11 of 53's
  windows): the queue gloss's "donne" alternative is real at
  @168/@708 ("on donne 21", "35 donne 71" both clean) but 53-12-41
  (@57) and 53-12-44 (@1581) break it as a single parse — 41/44
  are word-valued (n=19/n=15), not word-final letters, so the
  53-12 contact cannot be word-internal "n" everywhere. For the
  2/5 'ne' windows: @169/@709 stay disputed; the 3 undisputed
  'ne' windows (@809/@1075/@1736) are unaffected (ne-le-1075 "98 ne
  le 77" does not touch 53). The negation-'ne' census via 12-48 is
  3 clean + 2 disputed. Worker corrections (no verdict
  contradicted): queue gloss @-offsets were off by one (53 at
  @168/@708, the 12s at @169/@709, 53-12-41 at @57-59, 53-12-44
  at @1581-83); the n-e-12-48 battery's "'ne'=12-48 ×7" gloss
  re-derives as ×5 on the repaired stream (its promotion rests on
  GT-anchored legs, not the count — noted for downstream
  citations). Follow-ups queued: donne-168-708-leg (2-window leg
  battery; bar: "on donne 21" @168 and "35 donne 71" @708 parse
  with 21/71 named; 53-12-41/44 explicitly fenced out), donn-41-44
  (name 41/44 with ≥2 frame-legs each; if either resolves as a
  vowel-letter or inflectional ending, re-open prof-53 under
  53="don"-stem), ne-census-1248 (re-derive the 12-48 census as ×5
  and restate negation-'ne' as 3 clean + 2 disputed; correct
  downstream citations of the ×7 gloss). No standing red-team
  verdict on 53 exists; nothing contradicted, nothing overwritten.
  Trace: `code/crowd17/report_inbox/processed/battery-prof-53.md`.

### Round-17 null batch, wave 6 (crowd17, 2026-10-08 UTC)

- **N77 — s5-foundation-r2 NULL (ESCALATION, kill-grade evidence)**
  (five clean windows @51/@1655/@529/@1357/@1444 all ungrammatical
  under 37='le' — @51 "tout le la tout" article-article, @1655 "le
  la", @529/@1357/@1444 "le qui" determiner+relative-pronoun — on
  banked/promoted anchors only, all five clauses PASS at kill grade):
  the result CONFIRMS the contradiction found by s5-foundation and
  contradicts the standing S5 fence (37='le' MEDIUM, round-7). Per
  §5 this battery gathers evidence only — it does not downgrade S5,
  does not promote any value; the S5 downgrade decision belongs to the
  red team. Trace: `code/crowd17/report_inbox/processed/battery-s5-foundation-r2.md`.
- **N78 — ver78-296-reparse NULL (fenced)** (the 1-window residual
  stands): @296 '11 78 40 97 86' does not re-parse as one French word
  under 78='ver' — 97 has no battery-derived value or frame (no 97
  battery exists), 86's value battery (stem-86) is still queued, and
  the lexical sweep exhausts completions ("lavèrent" needs 97='n'
  86='t'; "véreux" needs 97+86="use"/"ux" — all force 97/86 values
  their own contact profiles reject). @296 stays the red-team-fenced
  1-window residual (R16-005); the 'l'ere' rival stands undisplaced.
  No standing verdict contradicted, nothing downgraded. Follow-ups:
  frame-97-profile (p2), ver78-296-97gate (p3), lere-296-rival (p3).
  Trace: `code/crowd17/report_inbox/processed/battery-ver78-296-reparse.md`.
- **N79 — x-33-laisser-test NULL (gated; lead recorded)** (16 and 85
  must resolve as infinitives in the stem frames, zero contradiction):
  NOT MET — both gates are still queued (frame-82-16, stem-85) and both
  carry affirmative contradictions (`62-16` x4 + `12-16` x3
  finite-verb-shaped vs `16-00` x4 noun-shaped under the §7
  sole-polyvalence law; `79-85` x2 noun-shaped under promoted
  79="tout"). Fallback fallback-recorded: X = the causative -er family
  — 'laisser' at LEAD strength, gated on 16/85 — forced by @1477's
  "veut [X]er me [V/N]" frame (82="m" banked; clitic "me" cannot
  follow a non-causative infinitive); prononcer fenced dead at the
  V+me+order frame. Not a kill: no window forces the stem reading
  false. Follow-ups: laisser-gate-16, laisser-gate-85,
  gate-satisfiability-16-85 (the kill-if-banked-forced-non-infinitive
  gate). Trace: `code/crowd17/report_inbox/processed/battery-x-33-laisser-test.md`.
- **N80 — dict-frame-78-45-13-55-61 NULL** (13-55-61 unnameable as one
  French unit): clause 1 FAIL — the three contact profiles are scattered
  (13->24 x3, 55->81 x6 noun-context vs 55->61 x3, 61 scattered n=18) and
  no candidate word survives cross-window triangulation; W1's "ne
  mentent" (3pl, R17-007) is subjectless ("ce verdict" is singular) and
  W2's right context is "ne ce" (94-87 stream-unique bigram, 1/1847 —
  ungrammatical under 94='ne' STRONG LEAD + 87='ce' granted). Not
  kill-grade: the claim is conditional on unsettled leads (78='ver' LEAD,
  45='dict' lead) — an unfired conditional is null, not kill (per the
  fork-78-45-rerun precedent). Clauses 2 and 3 PASS (clause 2 conditional
  on 94='ne' STRONG LEAD; clause 3 fenced — 67='et' by the §7 positional
  rule, blocker is 21's open value). No standing verdict contradicted;
  the 5-gram 78-45 one-word boundary stands promoted (F108); the
  dict-contact boundary (F106) is cited, not re-run. The W2 "94 87"
  hapax is flagged as a 94-frame anomaly for red-team awareness.
  Follow-ups: name-13-55-61 (p2), ne-ce-1169 (p2), w1-573-subject (p3).
  Trace: `code/crowd17/report_inbox/processed/battery-dict-frame-78-45-13-55-61.md`.
- **N81 — lever-77-78 NULL (composition-only scope)**: '77 78' = "lever"
  (infinitive; '48 77 78' = "elever") not promoted, not killed — clause 1
  soft-FAIL: 6/7 windows parse with stated fences (@7, @647, @1077 via
  the 12-48 letter re-parse "n'elever qui", @1180/@1351 via stated clause
  boundaries, @1542 "88 lever [43] pour que prenne" the firmest leg);
  @213 fails (follower 06 is verb-stem-class/non-nominal per F52-L2;
  ISLET-10 reads 06-59 as the "V-este" verb unit — strain shared with
  the F2 rival, non-discriminating, fenced to queued 06 work). Clauses 2
  and 3 soft-PASS (F25 conditioned-94 "en" unavailable at both — pre=78,
  suc=82, consistent with the red-team's denial of the 94="en"
  co-value). Clause 4 PASS WITH CORRECTION: adjacency holds 7/7, but the
  "never splits" control gloss is wrong — one non-adjacent 77…78
  co-occurrence exists ("77 86 78" @877-879, 43/44); it is not a lever
  window and does not contradict the composition. ANOMALY corrected: the
  ne-le-1075 note's "94 never co-occurs with 77 within distance 3" is
  true at the @1075 locus but false stream-wide (94 within d3 of 77 at
  @507-509, @1180-1182, @1351-1353); the locus conclusion is unaffected.
  The "…levement"/nement-host rival at @1180/@1351 stays undemonstrated
  (no pre-syllable value). 77="le" stays provisional under either
  reading; no value promoted or killed. Follow-ups: lever-213-complement
  (p2), lever-88-governor (p2), lever-lement-rival (p3).
  Trace: `code/crowd17/report_inbox/processed/battery-lever-77-78.md`.
- **N82 — fence-911-de NULL (kill-grade failure of UNCONDITIONED
  83='de', escalated; no battery-level kill — lead shared with
  le83-window)** (@910-912 '64 83 59' = "qui de est" under 64='qui'
  granted, 59='est' provisional — ungrammatical; trigram unique
  stream-wide): no grammatical parse covers the trigram with <=1
  non-granted assumption — the "59 not 'est'" fence contradicts the
  local 59->37 A1 frame, and the clause-boundary fence leaves a
  stranded "de" (French has no preposition stranding). @911 forces
  unconditioned 83='de' false conditional on 64='qui' and locally
  coherent 59='est'. 15-window 83 profile: 5/15 hostile to
  unconditioned 'de' (@911 kill-grade; @1217 "le de"; @614/@1171 "ce
  de" x2 → queued frame-87-83-cede 'cède'-verb rival; @1334 "39-83-86"
  "a de [INF]" new cell; @1829 "38-83-24" "de"+finite-verb new cell),
  the rest de-compatible. Escalated to the red team; 83='de' NOT
  killed at battery level (shared lead). Trace:
  `code/crowd17/report_inbox/processed/battery-fence-911-de.md`.
- **N83 — lever-88-governor NULL (soft-pass 3/3, composition-gated)**:
  88 (n=23, 88-77 x3 @86/@646/@1541; 88-77-78 x2 @646/@1541 —
  full stream census) shows verb-frame contact at all three 88-77
  windows under BOTH the one-word ("88 lever") and two-word ("88 le"+
  78) readings, but each contact is weak (77 takes 15 predecessor
  types; @86's 06-88 relation open). @1541 re-parses as "88 lever
  [43-obj] pour que prenne [92]" — 43 nominal via "43 pour" x3 and
  "par 43" x2; "pour que" (00='pour' granted, 46='que' GT); "prenne" =
  70-12-94 ("pre"+"n"+"ne"); 92 fenced as postposed-subject candidate.
  88's class consistent across @646/@1541. NOT promoted: 88's value
  open (F1 owns it; 88-40 @334 "88 40 03" possibly word-internal),
  and the whole claim rides on the parent lever-77-78 null. Gated
  follow-ups: governor-88-value (p2), governor-88-rerun after the
  lever-213-complement / lever-lement-rival settle (p2),
  finiteness-88-86 (p3). Trace:
  `code/crowd17/report_inbox/processed/battery-lever-88-governor.md`.
- **N84 — lon-29-146 NULL (fenced, residual R3)**: @146 '84 29' is
  unique stream-wide (84->29 x1 of n(84)=25; all other 84 successors
  'on'-compatible). No placement of 29='er' (banked) covers
  '64 77 84 29 87 64' ("qui l'on [29] ce qui") — left-attach gives
  "oner" (no French word), word-initial "er"+"ce" unattested, as a
  standalone word 'er' is not French, "erre" gives two subjects and
  no verb, and word-internal "erce" re-litigates granted 87='ce'. The
  29-87 junction matches the attested "[stem]er | ce" pattern — the
  failure is strictly the 84 left context. The promoted
  frame-qui-77-84 stands untouched on its 77-independent legs (sister
  windows @1445/@1801 re-derived "qui l'on est [35/36]"). @146 joins
  A15-C3's fenced R1 (@1619) and R2 (@1664) as residual R3. Trace:
  `code/crowd17/report_inbox/processed/battery-lon-29-146.md`.
- **N85 — stem-42-verb NULL (2/5 windows, bar needs >=3)** (claim: 42
  takes 'ent' as a verb stem; 06='ent' battery-promoted pending
  ratification): W1 @206 PASS ("[42]ent le [44]" transitive verb +
  "le"+noun object; left junction fenced), W3 @544 PASS ("[42]ent pour
  que" — strongest verb-class contact; noun rival rejected — no
  determiner precedes 42), W2 @267 FAIL/fenced (33's
  dire/infinitive contact forces a non-verb 42-06 unit), W4 @1188
  FAIL/fenced (is the second A1 "est [42]" grant window — grant left
  intact per bar clause 2), W5 @1815 dissolved by the "enter"-junction
  rival ("[42]enter" = "entrer"-shaped, single-r; clause-boundary
  alternative escalated — only the red team can declare a second
  polyvalence). Not kill: W3 is a genuine verb leg. A1 value-vs-frame
  tension escalated to the red team. Adverses: 42->94 x3 nominal
  contact recorded (below kill grade). Follow-ups: subj-42-w3 (p2),
  val-42-nominal (p2), w5-enter-junction (p3). Trace:
  `code/crowd17/report_inbox/processed/battery-stem-42-verb.md`.
- **N86 — val-89-mirror NULL (mirror selects NOUN over infinitive;
  class not decided)**: 89 n=14, re-derived. Under noun-89 all three
  mirror windows parse (@273 "veut [X]er [89-noun], on…"; @1375 "pour
  [86]-er [89-noun], on…" — re-derives the frames-80-89-indep HARD
  finding: 89 cannot be a verb after "pour [inf]"; @1391 "veut
  [86]-er [89-noun] [16]…" consistent but incomplete — 16's class
  open, adverse unanswered). Infinitive-89 is kill-grade dead at @1375
  ("pour [inf] [inf]" ungrammatical; 86 INF-class, no
  causative/perception evidence). 89's wider census: 11/14 windows
  clean under noun; the 3 non-noun windows are exactly the 24-modal
  infinitive-slot legs (@221/@986/@1498) — the known class conflict,
  already escalated by frames-80-89-indep (implicates the §7
  67-sole-polyvalence law; battery level barred from declaring
  polyvalence). Promote would overclaim; kill of the bar unsupported.
  Follow-ups: class-89-adjudicate (red team), tail-89-16 (after
  frame-82-16), laisser-89-impact (feed to the X thread — the
  causative-strengthening conditional did NOT fire; X='laisser' stays
  conditional on 16/85). Trace:
  `code/crowd17/report_inbox/processed/battery-val-89-mirror.md`.

### Round-17 null batch, wave 8 (crowd17, 2026-10-08 UTC)

- **N87 — ci-bound-01 NULL (under-evidenced, not refuted)**: the
  bar "all four ce-context windows parse as 'ceci'" is NOT met.
  @984 (a6_01) passes clean: "ce(45)-ci [24-modal] [89-inf]" =
  "ceci peut [inf] ..." — grammatical, but load-bearing on the A11
  HOLD (45='ce', allophone tier), with the fork-78-45/ver-78 watch
  item flagged (if ver-78 ever promotes, this leg must be re-examined;
  antecedent currently false). @195 is a provisional pass (gated on
  open 21's class). @345 and @1029 FAIL as 'ceci' parses — but both
  are fenced as neighbor-driven residuals (06 bare 'ent' ending,
  load-bearing on ent-06's PROMOTE; 03-infinitive + 80-imperative),
  ungrammatical under EVERY reading, so neither forces "ceci" false
  specifically. By the parent battery's kill standard ("kill iff any
  of the four forces 'ceci' false in full context"), this is not
  kill-grade. Clause 2 PASSES: 01 n=28, valueless in all 24 non-ce
  windows (the A12 unit and the "-cier" syllable lead are sub-token
  and name no value). No standing verdict contradicted (A11 and A12
  relied on, not challenged; ver-78/fork-78-45/dict-45 nulls
  consistent). Follow-ups: ceci-984-195-pair (p2), residual-345-06
  (p3), residual-1029-infinitive (p3). Trace:
  `code/crowd17/report_inbox/processed/battery-ci-bound-01.md`.
- **N88 — de-frame-44-83-21 NULL (escalated to red team)**: the 5-gram
  '44-83-21-67-78' x2 (@1160, @1839) parses cleanly as "[44-nominal]
  de [21-noun] et [ver-word]" — clauses (a)–(c) all pass at window
  level — but promotion is BLOCKED by the wave-7 noun-44 kill under
  the §7 sole-polyvalence law: the kill (conditional on 94='ne'
  battery-promoted + 59='est' provisional) forces 44 into a clitic
  slot at @1714, and asserting whole-word nominal 44 at @1839 would
  need a second value only the red team can declare. This battery did
  not re-litigate the kill and declares no polyvalence. Supporting
  facts: 21 = noun (stated class: 'la [21]' x2, 'de [21]' x3,
  21-67 x8/30, no value named); 67='et' at both windows by the §7
  positional rule (78 not infinitive-shaped); 78 = 'ver'-word lead
  (R16-005, ver-78 null — used conditionally); 83='de' grammatical in
  both windows. NEW adverse recorded for the shared 83='de' lead:
  @1829 '83 24' is stale in the le83-window battery under the
  class-level 24 promote — flagged for de-83-residuals (handled this
  wave, F116). Follow-ups: de-frame-21-class (p2), stem-44-1839 (p2),
  escalate-44-deframe (red team). Trace:
  `code/crowd17/report_inbox/processed/battery-de-frame-44-83-21.md`.
- **N89 — subj-42-w3 NULL (left junction fenced; leg conditional)**:
  the '44-29-48' = feminine-plural '-eres' subject claim does not name
  cleanly. Three blocks: (a) no plural determiner anywhere in
  @505-544 (a bare '-eres' noun as subject is ungrammatical); (b)
  gender tension on the 44 root ('le 44' x2 @208/@1679 vs 'la 44' x1
  @1070 — NOTE: this wave's gender-44 (F118) has since adjudicated 44
  masculine, dissolving the feminine window into word-internal
  "préalable"; a future revisit could re-run the '-eres' hypothesis
  against that ruling); (c) hapax suffixing (29-48 x1 and 44-29 x1
  stream-wide). @544's verb-class leg stays CONDITIONAL (recorded, not
  forced) — the stem-42-verb null verdict stands unweakened. Not a
  kill: no window forces the subject claim false globally, and 44's
  noun class is independently supported ('le 44' x2, '44 pour' x3).
  No standing verdict contradicted (42's value open, A1 frame grant
  untouched). This null's three follow-ups are now resolved: det-pl-544
  (this wave, F117 — confirmed absence), gender-44 (this wave, F118 —
  masculine), subj-42-qui (still queued, p3). Trace:
  `code/crowd17/report_inbox/processed/battery-subj-42-w3.md`.

### Round-17 null batch, wave 9 (crowd17, 2026-10-08 UTC)

- **N90 — frame-43-la-52-37 NULL (protocol §4: clause (a) untestable
  as written)**: 52's contact profile pulls three ways — nominal
  "la 52" x3 vs clitic "ne 52 [80]" x2 vs "52-82" x5 — no single name
  without guessing; 98's open value fences continuation B. Clause (b)
  still narrows independently: {suite, condition, maniere, mesure} →
  {condition, mesure} ("suite pour [inf]" / "maniere pour [inf]" not
  French; condition/mesure spared) — the same pair the noun-43 kill
  leaves standing. Clause (c): both windows read "[verb-ent] la
  [52-37] 43", so 43 is feminine — all four candidates feminine.
  Enlightenment: the brief's named f-qui-par finder report is NOT on
  disk (inbox, processed, and full-lane find all empty) — the 4-gram
  was re-derived from the stream rather than taken on trust.
  Follow-ups: cont98-43-value (p2 — naming 98 decides condition vs
  mesure via continuation B), unit-52-37-name (p2),
  frame-43-pour-census (p3). Caveats: 37's predicative-vs-nominal
  tension (A1 grant) not re-litigated; @1129 "52-37-86" hapax has
  ambiguous segmentation. Trace:
  `code/crowd17/report_inbox/processed/battery-frame-43-la-52-37.md`.
- **N91 — noun26-1560-06-value NULL (06's class on the '30 06'
  windows x4)**: E/D/N parse attempts under standing values only —
  0/4 at battery grade each. 'de' is shape-clean everywhere but
  licensed nowhere (needs an invented ellipsis matrix); 'ne' is
  hard-fenced at @1327 ("pas. Ne [62] ne" = double 'ne',
  ungrammatical) AND would need a second polyvalence (§7 bar); 'ent'
  stays fenced on these windows as already recorded. Enlightenment:
  correction to ent-06's successor census — its "77 x7" mixes one
  reverse bigram (@522 is 77→06); the true forward count is 6;
  n(06)=n(77)=44, ratio exactly 1.0. At @1762 "ne le on" fences 'ne'
  outright while "[93]ent l'on" keeps 'ent' conditionally alive.
  Follow-ups: ellipsis-65-62-60-profile (p — test the 'de' leg via
  right-neighbor profiles), ne-06-polyvalence-question (p — red-team
  packet: does 06 get a second 'ne' value anywhere?),
  spell-pasent-test (p — census 3pl '-ent' clerk single-consonant
  spellings; a zero hardens the windows as genuine residuals).
  Caveats: ent-06's three clean frames ("ne mentent" x2,
  "entreprenne") untouched, not re-tested; @1561-1563 stays an
  unresolved residual. Trace:
  `code/crowd17/report_inbox/processed/battery-noun26-1560-06-value.md`.
- **N92 — noun26-1560-pas NULL (escalated: sits between two standing
  grants in tension)**: boundary 26|30 is forced ('pas' cannot
  right-adjoin to a nominal), but 'pas' gets only a structural role —
  head of the twice-attested "30 06 60" fragment — its constructional
  licensing undecided. This battery sits between R17-011 ("'26 30'=
  [verb] pas", INCLUDING @1560) and R17-020 (positional noun at
  @1560) and may overwrite neither. Enlightenment: the bare-'pas'
  anomaly is NOT @1560-specific — the '26 30 06' trigram at @1250
  (verb branch, no 'ne' within 15) has the same shape; the minimal
  pair is branch-level, not window-level. Nearest upstream 94 to
  @1561 is @1549 (closed "00 46 70 12 94" frame, different clause
  across a row boundary). Follow-ups: noun26-1560-1733-fragment (p —
  parse @1733's "30 06 60 12 48", whose letter foothold "n e" is
  narrower than the bare-pas umbrella), noun26-trigram-minimal-pair
  (p — state the constructional difference between the two trigram
  branches). Caveats: exact unparsable span named for red team —
  @1561-1563 "30 06 60"; 06's value contested de/ne; bare-pas
  licensing owned by queued ne-alone-02-74. Trace:
  `code/crowd17/report_inbox/processed/battery-noun26-1560-pas.md`.
- **N93 — pronoun-44-1714 NULL (clitic residual)**: at @1714
  ('65 94 44 59 30') both rivals parse — "[65] n'en est pas qui…"
  and "[65] ne l'est pas qui…" — undiscriminated at the window;
  globally both fail all six frame instances ('en': "le en [50]"/"le
  en pour"/"ce en est"/"[92] en pour" all ungrammatical; 'l'': "le
  l' [50]"/"ce l'est"/"l' pour" all ungrammatical). The bar's fencing
  arm is unavailable, not unattempted — naming either rival would be
  the forbidden forcing the adverses rule out. 44's promoted
  masculine gender (F118) leans weakly toward 'l'' but excludes
  nothing. Residual recorded: 44 occupies a clitic slot at @1714
  with value ∈ {'en', 'l''} — consistent with the noun-44 kill
  mechanism (no lexical noun can intervene between 'ne' and 'est');
  94='ne' and 30='pas' used, not overturned. Follow-ups:
  clitic-44-65-discriminator (p2 — discriminate 'en' vs 'l'' via
  65's contact profile), clitic-44-census (p3 — classify all 15
  44-windows). Trace:
  `code/crowd17/report_inbox/processed/battery-pronoun-44-1714.md`.
- **N94 — subsample-power-60-68 NULL (own bar: power-artifact arm
  passes; predecessor escalation REFUTED — see the wave-9 meta kill)**:
  10,000 draws of 7 tokens from 60's 17 free tokens: fail-to-reject
  rate 95.29% (robust 95.05–95.71% across 3 seeds) ≫ 80% bar — the
  test has essentially no power at n=7; the p-value distribution is
  near-uniform (5th pct 0.053/0.056) — the signature of a no-power
  test; the successor-side non-rejection is a power artifact, not
  evidence about 68's class. Enlightenment: rejection happens only
  when a draw concentrates a repeated type (exemplar #4972: all four
  60→03 tokens, p_suc=0.0101) — typical draws cannot move the
  needle. Follow-ups: pair-60-68-readjudicate (done — kill),
  singleton-68-predecessors (p2), suc-60-68-standalone (p3 — record
  the power-calibrated successor conclusion). Caveats: draws reuse
  the fixed 17-token pool (descriptive Monte Carlo, not i.i.d.).
  Trace:
  `code/crowd17/report_inbox/processed/battery-subsample-power-60-68.md`.
- **N95 — thirds-60-68-pair NULL (marginal pass — neither promote nor
  kill earned)**: successor p=0.0552, predecessor p=0.0546 — both
  ~0.005 above α=0.05; 3-way homophony rejected on successors
  (p<0.0001); 60-62 pair p<0.0001, 62-68 p=0.0020; shared types:
  predecessors ∅, successors {06} x1/x1; uniformity χ²=4.167 on 17:7
  vs 12:12 (p≈0.041, rejected — blocks promote); 62's exclusion held
  (62→94 x9 vs 60→94 x0 / 68→94 x0; collision-62-84 kill). Failing
  to reject at p≈0.055 is absence of rejection, not demonstration —
  two adverses stand unanswered (marginal p-values +
  uniformity-law violation); no window forces the 2-cell claim
  false, so kill is not earned either. Enlightenment: 68's only
  contact with 21 is formula-bound (21-68 n=1 globally @1788); 60's
  "21-60" is free x3 — yet the only structural fact both cells
  share is the formula's "21-[third]" slot; the data cannot
  distinguish "homophones" from "distinct cells sharing one formula
  slot". Follow-ups: subsample-power-60-68 (done — null),
  frame-share-60-68 (p2), nir-value-60-68 (p3). Caveats: 83='de' is
  lead-level (fencing owned by queued T2/T4 fence-911-de and
  frame-87-83-cede); 98's French head unconfirmed; 68 n=7 is
  intrinsic, not a misread. Trace:
  `code/crowd17/report_inbox/processed/battery-thirds-60-68-pair.md`.

### Round-17 null batch, wave 10 (crowd17, 2026-10-08 UTC)

- **N96 — noun-60 KILL (60 = masculine noun dead)**: see the wave-10
  findings entry — C1/C2 coherence fails on all four bar frames,
  "value unnamed" unanswerable, @1338 'qui 60' and @700 'ne 60'
  force verb slots at kill grade. Offset correction banked: the
  queue's @1675/@691 are 03 positions; 60 sits at @1674/@690.
  Attribution correction banked: 'ce [03]' @1014/@1790 is via 47='ce'
  (granted A4) — '87 03' occurs x0 stream-wide. Trace:
  `code/crowd17/report_inbox/processed/battery-noun-60.md`.
- **N97 — adj-60 KILL (60 = masculine adjective single-value dead)**:
  see the wave-10 findings entry — C1–C3 pass (adjective confirmed
  as the cleaner rival to the killed noun claim on the four bar
  frames), but C4 fails at kill grade: @1338 'qui 60 08' and @700
  'ne 60 12' force 60 verbal under red-team-granted values. Both
  single-value claims for 60 dead; the live result is the bare-60 vs
  ent-60 verbal shape split (N100). Follow-ups: poly-60-redteam (p1
  — queued), adj-frames-995-637 (p2 — queued), participle-60 (p2 —
  queued). Trace:
  `code/crowd17/report_inbox/processed/battery-adj-60.md`.
- **N98 — at21-82-43-29-adjudicate NULL (red-team escalation)**:
  clause (c) of the bar cannot be satisfied at battery level. @21's
  unique 82-43-29 trigram forces 43 word-internal — 'mener'/
  'emmener'-family with 43='en' under the non-negotiable 82='m',
  29='er' (47='ce' fencing the stem) — while @343/@1027 'par [43]'
  forces noun-43 ('par suite' the only grammatical reading). No
  single value covers both windows; declaring a second polyvalence
  or a positional rule for 43 is a red-team act per §7 (67 et/veut
  is the sole true polyvalence) — petition filed with stated cause.
  No standing verdict contradicted (no red-team ruling exists on
  43's value); noun-43 stays queued, not verdict-recorded — the
  adjudication bar for 'par [43]' is not duplicated. Enlightenment:
  the 'par [43]' noun force and the @21 word-internal force come
  from disjoint value sets (granted vs non-negotiable) — the split
  is structural, not a value-choice artifact. Follow-ups:
  vient-98-name (done — F123 promote), ce33-noun-slot (p2 — queued),
  en43-wordinternal-census (p3 — queued). Trace:
  `code/crowd17/report_inbox/processed/battery-at21-82-43-29-adjudicate.md`.
- **N99 — fence-83-1217 NULL (localized residual confirmed, fence
  formalized)**: no grammatical parse of '36 77 83' @1215-1217
  (a7_00) exists with 83 unfixed within ≤1 non-granted assumption —
  naming 36 and placing a clause boundary both fail. 36 census
  n=9 (@388/@421/@740/@1174/@1215/@1313/@1449/@1585/@1834;
  predecessors 00 x3 'pour', 59 x2 'est'-prov, 91/49/85/45 x1;
  successors 74 x2, 62/29/20/77/67/70/69 x1) — no class nameable;
  83 n=15, 12–13/15 de-compatible — 83 stays the designated blocker,
  its 'de' lead not re-litigated. The 77-83 bigram and '36 77' are
  both unique stream-wide. Follow-ups: class-36-profile (queued),
  fence-92-1218 (queued), clause-boundary-precedent (queued). Trace:
  `code/crowd17/report_inbox/processed/battery-fence-83-1217.md`.
- **N100 — verb-60 NULL (bare-60 vs ent-60 shape split)**: the six
  verbal windows (@1338 'qui 60 08', @700 'ne 60 12', @995 '03 60
  67', @1474 '53 60 06', @1563 '06 60 71', @1735 '06 60 12') do not
  cohere under one nameable verbal value (C1/C2 fail — no single
  verb or positional rule covers all six), but the verbal class is
  undefeated (C4 passes: @1338, @700, @995, @1474 force 60 verbal;
  noun and adjective single-value claims both killed). Structural
  result: the bare-60 windows vs the 'ent-60' windows split by
  shape, testable. Follow-ups: verb-60-bare (p2 — queued),
  verb-60-ent (p2 — queued), split-60-verbs (p3 — queued). Trace:
  `code/crowd17/report_inbox/processed/battery-verb-60.md`.
- **N101 — tout-14-rerun NULL (bar unsatisfiable under the landed
  noun-60 kill; 14='le' NOT forced false)**: under the live
  adjective rival, 14='le' (determiner) heads a coherent
  "le [60-adj] [03-N]" NP tail at both frame windows (@1365,
  @1689). '79 14' x2 is frame-exclusive — '79 77', '79 11', '79 47'
  occur x0 stream-wide: 'tout' never precedes another determiner
  outside the '62-94-79-14-60' family. No window forces 14='le'
  false; no cleaner rival demonstrated (clitic tie stays tied). The
  frame-62-94-79 battery kills are used as premises, not
  re-litigated; frame resolution itself stays with queued
  frame-62-94-79-reparse. Follow-ups: le14-adj60-tail (p2 —
  queued), clitic-14-82-breakers (p3 — queued), det14-elsewhere (p3
  — queued). Trace:
  `code/crowd17/report_inbox/processed/battery-tout-14-rerun.md`.
- **N102 — tout-slot-14 NULL (no class nameable)**: C1 fails — the
  'tout [14]' ∥ 'tout [82]' parallelism is underdetermined under
  one stated value; all four breakers fence with stated cause (@84:
  '16 14' — 16 open; @424 '47 14 62 48' RESOLVES under 14='le' via
  the A8-granted 'ce le [verb]' frame with 24=finite verb now
  class-level; @623/@896 '82 14' fenced; @1121 '06 14 06' fenced).
  14='le' was never promoted — no §7 second-polyvalence violation,
  no 77~14 homophony created. Follow-ups: tout-14-rerun (done —
  null), breaker-b4-1121 (queued), verb-14-rival (queued). Trace:
  `code/crowd17/report_inbox/processed/battery-tout-slot-14.md`.
- **N103 — donne-168-708-leg NULL (windows parse; naming unmet)**:
  both leg windows parse cleanly under standing values — 'on donne
  21' @168 (84='on' granted, 12='n'/48='e' promoted; "84 53-12-48"
  = "on donne" compositional) and '35 donne 71' @708 (conditional
  on 35 singular, uncontradicted) — and the 53-12-48 trigram census
  on the repaired stream is exactly 2x (@168, @708): the leg covers
  the full trigram population. But the bar's naming requirement
  fails both clauses: 21 (n=30) is unnamed in every standing
  battery (no candidate ≥2 independent grammatical frame-legs), 71
  (n=7, all singleton successors) unnamed at promote-grade. No
  promote (bar unmet); no kill (no window forces the claim false,
  no cleaner rival on the same frames). prof-53's null verdict
  stands untouched — the leg's 'donne' reading is leg-local, not a
  profile claim; 53-12-41/44 fenced to queued donn-41-44.
  Enlightenment: the naming blocker is data-thinness, not grammar —
  both windows are clean; the bar's named-value requirement is the
  only unmet arm. Follow-ups: name-21-obj (p2), name-71 (p3),
  prof-35 (p3) — PROPOSED, not yet queued (supervisor audit
  pending). Trace:
  `code/crowd17/report_inbox/battery-donne-168-708-leg.md`.
- **N104 — stem-44-nominal NULL (stem/whole split fenced for the red
  team)**: all 15 windows of 44 adjudicated on the repaired stream
  (n(44)=15; all 14 bigram counts re-derived, not copied). 2 force
  stem-level composition — @540 '12 44 29' ("44ere"-shaped: "ere"
  is not a French word; whole-word 44 strands it — FORCED
  stem-level) and @1160 '82 44' ("m[44]": the "m'" elision
  alternative is excluded — 'la 44' @1070 unelided with banked
  11='la' proves consonant-initial under §7's one-form rule) — vs
  13 force whole-word (incl. @527 '47 44': word-internal "ce44"
  would overturn granted 47='ce'; @1070 'la 44': banked 11='la';
  @1714 '65 94 44 59 30' clitic slot, segmentation robust to the
  pending 94/59 ratifications). Neither uniform status meets the
  ≤10% orphan bar (whole-only orphans 2/15 = 13.3%; stem-only
  orphans 13/15 = 86.7% and is unavailable — it overturns granted
  values). This is the A10 (33/86) stem/whole HOLD precedent in
  parallel — a standing split, not a forced answer. The noun-44
  KILL stands untouched (segmentation ≠ noun value; whole-word
  status is not a noun value). Per §7, declaring a second
  polyvalence for 44 is a red-team act — the docket packet is the
  follow-up. Follow-ups: phon-44-elision, stem-44-value,
  poly-44-docket (red-team decision) — PROPOSED, not yet queued
  (supervisor audit pending). Trace:
  `code/crowd17/report_inbox/battery-stem-44-nominal.md`.
- **N105 — noun-89-1377-adjudicate NULL (class conflict confirmed)**:
  no verb-89 parse of @1376 kills the noun/adverb reading — seven
  candidates tested under standing values (finite, infinitive,
  imperative, participle, postposed-subject "V on", "[89]on"
  compounding, re-segmentation); all fail. The sole verb-shaped
  parse (causative-complement infinitive "pour faire [89-inf]")
  needs ungranted 86='faire'-shaped — independently found
  evidenceless by val-89-mirror — and would not kill the
  noun/adverb reading anyway. The infinitive-slot legs @221 and
  @985 re-derive standing, 77-independent (24=modal battery-promote
  takes infinitive complements; the 48-junction at @985 fenced
  rightward under 48='e'). Same cell, two classes — the conflict
  is genuine and confirmed; its resolution belongs to the red team
  under §7's sole-polyvalence law, whose packaging
  (class-89-adjudicate, PROMOTED 2026-10-08 — window table 11/14
  noun-clean + 3 infinitive-slot legs, no class named, no
  polyvalence declared) already exists — this battery's
  confirmation feeds that docket, no new escalation opened. Feed
  for val-89-mirror's clause 3 confirmed already present in its
  docket (adopted via frames-80-89-indep) — bar not duplicated.
  Follow-ups: faire-86-causative-test, adv-89-1376, tail-1376-on92
  — PROPOSED, not yet queued (supervisor audit pending). Trace:
  `code/crowd17/report_inbox/battery-noun-89-1377-adjudicate.md`.

### Round-17 null batch, wave 11 (crowd17, 2026-10-08/09 UTC)

- **N106 — prenne-92-noun KILL (92 as unconditioned feminine noun
  dead)** (battery-prenne-92-noun). The bar's distributional gate
  rejects the claim at the lane's standard; two windows force an
  unconditioned feminine-noun value false at kill grade. No standing
  verdict contradicted: A14's 92 INF-signal grant was set-level
  ("genuinely ambiguous"), untouched; the A6 '-ère' value kill
  untouched (@683 fenced, never re-valued); the 09~92 HOLD untouched;
  prenne-subject-S1545's promote (92 direct-object-shaped as a SLOT
  claim) stands — it was never a value claim. The split/polyvalence
  question stays with the red team (split-92-redteam-evidence is
  verdict-tagged in queue.json) — this kill is the noun VALUE arm
  only, per §7.
- **N107 — prenne-trigger-348 KILL (subjunctive trigger claim false)**
  (battery-prenne-trigger-348). Clause-boundary analysis @300-347
  locates no subjunctive trigger for @347-349 — the window is
  triggerless, with stated cause. No standing verdict contradicted;
  the 12/94 duality stays fenced for the red team (the sibling
  battery-prenne-70-12-94 null's fencing untouched); neither the
  ne-94 nor the n-e-12-48 promote is downgraded (scoped to the
  trigger bar only). Follow-up: prenne-R3-relative-341 (p2 — the
  surviving horn: @347 as the verb of the @341 'qui'-relative,
  subjunctive licensed by the @340 45 antecedent's force — queued).
- **N108 — suite-21-qui-que KILL (21="suite" VALUE dead at bar grade)**
  (battery-suite-21-qui-que). @134 forces the claim ("@134 and @1529
  resolve under 21='suite'") false under standing values; the sole
  structural rescue is the 21-65 unit-verb reading — a §7 red-team
  act, ESCALATED, never decided here (if the red team grants it,
  this kill re-opens). The noun CLASS verdict (F122) is NOT
  downgraded — no window forces the class false; the contradictions
  are value-grade. No cleaner rival value demonstrated here; rival
  testing continues in queued rival-21-feminine; prof-65 (queued,
  still open) decides @1529's conditional "que suite [65-verb]" parse.
- **N109 — adj-frames-995-637 NULL (@637 fenced for the red team)**
  (battery-adj-frames-995-637). C1/C3/C4 pass: the @995
  postnominal-adjective frame holds with independently supported
  03-nominal anchors ('ce [03]' x2 @1014/@1790 via granted 47='ce';
  'le [03]' @722; '03 64' x4; 'pas [03] qui' @30) and zero
  contradictions. C2 fails at battery level: @637's
  coordinated-adjective parse is blocked by standing A8 (89
  verb-framed) and needs a red-team ruling on 89's class/polyvalence.
  Not kill — no window forces the @637 frame false; unpromotable
  now, not refuted. Follow-up: adj-frame-995-solo (p2 — narrow re-bar
  on @995 alone — queued).
- **N110 — dict-45-ce-rival-1165 NULL (double residual recorded)**
  (battery-dict-45-ce-rival-1165). No 'ce' parse within the assumption
  budget; the 78='ver' adverse stays LEAD, unresolved. Not kill: the
  bar's second arm is a record instruction and is discharged by
  recording the double-residual (the determiner-gap finding at reading
  1 is kill-grade within the two-token scope but is recorded as the
  residual, not as a kill of the claim, pending the red-team
  polyvalence decision — per the fork-78-45-adjudication precedent,
  an unfired conditional is null, not kill). A11 HOLD (45='ce')
  untouched; scope fenced to the fork windows. Follow-up:
  vers-78-w4-gate (p2 — re-test W4's 'ce' parse once gates clear —
  queued).
- **N111 — dict-45-w3-ceci NULL (promote blocked three ways)**
  (battery-dict-45-w3-ceci). "ce verdict-ci fait [89]" R1 parses with
  full window coverage — not kill. Promote blocked on three
  independent grounds: (i) the queue's never-downgrade rule —
  promoting 01='-ci' at @984 would downgrade F124's standing
  battery-promote of 01='en' at the same window; (ii) the 78='ver'
  ↔ 45='dict' mutual conditionality means the window adds no
  independent positive leg (it re-counts ver-78-rebar's conditional
  positive); (iii) both adverses fence rather than answer. No
  standing verdict contradicted or downgraded. Follow-up:
  dict-45-circle-break (p2 — independent leg for 45='dict'-syllable
  at post-78 windows where 01 is absent — queued).
- **N112 — dict-78-45-wordbound NULL (boundary holds; value arm
  escalated)** (battery-dict-78-45-wordbound). The boundary holds at
  W2-W4 with W1 fenced as a two-word exception (per F130), but the
  claim cannot promote — the value arm ('verdict') and the positional
  declaration both need red-team action, so this escalates. Naming
  78-45='verdict' would jump ahead of R16-005's LEAD grading of
  78='ver' (ver-78 returned null 2026-10-08; @296 the fenced
  residual) — per §5 this is null-and-escalated, not kill.
  Follow-up: verdict78-gate-wordbound (p1 — re-test this bar once
  ver-78 resolves — queued).
- **N113 — feeder-ceci-47-45 NULL (clause (a) resists with stated
  cause)** (battery-feeder-ceci-47-45). The resistance is downstream
  of the 47-01 bigram (at [21]/[60]) and does not force "ceci" false
  at the bigram — not kill-grade; but the bar's (a) is not met, so
  not a promote-feed either. @984 stands as the one clean
  ceci+modal+infinitive window; @195 cannot serve as a clean
  ceci+verb window while 21 is nominal and 60's slot is open. No
  standing verdict contradicted or downgraded (A4, A11, A8, the
  21-noun promote, the 24-modal promote all used, not re-litigated).
  Follow-ups: ceci-195-nounslot (p3), residual-345-06,
  residual-1029-infinitive — all queued (no duplicates of queued
  ceci-984-195-pair, disc-01-24-ci-X, poly-60-redteam, etc.).
- **N114 — la-523743-adjective NULL (S5 contradiction escalated)**
  (battery-la-523743-adjective). The headline is not the verdict — it
  is the contradiction: the la-finder's adjective vote for 37 parses
  the two vote windows as "[verb-ent] la [52-37] 43" with 52-37 a
  prenominal adjective unit, under which 37="le" reads "la [52] le
  [43]" (double article, ungrammatical) — contradicting the standing
  S5 fence (round-7, 37="le" MEDIUM). New data for the red team:
  "37-11" x2 (@51 "tout 37 la tout", @1655 "[56] 37 la [24]") are
  "le la"-shaped under S5 and were never examined by the le-la
  battery (which dissolved only the three 77-11 co-occurrences). The
  S5 fence is not overturned here — it is escalated to the
  designated venue s5-foundation (verdict-tagged in queue.json, p1).
  The adjective vote itself is recorded as UNANCHORED (2 tokens, 1
  phrase type, LEAD-grade per the la-battery — not killed: no window
  forces adjective-class 37 false). Follow-ups: lela-37-51-1655
  (p2), unit-52-37-name (p2 — both queued).
- **N115 — lon-62-on-conditioned NULL (open question packaged for the
  red team)** (battery-lon-62-on-conditioned). Clause (a) passes
  fully: @508's elision context is unique to 62 (77 x1/35
  predecessors; 62->59 x0; no other vowel-context predecessor).
  Clause (b) is not battery-decidable — conditioned 62='on'
  admissibility is the deferred red-team act from collision-62-84
  (§7: 67 is the sole true polyvalence; this battery declares none).
  No standing verdict contradicted: collision-62-84's unconditioned
  kill stands; lon-ne-77-62-94's null stands beside it.
- **N116 — lon-94-64-rightedge NULL (genuine 1-window residual,
  fenced)** (battery-lon-94-64-rightedge). The 'ne qui' singleton at
  @509-510 is a genuine residual: no clause boundary can intervene
  between the pairs ('ne' dangles on both rival readings and cannot
  open the next clause), and no window-local cause exists for
  64='qui' to fail here. The contact is symmetric (94's sole 'qui' of
  37; 64's sole 'ne' of 47), so the residual localizes to the
  contact itself, not to either value's profile. Per the task brief,
  this is null-grade: the 64='qui' grant is NOT downgraded, the
  94='ne' promotion-track is NOT re-litigated. Fenced with stated
  cause.
- **N117 — name-21-obj NULL ("suite" leads, promote blocked)**
  (battery-name-21-obj). Class resolved (noun, cited promote). Value
  "suite" leads on anchored idiom frames but is blocked at
  promote-grade by two bar-grade contradictions (@134, @1529) in the
  "qui/que + 21 + 65" family. Not kill: no window forces the class
  false, and "suite" beats every rival tested on the anchored frames.
  Relationship to this wave: the battery's own follow-up
  suite-21-qui-que ran and KILLED the "suite" VALUE (N108) — the
  kill stands; this null records the idiom-frame lead as the
  residual shape of the evidence. Downstream: ceci-984-195-pair,
  stem-85-then-1700 unaffected (both queued).
- **N118 — ver78-la78-census NULL (clause (a) fails 5/9 < 7/9)**
  (battery-ver78-la78-census). Not promote. Not kill: no window
  forces 78 as noun-head false at kill grade (the three failures are
  soft — unparsed, not contradicted), and no cleaner rival value was
  demonstrated on these frames (lever-77-78 is NULL, not
  demonstrated). The 16/31 determiner-headed noun distribution for 78
  stands unrebutted. R16-005's 78='ver' LEAD untouched; the ne-le-1075
  kill respected; §7 unviolated. Follow-up: ver78-rerun-214-1543
  (p2 — re-parse @214 and @1543 once 06's class and 43's value
  resolve — queued).
- **N119 — w1-314-ambig NULL (the bar's consequence mapping was
  inverted)** (battery-w1-314-ambig). Headline: the modal-24 evidence
  inverts the bar's consequence mapping — W1 decides for CE, but the
  bar as written would have said dict. The data conclusively
  establishes: 37-78 word-internal as the infinitive complement of
  promoted modal-24; the infinitive complete at 78 (@475 control:
  identical left context strands 78 before 74); the forced boundary
  before 45 makes 45@314 word-initial 'ce' (A11 HOLD, mirror leg
  45-64 intact); every dict parse of W1 ungrammatical. CE wins W1;
  the "verdict" reading is excluded at W1. Scope: W1 and the
  84-24-37 family only — W2/W3/W4 have different left contexts and
  are untouched. Not a promote here (the promote is F130,
  w1-314-rebar, which was this battery's own proposed p1 follow-up
  and already ran). Nulls never duplicate: this battery's follow-up
  list is discharged by the rebar's verdict.

### Round-17 null batch, wave-11 mid-sweep arrivals (7 battery notes landed
during this sweep)

- **N120 — prenne-R3-relative-341 KILL (the surviving horn killed)**
  (battery-prenne-R3-relative-341). The trigger-less @347-349
  window's last surviving reading — @347 as the verb of the @341
  'qui'-relative — is killed at bar grade. Load-bearing on
  noun-43-discriminator's kill of 43="suite" (battery verdict
  2026-10-08, unratified): if "suite" ever revives, clause 2's "par
  suite" parse revives with it and this target re-opens (dependency
  noted, not a new target). Secondary load: ci-01-value's kill. No
  new follow-ups — the kill is decisive on both clauses; the only
  regeneration path is the stated dependency.
- **N121 — dict-45-circle-break NULL (independence nowhere
  available)** (battery-dict-45-circle-break; the follow-up N111
  proposed, now run). The claim needed an independent leg for
  45='dict'-syllable at post-78 windows where 01 is absent
  (@313/@573/@1165). Headline: the independence is nowhere
  available — all three windows' dict readings run through the
  unsettled 78='ver' LEAD, extending the w3-ceci circularity finding
  to W1/W2/W4. The bar's resolve condition is unsatisfied (clause 3
  fails at battery level; clauses 1-2 conditional on unsettled
  leads); the kill condition is not met either. Follow-up:
  dict-313-w1-adjudicate (p2 — queued).
- **N122 — importe-30-elision-test NULL ('importe' neither killed nor
  advanced)** (battery-importe-30-elision-test). No window forces
  consonant-initial 30 (kill clause fails); no second "n'importe"
  frame exists (promote-consideration fails). The rival stands exactly
  where ne-30-1700 left it: conditional word-formation at @1702
  ("n'importe", stream-unique 94-30 adjacency, elision-licensed),
  with no clause-level parse under standing values. Follow-up:
  wordbound-30-06-importent ("30-06" x4
  @1251/@1327/@1561/@1733 — queued).
- **N123 — lon-on-elision-control NULL (discriminator recorded, case
  weakened, not killed)** (battery-lon-on-elision-control). Clause 2
  passes (elision mechanism identical under the 77='le' provisional
  hold); clause 1 fails at weakening grade: granted 'on' legs show
  zero 'ne'-followers (0/25 — the 7 "l'on"-leg followers are 09 x2,
  59 x2, 29, 74, 24), while @508 under the conditioned reading is
  'on'+'ne'. Fisher one-sided p=0.038 does not reach the lane's
  rejection standard, so this is not kill-grade; no window forces the
  conditioned-'on' reading false, and the single-observation @508
  side structurally cannot promote.

### Round-17 null batch, wave 12 (crowd17, 2026-10-08/09 UTC)

17 kills, 65 nulls. Kill grade = a window forces the claim false.
All notes trace to `code/crowd17/report_inbox/` (file names below).

- **N124 — ce-inf-1841 KILL: "ce + infinitive" nominalization is
  ungrammatical in 1841 French** (battery-ce-inf-1841). Period corpus
  (Littré 1872–1877, period grammars) positively establishes "le" as the
  substantivizer; @23-24 and @1232 cannot parse under "ce + infinitive".
- **N125 — dite-52-37-anaphora KILL: "dite" (=ladite) eliminated from the
  Type-A 52-37 adjective set** (battery-dite-52-37-anaphora). No antecedent
  at @1124/@1722. Caveat: bar scoped to the named rows — a
  whole-discourse scope would NOT eliminate "dite".
- **N126 — edge-1024-clause-boundary KILL** (battery-edge-1024-clause-boundary).
  Boundary between @1023 "qui" and @1024 "ce" killed — strands a verb-less
  relative "qui".
- **N127 — ellipsis-760 KILL (partial): the uniform clause-initial-particle
  account of 20 is killed @1703** (battery-ellipsis-760). "ne pas" requires
  a verbal complement. The W1-local ellipsis reading @760 survives.
- **N128 — le-14-kill-1121 KILL: 14="le" as a window-independent value**
  (battery-le-14-kill-1121). Kill-grade at the @1121 breaker window; 14
  fully open ("le", "sou", "souv" all dead at window level).
- **N129 — lever-213-complement KILL** (battery-lever-213-complement). "@213
  '74 lever 06' resolves the 06-complement problem" killed — the window
  forces the conditional claim false.
- **N130 — lex-passepartout-48 KILL: "passe-partout" reading of @44–48**
  (battery-lex-passepartout-48). Needs @48="tout", but @48=00="pour"
  (granted).
- **N131 — mannequin-62-98-test KILL: joint 62="man"/98="n"**
  (battery-mannequin-62-98-test). 62-48 ×6 reads "mane" — not a French
  word ("crinière" is); 98-83 ×5 strands a bare "n".
- **N132 — name-88-value KILL: one value for 88 across its 23 windows**
  (battery-name-88-value). No single value covers all 23.
- **N133 — ne-317-wide-parse KILL** (battery-ne-317-wide-parse). No
  grammatical parse of @314–325 under standing values with ≤1 new-value
  assumption; the "verdict qui" rival also dead.
- **N134 — nece-94-87-initial KILL: the word-initial "néce-" rescue**
  (battery-nece-94-87-initial). @1169–1172 forces it false. Does NOT
  disturb 94="ne" STRONG LEAD (R17-001) or the 87="ce" grant.
- **N135 — prennent-70-12-06 KILL (stated parse only)**
  (battery-prennent-70-12-06). The "'11 88 70 12 06' as plural NP +
  'prennent' with subject agreement" reading killed @1116–1120; the
  souvent clause itself is not killed, only this subject-agreement
  reading.
- **N136 — prennent-88-subject KILL: the plural-pronoun arm for 88**
  (battery-prennent-88-subject). Banked 79="tout" at @496 cannot precede
  a plural pronoun.
- **N137 — souv-14-06-repair KILL** (battery-souv-14-06-repair). 14="souv"
  gives exact "souvent" at both windows but is distributionally
  untenable (@586) — the spelling repair works, the value dies.
- **N138 — souvent-14-06-retest KILL: 14="sou"** (battery-souvent-14-06-retest).
  Killed at @84 ("souent" ≠ "souvent" under standing 06="ent").
- **N139 — stem48-legs-rival KILL: the rival letter-"e" claim @1229/@1589**
  (battery-stem48-legs-rival). Eliminated at kill grade — the stem
  requirement stands.
- **N140 — val-61-contact KILL: any global 61 value**
  (battery-val-61-contact). No single French value covers the four
  discriminating 61 frames. Coexists with F135's locus-level
  "première fois" @1556 — locus promote and global kill, no downgrade
  either way.

Nulls (65, grouped by family):

- **62 family** (7: 62-third-leg, class-62-25, class-62-fullcensus,
  class-62-nof94, frame-20-62-94, seg-30-62-96, seg-a1_01-offset1-test):
  no third noun frame-leg — class stays open (2 legs < the lane's ≥3
  standard); no single class over the 25 non-94 windows; "il" dead at
  kill grade across the full 35-window census; the conditioned split is
  the live hypothesis but needs red-team approval (§7 sole-polyvalence
  law); @46 fenced as segmentation-open; "96 00" ungrammatical ×3
  (@47/@465/@960) routed to seg-par-pour-96-00.
- **Determiner/adjective block** (13: det-20-value, det-20-307-fenced,
  noun-20-value, det-80-1156-corrob, det-adj-80-adjudicate,
  le-86-determiner-subset, homophone-79-split, homophone-86-split,
  s5-la-tout-adjudicate, s5-rival-five-windows,
  s5-verb-rival-four-windows, adj-frames-995-637,
  adj-groundwork-refollower): no feminine-noun value for 20; the
  determiner/adjective paradox is confirmed structural; 86="voi" (voir
  stem) fails globally; the 37-"le" MEDIUM (S5 fence) contradicts the
  adjective vote and is escalated to red team (s5-foundation, P1) with
  new "37-11" ×2 @51/@1655 "le la"-shaped data; 91 (n=21) shows exactly
  one adjective-shaped window (@723) — no adjective value nameable.
- **ceci/dictionary block** (6: ce33-noun-slot, ceci-984-195-pair,
  feeder-ceci-47-45, dict-45-ce-rival-1165, dict-independence-census,
  dict-78-45-wordbound): restricted "-ci bound, 2 loci" reading not
  both-parsed; the 45/78 ceci line stays open.
- **ne family** (6: ne-ce-1169, ne-508-reseg, qui-94-syllabic-rival,
  finite-88-ne, verb-gap-ne-508, seg-94-82-06): "ne ce" @1169 unresolved
  (rescue-2 killed); @508 fenced to the red-team 12/94 duality; "ne qui"
  @509–510 fenced as a singleton; verb gap @505–525 confirmed as a
  second window residual; no uniform left-edge for "94/18 82 06" —
  frame D parses "ne ment pas" cleanly but needs 2+ assumptions.
  seg-94-82-06-f2: 18's distribution (n=7) too thin for
  slot-equivalence in either direction; word-edge-after-X not advanced.
- **vient block** (3: cont98-43-value, vient-65-complement,
  vient-98-511-relative): naming 98 does not decide condition vs mesure;
  98-65 fenced; @510–517 inconclusive for the battery-promoted
  98="vient" (unratified).
- **60 block** (5: participle-60, poly-66-split, verb-60-bare,
  verb-60-ent, npframe-60-454): single-class rescue fails; 66 split NULL
  by authority (§7), not evidence; V1/V3/V4 cohere under the -dre family
  but no verb is nameable.
- **segmentation block** (7: seg-55-61-94-word, seg-61-94-word,
  seg-55-re-prefix, par-pour-962-adjudicate, wordbound-30-06-importent,
  breaker-b4-1121, reseg-700-verbal): "30 06" boundary not independently
  decided; 55="re" prefix NULL (81="prin" kill intact); @1121 breaker
  resolved window-locally only (clause 2 rested on 14="sou", since
  killed — do not cite as a leg).
- **value/name block** (rest, incl. name-13-55-61, name-55-61-core,
  name-21-obj, rival-21-feminine, rival-porter-envoyer,
  unit-13-55-61-contact, unit-52-37-name, adj-52-37-value,
  val-33-verb, w1-314-ambig, verdict78-gate-wordbound, fence-92-1218,
  ellipsis-65-62-60-profile, ent-er-residual, ce-le-verb-frame,
  importe-30-subject-sweep): name-55-61-core NULL — the 13/43 slot values
  cannot be stated under §7, so no French word X is nameable over the
  55-61 bigram; 52-37 split candidacy to red team (Type-A adjectival
  firm but window-local; adj tie {même, seule} unbroken after "dite"
  died — N125); rival-porter-envoyer escalated for red-team promotion
  ratification; 62="on" conditioned-elision package complete and open;
  preverbal ce+le stack fenced as a 77-value residual.

### Round-17 null batch, wave 13 (crowd17, 2026-10-09 UTC)

17 kills, 47 nulls. Kill grade = a window forces the claim false.
All notes trace to `code/crowd17/report_inbox/` (75 new files) and
`code/crowd17/report_inbox/processed/` (25 files whose verdicts were
never folded before this sweep).

- **N141 — ant-58-ending KILL: 58="ant" (present-participle ending) is
  dead at kill grade** (battery-ant-58-ending). @1203 forces 58
  non-verbal: 45="ce" (A11 HOLD, R18-strengthened; "dict" excluded by
  F169's sole-host certification) + 47="ce" (A4) makes "ceant" a
  non-word. The promote side reached 2/3 legs (@1696/@1757 gerund
  windows) — the "en [85] [58]" segmentation survives; only the "ending"
  rival dies.
- **N142 — class-55-det KILL: 55 as determiner** (battery-class-55-det).
  W3 (@1205) forces 55 word-internal under the standing promoted
  "prend(55-61)" discriminator (F155); §7 bars a separate-at-11/
  word-internal-at-1 split at battery level. Clause 1 also failed (1
  clean pre-noun slot of the required ≥2).
- **N143 — donc-28-triangulate KILL: 28="donc"**
  (battery-donc-28-triangulate, processed). @698 forces it false under
  the A11 HOLD ("ce donc ne" ungrammatical). Informative in defeat:
  "donc" was 5/6 clean across the 28 census.
- **N144 — frame-qui-47 KILL: 76 verb-hood** (battery-frame-qui-47,
  processed). Verb-hood is kill-grade dead against the standing battery
  verdict; the verdict states it on 76.
- **N145 — frame-vient-parvenir KILL: the 3-cell homophone set (60/62/68
  = one plaintext, "nir")** (battery-frame-vient-parvenir). Permutation
  test rejects successor homogeneity at p=0.0002; frequency split
  (35/18/8) violates uniformity. Narrow kill — the set dies, not the
  frame: the "98 83 82 96 21" formula and conditioned 83="de" in the
  "vient de" environment stand.
- **N146 — homophone-12-30 KILL: the 12~30 merge** (battery-homophone-
  12-30). Predecessor/successor distributions distinguishable (p=0.0124 /
  p=0.0002) under the {33,86} standard; the claim independently
  contradicts standing adjudications 12="n" (letter-tier) and 30="pas"
  (R17-011).
- **N147 — pasent-subject-26-56 KILL: the "passent" word-reading of
  30-06** (battery-pasent-subject-26-56). The 3pl-subject hypothesis for
  26/56 is killed; per the pre-registered bar the "passent" reading dies
  grammatically at @1251/@1327/@1561/@1733. What survives: the letter
  strings "pas"+"ent" only.
- **N148 — pronoun-13-les KILL: 13="les" object pronoun**
  (battery-pronoun-13-les). @567 ("97 les [76-noun]") forces it false —
  76 is a battery-promoted noun that cannot host a preverbal clitic, and
  every re-segmentation fails. Both French "les" arms now dead
  (determiner arm: N152).
- **N149 — seg-61-pren-polyvalence KILL: 61="pren" as a global value**
  (battery-seg-61-pren-polyvalence, processed). Two independent windows
  (@1556, @367) force it false with banked neighbors; the 61="pren"/
  70="pre" tension resolves against 61 (70="pre" pencil stands). A
  frame-restricted rescue would be polyvalence, barred by §7. Coexists
  with F135's locus-level "première fois" @1556.
- **N150 — sel-62-48-94 KILL: the 62 selector claim**
  (battery-sel-62-48-94). False on two grounds: no 62 value makes 62-48
  and 62-94 one morpheme (candidate space exhausted), and the bar's
  explicit kill-grade fires — @348 forces 94 syllabic, breaking the
  particle-only selector.
- **N151 — slot-13-43-compare KILL: the claim that 13 and 43 share a
  slot** (battery-slot-13-43-compare). Successor overlap does not exceed
  chance (p=0.18); predecessor environments fully disjoint. No window
  forces it false, but the bar's stated distributional test rejects the
  same-slot reading at the lane's standard.
- **N152 — subj-13-value KILL: the plural-determiner hypothesis for 13**
  (battery-subj-13-value). Five windows (13->24 x3, 13->93 x2) force a
  determiner before a promoted finite-verb class — categorically
  ungrammatical. Kill is class-level (any plural determiner). W1's "ne
  mentent" subject is not found.
- **N153 — subj-55-61-word KILL: the plural-noun value for the 55-61
  word** (battery-subj-55-61-word). W3 (@1205–1206) forces 55-61
  verb-shaped; §7 bars a noun-at-W1/verb-at-W3 split at battery level. A
  cleaner rival stands on the same frame ("prend" + noun object, F155).
  CONFIRMS F155 and NARROWS w1-573-subject's null (W1's 3pl-subject slot
  stays open; the 55-61-word route to it is closed).
- **N154 — value-13-third-arm KILL: no uniform word-level non-"les" value
  exists for 13** (battery-value-13-third-arm). With both "les" arms dead
  (N148, N152), the uniform-value question for 13 is closed; the
  surviving space is sub-lexical 13 or a §7 split — red-team territory.
- **N155 — dit-60-syncretic KILL: 60="dit"** (battery-dit-60-syncretic,
  processed). Forced false at @690 ("ne er dit" ungrammatical under every
  available segmentation, banked 29="er" immovable) — the irony is clean:
  "dit" was the unique value parsing both founding windows (@454 "ledit
  [65]", @1338 "qui dit"). Does not disturb the 60 polyvalence question
  (poly-60-redteam).
- **N156 — ne-alone-02-74 KILL: 02 and 74 as the negated verbs in "42 ne
  02" / "42 ne 74"** (battery-ne-alone-02-74, processed). 51 windows of
  02+74 with zero verb-frame contact in the bar's stated test set.
  94="ne" keeps its R17-001 STRONG LEAD; the A1 predicative grant on 42
  holds.
- **N157 — stem-68-id KILL (of the naming claim): 68 as verb stem**
  (battery-stem-68-id, processed). Contact profile does not match a verb
  stem: 0/8 windows require a verb; @1442 "[68] est" and @884 "tout
  [68]" are anti-verb, one forcing. Verb-stem status fenced out; class
  stays open. Battery-grade narrowing of ent-06's supporting leg: the 68
  leg of its la-frame argument is void (06="ent" promote itself
  untouched).

**Kills (2026-10-09 wave-5):**

- **N158 — contre-00-global-census KILL (of the global 00="contre"
  promote)** (battery-contre-00-global-census). Full 55-window
  census under 00="contre": all four "contre que" windows are hard
  contradictions under banked 46="que" (a fifth battery-grade
  contradiction at @1138, "vient contre vient"); "contre" never
  introduces a "que" clause in 1841 diplomatic French. The claim
  fences to the "96 00" positional reading at the three positional
  windows (@48, @466, @961) — packaged for the red team (par/pour
  anomaly docket), NOT promoted (§7). The A9 00="pour" class-level
  grant is untouched.
- **N159 — rival-37-01-certain KILL** (battery-rival-37-01-certain).
  The local word "certain" (37="cer", 01="tain") fails at kill grade
  at all three 37-01 windows (@940, @1634, @1818) — no grammatical
  integration with a stated consequence. 'tain' is dead everywhere,
  not local; the live reading is 01="fait" in a "faire"-compound
  (F225). Correction: the lane's prior brief wording "'tain' local
  to 37-01" was stale and is superseded by this kill.
- **N160 — faisant-absolute-01 KILL** (battery-faisant-absolute-01).
  The absolute "ce faisant" reading of 01 is killed at battery
  grade: all four ce-windows force it false (recoverable subject
  but ungoverned subjunctive @345; infinitive "[03]er" blocks any
  finite main clause @1029; adjective-grade 60 blocks any finite
  main clause @195; no recoverable subject for finite 24 @984).
  Covers only the ABSOLUTE frame shape; word-internal 01 readings
  (37-01 "-faisant" compounds, 01-29 "-cier") untested here.
- **N161 — clause-boundary-precedent KILL** (battery-clause-boundary-
  precedent). Survey of all 35 distinct "X 77 [open-value]" windows
  (n(77)=44): zero windows where a clause boundary demonstrably
  resolves the adjacency with a complete clause on each side.
  The lane's boundary mechanisms stay dead; C (valueless 01 at
  @1029) is dead inside the same mechanism.
- **N162 — telle-52-37-rival KILL** (battery-telle-52-37-rival).
  "telle" excluded at kill grade at both Type-A 52-37 windows
  (@1124/@1722, the byte-identical 5-gram "06 11 52 37 43" in both);
  the candidate set reverts to {même, seule, dite}.
- **N163 — verb-14-rival KILL** (battery-verb-14-rival). The rival
  14=infinitive/verb-stem is killed at battery grade: 0/6 bar
  windows parse as verb frames (@72, @178, B4 failing at kill
  grade). Strengthens stem-14-84-retest's lane-wide verb-class
  fence (NULL). Terminal for the rival; 14's live arms are the
  determiner locus (F182) and the 'en' arm (F185).
- **N164 — edge-340-31-14 KILL** (battery-edge-340-31-14). The claim
  that "…03 qui 31 14 ce qui…" resolves once 31/14 are named is
  kill-grade dead: naming 31 (VERB class, F184) and exhausting 14's
  roles cannot resolve the edge — the break ("ce qui par" under
  banked/promoted values) lies downstream of both cells and admits
  no clause-boundary rescue. Upgrades ce-frame-45-64-96-43-87-01's
  fence to a kill.
- **N165 — ver78-65-completion KILL** (battery-ver78-65-completion).
  "@1105's 'ce ver[65]' completes a French ver-word" is forced
  false at kill grade by prof-65's standing PROMOTE (65 is
  noun-class; under §7 a noun-class cell cannot supply the
  word-tail syllable). @1105 is fenced as non-completing. 78="ver"
  as a LEAD (R16-005) is not re-graded here.
- **N166 — class-71-adjective C3 KILL** (battery-class-71-adjective).
  The uniform-class claim for 71 is killed; the adjective-shaped
  legs at W2/W3 are locus-level only (see F173 for the parallel
  38 narrowing).
- **N167 — seg-61-94-word-adjudicate KILL**
  (battery-seg-61-94-word-adjudicate).
- **N168 — seg-a1_01-hybrid-phase KILL**
  (battery-seg-a1_01-hybrid-phase).
- **N169 — unit-85-01 KILL** (battery-unit-85-01).
- **N170 — nir-value-60-68 KILL** (battery-nir-value-60-68).
- **N171 — lere-296-rival KILL** (battery-lere-296-rival).
- **N172 — w4-dict-det-gap KILL** (battery-w4-dict-det-gap).
- **N173 — inf-83-fork KILL** (battery-inf-83-fork): the
  frame-vient-parvenir "vient de me" leg is kill-grade dead
  (superseded by prof-98's finite-verb class grant).
- **N174 — sub02-wordinternal kill narrowed**
  (battery-sub02-wordinternal): the kill now covers only the
  phase-solid @459/@887 windows; @495 and @1152 re-derive under
  follow-ups.

Nulls (47, grouped by family):

- **02/14 stem block** (5: 02-class-609, stem-14-id, stem-62-ent-665-1536,
  stem-class-split, stem-03-value): 02's class cannot be named — the
  qui-windows x2 (@609/@750) are verb-selecting but @305/@858 force
  non-finite; packaged as a §7 split candidate; 14's value fenced (the
  @1122 la-frame dissolves: "14-06-11" is not verb+object); 62-as-verb-
  stem-final unconfirmable at both windows; stem-03-value fence (17
  non-verb-compatible windows: "[03] qui" x4, "pas [03]" x3, "ce [03]"
  x2, "[03] à" x3, "[03]e" x1).
- **13/41/43/44 block** (6: split-13-det-pron, w1-573-subject,
  class-41-contact, noun-43, donn-41-44, cond-mesure-43full): 13's
  distributional split is real and unseparated — 5 verb-successor windows
  vs 7 non-verb windows with no positional separator; packaged as a
  second-polyvalence candidate for the red team; W1's subject hunt closed
  at battery level (F158); 41 has no uniform class across its
  standing-value contacts (verb @40 vs determiner @238) — §7 split
  candidate escalated; 43's noun candidate set is empty ("condition"/
  "mesure" both fail @21/@343/@1027 at kill grade after "suite"/"manière"
  died; F152 terminal).
- **Determiner/adjective block** (9: adj-19, adj-91-723-second-leg,
  adj-78-fence, 61-20-61-frame, name-71, val-16-a-vs-est,
  head-77-62-94-noun, pre-71-60-class, inflect-19e-48): 19's adjective
  class holds one leg only ("est 19[e]" @1778–1780); 91's adjective
  reading fenced (@723 stands alone of 21 windows); 20 has no
  determiner/adjective value @279–281 (the 20 determiner/adjective
  paradox stands); 71's value fenced (name-71 NULL); "16 a vs est"
  fenced; 60-nominal fails at the "60 71" windows ("par"+verb and "pas
  ent"+verb both ungrammatical — the windows are 60-class-hostile
  generally); the feminine "-e" inflection frame tested for 19-48 (F148
  covers 32-48 x4 + 19-48 x1).
- **ceci/dict block** (3: dict-45-w4-adjudicate, ci-demonstrative-census,
  verdict45-value): the "ce verdict" positive leg is x1 (@573), not x2 —
  @982 fenced neutral under the w3-ceci circularity; the general claim
  "bound '-ci' outside ce-adjacent positions" finds zero support in the
  28-window census — @984 fenced as the unique candidate; no "determiner
  gap" leg stands.
- **ne family** (3: ne-94-non12-prefamily, est-ce-104,
  seg-94-82-06-f1): @508 stands alone — no word-internal-94 family beyond
  the 12-94 "prenne" family (excluded by the bar); the word-internal-94
  question closes at battery grade; est-ce-104 null; the F66 frame-C
  fence CONFIRMED at the local level (the fence is not lifted).
- **pas/30 block** (6: adv-62-pas-par, bound-96-00-clause,
  part-62-46-slot, pas-30-importe-discrim, reseg-3006-w2, reseg-3006-w35):
  the 62-adverb arm at @44–48 is fenced twice over — no adverb candidate
  parses ("par pour" right-edge kills every candidate; right-edge
  impossibility under granted values), and no byte evidence exists for a
  clause boundary between @47–@48 at any of the three "96 00" windows
  (all mid-row); the participial route at @46 is fenced too (62's
  word-class inventory between "pas" and "par" is now exhausted); the
  pas/importe rivalry is settled at battery level (0/19 @30 windows fail
  under "pas"; "importe" stays @1702-word-formation-confined); "00 67 46
  26 30 06 65" @1249–1256 fenced as a genuine residual (subjectless "que
  [26-verb]", unlicensed "pas", the "pour et que" left knot); the "pas |
  [06…]" shifts at the w35 windows fence epistemically.
- **segmentation block** (3: doubled-1195-offset-audit,
  spell-single-consonant, imp-80-set): doubled-offset audit null —
  laisser-gate-16's verdicts stand; the spelling rule cannot be confirmed
  (general form contradicted by byte evidence, narrow form ad hoc);
  imp-80-set null.
- **83/de block** (2: de-83-sweep, frame-87-83-cede): the promote bar not
  earned — unconditioned 83="de" kill stays owned by fence-911-de (no
  double-count); 83="de" lead in the 87-83-cede frame fenced, not killed.
- **value/misc block** (10: fem-32e, laisser-gate-16, lon-09-verb,
  frame-29-47, frame-82-16, npframe-60-690, cede-614-subject,
  contre-00-three-windows, noun26-26n-exclude, veut-86-1392-adjudicate):
  the 32-feminine frame fenced (passive remnant); laisser-gate-16 null
  (the "universal killer" untouched); lon-09-verb fenced; 29-47 / 82-16 /
  87-83-cede frames null; 60="dit"-shaped NP at @690 null (subsumed by
  N155); cede-614-subject null (58's class open, the conditional never
  fired); "par contre" parses all three "96 00" windows but cannot
  promote under the A9 00="pour" grant — escalated to red team (the "par
  pour" x3 systematic anomaly); the "[26n]" one-word rival fenced at 2 of
  3 la-windows; **veut-86-1392 escalated: standing-rule contradiction at
  @1390** — red-team-graded `battery67_final.json` R_et3 classifies 67
  @1390 as "et" while the granted §7 positional rule classifies the same
  window as "veut"; a battery cannot retire either system.

**Nulls (wave-5, 2026-10-09, grouped by family):**

- **@1029 / @1032 clause block** (3): ce01-slot-1029 NULL — the
  clause's last open slot goes to the red team as a clean two-horse
  race: A ('c'en', three profile legs: established local 'en',
  "m'en" @828 elision precedent, second "ce en" leg @984) vs B
  ('ce se', unattested for 01, no elision precedent); C
  (clause-boundary) killed; neither A nor B can promote at battery
  level ('en'-locality hard constraint + §7 polyvalence flag for
  A; red-team scope for B). Note also records the residual-1029-
  infinitive target as carrying a stale "ceci [03]er" premise and
  needing re-brief. edge-340-31-14's kill (N164) upstream of it.
- **24 block** (1): 24-en-verb-conflict NULL — escalate to red team
  (headline): definite window-level finding, mutual kill — 6
  windows kill 24="en", 4 windows kill 24=verb; §7 bars the
  split declaration, so the battery stops and escalates.
- **02/14 block** (4): clitic-14-82-breakers NULL (fence as tie —
  "82 14" = "mle", letter-level, adopted); conj-02-306 NULL — the
  "02 is a conjunction" claim fenced, not kill-grade dead in every
  window (@305 genuinely fits "et"/"ou"); qui-02-750-parse NULL —
  02's qui-legs stand at two (@609/@750), 02 remains a §7 split
  candidate (verb-selecting vs non-finite); det14-elsewhere NULL
  (fence executed) — 0/4 pre-registered windows yield a determiner
  leg, so 14's determiner value is fenced to the frame-tail
  window; stem-14-84-retest NULL (fence executed) — 14's verb
  class fenced lane-wide.
- **43/frame block** (4): frame-43-21-43-doublet NULL — C2 fails
  at kill grade, no shared 43 value nameable (noun set empty;
  verb-stem shape is red-team venue); frame-43-pour-census NULL
  (@244 untestable at battery grade — 66 open — fenced, not
  failed); frame-1205-parse null; head-62-94-21coord null.
- **52 block** (3): ne52inf-adverb NULL — the 'ne [52] [INF]' frame
  is real and 52 is negation-adverb-shaped inside it, but battery
  grade cannot NAME 52 ({plus, jamais} tie); profile-52-host-word
  NULL; val-62-ne-noun NULL (the "règne"/"trône" battery-null;
  one window fenced with stated cause).
- **56/65 block** (3): name-56-verb NULL (fence executed);
  noun-65-value NULL; stem48-65-value NULL.
- **60 block** (3): npframe-60-1366 NULL; npframe-60-1674 NULL;
  ledit-60-corrob NULL.
- **80 block** (3): x29-80-1596-nominal NULL (fence executed per the
  bar's else-branch); x29-80-collocation NULL — escalate to the
  poly-80-docket (the bar's uniformity presupposition is falsified
  inside the frame: two standing-grade, mutually exclusive roles);
  residual-345-06 NULL (fence executed per the bar's else-branch).
- **Misc nulls** (7): la-frame-52-37-43-noun NULL; leftedge-13-55
  NULL; reseg-553-retry NULL; satisfait-contrefait-lex NULL;
  seg-81-30-boundary NULL; seg-a1_01-extrinsic-phase NULL;
  syll-83-de NULL; verb-41-value NULL; w4-21-leftedge NULL;
  frame-43-pour-que-1544 NULL — the frame is a dead discriminator
  at battery level.

### Round-17 null batch, wave 14 (crowd17, 2026-10-09 UTC)

**KILLs (30, cipher-side):**

- **N175 — 62="bien" adverb KILLED** (battery-adv-62-bien-1482). The
  five "bien vient" kills rest on 98's promoted finite-verb class —
  preverbal "bien" before an ordinary finite verb is ungrammatical
  outside fixed idioms; @1482's concessive pass fails.
- **N176 — 85's value cannot be named from the -cier family**
  (battery-cier-85-595-name). No -cier member's stem fits 85's windows;
  @97 kills every stem at kill grade.
- **N177 — 86 = object clitic on the four 77-adjacent D-windows KILLED**
  (battery-clitic-86-77-windows). @951 forces the reading false at kill
  grade on granted values.
- **N178 — the 62–98 compound-venir prefix hypothesis KILLED**
  (battery-compound-62-vient). "62 98" never forms a compound-venir
  word at any of the five windows; the two-word "[62=il] vient"
  reading holds.
- **N179 — uniform-determiner-value over 86's 26 D-windows KILLED**
  (battery-det-86-dlife-value). Three windows independently force all 8
  candidates false (D00 @175 with 87=ce granted; D04 @671 with 11=la
  pencil; D21 @1345 with 47=ce granted). Scope note (the note's own):
  the kill is of the UNIFORM claim only — subset noun values untouched
  (see N205).
- **N180 — 06 rightward "pas"+"ent[65/62/60]" parse KILLED at
  @1251/@1327/@1561/@1733** (battery-ent-right-attach-sweep). 2 of 6
  control legs force non-words (@271, @789), firing clause 2.
- **N181 — uniform 37="re" candidate KILLED (conditional)**
  (battery-enterre-37re-s5). Re-opens only iff 77≠"le".
- **N182 — word-internal "[G]er89" KILLED at @113/@275/@781/@1377/@1393**
  (battery-er89-wordinternal-govern). "29 89" is a word boundary at all
  five — 89 is standalone.
- **N183 — 20's verbal value KILLED** (battery-inf-20-nepas). No
  verbal-20 value parses both "pas [20]" windows; at @1270 the bar
  fails at kill grade because "qui ce [76-noun]" is ungrammatical
  value-independently.
- **N184 — 60's "de" arm KILLED at @1736–1739**
  (battery-leftedge-60-value). Promoted 06="ent" cannot stand or attach
  left, so 60 is word-internal under the standing ent-60 arm; as a
  uniform value, 60="de" is contradicted by the 03 ×4 verb-stem
  successors.
- **N185 — the "[97-imperative] les!" re-segmentation at @567 KILLED**
  (battery-les567-imperative). 97 is nominal (forced at @289, zero
  contradictions across all windows).
- **N186 — uniform-gendered-noun over 86's D-windows KILLED**
  (battery-noun-86-dlife). @671 (11=la pencil) forces feminine while
  @175/@1345 (87/47=ce granted) force masculine; the only escape is an
  unevidenced epicene.
- **N187 — the uniform-86 noun value is unnameable AND distributionally
  dead** (battery-noun-86-dlife-name). PROMOTE:FAIL — no noun value
  nameable (feminine window count 1 < the bar's ≥2); KILL:PASS — the
  gender split forces every single gendered noun value false. Subset
  values untouched (see N205).
- **N188 — 88 as plural noun subject at @1117 KILLED**
  (battery-noun-88-subject). Forced false by @1114–1123 ("la" + plural
  noun agreement violation on banked 11=la) and @496–497 ("tout" + bare
  plural noun on granted 79=tout). Consistent with F243's 88=VERB
  promote.
- **N189 — 08="on" homophony KILLED** (battery-on-08-homophony). 08 is
  not a homophone of granted 84="on": clumped cycling (z=-2.516,
  kill-grade per the {33,86} precedent), predecessor segregation (08
  excluded from 84's signature "l'on" frame, Fisher p=0.030), zero frame
  interchangeability across 29 anchor frames. §7: asserting it would
  declare a second polyvalence. 08's value stays open.
- **N190 — 62's "other" windows fail the participial census**
  (battery-part-62-elsewhere). The participial-shaped environment with
  a clean right edge fails the bar across 62-94 ×9, 62-48 ×6, 62-98 ×5,
  62-16 ×4, 62-61 ×2, 62-06 ×2, 62-96 ×1. 62's conditioned scope stays
  a red-team docket item.
- **N191 — the one-stem "re-[62]ent" reading KILLED at window A**
  (battery-re-prefix-03-665).
- **N192 — 61="son" possessive KILLED** (battery-re61-son-test). C1
  fails: zero clean "son" legs; the two flagships are one repeated
  formula and flagship 1's parse is dead.
- **N193 — 83="gar" KILLED across the n=15 census**
  (battery-re83-gar-test). The 87-83="cède" window is a different,
  incompatible 83 value; five 98-conditioned "de" windows kept intact.
- **N194 — the x9 62–94 word-final-"ne" claim KILLED**
  (battery-seg-62-94-wordfinal). @1772 forces a word break between 62
  and 94 at kill grade under standing promoted values; only 2/9
  windows parse as one word. The scoped residue is separately promoted
  (F244).
- **N195 — 06="entre" spelling KILLED at the "06 70 12 94" window**
  (battery-spell-06-entre). Any future 06="entre" claim needs
  independent byte evidence (red-team §7 venue only).
- **N196 — the subject reading of 26 at @1753 KILLED at kill grade on
  all three live class hypotheses** (battery-subj-26-1753) — the
  pasent-subject-26-56 category clash.
- **N197 — 61 is not word-internal to a longer unit at either locus**
  (battery-unit-78-45-13-55-61).
- **N198 — 53's "[X]i"-noun space KILLED** (battery-val-53-Xi-noun).
  Exhaustive French "[X]i" enumeration admits only three weak
  candidates ("bon", "so", "co"), each forced false by the @402 object
  slot and the "53 12" ×4 windows with zero new assumptions. 53's
  value itself unnamed; the "don"-vs-"doni" irreconcilability untouched
  (F242).
- **N199 — the "que [60-V] et le [89-V]e" verb-coordination parse at
  @637 is an unresolved parse and a kill-grade contradiction**
  (battery-verb-coord-637) — the subject gap is unbridgeable here.
- **N200 — 88's uniform vient/tient-family verb stem KILLED**
  (battery-verb88-26-stem). Stem-level only: 88's class is separately
  promoted (F243).
- **N201 — W1's 55–61 non-detachable arms KILLED**
  (battery-w1-55-61-reseg). 55-61-94 closed by a standing kill-grade
  verdict (red-team-only re-open); 13-55-61 forced false at kill grade.
- **N202 — W2's 55–61 window fenced as a "ne ce"-driven residual with
  stated cause** (battery-w2-5561-nece-frame; stream-unique 94-87
  hapax). The bar's resolution arm is met — fenced, not killed (the
  distinction matters).
- **N203 — 07 = verb stem KILLED at kill grade**
  (battery-x-07-verb-stem). Three independent windows (@794/@1193/
  @1751) force 07 non-verb-stem; the sole stem-shaped window (@772)
  parses as such only under the claim itself; the ≥2-frame threshold
  is unmet (exactly 1).
- **N204 — the detachable-slot reading (one French word X over the
  55–61 bigram at W1/W2/W3) KILLED** (battery-x-55-61-candidate-list).
  The candidate space collapses to zero (W3's promoted "prend" is
  ungrammatical at W1/W2; the plural-noun alternative is already
  kill-grade dead). 55 or 61 individually unexamined; the 55-61-94
  word-unit hypothesis stays live.

**Mixed partition (1):**

- **N205 — MIXED per subset over 86's 26 D-windows**
  (battery-det-86-dlife-partition). (1) "le"-life subset: NULL — the
  "le" lead survives, promote gated on par-pour-962-adjudicate; (2)
  det-left 3 (noun-class): PROMOTE — 86=noun at battery level,
  subset-scoped, class-level, value unnamed; (3) 77-adjacent 4: clitic
  value KILL (granted window forces false), noun reading PROMOTE. The
  lane's 86 picture is now partitioned — determiner dead uniformly
  (N179), noun live per-subset (N186/N187 killed only the uniform
  noun claims). No verdict overwritten.

**NULLs (35, cipher-side):**

- **N206** — 01 as adverb at @483 ("30 01 19") fenced per the bar's
  else-branch (battery-adv-01-19-frame).
- **N207** — no modal nameable for 02; "fait" packaged as a conditioned
  candidate for the red-team §7 split docket (battery-adv-02-858).
- **N208** — 44's l'-antecedent unresolved (fence executed;
  battery-antecedent-44-l-prime).
- **N209** — no grammatical 1841-French parse of @1028–1040 under
  standing values once the exclamatory-infinitive assumption is removed
  — residual fenced (battery-ce01-slot-1029-infinitive-avenue).
- **N210** — 87's role at @1028 fenced, not named; leading arm: the
  "ceci" compound (87 + bound "-ci"); alternative: stranded-"ce"
  (battery-ce87-1028-role).
- **N211** — 53's value unnamed and unnameable at battery grade without
  inventing data (battery-ce88-53-value).
- **N212** — effect of the "cela" promote on @1117's determiner frame
  undecidable until the trigger fires (conditional bar;
  battery-cela-1117-frame).
- **N213** — 23's class not uniformly decidable: verb established at 7/8
  windows but W8 @1782 ("65 23 98-vient") forces a non-verb parse (1/8
  = 12.5% > the 10% bar); packaged as a FENCED SPLIT for the red-team
  docket — implicates the vient-98 formula leg at @1783 and the §7
  sole-polyvalence law (battery-class-23-qui-adjective).
- **N214** — the 20-window paradigm decided affirmative at battery
  grade but escalated to the red team ("@760 forces determiner-block"
  fails — @760 admits grammatical 20-valued parses;
  battery-det-20-window-local-paradigm).
- **N215** — 65's gender unadjudicated at battery grade; the masculine
  leg ("tout 65" @1682–1683) is now the stronger; the feminine leg
  (@1211 "est 32e par") is conditional on 32's unresolved adjective arm
  (battery-det-65-gender-adjudicate).
- **N216** — the 18-window "premier"-duality census complete and
  escalated: 9 premier-resisting, 5 unresolved, window-level reasons
  recorded (battery-duality-61-7034-pattern).
- **N217** — each window fenced with stated cause
  (battery-ere-word-65-frames).
- **N218** — the "et 86 er" licensor (16) stays unnamed; fence executed
  under the R_et3-conditional (battery-et86er-licensor-16).
- **N219** — the [42ne] composition is a live conditioned hypothesis
  (clean at W3) but docket-gated at W2 (needs 24="en") — cannot
  promote under standing values; no polyvalence declared
  (battery-frame-42-94-leftward).
- **N220** — "ne [76]" ×2 verb-vs-sub-word inconclusive — verb read
  blocked by the missing verb lock (battery-frame-76-ne-94).
- **N221** — 76's gender tension: no window forces the one-class claim
  false at kill grade; each rival admits a live alternative
  (battery-frame-76-tension).
- **N222** — 09's "lon"-resegmentation fenced (fence executed); a
  general prefix-class for 09 is killed at battery grade (@290)
  (battery-lon-09-reseg).
- **N223** — trigger condition not met — the bar's precondition is
  absent, not falsified (battery-lon-77-le-gate).
- **N224** — pas-slot audit: zero "ne" legs on 08 across all 18 windows
  (kill-grade baseline for any future "ne" claim on 08: must produce
  ≥2 clean "ne…pas" frames or explain @1323's order inversion and
  @1520's 24-contradiction; battery-ne-08-frames).
- **N225** — 09's noun claim at @916 fenced (battery-noun-09-916).
- **N226** — neither arm kills: the adjective arm retains its battery
  HOLD ("est 19[e]" @1778–1780); the PP arm is unsupported (no agent,
  no verb-frame evidence at 9 windows; battery-participle-19e-frame).
- **N227** — particle face confirmed at battery grade; value "mais"
  named and routed to the poly-20-docket (battery-particle-20-760-839).
- **N228** — 08 as verbal prefix/syllable with 31 survives everything
  but composition is not demonstrated over adjacency — inconclusive,
  regenerates work (battery-prefix-08-31).
- **N229** — 43's class cannot be named at battery grade (noun is
  distributionally the runaway leader but triple-barred: noun-43
  closure, 43-29-segment's scope bar, la-frame's red-team gate); the
  "43 81" direct-object NP fails, so the seg-81-30-boundary fence stays
  closed (battery-prof-43-object).
- **N230** — 09 at @290 fenced per C3 (battery-rel-09-290).
- **N231** — all three word-internal arms blocked at battery grade — no
  arm parses the full clause (battery-seg-86-52-37-86).
- **N232** — the second 06's value in the 06-06 doublings fenced: "ent
  ent" (two-word) kill-grade dead; the new-word "ent…" reading
  unfalsified but unnameable within the ≤1-assumption bar
  (battery-seg-94-82-06-f3).
- **N233** — 08's value undecided: "se" eliminated at kill grade;
  "on"/"ne" inseparable from granted 84="on"/promoted 94="ne" without
  forcing (battery-stem-08).
- **N234** — the "42 94" frame fenced: the nominal arm fails (02 and 74
  take no stated nominal class), the verbal arm is already dead
  (battery-subj-42-ne-frame).
- **N235** — 16/84's role (fail closed; battery-val-16-84-role).
- **N236** — 92's value unnameable at battery level (coordinate with
  the split-92 red-team docket if unresolved;
  battery-verb-92-value).
- **N237** — the global-"voi" hypothesis on the D-partition is neither
  killed nor promoted — converges with the earlier voir-86-sweep NULL
  on an independent ratified-only re-derivation
  (battery-voi-86-dwindow-composition).
- **N238** — 16's class: C1 passes but C2 (the left-edge-closing
  hypothesis) fails; the bar as a whole is not satisfied
  (battery-w2-16-class).
- **N239** — fence executed per the bar's second disjunct
  (battery-w2-knot-etque).
- **N240** — the W4 left edge @1158–1163 ("77 82 44 83 21 67") does not
  decide whether "et" coordinates an antecedent NP — the decision still
  pivots on 21's value (battery-w4-left-edge-21-83).

**Corpus-side nulls (34, compressed — each is a fence-executed null from
the disloc-demonstrative / governed-exclamatory / reinforced-pour-inf
program; no standing verdict touched):** the drama corpus-gap null
(battery-disloc-demonstrative-drama — bar untestable until the ingest
landed, which fired the commission instead); prose disloc-demonstrative
zero (`disloc-demonstrative-inf_census.json`: 27.66M chars, 15
candidates, 0 genuine); quoted-dialogue disloc-demonstrative zero
(`disloc-demonstrative-quoted-drama_census.json`: ~10.3M chars, 169
dem-comma in dialogue, 0 genuine — the "ca" control zero too);
reinforced-head prose zero
(`disloc-demonstrative-reinforced_census.json`: 27.66M chars, 231 hits,
0 genuine); drama reinforced-head zero
(`disloc-demonstrative-drama-reinforced_census.json`: 2,969,582 chars,
41 hits, 0 genuine); drama clause-initial demonstrative zero
(`disloc-demonstrative-drama-clause-initial_census.json`: 2,969,582
chars, 190 dem-comma → 12 clause-initial → 0 exclamatory — the three
near-misses dissolve on "cela" as governed object, not fronted topic);
drama dialogue-scoped zero
(`disloc-demonstrative-drama-dialogue_census.json`: 2,939,372 chars,
35 candidates, 0 genuine — Hernani has bare exclamatory infinitives but
never under dislocated demonstratives); drama reissue zero
(`disloc-demonstrative-drama-reissue_census.json`: 2,969,582 chars, 190
dem-comma → 35 candidates → 0 genuine); pausemark-recall zero in drama
(`disloc-demonstrative-drama-pausemark-recall_census.json`: 307
separator hits → 120 hand-classified → 0 genuine — fence covers comma
AND non-comma separators); reinforced-head prose clause-initial zero
(`disloc-demonstrative-prose-clause-initial_census.json`: 27,656,185
chars, 447 dem-comma → 16 clause-initial, all finite — arm (a) of
ce87-1028-role now fenced in prose as well as drama); prose pausemark
recall (`disloc-reinforced-pausemark-prose-recall_census.json`:
27,657,940 chars, exactly 1 dem-pausemark hit, 0 genuine — all seven
pause-mark classes accounted); zero-pause extension
(`reinforced-pour-inf-zeropause_census.json`: 929 zero-pause windows, 0
genuine; 16 declarative zero-pause governed-infinitive windows exist);
reinforced-head drama clause-complete
(`disloc-demonstrative-drama-reinforced_census.json` counted above);
drama governed-inf prep-family zero
(`disloc-reinforced-prep-inf-drama_census.json`: 2,969,582 chars, 41
hits, 0 governed-infinitive candidates); drama modal/perception
governor zero (`reinforced-modal-inf-drama_census.json`: 2,939,372
chars, 41 dem-comma hits, 0 pattern candidates — fence robust to
governor widening); drama reinforced pour-inf recall
(`reinforced-pour-inf-drama-recall_census.json`: 41 dem-comma hits, 6
uncapped windows, 0 genuine; side observation — Ruy Blas @34184 shows
the register HAS bare exclamatory infinitives under modal/perception
government in reinforced-head windows); drama pour-inf
(`reinforced-pour-inf-drama_census.json`: 2.94M chars, 41 dem-comma
hits, 1 candidate dissolving on clitic resumption, 0 genuine —
two-register program complete: 0 genuine in 30.6M chars prose+drama);
pour-inf diagnostic (`reinforced-pour-inf-diagnostic_census.json`:
27.66M chars, 206 dem-comma → 4 governed-infinitive candidates → 0
genuine — the "pinpoint the fence at governed-vs-bare" fork resolves as
no-line: the fence is head-local); pour-inf recall
(`reinforced-pour-inf-recall_census.json`: complete 232-occurrence
inventory in 27,657,940 chars → 0 genuine); reinforced adjacent-excl
recall (`reinforced-pour-inf-adjacent-excl_census.json`: 24 head+prep+inf
hits → 22 genuine declarative zero-pause windows, 0 adjacent
exclamatory clauses — the parent zero is not a window-boundary
artifact); comedy bare-heads zero
(`disloc-comedy-bare-heads-extension_census.json`: 465,531 chars, 51
dem-comma hits, 0 bare-"ce"-comma hits → 0 genuine) and its recall
(`disloc-comedy-bare-heads-recall_census.json`: 31 variant candidates,
0 genuine — dash/paren documented as empty pause classes); comedy
governed-inf zero-pause recall covered above; reinforced-head comedy
extension zero (`disloc-reinforced-comedy-extension_census.json`:
465,531 chars, 2 reinforced-head-comma hits, 0 candidates — dem-comma
hit rate ~1/233k in comedy vs ~1/72k in drama); comedy recall zero
(`disloc-reinforced-comedy-recall_census.json`: 1 recall candidate —
cross-speaker bleed, excluded — 0 genuine); wider-comedy zero
(`disloc-reinforced-comedy-widercorpus_census.json`: 1,359,737 chars, 9
candidates, 0 genuine — the note honestly logs the shortfall: only
565k added vs the parent's ≥1M suggestion); verse-vs-prose comedy zero
(`disloc-reinforced-verse-vs-prose-comedy_census.json`: verse 4
candidates in 362,408 chars, dialogue 57 in ~1.2M chars, 0 genuine —
fence generalizes across sung verse and spoken dialogue); gov-excl-inf
register zero (`gov-excl-inf-register_census.json`: 27.66M chars, 859
candidates → 0 genuine — the headline reframe: the zero is
REGISTER-LEVEL, not head-local); gov-excl-inf recall zero
(`gov-excl-inf-recall_census.json` + classification: 1,874 candidates
across previously unsearched window classes → 0 genuine — combined
2,733 classified candidates, the largest base in the family); epistolary
zero (`disloc-governed-excl-epistolary_census.json`: 11.78M chars
correspondence, 77 reinforced + 198 plain-demonstrative-head hits → 0
genuine — closes the last live prose hunting ground); prose recall
(`disloc-governed-excl-prose-recall_census.json`: 30.6M chars, 231 hits
→ 0 genuine — with 236 "pour/de [inf] !" positive controls, so the
absence is head-specific, not register-wide); tonic-pronoun governed
zeros — drama (`battery-personal-tonic-governed-excl-drama`: 1,986
pronoun-comma hits → 29 candidates → 0 genuine — the fence sits exactly
at governed-vs-bare) and prose
(`personal-tonic-governed-excl-prose_census.json`: 27,656,185 chars,
4,495 pronoun-comma hits → 26 candidates → 0 genuine); pasX-adverb
census (battery-pasX-adverb-census: 19 "30 X" windows re-derived on the
repaired stream — no adverb-shaped X with a complement-bearing right
edge; the note carries a data-quality flag for supervisor audit).

### Round-17 backlog null/kill fold (2026-10-09 UTC — 18 notes: 8 kills, 10 nulls; battery grade)

 — N241–N248:**

- **N241 — the "06-14-06" residual @1120–1122 confirmed UNRESOLVABLE
  at battery grade** (battery-ent14ent-residual-adjudicate). Every
  sub-word role for 14 dies under standing values within the
  one-assumption budget; all four battery-named escapes ("le", "sou",
  verb-stem, single-n "prennent") are kill- or fence-grade dead.
  Narrow scope: kills resolvability, not 14 globally. The surviving
  "le"-legs (@72/@117/@178) remain homophony-question evidence,
  escalated to the red team.
- **N242 — the "A3 mirror" KILLED** (battery-formula-94-07-06-94). Two
  adjacent, independent negated clauses abutting across a manuscript
  row break ("…ne [07]ent | ne [15]…"), not one mirror frame — forced
  false at kill grade. Reinforces the ne-94 and ent-06 promotions (two
  more clean ne-frames, one more -ent verb). Follow-up: name 07 via the
  "94 07 06" = "ne [07]ent" leg (x-07-verb-stem, P3).
- **N243 — @486 contains no relative clause**
  (battery-noun-19-486-relative). "19 qui 76…" with 76 a
  battery-promoted noun cannot parse as antecedent + subject-relative
  in 1841 diplomatic French, against clean "qui + verb" controls at @19
  and @511; the relative-clause rival to the predicative account of 19
  dies at kill grade, and the single predicative leg ("est 19[e]")
  stands alone. "01 19" ×2 with 01 classless out of scope here.
- **N244 — the word-internal rival for 86 is dead at all four problem
  windows** (battery-reseg-86-problem-windows). At #0/#6/#8 any
  word-internal parse contradicts banked ground truth or granted
  standalone values (kill grade); at #7 no French word is nameable
  without invented values. The standalone assumption survives; #7 stays
  a residual orphan under stem-86's adjudication.
- **N245 — search closure on 21's value, not a class downgrade**
  (battery-val-21-reopen). "A battery-grade value for 21 exists" fails
  at kill grade: @134 forces every noun value false, @109/@359 force
  every masculine value false, and non-noun values contradict the
  battery-promoted noun class. 21=noun (de-frame-21-class) stands
  untouched. Re-open is red-team venue only (overturn prof-65's
  65=noun promote; grant the §7 21-65 unit-verb rescue; re-tier 21's
  class).
- **N246 — the claim "W4's 'qui 52 38 ce 86' can be resolved with 38's
  class open" falsified at @1343** (battery-adj-38-w4-parse). All 9
  candidate parses fail (7 classes of 38 + the 52–38 unit + 3
  clause-boundary rescues), so W4 is fenced with stated cause. n(38) =
  7 byte-confirmed at @384/@826/@1113/@1343/@1469/@1650/@1828. Re-open
  conditional on a standing grant changing underneath (52's class, 86
  beyond INF-class, or 47's allophone tier).
- **N247 — "qui" (64 @531, 1-based) cannot be the 3pl subject of
  "[42]ent" (@544)** (battery-subj-42-qui). A subject relative pronoun
  does not sit 12 lexical tokens from its verb (stream max is 3,
  clitics only), and a 3pl verb cannot agree with the singular
  antecedent the relative clause requires. The live rivals for @544's
  subject stay undecided (w3's fenced 44-29-48 hypothesis vs the
  "qui [26]" short-clause cut) — this kill decides neither.
- **N248 — bare "ce" cannot head an exclamatory infinitive clause in
  1841 French** (battery-ce87-topic-licensing). Clitics cannot be
  dislocated; zero attestations in the 24.4M-character 1841-register
  corpus — tonic cela/ceci/ça own the slot. Candidates A ("c'en") and
  B ("ce se") at @1029 both die on their single shared load-bearing
  assumption (refuted), and ce01-slot-1029 found no alternative
  grammatical route. 87="ce" value stands; 87's role at @1028
  re-opened. This is the register-level precursor of the wave-14
  corpus program's pronoun-only licensing finding; F245's skeleton
  revision ("Ceci, [03]er!…") is consistent with it.

**Backlog nulls (10) — N249–N258:**

- **N249** — the W1 full-window-parse claim under 14="en" is NOT
  falsified ("[76] m'en est [37]" parses cleanly; "82 14" has a second
  "m'en" leg @896; "79 14" ×2 fits "tout en") but the bar's
  full-window parse cannot be completed within battery authority and
  the ≤1-assumption budget — blocked at 1-based @626–627 ("37 33",
  A1-predicative + bare INF-class 33, a stream-wide hapax)
  (battery-clitic-14-623-steelman).
- **N250** — 74 stays class-open; @141's "le [74]" stays headless as a
  determiner leg (independently unlicensable per det14-elsewhere)
  (battery-noun-74-census). All doubling windows sit on offset-0 rows
  with unvalidated upstream offsets — a row re-phase would re-open
  that window only.
- **N251** — the verb-branch residual claim ("resolve @531/@1470/
  @1753") not established: 1 of 3 windows parses (@531), 2 fenced with
  stated cause (@1470 blocked on 38's class, @1753 on 89's class); not
  killed — no window forces the claim false
  (battery-noun26-residual-adjud).
- **N252** — the @354/@356 "40 92 98 92" segmentation unresolved:
  the word-internal alternative dies only conditional on battery-grade
  98="vient" (not §7), and the two-word alternative is underdetermined,
  not refuted (battery-seg-92-354-356).
- **N253** — "12 16" occurs exactly 3× (@241/@843/@1430): 12 is
  word-initial at the 2 decided windows, but uniformity is not
  established (W2 @241 is the fenced window itself)
  (battery-tail-12-16-uniform).
- **N254** — clause 1 fails at null grade: 52 unnameable at battery
  grade — the "ne [52] [INF]" frame is real but no value covers 52's 27
  windows without red-team-declared polyvalence; clauses 2–3 pass. Not
  killed: no window forces the "ne [52] [86]" parse structure false
  (battery-leftedge-52-86-1736).
- **N255** — 56's value underdetermined at @1745 (mixed class profile,
  §7 polyvalence question): not killed (the segment parses cleanly as
  "que"+3pl verb), not promoted (the bar demands 56 NAMED)
  (battery-rightedge-56-1745).
- **N256** — the one-word read of "11-78-40-97-86" @296–@300 not
  demonstrated under the licensed frames (frame-97-profile: 97 =
  INFINITIVE class, value open; stem-86: NULL). Not killed: @296 stays
  compatible with 78="ver" as the R16-005-fenced 1-window residual; the
  fence reason updates — lack of a licensed 97/86 completion, not the
  (now-dead) "l'ere" rival (battery-ver78-296-97gate).
- **N257** — W4 (@1164) undecidable at battery level: the word-medial
  rule's antecedent is conditional on the red-team-escalated one-word
  boundary (dict-78-45-wordbound null), and its consequent ("et verdict
  [13-55-61]") fails to compose under standing values. W4 stays fenced
  as the last unclassified 78-45 window, pending (a) the red-team §7
  boundary declaration and (b) ver-78's resolution
  (battery-dict-45-w4-adjudicate).
- **N258** — the "77-62-94" word's syntactic slot identified (62,
  masculine nominal stem, "-ne"-final under the conditional
  syllabic-94 reading) but no lexical value forced — the word cannot
  be named at battery grade (battery-head-77-62-94-noun). REPORT.md's
  prior "77-62-94" hits all belong to the separate
  battery-lon-ne-77-62-94 note, not this verdict.

### Round-17 null batch, wave-14 mid-sweep arrivals (2026-10-09 UTC —
8 notes: 8 nulls; battery grade)

- **N259** — stem48-qui-65-hapax NULL (fence executed). The @1585-1588
  "36 70 64 65" 4-gram has no licensed full parse under standing
  values: "pour [36-noun]" closes cleanly upstream (licensed PP frame,
  class-36-profile), so the orphan localizes to the stranded "pre"
  (70) — word-initial in all 15 windows of its profile, with "qui"
  (granted 64) occupying its continuation slot at the 70|64 boundary;
  "36 70" hapax, "70 64" hapax, "64 65" hapax; every rival "qui"-role
  (relative/interrogative/indefinite/exclamative/"ce qui") dies at
  kill grade. Phase-conditional: row a8_02's upstream offset is one of
  the 68 unvalidated.
- **N260** — regne-trone-tiebreak NULL: the "regne"-vs-"trone" tie at
  @508 is NOT broken at battery grade. Avenue (b) negative (no landed
  neighbor creates selectional pressure); avenue (a) finds a
  differential frame ("le [62]ne qui vient" — "regne" selectionally
  licensed + 1 weak attestation vs "trone" strained + 0 in 31.66M
  chars) but below battery-grade naming confidence. Per section 5 the
  contradiction with the standing battery-grade @508 "trone" locus
  promote (F250) is escalated to the red team — a battery never
  downgrades an existing verdict. Follow-ups: val-65-at-508 (P3),
  trone-vient-register (P3), redteam-508-reread (P2).
- **N261** — 01-verbclass-probe NULL: 1 of 28 windows verb-shaped
  (@1256/P1, "[65-N] que [01-V-finite] [61-S]") re-opens avenue A (01
  as infinitive governor at @1029); the @1028-1031 fence is NOT
  hardened. The P1/P2 section-7 tension (01 verbal vs nominal — 67 is
  the sole polyvalence) is red-team venue; 61-verbclass-probe (P3)
  would flip @1256 to P2 and re-kill avenue A.
- **N262** — fin-41-lexicon NULL: untestable-as-written — no
  finite-verb value candidate for 41 exists on the lane record (lexicon
  generation would be invention, not testing), and the "qui [41]"
  frame's subject (antecedent "08 91 39") is a stream-hapax with no
  landed value, so the agreement shape is unrecoverable. An epistemic
  null, not a refutation. Follow-ups: antec-08-91-39, qui-subject-
  recoverability, fin-41-lexicon-r2 (all gated).
- **N263** — disloc-demonstrative-inversion-drama NULL: 490 unique
  candidates hand-classified with cause across the 14-play drama
  corpus → 0 genuine postposed-demonstrative + bare exclamatory
  infinitives. Inverted order fenced in drama dialogue; arm (a) of
  ce87-1028-role now fenced at seven levels. Script
  `disloc_demonstrative_inversion_drama_census.py`; raw
  `disloc-demonstrative-inversion-drama_census.json`.
- **N264** — bare-excl-inf-head-inventory-drama NULL: the head-type
  table lands (1,641 pattern candidates over 2,939,372 chars) — 0
  genuine demonstrative-headed bare exclamatory infinitives (all 13
  demonstrative-involving candidates excluded with cause) vs 5 genuine
  tonic-pronoun heads ("moi, fuir devant le duc de Guise !" et al.).
  The arm-(a) fence holds exactly at the demonstrative head, with
  positive-space contrast. Raw
  `bare-excl-inf-head-inventory-drama_census.json`.
- **N265** — disloc-demonstrative-inversion-prose NULL: 146 candidates
  hand-classified with cause over the 21-file prose corpus
  (27,656,185 chars) → 0 genuine; strict-pattern check ("[inf-suffix]
  ! , cela/ceci/ça") run over all 21 files → 0 hits, so the loose-rule
  zero is not a recall artifact. Inverted order fenced in prose: arm
  (a) now fenced in both word orders across all three registers.
  Raw `disloc-demonstrative-inversion-prose_census.json`.
- **N266** — disloc-demonstrative-drama-pausemark-dialogue NULL: 128
  candidates in dialogue-scoped drama text (2,539,841 scoped chars;
  front matter, ALL-CAPS headers, stage directions stripped) → 0
  genuine (119 carried from the parent's 0-genuine classification, 9
  new all excluded with cause). Non-comma separators fenced at dialogue
  level too. Raw
  `disloc-demonstrative-drama-pausemark-dialogue_census.json`.

### Round-17 null batch, wave-15 arrivals (crowd17, 2026-10-09 UTC —
48 notes: 48 nulls; battery grade)

- **N267** — adj-68-postnominal NULL: three post-nominal windows
  unresolved (@1719/@884/@1442) — the noun/adjective split forces the
  fence.
- **N268** — antec-08-91-39 NULL: the antecedent question unfired at
  battery grade; no standing verdict touched.
- **N269** — bound-70-abbrev-premiere NULL: the 70-as-abbreviation
  route fenced (abbreviation arm only; distinct from the value
  question).
- **N270** — complement-14-60-27-head NULL: the bar's else-arm fired
  as designed — the hapax fence is the finding.
- **N271** — conj-prep-20-wide NULL: the conj/prep route for 20
  fenced — no clean route survives.
- **N272** — croire-33-compound85 NULL: trigger condition fails as
  gated — the dire-only compound geometry is unfalsified but
  unnameable.
- **N273** — det-91-11-frame NULL: neither "91 11" window gives "la"
  a battery-grade NP frame (W1 lacks tail bytes; W2 crashes on the
  91/81 agreement).
- **N274** — dire-33-asymmetry-no21 NULL: the resolve arm unfired;
  fenced as 21-load-bearing. The N281 kill (croire-33-noun21) resolves
  the reopen condition — this fence is now a revisit candidate.
- **N275** — disloc-demonstrative-epistolary-pausemark NULL: zero
  genuine dislocated-demonstrative + non-comma pausemark in the
  epistolary corpus; the arm-(a) fence holds there too.
- **N276** — disloc-demonstrative-prose-pausemark-recall NULL: the
  recall sweep confirms zero genuine dislocated-demonstrative +
  non-comma pausemark in prose.
- **N277** — fin-88-645 NULL: finite-88 at @646 is neither forced
  nor forced false — "ce [61] [88] le [78]" stays a 61/88 residual.
- **N278** — follower-65-adjclass-census NULL: the follower route is
  fenced — adjective-position followers (23×3, 88, 16, 68) cannot
  supply the gender-agreement window.
- **N279** — frame-76-94-trigram NULL: the 76-94 trigram frame
  unfired — fence as designed.
- **N280** — frame-parallel-08-31 NULL: no polyvalence declared —
  67="et" follows the positional rule at @630/@1519.
- **N281** — frameA-50-value NULL: the "ent…" new-word reading is
  unfalsified but unnameable — 50's value underdetermined.
- **N282** — imp-80-bare-1156-1596 NULL: both imperative-80
  candidates fenced, neither killed — the bytes do not ground the
  boundary.
- **N283** — inf-7780-reseg NULL: re-segmentation undecidable
  pending red-team adjudication of the 80/89 infinitive class;
  3 follow-ups.
- **N284** — inf-80-89-ratify NULL: the bar is untestable as written
  — the records prove the precondition "MET" is NOT met at ratified
  grade. The worker formally rejected the bar (second such rejection
  lane-wide); a record-adjudicated inter-report conflict was resolved
  at the records layer without invention.
- **N285** — inv-98-76-12 NULL: no window forces a falsehood about
  98-76; fence executed.
- **N286** — left-64-29-boundary NULL: no uniform reading
  demonstrable — an epistemic fence, with the 64="qui" grant
  respected.
- **N287** — left-88-02-88-307 NULL: a conditional claim at a hapax
  locus — kill would require excluding every construction.
- **N288** — mne-52-16-branch NULL: the defect isolates to 94 — C1
  passes, C2 fails; the kill leg cannot fire at grade.
- **N289** — ne-08-verb-slot NULL: 08's class stays open — stem-08's
  word-internal PROMOTE is a live rival explanation, not adjudicated
  here.
- **N290** — neque-79-twin-frame NULL: the distributional twin is
  real (byte-identical "94 79 14 60" @1363/@1687) but not
  grammatically licensed at either locus — CONFIRMS the
  npframe-60-detleft-closeout fence as a residual.
- **N291** — neque-bracket-verb-search NULL (permanent residual):
  the instance-B "ne…que" verb slot is a structural zero — this NULL
  spawned the now-complete neque-instance-sweep finder beat.
- **N292** — nom-71-1336-value NULL: 71's value unfirable; fence
  executed with stated cause.
- **N293** — nondet-20-sandwich NULL: all three non-det/adj arms for
  20 fenced with stated cause.
- **N294** — noun-43-1205-window NULL: noun-43's candidate set is
  empty at battery grade (all four killed) — the question is fenced as
  dependent on the noun-43 line.
- **N295** — npframe-60-322 NULL: no verbal-60 class parses
  "92 60 15" at @322.
- **N296** — npframe-60-detleft-closeout NULL: hapax, class unnamed
  — the detleft route for 60 closed.
- **N297** — par43-ce-scope NULL (docket-input grade):
  discriminating frames delivered to the red-team 43 docket; no
  verdict claim named.
- **N298** — parse-1626-clause NULL: @1626 clause structure blocks
  any semantic verdict — 3 follow-ups (56's form, 69's class,
  the 69-26-00-33 kernel).
- **N299** — premier-61-flank-census NULL: "premier" is NOT 61's
  conditioned value — exactly 1 proven admission (@1556) + 1
  flank-supported candidate (@645).
- **N300** — procreer-56-semantic NULL: procréer not excluded (@1745
  gradient fit via Littré absolute use) but the 8-way tie for 56
  stands.
- **N301** — qui-02-609-parse NULL: the verb requirement on 02 at
  @609 is unmet — the conditional does not fire.
- **N302** — qui-41-01-boundary NULL: the rival phase is unvalidated;
  no window forces the boundary false.
- **N303** — reseg-367-4961-bound NULL: the boundary unfired;
  3 follow-ups (name 49 via "49 74"×5, 70-as-abbreviation, the gated
  61pre letter-tier).
- **N304** — seg-08-ier-61 NULL: no window forces a falsehood about
  08's class.
- **N305** — stem-85-then-1700 NULL: a self-gating bar, gate closed —
  stem-85 has not named 85's value.
- **N306** — tail-89-16 NULL: the trigger is unresolved; fence
  executed.
- **N307** — tense-24-307 NULL: the bar's gating clause fails — 24 is
  unresolved at standing (a section-5 escalation candidate).
- **N308** — val-38-verb NULL: 38's verb narrowed to
  {"vouloir","devoir"} — "vouloir" is the parsimony lead.
- **N309** — val-42-estframes NULL: 42's value underdetermined — the
  kill arm's condition ("no value parses") is false.
- **N310** — val-65-1204-rightedge NULL: the naming bar is
  unsatisfiable — the @1204 right edge admits an open class of French
  nouns.
- **N311** — val-97-verb-test NULL: INF/NOM tie; FIN-97 killed; the
  class-naming condition unmet.
- **N312** — valency-56-wide NULL: valency cannot discriminate the
  Xeent candidates at any window — the 8-way tie stands.
- **N313** — verb56-register-closeout NULL: the register venue is
  closed — yield is one kill (réer) plus the fenced 8-way tie.
- **N315** — 15-noun-verify NULL: at @1696 the plural noun claim dies
  at class level — "ne [15] [33]" @775 and "pas [15] [01]" @1730 are
  canonical adverb slots, zero determiner-adjacent bigrams in 10
  windows; §7 bars any adverb/noun split. R1 @1495 ("[66] [15]
  [59='est']") keeps a live "en"/"y" pronoun rival fenced as a
  window-level residual. Delivers to the 58-det-numeral-tension
  docket: frame B of `58-value-name` loses its licensing leg.
- **N316** — 15-value-id NULL: 'encore' killed (0 genuine "ne encore +
  V" in 31,664,431 chars; 3 raw hits = substrings of
  "règne"/"jeune"/"me répugne"); 'jamais' killed (0 occurrences);
  'plus' survives but cannot be named (needs 01's class, n(01)=28,
  open; needs 41's value, unvalued). Pronoun rival ('en'/'y') KILLED
  as 15's global value (clitic order forces elision to "n'en").
- **N317** — bound-1132-modal-edge NULL: 24's value at @1132 unnamed
  (R24 grants class only); even a named value would not fix the right
  edge, because modal + clitic + governed infinitive binds 86 into the
  clause and 20 remains licensable as a clause-final adverb ("…le
  laisser ainsi"-shaped, queued as `adv-1135-leftward`).
- **N318** — ceci-correlative-corpus NULL: exact "ce qui par" = 3 in
  31,664,431 chars of `code/side-period/corpus` (2 finite-verb
  relatives, 1 c'est-cleft — all excluded); generosity
  "qui par"+ceci ≤600 chars = 0. Confirmed zero hardens the
  `leftedge-1024-43-governor` fence (census:
  `code/crowd17/next-token/ceci-correlative_census.json`,
  `ceci-correlative_generosity.json`). Comedy-register check queued.
- **N319** — 31-08-word-host NULL: the [08][31] host-class gate is
  licensed (complete two-cell word in all 3 windows) but the word is
  unnameable at battery grade (≤1 ungranted assumption allowed; needs
  ≥2: 08's letter + 31's spelling value). "ce [08][31]" @1488 demands
  a nominal/adjectival word while 31's banked class is VERBAL —
  recorded as non-contradiction (nominal word can contain a
  verbal-shaped syllable) for the naming battery.
- **N320** — dwindow-voisin-family NULL: 0/26 D-windows parse a
  'vois-'-prefixed word with a named neighbor value (n(86)=32;
  named followers ne/pre/ver/par/e/n/noun-class/verb-class compose
  non-words). Not dead — re-opens on any follower value named to
  "in"/"ine"/"ins"/"ines" (candidates 56×4, 52, 01, 66, 24, 21, 91,
  16, 20, 44, 50, 67, 71).
- **N321** — inf89-letter-interior NULL: no interior letter of the
  "[89]e" word is nameable with byte evidence (89 census n=14;
  "29 89 48" trigram 0× stream-wide; only letter-tier neighbors 48
  word-final and 29 §7-barred-as-interior). Re-open routes queued:
  `inf89-er89-boundary`, `word89e-right-bound`,
  `inf89-rerun-77gate`.
- **N322** — inf97-526-vs-567 NULL: the joint class test is undecidable
  at battery grade — W1 @526 parses under nominal-97 but W2 @567 is
  blocked by 13's ungranted class (13 unvalued in the registry), not
  by anything about 97. Follow-up `val-13-567` (P3) is the direct
  blocker. INF/NOM tie survives.
- **N323** — lex-52-deinf-register NULL: the tie-break route is closed
  at battery grade — "prescrira" 0, "prévoira" 0, "préserva" 1 (de +
  noun, not +INF) in 32,547,082 chars; lemma-level de+INF count 0/0/0
  for all three candidates ("préserver de" ×7, all de+noun). Register
  cannot discriminate the 52 candidates. Corpus zeros do not falsify
  the lexicon-level de+INF government claims.
- **N324** — locus-368-fullparse NULL: 8 parse routes at @362–375 all
  fail (cheapest needs 49 + 61 named + "pre fois" adjacency licensed =
  ≥3 ungranted assumptions vs budget ≤1); no finite verb exists in the
  window. Fenced as undecidable-at-battery-grade, stated cause:
  unresolvable "48 49 61" trigram, unlicensed "pre fois" adjacency.
  Naming 49/61/85 could revive routes 3–4.
- **N325** — neque-verb-slot-wide NULL: the verb slot is empty in 15/16
  '94…46' brackets — but W03 (94@161 → 46@217) is a genuine exception
  (24@162 finite/modal per R24), so the systematic-residual fence
  cannot fire. The family is undecided, not killed. Regenerates
  `neque-W3-parse` (P3), `neque-15slot-fence` (P3),
  `val-24-162-modal` (P4).
- **N326** — qui-38-608-aqui NULL: the "à qui" shape is grammatical,
  but both antecedents are unnameable at battery grade (@26–@36 span
  holds no noun-class cell; @608's left neighbor is another qui,
  fenced by the a-39 adverse). Follow-ups `ant-91-36-noun`,
  `ant-54-605-noun`, `wordbound-39-607` queued.
- **N327** — mentent-580-rival KILL: the "ne mentent" (3pl of
  *mentir*) rival segmentation of "94 82 06 06" is forced false at
  battery grade at both Frame A windows — no 3pl subject licensed;
  preverbal slots positively filled by singular determiners (87='ce',
  45='ce'); French is non-pro-drop. Kills only the rival clause
  parse; 06="ent" (R17-007), 94="ne" (R19-167), 82='m' untouched.
- **N328** — mentent-w2-killseek KILL: 12-rescue audit at @1182–1187
  ("ne mentent est [42]") finds no grammatical rescue (subject,
  noun, segmentation, clitic, mood, downstream-24, value-challenge
  families all dead). Kills only the W2 "ne mentent" one-word rival
  parse; consistent with `nementent-W2-subject` PROMOTE.
- **N329** — modal-80-license KILL: the modal-80 arm is dead at
  battery grade — 17/17 80-windows fail (16 on follower class: zero
  infinitive-shaped followers; @565 on adjacent-finite conflict).
  Consequence: the INF reading at @567 is killed; the @567 question
  reduces to the NOM arm plus 13's class. 80's split is red-team
  venue (`poly-80-docket`, untouched).

### Round-17 null batch, wave-16 arrivals (crowd17, 2026-10-09 UTC —
10 notes: 6 nulls, 1 kill, 3 promotes (folded as F228–F230 in
section 4); battery grade)

- **N330** — fin-88-730-rerun NULL (fence executed): 88's finiteness at
  @730 is undecidable at battery grade. C1 fails (88=inf needs a
  licensed governor; the cheapest route costs 2 ungranted assumptions:
  the T3 boundary reading of the 48-88 contact plus 86=modal). C2
  fails/moot (88=finite needs a licensed subject; no subject survives —
  the red team already exhausted the rescues at @732, and an
  ungoverned 88=inf would not join the governed-infinitive population
  anyway). Neither arm fires → NULL per protocol. New lead, not a
  finding: IF 86='entr', all three 86 shapes converge ("pour entrer"
  ×12, "entrer" ×4, "entre[88]" ×1) and 88 goes word-internal —
  dissolving the finiteness question at @730 entirely (1 ungranted
  assumption). 'la' at @731: as article, dead ('en' follows, not a
  noun); as "l'en" clitic, needs a verbal host (85 open) — recorded,
  feeds objpron-88-77-11. Follow-ups: val-86-728-entr (P3),
  gov-88-730-modal (P4, gated), subj-88-730 (P3).
- **N331** — noun-74-formula NULL: no French nominal/formula frame
  parses the four '49 74 74 [46/47/48/40]' chains (W1–W4 at
  @416/@815/@860/@918, byte-exact). The '74 74' doubling (×6) kills any
  whole-word nominal head at kill grade; the four chains vary on both
  edges (right followers que/ce/e/e; left contexts differ), so no fixed
  formula frame covers them; naming a frame would invent a value for 49
  or 74 (§3). The kill arm does NOT fire: 0/34 74-windows show
  verb-frame contact under the lane's distributional standard (test set
  {80, 89, 29, 85, 33}). Two subject-contact windows (@261 "on 74",
  @1500 "74 on [INF]") are recorded as the lead follow-up — that target
  lands as N335 below. Follow-ups: subj-74-261-1500 (fired),
  formula-49-value (fired), chain-follower-class (P4, queued).
- **N332** — objpron-88-77-11 NULL (fence executed): the uniform
  verb+clitic-pronoun rival across the '88 77'/'88 11' population
  (n(88)=23; '88 77' ×3 at @86/@646/@1541; '88 11' ×2 at @730/@1514) is
  fenced as inconsistent. Kill-grade failures: @646 (78 nominal in all
  standing uses — no verb host for proclitic "le"), @1541 (same 78
  ground, reinforced by the adopted "Il [93-fin] [88-inf] le [78]"
  frame), @1514 (31=VERBAL gives "la" a host but the trailing "la [91]"
  forces a double-direct-object violation; all rescues dead or
  over-budget). Fenced: @86 (66 unvalued — the pronoun leg needs an
  invented 66=verb). The one survival: @730 "la en" — a correctly
  ordered clitic cluster preceding 85 (standing en85 proclitic host) —
  CONDITIONAL on 88's finiteness and 93's role. That leg is now F230 in
  section 4 above. Follow-ups: pron730-clause-wide (fired → PROMOTE),
  val-66-87-verb (P3, queued), pron1514-dislocation-corpus (P4, queued).
- **N333** — formula-49-value NULL (fence executed): n(49)=12, no class
  nameable at battery grade. Verb-49, determiner-49, and
  relative/interrogative-pronoun-49 are all DEAD at kill grade (the
  byte-identical "76 49 24 26 30 03" ×2 frame at @652/@989 kills verb and
  determiner; "49 qui" at @909/@1433 kills the pronoun). Adverb and noun
  are strained, not nameable. Best surviving leg: adjective — canonical
  post-nominal position in the ×2 frame — but the hostile windows @366
  ("48(e) 49 61": nothing for the adjective to modify) and @420
  ("46(que) 49 [36-noun]": adjective before a bare noun is ungrammatical)
  cost 2+ rescues — over budget. The '49 74 74' chain parse stays
  locked: it needs 49 named (failed) AND the '74 74' doubling resolved
  (`unit-49-74-74`, queued). Follow-ups: adj-49-420-366 (fired → KILL,
  adjective-49 dead at kill grade — this is the basis of the R20-080
  override below), formula-76-49-24 (fired → battery PROMOTE, then
  overridden to FENCE by the red team; see R20-080), noun-49-909-875
  (P4, queued).
- **N334** — tonic-pronoun-stream-locate NULL (fence executed): the
  stream is fenced as tonicless at battery grade — no unvalued group is
  locatable as a personal-tonic-pronoun candidate
  (moi/toi/lui/elle/nous/vous/eux inventory) under standing values.
  Determiner-exclusion removes 86 (8 determiner predecessors; kill
  grade), 92 (3× after 11="la"; kill grade), 33 (2× after 47="ce"; kill
  grade), and 66 at battery grade (1× after 77="le" @88, plus the
  hostile @189 "pour [66] [V-fin]"); zero "00 X INF" windows
  stream-wide except @714 ("00 66 86" — X=66, already excluded). The
  5-signature census, the exclusion table, and the gloss gap (the
  manuscript pencil gloss anchors only "la premiere" and "que" — no
  pronoun gloss exists) are packaged as `redteam-tonic-fence-input`
  (P2, queued). Scope: no GROUP is locatable — this does not claim the
  French text lacks pronouns. 84="on" is adopted as premise, not a
  candidate. Gated follow-up: tonic-66-rearm (P4, queued).
- **N335** — subj-74-261-1500 KILL (battery grade): the nominal/formula
  hypothesis for 74 is KILLED. A15's 'on' conditions C1–C3 all hold at
  both subject-contact windows (7 77→84 elision legs re-verified
  stream-wide incl. @260; @1501's successor graded NO-CONTRADICTION),
  so 'on' is licensed at @260 and @1501, and 74 sits in the finite-verb
  slot in both frames: predecessor-side "on(84) 74" at @261 (the only
  84→74 bigram of 25 84-windows) and inversion-side "74 on(84) [33-INF]"
  at @1500 (the only 74→84 bigram of 34 74-windows). A whole-word noun
  or formula cannot occupy those slots in French. Scope: NOT a verb
  promotion for 74 — 74's class stays open at battery grade (promotions
  are red-team-ratified only); the standing ne-alone-02-74 kill is not
  re-litigated (different windows, different test). Residual tension
  (red-team venue): the '74 74' doubling family (×6) independently
  contradicts whole-word verb-74 at kill grade — a wholesale verb
  reading would need a red-team polyvalence ruling. §7 intact.

---

### Round-17 null/kill batch, backlog fold 2 (crowd17, 2026-10-09 UTC —
34 notes: 7 kills, 27 nulls; battery grade)

- **N336** — prefix-productivity-08 KILL: the "08-65 = prefixed verb stem"
  claim dies at kill grade. "08 65" ×2 (@922, @1339) needed 65 verb-shaped;
  battery-prof-65 PROMOTED 65=noun and red team GRANTED it (R20-047,
  registry "65 stays ['noun','cls']") — and @1339 itself reads "08 65 qui":
  a verb cannot antecede "qui", so the promote arm's own locus window kills
  the verb-65 reading. No other 08 successor is verb-shaped (n(08)=18:
  31 ×3, 65 ×2, 62 ×2 pronominal; singletons are letters, full words, or
  nominals). The 31-only prefix attachment stays a stipulation; sibling
  battery-prof-65 adopted, not re-litigated.
- **N337** — reseg-13-armB KILL: the universal "same leftward nominal-closing
  13 re-segments all 7 arm-B windows" dies at kill grade — at @481/@575/@1166
  the left neighbor is "pour" (00, A9) or "ce" (45, A11), to which no nominal
  suffix can attach (3 hard fails + 3 strong + 1 conditional of 7 windows;
  n(13)=12, byte-exact "65 13 66 14" ×2 stream-wide). The kill lands via the
  bar's clause 1, not the pre-registered word-level falsifier. A narrowed
  4-window suffix venue survives; an R20-106 counting note ("does not count
  92 as verb-class") is flagged for the red team.
- **N338** — reseg-1564-26pas KILL: the "26 30" = one-French-word "Xpas" arm
  dies on gender, not spelling. "26 30" ×4 genuine in-row (@655/@992/@1250/
  @1560; n(26)=17, n(30)=19); French -pas words {pas, repas, trépas, appas,
  compas} are all masculine, but @1560 "fois la Xpas" (11=la GT, 17=fois)
  forces a feminine noun — no X satisfies — and @1250 "que Xpas" (46=que GT)
  is an unlicensed determiner-less subject. The arm is dead, not merely
  fenced. 26's noun lead untouched.
- **N339** — split-13-secondleft KILL: the -2-slot value-disjointness between
  the 5 arm-A windows (@68/@822/@1381/@1554/@1684) and the 7 arm-B 13-windows
  dissolves as coincidence — exact permutation test over C(12,5)=792
  labelings gives p=0.222; at n=12 over 96 types, disjoint slots are ordinary
  (a 1-in-4.5 draw). The parent's recorded lead was a small-n artifact; the
  5/7 distributional split survives as observed fact, and the red-team
  second-polyvalence package is untouched.
- **N340** — val-39-class-census KILL (verb-39 arm only): the bar wanted ≥2
  independent verb-frame legs for verb-39; zero existed (n(39)=13). Four
  windows force 39 non-verb at kill grade: @37 "39 qui" (granted 64="qui"
  makes verb + relative "qui" ungrammatical — the strongest leg, built on a
  granted value), @764 adjacent verbs, @1068/@1605 "pre[39]" bound-syllable.
  39's class stays open: nominal-39 is forced at @37 (F262), syllable-tier
  39 in "pre[39]" ×2. R17-005 (39=/a/ LEAD, R20-010 confirmed) untouched;
  Route E at @609 does not re-open.
- **N341** — det-77-86-substantivized KILL (determiner-77 at battery grade):
  the "last stand" claim — 77 governs a substantivized infinitive 86 at the
  five '77 86' windows (@430/@798/@877/@950/@1133) — closes. 1/5 parses
  cleanly (@430, "le [stem]er"-shaped); @950 fails at kill grade — the banked
  follower 96='par' (granted) proves the infinitive ending absent, not merely
  unknown, and a nominalized infinitive cannot take "par ce que" as
  complement. With 0/44 nominal followers of 77 stream-wide, determiner-77
  closes per the pre-registered fail clause. The 'le' value survives
  provisional via the clitic arm (objpron-77-89 queued); the @430 leg is
  fenced with cause for future re-opening. Awaits red-team ratification.
- **N342** — prof-43-rerun-polyvalence KILL ('43 81'-NP sub-claim only): '43 81'
  ×1 (hapax @43); 43's 16-occurrence follower census has zero nominal-class
  followers; no 'ne' (94) within ±8 pairs of @43; 81's only licensed NP
  template is 'le 81'. Gate verified: R19-064/R20-117 43=["noun","cls"] —
  and the kill respects that grant (a noun need not form an NP with 81),
  closing the NP arm and the ne-drop arm that depended on it. The
  seg-81-30-boundary C2 arm closure follows.

- **N343** — inf-03-91-complement NULL: fence at @722–723. C1 failed (03's
  verb-stem value unnamable; R20 deferred the 03/71 split; local "77 03" is
  determiner geometry); C2 failed (n(91)=21, scattered predecessors/followers
  — no class signature; "03 91" is a stream hapax, 1/1847). The
  verb-complement arm is closed at this locus only. 03's genuine
  infinitive-shape legs ("03 29" Xer at @1030/@1320/@1594) do not transfer
  here and are untouched.
- **N344** — noun-91-det-frames NULL: the DET-window naming claim for 91 is
  fenced. n(91)=21; exactly 3 "DET 91" windows (@15, @1005, @1518); only
  @1518 ("11 91" = "la [N] et…") parses cleanly — below the bar's ≥2
  threshold. @15/@1005 strained but not kill-grade contradictions. The fence
  stays narrow: strain is not contradiction. R19-164's locus grant (91 = past
  participle at @538/@1371) untouched; 91's class stays open.
- **N345** — noun-91-nondet-windows NULL: fenced at @277/@520. @277 ("on [91]
  [37-pred]"): subject "on" forces a finite verb — kill-grade contradiction
  of nominal-91, and the window affirmatively favors verb-shaped 91 (battery
  claim, not adjudicated — see §6). @520 ("70 91"): bound "pre" makes one
  word, blocking standalone-word 91. Both hostile bigrams are hapaxes
  ("70 91" ×1 @519, "84 91" ×1 @276).
- **N346** — personal-tonic-governed-interr-prose NULL: the interrogative-force
  variant closes in prose at battery grade. 53 candidates (35 strict + 18
  loose-only), all hand-read ±700 chars: 0 genuine. Corpus gate: 20 files,
  27,656,185 chars, 4,495 pronoun-comma hits (parent's counts); census
  script `code/crowd17/next-token/personal_tonic_governed_interr_prose_
  census.py`. Nearest misses are near: e.g. "ai-je craint, moi, de me
  compromettre?" has a true dislocated topic but the "?" force lands on the
  finite verb, not the infinitive. Drama-register variant stays open
  (follow-up proposed).
- **N347** — procreer-absolute-corpus NULL: period-diplomatic French (77 files,
  ~34.5M chars, `code/side-period/corpus`): 5 procréer-stem tokens in 4
  files; 3 verb tokens, 3/3 transitive, 0 absolute. The near-miss
  (Metternich's "ce que le temps seul sait procreer") collapses on
  hand-parse: "ce que" supplies the object. Littré's absolute-use record
  stands as a dictionary record, not a period diplomatic attestation (its
  citations are undated). The @1745 8-way Xéent tie must be re-scored
  without the Littré-absolute advantage (follow-up
  procreer-56-semantic-reweight).
- **N348** — qui-predicate-87-census NULL: @1775 fenced as the sole licensor
  of the "ce qui" + predicate frame. 5 "87 64" windows; exactly 1 licenses
  (@1776 "ce qui est" via provisional 59=est); the other 4 are fenced, not
  killed (@149 follower 96=par; @181 follower 23, no value; @1768 follower
  26, no value; @1801 follower 77=le*, ungrammatical). Battery-grade fence;
  59=est* used as provisional license only.
- **N349** — reinforced-head-narrative-uncapped-drama NULL: the deep-narrative
  recall gap closes. 14-play drama corpus (2,969,582 chars) re-run with
  punctuation-aware uncapped windows: Pass B reproduces the parent exactly
  (41 dem hits; exactly 1 window uncapped at 400 — dumas-tour-de-nesle @79885,
  resolved at 415 chars, a narrative récit passage, no candidate); Pass C
  adds 0 new candidates; 3 windows hand-classified, 0 genuine. Nothing was
  hiding past the cap. (Drama register; prose/comedy uncapped recalls are
  separate follow-ups.)
- **N350** — reinforced-head-topology-drama NULL (map deliverable): 41/41
  dem-comma windows in the 14-play drama corpus (2,939,372 chars)
  hand-classified into 9 resolution classes (A copular/cleft 13; B clitic
  resumption finite 6; C clitic resumption + infinitive complement 3; D
  finite anaphoric 8; E verbless appositive/NP 4; F colon/vocative 2; G
  relative 2; H adjectival apposition + exclamation 1; I verbless deictic
  2); 0/41 show a reinforced head governing an infinitive — the reversal is
  that government runs the wrong way: heads co-occur with governed
  infinitives only as the infinitive's (resumed) object, never as governors.
  This is why N350 rejects F268's fence wording — see the §6 rephrase item.
- **N351** — reinforced-modal-inf-prose NULL: 20-file 19th-c. prose corpus
  (27,656,185 chars); 231 reinforced-demonstrative-comma hits → 2
  modal/perception-inf candidates → 0 genuine (both were one regex re-match
  inside a single nesselrode-v8 passage; heads were objects of "l'intimité
  de", "penser" under finite "on a (vite) fait"). Cross-register:
  2 candidates / ~30.6M chars / 0 genuine (drama parent: 0 in 2,939,372).
  Per the sibling zero-yield convention, a confirmed zero is an absence,
  not a kill.
- **N352** — reseg-13-rightward NULL: rightward attachment fenced at
  @481/@575/@1166 (byte-confirmed; "45 13 55" byte-same ×2 at @575/@1166).
  Naming needs standing content for 13 AND 52/55; 13='les' is killed,
  13='que' is §7-blocked, 52/55 class-open — every French candidate needs
  new assumptions, and the bar allowed zero. The three loci are now
  double-fenced (leftward killed N337, rightward unfenceable-until-named);
  the blocker is structural and identical at all three windows — a
  deterministic failure, not a close call.
- **N353** — seg-41-08-leftedge NULL: budget fence at @59. The "41 08" onset
  claim (feeding the "ière" tail: 34='i', 29='er', 40='e' GT) needs 41's
  letter + 08's letter — 2 new assumptions; the bar allowed ≤1. Both cells
  registry-open (`code/table-grid/table-registry.json`); n(41)=19, n(08)=18;
  @60–61 "08 34" is a hapax. The failure is a budget failure, not an
  evidence failure — the standing-value inventory simply cannot pay for it
  yet. @59 stays fenced residual.
- **N354** — seg-77-03-722 NULL: triple-arm locus fence at @722 ("77 03" is a
  stream hapax, 1/1847; n(77)=44). Nominal-03, nominalized infinitive, and
  word-boundary rival all need ≥1 new assumption; none is forced and none is
  kill-grade contradicted. A clean three-way fence — zero discrimination
  added, defers entirely to the queued 03 batteries (val-03-noun,
  val-03-value-census). Pairs with N343's @722–723 verb-complement fence.
- **N355** — temp-65-loc-census NULL (TERMINAL fence at @512): 65 is
  noun-class (R20-047 GRANT) and 98="vient" lead, but bare temporal/locative
  nouns cannot follow "venir" in 1841 French — the barrier is grammatical,
  so no future 65-value naming can re-open @512. Corpus: 2,636 vient+X hits
  in `code/side-period/corpus`, 0 bare temporal/locative nouns. n(65)=25
  all listed ±4 context; `98 65` hapax (1/1847), "24 65" ×2, "29 40 65" ×3.
- **N356** — val-02-prep-sweep NULL: preposition-02 fenced stream-wide.
  n(02)=17; 0/17 windows license a preposition value with zero new
  assumptions; 8 kill-grade hostile (@495/@609/@695/@750/@858/@887/@1152/
  @1299 — e.g. "qui [prep]" after granted 64="qui" is ungrammatical). This is
  not a class kill: @1084 ("24-V [02] 55") could re-open if 55's class names
  favorably later. The parent's left-88-02-88-307 prepositional arm stays
  closed.
- **N357** — val-03-noun NULL (epistemic, not evidential): the bar assumed
  candidate lexemes existed for noun-03; the inventory was empty — an
  exhaustive inbox sweep found exactly one ever-proposed 03 lexeme ("re-",
  killed at kill grade in battery-re-prefix-03-665), and it failed all six
  forced-nominal windows (@336/@674/@1645/@1014/@1790/@722). Nothing was
  tested; this proves nothing about noun-03's value. R19-180 (stem-03
  GRANT) stands; the 03/71 §7 split stays red-team venue. Missing
  prerequisite: 03's letter content (@1237 "[10] [03]e" is the only
  letter-adjacent window).
- **N358** — val-31-verb-test NULL: the 3-leg verb-class bar fails at 2/3.
  The two "qui [31]" legs (@338/@1647; n(31)=8; "64 31" ×2) license
  finite-verb 31 with zero new assumptions — but the "31 29" stem leg
  (@1257, hapax) needs an ungranted infinitive governor or an ungranted noun
  parse. The battery fences honestly rather than trimming the bar to the
  two legs that passed. The two finite legs stand at battery grade as
  red-team input material; the joint 3-leg verb-class establishment is not
  earned.
- **N359** — val-41-letter-census NULL: letter-cell-41 fenced. n(41)=19; the
  adjacency scan is absolute: 0 windows put 41 next to a banked GT letter
  cell {70, 82, 34, 29, 40, 46}. "41 41" @589/@590 non-discriminating. The
  @59 letter-shaped window was already fenced residual (N353); word-cell
  legs are abundant and clean (@39 "qui [41]", @808/@1016 "en [41]"). Only
  the letter arm is fenced; word-cell-41 and the §7 split (R20-108/R20-082)
  are untouched and stay red-team venue.
- **N360** — val-49-74-frame NULL: the naming claim at the five "49 74"
  windows (@416/@815/@860/@918/@1844) is fenced. The blocker is structural,
  not value-specific: '74 74' doubling ×6 kills any whole-word parse of the
  chains at kill grade, and licensing 74 at sub-word tier would be a new
  assumption — so the bar was untestable-as-satisfiable; the battery fences
  anyway rather than inventing assumptions. Standing fences unchanged;
  `unit-49-74-74` (the sub-word reading) stays queued.
- **N361** — val-85-narrow NULL: n(85)=15; 6 A3 legs re-derived (5 "24-85"
  @732/@955/@1438/@1693/@1754 + 1 "46-29-85"); neither surviving candidate
  is named nor killed. 'laisser' stays LEAD (gated on 16's class and 33's
  tie, outside these legs); 'contredire' stays compound, red-team venue.
  The 4 clean "en [85]" gerunds select the -er class, not a value. Note:
  the legs kill global-'contre' ("en contre" ungrammatical) at kill grade —
  but global-'contre' was never the live claim, so it is a kill of a
  phantom while the real locus-compound survives untouched.
- **N362** — plus-jamais-tiebreak NULL: 52='plus' vs 'jamais' fenced as
  unbreakable at battery grade. Three ne-frame windows (@1293–1296
  `94 52 80 04`; @1735–1739 `60 12 48 52 86`; @1806–1809 byte-identical to
  W1); all three promised selector values are missing — 80's value open
  (red-team venue), 86's value never named (R20-087 class grant only), 60
  unnameable at @1735 (KILL). Naming either value would be an arbitrary
  coin-flip. 52='pas' stays BLOCKED. Anti-gate: the three gated re-runs must
  key on a red-team value GRANT, not a battery promote (gate rule
  2026-10-09).
- **N363** — qui-fol-23-26-value NULL (§5.2 escalation — genuine, not a
  stalemate): copula/verb value CARRIES for 23 (3 legs: @182/@679 copula,
  @1609 finite) and 26 (8 legs: @155/@406/@934/@1628 finite; @531/@1769
  copula; @601 verb; @842 ne-verb; n(23)=8, n(26)=17) — but the only
  nameable value the legs support is "est", which collides with provisional
  59=est under §7's sole-polyvalence rule. Naming "est" without a red-team
  polyvalence/homophony grant would overwrite standing verdicts; any other
  verb value would be invention. Blocker is jurisdictional, not evidential.
  The 23~26 split holds; reseg-1564-26pas's kills at @655/@992/@1250/@1560
  (N338) are honored, not re-litigated. Two 1690 frequency-uniformity
  gathers + one red-team input package proposed.
- **N364** — tail-385-rerun-43poly NULL: the @385 re-anchor fences with
  stated cause. The gate premise cleared (R20-117: 43=["noun","cls"]), but
  the anchor needed ≥2 independent legs and only one exists: "37 43" ×3
  (@385/@1125/@1723), and @1125/@1723 sit inside the la-vote windows
  themselves — circular as legs. The la-vote stays unanchored. S5 tension
  escalated: under 37="le" (MEDIUM), @385 reads "52 38 le [43-noun]",
  directly contradicting the anchor's adjectival reading — red-team venue
  (follow-up s5-37-385-adjudicate, P2).
- **N365** — val-31-1257-word NULL: "[31]er" at @1257 — infinitive and noun
  arms fenced (no licensed governor or nominal parse under standing values;
  both would need an ungranted §7 polyvalence against 31's finite-verb legs
  at @338/@1647); the word-internal arm is unfenceable at kill grade
  ("61 31" hapax, no discriminating evidence). n(31)=8; "31 29" hapax
  @1257. Enlightenment: all three arms shared an unexamined "[31]er"
  word-shape presupposition — follow-up `locus-1257-reseg` tests the "31 |
  29" re-segmentation. Poly-31 docket item to the red team.
- **N366** — verb-slot-62-1686-neque NULL: the @1686 verb slot fences as
  genuine residual. Exactly 2 bracket geometries stream-wide (@100, @1686);
  all 9 "62 94" loci censused; the @1686 span `62 94 79 14 60 27 46` holds no
  licensed finite verb (79/14 non-verbal; 60/27 no licensed verb value; the
  only licensed finite-verb value is provisional 59="est", absent within 24
  pairs). Window-local, not geometry-wide: @100's bracket contains licensed
  59="est". The frame itself is conditional on ungranted 94="ne" (strong
  lead — R17-001 promote REJECTED), and 62="il" stays KILLED (R19-106,
  R20-125). Arms a future gate (neque-94lead-gate, P4): re-open only when
  94='ne' moves lead→grant at red-team level.
- **N367** — wordinternal-41-census NULL (census-only, no class decision):
  n(41)=19 across 17 rows; 0 immediate GT-letter neighbors in any window
  (closest at distance 2: @59 "41 08 34", @1048 "41 88 29", @237 "70 98
  41"); word-unit framing in 7 windows; a 6-window "pour"-proximal cluster;
  "41 41" @589–590. Composition evidence exists but at arm's length —
  letter-tier decided against on current evidence, class claim not made;
  everything routes to the split-41-redteam docket. Pairs with F274/F275
  (locus claims) and N359 (letter fence).

- **N368** — ne-508-reseg-gate62 NULL (§5.2 contradiction — the gate's claim
  is REJECTED): the dispatch brief said "run now with 62='il'", but 62='il'
  is KILLED at kill grade, permanent — R19-097 REJECTED the very battery
  promote the gate had verified as "satisfied" (2026-10-08), and R20-125
  confirmed the kill. Per the gate rule, a battery promote the red team
  rejected does NOT satisfy a gate trigger — the worker correctly refused to
  run the re-test and did not overwrite standing verdicts. Byte verification
  confirms @507–509 = 77, 62, 94 (row a3_00; '62 94' ×9 stream-wide,
  n(62)=35, n(94)=37). The else-arm outcome is already the standing state:
  @508 is a fenced residual (N52; R20-125 "@508 unclean"), and the
  distributional-only fence on '62 94' = subject+'ne' is HARDENED. Follow-up
  `ne-508-reseg-rearm` (P3) arms only on a red-team 62-value grant.
- **N369** — verdict78-gate-wordbound-rearm NULL (gate untestable-as-written —
  no gate satisfied): the six trigger returns are leg-gains and arm-kills,
  not a change in 78's status. Promotes: ver78-ce78-census,
  ver78-flagship-1181-1352, ver78-1670-5581 (leg frames), and
  ver78-non45-positive-leg (@819 'ce verre' on banked/granted values only —
  breaks 78↔45 mutual conditionality from the 78 side; its own adverse bars
  a global promote from legs). Kills: ver78-65-completion,
  ver78-ce78-open-succ (killed ver-word COMPLETION arms, not 78='ver').
  Round 20: 78='ver' DEFERRED (R16-005 LEAD stands). Neither bar clause can
  fire: clause (a)'s antecedent (78='ver' promotes) is false; clause (b)'s
  (ver-78 kills 78='ver') is false. Recorded state: 78-45 loci unchanged
  (@313/@573/@982/@1164, n(78)=31); W2-W4 one-word boundary stands;
  the 'verdict' arm survives — strictly stronger via the R20-banked @819
  leg but still conditional; W1/A11 @314 corroborated, not flipped
  (dict-313-w1-adjudicate promote stands). R16-005 LEAD respected; no
  promote of 78='ver' or 'verdict' made or implied. Future re-arms should
  key on red-team resolution of 78='ver', not battery leg returns.

**Cross-battery conflict noted (for §6):** reinforced-pour-inf-interro's
fence wording ("reinforced heads govern infinitives…") is rejected by
reinforced-head-topology-drama (N350) — 0/41 head-as-governor windows. The
widercorpus promote (F269) and the topology null are mutually consistent
(presence/absence, no wording conflict). Also: 41-05-class (F274) corrects
val-41-word-census's same-day "STANDALONE forced" judgment — a worker
judgment, corrected with cause, not a standing. reseg-13-armB (N337) flags
an R20-106 counting note for the red team (92 not counted verb-class) —
observation, not contradiction. Nothing here contradicts a standing
red-team verdict or §7.

### Round-17 null/kill batch, backlog fold 3 (crowd17, 2026-10-09 UTC —
7 notes: 0 kills, 7 nulls; battery grade)

- **N370** — 62-regne-trone-final NULL: the règne/trône tie is not broken
  at battery grade. Exact head frames are zero for both candidates in
  34,551,456 chars of 1841-register French (`code/side-period/corpus/`,
  accent-insensitive): "et le trone qui" ×0, "et le regne qui" ×0,
  "le trone qui vient" ×0, "le regne qui vient" ×0. The sub-frames split:
  "et le [W]" → trône 3v0 ("et le trone" ×3, all genuine, genre-matched;
  "et le regne" ×0); "[W] qui vient" → règne (1 attestation, "regne
  vient de commencer en france", found only via a double-space OCR
  artifact — re-weighing the same evidence is not new evidence).
  35-window 62-94 census re-derived byte-exact; all 8 non-508 windows
  (@100/@761/@840/@1329/@1362/@1686/@1704/@1772) tested, none
  discriminates. Locus bytes @506–511 (row a3_00): "67 77 62 94 64 98".
  Naming règne would contradict the standing w508-noun-ne "trône" battery
  promote — §5 bars the downgrade; no new value is named. Follow-up
  proposed: redteam-508-reread (red-team escalation package, no gate
  claim).

- **N371** — reinforced-head-governed-topology-drama NULL: the parent map
  is reproduced 41/41 and the fence hardens. 14-play drama corpus,
  2,939,372 chars; the 41 dem-comma windows re-classified into the 9
  resolution classes (A copular/cleft 13; B clitic resumption finite 6;
  C clitic resumption + infinitive complement 3; D finite anaphoric 8;
  E verbless appositive/NP 4; F colon/vocative 2; G relative 2;
  H adjectival apposition + exclamation 1; I verbless deictic 2); 15/15
  spot-checks confirm the parent's assignments. Full-turn audit (no '!'
  filter, no 180-char cap): 11/41 turns contain '!', 0/41 show a
  reinforced head heading an exclamatory infinitive. Dash/paren
  recall-gap extension: 0 hits corpus-wide. New observation at idx 38
  ("pour être ma maîtresse !", verre-d-eau @36952): a genuine governed
  exclamatory infinitive with subject "je" (the Queen), no anaphoric link
  to "ceux-là" — drama HAS the construction; it just never takes a
  reinforced-demonstrative topic. Fence boundary: prose 0/27.66M +
  drama 0/2.94M. F268's wording still needs the rephrase recorded in
  backlog fold 2.

- **N372** — val-01-rival-sweep NULL ('ein' killed at kill grade within):
  15 @-offsets tested (@195/@255/@327/@409/@484/@717/@940/@1255/@1261/
  @1440/@1462/@1634/@1653/@1731/@1818) against a 33.6M-char French
  corpus (German files excluded). 'ein': 0 genuine French word-initial
  attestations ("ein" 9×, "eine" 5× are German fragments/OCR noise);
  word-initial 01 at @195/@1255/@1462 (+@484 supporting, 30=pas LEAD)
  kills 'ein' at kill grade — the kill is positional, not global
  ('peine' 1,554×, 'reine', 'plein' word-internal). 'ain' (via "ainsi"
  3,816×), 'in', 'an' survive with zero kill-grade contradictions but
  are not positively parsed → fenced; re-open when right-neighbors 21/61
  are valued. Note: the bar's own count was off (14 stated vs 15 listed
  offsets) — all 15 were tested anyway.

- **N373** — val-31-1257-word NULL (partial fence): n(31)=8; "31 29" ×1
  @1257, "61 31" ×1 @1256–1257, both stream hapaxes. Locus bytes
  @1248–1267 (row a7_02): "67 46 26 30 06 65 46 01 61 [31] 29 69 88 01
  09 11 50 46 69 88". The infinitive arm is fenced (no licensed
  governor: 61/01 unvalued, 46='que' takes finite clauses) and the noun
  arm is fenced (no determiner; determiner-less candidate sets for 01/61
  unvalued) — but the word-internal-31 arm is NOT fenced: no kill-grade
  contradiction and no license (hapax), and it "hinges on 61's (future)
  value". Bar clauses C1 and C2 both failed → NULL. The standing battery
  finite-verb legs for 31 (@338/@1647, "qui [31]" ×2) are untouched;
  re-opening arms 1–2 is red-team polyvalence venue, not battery venue.

- **N374** — val-41-40-independent NULL: census of all 19 41-windows
  (14 distinct predecessors, 17 distinct followers, max count 2). The
  "64 41" qui-frame at @40 (@37–44: "91 39 64 41 01 24 88") licenses a
  finite-verb slot, not a value — thousands of French verbs fit. The
  frame is phase-contingent: under the rival a1_01 offset the "64 41"
  frame dissolves entirely (byte-exact; 68 of 70 upstream row offsets
  unvalidated — canonicality caveat carried throughout). 41 is
  class-split stream-wide (noun arms @6/@238/@1017, verb arm @40,
  determiner arm @238), so naming one value needs a §7 ruling the
  battery must not pre-empt. The qui class-licensing holds whether or
  not 01 is a boundary (01-independence in the weak sense) — elegant,
  but still not a name.

- **N375** — val-86-inf-locus NULL: full 32-window 86 census; @1336
  "70=pre 52 39 83 [86] 71 64=qui 60 08". The only multi-leg candidacy
  ('voi'/'voir': "voir" ×4, "pourvoir" ×2, "pourvoient" ×1) collapsed:
  "86 29" is orthographically incoherent ("voi"+"er" ≠ French "voir"),
  and the "pourvoient" @889 leg is §5.2-blocked by the standing
  "00 86 | 06 77" clause-boundary fence. Independent fence: naming at an
  infinitive-life window would pre-judge the red-team split declaration
  (split-86-amended-rule battery PROMOTE reserves determiner-life vs
  stem-life to the red team). Census bigrams: "00 86" ×12, "77 86" ×5,
  "86 29" ×4, "86 56" ×4, "83 86" ×2, "86 52" ×2, "86 01" ×2,
  "86 24" ×2, "86 66" ×2.

- **N376** — word-12-06-1121 NULL (hard residual): exactly 2 "12 06"
  bigrams stream-wide (@1119 row a6_07, @1708 row a8_06). @1119
  "70 12 06" = "prenent": 0/57 files; "prennent" 108/57 files
  (`code/side-period/corpus/`, 57 French files). Both rescues are
  kill-grade dead: the single-n spelling (clerk-error leg killed by
  spell-pasent-test), and the plural-subject license (banked singular
  11="la" cannot head a plural NP). @1708 "12 06 29 40" = "nentere":
  non-word under every boundary; the only coherent word-shape
  ("[26]nent", 3pl verb, "viennent"-shaped) gates on 26's open class.
  Structural defect: no single-n "pren-" stem takes -ent in French
  ("nent" occurs only in line-break hyphenation artifacts like
  "soutien-nent"). Ground-truth anchors: 12="n" (R17-002), promoted
  06="ent", pencil-GT 29="er"; provisional: 59=est, 77=le, 94="ne" lead.
  Follow-up: stem-26-nent-verb.

### Round-17 null/kill batch, backlog fold 4 (crowd17, 2026-10-09 UTC —
4 notes: 2 kills, 2 nulls; battery grade)

- **N377** — letter-41-dist2-tri NULL: keep 41 outside the letter tier (the
  fence fires; evidentiary, not terminal). n(41)=19; three windows, three
  fails, all byte-verified against `data/upstream-ct_R5005.txt` +
  `code/side-keyhunt/repaired_offsets.json`. W1 @59 (row a1_01, "41 08 i
  er"): best reading "prière" (41=p, 08=r) is the unique common word only
  in the @59–63 segmentation, which is not forced — the @59–62
  segmentation yields 6 rivals (acier/osier/trier/crier/prier/scier) and
  assigns 41 a different value; no boundary evidence at @58|59, @62|63, or
  @63|64. Not kill-grade. W2 @1048 (row a6_04, "41 88 29=er"): fenced —
  88 is verb-stem (A3 frame), class-incompatible with a letter reading;
  6+8 rivals even hypothetically (frère/bière/fière/opère/avère/acère;
  fier/hier/lier/amer/suer/tuer/muer/nuer). W3 @235–237 (row a2_01,
  "70 98 41"): fenced by standing battery promote vient-98-name
  (2026-10-08, explicitly covering @236) — the window reads "prévient
  [41]" with 41 word-external; 5 rivals even hypothetically
  (prend/preux/prêts/préau/prêta). Three follow-ups proposed for the
  supervisor: letter-41-08-rerun (P3 — re-test W1 once 08's letter value
  banks; "prière" needs 08=r), letter-41-88-classcheck (P3),
  wordbound-41-59-seg (P3 — boundary evidence to force the segmentation).
  Discovered tension recorded: the parent census (battery-wordinternal-41-
  census NULL follow-up 2) listed the @237 lead without flagging the
  standing 98='vient' promote — adopted per lane convention, not
  re-litigated.

- **N378** — syll-39-de-host KILL: the @1334 '-de'-final-verb leg is dead at
  kill grade. Locus bytes @1327–1337 (row a7_04/a7_05): "… ne pre [52]
  a-de [86-INF]". Standing: 94='ne' promoted, 70='pre' banked pencil GT,
  39=/a/ promoted. 94='ne' is the preverbal negation particle and must be
  followed by a verb; 70='pre' is not a verb, so the verb must span 70 —
  it starts with 'pre', ends with 39-83 = "ade", and contains 52
  medially: /^pre.*ade$/. Corpus check: zero French words match in
  29,489,376 chars of 1841-register French ("ade"-final words exist —
  persuade, parade, dégrade, saccade, malade, promenade — none begins
  with "pre"). The "strand 70" rescue is ungrammatical ("ne pré" is not
  French; no clitic reading exists); 52's open value cannot fill a
  corpus-empty set. Phase-fragility verified: row a7_05 has 55 digits
  (odd), so under offset 1 the 39-83 bigram dissolves entirely —
  consistent with the kill, not a rescue. Scope: kills only the
  @1334-specific verb-host instantiation; the word-level 83='de' reading
  ("[pre[52]a] de [86-INF]", de-83-residuals PROMOTE) is untouched and now
  the default fork; syllabic-83 at @614/@1171 unaffected.

- **N379** — syll-83-de-1829 NULL: the '-de'-final VERB fork is fenced at
  kill grade (grammatical impossibility); the '-de'-final NOUN fork
  survives as a live residual. Locus @1829 (row a8_11): "… 00 97 00 86
  29(er) 82(m) [38 83 24] 82 16 59 …". French verb morphology: the ONLY
  verb forms ending in orthographic 'de' are FINITE (1sg/3sg present of
  -der verbs — aide, cède, décide, garde — 2sg imperative). Corpus check
  (76 files, 801 distinct de-final tokens): monde, grande, demande, garde,
  mode, regarde, possède, aide — nouns, adjectives, finite verbs only;
  zero non-finite verb forms. A '-de'-final verb at @1829 would sit
  immediately before 24, a class-level promoted FINITE verb — finite+finite
  adjacency with no conjunction is ungrammatical ("*il aide peut"). The
  fence is grammatical, not evidentiary: it holds regardless of 38's
  future value (38 open, n=7) and regardless of the 83='de' adjudication.
  NOT fenced: the noun fork ("la demande peut" is grammatical). Two
  follow-ups: noun-38de-1829-host (P3 — name the noun, parse the full
  window; candidate shape "[N-de] [24-modal] me [16-INF]"; cf. "mode" if
  38='o'), syll-38-value-census (P3 — 38's 7 windows @384/@826/@1113/
  @1343/@1469/@1650/@1828, name with ≥2 independent legs).

- **N380** — val-42-ne-noun KILL: [42ne]-as-noun-word is dead — no noun
  value for 42 is compatible with a -ne-final French word. Full 20-window
  census of 42 (@79/@205/@219/@266/@282/@428/@464/@488/@493/@543/@784/
  @1072/@1144/@1187/@1410/@1503/@1617/@1794/@1814/@1838). The one-word
  composition can apply only in the three '42 94' windows: @493
  ("78 [42] 94"), @784 ("24 [42] 94"), @1794 ("56 [42] 94"). Compatibility
  demands for stem S: (i) standalone French word; (ii) "er"+S is a French
  word (T3 fence: "29 42"×3); (iii) S+"ne" is a NOUN; (iv) S bare-capable
  (42 is determiner-less in argument positions, `val-42-det-gap`; the
  three windows supply no determiner — 78 is 'ver'-syllable lead, 24 is
  finite-modal, 56 is class-open). Corpus-wide computation over 41,923
  word types (`code/side-period/corpus/`, 59 French files, 34.5M chars;
  723 -ne-final types at freq≥3): exactly ONE stem satisfies (i)+(ii)+
  (iii) — "re" — already killed in noun-42-value (bare "re"/"rêne"
  ungrammatical, 1/20). All others fail: non-word stems (pei/hai/vei/
  scè/…→peine/haine/veine/scène), determiner-requiring nouns
  (chai→chaîne, cor→corne, don→donne, ton→tonne, …) which also fail "er"+S
  (erchai/erlai/erdon/…), pronoun stems (contradict R19-055 noun grant),
  and the "Jean"/"Jeanne" proper-name invention. Window-level
  confirmation: no -ne noun parses bare in the three windows (@784:
  finite-modal 24 + bare noun ungrammatical; bare "erreur" 0/34.4M chars
  vs "l'erreur" 86× — `noun-42-value`). Consequence: the three '42 94'
  windows must parse as "[42-N] + ne(clausal) + X" (composition (b), the
  standing alternative per `subj-42-class` C3). This closes the one-word
  composition entirely — noun was the only live class for [42ne]
  (`frame-42-94-leftward`: verb/adjective/adverb/pronoun arms dead or
  class-contradicting).

### Round-17 null/kill batch, backlog fold 5 (crowd17, 2026-10-09 UTC —
1 note: 0 kills, 1 null; battery grade)

- **N381** — doublet-41-589 NULL: the "41 41" adjacency at @589–590 stays
  unresolved between doubled word (H1) and syllable doubling (H3); only
  the geminate-boundary reading (H2) is fenced at frame level. Frame
  byte-exact: @587..592 = "00 97 41 41 09 00", row break between @589
  (a3_02 end) and @590 (a4_00 start); the "00 97 X" slot is word-tier in
  all 4 frames (X = 51 / 09 / 00 elsewhere, all word-tier cells). Self-
  adjacency census: 14 doublets stream-wide, 6 values; in-text precedents
  for H1 ("11 11" = "la la", granted) and H3 ("82 06 06" ×2 "mentent",
  "49 74 74" ×4, "42 98 98" ×2). H2 fails: row breaks do not align with
  word boundaries (row-start starter rate 0.072 vs baseline 0.095 over
  69 breaks) and no cross-word gemination precedent exists. Scribal
  dittography not established: 2/69 line-start==line-end matches at 1/96
  chance (p≈0.17). 41's doublet is unstereotyped (single, unique frame,
  lowest letter-neighbor rate of the doubler cells: 2/19); "97 41" and
  "41 09" are stream hapaxes. Feeds split-41-redteam; does not decide it.
  Follow-ups: doublet-589-97-role, doublet-589-09-role,
  linebreak-repeat-audit (all for the supervisor).

### Round-17 null/kill batch, backlog fold 6 (crowd17, 2026-10-09 UTC —
4 notes: 0 kills, 4 nulls; battery grade)

- **N382** — adj-37-independent-slot NULL (fence with cause): the supply
  arm fails on count — the independent (non-43-family) prenominal
  adjective-slot claim for 37 is fenced. Bar required ≥2 independent "37
  [granted-noun-head]" windows outside the 43 family; all 28 windows of
  group 37 censused ±3 context on the repaired stream, followers
  tabulated against the granted noun roster (43 per R19-064/R20-117, 65
  per R20-047, 68 per R19-107, 69 per R19-109, 76 per R19-111). Only one
  non-43 "37 [granted-noun]" window exists: @620 (`29('er') 88 [37] 76
  82('m') 14`, row a4_01), held hostage by the live rival S5 (37="le",
  MEDIUM, never killed) reading the same bigram as determiner+noun —
  mutually exclusive with the adjective slot, so @620 cannot count as a
  clean leg. The 43-family ("37 43" ×3 at @385/@1125/@1723) excluded by
  the bar; zero "37 65/68/69" windows stream-wide. Scarcity-of-legs null,
  not a rival-victory null. 37's noun-class grant (R17-003/R17-008), the
  A12 "37 01" unit, and the 43-family windows untouched. Follow-ups:
  adj-37-76-rerun (P3) — re-test @620's adjective reading once S5 is
  adjudicated (s5-37-385-adjudicate, already queued); adj-37-nounwatch
  (P4) — re-run this census if a new noun grant lands.
- **N383** — det-385-leftedge NULL (fence with cause): the bar's
  else-branch fires — no battery-grade determiner candidate in the @385
  left edge to head the '38 37 43' fragment; the bare-NP reading stays
  fenced under the adjectival-37 frame. Byte-traced on the repaired
  stream: left edge @378–383 = `00 11 50 82 16 52`, fragment @384–386 =
  `38 37 43` (row a2_07) — verified in this fold against
  `code/side-keyhunt/repair_parse.py` (1,847 pairs / 96 types; the
  target's "@379-383" is the 1-based lane convention, worker offsets
  0-based). Six candidates excluded with cause: 00="pour" (A9)
  preposition; 82="m" (pencil GT) sub-lexical; 16 finite-verb here
  ("m'a/m'est [52]" per battery-val-16-a-vs-est); 50 no determiner arm
  (frameA-50-value NULL); 52 no determiner tier (val-52-630-frame PROMOTE:
  verb/adverb/sub-lexical only); 11="la" (pencil GT) genuine determiner
  but cannot span five cells — 82="m" forces "50-82-16" word-internal,
  "52-38" collapse KILLed, zero battery-grade evidence stream-wide for
  an 11-headed span of >1 intervening cell. Wider @355–377:
  determiner-valued cells (47="ce" @357/@363, 11="la" @358) 20+ cells out
  behind finite-verb clauses — no cross-clausal determiner heading is
  grammatical. Adopted: battery-tail-385-rerun-43poly NULL,
  battery-val-52-38-unit KILL, val-52-630-frame PROMOTE. S5 fork
  untouched — fence applies strictly under the adjectival-37 frame; if
  37="le" (s5-37-385-adjudicate, queued), no external determiner was ever
  needed. Follow-ups: la-379-span-test (P4); det-52-arm-kill (P3);
  np-43-determiner-census (P4).
- **N384** — residual-86-finer NULL (fence outcome): re-derived all 32
  86-windows (±4 context, repaired stream); the residual 10 from
  det-86-dlife-partition Subset 4 neither partitions into a
  frame-consistent value subset (86='le' and 86=noun already NULL at
  det-86-dlife-partition §4a/4b; nothing in the 08='t', 52-split, 76=noun
  verdicts re-opens any window) nor leaves any window unaddressed. Fence
  inventory: A ×2 orthogonal granted-defect (@728 "la pour", @867 "que
  pour" — ungrammatical left of 86 under any 86 value, par-pour-962
  docket); B ×2 83-left pair (@899/@1335) — 83's noun fork live per
  syll-83-de-1829 NULL but selects no 86 value; C ×4 confirmed orphans
  (@300/@716/@1131/@1147 via adopted kill-grade orphan86 KILLs); D ×2
  open-neighbor (@557 "fois [86]" absolute-construction tension; @1739
  fully open neighbors, force-free). 86='le'/noun stay unforced. §7
  intact; det-86-dlife-partition's PROMOTE untouched (never-downgrade).
  Follow-ups: residual-86-83pair (P4); residual-86-557-fois (P4);
  redteam-86-residual-closure (P2, gather-only) for the red-team 86-split
  docket (already queued). Caveat: fences are conditional — each names
  the value that un-fences it; if any lands, the window must be
  re-tested, not the null re-cited as closure.
- **N385** — un-71-det-census NULL: determiner census across all 96 cells
  at two grades found no cell holding "un"/"une" other than 71 itself.
  Red-team grade: all 50 registry cells in
  `code/table-grid/table-registry.json` censused — zero "un"/"une".
  Battery grade: full-text grep of `code/crowd17/report_inbox/` (inbox +
  processed/) — "un" zero value claims; "une" only as scoped/window-local
  readings: 20="une" (fenced to @307), 41="une" (bar-stipulation at @239;
  global value owned by queued donn-41-44; the four 41-PROMOTE batteries
  name no "une" value), 71 itself (frequency leader;
  quant-71-925-value NULL). No homophony exclusion fires; "une" stays
  frequency leader for 71, value underdetermined (une/deux/plusieurs/trois
  per quant-71-925-value); §5.2 does not fire; §7 intact. 71's 7 windows
  re-derived (@233/@325/@711/@924/@1336/@1564/@1613). Follow-ups:
  un-71-gender-frame (P3); un-41-vs-71-homophony (P3 — re-test iff
  donn-41-44 lands 41="une"); quant-71-rerun-neighbors (P4). Caveat: the
  battery-grade census is only as complete as report_inbox coverage.

## 6. Open hypotheses (not promoted — each needs ≥2 independent checks)

**Round-12/13 status deltas (2026-10-07):** 31=VERBAL (finite)
provisional-conditioned promoted (F84); 77="gouv" demoted→disfavored
(N44); 21="ce" banked LEAD; 20="fois" banked LEAD @1034; 33 paradox
recorded; unconditioned-48="de" KILLED (N43). **Round-13 adjudicated
(2026-10-07, docket CLOSED 21/21):** islet-audit grants dissolve 5/10
islets into word/frame rules — the 67 fork (ISLET 4) is the registry's
ONLY true polyvalence, SUPPORTED; ISLET 5 INCONCLUSIVE keep LEAD;
citation corrections @1444/@1800/@960 banked. All four homophone sets
**SPLIT as class-mates with different values**: {33,86} (SPLIT —
§b PROPOSE retired, no 33+86 window merging; 33's infinitive hunt on
its 8 pour-frames alone), {48,94} (SPLIT — 48 stays UNIDENTIFIED),
{52,59} (SPLIT — 52 UNIDENTIFIED, weak est-arm lead), {76,78}
(SPLIT — 76 UNIDENTIFIED, weak ver-INITIAL lead). 31=VERBAL (finite)
CONFIRMED; 92 NULL constrained; 33 NULL constrained (savoir forbidden
both forks). Missing-mass granted: ~17–20 cells among the 84
unidentified groups, 0 for identified syllables; **digit hunt
RETIRED**; priors banked as priors only. @1248: PC-1 leg granted,
DP-1 PERMANENT FENCE, NEITHER-fence stands; **atteste FRAME-BEST
LEAD** (n=1, fragile — not a promotion); H_stem gains one leg (B1+B2)
with open ne-marginals tension. Baselines: 237/237 R13BANK +
160/160 ROUND13-LEDGER, both exit 0.

**Round-17 wave-2 deltas (2026-10-08):** 39="a/à" (F88), 30="pas"
(F89), and the 59-frames (F90) battery-PROMOTED — all pending red-team
ratification; 62="on" KILLED (N52), the "ierenne" one-word composition
KILLED (N53); 78="ver" NULL (N54) — escalated, red team must decide
ratify-vs-R16-004; prenne-70-12-94 NULL (N55) — 12="n"/94="ne" duality
unresolved, neither side advances on that evidence. Open and queued:
lever-77-78 ("77 78"="lever", "48 77 78"="élever" composition, F3),
noun-44 (F5 input), ne-alone-02-74 (bare-"ne" modal cluster, F2),
fem-32e (F4), ver78-la78-census, ver78-45-dependency-gate, and a
dedicated noun-26 battery (the 26 war: verb legs dominate, crux
window @1559 unresolved).

**Round-17 wave-5 deltas (2026-10-09):** 105 next-token battery
verdicts folded (F173–F225, N158–N174, ~30 grouped nulls). New
battery-PROMOTES, all pending red-team ratification where the note
says so: 31 = VERB class (F184); 14 determiner-shaped @117, 'le'
leading (F182); the 'en' arm for 14 kept at battery grade (F185);
56 whole-word (F210); 37-01 word-internal "faire"-compound, 01 =
"fait" (F225); 55 = verb class, battery-grade (F220); the 60 verb
split, bare-60 (V1–V4) vs ent-60 (V5–V6) (F208); 94 word-final
"ne" @508 (F216, function-scoped, conditional); 65 postverbal
subject of "que [56]ent" @1744–1747 (F214); "ceci" = 87+61 @644
(F206); the 84 ne-follower discriminator holds at the widened
census (F194). KILLED: global 00="contre" (N158 — fenced to the
"96 00" positional arm, packaged for the red team); 'tain'/
"certain" at all three 37-01 windows (N159); absolute "ce
faisant" (N160); the clause-boundary mechanism survey-negative
(N161); "telle" at both Type-A 52-37 windows (N162); 14=verb
(N163); the '@337–345 one-run parse (N164); '@1105 "ce ver[65]"
completion (N165). Escalations stacked for the red team: 24
(mutual kill, battery-24-en-verb-conflict), the @1029 two-horse
race ('c'en' vs 'ce se', battery-ce01-slot-1029), the
poly-80-docket (battery-x29-80-collocation), noun26-89-class and
stem48-65-governor (ratification). §7 split candidates live: 02
(verb-selecting vs non-finite), 41 (verb @40 vs determiner @238),
13's distributional split, 60's two-item split (F208 needs
ratification).
Proposed follow-ups (nulls regenerate work — queueing is the
battery supervisor's per its protocol, recorded here as open
hypotheses): ce01-1029-redteam-package (P2 — A-vs-B adjudication
package), stem-03-en-se-licensing (P3 — once stem-03-value lands),
ce87-topic-licensing (P3 — bare-'ce' topic precedent; kills both
A and B if none exists), adj-38-w4-parse (P3), w4-38-1343-revisit
(P4), phase02-kill-windows (P3), val-21-pivot-rerun (P3, gated on
redteam-43-polyvalence). Supervisory note: residual-1029-
infinitive is still queued carrying the stale "ceci [03]er"
premise — needs re-brief before execution.

**Round-17 wave-4 deltas (2026-10-08):** battery-PROMOTED: 06="ent"
(F97 — verb-ending/adverb fork closed at battery level, pending
red-team ratification), 32 = one verb lexeme (F98 — dissolves the
adj-32 dual-behavior question, no second polyvalence needed),
24 = finite-verb class (F99 — VALUE OPEN; the old "24 = en"
reading is excluded by the verb class). KILLED: 01="ci" and
01="faisant" as general token values (F100, both at kill grade on
the discriminator windows; narrower bound-"-ci"/word-internal
readings fenced, not dead — the "ci" kill is load-bearing on
F99's 24 class grant); the @317 "94 06" gate claim (N67 — closed,
follow-up retired). The noun-26 umbrella is adjudicated NULL
(N68): the positional noun/verb rule is stated but its
declaration is a red-team act per S7. Escalations now stacked for
the red team: class-92 (N64), verb-48 vs A7-L2 (N69, N70), plus
the wave-3 s5/frame-37/62 items. Conditional leads for the
supervisor's queue: 33="laisser" (N65, gated on open 16/85),
ce-frame's conditional "par suite" (N63, gated on noun-43),
83="de"'s C2 "vient de" leg (N66, gated on 98="vient").

**Round-17 wave-3 deltas (2026-10-08):** nest-subject-86-62-42
PROMOTED (F93 — the three "n'est" frames are the only X-94-59
trigrams, closed-set census); noun26-pas-frames PROMOTED with a
recorded positional exception (F94 — 26 verb-class, "26 30" x4 =
"[verb] pas"; @1559's banked "la" forces the "noun iff preceded by
11='la'" rule, recorded-not-declared); noun26-encequi-triple
PROMOTED (F95 — 26 verb-class in the "24 87 64" formula slot by
frame uniformity; value open); prenne-subject-S1545 PROMOTED via
the subjectless disjunct (F96 — @1545 is the only "pour que" window
whose subject slot is empty; closed 4-window "00 46" census).
NULLs: adj-32 (N56 — 94/48 resolve except the @317 "ne 06" hapax;
dual verb/adjective behavior needs red-team polyvalence call),
fork-78-45-adjudication (N57 — vacuous while ver-78 unsettled;
R-pos stated), dict-45 (N58 — general "dict" dead, positional arm
survives), frame-37-reexam (N59 — ESCALATION: ISLET-10 fencing
exact; A1 scope gap; A1 6 windows not 7), s5-foundation (N60 —
ESCALATION: 5 windows anti-37="le"; @913 "le par" ungrammatical),
lon-ne-77-62-94 (N61 — ESCALATION: contradicts collision-62-84's
kill; conditioned 62="on" queued for red team), stem-33-86 (N62 —
orphan rate 10.5% misses the 10% bar; 86 is n=32, not 12).
Finder beats: f-qui-par (43 n=16/13 productive, 01 n=28/26
productive; triple-"ce" composition is 01="ci"'s strongest leg; 8
targets queued) and est-reexam (both sides' counts re-derived
exact; "52-37" corrected x3->x4). Battery queue now 148 targets:
52 verdict / 96 queued.

**Round-16 status deltas (2026-10-08 UTC, crowd16 next-token, 16/16
battery-adjudicated):** 77="le" PROMOTED (provisional → promoted;
"le la" adverse dissolved); 78="er" KILLED distributionally, 78="ver"
LEAD; 45="ce" DEMOTED PROMOTE→HOLD, 45 "ce/dict positional allophones"
LEAD (conditional on 78="ver"); 37/42 predicative est-frames DEMOTED→HOLD
(0 valid legs each); 32 est-frame STANDS (3→2 legs); 19 HOLD (1 leg,
verified); **30="pas" NEW LEAD** (ne-frames @559/@1715); 47="ce" grant
HOLDS (28/28, no value break) with a positional spec now naming two
exceptions — **47="se" after infinitives is a competing LEAD** (allophony,
not polyvalence); **67 et/veut fork RESOLVED positionally** ("veut" iff
infinitive-shaped follower — LEAD, circularity caveat recorded);
**94="ne" STRONG LEAD** ("n'est" ×3, "ne me/m'" ×4); **12="n" LEAD**;
**39="a/à" LEAD**; **06="ent/ment" LEAD**; **33="dire" LEAD** (promotion
blocked by the 29-8X word-shapes); 31=VERBAL class CONFIRMED (8/8
distinct followers); 00="pour" banked CONFIRMED with fenced adverses
(@1247 strong, @864/@291/@685/@1287 fenced, ~5× register-rate adverse);
79="tout" banked CONFIRMED (2 fenced qui+tout residuals);
**84="on" STANDS WEAKENED** ("on est" legs void; 3 fenced residuals,
new @146; ESTE-verb tension for red team); "vient de me parvenir"
word-reading LEAD (98="vient"/83="de" word-anchored); "entrepre[12]" LEAD
(conditioned on 06="ent"); "la première [20]" forces 20 = feminine
singular noun (20-paradox now one-sided); "l'en-X" ×3 LEAD (conditioned
on 24="en"); 26-noun ×2 LEAD (tensions 26=verb); 81 masculine-noun LEAD;
86-29 substantivized-infinitive LEAD; 43 feminine-noun LEAD; 91="va" LEAD;
88="s"/10="s" LEAD; 44="ble" LEAD; 73="lu" LEAD. Record corrections:
67-33 ×1→×6, 12-48 ×7→×5, 26-30 ×3→×4. **Smith/fleet:** rung-C clean
re-run PASS (36/36, 3–0 unanimous; bar ≥35/36), red-team audit ADMISSIBLE,
strike one CLEARED, v3C instrument ACCEPTED, step-4 clearance re-requested;
**memorization re-probe CLEAN** (36/36, margins −77..−85, void rule not
tripped) — seal paradox resolved by binding red-team ruling (a).
crowd15/next-token DB rebuilt (1001.1 MB); calibration in progress
(calibrate.json still empty — fold numbers next sweep). track-b training
resumed (upd 13,500, epoch 7, best heldout 2.0198 @upd 13,200, declining).
table-grid registry refreshed 01:47 UTC — **77's promotion and the
78 "er"-kill are not yet merged into it** (coordinator-owned).

**Round-17 status deltas (2026-10-08 UTC, crowd17 next-token, battery-
adjudicated, red-team ratification pending):** **12="n" PROMOTE**
("en" 40-12 @63, "ni" 12-34 @1740, "pren" 70-12 ×3 — 5 occurrences);
**48="e" PROMOTE** ("me" 82-48 ×4, "ere" 29-48 @541 — 5 occurrences;
single "ere" occurrence is the soft leg); **94="ne" PROMOTE** ("n'est"
×3 @558/@762/@1795, "ne me/m'" ×4, 62-94 ×9, "prenne" 70-12-94 ×2;
37-window census, zero hard contradictions); "prenne" analytic/
syllabic duality (70-12-94 vs 94) is the two batteries' handshake,
consistent under both, resolved by neither. **77="le" PROVISIONAL**
(44 windows; @611 rescue killed, strain at 87; @1033 escalated to red
team). **33 stays OPEN** — croire-vs-dire tie (25 windows),
single-"dire" killed, {dire, X-er} set unfalsified with X unnamed.
**45="ce" HOLD** (second mirror frame-type not found; 78-45 fork
live). **80 inflectional mood alternation escalated to red team.**
**84 vowel-initial mechanism banked**: 77's l'-elision fires
exclusively before 84 among known vowel-initial cells
(77→{59,94,46,40,34,47,17} = 0) — independent proof. 12/48/94
promotions NOT yet merged into table-registry.json (coordinator-owned;
12/48 absent from it). Record corrections: "n'est" third instance
@101→@1795; 'ne' = 12-48 ×5 confirmed (brief's ×7 corrected twice,
independently). **Smith/fleet + calibration**: rung-C PASS and
memorization re-probe CLEAN stand; **calibration LANDED** (standard
n=19,998 top-1 0.3207/top-5 0.5218/MRR 0.4183; by-ear n=19,999 top-1
0.3342/top-5 0.5366/MRR 0.4318; 11.07% by-ear word disagreement on
200k-word sample); track-b upd 14,100, best heldout 2.0138 (still
declining); side-period mine-v3 corpus +18 texts (14× Allgemeine
Zeitung Augsburg 1841-01-12..25, Guizot t1–t3, Talleyrand v1 —
unmeasured, provisional; the mine-v3/corpus copies were removed
2026-10-08 as duplicates of corpus/).

- **Round-17 wave-6 deltas (2026-10-08):** battery-PROMOTED: 45's post-78
  follower profile (F106 — ver-78-independent contact boundary; 45="dict"
  NOT promoted), 26 verb-form via three independent governors (F107 —
  does NOT grant 26=verb globally; the noun-26 legs and @1559 crux stay
  with noun26-la-frames/T4), W2 @573 one-word gate (F108 —
  ver-78-independent; 45='ce' kill-scope 1/22), 62/84 conditioned slot
  split (F109 — distributional only, no value named), the 45->93 x3 cluster
  under one parse (F110 — 93's global class fenced to verb-93, p3
  queued; bar-(b) tripwire: a verb-93 positive converts to a kill-grade
  adverse for A11), the @1502 orphan guard (F111 — 33-set orphan rate
  2/25 = 8%, at/under the 10% threshold). KILLED: ver-78
  successor-completion ('ce ver[48/65]') — @364 "ce vere[49]" and @1397
  "ce veree" force it false; 78="ver" stays LEAD (R16-005), @296 stays the
  fenced 1-window residual (N78). NULLs: s5-foundation-r2 (N77 — kill-grade
  contradiction of the S5 fence, 37='le' MEDIUM now ESCALATED to the red
  team), x-33-laisser-test (N79 — 'laisser' at LEAD strength, gated on
  frame-82-16 + stem-85; gate-satisfiability-16-85 owns the
  kill-if-banked-forced-non-infinitive), dict-frame-78-45-13-55-61 (N80 —
  13-55-61 unnameable with evidential support; W2's "ne ce" = stream-unique
  94-87 bigram flagged as 94-frame anomaly), lever-77-78 (N81 — 'lever'
  composition neither promoted nor killed; clause-1 soft-fail at @213
  fenced to open 06 value; "77 78 never splits" corrected — one
  non-adjacent co-occurrence @877-879; 77="le" stays provisional). ANOMALY flagged: the queue cites
  the parent set report at `code/crowd17/report_inbox/battery-dire-33-set.md`,
  but the file lives at `report_inbox/processed/battery-dire-33-set.md`
  (wrong path in the queue, file present; data chain intact via
  battery-erstem-33-id). Conditional leads for the supervisor's queue:
  33="laisser" (N79, gated on 16/85), the 'ce ver[65]' completion at @1105
  (ver78-65-completion, gated on prof-65), the 'ce verdict' x2 leg @573/@982
  (verdict45-value, gated on R16-004).

- **Round-17 wave-10 deltas (2026-10-08):** battery-PROMOTED: 98='vient'
  (finite semi-auxiliary, F123 — 40/40 windows, zero board
  contradictions; caveats: rests on the 83='de' lead, doubled-98 x3
  cause unknown, four '[62] vient' windows ride on unpromoted
  62='il'). KILLED: 60=masculine-noun (N96), 60=masculine-adjective
  single-value (N97) — both single-value claims dead; the live
  result is the bare-60 vs ent-60 verbal shape split (N100).
  NULLs: donne-168-708-leg (N103 — both 'donne' windows parse, the
  53-12-48 trigram is exactly 2x stream-wide, but 21/71 unnamed;
  prof-53 null untouched), stem-44-nominal (N104 — 2/15 windows
  force stem-level @540/@1160 vs 13/15 whole-word; whole-only
  orphans 13.3% > 10% bar — the A10 stem/whole HOLD in parallel,
  red-team docket), noun-89-1377-adjudicate (N105 — class conflict
  confirmed: no verb-89 parse of @1376 kills the noun/adverb
  reading; infinitive-slot legs @221/@985 stand; escalated to the
  already-promoted class-89-adjudicate packaging), at21-82-43-29
  (N98 — @21 forces word-internal 'en' vs 'par [43]' forces noun;
  §7 red-team petition), fence-83-1217 (N99 — localized residual,
  83 designated blocker), verb-60 (N100), tout-14-rerun (N101 —
  14='le' not forced false under the adjective rival),
  tout-slot-14 (N102 — no class; all four breakers fenced). Open and
  queued: poly-60-redteam (p1), adj-frames-995-637 (p2),
  participle-60 (p2), ce33-noun-slot (p2), en43-wordinternal-census
  (p3), class-36-profile, fence-92-1218, clause-boundary-precedent,
  le14-adj60-tail (p2), clitic-14-82-breakers (p3),
  det14-elsewhere (p3), breaker-b4-1121, verb-14-rival,
  verb-60-bare (p2), verb-60-ent (p2), split-60-verbs (p3).
  SUPERVISOR GAP: 9 follow-ups proposed by this wave's batteries are
  NOT yet in `code/crowd17/next-token/battery-queue.json` —
  name-21-obj (p2), name-71 (p3), prof-35 (p3), phon-44-elision,
  stem-44-value, poly-44-docket (red-team decision),
  faire-86-causative-test, adv-89-1376, tail-1376-on92 — the
  supervisor audit of their follow-up sections is outstanding
  (standing directive: the supervisor queues proposed targets
  itself).

- **Round-17 wave-11 deltas (2026-10-08/09):** battery-PROMOTED: 24="faire"
  (verb lexeme) + 01="en" LOCAL to the three 01-24 windows (F124 —
  general 01="ci" and 01="faisant" stay KILLED, now mechanically
  explained; never-downgrade rule fired against 01='-ci' @984), 97 =
  infinitive-class (F125 — value open; ver78-296-97gate still gated),
  'ARTICLE + PROMOTED PREPOSITION' violation systematic at @913/@997
  (F126 — distributional calibration only, S5/A1 untouched),
  24=finite-modal-class + 87=ce + 64=qui in "qui [23/26] 37" frames
  (F127), the 37 rival-value RANKING (F128 — no value named),
  92=verb on its verbal-governor subset (F129 — global split to the
  red team), W1 decides for CE (F130 — 37-78 word-internal infinitive
  complement of modal-24; 45@314 word-initial 'ce'; all dict parses
  ungrammatical; unconditioned R-pos falsified). KILLED: 92 as
  unconditioned feminine noun (N106 — A14/A6/09~92 holdings and the
  prenne-subject-S1545 slot claim untouched), subjunctive trigger
  @347-349 (N107 — triggerless), 21="suite" VALUE (N108 — noun class
  F122 not downgraded; 21-65 unit-verb rescue escalated to red team).
  NULLs: adj-frames-995-637 (N109 — @637 blocked by A8, red-team
  ruling on 89 needed), dict-45-ce-rival-1165 (N110 — double residual;
  78='ver' LEAD unresolved), dict-45-w3-ceci (N111 — promote blocked
  by never-downgrade, conditionality, fenced adverses),
  dict-78-45-wordbound (N112 — boundary holds W2-W4, 'verdict' value
  arm escalated), feeder-ceci-47-45 (N113 — @984 the clean window),
  la-523743-adjective (N114 — S5 contradiction escalated; the
  adjective vote UNANCHORED; new "37-11" x2 data), lon-62-on-conditioned
  (N115 — clause (a) passes; conditioned admissibility red-team),
  lon-94-64-rightedge (N116 — genuine 1-window residual, fenced),
  name-21-obj (N117 — "suite" idiom lead, promote blocked;
  suite-21-qui-que killed the value), ver78-la78-census (N118 —
  5/9 < 7/9; 16/31 determiner-headed noun distribution unrebutted),
  w1-314-ambig (N119 — bar's consequence mapping inverted; promote
  discharged via rebar F130). Open and queued (all verified in
  queue.json this sweep): adj-frame-995-solo (p2), vers-78-w4-gate
  (p2), dict-45-circle-break (p2), verdict78-gate-wordbound (p1),
  ceci-195-nounslot (p3), residual-345-06, residual-1029-infinitive,
  lela-37-51-1655 (p2), unit-52-37-name (p2), prenne-R3-relative-341
  (p2), rival-21-feminine, prof-65, ver78-rerun-214-1543 (p2),
  rpos-w1-exception. SUPERVISOR STATUS: HEALTHY — the wave-10 gap is
  closed (all 9 follow-ups queued or verdict-tagged) and every
  wave-11 note has a verdict-tagged queue entry matching its verdict;
  null-regeneration protocol held (w1-314-ambig's p1 follow-up
  w1-314-rebar ran and promoted). Decode renders:
  `decode-current.txt` / `decode-sidebyside.txt` (R5005, 1,847-pair
  stream; ~1/3 of groups readable) now mark `ce/dict?` at the 78-45
  loci, `le?` at the S5-fence, `ver?` for the 78='ver' LEAD, and
  class tags for the wave-11 class promotes.

- **Round-17 wave-11 mid-sweep deltas (7 battery notes landed during the
  sweep, folded this sweep):** battery-PROMOTED: the 'le qui' violation
  class systematic (F131 — mirror to F126 on the 64 axis; S5/A1/77='le'
  untouched), 01@984='en' CONFIRMED via the never-downgrade adjudication
  (F132 — R2 parses assumption-free, R1 needs >=1 extra assumption;
  '-ci' at @984 fenced; F124 confirmed, not downgraded), whole-word
  nominal-head 44 at @1839, instance-scoped (F133 — no value named;
  global question stays in the red-team docket). KILLED:
  prenne-R3-relative-341 (N120 — the surviving horn dead; load-bearing
  on the 43="suite" kill; re-opens only if "suite" revives). NULLs:
  dict-45-circle-break (N121 — independence nowhere available; the
  w3-ceci circularity extends to W1/W2/W4), importe-30-elision-test
  (N122 — 'importe' neither killed nor advanced), lon-on-elision-control
  (N123 — discriminator recorded, case weakened: granted 'on' legs
  0/25 'ne'-followers vs @508 'on'+'ne', p=0.038 below rejection —
  not kill-grade). Open and queued: dict-313-w1-adjudicate (p2),
  wordbound-30-06-importent, ci-demonstrative-census. Note: 7 of this
  sweep's 28 folded notes arrived while the sweep was running; the
  battery fleet is consuming wave-11 follow-ups in real time
  (dict-45-circle-break and prenne-R3-relative-341 were proposed in
  this same sweep and already ran).

- **Round-17 wave-12 deltas (2026-10-08/09, 85 battery notes):** battery-PROMOTED:
  "69 11" @1115–1116 locus-level "cela"-shaped (F134 — global 69 stays
  open), "61 40 17" @1556 locus-level "première fois" (F135 — global 61
  DEAD at the same wave), byte-exact ungrammatical-"ne" window map as an
  evidence package for the red-team 94 duality (F136 — no value claim).
  KILLED (N124–N140): "ce + infinitive" nominalization (period corpus:
  "le" is the substantivizer), "dite" from the 52-37 Type-A set,
  the @1023/@1024 clause boundary, the uniform 20-particle account
  (W1-local ellipsis survives), window-independent 14="le", the @213
  06-complement claim, "passe-partout" @44–48, joint 62="man"/98="n",
  one-value-for-88, the @314–325 parse family, the "néce-" rescue (94="ne"
  STRONG LEAD untouched), the prennent subject-agreement reading
  @1116–1120 (souvent clause itself not killed), the 88 plural-pronoun
  arm, 14="souv" (spelling works, distribution kills), 14="sou", the
  rival letter-"e" @1229/@1589, any global 61 value. NULLs: 62 noun-class
  holds 2/3 legs (conditioned split with red team); 98="vient"
  battery-promoted, unratified; 43 ∈ {condition, mesure} undecided;
  52-37 {même, seule} tie; 37 under S5 escalated (s5-foundation P1);
  14 fully open. Note: no wave-12 note proposes a change to
  `code/table-grid/table-registry.json` (`generate.py` reports UNCHANGED);
  `code/side-keyhunt/repaired_offsets.json` was rewritten but is
  byte-identical to the pushed copy — content-neutral.

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
  (this sweep). Round-17 wave-6 (F109): conditioned split demonstrated —
  62's pre-'ne' slot (15/35) and 84's post-clitic elision slot (9/25)
  are disjoint with zero crossover — distributional only, no value
  named, no polyvalence declared; conditioned-62='on' stays with
  lon-62-on-conditioned / the red team.
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

**Round-17 wave-13 additions (2026-10-09 UTC):**
- **"par pour" x3 → conditioned 00="contre" after 96="par".** Fence
  (bound-96-00-clause: all three "96 00" windows boundary-less, mid-row,
  "par" complement-less — a systematic anomaly) + leg
  (contre-00-three-windows: "par contre" parses all three windows,
  Littré-attested 19th-century French). Independent checks still needed:
  (a) red-team ruling on the conditioned value under the A9 00="pour"
  grant; (b) par-96-complement-census — is 96 ever complement-less
  elsewhere?
- **13: sub-lexical or §7 split.** Both word-level "les" arms dead at
  kill grade (N148 @567, N152 before promoted verb class); the
  distributional split is real and unseparated (split-13-det-pron: 5
  verb-successor windows vs 7 non-verb, no positional separator).
  Independent checks still needed: (a) test sub-lexical 13 at the
  "78-45-13" windows; (b) red-team split declaration.
- **02: §7 split candidate.** The qui-windows (x2, verb-selecting) vs the
  non-finite-forcing windows (@305/@858) are irreducibly split
  (02-class-609); the negated-verb reading died at distributional grade
  (N156). Independent checks still needed: (a) deep parse of @750 to test
  whether the second qui-leg dissolves; (b) conjunction candidacy at
  @305/@858.
- **41: §7 split candidate.** No uniform class across standing-value
  contacts (class-41-contact: verb @40 vs determiner @238). Independent
  checks still needed: (a) a second battery on 41's successor
  distribution at distributional grade; (b) red-team split declaration.
- **71: §7 split candidate — nominal@1337 vs non-nominal@925** (F159).
  Independent checks still needed: (a) a second nominal leg at
  distributional grade; (b) red-team split declaration.

### Sweep deltas — open-hypothesis status + housekeeping (2026-10-09 13:15 UTC)

- 62='il' is KILLED at kill grade (R19-106, registry round19 merge);
  the ['il','lead'] cell is removed. Open-hypothesis items riding on
  an unpromoted 62='il' (e.g. the four '[62] vient' windows noted in
  the wave-11 deltas) are closed on that value; 62's value remains
  open (62='on' FENCED-LEAD stands).
- 76=noun (masculine) lead→prom (R19-111) — F104 ratified at the
  registry; 76 is no longer an open cell.
- Housekeeping: `code/side-keyhunt/repaired_offsets.json` mtime moved
  11:16→11:34 UTC; no baseline exists for a content diff. All
  in-session batteries re-derive the stream and assert 1,847 pairs /
  96 types, and `generate.py` printed UNCHANGED, so the grid
  frequencies are unaffected.

### Sweep deltas — post-13:30 UTC batch (2026-10-09)

- 74: the nominal/formula hypothesis is KILLED at battery grade
  (N335); 74's class stays OPEN at battery grade (red-team venue); the
  '49 74 74' chains stay unparsed (N331). Residual: '74 74' ×6
  contradicts any whole-word class at kill grade.
- @730: the "la en" leg is PROMOTED window-local (F230) — the clause
  @729–735 parses as full French with one ungranted assumption
  (48=subject). 88=finite here is forced, window-local, not a global
  promotion; the uniform clitic-pronoun rival across the 88 population
  stays fenced (N332).
- New queued follow-ups: val-86-728-entr (tests 'entr'; R20-116's local
  'voi' composition at @889 stands), gov-88-730-modal (gated),
  subj-88-730, val-66-87-verb, pron1514-dislocation-corpus,
  chain-follower-class, unit-49-74-74, tonic-66-rearm (gated),
  redteam-tonic-fence-input, noun-49-909-875. (adj-49-420-366 already
  landed: KILL; formula-76-49-24's promote was R20-overridden to FENCE.)
- Personal-tonic family: the stream side is fenced as tonicless (N334)
  while the corpus side has one genuine interrogative (F229) — the two
  arms do not collide (stream-Group locating vs corpus attestation).
  The sibling disagreement on @86308 (Dumas *Henri III*) is headlined
  for the red team.
- Red-team Round 20 (136 rulings) is folded as the R20 addendum in
  section 4: the sole standing revision is @889 "pourvoient" (one
  word); registry unchanged at 50/96 cells.
- Queue state (read-only cross-check, 2026-10-09 ~15:16 UTC): 1,353
  targets — 434 null / 314 promote / 173 kill / 2 split verdicts;
  430 still queued.

---

### Sweep deltas — backlog fold 2 (2026-10-09 UTC)

- **Gate status this batch: no gate satisfied.** Two gate claims, both
  refused correctly. `ne-508-reseg-gate62` (N368): the gate had verified
  "satisfied" on a 62='il' battery promote that the red team then REJECTED
  (R19-097) and killed at kill grade permanently (R19-106, R20-125) — a
  battery promote the red team rejected does not satisfy a gate trigger.
  `verdict78-gate-wordbound-rearm` (N369): the six ver-78-class returns are
  leg-gains and completion-arm kills, not a change in 78's status
  (78='ver' stays DEFERRED per R20, R16-005 LEAD) — neither bar clause is
  testable. Two gates properly satisfied and folded: adj-80-469-ratify
  (F276) keyed on red-team-ratified 06='ent' (R17-007/R20-011/R20-064), and
  prof-43-rerun-polyvalence (N342) keyed on red-team 43=["noun","cls"]
  (R19-064/R20-117). Two gates armed for the future, not fired:
  `ne-508-reseg-rearm` (on a red-team 62-value grant) and `neque-94lead-gate`
  (on 94='ne' moving strong-lead→grant at red-team level); plus-jamais's
  three re-runs explicitly require red-team value grants, not battery
  promotes (gate rule 2026-10-09).
- **F268 wording rephrase (supervisor's call):** the reinforced-pour-inf
  fence statement must drop "reinforced heads govern infinitives" — the
  topology null (N350) shows 0/41 head-as-governor windows; heads occur only
  as the infinitive's resumed object. Proposed rephrase: "reinforced heads
  never license the exclamatory pairing". The fence itself stands (F268/F269
  plus N349/N351); only the wording is contested.
- **redteam-01-split-docket (gather-only input, no verdict):** 01 has three
  disjoint local readings — 'en' clean only at @988, 'on' windows
  (@893/@970/@40/@984), 'fait'-syllable word-internal in '37 01' ×3
  (@940/@1634/@1818); uniform 'en' has 9 kill-grade deaths, uniform 'on'
  5+ (battery-val-01-census). Live tension: @40 is both the battery-promoted
  01='en'-local window ("en faire") and the census's 'on' leg. Red team
  must decide: conditioned split or a second polyvalence after 67.
- **redteam-55-polyvalence (gather-only input, no verdict):** 55's class
  holds three readings — 'prend'-stem word-internal at the 55-61 ×3 windows
  (@1205 promoted: "this [43] takes [21]"), 're'-prefix at the 55-81 ×6
  windows (stems repas/regard/retour survive only at @523), determiner
  separate-word (KILLED: 1 clean pre-noun slot of ≥2; W3 @1205 forces
  word-internality). 11-vs-1 tension: 11 windows separate-word-shaped vs 1
  forced word-internal — positional-polyvalence-shaped under §7's
  sole-polyvalence rule; the internal letter split ("reprenne" vs "prend")
  is unresolvable at battery grade. Red team adjudicates.
- **Verb-shaped 91 at @277 (battery-affirmed, not adjudicated):**
  noun-91-nondet-windows (N345) kill-grade contradicts nominal-91 at @277
  and reads verb-shaped 91 there, but the promote was not made — this is a
  hypothesis needing ≥2 independent checks before it enters §4.
- **41's tier (split-41-redteam venue):** F274 (noun-class at @5) and F275
  (standalone word at @808) are locus-level battery promotes; the global
  tier stays with the red-team docket. Note: F274 corrects val-41-word-
  census's same-day "STANDALONE forced" judgment with cause — a worker
  judgment, not a standing; §7 untouched. The wordinternal-41-census
  (N367) supplies the evidence package (19 windows, 0 immediate GT-letter
  neighbors).
- **20's exact word:** F270 names only the relative-adverb subclass at @1703
  (où/quand/comment) with zero new assumptions; the exact word is
  poly-20-docket venue per R20-126.
- **qui-fol-23-26-value escalation (N363):** copula/verb value carries for 23
  (3 legs) and 26 (8 legs) but is unnameable at battery grade — the only
  nameable value is "est", blocked by provisional 59=est under §7's
  sole-polyvalence rule. Red-team polyvalence/homophony decision needed.
- **Poly-31 venue:** val-31-1257-word (N365) leaves the word-internal "[31]er"
  arm open and flags the shared presupposition (all three arms assumed the
  "[31]er" word shape; `locus-1257-reseg` tests "31 | 29") — poly-31-docket
  is red-team venue.
- **tonic-66-rearm (gated):** the personal-tonic stream fence (N334, wave-16)
  can only re-open on two preconditions jointly: 77="le" killed AND 00's
  class re-scoped. The @714 "00 66 86" geometry survives but its candidate
  does not.
- Queue state (read-only cross-check): not re-read in this fold — the 14
  fresh inbox notes carry queue-entry confirmations for their own targets
  only.

### Sweep deltas — backlog fold 3 (2026-10-09 UTC)

- **Gate status this batch: no gate satisfied.** Zero gate claims in all
  10 reports — no worker claims any gate satisfied, armed, or re-armed.
  No battery promote of 62='il' anywhere; 62='il' kill-grade dead is
  reaffirmed (R19-097/R19-106/R20-125). 78='ver' untouched (DEFERRED, R20,
  R16-005 LEAD). Per the gate rule, nothing here can fire a gate trigger.

- **redteam-23-26-copula-input (gather-only input, no verdict):** the 11
  parent-inventory legs re-verified byte-exact — 23 (n=8): 3 copula/verb
  legs (@182/@679/@1609); 26 (n=17): 8 legs (@155/@406/@531/@601/@842/
  @934/@1628/@1769). The only nameable value is "est" — homophony with
  provisional 59=est, which needs a red-team polyvalence grant under §7's
  sole-polyvalence rule; any other value would be invention. The package
  is handed to the red team with zero battery-level naming. Granted
  anchors: 64=qui, 45=ce (A11), A1 predicative set {37,32,42}, A15
  84="on", A2 SPLIT GRANTED; provisional: 59=est (the homophony
  incumbent). Comparison context: 59→A1 11/27 (40.7%: 37 ×6, 42 ×2,
  32 ×3) vs 23→A1 1/8 (12.5%) vs 26→A1 3/17 (17.6%) — frequency
  uniformity is necessary but insufficient for homophony (§7).
  @182 bytes: "14 24 87 64 [23] 37 06 00 33".

- **Queued follow-ups this batch (for the supervisor):**
  et-regne-wider-register, redteam-508-reread, det-62ne-1772-select
  (from 62-regne-trone-final); reinforced-head-excl-adj-drama,
  pour-inf-excl-topic-census-drama, redteam-reinforced-head-closure
  (from reinforced-head-governed-topology-drama); val-01-in-an-retest,
  val-01-ainsi-test, redteam-01-rival-input (from val-01-rival-sweep);
  poly-31-docket-input, val-61-wordbound-1257, locus-1257-reseg (from
  val-31-1257-word); val-41-40-classconfirm, letter-41-qui40-compose,
  a101-phase-40-reaudit (from val-41-40-independent);
  val-86-voir-orthography, val-83-de-98frame, inf-86-pour-frame-corpus
  (from val-86-inf-locus); stem-26-nent-verb (from word-12-06-1121).
  Middle groups and post-41 boundaries are now worth their own batteries
  (from wordbound-41-pour-cluster).

### Sweep deltas — backlog fold 4 (2026-10-09 UTC)

- **Gate status this batch: no gate satisfied.** None of the 6 reports
  claims a gate trigger. Checked against
  `code/crowd17/report_inbox/processed/next-token-redteam-r20.md`: the two
  promotes (val-08-successor-class, val-52-630-frame) are battery grade
  only — NOT red-team ratified — and neither is keyed to a gate; the gate
  rule stands (a battery promote the red team rejected or has not ratified
  does not satisfy a gate trigger). val-52-630-frame's 08="t" premise is
  explicitly conditional on battery-grade `battery-val-08-letter-census`,
  with independent distributional corroboration (08 never standalone in
  18/18 windows). ne-508-reseg-gate62 stays refused: 62='il' remains
  KILLED at kill grade (R19-106, R20-125). No gates armed or fired by this
  batch.

- **"prière" (41=p) lead, re-runnable but provisional:** letter-41-
  dist2-tri's strongest reading — @59–63 gives "prière" as the unique
  common word IFF 08=r — is not kill-grade: the segmentation (@59–63 vs
  @59–62) is underdetermined and 08 is value-open. The fence stands (41
  stays outside the letter tier) until two follow-ups land:
  letter-41-08-rerun (P3, re-test W1 once 08's letter value banks) and
  wordbound-41-59-seg (P3, boundary evidence to force the segmentation).

- **noun-38de-1829-host venue:** syll-83-de-1829 kills only the verb host
  at @1829; the '-de'-final NOUN as subject of finite 24 stays live.
  Follow-ups for the supervisor: noun-38de-1829-host (P3 — name the noun,
  parse "86 29 82 38 83 24 82 16"; candidate "mode" if 38='o') and
  syll-38-value-census (P3 — 38's 7 windows @384/@826/@1113/@1343/@1469/
  @1650/@1828). 38's value discriminates the noun candidate and the "82 38"
  / "38 82" letter contacts.

- **verb-21-second-leg venue:** val-08-successor-class batteries 21's noun
  class (5 legs) but leaves one fenced tension — @134 "qui 21 65" forces
  a verb reading on a single leg. A second verb-frame 21 window (or a "64
  21" wordhood re-parse) decides whether 21's split is real; the
  split-declaration bar is unmet until then.

- **split-52 red-team input (gather-only):** val-52-630-frame's second
  follow-up, split-52-redteam-input (P2), packages 52's locus-level tiers
  (verb "qui 52" ×2, adverb "ne 52 [INF]" + "la plus" ×3, sub-lexical
  "t52"/"pre52") for a 52 split/non-uniformity docket item mirroring the
  88 treatment — no adjudication asked here; word-t52-630-identify (P3)
  targets the "t[52]" word at @630 once 52's letter value or 63's class
  constrains the "et X et Y" coordination.

- **val-42 consequence:** the [42ne]-noun kill (N380) forces the three
  '42 94' windows into composition (b) — "[42-N] + ne(clausal) + X" —
  already the standing alternative per subj-42-class C3. No new
  hypothesis; the hypothesis space narrows.

- **Queue state (read-only cross-check):** not re-read in this fold — the
  6 fresh inbox notes carry queue-entry confirmations for their own
  targets only. Null/kill regenerations (letter-41's 3 follow-ups,
  syll-83-de-1829's 2, val-08's verb-21-second-leg + cet-08-975-1592,
  val-52's 2) are for the supervisor to queue.

### Sweep deltas — backlog fold 5 (2026-10-09 UTC)

- **Gate status this batch: no gate satisfied.** doublet-41-589 claims no
  gate trigger; no red-team adjudication touched.
- **Doublet-41 follow-ups (for the supervisor):** doublet-589-97-role
  (pin 97's class from its 10 windows), doublet-589-09-role (pin 09's
  class from its 12 windows), linebreak-repeat-audit (test the scribal-
  dittography rival across all 69 row breaks).

### Sweep deltas — backlog fold 6 (2026-10-09 UTC)

- **Gate status this batch: one legitimate gate satisfaction.**
  laisser-unique-sweep's R19-188 claim verified against the red-team
  record (`code/crowd17/report_inbox/processed/next-token-redteam-r19.md`
  line 1193: RATIFY the porter+envoyer eliminations, conditioned on the
  "82 16" segmentation — condition checked against frame-82-16, null
  2026-10-09). No other gate claims in this batch. Both other PROMOTEs
  remain battery-grade, red-team ratification pending: 97's VERB-class
  promote lands against the live R18-009/R18-023 rejection of
  frame-97-profile (red-team venue); en-988's locus promote confirms
  evidence the redteam-01-split-docket already gathered (no adjudication
  yet).
- **Follow-ups for the supervisor:** split-97 (suggested red-team docket
  — formal declaration of the 97 verb-class vs @751 letter-tier split);
  adj-37-76-rerun (P3, gated on s5-37-385-adjudicate);
  adj-37-nounwatch (P4); la-379-span-test (P4); det-52-arm-kill (P3);
  np-43-determiner-census (P4); residual-86-83pair (P4);
  residual-86-557-fois (P4); redteam-86-residual-closure (P2,
  gather-only); un-71-gender-frame (P3); un-41-vs-71-homophony (P3);
  quant-71-rerun-neighbors (P4); 16=inf discriminator (frame-82-16 —
  gates the laisser value); 85=inf (stem-85); a7_10 offset validation.
  (doublet-589-09-role already queued per N381; s5-37-385-adjudicate,
  redteam-86-split-docket, redteam-01-split-docket already open.)
- **§6 venue — redteam-55-polyvalence input package (gather-only, no
  verdict):** re-derived 55's 12-window census byte-exact (followers 81×6
  / 61×3 / 83×2 / 68×1; 61↔81 zero contact stream-wide); three resolution
  options recorded for red-team decision, none adjudicated: (A) second
  polyvalence — 55="prend"-stem @1205 vs 55="re"-prefix at the 55-81 ×6
  windows; (B) positional segmentation rule — "55 word-internal iff
  followed by 61" covers all 12 with zero exceptions; (C) uniform
  verb-class (R19-077 battery-grade) blocked at W2 and W6. Missing
  evidence: re81-W2-noun-discrim and re81-W4-02-class still queued —
  re-package after their return proposed. Citations R20-034/R20-045/R19-077
  verified verbatim in the R20 round report. No §7 polyvalence declared.

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
8. 77="le" — **PROVISIONAL (demoted round-16; R17-023 confirms)** — the
   "le la" adverse is dissolved (all three co-occurrences parse); three
   independent legs on banked values; the load-bearing frames (A8, A13,
   A15-C1) get stronger; the A15-C1 **elision leg is battery-PROMOTED**
   (F105: 77→84 ×7, all intra-row, zero other vowel-initial
   followers); the R16-001 docket advances: the 76-noun battery (F104)
   resolved in favor, so 77="le" is re-evaluable by the red team — the
   80/89-verb battery still needed, then two of @832/@516/@870/@1042
   upgrade to clean legs. @1031 "[inf] [80] le la" stays fenced
   (enclitic+break).
9. **Wave-5 queued work orders:** donne-168-708-leg (2-window leg
   battery — "on donne 21" @168, "35 donne 71" @708; 53-12-41/44
   fenced out); donn-41-44 (name 41/44 with ≥2 frame-legs each; if
   either is a vowel-letter or inflectional ending, re-open prof-53
   under 53="don"-stem); ne-census-1248 (re-derive the 12-48 census
   as ×5, restate negation-'ne' as 3 clean + 2 disputed, correct
   downstream citations of the ×7 gloss); split-92 question (split
   vs second polyvalence vs governor misread) is red-team-only, §7 —
   the corrected evidence package (follower scatter: five 2× pairs)
   is in the adjudication queue.
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
15. **Rounds 11–12 complete and ADJUDICATED (2026-10-07)** — round 11:
    docket CLOSED 7/7, 0 promotions/0 kills/0 demotions, baselines
    148/148 + 100/100 (F77–F83 granted: ISLET 3 survives; 33=
    infinitive-class; este-verb H0 holds; "peu" 4/8; @633
    et-CONDITIONAL; 48 stays UNIDENTIFIED). Round 12: docket CLOSED
    13/13 (R1–R7 + French-blitz R8–R13); net 1 provisional-conditioned
    classification (31=VERBAL finite), 2 kills (unconditioned-48="de",
    kill-grade 10 windows; "gouvernement" thread, all 7 windows), 1
    demotion (77="gouv"→disfavored), 1 retirement (é-initial-noun
    theory); 33-value paradox RECORDED; "peu" 4/8→5/9 with double-pour
    EXPLICIT FENCE (~22MB); -este H0 holds on T1–T5; lead 21="ce". **Round-13
    (council) executor recommendations await red-team adjudication:**
    systematic drag (9 hits, 6 new LEAD-grade, FDR≈1.4 — leads, not
    discoveries); carry-classes (33 NULL, 31 CONFIRM, 92 NULL); four
    homophone SPLITs ({33,86}, {48,94}, {52,59}, {76,78}); islet audit
    (5/10 dissolve → word rules, 67 the only true polyvalence, 59
    monovalent "est"); missing-mass inventory (~17 missing cells among
    the 84 unidentified, 0 for identified syllables; digit hunt NEGATIVE
    — retire); word segmenter (72/1847=3.90% coverage, 32 segments).
    Smith round 2 remains rebuild2-side (main-fleet scope ZERO until C1);
    Track A H1 SUPPORTED (M_d=+2,200.68), Track C v3 NULL-v3, Track D
    Experiment 0 SLIDE — likelihood lesion triply confirmed.
16. **Fig5 refresh still queued** — the board list in
    `code/make_report_figures.py` is hardcoded through crowd rounds
    1–5 + sidepaths; rounds 6–11 rows (62 battery, redteam F26-17, T4,
    bedrock, F60–F76, ISLET 10, @1351, @1248 arms) require editing the
    `board` list and re-running exactly as documented. **Not done this
    sweep: fig inputs in `data/` (attempt1–3_results.json, quadgrams,
    Gutenberg texts, upstream R5005 files — all mtime ≤12:32 today) are
    unchanged since the PNGs were built (16:09 today), so no figure was
    regenerated.** Figs 1–4/6 are
    current; fig6's χ²=366.3 annotation carries the memo3
    noisy-detector caveat (F62).
17. **Round-16 queued batteries (ranked by the batteries themselves):**
    65 full profile (priority 1 — highest-value unknown); 78="ver"
    word-level confirmation (before 45's battery); 45 ce/dict battery;
    94="ne" (needs 62="on" promotion or a clean "ne"+banked-verb leg);
    12="n" second-leg hunt ("ni"/"en" disambiguation); 33="dire" idiom
    battery (blocked by 29-89-84 / 29-82-16 "erreur" shapes); 47-predecessor
    distribution + 47-33 bigram (the "se" frame); 76/68 verb-hood (decides
    qui-ce vs qui-se — red-team escalation clause if verbal); 32
    adjective-vs-verb class battery; 30="pas" 19-window census; 37-syllable
    battery ("cern" test); 26 noun-vs-verb; 08 disambiguation (ne/se/on vs
    spelling-letter); 80-distribution (determiner vs mystery); 86-value
    battery (12× "pour 86" bedrock + "00 86 56" ×4); 93/86 infinitive-stem
    test (67 rule); 84 -este-verb tension (red team); 76 gender tension
    (red team); @1196 doubled 82-16 and @369 70-polyvalence (red team);
    12~30 / 44~63 / 60/62/68 homophone batteries; 43 feminine-noun;
    81/91/88/44/73 cell batteries; 03 profile; "entrepre[12]" paradigm;
    21 battery. Do NOT promote on any of these without the lane's ≥2-
    independent-checks bar + red-team ruling. Durable infrastructure for
    the queue landed 03:32 UTC: `code/crowd17/next-token/` (battery-
    queue.json as single source of truth, BATTERY-PROTOCOL.md,
    locks/ with 90-minute stale-lock semantics, finder-beats registry)
    + `code/crowd17/report_inbox/` as the next sweep's inbox.
18. **crowd15/next-token calibration** — `calibrate.py` running since
    2026-10-08 01:41 UTC; fold the top-1/3/5, MRR, solved-context ranks
    and by-ear mismatch numbers into the report when `calibrate.json`
    lands (currently 0 bytes; log stalled at "[byear] targeted contexts"
    since 02:28 UTC — if still stalled next sweep, treat as a stuck run).
19. **track-b** — training resumed and live (upd 13,500, epoch 7, best
    heldout 2.0198 @upd 13,200, still declining). Continue on the numbers.
20. **Smith** — step-4 clearance request filed; await solver-side red-team
    ruling. Memorization re-probe CLEAN is banked as a control result.
    `FLEET-CHARTER.md`'s "probe still parked" line (01:53 UTC entry) is
    STALE — the jsonl shows the package delivered and the probe CLEAN;
    charter should carry an addendum next sweep. Grid registry refreshed
    01:47 UTC; the 77-promotion and 78 "er"-kill await coordinator merge.
    **Update 2026-10-08 ~07:21 UTC: coordinator merged the registry
    (round-17 battery verdicts as leads: 12/30/39/45/48/94/06 leads,
    00 prom, 77 prov, 78 "ver" lead) and regenerated the grid; the
    sweeper's `generate.py` printed UNCHANGED — grid current.**

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
├── clause-730-decode.gif       @729–735 clause decode animation (F230; green = confirmed, amber = illustrative)
│   + clause-730-decode.gif.py  generator script
├── report_inbox/              ← worker notes land here; processed/ after sweep
│   └── processed/             ← folded into REPORT.md (136 notes;
│       plus crowd-local processed/ dirs next to their inboxes — 962 battery
│       notes in code/crowd17/report_inbox/processed/ to date)
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
| 46 | que | pencil crib (ground truth) — independently RE-DERIVED round-13
(KE2-A, adjudicated: two legs, rank-match + predecessor-profile) — GT
keeps, ISLET 10's dependency on 46=que stands (not conditional) |
| 87 | ce | PROMOTED (round-15 A4 battery; registry "prom") |
| 64 | qui | PROMOTED (registry "prom") |
| 96 | par | PROMOTED (registry "prom") |
| 17 | fois | PROMOTED (registry "prom") |
| 79 | tout | PROMOTED (round-15 A5; registry "prom"; round-16 tout-battery CONFIRM; 2 fenced qui+tout residuals @396/@1227) |
| 94 | ne | STRONG LEAD — "n'est" ×3 @558/@762/@1795, "ne me/m'" ×4 @578/@1182/@1353/@1742 (round-16 pre-battery); promotion DECLINED (R16-006; R17-001 REJECTED the promote — no new byte evidence; stays STRONG LEAD); @578 thread closed |
| 06 | ent | **PROMOTED (conditional, R17: fork closed at battery level, F97 ratified** —
ratification): verb-ending syllable; the verb-ending vs adverb-ending fork is
DECIDED at battery level ("[X]-06-11" frames parse only as verb+object);
"-ment" = 82+06 compositional, not a standalone 06 value |
| 67 | et/veut | fork RESOLVED positionally (round-16 forks battery, LEAD-grade): "veut" iff the follower is infinitive-shaped (8/38: 33 ×6, stem+29 ×2), else "et" (30/38), zero adverses; circularity caveat recorded; independent test = 93/86 infinitive-stem predictions |
| 77 | le | **provisional** — DEMOTED prom->prov round-16; R17-023 CONFIRMS (no new evidence; R16-001 stands). Docket: 76-noun battery (F104) resolved in favor — 77="le" now re-evaluable by the red team; 80/89-verb battery still needed; then two of @832/@516/@870/@1042 upgrade to clean legs. A15-C1 elision leg PROMOTED (F105: 77->84 x7 elides before vowel-initial 84; value untouched). "gou" exception stays fenced |
| 31 | VERBAL (finite) | provisional-conditioned — 3 disambiguated verbal
windows (@338/@1647/@1489); conditional on C1 provisionals (64="qui",
87="ce") + 08="l'" lead; era leg E31-1 VOID (round-12 R3 GRANT);
round-16 class CONFIRM: 8 followers 8/8 distinct (class-tier signature) |
| 21 | ce | lead — post-hoc 1 check (F-E W-slot "ce" 14/29, demonstratives
62%); homophonic collision with 87="ce"-prov allowed; rival 21="me"
ungranted (round-12 R1) |
| 20 | fois | lead — "la première fois" @1034 GRANTED (three legs); 20="fois"
homophone battery warranted for round 13 (round-12 R10) |
| 33 | INF class + "dire" | class provisional (round-12 R1); **"dire" LEAD** (round-16
classes battery): "67 33 46" ×2 idiomatic under BOTH 67 forks, "47 33" ×2,
"33 21 64 37" ×2; promotion BLOCKED by P2 ("33 29" ×5 puzzles all candidates —
29-8X word-shapes must resolve); vouloir KILLED, penser weak; value paradox stands |
| 77 | gouv | DISFAVORED — demoted round-12 (R9); gouvernement/gouvernent thread
dead at all 7 windows (N44) |
| 62 | "on" | **KILLED unconditioned (R17-017**: 62->94 x9 vs 84->59 x4, zero crossover; §7 forbids a second unconditioned "on" against the A15 84="on" grant); **"il" battery-PROMOTE (F103: 32/35 subject windows, pending red-team ratification; registry lead)** — the live reading is now "il" |
Méhémet-Ali 62='a' tension fenced (round-12 R8, not a kill-threat) |
| 78 | me (syllable) | lead — L1s 1.131×; "me"-word disfavored-strong (L1w 22.76×) |
| 78 | ver | LEAD — **"er" arm KILLED distributionally (round-16 forks battery; R17-014 CONFIRMED** (round-16 forks battery:
determiner-predecessors 16/31 vs 29="er" 2/45; after 33=INF 0 vs 5; OR ~22.9);
"ver" survives unproven; "verdict" ×4 word-level support; old F61 downgrade superseded |
| 45 | ce/dict | **HOLD** — 45="ce" DEMOTED from PROMOTE (round-16 forks battery: "ce verdict"
×2 forces "dict" @573/@982; "par ce" ×2 forces "ce" @602/@1213; @314 contested);
**"ce/dict positional allophones" LEAD** (conditional on 78="ver") |
| 52 | pas | lead — vs "se"/"so" rivals (F23/F26) |
| 24 | finite verb (modal-shaped) | **PROMOTED (class tier, R17)**: (F99) finite-verb slots @547/@955/@1693/@311/@474/@1486, infinitive-taking
24→85 ×5 / →89 ×3 / →80 ×2 / →82→16 ×2; VALUE NOT named — the old "24 = en"
reading is excluded by the verb class; "est" already refuted |
| 47 | ce | **PROMOTED** (allophone tier, round-15 A4; registry "prom"); round-16 ce47
battery: 28/28 windows re-derived, NO value break (allophone HOLDS); positional spec
now names two exceptions (never-after-24 unconditioned/@548 conditioned, never-before-64);
**"se"-after-infinitives competing LEAD** (allophony, not polyvalence) |
| 48 | e | **PROMOTED (letter tier, R17-003** — 38-window sweep: "ne" x5 via 12-48, "me la" @126 [82="m" GT], feminine/mute-"e" x5, "[89]-e" verb+ending x3; R16-007 decline OVERTURNED); general value; A7-L2 verb-stem frame NARROWED to exclusive legs @1229/@1589 (R17-024, conditioned frame — not a second polyvalence) |
| 76 | noun (masculine) | **battery-PROMOTE (F104, pending red-team ratification; registry lead)** — R16-001 docket condition satisfied: 'le [76]' x3 legs resolve in favor |
| 59 | est | STRONG LEAD — executor-grade, pending red-team (F44); ISLET-10 conditioned;
round-16 est battery: **37/42 predicative frames DEMOTED→HOLD** (0 valid legs each);
**32 est-frame STANDS (3→2 legs: @316/@1210)**; 19 HOLD (@1777, 1 leg) |
| 00 | pour | **BANKED** (round-15 A9 red-team grant; round-16 pour-battery CONFIRM):
~50/55 windows clean-or-neutral; fenced adverses @1247 (strongest), @864 (cheapest decisive
test), @291/@685 (new, "pour"+subjunctive), @1287; ~5× register-rate adverse (2.978% vs
0.592%) — split battery queued |
| 84 | on | **GRANTED (round-15 A15) — WEAKENED round-16**: "on est" legs VOID (59 ESTE/FENCED);
keeps 59-independent legs ("qu'on en" ×2, "mon" @166, "l'on" ×7, 84→24 ×3);
3 fenced residuals (R1 @1619 "la on", R2 @1664 "ne on", R3 @146 new);
ESTE-verb tension flagged for red team |
| 30 | pas | **PROMOTED (conditional, R17)** — ne-frames @559 "n'est 30" + @1715 "ne [V] 30" (round-16 est battery);
19-window census queued |
| 12 | n | **PROMOTED (letter tier, R17-002**: 40-12 "en" @64 [40="e" GT], 12-34 "ni" @1740 [34="i" GT], 70-12 "pren" @347/@1118/@1547 [70="pre" GT]; 0 contradictions in 23-window census; upgrades R16-010 LEAD); 12-48 = ×5 (×7 gloss corrected R17) |
| 39 | /a/ | **LEAD (allophone, R17-005**: R16-011 HYPOTHESIS upgraded — three /a/ frames, zero forced contradictions, "a qui" French correction noted) — "qui a" ×1 @606, "pré-a-la" ×2, "n'est [39]" @763 |
| 32 | one verb lexeme | **PROMOTED (class tier, R17)**: (F98 battery)
finite 3sg + past-participle forms across all 13 windows; the adjectival function
is the participle of the same lexeme — adj-32's dual-behavior question dissolved,
no second polyvalence needed |
| 81 | masculine noun | LEAD — 77-81 ×4: "le [81] pour [33-INF]", "le [81]. Cela" (round-16 le-battery);
"prin" reading dead |
| 78-45 | même/verdict | CONTESTED — "le même qui" lock @313 (F47, executor-grade, pending red-team)
vs **"verdict" ×4** (round-16 forks battery: "ce verdict" ×2 @573/@982)

Banned (asserted-absent, from the skeleton ledger + adjudications):
77=pas, 77=que, 06=/mɑ̃/ (standalone adverbial reading; 06="ent" is now
battery-PROMOTED, F97), 96="de", 47="me" (word reading),
01="ci" (general value, F100; bound "-ci" in "ceci" fenced, not dead),
01="faisant" (general value, F100; word-internal readings fenced, not dead), 84="plus" (via 59="est"), 84="a", 84=verb-class, **78="er" (round-16 forks battery, distributional kill; R17-014 CONFIRMED)**, "enne" one-word composition (R17-016 — 34-29-40-12-94 @61 = "ierenne" admits no French word), the ne-06-317 gate claim (R17-025). Fenced
(conditioned-or-dead): 43="me" (downgraded MEDIUM→WEAK — 96→43 "par me"
era-dead; F48); 47="ce"'s positional exceptions (round-16 ce47 battery);
00="pour" adverses @1247/@864/@291/@685 (round-16 pour/i batteries).

*Rank convention: figure labels use 1-based positions in the frequency-sorted
list; lane code and NOTES.md use 0-based indices (figure #N = code rank N−1).
Parse convention: 1,847-pair repaired parse; old-parse indices ≥773 shift +1
(see `code/crowd4/REINDEX.md`).*
