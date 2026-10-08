# Battery A2 — 23/26 homophone battery ("en ce qui concerne/regarde" verb slot)

Date: 2026-10-07. Runner: battery-runner (resumed, round 15).
Stream: repaired 1,847-pair parse recomputed in-session
(`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`,
per `code/side-keyhunt/repair_parse.py`).

Source: parent queue P2; finder P1 (next-token-findings-qui.md).
Anchor windows: @181 "qui 23-37-06" (64@180) and @1768 "qui 26-37-78"
(64@1767); @1774 "en ce qui est 19-48" is the est-variant of the formula.

## Pre-registered bar (written BEFORE touching data)

Claim under test: 23 and 26 are homophones (or near-synonyms) occupying the
same verb slot in "en ce qui [verb]".

- **PROMOTE homophone** iff BOTH: (a) ≥2 joint frames beyond the anchor
  windows — i.e., 23 and 26 share ≥2 distinct predecessor-bigrams or
  successor-bigrams elsewhere in the stream (the {33,86} precedent used
  joint-frame counting: 0/30 shared killed there); (b) contact profiles do
  not contradict sameness — predecessor-class and successor-class sets
  overlap with no class-exclusive asymmetry that a homophone pair would not
  show (e.g. one takes only verbal successors, the other only nominal).
- **SPLIT** (distinct groups, do not merge) iff: 0 shared joint frames
  outside the anchor AND/OR a clean distributional asymmetry (different
  successor classes, different positional behavior). Near-synonym with
  different distribution also splits the homophone claim.
- **HOLD** if 1 shared joint frame, or counts too thin to test (n<3 for
  either group makes the distribution test decorative — say so).
- **Value discipline:** this battery tests the homophone relation, not the
  "concerne/regarde" value. Do not promote a value from this battery alone.
- Note the compositional read from finder P1: 23-37-06 may be "con-cern-ent"
  (06="ent" verbal ending). If 23-37 is one word, the "verb slot" is 23-37
  jointly and the homophone claim must be re-scoped to 23-37 vs 26-37.
  Test both scopings; report which survives.

## Data

### Corpus census (re-derived)

**23 (n=8):**
| pos | window |
|---|---|
| @136 | 64-21-65-**23**-91-65-13 |
| @182 | 24-87-64-**23**-37-06-00 (anchor: "en ce qui 23-37-06") |
| @679 | 37-77-45-**23**-09-07-00 |
| @1056 | 74-74-45-**23**-77-84-09 |
| @1552 | 94-92-45-**23**-99-13-93 |
| @1609 | 11-92-65-**23**-08-55-83 |
| @1697 | 85-58-15-**23**-91-85-33 |
| @1782 | 48-74-65-**23**-98-83-82 |
preds: 65×3, 45×3, 64×1, 15×1. sucs: 91×2, 37×1, 09, 77, 99, 08, 98.

**26 (n=17):**
preds: 69×3, 11×2, 64×2, 24×2, 02, 84, 39, 94, 46, 38, 88, 89.
sucs: 12×4, 30×4, 00×3, 32×2, 35, 96, 24, 37.
Key windows: @531 "59-37-64-**26**-32" (second "qui 26" — "est 37 qui 26 32");
@1769 "24-87-64-**26**-37-78" (anchor: "en ce qui 26-37-78").

### Joint-frame test (the {33,86}-precedent standard)

- Shared predecessor-frame types outside the anchor: **1** (pre=64 "qui":
  23@182 vs 26@531/@1769). Weak — "qui" is a top-10 predecessor generally.
- Shared successor-frame types outside the anchor: **0**. 23's successors
  (91/09/77/99/08/98) never overlap 26's (12/30/00/32/35/96/24).
- The anchor's shared-37 is the single overlapping cell; everything else diverges.

### Distribution test

Successor-class asymmetry: suc ∈ {12, 30, 00}: 23 → 0/8, 26 → 11/17.
Fisher exact p = **0.0029** — significant. 26 has a locked-in successor
triad; 23's successors are all singletons/doubletons from a disjoint set.
A homophone pair would not show this clean a split at n=8/17.

### Compositional re-scoping (per the bar)

23-37 occurs 1× (@182–183), 26-37 occurs 1× (@1769–1770) — both singletons,
untestable as units. Noted: 37→78 ×4 (@312, @414, @475, @1770) vs 37→06 ×1
(@183, the 23-anchor) — the 26-anchor's "37-78" tail is the recurring shape,
the 23-anchor's "37-06" is not. This asymmetry is consistent with the SPLIT,
not a rescue of it.

### Formula check (corpus, code/side-period/corpus/)

"en ce qui concerne" ×6, "en ce qui touche" ×2 in the 1841 diplomatic
corpus. The "en ce qui [verb]" formula reading is register-typical —
the formula survives; the homophone claim does not.

## Verdict: SPLIT

**23 ~ 26 are NOT homophones.** 0 shared successor frames outside the
anchor, 1 weak shared predecessor frame ("qui"), and a Fisher-significant
distributional asymmetry (p=0.0029) on successor classes. The {33,86}
precedent would split on weaker evidence than this.
Near-synonymy is not rescued either: near-synonyms in the same slot would
still share successor-class distributions, which these do not.
**Do not merge 23/26. Do not treat "23-37" and "26-37" as the same verb.**

Surviving facts: the "en ce qui [verb]" frame is real (corpus ×8,
@1774 est-variant); 26 follows "qui" twice (@531, @1769), 23 once (@182);
the "concerne/regarde" value hypothesis stays open but unattached to a
specific group — it needs its own legs.
