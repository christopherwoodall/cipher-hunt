# Battery A5 — 79 = "tout" (compositional interlock)

Date: 2026-10-07. Runner: battery-runner (resumed, round 15).
Stream: repaired 1,847-pair parse recomputed in-session
(`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`,
per `code/side-keyhunt/repair_parse.py`).

Source: finder §2 (next-token-findings-parle-and-rest.md).
Standing values used: 17="fois" (promoted), 87="ce" (promoted), 64="qui"
(promoted), 11="la" (GT), 87+11="cela" (P1 confirmed compositional).

## Pre-registered bar (written BEFORE touching data)

- **PROMOTE 79="tout"** iff ALL hold: (a) 79-17 ×2 (@451, @1460) parse as
  "toutefois" in clause-medial/adverbial position with no board
  contradiction (uses promoted 17); (b) 79-87-11 @460 parses as "tout cela"
  (uses P1's confirmed "cela" composition); (c) 79-87-64 @1799 parses as
  "tout ce qui" (uses promoted 87+64); (d) a full scan of 79's remaining
  windows shows ZERO hard contradictions with "tout" (boundary-artifact
  fencings allowed only with a stated cause, not as hand-waving).
- **HOLD** if (a)–(c) hold but ≥1 remaining window resists "tout" without a
  fenced cause.
- **KILL** if any compositional leg fails (e.g. 79-17 window contradicts
  "toutefois", or 17's promotion is undermined at those windows).
- **Open item carried:** 79-80 ×3 (@468, @1010, @1089) — the one "tout+X"
  bigram without a compositional reading. It is NOT a contradiction unless
  "tout 80" is ungrammatical; audit it as a lead, not a kill condition.
- Compositional-trap check: the three legs must be independent windows
  (non-overlapping) — verified from the stream, not assumed.

## Data

### The three compositional legs (re-derived; four windows, non-overlapping)

**(a) 79-17 = "toutefois" ×2:**
- @451: `32-48-79-17-77-60` = "[32] [48], toutefois [77=le]…" — clause-medial
  adverbial position ("however"), grammatical.
- @1460: `86-66-79-17-01-21` = "[66], toutefois [01]…" — clause-medial ✓.
- Phonological note (honest): "toutefois" needs the feminine "e" absorbed
  ("tout"+"fois" = "toutfois"). This matches the lane's documented clerk
  habits — mute-e elision, inconsistent cuts (R2), byear.py's mute-e rules
  ("dame"→"dam|e"). Not a kill; flagged for the red team as the softest
  phonological step in the battery.

**(b) 79-87-11 = "tout cela" @460:** `02-79-87-11-59-42` = "[02] **tout cela
est** [42]" — three-cell composition using P1's confirmed "cela". P1's
strongest window, extended.

**(c) 79-87-64 = "tout ce qui" @1799:** `91-79-87-64-77-84` = "[91] **tout ce
qui** le [84]" — uses promoted 87="ce", 64="qui". ✓

### Full 79 scan (n=18) — contradiction hunt

| pos | window | "tout" read |
|---|---|---|
| @50 | 00-92-79-37-11 | "[92] tout [37-adj] la" — adverb before adjective ✓ |
| @53 | 37-11-79-85-58 | "[37] la. Tout [85-verb]…" — pronoun subject ✓ |
| @396/@1227 | 64-79-82-48 | "qui tout m [48]" — STRAINED (finder's adverse note) → **fenced to P6** |
| @468/@1010/@1089 | 79-80 (+06/78) | "tout [80]" ×3 — determiner + noun, grammatical ("tout homme"-shaped) ✓; 80's noun leg |
| @496 | 02-79-88-47 | "tout [88]" ✓ neutral |
| @594 | 00-92-79-85-01 | "[92] tout [85-verb]" — pronoun + verb ✓ |
| @883 | 31-79-68-37 | "[31=VERBAL] tout [68]" — object "everything" ✓ |
| @1364/@1688 | 62-94-79-14-60 | "on ne tout [14]" — word order fails → **fenced**: 94's value disputed here (94="ne" can't precede "tout" without a verb; the "en"/"re" rivals are live). Cause stated; the problem is 94, not 79. |
| @1419 | 84-79-15-33 | "[84] tout [15]" ✓ neutral |
| @1682 | 46-79-65-13 | "que tout [65]" ✓ |

Zero hard contradictions. Two fenced items, both with stated causes
(P6's dedicated battery; 94's polyvalence).

### "tout 80" ×3 — the finder's open item, resolved as lead
@468/@1010/@1089 share "79-80" with 80's successors 06/78/06. "tout [80]"
is grammatical (determiner+noun), so this is not a contradiction — it is
80's first noun-frame leg (80 as noun after "tout"). Queued for the 80
battery.

## Verdict: PROMOTE

**79="tout" is PROMOTED.** Three independent compositional legs, each built
only on banked/promoted/P1-confirmed values: "toutefois" ×2 (uses 17),
"tout cela" (uses P1's "cela"), "tout ce qui" (uses 87+64). Full 18-window
scan: zero hard contradictions, two fenced-with-cause residuals.
**Weakest leg (named for the red team):** the "toutefois" mute-e absorption —
the composition needs "toute"+"fois"→79+17, which relies on the clerk's
documented mute-e habits rather than a byte-exact spelling match.
**Fenced residuals:** P6 trigram @396/@1227 (dedicated battery queued);
"94-79" ×2 @1364/@1688 (94's value, not 79's).
