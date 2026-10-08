# Battery report: ne-le-1075 — "'ne le' frame test @1075"

- Target: `ne-le-1075` (priority 2), claim: "'ne le' frame test @1075"
- Worker: subagent session ecf963e5-7d65-4808-9dd5-6a0225df52e6
- Date: 2026-10-08
- Lock: no prior `locks/ne-le-1075.lock` existed (not stale, simply absent); lock created 2026-10-08T12:37:02Z, deleted on completion.
- Verdict: **KILL** (the 'ne le [78=verb-head]' frame as posed; re-open condition stated below)

## Bar (verbatim, from battery-queue.json)

> resolve iff 78's profile allows heading a verb phrase after 'ne le'; else weaken the frame

### Numbered clauses (pre-registered, unmodified after testing)

- **C1.** The @1075 window re-derives on the repaired 1,847-pair stream as a 'ne le'-shaped locus ('12 48 77 78' with row-level confirmation).
- **C2.** 78's standing profile allows heading a verb phrase: 78 is attested in verb-head slots, and a verb reading is compatible with the red-team R16-005 grading and the §7 sole-polyvalence rule.
- **C3 (control).** Other 'ne le'-shaped windows exist stream-wide (94-77 adjacency; 12-48-77 trigrams) and behave consistently with the frame.
- **Rule.** Promote the frame iff C1–C3 all pass; otherwise weaken (kill or null with the weakened form stated).

## Method

- Stream only: `code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed exactly like `code/side-keyhunt/repair_parse.py` (1,847 pairs confirmed). Never `canonical.py`, never R5005.
- Re-derived the target window at 0-based pair index; confirmed row id `a6_05`.
- Full census of 78 (n=31): every window with ±3 context; predecessor/follower distributions.
- Controls: all 94-77 adjacencies; all 12-48-77 trigrams; all 77-78 bigrams with left context; followers of 94; all five 12-48 bigrams.
- Standing verdicts read, not re-run: `ver-78` NULL (2026-10-08), `ver-78-rebar` NULL (2026-10-08), `fork-78-45-adjudication` NULL (2026-10-08); queued `lever-77-78`, `ver78-la78-census`, `ver78-ce78-open-succ`, `ver78-296-reparse` (overlap noted, not re-litigated).

## Offset reconciliation (measured, not assumed)

- The target's 6-gram `98 12 48 77 78 64` sits at **repaired-stream @1073–1078** (row `a6_05`); the 'ne le' locus `12 48 77 78` is at **repaired @1075–1078**, follower `64` at @1079, `06` at @1080.
- Target/finder offsets run +2 ahead of repaired offsets here (same shift as `lever-77-78`'s "@1077 '98 n elever 64'" and the known pre-repair/post-repair shift family, e.g. est-59-frames @762→@760). All @-offsets below are repaired-stream unless marked "finder".

## Window-level evidence

Repaired @1073–1083 (`a6_05`): `98 98 12 48 77 78 64 06 52 89 24`.

78 census (n=31), predecessors: 77 x7, 47 x5, 87 x2, 37 x4, 67 x4, 11 x2, 16/50/86/80 x1.
That is 16/31 after determiner/'ce'-class heads (77='le' provisional x7, 11='la' x2, 47/87='ce' x7), 4/31 after 37 (A1 predicative), 4/31 after 67 ('et'-fork: 78 is not infinitive-shaped, so §7 resolves 67='et' → noun coordination, e.g. @352 `67 78 40`, @1164 `67 78 45` = 'et ver[dict]').

78 successors: 45 x4 ('verdict' fork), 40 x3, 48/49/41/62/94 x2, 18/06/63/17/43/47/65/66/55 x1.

Verb-head search over all 31 windows: **0 clean verb frames**. The nearest candidates fail:
- @1621 `11 84 78 66` ("la on [78] 66"): the only `84 78` ('on 78') contact stream-wide, but the `11 84` ('la on') left edge is itself an unparsed clause boundary; not a clean verb frame.
- @1012 `79 80 78 47` ("tout [80-verb] [78] ce"): 78 follows the A8 verb-frame 80 in object position → noun-78, not verb-78.
- @879 `77 86 78 17` ('le' + 86-INF-class + 78 + 'fois'): 78 after a substantivized infinitive → complement/noun slot.
- @352/@492/@1164/@1843 `67 78 …`: 67='et' per §7 (follower not infinitive-shaped) → noun coordination.

Controls:
- **94-77 adjacency: 0 stream-wide.** No 94 within 1–3 pairs before any 77 either. The 'ne le' reading cannot come from 94='ne' + 77='le' anywhere.
- **12-48-77 trigram: exactly 1 stream-wide** — the target window (repaired @1075). The frame has exactly one leg.
- 12-48 bigrams: 5 (@169, @709, @809, @1075, @1736); followers 21/71/24/77/52 — only @1075 continues to 77-78.
- Followers of 94 ('ne', n=37): 82 x4, 74/59/52 x3, 92/24/76/79 x2, 93/65/06/02 x1 — **78 never follows 94**.
- Of the 7 `77 78` windows (@7, @213, @647, @1077, @1180, @1351, @1542), only @1077 carries a 'ne'-shaped left context (12-48). `78 64` ('ver qui') occurs exactly once stream-wide (@1078).

## Per-clause results

- **C1 — PASS.** The 'ne le'-shaped locus re-derives: repaired @1075 `12 48 77 78` = 'n e le 78' (row `a6_05`), unique stream-wide.
- **C2 — FAIL (kill grade).** 78's profile does not allow heading a verb phrase: 0/31 verb-headed windows; 16/31 determiner/'ce'-headed noun slots; 4/31 predicative-37 slots; 4/31 'et'-coordination slots. Standing law independently bars the required value: red-team R16-005 grades 78='ver' as **LEAD, a noun syllable** ('verdict' x4 conditional on 45='dict'; 'la verte'-shaped), and §7's sole-polyvalence rule (67 et/veut) forbids a second, verb-headed value for 78 at battery level — declaring one is a red-team act. The frame needs 78 to head a verb phrase; the lane's own grading says 78 heads noun phrases. A distributional kill is also available: 78's verb-slot rate is 0/31 against 16/31 explicit noun slots.
- **C3 — no support.** The frame's only possible leg is the target window itself (94-77 x0; 12-48-77 x1). Recorded as context, not an independent failure.

## Adverses

- "78's profile open (78='ver' queued as ver-78)" — **ANSWERED, not ignored.** Since the target was queued, `ver-78` (2026-10-08) and `ver-78-rebar` (2026-10-08) both returned **NULL with 78='ver' as red-team-graded LEAD (R16-005), noun-syllable**: 'ce [78]' x7 'er'-exclusion confirmed; distributional kill of 'er' holds with corrected attribution (29: 2/45 det-pred, 5/45 pred-33; 78: 16/31, 0/31; OR=22.93; Fisher p≈2.5e-06); @296 fenced as red-team residual. The profile is no longer open in the feared way — it is settled noun-headed, which is exactly what defeats C2.

## Verdict: KILL

The 'ne le [78=verb-head]' frame as posed is **killed**: its resolution condition (78 heading a verb phrase after 'ne le') is blocked by standing lane law (R16-005 noun-syllable LEAD + §7 sole polyvalence) and by the measured 0/31 verb-slot rate. This kill does **not** contradict any standing red-team verdict — it agrees with R16-005.

**Weakened/surviving forms of the @1075 locus** (already chartered; no new targets queued):
- (a) `lever-77-78` (queued): the `77 78`='lever' composition at this same locus; its bar clause 3 already owns the 'ne lever qui' / 12-48 re-parse resolution.
- (b) Analytic 12-48 = 'n'+'e' letters with 48='e' second-order ("n'élever") — feeds `lever-77-78` clause 3.
- (c) Noun 'ver-' reading ('ne le ver[dit] qui') conditional on the `dict-45` / `fork-78-45-*` family (queued) — note it still needs a finite verb or 'pas' to make "ne le verdict qui" grammatical.

**Re-open condition:** this kill re-opens iff the red team declares a second polyvalence for 78 (verb head alongside noun 'ver') or overturns R16-005's noun-syllable grading.

**Note for the `lever-77-78` worker:** 12-48-77 is unique stream-wide (x1) and 94 never co-occurs with 77 within distance 3 — the 'ne' at this locus must come from the 12-48 letter reading, never from 94.

## Dependencies stated (§7)

77='le' provisional (le-77 NULL 2026-10-07); 12='n'/48='e' and 94='ne' battery-promoted, **pending red-team ratification** — the 'ne' reading of 12-48 depends on them; 59='est' provisional (not load-bearing here); canonicality caveat stands (68 of 70 upstream row offsets unvalidated). No invented numbers: every count above was re-derived from the repaired 1,847-pair stream in this run.
