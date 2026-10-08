# Battery report: frame-62-94-79 ("62-94-79-14-60" frame)

Worker: 2a40ff29-b34b-42bf-89cd-d98e7d467019. Date: 2026-10-08.
Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json +
data/upstream-ct_R5005.txt). canonical.py never used. R5005 never touched.

Indexing: @i = 0-based index into the pair list.
Offset note: the queue evidence cites @1363/@1687 (pre-repair offsets).
Re-derived on the repaired stream: 62 sits at @1362 and @1686 (row a7_06,
row a8_05). All offsets below are repaired-stream.

## Bar (verbatim, pre-registered)

"resolve iff frame parses under standing values or with one stated new-value assumption"

Numbered clauses:

1. The frame "62-94-79-14-60" parses as grammatical French under standing
   values (62='il' battery-promoted, 94='ne' battery-promoted pending
   ratification, 79='tout' red-team granted A5), with [14][60] taking a
   reading consistent with their contact profiles — in BOTH instances.
2. If clause 1 fails, the frame parses with exactly ONE stated new-value
   assumption (14's or 60's class/value), applied identically in both
   instances.
3. No window forces the frame-type incoherent (kill-grade check).
4. A single parse covers both instances (promote-grade check).

## Method

Fresh parse per the protocol. No prior counts trusted. Re-derived: the
5-gram "62 94 79 14 60" is byte-identical x2 (@1362, @1686). "94 79"
("ne tout") occurs x2, both inside this frame, zero elsewhere. "14 60"
occurs x2, both inside this frame, zero elsewhere. n14=15, n60=18.
Full ±12-group windows pulled for both instances. All 15 windows of 14
and all 18 windows of 60 scanned for class evidence. Candidate parses of
[14][60] tested: 'me'+stem (14='me', 60=verb-stem), verb-stem shapes
(14=verb / 60=verb), one-word 14-60 unit (verb, noun, adverb, "a fait",
"meme", pronoun), 14=determiner + 60=noun, 60=noun + 03=verb,
clause-boundary segmentations, expletive-"ne" readings.

Standing values used. Banked: 11=la, 70=pre, 82=m, 34=i, 29=er, 40=e,
46=que. Granted: 87=ce, 64=qui, 96=par, 17=fois, 79=tout, 00=pour, 84=on,
47=ce. Provisional: 59=est, 77=le. Promoted: 94=ne, 48='e' (letter),
30=pas, 39=a, 62=il, 06=ent.

## Window-level evidence (@-offsets, repaired stream)

Instance A @1362 (a7_06):
@1350 48 @1351 77 @1352 78 @1353 94 @1354 82 @1355 06 @1356 52 @1357 37
@1358 64 @1359 35 @1360 13 @1361 92 | @1362 62 @1363 94 @1364 79 @1365 14
@1366 60 @1367 03 @1368 30 @1369 82 @1370 16 @1371 91 @1372 67 @1373 98
@1374 00
Reads: "e[48] le[77] [78] ne[94] m[82] ent[06] [52] [37] qui[64] [35] [13]
[92] il[62] ne[94] tout[79] [14] [60] [03] pas[30] m[82] [16] [91] et[67]
[98] pour[00]".
Key: "ne...pas" brackets "tout [14] [60] [03]" (94@1363 -> 30@1368; this
"ne...pas" leg was already used by the pas-30 battery).

Instance B @1686 (a8_05):
@1674 60 @1675 03 @1676 39 @1677 74 @1678 77 @1679 44 @1680 00 @1681 46
@1682 79 @1683 65 @1684 13 @1685 93 | @1686 62 @1687 94 @1688 79 @1689 14
@1690 60 @1691 27 @1692 46 @1693 24 @1694 85 @1695 58 @1696 15 @1697 23
@1698 91
Reads: "[60] [03] a[39] [74] le[77] [44] pour[00] que[46] tout[79] [65]
[13] [93] il[62] ne[94] tout[79] [14] [60] [27] que[46] [24] [85] [58]".
Key: "ne...que" ("only") brackets "tout [14] [60] [27]" (94@1687 ->
46@1692). 27 is a hapax (n=1, occurs only here, only before 46).

Shared left edge: both instances have "13 [92/93]" directly before 62
(@1360-1361 = "13 92"; @1684-1685 = "13 93").

14's contact profile (n=15): pre = 66 x2, 82 x2, 79 x2, 87, 16, 67, 69,
31, 47, 18, 06, 65. suc = 24 x2, 06 x2, 60 x2, 21, 74, 45, 62, 02, 29.
Note: "tout [14]" x2 mirrors "tout [82]" x2 (@396, @1227; 82='m',
the A7-L2 "tout me/m'+verb" frame). 14 sits in the same post-"tout" slot
as 82.

60's contact profile (n=18): pre = 21 x4, 92 x2, 14 x2, 06 x2, 77, 46,
29, 94. suc = 03 x4, 08 x2, 71 x2, 67 x2, 12 x2, 90, 09, 15.
Note: "le [60]" @454 (77='le' provisional) -> 60 is noun-shaped
(masculine). "60 03" x4: in 3 of 4 non-frame windows it is NP-shaped
(@1644 "[60] [03] qui[64]", @1675 "[60] [03] a[39] le[77]",
@691 "[60] [03] a[39] [74] que[46]").

03's profile (n=20): "le [03]" @722 and "ce [03]" @1014/@1790 (noun-shaped);
"[03]er" @1030/@1320/@1594 (verb-stem-shaped; cf. queued stem-03 target).

## Candidate parse tests

Under standing values the two instances read:
(A) "il ne tout [14] [60] [03] pas m[16]"
(B) "il ne tout [14] [60] [27] que [24] [85]"
"ne...pas" (A) and "ne...que" (B) both require the verb between "ne" and
the closer. The only material in that slot is "tout [14] [60] [03/27]".
79='tout' (red-team granted A5) is not a verb and cannot head the verb
phrase. "il ne tout [verb] pas/que" is ungrammatical in French: "tout"
must follow the verb ("il ne [verb] pas tout", "il ne [verb] que [X]"),
or be the subject ("tout [verb]" = "everything verbs", A7-L2) — but "il"
already occupies the subject slot. No clause boundary rescues it
("ne" cannot open a clause; "[03] pas m[16]" / "[27] que [24]" cannot
open one either).

Single-assumption candidates (one per test, applied to both instances):

(a) 14='me', 60=verb-stem: "il ne tout me [60] [03] pas". Fails twice:
"tout" is still misplaced before "me [verb]" ("il ne me [verb] pas
tout" is the grammatical order); and 14='me' breaks four independent
windows: @424 "ce[47] me il[62]" ("ce me il" ungrammatical), @623/@896
"m[82] me" ("m'me"), @1121 "ent[06] me ent[06]". 14 is not 'me'.
(b) 14=verb-class: "il ne tout [14-verb] [60]..." — "tout" before the
verb. Ungrammatical. Fails.
(c) 60=verb-class: contradicts "le [60]" @454 (nominal); "tout" still
misplaced. Fails.
(d) 14=determiner/adjective, 60=noun ("le [60]"): "il ne tout [14] [60]
[03-verb] pas" puts the object "tout [14] [60]" before the verb,
violating SVO order ("il ne [03] pas tout [14] [60]" would be the
order). Fails.
(e) 14-60 = one lexical unit, as verb: "il ne tout [verb] [03] pas" —
"tout" before verb. Fails. As adverb ("a fait"-shaped): "il ne tout a
fait [03] pas" — "tout a fait" must follow the verb ("il ne [03] pas
tout a fait"). Fails. As pronoun ("nous"/"vous"/"les"-shaped): "il ne
tout [pronoun] [03] pas" — "tout" cannot sit between "ne" and the
object pronoun. Fails. As "meme": "il ne tout meme [03] pas" — no verb,
no sense. Fails.
(f) 14='est' (to license "il ne tout [14-60] [03] pas" as "il n'est pas
tout..."): killed distributionally — 14 shows zero of 59's predicative
concentration (14->{37,32,35} = 0/15 vs 59->{37,32,35} = 12/27; same
A7-L1 standard that killed 48='est'). Fails.
(g) Expletive-"ne" readings (subordinate clause, no "pas"/"que"
negation): both instances have real closers ("pas" @1368 promoted;
"que" @1692 granted), so expletive "ne" is excluded. Fails.
(h) 62 word-internal (cf. il-62 battery @46/@1482): "[92-62] ne tout..."
— "ne" still cannot open the clause. Fails.

No single new-value assumption for 14 or 60 produces a grammatical parse
in both instances. The blocker is structural, not lexical: "tout" (79,
red-team granted) sits between "ne" and the verb/object, and no
one-assumption re-valuing of 14 or 60 moves it or supplies a verb
before it.

## Per-clause pass/fail

1. Parses under standing values in both instances — FAIL. "il ne tout
   [14] [60] [03] pas" (A) / "il ne tout [14] [60] [27] que" (B) leave
   "tout" between "ne" and the verb slot in both "ne...pas" and
   "ne...que" frames; ungrammatical.
2. Parses with one stated new-value assumption — FAIL. Eight candidate
   families tested (a)-(h); all fail, most on the "tout"-placement wall,
   (a) and (f) additionally on independent distributional kills.
3. No window forces the frame-type incoherent — PASS (no kill). The
   5-gram is byte-identical x2; "94 79" and "14 60" are both
   frame-exclusive bigrams (x2 each, zero elsewhere); both instances
   carry genuine "ne"-closers. The frame-type is real; only its French
   is unresolved.
4. Single parse covers both instances — FAIL (no parse found).

## Verdict

NULL. The frame-type "62-94-79-14-60" is real (byte-identical x2, two
frame-exclusive bigrams, parallel "13 [92/93]" left edges, genuine
"ne...pas"/"ne...que" closers), but it does not parse under standing
values or with one stated new-value assumption for 14/60. The blocker
is the position of "tout" (79, red-team granted A5) between "ne" and
the verb slot. No red-team verdict is contradicted: A5 (79='tout'),
the il-62 promotion (which read these windows as "il ne tout" only for
62's subject slot), and the pas-30 promotion (which used "94->30" only
as a "ne...pas" leg) all stand untouched.

Corroboration: the crowd15 tout-battery (code/crowd15/report_inbox/
next-token-79-tout.md:63) independently fenced this same frame for
word-order failure ("on ne tout [14]" — 94's value disputed there).
That fence predates the 94='ne' battery promotion; this battery
re-tested under 94='ne' (now promoted, pending ratification) and the
word-order failure persists, so the fence is superseded by this null
rather than contradicted.

## Follow-ups (null regenerates work)

1. **tout-slot-14** (priority 2): 14 mirrors 82='m' in the post-"tout"
   slot ("tout [14]" x2 @1365/@1689 vs "tout [82]" x2 @396/@1227,
   A7-L2). Determine 14's class from its 15-window contact profile,
   testing clitic/determiner hypotheses against the breakers (@424
   "47 14 62", @623/@896 "82 14", @1121 "06 14 06"). Bar: name 14's
   class iff "tout [14]" parallels "tout [82]" under one stated value
   AND the four breaker windows resolve or fence with stated cause.
2. **noun-60** (priority 2): 60 is noun-shaped ("le [60]" @454; "60 03"
   NP-shaped @1644/@1675/@691 with "qui"/"a"; pre60 includes 77/46/29).
   Name 60's masculine-noun value. Bar: promote iff "le [60]" plus >=2
   "60 03" NP-frames cohere under one nominal value.
3. **frame-62-94-79-reparse** (priority 3): re-test this frame once 14
   and/or 60 are named (inputs: tout-slot-14, noun-60). If it still does
   not parse, fence "94 79" ("ne tout", 2-window exclusive bigram) as a
   genuine anomaly with stated cause — either non-standard "tout"
   placement (2-window idiolect/scribal artifact) or a mis-segmentation
   with a word boundary inside 79-14-60. Bar: resolve iff the frame
   parses under the newly named values; else fence with stated cause.
