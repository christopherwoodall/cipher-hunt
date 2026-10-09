# Battery report: sel-62-48-94

Worker: 0152c1fc-fcee-4bd6-bcdf-2083ab153944. Date: 2026-10-09.
Target: `sel-62-48-94`. Priority 3.
Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json +
data/upstream-ct_R5005.txt, parsed per code/side-keyhunt/repair_parse.py).
canonical.py never used. R5005 never touched. All counts re-derived below;
no prior counts trusted.

## Bar (verbatim, pre-registered)

"produce the value and parse three 62-48 windows (@360, @1349, @1569) plus
three 62-94 windows (@100, @1329, @1772) under it; kill-grade if the
12-94='prenne' word-internal use (@348) forces 94 syllabic and breaks the
particle-only selector."

Numbered clauses:

1. Produce a 62 value under which 62-48 and 62-94 are one morpheme with
   spelling variants (48='e' vs 94='ne').
2. The three 62-48 windows (@360, @1349, @1569) parse under that value as
   the morpheme.
3. The three 62-94 windows (@100, @1329, @1772) parse under that value as
   the SAME morpheme (spelling variant).
4. Kill-grade check: the 12-94='prenne' use at @348 forces 94 syllabic AND
   breaks the particle-only selector.

## Method

Fresh parse of the repaired stream (1,847 pairs / 96 types verified).
Re-derived: 62-48 x6 (@360, @425, @1315, @1349, @1464, @1569), 62-94 x9
(@100, @508, @761, @840, @1329, @1362, @1686, @1704, @1772), 12-94 x3
(@64, @348, @1548), 62-06 x2 (@665, @1536). Standing values used —
banked: 11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que; granted: 87=ce,
64=qui, 96=par, 17=fois, 79=tout, 00=pour, 84=on, 47=ce; promoted:
48='e' (letter), 12='n' (letter); provisional: 59=est, 77=le; leads:
94='ne', 78='ver'. Standing kills honored: 62='il' kill-grade dead
(class-62-25, 2026-10-09; @1482 "vient 62 que" defeats every
independent-word class), 62='on' killed (collision-62-84). §7
sole-polyvalence (67) honored: no second polyvalence declared.

## Window-level evidence (@-offsets, repaired stream)

### The six bar windows (wide context)

- @360 a2_06 (62-48): "…92 47 11 21 | 62 48 | 76 47 78 48…"
  = "…[92] ce[47] la[11] [21] [62-48] [76] ce[47] [78] e[48]…"
  21 = noun-class ('suite' lead), 76 = masculine noun (promoted).
- @1349 a7_05 (62-48): "…66 73 34 | 62 48 | 77 78 94 82 06…"
  = "…[66] [73] i[34] [62-48] le[77] [78] ne[94] m[82] ent[06]…"
- @1569 a8_01 (62-48): "…50 29 24 74 | 62 48 | 56 32 28 52…"
  = "…[50] er[29] [24] [74] [62-48] [56] [32]…"
- @100 a1_02 (62-94): "…29 85 08 21 | 62 94 | 93 59 45 28…"
  = "…er[29] [85] [08] [21] [62-94] [93] est[59] [45]…"
- @1329 a7_04 (62-94): "…62 98 56 30 06 | 62 94 | 70 52 39 83…"
  = "…[62] vient[98] [56] pas[30] ent[06] [62-94] pre[70] [52]…"
- @1772 a8_09 (62-94): "…64 26 37 78 | 62 94 | 24 87 64 59…"
  = "…qui[64] [26] [37] [78] [62-94] [24] ce[87] qui[64] est[59]…"
  24 = verb-class, 87='ce' granted, 59='est' provisional.

### The @348 kill-grade window

- @348 a2_05 (12-94): "…87 01 06 70 | 12 94 | 74 67 78 40…"
  = "…ce[87] [01] ent[06] pre[70] n[12] ne[94] [74]…"
  70='pre' is ground truth, 12='n' is promoted (letter tier).
  "70-12-94" admits exactly one French reading: "pre"+"n"+"ne" =
  "prenne". The alternatives are impossible: "pren"+"ne"(particle)
  fails because "pren" is not a French word; "pre"+"n"(word-final)
  fails for the same reason. **94 is forced word-internal/syllabic
  at @348.**
- @1548 a8_00 (12-94): "…43 00 46 70 | 12 94 | 92 45…"
  = "…[43] pour[00] que[46] pre[70] n[12] ne[94] [92]…"
  = "…pour que prenne [92]…" — "pour que" + subjunctive "prenne", a
  perfect French frame. Confirms 94 syllabic in "prenne" independently.
- @64 a1_01 (12-94): "…08 34 29 40 | 12 94 | 92…"
  = "…[08] i[34] er[29] e[40] n[12] ne[94]…" = "…ierenne" —
  12-94 = "nne" word-internal. Third syllabic demonstration.

### The 62-06 discriminator (@665, @1536)

- @665: "50 80 03 | 62 06 | 00 20" ; @1536: "66 73 41 | 62 06 | 21 62".
  06='ent' promoted. 62-06 = "[stem]62-ent" (3pl verb ending).

## Analysis

### Clause 1+2+3: no value exists — demonstrated impossibility

For 62-48 (X+"e") and 62-94 (X+"ne") to be ONE morpheme, X must end in
'n' (else "Xe"="Xne" is impossible), and the pair must be a doubled-n
word with spelling variance ("done"~"donne", "mene"~"mene", …).
Exhausting the plausible n-final X against all six windows plus 62-06:

| X | 62-48 (X+"e") | 62-94 (X+"ne") | 62-06 (X+"ent") | Verdict |
|---|---|---|---|---|
| don | "done" (variant of "donne") | "donne" ✓ | "donent" ✗ (not French) | dies at 62-06 |
| donn | "donne" ✓ | "donne" ✗ (triple n) | "donnent" ✓ | dies at 62-94 |
| men | "mene"="mène" ✓ | "mene" ✗ (nn never correct) | "menent"="mènent" ✓ | dies at 62-94 |
| son/bon/ton | same pattern as don/donn | — | — | dies at 62-48 or 62-94 |
| vien | "viene" ✗ | "vienne" (subj., needs "que") | "viennent" ✓ | dies at 62-48, @360/@100 |
| tien | "tiene" ✗ | "tienne" (needs "que"/"la") | — | dies at 62-48 |
| person | "persone" (variant) | "personne" ✓ | — | dies as verb at @360/@100 |

Every candidate fails at least one leg: **no X yields correct French
across 62-48, 62-94, and 62-06 simultaneously.** The cipher's own
convention aggravates this: "prenne" is spelled 70+12+94 ("pre"+"n"+
"ne"), i.e. doubled-n is written with an explicit 12('n') before
94('ne'). A 62-94="donne" spelling (bare 94 after n-final 62, no 12)
contradicts that convention — the "spelling variant" has no precedent
in the cipher's orthography.

Grammatical overconstraint (independent of spelling): @360 and @100
require the morpheme to be a finite transitive verb ("la suite donne
[76]", "[21] donne [93]"), while @1772 ("…[78] [62-94] [24-verb] ce qui
est…", 24 verb-class) admits NO verb parse for 62-94 — imperative +
bare infinitive is ungrammatical, 3sg lacks a subject — and forces a
subject noun/pronoun, a role no doubled-n word fills while also serving
as the verb elsewhere (segmentation alternatives at @1772 —
"[78-62]"+"ne"(particle), "[62]"+"ne [24]", "[78-62-94]" one word — all
make 62-94 non-morphemic, directly contradicting the claim). **Clauses
1–3 FAIL: the existential claim is false.**

### Clause 4: kill-grade FIRES

@348 forces 94 syllabic (shown above: "prenne" is the only French
reading; "pren" is not a word; 12='n' promoted). @1548 ("pour que
prenne") and @64 ("…nne") confirm. A group demonstrated word-internal
cannot be particle-only: the particle-only selector (94='ne' negation
particle in every 62-94 window, cf. il-62 Group A) is broken. Per §7,
making 94 both particle and syllable would be a second polyvalence —
a red-team act, not available at battery level — so the particle-only
reading stands broken. **Clause 4 FIRES at kill grade.**

## Per-clause pass/fail

1. Produce the value — **FAIL** (no value satisfies all legs;
   demonstrated impossibility, see table).
2. Parse @360/@1349/@1569 as the morpheme — **FAIL** (no value to
   parse under; best candidates die at 62-06 or @1772).
3. Parse @100/@1329/@1772 as the same morpheme — **FAIL** (@1772
   admits no morphemic verb parse under any segmentation).
4. @348 kill-grade — **FIRES** (94 forced syllabic; particle-only
   selector broken).

## Adverses

- "94's syllabic use ('prenne' @348, @1548) tensions a particle-only
  selector" — **ANSWERED at kill grade**: the syllabic use is forced
  (not merely possible), and it kills the particle-only selector. The
  tension is resolved by eliminating the particle-only model.
- "94='ne' is promotion-track not granted" — **HONORED**: nothing here
  grants 94='ne' as particle. The analysis uses 94='ne' only as a
  word-internal syllable (demonstrated at @348/@1548/@64), a separate
  question from the particle promotion-track.
- "section 7 sole-polyvalence" — **HONORED**: no second polyvalence
  declared. The 94 particle-vs-syllable tension is flagged for the red
  team (see below), not decided here.

## Verdict

**KILL.** The selector claim is false on two independent grounds:
(1) no 62 value makes 62-48 and 62-94 one morpheme — the candidate
space is exhausted and every candidate dies on spelling (62-06
discriminator; "prenne"=70+12+94 convention) or grammar (@1772);
(2) the bar's explicit kill-grade fires — @348 forces 94 syllabic,
breaking the particle-only selector. No standing verdict is
contradicted or downgraded (62='il' kill-grade dead already standing;
il-62's battery promote not re-litigated beyond the honored kill).

## Red-team notes / surviving leads (not queued targets)

- 94's syllabic demonstrations (@348/@1548/@64: "prenne", "…nne")
  coexist with its 9/37 particle-'ne' legs (frame-20-62-94 census).
  Under §7 this is a second-polyvalence question; red-team authority
  required to resolve.
- 62-06 x2 (@665 "…[03] donnent pour [20]", @1536 "…[41] donnent
  [21]…") strongly favors an nn-final stem value for 62 ('donn'-type),
  consistent with class-62-25's "verb-stem-final" behavior split. This
  is a value lead for 62, not a claim about 48/94.
- The "62-48 as adjective/noun" behavior (class-62-25) is untouched by
  this kill, which targets only the one-morpheme-with-variants claim.
