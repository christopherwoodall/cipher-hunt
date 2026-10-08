# Battery report — dire-33 (33="dire")

Worker: 4acdfc83-8f38-4093-960c-959e08fa82f2. Date: 2026-10-07.
Lock note (protocol §6): predecessor lock `locks/dire-33.lock`
(adbdb5bd-ca9d-42cd-ac85-804239f7ce2a, 2026-10-08T04:21:49Z) was fresh but its
worker died in the agent-daemon restart at ~2026-10-08 04:26 UTC with no
partial report on disk. Lock refreshed 2026-10-08T04:28:01Z; clean restart,
nothing inherited.

## Bar (verbatim, from battery-queue.json)

`promote iff 29-89-84/29-82-16 word-shapes resolve + 'dire' wins idiom battery vs croire/savoir + single-infinitive test passes`

Numbered clauses (pre-registered BEFORE testing, not modified after):

1. C1 — the word-shapes of `29-89-84` (@273) and `29-82-16` (@1477) resolve
   (segmentation determined; the 'erreur' blocker admitted or dissolved
   with stated cause).
2. C2 — `dire` WINS the idiom battery against `croire` and `savoir`
   (beats both rivals on discriminating frames).
3. C3 — the single-infinitive test passes: all 25 windows with 33 parse
   under the single value 33="dire" (whole infinitive or the noun "le dire").

## Method

Parsed per `code/side-keyhunt/repair_parse.py`: `repaired_offsets.json` +
`data/upstream-ct_R5005.txt` = 1,847 pairs. `canonical.py` not used. R5005
not touched. All counts below re-derived from the stream in this run.

33 occurs in 25 windows. Successor census: 29 x5, 21 x3, 46 x2, 16 x2,
79 x2, 42 x2, 00 x2, 55/01/73/96/66/98/94 x1. Predecessors: 00 x8
("pour 33"), 67 x6, 47 x2, 15 x2, 52/37/82/84/42/12/85 x1.
Key frames: `00-33` x8 (@186/@408/@467/@846/@936/@1088/@1245/@1630);
`33-29` x5 (@273/@626/@1232/@1424/@1477); `67-33-46` x2 (@1451/@1624);
`47-33` x2 (@24/@1232); `33-21` x3 (@936/@1421/@1630);
`67-33-29` x3 (@273/@1424/@1477); `33-29-87` x2 (@626/@1424);
byte-identical `00-33-21-64-37-01` x2 (@936/@1630).

Standing values used: 29="er", 82="m" (banked GT); 87="ce", 64="qui",
96="par", 46="que", 79="tout", 00="pour", 47="ce" (A4, allophone tier),
84="on" (A15, with conditions); 67 et/veut sole polyvalence with the
positional rule (67="veut" iff follower infinitive-shaped) — applied
explicitly below. A10 (33 que-valency grant; 33+29 stem/whole HOLD) and
the red-team note ("'dire' recorded as leading partial, unpromoted",
next-token-redteam.md:170) are consistent with this battery; nothing here
contradicts a standing red-team verdict.

## C1 — word-shapes of 29-89-84 / 29-82-16

Windows: @273 `47-11-06-67-33-29-89-84-91`; @1477
`53-60-06-67-33-29-82-16-98`. Global: `29-89` x5, `89-84` x2 (only after
29), `29-82` x3, `82-16` x11.

The 'erreur' hypothesis dies three independent ways:

1. `29-89-84` = "erreur" needs 84="ur". 84="on" is granted (A15); 67 is
   the SOLE true polyvalence (§7) — a second value for 84 is declarable
   only by the red team. Blocked.
2. `29-89` = "erreur" needs 89="reur". Then `77-89` x2 (@639/@871,
   byte-identical `77-89-48-20`) reads "le reur" — ungrammatical x2. Dead.
3. 89 = the whole word "erreur" needs `29-89` x5 to read "er erreur" —
   ungrammatical x5. Dead.
4. `29-82-16` = "erreur" needs 82="re"; 82="m" is banked GT. Dead
   outright.

Resolved segmentation: `29-89-84` = `[X]er [89] on` — stem+"er"
infinitive, then 89, then 84="on". @273: "veut [33]er [89], on [91]"
(67="veut" by the positional rule: follower 33 is infinitive-shaped).
The parallel @1376 `00-86-29-89-84-92` reads identically,
"pour [86]er [89], on [92]" — the same shape under 86's INF-class (A9),
which corroborates the segmentation. `29-82-16` = `[33]er m[16]`:
@1477 "veut [33]er m[16] [98]" (82="m" GT; 82-16 x11 m-cluster; 16's
value open — queued as frame-82-16).

C1: PASS. The 'erreur' blocker is dissolved as a misread (it would break
standing 84="on" and the `77-89` x2 windows). Note the honest cost, used
in C3: dissolving 'erreur' CONFIRMS the stem reading `[33]er` at these
windows.

## C2 — idiom battery: dire vs croire/savoir

- F1 `67-33-46` x2 (@1451 `36-67-33-46-92-62`, @1624 `66-67-33-46-56-69`):
  positional rule applied explicitly — 33 is infinitive-shaped under
  every candidate, so 67="veut" (the "et dire que" fork is closed by the
  rule). "veut dire que" ✓ idiomatic; "veut croire que" ✓ grammatical;
  "veut savoir que" ✗ (savoir does not take que-clauses under vouloir).
  → savoir eliminated; croire ties dire.
- F2 `47-33` x2 (@24, @1232): "se/ce [inf]" — "se dire"/"se croire"/
  "se savoir" all grammatical; "ce"-readings equally murky for all three.
  No discrimination.
- F3 `pour 33` x8: "pour dire"/"pour croire"/"pour savoir" all clean.
  No discrimination.
- F4 `33-21` x3: 21's value is open (noun? "venir" via 96-21="parvenir"?),
  so the "noun-shaped" leg cannot be verified here. Non-discriminating.
- Lead noted but NOT used: @1700 `85-33-94-30` could read "contre-dire"
  (dire-only), but 85's value is open under the A3 verb-stem frame grant —
  not battery-usable.

C2: FAIL. "dire" beats "savoir" (F1) but does NOT beat "croire": croire
ties dire on every verifiable frame (`veut [inf] que` x2, `pour [inf]`
x8, `se [inf]` x2). The bar demands a win vs croire AND savoir.

## C3 — single-infinitive test

Five of 25 windows force 33 to be a stem, not "dire":

- @273: "veut [33]er [89], on [91]" (C1 segmentation)
- @626: `37-33-29-87-78` = "[37] [33]er ce [78]" (87="ce")
- @1232: `47-33-29-85-56` = "ce/se [33]er [85] [56]"
- @1424: `67-33-29-87-63` = "veut [33]er ce [63]"
- @1477: "veut [33]er m[16] [98]" (C1 segmentation)

No re-segmentation escapes: 29="er" is banked GT; "29-89-84"="erreur"
and "29-82-16"="erreur" are blocked (C1). "dire"+"er" is not a French
word. Orphan rate under single-"dire" = 5/25 = 20%, over the lane's 10%
orphan tolerance (cf. stem-33-86 bar). Positive set evidence: the chain
@1421-24 `15-33-21-67-33-29-87-63` needs BOTH a whole-33 ("[15] dire
[21]") and a stem-33 ("veut [33]er ce") inside one window.

C3: FAIL.

## Adverses disposition

- BLOCKER ('33 29' x5 / 'erreur'): DISSOLVED as misread (C1) — with the
  noted cost that the surviving parse confirms the stem reading.
- Single-vs-set ('33 21 67 33' chains): ANSWERED in favor of SET — the
  @1421-24 chain requires two values of 33 in one window; the single-value
  claim is falsified, the 2-member set stays live.
- "'33 que' x2 kills 'faire'": intact, faire not revived.
- vouloir KILLED / penser weak: untouched (outside this bar's scope).

## Verdict: null

"dire" is strongly supported as A value of 33 — 20/25 windows parse
cleanly, including the flagship `pour dire` x8 and `veut dire que` x2 —
but the single-value claim fails (5 stem windows need a second, -er
infinitive value) and "croire" ties "dire" on every whole-frame, so this
is inconclusive for promotion, not a kill: no cleaner rival is
demonstrated for the whole-frames, and killing "dire" would contradict
20 clean windows. Consistent with A10 ("leading partial, unpromoted") —
no red-team contradiction, no escalation.

## Follow-ups (null regenerates work)

1. **dire-33-set** — claim: 33 = {dire, [X]er} 2-member set (whole
   infinitive "dire" + one -er stem). Bars: resolve iff (a) the 5 stem
   windows cohere as ONE -er infinitive X (identify via contact profile);
   (b) all 20 whole-windows parse as "dire"; (c) no window needs a third
   value (<=10% orphan). Evidence: `33-29-87` x2 / `67-33-29` x3
   byte-identical stem frames vs `00-33` x8 / `67-33-46` x2 whole frames;
   @1421-24 chain needs both members. Adverses: croire ties dire on
   whole-frames; X unidentified; 89/16 values open.
2. **croire-33-tiebreak** — claim: 33 = croire (rival to dire).
   Bars: promote-33="croire" iff a discriminating frame is found
   (parses under croire, fails under dire) or vice versa; else record
   the tie. Evidence: dire/croire tie on `veut [inf] que` x2,
   `pour [inf]` x8, `se [inf]` x2; savoir killed by F1; "le dire" exists
   as noun vs "le croire" does not (noun test needs 21's value).
   Adverses: 21's value open; stem windows kill both equally; @1700
   "contredire" lead untested (85's value open under A3).
3. **erstem-33-id** — claim: identify X, the -er stem in `33-29` x5.
   Bars: name X iff its contact profile (pre: 67="veut" x3, 37 x1,
   47 x1; frames `[X]er ce` x2 @626/@1424, `[X]er [89] on` @273,
   `[X]er m[16]` @1477) matches a real -er infinitive's valency; use
   `86-29` x3 ("pour [86]er") as control. Evidence: 5 stem windows;
   A10 HOLD; `33-29-87` x2 byte-identical. Adverses: 89's value open;
   16's value open (frame-82-16 queued); overlaps stem-33-86 — coordinate.
