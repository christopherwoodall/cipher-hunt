# Battery report: disloc-demonstrative-inversion-verbtags

- Target id: `disloc-demonstrative-inversion-verbtags`
- Claim: "POS-tagged genuine-infinitive re-census of the
  postposed-demonstrative search"
- Date: 2026-10-09
- Worker: battery worker (subagent a6c76bd9-3045-49e4-90b4-e4adbe933cbc)
- Stream: not applicable — corpus census against period French, per
  target charter and the disloc-demonstrative-inversion precedent. The
  1,847-pair repaired parse was not used. R5005, sealed gate instances,
  and the red-team adjudication queue were not touched.

Terms (ASD-STE100): "dislocation" = a topic moved out of its normal
position, set off by a pause, and resumed by a pronoun. "Tonic" = the
stressed form of a pronoun (cela, ceci, ça). "Postposed" = the
demonstrative comes AFTER the infinitive ("[inf] !, cela"), the inverse
of the preposed order. "POS" = part-of-speech tag (verb, noun,
adjective...). "VerbForm=Inf" = the tagger marks the word as a true
infinitive form. "False-INF" = a word that matches the infinitive
suffix pattern but is not an infinitive (noun, adjective, finite verb).

## Parentage

Follow-up of the battery-level NULL
`disloc-demonstrative-inversion` (2026-10-09): 37 unique postposed-dem
candidates in quoted dialogue of revue-deux-mondes-1841 (q1..q4);
21 were false-INF noise (nouns, adjectives, possessives, finite verbs
matched by the raw suffix pattern `\b...{2,}(er|ir|re|oir)\b`). This
battery re-runs the census with a POS filter so the 21-noise class is
removed by instrument, not by hand.

## Bar (verbatim, pre-registered before testing)

">=1 genuine attestation with POS-tagged infinitives re-opens;
confirmed zero keeps the fence"

Numbered pass/fail clauses (restated before testing, not modified
after):

1. At least one GENUINE postposed "[inf] !, cela/ceci/ça" attestation
   exists on the POS-tagged (genuine-infinitive) candidate set inside
   quoted-dialogue windows of revue-deux-mondes-1841. If yes: arm (a)
   of ce87-1028-role re-opens as a word-order variant.
2. If clause 1's POS-tagged census is a confirmed zero — every
   candidate classified, the noise class removed by instrument, the
   rest excluded with cause — the pairing stays fenced at
   verb-filtered level (null per §4: zero is an absence, not a kill).

## Method

1. Read BATTERY-PROTOCOL.md first. Created the lock
   `code/crowd17/next-token/locks/disloc-demonstrative-inversion-verbtags.lock`
   on start (agent id + UTC timestamp; no stale lock for this id
   existed); deleted on completion.
2. Reused the inversion census verbatim: corpus files, dialogue-span
   extraction (D1 guillemet, D2 straight double quote, D3 em-dash
   paragraphs), INF suffix pattern, and the postposed-demonstrative
   window logic are imported unchanged from
   `code/crowd17/next-token/disloc_demonstrative_inversion_census.py`
   — the candidate universe is identical: the same 37 candidates.
   Corpus (character counts): revue-deux-mondes-1841-q1.txt 3,013,552;
   q2.txt 2,964,405; q3.txt 3,054,350; q4.txt 3,165,234 (total
   12,197,541 chars; 3,590 dialogue spans; ~10,315,830 dialogue chars).
3. Rule-based filter (documented, since no POS tagger ships on the VM):
   `code/crowd17/next-token/disloc_demonstrative_inversion_verbtags_census.py`.
   For each candidate the up-to-3 left-context words are checked:
   - F1: left word is a French determiner/possessive/article →
     noun/adjective slot, excluded.
   - F2: a subject clitic (je/tu/il/elle/on/nous/vous/ils/elles) in
     the 2 left words → finite verb, excluded.
   - F3: the token itself is closed-class (votre/notre/votre) →
     excluded.
   - F4: left word is an interjection (ah/oh/eh/...) → vocative noun,
     excluded.
   Results written to
   `code/crowd17/next-token/disloc-demonstrative-inversion-verbtags_census.json`:
   **13 dropped by rule, 24 kept** (12 of the parent's 21 false-INF
   dropped; see discrepancies below).
4. True statistical POS pass: spaCy 3.8.16 + fr_core_news_sm-3.8.0
   (installed on the VM during this battery; no tagger was present
   before). `code/crowd17/next-token/disloc_demonstrative_inversion_spacy_pass.py`
   tags each INF-shaped token in a 120-char-before / 100-char-after
   context slice (context matters: isolated bare infinitives mis-tag
   as PROPN) and aligns to the LAST token of the regex match (clitic
   prefixes like "l'arracher", "s'établir" must resolve to the verb
   stem, not the clitic). Genuine-infinitive = POS VERB or AUX with
   VerbForm=Inf. Results in
   `code/crowd17/next-token/disloc-demonstrative-inversion-verbtags_spacy.json`.
5. Reconciliation: rule-based + statistical + the parent's manual
   taxonomy, every discrepancy documented (see "Instrument
   discrepancies"). Final genuine-infinitive universe: 16 candidates.

## Window-level evidence

All 37 candidates ("/" = source line break; @-offset = corpus char
offset of the infinitive-shaped word; q1..q4 =
revue-deux-mondes-1841-qN.txt). Offsets and windows are verbatim from
the parent census; the POS column is this battery's new data.

### Reconciled genuine-infinitive universe (16): all excluded with cause

1. q1 @2560691 (dquote) inf=`être`, POS=ADV (tagger error — OCR
   squished "que cela" into "quecera"; genuine infinitive by manual
   reading) `être quecela ne mange pas! — Cela \it-il sur terre ou
   sur mer?` — "cela ne mange pas" = cela subject of "mange".
   Excluded.
2. q2 @901694 (dquote) inf=`traiter`, POS=VERB Inf `traiter de
   fourbe ! / Il mitl'épée au vent en disant cela.` — "cela" is the
   object of the gerund "disant" in a separate narrative clause.
   Excluded.
3. q2 @1399795 (guillemet) inf=`faire`, POS=VERB Inf `faire un neuf,
   moi je te couperai la tête pour faire de toi un zéro. Ah! ceci
   n'est pas` — "ceci n'est pas" = ceci subject of finite "est".
   Excluded.
4. q2 @1399852 (guillemet) inf=`faire`, POS=VERB Inf `faire de toi
   un zéro. Ah! ceci n'est pas trop mal , j'espère.` — same "Ah!
   ceci n'est pas..." clause as #3; "faire" is governed by "pour".
   Excluded.
5. q2 @2264377 (guillemet) inf=`disparaître`, POS=NOUN (tagger error
   — nominalization reading of the causative "faire disparaître";
   genuine infinitive by manual reading) `disparaître ! et sur cela
   entre dans une telle fureur` — "cela" is governed by the
   preposition "sur", not a dislocated topic. Excluded with cause.
6. q3 @2812762 (guillemet) inf=`l'arracher`, POS=NOUN (tagger error —
   "devrait l'arracher"; genuine infinitive) `l'arracher de la
   poitrine! / Ceci, dit au fort de la colère et peut-être sans
   intention , tomba` — "Ceci" heads its own clause as the fronted
   (preposed) topic of "dit... tomba": the already-fenced preposed
   order, not postposed. Excluded.
7. q3 @2943820 (dquote) inf=`sortir`, POS=VERB Inf `sortir. — Ah!
   c'est toi, Paulet, s'écria-t-il, cela est heureux...` — "cela est
   heureux" = cela subject of finite "est". Excluded.
8. q4 @921933 (guillemet) inf=`déplorer`, POS=VERB Inf `déplorer !
   / — Ah ça ! monsieur, où voulez-vous en venir?` — "à"-governed
   infinitive, not a bare exclamatory infinitive; "Ah ça !" is the
   fixed interjection "ah ça". Excluded.
9. q4 @1268136 (em-dash) inf=`s'établir`, POS=VERB Inf `s'établir à
   Riquemont tout exprès pour soigner vos gastrites? A votre aise!
   Vivez, mourez, cela` — "cela" opens "cela vous regarde" as the
   subject of finite "regarde"; the infinitives belong to the
   preceding question. Excluded.
10. q4 @1268181 (em-dash) inf=`soigner`, POS=VERB Inf `soigner vos
    gastrites? A votre aise! Vivez, mourez, cela vous regarde; pour
    moi, je ne m'en` — same "cela vous regarde" finite clause as #9.
    Excluded.
11. q4 @2652536 (guillemet) inf=`dire`, POS=VERB Inf `dire avec un
    sourire moqueur : Ce n'est pas plus difficile que cela!` —
    "cela" is governed by the comparative "que". Excluded.
    (Rule F2 falsely dropped this one: "vous" is the object clitic
    of "semble", not a subject — restored manually; see
    discrepancies.)
12. q4 @2818210 (dquote) inf=`avoir`, POS=AUX Inf `avoir voulu
    étendre la portée, quelle leçon pour M. Guizot! mais que cela
    est triste pour` — "avoir"/"étendre" belong to the
    "avoir voulu" finite chain; "cela" is the subject of finite
    "que cela est triste". Excluded.
13. q4 @2818224 (dquote) inf=`étendre`, POS=VERB Inf `étendre la
    portée, quelle leçon pour M. Guizot! mais que cela est triste
    pour la France!` — same "que cela est triste" clause as #12.
    Excluded.
14. q4 @836471 (em-dash) inf=`vivre`, POS=VERB Fin (tagger error —
    "ni vivre ni mourir" is coordinate infinitive, not 3sg present;
    genuine infinitive by manual reading) `vivre ni mourir. Ruses
    que tout cela! mensonges imaginés pour auto- riser vos visites
    !` — "cela" sits inside the relative "que tout cela" (subject
    of the verbless exclamation "Ruses"), two sentences after the
    infinitives. Excluded.
15. q4 @836482 (em-dash) inf=`mourir`, POS=NOUN (same tagger error
    as #14; genuine infinitive) `mourir. Ruses que tout cela!
    mensonges imaginés pour auto- riser vos visites !` — same
    relative clause as #14. Excluded.
16. q1 @30461 (guillemet) inf=`noyer`, POS=VERB Inf (tagger false
    positive — "noyer." is sentence-initial; the context reads as the
    walnut-tree noun per the parent battery) `noyer. Elle s'écria
    incontinent : Ha! mon Dieu! quel augure de voyage est ceci?` —
    "ceci" is the subject of "est". Excluded.

### POS-confirmed noise class (21): removed by instrument

- POS=NOUN: mesure (q2 @1534042), maître (q2 @1537960), arrière
  (q2 @1975155), singulier (q3 @1766127), livre (q3 @1766138),
  guerre (q3 @2838234), vicaire (q4 @748489), heure (q4 @760488),
  désastre (q4 @921920), sombre (q4 @1750415), Contre-temps (q4
  @69300 — OCR hyphenation fragment, matches parent group C).
- POS=ADJ: dernier (q3 @2812736), premier (q4 @235572), jure (q3
  @1766175 — 1sg of jurer, finite), sourire (q4 @2652552).
- POS=DET (possessive): votre (q1 @64114), votre (q4 @1268210).
- PROPN/merged tokens: paratonnerre (q4 @56927, PROPN),
  grand-aumônier (q2 @2264351, merged token), grand-père (q2 @895149,
  merged token), Maître (q2 @2350959, PROPN vocative).

All 21 map onto the parent battery's false-INF group (A) and OCR
group (C); none was a genuine infinitive the parent had missed.

## Instrument discrepancies (documented, none changes the outcome)

1. Tagger false negatives (5 genuine infinitives the model missed,
   all restored manually with cause): être @2560691 (ADV — squished
   OCR "quecera"), disparaître @2264377 (NOUN — nominalization
   reading of "faire disparaître"), arracher @2812762 (NOUN —
   "devrait l'arracher"), vivre @836471 (VERB Fin — "ni vivre ni
   mourir" misread as 3sg present), mourir @836482 (NOUN — same
   coordinate-infinitive context).
2. Tagger false positive (1): noyer @30461 tagged VERB Inf; context
   is the walnut-tree noun (parent group A #1); excluded with cause.
3. Rule-based F2 false drop (1): dire @2652536 — "vous" is the
   object clitic of "semble" ("et semble vous"), not a subject;
   restored manually; excluded with cause (cela
   comparative-governed).
4. Rule-based filter otherwise dropped 12 of the 21 parent false-INF
   (F1 determiner-slot: 9; F2 finite: jure; F3 closed-class: 2
   "votre"); its 9 misses (bare nouns/adjectives with no left
   determiner: noyer, père, maître, arrière, aumônier, vicaire,
   heure, désastre, sombre) were all caught by the statistical pass
   — the two instruments complement each other.

## Per-clause pass/fail

1. ≥1 genuine postposed "[inf] !, cela/ceci/ça" attestation on the
   POS-tagged candidate set: **FAIL (confirmed zero).** 37 unique
   candidates → reconciled genuine-infinitive universe of 16 (11
   POS-confirmed VERB/AUX-Inf + 5 manual restorations of documented
   tagger errors) → all 16 excluded with cause; the 21 instrument
   noise (19 POS=NOUN/ADJ/DET/PROPN + 1 OCR fragment + 1
   tagger-false-positive noun) removed. 0 genuine pairings.
2. Confirmed zero → the pairing stays fenced at verb-filtered level:
   **EXECUTED.** Zero is an absence, not a refutation. The fence now
   holds at POS-tagged level, cross-checked by two independent
   instruments plus the parent manual taxonomy. Per §4 this is a
   **null**, not a kill.

## Adverses, answered

- None pre-registered ("Adverses: none listed").
- Self-check: no contradiction with the standing KILL
  (ce87-topic-licensing, bare "ce" cannot head the construction) —
  this battery tested tonic demonstratives only.
- Self-check: no contradiction with the parent NULL
  (disloc-demonstrative-inversion) — the bar anticipated exactly
  this outcome ("confirmed zero keeps the fence").
- §5.2: no standing red-team verdict touched; no overwrite, no
  escalation required.

## Verdict: NULL (fence per clause 2)

Zero genuine postposed demonstrative + bare-exclamatory-infinitive
attestations in ~10.3M characters of quoted dialogue inside
revue-deux-mondes-1841, re-tested with POS-tagged infinitives: 37
unique candidates, 16 reconciled genuine infinitives, all excluded
with cause; 21 removed as instrument noise; none pairs the
demonstrative with the infinitive as a postposed dislocation. Arm
(a) of ce87-1028-role stays fenced in both word orders at quoted-
drama level, now at POS-tagged depth. Work regenerates via the
follow-ups below.

## Follow-ups (nulls regenerate work)

Checked against battery-queue.json: neither duplicates a queued
target (`disloc-demonstrative-inversion-fullcorpus` and
`joint-order-demonstrative-pairing-census` are already queued; these
are new):

1. **disloc-demonstrative-inversion-drama-corpus** (P4): run the
   same verbtags inversion census on the in-lane French drama
   corpus (dumas-antony.txt, dumas-henri-iii.txt, dumas-kean.txt,
   dumas-tour-de-nesle.txt, dumas-mariage-louis-xv-1841.txt,
   hugo-hernani.txt, hugo-burgraves.txt in
   code/side-period/corpus/) — quoted dialogue there is denser in
   exclamatory infinitives than RDM 1841 prose, and "Moi, voler !"
   itself comes from drama. Bar: ≥1 genuine postposed attestation
   re-opens arm (a) as a register variant; confirmed zero fences
   the pairing in 1841 French drama too.
2. **disloc-demonstrative-inversion-nonbang** (P4): drop the "!"
   locality constraint — bare infinitive + postposed tonic
   demonstrative adjacency with comma/colon pause shapes ("Voler,
   cela", "Voler : cela"), no exclamation required. The parent's "!"
   window may have been the artefact, not the word order. Bar: ≥1
   genuine non-exclamatory attestation re-opens the construction;
   confirmed zero fences the pairing shape itself.

## Bookkeeping

- Census scripts (both re-runnable):
  - code/crowd17/next-token/disloc_demonstrative_inversion_verbtags_census.py
    (rule-based filter; imports the parent census verbatim)
  - code/crowd17/next-token/disloc_demonstrative_inversion_spacy_pass.py
    (spaCy fr_core_news_sm-3.8.0 statistical pass, last-token
    alignment, 120/100-char context slices)
- Outputs:
  - code/crowd17/next-token/disloc-demonstrative-inversion-verbtags_census.json
    (13 rule-dropped / 24 kept)
  - code/crowd17/next-token/disloc-demonstrative-inversion-verbtags_spacy.json
    (37 rows with pos/tag/morph + genuine_inf flag)
- Report: code/crowd17/report_inbox/battery-disloc-demonstrative-inversion-verbtags.md
  (this file).
- battery-queue.json: `disloc-demonstrative-inversion-verbtags`
  queued -> verdict/null via temp-file + rename (pre-write assert
  confirmed queued/verdictless; JSON re-validated post-write; own
  entry only; claim/bars/evidence/adverses preserved).
- Lock created on start (agent id + UTC timestamp; no stale lock for
  this id existed), deleted on completion.
- R5005, sealed gates, red-team queue untouched. Every number traces
  to the named corpus files or the census scripts; no invented data.
