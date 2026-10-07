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
  - Phase A (verification): transcription = 70 lines, **3,764 digits** → 1,847 pairs after applying
    per-line offsets (repaired canonical parse, F32 — supersedes the 1,846-pair upstream-EM parse;
    `code/side-keyhunt/repaired_offsets.json` is now canonical), 96 distinct groups. **Discrepancy:** the web page claims 3,969 digits; the sha256-verified
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
- **2026-10-07 (crowd round — 9 executors, coordinator-curated):** nine diverse
  attackers fanned out in parallel, each writing only to `code/crowd/<name>_results.{md,json}`;
  the coordinator verified every merged claim against the lane data before recording.
  - **Phonotactician** (constrained syllabary search, French syllable-structure scorer,
    8 anchors pinned): NULL — the optimizer beat baselines by +2798 (uniform) / +3578
    (freq-matched) but degenerately: best key uses 4 syllables for all 88 free groups
    (`champmatmatchamphi…` soup); only 1/88 groups stable ≥0.75 across restarts.
    Verdict: scorer exploited, no signal. (`code/crowd/phonotactician.py`)
  - **Crib Surgeon** (positional attack on "la première"): the full 6-group sequence
    11-70-82-34-29-40 occurs **exactly once @pair 1033 (56.0%)** [old parse; SUPERSEDED by
    F32 — repaired parse: TWICE, @pairs 754 and 1034], mid-letter in a
    back-reference context (`…87(ce) 01 03 29(er) 80 77 | la-pre-m-i-er-e | 17 77
    82(m) 63 11(la) 67…`) — "la première [fois/lettre]". Zero near-misses. Three
    value hypotheses (≥2 checks each, none promoted): **H1 24="est" (strong, 4 checks:**
    rank-1 band, P(ce|24)=0.192 vs 1.7% base, "qu'est" elision ×3; anomaly: "est cela"
    ×3), **H2 77="pas" (3 checks**; caveat: rival "ne"-like predecessor 67→77 ×6),
    **H3 06="ne" (3 checks)**. The 5-group chain 64-96-43-87(ce)-01 recurs ×2
    (@341, @1024) — positional hard constraint, no value assigned.
  - **Contactor** (contact-chain clustering, 96 groups): **3-phase rotational contact
    structure A→C→B→A** — P(A→C)=0.418, P(C→B)=0.450, P(B→A)=0.476 (all 1.35–1.52×
    over independence), chi-square=181.3 on 4 df (p≪1e-6), self-transitions suppressed
    (0.51–0.74×). 29=er anchors phase C (word-final-ish: prev-A 0.77, next-B 0.89).
    Both pre-registered predictions FAILED as stated (P1: 34=i/40=e vowel-class
    contacts; P2: 87 function-word-like) — but 40=e is 34=i's 2nd-nearest anchor
    (Jaccard 0.241) and **87's nearest anchor is 82=m at Jaccard 0.423** (highest
    anchor-anchor value by far; shared C→X→A block signature) — compatible with 87=ce
    as proclitic, but a caution flag since 87 doesn't pattern with la/que.
  - **Red Team** (kill authority over 87=ce): **VERDICT — WEAKENED, demote to
    PLAUSIBLE/provisional.** All attempt-2 counts reproduce, but the scorecard is
    unsound: check (b)'s "P(cela|ce)=0.278" was **n_cela/n_ce, a count ratio, not a
    conditional** — the honest syllable-level bound is P("la"|"ce"-syllable) ≤ 0.1805,
    and observed 0.2188 *exceeds* it (check void); checks (a)/(d) also passed for the
    refuted de/à (non-discriminating); check (c) is n=3, Wilson CI [0.032,0.242]
    (weak). New reframing: **P(46|87,pre=96)=3/3 vs P(46|87,pre=24)=0/10** — the "que"
    is licensed by predecessor 96, never 24. If 24=est (surgeon's H1), the 24-87-46
    0/10 becomes a joint contradiction (binomial p=9.1e-04 under Les Mis rates).
    No alternative beats ce ("pour" loses honestly, "sans" refuted, de/à refutation
    upheld) — the kill fails on alternatives, succeeds on scorecard integrity.
  - **Drag Racer** (function-word drag v2, syllable-level scorer): PARTIAL — the
    syllable scorer discriminates where letter-quadgrams tied (54/55 distinct scores,
    no floor degeneracy), but the discrimination is **word-prior, not placement**:
    at 12.8% anchor sparsity the best window for ~half the candidates is the isolated
    word (best == chain prior for 26/55). Only exact multi-anchor placement is
    cela=87-11 ×7. Model-free corroboration: 87 is the #1 predecessor of 11
    (P=0.219); ce-la observed 7 vs E=0.7 (z=+7.6). Independently caught attempt-2's
    ratio error (true cross-word P(la|ce)=0.022 — the cipher is ~10× cela-denser
    than Tocqueville; register note, not anchor refutation). Granularity warning:
    cipher cells include single letters m/i/e and hyper-frequent "er" (rank 3),
    which hyphenation-based syllable units almost never emit — er/m/i/e bigram
    expectations are uncalibrated (v1 z=+33..+101 retracted as artifact).
  - **Historian** (archive-side research): key NOT FOUND in any published source —
    but both blockers now have concrete resolutions (see F14). DECODE registration is
    free and self-service; HStAD Dresden accepts mail-in scan orders.
  - **Formula Hunter** (repeat census at pair alignment): repeats are **discourse-level
    set phrases, not letter-framing formulas** — 13/16 long repeats (L≥5) are
    body/body; **no repeat is exclusive to the opening or closing 100 groups**.
    Longest repeat `56 69 26 00 33 21 64 37 01` ×2 @931/@1625 (unread — top crib-drag
    target). `96 87 46` ×3 ("parce que"/"de ce que", unchecked). `24 87 64` ×3
    ("[pour|en] ce qui" — blocked on attempt-3's 64="qui"). `77 78 94 82 06` ×2
    re-verified @1179/@1350 ("-ment/-nement" word family, weak). Nulls: no Dresde /
    Saint-Pétersbourg / janvier / title evidence by repetition; `06 77 78 18 71 10 01`
    re-verified 0×; `24 87 46` = 0×.
  - **Annealer** (24 restarts × 60k iters, 8 anchors pinned, syllable-bigram scorer):
    **method-broken-on-control → NULL.** Synthetic control recovers **1/88 planted
    assignments (≈chance)**; the planted true key scores −5.36 per-pair logp while the
    annealer's "best" nonsense scores −2.90 — the scorer's global optimum sits ~2.5
    nats/pair *above* real French. Stability table shows the degeneracy: ~20 groups
    collapse to "de" at 20–24/24 recurrence. Same failure mode as Bourdeau's syllable
    solvers ("drift to fluent nonsense"), now proven by control rather than inferred.
  - **Linguist** (1841 French priors): **register mismatch with Les Mis is more
    dangerous than era mismatch** — a despatch is first-person formulaic administrative
    French; Les Mis is third-person narration + dialogue + argot. Orthography is
    post-1835/pre-1878 (cribs must read "collége", "poëte", "asyle"); "cela" beats
    "ça" 47:1 in 1835–1850 print ("ça" ≈ absent from diplomatic register).
    Syllable tiers from Meisel 1826 diplomatic corpus (98k words); diplomatic formulae
    with syllable segmentations (openings, closings, "Par ma dépêche du…", "En réponse
    à la dépêche de Votre Excellence du…"). New crib HYPOTHESIS: the ×5 repeat
    `77 78 94 82 06` = **"J'ai l'honneur de"** (5 syllable units: j'ai·l'·hon·neur·de;
    test the l'-position as a single-letter consonant, check hon–neur adjacency).
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

- **2026-10-07 (crowd round 2 — 6 executors, coordinator-curated):** fresh diverse cast
  on the round-2 work orders; each wrote only to `code/crowd2/` plus a report-inbox
  note per REPORTING.md (Context/Decision/Why/Enlightenment). The coordinator
  re-derived every headline cipher-side number against the lane data before merging —
  all verified: 24 freq 52 rank 2/96 (00 leads at 54); P(87|24)=10/52=0.1923;
  P(24|46)=3/29=0.1034; 24-87-64 ×3; 96-87-46 ×3 with P(87|96)=3/21=0.1429;
  64-96-43-87-01 ×2; 82→16 11× with 0 within ±3 of 87; 77-78-94-82-06 ×2;
  11→24 ×4; P(77|06)=6/46=0.1304; 9-mer 56…01 ×2 @931/@1625.
  - **Closer** (WO1 — resolve 24="est", must also refute): **REFUTED.** All four H1
    checks re-graded on era rates: rank "1" was 0-based (24 is rank 2/96);
    P(ce|24)=0.1923 vs era P(ce|"est")=0.0099 = 19.5× fail; "qu'est" ×3 never
    rate-checked: P(24|46)=0.1034 vs era 0.0014 = 74× fail. Refutation legs:
    C-check structural/instrument-independent ("que"+"est" ungrammatical outside
    "qu'est-ce", fails 6.6× even under Les Mis); predecessor kill — top predecessor
    of 24 is 11=la ×4, "la"+"est"=0 in both corpora. Rivals scored honestly:
    sont/ont dead, c'est dead 5×/30×, de dead 11.5× + "la de"=0, en dead 26×/4.8×.
    Inversion sweep (45 function words): no era word satisfies
    P(ce|V)≈0.19 ∧ P(V|que)≈0.10 — intersection empty, itself a lead pointing back
    at provisional 87=ce. "est cela"×3 anomaly moot. Methodology finding: the
    "est ce" bigram family has an 11.9× Les-Mis/Tocqueville register gap — larger
    than F10's cela gap; per-bigram caveats needed for dialogue-driven bigrams.
  - **Formula Tester** (WO2): **H5 "J'ai l'honneur de" REFUTED as stated** —
    kill-grade: position 4 is 82='m' (ground-truth pencil anchor), the phrase needs
    "neur". Rates bury it independently: 82 at 2.06% is 67× too frequent for tier-3
    "neur" (era 0.031%); 94 at 1.95% is 184× too frequent for "hon" (era 0.011%);
    77=j'ai 47× over era. Surviving sub-claims: 77→78 "j'ai l'" bound chunk (7×,
    5 outside repeat), 78 as proclitic (1.68% vs era l' 1.48%, 21 followers).
    **9-mer drag NULL**: best corpus candidate "seule différence qui existe" ×3
    killed (needs 00="fé" but 00 is the rank-1 group at 2.93% vs era "fé" 0.19% =
    15×; needs 21="ce" colliding with provisional 87=ce).
  - **Context Miner** (WO3): five "ce qui" contexts tabulated; **24→87→64 ×3
    promoted as a formula (value withheld)** — 24 is 10/32 (31%) of 87's
    predecessors; "est" matched P(qui|est ce) exactly (0.304 vs 0.30) yet died 19×
    on P(ce|est); "tout" 1/3, "de" fails. **New formula: 64 96 43 87 01 ×2**
    (@341/@1024) — "qui … ce" reverse joints, the only two 87→01 bigrams in the
    text. 82→16 vs qui-windows: null (2 within ±3 of 64, Poisson chance-consistent;
    0 within ±5 of 87). 16="a" not promoted. Tension (not kill) for 96="par":
    "ce qui 96 47 que" wants a verb, not par/de.
  - **Scorer Smith** (WO4): **scorer BROKEN-ON-CONTROL — real drag not run.**
    Top-1 0.021 vs chance 0.076; MRR 0.133 vs 0.30 bar (47 words, 198 candidates;
    only 1/47 recovered, 0/12 multi-anchor). Diagnosis: placement ranking ties —
    all placements share cells, only 1–2 edge bigrams differ; missing signal is
    **global consistency of implied assignments**. Documented rule-based French
    syllabifier + two-tier hybrid cell scorer built as reusable infrastructure.
    Bonus inference: encipherer systematically stripped final "-er" (corpus
    P(ends-in-"er")=0.0211 ≈ cipher 0.0255 vs standalone "er" 0.0020).
  - **Hypothesis Sweeper** (WO5): **96="par" CONFIRMED (4/4) → 10th provisional
    value** (inherits 87=ce's provisional status). Legs: P(96)=0.0114 vs
    inflation-scaled era P("par")=0.0083 (1.37×); "parce" P(87|96)=0.1429 vs era
    0.1274 (1.12×); "parce que" frame 3/3=1.00 vs era 1.0000 (elision fix moved
    0.3258→1.0000); 15 preds/12 followers. 96="de" REFUTED (freq 6.4× miss).
    77="pas" INCONCLUSIVE (era conditional inverts surgeon's check: P(77|06)=0.1304
    vs era P(pas|ne)=0.0063 = 20.6× miss — wrong baseline — but "pas" itself
    survives; partner 06 probably not "ne"). 06="ne" INCONCLUSIVE (06→77 13% vs
    ≈0.6% expected; 06→29(er)=5/46 vs era exactly zero in 215k words). **New lead:
    06 = verb stem** — era predecessors of "pas" are verbs 98%; 06's follower set
    reads verb-stem (06→77=6, 06→29=5 infinitive, 06→11=4 verb+object, 30 preds);
    explains both "ne" anomalies at once. Six rivals killed; 77="que" reopens if 06
    revalued.
  - **Red Team** (kill authority): **24="est" DEMOTED** (refuted as 4-check
    confirmation; weak open at best) — check 3's P(ce|est)=0.118 was Les-Mis
    dialogue rate (era 0.0099, 12× register gap; observed 19.4× over); check 4
    never rate-checked (31× fail); elision inconsistency (era P(est|c')=0.914
    predicts ~29/32 "c'est", observed 0). **64="qui" DEMOTED** CONFIRMED 4/4 →
    PROVISIONAL — check (b) conditioned on provisional 87=ce; factor-2 band admits
    qui (0.83), "qu'" (1.50), "n'" (1.97). **H5 KILL** (independent corroboration).
    **Factor-2 band UNCALIBRATED** — never validated; sole testable ground-truth
    pair inconclusive; verdicts flip with corpus choice. **F13 "joint
    contradiction" DISSOLVED**: era-matched binomial P(0/10)=0.247, not significant.

- **2026-10-07 (crowd round 3 — 9 executors; 6 merged, 3 pending):** the cast grew
  mid-round: the Tuner (work order 6, added 08:30) plus the Frenchman, the
  Segmenter, and the Bigram Closer (operator order, added ~08:45; still running).
  The six completed executors' verdicts were adjudicated by the red team
  (13 rulings) before merging; the three new executors' claims will get their own
  red-team review when they land. Red-team docket now: no claim merges without
  its ruling; provisional anchors propagate their status to everything built on
  them (87=ce → 64="qui" re-promotion BLOCKED, 96="par" keeps CONFIRMED on the
  repaired leg, all drags inherit provisional).
  - **Closer** (WO4 — resolve 87=ce, steelman AND attack): claimed PROMOTE to
    CONFIRMED on three new legs (N1 rival-kill CIs: P(46|87)=3/32, P(64|87)=5/32,
    all six rivals outside; N2 exhaustive inversion ~4,000 era words, "ce" the only
    n>100 passer; N3 "parce que" frame ×3). Red team DEMOTED → provisional-
    strengthened: N3 admitted circular; R1 "corroboration" recycled the dead
    24="est" number; .md steelman ratios don't reproduce from archived code
    (trust the JSON: 1.89×/1.98×, que-leg at band edge). Also repaired F19's
    "parce" miscomputation (C1). Inversion redo: 24 empty under era, Les Mis,
    AND the union model — 24 is likely not a plain function word.
  - **Morphologist** (WO1 — test R4 "-ment" family, must also refute): corrected
    its own work order (94→82 is 4× @[578,1181,1352,1741]; @1741 is 94-82-46,
    not 94-82-06). **94="ne" CONFIRMED on legs 1–2** (era rate 1.025×, trigram
    ×3 at 1.054× era -nement rate with ground-truth 82=m centered) — red team
    DEMOTED to provisional-strong (leg 3 void: tuner-falsified phase mapping;
    rival 94="re" live: "-rement" 1.28× vs "-nement" 0.66×). **06="ent" general
    REFUTED** (red-team UPHELD; two legs downgraded) — survives PLAUSIBLE only
    on the three trigrams.
  - **Stem Hunter** (WO2 — 06 verb stem, companion 67, re-test 77): claimed
    06=/mɑ̃/ "demand-" CONFIRMED (4 checks, phonetic mute-e model) — red team
    KILLED via crib contradiction ("première" writes 40="e" for mute final -e;
    06→40→77 is 0×). 06=verb-stem class DEMOTED CONFIRMED→provisional (compat
    37% circular, V29 contaminated); 67="veut" CONFIRMED→provisional; 77="pas"
    CONFIRMED→inconclusive; 77="que" REFUTED→disfavored. The 06 tension
    DISSOLVED→open: WO1's /ɑ̃/ and the stem's /mɑ̃/ are different syllables
    sharing group 06 — polyvalence (homophone-merging) stays live, plausible
    not confirmed. New leads: 64="même" (rivals provisional 64="qui"),
    21="le/les", 00="de", 78="vrai".
  - **Scorer Smith** (WO3 — global-consistency scorer, control-first): three
    variants BROKEN-ON-CONTROL (top-1 0.045/0.091/0.071, MRR < 0.30 bar);
    per the control-first rule no real drag ran. Diagnosis: consistency signal
    real but not distinctive — French bigram contexts underdetermine a cell;
    the missing ingredient is JOINT inference (annealing/EM over the full key).
    Reusable `scorer3.py` API banked. Red team UPHELD.
  - **Tuner** (WO6 — what do the contact phases mean linguistically):
    **NULL.** Leave-one-out: phase-constrained ranking never beats baseline
    (2/34 vs 6/34 top-10 slots, both syllabification rules, ±provisional
    anchors); modal-position analysis falsifies "A=medial". The rotation is real
    (chi²=188.3 re-verified) but phases are NOT word-position classes. Bonus:
    'er' 67× segmentation mismatch uncalibrates corpus-tuned ranking generally;
    phase-placement tensions flagged for 96="par" and 87="ce" (not kills).
    Red team UPHELD/endorsed. Alternatives: table-geometry or phonotactic
    alternation.
  - **Red Team** (kill authority, 13 rulings): verdicts as above. 06-tension
    adjudication: F21 (verb stem, class) wins the general reading by worker
    convergence; 06="ent" general REFUTED (upheld); restricted-"ent" PLAUSIBLE
    on the 3 -ment trigrams; neither side holds CONFIRMED on 06. Methodology
    flags banked as F26. Net of round 3: two kills (06=/mɑ̃/, H5-by-round-2),
    five demotions, zero new CONFIRMED promotions — the bar held.
  - Pending: **Frenchman** (ear-checks + idiom completions), **Segmenter**
    (word boundaries), **Bigram Closer** (anchor factory) — merge on arrival
    after their own red-team review.

- **2026-10-07 (crowd round 3 COMPLETE — 9/9 executors merged; red-team 3b
  follow-up review done):** the three newcomers landed and were adjudicated
  before merging. All headline cipher-side numbers re-derived by the curator
  against the lane data — verified: 62→94 ×8 ("on ne"), 78→40 ×3, 11→78 ×2,
  47→78 ×5, 37→78 ×4, 24→87 ×10/52, 94→52 ×3 + 94→59 ×2 ("ne se" ×5),
  64→77 ×3, 77→78 ×7.
  - **Frenchman** (ear-checks, ~140 windows, bilingual): ear-confirmations of
    87="ce", 64="qui", 96="par", 94="ne" as INDEPENDENT corroboration (no
    status changes — defers to red team). Kills K1–K7 adjudicated: K1 accepted
    (converges with N19), K2 accepted scoped (24="de" in « en ce qui »), K3
    conditional, K4 accepted provisional (01="ci" kill), K5 accepted scoped
    (forces 52 polyvalence), K6 no action, K7 rejected. Leads: 24="en" STRONG,
    52="pas" STRONG bounded, 62="on" STRONG (one check from promotion),
    37/01/56/43 MEDIUM, 17="fois" WEAK, 94="en" islets LEAD-grade. THE
    ENLIGHTENMENT: the encipherer spells by ear and cuts inconsistently
    (« prend »→« pre »; « personne » as « per|so|nne » AND « pers|on|ne » —
    two spellings of one word in one cipher) — this explains the tuner NULL,
    the 'er' mismatch, and F22. Register reclassified: the cela gap is GENRE
    (reporter's event-anaphora), not formality.
  - **Segmenter** (semi-Markov forward-backward, unsupervised EM boundary
    rates, honors the tuner NULL): verdict PARTIAL. Ground truth "la première"
    @1033: 3/3 boundaries ≥0.5 out-of-sample, la|première 0.937 unprompted.
    Provisional-word recall 5/23 — at/below chance, but NOT anti-evidence
    (metric muddling + inconsistent segmentation predicts it). Lengths sane
    (mean 1.93 vs era 1.75); 25 crib-drag targets cleared as LEAD-grade.
  - **Bigram Closer** (battery on 41 groups, reusable `battery.py`): headline
    calibration finding — 29=er 182× and 82=m 60× over era, so 29/82/34
    excluded from all rate legs (validates the tuner/frenchedman from a third
    angle). ONE promotion candidate **78="me"** → red-team REJECTED to LEAD:
    the "e"-kill was a syllabifier artifact and the L2 leg divided by the wrong
    marginal (1.66×→2.26× out of band); the "l'"-kill recomputed STRONGER (58×).
    77 symmetric battery: "pas" REFUTED→red-team refined to DISFAVORED (strong);
    "que" lead→DISFAVORED stands; "le" LEAD-weak accepted; 77 is verb-adjacent.
    Refuted: 41="der"/"ni" general, 24="c'est" (28.9×), 47="l", 65="des"/"se",
    12="se"/"en", 00's de/a/le. 24, 00/16/62 INCONCLUSIVE.
  - **Red Team 3b** (7 adjudications): 78="me" promote→LEAD; 77 three-way
    reconciled; calibration exclusion VALID with blast radius named (red team's
    own "ent|er strained" leg VOID — exemplary self-kill); K1–K7 ruled; leads
    graded; segmenter PARTIAL accepted; **lane position: rigid syllabification
    is DEAD as an instrument** (F30) — three independent lines converge.
  - Net of round 3: kills (06=/mɑ̃/ via crib, 01="ci" provisional, 24="de"
    scoped, 52="pas"-single scoped, H5 by round 2), eight demotions,
    ZERO promotions — the bar held. **62="on" is the promotion candidate.**
  - Pending: none. Round 4 next steps in STATE.md.

## Null results
- **N1 (2026-10-07):** crib-anchored function-word drag (Phase C above) — degenerate at 7-anchor
  sparsity; all candidates tie at floor. Not a disproof of the crib-anchored strategy, only of
  this scorer at this sparsity.
- **N2 (2026-10-07):** drag re-run with 8 anchors (7 pencil cribs + provisional
  lane-inferred 87=ce) — still degenerate; all top candidates tie at the quadgram
  floor (−7.714). The window-quadgram crib-drag is shelved until anchor density or
  the scorer changes.
- **N3 (2026-10-07):** drag re-run with 9 anchors (7 pencil cribs + provisional 87=ce +
  provisional 64=qui) — still null. Anchors-only baseline lifts off the quadgram floor
  on some windows (anchor density finally registering), but no (group, word) candidate
  separates from the floor. The window-quadgram crib-drag stays shelved; a syllable-level
  scorer is the candidate replacement.
- **N4 (2026-10-07, crowd/phonotactician):** phonotactic syllabary search — NULL.
  Beat uniform (+2798) and freq-matched (+3578, 19.0 sd) baselines degenerately: best key
  assigns 4 syllables to all 88 free groups (`champmatmatchamphi…` soup); only 1/88 groups
  stable ≥0.75 across 12 restarts. The scorer is exploited, not informative. Fix candidates:
  unicity/dispersion constraint, unigram prior, lexical word-segmentation scoring.
  Evidence: `code/crowd/phonotactician_results.{md,json}`.
- **N5 (2026-10-07, crowd/annealer):** syllable-bigram annealing — **method-broken-on-control.**
  Synthetic control (Les Mis French through a known random syllabary, 8 anchors pinned):
  1/88 planted assignments recovered (≈chance). Planted true key scores −5.36 per-pair
  logp vs the annealer's "best" nonsense at −2.90 — the scorer's global optimum sits
  ~2.5 nats/pair above real French. ~20 groups collapse to "de" at 20–24/24 recurrence.
  Real-ciphertext assignments are null; promote none. Same failure mode as Bourdeau's
  syllable solvers, now proven by control. Fix candidates: word-level scoring, unigram
  prior — each needs its own synthetic control first.
  Evidence: `code/crowd/annealer_results.{md,json}`.
- **N6 (2026-10-07, crowd/drag-racer):** syllable-level function-word drag — PARTIAL.
  Discriminates where letter-quadgrams tied (54/55 distinct scores, no floor degeneracy),
  but the discrimination is word-prior, not placement: at 12.8% anchor sparsity the best
  window for ~half the candidates is the isolated word itself. Only exact multi-anchor
  placement: cela=87-11 ×7. Min2 (≥2 anchor coincidences) placements: exactly one
  candidate. Letter-drag death diagnosed: ±6 windows decode to ~1.7 anchored groups.
  Granularity warning: pyphen hyphenation units almost never emit er/m/i/e (cipher cells
  include single letters) — er/m/i/e bigram expectations uncalibrated.
  Evidence: `code/crowd/drag_racer_results.{md,json}`.
- **N7 (2026-10-07, crowd/historian):** no 1840s Saxon cipher key in any published source
  or catalogue checked (DECODE Dresden keys stop at 1799–1806; Rous 2023 covers 1500–1763
  only). Search trail in `code/crowd/historian_results.md`.
- **N8 (2026-10-07, crowd/contactor):** both pre-registered contact predictions failed as
  stated — P1 (34=i/40=e share vowel-class contacts: different clusters A vs B; 40=e not
  in 34=i's top-10 Jaccard neighbors) and P2 (87 function-word-like: lands in B with
  82=m, zero function-word anchors in top-10). Suggestive residuals: 40=e is 34=i's
  2nd-nearest anchor (0.241); 87's nearest anchor is 82=m (0.423).
  Evidence: `code/crowd/contactor_results.{md,json}`.
- **N9 (2026-10-07, crowd/crib-surgeon):** no 46=que within ±10 of the "la première"
  crib; no second "première" anywhere; 11-70 ("la pre") unique to @1033.
  Evidence: `code/crowd/crib_surgeon_results.{md,json}`.

- **N10 (2026-10-07, crowd2/closer):** 24="est" REFUTED under the era-matched standard.
  All four H1 checks fail or downgrade on Tocqueville rates (19.5×, 74× fails;
  rank "1" was 0-based). Structural refutation legs (C-check, 11=la ×4 predecessor
  kill) are instrument-independent. Rivals (sont/ont, c'est, de, en) all die;
  45-word inversion sweep: no era word fits P(ce|V)≈0.19 ∧ P(V|que)≈0.10 —
  intersection empty (lead: points back at provisional 87=ce). 24 unidentified.
  Evidence: `code/crowd2/closer_results.{md,json}`.
- **N11 (2026-10-07, crowd2/formula-tester):** H5 "J'ai l'honneur de" REFUTED as
  stated — kill-grade structural contradiction (82='m' ground truth vs needed
  "neur") plus 67×/184×/47× rate failures. Surviving: 77→78 "j'ai l'" chunk,
  78-as-proclitic. 9-mer drag NULL (best candidate killed on 00="fé" 15× and
  21="ce" collision). Evidence: `code/crowd2/formula_tester_results.{md,json}`.
- **N12 (2026-10-07, crowd2/scorer-smith):** syllable-level scorer BROKEN-ON-CONTROL
  (top-1 0.021 < chance 0.076; MRR 0.133 < 0.30 bar) — real drag not run, per the
  control-first rule. Failure mechanism diagnosed: placement ties; missing signal
  is global consistency of implied assignments. Redesign direction recorded.
  Evidence: `code/crowd2/scorer_smith_results.{md,json}`.
- **N13 (2026-10-07, crowd2/context-miner):** 82→16 vs qui-windows null
  (chance-consistent); 0 within ±5 of 87=ce (p≈0.12, sub-significant). 16 neither
  ce-like nor qui-like; 16="a" not promoted. 16 unidentified.
  Evidence: `code/crowd2/context_miner_results.{md,json}`.
- **N14 (2026-10-07, crowd2/hypothesis-sweeper):** 96="de" REFUTED (1/3). 77="pas"
  INCONCLUSIVE (survives as best reading for 77; partner 06 probably not "ne").
  06="ne" INCONCLUSIVE (two unexplained bigram anomalies). 41="der"/08="ni"
  INCONCLUSIVE (n=1). Six rivals killed (77="plus", 77="ne"-swap, 06="de"/"le",
  96="pour", 96="a/à", 41="ter"/"mer"). Evidence:
  `code/crowd2/hypothesis_sweeper_results.{md,json}`.
- **N15 (2026-10-07, crowd3/tuner):** contact-phase→word-position mapping NULL.
  Leave-one-out on anchored groups: phase-constrained ranking 2/34 vs unconstrained
  6/34 top-10 slots (both syllabification rules, with and without provisional
  anchors). Modal-position analysis falsifies "A=medial" (0/4 A-phase anchors
  modal-medial). 'er' segmentation mismatch: cipher 29=er at 2.55% vs bare-'er'
  0.038% in the era corpus — the 1841 syllabary segments differently than any rule
  tried, uncalibrating corpus-tuned ranking generally. The rotation itself
  re-verified (chi²=188.3); the phases are real but are NOT word-position classes.
  No shortlists emitted. Evidence: `code/crowd3/tuner_results.{md,json}`.
- **N16 (2026-10-07, crowd3/scorer-smith):** global-consistency scorer
  BROKEN-ON-CONTROL — three variants fail the pre-registered bar (top-1
  0.045/0.091/0.071, MRR < 0.30). Diagnosis: the consistency signal is real but
  not distinctive — French bigram contexts underdetermine a cell, single-letter
  impostors matching a true edge outscore the truth, and no per-occurrence
  aggregation fixes an uninformative likelihood. Missing ingredient: JOINT
  inference (simulated annealing/EM over the full key). Real drag not run per the
  control-first rule. Reusable `code/crowd3/scorer3.py` API banked.
  Evidence: `code/crowd3/scorer_smith_results.{md,json}`.
- **N17 (2026-10-07, crowd3/red-team):** 06=/mɑ̃/ "demand-" model KILLED —
  crib contradiction: "première"=pre|m|i|er|**e** writes 40="e" for mute final
  -e, but the model needs mute-e unwritten ("demande pas"=?+06+77; observed
  06→40→77 is 0×). The ground-truth crib kills the phonetic model cleanly.
- **N18 (2026-10-07, crowd3/red-team):** demotions — 06=verb-stem (class)
  CONFIRMED→provisional (compat 37% circular, V29 contaminated); 67="veut"
  CONFIRMED→provisional; 77="pas" CONFIRMED→inconclusive; 06 polyvalence
  CONFIRMED→plausible; tension DISSOLVED→open. 77="que" REFUTED→disfavored.
- **N19 (2026-10-07, crowd3/morphologist; red-team UPHELD):** 06="ent" as a general
  reading REFUTED — 06∈A at all phase cuts; 0/3 trigram-final 06s followed by
  anything word-initial (binomial p≈0.001); 06→29(er)×5 reads "ent|er",
  ungrammatical. Survives only as PLAUSIBLE restricted to the three 94-82-06
  trigrams. Rivals 94="en" ("en-m-ent" is no French word; rate 1.79× vs 1.025×)
  and 94="re" (bigram geometry "m-re" impossible) killed for the trigram.
  Evidence: `code/crowd3/morphologist_results.{md,json}`.
- **N20 (2026-10-07, crowd3/red-team-3b):** 78="me" promotion REJECTED → LEAD.
  Two load-bearing legs broken: (B-78a) the "e"-rival kill via era ("e","e")=0
  is a **syllabifier artifact** — the era tokenizer almost never emits word-final
  bare 'e' ("rue"→'rue', "première"→'pre','mie','re'), while cipher 40 is the
  word-final mute-e writer per the crib; the zero measures tokenizer habits, not
  French grammar — "e" returns as a live rival (L1 1.044 in-band); (B-78b) the
  headline L2 leg miscomputed — closer divided by the wrong marginal
  (154/5617=0.0274 = P(la|me) for P(me|la)); recomputed 154/7652=**0.0201**,
  ratio **2.26× out of band**. Survives: L1 1.108, L2b 0.731, L3b "la même"
  era n=154, and the "l'"-kill recomputed STRONGER (58×, not 40.4× — "la l'"
  genuinely ungrammatical). Net: rival "l'" killed, rival "e" unkilled → LEAD.
  Extension: 40="e" conditional/attestation legs are uncalibrated too
  (unigram 0.71× stays as context).
  Evidence: `code/crowd3/bigram_closer_results.{md,json}`,
  `code/crowd3/red_team_round3b_results.{md,json}`.
- **N21 (2026-10-07, crowd3/red-team-3b):** 77 verdicts refined. 77="pas":
  INCONCLUSIVE→**DISFAVORED (strong)** — the closer's L1 6.69× reproduces
  (5.21× at word-space, survives sense-mixing correction; grammatical "ce pas" ×2
  under 87=ce); legitimate new instrument, but grade too high for REFUTED (no
  unconditional leg; band uncalibrated). 77="que": DISFAVORED stands — all 3
  checks are uncalibrated-band legs; polyvalence cost with GT 46=que stands
  (cosine 0.198); killed at its own crown example by the frenchman's @790
  "qui que" window ("que qui que" ungrammatical). 77="le": LEAD-weak accepted.
  New direction: 77 is verb-adjacent (frenchman's « qui [verbe] » + verb-stem
  predecessors 06×6, 67×6). Closer's L2prov legs were hand-computed in no
  archived code — provisional-conditioned, unverifiable as stated.
- **N22 (2026-10-07, crowd3/red-team-3b):** calibration exclusion VALID —
  181.5×/61.1×/3.3× reproduce. Blast radius: red team's own round-3 "ent|er
  strained" leg VOID (er-rate uncalibrated; 06="ent"-general REFUTED stands on
  reduced legs); the 06="ne" ne+er-initial leg VOID (no live claim affected);
  closer's 94→82 "ne m'" void endorsed. Unaffected: the 87=ce battery and
  inversion, 94="ne" unigram rate, the 64→77×3 word-space anomaly, all
  cipher-side legs, all ear readings.
- **N23 (2026-10-07, crowd3/red-team-3b):** kill ledger — **01="ci" provisional
  kill** (3.84× + "ici" ×0; @295 leg circular); **24="de" scoped kill** (inside
  « en ce qui », conditioned on 87=ce/64=qui); **52="pas"-as-single-reading
  scoped kill** (@160 « per|so|nne » proves 52 word-internal — forces 52
  polyvalence); 43="parmi" conditional kill (needs unconfirmed 01="est");
  K7 (56="plus" as single reading) REJECTED (rests on unconfirmed 37="le" +
  unidentified 44). No promotions this round. **62="on" is the promotion
  candidate** — one independent check away.
- **N24 (2026-10-07, crowd4/morphologist; red-team: DEMOTE ACCEPTED fenced):**
  94="re" demoted live-rival→**disfavored**. Symmetric F30-legal battery:
  word-space host odds 641 ("nement") vs 282 ("rement") = **2.27:1 for "ne"**;
  "re" composes in **0/36** occurrences; the old 1.28× "re" leg VOID per F30
  (worker's admission — artifact of the dead rigid-syllable instrument).
  94="ne" holds provisional-strong on rebuilt legs. 94="en" coexists as a
  CONDITIONED islet (iff pre=82 "m'en" ×3 or suc=87 "en ce" ×1, 4/4 — new
  indices 1169/1576). Fence: @578 trigram host unidentified (revival thread).
  Evidence: `code/crowd4/morph94_re_battery.py`/`.json`,
  `code/crowd4/report_inbox/morphologist-94-re.md`.
- **N25 (2026-10-07, crowd4/bigram-closer; red-team: no reversals):** battery
  B-78b repaired (`code/crowd4/battery4.py` — L2 now divides by the context
  marginal; N22 exclusions enforced in code; crowd3 files untouched). Headline
  leg before/after: 1.658 (wrong marginal) → **2.259 out-of-band** (matches
  red-team's recompute). Verdicts: 77="pas" DISFAVORED-strong (unchanged),
  77="que" DISFAVORED (unchanged), 77="le" LEAD-weak→**LEAD** (ACCEPT fenced —
  77→86 ×5 verified @430/798/877/950/1133 new), 78="me" LEAD (promotion not
  granted; rival "e" live). New adverse evidence (fenced): 77→78 ×7 frames
  under 78="me" ("pas me" era-0 kill-grade); 2/7 sit inside the "gouvernement"
  trigram → 78="ver" word-internal there. Evidence:
  `code/crowd4/battery4.py`, `code/crowd4/battery4_results.json`.
- **N26 (2026-10-07, crowd4/segmenter):** control **PASS** pre-registered
  (`code/crowd4/segmenter_control.md` — synthetic Tocqueville cipher, ear-cutting
  noise; 0.721/0.939/0.258 vs thresholds 0.60/0.70/0.10). Drag of the 25
  crib-targets: **0 proposed / 25 LEAD-held / 0 killed** — honest all-null (a
  vacuous "14 PROPOSED" first pass was caught and corrected before reporting).
  Tension: @81-83 zero era candidates under 62="on" (likely MAP-span merge
  error — control M1=0.72 ⇒ ~28% miss rate — not a kill of 62="on").
  Evidence: `code/crowd4/drag25.py`, `code/crowd4/drag25_results.json`.
- **N27 (2026-10-07, crowd4/closer; red-team: DEMOTE ACCEPTED bounded):**
  64="même" LEAD→**disfavored** (87→64 ×5 at 9.83× over era P(même|ce),
  p=1.43e-4; verb-gap 6.3×; "même si" dead at 2.7e-5). 64="qui"
  provisional-FAVORED; re-promotion block STAYS. Catch: 64→77×3 is one
  byte-identical trigram **64-77-84 ×3** (new @144/1445/1801, n_eff=1 —
  curator-verified) — prior rate arguments triple-counted one phrase. 87-leg:
  register-matched reporter-voice subset FAILs pre-stated bar (0.0398 vs 0.0414
  baseline; cela leg stays dead); ci/te anchor scan NULL. New corroboration
  (not promotion): 87-64-77-84 @1800–1803 (new; curator-verified) parses as
  «ce qui [verbe] 84» under (87=ce ∧ 64=qui ∧ 77=verb-adjacent). Evidence:
  `code/crowd4/closer64_87.py`/`.json`.
- **N28 (2026-10-07, crowd4/frenchman; red-team: promotion NOT granted):**
  third leg for 62="on" FOUND but held at **STRONG LEAD** — fresh-window
  subject triangulation: new @845–853 reads "…par écrit, **on me** [dit]…"
  (curator-verified window 00 33 96 40 62 21 67 91 51), object pronoun 21="me"
  forces a subject; zero counterexamples in 26 fresh windows; /ɔ̃/ rivals
  (son/mon/nom/ont) killed. Red team: legs 1&3 share the ear instrument —
  not independent; promotion needs an instrument-independent third leg.
  Parse-repair update (curator): 62→94 is **9/35=0.2571 (2.18× era)** on the
  repaired parse (was 8/34) — the repaired a5_03 region contributes a 9th
  "on ne" @761. Discarded null: STRUCT boundary leg uncalibrated (GT control
  fails its own signature). Enlightenment: the by-ear model PREDICTED the
  46→62 ×0 absence ("qu'on"=/kɔ̃/ = one spoken syllable → one group).
  Evidence: `code/crowd4/frenchman4_62.py`/`.json`.
- **N29 (2026-10-07, crowd4/stem-hunter):** 47="me" as a uniform word
  **KILLED** (3 independent: "par me" era n=0 — the 802× hardens to a hard
  zero in word space; "me que" P=0; "me la" P=0). **47="ce" LEAD** (polyvalent
  with 87): "ce que" 3/28=0.1071 vs era 0.1076 → **1.00× exact**
  (curator-verified); "par ce" 2.85×; 47→11 ×3 "cela". The "même" joint
  survives as a FRAGMENT reading only. @148–150 jar BOUNDED (@150–152 =
  "par ce que" ✓; residual = the verbless 64 slot). 06 stem: bounded, NOT
  identified (06-verb ≈13.6/1000 vs era "demand*" 0.20/1000 = 66× gap; no
  single -er stem fits; /mɑ̃/ not revived). NEW mechanism: **06/86
  complementary distribution** — 06 = finite/imperative stem (06→29 ×4,
  06→11 ×4, 06→00 ×4), 86 = infinitive-complement stem (00→86 ×12 vs 00→06
  ×0). Parse-repair correction (curator): 06→29 is **×4** on the repaired
  parse — the old 5th (@760) was an off-phase artifact of row a5_03; the
  infinitive-frame check survives on 4. Cutting rules banked
  (`code/crowd4/syllabary4.py`): R1 cells 1–4 letters; R2 by-ear inconsistent
  cuts ("personne" = 93|52|94 @160 vs 77|62|94 @507, positions verified);
  R3 mute -e WRITTEN by default. Upstream 180-unit inventory is NOT the
  encipherer's table (all three annealers failed on it). Evidence:
  `code/crowd4/stem47_06_final.py`, `code/crowd4/stem47_06_results.json`.
- **N30 (2026-10-07, crowd4/scorer-smith):** joint decipherment engine
  (annealing/EM, polyvalent emission, rotation-aware transition prior, 7 pins)
  is model-correct but **BROKEN-ON-CONTROL** — truth −2.65 beats annealed
  −3.05, but search can't find truth's basin: **identifiability problem**
  (flat landscape from the lossy 96-vs-~700 key), not a model problem. Gate
  held: no R5005 run. Parse adopted mid-round (`code/crowd4/repaired_parse.py`).
  Notable: recomputed phases on the repaired stream give rotation
  chi²=**366.3** (vs 178.8 banked) — the rotation is much stronger under the
  repaired parse — but cluster assignments are fragile (61/96 groups change
  phase). Engine uses recomputed phases as a weak prior. Evidence:
  `code/crowd4/report_inbox/scorer-smith-joint.md`.
- **N31 (2026-10-07, crowd4/red-team):** 4 rulings, every number recomputed:
  77="le" LEAD-weak→LEAD **ACCEPT (fenced)**; 64="même" LEAD→disfavored
  **DEMOTE ACCEPTED (bounded, not killed)**; 94="re" live-rival→disfavored
  **DEMOTE ACCEPTED (fenced on @578)**; 94="en" LEAD→provisional co-value
  **DENY** — 4 instances/2 types = one evidential body (independence fail),
  stays LEAD. Records: 78="me" LEAD, 62="on" STRONG LEAD, 87=ce unchanged,
  94="ne" provisional-strong. Note: rulings computed on the old-parse stream;
  values identical for n≥773 and no cited position in the repaired region
  (REINDEX.md) — rulings stand. Evidence:
  `code/crowd4/red_team_rulings.json`.
- **N32 (2026-10-07, side-wordpattern/overwatch): word-pattern dictionary attack
  honest NULL.** Instrument validity MIXED across two orthogonal dimensions.
  Polyvalence dimension VALID-WITH-RESTRICTIONS: pattern survival 0.995 overall
  (freq-weighted 0.998); per-islet 06: 0.993, 94: 0.992, 52: 0.994; worst case
  "sérieuse"/"sérieusement" 0.38. Smart expansion (only words that can actually
  produce the pattern) inflates candidates ≤6.0×; naive whole-closure expansion
  (202×–2318×) is an instrument-killer and must never be done. Unit-inventory
  dimension INVALID as built: the ground-truth control fails — the known
  "première" tail @1035–1038 (82-34-29-40, four pencil-crib anchors) returns
  ZERO lexicon candidates in both alphabets (red-team refinement: effectively
  a single-unit test, 'm' drives 100% of the zero). All 26 would-be proposals
  KILLED and restamped DEAD (A: "quiconque" ×7, pure echo of provisional
  64=qui — caution: provisional anchors breed echoes; B: hapax accidents, all
  freq ≤17, zero with ≥2 GT anchors; C: by-ear variant artifacts; Restriction 4
  kills "pionnier" harder — needs 06="ni", inconsistent with every live 06
  reading). Traceability flags: tester's §6 K≥3 synthetic numbers
  (0.914/0.891/0.879) do NOT reproduce from archived code (~0.93–0.94 on
  re-run) — regenerate, don't cite; old-parse islet counts stale (se weight
  basis n=5→n=6, 0.380→0.375 — verdict robust). Evidence:
  `code/side-wordpattern/`, `code/side-wordpattern/redteam/ADJUDICATION.md`.
- **N33 (2026-10-07, side-wordpattern/overwatch): polyvalence gate
  VALID-WITH-RESTRICTIONS** — governs recall, not positive evidence; promotes
  nothing by itself. Red-team-amended restrictions R1–R8 banked: R1
  strengthened (expanded index unconditional), R3 demoted to recommendation,
  R6 extended to parse changes, R7 fenced non-implementable, new R8 (prefer
  orth alphabet for repetition patterns — orth survival 1.000). Reusable by the
  main fleet with these restrictions. Evidence:
  `code/side-wordpattern/polyvalence/POLYVALENCE_REPORT.md`.
- **N34 (2026-10-07, sidepath/overwatch): rapid crib-bootstrap loop honest NULL
  after 1 of 5 passes** — VOID condition fired per pre-registered stop rule
  (174 real accepts vs control mean 208.3; 174 < 2×208.3). Diagnosis: the fuzzy
  scorer cannot separate signal from noise at 30.66% anchor sparsity; the
  sharpest targets (all eight 62→94 windows, all W-47 sub-windows) emitted
  nothing — the missing readings aren't in the frozen candidate set. Byproducts:
  canonical recounts **n24=52, n52=27, n62=34** (old 42/13/32 were parse
  artifacts — CAVEAT: pre-parse-repair counts, re-verify on the 1,847-pair
  parse); skeleton at 30.66% stream coverage (566/1,846, sha256
  18d48ccd…9373f); "montrera" as independent 94="re" support (S=0.917).
  Methodology lesson: shuffling de-anchors windows so controls accept MORE than
  real — future drags need ANCHOR-PRESERVING controls. Frame bug caught before
  damage (first slider parsed 1,882 pairs vs canonical 1,846; re-parsed,
  prereg amended v1.1). Evidence: `code/sidepath/`.

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
- F6 (2026-10-07, this lane; **REVISED by Red Team 2026-10-07 — demoted**):
  87="ce" was scored CONFIRMED 4/5 in attempt 2; the scorecard does not survive.
  Check (b)'s "P(cela|ce)=0.278" was n_cela/n_ce, a count ratio, not a conditional —
  honest syllable-level bound P("la"|"ce"-syllable) ≤ 0.1805, and observed 0.2188
  exceeds it (check void); checks (a)/(d) also passed for the refuted de/à
  (non-discriminating); check (c) is n=3, Wilson CI [0.032,0.242] (weak). Status now:
  **PLAUSIBLE provisional hypothesis — best-tested reading, unsound scorecard.**
  No alternative beats it ("pour" loses, "sans" refuted, de/à refutation upheld).
  Surviving model-free support: 87 is the #1 predecessor of 11 (P=0.219); ce-la
  observed 7 vs E=0.7 (z=+7.6) — drag-racer corroboration. Caution flags: 87 clusters
  with 82=m, not with la/que (contactor); P(46|87,pre=96)=3/3 vs pre=24 0/10 — the
  "que" is licensed by predecessor 96, never 24. Everything downstream that used
  87=ce (N2 drag re-run) inherits this uncertainty. **Update (attempt 3, same day):**
  re-validated against the era-matched Tocqueville corpus at **CONFIRMED 3/4** —
  P(que|87)=0.094 ≈ era P(que|ce)=0.108; the "cela"-rate leg is downgraded to
  register-dependent (era n(cela)/n(ce)=0.041 vs Les Mis 0.278 — a 6.7× register gap;
  the cipher's P(11|87)=0.219 sits with Les Mis, not the era corpus). Net status:
  **provisional anchor, best-tested reading, cela-leg register-dependent.**
  Evidence: `code/attempt2.py`,
  `data/attempt2_results.json`, `code/crowd/red_team_results.{md,json}`,
  `code/attempt3.py`, `data/attempt3_results.json`.
- F7 (2026-10-07, this lane): H1 (82→16 as "ma", 16="a") **not confirmed** — PLAUSIBLE (1/4):
  rank(16)=22 in vowel band, but P(82|16)=0.39, mi/me controls absent (82→34=1, 82→40=0),
  Les Mis P(a|m)=0.19 not dominant. 16 unidentified. Evidence: same as F6.
- F8 (2026-10-07, this lane, erratum): attempt-1 prose "87→11 in 7/44" quoted P(87|11);
  the correct hypothesis rate is **P(11|87)=7/32=21.9%**. Raw counts in
  `data/attempt1_results.json` were always correct; only the prose ratio is corrected.
- F11 (2026-10-07, crowd/contactor): **3-phase rotational contact structure A→C→B→A**
  over the 96 groups — P(A→C)=0.418, P(C→B)=0.450, P(B→A)=0.476 (1.35–1.52× over
  independence), chi-square=181.3 on 4 df (p≪1e-6), self-transitions suppressed
  (0.51–0.74×). Shape matches word-position phonotactics: 29=er anchors phase C
  (prev-A 0.77, next-B 0.89 — word-final-ish, "er" = classic French final syllable;
  C→B is the word-boundary edge). 87↔82 is the highest anchor-anchor Jaccard
  (0.423) with an identical C→X→A block signature — 87 patterns as proclitic/onset,
  compatible with 87=ce but a caution flag on its provisional status. Evidence:
  `code/crowd/contactor.py`, `code/crowd/contactor_results.json`.
- F12 (2026-10-07, crowd/crib-surgeon + formula-hunter, convergent; **curator-verified
  byte-level**): **"la première" = 11-70-82-34-29-40 occurs exactly once @pair 1033
  (56.0%)** [old parse; SUPERSEDED by F32 — repaired parse: TWICE, @pairs 754 (the
  manuscript gloss line a5_03) and 1034] — six consecutive groups, every one a
  ground-truth pencil-crib anchor.
  The lane's first multi-group word read from cribs alone. Mid-letter position in a
  back-reference context ("la première [fois/lettre]"). Zero single-group
  near-misses; 11-70 unique to that spot. Evidence: `code/crowd/crib_surgeon_results.json`,
  `code/crowd/formula_hunter_results.json`; independently re-derived by curator.
- F13 (2026-10-07, crowd/red-team; curator-verified): attempt-2's "P(cela|ce)=0.278"
  was a count ratio, not a conditional (see revised F6); additionally,
  **P(46|87,pre=96)=3/3 vs P(46|87,pre=24)=0/10** — the "que" after 87 is licensed by
  predecessor 96, never by 24. If 24=est (surgeon's H1), the 24-87-46 0/10 is a joint
  contradiction (binomial p=9.1e-04 under Les Mis rates — re-validate era-matched).
  The drag racer independently caught the ratio error (true cross-word P(la|ce)=0.022).
  Evidence: `code/crowd/red_team_results.json`; curator re-derivation matches.
- F14 (2026-10-07, crowd/formula-hunter): repeat census at pair alignment — repeats are
  **discourse-level set phrases, not letter-framing formulas**: 13/16 long repeats
  (L≥5) are body/body, none exclusive to the opening or closing 100 groups (the
  valediction occurs once, unrecoverable by repetition). Longest repeat
  `56 69 26 00 33 21 64 37 01` ×2 @931/@1625 (unread — top crib-drag target).
  `96 87 46` ×3 ("parce que"/"de ce que", unchecked). `24 87 64` ×3 ("[pour|en] ce
  qui" — blocked on 64="qui"). `77 78 94 82 06` ×2 re-verified @1179/@1350.
  Evidence: `code/crowd/formula_hunter_results.json`.
- F15 (2026-10-07, crowd/linguist): **register mismatch with Les Mis is more dangerous
  than era mismatch** — despatch French is first-person formulaic administrative prose;
  Les Mis is third-person narration + dialogue + argot (the likely mechanism behind the
  "fluent nonsense" solver drift). Orthography post-1835/pre-1878 ("collége", "poëte",
  "asyle", "français", "était"); "cela":"ça" = 47:1 in 1835–1850 print. Syllable tiers
  from Meisel 1826 diplomatic corpus (98k words); diplomatic formulae with syllable
  segmentations recorded (openings, closings, "Par ma dépêche du…", "En réponse à la
  dépêche de Votre Excellence du…"). New crib HYPOTHESIS (not finding): the ×5 repeat
  `77 78 94 82 06` = **"J'ai l'honneur de"** (j'ai·l'·hon·neur·de, 5 syllable units).
  Evidence: `code/crowd/linguist_results.{md,json}` (per-claim OBS/DER/INF marks).
- F16 (2026-10-07, crowd/historian): identities established — Heinrich Anton von Zeschau
  (1789–1870), Saxon finance minister 1831–1848, took over Foreign Affairs 1835, writing
  as minister to his envoy Albin Leo von Seebach (1811–1884), Geschäftsträger 1839 /
  Ministerresident 1840 / Envoy 1847, in St Petersburg 1839–1852, married to Russian
  chancellor Nesselrode's daughter. Concrete routes: **DECODE registration is free and
  self-service** (https://de-crypt.org/decrypt-web/register — unlocks R5006–R5008 full
  images); **HStAD Dresden accepts mail-in scan orders** ("Antrag auf Herstellung von
  Kopien" → poststelle@sta.smi.sachsen.de), shelfmark verbatim "Sächsisches
  Staatsarchiv, 10731 Sächsische Gesandtschaft für Russland, St. Petersburg, Nr. 12";
  key-candidate files **10731 Nr. 12** (the letters themselves) and **10717 Nr. 3332
  (1841) / 3333 (1842)** "Korrespondenz des Ministeriums mit der Gesandtschaft
  Petersburg" (the ministry/Dresden side). Evidence:
  `code/crowd/historian_results.{md,json}`.
- F17 (2026-10-07, crowd2/context-miner; curator-verified): trigram formula
  **24→87→64 ×3** — every 87→64 bigram has 24 immediately before; 24 supplies
  10/32 (31%) of 87's predecessors; 24 is rank 2/96 at freq 52. Value WITHHELD:
  "est" matched P(qui|est ce) exactly (0.304 vs 0.30) yet died 19× on P(ce|est);
  "tout" 1/3; "de" fails. No candidate clears ≥2 independent checks.
  Evidence: `code/crowd2/context_miner_results.json` (curator re-derived counts).
- F18 (2026-10-07, crowd2/context-miner; curator-verified): exact 5-group repeat
  **64 96 43 87 01 ×2** (@341/@1024) — "qui … ce" reverse joints; the only two
  87→01 bigrams in the whole text sit inside this formula. Reverse joints are
  consistently shaped 64 X Y (Z) 87, never adjacent.
  Evidence: `code/crowd2/context_miner_results.json` (curator re-derived).
- F19 (2026-10-07, crowd2/hypothesis-sweeper): **96="par" CONFIRMED (4/4)** →
  10th provisional lane-inferred value (inherits 87=ce's provisional status).
  Legs: P(96)=0.0114 vs inflation-scaled era P("par")=0.0083 (1.37×); "parce"
  compound P(87|96)=3/21=0.1429 vs era 132/1036=0.1274 (1.12×); "parce que"
  frame 3/3=1.00 vs era P(que|parce)=1.0000 (elision fix moved 0.3258→1.0000);
  15 predecessors / 12 followers diversity. Tension (unresolved): the context
  miner's "ce qui 96 47 que" window doesn't parse with "par" — a verb does.
  Evidence: `code/crowd2/hypothesis_sweeper_results.{md,json}`.
- F20 (2026-10-07, crowd2/red-team): demotions. **24="est" demoted** — refuted as a
  4-check confirmation case (check 3's P(ce|est)=0.118 was Les-Mis dialogue rate;
  era 0.0099 is a 12× register gap and observed 0.1923 sits 19.4× over; check 4
  never rate-checked, 31× fail under era; elision inconsistency — era P(est|c')=
  0.914 predicts ~29/32 "c'est", observed 0); remains a weak open hypothesis at
  best. **64="qui" demoted** CONFIRMED 4/4 → PROVISIONAL: check (b) conditioned on
  provisional 87=ce; the factor-2 band admits qui (0.83), "qu'" elided que (1.50),
  "n'" elided ne (1.97) — the band doesn't identify "qui". **Factor-2 band
  methodology UNCALIBRATED**: never validated against ground truth; the sole
  testable pair (que→la, n=29) is inconclusive; verdicts flip with corpus choice.
  **F13 "joint contradiction" DISSOLVED**: era-matched binomial P(0/10)=0.247, not
  significant (the 9.1e-04 used Les Mis rates — a register artifact).
  Evidence: `code/crowd2/red_team_results.{md,json}`.
- F21 (2026-10-07, crowd2/hypothesis-sweeper): new lead — **06 = verb stem**
  (unscored, flagged for round 3). Era predecessors of "pas" are verbs 98%
  (est 163, a 102, sont 43; "ne" only 20/984 = 2%); 06's follower set reads as a
  verb-stem profile: 06→77(pas)=6, 06→29(er)=5 (infinitive X-er), 06→11(la)=4
  (verb+object), 30 distinct predecessors. Explains both of "ne"'s anomalies at
  once. Companion unknown: 67 (the other 6× predecessor of 77).
  Evidence: `code/crowd2/hypothesis_sweeper_results.{md,json}`.
- F22 (2026-10-07, crowd2/scorer-smith; inference, testable): encipherer
  granularity claim — corpus P(standalone "er" unit)=0.0020 vs cipher 0.0255
  (13× gap), but corpus P(unit *ends in letters* "er")=0.0211 ≈ cipher 0.0255:
  the encipherer systematically stripped final "-er" (parl|er). Marked inference,
  not finding. Evidence: `code/crowd2/scorer_smith_results.{md,json}`.
- F23 (2026-10-07, crowd2/formula-tester; referred as round-3 work order): R4
  **"-ment" word family promoted to live reading: 94=ne, 82=m ('m' is ground
  truth ✓), 06=ent.** The 2 extra 94→82 instances (@578/@1181, outside the
  ×2 repeat) are exactly what R4 predicts. Test bed for round 3.
  Evidence: `code/crowd2/formula_tester_results.{md,json}`.
- **F24 (2026-10-07, crowd3/morphologist; red-team: DEMOTED CONFIRMED→
  provisional-strong):** 94="ne" — era syllable rate 1.025× (0.01950 vs 0.01902,
  documented orthographic syllabifier); trigram 94-82-06 ×3 at 1.054× the era
  -nement rate with ground-truth 82=m centered; ×2 byte-identical repeat
  @1179/@1350. Leg 3 (phase predecessor profile) VOID — it used the
  tuner-falsified phase mapping. Correction: 94→82 is 4× @[578, 1181, 1352,
  1741] (@1181 inside repeat #1; @1741 is 94-82-46, unparsed "i-ne-m-que" —
  25% of the 94→82 family unexplained). Live rival: **94="re"** ("-rement"
  1.28× vs "-nement" 0.66×) — round-4 lead.
  Evidence: `code/crowd3/morphologist_results.{md,json}`.
- **F25 (2026-10-07, crowd3, red-team adjudicated):** 06 working state — F21
  verb-stem (class-level) wins the general reading by worker convergence but
  holds only PROVISIONAL (CONFIRMED never earned); 06="ent" general REFUTED
  (N19), restricted-"ent" PLAUSIBLE on the 3 -ment trigrams; the specific
  /mɑ̃/ "demand-" model KILLED by crib contradiction (N17). Neither side holds
  CONFIRMED on 06. Polyvalence remains the live mechanism — plausible, not
  confirmed. Identify the stem via 06→29×5 (infinitive frames) in round 4.
- **F26 (2026-10-07, crowd3/red-team):** methodology flags — (1) phase→position
  instrument VOID (N15); (2) the 'er' 67× segmentation mismatch uncalibrates ALL
  "er"-rate checks; (3) the crib writes mute -e (40="e" in "première") — kills
  phonetic mute-e models cleanly; (4) V29 contaminated; (5) mixed-register
  modeling is principled as a ROBUSTNESS check (24-union still empty = strong
  null) but not as a confirmation instrument; (6) the closer's .md steelman
  ratios (1.15×/1.10×) do not reproduce from archived code (JSON: 1.89×/1.98×,
  que-leg at band edge) — traceability violation; trust the JSON.
- **F27 (2026-10-07, crowd3/closer; red-team: DEMOTED CONFIRMED→provisional-
  strengthened):** 87="ce" stays provisional. Three new legs: N1 rival-kill —
  P(46|87)=3/32 and P(64|87)=5/32 with 95% CIs; all six rival function words
  fall outside both intervals, several at register-independent grammatical
  zero ("le qui", "je que"); only "ce" makes {cela, ce que, ce qui} all
  grammatical — UPHELD in substance (que-leg at band edge per JSON);
  N2 exhaustive inversion — ~4,000 era words on {P(que|W), P(qui|W)}, "ce" the
  only n>100 passer — UPHELD; N3 96-frame ("parce que" ×3) — admitted CIRCULAR
  (conditions on 96="par"). R1 "corroboration" recycled the dead 24="est"
  number — void. Residual caveat: the cela leg is dialogue-register (era fails,
  Les Mis passes; corroborates round-2's "est ce" register finding; favors no
  rival). Dependency chain: 87="ce" provisional → 64="qui" re-promotion BLOCKED
  (new anomaly: 64→77×3 vs era P(pas|"qui")=0/2360; "même" rival live) →
  96="par" keeps CONFIRMED on the repaired leg → all drags inherit provisional.
  Inversion redo: 24's intersection stays EMPTY under era, Les Mis, and the
  union model — 24 is likely not a plain function word.
  Evidence: `code/crowd3/closer_results.{md,json}`.
- **F28 (2026-10-07, crowd3/closer C1, curator-verified):** F19 correction —
  the "parce" rate was miscomputed as 132/1036 (n("parce") used as the bigram
  count); true word-space P(ce|par)=13/1036=0.0125 (an 11.4× fail). The
  syllabary-aware repair gives P(87|96)=0.1429 vs predicted 0.1130 (1.26×).
  96="par" CONFIRMED stands on the repaired leg.
- **F29 (2026-10-07, crowd3/segmenter; red-team-3b: PARTIAL accepted):**
  semi-Markov forward-backward with unsupervised EM-fit boundary rates
  (rotation-break assumption only — honors the tuner NULL). Ground-truth
  "la"+"première" @1033: 3/3 boundaries ≥0.5 out-of-sample, la|première split
  0.937 unprompted. The 5/23 provisional-boundary miss is NOT anti-evidence:
  metric muddling (cela-internal 7/7 <0.5 is the model correctly not splitting
  "cela" — mildly favors "cela" one word), weak rotation-break at parce|que,
  and the inconsistent-segmentation enlightenment predicts exactly this failure.
  Lengths sane (958 words, mean 1.93 vs era 1.75, chi²=121.8); π_C=0.578
  highest — C as word-final-ish, unprompted. **25 crib-drag targets cleared as
  LEAD-grade** (@1110-1112 [41 65 38], @81-83 [51 62 16] first; pre-registered
  control required per the scorer lesson; provisional-touching targets inherit
  provisional uncertainty).
  Evidence: `code/crowd3/segmenter_results.{md,json}`.
- **F30 (2026-10-07, crowd3/red-team-3b): lane position — rigid syllabification
  is DEAD as an instrument.** Three independent lines converge: tuner NULL
  (N15), the calibration mismatch (N22), and the frenchman's enlightenment
  (the encipherer spells by ear and cuts inconsistently — « personne » in two
  spellings in one cipher, « prend »→« pre », « pre|m|i|er|e »). What survives:
  cipher-side geometry, word-space grammatical kills, ear/formula locks, era
  unigrams as context. **Round-4+ rule:** no era-syllable-conditional legs on
  morphological fragments (29/82/34 excluded; 40-conditionals excluded); era
  word-space legs survive; fragment hypotheses test against the recovered
  syllabary (`data/upstream-syll*.py`, tuner step 2).
- **F31 (2026-10-07, crowd3/frenchman; red-team-3b: merged).** Ear-confirmations
  (87="ce", 64="qui", 96="par", 94="ne") = independent corroboration, NO
  status changes. K1 accepted (converges with N19; @1181 shows polyvalence
  naked); K2 accepted scoped (24="de" in « en ce qui »); K3 conditional only;
  K4 accepted provisional (01="ci" kill); K5 accepted scoped (forces 52
  polyvalence); K6 no action (honesty noted); K7 rejected. Leads:
  **24="en" STRONG** (sharpest ear-vs-stats tension: 24→87×10 at 26–31× over
  era P(ce|en); failed L2prov does not kill the lead); **52="pas" STRONG,
  bounded** (rival 52="se" stays LEAD); **62="on" STRONG** — strongest of the
  batch (ear lock + 62→94 "on ne" ×8 at 1.97× in-band; one independent check
  from promotion); 37="le"/01="est"/56="plus"/43="me" MEDIUM; 17="fois" WEAK;
  94="en" islets LEAD-grade conditioned polyvalence (@1168 « en ce 83 »,
  @1575 « m'en 76 »); @1741 unresolved under both readings. 64→77×3 reclassified
  as a **77-problem** (« qui [verbe] ») — pressure on 64 dissolves, re-promotion
  stays blocked. Register reclassified: the cela gap is **genre** (reporter's
  event-anaphora), not formality — expect political lexicon, diplomatic
  formulae, subjunctives; don't expect slang/« ça »/dropped « ne ».
  Evidence: `code/crowd3/frenchman_results.{md,json}`.
- **F32 (2026-10-07, key-hunt side fleet, red-team methodology ruling R1 —
  CANONICAL PARSE REPAIR):** the lane's 1,846-pair parse contradicted manuscript
  gloss (i) — erased pencil "la pre m i er e" over `11 70 82 34 29 40` on row
  a5_03, where the raw 12-digit crib `117082342940` starts at raw offset 1532
  (even), requiring EVEN pair-phase; upstream's EM choice `offsets['a5_03']=1`
  made it ODD. Repair: flip a5_03 1→0 (removes 2 dropped digits, an even count;
  all rows after keep exact pair sequence). **New canonical facts: 1,847 pairs;
  `11 70 82 34 29 40` at pairs 754 (a5_03, the gloss line) AND 1034 (a6_03) —
  "la première" TWICE; a8_05 still ends `46` (@1692); same 96 groups, same pair
  IC.** Old "1,846 pairs / pair 1033" facts SUPERSEDED everywhere. Re-index rule
  (0-based): old n<748 unchanged; 748–772 = repaired region (re-paired, re-examine);
  old n≥773 → n+1. Full remap: `code/crowd4/REINDEX.md`. Related fix:
  `code/crib_attack.py::qscore` always returned the floor constant (−7.71) — the
  quadgram table is nested under 'logp'; one-line fix applied. Caveat: manuscript
  images not re-examined — if the a5_03 gloss line-tag is wrong, the old parse
  revives. Evidence: `code/side-keyhunt/methodology-ruling.md`,
  `code/side-keyhunt/repair_parse.py` (asserts pass),
  `code/side-keyhunt/repaired_offsets.json` (now canonical).
- **F33 (2026-10-07, crowd4/red-team): lane position — polyvalence is
  CONDITIONED, not free.** 3 of 25 identified groups (12.0%) carry ≥2 live
  readings, each with a verified positional/lexical conditioning rule
  (06: trigram-internal "ent" vs verb-stem class, with naked adjacency of the
  two readings; 52: "pas" iff negation-frame vs "so"/"se" elsewhere; 94: "ne" vs "en"
  islets iff pre=82/suc=87). **Zero cases of free polyvalence.** The 96-group
  code is therefore information-lossless in principle — recoverability is
  bounded only by key identification, now at **35.2% token coverage**. Two
  nulls recorded honestly: the kill-rate null does NOT reject misreading on
  count alone (κ≈0.324, p≈0.095); the exemplar-direction null REJECTS
  ear-cutting-inconsistency-alone — the encipherer's demonstrated noise is
  allophony (1 sound→N groups; "personne" ×2 keeps 94 for the unchanged sound)
  while every double runs the reverse (1 group→N distinct sounds). Falsifiable:
  a single verified case of unconditioned 1-group→2-sounds breaks it.
  Evidence: `code/crowd4/analyze_polyvalence.py`, `code/crowd4/red_team_rulings.json`.
- **F34 (2026-10-07, side-wordpattern/overwatch): @507 NULL reframed** — matches
  no French ?-on-ne word, but it is NOT a 77-datum: holds for every first
  syllable; fully explained by the per|son|ne vs pers|on|ne cutting mismatch.
  Corroborates F30 (rigid syllabification dead), nothing more. Evidence:
  `code/side-wordpattern/redteam/ADJUDICATION.md`.
- **F35 (2026-10-07, side-keyhunt/overwatch): R5005's 96-group shape belongs to
  the documented French *petit-chiffre* tier** (~100-cell routine-correspondence
  class). Structural priors for the lane: sparse homophones on frequent
  syllables (a 1690 royal order *mandated* homophone use — consistent with
  F33's conditioned polyvalence); French tradition used nulls but the
  petit-chiffre table has NONE (matches upstream's null-digit negative —
  don't hunt nulls); word-family packing, i.e. one group = an inflected family
  (supports reading 06/86 as stem allomorphs rather than separate syllables);
  two-part tables (chiffrante/déchiffrante); grand/petit tiering was formal
  doctrine. Reference table: Petit Chiffre de la Grande Armée, 144 groups,
  transcribed from the ARCSI reproduction of Bazeries 1901 pp. 275–277 —
  RULED OUT as R5005's key (0/7 anchors: 11 absent; 70→ei, 82→es, 34→at,
  29→bi, 40→co, 46→1), anachronistic, addressing-incompatible; stands as
  family reference. Evidence: `code/side-keyhunt/tables.md`,
  `code/side-keyhunt/tables/petit-chiffre-grande-armee.json`,
  `code/side-keyhunt/verdict-petit-chiffre.md`.
- **F36 (2026-10-07, side-keyhunt/overwatch): clean negative — no published
  French diplomatic syllabary/code table of 1830–1848 exists** in the
  searchable literature. Kahn's French material is all Rossignol/black-chamber
  era; DECODE's own R5005–R5008 records have empty Key: fields (verified
  live); no July-Monarchy code-system description found. One false lead killed
  (Palluel's *Dictionnaire* is Napoleon's sayings, not a codebook). The
  literature key-hunting channel is exhausted — do not repeat without a new
  source class. Evidence: `code/side-keyhunt/search-log.md` (20 queries +
  13 source checks).
- **F37 (2026-10-07, side-wordpattern/overwatch): the syllable inventory must
  be learned from the cribs, not adopted from standard French.** The
  encipherer chunks by ear: standalone 'm' as a syllable is phonotactically
  impossible in French but real here, proven by the pencil cribs — which is
  why the ground-truth "première" tail returns zero hits in any standard
  French syllabified lexicon. Any instrument assuming standard syllabification
  (rate legs, drags, scorers, solver inventories) is searching the wrong unit
  space. Reusable: the 11,870-word pattern lexicon (31 orth / 36 phon keys,
  `code/side-wordpattern/lexicon/`) and the polyvalence-expansion method with
  R1–R8. Cross-fleet status (2026-10-07): the homophonic solver's inventory
  (`solver.py::load_inventory` from `data/upstream-syll.py` UNITS +
  scorer_smith syllabifier) is NOT crib-learned — flagged to that fleet via
  `code/crossfleet/memo-crib-inventory-to-homophonic.md`; its real-data adapter
  (`ct_loader.py`) still uses the pre-repair offsets — flagged via
  `code/crossfleet/memo-parse-repair-to-homophonic.md`. Evidence:
  `code/side-wordpattern/redteam/ADJUDICATION.md`, `code/crossfleet/`.

## Open hypotheses (not promoted — each needs ≥2 independent checks)
  Round-4 status after red-team adjudication (2026-10-07, 8/8 executors merged;
  canonical parse repaired mid-round per F32 — positions below use the repaired
  1,847-pair indexing unless marked "old"):
- H1: **24="est" — REFUTED** (N10, F20). 24 unidentified; with 87=ce
  strengthened-provisional, the closer's inversion redo (empty under era,
  Les Mis, AND the mixed-register union model) says 24 is likely NOT a plain
  function word (F27). New STRONG lead: **24="en"** (F31 — « en ce qui » ×2,
  « en plus » @73, « qu'en 85 » @952; rank-2 2.82% fits; the rate tension
  24→87×10 at 26–31× over era P(ce|en) does not kill it). 24="c'est" REFUTED
  (28.9×). 24="de" scoped kill inside « en ce qui » (N23).
- H2: **77="pas" — DISFAVORED (strong)** (N21, N25). 77="que": disfavored stands.
  77="le": **LEAD** (promoted from LEAD-weak, N25; red-team ACCEPT fenced —
  77→86 ×5 = "le"+verb-stem object-pronoun frame). Direction: 77 is verb-adjacent
  (« qui [verbe] » + verb-stem predecessors 06×6, 67×6).
- H3: **06 — working state F25+N29**: verb-stem (class) PROVISIONAL general
  reading; /mɑ̃/ "demand-" KILLED (N17); 06="ent" general REFUTED (N19),
  restricted-"ent" PLAUSIBLE on the three 94-82-06 trigrams. 06="ne" dead.
  Specific stem bounded, NOT identified (66× rate gap vs "demand*").
  **06/86 complementary distribution** (N29): 06 = finite/imperative stem,
  86 = infinitive-complement stem (00→86 ×12 vs 00→06 ×0). Parse-repair
  correction: 06→29 is ×4 (the old 5th was an off-phase artifact).
  Polyvalence now QUANTIFIED as conditioned (F33), not merely plausible.
- H4: **96="par" — CONFIRMED 4/4**, provisional-inherits-87=ce-status, on the
  repaired C1 leg (F28). 96="de" REFUTED (N14). Tension: "ce qui 96 47 que"
  wants a verb.
- H5: **REFUTED** (N11). Replaced by R4 "-ment" family: **94="ne"
  provisional-strong** (F24, N24 — holds on rebuilt F30-legal legs), 82=m ✓,
  06="ent" restricted. Rival **94="re" DEMOTED → disfavored** (N24; 2.27:1
  host odds for "ne", 0/36 composing instances; fence: @578 trigram host).
  94="en" coexists as a CONDITIONED islet (pre=82/suc=87, 4/4); co-value
  promotion DENIED (independence fail, N31).
- **78="me" — LEAD** (promotion REJECTED, N20; N25 — B-78b fix verified, no
  reversals): rival "l'" killed (58×), rival "e" live; new adverse 77→78 ×7
  frames fenced on unconfirmed 78 ("pas me" era-0); 2/7 inside the
  "gouvernement" trigram → 78="ver" word-internal hypothesis open.
- **62="on" — STRONG LEAD** (N28; red-team: promotion NOT granted): ear lock +
  62→94 "on ne" ×8 at 1.99× (old parse; **9/35=0.2571, 2.18× era on the
  repaired parse** — curator) + fresh-window subject triangulation
  (@845–853 "…par écrit, on me [dit]…", zero counterexamples in 26 windows,
  /ɔ̃/ rivals killed). Held: legs 1&3 share the ear instrument — promotion
  needs an instrument-independent third leg (round-5 target).
- **52="pas" — STRONG, bounded** (F31; rival 52="se" stays LEAD; K5 forces
  52 polyvalence; F33 conditions it: "pas" iff negation-frame).
- 64="qui": provisional-FAVORED (N27); re-promotion BLOCKED; rival
  **64="même" DEMOTED → disfavored** (bounded, not killed). 64→77×3 =
  one byte-identical trigram 64-77-84 ×3 (n_eff=1 — prior rate arguments
  triple-counted). New corroboration: 87-64-77-84 @1800–1803 = «ce qui
  [verbe] 84».
- 87="ce": provisional, strengthened (F27); register-matched subset FAILs
  pre-stated bar, ci/te scan NULL — cela leg stays dead (N27). Resolving 87
  remains the lane's central open problem.
- 67="veut": provisional (demoted from CONFIRMED, N18); 67="re" is a 1-leg
  lead ("les" killed 35.5×); modal-governor + 06 lexical-stem is the live
  verb-system picture.
- **47="ce" — LEAD** (N29; polyvalent with 87): 47="me" as uniform word
  KILLED (3 independent); "ce que" 3/28=0.1071 vs era 0.1076 → 1.00× exact;
  @148–150 jar BOUNDED (@150–152 = "par ce que" ✓).
  01="ci": provisional kill (N23); 01="est" MEDIUM lead; 43="me" MEDIUM
  (« il me [v] » @43); 43="parmi" conditional kill; 37="le"/56="plus" MEDIUM;
  74="te" lead; 21="me" lead; 17="fois" WEAK; @1742 (old @1741) unresolved
  under both readings.
- 24→87→64 ×3 formula: promoted, value withheld (F17). 64 96 43 87 01 ×2:
  "qui … ce" reverse joints (F18). 41="der"/08="ni" INCONCLUSIVE (n=1) —
  refuted as general readings. 00 and 24 remain the top-frequency unknowns.
- **Lane instrument position (F30):** rigid syllabification DEAD — no
  era-syllable-conditional legs on morphological fragments (29/82/34 excluded;
  40-conditionals excluded); era word-space legs survive; fragment hypotheses
  test against the recovered syllabary (`data/upstream-syll*.py`).

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
Crowd round (2026-10-07) — nine executors, coordinator-curated; each wrote only to
`code/crowd/<name>_results.{md,json}` (the curator alone edited NOTES.md/STATE.md):
  code/crowd/phonotactician.py, phonotactician_results.{md,json}
  code/crowd/crib_surgeon_results.{md,json}
  code/crowd/contactor.py, contactor_results.{md,json}
  code/crowd/red_team_results.{md,json}
  code/crowd/drag_racer_results.{md,json}
  code/crowd/historian_results.{md,json}
  code/crowd/formula_hunter_results.{md,json}
  code/crowd/anneal.py, annealer_results.{md,json}
  code/crowd/linguist_results.{md,json}
  (plus __pycache__/ — regenerable, not evidence)
Era-matched reference corpus (attempt 3, 2026-10-07) — Tocqueville, *De la démocratie
en Amérique*, Tomes 1+2 (French, 1835/1840), formal political prose, 214,861 words.
Supersedes Les Mis as the rate reference (era + register match to the 1841 despatch):
  fafebe4f69bc8e7abc6ed95bd10c2257bd26a307b2c1071056187ef76154aeaa  data/gutenberg-30513-tocqueville-t1.txt
  20e46d72bc398f1c903449908a35a691e0d32763234bc75b2376cd21dbe33ee9  data/gutenberg-30514-tocqueville-t2.txt
  (provenance: data/PROVENANCE-tocqueville.txt; hashes appended to data/SHA256SUMS.txt)
Attempt 3 outputs: `code/attempt3.py`, `data/attempt3_results.json`.
Crowd round 2 (2026-10-07) — six executors, coordinator-curated; each wrote only to
`code/crowd2/` plus a report-inbox note per REPORTING.md
(`code/crowd2/report_inbox/<name>-<topic>.md`, swept into REPORT.md every 2h):
  code/crowd2/closer.py, closer_results.{md,json}
  code/crowd2/formula_tester.py, formula_tester_results.{md,json}
  code/crowd2/context_miner.py, context_miner_results.{md,json}
  code/crowd2/scorer_smith.py, scorer_smith_results.{md,json}
  code/crowd2/hypothesis_sweeper.py, hypothesis_sweeper_results.{md,json}
  code/crowd2/red_team.py, red_team_results.{md,json}
  (plus __pycache__/ — regenerable, not evidence)
Crowd round 3 (2026-10-07) — nine executors, coordinator-curated with red-team
adjudication; each wrote only to `code/crowd3/` plus a report-inbox note per
REPORTING.md (`code/crowd3/report_inbox/<name>-<topic>.md`, swept into REPORT.md
every 2h). Merged 6/9 at checkpoint (frenchman, segmenter, bigram-closer pending):
  code/crowd3/closer.py, closer_results.{md,json}
  code/crowd3/morphologist_results.{md,json}
  code/crowd3/stem_hunter.py, stem_hunter_results.{md,json}
  code/crowd3/scorer3.py, scorer_smith_results.{md,json}
  code/crowd3/tuner.py, tuner_results.{md,json}
  code/crowd3/red_team_results.{md,json}
  Round-3 newcomers (operator order, merged after red-team-3b follow-up review):
  code/crowd3/frenchman_results.{md,json} (+ report_inbox/frenchman-ear-check.md)
  code/crowd3/segmenter_results.{md,json} (+ report_inbox/segmenter-word-boundaries.md)
  code/crowd3/battery.py, bigram_closer_results.{md,json} (+ report_inbox/bigram-closer-anchor-factory.md)
  code/crowd3/red_team_round3b_results.{md,json} (+ report_inbox/red-team-round3b.md)
  (plus __pycache__/ — regenerable, not evidence)
