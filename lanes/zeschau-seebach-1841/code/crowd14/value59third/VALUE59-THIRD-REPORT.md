# VALUE59-THIRD — @825 third-value hunt (round 14)

## 1. @825 byte-exact re-derivation (±5, repaired stream)

Rebuilt from `code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`
via `repair_stream.py` (upstream tokenization `[s[i:i+2] for i in range(o, len(s)-1, 2)]`;
NEVER `canonical.py`). 1,847 pairs; crib `11 70 82 34 29 40` pair-aligned @754/@1034. ✓

| pos | grp | row | value |
|---|---|---|---|
| 820 | 40 | a5_05 | e (pencil GT) |
| 821 | 95 | a5_05 | — |
| 822 | 13 | a5_05 | — |
| 823 | 24 | a5_05 | "en" (F31 STRONG lead) |
| 824 | 87 | a5_05 | ce (provisional) — **last group of row a5_05** |
| **825** | **59** | **a5_06** | **? — first group of row a5_06** |
| 826 | 38 | a5_06 | — (n38=7, all windows distinct) |
| 827 | 82 | a5_06 | m (pencil GT letter) |
| 828 | 01 | a5_06 | — (01="ci" KILLED, K4 provisional) |
| 829 | 24 | a5_06 | "en" (F31) |
| 830 | 87 | a5_06 | ce |

±10: `49 74 74 47 78 | 40 95 13 24 87 | 59 | 38 82 01 24 87 11 | 77 76 59 35`
(@831=11=la GT, @832=77, @833=76, @834=59, @835=35.)

Notes: (a) the 87|59 split sits **exactly on the manuscript row break** a5_05→a5_06;
(b) n59=27 re-verified; **@825 is the ONLY 87-59 window in the stream**;
(c) 24-87 occurs 10× (@74/@163/@180/@191/@644/@824/@830/@1487/@1767/@1775):
«en ce qui»×3 (@180/@1767/@1775), 24-87-11×3 (@74/@163/@830).

## 2. «en ce»+noun corpus test

Pool: `code/side-period/corpus/` minus `nesselrode-v8.txt` = **4,125,343 tokens**,
lane `tok_elision` verbatim (`ence_frame.py` → `ence_frame_results.json`).

- «en ce» = 441: moment 195, qui 76, genre 32, cas 21, sens 19, monde 14, temps 10,
  jour 6, lieu 6, pays 6, point 3, … — frame is **noun-or-qui**, as the frame map said.
- **«en ce» + est-initial word: 0/441.** No est-initial word ever follows «en ce».
- ⇒ 59 (the est-syllable) **cannot be the first syllable of the noun** after «en ce».
  The «en ce»+noun-with-59 parse is corpus-dead. (59 = the noun? NO. Part of it? NO.)

## 3. Ranked grammatical readings of @825

### R-A — LEAD: 87-59 = «c'est» (ce+est elided); 24 = clause-final «en»
Parse: `[…13] en. C'est [38=pred] …`
The frame map's «ce est»=0 kill tested only the **non-elided** bigram. French elides
«ce»+«est» obligatorily → «c'est»; with `tok_elision`, «c'est» → `c' est`.

Legs (4, independent):
- **L1 — adjudicated mechanism precedent.** W-est1 (93-59=«l'est», R-IA1 GRANT):
  elided-proclitic + 59 is already a banked word rule. 87-59=«c'est» is the same
  construction with 87=«c'».
- **L2 — corpus.** «c' est» = **8,147**/4.1M vs «ce est» literal = 0. Elision
  obligatory; elided form massive.
- **L3 — elimination.** «en ce»+est-initial = 0/441; «de ce»+est-initial = 0/2733
  («de ce»: qui 227, que 215, genre 130, pays 89, côté 76…); -este needs a verb
  stem (pre=87≠stem); «c'est» is the unique grammatical ce+est word.
- **L4 — diplomatic parallel.** «[X] en, c'est [pred]» directly attested in 1840s
  despatches (raw-text grep): Guizot t5-t6 «en Orient, c'est la paix»,
  «en Asie, c'est le commencement», «vous en avertit. C'est son état»;
  Levant 1841 «en Syrie. C'est par de pareils faits»; «en ce moment, c'est d'en
  bien marquer…». The pronoun-«en»-then-«c'est» clause boundary is era-normal.

Fence items (named missing legs for promotion):
- **F-a:** 24="en" is STRONG lead (F31) but unconfirmed — and must be clause-final
  (same-clause «en c'est» ≈ 0; apparent hits are «en [year]. C'est» artifacts).
  Needs 24 confirmation + left-context (13/95/78/47/74) support.
- **F-b:** 38 = predicate after «c'est» — unidentified (n38=7, all distinct windows).
  («c'est»+le/la = 534/517; «c'est le même» = 3 — weak.)
- **F-c:** single 87-59 window — a second occurrence would clinch the word rule
  (call it **W-cest**).

### R-B — FENCED: 24-87=«en ce», 59-38-82-01=«moment» (59=«mo», genuine third value)
- For: 24-87=«en ce» is a real 10× frame; «moment» is the #1 «en ce» follower
  (195/441 = 44%); wider context even has «en cela» right after (@829-831).
- FENCE (0 legs + adjudication conflict): no independent leg for 59=«mo»;
  **contradicts R-IA1** («59 monovalent est syllable», GRANT); 38/01 as
  «ment»-pieces untestable and order-awkward (38-82-01 vs «ment»=m-ent).
- Named missing legs: second «en ce»+59 window; independent 59=«mo» frame;
  38/01=«ment»; R-IA1 overturn.

### R-C — DEAD: 24=«de», «de ce»+59. No est-initial follower of «de ce» (0/2733).
### R-D — DEAD: 59=«-este» verb-final. pre=87=ce is not a verb stem.
### R-E — DEAD: 87-59-38 as one French word. None exists.
### R-F — DEAD (standing, not re-litigated): 59=word-«est» after «ce» non-elided. «ce est»=0.

## 4. Generalization test (other leftovers)

| pos | window | reading | 59's value | «c'est» applies? |
|---|---|---|---|---|
| @463 | 79-87-11-59-42 | «cela est [42]» (87-11=«cela» over-split; «cela est»=173) | est (word) | No (87 not adjacent to 59) |
| @834 | 11-77-76-59-35 | «[76] est» iff 76=noun | est (word) | No (pre=76) |
| @1511 | 41-12-61-59-39 | pre=61 ∈ W-este2 stems → «[61]este» candidate | este-arm | No (pre=61) |
| @1833 | 24-82-16-59-36 | «m'y est» strained — open | ? | No (pre=16) |
| @1496 | 00-66-15-59-24 | «reste en» (15-59=«reste», 21 hits) | est syllable, word-internal | Analog only |

**Verdict:** @825 is sui generis as the sole 87-59 window, but not anomalous — it is
the predictable «c'est» word-rule, structurally parallel to adjudicated W-est1
(93-59=«l'est»). None of the other leftovers needs a third value either; @1496
(«reste») is the closest analog — the est-syllable occurs word-internally in more
words than the conditioned pre-frames cover. Bonus: 24-87-11 ×3 (@74/@163/@830)
supports the 87-11=«cela» over-split (relevant to @463's F1-WATCH; «en cela»=49).

## 5. 59's value inventory after round 14

- **est-syllable, monovalent per R-IA1** — word inventory EXTENDED this round:
  - W-est1: 93-59=«l'est» (@103) [adjudicated]
  - W-est2: 94-59=«n'est» (@559/@763) [adjudicated]
  - F-qui-est: 64-59=«qui est» (@316/@1210/@1777) [adjudicated]
  - **W-cest (LEAD): 87-59=«c'est» (@825)** — 4 legs; fenced on F-a/F-b/F-c
  - «cela est» @463 (F1-WATCH; needs 42)
  - «reste» @1496 (15-59; «reste en»=21)
- W-este2: [stem]-59, stems 84/06/61/44/86 (@1190/@1448/@1804 firm; @1291 fenced)
- Sub-tier verb-units @216/@1186/@448/@1715/@554 (fenced)
- S5-fenced ×6 (@528/@624/@912/@1178/@1443/@1796; pending 37=«le»)
- Leftovers: @834 (76=noun?), @1511 (61-59 este?), @1833 (open)
- **Third value: NONE FOUND.** @825 does not require one. The «en ce»+noun frame
  was a misparse — the frame map's «ce est»=0 missed the elided «c'est».
  The «en ce moment»/59=«mo» rival is fenced at 0 legs + R-IA1 contradiction.

## Artifacts
- `repair_stream.py` — byte-exact repaired-stream builder (replaces canonical.py)
- `ence_frame.py` → `ence_frame_results.json` — «en ce»/«c'est»/«de ce» corpus battery
- Raw «en, c'est» diplomatic parallels verified by raw-text grep (Guizot t5-t6, Levant 1841)

## Constraints honored
No re-litigation of unconditioned-59 (REFUTED), «ce est»=0 (standing),
{52,59}/{76,78} splits, or any settled round-11/12/13 fence. ISLET 10's word rules
used as W-est1/W-est2/W-este2/F-qui-est per R-IA1. No promotion claimed —
LEAD-grade with named fence items, for red-team adjudication.
