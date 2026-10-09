# Battery `15-noun-verify` — verdict: NULL (fence)

Worker: d57e73e5-2df5-4dce-b68a-36be8a5cf596 · 2026-10-09T12:47:22Z start
Follow-up #3 of `58-value-name` NULL (2026-10-09). Feeds red-team input package `58-det-numeral-tension`.

## Bar (verbatim, pre-registered)
"name 15's class at @1696; a (plural) noun licenses the 'que [24] [85] [58=deux/plusieurs] [15]' parse and sharpens 58-det-numeral-tension's package; else fence"

Restated as numbered pass/fail clauses:
- C1: 15's class at @1696 is a (plural) noun, named on the repaired stream with zero ungranted assumptions.
- C2: the noun naming licenses the "que [24] [85] [58=deux/plusieurs] [15]" parse and sharpens the `58-det-numeral-tension` red-team package.
- C3 (else-arm): if 15 cannot be named a (plural) noun, fence with stated cause.

## Method
Re-derived the repaired 1,847-pair / 96-type stream in-session from
`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`,
parsed like `code/side-keyhunt/repair_parse.py` (asserts held: 1847 pairs,
96 types). `canonical.py` never used. Adopted premises: 46=que (banked),
17=fois (promoted), 94=ne (battery-promoted), 30=pas (battery-promoted),
79=tout (A5), 85 verb-stem (A3 frame grant), 24 finite/modal-shaped verb
class (R17-009, provisional), §7 (67 sole true polyvalence; 1690 uniformity
necessary but insufficient). Target window @1696 re-derived byte-exact.

## Window-level evidence (byte-exact, 0-based)

**Target W0 @1696** (row a8_06): `@1692..1700 = 46 24 85 58 | 15 | 23 91 85 33`
→ "…que [24] [85] [58] [15] 23 91 [85] [33]…". Note: @1692=46 is the last
pair of row a8_05 (gloss ii holds); @1701=94, @1702=30 → "…[85] [33] ne pas"
postposed "ne pas" tail (flagged for the re-parse follow-up, not decided here).

**15 census: n(15)=10** — [@323, @775, @1017, @1318, @1420, @1495, @1696,
@1730, @1760, @1811]. Predecessors: {41 x2, 60, 94, 98, 79, 66, 58, 30, 61}.
Followers: {33 x2, 93 x2, 63, 66, 24, 59, 23, 01}. 15 is NEVER adjacent to a
banked/promoted determiner (11/77/45/47): zero determiner-adjacent bigrams in
10 windows.

**Diagnostic windows:**
- **D1 @775** (a5_04): `@771..779 = 94 07 06 94 | 15 | 33 73 37 08` →
  "[94=ne] [15] [33]" with 33 verb-shaped (dire-leaning, A10 HOLD).
  "ne [15] [verb]" is the canonical French adverb/object-pronoun slot
  ("ne jamais/plus/rien/guère dire"-shaped). A bare common noun is
  ungrammatical here (*"ne conseil dire"). 15 ∈ {adverb, pronoun}; noun excluded.
- **D2 @1730** (a8_07): `@1726..1734 = 39 88 24 30 | 15 | 01 56 30 06` →
  "[30=pas] [15] [01]". "pas [15] [X]" is the canonical post-"pas" adverb
  slot ("pas encore/toujours/même"-shaped). Noun excluded.
- **D3 @1017** (a6_02): `@1013..1021 = 47 03 24 41 | 15 | 66 91 53 84` →
  "[41] [15] [66]"; 66 is infinitive-shaped (pre=00='pour' x7, A9-parallel).
  "[15] [inf]" is adverb-compatible, noun-incompatible without a determiner.
- **D4 @1318** (a7_04): `@1314..1322 = 74 62 48 98 | 15 | 24 03 29 80` →
  "[98] [15] [24]"; adverb-before-finite-verb compatible (clause-boundary
  dependent), noun needs a determiner (absent).

**Fenced residuals (compatible, not diagnostic):**
- R1 @1495 (a7_10): `@1491..1499 = 39 24 00 66 | 15 | 59 24 89 41` →
  "[66] [15] [59=est]". Resists a clean bare-adverb parse ("[verb] jamais
  est" ungrammatical); 15-as-pronoun ("en"/"y"-shaped: "[66] en est [24]")
  is the live alternative — 66's and 24's classes are open. Fenced, not decided.
- R2 @1420 (a7_08): `@1416..1424 = 52 32 84 79 | 15 | 33 21 67 33` →
  "[79=tout] [15] [33]". Needs a clause boundary under the adverb reading
  ("…on tout. [15-adv] [33]…"); fenced with cause.
- R3 @323/@1760/@1811: "60 15 63", "41 15 93" x2 — open-class contacts,
  no determiner signal, no contradiction either way.

## Per-clause results

- **C1: FAIL.** 15 profiles as adverb-class (possibly pronoun-adjacent),
  not noun-class: two diagnostic adverb slots (D1 "ne _ V", D2 "pas _ X"),
  two adverb-compatible slots (D3, D4), and ZERO noun slots in 10 windows
  (never determiner-adjacent; never verb-argument-shaped). Under §7's sole-
  polyvalence rule (67 is the only true polyvalence), 15 cannot be
  adverb-class at @775/@1730 and noun-class at @1696 — no second
  polyvalence may be declared at battery grade. The (plural) sub-requirement
  is moot: no number evidence exists and the class fails first.
- **C2: FAIL** (consequence of C1). The parse "que [24] [85]
  [58=deux/plusieurs] [15]" is not licensed: with 15 adverb-class it is
  ungrammatical ("que veut répéter deux jamais"-shaped). The finding cuts
  the other way (see below).
- **C3: FIRES.** Per the bar's else-arm: NULL, fence with stated cause.

## Adverses (none pre-listed; found in testing)
- A1 (@775 "ne [15] [33-verb]"): forces 15 ∈ {adverb, pronoun}, noun
  excluded grammatically. Fenced as the class anchor — cannot be "answered"
  under a noun claim; it is the fence post.
- A2 (@1730 "pas [15] [01]"): independent adverb-slot confirmation. Same
  fencing status as A1.
- A3 (§7 sole-polyvalence): blocks any adverb-at-D1/noun-at-@1696 split
  reading at battery grade. Standing rule, not re-opened.
- A4 (R1 @1495, R2 @1420): residuals fenced with cause above; neither
  re-opens the noun arm (R1's live alternative is pronoun, not noun).

Kill-grade note for the supervisor: A1+A2+§7 jointly force the noun claim
false at the type level, which meets §4's kill definition in strength. The
verdict is recorded NULL per the bar's explicit else-arm ("else fence");
the supervisor may harden NULL→KILL (upgrade, not downgrade, per precedent).

## Package impact (headline for `58-det-numeral-tension`)
Frame B of `58-value-name` ("que [24] [85] [58] [15]" grammatical iff 15 is
a plural noun) LOSES ITS LICENSING LEG: 15 is adverb-class, so the B-frame
numeral/determiner reading ("que [modal] [verb] deux/plusieurs [15]")
does not parse as written. The A-frame (@1756 "[58] fois") is unaffected.
The red-team package should carry this adverse: either the B-frame needs a
clause-boundary rescue ("…[85] [58]. [15-adv] [23]…") or the numeral reading
rests on frame A alone. Note the postposed "94 30" (@1701–1702) tail for the
re-parse.

## Verdict: NULL (fence)

## Follow-ups (all verified ABSENT from battery-queue.json 2026-10-09)
1. `15-value-id` (P3) — name 15's value among adverb candidates. Constraints:
   "ne [15] [33=dire]" (@775), "pas [15] [01]" (@1730), "[41] [15] [66-inf]"
   (@1017). Discriminators: "encore" fails @775 (*"ne encore dire");
   "jamais" fails @1730 (*"pas jamais [X]"); "plus" fits both ("ne plus
   dire"; "pas plus [01]" iff 01 adjectival — test 01's class). Pronoun
   rival ("en"/"y", via R1 @1495) to be fenced or pursued.
2. `1696-reparse-adverb` (P3) — re-parse the @1696 window under 15=adverb:
   (a) clause-boundary-after-58 ("…[85] [58]. [15-adv] [23] 91…"),
   (b) verb+object+adverb ("que [24] [85] [58-noun] [15-adv]" — "[inf]
   [noun] souvent"-shaped), (c) the postposed "94 30" @1701–1702 geometry.
   Deliver the surviving parse (or the confirmed B-frame collapse) to the
   `58-det-numeral-tension` docket.
3. `23-1697-class` (P4) — name 23's class at @1697 (n=8; pre {65 x3, 45 x3,
   64 x1, 15 x1}, suc {91 x2, 37, 09, 77, 99, 08}; 23~26 SPLIT granted so no
   homophone rescue via 23). Decides the "[15] [23] 91" tail parse and tests
   whether "ce [23]" (45-pre x3) mirrors a nominal frame.

## Scope
Fences 15's noun-class claim only. Untouched: all §7 standings, all
red-team verdicts, `58-det-numeral-tension` (adverse delivered, not decided),
R5005, sealed gates, red-team queue. No standing verdict contradicted.
Canonical-stream caveat stands (rows a8_06/a5_04/a8_07 offsets unvalidated).
