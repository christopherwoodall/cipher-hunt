# PRE-REGISTRATION — 33-CLASS CENSUS, round 11 (work order 3)
**Executor:** 33 CLASS CENSUSER
**Timestamp: 2026-10-07 20:59:25 UTC** (written before any round-11 census
computation; only standing/recorded numbers consulted)

**Task:** census group 33's contact profile across the full repaired 1,847-pair
stream; classify 33's predecessors and successors as infinitive-class vs
nominal-class signatures; apply the F74 decider to @1450/@1623 (67="veut" vs
67="et").

**Standing record (not re-derived):**
- Round-10 E7: @1450 win 59-36-67-33-46, @1623 win 78-66-67-33-46 (F0 PASS).
  L1: E_et=n("et * que")=16, E_veut=n("veut * que")=2 → FAIL (bar needs ≥20).
  L2: n(11→33)=0 → FAIL. Both stay open-residual. veut-gap-que middles (v8):
  {coûte:1, prouver:1} — "prouver" is an infinitive.
- Round-10 contact census: other 67-windows with suc==33: et 3
  (@272,@1148,@1476), veut 1 (@1423), open 2 (the pair themselves).
  Round-10 PREREG design-time: suc-contact excluded as confounded — NOT reused
  here as a leg (this census is 33-side, independent).
- Standing 67 classes: `code/crowd7/morphologist/battery67_final.json`
  (et 18 / veut 11 / open 9) + round-10 overlays (1248 NEITHER-fenced,
  199 NEITHER-fenced-conditional, 630 et-CONDITIONAL).
  veut-67 positions: {110,116,351,491,506,851,1045,1163,1423,1457,1842}.
- Board: GT 11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que.
  Provisional: 87=ce, 64=qui, 96=par, 59=est(-islet), 77="le"-conditioned.
  Leads: 00="pour" (strong), 47="ce", {93,8}="l'", 06=verb-stem-class,
  86=infinitive-complement-stem, 06="ent"-iff-82, 16="i".
- Mechanics only (script input, not findings): n33=25 on the repaired parse.

**Era:** Nesselrode v8, lane tokenizer verbatim (vendored round-9/10 copy;
NW=92,123). Rate bars use Nesselrode v8 only. Never score manual-tiling
bearing counts (F59). No re-litigation of settled kills
(N29 47="me"; N10 24="est"; N11 H5; N17 06=/mɑ̃/; N19 06="ent"-general;
F56 merger refutations; EV1–EV14 vetos; F73 "cela" REFUTED).

## Class-signature definitions (fixed now)

For each 33-occurrence at index i: pre=pairs[i-1], suc=pairs[i+1].
(No boundary positions; min 33-position is 24.)

**INFINITIVE-class signatures** (pre-verbal position, complement structure):
- **I1**: pre == 00. "pour" (STRONG LEAD) + infinitive = canonical infinitive
  governor. Lead-conditioned; carries the mark.
- **I2**: pre == 67 AND (i-1) ∈ standing veut-67 positions. "veut" takes
  infinitive complements.
- **I3**: pre ∈ {06, 86}. 06/86 = verb-stem class (F40 M1, provisional):
  stem + complement = verbal frame. Class-level mark.
- **I4**: suc == 29 ("er" GT). 33 as stem + written "-er" = infinitive
  spelling (F22; the lane's own 06→29 ×4 infinitive-frame template).
- **I5** (frame, conditional): suc == 46 (que GT) AND pre ∈ {00, 67-veut,
  06, 86} — infinitive licensing "que" (cf. "empêcher que", banked F67/F73).
  Fires only under the pre-condition; never standalone.

**NOMINAL-class signatures:**
- **N1**: pre == 11. 11="la" GT. GT-anchored.
- **N2**: pre == 77. 77="le" provisional-CONDITIONED (F37). Excluded at any
  33-window sitting in a gouv-fenced position (@1180/@1351-only per
  F70 — pre-checked before firing).
- **N3/N6** (one kind): pre == 87 ("ce" provisional) / pre == 47 ("ce" LEAD).
  Both are the "ce"-governor; count as ONE signature kind for the bar.
- **N4**: pre == 96. 96="par" provisional.
- **N5** (frame, conditional): suc == 46 (que GT) AND pre ∈
  {11,77,87,47,96} — nominal + relative-que.
- **Ambiguity rule (fixed):** suc == 46 fires I5 iff the pre-side is
  infinitive-governed (I1–I3 condition), fires N5 iff the pre-side is
  nominal (N1–N4/N6 condition); otherwise suc == 46 is UNCLASSIFIED
  (recorded, unscored — ambiguity is a datum, not a leg).

**VERBAL-FINITE bucket (third, anti-both):**
- **V1**: pre == 64. 64="qui" provisional; "qui" governs a finite verb
  phrase. Favors neither fork arm ("et"+finite clause is grammatical,
  "veut"+finite is not). Recorded; breaks ties toward et if it fires at a
  decider window, but it is not a nominal leg.
- pre == 59 ("est"-islet): recorded, unscored (copula frame, confounded).

## Census bars (fixed now)

- **C1 (infinitive-class):** 33 = infinitive-class iff ≥2 of {I1,I2,I3,I4}
  fire (two INDEPENDENT signature kinds) AND zero GT-anchored nominal hits
  (N1) AND zero unambiguous-N5 hits.
- **C2 (nominal-class):** 33 = nominal-class iff ≥2 independent kinds among
  {N1,N2,N3/N6,N4} fire, with ≥1 GT-anchored (N1) or ≥2 provisional/lead,
  AND zero hits among {I1,I2,I3,I4}.
- **C3:** else 33 = UNCLASSIFIED → the decider does not fire.

**Exclusions:** the two decider windows (@1451, @1624 — the 33s after
67@1450/67@1623) are EXCLUDED from the census (anti-circularity); counted
separately as a sensitivity check. **Independence accounting** (F26-15/N35
case law): no recycled cells; each signature event counted once; pre/suc
cells of one window are distinct cells. Per-window nulls where base rates
exist: E = n33 × nX/1847 (binomial), never tiling scores.

## Decider application (fixed now)

- **C1 passes → lean-veut at @1450/@1623** ("veut lives"): the census
  licenses the infinitive reading of 33; era class-matched frame is
  "veut [infinitive] que" (v8: "veut prouver que", n=1 of the 2
  veut-gap-que). 67="veut" survives as the favored arm at LEAN grade.
- **C2 passes → lean-et at @1450/@1623** ("et" favored): era class-matched
  frame "et [nominal] que" (v8 n=16; middles enumerated and hand-classed);
  "veut 33 que" with nominal 33 is ungrammatical.
- **C3 → no ruling**; @1450/@1623 stay open-residual; 33's class banked as
  the explicit missing leg.
- **Grade cap:** the decider is ONE new bar → LEAN only, never a
  classification (lane ≥2-independent-check rule). It does not re-litigate
  E7's failed L1/L2. @1248 counterdatum stays a scope amendment (F74),
  untouched.

## Frenchman register check (claims I will make, pre-checked)

1. "pour + infinitive" — standing French; no veto touches it.
2. "veut + infinitive + que" grammatical — era-attested ("veut prouver
   que", v8). Gate-4 concern is cela-class (VOID per F73), not infinitives.
3. "et + nominal + relative-que" — verified against v8 "et * que" middles
   (hand-classed, n=16).
4. "stem + er = infinitive spelling" — F22 lane standing.
5. Veto sweep: EV11 (cela-class VOID) and EV12 (finite-verb @1248) — my bars
   use neither cela-class nor @1248. F73 "cela" REFUTED — not used. The
   "qu'on"-merger/H-split dispute (N28/N39) does not touch any 33 window
   (46→33/33→62 counts reported as datums only).

## What counts as "done"

Census table (25 windows, pre/suc, signature firings, exclusions applied),
class verdict C1/C2/C3 with the two-bar audit, era middle-classification for
the class-matched frame, the @1450/@1623 ruling at its capped grade, and an
explicit missing-legs list. Red team adjudicates any status change — this
package is a recommendation, not a merge.
