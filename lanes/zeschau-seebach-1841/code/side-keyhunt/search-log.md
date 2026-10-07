# Bibliographer search log — Seebach key hunt, 2026-10-07

Every query run and source consulted. Verdicts: FOUND / NEGATIVE / BLOCKED / KILLED.

## Web searches (browser.search)

| # | Query (lang) | Verdict | Notes |
|---|---|---|---|
| 1 | `DECODE R5005 Seebach Zeschau cipher` (en) | NEGATIVE | No DECODE-specific publications on the family; only generic cipher-news noise |
| 2 | `Kahn "The Codebreakers" French diplomatic codes July Monarchy 1840s chiffre` (en) | NEGATIVE (partial) | No July-Monarchy-specific Kahn material surfaced; led to the unofficial full-text copy (see source checks) |
| 3 | `"chiffre" diplomatique français 1840 table syllabaire ministère affaires étrangères` (fr) | NEGATIVE | Led to Grand Chiffre / Rossignol background and the openedition telegraph-era book (covers 1850s+, not our period) |
| 4 | `"bureau du chiffre" ministère affaires étrangères histoire 1830 1848 code diplomatique` (fr) | NEGATIVE | Bureau-du-Chiffre histories found are telegraph-era (1850s+) or 1904 reorganization; nothing on 1830–48 systems |
| 5 | `19th century French diplomatic cipher syllabary nomenclator two-digit groups historical cryptography` (en) | FOUND (structural) | Grand Chiffre background (587 groups, syllabic); Wouves 1797 syllabical table (US, not diplomatic) |
| 6 | `"Petit Chiffre" Rossignol diplomatic syllabary structure number groups 19th century` (en) | FOUND (structural) | Confirmed grand/petit tier distinction (Petit Chiffre = merely-confidential tier) |
| 7 | `HistoCrypt proceedings French diplomatic cipher nineteenth century key paper` (en) | NEGATIVE | Nearest: Antal et al. Slovak aristocratic keys (18th–19th c., nomenclators, not French); Bellecombe 1782 (French colonial, 18th c.) |
| 8 | `Gallica "chiffre" instruction ambassade 1840 dépêche chiffrée imprimé` (fr) | NEGATIVE | No printed 1840 instruction/table surfaced |
| 9 | `Bazeries "Chiffres secrets dévoilés" 1901 Gallica table Grand Chiffre` (fr) | **FOUND (table)** | → arcsi.fr/doc/Tant/371.pdf: complete Petit Chiffre de la Grande Armée table (Bazeries 1901, pp. 275–277) |
| 10 | `Vaillé "cabinet noir" histoire chiffre français XIXe siècle diplomatie` (fr) | NEGATIVE | Vaillé's *Le Cabinet noir* (PUF 1950) is postal-interception history, not code tables |
| 11 | `DECODE database Dresden Saxon 1841 cipher records Seebach Zeschau` (en) | NEGATIVE | Nothing beyond the DECODE records themselves |
| 12 | `Palluel "Dictionnaire de l'Empereur" Napoléon code chiffré groupes` (fr) | KILLED | It's a dictionary of Napoleon's *sayings* (Plon 1969), not a codebook — false lead from an intelligence-history citation |
| 13 | `de-crypt.org publications historical cryptology list papers` (en) | NEGATIVE | No publication describing the R5005 family's key system; only the generic DECODE-database paper (Megyesi et al. 2019) |
| 14 | `"tableau chiffrant" OR "dictionnaire chiffré" 1840 diplomatie française` (fr) | NEGATIVE | Rossignol background only |
| 15 | `Bazeries 1896 "Chiffres de Napoléon" campagne 1813 Hambourg texte` (fr) | **FOUND (structural)** | → bribes.org PDF: 1,200-group 1813 chiffre, tiered grand/petit order (Mar 1813), partial reconstruction only |
| 16 | `"monarchie de juillet" chiffre diplomatique Louis-Philippe cryptographie` (fr) | NEGATIVE | Coin-collector noise; zero cryptographic content |
| 17 | `hcportal.eu historical cryptology portal ciphers keys database` (en) | BLOCKED (partial) | Portal confirmed (Database of Cryptograms and Cipher Keys + public API advertised) but `/api` 404s and the front page is JS-only; not pursued further |
| 18 | `arcsi.fr doc chiffre diplomatique table chiffrante` (fr) | NEGATIVE | No further ARCSI tables surfaced |
| 19 | `"Tables du grand chiffre de Louis XIV" blogspot` (fr) | FOUND (reference) | Confirmed via fr.wikipedia *Étienne Bazeries* ref [6] (familleleeger.blogspot.com); direct URL not recovered verbatim |
| 20 | `"Les chiffres secrets dévoilés" Bazeries 1901 full text hathitrust OR archive.org` (en) | FOUND (bibliographic) | HathiTrust page images exist (US-access-only per OBP); full text not retrieved — but the needed table (pp. 275–277) was already captured via ARCSI. Also surfaced Vesin 1840/1844 and P.L. Jacob 1858 (see below) |

## Direct source checks (browser.open / curl)

| Source | Verdict | Notes |
|---|---|---|
| https://www.arcsi.fr/doc/Tant/371.pdf | **FOUND** | Complete Petit Chiffre de la Grande Armée table → transcribed to `tables/petit-chiffre-grande-armee.json` (144 groups) |
| https://bribes.org/crypto/Bazeries_Chiffres_de_Napol%e9on_I.pdf (Bazeries 1896) | FOUND (structural) | 1,200 groups; tiered system; no full table published; OCR poor but key passages recovered via find ("groupes") |
| https://de-crypt.org/decrypt-web/RecordsView/5005 /5006 /5007 /5008 | FOUND (negative intel) | All Key: fields empty; "Simple substitution, Homophonic substitution" tags; R5005 "interlinear decrypted, but unfortunately rubbed out"; R5008 "spaces between numbers are marked with pencil cuts"; R5007 title-date error confirmed |
| https://books.openedition.org/pur/48925 (télégramme diplomatique avant 1918) | NEGATIVE | Telegraph era (1850s+); nothing pre-1848 |
| https://journals.openedition.org/rbnu/1501 (Strasbourg cryptology history) | FOUND (structural) | Rossignol → dictionnaires chiffrés; Grand-Chiffre-type use in French army 1870 + German diplomacy WWI |
| https://fr.wikipedia.org/wiki/Étienne_Bazeries | FOUND (structural) | 597-group Grand Chiffre tables reference; ~2000-group Napoleon claim (discrepant w/ Bazeries 1896's 1,200 — recorded both); bibliography |
| https://bookreadfree.com/271442/6686651 (unofficial *Codebreakers* full text) | FOUND (structural, unverified) | Rossignol two-part nomenclator; 2,000–3,000-element 1700s nomenclators; "several hundred" French war-ministry groups (Louis XV); 1833 French-envoy key theft — **flag: verify against print; unofficial source** |
| https://onlinebooks.library.upenn.edu (cryptography bibliography) | FOUND (bibliographic) | Vesin *La cryptographie dévoilée* (Deprez-Parent, **1840**) + *Résumé* (1844) + 1857 ed.; P.L. Jacob *La cryptographie* (1858); Rochfort (1836) — deciphering manuals, not codebooks |
| Gallica SRU (`gallica.bnf.fr/SRU`, title=chiffre, 1830–1848) | BLOCKED | HTTP 403 from this VM |
| archive.org advancedsearch (Bazeries 1901; Vesin) | BLOCKED/FAILED | Creator query returned 0 docs; title query failed on transient empty response |
| Google Books API (Vesin) | BLOCKED | 429 quota-exceeded |
| HathiTrust catalog search (Vesin 1840) | BLOCKED | Cloudflare challenge page |
| https://hcportal.eu/ + /api | BLOCKED | JS-only front page; `/api` 404 |

## Deliberately not pursued
- Archive emails / outreach / account creation: forbidden by task constraints.
- Transcribing the 597-group Grand Chiffre tables: 17th c., wrong scale; recorded as reference only.
- Vesin 1840 retrieval: deciphering manual, not a codebook — low key-candidate value; documented above for a follow-up worker with better HathiTrust access.
- Saxon-side keys (DECODE record_type 2, HStAD): already ruled out by lane N7 — not redone.
- Tomokiyo's list: already checked by upstream — not redone.
