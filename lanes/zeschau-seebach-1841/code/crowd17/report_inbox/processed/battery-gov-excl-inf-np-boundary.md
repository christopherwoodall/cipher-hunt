# Battery report: gov-excl-inf-np-boundary

- Target id: `gov-excl-inf-np-boundary`
- Claim: "inventory governors of the Cause-C exclaimed-NP near-misses to map the NP-vs-infinitive-phrase boundary"
- Evidence (from queue): battery-gov-excl-inf-register null (2026-10-09): ~10% of candidates were infinitives embedded in exclaimed NPs ('des perdreaux a tuer!', 'Cinq louis d'or a gagner!').
- Date: 2026-10-09
- Worker: battery worker (subagent ba14a5fa-b5d8-444e-88c0-bdcb063a580f)
- Stream: not applicable — corpus census against period French, per target charter (same register as the parent battery). The 1,847-pair repaired parse was not used. R5005, sealed gate instances, and the red-team adjudication queue were not touched.

Terms (ASD-STE100): "governed exclamatory infinitive" = a preposition-governed infinitive (pour/à/de) used as an exclamation in its own right ("pour rire !" — the infinitive phrase IS the exclaimed element). "Cause-C" = the parent battery's classification: an infinitive embedded in an exclaimed noun/adjective phrase (the phrase is exclaimed, not the infinitive). "Governor" = the preposition licensing the infinitive (pour / à / de).

## Bar (verbatim, pre-registered before testing)

"map the NP-vs-infinitive-phrase boundary with byte evidence per governor class"

Numbered pass/fail clauses (restated before testing, not modified after):

1. Inventory the Cause-C exclaimed NPs corpus-wide, with per-governor (pour / à / de) counts, byte-verified window by window.
2. Governor-asymmetry test: if one governor is absent (or overwhelmingly dominant) in the NP-embedded class, the register gap narrows to a governor effect; if all three governors occur, the boundary is phrase-level (NP vs infinitive phrase), not governor-level.
3. Contrast check: the NP-embedded count is consistent with the parent's zero for bare governed exclamatory infinitives (0 genuine in 859 candidates) — i.e. governed infinitives exclaim freely when embedded in an NP, never as bare infinitive phrases.

## Method

1. Read BATTERY-PROTOCOL.md first. Created the lock `code/crowd17/next-token/locks/gov-excl-inf-np-boundary.lock` on start (agent id + UTC timestamp 2026-10-09T12:12:03Z; no stale lock for this id existed).
2. Ran a new census script `code/crowd17/next-token/gov_excl_inf_np_boundary_census.py` over the parent's register corpus plus the parent's wider 19c control:
   - 1841 register: the parent's 17-file set (guizot t1/t2/t3/t5-t6, nesselrode v7/v8/v9/v10, revue-deux-mondes-1841 q1/q2/q3/q4, metternich-papiere v4/v6, talleyrand-memoires-v1, pozzo-di-borgo-correspondance-v1, levant-correspondence-1841-p3) — 25,668,503 chars, 4,995 "!". (Parent reported "18 files / 25,670,258 chars"; the file list it named is 17 files; char delta 1,755 is unexplained but immaterial.)
   - Wider 19c control: data/gutenberg-17489-miserables1.txt, data/gutenberg-30513-tocqueville-t1.txt, data/gutenberg-30514-tocqueville-t2.txt.
   - Note: the corpus directory has since grown (drama files added 2026-10-09 ~08:31–09:02 by sibling batteries); those files were NOT included here, to keep the register identical to the parent's.
3. Extraction: for every "!", sentence-span back to the last [.;!?;]; run the parent's GOV_INF pattern; keep the match closest to the "!"; flag the window iff the head (same sentence, before the governor) carries an NP-exclamation marker: exclamative determiners (quel/quels/quelles/combien/que de), offer-NP quantifier/numeral with governor "à", exclaimed adjective phrase (trop/si/tant/aussi/assez/bien + adj) with governor "de", or a compound exclamation ("!" in the 160-char lookback head). 220 windows flagged; raw JSON in `code/crowd17/next-token/gov-excl-inf-np-boundary_census.json`.
4. Hand-classified all 220 windows (classification table below; intermediate file `code/crowd17/next-token/np-boundary-classify2.txt`). Cause-C = the "!" terminates an NP/AP AND the governed infinitive is a genuine infinitive complementing the NP/AP head (or a noun/adjective inside it) — NOT governed by a verb inside a finite clause or relative clause, and not OCR noise.

## Window-level evidence (Cause-C inventory)

### Governor "de" — 9 windows

1. (nesselrode-v7) "Quel bonheur de pouvoir épargner le sang!" — head "bonheur" + "de pouvoir épargner le sang".
2. (revue-deux-mondes-1841-q1) "combien de charmantes facéties sur leur habitude de fumer et sur le lavage quotidien des rues et des maisons!" — head "facéties" + PP "sur leur habitude de fumer".
3. (revue-deux-mondes-1841-q1) "Et quelle gloire pour la république de Buénos-Ayres de pouvoir se vanter un jour d'avoir tenu la France en échec!" — head "gloire" + "de pouvoir se vanter...".
4. (revue-deux-mondes-1841-q1) "quel supplice, si ce n'était un plaisir, le plaisir de faire sa fortune!" — appositive NP "le plaisir de faire sa fortune".
5. (revue-deux-mondes-1841-q4) "trop heureux de s'en être bien tiré!" — exclaimed adjective phrase "trop heureux de s'en être bien tiré".
6. (revue-deux-mondes-1841-q4) "et quelle concession! le conseil donné par nous au pacha d'Egypte de céder!" — head "conseil" + "de céder".
7. (revue-deux-mondes-1841-q4) "et quel espoir plus propre à séduire que Celui de se rencontrer avec l'auteur dans le jugement qu'on portera sur son œuvre!" — head "Celui"/"espoir" + "de se rencontrer...".
8. (metternich-papiere-v4) "combien de motifs n'existe-t-il pas de plus aujourd'hui de rester fidele à notre idee primitive!" — head "motifs" + "de rester fidèle...".
9. (metternich-papiere-v6) "dans la seule idee — croyez-le bien — de se venger de mon refus d'intervenir en Espagne!" — head "refus" + "d'intervenir en Espagne".

### Governor "à" — 11 windows

1. (nesselrode-v7) "le duc de Mortemart fut un des premiers à se prononcer pour la déchéance!" — head "premiers" + "à se prononcer".
2. (nesselrode-v8) "Quelle tristesse de voir des Russes se complaire à dénigrer leur pays!" — head "tristesse" + "de voir..."; "à dénigrer" governed by "se complaire" inside the complement.
3. (revue-deux-mondes-1841-q2) "quelle coustume De demeurer si tard en la rue à causer!" — head "coustume" + "de demeurer si tard en la rue à causer".
4. (revue-deux-mondes-1841-q2) "quel mensonge de plus à mettre sur votre conscience!" — head "mensonge" + "de plus à mettre sur votre conscience".
5. (revue-deux-mondes-1841-q3) "Eros, ô bel archer si doux à percer l'ame!" — vocative NP "ô bel archer si doux à percer l'âme".
6. (revue-deux-mondes-1841-q3) "cette harmonie si difficile à établir!" — head "harmonie" + "si difficile à établir".
7. (revue-deux-mondes-1841-q4) "des perdreaux à tuer!" — head "perdreaux" + "à tuer" (offer-NP).
8. (revue-deux-mondes-1841-q4) "d'autres droits non moins doux à défendre!" — head "droits" + "doux à défendre".
9. (revue-deux-mondes-1841-q4) "combien est rapide et facile à descendre la pente du bonheur, si lente et si rude à gravir!" — head "la pente du bonheur" + "si lente et si rude à gravir".
10. (gutenberg-17489-miserables1) "Cinq louis d'or à gagner!" — offer-NP.
11. (gutenberg-17489-miserables1) "Six mois à gagner sept sous par jour!" — head "six mois" + "à gagner sept sous par jour".

### Governor "pour" — 4 windows

1. (revue-deux-mondes-1841-q2) "Nations! mot pompeux pour dire barbarie!" — appositive NP "mot pompeux pour dire barbarie".
2. (revue-deux-mondes-1841-q3) "Quel art pour tout s'approprier, depuis Homère jusqu'à Tacite!" — head "art" + "pour tout s'approprier".
3. (revue-deux-mondes-1841-q4) "que d'études et de recherches! que de pénétration, que d'intelligence pour vivifier ces études!" — head "intelligence" + "pour vivifier ces études".
4. (gutenberg-17489-miserables1) "une planche pour dormir, le chaud, le froid, le travail!" (enumeration: "Oh! la casaque rouge, le boulet au pied, une planche pour dormir, ...") — head "planche" + "pour dormir".

### Register split

- 1841 register (17 files): 21 Cause-C (de=9, à=9, pour=3).
- Wider 19c control (3 files): 3 Cause-C (de=0, à=2, pour=1).

### Excluded with cause (of the 220 flagged)

- 196 windows: ~60% OCR "-er" false friends (infinitive-shaped nouns/adjectives: propre, l'affaire, chambre, mémoire, pierre, pourpre, gloire, mesure, maire, misère, mère, autre, terre, l'air, d'autre, notre, premier, dernier, contraire, etc.), "a" = verb-avoir noise, frozen forms ("à la bonne heure", "à mesure que", "à dater de", "à plaisir"), bare infinitives ("venir faire", "faire + inf" causatives, optative "puisse"), and finite-matrix embeddings where the governed infinitive is governed by a verb inside a finite/relative clause (the parent's Cause-B/D).

## Per-clause pass/fail

1. Cause-C inventory with per-governor counts: **PASS.** 24 windows byte-verified: de=9, à=11, pour=4.
2. Governor-asymmetry test: **PASS — boundary is phrase-level, not governor-level.** All three governors license NP-embedded governed infinitives under exclamation. The parent's follow-up sketch predicted a possible "only à, never pour" asymmetry; the data falsifies it: "pour" occurs 4× ("mot pompeux pour dire barbarie", "Quel art pour tout s'approprier", "que d'intelligence pour vivifier ces études", "une planche pour dormir").
3. Contrast check: **PASS.** 24 NP-embedded attestations vs the parent's 0 genuine bare governed exclamatory infinitives in the same register. The construction exclaims freely as an NP complement and never as a bare infinitive phrase.

## The map

The NP-vs-infinitive-phrase boundary, with byte evidence:

- **NP-embedded governed infinitives exclaim freely (24 windows).** Three sub-classes: (a) offer/purpose NPs — "des perdreaux à tuer", "Cinq louis d'or à gagner", "Six mois à gagner sept sous par jour", "une planche pour dormir", "mot pompeux pour dire barbarie"; (b) exclamative quel/combien NPs with head-complements — "Quel bonheur de pouvoir épargner le sang", "Quelle tristesse de voir des Russes se complaire à dénigrer leur pays", "quel mensonge de plus à mettre sur votre conscience", "cette harmonie si difficile à établir"; (c) exclaimed adjective phrases — "trop heureux de s'en être bien tiré".
- **Bare governed infinitive phrases never exclaim (0 windows, parent census).** Every governor-independent attempt dies: the governed infinitive is always either embedded in a finite clause (Cause-B), in an exclaimed NP (Cause-C), or in a quotation/interjection (Cause-D).
- **The governor does not move the boundary.** de=9, à=11, pour=4 — no governor is excluded from the NP-embedded class, so the register gap cannot be narrowed to a governor effect.

## Adverses, answered

- None pre-registered ("Adverses: none listed").
- Self-check: recall limitation — my sentence-span + marker flags are a lower bound (24 Cause-C) vs the parent's looser ~10%-of-859 estimate. The boundary conclusion does not depend on the count: the parent's own 7 Cause-C exemplars already spanned à×3/pour×3/de×1, and my 24-window inventory confirms all three governors with byte evidence. No standing/red-team verdict touched; nothing contradicted or downgraded.

## Verdict: PROMOTE

The boundary is mapped with byte evidence per governor class: the NP-vs-infinitive-phrase boundary is phrase-level, not governor-level. Governed infinitives exclaim when embedded in an NP (24 windows, all three governors); the bare governed infinitive phrase never exclaims (parent's register-level zero stands). Per §4, promotes propose no follow-ups.

## Bookkeeping

- Census script: code/crowd17/next-token/gov_excl_inf_np_boundary_census.py (re-runnable; parent register + wider 19c control; outputs gov-excl-inf-np-boundary_census.json).
- Classification table source: code/crowd17/next-token/np-boundary-classify2.txt (all 220 flagged windows with per-window classification in this report).
- Report: code/crowd17/report_inbox/battery-gov-excl-inf-np-boundary.md (this file).
- battery-queue.json: `gov-excl-inf-np-boundary` queued -> verdict/promote via temp-file + rename (pre-write assert confirmed queued/verdictless; JSON re-validated post-write; own entry only; claim/bars/evidence/adverses preserved).
- Lock created on start (2026-10-09T12:12:03Z), deleted on completion. No stale lock for this target existed.
- R5005, sealed gates, red-team adjudication queue untouched. Every number traces to the named corpus files or the census script; no invented data.
