# Battery report: disloc-governed-excl-epistolary

- Target id: `disloc-governed-excl-epistolary`
- Claim: "targeted correspondence sub-corpus census for governed exclamatory infinitives under dislocated heads"
- Date: 2026-10-09
- Worker: battery worker (subagent 4cf90509-edf1-4602-9c06-b572195cb446)
- Stream: not applicable — corpus census against period correspondence, per target charter. The 1,847-pair repaired parse was not used. R5005, sealed gate instances, and the red-team adjudication queue were not touched.

Terms (ASD-STE100): "dislocation" = a topic moved to the front of the clause, set off by a pause, and resumed by a pronoun. "Governed exclamatory infinitive" = an infinitive led by a preposition (pour, de, à) that carries exclamatory force on its own ("celui-là, pour rire !" = "that one — what a laugh!") — not a plain governed infinitive inside a finite clause.

## Parentage

Follow-up #2 of the NULL `disloc-governed-excl-prose-recall` (2026-10-09): two of its four prose candidates were Nesselrode private letters (anaphoric finite declarative; OCR-artifact "en es!"), and the correspondence sub-corpus had never been censused at battery level. This battery runs the same governed-exclamatory P3 + clitic-tolerant P3b against the correspondence set.

## Corpus gate (byte-pinned by name)

Correspondence sub-corpus, exactly the parent's follow-up #2 list, byte counts asserted at runtime:

- Nesselrode: v7 (521,560 chars), v8 (614,206), v9 (498,642), v10 (556,659)
- Pozzo-di-Borgo: correspondance-v1 (1,001,901)
- Talleyrand: memoires-v1 (926,037)
- Guizot: memoires t1 (769,437), t2 (830,700), t3 (852,681), t5-t6 (1,992,545)
- Metternich: papiere v4 (1,492,023), v6 (1,723,645)
- Total: 12 files, 11,780,036 characters

Exclusions with cause (not hidden):
- `levant-correspondence-1841-p3.txt` (1,714,311 chars) is correspondence but was NOT in the parent's pinned list; a recall pass can cover it (follow-up #1 below).
- Tonic personal heads (moi/toi/lui...) excluded: the queued `personal-tonic-governed-excl-prose` battery owns them; not duplicated here.

## Bar (verbatim, pre-registered before testing)

">=1 genuine re-opens the epistolary register; confirmed zero fences the last live prose hunting ground"

Numbered pass/fail clauses (restated before testing, not modified after):

1. At least one GENUINE governed exclamatory infinitive (a preposition-led infinitive carrying exclamatory illocutionary force on its own, not plain-governed inside a finite clause) under a dislocated head exists in the correspondence corpus. If yes: the epistolary register re-opens (promote).
2. If clause 1's census is a confirmed zero — every candidate classified, false friends excluded with cause — the last live prose hunting ground is fenced (null per §4: zero is an absence, not a refutation).

## Method

1. Read BATTERY-PROTOCOL.md first. Created `code/crowd17/next-token/locks/disloc-governed-excl-epistolary.lock` on start; deleted on completion.
2. Reproducible census script: `code/crowd17/next-token/disloc_governed_excl_epistolary_census.py`. Raw results: `code/crowd17/next-token/disloc-governed-excl-epistolary_census.json`.
3. Search patterns (same P1/P2/P3 taxonomy as the parent):
   - H1 heads (reinforced): `(celui|ceux|celle|celles)[-là/ci]`, `ça[-là/ci]` followed by `[,;:]`
   - H2 heads (plain demonstratives): `cela|ceci|ça` followed by `[,;:]`
   - P2: window (head → next `[!?.]`, ≤180 chars) must contain "!"
   - P3 strict: `(pour|de|d'|à) + infinitive-shaped` ; P3b clitic-tolerant: up to 2 short words between
   - All 4 candidates hand-classified with ±300-char context.
   - Register positive control: "pour/de [inf] !" hits per file.

## Window-level evidence

- 77 reinforced-head hits + 198 plain-demonstrative-head hits → strict + clitic-tolerant P3 candidates: **4**.
- **0 genuine.** All four classified with cause:

**Candidates 1+2 — nesselrode-v8.txt @165979 ("celle-ci") and @165994 ("celle-là"), same window:** "...dans les coteries, comme on critique l'intimité de celle-ci, de celle-là, et comme on a vite fait de faire penser hommes et femmes sur toute chose!" — the two heads sit inside a finite exclamatory "comme…" matrix; "de faire penser" is plain-governed by the idiom "vite fait de". These reproduce the parent battery's candidates 2+3 (same windows, same classification). **Excluded with cause: finite "comme"-matrix exclamation; infinitive governed by "vite fait de", not itself exclamatory.**

**Candidate 3 — nesselrode-v10.txt @494889 ("celle-ci"):** "...en relisant celle-ci, je me suis convaincu qu'il n'y a aucun inconvénient à en donner lecture in extenso ; qu'il y a même nécessité à le faire, puisqu'il en es! fait mention…" — the head is anaphoric to the dispatch inside a finite declarative matrix ("je me suis convaincu que…"); the infinitives are plain-governed by "inconvénient à"/"nécessité à"; the "!" is OCR noise ("en es! fait mention" = "est"). Reproduces the parent battery's candidate 1. **Excluded with cause: finite declarative matrix; no exclamatory infinitive; "!" is an OCR artifact.**

**Candidate 4 — metternich-papiere-v6.txt @860050 ("ceci"):** "...— notez bien ceci, — l'un en dépit et aux dépens de l'autre ! Vive donc le régime représentatif moderne !" — the strict pattern hit "de l'autre" on OCR-corrupted text ("Fautre", "de*pit"). "L'autre" is a pronoun, not an infinitive; there is no infinitive in the window. **Excluded with cause: false pattern hit on OCR-corrupted text; no infinitive present.**

- Register positive control: 77 "pour/de [inf] !" hits across the correspondence files (Metternich v6: 20, v4: 13, Guizot t5-t6: 10, Talleyrand: 8, Nesselrode v7: 8, etc.) — epistolary French HAS governed-exclamatory infinitives; none sits under a dislocated head.

### Per-clause pass/fail

1. ≥1 genuine governed exclamatory infinitive under a dislocated head in correspondence: **FAIL** — confirmed zero. All 4 candidates excluded with cause (2 finite-matrix embeddings — same windows the parent saw — 1 anaphoric-inside-declarative + OCR-noise "!", 1 OCR-corruption false hit).
2. Confirmed zero fences the last live prose hunting ground: **PASS (executed)**.

## Verdict: NULL

The epistolary hunting ground is closed: 0 genuine in 11.78M chars of correspondence (Nesselrode, Pozzo, Talleyrand, Guizot, Metternich). Combined program: prose 30.6M + drama ~2.97M + correspondence 11.78M chars — zero genuine governed-exclamatory infinitives under dislocated heads anywhere. Null per §4 — zero is an absence, not a refutation. No standing verdict contradicted; no red-team verdict touched.

## Follow-ups proposed (nulls regenerate work)

1. `disloc-governed-excl-epistolary-levant` (P3) — run the same census (H1+H2, P2, P3/P3b) on `levant-correspondence-1841-p3.txt` (1,714,311 chars), the correspondence file excluded from this battery's gate. Bar: ≥1 genuine re-opens; confirmed zero closes it.
2. `governed-excl-inf-topic-audit-epistolary` (P3) — classify the 77 register-control "pour/de [inf] !" hits in this correspondence set by topic shape (any topic class). Bar: any genuine with a dislocated topic of any class re-opens the licensor question; confirmed zero generalizes the fence to all heads in correspondence.
3. `disloc-governed-excl-epistolary-pausemarks` (P3) — dash/parenthesis pause-mark variant of the search on the same 12-file correspondence set. Bar: ≥1 genuine re-opens; confirmed zero confirms the zero is not a separator artifact.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-disloc-governed-excl-epistolary.md`
- Census script: `code/crowd17/next-token/disloc_governed_excl_epistolary_census.py`
- Raw results: `code/crowd17/next-token/disloc-governed-excl-epistolary_census.json`
- Lock created on start, deleted on completion (verified).
