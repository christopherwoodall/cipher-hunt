# Period sources for the Seebach cipher lane — ranked source list
**Bibliographer pass, 2026-10-07.** Goal: published, web-reachable 1841-milieu text for cribs
(names, places, events, formulae, collocations) against the 18 Jan 1841 French despatch.

**Coordination:** the Harvester (parallel) owns the *retrieval* of targets **1** (Nesselrode
corpus) and **2** (ANNO Jan-1841 newspapers). This file is the bibliography it reads;
entries 1–2 are specified here so it can start immediately, but the fetch work is its lane.

Access notes: Gallica SRU is blocked — not used. Wayback only via `http://` (port 80).
Python httpx is broken on this VM; use `curl`. All listed originals are pre-1923 = public
domain. No paywalls, no outreach, no archive requests.

---
## What Zeschau was writing about (Jan 1841) — crib seeds
The Eastern Question dominated every chancellery that winter:
- **Mehemet Ali's submission**: evacuation of Syria by Egyptian forces Jan–Feb 1841
  (Gaza/Jaffa, Ibrahim Pasha embarking); the Porte's peace terms; the **firman of
  investiture** granting hereditary Egypt (issued Feb 1841); the Straits/Dardanelles
  settlement being negotiated (Unkiar-Skelessi expiring July 1841 → Straits Convention
  13 July 1841).
- France re-entering the Concert after the 1840 humiliation (Thiers fell Oct 1840,
  **Guizot** foreign minister; French resentment of the 15 July 1840 London Treaty).
- Spain: **Espartero** regency; France: Louis-Philippe/Guizot ministry; Russia: Nicholas I
  and **Nesselrode** (Seebach's father-in-law); Prussia: Friedrich Wilhelm IV's early reign;
  Austria: **Metternich**.
- Also in the air: **Kossuth** launches *Pesti Hírlap* 2 Jan 1841; Britain occupies
  **Hong Kong** 26 Jan 1841 (Opium War); Polish émigré politics; Zollverein trade politics
  (Zeschau's other portfolio).
- Likely cipher-vocabulary: *Constantinople, Londres, Paris, Vienne, Berlin,
  Pétersbourg/Saint-Pétersbourg, Sultan, Méhémet-Ali, Egypte, Syrie, Dardanelles,
  convention, traité, firman, Majesté, Empereur, ambassadeur, dépêche, cabinet,
  ministre, affaires, Porte, héréditaire, évacuation, plénipotentiaires.*

---
## Family 1 — Nesselrode correspondence (highest value: same milieu, French)

### 1. *Lettres et papiers du chancelier comte de Nesselrode, 1760–1856* (11 vols., Paris: Lahure, 1904–1912), ed. Anatole de Nesselrode
- **URL:** `https://archive.org/details/lettresetpapiers09ness_0` (vol. 9 verified on archive.org;
  full text `https://archive.org/download/lettresetpapiers09ness_0/lettresetpapiers09ness_0_djvu.txt` downloads clean, 515 KB);
  second scan (volume TBD) `https://archive.org/details/bub_gb_QidLAAAAMAAJ`.
  Remaining vols (esp. 7–8, the 1840–41 years) to hunt via Google Books / HathiTrust full view.
- **Access:** direct archive.org download (curl). No login.
- **Contains:** Nesselrode's own letters + state papers, entirely in French. Vol. 9 covers
  ~1847–56 (1848 dominant); vols 7–8 should cover 1835–45 = the despatch's window.
  Shared topics, shared phrasing, possibly shared ministerial formulae with Zeschau.
- **Language:** French. **Rights:** public domain (1904–12).
- **Priority: P0** — Harvester: fetch v.9 text now (drop in `corpus/nesselrode-v9.txt`;
  a copy is staged at `/tmp/ness_v9.txt`), then locate vols 7–8.

### 2. *Correspondance diplomatique du comte Pozzo di Borgo, ambassadeur de Russie en France, et du comte de Nesselrode, 1814–1818* (2 vols., Paris: Calmann Lévy, 1890–97), ed. Charles Pozzo di Borgo
- **URL:** archive.org identifiers confirmed live via the archive.org search API:
  `correspondanced00borggoog`, `correspondanced00nessgoog`, `correspondanced01nessgoog`,
  `correspondanced02nessgoog`, `correspondancedi01pozz`
  (e.g. `https://archive.org/details/correspondanced01nessgoog`).
  Also HathiTrust page images (UPenn Online Books Page index).
- **Access:** direct archive.org download.
- **Contains:** Russian-embassy diplomatic correspondence in French, Nesselrode's own
  hand in despatches. Earlier period (1814–18) but the *register* — chancellery French,
  openings/closings, set phrases — is the same school Zeschau wrote in.
- **Language:** French. **Rights:** public domain.
- **Priority: P1.**

---
## Family 2 — January 1841 newspapers (Harvester-owned; specs here)

### 3. ANNO — AustriaN Newspapers Online: *Wiener Zeitung* and others, Jan 1841
- **URL:** `https://anno.onb.ac.at/neu.htm` (portal); title index `https://anno.onb.ac.at/alph_list.htm`.
  28M pages; Wiener Zeitung runs through the 1840s (ANNO short code `wrz`).
- **Access:** free portal, calendar browse + full-text search, page scans + OCR.
- **Contains:** day-by-day Jan 1841 news as Vienna read it — Levant crisis, firmans,
  court/diplomatic notices. German.
- **Language:** German. **Rights:** public domain.
- **Priority: P0 — Harvester-owned.** Pull Jan 1–31 1841 Wiener Zeitung; harvest
  proper nouns + diplomatic vocabulary for the crib list.

### 4. digiPress (Bayerische Staatsbibliothek): *Allgemeine Zeitung* (Augsburg), Jan 1841
- **URL:** `http://digipress.digitale-sammlungen.de/newspaper/bsbmult00000002/info`
  (title page; issue calendar with per-day viewer links, e.g. Jan 1841 issues exist in the
  same viewer URL scheme).
- **Access:** free, full-text searchable, OCR + scans. No login.
- **Contains:** the leading German political daily of the era — the paper Saxon ministers
  actually read. Foreign-politics coverage, diplomatic notes, names/places of Jan 1841.
- **Language:** German. **Rights:** public domain.
- **Priority: P0.** Best OCR'd free German daily for the exact month.

### 5. Deutsches Zeitungsportal / ZEFYS (Staatsbibliothek zu Berlin) — directory route
- **URL:** `https://zefys.staatsbibliothek-berlin.de/` (e.g. title record
  `https://zefys.staatsbibliothek-berlin.de/list/title/zdb/24340492/-/1881/` shows the
  record layout); successor portal is the Deutsches Zeitungsportal.
- **Access:** free directory; links out to digitized papers (incl. digiPress mirrors).
- **Contains:** Prussian/German papers of Jan 1841 (e.g. *Allgemeine Preußische Zeitung*).
- **Language:** German. **Rights:** public domain.
- **Priority: P2** — use as a finder, not a corpus.

### 6. *Niles' National Register*, 1841 (U.S. weekly, reprints European news)
- **URL:** e.g. `https://archive.org/download/sim_niles-national-register_1841-10-09_61_1567/sim_niles-national-register_1841-10-09_61_1567.pdf`
  (full 1841 run on archive.org under `sim_niles-national-register_1841-*`).
- **Access:** direct archive.org download.
- **Contains:** English-language digests of the European news stream of 1841 — useful
  for event vocabulary only, not French register.
- **Language:** English. **Rights:** public domain.
- **Priority: P2.**

---
## Family 3 — Saxon diplomatic editions / Saxonica

### 7. Flathe, *Zeschau, Heinrich Anton von* (ADB vol. 45, 1900, pp. 105–108)
- **URL:** `https://de.wikisource.org/wiki/ADB:Zeschau,_Heinrich_Anton_von`
  (also `https://www.deutsche-biographie.de/pnd117597295.html?language=en`).
- **Access:** Wikisource full text, free.
- **Contains:** the standard 19th-c. biography; career chronology 1835–48 foreign ministry;
  bibliography points to Witzleben 1874. Quotes no letters at length, but fixes names,
  dates, and the scope of Zeschau's Russia/Saxony business.
- **Language:** German. **Rights:** public domain.
- **Priority: P1** (context + pointer).

### 8. Witzleben, C. D. von: *Heinrich Anton von Zeschau. Sein Leben und öffentliches Wirken* (Leipzig: Tauchnitz, 1874), VIII+334 pp., with portrait and facsimile
- **URL:** DNB record `https://portal.dnb.de/opac.htm?method=simpleSearch&cqlMode=true&query=idn%3D578404168`;
  Michigan digitization indexed at `https://core.ac.uk/outputs/66382228/`
  (oai:quod.lib.umich.edu:MIU01-010247091). Google Books API returned no full-view hit —
  try HathiTrust full view / Michigan copy directly.
- **Access:** free if a full-view scan is found; rare in print.
- **Contains:** the only book-length Zeschau biography; an archivist's work (Witzleben was a
  Saxon archivist) — most likely source to *quote Zeschau's own letters*.
- **Language:** German. **Rights:** public domain.
- **Priority: P1** — worth one lookup round; if no scan, park it.

### 9. *Weber-Gesamtausgabe*: letter Georg Rudolph von Gersdorff → Zeschau, London, 2 April 1841
- **URL:** `https://www.weber-gesamtausgabe.de/de/A00011D/Korrespondenz/A047524.html`
- **Access:** free, full transcription + apparatus.
- **Contains:** a real April-1841 letter *addressed to Zeschau himself* — address block,
  salutation, closing formulae in period German chancellery style ("mit den Gefühlen
  ehrerbietigster Hochachtung … Ew. Excellenz"). Formulae reference.
- **Language:** German. **Rights:** scholarly edition, free to read (quote briefly).
- **Priority: P1** (formulae only; one page).

### 10. Historische Kommission für Sachsen / *Neues Archiv für sächsische Geschichte* — route note
- No single published edition of Saxon foreign-ministry correspondence 1835–48 found.
  Route: SLUB Dresden digital + the journal *Neues Archiv für sächsische Geschichte*
  (articles on Zeschau/Seebach eras). NDB/Deutsche Biographie entry for
  **Albin Leo von Seebach** not yet located — check `https://www.deutsche-biographie.de/`
  name search; the ADB has no Seebach article (only the family, via Wikipedia).
- **Priority: P2** — opportunistic; do not spend more than one lookup round.

---
## Family 4 — biographies/memoirs quoting correspondence

### 11. Princess Dorothea Lieven: *Letters … during her residence in London, 1812–1834* (ed. Robinson, London 1902)
- **URL:** on archive.org (search "Letters of Dorothea Princess Lieven 1902").
- **Contains:** the inner circle's letters — Lieven was Nesselrode's close correspondent;
  British Library Lieven papers vols. XI–XX are Nesselrode correspondence 1810–1839,
  partly printed in *Lettres et papiers* vol. vii. Style/register of Russian-French
  diplomatic society.
- **Language:** English (translations). **Rights:** public domain.
- **Priority: P2.**

### 12. *Mémoires de la duchesse de Dino (afterwards duchesse de Talleyrand), 1831–1835* (Heinemann, 1909)
- **URL:** HathiTrust page images (UPenn Online Books Page index; 1909 = public domain).
- **Contains:** Paris diplomatic-society memoirs of the exact milieu, quoting letters.
- **Language:** French. **Rights:** public domain.
- **Priority: P2** (HathiTrust full-view download needs the data API; park if friction).

### 13. Sainte-Aulaire: *Souvenirs (Vienne, 1832–1841)* (Calmann-Lévy, 1926)
- **URL:** HathiTrust page images — flagged "US access only" in the UPenn index.
- **Contains:** French ambassador in Vienna's recollections ending exactly in 1841.
- **Language:** French. **Rights:** 1926 — check; likely still restricted.
- **Priority: P2** — access caveat; only if a full view turns up.

---
## Family 5 — 1840s French diplomatic formulae (openings, closings, set phrases)

### 14. Metternich: *Aus Metternich's nachgelassenen Papieren*, 8 vols. (Vienna: Braumüller, 1880–84)
- **URL:** archive.org, all volumes verified: e.g.
  `https://archive.org/details/ausmetternichsna02mettuoft/mode/1up`,
  `https://archive.org/details/ausmetternichsna03mettuoft`.
  Author index with per-volume links: `https://de.wikisource.org/wiki/Klemens_Wenzel_Lothar_von_Metternich`.
  **Vols 3–7 = "Friedens-Aera 1816–1848" — the despatches of 1840–41 live here.**
- **Access:** direct archive.org download (`_djvu.txt`), curl-friendly.
- **Contains:** Metternich's outgoing diplomatic correspondence — the other great
  chancellery of the German world writing in the same era and often the same language
  conventions. Topics overlap directly (Syrian question, Straits, the Concert).
- **Language:** German. **Rights:** public domain.
- **Priority: P0** — pull vols 4–6 texts now; mine for diplomatic vocabulary + topics.

### 15. Guizot: *Mémoires pour servir à l'histoire de mon temps*, 8 vols. (Paris: Michel Lévy, 1858–67)
- **URL:** Gutenberg clean texts — t.1 `https://m.gutenberg.org/ebooks/14791.html.images`,
  t.2 `https://m.gutenberg.org/ebooks/15312.html.images`,
  t.3 `http://www.gutenberg.org/cache/epub/15433/pg15433.html`;
  archive.org scans — t.5 `https://archive.org/download/memoirespourser05fragoog/memoirespourser05fragoog_text.pdf`,
  t.9 txt `https://archive.org/stream/memoirespourser09fragoog/memoirespourser09fragoog_djvu.txt`;
  t.6 PDF (Brazilian gov digital library) `https://bibliotecadigital.mj.gov.br/bitstream/1/11041/4/M%c3%a9moires%20pour%20servir%20%c3%a0%20l%27histoire%20de%20mon%20temps%20v6.pdf`
  — contains Guizot's actual Nov-1841 foreign-minister despatches (e.g. to Salvandy, Madrid).
- **Access:** free, clean OCR (Gutenberg) + scans.
- **Contains:** Guizot was French foreign minister **Oct 1840–Feb 1848** — vols 5–6 cover
  the despatch's exact window and print his *instructions and despatches verbatim* with
  full period formulae ("Monsieur le comte, …", "Je suis, etc., etc.....").
  The single best French-register formulae source for a Jan-1841 despatch.
- **Language:** French. **Rights:** public domain.
- **Priority: P0** — t.5–6 are the prize.

### 16. Talleyrand: *Mémoires du prince de Talleyrand* (Calmann Lévy, 1891–92), 5 vols.
- **URL:** archive.org v.1 `https://archive.org/details/talleyrand-perigord-memoires-du-prince-de-talleyrand-v-1&playlist=1?view=theater&ui=embed&wrapper=false`
  (French OCR, PD Mark 1.0).
- **Contains:** the master of the French diplomatic despatch; earlier period but the
  *form* of the French diplomatic letter.
- **Language:** French. **Rights:** public domain.
- **Priority: P1.**

### 17. *British and Foreign State Papers*, vol. 29 (1840/41)
- **URL:** HathiTrust full view (Univ. of Michigan): `https://catalog.hathitrust.org/Record/000543381`;
  serial index `https://onlinebooks.library.upenn.edu/webbin/serial?id=britfornstatpap`.
- **Contains:** the year's treaties, protocols, and diplomatic documents — **in French
  original** (e.g. the July 1840 London Treaty instruments, the 1841 Straits negotiations).
  Set-phrase vocabulary: *Sa Majesté Impériale, plénipotentiaires, convention, protocole…*
- **Language:** French + English. **Rights:** public domain.
- **Priority: P1.**

### 18. *Correspondence relative to the Affairs of the Levant, 1841: Part III* (British parliamentary paper)
- **URL:** `https://archive.org/download/correspondence-relative-to-the-affairs-of-the-levant_1841_part-3/correspondence-relative-to-the-affairs-of-the-levant_1841_part-3.pdf`
- **Access:** direct PDF, free.
- **Contains:** actual **Jan–Feb 1841** despatches (Bridgeman, Jaffa, 19 Feb 1841 on the
  Egyptian evacuation of Syria) — exactly what Zeschau was reading about that week.
- **Language:** English. **Rights:** public domain.
- **Priority: P1** (topics/names → cribs; not French register).

### 19. Foreign Office Confidential Print: *Eastern Affairs 1812–1946*, Part IV (July 1841)
- **URL:** full text `http://archive.org/stream/eastern-affairs/FO%2B406_6_djvu.txt`
  (PDF `https://archive.org/download/eastern-affairs/FO+406_6_text.pdf`).
- **Contains:** **April–July 1841** Levant despatches (Metternich's views, Ponsonby,
  the Straits Convention run-up).
- **Language:** English. **Rights:** public domain.
- **Priority: P1.**

### 20. Cargill, William: *The Foreign Affairs of Great Britain administered by … Viscount Palmerston* (London, 1841)
- **URL:** `https://archive.org/details/foreignaffairsof01carg`
- **Contains:** a contemporary (1841!) English summary of the diplomatic landscape —
  fast topic briefing for crib generation.
- **Language:** English. **Rights:** public domain.
- **Priority: P2.**

### 21. guizot.com — François Guizot portal (modern)
- **URL:** `https://www.guizot.com/wp-content/uploads/wp-post-to-pdf-cache/1/accueil.pdf`
- **Contains:** biography + pointers to the correspondence; not a corpus itself.
- **Priority: P2** — route marker only.

---
## Context/method sources (not corpora)

### 22. "Metternich and the Syrian Question: 1840–1841" (*Austrian History Yearbook*, Cambridge)
- **URL:** `https://www.cambridge.org/core/journals/austrian-history-yearbook/article/metternich-and-the-syrian-question-18401841/5D274BE9A84B217961C101906C93F65B`
- **Contains:** footnotes pinning exact Jan–Feb 1841 despatches (Metternich→Stürmer,
  Metternich→Apponyi 26 Jan 1841, Sainte-Aulaire→Guizot 23/27 Jan 1841…) with archive
  signatures — a dated topic map of what every chancellery was writing that month.
- **Priority: P1** (topic map for crib selection).

### 23. *France and the Levant*, ch. 6 (Wikisource, English)
- **URL:** `https://en.wikisource.org/wiki/France_and_the_Levant/Chapter_6`
- **Contains:** free narrative of the 1840–41 crisis sequence — fast briefing.
- **Priority: P2.**

### 24. Wikipedia: `https://en.wikipedia.org/wiki/1841`, `https://fr.wikipedia.org/wiki/Charles_Robert_de_Nesselrode`, `https://de.wikipedia.org/wiki/Heinrich_Anton_von_Zeschau`, `https://de.wikipedia.org/wiki/Albin_Leo_von_Seebach`
- Fast fact-checking only (dates, offices, family). Not corpus material.
- **Priority: P2.**

---
## What came up empty / caveats
- **Saxon foreign-ministry correspondence edition:** none found — no published
  *Politische Korrespondenz* of the Saxon Auswärtiges Ministerium 1835–48 surfaced.
  (Family 3 is the thinnest; Witzleben 1874 is the best substitute.)
- **NDB/ADB article for Albin Leo von Seebach:** none located; only Wikipedia +
  the Seebach family page. No published Seebach correspondence found.
- **Le Moniteur universel Jan 1841:** Gallica blocked per lane rules; Google Books API
  returned no usable full-view hit for the Jan-1841 *Moniteur*. ANNO + digiPress cover
  the newspaper need.
- **Nesselrode vols 7–8 (the 1835–45 years):** not on archive.org (only v.9 +
  one unidentified Google scan found via the archive.org API). Route: Google Books /
  HathiTrust full view — Harvester to attempt.
- **Witzleben 1874:** no confirmed full-view scan yet (DNB record only; Michigan copy
  indexed via CORE). One lookup round recommended, then park.
- **Sainte-Aulaire *Souvenirs* (1926):** HathiTrust "US access only" per UPenn index —
  likely inaccessible; kept as P2 with caveat.
- Copyright: nothing reproduced beyond brief fair-use quotes; all corpus targets are
  pre-1923 public domain.
