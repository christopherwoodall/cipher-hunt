# Red-team round-9 report — baselines extended, bars pre-registered

2026-10-07 15:22 CDT · round-9 red-team adjudicator (independent) · kill authority
over round-9 promotions.

## JOB 1 — baseline extensions (extended, not rebuilt; all checks on the repaired 1,847-pair stream)

- `code/crowd7/redteam/verify_f26_17.py`: 77/77 → **98/98 PASS**. R9BANK adds 21
  checks — the round-8 adjudicated cipher-side facts (RULINGS-FINAL.md R1–R7):
  48 H5 adverses @863/@1657 + H2 kill-leg cipher part 4.78×; «qu'en» withdrawal
  windows (46-84-24-37-78 ×2 @309/@472); conditional 66-84/89-84 extensions
  (84-indices [154,1151]/[276,1378], n_eff=2+2); 82-84 GT frame @167;
  «qui le 84 59» ×2 @1445/@1801 (referred); S4#2 06-84-59-46 @1188;
  {93,8}="l'" legs (n93=14/n8=18, (93|8)→62 @10/@1685/@944/@1323, shared
  predecessors {45,67,85}, shared followers {29,52,62}); 94-93-59 @101;
  fenced costs 93→52=2/87→8=1; 06-islet (06-indices [580,738,1184,1355],
  n_eff=3, GT core 94-82-06-06 @578/@1182); @1246 window [16,00,67,46,26].
- `code/crowd7/redteam/verify_round7.py`: 58/58 → **79/79 PASS**. ROUND8-LEDGER
  adds 21 checks: the round-8 status ledger (LEDGER8 — 20 statuses, vocabulary
  extended for DISFAVORED-STRONG/LEAD-weak/refuted-with-modifiers); 48="ne"
  settled-killed; corpus-side drift guards on the archived executors' results
  (B1 3.91×/B3 3.19× French-only; H2 4.775/KILL; L_B E/P0/LR; L_A; 06-islet
  windows; T1 p=0.9398 + patternist verdicts); F59's RdDM-293× UNVERIFIED flag
  LIFTED — independent recount of 'Méhémet-Ali' in the 4-tome 1841 RdDM corpus
  reproduces **293** exactly.
- Both scripts exit 0. Existing checks untouched.

## JOB 2 — pre-registered bars (written before any executor numbers arrived)

`code/crowd9/redteam/PREREG-ROUND9.md` holds the kill/confirm thresholds for all
round-9 work orders. Standing rules enforced verbatim: **≥2 independent legs for
ANY promotion** (hold the line); n≥3 kill rule; F33 conditioning (pre-register
partitions — and no post-hoc CONDITION EXPANSIONS, e.g. 96=verb to suc=43);
no double-counting of banked legs (round-8 R1–R9 legs are spent); exact tests;
Nesselrode-v8 rate bars with the fait 4.6× soft edge symmetric; era- and
register-matched corpus legs with dispersion; clean fails are fails; T7 (never
score manual-tiling bearing counts); **no re-litigation of settled kills**
(48="ne" F60, 93="l'" alone, refuge concretizations, retired WO-6) — interim
kill on violation; F60 (interchangeability necessary≠sufficient); F56 merger
template. No coordinator-applied bars (F26-17).

Key per-order bars:

- **Conditioner:** qui-96-43 ×2 classification needs the extension condition
  (pre=64 & suc=43) PRE-REGISTERED before classification — post-hoc expansion
  DENIED. «qui le [verb=84-59]» promotion blocked until 59-as-syllable is banked
  (≥2 legs); stays a lead. 66/89 readings: confirm or the corresponding
  extension falls (GT-anchored pre∈{82} survives). 86's identity needs its own
  ≥2-leg bar; B3 dissolution needs zero unexplained residuals at n≥3.
- **48-successor:** battery must pre-register values + exact tests + decision
  rule before data; post-hoc naming DENIED. F60 guard ARMED — ne-allophony
  re-litigation = interim kill. "on 48"×6 may not be spent as a 62="on" leg.
- **62-resolver:** independent cells (not N39's ear cells) + criterion +
  decision rule pre-registered; L_A/L_B re-spending = double-counting. "on"→
  provisional needs ≥2 NEW legs; "il" kill needs the M1-template + grammatical
  adverse. Mehemet-Ali D1 and @1248 stay blocked on this battery.
- **67-finisher:** new arm needs a concrete falsifiable class pre-registered
  before classification + ≥2 independent legs. Fork kill: ≥3 unclassifiable
  opens or any BOTH conflict. @1248 stays fenced.
- **Smith-liaison:** scope ZERO until C1 passes (F57); memos banked as
  constraints. T7 armed — bearing counts on manual tilings = interim kill.
- **77/78-hunter + 06-watch:** 8th attempt needs ≥2 NEW legs (T4 banked).
  "Verbal frame" pre-registered F33-grade before the watch classifies; a flagged
  82-06 window verbal under the frozen definition → islet KILLED.

## Round-9 work-order compliance review (pre-registration audit of the orders)

The 7 work orders (RULINGS-FINAL.md) were reviewed before executor data: all
COMPLIANT as written, with executor obligations recorded in RULINGS-ROUND9.md —
conditioner must pre-register the 96=verb extension condition; 48 battery must
pre-register values/tests/rule; 62 battery must pre-register independent cells;
67 must pre-register the arm class; smith holds scope-zero; 06 watch must
pre-register "verbal frame". Executor-level pre-registrations will be
timestamp-audited on arrival: bars written after data runs fail the audit.

## Rulings on promotion recommendations

**Three packages landed 2026-10-07 ~15:20–15:23 CDT; all ruled.** Full
rulings with file+line citations and re-derived numbers in
`code/crowd9/redteam/RULINGS-ROUND9.md` (R1–R3). Interim kills: **none** —
every landed prereg passed the content screen (no settled-kill re-litigation,
no T7 violations, no post-hoc partitions).

### Pre-registration audit (timestamps)

| Executor | Verdict |
|---|---|
| conditioner | PASS (PREREG 20:20:00 < data 20:20:14 UTC) |
| successor48 | PASS (20:21:15 < 20:22:03) — exemplary F60 binding |
| resolver62 | PASS (20:22:05 < 20:22:50) — data-blindness statement |
| hunter7778 | PASS (20:22:11 < 20:22:25) |
| watch06 | PASS WITH NOTE — census log predates PREREG by 8ms, explained by the disclosed post-census addendum (bars in future tense, no outcome references, no bar-fitting); future preregs must keep addenda in a separate file |
| frenchman / germanist | NO PREREG on file (no promotion recommended; noted — future promotion without one is post-hoc → denied) |

### R1 — 06-falsifier-watch: GRANT (bank the negative finding; no status change)

The frozen falsifier was attempted on all three pre-registered prongs and did
not fire. FIRE-PART: census finds exactly the 4 predicted 82→06 windows
([580,738,1184,1355], re-derived). FIRE-IN: 4/4 by-ear audits pass (@738
weakest, recorded). FIRE-OUT: 40 out-of-domain windows screened, near-misses
rejected under the rule (06→29 ×4 cited from N19, not re-spent). Coincidence
probe: P(X≥4)=0.0138 (re-derived) — between the pre-registered bars; honest
middle verdict, fragility (one window from the fence at n_eff=3) banked as a
standing caveat. Successor-profile correctly NOT scored (post-hoc). Zero
adverses. **06="ent"-iff-pre=82 holds conditioned LEAD.**

### R2 — smith-liaison memo: BANK as constraint (no status change)

Constraints spec + rebuild2 status; no promotion recommended. Scope-zero
holds ("Nothing in this memo waives C1"); settled kills carried as
prohibitions (compliance, not re-litigation); §1c "verb-stem class
provisional" matches banked F25 working state. Citation-form note: GT core
"@1183-1186" corrected to 0-based @1182 (round-8 slip; window exists).

### R3 — germanist cross-check: GRANT-WITH-MODIFICATION

No vetoes. **M3's he-cell purity adverse STRUCK** (scoped): AZ "Mehemed Ali"
75× with pronounced /h/ makes the 'he' cell by-ear under German phonetics —
the adverse assumed French phonetics. Modification: the general
German-interference premise is NOT banked; interference is window-specific
(cf. the germanist's own 78="ver" French-phonetics finding). Mehemet-Ali @8
stays **LEAD-weak** (D1 + D2 stand). Watch-items banked as conditionals
(standalone 78="er" → German "er" rival; 67@1248="cela/ça" → "dafür daß"
calque). Crib list referred to the conditioner; "Mohammed"=Dost Mohammed
guard banked.

_Pending: conditioner, successor48, resolver62, hunter7778, 67-finisher
(still running; rulings continue in RULINGS-ROUND9.md as they land)._

### R4 — 48-successor: GRANT (H_verb KILLED, HONEST NULL)

K2 fired per its pre-registered terms: V2 ADVERSE (0/2 "48 pas" ne-licensed,
span-robust) ∧ V3 31.6% < 40%. The steelman (V3 miscalibrated → LEAD-weak)
DENIED — overriding a fired kill is post-hoc rescue, and the prereg requires
"zero kills" for LEAD-weak. V2 independently confirmed (frenchman: verbal
"[V] pas" without "ne" is era-0); V1/V4 explicitly weak. **H_verb dead; 48
stays UNIDENTIFIED.** H_stem untested (V5 underpowered, not adverse).
Datum correction banked: 48 has 29 distinct successors (not 19 — old-parse
figure). Syllable-cell alternative referred to the coordinator as a round-10
lead. All numbers re-derived ✓.

### R5 — 62-resolver: GRANT (HOLD)

No cell met its bar (C1–C4 all NULL; C1 p_two_il=0.072 stays sub-bar lean —
no quiet upgrade). **No status movement**: 62="on" fenced STRONG LEAD,
62="il" DISFAVORED-STRONG. @100 "62 ne l'est" admissible as FENCED n=1
descriptive, zero leg weight (predecessor contact is a distinct datum from
M_hom's trigram; the frenchman/resolver "on ne l'est" attestation tension
noted, both fenced). C1–C4 banked as tested-NULL. Mehemet-Ali stays
LEAD-weak; @1248 still needs its arm. All numbers re-derived ✓.

### R6 — 77/78-hunter: GRANT (H3a weak leg banked; @1351 fenced; no promotion)

**H3a BANKED as a WEAK leg for fork-tine (c)** — passes its pre-registered
bar (10.4× ≥5×, Fisher p=3.2e-11 <0.01; gouvernement-family excluded).
Fork-tine (c): lexicon-lean + H3b + H3a — still below promotion. Fork stays
unresolved. H1c/H1d fenced per their bars (n=1 each); on the referred
question: **fence the @1351 window, don't revisit neighbors** (62="on"
STRONG LEAD etc. — disproportionate on n=1). The @1351 window now carries
three independent fenced items (H1c, H1d, frenchman triple collision) —
accumulation recorded for round 10, not a kill (no pre-registered kill
condition; n≥3 binds). H2 consistency PASS; 78→94 only @1181/@1352
re-derived ✓.

### R7 — frenchman register gate: NOTED (no status recommendation)

Outside the ruling docket; fenced items banked where they touch it:
"l'pas" conjunction veto (adverse datum); @1184 + @738 fenced n=1 adverses
on 06-islet by-ear readings (R1 stands — different test than the frozen
falsifier); 84 en-islet predecessors era-attested; 67@1248 era-bounded
(non-finite); 48 vetoes (missing-"ne" converges with R4's V2); @1351 triple
collision (third fenced item). 93-alone kill upheld on strict v8 (not
re-litigated).

### R8 — conditioner: GRANT / GRANT / NOTE / GRANT / GRANT / GRANT

1. **86=que-family → REFUTED (kill-grade, hypothesis-kill): GRANT.** Four
   pre-registered adverse legs, two kill-grade exact tests: L2 (21×/9.2×
   OVER, re-derived), L4 (Jaccard 0.33/0.25), L5 (7/32 consonant-initial
   successors kill "qu'", re-derived), L6 (77-86 ×5, era P≈0.00007).
   Verdict-ladder gap covered by the standing n≥3 instrument. F40's
   verb-stem-class working hypothesis stands; 86's value NULL.
2. **B3 dissolution premise DEAD; B3 (3.19×) STANDS: GRANT.** Era number
   corrected (0.31 → 0.0343; 8.5× OVER re-derived) — and 86≠que-family anyway.
3. **64-77-84-59 ×2: NOTED** (frame strengthened; unit hypothesis-internal —
   needs unbanked 59 polyvalence; no promotion).
4. **qui-96-43 formula HOLD: GRANT; 43="me" clitic-order adverse BANKED.**
   Extension test (a/b/c) did not confirm → classification denied per WO-1.
5. **84's 9 residuals: GRANT** (no islet change; @857 lean correctly withdrawn
   on F60 dependency dissolution).
6. **66-class / 89 noun-class CONFIRMED: GRANT** (≥2 legs each; 84 en-islet
   pre∈{66,89} dependencies hold). All numbers re-derived ✓.

### R9 — 67-finisher: GRANT (all)

**@1248 NEITHER-fence UPHELD** (Bar N1 F1∧F2∧F3; new-arm census null;
62-conditionality carried forward). **@199 NEITHER-fence CONDITIONAL on
08="l'"** (reopens if 08 revalued). **@630 et-CONDITIONAL** (Bar E2 passes;
C1∧C2 explicit, C2 unresolvable — not a classification; reverts if
conditions fail). **6 open-residual confirmed.** R_veut4 dropped confirmed.
**Fork stays SUPPORTED, fenced n=2** (WO-7 kill instrument doesn't fire).

## Interim kills

None issued — all 9 packages landed; every prereg passed audit; no
settled-kill re-litigation, no T7 violations, no post-hoc partitions.

## Baselines (final)

- `verify_f26_17.py`: 77/77 → **114/114 PASS** (R9BANK +21, R9BANK2 +16)
- `verify_round7.py`: 58/58 → **82/82 PASS** (ROUND8-LEDGER +21, ROUND9 +3)
- F59's RdDM-293× UNVERIFIED flag LIFTED (independent recount: 293).
