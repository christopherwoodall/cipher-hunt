# PRE-REGISTRATION — 4-gram frame test + 06-falsifier-watch round 10
## work order 6 · 2026-10-07 20:38 UTC (America/Chicago 15:38 CDT) · written BEFORE any round-10 computation

### A. The post-hoc datum (banked from round 9, not re-derived here)
On the repaired 1,847-pair stream, n06=44. Exactly **2** 06-windows have
successor 06: 06@580 (suc @581=06) and 06@1184 (suc @1185=06). **Both are
islet windows** (pre=82). Naive post-hoc p = C(4,2)/C(44,2) = 6/946 =
**0.0063**. Both windows sit in the byte sequence 94-82-06-06 starting at
@578 and @1182 (06-positions of the frame's third group: @580, @1184).

Candidate refinement H4g: "the true -ment frame is 94-82-06-06; 06 reads
'ent' iff (pre=82 AND suc=06)". Predicted window list W06-4g = [@580,
@1184] (n=2). n_eff: the two 4-grams differ at +2 (50 vs 59) ⇒ n_eff=2
provisional, extended-context check required before any confirm claim.

H4g COMPETES with the banked islet (06="ent" iff pre=82, W06 =
[580,738,1184,1355], n_eff=3): H4g would demote @738 (18-82-06-0) and @1355
(94-82-06-52) out of the islet, breaking the n_eff=3 repeat leg. H4g is
therefore held to a bar STRICTER than naive — it must displace, not just
decorate, the banked islet.

### B. HARKing analysis (pre-registered method; numbers computed after)
The 0.0063 is post-hoc: the successor profile was scanned and suc=06 was
fixated because it stood out. The honest test is the family-wise corrected
p over the full set of (offset, value) cells that could have produced an
equivalent "wow" — defined NOW, before computing:

- FAMILY F_suc: all successor values of 06-windows with count ≥ 2
  (from the round-9 census: {6,21,52,59,60,65} at k=2; {67} at k=3;
  {0,11,29} at k=4; {77} at k=6). For a count-k value, single-test
  p_k = C(4,k)/C(44,k) (P(all k land inside the 4 islet windows under
  independence). Family-wise p_fw = 1 − Π_v (1 − p_{k(v)}).
- FAMILY F_pre2: all prepre (offset −2) values of 06-windows with
  count ≥ 2 — the frame's OTHER observed dimension (3/4 islet windows
  have prepre=94) could equally have been fixated. Same p_k form.
- COMBINED family p_fw over F_suc ∪ F_pre2 (Bonferroni-style union over
  the two families: p_comb = 1 − (1−p_fw_suc)(1−p_fw_pre2)).

**Selection bar (pre-registered):** H4g's selection leg passes ONLY IF
p_comb < 0.01. If p_comb > 0.05 ⇒ REFUTED as post-hoc coincidence (banked
islet stands unchanged). If 0.01 ≤ p_comb ≤ 0.05 ⇒ NULL (inconclusive;
bank H4g as untestable-at-n=2, islet unchanged).

Note: the correction deliberately does NOT include offsets ±3,±4 or
suc-suc — those were not part of the observed frame. Widening the family
further would only strengthen a refutation; the fenced family above is
the conservative-minimum correction.

### C. Content leg (independent of the successor coincidence)
H4g must ALSO clear an independent content bar at BOTH 4-gram windows,
because a frame with no coherent French content is a coincidence with
makeup. Under banked values (GT 7 + provisional {87=ce, 64=qui, 59=est,
94=ne, 77=le} + F21 06-verb-stem as the general reading):

- The 94-82-06 head must admit "ne-m-ent" with no contact violation at
  @578–580 and @1182–1184 (pre-registered readings of prepre/pre are
  94=ne / 82=m; the judgment is by-ear, recorded verbatim for red-team
  audit; the F34/F44 rule applies: unknown gloss ≠ support).
- The SECOND 06 (suc, pre=06 ≠ 82) does NOT read "ent" under the strict
  iff — it falls under F21's 06-verb-stem general reading. The content
  leg REQUIRES a banked-consistent reading for each suc-06:
  06@581 (pre=06, suc=50) and 06@1185 (pre=06, suc=59=est). If either
  suc-06 is unreadable under every live 06 reading (stem-class per F21,
  plus the 06/86 complementary-distribution note from N29), the frame
  has no coherent content ⇒ H4g REFUTED regardless of selection p.

Content-leg verdict recorded per window with the by-ear sentence. A
window that needs an unbanked value to parse = content-leg FAIL at that
window. One FAIL ⇒ H4g REFUTED (frame incoherent). Both pass ⇒ leg holds.

### D. @1351 non-interference condition
The @1351 resolver (work order 1, their lane) adjudicates @1351–1356,
which contains islet window @1355 (94-82-06-52) and the byte-identical
twin of @1184's 5-mer. H4g CANNOT confirm while a constituent window is
under fenced pressure: if the resolver removes @1184 or @1355 from the
06="ent" domain (e.g. rules @1351-1356 exclusively "gouvernement" with
77-78-94-82-06 as one fused word, or 77="le" exclusive), H4g's n drops
below 2 ⇒ H4g is MOOT (not confirmed, not refuted — vacated), and the
banked islet is re-opened by the resolver's ruling, not by this watch.
Resolver status at prereg time: NO RULING LANDED (code/crowd10/resolver1351/
empty as of prereg). This watch proceeds independently; coordination is
by report, not by waiting.

### E. Confirm / refute / null summary for H4g
- **CONFIRMED** iff: p_comb < 0.01 AND content leg passes at both windows
  AND @1351 ruling does not vacate a constituent window AND n_eff=2
  verified in ±6 extended context (no longer byte-identical repeat).
  Consequence if confirmed: registry refinement — islet conditioning
  narrows to (pre=82 ∧ suc=06); @738/@1355 re-classified as non-islet
  06s (their "ent" reading withdrawn); red-team ruling required before
  the registry changes (I do not own the registry).
- **REFUTED** iff: p_comb > 0.05, OR content leg fails at either window.
  Consequence: H4g discarded as post-hoc coincidence; banked islet
  (pre=82, n_eff=3) stands; the suc=06 datum banked as a curiosity.
- **NULL** iff: 0.01 ≤ p_comb ≤ 0.05 with content leg passing, or content
  leg passing but n_eff check shows the two 4-grams are one repeated
  block (n_eff=1). Banked as untestable-at-n=2.
- **MOOT** iff the @1351 ruling vacates a constituent window first.

### F. Round-10 falsifier-watch continuation (banked islet: 06="ent" iff pre=82)
The three banked falsifiers (FIRE-IN / FIRE-OUT / FIRE-PART, prereg round 9)
were all unfired in round 9. Round 10 re-verifies on the same repaired
stream (no new cipher data exists; the census is re-run to catch any
re-index drift, and the by-ear audits are re-applied):

1. **FIRE-PART:** re-run the independent 82→06 census; the predicted list
   in 06-positions is [580, 738, 1184, 1355]. Any 82→06 window NOT on the
   list ⇒ falsifier fires (partition defect).
2. **FIRE-IN:** re-audit the 4 islet windows' contacts under the round-9
   decision rule: predecessor-of-82 frame making "m" unreadable, or a GT
   successor forcing re-syllabification of "ent" into a live GT lexeme.
   (Standing: 06→29 "er" is NOT a contradiction; no manual-tiling bearing
   counts are scored.)
3. **FIRE-OUT:** re-sweep all 40 pre≠82 06-windows under the round-9
   decision rule: counts iff an era reader accepts
   [gloss(pre)]+"ent"+[gloss(suc)] as a French word tail, gloss from GT +
   provisional {87,64,59,94,77}; unknown gloss ⇒ NOT counted. New: also
   flag any pre≠82 06-window in a 94-82-06-like trigram frame (none
   expected — census showed trigrams only at islet positions).
4. **@1351 watch:** dump the @1351–1356 region's ±6 context for the
   resolver; record any window-status change affecting W06 ([580, 738,
   1184, 1355]) as a registry coordination note. I do NOT adjudicate
   @1351 — the resolver owns it.

Bars unchanged from round 9: single adverse = fenced (lane n≥3 rule);
≥2 independent adverses (n_eff≥2) on the same leg ⇒ recommend DEMOTION;
≥3 ⇒ recommend KILL. One clean falsifier kills the islet (n_eff=3
fragility is banked). Recommendation PACKAGE only — red team adjudicates.

### G. Blindness note (honest)
The round-9 census numbers (n06=44, the 4 islet windows, suc=06 at @580/
@1184, prepre=94 at 3/4 islet windows) were visible before this prereg.
The CORRECTION METHOD (§B) and the CONTENT LEG (§C) were defined before
any round-10 computation. The FAMILY definitions above (§B) fix the
forking paths in advance; no post-hoc family widening is permitted.
