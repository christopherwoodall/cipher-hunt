# Battery report: disloc-demonstrative-epistolary-pausemark

- Target id: `disloc-demonstrative-epistolary-pausemark`
- Claim: "the same bare-head pausemark census on the epistolary sub-corpus (Nesselrode/Talleyrand/Guizot/Metternich/Pozzo/Levant correspondence only)"
- Date: 2026-10-09
- Worker: battery worker (subagent bb11fdbf-68a2-485e-8272-f88422118866)
- Stream: not applicable — corpus census against 19th-century French
  epistolary texts, per target charter. The 1,847-pair repaired parse was
  not used; BATTERY-PROTOCOL §3's stream rule is superseded by the target
  charter here, exactly as in the parent prose battery
  (battery-disloc-demonstrative-prose-pausemark-recall.md). R5005,
  sealed gate instances, and the red-team adjudication queue were not
  touched.

Terms (ASD-STE100): "dislocation" = a topic moved to the front of the
clause, set off by a pause, and resumed by a pronoun. "Bare exclamatory
infinitive" = an infinitive used as an exclamation with no preposition,
no "que", and no resumptive clitic between the topic and the verb
("Moi, voler !"). "Pausemark" = any clause-initial pause separator other
than a comma. "Epistolary sub-corpus" = the correspondence files listed
below, a 13-file, 13,470,962-character subset of
code/side-period/corpus/.

## Parentage

Epistolary-register counterpart of
`disloc-demonstrative-prose-pausemark-recall` (NULL 2026-10-09: 156
dem+separator hits -> 38 with "!" -> 0 genuine in 27.66M chars). Tests
bare demonstrative heads (cela/ceci/ça) only — the reinforced family has
its own batteries. Continues the register family on the same corpus
roots: the governed-family near-misses came from correspondence, which is
why this battery exists.

## Bar (verbatim, pre-registered before testing)

">=1 genuine (cela/ceci/ça) + non-comma pause separator + bare exclamatory infinitive re-opens the epistolary register; confirmed zero fences it"

Numbered pass/fail clauses (restated before testing, not modified after):

1. At least one GENUINE dislocated-demonstrative (cela/ceci/ça) + a
   non-comma pause separator + a bare exclamatory infinitive attestation
   exists in the 13-file epistolary sub-corpus. If yes: the epistolary
   register re-opens for arm (a) of ce87-1028-role (promote).
2. If clause 1's census is a confirmed zero — every candidate
   hand-classified with cause, no unclassified residue — the epistolary
   register is fenced (null per §4: zero is an absence).

## Method

1. Read BATTERY-PROTOCOL.md in full before touching anything. Created the
   lock
   `code/crowd17/next-token/locks/disloc-demonstrative-epistolary-pausemark.lock`
   on start (agent id bb11fdbf-68a2-485e-8272-f88422118866 +
   2026-10-09T09:45:54Z); no prior or stale lock existed for this id.
2. Wrote a re-runnable census script:
   `code/crowd17/next-token/disloc_demonstrative_epistolary_pausemark_census.py`.
   Raw results in
   `code/crowd17/next-token/disloc-demonstrative-epistolary-pausemark_census.json`.
3. P1/P2/P3 copied VERBATIM from the parent prose pausemark battery:
   - P1: `\b(cela|ceci|ça|ca)\s*(?:[!?…:;]|—+|--+|\.{2,})`
     case-insensitive (bare demonstrative + non-comma separator).
   - P2: window (demonstrative .. demonstrative+70) must contain "!"
     before its end.
   - P3: `[a-zàâäçéèêëîïôöùûü']{2,}(er|ir|re|oir)` inside the window
     (infinitive-shaped word); all candidates hand-classified (regex
     cannot separate -er infinitives from nouns/adjectives in -er).
4. Corpus, name-pinned (13 files, 13,470,962 characters) under
   `code/side-period/corpus/`:
   - nesselrode-v7.txt, nesselrode-v8.txt, nesselrode-v9.txt,
     nesselrode-v10.txt (2,346,619 chars)
   - talleyrand-memoires-v1.txt (954,364 chars)
   - guizot-memoires-t1-gutenberg.txt, -t2-gutenberg.txt,
     -t3-gutenberg.txt, -t5-t6.txt (4,610,646 chars)
   - metternich-papiere-v4.txt, metternich-papiere-v6.txt (3,266,383
     chars)
   - pozzo-di-borgo-correspondance-v1.txt (1,029,046 chars)
   - levant-correspondence-1841-p3.txt (1,714,311 chars)
   German files and all drama texts excluded with cause (register is
   French epistolary prose; the target evidence field names these files
   explicitly).
5. The 1,847-pair repaired stream was not used (corpus census per target
   charter); `canonical.py` never touched.

## Window-level evidence

47 demonstrative+non-comma-separator hits -> **6 candidates with "!"**
in the 70-char window -> **0 genuine**, all hand-classified with cause
("@" = character offset of the demonstrative; windows verbatim from the
corpus):

- #1 nesselrode-v9 @207897 "Que dire après cela! Lei, tout / est
  tranquille, on se prépare" — "cela" governed by the preposition
  "après"; "prépare" is the finite verb "on se prépare", false
  infinitive hit. Excluded.
- #2 talleyrand-memoires-v1 @838917 "comment avez-vous oublié cela ?
  Vous êtes toujours / Autrichien !" — "cela" is the object of
  "oublié"; interrogative. Excluded.
- #3 guizot-memoires-t5-t6 @201293 "Si peu de choses méritent qu'on en
  dise / cela! »" — "cela" is the object of "dire"; closes a quoted
  clause. Excluded.
- #4 metternich-papiere-v4 @1148124 "m'a repondu k cela: „Ob! les
  Turcs..." — "cela" governed by "répondu à cela"; "!" is the German
  interjection "Ob!". Excluded.
- #5 metternich-papiere-v6 @840006 "c'est cela! / / Quant a la fin de
  votre travail" — exclamatory "c'est cela!"; "votre" is a -re suffix
  false infinitive hit. Excluded.
- #6 metternich-papiere-v6 @960146 "C'est toujours / cela!" —
  exclamatory NP, no infinitive. Excluded.

Dominant confound classes: preposition/verb-governed demonstratives
(3), exclamatory nominals ("c'est cela!") (2), interrogative (1). No
unclassified residue.

Separator-mark census: bare heads do take non-comma separators in
epistolary prose (47 hits) — but none of those dislocations heads a
bare exclamatory infinitive.

## Per-clause pass/fail

1. ≥1 genuine demonstrative + non-comma separator + bare exclamatory
   infinitive in the epistolary sub-corpus: **FAIL (confirmed zero).**
   47 dem+separator hits -> 6 "!"-candidates -> 0 genuine in
   13,470,962 characters; every candidate excluded with cause.
2. Confirmed zero -> the epistolary register is fenced: **EXECUTED.**
   The register zero is not a separator artifact: demonstratives with
   ! ? : separators were all swept and all head governed clauses,
   interrogatives, or exclamatory nominals — never a bare exclamatory
   infinitive.

## Adverses, answered

- "bare-head family only; German files excluded; drama excluded": kept —
  P1 tests cela/ceci/ça only; German files and drama texts were not
  swept (register is French epistolary prose; the parent battery records
  the same exclusions with cause).
- Self-check: does this null contradict the standing KILL
  (ce87-topic-licensing, bare "ce")? No — this battery tested tonic
  demonstratives, a different construction.
- Self-check: does this null contradict the battery-level NULL
  (ce87-1028-role) whose arm (a) it tests? No — the bar anticipated
  exactly this outcome.
- Self-check: does this null contradict any standing red-team verdict?
  No standing red-team verdict covers the epistolary register for this
  construction; the two correspondence near-misses belong to the
  GOVERNED family, which this battery does not test.
- §7 untouched. No standing or red-team verdict contradicted.

## Verdict: NULL (fence per clause 2 — confirmed zero)

Zero genuine dislocated-demonstrative + non-comma-pausemark + bare
exclamatory infinitive attestations in 13,470,962 characters of
19th-century French correspondence (47 dem+separator hits -> 6
candidates -> 0 genuine; all excluded with cause). Arm (a) of
ce87-1028-role stays fenced in the epistolary register across the
swept separator classes (!, ?, :). Correspondence's two near-misses
remain governed-family phenomena, not bare-head phenomena.

## Follow-ups (nulls regenerate work)

1. **disloc-demonstrative-epistolary-comma-recall** (P4) — comma
   separator recall closure on the 13-file epistolary register (bare
   heads): the governed family produced its near-misses here, but the
   bare family has never been swept with comma separators in this
   register. Bar: ≥1 genuine re-opens the epistolary register;
   confirmed zero fences it fully.
2. **disloc-demonstrative-epistolary-clause-initial** (P4) —
   clause-initial bare demonstratives + bare exclamatory infinitives in
   the epistolary register (mirror of
   disloc-demonstrative-prose-clause-initial, NULL on prose). Bar: ≥1
   genuine re-opens; confirmed zero fences the clause-initial arm in
   epistolary.
3. **disloc-demonstrative-epistolary-pausemark-dash-only-400w** (P4) —
   strict dash-family-only pass with a 400-char window on the
   epistolary register (mirrors the parent battery's prose follow-up
   #1); closes the recall gap on distant infinitives after dash-headed
   demonstratives. Bar: ≥1 genuine re-opens; confirmed zero closes the
   dash arm in epistolary.

Note for the supervisor: none of these three ids is in the queue; they
are not duplicates of any queued or veredicted target.
