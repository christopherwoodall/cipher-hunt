# battery-personal-tonic-governed-excl-drama — report

## Bar (verbatim, pre-registered)

">=1 genuine opens the licensor class to tonic pronouns; confirmed zero generalizes the reinforced-head fence to all dislocated topics"

## Numbered clauses

1. **Clause 1 (attest arm):** ≥1 genuine personal tonic pronoun topic + governed exclamatory infinitive in the drama register re-opens the licensor class to tonic pronouns.
2. **Clause 2 (fence arm):** a confirmed zero (after classifying every candidate with cause) generalizes the reinforced-head fence to all dislocated topics at drama-register level.

## Method

- Re-runnable script: `code/crowd17/next-token/personal_tonic_governed_excl_drama_census.py`, raw census JSON alongside.
- P1 (dislocation): `\b(moi|toi|lui|elle|nous|vous|eux)\s*[,;:]` (case-insensitive) — the tonic-pronoun inventory from `disloc_tonic_personal_census.py`.
- Window: from the pronoun through the next `[!?.]`, capped at 180 chars.
- P2 (exclamatory filter): window must contain `!`.
- P3 (governed-infinitive candidate): strict — `\b(?:pour|de|d'|d'|à)\s+[a-z…]{2,}(er|ir|re|oir)\b`; loose (clitic-tolerant, tagged separately) — same with up to 2 intervening short words (catches "de les accueillir"). Manual classification of all candidates follows (regex cannot judge exclamatory illocutionary force or topic status).
- Corpus gate verified on disk: 14 unique plays in `code/side-period/corpus/` (hugo-hernani-1870.txt kept, hugo-hernani.txt excluded — one edition per play): 2,969,582 chars total. All 14 FILES entries present; `hugo-hernani.txt` present-but-excluded as expected.
- Sibling context read before testing: battery-disloc-reinforced-prep-inf-drama (null, 2026-10-09; 0 strict candidates, 1 excluded escapee — Scribe Le Verre d'eau @36952) and battery-disloc-tonic-personal-census (promote, 2026-10-09; 21 genuine bare-shape windows, disjoint positive class).
- Lock: supervisor dispatch lock overwritten on start (6031bdcf-d717-4d13-a318-796eba93f9b5, 2026-10-09T08:51:04Z — not stale, adopted per the dispatch brief), deleted on completion.

## Yield

- 1,986 pronoun-comma hits across 2,969,582 chars (matches the tonic-personal sibling census exactly).
- **29 governed-exclamatory candidates** (15 strict, 14 loose-only), all hand-classified. **0 genuine.**

## Classification (all 29, with cause)

No-true-infinitive false positives (11): [01] burgraves @50171 — "de l'ombre" is a noun ("au seul astre de l'ombre !"); [09] antony @58307 — "pour la vie entière" is a noun phrase; [11] kean @126372 — "à moi qui souffre" (finite "souffre"); [13] tour-de-nesle @127250 — "de mon père" is a noun; [14] tour-de-nesle @127761 — "pour un moment de plaisir" is a noun; [16] bertrand-et-raton @67110 — "des brillants salons de votre père" is a noun; [17] bertrand-et-raton @106359 — "le malheur de votre vie" is a noun; [18] bertrand-et-raton @134823 — "de la tête de Koller !" is an exclaimed NP, no infinitive; [23] verre-d-eau @138561 — "de la dernière importance" is adjectival.

Finite-matrix-governed (15): [02] burgraves @72938 — "de le frapper" governed by "empêchera" ("Rien ne m'empêchera de le frapper!"); [03] burgraves @143260 — "murmurer" governed by causative "a fait"; [04] mariage-louis-xv @60684 — "à me plaindre" governed by "je n'ai point" (vocative "vous, chevalier"); [05] mariage-louis-xv @60717 — same matrix ("je sais que je n'ai point à me plaindre"); [06] antony @7858 — "de cacher" governed by "j'essaierai"; [07] antony @7891 — same matrix; [08] antony @26490 — "à me sauver" governed by "tu auras aidé"; [10] kean @95215 — "à me rendre fou" governed by cleft "c'est" ("vous, Elena" vocative); [12] tour-de-nesle @62103 — "de mourir" governed by "je serais heureuse"; [15] bertrand-et-raton @63227 — "à crier" governed by "je me mets" ("!" terminates interjection "À moi !"); [19] bertrand-et-raton @161965 — "pour me sauver" governed by conditional "marcherait"; [20] verre-d-eau @103586 — "à mourir" governed by "je n'ai plus qu'"; [21] verre-d-eau @126691 — "de vous voir" governed by "je suis heureuse" (vocative "vous, Bolingbroke"); [22] verre-d-eau @131969 — "à exécuter" governed by "sommes prêts"; [25] chatterton @38642 — "de parler" governed by "vient"; [26] musset @143858 — "de tracer" governed by "il t'est facile" (context widened: "Qu'il t'est facile à toi, dans le silence du cabinet, de tracer…"); [28] musset @746377 — "de nous eiîdiabler" governed by "il vous plaît".

Purpose adjuncts of finite clauses (2): [00] hernani-1870 @44016 — "Moi, pour vouloir si peu je ne suis pas si fou !" — "pour vouloir si peu" is the purpose adjunct of the finite matrix "je ne suis pas si fou"; [27] musset @187096 — "pour tirer nos épées" is the purpose adjunct of "nous attendons qu'on nous insulte".

Noun-governed within finite clause (1): [24] poudre-aux-yeux @54243 — "de nous adresser" governed by the noun "la bonté" ("vous avez eu la bonté de nous adresser…").

Note on the nearest near-miss: [19] "moi, pour me sauver qu'il marcherait à la mort !" is a tonic topic followed by a governed infinitive — but the infinitive is governed by the finite conditional "marcherait", and the "!" terminates the finite clause, not the infinitive phrase. Fails the exclamatory-force-on-the-infinitive gate.

## Per-clause pass/fail

1. **Clause 1 (attest arm): FAIL — antecedent false.** Zero genuine tonic-topic + governed exclamatory infinitive windows in 29 candidates over 2,969,582 chars. The "Moi, pour rire !" shape is unattested at battery level in drama.
2. **Clause 2 (fence arm): PASS.** The zero survives manual classification of the full candidate set: 11 regex false positives, 15 finite-matrix-governed (the dominant confound class), 2 purpose adjuncts, 1 noun-governed. No unclassified residue.

## Verdict

**NULL** — confirmed zero, not a refutation (§4: zero is an absence, not a kill). The reinforced-head fence now generalizes to all dislocated topics at drama-register level: reinforced demonstrative heads (battery-disloc-reinforced-prep-inf-drama, null) AND personal tonic pronouns (this battery) both fail to license the governed exclamatory infinitive, even though tonic pronouns DO license the bare shape (21 genuine, battery-disloc-tonic-personal-census, promote) and the register has governed exclamatory infinitives with zero topic (193 "pour/de [inf] !" register controls; "Pour conspirer !" genuine, battery-gov-excl-inf-register-drama, promote).

## Follow-ups proposed (nulls regenerate work)

1. **personal-tonic-governed-excl-prose (P2)** — run the identical P1/P2/P3 taxonomy against the prose corpus (27.66M chars, parent's 18-file set pinned by name): if tonic pronouns license the governed exclamatory infinitive in prose, the fence is register-bound; if zero, the fence generalizes across registers.
2. **personal-tonic-pour-inf-drama (P3)** — restrict the governor to "pour" only (the canonical governed-exclamatory governor; the zero here was partly carried by "de/à" finite-matrix confounds): 0 genuine with a clean "pour"-only search hardens the fence to the governor class.
3. **personal-tonic-governed-excl-recall (P3)** — widen the search window to 400 chars and include "?" termination (recall-gap closure for the one shape this battery's 180-char "!"-gated net could have missed).

## Standing items

- R5005, sealed gates, red-team adjudication queue: untouched.
- Standing §7 values (§7 banked/promoted/kills/splits/holds): untouched, none contradicted.
- No numbers invented: every count traces to the census script output above.
