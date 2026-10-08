# Battery report: fork-78-45-rerun

Target: `fork-78-45-rerun`. Claim: re-run the 78-45 fork battery once ver-78 resolves.
Date: 2026-10-08. Worker: 0672a4a8-21a4-4ee0-9243-d363b6eda5e0. No stale lock existed at start (locks dir holds only NOTE.md).

## Bar (verbatim, pre-registered)

"(a) if ver-78 promotes 78='ver', test the four windows (@314, @574, @983, @1165) for 'verdict...' reads; kill 45='ce' at exactly the windows that force it and record kill scope as k/22; (b) if ver-78 kills 78='ver', 45='dict' loses its syllabic host - kill dict-45's fork arm"

## Bar restated as numbered pass/fail clauses

1. Clause (a) — conditional on ver-78 PROMOTING 78='ver': test the four 78-45 windows for 'verdict...' reads; kill 45='ce' at exactly the windows that force it; record kill scope as k/22.
2. Clause (b) — conditional on ver-78 KILLING 78='ver': 45='dict' loses its syllabic host; kill dict-45's fork arm.

## Method

Repaired 1,847-pair stream only: `code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py` (`canonical.py` never used). No R5005, no sealed gates, no red-team contact. Every count below traces to the stream.

Current antecedent check (battery-queue.json, 2026-10-08):
- `ver-78`: status `verdict`, result **null** — R16-005 graded 78='ver' LEAD, not settled; @296 red-team-fenced 1-window residual. NOT promoted.
- `ver-78-rebar`: status `verdict`, result **null** — lane-legal bar, same unsettled state. NOT promoted.
- No queue entry records 78='ver' as killed.

## Window-level evidence (@-offsets are the 78 position; 45 = 78+1) — re-derived to confirm unchanged

- W1 — 78@313 (row a2_04): `20 17 46 84 24 37 | 78 45 | 64 59 32 94 06 11` — matches battery-fork-78-45-adjudication.md.
- W2 — 78@573 (row a3_02): `76 45 94 52 87 | 78 45 | 13 55 61 94 82 06` — matches (byte-identical 78-45-13-55-61 5-gram with W4).
- W3 — 78@982 (row a6_01): `92 07 76 47 | 78 45 | 01 24 89 48 01 76` — matches.
- W4 — 78@1164 (row a6_09): `82 44 83 21 67 | 78 45 | 13 55 61 94 87 83` — matches.
- n(45) = 22; 78 is 45's top predecessor (4/22). Both match the adjudication record.

Nothing changed since battery-fork-78-45-adjudication.md: all four what-if parses there remain the standing record (W1 ambiguous; W2/W3 favor dict under the what-if; W4 partial, needs 78 noun-shaped either way).

## Per-clause pass/fail

1. Clause (a): **NOT TESTED — antecedent false.** ver-78 did not promote 78='ver' (null/LEAD, unsettled); ver-78-rebar also null. LEAD is not promotion; the bar's conditional cannot fire. No windows tested against 'verdict...' reads; no kill of 45='ce'; no k/22 scope recorded.
2. Clause (b): **NOT TESTED — antecedent false.** 78='ver' was not killed by any battery or red-team ruling; ver-78 remains open. dict-45's fork arm is untouched.

## Adverses fenced (not ignored)

- R16-005 LEAD grading: answered — LEAD ≠ promotion; the bar explicitly keys on promotion, so this battery records the gap rather than bridging it.
- A11 HOLD (45='ce'): untouched. No kill fired at 0/22 windows; the adjudication report's clause-(a)-else branch ("45='ce' is killed at 4/22") is likewise unfired because its antecedent never held.
- W1 ambiguity: carried forward unchanged; assigned to w1-314-ambig (already queued).

## Verdict: null

Headline: the bar cannot fire. Both of the bar's conditionals key on a ver-78 resolution that has not happened — ver-78 and ver-78-rebar are both null (R16-005 LEAD, unsettled). The fork stays open exactly as battery-fork-78-45-adjudication.md left it: what-if parses recorded, R-pos positional rule awaiting red-team declaration per protocol §7. No contradiction with any standing verdict (A11 HOLD and R16-005 LEAD both untouched) — nothing to escalate.

## Follow-up targets (null regenerates work; both absent from queue, verified 2026-10-08)

1. verdict-w2-574-gate (priority 1). Claim: W2 @573 ("ce verdict [13-55-61] ne m'") is the flagship fork window; when ver-78 resolves, adjudicate W2 before W1/W3/W4. Bars: (a) decide by boundary evidence whether 78-45@573 is one word ('verdict') or two — state why the two-word parse is impossible under 78='ver'; (b) record whether 'ce [78] ce' survives at W2 under a non-ver 78 value, so the gate is useful even under a ver-78 kill. Evidence: 'ce verdict' x2 @573/@982; 94-82 = 'ne m'' elision frame clean under dict reading. Adverses: A11 HOLD; W1 ambiguity; R-pos needs red-team declaration.
2. dict-45-contact-update (priority 2). Claim: 45's post-78 followers ({13, 01, 64}) form a disjoint profile from standalone-45 followers, strengthening the syllable rival independent of ver-78. Bars: (a) census all 22 of 45's followers split by pre=78 vs pre≠78; (b) boundary holds iff follower distributions are disjoint at Fisher p<0.05 with stated counts. Evidence: 13-55-61 follows 45 only after 78; 01 follows 45 only at W3; 45->13 x2 = the 78-45-13-55-61 5-gram. Adverses: W1's 45-64 follower shared with standalone @340/@1024; n=22 small.

Note: the queue's verdict path for fork-78-45-adjudication says `code/crowd17/report_inbox/battery-fork-78-45-adjudication.md`, but the file actually lives at lane-root `report_inbox/processed/battery-fork-78-45-adjudication.md`. Flagged for the supervisor; this report is written at the queue-specified path `code/crowd17/report_inbox/battery-fork-78-45-rerun.md`.
