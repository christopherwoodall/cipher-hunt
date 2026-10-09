# Battery `ceci-correlative-corpus` — verdict: NULL (fence hardened)

## Bar (verbatim, pre-registered)

"corpus test: does 'ce qui par [N], ceci' occur as a correlative frame in 1841 prose? Bar: >=1 genuine attestation licenses the chunk; confirmed zero hardens the fence."

## Bar restated (numbered, before testing)

- **C1:** ≥1 genuine attestation of the verbless "ce qui par [N]" + "ceci" correlative frame in 1841 diplomatic prose → the chunk licenses.
- **C2:** confirmed zero → the `leftedge-1024-43-governor` fence hardens.

Adverses: none listed.

## Method

Byte-exact corpus census over the lane's period prose corpus (`code/side-period/corpus`, 63 texts, 31,664,431 chars — same corpus family as the vient/gerund corpora). Regex `ce\s+qui\s+par\b` (whitespace-normalized) found all "ce qui par" occurrences; each was hand-classified against the genuine criterion: a VERBLESS "ce qui par [N]" chunk followed by "ceci" heading the main clause, i.e. the cipher's frame "45 64 96 43 87 01" as a correlative. Generosity pass: "qui\s+par\b" with "ceci" anywhere in the following ~600 chars. Script: census in `code/crowd17/next-token/ceci-correlative_census.json`; generosity in `code/crowd17/next-token/ceci-correlative_generosity.json`. `canonical.py` never used (corpus test, not stream).

## Findings

- **Exact "ce qui par": 3 occurrences in 31,664,431 chars.** All hand-classified:
  1. **metternich-papiere-v4.txt @1285388** — "…difficile à renverser et même à remuer, **ce qui par cela même doit les contrarier** beaucoup." Relative "ce qui" + adjunct "par cela même" + FINITE VERB "doit". Not verbless; no "ceci". Excluded.
  2. **metternich-papiere-v4.txt @1412212** — "…toute circonstance **qui par la suite pourrait** vous aider dans vos observations." Relative + adjunct "par la suite" + finite "pourrait". Not verbless; no "ceci". Excluded.
  3. **metternich-papiere-v6.txt @1071660** — "**Ce qui par contre est vrai**, c'est que les mouvements ne se ressemblent pas." Free relative WITH finite verb "est" + c'est-cleft. This is the licensed correlative shape — and it requires the finite verb. The cipher chunk is verbless; hit 3 therefore demonstrates the licensing condition the cipher chunk violates, not the chunk itself. Excluded with cause.
- **Generosity: 0.** No "qui par" anywhere in the corpus is followed by "ceci" within the ~600-char window.

## Per-clause verdict

- **C1 FAIL:** 0 genuine attestations of the verbless "ce qui par [N], ceci" correlative.
- **C2 FIRES:** confirmed zero hardens the fence. The verbless-left-edge venue stays fenced as the red-team recorded it; no licensed parse under standing values, now with a 31.66M-char corpus zero behind it (corpus-wide, not just register-level suspicion).

## Scope

Corpus result only. No standing/red-team verdict contradicted or downgraded (adopts R19-045 43=noun-class, R19-046 par-43 value hunt open, the leftedge-1024-43-governor NULL fence); §7 intact. The zero does not kill the "par nature" adjunct arm (needs 43's value named, red-team venue); it hardens the verbless correlative specifically. Canonical-stream caveat stands for the cipher-side loci only.

## Follow-ups proposed (for supervisor queuing)

1. `ceci-correlative-comedy` (P4) — test the verbless "ce qui par [N], ceci" correlative in the 28-play drama corpus; dialogue-ellipsis could license there what prose never does (the drama-register precedent from the gov-excl-inf family).
2. `cequi-par-corpus-widen` (P4) — expand the prose census with more 1841 diplomatic texts to harden the zero beyond 31.66M chars.
3. `verbless-cequi-relatives` (P3) — census all verbless "ce qui" + prepositional-phrase heads in the cipher stream against sentential licenses; decides whether the verblessness itself is systematic beyond the "par" geometry.

## Standing state

No standing/red-team verdict contradicted or downgraded. §7 intact (67 sole polyvalence). Adverses answered: none listed.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-ceci-correlative-corpus.md`
- Census: `code/crowd17/next-token/ceci-correlative_census.json`, `code/crowd17/next-token/ceci-correlative_generosity.json`
- Queue: `ceci-correlative-corpus` → `status: verdict`, `result: null`, 2026-10-09
- Lock created on start, deleted on completion (verified below).
- R5005, sealed gates, red-team adjudication queue untouched.
