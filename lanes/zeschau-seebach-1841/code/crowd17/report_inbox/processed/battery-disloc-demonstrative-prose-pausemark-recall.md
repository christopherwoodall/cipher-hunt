# Battery report: disloc-demonstrative-prose-pausemark-recall

- Target id: `disloc-demonstrative-prose-pausemark-recall`
- Claim: "the pausemark census extends to the 27.66M-char prose corpus"
- Date: 2026-10-09
- Worker: battery worker (subagent 4d692ded-2de4-42c3-a9ab-4e0721ec9878)
- Stream: not applicable — corpus census against 19th-century French prose,
  per target charter. The 1,847-pair repaired parse was not used. R5005,
  sealed gate instances, and the red-team adjudication queue were not
  touched.

Terms (ASD-STE100): "dislocation" = a topic moved to the front of the
clause, set off by a pause, and resumed by a pronoun. "Bare exclamatory
infinitive" = an infinitive used as an exclamation with no preposition,
no "que", and no resumptive clitic between the topic and the verb
("Moi, voler !"). "Pausemark" = any clause-initial pause separator other
than a comma. "Confound class" = mid-clause demonstratives, where the
pause mark alone suggests a dislocation but the demonstrative is governed
by a preceding preposition or verb.

## Parentage

Prose-register counterpart of `disloc-demonstrative-drama-pausemark-recall`
(NULL 2026-10-09: 307 demonstrative+non-comma-separator hits -> 120 with
"!" -> 0 genuine in 14 drama plays). Tests bare demonstrative heads
(cela/ceci/ça) only — the reinforced family has its own pausemark battery
(`disloc-reinforced-pausemark-prose-recall`, NULL: 1 dem-pausemark hit in
27,657,940 chars, a footnote artifact, 0 candidates). Continues the
prose-register family: `disloc-demonstrative-inf` (NULL: 447 dem-comma
hits -> 15 candidates -> 0 genuine) and
`disloc-demonstrative-prose-clause-initial` (NULL: 447 -> 16 clause-initial
-> 0 genuine), both on this exact 21-file prose corpus.

## Bar (verbatim, pre-registered before testing)

"Extend the pausemark census to the 27.66M-char prose corpus; >=1 genuine
re-opens arm (a) in prose via non-comma separators; confirmed zero confirms
the prose zero is not a separator artifact either"

Numbered pass/fail clauses (restated before testing, not modified after):

1. At least one GENUINE dislocated-demonstrative (cela/ceci/ça) + bare
   exclamatory infinitive attestation with a non-comma pause separator
   exists in 19th-century French prose. If yes: arm (a) of
   ce87-1028-role re-opens in prose (promote).
2. If clause 1's census is a confirmed zero — every candidate classified,
   false friends and OCR excluded with cause — the prose zero is not a
   separator artifact (null per §4: zero is an absence).

## Method

1. Read BATTERY-PROTOCOL.md first. Created the lock
   `code/crowd17/next-token/locks/disloc-demonstrative-prose-pausemark-recall.lock`
   on start (agent id + 2026-10-09T09:25:41Z); no prior lock existed for
   this id.
2. Wrote a re-runnable census script:
   `code/crowd17/next-token/disloc_demonstrative_prose_pausemark_recall_census.py`.
   Raw results in
   `code/crowd17/next-token/disloc-demonstrative-prose-pausemark-recall_census.json`.
3. P1/P2/P3 copied VERBATIM from the drama pausemark battery:
   - P1: `\b(cela|ceci|ça|ca)\s*(?:[!?…:;]|—+|--+|\.{2,})`
     case-insensitive (bare demonstrative + non-comma separator).
   - P2: window must contain "!" before its end.
   - P3: `[a-zàâäçéèêëîïôöùûü']{2,}(er|ir|re|oir)` inside the window
     (infinitive-shaped word); all candidates hand-classified (regex
     cannot separate -er infinitives from nouns/adjectives in -er).
4. Corpus, name-pinned and byte-identity asserted against the parent
   batteries (character counts matched in-session):
   - 1841-register prose (`code/side-period/corpus/`): 18 files,
     25,670,258 characters — guizot-memoires t1/t2/t3/t5-t6, nesselrode
     v7/v8/v9/v10, revue-deux-mondes-1841 q1/q2/q3/q4,
     metternich-papiere v4/v6, talleyrand-memoires-v1,
     pozzo-di-borgo-correspondance-v1, levant-correspondence-1841-p3.
   - Wider 19th century (`data/`): 3 files, 1,987,682 characters —
     gutenberg-17489-miserables1.txt (Les Misérables tome 1, 1862),
     gutenberg-30513-tocqueville-t1.txt, gutenberg-30514-tocqueville-t2.txt.
   - Total: 21 files, 27,657,940 characters. German files and all drama
     texts excluded with cause (register is French prose; drama has its
     own batteries).
5. The 1,847-pair repaired stream was not used (corpus census per target
   charter); `canonical.py` never touched.

## Window-level evidence

156 demonstrative+non-comma-separator hits -> **38 candidates with "!"**
in the 70-char window -> **0 genuine**, all hand-classified with cause
("@" = character offset of the demonstrative; windows verbatim from the
corpus):

- #1 guizot-memoires-t5-t6 @201293 "qu'on en dise / cela! »" — "cela" is
  the object of "dire". Excluded.
- #2 metternich-papiere-v4 @1148124 "m'a repondu k cela: „Ob! les
  Turcs..." — governed by "répondu à cela". Excluded.
- #3 metternich-papiere-v6 @840006 "c'est cela! / / Quant a la fin de
  votre travail" — exclamatory "c'est cela!"; "votre" is a -re suffix
  false infinitive hit. Excluded.
- #4 metternich-papiere-v6 @960146 "C'est toujours / cela!" —
  exclamatory NP, no infinitive. Excluded.
- #5 nesselrode-v9 @207897 "Que dire après cela! Lei, tout / est
  tranquille, on se prépare" — "cela" governed by "après"; "prépare"
  is the finite verb "on se prépare", false infinitive hit. Excluded.
- #6/#7 rdm-1841-q1 @94521/@103594 "Ceci!" in garbled footnote OCR
  ("Dniry à Ceci!, 2!) mars 15Cr", "parle secret lire de Ceci!") —
  footnote reference, not a dislocation. Excluded.
- #8 rdm-1841-q1 @1446022 "j'ai donc pu faire cela !" — "cela" is the
  object of "faire"; "première" is the adjective "à la première
  occasion", false infinitive hit. Excluded.
- #9 rdm-1841-q2 @313774 "la forme, rien que cela! / / Sous l'empire" —
  exclamatory NP "rien que cela!"; "empire" is a noun, false hit.
  Excluded.
- #10 rdm-1841-q2 @403126 "c'est bien cela!... Allons, allons" —
  "c'est cela", no infinitive. Excluded.
- #11/#12/#19 rdm-1841-q2 @1011885, @1446264; rdm-1841-q4 @921954 "Ah
  ça!" / "Ah! ça!" — interjections; "faire" (#11) is the finite clause
  "venez-vous faire ici?"; "venir" (#19) is "voulez-vous en venir?".
  Excluded.
- #13 rdm-1841-q3 @1391512 "je lui fasse un reproche de cela!" —
  preposition-governed "de cela". Excluded.
- #14 rdm-1841-q3 @2620958 "comment dois-je entendre / ceci?" — "ceci"
  is the object of "entendre"; "marcher" is the finite clause "je ne
  puis marcher encore !". Excluded.
- #15 rdm-1841-q4 @56980 "vous avez découvert cela!" — finite clause.
  Excluded.
- #16 rdm-1841-q4 @235596 "Cest cela!" — "c'est cela", no infinitive.
  Excluded.
- #17 rdm-1841-q4 @752604 "C'est horrible, cela!" — postposed
  demonstrative, but the exclamation is the nominal "C'est horrible",
  no infinitive. Excluded.
- #18 rdm-1841-q4 @836509 "Ruses que tout cela! mensonges imaginés pour
  auto- / riser vos visites !" — exclamatory NP; the infinitive
  "autoriser" sits inside a finite-clause exclamation and "tout cela"
  is its subject, not a topic. Excluded.
- #20 rdm-1841-q4 @1167225 "Il ne manquait plus que cela!" — "cela" is
  the object of "manquer". Excluded.
- #21/#22 rdm-1841-q4 @1261252/@1722425 "c'est infâme, cela!" /
  "c'est affreux, cela!" — exclamatory nominals, no infinitives.
  Excluded.
- #23 rdm-1841-q4 @2652611 "pas plus / difficile que cela!" —
  comparative complement, no infinitive. Excluded.
- #24 talleyrand-memoires-v1 @838917 "comment avez-vous oublié cela ?" —
  object of "oublié". Excluded.
- #25 miserables1 @171235 "gagner cela?" — object of "gagner". Excluded.
- #26 miserables1 @185498 "comme cela!" — adverbial "comme cela";
  "rire" is the noun "avec un rire". Excluded.
- #27 miserables1 @237446 "recevoir un homme comme cela! et le loger à
  côté de soi!" — adverbial "comme cela"; the infinitives sit inside
  the finite-matrix exclamation ("a-t-on idée! ... on songe!").
  Excluded.
- #28 miserables1 @317165 "fichue bête comme ça!" — adverbial, no
  infinitive. Excluded.
- #29 miserables1 @407146 "quarante francs! que ça!" — exclamatory NP,
  no infinitive. Excluded.
- #30 miserables1 @495048 "qu'est-ce qu'il y a de / malheureux dans
  ceci?" — interrogative. Excluded.
- #31 miserables1 @499851 "entendu par ceci: 'Mon but est atteint!'" —
  "par ceci" governed by the preposition "par". Excluded.
- #32/#33 miserables1 @499898 "Il fallait faire cela!" / "s'il ne
  faisait pas cela!" — "cela" is the object of "faire". Excluded.
- #34 miserables1 @507179 "c'est de l'égoïsme / tout cela!" —
  exclamatory NP, no infinitive. Excluded.
- #35 miserables1 @510333 "n'est pour cela!" — preposition-governed
  "pour cela". Excluded.
- #36/#38 miserables1 @547389/@648743 "Comment cela?" / "Qui ça?" —
  interrogatives. Excluded.
- #37 miserables1 @565187 "c'est un tel / mystère que tout cela!" —
  exclamatory NP, no infinitive. Excluded.

Dominant confound classes: demonstrative as object of the preceding
verb/preposition (~15), exclamatory nominals ("c'est cela!", "rien que
cela!") (~9), interjections "Ah ça!" (~3), adverbials "comme cela"
(~3), interrogatives (~4), footnote OCR (~2). No unclassified residue.

Separator-mark census: the reinforced family found dashes essentially
absent after reinforced heads in prose (1 footnote artifact in 27.7M
chars). Bare heads DO take dashes/colons/ellipses/question marks in
prose (156 hits here) — but none of those dislocations heads a bare
exclamatory infinitive.

## Per-clause pass/fail

1. ≥1 genuine demonstrative + bare exclamatory infinitive with a
   non-comma separator in prose: **FAIL (confirmed zero).** 156
   dem+separator hits -> 38 "!"-candidates -> 0 genuine in
   27,657,940 characters; every candidate excluded with cause.
2. Confirmed zero -> not a separator artifact: **EXECUTED.** The prose
   zero cannot be hiding behind a different pause mark: demonstratives
   with ! ? … — -- ... : ; separators were all swept and all head
   finite clauses, governed clauses, interjections, or exclamatory
   nominals — never a bare exclamatory infinitive.

## Adverses, answered

- "Does not duplicate disloc-reinforced-pausemark-prose-recall": kept —
  this battery tests the BARE-head family (cela/ceci/ça), the other
  battery the REINFORCED-head family (celui-là, etc.). Findings are
  complementary: reinforced heads show near-zero dash/ellipsis use in
  prose; bare heads use them (156 hits) but never before a bare
  exclamatory infinitive.
- Self-check: does this null contradict the standing KILL
  (ce87-topic-licensing, bare "ce")? No — this battery tested tonic
  demonstratives, a different construction.
- Self-check: does this null contradict the battery-level NULL
  (ce87-1028-role) whose arm (a) it tests? No — the bar anticipated
  exactly this outcome.
- §7 untouched. No standing or red-team verdict contradicted.

## Verdict: NULL (fence per clause 2 — confirmed zero)

Zero genuine dislocated-demonstrative + bare-exclamatory-infinitive
attestations with non-comma pause separators in 27,657,940 characters of
19th-century French prose (156 dem+separator hits -> 38 candidates ->
0 genuine; all excluded with cause). Arm (a) of ce87-1028-role stays
fenced in prose across every separator class: comma, semicolon, colon,
question mark, exclamation mark, ellipsis, em/en dash, hyphen.

## Follow-ups (nulls regenerate work)

1. **disloc-demonstrative-prose-pausemark-dash-only** (P4) — strict
   dash-family-only pass with a 400-char window (dash dislocation is the
   one live 19th-century prose mark; recall-gap closure on distant
   infinitives). Bar: ≥1 genuine re-opens; confirmed zero closes the
   dash arm in prose.
2. **disloc-demonstrative-epistolary-pausemark** (P3) — the same bare-head
   pausemark census on the epistolary sub-corpus (Nesselrode/Talleyrand/
   Guizot/Metternich/Pozzo/Levant correspondence only); correspondence
   produced the two near-misses of the governed family. Bar: ≥1 genuine
   re-opens the epistolary register; confirmed zero fences it.
3. **tonic-vs-demonstrative-topic-census** (P4) — quantify the licensing
   contrast as a grammar fact: tonic-pronoun topics license bare
   exclamatory infinitives (drama inventory: 5 genuine) while
   demonstrative topics never do (0 genuine across ~29M drama + 27.7M
   prose chars in the bare family). Bar: a ranked head-class table;
   re-check whether any demonstrative-headed shape survives the joint
   tally.

Note for the supervisor: the following were already queued and are NOT
re-proposed: `disloc-demonstrative-1770-1820`,
`disloc-demonstrative-inversion-prose-1800-1820`,
`bare-excl-inf-head-inventory-prose`, `arm-a-fence-ratify`.
