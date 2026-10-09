# Battery report: personal-tonic-governed-excl-prose

- Target id: `personal-tonic-governed-excl-prose`
- Claim: run the tonic-pronoun + governed-exclamatory-infinitive taxonomy on the 27.66M-char prose corpus
- Date: 2026-10-09
- Stream: corpus census per target charter; the 1,847-pair repaired parse not applicable (no cipher data touched). `canonical.py` never used. R5005, sealed gates, red-team adjudication queue untouched.
- Terms (ASD-STE100): "dislocation" = a topic moved to the front of the clause, set off by a pause, resumed by a pronoun. "Governed exclamatory infinitive" = an infinitive led by a preposition (pour/de/à) and carrying the exclamatory force itself ("Moi, pour rire !"). "Tonic pronoun" = moi/toi/lui/elle/nous/vous/eux.

## Parentage

Prose-register counterpart of `personal-tonic-governed-excl-drama` (NULL 2026-10-09: 29 candidates, 0 genuine in 2.97M chars). That battery proposed exactly this run as its follow-up #1: "if tonic pronouns license the governed exclamatory infinitive in prose, the fence is register-bound; if zero, the fence generalizes across registers."

## Bar (verbatim, pre-registered before testing)

">=1 genuine opens the prose licensor class; confirmed zero generalizes the drama fence to prose."

Numbered pass/fail clauses (restated before testing, not modified after):

1. **Clause 1 (attest):** ≥1 genuine personal-tonic-pronoun topic + governed exclamatory infinitive in 19th-century French prose → the prose licensor class opens to tonic pronouns (promote).
2. **Clause 2 (fence):** a confirmed zero (every candidate classified with cause) → the drama fence generalizes to prose: tonic pronouns do not license the governed exclamatory infinitive in either register (null per §4: zero is an absence, not a kill).

## Method

1. Read BATTERY-PROTOCOL.md first. Created `code/crowd17/next-token/locks/personal-tonic-governed-excl-prose.lock` on start (2026-10-09T08:57Z); no prior lock existed for this id.
2. Re-runnable script: `code/crowd17/next-token/personal_tonic_governed_excl_prose_census.py`; raw results in `code/crowd17/next-token/personal-tonic-governed-excl-prose_census.json`.
3. P1/P2/P3 copied VERBATIM from the drama sibling (`personal_tonic_governed_excl_drama_census.py`, not modified after seeing data):
   - P1: `\b(moi|toi|lui|elle|nous|vous|eux)\s*[,;:]` case-insensitive; window = text from the pronoun through the next `[!?.]`, capped at 180 chars.
   - P2: the window must contain "!" before its end.
   - P3: strict `\b(?:pour|de|d'|d'|à)\s+[a-z…]{2,}(er|ir|re|oir)\b`; loose (clitic-tolerant, tagged separately) = same with up to 2 intervening short words. All candidates hand-classified (regex cannot judge exclamatory illocutionary force or topic status).
4. Corpus VERBATIM from `disloc-demonstrative-prose-clause-initial` (20 files, 27,656,185 chars, computed in-session — matches exactly):
   - 1841-register prose, 17 files, `code/side-period/corpus/`: guizot-memoires t1/t2/t3/t5-t6, nesselrode v7/v8/v9/v10, revue-deux-mondes-1841 q1/q2/q3/q4, metternich-papiere v4/v6, talleyrand-memoires-v1, pozzo-di-borgo-correspondance-v1, levant-correspondence-1841-p3.
   - Wider 19th century, 3 files, `data/`: gutenberg-17489-miserables1.txt, gutenberg-30513-tocqueville-t1.txt, gutenberg-30514-tocqueville-t2.txt.
   - German files and all drama texts excluded with cause (register is French prose; drama has its own battery).

## Yield

4,495 pronoun-comma hits across 27,656,185 chars → **26 governed-exclamatory candidates** (19 strict, 7 loose-only), all hand-classified with 300/500-char wider context. **0 genuine.**

## Classification (all 26, with cause)

Pronoun-governed, no dislocation (5):
- [00] guizot-t1 @221751 — "nous" is the object of "parmi" ("à recueillir parmi nous, à épurer, à fortifier…"); infinitives governed by "tendent"; "!" terminates "à ses devoirs" (relative-clause purpose NP).
- [04] rdm-q1 @599544 — "moi" is the tail of "de moi" ("se sauver de moi"); "Implorer" is bare, not governed; no dislocation.
- [11] rdm-q4 @164600 — "elle" is the tail of "d'elle" (regex apostrophe-boundary artifact); "à la repousser" governed by "prendre plaisir et orgueil à…"; "!" is "Hélas!".
- [12] rdm-q4 @890076 — "pour moi" / "pour vous": both pronouns governed by "pour"; "!" belongs to "quelle joie".
- [13] rdm-q4 @1039717 — "à nous": "il nous serait interdit à nous, France, de seconder le parti modéré!"; "nous" is the argument of "à" in the impersonal "il est interdit à X de Y" construction, not a topic.

Vocative, not dislocated topic (3):
- [05] rdm-q1 @1289464 — "vous, je continue à vous respecter…"; first "vous" vocative; "à vous respecter" governed by finite "continue"; "!" on the finite cleft.
- [06] rdm-q1 @1628920 — "moi, mon père, … aidez-moi à sortir d'ici!"; imperative matrix "aidez-moi"; "à sortir" governed by "aidez".
- [18] metternich-v6 @1080212 — "lui, mais je n'agirai jamais…"; vocative/topic of a finite clause; "de le faire" governed by finite "vient"; "!" on the finite clause.

Finite-matrix-governed (10):
- [02] rdm-q1 @34077 — "Moi, j'apprendrai à faire…"; finite "j'apprendrai"; "!" terminates the finite clause.
- [07] rdm-q2 @416485 — "elle, muette, et moi cherchant à deviner…"; "à deviner" governed by participle "cherchant"; "!" is the quoted "Herr Jésus!".
- [08] rdm-q2 @1165847 — "lui; prêt à franchir le seuil de !"; truncated/OCR fragment; "à franchir" governed by "prêt"; no genuine exclamatory infinitive.
- [09] rdm-q3 @2262867 — "moi, je pleure…"; "de cendre" is a noun-phrase false positive; finite clauses.
- [10] rdm-q3 @2568084 — "nous, ne se hausse point… que nous ayons à nous plaindre…"; "à nous plaindre" governed by finite subjunctive "ayons"; "!" is "à Dieu ne plaise!".
- [15] rdm-q4 @1633288 — "eux; il y avait donc eu d'autres émissaires… envoyés… pour exciter la révolte!"; "pour exciter" governed by participle "envoyés"; "!" on the finite clause.
- [19] metternich-v6 @1092996 — "moi; …il en est autrement de l'avenir…"; "de l'avenir" noun-phrase false positive; finite.
- [20] metternich-v6 @1093065 — duplicate offset of [19], same cause.
- [24] miserables1 @419551 — "lui, il lui jetait…"; "lui" dislocated topic resumed by "lui" of a FINITE clause; "de son cigare" noun-phrase false positive; "!" is the quoted "Que tu es laide!".
- [25] miserables1 @460876 — "Lui, il n'a pas l'air de comprendre…"; topic of a finite clause; "de comprendre" governed by the noun "l'air"; "!" is the quoted "Je suis Champmathieu…!".

Noun-governed within finite clause (4):
- [16] metternich-v4 @50484 — "Moi; tenant la paix… et connaissant seul les moyens de rassurer, — moi au lit!"; "de rassurer" governed by "les moyens"; "!" is "moi au lit!".
- [17] metternich-v6 @188673 — "moi, pauvre chancelier, forcé de faire mouvoir…"; "de faire" governed by participle "forcé"; "!" terminates the participial clause.
- [21] metternich-v6 @1307068 — "lui, à sa manière de voir et de juger que cela semblerait être uniquement du!"; "de voir / de juger" governed by "manière"; "!" is the "que + conditional" exclamative finite clause.
- [22] metternich-v6 @1395760 — "moi, à raison à l'égard de la question de savoir…"; "de savoir" governed by "la question"; "!" is "oui ou non!".

Purpose adjunct of a finite matrix (1):
- [01] guizot-t2 @282484 — "lui, pour prendre la parole: «Ici, d'Argout!»"; purpose adjunct with colon; "!" belongs to the downstream quote, not the infinitive.

Finite optative / exclaimed NP, not infinitive (2):
- [03] rdm-q1 @112215 — "elle, que vous tenez dans la vôtre, j'aurai pour ceci votre tête (2)!"; "pour ceci votre" false -re positive (NP "votre tête"); finite "j'aurai".
- [23] talleyrand @649477 — "elle, L'ancienne gloire…"; "de quatre" noun-phrase false positive ("action de quatre heures"); "!" is the exclaimed NP "la bataille d'Iéna!".

P3 false positive, bare shape out of scope (1):
- [14] rdm-q4 @1248948 — "vous, au bout de votre carrière, rencontrer moins d'épines…!"; "de votre" is a noun-phrase false positive; the window's infinitive "rencontrer" is BARE. This is the bare-shape positive class (sibling battery disloc-tonic-personal-census), not governed; out of this battery's bar.

No unclassified residue. Dominant confound class: finite-matrix-governed (10) and noun-governed (4) — the same taxonomy as the drama sibling.

## Per-clause pass/fail

1. **Clause 1 (attest): FAIL.** Zero genuine tonic-topic + governed exclamatory infinitive windows in 26 candidates over 27,656,185 chars of prose. The "Moi, pour rire !" shape is unattested at battery level in prose, matching drama.
2. **Clause 2 (fence): EXECUTED.** The zero survives manual classification of the full candidate set: 5 pronoun-governed non-dislocations, 3 vocatives, 10 finite-matrix-governed, 4 noun-governed, 1 purpose adjunct, 2 finite-optative/exclaimed-NP false positives, 1 bare-shape false positive. Per §4 this is a **null**, not a kill — zero is an absence, not a refutation.

## Verdict: NULL

The drama fence generalizes to prose: tonic-pronoun topics do not license the governed exclamatory infinitive in either register. Reinforced demonstrative heads (drama + prose batteries, null) and personal tonic pronouns (drama sibling + this battery) now all fail to license it, even though tonic pronouns DO license the bare shape in drama (21 genuine, disloc-tonic-personal-census promote) and a prose bare-shape window surfaces here ([14], out of bar).

## Follow-ups (nulls regenerate work)

1. **personal-tonic-bare-inf-prose-inventory** (P3) — ranked head-class inventory of BARE exclamatory infinitives under tonic-pronoun topics in the 27.66M-char prose corpus; sibling battery disloc-tonic-personal-census was drama-scope, and window [14] here shows the bare shape lives in prose too.
2. **personal-tonic-pour-only-prose** (P3) — restrict the governor to "pour" only (the canonical governed-exclamatory governor) to cut the finite-matrix confounds that carried most of this zero.
3. **personal-tonic-governed-excl-prose-window-widen** (P4) — 400-char window + "?" termination recall-gap closure for the 180-char "!"-gated net (mirrors the drama sibling's follow-up #3).

## Adverses, answered

- None pre-registered ("Adverses: None").
- Self-check: no standing or red-team verdict contradicted; §7 untouched. No value named, nothing adjudicated.
- Corpus note: metternich-papiere v4/v6 contain German-language passages; the set is the parent's pinned 20-file prose corpus (kept verbatim for comparability) and no candidate classified above depended on German text.

## Bookkeeping

- Lock: `code/crowd17/next-token/locks/personal-tonic-governed-excl-prose.lock` created on start, deleted on completion.
- Census script: `code/crowd17/next-token/personal_tonic_governed_excl_prose_census.py`; raw JSON: `code/crowd17/next-token/personal-tonic-governed-excl-prose_census.json`.
- `battery-queue.json` updated via temp-file + rename (own entry only; no downgrade).
