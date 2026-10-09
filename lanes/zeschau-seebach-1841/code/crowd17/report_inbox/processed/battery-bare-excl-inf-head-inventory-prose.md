# Battery report: bare-excl-inf-head-inventory-prose

- Target id: `bare-excl-inf-head-inventory-prose`
- Claim: a ranked head-class inventory of bare exclamatory infinitives in prose exists (personal tonic pronouns, reinforced heads)
- Date: 2026-10-09
- Worker: battery worker (subagent e4777b3c-e97f-4c39-a05e-d279fca28b41)
- Stream: corpus census per target charter; the 1,847-pair repaired parse not applicable (no cipher data touched). `canonical.py` never used. R5005, sealed gate instances, red-team adjudication queue untouched.

Terms (ASD-STE100): "bare exclamatory infinitive" = an infinitive used as an exclamation with no preposition (de, pour), no "que", no resumptive clitic. "Head" = the topic before the infinitive. "Demonstrative-headed" = a demonstrative (cela/ceci/ça/celui...) as fronted topic. "Reinforced head" = a demonstrative compound marked with -là or -ci (celui-là, ceux-là, celle-là, celles-là, celui-ci, ceux-ci, celle-ci, celles-ci), per the family glossary.

## Parentage

Prose-register counterpart of `bare-excl-inf-head-inventory-drama` (NULL 2026-10-09: 5 genuine tonic-headed, 0 genuine demonstrative-headed of 13 candidates in 2.94M chars of drama). Sibling of `personal-tonic-bare-inf-prose-inventory` (1 genuine tonic-headed bare exclamatory infinitive in 27.66M chars of prose: "Moi, voler!").

## Bar (verbatim, pre-registered before testing)

"A ranked head-class inventory; if demonstratives sit inside a licensed class, the grammatical blocker is weakened"

Numbered pass/fail clauses (restated before testing, not modified after):

1. **C1 (deliverable):** a ranked head-class inventory of bare exclamatory infinitives in the prose corpus, classified by head type (tonic pronoun, demonstrative, reinforced demonstrative, noun, zero, other). PASS iff the discriminating classes are hand-reviewed with stated causes.
2. **C2 (conditional):** if ≥1 GENUINE demonstrative-headed bare exclamatory infinitive is found → the grammatical blocker (demonstratives never head bare exclamatory infinitives) is weakened. If zero → the blocker stands.

## Method

1. Read BATTERY-PROTOCOL.md first. Created `code/crowd17/next-token/locks/bare-excl-inf-head-inventory-prose.lock` on start (2026-10-09T18:17:00Z); no prior lock existed for this id.
2. Corpus VERBATIM the prose batteries' 20-file set (27,656,185 chars, computed in-session — matches the parent prose battery exactly): 17 files in `code/side-period/corpus/`, 3 in lane `data/`.
3. Primary sweep: re-runnable script `code/crowd17/next-token/bare_excl_inf_head_inventory_prose_census.py` — VERBATIM the drama sibling's head-classification method (for each `!`-terminated clause, last-160-char window, infinitive-shaped word in first 40 chars, EXCL-marker filter, head classified DEM_TOPIC/TONIC/NOUN/ZERO/OTHER/DEM_OTHER). Raw results: `code/crowd17/next-token/bare-excl-inf-head-inventory-prose_census.json` (940 pattern candidates).
4. Recall extension (no 160/40 cap): full-clause sweeps for (a) demonstrative + pause + infinitive in `!`-clauses (47 pattern hits), (b) reinforced-head + pause + infinitive (18 pattern hits). All hits hand-reviewed.
5. All discriminating candidates hand-classified against wider context.

## Findings

### Head-type table (27,656,185 chars; 940 pattern-level candidates)

| Head class | Candidates | Review | Genuine |
|---|---|---|---|
| DEM_TOPIC (demonstrative fronted topic) | 1 | hand-reviewed | **0** |
| DEM_OTHER (demonstrative in head, not topic) | 8 | hand-reviewed | **0** |
| TONIC (tonic pronoun) | 8 | hand-reviewed | **0** (capped sweep; see tonic note) |
| REINFORCED (celui-là/ci family) | 0 capped / 18 recall-sweep | hand-reviewed | **0** |
| ZERO (infinitive first) | 231 | recall control | n/a |
| NOUN | 78 | pattern level | n/a |
| OTHER | 614 | pattern level | n/a |

### Demonstrative-involving candidates (all 9, with cause)

**DEM_TOPIC (1):**
1. rdm-q2: "comme cela soupire la douleur et la plainte!" — 'soupire' is a finite verb (3sg present of soupirer), not an infinitive (regex -re false positive); "comme cela" is not a fronted topic anyway. FALSE.

**DEM_OTHER (8):**
1. rdm-q1: "Cela lient du délire !" — OCR garble; 'délire' is a noun (le délire), not an infinitive. FALSE.
2. rdm-q1: "celui-ci, charmé d'être l'objet des caresses du gouverneur..." — 'être' governed by "charmé d'"; the "!" belongs to "généra!" (OCR). FALSE.
3. rdm-q2: "Cela ne vaut pas trois livres sterling!" — 'vaut' finite; 'sterling' noun. FALSE.
4. rdm-q4: "Et cela s'appelait une histoire galante, une aventure romanesque !" — 'histoire' noun. FALSE.
5. metternich-v6: "celle d'avancer d'un pas ferme... Quelle leçon...!" — 'avancer' governed by "d'"; "!" belongs to the next clause. FALSE.
6. talleyrand: "Cest vni, Sire, ... Qu'est devenu ce mauvais sujet de Kotzebue!" — 'Sire' noun (vocative). FALSE.
7. miserables1: "ons cela après dîner... --Ah bah!" — 'dîner' governed by "après"; "!" belongs to "Ah bah!". FALSE.
8. miserables1: "cela venait précisément d'arriver..." — 'arriver' governed by "d'". FALSE.

### Recall sweep (full clause, no cap): 47 demonstrative-pattern hits, 0 genuine

All 47 hand-scanned: the matched "infinitive" is a noun/adjective in -re (autre, votre, étranger, maître, père...), or governed (plaindre, imiter), or the "!" belongs to a different clause, or the demonstrative is an argument (not a topic), or OCR noise. No genuine demonstrative-topic + bare exclamatory infinitive. The one near-shape, rdm-q4 "tout cela mente réflexion. — Attendre !", has a zero topic ("Attendre !" is infinitive-first); the demonstrative sits in the previous sentence.

### Reinforced heads: 0 genuine of 18 recall-sweep hits

celui-là/ceux-là/celle-là/celles-là/celui-ci/ceux-ci/celle-ci/celles-ci + pause + infinitive in `!`-clauses: all 18 are false friends (governed infinitives, finite verbs, nouns in -re, OCR noise, "!" in a different clause). Zero genuine reinforced-head + bare exclamatory infinitive in prose — consistent with the drama result (0/41 reinforced-head windows, full-turn audit).

### Tonic note

My capped sweep's 8 TONIC candidates are all false (imperative government "laisse-moi jouir", governed "vient lui dire", "ne saurait lui passer", optative "Puisse Dieu lui envoyer", causative-causee "lui faire partager son dénûment" — class f: pronoun governed, not a topic; wrong-clause "!"s). The capped method misses the known genuine "Moi, voler!" (rdm-q1 @1331887) because its clause is 261 chars and the 160/40 window cap drops it — a stated recall limitation. The prose inventory battery's uncapped tonic-comma sweep (P1/P2/P3, same corpus) already established the tonic inventory: **exactly 1 genuine** ("Moi, voler!", transitive). Adopted as the standing tonic leg.

## Ranked prose inventory (genuine set)

| Rank | Head class | Genuine (n) | Evidence |
|---|---|---|---|
| 1 | Tonic pronoun | 1 | "Moi, voler!" (rdm-q1 @1331887, transitive voler) — adopted from personal-tonic-bare-inf-prose-inventory |
| 2 | Zero-topic | 0 named | pattern-level only |
| 3 | Noun | 0 named | pattern-level only |
| — | Demonstrative (cela/ceci/ça/celui...) | **0** (9 discriminating candidates + 47 recall hits, all false) | blocker holds |
| — | Reinforced demonstrative (-là/-ci) | **0** (18 recall hits, all false) | blocker holds |

## Per-clause pass/fail

1. **C1 (inventory): PASS** — ranked head-class inventory delivered with byte evidence; all discriminating candidates hand-reviewed with stated causes.
2. **C2 (conditional): antecedent false** — 0 genuine demonstrative-headed bare exclamatory infinitives in prose (0/9 discriminating + 0/47 recall-sweep + 0/18 reinforced-head). The grammatical blocker is NOT weakened; it stands, now hardened in prose as well as drama (drama: 0/13 candidates, 2.94M chars).

## Verdict: NULL

The inventory exists and the blocker holds — the fence is sharpened, not weakened. This mirrors the drama sibling's NULL. Per §4, zero is an absence, not a refutation; the claim's presupposition that reinforced heads license the shape in prose is not supported (0 genuine in either register).

No standing/red-team verdict contradicted; §7 intact. No cipher data touched.

## Follow-ups (null regenerates work; all verified ABSENT from battery-queue.json)

1. `bare-excl-inf-tonic-recall-prose` (P4) — re-run the tonic-pronoun-comma sweep with uncapped clause windows to confirm the prose tonic inventory is complete at 1 genuine (the capped pattern missed "Moi, voler!").
2. `dem-excl-inf-diachronic` (P4) — test demonstrative-headed bare exclamatory infinitives in pre-1841 and post-1841 French; decides whether the fence is period-specific or structural.
3. `reinforced-head-excl-adj-prose` (P4) — do exclamatory non-infinitives pair with reinforced heads in prose (mirrors the drama follow-up); tests whether the gap is infinitive-specific.

## Bookkeeping

- Script: `code/crowd17/next-token/bare_excl_inf_head_inventory_prose_census.py` (re-runnable); raw: `code/crowd17/next-token/bare-excl-inf-head-inventory-prose_census.json`
- Report: `code/crowd17/report_inbox/battery-bare-excl-inf-head-inventory-prose.md`
- Queue: `bare-excl-inf-head-inventory-prose` → `status: verdict`, `result: null`, 2026-10-09 (pre-write assert: queued/verdictless; temp-file + rename; disk re-validated; own entry only; no downgrade)
- Lock created on start (2026-10-09T18:17:00Z, no prior lock), deleted on completion.
- Provenance: period corpus already cached under `code/side-period/corpus/` with PROVENANCE.md; this battery added no new corpus files.
