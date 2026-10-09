# Battery report: disloc-demonstrative-drama-reissue

- Target id: `disloc-demonstrative-drama-reissue`
- Claim: "re-run the drama battery with the same pre-registered bars once the
  drama corpus is ingested"
- Date: 2026-10-09
- Worker: battery worker (subagent 21d4ff9b-0ab0-441b-a580-b8449fe1e5e7)
- Stream: not applicable — corpus census against the ingested drama corpus,
  per target charter. The 1,847-pair repaired parse was not used. R5005,
  sealed gate instances, and the red-team adjudication queue were not
  touched.

Terms (ASD-STE100): "dislocation" = a topic moved to the front of the clause,
set off by a pause, and resumed by a pronoun. "Bare exclamatory infinitive" =
an infinitive used as an exclamation with no preposition, no "que", and no
resumptive clitic between the topic and the verb ("Moi, voler !").

## Parentage

This is follow-up #3 of the battery-level NULL `disloc-demonstrative-drama`
(2026-10-09, verdict: null, untestable — no drama corpus existed in the lane
then). The blocker was corpus, not method: two ingest passes have since
landed in `code/side-period/corpus/` — (a) 4 archive.org files (Family 9,
PROVENANCE.md) and (b) 11 fr.wikisource files ("Family — 19th-century French
drama, wikisource ingest"), totalling 15 drama files / 14 distinct plays
(Hernani in two editions). This reissue retires the original null by running
its exact bars on the ingested corpus. The ingest battery itself
(2026-10-09, verdict: promote) ran a partial version of the census over the
4 archive.org files only and found a confirmed zero there; this reissue runs
the full corpus with the original battery's pattern set and classifies every
candidate independently.

## Gate check

The dispatch gate named 11 files / 1,573,255 chars (the wikisource batch
alone, commit 517a0075). The corpus dir now holds 15 drama files; per the
task's corpus note ("Hernani exists in two editions in the corpus — use ONE
edition per play"), the census ran on 14 files (2,969,582 characters),
excluding `hugo-hernani.txt` (second Hernani edition, fr.wikisource Hetzel
1889 — noted in PROVENANCE.md; kept `hugo-hernani-1870.txt`, the edition the
ingest battery's census used). The gate corpus is fully contained in the
census corpus. If the corpus had been absent, this would have been a null —
it was not.

## Bar (verbatim, pre-registered before testing)

"same pre-registered bars as disloc-demonstrative-drama, run against the
ingested drama corpus"

Numbered pass/fail clauses (restated before testing, not modified after;
inherited verbatim from disloc-demonstrative-drama):

1. At least one GENUINE "cela/ceci/ça, [bare infinitive] !" attestation in
   19th-century French DRAMA exists. If yes: arm (a) of ce87-1028-role is
   strengthened to promote-grade (promote).
2. If clause 1's census is a confirmed zero — every candidate window
   classified, false friends and OCR excluded with cause — arm (a) stays
   fenced at the drama-register level (null per §4: inconclusive as a kill,
   since zero is an absence).

## Method

1. Read BATTERY-PROTOCOL.md first. Created the lock
   `code/crowd17/next-token/locks/disloc-demonstrative-drama-reissue.lock`
   on start (no prior lock, stale or fresh, existed for this id).
2. Wrote a re-runnable census script:
   `code/crowd17/next-token/disloc_demonstrative_drama_reissue_census.py`.
   Raw results in
   `code/crowd17/next-token/disloc-demonstrative-drama-reissue_census.json`.
3. Patterns copied VERBATIM from `disloc_demonstrative_census.py`
   (disloc-demonstrative-inf), not modified after seeing data:
   - P1 (dislocation): `\b(cela|ceci|ça|cel[àa]|cec[iy])\s*[,;:]`
     case-insensitive. Window = text from the demonstrative through the
     next `[!?.]`, capped at 180 characters.
   - P2 (exclamatory filter): the window must contain "!" before its end.
   - P3 (infinitive candidate): `[a-zàâäçéèêëîïôöùûü']{2,}(er|ir|re|oir)`
     inside the window; all candidates classified by hand (regex cannot
     separate -er infinitives from nouns/adjectives in -er).
4. Cross-check pass (from the ingest battery's inline census): strict
   `(cela|ceci|ça)[,;:…] (≤1 short word) [inf-er/ir/re] !` within 50 chars,
   plus a loose `(cela|ceci|ça) …[inf]…!` within 35 chars; all loose hits
   inspected with ±90 chars of context.
5. Corpus, named with sizes (character counts, computed in-session) —
   14 files, 2,969,582 characters of 19th-century French drama:
   - dumas-antony.txt: 102,234 — Dumas père, *Antony* (drame, 1831)
   - dumas-henri-iii.txt: 128,462 — Dumas père, *Henri III et sa cour* (1829)
   - dumas-kean.txt: 152,233 — Dumas père, *Kean* (drame, 1836)
   - dumas-mariage-louis-xv-1841.txt: 204,641 — Dumas père, *Un mariage
     sous Louis XV* (1841)
   - dumas-tour-de-nesle.txt: 132,586 — Dumas père, *La Tour de Nesle* (1832)
   - hugo-burgraves.txt: 151,408 — Hugo, *Les Burgraves* (drame, 1843)
   - hugo-hernani-1870.txt: 203,769 — Hugo, *Hernani* (1830), Jenkins 1870
     ed. (the second Hernani edition, hugo-hernani.txt / Hetzel 1889,
     excluded with cause per the one-edition-per-play rule)
   - hugo-ruy-blas.txt: 198,265 — Hugo, *Ruy Blas* (drame, 1838)
   - labiche-chapeau-de-paille.txt: 118,567 — Labiche & Marc-Michel, *Un
     chapeau de paille d'Italie* (comédie-vaudeville, 1851)
   - labiche-martin-poudre-aux-yeux.txt: 87,042 — Labiche & Martin, *La
     Poudre aux yeux* (comédie, 1861)
   - musset-comedies-proverbes-1850.txt: 972,696 — Musset, *Comédies et
     proverbes* (10 plays incl. Lorenzaccio, Le Chandelier, On ne badine
     pas avec l'amour), Poitiers 1850
   - scribe-bertrand-et-raton.txt: 182,448 — Scribe, *Bertrand et Raton*
     (comédie, 1833)
   - scribe-verre-d-eau.txt: 146,451 — Scribe, *Le Verre d'eau* (comédie,
     1840)
   - vigny-chatterton-1835.txt: 188,780 — Vigny, *Chatterton* (1835)
   Distinct plays: ~23 across the 14 files. All public domain (authors
   d. 1861–1888; editions pre-1923); provenance in PROVENANCE.md.

## Window-level evidence

- 190 demonstrative-comma hits → 35 exclamatory candidates (P1/P2/P3);
  cross-check: 1 strict hit, 35 loose hits.
- **0 of 35 candidates is genuine.** Classification below (all windows shown
  verbatim; "/" marks line breaks in the source; @ = character offset of
  the demonstrative in the file):

dumas-antony.txt:
1. @13240 `cela, va !` — "va" is the imperative of aller, not an infinitive.
   Excluded with cause.
2. @69365 `cela, et ce serait dommage ; vous, bâtie de fleurs et de gaze,
   vous voulez aimer et être aimée d'amour ; ah !` — finite clause ("vous
   voulez"); "aimer"/"être aimée" are governed by the modal "vouloir", not
   a bare exclamatory infinitive. Excluded with cause.

dumas-kean.txt:
3. @35666 `ça, moi !` — pronoun interjection, no verb.
4. @65809 `ça, lui ; mais nous autres !` — pronoun, no verb.
5. @119377 `cela, sous prétexte qu'il est noble, qu'il est lord, qu'il est
   pair… Ah !` — "pair" is a noun (a peer); no infinitive. Excluded with
   cause.

dumas-mariage-louis-xv-1841.txt:
6. @44415 `cela, moi !` — interjection.
7. @101348 `cela, che- / valier !` — the STRICT cross-check's single hit;
   dissolves to "chevalier" (OCR line-break hyphenation), a noun. Excluded
   with cause.
8. @122127 `cela, mon oncle, je peux vous en répon- / dre, parole
   d'honneur!` — finite "je peux"; "répondre" governed by "pouvoir".
   Excluded with cause.

dumas-tour-de-nesle.txt:
9. @129575 `cela, qui m'a mis au cœur cet amour bizarre, tout de mère et
   pas d'amante !` — relative clause with finite "a mis"; "mère"/"bizarre"
   are a noun/adjective in -re, false infinitive-shaped hits. Excluded with
   cause.

hugo-burgraves.txt:
10. @80459 `ceci : / / Si tout est en repos au fond de vos pensées, / / Si
    rien, en méditant vos actions passées, / / Ne trouble vos cœurs, purs
    comme le ciel est bleu, / / Vivez, riez, chantez!` — colon introduces a
    conditional with finite imperatives ("vivez, riez, chantez" are
    imperative 2pl forms, not infinitives). Excluded with cause.
11. @145006 `cela, par grâce !` — interjection, no verb at all.

hugo-hernani-1870.txt:
12. @185467 `cela, c'est assez I^ / En maudissant tout bas le mendiant
    avide / Auquel il faut jeter le fond du verre vide!` — "c'est" finite;
    "jeter" governed by "il faut"; "I^" is OCR noise. Excluded with cause.

hugo-ruy-blas.txt:
13. @74859 `cela, pour si peu, s'aventurer ainsi !` — context: "Pour
    m'apporter les fleurs qu'on me refuse ici, / Pour cela, pour si peu,
    s'aventurer ainsi !" — "cela" is the object of the preposition "pour"
    ("pour cela" = "for that"), not a fronted topic; the exclamatory
    infinitive "s'aventurer" is not headed by a dislocated demonstrative.
    Excluded with cause (nearest near-miss #3).

labiche-chapeau-de-paille.txt:
14. @11270 `ça : « Bah !` — quotation introduction, interjection.
15. @34682 `ça : « Mon Dieu !` — quotation introduction, interjection.

labiche-martin-poudre-aux-yeux.txt:
16. @19881 `ça, ils sont très gentils !` — finite clause.
17. @48985 `ça, je me tais !` — finite clause.
18. @62669 `Ça, je l'ai vu ; sept à huit pieds !` — finite clause.
19. @72673 `ça, quand le faux à l'air vrai… ce n'est plus du faux !` —
    finite clause.
20. @75702 `ça, c'est du sentiment… ça nous éloigne !` — finite "c'est".

musset-comedies-proverbes-1850.txt:
21. @21031 `cela , avoir / peuplé un palais d'ouvrages magnifiques, et
    rallumé le feu sacré des arts, prêt à s'éteindre à Florence!` —
    context: "…les bénédictions de la patrie à recevoir, et, après tout
    **cela, avoir peuplé** un palais d'ouvrages magnifiques, et rallumé le
    feu sacré des arts, prêt à s'éteindre à Florence !" — "cela" is the
    object of the preposition "après" ("après tout cela" = "after all
    that"), not a dislocated topic; the infinitives "avoir peuplé"/"rallumé"
    are governed by "après". Excluded with cause (nearest near-miss #1).
22. @63055 `cela, mou cher seigneur, et puisse le ciel venir à / votre
    aide !` — "mou" = OCR "mon" (vocative "mon cher seigneur"); "venir"
    governed by finite "puisse". Excluded with cause.
23. @88090 `cela , je suis volé d'un millier / de ducats !` — finite "je
    suis"; "millier" is a noun in -er, false infinitive-shaped hit.
    Excluded with cause.
24. @293411 `cela, une occasion!` — noun, no verb.
25. @303933 `cela ; tra la la !` — interjection.
26. @587968 `cela , ô Dieu !` — vocative interjection.
27. @789464 `cela , et si / je vous le dis, dame!` — finite conditional
    clause.
28. @878534 `ça, je n'ai pas de bougies!` — finite clause.

scribe-bertrand-et-raton.txt:
29. @21271 `cela, risquer ma position, mon crédit !` — context: "…et
    j'irais **compromettre tout cela, risquer** ma position, mon crédit !…
    Pourquoi, je vous le demande ?" — "cela" is the direct object of
    "compromettre" ("compromettre tout cela" = "to compromise all this"),
    and "risquer ma position, mon crédit" are serial infinitives governed
    by "j'irais" ("I would go compromise all this, risk my position, my
    credit!"). "Cela" is NOT a fronted topic. Excluded with cause (nearest
    near-miss #2).

scribe-verre-d-eau.txt:
30. @61683 `cela, et pour bonnes raisons !` — no verb.
31. @91030 `cela, il faut le connaître !` — "connaître" governed by "il
    faut". Excluded with cause.
32. @99172 `cela, malheureux !` — adjective interjection, no verb.
33. @101916 `cela, il faut que vous nous laissiez !` — finite "il faut
    que".

vigny-chatterton-1835.txt:
34. @75863 `cela, sou- / viens-toi de Primerose-IIill !` — imperative
    ("souviens-toi"), hyphenation artifact; "IIill" is OCR noise (Primerose
    Hill). Excluded with cause.
35. @105683 `cela , je ne lui répon- / drais pas!` — finite conditional
    "répondrais". Excluded with cause.

Loose cross-check (35 hits with ±90 chars context): all are false friends
of the same taxonomy — demonstrative as grammatical subject or object of a
finite verb with the "!" belonging to a downstream clause ("cela me fait
de la peine", "cela va sans dire", "Cela serait drôle à penser ! penser
n'est rien", "pour lui cela veut dire : — joie !", "Cela viendra ;
l'avenir est à lui !"). None is a fronted-topic + bare-infinitive shape.

### Due-diligence checks

- Shape precedent re-derived in drama: Hernani uses bare exclamatory
  infinitives — "Gouverner tout cela ! — Monter, si l'on vous nomme !"
  (hugo-hernani-1870.txt) — but with the demonstrative as OBJECT after the
  infinitive, never as a fronted topic. The register has the infinitive
  construction; the dislocated-demonstrative topic shape is absent.
- Common confound class identified: the three nearest near-misses
  (#29 Scribe, #21 Musset, #13 Ruy Blas) all share one structure — "cela"
  governed by a PRECEDING preposition or verb ("compromettre tout cela",
  "après tout cela", "Pour cela"), followed by a comma and a
  bare-looking infinitive. The comma alone does not make a dislocation.
- Corpus counts: 2,969,582 chars / 190 dem-comma hits / 35 exclamatory
  candidates / 35 classified / 0 genuine. Strict pass: 1 hit ("che-valier"
  noun, excluded). No numbers invented; every count traces to the named
  files via the census script.

## Per-clause pass/fail

1. ≥1 genuine "cela/ceci/ça, [bare infinitive] !" attestation in
   19th-century French drama: **FAIL (confirmed zero).** 35/35 candidates
   classified across 2,969,582 characters of drama (~23 plays, Hugo /
   Dumas / Vigny / Musset / Scribe / Labiche); 0 genuine. The three
   nearest near-misses all dissolve on wider context with "cela" governed
   by a preceding preposition/verb, not a fronted topic.
2. Confirmed zero → arm (a) of ce87-1028-role fenced at the drama-register
   level: **EXECUTED.** Zero is an absence, not a refutation — the "Moi,
   voler !" precedent and Hernani's "Gouverner tout cela !" prove the
   exclamatory-infinitive shape is grammatical in 19th-century French and
   present in drama, so the demonstrative-headed version stays
   possible-but-unattested. Per §4 this is a **null**, not a kill.

## Adverses, answered

- None pre-registered ("Adverses: null").
- Self-check: does this null contradict the standing KILL
  (ce87-topic-licensing, bare "ce" cannot head an exclamatory infinitive)?
  No — this battery tested tonic demonstratives, a different construction;
  the kill stands untouched.
- Self-check: does this null contradict the battery-level NULL
  (disloc-demonstrative-inf) or the parent NULL (ce87-1028-role arm (a)
  fencing)? No — it is the chartered re-run of disloc-demonstrative-drama
  and retires its corpus-gap null with a real confirmed zero; arm (a)
  remains fenced at the drama-register level as the bar prescribes.
- Self-check: the original disloc-demonstrative-drama verdict was NULL
  (untestable); this report records the testable outcome without
  downgrading it — the original verdict's status is historical and
  untouched. §5.2: no standing or red-team verdict touched, no overwrite,
  no escalation required.

## Verdict: NULL (fence per clause 2 — confirmed zero in the drama register)

Zero genuine dislocated-demonstrative + bare-exclamatory-infinitive
attestations in 2,969,582 characters of 19th-century French drama
(35 candidates all classified: 3 preposition/verb-governed "cela"
near-misses, 4 OCR/noise, 28 grammatical false friends — imperatives,
finite clauses, governed infinitives, nouns, vocatives). The three closest
windows ("compromettre tout cela, risquer ma position, mon crédit !",
"après tout cela, avoir peuplé… et rallumé…!", "Pour cela, pour si peu,
s'aventurer ainsi !") all have "cela" as a governed object, not a fronted
topic. Arm (a) of ce87-1028-role stays fenced at the drama-register level.
Work regenerates via the follow-ups below.

## Follow-ups (nulls regenerate work)

1. **disloc-demonstrative-drama-clause-initial** (P2): rerun the drama
   census restricted to CLAUSE-INITIAL "cela/ceci/ça" (preceded by [. !? :],
   a speaker-label line end, or the start of a speech turn) to eliminate
   the preposition/verb-object confound class that produced all three
   near-misses ("compromettre tout cela", "après tout cela", "Pour cela").
   Bar: ≥1 genuine clause-initial attestation re-opens arm (a) at the
   drama-register level; confirmed zero hardens the fence against the
   confound class. (Does not duplicate disloc-demonstrative-drama-dialogue
   — different filter, same corpus.)
2. **disloc-demonstrative-drama-edition-delta** (P3): run the identical
   P1/P2/P3 census on the excluded second Hernani edition alone
   (`hugo-hernani.txt`, fr.wikisource Hetzel 1889, ~173,559 chars).
   Bar: ≥1 genuine attestation means the one-edition-per-play exclusion was
   material — re-open the register census on that edition; confirmed zero
   means the exclusion is safe and can be recorded and closed. (Does not
   duplicate: the reissue never tested the excluded file.)
3. **disloc-demonstrative-drama-dialogue** (already queued, P3): noted as
   the running continuation — dialogue-scoped rerun on the full ingested
   drama corpus. No duplicate needed from this report.

Note for the supervisor: `disloc-demonstrative-drama-reinforced` is already
queued (reinforced-head inventory on the drama corpus); none of the three
follow-ups above duplicates it. `ce01-slot-1029-infinitive-avenue` is
already queued (the post-fence replacement-role commission); not re-proposed.

## Bookkeeping

- Census script: code/crowd17/next-token/disloc_demonstrative_drama_reissue_census.py
  (re-runnable; outputs disloc-demonstrative-drama-reissue_census.json with
  per-file sizes, hit counts, and all candidate windows).
- Report: code/crowd17/report_inbox/battery-disloc-demonstrative-drama-reissue.md
  (this file).
- battery-queue.json: `disloc-demonstrative-drama-reissue` queued ->
  verdict/null via temp-file + rename (pre-write assert confirmed
  queued/verdictless; JSON re-validated post-write; own entry only;
  claim/bars/evidence/adverses preserved).
- Lock created on start (agent id 21d4ff9b-0ab0-441b-a580-b8449fe1e5e7 +
  2026-10-09T08:41:00Z); no stale lock existed. Deleted on completion
  (verified gone).
- R5005, sealed gates, red-team queue untouched. Every number traces to
  the named corpus files or the census script; no invented data.
