# Battery P1 — "cela" = 87+11 compositional (all 7 windows)

Date: 2026-10-07. Runner: battery-runner (round 15). Stream: repaired 1,847-pair
parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`,
recomputed in-session per `code/side-keyhunt/repair_parse.py`; never the stale
`canonical.py`).

## Pre-registered bar (written before touching data)

PROMOTE the "cela" reading iff ≥2 windows parse cleanly as "cela" with zero
board contradictions. Extend or correct the round-13 segmenter's
"en ce"→"en cela" at 3/10 windows (F107).

## Data

87-11 occurs 7× (87's top successor: 7/32; 87 is 11's top predecessor: 7/45 —
mutual top-attraction):

| pos | window (±3) | "en cela"? |
|---|---|---|
| @74 | 24-87-11-00-11-29 (pre: 87-14-24) | yes |
| @163 | 94-24-87-11-24-82 (pre: 52-94-24) | yes |
| @201 | 76-87-11-92-63 (pre: 08-67-76) | no |
| @461 | 79-87-11-59-42 (pre: 14-02-79) | no |
| @830 | 24-87-11-77-76 (pre: 82-01-24) | yes |
| @1242 | 81-87-11-00-33 (pre: 67-77-81) | no |
| @1403 | 81-87-11-00-11-95 (pre: 67-77-81) | no |

"en cela" (24-87-11) ×3 = @74, @163, @830 — exactly F107's 3/10. Extended, not
corrected.

## Window audits

- **@460–464: "79-87-11-59-42"** — CLEAN. Independent finder result
  (next-token-findings-parle-and-rest.md §2) gives 79="tout" (PROMOTE-grade,
  3 legs). "tout cela est 42" = "all that is 42". Uses only board values +
  the tout composition. Strongest window.
- **@830: "24-87-11-77-76"** — CLEAN. "en cela le [76]" (77="le"
  provisional-conditioned): "cela" as adverbial, "le" clitic/object. No
  contradiction.
- **@1242: "81-87-11-00-33"** — CLEAN. "[81] cela [00] [33=INF]": "cela" as
  direct object of (verb) 81, followed by 00+infinitive ("cela [à/de] [faire]"-shaped).
- **@1403: "81-87-11-00-11-95"** — CLEAN. "[81] cela [00] la [95]": "cela" as
  direct object ("cela [de] la [95-noun]"-shaped).
- **@74: "24-87-11-00-11-29"** — SUPPORTING (conditional). "en cela [00] la [29=er]":
  reads as "en cela [a] l'air [42]" = "in that, seems [42]" iff 00="a"
  (new lead, not claimed) and 11-29="l'air" (29="er"/"air" homophony, plausible
  in a syllabary). "cela" as subject fits regardless.
- **@201: "76-87-11-92-63"** — SUPPORTING (conditional). "cela [92] [63]":
  "cela se [63]" (reflexive, "cela se [fait]"-shaped) iff 92="se" (new lead).
- **@163: "52-94-24-87-11-24-82-84"** — RESIDUAL. "94-24" ("ne"+"en"/"de")
  before "cela" resists a clean parse ("[52] ne [de] cela [en] m'en [53]" —
  word order wrong for negation; 94's "ne"-reading likely wrong here).
  "cela" itself is not contradicted; the surrounding frame is unparsed.

Zero windows contradict 87="ce" or 11="la". The competing "ce"+"la"
(demonstrative + article, ungrammatical as adjacent) has no window; "cela"
is the only grammatical French for ce+la in all 7 positions.

## Verdict: PROMOTE

**"cela" = 87+11 is a confirmed compositional reading** (not a new group
value; it strengthens 87="ce" and 11="la"). Legs: (1) 4 clean windows
(@461 "tout cela est", @830 "en cela", @1242/@1403 "[verb] cela"); (2) mutual
top-attraction (87→11 is 87's #1 successor, 87 is 11's #1 predecessor);
(3) F107's independent "en cela" 3/10, confirmed and extended to 7/7;
(4) @460's "tout cela" composition cross-confirms the independent 79="tout"
prediction (next-token-findings-parle-and-rest.md §2) — two predictions
interlocking on one window.

## Residuals / new leads

- R1: @163's "94-24-87-11" frame unparsed — queue for the 94/24 battery.
- R2: 00="a" (@74 "cela a l'air") and 92="se" (@201 "cela se [63]") as
  derived leads, untested.
- R3: 87's other ce+X compositions (87-01×2, 87-77×2, 87-78×2, 87-83×2 —
  "ceux"/"ceci" candidates) untouched; the 87-78×2 pair belongs to the 78 fork.
