# "LA PREMIÈRE" FOLLOWER BATTERIES — fois-battery (2026-10-07)

**Feeds round 15** (round 14's docket is with the red team; nothing here assumes round-14 rulings).
Lane: zeschau-seebach-1841. All numbers re-derived from the repaired 1,847-pair stream this session.

## Setup

- Pencil crib "la première" (11-70-82-34-29-40, all GT) occurs twice:
  - W1: crib@754, follower **20**@760: `40 | 20 62 94 59 39` = "première [20], on n'est…" (62="on" fenced STRONG, 94-59="n'est" ISLET 10)
  - W2: crib@1034, follower **17**@1040: `40 | 17 77 82 63 11` = "première [17], le m… la…" (77="le" provisional — the "le la" tension is noted, not resolved here)
- Corpus census (premiere-noun.md, ~3.1M words 1840–42 diplomatic French): "la première X" → fois 168, de 46, et 29, partie 25, occasion 22, est 16, moitié 14, nouvelle 11, année 11, place 10.
- Board: 17="fois"-WEAK, 20 unidentified. n17=15, n20=15.
- H-A stands (40=e is première's final mute-e); H-B is dead and is not re-litigated.

## Pre-registered bars

*Transparency note: window enumeration preceded bar documentation in wall-clock time (single session). The bars below are precedent-derived and reference no window-specific facts observed beforehand; they are the bars the lane's own standards ({33,86} split precedent, ≥2-leg promotion rule) dictate.*

**Battery 1 (17="fois" WEAK→promote):** PROMOTE iff (a) ≥2 independent "fois"-frame fits across distinct windows, (b) zero board contradictions in all 15 windows, (c) the @1040 flagship window parses cleanly in French. HOLD otherwise. KILL iff a window forces 17≠"fois".

**Battery 2a (20~17 homophony):** MERGE iff joint-frame sharing AND distributional indistinguishability (permutation test on successor/predecessor distributions, n.s.). SPLIT iff joint frames ~0 shared AND successor (or predecessor) distributions differ significantly (p<0.05), per the {33,86} precedent (split on 2/45 shared + Fisher p=0.0007). Uniformity (1690) is necessary but INSUFFICIENT per lane law.

**Battery 2b (20="fois"):** PROMOTE iff 2a MERGEs and 20's windows admit "fois" frames. KILL iff (conditional on Battery 1) any window becomes ungrammatical under 20="fois". Runner-ups (place, lettre — the only other monosyllabic census nouns) tested against 20's windows; polysyllabic followers (partie, occasion, moitié, nouvelle, année) are killed a priori on syllable count (1-group slot = monosyllabic, bounded by 62="on").

## Battery 1 — 17="fois": VERDICT **PROMOTE**

**Legs (4):**
1. **@1040 flagship:** "la première [17], le m… la…" — "la première fois, le…" parses cleanly; the crib's own follower slot. (Independent of census.)
2. **@1289:** `00 11 17 84 59` = "[00] la fois [84] est…" — the "la fois" frame is "fois"-diagnostic (cf. "à la fois", "la fois où"). No other candidate value explains "la [17]" as naturally.
3. **@308:** `88 20 17 46` = "[20] fois que…" — "fois que" with GT 46="que" is textbook French ("une/chaque fois que"). (Conditional on 20≠"fois"; see Battery 2.)
4. **Census dominance:** fois 168 = 3.7× the runner-up (de 46); next noun at 25. The collocation "la première fois" is the era's default.

**All 15 windows checked for board contradictions: zero.** 17's neighbors include GT/board cells (64="qui", 11="la", 46="que", 77="le", 40="e", 59="est") and none force 17≠"fois".

**Residuals (mild syntactic adverses, not contradictions — recorded for the red team):**
- @369: `61 70 17 06` = "…pre fois [06]…" — no clean French word ends in "pre" before "fois".
- @556: `59 34 17 86` = "…est i fois [86]…" — "i fois" awkward (34="i" role unclear here).
- @880: `86 78 17 08` = "…[78] fois [08]…" — determiner-less "fois" after the 78 ver/er fork.

**Plausible absolute-construction fits** ("une fois le/la…", temporal absolute): @238, @452, @1157, @1558. Neutral: @17, @837, @925, @1461, @1757.

**Verdict: PROMOTE 17="fois"** — 4 independent legs, zero contradictions. The 3 mild adverses are residuals, not refutations.

## Battery 2a — 20~17 homophony: VERDICT **SPLIT**

- **Uniformity:** n17=15, n20=15, χ²=0.0 — passes (necessary, insufficient).
- **Joint frames:** 0/30 shared (15 distinct frames each, all unique). Precedent {33,86} split on 2/45.
- **Successor distributions:** permutation test (20k reps), χ²-distance=52.0, **p=0.0148** — significant. The difference is structural: 20→62 ("on", fenced strong) ×4 vs 17→62 ×0; 17→77 ("le") ×3 vs 20→77 ×0. Segregated-by-successor, the anti-homophony pattern.
- **Predecessor distributions:** permutation p=0.2348 — n.s. (honesty note: not all tests discriminate).
- **Temporal interleaving:** 30 occurrences, 17 runs (expectation under random ≈16) — interleaved, not clumped. Consistent with homophony on this axis; does not rescue the successor split.

**Verdict: SPLIT — do NOT merge 17+20.** 17 and 20 are not free homophones. (Positional-allophone rescue: no clean positional story found — the segregation is by successor identity, not position.)

## Battery 2b — 20="fois": VERDICT **KILL** (conditional on Battery 1)

- **The @307 killer:** pairs `…88 20 17 46…` = "[20] fois que…" (17="fois" per Battery 1, 46="que" GT). Under 20="fois" this reads **"fois fois que"** — ungrammatical. Exactly one 17–20 adjacency exists in the stream, and it is fatal to the merge.
- Corpus check ("X fois que", ~3.36M tokens, 91 bigrams): predecessors are **exclusively determiners/adjectives** — les 22, première 19, chaque 15, une 9, dernière 4, plusieurs 3, la 2, deux 2, cette 2, … — zero nouns. So @307 independently demands 20 = determiner/adjective-like.
- **Runner-ups:** place ("la première place" ok-ish at W1) and lettre ("la première lettre" = first dispatch, plausible) both die at @307: "place fois que" / "lettre fois que" are ungrammatical, and the corpus admits no noun in that slot.
- **The 20 paradox (recorded for round 15):** W1 (@760) requires a feminine singular **noun** ("la première _, on n'est…"); @307 requires a **determiner/adjective** ("_ fois que…"). No monovalent monosyllabic cell satisfies both. 20 stays **UNIDENTIFIED**. Candidate resolutions for round 15: (i) re-examine W1 under the ellipsis hypothesis ("la première" nominalized, 20 = clause-initial); (ii) 20-polyvalence as last resort (strongly disfavored — the lane dissolved the polyvalence program, only 67's fork survives).

**Verdict: 20="fois" KILLED** (conditional on 17="fois" promoting; the 2a SPLIT stands independently of value). **20 = NULL**, paradox documented.

## Summary for the red team

| Battery | Verdict | Key numbers |
|---|---|---|
| 17="fois" | **PROMOTE** | 4 legs (@1040, @1289, @308, census 3.7×); 0 contradictions; 3 mild residuals |
| 17~20 homophony | **SPLIT** | 0/30 joint frames; successor perm p=0.0148; uniformity 15/15 (insufficient) |
| 20="fois" | **KILL** (cond.) | @307 "fois fois que"; corpus 91/91 det/adj before "fois que" |
| 20's value | **NULL** | W1↔@307 paradox recorded for round 15 |

## Methodology note

`40=e` H-A framing honored throughout; H-B not re-litigated. 77="le" untouched (provisional). No coordinator-applied bars — all verdicts above are recommendations for red-team adjudication. Nulls reported as nulls (20=NULL, 2b runner-ups dead).
