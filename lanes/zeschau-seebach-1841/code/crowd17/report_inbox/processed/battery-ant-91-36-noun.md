# Battery report: ant-91-36-noun — verdict: KILL

- Worker session: 010ebf28-22d0-4b3e-9c04-8c235ca28191
- Date: 2026-10-09
- Lock: `code/crowd17/next-token/locks/ant-91-36-noun.lock` created on start
  (2026-10-09T13:30:06Z; agent id + UTC timestamp inside), deleted on completion.
- Stream: repaired 1,847-pair parse re-derived in-session from
  `code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`,
  parsed per `code/side-keyhunt/repair_parse.py` (asserts held: 1,847 pairs,
  96 types). `canonical.py` never used. R5005 never touched. Sealed gate
  instances untouched. Red-team adjudication queue untouched. No data invented.
- Coordination: sibling battery `ant-54-605-noun` works 54 at @605-608 in
  parallel — different locus (@36-38 here); only this target's queue entry
  was touched.

## Bar (verbatim from battery-queue.json — pre-registered BEFORE testing)

"promote iff a noun-class 91 parses the antecedent slot with zero new assumptions."

## Numbered clauses (fixed before the stream census, not modified after)

- **C1 (class arm):** 91's noun-class is licensed at battery grade — i.e.,
  battery-grade evidence names 91 noun-class, so that the class assertion is
  not an invented value. This is what answers the adverse.
- **C2 (slot arm):** with 91 as noun-class, the antecedent slot
  "...[91] à qui..." (@36-38) parses with zero new assumptions — no
  standing-value conflicts, no extra ungranted moves.
- **Verdict rule:** promote iff C1 and C2 pass and the adverse is answered;
  kill iff a clause fails at kill grade (a window forces the claim false, or
  a distributional test rejects at the lane's standard).

## Method

1. Read `BATTERY-PROTOCOL.md` in full. Created the lock on start.
2. Re-derived the repaired stream byte-exact per `repair_parse.py`.
3. Re-derived 91's full census in-session (n=21, positions byte-exact).
4. Adopted as premises, not re-litigated (§7 and standing batteries):
   64=qui granted; 39=à allophone-tier lead (a-39 PROMOTE); 84="on" A15
   granted with conditions C1-C3; 47="ce" granted (A4); 11=la banked pencil;
   45="ce" A11 HOLD; 67 et/veut sole true polyvalence; R24 (24='en' iff
   follower=85, else finite/modal verb); val-91-pp-adj PROMOTE (91=past
   participle, locus-level @537/@1370, 2026-10-09); noun-74-census
   kill-grade precedent for "on [X]" frames; det-91-81-agree-test KILL
   (la-frame route for 91 dead).

## Window-level evidence (@-offsets, 0-based, repaired stream)

**Locus @36 (row a1_01):** `64 32 01 08 91 39 64 41 01 24 88 43`
(@32-@43) = `qui(64) [32] [01] [08] [91] à(39) qui(64) [41] [01] [24] [88] [43]`.
The claim's frame: 91 at @36 immediately left of "à" @37 / "qui" @38.

**91 census (re-derived, n=21).** Positions:
[15, 36, 137, 247, 256, 277, 301, 387, 390, 520, 538, 723, 852, 1005, 1019,
1371, 1428, 1518, 1668, 1698, 1798].
Predecessors: {45:1, 08:1, 23:2, 66:2, 01:1, 84:1, 86:1, 43:1, 62:1, 70:1,
16:2, 03:1, 67:1, 47:1, 63:1, 11:1, 06:1, 37:1}.
Successors: {53:2, 39:1, 65:2, 32:2, 37:1, 18:1, 36:1, 84:1, 77:1, 12:1,
51:1, 11:2, 67:2, 61:1, 85:1, 79:1}.
(Cross-check: n=21 and the successor multiset match antec-08-91-39's
independent census byte-exact.)

**Noun-shaped windows (recorded honestly — the signal that motivated this
battery).** Three independent determiner/demonstrative-preceded windows:
- @15 (a1_00): `62 98 76 45 91 53 17 64 98` — pre=45 ("ce", A11 HOLD).
- @1005 (a6_02): `00 86 56 47 91 11 52 35 18` — pre=47 ("ce", granted A4).
- @1518 (a7_11): `88 11 31 11 91 67 08 31 24` — pre=11 ("la", banked).
Plus verb-adjacent subject-shaped windows @247 (`66 91 32`) and @256
(`01 91 32`), both "[X] [91] [32-verb]".

**Kill window @277 (row a2_03):** `33 29 89 84 91 37 61 20 61`
(@273-@281) — "...[89] on(84) [91] [37]...".
84="on" is A15-granted. In 1841 French a subject pronoun "on" is followed
by a verb (or adverb+verb); a bare noun directly after "on" is
ungrammatical. Surviving classes for 91 at this window: finite verb or
adverb — both non-nominal. Per the lane's noun-74-census precedent, an
"on [X]" frame is a kill-grade contradiction of X's noun-class ("@261
'on [74] ce': 'on'(A15) + bare noun — ungrammatical; 74 != noun").
Caveat fenced with stated cause: A15's conditions C1-C3 could in principle
exclude @277, but no battery has done so — the same caveat the lane
accepted when it killed noun-74.

**Standing-state block on the promote arm.** val-91-pp-adj (PROMOTE,
2026-10-09) names 91 = past participle at the 16-91 windows @537/@1370
(locus-level). Battery level declares no polyvalence (§7: 67 et/veut is the
sole true polyvalence). A noun-class 91 at @36 alongside pp-91 at
@537/@1370 would be undeclared polyvalence — red-team territory, not
battery grade. The promote arm is therefore blocked independent of @277.

**Fenced residual (not a kill leg).** @387 (a2_07): `43 91 36` — "[43] [91]
[36]". A bare "N N" juxtaposition reading would be a second anti-nominal
signal, but 43's noun standing was not verified in-session, so this window
is fenced, not fired.

## Per-clause results

- **C1 — FAIL AT KILL GRADE.** @277 ("on [91]") forces non-nominal under
  the lane's own precedent; one kill-grade contradiction caps the class
  claim (noun-74 precedent: the bar needs zero contradictions). The three
  determiner-preceded windows are real distributional signal, but signal
  does not survive a kill-grade contradiction. Separately, the standing
  pp-promote for 91 blocks noun-class without red-team polyvalence.
- **C2 — passes conditionally, moot.** With 91 as noun-class, "...[91] à
  qui..." parses clean under standing values: @37=39 (à, allophone lead),
  @38=64 (qui, granted); the relative clause has its predicate (@41=24 is
  finite/modal per R24, follower @42=88 not 85); no neighbor conflicts.
  But C2's condition (C1) is dead, so the slot arm cannot fire.
- **Adverse ("naming 91 a noun would otherwise be inventing a value
  (§3)") — CONFIRMED, not answered.** No battery-grade route licenses the
  class assertion; the @277 window actively forbids it.

## Verdict: KILL

91 is not noun-class at battery grade. The "…[91] à qui…" antecedent frame
for qui @38 cannot be licensed through a noun-91; the parent battery's
fence (qui-38-608-aqui NULL: antecedent unnameable) stands unreopened by
this route.

No standing or red-team verdict contradicted or downgraded: this kill
agrees with val-91-pp-adj's PROMOTE (91=past participle, locus-level) and
with det-91-81-agree-test's KILL; no red-team verdict on 91 exists. §7
intact (67 remains sole polyvalence). Canonical-stream caveat stands (row
a1_01 offset unvalidated per protocol).

## Follow-ups (optional — verdict is KILL, so §4 requires none; one
discriminating residual proposed, verified ABSENT from battery-queue.json)

1. `verb-91-277-frame` (P3) — name 91's class at the @277 "on [91]" window:
   the kill leg forces 91 into a verb/adverb-compatible class there; test
   finite-verb vs adverb using @277 plus 91's other verb-shaped windows.
   Bar: promote verb-class iff >=2 independent "on/modal + [91]" frames
   parse with 91 as the finite verb and zero forced contradiction; kill
   verb-class iff any window forces non-verbal. Evidence: @277 (a2_03)
   `33 29 89 84 91 37 61 20 61` ("on [91]", 84="on" A15 granted); control
   windows @247 (a2_02) `56 43 00 66 91 32 44 94 65` and @256 (a2_02)
   `63 00 66 01 91 32 43 77 84` (91 in pre-verbal subject slot before
   32=[verb,cls]). Adverses: A15's C1-C3 could in principle exclude @277
   (fenced, unexamined in-session); 91's locus-level pp naming at
   @537/@1370 does not decide the global class (no polyvalence declared at
   battery level — red-team territory).

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-ant-91-36-noun.md` (this file).
- Queue: `ant-91-36-noun` → status `verdict`, result `kill`, 2026-10-09
  (pre-write assert passed — was queued/verdictless; temp-file + rename;
  JSON re-validated; own entry only; no downgrade).
- Lock `code/crowd17/next-token/locks/ant-91-36-noun.lock`: created on start,
  deleted on completion (verified gone).
