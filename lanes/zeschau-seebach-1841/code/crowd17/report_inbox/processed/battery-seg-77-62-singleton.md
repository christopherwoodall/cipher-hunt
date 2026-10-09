# Battery report: seg-77-62-singleton

- Target id: `seg-77-62-singleton`
- Claim: "resolve the 77-62 stream singleton (@507 only)"
- Date: 2026-10-09
- Worker: battery worker (subagent 14aa04ab-a6e1-40a0-b30b-2e9a04317c45)
- Stream: repaired 1,847-pair parse (`data/upstream-ct_R5005.txt` +
  `code/side-keyhunt/repaired_offsets.json`, parsed like
  `code/side-keyhunt/repair_parse.py`). `canonical.py` never used.
  R5005, sealed gates, red-team adjudication queue untouched.
- Lock: `code/crowd17/next-token/locks/seg-77-62-singleton.lock`
  (created at start, deleted on completion).

## Bar (verbatim, pre-registered before testing)

"resolve iff a second 77-62 contact or a 77-initial word family is found
on the repaired stream; else confirm singleton (weakens any compositional
claim at @507)"

Numbered pass/fail clauses (restated before testing, not modified after):

1. (C1) The `77 62` bigram count on the repaired stream is re-derived
   byte-exact; resolve the "second contact" leg iff a second `77->62`
   adjacency exists at any stream position.
2. (C2) A 77-initial word family is found iff a battery-grade
   77-initial syllabic composition (a word family starting with 77's
   syllable) exists on the repaired stream under standing values.
3. (C3) If neither C1 nor C2 fires, the singleton is confirmed with
   the byte-exact count; the pre-registered consequence follows —
   any compositional claim at @507 (the `77-62-94` "le [62]ne" word)
   is weakened, not strengthened, by this result.

## Method

1. Re-derived the repaired stream in-session: 1,847 pairs, 96 types
   asserted. Never used `canonical.py`. R5005 untouched.
2. Census of all `77->62` adjacencies with row ids and +-6 context.
3. Census of all 77 successors (n(77)=44) and all 62 predecessors
   (n(62)=35).
4. Lane-wide sweep of the battery queue for any standing 77-initial
   word-family finding (`lever-77-78` and 77-related promote/kill
   verdicts), adopted as premises, not re-run.
5. Phase check: re-parsed row a3_00 under its rival offset.

## Window-level evidence

### C1: 77-62 contact census — NO second contact

`77->62` occurs exactly **1x** stream-wide:

- **@507 (0-based), row a3_00** (mid-row): `... 21 67 77 62 94 64 98 ...`

The related battery `battery-head-77-62-94-noun.md` (verdict NULL)
independently verified the same 1x count. n(77)=44; n(62)=35.
The most common 77 successors are 78 (x7), 84 (x7), 86 (x5), 81 (x4);
62's most common predecessors are 21 (x5), 20 (x4), 74 (x3).
**C1 does not fire: singleton confirmed.**

### C2: 77-initial word family — NONE at battery grade

Under provisional 77="le", a 77-initial word family would be words of
the form "le"+syllable. The only such family ever tested in the lane
is the `77 78` -> "lever" composition:

- `lever-77-78` (claim: "'77 78' reads 'lever' ... in all 7 windows"):
  verdict **null**. The composition is not established at battery
  grade; it remains a hypothesis, not a finding.
- The two standing 77 promote verdicts (`frame-qui-77-84`,
  `elision-77-84`) concern 77="le" eliding to l' before vowel-initial
  84 — a letter-level elision mechanism, not a 77-initial word family.
- No other 77 successor (84/86/81/76/44/89/82/66/60/80/06/87/45/03/
  64/11/83/74/62) has any battery-grade compositional word claim;
  "leon"/"lela"/"lequi"-shaped readings are unproposed anywhere.
- The @507 compositional candidate itself (`77-62-94` = "le [62]ne")
  is the subject of the weakness the bar's else-branch records —
  it cannot serve as its own family.

**C2 does not fire: no 77-initial word family exists at battery
grade.** The closest hypothesis (`lever-77-78`) is verdict null.

### C3: singleton confirmed

The `77 62` bigram is a byte-exact singleton (@507, row a3_00) with
no second contact and no established 77-initial family. Per the
pre-registered consequence, the compositional claim at @507 —
`77-62-94` as one word under the conditional syllabic-94 reading —
is weakened: it has no distributional precedent anywhere in the
stream. This is consistent with (not a downgrade of)
`head-77-62-94-noun`'s NULL: that battery left the locus parse as an
un-named conditional; this battery records that the conditional
has no sibling anywhere.

### Phase caveat (stated, not hidden)

Row a3_00 (58 digits, upstream offset 0): under its rival offset-1
the entire row re-pairs with **no `77-62` bigram** — the singleton
is a canonical-offset object, same mechanism class as the a1_01 and
a7_10 findings. The confirmation holds on the canonical stream per
protocol; it dissolves if a3_00 re-phases. The phase-fragility
itself strengthens the weakness of the compositional claim (it is
doubly isolated: no siblings AND no byte-anchor).

## Per-clause pass/fail

1. C1 (second contact): NOT FOUND — byte-exact 1x.
2. C2 (77-initial word family): NOT FOUND — nearest candidate
   (`lever-77-78`) is verdict null.
3. C3 (confirm singleton): PASS — else-branch deliverable met.

## Adverses

None listed in the queue entry.

## Verdict: PROMOTE (finding grade)

The bar's else-branch deliverable is met: the 77-62 singleton is
confirmed byte-exact on the repaired stream, with no second contact
and no established 77-initial word family. The pre-registered
consequence follows — the @507 compositional claim is weakened.
No standing or red-team verdict contradicted or downgraded;
§7 intact. Canonicality caveat stands (a3_00's upstream offset
unvalidated; the singleton dissolves under rival offset-1).

No follow-ups required — this is a promote, not a null. Optional:
an offset-1 constraint sweep of a3_00 (P4) would harden or dissolve
the singleton; recorded here rather than queued, since the canonical
confirmation stands as the deliverable.
