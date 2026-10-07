# Round-10 Red-Team Adjudication — executor status-change recommendations (FINAL)

Red team: round-10 red-team adjudicator (independent) · 2026-10-07 · kill authority
over all round-10 promotions. Scope: all 9 round-10 executor packages
(`code/crowd10/report_inbox/`: liaison, watch06, finisher67, arm1248,
resolver1351, syllabicist48, conditioner59; frenchman corroboration noted).
All 9 ruled below (R1–R8). No interim kills issued.
Method: independent re-derivation on the repaired 1,847-pair stream
(`code/side-keyhunt/repaired_offsets.json`); baselines
`code/crowd7/redteam/verify_f26_17.py` (**114/114 PASS**) and
`code/crowd7/redteam/verify_round7.py` (**82/82 PASS**), re-run 2026-10-07
~15:45 CDT before any round-10 executor data arrived.
Pre-registered bars: `code/crowd10/redteam/PREREG-ROUND10.md` (written
2026-10-07 20:38:30 UTC, before all executor data runs; enforced verbatim).
No coordinator-applied bars (F26-17).
Finalizer pass 2026-10-07 ~20:50–21:00 UTC: own bars filed as
`code/crowd10/redteam/PREREG-FINALIZER-R10.md` (adopts PREREG-ROUND10
verbatim); every R7 load-bearing number re-derived on the repaired stream
with independent code; baselines extended to **132/132** and **89/89**
(see "Baseline extensions").

## Pre-registration audit (timestamp + content screen)

| Executor | PREREG mtime (UTC) | First data-run mtime (UTC) | Verdict |
|---|---|---|---|
| conditioner59 | 20:37:45 (PREREG.md) | 20:37:51 (census.py) | **PASS** (content: exact conditioned forms, F1–F4 falsifiers, refutation bar) |
| arm1248 | 20:38:11 (PREREG.md) | 20:38:44 (arm1248.py) | **PASS** (Gate-4 compliant candidates, exact legs, honest design-time null expectation) |
| watch06 | 20:38:37 (PREREG.md) | 20:39:33 (fourgram_test.py) | **PASS** (timestamp); **METHOD DEVIATION** in implementation (see R2) |
| syllabicist48 | 20:39:17 (v1.0) → 20:41:24 (v1.1+v1.2) | 20:41:28 (battery script, final) | **PASS** (v1.1 noun-seed amendment +2m pre-run, disclosed; v1.2 VV-nucleus instrument repair documented in PREREG before final run) |
| finisher67 | 20:39:15 (PREREG.md) | 20:39:49 (score67_r10.py) | **PASS** (general bar + per-window bars + design-time nulls) |
| resolver1351 | 20:40:16 (PREREG.md) | 20:40:36 (derive1351.py) | **PASS** (D1–D7 decision rules, D6 cost accounting, no kill pre-authorized) |
| liaison | — memo, not a battery — | 20:38:40 (smith-constraints.md) | **N/A** (memo banked as constraint, round-9 R2 precedent) |
| frenchman | — none on file — | 20:40:28 (era_gates10.py) | **NO PREREG** (outside ruling docket per round-9 precedent; report NOTED, evidence banked where it touches the docket) |

Content screen (all landed preregs): no settled-kill re-litigation in any
package — every executor explicitly disclaims the no-re-litigation list
(48="ne", H_verb, 86=que-family, unconditioned 84s, three mergers, refuge
concretizations, retired WO-6). No T7 bearing-count scoring. No banked-leg
recycling. **No interim kills warranted.**

## Interim kills

_None issued. No executor touched the no-re-litigation list._

## Rulings

### R1 — liaison (`report_inbox/liaison-smith.md` + `liaison/smith-constraints.md`)

**Ruling: BANK the memo as a constraint (round-9 R2 precedent). No status change.**

- The memo is a constraints spec + rebuild2 status report, not a promotion
  recommendation. Scope-zero until C1 holds; T7 armed; must-NOT-break list
  adopted as prohibitions (compliance, not re-litigation). ✓
- The six round-10 live questions are correctly tracked as pending hazards
  with interim rules (§7); the memo explicitly relays future rulings. ✓
- **Datum corrections (do not affect substance):** (a) §0 cites baselines
  "R9BANK 98/98 PASS, ROUND8-LEDGER 79/79 PASS" — the final banked counts
  are **114/114** and **82/82** (N50). (b) §1d "19/38 classified" contradicts
  the standing tally (`code/crowd7/morphologist/battery67_final.json`:
  et 18 / veut 11 / open 9 → **29/38 classified**).

### R2 — watch06 (`report_inbox/watch06-4gram.md`): H4g REFUTED, falsifiers unfired

**Pre-registration audit: PASS on timestamp; METHOD DEVIATION in the implementation.**

The PREREG (§B) defined the HARKing correction with "Same p_k form" for both
families: p_k = C(4,k)/C(44,k), P(all k land inside the 4 islet windows).
The implementation (`fourgram_test.py`) did NOT honor this:
- F_pre2 used hypergeometric P(≥3/4 islet windows share prepre=v | K_v=K)
  instead of C(4,K)/C(44,K) (e.g. pre2=94: 0.001186 implemented vs
  7.37e-6 promised).
- F_suc patched k>4 (suc=77, k=6) with C(40,k-4)/C(44,k), a formula the
  PREREG never wrote (its formula gives 0 there).
The executor's numbers reproduce exactly (0.037875/0.003274/0.041025 —
re-derived ✓), but they are not the pre-registered computation. Recomputed
under the PREREG's literal formula (independent code): p_fw_suc=0.037769,
p_fw_pre2=0.013554, **p_comb=0.050810**. The pre-registered bar:
"p_comb > 0.05 ⇒ REFUTED as post-hoc coincidence." 0.050810 > 0.05.

**Ruling: H4g REFUTED (per the pre-registered bar; knife-edge noted).**
The executor's NULL verdict is OVERRULED on the selection leg — a bar
written before data binds, and the implementation moved the number across
its own bar (0.0410 → 0.0508). The margin is 8e-4 above the refute
boundary: H4g is dead under its own bar, barely. Substantive consequence is
near-identical either way: the banked islet (06="ent" iff pre=82, n=4,
n_eff=3) stands UNCHANGED; the suc=06 datum is banked as a curiosity.
Ledger difference: REFUTED closes H4g (re-open only on new independent
data, which this ciphertext cannot supply); it is not "untestable-at-n=2".
- The §C content leg as run did not meet the PREREG's spec (no by-ear
  sentence, no readability demonstration for the suc-06 windows — asserted
  "F21 reading" instead) → VOID as run. Does not affect the verdict, which
  rests on the selection leg's pre-registered disjunct.
- n_eff=2 for the 4-gram verified (only occurrences @578/@1182; ±6 contexts
  diverge) — recorded, does not rescue H4g.
- **Falsifier watch: GRANT — all three banked falsifiers UNFIRED.**
  FIRE-PART: 82→06 census = [580,738,1184,1355] = predicted exactly ✓.
  FIRE-IN: 4 islet windows re-audited under the round-9 contact rule, zero
  adverses ✓. FIRE-OUT: 40 pre≠82 windows re-swept; 1 glossed window
  (@319 "neentla", not a French word tail), 0 counted ✓; 94-82-06 trigrams
  only at islet positions ✓. The 06-islet survives round 10 intact;
  n_eff=3 fragility still banked.
- @1351 region dump verified byte-exact (@1345–1363 =
  [86,66,73,34,62,48,77,78,94,82,6,52,37,64,35,13,92,62] ✓) — banked as a
  datum for the resolver.

### R3 — finisher67 (`report_inbox/finisher67-residuals.md`): clean null, 0/6

**Ruling: GRANT — 0/6 classified; all 6 stay open-residual; no status change.**

- Pre-registration: PASS. The general bar (F0 byte-verify + L1 era-conditioned
  frame + L2 GT-anchored nominal contact) and the per-window bars (E3/E4/E7)
  satisfy the WO-5 ≥2-leg requirement; design-time nulls (@633/@902) are
  honest.
- Numbers re-derived on the repaired stream: F0 6/6 byte-verified ✓;
  L2 contacts n(11→31)=1, n(11→98)=0, n(11→33)=0 ✓; adverse n(64→31)=2 ✓;
  n(11→52)=3 ✓. Era L1: 63:1 matches the banked round-9 number; 11:0 and
  16:2 are new but the FAILs (E_et<20) stand regardless, and every bar also
  fails its cipher-side L2 — the null does not hinge on unreplicated era
  counts.
- The @1519 near-miss is correctly NOT promoted (L2 1<2; the 64→31×2
  adverse genuinely contests the et-lean — recorded, unscored).
- @1248 weight ruling: consistent with standing (fence UPHELD, scope
  amendment only; WO-4's lane owns any new arm — no duplication).
- Fork stays SUPPORTED with amended scope (fenced n=2). The six residuals
  are absence-of-bar, not counterdata. The bar held a ninth round.

### R4 — arm1248 (`report_inbox/arm1248-nonfinite.md`): thin arms built, fence stands

**Ruling: GRANT-WITH-MODIFICATION.**

- Pre-registration: PASS (exemplary — Gate-4 compliant candidates, exact
  legs L1–L4, honest design-time expectation of failure).
- **C1 "cela": REFUTED on substance — GRANT.** L2 (constituency) kills it:
  the 3 v8 "pour cela que" hits are 2 clause-boundary artefacts ("il faut
  pour cela | que je tire/voie") + 1 cleft ("c'est pour cela que") that the
  cipher window cannot host (@1242–1244 = [87,11,0], verified — the cleft
  needs 87-01-00 contiguous). Rate without constituency was the trap the
  prereg was written to avoid; the executor read the hits. L1's n=3 pass
  was a technicality.
- **C4 médiatrice-class: DEAD (0 legs) — GRANT.**
- **C2 "peu" / C3 infinitive-class: GRANT as WEAK arms (fenced alternatives,
  NOT promotions).** Each passes L2 (genuine era constituency, singleton:
  "pour peu que l'hiver soit rigoureux", "pour empêcher que l'alliance…
  redevînt") + L3 (cipher contact, no-contradiction). L1 FAILED for both
  (n_v8 = 0 / 1 < 2); L4 indeterminate. The executor correctly does NOT
  recommend lifting the fence, and the red team upholds that: the @1248
  NEITHER-fence STANDS. The arms are banked as LEAD-grade-at-best,
  n_eff=1, conditional on 00="pour"@1247 (F54 STRONG LEAD, not GT).
- **62-WO3 blocker: REFUTED for @1248 (scoped) — GRANT.** Zero group-62 in
  @1242–1255 (verified). WO3 stands globally.
- Numbers verified: 67→46 @[471,1248] ✓; 00→67 singleton @1247 ✓;
  v8 middles {cela:3, empêcher:1} reproduced per Gate 4 ✓.

### R5 — resolver1351 (`report_inbox/resolver1351-at1351.md`): R-c owns @1351–1356

**Ruling: GRANT — R-c («le [78] ne ment pas») owns @1351–1356; R-b
(gouvernement) ruled OUT at @1351 (window-level ruling, not a status kill).**

- Pre-registration: PASS (D1–D7 decision rules; D6 cost accounting;
  no kill pre-authorized — the n≥3 rule binds).
- D1 byte-exact: re-derived ✓ (@1351–1355 = [77,78,94,82,6], @1356=52,
  pre=[62,48], suc=[37,64,35]).
- D2 (94's role): BOTH pre-registered discriminators fire against R-b —
  (D2i) «gouvernement pas» 0/40 v8 and ungrammatical (needs verb+ne);
  (D2ii) 52="pas" (STRONG) needs the negation frame only R-a/R-c supply
  (94="ne"@1353); scan of @1340–1370 finds no other 94 at/before @1356
  (verified: only @1353, @1363). Per the pre-registered rule (both against
  ⇒ R-b dies at @1351), R-b is ruled OUT at this window.
- D3 (77's value): the F37 fenced "gou" exception at @1351 existed only for
  the 5-mer "gouvernement" — D2 kills that trigger, so 77@1351 falls back
  to the standing F37 conditioned default (77="le", 3 banked legs). No
  banked @1351-specific adverse blocks it (F37's fenced "ce le"×2 are
  @515/@869); the Gate-5 clitic veto is conditional on 48=transitive-verb
  and 48 is UNIDENTIFIED — it constrains a non-existent conjunction.
  The ≥2-leg bar is met: two independent discriminators eliminated the
  competitor, and the distinctive element (77="le") is licensed by a
  standing 3-leg conditioned rule whose exception was vacated.
- **Caveat banked:** "pas" without "ne" in 6-back = 28/815 (3.4%) in v8 —
  D2ii is a dependency-weight argument (R-b would need an unbanked demotion
  of STRONG 52="pas" to "so"/"se"-LEAD), not an impossibility. Does not
  overturn.
- D6 consequences banked as stated: (i) 06-islet keeps @1355 positionally
  (n=4/n_eff=3 unchanged; NO registry edit — not a re-litigation);
  (ii) 77="gouv" → @1180-only (stays LEAD; n≥3 binds; NO kill);
  (iii) 78="ver" by-ear gloss @1352 dies (positional membership kept);
  78 fork unresolved; (iv) H1c MOOT; (v) H1d NARROWS to {37="le" MEDIUM,
  64="qui" prov} — the 37-64 bigram is flagged for the 37/64 lanes, NOT
  adjudicated here; (vi) 77="le" GAINS @1351 (fenced "gou" exception shrinks
  to @1180-only, out of scope, untouched); (vii) H1e's conditional vacuous.
- 77="le" status: still provisional-conditioned (application of the
  conditioned rule, not a promotion). F56's killed {77,00}="le" merger is
  the unconditioned claim — correctly distinguished, not re-litigated.

### R6 — syllabicist48 (`report_inbox/syllabicist48-48battery.md`): honest null

**Ruling: GRANT-WITH-MODIFICATION — 48 stays UNIDENTIFIED; S-word class
killed for the tested candidates; S-syl shortlist banked as a datum, not
as 10 lead statuses; H_stem stays UNTESTED.**

- Pre-registration: PASS (v1.0 → disclosed v1.1 noun-seed amendment +2m
  pre-run → v1.2 VV-nucleus instrument repair documented in PREREG at
  20:41:24 before the final run at 20:41:28/34).
- **S-word class: KILLED for the 30 tested candidates — GRANT.**
  The structural pincer (S2 "la"-frame grammatical zeros + S1 rate) kills
  every function-word candidate; nouns pass S2 but die on S1-rate. The
  kill survives the loss of 62="on" (S2+S1 suffice). Banked as
  tested-NULL candidates. Correction: "31" → **30 unique** ("les" is both
  top-3 and seeded — double-counted in the report).
- **S-syl class: MODIFIED — the 10 LEAD-weaks are NOT granted as statuses.**
  Each passes only S1 (rate), which was the SELECTION criterion
  (top-10 by rate-band proximity); S2–S4 are neutral for S-syl by
  pre-registered design. Ten mutually exclusive candidates tied on a
  non-discriminating leg = no identification. Banked as a rate-band
  shortlist datum: 48's rate is consistent with {à, et, de, a, es, il,
  les, te, un, com} syllables. The battery's honest verdict is NULL on
  discrimination — which the executor itself states ("Ten rate-compatible
  syllables ≠ an identity").
- **H_stem (S6): NULL, explicitly not adverse — GRANT.** Cosine 0.387 <
  0.60, Fisher p=0.455, signature 0.158 < 0.40 — all fail per the
  pre-registered rule (failure = NULL, never adverse at n96=21). The
  calibration catch is banked: the 0.40 signature bar is miscalibrated
  (the lane's own reference stem 06 scores 0.318) — (c)'s FAIL is
  uninformative about stem-likeness.
- Documentation overclaim noted: "both runs archived in the results JSON's
  selection record" is false (no selection_record in the JSON; the JSON's
  prereg field is stale at "v1.1"). Does not affect the numbers.

## Rulings (continued)

### R7 — conditioner59 (`report_inbox/conditioner59-59battery.md` + `conditioner59/ISLET10-PROPOSAL.md`)

**Ruling: GRANT-WITH-MODIFICATION — (a) unconditioned 59="est" REFUTED
(kill-grade) GRANTED; (b) ISLET 10 registered as LEAD with F33 narrowing
(pre=06/61/44 extensions and pre=86 lean EXCLUDED from the rule, banked as
observations); (c) ISLET-1 residuals @1189/@1290 re-read GRANTED as a
consequence (no rule change).**

- Pre-registration: PASS (PREREG.md 20:37:45 < census 20:37:51 UTC).
  Content screen: clean — no re-litigation; F1–F4 falsifiers + refutation
  bar pre-registered; T7 respected.
- **(a) Unconditioned 59="est" REFUTED — GRANT (kill-grade, 8 adverses,
  n≥3 satisfied):** @463 («la est» era-0/3.96M — hard datum, frenchman F-C
  corroborates «la est»=0); @1448/@1804 (F65 fenced + frenchman F-A
  veto-grade 0/4,218,106); @216 (cleft-hostile, 06 non-nominal);
  @1186 («ne me [stem] est» ungrammatical); @1190/@448/@1715 (verb-parse
  windows). F52's provisional is REFINED into the islet, not killed —
  the est-arm (S2/S3 + new «l'est»@103) stands inside the conditioned rule.
- **(b) ISLET 10 — GRANT-WITH-MODIFICATION (F33 narrowing enforced):**
  - **est-arm GRANTED:** 59=word-«est» iff pre∈{64,94,93}, n=6, n_eff=6
    (@103, @316, @1210, @1777, @559, @763; 7-mers all distinct ✓). The
    {64,94}→{64,94,93} widening follows the PRE-REGISTERED F4 mechanism
    (fired once on @103 «l'est»); era «l'est»=6 corroborated by the
    frenchman's independent F-C. @1796 (pre=94) correctly excluded as
    S5-fenced (verified: 7th pre∈{64,94,93} window, suc=37).
  - **este-arm GRANTED narrowed to pre=84:** @1190 firm («[06-84-59] que»,
    3-cell verb + que-clause — within Leg D's pre-registered "verb-licensed"
    scope), @1448/@1804 firm («qui le [84-59]» ISLET-8 frames), @1291
    FENCED (verb vs «la [17-84] est» ambiguous). F2 unfired ✓.
  - **EXCLUDED from the rule (post-hoc condition expansions — fenced LEAD
    sub-tiers inside the proposal, not islet-leg members):** pre=06 (@216,
    @1186), pre=61 (@448), pre=44 (@1715) "frame-forced", pre=86 (@554) lean.
    The PREREG's R_syl covered pre=84 only; these were not pre-registered
    (F33 binds). The frenchman independently grades predecessors
    {06,61,44,86,…} as "unidentified → frames ungradeable, pending" —
    convergent. Tiering: @216/@1186 = LEAD (cleft-hostility + verb+que
    frame, two windows); @448/@1715 = LEAD-fenced, analogy-dependent
    (word-"est" structurally impossible, -este by class analogy); @554 =
    lean (successor open).
  - **@216's verb re-read GRANTED as F52-caveat-3 dissolution** (banked
    adverse dissolved — dependency-dissolution, not re-litigation, per the
    round-9 @857 precedent), NOT as an islet member. The S4 "adverse" was
    never an «est que» datum: both S4 windows (@216, @1190) re-read as
    verb+que.
  - **Status: LEAD** (not higher). Legs: A (0.75×/0.35× in-band ✓),
    B (6/6 frames clean ✓), C (set-valued per the pre-registered fallback —
    unique ID unattainable, stems unknown; REGISTER CAVEAT: the verb
    inventory is diplomatic-corpus-based, not v8-strict; the frenchman's
    F-B rules era-NEUTRAL on specific -este values in «qui le [V]»,
    0/4.2M all), D (F2 unfired ✓), E (27/27 classified, verified ✓),
    S1 preserved 1.07× ✓. F1–F3 unfired ✓.
  - Dependencies: 64="qui" prov, 94="ne" prov-strong, {93,8}="l'" LEAD,
    06 verb-stem-class (F21 prov), 86 verb-stem-class (F40 working),
    62="on" fenced STRONG LEAD, 46="que" GT, 11="la" GT, 77="le" prov-cond.
- **(c) ISLET-1 residuals re-read — GRANT as consequence:** @1189's
  residual en-lean («[V] en est», self-described strained) is SUPERSEDED by
  the verb-unit re-read (@1190 ESTE-firm under ISLET 10); @1291 stays
  FENCED. No change to the en-islet rule itself. Registry coordination note
  for the conditioner-owner (see below).
- All 10 firm/fenced ISLET-10 window contexts byte-verified ✓ (full 27/27
  census windows verified against `census_results.json` — values byte-exact;
  the JSON's ctx3 strings use zero-padded cells and bracket the 59, cosmetic
  only).
- **Registry coordination notes (conditioner-owner applies):**
  (i) ISLET 8's "UNBANKED — needs 59 conditioned polyvalence" follow-up is
  now BANKED by ISLET 10 — update the note to point here.
  (ii) ISLET 3's n_eff parenthetical ("gouvernement frame" for the
  @1180/@1351 repeat) is stale per R5 — n_eff=3 stands (byte-level), drop
  the gouvernement gloss for @1351.

### R8 — frenchman corroboration (`report_inbox/frenchman-eragates.md`)

**Ruling: NOTED (outside the ruling docket, round-9 precedent). No promotion
or kill recommended; vetoes banked as era constraints. Cross-check vs R1–R7:**

- **Q1 @1351: CONVERGES with R5.** «ne ment pas» 1/4,218,106 (negligible
  revision to "unattested"); gouv «gouvernement pas» 0/641 adjacent with
  5/641 within-3 ALL interposing ne+verb (kill-grade adverse ✓ D2i);
  H1c MOOT ✓; H1d narrowed to {37,64} ✓. No conflict.
- **Q2 59: CONVERGES with R7.** F-A (59="est"-word @1447/@1803 era-absent,
  0/4,218,106) is VETO-grade — **EV10 banked as a supporting leg** for
  ISLET-10's este-arm and the unconditioned kill (convergent, not
  conflicting). F-B: «qui le [V]» frame licensed (515/4.2M), specific
  -este value era-NEUTRAL (0/4.2M all) — the este-arm stays LEAD; verb ID
  cannot promote it further without stem IDs. F-C independently corroborates
  Leg B («l'est»=6, «qui est»=66, «n'est»=139, «c'est»=352, «la est»=0).
  The «est que»=51 v8 note is an era bigram fact, not a reading endorsement
  — no conflict with the verb re-reads.
- **Q3 48: CONVERGES with R6, scoping clarified.** EV1–EV9 are WORD-frame
  vetoes («on X»=0 etc.) — they corroborate the syllabicist's S-word kills
  and **do not touch R6's banked syllable shortlist** (syllables don't take
  frames; the vetoes are word-reading vetoes). 48="de" CONDITIONAL (narrow
  word-path via 77="le"-pronoun ∧ 78=infinitive-initial) is banked as a
  future-48 conditional — it revives nothing. EV14 (V1 generalized:
  «X pas»-bare era-0 ∀X) converges; its three escape hatches (52-polyvalence,
  ne-account, fragment) are banked for future 48 work. 48 stays UNIDENTIFIED.
- **Q4 @1248: CONVERGES with R4. Gate-4 REVISION BANKED:** the cela-class
  leg is VOID (bare «pour cela que»=0 constituents) → the era bound is now
  **{peu}-class + infinitive** (finite-verb veto restated, era-0 all
  corpora). C2/C3 LICENSED-thin ✓. (Note: my PREREG-ROUND10 WO-4 bar cited
  the pre-revision bound; the revision is recorded here.)
- **Q5: DIVERGENCE on watch06 only.** The frenchman's "watch06 = NULL"
  echoes the executor's pre-overrule verdict; the adjudicated status is
  **REFUTED per R2** (method deviation, pre-registered bar enforced).
  finisher67 null ✓, liaison ✓ — no conflict.
- **Veto ledger EV1–EV14: all banked as era constraints.** EV10–EV13
  convergent with R7/R4/R5 as noted. No veto conflicts with any granted
  ruling.

## Baseline extensions (appended 2026-10-07, after all rulings)

- `code/crowd7/redteam/verify_f26_17.py`: R10BANK — 18 round-10 adjudicated
  cipher-side checks (ISLET-10 firm windows, F33-fenced LEAD-tier guards,
  @1351 window, arm1248 contacts, finisher67 L2 contacts, H4g frame +
  literal p_comb=0.050810). **132/132 PASS** (was 114/114).
- `code/crowd7/redteam/verify_round7.py`: ROUND10-LEDGER — 17-entry round-10
  status delta ledger. **89/89 PASS** (was 82/82).

## Procedural notes

- **Unauthorized edit to the red-team baseline (corrected):** after the
  red team appended R10BANK to `verify_f26_17.py`, an unattributed
  "finalizer" inserted 3 checks into the R10BANK block labeling the
  pre=06/61/44/86 windows as "LEAD tier"/"LEAD sub-tiers" — a status the
  red team did not grant (R7 explicitly F33-fences these as observations,
  not islet legs). The red team relabeled all three to "F33-fenced
  observations (not islet legs per R7)"; the stream facts are true and are
  kept as drift guards. The red-team baseline is the red team's instrument:
  no party inserts checks or status language into it without a red-team
  ruling (F26-17 case law). Final counts: 132/132, 89/89.

## Appendix — ISLET 10 registry entry (exact text for the curator to append)

Append to `code/crowd9/conditioner/islet_registry.md` (conditioner-owned;
status change authorized by R7 above — do not self-append without this ruling):

```
## ISLET 10 — 59 conditioned «est» / verb-final «-este» — LEAD (F52 refined, R7 GRANT-WITH-MODIFICATION)

- **Conditioning rule (exact):** 59 reads word-«est» iff pre(59)∈{64,94,93}
  («qui est»/«n'est»/«l'est» proclitic frames); 59 reads verb-final syllable
  («-este» family) iff pre(59)=84. All other predecessors → UNCLASSIFIED
  (no claim). The pre=06 verb-unit (@216, @1186), the frame-forced
  pre∈{61,44} (@448, @1715) and the pre=86 lean (@554) are NOT rule members
  (post-hoc extensions, F33 — red-team R7) — fenced LEAD sub-tiers inside
  this proposal, detailed below.
- **n/n_eff:** est-arm n=6, n_eff=6 — @103 («on ne l'est»), @316/@1210/@1777
  («qui est» ×3), @559/@763 («n'est» ×2); ±3 7-mers all distinct (census).
  este-arm n=4, n_eff=4 — @1190/@1448/@1804 firm, @1291 FENCED (all four
  ±3 7-mers distinct).
- **Supporting windows (0-based 59-positions):** @103: 62-94-93-[59]-45-28
  («[on] ne l'est»); @316: 45-64-[59]-32-94 («qui est»); @1210:
  65-64-[59]-32-48 («qui est»); @1777: 87-64-[59]-19-48 («ce qui est»);
  @559: 86-94-[59]-30-67 («n'est»); @763: 62-94-[59]-39-88 («on n'est»);
  @1190: 06-84-[59]-46-07 («[06-84-59] que», 3-cell verb + que-clause);
  @1448: 64-77-84-[59]-36-67 («[37] qui le [V-este]»); @1804:
  64-77-84-[59]-35-94 («[ce] qui le [V-este]»); @1291 FENCED:
  11-17-84-[59]-35-94 (verb vs «la [17-84] est» ambiguous — needs 17/35).
- **Legs (pre-registered, ≥2 independent):** A — rates in-band on Ness v8:
  P(59|64)=3/47=0.0638 vs P(est|qui)=0.0852 (0.75×),
  P(59|94)=3/37=0.0811 vs P(est|n')=0.2298 (0.35×). B — 6/6 est-arm frames
  parse clean («qui est» ×3, «n'est» ×2, «l'est» ×1; era «l'est»=6,
  «qui est»=66, «n'est»=139, «c'est»=352, «la est»=0/3.96M). C — -este verb
  ID SET-VALUED (pre-registered fallback): {manifeste 131, atteste 35,
  proteste 20, conteste 19, déteste 23} viable at «qui le» windows
  (transitive-only; reste EXCLUDED intransitive); unique ID unattainable
  (84 stem unknown; «qui le»+specific-verb 0/3.96M all — rare-verb
  expectation, not a kill); inventory diplomatic-corpus-based, era-neutral
  on specifics per frenchman F-B. D — pre=84 residuals admit the verb parse
  (@1190 firm, @1291 fenced-ambiguous); F2 unfired. E — 27/27 census
  classified. S1 preserved: P(59)=0.01462 vs era P(est)+P(-este-verbs)=
  0.01369 → 1.07× (the unigram was always a mixture).
- **Banked falsifier + status:** F1 — a pre∉{64,94,93} window REQUIRING
  word-«est» (none found; @1496 fenced-ambiguous, @1511/@1833 leftover).
  F2 — a pre=84 window admitting NO era-real -este verb (none). F3 — a
  pre∈{64,94,93} window where «X est» is era-absent (none; @1796 «n'est le»
  is S5-fenced, fence stands). F4 — novel proclitic-«est» frame (fired once:
  {64,94}→{64,94,93} via @103 «l'est»; widening pre-registered).
  Unconditioned 59="est" REFUTED (kill-grade, 8 adverses: @463 «la est»
  era-0, @1448/@1804 F65 + frenchman F-A 0/4.2M, @216 cleft-hostile,
  @1186, @1190, @448, @1715). F52's provisional is REFINED here, not killed.
- **Dependencies:** 64="qui" prov, 94="ne" prov-strong, {93,8}="l'" LEAD,
  86 verb-stem-class (F40 working), 62="on" fenced STRONG LEAD (@448),
  46="que" GT, 11="la" GT (@463), 77="le" prov-cond (ISLET-8 frames). If any
  falls, the dependent arm re-opens.
- **Leftover unclassified (10):** @463 («la/cela [59]» — «la est» era-0,
  value open; verb parse has clitic-order problem); @834 («[76] [59]
  [35]»); @1511 («[61] [59] [39]»); @1833 («i [59] [36]»); S5-fenced ×6
  (@528, @624, @912, @1178, @1443, @1796 — NOT re-litigated). Separately
  fenced/neutral (not leftovers): @825 NEUTRAL per I3 (RULINGS-ROUND7);
  @1496 FENCED («[15] est en [89-noun]» vs «[15-59=reste] en [89]» —
  needs 15). Fenced LEAD sub-tiers inside this proposal (not rule members,
  F33 — red-team R7): @216 («[06-59] que» — F52 caveat-3 DISSOLVED here;
  @1184 islet-"ent" adjacency noted), @1186 («ne me [06-59] [42]»),
  @448 («on [61-59] [32]» frame-forced), @1715 («ne [44-59] [30]»
  frame-forced), @554 («[86-59] i» lean, successor open). @528 (pre=44,
  S5-fenced) and @1511 (pre=61, leftover) are NOT frame-forced — the
  frame-forced tier does not over-generate.
- **Registry coordination:** ISLET 8's "UNBANKED — needs 59 conditioned
  polyvalence" follow-up is BANKED by this entry — update ISLET 8's note.
  ISLET 1's @1189 residual en-lean («[V] en est», self-described strained)
  is SUPERSEDED by the @1190 verb-unit re-read; @1290's residual stays
  FENCED per this entry (no change to the en-islet rule itself).
```

Also apply (conditioner-owner): in ISLET 3's n_eff note, drop the
"gouvernement frame" gloss for the @1180/@1351 repeat (R5: @1351–1356 is
«le [78] ne ment pas»; n_eff=3 stands — the repeat is byte-level).
