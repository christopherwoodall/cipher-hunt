# Battery report — bare-noun-1841

**Target:** `bare-noun-1841`
**Date:** 2026-10-09
**Verdict: KILL** — the grammaticality objection is kill-grade: productive bare singular nominals as direct objects are unattested in 1841 French. Any cipher parse requiring a productive (non-idiomatic) bare singular nominal as direct object — including as head of a "[Vinf] N et le N'" coordination — is dead.

## Bar (verbatim from battery-queue.json)

`None`

**Restated as numbered clauses (pre-registered before testing; the bar is the claim itself):**
- **C1:** Census bare singular common nouns as direct objects of infinitives in the 1841 French corpus. If zero productive (non-idiom, non-proper-name) instances → the objection is kill-grade. If productive instances exist → the objection is merely a fence.
- **C2:** Census the "[Vinf] N et le N'" coordination pattern (bare N heading a direct-object coordination). If zero genuine instances → kill-grade. If genuine instances exist → fence.

## Method

Corpus: `code/side-period/corpus`, French files only (58 files, 30,877,284 chars, 4,657,121 tokens; harvested 2026-10-07 per `PROVENANCE.md`). German files excluded: `adb-zeschau-*`, `allgemeine-zeitung-augsburg-1841-*` (15), `metternich-papiere-*` (2).

Pipeline (scripts `/tmp/bare-noun-1841-v2.py`, `/tmp/bare-noun-1841-v4.py`; rerunnable):
1. Tokenized (lowercased, apostrophe-preserving).
2. Noun lexicon: words following a determiner/article (le/la/l'/les/un/une/des/du/de/d'/au/aux/ce/…) ≥5 times, minus function-word stoplist → 11,733 nouns. Elided determiners (`l'`, `d'`, `qu'`) recognized so `l'univers` is not misread as bare.
3. Infinitive set: curated list of 186 common French infinitives actually attested in the corpus (ending-heuristics rejected — `-re` admits `votre/autre/lettre`; `-er` admits adjectives).
4. Pattern A: INF + bare NOUN (adjacent, noun truly determiner-less) → 13,379 tokens / 6,060 distinct pairs.
5. Pattern B: INF + bare NOUN + `et` + DET + NOUN → 84 raw hits, re-filtered strict → 32.
6. Baseline: INF + DET + NOUN → 11,033 tokens (the licensed construction, for scale).
7. Hand-classified all top pairs and every surviving candidate with full context.

## Findings

### C1: bare singular nominals as direct objects — 0 productive instances

Every Pattern A hit falls into exactly one of these bins; **zero** are productive bare common-noun direct objects:

- **INF+INF sequences** (largest bin): `faire connaître/entendre/passer/comprendre/cesser/sortir/sentir/oublier/rentrer/parvenir/remarquer/croire/entrer/respecter/venir/tomber/triompher/prendre/voir/dire`, `laisser aller/faire/tomber`, `aller chercher`, `savoir faire`, `voir arriver`, `entendre parler`, etc.
- **Closed idiom inventory** (all lexicalized; each bound to 1–3 verbs): `rendre compte`, `prendre part/partie`, `mettre fin`, `tenir compte`, `donner lieu/suite/lecture/communication/avis/satisfaction`, `porter atteinte/secours/remède`, `faire face/peur/part/usage/mention/honneur/plaisir/preuve/fortune/feu/violence/injure/appel/attention`, `demander asile`, `prendre soin/copie/patience/position/possession/racine/garde`, `rendre maître/service/hommage`, `chercher querelle`, `courir sus`, `faire jour/cause`, `mettre obstacle`.
- **Vocatives / proper names** (grammatically licensed — proper names take no determiner): `dire monsieur`, `voir madame`, `voir lord`, `traduire pétrarque`.
- **Editorial cross-references:** `voir page`, `voir pages`, `voir ci-dessus`.
- **Complementizers / adverbs / pronouns / prepositions** misclassified by the lexicon: `dire que`, `voir comment`, `faire autrement/autant`, `voir clair/enfin`, `dire vrai/aujourd'hui`, `rendre heureux/digne/possible` (adjectives), `aller jusqu'à`, `faire auprès`, `dire rien` (negation).
- **`pouvoir` as noun:** `pouvoir absolu/politique/royal` (`le pouvoir`).
- **OCR/editorial noise:** `faire con[duire]` (line-break split), `acte ii scène i` (theatrical act/scene references), `archives du comte` (archival insertions in Nesselrode correspondence).

**Decisive check:** nouns appearing bare after ≥3 distinct infinitives (613 candidates) were audited — every one resolves to adverbs (`aujourd'hui`, `plutôt`, `davantage`), verbs (`était`, `sont`, `dit`), pronouns (`chacun`, `rien`, `moi`), numbers (`deux`, `mille`, `trois`), conjunctions (`puisque`, `lorsque`), prepositions (`jusqu'au`, `hors`, `auprès`), interjections (`adieu`), or proper names (`dieu`, `marguerite`, `edouard`, `armand`). **Not one genuine common noun appears bare across multiple verbs.** The two apparent exceptions collapsed on inspection: `acte` = theatrical references + `faire/prendre acte` idioms; `archives` = plural editorial insertions.

Scale contrast: determined direct objects (INF+DET+NOUN) = **11,033 tokens**; productive bare-noun direct objects = **0 tokens** in 4.66M tokens of 1841 French.

### C2: "[Vinf] N et le N'" coordination — 0 genuine instances

Of 32 strict hits, **zero** are genuine `[Vinf] [bare-N] et [DET] [N]` coordinations. All are:
- verb-phrase coordinations (`donner chasse et le payer`, `faire ministre et le conserver ministre`, `faire justice et de rendre évidente`),
- new clauses after the infinitive phrase (`faire subir et le pays tout entier…`, `faire remarquer et le gouvernement…`, `porter remède et les démarches…`, `prendre racine et la main…`, `faire fortune et le dimanche…`),
- proper-name coordination (`traduire pétrarque et les poètes italiens` — licensed),
- idiom + new clause (`tenir parole et le duc…`, `faire halte et le quartier général…`),
- lexicon noise (`faire oublier et le juillet` — `oublier` mislexiconed via `l'oublier`).

## Per-clause pass/fail

- **C1:** PASS at kill grade — 0 productive bare singular nominal direct objects in 30.9M chars / 4.66M tokens, against 11,033 determined-DO tokens. Distributional rejection at the lane's standard.
- **C2:** PASS at kill grade — 0 genuine `[Vinf] N et le N'` coordinations; all 32 strict hits reclassify as verb coordinations, clause boundaries, proper names, or noise.

## Verdict: KILL

The grammaticality objection is **kill-grade**, not a fence. A cipher-window parse that requires a bare singular common nominal as a direct object — or as the head of a direct-object coordination — is ungrammatical in 1841 French and is dead **unless** it falls into one of the three licensed exceptions:

1. **Closed idiom inventory** (listed above — `faire/donner/prendre/porter/rendre/tenir/demander/chercher` + fixed nouns; the inventory is closed, not productive);
2. **Proper names** (no determiner required);
3. **Vocatives** (`dire monsieur`, `voir madame`).

Any future battery invoking a bare-noun direct-object parse must name the specific licensing idiom or exception; otherwise the parse is kill-grade dead on this corpus result.

## Scope

Corpus result only; names no cipher values and touches no stream windows. No standing or red-team verdict contradicted; §7 intact. Does not re-litigate any prior battery. The idiom inventory above is offered as a resource for future batteries testing specific verb+noun pairs.

## Adverses

None listed on the target (bars field was `None`).

## Bookkeeping

- Lock: `code/crowd17/next-token/locks/bare-noun-1841.lock` created 2026-10-09T18:17:00Z (agent d242e803-d595-4f99-91e3-531f483edeca), deleted on completion.
- Queue: `bare-noun-1841` queued/verdictless at start (pre-write assert passed); updated via temp-file + rename to `status: verdict`, `verdict: {result: kill, report: ..., date: 2026-10-09}`; own entry only; disk re-validated; no downgrade.
- R5005, sealed gate instances, and the red-team adjudication queue untouched.
- Corpus provenance: `code/side-period/corpus/PROVENANCE.md` (harvested 2026-10-07, public domain pre-1923 works); German files excluded as listed in Method.
