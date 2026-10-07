# Verdict: Petit Chiffre de la Grande Armée vs R5005 (coordinator analysis, 2026-10-07)

Source table: `tables/petit-chiffre-grande-armee.json` (144 groups, Bazeries 1901 via ARCSI).

## Testability: NOT DIRECTLY TESTABLE
- Petit-chiffre groups are numbered with 1–3 digits (keys like '7', '46', '106', '141'); R5005 uses
  strictly 2-digit groups (00–99, 96 occurring). There is no defined mapping between the two
  addressing schemes, so `test_table.py` cannot apply it. This is a structural incompatibility,
  not a near-miss.

## Structural comparison (syllable inventory vs our 7 ground-truth anchors)
| anchor | in petit-chiffre? |
|---|---|
| la | yes — 2 homophone groups (106, 109) |
| pre | ABSENT |
| m | yes — group 141 |
| i | ABSENT |
| er | yes — group 62 |
| e | ABSENT |
| que | yes — group 136 |

- 3 of 7 anchor syllables (pre, i, e) have no counterpart at all in the petit-chiffre inventory.
- Design differences: Napoleonic military vocabulary packing (e.g. group 39 → al/Allemagne-family
  fragments), 144 groups vs our 96, 1–3 digit addressing vs strict pairs.
- Homophone policy: petit-chiffre uses sparse homophones on frequent syllables (la×2 etc.);
  our cipher shows polyvalence (06, 94 ne/en islets, 52) — same *instinct*, different implementation.

## Conclusion
The petit chiffre is definitively NOT the key family for R5005 — wrong era (Napoleonic vs 1841),
wrong addressing, incompatible syllable inventory. It stands as a family/structural reference only:
it confirms R5005's 96-of-100-group shape belongs to the documented French *petit-chiffre* tier
(~100-cell routine-correspondence class), which is itself a useful calibration of the cipher's design.
