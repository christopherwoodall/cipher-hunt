# corpus/ provenance — Seebach cipher lane, side-period harvest

Harvested 2026-10-07 (retrieval date for all files unless noted) by the
PERIOD-SOURCES Harvester; `nesselrode-v9.txt` staged earlier the same day by the
Bibliographer (entry kept verbatim below). Retrieval method: `curl` downloads to
disk; archive.org items fetched from
`https://archive.org/download/<item>/<item>_djvu.txt` (Internet Archive OCR of
the named scans) unless noted. All works are public domain (pre-1923
publication, no surviving copyright interest); see per-entry rights notes.
French unless noted.

## Family 1 — Nesselrode correspondence

- `nesselrode-v7.txt` — *Lettres et papiers du chancelier comte de Nesselrode,
  1760–1850*, vol. 7 (Paris: A. Lahure, 1904–1912 series; ed. Anatole de
  Nesselrode). Source URL:
  https://archive.org/download/lettresetpapiers07ness/lettresetpapiers07ness_djvu.txt
  (archive.org item `lettresetpapiers07ness`; 1904 Google digitization, Internet
  Archive OCR). Coverage ~1817–1831 (letter dates peak 1828–31). Rights: public
  domain (series published 1904–1912; author Karl Robert von Nesselrode d. 23 Mar
  1862; editor Anatole de Nesselrode d. 1924). 533,520 bytes.
- `nesselrode-v8.txt` — same series, vol. 8. Source URL:
  https://archive.org/download/lettresetpapiers08ness/lettresetpapiers08ness_djvu.txt
  (archive.org item `lettresetpapiers08ness`). **Coverage 1840–46 incl. the full
  1841 run — letters dated 1 Jan 1841 (Paris) through Dec 1841, incl.
  Saint-Pétersbourg despatches; the single highest-value corpus file for the
  18 Jan 1841 despatch.** Rights: public domain (as above). 627,848 bytes.
- `nesselrode-v9.txt` — *Lettres et papiers du chancelier comte de Nesselrode, 1760-1856*,
  vol. 9 (Paris: Lahure, 1904). Retrieved 2026-10-07 via curl from
  https://archive.org/download/lettresetpapiers09ness_0/lettresetpapiers09ness_0_djvu.txt
  (archive.org item `lettresetpapiers09ness_0`; UIUC 2021 scan, Internet Archive OCR).
  Coverage ~1847-1856 (1848 dominant). Public domain. Placed here as a head start for
  the Harvester; vols 7-8 (the 1835-45 years) still to locate — see ../sources.md.
- `nesselrode-v10.txt` — same series, vol. 10. Source URL:
  https://archive.org/download/lettresetpapiers10ness/lettresetpapiers10ness_djvu.txt
  (archive.org item `lettresetpapiers10ness`). Coverage ~1847–49. Rights: public
  domain (as above). 569,508 bytes.
- `pozzo-di-borgo-correspondance-v1.txt` — *Correspondance diplomatique du comte
  Pozzo di Borgo, ambassadeur de Russie en France, et du comte de Nesselrode,
  1814–1818*, vol. 1 (Paris: Calmann Lévy, 1890; ed. Charles Pozzo di Borgo).
  Source URL:
  https://archive.org/download/correspondancedi01pozz/correspondancedi01pozz_djvu.txt
  (archive.org item `correspondancedi01pozz`; Google digitization, Internet
  Archive OCR). Earlier period (1814–16 letter dates) but the same chancellery
  French register. Rights: public domain (published 1890). 1,029,046 bytes.

## Family 2 — January 1841 newspapers

- `allgemeine-zeitung-augsburg-1841-01-DD.txt` (one file per issue) — *Allgemeine
  Zeitung* (Augsburg), January 1841 issues, via digiPress (Bayerische
  Staatsbibliothek). Per-issue pages OCR'd by BSB and harvested from the BSB
  IIIF OCR endpoint `https://api.digitale-sammlungen.de/ocr/bsb10504343/<page>`
  (hOCR → plain text, line-preserving) driven by issue manifests at
  `https://digipress.digitale-sammlungen.de/calendar/1841/1/<DD>/newspaper/bsbmult00000002`.
  Harvest script: `../bin/digipress_harvest.py`. Issues harvested: **15, one per
  day 11–25 Jan 1841** (see `harvest-log.txt` for per-issue BSB identifiers),
  incl. the 18 Jan issue of the despatch's date (verified masthead
  "Allgemeine Zeitung. Mit allerhöchsten Privilegien. 18 Januar 1841.").
  16 pages/issue, 1,854,741 bytes total. Rights: public domain (published 1841).
  German, Fraktur OCR (noisy but usable for names/places/vocabulary).
- ANNO (*Wiener Zeitung*, Jan 1841) was **not** harvested: anno.onb.ac.at's
  `cgi-content` reader endpoints sit behind a Cloudflare Turnstile
  human-verification wall (verified 2026-10-07; homepage/calendar pages still
  serve, but page content requires an interactive JS challenge). ZEFYS
  (zefys.staatsbibliothek-berlin.de) was unreachable from this VM (empty reply
  to TCP). digiPress/Allgemeine Zeitung above is the substitute German-daily
  coverage.

## Family 4/5 — French diplomatic register

- `guizot-memoires-t5-t6.txt` — François Guizot, *Mémoires pour servir à
  l'histoire de mon temps*, t. 5–6 (Paris: Michel Lévy, 1858–67). Source URL:
  https://archive.org/download/mmoirespourser56guiz/mmoirespourser56guiz_djvu.txt
  (archive.org item `mmoirespourser56guiz`; Google digitization, Internet Archive
  OCR). Covers 1840–42 incl. Guizot's printed foreign-minister despatches and
  instructions (Oct 1840–) — the lane's best French formulae source for a
  Jan-1841 despatch. Rights: public domain (published 1858–67; Guizot d. 1874).
  2,043,767 bytes.
- `guizot-memoires-t1-gutenberg.txt` — François Guizot, *Mémoires pour servir à
  l'histoire de mon temps*, t. 1 (Paris: Michel Lévy, 1858), Project Gutenberg
  eBook #14791 (clean transcription). Source URL:
  https://www.gutenberg.org/cache/epub/14791/pg14791.txt. Rights: public
  domain (Gutenberg license: pre-1923 work). 805,355 bytes.
- `guizot-memoires-t2-gutenberg.txt` — same, t. 2 (1859), Gutenberg #15312.
  Source URL: https://www.gutenberg.org/cache/epub/15312/pg15312.txt.
  Rights: public domain. 869,256 bytes.
- `guizot-memoires-t3-gutenberg.txt` — same, t. 3 (1860), Gutenberg #15433.
  Source URL: https://www.gutenberg.org/cache/epub/15433/pg15433.txt.
  Rights: public domain. 892,268 bytes.
- `metternich-papiere-v4.txt` — *Aus Metternich's nachgelassenen Papieren*,
  hrsg. von Richard Metternich-Winneburg, vol. 4 (Wien: Braumüller, 1880–84).
  Source URL:
  https://archive.org/download/ausmetternichsna04mettuoft/ausmetternichsna04mettuoft_djvu.txt
  (archive.org item `ausmetternichsna04mettuoft`; UofT digitization, Internet
  Archive OCR). Coverage ~1823–28 despatches. Rights: public domain (published
  1880–84; Metternich d. 1859). 1,511,320 bytes. German.
- `metternich-papiere-v6.txt` — same series, vol. 6. Source URL:
  https://archive.org/download/ausmetternichsna06mettuoft/ausmetternichsna06mettuoft_djvu.txt
  (archive.org item `ausmetternichsna06mettuoft`). Coverage 1835–43 (letter
  dates peak 1840; 1841 material present). Rights: public domain. 1,755,063
  bytes. German.
- `talleyrand-memoires-v1.txt` — *Mémoires du prince de Talleyrand* (Paris:
  Calmann Lévy, 1891), vol. 1. Source URL:
  https://archive.org/download/talleyrand-perigord-memoires-du-prince-de-talleyrand-v-1/Talleyrand-Perigord%20Memoires%20du%20prince%20de%20Talleyrand%20v%201_djvu.txt
  (archive.org item `talleyrand-perigord-memoires-du-prince-de-talleyrand-v-1`).
  Earlier period but the classic form of the French diplomatic letter. Rights:
  public domain (published 1891; Talleyrand d. 1838). 954,364 bytes.

## 1841 periodicals

- `revue-deux-mondes-1841-q1.txt` — *Revue des deux mondes*, 4e série, t. XXV
  (Paris, janvier 1841 — imprint per title page "Imprimerie de H. Fournier et
  Cie", OCR reads "II. FOURMER"). Source URL:
  https://archive.org/download/revuedesdeuxmond011841pari/revuedesdeuxmond011841pari_djvu.txt
  (archive.org item `revuedesdeuxmond011841pari`; Tufts College Library 1901
  stamp; Google digitization, Internet Archive OCR). Rights: public domain
  (published 1841). 3,087,127 bytes.
- `revue-deux-mondes-1841-q2.txt` — same, t. XXVI (avril 1841). Source URL:
  https://archive.org/download/revuedesdeuxmond021841pari/revuedesdeuxmond021841pari_djvu.txt
  (archive.org item `revuedesdeuxmond021841pari`). Rights: public domain.
  3,037,263 bytes.
- `revue-deux-mondes-1841-q3.txt` — same, t. XXVII (juillet 1841). Source URL:
  https://archive.org/download/revuedesdeuxmond031841pari/revuedesdeuxmond031841pari_djvu.txt
  (archive.org item `revuedesdeuxmond031841pari`). Rights: public domain.
  3,129,322 bytes.
- `revue-deux-mondes-1841-q4.txt` — same, t. XXVIII (octobre 1841). Source URL:
  https://archive.org/download/revuedesdeuxmond041841pari/revuedesdeuxmond041841pari_djvu.txt
  (archive.org item `revuedesdeuxmond041841pari`). Rights: public domain.
  3,244,434 bytes.

## Context

- `adb-zeschau-heinrich-anton-von.txt` — Allgemeine Deutsche Biographie, vol. 45
  (Leipzig: Duncker & Humblot, 1900), pp. 105–108: "Zeschau, Heinrich Anton von"
  (Th. Flathe). Retrieved 2026-10-07 via the de.wikisource.org MediaWiki API
  (`action=query&prop=revisions&rvprop=content`; wikitext stripped of templates
  and links). Source URL: https://de.wikisource.org/wiki/ADB:Zeschau,_Heinrich_Anton_von.
  Rights: public domain (published 1900; Flathe d. 1895). German. 11,637 bytes.
- `levant-correspondence-1841-p3.txt` — *Correspondence relative to the Affairs
  of the Levant, 1841: Part III* (London: T. R. Harrison, 1841; British
  parliamentary paper presented to both Houses by Command of Her Majesty).
  Source URL:
  https://archive.org/download/correspondence-relative-to-the-affairs-of-the-levant_1841_part-3/correspondence-relative-to-the-affairs-of-the-levant_1841_part-3_djvu.txt
  (archive.org item `correspondence-relative-to-the-affairs-of-the-levant_1841_part-3`;
  Internet Archive 2026 scan, Internet Archive OCR). Actual Jan–Feb 1841
  despatches on the Eastern Question (topics/names, not French register).
  Rights: public domain (UK parliamentary paper, 1841). English. 1,714,311
  bytes.

## Corpus totals

- Book/periodical files: 18 (Nesselrode ×4, Pozzo ×1, Guizot t5–6 + Gutenberg
  t1–t3, Metternich ×2, Talleyrand v1, RDM 1841 ×4, ADB Zeschau, Levant corr.)
  = **26.3 MB**.
- Newspaper issues: 15 *Allgemeine Zeitung* (Augsburg) issues, 11–25 Jan 1841,
  ≈1.85 MB (see `harvest-log.txt`).
- **Corpus total: 28.2 MB across 33 text files** (books/context 26.3 MB +
  newspapers 1.85 MB).

## Family 9 — 19th-century French DRAMA (harvested 2026-10-09)

Ingested 2026-10-09 by the battery worker `disloc-demonstrative-drama-ingest`
to make the drama-register bars of the disloc-demonstrative battery chain
testable. Retrieval method: `curl -sSL` downloads (follows archive.org's
redirect to the dn*.archive.org host — plain `curl` returns zero bytes)
to `code/side-period/corpus/`. Retrieval time 2026-10-09 ~08:30 UTC for all
files. All works public domain (19th-century editions listed; authors
d. Hugo 1885, Musset 1857, Dumas 1870, Vigny 1863). French drama.

- `hugo-hernani-1870.txt` — Victor Hugo, *Hernani, drame en cinq actes*
  (New York: William R. Jenkins, 1870 ed., with explanatory notes by Gustave
  Masson). Source URL:
  https://archive.org/download/hernanidrameenci00hugouoft/hernanidrameenci00hugouoft_djvu.txt
  (archive.org item `hernanidrameenci00hugouoft`; Internet Archive OCR).
  207,880 bytes. sha256:
  05a6b8f71d5812e28cff6b4f469637e4f32b215c431ec11dea77c0a587e0bac6
- `dumas-mariage-louis-xv-1841.txt` — Alexandre Dumas père, *Un mariage sous
  Louis XV, comédie en cinq actes* (Paris, 1841 ed. — contemporary with the
  R5005 letter). Source URL:
  https://archive.org/download/unmariagesouslou00duma/unmariagesouslou00duma_djvu.txt
  (archive.org item `unmariagesouslou00duma`; Internet Archive OCR).
  207,347 bytes. sha256:
  f51b724d73e997c59874ea092cb11c423e221d4460c4e4c1a949205e63b4dfcc
- `vigny-chatterton-1835.txt` — Alfred de Vigny, *Chatterton* (in *Oeuvres*,
  Bruxelles: Louis Hauman et comp., 1835). Source URL:
  https://archive.org/download/chatterton00vignuoft/chatterton00vignuoft_djvu.txt
  (archive.org item `chatterton00vignuoft`; Internet Archive OCR).
  192,684 bytes. sha256:
  277dd951ac8c9ff49d405ab37a436c64ccb13b1a356357130ba608ac851c046a
- `musset-comedies-proverbes-1850.txt` — Alfred de Musset, *Comédies et
  proverbes* (Poitiers: A. Dupré, 1850 ed.; contains André del Sarto,
  Lorenzaccio, Les Caprices de Marianne, Fantasio, On ne badine pas avec
  l'amour, La Nuit vénitienne, La Quenouille de Barberine, Le Chandelier,
  Il ne faut jurer de rien, Un Caprice). Source URL:
  https://archive.org/download/comdiesetpro00muss/comdiesetpro00muss_djvu.txt
  (archive.org item `comdiesetpro00muss`; Internet Archive OCR).
  990,193 bytes. sha256:
  fb6074c38356213443c5337bdf54ab9db14e955afb0b91ac3d5d1aa3423ca76a

Total new drama: 1,598,104 bytes (1,569,886 characters by Python count).

## Family — 19th-century French drama, wikisource ingest (2026-10-09)

Ingested 2026-10-09 by the corpus-ingest commission
(`disloc-demonstrative-drama-ingest` follow-up #1 of battery
`disloc-demonstrative-drama`) to complete the drama register for the
dislocated-demonstrative census. Retrieval method: `curl -sL` against the
fr.wikisource MediaWiki parse API
(`https://fr.wikisource.org/w/api.php?action=parse&page=<title>&prop=text&redirects=1&format=json&formatversion=2`;
transclusions expanded server-side), HTML stripped to plain UTF-8 text,
wikisource header-nav chrome trimmed. Retrieval window 2026-10-09
~08:20–08:45 UTC for all files. Raw API JSON kept in the goal workspace
(`goals/cipher-hunt-cracking-lanes/hidden_files/drama-ingest/`). All works
public domain (authors d.: Victor Hugo 1885, Alexandre Dumas père 1870,
Eugène Scribe 1861, Eugène Labiche 1888, Marc-Michel 1887,
Édouard Martin 1866). French drama throughout.

- `hugo-hernani.txt` — Victor Hugo, *Hernani* (drame, 1830), éd. Hetzel 1889.
  Source page: https://fr.wikisource.org/wiki/Hernani_(Hetzel,_1889)/Texte_entier
  (full text). 182,092 bytes. sha256:
  63b22c5c5edfc632debbe5949ae9032b220bb836fc60c2f8fe67fabcdcaa1a95
  NOTE: second edition of Hernani in this dir — `hugo-hernani-1870.txt`
  (Jenkins 1870 ed., archive.org OCR) already present. Census runs should
  use ONE edition per play to avoid double-counting.
- `hugo-ruy-blas.txt` — Victor Hugo, *Ruy Blas* (drame, 1838), édition 1839
  (Société Belge de librairie). Source pages:
  https://fr.wikisource.org/wiki/Ruy_Blas/Préface,
  /Personnages, /Acte_1 … /Acte_5 (the top-level "Ruy Blas" page renders
  only the sommaire, so acts fetched individually). 208,673 bytes. sha256:
  a4c467c746ed65a6bb3ccdb79e41558c75d32ef74e41d9701145b92ae6704a56
- `hugo-burgraves.txt` — Victor Hugo, *Les Burgraves* (drame, 1843),
  Œuvres complètes Impr. nat., Théâtre t. III. Source page:
  https://fr.wikisource.org/wiki/Les_Burgraves (full text). 155,722 bytes.
  sha256:
  2f44125d708ce5e8216ef54c5c667707322a4aa37e3728b7135d4f54f9d3fca0
- `dumas-antony.txt` — Alexandre Dumas père, *Antony* (drame, 1831),
  Œuvres 1838 vol. 2 (Meline, Cans et cie, Bruxelles). Source pages:
  https://fr.wikisource.org/wiki/Antony + /Acte_I … /Acte_V.
  109,308 bytes. sha256:
  eb2fb304799e451c35d3946692a3bae864a5d8a3afd90dfc3e9ca7bf4eed4865
- `dumas-tour-de-nesle.txt` — Alexandre Dumas père (with Frédéric
  Gaillardet), *La Tour de Nesle* (drame, 1832), Œuvres 1838 vol. 2.
  Source pages: https://fr.wikisource.org/wiki/La_Tour_de_Nesle_(Dumas)/Personnages
  + /Acte_I … /Acte_V (top-level page is a title page only, excluded).
  138,666 bytes. sha256:
  1f583b70ee88d1b807874546077f6c233ab523a4e6dd768aa71e6ae5bf486753
- `dumas-henri-iii.txt` — Alexandre Dumas père, *Henri III et sa cour*
  (drame, 1829), Œuvres 1838 vol. 2. Source pages:
  https://fr.wikisource.org/wiki/Henri_III_et_sa_cour/Personnages
  + /Acte_I … /Acte_V (top-level page is a title page only, excluded).
  136,064 bytes. sha256:
  64ddd49d10e0100bdb46c9b081bec784d2f72532dea6f662f86da1f03c0afc86
- `dumas-kean.txt` — Alexandre Dumas père, *Kean* (drame, 1836),
  Œuvres 1838 vol. 2. Source pages:
  https://fr.wikisource.org/wiki/Kean_(Dumas)/Acte_I … /Acte_V
  (top-level page is a title page only, excluded). 160,337 bytes. sha256:
  54e433311f5990a271e204b633d150908a1969c3f3b8ebed8d5a7b0bceb1b4da
- `scribe-bertrand-et-raton.txt` — Eugène Scribe, *Bertrand et Raton, ou
  l'Art de conspirer* (comédie, 1833), éd. 1835 (Théâtre, 15). Source page:
  https://fr.wikisource.org/wiki/Bertrand_et_Raton,_ou_l’Art_de_conspirer
  (full text). 192,218 bytes. sha256:
  9cccc55f2b68e130249e6c3d04100b2229a34eb68b7624630efd5189e3ed8cab
- `scribe-verre-d-eau.txt` — Eugène Scribe, *Le Verre d'eau, ou les Effets
  et les Causes* (comédie, 1840), éd. 1861 (from the 1860 djvu). Source page:
  https://fr.wikisource.org/wiki/Le_Verre_d’eau_(1861) (full text).
  156,592 bytes. sha256:
  1ded328072f42eb5eeddcef9ee17a85e35b2907d372d5889ef84dbaafa66587c
  SUBSTITUTION: the éd. 1841 full-text subpage ("Le Verre d’eau ou les
  Effets et les Causes", Scribe - Théâtre, 22.djvu) does not exist on
  fr.wikisource (API `missingtitle`); the 1861 edition was used instead.
- `labiche-chapeau-de-paille.txt` — Eugène Labiche & Marc-Michel,
  *Un chapeau de paille d'Italie* (comédie-vaudeville, 1851), Théâtre
  complet Calmann-Lévy 1898 vol. 1. Source page:
  https://fr.wikisource.org/wiki/Un_chapeau_de_paille_d’Italie (full text).
  126,750 bytes. sha256:
  5748dd9e0d5b946756eee02b971409adcebb7deb8704f6999e2bcabff0ad84fe
- `labiche-martin-poudre-aux-yeux.txt` — Eugène Labiche & Édouard Martin,
  *La Poudre aux yeux* (comédie, 1861), Théâtre complet Calmann-Lévy 1898
  vol. 2. Source page: https://fr.wikisource.org/wiki/La_Poudre_aux_yeux
  (full text). 92,386 bytes. sha256:
  da5000a14f04499c48509ce2c44a96dc02ad16681a1ab5a37f869118f9df6da1

Total wikisource drama ingest: 1,658,808 bytes (1,573,255 characters by
Python count) across 11 files. Combined with the archive.org drama family
above, the lane now holds 15 French drama files (14 distinct plays —
Hernani in two editions).

## Family — Scribe/Labiche comedy extension (fr.wikisource ingest, 2026-10-09)

Ingested 2026-10-09 by the battery worker `disloc-reinforced-comedy-extension`
(follow-up #3 of `disloc-demonstrative-drama-reinforced`, null 2026-10-09) to
close the comedy-register gap: the parent battery found Scribe contributed the
only infinitive-rich near-misses, and the ingested corpus held only Scribe ×2 /
Labiche ×2. Retrieval method: same as the drama wikisource ingest —
`curl -sSL` against the fr.wikisource MediaWiki parse API
(`https://fr.wikisource.org/w/api.php?action=parse&page=<title>&prop=text&redirects=1&format=json&formatversion=2`;
transclusions expanded server-side), HTML stripped to plain UTF-8 text
(script/style/catlinks/printfooter/jump-link elements removed), whitespace
collapsed, header-nav chrome trimmed. Retrieval 2026-10-09 08:48 UTC
(retrieval time for all files). Raw API JSON kept in the goal workspace
(`goals/cipher-hunt-cracking-lanes/hidden_files/comedy-extension-ingest/`).
User-Agent: `cipher-hunt-lane/1.0 (research corpus ingest)`. All works public
domain (authors d.: Eugène Scribe 1861, Eugène Labiche 1888; co-authors
Édouard Martin 1866, Alfred Delacour d. 1890, Albert Monnier d. 1869). French
comedy/vaudeville throughout.

- `scribe-le-savant.txt` — Eugène Scribe, *Le Savant, comédie en cinq actes*
  (1832), Aimé André éd., 1835 (Théâtre complet, t. XII, p. 266–362).
  Source page: https://fr.wikisource.org/wiki/Le_Savant_(Scribe) (full text).
  88,948 characters. sha256:
  6c2cc8275073be23169271463dd92a778cc753ef5cec47cf0168fb64876456d6
- `scribe-le-lorgnon.txt` — Eugène Scribe, *Le Lorgnon, comédie en deux
  actes* (1833), Aimé André éd., 1835 (Théâtre complet, t. XIII, p. 384–460).
  Source page: https://fr.wikisource.org/wiki/Le_Lorgnon_(Scribe) (full text).
  67,027 characters. sha256:
  206a5990c24f651451e363872a08125ca5a7d4cf12d26d82c32b9cb849bb0985
- `labiche-voyage-perrichon.txt` — Eugène Labiche & Édouard Martin,
  *Le Voyage de monsieur Perrichon, comédie en quatre actes* (1860),
  Calmann-Lévy, Théâtre complet t. 2 (1898, p. 1–121).
  Source page: https://fr.wikisource.org/wiki/Le_Voyage_de_monsieur_Perrichon
  (full text). 97,394 characters. sha256:
  6fb829c40d71ac952f77b0f2781cbf6d52e2005335cf81b44aa4aa86b4a6c923
- `labiche-la-cagnotte.txt` — Eugène Labiche & Alfred Delacour,
  *La Cagnotte, comédie-vaudeville en cinq actes* (1864), Calmann-Lévy,
  Théâtre complet t. 5 (1898, p. 1–170).
  Source page: https://fr.wikisource.org/wiki/La_Cagnotte (full text).
  134,352 characters. sha256:
  83b99bb3ac5e0ec8632aea2ca58534f35f845a0d5a4ecf23e5d2781353e3f579
- `labiche-29-degres-ombre.txt` — Eugène Labiche,
  *29 degrés à l'ombre, comédie en un acte* (1873), Calmann-Lévy,
  Théâtre complet t. 7 (1898, p. 173–215).
  Source page: https://fr.wikisource.org/wiki/29_degr%C3%A9s_%C3%A0_l%27ombre
  (full text). 34,633 characters. sha256:
  a6cdfbc11cf01251283101d2f24e3243241f6a30f220c9cee260ddfdf010b3b0
- `labiche-affaire-rue-lourcine.txt` — Eugène Labiche, Albert Monnier &
  Édouard Martin, *L'Affaire de la rue de Lourcine, comédie en un acte*
  (1857), Calmann-Lévy, Théâtre complet t. I (1898, p. 431–487).
  Source page: https://fr.wikisource.org/wiki/L%27Affaire_de_la_rue_de_Lourcine
  (full text). 43,171 characters. sha256:
  a6c298132d76d5e73061dc638083221eb65ed9db7fca5d49078c709e0c9fe2ec

## Family — Scribe/Labiche comedy WIDER corpus (fr.wikisource ingest, 2026-10-09)

Ingested 2026-10-09 ~08:52 UTC by the battery worker
`disloc-reinforced-comedy-widercorpus` (follow-up #1 of
`disloc-reinforced-comedy-recall`, null 2026-10-09) to harden the
comedy-register fence: the recall battery's suggested bar was "0 genuine in
≥1M added chars confirms". 565,307 chars added (8 full-text comedies).
Retrieval method: `curl -sSL` against the fr.wikisource MediaWiki parse API
(`https://fr.wikisource.org/w/api.php?action=parse&page=<title>&prop=text&redirects=1&format=json&formatversion=2`;
transclusions expanded server-side), HTML stripped to plain UTF-8 text
(script/style elements, catlinks/printfooter chrome removed), whitespace
collapsed. Retrieval 2026-10-09 ~08:52 UTC. Raw API JSON kept in
`code/crowd17/next-token/widercomedy-ingest-raw/`. User-Agent:
`cipher-hunt-lane/1.0 (research corpus ingest)`. All works published pre-1923
(played/published 1825–1872), public domain.

- `scribe-charlatanisme.txt` — Eugène Scribe, *Le Charlatanisme* (1825),
  Théâtre complet. Source page: https://fr.wikisource.org/wiki/Le_Charlatanisme
  (full text). 60,202 characters. sha256:
  64cdd6c2b0773a023fc5a43587a11ae4fe6cbd5db9ecdeedb223be0bffe857a6
- `labiche-misanthrope-auvergnat.txt` — Eugène Labiche, Lubize & Paul
  Siraudin, *Le Misanthrope et l'Auvergnat* (1852), Calmann-Lévy, Théâtre
  complet t. I (1898, p. 133–199). Source page:
  https://fr.wikisource.org/wiki/Le_Misanthrope_et_l%27Auvergnat (full text).
  56,991 characters. sha256:
  f25906b4dad1197ce25d42d428a99a5b2216b81af224b0b683e3db5c99d54642
- `labiche-main-leste.txt` — Eugène Labiche, *La Main leste*, Calmann-Lévy,
  Théâtre complet t. 7 (1898, p. 273–318). Source page:
  https://fr.wikisource.org/wiki/La_Main_leste (full text). 39,272 characters.
  sha256: c1334f3c62cadde5749a06535071d87014267642076effb21b000e4a62a8605c
- `labiche-edgard-bonne.txt` — Eugène Labiche & Marc-Michel,
  *Edgard et sa bonne* (1852), Calmann-Lévy, Théâtre complet t. I (1898,
  p. 201–264). Source page:
  https://fr.wikisource.org/wiki/Edgard_et_sa_bonne (full text). 57,212
  characters. sha256:
  e33a790252d0aecc21e8979ef2e04556797eea21503a7654c2853fa4859ee9b9
- `labiche-prix-martin.txt` — Eugène Labiche & Émile Augier, *Le Prix Martin*
  (1876), Calmann-Lévy, Théâtre complet t. 10 (1898, p. 1–121). Source page:
  https://fr.wikisource.org/wiki/Le_Prix_Martin (full text). 103,002
  characters. sha256:
  f6a79a643933f4785c7f0fce0820da50bf9afa9c3c02b92f1ddd20f8bed4ab81
- `labiche-noces-bouchencoeur.txt` — Eugène Labiche, *Les Noces de
  Bouchencœur* (1857). Source page:
  https://fr.wikisource.org/wiki/Les_Noces_de_Bouchenc%C5%93ur (full text).
  80,053 characters. sha256:
  6a3c866c62500817c5e4917063345eb09d6b304cd51bfc7ce5b5cf3dd6592258
- `labiche-baron-fourchevif.txt` — Eugène Labiche & Alphonse Jolly,
  *Le Baron de Fourchevif* (1859). Source page:
  https://fr.wikisource.org/wiki/Le_Baron_de_Fourchevif (full text). 54,412
  characters. sha256:
  25c94e9813afae945b2d76d8c30584adbdb38296c883920d0f1fba4cf1c8aa39
- `labiche-doit-on-le-dire.txt` — Eugène Labiche & Alfred Duru,
  *Doit-on le dire ?* (1872), Calmann-Lévy, Théâtre complet. Source page:
  https://fr.wikisource.org/wiki/Doit-on_le_dire_%3F (full text). 114,163
  characters. sha256:
  96ea69eae6160d9b6aeaf06a3267167154262a3e673cbd09fe35911e731eec4a
