# STATE — zeschau-seebach-1841

- **status:** `cracking` (crowd round 2 done 2026-10-07: 6 executors, coordinator-curated;
  10 provisional values — 7 pencil cribs + 87=ce (provisional) + 64=qui (provisional) +
  96="par" (provisional, NEW); red team demoted 24="est" (refuted) and 64="qui"
  (CONFIRMED→provisional); H5 "J'ai l'honneur de" killed; scorer broken-on-control;
  first byte-level word read "la première" @1033 stands)
- **checkpoint:** Transcription fetched, hashed, verified (3,764 digits / 1,846 pairs / 96 groups).
  Attempt 1 (`code/crib_attack.py`) complete: repeats corrected to 2×/0× at pair alignment (F3);
  digit-count discrepancy 3,764 vs 3,969 recorded (F4); bigram 82→16 at 29% flagged (F5);
  function-word drag null at 7-anchor sparsity (N1). Results in `data/attempt1_results.json`.
  Attempt 2 (`code/attempt2.py`) complete: **87="ce" CONFIRMED (4/5)** — "cela" ×7 and
  "ce que" ×3 at Les-Mis-matching rates; joins as lane-inferred provisional anchor
  (8 anchors total; F6). 87="de"/"à" REFUTED by 87→que ×3. H1 (82→16 as "ma") PLAUSIBLE
  (1/4), not promoted (F7). Drag re-run with 8 anchors still degenerate (N2).
  Results in `data/attempt2_results.json`. French reference: Les Mis Tome 1 in `data/`.
  Attempt 3 (`code/attempt3.py`) complete: era-matched reference built — Tocqueville
  *Démocratie en Amérique* Tomes 1+2 (1835/1840, formal prose, 214,861 words;
  `data/PROVENANCE-tocqueville.txt`, sha256 in `data/SHA256SUMS.txt`). Rate comparison
  vs Les Mis: P(que|ce), P(qui|ce), P(la|de), P(la|à) all agree within factor 2;
  n("cela")/n("ce") disagrees 6.7× (0.041 era vs 0.278 Les Mis) — register gap (F10).
  **64="qui" CONFIRMED (4/4)** — 87→64 ×5, P(64|87)=0.1562 ≈ era P(qui|ce)=0.1878
  ("qui" is the #1 follower of "ce" in Tocqueville); rank(64)=4 vs era rank("qui")=13;
  46=que→64 = 0; 28 followers/28 predecessors. Joins as provisional anchor 9 (F9).
  87=ce re-validated 3/4 on era rates (cela-leg downgraded to register-dependent, stands).
  Drag re-run with 9 anchors still null — no candidate separates (N3). Bonus: 82→16
  never occurs within ±3 groups of 87=ce (0/11). Results in `data/attempt3_results.json`.
  **Crowd round** (9 executors, `code/crowd/`, coordinator-verified then merged):
  - 87=ce DEMOTED by Red Team (F6 revised): attempt-2's "P(cela|ce)=0.278" was a count
    ratio, not a conditional (honest syllable bound 0.1805 < observed 0.2188 — check void);
    checks (a)/(d) non-discriminating; (c) weak (n=3). No alternative beats ce. Reframing:
    P(46|87,pre=96)=3/3 vs pre=24 0/10 — "que" licensed by 96, never 24. Status:
    provisional, best-tested, cela-leg register-dependent (attempt 3 re-validated 3/4).
  - "la première" = 11-70-82-34-29-40 exactly once @pair 1033 — byte-level confirmed
    from ground-truth anchors; mid-letter back-reference (F12, curator-verified).
  - 3-phase rotational contact structure A→C→B→A (chi²=181.3, 4df; F11); 29=er anchors
    phase C (word-final-ish); 87↔82 strongest anchor-anchor Jaccard (0.423).
  - Phonotactic search NULL (N4 — scorer exploited); syllable-bigram annealing
    method-broken-on-control (N5 — synthetic control 1/88 ≈ chance); syllable drag
    PARTIAL (N6 — discriminates but word-prior, not placement); no 1840s Saxon key
    published (N7); contact predictions P1/P2 failed as stated (N8); no que near the
    crib, no second "première" (N9).
  - New hypotheses (not promoted): 24="est" (4 checks, strong — if confirmed, 24-87-46
    0/10 becomes a joint contradiction for 87=ce); 77="pas" (3 checks); 06="ne"
    (3 checks); 96="par"/"de"; 41="der"/08="ni"; ×5 repeat 77 78 94 82 06 =
    "J'ai l'honneur de" (linguist).
  - Historian: identities established (Zeschau 1789–1870; Seebach 1811–1884, envoy
    St Petersburg 1839–1852); DECODE registration free/self-service (unlocks R5006–R5008);
    HStAD mail-in scan order (poststelle@sta.smi.sachsen.de), shelfmark 10731 Nr. 12;
    key-candidate files 10731 Nr. 12 + 10717 Nr. 3332/3333 (F16).
  **Crowd round 2** (6 executors, `code/crowd2/`, coordinator-verified then merged;
  all headline cipher-side numbers re-derived by curator — verified):
  - Closer: **24="est" REFUTED** (N10) — all four H1 checks fail/downgrade on era
    rates (19.5×, 74× fails; rank "1" was 0-based); structural refutation legs
    (C-check, 11=la ×4 predecessor kill) instrument-independent; rivals (sont/ont,
    c'est, de, en) all die; 45-word inversion sweep: no era word fits
    P(ce|V)≈0.19 ∧ P(V|que)≈0.10 — empty intersection points back at provisional
    87=ce. 24 unidentified.
  - Formula Tester: **H5 "J'ai l'honneur de" REFUTED** (N11) — kill-grade: 82='m'
    ground truth vs needed "neur"; 67×/184×/47× rate failures. Surviving: 77→78
    "j'ai l'" chunk, 78-as-proclitic. 9-mer drag NULL (best candidate killed on
    00="fé" 15× and 21="ce" collision).
  - Context Miner: **24→87→64 ×3 formula promoted (value withheld)** (F17);
    **64 96 43 87 01 ×2 reverse joints** (F18); 82→16 vs qui-windows null (N13);
    16="a" not promoted. Tension for 96="par": "ce qui 96 47 que" wants a verb.
  - Scorer Smith: **syllable scorer BROKEN-ON-CONTROL** (N12) — top-1 0.021 <
    chance; real drag not run. Diagnosis: placement ties; missing signal is global
    consistency of implied assignments. Bonus inference: encipherer stripped
    final "-er" (F22).
  - Hypothesis Sweeper: **96="par" CONFIRMED (4/4) → 10th provisional value**
    (F19; inherits 87=ce's provisional status). 96="de" REFUTED (N14). 77="pas"
    INCONCLUSIVE (survives; partner 06 probably not "ne"). 06="ne" INCONCLUSIVE —
    **new lead: 06 = verb stem** (F21). Six rivals killed; 77="que" reopens if 06
    revalued.
  - Red Team: **24="est" DEMOTED** (refuted as 4-check case); **64="qui" DEMOTED**
    CONFIRMED 4/4 → PROVISIONAL (F20); **H5 KILL** (corroborated); **factor-2 band
    UNCALIBRATED**; **F13 joint contradiction DISSOLVED** (era binomial 0.247).
- **next:** Round-3 work orders (crowd round 2 curation 2026-10-07):
  1. **Test R4 "-ment" family** (94=ne, 82=m ['m' ground truth ✓], 06=ent) as its own
     work order — the 2 extra 94→82 instances (@578/@1181) are the test bed; check
     ent/ment word-final behavior against 29=er's phase-C anchor (F23).
  2. **Pursue 06 verb-stem lead** (F21): profile 06's full follower set against
     verb-stem expectations; resolve companion unknown 67; re-test 77="pas"/"que"
     under verb-stem 06.
  3. **Redesign scorer with global-consistency signal** (scorer smith's direction):
     check whether X='d' reads as 'd' everywhere X occurs — the missing signal.
  4. **Resolve 87=ce's provisional status** — the lane's central open problem: the
     closer's empty inversion intersection points back at it; 96="par" and 64="qui"
     inherit its uncertainty. Test 87 against non-"ce" function words with equal rigor.
  5. **DECODE registration** (parent handling via browser task, in flight) → R5006–R5008
     full images; **HStAD scan order** for 10731 Nr. 12 + 10717 Nr. 3332/3333.
  Do NOT promote anything without ≥2 independent checks. New standing convention:
  every executor leaves a report note at `code/crowd2/report_inbox/<name>-<topic>.md`
  per REPORTING.md (swept into REPORT.md every 2h).
- **blockers:**
  - R5006–R5008 (sibling letters, 2+3+3 pp) NOT obtainable: DECODE records public at
    de-crypt.org/decrypt-web/RecordsView/{5006,5007,5008} but all "Authentication required";
    200×150px thumbnails are public (verified) yet unusable for transcription; full-size image
    URLs return a black 986×568 placeholder without a session. Checked 2026-10-07.
    **Route now concrete (crowd/historian):** DECODE registration is free and self-service
    at https://de-crypt.org/decrypt-web/register (email + activation link) — needs
    BigSexyWarlock69's word (standing rule: no personal info into new accounts). Alternative:
    HStAD Dresden mail-in scan order ("Antrag auf Herstellung von Kopien" →
    poststelle@sta.smi.sachsen.de) for 10731 Nr. 12 + 10717 Nr. 3332/3333.
  - No 1840s Saxon key on DECODE (latest Dresden key 1799–1806, different fonds).
  - Erased pencil decipherment would need UV/multispectral imaging (physical access, HStAD).

## Standing facts (do not re-derive)
- Target: Heinrich Anton von Zeschau (Dresden) → Albin Leo von Seebach (St Petersburg), 18 Jan 1841 – 26 Oct 1843. Shelfmark: HStAD 10731 Sächsische Gesandtschaft in Russland, Nr. 12. DECODE R5005–R5008.
- R5005 (18 Jan 1841): whole despatch, 70 lines, 3,969 unseparated digits, language **French**. R5006 (6 Apr 1842): French clear + 8+3 cipher lines. R5007 (13 Jun 1842): German, ~10 cipher lines. R5008 (26 Oct 1843): German, 5 cipher lines.
- Cipher: two-digit syllabary (letters + syllables mixed), 96/100 groups used, plain pairs only.
- Seven crib values from erased pencil decipherment: 11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que ("la première … que").
- Prior work (Bourdeau, Sept 2026): every Dresden DECODE key checked (latest 1799–1806, none for fonds 10731); homophonic letter solver with French 4-gram fails on R5005 (−3.05 to −3.17/letter vs −2.18 control); syllable solvers with 7 glosses fixed drift to fluent nonsense. Not repeated here without a new idea.
- Long repeats: `7778948206` ×5, `06777818711001` ×3 — probable names/set phrases.
