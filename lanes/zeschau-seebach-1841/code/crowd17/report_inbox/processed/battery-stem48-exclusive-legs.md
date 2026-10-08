# Battery report: stem48-exclusive-legs — 2026-10-08

Worker: d03cc915-a403-42ad-ab8f-8b755c70f52a. Stream: repaired 1,847-pair parse
(code/side-keyhunt/repaired_offsets.json + data/upstream-ct_R5005.txt, parsed per
code/side-keyhunt/repair_parse.py). @-offsets below are the pair index of 48 itself.
n(48) = 38 on the repaired stream. Lock: locks/stem48-exclusive-legs.lock (no stale lock present).

## Bar (verbatim, pre-registered)

"retire-frame iff zero windows require the stem reading (a window requires the stem reading iff it is ungrammatical under standing 48='e'); hold-frame iff >=1 requires it AND letter-'e'-required windows stay below 10%. Full 38-window sweep."

## Numbered clauses

1. RETIRE: the frame retires iff ZERO windows require the stem reading, where a
   window requires the stem reading iff it is ungrammatical under standing 48='e'.
2. HOLD: the frame holds iff (>=1 window requires the stem reading) AND
   (letter-'e'-required windows < 10% of 38, i.e. at most 3 windows).
   Letter-'e'-required = ungrammatical under 48=verb-stem (symmetric definition).
3. Full 38-window sweep: every window classified, every number traced to the stream.

## Method

Parsed the repaired stream per repair_parse.py (never canonical.py). Found all 38
windows of 48. For each window I tested two parses: (E) grammatical French with
48 as letter-'e' under standing values (§7 banked/granted/provisional/battery
values); (S) grammatical French with 48 as verb-stem (the A7-L2 frame shapes:
48-29 = "[STEM]er" infinitive, 82-48 = "me [48-verb]"). A bare stem outside those
shapes is ungrammatical (French bare stems are not words). Coordination: queued
fem-e-48's 40-vs-48 final-e distribution is cited, not re-run; queued
w48-boundary-census and elision82-48-x1 are cited where they touch the same windows.

## Evidence — full 38-window sweep

E = parses under 48='e'; S = parses under 48=verb-stem. ✓ clean, ~ admits via open
values, ? doubtful/possible orphan, ✗ ungrammatical.

| @ | pre-48-suc | E | S | class |
|---|---|---|---|---|
| 126 | 82-48-11 | ✓ "me la" | ✗ bare stem + article | letter-e (strong) |
| 170 | 12-48-21 | ✓ "ne" | ✗ "n[STEM]" | letter-e (strong) |
| 283 | 42-48-52 | ✓ "[42]-e" feminine -e (A1) | ✗ | letter-e (strong) |
| 361 | 62-48-76 | ~ admits (62/76 open) | ✗ | letter-e (weak) |
| 365 | 78-48-49 | ~ admits ("[78]e") | ✗ | letter-e (weak) |
| 377 | 85-48-00 | ? "[85] me pour" resists clean parse | ✗ | doubtful |
| 398 | 82-48-06 | ? "me e ent" resists clean parse | ✗ | doubtful |
| 426 | 62-48-76 | ~ admits | ✗ | letter-e (weak) |
| 450 | 32-48-79 | ✓ "est [32]-e toutefois" (79-17 per A5) | ✗ | letter-e (strong) |
| 542 | 29-48-42 | ~ "[44]ere"-shaped admits | ✗ | letter-e (weak) |
| 641 | 89-48-20 | ✓ "[89]-e" verb+ending (A8) | ✗ | letter-e (strong) |
| 710 | 12-48-71 | ✓ "ne" | ✗ | letter-e (strong) |
| 729 | 86-48-88 | ~ admits | ✗ | letter-e (weak) |
| 810 | 12-48-24 | ✓ "ne" | ✗ | letter-e (strong) |
| 856 | 32-48-84 | ~ admits | ✗ | letter-e (weak) |
| 863 | 74-48-47 | ~ admits | ✗ | letter-e (weak) |
| 872 | 89-48-20 | ✓ "[89]-e" | ✗ | letter-e (strong) |
| 928 | 96-48-82 | ? "par e me" resists clean parse | ✗ | doubtful |
| 972 | 98-48-51 | ~ admits | ✗ | letter-e (weak) |
| 987 | 89-48-01 | ✓ "[89]-e" | ✗ | letter-e (strong) |
| 1076 | 12-48-77 | ✓ "ne" | ✗ | letter-e (strong) |
| 1177 | 32-48-59 | ✓ "[74] [32]e est [37]" ("la table est"-shaped) | ✗ | letter-e (strong) |
| 1212 | 32-48-96 | ✓ "est [32]-e par" | ✗ | letter-e (strong) |
| 1221 | 24-48-30 | ~ admits ("[24]e pas") | ✗ | letter-e (weak) |
| 1229 | 82-48-29 | ✗ (see adjudication) | ✓ "me [STEM]er ce" | STEM-REQUIRED |
| 1276 | 76-48-56 | ~ admits | ✗ | letter-e (weak) |
| 1279 | 85-48-53 | ~ "[85]e" finite admits | ✗ | letter-e (weak) |
| 1316 | 62-48-98 | ~ admits | ✗ | letter-e (weak) |
| 1350 | 62-48-77 | ~ admits | ✗ | letter-e (weak) |
| 1398 | 78-48-40 | ? "[78]e e et" resists clean parse | ✗ | doubtful |
| 1465 | 62-48-21 | ~ admits | ✗ | letter-e (weak) |
| 1525 | 11-48-96 | ? "la la e par" resists clean parse | ✗ | doubtful |
| 1570 | 62-48-56 | ~ admits | ✗ | letter-e (weak) |
| 1589 | 65-48-29 | ✗ (see adjudication) | ✓ "[65] [STEM]er ce" | STEM-REQUIRED |
| 1614 | 71-48-31 | ~ admits | ✗ | letter-e (weak) |
| 1658 | 24-48-47 | ~ admits | ✗ | letter-e (weak) |
| 1737 | 12-48-52 | ✓ "ne" | ✗ | letter-e (strong) |
| 1779 | 19-48-74 | ✓ "est [19]-e" | ✗ | letter-e (strong) |

Totals: stem-required 2, letter-e strong 14, letter-e weak 17, doubtful 5. 2+14+17+5 = 38. ✓

### Adjudication: @1229 (a7_01) — "57 64 79 82 48 29 47 33 29 85"

Under 48='e', the trigram 48-29-47 = "e"+"er"+"ce". Exhausted segmentations:
"e"|"er"|"ce" ("er" is not a French word); "e"|"erce" (no word starts "erce");
"eer"|"ce"; "eerce"; 82-48-29-47 = "m"+"e"+"er"+"ce": "me"|"erce", "meer"|"ce"
("meer" is not French), "meerce" (no French word contains "meerce"); elision
"m'" needs a vowel-initial word at 29 ("er..." — none); 29='er' is banked, not
open to re-read. No grammatical parse exists under 48='e'. Under 48=verb-stem:
82-48-29 = "me"/"m'" + [STEM] + "er" (elided "me" + vowel-initial infinitive,
morphologically exact), 47-33-29 = "ce [33]er" (demonstrative + infinitive-as-noun,
33 open). Parses under the stem reading. → REQUIRES the stem reading.

### Adjudication: @1589 (a8_02) — "36 70 64 65 48 29 47 08 81"

Under 48='e': 65-48-29-47 = [65]+"e"+"er"+"ce". Segmentations: "[65]e"|"er"|"ce"
("er" not a word); "[65]"|"eer"|"ce"; "[65]eerce" (no French word contains
"eerce"); 48-29-47 word-internal "eerce" (none). No grammatical parse under
48='e'. Under 48=verb-stem: 65-48-29 = "[65] [STEM]er" (infinitive complement),
47 = "ce". Byte-identical "48-29-47" = "[48]er ce" leg shape (A7-L2). → REQUIRES
the stem reading.

### The letter-'e'-required count (Clause 2 input)

Strong (clean 'e' parse, stem impossible): 14 windows — "ne" x5
(@170/@710/@810/@1076/@1737), "me la" (@126), feminine/mute-'e' x5
(@283/@450/@1212/@1779/@1177), "[89]-e" verb+ending x3 (@641/@872/@987).
14/38 = 36.8%. The 10% ceiling allows at most 3 windows. Even the "ne" x5 alone
(13.2%) exceeds it. Weak (admits via open values, stem impossible): 17 more.
Doubtful (no clean 'e' parse found, stem also impossible — possible orphans,
locus named): @377 ("[85] me pour"), @398 ("tout me e ent"), @928 ("par e me"),
@1398 ("[78]e e et"), @1525 ("la la e par"). These are fenced, not counted toward
either requirement: no stem parse exists at any of them, so they cannot make the
frame retire or hold.

## Per-clause pass/fail

1. RETIRE (zero windows require the stem): FAIL. @1229 and @1589 require the stem
   reading (ungrammatical under 48='e', grammatical under 48=verb-stem). 2 ≠ 0.
   The frame does not retire.
2. HOLD (>=1 requires stem AND letter-'e'-required < 10%): FAIL. First conjunct
   passes (2 windows); second conjunct fails — letter-'e'-required is 14/38 =
   36.8% on strong windows alone, against a <10% (≤3-window) ceiling. The frame
   does not hold.
3. Full sweep: PASS. All 38 windows classified with @-offsets; no invented data.

## Verdict: NULL

HEADLINE: the bar decides neither way. The verb-stem frame has exactly two
exclusive legs (@1229/@1589, "…[48]er ce" x2, byte-identical trigram) and cannot
retire — but letter-'e' is required at 14 of 38 windows (36.8%, floor), so the
frame cannot hold as a general claim about 48 either. This confirms and sharpens
the verb-48 battery's escalation (2026-10-08): the standing battery-promoted
48='e' and the red-team-granted A7-L2 verb-stem frame are in tension, and the
§7 sole-polyvalence rule (67 et/veut only) leaves no room for both without a
red-team scope ruling. The A7-L2 grant is NOT overwritten here; its live scope
is its two exclusive legs unless the red team narrows or retires it. Escalated
to the red team in this headline, per protocol §5.

## Follow-up targets (null regenerates work)

1. stem48-legs-rival — Rival letter-'e' parses of the 2 exclusive legs. Test @1229
   (82-48-29-47 as one orthographic word; 48 as stem-vowel of a longer word;
   29-47 word-internal "erce" with 48 as preceding word-final 'e') and @1589
   ("[65]e" + "er ce" segmentations) for any grammatical letter-'e' parse.
   Bar: the stem-requirement stands iff no grammatical letter-'e' parse is found
   at either window; a parse at either window re-opens this battery's Clause 1.
2. stem48-scope-fence — Fence the 5 doubtful windows (@377/@398/@928/@1398/@1525):
   each parses under 48='e' with stated cause, or is confirmed orphan with the
   orphan's locus named (48 vs neighbor value). Bar: all 5 resolved; the A7-L2
   frame's scope stays exactly @1229/@1589 iff none of the 5 admits a stem parse.
3. stem48-65-value — Name 65 at @1589: "[65] [STEM]er ce [08]" needs 65's class
   for the stem leg's syntax to close (noun taking infinitive? verb?). Bar: 65
   named with the infinitive complement parsing under standing values; input to
   the A7-L2 scope ruling.
