## lexicographer: pattern lexicon built
- Context: the side fleet needs a French word→repetition-pattern lexicon so the
  Pattern Matcher can look up cipher words by their group-repetition shape
  (e.g. cipher 12-45-12 → ABA). Built from the era+register corpus per the
  Frenchman's methodological steer (1841 diplomatic French, not 1862 novel French).
- Decision: custom rule-based orthographic syllabifier + dual orthographic /
  phonetic-normalized patterns per word, indexed by (n_syllables, pattern).
  Rejected pyphen hyphenation (glues mute-e: `pre-mière`, `parce` unsplit —
  wrong for a syllabary whose unit inventory cuts `re`/`ere`/`ment`/`tion`)
  and rejected `data/upstream-syll*.py` (annealers, not syllabifiers).
- Why: the encipherer spells by ear and cuts inconsistently (Frenchman:
  `personne` in two spellings in one cipher), so each entry carries BOTH the
  canonical orthographic cut and a by-ear normalized cut (e/é/è/ê→e,
  s/ss/c/ç→s, au/o/eau→o, ai/ei→e, double-collapse, final mute-e drop).
  Canonical cut is deterministic; variant tolerance is the matcher's job.
- Enlightenment: the brief said "première → 4 syllables (pre-miè-re)" — the
  parenthetical shows only 3 dash-parts, but the "4" is the correct reading:
  uniform diérèse `i|è` gives `pre-mi-è-re` (4), matching `deux-i-è-me`, and
  the segmenter's 4-group span @1034–1037 for `première` independently
  supports a 4-cut. So the parenthetical is a missing-dash typo, not a spec
  conflict — reported as a finding in SELFTEST.md, not hidden.
- For the report: Pattern-lexicon section. Numbers: 11,870 distinct words
  from 214,861 Tocqueville tokens; 31 orth keys / 36 phon keys; 21
  repetition-bearing orth keys (e.g. `3|ABA`: 8 words; `4|ABAC`: 6;
  `2|AA`: 2). Self-test: all 7 crib syllables (la, pre, m, i, er, e, que)
  present; `première` → pre-mi-è-re, pattern ABCD, freq 105. 59-word
  regression battery + 20-word random spot check (seed 20261007) all PASS.
  Files: `code/side-wordpattern/lexicon/` (lexicon.jsonl, index.json,
  PROVENANCE.md, SELFTEST.md, build_lexicon.py).
- Caveats: orthographic-canonical by design — by-ear variants the matcher
  must try itself: `-ent` kept as syllable (`par-lent`, by ear 1), `-ier`
  verbs collapsed (`ou-blier`, by ear `ou-bli-er`), interior schwa kept
  (`pe-tit`, by ear often `pti`), `pierre`→`pier-re` (by ear 1). Single-letter
  tokens (m, i, e) come from elisions (`m'`, `l'`). Two English words in the
  corpus (`england`, `humanity`) syllabified as-is.
