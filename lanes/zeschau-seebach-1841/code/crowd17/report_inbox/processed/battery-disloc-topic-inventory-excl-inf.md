# Battery report: disloc-topic-inventory-excl-inf

- Target id: `disloc-topic-inventory-excl-inf`
- Claim: "census ALL bare exclamatory infinitives in the 27.66M-char corpus
  and tabulate which topics license them"
- Date: 2026-10-09
- Worker: battery worker (subagent 5bda8f1b-d435-4755-a308-39cc329d61cd)
- Stream: not applicable — corpus census against period French, per target
  charter. The 1,847-pair repaired parse was not used. R5005, sealed gate
  instances, and the red-team adjudication queue were not touched.

Terms (ASD-STE100): "dislocation" = a topic moved to the front of the clause,
set off by a pause ("Moi, je sais" = "me, I know"). "Tonic" = the stressed
form of a pronoun (moi, lui). "Exclamatory infinitive" = an infinitive used as
an exclamation ("Moi, voler !" = "me, to steal!"). "Bare" = the infinitive
stands alone: no governing preposition (de, pour, à), no "que", no modal or
perception verb governing it (falloir, pouvoir, vouloir, entendre, voir), and
no resumptive clitic between the topic and the verb. "Topic licensing" = the
dislocated topic is what the exclamatory infinitive is said of.

## Parentage

Follow-up #2 of the NULL `disloc-demonstrative-reinforced` (2026-10-09),
which fenced the whole tonic-demonstrative + bare-infinitive family (bare
heads fenced by `disloc-demonstrative-inf`, reinforced heads fenced by
`-reinforced`). The parent's discriminating question: is the demonstrative
gap sampling noise (re-open the family) or a genuine topic-licensing
restriction (fence holds, residual closes)? This battery answers it by
censusing EVERY bare exclamatory infinitive in the same 27.66M-char corpus
and tabulating the topic inventory. Does not duplicate either demonstrative
census (new question: the full topic inventory, not the demonstrative head).

## Bar (verbatim, pre-registered before testing)

"if any non-pronominal topic (demonstrative excluded, nouns/others) licenses
the bare exclamatory infinitive, the demonstrative gap is sampling noise ->
re-open the family; if only personal pronouns do, the fence holds and the
residual closes"

Numbered pass/fail clauses (restated before testing, not modified after):

1. At least one GENUINE bare exclamatory infinitive headed by a
   non-pronominal, non-demonstrative topic (noun, proper noun, quantifier,
   other) exists in the 27.66M-char corpus. If yes: the demonstrative gap
   is sampling noise → re-open the family (promote).
2. If clause 1's census is a confirmed zero — every candidate window
   classified, governed infinitives / vocatives / finite clauses / OCR
   excluded with cause — and only personal pronouns head genuine
   attestations, the fence holds and the residual closes (kill of the
   re-open hypothesis, per §4: the distributional test rejects the
   sampling-noise claim at the lane's census standard).

## Method

1. Read BATTERY-PROTOCOL.md first. Created the lock
   `code/crowd17/next-token/locks/disloc-topic-inventory-excl-inf.lock` on
   start (no stale lock for this id existed); deleted on completion.
2. Ran a reproducible census script:
   `code/crowd17/next-token/disloc_topic_inventory_census.py`. Raw results in
   `code/crowd17/next-token/disloc-topic-inventory-excl-inf_census.json`.
3. Corpus, identical to `disloc-demonstrative-inf` / `-reinforced`
   (character counts recomputed in-session, matching to the character):
   - 1841-register lane corpus (French files only): 18 files, 25,670,258
     characters — guizot-memoires t1/t2/t3/t5-t6, nesselrode v7/v8/v9/v10,
     revue-deux-mondes-1841 q1/q2/q3/q4, metternich-papiere v4/v6,
     talleyrand-memoires-v1, pozzo-di-borgo-correspondance-v1,
     levant-correspondence-1841-p3.
   - Wider 19th-century register: 3 files, 1,987,682 characters —
     data/gutenberg-17489-miserables1.txt (Les Misérables tome 1, 1862),
     data/gutenberg-30513-tocqueville-t1.txt (Démocratie en Amérique t1,
     1835), data/gutenberg-30514-tocqueville-t2.txt (t2, 1840).
   - Total: 21 files, 27,657,940 characters of 19th-century French.
   - German files excluded with cause (register is French, not 1841 French):
     allgemeine-zeitung-augsburg-1841-01-11 through -01-24 (14 files) and
     adb-zeschau-heinrich-anton-von.txt.
4. Search patterns (verbatim, from the script):
   - P1 (topic inventory): `TOPIC\s*[,;:]` where TOPIC = PRON
     (moi|toi|lui|elle|nous|vous|eux|elles|soi) | DEM (cela|ceci|ça|
     celui|ceux|celle|celles + optional -là/-ci) | NP (determiner + 1-3
     words) | PROP (capitalized word) | OTH (tout le monde|personne|
     chacun|chacune|rien|quelqu'un|jamais|toujours|encore|souvent|
     rarement|déjà|bientôt|vite|bien|mal|mieux|pis), case-insensitive.
     Window = text from the topic start through the next [!?.]
     (inclusive), capped at 200 characters.
   - P2 (exclamatory filter): the window must contain "!" before its end.
   - P3 (infinitive candidate): an infinitive-shaped word
     (`[a-zàâäçéèêëîïôöùûü']{2,}(er|ir|re|oir)`) inside the window.
5. Triage (all scripted, then hand-classified):
   - 341,564 topic-comma hits → 3,310 exclamatory candidates → 3,304
     unique (file, window).
   - Clean-shape filter (only negation/clitic interveners between the topic
     comma and the infinitive — the definitional bare shape): 236
     candidates, ALL hand-reviewed with corpus context.
   - Pronoun class: 53 candidates, ALL individually reviewed.
   - Demonstrative class: 10 candidates, ALL individually reviewed.
   - Safety net (1–3 non-preposition interveners, verb-lexicon check):
     534 → 100 hits, ALL individually reviewed with corpus context.
   - Coverage claim: every candidate structurally compatible with the bare
     construction (infinitive reachable from the topic without an
     intervening governor) was hand-reviewed. Remaining unreviewed
     candidates have ≥4 intervening words or a governing preposition/modal
     between topic and infinitive — structurally incompatible with bareness.

## Window-level evidence

### The two genuine attestations (both personal-pronoun-headed)

1. `Moi, voler!` (revue-deux-mondes-1841-q1) — topic "moi" (personal tonic
   pronoun), bare infinitive "voler". Context: "— Moi, voler! répond le bon
   Charlemagne..." The known shape precedent, re-confirmed. GENUINE.
2. `Lui qui n'était rentré en France qu'à la suite de l'étranger, s'opposer
   avec acharnement à un projet qui avait pour but de fermer les portes de
   la capitale à l'étranger!` (revue-deux-mondes-1841-q2) — topic "Lui"
   (personal tonic pronoun + relative clause), bare infinitive "s'opposer".
   Context: "Qu'il avait été mal inspiré! Lui qui n'était rentré en France
   qu'à la suite de l'étranger, s'opposer avec acharnement à un projet...!"
   A second, independent pronoun-headed attestation. GENUINE.

### Non-pronominal topics: confirmed zero

Every noun/proper-noun/quantifier-headed candidate was excluded with cause.
The recurring exclusion classes (with the strongest near-misses first):

- Governed by a modal/volitional verb (the dominant false-friend class):
  `il fallut, sous peine de l'avoir pour ennemi, en substituer une pure et
  simple...!` (talleyrand; governed by "fallut" — the "ennemi" topic parse
  was a misread); `auraient pu et dû, dans leur lutte, s'arrêter sur cette
  pente...!` (guizot t1; governed by "pouvoir/devoir"); `Puisse le ciel,
  sire, qui vous a fait le plus grand des rois, vous rendre encore le plus
  heureux des hommes!` (rdm q1; governed by "puisse"); `on a entendu...
  blâmer sa condescendance et railler son dévouement!` (rdm q1; governed by
  "entendre"); `J'ai vu... de malheureuses jeunes femmes... passer... des
  journées entières courbées...!` (rdm q2; governed by "voir"); `si je
  pouvais m'affranchir de Rivera et de Ferré, passer le Parana...!`
  (rdm q1; governed by "pouvoir"); `il m'a fallu... faire une marche de neuf
  jours...!` (rdm q3; governed by "falloir").
- Governed by a preposition: `cela, même pour rire!` (miserables; "pour");
  `forcé de faire mouvoir toute cette masse...!` (metternich v6; "de");
  `d'avoir une autre politique et de la pratiquer!` (rdm q1; "de").
- Infinitive as subject of a cleft (the "!" exclaims the cleft, not the
  infinitive): `des hommes, ne pas l'empêcher, s'y prêter par son silence,
  ne rien faire enfin, c'était faire tout!` (miserables); `reprendre son
  nom, redevenir par devoir le forçat Jean Valjean, c'était là vraiment
  achever sa résurrection...!` (miserables); `Il me convient de me taire ou
  de me dénoncer,—cacher ma personne ou sauver mon âme... c'est moi, c'est
  toujours moi...!` (miserables).
- Topic-less infinitive series (no dislocated topic at all): `être vieux,
  être tutoyé par le premier venu, être fouillé par le garde-chiourme,
  recevoir le coup de bâton de l'argousin!` (miserables, the convict
  litany); `Battre les Anglais! prendre sur eux d'infernales revanches, et
  couvrir la plage de marchandises précieuses...!` (rdm q2); `les critiquer,
  les chicaner, les accuser d'avoir commis une faute...!` (rdm q2, governed
  by "pour que personne ne puisse"); `Réchauffer le vieil orgueil national,
  inspirer la confiance, l'espérance, la passion publique...!` (rdm q3,
  hortative series); `Écrire? Écrire, lorsque toute vocation s'est
  évanouie, occuper le public de sa personne, imposer ses œuvres...!`
  (rdm q1).
- Vocative/interjection + topic-less infinitive (vocatives excluded per the
  lane taxonomy): `O mon Dieu, être là et ne pouvoir mourir!` (rdm q1);
  `Mon enfant! s'écria-t-elle, aller chercher mon enfant!` (miserables).
- Optative infinitive with its own subject (not topic-headed): `paix, le
  genre humain tout entier être uni d'esprit et de cœur...!` (guizot t5-t6;
  "paix" is an interjection, the infinitive clause carries its own subject).
- Finite clauses, noun enumerations/appositives, imperative verbs, OCR
  noise: `les Anglais, le beurre est si cher!`; `le Tasse, Millon,
  Klopstock, Gessner, Voltaire même!`; `toi, corbeau au capuchon noir,
  ménage le blé de mon champ!` ("ménage" is imperative); `souiUer` =
  OCR for "souiller" in a "tu veux"-governed clause (rdm q4).

### Demonstrative re-check

The 10 demonstrative-class candidates are the same false friends already
classified by `disloc-demonstrative-inf` and `-reinforced` (OCR noise,
finite clauses, "pour"-governed, quotation introductions, vocatives).
Zero genuine — consistent with both fenced nulls; no contradiction, no new
adverse.

### Topic-licensing tabulation (27,657,940 characters)

| Topic class | Genuine bare exclamatory infinitives |
|---|---|
| Personal tonic pronouns (moi, lui) | 2 |
| Nouns / noun phrases | 0 |
| Proper nouns | 0 |
| Quantifiers / adverbial topics | 0 |
| Demonstratives (bare + reinforced) | 0 |

## Per-clause pass/fail

1. ≥1 genuine non-pronominal, non-demonstrative topic-headed bare
   exclamatory infinitive: **FAIL (confirmed zero).** 3,304 unique
   candidates triaged; every structurally compatible window hand-reviewed
   with corpus context; all noun-headed candidates excluded with cause
   (governed infinitives, cleft subjects, topic-less series, vocatives,
   finite clauses, OCR).
2. Only personal pronouns license the construction → fence holds, residual
   closes: **EXECUTED.** Exactly 2 genuine attestations in 27.66M
   characters, both headed by personal tonic pronouns ("Moi, voler !";
   "Lui, ...s'opposer... !"). Nouns dominate topic position in this corpus
   yet never head the construction — the demonstrative gap is a genuine
   topic-licensing restriction, not sampling noise.

## Adverses, answered

- None pre-registered ("Adverses: none listed").
- Self-check: does this KILL contradict the standing NULLs
  (`disloc-demonstrative-inf`, `disloc-demonstrative-reinforced`)? No — it
  strengthens them: the fence they erected now rests on a positive
  distributional finding (pronoun-only licensing) rather than on absence
  alone. The residual they left open ("is the gap sampling noise?") is the
  thing this battery closes, exactly as chartered.
- Self-check: does this KILL contradict the standing KILL
  (`ce87-topic-licensing`, bare "ce" cannot head the construction)? No —
  different construction (tonic topics, not atonic "ce"); nothing
  bare-"ce" surfaced.
- Self-check: the "Lui, ...s'opposer...!" attestation — is "lui" really the
  topic, or is the relative clause doing the work? The head is the personal
  pronoun "lui"; the relative clause only specifies it. It counts as
  pronoun-headed under the bar's taxonomy (non-pronominal = nouns/others).
- §5.2: no standing red-team verdict touched; no overwrite, no escalation
  required. Per the task brief, promotions are ratified by the red team
  only — this battery promotes nothing.

## Verdict: KILL (of the sampling-noise / re-open hypothesis)

Zero non-pronominal topics license the bare exclamatory infinitive in
27.66M characters of 19th-century French; the only licensers are personal
tonic pronouns (2 genuine attestations: "Moi, voler !" and "Lui,
...s'opposer... !"). The demonstrative gap is a genuine topic-licensing
restriction, not sampling noise. The tonic-demonstrative family fence
holds, and the residual — whether the gap could be a sampling artifact —
is closed. The "Moi, voler !" precedent stands as the pronoun-licensed
shape; demonstratives never head it.

## Notes for the supervisor / red team (not queued targets)

1. The positive distributional claim "only personal tonic pronouns license
   the bare exclamatory infinitive in this register" is promotion-grade
   material for the red team to adjudicate — this job does not promote.
2. Watch item: the in-flight sibling `disloc-demonstrative-drama` censuses
   the drama corpus. If drama yields noun-headed bare exclamatory
   infinitives, the pronoun-only restriction found here is
   register-specific and the fence re-opens — flag any conflict to the red
   team rather than overwriting this verdict.

## Bookkeeping

- Census script: code/crowd17/next-token/disloc_topic_inventory_census.py
  (re-runnable; outputs disloc-topic-inventory-excl-inf_census.json with
  per-file sizes, hit counts per topic class, and all 3,310 candidate
  windows).
- Report: code/crowd17/report_inbox/battery-disloc-topic-inventory-excl-inf.md
  (this file).
- battery-queue.json: `disloc-topic-inventory-excl-inf` queued ->
  verdict/kill via temp-file + rename (pre-write assert confirmed
  queued/verdictless; JSON re-validated post-write; own entry only;
  claim/bars/evidence/adverses preserved).
- Lock created on start (agent id + UTC timestamp), deleted on completion.
  No stale lock for this target existed.
- R5005, sealed gates, red-team queue untouched. Every number traces to the
  named corpus files or the census script; no invented data.
