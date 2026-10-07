# STATE — zeschau-seebach-1841

- **status:** `cracking` (attempt 3 done 2026-10-07: 64=qui confirmed 4/4 as provisional
  anchor 9; 87=ce re-validated 3/4 vs era-matched Tocqueville corpus; drag still null)
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
- **next:** Attempt 4 — exploit 64=qui: examine the five "ce qui" contexts and the
  followers of 64 for verb-group candidates; profile joint 87/64 ("ce"/"qui") windows
  for further function words; re-examine 82→16 in qui-anchored windows (it avoids
  ce-windows entirely); consider a syllable-level scorer to replace the shelved
  window-quadgram drag. Do NOT promote anything without ≥2 independent checks.
- **blockers:**
  - R5006–R5008 (sibling letters, 2+3+3 pp) NOT obtainable: DECODE records public at
    de-crypt.org/decrypt-web/RecordsView/{5006,5007,5008} but all "Authentication required";
    200×150px thumbnails are public (verified) yet unusable for transcription; full-size image
    URLs return a black 986×568 placeholder without a session. Needs DECODE login or an HStAD
    (Dresden) scan order. Checked 2026-10-07.
  - No 1840s Saxon key on DECODE (latest Dresden key 1799–1806, different fonds).
  - Erased pencil decipherment would need UV/multispectral imaging (physical access, HStAD).

## Standing facts (do not re-derive)
- Target: Heinrich Anton von Zeschau (Dresden) → Albin Leo von Seebach (St Petersburg), 18 Jan 1841 – 26 Oct 1843. Shelfmark: HStAD 10731 Sächsische Gesandtschaft in Russland, Nr. 12. DECODE R5005–R5008.
- R5005 (18 Jan 1841): whole despatch, 70 lines, 3,969 unseparated digits, language **French**. R5006 (6 Apr 1842): French clear + 8+3 cipher lines. R5007 (13 Jun 1842): German, ~10 cipher lines. R5008 (26 Oct 1843): German, 5 cipher lines.
- Cipher: two-digit syllabary (letters + syllables mixed), 96/100 groups used, plain pairs only.
- Seven crib values from erased pencil decipherment: 11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que ("la première … que").
- Prior work (Bourdeau, Sept 2026): every Dresden DECODE key checked (latest 1799–1806, none for fonds 10731); homophonic letter solver with French 4-gram fails on R5005 (−3.05 to −3.17/letter vs −2.18 control); syllable solvers with 7 glosses fixed drift to fluent nonsense. Not repeated here without a new idea.
- Long repeats: `7778948206` ×5, `06777818711001` ×3 — probable names/set phrases.
