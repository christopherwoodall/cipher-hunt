## bibliographer: French-system key tables — one full table found, era table a clean negative
- Context: I was hunting PUBLISHED French diplomatic/military syllabaries of the 1830s–1840s
  that could be the key family for R5005 (Saxon diplomacy leaned on French models; Saxon-side
  keys already ruled out by lane N7). Searched Kahn secondary material, DECODE/de-crypt.org,
  HistoCrypt, openedition, Gallica, archive.org, ARCSI, and general web, in EN+FR.
- Decision: promoted ONE complete table to `tables/petit-chiffre-grande-armee.json` (144
  groups, hand-transcribed from the ARCSI reproduction of Bazeries 1901, pp. 275–277), and
  called a **clean negative** on any published 1830s–40s French diplomatic table. Also
  recorded structural intel (group-count ladder, homophone/null policy, grand/petit tiering)
  in `tables.md`, and the full query-by-query trail in `search-log.md`.
- Why: the Petit Chiffre de la Grande Armée is the only complete published table of the
  French *petit-chiffre class* — the ~100-cell routine-correspondence syllabary tier that
  R5005's 96-of-100 two-digit groups belong to (vs the 587–1,200-cell grand-chiffre tier).
  Its design grammar is the calibration prior: sparse homophones on frequent syllables
  (10 sets/22 groups: es×3, la×2, I,J×3…), stem+completion word-family packing (39→al/
  Allemagne/aland/als/ales), digits-as-groups, no nulls. DECODE's own R5005–R5008 records
  carry zero key metadata (all Key: fields empty), and no DECODE paper describes the family.
- Enlightenment: two things changed my picture. (1) Napoleon's March 1813 order explicitly
  demanded *two* chiffre kinds (corps commanders vs army commanders) — the grand/petit
  tiering was formal doctrine, and Bazeries 1896 says the 1813 grand chiffre had 1,200
  groups while fr.wikipedia claims ~2,000 for "Napoleon's" generally: different editions,
  both recorded, the 1,200 better sourced. (2) I nearly logged Palluel's *Dictionnaire de
  l'Empereur* (1969) as a codebook lead from an intelligence-history citation — it's a
  dictionary of Napoleon's *sayings*. Killed before it polluted the tables file.
- For the report: "Key hunt / published tables" — 1 table transcribed (petit-chiffre JSON,
  144 groups, Napoleonic, family reference not the key); era-specific table = clean negative
  (20 queries + 13 source checks logged); structural prior for R5005 = ~100-cell French
  syllabary, homophone budget ~10–20% of cells, no nulls. Note for tester: the JSON's
  groups are 1–3 digits so it can't run in test_table.py as-is (documented in tables.md).
- Caveats: the table is Napoleonic, not Saxon-1841 — family resemblance only, never a key
  claim. The 1833 French-envoy key-theft anecdote (Kahn) came from an unofficial online
  full text — verify against print before citing. Gallica/HathiTrust/archive.org were
  variously blocked from this VM, so "no published 1830s–40s table" means "none findable
  through accessible channels" — a follow-up with library access should check Vesin 1840
  (deciphering manual, low key value) and the BnF's Bazeries holdings.
