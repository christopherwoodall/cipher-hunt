# Battery verdict — disloc-demonstrative-inversion-drama

- Target: `disloc-demonstrative-inversion-drama`
- Verdict: **NULL** (fence)
- Date: 2026-10-09 (UTC)
- Worker session: 648e78fb-6e89-449a-b957-e9d7a4dac85c

## Claim under test

Postposed demonstratives ('[bare inf] !, cela/ceci/ça', e.g. "Voler, cela !") occur in drama-corpus dialogue.

## Bars (verbatim)

1. Census postposed demonstratives ('[bare inf] !, cela/ceci/ça', e.g. 'Voler, cela !') in the drama-corpus dialogue.
2. ≥1 genuine postposed-demonstrative + bare exclamatory infinitive re-opens.
3. Confirmed zero fences.

## Method

- Corpus: the same 14-play French drama set as the sibling target `disloc-demonstrative-drama-dialogue` (Hugo, Dumas, Vigny, Musset, Scribe, Labiche), one edition per play (`hugo-hernani.txt` is the Hetzel 1889 edition; `hugo-hernani-1870.txt` excluded as a duplicate edition).
- Scripts: `code/crowd17/next-token/disloc_demonstrative_inversion_drama_census.py`, with the inversion patterns verbatim from the parent census `disloc_demonstrative_inversion_census.py`:
  - INF = `\b[a-zàâäçéèêëîïôöùûü']{2,}(er|ir|re|oir)\b`
  - DEM_POST = `\b(cela|ceci|ça|ca|cel[àa]|cec[iy])\b`
  - Candidate = a demonstrative starting after an infinitive within 100 chars, with "!" within 20 chars after the demonstrative; deduplicated by (file, offset).
- Output: `code/crowd17/next-token/disloc-demonstrative-inversion-drama_census.json` — **490 unique candidates**.
- Because the plays use speaker-header formatting rather than quotation marks, the census ran over the full play text; every candidate was hand-classified for dialogue vs non-dialogue status per the sibling's method. A confirmed zero over the full text implies a confirmed zero in dialogue.
- All 490 candidates were classified by hand. A candidate was genuine only if a postposed tonic demonstrative functioned as the topic/head of a bare exclamatory infinitive.

## Per-file candidate counts

| Play file | Candidates |
|---|---|
| musset-comedies-proverbes-1850 | 107 |
| scribe-bertrand-et-raton | 57 |
| dumas-mariage-louis-xv-1841 | 56 |
| dumas-kean | 46 |
| labiche-chapeau-de-paille | 44 |
| scribe-verre-d-eau | 40 |
| labiche-martin-poudre-aux-yeux | 33 |
| hugo-ruy-blas | 26 |
| dumas-tour-de-nesle | 23 |
| vigny-chatterton-1835 | 18 |
| dumas-antony | 17 |
| dumas-henri-iii | 11 |
| hugo-hernani | 10 |
| hugo-burgraves | 2 |
| **Total** | **490** |

## Classification (all 490 non-genuine)

| Confound class | Share of candidates | Examples |
|---|---|---|
| Demonstrative in a finite clause ("cela est", "ça me fera plaisir", "C'est cela !", "tout cela n'est que préjugé", "Qu'est-ce que cela me fait ?") | dominant, especially Labiche's colloquial "ça" | labiche-chapeau-de-paille @9005, @9005+; labiche-martin-poudre-aux-yeux @58272+; musset @60310+ |
| Demonstrative governed by a verb or preposition ("pour cela", "de cela", "dites mieux que cela", "Songez à ceci !", "s'attendre à cela", "faire de cela") | common | musset-comedies-proverbes-1850 @271 ("après tout cela, avoir peuplé un palais d'ouvrages magnifiques" — infinitive present, but "cela" governed by "après"); vigny-chatterton-1835 @15938/15969 ("Songez à ceci !"); musset @139147 |
| Demonstrative as object of the bare exclamatory infinitive, not as postposed topic | rare but closest misses | dumas-henri-iii @168: "Gouverner tout cela ! — Monter, si l'on vous nomme, À ce faîte !" — "tout cela" is the direct object of "Gouverner", not a dislocated topic |
| Interrogative / formulaic ("comment cela ?", "Comment cela va-t-il ?", "qu'à cela ne tienne", "Si ce n'était que cela !…") | common | hugo-ruy-blas @880; scribe-bertrand-et-raton @132885+ |
| "ah ça" / "ça," interjections and vocatives | Labiche-heavy | labiche-chapeau-de-paille @19233+ |
| False-INF hits (nouns/finite verbs ending in -er/-ir/-re/-oir: "souvenir", "pauvre", "blessure", "votre", "père", "fiacre", "soulier", "arrosoir", "jarretière", "bouilloire", "réverbère") | regular | musset @304/305 ("une ca-verne" — the regex's bare "ca" variant catches the hyphenated OCR line break) |

## Window-level evidence (offsets are absolute byte offsets in the play text)

1. Closest structural miss, dumas-henri-iii @168: "Gouverner tout cela ! — Monter, si l'on vous nomme, À ce faîte !" — genuine bare exclamatory infinitive "Gouverner", but the demonstrative is its object, not a postposed topic. Non-genuine.
2. scribe-verre-d-eau @146395: "Bolingbroke, ministre !… Et tout cela grâce à un verre d'eau !" — exclamatory nominal structure; "tout cela" is not the topic of an infinitive. Non-genuine.
3. musset-comedies-proverbes-1850 @20954: "le rôle d'un bon ange à jouer ! … et, après tout cela, avoir peuplé un palais d'ouvrages magnifiques" — bare exclamatory infinitive "avoir peuplé" present, but "cela" is governed by "après". Non-genuine.
4. vigny-chatterton-1835 @15938/15969: "Songez à ceci ! la raison est une puissance froide et lente" — imperative finite verb; "ceci" its governed object. Non-genuine.
5. labiche-chapeau-de-paille @15783: "C'est très louche, ça, madame…" — demonstrative in a finite clause (Labiche's signature "ça"). Non-genuine.
6. musset-comedies-proverbes-1850 @198789: "tu rugis comme une ca-verne" — OCR hyphenation artifact caught by the bare-"ca" regex variant. Non-genuine.

## Per-clause results

1. Census bar: **PASS** — 490 unique candidates from a 14-play drama corpus were exhaustively hand-classified with window-level evidence.
2. ≥1 genuine re-opens: **NO FIRE** — 0 of 490 candidates are genuine postposed-demonstrative + bare exclamatory infinitives.
3. Confirmed zero fences: **CONFIRMED** — zero genuine attestations over the full play texts implies zero in dialogue.

## Verdict

**NULL → fence.** The inverted order "[bare inf]!, cela/ceci/ça" is confirmed absent in drama-corpus dialogue. This fences arm (a) of the `ce87-1028-role` target at a seventh level, joining the six already fenced: RDM-1841 full-corpus inversion census, drama dialogue (arm (a) at four levels), prose inversion, prose clause-initial, epistolary, and comedy reinforcement probes.

## Proposed follow-up targets (all verified absent from battery-queue.json, 2026-10-09)

1. `disloc-nominal-inversion-drama` — census postposed NOMINAL topics ("Voler, la victoire !") in the same 14-play drama corpus. Tests whether the fence is demonstrative-specific or topic-postposition-specific; a genuine nominal postposition with zero demonstrative postposition would sharpen the fence into a demonstrative-only prohibition.
2. `disloc-demonstrative-inversion-comedy` — run the same inversion census over the widened comedy corpus (Scribe/Labiche, ~1.36M chars). Labiche's dialogue carries the densest "ça" usage in the whole drama set; comedy is the most plausible remaining register for the shape if it exists anywhere in dialogue.
3. `disloc-demonstrative-inversion-periodical` — run the inversion census over the side-period corpus (14 Allgemeine-Zeitung 1841 issues + Guizot/Talleyrand memoirs). Journalistic and political prose use exclamatory rhetoric heavily; this tests the shape in a non-literary prose register.
