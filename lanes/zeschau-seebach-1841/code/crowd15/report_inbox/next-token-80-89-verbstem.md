# Battery A8 — 80/89 verb stems ("ce le [verb]" @515/@869; "tout 80" ×3 tension)

Date: 2026-10-07. Runner: battery-runner (resumed, round 15).
Stream: repaired 1,847-pair parse recomputed in-session
(`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`,
per `code/side-keyhunt/repair_parse.py`).

Source: finder C3 (next-token-findings-que-ce.md); A5's "tout 80" ×3.
Standing: 87="ce" promoted; 77="le" provisional (dependency noted);
79="tout" promoted (A5).

## Pre-registered bar (written BEFORE touching data)

- **PROMOTE verb-frame** for 80 (resp. 89) iff: (a) its C3 window parses as
  "ce le [verb]" with zero board contradiction (depends on 77="le" —
  if 77 falls, this frame falls with it; say so); (b) its contact profile
  is verb-compatible (predecessors: subject/clitic/demonstrative slots;
  successors: complement-like spread, not determiner-like); (c) ≥1
  independent verb-frame leg beyond the C3 window (else HOLD).
- **80-vs-89:** same-slot comparison per the homophone standard (joint
  frames + distribution test). Verdict one of: SAME (merge candidate),
  DISTINCT verbs, or UNRESOLVED.
- **"tout 80" ×3 tension (A5):** A5 read "tout [80]" as determiner+noun.
  If 80 verb-promotes here, reconcile: either (i) 80 is polyvalent
  (verb/noun homograph — needs both frames solid), or (ii) one reading
  yields. Do NOT hold both readings silently — pick with cause or HOLD
  both.
- **KILL** the verb reading for a group if its C3 window contradicts it
  or its profile is noun-locked.

## Data

### C3 windows (re-derived)

- @515–519: `…56-87-77-80-09…` = "ce le [80] [09]" — "this [80]s it" ✓
- @869–873: `…70-87-77-89-48…` = "ce le [89] [48]" — "this [89]s it" ✓
Both depend on 77="le" (provisional) — if 77 falls, these frames fall.

### Contact profiles

**80 (n=17):** preds 29×4 ("er"), 98×3, 79×3 ("tout"), 24×2, 52×2, 77, 50, 21.
sucs 06×2, 03×2, 77×2, 04×2, 50, 09, 97, 10, 78, 47, 17, 67, 08, 22.
Verb-compatible: post-infinitive slot (29×4), clitic/demonstrative preds,
diverse complement sucs. Independent verb legs beyond C3: "tout [80]" ×3
(@469, @1011, @1090 — re-read below) + post-"er" ×4.

**89 (n=14):** preds 29×5 ("er"), 24×3, 52×2, 77×2, 18, 28.
sucs 48×3, 84×2, 68, 61, 28, 88, 11, 24, 26, 16.
Verb-compatible. Independent verb legs beyond C3: post-"er" ×5.

### 80-vs-89 (homophone standard)

- Shared (pre, suc) frames: **0**.
- Shared pre classes: {77, 29, 24, 52}; shared suc classes: **0**.
- Predecessor distributions: p=0.31 (same verb class).
- Successor distributions: **p=0.0021** (significantly different).
→ Same class, different verbs. No merge.

### Corpus check (adverse note, honest)

"ce le [verb]" is rare in the 1841 corpus (hits are "ce le [noun]" with
comma intonation: "ce le régime/moment/droit"). The C3 parse is
grammatical but uncommon — it survives as the ONLY grammatical parse of
"87-77-80/89" (demonstrative "ce" + object "le" + verb), not as a
high-frequency frame. Downgrades C3 from "clean" to "best available".

### "tout 80" ×3 tension — RESOLVED

A5's determiner+noun read ("tout [80-noun]") yields: "tout [80]" ×3
re-reads as pronoun+verb ("everything [80]s" — cf. A7's corpus "tout me
[verb]" ×4 pattern). The three windows (@469/@1090 "00-33-79-80-06",
@1011 "18-79-80-78") all accept "…tout [80-verb]…". **Correction to A5:**
80's noun lead is retired; 80 is verb-framed in all its windows.

## Verdicts

- **80: PROMOTE verb-frame** (conditional on 77="le"): C3 window clean +
  2 independent verb legs ("tout [80]" ×3, post-"er" ×4). Value NOT promoted.
- **89: PROMOTE verb-frame** (conditional on 77="le", weaker — 2 legs:
  C3 window + post-"er" ×5). Value NOT promoted.
- **80-vs-89: DISTINCT** — zero shared frames, zero shared successor
  classes, successor distributions differ (p=0.0021). Same verb class,
  different verbs. Do not merge.
- **A5 correction:** "tout 80" ×3 = pronoun+verb, not determiner+noun.
- **Caveat for the red team:** both promotions inherit 77="le"'s
  provisional status; the corpus shows "ce le [verb]" is grammatical but
  rare — the frame is "best available parse", not "typical construction".
