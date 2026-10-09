# Battery report: importe-30-elision-test — vowel-initial value test for 30

- Target: `importe-30-elision-test` (battery-queue.json, priority 2, status queued)
- Claim: "vowel-initial value test for 30 across all 19 @30 windows ('importe' rival)"
- Worker: ag-1777ba61
- Date: 2026-10-08
- Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`). `canonical.py` NOT used. R5005 untouched.
- All @-offsets are pair indices in the repaired stream.
- Lock: `code/crowd17/next-token/locks/importe-30-elision-test.lock` created on start; no stale lock present.

## Bar (verbatim, pre-registered)

"kill 30='importe' iff >=1 window forces consonant-initial 30; promote-consideration iff a second grammatical 'n\'importe' frame is found"

Numbered clauses (frozen before testing):
1. >=1 window forces consonant-initial 30 -> kill 30='importe'.
2. A second grammatical "n'importe" frame is found (besides @1702) -> promote-consideration for 30='importe'.

## Method

Parsed the repaired stream fresh (1,847 pairs confirmed; n(30) = 19, re-derived).
For each of the 19 windows recorded predecessor, successor, and nearest
upstream 94. Tested two things per clause:

- Clause 1: elision-orthography scan — any window where 30 directly follows
  an eliding particle written UNELIDED forces consonant-initial (a vowel
  there would have forced elision). Standing eliding particles: 94='ne'
  (battery-promoted, ratification pending), 77='le' (provisional). Also
  scanned for word-internal composition forcing a consonant onset.
- Clause 2: "n'importe" needs 94 directly before 30 (n'-elision needs
  adjacency; the compound does not split). Census all 19 windows for a
  second 94-30 adjacency with a grammatical frame.

Standing values used: banked pencil (11=la, 70=pre, 82=m, 34=i, 29=er, 40=e,
46=que), promoted/granted (87=ce, 64=qui, 96=par, 17=fois, 79=tout, 00=pour,
84=on, 47=ce), battery-promoted 94='ne' (caveat inherited), provisional
59='est', 77='le', 06='ent' (verb ending, promoted 2026-10-08), 24=finite
verb (class-level promote), 12='n'/48='e' letters. 67 et/veut sole
polyvalence respected. NOT assumed: 33's value (dire/croire tie), 85's
value, 26's class, 20's value.

## Window-level evidence

Predecessor census (19 windows): 24 x3 (@30/@1269/@1729), 26 x4
(@656/@993/@1251/@1561), 52 x2 (@483/@1309), 59 x2 (@560/@1716), 56 x2
(@1327/@1733), 81 x1 (@45), 20 x1 (@742), 38 x1 (@1114), 48 x1 (@1222),
03 x1 (@1368), 94 x1 (@1702).

94-30 adjacency census: @1702 is the SOLE 94-30 adjacency in the stream
(re-derived; matches ne-30-1700). Elision applies there ("n'importe"),
consistent with vowel-initial 30. No other window has an eliding particle
directly before 30: 77='le' never directly precedes 30; 24 is a finite verb
(no elision); 59='est' does not elide; 48 is the letter 'e' (word boundary
at @1222: "e"+"pas"/"e"+"importe" are both non-words, so boundary, no
forcing either way).

Clause-1 per-window forcing check (does the window REQUIRE consonant-initial?):
- @560 "86 94 59 30 67" ('n'est [30]'): 'pas' parses ("n'est pas"), but a
  vowel-initial predicative also parses ("n'est autre"-shaped). Not forced.
- @1716 "94 44 59 30 64" ('ne [44] est [30]'): same — vowel-initial adverb
  ("aucunement"-shaped) parses. Not forced.
- @30/@1269/@1729 "24 30" ([modal-verb] [30]): "24 pas" parses; vowel-initial
  infinitive ("peut entrer"-shaped) also parses. Not forced.
- @656/@993/@1251/@1561 "26 30": 26's class open (noun-26 null); no value
  forces the onset. Not forced.
- @483/@1309 "52 30", @45 "81 30", @742 "20 30", @1114 "38 30",
  @1368 "03 30", @1327/@1733 "56 30", @1222 "48 30": all neighbors open or
  non-eliding; no word-internal composition demonstrable (all neighbor
  values needed for a compound are open). Not forced.
- @1702 "94 30": elision APPLIES ("n'importe") — actively consistent with
  vowel-initial, the opposite of forcing.

Result: ZERO windows force consonant-initial 30. Clause 1 not satisfied.

Clause-2 second-frame search: "n'importe" needs 94-30 adjacency. Only @1702
qualifies. The finite-verb vehicle ("[subj] importe") was also swept: no
window yields a grammatical subject-headed parse under GRANTED values only
(@1561 "17 11 26 30" = "fois la [26] [30]" needs ungranted noun-26;
@1309 "77 74 52 30" needs ungranted 74/52; @1327 "62 98 56 30" needs
ungranted 62='il'). No second "n'importe" frame. Clause 2 not satisfied.

Observation (not a bar trigger, flagged for follow-up): "30 06" x4
(@1251/@1327/@1561/@1733) with 06='ent' verb ending. If "30-06" is ONE word,
30='importe' gives "importent" (real 3pl of importer) while 30='pas' gives
"pasent" (non-word) — the boundary is underdetermined ("pas [verb]-ent" two
words also parses), so this stays an observation, owned by follow-up 1.

## Per-clause results

1. >=1 window forces consonant-initial 30: FAIL — 0/19 windows force it.
   Elision scan clean; @1702's applied elision is vowel-consistent.
2. Second grammatical "n'importe" frame: FAIL — sole 94-30 adjacency is
   @1702; no subject-headed finite-verb parse under granted values.

## Adverses (answered, not ignored)

- **"word-formation level only — clause-level parse needs open 85/33
  values":** CONFIRMED and respected. This battery stayed at
  word-formation/elision level by design. The clause-level parse of @1702
  still needs 85's value and the 33 dire/croire tiebreak — owned by queued
  `stem-85-then-1700`, not re-decided here.
- **No contradiction with pas-30's promotion** (2026-10-08): this battery
  does not re-vote 30='pas'; the phonological test returns negative on both
  clauses, which neither confirms nor re-opens pas-30. No downgrade.
- **No red-team verdict touched.** 94='ne' used with ratification-pending
  caveat; no new polyvalence declared (§7 respected).

## Verdict

**null** — 'importe' is neither killed nor advanced. No window forces
consonant-initial 30 (kill clause fails); no second "n'importe" frame exists
(promote-consideration fails). The rival stands exactly where ne-30-1700 left
it: conditional word-formation at @1702 ("n'importe", stream-unique 94-30
adjacency, elision-licensed), with no clause-level parse under standing
values. Work regenerates below.

## Follow-ups (null regenerates work; supervisor to queue)

1. `wordbound-30-06-importent` — "30-06" x4 (@1251/@1327/@1561/@1733):
   if one word, 30='importe'+06='ent' = "importent" (real 3pl) vs
   30='pas'+"ent" = "pasent" (non-word) — the boundary discriminates the
   vowel-initial rival. Bar: resolve iff 06's left-attachment profile
   decides the boundary (cf. ent-06 battery's "mentent" x2 legs); one-word
   gives 'importe' its first non-@1702 word-level leg, two-word is neutral.
2. `importe-30-subject-sweep` — finite-verb vehicle sweep over all 19
   windows under granted values only (@1561 "17 11 26 30" gated on noun-26;
   @1309 "77 74 52 30" gated on 74/52; @1327 "62 98 56 30" gated on 62).
   Bar: promote-consideration iff >=1 window parses "[subj] importe" with a
   granted subject; else record 'importe' as @1702-word-formation-confined.
3. `elision-30-retest-after-26` — gated retest: 26 directly precedes 30 in
   4/19 windows (largest predecessor share); re-run the vowel-initial test
   once noun-26 resolves (verb-shaped 26 changes "26 importe" readings;
   nominal 26 makes "la [26] importe" testable at @1561).
