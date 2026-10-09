# Battery `gov-excl-inf-drama-comedy-skew` — verdict: PROMOTE

## Bar (verbatim, pre-registered)

"> =1 genuine in a non-comedy play shows drama-wide; zero outside comedy-drama hardens the comedy-skew"

→ C1 (≥1 genuine governed exclamatory infinitive in a non-comedy play → drama-wide) / C2 (confirmed zero outside comedy-drama → comedy-skew hardened).

## Method

New corpus arm: 7 non-comic 19th-century plays ingested from fr.wikisource via
the API (action=parse, prop=text) with the same strip-and-save pipeline as
`comedy_extension_ingest.py`; raw API JSON kept under
`goals/cipher-hunt-cracking-lanes/hidden_files/comedy-skew-ingest/`.
Ingest script: `code/crowd17/next-token/comedy_skew_ingest_v2.py`
(v1 fetched only Ponsard's *Lucrèce*; title resolution + act-subpage
fallback in v2).

Corpus (all new, never censused before — 1,206,208 chars, 5,102 bangs):
- hugo-roi-samuse.txt — Hugo, *Le Roi s'amuse* (drame, 1832), 267,543 chars
- hugo-lucrece-borgia.txt — Hugo, *Lucrèce Borgia* (drame, 1833), 143,773 chars
- hugo-marie-tudor.txt — Hugo, *Marie Tudor* (drame, 1833), 250,077 chars
- hugo-angelo.txt — Hugo, *Angelo, tyran de Padoue* (drame, 1835), 33,951 chars
- musset-lorenzaccio.txt — Musset, *Lorenzaccio* (drame, 1834), 244,286 chars
- dumas-fils-dame-camelias.txt — Dumas fils, *La Dame aux camélias* (drame, 1852), 231,022 chars
- ponsard-lucrece.txt — Ponsard, *Lucrèce* (tragédie, 1843), 98,042 chars

Two fetch attempts dropped with cause: `hugo-marion-delorme.txt` was the
preface only (no play text); `scribe-adrienne-lecouvreur.txt` was a
*Revue des Deux Mondes* review, not the play.

Census: P1/P2 design VERBATIM from `gov_excl_inf_register_drama_census.py`
(120-char lookback per "!", GOV_INF = (pour|à|de|d') + ≤2 short tokens +
infinitive-shaped word, closest match, skip on [.;] tail). Script:
`code/crowd17/next-token/gov_excl_inf_drama_comedy_skew_census.py`;
output `gov-excl-inf-drama-comedy-skew_census.json`. 371 candidates;
ALL 371 classified by hand against the parent taxonomy.

## Findings

**C1 FIRES — 4 genuine attestations, all in non-comedy drames:**

1. **Hugo, *Le Roi s'amuse*** (@18467, dist 13, de+vouloir): Triboulet's
   corrective retort — "…vous rêvez, / **De vouloir des savants !**"
   The "!" terminates the de-infinitive phrase itself; no finite verb in
   the unit. Context byte-verified.
2. **Hugo, *Le Roi s'amuse*** (@18500, dist 13, de+vouloir): the Roi's
   echo — "**De vouloir des savants !** Moi, foi de gentilhomme…"
   Same fragment grade, independent utterance.
3. **Hugo, *Lucrèce Borgia*** (@106314, dist 18, de+écraser): Lucrezia —
   "…La salle d'à côté est pleine de piques. **À mon tour maintenant,
   à moi de parler haut et de vous écraser la tête du talon !**"
   No finite verb; the "!" closes the de-infinitive phrase. Context
   byte-verified.
4. **Dumas fils, *La Dame aux camélias*** (@57990, dist 1, pour+payer):
   Q/A fragment — Armand: "Et pourquoi ces ventes et ces
   engagements ?" / Prudence: "**Pour payer !**"
   No finite verb; same fragment grade as the sibling n2's accepted
   cases ("Pour lui causer !", "Pas pour être témoin !").
   Context byte-verified.

All four are dialogue-elliptical fragments — the same grade as the 6
comedy-drama cases (2 Scribe, 4 Labiche), not a fully conventionalized
standalone "pour rire !". So the genre difference is not in grade, only
in genre label: the construction is **drama-wide, not comedy-skewed**.

Per-play results:
- *Le Roi s'amuse*: 100 candidates → 2 genuine (rest: finite matrices,
  Cause-C exclaimed-NP embeddings, interrogatives, noun false friends,
  bare infinitives)
- *Lucrèce Borgia*: 66 candidates → 1 genuine (rest: finite matrices,
  Cause-C, bare infinitives, quoted cries, song/imperative "!"s)
- *Marie Tudor*: 67 candidates → 0 genuine (near-misses: "personne à qui
  me fier ici !" — pronoun-headed, Cause-C family; "un ordre pour
  suspendre l'exécution !" — exclaimed NP, Cause-C)
- *Angelo*: 14 candidates → 0 genuine (3 Cause-C near-misses:
  "La belle occasion pour prendre cet air effaré !",
  "Quelle joie de pouvoir être seuls…", "Quelle folie d'être venus…")
- *Lorenzaccio*: 64 candidates → 0 genuine ("quelle belle épaule à
  essuyer", "Le joli pied à déchausser", "Renzo, un homme à craindre"
  all Cause-C; "Il s'agissait bien de réclamer justice !" finite;
  "Parler de mains expérimentées…" bare)
- *La Dame aux camélias*: 42 candidates → 1 genuine
- *Lucrèce* (Ponsard): 18 candidates → 0 genuine (all false friends /
  finite matrices / purpose adjuncts)

**C2 antecedent false.** The comedy-skew hypothesis is falsified at the
bar's stated standard: genuine cases now sit in drames (Hugo ×3,
Dumas fils ×1) alongside the comedies (Scribe ×2, Labiche ×4).
Cumulative drama state: 35 files, ~5.2M chars, 10 genuine — 6 comedy,
4 drame. Tragédie proper still zero (only Ponsard's *Lucrèce* censused;
one data point, not a pattern).

## Verdict: PROMOTE

The corpus result is delivered: the governed exclamatory infinitive is
drama-wide. The comedy-skew residual is closed — genre label does not
predict the construction; dialogue-elliptical fragment grade does.
No standing/red-team verdict touched; §7 intact.

## Follow-ups proposed (for supervisor queuing)

1. `gov-excl-inf-tragedy-n2` (P3) — census 2–3 more tragédies (Delavigne,
   Chénier, *Lucrèce Borgia* is drame not tragédie) to test the
   remaining tragédie-zero with more than one data point.
2. `gov-excl-inf-drama-grade` (P3) — corpus audit: is the construction
   ALWAYS dialogue-elliptical fragments in drama, or does any play
   show a standalone ("pour rire !"-grade) case? Sharpens the
   construction's grammar.
3. `gov-excl-inf-prose-drama-bridge` (P4) — gated: test whether the 4
   drame cases' dialogue-elliptical character predicts prose zeros
   (prose lacks the dialogue retort slot) — registers as venue.

## Bookkeeping

- Corpus: 7 files under `code/side-period/corpus/` (+ PROVENANCE-comedy-skew-v2.txt
  in the hidden ingest dir); raw API JSON in
  `goals/cipher-hunt-cracking-lanes/hidden_files/comedy-skew-ingest/`
- Census script: `code/crowd17/next-token/gov_excl_inf_drama_comedy_skew_census.py`;
  ingest scripts: `comedy_skew_ingest.py`, `comedy_skew_ingest_v2.py`
- Output: `code/crowd17/next-token/gov-excl-inf-drama-comedy-skew_census.json`
- Queue: `gov-excl-inf-drama-comedy-skew` → `status: verdict`, `result: promote`,
  2026-10-09 (pre-write assert passed — was queued/verdictless; temp-file +
  rename; JSON re-validated; own entry only; no downgrade)
- Lock created on start, deleted on completion (verified gone). R5005,
  sealed gates, red-team adjudication queue untouched.
