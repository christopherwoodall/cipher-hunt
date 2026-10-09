# Battery verdict: nir-value-60-68

Worker: e6c7627f-cb75-48cd-a6f6-8ddfeefe82ac. Date: 2026-10-09.
Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json +
data/upstream-ct_R5005.txt), parsed per code/side-keyhunt/repair_parse.py;
1,847 pairs / 96 types verified in-session. canonical.py never used.
R5005, sealed gates, red-team adjudication queue untouched.
@-offsets are 1-based (lane convention). The bar's "@114/@504" and the
finder's "@227/@1783" are 0-based; mapped to 1-based below (@115/@505,
third cells @233/@1789).
Lock: locks/nir-value-60-68.lock created on start (agent id + UTC timestamp),
no prior lock (fresh or stale).

No red-team verdict on 60 or 68 exists — no contradiction, no overwrite.
Standing verdicts honored: noun-60 (kill), adj-60 (kill, single-value claim),
verb-60 (null), poly-60-redteam (queued pri-1 red-team docket — coordinated,
not preempted), frame-vient-parvenir (kill of the 3-cell set), frame-qui-47
(kill of 76/68 verb-hood). No polyvalence declared (§7 intact: 67 et/veut
remains the sole declared polyvalence).

## Bar (verbatim, pre-registered before testing)

"(a) every free 60 window (x17) and 68 window (x7) parsed with the cell as
'nir' under standing values with zero hard contradictions; (b) kill iff any
window forces non-'nir' or a cleaner rival value is demonstrated on the same
frames; (c) the formula slots @227/@1783 cited, not re-proved."

Numbered clauses (fixed before data examination):

1. (C1) Each of the 17 free 60-windows and 7 free 68-windows parses with the
   cell as 'nir' (the "par-ve-nir" syllable) under standing values, with
   zero hard contradictions. A "hard contradiction" = every word-boundary
   assignment either violates a standing value or requires inventing a
   value for an open cell; fenced-but-conditional parses (open neighbor
   must supply the stem) are not hard contradictions but are recorded.
2. (C2) KILL iff any window forces non-'nir' (no boundary assignment works
   under standing values) OR a cleaner rival value is demonstrated on the
   same frames.
3. (C3) The formula slots (98-83-82-96-21-[60/62/68] x3, third cells at
   1-based @233/@1066/@1789) are cited from battery-frame-vient-parvenir.md
   (kill, 2026-10-09) and next-token-findings-parvenir-thirds.md — not
   re-proved, not re-litigated.

Standing values used (marking: banked pencil; granted/promoted; ? provisional;
* battery-promoted pending ratification; ~ lead/rival; open otherwise):
11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que; 87=ce, 64=qui, 96=par,
17=fois, 79=tout, 00=pour, 84=on, 47=ce (A4); 59=est?, 77=le?; 94=ne*,
12=n*, 48=e*, 30=pas*, 39=a/a*, 06=ent*; 67=et/veut (sole polyvalence,
positional rule); 03=verb-stem class*, 65=noun-class*, 93=verb-class*,
76=noun masc.*; 21='suite'~ (lead); 62='il'~ (demonstrated rival, unpromoted).

'nir' is not a French word; as a value it can only be a word-final (or
word-internal) syllable, i.e. every window needs a stem to its left (or a
continuation to its right) forming a French word under standing values.

## Window-level evidence — 60 (17 free; formula cell @233 excluded)

HARD = hard contradiction (forces non-'nir'). FENCE = conditional parse,
open neighbor must supply the stem (fenced with cause, not ignored).

- @120 "67 14 | 21 60 | 90 19": FENCE. "[21]nir" conditional on 21's open
  value (21='suite' is a lead, not a grant). 'nir' standalone broken.
- @173 "84 53 12 48 | 21 60 | 09 87": FENCE. Same 21-60 shape; "ne [21]nir"
  conditional on 21.
- @198 "47 01 | 21 60 | 08 67": FENCE. Same; 01/08 open.
- @323 "06 11 92 | 60 | 15 63": FENCE. "[92]nir" conditional on 92 (open;
  09~92 hold, value open). 'nir' standalone after "la [92]" broken.
- @455 "17 79(tout) 17(fois) 77(le?) | 60 | 65(N*) 13": **HARD.**
  "fois le [60] [65-noun]" NP frame (noun-60/adj-60 anchor). "le nir"
  ungrammatical; "lenir" not French; "nir[65]" impossible (65 is a whole
  noun word). Forces non-'nir' (conditional on provisional 77='le').
- @638 "74 46(que) | 60 | 67(et/veut) 77": **HARD.** "que nir" ungrammatical
  (46='que' banked pencil); "quenir" not French; "nir[67]" impossible
  (67 is a word). Forces non-'nir'.
- @691 "94(ne*) 29(er) | 60 | 03(Vstem*) 39": **HARD.** "er nir [03]":
  "ernir[03]" not French; 'nir' standalone between "er" and a verb stem
  broken; "nir[03]" would need inventing 03's open value. Forces non-'nir'.
- @701 "45 28 94(ne*) | 60 | 12(n*) 98": **HARD.** "ne [60]": 94='ne'*
  takes a finite verb; 'nir' is not a word and cannot be a finite verb;
  "nirn" not French. Forces non-'nir' (battery-grade).
- @996 "30(pas*) 03(Vstem*) | 60 | 67 11": PARSES (conditional).
  "[03]nir" = "[stem]nir" ("souvenir"-shaped) conditional on 03's open
  value; "…[03]nir, et…" locally grammatical. The one 'nir'-compatible
  window; 03's value open, so support is conditional, not proof.
- @1339 "86 71 64(qui) | 60 | 08 65": **HARD (kill-grade).** "qui [60]":
  64='qui' GRANTED (relative pronoun) requires a finite verb; 'nir' is not
  a French word; "nir[08]" with 08's open candidates {ne,se,on,
  spelling-letter} (stem-08 queued) yields no French word. Forces
  non-'nir'. Single-handedly decides C2.
- @1367 "79(tout) 14 | 60 | 03(Vstem*) 30": FENCE. "[14]nir [03]"
  conditional on 14 (open). (One of the 60->03 x4 adverse windows.)
- @1475 "41 53 | 60 | 06(ent*) 67": FENCE. "[53]nir" conditional on 53
  (open; prof-53 null). "nirent" is not a French word, so 06 cannot rescue.
- @1564 "30(pas*) 06(ent*) | 60 | 71 50": **HARD.** "ent nir": 06 attaches
  left ("pasent" no) or stands word-initial ("entnir" no per
  wordbound-30-06-importent bimodality); 'nir' standalone broken;
  "nir[71]" requires inventing 71's open value. Forces non-'nir'
  (battery-grade).
- @1645 "33 98(V*) | 60 | 03(Vstem*) 64": **HARD.** Finite verb 98* +
  "nir" broken; 98 is a whole word, cannot merge; "nir[03]" invents 03.
  Forces non-'nir' (battery-grade).
- @1675 "81 92 | 60 | 03(Vstem*) 39": FENCE. "[92]nir [03]" conditional on
  92 (open). (One of the 60->03 x4 adverse windows.)
- @1691 "79(tout) 14 | 60 | 27 46": FENCE. "[14]nir" conditional on 14
  (open); 27 open.
- @1736 "30(pas*) 06(ent*) | 60 | 12(n*) 48": **HARD.** "ent nir n":
  no boundary assignment works ("entnir"/"nirn" not French; 'nir'
  standalone broken). Forces non-'nir' (battery-grade).

60 tally: 8 HARD (@455, @638, @691, @701, @1339, @1564, @1645, @1736),
1 conditional parse (@996), 8 FENCE (all conditional on open neighbors
21/92/14/53).

## Window-level evidence — 68 (7 free; formula cell @1789 excluded)

- @115 "93(V*) 29(er) 89 | 68 | 21(suite~) 67 14": FENCE (adverse window;
  bar's "@114"). "[89]nir" conditional on 89 (open; 80/89 verb-frames
  granted, value open). "…[89-stem]nir, suite[21], et/veut[67]…" is the
  parse shape; 21='suite' is a lead and 89/14 are open — fenced with cause,
  not a clean parse.
- @505 "40(e) 56 39(a/a*) | 68 | 21(suite~) 67 77": FENCE (adverse window;
  bar's "@504"). "a/à nir" broken as words, BUT 39 has a fenced
  word-internal /a/ face (a-39 battery @607 precedent: "pre-a-la"-shaped),
  so "[56]anir" is structurally allowed — conditional on 56 (open).
  Fenced with cause; not a hard contradiction.
- @885 "31 79(tout) | 68 | 37 03(Vstem*)": **HARD.** "tout [68] [37]":
  79='tout' GRANTED (A5). "tout nir" ungrammatical (tout+adverb/adjective/
  noun frames only); "toutnir" not French; "nir[37]" requires inventing
  37's open value ("nirvana" is the only French "nir…"-word). The qui-47
  kill battery independently reads this as "tout [68-adj/noun]". Forces
  non-'nir'.
- @1287 "98 55 | 68 | 00(pour) 11": FENCE. "[55]nir pour…" conditional on
  55 (open).
- @1385 "13 24 65(N*) | 68 | 52 82(m)": **HARD.** "[65-noun] [68] [52]":
  65 is a whole noun word (65 full-profile battery-promote); noun + "nir"
  broken; "nir[52]" invents 52. Forces non-'nir' (battery-grade).
- @1443 "52 | 68 | 59(est?) 37": FENCE. "[52]nir est…" conditional on 52
  (open). (qui-47's "[68] est" subject+copula read would need 68 nominal —
  'nir' cannot supply it; the parse survives only via 52.)
- @1720 "64(qui) 47(ce) | 68 | 06(ent*) 11": **HARD.** "ce [68] ent":
  47='ce' GRANTED (A4). "ce nir" ungrammatical; "cenir" not French;
  "nir"+"ent"="nirent" not a French word (no -nirent conjugation);
  clause-boundary "…ce. Nir…" invents a proper name. Forces non-'nir'.

68 tally: 3 HARD (@885, @1385, @1720), 4 FENCE (@115, @505, @1287, @1443 —
all conditional on open neighbors 89/56/55/52).

## Adverses (pre-registered) — answered

1. "68's '68-21-67' x2 (@114/@504) must parse under 'nir' or be fenced
   with cause": @115 fenced — "[89]nir" conditional on 89's open value;
   21='suite' is a lead, 89/14 open. @505 fenced — "a/à nir" broken as
   words, but 39's word-internal /a/ face (a-39 @607 precedent) allows
   "[56]anir", conditional on 56 (open). Neither parses cleanly; both
   fenced with stated cause, not ignored.
2. "60->03 x4 (03 verb-stem, queued stem-03) constrains 60's right edge":
   tested — the constraint is real and it kills the claim where the left
   neighbor is a standing word: @691 ("er[29-banked] nir [03]") HARD,
   @1645 ("[98-V*] nir [03]") HARD; @1367/@1675 FENCE (14/92 open).
   Note: stem-03 has since been PROMOTED (class-level, 2026-10-09); the
   adverse's "queued" gloss is stale but the constraint tested is the same.

## Per-clause results

- **C1: FAIL.** 8 of 17 free 60-windows and 3 of 7 free 68-windows are hard
  contradictions under standing values. The "zero hard contradictions"
  standard is not met. Only @996 offers even a conditional 'nir'-shaped
  parse ("[03-stem]nir", 03's value open).
- **C2: KILL (both triggers).** (i) Windows force non-'nir': @1339
  ("qui[64-granted] [60]") alone is kill-grade — 'nir' is not a French
  word and cannot fill the finite-verb slot; @701, @638, @691, @1645,
  @1736, @1564, @455 (60) and @885, @1385, @1720 (68) independently
  force the same. (ii) Cleaner rival demonstrated on the same frames:
  the adj-60 battery demonstrated 60=masculine-adjective (+ 03=
  masculine-noun) parsing the @455/@691/@1645/@1675 frames with zero
  unattested assumptions, vs 'nir' which parses none of them.
- **C3: SATISFIED (citation).** Formula slots cited from
  battery-frame-vient-parvenir.md (kill, 2026-10-09): 98-83-82-96-21
  formula-bound x3, thirds 60/62/68, 96-21 nowhere else globally;
  conditioned 83='de' in the "vient de" environment stands. Not
  re-proved, not re-litigated. This kill names no third-cell value and
  leaves the formula's French to its owners.

## Verdict: KILL

The value claim "60 and 68 both parse as 'nir' in their free windows" is
dead at kill grade. 'nir' is not a French word, so the claim requires
every window to supply a stem (or continuation) forming a French
"…nir" word under standing values — eleven windows cannot, including
@1339 on the granted 64='qui' and @885/@1720 on the granted 79='tout'
and 47='ce'. The kill is consistent with every standing verdict:
noun-60 kill, adj-60 kill (single-value), verb-60 null, poly-60-redteam
(queued — untouched, still the red team's docket), frame-vient-parvenir
kill, frame-qui-47 kill (68 verb-hood dead, adjective/nominal lean —
this kill does not name 68's value). No red-team verdict contradicted;
nothing overwritten; §7 intact (no polyvalence declared).

No follow-ups are required for a kill verdict. Notes for the supervisor
(not queued targets): 68's value remains open (qui-47 left it
adjective/nominal-leaning, unnamed); 60's adjective-vs-verb question
remains with queued poly-60-redteam; the "parvenir" formula's third-cell
values stay open per the vient-parvenir kill.

## Bookkeeping

- Report: code/crowd17/report_inbox/battery-nir-value-60-68.md
- battery-queue.json: `nir-value-60-68` -> status `verdict`, result `kill`,
  date 2026-10-09 (temp-file + rename in the same directory; pre-write
  assert confirmed queued/verdictless; JSON re-validated post-write)
- Lock created on start with agent id + UTC timestamp; deleted on completion.
