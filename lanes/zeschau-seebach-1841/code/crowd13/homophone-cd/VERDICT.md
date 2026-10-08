# VERDICT — Homophone-set batteries {52,59} & {76,78} (round 13 WO2)

Date: 2026-10-07. Executor: homophone-set-battery. Pre-reg:
`code/crowd13/homophone-cd/PREREG.md` (written before any new data query).
All cipher counts re-derived from the repaired 1,847-pair stream
(`code/crowd6/redteam/verify_baseline.load_stream`); era rates on the
clean-diplo pool with the lane tokenizer verbatim (N=3,618,487 here vs
3.87M in frame59-map.md — same files, minor tokenizer drift; all test
frames massively attested either way, conclusions rate-robust).
v8 VOID for phrases. `code/council/drag/drag_hits.json` does not exist —
nothing consulted.

## Verdicts

| Set | Verdict | Basis |
|---|---|---|
| {52,59} | **SPLIT** | Not free homophones. -este arm (pre=84) exclusive to 59 (0/27 vs 4/27, Fisher exact p=0.0555); frame battery 1/7 clean. 52 keeps a WEAK est-arm lead, unconfirmed. |
| {76,78} | **SPLIT** | Not free homophones. 76 fits only the ver-tine («le ver[…]» ×3) and fails the er-tine everywhere; 4/21 windows fail both tines. 76-94 = 0 (er-diagnostic absent). |

Neither set is KILLED as a value-relationship (52's est-lead and 76's
ver-lead survive as weak local hypotheses); neither is PROMOTED (frame
batteries far below the ≥2-independent-check bar). Both are SPLIT in the
{47,87} sense: arm-segregated, not freely interchangeable. Do NOT merge
either pair in the solver.

---

## SET {52,59} — detail

### Leg B — uniformity
(27,27): χ²=0.0, p=1.0, ratio 1.0. ✓ (Trivially — identical n. Not an
independent leg, recorded for the file.)

### Leg C — cycling + predecessor segregation
- Runs test on the 54-occurrence membership sequence (stream order):
  R=23, μ=28.0, z=−1.374, p=0.17 (two-sided). Mild clumping, not
  significant — consistent with 1690 cycling. Does not reject homophony.
- Predecessor homogeneity χ² (top-6 cats + OTHER): χ²=5.68, df=6,
  p=0.46. No significant divergence — BUT the test is underpowered at
  n=27 and the linguistically load-bearing cell is:
- **-este arm exclusivity:** pre(59)=84 ×4 (@1190/@1448/@1804 firm,
  @1291 fenced — matches frame59-map); pre(52)=84 ×0. Fisher exact
  P(all 4 on 59 | H0) = 0.0555. Marginal statistically; principled
  linguistically («-este» verb-final ≠ word «est» — distinct morphemes).
  A free homophone of 59 should appear after 84 sometimes. It never does.

### Leg A — frame battery: 52 in 59's «est» frames (7 licensed windows)

| pos | frame | word-«est» parse | grade |
|---|---|---|---|
| @1342 | 64-52-38 «qui est [38]» | «qui est» era 904/3.6M, grammatical | **CLEAN** |
| @1294 | 94-52-80 «[59] 35 ne [52] [80]» | «n'est [80]» vs «ne pas [80]»; «pas» favored by K5/N29 parallel @1804 | AMBIGUOUS |
| @1807 | 94-52-80 (same 5-gram as @1294) | same | AMBIGUOUS |
| @1435 | 64-52-82 «qui est m[16]» | «qui est même» speculative; needs 82-led word | STRAINED |
| @160 | 93-52-94 «[35] [93] est ne…» | 93=«l'» needs «ne» BEFORE (cf 59@103 «on ne l'est»); here «ne» follows | STRAINED |
| @264 | 93-52-33 «[45] [93] est [33=inf]» | «l'est» + infinitive ungrammatical under banked 93=«l'» | FAIL |
| @571 | 94-52-87 «ne est ce [78]» | «n'est-ce» needs «pas»; suc(87)=78≠pas | FAIL |

1/7 clean, 2/7 ambiguous, 4/7 strained-or-fail. The prereg bar (≥1 clean
window) is met on its letter by @1342 — but a single «qui est» also fits
rivals («a», «sont»); contact-sim 0.56 to 59 is the only «est»-specific
tie, and it is the proposal's basis, not an independent check. **Not
≥2 independent checks → no PROMOTE.**

Negative control: no 52 window with pre∉{64,94,93} forces «est»
(@1007/@1124/@1722 «la 52 X»: era «la est»=0 — consistent with
CONDITIONED «est», not a contradiction). 52's non-est value is
unidentified («pas» per K5/N29 fails in most OTHER windows, e.g.
«la pas 37»).

### Implication for 52's identity
52 stays **UNIDENTIFIED**. IF est-family, it fits ONLY the est-arm
(pre∈{64,94,93}) — never the este-arm. The est-arm lead is WEAK (1 clean
frame). Open residuals: «la 52» ×3 (nominal/adjectival slot — polyvalence
or distinct value), @649's opaque «le [78] 52 m ne» window (W3, known).

---

## SET {76,78} — detail

### Leg B — uniformity
(21,31): χ²=1.923, p=0.166, ratio 1.476 < 2. ✓

### Leg C — cycling + predecessor segregation
- Runs: R=31, μ=26.04, z=+1.444, p=0.15. No clumping. Consistent.
- Pre-homogeneity χ²: 6.18, df=6, p=0.40. Overlap on {77,67,47,87,37};
  78 distinctive: 47×5, 37×4; 76 distinctive: 94×2, 48×2, 16×2. Not
  significant — weak instrument, does not reject.

### Leg A — frame battery: 76 in ver/er frames

**er-tine (78's leaned value):** 76 NEVER parses as «er».
- er|ne diagnostic: 76→94 = 0× vs 78→94 = 2× (@1181, @1352, both
  «le [78] ne m» — the 5-mer family). P(0 | rate 2/31, n=21) = 0.25:
  absence is weak evidence, but there is zero positive er-support for 76.
- «le [76]» ×3 (@833/@892/@969): «le er» ungrammatical on the er-tine.

**ver-tine:** 3/21 compatible, 4/21 fail both tines, 14/21 neutral.
- @892/@969: 77-76-1 «le [76] [1]» — «le ver[…]» («le vers/verre/vert»-type,
  76 as word-INITIAL syllable; suc=1 open). Compatible.
- @833: 77-76-59 «le [76] [59]» — «le ver[re]»-type (59's value here is
  open: pre=76 ∉ ISLET-10 licensed set). Compatible.
- @652: 94-76-49 «ne [76] [49]» — «ne ver»/«ne er» both ungrammatical. FAIL.
- @1577: 94-76-47 «ne [76] ce» — both tines fail. FAIL.
- @1273/@1275: «47=ce 76 87=ce 76 48» — «ce [76] ce [76]» — both tines
  fail. OPAQUE (recorded residual; neighbor 47=«ce~» is weak).
- @487: 64-76-42 «qui [76] [42]» — «qui» wants a verb; neither tine fits.
  (76-as-verb not in the fork — noted, not tested.)

### Implication for the 78 fork
**None directly — the fork is unresolved by this battery.** 76 contributes
no er-evidence (76-94=0) and its ver-compatibility is 76-local. The fork
stays with french-blitz (leans «er» via er|ne, p=3.2e-11; unresolved).
**Flagged tension (not tested):** «le»-frames favor ver-INITIAL for BOTH
76 («le ver[…]» ×3) and 78 («le [78]» ×7: «le vers/verre»-type parses;
«le er» does not) — against the er|ne diagnostic favoring «er» at 78-94.
Possible resolution: 78 polyvalent ver/er by position. That is the fork
owner's battery, not this one.

---

## Method notes & caveats
- Era pool here N=3,618,487 vs frame59-map's 3.87M (same file list;
  tokenizer drift). «qui est» 904 vs banked 1033; «n'est» 3354 vs 3674;
  «ne l'est» 43 vs 51. All test frames massively attested — no verdict
  is rate-sensitive.
- Pre-homogeneity χ² cells are sparse (n=21–31); treat p-values as
  coarse. The -este Fisher exact (0.0555) is the sharpest segregation
  number in either set.
- 52=«pas»-polyvalent (K5/N29) respected: @1294/@1807 graded ambiguous,
  not counted as est-frames.
- No status changes made (red team adjudicates). Solver constraint to
  bank: do NOT tie 52↔59 or 76↔78 as homophone pairs.
