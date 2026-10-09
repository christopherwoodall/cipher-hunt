# Battery report: disloc-demonstrative-prose-clause-initial

- Target id: `disloc-demonstrative-prose-clause-initial`
- Claim: "apply the strict clause-initial gate to the demonstrative-comma census on the 27.66M-char prose corpus"
- Date: 2026-10-09
- Worker: battery worker (subagent 0407135c-be6b-4746-a672-6eb443714bab)
- Stream: not applicable — corpus census against 19th-century French prose,
  per target charter. The 1,847-pair repaired parse was not used. R5005,
  sealed gate instances, and the red-team adjudication queue were not
  touched.

Terms (ASD-STE100): "dislocation" = a topic moved to the front of the
clause, set off by a pause, and resumed by a pronoun. "Bare exclamatory
infinitive" = an infinitive used as an exclamation with no preposition, no
"que", and no resumptive clitic between the topic and the verb ("Moi,
voler !"). "Clause-initial" = the demonstrative opens the clause: preceded
(mod whitespace) by a sentence terminator, a colon, a turn-initial dash or
opening quote, a paragraph break, a speaker-label line end (demonstrative
must start its own line), or start of text. "Confound class" =
mid-clause demonstratives, where the comma alone suggests a dislocation but
the demonstrative is governed by a preceding preposition or verb.

## Parentage

Prose-register counterpart of
`disloc-demonstrative-drama-clause-initial` (NULL 2026-10-09). Both are
follow-ups of `disloc-demonstrative-inf` (NULL 2026-10-09: 447 dem-comma
hits -> 15 excl candidates -> 0 genuine in 27.66M chars). The strict
clause-initial gate re-runs the prose corpus with the demonstrative pool
restricted to clause-initial occurrences, so the preposition/verb-object
confound class cannot dilute or mimic a genuine attestation.

## Bar (verbatim, pre-registered before testing)

">=1 genuine clause-initial demonstrative + bare exclamatory infinitive
in prose re-opens arm (a) of ce87-1028-role; confirmed zero fences the
topic shape in prose too"

Numbered pass/fail clauses (restated before testing, not modified after):

1. At least one GENUINE clause-initial "cela/ceci/ça, [bare infinitive] !"
   attestation exists in 19th-century French prose. If yes: arm (a) of
   ce87-1028-role re-opens (promote).
2. If clause 1's census is a confirmed zero — every clause-initial
   candidate window classified, false friends and OCR excluded with cause —
   the topic shape stays fenced in prose too (null per §4: zero is an
   absence).

## Method

1. Read BATTERY-PROTOCOL.md first. Created the lock
   `code/crowd17/next-token/locks/disloc-demonstrative-prose-clause-initial.lock`
   on start (agent id + 2026-10-09T08:52:00Z); no prior lock, stale or
   fresh, existed for this id.
2. Wrote a re-runnable census script:
   `code/crowd17/next-token/disloc_demonstrative_prose_clause_initial_census.py`.
   Raw results in
   `code/crowd17/next-token/disloc-demonstrative-prose-clause-initial_census.json`
   (per-file sizes, hit counts, all candidate windows, gate reasons).
3. P1/P2/P3 copied VERBATIM from the parent script
   (`disloc_demonstrative_census.py`, not modified after seeing data):
   - P1: `\b(cela|ceci|ça|cel[àa]|cec[iy])\s*[,;:]` case-insensitive.
     Window = text from the demonstrative through the next `[!?.]`,
     capped at 180 characters.
   - P2: the window must contain "!" before its end.
   - P3: `[a-zàâäçéèêëîïôöùûü']{2,}(er|ir|re|oir)` inside the window; all
     candidates classified by hand (regex cannot separate -er infinitives
     from nouns/adjectives in -er).
4. Clause-initial gate copied VERBATIM from
   `disloc_demonstrative_drama_clause_initial_census.py` (including the
   corrected speaker-label/paragraph rule: the demonstrative must START
   ITS OWN LINE for label/paragraph rules; verse line breaks do not count
   as clause boundaries).
5. Corpus, named with sizes (character counts, computed in-session) —
   identical set to `disloc-demonstrative-inf`:
   - 1841-register prose (code/side-period/corpus/): 17 files,
     26,319,515 characters — guizot-memoires t1/t2/t3/t5-t6, nesselrode
     v7/v8/v9/v10, revue-deux-mondes-1841 q1/q2/q3/q4,
     metternich-papiere v4/v6, talleyrand-memoires-v1,
     pozzo-di-borgo-correspondance-v1, levant-correspondence-1841-p3.
   - Wider 19th century (data/): 3 files, 1,336,670 characters —
     gutenberg-17489-miserables1.txt (Les Misérables tome 1, 1862),
     gutenberg-30513-tocqueville-t1.txt, gutenberg-30514-tocqueville-t2.txt.
   - Total: 20 files, 27,656,185 characters. German files (allgemeine-zeitung
     14 issues, adb-zeschau-heinrich-anton-von.txt) and all drama texts
     excluded with cause (register is French prose; drama has its own
     batteries).

## Window-level evidence

- 447 demonstrative-comma hits → **16 clause-initial** → **0 clause-initial
  exclamatory candidates** (P2+P3). Clause 1 is a confirmed zero.
- All 16 clause-initial hits themselves head finite-clause continuations,
  never bare exclamatory infinitives ("@" = character offset of the
  demonstrative; windows verbatim from the corpus):

  1. guizot-memoires-t5-t6 @541440: "Cela, interprété au vrai, signifie
     qu'après avoir accepté l'alliance russe…" — finite "signifie".
  2. nesselrode-v10 @237982: "ça, est-ce que ce n'est pas fini toutes ces
     bêtises?" — finite "est-ce que".
  3. nesselrode-v9 @142309: "cela, il verra de près le mic-mac de
     Francfort…" — finite "il verra".
  4. rdm-1841-q1 @609591: "Ceci, pour commencer, n'était pas tout-à-fait
     juste…" — finite "n'était".
  5. rdm-1841-q1 @2672508: "Ceci, dit-il, tient n notre vie privée…" —
     finite "tient".
  6. rdm-1841-q1 @2710648: "Cela, me disais-je, ne peut se passer…" —
     finite "ne peut".
  7. rdm-1841-q2 @1830294: "Cela, je le sais, est fort difficile…" —
     finite "je le sais".
  8. rdm-1841-q2 @1844279: "cela, j'en conviens, il ne faut pas partir…" —
     finite "il ne faut".
  9. rdm-1841-q3 @1431808: "Cela, du reste, n'est point particulier à
     l'Orient…" — finite "n'est".
  10. rdm-1841-q3 @2812794: "Ceci, dit au fort de la colère…, tombait en
      plein sur le frère…" — finite "tombait".
  11. metternich-v6 @1077674: "Cela, mon eher Comte, est de l'histoire et
      non pas du roman." — finite "est".
  12. metternich-v6 @1434288: "Ceci, sans doute, est possible, mais ne
      saurait produire…" — finite "est".
  13. levant-correspondence-1841-p3 @1294400: "cela, tout ce que j'aurais
      dit n'aurait servi a rien, je pris le parti de me taire…" — finite.
  14. miserables1 @314496: "Ceci, mesdames, que vous buvez d'un air
      tranquille, est du vin de Madère…" — finite "est".
  15. miserables1 @463879: "Cela, ce n'est rien." — finite "ce n'est".
  16. tocqueville-t2 @94606: "Ceci, du reste, ne se rapporte point
      uniquement à la science administrative." — finite "ne se rapporte".

- 4 confound-class exclamatory candidates (mid-clause + P2 + P3), ALL
  previously classified as false friends in `disloc-demonstrative-inf`
  (candidate numbers refer to that battery), all excluded with cause:
  1. metternich-papiere-v6 @860050: "ceci, — Fun en de*pit et aux depens
     de Fautre!" — OCR noise ("Fun"/"Fautre" = German "von" misread);
     inf-hit "fautre". (inf candidate #2.)
  2. miserables1 @299519: "cela, même pour rire!" — the infinitive "rire"
     is governed by the preposition "pour"; not a bare infinitive.
     Nearest near-miss in the whole census. (inf candidate #9.)
  3. miserables1 @307350: "cela, elle erre gaîment, la douce amourette!"
     — finite clause ("elle erre"); "amourette" is a noun in -re, false
     infinitive-shaped hit. (inf candidate #10.)
  4. miserables1 @601675: "ça, je ne peux pas dire, on parle contre moi,
     on me dit: répondez!" — finite clause ("je ne peux pas dire"); the
     "!" is a downstream imperative. (inf candidate #15.)

- Due diligence: the "Moi, voler !" shape precedent (rdm-1841-q1, quoted
  speech) re-confirms that the tonic-topic + bare-exclamatory-infinitive
  SHAPE is grammatical in 1841 prose — only the demonstrative head is
  absent. Clause-initial demonstratives in prose head finite clauses,
  imperatives, and interjections, never bare exclamatory infinitives.

## Per-clause pass/fail

1. ≥1 genuine clause-initial "cela/ceci/ça, [bare infinitive] !" in
   19th-century French prose: **FAIL (confirmed zero).** 447 dem-comma
   hits → 16 clause-initial → 0 exclamatory candidates in 27,656,185
   characters of prose; the 16 clause-initial hits all head finite
   clauses. The 4 confound-class candidates are all excluded with cause
   (1 OCR noise, 3 grammatical false friends).
2. Confirmed zero → topic shape fenced in prose too: **EXECUTED.** Zero is
   an absence, not a refutation — the "Moi, voler !" precedent proves the
   shape is grammatical, so the demonstrative-headed version stays
   possible-but-unattested. Per §4 this is a **null**, not a kill. Arm (a)
   of ce87-1028-role now stays fenced in BOTH registers against the
   confound class: drama (drama-clause-initial: 190 → 12 → 0) and prose
   (this battery: 447 → 16 → 0).

## Adverses, answered

- None pre-registered ("Adverses: None").
- Self-check: does this null contradict the standing KILL
  (ce87-topic-licensing, bare "ce")? No — this battery tested tonic
  demonstratives, a different construction.
- Self-check: does this null contradict the battery-level NULL
  (ce87-1028-role) whose arm (a) it tests? No — the bar anticipated
  exactly this outcome ("confirmed zero fences the topic shape in prose
  too").
- Self-check: no new red-team venue opened. §7 untouched.

## Verdict: NULL (fence per clause 2 — confirmed zero in the prose register)

Zero genuine clause-initial dislocated-demonstrative +
bare-exclamatory-infinitive attestations in 27,656,185 characters of
19th-century French prose (447 dem-comma hits → 16 clause-initial → 0
exclamatory candidates; all 16 head finite clauses; 4 confound-class
candidates all excluded with cause: 1 OCR noise, 1 "pour"-governed
infinitive, 2 finite clauses). Arm (a) of ce87-1028-role stays fenced in
prose as well as drama.

## Follow-ups (nulls regenerate work)

1. **disloc-demonstrative-inversion-prose** (P3): the postposed order
   ("[inf] !, cela") was fenced in drama and in the RDM full corpus but
   never in the prose corpus. Bar: ≥1 genuine inversion in prose
   re-opens arm (a) via the inverted order; confirmed zero fences it in
   prose too.
2. **disloc-demonstrative-1770-1820** (P4): test the shape in a pre-1841
   literary prose corpus — determines whether the fence is a period
   effect. Bar: ≥1 genuine pre-1841 attestation bounds the fence
   chronologically; confirmed zero extends the fence backward.
3. **bare-excl-inf-head-inventory-prose** (P4): positive-space complement —
   inventory what CAN head a bare exclamatory infinitive in prose
   (personal tonic pronouns, reinforced heads). Bar: a ranked head-class
   inventory; if demonstratives sit inside a licensed class, the
   grammatical blocker is weakened.

Note for the supervisor: none of these duplicates the queued
`disloc-demonstrative-inversion-fullcorpus` (RDM scope),
`disloc-demonstrative-inversion-verbtags`, or `bare-excl-inf-head-inventory-drama`
(drama scope) batteries.
