# Battery report — orphan-1502 (resolve @1501-1507 or confirm orphan for the 33 set)

Worker: battery-worker-orphan-1502 (agent c7e0e518-341f-45e2-895e-85ad592c12a8). Date: 2026-10-08.
Lock: `code/crowd17/next-token/locks/orphan-1502.lock` created 2026-10-08T14:58:22Z, no prior lock existed; deleted on completion.
Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`), parsed per `code/side-keyhunt/repair_parse.py` (replicated, not `canonical.py`). R5005 not touched. Every count below re-derived from the stream in this run.

Scope note: this battery does NOT re-litigate the 33={dire,[X]er} set's content (owned by dire-33-set, null 2026-10-08, and erstem-33-id, null 2026-10-08). It decides ONLY the @1501-1507 window plus the orphan census.

## Bar (pre-registered verbatim, from battery-queue.json)

`resolve iff @1501-1507 parses under standing values or confirms orphan with stated cause; scan for any third orphan`

Numbered clauses (pre-registered BEFORE testing, not modified after):

1. @1501-1507 parses under standing values (33 = 'dire' or the -er stem X, all neighbors at granted/banked values).
2. OR @1501-1507 confirms as an orphan with a stated cause (which neighbor's granted value forces the break, and why).
3. Full census of all 33-windows shows no third orphan (orphan count stays at 2/25 = 8%, at or under the 10% threshold).

Standing values used: 84="on" (A15, re-derived as UNCONDITIONED by battery-collision-62-84, 2026-10-08); 12="n" letter (battery-n-e-12-48, promote 2026-10-08); 94="ne", 30="pas" (battery-promoted); 00="pour" (A9); 86 INF-class (A9); 87="ce", 47="ce" (allophone tier), 46="que", 96="par", 64="qui", 79="tout" (promoted); 29="er", 82="m", 40="e", 11="la", 70="pre", 34="i" (banked GT); 59="est" provisional; 67 et/veut positional rule (§7 sole polyvalence).

## Method

Re-parsed the repaired stream (1,847 pairs confirmed). Re-derived the @1501-1507 window and all 25 occurrences of group 33. Tested clause 1 with every standing-value parse available (direct, neighbor re-reads, clause-boundary, compound). Tested clause 2 by identifying the forcing neighbor. For clause 3, classified each of the 25 windows as stem ([X]er, inherited from erstem-33-id), whole ('dire'), or orphan, applying the lane's orphan test: a window is an orphan iff a STANDING (granted/banked/promoted) value forces a reading no set member can satisfy — open neighbors do not force.

## Window-level evidence (@-offsets are repaired-stream pair indices)

Target window @1501-1507 (row a7_11): `84 33 42 33 00 86 56` = "on [33] [42] [33] pour [86] [56]".

- @1501: 84 = "on" (granted, unconditioned per collision-62-84 battery 2026-10-08; §7 lists 84="on" as promoted).
- @1502: 33 in the set {dire, [X]er} — both infinitives.
- "on" + infinitive is ungrammatical in French; "on" requires a finite verb. Parse attempts:
  (a) 33='dire' directly: "on dire" — FAIL (ungrammatical).
  (b) 33=[X]er: "on [X]er" — FAIL (same; X is an -er infinitive).
  (c) 84 re-read as not-"on": BLOCKED — A15 grant stands unconditioned; battery may not overturn it.
  (d) Clause boundary ("on. dire…"): "on" cannot end a clause — FAIL.
  (e) 33 as non-verbal (noun "le dire"-shaped): no determiner present; "on" still needs a verb — FAIL.
  No parse under standing values exists. Clause 1 FAILS.
- Forcing neighbor: 84's granted "on" forces a finite-verb frame that neither set member (both infinitives) can satisfy. Cause stated: the orphan is 84-driven, not 33-driven — 33='dire' is the correct member, but the frame cannot host an infinitive. Fenced to the neighbor 84, consistent with the lane's residual-fencing convention (cf. @1642 fenced to 12 in croire-33-residuals). Clause 2 PASSES.

- @1504 (second 33 in the window): "42 33 00 86" = "[42] dire pour [86]". Right frame "dire pour [INF]" parses cleanly ('pour'+infinitive; 86 INF-class granted A9). Left neighbor 42 is OPEN (predicative frame granted A1, value unnamed) — it forces nothing, so @1504 does not need a third value. NOT an orphan.

Other orphan @1642 (row a8_04): `12 33 98` = "n' [33] [98]". 12="n" (letter, battery-promoted 2026-10-08). "n'" requires a vowel-initial word; both set members are consonant-initial ('dire'; X is a consonant-initial -er infinitive, 'laisser' lead). "n'dire" ungrammatical. Fenced to the neighbor 12 (owned for resolution by queued croire-33-residuals; not re-decided here). Stays an orphan.

## Orphan census (all 25 windows of 33, re-derived this run)

- Stem windows, parse as [X]er (5): @273, @626, @1232, @1424, @1477 — inherited from erstem-33-id (identical bigram set re-derived here).
- Whole windows, parse as 'dire' (18): @24 ("ce dire", 47='ce'), @186/@408/@846/@936/@1088/@1245/@1630 ("pour dire", 00='pour'), @467 ("pour dire tout"), @265 ("[52] dire [42]", open neighbors, no contradiction), @776 ("ne [15] dire", 94='ne'), @1000 ("par me dire", 82='m' banked, 96='par'), @1149 ("veut dire", 67='veut' by positional rule), @1421 ("[15] dire [21]", chain window), @1451/@1624 ("veut/et dire que", 67-33-46 idiom), @1504 ("dire pour [86]", see above), @1700 ("[85] dire ne pas" — 33='dire', dire-shaped compound tail per the @1700 'contredire' lead; the 30-question there belongs to ne-30-1700, not this census).
- Orphans (2): @1502 (fenced to 84, this battery), @1642 (fenced to 12, croire-33-residuals).

5 + 18 + 2 = 25. Orphan rate 2/25 = 8%, at/under the 10% threshold. NO third orphan anywhere on the stream.

## Per-clause pass/fail

1. @1501-1507 parses under standing values: FAIL — "on"+infinitive ungrammatical with 84="on" granted unconditionally; all five parse attempts exhausted (a–e above).
2. Orphan confirmed with stated cause: PASS — forcing neighbor 84 ("on", granted, unconditioned per collision-62-84 2026-10-08); set offers infinitives only; fenced to 84.
3. No third orphan: PASS — full 25-window census re-derived; every non-orphan window admits a set-member parse with no standing-value contradiction.

## Adverses disposition

- "a third orphan anywhere (3/25 = 12%) kills the set": ANSWERED — no third orphan exists; census is 2/25 = 8%. The threshold guard holds; the set is not killed by this battery.

## Standing-verdict check

No contradiction with any standing verdict: 84="on" grant and its unconditioned re-derivation respected; §7 sole-polyvalence rule untouched (no new polyvalence declared); A10 33+29 HOLD respected; @1642 left for queued croire-33-residuals (not re-decided). Nothing to escalate.

## Verdict: promote

The bar's disjunction is satisfied via its second arm (orphan confirmed with stated cause) and the threshold scan passes (2/25 = 8%, no third orphan). The claim "resolve @1501-1507 or confirm orphan for the 33 set" holds. This is a guard-battery success, not a value promotion: @1502 stays an orphan fenced to 84; the dire-33-set's 10% orphan threshold is verified intact.

## Anomaly (for the supervisor, not this battery to fix)

The queue cites the parent set battery's report at `code/crowd17/report_inbox/battery-dire-33-set.md`, but that file does not exist on disk (checked inbox root and `processed/`). The erstem-33-id report (in `processed/`) confirms the set battery ran null on 2026-10-08 and inherits its census, so the data chain is intact — but the cited report path is dangling.
