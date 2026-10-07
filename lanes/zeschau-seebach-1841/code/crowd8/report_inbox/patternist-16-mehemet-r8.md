## patternist: WO-11 (16="i" position test) + WO-12 (Mehemet-Ali discrimination, RdDM 293×)
Round 8 · 2026-10-07 · code: `code/crowd8/patternist/` (`PREREG.md` pre-registered
BEFORE data; `round8.py`; `round8_results.json`). Canonical repaired 1,847-pair parse.

- Context: WO-11 tests the position-conditioned rescue B1's clean fail redirects to
  (16=word-final /i/ vs 34=word-internal /i/); WO-12 discriminates "Mehemet-Ali" @8
  from common me-words and settles the F59-flagged "293× in Revue des Deux Mondes".
- Decision (a): the position-conditioned alternative is NOT SUPPORTED — 16="i" stays
  unconditioned LEAD. Decision (b): recommend DEMOTE "Mehemet-Ali" @8 LEAD→LEAD-weak
  (red team adjudicates); the RdDM 293× figure is VERIFIED, F59's UNVERIFIED flag LIFTED.

### WO-11: 16="i" position-conditioned test
- **T1 follower word-initial-anchor enrichment — FAIL (clean, wrong direction).**
  WI={'11','70','46','87','64','94','96','62'} (GT + provisional-or-better
  obligatorily word-initial function words). 2×2 table [[2,26],[2,9]] (16 vs 34
  followers in WI): one-sided Fisher p=0.9398, odds ratio 0.35 — the effect runs
  opposite to the split prediction. Sensitivities: S1 (GT-only WI) p=1.0;
  S2 (+77) p=0.87; S3 (drop parmi-window follower 16@1198→64) p=0.98. All fail.
  Observation (not scored — no reverse bar pre-reg'd): 34's two WI followers are
  34@1348→62 ("on") and 34@1741→94 ("ne") — word-initial anchors following the
  supposedly word-internal /i/, also awkward for the split.
- **T2 "premier"/"première" minimal-pair frame — UNINFORMATIVE (not scored).**
  70-82-34-29 (masc, P[i+4]≠40): 0; 70-82-16-29: 0; 70-82-16-29-40: 0;
  GT 70-82-34-29-40: 2. The masculine frame never occurs — the test can't fire.
- Why: two independent, pre-registered instruments; the distributional one fails
  in the wrong direction and the frame one is vacuous. The B1 redirect is exhausted.
  16="i" keeps its B2/B3 legs (unconditioned LEAD); no conditioned rule exists.

### WO-12a: Mehemet-Ali discrimination — the 62-tension (NEW adverse)
- **D1 62-tension CONFIRMED (adverse-moderate).** The claim's own tiling
  me|he|met|a|li on [78,18,93,62,98] assigns 62='a'; lane STRONG LEAD 62="on"
  (/ɔ̃/) assigns 62='on' — incompatible as single values (62 not in the F33
  polyvalence set). Robustness: by-ear top-8 tilings of "mehemetali"/"mehemedali"
  contain ZERO len-5 'me'-initial tilings — no alternative tiling within the
  lane's by-ear instrument avoids /a/ on 62. Escape hatch: 62 polyvalence
  (new posit) or 62="on" falls.
- **D2 common-word contrast CONFIRMED (adverse-moderate).** The 33 @8 fitters
  reproduce exactly (assert len(cells)==len(groups); 33/33). 62-cell distribution:
  e:8, i:8, r:3, g:3, t:2, n:2, qu:1, nu:1, z:1, en:1, c:1, s:1, on:1. ONE
  common-word fitter is fully compatible with 62="on": **"mêleront"**
  (me|le|r|on|t). The name is the candidate that destroys the lane's stronger
  claim while a common-word rival preserves it. (Name-like "mexique"
  me|x|i|qu|e also conflicts with 62="on".)
- Why: T7 left the name "possible, not preferred" with nothing adverse; the
  62-tension is genuine adverse — promotion is now blocked on 62="on" resolution.
  M2 (spelling/topicality) stands, so this is a demotion recommendation
  (LEAD→LEAD-weak), not a kill.

### WO-12b: RdDM "293×" — VERIFIED (exact)
- The corpus WAS on the VM: `code/side-period/corpus/revue-deux-mondes-1841-q1..q4.txt`
  (full 1841 run, 4e série t. XXV–XXVIII, archive.org OCR, provenance in
  `corpus/PROVENANCE.md`) — harvested 2026-10-07, after F59 was written.
- Exact count of the clean form **'Méhémet-Ali': 293** (q1:16, q2:15, q3:46, q4:241
  as 'méhémet[-\s]+ali' bigrams; form table: 'Méhémet-Ali' 293, 'Méhémet-\nAli' 16,
  'Mehemet-Ali' 7, 'Mehémet-Ali' 1, 'Mêhémet-Ali' 1). Cross-check: period fleet's
  mined bigram ('méhémet','ali')=297 (`work/mine-rdm/mine.json`); my recount 318
  incl. variants. The fleet's 293 = the clean accented-hyphenated form, exact.
- Bonus for M2: the accented-hyphenated spelling is DOMINANT in 1841 French print
  (293/318); the cipher's accent-stripped 'Mehemet-Ali' matches the 7 unaccented
  attestations' shape. Zero 'mohamed'/'mehemed' in the run.
- For the report: F59's "UNVERIFIED — do not cite" is superseded; the figure may
  now be cited as: 293× 'Méhémet-Ali' in the 1841 RdDM run (4 tomes, OCR).

### Enlightenment
A `grep -oi "m[ée]h[ée]met"` returned only 7 hits (all q4, unaccented) — nearly
producing a false "claim refuted" verdict. Cause: multibyte é inside a bracket
expression under the C locale silently fails to match. Python `re` found 353
mehemet tokens / 318 bigrams. Lane lesson: never trust grep character classes
with multibyte text on this VM; recount in Python.

### Caveats
- T1's WI set leans on provisional values (87/64/96/94/62); the GT-only
  sensitivity (S1) also fails, bounding the damage.
- D1's "no alternative tiling" is within the by-ear top-8 instrument only; the
  claim's me|he|met|a|li tiling is hand-made (absent from the tiler's top-8 —
  the tiler prefers letter-heavy cuts like me|h|e|m|e|t|a|l|i).
- The 62-tension assumes single-value 62; conditioned polyvalence dissolves it
  at the cost of a new posit.
- RdDM counts are OCR-based (Internet Archive djvu.txt); 293 is the clean-form
  count — cite with the OCR caveat.
- No status changes applied — red team adjudicates the LEAD→LEAD-weak recommendation.

### For the report
- §16="i": add "position-conditioned alternative NOT SUPPORTED (R8: T1 p=0.94
  wrong-direction, T2 vacuous); B1 redirect exhausted; stays unconditioned LEAD."
- §Mehemet-Ali: add "R8: 62-tension adverse (name needs 62='a' vs 62='on' STRONG
  LEAD); 'mêleront' is a 62-compatible common-word rival; recommend LEAD-weak,
  promotion blocked on 62. RdDM 293× VERIFIED (1841 full run, exact clean-form
  count; F59 flag lifted)."
