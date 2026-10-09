# Battery report: dict-independence-census

- Target id: `dict-independence-census`
- Claim: "the independence test — census all four post-78 45-windows for 78-independent dict evidence"
- Date: 2026-10-09
- Worker: battery worker (session 44de40ac-2ae8-4384-97e8-608dc6c8a694)
- Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json +
  data/upstream-ct_R5005.txt, parsed per code/side-keyhunt/repair_parse.py;
  re-derived in-session: 1,847 pairs / 96 types confirmed).
  `canonical.py` never used. R5005, sealed gates, red-team adjudication queue untouched.
- Lock: code/crowd17/next-token/locks/dict-independence-census.lock (created at
  start with agent id + UTC timestamp, deleted at end; no prior lock existed).

## Bar (verbatim, pre-registered before testing)

"(a) census all four post-78 45-windows for evidence bearing on 45='dict' that is NOT conditional on 78's value (syllable-positional constraints, follower morphology, host inventory) — cite verdict45-value and dict-45-host-inventory (both queued) for the host question, do not re-run them; (b) name >=1 window whose dict reading is supported by 78-independent evidence, or record the independence failure with stated scope; (c) declare nothing (§7)."

Numbered pass/fail clauses (restated before testing, not modified after):

1. (a) All four post-78 45-windows censused for 78-value-independent
   dict evidence across the three named types (syllable-positional,
   follower morphology, host inventory — the latter two targets cited,
   not re-run).
2. (b) >=1 window named whose dict reading is supported by 78-independent
   evidence, OR the independence failure recorded with stated scope.
3. (c) Nothing declared (§7).

## Method

1. Re-derived the repaired stream in-session (1,847 pairs, 96 types).
   n(45)=22; 45 offsets: 14, 104, 262, 314, 332, 340, 401, 437, 478, 569,
   574, 603, 678, 697, 974, 983, 1024, 1055, 1165, 1201, 1214, 1551.
   Post-78 45-windows (predecessor 78): @314, @574, @983, @1165.
2. Re-derived follower censuses: 13 (n=12), 01 (n=28), 64 (n=47), 78 (n=31),
   55 (n=12), 61 (n=18). Bigram loci: 13->55 only at {575, 1166};
   55->61 at {576, 1167, 1205}.
3. Coordinated (not re-run): dict-45-circle-break (null — mutual
   conditionality at W1/W2/W4), verdict-w2-574-gate (promote — W2 one-word
   boundary), dict-78-45-wordbound (null — boundary holds W2-W4, W1 the
   two-word exception), dict-frame-78-45-13-55-61 (null — 13-55-61
   unnameable as one French unit), dict-45-ce-rival-1165 (null — W4
   double-residual), w3-ceci (circularity at W3).
4. Cited (not re-run) per bar (a): verdict45-value (queued — "the surviving
   positive leg for 78='ver' is 'ce verdict' x2"), dict-45-host-inventory
   (queued — "closed '-dict-' host inventory: 'verdict' the sole host").
5. Standing values used: §7 banked pencil (11=la, 70=pre, 82=m, 34=i,
   29=er, 40=e, 46=que) and granted (87=ce, 64=qui, 96=par, 17=fois,
   79=tout, 00=pour, 84=on, 47=ce allophone-tier); 78='ver' is LEAD
   (R16-005), not settled; A11 45='ce' HOLD stands.

## Window-level evidence (@-offsets are 0-based pair indices)

### W1 @314: 78 45 64 59 32 ("24 37 78 45 64 59 32")

- Follower morphology: 64 follows 45 at @314, but also at @340 and @1024 —
  the A11 standalone mirror legs. The 64-follower is NOT post-78-exclusive;
  it is the shared 'ce qui' pattern. No distinctness, no naming.
- Syllable-positional: boundary fenced as the two-word exception
  (dict-78-45-wordbound) — 45 is word-INITIAL here under the standing
  fence, the wrong syllable slot for 'dict' entirely. Position evidence,
  such as it is, points away.
- Host: naming any host requires 78's value (cited targets own this).
- 78-value-independent dict evidence: NONE.

### W2 @574: 78 45 13 55 61 ("52 87 78 45 13 55 61")

- Follower morphology: 13 follows 45 at @574 and @1165 ONLY (2/2 post-78;
  no standalone 45 takes 13). 13->55 occurs only at {575, 1166}; the
  13-55-61 trigram occurs exactly 2x, both post-78-45. This exclusivity is
  78-precedence-conditional but 78-VALUE-independent. It marks post-78 45
  as distributionally distinct from standalone 'ce'-45 — i.e. evidence for
  "not-'ce'", not for 'dict'. The trigram is unnameable as one French unit
  (dict-frame-78-45-13-55-61, coordinated).
- Syllable-positional: verdict-w2-574-gate promoted the one-word boundary;
  per the circle-break coordination, the two-word parse ("ce ver ce") was
  ruled out under 78='ver' AND under every non-ver 78 value — i.e. the
  boundary finding ranges over all 78 values and is 78-value-independent.
  So 45 is word-internal at W2 independent of 78's value. But word-internal
  position cannot NAME the syllable: 'dict', or any other non-initial
  syllable, fits the slot equally.
- Host: cited, not re-run (both cited targets' claims are themselves
  78-value-conditional: 'verdict' as sole host requires 78='ver').
- 78-value-independent dict evidence: none that names 'dict'. Strongest
  value-independent findings are "not-'ce'" (distributional distinctness)
  and "word-internal" (boundary) — neither is the dict reading.

### W3 @983: 78 45 01 24 89 ("76 47 78 45 01 24 89")

- Follower morphology: 01 follows 45 at @983 ONLY (1/1 post-78; 01 n=28
  elsewhere, never after 45). Same shape as W2: 78-value-independent
  distinctness, value-neutral naming (marks "not-'ce'", not 'dict').
- Syllable-positional: one-word boundary holds per dict-78-45-wordbound
  (W2-W4) — 45 word-internal, same naming limitation as W2.
- This is the w3-ceci circularity window: excluded from independent-leg
  duty by the chartering report; not re-litigated.
- 78-value-independent dict evidence: NONE.

### W4 @1165: 78 45 13 55 61 ("21 67 78 45 13 55 61")

- Follower morphology: identical to W2 (13-follower, 13-55-61 trigram,
  both post-78-exclusive). Same verdict: value-neutral distinctness.
- Syllable-positional: one-word boundary holds (W2-W4 per the boundary
  battery); same naming limitation.
- Battery-level status is double-residual (dict-45-ce-rival-1165,
  coordinated) — neither two-token reading parses; the residual is
  recorded conditional on the unsettled 78='ver' LEAD.
- 78-value-independent dict evidence: NONE.

### Census summary across the bar's three evidence types

- Syllable-positional constraints: the only 78-value-independent positional
  fact is W2/W3/W4 word-internality (W1 is fenced word-initial). Position
  cannot name a syllable value — 'dict' is one of unbounded occupants.
  No 78-value-independent positional evidence supports the dict reading.
- Follower morphology: {13, 01} are post-78-exclusive 45-followers
  (13: 2/2 post-78; 01: 1/1 post-78; 13->55 only at 575/1166). This is
  78-value-independent but value-neutral: it supports "post-78 45 is not
  plain 'ce'" and nothing further. The 64-follower (W1) is shared with
  the A11 mirror legs and supports nothing distinct at all.
- Host inventory: cited verdict45-value and dict-45-host-inventory (both
  queued) per the bar; not re-run. Recorded: the latter's claim ('verdict'
  the sole host) is itself 78-value-conditional, so the host question
  contributes no 78-independent leg by construction.

## Per-clause pass/fail

1. (a) Census complete: all four windows examined under all three evidence
   types, every number re-derived in-session. PASS.
2. (b) No window's dict reading is supported by 78-value-independent
   evidence. The strongest value-independent findings ("not-'ce'"
   distinctness via {13,01}-exclusivity; W2/W3/W4 word-internality) do not
   name 'dict'. INDEPENDENCE FAILURE RECORDED. Scope: the failure covers
   all three bar-named evidence types at all four post-78 windows; it does
   not extend to 78-conditional support (which stays labeled per the
   adverse) and does not foreclose a future 78-value-independent naming
   argument built on the "not-'ce'" residue (see follow-ups).
3. (c) Nothing declared: no value named, no positional allophone account
   declared, no polyvalence declared. PASS.

## Adverses

1. 78='ver' is LEAD (R16-005): respected throughout — every 78-conditional
   reading stays labeled conditional; the LEAD is neither used as granted
   nor challenged. No standing verdict contradicted or downgraded.
2. ver78-45-dependency-gate (queued) owns the red-team gate: this battery
   does not touch it; the independence failure is recorded at battery
   level, below the gate.

## Verdict: NULL

Headline: the independence failure is confirmed with stated scope — at no
post-78 45-window does 78-value-independent evidence support the dict
reading. The bar's three evidence types were all censused: syllable
position cannot name a value (W1 even fenced word-initial); follower
morphology yields value-neutral "not-'ce'" distinctness ({13,01}
post-78-exclusive); the host question is 78-value-conditional by
construction (cited targets own it). This extends the dict-45-circle-break
finding: the mutual conditionality is not an artifact of the three
01-free windows — W3's 01-follower shows the same shape. Kill is not met
(no window forces the census claim false; clause 2's record-the-failure
branch was satisfied). Promote is blocked (no window named under (b)).

## Follow-up targets (null regenerates work; all absent from queue, verified 2026-10-09)

1. **dict-w2-syllable-naming** (priority 2). Claim: with 45 word-internal at
   W2 independent of 78's value (this report), the naming step is attacked
   directly — enumerate the French syllables that can occupy the
   second-syllable slot given the one-word boundary and the 13-55-61
   follower, and test whether 'dict' is forced, favored, or one of many.
   Bars: (a) candidate syllable inventory for the W2 slot under standing
   values with <=1 ungranted assumption each; (b) 'dict' wins iff it is the
   unique candidate surviving the 13-follower exclusivity; else fence with
   the surviving set named. Evidence: this report (W2 word-internality,
   78-value-independent). Adverses: 78='ver' LEAD (R16-005) — label all
   conditional readings; do not declare (§7).
2. **follower-13-01-exclusivity** (priority 3). Claim: the {13,01}
   post-78-exclusive follower partition of 45 is a robust distributional
   class leg, not a small-n artifact. Bars: (a) permutation/bootstrap test
   of the partition over the 22 windows of 45 (13: 2/2 post-78, 01: 1/1
   post-78); (b) the leg upgrades "not-'ce'" to a distributional class
   iff p<0.05 under the null of random follower assignment; else record
   the artifact verdict. Evidence: this report's follower census
   (13 n=12, 01 n=28, 13->55 only at 575/1166). Adverses: n=22 is small —
   state the power limitation in the report.
3. **w3-01-host** (priority 3). Claim: W3's 01-follower — the stream's only
   45-01 bigram — is profiled for a host in which 45 is a non-initial
   syllable other than 'dict', or the w3-ceci circularity is confirmed to
   stand. Bars: (a) census 01's 28 windows for nominal/verbal hosts
   compatible with a preceding non-initial 45-syllable; (b) name >=1
   concrete host parse or confirm the circularity fence with stated cause.
   Evidence: this report (@983 "76 47 78 45 01 24 89"; 01 never follows
   standalone 45). Adverses: w3-ceci circularity (cite, do not re-run
   without new data); 01 unvalued (§7).

## Reproducibility

Stream re-derivation: `code/side-keyhunt/repair_parse.py` (`load_rows` +
`parse` with `repaired_offsets.json`), run in-session 2026-10-09: 1,847
pairs / 96 types; n(45)=22 with offsets listed in Method §1; 13/01/64/78/
55/61 censuses and bigram loci in Method §2. No writes outside this
report, the queue edit (own entry only, temp-file + rename), and the
lockfile (deleted).
