# STATE — zeschau-seebach-1841

- **status:** `cracking` (attempt 1 done 2026-10-07: verification + anchor profiling solid; function-word drag null)
- **checkpoint:** Transcription fetched, hashed, verified (3,764 digits / 1,846 pairs / 96 groups).
  Attempt 1 (`code/crib_attack.py`) complete: repeats corrected to 2×/0× at pair alignment (F3);
  digit-count discrepancy 3,764 vs 3,969 recorded (F4); bigram 82→16 at 29% flagged (F5);
  function-word drag null at 7-anchor sparsity (N1). Results in `data/attempt1_results.json`.
- **next:** Attempt 2 — test 82→16 and 87→11 as anchor *hypotheses* (not cribs): fit candidate
  French syllables/words against bigram-frequency expectations; if either resolves plausibly,
  re-run the drag with 9 anchors. Do NOT promote hypotheses to anchors without a second
  independent check.
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
