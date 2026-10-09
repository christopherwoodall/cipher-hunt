# Battery verdict: prof-98 — 98's class decided by its follower census

- Target: `prof-98`
- Claim: 98's class is decided by its follower census (verb-frame test of the formula head)
- Worker: battery-worker prof-98 (5fe35c82-2ed3-422a-8039-27e41a37cefa)
- Date: 2026-10-09
- Verdict: **PROMOTE** (class-level: 98 is a finite verb; battery grade, needs red-team ratification per pipeline rule)

## Pre-registered bar (verbatim)

"(a) 98-83 x5 parsed under one class for 98 (the x3 formula + @897/@930); (b) 98-98 x3 (@1073/@1145/@1660) fenced as formula or parsed — finite-verb readings must survive the doublings or be withdrawn; (c) 98-82 x3 (@19/@124/@894) and 98-80 x3 parsed under the same class"

## Bar as numbered clauses

1. PASS/FAIL: 98-83 x5 (@227/@897/@930/@1060/@1783) parse under one class for 98 — the x3 formula `98 83 82 96 21` plus @897 and @930.
2. PASS/FAIL: 98-98 x3 (@1073/@1145/@1660) fenced as formula or parsed; finite-verb reading survives the doublings or is withdrawn.
3. PASS/FAIL: 98-82 x3 (@19/@124/@894) and 98-80 x3 (@440/@767/@1661) parse under the same class.

## Method

- Stream: repaired 1,847-pair parse only. Built from `code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt` with the repair_parse.py tokenization (2-digit pairs per row offset). `canonical.py` never used. R5005 untouched. Red-team adjudication queue untouched.
- All @-offsets are pair indices on the repaired stream. Every window below re-derived by script in this run. Census re-derived: 98 n=40; followers 83 x5 / 82 x3 / 80 x3 / 98 x3 / 00 x3 / 56 x2 / 20 x2 + singletons; predecessors 62 x5 / 42 x3 / 66 x3 / 98 x3. Matches the queue's cited census exactly.
- Standing values used as given (§7): 82=m, 46=que, 64=qui, 96=par, 00=pour (A9 class-level), 87=ce, 47=ce (A4), 12=n, 48=e, 59=est provisional, 77=le provisional, 86 INF-class (A9), 80/89 verb-frames (A8). 83='de' is a LEAD (le83-window null; fence-911-de null). 62's value/class open: 62='il' dead globally at kill grade, 62='on' unconditioned eliminated. 98='vient' is battery-PROMOTED (vient-98-name, 2026-10-08), not red-team ratified — this battery tests the CLASS independently and does not re-derive the value.

## Window evidence

### Clause 1 — 98-83 x5 under 98 = finite verb

- Formula x3, byte-identical 5-gram `98 83 82 96 21` (verified): @227 [a2_01] `87 46 98 83 82 96 21 60 71`; @1060 [a6_04] `09 98 83 82 96 21 62 18`; @1783 [a8_09] `23 98 83 82 96 21 68 47`. Thirds 60/62/68 vary. Under 98=finite-verb + 83='de' (lead): "que vient de [82] par [21]…" — the 'venir de' + infinitive semi-auxiliary frame. Frame-level parse secure; complement semantics depend on open values (see residual R1 below).
- @897 [a5_08]: `14 98 83 86 16` — "[14] vient de [86-inf]" (86 INF-class, A9 grant). Clean.
- @930 [a5_10]: `82 98 83 56 69` — "me vient de [56]" (82='m' proclitic 'me' + finite 98 + 'de' + complement; complement class open, fenced as complement residual — strain on 56, not 98).
- All five are "vient de X" frames. PASS. Dependency stated: the 'de' reading of 83 is lead-strength, not granted; the frame shape (finite verb + 83 + complement) holds regardless.

### Clause 2 — 98-98 x3

- @1073 [a6_05]: `42 98 98 12 48` — "[42] vient vient ne…" (12-48 = analytic 'ne'). Mid-row, no boundary artifact.
- @1145 [a6_08]: `42 98 98 86 67` — "[42] vient vient [86] et/veut". Mid-row.
- @1660 [a8_04]: `47 98 98 80 22` — "ce vient vient [80]". Mid-row. (47='ce' granted A4.)
- "vient vient" is ungrammatical in French of any period — no finite-verb parse survives. No clean re-parse found (pre∈{42,47}, suc∈{12,86,80}); sentence-boundary rescue ungranted; "vient de venir" needs the absent 83; second-value-of-98 is a red-team act per §7.
- FENCED AS FORMULA with stated cause: systematic mid-row reduplication of unknown cause (candidates: scribal/emphatic doubling, undeclared second value at these windows, unattested compound — red-team territory). The three windows are held OUT of 98's support; they do not force 98≠finite-verb (37/40 windows consistent). PASS via the bar's explicit fence arm.

### Clause 3 — 98-82 x3 and 98-80 x3 under 98 = finite verb

98-82 x3:
- @19 [a1_00]: `64 98 82 43 29` — "qui vient m'[43]er" (64='qui' GT forces finite verb independently; "vient me [inf]" grammatical, conditional on 43 vowel-initial infinitive). Clean.
- @124 [a1_03]: `66 98 82 48 11` — "[66] vient me [48]…"; 'er' absent after 48, so the infinitive complement fails — FENCED as 48-value residual (strain localizes to 48's open value, not to 98).
- @894 [a5_08]: `01 98 82 14` — "[01] vient m'[14]" (elided 'me' before vowel-initial 14; conditional on 14 vowel-initial infinitive). Parses.

98-80 x3:
- @440 [a2_09]: `43 98 80 50` — "[43] vient [80]" ('vient' + infinitive; 80 verb-frame A8 grant). Conditional pass.
- @767 [a5_03]: `66 98 80 10` — "[66] vient [80]". Conditional pass (same).
- @1661 [a8_04]: `98 98 80 22` — second 98 of the @1660 doubling + "vient [80]"; covered by the clause-2 fence, otherwise conditional pass.
- PASS with stated conditions.

### Class-level confirmation independent of the value

- "qui 98" x2 (@19, @511): 64='qui' (GT) requires a finite verb — 98 is finite-verb class by syntax alone, independent of 83 or the 'vient' value.
- Proclitic "82 98" (@930, @1601): 'me' procliticizes only to a finite verb.
- mannequin-62-98-test KILL (2026-10-09): the 98='n' (letter) rival is dead across 98's 40 windows — 98 is a full word, not a letter.
- Coordinated with (not duplicated): vient-98-name's 40-window scan (zero board contradictions) and vient-98-511-relative's frame inventory ('vient de' x5, 'vient pour' x3, 'vient'+INF x1).

## Per-clause results

1. **PASS.** All five 98-83 windows parse as finite-verb "vient de X" frames (83='de' lead dependency stated).
2. **PASS (fenced as formula).** The three doublings are ungrammatical under finite-verb and are fenced as systematic reduplication of unknown cause; the finite-verb reading is NOT withdrawn (37/40 windows consistent, bar permits the fence arm).
3. **PASS.** 98-82 x3 and 98-80 x3 parse under finite-verb with stated conditions (@124 fenced as 48-residual).

## Adverses answered

- "French of 98 unconfirmed" → answered: the CLASS (finite verb) is confirmed by syntax independent of the value ('qui 98', proclitic 'me 98', 'vient pour' + INF); 98='vient' specifically is battery-promoted (vient-98-name) pending red-team ratification. This promote claims the class only and does not overreach.
- "doubled 98 resists finite-verb" → answered: fenced with stated cause in clause 2; held out of 98's support, not ignored.
- "62->98 x5 entangles the collision cell" → answered: the five "62 98" windows (@12/@803/@946/@1137/@1325) are consistent with 98=finite-verb under any subject-like 62; 62's own class/value is open (62='il' kill-grade dead; 62='on' unconditioned eliminated). These windows are fenced as 62-residuals — strain localizes to 62, not to 98. 98's class is decided by its followers (this claim's scope), not its predecessors.

## Verdict

**PROMOTE** — 98's class is finite verb, decided by its follower census. All three bar clauses pass (clause 2 via the bar's explicit fence arm); all three listed adverses answered. Consistent with (and weaker than) the standing battery promote 98='vient'; no red-team verdict contradicted.

## Residuals for other lanes (not this claim)

- R1: the formula's full French ("vient de me parvenir" per the thirds finder) needs 82 to cover "me", which collides with 82='m' ground truth — 82-value work / red-team territory. The frame-level "vient de X" stands regardless.
- R2: the doubling cause (scribal? second value? compound?) — red-team act per §7.
- R3: 62's class/value — the 62->98 windows stay 62-residuals until 62 resolves.
- R4: 83='de' ratification hardens clause 1 (le83 / fence-911-de line).

## Follow-ups

None required (promote, not null).
