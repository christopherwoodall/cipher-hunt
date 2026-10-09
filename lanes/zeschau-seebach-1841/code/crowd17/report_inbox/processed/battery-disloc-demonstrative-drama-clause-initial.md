# Battery report: disloc-demonstrative-drama-clause-initial

- Target id: `disloc-demonstrative-drama-clause-initial`
- Claim: "test the clause-initial demonstrative-topic shape in the drama
  corpus with the preposition/verb-object confound class eliminated"
- Date: 2026-10-09
- Worker: battery worker (subagent b2c5daf5-ae97-4c05-8c7d-417210650ca6)
- Stream: not applicable — corpus census against the ingested drama corpus,
  per target charter. The 1,847-pair repaired parse was not used. R5005,
  sealed gate instances, and the red-team adjudication queue were not
  touched.

Terms (ASD-STE100): "dislocation" = a topic moved to the front of the
clause, set off by a pause, and resumed by a pronoun. "Bare exclamatory
infinitive" = an infinitive used as an exclamation with no preposition, no
"que", and no resumptive clitic between the topic and the verb ("Moi,
voler !"). "Clause-initial" = the demonstrative opens the clause: preceded
(mod whitespace) by [. !? :] or a speaker-label line end or the start of a
speech turn. "Confound class" = mid-clause demonstratives, where the comma
alone suggests a dislocation but the demonstrative is governed by a
preceding preposition or verb.

## Parentage

Follow-up #1 of the battery-level NULL
`disloc-demonstrative-drama-reissue` (2026-10-09). The reissue's census of
the ingested drama corpus found 35 exclamatory candidates, 35/35 classified,
0 genuine — and identified the common confound class behind the three
nearest near-misses: "cela" governed by a PRECEDING preposition or verb,
comma after it, then a bare-looking infinitive ("compromettre tout cela,
risquer ma position, mon crédit !" — Scribe *Bertrand et Raton*;
"après tout cela, avoir peuplé… et rallumé…!" — Musset; "Pour cela, pour
si peu, s'aventurer ainsi !" — Hugo *Ruy Blas*). This battery re-runs the
same corpus with the demonstrative pool restricted to clause-initial
occurrences, so the confound class cannot dilute or mimic a genuine
attestation.

## Bar (verbatim, pre-registered before testing)

"classify all demonstrative-comma windows with strict clause-initial
position gating (>=1 genuine attestation re-opens arm (a) of ce87-1028-role;
confirmed zero fences the topic shape at drama-register level)"

Numbered pass/fail clauses (restated before testing, not modified after):

1. At least one GENUINE clause-initial "cela/ceci/ça, [bare infinitive] !"
   attestation exists in 19th-century French drama. If yes: arm (a) of
   ce87-1028-role re-opens at the drama-register level (promote).
2. If clause 1's census is a confirmed zero — every clause-initial
   candidate window classified, false friends and OCR excluded with cause —
   arm (a) stays fenced at the drama-register level (null per §4:
   inconclusive as a kill, since zero is an absence).

## Method

1. Read BATTERY-PROTOCOL.md first. Created the lock
   `code/crowd17/next-token/locks/disloc-demonstrative-drama-clause-initial.lock`
   on start (agent id + 2026-10-09T08:46:57Z); no prior lock, stale or
   fresh, existed for this id.
2. Wrote a re-runnable census script:
   `code/crowd17/next-token/disloc_demonstrative_drama_clause_initial_census.py`.
   Raw results in
   `code/crowd17/next-token/disloc-demonstrative-drama-clause-initial_census.json`
   (per-file sizes, hit counts, all candidate windows, gate reasons).
3. P1/P2/P3 copied VERBATIM from the reissue script (disloc-demonstrative-inf
   pattern set), not modified after seeing data:
   - P1: `\b(cela|ceci|ça|cel[àa]|cec[iy])\s*[,;:]` case-insensitive.
     Window = text from the demonstrative through the next `[!?.]`,
     capped at 180 characters.
   - P2: the window must contain "!" before its end.
   - P3: `[a-zàâäçéèêëîïôöùûü']{2,}(er|ir|re|oir)` inside the window; all
     candidates classified by hand (regex cannot separate -er infinitives
     from nouns/adjectives in -er).
4. Clause-initial gate (per charter; see correction note below): the
   demonstrative is clause-initial iff the preceding text (mod whitespace)
   ends with start-of-text, a sentence terminator `[. ! ? …]`, a closing
   quote after a terminator, a colon, a turn-initial em-dash or opening
   guillemet, a paragraph break (blank line), or a speaker-label line —
   the latter two requiring the demonstrative to START ITS OWN LINE (so a
   label two lines above a mid-speech "cela" does not promote it). Verse
   line breaks do not count as clause boundaries. All other hits are the
   confound class: counted and listed separately, excluded from the
   candidates.
5. Corpus, named with sizes (character counts, computed in-session) —
   identical 14 files as the reissue, 2,969,582 characters, one edition per
   play (hugo-hernani.txt excluded, hugo-hernani-1870.txt kept): see the
   reissue report's file table; per-file counts are in the census JSON.

### Gate-rule correction (recorded, not hidden)

The first draft of the gate applied the speaker-label rule without
requiring the demonstrative to start its own line. Wider context
(±150 chars) on the 3 "clause-initial" candidates it produced showed all
three were mid-speech ("c'est sacré, cela, chevalier !"; "…dirigé tout
cela, qui m'a mis…"; "avec tout cela, je suis volé d'un millier…") — the
speaker label sat two lines above, not at turn start. I tightened the rule
(the demonstrative must start its own line for the label/paragraph rules)
and re-ran the FULL census from scratch; the final numbers below are from
the corrected run. The bar was not rewritten — this was a gate-bug fix,
and it is conservative in the verdict-relevant direction: the tightened
gate only REMOVES hits from the clause-initial pool, and every hit in
both pools was classified, so no genuine attestation could hide in either
pool.

## Window-level evidence

- 190 demonstrative-comma hits → **12 clause-initial** → **0 clause-initial
  exclamatory candidates** (P2+P3). Clause 1 is a confirmed zero.
- 11 confound-class exclamatory candidates (mid-clause + P2 + P3), ALL
  excluded with cause — same taxonomy as the reissue, confirming the
  confound class is exactly what the charter predicted ("@ = character
  offset of the demonstrative in the file; / = line break in source):

dumas-antony.txt:
1. @69365 `cela, et ce serait dommage ; vous, bâtie de fleurs et de gaze,
   vous voulez aimer et être aimée d'amour ; ah !` — "aimer"/"être aimée"
   governed by the finite modal "vous voulez". Excluded with cause.
dumas-kean.txt:
2. @119377 `cela, sous prétexte qu'il est noble, qu'il est lord, qu'il
   est pair… Ah !` — "pair" is a noun (a peer); no infinitive. Excluded.
dumas-mariage-louis-xv-1841.txt:
3. @101348 `cela, che- /valier !` — wider context: "c'est sacré, cela,
   chevalier ! Ah ! vous êtes un bon ami…" — "cela" is mid-speech after
   "c'est sacré," and "che-valier" dissolves to the noun "chevalier"
   (vocative; OCR line-break hyphenation). Excluded with cause.
dumas-tour-de-nesle.txt:
4. @129575 `cela, qui m'a mis au cœur cet amour bizarre, tout de mère et
   pas d'amante !` — wider context: "…qui a dirigé tout cela, qui m'a mis
   au cœur…" — relative clause, finite "a mis"; "mère"/"bizarre" are a
   noun/adjective in -re, false infinitive-shaped hits. Excluded with
   cause.
hugo-hernani-1870.txt:
5. @185467 `cela, c'est assez I^ / En maudissant tout bas le mendiant
   avide / Auquel il faut jeter le fond du verre vide!` — "c'est" finite;
   "jeter" governed by "il faut"; "I^" is OCR noise. Excluded with cause.
hugo-ruy-blas.txt:
6. @74859 `cela, pour si peu, s'aventurer ainsi !` — wider context: "Pour
   m'apporter les fleurs qu'on me refuse ici, / Pour cela, pour si peu,
   s'aventurer ainsi !" — "cela" is the object of the preposition "pour",
   not a fronted topic (verse line break is not a clause boundary).
   Excluded with cause (reissue near-miss #3).
musset-comedies-proverbes-1850.txt:
7. @21031 `cela, avoir /peuplé un palais d'ouvrages magnifiques, et
   rallumé le feu sacré des arts, prêt à s'éteindre à Florence!` — wider
   context: "…les bénédictions de la patrie à recevoir, et, après tout
   cela, avoir peuplé un palais…" — "cela" is the object of "après";
   infinitives governed by the preposition. Excluded with cause (reissue
   near-miss #1).
8. @63055 `cela, mou cher seigneur, et puisse le ciel venir à /votre
   aide !` — "mou" = OCR "mon" (vocative); "venir" governed by finite
   "puisse". Excluded with cause.
9. @88090 `cela, je suis volé d'un millier /de ducats !` — wider context:
   "…avec tout cela, je suis volé d'un millier de ducats !" — finite "je
   suis"; "millier" is a noun in -er. Excluded with cause.
scribe-bertrand-et-raton.txt:
10. @21271 `cela, risquer ma position, mon crédit !` — wider context:
    "…et j'irais compromettre tout cela, risquer ma position, mon crédit
    !…" — "cela" is the direct object of "compromettre"; "risquer" is a
    serial infinitive governed by "j'irais". Excluded with cause (reissue
    near-miss #2).
scribe-verre-d-eau.txt:
11. @91030 `cela, il faut le connaître !` — "connaître" governed by "il
    faut". Excluded with cause.

- The 12 clause-initial demonstrative-comma hits themselves: none is
  followed by an exclamatory-infinitive shape at all (0 pass P2+P3) — the
  register's clause-initial demonstratives head imperatives, finite
  clauses, interjections, and quotations, never bare exclamatory
  infinitives.
- Due diligence: the reissue's shape precedent stands — Hernani's
  "Gouverner tout cela !" proves the bare exclamatory infinitive is
  grammatical in drama; the demonstrative-headed, clause-initial variant
  is absent.

## Per-clause pass/fail

1. ≥1 genuine clause-initial "cela/ceci/ça, [bare infinitive] !"
   attestation in 19th-century French drama: **FAIL (confirmed zero).**
   190 dem-comma hits → 12 clause-initial → 0 exclamatory candidates
   across 2,969,582 characters of drama. The 11 confound-class candidates
   are all excluded with cause (governed by preceding verb/preposition:
   7; noun or false infinitive-shaped: 3; finite clause: remaining).
2. Confirmed zero → arm (a) of ce87-1028-role fenced at the drama-register
   level: **EXECUTED.** Zero is an absence, not a refutation — the "Moi,
   voler !" precedent and Hernani's "Gouverner tout cela !" prove the
   exclamatory-infinitive shape is grammatical and present in drama, so
   the demonstrative-headed version stays possible-but-unattested. Per §4
   this is a **null**, not a kill. The fence now holds against the
   confound class explicitly: none of the three reissue near-misses
   survives clause-initial gating.

## Adverses, answered

- None pre-registered ("Adverses: null").
- Self-check: does this null contradict the standing KILL
  (ce87-topic-licensing, bare "ce" cannot head an exclamatory infinitive)?
  No — this battery tested tonic demonstratives, a different
  construction; the kill stands untouched.
- Self-check: does this null contradict the battery-level NULL
  (disloc-demonstrative-inf) or the parent NULL
  (disloc-demonstrative-drama-reissue)? No — it is the chartered
  follow-up #1 of the reissue and hardens its fence against the confound
  class.
- Self-check: the in-run gate correction (above) is recorded with its
  rationale and its conservative direction; the final verdict does not
  depend on which rule version was used, since both pools were fully
  classified.

## Verdict: NULL (fence per clause 2 — confirmed zero in the drama register)

Zero genuine clause-initial dislocated-demonstrative +
bare-exclamatory-infinitive attestations in 2,969,582 characters of
19th-century French drama (190 dem-comma hits → 12 clause-initial → 0
exclamatory candidates; 11 confound-class candidates all excluded with
cause: 7 verb/preposition-governed, 3 noun/false-infinitive-shaped, the
rest finite clauses). All three reissue near-misses ("compromettre tout
cela, risquer…", "après tout cela, avoir peuplé…", "Pour cela, pour si
peu, s'aventurer ainsi !") fall in the confound class on the corrected
gate. Arm (a) of ce87-1028-role stays fenced at the drama-register level,
now explicitly against the confound class.

## Follow-ups (nulls regenerate work)

1. **disloc-demonstrative-prose-clause-initial** (P2): apply the same
   strict clause-initial gate to the 27.66M-char PROSE corpus
   (disloc-demonstrative-inf: 35 candidates → 0 genuine). Bar: ≥1 genuine
   clause-initial attestation in prose re-opens the shape outside drama;
   confirmed zero hardens the fence in the prose register against the
   same confound class.
2. **disloc-demonstrative-drama-pausemark-recall** (P3): the clause-initial
   pool was tiny (12 of 190) — a pause-mark recall audit: clause-initial
   demonstratives NOT followed by comma/semicolon/colon (e.g. "cela !",
   "cela —", "cela…") checked for exclamatory-infinitive continuations.
   Bar: ≥1 genuine with a non-comma pause mark re-opens the shape;
   confirmed zero closes the pause-mark variant.
3. Note for the supervisor: `disloc-demonstrative-drama-edition-delta`,
   `disloc-tonic-personal-census`, `disloc-reinforced-prep-inf-drama`,
   and `disloc-demonstrative-drama-dialogue` are already queued — none of
   the two proposed above duplicates them.

## Bookkeeping

- Census script:
  code/crowd17/next-token/disloc_demonstrative_drama_clause_initial_census.py
  (re-runnable; outputs
  disloc-demonstrative-drama-clause-initial_census.json with per-file
  sizes, hit counts, gate reasons, and all candidate windows).
- Report: code/crowd17/report_inbox/battery-disloc-demonstrative-drama-clause-initial.md
  (this file).
- battery-queue.json: `disloc-demonstrative-drama-clause-initial`
  queued -> verdict/null via temp-file + rename (pre-write assert
  confirmed queued/verdictless; JSON re-validated post-write; own entry
  only; claim/bars/evidence/adverses preserved).
- Lock created on start (agent id b2c5daf5-ae97-4c05-8c7d-417210650ca6 +
  2026-10-09T08:46:57Z); no stale lock existed. Deleted on completion
  (verified gone).
- R5005, sealed gates, red-team queue untouched. Every number traces to
  the named corpus files or the census script; no invented data.
