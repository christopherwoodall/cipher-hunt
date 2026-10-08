# Round-13 Red-Team Adjudication — executor status-change docket (OPEN)

Red team: round-13 red-team adjudicator (council-round, independent) · 2026-10-07 · kill authority
over all round-13 promotions and status changes. Scope: the 7 council-round executor packages
named in the task brief (islet-auditor, homophone-ab, homophone-cd, segmenter, missing-mass,
carry-classes, carry-rest). **Out of scope:** KE1/KE2 kill experiments — ruled by the red-team
killer agent itself, not by this adjudicator; do not touch.
Standing convention: every executor leaves a report note at `code/crowd13/report_inbox/` per
REPORTING.md; the red team rules ALL status changes before any merge — no claim merges without
its ruling; no coordinator-applied bars (standing F26-17). Round-12 precedent: RULINGS-ROUND12.md
(13 items, closed). Round-11 precedent: three sequential independent adjudicators ruled R1–R7.

## Docket status (2026-10-07 23:59 UTC — CLOSED)

**DOCKET CLOSED — 21 rulings issued; 0 packages pending.**
First shift (23:15–23:35 UTC): R-DRAG (GRANT-WITH-MODIFICATION), R-CD1 (GRANT),
R-CD2 (GRANT-WITH-CONDITION), R-IA1–R-IA7 (all GRANT), R-CC92
(GRANT-WITH-MODIFICATION). Second shift: R-AB1 (GRANT — {33,86} SPLIT),
R-AB2 (GRANT — {48,94} SPLIT), R-CC31 (GRANT — 31=VERBAL CONFIRM),
R-CC33 (GRANT — 33 NULL constrained), R-CR48 (GRANT — 74-class OPEN / H_stem
leg / second-frame negative), R-CR1248 (GRANT-WITH-CONDITION — PC-1 leg /
DP-1 permanent fence), R-CRESTE (GRANT-WITH-CONDITION — atteste FRAME-BEST
LEAD), R-MM1 (GRANT — deficit arithmetic), R-MM2 (GRANT-WITH-MODIFICATION —
priors as priors + digit hunt retired). Battery-numbers audited, recommendations pending: NONE.
Out of scope: KE1/KE2 (red-team killer agent's jurisdiction — not touched);
liaison/smith-constraints.md (BANKED as constraint per round-9/10/11/12
precedent — memo, not verdicts; main-fleet search scope ZERO maintained).
Interim kills: NONE.

**Baseline extensions applied at close:** R13BANK in
`code/crowd7/redteam/verify_f26_17.py` (cipher-side stream checks behind
every round-13 adjudicated fact); ROUND13-LEDGER in
`code/crowd7/redteam/verify_round7.py` (status deltas + drift guards).
Extend, don't rebuild — earlier BANK/LEDGER blocks untouched.

**Baseline state at round-13 close (2026-10-07 24:00 UTC):**
`code/crowd7/redteam/verify_f26_17.py`: **237/237 PASS** (203 pre-round +
34 R13BANK checks). `code/crowd7/redteam/verify_round7.py`: **160/160 PASS**
(133 pre-round + 27 ROUND13-LEDGER checks). Earlier BANK/LEDGER blocks
untouched; both scripts exit 0.

**Citation-convention corrections for first-shift rulings (substance
unaffected):** R-IA2's frame starts are @1444 (37-64-77-84-59-36-67) and
@1800 (87-64-77-84-59-35-94), not @1445/@1801 (those index the 64 cells);
R-IA4's third 96-00 window starts at @960 (96 position), not @961 (the 00
position); R-IA7's @150 indexes the 96 cell (frame start @149). The R13BANK
checks below use the corrected indices.

Expected packages (from the task brief + `code/council/table-reconstruction.md` attack plan):
1. **islet-auditor** (dir `code/crowd13/islet-audit/`, EMPTY at last sweep) — Step 1: compositional
   audit of all 10 islets via the §c battery (lexical-bigram check, residual test, forced-context
   test). Each islet: WORD-RULE / TRUE-POLYVALENCE / KILLED. **This adjudicator re-derives the
   4-part battery numbers (spot-check minimum; full re-derivation for any KILL or registry
   change).** The registry (`code/crowd9/conditioner/islet_registry.md`) is under audit — no
   dissolution enters the registry without a ruling here.
2. **homophone-ab** (dir TBD — NOT YET CREATED at last sweep) — sets {33,86} & {48,94}: frame
   battery, uniformity χ², cycling/runs test. PROMOTE / SPLIT / KILL.
3. **homophone-cd** (PREREG landed 23:04:23 UTC, battery not yet run) — sets {52,59} & {76,78}.
4. **segmenter** — Step 2: word-boundary map from confirmed bigrams; coverage fraction of the
   1,847-pair stream. **Consistency falsifier must be run — coverage alone is not a ruling.**
5. **missing-mass** — Step 4: deficit arithmetic (era rates − observed rates → missing-cell
   counts). **Priors are NOT promotions** — any candidate list presented as stronger than a
   prior gets FENCED.
6. **carry-classes / carry-rest** — LEAD verdicts need ≥2 legs; kills need kill-grade evidence
   (pre-registered bar fired, no escape hatch).
7. **KE1/KE2** — OUT OF SCOPE (red-team killer agent's jurisdiction).

## Standards in force (case law)

- No coordinator-applied bars — I am the bar (F26-17 standing).
- Pre-registration must predate the data: check PREREG mtime vs first data-run mtime; the
  round-12 precedent's 13s margin was clean, loose header rounding is tolerated only when
  mtimes govern and the margin is positive.
- Promotion bar: ≥2 independent checks (STATE.md standing convention). Enforced strictly.
- Nesselrode v8 VOID for phrase queries — any phrase evidence sourced from v8 is REJECTED
  (R12 methodology flag: v8's "ment" tokens are OCR word-splits; token-level zeros void;
  clean 3.87M diplomatic corpus = the phrase instrument).
- French grammaticality claims need corpus backing or an explicit "unattested" mark.
- Settled kills are NEVER re-litigated (STATE.md list; see below).
- Kills need kill-grade evidence: pre-registered bar fired, no escape hatch.

## Interim kills

None issued.

## Pre-registration audit (table filled as PREREGs land)

| Executor | PREREG mtime (UTC) | First data-run mtime (UTC) | Verdict |
|---|---|---|---|
| homophone-cd | 23:04:23 (header "~18:05 CDT" = 18:04:23 CDT — consistent within a minute; mtimes govern) | 23:04:52 (homophone_cd.py; results 23:05:43) | **PASS** — timestamp clean (29s margin); methods licensed (clean-diplo pool verbatim, v8 explicitly VOID for phrases); decision bars name PROMOTE≥2-legs (A+C), SPLIT, KILL; design numbers re-derived ✓ (n52=27, n59=27, n76=21, n78=31; uniformity χ²=1.92, ratio 1.48); ISLET-10 arm citations match registry verbatim. TWO RESERVATIONS recorded: (a) battery premise depends on ISLET-10 arms, which are UNDER AUDIT this round — if the islet auditor dissolves ISLET-10, {52,59} frame premises are VOID and the package must be re-benched on the dissolved wording (flag, not a kill); (b) the "{47,87} positional-allophone pattern" is design-level analogy only — NOT a re-read of the F56 merger kill, carries no status weight. |
| islet-auditor | 23:05:23 (no claimed time in header — clean) | none yet (era.py/stream.py at 23:05:09 are loader apparatus, no results) | **PASS** — timestamp clean; battery form per islet licensed (lexical-bigram / residual / forced-context / homophone-cycling uniformity); verdict codes WORD-RULE / TRUE-POLYVALENCE / KILLED / INCONCLUSIVE / CLASS-RULE; explicit no-re-litigation of the settled list; no coordinator bars. CAUTION recorded: loader scripts predate the PREREG by 14s — apparatus, not a data run (no results produced); the binding check is first-results mtime vs 23:05:23 UTC when the package lands. CROSS-CHECK NOTE: ISLET-9 Part-4 ({33,86} homophone χ²) duplicates homophone-ab's territory — the number is bankable but the {33,86} verdict belongs to homophone-ab; any conflict is reconciled here, not double-adjudicated. |
| homophone-ab | 23:06:24 (no claimed time in header — clean) | 23:06:40 (battery_stats.py; results 23:06:42) | **PASS** — timestamp clean (16s margin); Set A {33,86} bars strict (uniformity re-derive p>0.05 + runs |z|<2 + pre-segregation p>0.05 + ≥2 frame-interchangeability legs for PROMOTE; SPLIT/KILL bars defined); Set B {48,94} PROMOTE correctly PRE-BARRED (48="ne" killed kill-grade F60 — case law applied, not re-litigated); falsifiers banked; drag-not-landed checked and recorded. Stat numbers re-derived ✓ (setA: uniformity χ²=0.8596 p=0.354 matches table claim 0.86/0.35, runs z=-0.291, pre χ²=6.573 p=0.160; setB: uniformity χ²=0.0133 p=0.908, runs z=-0.347, pre p=0.482, suc p=0.509). NOTE for the verdict: setB shows NO predecessor divergence (p=0.48) despite 48≠"ne" being settled — no-divergence does not imply homophony (F60 lesson); the frame-substitution battery (V1–V4) and verdicts are still pending. |
| carry-classes | 23:06:03 (header: "written BEFORE any round-13 decision computation" — clean) | 23:06:28 (r13_31.py; r13_92.py 23:06:39; r13_33.py 23:08:18) | **PASS (with one reservation)** — timestamp clean (25s margin); scope conditions disclosed (Fork-W whole-word scope; ID capped by the unresolved fork — honest); instrument gates byte-exact (N=1847, @1519/@902 windows, |C|=461→453, top-10 drift check); new phrase queries on pool∖v8 (disjoint from v8 AND round-12's v8 tail arm — strictly stronger than F77); T2 on pool∖v8 with 21="ce" banked datum gives a genuinely independent second leg (R⊥T2 by disjoint corpora); R13-31 is verification re-derivation (no status change). **RESERVATION: R13-92's T_683 uses n_v8("pour X W qui") — a phrase query on v8, which the standing F77 rule VOIDS** ("no phrase query rests on v8 OCR text"; R12 case law: v8 phrase-zeros are VOID as French measurements). The v8 arm must be re-run on pool∖v8 or dropped before T_683 banks anything; the @683 NOUN-islet corroboration cannot rest on it. |
| segmenter | not yet landed | — | PENDING |
| missing-mass | 23:05:33 (header undated-claim — clean) | none yet | **PASS (with reservations)** — timestamp clean; methods fixed (lane `build_syll_model.py::syllabify`, cosine ranking recomputed from stream, FLAG/STRONG thresholds numeric, digit-hunt T1–T4 with T4 falsifier); explicitly PRIORS-only, no value assignments ("priors are NOT promotions" honored). TWO RESERVATIONS: (a) **v8 in the French rate pool** — nesselrode v7/v8/v9/v10 listed; v8's OCR word-splits distort syllable UNIGRAM rates too, not just phrases. Require a with/without-v8 sensitivity run before any deficit number is banked, or explicit exclusion; (b) conditioned islets (84="en"/06="ent"/00="le") are assumed WORD-rules per the reconstructor §c in the observed-rate sums — this PRE-JUDGES the islet audit. If the auditor rules TRUE-POLYVALENCE on any of them, the deficit arithmetic must be re-benched; the adjudicator re-derives either way. |
| carry-classes | not yet landed | — | PENDING |
| carry-rest | 23:05:42 (header "~18:10 CDT" — file is 18:05:42 CDT, ~4min EARLIER than claimed; loose rounding in the conservative direction, mtimes govern, no amendment) | none yet | **PASS** — timestamp clean; standing inputs frozen and named (GT + provisional + ISLET 3/10 arms + 48 fences + settled kills explicitly NOT re-litigated); v8 VOID acknowledged; per-leg bars numeric (A1 ≥70% dominant-class, A2 kill-on-banked-contradiction, B2 ≥5% license share, E-trans n("le",V3sg)≥1, tie-break ≥2 legs). TWO RESERVATIONS: (a) [FR-JUDGMENT] legs (A1 classification, E-trans transitivity) are judgment-backed — the package must mark them as such explicitly; corpus counts alone do not license French grammaticality claims (case law); (b) @863 islet promotion would collide with round-12's POINTER-ONLY rating — A1+A2 agreement is the required ≥2-leg bar, no upgrade on single legs; D's PC-1/DP-1 recommendations come to THIS docket (not self-granted). |
| systematic-drag | plan 22:52 (pre-registered bar §3.1) | 22:57+ (all code/data after plan) | **PASS** — plan predates all code/data; hit bar (§2.3) and null bar (`h_real > max(h_s)`, §3.1) both pre-registered; positive control exact; decoy null 0/122. Ruled as R-DRAG (GRANT-WITH-MODIFICATION). |

## Battery-number audits (re-derived from the repaired stream; verdicts pending)

### homophone-cd — AUDITED-PASS (numbers only; verdicts pending)
All battery numbers re-derive byte-exactly: {52,59} uniformity χ²=0.0 p=1.0 ✓,
runs r=23 mu=28.00 z=-1.374 ✓, pre-homogeneity χ²=5.676 p=0.4604 df=6 ✓;
{76,78} uniformity χ²=1.923 p=0.166 ✓, runs r=31 mu=26.04 z=1.444 ✓,
pre-homogeneity χ²=6.179 p=0.4034 df=6 ✓; n52_pre84=0 / n59_pre84=4 ✓;
76→94=0 / 78→94=2 ✓; pre94_76=[652,1577] / pre94_78=[] ✓; pre77_76 (3) /
pre77_78 (7) ✓. Corpus verified: clean-diplo pool verbatim from
estetie.py's FRENCH_CLEAN (13 files, N=3,618,487 tokens), v8 excluded from
phrases as promised; lane tokenizer verbatim. Era frame counts on the clean
pool: qui_est=904, n_est=3354, ne_l_est=43, qui_le_est=0, ce_qui_le_est=0.
METHOD NOTE for the eventual verdict: the {76,78} pre-homogeneity categories
drop pre=94 (2 for 76, 0 for 78) while the {52,59} set includes pre=84 (0 vs 4)
but drops pre=93 (2 vs 1) — category choice is a degree of freedom; the
no-divergence conclusions (p=0.46 / p=0.40) are far from the p<0.05 bar either
way. The PROMOTE/SPLIT/KILL recommendations have NOT landed (no verdict
fields, no report note at lane report_inbox/). **Status: numbers banked as
audited data; verdicts PENDING.**

### homophone-ab — AUDITED-PASS (stats only; frame batteries + verdicts pending)
Uniformity/runs re-derive exactly (setA: χ²=0.8596, z=-0.291; setB:
χ²=0.0133, z=-0.347). The frame-interchangeability batteries (setA L1–L3;
setB V1–V4) and the PROMOTE/SPLIT/KILL verdicts have NOT landed.
**Status: stats banked as audited data; verdicts PENDING.**

### segmenter — GRANT-WITH-MODIFICATION (no PREREG; data granted, map fenced)
Coverage and census re-derive byte-exactly: 32 segments, 72/1847 pairs =
3.90% coverage (0 pattern mismatches); la-première n=2 @754/@1034 ✓;
m'en (82-84) n=1 @166 ✓; ment (82-06) n=4 @579/@737/@1183/@1354 ✓;
par-le (96-00) n=3 @47/@465/@960 ✓; en-ce (24-87) n=10 ✓;
c'est (87-01) n=2 @344/@1028 ✓; par-ce-que (96-87-46) n=3 @224/@952/@1526 ✓;
cela (87-11) n=7 ✓. The consistency falsifier WAS run (C1–C6 in segment.py):
C4 47-01 analog @194, C5 94-87 variant @1169, C2 cross-tier overlaps = 0.
**Modification:** (a) no PREREG exists for this package — the word list mixes
banked words (A+/A tiers) with proposals ("en ce" tier B depends on the
reconstructor's §c reading, which the islet auditor has not yet ruled on);
the map is therefore granted as DATA (census + coverage + tier labels), not
as confirmed word boundaries. (b) Three same-tier overlaps are recorded but
UNRESOLVED: "en ce" × "cela" share pairs @74/@163/@830 (the 24-87-11
trigram). C2's tier-rank equality (B=B*=2) let them pass as non-conflicts, but
a word-boundary map cannot contain overlapping segments — the 24-87-11
trigram needs one resolution ("en cela" unit, or drop one reading) before the
map is usable as a solver-side deliverable. **Missing leg (sent back): the
overlap resolution + islet-audit rulings on the compositional words. The
coverage number (3.90%) and per-word census bank as audited data.**

### segmenter — GRANT (map as tiered constraint set; was GRANT-WITH-MODIFICATION)

Coverage and census re-derive byte-exactly: 32 segments, 72/1847 pairs =
3.90% coverage (0 pattern mismatches); la-première n=2 @754/@1034 ✓;
m'en (82-84) n=1 @166 ✓; ment (82-06) n=4 @579/@737/@1183/@1354 ✓;
par-le (96-00) n=3 @47/@465/@960 ✓; en-ce (24-87) n=10 ✓;
c'est (87-01) n=2 @344/@1028 ✓; par-ce-que (96-87-46) n=3 @224/@952/@1526 ✓;
cela (87-11) n=7 ✓. The consistency falsifier WAS run (C1–C6).
**Update 23:25 UTC:** the missing leg has landed — the 3 same-tier overlaps
("en ce" × "cela" @74/@163/@830, the 24-87-11 trigram) are now resolved with
per-segment `status`: the 3 contested "en ce" segments are `superseded`
(withdrawn as constraints, kept for audit, conflict note records the "en
cela" reading with period-corpus backing); 2 "ment" segments (@579/@1183)
are `suspect` (word-edge soft — bare "ne ment [06]" without "pas"); 8 are
`live*` (boundary stands, adjacency tension noted); 19 `live`. The
memo-to-smith.md handoff gives the solver tiered consumption rules (A+/A
hard, B/B* strong-soft, C bonus-only) with the explicit headline that
coverage is anchor constraints, not a tiling. **Granted as the tiered
constraint set** (19 live + 8 live* + 2 suspect usable per the memo's rules;
3 superseded excluded from constraints). The "en cela" resolution at the 3
trigrams is the segmenter's judgment, recorded transparently — not a
red-team finding. Note: the map's B-tier words ("en ce", "par le",
"par ce que") now rest on the auditor's word rules (R-IA1–R-IA4) rather than
the reconstructor's proposal — the compositional grounding the map assumed
is now adjudicated.

### homophone-ab — frame battery AUDITED (verdicts pending)

battery_frames.py/json landed 23:11. Numbers re-derived from the JSON's own
method (characteristic frames = count≥2; binomial depletion tests):
- setA {33,86}: n_shared=2 ([67,66] 1×1, [67,29] 3×1), frac_disjoint=0.956;
  86 in 33's char frames 1/11, p=0.00174 (depleted); 33 in 86's char frames
  0/6, p=0.03131 (depleted); pour-successor overlap EMPTY
  (33: {16,01,79,96,21}; 86: {59,50,48,70,06,56,52,29}).
- setB {48,94}: n_shared=1 ([65,29]), frac_disjoint=0.985; 94 in 48's char
  frames 0/4, p=0.0659; 48 in 94's char frames 0/10, p=0.00085 (depleted).
The frames are 95.6%/98.5% disjoint with significant mutual depletion —
this is the prereg's KILL-bar shape for {33,86} ("zero frame
interchangeability with similarity attributable to shared class alone")
and supports {48,94} SPLIT-vs-KILL toward KILL on frames. **The executor's
PROMOTE/SPLIT/KILL recommendations have NOT landed — verdicts PENDING.**
The V1–V4 substitution battery for setB (48 in 94's "ne" frames) is not in
this JSON; confirm it lands with the recommendation package.

## Rulings

(Per-package: GRANT / GRANT-WITH-MODIFICATION / DENY / FENCE, numbered, file+line citations.
To be filled as packages land. None landed yet at 2026-10-07 23:10 UTC.)

### R-DRAG — systematic drag (council work order, `code/council/drag/`)

**Ruling: GRANT-WITH-MODIFICATION** (2026-10-07 23:15 UTC).

Pre-registration audit: PASS. Plan `code/council/systematic-drag.md` (mtime
2026-10-07 22:52 UTC) predates all drag code/data (common.py 22:57, run_drag.py
23:02, build_inventory.py 23:04, drag_hits.json 23:06, null_report.json 23:08).
The hit bar is pre-registered at plan §2.3 and the null bar (`h_real > max(h_s)`,
real beats all 20 shuffles) at plan §3.1 line 180 — both predate the data.
Positive control: "par ce que" reproduced @224/@952/@1526 byte-exactly —
independently re-derived from the repaired stream (96-87-46 census = [224, 952,
1526]) ✓. Decoy null 0/122 ✓ (bar is tight, not loose). Instrument healthy.

Number re-derivations (all from the repaired stream / the JSON's own lists):
- All 6 new hit positions byte-exact: @1240/@1401=[77,81,87] ✓;
  @179/@1766/@1774=[24,87,64] ✓; @1799=[79,87,64] ✓.
- Null: the JSON's replicate list sums to 254 → mean **12.7** (pop-std 4.8),
  NOT the report text's "13.1 ± 5.2" — **the JSON is the source of truth; the
  report text's null summary is corrected to 12.7 ± 4.8.** FDR = 12.7/9 = 1.411
  ✓ (matches JSON's fdr_estimate). Real=9 < max(shuffles)=24 → the pre-registered
  bar is NOT met; real sits 0.77σ below the null mean. The null verdict stands
  unaffected by the text correction.

Granted:
1. **Null verdict (data):** the 6 new hits are consistent with chance
   (FDR≈1.4). They enter as recorded items, not discoveries.
2. **"le prince" ×2 @1240/@1401** — recorded, one leg each toward 81="prin"
   (new lead). No board tension (le=77✓ provisional-conditioned, ce=87✓
   provisional; prin→81 unknown). A second independent leg is required before
   any LEAD status (≥2-leg rule).
3. **"tout ce qui" @1799 (tout→79)** — recorded, one leg; clean of the 24
   tension (79 unidentified).
4. **0 veto-sensitive** — banked: no provisional is vetoing would-be hits;
   no board-risk flags.
5. **Drag as reusable infrastructure** — banked (seeded, byte-rederivable,
   ~95 s end-to-end).

Modification (downgrade of the task's "one leg each" for three hits):
6. **"tout ce qui" ×3 @179/@1766/@1774 (tout→24) — ZERO fresh legs.**
   These bytes are F31's own «en ce qui» windows re-glossed under the rival
   24="tout" reading; 24="en" is STRONG (F31, NOTES.md) and absorbs them.
   They are non-independent of the standing board. Recorded instead as a
   testable tension/prediction: if 24="en" holds, the tout-reading at these
   three windows is dead. A genuine 24="tout" claim would need to overturn
   F31, not re-gloss its windows.

Recorded as datum (observation, not a claim): the builder's honest read that
the remaining plaintext avoids the top-500 formulaic phrases — a
register/topic constraint in itself.

No status changes. No interim kills. Baseline untouched by this ruling.

### R-CD1 — homophone-cd {52,59} → SPLIT

**Ruling: GRANT** (2026-10-07 23:20 UTC). The executor's VERDICT.md (23:10:38)
recommends SPLIT; the battery numbers were independently re-derived (see
Battery-number audits). All 7 frame-table windows byte-verified (@1342
64-52-38, @1294/@1807 94-52-80, @1435 64-52-82, @160 93-52-94, @264 93-52-33,
@571 94-52-87 ✓). The -este arm exclusivity (pre(59)=84 ×4 vs pre(52)=84 ×0,
Fisher p=0.0555) is the sharpest segregation datum and is linguistically
principled (verb-final "-este" ≠ word "est" — distinct morphemes); a free
homophone of 59 should appear after 84 sometimes, and 52 never does. Frame
battery 1/7 clean (@1342 «qui est» — which also fits rivals, so not an
independent «est»-specific leg); the prereg's SPLIT bar (Leg A passes on its
letter + arm-level segregation per the §c.4 pattern) is met in substance.
The executor is conservative (SPLIT, not KILL; keeps 52's WEAK est-arm lead).
Caveats recorded: Fisher p=0.0555 is marginal — the SPLIT rests on the
linguistic principle as much as the statistic; the "same 5-gram" claim for
@1294/@1807 is actually a shared 4-gram (5th cell differs: 62 vs 61) —
immaterial. The executor's "drag_hits.json does not exist" is stale (landed
23:06) but immaterial — no drag hit touches {52,59}. **Banked solver
constraint: do NOT tie 52↔59 as homophones.** 52 stays UNIDENTIFIED with a
WEAK est-arm lead (pre∈{64,94,93} only, never the este-arm).

### R-CD2 — homophone-cd {76,78} → SPLIT

**Ruling: GRANT-WITH-CONDITION** (2026-10-07 23:20 UTC). 76 never parses as
«er» (76→94=0; «le [76]» ×3 ungrammatical on the er-tine); 76 fits only the
ver-tine («le ver[…]» ×3 @833/@892/@969), with 4/21 windows failing both
tines. Not free homophones — SPLIT granted. **Condition:** the SPLIT is
conditional on the 78 fork's er-lean (french-blitz er|ne, p=3.2e-11). If the
fork owner resolves 78="ver", the {76,78} question re-opens — this ruling
does not pre-judge that. The flagged tension («le»-frames favor ver-INITIAL
for both 76 and 78, against the er|ne diagnostic) is recorded for the fork
owner's battery, not adjudicated here. **Banked solver constraint: do NOT tie
76↔78 as homophones.** 76's ver-lead stays weak-local; the 78 fork is
unresolved by this battery.

### R-IA1 — islet-audit ISLET 10 → WORD-RULE (dissolve; retire polyvalence entry)

**Ruling: GRANT** (2026-10-07 23:22 UTC). Full re-derivation (registry change):
n59=27; naive pre-partition 7/4/7/9 re-derives from the stream; the corrected
partition (est=6 @103/@316/@559/@763/@1210/@1777 + @1796 S5-fenced; este=4
@1190/@1448/@1804 firm + @1291 fenced; sub-tier=5 @216/@1186/@448/@1715/@554;
leftovers=4 @463/@834/@1511/@1833; S5-fenced=6; neutral/fenced=2 @825/@1496)
matches the registry's fences exactly — the fences are load-bearing (naive
pre-only over-counts est=7/subtier=7). Battery: (1) lexical-bigram —
93-59=«l'est» and 94-59=«n'est» are single orthographic words (standard French
orthography, no corpus needed); 84-59 stem+syllable of era-attested -este
verbs (manifeste 130, atteste 35, proteste 19, conteste 19, déteste 15 on the
auditor's v8-free pool); 64-59=«qui est» frame (two words). (2) residual —
word-«est» fails outside {64,94,93} (8 settled adverses, not re-litigated).
(3) forced-context — F1 unfired. (4) homophone-cycling — {52,59} uniform
(p=0.51/0.13). Re-banked as W-est1 (93-59=«l'est») / W-est2 (94-59=«n'est»)
/ W-este2 ([stem]-59, stems 84/06/61/44/86, fenced 15) / F-qui-est (64-59)
+ 59 monovalent «est» syllable. The conditioned-polyvalence entry is
RETIRED. Caveat recorded (phonetic /ɛ/ vs /ɛst/ — the table may list two
syllables; operationally word-membership either way). The F1–F4 falsifiers
are superseded by the word rules (content preserved). **Reconciliation with
R-CD1:** the ISLET-10 dissolution does NOT void the {52,59} SPLIT — the frame
premises re-anchor on the word rules (the est-arm windows still read
«qui est»/«n'est»/«l'est»; the -este exclusivity is about W-este2 verb-words).
Prereg-audit reservation (a) is DISCHARGED.

### R-IA2 — islet-audit ISLET 8 → WORD-RULE (F-qui-le + W-este1)

**Ruling: GRANT** (2026-10-07 23:22 UTC). Both frames re-derived @1445
(37-64-77-84-59-36-67) and @1801 (87-64-77-84-59-35-94) ✓. 84-59 is
stem+syllable of one -este verb (W-este2). Banked falsifier («qui le X est»)
count re-derives as 2 on the auditor's pool; both instances rescued by the
auditor's constituency readings («qui le concernent est effrayé de» —
clause boundary; «qui le pain est une chose» — article not pronoun),
recorded as the auditor's judgments. Re-banked as FRAME F-qui-le
(64-77=«qui le»; depends 64=«qui» prov, 77=«le» lead) + WORD W-este1
(84-59=«[X]este»). ISLET 8's "UNBANKED — needs 59 polyvalence" dependency
is now BANKED-AS-WORD (closed).

### R-IA3 — islet-audit ISLET 1 → 82-arm WORD, 66/89 arms FRAME

**Ruling: GRANT** (2026-10-07 23:22 UTC). Arms re-verified: 82-84 @166
(«m'en»), 66-84 @153/@1150 (cell-position convention: 84 at @154/@1151 ✓),
89-84 @275/@1377 (84 at @276/@1378 ✓, with 29-89-84 ×2 recurrence).
Full 84 accounting re-derives: n84=25 = 5 arms + 9 leftovers + 8 rescoped +
2 formula (46-84-24 ×2 @310/@473) + 1 fenced-adverse (@1665) ✓. Re-banked:
82-arm → WORD (82-84=«m'en»); 66/89 arms → FRAME («[noun] en [V]», depend on
ISLETS 6/7, now class-tier per R-IA5).

### R-IA4 — islet-audit ISLETS 2, 3 → WORD rules

**Ruling: GRANT** (2026-10-07 23:22 UTC). Sanity re-verifications exact:
96-00 @47/@465/@961 («par le» ×3) ✓; W06 06-positions [580,738,1184,1355]
✓ with @1351 reading «le [78] ne ment pas» in context ✓. Re-banked as WORD
rules; residuals recorded (00=«pour» 52/55; 06=verb-stem-class F21).

### R-IA5 — islet-audit ISLETS 6, 7 → class-constraint tier

**Ruling: GRANT** (2026-10-07 23:22 UTC). ISLET 6: 19/19 windows fit
noun/infinitive/nous-vous-class frames, zero subject-pronoun-forcing
windows, 0/19 inside confirmed words ✓. ISLET 7: 14/14 re-derived
(77-89 ×2, 29-89 ×5, 89-48 ×3, 24-89 ×3, 52-89 ×2 fenced non-kill-grade,
29-89-84 ×2), 29-89 never completes «premier», 0/14 in words ✓. Moved to a
class-constraint tier (out of polyvalence). Specific values stay NULL
(honest).

### R-IA6 — islet-audit ISLET 4 → TRUE-POLYVALENCE (sole entry, SUPPORTED)

**Ruling: GRANT** (2026-10-07 23:22 UTC). Re-derived: 29/38 classify
(veut=11, et=18, open=9), ZERO BOTH-conflicts, 0/38 inside confirmed words
(compositional dissolution fails), open list matches the lane record exactly
[199,630,633,902,1248,1372,1450,1519,1623], @1248 NEITHER-fence stands as a
bound. Era legs reproduce on the v8-free pool: «et la»=4070 vs «veut
la»=41 (99:1), «et le»=3788 vs «veut le»=33 (115:1), «et par»=819 vs «veut
par»=3 (273:1), «et qui»=2041 vs «veut qui»=2 ✓. The 67 et/veut fork is the
registry's ONLY genuine frame-conditioned polyvalence — kept as the sole
TRUE-POLYVALENCE entry (SUPPORTED).

### R-IA7 — islet-audit ISLET 5 → INCONCLUSIVE (keep LEAD)

**Ruling: GRANT** (2026-10-07 23:22 UTC). Singleton 64-96-47 @150 confirmed
(ctx 29-87-64-96-47-46-66); n96=21; 96-00 «par le» ×3 kills verb-stem
elsewhere; no second window (F63's retired falsifier confirmed unmeetable).
Era caveat honestly disclosed: the 5-frame leg is v8-dependent (clean pool
n=1, filler «arriva»); the «ce qui par ce que»=0 double-zero reproduces
v8-free. Standing LEAD keeps; no promotion case without v8. Flag recorded.

**Registry summary after R-IA1–R-IA7:** of 10 islets, 5 dissolve into
word/frame rules (1, 2, 3, 8, 10), 1 is true polyvalence (4: the 67 fork),
2 are class rules (6, 7), 1 is an underpowered singleton (5), 1 is a
confirmed kill (9). The auditor's 7 recommended registry edits are ADOPTED
as ruled above. No settled kill was re-litigated. The compositional thesis
is confirmed as the dominant pattern.

**Update 2026-10-07 23:30 UTC:** the "ISLET 10 is provisional (not settled —
auditable)" watch-out is now SUPERSEDED — ISLET 10 is DISSOLVED per R-IA1
(re-banked as W-est1/W-est2/W-este2/F-qui-est + 59 monovalent «est»). The
islet registry's conditioned-polyvalence tier now holds ONE entry: ISLET 4
(the 67 et/veut fork, SUPPORTED). ISLETS 6/7 are class-tier; ISLET 5 is
LEAD-singleton; ISLET 9 is a confirmed kill.

### R-CC92 — carry-classes R13-92 (92 F33 battery)

**Ruling: GRANT-WITH-MODIFICATION** (2026-10-07 23:30 UTC). The six POUR-arm
windows re-derive byte-exactly (@49 00-92-79, @330 00-92-50, @593 00-92-79,
@683 00-92-64, @978 00-92-07, @1154 00-92-29 ✓); R_top10 no-drift gate PASS
(top-10 identical to round-12's); T n/a at 4/6 windows honestly recorded.
The NULL (constrained) verdict is GRANTED (expected outcome; fork scope
Fork-W bounds all; 92 mirrors the 33 paradox at small n — recorded).
**Modification:** the T_683-dependent claims are FENCED, not banked.
T_683 = n_v8("pour X W qui") = 0 is a v8 phrase-zero — VOID under the
standing F77 rule and R12 case law ("v8 phrase-zeros are VOID as French
measurements"). The "J_POUR FAILS at @683" verdict and the "@683 NOUN-islet
CORROBORATED" claim cannot rest on it; both need a pool∖v8 re-run of the
tail query before they bank. The executor's drag_integration is recorded as
lead-adjacency (79="tout" at @49/@593; tout_24 dead-if-24="en"-STRONG;
81@1402 adjacency to the 92 VERB-arm) — consistent with R-DRAG, not a new
leg. R13-31 and R13-33 results have not landed; the carry-classes package
is partial — verdicts PENDING on those.

### R-AB1 — homophone-ab {33,86} → SPLIT

**Ruling: GRANT** (2026-10-07 23:50 UTC). The executor's VERDICT.md
recommends SPLIT; every battery number re-derives byte-exactly from the
JSON's own method: joint frames 2/45 shared (frac_disjoint 0.9556) ✓; 86 in
33's char frames 1/11, binomial p=0.00174 ✓; 33 in 86's char frames 0/6,
p=0.03131 ✓; 86 depleted in 33's pour-successors {16,79,21}, Fisher
p=0.00072 ✓; 77-frames 86-only, one-sided Fisher p=0.04809 ✓ (the battery
script's `fisher_depleted` is one-sided by design — the tested hypothesis is
depletion, and the PREREG names "Fisher asymmetries"; accepted). Pour-frame
successor sets fully disjoint (33: {16×2,79×2,21×2,01,96}; 86:
{56×4,29×2,59,50,48,70,06,52}) ✓; uniformity χ²=0.8596 p=0.354 ✓; runs
z=-0.291 ✓. The ≥2-leg bar is met (depletion binomials + pour-successor
Fisher + disjoint pour completions + 77-frame asymmetry). The disclosed
joint-governs-marginal refinement is accepted — the work order's literal test
is the joint frame, and the PREREG already named frame-interchangeability as
the PROMOTE requirement.
**Independent corroboration:** the missing-mass agent's phase maps (both
`phase_map_repaired.json` and `keystruct/phase_cache.json`) read 33=A/86=B,
against the reconstructor's §b B,B — an independent second strike on shared
value (phase A/B mismatch, CANDIDATES.md §B). Reclassification GRANTED:
{33,86} are class-mates (cf. the 06/86 pattern), not homophones; the
reconstructor's §b {33,86} PROPOSE is RETIRED. **Banked solver constraints:
do NOT merge 33+86 windows in any downstream ID battery; 33's infinitive
hunt proceeds on its 8 pour-frames alone.** The executor's falsifier is
recorded (a second independent frame type where 33/86 interchange at 1690
rates, or a 33 value ID that also parses 86's 77-frames and 56-frames).

### R-AB2 — homophone-ab {48,94} → SPLIT

**Ruling: GRANT** (2026-10-07 23:50 UTC). Numbers re-derive: joint frames
1/67 shared (frac_disjoint 0.9851) ✓; 48 depleted in 94's char frames 0/10,
binomial p=0.00085 ✓; uniformity χ²=0.0133 p=0.908 ✓; runs z=-0.347 ✓;
pre/suc marginals p=0.482/0.509 ✓; mutual NN at 0.643 ✓. PROMOTE was
correctly PRE-BARRED (48="ne" killed kill-grade, F60 — case law applied, not
re-litigated). The SPLIT verdict (class-mates, ne-distributed, different
values) is granted on the frame disjointness/depletion + F60 + the
missing-mass independent corroboration (contact P1c, era-budget conflict,
CANDIDATES.md §C). Two recorded notes: (a) the V1–V4 substitution battery as
named did not land — the executor's test 8 (joint-disjoint ⇒ no substitution
parse) is the honest equivalent; the substitution is vacuous on 98.5%
disjoint joints, and the single shared ('65','29') frame is tense for
94="ne" ("ne er" without a stem — flagged, not litigated). (b) Tests 6 and 8
share the joint-frame data — the ≥2-leg structure is frame
disjointness/depletion + F60 + independent corroboration, not 6+8 as two
fully independent legs. **Banked solver constraint: do NOT tie 48↔94 as
homophones.** 48 stays UNIDENTIFIED, constrained to a ne-class pre-verbal
item ≠"ne"; the 48-specific "de ce que" islet (@863) survives untouched and
counts as evidence FOR 48's own value. The executor's falsifier is recorded
(a (pre,suc) frame with ≥3 windows where 48/94 interchange at 1690 rates, or
a 48 value ID that parses in 94's ('62','79')/"on ne" frames).

### R-CC31 — carry-classes R13-31 → CONFIRM 31=VERBAL (provisional-conditioned)

**Ruling: GRANT** (2026-10-07 23:55 UTC). This is verification, not
re-litigation: the independent re-derivation is byte-identical to round-12's
(3 disambiguated verbal windows — qui-relative @338/@1647, D-ce @1488; 0
disambiguated nominal; route-b STILL UNMEETABLE: 11→31 n=1 @1516, 46→31
n=0). The conservative-outcome audit is fully disclosed (C1 conditionals
64="qui"/87="ce", 08="l'"-lead; "-quière" FENCE on 64="qui"-word open; E31-1
era leg VOID; one-sidedness of the D-rules). The suc-29 consistency datum is
correctly marked as sharing the hypothesis, not a leg. **31=VERBAL (finite)
provisional-conditioned CONFIRMED** — the round-12 GRANT stands with the
audit attached. No status change beyond the standing grant.

### R-CC33 — carry-classes R13-33 → NULL (constrained; paradox sharpened)

**Ruling: GRANT** (2026-10-07 23:55 UTC). T2 fired mechanically per its
pre-registered bar: n_pool∖v8("pour X ce qui")=14, unique argmax savoir n=2 ✓
(pool∖v8 = 3,867,332 tokens, disjoint from v8 AND round-12's v8 tail arm —
strictly F77-compliant). But LEAN is correctly NOT claimed: savoir ∉ R top-10
(base-rate leg fails), savoir is bisyllabic ⇒ fork-incompatible under
Fork-W, and suc=21="ce"-banked cannot be "-oir" under Fork-S. **The T2
winner is exactly the candidate the granularity fork forbids under both
forks — the paradox is sharpened, not resolved.** NULL (constrained) is the
honest verdict: F-D fence re-confirmed 0 on the disjoint pool∖v8
(conditional on 96="par"); F-A stays FENCED; F-B/F-C/F-E NULL; F-C pair =
one unknown infinitive ×2 (replication datum); fork scope Fork-W only.
Drag integration: no verdict change; two named items recorded — 81="prin"
carries a post-context adverse at BOTH windows ("la pour" ungrammatical after
"le prince" — replicated, LEAD-grade); 79="tout" (@1799, clean of the 24
tension) names the first F-C tail-gloss battery ("pour X tout W", round-14,
gated on 79="tout" promotion — NOT run).

### R-CR48 — carry-rest 48 follow-ups → 74-class OPEN / H_stem leg / negative

**Ruling: GRANT** (2026-10-07 23:58 UTC). Three recommendations, all
conservative, all with [FR-JUDGMENT] legs explicitly marked (PREREG lines 34,
92; carry_results.json method_notes) — the first-shift PREREG reservation
(a) is discharged.
- **74-class → OPEN; the @863 islet neither promoted nor killed.** A1:
  "de ce que" L1s are class-ambiguous on the clean-diplo pool (191 hits, 155
  distinct L1s, no class ≥70%; top-40-only classification disclosed as
  approximate). A2: 74→77 ×2 (@212/@1677) is anti-verb but adverse-grade
  only (77 provisional-conditioned); noun/adj/participle compatible. Kill bar
  and promote bar both not met. The "74 is unlikely a verb" datum is banked
  as adverse-grade, not kill-grade.
- **H_stem GAINS A LEG** — 48 = vowel-initial verb-stem syllable cell. B1
  PASS (3 windows compatible on banked values; @1229 actively friendly —
  82="m" elision forces vowel-initial); B2 13.3% (11,509/86,527) ≥ 5% bar,
  licensing the two-cell stem+"er" split as a real French class. **Leg only —
  NOT a value promotion.** Recorded open tension (from R-AB2): 48's ne-like
  marginals tension H_stem the same way they tensioned the syllable tier;
  the executor's testable prediction stands — name a construction where
  stems occupy pre-verbal slots, or drop the leg.
- **Second "48-47-46" hunt → CLEAN NEGATIVE** (only @863; @1658=48-47-98
  confirmed). followup48 863-c BANK-AS-LEAD stands unchanged.

### R-CR1248 — carry-rest @1248 → PC-1 leg GRANT / DP-1 PERMANENT FENCE

**Ruling: GRANT-WITH-CONDITION** (2026-10-07 23:58 UTC).
- **PC-1: GRANTED as an attestation-breadth leg** (peu arm 4/8 → 5/9). The
  spot-check re-reads genuine: "il craignait [CHAPITRE XXVII running head]
  peu que M. Thiers se livrât…" — "craindre peu que" + subjunctive, a new
  lemma in Guizot-DIP (diplomatic register), OCR-running-head caveat honestly
  recorded. A leg, not a promotion.
- **DP-1: PERMANENT FENCE for both arms** — the double-pour stack
  pairs[1244:1255] is UNLICENSED: zero genuine in ~22MB round-12 pool + the
  executor's independent 758k-token re-check (RDM-1841-q1 459,176 +
  Guizot-DIP 298,765; strict_dp_inf=0, strict_dp_peu=0), and the k-depth
  family absent at ALL depths k=1–5. **Condition:** recorded as
  frame-unattested, NOT ungrammaticality evidence (pre-registered scope); the
  "permanent" binds future re-tests to a new instrument or new data through
  this docket, not to self-service.
- @1248 NEITHER-fence STANDS (WO6 single-work-order bar; neither arm
  promotes).

### R-CRESTE — carry-rest -este tie-break → atteste FRAME-BEST LEAD

**Ruling: GRANT-WITH-CONDITION** (2026-10-07 23:58 UTC). The transitivity
census (clean-diplo 3.6M tokens, every hit constituency-read, [FR-JUDGMENT]
marked and disclosed) plus the frame search give **atteste FRAME-BEST LEAD**:
the ONLY candidate with the exact «qui le V» frame attested in-register
("c'est lord Beauvale qui l'atteste dans une dépêche", RDM-1841-q4) + 4×
«le/l'»-government ("comme l'atteste une légende/Strabon" — «l'» direct
object, postposed subject). **Condition:** this is a LEAD, NOT a unique-ID
promotion — the n=1 fragility is recorded (exact trigram on one token; OCR
hyphenation caveat standard), and the este-verb PROMOTE bar (≥2 independent
legs + stem-ID) stays with the red team. manifeste/conteste remain
transitivity-licensed; the E-trans "bar_refinement" (nominal «le manifeste»
excluded; feminine «la déteste» counted as government evidence) is
judgment-backed and disclosed — the grades stand as Frenchman readings, and
corpus counts alone license no grammaticality claim beyond what was
constituency-read. T1/T2/T4/T5: honest nulls recorded. T3: 06="pro" stays
LEAD-WEAK (proteste now doubly-weak but NOT killed — dictionary-transitive
"protester sa bonne foi" keeps it alive). reste EXCLUDED (intransitive; not
in H0 — pool-scoping, no status change). H0 stays set-valued.

### R-MM1 — missing-mass deficit arithmetic → GRANT (data)

**Ruling: GRANT** (2026-10-07 23:59 UTC). The arithmetic re-derives exactly:
11 STRONG deficits, all in syllables with zero identified coverage, summing
385.6 occ → 20.0 cells naive (mean cell 19.24); fragment-corrected (qu
remainder ≈20 occ ≈1.0 cell after que/qui/qu' re-bundling; "re" covered by
29's coarse {er,re,é} bundle) ≈330 occ → **~17 cells, range 17–20**. No
identified syllable clears the pre-registered FLAG bar (≥1 mean cell AND
z<−2). The v8 genre sensitivity reproduces the direction: no identified
syllable flags (46=que −2.1 occ z=+0.40 balanced; 29={er,re,é} +7.8 occ
z=−1.08 balanced; 87={ce,se} +12.0 z=−1.83 near-miss, below bar).
Both first-shift PREREG reservations are discharged: (a) the v8 sensitivity
run landed (v8_counts.json/v8_deficit.json); (b) the conditioned-islet
WORD-rule assumption is now adjudicated (R-IA1–R-IA4 dissolved the relevant
islets into word rules). **Banked datum:** the missing mass is in uncovered
syllables (~17–20 cells among the 84 unidentified groups), not second cells
for la/que/ce; identified cells run 2.9× hot in aggregate vs era (register/
granularity caveat carried, not hidden).

### R-MM2 — missing-mass priors + digit hunt → GRANT-WITH-MODIFICATION

**Ruling: GRANT-WITH-MODIFICATION** (2026-10-07 23:59 UTC). The ranked priors
are BANKED AS PRIORS ONLY — explicitly not promotions, with an
**anti-promotion fence**: no prior may serve as a promotion leg or status
claim without a fresh pre-registered battery and a new ruling.
- 48→ne-class **P1c** (contact P1: sim 0.643 mutual NN, B/B; era-budget
  conflict: 94 alone 1.55× ne budget; 48+94 → 3.2×).
- 52→est-class **P1c** (contact P1: sim 0.557 mutual NN, C/C, n 27/27;
  budget conflict: 59 alone 2–3.5× est budget; 52+59 → 4–7×).
- 76→ver/er **P1** — cleanest surviving set (mutual NN, C/C, rate-compatible).
- de-pool **P2** = {01, 98, 14, 88, 16, 43, 44, 08, 37}; les/te/et an honest
  three-way tie ({01, 88, 16, 37, 91}).
- **{33,86} demotion to WATCH converges with R-AB1**: the phase discrepancy
  is independently confirmed (both phase maps: 33=A/86=B; the reconstructor's
  §b B,B is the outlier) — two independent strikes against shared value.
- **Digit hunt: NEGATIVE → RETIRE.** The T2/T4 falsifier fired (95/22/27/57/
  54/04 sit in grammatical frame slots, not isolated digit cells); T1
  uninformative; T3 chance-consistent. The 8 groups (04, 22, 27, 54, 57, 90,
  95, 99 — all phase R) are reclassified as rare-vocabulary cells.
**Modification:** the de-pool P2 list includes 08, which carries R-CC31's
08="l'" LEAD — the P2 contact prior and the value lead coexist as
priors/leads, not as value claims; any 08="de" battery must name and beat
the "l'" lead explicitly.

## Settled kills — no re-litigation (STATE.md + R12, enforced verbatim)

unconditioned-59 (REFUTED, R10-R7) · H4g (REFUTED, R10-R2) · 48="ne" (killed) · H_verb (killed) ·
86=que-family (refuted) · unconditioned 84s (killed) · three mergers (killed: F56 {77,00}="le",
others per ledger) · column-refuge concretizations (retired) · retired WO-6 bar (superseded) ·
unconditioned-48="de" (KILLED kill-grade 10 windows, R13) · "gouvernement"/"gouvernent" readings
(killed, R9) · é-initial-noun theory (retired, R10) · 77="gouv" (demoted→disfavored, R9).

Watch-outs for this round's executors: ISLET 10 is provisional (not settled — auditable); the
84=noun arm was RESCOPED not killed (F62); 52="pas"-STRONG is banked (registry ISLET 9 L5);
62="on" is fenced STRONG LEAD; 92's H-pre is REFUTED / H-presuc FENCED (R12); the veut-arm
subject bar is banked and reusable (R12); the V-1519b battery design is VOID (R12); the
n_eff cap precedent: islet claims cap at FENCED below ISLET-3's n=4/n_eff=3 precedent (R12).

## Methodology flags carried (standing — R11/R12)

- Nesselrode v8 VOID for phrase queries; clean-diplo corpus is the phrase instrument (F77).
- Never score manual-tiling bearing counts (N30/N32 instrument ban).
- Double-pour label convention: pairs[1244:1255], cite "@1244–1254" (R7 correction).
- Watch06 H4g case law: the prereg's LITERAL formula binds (RULINGS-ROUND10 R2).
- V29 contaminated; phase instrument VOID; 'er'-rate checks uncalibrated (F26).
- Era bigram attestations must be constituency-read before supporting a grammar rule (R12:
  est-ce confound case law — kill the confound at the window, don't average over the pool).
- v8's 149 "pour INF" underpowers rare-shape fences — pool-level license checks pre-registered;
  a v8 L-failure at P(v8-zero)≈0.44 under H0 is noise, not a frame fence (R12).
- Promotion bar: ≥2 independent checks. Provisional anchors propagate their status to
  everything built on them.

## Baseline state at round-13 start (2026-10-07 23:10 UTC — re-confirmed before ruling)

- `code/crowd7/redteam/verify_f26_17.py`: **203/203 PASS** (R12BANK's 203 re-run green at
  round-13 start; earlier BANK blocks untouched).
- `code/crowd7/redteam/verify_round7.py`: **133/133 PASS** (ROUND12-LEDGER's 133 re-run green
  at round-13 start; earlier LEDGER blocks untouched).

(R13BANK / ROUND13-LEDGER extension to be applied at docket close behind the adjudicated
facts — extend, don't rebuild.)

## Procedural notes

- This docket file is the adjudicator's instrument: no party inserts checks or status language
  into `verify_f26_17.py` / `verify_round7.py` without a ruling in this document (round-10
  "unauthorized finalizer edit" case law).
- Status vocabulary in force: GROUND TRUTH (pencil cribs only) · CONFIRMED · provisional (with
  conditions named) · provisional-conditioned · LEAD · STRONG LEAD · LEAD-fenced / fenced ·
  WEAK arms · INCONCLUSIVE · PLAUSIBLE · disfavored · DISFAVORED (strong) · REFUTED · KILLED ·
  NEITHER-fence · UNIDENTIFIED · UNTESTED (NULL, not adverse).
- Interim-kill authority is armed: any package re-litigating the settled list, or attempting
  a coordinator-applied bar, or inserting unauthorized baseline edits, gets an interim kill.
- Running docket: packages ruled as they land, not held for batch.
