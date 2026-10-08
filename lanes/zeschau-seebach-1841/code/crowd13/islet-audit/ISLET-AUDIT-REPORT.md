# ISLET AUDIT — round 13 (council work order 1)

2026-10-07 · Islet Auditor → coordinator. PREREG with per-islet bars at
`PREREG.md` (registered before any battery ran). All cipher counts re-derived
from `code/side-keyhunt/repaired_offsets.json` (1,847 pairs; loader
`stream.py` asserts crib @754/@1034). Era checks on the clean diplomatic pool
(`code/side-period/corpus/`, nesselrode-v8 EXCLUDED from all phrase queries
per work order, AZ German issues excluded; N=3,867,332 words). Code:
`battery.py`; numbers: `results.json`. **Recommendations only — no status
changes; adjudicator rules.** Settled kills not re-litigated.

## Verdict table (recommendations)

| Islet | Claim | Battery result | Recommended verdict |
|---|---|---|---|
| 4 — 67 et/veut | frame-conditioned fork | 29/38 clean, 0 BOTH, 0/38 in words, era legs 99–273:1 | **TRUE-POLYVALENCE** (keep SUPPORTED) |
| 5 — 96 verb-stem | iff pre=64 & suc=47 | singleton confirmed; era leg v8-dependent (n=1 clean) | **INCONCLUSIVE** (keep LEAD) |
| 6 — 66 class | noun/inf/pronoun | 19/19 fit, 0 adverses, 0 in words | **CLASS-RULE** (keep CONFIRMED) |
| 7 — 89 noun-class | noun | 14/14 fit, 29-89 not «premier»-fusion, 0 in words | **CLASS-RULE** (keep CONFIRMED) |
| 8 — 64-77-84-59 | «qui le [V-este]» | 84-59 = one verb; QLXE falsifier unfired (2 instances rescued) | **WORD-RULE** (re-bank as frame+word) |
| 9 — 86 | que-family (settled kill) | kill legs re-derived; {33,86} uniform (p=0.087/0.296) | **KILLED stands** (confirmed, no re-litigation) |
| 10 — 59 est/-este | iff pre∈{64,94,93} / pre=84 | 93-59, 94-59 fused words; stem-59 one verb; 59 monovalent | **WORD-RULE** (dissolve; retire polyvalence entry) |
| 1 — 84 (sanity) | «en» iff pre∈{82,66,89} | arms re-verified; 82-84=«m'en» | dissolution CONFIRMED (word + frame arms) |
| 2 — 00 (sanity) | «le» iff pre=96 | 3 windows re-verified | dissolution CONFIRMED (96-00=«par le») |
| 3 — 06 (sanity) | «ent» iff pre=82 | W06=[580,738,1184,1355] re-verified; @1351 «ne ment pas» | dissolution CONFIRMED (82-06=«ment») |

## Per-islet battery evidence

### ISLET 4 — 67 et/veut fork → TRUE-POLYVALENCE (recommend keep SUPPORTED)
1. **Lexical-bigram:** 0/38 67-windows fall inside confirmed multi-cell
   words (`m'en`, `ment`, `par le`, `en ce`, `c'est`, `la première`) —
   compositional dissolution FAILS. 67+suc never fuses («et la» two words).
2. **Residual:** 29/38 classify under the fenced standing rules
   (R_et1–6, R_veut1–3, R_et5 fence) with **zero BOTH-conflicts**; open=9
   ([199,630,633,902,1248,1372,1450,1519,1623]) — matches the lane record
   exactly. @1248 (00-67-46 «pour 67 que») is open → NEITHER-fence stands;
   it bounds the fork, doesn't kill it.
3. **Forced-context:** @506 (pre=21, suc=77) → R_et5 fenced, R_veut1 fires
   → «veut»; adjudication re-derives. GT-adjacent 67s (@394 «i et qui»,
   @753 «e et la première», @1045 «la veut», @1098/@1390 «[06]er et»,
   @1239/@1400 «e et le», @471 «[06] et que») all classify consistently —
   **no counterdatum**.
4. **Homophone-cycling:** N/A — 67 has no claimed homophone ({17,67} is
   WATCH-only, "probably not shared value").
- **Era legs (clean pool):** «et la»=4070 vs «veut la»=41 (99:1);
  «et le»=3788 vs «veut le»=33 (115:1); «et par»=819 vs «veut par»=3
  (273:1); «et qui»=2041 vs «veut qui»=2. All reproduce.
- The fork is the registry's only genuine frame-conditioned polyvalence.

### ISLET 5 — 96=verb-stem iff pre=64 & suc=47 → INCONCLUSIVE (keep LEAD)
1. **Lexical-bigram:** «ce qui [96] ce que» is a frame, not a word — no
   fusion. Dissolution fails.
2. **Residual:** exactly ONE 64-96-47 window on the repaired stream (96@150;
   ctx 29-87-**64-96-47**-46-66 = «[ce] qui [96] ce que» — note 87=«ce»
   provisional immediately upstream, corroborating the frame). n96=21;
   96-00 «par le» ×3 kills verb-stem elsewhere. No second window exists
   (F63's retired falsifier confirmed unmeetable by construction).
3. **Forced-context:** none.
4. **Homophone-cycling:** N/A.
- **Era caveat (honest):** the WO-10 leg (5 «ce qui X ce que», all
  verb-filled) is v8-dependent — clean pool yields n=1 (filler «arriva»).
  The «ce qui par ce que»=0 double-zero DOES reproduce in the clean pool.
  Standing LEAD keeps; no promotion case can be made without v8.

### ISLET 6 — 66 word-class → CLASS-RULE (recommend keep CONFIRMED)
- 19/19 windows fit noun/infinitive/nous-vous-class frames: «pour 66» ×7
  (pre=00 @189/@246/@254/@715/@1109/@1494/@1533), 66-84 ×2 («[66] en [V]»
  @153/@1150), 00-predecessor dominance (7/19) fits content-word.
- Zero subject-pronoun-forcing windows; era «pour»+subject-pronouns ≈0
  (il/on/ils/je/tu all 0–2) vs «pour nous/vous» attested.
- 0/19 inside confirmed words. Not a polyvalence islet — class constraint,
  keep as is. Specific value stays NULL (honest).

### ISLET 7 — 89 noun-class → CLASS-RULE (recommend keep CONFIRMED)
- 14/14 re-derived: 77-89 ×2 («le [89]» @640/@871), 29-89 ×5, 89-48 ×3
  («[89] ne» @640/@871/@986), 24-89 ×3 («en [89]» @222/@986/@1498),
  52-89 ×2 (fenced tension, non-kill-grade), 29-89-84 ×2 (@275/@1377).
- **Compositional check:** 29-89's 5-mers never complete «premier»
  (e.g. @275: 11-06-67-33-29; @781: 33-73-37-08-29) — no stem+ending
  fusion; 0/14 inside confirmed words.
- 52-89 ×2 stays fenced (bare «pas»+noun restricted, not kill-grade).

### ISLET 8 — 64-77-84-59 ×2 → WORD-RULE (recommend re-bank)
- Both frames re-verified @1445 (37-64-77-84-59-36-67) and @1801
  (87-64-77-84-59-35-94).
- **Battery 1:** 84-59 is stem+syllable of ONE -este verb — the "conditioning
  predecessor" 84 is the other half of the word. Dissolves into ISLET 10's
  W-este arm.
- **Banked falsifier (unfired):** «qui le X est» = 2 in the clean pool, but
  BOTH are rescued/broken — «qui le concernent est effrayé de» (clause
  boundary before «est») and «qui le pain est une chose» («le»=article, not
  pronoun). The falsifier does NOT fire.
- **Era inventory:** manifeste 130, atteste 35, proteste 19, conteste 19,
  déteste 15 (reste 1212 excluded — intransitive).
- Re-banked form: FRAME F-qui-le (64-77=«qui le»; depends 64=«qui» prov,
  77=«le» lead) + WORD W-este1 (84-59=«[X]este» verb). ISLET 8's
  "UNBANKED — needs 59 polyvalence" dependency is now BANKED-AS-WORD.

### ISLET 9 — 86 identity → KILLED stands (confirmed, not re-litigated)
- Kill legs re-derived on repaired stream: 00→86 ×12 (n00=55) = 0.2182 vs
  era P(que|pour)=0.0180 / P(qu|pour)=0.0132 — **12–16× over**; elision
  kills on 7 windows (86→70 ×1 «qu'pre» impossible; 86→52 ×2; 86→56 ×4);
  77-86 ×5 with era «le que»=5/74377, «le qu»=2/74377 (≈0).
- 86→29 ×4 («[86]er» infinitive — stem+completion, supports F40's
  verb-stem-class working hypothesis; 86 is a word-PART, not polyvalent).
- **Part 4:** {33,86} predecessor χ²=6.562 (dof=3, p=0.0872), successor
  χ²=6.104 (dof=5, p=0.2962) — uniform, homophone proposal SURVIVES this
  test (not proven). {66,86}: predecessor Jaccard=0.087 — divergence;
  demote stands.

### ISLET 10 — 59 «est» / «-este» → WORD-RULE (recommend dissolve)
1. **Lexical-bigram:** 93-59 = «l'est» and 94-59 = «n'est» are single
   orthographic words (proclitic fusion) — the "conditioning predecessor"
   is the other half of the word. 84-59 (and fenced 06/61/44/86-59) are
   stem+syllable of one verb. 64-59 = «qui est» is frame (two words).
   → the islet's "conditions" are word-membership, not cell properties.
2. **Residual:** word-«est» fails outside {64,94,93} (the 8 settled
   adverses — not re-litigated); verb-syllable fails outside stem contexts
   (@1496 «[15-59=reste]» is fenced-ambiguous, the only extension
   candidate; @1511 pre=61 leftover shows the tier doesn't over-generate).
3. **Forced-context:** F1 unfired — no window forces word-«est» outside S.
4. **Homophone-cycling:** {52,59} pre χ²=10.2 (dof=11, p=0.5125), suc
   χ²=16.4 (dof=11, p=0.1269) — uniform; the homophone proposal survives
   (value-sharing untested here).
- **Era legs:** «qui est»=1033, «l'est»=203, «n'est»=3688 (clean pool).
- **Census check:** 27/27 positions re-derived. Arm partition verified with
  registry fences: est=6 (@103/@316/@559/@763/@1210/@1777) + @1796 S5-fenced;
  este=4 (@1190/@1448/@1804 firm, @1291 fenced); sub-tier=5
  (@216/@1186/@448/@1715/@554); leftovers=4 (@463/@834/@1511/@1833);
  S5-fenced=6; neutral/fenced=2 (@825/@1496). (A naive pre-only classifier
  over-counts est=7/subtier=7 — the fences are load-bearing.)
- **Re-banked form:** 59 = «est» MONOVALENT (syllable). WORD RULE W-est1:
  93-59=«l'est». WORD RULE W-est2: 94-59=«n'est». WORD RULE W-este2:
  [stem]-59 = -este verb (stems 84/06/61/44/86; fenced 15). FRAME F-qui-est:
  64-59=«qui est» (59 = standalone word). The conditioned-polyvalence
  entry DISSOLVES — there is no second reading, only word-boundary
  placement.
- **Caveat:** phonetic /ɛ/ (word «est») vs /ɛst/ (-este syllable) — the
  table may list two syllables; operationally the condition is
  word-membership either way.

## Sanity checks (three dissolved islets)
- **ISLET 3:** W06 06-positions [580,738,1184,1355] re-verified exactly;
  @1351: 77-78-94-82-06-52 = «le [78] ne ment pas» (52=«pas»-STRONG) —
  dissolution holds in context. 06 residual = verb-stem-class (F21).
- **ISLET 2:** 96-00 @48/@466/@961 re-verified («par le» ×3). 00 residual =
  «pour» (52/55).
- **ISLET 1:** arms re-verified @167 (82-84 «m'en»), @154/@1151 (66-84),
  @276/@1378 (89-84, with 29-89-84 ×2 recurrence). Full 84 accounting:
  25 = 5 arms + 9 leftovers + 8 rescoped + 2 formula (46-84-24 ×2 @310/@473)
  + 1 fenced-adverse (@1665). Dissolution holds: 82-arm → WORD (82-84=
  «m'en»); 66/89-arms → FRAME («[noun] en [V]» pronoun frames, depend on
  ISLETS 6/7).

## What the compositional tier means for the registry

Of 10 islets: **5 dissolve into word/frame rules** (1, 2, 3, 8, 10), **1 is
true polyvalence** (4: the 67 fork — the only cell that genuinely carries
two readings under frame conditioning), **2 are class rules, never
polyvalence** (6, 7), **1 is an underpowered singleton** (5), **1 is a
confirmed kill** (9). The "conditioned polyvalence" tier shrinks to one
entry plus ISLET 1's 66/89 frame arms. The compositional thesis is confirmed
as the dominant pattern: the "conditioning predecessor" is, in the
dissolved cases, the other half of a multi-cell word — misattributed to the
cell because the lane scores groups instead of segmenting words first.

Recommended registry edits (for adjudicator ruling):
1. ISLET 10 → retire; re-bank as W-est1/W-est2/W-este2/F-qui-est + 59
   monovalent «est».
2. ISLET 8 → re-bank as F-qui-le + W-este1; close the "UNBANKED 59"
   dependency (now banked-as-word).
3. ISLET 1 → re-bank 82-arm as WORD (82-84=«m'en»); keep 66/89 arms as
   FRAME (depend on 6/7).
4. ISLETS 2, 3 → re-bank as WORD rules (96-00, 82-06); record residuals
   (00=«pour», 06=verb-stem-class).
5. ISLETS 6, 7 → move to a class-constraint tier (out of polyvalence).
6. ISLET 4 → keep as the sole TRUE-POLYVALENCE entry (SUPPORTED).
7. ISLET 5 → keep LEAD, flag era leg as v8-dependent.

## Caveats
- Era pool here (N=3,867,332, v8-free) differs from the lane's earlier
  v8/Tocqueville pools — ratios reproduce, absolutes don't transfer.
- ISLET 5's 5-frame era leg cannot be re-verified without v8 (clean n=1).
- 06 FIRE-OUT hunting belongs to the 06-falsifier-watch (not duplicated).
- S5-fenced ×6 (@528/@624/@912/@1178/@1443/@1796) not re-litigated.
- All verdicts are recommendations; no registry edits made.
