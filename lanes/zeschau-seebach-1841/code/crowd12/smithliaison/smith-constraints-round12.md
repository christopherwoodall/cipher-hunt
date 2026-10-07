# Smith constraints — Round-12 DELTA memo (2026-10-07)

Liaison (smith_liaison), round-12 work order 8. Read-mostly liaison; no
Smith work duplicated, nothing on the Smith's side changed. Main-fleet
search scope stays ZERO — no joint search run, none recommended beyond
scope-ZERO maintenance.

**Carry-forward:** `code/crowd10/liaison/smith-constraints.md` (full spec,
STANDS) + `code/crowd11/smith_liaison/smith-constraints-round11.md`
(DELTA over it, STANDS). This memo is a DELTA over the round-11 memo:
(1) rebuild-side execution state since F78, (2) round-11 adjudication
outcomes (RULINGS-ROUND11 R1–R7, docket CLOSED 7/7, 2026-10-07) as new
scorer constraints. The future joint scorer must respect all of it.

## 1. Rebuild-side state delta since F78: NONE

Verified from disk 2026-10-07 ~16:20 CDT (`code/side-homophonic-rebuild2/`):

- **Track A (register-gap diagnostic): still GO, still not executed.**
  Files unchanged since 2026-10-07 19:21–19:23 (PREREG.md, build_ref.py,
  rescore_reg.py, lm_ref_diplo/). No `results/` dir. Step-3 sanity +
  diagnostic rescore not run. Unaddressed: R4a — `rescore_reg.py` prints
  "MISMATCH -- STOP" on sanity fail but CONTINUES; hard-exit (`sys.exit(1)`)
  required before any diagnostic verdict prints.
- **Track B (neural char LM): still GO, still not executed.** `track-b/`
  holds PREREG.md only (19:25:57) — no training, no code, nothing built.
  The 9-step order cleared at R5 with the binding cross-track constraint R5b
  (exclude guizot-memoires-t5-t6.txt word offsets [100000,104000) and
  [200000,204000) per Track-A tokenization, pre-tokenization, logged in
  `manifest.json`; overlap > 0 ⇒ run VOID). Unaddressed: R5a — 8-gram
  hit-table inconsistency ("13 hits" text vs table summing 14;
  metternich-v6 4 vs 5).
- **Track C (word-boundary inference): still GO, still not executed.**
  PREREG.md, build_decodes.py, decodes.json, word_stats.py/json,
  word_vocab.json all unchanged since 2026-10-07 19:18–19:22. §4 hygiene
  gate (15-gram Les-Mis scan, KILL at >5) not run; `score_boundaries.py`
  not written. Unaddressed: R3a — PREREG:83 C typo (1,717,930 → 1,717,960;
  `word_stats.json` is the machine authority); R3b — B(D) is a raw total,
  not length-normalized; report W_uni/W_len/W_bnd; the §6 300-cell pilot
  (requires PROMISING, M ≥ +800) is the behavioral arbiter.
- **Red team:** `redteam/RULINGS.md` unchanged (19:30:40). No new rulings,
  no round-12 red-team actions. Tally still 0 KILL / 0 DEMOTE / 3 GO.
- **Fleet PREREGs still do not cite the liaison memos** — consistent with
  the diagnostic charter: cleared steps touch no R5005-derived values; the
  §2 constraints below are prospective for the future joint scorer.

## 2. Round-11 adjudication deltas → banked as scorer constraints

All are R5005-main-fleet rulings (RULINGS-ROUND11, R1–R7) the future joint
scorer must respect. Baseline is now 132/132 R10BANK + 89/89
ROUND10-LEDGER PASS + R11BANK/ROUND11-LEDGER applied (R3/R5/R6 status
changes; R6's V-1519b VOID; @863 follow-up note; R1/R2/R4 holds).

### C-R11-1 — ISLET 3 tightened: 06="ent" iff pre=82 (R1 / F77)
All three 06 falsifiers UNFIRED — FIRE-PART (82→06 census
[580,738,1184,1355] exact), FIRE-IN, FIRE-OUT (0/40 pre≠82 06-windows
under the ISLET-10-tightened by-ear rule). ISLET 3 stands, LEAD
conditioned, n=4/n_eff=3. **Scorer must respect the iff:** 06="ent"
ONLY under pre=82 — no unconditioned 06="ent" readings, no new pre
admissions without a fresh falsifier battery. Correlated data point:
the @1355 «ne ment pas» gloss is rare-but-real in the diplomatic genre
(3.96M diplomatic corpus attests «ne ment pas»=1); Nesselrode v8's 54
"ment" tokens are archive.org OCR word-splits — v8 phrase zeros are VOID
as French. A scorer's French model must not let Les-Mis register priors
veto the diplomatic-genre reading.

### C-R11-2 — 33 = infinitive-class (R3 / F79)
C1 PASS, three independent infinitive signature kinds: I1 pre==00 ×8
(@186/@408/@467/@846/@936/@1088/@1245/@1630), I4 suc==29 ×5, I2
pre==67 ×1; nominal signatures effectively zero. Window-level
re-derivation byte-exact on all 23 in-census windows. Census facts:
n33=25, 00→33×8, 33→29×5. @1450/@1623 → lean-veut per the F74 decider,
grade capped LEAN (lane ≥2-check rule). **67 stays provisional; the 67
et/veut fork stays SUPPORTED.** Scorer constraint: 33 must be scored as
infinitive-class; the "pour 33" frame is now an 8-instance construction
(00="pour" context), and 33→29 is a 5-instance successor pattern.

### C-R11-3 — -este verb: no single value; 84 polyvalent-or-split (R4 / F80)
H0 holds — the -este verb stays set-valued
{manifeste, atteste, proteste, conteste, déteste}. a3-monovalence banked
as data: for all five, stem@1447 ∉ by-ear mid-options@1189 ⇒ **84 is
polyvalent across these windows OR @1190's verb ≠ @1448/@1804's.**
77→84 ×7 (3× «qui le [84]»). @1291↔@1804 share a byte-identical 5-mer
suffix [35,94,52,80,4] (fenced-lean support for @1291's verb parse;
conditional discriminator narrows to {manifeste, proteste} under
verb-parse + [35]=subject). **Scorer constraint: 84="este"-verb must be
scored set-valued — no single -este ID enters any objective as a fixed
target.** Tie-breakers T1–T5 are open work, not constraints.

### C-R11-4 — @1248: "peu" STRENGTHENED; double-pour stack ERA-VETO (R5 / F81)
"peu" STRENGTHENED 4/8 — P-A: 13/13 genuine «pour peu que»+subjunctive
in new corpora (11× RDM 1841, 2× Guizot despatches; no longer
hapax-anchored); P-B: construction-shape S=(verb-offset 3,
clause-length 4) matches the cipher clause. Infinitive-class
(«empêcher») stays WEAK-FENCED 3/7 (E-A: 28 distinct genuine infinitives
in «pour INF que»). **Hard era veto for the scorer: the double-pour
stack «pour 33 16 pour 67 que» has NO era license in ~16.5MB of 1840s
formal French (P-D and E-C both zero). Any decode emitting that stack is
dead on arrival.** LABEL CORRECTION (R7): the 11-token frame spans
pairs[1244:1255], not "@1244–1256" — downstream notes citing the old
label should read @1244–1254.

### C-R11-5 — @633 → et-CONDITIONAL(C1∧C2) (R6 / F82)
92:2 "l' * et" vs "l' * veut" in Nesselrode v8; L2 n(11→52)=3.
5 clean nulls; the round's only classification. Fork tally now
29 classified + 2 conditional + 5 open + 2 fenced = 38; **fork stays
SUPPORTED**. Conditional dependencies (08="l'", C2) must travel with
any reuse of this classification.

### C-R11-6 — 48 stays UNIDENTIFIED; all three paths fenced (R7 / F83)
Path A ("on 48" windows) FENCED — no S coheres; A1 0/10 is a real zero;
tension points at the premises (62="on" ear-only is the load-bearing
weak link). Path B (82="m'" premise) FENCED. Path D (48="de"-conditional,
pronoun+infinitive) FENCED with explicit missing legs: D1 LICENSED
(«de le»+INF 29/29=1.00, 19 distinct X hand-verified); @1350 OUT
(pre-registered R-c exclusion); @126 OUT (left context unlicensed);
@1076 IN-PENDING — **missing legs ML-1 (@1077 infinitive-ID) and ML-2
(pre=12 licensor-ID, adj/noun/participle per era L1)**. **Scorer
constraint: 48="de"-conditional remains the only live word-reading for
48, but it is fenced-pending two legs — no objective may treat it as
settled.** Follow-up pointer (not a leg, not a constraint yet): @863 =
48-47-46 reads «de ce que» (10× v8) — a second "de"-frame outside the
narrow path.

### C-R11-7 — Liaison precedent (R2 / F78)
Round-9 R2 / round-10 R1 precedent upheld: this memo (a liaison memo,
not a battery) is BANKED as a constraint with no adjudicated status
change. No interim kills issued at round-11 close.

## 3. Retired hazards → replacement watch-list

The round-11 memo's §4 "live questions" are ALL CLOSED at round-11 close:
-este verb ID (F80 — set-valued H0 holds), 48 successor-word anchoring
(F83 — fenced, two legs named), 33's class (F79 — infinitive-class,
@1450/@1623 lean-veut), 67 residuals (F82 — @633 classified, fork tally
38), @1248 weak arms (F81 — peu strengthened, double-pour stack
era-VETO), 06 falsifier watch (F77 — unfired, ISLET 3 stands).
Standing replacement watch-list (open work, NOT constraints yet — relay
only when rulings land):
- 48: ML-1 (@1077 infinitive-ID) / ML-2 (pre=12 licensor-ID);
  @863 «de ce que» second-frame follow-up.
- -este verb: T1–T5 tie-breakers.
- 06: the 94-82-06-06 4-gram frame hypothesis (STATE.md WO item 6;
  both suc=6 windows are islet windows, p=0.0063).

## 4. Search-scope status: ZERO, maintained

No joint search was run; none is scoped. All three tracks have GO status
but ZERO execution since F78 — Track A's sanity+diagnostic rescore, Track
B's 9-step order, and Track C's hygiene gate + 300-cell pilot are all
pending. C1 has not run, let alone passed. Main-fleet search scope stays
ZERO until C1 passes on the gapped family (STATE.md standing order;
F57 case law: the failure is in the likelihood, not the weights —
scorer reweighting within the 5-gram+lexicon family is EXHAUSTED).

## 5. Channel health

One-way disk channel intact. Red-team `RULINGS.md` unchanged since
2026-10-07 19:30:40. No new rulings, no round-12 red-team actions.
Carried-forward unaddressed non-blocking concerns: R4a (rescore_reg.py
sys.exit(1)), R5a (8-gram hit-table inconsistency), R3a (PREREG:83 C
typo — word_stats.json is authority), R3b (B(D) length-normalization).
Round-11 docket CLOSED 7/7 (RULINGS-ROUND11, ~16:15 CDT); no crowd12
packages exist yet.
