# Battery `disloc-demonstrative-inversion-prose` — verdict: NULL

## Bar (verbatim)
">=1 genuine inversion in prose re-opens arm (a) via the inverted order; confirmed zero fences it in prose too"

## Bar restated as numbered clauses
- (C1) ≥1 genuine "[bare inf] !, cela/ceci/ça" postposed-demonstrative + bare exclamatory infinitive in prose → re-opens arm (a) of ce87-1028-role via the inverted order.
- (C2) Confirmed zero → fence the inverted order at the prose level.

## Method
Read BATTERY-PROTOCOL.md first; created/deleted `locks/disloc-demonstrative-inversion-prose.lock`.
Ran `code/crowd17/next-token/disloc_demonstrative_inversion_prose_census.py`
(SAME inversion census as `disloc_demonstrative_inversion_fullcorpus_census.py`
verbatim: same INF suffix pattern, same DEM_POST tonic set, same candidate
rule — DEM match starts after the infinitive inside INF..INF+100, and "!"
occurs between INF start and 20 chars past the DEM match end) over the
21-file prose corpus (18 French 1841-register prose files + 3 wider 19th-c
prose files — the same set as the prose clause-initial census):
guizot-memoires t1/t2/t3/t5-t6, nesselrode v7/v8/v9/v10, revue-deux-mondes
1841 q1–q4, metternich-papiere v4/v6, talleyrand-memoires v1,
pozzo-di-borgo-correspondance v1, levant-correspondence-1841-p3,
gutenberg-17489-miserables1, gutenberg-30513/30514-tocqueville t1/t2.
Total 27,656,185 chars. Raw results in
`code/crowd17/next-token/disloc-demonstrative-inversion-prose_census.json`.
Corpus census per target charter; the 1,847-pair repaired parse is not
applicable here. `canonical.py` never used. R5005, sealed gates, red-team
queue untouched.

## Findings
- **146 unique candidates** from the loose candidate rule (the INF suffix
  pattern catches nouns/adjectives/finite verbs ending -er/-ir/-re/-oir —
  suffix noise, as in the sibling batteries).
- **0 genuine.** All 146 hand-classified with cause:

| confound class | n | example |
|---|---|---|
| demonstrative subject/object of a finite clause | ~85 | guizot-t3 @169049 "Non, Messieurs, cela n'est pas possible!"; metternich-v6 @873320 "Tout cela se reglera sans doute"; miserables @512345 "cela m'a soulagé de prendre une résolution!" |
| demonstrative as object of infinitive/gerund in a finite matrix | ~25 | rdm-q1 @1446015 "j'ai donc pu faire cela !"; rdm-q2 @901694 "Il mit l'épée au vent en disant cela"; nesselrode-v9 @207811 "Que dire après cela!"; miserables @499754 "Il fallait faire cela!" |
| "Ah ça!" interjection | 6 | rdm-q2 @1446218, @2790701; rdm-q4 @921920; miserables @494918 |
| "comme ça/cela" adverbial | 6 | miserables @300971 "des choses comme ça"; rdm-q2 @1537960 "comme cela soupire la douleur" |
| "Viens ça" imperative | 2 | rdm-q4 @1095036/1095051 |
| absolute "cela dit / cela fait" | 3 | rdm-q2 @2381800 "Cela dit"; talleyrand-v1 @319769 "Cela fait" |
| exclamatory NP ("Ruses que tout cela!") | 3 | rdm-q4 @836471; miserables @565170 "mystère que tout cela!" |
| OCR garbage / truncated fragments | 6 | guizot-t5-t6 @76108; rdm-q1 @103539–103584 (garbled index page); rdm-q1 @2560691; rdm-q4 @69300 "celle du détestable ca-" |
| finite-interrogative confounds | ~8 | rdm-q1 @30461 "quel augure de voyage est ceci?"; talleyrand-v1 @868526 "nous parlerons de cela une autre fois" |

- **Nearest near-miss** (nesselrode-v9 @246111): "d'accomplir une si belle
  œuvre ! Dans les temps où nous vivons, cela frise le miracle."
  Excluded: "cela" is the subject of a NEW finite sentence ("cela frise"),
  not postposed to the infinitive — no dislocation, no comma, a full
  sentence intervenes.
- **Strict-pattern check:** regex for "[inf-suffix] ! , cela/ceci/ça"
  (exclamation mark immediately followed by comma-demonstrative) run over
  all 21 files → **0 hits**. The loose-rule zero is not a recall artifact.
- Corpus note: pozzo-di-borgo-correspondance, levant-correspondence-1841-p3,
  guizot-t1, tocqueville t1/t2 contributed 0 candidates; the RDM 1841
  quarter files and Les Misérables dominate the candidate count, which is
  why a register-wide loose sweep was needed.

## Per-clause result
- (C1) FAIL — confirmed zero genuine inversions in 27.66M chars of prose.
- (C2) EXECUTED — the inverted order "[inf] !, cela/ceci/ça" is fenced at
  the prose level. Arm (a) of ce87-1028-role stays fenced in both word
  orders across all three registers (drama, RDM/dialogue, prose).
- Per §4 this is a **null** (zero is an absence), not a kill.

No standing or red-team verdict contradicted; §7 intact. Adverses: none
listed on the target.

## Follow-ups proposed (all verified absent from battery-queue.json)
1. `disloc-demonstrative-inversion-prose-1800-1820` (P4) — pre-1841 literary
   prose census; tests whether the fence is a period effect rather than a
   register effect.
2. `inversion-prose-window-widen` (P4) — 200-char DEM window + dash/ellipsis
   pause variants; recall-gap closure for the loose rule.
3. `arm-a-inversion-fence-ratify` — escalate the now-three-register
   inverted-order fence to the red team for ratification.

## Bookkeeping
- Report: `code/crowd17/report_inbox/battery-disloc-demonstrative-inversion-prose.md`
- Census script: `code/crowd17/next-token/disloc_demonstrative_inversion_prose_census.py`; raw results: `code/crowd17/next-token/disloc-demonstrative-inversion-prose_census.json`
- Queue: `disloc-demonstrative-inversion-prose` → `verdict`/`null`, 2026-10-09 (temp-file + rename)
- Lock created on start, deleted on completion. `canonical.py` never used;
  R5005, sealed gates, red-team queue untouched.
