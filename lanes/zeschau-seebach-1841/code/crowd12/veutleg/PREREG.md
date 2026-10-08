# PRE-REGISTRATION — VEUT-ARM SUBJECT BAR (second leg for lean-veut), round 12
**Executor:** VEUT-SECOND-LEG
**Timestamp: 2026-10-07 21:24 UTC** (written before any round-12 computation on
this question; only standing/recorded numbers consulted: window contents
@1450/@1623, n36=9, n66=19, 33 suc==46 positions — sample geometry only, not
hypothesis-relevant outcomes)

**Task:** STATE.md round-12 WO-2 — give lean-veut (@1450/@1623, F79 decider,
grade LEAN) its second independent leg via the PRE-SIDE of the decider
windows: 36 @1449 (predecessor of 67@1450) and 66 @1622 (predecessor of
67@1623). Question: does an era "veut" frame license a 36/66 predecessor?
Era: Nesselrode v8 (`code/side-period/corpus/nesselrode-v8.txt`), lane
tokenizer verbatim (same `tok()`/`split_nesselrode()` as
`code/crowd11/census33/census33.py`; NW=92,123).

## Standing premises (not re-derived)
- F79 (adjudicator GRANT; red-team adjudication of the package pending):
  33 = infinitive-class (C1: I1 x8, I4 x5, I2 x1; zero nominal). Decider:
  infinitive -> veut lives at @1450/@1623 ("veut [inf] que" era-compositional;
  "et [inf] que" frozen-idiom-only). Grade LEAN (one check; >=2-check rule).
- Fork SUPPORTED; 67="veut" provisional; **no veut-bar exists** (F82). This
  prereg DEFINES the veut-arm bar (subject-leg); it does not apply any status.
- Decider windows (byte-exact, repaired 1,847-pair parse):
  @1450: 59-36-**67**-33-46 ; @1623: 78-66-**67**-33-46. (33s at @1451/@1624,
  suc==46 "que" GT.)
- 66-class: F65 CONFIRMED broad {noun, infinitive, nous/vous-type pronoun}
  (context only, NOT a leg; re-censused here excluding @1622).
- 36: unclassified; no standing battery.
- Licensor case law: V-1519b/V-902a nominal/verb licensor sets; census33
  I1-I4 infinitive signatures; F22 stem+"er" infinitive spelling; F37
  77="le" provisional-conditioned; F82 caught-prereg precedent (08="l'"
  article/pronoun-ambiguous -- 08/77 are WEAK nominal licensors, marked).
- Standing veut-67 positions (for reference): {110,116,351,491,506,851,
  1045,1163,1423,1457,1842}.

## Linguistic premise (pre-registered; era-checked in E1)
- Under 67="veut" (3sg present of vouloir), the adjacent predecessor 36/66
  MUST be the subject: nominal and subject-position-capable. A verbal 36/66
  (*"INF veut", *"V-finite veut") or a non-subject particle kills the
  veut-arm at that window.
- Under 67="et", 36/66 is a conjunct; the et-arm's burden ("et [inf] que")
  is already settled by census33 (frozen-idiom-only) and is NOT re-litigated
  here. This leg tests whether the VEUT-arm survives its own subject
  requirement. It is one-sided by linguistic fact, but FALSIFIABLE: a
  verbal/non-nominal 36/66 KILLS lean-veut at that window.

## Cipher-side procedure (per P in {36, 66})
- POS(P) = {i : pairs[i]==P} minus the decider position (1449 for 36, 1622
  for 66). Anti-circularity: the decider windows' own cells are never scored.
- Licensor sets (pre-registered):
  - NOM_pre = {11 (GT "la", strong), 08 ("l'" lead, WEAK per F82), 77 ("le"
    prov-cond, WEAK), 96 ("par" prov), 87 ("ce" prov), 47 ("ce" lead)}
  - NOM_suc = {64} (suc=="qui" follows nominals; 64="qui" prov)
  - VRB_pre = {64} (pre=="qui" -> P is finite-verbal; "qui"+nominal
    ungrammatical)
  - VRB_suc = {29} (suc=="er" GT -> P is a verb stem, F22)
  - EXCLUDED as ambiguous (recorded as datums only, never scored):
    pre in {00, 06, 86, 67v, 46, 59} ("pour"/stem/"veut"/"que"/"est"-islet
    take nominal AND verbal complements; census33's "ambiguity is a datum"
    precedent). 46 excluded per its que-nominal-subject ambiguity.
- nom(P) = distinct licensors from NOM_pre u NOM_suc with >=1 firing at
  POS(P) (pre=pairs[i-1] / suc=pairs[i+1] as applicable).
- vrb(P) = distinct licensors from VRB_pre u VRB_suc with >=1 firing.
- CLASS(P): NOMINAL iff |nom|>=2 and |vrb|<=1; VERBAL iff |vrb|>=2 and
  |nom|<=1; else UNRESOLVED (|nom|>=2 and |vrb|>=2 ->
  UNRESOLVED-CONTRADICTORY, adverse banked).
- Binomial nulls reported per fired licensor (E = |POS(P)| * freq(L)/1847);
  the BAR is the >=2-distinct-leg rule, not the p-value.
- Full pre/suc tables for 36 and 66 published for transparency.

## Era-side procedure (Nesselrode v8, verbatim tokenizer)
- E1 (subject-premise license; NEW cells): all i with W[i]=="veut"
  (n_veut); predecessor pre=W[i-1]; report top-25 pre with counts.
  BAR: |{i : pre_i in SUBJPRO}| / n_veut >= 0.50, SUBJPRO =
  {il,elle,ils,elles,on,cela,qui,je,tu,nous,vous} (unambiguous subject
  pronouns). If < 0.50 -> subject-premise VOID -> no cipher SUPPORTS may
  count (leg fenced). Rationale: the WO's question "does an era 'veut'
  frame license a 36/66 predecessor" -- a nominal 36/66 is licensed iff
  "veut" is normally subject-preceded in era diplomatic French.
- E2 (frame license; STANDING, cited not re-counted): "veut [inf] que"
  compositional attestation = census33's "il veut prouver que" (v8). No
  recycled cells: my new era cells are the predecessors (E1), disjoint from
  census33's "veut * que" middles and E7's counts.
- OCR caveat (F77): v8's VOID-as-French tokens are archive.org word-splits
  ("ment"-type); "veut" and subject pronouns are high-frequency closed-class
  items, not word-split artifacts. E1 is a predecessor distribution, not a
  phrase rate bar.

## Per-window verdict (pre-registered)
- CLASS(P)=NOMINAL and E1 passes -> second-leg SUPPORTS at W.
- CLASS(P)=VERBAL -> second-leg KILLS lean-veut at W. Recommendation if so:
  lean-veut WITHDRAWN at W (window left contradictory/open; the et-arm is
  NOT resurrected -- its "et [inf] que" burden stands per census33).
- CLASS(P)=UNRESOLVED -> clean NULL at W (missing leg named).
- Sensitivity (pre-registered): if a VERBAL verdict rests SOLELY on
  64-contacts with zero suc29, downgrade KILL -> NULL with the
  qui-provisional caveat fenced (64="qui" is provisional, not GT).

## Joint recommendation (pre-registered)
- SUPPORTS at both windows -> second leg CONFIRMED.
- SUPPORTS at one, NULL at the other -> FENCED (partial).
- NULL at both -> NULL.
- KILL at either window -> joint NULL, with per-window kill recommendation.
- Grade implication (for RED TEAM, not applied here): CONFIRMED + F79
  granted = 2 independent checks -> recommend veut-CONDITIONAL at the
  supported windows (conditional on 33=infinitive-class and the
  subject-license; mirrors @630's et-CONDITIONAL). FENCED/NULL -> lean-veut
  stays LEAN. 67 stays provisional and the fork stays SUPPORTED regardless
  (per WO).

## Independence accounting (F26-15/N35 case law)
- Cipher cells: 36/66 positions excluding decider windows -- disjoint from
  census33's 33-position cells and from every 67-battery cell.
- Era cells: pre("veut") tokens -- disjoint from census33's middles, E7's
  "et/veut * que" counts.
- F65's 66-cells may overlap mine; F65 is context only, my census (excl.
  @1622) is the leg.
- No manual-tiling bearing counts (F59 ban). No re-litigation: census33's
  "et [inf] que" frozen-idiom datum and E7's failed L1/L2 are cited, never
  re-derived. 33's class is a standing premise (F79), not re-censused.

## Why not alternative (b) (documented negative, not scored)
- Byte-exact check (pre-registered): enumerate all 33-positions with
  suc==46. If the ONLY hits are @1451/@1624 (the decider pair), then no
  other "33 que" frame exists anywhere in the stream, and alternative (b)
  ("another infinitive-governed 33 frame ... that independently
  discriminates veut from et") has no available discriminator: the "que"
  is the discriminating element (census33), and only the decider windows
  carry it. The "veut 33-er" @1424 frame (67=veut-classified standing) is
  same-arm consistency, not discrimination; the "et 33-er" @273/@1477
  frames show et+infinitive is fine WITHOUT "que". Recorded as the reason
  for pursuing (a).

## Fenced follow-ups (not scored here)
- F1: person/number agreement narrowing for 66 (F65's nous/vous member vs
  noun; F82-noted "new battery"). If CLASS(66)=NOMINAL via article-free
  licensors only, the agreement question stays fenced; the leg licenses the
  subject SLOT, not person-agreement.
- F2: 33's specific value (STATE.md WO-1) -- untouched.
- F3: clean 3.96M diplomatic corpus cross-check of E1 -- available, not run
  (WO directs v8).

## What counts as done
PREREG.md (this file) + `veutleg.py` implementing it literally + 
`veutleg_results.json` (full tables, firings, nulls, E1 distribution,
verdicts) + report note at `code/crowd12/report_inbox/veutleg-second-leg.md`.
Byte-exact positions throughout. Red team adjudicates every status change;
this package is a recommendation.
