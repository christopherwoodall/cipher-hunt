# Round-9 Red-Team Adjudication — executor status-change recommendations

Red team: round-9 red-team adjudicator (independent) · 2026-10-07 · kill authority
over all round-9 promotions. Scope: the round-9 executor recommendation packages
in `code/crowd9/report_inbox/` (docket: conditioner/islet-registry, 48-successor,
62-resolver, 67-finisher, smith-liaison, 77/78-hunter, 06-falsifier-watch).
Method: independent re-derivation on the repaired 1,847-pair stream
(`code/side-keyhunt/repaired_offsets.json`); baselines
`code/crowd7/redteam/verify_f26_17.py` (**98/98 PASS**, R9BANK) and
`code/crowd7/redteam/verify_round7.py` (**79/79 PASS**, ROUND8-LEDGER).
Pre-registered bars: `code/crowd9/redteam/PREREG-ROUND9.md` (written before any
executor numbers arrived; enforced verbatim). No coordinator-applied bars (F26-17).

## Pre-registration record (2026-10-07, before executor results)

- Baselines extended, not rebuilt, all on the repaired 1,847-pair stream:
  `verify_f26_17.py` 77/77 → **98/98 PASS** (R9BANK: 21 checks — the round-8
  adjudicated cipher-side facts: 48 H5 adverses + H2 4.78×, «qu'en» withdrawal
  windows, 66-84/89-84 conditional extensions n_eff=2+2, 82-84 GT frame,
  «qui le 84 59» ×2, S4#2 06-84-59-46, {93,8} homophony legs, 94-93-59 @101,
  06-islet n_eff=3 + GT core @578/@1182, @1246 window).
  `verify_round7.py` 58/58 → **79/79 PASS** (ROUND8-LEDGER: 21 checks — the
  round-8 status ledger with extended vocabulary; corpus-side drift guards on
  B1 3.91×/B3 3.19×, H2 4.775/KILL, L_B E/P0/LR, L_A, 06-islet windows,
  T1 p=0.9398 + verdicts; RdDM-293× independently recounted at 293 and its
  UNVERIFIED flag LIFTED).
- Status line banked (LEDGER8): 48="ne" **REFUTED** (F60), {93,8}="l'" LEAD,
  06="ent"-iff-82 LEAD, 62="il" DISFAVORED-STRONG, Mehemet-Ali LEAD-weak, 84
  en-islet re-scoped, 00="pour" STRONG LEAD (B1 3.91×/B3 3.19×), WO-6 criterion
  RETIRED, main-fleet search scope ZERO (F57).
- Bars pre-registered for all work orders (`PREREG-ROUND9.md`): ≥2 independent
  legs for ANY promotion (hold the line); n≥3 kill rule; F33 conditioning (no
  post-hoc partitions or condition expansions); no double-counting of banked
  legs; exact tests; Nesselrode-v8 rate bars with the fait 4.6× soft edge
  symmetric; era- and register-matched corpus legs with dispersion; clean fails
  are fails; T7 (no manual-tiling bearing counts); no re-litigation of settled
  kills (interim kill on violation); F60 interchangeability necessary≠sufficient;
  F56 merger template.

## Round-9 work-order compliance review (pre-registration audit of the orders)

The 7 round-9 work orders handed down in
`code/crowd8/adjudicator/RULINGS-FINAL.md` §"Round-9 work orders" were reviewed
for pre-registration compliance BEFORE any executor data. Verdicts:

1. **Conditioner successor** — COMPLIANT as written. "pre-register a test or
   keep as lead" is explicit; the 66/89 confirm-or-fall is falsifiable. EXECUTOR
   OBLIGATION: the 96=verb extension condition (pre=64 & suc=43) must be
   pre-registered BEFORE the qui-96-43 ×2 windows are classified — otherwise the
   classification is post-hoc and DENIED under F33/WO-4 precedent. 86's identity
   needs its own pre-registered ≥2-leg bar; it does not inherit one.
2. **48 successor** — COMPLIANT as written ("fresh battery, no allophony
   presumption"). EXECUTOR OBLIGATION: the battery must pre-register candidate
   values + exact tests + decision rule before data. F60 guard is ARMED: any
   ne-allophony re-litigation gets an interim kill. "on 48"×6 may not be spent as
   a 62="on" leg.
3. **62 resolver** — COMPLIANT in principle. EXECUTOR OBLIGATION: pre-register
   the independent cells (distinct from N39's ear cells) + discrimination
   criterion + decision rule. L_A/L_B are banked — re-spending them is
   double-counting.
4. **67 finisher** — COMPLIANT as written ("needs its own ≥2-leg bar per WO-7"
   is explicit). EXECUTOR OBLIGATION: the new arm's class definition must be
   concrete, falsifiable, and pre-registered before classification.
5. **Smith (objective-repair round 2)** — COMPLIANT. C1 gate is pre-registered
   (R10/F57); scope-zero holds until C1 passes. T7 is armed: any bearing-count
   scoring on manual tilings = interim kill of the memo's recommendation.
6. **77/78 hunter (8th) + 06 falsifier watch** — COMPLIANT as written: the
   falsifier is frozen verbatim. EXECUTOR OBLIGATION: "verbal frame" must be
   pre-registered F33-grade before the watch classifies; the 8th support hunt
   needs ≥2 NEW pre-registered legs (T4 5-mer is banked).
7. **No re-litigation** (93-alone kill, 48="ne" kill, refuge concretizations,
   retired WO-6 criterion) — standing rule, enforced by red team with interim
   kills. H5/H6-style adverses and the n≥3 rule stay the standing instruments.

_No executor pre-registration files have been received as of 2026-10-07 15:22 CDT.
Executor-level pre-registrations (`code/crowd9/<agent>/PREREG*.md`) will be
timestamp-audited on arrival: bars written AFTER the executor's data runs fail
the audit and the package is failed (work order 3)._

## Pre-registration audit results (packages landed 2026-10-07 ~15:20–15:23 CDT)

| Executor | PREREG mtime (UTC) | First data-run mtime (UTC) | Verdict |
|---|---|---|---|
| conditioner | 20:20:00 (PREREG9.md) | 20:20:14 (census_results.json) | **PASS** |
| successor48 | 20:21:15 (PRE-REGISTER.md) | 20:22:03 (battery48_verb.py) | **PASS** |
| resolver62 | 20:22:05 (PREREG.md) | 20:22:50 (battery.py) | **PASS** |
| hunter7778 | 20:22:11 (PREREG.md) | 20:22:25 (h1_h2_h4.py) | **PASS** |
| watch06 | 20:21:15.930 (PREREG.md) | 20:21:15.922 (census06.log) | **PASS WITH NOTE** (see below) |
| frenchman | — none on file — | 20:21:33 (corpus9.py) | **NO PREREG** (no promotion recommended; noted) |
| germanist | — none on file — | 20:20:59 (az_evidence.json) | **NO PREREG** (no promotion recommended; noted) |
| liaison | — none on file (memo, not a battery) — | 20:20:45 (smith-constraints.md) | **N/A** (memo banked as constraint) |

**watch06 note:** the census log predates PREREG.md by 8ms — a technical
inversion. It is EXPLAINED: PREREG.md carries a disclosed post-census addendum
("Addendum (post-census, 2026-10-07): index-convention correction"), whose edit
bumped the mtime; the bars' content is written in future tense and references
no census outcome. The executor's own report shows no bar-fitting (honest
middle verdict on the coincidence probe at p=0.0138 between the pre-registered
bars; the post-hoc 06-06 observation explicitly NOT scored; weakest window
@738 recorded). Audit = PASS. Methodology rule for future preregs: keep
post-census addenda in a separate file so the timestamp audit is clean —
unexplained inversions will fail.

**Content screen (all landed preregs):** no settled-kill re-litigation, no T7
bearing-count scoring, no post-hoc partitions. successor48's PRE-REGISTER.md
explicitly binds itself to F60 (kill legs not reused as positive legs);
V2 "ne-licensing" tests the verb hypothesis via nearby 94 — it does NOT
re-open 48="ne" (the kill stands untouched). conditioner respects F61/F62/F63
as adjudicated; resolver62's data-blindness statement bars ear cells and
L_A/L_B from recycling; hunter7778 attempts no promotion. **No interim kills
warranted.**

## Interim kills

_None issued as of 2026-10-07 15:35 CDT. Settled-kill re-litigation or
standing-rule violations in arriving packages are killed here immediately,
with the violated rule named._

## Rulings

### R1 — 06-falsifier-watch (`report_inbox/watch06-falsifier.md`): falsifier did not fire

**Ruling: GRANT the package (bank the negative finding; no status change).**
The frozen falsifier ("an 82-06 window in a verbal frame kills the islet")
was attempted on all three pre-registered prongs and did not fire:

- **FIRE-PART (partition defect): DOES NOT FIRE.** Independent census finds
  exactly the 4 predicted 82→06 windows (06-positions [580,738,1184,1355],
  re-derived ✓). The census log's "NOT on predicted W06" line was the
  index-convention artifact (06-positions vs the frenchman's 82-positions);
  the report catches and corrects it — the addendum is disclosed, not hidden.
- **FIRE-IN (domain contradiction): NO FIRE.** All four pre=82 windows pass
  the by-ear audit under the pre-registered rule (F34/F44): @580 "…nement"
  + boundary (second 06 pre=6, out-of-domain) ✓; @738 lone-82 "X-ment"
  (weakest leg — no 94 prefix, recorded honestly) ✓; @1184 "…nement est…"
  ✓; @1355 "…nement …" ✓. Zero in-domain contradictions.
- **FIRE-OUT (iff break): NO FIRE.** 40 out-of-domain windows screened under
  the pre-registered "reads cleanly as ent" rule; near-misses all rejected
  (@319 "neent" not French; @271 "la-ent" needs unlicensed elision;
  06→29 ×4 @[1096,1388,1709,1815] re-derived ✓ — banked by N19 as
  "ent|er" UNGRAMMATICAL, cited not re-spent ✓; all others unknown-gloss
  contact). The ← leg survives.
- **Coincidence probe:** n82=39, E[82→06]=0.93, obs=4, exact binomial
  P(X≥4)=0.0138 (re-derived ✓) — between the pre-registered bars (p>0.05
  adverse / p<0.01 real). Honest middle verdict; the fragility (one window
  from the fence at n_eff=3) is banked as a standing caveat for the
  conditioner, not a kill.
- **Successor-profile check:** correctly NOT scored (post-hoc — islet defined
  by pre=82, not suc=6); handed to the conditioner as a shape observation
  (94-82-06-06 core @578/@1182 may under-describe the frame). Hypergeometric
  P(X≥2)=0.0063 re-derived ✓.

**Disposition:** 06="ent"-iff-pre=82 holds conditioned LEAD. Zero adverses
found, zero fenced. The package recommends no promotion — none granted. The
fragility caveat, the @738 weakest-window note, and the post-hoc 06-06
observation are REFERRED to the conditioner (registry business), not rulings.

### R2 — smith-liaison (`report_inbox/liaison-smith.md` + `liaison/smith-constraints.md`)

**Ruling: BANK the memo as a constraint (round-8 R10 precedent). No status change.**

- The memo is a constraints spec + rebuild2 status report, not a promotion
  recommendation. No ≥2-leg promotion claim is made; none is granted.
- **Scope-zero holds:** "Nothing in this memo waives C1" (explicit); no
  scored comparison has run (no `results/` dirs); all three rebuild2 tracks
  executing per PREREG under sign-off. No scope expansion recommended.
- **Settled kills respected:** the must-NOT-break list (§4) carries 48="ne",
  93-alone, 24="est"/H5, 06-ent-general, single-stem-06, the 46-part of 84's
  condition, mute-e, retired WO-6, refuge concretizations, and the T7/C1
  prohibitions as PROHIBITIONS — compliance, not re-litigation. ✓
- **§1c "06=verb-stem class provisional":** consistent with the banked F25
  working state (NOTES.md: "verb-stem (class) PROVISIONAL general"); not a new
  promotion claim. The anchor set (7 GT + 5 provisional) matches the lane
  board. ✓
- **Citation-form note (substance confirmed):** §1c/§3 cite the 06-islet GT
  core as "94-82-06-06 @578-581, @1183-1186" — the second window is 0-based
  @1182 (the round-8 1-off slip; pairs[1182:1186]=[94,82,6,6] re-derived).
  The window exists; the citation is corrected here.

### R3 — germanist cross-check (`report_inbox/germanist-crosscheck.md`)

**Ruling: GRANT-WITH-MODIFICATION.** No vetoes; no promotion recommended; no
settled kill re-litigated. Evidence spot-checked (`az_evidence.json`:
"Mehemed Ali" 75×, Thiers 76×, Guizot 31×, Pforte 85×; AZ corpus 15 issues
present ✓).

**(a) M3 he-cell re-grade — GRANTED as scoped bookkeeping amendment.** M3's
banked adverse ("'he' writes a SILENT h... weak adverse... not kill-grade",
`battery_mehemet_results.json`) assumed French phonetics. The germanist's AZ
leg (German "Mehemed Ali" 75×, h pronounced /h/, final -d devoicing →
[meˈheːmɛt] converging with French [meemet]) makes the 'he' cell by-ear under
German phonetics for this proper name. The purity-cost adverse is STRUCK.
**Modification:** the strike is scoped to this German-phonetics basis — the
general "German-interference premise" is NOT banked as a lane premise, and
the germanist's own 78="ver" finding (French phonetics at that cell) shows
interference is window-specific. Mehemet-Ali @8 stays **LEAD-weak** (D1
62-tension + D2 "mêleront" stand; the struck adverse was weak, not load-bearing).

**(b) Germanism watch-items — BANKED as standing conditionals:** (i) a
standalone 78="er" outside the gouvernement formula → German "er" becomes a
live rival; (ii) 67@1248 X resolving to "cela/ça" → "dafür daß" calque,
evidence FOR interference. Neither fires now.

**(c) Crib list — REFERRED to the conditioner** (drag-order decision is
registry business). Guard banked: the 15× "Mohammed" is Dost Mohammed
(Afghan emir) — it must NOT enter the crib list as a Mehemed-Ali variant.

**Pre-registration note:** germanist has no PREREG on file. No promotion or
status-change was recommended, so no audit failure; any future germanist
promotion recommendation without a pre-registered bar is post-hoc → denied.

- Vetoes V1–V5 banked as constraints on future proposals, not kills.

### R8 — conditioner (`report_inbox/conditioner-islets.md`): 86 battery, 66/89, formulas, residuals

**Pre-registration audit: PASS** (PREREG9.md 20:20:00 < census 20:20:14 UTC).
Content screen: clean — F61/F62/F63 respected as adjudicated (not re-derived);
"do not re-litigate F55" and "do not re-litigate 43's WEAK status" honored;
T7 respected. No interim kill warranted.

**Ruling 1 — 86=que-family → REFUTED: GRANT (kill-grade, hypothesis-kill).**
Four pre-registered adverse legs, two at kill-grade exact tests:
- L2: 00→86=12/55=0.218 vs era P("qu'"|"pour")=0.0104 (21.0× OVER) and vs
  P("que"|"pour")=0.0238 (9.2× OVER) — re-derived ✓.
- L4: 86-vs-46(que-GT) profile parity fails (Jaccard 0.33/0.25).
- L5: elision kills "qu'" — 86→70 ×1 (70="pre" consonant), 86→52 ×2,
  86→56 ×4 re-derived ✓: 7/32 windows with consonant-initial successors;
  «qu'pre/qu'pas/qu'plus» impossible. (Report's "3–7/12" denominator is
  garbled; the verified 7/32 carries the conclusion.)
- L6: 77-86 ×5 @[430,798,877,950,1133] (77-indices; re-derived ✓) with
  77="le" at all five; era P("que"|"le")≈0.00007 — kill-grade adverse
  (mild circularity via 77="le" provisional disclosed in registry).
The prereg's verdict ladder omitted "REFUTED," but L5/L6 are pre-registered
exact tests firing at kill-grade and the standing n≥3 instrument covers the
ladder gap. Recorded as a **hypothesis-kill** (que-family was never a banked
status), not a status-line kill. F40's verb-stem-class working hypothesis
stands per the prereg ladder; 86's specific value stays NULL (honest).

**Ruling 2 — B3 dissolution premise DEAD; B3 (3.19×) STANDS: GRANT.**
The ratemodel's caveat was wrong twice over: the era number is 0.0343
French-only (not 0.31), so 16/55=0.29 would be 8.5× OVER (0.29/0.0343
re-derived ✓) — and 86 isn't que-family anyway (Ruling 1). Double dead.

**Ruling 3 — 64-77-84-59 ×2: NOTED (frame strengthened; unit hypothesis-internal).**
No promotion recommended, none granted. (i) Noun+"est" parse dead
(«qui le X est» 2/4.2M, «ce qui le X est» 0/4.2M). (ii) 59="est"-as-word
after 84 era-absent («qui le [V] est» 0/4.2M all verbs) — adverse datum
for 59="est" AT @1447/@1803, banked fenced n=2 (59="est" provisional
stands elsewhere). (iii) Viable parse: F62's bisyllabic-verb unit
(era-common «[N] qui le [V-bi]» frames). (iv) Prereg falsifier does not
fire (-este verbs era-common). The UNIT reading (84-59 = one verb) needs
unbanked 59 conditioned polyvalence → **referred as follow-up** (59
word-"est" vs verb-final-syllable battery + -este verb ID).

**Ruling 4 — qui-96-43 ×2 formula: HOLD GRANTED; 43="me" adverse BANKED.**
Windows re-derived @341/@1025 (the +1 shift; 45-64-96-43-87-01 @[340,1024]
✓). The pre-registered extension test (a/b/c) did not confirm: (a) PARTIAL
(left context only), (b) era «qui [V] me»=3/1597 (nonzero but rare),
(c) suc==43 is an unbanked extension of the suc==47 banking. Per WO-1 bar,
classification as 96=verb-stem DENIED; formula stays FORMULA-UNCONFIRMED.
**Banked datum:** 43="me" suffers a clitic-order adverse IN THIS FRAME
(«qui [V] me» ungrammatical as verb+object); 43="me" WEAK stands globally.

**Ruling 5 — 84's 9 residuals: GRANT (all RESIDUAL, no islet change).**
n84=25 = 5 en-islet + 2 withdrawn + 1 fenced + 8 rescoped-noun + 9 residual
✓. The only recurrent pre (53 ×2) has no class signature — recurrence
without class does not extend islets (round-8 prereg, binding). **@857's
lean change NOTED:** round-8's adverse-lean correctly WITHDRAWN (it was
conditional on 48="ne", KILLED F60 — dependency dissolution, not
re-litigation).

**Ruling 6 — 66-class / 89 noun-class: CONFIRMED GRANTED.**
66: «pour 66» ×7 re-derived @[188,245,253,714,1108,1493,1532] ✓ + era
«pour»+subject-pronouns=0 + 66-84 ×2 grammatical — ≥2 legs; class
CONFIRMED broad {noun, infinitive, nous/vous-type} (specific value NULL,
honestly). 89: 77-89 ×2, 29-89 ×5, 89-48 ×3 re-derived ✓ + full 14-window
census (n89=14 ✓), no kill-grade adverse — NOUN-CLASS CONFIRMED (52-89 ×2
tension fenced). The 84 en-islet's pre∈{66,89} arm dependencies HOLD.

### R9 — 67-finisher (`report_inbox/finisher67-classification.md`)

**Pre-registration audit: PASS** (prereg.md 20:26:59 < results_r9.json
20:27:13 UTC). Content screen: clean — no 62 duplication; fork re-scope
not attempted (correctly — needs its own ≥2-leg bar). No interim kill.

**Ruling 1 — @1248 NEITHER-fence UPHELD: GRANT.** Bar N1 (F1∧F2∧F3)
passes: parse-verified; "pour et que"="pour veut que"=0 (v8); new-arm
census null ("pour * que" middles {cela:3, empêcher:1}, no single-syllable
X with n≥2 — option (a) declined with evidence). The 62-conditionality is
carried forward procedurally (resolver62 HOLD — blocker not lifted, no
status change; the fence legs do not involve 62).

**Ruling 2 — @199 NEITHER-fence CONDITIONAL on 08="l'": GRANT (conditional).**
Bar N1 passes (@199: [60,8,67,76,87] re-derived ✓; "l et"="l veut"=0).
Fenced conditional on 08="l'" (LEAD) holding — if 08 is revalued, @199
reopens. Second fenced NEITHER-class window under the F63 mechanism.

**Ruling 3 — @630 et-CONDITIONAL: GRANT as conditional (not a classification).**
Bar E2 passes: L1 "et l'"=63 vs "veut l'"=1 (63≥20, 1≤3, ratio 63≥10 ✓);
L2 11→52=3 ≥2 ✓ (@630: [87,78,67,8,52] re-derived ✓). Conditions C1
(08="l'") and C2 (67 standalone word) explicit; C2 unresolvable — under
the clitic-"me" competitor @630 is NEITHER. Banked as conditional-et;
reverts to open-residual (or NEITHER) if C1/C2 fail. Not a promotion
(WO-4: neither arm promotes on this battery).

**Ruling 4 — 6 open-residual: CONFIRMED** (@633, @902, @1372, @1450, @1519,
@1623 — no standing rule or pre-registered bar fires; forcing
classifications on single legs would violate the ≥2-leg bar).

**Ruling 5 — R_veut4 DROPPED: CONFIRMED** (design-time null — v8 kills
both arms under the clitic reading; honestly recorded).

**Ruling 6 — fork scope: SUPPORTED, fenced n=2.** The WO-7 kill instrument
(≥3 unclassifiable opens or BOTH conflict) does not fire: 2 NEITHER-fenced
(@1248 upheld, @199 conditional), 0 BOTH conflicts. Fork stays SUPPORTED
with amended scope. The frenchman Gate 4 era-bounding (@1248 → {cela,
peu}-class/infinitive; finite-verb arms era-0) constrains any future arm
to non-finite/non-verb.

_All 9 executor packages ruled. No interim kills issued this round._

### R4 — 48-successor (`report_inbox/successor48-verbresidual.md`): H_verb KILLED, HONEST NULL

**Ruling: GRANT the K2 kill and the HONEST NULL.** 48 stays UNIDENTIFIED; no
verb reading promotes.

- Pre-registration: PASS (exemplary — F60 kill legs explicitly barred as
  positive legs; V1–V6 + K1–K4 + verdict rules pre-registered; Nesselrode v8;
  T7 respected). Content screen: clean — V2 "ne-licensing" tests the verb
  hypothesis via nearby 94; it does NOT re-open 48="ne" (the F60 kill stands
  untouched). No interim kill warranted.
- Numbers re-derived on the repaired stream: 48→52=2 @[283,1737] ✓;
  62→48=6 ✓; n52=27 ✓; E[62→48]=0.72, p(X≥6)=7.37e-05 ✓ (association genuine);
  E[48→52]=0.555, p=0.106 ✓ (the "pas" frame was never above chance);
  29 distinct successors/38 ✓ (**datum correction recorded:** the F60
  referral's "19 distinct" does not reproduce — old-parse figure; the
  repaired-parse 29 stands and is flatter, strengthening the syllable-cell
  alternative); V3 licensing 12/38=31.6% ✓; hard-incompatible 1 ✓; n96=21 ✓.
- **K2 fired per its pre-registered terms:** V2 ADVERSE (0/2 "48 pas" windows
  ne-licensed, robust to span-widening i−10) ∧ V3 31.6% < 40%. The bar binds
  (round-7 case law). The steelman (V3's 60% bar miscalibrated for a syllabic
  system → LEAD-weak) is DENIED: overriding a fired kill condition is
  post-hoc rescue, and the prereg's own verdict rules require "zero kills"
  for LEAD-weak — K2 fired, so even the steelman's fallback contradicts the
  prereg. Moreover V2 is independently confirmed (frenchman Gate 5: verbal
  "[V] pas" without "ne" is era-0 in 1841 formal prose), and the positive legs
  are both explicitly weak (V1's comparator collapsed to 2 forms — "est/a-class
  frequency," not "verb form"; V4 is absence-of-a-kill on unbanked successors).
- **H_stem: unsupported, stays untested.** V5 NULL was pre-registered as
  underpowered-not-adverse (n96=21); correctly not claimed either way.
- Rulings on the five referred questions: (1) K2's verdict logic —
  **GRANTED** (H_verb dead as a LEAD candidate). (2) V1's comparator collapse —
  mechanical PASS-weak stands as recorded; the caveat binds the leg's weight;
  no re-run without a new prereg (correctly not done). (3) 29-vs-19 —
  **datum correction banked** (above). (4) Syllable-cell alternative —
  **REFERRED to the coordinator as a round-10 lead** (untested, not a claim);
  the "on"-association (p=7.37e-05) noted for verb-initial-syllable mining.
  (5) K3 — withholding confirmed correct: @1350's nearest candidacy is saved
  by the syllabic rescue, which K3 explicitly allows.

### R5 — 62-resolver (`report_inbox/resolver62-onil.md`): HOLD

**Ruling: GRANT the HOLD.** No status movement for 62="on" (fenced STRONG
LEAD) or 62="il" (DISFAVORED-STRONG). The WO3 blocker is carried forward.

- Pre-registration: PASS (exemplary — data-blindness statement; ear cells,
  L_A/L_B, 62→94/62→48 barred from recycling; Nesselrode v8 only; exact
  binomials). Content screen: clean.
- Numbers re-derived: C1 62→59=0/35, E_on=1.12, E_il=3.24,
  p_two=0.630/0.072 ✓; C2 59→62=0/27 ✓; C3 62→(93|8)=1/35 @1539 (k3=0/1) ✓;
  C4 1/35 ✓; PAIRS[100:104]=[62,94,93,59] ✓; 62→01=0, 01→62=0 ✓; L_A
  predecessors @10/@944/@1323/@1685 = {13,18,40,80} ✓ (none 46="que" —
  no "que l'on" frame).
- All four cells NULL against their pre-registered bars — honest nulls, no
  quiet upgrades. C1's p_two_il=0.072 stays a sub-bar lean (the report
  explicitly refuses to move it post-hoc — correct).
- **@100 "62 ne l'est": admissible as a FENCED n=1 descriptive, zero leg
  weight.** The predecessor contact (position 100's value) is a distinct
  datum from M_hom's trigram leg (101–103); at n=1 it fences per the n≥3
  rule. Noted tension: the frenchman's "on ne l'" ×3 (compositional
  "era-good") vs the resolver's full "on ne l'est" ~absent — both fenced,
  neither moves status.
- **C1–C4 banked as tested-NULL** (with their pre-registered fences) —
  future batteries may not re-run them as fresh cells.
- Mehemet-Ali stays LEAD-weak; @1248 still needs its own ≥2-leg arm.

### R6 — 77/78-hunter 8th attempt (`report_inbox/hunter7778-8th.md`)

**Ruling: GRANT — bank H3a as a WEAK leg for fork-tine (c); fence the @1351
items; no promotion (correctly not attempted).**

- Pre-registration: PASS. Content screen: clean (T7 respected; N46-amended
  claim not cited; no promotion attempted — the ≥2-leg bar correctly applied
  to itself).
- **H3a: BANKED as a WEAK leg for (c).** Passes its pre-registered bar
  (≥5×, Fisher p<0.01): er|ne 52 tokens/22 types vs ver|ne 5/3 (proper
  nouns/noise only), 10.4×, p=3.2e-11, gouvernement-family excluded
  (else circular). Weak by construction (language stat ≠ encipherer cut) —
  banked at exactly that weight. Fork-tine (c) now holds: lexicon-lean +
  H3b + H3a — still below any promotion bar. Fork stays unresolved.
- **H1c / H1d: FENCED per their pre-registered terms** (n=1 each). On the
  referred question (fence the @1351 window vs revisit a neighbor):
  **fence, don't revisit.** 62="on" is STRONG LEAD, 37="le" MEDIUM,
  64="qui" provisional — revisiting a banked neighbor on n=1 tensions is
  disproportionate. The @1351 window now carries three independent fenced
  items (H1c, H1d, frenchman Gate 6 triple collision) — recorded as an
  accumulation for round 10, not a kill (no pre-registered kill condition
  exists for the islets; the n≥3 rule binds).
- H2: consistency PASS (not a leg) ✓ — F61's prediction holds on all
  77-78-adjacent 06s; 78→94 only @1181/@1352 re-derived ✓.
  H1b: NULL (bar failed on n) ✓. H4: NULL ✓. H1e packaged for
  successor48 (not a claim here) ✓.

### R7 — frenchman era/register gate (`report_inbox/frenchman-register.md`)

**Ruling: NOTED (no status recommendation made; fenced items banked).**
The frenchman is outside the ruling docket and recommends no promotion or
kill — per PREREG-ROUND9 its report is noted, with the evidence it produces
banked where it touches the docket:

- **Gate 1:** {93,8}="l'" era SUPPORT noted (already LEAD — no promotion).
  93-alone kill CONFIRMED on strict v8 (p=0.0003) — settled kill upheld,
  not re-litigated ✓. The "l'pas" conjunction veto banked as adverse datum
  (93→52 @[159,263], 8→52 @[631] re-derived ✓) — per-window, one reading
  must give. Register flag (v8 E=32.9 in-band vs pooled E=11.9) is honest
  dispersion reporting; the brief names v8 as the bar ✓.
- **Gate 2:** two FENCED n=1 adverses on the 06-islet's by-ear readings —
  @1184 ("ne mentent/entendent est" ungrammatical with 59="est"-as-word;
  escape hatches noted) and @738 (technical: stem 18 unidentified, fails
  the bar's letter, no content contradiction). Both fenced; R1 stands
  (different test than the frozen falsifier — contact-violation vs
  grammaticality). The over-splitting lens (06 as sub-syllabic fragment,
  not spoken syllable) noted as methodology.
- **Gate 3:** 84 en-islet predecessors era-attested; "qu'en en" ×0 —
  withdrawn legs stay withdrawn ✓.
- **Gate 4:** 67@1248 era-bounded to {cela, peu}-class or infinitive;
  finite-verb third arms era-0 — **constrains the 67-finisher's arm**
  (pending package).
- **Gate 5:** 48 vetoes noted — the missing-"ne" veto converges with R4's
  V2 (independent confirmation); the @1350 clitic-order veto constrains the
  (48=transitive-verb ∧ 77="le") conjunction only.
- **Gate 6:** @1351 triple collision — third fenced item vs the @1351
  window (with R6's H1c/H1d); era favors the 06-islet parse ("ne ment pas")
  over the gouv parse there. Accumulation recorded for round 10.
- Vetoes V1–V5 banked as constraints on future proposals, not kills.
