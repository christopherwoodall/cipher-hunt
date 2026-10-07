# PERIOD DRAG T1–T8 — report (crowd6, 2026-10-07)

## Context
Dragged the 117 red-team-adjudicated period crib cards (work order
`code/crossfleet/memo2-period-corpus.md`) against the canonical 1,847-pair
repaired stream at the 8 concrete targets. Instrument: the crib-learned F44
24-unit by-ear alphabet (inventorist tiler top-8 UNION manual fused/split
variants) — no standard-French syllabification. Anchor-preserving controls
(N34): every null counts lexicon fitters (11,870 words) at the SAME window
with the SAME anchor set; anchors never shuffled. Anti-collision honored:
"premier"/"première" never dragged. ≥2 independent checks per claim.
Code: `code/crowd6/period_drag/` (common.py, drag_t1_t8.py, t7_anchored.py);
numbers: `code/crowd6/period_drag/results.json` (+ t7_anchored.json).

## Frame verification (before citing positions)
All memo positions re-verified against the repaired parse; two memo claims VOID:
- "la première" @754/@1034 repaired = memo raw 766/1054. VERIFIED.
- R1 `77 78 94 82 06` @**1180**/@**1351** repaired (= memo raw 884/1204).
  **The memo's "R1a followed by 77=le (sentence break)" is a RAW-FRAME ARTIFACT**:
  raw@884's 9-mer (`...06 77 44 91 67`) is absent from every canonical parse
  (old 1,846 and repaired 1,847). No R1 window is followed by 77 in any parse.
- **Memo R2 `06 77 78 18 71 10 01` @raw1429: 0× in the repaired stream**
  (0× in the old parse too, per the crowd round). Raw-only artifact straddling
  dropped digits — the "06|77|78 = ent le gou" cross-check cannot be run. VOID.
- 94-82-06 trigram ×3 @578/@1182/@1353 repaired; @1182/@1353 sit INSIDE the T4
  windows (@1180/@1351 +2) — the T4 windows ARE two of the three
  "restricted-ent PLAUSIBLE" trigrams.
- 96=par ×21 repaired @47/131/150/224/230/342/465/602/847/914/927/947/952/960/
  998/1026/1063/1196/1213/1526/1786.

## Decision — one line per target
- **T1 (opening @0, `09 00 97 51 47 41`): NULL.** Neither "Monsieur le Baron"
  nor "Mon cher Baron" fits under standing anchors (47={ce} islet blocks
  cell4); releasing the islet makes the fit vacuous. Honest null.
- **T2 ("Votre dépêche du" / "J'ai reçu votre dépêche du", 0–150): NULL.**
  25/7 windows fit but ALL are anchor-free (nulls 0.68/0.32); zero
  anchor-bearing placements. Unconstraining fits, not evidence.
- **T3 (noun after "la première" @754/@1034): NULL.** The memo's shared
  é-initial-noun theory does not survive: entrevue 0 fits (killed @759 by
  94="ne" prov-strong, killed @1039 by 77=le; survives IFF 94≠ne — override of
  prov-strong); expédition 0 fits (same two kills); épreuve fits @759 ONLY
  ([e,pre,uve]/[e,preu,ve], 244/11,870 nulls — unconstraining), killed @1039 by
  77=le. @1039 admits only [e,?,le] words (13 fitters: elle/égale/école…),
  none a memo candidate. Alignment-B inversions: @760 n_fit=4
  (défense/dépense/dépensé/offensé, 94='en' islet — no discrimination);
  @1040 n_fit=7 (élément/parlement/nullement… — no grammatical noun phrase).
- **T4 ("le gouverment" @1180/@1351): HIT on the SHAPE, both windows;
  94-reading REFERRED to red team.** Three live tilings:
  (a) le|gou|ver|m|ent (memo: 77=le,78=gou,**94=ver**,82=m,06=ent);
  (b) le|gouv|er|m|ent (94=er, collides with GT 29=er);
  (c) gouv|er|ne|m|ent = "gouvernement" proper (77=gouv,78=er,**94=ne**,82=m,06=ent —
  keeps 94="ne" prov-strong + 06=ent restricted + 82=m GT; 77 free per F37 fence).
  Checks: C1 exact by-ear fits at BOTH windows (82=m GT-anchored); C2 shape
  rarity — [le,?,?,m,ent] family 1/11,870 ("légalement"), general null
  289/11,870=2.43%/window; C3 94-reading among lexicon fitters: @T4 ne×10 /
  ver×0 / er×3, independent @578 trigram ne×3 / ver×0 / er×17; C4 memo-context
  corrections above. **(a) vs (c) is exactly: keep 77=le + break 94=ne, or keep
  94=ne + break 77=le (fenced).** 94="ne" NOT adopted/demoted here — red team
  to adjudicate against the F33 islets.
- **T5 ("par le dernier courrier" @21 96-windows): NULL (phrase);
  LEAD: 00="le" ×2.** The full phrase fits @465/@914/@960 but the placements
  imply MUTUALLY INCONSISTENT assignments (le→00 vs 09; der→33 vs 02) — no
  joint phrase. Structural kill: **96→77 is 0/21** — the memo's 96|77|…
  shape never occurs. LEAD: 96-00 "par le" ×3 (@47/@465/@960) consistent on
  00="le" (null 64/11,870=0.5% @465) — needs its own battery; TENSIONS F40
  00="pour" ("pour que" 00→46 ×4). Flagged, not resolved.
- **T6 (tail closings, 1800–1846): NULL.** All candidates fit only at
  anchor-free windows (nulls 0.32–0.68). Tail inversions: nothing closing-shaped
  ("considération/distinguée/Adieu/Tout à vous/haute considération" all vacuous).
- **T7 (names): NULL per name; one LEAD.** Anchor-bearing recount (tilings
  engaging the anchor cell only): Metternich 18 windows (null 1.7%),
  Nesselrode 13–15 (null 0.8–1.2%), Ibrahim 4–5 (null 0.6–1.3%), Saxe 8
  (null 4.2%) — no discrimination, honest nulls. Ibrahim+"pacha" follow-up
  VACUOUS (2-cell words fit any 2 unanchored groups). l'Empereur/Guizot/Damas:
  vacuous by method (no anchors). **LEAD: "Mehemet-Ali" @8** [78,18,93,62,98]
  = me|he|met|a|li — anchor-bearing on the 78={me,ver} islet, null 33/11,870
  = 0.28%, despatch-opening position; but 10 bearing windows and LEAD-grade
  islet — needs its own battery, not a hit.
- **T8 (treaty double-surface): NULL.** 77-engaged recount: "le traité de
  Londres" 8 windows (207/453/677/798/870/968/1133/1216, null 30/11,870=0.25%),
  "le traité du 15 juillet" 6 windows (null 21/11,870=0.18%); the two surfaces
  share 6 windows — not discriminated; no second anchor in any phrase window.
  Candidate set recorded, no promotion.

## Why (methodology notes)
- F44 by-ear tiler + manual fused/split variants per candidate (e.g. T4
  [le,gou,ver,m,ent] is manual — the tiler over-splits to 7–8 cells and never
  emits it; the memo's cut model requires hand variants).
- 77=le enforced everywhere EXCEPT the T4 windows (F37 fenced exception);
  94=ne enforced everywhere EXCEPT T4 (test variable) and noted conditionals;
  06 never hard (verb-stem-class, no string); islets enforced as reading sets.
- Provisional anchors propagate their status: every T4/T5/T7-LEAD claim is
  marked provisional-dependent. Nothing promoted — all HITs/LEADs await
  red-team ruling.
- Nulls are anchor-preserving by construction (N34): same window, same anchor
  set, lexicon background. Vacuous fits (high null, zero engaged anchors) are
  reported as honest nulls, not hits.

## Enlightenment
- The memo's raw-frame T4 context (R1a+"sentence break", R2 cross-check) does
  not survive the canonical parse — both were raw artifacts. The T4 windows
  themselves are real (×2, both parses) and ARE two of the three 94-82-06
  trigrams, which sharpens the 94-reading question rather than dissolving it.
- T4's three tilings reduce the 94="ne" tension to a clean either/or:
  (a) le|gou|ver|m|ent keeps 77=le, breaks 94=ne; (c) gouv|er|ne|m|ent keeps
  94=ne, breaks 77=le at exactly the F37-fenced windows. The lexicon background
  favors 'ne' (10 vs 0 among fitters) but cannot judge the by-ear misspelling
  "gouverment", which is outside the lexicon by construction.
- T5's structural datum (96→77 = 0/21) kills the memo's expected shape
  outright; the surviving 00="le" ×3 sub-pattern is the sharp end for a
  follow-up battery, with the F40 "pour" tension pre-flagged.

## For red team
Adjudicate: (1) T4 94-reading (a) 94=ver vs (c) 94=ne — the either/or above,
against the F33 islets; (2) T5 00="le" LEAD vs F40 00="pour"; (3) T7
Mehemet-Ali @8 LEAD (78='me'-islet dependency); (4) the T3 kill ledger
(entrevue/expédition conditional on 94=ne; épreuve/époque unconstraining).
Confirm the two frame corrections (R1a-follow-77 artifact, R2 void).
