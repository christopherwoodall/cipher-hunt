# Battery report: disloc-demonstrative-drama-dialogue

- Target id: `disloc-demonstrative-drama-dialogue`
- Claim: "run the same dialogue-scoped demonstrative census on the
  ingested drama corpus"
- Date: 2026-10-09
- Worker: battery worker (subagent ece3c259-03b0-41b5-a8f1-0a5f3d69d83c)
- Stream: not applicable — corpus census against period French drama, per
  target charter and the disloc-demonstrative-inf precedent. The 1,847-pair
  repaired parse was not used. R5005, sealed gate instances, and the
  red-team adjudication queue were not touched.

Terms (ASD-STE100): "dislocation" = a topic moved to the front of the
clause, set off by a pause, and resumed by a pronoun. "Tonic" = the
stressed form of a pronoun (cela, ça). "Bare exclamatory infinitive" =
an infinitive used as an exclamation with no preposition (de, pour), no
"que", no resumptive clitic. "Dialogue" = the spoken speech of the plays
(speaker-header format), not prefaces, title pages, cast lists, or stage
directions.

## Parentage

Fires follow-up #2 of the battery-level NULL
`disloc-demonstrative-quoted-drama` (2026-10-09): run the same
demonstrative census on the ingested drama corpus dialogue, now that the
drama corpus has landed. Does not duplicate
`disloc-demonstrative-drama-reissue` (full-text, other Hernani edition) —
dialogue-scoped, and run on the Hetzel 1889 Hernani edition
(`hugo-hernani.txt`), with `hugo-hernani-1870.txt` excluded per the
one-edition-per-play rule.

## Bar (verbatim, pre-registered before testing)

"same bars as disloc-demonstrative-quoted-drama, run on the ingested
drama corpus dialogue"

Numbered pass/fail clauses (restated before testing, not modified after;
inherited from disloc-demonstrative-quoted-drama):

1. At least one GENUINE "cela/ceci/ça, [bare infinitive] !" attestation
   exists in the dialogue of the ingested drama corpus plays. If yes:
   arm (a) of ce87-1028-role is promoted (drama-specific).
2. If clause 1's census is a confirmed zero — every candidate window
   classified, false friends excluded with cause — arm (a) is fenced at
   the drama-dialogue level (null per §4: inconclusive as a kill, since
   zero is an absence).

## Method

1. Read BATTERY-PROTOCOL.md first. Created the lock
   `code/crowd17/next-token/locks/disloc-demonstrative-drama-dialogue.lock`
   on start (no prior lock, stale or fresh, existed for this id); deleted
   on completion.
2. Corpus, named with sizes (character counts, computed in-session) — 14
   files, 2,939,372 characters, ~23 distinct plays (Dumas, Hugo, Vigny,
   Musset, Scribe, Labiche):
   dumas-antony.txt (102,234); dumas-henri-iii.txt (128,462);
   dumas-kean.txt (152,233); dumas-mariage-louis-xv-1841.txt (204,641);
   dumas-tour-de-nesle.txt (132,586); hugo-burgraves.txt (151,408);
   hugo-hernani.txt (173,559, Hetzel 1889 wikisource ed. — the ONE Hernani
   edition used, `hugo-hernani-1870.txt` excluded with cause per the
   one-edition rule); hugo-ruy-blas.txt (198,265);
   labiche-chapeau-de-paille.txt (118,567);
   labiche-martin-poudre-aux-yeux.txt (87,042);
   musset-comedies-proverbes-1850.txt (972,696);
   scribe-bertrand-et-raton.txt (182,448); scribe-verre-d-eau.txt
   (146,451); vigny-chatterton-1835.txt (188,780).
3. Extraction caveat: the quoted-drama battery's D1–D3 rule (guillemets,
   straight quotes, em-dash paragraphs) catches almost no play dialogue —
   plays mark speech with ALL-CAPS speaker headers, not quotes (a verbatim
   D1–D3 run found only 14 candidates, ~1.3M of 2.9M chars covered). So
   the honest dialogue-scoped census ran the same verbatim P1–P3 DEM/INF
   patterns over the full play text and classified EVERY candidate by
   hand with dialogue-vs-non-dialogue status. A confirmed zero over the
   full play text implies a confirmed zero in dialogue; no genuine hit can
   hide in a preface or stage direction.
4. Reproducible census script:
   `code/crowd17/next-token/disloc_demonstrative_drama_dialogue_census.py`.
   Raw results in
   `code/crowd17/next-token/disloc-demonstrative-drama-dialogue_census.json`
   (per-file sizes, dem-comma hits, 35 pass-A candidates with @offsets and
   ±120-char context, 68 control hits). Patterns verbatim from
   `disloc_demonstrative_census.py` (P1–P3). Controls: C1 cedilla-less
   "ca," + "!" + infinitive-shaped word (0 hits); C2 loose pass
   (any cela|ceci|ça|ca with infinitive-shaped word ≤40 chars after and
   "!" ≤70 chars after — catches comma-less shapes; 68 hits, all
   classified).

## Window-level evidence

All 35 pass-A candidates classified (dialogue location noted; "/" marks
line breaks; @ = char offset of the demonstrative in the file):

1. dumas-antony.txt @13240 `cela, va !` — "va" is the imperative of aller,
   not an infinitive. Excluded. In dialogue (Adèle).
2. dumas-antony.txt @69365 `cela, et ce serait dommage ; vous, bâtie de
   fleurs et de gaze, vous voulez aimer et être aimée d'amour ; ah !` —
   finite "vous voulez"; "aimer"/"être aimée" governed by modal "vouloir".
   Excluded. In dialogue.
3. dumas-kean.txt @35666 `ça, moi !` — pronoun interjection, no verb.
4. dumas-kean.txt @65809 `ça, lui ; mais nous autres !` — pronoun, no verb.
5. dumas-kean.txt @119377 `cela, sous prétexte qu'il est noble, qu'il est
   lord, qu'il est pair… Ah !` — "pair" is a noun (a peer); no infinitive.
6. dumas-mariage-louis-xv-1841.txt @44415 `cela, moi !` — interjection.
7. dumas-mariage-louis-xv-1841.txt @101348 `cela, che- / valier !` — "che-
   valier" dissolves to "chevalier" (OCR line-break hyphenation), a noun.
8. dumas-mariage-louis-xv-1841.txt @122127 `cela, mon oncle, je peux vous
   en répon- / dre, parole d'honneur!` — finite "je peux"; "répondre"
   governed by "pouvoir". Excluded. In dialogue (Marton).
9. dumas-tour-de-nesle.txt @129575 `cela, qui m'a mis au cœur cet amour
   bizarre, tout de mère et pas d'amante !` — relative clause with finite
   "a mis"; "mère"/"bizarre" false infinitive-shaped hits. Excluded.
10. hugo-burgraves.txt @80459 `ceci : / / Si tout est en repos au fond de
    vos pensées, / / ... Vivez, riez, chantez!` — colon introduces a
    conditional with finite imperatives ("vivez, riez, chantez" are
    imperative 2pl, not infinitives). Excluded.
11. hugo-burgraves.txt @145006 `cela, par grâce !` — no verb at all.
12. hugo-hernani.txt @167356 `cela, c'est assez !` — finite "c'est".
    (The Hetzel-edition Hernani candidate; the reissue's 1870-edition
    candidate was also finite.)
13. hugo-ruy-blas.txt @74859 `cela, pour si peu, s'aventurer ainsi !` —
    context: "Pour m'apporter les fleurs qu'on me refuse ici, / Pour cela,
    pour si peu, s'aventurer ainsi !" — "cela" is the object of the
    preposition "pour", not a fronted topic. Excluded (near-miss).
14. labiche-chapeau-de-paille.txt @11270 `ça : « Bah !` — quotation
    introduction, interjection.
15. labiche-chapeau-de-paille.txt @34682 `ça : « Mon Dieu !` — same.
16. labiche-martin-poudre-aux-yeux.txt @19881 `ça, ils sont très gentils !`
    — finite clause.
17. @48985 `ça, je me tais !` — finite clause.
18. @62669 `Ça, je l'ai vu ; sept à huit pieds !` — finite clause.
19. @72673 `ça, quand le faux à l'air vrai… ce n'est plus du faux !` —
    finite clause.
20. @75702 `ça, c'est du sentiment… ça nous éloigne !` — finite "c'est".
21. musset-comedies-proverbes-1850.txt @21031 `cela, avoir / peuplé un
    palais d'ouvrages magnifiques, et rallumé le feu / sacré des arts,
    prêt à s'éteindre à Florence!` — context: "…les bénédictions de la
    patrie à recevoir, et, après tout **cela, avoir peuplé** un palais…"
    — "cela" is the object of the preposition "après", not a dislocated
    topic; infinitives governed by "après". Excluded (near-miss). In
    dialogue (André).
22. musset @63055 `cela, mou cher seigneur, et puisse le ciel venir à /
    votre aide !` — "mou" = OCR "mon" (vocative); "venir" governed by
    finite "puisse". Excluded.
23. musset @88090 `cela, je suis volé d'un millier / de ducats !` —
    finite "je suis"; "millier" is a noun in -er. Excluded.
24. musset @293411 `cela, une occasion!` — noun, no verb.
25. musset @303933 `cela ; tra la la !` — interjection.
26. musset @587968 `cela , ô Dieu !` — vocative interjection.
27. musset @789464 `cela , et si / je vous le dis, dame!` — finite
    conditional clause.
28. musset @878534 `ça, je n'ai pas de bougies!` — finite clause.
29. scribe-bertrand-et-raton.txt @21271 `cela, risquer ma position, mon
    crédit !` — context: "…et j'irais **compromettre tout cela, risquer**
    ma position, mon crédit !…" — "cela" is the direct object of
    "compromettre", and the infinitives are serial infinitives governed by
    "j'irais". "Cela" is NOT a fronted topic. Excluded (near-miss). In
    dialogue (Bertrand).
30. scribe-verre-d-eau.txt @61683 `cela, et pour bonnes raisons !` —
    no verb.
31. scribe-verre-d-eau.txt @91030 `cela, il faut le connaître !` —
    "connaître" governed by "il faut". Excluded.
32. scribe-verre-d-eau.txt @99172 `cela, malheureux !` — adjective
    interjection, no verb.
33. scribe-verre-d-eau.txt @101916 `cela, il faut que vous nous
    laissiez !` — finite "il faut que".
34. vigny-chatterton-1835.txt @75863 `cela, sou- / viens-toi de
    Primerose-IIill !` — imperative ("souviens-toi"); hyphenation
    artifact; "IIill" is OCR noise. Excluded.
35. vigny-chatterton-1835.txt @105683 `cela , je ne lui répon- / drais
    pas!` — finite conditional "répondrais". Excluded.

**0 of 35 genuine.** The three nearest near-misses (#13 Ruy Blas, #21
Musset, #29 Scribe) all share one structure: "cela" governed by a
PRECEDING preposition or verb ("Pour cela", "après tout cela",
"compromettre tout cela") — the comma alone does not make a dislocation.

Control results (all classified with ±120-char context, no genuine):
- C1 (cedilla-less "ca," + "!" + infinitive-shaped word): **0 hits** in
  2,939,372 chars.
- C2 (loose, comma-less shapes): 68 hits; all non-genuine of the same
  false-friend taxonomy — "cela" as grammatical subject/object of a
  finite verb with "!" belonging to a downstream clause ("cela va sans
  dire", "Cela serait drôle à penser !", "ça va finir !", "Ça, je l'ai vu"),
  pour/preposition-governed infinitives ("Et tout cela pour être
  fournisseur breveté !", "Mais pour tout cela une demi-heure !"), and
  finite "vous lui avez dit tout cela à son couvent !". Notable: zero
  "cela, [bare infinitive] !" shapes hiding outside the comma rule.

## Per-clause pass/fail

1. ≥1 genuine "cela/ceci/ça, [bare infinitive] !" attestation in drama
   dialogue: **FAIL (confirmed zero).** 35/35 pass-A candidates classified
   across 2,939,372 characters of drama dialogue (~23 plays, one Hernani
   edition); C1 and C2 controls find nothing the comma rule missed. 0
   genuine.
2. Confirmed zero → arm (a) fenced at drama-dialogue level: **EXECUTED.**
   Zero is an absence, not a refutation — the "Moi, voler !" precedent and
   Hernani's "Gouverner tout cela !" (bare exclamatory infinitive with the
   demonstrative as OBJECT after the infinitive, re-derived in drama by
   the reissue battery) prove the exclamatory-infinitive shape is
   grammatical and present in drama. Only the demonstrative-headed topic
   version stays possible-but-unattested. Per §4 this is a **null**, not a
   kill.

## Adverses, answered

- None pre-registered ("Adverses: none listed").
- Self-check: no contradiction with the standing KILL
  (ce87-topic-licensing, bare "ce" cannot head the construction) — this
  battery tested tonic demonstratives only.
- Self-check: no contradiction with the standing battery NULL
  (disloc-demonstrative-drama-reissue) — independent census on the
  second Hernani edition, same outcome; the fence now holds at
  full-corpus (RDM), quoted-dialogue (RDM), drama full-text, AND
  drama-dialogue levels.
- §5.2: no standing red-team verdict touched; no overwrite, no
  downgrade. This verdict does not contradict one.

## Verdict: NULL (fence per clause 2)

Zero genuine dislocated-demonstrative + bare-exclamatory-infinitive
attestations in 2,939,372 characters of 19th-century French drama dialogue
(~23 plays; Hugo, Dumas, Vigny, Musset, Scribe, Labiche; one Hernani
edition). Arm (a) of ce87-1028-role stays fenced — now at drama-dialogue
level as well. Work regenerates via the follow-ups below.

## Follow-ups (nulls regenerate work)

Checked against battery-queue.json; none duplicates a queued or verdict
target:

1. **disloc-demonstrative-inversion-drama** (P3): the inversion batteries
   (disloc-demonstrative-inversion, -inversion-verbtags,
   -inversion-fullcorpus) covered RDM dialogue and the full corpus, but
   never the drama plays. Census postposed demonstratives ("[bare inf] !,
   cela/ceci/ça", e.g. "Voler, cela !") in the drama-corpus dialogue. Bar:
   ≥1 genuine postposed-demonstrative + bare exclamatory infinitive
   attestation in drama dialogue re-opens arm (a) in inverted form;
   confirmed zero fences it there too.
2. **bare-excl-inf-head-inventory-drama** (P3): positive-space complement
   of this fence — inventory what CAN head a bare exclamatory infinitive
   in drama dialogue (e.g. Hernani's "Gouverner tout cela !" has the
   demonstrative as object; the RDM precedent has a tonic pronoun
   head). disloc-topic-inventory-excl-inf covered the 27.66M-char corpus
   and gov-excl-inf-register-drama covered governed infinitives; a
   drama-dialogue head inventory is still open. Bar: census of bare
   exclamatory infinitives in drama dialogue lands with a head-type
   table (topic-demonstrative vs other); ≥1 demonstrative-headed hit
   re-opens arm (a).
3. **arm-a-fence-ratify** (escalate to red team): arm (a) of ce87-1028-role
   is now fenced at four independent levels — RDM full corpus, RDM
   quoted dialogue, drama full text (both Hernani editions), drama
   dialogue — each a confirmed zero with every candidate classified.
   Package the four fencing reports for red-team ratification of the
   arm-(a) fence as standing.

## Bookkeeping

- Census script:
  code/crowd17/next-token/disloc_demonstrative_drama_dialogue_census.py
  (re-runnable; outputs
  disloc-demonstrative-drama-dialogue_census.json with per-file sizes,
  dem-comma hits, all 35 candidates with @offsets and ±120-char context,
  and all 68 control hits).
- Report: code/crowd17/report_inbox/battery-disloc-demonstrative-drama-dialogue.md
  (this file).
- battery-queue.json: `disloc-demonstrative-drama-dialogue` queued ->
  verdict/null via temp-file + rename (pre-write assert confirmed
  queued/verdictless; JSON re-validated post-write; own entry only;
  claim/bars/evidence/adverses preserved).
- Lock created on start (agent id + UTC timestamp), deleted on
  completion.
- R5005, sealed gates, red-team queue untouched. Every number traces to
  the named corpus files or the census script; no invented data.
