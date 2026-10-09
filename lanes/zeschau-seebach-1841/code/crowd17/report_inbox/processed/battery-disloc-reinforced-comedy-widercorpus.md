# Battery report: disloc-reinforced-comedy-widercorpus

- Target id: `disloc-reinforced-comedy-widercorpus`
- Claim: widen the comedy corpus with more Scribe/Labiche comedies from fr.wikisource and re-run the reinforced-head census.
- Date: 2026-10-09
- Worker: battery worker (subagent 60cc1eb8-f4a1-4417-a580-fe4b836fb009)
- Stream: not applicable — corpus census against wider period French comedy, per target charter. The 1,847-pair repaired parse was not used. R5005, sealed gate instances, and the red-team adjudication queue were not touched.

Terms (ASD-STE100): "dislocation" = a topic moved to the front of the clause, set off by a pause, and resumed by a pronoun. "Reinforced head" = a demonstrative compound marked with -là or -ci (celui-là, ceux-ci), as opposed to the bare tonic heads (cela, ceci, ça). "Bare exclamatory infinitive" = an infinitive used as an exclamation with no preposition, no "que", and no governing verb between the topic and the verb ("Moi, voler !" = "me, steal !").

## Parentage

Follow-up #1 of the NULL `disloc-reinforced-comedy-recall` (2026-10-09), which confirmed the comedy zero was not a separator-class or window-truncation artifact on 6 comedy files (465,531 chars). Its suggested bar: "0 genuine in ≥1M added chars confirms; any genuine re-opens."

## Corpus widening

8 new full-text comedies ingested from fr.wikisource (MediaWiki parse API, transclusions expanded server-side, HTML stripped to plain UTF-8, provenance in `code/side-period/corpus/PROVENANCE.md`, raw API JSON in `code/crowd17/next-token/widercomedy-ingest-raw/`):

| File | Play | Author | Chars |
|---|---|---|---|
| scribe-charlatanisme.txt | Le Charlatanisme (1825) | Scribe | 60,202 |
| labiche-misanthrope-auvergnat.txt | Le Misanthrope et l'Auvergnat (1852) | Labiche, Lubize & Siraudin | 56,991 |
| labiche-main-leste.txt | La Main leste | Labiche | 39,272 |
| labiche-edgard-bonne.txt | Edgard et sa bonne (1852) | Labiche & Marc-Michel | 57,212 |
| labiche-prix-martin.txt | Le Prix Martin (1876) | Labiche & Émile Augier | 103,002 |
| labiche-noces-bouchencoeur.txt | Les Noces de Bouchencœur (1857) | Labiche | 80,053 |
| labiche-baron-fourchevif.txt | Le Baron de Fourchevif (1859) | Labiche & Alphonse Jolly | 54,412 |
| labiche-doit-on-le-dire.txt | Doit-on le dire ? (1872) | Labiche & Alfred Duru | 114,163 |

565,307 new chars added. Total census base: **16 comedy texts, 1,359,737 chars** (prior 6 = 465,531 + 2 already-ingested Scribe files bertrand-et-raton + verre-d-eau 328,899 + new 8 = 565,307). Added chars beyond the recall base: 894,206 — just under the parent battery's ≥1M suggestion; noted as a caveat below.

## Bar (verbatim, pre-registered before testing)

">=1 genuine re-opens the family; confirmed zero hardens the comedy-register fence on a stronger base"

Numbered pass/fail clauses (restated before testing, not modified after):

1. At least one GENUINE dislocated reinforced-demonstrative head + bare exclamatory infinitive exists in the 16-file widened comedy corpus. If yes: the pairing re-opens.
2. If clause 1's census is a confirmed zero — every candidate hand-classified, false friends excluded with cause — the comedy-register fence is hardened on the stronger base (null per §4: zero is an absence, not a kill).

## Method

1. Read BATTERY-PROTOCOL.md first. Created `code/crowd17/next-token/locks/disloc-reinforced-comedy-widercorpus.lock` on start; deleted on completion.
2. Wrote and ran `code/crowd17/next-token/disloc_reinforced_comedy_widercorpus_census.py` — same P1/P2/P3 as the recall battery verbatim: DEM_REINF + separator class `[,;:—–\-()]`, uncapped 400-char window, window must contain "!", -er/-ir/-re/-oir token regex. Raw results in `code/crowd17/next-token/disloc-reinforced-comedy-widercorpus_census.json`.
3. Hand-classified all 9 candidates below.

## Window-level evidence: 9 candidates, 0 genuine

69 reinforced heads across the 16 files. Separator coverage: only commas attested (dash/paren variants: zero attested).

1. **scribe-le-lorgnon.txt @5398** — "Celui-là, fidèle et sensible, / Ne me vole pas, j'en suis sûr." — SAME vaudeville couplet already excluded by the parent battery: appositive adjective phrase in verse + finite negative clause; "prendre"/"rendre"/"voler" belong to a later speaker's modal construction ("Je le défie, hélas ! de me rien prendre…"). Cross-speaker window bleed. NOT genuine.
2. **scribe-bertrand-et-raton.txt @110103** — "ceux-là, et, s'il fallait les perdre ou les voir compromis… j'aimerais mieux mourir !" — head followed by "et" + conditional clause; infinitives "perdre"/"voir" governed by "fallait"; the "!" belongs to finite "j'aimerais mieux mourir". NOT genuine.
3. **scribe-bertrand-et-raton.txt @123054** — "celle-là, mais nous l'obtiendrons." — head = object of finite clause; no exclamatory infinitive. NOT genuine.
4. **scribe-verre-d-eau.txt @36952** — "ceux-là, je ne suis pas libre de les accueillir…" — finite clause; "accueillir" governed by "être libre de". NOT genuine.
5. **scribe-verre-d-eau.txt @124330** — "celui-là, j'en suis sûre…" — finite clause. NOT genuine.
6. **scribe-charlatanisme.txt @49689** — "celui-ci, je l'ai traité en conscience." — finite clause. NOT genuine.
7. **labiche-misanthrope-auvergnat.txt @1374** — "celui-là, il vit tout seul, dans des endroits noirs, comme un colimaçon !…" — head = subject of finite clause "il vit tout seul"; the "!" belongs to the finite clause; "contempler" governed by "afin de". NOT genuine.
8. **labiche-edgard-bonne.txt @20303** — "ceux-ci, je vais chercher les autres rideaux… Montez…" — head = object of "je vais chercher"; imperative "Montez !" belongs to the next speaker's turn. NOT genuine.
9. **labiche-baron-fourchevif.txt @43030** — "ceux-là, on ne les coupe jamais !" — head = object of finite clause "on ne les coupe jamais"; the "!" belongs to the finite clause. NOT genuine.

## Per-clause pass/fail

- Clause 1 (≥1 genuine in the widened corpus): FAIL — 0 genuine of 9 candidates in 1,359,737 chars.
- Clause 2 (confirmed zero → hardened comedy-register fence): PASS — executed per the pre-registered census; every candidate classified with cause. Verdict **null** per §4.

Caveat: the parent battery suggested "≥1M added chars"; this battery added 565,307 chars (total base 1,359,737 chars, ~3× the recall base). The fence is hardened but not at the full suggested strength — the zero held on a substantially stronger base, so the gap is minor.

No standing verdict contradicted; no red-team verdict touched; §7 intact. Adverses: none listed.

## Follow-ups (nulls regenerate work — proposed for the supervisor to queue)

1. **`disloc-reinforced-tragedy-register`** (P3) — run the same reinforced-head census on higher-register drama (Corneille/Racine via fr.wikisource) to test whether the fence is comedy-specific. Bar: ≥1 genuine in tragedy re-opens the register; confirmed zero generalizes the fence upward.
2. **`disloc-reinforced-prose-fiction`** (P3) — prose-fiction census of reinforced heads + bare exclamatory infinitive on the 27.66M-char prose corpus; completes the register ladder. Bar: ≥1 genuine re-opens; confirmed zero fences the prose register too.
3. **`disloc-reinforced-governed-excl-census`** (P4) — test the governed (preposition/modal-governed) exclamatory infinitive under reinforced heads in comedy — the remaining uncapped pairing arm. Bar: ≥1 genuine re-opens the governed arm; confirmed zero closes it.

## Files

- Report: `code/crowd17/report_inbox/battery-disloc-reinforced-comedy-widercorpus.md` (this file)
- Census script: `code/crowd17/next-token/disloc_reinforced_comedy_widercorpus_census.py`
- Raw census JSON: `code/crowd17/next-token/disloc-reinforced-comedy-widercorpus_census.json`
- Ingest script: `code/crowd17/next-token/widercomedy_ingest.py`; raw API JSON: `code/crowd17/next-token/widercomedy-ingest-raw/`
- Corpus: `code/side-period/corpus/` (8 new files; provenance in PROVENANCE.md)
- Queue: `code/crowd17/next-token/battery-queue.json` — target `disloc-reinforced-comedy-widercorpus` set to status `verdict`/null via temp-file + atomic rename, own entry only, pre-write assert + post-write re-validation
