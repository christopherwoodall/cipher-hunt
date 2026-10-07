# Lexicon self-test — 2026-10-07

## 7 ground-truth crib syllables (11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que)
- `la`: present as a lexicon syllable in 97 word-entries (e.g. législature, population, législation; token itself: yes) — PASS
- `pre`: present as a lexicon syllable in 31 word-entries (e.g. premier, première, premiers; token itself: no) — PASS
- `m`: present as a lexicon syllable in 1 word-entries (e.g. —; token itself: yes) — PASS
- `i`: present as a lexicon syllable in 205 word-entries (e.g. existence, idée, existe; token itself: yes) — PASS
- `er`: present as a lexicon syllable in 58 word-entries (e.g. exerce, exercice, exercer; token itself: yes) — PASS
- `e`: present as a lexicon syllable in 223 word-entries (e.g. une, commune, aucune; token itself: yes) — PASS
- `que`: present as a lexicon syllable in 125 word-entries (e.g. amérique, chaque, politique; token itself: yes) — PASS

## `première` (lane spec: 4 syllables)
- entry: `première` → `pre`-`mi`-`è`-`re` (4 syllables), orth pattern `ABCD`, phon pattern `pr`-`mi`-`e`-`r`/`ABCD`, freq 105 — PASS

## 20-word random spot check (seed 20261007, hand-verified vs corpus text)
- `formule` → `for-mu-le` [ok] — PASS
- `gage` → `ga-ge` [ok] — PASS
- `devenu` → `de-ve-nu` [ok] — PASS
- `porterait` → `por-te-rait` [ok] — PASS
- `océans` → `o-cé-ans` [ok] — PASS
- `peuplade` → `peu-pla-de` [ok] — PASS
- `unirait` → `u-ni-rait` [ok] — PASS
- `incertitudes` → `in-cer-ti-tu-des` [ok] — PASS
- `budgets` → `bud-gets` [ok] — PASS
- `infamante` → `in-fa-man-te` [ok] — PASS
- `england` → `en-gland` [ok — English loanword] — PASS
- `dons` → `dons` [ok] — PASS
- `humanity` → `u-ma-nity` [ok — English word in text] — PASS
- `concourir` → `con-cou-rir` [ok] — PASS
- `douter` → `dou-ter` [ok] — PASS
- `confondaient` → `con-fon-daient` [ok — `aient`=/ɛ/ 1 syllable, verified by hand] — PASS
- `été` → `é-té` [ok] — PASS
- `productive` → `pro-duc-ti-ve` [ok] — PASS
- `condamnation` → `con-dam-na-ti-on` [ok] — PASS
- `étendirent` → `é-ten-di-rent` [ok] — PASS
