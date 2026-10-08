# Round-14 Red-Team Adjudication — executor status-change docket (CLOSED)

Red team: round-14 red-team adjudicator · 2026-10-07 (CDT) · kill authority
over all round-14 promotions, demotions, and kill recommendations. Scope:
every round-14 executor recommendation under STATE.md "next: Round-14 work
orders" (WO1–WO8). **Out of scope:** KE1/KE2 (red-team-owned, adjudicated
round 13). Standing convention: the red team rules ALL status changes before
any merge — no claim merges without its ruling; no coordinator-applied bars,
ever (F26-17 standing). Round-13 precedent: RULINGS-ROUND13.md (21 rulings).
Bars: `code/crowd14/redteam/PREREG14.md` (LOCKED 23:31:37 UTC, before any
round-14 executor output existed — bars applied as written).

## Docket status (2026-10-07 — CLOSED)

**DOCKET CLOSED — 9 rulings issued; 0 packages pending.**
All 10 round-14 work products landed (`code/crowd14/`): registry,
infinitive33, prin81, battery48, poly62, value52, fork78, value59third,
liaison (+ report_inbox notes). 9 rulings below, numbered R-001–R-009 in
order of issue. Each: claim, evidence re-derived by the red team, ruling,
and what would overturn it.

**Net: 0 promotions (bar held an eleventh round); 1 kill (81="prin" LEAD);
1 fork resolution (78 positional polyvalence, F33-form); 6 GRANT/HOLD;
1 GRANT-WITH-CONDITION; 1 BANK. 3 prereg deficiencies noted (no PREREG.md:
value52, poly62, value59third).**

**Baseline extensions applied at close:** R14BANK-close in
`code/crowd7/redteam/verify_f26_17.py` (11 cipher-side checks behind the
rulings); ROUND14-CLOSE in `code/crowd7/redteam/verify_round7.py` (12-entry
status-delta ledger). Extend, don't rebuild — earlier blocks untouched.

**Baseline state at round-14 close:** `verify_f26_17.py` **259/259 PASS**
(249 pre-close + 10 R14BANK-close). `verify_round7.py` **174/174 PASS**
(169 pre-close + 5 ROUND14-CLOSE). Both exit 0.

## Standards in force (PREREG14, locked)

- No coordinator-applied bars — the red team is the bar.
- Prereg mtime must predate first data-run mtime (§2).
- Promotion: ≥2 independent legs, counted by the red team (§3).
- Kill: pre-registered bar fired AS SPECIFIED — no bar, no kill (§4).
- No-re-litigation list (§5, extended). 1690 uniformity NECESSARY but
  INSUFFICIENT. v8 phrase-zeros VOID (F77). F30 rigid syllabification DEAD.
- Traceability: trust the JSON; full re-derivation for kills/registry
  changes. Anchor-preserving controls. Provisional statuses propagate.

## Interim kills

None issued (the single kill below is a docket ruling, not interim).

## Pre-registration audit

| Executor | PREREG mtime (UTC) | First data-run mtime (UTC) | Verdict |
|---|---|---|---|
| infinitive33 | 23:31:49 | 23:32:09 (fork_disc.py; results 23:34:55) | **PASS** (20s margin) |
| prin81 | 23:30:15 | 23:32:39 (corpus_test.py; results 23:33:17) | **PASS** (2m24s margin) |
| battery48 | 23:33:20 | 23:33:38 (a74.py; results 23:40:20) | **PASS** (18s margin) |
| fork78 | 23:35:57 | 23:37:15 (fork78.py; results 23:37:22) | **PASS** (78s margin) |
| value52 | — (none) | 23:31:24 (value52.py) | **FAIL** — deficiency NOTE (§1.4); no status change recommended, impact limited |
| poly62 | — (none) | 23:30 (build_stream.py) | **FAIL** — deficiency NOTE (§1.4); HOLD only, impact limited |
| value59third | — (none) | 23:33:01 (ence_frame.py) | **FAIL** — deficiency NOTE (§1.4); LEAD-grade DENIED, fenced candidate only |
| registry | n/a (application of adjudicated rulings) | — | n/a |
| liaison | n/a (memo) | — | n/a |

## Battery-number audits (re-derived from the repaired stream)

All headline cipher-side numbers below were re-derived by the red team
against `code/side-keyhunt/repaired_offsets.json` (never `canonical.py`).
Corpus-side spot checks replicated with the lane tokenizer on the stated
pools.

---

### R-001 — Registry rewrite: GRANT (ADOPT)

**Claim:** R-IA1–R-IA7 applied verbatim; 3/3 byte-exact verifications;
4 downstream files updated; 3 ambiguities flagged not resolved.
**Evidence (re-derived):** W-ment 06-positions [580,738,1184,1355], all
pre=82 (82-positions [579,737,1183,1354] — R14BANK) ✓; F-qui-le @1444 =
[37,64,77,84,59,36,67], @1800 = [87,64,77,84,59,35,94] ✓ (corrected
frame-start indices per the round-13 docket note); W-par-le 96→00 @
[47,465,960] ✓ (R14BANK). Downstream edits confirmed in
`code/council/solver-architecture.md`, `code/council/systematic-drag.md`,
`code/crowd13/liaison/smith-constraints.md` (dated amendment block, original
kept as record), `code/crowd9/conditioner/islet_registry.md` (supersession
pointer, content otherwise untouched). The 3 ambiguities (N60 wording vs
R-IA3; 66/89 class-fall ruling question; crowd14 INDEX) are properly fenced
as curator/red-team questions — the rewriter correctly followed the
adjudicator's ruling text over the curator's gloss where they differ.
**Ruling: GRANT — ADOPT the rewrite as the working registry.**
**Overturned by:** a byte-mismatch in any verification or a deviation from
the R-IA1–R-IA7 ruling text.

### R-002 — Infinitive-33: GRANT

**Claim:** Fork S/W discriminator 8/8, no unconditional refutation; Fork S
survives only by overriding 4 standing values; Fork W intersection empty;
@460 = second tout-frame for 79; paradox stands sharpened; no promotion.
**Evidence (re-derived):** 8 "pour 33" frames byte-exact
{186,408,467,846,936,1088,1245,1630} ✓ (matches R-CC33 banked); @460 =
[79,87,11,59] ✓; n("tout cela est")=48 and n("tout ce qui")=523 on
pool∖v8 (3,867,332 tokens) — replicated exactly with the executor's
method ✓; savoir fork-forbidden under both forks ✓ (W: disyllabic vs
1 group; S: needs 21="ir"-chunk, breaking banked 21="ce"); Fork S must
break 16="i"/79="tout"/96="par"/21="ce" (4 standing values) ✓; Fork W
intersection [] ✓. The executor honestly reports the unlock-bar (i)
literally FAILS (@1799 not the sole tout-frame) and does not force the
unlock — exemplary.
**Ruling: GRANT.** Discriminator ran as pre-registered; paradox stands
sharpened; @460 banked as a second tout-frame DATUM for the 79="tout"
promotion lane (not a promotion — correctly fenced).
**Overturned by:** a frame re-derivation mismatch, or a monosyllabic X
with ≥2 independent legs (the prereg's own break condition §5.3).

### R-003 — Prin-81: KILL GRANTED

**Claim:** KILL 81="prin" — "la pour" era-fenced (0 genuine), "cela" kills
"le prince" at both windows, F-C anchor tension; 81 UNIDENTIFIED.
**Evidence (re-derived):** windows byte-exact — @1239–1247 =
[67,77,81,87,11,0,33,16,0], @1400–1408 = [67,77,81,87,11,0,11,95,46] ✓;
n81=14 ✓. Corpus spot-check on the CLEAN pool (v8 excluded):
"le prince la" = 0 ✓ (kill leg survives), "cela pour" = 22 ✓ (attested),
"le prince" = 734 (sane baseline). The two readings are mutually exclusive
(share cell 87); "cela pour" 22× vs "le prince la" 0× is a word-space
grammatical kill; F-C flanks (@1086/@1095) admit no "prin"-word (zero French
words end in "prin" per the battery's survey). **Methodology flag:** the
code did NOT exclude v8 despite the prereg's "clean pool" clause —
verdict survives on clean-pool re-derivation (flag, not overturn; the zeros
are conservative under v8 inclusion).
**Ruling: KILL GRANTED.** 81="prin" LEAD is dead; 81 returns to
UNIDENTIFIED. "cela"@1242/@1403 confirmed (standing 87-11 unit — no status
change). 11="la" (GT) and 00="pour" (STRONG LEAD) untouched. Drag docket
item "le prince"×2 closed as FDR-consistent chance artifact (F108).
**Overturned by:** an era-attested "le prince la" frame or a second
independent "prin" leg.

### R-004 — Battery48: GRANT (HOLDs as specified; B4a referral adjudicated)

**Claims:** 74-class HOLD (74=syllable-class, word-class fenced);
48="de" iff "de ce que" LEAD-weak STANDS; H_stem HOLD strengthened
(B4b 299 genuine; B3c named); B4a bar referred.
**Evidence (re-derived):** 74-74 bigrams = 6 @[417,816,861,919,1053,1637],
6/33 = 18.18% vs era word self-repeat 0.057% = 319×; bar (era < 0.5%)
fired as specified ✓. @862–866 = [74,48,47,46,0] ✓ (frame re-derives;
islet not killed, not promoted — HOLD correct). B3a windows: [1229]=48/
[1230]=29, [1589]=48/[1590]=29, [1398]=48/[1399]=40, [1228]=82="m" GT ✓.
B3b kill-falsifier not fired (48→INF=5, 48→WSEG=2) ✓. B3c: naive "ne 48"
naming failed (0), complementary-slot construction NAMED (pre48 =
62×6 + 82×4 banked pre-verbal; 94 never pre-vocalic — elision explains
94-48=0) — red-team caveat 3 satisfied ✓.
**B4a referral — adjudicated:** share 0.0342 vs pre-registered bar 0.05 →
**bar MISSED as specified; the bar stands.** The miscalibration diagnosis
is ACCEPTED as explanatory only: the 5% bar was set above the 4.0%
independence expectation (0.133×0.3007), and observed 0.0342 = 86% of
expectation — independence-consistent, neutral-not-adverse. Per PREREG14
§2.2, no post-hoc recalibration: the LEAD-grade bar (B3a ∧ B4a≥5% ∧
B4b≥3) does NOT fire. H_stem keeps its round-13 leg, strengthened by B4b
(299 genuine, bar met 100× over) and B3c — HOLD, not LEAD, not killed.
**Ruling: GRANT** — both batteries' HOLD verdicts as specified; B4a bar
stands as specified (miss recorded as bar-design failure, not adverse
evidence).
**Overturned by:** B4a ≥5% on a preregistered re-run, or a second
independent H_stem leg.

### R-005 — Poly62: GRANT (HOLD)

**Claim:** adverse NOT dissolved; L1 rate leg banked (3.2× over);
uniformity satisfied (necessary only); CONFIRM/KILL bars not met.
**Evidence (re-derived):** 62→48 windows [360,425,1315,1349,1464,1569] ✓
(6/6); n62=35 ✓; 62→94=9 ✓ (STRONG LEAD legs survive untouched); window
contexts match the report's table ✓. No window composes an era-attested
word with 62 as syllable-"on" under standing values — the dissolution
condition fails honestly. L1: 35 vs ≈10.8 monovalent expectation (3.2×) —
banked as QUALITATIVE leg (direction robust; quantitative fit
cut-dependent per the executor's own honesty note; primary-diplomatic pool
includes v8 — rate caveat noted). Uniformity (Fisher p=0.195/0.070,
χ² p≈0.058): necessary condition satisfied, correctly not used as a
positive leg (1690 law). The "me on"/"te on"=0 genuine finding is exported
as a FENCED adverse for the 21="me"/74="te" leads (not a ruling on 21/74).
**Ruling: GRANT** — HOLD as specified. Deficiency NOTE: no PREREG.md
(§1.4); the §5 "pre-registered bar" has no timestamped prereg — HOLD is
no status change, impact limited, but future batteries citing these bars
need proper preregs.
**Overturned by:** a window composing an era-attested word with 62 as
syllable-"on" under standing values.

### R-006 — Value52: GRANT

**Claim:** 52 UNIDENTIFIED; "la 52"×3 FENCED; allophone test
STRENGTHENED; Vstem-arm referred not run.
**Evidence (re-derived):** 5-gram [6,11,52,37,43] ×2 @1122/@1720 ✓
(la-arm formulaic, n_eff=2); 11→59 @463 ✓ (same-pre/different-suc
allophone datum — and it's the @460 "tout cela est" window,
cross-confirming R-002); Vstem-arm 52s @1081(pre=6)/@1100(pre=86)/
@1129(pre=86)/@1356(pre=6) ✓ (4 windows, referred); P(52)=27/1847=
0.01462 ✓ ("france"-word kill 9.1× stands). The allophone
strengthening (0 shared (pre,suc) frames; MC P=0.059) corroborates the
STANDING F103 split — not re-litigation (§5.3); do not merge 52/59
windows. "la est"=0 kills est at all three la-windows ✓.
**Ruling: GRANT** — 52 UNIDENTIFIED stands; "la 52" FENCED (missing legs
named); Vstem-arm banked as OPEN residual/referral. Deficiency NOTE: no
PREREG.md (§1.4); the "pre-registered bar" for the la-inversion is
unverifiable as pre-registered — fences/holds only, impact limited.
**Overturned by:** a 52 value with ≥2 independent legs.

### R-007 — Fork78: GRANT-WITH-MODIFICATION (H1 CONFIRMED, F33-form)

**Claim:** H1 CONFIRMED — fork RESOLVED: 78="ver" word-initial / 78="er"
at non-initial er|ne boundaries.
**Evidence (re-derived):** 6 INITIAL×ver-frame windows byte-exact —
@297/@1670 [11,78,*] ("la 78", pre=11=la GT), @415/@476/@1771 [37,78,*],
@629 [87,78,67] ✓; @1181 = [77,78,94] ✓ (NON-INITIAL×er-frame);
78→94 ×2 @1181/@1352 ✓ (banked F38); 76 = 21 windows, 76→94 = 0 ✓.
Leg 2 (H0-er KILL): "la er" ungrammatical ×2 GT-anchored contradictions —
kill-grade, instrument-independent ✓. Leg 3 (H0-ver contradiction): 78-94
as "ver|ne" = zero genuine common words (h3a diagnostic p=3.2e-11) —
weak grade per h3a's own prereg, honestly graded ✓. Leg 4 (76 contrast):
76 uniform "ver" (initial+final, 0 er-frames) — the er-arm is licensed
only at er|ne boundaries, which 76 never reaches (0/21) ✓; the prereg's
"zero FINAL" expectation was corrected by the Frenchman (French "ver"
is positional-broad — honest revision, not hidden) ✓. Leg 5 (Frenchman):
concurs ✓. Leg 1 table [[6,0],[0,1]] directionally perfect, p=0.143 —
pre-registered p<0.05 bar NOT met, honestly reported (underpowered) ✓.
Verdict rule (pre-registered): both uniform alternatives contradicted ✓,
table directionally perfect ✓, ≥2 independent legs ✓ (4: grammar+GT,
corpus diagnostic, 76-contrast, ear), Frenchman concurs ✓, {76,78}
tension addressed ✓.
**Ruling: GRANT-WITH-MODIFICATION — H1 CONFIRMED as F33-form conditioned
polyvalence.** Modifications: (a) the er-arm is boundary-specific
(er|ne), NOT generic non-initial — the ruled form; "er-FINAL" per se
remains UNTESTED (zero word-final 78s); (b) the rule inherits 94="ne"
provisional-strong (Legs 1-er-frame, 3 depend on it); (c) même-4 fenced,
@1352 contested, 16/31 windows positionally UNCERTAIN — the rule is
proven on the classifiable subset; (d) the {76,78} split STANDS (F103,
1690 law) — no merger; whether initial-76/78 share the "ver" cell is
fenced for the solver side.
**Overturned by:** a word-initial 78-94, or a 76 at an er|ne boundary.

### R-008 — Value59-third: GRANT-WITH-CONDITION

**Claims:** (a) no third value needed — the «en ce»+noun frame was a
misparse; (b) @825 = 87-59 = «c'est», W-cest LEAD-grade, 4 legs.
**Evidence (re-derived):** 87→59 sole window @824 (59 cell @825) ✓ —
exactly 1 in the stream; pairs[823:830] = [24,87,59,38,82,1,24] ✓.
Corpus replication (pool∖v8, 4.13M): «en ce» = 441 ✓, «en ce»+est-initial
= 0 ✓, «c' est» ≈ 8,160 (≈ executor's 8,147; 0.16% pool-definition delta)
✓. The decisive point is grammatical, not numeric: the standing
«ce est»=0 kill tested the NON-ELIDED bigram; French obligatorily elides
ce+est → «c'est» — the frame map missed the elision. (a) is a correction
of prior analysis, not a new hypothesis. (b)'s 4 legs (W-est1 precedent,
corpus 8k, elimination, diplomatic parallels) are substantive but
POST-HOC — no PREREG.md exists.
**Ruling: GRANT-WITH-CONDITION.** (a) GRANTED — no third value needed;
WO7's premise dissolves (the «en ce»+noun frame was a misparse); 59's
inventory needs no third value. (b) W-cest banked as FENCED CANDIDATE,
NOT LEAD-grade — LEAD-grade requires preregistered legs (§1.4, §2.2);
the 4 legs are recorded as post-hoc supporting analysis. Fence items
F-a (24="en" confirmation), F-b (38's identity), F-c (second 87-59
window) stand. Deficiency NOTE: no PREREG.md.
**Overturned/promoted by:** a preregistered W-cest battery + 24="en"
confirmation + 38's identity + a second 87-59 window.

### R-009 — Liaison: BANK

**Claim:** status table + constraints memo v2 + unblock plan; no
main-fleet action required.
**Evidence:** read-only memo; Experiment 0 6/6 SLIDE and judge-instrument
acceptance 6/6 FAIL relayed from disk with sha256/log cross-checks;
round-14 restructured registry relayed as solver constraints.
**Ruling: BANK** — constraints memo v2 banked per round-9/10/11/12/13
precedent (memos are constraints, not verdicts). Main-fleet search scope
stays ZERO until C1 passes (standing). No status change.

---

## Scoreboard after round 14

12 values (7 pencil GT + 87=ce/64=qui/96=par/59=est provisional +
77="le" provisional-conditioned) — **unchanged; 0 promotions (bar held an
eleventh round).** Deltas: 81="prin" LEAD **killed** (81 UNIDENTIFIED);
78 fork **resolved** (ver-initial / er-at-er|ne, F33-form); 74 =
syllable-class (word-class fenced); registry rewrite **adopted**;
@460 second tout-frame banked (79="tout" promotion lane); W-cest fenced
candidate; 3 prereg deficiencies noted for future batteries.
