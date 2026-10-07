# Candidate key tables — French-system syllabaries (bibliographer, 2026-10-07)

Scope: PUBLISHED French diplomatic/military syllabaries and code tables that could be the
key *family* for R5005 (Zeschau→Seebach, 18 Jan 1841, two-digit syllabary, 96 of 100 groups
observed, ~1,846 pairs). Saxon-side keys were already ruled out (lane N7: no DECODE key for
the 1840s; latest Dresden key R2334, 1799–1806). Machine-readable copies in `tables/*.json`.

## 1. TESTABLE CANDIDATE (full transcription)

### Petit Chiffre de la Grande Armée — table chiffrante (complete)
- **File:** `tables/petit-chiffre-grande-armee.json` (144 groups, keys "1"–"182")
- **Provenance:** Association des Réservistes du Chiffre et de la Sécurité de l'Information
  (ARCSI), document Tant/371 — https://www.arcsi.fr/doc/Tant/371.pdf
  (retrieved 2026-10-07; PDF text layer hand-transcribed, see JSON `meta`).
  Reproduced there from: Commandant Étienne Bazeries, *Les chiffres secrets dévoilés*,
  Paris: Charpentier et Fasquelle, 1901, pp. 275–277. Napoleonic-era table; the 1901 book
  is public domain (Bazeries d. 1931).
- **How found:** web search for Bazeries' *Chiffres secrets dévoilés* table reproductions.
- **Structure:**
  - 144 groups numbered 1–182 (not all numbers used); syllabic French.
  - Each group = a syllable **stem plus listed completions**: the group stands for any
    listed value, and stem+completion reads as a word family
    (e.g. 39 → al / Allemagne / aland / als / ales; 22 → ar / arme / are / ars /
    armement / armements; 71 → fo / for / force / forces / fort / forte / fortes /
    fortement). This is a compressed nomenclator: one group covers an inflected word family.
  - Single letters have dedicated groups; case distinguished (37=B vs 141=m; 90=O vs 147=o).
  - Digits 0,1,2,3,5,9 have dedicated groups (7=Zéro, 46=Un, 44=Deux, 26=Trois, 1=Cinq,
    2=Neuf; 4,6,7,8 not listed — presumably spelled out).
  - **Homophones (primary readings only):** 10 sets / 22 groups — I,J ×3 (87,89,119);
    es ×3 (82,86,182); la ×2 (106,109); pu ×2 (160,162); ar ×2 (22,25); ca ×2 (4,32);
    di ×2 (75,67); fo ×2 (17,71); ga ×2 (51,78); in ×2 (118,48). Sparse, and aimed at
    frequent syllables.
  - **Nulls:** none listed. Every group maps to a syllable, letter, or digit.
  - Only the *table chiffrante* is reproduced in the ARCSI doc (no déchiffrante).
- **Why it matters for R5005:** this is the documented French **"petit chiffre"** class —
  the small, routine-correspondence syllabary tier. R5005's 96-of-100 two-digit groups put
  it in exactly this class (~100 cells), versus the 600–1,200-cell grand-chiffre tier.
  Structural calibration even if the key itself differs: expect a ~100-cell syllabary,
  sparse homophones on frequent syllables, digits-as-groups, no nulls.
- **Testability caveat:** groups are 1–3 digits (1..182), NOT two-digit, so this table
  cannot be fed to `test_table.py` as-is (it requires `\d{2}` keys). Kept as a
  family/structural reference. A tester-side adaptation (e.g. syllable-inventory
  comparison against R5005's reconstructed inventory) is possible but was out of scope.

## 2. REFERENCE TABLES (published, not transcribed — wrong era/scale for direct testing)

### Grand Chiffre de Louis XIV (Rossignol, ~1680s) — 587/597 groups
- The two surviving tables (597 groups per fr.wikipedia's *Étienne Bazeries* article, §
  "Les 2 tables (seulement 597 groupes) du grand chiffre de Louis XIV sont disponibles")
  are reproduced at familleleeger.blogspot.com (cited as ref [6] on
  https://fr.wikipedia.org/wiki/Étienne_Bazeries; consulted 2026-10-07 — direct blog URL
  not recovered verbatim, recorded here via the Wikipedia citation).
- Syllabic nomenclator; Bazeries broke it ~1893 via the repeated 124-22-125-46-345 =
  "les ennemis" cribs. Two-part construction (table chiffrante / table déchiffrante).
- Value: the archetype of the French syllabic tradition. Too early (17th c.) and too large
  (597 vs 96 groups) to be R5005's key family directly.

### Napoleon's 1813 "grand chiffre" (Hamburg) — 1,200 groups
- Étienne Bazeries, *Les "Chiffres" de Napoléon pendant la campagne de 1813* (Fontainebleau:
  Maurice Bourges, 1896; full PDF at https://bribes.org/crypto/Bazeries_Chiffres_de_Napol%e9on_I.pdf,
  public domain; retrieved 2026-10-07).
- Bazeries states the submitted cipher had **1,200 groups** ("celui de Louis XIV n'en avait
  que 600"); in use from August 1813 to early February 1814. He partially reconstructed it
  from dispatches found at Aix-la-Chapelle (Archives nationales / Dépôt de la Guerre), some
  with translations — **no complete table is published**, only worked decipherments with
  group numbers (e.g. 472, 855, 1072, 1095, 1169 — mixed inline with cleartext words).
- NOTE a discrepancy: fr.wikipedia's Bazeries article says Napoleon's cipher had "~2000
  groups". Bazeries 1896 (primary) says 1,200 for the 1813 Hamburg edition; the ~2000
  figure may refer to a different edition. Both recorded; the 1,200 is better sourced.

## 3. STRUCTURAL INTEL (no full table — calibrates expectations for the 1841 key)

| Fact | Source |
|---|---|
| French diplomatic/military codes of the era were **syllabic nomenclators**, not letter substitutions | Kahn, *The Codebreakers* (Rossignol chapter); Strasbourg article (journals.openedition.org/rbnu/1501) |
| **Two-part (mixed) nomenclator** invented by Rossignol: *table chiffrante* (plain alphabetical → mixed groups) + *table déchiffrante* (groups numerical → mixed plain) | Kahn, *The Codebreakers* |
| **Tiered system — grand vs petit chiffre.** Grand chiffre (587–1,200 groups) for ultra-secret; **petit chiffre (~100–180 groups) for routine correspondence.** Napoleon's 2 March 1813 order explicitly demanded *two kinds*: "un chiffre avec les différents commandants des corps" and "un chiffre avec les commandants de l'armée" | Bazeries 1896 (letters quoted pp. ~30–33 of PDF); fr.wikipedia *Grand Chiffre* (Petit Chiffre "pour les communications à caractère simplement confidentiel") |
| **Group-count ladder:** 1700s nomenclators 2,000–3,000 elements (Kahn); Napoleon's 1813 grand chiffre 1,200 (Bazeries 1896); Grand Chiffre 587–597; French war-ministry nomenclators under Louis XV "several hundred number groups" in disarranged order (Kahn); **Petit Chiffre de la Grande Armée 144 groups**; **R5005: 96 of 100 two-digit groups** | Kahn; Bazeries 1896; ARCSI doc; lane canonical parse |
| **Homophone policy:** used deliberately on frequent items. 1690 royal order: governors must "use the homophones in the new nomenclator and not always repeat the same cipher character" (Kahn). Petit chiffre: 10 homophone sets / 22 groups, all on frequent syllables (es×3, la×2, I,J×3…) | Kahn; petit-chiffre JSON `meta.homophones` |
| **Nulls:** standard in the French tradition (Renaissance tables had *nulles*; Charles Quint's 1547 key had 9+ null symbols). **Not** present in the petit-chiffre table; upstream null-digit tests on R5005 showed no gain | Strasbourg openedition article; fr.wikipedia *Correspondance chiffrée de Charles Quint*; upstream-NOTES.md |
| **Continuity:** "Un chiffrement du type du Grand Chiffre de Louis XIV était encore en usage dans l'armée française lors de la guerre de 1870, et dans la diplomatie allemande pendant la Première Guerre mondiale" — the French syllabary model survived into the late 19th c. | Strasbourg, témoin de l'évolution de la cryptologie (journals.openedition.org/rbnu/1501) |
| **Physical codebooks:** French diplomatic keys were physical books subject to theft — Kahn notes that in 1833 the key of the French envoy was stealthily removed, copied and replaced from a cupboard in the French legation secretary's bedroom (consulted via unofficial online full text of *The Codebreakers*; verify against print) | Kahn, *The Codebreakers* |
| **DECODE on the R5005 family:** records R5005/R5006/R5007/R5008 (all Zeschau→Seebach, HStAD 10731 Nr. 12) tag cipher type "Simple substitution, Homophonic substitution"; **every Key: metadata field is empty** — no key record, no nomenclature size, no syllable/word lists. R5005: "interlinear decrypted, but unfortunately rubbed out". R5007's title date (13.06.1846) contradicts the letter (13 June 1842; upstream already noted). R5008: "spaces between numbers are marked with pencil cuts" — potentially useful for segmenting R5008 | https://de-crypt.org/decrypt-web/RecordsView/5005 (5006/5007/5008), retrieved 2026-10-07 |
| **No DECODE publication** found describing the key system of the R5005 family; the DECODE database paper (Megyesi, Blomqvist, Pettersson, HistoCrypt 2019) is a general collection description | web search 2026-10-07 |

## 4. CLEAN NEGATIVES (published 1830s–1840s French diplomatic tables)

- **No published French diplomatic syllabary / code table of 1830–1848 was found.** Searched
  in English and French across: Kahn summaries/secondary sources, DECODE/de-crypt.org,
  HistoCrypt proceedings, openedition.org academic books/articles, Gallica (SRU blocked,
  403), archive.org, ARCSI docs, and general web. See `search-log.md` for the full query list.
- **No July-Monarchy-specific description** of the French Foreign Ministry's code system
  found in published literature (the bureau-du-Chiffre histories found cover the telegraph
  era, 1850s+, or the 1904 reorganization).
- **Kahn's *The Codebreakers*:** the French material located covers the Rossignol era,
  black chambers, and the 19th-century *dilettantes* — no passage describing a
  19th-century French diplomatic table was found. (Consulted via an unofficial online full
  text; the 1833 key-theft anecdote above should be verified against print.)
- Near-miss recorded and killed: André Palluel's *Dictionnaire de l'Empereur* (Plon, 1969),
  cited in an intelligence-history excerpt, is a dictionary of Napoleon's *sayings*, not a
  codebook — not relevant.
- Identified but not retrieved (low key-candidate value): Ch.-Fr. Vesin, *La cryptographie
  dévoilée* (Paris: Deprez-Parent, **1840**) and *Résumé* (1844) — a deciphering manual, not
  a codebook; HathiTrust page images exist but the catalog was Cloudflare-blocked and the
  archive.org query failed. Listed in search-log for completeness.

## Bottom line for the key hunt
The French model gives a sharp structural prior: R5005's 96-of-100 two-digit groups =
**petit-chiffre tier** — a ~100-cell French syllabary with sparse homophones on frequent
syllables, digits-as-groups, word-family packing (one group per inflected family), no
nulls, two-part (chiffrante/déchiffrante) construction. The transcribed
`petit-chiffre-grande-armee.json` is the only complete published table of this class found;
it is Napoleonic, not Saxon-1841, so it is a **family reference, not the key** — but any
reconstructed R5005 table should be sanity-checked against its design grammar (cell count
≈ 100, homophone budget ≈ 10–20% of cells, stem+completion packing).
