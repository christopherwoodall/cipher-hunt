# watch06 round-10 report: 4-gram frame test + falsifier watch (work order 6)

## Context
Work order 6: test the post-hoc 94-82-06-06 4-gram frame hypothesis (round-9
datum: both suc=06 windows are islet windows, naive p=0.0063) and continue the
06 falsifier watch against the banked islet 06="ent" iff pre=82 (W06 =
[580,738,1184,1355] in 06-positions, n_eff=3). Prereg banked at
`code/crowd10/watch06/PREREG.md` (2026-10-07 20:38 UTC), BEFORE any round-10
computation. H4g as stated: "06 reads 'ent' iff (pre=82 AND suc=06)",
W06-4g=[@580,@1184] — a refinement that would DEMOTE @738/@1355 out of the
islet and break its n_eff=3 repeat leg, so it was held to a stricter-than-naive
bar. All numbers re-derived from the repaired 1,847-pair stream
(`code/crowd8/frenchman/util.py`); script + log:
`code/crowd10/watch06/fourgram_test.py` / `.log`.

## Decision
1. **4-gram verdict: NULL** (pre-registered bar: confirm<0.01 / null 0.01–0.05 /
   refute>0.05 on the HARKing-corrected p).
   - Naive post-hoc p=0.0063 does NOT survive the garden-of-forking-paths
     correction. Family-wise over all successor values with count≥2
     (F_suc: {6,21,52,59,60,65}@k=2, {67}@k=3, {0,11,29}@k=4, {77}@k=6):
     p_fw_suc=0.0379. Family-wise over all prepre values with count≥2
     (F_pre2: the frame's other observed dimension, 3/4 islet windows with
     prepre=94): p_fw_pre2=0.0033. Combined p_comb=**0.0410** → NULL band.
   - Content leg (§C) passes weakly at both windows: @578–581 =
     55 61 [94=ne 82=m 06 06] 50 10 and @1182–1185 =
     77=le 78 [94=ne 82=m 06 06] 59=est 42 — the 94-82-06 head admits the
     banked "-nement" tail with no contact violation; each suc-06
     (@581: pre=06,suc=50; @1185: pre=06,suc=59=est) admits the F21
     06-verb-stem general reading with no forced violation. Neither window
     needs an unbanked value to parse. (Weak pass: unknown neighbors
     cannot contradict by the F34/F44 rule — the leg is nearly toothless,
     which is WHY the selection bar carries the verdict.)
   - n_eff verified = 2: the two 4-grams differ at −2/−1 (55,61 vs 77,78)
     and +2 (50 vs 59); 94-82-06-06 occurs exactly 2× in the stream
     (@578, @1182) — a repeated 4-gram with divergent context both sides,
     not a shared formula.
   - @1351 condition: no ruling has landed (resolver1351/ empty) — no
     vacatur; H4g judged on its own numbers.
   - **Consequence: H4g banked as untestable-at-n=2. The banked islet
     (pre=82, n_eff=3) stands UNCHANGED.** The suc=06 datum is a curiosity,
     not a refinement.
2. **Falsifier watch round 10: all three banked falsifiers UNFIRED.**
   - FIRE-PART: independent 82→06 census = [580,738,1184,1355] = predicted
     list exactly. No partition defect.
   - FIRE-IN: all 4 islet windows re-audited under the round-9 contact rule
     (@580: 94-82-[06]-06; @738: 18-82-[06]-0; @1184: 94-82-[06]-06;
     @1355: 94-82-[06]-52). No predecessor-of-82 frame breaks "m"; no GT
     successor fuses "ent" into a live lexeme. Zero adverses.
   - FIRE-OUT: all 40 pre≠82 06-windows re-swept under the by-ear rule.
     Only ONE window has both pre and suc glossed (@319: 94=ne [06] 11=la
     → "neentla" — not a French word tail). 0 counted. 94-82-06 trigrams
     occur only at islet positions [580,1184,1355]. Does not fire.
   - **The 06-islet survives round 10 intact. n_eff=3 fragility still banked:
     one clean falsifier kills it.**
3. **Registry coordination: NO window-status changes.** Nothing to merge
   into the islet registry this round. Conditioner note: the F_pre2
   sub-finding (prepre=94 at 3/4 islet windows) is the already-banked
   morphologist trigram re-expressed — no new claim, not promoted.

## Why
The 0.0063 was computed AFTER seeing that suc=06's both occurrences land
in the islet — textbook HARKing. The correction enumerates every
(successor value, count≥2) cell that could have produced an equivalent
"wow" (11 cells; note suc=52@k=2 also had 1/2 in-islet, suc=0@k=4 had 1/4 —
the near-misses the naive p ignores) plus every (prepre value, count≥2)
cell for the frame's second dimension (7 cells). The corrected 0.041 sits
in the pre-registered NULL band: suggestive, not significant. Promoting a
refinement on 0.041 that would simultaneously amputate two of the islet's
four windows (incl. the repeat twin carrying n_eff=3) would be exactly the
post-hoc carving the prereg was written to prevent. The content leg cannot
rescue it — at n=2 with unknown neighbors on both sides, by-ear
grammaticality is nearly unfalsifiable, which the prereg acknowledged in
advance by making selection carry the verdict.

## Enlightenment
- The near-miss structure is the real story of this datum: suc=6 occurs
  ONLY at the two islet windows (2/2), but the profile also holds
  suc=52 at 1/2 in-islet (@1355 islet, one outside) and suc=0 at 1/4
  in-islet (@738 islet, three outside) — chance-consistent partial
  overlaps the naive p=0.0063 ignores. The family-wise correction
  properly prices these in, which is why 0.0063 → 0.041.
- For the @1351 resolver: region dump @1345–1362 =
  86 66 73 34=i 62 48 77=le 78 94=ne 82=m 6 52 37 64=qui 35 13 92 62
  (raw: 86,66,73,34,62,48,77,78,94,82,6,52,37,64,35,13,92,62). Islet
  window @1355 (94-82-06-52) sits inside your adjudication zone; if your
  ruling vacates it, the islet drops to n=3/n_eff=3 (repeat leg gone,
  fragility unchanged numerically). This watch takes no position on
  @1351–1356 — your lane owns it.
- Method note for future frame-hunts: pre-register the (offset, value)
  family BEFORE looking, and require the selection bar to clear 0.01
  family-wise — the naive single-cell p will always flatter a fixated
  frame.

## Open / deferred
- H4g: banked NULL, untestable-at-n=2. Re-open ONLY IF new independent
  data arrives (it can't from this ciphertext) or the @1351 ruling
  changes the constituent windows' status (then MOOT, re-assess).
- 06-islet falsifier watch: standing — re-run each round until a
  falsifier fires or the islet is otherwise resolved.
- Red team: no status-change recommendation this round (NULL is not a
  change); the H4g NULL and the unfired falsifiers are reported for the
  record, no ruling required — unless the red team wants to audit the
  F_pre2 family definition.
