# PRE-REGISTRATION — 62-RESOLVER round 9: N35 independent-cell on/il battery
Date: 2026-10-07. Work order: STATE.md WO3 (blocker for Mehemet-Ali and @1248).

## Claim under test
62 = "on" (fenced STRONG LEAD, +2 non-ear legs banked: L_A, L_B) vs 62 = "il"
(DISFAVORED-STRONG, conditional on M_hom). Target outcomes: (a) promote
62="on" to provisional (needs ≥2 NEW independent legs), (b) kill 62="il"
outright, or (c) honest hold with the discrimination gap named precisely.

## Settled / barred cells (NOT to be recycled — F26-15, N35)
- Ear legs (62→94=9/35 and the 26-window by-ear triangulation): barred by battery charter.
- L_A: (93|8)→62=4 @10/@944/@1323/@1685 (conditional on M_hom): settled.
- L_B: 46→62=0, LR=21.3: settled. One datum, two uses — not re-entered.
- 62→48=6: RESERVED for the round-9 48-successor battery (WO2) — not touched here.
- 62→59 was *contemplated* in crowd8/frenchman/PREREG.md §E as an unexecuted
  angle ("if the chain fails") — never computed, never a leg. Still a fresh cell.

## Data-blindness statement
Seen before writing this: n62=35, 46→62=0, (93|8)→62=4 (+positions),
62→48=6, 62→94=9, 59→46 ×2, 59→37 ×6, 94-93-59 @101–103 (M_hom leg 3).
NOT seen: 62→59, 59→62, 62→(93|8), 62-(93|8)-59, (93|8)→59 (beyond @101–103),
predecessors of the four L_A windows, PAIRS[100], 62→01, {59,01}→62.
No cell below has had its cipher count observed by the author.

## Battery cells (all on the repaired 1,847-pair stream; n62=35 asserted in code)
Era reference: Nesselrode v8 ONLY (standing rule), frenchman tok_elision
tokenizer verbatim. Exact two-sided binomial throughout (no χ² — N35).

- **C1 — "il est"/"on est" rate (62→59).** Cipher k1=#{i:P[i]=62,P[i+1]=59}, n1=35.
  Era p_on=C("on","est")/C("on"); p_il=C("il","est")/C("il").
  Rationale: impersonal "il est" is modal in formal prose; "on est" is rare.
  Fenced: conditional on 59="est" (provisional). The 01="est" (MEDIUM)
  split-cell caveat is fenced (see S1).
- **C2 — inversion "est-il" vs *"est-on" (59→62).** Cipher k2=#{i:P[i]=59,P[i+1]=62},
  n2=UNI[59]. Era q_il=C("est","il")/C("est"); q_on=C("est","on")/C("est").
  Rationale: "est-il" (question inversion) is common in diplo prose; "est-on" ≈ 0.
  Fenced: 59="est" provisional + hyphen-tokenization assumption
  ("est-il" → 59-62; same compositionality class as L_B).
- **C3 — predicative "l'est" trigram (62-(93|8)-59).** Cipher
  n3=#{i:P[i]=62,P[i+1]∈{93,8}}, k3=#{of those with P[i+2]=59}.
  Era r_il=C("il","l'","est")/C("il","l'"); r_on=C("on","l'","est")/C("on","l'").
  Rationale (the task's l'-ask): "il l'est" is grammatical/idiomatic;
  "on l'est" is ~ungrammatical in 1841 formal prose.
  Test: exact binomial k3|n3 (conditional on observed n3).
  Fenced: 59="est" provisional + M_hom {93,8}="l'" (LEAD).
- **C4 — object-"l'" rate (62→(93|8)).** Cipher k4=n3, n4=35.
  Era s_on=C("on","l'")/C("on"); s_il=C("il","l'")/C("il").
  Rationale: weak-prior control — both "on l'"/"il l'" are grammatical
  ("on l'a"/"il l'a"); expected NULL, included against cherry-picking.
  Independence note: C3 conditions on n3=k4; under each hypothesis the
  marginal test (C4: k4|35) and the conditional test (C3: k3|n3) are
  independent pieces (conditional factorization). Red team adjudicates.

Void condition: any cell whose era denominator < 10 is VOID (no test).

## Decision bars (per cell, pre-registered)
- Compatibility: two-sided exact binomial p ≥ 0.10 → compatible with H.
- Incompatibility: two-sided exact binomial p < 0.01 → incompatible with H.
- LEG FOR "on": compatible(H_on) AND incompatible(H_il). Symmetric for "il".
- NULL: any other combination (compatible/both, incompatible/both, neither
  threshold met). "Incompatible with both" is reported as frame-adverse, not a leg.
- KILL 62="il" outright: ≥2 cells each incompatible(H_il) at p < 0.005
  AND compatible(H_on) at p ≥ 0.10. (Deliberately high; "il" is already
  DISFAVORED-STRONG — a kill must be M_hom-independent and non-recycled.)
- PROMOTE 62="on" to provisional: ≥2 NEW independent legs FOR "on".
  Instrument caveat (for the red team): C1–C4 share one instrument family
  (era bigram/trigram rates, Nesselrode v8) and all lean on 59="est"
  (provisional; C3 also on M_hom LEAD). Whether distinct grammatical
  asymmetries count as independent legs is adjudicated, not assumed.
- Else HOLD: name the discrimination gap precisely.

## N35 accounting
- No recycled cells: none of C1–C4 re-uses ear legs, L_A, L_B, 62→94, 62→48.
- Overlap audit: window positions of C1/C2/C3 printed; any shared pair
  position across cells → the shared window is dropped from the later cell
  and the drop is reported.
- N22: no 29/82/34/40 cells involved. No manual-tiling counts scored (F34/F44
  by-ear N/A — no ear work in this battery).

## Descriptives (NO bars — context only, reported without verdict weight)
- **D1:** all (93|8)→59 "l'est" windows: count, positions, predecessors.
  Includes the @101–103 (94-93-59) window's PAIRS[100] predecessor as an n=1
  observation (fenced: M_hom leg window re-entered for context only).
- **D2:** predecessors of the four L_A (93|8)→62 windows @10/@944/@1323/@1685
  (fenced: shares windows with L_A; "que l'on" check only).
- **S1 (sensitivity):** C1/C2 analogues with {59,01} pooled ("est"-as-word,
  leaning on 01="est" MEDIUM too). Descriptive — corroborates or fences,
  never a leg by itself.
