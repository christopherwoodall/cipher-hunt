# CONDITIONER — pre-registration (written BEFORE any new computation, 2026-10-07)

Standing: red-team verify_f26_17.py (61/61 PASS) supersedes NOTES.md figures; all
positions below in 0-based repaired 1,847-pair starts unless noted. The conditioning
rule R is the Closer's own flagged resolution recorded at F46 (pre-round-7, not
fitted by me). The 00 rule is my own test candidate, pre-registered here.

## Work order 1 — the 84 conflict

Rule R: 84="en" iff pre(84)∈{46,94,82}; 84=masculine-noun iff pre(84)∈{77,11}.

Pre-registered bars (F33: verified, falsifiable, zero free cases):
- B1 COVERAGE: every one of the n84=25 occurrences has pre∈{46,94,82,77,11}.
  FAIL ⇒ conditioned polyvalence falsified ⇒ kill the polyvalence, compare sides.
- B2 "en"-CLASS COHERENCE: each pre∈{46,94,82} window reads grammatically with
  84="en" — 46-84="qu'en" (GT-anchored), 82-84="m'en" (GT-anchored), 94-84="n'en"
  (94="ne" prov-strong, elision-licensed). Any successor that breaks the read is
  an adverse datum; ≥1 unrepairable break ⇒ side fails.
- B3 NOUN-CLASS COHERENCE: each pre∈{77,11} window reads as article+noun;
  successors compatible with a masculine noun. ≥1 unrepairable break ⇒ side fails.
- B4 INDEPENDENCE (no double-count): the "en" legs (E1/E2/E5) and the noun legs
  must rest on DISJOINT occurrence sets. Overlap ⇒ demote the double-counted leg.
- B5 n_eff: byte-identical repeated windows count once for rate claims
  (64-77-84 ×3, n_eff=1, is already so-scoped).

Decision tree: all pass ⇒ confirm conditioned polyvalence (F33-grade); B1 fails ⇒
kill polyvalence, compare "en"-only vs noun-only on the full 25; B2 or B3 fails ⇒
demote failing side, promote survivor. No status change merges without red-team ruling.

NOTE on E4 (the "l'en" 141×/63× blocker): it rests on reading all 77→84 as "l'en"
under 77="le". Under rule R those windows are noun-class by construction, so B1
PASS dissolves E4 automatically — no separate re-derivation needed; the blocker
then applies to NO occurrence.

## Work order 2 — the 00 conflict

Candidate conditioned rule S: 00="le" iff pre(00)=96 ("par le" ×3); 00="pour"
elsewhere. (Motivation: 96-00="par pour" is ungrammatical under "pour" at all
three windows; 00="pour" survives everywhere else. Recorded here before testing.)

Pre-registered bars:
- C1 RATE-REPAIR: build an elision-split word model on the diplomatic corpus
  (identical tokenizer to closer87_00.py: lower, '→space elision split,
  [a-z\u00e0-\u00ff]+). Recompute r1=P(00)/P_dip("pour") and
  r3=P(46|00)/P_dip("que"|"pour"). REPAIRED iff both ≤2× (lane band; band is
  UNCALIBRATED per F20, so raw ratios are reported alongside).
  Primary: despatches subset (nesselrode-v8 1840–46, levant-correspondence-1841-p3).
  Secondary: full diplomatic French set. Method parity sanity check: re-tokenize
  Tocqueville t1+t2 and reproduce B1=6.22× / B3=3.85× first.
- C2 INCOMPATIBILITY: at 96→00 @47/@465/@960, check successors @48/@466/@961;
  "par pour X" must be ungrammatical at ALL three ⇒ tension confirmed. If any
  successor rescues "par pour", "le" loses its forced reading.
- C3 "le"-ISLET COHERENCE: zero free cases among pre=96 occurrences of 00 (all
  three are the 96→00 bigram), and «par le X» reads cleanly at each successor.
- C4 "pour"-BATTERY INTEGRITY: drop the 3 pre=96 windows from the battery and
  re-verify: 00→86 ×12 vs 00→06 ×0 (B2a), P(86|00) (B2b), 06→00 ×4 (B5),
  00→46 ×4, 00→11 ×4 — counts must survive with no leg lost.

Decision tree: C1 repaired + C2/C3/C4 hold ⇒ conditioned polyvalence
(00="le" iff pre=96; 00="pour" elsewhere) recommended to red team at
provisional-tier. C1 not repaired ⇒ blockers stand: "pour" stays STRONG LEAD,
"le" holds LEAD as a conditioned islet (independent n=3 legs, unchanged). No
kill of "pour": all rivals are already dead and no kill-grade adverse exists;
no kill of "le" while C2 holds (the windows force a non-"pour" value).
