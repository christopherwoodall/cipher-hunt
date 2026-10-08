# Battery A14 — "par le [X]" discriminator (X ∈ {92, 33, 86})

Date: 2026-10-07. Runner: battery-runner (resumed, round 15).
Stream: repaired 1,847-pair parse recomputed in-session
(`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`,
per `code/side-keyhunt/repair_parse.py`).

Source: finder §4 (next-token-findings-parle-and-rest.md).
Standing: 96="par" promoted; 00="le" ONLY as pre=96 islet (F54) — so
96-00-X = "par le [X]" with the islet intact; 00="pour" elsewhere (A9).
33=INF class; 86=INF class (A9, by 33-parallel); 92's INF-signal open.
Windows: @47 `96-00-92-79-37`, @465 `96-00-33-79-80`, @960 `96-00-86-56-41`.

## Pre-registered bar (written BEFORE touching data)

Two readings: (a) **substantivized infinitives** — "par le pouvoir/devoir/
vouloir" (grammatical, diplomatic); (b) **monosyllabic nouns** (roi/fait/chef).
- **Discriminator:** for each X, INF-signal = (→29 "er" count) + ("pour"-valency
  = pre=00 count) + nominal-frame count (determiner/adjective slots).
- **PROMOTE (a)** iff ≥2 of the three X show net INF-signal AND all three
  "par le [X]" windows parse under (a) with no contradiction.
- **PROMOTE (b)** iff ≥2 show net nominal signal instead.
- **SPLIT** the X-set iff they discriminate differently (e.g. 33/86 → (a),
  92 → (b)) — the set need not move together.
- Note the shared 79="tout" (A5) in @47/@465: "par le [X], tout [Y]" —
  Y=37 (@47, A1-adjective) / Y=80 (@465, A8-verb). The Y-slot must parse
  under the winning reading; if it contradicts, HOLD.

## Data

### Discriminator table

| X | n | pour-valency (pre=00) | →29 ("er") | pre-det {11,77} | net signal |
|---|---|---|---|---|---|
| 92 | 22 | **6** | 1 | 3 ("la"×3) | INF-leaning (wrinkle noted) |
| 33 | 25 | **8** | **5** | 0 | INF (class-confirmed) |
| 86 | 32 | **12** | **4** | 6 ("le"×5) | INF (class-confirmed) |

- 86's pre-det ×5 ("le [86]") is itself substantivized-infinitive-shaped
  ("le pouvoir") — supports (a), not (b).
- 92's pre-det ×3 ("la [92]"): ambiguous — article+noun (b) vs object
  pronoun+verb ("la [92-verb]", verb-compatible). Wrinkle, not a kill.

### Window parses under (a) "par le [inf]"

- @47: `96-00-92-79-37` = "par le [92] tout [37-adj]" ✓ ("by the [X],
  all [is 37]…")
- @465: `96-00-33-79-80` = "par le [33] tout [80-verb]" ✓ ("by the
  [saying], everything [80]s" — uses A8's "tout [80]" verb re-read)
- @960: `96-00-86-56-41` = "par le [86] [56] [41]" ✓
All three parse; Y-slots (79="tout"+37 / 79+80) consistent under (a).
Under (b), the windows also parse at surface level — the INF-signals
are the discriminator, and they point one way.

## Verdict: PROMOTE (a)

**"par le [X]" = "par le"+substantivized infinitive for X∈{92,33,86}.**
33 and 86 strongly (class-confirmed INF); 92 by pour-valency (6×) with
the "la [92]"×3 wrinkle named. No split — all three lean the same way.
Values NOT named ("pouvoir/devoir/vouloir" stay candidates).
**Weakest leg (red team):** 92's INF-signal is pour-valency only (→29
×1/22 is thin); 92 rides on the set, not on its own legs.
