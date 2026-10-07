## watch06: 06-falsifier-watch round 11 (work order 6)

- Context: standing falsifier watch against ISLET 3 — 06="ent" iff pre=82
  (W06 = [580,738,1184,1355] in 06-positions, n=4, n_eff=3). Round 11 runs
  after two material changes: F70 resolved @1351–1356 to R-c «le [78] ne
  ment pas» (islet @1355 positional membership intact, now the islet's
  glossed window), and F71/ISLET-10 conditioned 59 ("est" only where
  pre∈{64,94,93}) — which tightens this round's FIRE-OUT gloss rule. H4g
  stays REFUTED per F72 (p_comb=0.0508); not re-litigated. PREREG banked
  BEFORE any computation at `code/crowd11/watch06/PREREG.md`; script+log at
  `code/crowd11/watch06/watch11.py` / `watch11.log`. Stream re-verified from
  `code/crowd8/frenchman/util.py` (repaired offsets).

- Decision: **all three banked falsifiers UNFIRED (round 11).**
  1. FIRE-PART: 82→06 census = [580,738,1184,1355] = predicted list,
     exactly. No partition defect. (Census-fidelity gate: N=1847, n06=44,
     n82=39 — all confirmed, no parse drift.)
  2. FIRE-IN: zero forced adverses at the 4 islet windows under the
     round-9 contact rule. @1355 now carries the banked F70 gloss
     («le [78] ne ment pas» — byte-exact @1349–1362 re-verified). The F66
     @1184 fenced adverse ("ne mentent/entendent est") was re-audited and
     stays FENCED, not promoted: both candidate parses require unbanked
     readings at 06@1185 (the "mentent" tile needs 06@1185="ent", which the
     iff itself excludes; "entendent est" needs 59=est-as-word at pre=06,
     which ISLET-10 holds only as a fenced LEAD sub-tier). No GT successor
     fuses "ent" into a live lexeme at any islet window.
  3. FIRE-OUT: 0 counted windows across all 40 pre≠82 06s under the
     ISLET-10-tightened by-ear rule. Only one window has both neighbors
     glossed (@319: "neentla" — not a French word tail). The tightening
     removed no qualifying window (none had a 59-glossed neighbor under the
     old unconditional rule). 94-82-06 trigrams occur only at islet
     positions [580,1184,1355] — no new trigram frames.
  Census update: none — every census number is identical to rounds 9–10.

- Why: the census enumerates independently from the repaired stream and
  would flag any new 82→06 window (predicted or not); the partition list
  is complete. The FIRE-IN bar requires a FORCED non-"ent" parse (impossible
  junction or GT-lexeme fusion), not gloss strain — @1184's contact
  (prepre=94=ne, pre=82=m GT, suc=06 non-GT) admits "ne-m-ent" with no
  violation. FIRE-OUT's by-ear rule is deliberately conservative
  (unknown gloss ≠ support); with only 1/40 windows fully glossed the
  sweep is nearly toothless at current anchor density, which is reported
  as a coverage limitation, not a pass-by-design. Coincidence probe
  (cipher-internal exact binomial): P(X≥4)=0.0138, enrichment 4.31× —
  same as round 9, in the honest middle band of the prereg read
  (neither chance-level adverse nor p<0.01 "selection real").

- Enlightenment: the register check bit twice and both times honestly.
  (1) Nesselrode v8's 54 "ment" tokens are archive.org OCR word-splits
  ("infini ment"), not the verb — token-level checks on v8 for "ne ment"/
  "ment pas" are void; the v8 zeros measure OCR, not French. (2) On the
  clean 3.96M-token diplomatic corpus, «ne ment pas» = 1, «ment pas» = 5 —
  the F70 @1355 gloss is era-attested in diplomatic register, rare-but-real,
  exactly what the genre reclassification (F31) predicts. The takeaway for
  future register checks: state the base rate first (mentir is lexically
  rare in memoirs), and never run phrase-attestation on OCR-split corpora
  without the caveat. Also: the F66 @1184 "adverse" dissolves on inspection
  because it argues against the islet using a reading the islet excludes —
  a reminder that by-ear adverses must be checked against the conditioning
  they attack.

- For the report: 06-islet watch section. Numbers: 82→06 census
  [580,738,1184,1355] (no change); 94-82-06 trigrams [580,1184,1355]
  (islet-only); FIRE-IN/FIRE-OUT/FIRE-PART all unfired; coincidence
  P(X≥4)=0.0138, 4.31×; «ne ment pas» 1/3.96M diplomatic tokens
  (attested); islet status unchanged (LEAD conditioned, n=4, n_eff=3).

- Caveats: (1) The FIRE-OUT sweep covers only 1/40 windows at full gloss —
  the islet's ← leg is defended by anchor sparsity as much as by evidence.
  (2) @738 (lone 82-06, pre=18 unglossed) and @580 still carry no banked
  French gloss; the trigram "ent" reading at those two rests on the
  -ment shape + contact absence, not on an identified stem. (3) The F66
  @1184 by-ear stays fenced — it re-opens if 06@1185's verb-stem or the
  @1186 [06-59] verb-unit (ISLET-10 sub-tier) gets a banked reading.
  (4) n_eff=3 fragility still banked: one clean falsifier kills the islet.
  (5) No manual-tiling bearing counts scored anywhere (lane rule); all
  rate bars Nesselrode v8 / diplomatic corpus as noted.
