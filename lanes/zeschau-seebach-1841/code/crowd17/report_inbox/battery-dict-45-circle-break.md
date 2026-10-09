# Battery report: dict-45-circle-break

- Target id: `dict-45-circle-break`
- Claim: "45='dict'-syllable gets an independent leg at the 01-free post-78 windows (@313, @573, @1165)"
- Date: 2026-10-08
- Worker: battery worker (session fc0be7db-7e25-4d0c-849c-086dddaee7d4)
- Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json +
  data/upstream-ct_R5005.txt, parsed per code/side-keyhunt/repair_parse.py;
  re-derived in-session: 1,847 pairs / 96 types confirmed).
  `canonical.py` never used. R5005, sealed gates, red-team adjudication queue untouched.
- Lock: code/crowd17/next-token/locks/dict-45-circle-break.lock (created at start,
  deleted at end; no prior lock existed).
- Scope: the three 01-free post-78 windows. W3 (@982) excluded per the chartering
  report's circularity finding; not re-tested here.

## Bar (verbatim, pre-registered before testing)

"resolve iff all three compose as ver+dict-syllable with stated follower parses (64='qui' promoted; 13-55-61 per dict-frame-78-45-13-55-61 — coordinate, do not re-run); kill iff any window forces non-dict"

Numbered pass/fail clauses (restated before testing, not modified after):

1. @313 (W1): composes as ver+dict-syllable with the stated follower parse
   64='qui' (promoted).
2. @573 (W2): composes as ver+dict-syllable with the stated follower parse
   13-55-61 per dict-frame-78-45-13-55-61 (coordinated, not re-run).
3. @1165 (W4): composes as ver+dict-syllable with the stated follower parse
   13-55-61 per dict-frame-78-45-13-55-61 (coordinated, not re-run).
4. Kill: kill iff any window forces non-dict.

## Method

1. Re-derived the repaired stream in-session (1,847 pairs, 96 types).
   78-45 loci: @313, @573, @982, @1164. n(45)=22. Post-78 45 followers:
   {64, 13, 01, 13}. 13-55-61 occurs only at @575 and @1166.
2. Windows re-derived, not cited from memory:
   - @307-319 (row a2_04): `20 17 46 84 24 37 | 78 45 | 64 59 32 94 06 11 92`
   - @567-579 (row a3_02): `13 76 45 94 52 87 | 78 45 | 13 55 61 94 82 06 06`
   - @1159-1171 (row a6_09): `82 44 83 21 67 | 78 45 | 13 55 61 94 87 83`
3. Coordinated (not re-run): dict-frame-78-45-13-55-61 (null),
   dict-78-45-wordbound (null, boundary verdict), verdict-w2-574-gate
   (promote, W2 one-word boundary), dict-45-ce-rival-1165 (null, W4
   double-residual), battery-w1-314-ambig (null, in report_inbox).
   Standing values used: §7 banked (11=la, 70=pre, 82=m, 34=i, 29=er, 40=e,
   46=que) and granted (87=ce, 64=qui, 96=par, 17=fois, 79=tout, 00=pour,
   84=on, 47=ce allophone-tier); 78='ver' is LEAD (R16-005), not settled;
   A11 45='ce' HOLD stands; 67 et/veut sole true polyvalence.

## Window-level evidence (@-offsets are 0-based pair indices in the repaired stream)

### @313 (W1): 'verdict qui' composes — conditionally

- One-word: "...[37] verdict qui est [32]..." — 64='qui' promoted (stated
  follower parse holds), 59='est' provisional, 32 predicative granted (A1).
  Full local composition available.
- Two-word: "...[37] ce qui est [32]..." — fully grammatical under standing
  values (A11 mirror leg; 64 shared with standalone 45-64 @340/@1024).
- dict-78-45-wordbound fenced W1 as the two-word EXCEPTION: the contact
  profile is silent on W1 (64 is profile-neutral), so the boundary cannot
  decide it. W1's one-word reading stays conditional on the unsettled
  78='ver' LEAD + the 45='dict' lead — the same mutual conditionality the
  w3-ceci report diagnosed.
- Grade: CONDITIONAL. The window composes, but as an A11-held two-word
  window with a conditional one-word alternative. It cannot serve as an
  independent dict leg while A11's exception stands.

### @573 (W2): 'ce verdict [13-55-61]' composes — conditionally

- verdict-w2-574-gate promoted the one-word boundary: 87='ce' granted +
  78-45 one word; the two-word parse ("ce ver ce") is impossible under
  78='ver' and under every non-ver 78 value. 94-82 = 'ne m'' elision frame.
- Per dict-frame-78-45-13-55-61 (coordinated): the 5-gram is byte-identical
  x2; 13-55-61 occurs nowhere else; 13->55 occurs ONLY in the two 5-grams.
  But clause 1 of that battery FAILED: 13-55-61 is unnameable as one French
  unit (scattered contact profiles; W1's "ne mentent" subjectless). The
  follower parse is therefore POSITIONAL, not lexical: the trigram is a
  post-78-45-exclusive unit, not a named French word.
- The 'verdict' value reading stays conditional on the unsettled 78='ver'
  LEAD (R16-005) — the w3-ceci mutual conditionality persists here.
- Grade: CONDITIONAL. Composes under the LEAD with a positional (unnamed)
  follower parse. Not independent of 78.

### @1165 (W4): does not compose at battery level

- dict-45-ce-rival-1165 (coordinated): W4 is a DOUBLE-RESIDUAL.
  Reading 1 ('et verdict [13-55-61]'): bare countable noun 'verdict' in
  argument position with no determiner — ungrammatical at kill grade
  WITHIN THE TWO-TOKEN SCOPE (no period zero-determiner construction
  applies). Reading 2 ('et vers ce [13-55-61]'): needs 2 non-granted
  assumptions (78='vers' + 13-55-61 nounhood); budget was <=1.
- The 5-gram-unit escape belongs to dict-frame-78-45-13-55-61, which
  nulled on naming (this target was told to coordinate, not re-run).
- Right edge @1169-1170 = '94 87', stream-unique (1/1,847), 'ne ce' under
  94='ne' STRONG LEAD — owned by queued ne-ce-1169, not re-litigated here.
- Grade: FAIL at battery level. The window cannot compose as
  ver+dict-syllable within battery scope. This does NOT force non-dict:
  the ce-rival battery recorded the double-residual as conditional on the
  unsettled 78='ver' LEAD (per the fork-78-45 precedent, an unfired
  conditional is null, not kill), and the 5-gram unit escape is fenced
  elsewhere, not falsified here.

## Per-clause pass/fail

1. @313 composes as ver+dict-syllable with 64='qui': CONDITIONAL PASS
   ('verdict qui est [32]' composes; 'ce qui est [32]' also clean and is
   the standing A11 two-word exception — contact profile silent).
2. @573 composes as ver+dict-syllable with 13-55-61 follower: CONDITIONAL
   PASS (one-word boundary promoted; value conditional on unsettled
   78='ver' LEAD; follower parse positional, unit unnameable per
   dict-frame — coordinated, not re-run).
3. @1165 composes as ver+dict-syllable with 13-55-61 follower: FAIL
   (double-residual: two-token 'verdict' reading kill-grade within
   two-token scope via determiner gap; 'vers ce' reading over budget;
   5-gram escape fenced to dict-frame's null).
4. Kill clause ("kill iff any window forces non-dict"): NOT MET. @313's
   exception is ambiguity + fencing, not forcing. @573's boundary promotes
   the one-word reading. @1165's residual is explicitly recorded
   conditional on the unsettled 78='ver' LEAD — unfired conditionals are
   null, not kill, per the fork-78-45-adjudication precedent. No window
   forces non-dict on 45.

## Adverses

1. A11 45='ce' HOLD — positional allophone account (which windows each
   value owns), STATED not declared (§7 reserves declarations for red team):
   - 'ce' owns: all 18 standalone windows (followers {93x3, 23x3, 28x2,
     64x2 @340/@1024, 91, 54, 88, 46, 94, 08, 58, 36}); W1 @314
     (two-word exception — 'ce qui' mirror leg, A11 keeps all three
     mirror legs @314/@340/@1024); W3 @983 fenced under the w3-ceci
     circularity (conditional, excluded here).
   - 'dict'-syllable owns: @574 (W2; one-word boundary promoted,
     value conditional on 78='ver' LEAD); @1165 (W4; residual — neither
     two-token reading parses at battery level, fenced pending red-team
     polyvalence decision); @983 (W3; circular, excluded).
2. dict-78-45-wordbound boundary (coordinated, not re-run): boundary holds
   at W2-W4 with W1 as the two-word exception — consistent with every
   clause grade above. The value-arm ('verdict') waits on ver-78; the
   positional declaration is already escalated to the red team by that
   battery. verdict-w2-574-gate's 1/22 kill-scope (@574) for 45='ce' is
   respected.

## Verdict: NULL

Headline: the independence the claim needs is nowhere available — all
three windows' dict readings run through the unsettled 78='ver' LEAD,
extending the w3-ceci circularity finding to W1/W2/W4. The bar's resolve
condition ("all three compose") is unsatisfied: clause 3 fails at battery
level and clauses 1-2 are conditional on unsettled leads. The bar's kill
condition is not met: no window forces non-dict. Promote is blocked on
three independent grounds: (i) @1165's double-residual; (ii) the
positional allophone declaration is red-team territory per §7 (67 sole
true polyvalence) and is already escalated; (iii) promoting 'dict' at
@313 would override A11's standing two-word exception, violating the
never-downgrade rule.

No standing red-team verdict is contradicted or downgraded: R16-005 LEAD
respected, A11 HOLD untouched (all three mirror legs preserved),
verdict-w2-574-gate's boundary scope respected, the fork battery's
unfired-conditional precedent followed. No new escalation beyond the
existing ver-78 / fork-78-45 / ne-ce-1169 red-team items.

## Follow-up targets (null regenerates work; all absent from queue, verified 2026-10-08)

1. **dict-313-w1-adjudicate** (priority 2). Claim: @313's parse is decided
   between 'ce qui' (A11 two-word exception, standing) and 'verdict qui'
   (one-word, conditional on 78='ver' LEAD + 45='dict' lead). Bars:
   (a) parse @305-322 under both readings with the left edge '84-24-37'
   (84='on' granted A15) and the right edge '64-59-32' (59='est'
   provisional, A1 predicative) — the reading needing fewer ungranted
   assumptions wins; (b) if tied, fence @314 as A11's 'ce' with no verdict
   change (never-downgrade) and record ver-78's resolution as the gate
   that flips it; (c) coordinate with rpos-w1-exception (queued — owns the
   refined R-pos framing; do not duplicate). Evidence: this report's
   clause-1 finding. Adverses: 64='qui' promoted; contact profile silent
   on W1 (dict-78-45-wordbound — cite, do not re-run).
2. **dict-independence-census** (priority 2). Claim: the independence test
   this target was chartered for. Bars: (a) census all four post-78
   45-windows for evidence bearing on 45='dict' that is NOT conditional
   on 78's value (syllable-positional constraints, follower morphology,
   host inventory) — cite verdict45-value and dict-45-host-inventory
   (both queued) for the host question, do not re-run them; (b) name >=1
   window whose dict reading is supported by 78-independent evidence, or
   record the independence failure with stated scope; (c) declare nothing
   (§7). Evidence: this report (mutual conditionality extended to
   W1/W2/W4). Adverses: 78='ver' is LEAD (R16-005) — all conditional
   support stays labeled; ver78-45-dependency-gate (queued) owns the
   red-team gate.
3. **allophone-45-scoping** (priority 3). Claim: full positional-allophone
   account for A11. Bars: (a) enumerate all 22 windows of 45, assign each
   to 'ce' or 'dict'-syllable (or fenced residual) with per-window parse;
   (b) the account holds iff the assignment matches the {13,01}-exclusivity
   partition with <=2 fenced residuals and preserves A11's three mirror
   legs (@314/@340/@1024); (c) gather only — the positional declaration
   stays escalated to the red team, no battery-level declaration.
   Evidence: this report's adverse-1 account. Adverses:
   boundary-45-exclusivity-sensitivity (queued — exclusivity robustness
   owned there); §7 sole-polyvalence.

## Reproducibility

Stream re-derivation: `code/side-keyhunt/repair_parse.py` (`load_rows` +
`parse` with `repaired_offsets.json`), run in-session 2026-10-08: 1,847
pairs / 96 types; 78-45 loci @313/@573/@982/@1164; n(45)=22; post-78
followers {64, 13, 01, 13}; 13-55-61 only at @575/@1166. Windows dumped in
Method §2 above. No writes outside this report, the queue edit (own entry
only, via flock), and the lockfile (deleted).
