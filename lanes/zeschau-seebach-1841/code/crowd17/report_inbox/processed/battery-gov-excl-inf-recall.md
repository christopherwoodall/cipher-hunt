# Battery report: gov-excl-inf-recall

- Target id: `gov-excl-inf-recall`
- Claim: "close recall gaps: '?'-terminated windows, longer preposition->infinitive spans, dash/colon-adjacent exclamations"
- Date: 2026-10-09
- Worker: battery worker (subagent 40bcb348-8c72-47ef-b737-384628a09e67)
- Stream: not applicable — corpus census against period French, per target
  charter (same 27.66M-char corpus as the register battery, byte-identical
  file set, asserted in-session). The 1,847-pair repaired parse was not
  used. R5005, sealed gate instances, and the red-team adjudication queue
  were not touched.

Terms: "governed exclamatory infinitive" = a preposition-governed
infinitive phrase (pour / à / de + infinitive) that IS itself the
exclaimed element ("pour rire !"). "Genuine attestation" = the
terminator (! or ?) terminates the governed infinitive phrase itself;
the infinitive is not embedded in a finite matrix clause whose
terminator belongs to the matrix, not embedded in an exclaimed noun
phrase, and (for '?') the "?" marks exclamatory incredulity at the
infinitive phrase, not a matrix question.

## Parentage

Follow-up #2 of the NULL `battery-gov-excl-inf-register` (2026-10-09).
That battery ran 859 candidates through the parent's search design and
found 0 genuine, concluding the governed exclamatory infinitive is
register-absent from 1841 French print — but fenced three recall gaps
its design never searched: "?"-terminated windows, preposition-to-
infinitive spans longer than two short tokens, and exclamations
adjacent to dash/colon pause marks. THIS battery searches exactly those
three window classes, and nothing else.

## Bar (verbatim, pre-registered before testing)

">=1 genuine attestation in the widened search re-opens the register question; confirmed zero closes the recall gap"

Numbered pass/fail clauses (restated before testing, not modified after):

1. If >=1 genuine attestation is found in the widened search, the
   register question is re-opened (the parent's register-level zero is
   undercut).
2. If the widened search confirms zero genuine attestations, the recall
   gap is closed (the parent's zero stands with recall due-diligence
   complete).

## Method

1. Read BATTERY-PROTOCOL.md first. Created the lock
   `code/crowd17/next-token/locks/gov-excl-inf-recall.lock` on start
   (agent id + UTC timestamp 2026-10-09T08:33:00Z; no stale lock for
   this id existed); deleted on completion.
2. Ran a reproducible census script:
   `code/crowd17/next-token/gov_excl_inf_recall_census.py`. Raw results
   in `code/crowd17/next-token/gov-excl-inf-recall_census.json`
   (per-gap yields, per-file sizes, every candidate window with
   prep/infinitive/dist/absolute-terminator-offset fields).
   Classification record in
   `code/crowd17/next-token/gov-excl-inf-recall_classification.json`
   (auto-A denylist, per-candidate cause decisions, wide-scan log).
3. Corpus, byte-identical to the parent battery (file set pinned by
   name from the parent's census JSON; the corpus directory has grown
   since the parent's run — drama ingest — so name-pinning, not
   directory listing, was used; total asserted in-session):
   - 1841-register lane corpus: 18 files, 25,670,258 characters,
     4,995 "!", 6,843 "?" — guizot-memoires t1/t2/t3/t5-t6,
     nesselrode v7/v8/v9/v10, revue-deux-mondes-1841 q1/q2/q3/q4,
     metternich-papiere v4/v6, talleyrand-memoires-v1,
     pozzo-di-borgo-correspondance-v1, levant-correspondence-1841-p3,
     harvest-log.txt (as in the parent set).
   - Wider 19th-century register: 3 files, 1,987,682 characters,
     901 "!", 915 "?" — data/gutenberg-17489-miserables1.txt (1862),
     data/gutenberg-30513-tocqueville-t1.txt (1835),
     data/gutenberg-30514-tocqueville-t2.txt (1840).
   - Total: 21 files, 27,657,940 characters, 5,896 "!", 7,758 "?".
4. The three gap searches (exact patterns in the script); each targets
   windows the parent's design could not produce:
   - G1 ('?'-terminated): parent keyed ONLY on "!". For every "?" in
     the corpus: 120-char lookback, the parent's GOV_INF pattern
     verbatim (prep + 0-2 short tokens + infinitive-shaped word),
     closest match to "?", no [.;] between match end and "?" (same
     sentence-internal rule as the parent). ALL G1 candidates are
     novel by construction. 1,487 candidates (871 tight, dist<=40).
   - G2 (long spans): parent's GOV_INF allowed at most 2 short tokens
     between prep and infinitive. For every "!": 300-char lookback,
     LONG_INF = prep + 3-6 short tokens (each <=8 chars) +
     infinitive-shaped word, closest match to "!", same no-[.;]-tail
     rule. Novelty is structural: no G2 match span is reproducible by
     the parent's regex (verified: the {3,6}-token floor vs the
     parent's {0,2} ceiling makes the spans disjoint; 35 G2 candidates
     share a terminator with a parent candidate, but in every case the
     parent kept a SHORTER match at that "!" and the long-span reading
     was untested). 349 candidates (134 tight).
   - G3 (dash/colon-adjacent): parent kept only the CLOSEST match per
     "!" (its candidates() keeps max g.end()). For every "!":
     120-char lookback, ALL GOV_INF matches; keep the non-closest
     ones where a dash (em/en/hyphen) or colon lies between the match
     end and the "!" (no [.;] between match end and the pause mark).
     These pause-mark-adjacent exclamations are exactly what the
     parent's closest-match rule discarded. 38 candidates (3 tight).
   - Dist = chars from infinitive-shaped word end to terminator.
     Tight band dist<=40 is the discriminating band (the exclaimed
     element is the infinitive phrase itself).
5. Classification. Tight band (1,008 candidates) fully classified by
   hand, in two passes. Pass 1 (automatic): 371 candidates whose
   infinitive-shaped word is on the NEVER_INF denylist — words that
   can never be French infinitives (nouns, adjectives, determiners,
   prepositions, adverbs, names, conjugated verb forms, OCR garbage;
   denylist recorded verbatim in the classification JSON; dual-use
   words like rire/dire/pouvoir/sourire/dîner were NOT denylisted and
   were read) — excluded as cause A, the parent's cause-A class.
   Pass 2 (manual): the remaining 637 tight candidates read window by
   window and classified B (finite-matrix embedding), C
   (exclaimed-NP embedding), D (terminator belongs to a following
   quotation/interjection), E (interrogative matrix, '?' windows), or
   GENUINE. Wide band (866 candidates) scanned in full, parent
   battery's "scanned" treatment. The 81 G3-diag candidates
   (non-closest matches with NO dash/colon — untested by the parent
   but outside this battery's three named gaps) were scanned as due
   diligence: 16 tight, 0 genuine (all B/C/D/A).

## Window-level evidence

### Census yields

- G1 '?'-windows: 1,487 candidates (871 tight). Tight: 559 E, 371 A
  (308 auto + 4 hand: "l'enfer", "tembre" [=septembre, hyphenation
  split], "l'escadre", "rire"-as-noun in "éclat de rire"). 616 wide
  scanned, all E.
- G2 long spans: 349 candidates (134 tight). Tight: 61 B, 64 A (61
  auto + "désir"-as-noun, "bien-être", "désertèrent" finite), 3 C,
  6 D. 215 wide scanned.
- G3 dash/colon: 38 candidates (3 tight: 1 B + 2 auto-A). 35 wide
  scanned (B/C/D).
- **0 of 1,874 gap candidates is genuine.**

### Cause distribution (tight band, 1,008 classified)

- E — interrogative matrix, "?" belongs to a question (559; all G1):
  e.g. (guizot-memoires-t1 @36022) "Qui êtes-vous pour
  m'attaquer?"; (gutenberg-17489-miserables1 @299475) "Qu'est-ce que
  tu ferais, Favourite, si je cessais de t'aimer?"; (revue-deux-
  mondes-1841-q4 @78828) "des perdreaux à tuer! ne dirait-on pas que
  ce soit du poison / à prendre?" — the "?" belongs to "ne
  dirait-on pas...?".
- B — governed infinitive embedded in a finite matrix clause whose
  "!" belongs to the matrix (62): e.g. (metternich-papiere-v6
  @375812, G2, ntok=5) "On est toujours réduit a se demander qui
  l'on veut tromper!"; (revue-deux-mondes-1841-q1 @591546, G2,
  ntok=4) "Que puisse ma muse fidèle / A sa gloire à jamais
  s'unir!" — optative "Que puisse..." matrix, "s'unir" its
  complement; (revue-deux-mondes-1841-q1 @1762173, G2, ntok=5)
  "Ils croyaient échapper à cet Être immobile / Qui regarde mourir
  !" — relative clause, "mourir" complement of "regarde"; the "!"
  exclaims the relative clause, not the infinitive phrase.
- A — infinitive-shaped word is not an infinitive (375: 371 auto +
  4 hand): nouns/adjectives/determiners ("votre", "guerre",
  "l'angleterre", "l'avenir", "quatre", "contre"...), finite verb
  forms ("désertèrent", "prépare", "sépare"), OCR garbage
  ("ratt'ermir", "miutaire", "empörter", "moinsd'enadmirer").
- C — infinitive embedded in an exclaimed NP (3): (metternich-
  papiere-v6 @1311599, G2) "de se venger de mon refus d'intervenir
  en Espagne!" — "intervenir" inside the NP "mon refus
  d'intervenir"; (revue-deux-mondes-1841-q3 @1647310, G2) "à
  l'autre frère le devoir d'obéir et de souffrir!" — "le devoir
  d'obéir"; (nesselrode-v8 @333955, G2) "Quelle tristesse de voir
  des Russes / se complaire à dénigrer leur pays !" — the parent's
  cause-C shape recurring ("Quelle" exclamative NP).
- D — terminator belongs to a following quotation/interjection, not
  the infinitive (6): (revue-deux-mondes-1841-q4 @1095085, G2)
  "...de la reconnaître : / / Viens ça, l'ami!" — "!" belongs to
  "Viens ça, l'ami!"; (revue-deux-mondes-1841-q1 @34216, G2) "...ce
  qu'ils doivent faire! / / — A Dieu ne plaise!" — "!" belongs to
  "A Dieu ne plaise!"; (revue-deux-mondes-1841-q4 @1220180, G3-diag
  class, wide) "...de le défendre? / / — Tout est perdu !".

### Nearest near-misses ("/" marks line breaks)

- G1 nearest to an exclamatory "?": (revue-deux-mondes-1841-q1
  @541885, dist=10) "— Mais, n'y a-t-il donc rien à louer? —
  Louer?" — the second "Louer?" is a bare echo-question, not a
  governed exclamatory infinitive; the governed candidate's "?"
  belongs to the interrogative matrix. No "Lui, pour rire ?"
  incredulity shape anywhere in 1,487 "?" candidates.
- G2 nearest: (revue-deux-mondes-1841-q1 @1762173, dist=17) "Qui
  regarde mourir !" (B, relative clause — above); (gutenberg-
  17489-miserables1 @459424, wide, dist=61) "Javert se mit à rire
  de ce rire douloureux qui échappe à une conviction / profonde: /
  / --Oh, sûr!" — "!" belongs to "--Oh, sûr!" (D).
- G3: only one tight candidate (revue-deux-mondes-1841-q1 @680012,
  dist=39) "...pour l'aider à dé- / guiser sa curiosité puérile!"
  — purpose adjunct in the finite matrix (B); the dash/colon the
  pattern keyed on sits earlier in the 120-char segment.
- Wide-band notable recurrences: (revue-deux-mondes-1841-q3
  @1773464, dist=111) "Voyez cependant où la manie de phi- /
  losopher entraîne les poètes : ôter à Moïse son auréole !" —
  the parent's POSITIVE CONTROL (bare exclamatory infinitive
  "ôter...!") re-observed; the candidate word was "l'histoire"
  (A), and the "!" belongs to the BARE infinitive, not a governed
  one. (gutenberg-17489-miserables1 @546038, wide, dist=51) "Voir
  mille objets pour la première et / pour la dernière fois, quoi
  de plus mélancolique et de plus profond!" — likewise the bare-
  infinitive control; candidate "dernière" is an adjective (A).
  (revue-deux-mondes-1841-q3 @2855440, wide, dist=124) "que
  d'intelligence pour vivifier ces études!" — the parent's
  cause-C near-miss recurring; "!" exclaims the "que de" NP (C).

### Positive controls (the widened census detects the shapes)

The bare exclamatory infinitive re-attests inside the widened
windows ("ôter à Moïse son auréole !", "Voir mille objets...!"),
proving the zero is not a detection failure: the widened patterns
fire on exclamatory infinitives when they exist — they find only
the BARE variant, never the governed one.

### Due-diligence checks

- The zero is not an empty-search artifact: 1,874 governed-
  infinitive + terminator candidates exist in the gap windows
  alone; governed infinitives are frequent before "?" and "!";
  they are never themselves the exclaimed element.
- G1's 559 interrogative matrices include rhetorical, echo, and
  indirect questions — the "?"-as-exclamation reading never
  materializes for a governed infinitive phrase.
- G2's 300-char lookback found no long-complement exclamatory
  infinitive ("pour [long] rire ... !" with the phrase exclaimed):
  the wide band holds only finite matrices, exclamative NPs,
  quoted cries, and OCR noise.
- The wider 19c control agrees: 0 genuine in all three gaps
  (G1 175, G2 34, G3 5 candidates).
- G3-diag (81 non-closest matches with no dash/colon, outside the
  bar): 16 tight scanned, 0 genuine — e.g. (revue-deux-mondes-
  1841-q2 @1777398, dist=36) "quelle coutume / De demeurer si tard
  en la rue à causer !" (C, "quelle" NP).

## Per-clause pass/fail

1. >=1 genuine attestation in the widened search re-opens the
   register question: **ANTECEDENT FALSE.** 0 genuine in 1,874
   candidates across 27,657,940 characters — 559 interrogative
   matrices, 375 non-infinitive words, 62 finite-matrix embeddings,
   6 quotation/interjection terminators, 3 exclaimed-NP embeddings
   (tight band); 866 wide-band windows scanned, 0 genuine. The
   register question is NOT re-opened.
2. Confirmed zero closes the recall gap: **CONFIRMED (PASS).** All
   three fenced gap classes are now searched with designs
   structurally disjoint from the parent's: "?"-terminators (never
   keyed), >=3-token prep->infinitive spans (unproducible by the
   parent's regex), and non-closest dash/colon-adjacent matches (the
   parent's closest-match rule discarded them). The recall gap is
   closed.

## Adverses, answered

- None pre-registered ("Adverses: none listed").
- Self-check: no conflict with any standing verdict. The parent
  battery's NULL is undisturbed (this battery was chartered by its
  follow-up #2); the register-level zero now rests on 859 + 1,874 =
  2,733 classified candidates, 0 genuine.

## Verdict: NULL (recall gaps closed; parent register-level zero stands)

Zero genuine governed exclamatory infinitives in the three
previously unsearched window classes (1,874/1,874 candidates
classified or scanned: 1,008 tight classified by hand, 866 wide
scanned). The parent's register-level zero survives the recall
audit: the construction is absent from the 1841 French print
register AND from the wider 19c control, in "!"-windows,
"?"-windows, long-span windows, and dash/colon-adjacent windows
alike. Work regenerates via the follow-ups below.

## Follow-ups (nulls regenerate work)

1. **gov-excl-inf-recall-drama** (P3, gated on the drama ingest —
   coordinates with, does not duplicate, queued gov-excl-inf-drama):
   run the G1/G2/G3 gap searches in the drama corpus (the natural
   habitat of exclamatory infinitives; '?' incredulity is a
   dialogue shape). Bar: >=1 genuine in drama re-opens the
   register question at register level (print-vs-drama split);
   confirmed zero closes the recall gap in both registers.
2. **gov-excl-inf-grammars** (P3): search 19th-c. French grammars,
   rhetorics, and dictionaries of difficulties for CITED examples
   of the governed exclamatory infinitive ("pour rire !" given as
   an example sentence). Bar: >=1 cited example -> contemporaries
   recognized the construction (the print zero is avoidance, not
   absence from the language); confirmed zero -> the construction
   was unrecognized even metalinguistically, hardening the
   register zero.
3. **gov-excl-inf-modern** (P3): run the governed-shape census in a
   modern French corpus. Bar: attests in modern -> the 1841 zero
   is period-specific; zero in modern too -> the construction was
   never productive, reframing "register absence" as
   "construction-marginal".

## Bookkeeping

- Census script:
  code/crowd17/next-token/gov_excl_inf_recall_census.py (re-runnable;
  corpus pinned by name to the parent's exact 18-file set, total
  asserted in-session; outputs gov-excl-inf-recall_census.json).
- Classification harness + record:
  code/crowd17/next-token/gov_excl_inf_recall_classify.py,
  code/crowd17/next-token/gov-excl-inf-recall_classification.json
  (NEVER_INF denylist verbatim, per-candidate cause decisions with
  file@offset, wide-scan log).
- Report: code/crowd17/report_inbox/battery-gov-excl-inf-recall.md
  (this file).
- battery-queue.json: `gov-excl-inf-recall` queued -> verdict/null
  via temp-file + rename (pre-write assert confirmed queued/
  verdictless; JSON re-validated post-write; own entry only;
  claim/bars/evidence/adverses preserved).
- Lock created on start (agent id + UTC timestamp
  2026-10-09T08:33:00Z), deleted on completion. No stale lock for
  this target existed.
- R5005, sealed gates, red-team queue untouched. Every number traces
  to the named corpus files or the census/classification scripts; no
  invented data.
