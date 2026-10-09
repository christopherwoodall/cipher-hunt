# Battery `gov-excl-inf-tragedy-n2` — verdict: PROMOTE

## Bar (verbatim, pre-registered)

"census 2-3 additional tragédies with the P1/P2 design VERBATIM; zero
genuine outside comedy-drama hardens the comedy-skew, >=1 genuine tragédie
case shows drama-wide"

→ C1 (≥1 genuine tragédie case → the construction is drama-wide, extending
to tragédie proper) / C2 (confirmed zero across all new tragédies →
tragédie-zero hardened). Note: the "comedy-skew" antecedent in the bar is
stale — the sibling `gov-excl-inf-drama-comedy-skew` already falsified it
(drames attest the construction, Hugo ×3, Dumas fils ×1). The live question
is tragédie proper, still zero on the single Ponsard *Lucrèce* data point.

## Method

Census design VERBATIM from `gov_excl_inf_register_drama_census.py` (via the
sibling's census script): for every "!", 120-char lookback, GOV_INF =
(pour|à|a|de|d') + ≤2 short tokens + infinitive-shaped word, closest match,
skip if [.;] between match end and "!". All 75 candidates classified BY HAND
against the parent taxonomy. Census script:
`code/crowd17/next-token/gov_excl_inf_tragedy_n2_census.py` (regex and
candidate function byte-identical to the sibling's);
output `code/crowd17/next-token/gov-excl-inf-tragedy-n2_census.json`.

Corpus: 3 NEW Delavigne tragédies (never censused before), byte-split from
Internet Archive OCR of the 1854 Didier *Théâtre* set — 322,004 chars,
987 bangs, 75 candidates:
- `code/side-period/corpus/delavigne-vepres-siciliennes.txt` — Delavigne,
  *Les Vêpres siciliennes, tragédie en cinq actes* (1819), 106,184 chars,
  323 bangs, 29 candidates (split [707:106891] of vol 1; examen critique
  excluded)
- `code/side-period/corpus/delavigne-paria.txt` — Delavigne, *Le Paria,
  tragédie* (1821), 136,293 chars, 335 bangs, 30 candidates
  (split [263121:399414] of vol 1)
- `code/side-period/corpus/delavigne-famille-luther.txt` — Delavigne,
  *Une famille au temps de Luther, tragédie* (1836), 79,527 chars,
  329 bangs, 16 candidates (split [672:80199] of vol 3)

Raw OCR volumes retained in-corpus as `raw-thtredecasim01dela-djvu.txt`
and `raw-thtredecasim03dela-djvu.txt`; provenance (source URL, retrieval
time, sha256) in `code/side-period/corpus/PROVENANCE-delavigne-tragedies.txt`.
OCR is UNCORRECTED (Google-scanner noise, e.g. "Lies Vêpres", "Tppprobre");
diacritic noise tolerated by the char-class regex.

Fetch note (dropped with cause, sibling-report precedent): Delavigne and
Chénier tragédies are largely absent from fr.wikisource — "Le Paria" there
is Ubald Paquin's 1933 novel (not the play); "Les Enfants d'Édouard",
"Louis XI", "Le Paria (Delavigne)", "Les Vêpres siciliennes", "Charles IX
(Chénier)", "Caius Gracchus", "La Mort de Calas", "Timoléon" all MISSING via
exact title query, opensearch, and allpages-prefix listing. Internet
Archive supplied three clean Delavigne tragédies instead; Chénier remains
uncensused.

## Findings

**C1 FIRES — 1 genuine tragédie case. C2 antecedent false.**

The 74 excluded candidates (all classified by hand; per-play windows in
the census JSON): finite matrices (optative "Puissé-je", passé simple
"soutint"/"sembla"/"mourut", subjunctives "sorte"/"vienne"/"meure"/
"cessent"/"retienne", interrogatives "Puis-je...?"/"devais-je...?",
imperatives "Rends"/"Choisissez"/"Mur-mure"/"sauve"), Cause-C
exclaimed-NP embeddings ("un ordre"-grade: "D'immoler votre chef à ma
gloire offensée !" — infinitive governed by the head noun "pensée",
excluded per parent taxonomy like "un ordre pour suspendre l'exécution !"),
noun false friends (cendre, maître, gloire, victoire, titre, sceptre,
soupir, père, l'autre), and purpose adjuncts inside finite clauses
("pour chercher un coupable !", "pour foudroyer sa tête !").

The genuine case (byte-verified, window clean, no OCR noise):
- **Delavigne, *Une famille au temps de Luther*** (@70173, dist 0, à+revoir):
  Luigi — "…Jugera qui de nous suit son précepte. Adieu, /
  {Revenant sur ses pas pour lui serrer la main.) / **Ou plutôt à
  revoir !**"
  Corrective self-repair of "Adieu": the "!" directly terminates the
  "à revoir" fragment; the only infinitive in the stage direction
  ("serrer") is a purpose adjunct, and the nearest finite verb ("Jugera")
  is two sentences back. Exclaimed à+infinitive fragment with no finite
  verb in the unit — the same dialogue-elliptical fragment grade as all
  prior genuine cases ("Pour payer !", "Pas pour être témoin !",
  "De vouloir des savants !"), not a fully conventionalized standalone.

Per-play: *Vêpres siciliennes* 29→0 genuine; *Le Paria* 30→0 genuine;
*Une famille au temps de Luther* 16→1 genuine.

## Verdict: PROMOTE

The governed exclamatory infinitive is now attested in tragédie proper.
The tragédie-zero is dead on four data points (Ponsard *Lucrèce* ×0,
Delavigne *Vêpres siciliennes* ×0, Delavigne *Le Paria* ×0, Delavigne
*Une famille au temps de Luther* ×1): the construction is drama-wide
across comedy-drama (Scribe ×2, Labiche ×4), drame (Hugo ×3, Dumas
fils ×1), and tragédie (Delavigne ×1). Cumulative drama state: 38 files,
~5.5M chars, 11 genuine. Genre label does not predict the construction;
the dialogue-elliptical fragment grade does.
No standing/red-team verdict touched; §7 intact; R5005, sealed gates,
red-team queue untouched. No follow-ups required per §4 (promote);
Chénier tragédies remain an optional future data point.

## Bookkeeping

- Queue: `gov-excl-inf-tragedy-n2` → `status: verdict`, `result: promote`,
  2026-10-09 (pre-write assert passed — was queued/verdictless; temp-file
  + rename; JSON re-validated from disk; own entry only; no downgrade)
- Lock created on start (2026-10-09T13:18:00Z), deleted on completion
  (verified gone).
- Corpus: 3 play files + 2 raw OCR files + PROVENANCE-delavigne-tragedies.txt
  under `code/side-period/corpus/`
- Census script + output: `code/crowd17/next-token/`
  (gov_excl_inf_tragedy_n2_census.py, gov-excl-inf-tragedy-n2_census.json)
