# Battery A6 — 09/92 homophone battery ("[09/92]+ère" @290/@684)

Date: 2026-10-07. Runner: battery-runner (resumed, round 15).
Stream: repaired 1,847-pair parse recomputed in-session
(`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`,
per `code/side-keyhunt/repair_parse.py`).

Source: finder P7 (next-token-findings-qui.md).
Anchor: @290 `64-09-29-40-65` ("qui [09] er e 65") vs @684
`64-92-29-40-65` ("qui [92] er e 65") — identical except slot 1.
Prediction: "-ière/-ère" noun ("manière"/"lumière"/"dernière" family),
09/92 same-slot pair (same shape as the now-SPLIT 23/26).

## Pre-registered bar (written BEFORE touching data)

- **PROMOTE homophone** iff ALL hold: (a) the anchor frame is byte-identical
  except slot 1 across ≥3 groups (64 _ 29 40 65 — shared pre AND shared
  3-group successor; a 4-group joint frame counts as 2 frame-legs);
  (b) contact profiles do not contradict sameness — qualitative overlap of
  predecessor/successor classes, plus a Fisher check on the top successor
  class if counts allow (n≥5 per group; else say so and use qualitative);
  (c) zero windows forcing distinct readings of 09 vs 92.
- **SPLIT** iff a clean distributional asymmetry (Fisher p<0.05 on a
  well-populated class) or any window forces distinct values.
- **HOLD** if profiles are too thin to test and the anchor is the only
  joint frame.
- **Value discipline:** the "-ère"-noun prediction is NOT promoted by this
  battery — only the 09~92 relation. The noun reading needs 65's value and
  its own legs (finder's testable item, queued).
- Contrast case on record: A2 SPLIT 23/26 on 0 shared suc-frames + Fisher
  p=0.0029. Same standard applies.

## Data

### DIRECTION CORRECTION (finder error — read first)

The finder reported "qui [09/92] er e 65". The stream says the opposite:
- @289–293: `09-64-29-40-65`
- @683–687: `92-64-29-40-65`

The varying slot **precedes** "qui": the frame is **[09/92]-qui-er-e-65**,
not "qui-[09/92]-er-e". The finder's "-ière/-ère noun" value prediction
("manière"/"lumière" family) is **directionally void** — 09/92 are not in
the "-ère" slot at all. What precedes "qui"+"er"+"e" is an open frame
question (relative-clause head? determiner?), not a noun reading. This
battery therefore tests ONLY the 09~92 relation.

### Joint frames (re-derived)

- Anchor: 5-group byte-identical frame X-64-29-40-65 (@289, @683). Strong.
- Shared predecessors beyond anchor: **84** (09@1059/@1765, 92@1022/@1379),
  **30** (09@1223, 92@1310) → 2.
- Shared successors beyond anchor: **98** (09@1059, 92@354), **07**
  (09@680, 92@978); 64 shared at anchor + 92@1022 → effectively 2–3.
- Total: **4+ joint frames beyond the anchor** — far stronger than the
  {33,86} precedent's 0/30.

### Distribution tests (honest, no cherry-picking)

Post-hoc Fisher probes (reported for transparency, NOT verdict-grade):
pred=00 → p=0.069; suc∈{79,69,60,62} → p=0.030 (post-hoc class — discounted).
Full-distribution permutation tests (20k trials, verdict-grade):
- predecessors 09 vs 92: **p=0.0455** — marginally significant, driven by a
  single class (92←00 ×6 @49/@593/@978/@1154/@330 vs 09←00 0×).
- successors 09 vs 92: **p=0.256** — not significant.

### Reading the asymmetry

92 follows 00 ("pour"-candidate) 6× with varied pre-pre contexts
(96, 09, 01, 02, 19) — a real "pour [92]" valency. 09 (n=12) never does.
This is either a true valency difference or n=12 thinness. It blocks a
clean PROMOTE under bar clause (b) but is single-class-driven and
marginal — not a clean SPLIT.

## Verdict: HOLD

**09 ~ 92 homophony is neither confirmed nor killed.** For: 5-group
identical anchor + 4 joint frames beyond it + successor distributions
indistinguishable (p=0.26). Against: predecessor distributions marginally
asymmetric (p=0.046) on 92's "pour"-valency (00×6 vs 0). The limiting
factor is 09's n=12 — the homophone hypothesis stays alive but unpromoted
until 09 either takes 00 or grows n. **Do not merge; do not split.**
**Finder correction stands:** the "-ère noun" value prediction is void
(direction error); the frame is [X]-qui-er-e-65, value unknown.

## Queued
- L1: 09's "pour"-valency (does 09 ever take 00 as n grows?) — re-test at n≥20.
- L2: the [X]-qui-er-e-65 frame — what precedes "qui"+"er"+"e"? (needs 65).
