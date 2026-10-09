# Battery report: wordbound-30-06-importent — "30 06" x4 word boundary via 06's left-attachment profile

- Target: `wordbound-30-06-importent` (battery-queue.json, priority 2, status queued)
- Claim: "resolve the '30-06' x4 word boundary via 06's left-attachment profile"
- Worker: ag-990be61d
- Date: 2026-10-09
- Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`). `canonical.py` NOT used. R5005 untouched.
- All @-offsets are pair indices in the repaired stream.
- Lock: `code/crowd17/next-token/locks/wordbound-30-06-importent.lock` created on start; no stale lock present.

## Bar (verbatim, pre-registered)

"resolve iff 06's left-attachment profile decides the boundary (cf. ent-06 battery's 'mentent' x2 legs); one-word gives 'importe' its first non-@1702 word-level leg, two-word is neutral."

Numbered clauses (frozen before testing):
1. 06's left-attachment profile, derived from all 06 windows on the repaired stream, decides the "30 06" boundary.
2. If one-word: 'importe' earns its first non-@1702 word-level leg ("importent").
3. If two-word: neutral (no movement for 'importe').

## Method

Parsed the repaired stream fresh (1,847 pairs confirmed; n(06) = 44, re-derived).
For each of the 44 06-windows recorded the left neighbor and classified it
against standing values: STEM (known letter/stem: 82=m, 12=n, 34=i, 29=er,
40=e, 70=pre), WORD (known word: 11=la, 64=qui, 84=on, 87=ce, 96=par,
17=fois, 79=tout, 00=pour, 59=est, 47=ce, 46=que, 77=le), OPEN (value open).
94 classified OPEN throughout: its 'ne' value is battery-promoted pending
ratification AND a standing polyvalence candidate (94 census: 28/37 windows
not grammatically attachable as particle-ne). The four target windows:
"30 06" @1251/@1327/@1561/@1733 (06 at @1252/@1328/@1562/@1734).

## Window-level evidence

The four target windows (wide context, 30 at @w, 06 at @w+1):
- @1251: `00 67 46 26 | 30 06 | 65 46 01 61 31` (rows a7_01/a7_02)
- @1327: `08 62 98 56 | 30 06 | 62 94 70 52 39` (rows a7_04/a7_05)
- @1561: `40 17 11 26 | 30 06 | 60 71 50 29 24` (row a8_01)
- @1733: `30 15 01 56 | 30 06 | 60 12 48 52 86` (row a8_07)

06 left-attachment census (all 44, L = left neighbor):

STEM-attach legs (06 word-internal, attaches leftward onto stem/letter) — 9:
- @580/@581: `94 82 06 06 50` = "ne mentent" — first 06 attaches onto 82='m', second 06 word-internal by construction.
- @1184/@1185: `94 82 06 06 59` = "ne mentent est" — same mechanism, second instance (the bar's "mentent x2 legs" confirmed byte-exact).
- @738: `82 06 00` = "m"+"ent"+"pour" — "ment" (3sg of mentir) + "pour"; 06 left-attaches onto 82.
- @1120: `70 12 06 14` = "pre"+"n"+"ent" — "prennent/prenent" shape; 06 left-attaches onto 12='n'.
- @1355: `82 06 52` = "m"+"ent"+[52]; 06 left-attaches onto 82 (52's continuation open).
- @1709: `12 06 29 40` = "n"+"ent"+"er"+"e"; 06 left-attaches onto 12='n' (same mechanism as @1120; full word unidentified, mechanism leg only).
- @1747: `40 06 65` = "e"+"ent"+[65] — "creent"-shaped (vowel-final stem + -ent, cf. "creent", "agreent"); 06 left-attaches onto 40='e'.

WORD-boundary legs (06 does NOT attach leftward; stands word-initial after a known word) — 6:
- @271: `11 06 67` = "la"+"ent"+[67] — boundary after 11='la'.
- @370: `17 06 21` = "fois"+"ent"+[21] — boundary after 17='fois'.
- @522: `77 06 55` = "le"+"ent"+[55] — boundary after 77='le' (provisional).
- @789: `84 06 77` = "on"+"ent"+"le" — boundary after 84='on'.
- @1080: `64 06 52` = "qui"+"ent"+[52] — boundary after 64='qui'.
- @1667: `64 06 91` = "qui"+"ent"+[91] — boundary after 64='qui'.

OPEN (neighbor value open; profile-neutral) — 29, including the four target
windows @1252/@1328/@1562/@1734 (L=30, value contested) and @319 (L=94,
94's class open — 94-06 there is "ne"+"ent", ungrammatical as particle+ending,
consistent with 94's standing syllabic/word-final duality).

## Per-clause results

1. Profile decides the boundary INDEPENDENTLY: FAIL. The profile is
   BIMODAL, not systematic: 06 attaches leftward onto known stems/letters
   (9 legs) and stands word-initial after known words (6 legs). The
   boundary for "30 06" is therefore downstream of 30's class — the profile
   alone cannot decide it. The bar's hoped-for "mentent"-only systematicity
   does not survive the full 44-window census.
2. One-word -> 'importe' leg: NOT AVAILABLE. One-word under the standing
   promoted 30='pas' is "pasent" — a non-word, and the clerk single-
   consonant license for it is dead at kill grade (spell-pasent-test,
   2026-10-08). One-word "importent" (real 3pl) requires 30='importe',
   which would contradict the standing promoted 30='pas' — not decidable
   at battery level.
3. Two-word: HOLDS under standing values, and is NEUTRAL per the bar.
   Under 30='pas' (promoted; its promotion rests on independent ne-frames
   @558/@1713/@651->656/@1363->1368, no circularity), 30 is a word, so the
   bimodal profile places 06 word-initial: "pas" + "ent[65/62/60]" with
   rightward attachment. The 6 WORD-boundary legs confirm 06 does stand
   word-initial in exactly this configuration. Followers 65/62/60 are
   value-open, so "ent"+follower word formation is untestable — neutral,
   as the bar states.

## Adverses (answered, not ignored)

- **"boundary underdetermined ('pas [verb]-ent' two-word also parses);
  coordinate with queued spell-pasent-test, do not duplicate":** the
  underdetermination is CONFIRMED and now characterized: it is not 06's
  doing (06's profile is bimodal and consistent) but 30's — the boundary
  follows 30's class. spell-pasent-test (verdict 2026-10-08) is cited, not
  re-run: its kill of the "pasent" clerk spelling is what closes the
  one-word-under-'pas' reading here.
- **No standing verdict contradicted or downgraded.** pas-30's promotion,
  06='ent', the mentent/prennent legs, and the 94 duality all hold; the
  two-word parse under standing values is profile-consistent. Per protocol
  no escalation is needed (nothing contradicts a red-team verdict).

## Verdict

**null** — the profile does not independently decide the boundary; it is
bimodal (stem-attach vs word-initial), so "30 06" follows 30's class.
Under the standing promoted 30='pas' the boundary is two-word, which the
bar declares neutral. 'importe' gains no word-level leg; nothing is killed.
The one-word "importent" reading survives ONLY as a conditional on a future
re-opening of 30's value (pas-30's own adverse flags ne-30-1700 as the
re-opener). Work regenerates below.

## Follow-ups (null regenerates work; supervisor to queue)

1. `importe-30-reopen-gate` (P3, gated) — re-run this battery's boundary
   test if 30's value ever re-opens (gate: ne-30-1700 demonstrates
   30='importe' at @1702, or pas-30 is otherwise re-opened). Bar: one-word
   "importent" promotes 'importe' to its first non-@1702 word-level leg;
   else boundary stays two-word.
2. `ent-right-attach-sweep` (P2) — classify 06's RIGHTWARD attachment in
   the 6 word-initial legs (@271/@370/@522/@789/@1080/@1667): does
   "ent"+follower ever form a real French word? Bar: kill the two-word
   "pas"+"ent[65/62/60]" parse at the four target windows iff >=2 of the 6
   control legs force non-words on the rightward attachment.
3. `30-06-follower-60-65` (P3, gated on 60/65 values resolving) — once 60
   and 65 are named, test "ent"+[60/65] word formation at
   @1252/@1328/@1562/@1734; decides whether the two-word parse's rightward
   attachment is real French or a fenced residual.
