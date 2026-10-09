# Battery verdict: ce28-contact

Worker: 4b052112-8dba-4654-9bf7-97fa9870cd92. Date: 2026-10-09.
Lock: code/crowd17/next-token/locks/ce28-contact.lock (created 2026-10-09T06:46:01Z; no prior lock).
Target id: ce28-contact. Queue status at take: queued, priority 2, no verdict.
Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json +
data/upstream-ct_R5005.txt, parsed like code/side-keyhunt/repair_parse.py).
canonical.py never used. R5005, sealed gates, red-team adjudication queue untouched.
No data invented. @-offsets are 0-based stream indices.

## Bar (pre-registered verbatim from battery-queue.json, BEFORE testing)

"Adjudicate the '45 28' bigram x2 (@104/@697) - is 45='ce' at @697 ('02 50 45 28 94')? If 45 is not 'ce' there, the @698 constraint on 28 loosens and 'donc' revives."

Numbered clauses:
1. The '45 28' bigram occurs exactly twice in the stream (@104/@697) — confirm both.
2. At @104 ('59-45-28'): determine whether the window requires 45='ce' or permits a non-'ce' reading.
3. At @697 ('02 50 45 28 94'): adjudicate whether 45='ce' holds there.
4. Conditional consequence: if 45 is not 'ce' at @697, record that the @698 constraint on 28 loosens and 28='donc' revives.

## Method

1. Re-derived the stream in-session (1,847 pairs confirmed). Re-derived:
   45-28 contacts (0b @104/@697, exactly x2), n(45)=22, n(28)=6
   (@105/@286/@698/@747/@1573/@1751), 50-45 contacts (0b @331/@696, exactly x2),
   94->60 contacts (0b @699, exactly x1 — hapax).
2. Re-derived the post-78 vs non-post-78 follower partition for 45 (byte-exact).
3. Substituted standing values into both windows: 59='est' (provisional),
   00='pour' (A9), 46='que' (GT), 11='la' (GT), 94='ne' (battery-promoted),
   12='n' (letter, battery-promoted). 28, 02, 50, 74, 60, 98 left open.
4. Checked for any admissible battery-level alternative to 45='ce' at @697.

## Window-level evidence

**@104 (a1_02->a1_03):** `100:62 101:94 102:93 103:59 104:45 105:28 106:00 107:46 108:11`
= "...est(59) ce(45) [28] pour(00) que(46) la(11)...". The 'est-ce [28]' frame
(est-ce-104) is consistent with 45='ce'. Predecessor of 45 is 59 (not 78).
No window-specific evidence against 45='ce'.

**@697 (a5_00->a5_01):** `693:74 694:46 695:02 696:50 697:45 698:28 699:94 700:60 701:12 702:98`
= "...[74] que(46) [02] [50] [45] [28] ne(94) [60] n(12) [98]...".

Evidence for 45='ce' at @697:

- **P1 (positional):** predecessor of 45 at @697 is 50, not 78. The refined
  positional candidate (45='dict' iff 78 word-medial, escalated R18-026) does
  not fire here: its condition is false, so it yields 'ce'. The general
  syllable rival is positionally excluded; the general second value is barred
  by the S7 sole-polyvalence rule (67 et/veut) at battery level.
- **P2 (distributional partition, re-derived byte-exact):** the 4 post-78 45s
  (0b @314/@574/@983/@1165) take followers {64, 13, 01, 13}; the other 18 45s
  take followers {08, 23 x3, 28 x2, 36, 46, 54, 58, 64 x2, 88, 91, 93 x3, 94}
  — zero 13, zero 01. The {13,01}-exclusivity holds exactly. 28 is a
  non-post-78 'ce'-tier follower, on the same side of the partition as
  'ce'-followers 91/93/23/54/88/46/94/08/58/36.
- **P3 (host inventory):** dict-45-host-inventory (promote) certifies 'verdict'
  as the sole '-dict-' host; @697 is not among the four post-78 hosts.
- **P4 (sibling bigram):** the other 50-45 contact (0b @331):
  `327:01 328:19 329:00 330:92 331:50 332:45 333:54 334:88`
  = "pour(00) [92] [50] ce(45) [54] [88]" — no contradiction with 45='ce' in
  the identical bigram.
- **P5 ('ne [60]' frame resolves):** 94->60 is a hapax (only at @699), so the
  'ne' frame has no independent distributional support — but @700 is a bare-60
  verb window per split-60-verbs (promote: bare-60 verb V1–V4 includes @700).
  "ne(94) [60-verb]" parses as negation; no contradiction with 45='ce'.
- **P6 (no admissible alternative):** at battery level there is no rival value
  for 45 at @697 — the 'dict' rival is positionally excluded (P1–P3) and a
  general second value is barred by S7. A positional split would be a red-team
  act, and the escalated candidate does not cover this window anyway.

## Per-clause pass/fail

1. **'45 28' x2 confirmed: PASS.** Contacts at 0b @104/@697 exactly (n(45)=22,
   n(28)=6 re-derived).
2. **@104 adjudicated: PASS.** "est(59) ce(45) [28] pour(00) que(46) la(11)"
   is the natural parse under standing values; pre=59; 28 is 'ce'-tier;
   no contrary byte evidence.
3. **@697 adjudicated: PASS.** 45='ce' holds: positional (P1), distributional
   (P2), host-inventory (P3), sibling-bigram (P4), and negation-frame (P5)
   evidence all agree; no admissible battery-level alternative (P6).
4. **Conditional consequence: RECORDED.** The antecedent (45 not 'ce' at @697)
   is false at battery grade, so the consequence is moot: the @698 constraint
   on 28 stands, and 28='donc' stays killed (donc-28-triangulate's kill
   condition, clause 3, is now FINAL).

## Adverses answered

- "45='ce' is A11 HOLD": ANSWERED — the HOLD is honored, and independently
  corroborated (P1–P6), not merely assumed. The adjudication agrees with the
  standing red-team verdict; nothing is downgraded or contradicted.
- "@697's window '[02] [50] [45] [28] ne(94)' needs its own adjudication":
  ANSWERED — window parsed with standing values; the 'ne [60]' frame resolves
  via split-60-verbs; 28 stays unnamed (no 28 value is needed to settle the
  45 question); no contradiction found, no forced alternative.

## Caveats

- The refined positional candidate (45='dict' iff 78 word-medial, R18-026) is
  still red-team-escalated, not granted. If granted, @697 still reads 'ce'
  (pre=50), so this adjudication is grant-robust.
- 28's value stays unknown. The full @697 window still has open values
  (02, 50, 74, 98; 60's value unnamed). The queued `x-pour-que-paradigm`
  target discriminates 28's remaining candidates (bien/aussi/encore/la) by
  distribution.
- frame-74-45-93's conditional tripwire (bar b) is noted but not triggered
  here: it concerns the 45->93 windows, not @697.

## Verdict: PROMOTE

The adjudication is settled at battery grade: 45='ce' at @697 (and @104).
The @698 "ce donc" contact stands; 28='donc' stays killed. No follow-ups
required (null-only rule); the `x-pour-que-paradigm` pointer above is a
standing queue item, not a new proposal.

## Bookkeeping

Report: code/crowd17/report_inbox/battery-ce28-contact.md. Queue updated via
temp-file + rename (ce28-contact: queued -> verdict/promote; pre-write assert
confirmed status was queued with no prior verdict; JSON re-validated).
Lock deleted on completion.
