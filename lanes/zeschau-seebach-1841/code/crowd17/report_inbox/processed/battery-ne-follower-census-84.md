# Battery report: ne-follower-census-84 (@-offsets 84-successor census vs all ne-candidates under alternate readings)

Worker: 11e61fe9-2f5b-4240-97d2-ea5ddd4391d7. Date: 2026-10-09.
Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json +
data/upstream-ct_R5005.txt, parsed per code/side-keyhunt/repair_parse.py;
pair count verified 1847 at test time). canonical.py never used.
R5005 never touched. Red-team queue never touched.
Lock: code/crowd17/next-token/locks/ne-follower-census-84.lock (created
2026-10-09T06:16:25Z, deleted on completion). No fresh lock present on entry.
This target's own follow-up target (from lon-on-elision-control null,
2026-10-08). Its source report was read from report_inbox/processed/
(the source path in the queue entry omitted the processed/ segment).

## Bar (verbatim, pre-registered)

"census 84's successors against ALL ne-candidates (94, 48, 12='n') under
alternate readings; if any 'on'+ne-contact exists under a rival reading,
record the weakening of the lon-on-elision-control discriminator."

Numbered clauses (stated BEFORE testing):

1. Re-derive 84's successor census fresh from the repaired stream — PASS iff
   n=25 windows and the successor distribution matches the lon-on-elision-
   control census exactly (no phantom windows, none at stream end).
2. Under each STATED alternate reading (94='ne', 48='ne', 12='n'), record
   84->X contact counts — PASS iff counts are recorded per reading, with
   @-offsets for any hits.
3. Record the effect on the lon-on-elision-control discriminator — PASS iff
   the discriminator is weakened (any 'on'+ne-contact) or confirmed to hold
   (zero contact under every stated reading), with the result recorded.

## Alternate readings (stated, not assumed — per the adverse)

- Reading A: 94='ne'. Standing: battery promote 2026-10-07, pending
  red-team ratification (unratified — the adverse). From
  battery-prenne-70-12-94.md: "neither the ne-94 battery promote nor the
  n-e-12-48 battery promote is downgraded".
- Reading B: 48='ne'. Standing: KILLED per §7 (48="est"/"ne"/"de" kill
  holds; {48,94} homophone-set kill holds). Tested anyway as a stated
  rival reading per the bar's "ALL ne-candidates ... under alternate
  readings" — a zero count under this reading forces no contradiction
  with the kill.
- Reading C: 12='n' (letter tier: 12 as the letter "n", from the
  "prenne"/"enne" family). Standing: battery letter-tier promote,
  pending red-team ratification (per battery-enne-word-64.md).

## Method

Fresh parse of the repaired stream; no prior counts trusted. Re-derived:
all 25 legs of 84 with rows and successors; contact counts 84->94,
84->48, 84->12 under each stated reading. No re-litigation of the
94='ne' promote, the 48 kill, or the 12='n' promote.

## Window-level evidence (@-offsets, repaired stream)

84 legs (n=25), none at stream end (all 25 have a successor):
@146, @154, @167, @260, @276, @310, @391, @412, @473, @788, @857,
@1021, @1058, @1151, @1189, @1290, @1378, @1418, @1447, @1485, @1501,
@1620, @1665, @1764, @1803 (rows a1_04 x2, a1_05, a2_02, a2_03, a2_04,
a2_07, a2_08, a2_10, a5_04, a5_07, a6_03, a6_04, a6_08, a6_10, a7_03,
a7_06, a7_08, a7_09, a7_10, a7_11, a8_03, a8_04, a8_08, a8_10).

84 successor census (n=25): 59 x4, 24 x3, 02 x2, 92 x2, 09 x2, 29 x1,
26 x1, 53 x1, 74 x1, 91 x1, 73 x1, 51 x1, 06 x1, 79 x1, 33 x1, 78 x1,
64 x1. Matches the lon-on-elision-control census exactly.

Contact under the stated readings:
- 84->94: x0 stream-wide (Reading A: 'on'+'ne' contact x0).
- 84->48: x0 stream-wide (Reading B: 'on'+'ne' contact x0).
- 84->12: x0 stream-wide (Reading C: 'on'+'n' contact x0).

## Per-clause pass/fail

1. Successor census re-derivation — PASS. n=25, distribution identical
   to the lon report; no phantom windows, no terminal-84 legs.
2. Contact per stated reading — PASS. 84->94 x0, 84->48 x0, 84->12 x0;
   zero 'on'+ne-contact under Reading A (94='ne'), Reading B
   (48='ne'), or Reading C (12='n').
3. Discriminator effect — PASS (recorded). The lon-on-elision-control
   discriminator ("granted 'on' legs show zero 'ne'-followers") is NOT
   weakened: zero contact holds against the FULL ne-candidate set
   under every stated reading. The zero was tested under the widest
   rival-reading set this lane admits and it survives.

## Verdict

**PROMOTE — the discriminator holds against the widened census.** Zero
84->94, 84->48, 84->12 across all 25 granted-'on' windows. No
'on'+ne-contact exists under any stated reading, so the bar's weaken
condition does not trigger. The lone surviving 'on'+'ne' in the lane
remains the conditioned @508 leg (77-62-94 under the lon readings),
which is the red team's act, not this battery's. No standing red-team
verdict is contradicted or downgraded: the 94='ne' and 12='n' promotes
stay pending ratification (this battery's zero-contact result is
conditional on neither — the count is zero regardless of the readings),
and the 48 kill is untouched (zero contact under Reading B forces no
re-open). No promotion of a value is declared here — a distributional
negative is banked.

## Adverses (answered or fenced, never ignored)

- 94='ne' unratified: fenced with stated cause. The test outcome does
  not depend on ratification: 84->94 is x0, so the reading only
  affects labeling, not the count. If the red team overturns 94='ne',
  the label changes but the zero contact stands.
- Alternate readings must be stated, not assumed: answered. All three
  readings stated above with their standing and source reports.
- 48='ne' contradicts a standing kill (§7): fenced with stated cause.
  Tested only as a stated rival reading per the bar; zero contact
  means the kill is never re-litigated and no contradiction is forced.

## Standing-constraint check

- No R5005 contact, no sealed gates, no red-team queue writes.
- No verdict overwritten; no contradiction with any standing verdict
  (48 kill, {48,94} homophone-set kill, 94='ne' and 12='n' pending
  promotions, lon-62-on-conditioned null, lon-on-elision-control null
  all stand beside this report).
- 67 remains the sole true polyvalence.
