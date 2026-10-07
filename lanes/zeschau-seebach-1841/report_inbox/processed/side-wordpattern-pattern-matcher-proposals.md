## pattern-matcher: word-pattern matching run — HONEST NULL
- Context: I am the PATTERN MATCHER for the Seebach word-pattern side fleet.
  The instrument: segment the cipher pair stream into words (segmenter STRUCT
  boundary probs, `code/crowd3/segmenter_results.json`), compute each word's
  group-repetition pattern, look it up in the French pattern lexicon
  (`code/side-wordpattern/lexicon/`, 11,870 Tocqueville words, orth+phonetic
  indexes), filter by anchor consistency (tiers T0 GT-only → T3 all
  constraints), rank by era frequency. Tested: the 25 segmenter crib-drag
  targets + every word containing ≥1 anchored group, at cuts ≥0.5 and ≥0.7,
  against all 4 spec'd by-ear variants (-ent kept/dropped, -ier
  collapsed/split, interior schwa kept/dropped, pierre 1-vs-2 syllables).
  Anchor statuses: GT 11=la 70=pre 82=m 34=i 29=er 40=e 46=que;
  PROV-STRONG 87=ce 64=qui 96=par 94=ne; PROV 67=veut (06=verb-stem class,
  unusable as syllable anchor); LEAD 62=on 78=me 52=pas 24=en.
- Decision: **NULL — promote nothing.** The promotion rule's "unique survivor"
  clause fires 11× (cut 0.5) / 15× (cut 0.7), but every hit fails the lane's
  ≥2-independent-checks bar, and the instrument fails its ground-truth control
  (below). All would-be hits are demoted to graded leads; every one is
  stamped PROVISIONAL-PENDING-POLYVALENCE-VERDICT (tester verdict pending).
- Why: (1) **Ground-truth control fails.** The known word "première" tail
  @1035–1038 = 82-34-29-40 (m|i|er|e, FOUR GT anchors) returns ZERO
  candidates at every tier — the encipherer's by-ear units (m, i as standalone
  syllables) are not in the lexicon's syllable inventory ('m' occurs as a
  syllable in exactly 1 of 11,870 entries; SELFTEST). An instrument that
  cannot recover a 4-anchor known word cannot be trusted on 0–1-anchor
  unknowns. (2) **The "unique survivors" are noise.** 7× "quiconque" is a pure
  echo of provisional 64=qui (0 GT anchors; seven different cipher words all
  "propose" the same word); the rest are hapax accidents at freq 1–5
  ("morcela", "susquehanna" — Tocqueville-register pollution in a Saxon
  despatch — "laborieusement", "outrepassé", "envahi" ×3, "apercevrions",
  "prévienne", "ancêtres", "perfectionnement", "nécessairement" f17 max);
  ZERO have ≥2 GT anchors. (3) **Unstable under segmentation:** only 4/11
  survive the 0.5→0.7 cut (@144 quiconque, @200 morcela, @239 laborieusement,
  @664 pionnier) — segmentation artifacts, not words. (4) The 25 crib-drag
  targets: 0 proposals, 24 leads, 1 null — the "leads" are pure frequency
  priors (2|AB→une/états/même; 3|ABC→encore/union/amérique;
  4|ABCD→gouvernement/amérique/américains), carrying no anchor information.
- Enlightenment: the mechanics are sound — a synthetic [87,11] word returns
  "cela" as the UNIQUE survivor in both alphabets (freq 47) — so the failure
  is the unit inventory, not the lookup. The cipher's syllabary writes units
  the lexicon never emits (m, i letters; "ère"→er|e in "première"), exactly
  the Frenchman's "spells by ear, cuts inconsistently" finding. The fix is not
  more variants but the syllabary's own unit inventory (round-4 WO5:
  `data/upstream-syll*.py`) — pattern-matching against French syllables is
  the wrong alphabet for this cipher. Also: the segmenter glues a following
  group onto "cela" (87-11-00-33 @1241, 87-11-00-11 @1402 → NULL at all
  tiers); and @507 (77-62-94, anchors on+ne) → NULL, i.e. no French ?-on-ne
  word fits the 77 slot — a small datum for the 77 investigation.
- For the report: Pattern-matcher section. Numbers that matter:
  byte-checks all reproduce — 1,846 pairs / 96 groups / 3,764 digits,
  odd_lines=28, off1=32, digits.txt byte-identical to ct_R5005.txt digits,
  la|première span @1033–1038 = 11-70-82-34-29-40, boundary bc[1033]=0.9365
  (matches `code/crowd3/segmenter_results.json` checkpoint);
  segmentation 926 words @0.5 / 555 @0.7 (vs segmenter Viterbi MAP 958 —
  per-boundary threshold vs joint decoding, expected);
  367 words (0.5) / 301 (0.7) contain ≥1 anchored group;
  proposals 11→15 across cuts, overlap 4; leads 110/69; nulls 122/168;
  ground-truth control: première-tail NULL at 4 GT anchors;
  'm'-as-syllable in 1/11,870 lexicon entries.
  Files: `code/side-wordpattern/matcher/matcher.py`,
  `code/side-wordpattern/matcher/match_results.json`,
  `code/side-wordpattern/matcher/README.md`.
- Caveats: I could NOT verify the Polyvalence Tester's verdict — no output
  from it exists yet in `code/side-wordpattern/report_inbox/`; every
  would-be proposal is stamped PROVISIONAL-PENDING-POLYVALENCE-VERDICT (5/11
  at cut 0.5 touch polyvalent groups 06/94/52). Phase rhythm (chi²≈188) was
  NOT used as a filter — the tuner NULL'd phases as word-position classes
  (N15), so applying it would be unprincipled. The -ier-split variant
  over-generates on nouns ("pionnier" via V-orth-iersplit on 03-62-06-00);
  flagged in the JSON per hit. Single-group anchored words (124 @0.5) are
  anchor restatements, not evidence, and were excluded from promotion.
