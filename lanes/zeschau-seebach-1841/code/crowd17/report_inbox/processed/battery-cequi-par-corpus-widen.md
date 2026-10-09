# Battery `cequi-par-corpus-widen` — verdict: PROMOTE (zero hardened: 0 genuine in 57.37M chars)

## Bar (verbatim, pre-registered)

"expand the prose census with more 1841 diplomatic texts to harden the zero beyond 31.66M chars."

## Bar restated (numbered, before testing)

- **C1:** Add ≥1 new 1841-diplomatic French prose text to the period corpus, with provenance (source URL, retrieval method/date, sha256, rights).
- **C2:** Re-run the parent `ceci-correlative-corpus` methodology (exact regex `ce\s+qui\s+par\b` on whitespace-normalized text; generosity pass `qui\s+par\b` with `ceci` within ~600 chars) on the widened French corpus; total chars must exceed the parent's 31,664,431.
- **C3:** Hand-classify every NEW hit against the genuine criterion (a VERBLESS "ce qui par [N]" chunk followed by "ceci" heading the main clause, i.e. the cipher's "45 64 96 43 87 01" frame as a correlative); the zero hardens iff 0 genuine attestations.

Adverses: none listed on the target.

## Method

Harvested 21 new French prose texts (2026-10-09, curl; Gutenberg HTTPS and
archive.org http + redirect-follow), all public domain, all with provenance
entries in `code/side-period/corpus/PROVENANCE.md` (source URL, retrieval
method/date, byte count, sha256 prefix, rights note). New families:
Talleyrand *Mémoires* vols 2–5 (archive.org), Chateaubriand *Mémoires
d'Outre-Tombe* tomes 1–5 (Gutenberg #18864/#23654/#45550/#25575/#28930),
Guizot *Mémoires* t. 3–4 UofT scan (archive.org item
`mmoirespourser03guizuoft`), Pozzo di Borgo *Correspondance* vol. 2,
Tocqueville *De la Démocratie en Amérique* t. 1–4 (Gutenberg
#30513–#30516), Thiers *Histoire du Consulat et de l'Empire* vols 1–4
(Gutenberg #27380/#27381/#30603/#31846), *Revue des deux mondes* 1840
vols 2–3 (archive.org). One planned file failed: 1840 vol. 1's
`_djvu.txt` returned HTTP 500 from archive.org (recorded in PROVENANCE.md
for retry).

Census script: `code/crowd17/next-token/cequi_par_widen_census.py`;
results: `code/crowd17/next-token/cequi-par-widen_census.json`.
Census set: 80 texts (all French `.txt` in `code/side-period/corpus`,
excluding the 15 German *Allgemeine Zeitung* issues, `adb-zeschau`,
provenance/harvest logs; metternich-papiere-v4/v6 INCLUDED to replicate
the parent's hits). `canonical.py` never used (corpus test, not stream).

## Findings

- **Corpus: 80 texts, 57,374,033 chars** (parent: 63 texts, 31,664,431
  chars). C1 and C2 PASS.
- **Parent replication check:** the parent's 3 exact hits reproduce at
  byte-identical offsets (metternich-papiere-v4 @1102764, @1210274;
  metternich-papiere-v6 @917425) — methodology verified.
- **New exact hits: 1.** `talleyrand-memoires-v5.txt` @722480:
  "…je me bornerai donc à vous tenir exactement informé de **tout ce qui
  par viendra à ma connaissance**." Hand-classified EXCLUDED: this is
  "ce qui parviendra" — the verb *parvenir* (future), OCR-split as "par
  viendra" — i.e. relative "ce qui" + FINITE VERB, not prepositional
  "par" + noun. Not verbless; no "ceci". Excluded with cause (regex
  artifact of OCR word-splitting).
- **New generosity hits: 1.** `revue-deux-mondes-1840-q3.txt` @1187509:
  "…et **qui par là** me faisoit espérer bien des choses de cette part…"
  Hand-classified EXCLUDED: relative + adjunct "par là" + finite verb
  "faisoit" — not verbless; the window's "ceci" is parenthetical ("je dis
  ceci pour me faire connaître"), not a correlative main-clause head.
- **0 genuine attestations in 57,374,033 chars.** The parent's 0/31.66M
  zero hardens to 0/57.37M. (Rule-of-three 95% upper bound on the
  construction's rate: ~5.2e-8 per char.)

## Per-clause verdict

- **C1 PASS:** 21 new French prose texts added with full provenance.
- **C2 PASS:** 80 texts / 57,374,033 chars > 31,664,431; parent hits replicated.
- **C3 PASS:** 2 new hits, both excluded with stated cause; 0 genuine.

## Verdict: PROMOTE

The claim "the expanded census hardens the zero" is established: the
verbless "ce qui par [N], ceci" correlative remains unattested across
57.37M chars of 1841 French prose, nearly doubling the parent's 31.66M.
The `leftedge-1024-43-governor` fence stays hardened; no licensed parse
under standing values. Scope: corpus result only; adopts the parent's
classification of the 3 replicated hits; no standing/red-team verdict
contradicted or downgraded; §7 intact. OCR caveat: the talleyrand hit
shows OCR can split verbs ("par viendra"), so the exact-regex pass is
conservative in the direction of OVER-matching; the generosity pass and
hand-classification cover the under-matching direction.

## Follow-ups (optional; verdict is promote)

1. `revue-1840-q1-retry` (P5) — retry the failed 1840 vol. 1 `_djvu.txt`
   download (HTTP 500 on 2026-10-09); marginal corpus gain.
2. `cequi-par-german-sweep` (P5) — the German metternich/adb files were
   excluded from the widened French census; a deliberate German-register
   pass could test whether the construction is a Germanism (low value;
   the cipher is French).

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-cequi-par-corpus-widen.md`
- Census: `code/crowd17/next-token/cequi_par_widen_census.py`,
  `code/crowd17/next-token/cequi-par-widen_census.json`
- Corpus additions: 21 files in `code/side-period/corpus/` with
  provenance in `code/side-period/corpus/PROVENANCE.md`
  (2026-10-09 cequi-par-corpus-widen harvest section)
- Queue: `cequi-par-corpus-widen` → `status: verdict`,
  `verdict: {"result": "promote", "report": "code/crowd17/report_inbox/battery-cequi-par-corpus-widen.md", "date": "2026-10-09"}`
  (pre-write assert: queued/verdictless; temp-file + rename; own entry
  only; no downgrade)
- Lock: created on start (agent 0b26fe9e-16f5-4330-8b49-685a2ffa3323,
  2026-10-09T18:20:00Z), deleted on completion.
- R5005, sealed gate instances, red-team adjudication queue untouched.
  No standing/red-team verdict contradicted; §7 intact.
