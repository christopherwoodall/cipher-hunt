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
- **2026-10-07 (attempt 2 — bigram-hypothesis tests, `code/attempt2.py`):** executed.
  Tested H1 (82=m → 16, 11/38) and H2 (87 → 11=la, 7/32) against French
  expectations, with Les Misérables Tome 1 as an independent reference
  (119,514 words; P(la|de)=0.131, P(la|à)=0.098, P(cela|ce)=0.278, P(que|ce)=0.140;
  P(a|m)=0.19, P(e|m)=0.29 — 'a' is NOT the dominant follower of m in French).
  - **H1 (82→16 as "ma", 16="a"): PLAUSIBLE (1/4) — not confirmed.** rank(16)=22 sits
    in the vowel band (e:36, i:70), but P(82|16)=0.39 (16 not bound to m; other
    predecessors 62×4, 12×3, 33×2, 42×2), the mi/me controls are absent
    (82→34=1, 82→40=0 — no letter-spelling pattern), and Les Mis P(a|m)=0.19 is not
    dominant. 16 remains unidentified.
  - **H2 (87="de"/"à"): REFUTED.** 87→46=que occurs **3×** — "de que" and "à que"
    are ungrammatical in French. The two passing checks (rate match, predecessor
    diversity) do not survive the contradiction.
  - **H2b (87="ce"): CONFIRMED (4/5 independent checks).** The very 87→que hits that
    refute de/à are what "ce" predicts: 87→11=**"cela" ×7** with P(11|87)=0.219 ≈
    Les Mis P(cela|ce)=0.278, and 87→46=**"ce que" ×3** with P(que|87)=0.094 ≈ Les Mis
    P(que|ce)=0.140; rank(87)=15 is common-word band; 14 distinct predecessors
    (free function word). The 24-87-46 "est-ce que" trigram did not fire (0×) —
    the one miss. 87=ce joins as a **lane-inferred provisional anchor** (not a
    pencil crib): 8 anchors total.
  - **Drag re-run (8 anchors incl. provisional 87=ce): NULL — still degenerate.**
    All top candidates tie at the quadgram floor (mean −7.714); no discrimination.
    The window-quadgram scorer cannot work at this anchor density either.
  - Erratum to attempt-1 prose: "87→11 in 7/44" quoted P(87|11); the hypothesis-relevant
    rate is P(11|87)=7/32=21.9% (the 44 is the frequency of 11=la itself).
  - Full numeric output: `data/attempt2_results.json`.
- **2026-10-07 (attempt 3 — era-matched reference + H3 64="qui", `code/attempt3.py`):**
  executed. Operator constraint: Les Mis (novel, 1862) mismatches the 1841 diplomatic
  despatch in era AND register. New reference: Tocqueville, *De la démocratie en
  Amérique*, Tomes 1+2 (1835/1840, formal political prose), 214,861 words, fetched from
  Project Gutenberg with provenance (`data/PROVENANCE-tocqueville.txt`, sha256 in
  `data/SHA256SUMS.txt`). Method mirrors attempt 2 (same tokenizer, same factor-2 band).
  - **Era-vs-LesMis rate comparison** (the point of the exercise): P(que|ce) 0.108 vs
    0.140 ✓ agree; P(qui|ce) 0.188 vs 0.118 ✓ agree (era *closer* to the cipher's 0.156);
    P(la|de) 0.192 vs 0.131 ✓; P(la|à) 0.128 vs 0.098 ✓. **One disagreement:**
    n("cela")/n("ce") is 0.041 in Tocqueville vs 0.278 in Les Mis — a 6.7× register gap
    (novels use "cela" in dialogue; formal prose almost never does). The cipher's
    P(11|87)=0.219 sits with Les Mis, not Tocqueville.
  - **87=ce re-validated vs era: CONFIRMED (3/4).** Rank band, P(que|87)=0.094 ≈ era
    P(que|ce)=0.108, and 14 distinct predecessors all still pass. The "cela"-rate leg
    now FAILS the factor-2 band against the era corpus (0.219 vs 0.041) and is downgraded
    to register-dependent — it does not overturn the confirmation (the grammatical
    refutation of 87="de"/"à" and the other legs stand), but attempt 2's 4/5 is now 3/4
    on era-matched rates. Noted as a caveat, not a refutation.
  - **H3 (64="qui"): CONFIRMED (4/4) → 9th anchor (provisional, lane-inferred).**
    (a) rank(64)=4 of 96 groups; era rank("qui")=13 — top-word band. (b) P(64|87)=0.1562
    ≈ era P(qui|ce)=0.1878 — and "qui" is the #1 follower of "ce" in Tocqueville (213×),
    ahead of "que" (122×). (c) 46=que → 64 = 0: no "que qui" (negative control holds).
    (d) 64 has 28 distinct followers / 28 distinct predecessors, top follower share 0.07 —
    a free function word, not a fixed phrase. Rival reading 64="ci" ("ceci"=87+64):
    P(87|64)=0.109 — 64 is not ceci-bound, favouring "qui" (diverse contexts).
  - **Bonus (STATE.md next):** 82→16 occurs 11× total, **0× with 87=ce within ±3 groups**
    — the 82→16 bigram avoids ce-windows entirely. Datum only; suggests re-examining
    82→16 in qui-anchored windows next.
  - **Drag re-run (9 anchors incl. provisional 64=qui): NULL — still no discrimination.**
    Technical note: the anchors-only baseline now lifts off the quadgram floor on some
    windows (density finally registering), but every (group, word) candidate still ties
    at the floor — zero separation between candidates. The window-quadgram scorer remains
    shelved; attempt 4 should consider a syllable-level scorer.
  - Full numeric output: `data/attempt3_results.json`.

## Null results
- **N1 (2026-10-07):** crib-anchored function-word drag (Phase C above) — degenerate at 7-anchor
  sparsity; all candidates tie at floor. Not a disproof of the crib-anchored strategy, only of
  this scorer at this sparsity.
- **N3 (2026-10-07):** drag re-run with 9 anchors (7 pencil cribs + provisional 87=ce +
  provisional 64=qui) — still null. Anchors-only baseline lifts off the quadgram floor
  on some windows (anchor density finally registering), but no (group, word) candidate
  separates from the floor. The window-quadgram crib-drag stays shelved; a syllable-level
  scorer is the candidate replacement.

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
- F6 (2026-10-07, this lane): **87="ce" — lane-inferred provisional anchor, CONFIRMED 4/5.**
  87→11="cela" ×7 (P=0.219 ≈ Les Mis P(cela|ce)=0.278) and 87→46="ce que" ×3 (P=0.094 ≈
  Les Mis P(que|ce)=0.140); rank 15; 14 distinct predecessors. The rival readings 87="de"/"à"
  are REFUTED by 87→que ×3 ("de que"/"à que" ungrammatical). Status: provisional anchor
  (not pencil-crib); 8 anchors total. Evidence: `code/attempt2.py`, `data/attempt2_results.json`.
- F7 (2026-10-07, this lane): H1 (82→16 as "ma", 16="a") **not confirmed** — PLAUSIBLE (1/4):
  rank(16)=22 in vowel band, but P(82|16)=0.39, mi/me controls absent (82→34=1, 82→40=0),
  Les Mis P(a|m)=0.19 not dominant. 16 unidentified. Evidence: same as F6.
- F8 (2026-10-07, this lane, erratum): attempt-1 prose "87→11 in 7/44" quoted P(87|11);
  the correct hypothesis rate is **P(11|87)=7/32=21.9%**. Raw counts in
  `data/attempt1_results.json` were always correct; only the prose ratio is corrected.
- F9 (2026-10-07, this lane): **64="qui" — lane-inferred provisional anchor, CONFIRMED 4/4.**
  87→64 ×5 ("ce qui"); P(64|87)=0.1562 ≈ era P(qui|ce)=0.1878 ("qui" is the #1 follower
  of "ce" in Tocqueville, 213×); rank(64)=4 of 96 vs era rank("qui")=13; 46=que → 64 = 0;
  28 followers/28 predecessors, top share 0.07. Rival 64="ci" disfavoured (P(87|64)=0.109).
  9 anchors total. Evidence: `code/attempt3.py`, `data/attempt3_results.json`.
- F10 (2026-10-07, this lane): **era-matched reference corpus built** (Tocqueville 1835/1840,
  214,861 words, formal prose). Rate comparison vs Les Mis (1862 novel): P(que|ce),
  P(qui|ce), P(la|de), P(la|à) all agree within factor 2; **n("cela")/n("ce") disagrees
  6.7×** (0.041 era vs 0.278 Les Mis) — a register gap, not an era subtlety. Consequence:
  attempt 2's "cela"-rate leg for 87=ce is downgraded to register-dependent; 87=ce
  re-validates at 3/4 on era rates and stands. Evidence: `data/PROVENANCE-tocqueville.txt`,
  `data/attempt3_results.json`.

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
This lane's outputs: `code/crib_attack.py`, `data/attempt1_results.json`,
`code/attempt2.py`, `data/attempt2_results.json`.
French reference text (Les Misérables Tome I, Project Gutenberg ebook 17489), copied
2026-10-07 from sibling lane catherine-medici-1567/data/gutenberg-17489-miserables1.txt
for independent bigram/word-rate checks (attempt 2):
  a5de514ba7b9f2e1  data/gutenberg-17489-miserables1.txt (first 16 hex of sha256; full hash in SHA256SUMS.txt)
Era-matched reference corpus (attempt 3, 2026-10-07) — Tocqueville, *De la démocratie
en Amérique*, Tomes 1+2 (French, 1835/1840), formal political prose, 214,861 words.
Supersedes Les Mis as the rate reference (era + register match to the 1841 despatch):
  fafebe4f69bc8e7abc6ed95bd10c2257bd26a307b2c1071056187ef76154aeaa  data/gutenberg-30513-tocqueville-t1.txt
  20e46d72bc398f1c903449908a35a691e0d32763234bc75b2376cd21dbe33ee9  data/gutenberg-30514-tocqueville-t2.txt
  (provenance: data/PROVENANCE-tocqueville.txt; hashes appended to data/SHA256SUMS.txt)
Attempt 3 outputs: `code/attempt3.py`, `data/attempt3_results.json`.
