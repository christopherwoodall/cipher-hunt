# Battery verdict: val-42-det-gap — determiner-adjacency census across 42's 20 windows

Date: 2026-10-09. Worker: 56301a75-4450-4129-95c9-a9d8ccc495f7.

Parent: `noun-42-value` (verdict null, 2026-10-09), follow-up #1. The parent
fenced the value-naming route (best candidate 'erreur' 1/20; "er"+C
inventory exhausted; syllable-vs-word joint unsatisfiability) and left
42's value open under R19-055 (42=["noun","cls"]).

## Bar (verbatim from battery-queue.json)

"if 42 is systematically determiner-less in argument positions, restrict
the value inventory to bare-capable nouns (proper nouns, pronoun-class
"rien"-family — the latter contradicts R19-055, so report as
contradiction-headline null per §5 if it fires); else fence the
restriction."

Numbered clauses (fixed BEFORE the census, not modified after):

- **C1:** 42 is systematically determiner-less in argument positions —
  no determiner cell ("le/la/ce/un") heads 42 in any window where 42
  occupies a subject/object argument slot, after excluding
  position-artifact windows (the listed adverse).
- **C2 (then-arm):** Restrict 42's value inventory to bare-capable nouns:
  proper nouns, pronoun-class "rien"-family.
- **C3 (contradiction check):** If the evidence forces the pronoun-class
  leg specifically, report as contradiction-headline null per §5 (it
  contradicts R19-055's noun-class grant); do not adopt it.
- **C4 (else-arm):** If C1 fails, fence the restriction with stated cause.

## Method

- Re-derived the full 1,847-pair / 96-type stream from
  `data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`
  (parse per `code/side-keyhunt/repair_parse.py`; asserts held: 1,847
  pairs, 96 types). `canonical.py` never touched.
- Full 20-window census of 42 re-derived (0-based @79/@205/@219/@266/
  @282/@428/@464/@488/@493/@543/@784/@1072/@1144/@1187/@1410/@1503/
  @1617/@1794/@1814/@1838 — byte-identical to the parent's list).
- Determiner-value cells per the standing registry
  (`code/table-grid/table-registry.json`): 11="la" (gt), 47="ce"
  (prom), 77="le" (prov), 79="tout" (prom), 87="ce" (prom). No
  "un"/"une" cell exists in the registry. 45="ce/dict" is lead-grade
  (A11 hold), not a standing determiner.
- Adopted (never re-litigated): 42=["noun","cls"] (R19-055); A1
  predicative frame; T3 "29→42" composition fence (val-42-nominal);
  pencil 11=la, 29=er, 46=que, 70=pre, 82=m, 34=i, 40=e; granted 87=ce,
  96=par, 00=pour (A9), 79=tout, 84=on, 47=ce (A4); provisional 59=est,
  77=le; 76 masculine-noun class (R19); R24 (24 finite/modal iff follower
  != 85); 94="ne" single value (R19); no pro-drop in 1841 French.
- R5005, sealed gates, red-team adjudication queue untouched.

## Window-level evidence (0-based @-offsets, ±4 context)

Determiner scan: immediate-left determiner count = **0/20** (byte-exact).
Left-context determiner cells within −4..−1 and their constituent:

| @ | ±4 context | det cells in −4..−1 | 42's position | 42's determiner? |
|---|-----------|---------------------|---------------|------------------|
| 79 | 11 00 11 29 [42] 98 51 62 | 11(−4), 11(−2) | T3 "29 42" composition ("er"+42 syllable) — not a word slot | "la"(−2) heads the "er[42]" word ("l'erreur" frame), not a standalone 42 — excluded |
| 205 | 87 11 92 63 [42] 06 77 44 | 87(−4), 11(−3) | post-verbal ("63 [42]", 63 finite-shaped) — object or object-predicative | "ce la" belong to pre-verbal material (separated by 92 + verb) — none |
| 219 | 06 59 46 29 [42] 16 24 89 | none | T3 "29 42" composition ("est que er[42]") — excluded | n/a |
| 266 | 45 93 52 33 [42] 06 73 47 | none (45="ce/dict" lead at −4, not a standing determiner) | "33 [42]", 33 open — undetermined | undetermined |
| 282 | 37 61 20 61 [42] 48 52 89 | none | A1-frame window, 42's role frame-internal — undetermined | undetermined |
| 428 | 14 62 48 76 [42] 63 77 86 | none | "76 [42]" attributive to promoted noun — adjective/apposition slot, no determiner expected — excluded (artifact) | n/a |
| 464 | 79 87 11 59 [42] 96 00 33 | 79(−4), 87(−3), 11(−2) | "59 [42]" = est-predicative (A1); "87 11" = "cela" ("tout cela est [42]") — predicative, no determiner expected — excluded (artifact) | n/a |
| 488 | 01 19 64 76 [42] 41 20 67 | none | "qui [76-noun] [42]" — attributive — excluded (artifact) | n/a |
| 493 | 41 20 67 78 [42] 94 02 79 | none | "[78] [42] ne [02]": 42 = subject of "ne [02]" (if 02 finite) OR object of 78 — determiner-less under BOTH parses | none (robust) |
| 543 | 12 44 29 48 [42] 06 00 46 | none | "48 [42]", 48 open — undetermined | undetermined |
| 784 | 29 89 11 24 [42] 94 74 65 | 11(−2) | "[24-fin] [42]" (R24: follower 42≠85 → finite). "11 24" = object-pronoun "la" + finite verb → 42 = predicative complement of the object ("la V [42]"-shaped); determiner-less under all parses but likely predicative — noted as probable artifact | "la"(−2) is the verb's object pronoun, cannot head 42 (R24 bars 24 nominal) |
| 1072 | 39 11 44 74 [42] 98 98 12 | 11(−3) | "74 [42]", 74 open — undetermined ("la" at −3 separated by 44+74, no NP license) | undetermined |
| 1144 | 78 62 16 29 [42] 98 98 86 | none | T3 "29 42" composition — excluded | n/a |
| 1187 | 82 06 06 59 [42] 06 84 59 | none | "59 [42]" = est-predicative (A1) — excluded (artifact) | n/a |
| 1410 | 11 95 46 52 [42] 16 97 69 | 11(−4) | "[52] [42]" — object of 52 prendre-family stem (conditional on 52 verb class); "la" at −4 separated by "que"+52 — cannot head 42 | none |
| 1503 | 41 74 84 33 [42] 33 00 86 | none | "on [33] [42]" (84=on promoted subject) — object of 33-stem (conditional on 33 verb class) | none |
| 1617 | 71 48 31 76 [42] 44 11 84 | none | "76 [42]" attributive — excluded (artifact) | n/a |
| 1794 | 03 00 86 56 [42] 94 59 37 | none | "[42] ne est [37]": 94="ne" promoted, 59=est provisional. The "ne est [37]" clause needs a subject (no pro-drop in 1841 French); 42 is the only candidate → 42 = SUBJECT of "n'est [37]". The "[56] [42]"-as-phrase rival strands the ne-clause subjectless → rejected | none — STRONGEST leg: determiner-less subject |
| 1814 | 61 15 93 50 [42] 06 29 37 | none | "50 [42]", 50 open — undetermined | undetermined |
| 1838 | 36 69 64 22 [42] 44 83 21 | none | "qui [22] [42]", 22 open — undetermined | undetermined |

Position buckets (adverse answered):

- **Artifact exclusions (8):** @79/@219/@1144 (T3 syllabic composition),
  @428/@488/@1617 ("76 [42]" attributive), @464/@1187 ("59 [42]"
  predicative). Determiners are not expected in these slots; their
  bareness is positional, not lexical. @784 is probably predicative
  (object-predicative under the forced "la"=object-pronoun parse) and is
  noted as likely artifact too.
- **Argument positions, all determiner-less (5):** @1794 (subject —
  strongest), @205 (post-verbal), @1410 (object of 52-stem),
  @1503 (object of 33-stem), @493 (subject-or-object, robust under both
  parses). Three are conditional on open neighbor classes (52, 33, 63);
  all five are determiner-less under every standing-compatible parse.
- **Undetermined (5):** @266/@543/@1072/@1814/@1838 (open neighbors);
  @282 (A1 frame-internal). None shows a determiner; none can currently
  supply one.

## Per-clause results

- **C1: PASS.** 42 is systematically determiner-less in argument
  positions at battery grade: 0/20 immediate-left determiners
  (byte-exact); every determiner cell in the left context belongs to
  another constituent (composition frame @79, pre-verbal material
  @205/@464, the verb's object pronoun @784); and after excluding the
  eight position-artifact windows, the five classifiable argument
  windows (@1794 subject, @205/@1410/@1503/@493 object-or-subject) are
  uniformly determiner-less under all standing-compatible parses. The
  adverse is answered: the bareness survives argument-position
  classification and is not a window-position artifact.
- **C2: FIRES — value inventory restricted.** 42's value inventory is
  restricted to bare-capable nouns: **proper nouns** (R19-055-compatible:
  proper nouns are nouns; "X n'est [37]", "V [proper]" all grammatical
  at the argument windows) and **pronoun-class "rien"-family** (fits the
  argument windows: "rien n'est [37]", "V rien" — see C3).
- **C3: pronoun-class leg NOT adopted — escalated per §5, headline
  below.** The evidence does not force pronoun-class (proper nouns fit
  every argument window), so no forced contradiction fires. But the
  pronoun-class disjunct is live on the argument windows and would
  contradict R19-055's noun-class grant per the bar author's judgment —
  it is FLAGGED for the red team, not adopted by this battery.
- **C4: does not fire** (C1 passed).

**§5 CONTRADICTION HEADLINE (escalation, not adoption):** the live
pronoun-class "rien"-family leg of the C2 restriction contradicts
R19-055 (42=["noun","cls"]) on the bar author's reading. This battery
adopts only the proper-noun leg; the pronoun-class leg is escalated to
the red-team docket (R20 42 venue) for adjudication. No standing verdict
is contradicted or downgraded by the adopted finding; §7 intact.

**Caveat (not verdict-changing):** the parent's spot-check found @464
("tout cela est [42]") semantically rejects proper nouns. @464 is a
predicative artifact window outside this target's determiner test, and
the objection was a battery spot-check, not a ruling — recorded here so
the red team sees both legs' problems: proper nouns strained at @464,
pronoun-class barred by R19-055.

## Verdict: PROMOTE (C2 restriction banks at battery grade)

Scope: narrows 42's value inventory to bare-capable nouns (proper-noun
leg adopted; pronoun-class leg escalated). Names no value; changes no
registry entry; contradicts no standing or red-team verdict; §7 intact.
Canonical-stream caveat stands (68 of 70 upstream row offsets
unvalidated). Per §4 (promote), no follow-ups required.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-val-42-det-gap.md` (this file).
- battery-queue.json: `val-42-det-gap` queued → verdict/promote via
  temp-file + rename (own entry only; pre-write assert confirmed
  queued/verdictless; JSON re-validated post-write; no downgrade).
- Lock `code/crowd17/next-token/locks/val-42-det-gap.lock`: created on
  start, deleted on completion.
- R5005, sealed gates, red-team adjudication queue untouched.
