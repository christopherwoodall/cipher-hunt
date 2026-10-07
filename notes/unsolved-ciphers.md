# Unsolved Ciphers — consolidated notes

Extracted 2026-10-06 from two live pages:
- **(B)** Daniel Bourdeau, "Unsolved Historical Ciphers — Working Notes, Solutions and Corrections", https://dbourdeau.github.io/cyphersolver/index.html — 248 catalogue entries; 68 still unsolved or only partly broken (site labels: "not solved" / "ciphertext-only break" / "in progress").
- **(C)** "Unsolved Historical Ciphers", https://cryptiana.web.fc2.com/code/unsolved.htm — a language-by-language survey by the same DECODE research circle (the author cites Bourdeau's solutions throughout); only entries still marked unsolved (or partly solved) are listed below.

Neither page lists the Beale ciphers. The Zodiac Z340 is on page (C) but marked **solved** (2020, Oranchak/Rook/Olsen); Z13/Z32 get only a passing mention.

## The famous ones (on these pages)

### Voynich manuscript (Beinecke MS 408), c.1404–38 — (B) not solved
Type unknown (possibly verbose encoding, possibly structured meaningless text). Translational-robust entropy analysis excludes a plain or simply enciphered European language; verbose-cipher vs. meaningless-text hypotheses are left roughly even, with the author naming the tests that would separate them.

### Indus script, Mohenjo-daro / Harappa / ~50 sites, c.2600–1900 BCE — (B) not solved
Not a cipher per se — an undeciphered script. No sound value recovered. Parpola's structural claims hold up; 2,364 hypotheses registered and tested (1,224 held, 1,140 failed) pinning down grammar (ending slots, line-break rules, numeral behavior, seal-name populations like Linear B personal names), but no word translated.

### Linear A, Minoan Crete — (B) not solved
Language unknown; Linear B sound values carry over (6 matches vs 0.49 expected). 41.8% of tokens give sense (numbers, fractions, commodities, KU-RO/KI-RO, three place names). Semitic and Luwian relatives fit no better than control languages; no word translated.

### German Ordnungspolizei Doppelkasten radiograms, Mogilev/Rovno/Proskurov, 27 Feb & 16 Jun 1942 — (B) not solved
Double Playfair, each pair enciphered twice through the same two boxes. All standard attacks (annealing, tempering, EM, etc.) fail even on a synthetic control with a known key. A known-plaintext solver recovers the boxes from ~80 pairs, but Bletchley's 1942 decrypt of the 16 June message (Borki) won't align with its ciphertext. Needs the February decrypts (TNA HW 16/17) or the exact enciphered wording of the June message.

### Scorpion letters S1 and S5, 1991 — (B) not solved
Below the unicity distance for a homophonic key — controls produce fluent false solutions, so no claimed reading can be trusted. A 2018 claim was tested and didn't hold.

### Copenhagen cryptogram, c.1950s — (B) not solved
Two transcriptions, ten languages, six reading conventions tried; not a simple substitution in any language tested.

### Debosnys cryptograms, 1882–83 — (B) not solved
A cipher poem in rhyming couplets in a French syllabary, too short for any crib-free attack.

## From the Bourdeau page (B), in page order

### Four cipher letters to Gianfrancesco Gonzaga, lord of Mantua, 1428–30 — (B) ciphertext-only break, 3 of 4 read
Homophonic + nulls; keys rebuilt from ciphertext alone (96–100% reads on three letters: a Gonzaga marriage, the Malatesta/Urbino/pope, the archbishop of Patras offering his see to Venice). **Open:** Pandolfo Malatesta's own three runs (262 signs) — not a simple or homophonic substitution; no fitting key.

### Sienese Concistoro cipher letters, before 1429–1547 — (B) ciphertext-only break, partial
Keys recovered ciphertext-only for several letters (87–97% reads: a lord's route into Sienese territory, Latin treaty articles with the Emperor, etc.). **Open:** Meister's 1421 letter, nos. 2, 26–28 (not photographed), two long systems, and six letters without a key.

### Queen María of Castile → Alfonso V, Valencia, 5 Aug 1435 — (B) not solved
42 signs in three runs inside clear Catalan (day of Ponza; context suggests the truce of Majano). Period keys don't fit the alphabet; a 1429 nomenclator may match the dotted word-signs but it's a hypothesis, not a reading. Blocked on undigitised registers.

### Sforza side → Giorgio del Maino, 4 May 1446 — (B) in progress
404 signs of graphic-sign runs in clear Lombard Italian; annealing fails. Needs the 1446 Maino key or a colour scan.

### Benedetto Fantini → the Este court, Buda/Eger, 1517–18 — (B) not solved
Two-tier sign cipher (syllabic, Caprile-1519 family); 1,370 columns transcribed. A syllabary annealer that recovers a same-size control gives no Italian. Needs a key or a paired letter.

### Lope de Soria → Charles V, Genoa, Jun–Jul 1523 — (B) ciphertext-only break, read
Substitution alphabet found by annealing from random starts; Venetian league, Milanese money, 18,000 ducats, the French king's descent on Italy. **Open:** code words rip, pur, qed, mul.

### Pseudo-Elias of Cortona, *Lumen luminum*, North Italy c.1525 — (B) not solved
Alchemical codex, not a letter (Beinecke Mellon MS 29). Not simple substitution (IC 0.075); every system tried (mono, homophonic, Caesar/Trithemius, Vigenère, Alberti) fails in Italian and Latin. Possibly invented secret names — the Beinecke catalogue suspects charlatanism.

### Gilbert Bayard → Montmorency, Toledo, 5 Jan 1526 — (B) not solved
56 signs, 29 kinds; period keys share shapes but not values; too short for a blind break. Needs the original (BnF V. 41 f. 4).

### Giovan Gioacchino da Passano → Francis I, London, 15 Mar 1530 — (B) ciphertext-only break, read
Surviving account (cash, credits, jewels, Winchester/St Albans/York) — 96% coherent. **Open:** three rare signs, plus pages/lines the 16th-c. copyist omitted.

### Guido Rangone → Montmorency, Venice, 1530 — (B) ciphertext-only break, read
Homophonic substitution (~50 signs) broken by annealing; Cesare Fregoso, Venice's Verona governorship. **Open:** four short runs of hapax signs.

### A Bavarian agent → the Dukes of Bavaria, Pressburg talks, c.1533–34 — (B) ciphertext-only break, read
Homophonic substitution broken on the first run; Pressburg negotiations, a Turkish embassy, Gritti dispatched. **Open:** person codes.

### Charles of Egmond → grand master of France, Arnhem, 18 Jul (?) — (B) ciphertext-only break, read
Independent re-solution of Lasry's 2023 break (requests support after entering war); date sign and a few anomalies retained, recipient/year unsettled.

### Vatican Challenge Part 5 (Farnese → Poggio), Apr 1542 — (B) not solved (already solved by Klee)
Note: the entry records Simon Klee's Sept 2026 solution (18 letter codes + null; mixed one-/two-digit monoalphabetic key) — found already solved. **Open:** companion R91 (Spagna IA-1), another key.

### Claude de La Guiche → Montmorency, Rome, 22 Nov 1551 — (B) ciphertext-only break, read
Simple 22-sign substitution broken by permutation annealing; Dom Diego, the Sienese envoy, Count of Santa Fiora. **Open:** one name, the struck-through opening; Seure's six homophonic Lisbon letters (~2,000 signs) still open.

### Sir Henry Percy to Cecil, Norham, 23 Jul 1559 — (B) not solved
63 signs in a box script with dot/underline marks (only a Forbes tracing survives). No substitution fits; Cecil's decipherment sits on the TNA original, calendars silent on which words were ciphered.

### Unknown Catholic gentleman of the Agenais → Montmorency, 12 Dec 1560 — (B) ciphertext-only break, read
Homophonic substitution with word division (Lasry had independently solved it in 2023, unpublished); 98.9% of 1,715 words read — a report on the Protestant rising in the Agenais after François II's death. **Open:** 16 scattered words, the writer's name.

### Walsingham letter-book ciphers, 1571–73 — (B) not solved (4 entries)
- **Walsingham → Burghley, Jun 1571:** nine-sign run `6174aH6HH` and codes [12], [E4] unread — too short, no key.
- **Burghley/Leicester ↔ Walsingham, Nov 1572:** codes [7], [9], H and a nine-sign letter run unread ([3] = the Queen by context).
- **Walsingham → Burghley, 20 Jan 1572/3:** a six-sign port name in a clear letter; Dieppe/Calais/Nantes all possible.
- **Burghley → Walsingham, 5 Jul 1572:** codes [2], [4], [5], a monogram, A, F unread ([3] = the French King by context).

### Desiderio l'Abbé → Duke of Nevers, Prague/Breslau, 1577 — (B) not solved
834 + 77 digits inventoried; grouping/null searches fail. A clear reference to a 24 Feb cipher dispatch points to earlier correspondence (fr. 4695 no. 51), still uninspected.

### "L'Estat du Roy de Navarre", after 1580 — (B) ciphertext-only break, read
Homophonic alphabet of ~50 graphic signs; the letter *m* was a dot-group taken for punctuation — that misread blocked every earlier attempt. French memoir on Navarre's party, 95% read. **Open:** ten nomenclator numbers.

### Henry of Navarre → Ségur, 1585–86 — (B) ciphertext-only break, read
Figure-cipher letters to the envoy raising a German army (Lasry independently solved, unpublished); alphabetical syllabary, 97% on a matched control. **Open:** word-signs partly glossed.

### Anonymous ("MR") → duc de Mercœur, c.1586 — (B) not solved
Six cipher runs in clear French, 217 signs of 55 kinds (Greek letters, shapes, digits). Homophonic annealing scores no better than a shuffled control; not Lasry's 2022 fr.15564 key.

### Louis de Gonzague, duc de Nevers → La Vieuville, 30 Sept 1587 — (B) not solved
A Nevers key (fr. 3995 no. 76) fits the code numbers but the cipher runs (33 signs) give no French. Blocked on a colour scan or the original (B/W microfilm ~30–40% legible).

### Charles III, duke of Lorraine → comte de Vaudémont, 18 Jun 1592 — (B) ciphertext-only break, read
Independent re-solution (Tomokiyo read it 2025); reciprocal letter-pair substitution with syllable/word figures; 76.6% measured. **Open:** ~60 tokens in unkeyed special signs, ten single figures, three garbled runs.

### Dinteville (Langres) → Duke of Nevers, 3 Jul 1592 — (B) not solved
Two cipher passages; the sibling leaf's interlinear decipherment fits no one-sign-one-letter key (code signs likely). Needs a careful sign transcription of ff. 128 and 130.

### Thomas Edmondes → Burghley, at Henri IV's court, 1593–94 — (B) ciphertext-only break, read
Independent re-solution of Butler's 1913 break; simple substitution with homophones and person signs broken from clear context; 98.8% of signs read. **Open:** the person signs 9, n, £, and one sign on f. 109v.

### Nevers → Villeroy, Saint-Quentin, 16 Aug 1595 — (B) not solved
17 runs, 753 signs of figures and Greek-like signs; no key in Nevers's collection (same-sign-family keys have other values). Control experiments show a syllabic model fails at this length — likely a nomenclator with syllables/word codes whose marks the copyist dropped.

### Matheo de Segura → Constable of Castile, Madrid, 8 Aug 1596 — (B) ciphertext-only break, read
Homophonic key rebuilt by annealing and image resegmentation; 95.2% of tokens — the world ending or the king dying by September. **Open:** six tentative assignments; no independent key.

### Ferdinand of Bavaria, Elector of Cologne → Duke Maximilian I, Bonn, 22 Dec 1619 — (B) ciphertext-only break, read
Homophonic substitution on even two-digit figures + three-digit nomenclator, annealed from ciphertext alone; 95.8% — troop quartering, levies, the argument Catholics must act. Sibling R9425 read unchanged with the same key. **Open:** 31 of 32 nomenclator groups, three names, four words.

### Warsaw → Bishop of Olmütz (?), 24 Dec 1627 — (B) ciphertext-only break, read
Homophonic substitution with letter pairs, syllables, word codes and nulls; 95.2% — the writer presses for a canonry of Olmütz for a Queen of Poland's son. **Open:** ten word codes and two small groups glossed from context only.

### Sir Simonds D'Ewes's private cipher log, 1635–36 — (B) ciphertext-only break, read
D'Ewes's invented alphabet, simple substitution of Latin, rebuilt by crib (convulsio, plena luna); 96.5% — his son Clopton's convulsion fits. **Open:** trimmed last line, one word of l. 13, a faint phrase.

### Unknown writer → Hesse-Kassel, undated — (B) ciphertext-only break, read
Digit-and-sign letter substitution, annealed and confirmed by the contemporary gloss; ~97% read. **Open:** nine signs at the end of line 1 under the faded gloss.

### Rohan papers / Louis XIII & Châtillon letters, BnF, 1635–36 — (B) not solved
Cipher blocks in clear prose (incl. the king's Valtellina force estimate, Châtillon's Schenkenschans account) lack a verified key; some leaves lie beyond the Gallica scan.

### Otto von der Malsburg → Landgrave Wilhelm V, Westphalia, 1637 — (B) ciphertext-only break, read
German homophonic table (89 two-digit groups) annealed from ciphertext alone; 95.9% of 9,736 groups — unpaid garrisons, Ehrenbreitstein, the Cologne peace talks, the Dutch alliance. A separate ten-line alphabetic block now has a period-five key (Larry Beck, via ChatGPT). **Open:** ~40 numerical code groups, some alphabetic groups.

### Archduke Leopold Wilhelm → baron de Mercy, Barneton, 6 Jun 1648 — (B) ciphertext-only break, read
Homophonic substitution in clear Spanish, key recovered ciphertext-only by NoAutopilot; 98.5% — Mercy to go to Cleves about raising 3,000 infantry. **Open:** code 15 (eight tokens) and letters lost at the trimmed edge.

### Unknown writer → "Monsieur", Nancy, December (17th c.) — (B) ciphertext-only break, read
Homophonic pigpen cipher (the pencil key on the flap reads nothing); 95.6% reads as French — an envoy to congratulate His Majesty's recovery. **Open:** stretches under blots and a stain, 14 name signs, sender/recipient/year.

### Niccolò Guidi di Bagno (Paris) → Secretariat of State (Rome), 5 Jan 1652 — (B) not solved
Four pages of unseparated decimal cipher in Italian; Lasry's Francia 346 key structurally excluded. No transcript, clear copy, edition, or matching sibling found. Needs a manual double-pass transcription and the 1652 Paris nunciature key.

### Abraham Cowley's hand ("Mr. Cowleys Hand"), Paris, 1652–53 — (B) in progress
Two clear English letters from the Queen's court with 23 unread code numbers (names, a place; 248:88:46:47:96:52:7:57 perhaps "Scotland"). Too few for ciphertext-only; needs a Jermyn/Queen key of 1652–53.

### Ferenc Wesselényi, Palatine of Hungary → King Leopold I, c.1663–64 — (B) ciphertext-only break, read
Reversed alphabet (24 = a … 3 = x) with vowel homophones; 98.8% — regiments to join, 2,000 foot, a garrison to take by force. **Open:** codes 60 (a general, perhaps de Souches) and 64 (a place).

### Desmarets → unnamed correspondent, Marly, 4 June 1710 — (B) not solved
471 groups of a ~570-value numerical code; the French between the figures is clear prose on Geertruidenberg, not a decipherment. No key on DECODE or in print.

### Potocka and Mniszech → Jakub Dunin, 1714–16 — (B) ciphertext-only break, read
Potocka's alphabet broken from a Polish postscript and transferred to eight French letters (with doubled homophones); 97.3% of tokens valued — property, court influence, correspondence security. **Open:** four person codes, figure 73, doubtful spellings; Mniszech's R7524 unread (75.5% coverage with her letters included).

### Paris 1719 and Carré 1742–45 code letters — (B) not solved
A codebreaker's file: the 1719 Paris letters are a two-part 3-figure code with ~12 contemporary glosses (354 groups); the Carré letters (1,323 groups, 381 distinct) test as a two-part code of ~800 entries with no gloss or crib — ciphertext-only closed.

### Palm → Starhemberg / Visconti, London, 1727 — (B) in progress
R7927 = German letter, 14 homophonic+nomenclator passages (162 tokens) with glosses 33=e, 23=n etc.; Windischgrätz key doesn't fit; 5-gram annealing failed. Needs Palm's key or the clear copy.

### Unknown sender → unknown recipient, 1728 — (B) in progress
One page of 205 invented cursive signs (IoC 1.07 — not simple substitution); mono, Vigenère and Quagmire-type anneals failed. Needs the key or sibling letters.

### Military news for Prince Carl August Friedrich of Waldeck, HStAM, 1744 — (B) not solved
717 three-digit groups (303 distinct) of a two-part homophonic nomenclator; ciphertext-only declared closed (true key scores below gibberish keys on a matched control). Blocked on a key in undigitised 118 a Nr. 1973–1980.

### Hellen → Frederick II, 1752–63 — (B) in progress
Investigation open; transcription parser audited, a repeated passage confirmed on the manuscript. Fagel 5206 lists deciphered 1752–53 letters, but no matching text or key has been verified.

### Johann Heinrich Kauderbach → Brühl / Friedrich August II, The Hague, 1754–56 — (B) ciphertext-only break, read
Ten intercepted despatches, one key for all; a one-to-one anneal onto Kauderbach's 1761 Dresden key converged. All ten read 65–97%: the Dutch augmentation debate, the Saxon subsidy treaty, the Treaty of Versailles (May 1756). **Open:** clear sigla, four rare codes, R1954 (weak transcription).

### Gottfried van Swieten → Count Cobenzl, 1757–59 — (B) ciphertext-only break, read
The 1759 letters' table (100–442) rebuilt ciphertext-only against a French LM; 96% of 553 groups — the Gueldre convention, Soubise's army, complaints against Count Pergen. **Open:** ~21 groups, mostly names.

### Van Dedem → Van de Spiegel / Van der Goes, Constantinople, 1788–99 — (B) in progress
R2122 (258 groups) and R2131 (50) use one homophonic word code; cribs cover only ~55% of groups and don't align to a consistent key; R1895 (1799) is a different system.

### An Orange prince (son of William V) → a Dutch émigré officer, Germany, 1795 — (B) ciphertext-only break, read
A 6×6 digit square broken ciphertext-only (Lasry independently solved in 2021, unpublished); 95.2% — General Dundas, pay, embarkation into British service; writer identified as Prince Frederick. **Open:** recurring word signs in the Dutch postscript.

### Dirk van Hogendorp → Van der Goes, St Petersburg, 5 Jul 1803 — (B) not solved
Subject identified (Hogendorp's approach to Chancellor Vorontsov via Suchtelen) and the matching 1803 Russian-legation codebook (R1035, 1,849 entries) found on DECODE. **Open:** exact superposed marks and a group-by-group reading of all 286 groups.

### Lodewijk van Toulon → Dirk van Hogendorp, The Hague → St Petersburg, 30 Jul 1803 — (B) not solved
Croiset's six-series Correspondentiecijffer survives only undigitised (NA 2.21.045/34313); the 1801 solutions fix 3 of 67 words. Needs the codebook.

### Robert Fagel → William V, The Hague, 18 Jun 1804 — (B) in progress
128 groups of a French numerical nomenclator to at least 2510, in the 1804 Orange compensation talks. Grand Chiffre and all KHA/Fagel/BL/Uppsala keys ruled out. Most likely in undigitised KHA A31-902 (archive request drafted).

### Van Spaen → Van der Goes, Düsseldorf, Jan 1808 — (B) in progress
Letter (228 groups) and annex (75) of a plain numerical code to at least 1339; no DECODE key; not the Dedem, Spaen-1801, or Fagel-1804 codes. Needs the annex reading or the commission's code.

### Roell (?) → Van Dedem, Amsterdam → Constantinople, 9 Feb 1809 — (B) in progress
Two unsigned letters, 13 pages, 2,585 groups of a heavily homophonic code to ~3,300 (no group above 1%). No decipherment on the scans; no key on DECODE or in Roell's papers.

### Zeschau → Seebach, Dresden → St Petersburg, 1841–43 — (B) not solved
3,969 unseparated digits of R5005 transcribed; a rubbed-out pencil decipherment shows a two-digit syllabary (11=la, 70=pre, 82=m…). No 1840s Saxon key on DECODE; annealers fail. Needs the key, UV imaging of the pencil, or R5006–R5008 transcribed.

### Cardinal Soglia → nuncio Viale Prelà, Innsbruck, 1848 — (B) ciphertext-only break, read
64-cell two-digit table with 8XXX = one-part code in alphabetical order; a counter-order to stay with the Emperor and suspend the passport request. **Open:** 11 code groups (incl. the date of the earlier letter).

### Swatow telegram to Sun Yat-sen, 1916 — (B) ciphertext-only break, read
Systematic code condenser over the standard telegraph code recovered by brute force; 41 of ~44 characters read.

### Sun Yat-sen's intercepted telegrams, 1916–17 — (B) ciphertext-only break, read
~60 condenser telegrams read under seven Swatow-family keys (Sun ↔ Yamada, Chen Qimei, Qingdao, Manila, San Francisco, Dai Jitao 1917) plus the Hankow +111 digit code; incl. Chen Qimei's assassination as reported to Tokyo. **Open:** Sun's six-vowel 文密 code.

## From the cryptiana page (C), in page order

### Serno Gilino's Cipher with Superscript Digits, 15 Sept 1527 — (C) unsolved
An undeciphered Latin letter; most superscript numerals are two-digit numbers. Same family as the Bishop of Worcester's cipher (one of whose letters also remains unsolved).

### Nicholas Throckmorton (1559) / John Wod (1568) — (C) partly unsolved
BL Add MS 4136: three ciphers reconstructed, but two remain unidentified — the marginal ciphertext on DECRYPT no.2988 (Throckmorton to Elizabeth, 10 Jul 1559, ~half a page, in a different cipher) and the John Wod ciphertext on the no.2989 sheet (Throckmorton to Cecil, 8 Aug 1559).

### More Undeciphered Letters Related to Mary, Queen of Scots (1581) — (C) partly unsolved
SP53/11 no.50: Walsingham's letter to his codebreaker John Somers (21 Jul 1581) encloses a letter in cipher found in Mary's intercepted mail — the enclosure (no.50I) is entirely in cipher and undeciphered. (Some other SP53 ciphertexts turned out to match plaintexts in the same volume, so there's hope the plaintext sits nearby in the archive.)

### SP53/16 no.78 (1585?) — (C) unsolved
Anonymous cipher letter to Mr. Tempest, an English priest in Paris; cleartext lines in French; endorsed by Phelippes. Not deciphered.

### SP53/16 no.79 (1585?) — (C) unsolved
Another anonymous cipher letter in the same hand (copyist's?) as no.78, addressed to Doctor Barret, President of the English seminary at Rheims. Endorsed. Not deciphered.

### SP53/22 f.52 — (C) unsolved
Short undeciphered ciphertext endorsed "Cifer with[?] Spanish Spye" in a collection of Mary-Queen-of-Scots ciphers (starts 6b;4b;8b;8b;5;10b;7b;4;…). The verso of the f.40 cipher key also carries a short undeciphered ciphertext.

### Ciphers related to Sir Francis Walsingham — (C) partly unsolved
Ciphertext in a letter from Robert Bowes (1583) and in one from William Davison (1584) remain undeciphered.

### Postscript to King Ferdinand's Letter to his Ambassador in Rome, 31 Aug 1498 — (C) unsolved
Parisi (2004) deciphered the letter to Garcilaso de la Vega, but the last ten lines are in a different cipher and remain undeciphered. Galende Díaz (1994) mentions a cipher of Garcilaso de la Vega in the archives.

### Spanish Letters, BnF Espagnol 318 (1497–1504) — (C) partly unsolved
Ff.5–6 and f.116 use known ciphers; three letters are in unknown ciphers. Lasry gave an approximate solution for f.122 no.95 (8 Jan 1497) in 2022. Still open: f.120–121 no.94 (Viceroy of Sicily to Ferdinand, 27 Apr 1503) and f.118 no.93 (Lorenzo Suarez to Ferdinand and Isabella, Venice, 24 Feb 1504).

### Hugo de Moncada to Charles V, 6 Oct 1524 — (C) unsolved
Letter from the Viceroy of Naples (BNE, Carta 9) in cipher; a later marginal hand notes "Decifrada en …" but the decipherment hasn't been located.

### Simancas, EST,LEG,1381,180 (1551) — (C) unsolved
Undeciphered 1551 letter (PARES); the recovered/deciphered portions reference copies of enciphered letters ("Copia do loque Su Magestad scrive a [Principe] Doria a v de setienbre presinte", "Al seno Ferando", "Al enbaxador Figueroa").

### Earliest French Ciphers (1526–1530) — (C) mostly solved, one unsolved
The earliest known specimen of ciphertext in France is still unsolved; others from Francis I's reign were broken 2021–2026 (Calvimont–Duprat, Gramont Bishop of Tarbe, two from BnF Clair.331 by Bourdeau with Claude, one by Vander Galien with Codex/Claude).

### Catherine de Medicis to Philibert du Croc, 27 Apr 1567 — (C) unsolved
Letter partly in cipher, reproduced in Destray (1924), *Un diplomate français du XVIe siècle* (Gallica, p.53). The clear lead-in: "jay recu du s…".

### Lodovico Birago to Duke of Nevers, 1570–72 — (C) partly unsolved
BnF fr. 3251 letters; some read with reconstructed keys, but some remain unreadable with any reconstructed key (transcription includes diacritic-marked digits).

### Blancmesnil to Duke of Nevers, "cer dernier juin" (BnF fr.3633 f.24) — (C) unsolved
Letter from Nicolas Potier de Blancmesnil with some phrases in cipher.

### Marie de Medici's Cipher (1610) — (C) unsolved
Short passages in cipher in letters from Regent Marie de Medici to M. de Breves appear unsolved.

### French (or Italian) Ciphers, c.1590 — (C) almost solved
BnF fr.4715: many undeciphered letters, most broken at least partially — three remain unsolved "despite their seeming simplicity" (one, no.61=f.84, was solved by Lasry in 2020). BnF fr.4712 also holds undeciphered letters.

### Ciphertexts Left Undeciphered by François Viète (1593–1594) — (C) one of two unsolved
Cinq Cents de Colbert 33 holds original letters Viète never broke. Senecey to the Archbishop of Lyon (f.555) was solved by Lasry (2020). Still open: Cardinal de Joyeuse to Villars, admiral de France, Rome, 15 Feb 1594 (f.539).

### Cocquet's Cipher, Rome, 13? Nov 1616 — (C) unsolved
BnF Clair. 369 f.316: partially enciphered letter from Cocquet to Mangot.

### Fragments in a Novel Cipher Invented by a Milanese — (C) almost solved?
Ms. 994 of the National Library, Madrid: ciphertexts broken by Luis Valle de la Cerda with a scheme invented by the Milanese Jerónimo Sertori — but Valle's solution is not extant. (Eloy Caballero got close in 2012 per Nick Pelling's blog.)

### King of Hungary and Bohemia (future Ferdinand III) — (C) unsolved
Letter of future Emperor Ferdinand III to Trauttmansdorff, 13 Nov 1634, not deciphered (SOA Pilsen, Trauttmansdorff archive, carton 6, i.no.68). The only enciphered letter between them in the archive — the cleartext suggests an important matter.

### More Ciphers of Ferdinand III? — (C) unsolved
DECODE R1579 (Emperor Ferdinand III, 1640): besides the Ernst-solved 20 Jul 1640 letter (images I7064–I7065), the record holds unsolved items — image I7060 (two-/three-digit and two-/three-letter codes; cleartext German, ciphertext may mix Latin), I7066 (blocks in a simple symbol cipher), I7068 (negative image, longer text in a similar cipher).

### Ferdinand III ↔ Cardinal-Infante Ferdinand of Austria (1634, 1635, 1640) — (C) two of three solved
Brussels archives; cleartext in Latin. One of the three letters (an old-style cipher with graphic symbols and three-letter codes, vs. the two newer two-digit-code letters) remains unsolved.

### Variable-length Figure Code in Austrian Archives (1644, 1627) — (C) two of three solved
DECODE R2159, R1408, R2179: Bourdeau solved R2159 and R1408 (Sept 2026); one ciphertext remains.

### Melchior de Sabran (1631–1635) — (C) mostly solved, one unsolved
Diplomat in Genoa; the author broke the 1632 Servien–Sabran cipher, Lasry solved Louis XIII's 1631 letter and the 1637 Farnese enclosure cipher. **Still unsolved:** short ciphered passages in a letter to "Mr de ch.g r", in a different cipher.

### Prince of Condé to Barrière, London, 15 Sept 1654 — (C) unsolved
Add MS 4200 f.98 (DECODE R8395) in cipher. Short ciphertext on f.101 (R8398) may not read with the known cipher — possibly yet another cipher.

### Colbert Correspondence (1665, 1673, 1674) — (C) partly unsolved
BnF Mélanges de Colbert: some letters read with reconstructed keys, but three passages still unsolved — (i) 172 f.23: Louis Béthune, Duke of Charost (1673), a short paragraph in unidentified cipher; (ii) 168bis f.553: abbé de Gravel to Comte de Maulevrier (1674), short cipher passages; (iii) 127 f.349: a few ciphered words (1665).

### An Unidentified Ormond-Arran Cipher, 24 Jan 1678 — (C) unsolved
Short undeciphered segments in a letter from Ormond to Arran (Ormonde MSS vol.4, p.93); the cipher looks similar to other Ormonde ciphers but seems different. Ormond's own words: "This is a trial whether you are skilful in deciphering, else it might have been written in plain letters."

### Private Cipher between Charles I and Henrietta-Maria (1645) — (C) unsolved
A passage of 8 April 1645 in the couple's private cipher appears to remain undeciphered.

### Charles I in the Isle of Wight (1648) — (C) two of four solved
Four enciphered letters from captivity; the cipher in two was solved by Biermann and Brown (2021); two letters remain unsolved.

### Prince Rupert's Cipher with His Brother Maurice (1645) — (C) unsolved
An encoded letter Rupert received from Maurice soon after the Battle of Naseby, printed in Warburton's *Memoirs of Prince Rupert* (p.133). Opens "By your cipher, you may observe, that 15 26 342 148 136 …".

### An Intercepted Royalist Letter, 21 May 1646 — (C) unsolved
BL Add MS 72438 f.9r (DECODE R8623), mostly clear with ciphered passages: "My lord your Lo^p being not a little beholding to 309 for y^e 500 44 66 24 …".

### An Intercepted Letter to Charles I, 13 May 1646 — (C) unsolved
BL Add MS 72438 f.10 (DECODE R8624). (A Thurloe State Papers vol.7 short intercepted letter also has undeciphered portions.)

### A Letter to Prince Rupert, The Hague, 6 Nov 1648 — (C) partly unsolved
BL Add MS 18982 ff.134–135 (DECODE R8447), William Craven, Baron Craven to Prince Rupert; most deciphered but undeciphered portions remain.

### Charles II to Duke of Hamilton (1650) — (C) unsolved
Some ciphered passages remain undeciphered; the key may lie in the collection of letters deciphered at the time.

### An Intercepted Letter of Hyde, 1 Nov 1659 — (C) unsolved
Add MS 4166 ff.92–93 (DECODE R4886), Edward Hyde letter with undeciphered portions.

### Dutch ciphers (1653) — (C) unsolved
Thurloe State Papers include undeciphered Dutch letters, e.g. Beverning and Vande Perre to ambassador Boreel at Paris, 1 Sept 1653.

### Intercepted Letters (1656) — (C) unsolved
Thurloe State Papers: e.g. an intercepted letter of du Gard in a letter to White, Brussels, 10 Jun 1656 NS; one from Brussels, 12 Aug 1656 NS; one from Jo. Waddall, 22 Aug 1656.

### French Cipher to Ambassador in Rome, 10 Jul 1690 — (C) unsolved
Louis XIV's instructions in code to the Duke of Chaulnes; discussion started on Klaus Schmeh's blog while the article was being written.

### French Ministers at Geertruidenberg (1710) — (C) unsolved
BL Add MS 61575 ff.38–41 (DECODE R8755): intercepted letter from foreign minister Torcy to French ministers at the Geertruidenberg peace talks.

### Marshal Villars to Abbé de Polignac, 1 Jun 1710 — (C) unsolved
BL Add MS 61575 f.44 (DECODE R8756): copy of a letter in cipher; Polignac was at Geertruidenberg.

### French Cipher Despatch of General Catinat, 15 Sept 1702 — (C) unsolved
A coded letter written by Marshal Catinat remains unsolved.

### French Code during the American Revolutionary War (1779) — (C) unsolved
Encoded letter from Admiral D'Estaing to Gérard, French minister in Philadelphia, 30 Apr 1779 (Clements Library, Clinton Papers): "A bord du Languedoc En rade du Fort Royal de la Martinique … 240 318 401 367 211 382 …".

### George Stepney to Earl of Manchester, Vienna, 23 Mar 1702 — (C) unsolved
A short ciphertext in the Manchester Papers ("… 836 468 445 242 / 233 55 44 370 30 325 576 246 …"); other Manchester-Papers letters read with the key (THE=454) kept with them; Bourdeau deciphered two 1699 letters.

### A Dictionary Code Used by Confederate Navy during the Civil War (1863) — (C) unsolved
Encoded letter from Lt. Barney (CSS Harriet Lane) to Mallory, Secretary of State, 19 Mar 1863: "(177)-2-16- the (216)-1-15-(113)-3-85- …". The dictionary is said to be a Webster's — the right edition hasn't been found (contrast the Johnston–Lee 1862 dictionary code, broken once the dictionary was identified).

### A Diplomatic Telegram from British Consulate in Africa (1911) — (C) unsolved
Encoded telegram from the British consulate in Lüderitz (then German South-West Africa).

### Telegrams Related to Sun Yat-Sen in Wen Mi (文密) (1916) — (C) partly unsolved
After the Swatow telegram's condenser was broken, Bourdeau found more telegrams on similar condensers — but Sun's six-vowel 文密 code is still open.

### German Diplomatic Codes during WWI — (C) unsolved
Van Kampen & Lasry's *Cryptologia* survey: dozens of messages from/to the military attaché in Madrid (RMA 5/2409–2417, German military archives) were never deciphered nor matched to documented plaintexts.

### Telegrams Found in a Sunken Ship Zhongshan (ca.1938) — (C) partly unsolved
In 2008 the Zhongshan Warship Museum called for solutions to encrypted telegrams found in SS Zhongshan (sunk by Japanese bombing, 1938); as of 2009, 352 of 891 were solved. The author hasn't located the primary sources.

### A Telegram from Switzerland, 8 Jan 1937 — (C) unsolved
Two encrypted telegrams Switzerland→London (posted on Klaus Schmeh's Facebook page), both beginning "BLUME SALAMANCA" followed by five-letter groups. IC matches English — possibly a transposition; a codebook may have been used.

### Another Enigma Message (1945) — (C) unsolved
A *photo* of an unsolved Enigma message sent 10 Jan 1945 by a deputy of "Oberbefehlshaber Oberrhein" (Supreme Commander of Upper Rhine). (Cited via Klaus Schmeh's blog; Weierud's CryptoCellar lists further messages, three of which were solved with AI in 2026.)

## Verdicts worth noting (not unsolved — author says not-a-cipher)

### Chinese gold bar cryptograms, Shanghai, 1933 — (B) "not a cipher or not reachable"
Almost exactly ten of every letter — flatter than any cipher of real text can be. Verdict: no message. (Famous on Elonka Dunin's list; the page excludes it as a cipher.)

### Roosevelt cryptogram, number block, 1935 — (B) "not a cipher or not reachable"
A permutation of 1–52 padded with zeros; statistics match a hand-written list, and testable ordered-key readings fail where matched controls succeed. Verdict: no message (Ernst's 2017 "doodle" claim confirmed).
