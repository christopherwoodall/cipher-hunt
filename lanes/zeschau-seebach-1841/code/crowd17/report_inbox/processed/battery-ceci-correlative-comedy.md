# Battery `ceci-correlative-comedy` — verdict: NULL (fence hardened at drama register)

## Target
- id: `ceci-correlative-comedy` (P4)
- Claim: test the verbless 'ce qui par [N], ceci' correlative in the 28-play drama corpus; dialogue-ellipsis could license there what prose never does.
- Parent: `ceci-correlative-corpus` (2026-10-09, NULL) — 31.66M chars of 1841 prose gave confirmed zero (3 "ce qui par" hits, all hand-excluded: two with finite verbs, one c'est-cleft requiring the finite verb the cipher chunk violates); generosity pass = 0.

## Bar (verbatim, pre-registered)

"test the verbless 'ce qui par [N], ceci' correlative in the 28-play drama corpus."

## Bar restated (numbered, before testing)

- **C1:** ≥1 genuine attestation of the verbless "ce qui par [N], ceci" correlative in the drama corpus → dialogue-ellipsis licenses the chunk; the pairing re-opens.
- **C2:** confirmed zero → the fence hardens at register level (not even drama dialogue licenses it).

Adverses: none listed.

## Method

Verbatim replication of the parent's census, register changed (prose → drama):
1. Drama corpus = all French play files in `code/side-period/corpus`: delavigne ×3, dumas ×6, hugo ×8 (hernani in two editions), musset ×2 (comedies-proverbes omnibus = multiple plays), scribe ×5, vigny ×1, labiche ×13, ponsard ×1 = **39 files, 5,962,742 bytes** (~5.9M chars). Note: the target's "28-play" label undercounts the on-disk set (26 non-labiche files, with the musset omnibus holding ~3 plays = 28; the 13 labiche comedies are tested too — a superset zero is strictly stronger).
2. Regex `ce\s+qui\s+par\b` (case-insensitive, whitespace-normalized) → strict hits; each hand-classified against the genuine criterion: a VERBLESS "ce qui par [N]" chunk followed by "ceci" heading the main clause.
3. Generosity pass: `qui\s+par\b` with `\bceci\b` anywhere in the following ~600 chars.
4. Script + data: inline census this run; hits JSON at `code/crowd17/next-token/ceci-correlative-comedy_census.json`. `canonical.py` never used (corpus test, not stream). Provenance: corpus files per `code/side-period/corpus/PROVENANCE.md`.

## Findings

- **Strict "ce qui par": 0 occurrences in 5,962,742 chars.**
- **Generosity: 0.** 7 "qui par\b" hits exist in 6 files; none is preceded by "ce", none is followed by "ceci" within 600 chars. "ceci" occurs 166× in the drama set — the pairing simply never co-occurs.
- All 7 "qui par" hits hand-classified (offsets in normalized text):
  1. **delavigne-paria.txt @99251** — "Ces fleurs, qui par leur deuil m'avaient prédit mon sort" — relative "qui" + adjunct "par leur deuil" + FINITE "avaient prédit". Not verbless; no "ceci". Excluded.
  2. **dumas-mariage-louis-xv-1841.txt @35228** — "des gens qui par-lent l'iroquois" — hyphenation artifact ("parlent" split across a line break). Not "par" at all. Excluded.
  3. **musset-comedies-proverbes-1850.txt @69945** — "ceux qui par-tent ensemble" — hyphenation artifact ("partent"). Excluded.
  4. **scribe-bertrand-et-raton.txt @6169** — "qui par les bontés de son roi ... élevé" — "qui" + adjunct "par les bontés" + participle "élevé" (reduced relative, still verbal). Not verbless; no "ceci". Excluded.
  5. **scribe-bertrand-et-raton.txt @23743** — "moi ... qui par conséquent ne conspirerai pas" — "qui" + "par conséquent" + finite "ne conspirerai pas". Not verbless; no "ceci". Excluded.
  6. **scribe-charlatanisme.txt @56621** — "Et qui par d'autres sollicite" — "qui" + adjunct "par d'autres" + finite "sollicite". Not verbless; no "ceci". Excluded.
  7. **scribe-le-lorgnon.txt @27725** — "conseil ... qui par l'évènement n'était pas si mauvais" — "qui" + adjunct + finite "n'était". Not verbless; no "ceci". Excluded.
- The genuine criterion (verbless "ce qui par [N]" + "ceci" heading the main clause) is met by **0/7** candidates. Dialogue-ellipsis does not license the frame anywhere in the drama register.

## Per-clause verdict

- **C1 FAIL:** 0 genuine attestations.
- **C2 FIRES:** confirmed zero hardens the fence. Combined with the parent's prose zero: **0 genuine in ~37.6M chars across both registers** (31.66M prose + 5.96M drama). The verbless-left-edge venue stays fenced; no licensed parse under standing values.

## Scope

Corpus result only. No standing/red-team verdict contradicted or downgraded (adopts R19-045 43=noun-class; the leftedge-1024-43-governor NULL fence stands; "par nature" adjunct arm still needs 43's value named, red-team venue); §7 intact. The zero does not test the cipher stream directly; it closes the register-escape route the parent's follow-up proposed.

## Follow-ups proposed (for supervisor queuing; parent's other two follow-ups already queued)

1. `cequi-par-dialogue-ellipsis-scope` (P4) — test whether drama dialogue-ellipsis licenses verbless relative heads with OTHER prepositions ("ce que", "ce dont", "ce à quoi" heads); decides whether the verblessness gap is "par"-specific or general across prepositions. Evidence: this report's 0/7 classification.
2. `hyphenation-artifact-audit-drama` (P4) — methodological: 2 of the 7 "qui par" hits were line-break hyphenation splits ("par-lent", "par-tent"); audit hyphenation-artifact rates in the drama corpus to calibrate false-positive rates for future word-boundary regex censuses. Evidence: hits 2–3 above.

## Standing state

No standing/red-team verdict contradicted or downgraded. §7 intact (67 sole polyvalence). Adverses answered: none listed.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-ceci-correlative-comedy.md`
- Census: `code/crowd17/next-token/ceci-correlative-comedy_census.json`
- Queue: `ceci-correlative-comedy` → `status: verdict`, `result: null`, 2026-10-09 (pre-write assert passed — was queued/verdictless; temp-file + rename; disk re-validated; own entry only; no downgrade)
- Lock created on start (2026-10-09T18:17:06Z, no stale lock), deleted on completion (verified below).
- R5005, sealed gates, red-team adjudication queue untouched.
