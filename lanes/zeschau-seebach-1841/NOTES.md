# NOTES — zeschau-seebach-1841

## Objective
Break the Zeschau → Seebach two-digit syllabary (DECODE R5005, 18 Jan 1841; siblings R5006–R5008).
Nobody has tried a **crib-anchored attack**: pin the seven pencil-crib values
(11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que) and run a constrained search over the
two-digit syllabary scored against a **French** syllable model (R5005 is French, not German),
exploiting the long repeats (`7778948206` ×5, `06777818711001` ×3) as probable names/set phrases.

## Methodology log
- **2026-10-07 (lane stand-up):** Read catalogue entry #47 and Bourdeau's dedicated page
  (https://dbourdeau.github.io/cyphersolver/zeschau1841.html). Corrections to the catalogue
  one-liner: R5005's language is **French** (two sibling letters are German); there are **seven**
  crib values, not three (11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que); the pencil reads
  "la pre m i er e" = *la première* plus "que" over 46. Upstream transcription + author's solver
  scripts located at github.com/dbourdeau/cyphersolver `targets/zeschau1841/`; fetching
  `ct_R5005.digits.txt`, `ct_R5005.txt`, `NOTES.md`, `offsets.json`, `profile.json`,
  `hsolve.py`, `syll.py`, `syll2.py`, `syll3.py` with provenance (see Data inventory).
- **2026-10-07 (attempt 1 — crib-anchored attack, `code/crib_attack.py`):** executed, three phases.
  - Phase A (verification): transcription = 70 lines, **3,764 digits** → 1,846 pairs after applying
    upstream per-line offsets (32 lines offset 1; 28 odd-digit lines), 96 distinct groups — matches
    upstream's 96/100 claim. **Discrepancy:** the web page claims 3,969 digits; the sha256-verified
    transcription files contain 3,764. Recorded as observed; not "corrected".
  - All seven crib groups present: 11=la ×44 (freq rank 6), 70=pre ×15 (rank 56), 82=m ×38 (rank 8),
    34=i ×10 (rank 70), 29=er ×47 (rank 2), 40=e ×21 (rank 36), 46=que ×29 (rank 19).
    29=er at rank 2 is consistent with 'er' as a top French syllable. Group-stream IC = 0.0142
    (flat over 96 groups ≈ 0.0104) — mild structure, as expected for a syllabary.
  - **Repeat claim corrected:** pair-aligned `77 78 94 82 06` occurs **2×**, not 5×;
    `06 77 78 18 71 10 01` occurs **0×**, not 3×. Raw digit-substring counts are 4 and 1 —
    the extra hits sit at odd digit-phase, i.e. artefacts of substring counting across pair
    boundaries, not true group repeats. Upstream's "×5 / ×3" does not survive pair alignment.
  - Phase B (anchor-context profiling): strongest bigram is **82→16 in 11/38 cases (29%)** —
    lead for attempt 2. **87→11 in 7/44** ("87 la", possibly a de/à+la construction). After
    46=que the followers are diffuse (no dominant word). The two true repeat occurrences sit in
    varying running text (contexts differ on both sides).
  - Phase C (function-word drag): **NULL — method degenerate.** With 7 anchors covering ~11% of
    groups, decoded ±6-group windows contain too few known letters; all 1,000+ (group, word)
    candidates scored exactly at the quadgram floor (−7.714), identical to the anchors-only
    baseline. Zero discrimination. Best windows were bare concatenations ('vousla', 'toutee').
    Verdict: window-quadgram crib-drag cannot work at this anchor sparsity. Shelved, not retried
    without denser anchors or a different scorer.
  - Full numeric output: `data/attempt1_results.json`.

## Null results
- **N1 (2026-10-07):** crib-anchored function-word drag (Phase C above) — degenerate at 7-anchor
  sparsity; all candidates tie at floor. Not a disproof of the crib-anchored strategy, only of
  this scorer at this sparsity.

## Verified findings
- F1 (source: Bourdeau zeschau1841 page, 2026-09-21/24): the unit is pairs of digits; 96 of 100
  possible groups occur; ~1/3 of lines have odd digit counts so groups run over line breaks;
  division into pairs fixed by strongest pair statistics. Status: accepted as upstream methodology.
- F2 (source: same): seven pencil-crib values — 11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que.
  Status: accepted as ground truth anchors.
- F3 (corrected 2026-10-07, this lane): the long repeats are **2×** (`77 78 94 82 06`) and **0×**
  (`06 77 78 18 71 10 01`) at pair alignment — upstream's ×5/×3 counts include misaligned
  substring artefacts. Evidence: `code/crib_attack.py` Phase A, `data/attempt1_results.json`.
- F4 (2026-10-07, this lane): transcription holds **3,764 digits**, not the 3,969 the page claims.
  Evidence: sha256-verified `data/upstream-ct_R5005.digits.txt` (3,764 digit chars) and
  `data/upstream-ct_R5005.txt` (same).
- F5 (2026-10-07, this lane): bigram **82→16 occurs 11/38 (29%)** — the strongest anchor-adjacent
  pattern in the text; candidate anchor-hypothesis for attempt 2. Evidence: Phase B output.

## Data inventory
Source: https://github.com/dbourdeau/cyphersolver `targets/zeschau1841/` (Daniel Bourdeau's
transcription + solver scripts for the 2026-09-21 write-up). Retrieved 2026-10-07 ~06:10 UTC
via GitHub API + raw.githubusercontent.com (curl). Original page:
https://dbourdeau.github.io/cyphersolver/zeschau1841.html (posted 2026-09-21, updated 2026-09-24).
sha256:
  adc23d961e59a76a1040ae712f5b169720e7cf63eecd7fafe01df04ee7f34c42  upstream-NOTES.md
  18d48ccdca83fe5133b840cd427d5b89046839c866441d1c7c06fc264493e73f  upstream-ct_R5005.digits.txt
  6db0807ff5b42f8bcc294409f99ca92f08e748dccb6c293c1a31bd766bc48069  upstream-ct_R5005.txt
  dae94eb60077a5cb3f383e0c2ce238d3f8c32a3804e3ba41f2ea1c24a2697fa1  upstream-hsolve.py
  6abc844c805d9d16567153c293793b3cb2a6f84e83886c7f20b5b3c3fa6de36c  upstream-offsets.json
  e4ad7f831744385f286bba9cb8dceb3d50f7cf769b8fd87ee3ee2ecea9e18ce6  upstream-profile.json
  e4be9e77a7cadf610cae077e9a92a83813cf068857132ca3ccff95155cfceae1  upstream-syll.py
  6268c218f607143617c60d701f95c9103c88b59114aae0ae2306ec786cf2bfb9  upstream-syll2.py
  ac94a73a3603ab8b665ce4b6e4e121ee527de9da55b40392ab1d8e513cdcee04  upstream-syll3.py
Copied from sibling lane catherine-medici-1567/data/french-quadgrams.json (French letter-quadgram
model built 2026-10-07 for that lane; reused as scorer here):
  a7ef886356b67030d6984dca3556568a5551fc97833fda69438515b4d1de843f  french-quadgrams.json
This lane's outputs: `code/crib_attack.py`, `data/attempt1_results.json`.
