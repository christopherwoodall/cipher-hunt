# Battery report: gov-excl-inf-register-drama

- Target id: `gov-excl-inf-register-drama`
- Claim: "corpus-wide census of governed exclamatory infinitives
  ('pour rire !', 'a donner lecture !', 'de croire !') with ANY topic
  in the drama corpus (drama-side arm of the prose
  gov-excl-inf-register)"
- Date: 2026-10-09
- Worker: battery worker (subagent 19d594f2-e849-4bca-99f2-7490e28dc5f9)
- Stream: not applicable — corpus census against period French drama,
  per target charter (same taxonomy as the prose battery). The
  1,847-pair repaired parse was not used. R5005, sealed gate
  instances, and the red-team adjudication queue were not touched.

Terms (ASD-STE100): "governed exclamatory infinitive" = an infinitive
governed by a preposition (pour / a / de) used as an exclamation in
its own right ("pour rire !" = the infinitive phrase IS the exclaimed
element, with or without a dislocated topic). "Genuine attestation" =
the "!" terminates the governed infinitive phrase itself; the
infinitive is not embedded in a finite matrix clause whose "!"
belongs to the matrix, and not embedded in an exclaimed noun phrase.
"Register" = the ingested drama corpus (14 distinct plays, listed
below).

## Parentage

Follow-up #1 of the NULL `battery-gov-excl-inf-register`
(2026-10-09). That battery found 0 genuine governed exclamatory
infinitives in 27,657,940 characters of 19th-century French print
(859/859 candidates classified) and framed the zero as
register-level. This battery runs the IDENTICAL P1/P2 census (any
topic) against the drama corpus — the natural habitat of
exclamatory infinitives — to test whether the zero is
print-register-specific or generalizes.

## Bar (verbatim, pre-registered before testing)

">=1 genuine governed exclamatory infinitive with a non-demonstrative
topic in drama locates the register boundary; confirmed zero
generalizes the prose null"

Numbered pass/fail clauses (restated before testing, not modified
after):

1. >=1 genuine governed exclamatory infinitive (pour / a / de +
   infinitive as the exclaimed element, non-demonstrative or zero
   topic) in the drama corpus: if yes, the register boundary is
   located — the construction exists in drama, and the prose null is
   print-register-specific. The pairing re-opens at register level.
2. Confirmed zero in drama: if yes, the prose null generalizes —
   the construction is absent from both registers and the fence
   hardens.

## Method

1. Read BATTERY-PROTOCOL.md first. Created the lock
   `code/crowd17/next-token/locks/gov-excl-inf-register-drama.lock`
   on start (agent id + UTC timestamp 2026-10-09T08:46:47Z; no stale
   lock for this id existed); deleted on completion.
2. Ran a reproducible census script:
   `code/crowd17/next-token/gov_excl_inf_register_drama_census.py`
   (P1/P2 verbatim from
   `gov_excl_inf_register_census.py`). Raw results in
   `code/crowd17/next-token/gov-excl-inf-register-drama_census.json`
   (per-file sizes, "!" counts, all 839 candidate windows with
   prep/infinitive/dist fields).
3. Corpus — the ingested drama corpus (14 files, 2,969,582
   characters, 13,212 "!"; counts recomputed in-session):
   dumas-antony.txt, dumas-henri-iii.txt, dumas-kean.txt,
   dumas-mariage-louis-xv-1841.txt, dumas-tour-de-nesle.txt,
   hugo-burgraves.txt, hugo-hernani-1870.txt (kept per the
   one-edition-per-play rule), hugo-ruy-blas.txt,
   labiche-chapeau-de-paille.txt,
   labiche-martin-poudre-aux-yeux.txt,
   musset-comedies-proverbes-1850.txt, scribe-bertrand-et-raton.txt,
   scribe-verre-d-eau.txt, vigny-chatterton-1835.txt.
   hugo-hernani.txt excluded (second Hernani edition). German files
   and the 1841-prose French files excluded with cause (wrong
   register; same exclusion as the sibling drama batteries).
4. Search patterns (verbatim, identical to the prose battery):
   - P1 (candidate): for every "!" in the corpus, take the 120 chars
     before it; run GOV_INF
     `\b(pour|a|de|d[''])\s+(?:[a-z...]{1,6}\s+){0,2}\b[a-z...]{2,}
     (er|ir|re|oir)\b` (case-insensitive) on that segment; keep the
     match closest to the "!"; between its end and the "!" there
     must be no [.;].
   - P2 (banding): dist = characters from the end of the
     infinitive-shaped word to the "!". Tight band dist <= 40 (524
     candidates) is the discriminating band; wide band
     41 <= dist <= 120 (315 candidates) triaged separately.
   - All 839 candidates classified by hand (regex cannot separate
     -er infinitives from nouns/adjectives in -er; unaccented "a"
     is verb-avoir noise; the "!" may belong to a matrix finite
     clause).

## Window-level evidence

### Census yields

- Drama register: 839 candidates (524 tight, 315 wide) from
  13,212 "!" in 2,969,582 characters.
- **1 of 839 candidates is genuine.** All 839 classified; the 838
  exclusions follow the prose battery's taxonomy, below.

### The genuine attestation (tight band, dist 1)

- (scribe-bertrand-et-raton.txt, pour/conspirer, dist 1) — the full
  exchange verbatim:
  - LA REINE: "Vous me refusez, vous, qui en secret aviez toujours
    pris ma defense, vous en qui j'esperais !…"
  - RANTZAU: "Pour conspirer !… Votre majeste avait grand tort."
  - Rantzau's turn is a standalone exclamation: the "!" terminates
    the pour-infinitive phrase itself. No finite matrix clause in
    his turn; not embedded in an exclaimed noun phrase. Zero topic
    (elliptical; the anaphor is the Queen's "vous me refusez").
    It is an ironic/elliptical purpose exclamation ("[You think I
    refuse] to conspire?!"), with the governed infinitive phrase as
    the exclaimed element — exactly the "pour rire !" shape, with a
    non-demonstrative (zero) topic.

### Positive controls (the census detects the shape)

The BARE exclamatory infinitive DOES attest in the drama corpus,
proving the zero in prose is not a detection failure:
- (scribe-bertrand-et-raton.txt) "Ecrire a un tapissier !… quand
  je suis la a ecrire a une reine !" — genuine bare exclamatory
  infinitive ("a un tapissier" is its complement, not a governor).
- (vigny-chatterton-1835.txt) "Ouvrir son coeur pour le mettre en
  etalage sur un comptoir !" — genuine bare exclamatory infinitive
  with a pour-purpose adjunct (the exclaimed element is the bare
  infinitive "Ouvrir son coeur", not the governed phrase).
- (hugo-hernani-1870.txt) "Gouverner tout cela !" — bare
  exclamatory infinitive (reported by the sibling drama batteries).

### Exclusion causes (838 windows, all with cause)

**Cause A — OCR "-er" false friends** (the infinitive-shaped word is
a noun/adjective/name: autre, grand'mere, lumiere, chair, marbre,
heure, frere, lettre, fenetre, derniere, colere, misere, chambre,
terre, verre, matiere, caractere, nature, titre, gageure, premier,
derniere, propre, contre, quatre, pierre, poudre, heure, koller,
tapissier, Alexandre, palefrenier, meurtrier, vinaigre, soeur...).
Largest class. Examples: "Pour une autre !", "des hommes de
marbre !", "C'est un coup de foudre !", "un lit d'auberge a mon
heure derniere !".

**Cause B — governed infinitive embedded in a finite matrix clause**
whose "!" belongs to the matrix. Examples:
- (hugo-burgraves.txt) "Rien ne m'empechera de le frapper !"
- (musset-comedies-proverbes-1850.txt) "permettez-moi de vous
  parler !"
- (dumas-henri-iii.txt) "Oh ! s'il pouvait m'aimer assez peu pour
  ne pas venir !"
- (dumas-antony.txt) "c'est a faire douter de la bonte celeste !"
- (hugo-ruy-blas.txt) "Epousez donc un roi pour vivre de la
  sorte !" (imperative matrix)
- (scribe-verre-d-eau.txt) "c'etait pour une affaire grave et
  importante… pour savoir jusqu'a quel point on m'abusait… pour
  connaitre enfin la verite !" (purpose adjunct of an elliptical
  matrix — the nearest wide near-miss; the "!" terminates the
  purpose chain as an adjunct, not a standalone exclamatory
  infinitive)

**Cause C — infinitive embedded in an exclaimed noun/adjective/
participial phrase** (the phrase is exclaimed, not the infinitive).
Examples:
- (musset-comedies-proverbes-1850.txt) "cent chefs-d'oeuvre a
  rapporter, cent artistes pauvres et souffrants a guerir, a
  enrichir !"; "le role d'un bon ange a jouer !"; "Renzo, un homme
  a craindre !"
- (hugo-ruy-blas.txt) "Quel beau role a jouer !"
- (vigny-chatterton-1835.txt) "Ecrit trop vite ! — Ecrit pour
  vivre !" — the exclaimed element is the participial phrase
  "Ecrit"; "pour vivre" is its purpose complement (excluded with
  cause; not the "pour rire !" shape)
- (musset-comedies-proverbes-1850.txt) "Quelle haine pour ce
  pauvre duc !"

**Cause D — "!" belongs to a following interjection, not the
infinitive.** Examples: "Le revoir ! Oh !", "Si je lui disais que
le seul desir de le voir… ah !", "tu auras aide a me sauver…
Oh !".

## Per-clause pass/fail

1. >=1 genuine governed exclamatory infinitive with a
   non-demonstrative topic in drama: **PASS.** 1 genuine of 839
   candidates: "Pour conspirer !" (Scribe, Bertrand et Raton,
   Rantzau's elliptical protest; zero topic). The register boundary
   is located — the construction exists in dramatic dialogue. The
   prose null is print-register-specific: dialogue licenses the
   elliptical standalone form that print prose never shows.
2. Confirmed zero generalizes the prose null: **ANTECEDENT
   FALSE.** The zero does not hold in drama.

## Verdict: PROMOTE

One genuine governed exclamatory infinitive in the drama corpus
(Scribe, Bertrand et Raton: "Pour conspirer !") locates the
register boundary for the prose null. The governed exclamatory
infinitive is absent from 27.66M characters of 19th-century French
print (859/859 classified, 0 genuine) but attests in dramatic
dialogue — the natural habitat of elliptical standalone
exclamations. The pairing (governed exclamatory infinitive +
zero/implied topic) re-opens at register level.

### Caveats (stated, not hidden)

- The promotion rests on n=1 genuine of 839 candidates. The
  register-boundary claim is thin but meets the pre-registered
  ">=1 genuine" bar.
- The attestation is a dialogue-anaphoric fragment: it completes
  the Queen's previous turn ("vous me refusez [pour conspirer]!").
  It is not a fully conventionalized standalone like "pour rire !".
  It passes the prose battery's strict taxonomy (the "!"
  terminates the governed infinitive phrase itself; not embedded
  in a finite matrix or an exclaimed NP), but the elliptical
  character is recorded so the red team can grade it.
- The drama corpus has ~4.5x the "!" density of the prose corpus;
  dialogue ellipsis is its natural habitat. This is the mechanism
  of the register boundary, not a contradiction of the prose null.

## Adverses, answered

- None pre-registered ("Adverses: none listed").
- Self-check: does this promote contradict the standing prose NULL
  (battery-gov-excl-inf-register)? No — different register; the
  prose battery's zero stands, and its explanation ("register
  absence from print") is now qualified as print-register
  specific. The prose report is not overwritten.
- Self-check: does this contradict any standing red-team verdict?
  No — no red-team verdict covers governed infinitives.
- Self-check: could "Pour conspirer !" be read as an elliptical
  purpose clause rather than an exclamatory infinitive? Recorded
  as a caveat above; under the parent battery's strict taxonomy it
  is genuine, and the bar's >=1 criterion was pre-registered.

## Follow-ups (promote; optional, not mandatory)

1. **gov-excl-inf-drama-n2**: widen the drama corpus (the excluded
   second Hernani edition, more Scribe/Labiche comedy per
   disloc-reinforced-comedy-extension) to raise the genuine count
   above n=1 and test whether the construction is drama-wide or
   Scribe-idiolectal.
2. **gov-excl-inf-drama-recall**: close this battery's recall gaps
   ("?"-terminated exclamatory infinitives, preposition-to-
   infinitive spans longer than two short tokens, dash/colon pause
   marks) — same fenced gaps as the prose battery.

## Bookkeeping

- Census script:
  code/crowd17/next-token/gov_excl_inf_register_drama_census.py
  (re-runnable; P1/P2 verbatim from the prose battery; outputs
  gov-excl-inf-register-drama_census.json with per-file sizes,
  "!" counts, and all 839 candidate windows with
  prep/infinitive/dist fields).
- Report: code/crowd17/report_inbox/battery-gov-excl-inf-register-drama.md
  (this file).
- battery-queue.json: `gov-excl-inf-register-drama` queued ->
  verdict/promote via temp-file + rename (pre-write assert
  confirmed queued/verdictless; JSON re-validated post-write; own
  entry only; claim/bars/evidence/adverses preserved).
- Lock created on start (agent id + UTC timestamp
  2026-10-09T08:46:47Z), deleted on completion. No stale lock for
  this target existed.
- R5005, sealed gates, red-team queue untouched. Every number
  traces to the named corpus files or the census script; no
  invented data.
