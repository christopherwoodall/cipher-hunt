# French petit-chiffre doctrine — why R5005 looks the way it does

Date: 2026-10-07. Lane: zeschau-seebach-1841.
Sources: key-hunt fleet, `code/side-keyhunt/tables.md` (full provenance there).

## The 1690 royal order: homophones were mandatory

In 1690 the French crown ordered its governors to **"use the homophones in the
new nomenclator and not always repeat the same cipher character"**
(Kahn, *The Codebreakers*; consulted via an unofficial online full text —
verify against print before citing externally).

This matters because it reframes what the lane found. F33 (conditioned
polyvalence: 4 groups — 06/52/94/78 — each with verified falsifiable
conditioning rules, zero free cases) is not an anomaly or a defect of the
cipher. It is the *expected design* of the French system: homophones were
doctrine, assigned deliberately to frequent syllables and their use was
ordered from the top. The Petit Chiffre de la Grande Armée (144 groups,
transcribed at `code/side-keyhunt/tables/petit-chiffre-grande-armee.json`
from Bazeries 1901 via ARCSI) shows the pattern concretely: 10 homophone
sets / 22 groups, every one on a frequent syllable (es×3, la×2, I,J×3,
pu×2, ar×2, ca×2, di×2, fo×2, ga×2, in×2).

Corollary for the lane: "free" polyvalence (any group standing for any of
several syllables at the encipherer's whim) would actually *violate* the
doctrine's spirit — homophones were assigned cells in the table, not
improvised. This independently supports F33's "conditioned, not free"
position: each polyvalent group should have a discoverable rule.

## Word-family packing: one group per inflected family

The petit-chiffre table is a *compressed nomenclator*. Each group is a
syllable **stem plus listed completions**: the group stands for any listed
value, and stem+completion reads as a word family. Examples from the table:

- 39 → al / Allemagne / aland / als / ales
- 22 → ar / arme / are / ars / armement / armements
- 71 → fo / for / force / forces / fort / forte / fortes / fortement

One group covers an inflected word family — not one syllable, not one word.
For the lane, this is the leading explanation of the **06/86 complementary
distribution** (finite/imperative vs infinitive-complement contexts, Fisher
7.3e-06): 06 and 86 are plausibly stem allomorphs of one family cell, the
way 22 covers both "arme" and "armement". It also predicts that some of our
"unidentified groups" are not missing syllables but family completions of
groups we already hold.

## The tier system: R5005 is petit chiffre

French doctrine tiered its codes. Grand chiffre (587–1,200 groups) for the
ultra-secret; **petit chiffre (~100–180 groups) for routine correspondence**
— Napoleon's 2 March 1813 order explicitly demanded *two kinds*. The
group-count ladder:

- 1700s nomenclators: 2,000–3,000 elements
- Napoleon's 1813 grand chiffre: 1,200
- Grand Chiffre (Louis XIV): 587–597
- Petit Chiffre de la Grande Armée: 144
- **R5005: 96 of 100 two-digit groups**

R5005 sits squarely in the petit-chiffre tier: a ~100-cell routine
syllabary. Design grammar to sanity-check any reconstructed table against:
cell count ≈ 100, homophone budget ≈ 10–20% of cells, stem+completion
packing, digits as dedicated groups, **no nulls** (the petit-chiffre table
has none, and upstream null-digit tests on R5005 showed no gain — do not
hunt nulls), two-part construction (*table chiffrante* / *table
déchiffrante*). The French syllabary model stayed in service into the late
19th century, so an 1841 Saxon office working on French lines using it is
unremarkable.

## Caveats

- Kahn passages were consulted via an unofficial online full text; verify
  against print before external citation. This includes the 1833 anecdote
  (French envoy's key stealthily copied from a bedroom cupboard).
- The Petit Chiffre de la Grande Armée is Napoleonic, not Saxon-1841: **family
  reference, not the key** (ruled out 0/7 anchors). Its groups are 1–3 digit
  (1–182), not two-digit, so it cannot be tested directly as a key.
- No published French diplomatic table of 1830–1848 was found (clean
  negative, 20 queries + 13 source checks in `code/side-keyhunt/search-log.md`).
