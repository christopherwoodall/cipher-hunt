# Battery report: gov-excl-inf-drama-n2

- Target id: `gov-excl-inf-drama-n2`
- Claim: "widen the drama corpus to test whether the governed exclamatory
  infinitive attestation is Scribe-idiolect or drama-wide"
- Date: 2026-10-09
- Worker: battery worker (subagent 81ae14d0-f60c-4803-9012-48f86f0d45c9)
- Stream: not applicable — corpus census against widened 19th-century French
  drama, per target charter (identical P1/P2 taxonomy as the parent drama
  battery). The 1,847-pair repaired parse was not used. R5005, sealed gate
  instances, and the red-team adjudication queue were not touched.

Terms (ASD-STE100, inherited from the parent battery
`gov-excl-inf-register-drama`): "governed exclamatory infinitive" = an
infinitive governed by a preposition (pour / a / de) used as an exclamation
in its own right ("pour rire !" = the infinitive phrase IS the exclaimed
element, with or without a dislocated topic). "Genuine attestation" = the
"!" terminates the governed infinitive phrase itself; the infinitive is
not embedded in a finite matrix clause whose "!" belongs to the matrix,
and not embedded in an exclaimed noun/adjective/pronoun phrase.
"Register" = the widened ingested drama corpus (14 new files, listed
below), i.e. drama files NOT covered by the parent battery.

## Parentage

Follow-up of the PROMOTE `battery-gov-excl-inf-register-drama`
(2026-10-09). That battery found 1 genuine governed exclamatory infinitive
in 839 candidates across 14 drama files (Scribe, *Bertrand et Raton*:
"Pour conspirer !…" — a dialogue-anaphoric fragment, n=1). The thin
attestation left the question open whether the construction is
Scribe-idiolectal or drama-wide. This battery runs the IDENTICAL P1/P2
census against the newly-ingested widening files (3 more Scribe plays, 12
more Labiche comedies from the Scribe/Labiche comedy-extension and
wider-corpus fr.wikisource harvests, 2026-10-09).

## Bar (verbatim, pre-registered before testing)

">=1 genuine in a non-Scribe play confirms drama-wide; zero outside Scribe
fences it as Scribe-idiolect"

Numbered pass/fail clauses (restated before testing, not modified after):

1. >=1 genuine governed exclamatory infinitive (per the parent taxonomy)
   in a non-Scribe play in the widened corpus: if yes, the construction
   is drama-wide — not Scribe-idiolectal.
2. Zero genuine outside Scribe in the widened corpus: if yes, the
   attestation fences as Scribe-idiolectal.

## Method

1. Read BATTERY-PROTOCOL.md first. Created the lock
   `code/crowd17/next-token/locks/gov-excl-inf-drama-n2.lock` on start
   (agent id + UTC timestamp 2026-10-09T12:10:30Z; no stale lock for this
   id existed); deleted on completion.
2. Reproducible census script:
   `code/crowd17/next-token/gov_excl_inf_drama_n2_census.py` (P1/P2
   verbatim from `gov_excl_inf_register_drama_census.py`; DRAMA lists
   replaced with the widening files). Raw results in
   `code/crowd17/next-token/gov-excl-inf-drama-n2_census.json` (per-file
   sizes, "!" counts, all 515 candidate windows with prep/infinitive/dist
   fields). Full per-candidate classification in
   `code/crowd17/next-token/gov-excl-inf-drama-n2_classification.json`
   (genuine/excluded + cause code for every candidate).
3. Corpus — the widened drama corpus (14 files NOT censused by the parent;
   all provenance in `code/side-period/corpus/PROVENANCE.md`, Scribe/
   Labiche comedy extension families):
   - New Scribe (3): scribe-charlatanisme.txt (*Le Charlatanisme*,
     1825), scribe-le-lorgnon.txt (*Le Lorgnon*), scribe-le-savant.txt
     (*Le Savant*).
   - New Labiche (11): labiche-29-degres-ombre.txt,
     labiche-affaire-rue-lourcine.txt, labiche-baron-fourchevif.txt,
     labiche-doit-on-le-dire.txt, labiche-edgard-bonne.txt,
     labiche-la-cagnotte.txt, labiche-main-leste.txt,
     labiche-misanthrope-auvergnat.txt, labiche-noces-bouchencoeur.txt,
     labiche-prix-martin.txt, labiche-voyage-perrichon.txt.
   (labiche-chapeau-de-paille.txt and
   labiche-martin-poudre-aux-yeux.txt were censused by the parent and
   are excluded here; the excluded second Hernani edition is not drama
   widening.)
4. Search patterns (verbatim, identical to the parent battery):
   - P1 (candidate): for every "!" in the corpus, take the 120 chars
     before it; run GOV_INF
     `\b(pour|à|a|de|d[''])\s+(?:[a-z...]{1,6}\s+){0,2}\b[a-z...]{2,}
     (er|ir|re|oir)\b` (case-insensitive) on that segment; keep the
     match closest to the "!"; between its end and the "!" there
     must be no [.;].
   - P2 (banding): dist = characters from the end of the
     infinitive-shaped word to the "!". Tight band dist <= 40 (364
     candidates) is the discriminating band; wide band
     41 <= dist <= 120 (151 candidates) triaged separately.
   - All 515 candidates classified by hand (regex cannot separate
     -er infinitives from nouns/adjectives in -er; unaccented "a"
     is verb-avoir noise; the "!" may belong to a matrix finite
     clause or a following interjection).

## Window-level evidence

### Census yields

- New Scribe: 3 files, 216,179 chars, 889 "!", 34 candidates (23 tight,
  11 wide).
- New Labiche: 11 files, 814,659 chars, 8,283 "!", 481 candidates (341
  tight, 140 wide).
- **6 of 515 candidates are genuine.** All 515 classified; the 509
  exclusions follow the parent taxonomy, below.

### The genuine attestations

1. (scribe-le-savant.txt, a/louer, dist 1) — "…qui est à louer pour
   quinze florins par mois, car j'ai vu écriteau. HANTZ. À louer !"
   Hantz's echo fragment: the "!" terminates the governed infinitive
   phrase "à louer" itself. No finite matrix in his turn; not embedded
   in an exclaimed NP. Same fragment grade as the parent's "Pour
   conspirer !…". Genuine, Scribe.
2. (labiche-edgard-bonne.txt, pour/causer, dist 1) — "Edgard. Pour quoi
   faire ? Florestine, appuyant. Pour lui causer !" Q/A fragment: the
   reply's "!" terminates the governed infinitive phrase. No finite
   matrix in the reply. Genuine, NON-Scribe (Labiche).
3. (labiche-edgard-bonne.txt, pour/polker, dist 1) — "Edgard. Pour quoi
   faire ? Henriette. Pour polker !" Same Q/A shape. Genuine,
   NON-Scribe (Labiche).
4. (labiche-voyage-perrichon.txt, pour/etre, dist 8) — "PERRICHON
   Puisque tu as demandé un congé. MAJORIN Pas pour être témoin !"
   Negated reply fragment; the "!" terminates "pour être témoin" (the
   negation "pas" does not change the shape). Genuine, NON-Scribe
   (Labiche).
5. (labiche-prix-martin.txt, de/quitter, dist 10) — "…ce n'était pas
   tant de passer l'arme à gauche que de te quitter. Martin, à part.
   Oui, oui ! de quitter ma femme !" Echo fragment completing the
   "pas tant… que" construction. Genuine, NON-Scribe (Labiche).
6. (labiche-misanthrope-auvergnat.txt, pour/mettre, dist 20) —
   "Chiffonnet, vous portez perruque ?… Chiffonnet. Oh ! oh ! au
   carnaval seulement… pour me mettre en garde-française !" Elliptical
   fragment; no finite verb anywhere in the turn (unlike the excluded
   verre-d-eau near-miss, which had an elliptical "c'était" matrix).
   Genuine, NON-Scribe (Labiche).

Attestation sources: 4 distinct Labiche plays (Edgard et sa bonne,
Le Voyage de M. Perrichon, Le Prix Martin, Le Misanthrope et
l'Auvergnat) and 1 Scribe play (Le Savant).

### Exclusion causes (509 windows, all with cause)

**Cause A — OCR "-er" false friends** (the infinitive-shaped word is a
noun/adjective/name/idiom: lisière, chambrière, notaire, charbonnière,
colère, foyer, l'heure, bonne heure, nature, mere, sucre, février,
grammaire, mois (plénipotentiaire), madère, votre, quatre, rivière,
mystère, etc.). Largest class.
**Cause B — governed infinitive embedded in a finite matrix clause**
whose "!" belongs to the matrix. Examples: "Je n'aime pas à voyager
comme ça !", "C'est pour rire !", "je vous défends de me suivre !",
"c'est si ridicule de se teindre !", "Vous ne pouvez pas m'obliger à
aller à Paris !", "je suis curieux de voir ce bonhomme-là !".
**Cause C — infinitive embedded in an exclaimed noun/adjective/
pronoun phrase** (the phrase is exclaimed, not the infinitive).
Examples: "Quel plaisir / De pouvoir tous se réunir !" (exclaimed NP
"quel plaisir"); "Rien à faire !" / "rien pour corrompre ce geôlier !"
(exclaimed pronoun "rien"); "Effroyable ! effroyable à imaginer !" and
"Impossible de me rappeler !" (exclaimed adjectives).
**Cause D — "!" belongs to a following interjection or quoted clause.**
Examples: "…à me promener en long et en large ?… Ah !" (L18 Scribe);
"pour lui dire… Ah !" (L110/L202); "Elle remonte… pour dire :) Vous
m'entendez !…" (L238/L327, "!" belongs to the quoted clause).
**Cause BARE-HEAD — exclaimed head is a bare infinitive**, the
governed infinitive being its complement (like the parent's "Ecrire a
un tapissier !"): "Lui apprendre à mentir !… Voilà une drôle d'idée !"
(L70, L277); "M'exposer à vous faire une visite !" (S12 Scribe); "Etre
assis près de ce qu'on aime !" (LW21/LW39/LW99/LW135, song lyric with
bare head).
Wide band (151 candidates): all 151 triaged with cause — no candidate
with the "!" terminating the governed infinitive phrase (the "!"
belongs to a following finite clause, a following interjection, or a
quoted cry in every case; spot-checked: "Pour lui faire mes adieux…
Sois tranquille…" carries no standalone "!" after "adieux").

## Per-clause pass/fail

1. >=1 genuine governed exclamatory infinitive in a non-Scribe play:
   **PASS.** 5 genuine in 4 non-Scribe (Labiche) plays: "Pour lui
   causer !", "Pour polker !", "Pas pour être témoin !",
   "de quitter ma femme !", "pour me mettre en garde-française !".
   The construction is drama-wide — not Scribe-idiolectal.
2. Zero genuine outside Scribe fences it as Scribe-idiolect:
   **ANTECEDENT FALSE.** Non-Scribe attestation exists; the
   Scribe-idiolect fence does not stand.

## Verdict: PROMOTE

The governed exclamatory infinitive attests in non-Scribe drama (5
genuine in 4 Labiche plays, out of 481 new-Labiche candidates), so it
is drama-wide, not Scribe-idiolectal. Cumulative drama state
(parent + this battery): 28 files, 4,000,420 chars, 22,384 "!",
1,354 candidates, 6 genuine (2 Scribe, 4 Labiche) — the register
boundary for the prose null stands, and the construction's habitat is
19th-century dramatic dialogue broadly.

### Caveats (stated, not hidden)

- All 6 genuine (parent + this battery) are dialogue-anaphoric or
  elliptical fragments (Q/A replies, echo fragments), at the same
  fragment grade as the parent's "Pour conspirer !…". A fully
  conventionalized standalone ("pour rire !") remains unattested in
  the drama corpus.
- The new non-Scribe attestations are all Labiche (comedy). Non-comic
  drama (Dumas x5, Hugo x3, Musset, Vigny in the parent corpus) still
  shows zero — the construction may be comedy-drama-skewed rather
  than uniformly drama-wide; that is a residual, not a verdict input
  (this battery's bar asked Scribe vs drama-wide only).

## Adverses, answered

- None pre-registered ("Adverses: none listed").
- Self-check: does this promote contradict the standing drama PROMOTE
  (battery-gov-excl-inf-register-drama)? No — it extends it (Scribe n=1
  → drama-wide n=6). The parent report is not overwritten.
- Self-check: does this contradict any standing red-team verdict?
  No — no red-team verdict covers governed infinitives.
- Self-check: are the Labiche genuine too elliptical to count? They
  are graded identically to the parent's genuine "Pour conspirer !…"
  (dialogue-anaphoric fragment, "!" terminating the governed
  infinitive phrase itself); the fragment grade is recorded as a
  caveat so the red team can grade it.

## Follow-ups (promote; optional, not mandatory)

1. **gov-excl-inf-drama-comedy-skew**: test whether the construction
   is comedy-drama-skewed — census more non-comic 19th-c. drama
   (tragedies/dramas beyond Dumas/Hugo/Musset/Vigny) to see whether
   the Labiche concentration reflects a comedy register within drama.
2. **gov-excl-inf-drama-n3**: re-run the identical census on any
   further drama ingest (e.g. more Scribe/Labiche beyond this
   widening) to keep the genuine count above n and test for a fully
   conventionalized standalone.

## Bookkeeping

- Census script:
  code/crowd17/next-token/gov_excl_inf_drama_n2_census.py (re-runnable;
  P1/P2 verbatim from the parent battery; outputs
  gov-excl-inf-drama-n2_census.json with per-file sizes, "!" counts,
  and all 515 candidate windows with prep/infinitive/dist fields).
- Classification:
  code/crowd17/next-token/gov-excl-inf-drama-n2_classification.json
  (genuine/excluded + cause code for every candidate; 6 genuine, 509
  excluded).
- Report: code/crowd17/report_inbox/battery-gov-excl-inf-drama-n2.md
  (this file).
- battery-queue.json: `gov-excl-inf-drama-n2` queued ->
  verdict/promote via temp-file + rename (pre-write assert
  confirmed queued/verdictless; JSON re-validated post-write; own
  entry only; claim/bars/evidence/adverses preserved).
- Lock created on start (agent id + UTC timestamp
  2026-10-09T12:10:30Z), deleted on completion. No stale lock for
  this target existed.
- R5005, sealed gates, red-team queue untouched. Every number traces
  to the named corpus files or the census/classification scripts; no
  invented data.
