# Battery report: disloc-demonstrative-drama-pausemark-recall

- Target id: `disloc-demonstrative-drama-pausemark-recall`
- Claim: "extend the clause-initial demonstrative census to non-comma separators in the drama corpus ('cela !', 'cela --', 'cela...')"
- Date: 2026-10-09
- Worker: battery worker (subagent 6b64641b)
- Stream: not applicable — corpus census against period French drama, per target charter. The 1,847-pair repaired parse was not used. `canonical.py` never used. R5005, sealed gate instances, and the red-team adjudication queue were not touched.

Terms (ASD-STE100): "demonstrative" = cela, ceci, ça (tonic demonstratives). "Non-comma separator" = any pause mark other than a comma: `!`, `?`, `--` / em-dash, `...` / ellipsis, `:` / `;`. "Bare exclamatory infinitive" = an infinitive used as an exclamation with no preposition (de, pour), no "que", no resumptive clitic.

## Bar (verbatim, pre-registered before testing)

">=1 genuine re-opens the shape; confirmed zero confirms the zero is not a separator artifact"

Numbered pass/fail clauses (restated before testing, not modified after):

1. At least one GENUINE dislocated-demonstrative (cela/ceci/ça) + NON-COMMA separator + [bare infinitive] ! attestation exists in the drama corpus. If yes: arm (a) of ce87-1028-role re-opens via the separator avenue.
2. If clause 1's census is a confirmed zero — every candidate classified, false friends excluded with cause — the parent zero is confirmed not to be a separator artifact (null per §4: zero is an absence).

## Parentage

Sibling recall of `disloc-demonstrative-drama` (2026-10-09, NULL) and `disloc-demonstrative-drama-dialogue` (2026-10-09, NULL): both censused demonstrative+COMMA heads in the drama corpus (35 pass-A candidates, 0 genuine). This battery asks whether the zero is a comma-pattern artifact — i.e. whether the shape hides behind `!`, `--`, `...`, `:`/`;` separators. Same 14-file drama corpus as the drama-dialogue battery (2,939,372 chars; hugo-hernani.txt as the one Hernani edition per the one-edition rule).

## Method

1. Read BATTERY-PROTOCOL.md first. Created `locks/disloc-demonstrative-drama-pausemark-recall.lock` on start; deleted on completion.
2. Re-runnable census script: `code/crowd17/next-token/disloc_demonstrative_drama_pausemark_recall_census.py`; raw results: `code/crowd17/next-token/disloc-demonstrative-drama-pausemark-recall_census.json`.
3. Pattern: `\b(cela|ceci|ça|ca)\s*[!?…:;—-…]...` with separator classes `! ? … …: ;` + `--`/em-dash + `...`/ellipsis; keep hits whose 70-char window contains a `!`; first infinitive-shaped word (er/ir/re ending) within 70 chars before the next sentence terminator; ±150/250-char context captured for hand classification.

## Results

- 14 files, 2,939,372 chars. **307 demonstrative + non-comma separator hits**; 120 with a `!` in the 70-char window. All 120 hand-classified.
- **0 genuine.** All 120 excluded with cause:

| # | File @offset | Head | Disposition |
|---|---|---|---|
| 1,4,6,7,8,9,10,15,16,19,20,21,23,24,25,27,29,33,34,35,37,38,41,45,46,48,49,50,51,55,56,66,68,69,72,75,76,77,78,79,80,81,82,84,85,87,88,92,93,95,96,97,98,99,101,102,103,104,105,106,107,109,110,111,112,113,114,115,116,120 | various | `cela ?` / `cela…` / `ça !` etc. | finite clause, question, or exclamation with no infinitive — "Pourquoi cela?", "Comment cela?", "c'est cela!", "qu'est cela?", "cela ne va pas!", "ah ça!" interjections |
| 2,3 | dumas-antony @41854/@41962 | `cela !` | "ne dîtes-vous pas cela !…"; "Dire cela !…" — "cela" is the object of "Dire" (imperative), not a fronted topic |
| 5 | dumas-antony @93804 | `cela…` | "de ce que je vais te dire…" — infinitive governed by "de"; finite frame |
| 13,14,17 | dumas-kean | `ça !` / `ça…` | "ça, moi !" / "ça, lui" — pronoun interjections, no verb |
| 22 | dumas-mariage-louis-xv @13168 | `cela  !` | "C'est cela ! pour que tout le monde vous voie" — finite c'est |
| 28,30,31,32,36,39 | dumas-mariage-louis-xv | `cela!` / `ça  !` / `cela  !` | finite clauses ("c'est monstrueux cela!", "c'est fort mal cela!", "c'est clair comme le jour"), or "ne me dites pas cela !" — finite |
| 42 | hugo-burgraves @62326 | `ceci !` | "Mais portons-lui ceci !" — "ceci" is the direct object of imperative "portons"; no infinitive |
| 43 | hugo-burgraves @71789 | `cela!` | "nous avons souffert tout cela!" — finite passé composé |
| 44 | hugo-hernani @26661 | `ceci !` | "vous me paierez ceci !" — finite |
| **47** | hugo-hernani @122401 | `cela !` | **"Gouverner tout cela ! — Monter, si l'on vous nomme…"** — "cela" is the direct object of the bare exclamatory infinitive "Gouverner" itself (the "!" terminates the infinitive phrase), not a dislocated topic. "Monter" has a conditional "si" clause, not bare. Nearest near-miss; excluded. |
| 52,53,54 | hugo-ruy-blas | `ça !` | "bois-moi ça !" — "ça" is the object of imperative "bois" |
| 58,61,64,65 | labiche-chapeau-de-paille | `ça :` / `ça ?` | "On me répond à ça : « Bah !" quotation intro; "Qui ça ?" / "Où ça ?" questions |
| 83 | labiche-martin @80161 | `cela !` | "je ne te savais pas aussi riche que cela !" — finite |
| 86 | musset @125647 | `cela  !` | "le moyen d'être propre avec cela !" — "cela" governed by "avec"; infinitive governed by "de" |
| 90 | musset @303933 | `cela  ;` | "mettez vos gants neufs… eh, mignon… tra la la !" — no infinitive; interjection |
| 94 | musset @558583 | `cela  !` | "Camille écrit cela !" — finite |
| 100 | scribe-bertrand @54388 | `cela !` | "je voudrais bien voir cela !" — finite "voudrais" |
| 117 | vigny-chatterton @16021 | `ceci  !` | "Songez à ceci ! la raison est…" — "ceci" governed by "à"; finite clause |
| 118 | vigny-chatterton @99965 | `cela!` | "ça ne va pas plus loin que cela! Les divertir…" — "cela" object of "que"; "divertir" governed by "Les" |
| 119 | vigny-chatterton @104702 | `ceci...` | "Je relisais ceci..." — object of "relisais" |

Taxonomy of the 120: ~60 interrogative "cela ?" / "ça ?" with finite verbs or no infinitive; ~40 exclamatory "cela !"/"ça !" with finite verbs; ~10 demonstrative governed by a preceding preposition or verb; 2 demonstrative as object of an infinitive (not a topic: #2 "Dire cela !", #47 "Gouverner tout cela !"); 8 pronoun interjections ("ça, moi !", "ah ça !").

No separator class yields a demonstrative topic + bare exclamatory infinitive: colon (ceci:, ça:) → quotations/interjections; dash/ellipsis → finite clauses; `!` → finite verbs or the demonstrative as object.

## Per-clause pass/fail

1. ≥1 genuine demonstrative + non-comma separator + [bare infinitive] ! in drama: **FAIL (confirmed zero).** 120/120 candidates classified; 0 genuine.
2. Confirmed zero → parent zero is not a separator artifact: **EXECUTED.** Per §4 this is a **null**, not a kill — the shape remains possible-but-unattested in drama with this separator class too.

## Adverses, answered

- None pre-registered.
- Self-check: consistent with the drama-dialogue NULL (comma heads, 0 genuine) and the drama-reissue NULL; the fence now covers comma and non-comma separators in drama full text. No standing or red-team verdict contradicted; §7 intact.

## Verdict: NULL (clause 2 executed)

Confirmed zero: no dislocated-demonstrative + bare-exclamatory-infinitive attestation behind non-comma separators in 2,939,372 characters of 19th-century French drama (~23 plays, one Hernani edition). Arm (a) of ce87-1028-role stays fenced. Work regenerates via the follow-ups below.

## Follow-ups (nulls regenerate work — all verified absent from the queue)

1. **disloc-demonstrative-drama-pausemark-dialogue** (P3): same pausemark census on dialogue-scoped drama text (speaker-header/stage-direction stripped). Bar: ≥1 genuine re-opens at dialogue level; confirmed zero closes the dialogue level too.
2. **disloc-demonstrative-prose-pausemark-recall** (P3): extend the pausemark census to the 27.66M-char prose corpus. Bar: ≥1 genuine re-opens arm (a) in prose via non-comma separators; confirmed zero confirms the prose zero is not a separator artifact either. (Does not duplicate `disloc-reinforced-pausemark-prose-recall`, which is the reinforced-head family.)
3. **arm-a-fence-ratify** (red team): arm (a) is now fenced at six levels — RDM full corpus, RDM quoted dialogue, RDM inversion, drama full-text (both Hernani editions), drama dialogue, drama non-comma separators. Package the fencing reports for red-team ratification.

## Bookkeeping

- Census script: `code/crowd17/next-token/disloc_demonstrative_drama_pausemark_recall_census.py` (re-runnable)
- Raw results: `code/crowd17/next-token/disloc-demonstrative-drama-pausemark-recall_census.json`
- Report: `code/crowd17/report_inbox/battery-disloc-demonstrative-drama-pausemark-recall.md` (this file)
- battery-queue.json: `disloc-demonstrative-drama-pausemark-recall` queued → verdict/null via temp-file + rename (pre-write assert queued/verdictless; JSON re-validated post-write; own entry only; claim/bars/evidence/adverses preserved)
- Lock created on start (agent id + UTC timestamp), deleted on completion.
- R5005, sealed gates, red-team queue untouched. Every number traces to the named corpus files or the census script; no invented data.
