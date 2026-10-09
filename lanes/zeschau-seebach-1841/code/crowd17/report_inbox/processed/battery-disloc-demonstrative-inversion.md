# Battery report: disloc-demonstrative-inversion

- Target id: `disloc-demonstrative-inversion`
- Claim: "census postposed demonstratives ('[inf] !, cela/ceci/ca') in RDM
  quoted dialogue"
- Date: 2026-10-09
- Worker: battery worker (subagent ae792c97-f68e-4160-948e-b20b12f16642)
- Stream: not applicable — corpus census against period French, per target
  charter and the disloc-demonstrative-inf / quoted-drama precedents. The
  1,847-pair repaired parse was not used. R5005, sealed gate instances,
  and the red-team adjudication queue were not touched.

Terms (ASD-STE100): "dislocation" = a topic moved out of its normal
position, set off by a pause, and resumed by a pronoun. "Tonic" = the
stressed form of a pronoun (cela, ceci, ça). "Postposed" = the
demonstrative comes AFTER the infinitive ("[inf] !, cela"), the inverse
of the preposed order fenced by the parent batteries. "Quoted-dialogue
windows" = text inside guillemet quotes («...»), straight double quotes
("..."), or em-dash dialogue paragraphs (— ...).

## Parentage

Follow-up of the battery-level NULL
`disloc-demonstrative-quoted-drama` (2026-10-09): the preposed order
("cela/ceci/ça, [bare inf] !") fenced at quoted-drama level (3,590
dialogue spans, 169 dem-comma hits, 3 candidates all classified
non-genuine). This battery tests whether the fence is a word-order
artefact: if the tonic head licenses the pairing from post-topic
position, the bar construction never shows up in the tested order.

## Bar (verbatim, pre-registered before testing)

">=1 genuine attestation re-opens the pairing as a word-order variant;
confirmed zero fences it beyond the preposed order"

Numbered pass/fail clauses (restated before testing, not modified after):

1. At least one GENUINE postposed "[inf] !, cela/ceci/ça" attestation
   (bare exclamatory infinitive, demonstrative in post-topic position,
   paired) exists inside a quoted-dialogue window of the
   revue-deux-mondes-1841 corpus. If yes: arm (a) of ce87-1028-role
   re-opens as a word-order variant (promote-grade per §4).
2. If clause 1's census is a confirmed zero — every candidate window
   classified, false friends excluded with cause — the pairing is fenced
   beyond the preposed order (null per §4: inconclusive as a kill,
   since zero is an absence).

## Method

1. Read BATTERY-PROTOCOL.md first. Created the lock
   `code/crowd17/next-token/locks/disloc-demonstrative-inversion.lock`
   on start (agent id + UTC timestamp; no stale lock for this id
   existed); deleted on completion.
2. Ran a reproducible census script:
   `code/crowd17/next-token/disloc_demonstrative_inversion_census.py`.
   Raw results in
   `code/crowd17/next-token/disloc-demonstrative-inversion_census.json`.
   It reuses the verbatim dialogue-span extraction (D1 guillemet,
   D2 straight double quote, D3 em-dash paragraphs) and the verbatim
   INF suffix pattern from
   `disloc_demonstrative_quoted_drama_census.py`, with the search
   inverted: for each infinitive-shaped word in a dialogue span, a
   window from the INF start through INF end + 100 chars is a candidate
   iff a tonic demonstrative
   `\b(cela|ceci|ça|ca|cel[àa]|cec[iy])\b` starts AFTER the infinitive
   and "!" occurs between the INF start and 20 chars past the
   demonstrative. This covers all postposed shapes: "Voler !, cela",
   "Voler, cela !", "Voler ! cela", "Voler cela !". Candidates deduped
   by (file, absolute INF offset); each candidate carries its corpus
   char offset.
3. Corpus, named with sizes (character counts, computed in-session;
   dialogue spans identical to the parent battery's run):
   - revue-deux-mondes-1841-q1.txt: 3,013,552 chars → 713 dialogue
     spans, 2,245,389 dialogue chars, 3 postposed-dem candidates.
   - revue-deux-mondes-1841-q2.txt: 2,964,405 chars → 730 dialogue
     spans, 2,375,587 dialogue chars, 10 postposed-dem candidates.
   - revue-deux-mondes-1841-q3.txt: 3,054,350 chars → 530 dialogue
     spans, 2,584,536 dialogue chars, 7 postposed-dem candidates.
   - revue-deux-mondes-1841-q4.txt: 3,165,234 chars → 1,617 dialogue
     spans, 3,110,318 dialogue chars, 17 postposed-dem candidates.
   - Totals: 12,197,541 corpus chars; 3,590 dialogue spans;
     ~10,315,830 dialogue chars; **37 unique postposed-dem candidates**.
4. Due-diligence controls run in-session:
   - Cedilla-less control: `\bca\b` was in the DEM pattern; its one
     hit (q4 @69300, "ca-" at a line break) is an OCR hyphenation
     fragment, not a demonstrative — excluded with cause, so the
     cedilla-less route contributes zero.
   - Monster-span caveat (unmatched quotes, per the parent battery):
     same extraction, same coverage; cannot hide a genuine hit.
   - The known preposed precedent "Moi, voler !" is correctly NOT hit
     by this census (demonstrative order is reversed) — the inversion
     filter discriminates by construction.

## Window-level evidence

All 37 unique candidates shown verbatim ("/" = source line break;
@-offset = corpus char offset of the infinitive-shaped word; file
abbrev q1..q4 = revue-deux-mondes-1841-qN.txt). Classified into three
groups; every candidate excluded with cause.

### Group A — false-INF: no infinitive at all (21 candidates)

Suffix-pattern noise (nouns, adjectives, possessives, finite verbs):

1. q1 @30461 (guillemet) `noyer. Elle s'écria incontinent : Ha! mon Dieu!
   quel augure de voyage est ceci?` — "noyer" is the walnut tree (noun);
   "ceci" is the subject of "est". Excluded.
2. q1 @64114 (guillemet) `Votre mari atout fait! — Ah ! cela est ainsi ,
   répondit-elle , adieu donc larmes !` — "votre" possessive; "cela est
   ainsi" = cela subject of finite verb. Excluded.
3. q2 @2264351 (guillemet) `aumônier, on l'a fait disparaître ! et sur
   cela entre dans une telle fureur` — "aumônier" noun; "sur cela" =
   prepositional. Excluded.
4. q2 @1534042 (dquote) `mesure sur les convenances dramatiques! Rubini,
   lui, ne fait rien de tout cela` — "mesure" noun; "cela" inside "de
   tout cela" (object). Excluded.
5. q2 @1537960 (dquote) `maître! comme cela soupire la douleur et la
   plainte!` — "maître" vocative noun; "cela soupire" = cela subject of
   finite verb. Excluded.
6. q2 @1975155 (dquote) `arrière de l'Allemagne! et tout cela parce que
   l'Alsace a le malheur d'être réunie à la Fra` — "arrière" noun/adverb;
   "tout cela" subject of the parce-que clause. Excluded.
7. q2 @2350959 (dquote) `Maître, un réal pour du tabac! — Mademoiselle,
   deux réaux pour du vin ! ) En disant cela,` — "maître" vocative noun;
   "disant cela" = cela object of gerund. Excluded.
8. q2 @895149 (em-dash) `père! murmurait-il suffoqué; je ne ie serai pas
   long-temps si cela est.` — "père" noun; "cela est" = cela subject of
   finite verb. Excluded.
9. q3 @2812736 (guillemet) `dernier goujat devrait l'arracher de la
   poitrine! Ceci, dit au fort de la colère et peut-êt` — "dernier"
   adjective. Excluded.
10. q3 @1766127 (dquote) `singulier livre. Terrible voyage, je vous jure !
    Et cela se prolonge ainsi près de deux cents` — "singulier" adjective;
    "cela se prolonge" = cela subject of finite verb. Excluded.
11. q3 @1766138 (dquote) `livre. Terrible voyage, je vous jure ! Et cela
    se prolonge ainsi près de deux cents pages` — "livre" noun; same
    "cela se prolonge" clause. Excluded.
12. q3 @1766175 (dquote) `jure ! Et cela se prolonge ainsi près de deux
    cents pages, à travers la maladie, le dés` — "jure" finite verb
    (1sg of jurer), not an infinitive. Excluded.
13. q3 @2838234 (dquote) `guerre? — Ou bien il interrompait tout net : —
    Comment! qu'est-ce? mais cela est impossible` — "guerre" noun; "cela
    est impossible" = cela subject. Excluded.
14. q4 @56927 (guillemet) `PARATONNERRE. 25 — Ah ! vous avez découvert
    cela!` — "paratonnerre" noun; "découvert cela" = cela object of
    participle. Excluded.
15. q4 @748489 (guillemet) `vicaire de moins, w — Eh bien! que dites-vous
    de cela? s'écria M. Riquemont.` — "vicaire" noun; "de cela" =
    prepositional. Excluded.
16. q4 @921920 (guillemet) `désastre à déplorer ! — Ah ça ! monsieur, où
    voulez-vous en venir?` — "désastre" noun. Excluded (the "ça" is the
    "Ah ça !" interjection — see group B #6).
17. q4 @2652552 (guillemet) `sourire moqueur : Ce n'est pas plus difficile
    que cela!` — "sourire" noun; "que cela" = comparative-governed.
    Excluded.
18. q4 @235572 (dquote) `premier coup : Cest cela!` — "premier" adjective;
    "Cest cela" = "C'est cela", cela predicate. Excluded.
19. q4 @760488 (dquote) `heure ! c'est beau , c'est vaillant, c'est bien
    attaché, ça fait honneur à son cavalier.` — "heure" noun; "ça fait
    honneur" = ça subject of finite verb. Excluded.
20. q4 @1268210 (em-dash) `votre aise! Vivez, mourez, cela vous regarde;`
    — "votre" possessive. Excluded (the "cela" belongs to group B #8).
21. q4 @1750415 (em-dash) `sombre découragement, ça ne mord pas! C'est
    tous les jours la même chose.` — "sombre" adjective; "ça ne mord
    pas" = ça subject of finite verb. Excluded.

### Group B — genuine infinitive, demonstrative not paired (15 candidates)

An infinitive-shaped word that is a real infinitive is present, but in
every case the demonstrative is the subject/object of a finite verb, a
preposition/comparative complement, an interjection, or sits in a
different clause — never the postposed dislocation paired with the
bare exclamatory infinitive:

1. q1 @2560691 (dquote) `être quecela ne mange pas! — Cela \it-il sur
   terre ou sur mer?` — "cela ne mange pas" = cela subject of "mange".
   Excluded.
2. q2 @1399795 (guillemet) `faire un neuf, moi je te couperai la tête
   pour faire de toi un zéro. Ah! ceci n'est pas` — "ceci n'est pas" =
   ceci subject of finite "est". Excluded.
3. q2 @1399852 (guillemet) `faire de toi un zéro. Ah! ceci n'est pas trop
   mal , j'espère.` — same "Ah! ceci n'est pas..." clause as #2; "faire"
   is governed by "pour"/the threat clause. Excluded.
4. q2 @2264377 (guillemet) `disparaître ! et sur cela entre dans une
   telle fureur` — "disparaître" is a genuine exclamatory infinitive,
   but "cela" is governed by the preposition "sur", not a dislocated
   topic. Excluded with cause.
5. q2 @901694 (dquote) `traiter de fourbe ! Il mitl'épée au vent en disant
   cela.` — "cela" is the object of the gerund "disant" in a separate
   narrative clause. Excluded.
6. q3 @2812762 (guillemet) `l'arracher de la poitrine! Ceci, dit au fort
   de la colère et peut-être sans intention , tomba` — "l'arracher" is
   governed by finite "devrait"; "Ceci" heads its own clause as the
   fronted (preposed) topic of "dit... tomba", not postposed to the
   infinitive. Excluded — this is the preposed order, already fenced.
7. q3 @2943820 (dquote) `sortir. — Ah! c'est toi, Paulet, s'écria-t-il,
   cela est heureux...` — "cela est heureux" = cela subject of finite
   "est"; the "!" is inside "Ah!", far from the demonstrative. Excluded.
8. q4 @921933 (guillemet) `déplorer ! — Ah ça ! monsieur, où voulez-vous
   en venir?` — "déployer"/"déplorer" is "à"-governed ("à déplorer"),
   not a bare exclamatory infinitive; "Ah ça !" is the fixed interjection
   "ah ça", not a dislocated topic. Excluded.
9. q4 @2652536 (guillemet) `dire avec un sourire moqueur : Ce n'est pas
   plus difficile que cela!` — "dire" heads stage-direction-style
   narrative; "cela" is governed by the comparative "que". Excluded.
10. q4 @2818210 (dquote) `avoir voulu étendre la portée, quelle leçon pour
    M. Guizot! mais que cela est triste pour` — "avoir"/"étendre" belong
    to the finite-clause "avoir voulu" chain; "cela" is the subject of
    finite "que cela est triste". Excluded.
11. q4 @2818224 (dquote) `étendre la portée, quelle leçon pour M. Guizot!
    mais que cela est triste pour la France!` — same "que cela est
    triste" clause as #10. Excluded.
12. q4 @836471 (em-dash) `vivre ni mourir. Ruses que tout cela! mensonges
    imaginés pour auto- riser vos visites !` — "vivre"/"mourir" are two
    sentences back; "cela" sits inside the relative "que tout cela"
    (subject of the verbless exclamation "Ruses"). Excluded.
13. q4 @836482 (em-dash) `mourir. Ruses que tout cela! mensonges imaginés
    pour auto- riser vos visites !` — same relative clause as #12.
    Excluded.
14. q4 @1268136 (em-dash) `s'établir à Riquemont tout exprès pour soigner
    vos gastrites? A votre aise! Vivez, mourez, cela` — "cela" opens
    "cela vous regarde" as the subject of finite "regarde"; the
    infinitives "s'établir"/"soigner" belong to the preceding question.
    Excluded.
15. q4 @1268181 (em-dash) `soigner vos gastrites? A votre aise! Vivez,
    mourez, cela vous regarde; pour moi, je ne m'en` — same "cela vous
    regarde" finite clause as #14. Excluded.

### Group C — OCR artefact (1 candidate)

1. q4 @69300 (guillemet) `Contre-temps fâcheux! la première figure que
   j'aperçus en entrant fut celle du détestable ca-` — "ca-" is a
   line-break hyphenation fragment of a longer word ("contre" is
   word-internal to "contre-temps"), not a demonstrative. Excluded.

**0 of 37 genuine.** The three nearest misses all fence themselves:
"disparaître ! et sur cela" (#B4, preposition-governed), "Ah ça !"
(#B8, fixed interjection with "à"-governed infinitive), "Ceci, dit..."
(#B6, preposed topic — the already-fenced order).

## Per-clause pass/fail

1. ≥1 genuine postposed "[inf] !, cela/ceci/ça" attestation in
   quoted-dialogue windows of RDM 1841: **FAIL (confirmed zero).**
   37 unique candidates in ~10.3M dialogue chars → 21 noun/adjective/
   possessive false-INF, 15 genuine infinitive with demonstrative in a
   finite/prepositional/interjectional slot, 1 OCR hyphenation
   fragment; 0 genuine.
2. Confirmed zero → the pairing fenced beyond the preposed order:
   **EXECUTED.** Zero is an absence, not a refutation. The fence now
   covers both word orders at quoted-drama level in RDM 1841. Per §4
   this is a **null**, not a kill.

## Adverses, answered

- None pre-registered ("Adverses: none listed").
- Self-check: no contradiction with the standing KILL
  (ce87-topic-licensing, bare "ce" cannot head the construction) — this
  battery tested tonic demonstratives only.
- Self-check: no contradiction with the parent NULL
  (disloc-demonstrative-quoted-drama) — the bar anticipated exactly
  this outcome ("confirmed zero fences it beyond the preposed order").
- §5.2: no standing red-team verdict touched; no overwrite, no
  escalation required.

## Verdict: NULL (fence per clause 2)

Zero genuine postposed demonstrative + bare-exclamatory-infinitive
attestations in ~10.3M characters of quoted dialogue inside
revue-deux-mondes-1841 (37 unique candidates, all classified: 21
false-INF, 15 demonstrative-in-wrong-slot, 1 OCR fragment; none pairs
the demonstrative with the infinitive as a postposed dislocation).
Arm (a) of ce87-1028-role stays fenced — now in both word orders at
quoted-drama level. Work regenerates via the follow-ups below.

## Follow-ups (nulls regenerate work)

None of these duplicates a queued target (checked against
battery-queue.json: no inversion targets queued; the disloc-demonstrative
family targets cover preposed-order re-runs only):

1. **disloc-demonstrative-inversion-verbtags** (P3): re-run this
   census with a POS-tagged genuine-infinitive filter. 21 of 37
   candidates here were noun/adjective/possessive false-INF noise from
   the suffix-only INF pattern; a verb-tagged pass would discriminate
   cleanly. Bar: ≥1 genuine postposed pairing on the cleaned candidate
   set re-opens arm (a) as a word-order variant; confirmed zero fences
   it at verb-filtered level.
2. **disloc-demonstrative-inversion-fullcorpus** (P3): run the same
   inversion census on full-corpus windows (not dialogue-scoped).
   Dialogue in RDM 1841 is sparse exclamatory-infinitive territory
   ("Moi, voler !" is itself narrative speech-tagged); if the pairing
   is a narrative-register feature, dialogue-scoping hides it. Bar:
   ≥1 genuine attestation promotes arm (a) as a register-general
   word-order variant; confirmed zero fences the family corpus-wide at
   RDM 1841.
3. **joint-order-demonstrative-pairing-census** (P4): supersede the
   order-framed batteries with one joint census of bare-exclamatory-
   infinitive + tonic demonstrative adjacency in EITHER order across
   the RDM 1841 corpus (full text). Bar: ≥1 genuine pairing in either
   order re-opens arm (a); confirmed zero closes the family at RDM
   1841 level.

## Bookkeeping

- Census script:
  code/crowd17/next-token/disloc_demonstrative_inversion_census.py
  (re-runnable; outputs
  disloc-demonstrative-inversion_census.json with per-file sizes,
  dialogue-span counts, 37 unique candidates, each with file,
  absolute INF char offset, span kind, and window text).
- Report: code/crowd17/report_inbox/battery-disloc-demonstrative-inversion.md
  (this file).
- battery-queue.json: `disloc-demonstrative-inversion` queued ->
  verdict/null via temp-file + rename (pre-write assert confirmed
  queued/verdictless; JSON re-validated post-write; own entry only;
  claim/bars/evidence/adverses preserved).
- Lock created on start (agent id + UTC timestamp; no stale lock for
  this id existed), deleted on completion.
- R5005, sealed gates, red-team queue untouched. Every number traces to
  the named corpus files or the census script; no invented data.
