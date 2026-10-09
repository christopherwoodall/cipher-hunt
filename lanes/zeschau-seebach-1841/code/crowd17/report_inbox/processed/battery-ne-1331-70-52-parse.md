# Battery verdict: ne-1331-70-52-parse

Worker: session f748ede8-fcf5-4a52-a653-52f2f9a6eb14. Date: 2026-10-09.
Target: `ne-1331-70-52-parse` (P3). Lock created 2026-10-09T14:15:46Z, deleted on completion.
Stream: repaired 1,847-pair / 96-type parse (`code/side-keyhunt/repaired_offsets.json` +
`data/upstream-ct_R5005.txt`, parsed per `repair_parse.py`). `canonical.py` never touched.
R5005, sealed gates, red-team adjudication queue untouched.

## Bar (verbatim, pre-registered)

"resolve iff @1331 parses under one arm with stated values; else fence with stated cause"

Numbered clauses (stated BEFORE testing, unchanged after data):

1. Arm A (clausal 'ne'): 94 is the negation particle before a "pre"+52
   prendre-family verb head, with a word boundary between 62 and 94 —
   all roles carried by stated standing values.
2. Arm B (word-internal '[62]ne'): 62+94 is one French word ending in "ne",
   stated under a named word.
3. Resolve iff exactly one arm survives with stated values; else fence
   with stated cause.

Indexing note: the target's `@1331` is the **1-based** index of the 94
cell (the ne-94-non12-prefamily parent's convention). 0-based:
62=@1329, 94=@1330, 70=@1331, 52=@1332. The `62 94 70 52` 4-gram is
unique stream-wide, so the locus is unambiguous under either convention.

## Method

Fresh re-parse of the repaired stream (1,847 pairs / 96 types verified);
window re-derived byte-exact below. Standing values used — pencil:
11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que; granted/promoted:
87=ce, 64=qui, 96=par, 17=fois, 79=tout, 00=pour, 84=on, 47=ce,
48='e', 12='n'; provisional: 59=est, 77=le; leads: 94='ne' (R17-001
STRONG LEAD; R19-167 closed the 94 split — single 'ne'),
39='a/à', 83='de' (11-window scope, R19), 78='ver'.
Honored kills: 62='il' (R19 kill grade), 62='on' (collision-62-84),
sel-62-48-94 KILL (no 62 value makes 62-48 and 62-94 one morpheme).
§7 sole-polyvalence (67) honored: no second polyvalence declared.

## Window-level evidence (0-based @, repaired stream)

Bytes @1324–1340, rows a7_04/a7_05 (row join between @1331 and @1332):

```
1324 62 a7_04
1325 98 a7_04
1326 56 a7_04
1327 30 a7_04
1328 06 a7_04
1329 62 a7_04
1330 94 a7_04
1331 70 a7_04
1332 52 a7_05
1333 39 a7_05
1334 83 a7_05
1335 86 a7_05
1336 71 a7_05
1337 64 a7_05
1338 60 a7_05
1339 08 a7_05
1340 65 a7_05
```

Right side: 39='a/à' lead, 83='de' lead, 86 INF-class. This is exactly
the "ne … [86-INF]" shape that battery `ne-attachable-paradigm`
(PROMOTE, 2026-10-09) verified as a CLEAN particle-'ne' positive control
at this same 94 cell, with the intervener chain fully stated:
70='pre' (pencil ground truth, syllable tier), 52 (prendre-family stem),
39/83 preposition-class leads.

## Arm-by-arm test

### Arm A — clausal 'ne': PASSES

- 94='ne' particle at this cell is established at battery grade by
  `ne-attachable-paradigm` (PROMOTE): "ne … [86-INF]" clean control.
- 70='pre' is pencil ground truth; 52 is the lexicon-verified
  prendre-family stem (prescrira/préserva/prévoira tie unbroken by
  `lex-52-deinf-register` NULL, but the family — and its de+INF
  government — is lexicon-verified and stands). So "ne pre[52]" is the
  prendre-family verb head governed by clausal 'ne'.
- The word boundary between 62 and 94 is established by the particle
  frame itself; no value for 62 is required to decide 94's role.

### Arm B — word-internal '[62]ne': FAILS

- `sel-62-48-94` (KILL, closed per this target's adverse) demonstrated
  the impossibility: no 62 value makes 62-48 and 62-94 one morpheme —
  the candidate space (don/donn, men, son/bon/ton, vien, tien, person)
  is exhausted and every candidate dies on spelling (62-06
  discriminator) or grammar (@1772).
- The cipher's own doubled-n convention kills the residual hope of a
  bare "donne"-style reading: "prenne" is spelled 70+12+94 ("pre"+"n"+
  "ne") — doubled n needs the explicit 12('n'); a bare 62+94 = "Xne"
  has no orthographic precedent in the cipher (sel-62-48-94 analysis,
  adopted).
- The only standing word-internal-'ne' precedent is the 12-94 "prenne"
  family (compositional doubled-n: 12+94; 12+06 and 30+06 stay single).
  Here pre-94 is 62, not 12 — no compositional 'ne' is licensed.
- R19-167 closed the 94 split: 94 is single 'ne'; word-internal 'ne'
  is a segmentation distinction, and no such segmentation is statable
  here (§3 bars inventing a word for the open-valued 62).

## Per-clause pass/fail

1. Arm A parses with stated values — **PASS** (94='ne' particle via
   ne-attachable-paradigm PROMOTE; 70='pre' GT; 52 prendre-family,
   lexicon-verified; 39/83/86 stated).
2. Arm B statable — **FAIL** (sel-62-48-94 KILL impossibility proof;
   no orthographic precedent for bare 62+94; no compositional license
   with pre-94=62).
3. Resolve — **FIRES**: exactly one arm survives. @1331 (1-based; the
   94 cell) is clausal 'ne' before the "pre"+52 prendre-family verb.

## Adverses

- "62's value open" — **ANSWERED, not ignored**: the decision does not
  require 62's value. 94's particle role is established independently
  by the standing battery PROMOTE; the 62–94 word boundary follows.
  (62's full census heads to the queued `redteam-62-split` package;
  nothing here prejudges it.)
- "sel-62-48-94 KILL closed the word-internal selector claim for 62-94"
  — **ADOPTED as premise**: it is the positive ground on which arm B
  dies. This target's parent `ne-94-non12-prefamily` (NULL, fence
  executed) had already classed @1331's 62-94 as clausal on that
  ground; this battery re-verified it byte-exact and records the
  resolution.

## Verdict

**PROMOTE** (resolution recorded at battery grade). The bar's resolve
arm passes: @1331 (1-based; 94 cell, 0-based @1330) is **clausal 'ne'
before the "pre"+52 prendre-family verb**. The word-internal '[62]ne'
arm is fenced with stated cause (sel-62-48-94 impossibility proof +
no orthographic precedent for bare 62+94 + no compositional license
with pre-94=62).

Scope: segmentation-level only. No registry change; 62's value stays
open (heads to redteam-62-split); 52's value stays in the
prescrira/préserva/prévoira tie. No standing/red-team verdict
contradicted or downgraded (R19-167, R19-192, A8, the 12-94
compositional finding, ne-attachable-paradigm PROMOTE all adopted as
premises); §7 intact; no polyvalence declared. Canonical-stream
caveat stands (rows a7_04/a7_05 unvalidated).

Per §4 (promote), no follow-ups required.
