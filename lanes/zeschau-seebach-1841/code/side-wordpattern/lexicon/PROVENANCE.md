# Lexicon provenance — Seebach word-pattern side fleet

Built 2026-10-07 by the lexicographer worker (coordinator session
2418001f-a4e3-41a0-8c1f-954166f266f7).

## Source corpus (era + register matched to the 1841 cipher)
- `data/gutenberg-30513-tocqueville-t1.txt` — "De la Démocratie en Amérique,
  tome premier" (1835), formal political prose.
  sha256 `fafebe4f69bc8e7abc6ed95bd10c2257bd26a307b2c1071056187ef76154aeaa`
- `data/gutenberg-30514-tocqueville-t2.txt` — tome deuxième (1840), same register.
  sha256 `20e46d72bc398f1c903449908a35a691e0d32763234bc75b2376cd21dbe33ee9`
  (both from `data/SHA256SUMS.txt`; retrieval notes in
  `data/PROVENANCE-tocqueville.txt`)
- Gutenberg boilerplate stripped (between `*** START/END OF THE PROJECT
  GUTENBERG EBOOK` markers). Tokens: `[A-Za-zÀ-ÿŒœÆæ]+`, lowercased,
  elisions split on `'` (`l'homme` → `l`, `homme`).
- 214,861 tokens → **11,870 distinct words**.

## Syllabifier choice
Custom rule-based **orthographic** French syllabifier
(`build_lexicon.py`: `unitize` + `syllabify`). Rejected the lane's
`data/upstream-syll*.py` (those are syllabic annealers over a fixed unit
inventory, not word syllabifiers) and rejected pyphen/fr hyphenation
(hyphenation glues final mute-e: `première` → `pre-mière`, `parce` unsplit —
wrong for a syllabary, whose upstream unit inventory includes `re`, `ere`,
`ment`, `tion` as cut units).

Core rules (documented in code):
- Maximal onset; single intervocalic consonant → next syllable; CC split
  except liquid/onset clusters (bl br cl cr dr fl fr gl gr pl pr tr vr st sp
  sc, gn, ch, ph, th); doubles always split (`per-sonne`, `ter-re`);
  `x` always coda (`ex-a-men`).
- Mute final `-e`/`-es` after a consonant gets its own syllable with a
  maximal onset steal (`ta-ble`, `pre-miè-re`, `en-tre`, `mar-bre`);
  `-e` after a vowel is silent (`vie`, `rue`); `-ée` is pronounced
  (`an-née`); `que`/`le`/`de` stay one syllable.
- Nasal vowels only before a consonant (`en-fant` nasal, `en-ne-mi` oral);
  `-ent` 3pl kept as its own syllable (`par-lent`, orthographic — by ear 1);
  interior schwa kept (`pe-tit`, `re-ve-nir`).
- `-ier` (masc) = 1 nucleus (`pre-mier`); `-ière` split `iè|re`
  (`pre-mi-è-re`, lane spec); `-ier` verbs collapsed (`ou-blier` — by-ear
  `ou-bli-er` is a documented matcher-side variant); final `-ille`/`-aille`/
  `-eille`/`-ouille` = 1 nucleus (`fille`, `bou-teille`); `y` between vowels
  is consonantal (`pa-yer`) but vocalic before consonant/end (`pa-ys`).
- Diérèse `i|è` applied uniformly (`pre-mi-è-re`, `deux-i-è-me`).

## By-ear (phonetic) normalization classes
Applied per syllable (`phon_syllable`), order-sensitive:
1. accent strip (é/è/ê/ë→e, à/â→a, î/ï→i, ô→o, ù/û→u, ç→c, æ→a, œ→o)
2. `qu`→k, `eue`→eu
3. final mute `-e` dropped when preceded by a consonant (`re`→`r`, `ble`→`bl`)
4. `eau`/`au`→o, `ai`/`ei`→e, `ou`→u, `oi`→wa, `ch`→sh, `ph`→f, `th`→t, `gn`→ny
5. `c`→s before e/i/y else →k; `g`→j before e/i/y
6. nasal merge: `en`→`an`, `ain`/`ein`→`in`
7. double-consonant collapse (`personne` ≡ `persone` — the Frenchman's
   "two spellings in one cipher" case)

## Outputs
- `lexicon.jsonl` — one JSON object per distinct word, sorted by
  (-freq, word): `w`, `syl` (orthographic syllables), `pat` (orthographic
  repetition pattern, first-occurrence A–Z then a–z), `phon` (normalized
  syllables), `ppat` (phonetic pattern), `freq`, `nsyl`.
- `index.json` — `orth`: `(nsyll|pattern)` → words sorted by (-freq, word);
  `phon`: same over phonetic patterns; plus `stats`.
- Rebuild: `python3 build_lexicon.py` (stdlib only, ~2 s).

## Stats
- entries 11,870; orth keys 31, phon keys 35.
- Orth key sizes: mean 382.9, max 4,651 (`2|AB`), 10 singletons.
  Keys carrying repetition (the discriminating ones for the matcher): 21,
  e.g. `3|ABA` (8 words: ohio, demande, lesquelles, retire, décidé, respire,
  …), `4|ABAC` (6), `5|ABCAD` (5), `2|AA` (2: chercher, ii).
- Phon key sizes: mean 329.7, max 4,636, 8 singletons.
