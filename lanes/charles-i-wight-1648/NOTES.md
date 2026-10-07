# Living notes — Charles I, Isle of Wight captivity letters, 1648

## Objective
Determine whether the published 2021 nomenclator (solved pair) breaks the two unsolved 1648 Isle of Wight letters; a clean, evidenced negative is the success criterion.
Phase 2 (2026-10-07): derive the OTHER nomenclator (the one the 1 Aug / 22 May letters actually use) from the 200 cipher tokens + cleartext context — outcome so far: documented negative (N5-N7).

## Methodology log
- 2026-10-07 04:19Z — Web research: found S. Tomokiyo's solution article
  "What It Takes to Break Charles I's Cipher Used in the Isle of Wight"
  (https://cryptiana.web.fc2.com/code/charlesi2.htm, first posted 25 Apr 2021,
  modified 6 May 2021). It states the cipher of two of the four letters was
  broken by Norbert Biermann and Matthew Brown, with final results published in
  Cipherbrain on 5 May 2021. Fetched via curl+iconv (SHIFT_JIS->UTF-8).
- 2026-10-07 04:20Z — Fetched transcriptions page
  https://cryptiana.web.fc2.com/code/charlesii.htm#SEC1 (section 4 "From the
  Isle of Wight (1648)"). Identified the four letters: (1) to Worsley ("Z"),
  22 May 1648, from History of the Isle of Wight (1795) p.237; (2) to Prince
  Charles, 1 Aug 1648, from Original Letters (Harley MS 6988, f.208);
  (3) to Prince Charles, 3 Oct 1648, from Vindication (SOLVED);
  (4) to Prince Charles, 7 Nov 1648, from Original Letters (SOLVED).
  Extracted verbatim transcriptions of the two unsolved letters.
- 2026-10-07 04:21Z — Fetched final Cipherbrain solution article
  (https://scienceblogs.de/klausis-krypto-kolumne/2021/05/05/geloest-die-verschluesselten-briefe-von-karl-i-an-seinen-sohn/).
  Correction to triage: FOUR letters solved (2 Sep, 3 Oct, 6 Nov, 7 Nov 1648;
  solvers: Norbert Biermann, Thomas Bosbach, Matthew Brown), TWO unsolved
  (1 Aug 1648 to son, 22 May 1648 to Worsley) — "wurden dagegen mit einem
  anderen Nomenklator verfasst und bleiben daher vorlaeufig ungeloest".
  Triage's "two of four solved" was Tomokiyo's pre-April-2021 count.
- 2026-10-07 04:26Z — Downloaded published nomenclator image
  (Nomenclator-Charles-I.png, 1200x919) and BL manuscript image of the
  1 Aug 1648 letter (Charles-Letter-1648-08-01.png, 900x814, source: BL
  Harley MS 6988). Verified the 1 Aug transcription token-by-token against
  the manuscript image: all 88 cipher tokens match in order.
- 2026-10-07 04:27Z — Transcribed the nomenclator image by hand into
  data/nomenclator-charles-i-1648-solved-key.json: letter section 1-90
  (homophonic, 24 letters: i/j and u/v merged; s has 5 homophones
  30/40/51/61/71), nulls {1,10,58,68,69,78,100-107} (+uncertain '9x'),
  word section 142-615 roughly alphabetical with green/yellow/red
  confidence flags (142=Argyll? red ... 615=you green).
- 2026-10-07 04:30-04:36Z — DECODE database (de-crypt.org) advanced search:
  sender=Charles -> 16 records, none 1648/England; holder='Harley MS 6988'
  -> 4 records: R8342 (f.208, 1648, Non-decrypted), R8343 (f.209, 1648,
  Decrypted), R8340/R8341 (Oxford 1646). R8342's "Partial Transcription"
  file downloads as a blank/corrupt 986x568 PNG (DECODE-side data issue).
  Sender=Worsley -> 0 records. Conclusion: DECODE covers the 1 Aug letter
  (R8342) but holds no usable transcription; the Worsley letter is absent.
  Used the published transcriptions as the ciphertext source instead.
- 2026-10-07 04:38Z — Wrote code/apply.py, ran it (exit 0). Results saved
  to code/apply-output.txt (79 lines). See Findings/Null results below.
- 2026-10-07 ~05:00Z — Work order (a): wrote code/derive.py (whitespace-run
  cipher-group parser: numbers separated only by whitespace form one group,
  so line-wrapped blocks parse correctly; verified token order matches the
  raw files: aug1648 = 1 group of 88, worsley = 6 groups 29/9/23/43/6/2,
  200 tokens total). Frequency tables per letter + combined and the crib
  table (every group with adjacent cleartext) written to
  data/freq-analysis.txt. Parser bug found and fixed mid-run (first version
  split groups on line breaks and swallowed mid-line group heads into
  cleartext — caught by the token-count check 85/89 vs 88/112).
  Calibration: the known-key solved 3 Oct control (67 tokens) shows
  61.2% low-block / 35.8% word-zone vs 54.5%/40.5% for the unknown letters —
  same bipartite split, suggesting the unknown nomenclator shares the
  ARCHITECTURE (homophonic low letter block + high word-code section) with
  different assignments (hypothesis only; N3 stands). 20 tokens shared
  between the two letters; only repeated bigram is "230 388" x2 in Worsley
  (parallel contexts g1 "...3 230 388 45 36" / g4 "...2 230 388 46 36").
- 2026-10-07 ~05:20Z — Work order (b): wrote code/cribs.py, the systematic
  crib battery ("clear text left by partial encoding"). First version had a
  methodology flaw (same-group competing candidates marked CONTRADICTED
  against whichever ran first); rewrote to two-phase: independent
  frequency-plausibility per variant, then pairwise cross-group
  compatibility. Results in data/crib-attempts.txt; see N5/N6.
- 2026-10-07 ~05:30Z — Work order (c): 3-strike fetch for the Worsley
  letter's source text (History of the Isle of Wight (1795) p.237) via
  Internet Archive; all three strikes failed — see N7. Not fabricated;
  recorded as null.
- 2026-10-07 05:20-05:40Z — Work order "recover p.122-123, hunt the 5 May
  letter": full-text hunt across KB SRU (0 records), Delpher (JS-rendered,
  no server-side results), ECCO via quod.lib.umich.edu (HTTP 403),
  Text Creation Partnership GitHub org (0 repos), Oxford Text Archive
  (timeout), Open Library (no scan), Google Books other 1781 copies
  (aoqlnQEACAAJ = 1975 EP reprint, lB44AQAAMAAJ = 2018 Gale reprint no
  preview — NO second 1781 scan exists on GB; PDF download
  CAPTCHA/429-blocked), HathiTrust catalog API (HTTP 403, single attempt
  per work order), Internet Archive retry (worsley AND "isle of wight" ->
  5 hits: Appuldurcombe catalogue, Museum Worsleyanum x2, 2 unrelated),
  web search for 1781 pdf/ebook (nothing). VERDICT: no openly accessible
  full text or page images of Worsley 1781 found (N10). Best obtainable
  remains GB OCR snippets: ran a second tiling pass (17 queries,
  2026-10-07 05:28-05:36Z) — sharpened Letter B opening + sign-off,
  recovered the cover note's continuation, confirmed Letter A head
  verbatim; narrative search of pp.117-127 for the 5 May letter = null
  (F8/N11). Raw responses consolidated in
  data/gb-tiling-2026-10-07.json.
- 2026-10-07 05:18-06:10Z — Work order (a)+(b)+(c), "find more material":
  (a) LOCATED Worsley's History of the Isle of Wight full text: Google
  Books id wOZWAAAAcAAJ ("The History of the Isle of Wight", Sir Richard
  Worsley, London: A. Hamilton, 1781; digitized from the National Library
  of the Netherlands copy, 18 Jun 2013;
  https://books.google.com/books?id=wOZWAAAAcAAJ). IA advancedsearch has
  NO copy (title+creator:worsley -> 0 hits; title-only 36 hits, none
  Worsley; creator "Worsley, Richard" -> only Museum Worsleyanum/trial
  pamphlets). HathiTrust catalog search -> HTTP 403 (single attempt per
  work order, no further attempts). Google Books page-image endpoint
  returns "image not available" (limited preview) and PDF/EPUB download
  is CAPTCHA-blocked (HTTP 429) — full-page text NOT retrievable; the
  SearchWithinVolume2 OCR-snippet API works and was used to tile p.122
  (~15 queries; raw JSON in /tmp/gb*.json, ephemeral). MAJOR CORRECTION:
  the 22 May letter is on p.122 of the 1781 first edition (ESTC T86489),
  NOT "(1795) p.237" — cryptiana's citation is wrong on both counts
  (no 1795 Worsley edition known; Warner's 1795 is a different work, N7).
  (b) DECODE R8340-R8345 fetched via RecordsView pages (curl, HTTP 200):
  R8340 = Harley MS 6988 f.193 (1646, to Glamorgan, Decrypted, graphic
  signs — different cipher); R8341 = f.194 (key, simple substitution);
  R8342 = f.208 (our 1 Aug letter, Non-decrypted); R8343 = f.209
  (Cairsbrook, Decrypted, 2pp — the solved 2 Sep 1648 letter); R8344/R8345
  = BL Add MS 32091 (unrelated). NO new 1648 items in the adjacent range.
  BL catalogue (searcharchives.bl.uk): Harley MS 6988 "Royal letters and
  warrants, 1625-1655" is marked digitised but the legacy Universal Viewer
  is UNAVAILABLE — neighboring folios f.206-210 not accessibly digitized.
  (c) cribs.py extended with Phase 3 (single-token semantic cribs from the
  new material), re-run exit 0: tallies unchanged (5 candidates /
  21 variants / 11 plausible / 10 implausible / 0 cross-group pairs);
  no convergence — see N8/N9, F6/F7.

- N10 (2026-10-07): Full-text / page-image hunt for Worsley 1781 = NULL.
  Search log (3-strike rule per route; all via curl unless noted):
  (1) KB jsru.kb.nl SRU (title="isle of wight" and creator=worsley) ->
  HTTP 200, 0 records (x2 attempts, index set wrong for old prints);
  (2) Delpher /nl/boeken/results (coll=boeken, boeken1, dts) -> HTTP 200
  but results are JS-rendered, no server-side data, no embedded JSON;
  (3) ECCO via quod.lib.umich.edu/e/ecco/ -> HTTP 403 (1 strike);
  (4) Text Creation Partnership GitHub org repo search (worsley isle
  wight) -> 0 repos, i.e. no TCP transcription;
  (5) Oxford Text Archive DSpace discover -> timed out, no file (1 strike);
  (6) Open Library works/OL7839279W -> 1 edition, no IA scan;
  (7) Google Books other copies: editions page lists aoqlnQEACAAJ,
  lB44AQAAMAAJ, y4UmtwEACAAJ — aoqlnQEACAAJ resolves to the 1975 EP
  Publishing reprint ("No eBook available"), lB44AQAAMAAJ to the 2018
  Gale Ecco reprint ("No preview available"); the page-image endpoint
  returns a 128x170 placeholder (sig invalid); PDF download endpoint ->
  HTTP 429 "unusual traffic" CAPTCHA page (x2 attempts after 90s wait).
  NO second 1781 scan exists on Google Books; wOZWAAAAcAAJ (KB copy,
  limited preview) is the only one;
  (8) HathiTrust catalog API -> HTTP 403 (the single allowed attempt,
  then stopped per work order);
  (9) Internet Archive advancedsearch retry (worsley AND "isle of wight")
  -> 5 hits: Appuldurcombe catalogue (1804), Museum Worsleyanum x2
  (gri_33125011848179, gri_33125009336864), 2 unrelated (the one allowed
  retry; route now dead);
  (10) web search for 1781 pdf/ebook/full text -> no full text, only
  references and reprint listings.
  CONCLUSION: no openly accessible full text or page images of Worsley
  1781 obtainable from this environment today; pp.122-123 verbatim
  extraction (work order (b)) is therefore NOT possible — the OCR-snippet
  reconstruction (data/letter-worsley-1648-southampton-cover-ocr.txt,
  explicitly not verbatim) remains the best obtainable text.
- N11 (2026-10-07): Narrative hunt for the ca. 5 May 1648 cipher letter
  in Worsley pp.117-127 = NULL. 17 snippet queries (run 2) covering the
  captivity narrative: "Hammond" -> pp.117-119, 124-127 (governor,
  chaplains, reading list, Derby-house letter — no cipher letters);
  "Carisbrooke" -> p.117; "the fifth" -> 10 hits, only p.122 relevant
  (the cover note itself); "May"/"escape" -> unrelated reigns and escape
  plots (pp.120-121, 124-131, 138-139); "Southampton" -> 10 hits, none on
  pp.118-122 relevant to the letters. No mention of the 5 May letter in
  the printed narrative; consistent with F8 (it was an enclosure, never
  printed). Caveat: snippet search surfaces ~10 results/query and OCR
  noise could hide a mention — a full-text grep remains the gold
  standard if a scan ever becomes available.
- N1 (2026-10-07): The published 2021 nomenclator does NOT decode the
  1 Aug 1648 letter. Evidence (code/apply-output.txt): 88 cipher tokens,
  only 46/88 (52.3%) defined in the key; the five most frequent tokens
  379(x4), 212(x4), 329(x3), 214(x3), 339(x3) are ALL undefined in the key;
  letter-section runs decode to non-English strings ("qh","ap","dh","de",
  "gmkfo","lx","crr","eh","ai","sweed","dl","ex") including impossible
  bigrams. The letter's word codes live in a different nomenclator.
- N2 (2026-10-07): The published 2021 nomenclator does NOT decode the
  22 May 1648 Worsley letter. Evidence (code/apply-output.txt): 112 cipher
  tokens, only 64/112 (57.1%) defined; top undefined tokens 86(x3), 248(x3),
  208(x2), 96(x2), 395(x2), 230(x2), 388(x2), 97(x2); the group
  "36 19 5 32 39 12 37 8 97" decodes to "o a e k r h p b [97]" = gibberish
  where clear context ("now it will be ___ I desyre you to enquyre")
  demands a word; token 97 lies outside every published section (letters
  1-90, nulls 100-107, words 142-615).
- N3 (2026-10-07): Crib test — maximal runs of tokens in the 1-90 block
  decoded with the published letter homophones yield no English in either
  letter (e.g. Worsley: "wan","hhg","nof","clit","oaekrhpb","qi","wooak",
  "knfuqlbe","ye","hh","oo","bge"). The low-number block is not shared
  either (or those tokens are word codes of the other nomenclator).
- N4 (2026-10-07): DECODE R8342's "Partial Transcription" attachment is a
  blank/corrupt PNG (986x568, all black), not a transcription — no usable
  ciphertext obtainable from DECODE for either unsolved letter beyond the
  record metadata.
- N5 (2026-10-07): Crib battery on the unknown nomenclator does NOT resolve
  any mapping (code/cribs.py, evidence data/crib-attempts.txt). 5 crib
  candidates / 21 spell variants evaluated on the short groups: 11 plausible,
  10 implausible on English letter-frequency grounds ('requisite' and all 9
  'required' null-variants killed by q: token 5 x6 -> q = 30x over English
  rate; token 32 x3 -> q = 15x over). The plausible fits ('expedient',
  'important', 'needfull' x9 null-positions on W-g2 "36 19 5 32 39 12 37 8 97",
  ctx "now it will be ___ I desyre you to enquyre") are mutually exclusive
  alternatives for ONE group; zero cross-group agreeing pairs, so convergence
  is untestable — crib density too low to discriminate. W-g5 (6 tokens) and
  W-g6 (2 tokens) admitted no viable single-word candidate (recorded as
  attempted-without-candidate); A-g1 (88), W-g1 (29), W-g3 (23), W-g4 (43)
  have no forcing context for word cribs. No partial-key entry met the
  evidence bar: no token is pinned by two independent cribs.
- N6 (2026-10-07): Solved-2021 word-gloss carryover test is a MISS.
  Only 4 unknown tokens coincide with solved word-section entries (149='aid'
  [yellow], 165='any' [yellow], 236='defeat' [green], 339='im' [green]),
  6/200 occurrences (3.0%) — at/below chance for 94 entries over 142-615.
  The tempting 236='defeat' at W-g4 pos 1 ("but for this defeat ...") is a
  single context-free token; not held.
- N7 (2026-10-07): Worsley source-text fetch = null (3-strike rule).
  (1) IA advancedsearch title+creator:worsley -> 0 hits; (2) IA creator
  "Worsley, Richard" -> only Museum Worsleyanum (1794), no History;
  (3) Warner's History of the Isle of Wight (1795, IA
  historyofisleofw00warniala) full-text grep for "desyre|enquyre" and
  "asseured Frend|verrie well satisfied" -> 0 hits: the letter is not in
  Warner. Bibliographic note: Worsley's "History of the Isle of Wight" is
  1781, not 1795 — the cryptiana "(1795)" citation may be erroneous or a
  different edition; the 1781 text (Google Books/HathiTrust) is the lead
  for a future work order. [SUPERSEDED 2026-10-07 ~06:00Z: the 1781 text
  WAS located — Google Books id wOZWAAAAcAAJ, p.122; see F6/F7, N8.]
- N8 (2026-10-07): The Worsley 1781 print does NOT resolve the 22 May
  letter's "...." illegible run or sharpen group boundaries. Evidence:
  Google Books OCR of p.122 (wOZWAAAAcAAJ, SearchWithinVolume2 snippets)
  reads the tail as "379 : 4 : 28 : 5 : 348 : 354 : the ......." — the
  illegible run is equally illegible in the OCR; the opening
  "208 : 343 : 294 : ..." and sign-off "206 : 18 : So I rest your
  affeured frend , J." match data/letter-worsley-1648-05-22-cipher.txt
  token-for-token. The print CONFIRMS Tomokiyo's transcription
  (byte-level on all sampled groups) but adds nothing to Letter A. Full
  detail in data/letter-worsley-1648-southampton-cover-ocr.txt
  ("LETTER A CROSS-CHECK" section).
- N9 (2026-10-07): No further letters in the same cipher from the
  institutional leads. DECODE R8340-R8345 (fetched 2026-10-07 via
  https://de-crypt.org/decrypt-web/RecordsView/<id>): only R8342 (f.208)
  and R8343 (f.209, Decrypted = the solved 2 Sep 1648 letter) are 1648
  Harley MS 6988 items; R8340/R8341 are 1646 Oxford/Glamorgan material in
  a graphic-sign cipher; R8344/R8345 are BL Add MS 32091 (unrelated).
  BL catalogue lists Harley MS 6988 as digitised but the legacy
  Universal Viewer is unavailable — ff.206-210 not accessibly digitized
  anywhere found.
- N12 (2026-10-07): TNA = null for this hunt. discovery.nationalarchives.
  gov.uk is WAF-challenged for curl (HTTP 202, 0 bytes, header
  x-amzn-waf-action: challenge; 1 strike, not retried). The TNA BETA
  catalogue (beta.nationalarchives.gov.uk/catalogue/, curl-friendly) was
  searched with 9 queries: "Worsley" (20 results: Chancery lawsuits +
  WWI medal cards), "Worsley 1648" (4: Foster v Worsley 1648, Surrey
  committee receipts, Partington v Worsley), "Charles I Isle of Wight
  1648 cipher" (0), "Appuldurcombe"/"Worsley of Appuldurcombe"/
  "Hopkins Newport Isle of Wight"/"YARB"/"Yarborough papers" (nothing
  relevant), "Yarborough Worsley papers 1648" (0). No Worsley family
  papers and no Charles I Isle of Wight 1648 material in the beta
  catalogue.
- N13 (2026-10-07): The Isle of Wight Record Office has NO online
  catalogue (3 strikes): calmview.iow.gov.uk = DNS/connection failure;
  iow.gov.uk/council/OtherServices/Record-Office/ = HTTP 403 via curl;
  same URL = HTTP 403 via browser.open. The site offers only genealogy
  databases (pauper lists, alehouse licences). The old A2A catalogue
  (cat=189-worsley) was recovered via Wayback instead (see F13/N14).
- N14 (2026-10-07): IOW-held Worsley papers contain no 1648 material.
  A2A "Worsley of Appuldurcombe" (JER/WA, C1250-1858, 42 series):
  the correspondence series JER/WA/38/1-8 is ALL 1770-1797 (Lady
  Seymour Worsley elopement letters, estate, Hampshire Militia
  command); misc family/estate papers (JER/WA/36) oldest items 1625
  letters patent / 1676 faculty; antiquarian papers (JER/WA/39)
  oldest c.1600 handlist. Nothing 17th-century correspondence.
- N15 (2026-10-07): Lincolnshire Archives CalmView catalogue not
  operable from this environment (3 strikes): WebForms POST search =
  connection closed without response; /CalmView/Record.aspx and
  /CalmView/Overview.aspx = HTTP 500; /Record.aspx?src=CalmView.
  Catalog&id=YARB = 30s timeout. The YARB (Yarborough) deposit is the
  identified location of the personal Worsley papers (F13) but its
  contents are unverifiable remotely — on-site or email enquiry route.
- N16 (2026-10-07): DECODE keyword sweep beyond R8342 = null.
  RecordsList GET (cmd=search): Worsley 0, Isle of Wight 0, Carisbrooke
  0, Hammond 0; "1648 Charles I" -> 1 irrelevant record (id 1648 =
  Austrian cipher key, 1759); Newport -> 3 (2 irrelevant + id 8716 =
  BL Add MS 72438 f 85 cipher KEY, 1625-1647, authors Newport — a key,
  not a letter); "Charles I" -> 20 Spanish/Italian 1521-1522 records
  (Charles V). No new 1648 Isle of Wight items.
- N17 (2026-10-07): Bodleian Archives (archives.bodleian.ox.ac.uk) and
  Archives Hub (archiveshub.jisc.ac.uk) are both Cloudflare-walled for
  curl (1 strike each, logged; routes dead from this environment).
- 2026-10-07 05:55-06:00Z — Work order "test the Titus cipher against the
  unknown cipher's tokens" COMPLETE. (a) Hillier 1852 fetched from Internet
  Archive (identifier narrativeattemp00hillgoog; strike 1, HTTP 200, 413533 B,
  sha256 7db7a5ed1b7ad11f270bc6f59269f37a1073ce6492ef63d37245b4bd59348ffc;
  Google scan of the Harvard College Library Bowie Collection copy, 1852
  imprint, public domain). Verbatim excerpts -> data/hillier1852-titus-cipher.txt
  (6 passages: title notice; W=Titus/J=king letter codes p.122; F=Dowcett/D=Firebrace
  used in-line p.135; enciphered groups 715=Mrs. Whorwood/457=Lady Carlisle/714=Dr.
  Fraizer/560:315="the queen"/315="queen (not the queen)" pp.147/154-155; "the numbers
  were changed for the use of every correspondent" pp.313-314). CORRECTION to F12's
  provenance: the word-series ranges 103-420/453-608 and 634-705 are NOT printed in
  Hillier as a table — they are S. Tomokiyo's reconstruction note (from Hillier +
  Poynting p.134), preserved in an HTML comment in data/charlesi-ciphers-tomokiyo.html.
  (b) code/titus_test.py (imports derive.py's parser; exit 0) tests the 200 unknown
  tokens against the Titus ranges vs solved-2021 ranges -> data/titus-range-test.txt.
  Result: range fit CANNOT discriminate — 199/200 (99.5%) of unknown tokens fall in
  Titus defined zones vs 192/200 (96.0%) in solved-2021 zones; both systems share the
  bipartite low-block + high-word-section architecture. Top-13 previously-undefined
  tokens: 10 in Titus series1 (103-420), 0 in series2 (453-608), 3 in the assumed
  letter zone (1-102); series2 has only 2 tokens total, numeral zone 634-705 has 0.
  Discriminating datum is ASSIGNMENT-level, not range-level: Hillier verbatim "the
  numbers were changed for the use of every correspondent" — the Titus cipher was
  Titus-specific, while the unknown nomenclator is SHARED by Worsley and Prince Charles
  (20 shared tokens; both letters call it "The Cypher" — 1 Aug PS: "This Cypher which
  now I write in"). None of the known Titus/Hopkins figure numbers
  (315/457/546/193/714/715/688/560/351) occurs in the unknown corpus (max token 592).
  (c) "Life of John Barwick" (1724) fetched from IA (lifeofjohnbarwic00barw, strike 1,
  HTTP 200, 979810 B); the fuller name-code list is item "10. A Key to the foregoing
  Letters." in the APPENDIX (print pp. 395-396 — the page Tomokiyo cited) ->
  data/barwick-name-codes.txt (verbatim OCR + normalized reading + OCR-caveat list).
  Overlap check: Barwick's key assigns LETTERS only (A-Z), so it explains NEITHER
  token 395 (male person-code, F6 — Barwick has no 395; person codes are letters)
  NOR the W-g2 group (all numbers). Corroboration only: J=The King matches the
  22 May letter's "J." signature; Z=Mr. Ed. Worsley matches Letter B's "1648. Z"
  heading and confirms F11.
  VERDICT: Titus cipher == "The Cypher" (the unknown nomenclator) is REFUTED at the
  assignment level; the two share a cipher FAMILY (letter-code layer + architecture).
  See N19/N20, F16/F17.

- N19 (2026-10-07): Titus-cipher identity test = REFUTED at assignment level; range
  fit = INCONCLUSIVE (null-grade evidence, recorded). Evidence:
  code/titus_test.py (exit 0), data/titus-range-test.txt. (i) Ranges cannot separate the
  schemes: 199/200 unknown tokens (99.5%) fall in Titus defined zones vs 192/200
  (96.0%) in solved-2021 zones — both share the low-number letter block + high word
  section, and Titus series1 (103-420) swallows the same 40.5% as solved-2021 words
  (142-615). The top-13 undefined tokens (379, 212, 329, 214, 339, 248, 208, 230, 388,
  395) all land in Titus series1; (86, 96, 97) in the assumed 1-102 letter zone; but
  the same tokens land in solved-2021 words/letters — no discrimination. (ii) DECISIVE:
  Hillier verbatim, "the numbers were changed for the use of every correspondent"
  (data/hillier1852-titus-cipher.txt, excerpt [F]) — the Titus numerical cipher was
  Titus-specific, while the unknown nomenclator was used by at least TWO correspondents
  (Worsley + Prince Charles, 20 shared tokens, both calling it "The Cypher").
  (iii) None of the attested Titus/Hopkins figure numbers occurs in the unknown corpus:
  315/457/546/193/714/715/688/560/351 all x0 (max unknown token 592; tokens 39/40/64
  occur once each but sit in the unknown letters' low-number block, so no carryover).
  So Titus != "The Cypher" numerically, though the Titus letters and the unknown
  letters belong to the same cipher family (shared letter codes, shared architecture).
- N20 (2026-10-07): Barwick key explains neither unknown-cipher target. The Barwick
  "Key to the foregoing Letters" assigns LETTER codes only (A-Z); all 200 unknown
  tokens are numbers, so: (a) token 395 (male person-code per F6) is NOT explained by
  Barwick — no 395 in the key, whose person codes are letters (W, L, N, ...); 395's
  person-hood rests solely on the Letter-B cleartext (F6). (b) W-g2
  "36 19 5 32 39 12 37 8 97" contains no letter codes; no Barwick overlap. Recorded
  as the work order (c) check result; full check in data/barwick-name-codes.txt.
- N21 (2026-10-07): No retrieval failures in this work order — IA served both
  Hillier 1852 and Barwick 1724 on strike 1 each. The 3-strike/Google-Books fallback
  was not needed.
- F16 (2026-10-07): Barwick name-code key RECOVERED and transcribed. Item "10. A Key
  to the foregoing Letters.", Appendix pp. 395-396 of "The Life of the Reverend Dr.
  John Barwick" (London, 1724; public domain) — data/barwick-name-codes.txt (verbatim
  OCR + normalized reading, 6743 B). 19 codes: A=Francis Cresset; B=Mrs. Mary, assistant
  to Lady Wheeler, laundress to his Majesty; C=Col. William Legge, groom of the
  bedchamber; D=Henry Firebrace; E=Lady Carlisle; F=Abraham Doucett; G=The Prince;
  H=Lady [rest lost in OCR at the page break — not guessed]; I=Lady Wheeler; J=The King;
  K=Lady Aubigny [OCR "Obtgny"]; L=Richard Osborne; M=The Queen; N=Mrs. Whorwood;
  O=Mr. Z[...] , a London merchant [surname illegible]; S=The Duke; V=John Burrows;
  W=Captain Titus; Z=Mr. Ed. Worsley, [???] in the Isle of Wight. VERIFIED STRUCTURAL
  FINDING: the letter-code layer is stable across three correspondences — the Barwick
  key (Firebrace letters), Hillier's Titus letters (W=Titus, J=king, F=Dowcett,
  D=Firebrace used in-line), and the Hopkins letters (F10: L=Osborne, W=Titus,
  N=Whorwood) — while Hillier states the NUMBERS "were changed for the use of every
  correspondent". I.e. shared letter-code layer + per-correspondent numerical
  nomenclator is the system's design. This confirms F11 (Z=Worsley) from a second
  primary source and corroborates the unknown letters' "J." signature (J=The King).
- F17 (2026-10-07): Correction to the Titus ranges as quoted in F12 — Hillier 1852
  itself prints Titus-letter groups 714 (Dr. Fraizer) and 715 (Mrs. Whorwood)
  (verbatim, data/hillier1852-titus-cipher.txt excerpt [D]), which lie ABOVE Tomokiyo's
  stated 634-705 numeral/day/random zone. The reconstruction's 634-705 upper bound is
  not exact even for the Titus cipher itself; treat 634-705 as approximate, not a
  hard section boundary.


## Findings
- F8 (2026-10-07): Cover-note continuation recovered (GB OCR, run 2):
  "...If I knew certainely that you had the Cypher out of w.ch I have
  writen this name, I would wryte more freely than ..." — the cover note
  ITSELF names someone in cypher ("this name" written "out of" = in The
  Cypher); the token is outside the snippet window. Implication for the
  5 May hunt: the ca. 5 May 1648 letter was an ENCLOSURE ("the inclosed",
  "the thin letter is for him", sent via Worsley/Z to the 395-person),
  and the king's note is a reply to Worsley's covering letter ("I thanke
  you for your care ... I have had an Answer and now this is a reply to
  that"). Enclosures were not printed in Worsley's History — the 5 May
  text is not in the volume; it would live among Worsley's or the
  recipient's papers, not in the printed narrative.
- F9 (2026-10-07): BL Egerton MS 1788 — original Carisbrooke letters
  with cipher material. Catalogue title (verbatim): "ORIGINAL letters
  from Charles I., when prisoner in Carisbrooke Castle, Isle of Wight,
  to Henry Firebrace [afterwards knighted by Charles II.], relative to
  plans for his escape, the means of communication with his adherents,
  etc . ; 23 Apr.-27 Dec. 1648, and n.d. Holograph, in a feigned hand;
  signed "J." and addressed "D."" — the same "J." signature as the
  1 Aug / 22 May / Letter B letters. Three cipher items in the volume:
  (5) "- to [Henry Firebrace], enclosing a letter from the king; n.d .
  On the back is a cipher of names. f. 51"; (6) "Cipher designed by
  Charles I., with note by the same. Holograph. f. 53"; (7) ""The names
  of severall persons knowne to King Charles the First of blessed memory
  by the letters of the alphabet heereafter mentioned who were
  serviceable to his majestic in the tymes of his most strickt
  ymprisonment by the Rebells in Ao 1648." In the hand of Henry
  Firebrace. f. 54". Record: https://searcharchives.bl.uk/catalog/
  032-001982692. NOT digitised; "Letter of introduction required to
  view this manuscript". Relevance: HIGHEST in this hunt — the f.53
  holograph cipher may BE "The Cypher" nomenclator, and the f.51
  enclosure + "cipher of names" matches the 5 May enclosure pattern.
- F10 (2026-10-07): BL RP 9319 — 70 photocopies, early-18th-century
  transcript volume (RP = Copies of Exported Manuscripts Deposited under
  Government Export Regulations; originals exported, current location
  unknown) containing, with the Hopkins petition transcript, "a copy of
  66 secret letters written by Charles I and smuggled out of the Isle
  of Wight, the originals of which went into the hands of Hopkins"
  (George Hopkins, of Newport, whose family home hosted the king during
  the Treaty of Newport 1648). Record: https://searcharchives.bl.uk/
  catalog/040-001606369. NOT digitised. Relevance: HIGH — the Hopkins
  letters contain in-clear figure assignments of the same cipher family
  (see F12 secondary findings): 39/40 (persons), 47->52 (party), 58
  (41's brother), 64 (Treaty); letter codes L (Osborne), W (Titus),
  N (Jane Whorwood); numerical 715 (Mrs Whorwood), 457 (Lady Carliffe),
  546/193, 714 (Dr Fraizer); the king sent "an addition of some
  Figures, with Names" on 26 July 1648 — RP 9319 may contain an actual
  partial key.
- F11 (2026-10-07): Z = Mr. Worsley, confirmed. Tomokiyo's "King
  Charles I's Ciphers" (https://cryptiana.web.fc2.com/code/charlesi.htm,
  citing Hillier p.112): the king and Firebrace "arranged some letter
  codes for names such as: A (Cresset), C (Col. Legge), F (Dowcett),
  Z (Mr. Worsley)"; "a fuller list is found in Life of John Barwick
  (Google) p.395". The DNB Firebrace entry glosses the cipher letters
  as "Francis Cresset, Colonel William Legg, groom of the bedchamber,
  Abraham Doucett, and Edward Worsely" — so Z = Edward Worsley. This
  confirms the lane's "to Worsley ('Z')" attribution and identifies the
  man.
- F12 (2026-10-07): The Titus numerical cipher, described (Tomokiyo
  charlesi.htm, reconstructed from Hillier and Poynting p.134): "In
  letters to Titus, a numerical cipher was used in addition to the
  above-mentioned letter codes. Lower numbers were reserved for single
  letters. Further, it had two series of generally alphabetically
  ordered words and syllables such as 103(am)-420(you) and
  453(business)-608(trouble), followed by numerals such as 634(one),
  647(twenty), days and months such as 659(Monday), 665(Sunday),
  672(May) and some random words such as 680(wife), 686(escape), and
  705(boat)". NOTE: ranges differ from the solved-2021 nomenclator
  (1-90 / 142-615) — whether the Titus cipher IS "The Cypher" is
  untested (next work order). The fifteen original Titus letters were
  sold to the British Museum c.1852 (Hillier 1852 intro, via
  titusfamily.ca) but no BL catalogue record was found (N18). The
  deciphered letters are printed in George Hillier, "Narrative of the
  attempted escapes of Charles the First from Carisbrook Castle"
  (London: Richard Bentley, 1852) — IA identifiers
  narrativeattemp00hillgoog, anarrativeattem00hillgoog,
  narrativeofattem00hilluoft.
- F13 (2026-10-07): Worsley papers provenance split (A2A cat=189-worsley
  archival history, via Wayback capture 20120617142648). The 2nd Earl
  of Yarborough removed the personal Worsley papers to Brocklesby Park,
  Lincolnshire c.1854; deposited with Lincolnshire County Record Office
  1957 (the YARB collection — catalogue not searchable from here, N15).
  Clement Francis Worsley's 1948 deposits went to: Borough of Newport,
  Hampshire CRO, Carisbrooke Castle Museum, the British Museum, and
  Godshill Parish Council — all but the British Museum deposit later
  passed to the Isle of Wight County Record Office. The British Museum
  deposit was mounted in 1967 as BL Add MS 46501 ("a beautifully bound
  volume of very miscellaneous content. Only about half the documents
  in it are Worsley papers at all", date range 1322-1830, NOT
  digitised: https://searcharchives.bl.uk/catalog/040-002102487).
  Implication: the 1781-printed letters' manuscripts most likely sit in
  the Lincolnshire YARB deposit or Add MS 46501 — NOT in the IOW-held
  JER/WA papers (N14).
- F14 (2026-10-07): BL Add MS 4186 = Thomas Birch's 1764 printer's copy
  of the Hammond/Derby House letters (1647-48) with "(f) a cipher.
  f. 80" (verbatim scope excerpt in data/catalogue-hunt-2026-10-07.json).
  Record: https://searcharchives.bl.uk/catalog/040-002109646. NOT
  digitised. Relevance: MEDIUM — the f.80 cipher's system is unidentified
  (may be the Hammond-correspondence cipher, not necessarily "The
  Cypher").
- F15 (2026-10-07): Harley MS 6988 neighbouring folios (BL scope,
  verbatim excerpts in data/catalogue-hunt-2026-10-07.json): f.208 = the
  1 Aug 1648 cipher letter; f.209 = the 2 Sep 1648 letter (solved 2021);
  ff.210r-211r = to the Scottish Parliament; ff.211v-212r = to
  Manchester/Lenthall (accepting the treaty); ff.212r-214v = demands,
  Carisbrook 28 Aug 1648; ff.214v-215v = to Manchester/Lenthall,
  Carisbrook 10 Aug 1648. No further cipher letters adjacent — N9
  stands.
- F1: The solve is Biermann + Brown (+Thomas Bosbach on the final key),  2021; NOT a Cryptologia paper. Publication chain:
  (a) Tomokiyo, "What It Takes to Break Charles I's Cipher Used in the Isle
  of Wight", Cryptiana, 25 Apr 2021 (mod. 6 May 2021),
  https://cryptiana.web.fc2.com/code/charlesi2.htm;
  (b) Klaus Schmeh, Cipherbrain, 11 Apr 2021 (challenge) and 5 May 2021
  (final results + full nomenclator + plaintexts),
  https://scienceblogs.de/klausis-krypto-kolumne/2021/05/05/geloest-die-verschluesselten-briefe-von-karl-i-an-seinen-sohn/.
- F2: System = nomenclator: homophonic letter substitution (numbers 1-90,
  24-letter alphabet, nulls 1/10/58/68/69/78/100-107) + alphabetically
  ordered word/nomenclature section 142 (able) - 615 (you). Full key in
  data/nomenclator-charles-i-1648-solved-key.json (hand-transcribed from
  the published key image; see provenance there).
- F3: Letter inventory (all four + the two later-added): UNSOLVED =
  Charles I to Prince Charles, 1 Aug 1648 (BL Harley MS 6988, f.208;
  DECODE R8342, status Non-decrypted) and Charles I to Worsley ("Z"),
  22 May 1648 (Worsley's History of the Isle of Wight, 1st ed. 1781,
  p.122 — corrected 2026-10-07, see F7; cryptiana's "(1795) p.237" is
  erroneous). SOLVED (2021) =
  to Prince Charles 2 Sep 1648 (Harley MS 6988), 3 Oct 1648 (Vindication),
  6 Nov 1648 (Harley MS 6988), 7 Nov 1648 (Original Letters).
  Triage correction: "two of four solved" is stale; current state is
  four of six solved, the two unsolved using a different nomenclator.
- F4: Positive control passes — code/apply.py decodes the solved 3 Oct 1648
  group (61 tokens) to "<the> <Scots> <offer> <you> <could> <be> <con> t e n t
  <to> m a r r y ..." which matches the published decipherment
  ("you can/could be content to marry mademoiselle in regard of her person,
  I finding her in (other respects) a good match for you"; verified against
  the Cipherbrain May-2021 plaintext image). Note: final plaintext reads
  211 as "can"; the key image labels 211 "could" (green) — source wording
  variant, flagged in the key JSON's confidence note, unresolved.
- F5: The 1 Aug 1648 transcription (data/letter-prince-charles-1648-08-01-cipher.txt,
  88 cipher tokens) is byte-verified against the BL manuscript image
  (data/letter-prince-charles-1648-08-01-manuscript.png): every token matches
  in order when read from the manuscript.
- F6 (2026-10-07): NEW cipher material in the same system ("The Cypher"),
  Worsley 1781 p.122 (Google Books wOZWAAAAcAAJ, OCR-snippet
  reconstruction — verbatim wording NOT established, see the file's
  provenance header). (i) LETTER B, headed "1648. Z" (undated in
  snippets): escape-planning cover letter — Southampton, Mrs. Pit's
  house, "where you will finde W: and deliver to him the inclosed",
  boat/landing/watchword, "the other is to 395 w.ch I defyre you send
  safely and speedely to him", signed "your most asseured frend, J.";
  (ii) a cover note: "The Cypher; the thin [?this] letter is for him, for
  whom I sent you one, upon the fifth of this month" — i.e. a THIRD
  cipher letter (ca. 5 May 1648) existed; its text was not recovered.
  Attribution (reasoned, not proven): same correspondents (J->Z), the
  king's "The Cypher" label, token 395 shared with the 22 May letter's
  W-g1/W-g4. New semantic constraints: 395 = male PERSON (name-code);
  W = male person at Mrs. Pit's. Full reconstruction in
  data/letter-worsley-1648-southampton-cover-ocr.txt.
- F7 (2026-10-07): Bibliographic correction — the 22 May 1648 Worsley
  letter is on p.122 of Worsley's History of the Isle of Wight, 1st ed.
  1781 (London: A. Hamilton; ESTC T86489), NOT "(1795) p.237" as
  cryptiana cites. No 1795 Worsley edition is known; Warner's 1795
  "History of the Isle of Wight" is a different work (N7).

## Data inventory
- data/gb-tiling-2026-10-07.json (26806 B, sha256
  565c354b977d037afbb73739a48f6f14152501cc74d7c62268c4520abe4386b0):
  consolidated raw SearchWithinVolume2 responses for Worsley 1781
  (wOZWAAAAcAAJ), run 2, 2026-10-07 05:28-05:36Z: 17 queries (Mrs. Pit,
  Southampton, 395, fifth of this month, watchword, desyre you send,
  the Cypher, Carisbrooke, Hammond, the fifth, W: and deliver, inclosed,
  speedely, asseured frend, May, escape, 208 : 343) with per-query
  byte counts and sha256. Retrieval: curl, HTTP 200. OCR snippets only —
  not verbatim text.
- data/letter-worsley-1648-southampton-cover-ocr.txt (6253 B, sha256
  f1060c7fc27353b7c3a530101d7d84e2053bcd20099f335244c462671701bfdd;
  SUPERSEDES the 4398 B / ee98412f version): Letter B + cover-note
  reconstruction, run-2 sharpened (continuous opening clause, "Least
  [=Lest?] you should not understand" sign-off postscript, cover-note
  continuation "out of w.ch I have writen this name", Letter-A head
  verbatim confirmation). Still OCR-reconstruction, NOT verbatim.
- data/letter-worsley-1648-05-22-cipher.txt (635 B, sha256
  539202a92df16693523a83765ab68d24f6fa835fc7b3b037734ae6398f92df7d):
  verbatim transcription of the unsolved Worsley letter cipher groups + clear
  text. Source: https://cryptiana.web.fc2.com/code/charlesii.htm#SEC1
  (section 4), retrieved 2026-10-07 04:20Z via curl; original Worsley's
  History of the Isle of Wight, 1st ed. 1781, p.122 (corrected 2026-10-07,
  see F7; public domain). Print cross-check 2026-10-07 (N8): matches the
  1781 print token-for-token on all sampled groups.
- data/letter-prince-charles-1648-08-01-cipher.txt (787 B, sha256
  c5cc4877da0e28643caed549a7d6a1b730b3de481b197698df0d25bbe99855be):
  verbatim transcription of the unsolved 1 Aug 1648 letter (88 cipher
  tokens), verified token-by-token against the manuscript image.
  Source: https://cryptiana.web.fc2.com/code/charlesii.htm#SEC1, retrieved
  2026-10-07 04:20Z via curl; original BL Harley MS 6988, f.208
  (DECODE R8342).
- data/letter-prince-charles-1648-10-03-solved-control.txt (717 B, sha256
  2255289aa4fe3db1bfd88918240b16381ddfadb1e6bbaf75963fbb1d45731c77):
  solved 3 Oct 1648 cipher groups (61 tokens) for the positive control.
  Source: https://cryptiana.web.fc2.com/code/charlesi2.htm, retrieved
  2026-10-07 04:19Z via curl.
- data/nomenclator-charles-i-1648-solved-key.json (3614 B, sha256
  1437621e749cd57a2e097058e0046d92f676d55c9ebb4270c004ddb0f0e10dd5):
  hand transcription of the published key. Source image retrieved
  2026-10-07 04:26Z via curl from
  https://scienceblogs.de/klausis-krypto-kolumne/files/2021/05/Nomenclator-Charles-I.png
  (key by Biermann/Bosbach/Brown, via Cipherbrain 5 May 2021).
- data/nomenclator-charles-i-1648-solved-key.png (166979 B, sha256
  44fd7a9876603acb485ab31ea751b4c3ce20c4fbb244c6dcc87bc1c5119c98fe):
  the published nomenclator image itself, same source/retrieval as above.
- data/letter-prince-charles-1648-08-01-manuscript.png (814800 B, sha256
  284f993a28d3ea6e70de7646e38818fb7752e8d9e0a87805b816b9892685111d):
  BL manuscript image of the unsolved 1 Aug 1648 letter, retrieved
  2026-10-07 04:26Z via curl from
  https://scienceblogs.de/klausis-krypto-kolumne/files/2021/04/Charles-Letter-1648-08-01.png
  (Cipherbrain April 2021 article; original BL Harley MS 6988).
- code/derive.py (8897 B, sha256
  6feb6552feb6887aa0429ad66ef9da2dcf79dd00cc24311b8ace72be5eea92e3):
  unknown-nomenclator work order (a): whitespace-run cipher-group parser,
  per-letter + combined token frequency tables, range histograms vs the
  solved-2021 section boundaries, repeated n-grams, cross-letter shared
  tokens, and the crib table (each group with adjacent cleartext).
- data/freq-analysis.txt (5504 B, sha256
  d83b802f6ed11d1b2efbd3f7daa9aae087908fc760c84b54622305b92dfa0e31):
  output of code/derive.py (2026-10-07): frequency tables, structure
  hypothesis (bipartite architecture shared with solved system, unverified),
  full crib table. The 200 tokens: 122 distinct; top 5(x6), 379(x5),
  50(x5); 54.5% in 1-90, 40.5% in 142-615.
- code/cribs.py (11323 B at run 1, sha256
  591035e48a16f9ed7bc75b318b9789bfee7c5fa5ccfabd108e1a55319dc77faa;
  SUPERSEDED 2026-10-07 by the 13147 B version below):
  unknown-nomenclator work order (b): systematic crib battery with
  two-phase evaluation (independent frequency-plausibility per variant,
  then pairwise cross-group compatibility) + solved-key word-gloss
  carryover test.
- data/crib-attempts.txt (5777 B, sha256
  aaa850041dc61588ed7ffdc4e9a4fa5379b3bb9f0fae955b4c0e541c555d821b):
  output of code/cribs.py (2026-10-07): 5 candidates / 21 variants,
  11 plausible / 10 implausible (frequency), 0 cross-group agreeing pairs.
- data/letter-worsley-1648-southampton-cover-ocr.txt (4398 B, sha256
  ee98412f07c4915eb40d3b6482cd1fd703539785ae83f14bc198070197ceec06):
  SUPERSEDED 2026-10-07 by the run-2 sharpened version (6253 B, sha256
  f1060c7fc27353b7c3a530101d7d84e2053bcd20099f335244c462671701bfdd —
  see the inventory entry above). Original entry: NEW same-system cipher
  material (F6): Letter B + "The Cypher" cover
  note reconstructed from Google Books OCR snippets of Worsley 1781
  p.122 (volume wOZWAAAAcAAJ, digitized from the National Library of the
  Netherlands copy 2013-06-18; https://books.google.com/books?id=wOZWAAAAcAAJ),
  with provenance header, [bracketed] OCR gaps, Letter-A print
  cross-check, and the 1781/p.122 bibliographic correction (F7).
  Reconstruction, not verbatim — wording not established.
- data/crib-attempts-run1-200tok.txt (5777 B, sha256
  aaa850041dc61588ed7ffdc4e9a4fa5379b3bb9f0fae955b4c0e541c555d821b):
  archived run-1 output of code/cribs.py (pre-Phase-3), kept so the
  re-run (run 2, data/crib-attempts.txt, sha256
  c7aebc7f79d94611730d3239f1ff638850673ae6902e8bde24aab0c3bc88f8bd)
  is diffable. Run 2 adds Phase 3 (single-token semantic cribs C1/C2):
  tallies unchanged, 0 cross-group agreeing pairs, verdict no convergence.
- 2026-10-07 05:35-07:00Z — Work order "manuscript catalogue hunt for the
  5 May 1648 enclosure and related papers" COMPLETE (goal = identification,
  not retrieval). Routes, all via curl unless noted, 3-strike rule per
  source: BL Archives and Manuscripts Catalogue (searcharchives.bl.uk —
  curl-friendly; 12 queries) -> Egerton MS 1788 (F9), RP 9319 (F10),
  Add MS 4186 (F14), Add MS 46501 (F13), Harley 6988 neighbours (F15);
  TNA Discovery WAF-challenged (strike 1, no retry) -> fell back to TNA
  BETA catalogue (9 queries) -> null (N12); IOW Record Office online
  catalogue does not exist (N13); A2A Worsley catalogue recovered via
  Wayback -> IOW papers null for 1648 (N14), provenance split (F13);
  Lincolnshire CalmView not operable from here (N15); DECODE keyword
  sweep -> null beyond R8342 (N16); Bodleian + Archives Hub Cloudflare-
  walled (N17); Titus originals provenance found via titusfamily.ca,
  BL shelfmark not located (N18/F12). Tomokiyo charlesi.htm fetched ->
  Z=Worsley attribution (F11) + Titus cipher description (F12). Full
  search log: data/catalogue-hunt-2026-10-07.json.
- code/cribs.py (13147 B, sha256
  da8a2737c4f0a1a498bd23eb426b420bedf4d2540e23291b81e9a6e853a1f136):
  + Phase 3 (single-token semantic cribs from the new Worsley p.122
  material); re-run 2026-10-07 exit 0.
- data/catalogue-hunt-2026-10-07.json (11877 B): consolidated search log
  for the 2026-10-07 manuscript catalogue hunt (BL/TNA/DECODE/A2A/
  Lincolnshire queries, hit counts, verbatim record extracts for
  Egerton MS 1788, RP 9319, Add MS 4186/46501, Harley MS 6988, plus
  secondary findings: Z-attribution, Titus cipher description,
  Hopkins figure assignments).
- data/charlesi-ciphers-tomokiyo.html (83011 B, sha256
  fcbf15939e733760752936f41b8e38d90000b2375ee9b0df7ec1f787e75e43f9):
  S. Tomokiyo, "King Charles I's Ciphers"
  (https://cryptiana.web.fc2.com/code/charlesi.htm), retrieved
  2026-10-07 via curl, SHIFT_JIS->UTF-8 decoded. Isle of Wight section:
  letter codes A(Cresset)/C(Legge)/F(Dowcett)/Z(Worsley) (Hillier p.112;
  fuller list in Life of John Barwick p.395); Titus numerical cipher
  reconstruction (Hillier/Poynting); Hopkins letters figure quotes
  (39/40, 47->52, 58, 64, 715=Whorwood, 457=Lady Carliffe, 546/193,
  714=Dr Fraizer; L=Osborne, W=Titus, N=Whorwood).
- data/a2a-worsley-cat189-top.html (28554 B, sha256
  289d1908c1353b3e3041334873a45cdd7fa8b5e9bfbe4ea8b6044bef4482a6f8):
  Wayback capture (20120617142648) of the A2A "Worsley of Appuldurcombe"
  catalogue top page (cat=189-worsley): reference JER/WA, C1250-1858,
  42 series, archival history (provenance split: Brocklesby/Lincolnshire
  YARB deposit 1957; Clement Francis Worsley's 1948 five-way deposit;
  British Museum deposit -> BL Add MS 46501).
- data/a2a-worsley-cat189-cid7.html (22664 B, sha256
  9ff911c810677fce2f4b577dbb9836ba6a5224add9db3a563d29c0128be108ce):
  same capture, cid=7 (MISCELLANEOUS FAMILY AND ESTATE PAPERS) —
  oldest items 1625/1676, no 17th-c. correspondence.
- data/a2a-worsley-cat189-cid9.html (18393 B, sha256
  062c1650ec431ddfcb7bbb7d944edcee85d72aab91da8b3c3c6fc4b077d3936448):
  same capture, cid=9 (CORRESPONDENCE = JER/WA/38/1-8): all 1770-1797,
  no 17th-century material (N14 evidence).
- data/a2a-worsley-cat189-cid10.html (18158 B, sha256
  e6287f7ad24617017505242ff5a244dc4cd468e591974741ed3058f271a5bb72):
  same capture, cid=10 (ANTIQUARIAN PAPERS) — oldest c.1600 handlist.
- data/hillier1852-titus-cipher.txt (9276 B, sha256
  1c19ef6940758014c5163a6a3ca4277f913bdaeaed2cdb99e755973777db8e33):
  NEW 2026-10-07. Verbatim excerpts from George Hillier, "Narrative of the attempted
  escapes of Charles the First from Carisbrook Castle" (London: Richard Bentley, 1852),
  full text https://archive.org/download/narrativeattemp00hillgoog/narrativeattemp00hillgoog_djvu.txt
  (IA id narrativeattemp00hillgoog; Google scan of Harvard College Library Bowie Collection
  copy; 1852 imprint, public domain). Retrieved 2026-10-07 ~05:55Z, curl HTTP 200,
  strike 1, 413533 B, sha256 7db7a5ed1b7ad11f270bc6f59269f37a1073ce6492ef63d37245b4bd59348ffc.
  6 verbatim passages: title notice; W=Titus/J=king (p.122); F=Dowcett/D=Firebrace in-line
  (p.135); enciphered groups 715=Mrs. Whorwood / 457=Lady Carlisle / 714=Dr. Fraizer /
  560:315="the queen" / 315="queen, not the queen" (pp.147/154-155); "the numbers were
  changed for the use of every correspondent" (pp.313-314). Provenance header notes that
  the 103-420/453-608/634-705 ranges are Tomokiyo's reconstruction, NOT in Hillier.
- code/titus_test.py (9059 B, sha256
  7c8238399078b8a17692e28daaa17695d23fc77e485762f7fc7a2c795ba277fe):
  NEW 2026-10-07. Titus-range fit test: loads the 200 unknown tokens via derive.py's
  parser, classifies each against the Titus ranges (1-102* letter zone ASSUMED bound,
  103-420, 453-608, 634-705, gaps 421-452/609-633) vs solved-2021 (1-90, 100-107,
  142-615); per-token tables, top-13 undefined-token placement, discriminating-token
  report, Hillier cross-check (714/715 above 634-705). Exit 0.
- data/titus-range-test.txt (3750 B, sha256
  1b35a3d9ecfc6938913a94f0568ee90234db4b539bf45cb3f10c5b297f611141):
  NEW 2026-10-07. Output of code/titus_test.py: 199/200 (99.5%) unknown tokens in
  Titus defined zones vs 192/200 (96.0%) solved-2021 — ranges cannot discriminate;
  top-13: 10 in series1, 3 in letter zone; numeral zone 634-705 = 0 tokens; verdict:
  identity decided at assignment level (N19), not by ranges.
- data/barwick-name-codes.txt (6743 B, sha256
  bd918a9f030d3e2d42a35178c582d3b8072523ff762ad023730d7df53ebf5f5b):
  NEW 2026-10-07. "Life of the Reverend Dr. John Barwick" (London, 1724, public domain),
  full text https://archive.org/download/lifeofjohnbarwic00barw/lifeofjohnbarwic00barw_djvu.txt
  (IA id lifeofjohnbarwic00barw). Retrieved 2026-10-07 ~05:58Z, curl HTTP 200, strike 1,
  979810 B, sha256 66993214c81f70d169c087b86fc18465c0e6bfaa958e1b859440af94b35663b5.
  Contains: item "10. A Key to the foregoing Letters." (Appendix pp. 395-396) verbatim
  OCR + normalized reading (19 codes A-Z; H truncated in OCR, marked not guessed) +
  OCR-caveat list + the token-overlap check (Barwick explains neither 395 nor W-g2;
  J/Z/W corroboration noted).
