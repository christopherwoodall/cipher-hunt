# Battery report: stem-03-at-1594

- Target id: `stem-03-at-1594`
- Claim: "'03 29' at @1594 infinitive-shaped or noun-shaped."
- Date: 2026-10-09
- Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` +
  `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`).
  All @-offsets below are 0-based repaired-stream indices (brief's @1594 =
  1-based @1595). Re-derived in-session: 1,847 pairs, 96 types confirmed.
  `canonical.py` never used. R5005, sealed gates, red-team queue untouched.
- Lock: `code/crowd17/next-token/locks/stem-03-at-1594.lock` (created at start,
  deleted at end).

## Bar (verbatim from parent brief, pre-registered before testing)

"decide infinitive vs noun at battery grade; fence with stated cause if undecidable"

Numbered pass/fail clauses (restated before testing, not modified after):

1. **C1:** the infinitive-shaped reading "[03]er" is licensed at @1594 with
   byte evidence at battery grade.
2. **C2:** the noun-shaped rival yields no grammatical parse at @1594 under
   standing values.
3. **C3:** kill iff the window forces 03 noun-shaped; fence if neither reading
   is decidable.

## Standing premises adopted (not re-litigated)

- 29='er' pencil ground truth (banked, §7).
- `stem-03` (battery PROMOTE, 2026-10-09): 03 = verb stem, class-level; F3 =
  @1595-1b/@1594-0b ("...08 81 03 29 80..." = "[81] [03]er").
- `stem-03-nounfamily` (battery PROMOTE, finding grade, 2026-10-09): split
  package — verb stem in "03 29" x3, noun elsewhere; red-team adjudication
  venue for conditioned split vs polyvalence. This target tests only @1594,
  not the split.
- `stem-03-value` (NULL, 2026-10-09): the three "03 29" windows parse as
  "[03]er" infinitives; the stem VALUE stays open. Adopted: infinitive shape.
- A8 80 verb-frame grant (value open). 67='et' positional rule. 77='le'
  provisional. 47='ce' granted (A4). 00='pour' (A9 leg-1).
- **Known weakening since `stem-03`:** R18-008 rejected battery 24='faire',
  demoted to conditional lead; {faire, laisser} remains open. This touches
  `stem-03`'s F1 wording ("faire [03]er" @1320) but NOT F3's byte evidence
  at this window (no 24 adjacency here). Stated, not hidden.

## Window-level evidence

Locus byte-confirmed (0-based), row a8_02:

```
@1591 47 (ce)  @1592 08  @1593 81  @1594 03  @1595 29 (er)  @1596 80
@1597 67 (et)  @1598 77 (le)  @1599 81  @1600 82 (m)  @1601 98
@1602 00 (pour)  @1603 44
```

= "ce [08] [81] [03]er [80] et le [81] m [98] pour [44]"

### C1 — PASS (infinitive-shaped licensed at battery grade)

- 29='er' banked GT: "03 29" = stem + infinitive ending. No assumption.
- "03 29 80" trigram is **byte-identical x3 stream-wide** (@1030, @1320,
  @1594, 0-based) — the other two loci are verb-stem frames (`stem-03` F1/F2;
  F2's exclamatory-infinitive parse at @1030 per imp-80-set). The frame is
  structurally invariant across independent rows.
- At this window: "[03]er [80]" sits under the A8 80 verb-frame family
  (adverse-free at this window; 80's polyvalence is red-team venue, untouched).
- No ungranted assumption is needed to license the infinitive shape.

### C2 — PASS (noun-shaped rival dies at this window)

- A noun 03 would strand 29: "ce [08] [81] [NOUN-03] er [80] et le...".
  'er' alone is not a French word, and 29='er' is banked pencil GT — it
  cannot be re-segmented into a composition (any "X+29" word claim
  contradicts banked GT).
- The noun-family battery's noun-shaped windows ("pas [03]" x3,
  "[03] qui" x4, "ce [03]" x2) are all **29-free**; its own report
  explicitly excluded the "03 29" x3 windows from the noun arm.
- No French parse exists for "[NOUN] er" here. The rival fails at the
  lexicon level, not at the assumption level.

### C3 — does not fire

No window forces 03 noun-shaped at @1594; the noun rival fails C2.
Neither reading is undecidable, so no fence.

## Verdict: PROMOTE (infinitive-shaped at @1594)

C1 and C2 pass; C3 does not fire. "03 29" at @1594 (0-based; brief's
1-based @1595) is infinitive-shaped: **[03]er**, 03 = verb stem at this
window. This corroborates (does not re-open or downgrade) standing
`stem-03`'s F3. The evidence note's conditional does not fire: 03 is not
nominal at this window, so the infinitive+DO frame stands and @1596's
question does not re-open.

## Caveats (stated, not hidden)

- The @1030 sibling leg (F2, exclamatory infinitive) carries the
  demonstrative-head bare-exclamatory-infinitive adverse (0 genuine across
  14 plays / 27.66M-char prose — hard corpus fence). The @1594 frame does
  not rely on that skeleton: it is licensed by 29='er' GT + the A8 80-frame.
- 03's stem VALUE stays open (`stem-03-value` NULL stands); the
  stem-vs-noun split package stays red-team venue (`stem-03-nounfamily`
  stands). This battery names no value and declares no polyvalence (§7).
- Canonical-stream caveat stands (row a8_02 offset unvalidated).

## Follow-ups

None — verdict is promote; per §4 kills and nulls regenerate, promotes do
not. The next-step work on 03's noun VALUE (not this window) is already
queued as `stem-03-nounfamily` follow-up 1.

## Bookkeeping

- Queue: `stem-03-at-1594` → `status: verdict`, `result: promote`,
  2026-10-09 (pre-write assert passed — was queued/verdictless; temp-file +
  rename; JSON re-validated; own entry only; no downgrade).
- Lock `locks/stem-03-at-1594.lock` created on start, deleted on completion
  (verified gone).
- No standing verdict contradicted or downgraded; §7 intact; R5005, sealed
  gates, red-team queue untouched; canonical.py never used.
