# Battery report: nest-subject-86-62-42

Target: `nest-subject-86-62-42` — claim "86, 62, 42 are subject-shaped before 'n\'est'".
Worker: a5ae40ad-bb30-4a18-9a91-01c6ff7740c8. Date: 2026-10-08. Stream: repaired
1,847-pair parse (code/side-keyhunt/repair_parse.py method; canonical.py NOT used).
Lock: no pre-existing lockfile for this target (no stale-lock note needed).

## Bar (verbatim, pre-registered)

"resolve iff each of {86, 62, 42} takes a subject parse consistent with its contact
profile with zero forced contradiction; else fence the failing slot"

## Bar restated as numbered pass/fail clauses

1. 86 takes a subject parse consistent with its contact profile, with zero forced
   contradiction — else fence the 86 slot.
2. 62 takes a subject parse consistent with its contact profile, with zero forced
   contradiction — else fence the 62 slot.
3. 42 takes a subject parse consistent with its contact profile, with zero forced
   contradiction — else fence the 42 slot.

## Method

Re-parsed the repaired stream from `code/side-keyhunt/repaired_offsets.json` +
`data/upstream-ct_R5005.txt` with the repair_parse.py tokenizer (byte-exact
upstream tokenization, a5_03 offset 0). Verified 1,847 pairs. Census of all
`X 94 59` trigrams stream-wide; full predecessor/successor contact profiles for
86, 62, 42; all `86 94` / `62 94` / `42 94` windows with context; left/right
clause-boundary checks at each locus. Every count below traces to the stream.

## Anchor note (repaired-stream offsets)

The three `X n'est ...` frames are the ONLY `X 94 59` trigrams in the 1,847-pair
stream. @-anchors below are on the 94 (the n' of n'est); physical subject-cell
indices given in parentheses:

- @558 — X=86 (86@557): row a3_01. Left context `@553-557: 86 59 34 17 86`;
  frame `@557-560: 86 94 59 30`; right `@561-563: 67 11 43`.
- @762 — X=62 (62@761): row a5_03. Physical locus `@760-764: 20 62 94 59 39`.
  NOTE: the queue's "post-repair @760 finder-anchored" is the 20-cell anchor of
  this same locus (frame-20-62-94 finder convention); the 94-anchor on the
  repaired stream re-derives at @762. Same physical frame, no conflict.
- @1795 — X=42 (42@1794): rows a8_09->a8_10. Left context `@1791-1793: 00 86 56`
  (the 'pour-86-56' formula tail ends at @1793); frame `@1794-1797: 42 94 59 37`;
  right `@1798-1800: 91 79 87`.

Independence: the three predecessors sit on three different rows (a3_01, a5_03,
a8_09) — three independent loci, as claimed.

## Window-level evidence

### Slot 86 @557 ('86 n'est 30')

Parse: previous clause ends at @556 (17='fois', promoted; "...est [34][17]" —
@554=59 provisional 'est', @555=34='i' GT). New clause: "[86] n'est pas, et
[11][43]..." — 86 is the subject of a negated clause; 94='ne' (promoted), 59=
'est' (provisional), 30='pas' (promoted today); @561=67 -> follower 11='la' so
67='et' per the §7 positional rule ("X n'est pas, et la 43..." — grammatical
clause boundary).

Contact profile (n=32): pre = 00 x12 ('pour'-governed, A9 INF-class grant),
77 x5, 67 x3, 83 x2, 87/97/17/11/66/96/37/98 x1; suc = 29 x4 ('er' stems),
56 x4 ('00 86 56' formula), 24/01/52/66 x2, 21/91/59/94/50/48 x1.

Subject-parse fit: the noun/substantivized-infinitive face of the INF class —
"lire n'est pas facile" is grammatical French. Direct noun-slot evidence exists:
77->86 x5 = 'le 86' (under provisional 77='le'). 86->59 x1 gives a second
"86 est" subject window. This window is 86's ONLY '86 94' contact, so no window
forces 86 away from noun-hood; no finite-verb or clitic forcing anywhere in
the profile.

### Slot 62 @761 ('62 n'est 39')

Parse: locus `@760-764: 20 62 94 59 39 88`. Under the standing collision-62-84
verdict (2026-10-08, kill-grade): 84='on' holds unconditioned, 62='on'
unconditioned ELIMINATED, and all nine 62->94 windows re-read as 'il ne'
(8 clean + @508 fenced). This window reads "il n'est à [88]..." — 39='a/à'
(promoted today): "il n'est à X" is grammatical French. 62 is the subject.

Contact profile (n=35): pre = 21 x5, 20 x4, 74 x3, 93/03/08/78/92 x2;
suc = 94 x9, 48 x6, 98 x5, 16 x4, 61/06 x2. The nine 62->94 windows are exactly
the collision battery's 'il ne' set; zero 62->59 crossover, consistent with
62 in subject position taking 'ne' before the verb. No window forces a
contradiction with the subject parse at @761.

### Slot 42 @1794 ('42 n'est 37')

Parse: left edge `@1791-1793: 00 86 56` = 'pour-86-56' formula (A9/A14), so a
clause boundary sits before @1794. New clause: "[42] n'est [37]..." with right
context `91 79 87` = "[91] tout ce" (79='tout', 87='ce' promoted): 42 is the
subject, 37 is predicative (A1 grants 37/32/42 predicative frames after 'est';
"X n'est [adj]" is the classic negative predicative). Grammatical end to end.

Contact profile (n=20): pre = 29 x3, 76 x3, 33 x2, 59 x2 (A1 'est 42'
predicative x2), 63/61/78/48/24/74/52/56 x1; suc = 06 x5, 98 x3, 94 x3, 16 x2,
44 x2, 48/63/96/41/33 x1. 42's two other '42 94' windows also admit the subject
reading: @493 '78 42 94 02' = "[42] ne [02]..." (subject + ne + verb) and
@784 '24 42 94 74' = "[42] ne [74]..." — neither forces a non-noun 42. Nothing
in the profile contradicts a noun-shaped subject at @1794.

## Adverses (answered, none ignored)

1. "86 is 'pour'-governed x12 ('pour 86') — infinitive/noun pull vs subject
   position": ANSWERED, not a contradiction. 'pour 86' x12 is the
   prepositional-complement face of the A9 INF class; the subject face is the
   substantivized infinitive / noun ("pour comprendre" vs "comprendre n'est pas
   facile" — same item, different slot). Direct noun-slot evidence: 77->86 x5
   ('le 86', under provisional 77='le'). Zero forced contradiction.
2. "59='est' provisional (inherited)": ANSWERED as a stated condition, not
   ignored. All three windows load on 59='est'. The est-59-frames battery
   PROMOTED the 'n'est'-frame claim today (2026-10-08), hardening this input;
   this verdict remains conditional on the provisional 59='est' standing.

## Per-clause verdicts

1. 86 subject parse: PASS. Zero forced contradiction; contact profile
   (INF-class, 'le 86' x5 noun face, 86->59 x1 second subject window) consistent.
2. 62 subject parse: PASS. Reads "il n'est à..." under the collision battery's
   demonstrated 62='il' rival (demonstrated, NOT promoted — flagged, not
   assumed). Zero forced contradiction.
3. 42 subject parse: PASS. Reads "[42] n'est [37]..." with A1-predicative 37;
   the other two '42 94' windows admit the same subject shape. Zero forced
   contradiction.

## Verdict

**promote** — all three bar clauses pass; both adverses answered (one
re-parsed clean, one fenced as a stated condition). The claim "86, 62, 42 are
subject-shaped before 'n'est'" is confirmed on the repaired stream. No
contradiction with any standing red-team verdict (consistent with
collision-62-84's 'il' rival and with the A1 predicative grants). No follow-up
targets proposed — no null.

Caveats carried forward (do not weaken the verdict): (a) conditional on
provisional 59='est'; (b) 62's subject value is the demonstrated-not-promoted
62='il' rival; (c) 86's subject face is the substantivized-infinitive/noun
reading, 'le 86' x5 loads on provisional 77='le'; (d) 94='ne' and 30='pas'
promotions are battery-level pending ratification; (e) canonicality caveat
(§7) stands.
