### Round-17 null/kill batch, backlog fold 4 (crowd17, 2026-10-09 UTC —
4 notes: 2 kills, 2 nulls; battery grade)

- **N377** — letter-41-dist2-tri NULL: keep 41 outside the letter tier (the
  fence fires; evidentiary, not terminal). n(41)=19; three windows, three
  fails, all byte-verified against `data/upstream-ct_R5005.txt` +
  `code/side-keyhunt/repaired_offsets.json`. W1 @59 (row a1_01, "41 08 i
  er"): best reading "prière" (41=p, 08=r) is the unique common word only
  in the @59–63 segmentation, which is not forced — the @59–62
  segmentation yields 6 rivals (acier/osier/trier/crier/prier/scier) and
  assigns 41 a different value; no boundary evidence at @58|59, @62|63, or
  @63|64. Not kill-grade. W2 @1048 (row a6_04, "41 88 29=er"): fenced —
  88 is verb-stem (A3 frame), class-incompatible with a letter reading;
  6+8 rivals even hypothetically (frère/bière/fière/opère/avère/acère;
  fier/hier/lier/amer/suer/tuer/muer/nuer). W3 @235–237 (row a2_01,
  "70 98 41"): fenced by standing battery promote vient-98-name
  (2026-10-08, explicitly covering @236) — the window reads "prévient
  [41]" with 41 word-external; 5 rivals even hypothetically
  (prend/preux/prêts/préau/prêta). Three follow-ups proposed for the
  supervisor: letter-41-08-rerun (P3 — re-test W1 once 08's letter value
  banks; "prière" needs 08=r), letter-41-88-classcheck (P3),
  wordbound-41-59-seg (P3 — boundary evidence to force the segmentation).
  Discovered tension recorded: the parent census (battery-wordinternal-41-
  census NULL follow-up 2) listed the @237 lead without flagging the
  standing 98='vient' promote — adopted per lane convention, not
  re-litigated.

- **N378** — syll-39-de-host KILL: the @1334 '-de'-final-verb leg is dead at
  kill grade. Locus bytes @1327–1337 (row a7_04/a7_05): "… ne pre [52]
  a-de [86-INF]". Standing: 94='ne' promoted, 70='pre' banked pencil GT,
  39=/a/ promoted. 94='ne' is the preverbal negation particle and must be
  followed by a verb; 70='pre' is not a verb, so the verb must span 70 —
  it starts with 'pre', ends with 39-83 = "ade", and contains 52
  medially: /^pre.*ade$/. Corpus check: zero French words match in
  29,489,376 chars of 1841-register French ("ade"-final words exist —
  persuade, parade, dégrade, saccade, malade, promenade — none begins
  with "pre"). The "strand 70" rescue is ungrammatical ("ne pré" is not
  French; no clitic reading exists); 52's open value cannot fill a
  corpus-empty set. Phase-fragility verified: row a7_05 has 55 digits
  (odd), so under offset 1 the 39-83 bigram dissolves entirely —
  consistent with the kill, not a rescue. Scope: kills only the
  @1334-specific verb-host instantiation; the word-level 83='de' reading
  ("[pre[52]a] de [86-INF]", de-83-residuals PROMOTE) is untouched and now
  the default fork; syllabic-83 at @614/@1171 unaffected.

- **N379** — syll-83-de-1829 NULL: the '-de'-final VERB fork is fenced at
  kill grade (grammatical impossibility); the '-de'-final NOUN fork
  survives as a live residual. Locus @1829 (row a8_11): "… 00 97 00 86
  29(er) 82(m) [38 83 24] 82 16 59 …". French verb morphology: the ONLY
  verb forms ending in orthographic 'de' are FINITE (1sg/3sg present of
  -der verbs — aide, cède, décide, garde — 2sg imperative). Corpus check
  (76 files, 801 distinct de-final tokens): monde, grande, demande, garde,
  mode, regarde, possède, aide — nouns, adjectives, finite verbs only;
  zero non-finite verb forms. A '-de'-final verb at @1829 would sit
  immediately before 24, a class-level promoted FINITE verb — finite+finite
  adjacency with no conjunction is ungrammatical ("*il aide peut"). The
  fence is grammatical, not evidentiary: it holds regardless of 38's
  future value (38 open, n=7) and regardless of the 83='de' adjudication.
  NOT fenced: the noun fork ("la demande peut" is grammatical). Two
  follow-ups: noun-38de-1829-host (P3 — name the noun, parse the full
  window; candidate shape "[N-de] [24-modal] me [16-INF]"; cf. "mode" if
  38='o'), syll-38-value-census (P3 — 38's 7 windows @384/@826/@1113/
  @1343/@1469/@1650/@1828, name with ≥2 independent legs).

- **N380** — val-42-ne-noun KILL: [42ne]-as-noun-word is dead — no noun
  value for 42 is compatible with a -ne-final French word. Full 20-window
  census of 42 (@79/@205/@219/@266/@282/@428/@464/@488/@493/@543/@784/
  @1072/@1144/@1187/@1410/@1503/@1617/@1794/@1814/@1838). The one-word
  composition can apply only in the three '42 94' windows: @493
  ("78 [42] 94"), @784 ("24 [42] 94"), @1794 ("56 [42] 94"). Compatibility
  demands for stem S: (i) standalone French word; (ii) "er"+S is a French
  word (T3 fence: "29 42"×3); (iii) S+"ne" is a NOUN; (iv) S bare-capable
  (42 is determiner-less in argument positions, `val-42-det-gap`; the
  three windows supply no determiner — 78 is 'ver'-syllable lead, 24 is
  finite-modal, 56 is class-open). Corpus-wide computation over 41,923
  word types (`code/side-period/corpus/`, 59 French files, 34.5M chars;
  723 -ne-final types at freq≥3): exactly ONE stem satisfies (i)+(ii)+
  (iii) — "re" — already killed in noun-42-value (bare "re"/"rêne"
  ungrammatical, 1/20). All others fail: non-word stems (pei/hai/vei/
  scè/…→peine/haine/veine/scène), determiner-requiring nouns
  (chai→chaîne, cor→corne, don→donne, ton→tonne, …) which also fail "er"+S
  (erchai/erlai/erdon/…), pronoun stems (contradict R19-055 noun grant),
  and the "Jean"/"Jeanne" proper-name invention. Window-level
  confirmation: no -ne noun parses bare in the three windows (@784:
  finite-modal 24 + bare noun ungrammatical; bare "erreur" 0/34.4M chars
  vs "l'erreur" 86× — `noun-42-value`). Consequence: the three '42 94'
  windows must parse as "[42-N] + ne(clausal) + X" (composition (b), the
  standing alternative per `subj-42-class` C3). This closes the one-word
  composition entirely — noun was the only live class for [42ne]
  (`frame-42-94-leftward`: verb/adjective/adverb/pronoun arms dead or
  class-contradicting).
