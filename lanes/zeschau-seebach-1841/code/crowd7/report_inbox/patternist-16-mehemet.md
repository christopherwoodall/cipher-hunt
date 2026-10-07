# Patternist report: 16="i" battery + "Mehemet-Ali" @8 battery
Round 7, work orders 4–5 · 2026-10-07 · code: `code/crowd7/patternist/`
Results: `battery16_results.json`, `battery_mehemet_results.json`
Red-team rulings applied: `code/crowd7/redteam/RULINGS.md`; corrected positions
from `verify_f26_17.py` (61/61 PASS) used throughout. Canonical repaired 1,847-pair
parse. Bars were pre-registered in the script docstrings BEFORE results were computed;
post-hoc audits are labeled as such (not silent bar changes).

## Verdicts
- **16="i": HOLD (LEAD).** Not promoted. 1 solid-ish leg (B3) + 1 thin leg (B2) + 1 clean fail (B1).
- **"Mehemet-Ali" @8: HOLD (LEAD).** T7 LEAD stands, unweakened. M1 VOID, M2 PASS, M3 weak-pass.

---

## Battery 1: 16="i" (second /i/ cell; 34=i is GT)

Lead: "parmi" @1196–1198 [96,82,16] = par|m|i (F48, red-team UPHELD).
Datum: 82→16 ×11 @[381,433,536,1194,1197,1369,1386,1436,1479,1651,1831] (n16=28, n34=11).

**B1 DISTRIBUTIONAL — FAIL (clean null).** Permutation test (20k reps) on contact
profiles, 16 vs 34: followers cosine 0.21, p=0.8374 (n 27/11); predecessors cosine
0.53, p=0.9291 (n 28/11). No homophone-profile similarity — the F49
contact-coherent-dealing prediction for two /i/ cells does NOT hold unconditioned.
Per the pre-registered plan this redirects (not kills) to the position-conditioned
alternative: 16 = word-final /i/ (11/28 predecessors are 82=m; followers diverse and
word-initial-ish) vs 34 = word-internal /i/ ("pre|m|i|er|e"). That conditioning is
UNTESTED — no F33-grade rule exists for it. I do not promote on an untested rescue.

**B2 BY-EAR TILINGS — mechanical PASS, audited THIN.** Eleven-window rival vote
(len-4 by-ear tilings, 16 free, GT+PROV+LE77+islets hard): 'i' in vote set at 8/11
windows, plurality (i:8, e:7, o:6, a:6). Post-hoc informativeness audit: 3 windows
(@536,@1369,@1651) have all-free neighbors — everything fits, zero discrimination;
2 (@1194,@1197) are arity-silent (no len-4 tiling spans the anchored "parmi" frames);
@1386 excludes 'i' both shapes — DISCOUNTED as lexicon-coverage artifact ('miser'
absent from the 11,870-word lexicon), not adverse. Informative subset (6 windows):
'i' UNIQUE at @381 and @1831 — both vote the mise/misère family
([ad|m|i|se]: admise/remise/chemise; [m|i|se|..]: misères/misère/mises; @1831's
59→'se' is islet-licensed). Informative tally: i:5, e:4, o:3, a:3. Real but thin —
2 clean windows, n_eff=2.

**B3 ANCHOR-ADJACENCY — PASS (weak, mostly no-contradiction).**
(a) H-split consistency (N39): 46→16 = 0/28 ✓ — the cipher never writes 46=que
before /i/ unsplit (46→34=0 known); holds for 16. Necessary, not sufficient.
(b) 4 distinct anchor frames, zero adverse vs /i/: 16→96=par @1195 ('mi|par' word
boundary, consistent); 16→77=le @876 (neutral); 16→29=er @1142 (neutral);
16→64=qui @1198 — "parmi|qui": mild adverse to the PARMI word reading (not to
16='i'; "parmi qui" is ungrammatical standalone — flagged for the closer lane).

**Honest boundary (work order):** single-letter universe only. Multi-letter cells
(ie/is/it/…) untested — a PASS here could only ever yield provisional, and "i" vs
"y" are by-ear indistinguishable.

**Verdict reasoning:** B2 meets its bar mechanically but only 2/11 windows
discriminate cleanly; B1 fails clean; B3 is weak. Two thin passes ≠ promotion.
16="i" stays LEAD, strengthened (two new banked legs: @381/@1831 'i'-unique votes;
H-split consistency). Next: test the position-conditioned 16/34 allophone rule
under F33 (n_eff≥2, falsifiable), or find a third clean 'i' window.

---

## Battery 2: "Mehemet-Ali" @8 (T7 LEAD, null 0.28%)

Window: P[8:13]=[78,18,93,62,98]; reading me|he|met|a|li on the 78={me,ver} islet.
Preceded by P[0:8]=[09,00,97,51,47,41,06,77] (47=ce LEAD @4, 77=le prov-cond @7);
followed by P[13:19]=[76,45,91,53,17,64].

**M0 REPRODUCE — confirmed.** 10 bearing windows [8,443,476,573,879,982,1105,1164,
1670,1758]; null @8 = 33/11,870 = 0.28% — matches the T7 engine exactly.

**M1 STREAM-WIDE EXCESS — VOID (design flaw found and documented).** The bearing
criterion (manual me|he|met|a|li fits) and the null criterion (by-ear lexicon fitter
exists) differ — and decisively: the manual tiling fits EVERY 78-window whose
positions 1–4 carry no conflicting hard/islet anchor (verified: all 20 non-bearing
windows fail on anchor conflicts — 40=e vs he ×3, 46=que vs li/a ×4, 94=ne vs met/he
×4, etc.; 30 78-windows total). The count "10 bearings" is structurally determined
by anchor placement, not by the name being real. M1 contributes nothing either way.
(The T7 per-window null 0.28% itself is unaffected — it is anchor-preserving per N34.)

**M2 SPELLING — PASS.** "Méhémet-Ali" (hyphenated, accented) and "Mehemet-Ali"
(unaccented) are both attested in French sources: Wikisource "Méhémet-Ali durant
ses dernières années" uses both forms; Driault's 1839–1841 crisis correspondence
(apud journals.openedition.org/cdlm/16391) quotes "Méhémet-Ali". Accent-stripping is
the lane's disclosed convention, so the cipher form matches the contemporary
spelling. Topical Jan 1841: London Convention 15 Jul 1840; hereditary-pashalik
settlement running into early 1841. — **The "293× in Revue des Deux Mondes" figure
attributed to the period fleet is UNVERIFIED**: no RdDM corpus exists on the VM;
Tocqueville 1835/1840 and Les Mis T1 attest ZERO occurrences (expected — neither
discusses Egypt). Do not cite 293× until reproduced.

**M3 ALTERNATIVE READINGS @8 — WEAK PASS (non-exclusion, not discrimination).**
The 33 anchor-preserving fitters are ALL common me-initial words (mesure, mettre,
membres, mérite, mexique, mémoire, …) — zero name-like. The name is not
discriminated from common words by cipher data; distinguished only by near-opening
position and the manual tiling. No common-word fitter uses strictly cleaner
(all-20-string-inventory) cells, so the name is not at a cell-purity disadvantage.
Rival spellings: "Mohamed" (mo|ha|med|a|li) DEAD — 78='mo' unlicensed by the islet
(clean falsification leg); "Mehemed" (me|he|med|a|li) FITS (t/d indifferent by ear);
by-ear-pure me|e|met|a|li FITS — **the silent-h adverse is discharged** (the reading
never needed the etymological 'h'); the T7 drag's second manual tiling
me|h|me|t|a|li is arity-DEAD (6 cells vs 5 groups — traceability nit: it could never
fit; the anchored recount rested on one tiling, not two).

**M4 CORROBORATION — reported, not scored.** The other 9 bearing windows are
anchor-conflict-free trivial fits of the manual tiling (per the M1 finding), each
also admitting common-word readings. P[13:19]=[76,45,91,53,17,64]: a "pacha"
follow-up is anchor-free → VACUOUS by method (same as Ibrahim+"pacha", N42).

**Verdict reasoning:** M1 void; M2 solid pass; M3 weak pass (possible, not
preferred — 33 common rivals at the same null). One solid new leg does not clear
the ≥2 promotion bar. T7 LEAD stands, unweakened: nothing adverse (Mohamed
excluded, silent-h adverse discharged, no cleaner rival, spelling verified).
Dependency recorded: 78="me" islet is LEAD — if the islet falls, this falls.
What would promote: a second name-bearing window with independent support, or a
discriminator at @8 the common words fail (e.g., the P[0:8] opening formula
resolving to an address/subject frame).

---

## Cross-cutting notes for other lanes / red team
1. The T7 anchored recount's "10 bearing windows" for ANY manual name-tiling is a
   structural constant (anchor-conflict-free 78-windows), not evidence of the name's
   presence. Any future name drag must score per-window nulls, not bearing counts.
2. The T7 drag's k=6 manual variant (me|h|me|t|a|li) was arity-dead — recounts
   should assert len(cells)==len(groups) for manual tilings.
3. "parmi|qui" @1198–1199: mild adverse to the F48 "parmi" word (not to 16='i').
4. Lexicon coverage: 'miser' absent from the 11,870-word lexicon — by-ear
   exclusions at single windows are unreliable; only positive votes bank.
5. Do not cite "Méhémet-Ali 293× RdDM" — unverified.
