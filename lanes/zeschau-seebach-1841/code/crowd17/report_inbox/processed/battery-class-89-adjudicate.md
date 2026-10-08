# Battery report — class-89-adjudicate (red-team adjudication package for 89's noun-vs-infinitive class conflict)

- Target id: `class-89-adjudicate`
- Claim: "red-team adjudication of 89's noun-vs-infinitive class conflict"
- Date: 2026-10-08
- Worker: battery worker (agent b76c0854-b7d9-4be8-ac5d-c9c03d8f0270). Lock
  `code/crowd17/next-token/locks/class-89-adjudicate.lock` created
  2026-10-08T17:54:33Z; no prior/stale lock existed (`locks/` was empty);
  deleted on completion after queue confirm.
- Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json`
  + `data/upstream-ct_R5005.txt`), parsed per `code/side-keyhunt/repair_parse.py`.
  1,847 pairs / 96 distinct groups re-derived. R5005 untouched. Never used
  `canonical.py`. No invented data.
- EVIDENCE-GATHERING ONLY: no class is named for 89, no polyvalence is declared.
  §7: 67 et/veut is the sole true polyvalence; the class conflict is handed to
  the red team raw.

Indexing convention: @-offsets are 0-indexed pair indices into the 1,847-pair
parse, citing the FIRST pair of the named frame (the pair two positions before
89 in the mirror windows). Each window also gives 89's own pair index. Row ids
are from the repaired parse.

## Bar (pre-registered verbatim, from battery-queue.json)

`package the re-derived window table (noun-clean 11/14 + infinitive-slot 3)
with @1375 kill-grade infinitive exclusion stated, for red-team adjudication;
no class named, no polyvalence declared`

Numbered clauses (pre-registered BEFORE testing, not modified after):

1. The re-derived window table shows noun-clean 11/14 + infinitive-slot 3
   (14 windows total, 89 n=14 on the repaired stream).
2. The @1375 kill-grade infinitive exclusion is stated.
3. The package is presented for red-team adjudication.
4. No class is named for 89; no polyvalence is declared.

## Method

Re-parsed the repaired stream from source (1,847 pairs confirmed). Re-derived
89's census independently: 89 n=14 at 0-indexed positions
[113, 222, 275, 285, 303, 640, 781, 871, 986, 1082, 1377, 1393, 1498, 1752].
Predecessor census: 29 x5, 24 x3, 52 x2, 77 x2, 18 x1, 28 x1 (14 = all).
Successor census: 48 x3, 84 x2, 68/61/28/88/11/24/16/41/26 x1 (14 = all).
The 29->89 x5 bigrams re-derived; 24->89 x3 re-derived; "89-84" x2 tail
(@275, @1377) re-derived.

Standing values used (none decided here): banked GT 11=la, 70=pre, 82=m,
34=i, 29=er, 40=e, 46=que; granted 87=ce, 64=qui, 96=par, 00=pour (A9),
84=on (A15), 47=ce; battery-promoted 24=modal (ne-24-profile), 06='ent',
48='e' (letter), 94='ne'; 86 INF-class (A9 grant: 00->86 x12, 86->29 x4,
re-derived); 67 et/veut positional rule (sole polyvalence). 16's class open
(frame-82-16 queued — coordinated, not re-run).

## Window table (re-derived)

### The three mirror windows

- @273 (89 at 275, row a2_03): wider `47 11 06 | 67 33 29 89 84 91 37 61`
  = "…[06] veut [33]-er [89], on [91]…". Governor 67="veut" by the positional
  rule (follower 33-29 is infinitive-shaped). Tail "89-84" with 84="on" reads
  as a clause boundary ("…, on …").
- @1375 (89 at 1377, row a7_06): `98 00 86 29 89 84 92 69`
  = "[98] pour [86]-er [89] on [92]…". Governor 00="pour" (A9 grant);
  86 is INF-class (A9). Tail "89-84" byte-identical to @273's.
- @1391 (89 at 1393, row a7_07): wider `52 82 16 06 29 | 67 86 29 89 16 76 47 78`
  = "…m[16], [06]-er?, veut [86]-er [89] [16] [76] ce [78]…". Governor
  67="veut" by the positional rule. Tail "89-16" — 16's class is OPEN, so
  @1391's tail is gated (frame-82-16 queued), not broken.

### @1375 kill-grade infinitive exclusion (stated)

After "pour [86]-er" (A9-granted infinitive), 89 cannot be a verb at @1375:
"[inf] [89-finite] on" is ungrammatical; "[inf] [89-infinitive] on" is
ungrammatical; "[89]-on" inversion cannot open a clause; "89-84" as one word
("89on") is still non-verb-89. Under the infinitive reading of 89, @1375 is a
KILL-grade window: the reading is forced false at the mirror. This finding is
restated, not decided upon — it is handed to red team with the package.

### Noun-clean 8 (remaining windows of the 11)

- @113 (89 at 113, a1_03): `21 67 93 29 89 68 21 67 14 21` — pre=29.
  "[93]-er [89]" post-infinitive complement slot, direct-object-shaped.
- @285 (89 at 285, a2_03): `61 42 48 52 89 28 00 97 09 64` — pre=52.
- @303 (89 at 303, a2_04): `97 86 91 18 89 88 02 88 20 17` — pre=18.
- @640 (89 at 640, a4_01): `46 60 67 77 89 48 20 24 87 61` — pre=77 ("ce [77] [89]").
- @781 (89 at 781, a5_04): `73 37 08 29 89 11 24 42 94 74` — pre=29.
  "[08]-er [89] la" direct-object slot.
- @871 (89 at 871, a5_07): `86 70 87 77 89 48 20 74 49 16` — pre=77 ("ce [77] [89]").
- @1082 (89 at 1082, a6_05): `78 64 06 52 89 24 02 55 81 00` — pre=52.
- @1752 (89 at 1752, a8_08): `65 34 07 28 89 26 24 85 58 17` — pre=28.

The pre=29 x5 (@113, @275, @781, @1377, @1393) are all post-infinitive
complement slots ("[X]er [89]"), re-derived.

### Infinitive-slot 3 (all pre=24; 77-independent)

- @221 (89 at 222, a2_01): `29 42 16 24 89 61 96 87 46` — "[24-modal] [89] [61]
  par ce que". The "[24-modal] ___" slot is verb-selecting (ne-24-profile,
  battery-grade; rests on 24->85 x5, independent of 89).
- @985 (89 at 986, a6_01): `78 45 01 24 89 48 01 76 49 24` — "[24-modal] [89]
  [48] [01]". 48-junction: 48='e' (letter battery) cannot attach left
  (would unmake the infinitive shape); attaches right ("e[01]").
- @1497 (89 at 1498, a7_11): `66 15 59 24 89 41 74 84 33 42` — "[24-modal]
  [89] [41]". Left junction "59 24" ("est [24]") is broken under provisional
  59='est' — fenced (59 provisional).

## Adverses disposition

- "@222/@986 infinitive-slot legs survive without 77='le' (frames-80-89-indep)":
  PRESERVED. Re-derivation confirms all three infinitive-slot legs have pre=24
  (24-modal), not 77 — they are 77-independent and survive. They are the 3 of
  the "infinitive-slot 3"; the bar's table partition is exactly this cut.
- "89's class conflict cannot be decided at battery level per §7 — battery
  gathers evidence for red-team adjudication only": HONORED. This package names
  no class for 89 and declares no polyvalence. The conflict presented:
  noun-clean 11/14 (incl. @1375 kill-grade infinitive exclusion) vs
  infinitive-slot 3 (@221/@985/@1497, all pre=24), implicating the §7
  67-sole-polyvalence law. Adjudication is the red team's act, not this
  battery's.

## Per-clause pass/fail

1. Window table re-derived (noun-clean 11/14 + infinitive-slot 3, 89 n=14):
   PASS — every count above re-derived from the repaired stream.
2. @1375 kill-grade infinitive exclusion stated: PASS (see §"@1375 kill-grade
   infinitive exclusion").
3. Package for red-team adjudication: PASS.
4. No class named, no polyvalence declared: PASS.

## Verdict: promote

This is a PACKAGING verdict, not a class promotion. The evidence package is
complete for red-team adjudication: the window table (noun-clean 11/14 +
infinitive-slot 3) re-derived on the repaired stream, @1375 kill-grade
infinitive exclusion stated, both queue adverses answered/fenced with stated
cause, no class named, no polyvalence declared per §7. The red team decides
89's class (noun vs infinitive, positional rule, or a second polyvalence —
their act alone).

Packaging notes for the red team's docket (not follow-up targets):
- @1391's "[89] [16]" tail is gated on 16's open class (frame-82-16 queued).
- @1497's left junction "59 24" is fenced on provisional 59='est'.
- @985's 48-junction resolves rightward ("e[01]") under 48='e' (letter battery).
