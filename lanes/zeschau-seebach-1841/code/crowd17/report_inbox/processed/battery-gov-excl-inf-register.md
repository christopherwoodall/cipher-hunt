# Battery report: gov-excl-inf-register

- Target id: `gov-excl-inf-register`
- Claim: "corpus-wide census of governed exclamatory infinitives
  ('pour rire !', 'a donner lecture !', 'de croire !') with ANY topic
  in the 27.66M-char corpus"
- Date: 2026-10-09
- Worker: battery worker (subagent e76b52c6-ced4-4b6e-a036-feebfb2ef875)
- Stream: not applicable — corpus census against period French, per target
  charter (same corpus as the parent diagnostic). The 1,847-pair repaired
  parse was not used. R5005, sealed gate instances, and the red-team
  adjudication queue were not touched.

Terms (ASD-STE100): "governed exclamatory infinitive" = an infinitive
governed by a preposition (pour / à / de) used as an exclamation in its
own right ("pour rire !" = the infinitive phrase IS the exclaimed
element, with or without a dislocated topic). "Genuine attestation" =
the "!" terminates the governed infinitive phrase itself; the
infinitive is not embedded in a finite matrix clause whose "!" belongs
to the matrix, and not embedded in an exclaimed noun phrase. "Register"
= 1841 French print (the lane's 18-file 1841 corpus) plus the 3-file
wider 19th-century control.

## Parentage

Follow-up #2 of the NULL `battery-reinforced-pour-inf-diagnostic`
(2026-10-09). That battery fenced reinforced-head + governed
exclamatory infinitive (0/4 genuine) and framed the failure as "local
to the reinforced-demonstrative HEAD licensing". This battery drops the
topic constraint and asks whether the governed exclamatory infinitive
exists AT ALL in the corpus with any topic — distinguishing a
head-specific gap from a register-level absence. Does not duplicate
`disloc-demonstrative-inf` (bare tonic heads, bare infinitive),
`disloc-demonstrative-reinforced` (reinforced heads, bare infinitive),
the parent diagnostic (reinforced heads, governed infinitive), or the
in-flight `disloc-topic-inventory-excl-inf` (bare infinitives, topic
inventory).

## Bar (verbatim, pre-registered before testing)

"if the construction is unattested corpus-wide, the zero is
register-level (construction absent from 1841 French print,
head-licensing moot); if it attests with other topics, the
demonstrative-head gap is specific and the fence stands"

Numbered pass/fail clauses (restated before testing, not modified after):

1. The governed exclamatory infinitive (pour/à/de + infinitive as the
   exclaimed element, any topic or none) is UNATTESTED in the
   27.66M-char corpus — every candidate window classified, false
   friends and OCR excluded with cause. If the zero is confirmed, the
   zero is register-level: the construction itself is absent from
   1841 French print, and head-licensing is moot.
2. The construction ATTESTS with other (non-demonstrative) topics:
   ≥1 genuine window. If yes, the demonstrative-head gap is specific
   and the parent's fence stands as head-local.

## Method

1. Read BATTERY-PROTOCOL.md first. Created the lock
   `code/crowd17/next-token/locks/gov-excl-inf-register.lock` on start
   (agent id + UTC timestamp 2026-10-09T08:24:33Z; no stale lock for
   this id existed); deleted on completion.
2. Ran a reproducible census script:
   `code/crowd17/next-token/gov_excl_inf_register_census.py` (same
   corpus as the parent diagnostic; P1/P2 design below). Raw results in
   `code/crowd17/next-token/gov-excl-inf-register_census.json`
   (per-file sizes, "!" counts, all 859 candidate windows with
   prep/infinitive/dist fields).
3. Corpus, identical to the parent diagnostic (character counts
   recomputed in-session):
   - 1841-register lane corpus (French files only): 18 files,
     25,670,258 characters, 4,995 "!" — guizot-memoires t1/t2/t3/t5-t6,
     nesselrode v7/v8/v9/v10, revue-deux-mondes-1841 q1/q2/q3/q4,
     metternich-papiere v4/v6, talleyrand-memoires-v1,
     pozzo-di-borgo-correspondance-v1, levant-correspondence-1841-p3.
   - Wider 19th-century register: 3 files, 1,987,682 characters,
     901 "!" — data/gutenberg-17489-miserables1.txt (Les Misérables
     tome 1, 1862), data/gutenberg-30513-tocqueville-t1.txt
     (Démocratie en Amérique t1, 1835),
     data/gutenberg-30514-tocqueville-t2.txt (t2, 1840).
   - Total: 21 files, 27,657,940 characters, 5,896 "!".
   - German files excluded with cause (register is French, not 1841
     French): allgemeine-zeitung-augsburg-1841-01-11 through -01-24
     (14 files) and adb-zeschau-heinrich-anton-von.txt.
4. Search patterns (verbatim, from the script):
   - P1 (candidate): for every "!" in the corpus, take the 120 chars
     before it; run GOV_INF on that segment:
     `\b(pour|à|a|de|d['’])\s+(?:[a-zàâäçéèêëîïôöùûü'\-]{1,6}\s+){0,2}
     \b[a-zàâäçéèêëîïôöùûü']{2,}(er|ir|re|oir)\b` (case-insensitive) —
     the parent battery's P3 pattern: preposition (pour/à/a/de/d') +
     up to two short tokens (clitics, articles, pronouns, "ne"/"pas")
     + an infinitive-shaped word. The match closest to the "!" is
     kept; between its end and the "!" there must be no [.;]
     (sentence-internal exclamation only).
   - P2 (banding): dist = characters from the end of the
     infinitive-shaped word to the "!". Tight band dist ≤ 40 (477
     candidates) is the discriminating band — the exclaimed element
     is the infinitive phrase itself. Wide band 41 ≤ dist ≤ 120 (382
     candidates) triaged separately; a genuine exclamatory infinitive
     there needs a long complement between infinitive and "!".
   - All 859 candidates were classified by hand (regex cannot separate
     -er infinitives from nouns/adjectives in -er; unaccented "a" is
     verb-avoir noise; the "!" may belong to a matrix finite clause).
5. Recall due-diligence: P1 admits only "!"-terminated windows
   ("?"-terminated exclamatory infinitives unsearched — fenced as
   follow-up #2's target); the 120-char lookback misses infinitives
   with complements longer than 120 chars before the "!" (fenced as a
   limitation; the wide band to 120 found no genuine, so the marginal
   recall beyond 120 is thin); the two-short-token pre-infinitive cap
   excludes longer prepositional chains ("pour ne plus jamais rire"
   unsearched — fenced as follow-up #2's target).

## Window-level evidence

### Census yields

- 1841 register: 734 candidates (411 tight) from 4,995 "!".
- Wider 19c: 125 candidates (66 tight) from 901 "!".
- **0 of 859 candidates is genuine.** Classified: 477 tight-band
  (dist 0–40) individually, 382 wide-band (dist 41–120) scanned.
  Exclusion causes, with the nearest near-misses verbatim ("/" marks
  line breaks):

**Cause A — OCR "-er" false friends** (the infinitive-shaped word is a
noun/adjective/name in -er/-re: terre, gloire, mère, misère, matière,
manière, l'Angleterre, l'avenir, l'empire, l'enfer, l'histoire, pierre,
traître, notre, votre, première, contre, quatre, propre, désordre,
chambre, caractère, affaire, désir, misère, l'atelier, l'observatoire,
Cythère, Thénardier, Weber, Müller, Montfort, premier, dernière,
septuagénaire, locataire, prière, madère, lumière, bière, cure,
colère). ~40% of candidates. Example (revue-deux-mondes-1841-q3):
"Je vous en prie, lui disait-elle souvent, ayez pitié de mon père!"
— "père" matched as -re infinitive; no infinitive present.

**Cause B — governed infinitive embedded in a finite matrix clause**
whose "!" belongs to the matrix (~45% of candidates). Examples:
- (revue-deux-mondes-1841-q3) "Faut-il que ces Allemands soient
  simples pour croire à de pareilles sornettes!" — "!" exclaims the
  finite "Faut-il que..." clause; "croire" is its purpose adjunct.
- (gutenberg-17489-miserables1) "Tu me demandes trois jours pour
  t'en aller!" — finite interrogative matrix.
- (revue-deux-mondes-1841-q1) "comme il s'arrange habilement pour
  mourir !" — finite "comme" clause.
- (metternich-papiere-v4) "brülait d'envie de la faire, ne voulait
  tout juste pas, pourvu qu'elle püt etre e'vite'e !" — finite.

**Cause C — infinitive embedded in an exclaimed noun/adjective phrase**
(the phrase is exclaimed, not the infinitive; ~10%). The nearest
near-misses:
- (revue-deux-mondes-1841-q4, dist 0) "des perdreaux à tuer!" — the
  exclaimed element is the NP "des perdreaux à tuer"; "tuer" is its
  complement. Not the "pour rire !" shape.
- (revue-deux-mondes-1841-q2, dist 9) "Nations! mot pompeux pour dire
  barbarie!" — exclaimed appositive NP; "dire" embedded.
- (gutenberg-17489-miserables1, dist 0) "Cinq louis d'or à gagner!" —
  exclaimed offer-NP; "gagner" embedded.
- (revue-deux-mondes-1841-q4, dist 11) "trop heureux de s'en être bien
  tiré!" — exclaimed adjective phrase; infinitive governed by the
  adjective.
- (revue-deux-mondes-1841-q2, dist 71) "Quel art pour tout
  s'approprier, depuis Homère jusqu'à Tacite, depuis Simonide jusqu'à
  Symmaque!" — exclamative "Quel art pour..." NP; the closest
  wide-band shape, still NP-embedded.
- (revue-deux-mondes-1841-q3, dist 13) "que d'intelligence pour
  vivifier ces études!" — "que de" exclamative NP.
- (nesselrode-v8, dist 14) "Quelle tristesse de voir des Russes se
  complaire à dénigrer leur pays !" — "Quelle" exclamative NP.

**Cause D — "!" belongs to a following interjection/quotation, not the
infinitive** (~5%). Examples:
- (gutenberg-17489-miserables1, dist 0) "Ah! ne dis pas cela, même
  pour rire!" — the corpus's only "pour rire"; it is an adjunct
  inside an imperative clause ("ne dis pas cela"), not a standalone
  exclamatory infinitive. Excluded with cause: embedded, and the "!"
  belongs to the imperative sentence.
- (revue-deux-mondes-1841-q1, dist 9) "les chefs interrompaient le
  discours pour s'écrier : Saga!" — "!" terminates "Saga".
- (revue-deux-mondes-1841-q4, dist 13) "s'attacha à témoigner par les
  cris de :« À bas Godoï!" — "!" terminates the quoted cry.

### Positive controls (the census detects the shape)

The BARE exclamatory infinitive — same exclamatory-infinitive family,
no preposition — DOES attest, proving the zero is not a detection
failure:
- (revue-deux-mondes-1841-q3) "Voyez cependant où la manie de
  philosopher entraîne les poètes : ôter à Moïse son auréole !" —
  genuine bare exclamatory infinitive, zero/implied topic.
- (gutenberg-17489-miserables1) "Voir mille objets pour la première
  et pour la dernière fois, quoi de plus mélancolique et de plus
  profond!" — genuine bare exclamatory infinitive.
- (nesselrode-v9) "Rompre avec Francfort et envoyer de gros canons
  contre l'ile d'Alsen!" — genuine bare exclamatory infinitive pair.
- (revue-deux-mondes-1841-q4) "Abdiquer le lendemain d'un jour de
  victoire!" — genuine bare exclamatory infinitive.
The register HAS the exclamatory infinitive; it is the GOVERNED
variant (pour/à/de + infinitive as the exclaimed element) that never
occurs.

### Due-diligence checks

- The zero is not an empty-search artifact: 859 governed-infinitive
  + "!" candidates exist in 27,657,940 characters — governed
  infinitives are frequent before exclamation marks; they are just
  never THEMSELVES the exclaimed element.
- The tight band (dist ≤ 40, 477 candidates) is where any genuine
  "pour rire !" shape must live; all 477 classified, 0 genuine.
- The wide band (382 candidates) contains only finite matrices,
  exclamative NPs, quoted interjections, and OCR noise — no
  long-complement exclamatory infinitive surfaced.
- The wider 19c control (Misérables 1862, Tocqueville 1835/1840)
  agrees: 125 candidates, 0 genuine — the zero is not 1841-specific
  within the sampled 19th century.

## Per-clause pass/fail

1. Governed exclamatory infinitive unattested corpus-wide →
   register-level zero: **CONFIRMED (PASS).** 0 genuine in 859
   candidates across 27,657,940 characters. The construction is
   absent from the sampled 1841 French print (and from the wider
   19c control); head-licensing is moot for the governed variant.
2. Construction attests with other topics → demonstrative-head gap
   specific: **ANTECEDENT FALSE.** No attestation with any topic —
   not with personal pronouns, not with nouns, not with zero topic.
   The demonstrative-head gap cannot be "specific" because there is
   no construction for any head to license.

## Reframe of the parent null (headline, not an overwrite)

The parent NULL (`battery-reinforced-pour-inf-diagnostic`) concluded
"the failure is local to the reinforced-demonstrative HEAD licensing,
bare or governed". This census reframes that: for the GOVERNED
variant, the failure is not head-local — the governed exclamatory
infinitive is absent register-wide, so the reinforced-head question
is moot, not answered. The parent's fence of the reinforced pairing
stands (nothing attests), but its explanation is superseded for the
governed variant: register absence, not head licensing. The parent's
BARE-variant fence is UNAFFECTED by this reframe — the bare
exclamatory infinitive attests with other topics (ôter/Voir/Rompre/
Abdiquer above), so the reinforced-head gap for the bare
construction remains head-specific. Per §5.2: no red-team verdict
touched, nothing overwritten — the reframe is recorded here for the
supervisor.

## Adverses, answered

- None pre-registered ("Adverses: none listed").
- Self-check: does this null contradict the standing KILL
  (ce87-topic-licensing, bare "ce" cannot head the construction)? No —
  different construction (governed vs bare) and no bare-"ce"
  surfaced.

## Verdict: NULL (register-level zero confirmed; fork resolved)

Zero genuine governed exclamatory infinitives with any topic in
27.66M characters of 19th-century French (859/859 candidates
classified: ~40% OCR -er false friends, ~45% finite-matrix
embeddings, ~10% exclaimed-NP embeddings, ~5% quotation/interjection
"!"). The parent null's two explanations are distinguished: the zero
is REGISTER-LEVEL, not head-local — the construction is absent from
the register, so demonstrative-head licensing of the governed variant
is moot. Work regenerates via the follow-ups below.

## Follow-ups (nulls regenerate work)

1. **gov-excl-inf-drama** (P3): run this battery's governed-shape
   census (P1/P2, any topic) in the drama corpus (the sibling
   `disloc-demonstrative-drama` register — the natural habitat of
   exclamatory infinitives). Bar: ≥1 genuine attestation in drama →
   the zero is print-register-specific and re-opens the pairing at
   register level; confirmed zero → the construction is absent from
   both registers and the fence hardens. (Discriminating frames;
   coordinates with, does not duplicate, the in-flight drama
   battery, which tests reinforced heads.)
2. **gov-excl-inf-recall** (P3): close this battery's fenced recall
   gaps — "?"-terminated windows ("Lui, pour rire ?"), preposition-
   to-infinitive spans longer than two short tokens ("pour ne plus
   jamais rire !"), and exclamations adjacent to dash/colon pause
   marks. Bar: ≥1 genuine in the widened search re-opens the
   register question; confirmed zero hardens the register-level
   zero. (Different search, not a re-run — targets unsearched
   windows only.)
3. **gov-excl-inf-np-boundary** (P2): inventory the governors
   (pour/à/de) of the Cause-C near-miss exclaimed NPs ("des
   perdreaux à tuer !", "mot pompeux pour dire barbarie !", "Six
   mois à gagner sept sous par jour !", "Quel art pour tout
   s'approprier !") to map the exact boundary: NP-embedded governed
   infinitives license exclamation while the bare infinitive phrase
   never does. Bar: a systematic governor asymmetry (e.g. only "à"
   in exclaimed NPs, never "pour") narrows the register gap to a
   governor effect; no asymmetry → the boundary is phrase-level
   (NP vs infinitive phrase), not governor-level.

## Bookkeeping

- Census script:
  code/crowd17/next-token/gov_excl_inf_register_census.py
  (re-runnable; same corpus as the parent diagnostic; outputs
  gov-excl-inf-register_census.json with per-file sizes, "!" counts,
  and all 859 candidate windows with prep/infinitive/dist fields).
- Report: code/crowd17/report_inbox/battery-gov-excl-inf-register.md
  (this file).
- battery-queue.json: `gov-excl-inf-register` queued -> verdict/null
  via temp-file + rename (pre-write assert confirmed queued/
  verdictless; JSON re-validated post-write; own entry only;
  claim/bars/evidence/adverses preserved).
- Lock created on start (agent id + UTC timestamp
  2026-10-09T08:24:33Z), deleted on completion. No stale lock for
  this target existed.
- R5005, sealed gates, red-team queue untouched. Every number traces
  to the named corpus files or the census script; no invented data.
