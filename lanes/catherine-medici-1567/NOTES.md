# Living notes — Catherine de Medicis -> Philibert du Croc, 27 Apr 1567

## Objective
Recover the plaintext of the ~150-token cipher passage (5.5 manuscript lines + 1 inline nomenclator glyph) in Catherine de Medicis' 27 April 1567 letter to du Croc; "cracked" = a French reading consistent with the 1567 Scots/English diplomatic context, verified against the plate image byte-for-byte.

## Methodology log
- 2026-10-07: ARK hunt. Gallica SRU via curl returned "Access Denied: 403"
  (/tmp/sru1.xml, 34 bytes); /services/engine/search/sru returned the Gallica
  security-check page (attempt 2); plain /Search?q=... returned the homepage
  with no results (attempt 3). All three curl attempts to gallica.bnf.fr search
  endpoints blocked — recorded as null (see Null results). Fell back to public
  web: cryptiana.web.fc2.com/code/unsolved.htm line 254 gives the Gallica link
  https://gallica.bnf.fr/ark:/12148/bpt6k932364m/f86.item.r=Paul%20destray for
  Destray (1924). ARK = ark:/12148/bpt6k932364m, confirmed on two entries
  (Catherine letter p.53; Charles IX letter p.80).
- 2026-10-07: IIIF fetch. Downloaded
  https://gallica.bnf.fr/iiif/ark:/12148/bpt6k932364m/f<N>/full/full/0/native.jpg
  for N=56..62 via curl. Viewed each: f57 = printed p.53 (letter XXI, the du
  Croc letter, "J'ay receu du sr [chiffres] lectres en datte"); f58 = printed
  p.54; f60 = printed p.56 (Smyth/Calais text); f61 = unnumbered photographic
  plate of the ORIGINAL dispatch between printed pp.56-57, captioned "XXI. —
  1567, 27 Avril. Lettre, en partie chiffrée, de Catherine de Médicis à du
  Croc." showing the manuscript with 5 full cipher lines + 1 short cipher row
  + 1 inline cipher glyph; f62 = blank (plate verso). Scan offset = printed+4.
- 2026-10-07: Transcription. Full-res plate (3328x4796) inspected with 2x-4x
  crops of every cipher line (/tmp/ln/*.png). Cipher -> 
  data/medici-1567-cipher.txt (verbatim + normalized ASCII, 150 tokens,
  40 distinct glyphs incl. inline X). Cleartext (printed p.53) ->
  data/medici-1567-clear.txt. Manuscript variants noted (e.g. "Fay receu du
  srs [X] lettres en datte"; closing "pour avoir en sa saincte garde" vs
  printed "vous avoir en sa saincte garde").
- 2026-10-07: Cipher assessment. Symbol set = Latin letters (upper+lower),
  digits 6/7, plus signs, and ~12 special glyphs (long-s, struck-f, 2beta
  ligature, epsilon, phi, xi, etc.) — a monoalphabetic/nomenclator-style
  system with probable homophones (40 symbols for a French plaintext).
  150 tokens total.
- 2026-10-07: Built code/anneal.py (from scratch): French quadgram
  log-likelihood model from Project Gutenberg ebook 17489 (Hugo, Les
  Misérables Tome I: Fantine, French; data/gutenberg-17489-miserables1.txt,
  710496 bytes) -> data/french-quadgrams.json (28293 distinct quads, 512933
  corpus chars). Simulated annealing over symbol->letter keys (many-to-one
  allowed), 25 restarts x 40000 iters = 1,000,000 steps, seed 15670427.
- 2026-10-07: Cross-reference. cryptiana.web.fc2.com/code/henryiii.htm and
  GL.htm document George Lasry's 2022 solution of the Charles IX -> du Croc
  cipher (same book, Destray p.80, same correspondent/period) with interlinear
  decipherment images (GL/GL_CharlesIX_decipher.png). Symbol repertoire looks
  similar (letters+digits+symbols). Key table not yet extracted — lead for a
  keyed attack (see Findings/next).
- 2026-10-07: Key-table extraction (keyed attack work order). No explicit key
  table exists in Lasry's images — the table had to be derived from the
  interlinear alignment (black cipher glyphs vs red plaintext letters).
  Method: connected-component segmentation of black glyphs per row
  (scipy.ndimage.label), enlarged strips (/tmp/vN_strip.png, /tmp/rN_strip.png),
  red plaintext read from 3x-8x crops; pairing by vertical column alignment.
  Pairing direction PROVEN as red-ABOVE <-> black-BELOW by the "≠1"->"QUE"
  nomenclator anchor (verso row 0: small red "Que" sits directly above black
  "≠"+"1", crops /tmp/v0_que_anchor.png, /tmp/v0_start.png). Recto assumed same
  by construction symmetry + glyph-count argument (B0=36 glyphs vs R00=41
  letters with nomenclators vs R01=47 letters).
  Result: 7 CERTAIN mappings with direct visual-alignment evidence:
  {#->I, 6->A, 7->R, +->O, h->E, B->D, Y->S} (Y=Catherine xi-like assumed =
  Charles IX xi by shape description). Evidence details in
  data/charlesIX-key-table.json and data/interlinear-workbook.md.
  CONFLICTS found (marked uncertain, not applied): x->{N,E,M} (3 visual obs,
  likely multiple similar x-like glyphs conflated); alpha->{O,D} (2 visual
  obs); 9c->D vs 9->null (may be distinct glyphs). Full per-row workbook in
  data/interlinear-workbook.md (verso row 0 fully paired, 19 high-confidence
  pairs; remainder sequential with uncertainty flags).
- 2026-10-07: ARCHIVAL KEY HUNT (work order). Searched three routes for period Catherine/Charles IX cipher keys:
  (a) cryptiana.web.fc2.com/code/henryiii.htm (Shift_JIS, decoded with iconv) — HIT. Tomokiyo's article "Ciphers during the reigns of Charles IX (1560-1574) and Henry III (1574-1589)" contains RECONSTRUCTED key tables: Bishop of Rennes cipher (1561-1564), BnF Colbert 390 ("contains many letters partially in cipher"; Tomokiyo: "The King and Queen Mother used the same ciphers as far as the specimens here are concerned"); Villeparisis cipher (1564), BnF fr.16039 ("cipher letters from Rome to Charles IX and Queen Mother, Catherine de Medici"); Bishop of Mans cipher (1569), BnF fr.16039; La Forest-du Croc cipher (1567). Key-table images fetched via curl to data/cryptiana-key-images/: CharlesIX_Rennes.png (119320 B, sha256 4b23764c797fd7d47135b31b37d119ba0d972e44dda4747a7c3ce10879c6d841), CharlesIX_Rennes2.png (45146 B, a5cce4e417a4919c47e140ed6dff439792b9359ee07c137e7c205d1e8b621df8), CharlesIX_Villeparisis.png (69037 B, 27cf1314c8acc1fe27baad407dca312bdd3326e6ad507ef3e14eab7dcaf2437e), CharlesIX_Mans.png (81238 B, c3bef8e913ea6ac37c503d816dcace0208029a6e88da9dc8f3afc64fc10355ed), CharlesIX_Catherine.png (251619 B, de13b6af0d0c259d41849d4670885a98af16fbf962e2fa19651c043bc055b01d; the cipher manuscript photo itself, NOT a key), CharlesIX_duCroc.png (376419 B, d0840cbb0f9401e50c1e11b32e3de243bfb9a1e3b24c4805ac8162298068ae76; La Forest-du Croc key table). Retrieved 2026-10-07 via curl (Mozilla UA) from https://cryptiana.web.fc2.com/code/<name>.png.
  (b) DECODE database (de-crypt.org) — HIT. Keyword search works via GET /decrypt-web/RecordsList?cmd=search&search=... Record 2788 = THIS cipher: "Catherine_de_Medicis_to_Philibert_du_Croc", 27 Apr 1567, Saint-Maur, Status: Non-decrypted, Access: Public. Public thumbnail fetched: https://de-crypt.org/decrypt-custom/filesrv/?file=TH_IMG_R2788_I17353_P.png -> data/decode-r2788-thumb.png (200x313, 60528 B, sha256 13af31458fbac0efe37632675957dc19df5e609e35bf9c0112bd3b7f6d6ba79a); shows the same letter/cipher plate, too small for transcription. Full ImagesList endpoint 302-redirects (auth wall); not pursued. No DECODE record holds the Colbert 390 / fr.16039 key tables (search matched record IDs, not shelfmarks).
  (c) Web search for "Colbert 390" / "fr.16039" + chiffre/cipher — no key tables surfaced (results were generic crypto-history pages).
  Gallica SRU: ZERO new attempts this session (null already recorded; work order capped retries at 1).
- 2026-10-07: Transcribed the Rennes (Colbert 390) alphabet row 1 from 3x/4x crops (data/cryptiana-key-images/rennes_alpha_L/R.png, rennes_row_A/B/C.png). 22 row-1 glyphs counted against 22 headers (a b c d e f g h i l m n o p q r s t u x y z; no j,k,v,w) -> data/archival-key-colbert390.json: 18 certain single-plain mappings (z->a, h->b, d->e, a->g, 6->l, D->m, g->n, l->o, b->p, G->t, 7->y, etc.), 2 certain-ambiguous homophone pairs (3->{c,s}, 4->{f,x}), homophone rows + nulls table recorded as uncertain. Word/nomenclator pink rows NOT transcribed.
- 2026-10-07: Transcribed the Villeparisis (fr.16039) alphabet row 1 from 3x crop (villep_alpha3x.png): 21 row-1 glyphs + z-column off-crop -> data/archival-key-fr16039.json: 13 certain single-plain (w->a, d->h, z->i, x->n, p->s, f->u, 7->q, etc.), 1 certain-ambiguous (m->{c,y}).
- 2026-10-07: Nomenclator transcription (work order). Transcribed the pink
  word/nomenclator rows of both archival key tables from the fetched images at
  4x-9x zoom (session crops in /tmp/nom/, not archived):
  Rennes/Colbert 390 (CharlesIX_Rennes.png, 517x322): 26 entries — row 1
  (13 words: bien com con dit ent est et faict faire la le lettre luy),
  row 2 (12: mais nous ont par plus puis quant que qui si vous votre?),
  row 3 (single cell: "l'Empereur Roy de Boheme" -> 2 glyphs e+v, unpaired).
  20 certain / 6 uncertain. Villeparisis/fr.16039
  (CharlesIX_Villeparisis.png, 476x228): 21 entries — row 1 (12: con dit?
  de(s) du l'empereur en et espagne faire faict il(s) le(s)), row 2 (9: par
  parler pour que quelle qui si? votre majeste). 17 certain / 3 uncertain /
  1 null ("majeste" cell verified EMPTY at 7x — reconstruction gap, not
  missing data). Pairing by left-to-right column order; word/glyph counts
  match per band (13/13, 12/12, 12/12, 8+null/9). Stored as "nomenclature"
  lists in data/archival-key-colbert390.json (sha256 now
  54212a939754b63c28a3cd2b03f3b5538a95fb03c4bdec4d2d8b549f3aa0fabf)
  and data/archival-key-fr16039.json (sha256 now
  90a4dabc144cb901a6ae2f51d2265f4ac3bba5e1cb8927d3a19e5ae608c757ea);
  alphabet mappings untouched. New applier code/apply_nomenclator.py
  (6824 bytes, sha256 995648066e15070bbd34ddb4e043a9b5ae607dfe94e2faa901d494cc68706159;
  NEW script — apply_archival_key.py left untouched so attempts 2/3 stay
  reproducible): pass 1 = certain nomenclature bigrams {word} on the raw
  stream (documented precedence: nomenclator words beat alphabet spelling),
  pass 2 = certain alphabet letters, pass 3 = certain nomenclature singletons
  {word}. Uncertain/ambiguous/null never applied.
- 2026-10-07: Full-key applies. Rennes ->
  data/keyed-attempt4-rennes-full.txt (2259 bytes, sha256
  97f9815946a173a275e70b7724d0e226d52a242dcc0004bca82f9ad208cd6576):
  70/150 tokens (46.7%) decoded — alphabet 43 + nomenclature singletons
  {est} (19x, cipher '#'), {mais} (3x, 'A'), {vous} (3x, '<'), {votre?} (1x,
  '+') + 1 bigram hit {par} ("a t"). Villeparisis ->
  data/keyed-attempt5-villeparisis-full.txt (2213 bytes, sha256
  5ad3a0b532ab167b535843063de0da49bc1430540d391665ab9afb7c3a2018f2):
  57/150 tokens (38.0%) — alphabet 38 + {dit?} (19x, cipher '#'); no bigram
  hits. ASSESSMENT: no French emerges in either (see Null results).
- 2026-10-07: Archival keyed applies (code/apply_archival_key.py, certain single-plain mappings only; ambiguous/uncertain never applied):
  Rennes -> data/keyed-attempt2-rennes.txt: 43/150 tokens decoded (28.7%). ASSESSMENT: no French emerges (best fragments L1 "...g m...n...n a", L5 "a...l a n...m...b...g t...a n l"; scattered letters, no words).
  Villeparisis -> data/keyed-attempt3-villeparisis.txt: 38/150 tokens decoded (25.3%). ASSESSMENT: no French emerges.
- 2026-10-07: Keyed apply (code/apply_key.py). Applied the 7 certain mappings
  to data/medici-1567-cipher.txt -> data/keyed-attempt1.txt. Coverage: 37/150
  tokens (24.7%). ASSESSMENT: no readable French emerges. Best stretches:
  L2 "...D E..." (D from B, E from h = "DE"), L5 "...E S I..." (E,S,I),
  scattered I/D/A/S/E/R/O do not form words; 75% bracketed. Verdict: PARTIAL /
  INCONCLUSIVE — coverage too low and conflicts unresolved to determine
  whether keys match or differ. Catherine's top glyphs p(11x), g(9x), z(9x),
  a(7x), o(7x), E(6x), f(6x) could not be mapped from examined rows.

## Null results
- Gallica search endpoints blocked to curl (3 attempts, 2026-10-07): (1) SRU
  https://gallica.bnf.fr/SRU?operation=searchRetrieve -> "Access Denied: 403
  Access Interdit" (34 bytes, /tmp/sru1.xml); (2)
  https://gallica.bnf.fr/services/engine/search/sru -> "Vérification de
  sécurité" anti-bot page (search2.html, 77818 bytes); (3)
  https://gallica.bnf.fr/Search?q=... -> homepage, no ARKs. IIIF image
  endpoint was NOT blocked (7 images fetched fine). ARK recovered via
  cryptiana instead; no page content invented.
- Blind anneal break FAILED (2026-10-07, data/anneal-run1-20261007.log):
  best score -527.70 (restart 6/25; range -527.70..-552.24), best key
  collapses 15+ cipher symbols onto E and the rest onto S/T/N/R — degenerate
  frequency collapse, plaintext guess is gibberish
  ("TSSEETEENTESENTNEESESENTRESSETEDEMENTEETEESENTREENESETENEETENENTEN...").
  No restart produced anything French-like. This is the expected outcome of
  the unicity math below: 150 tokens cannot pin a 40-symbol key.
- Keyed attack INCONCLUSIVE (2026-10-07, data/keyed-attempt1.txt): Charles IX
  key table extracted (7 certain mappings, data/charlesIX-key-table.json)
  applied to Catherine cipher: 37/150 tokens (24.7%) decoded, no French words
  emerge (best: L2 "D E", L5 "E S I"; rest brackets). NOT a proof the tables
  differ — coverage too low, and x/alpha conflicts show the manual
  transcription method is unreliable at this resolution. The key table is too
  partial to test the same-key hypothesis. Recorded as null (inconclusive),
  not as a negative on the hypothesis.
- Archival keyed attack NEGATIVE — Rennes/Colbert 390 key (2026-10-07,
  data/keyed-attempt2-rennes.txt): 18 certain row-1 mappings from
  data/archival-key-colbert390.json applied: 43/150 tokens (28.7%) decoded,
  no French emerges (scattered letters only). The Rennes key is the one
  Tomokiyo explicitly ties to Catherine ("The King and Queen Mother used the
  same ciphers"), so this is a genuine negative on the same-key hypothesis,
  with three supporting facts: (i) the cipher's top glyphs p(11x) and o(7x)
  (12% of all tokens) have NO mapping anywhere in the Rennes key table
  (row 1, homophone rows, or nulls); (ii) DIRECT CONFLICT with the lane's
  Lasry-derived table: Rennes row 1 maps cipher 'h'->plain 'b', the
  interlinear alignment gave cipher 'h'->plain 'E' (certain) — both cannot be
  the du Croc key; (iii) the cipher's #1 glyph '#' (19x) is only an uncertain
  homophone (q/r) in Rennes. Caveat: Tomokiyo's reconstruction is itself
  partial (word/nomenclator rows untranscribed), so this is a negative on the
  reconstructed key, not on the manuscript cipher system itself.
- Archival keyed attack NEGATIVE — Villeparisis/fr.16039 key (2026-10-07,
  data/keyed-attempt3-villeparisis.txt): 13 certain row-1 mappings from
  data/archival-key-fr16039.json applied: 38/150 tokens (25.3%) decoded, no
  French emerges. Glyph-inventory overlap only 8/40 (29.3% token coverage
  incl. uncertain); top glyphs g(9x), a(7x), o(7x), E(6x) have no mapping in
  the key. Negative on the Villeparisis-key hypothesis (letters to Charles IX
  AND Catherine, 1564).
- Archival FULL-key attacks NEGATIVE, STRENGTHENED (2026-10-07): with the
  nomenclator rows transcribed and applied (certain entries only),
  Rennes -> data/keyed-attempt4-rennes-full.txt: 70/150 tokens (46.7%)
  decoded, no French emerges. Best stretches: L1
  "{par} [t] [e] [J] [r] {est} {est} [p] g m [E] [q] [p] [o] [B] {mais} n
  [E] [V] [f] [x] [B] a [n] {est} [F] [E] n a"; L5
  "a {est} [c] {est} [o] l a n {vous} m [q] [p] [x] [V] b [Y] {est} g t [B]
  a [n] l [E] {est} [B] [!] [x]" — word tokens {est}/{mais}/{vous}/{par}
  sit inside alphabet-decoded gibberish; no French words form around them.
  Villeparisis -> data/keyed-attempt5-villeparisis-full.txt: 57/150 tokens
  (38.0%) decoded, no French emerges. Best: L4
  "[D] {dit?} s [o] [Y] [!] [e] s [q] h [+] s [a] [g] [b] {dit?} h [!] s
  [o] [D] [o] {dit?} [E] n [<] i [n] [g]"; L6 "[a] {dit?} s [e] q [A] [K] i".
  The nomenclator rows do NOT rescue either key: the #1 cipher glyph '#'
  (19x) now maps to a word ({est} Rennes / {dit?} Villeparisis) and still
  nothing reads. Top glyphs still unmapped: Rennes p(11x), o(7x), E(6x),
  f(6x); Villeparisis g(9x), a(7x), o(7x), E(6x). Both archival hypotheses
  now negative at 38-47% coverage with word-level mappings included —
  stronger than the alphabet-only negatives.

## Findings
- Nomenclator transcription conflicts (2026-10-07, all marked uncertain, never
  applied): (i) Rennes pink row 1 'com' and pink row 2 'ont' sit under the
  IDENTICAL circled-delta glyph — both pairings cannot hold, so at least one
  column of Tomokiyo's reconstruction is misaligned or the table reuses the
  glyph; (ii) Rennes pink row 1 'ent' sits under a circled-G identical in
  shape to alphabet row-1 cipher 'G' -> plain 't' (certain) — the same glyph
  cannot be both a word code and a letter; (iii) Villeparisis pink row 2
  'que' sits under a plain 'x' identical to alphabet row-1 cipher 'x' ->
  plain 'n' (certain) — same conflict. These are genuine inconsistencies in
  Tomokiyo's reconstructed tables (or column misalignments), and they cap
  how much of the nomenclator can ever be trusted without the manuscript.
- Word-code for the cipher's #1 glyph (2026-10-07): the double-plus '#'
  (19x, 12.7% of the cipher) maps to the word {est} in the Rennes
  nomenclator (certain, crisp alignment) and to {dit?} in the Villeparisis
  nomenclator (certain). Applied in attempts 4/5; neither produces French.
  The '#' also appears (circled) in the Rennes alphabet homophone row as
  uncertain {q,r} — shape variant, noted, not a certain conflict.
- 'majeste' has NO cipher glyph in Tomokiyo's Villeparisis table (2026-10-07):
  the cell under pink row 2 'majeste' is empty, verified at 7x
  (/tmp/nom/villep_w2_right_7x.png). Recorded as status null in
  data/archival-key-fr16039.json — a reconstruction gap, not missing data.
- CONFLICT between key sources (2026-10-07): Tomokiyo's reconstructed Rennes
  (Colbert 390) key maps cipher glyph 'h' -> plain 'b' (row 1, column b,
  certain by the 22-glyph/22-header count), while the lane's Lasry-interlinear
  extraction maps cipher 'h' -> plain 'E' (certain, 2 visual observations).
  Both cannot describe the same cipher. This independently weakens the
  Rennes-key hypothesis for the Catherine cipher beyond the failed apply.
- DECODE record 2788 (2026-10-07): the DECODE database holds this exact cipher
  as "Catherine_de_Medicis_to_Philibert_du_Croc" (27 Apr 1567, Saint-Maur),
  Status: Non-decrypted, Access: Public
  (https://de-crypt.org/decrypt-web/RecordsView/2788). Cross-reference only;
  no key material there. Thumbnail archived as data/decode-r2788-thumb.png.
- ARK ark:/12148/bpt6k932364m (Destray 1924), evidence: cryptiana unsolved.htm
  line 254 href. Scan offset verified by reading pages: f57=printed p.53,
  f58=p.54, f60=p.56, f61=unnumbered cipher plate, f62=blank.
- The cipher passage is on the photo plate (f61), NOT on printed p.53: 5 full
  manuscript lines + 1 short 8-token row + 1 inline single-glyph nomenclator
  token after "du srs". The printed edition's "[suivent cinq lignes en
  chiffres]" undercounts by the short row.
- Cipher stats (code/anneal.py --stats): 150 tokens, 40 distinct symbols; top
  frequencies #=19, p=11, g=9, z=9, a=7, o=7, x=7, E=6, B=6, f=6.
- UNICITY MATH: work-order rule of thumb needs ~28 x alphabet-size chars =
  28 x 40 = 1120 tokens; have 150 (13%). Even the Shannon simple-substitution
  unicity distance (~30 chars for 26 symbols) is out of reach for a
  40-symbol homophonic/nomenclator system at this length. Verdict:
  blocked-on-key for blind methods.
- LEAD (not yet pursued): Lasry's solved Charles IX->du Croc cipher (Destray
  p.80, same book/period/correspondent) may share the nomenclator table;
  interlinear solution images at cryptiana.web.fc2.com/code/GL/
  (GL_CharlesIX_decipher.png etc., saved to
  data/lasry-charlesIX-decipher-recto.png and -verso.png 2026-10-07). Next work
  order: extract that key table and try it as a keyed attack on this cipher.
- PARTIAL key table extracted 2026-10-07 (data/charlesIX-key-table.json):
  7 certain mappings {#->I, 6->A, 7->R, +->O, h->E, B->D, Y->S} from direct
  visual column-alignment (evidence per mapping in JSON; workbook in
  data/interlinear-workbook.md). Pairing direction red-above<->black-below
  proven by "≠1"->"QUE" nomenclator anchor (verso row 0). Applied via
  code/apply_key.py -> data/keyed-attempt1.txt (24.7% coverage); no French
  emerges — INCONCLUSIVE (see Null results), not a disproof. Conflicts
  (x->{N,E,M}, alpha->{O,D}) marked uncertain, never silently guessed.

## Data inventory
- data/destray1924-p53_f57.jpg — printed p.53 (letter XXI transcription).
  Source: https://gallica.bnf.fr/iiif/ark:/12148/bpt6k932364m/f57/full/full/0/native.jpg
  Retrieved 2026-10-07 ~04:22 UTC via curl (Mozilla UA). sha256:
  0bf5594de01464ecafba5b48bee9c985b68c865aa2690827f82cb1b1670f0b2d
- data/destray1924-plate_f61.jpg — photo plate of original dispatch (cipher).
  Source: https://gallica.bnf.fr/iiif/ark:/12148/bpt6k932364m/f61/full/full/0/native.jpg
  Retrieved 2026-10-07 ~04:26 UTC via curl. sha256:
  270d766967f18337c14543614b2d02824d4f0e844ec54c24332b5931257177df
- data/medici-1567-cipher.txt — verbatim + normalized cipher transcription
  (150 tokens / 40 glyphs), transcribed 2026-10-07 from the plate image above.
- data/medici-1567-clear.txt — cleartext transcription of printed p.53 letter
  XXI + manuscript variants, transcribed 2026-10-07.
- data/gutenberg-17489-miserables1.txt — French quadgram corpus (Hugo, Les
  Misérables T.I). Source: https://www.gutenberg.org/cache/epub/17489/pg17489.txt
  (via https://www.gutenberg.org/ebooks/17489.txt.utf-8 redirect). Retrieved
  2026-10-07 ~04:34 UTC via curl -L. 710496 bytes. sha256:
  a5de514ba7b9f2e1790e7e259c4e8b7a35ae1d29e4bf9a5f8767039c58b80503
- data/french-quadgrams.json — quadgram log-prob model built 2026-10-07 by
  code/anneal.py --build-model from the corpus above (28293 distinct quads).
- data/anneal-run1-20261007.log — full output of the 25x40000 annealing run
  (best score -527.70, degenerate; null result).
- data/lasry-charlesIX-decipher-recto.png / -verso.png — George Lasry's 2022
  interlinear solution of the Charles IX -> du Croc cipher (Destray p.80),
  key-table source for the planned keyed attack. Source:
  https://cryptiana.web.fc2.com/code/GL/GL_CharlesIX_decipher.png and
  .../GL_CharlesIX_decipher2.png (via https://cryptiana.web.fc2.com/code/GL.htm).
  Retrieved 2026-10-07 ~04:38 UTC via curl. sha256:
  747ae99d528ebc22911effc86d09faa93c50eabeded1fd4132acef2d837cbeb1 (recto)
  aa2f544523aa330a8ab96a2d99ee8c00ad4840459082672a9ee0d7a8bf8ba8e3 (verso)
- data/charlesIX-key-table.json — PARTIAL key table derived 2026-10-07 from
  the interlinear images above: 7 certain mappings {#->I, 6->A, 7->R, +->O,
  h->E, B->D, Y->S} with per-mapping visual-alignment evidence; conflicts
  (x->{N,E,M}, alpha->{O,D}, 9c->D vs 9->null) recorded under "uncertain",
  never guessed. Includes "source" and "notes" fields. NOTE: no explicit key
  table exists in Lasry's images; this was derived by column alignment
  (pairing red-above<->black-below proven by "≠1"->"QUE" anchor).
- data/interlinear-workbook.md — row-by-row transcription workbook for the key
  extraction (verso row 0 fully paired, 19 high-confidence pairs; method,
  anchors, and uncertainty flags documented).
- data/keyed-attempt1.txt — output of code/apply_key.py (2026-10-07): the 7
  certain mappings applied to data/medici-1567-cipher.txt; 37/150 tokens
  (24.7%) decoded, remainder bracketed. No French emerges; assessed
  INCONCLUSIVE (see Null results).
- data/cryptiana-key-images/CharlesIX_Rennes.png — Tomokiyo's reconstructed
  key table for the Bishop of Rennes cipher (1561-1564), BnF Colbert 390.
  Source: https://cryptiana.web.fc2.com/code/CharlesIX_Rennes.png (via
  cryptiana.web.fc2.com/code/henryiii.htm). Retrieved 2026-10-07 via curl
  (Mozilla UA). 119320 bytes. sha256:
  4b23764c797fd7d47135b31b37d119ba0d972e44dda4747a7c3ce10879c6d841
- data/cryptiana-key-images/CharlesIX_Rennes2.png — reconstructed key for the
  Bishop of Rennes <-> Cardinal de Lorraine cipher (1563), BnF Colbert 392.
  Source: https://cryptiana.web.fc2.com/code/CharlesIX_Rennes2.png.
  Retrieved 2026-10-07 via curl. 45146 bytes. sha256:
  a5cce4e417a4919c47e140ed6dff439792b9359ee07c137e7c205d1e8b621df8
  (fetched for context; not transcribed — different correspondence)
- data/cryptiana-key-images/CharlesIX_Villeparisis.png — Tomokiyo's
  reconstructed key table for the Villeparisis cipher (1564), BnF fr.16039
  (letters Rome -> Charles IX and Catherine de Medici). Source:
  https://cryptiana.web.fc2.com/code/CharlesIX_Villeparisis.png. Retrieved
  2026-10-07 via curl. 69037 bytes. sha256:
  27cf1314c8acc1fe27baad407dca312bdd3326e6ad507ef3e14eab7dcaf2437e
- data/cryptiana-key-images/CharlesIX_Mans.png — reconstructed key for the
  Bishop of Mans cipher (1569), BnF fr.16039. Source:
  https://cryptiana.web.fc2.com/code/CharlesIX_Mans.png. Retrieved 2026-10-07
  via curl. 81238 bytes. sha256:
  c3bef8e913ea6ac37c503d816dcace0208029a6e88da9dc8f3afc64fc10355ed
  (fetched for context; not transcribed — different cipher/correspondence)
- data/cryptiana-key-images/CharlesIX_Catherine.png — the Catherine->du Croc
  27 Apr 1567 cipher manuscript photo as reproduced in Tomokiyo's article
  (NOT a key table). Source:
  https://cryptiana.web.fc2.com/code/CharlesIX_Catherine.png. Retrieved
  2026-10-07 via curl. 251619 bytes. sha256:
  de13b6af0d0c259d41849d4670885a98af16fbf962e2fa19651c043bc055b01d
- data/cryptiana-key-images/CharlesIX_duCroc.png — Tomokiyo's reproduction of
  the La Forest-du Croc cipher (1567) key table (Destray 1924, leaf next to
  p.32). Source: https://cryptiana.web.fc2.com/code/CharlesIX_duCroc.png.
  Retrieved 2026-10-07 via curl. 376419 bytes. sha256:
  d0840cbb0f9401e50c1e11b32e3de243bfb9a1e3b24c4805ac8162298068ae76
  (transcription not attempted: alphabet-grid row orientation not reliably
  establishable at this resolution; different correspondence anyway)
- data/archival-key-colbert390.json — transcription (2026-10-07) of the
  Rennes/Colbert 390 alphabet row 1 from CharlesIX_Rennes.png: 18 certain
  single-plain mappings, 2 certain-ambiguous homophone pairs, homophone rows
  + nulls as uncertain. Format matches data/charlesIX-key-table.json.
  sha256: 62266d44f938c686a99a55363d15f196c9a25b398382902c7cd124a3d4472acf
- data/archival-key-fr16039.json — transcription (2026-10-07) of the
  Villeparisis/fr.16039 alphabet row 1 from CharlesIX_Villeparisis.png: 13
  certain single-plain mappings, 1 certain-ambiguous. sha256:
  b0fdca127954e3bcda669a929bcb739c9f2d9368fa8977cc7a2f9606304f50c4
- data/keyed-attempt2-rennes.txt — output of code/apply_archival_key.py
  (2026-10-07): 18 certain Rennes row-1 mappings applied to the cipher;
  43/150 tokens (28.7%) decoded. No French; NEGATIVE on Rennes-key
  hypothesis (see Null results). sha256:
  c785313f144f67a7e00f114aa41c7a3bc632388840a8eccee4edaf05d80eb236
- data/keyed-attempt3-villeparisis.txt — output of code/apply_archival_key.py
  (2026-10-07): 13 certain Villeparisis row-1 mappings applied; 38/150
  tokens (25.3%) decoded. No French; NEGATIVE on Villeparisis-key hypothesis.
  sha256: e29c798172946e70b27bd87a18dc22b19048784665a37c5b28feb31b72469eff
- code/apply_nomenclator.py — NEW applier (2026-10-07, 6824 bytes): applies
  alphabet certain single-plain mappings PLUS certain nomenclature entries
  (pass 1: bigram {word} on raw stream with nomenclator precedence; pass 2:
  alphabet; pass 3: singleton {word}); uncertain/ambiguous/null never
  applied. Written new (not an extension) so apply_archival_key.py and
  attempts 2/3 stay reproducible. sha256:
  995648066e15070bbd34ddb4e043a9b5ae607dfe94e2faa901d494cc68706159
- data/keyed-attempt4-rennes-full.txt — output of code/apply_nomenclator.py
  on data/archival-key-colbert390.json (2026-10-07): 70/150 tokens (46.7%)
  decoded (alphabet + {est}x19/{mais}x3/{vous}x3/{votre?}x1 + 1 {par} bigram).
  No French; STRENGTHENED NEGATIVE on Rennes-key hypothesis. 2259 bytes.
  sha256: 97f9815946a173a275e70b7724d0e226d52a242dcc0004bca82f9ad208cd6576
- data/keyed-attempt5-villeparisis-full.txt — output of
  code/apply_nomenclator.py on data/archival-key-fr16039.json (2026-10-07):
  57/150 tokens (38.0%) decoded (alphabet + {dit?}x19; no bigram hits). No
  French; STRENGTHENED NEGATIVE on Villeparisis-key hypothesis. 2213 bytes.
  sha256: 5ad3a0b532ab167b535843063de0da49bc1430540d391665ab9afb7c3a2018f4
- data/archival-key-colbert390.json — EXTENDED 2026-10-07 with "nomenclature"
  (26 entries: 20 certain / 6 uncertain) + "nomenclature_notes"; alphabet
  mappings untouched. New sha256:
  54212a939754b63c28a3cd2b03f3b5538a95fb03c4bdec4d2d8b549f3aa0fabf
- data/archival-key-fr16039.json — EXTENDED 2026-10-07 with "nomenclature"
  (21 entries: 17 certain / 3 uncertain / 1 null) + "nomenclature_notes";
  alphabet mappings untouched. New sha256:
  90a4dabc144cb901a6ae2f51d2265f4ac3bba5e1cb8927d3a19e5ae608c757ea
- data/decode-r2788-thumb.png — DECODE database record 2788 thumbnail of this
  cipher ("Catherine_de_Medicis_to_Philibert_du_Croc", 27 Apr 1567,
  Saint-Maur, Non-decrypted, Public). Source:
  https://de-crypt.org/decrypt-custom/filesrv/?file=TH_IMG_R2788_I17353_P.png
  Retrieved 2026-10-07 via curl. 200x313 PNG, 60528 bytes. sha256:
  13af31458fbac0efe37632675957dc19df5e609e35bf9c0112bd3b7f6d6ba79a

## Methodology log (continued)
- 2026-10-07: GALLICA MANUSCRIPT CHECK (work order). ARKs recovered from
  Tomokiyo's own Gallica hrefs (henryiii.htm re-fetched 2026-10-07 ~05:25 UTC
  via curl, Shift_JIS decoded with iconv, /tmp/henryiii_utf8.html 103541
  bytes; all gallica hrefs extracted with 350-char context): Colbert 390 =
  ark:/12148/btv1b10033942k (href on "BnF Colbert 390 (Gallica) contains many
  letters partially in cipher addressed to Bernardin Bochetel, Bishop of
  Rennes"); fr.16039 = ark:/12148/btv1b9060947g (href on "BnF fr.16039
  (Gallica) contains cipher letters from Rome to Charles IX and Queen Mother,
  Catherine de Medici"). This is the same recovery route as the Destray ARK
  (cryptiana cross-reference), and the stronger route — the permitted
  Gallica SRU curl retry (1 attempt budget) was NOT used.
- 2026-10-07: IIIF fetch to data/gallica-manuscripts/ (provenance: URL, UTC
  time, sha256 in PROVENANCE.txt; manifests: Colbert 390 = 184 canvases,
  fr.16039 = 535 canvases). Volume identity VERIFIED by reading f1 images:
  colbert390_f1.jpg shows binding label "COLB. 390 V" (sha256
  c903f343c71927875f7d88f86f072747a210deb8fd5307850b406ff2157ab025);
  fr16039_f1.jpg shows label "16039" + "Lettres de Rome (Cleutin)" note
  (sha256 2c3cabae54a35b896e9149b56e678fedfd637b91ed3d44abc624de680d9d9dda).
  Key specimen pages fetched at 1400px and read: Colbert 390 scans f70-f74
  (f70 = manuscript p.139, Tomokiyo's "undeciphered note on p.139 (p.72 of
  pdf)": a ciphertext slip + the "Deschiffrez vous mesmes" note below,
  verified on full-res 6320x4736 colbert390_f70_full.jpg, sha256
  1797fe67eec8e9040451b87aef9bc62905e7c5b9dd238d367eb19ccb35140679);
  fr.16039 scans f17-f21 (f18 right page numbered "17": "Le sr de Villeparis
  a la Reine / Rome / Dernier may 1564" with INLINE cipher glyphs; f19 left =
  cipher copy struck through; f21 signed "Villeparisis ... dernier jour de
  may 1564" — Tomokiyo's f.17 key specimen letter, confirmed).
- 2026-10-07: Adjudication verdict. NEITHER volume shows a standalone cipher
  KEY TABLE on the examined pages: Colbert 390 p.139 is a ciphertext slip
  (delta/G/x-family glyphs visible, no word pairings); fr.16039 f.17 is a
  letter with inline cipher (7, #, x, =, :, ~, chi-x visible, no key).
  Tomokiyo's tables are reconstructions FROM these letters, so the three
  conflicts + empty cell were re-checked against his key-table images at
  2x-5x zoom (magenta bands located programmatically) plus the manuscript
  glyph repertoire:
  (1) circled-delta com/ont: Tomokiyo's table genuinely places the SAME
  circled-delta (delta in oval) under THREE words — 'com' and 'dit' (pink
  row 1) and 'ont' (pink row 2). The prior 'dit' transcription
  ("integral-circled (long-s)", certain) was WRONG at re-read (5x crop
  /tmp/dit_et_5x.png) and is SUPERSEDED (old value kept in the JSON's
  prior_transcription_superseded). No manuscript key page exists to assign
  the glyph to a word -> all three stay uncertain. Genuine reconstruction
  inconsistency, not a lane transcription artifact.
  (2) circled-G 'ent' vs alphabet G->t: verified identical hand-drawn
  circled-G in both cells (5x crop); the nulls table row 'rix' ALSO lists
  circled-G among candidates -> three-way collision inside the
  reconstruction. No key page -> stays uncertain.
  (3) Villeparisis plain x 'que' vs alphabet x->n: verified visually
  identical chi-like x in both cells (2x bands /tmp/v_a1.png, /tmp/v_r2.png);
  manuscript f.17 shows x-like glyphs in the inline cipher but no key page
  -> stays uncertain.
  (4) 'majeste' empty cell: verified EMPTY in Tomokiyo's own image
  (/tmp/v_r2.png); no manuscript key table to fill it -> stays null
  (reconstruction gap).
  JSON changes: data/archival-key-colbert390.json (sha256 now
  b4467c3817ed0321aba452ce9c14145ecb09df852230a0c8f22613fa1cbc121a)
  and data/archival-key-fr16039.json (sha256 now
  2777ae4cd43a8dcfbf09b1c251844ac2edc3b5b34d974c9729e2e4286a79d97a)
  gained "manuscript_adjudication_2026-10-07" objects with dated evidence;
  'dit' demoted certain->uncertain with the old value preserved (supersede,
  never delete); dated notes appended to com/ont/ent/que/majeste entries.
- 2026-10-07: Post-correction re-apply. code/apply_nomenclator.py re-run on
  both updated JSONs. Rennes -> data/keyed-attempt4b-rennes-full.txt
  (2212 bytes, sha256
  d65d5316708d4a111776a42b93f75abcecdcb62895d2530470afe9415b27ffe8):
  70/150 tokens (46.7%) decoded — decode body BYTE-IDENTICAL to attempt4
  (only header stats lines changed: 'dit' moved from
  certain-but-inapplicable to non-certain). No French emerges. Villeparisis
  re-run byte-identical to attempt5 (sha256
  5ad3a0b532ab167b535843063de0da49bc1430540d391665ab9afb7c3a2018f4):
  57/150 (38.0%), no French. The mapping demotion changes nothing applied;
  both archival negatives STAND.

## Null results (continued)
- Manuscript key pages: NOT FOUND (2026-10-07). 13 Gallica IIIF pages read
  across both ARKs (data/gallica-manuscripts/, PROVENANCE.txt): Colbert 390
  p.139 is ciphertext, fr.16039 f.17 is a letter with inline cipher — no
  standalone key tables in either volume on the examined pages. The three
  Tomokiyo conflicts and the empty 'majeste' cell therefore cannot be
  adjudicated from a manuscript key page; they are internal to his
  reconstructions and remain uncertain/null.

## Findings (continued)
- Tomokiyo's Rennes table reuses the circled-delta glyph under THREE words
  ('com', 'dit', 'ont') and the circled-G under THREE cells (alphabet 't',
  nomenclator 'ent', nulls 'rix') — verified at 5x in his own key image
  (2026-10-07 manuscript check). Either the cipher genuinely reuses glyphs
  across alphabet/nomenclator/nulls, or his column alignment slipped in
  multiple places. The Villeparisis plain-x duplication ('que' vs alphabet
  'n') is likewise genuine in his table.
- 'dit' transcription corrected (2026-10-07): was "integral-circled
  (long-s)" certain, is circled-delta uncertain — old value preserved in
  the JSON under prior_transcription_superseded. Re-apply confirms zero
  change to decoded output (attempt4b body byte-identical to attempt4).

## Data inventory (continued)
- data/gallica-manuscripts/ — 13 Gallica IIIF pages + 2 manifests +
  PROVENANCE.txt (URLs, UTC times, sha256). colbert390_f1.jpg (volume
  identity), colbert390_f70.jpg + colbert390_f70_full.jpg (6320x4736, the
  p.139 cipher slip), colbert390_f71-f74.jpg; fr16039_f1.jpg (volume
  identity), fr16039_f17-f21.jpg (the 1564 Villeparisis letter, f.17);
  btv1b10033942k.manifest.json (184 canvases), btv1b9060947g.manifest.json
  (535 canvases).
- data/keyed-attempt4b-rennes-full.txt — re-run of code/apply_nomenclator.py
  on the post-correction data/archival-key-colbert390.json (2026-10-07):
  70/150 (46.7%), decode body byte-identical to attempt4. 2212 bytes.
  sha256: d65d5316708d4a111776a42b93f75abcecdcb62895d2530470afe9415b27ffe8
