# Battery report: disloc-reinforced-verse-vs-prose-comedy

- Target id: `disloc-reinforced-verse-vs-prose-comedy`
- Claim: "compare sung-verse couplets vs spoken dialogue windows within the comedy register for reinforced-head exclamatory infinitives"
- Date: 2026-10-09
- Worker: battery worker (subagent 3be4f2fe-cf1a-41c6-b32e-ca9e6e4d2f88)
- Stream: not applicable — corpus census against period French comedy, per target charter. The 1,847-pair repaired parse was not used. `canonical.py` never touched. R5005, sealed gate instances, and the red-team adjudication queue were not touched.

Terms (ASD-STE100): "reinforced head" = a demonstrative compound with -là or -ci (celui-là, celle-ci...). "Bare exclamatory infinitive" = infinitive used as exclamation with no preposition, "que", or governing verb between topic and verb. "Verse" = sung vaudeville couplets. "Dialogue" = spoken prose dialogue.

## Parentage

Follow-up #2 of the NULL `disloc-reinforced-comedy-recall` (2026-10-09). The parent's only recall candidate was a vaudeville couplet with cross-speaker bleed ("Celui-là, fidèle et sensible..." in Scribe's Le Lorgnon, Air du Piège); this battery tests whether the reinforced-head census behaves differently in sung verse vs spoken dialogue within the comedy register.

## Bar (verbatim, pre-registered before testing)

">=1 genuine in either sub-register locates the locus; confirmed zero in both generalizes the fence"

Numbered pass/fail clauses (restated before testing, not modified after):

1. At least one GENUINE dislocated reinforced-demonstrative head + bare exclamatory infinitive exists in the verse (sung-couplet) sub-register. If yes: the locus is verse.
2. At least one GENUINE dislocated reinforced-demonstrative head + bare exclamatory infinitive exists in the dialogue (spoken-prose) sub-register. If yes: the locus is dialogue.
3. If clauses 1–2 are a confirmed zero in both sub-registers — every candidate classified, false friends excluded with cause — the reinforced-head fence generalizes across the whole comedy register (null per §4: zero is an absence, not a kill).

## Method

1. Read BATTERY-PROTOCOL.md first. Created `locks/disloc-reinforced-verse-vs-prose-comedy.lock` on start; deleted on completion.
2. Corpus: all 18 comedy files in `code/side-period/corpus/` (12 labiche-*, 6 scribe-*), 1,565,346 chars — the 6 files of the recall parent plus the 8 wider-corpus files plus 4 already-present comedy files (chapeau-de-paille, bertrand-et-raton, verre-d-eau, poudre-aux-yeux).
3. Verse/dialogue partition: a verse region starts at a line matching `^(AIR|Air)\b` (vaudeville tune marker, 122 markers) and ends at the next ALL-CAPS speaker header, a "Scène N." line, or EOF. 362,408 chars verse vs ~1.2M chars dialogue. Stated limitation: tails of long vaudeville songs can bleed a few spoken lines (e.g. chapeau-de-paille's 306-line finale song); every candidate was hand-checked, so partition error cannot create a false genuine.
4. Ran `code/crowd17/next-token/disloc_reinforced_verse_vs_prose_comedy_census.py` (re-runnable): P1 = DEM_REINF head, P2 = one of `[,;:—–\-()]` in the 400-char window, P3 = "!" in window, P4 = -er/-ir/-re/-oir token in window. Raw results: `code/crowd17/next-token/disloc-reinforced-verse-vs-prose-comedy_census.json`.
5. Hand-classified every candidate in wider context.

## Window-level evidence

76 reinforced heads corpus-wide → 61 candidates (P1–P4) → **0 genuine**.

### Verse sub-register: 4 candidates, 0 genuine

1. `scribe-le-lorgnon.txt` @5398 — "Celui-là, fidèle et sensible, / Ne me vole pas, j'en suis sûr." The parent's known couplet: appositive adjective phrase + finite negative clause. Infinitives in window belong to a later speaker's verse. Excluded with cause: cross-speaker bleed; head's clause finite.
2. `labiche-edgard-bonne.txt` @20303 — "ceux-ci, je vais chercher les autres rideaux… Montez…" Finite matrix "je vais chercher"; the "!" belongs to imperatives ("Montez… !"). Excluded: no exclamatory infinitive.
3. `labiche-misanthrope-auvergnat.txt` @54515 — "celle-là !" Bare exclamatory head alone; no infinitive under the head. Excluded: no infinitive present.
4. `labiche-noces-bouchencoeur.txt` @37704 — "celles-là?... (haut) Qui demandez-vous?..." Interrogative with finite question. Excluded: not exclamatory infinitive.

### Dialogue sub-register: 57 candidates, 0 genuine

Classified with cause; no unclassified residue. Confound classes:

- **Exclamatory head, no dislocation (dominant, ~25):** "celui-là !…", "celle-ci !…", "ceux-là ?" — the head is itself the exclamation; no pause-separated topic, no infinitive (e.g. labiche-29-degres-ombre @30887, labiche-affaire-rue-lourcine @12503/@39634, labiche-baron-fourchevif @37520, scribe-verre-d-eau @81502/@102926).
- **Dislocation with finite matrix (~15):** head + comma + finite clause, "!" on a finite verb — e.g. labiche-baron-fourchevif @43030 "ceux-là, on ne les coupe jamais !"; scribe-verre-d-eau @36952 "ceux-là, je ne suis pas libre de les accueillir…"; labiche-voyage-perrichon @37755 "celle-là !… Je comptais m'en amuser…".
- **Dislocation with copula/predication (~8):** "celui-ci, je l'ai traité en conscience" (scribe-charlatanisme @49689), "celui-là est de bonne foi" (@53071), "Celle-là est à vous" (scribe-le-savant @56303).
- **Didascalie separators (~5):** parenthesis/semicolon/colon are stage directions, not pauses — e.g. labiche-la-cagnotte @70528 "Celui-là est idiot… (Haut.)"; labiche-martin-poudre-aux-yeux @14243 "celle-ci coiffe sa fille… (À Alexandrine.)".
- **Interrogative heads (~4):** "celui-là ?" / "ceux-là ?" with finite answers.
- **Nearest structural near-miss:** scribe-bertrand-et-raton @110103 "ceux-là, et, s'il fallait les perdre ou les voir compromis… j'aimerais mieux mourir !" — dislocated head, but the infinitives are conditional subjects of "fallait" inside a finite matrix; excluded with cause.

No standing or red-team verdict contradicted; §7 intact.

## Per-clause pass/fail

- Clause 1 (≥1 genuine in verse): FAIL — 0 genuine of 4 candidates in 362,408 verse chars.
- Clause 2 (≥1 genuine in dialogue): FAIL — 0 genuine of 57 candidates in ~1.2M dialogue chars.
- Clause 3 (confirmed zero in both → fence generalizes): EXECUTED — every candidate classified; the reinforced-head + bare exclamatory infinitive fence holds in sung verse and spoken dialogue alike. Verdict **null** per §4 (zero is an absence).

## Follow-ups (nulls regenerate work — proposed for the supervisor to queue; all verified absent)

1. **`disloc-reinforced-tragedy-register`** (P3) — same verse/dialogue census on Corneille/Racine tragedy via fr.wikisource; tests whether the fence is comedy-specific.
2. **`disloc-reinforced-verse-drama`** (P3) — run the verse/dialogue partition on the ingested drama corpus (Hugo's Hernani is verse drama); the sub-register split was only censused in comedy.
3. **`disloc-reinforced-prose-fiction`** (P3) — reinforced-head census on the 27.66M-char prose-fiction corpus; completes the register ladder.

## Files

- Report: `code/crowd17/report_inbox/battery-disloc-reinforced-verse-vs-prose-comedy.md` (this file)
- Census script: `code/crowd17/next-token/disloc_reinforced_verse_vs_prose_comedy_census.py`
- Raw census JSON: `code/crowd17/next-token/disloc-reinforced-verse-vs-prose-comedy_census.json`
- Queue: `code/crowd17/next-token/battery-queue.json` — target `disloc-reinforced-verse-vs-prose-comedy` set to status `verdict`/null via temp-file + atomic rename, own entry only, pre-write assert + post-write re-validation
