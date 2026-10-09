# Battery report: subj-74-261-1500

- Target: `subj-74-261-1500` (priority 3)
- Claim: "test the subject-contact windows @261 ('on 74') and @1500 ('74 on 33-INF') - decide whether A15's 'on' conditions C1-C3 hold at @260/@1501"
- Date: 2026-10-09
- Worker: battery worker (subagent 01c62546-8567-4e2b-9fac-f34996594480)
- Context: follow-up #1 of the noun-74-formula NULL (2026-10-09,
  `code/crowd17/report_inbox/processed/battery-noun-74-formula.md`), whose
  C2 explicitly recorded these two windows as the lead follow-up rather than
  a kill trigger ("firing here would re-litigate the standing
  `ne-alone-02-74` kill on untested conditions"). This battery tests the
  conditions. The standing `ne-alone-02-74` kill is NOT re-litigated.
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` +
  `code/side-keyhunt/repaired_offsets.json`, parsed like
  `code/side-keyhunt/repair_parse.py`; asserts held: 1,847 pairs, 96 types).
  `canonical.py` never used. R5005, sealed gates, red-team adjudication
  queue untouched.
- Lock: `code/crowd17/next-token/locks/subj-74-261-1500.lock` (created at
  start, deleted at end; no prior lock existed).

## Bar (verbatim from battery-queue.json, pre-registered BEFORE testing)

"if 'on' is licensed at both, 74 shows subject-frame contact (kill-seek the
formula hypothesis); else fence the contact as conditional. Kill iff
contact is licensed under stated conditions"

## Numbered pass/fail clauses (restated before testing, not modified after)

1. **Clause 1** — 84='on' is licensed at @260 under A15's conditions C1–C3.
2. **Clause 2** — 84='on' is licensed at @1501 under A15's conditions C1–C3.
3. **Clause 3 (kill arm)** — contact is licensed under the stated conditions
   at both windows: 74 shows subject-frame contact, killing the
   nominal/formula reading of 74.

## A15's conditions C1–C3 (as established by standing batteries)

- **C1**: 77='le' provisional support leg — "77='le' elides to l' exclusively
  before vowel-initial 84" (battery-elision-77-84 PROMOTE; 7 legs, ratified
  by the red team pending their own review). 77='le' itself stays
  provisional.
- **C2**: the 62='on' rival is killed unconditioned (battery-collision-62-84
  KILL); 84='on' holds 'on' unconditioned (per §7 polyvalence rule).
- **C3**: the only fenced residuals under the 'on' reading are R1 (@1620,
  succ 78) and R2 (@1665, succ 64) (battery-fence-84-29-gate).

## Method

Re-parsed the repaired stream exactly like
`code/side-keyhunt/repair_parse.py` (`repaired_offsets.json` over
`data/upstream-ct_R5005.txt`). All @-offsets 0-based repaired-stream pair
indices. For each window: (a) byte-exact re-derivation of the window;
(b) check 84's predecessor/successor against C1–C3; (c) check the 'on'
licensing grade from the 84-successor census
(battery-fence-84-29-gate: @260 succ 74 = NO-CONTRADICTION; @1501 succ
33 = NO-CONTRADICTION); (d) test the subject-frame contact; (e) answer the
two adverses carried from the parent report.

## Window-level evidence

### W1 @261 (row a2_02, offset-0)

Byte-exact (0-based):
`32@257 43@258 77@259 84@260 74@261 45@262 93@263 52@264 33@265 42@266`

- Predecessor contact: 84@260 -> 74@261, the ONLY 84->74 bigram
  stream-wide (84->74 x1 of 25 84-windows).
- Left: 77@259='le' (provisional). Right: 45@262='ce' (granted, A4 hold);
  93@263 verb-class per R19.
- Reading under licensed 'on': "on(84) 74" — a subject pronoun directly
  precedes 74, placing 74 in the finite-verb slot. Subject-frame contact:
  predecessor-side.

### W2 @1500 (row a7_11, offset-0)

Byte-exact (0-based):
`66@1494 15@1495 59@1496 24@1497 89@1498 41@1499 74@1500 84@1501 33@1502 42@1503 33@1504 00@1505 86@1506`

- Contact: 74@1500 -> 84@1501, the ONLY 74->84 bigram stream-wide
  (74->84 x1 of 34 74-windows).
- Right: 84@1501='on' (licensed, see clause 2), 33@1502 INF class.
- Reading under licensed 'on': "74 on(84) [33-INF]" — inversion shape
  "[V] on [INF]": 74 directly precedes the licensed subject pronoun with an
  infinitive-class complement, placing 74 in the finite-verb slot.
  Subject-frame contact: follower-side (inversion).

## Per-clause pass/fail

1. **Clause 1: PASS.** 84='on' is licensed at @260:
   - C1: 77@259->84@260 is one of the 7 promoted 'l'on' elision legs.
     Re-verified this run: exactly 7 77->84 legs stream-wide
     (84-positions 146, 260, 1058, 1447, 1485, 1764, 1803); @260 included.
   - C2: collision-62-84 kill stands; no 62 contact at this window.
   - C3: @260 is not R1 or R2; the 84-successor census grades @260
     (succ 74, value open) NO-CONTRADICTION — 74's open value contradicts
     nothing about 'on'.
2. **Clause 2: PASS.** 84='on' is licensed at @1501:
   - C1: no 77 contact here; nothing to violate (C1 is a support leg for
     elision windows, not a universal requirement; C2 resolves 84='on'
     unconditioned).
   - C2: 84='on' holds unconditioned; no 62 contact.
   - C3: @1501 is not R1 or R2; graded NO-CONTRADICTION (succ 33=INF
     class) — under the inversion reading the infinitive is governed by 74,
     not 'on'.
3. **Clause 3 (kill arm): FIRES.** 'on' is licensed under the stated
   conditions at BOTH windows. 74 shows subject-frame contact at two
   independent positions: predecessor-side at @261 ("on 74": subject pronoun
   requires a finite verb) and inversion-side at @1500 ("74 on [INF]":
   inversion requires a finite verb). The nominal/formula reading of 74
   cannot sit in the finite-verb slot in either frame. The formula
   hypothesis for 74 is killed.

## Verdict: KILL

The nominal/formula hypothesis for 74 is killed: under A15's conditions
C1–C3 (all verified holding at both windows), 'on' is licensed at @260 and
@1501, and 74 occupies the finite-verb slot in both the "on 74" and the
"74 on [INF]" frames. A whole-word noun or formula cannot occupy those
slots in French.

Scope of this kill (jurisdictional, §7):
- This is NOT a verb promotion for 74. Promotions are red-team-ratified
  only. 74's class stays open at battery grade.
- It does NOT re-litigate the standing `ne-alone-02-74` kill: that kill used
  the follower test set {80, 89, 29, 85, 33} on 02+74 windows; this battery
  uses a subject-frame test on two different windows. Both stands hold.
- §7 intact: 67 et/veut remains the sole true polyvalence — no second
  polyvalence is declared for 74 here; the 84='on' grant is used, not
  unconditioned-killed; no new value is named (49, 74, 93 stay open; 77
  stays provisional).

## Adverses answered

- Target's `adverses` field: null (none listed). The two caveats carried
  from the parent report are answered below, not ignored.
- **Adverse 1 — 93's verb-class (R19) breaks the old "governor + ce + NOUN"
  parse downstream of @262='ce'.** Answered as fenced, not blocking: the
  tested contact is predecessor-side (84->74); the 93 tension concerns the
  downstream parse of "ce 93 ...", which is a red-team-level tension out of
  battery scope. The subject-frame contact at @261 stands independently of
  how 45-93 resolves.
- **Adverse 2 — "41 74" could be a word unit (cf. the "82-84 = mon"
  word-unit precedent), collapsing the W2 inversion parse.** Answered at
  battery grade: 41->74 is a hapax — 1 of 19 41-windows, with 17 distinct
  followers of 41 (12x2, 15x2, 06, 01, 08, 98, 17, 10, 20, 41, 09, 19, 88,
  65, 53, 74, 62). No word-unit signature (a unit bigram would dominate 41's
  follower profile). Additionally, 74's predecessor census (34 windows)
  shows no modal left-contact: '74' x6, 49 x5, 94 x3, 39/44/36 x2 each, and
  14 distinct singletons including 84 and 41. The "82-84 = mon" precedent
  does not generalize; no 41-74 word unit is available.

## Residual tension (for the red team, not a battery act)

The doubling family ('74 74' x6 at first-indices 417, 816, 861, 919, 1053,
1637) independently contradicts whole-word verb-74 at kill grade per the
noun-74-census NULL. A wholesale verb-74 reading is therefore unavailable
at battery grade, and declaring one would need a red-team polyvalence
ruling (barred at battery level, §7: 67 sole). The subject-frame contact at
@261/@1500 stands as window-local evidence; the class question for 74
stays red-team territory. Canonicality caveat stands: rows a2_02 and a7_11
are offset-0 rows with unvalidated upstream offsets (68 of 70).

## Follow-ups

None required: the bar's kill arm fired, so the else-branch ("fence the
contact as conditional") does not fire, and §4 mandates follow-ups only
for nulls. Open sibling surfaces already in the queue: `unit-49-74-74`
(the '49 74 74' unit hypothesis) and `formula-49-value` (naming 49's
class) — this kill does not duplicate either.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-subj-74-261-1500.md` (this file).
- Queue: `battery-queue.json` — `subj-74-261-1500` status `queued` ->
  `verdict`, result `kill`, date 2026-10-09 (temp-file + rename; pre-write
  assert confirmed queued/verdictless; JSON re-validated post-write; only
  this entry's keys touched).
- Lock created at start, deleted at end (verified gone).
