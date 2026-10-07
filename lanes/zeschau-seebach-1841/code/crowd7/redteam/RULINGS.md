# Round-7 Red-Team Rulings — F26-17 review + T4 either/or adjudication

Red team: round-7 red-team agent · 2026-10-07 · kill authority over any round-7 promotion.
Scope: every "curator: ..." mark in NOTES.md N39–N44 and F45–F51 (coordinator-applied
after the round-6 red-team session ended — F26-17), plus work-order-3 T4 adjudication.

Method: independent re-derivation on the repaired 1,847-pair stream
(`code/side-keyhunt/repaired_offsets.json`, positions per `code/crowd4/REINDEX.md`).
Baseline extended, not rebuilt: `code/crowd6/redteam/verify_baseline.py` 49/49 PASS
(untouched) + new `code/crowd7/redteam/verify_f26_17.py` **61/61 PASS**.
Position convention below: bigram/trigram START indices, 0-based repaired parse.
Pre-registered bars: exact tests, no double-counting, no ear-premise leakage (N35),
F33 conditioning rules must be verified and falsifiable (zero free cases).

## Verdicts

### N39 — curator: NO PROMOTION, honest null → **UPHELD**
Re-derived: n62=35, 62→94=9/35=0.2571, 46→62=0/29, 46→34=0, 46→29 ×2 @95/@217,
21→62 ×5, 77→62 ×1 (bigram starts @507; memo cited the successor index @508 —
convention nit, count correct). E=29×0.2475=7.1775 ✓; p=(0.7525)^29=2.62e-4,
worker's "2.6e-4" ✓. Joint logLs: on −26.54 (−21.07−5.48+0) vs il −26.82
(−20.43−6.39+0), Δ=+0.27 tie ✓; qui −32.77 ✓.
The VOIDs are licensed, not asserted: N35's "il"-differential rested on the
unlicensed "qu'il"→46-62 spelling premise (46→34=0 — the cipher never writes 46
before /i/); N28's merger premise contradicts the cipher's demonstrated H-split
habit (46→29 ×2 @95/@217: /kɛʁ/ → two groups). Correct outcome: zero non-ear
legs delivered (Leg 1 voids, Leg 2 ties, Leg 3 null); the single weak
positive-+0.91 nats (n=1) cannot carry a promotion; the adverse datum is single
with 4 explicit caveats → correctly not kill-grade. 62="on" stays fenced
STRONG LEAD on ear legs 1&3 only.

### N40 — curator: CONTROL-FAIL → **UPHELD**
C1 PASS verified in `step5_control.json`: truth −1.4274 > annealed best −2.4116,
gap 0.9842 ✓. C2 FAIL: primary top-1 0.0 (0/20) ✓. C3 FAIL: islets 0/3 ✓.
C4 FAIL: pins 7/7, margin 0.921 < 1.0 ✓. Gate holds — NO R5005. The
"objective correct, search too weak" diagnosis is worker-faithful. No bar
misapplied.

### N41 — segmenter package → **UPHELD**
k=16 replicates: e1_z=5.54, agree_vs_ref=91 ✓. 69/96 vs "61/96 change"
reconciled: naive_change=61, bestperm_agree=69 (perm BACR) ✓. HMM vs 96-group
bigram held-out: −4.2638 vs −4.2356 (Δ0.028, 293 vs 9120 params = 31× fewer) ✓;
transition matrix cyclic (S1→S0 1.0, S0→S2 0.705, S2→S1 0.672) ✓. Column
geometry: momentum 0.6327 (n=765) vs 0.4856 (n=383), z=+4.77, SUPPORT ✓;
memory-2 null (FALSIFIED) ✓. The "fragile labeling / real phenomenon" verdict
and the N43 three-way scope cross-reference are correct.

### N42 — period-drag package → **UPHELD** (T4 either/or ruled separately below)
T1/T2/T6/T8 honest NULLs ✓. T3 NULL + kill ledger verified in results.json ✓.
Frame corrections verified: R1a "followed by 77" absent from every canonical
parse; R2 0× in the repaired stream ✓. T5: 96→00 ×3 @47/465/960 ✓, null
64/11,870=0.5% @465 ✓, 96→77=0/21 ✓, phrase placements mutually inconsistent ✓;
00="le" LEAD correctly provisional-dependent and tensioned vs F40/F47. T7:
Mehemet-Ali null 33/11,870=0.28% ✓, anchor-bearing recount honest ✓. T4 shape
HIT: exact by-ear fits at both windows (independent), 82=m GT-anchored; C2
family 1/11,870 ("légalement"), null 289/11,870=2.43%/window ✓; C3 ne×10/ver×0/
er×3 @T4, ne×3/ver×0/er×17 @578 ✓. "NO status change to either" correctly held —
the 94-reading was properly referred, never adopted.

### N43 — curator: CONTROL-FAIL, R5005 untouched → **UPHELD**
Synthetics χ² 36.6/0.4/787.3/375.5/6.2/2.9, in-band 0/6 ✓ (memo3 line 12);
design doc "Jaccard clustering recovers planted phases at purity ~0.5, making
its χ² a coin flip" ✓ (CONTROL-DESIGN.md L113-114). Uniform-random aliasing
χ²=3.9 ✓ (memo3 line 36). Three-way scope — (a) existence confirmed by
label-free lag-3 (gate e1 z=5.8089, consistent), (b) magnitude noisy, (c) mapping
~0.5 purity — correctly stated; no round-6 argument leans on exact χ² values.

### N44 — curator: "0 promotions, 0 kills, 0 demotions" → **OVERTURNED** (corrected net)
- "0 kills": UPHELD (no claim killed in round 6; rival-kills inside batteries don't count).
- "0 demotions": FALSE. 43="me" MEDIUM→WEAK was worker-decided (morphologist
  WO-B: adverses outweigh supports, kill rule n≥3 not met) and recorded in the
  round-6 status line. Corrected: **1 demotion**.
- "0 promotions": FALSE as an unqualified headline. 00="pour" moved
  lead→STRONG LEAD (F40→F47; worker-offered, coordinator-recorded). Under the
  lane's F37 precedent ("promotion" = elevation to provisional+), zero
  promotions-to-provisional is true — but unqualified it obscures two LEAD-tier
  elevations (00="pour"→STRONG LEAD; 59="est" entering new at STRONG LEAD, a
  two-grade fast-track that should have been staged or explicitly justified).
- **Corrected net: 0 promotions to provisional-or-above; 2 LEAD-tier elevations
  (both upheld, see F45/F47); 0 kills; 1 demotion (upheld).**
- All N44 headline stream numbers re-derived and CONFIRMED: n62=35, n94=37,
  n06=44, n78=31, n59=27, n84=25, n00=55, n47=28, n45=22, n16=28, n24=52, n52=27;
  62→94=9, 78→45=4, 00→86=12, 00→06=0, 46→62=0, 47→46=3, 47→64=0, 94→82=4,
  77→78=7, 77→86=5 (61/61 extension PASS).

### F45 — curator: HELD at STRONG LEAD → **UPHELD** (promotion to provisional DENIED)
Re-derived: 64→59 ×3 @315/1209/1776 (S2) ✓; 94→59 ×3 @558/762/1795 (S3) ✓;
59→46 ×2 @216/1190 (S4) ✓; S1 (27/1847)/0.01054=1.387× ✓; S4 (2/27)/0.0137=
5.41× adverse ✓ (worker wrote 5.40× — immaterial); 59→37 ×6 ✓; rivals killed on
rate (worker era-derived). The hold is correct: S4's 5.4× adverse (n=2) plus the
87→59 @824 "c'est" interaction (/ɛ/→{01,59} allophony OR 01≠"est", which would
weaken A1) are genuine unresolved blockers. The worker's "promotion-ready
pending red-team" is answered: NOT promotion-ready. Wording correction: the
record should read "promotion to provisional DENIED (S4 + 01-interaction)",
not the ambiguous "HELD". 59="est" enters new at STRONG LEAD (worker-offered;
fast-track flagged — round-7 executors may not cite it as ladder-climbed).

### F46 — 84 CONFLICT, both LEAD → **UPHELD** on grades and conflict banking; **POSITION LIST CORRECTED**
Re-derived: 77→84 ×7 starts @[145,259,1057,1446,1484,1763,1802] ✓
(worker-correct); 11→84 ×1 start @1619; 94→84 ×1 @1664; 82→84 ×1 @166;
46→84 ×2 @309/@472; 84→59 ×4 @1189/1290/1447/1803; E2 P(84|46)=2/29=0.0690 ✓.
**Correction:** NOTES.md F46's "curator re-derived" list
@[146,260,1058,1447,1485,1764,1803] is +1 on all 7 — successor indices, not
bigram starts. The worker's list was correct; the coordinator mis-cited
(traceability defect, F26-6 class). Same +1 slip inside closer87_00.md's own
table: 94→84 @1665→1664, 11→84 @1620→1619 (77→84 cited as starts in the same
table — worker-internal convention inconsistency; counts all correct).
Grades: 84="en" LEAD (E1 1.10×, E2 1.36× GT-anchored, E5 weak, 24/25 windows
clean; BLOCKED by E4 "l'en" 141×/63× over era under 77="le") ✓; 84=masculine-
noun LEAD (article + que-subject frames; identity NULL, register-robust) ✓.
Conflict correctly banked for round 7; the conditioned-polyvalence resolution
sketch stays flagged untested, not adopted.

### F47 — 00 CONFLICT → **UPHELD** on both grades and conflict banking
00="pour" STRONG LEAD: 00→86 ×12 vs 00→06 ×0 ✓; P(86|00)=12/55=0.2182 ✓;
06→00 ×4 @184/544/666/738 ✓; 00→46 ×4 @106/545/1545/1680 ✓; 00→11 ×4 ✓; rival
sweep incl. "et" killed 6.5× on the discriminating leg (worker era-derived).
Blockers B1 6.22× + B3 3.85× correctly prevent provisional. The lead→STRONG
LEAD elevation is upheld (this is the promotion N44 failed to count).
00="le" LEAD: 96→00 ×3 @47/465/960 ✓, null 0.5% ✓, provisional-dependent,
correctly tensioned vs F40. Conflict correctly banked; conditioned resolution
or kill in round 7.

### F48 — "parmi" LEAD + "cela" corroboration → **UPHELD**
pairs[1196:1199]=[96,82,16] ✓; "parmi" cells [par,m,i], ev 96=par PROV-STRONG +
82=m GT, status CRIB-PROPOSAL-unique, era freq 174 ✓. pairs[269:271]=
pairs[357:359]=[47,11] ✓; "cela" cells [ce,la], ev 47=ce LEAD + 11=la GT ✓.
The 16="i" entailment battery correctly flagged as needed (34=i GT). LEAD grade
correct.

### F50 — 78-45="même" LEAD → **UPHELD** on grade; **POSITION CORRECTED**
pairs[312:316]=[37,78,45,64] ✓ — the «le même qui» quad starts **@312, not
@313** (NOTES F50 and closer6.md "@313 = 24-37-78-45-64" both mis-cite; the
5-mer starts @311, the quad @312; 78-45 @313 ✓). 78→45 ×4 @313/573/982/1164 ✓;
0.57× in-band (worker era-derived); era locks worker-derived; the @312 lock is
conditional on 37="le" MEDIUM — correctly noted. 45="me"-word DISFAVORED-strong
(9.14× out), not REFUTED (kill leg fenced on 64="qui" provisional) — correct
conservative grade.

### F51 — "le me"×7 DISSOLVED (conditionally) → **UPHELD**
77→78 ×7 @[7,213,647,1077,1180,1351,1542] ✓; 2/7 = 78→94 islet @1180/@1351 ✓
(78→94 ×2 @1181/@1352); 5/7 me-syllable frames; P(78|77)=0.1591 vs
P(78|47)=0.1786 ✓; era («le»,«me»)=0/4570 (worker-derived). Both fences
explicit: (i) the 2 islet instances ride on the fenced «gouvernement» host —
now confirmed as "gouv" by the T4 ruling below, which STRENGTHENS this leg;
(ii) the 5 ride on 78="me"-syllable LEAD, whose fall revives the kill-grade
adverse — correctly flagged.

## Coordinator bars misapplied (F26-17 scope)
1. **N44 net count** — contradicts the lane's own round-6 status line and
   obscures the 00="pour" elevation. Corrected above.
2. **F46 position list** — curator's "re-derived" positions uniformly +1
   (successor indices); correct starts [145,259,1057,1446,1484,1763,1802].
3. **N42 either/or framing** — "(a) keeps 77=le" misstates F37: 77="le" was
   fenced OUT at @1180/@1351 by the round-5 red team, so (a) must OVERTURN F37,
   not "keep" a status. Understates (a)'s cost.
4. **F45 "HELD" wording** — ambiguous given the worker asked red team to rule
   on promotion. Correct record: promotion to provisional DENIED.
5. **Uncaught worker convention slips** (F26-6 traceability): closer87_00.md
   mixes bigram-start and successor-index citations in one table; closer6.md
   "@313 = 24-37-78-45-64" (quad @312); frenchman "@508" for 77→62 (starts
   @507). Counts all correct; indices corrected in `verify_f26_17.py`.
6. No double-counting found; no N28/N35 case-law violations in the marks; the
   coordinator correctly propagated provisional statuses and fenced
   dependencies.

## Confirmation for other executors
All UPHELD marks are now agent-adjudicated and may be built on. Use the
corrected position lists (F46, F50) — `code/crowd7/redteam/verify_f26_17.py`
(61/61 PASS) is the citation source, superseding the NOTES.md figures. N44's
net is corrected as above.

---

## T4 either/or adjudication (work order 3)

**Ruling: tiling (c) gouv|er|ne|m|ent ("gouvernement" proper) SURVIVES as a
LEAD-grade reading. Tiling (a) le|gou|ver|m|ent ("le gouverment") is
DISFAVORED. Tiling (b) is dead (94="er" collides with GT 29="er"). The
either/or is RESOLVED in favor of (c) — not unresolvable. NO status change to
94="ne" (stays provisional-strong) or 77="le" (stays provisional-conditioned).**

1. **(a) is doubly blocked by standing adjudications.** It needs 77="le" at
   @1180/@1351 — but the round-5 red team fenced 77="le" OUT at exactly these
   windows (F37: "the 'gou'@1180/@1351 exception FENCED"). The drag produced no
   evidence against the fence. It also needs 94="ver" at exactly these windows,
   demoting 94="ne" provisional-strong whose banked legs stand (unigram
   1.025×, trigram ×3 @1.054× era "-nement", 94→52/59 "ne se" ×5). A "94=ver
   iff T4 window" rule has n_eff=1 and must distinguish @1180/@1351 from @578
   (independently 94="ne" per F39) — unfalsifiable by construction, fails the
   F33 bar (verified, falsifiable conditioning rules; zero free cases).
2. **(c) preserves every banked status**: 94="ne" prov-strong ✓, 82=m GT ✓,
   06="ent" restricted-PLAUSIBLE ✓ — and it CONFIRMS F37's fenced trigger (the
   "gou" exception resolves to "gouv"). (c) does not "break" 77="le": 77="le"
   was never claimed at these windows.
3. **(c)'s only cost is F38's 78="ver" islet — whose "ver"-specific evidence is
   contaminated.** The islet ("ver iff next=94", 2/2 @1181/@1352, n_eff=1) rests
   on "'vernement' 554 vs 'verrement' 0" — but the worker's own memo states the
   554 are ALL "gouvernement*" (bigram78_77_578.md L39). "vernement" is not a
   word; inside "gouvernement*" it parses morphemically as gouv|erne|ment —
   supporting 78="er" (tiling c), not 78="ver". The worker's binary (ver+ne vs
   ver+re) never tested the live alternative er+ne. The islet's valid core —
   "78≠me at these windows given 94='ne'" (from "me ne" era-0) — stands and is
   preserved under (c).
4. **C3 lexicon background favors (c)**: @T4 ne×10/ver×0/er×3; @578
   ne×3/ver×0/er×17. (a)'s defense (the by-ear misspelling "gouverment" sits
   outside the lexicon by construction) is an unfalsifiable rescue positing an
   unevidenced encipherer misspelling; the lane prefers the real lexicon word
   under banked values.
5. **Shape HIT stands** (C1 exact by-ear fits at both windows, 82=m
   GT-anchored; C2 family 1/11,870, null 2.43%/window; n_eff=1 across the
   byte-identical windows) — consistent with LEAD, not promotion.

**Status consequences (explicit):**
- 94="ne": NO CHANGE (provisional-strong).
- 77="le": NO CHANGE (provisional-conditioned). F37's fence stands; its trigger
  is now identified ("gouv") — confirmation, not breakage.
- Tiling (c) @1180/@1351: new LEAD-grade reading. Entails two new conditioned
  islets at LEAD: 77="gouv" and 78="er" at exactly these windows (n_eff=1;
  need independent support before any promotion).
- Tiling (a): DISFAVORED (blocked by F37 + 94="ne" prov-strong + F33 n_eff=1
  bar). Not killed — reinstatement needs independent evidence overturning
  F37's fence AND a falsifiable 94="ver" conditioning rule.
- **F38's 78="ver" islet: value DOWNGRADED to fork.** It becomes "78∈{ver, er}
  at 94-following windows (given 94='ne'), 78≠me" — LEAD-grade fork. The "≠me"
  core (from "me ne" era-0) is untouched. Explicit correction to a round-5
  red-team-adjudicated islet, on new analysis.
- F51's dissolution leg (i) is strengthened: the 2 islet instances' host is no
  longer "unconfirmed".

**What would change this:** (1) a second, non-byte-identical "gouvernement"
window (licenses an F33 conditioning rule for 77="gouv"/78="er"); (2)
independent evidence for 78="er" vs "ver" outside the T4 windows; (3) for (a):
evidence overturning F37's fence plus a falsifiable 94="ver" rule.
