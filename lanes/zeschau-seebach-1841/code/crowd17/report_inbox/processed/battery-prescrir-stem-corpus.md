# Battery `prescrir-stem-corpus` — verdict: PROMOTE (census complete, finding grade)

## Pre-registered bar (verbatim)
"census the prescrir- stem across all period corpora."

Numbered clauses:
- **C1**: complete census of the prescrir- stem across all period corpora, with byte-exact counts, distributional table, and the 'prescrire de' lemma check → PASS.

## Method
- Corpus: `code/side-period/corpus` — 75 `.txt` files, 34,525,238 characters.
- Text normalized (NFKD strip accents, lowercase); regex `\bprescr[ie][itvr][a-z]*\b` catches all finite forms, participles, gerunds, infinitives.
- Re-ran and saved as `code/crowd17/next-token/prescrir_census.py` → `prescrir_census.json` (197 hits with file, offset, token, ±context).
- `canonical.py` never used; corpus bytes only (corpus test, not a stream test — no R5005 contact).
- Hand-audited all 5 hits with "de"-follow and all 5 with "de/à/pour"-precede.

## Findings
- **197 hits across 25 files.** Token distribution: prescrit ×66, prescrire ×34, prescrites ×31, prescrite ×16, prescrivent ×13, prescrivait ×12, prescrivit ×7, prescrivaient ×6, prescrivant ×4, prescrits ×3, prescrivirent ×3, prescrivez ×1, prescrira ×1.
- Top files: guizot-memoires-t5-t6 ×30, pozzo-di-borgo-correspondance-v1 ×24, guizot-memoires-t3-gutenberg ×22, revue-deux-mondes-1841-q2 ×16, levant-correspondence-1841-p3 ×15, guizot-memoires-t1-gutenberg ×13, revue-deux-mondes-1841-q4 ×13.
- **The 'prescrire de' lemma is wholly absent: 0 constructions.** No prescrir-form governs "de"/"d'" + infinitive anywhere in 197 hits (precise regex match: 0/197).
- The 5 "de"-after hits are partitives, not government: "prescrit des vertus" (guizot-memoires-t2 @716730), "prescrivaient de sa situation" (guizot-memoires-t3 @71302), "prescrites de Paris" (guizot-memoires-t3 @833047), "prescrivant du fardeau de la dette" (nesselrode-v10 @178301), "prescrites de ceux qui la connaissent" (pozzo-di-borgo-v1 @951464).
- The 5 "de/à/pour"-before hits are noun complements or pour-infinitives, not verb-government of "de": "des erreurs de prescrire" (metternich-papiere-v4 @1096055 — noun complement), "pour prescrire" (guizot-memoires-t3 @88317 — pour-infinitive), "de … prescrivant" (nesselrode-v10 @178301 — gerund), "l'esprit de prescrite" (pozzo-di-borgo-v1 @927246 — noun + participle), "l'ordonnance de prescrite" (revue-deux-mondes-1841-q2 @2434368 — noun + participle).
- Side count (lemma context only): "prescription" noun ×7 stream-wide; not parsed as lemma evidence.

## Scope
- Census only. No class, value, split, or polyvalence named; no standing/red-team verdict contradicted or downgraded; §7 intact.
- Closes the 'prescrire de' lemma question stated in the target claim (0 constructions). Consistent with `ne-1330-lexical-trio` (trio verbs do not license bare-'ne' government; licensed class = 7 verbs). No follow-ups required per §4 (promote).

## Bookkeeping
- Report: `code/crowd17/report_inbox/battery-prescrir-stem-corpus.md`
- Script + data: `code/crowd17/next-token/prescrir_census.py`, `code/crowd17/next-token/prescrir_census.json`
- Queue: `prescrir-stem-corpus` → `status: verdict`, `result: promote`, 2026-10-09 (pre-write assert: was queued/verdictless; temp-file + rename; own entry only; no downgrade)
- Lock created on start, deleted on completion. R5005, sealed gates, red-team adjudication queue untouched.
