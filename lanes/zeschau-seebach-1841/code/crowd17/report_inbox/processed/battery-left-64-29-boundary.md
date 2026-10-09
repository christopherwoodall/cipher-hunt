# Battery report: left-64-29-boundary

- Target id: `left-64-29-boundary`
- Claim: "64->29 x3 (@290, @684, @1199) decides 29 word-initial vs suffix."
- Date: 2026-10-09
- Worker: battery worker (subagent 3a0e8ecc-2a88-4541-a977-d477134aa94a)
- Stream: repaired 1,847-pair / 96-type parse from `code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, re-derived in-session (asserts: 1847 pairs, 96 types). `canonical.py` never used. R5005, sealed gates, red-team queue untouched. 1841 diplomatic French only.

Terms (ASD-STE100): "word-initial 29" = a word boundary sits between 64 and 29 (64="qui" stands as its own word, 29 starts the next word). "word-internal/suffix 29" = 64+29 form one word ("qui" absorbed as letters, e.g. "quière"-family). "@" = 0-based stream index (1-based lane equivalents given).

## Bar (queue verbatim, pre-registered before testing)

"resolve iff all three 64->29 windows parse under one word-boundary reading with 29's suffix-profile stated"

Numbered pass/fail clauses (restated before testing, not modified after):

1. (C1) Census all three 64→29 windows with byte-exact contexts.
2. (C2) State 29's suffix-profile (follower inventory).
3. (C3) Resolve iff all three windows parse under ONE word-boundary reading; else fence.

No adverses listed on the target.

## Method

1. Read `BATTERY-PROTOCOL.md` first. Created `code/crowd17/next-token/locks/left-64-29-boundary.lock` on start (agent id + UTC timestamp); deleted on completion.
2. Re-derived the repaired stream in-session; byte-exact census of "64 29" bigrams (exactly 3), "29 40 65" trigrams (exactly 3), 29 followers, "29 45" (x1), "45 58" (x1).
3. Tested against standing values: 64="qui" granted as a word (§7), 29="er" banked GT, 45="ce" HOLD, 40="e" banked GT. Adopted as premises (not re-litigated): rel-09-290's fenced W1 parse ("...qui [29-40-65 verb]..."), stem48-qui-65-hapax's fence of the syllabic-'qui' arm against the 64 grant, ere-word-65-frames' fenced "quière" composition (no standalone French word "quière"; single corpus hit is a "boutiquière" OCR line-break artifact).

## Window-level evidence

### Census (C1)

- W1 — 1b@291 (0b@290), row a2_03: `28 00 97 09 64 29 40 65 16 01 11`
- W2 — 1b@685 (0b@684), row a5_00: `09 07 00 92 64 29 40 65 94 29 60`
- W3 — 1b@1200 (0b@1199), row a7_00: `16 96 82 16 64 29 45 58 47 43 55`

### 29's suffix-profile (C2)

n(29)=45. Followers: 40 ×9, 89 ×5, 47 ×4, 80 ×4, 42 ×3, 85 ×3, 87 ×3, 82 ×3, 67 ×2, 48 ×1, 88 ×1, 60 ×1, rest singletons. The dominant 29→40 contact (×9, incl. the "29 40 65" trigram) is the "ere" 3pl-past-historic ending frame; 29 never occurs word-initial with a *named* French word elsewhere in the standing record.

### W1 and W2: word-initial 29 (decided)

- The "29 40 65" trigram is byte-identical at W1 (1b@292) and W2 (1b@686), and a third occurrence exists at 1b@1711 (`26 12 06 29 40 65 94 44 59`, row a8_06) **without** any preceding 64. The trigram therefore parses as the standalone word unit [29 40 65] (the "[X]èrent" 3pl verb, cf. ere-word-65-frames' licensable string "quiere...entere"), and 64 at W1/W2 is an independent preceding word — "qui", the standing grant.
- The word-internal rival ("qui"+"er" absorbed into a "quière"-family word, including the acquière/requière arms) is fenced against the grant: stem48-qui-65-hapax tested the syllabic-'qui' reading and it fails against granted word 64='qui' (grant scope is red-team venue, not adopted); ere-word-65-frames found no standalone French "quière".
- Verdict per window: **word-initial boundary (64 | 29)** at W1 and W2, with zero new assumptions.

### W3: fenced (undecidable at battery grade)

- "29 45" and "45 58" are both stream hapax; no distributional leverage.
- Word-initial arm: "qui" + a 29-initial word — but the 29-word would be bare "er" (not a French word), and 45="ce" is a granted word (HOLD), not licensable letters for an "erreur"-family composition. No licensed [29]-word at battery level.
- Word-internal arm: absorbing 64 contradicts the standing grant (same kill as W1/W2); "quière"-family has no French existence.
- Neither arm licenses a French word at battery level → **fenced with stated cause** (not a kill; the window is unparseable, not contradictory).

## Per-clause pass/fail

- C1: PASS — all three windows byte-censused.
- C2: PASS — 29's suffix-profile stated (40-dominant "ere" frame).
- C3: FAIL (does not fire) — no ONE uniform word-boundary reading covers all three windows: W1/W2 resolve word-initial, W3 is unparseable. The bar's resolve antecedent is unmet.

## Verdict: NULL (fence executed)

Per §4: no uniform reading is demonstrable at battery level, and W3 admits no licensed parse — this is an epistemic fence, not a kill. No standing or red-team verdict contradicted (64='qui' grant respected; nothing downgraded); §7 intact. Canonical-stream caveat stands (row a7_00's offset is one of the 68 unvalidated upstream offsets). No polyvalence declared.

### Headline findings (for the supervisor)

1. **64→29 is word-initial at W1 and W2** ("qui | [29 40 65]"): forced by the byte-identical third trigram occurrence at 1b@1711 without 64.
2. **W3 ("64 29 45 58") is fenced** — both arms fail at battery level; its resolution is gated on 45/58 letter values or a named 29-initial word.

## Follow-ups proposed (nulls regenerate work)

1. `w3-64-29-lettertier` (P3) — letter-tier composition test at W3's "29 45 58" once 45/58 letter values name (or once a battery tests 29+45 as a word-final syllable). Narrow bar, discriminating frame.
2. `29-initial-word-census` (P4) — census of stream [29]-initial words to inventory the word-initial arm's licensed shapes (tests whether "er"-initial French words exist anywhere in the cipher).
3. `w3-a700-clause-reread` (P4) — full-clause re-parse of a7_00's "82 16 64 29 45 58" once 16/45/58 resolve (narrower context, may supply the W3 governor).
