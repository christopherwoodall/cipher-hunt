# Battery report: mne-52-16-branch — verdict: NULL (fence; defect isolates to 94)

- Target id: `mne-52-16-branch` (priority 3)
- Worker: subagent 01468cfd-97b2-44b2-a951-02fd05c46946
- Date: 2026-10-09
- Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` +
  `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`;
  1,847 pairs asserted, 96 types asserted). `canonical.py` never used. R5005,
  sealed gate instances, and the red-team adjudication queue untouched.
- Lock: `code/crowd17/next-token/locks/mne-52-16-branch.lock` created
  2026-10-09T09:45:45Z with agent id + UTC timestamp. No prior lock existed
  (no stale lock to note). Deleted on completion.
- @-offsets below are 1-based pair indices (lane convention). The queue
  evidence cites the 82-position for branch A and the 94-position for
  branch B; both are given with full context so the reference is exact.

## Bar (verbatim from battery-queue.json, copied before testing)

"promote-52-82-unit iff "52 82 16" parses cleanly under a compositional "[52] me" unit AND "52 82 94" parses with the same unit; kill iff no compositional unit licenses both branches"

Numbered clauses (restated from the bar before testing; not modified after
seeing data):

- (C1) The "52 82 16" trigram parses cleanly under a compositional "[52] me"
  unit — at both windows (@1386, @1436, 82-position).
- (C2) The "52 82 94" trigram parses with the same "[52] me" unit — at all
  three windows (@651, @1102, @1576, 94-position).
- (C3, kill leg) No compositional unit licenses both branches.

## Method

1. Read `code/crowd17/next-token/BATTERY-PROTOCOL.md` in full before touching
   anything. Created the lockfile on start.
2. Re-derived the repaired stream in-session (assert 1,847 pairs). Re-censused
   "52 82" (n=5), "82 94" (n=3), and the followers of "52 82" from the stream.
   Every count below is byte-traced; no invented data.
3. Standing values used as granted per §7 and the target adverses: 82='m'
   (banked), 94='ne' (STRONG LEAD, pending ratification), 16=infinitive
   (standing battery promote, gate-satisfiability-16-85), 06='ent' (promoted),
   29='er' (banked), 85=verb-stem (A3 granted), 64='qui' (promoted),
   24=finite-modal (promoted class, per battery-ne-94-right-context).
   52's class/value is open (adverse).
4. 94's status at these windows was NOT adjudicated (red-team venue per the
   task constraints). The word-internal "[52]mne" rescue and any 94
   polyvalence are out of scope for this battery.

## Distributional verification (byte-traced)

- "52 82" occurs exactly 5x stream-wide. Followers: 94 x3, 16 x2. No other
  follower. (Confirms the queue evidence.)
- "82 94" occurs exactly 3x stream-wide — the three branch-B windows. No
  other "82 94".
- "52 82 16" x2; "52 82 94" x3. The two branches partition the "52 82" set.

## Window-level evidence

### Branch A — "52 82 16" x2 (infinitive-16 per standing promote)

- A1 @1386 (row a7_06): `65 68 | 52 82 16 06 29 | 67`
  Full: @1385-1391 = `68 52 82 16 06 29 67`.
  Parse under the "[52] me" unit: `[52] me [16-inf] [06-ent] [29-er]` =
  "[governor] me [infinitive] enter". The trigram has exactly the shape of
  the grammatical French template "[prep] me + infinitive" (sans / de /
  afin-de type: "sans me voir", "de me voir"). The tail "06 29" ("enter")
  reads as the infinitive's complement ("sans me [voir] entrer" shape) or a
  following word; either way it does not break the trigram parse.
- A2 @1436 (row a7_08): `49 64 | 52 82 16 24 85 | 01`
  Full: @1435-1442 = `49 64 52 82 16 24 85 01`.
  Parse: `[52] me [16-inf]` then a clean clause boundary: `[24-finite-modal]
  [85-verb-stem]` ("[modal] [verb-stem]" is a licit clause start under
  granted values). The trigram itself is the same "[prep] me + infinitive"
  template as A1.

C1 result: both windows parse cleanly under a compositional "[52] me" unit
with 52 as a me+infinitive governor (sans/de-type). 52's value stays open
per the adverse; no standing verdict forbids the governor face (52's global
value is owned by the queued red-team target split-52-redteam).

### Branch B — "52 82 94" x3 (94='ne' strong lead)

- B1 @651 (row a4_02): `77 78 | 52 82 94 76 49 | 24`
  Full: @647-654 = `77 78 52 82 94 76 49 24`.
- B2 @1102 (row a6_06): `67 86 | 52 82 94 74 47 | 78`
  Full: @1099-1106 = `67 86 52 82 94 74 47 78`. Note "06 29" immediately
  left (@1097-1098).
- B3 @1576 (row a8_01): `32 28 | 52 82 94 76 47 | 98`
  Full: @1574-1581 = `32 28 52 82 94 76 47 98`.

Parse attempt under the same "[52] me" unit: `[52] me [94] [76/74]` =
"[governor] me ne [76/74]". Under 94='ne' as particle, "me ne" is reversed
French clitic order — ungrammatical. The stream's own grammatical "ne me
[verb]" template is "94 82 06" x2 ("ne m'ent...", per battery-frame-76-ne-94);
"82 94" x3 is the reversed anomaly. No battery-established 94-function
rescues the trigram: the word-final '-ne' syllable is established only for
62-94 windows (seg-62-94-wordless6), not here; the word-internal "[52]mne"
rescue is red-team venue (queued target seg-528294-word).

C2 result: FAIL at battery level. Branch B does not parse with the "[52] me"
unit under any battery-established 94-function. The failure isolates
entirely to 94's status at these three windows.

## Per-clause pass/fail

- (C1) PASS — both "52 82 16" windows parse cleanly under the compositional
  "[52] me" unit (52 = me+infinitive governor, value open per adverse;
  16 = infinitive per standing promote).
- (C2) FAIL — "52 82 94" does not parse with the same unit at any of the
  three windows under standing values ("me ne" reversed clitic order).
- (C3, kill leg) NOT FIRED — the C2 failure turns entirely on 94's function
  at these windows, and 94='ne' is a STRONG LEAD pending ratification, not
  an established value. The standing promote battery-ne-94-right-context
  (2026-10-09) explicitly leaves @651/@1576 ('m ne 76') and @1102 ('ne 74')
  as unfenced live residuals "for the next round of the question". Firing
  the kill would adjudicate 94's status at these windows — forbidden at
  battery level by the task constraints ("do not adjudicate 94's status at
  battery level"). A window whose parse depends on an unratified value
  cannot force the claim false at kill grade.

## Adverses disposition

- 82='m' banked: used as granted throughout. Answered (not a blocker).
- 94='ne' STRONG LEAD pending ratification: used as granted for the parse
  test; its unratified status is exactly what blocks the kill leg and forces
  the fence. Fenced with stated cause, not ignored.
- 16=infinitive standing promote: used as granted for C1. Caveat (below).
- 52's class/value open: used as granted; C1 conditions on 52=governor at
  these windows only, with global value left to split-52-redteam.

## Standing-verdict check

- No standing or red-team verdict contradicted or downgraded. No polyvalence
  declared (§7 intact: 67 et/veut remains the sole true polyvalence; no 52
  split declared at battery level).
- Consistent with the parent battery-frame-76-94-trigram (NULL): its
  follow-up #1 designed this target so that "if '52 82 16' parses cleanly,
  94 becomes the sole defect and the fence isolates to 94" — that is exactly
  the outcome reached.
- Caveat: battery-frame-82-16 (NULL, 2026-10-09) carries a class lead
  (16 = finite verb, "a"/"est") that contradicts the standing promote
  16=infinitive, escalated to the red team. If the red team sustains the
  finite-verb lead, C1's "infinitive-16" premise re-opens and this target
  must be re-run. This battery does not re-litigate 16's class.

## Verdict: NULL (fence)

Rationale: C1 passes, C2 fails, and the kill leg cannot fire at kill grade
because the C2 failure isolates to 94's unratified status — red-team venue.
Promote is out (C2 fails under standing values); kill would overreach the
battery's mandate. The defect isolates to 94 at @651/@1102/@1576, as the
parent battery's design anticipated.

## Follow-ups proposed (all verified absent from battery-queue.json; n=983 targets checked)

1. `gov-52-branchA` (P3) — name 52's governor value at the branch-A windows:
   discriminate {sans, de, ...} via government of "me"+infinitive and
   left-context compatibility (68 @1385, 64 @1435); cross-check against
   52's "ne [52] [INF]" x3 adverb face. Gates on split-52-redteam.
2. `tail-52-82-16` (P4) — resolve the branch-A tails to harden C1: the
   "06 29" word boundary at @1389 (enter / entrer-tail / tenter-tail?) and
   the "24 85" modal-clause boundary at @1438-1439. A clean tail parse on
   both windows promotes C1 from conditional to firm.
3. Red-team escalation (in-report, not a queue target): adjudicate 94's
   function at @651/@1102/@1576 — particle-'ne' vs word-internal '[52]mne'
   (queued seg-528294-word covers the word-internal test) vs other function.
   This is the single gate on the C2 leg; the supervisor should route it
   with the parent battery's fence.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-mne-52-16-branch.md` (this file)
- Queue: `mne-52-16-branch` queued → status `verdict`, result `null`,
  date 2026-10-09 (temp-file + rename; pre-write assert confirmed
  queued/verdictless; JSON re-validated post-write)
- Lock created 2026-10-09T09:45:45Z with agent id, deleted on completion.
- Canonical-stream caveat stands (68 of 70 upstream row offsets unvalidated).
