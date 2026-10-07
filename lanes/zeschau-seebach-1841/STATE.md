# STATE — zeschau-seebach-1841

- **status:** `cracking` (crowd round 4 COMPLETE 2026-10-07: 8/8 executors merged after
  red-team adjudication (4 rulings + homophony position). Net: ZERO promotions — the
  bar held. Kills: 47="me" (uniform word, 3 independent). Demotions: 94="re"
  live-rival→disfavored, 64="même" LEAD→disfavored (bounded). 77="le" LEAD-weak→LEAD
  (accepted fenced). 62="on" third leg FOUND but promotion NOT granted (legs 1&3 share
  the ear instrument) — stays STRONG LEAD. 94="en" co-value DENIED (independence fail).
  **Canonical parse repaired mid-round (F32):** 1,847 pairs; "la première" TWICE
  (@754 and @1034); all positions re-indexed (`code/crowd4/REINDEX.md`).
  10 values: 7 pencil cribs (ground truth) + 87=ce (provisional-strengthened) +
  64=qui (provisional, re-promotion BLOCKED) + 96="par" (CONFIRMED, inherits ce status).
  94="ne" provisional-strong; 47="ce" LEAD (new); 06=verb-stem-class provisional
  (06/86 complementary distribution discovered); 67="veut" provisional.
  Lane position: polyvalence CONDITIONED, not free (F33) — 3/25 groups (12.0%) with
  verified conditioning rules; code information-lossless in principle; 35.2% token coverage.
  Joint engine: model-correct, search-broken on control (identifiability — N30).)
- **checkpoint:** Transcription fetched, hashed, verified (3,764 digits / 1,847 pairs / 96 groups;
  repaired canonical parse per F32 — `code/side-keyhunt/repaired_offsets.json` supersedes
  `data/upstream-offsets.json`; "la première" @pairs 754 AND 1034).
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
  - "la première" = 11-70-82-34-29-40 TWICE @pairs 754 (row a5_03, the manuscript gloss
    line) and 1034 (row a6_03) — byte-level confirmed from ground-truth anchors; the
    a5_03 occurrence is a mid-letter back-reference (F12 as repaired by F32; old
    "exactly once @pair 1033" SUPERSEDED).
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
  **Crowd round 3** (9 executors, `code/crowd3/`, red-team adjudicated before merge;
  6/9 merged 2026-10-07 — frenchman, segmenter, bigram-closer still running):
  - Closer (resolve 87=ce): claimed PROMOTE→CONFIRMED on N1 (rival-kill CIs:
    P(46|87)=3/32, P(64|87)=5/32, all six rivals outside), N2 (exhaustive inversion,
    ~4,000 era words, "ce" only n>100 passer), N3 ("parce que" frame ×3). Red team
    DEMOTED → provisional-strengthened: N3 admitted circular; R1 recycled the dead
    24="est" number; .md steelman ratios don't reproduce from archived code (trust
    JSON: 1.89×/1.98×, que-leg at band edge). Repaired F19's "parce" miscomputation
    (C1 → F28: syllabary-aware 1.26×). 24-inversion stays empty under era, Les Mis,
    AND the union model — 24 likely not a plain function word (F27).
  - Morphologist (test R4 "-ment" family): corrected its own work order (94→82 is
    4× @[578,1181,1352,1741]; @1741 is 94-82-46, unparsed "i-ne-m-que").
    94="ne" CONFIRMED on 2 legs → red team DEMOTED to provisional-strong (leg 3
    used the tuner-falsified phase mapping; rival 94="re" live: "-rement" 1.28×
    vs "-nement" 0.66×) (F24). 06="ent" general REFUTED (red-team UPHELD) —
    plausible only on the three trigrams (N19).
  - Stem Hunter (06 verb stem, companion 67, re-test 77): 06=/mɑ̃/ "demand-"
    CONFIRMED → red team KILLED — crib contradiction: "première"=pre|m|i|er|**e**
    writes 40="e" for mute final -e, but the model needs mute-e unwritten
    (06→40→77 is 0×) (N17). 06=verb-stem class DEMOTED CONFIRMED→provisional;
    67="veut" →provisional; 77="pas" →inconclusive; 77="que" REFUTED→disfavored
    (N18). 06-tension adjudicated: F21 (verb stem, class) wins the general reading
    by worker convergence; 06="ent" general REFUTED (upheld); restricted-"ent"
    PLAUSIBLE on the 3 trigrams; neither side holds CONFIRMED on 06 (F25).
    New leads: 64="même" (rivals 64="qui"), 21="le/les", 00="de", 78="vrai".
  - Scorer Smith (global-consistency scorer, control-first): three variants
    BROKEN-ON-CONTROL (N16) — signal real but not distinctive; real drag not run.
    Missing ingredient: JOINT inference (annealing/EM over the full key).
    `scorer3.py` API banked as infrastructure. Red team UPHELD.
  - Tuner (what do the contact phases mean): NULL (N15) — leave-one-out
    phase-constrained 2/34 vs unconstrained 6/34; phases are NOT word-position
    classes (rotation itself re-verified, chi²=188.3). 'er' 67× segmentation
    mismatch uncalibrates corpus-tuned ranking generally. Red team UPHELD.
  - Red Team (13 rulings, kill authority): two kills, four demotions, zero new
    CONFIRMED promotions; methodology flags banked (F26): phase instrument VOID,
    'er'-rate checks uncalibrated, crib writes mute -e (kills phonetic models),
    V29 contaminated, mixed-register = robustness check only.
- **next:** Round-5 work orders (crowd round 4 COMPLETE, curation 2026-10-07).
  Canonical parse: repaired 1,847-pair (`code/side-keyhunt/repaired_offsets.json`);
  positions per `code/crowd4/REINDEX.md` (repaired indexing; old n≥773 → n+1).
  1. **Instrument-independent third leg for 62="on"** — the red team named the
     exact gap (N28): legs 1&3 share the ear instrument. A statistical/structural
     leg (not ear) promotes 62="on".
  2. **47="ce" promotion battery** — needs C2 explained ("..er→ce" 12.6×),
     unigram 2.87× addressed, and the 64-slot residual resolved (N29).
  3. **Identify the 06 stem** — 4 infinitive frames (06→29 ×4, repaired count);
     exploit the 06/86 complementary distribution (N29).
  4. **Resolve @578 trigram host** — the fenced 94="re" revival thread (N24).
  5. **78="me" vs 78="ver"** — adjudicate the 77→78 ×7 adverse frames; test the
     word-internal "ver" hypothesis from the "gouvernement" trigram (N25).
  6. **77="le" promotion battery** — 77→86 ×5 object-pronoun frame + L1 (N25).
  7. **Attack the identifiability problem** — the joint engine is model-correct
     but search-broken (N30): better search (parallel tempering, smarter
     proposals) or shrink the space with the F33 conditioning rules.
  8. **Mine the SECOND "la première" window** (@754, row a5_03 — never examined;
     it was off-phase before the repair): comparative context mining 754 vs 1034.
  9. **87=ce new angles** — cela leg dead (N27); pursue the 87-64-77-84
     @1800–1803 «ce qui [verbe] 84» corroboration (resolve 84?) or a
     non-circular anchor.
  10. **Exploit the stronger rotation** — recomputed phases give chi²=366.3
      (N30); cluster assignments are fragile but the transition structure is
      robust — find what the rotation IS if not word-position (tuner NULL stands).
  Do NOT promote anything without ≥2 independent checks. Standing convention:
  every executor leaves a report note at `code/crowd<N>/report_inbox/<name>-<topic>.md`
  per REPORTING.md (swept into REPORT.md every 2h). Red team reviews ALL promotions
  before merge — no claim merges without its ruling.
- **external acquisition: ON HOLD per operator directive (2026-10-07).** No new external material — the archive scan-order route (HStAD) and DECODE elevation are stood down. Round 3+ works with R5005 (3,764 digits) and the 10 current values only. (DECODE account "alexrivers" exists and logs in, but full-size private-ciphertext images need admin elevation — recorded in `code/crowd2/report_inbox/decode-access-2026-10-07.md`; not pursued further unless the operator reverses.)
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
