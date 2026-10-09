# Battery report: disloc-tonic-personal-census

**Verdict: PROMOTE** — 2026-10-09

## Bar (verbatim, pre-registered)

"pins the licensor class if 'Moi, voler !' generalizes in drama; >=1 genuine re-opens the tonic-fronting frame"

Restated as numbered clauses:

1. A positive-space census of dislocated personal tonic pronouns (moi/toi/lui/elle/nous/vous/eux) + bare exclamatory infinitive across the full drama register **pins the licensor class if "Moi, voler !" generalizes in drama**.
2. **>=1 genuine attestation re-opens the tonic-fronting frame.**

## Corpus

`code/side-period/corpus/` — 14 unique plays, 2,969,582 characters. One edition per play per the queue gate: `hugo-hernani-1870.txt` kept, `hugo-hernani.txt` (Hetzel 1889 duplicate) excluded. Files: Hugo (Hernani 1870, Burgraves, Ruy Blas), Dumas (Mariage Louis XV, Antony, Henri III, Kean, Tour de Nesle), Scribe (Bertrand et Raton, Verre d'eau), Labiche (Chapeau de paille, Poudre aux yeux), Vigny (Chatterton), Musset (Comédies et proverbes, 10 plays). Provenance: `code/side-period/corpus/PROVENANCE.md` (Family 9 + wikisource ingest).

## Method

Re-runnable script `code/crowd17/next-token/disloc_tonic_personal_census.py`
(mirrors the sibling `disloc_demonstrative_drama_reinforced_census.py` taxonomy):

- **P1 (dislocation):** `\b(moi|toi|lui|elle|nous|vous|eux)\s*[,;:]` (case-insensitive). Window = pronoun through the next `[!?.]` (inclusive), capped at 180 chars.
- **P2 (exclamatory filter):** window must contain `!`.
- **P3 (infinitive candidate):** `\b[a-zàâäçéèêëîïôöùûü']{2,}(er|ir|re|oir)\b` on the window.

Yield: 1,986 pronoun-comma hits → 427 exclamatory candidates → **153 with infinitive-shaped tokens** → manual classification of all 153.

Classification taxonomy (cause labels): **a** = governed infinitive (pour/de/à/il-est-facile-de); **b** = modal-governed infinitive (pouvoir/vouloir/devoir/aller); **c** = finite clause (head is subject of a finite verb, or relative clause); **d** = nominal/adjectival/apposition exclamation (no infinitive); **f** = head governed (e.g. "à toi" indirect object), not a dislocated topic; **g** = no true infinitive (inf-shaped word is a noun/adjective/finite verb); **h** = imperative; **i** = vocative address.

**Excluded: 132 of 153** — a:11, b:6, c:51, d:31, f:2, g:11, h:4, i:16.

Two window cuts were re-checked against wider context (window truncation misleads):
- Burgraves "elle, disparaître, Hélas !" → full text "j'ai vu, comme elle, disparaître, Hélas ! sept de mes fils" — infinitive governed by "j'ai vu" (perception verb), "comme elle" is a comparison, not a topic. Excluded (a).
- Musset "toi, dans le silence du cabinet, de tracer ... !" → full text "Qu'il t'est facile à toi, dans le silence du cabinet, de tracer d'une main légère une ligne ..." — "de tracer" governed by "il est facile ... de". Excluded (a).

## Window-level evidence: 21 genuine

Dislocated personal tonic pronoun as topic + **bare** exclamatory infinitive. Offsets are character offsets in the named file.

1. hugo-burgraves.txt @52479 — "toi, Ne point contrarier ta fièvre et ton délire, Et te baiser les mains en te laissant tout dire !" (bare infinitives contrarier, baiser)
2. hugo-burgraves.txt @54594 — "Toi, mourir si jeune !"
3. dumas-mariage-louis-xv-1841.txt @53848 — "Moi, m'en aller!"
4. dumas-antony.txt @57731 — "Elle, pleurer !"
5. dumas-antony.txt @57748 — "elle, souffrir, ô mon Dieu !"
6. dumas-henri-iii.txt @26443 — "Moi, m'éloigner !"
7. dumas-henri-iii.txt @95619 — "Moi, vous tromper… Ah !"
8. dumas-henri-iii.txt @120601 — "Moi, fuir !"
9. dumas-henri-iii.txt @121229 — "moi, fuir devant le duc de Guise !"
10. dumas-kean.txt @31991 — "Moi, avoir oublié mes vieux camarades !" (infinitive composé, bare)
11. dumas-kean.txt @34814 — "Elle, refuser !"
12. dumas-kean.txt @48083 — "moi, quitter le théâtre, renoncer à ses émotions, à ses éblouissements, à ses douleurs !"
13. dumas-kean.txt @48172 — "moi, céder la place à Kemble et à Macready, pour qu'on m'oublie au bout d'un an, au bout de six mois, peut-être !" (purpose subjunctive adjunct after the bare infinitive)
14. dumas-kean.txt @134211 — "Moi, fuir… moi, quitter Londres, l'Angleterre, comme un lâche qui tremble… Oh !"
15. dumas-kean.txt @134222 — "moi, quitter Londres, l'Angleterre, comme un lâche qui tremble… Oh !" (same speech, repeated topic)
16. dumas-tour-de-nesle.txt @101319 — "Moi, quitter Paris !"
17. scribe-bertrand-et-raton.txt @47820 — "Moi, déprécier le commerce !"
18. scribe-bertrand-et-raton.txt @132274 — "Vous, Rantzau, donner votre démission !" (vous + apposition Rantzau)
19. scribe-bertrand-et-raton.txt @171804 — "Lui, nous trahir !"
20. labiche-chapeau-de-paille.txt @33939 — "moi, épouser une autre femme !"
21. vigny-chatterton-1835.txt @87048 — "moi, le tuer !"

Per-pronoun genuine counts: moi 14, toi 2, elle 3, vous 1, lui 1, nous 0, eux 0. Attested in 8 of 14 plays (Burgraves, Antony, Henri III, Kean, Tour de Nesle, Bertrand et Raton, Chapeau de paille, Chatterton, Mariage sous Louis XV).

## Per-clause pass/fail

- **Clause 1 — PASS.** "Moi, voler !" generalizes in drama: 21 genuine dislocated-tonic + bare-exclamatory-infinitive windows across 8 plays. The licensor class is pinned by contrast: personal tonic pronouns license the bare exclamatory infinitive (this battery), while demonstrative heads — bare "ce" (battery-disloc-demonstrative-drama-reissue, 0/35 genuine, null) and reinforced "celui-là/ceux-là/..." (battery-disloc-demonstrative-drama-reinforced, 0/8 genuine, null) — do not, over the same 2,969,582-char corpus. The register's positive controls (Hernani "Gouverner tout cela !") have the demonstrative as OBJECT after the infinitive — a different shape, untouched.
- **Clause 2 — PASS.** 21 ≥ 1. The tonic-fronting frame is re-opened.

## Verdict: PROMOTE

The tonic-fronting frame for bare exclamatory infinitives in the drama register is **licensed by dislocated personal tonic pronouns**. Licensor class pinned: {moi, toi, lui, elle, vous} attested; demonstrative heads fenced (sibling batteries' nulls, not contradicted — this battery's positive class is disjoint).

No adverses were pre-registered. No standing verdict touched; R5005 untouched; sealed gates and red-team queue untouched.

Lock: created on start (agent 1e169504-ff71-4045-a94b-de5c79e18b2c, 2026-10-09T08:46:46Z), no stale lock present, deleted on completion.

## Raw census data

- `code/crowd17/next-token/disloc-tonic-personal-census.json` — 153 candidate windows with per-file counts and infinitive-shaped hits.
- Script: `code/crowd17/next-token/disloc_tonic_personal_census.py`.
