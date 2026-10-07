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
