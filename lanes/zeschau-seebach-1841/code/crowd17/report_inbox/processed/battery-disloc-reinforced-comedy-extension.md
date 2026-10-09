# Battery report: disloc-reinforced-comedy-extension

- Target id: `disloc-reinforced-comedy-extension`
- Claim: "extend the reinforced-head census to remaining public-domain Scribe/Labiche comedy on fr.wikisource"
- Date: 2026-10-09
- Worker: battery worker (subagent 56d2ff18-b71d-4909-aaf2-af8d5317c994)
- Stream: not applicable — corpus census against new period French comedy, per target charter. The 1,847-pair repaired parse was not used. R5005, sealed gate instances, and the red-team adjudication queue were not touched.

Terms (ASD-STE100): "dislocation" = a topic moved to the front of the clause, set off by a pause, and resumed by a pronoun ("Celui-là, je le sauverai" = "that one, I will save him"). "Reinforced head" = a demonstrative compound marked with -là or -ci (celui-là, ceux-ci), as opposed to the bare tonic heads (cela, ceci, ça). "Bare exclamatory infinitive" = an infinitive used as an exclamation with no preposition (de, pour), no "que", and no governing verb between the topic and the verb ("Moi, voler !" = "me, steal !").

## Parentage

Follow-up #3 of the NULL `disloc-demonstrative-drama-reinforced` (2026-10-09), which fenced the reinforced-head inventory at the drama-register level: 41 reinforced-head-comma hits → 8 exclamatory candidates in 2,969,582 chars, 0 genuine. Its third proposed follow-up chartered this battery: Scribe contributed the only infinitive-rich near-misses in that census (Le Verre d'eau), and the ingested corpus held only Scribe ×2 / Labiche ×2 — extend to the remaining public-domain Scribe/Labiche comedy on fr.wikisource to close the comedy-register gap.

## Gate / corpus

The pre-registered gate was corpus ingest from fr.wikisource. Six new files were fetched (method: fr.wikisource MediaWiki parse API, transclusions expanded server-side, HTML stripped to plain UTF-8, header-nav chrome trimmed; retrieval 2026-10-09 08:48 UTC; raw API JSON kept in `goals/cipher-hunt-cracking-lanes/hidden_files/comedy-extension-ingest/`):

| file | chars | content |
|---|---|---|
| `scribe-le-savant.txt` | 88,948 | Scribe, *Le Savant* (1832), Dentu Théâtre complet t. XII |
| `scribe-le-lorgnon.txt` | 67,027 | Scribe, *Le Lorgnon* (1833), Dentu Théâtre complet t. XIII |
| `labiche-voyage-perrichon.txt` | 97,394 | Labiche & É. Martin, *Le Voyage de monsieur Perrichon* (1860), Calmann-Lévy t. 2 |
| `labiche-la-cagnotte.txt` | 134,352 | Labiche & Delacour, *La Cagnotte* (1864), Calmann-Lévy t. 5 |
| `labiche-29-degres-ombre.txt` | 34,633 | Labiche, *29 degrés à l'ombre* (1873), Calmann-Lévy t. 7 |
| `labiche-affaire-rue-lourcine.txt` | 43,171 | Labiche, Monnier & Martin, *L'Affaire de la rue de Lourcine* (1857), Calmann-Lévy t. I |
| **Total** | **465,531** | 6 texts, 6 plays |

All public domain (Scribe d. 1861; Labiche d. 1888; co-authors É. Martin d. 1866, Delacour d. 1890, Monnier d. 1869). Source URL, retrieval time/method, and sha256 recorded per file in `code/side-period/corpus/PROVENANCE.md` ("Scribe/Labiche comedy extension" family). Full plays verified: each file carries beginning → act/scen structure → explicit "FIN"/"RIDEAU" ending. "Le Mariage d'argent" on wikisource was a disambiguation page only — excluded, noted as a gap for a later fetch. "Célimare le bien-aimé" and "Les Vivacités du capitaine Tic" have no transcribed full-text page — not silently replaced.

## Bar (verbatim, pre-registered before testing)

"closes the comedy-register gap: >=1 genuine re-opens the family; confirmed zero fences the comedy register"

Numbered pass/fail clauses (restated before testing, not modified after):

1. At least one GENUINE dislocated reinforced-demonstrative head (celui-là / ceux-là / celle-là / celles-là / celui-ci / ceux-ci / celle-ci / celles-ci) + bare exclamatory infinitive exists in the new Scribe/Labiche comedy texts. If yes: the pairing re-opens (promote).
2. If clause 1's census is a confirmed zero — every candidate window classified, false friends excluded with cause — the comedy-register gap is closed and the whole family stays fenced at the comedy-register level too (null per §4: inconclusive as a kill, since zero is an absence).

## Method

1. Read BATTERY-PROTOCOL.md first. Created the lock `code/crowd17/next-token/locks/disloc-reinforced-comedy-extension.lock` on start (no lock, stale or fresh, existed for this id); deleted on completion.
2. Fetched the 6 plays with `code/crowd17/next-token/comedy_extension_ingest.py` (re-runnable; records provenance JSON in `code/crowd17/next-token/comedy_extension_ingest.json`).
3. Ran the census `code/crowd17/next-token/disloc_reinforced_comedy_extension_census.py` — same P1/P2/P3 taxonomy as the parent's `disloc_demonstrative_drama_reinforced_census.py`, corpus switched to the 6 new files. Raw results in `code/crowd17/next-token/disloc-reinforced-comedy-extension_census.json`.
4. Search patterns (verbatim, same as parent):
   - P1 (dislocation): `DEM_REINF\s*[,;:]` where DEM_REINF = `((?:celui|ceux|celle|celles)[-–— ]?(?:l[àa]|ci)|ça[-–— ]?(?:l[àa]|ci))`, case-insensitive.
   - P2 (exclamatory filter): window must contain "!" before its end. The bar construction is a BARE EXCLAMATORY infinitive; a window without "!" cannot instantiate it.
   - P3 (infinitive candidate): `[a-zàâäçéèêëîïôöùûü']{2,}(er|ir|re|oir)` on the window; all candidates classified by hand (regex cannot separate -er infinitives from nouns/adjectives in -er).
5. Sanity check on hit rate: raw reinforced heads without comma = 24 in 465,531 chars (Scribe Savant 4, Scribe Lorgnon 8, Perrichon 3, Cagnotte 6, 29 degrés 1, Lourcine 2) — the regex is not blind; heads exist but almost never in dislocated topic position.

## Window-level evidence

### Census yields

- **2 reinforced-head-comma hits → 0 exclamatory candidates in 465,531 chars → 0 genuine.**

### The two hits (verbatim, both fail P2 — no "!" in window; classified with cause)

1. `scribe-le-savant.txt` @44460 — "…si riche, / que celui-là, j'espère, ne sera pas exigeant sur la / dot." (MADAME DE WURTZB). Finite clause ("ne sera pas exigeant"), parenthetical "j'espère", no infinitive, no exclamation. Excluded.
2. `scribe-le-lorgnon.txt` @5398 — vaudeville couplet ("Air du Piège"): "Intendant vertueux et pur, / Celui-là, fidèle et sensible, / Ne me vole pas, j'en suis sûr." Appositive adjective phrase in verse ("fidèle et sensible"), finite negative clause, no infinitive, no exclamation. Excluded.

No uncapped-window recall gap applies: both hits' windows closed at a sentence-ending mark inside 180 chars; no dash/parenthesis variants were found (P1 covers `[,;:]` and the hyphen/space variants; hyphenated -là forms appear in the raw count).

### Comparison (observed, not claimed)

- Drama register: 41 dem-comma hits / 2,969,582 chars ≈ 1 per 72k; 8 exclamatory candidates, 0 genuine.
- Comedy extension: 2 dem-comma hits / 465,531 chars ≈ 1 per 233k; 0 candidates, 0 genuine.

Reinforced heads occur in comedy dialogue (24 raw heads in 465k chars), but dislocated reinforced topics are rare there (~3× rarer than in the drama register by rate) and none carry the exclamatory-infinitive frame.

## Per-clause pass/fail

- Clause 1 (≥1 genuine in comedy): FAIL — 0 genuine of 2 candidates in 465,531 chars; both classified and excluded with cause. The comedy-register gap is confirmed empty.
- Clause 2 (confirmed zero fences the comedy register): PASS — executed per the pre-registered census; every candidate classified; combined with the prose null (0 genuine in 27.66M chars) and the drama null (0/8 in 2.97M chars), the reinforced-demonstrative + bare-infinitive pairing is now fenced in prose, drama, and comedy registers. Verdict **null** per §4 (zero is an absence — fencing, not kill).

## Verdict

**NULL** — confirmed zero in the comedy register; no standing verdict contradicted; no red-team verdict touched.

## Follow-ups (nulls regenerate work — proposed for the supervisor to queue)

1. **`disloc-reinforced-comedy-recall`** (P2) — recall check on the new register: run pause-mark variants (dash, parenthesis, colon-less) and a sentence-end-uncapped pass over the 6 comedy files to confirm the zero is not a pattern-form artifact. Bar: 0 genuine with variants confirms; any genuine re-opens.
2. **`disloc-comedy-bare-heads-extension`** (P2) — the comedy gap was never covered for the BARE demonstrative inventory (ce/cela/ça): run the `disloc_demonstrative_drama_reissue` P1/P2/P3 taxonomy over the 6 new comedy files. Bar: ≥1 genuine re-opens the bare-head pairing in comedy; confirmed zero fences it.
3. **`reinforced-head-frequency-comedy`** (P3) — test whether dislocated reinforced heads are genuinely rarer in comedy (1/233k vs drama 1/72k) over a larger comedy sample; if the dislocation itself is comedy-absent, the fence has a syntactic not just lexical locus.

## Files

- Report: `code/crowd17/report_inbox/battery-disloc-reinforced-comedy-extension.md` (this file)
- Census script: `code/crowd17/next-token/disloc_reinforced_comedy_extension_census.py`
- Raw census JSON: `code/crowd17/next-token/disloc-reinforced-comedy-extension_census.json`
- Ingest script: `code/crowd17/next-token/comedy_extension_ingest.py`; provenance JSON: `code/crowd17/next-token/comedy_extension_ingest.json`
- Corpus: `code/side-period/corpus/{scribe-le-savant,scribe-le-lorgnon,labiche-voyage-perrichon,labiche-la-cagnotte,labiche-29-degres-ombre,labiche-affaire-rue-lourcine}.txt` + PROVENANCE.md family entry
- Queue: `code/crowd17/next-token/battery-queue.json` — target `disloc-reinforced-comedy-extension` set to status `verdict`/null via temp-file + atomic rename, own entry only, pre-write assert + post-write re-validation
