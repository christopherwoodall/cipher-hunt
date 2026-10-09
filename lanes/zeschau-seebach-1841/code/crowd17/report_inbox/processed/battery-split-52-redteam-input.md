# Battery `split-52-redteam-input` — verdict: PROMOTE (package only; docket undecided)

Gather-only red-team input package for a 52 split/non-uniformity docket
item, mirroring the 88 treatment (`battery-tout-88-frame`, PROCESSED).
Locus-level evidence only. No value named for 52, no split declared, no
polyvalence claimed (red-team venue). The non-uniformity observation is
distributional, not a class claim. Docket item is NOT decided at battery
level.

## Bar tested (verbatim)

pass iff 52's tiers are packaged gather-only — verb ("qui 52" x2), adverb
("ne 52 [INF]" x2 + "la plus" x3), sub-lexical ("t52"/@630, "pre52"/@1332);
the docket item is NOT decided at battery level

## Bar restated as numbered pass/fail clauses

- C1: Verb tier — exactly two "qui 52" loci (64="qui" granted) packaged
  with 0-based @-offsets and row labels.
- C2: Adverb tier A — exactly two "94 52 80 04" ("ne 52 [INF]") loci
  packaged with 0-based @-offsets and row labels.
- C3: Adverb tier B — exactly three "11 52" ("la plus") loci packaged
  with 0-based @-offsets and row labels.
- C4: Sub-lexical tier — "t52" (08 52) and "pre52" (70 52) loci packaged
  with corrected 0-based @-offsets.
- C5: Adverses answered — plus/jamais value tie fenced per
  plus-jamais-tiebreak; no new polyvalence declared; package only, docket
  stays red-team venue; no decision made at battery level.

## Method

Repaired 1,847-pair / 96-type stream re-derived in-session from
`code/side-keyhunt/repaired_offsets.json` +
`data/upstream-ct_R5005.txt`, parsed like
`code/side-keyhunt/repair_parse.py` (asserts: 1,847 pairs, 96 types —
held). `canonical.py` never used. Full predecessor census of 52
(n(52)=27, byte-exact) to check tier exhaustiveness; every number below
traces to the stream.

## Findings — tier packages

### Tier 1 — verb ("qui 52" x2), C1

64="qui" is granted (§7). 64 precedes 52 at exactly two stream positions:

- `@1341=64(a7_05) @1342=52(a7_05)` — context:
  `@1340=65 @1341=64 @1342=52 @1343=38 @1344=47`
- `@1434=64(a7_08) @1435=52(a7_08)` — context:
  `@1433=49 @1434=64 @1435=52 @1436=82 @1437=16`

Claimed loci "@1342/@1435" point at the 52 token; bigram starts are
@1341/@1434. Census confirms exhaustiveness: no other 64→52 bigram in
the stream.

**C1 PASS.**

### Tier 2 — adverb ("94 52 80 04" x2), C2

The 4-gram "94 52 80 04" occurs at exactly two stream positions, frame
structure byte-identical (94 52 80 04) and row-internal on both:

- `@1293=94 @1294=52 @1295=80 @1296=04 (a7_03)` — context:
  `@1291=59 @1292=35 @1293=94 @1294=52 @1295=80 @1296=04 @1297=62`
- `@1806=94 @1807=52 @1808=80 @1809=04 (a8_10)` — context:
  `@1804=59 @1805=35 @1806=94 @1807=52 @1808=80 @1809=04 @1810=61`

Both frames share the same left/right trigrams ("35 94" left, "04 62/61"
right) — the frame is positionally anchored, not scattered. Claimed loci
"@1294/@1807" point at the 52 token inside each frame; 0-based frame
starts are @1293/@1806 (corrected above).

Census note (red-team relevant, not battery-decided): 94 precedes 52 at
one further locus, `@570=94 @571=52 (a3_02)`, but with a different
follower — `@569=45 @570=94 @571=52 @572=87 @573=78` ("45 94 52 87 78";
45="ce" granted A11 flanks it). The "ne 52 [INF]" tier is defined by the
full 4-gram, not the 94→52 bigram alone.

**C2 PASS.**

### Tier 3 — adverb ("11 52" x3, "la plus"), C3

11="la" pencil ground truth (§7). 11 precedes 52 at exactly three stream
positions:

- `@1006=11 @1007=52 (a6_02)` — context:
  `@1004=47 @1005=91 @1006=11 @1007=52 @1008=35`
- `@1123=11 @1124=52 (a6_07)` — context:
  `@1121=14 @1122=06 @1123=11 @1124=52 @1125=37`
- `@1721=11 @1722=52 (a8_07)` — context:
  `@1719=68 @1720=06 @1721=11 @1722=52 @1723=37`

Claimed loci "@1006/@1123/@1721" are the bigram starts; 52s at
@1007/@1124/@1722. Census confirms exhaustiveness: no other 11→52
bigram. Note @1721's frame is near-duplicate of @1123's ("06 11 52 37").

**C3 PASS.**

### Tier 4 — sub-lexical ("t52", "pre52"), C4

- "t52" — `@631=08 @632=52 (a4_01)`: context
  `@629=78 @630=67 @631=08 @632=52 @633=67`. Claimed "@630" is off by
  one; the 08 52 bigram is at @631–@632 (52 at @632). 08 precedes 52
  exactly once in the stream.
- "pre52" — `@1331=70 @1332=52 (a7_04/a7_05)`: context
  `@1329=62 @1330=94 @1331=70 @1332=52 @1333=39`. Claimed "@1332" points
  at the 52; bigram start is @1331. 70="pre" pencil ground truth (§7).
  70 precedes 52 exactly once in the stream.

Both sub-lexical frames are row-boundary-crossing-adjacent only for
pre52 (a7_04 → a7_05 at the 70/52 seam).

**C4 PASS** (with the ±1 offset corrections recorded above — package
uses the verified 0-based values).

### Tier exhaustiveness (stream-level)

Full predecessor census of 52 (n=27): 93×2, 48×2, 16, 13, 94×3, 08×1,
78×1, 11×3, 06×2, 86×2, 74, 70×1, 64×2, 68, 46, 34, 01, 28. The four
claimed tiers account for 2+2+3+2 = 9 of the 27 loci; the remaining 18
are singletons under 14 other predecessors and are out of this
package's scope (no tier claimed for them).

## C5 — adverses

- plus/jamais value tie: fenced per plus-jamais-tiebreak — the package
  records the "ne 52 [INF]" gloss as the bar's own wording and does not
  adjudicate plus vs jamais; the docket venue owns that tie.
- No new polyvalence declared: the package claims distribution only;
  no 52 value and no split is declared here.
- Package only: this report decides nothing. The split/non-uniformity
  docket item stays with the red team. Untouched: R5005, sealed gate
  instances, the red-team adjudication queue, and every §7 standing
  value.

**C5 PASS.**

## Verdict: PROMOTE

All bar clauses pass and every listed adverse is answered. "Promote"
here means only this: the gather-only package is complete and handed to
the red team as input for the 52 split/non-uniformity docket item. It is
not a promotion of any 52 value, not a split declaration, and not a
battery-level decision of the docket item. No follow-ups per §4
(promote; no null).

## Scope / caveats

- Locus-level characterization only, mirroring the 88 treatment.
- Canonical-stream caveat stands: pencil gloss on row a5_03; 68 of 70
  upstream row offsets unvalidated.
- Offset-convention note: the queue entry's stated loci point variously
  at the 52 token (@1342, @1435, @1294, @1807, @1332) or at the bigram
  start (@1006, @1123, @1721); "@630" is +1 off the verified "08 52"
  bigram (@631–@632). The package above gives verified 0-based offsets
  for every token; use these, not the mixed-convention queue figures.
- A third 94→52 bigram exists at @570–@571 (a3_02, "45 94 52 87 78")
  outside the claimed 4-gram tier — flagged for red-team review, not
  battery-decided.
- No standing/red-team verdict contradicted or downgraded; §7 intact.

## Bookkeeping

- Stream re-derived in-session; asserts held (1,847 pairs, 96 types).
- `canonical.py` never used. R5005, sealed gates, red-team adjudication
  queue untouched.
- Lock `locks/split-52-redteam-input.lock` created on start, deleted on
  completion.
