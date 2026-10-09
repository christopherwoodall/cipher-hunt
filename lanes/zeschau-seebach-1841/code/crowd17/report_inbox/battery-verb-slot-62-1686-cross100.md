# Battery report: verb-slot-62-1686-cross100

- Target id: `verb-slot-62-1686-cross100`
- Claim: contrast parse: under provisional 59='est', test whether @100's
  '62 94 93 59 45 28 00 46' parses cleanly as a ne...que bracket
- Date: 2026-10-09
- Worker: battery worker (subagent 98fa3349-a171-481c-9c57-908248212940)
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` +
  `code/side-keyhunt/repaired_offsets.json`, parsed per
  `code/side-keyhunt/repair_parse.py`; asserts 1847/96 held in-session).
  `canonical.py` never used. R5005, sealed gate instances, red-team
  adjudication queue untouched.
- Prior: `battery-verb-slot-62-1686-neque.md` NULL 2026-10-09 (follow-up 1).

Terms (ASD-STE100): "bracket geometry" = adjacent "62 94" followed by a
"46" within 12 groups (the ne...que-shaped span). "Licensed verb" = a
finite-verb value granted or provisional in a standing verdict. "Co-opt" =
a stronger licensed unit ("pour que") consuming a token the weaker
reading needs ("que").

## Standing record adopted (not re-litigated)

- **62="il" is KILLED at kill grade** (R19-097/R19-106; confirmed R20-125).
  62's class/value kept open throughout; nothing below assumes "il".
- **94="ne" is STRONG LEAD, not granted** (R17-001 rejected the promote;
  R19-167, R20-007 confirm). The ne...que test below is conditional on the
  lead; the failure finding is structural and lead-independent.
- **59="est" is provisional** (R20-066). The only licensed finite-verb value
  in §7. 46="que" pencil ground truth. 00="pour" (A9, leg-1 class-level).
  45="ce" (A11 hold). 93 verb-class grant (R19-166) stands. §7 intact.

## Bar (verbatim, pre-registered before testing)

"discriminates isolated-@1686 residual vs a geometry that fails even with
its licensed verb present"

Numbered pass/fail clauses (restated before testing, not modified after):

1. **C1 (isolated-residual arm):** @100's "62 94 93 59 45 28 00 46" parses
   cleanly as a ne...que bracket under provisional 59="est" → the @1686
   residual is isolated (the geometry hosts a verb; only @1686's empty
   verb slot is the problem).
2. **C2 (geometry-broken arm):** @100's bracket fails even with its
   licensed verb present → the "62 94 ... 46" geometry fails structurally,
   independent of verb presence.

Adverses (from queue entry): 62='il' kill-grade (R19-097/R19-106, R20-125);
94='ne' strong lead not granted. Both answered below.

## Method

1. Read BATTERY-PROTOCOL.md first. Created
   `code/crowd17/next-token/locks/verb-slot-62-1686-cross100.lock` on start
   (agent id + 2026-10-09T20:50:00Z); no prior/stale lock; deleted on
   completion.
2. Re-derived the repaired stream byte-exact in-session.
3. Byte-confirmed both spans; census of "00 46" ("pour que") units.

## Window-level evidence

**@100 span (0-based, row a1_02/a1_03 boundary between @101 and @102):**
`@100=62 @101=94 @102=93 @103=59 @104=45 @105=28 @106=00 @107=46`,
right tail `@108=11(la) @109=21 @110=67 @111=93 @112=29 @113=89`.

**@1686 span:** `@1686=62 @1687=94 @1688=79 @1689=14 @1690=60 @1691=27
@1692=46`, right tail `@1693=24 @1694=85`.

**Census:** "00 46" bigram occurs 4× stream-wide. At @100 the terminal que
is the second half of a "00 46" unit; at @1686 the span contains no "00".

## Per-clause pass/fail

**C1: FAIL.** @100 does NOT parse cleanly as a ne...que bracket. Two
independent structural causes, both value-independent:

- **F1 — "pour" co-opts the terminal que.** @106–107 = "00 46" = "pour
  que", the licensed "so that" conjunction (00="pour" A9, 46="que"
  pencil GT). For the restrictive "ne...que", "que" must directly precede
  the restricted constituent; a "pour" stranded before it is
  ungrammatical ("*il n'est pour que X"). The "pour que" unit is the
  stronger licensed parse and consumes the que the restrictive reading
  needs.
- **F2 — the "ne" strands bare.** With "que" consumed by "pour", the span
  reads "[62] ne [93] est [45] [28] pour que ...". A lone "ne" without a
  second negative particle (pas/plus/point/guère) or an expletive licenser
  is ungrammatical. No licenser is present: expletive "ne" must follow its
  licenser ("de peur que..."), but here "ne" (@101) precedes "pour que"
  (@106–107); and "ne [93] est" with 93=adverb still leaves "ne" unpaired.

**"n'est pour X que Y" rescue fails on word order.** The licensed
"n'être pour X que Y" frame ("elle n'est pour moi qu'une amie") requires
"pour" to PRECEDE its complement X ("est pour [X] que [Y]"). Our order is
"est [45] [28] pour que" — "pour" follows 45/28 and attaches to "que",
not to them. The rescue is unstatable on the bytes.

**C2: FIRES.** The geometry fails even with its licensed verb present.
59="est" (provisional) sits inside the span at @103, yet the bracket
cannot parse as ne...que. The verb's presence changes nothing: the
failure is the "pour que" co-option (F1) plus the stranded "ne" (F2),
both structural and independent of which verb occupies the slot.

**Adverse answers:**
- 62="il" kill-grade: honored — 62's value/class kept open; the C1/C2
  analysis uses no 62 value.
- 94="ne" strong lead not granted: honored — the test was conditional on
  the lead, and the failure (F1/F2) is structural, independent of whether
  the lead ever becomes a grant.

**Structural-twin caveat (recorded):** @100 is not a true control for
@1686's bracket. @1686's terminal que has NO preceding "pour" (verified:
no "00" in @1686–1692), so the two spans differ in the terminal que's
attachment. The parent report's "window-local" reading (geometry fine,
only @1686's slot empty) does not survive this battery: the "62 94 ...
46" shape is not a reliable ne...que bracket at EITHER window — @100
fails on "pour que" co-option, and the control comparison is therefore
invalid.

## Verdict: PROMOTE

The discrimination is decisively made at battery grade: C2 fires with two
independent structural causes. @100's bracket does NOT parse cleanly as
ne...que despite holding the only licensed finite verb. No follow-ups
required (PROMOTE): the parent's own follow-ups `dep93-102-bracket-role`
(P4) and `neque-94lead-gate` (P4) are already queued and remain live;
this battery neither contradicts nor re-litigates them.

## Scope

Bracket-geometry test only at @100 vs @1686. Untouched: 93/45/28/21/67
values, 59="est" provisional, 94="ne" STRONG LEAD, 62="il" kill,
gerund-60-1688, class-27-independent, neque-tail-24-85-clause,
frame-62-94-79-reparse, val-27-1691-np, 24-redteam-adjudication, §7.
No standing or red-team verdict contradicted, downgraded, or
re-litigated. Canonical-stream caveat stands (row a1_02/a1_03 boundary
offsets unvalidated).

## Bookkeeping

- Report: this file.
- Queue: `verb-slot-62-1686-cross100` queued → `verdict`/`promote`,
  2026-10-09 (pre-write assert passed — was queued/verdictless;
  target-id-unique tmp
  `battery-queue.json.verb-slot-62-1686-cross100.tmp` + atomic rename;
  disk re-validated; own entry only; no downgrade; no tmp leftover).
- Lock created on start (no stale lock), deleted on completion (verified
  gone). R5005, sealed gates, red-team adjudication queue untouched.
