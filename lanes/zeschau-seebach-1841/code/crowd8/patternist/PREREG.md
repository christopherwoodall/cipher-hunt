# PREREG — Seebach round 8, patternist work orders 11–12
Date: 2026-10-07. Executor: patternist. Status: PRE-REGISTERED (no data touched).

Canonical parse: repaired 1,847-pair (`code/side-keyhunt/repaired_offsets.json`);
positions per `code/crowd4/REINDEX.md`. n16=28, n34=11 (crowd7 battery16 asserts).

## Part (a): 16="i" position-conditioned alternative (WO-11)

Redirect from B1's clean fail (F59): 16 = word-final /i/ vs 34 = word-internal /i/.
Anchoring: 34=i is GT-internal ("pre|m|i|er|e" @754/@1034); 16 is final in the
"parmi" lead ([96,82,16]@1196:1198, 16@1198 followed by 64=qui).

### T1 — follower word-initial-anchor enrichment (PRIMARY, distributional)
- WI set (primary): {'11','70','46','87','64','94','96','62'}.
  Rationale: GT pencil groups obligatorily word-initial in French (11=la article,
  70=pre prefix, 46=que conjunction) + provisional-or-better function words
  obligatorily word-initial (87=ce, 64=qui, 96=par, 94=ne, 62=on STRONG LEAD).
  Excluded: 59=est (verb, medial), 78 (LEAD islet), 77 (provisional-conditioned →
  sensitivity only), 82/34 (letter cells), 29/40 (word-final cells).
- Statistic: 2×2 table [WI_16, nonWI_16; WI_34, nonWI_34] over ALL followers
  (n16=28, n34=11); one-sided Fisher exact, H1: P(fol∈WI|16) > P(fol∈WI|34).
- Bar: p<0.05 → SUPPORT (one leg). Report raw table + odds ratio.
- Sensitivities (reported, not scored): S1 GT-only WI={'11','70','46'};
  S2 WI+{'77'}; S3 drop the parmi-window follower (16@1198→64).
- Overlap note: 2 of 28 16-followers (→64 @1198, →96 @1195) were cited in B3;
  B3 never compared 16 vs 34 — different statistic, mostly new data.

### T2 — "premier"/"première" minimal-pair frame (by-ear frame, independent of T1)
- Frames (4-grams at 70): A=70-82-34-29 (masc "premier": split predicts 34),
  B=70-82-16-29 (split predicts 0 — 16 never medial), C5=70-82-16-29-40
  (split requires 0; GT has 2× 70-82-34-29-40). For A, require P[i+4]≠40
  (else it is the GT feminine frame, not masculine).
- Bars: SUPPORT iff count(A)≥1 AND count(B)=0 AND count(C5)=0.
  ADVERSE iff count(B)≥1 OR count(C5)≥1.
  Else UNINFORMATIVE (not scored). n_eff small — one leg at most.

### Verdict rule (a)
- T1 SUPPORT and T2 not adverse → position-conditioned alternative SUPPORTED
  (16="i" stays LEAD, gains a conditioned leg; needs F33-grade rule next).
- T1 p≥0.05 and T2 uninformative → alternative NOT SUPPORTED (B1 redirect fails;
  16="i" stays unconditioned LEAD).
- T2 adverse → alternative KILLED (regardless of T1).

## Part (b): "Mehemet-Ali" @8 discrimination + RdDM 293× (WO-12)

### D1 — the 62-tension (logical incompatibility)
- Fact to verify: the claim AS STATED (me|he|met|a|li on [78,18,93,62,98])
  assigns 62='a'; lane STRONG LEAD 62="on" (/ɔ̃/) assigns 62='on'. Incompatible
  as single values (62 not in the F33 polyvalence set).
- Robustness: enumerate by-ear top-8 tilings of "mehemetali"/"mehemedali"
  (accent-stripped, lane convention), filter len(cells)==5 and cells[0]=='me';
  check whether ALL put an /a/-containing cell on 62 (position 3).
- Bar: claim's own tiling puts /a/ on 62 (verify) AND no top-8 alternative
  tiling avoids /a/ on 62 → 62-TENSION CONFIRMED (adverse-moderate to the name:
  it survives only if 62="on" falls or 62 is polyvalent — a new posit).
  If an alternative tiling avoids /a/ on 62 → tension DISSOLVED for that tiling.

### D2 — common-word contrast at @8 through the 62 lens
- Recompute the 33 anchor-preserving fitters at P[8:13] (by-ear top-8 tilings,
  HARD=GT+PROV+LE77; assert len(cells)==len(groups)); tabulate cells[3]
  (the 62-cell). Note name-like fitters ('mehemetali', 'mexique').
- Bar: ≥1 common-word fitter with cells[3]=='on' (compatible with the STRONG
  LEAD) while the name is incompatible → DISCRIMINATOR CONFIRMED
  (adverse-moderate: a rival preserves the lane's stronger claim; the name
  destroys it). Report the full cells[3] distribution.

### D3 — RdDM "293×" verification
- Check VM for any Revue des Deux Mondes corpus bytes; one documented
  retrieval probe (Gallica SRU full-text) for plausibility context.
- Bar: VERIFIED only by corpus bytes on the VM reproducing ≈293 under a
  documented count methodology, or a documented retrieval reproducing it.
  Otherwise → RETRACTED explicitly in the report note. Not cited either way
  until verified.

### Verdict rule (b)
- D1 confirmed + D2 confirmed → recommend DEMOTE LEAD→LEAD-weak (red team
  adjudicates): the name is possible (M2 spelling/topicality stands) but now
  disfavored vs common-word rivals at @8 and blocked on 62="on".
- D1 confirmed alone → HOLD (LEAD), weakened; promotion blocked on 62.
- Neither → HOLD (LEAD) unchanged.
- D3: figure VERIFIED or RETRACTED per bar above.

## Standing rules honored
- F59/WO-14: no bearing counts scored on manual tilings — per-window nulls
  only (D2 recomputes the per-window null sample); assert len(cells)==len(groups).
- ≥2 independent checks per promotion (none proposed here).
- Red team adjudicates all status changes; this note is a recommendation.
