# RULINGS-FINAL — crowd round 8 (independent adjudicator)

2026-10-07 · independent adjudicator (depth-2 subagent) · final ruling pass.
Scope: all 9 executor notes in `code/crowd8/report_inbox/` (+ `code/crowd8/morphologist/results_r8.json`
+ `code/crowd8/scorerliaison/` memos; no inbox note was left for the morphologist or scorer-liaison —
the artifacts above were ruled on directly). Bars: `code/crowd8/redteam/PREREG-ROUND8.md`
(binding; red team's `RULINGS-ROUND8.md` still records no arrived recommendations as of 15:01 CDT —
these rulings are the round-8 adjudication record).

## Independent re-derivation (repaired 1,847-pair stream, `repair_parse.load_rows`)

Every load-bearing cipher-side number behind the rulings below was re-derived before
ruling. All confirmed: n93=14, n8=18, n48=38, n94=37, n62=35, n84=25, n01=28, n59=27,
n00=55, (93|8)→62=4 (2+2), 62→48=6, 48→46=0, 48↔94=0, 59→37=6, 46→62=0, 00→46=4,
64-96-47 singleton (0-based 149–151; the only 96 with pre==64 AND suc==47; 96 suc==47
only @150), 06 pre==82 ×4 (0-based 06-indices [580,738,1184,1355]), 48→47→46 at
0-based [863,864,865], 24→48→47→98 at 0-based [1657..1660], 66-84 ×2 (0-based 154,
1151), 89-84 ×2 (0-based 276, 1378), 46-84-24-37-78 ×2 (0-based starts 309, 472),
64-77-84-59 ×2 (0-based starts 1445, 1801), 87→01 ×2, 47→01 ×1, 93→52=2, 87→8=1,
94-93-59 @0-based [101,102,103], @1248 window [16,00,67,46,26] 0-based.
Derived statistics re-checked by hand: H1 Fisher two-sided p=0.1997 ✓, C2 binomial
(27/55)^6=0.0140 ✓, merged 75/1847/0.00850=4.78× ✓, L_B LR=e^-1.77/e^-4.83=21.3 ✓.
RdDM spot-recount: 301 on a slightly broader form class vs the patternist's
293 clean-form 'Méhémet-Ali' — magnitude consistent, exact-form detail stands in
their script.

**Citation-form notes** (substance confirmed everywhere; cited in rulings):
(a) Homophonist's `@1658` is 1-based (0-based 1657=24); its `@863` is the 0-based index
of the 48 (trigram at 0-based [863,864,865]).
(b) Frenchman's `@579` = the 82 at 0-based 579 (06 at 580).
(c) Closer59's `@1193` is loose: the S4#2 window is 0-based [1188..1191]
(06-84-59-46); 84 at 0-based 1189, pre=06 — the unlicensed-classification finding stands.

## Docket

| # | Executor (work order) | Recommendation | Ruling | One-line justification |
|---|---|---|---|---|
| 1 | homophonist-48-ne (WO-1) | 48="ne"-allophone → KILL | **KILL** | H2 4.78× kill leg (bar >3×) + H5/H6 adverses; H1 min p=0.1997 does NOT fire |
| 2 | closer59-consolidation (WO-2) | 59="est" provisional CONFIRMED | **HOLD (provisional upheld)** | No new adverse reaches the demote bar; S5 quarantined adverse-to-conjunction; S4 residual widened 2/2 (0/79), count-n.s. |
| 3 | closer01-01-est (WO-3) | 01="est" CONFIRM MEDIUM | **GRANT** | D3 failed strictly (fait 4.6× < pre-reg ≥5× bar); C1 dead; C2 (p=0.014) is one leg, not two; exclusivity unproven |
| 4 | conditioner84-round8 (WO-4) | en-islet re-scope + qu'en withdrawal + noun NULL stands | **GRANT** | 46-legs killed at @310/@473 ("qu'en en" era-absent); re-scope pre∈{82} GT-anchored ∪ pre∈{66,89} conditional |
| 5 | ratemodel-00 (WO-5) | Replace B1/B3; accept ceiling | **GRANT** | English-dilution ~57% verified by tokenizer parity; residual 3–4× above the ≤2× promotion bar — strong-lead ceiling stands |
| 6 | morphologist (WO-6/WO-7, results JSON) | 96=verb LEAD n_eff=1; retire WO-6 bar; @1248 counterdatum; qui-96-43 referral | **GRANT / GRANT / fence n=1 / REFER** | Census found exactly one 64-96-47 window — the n_eff=2 criterion is logically unmeetable on this stream |
| 7 | frenchman-93-7778 (WO-9/10) | M_hom LEAD; 93-alone kill; 62 legs; 77/78 NULL; 06="ent"-iff-82 islet LEAD; amend N46 | **GRANT (all)** | 32 vs E=31.26 in-band + intermixing + "ne l'est" ≥2 legs; 06 islet n_eff=3 F33-form with frozen falsifier |
| 8 | patternist-16-mehemet-r8 (WO-11/12) | 16="i" stays; Mehemet-Ali LEAD→LEAD-weak; RdDM 293× verified | **GRANT (all)** | T1 clean wrong-direction fail + vacuous T2; D1 62-tension + D2 "mêleront" = 2 adverses → demote, not kill |
| 9 | segmenter-refuge-scope (WO-13) | Refuge scoped; concretizations dead | **GRANT** | X1–X4 signature+recoverability all dead; schema stays LOGICALLY-OPEN-NO-EVIDENCE (key recovery, standing) |
| 10 | scorer-liaison (WO-8) | Memos banked | **BANK** | No status change; search scope stays ZERO until C1 |

## Detailed rulings

### R1 — homophonist (`report_inbox/homophonist-48-ne.md`): 48="ne"-allophone → REFUTED

**Ruling: KILL.** The battery's pre-registered verdict logic (KILL if H1-fires ∨ H2>3× ∨
≥2 adverses) is satisfied twice over: H2 merged unigram 75/1847=0.04061 vs diplomatic
P("ne")=0.00850 → **4.78×** (bar >3×, pre-registered on the 00="pour" B1 word-level
precedent; arithmetic re-derived). H1 (F56 template) does NOT fire — min p=0.1997
across all 16 contact cells (re-derived 0.1997 two-sided) — which is the ruling's key
methodological point: **interchangeability is necessary but not sufficient for
homophony; contact-interchangeability survived while the merger died on rate + grammar.**
H5 is a genuine adverse: 48→47→46 at 0-based [863,864,865] with 46="que" ground truth
reads "ne ce que", ungrammatical, and 24→48→47→98 at 0-based [1657..1660] reads "en ne
ce" (doubly strained; Q2 forces 47="ce" at both). H6 (predecessor fit −0.585 nats) is
the second adverse (corpus-side, taken on the instrument; the 'en'×2 driver is
word-level valid). F58 referral now ADJUDICATED → **REFUTED**; 48 does not enter the
status line. 48=verb/verb-stem residual noted, NOT claimed. Recorded caveats stand:
sound-rate reading 2.86× (fence, not kill) kept beside the pre-registered word-rate bar;
48's identity stays open. With 48="ne" dead, closer59's conditional @1178 "n'est le"
worry evaporates (48 cannot be "ne"), strengthening the S5 quarantine (R2).

### R2 — 59-closer (`report_inbox/closer59-consolidation.md`): 59="est" provisional

**Ruling: provisional HOLDS (upheld — no demote, no upgrade).** Per the WO-2 bar,
CONFIRMED required ≥2 NEW positive legs + a falsifiable structural account of the S4#1
frame; the battery delivered neither (it delivered adverse-localization and a record
correction). What it delivered: (i) S5 is adverse-to-the-**conjunction**, not to 59 —
11.42× (32.63× bare-est) vs Nesselrode v8, worse than the old 6.47× Tocqueville figure;
the promotion verdict never used S5, so the pressure lands on the weaker conjunct,
37="le" MEDIUM (examined, not upgraded, not killed); S5's dependence is quarantined.
(ii) S4#2's round-7 "cleft conditioned on 84=noun" was unlicensed — pre(84) at S4#2 is
06 (verified), so 84 is UNCLASSIFIED per F53; **2/2** S4 windows (not 1/2) lack a
corpus-attested frame, 0/79 corpus-compatible — the stated residual is WIDER, but the
count-level adverse stays n.s. (P(X≥2|n=27)=0.11–0.31), no new cipher facts, no rival
promoted → no demotion bar met. 59="est" remains provisional with the bounded residual
stated: 2/2 S4 windows lack a licensed grammatical frame under banked values.
**Record correction banked:** round-7's "conditioned cleft" claim for S4#2 is retracted.

### R3 — 01-closer (`report_inbox/closer01-01-est.md`): 01="est" stays MEDIUM

**Ruling: GRANT CONFIRM at MEDIUM.** The pre-registered demotion bar needed D1∧D2∧D3;
D1 and D2 fired, D3 failed strictly — fait's L5 rival-kill is 4.6× vs the ≥5× bar on
Nesselrode v8 (re-computed from their numbers). The bar binds (round-7 case law); the
red team's flip-condition ("fait sustains L5 on substance") is NOT granted: 4.6× vs a
5× bar is a near-miss, not a pass, and the fait soft edge applies symmetrically to
59's L5 and 01's C3 (4.77×). Promotion is also out: C1 conditioning scan found no
F33-grade family (F4 rotation-trivial, F5 incomplete — no complementary split), and C2's
forced-frame exclusivity (6/6→59, p=0.014 re-derived; windows @[316,559,763,1210,1777,1796]
re-verified) is ONE leg, not two. **"Mutual exclusivity (59 wins)" is denied as an
available conclusion** — the WO-3 prereg denied it in advance, and this battery did not
supply the ≥2 legs to establish it. 59's legs remain 01-independent. **Convention
banked:** future rate bars use Nesselrode v8 (the banked "9–51×" L5 used diplomatic_all).

### R4 — 84-conditioner (`report_inbox/conditioner84-round8.md`)

**Ruling: GRANT the re-scope, the withdrawal, and the NULL-stands.**
(a) **«qu'en» legs WITHDRAWN** from en-islet support: at 0-based 309–311 and 472–474
(46-84-24-37-78 ×2, 1-based @310/@473), 24="en" holds STRONG locally and "qu'en en" =
0/4.2M era ("en en" absent in despatches_primary, noise-level elsewhere) — the B2
adverse is unrepairable under banked values. The formula stays an open residual
(repeated 5-gram, no valid reading under banked values).
(b) **En-islet re-scoped: 84="en" iff pre∈{82} (GT-anchored: @167 "m'en", n_eff=1) or
pre∈{66,89} (conditional extensions: 66-84 ×2 @154/@1151, 89-84 ×2 @276/@1378, n_eff=4;
conditional on the 66/89 noun-class readings, which are leads, not provisional). LEAD
holds at the re-scope.** The 46-part of F53's condition is falsified, not expanded —
shrinking a condition on an adverse is legitimate falsification, not post-hoc fitting.
9 windows remain residual (2 en-lean, 2 adverse-lean, 5 plain); @857/@1501 adverse-leans
are fenced (48="ne" now REFUTED — @857's "ne en" strain dissolves with R1).
(c) **Noun identity NULL STANDS** (bounded, not named): L1 fails for every candidate
(best 0.38×), @1620 «la 84 78» is a gender hole, @146/@260 have syllable successors,
and «qui le 84 est» ×2 is NOT article+noun (corpus: "qui le X"=515, X overwhelmingly
verbs). The «qui le [verb=84-59]» lead (needs 59-as-syllable, unbanked) is **REFERRED
to round 9, not claimed**. The conditioned noun-islet (pre∈{77,11}) keeps LEAD at
identity-NULL; @1803 withdrawn from its support, @1447 conditional (0-based 84-indices
1801/1445 verified).

### R5 — rate-modeler (`report_inbox/ratemodel-00.md`)

**Ruling: GRANT both recommendations.** (1) The standing figures are replaced: B1
9.14×→**3.91×**, B3→**3.19×** (French-only reference). The English-dilution mechanism
is verified: the modeler's pipeline reproduces the old 9.14×/6.22×/3.85× exactly
(tokenizer parity), and ~57% of the over was levant-p3 English denominator dilution;
French diplomatic "pour" is stable across independent sources (Nesselrode 0.00724 vs
levant-French 0.00814, within 12%). (2) The strong-lead ceiling is accepted: combined
floor 2.73× stays above the ≤2× promotion bar (WO-5 bar: B1 or B3 ≤2× on the
register-best corpus — not met); the demotion bar (r1 AND r3 ≤1.5×) is also not met.
The ~3–4× residual is an unexplained over, not a kill-grade adverse — the
identification rests on the B2a/B2b/B4/B5 conditional-profile legs, independent of
the unigram rate. 00="pour" stays STRONG LEAD. Follow-up for round 9: 86's identity
(86 que-family would dissolve B3).

### R6 — morphologist (WO-6/WO-7; `code/crowd8/morphologist/results_r8.json`)

**Rulings:**
(a) **96=verb-stem stays LEAD, n_eff=1.** The census found exactly ONE 64-96-47 window
(0-based 149–151; also the only 96 with suc==47, @150). No falsifier appeared.
(b) **RETIRE WO-6's "second window before promotion" criterion.** The cipher stream is
fixed and fully censused — if a second 3-gram existed it would already be found; the
n_eff=2 bar is logically unmeetable on R5005. Retired, not deferred. 96=verb's
strengthening path is now non-census evidence (downstream-verb hunt, etc.).
(c) **@1248 fork counterdatum: fenced adverse at n=1, no status change.** 0-based
@1248 window = [16,00,67,46,26] = "…pour 67 que" with 00="pour" STRONG LEAD and
46="que" GT; era "pour et que"="pour veut que"=0 — neither fork arm licenses the frame.
Per the WO-7 prereg (kill needs ≥3 unclassifiable opens or a BOTH conflict), one
NEITHER-class window does not demote the fork. The et/veut fork stays SUPPORTED;
9 opens unchanged.
(d) **qui-96-43 ×2 (0-based [341,342,343], [1025,1026,1027]) REFERRED to the
conditioner** as round-9 material (the 96's two non-@150 pre==64 windows, both suc=43).

### R7 — frenchman (`report_inbox/frenchman-93-7778.md`)

**Rulings:**
(a) **GRANT: M_hom {93,8}="l'" → LEAD (unconditioned homophones).** ≥2 independent legs:
(1) joint unigram n=14+18=32 vs E=31.26 dead-center, in-band in all four diplo slices
(two-sided p 0.47–0.60); (2) contact intermixing — shared predecessors {45,67,85}
(re-verified) and shared followers {29,52,62} (re-verified), (93|8)→62=4 (re-verified
2+2), zero GT-determiner predecessors; (3) "ne l'est" @0-based [101,102,103]=94-93-59
(grammatical, re-verified). Rival pairs eliminated (3.8e-4 etc.). Fenced costs stand:
93→52=2 ("l'pas", needs a vowel-initial third reading of 52 — 52's polyvalence is
K5-forced; unevidenced, recorded honestly) and 87→8=1 ("ce l'", one exception).
Rate-saturation corollary banked: 32≈31.3 caps the model space (no fused l'V cells).
(b) **UPHELD: 93="l'" ALONE rate-KILLED** (p=4.1e-4 in every diplo slice — banked, not
re-litigated).
(c) **GRANT: 62="il" → DISFAVORED-STRONG (not a full kill).** L_A: M_hom ∧ (93|8)→62 ×4
(@10/@944/@1323/@1685) ∧ diplo l'+il=0/4.2M — conditional kill on the LEAD-grade M_hom
condition; L_B: 46→62=0 with E[qu'on]=1.77 (P0=0.170) vs E[qu'il]=4.83 (P0=0.0080),
LR=21.3 (arithmetic re-derived) — M_hom-independent, single-datum with a
compositionality assumption, recorded. **62="on" stays fenced STRONG LEAD** (+2 non-ear
legs banked); the frenchman's "gains two non-ear legs, status unchanged" is correct.
(d) **GRANT: 77="gouv"/78="er" independent support NULL (7th consecutive); fork (a2)
vs (c) unresolved, lean (c).** Both stay LEAD n_eff=1. F38's "ver iff next=94" islet is
circular as a fork-resolver (defined on its only covered windows). The @1351 tension
(48="ne"-LEAD ∧ 52="pas"-STRONG ∧ 5-mer="gouvernement") is dissolved by R1: 48 is not
"ne", so the tension's weakest leg is gone.
(e) **GRANT: 06="ent" iff pre=82 → LEAD (conditioned).** n=4 (0-based 06-indices
[580,738,1184,1355]), n_eff=3, F33-form with stated falsifier ("an 82-06 window in a
verbal frame"). Pre-registration-form note: the partition was articulated in the
report, not the prereg — the condition (pre∈{82}, GT-anchored "ne-ment" frames) is now
frozen verbatim and banked; the in-prereg T4 5-mer windows (94-82-06-06 @578-581,
@1183-1186) supply the GT-anchored core.
(f) **GRANT: AMEND N46** — the "93 shape-STRONG (vow≥2)" claim is irreproducible
(fresh vow=1; round-7's archived u2_lcell.json lacks 93 entirely) — traceability flag
banked per F26 class.

### R8 — patternist (`report_inbox/patternist-16-mehemet-r8.md`)

**Rulings:**
(a) **GRANT: 16="i" stays unconditioned LEAD.** T1 (follower WI-enrichment) failed
cleanly in the wrong direction (p=0.9398; sensitivities S1–S3 all fail); T2
("premier"/"première" frame) was vacuous. The B1 redirect is exhausted; the
position-conditioned alternative is NOT SUPPORTED.
(b) **GRANT: "Mehemet-Ali" @8 DEMOTE LEAD→LEAD-weak.** Two moderated adverses (fenced
at n=2, not kill-grade): D1 62-tension (name's tiling needs 62='a' vs 62="on" STRONG
LEAD — no alternative me-initial len-5 tiling in the lane's by-ear top-8 instrument
avoids /a/ on 62) and D2 "mêleront" (me|le|r|on|t) — a common-word rival fully
compatible with 62="on". M2 (spelling/topicality) stands, so this is a demotion, not
a kill. Promotion stays blocked on 62="on" resolution.
(c) **GRANT: AMEND F59 — the RdM "293×" figure is VERIFIED.** The corpus was on the VM
(`code/side-period/corpus/revue-deux-mondes-1841-q1..q4.txt`, 1841 full run);
293× 'Méhémet-Ali' clean form (patternist's form table; my spot-recount 301 on a
slightly broader class — magnitude consistent). Cite as: **293× in the 1841 RdDM run
(4 tomes, archive.org OCR — OCR caveat)**. F59's UNVERIFIED flag is LIFTED (superseded).

### R9 — segmenter (`report_inbox/segmenter-refuge-scope.md`)

**Ruling: GRANT.** Four pre-registered syllable classes run through signature (C1) +
recoverability (ARI vs 200 random partitions): momentum z = −64.9 (X1), +8.6→−7.0
register-reversed (X2), −111.7 (X3), −100.2 (X4); ARI≈0 for all four on the
lane-faithful k=12/top-96 pipeline. Every concretization dead. The refuge schema
survives only unconcretized → **LOGICALLY-OPEN-NO-EVIDENCE** (standing; full kill
needs key recovery). No status change. The k=12 ARI rerun was labeled post-hoc
diagnostic in its own script — the in-prereg X1–X4 results are what the ruling rests on.

### R10 — scorer-liaison (`code/crowd8/scorerliaison/SCORER-CONSTRAINTS.md`,
`T7-STANDING-RULE.md`)

**Ruling: BANK.** Both memos banked as constraints for the search designer (WO-8):
C1 gate (truth > max random-20 on every gapped instance; currently 3/3 FAIL, worst
gap −0.28), diagnosed scorer facts (letter-term +0.09 nats above noise, word bonus no
separation, LAM_POLY=0.05 anti-truth −0.30), the banked-but-UNRUN prototype
(imports RepairedModel — do not "fix" by re-pointing), and the T7 standing rule
(never score manual-tiling bearing counts). **Main-fleet search scope stays ZERO
until C1 passes on the gapped family** (F57). No status change.

## Scoreboard deltas (round 8)

| Claim | Before | After |
|---|---|---|
| 48="ne"-allophone {94,48} | FLAGGED-UNTESTED (F58) | **REFUTED** (KILLED) |
| 59="est" | provisional | provisional (upheld; residual: 2/2 S4 windows unframed, S5 quarantined) |
| 01="est" | MEDIUM | MEDIUM (confirmed) |
| 84="en" islet | LEAD, pre∈{46,94,82} | **LEAD, re-scoped pre∈{82} GT-anchored ∪ pre∈{66,89} conditional**; «qu'en» @310/@473 withdrawn |
| 84 noun islet | LEAD, pre∈{77,11}, identity NULL | LEAD, identity NULL (stands); @1803 withdrawn from support; «qui le [verb=84-59]» referred |
| 00="pour" | STRONG LEAD (B1 9.14×) | STRONG LEAD (**B1 3.91×, B3 3.19×**) |
| 47="ce" / 96=verb | LEAD / LEAD n_eff=1 | unchanged; **WO-6 second-window criterion RETIRED** |
| {93,8}="l'" | (93="l'" rate-KILLED) | **LEAD (new, unconditioned homophones)** |
| 62="on" / 62="il" | fenced STRONG LEAD / open | fenced STRONG LEAD (+2 non-ear legs) / **DISFAVORED-STRONG** |
| 06="ent"-iff-pre=82 | — | **LEAD (new, conditioned; condition frozen)** |
| 77="gouv"/78="er" | LEAD n_eff=1 | unchanged (7th support null; fork (a2)/(c) unresolved, lean (c)) |
| 16="i" | unconditioned LEAD | unchanged (position alternative NOT SUPPORTED) |
| "Mehemet-Ali" @8 | LEAD | **LEAD-weak** (62-tension + "mêleront" adverses) |
| columns refuge | concretizations dead/weakened | concretizations DEAD; schema LOGICALLY-OPEN-NO-EVIDENCE |
| 67 et/veut fork | SUPPORTED | unchanged (@1248 NEITHER-class window fenced n=1) |

**Amendments:** N46 (shape-STRONG claim irreproducible — traceability flag); F59 (RdM
293× verified — cite as 293× 'Méhémet-Ali', 1841 RdDM 4-tome run, OCR caveat).
**Conventions banked:** future rate bars use Nesselrode v8 (fait 4.6× soft edge
applies symmetrically); never score manual-tiling bearing counts (T7 standing).

## Round-9 work orders

1. **Conditioner successor (WO-4 follow-on):** qui-96-43 ×2 (0-based [341,342,343],
   [1025,1026,1027]) — classify under the 96=verb conditioned reading; the
   «qui le [verb=84-59]» lead (needs 59-as-syllable, unbanked) — pre-register a test
   or keep as lead. 66/89 class readings (the 84 en-extension's dependencies) — confirm
   or the 66-84/89-84 extensions fall. 86's identity (86 que-family dissolves B3).
2. **48 successor (unidentified):** the homophonist's verb/verb-stem residual ("on 48"
   ×6, "48 pas" ×2, flat followers) — a fresh battery, no allophony presumption.
3. **62 resolution:** 62="on" remains the blocker for Mehemet-Ali's promotion and the
   fork's @1248 window; the on/il discrimination needs the N35 independent-cell
   battery (the L_A/L_B legs are ear/first-instrument).
4. **67:** 9 open windows; @1248's NEITHER-class window fenced — resolution waits on
   neighbor values (00/46 both banked, so a new non-{et,veut} arm or a fork re-scope
   is round-9 business; needs its own ≥2-leg bar per WO-7).
5. **Smith (side-homophonic-rebuild):** objective-repair round 2 continues; main-fleet
   search scope stays zero until C1 passes on the gapped family.
6. **77/78:** independent-support hunt continues (8th attempt); 06="ent"-iff-pre=82
   falsifier watch: any 82-06 window in a verbal frame kills the islet.
7. **No re-litigation:** 93-alone rate-kill, 48="ne" kill, refuge concretizations, and
   the retired WO-6 criterion are closed. H5/H6-style adverses and the n≥3 rule stay
   the standing instruments.
