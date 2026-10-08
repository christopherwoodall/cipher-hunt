# Battery report — frame-74-45-93

Target: `frame-74-45-93`. Claim: "45->93 x3 cluster resolves under one parse".
Worker: b6b74371-d8ca-4fbf-ab14-119b69bf1816. Date: 2026-10-08.
No pre-existing lockfile found. Lock created at start, deleted at end.

## Bar (verbatim from battery-queue.json)

"(a) all three windows parse with 93's class stated; (b) joint with verb-93: if 93 is verb-shaped, record 45!='ce' at these windows as a kill-grade adverse for A11 (do not promote around it)"

## Bar restated as numbered pass/fail clauses

1. Clause (a): each of the three 45->93 windows parses with 93's class stated.
2. Clause (b): conditional — IF 93 is verb-shaped, THEN record 45!="ce" at these windows as a kill-grade adverse for A11, and do not promote around it.

The bar was copied before testing and not changed after seeing data.

## Method

Tested only against the repaired 1,847-pair stream: `data/upstream-ct_R5005.txt`
parsed with `code/side-keyhunt/repaired_offsets.json` using the byte-exact
tokenization from `code/side-keyhunt/repair_parse.py`. `canonical.py` was not
used. R5005 was not touched. Offsets below are 0-based pair indices
(the queue's @262/@478/@603 are the same windows, 1-based).

Verified counts: 45->93 occurs exactly 3x in the stream (the three windows
below). 87->93 occurs 0x, as the queue states. 93 occurs 14x total.

## Window-level evidence

Standing values used: 45="ce" (A11 hold), 96="par" (granted), 64="qui"
(granted), 00="pour" (granted), 84="on" (granted), 59="est" (provisional),
77="le" (provisional).

W1 — index 261, row a2_02 (raw pair offset 34):
`43 77 84 [74 45 93] 52 33 42 06`
Parse: `84`="on" `74`[governor] `45`="ce" `93`[noun] `52` — "on [V/gov] ce [N] 52".
93 is determiner-governed ("ce" + nominal). Parses with 93 as noun.

W2 — index 477, row a2_11 (raw pair offset 0):
`24 37 78 [74 45 93] 00 13 52 30`
Parse: `37`[predicative frame, A1] `78` `74`[governor] `45`="ce" `93`[noun]
`00`="pour" `13` — "74 ce [N] pour 13". Parses with 93 as noun.

W3 — index 602, row a4_00 (raw pair offset 24):
`03 39 26 [96 45 93] 54 64 39 64`
Parse: `96`="par" `45`="ce" `93`[noun] `54` `64`="qui" — "par ce [N] 54 qui ...".
A prepositional phrase "par ce N" followed by a relative clause. Parses
cleanly with 93 as noun.

## Distributional support for 93 = noun (class stated)

- 45="ce" governs 93 x3 (these windows). "ce" governs nominals only.
- W3 left context is `96`="par" (granted): "par ce [N]" is canonical.
- Index 9 (row a1_00): `06 77 78 18 [93] 62` — 93 sits after `77`="le"
  (provisional article): article-governed slot, noun-shaped.
- Index 101 (row a1_03): `08 21 62 94 [93] 59 45` — 93 directly precedes
  `59`="est" (provisional): "93 est" puts a nominal, not a verb, before "est".
- 74's profile (n=34): precedes `46`="que" x3, `45`="ce" x3, `77`="le" x2,
  `47`="ce". 74 is a governor (verb- or preposition-shaped), so both W1/W2
  ("74 ce N") and W3 ("par ce N") share one structure: GOVERNOR + ce + NOUN.
  The left-context difference (adverse 2) is lexical, not structural.

## Per-clause results

1. Clause (a) — PASS. All three windows parse with 93's class stated as noun:
   W1 "on [gov] ce [N93] 52", W2 "[pred] 74 ce [N93] pour 13",
   W3 "par ce [N93] 54 qui ...". One parse: governor + "ce" + nominal head.
2. Clause (b) — PASS (conditional does not fire). At these windows 93 is
   determiner-governed ("ce", "par ce"), which excludes a verb reading of 93
   here. No kill-grade adverse for A11 is recorded. Nothing is promoted around:
   the A11 hold (45="ce") stands untouched, and the global verb-shaped question
   stays with the dedicated `verb-93` discriminator battery (priority 3, still
   queued). If `verb-93` later finds 93 verb-shaped elsewhere, bar (b)'s
   tripwire converts to a kill-grade adverse for A11 at that time.

## Adverses answered

- "93's class open" — ANSWERED. Class stated: noun (nominal head), supported by
  determiner government (ce x3, par-ce, le-slot at index 9) and "93 est" at
  index 101. Fenced with stated cause: verb-slot hints at other windows
  (index 733 "85[verb-stem] 93", index 1684 "46=que 79=tout 65 13 93",
  index 1811 "80[verb-frame] 04 61 15 93") are left open and assigned to the
  `verb-93` battery, which owns the global discriminator.
- "74 vs 96 left contexts differ" — ANSWERED. `96`="par" is granted, giving W3
  "par ce N". 74's governor profile (governs que/ce/le) shows W1/W2 have the
  same governor + "ce N" structure. The difference does not break the parse.

## Verdict: promote

All bar clauses pass and both listed adverses are answered. The claim holds:
the 45->93 x3 cluster resolves under one parse — 45="ce" (A11) + 93 as nominal
head — at indices 261, 477, and 602. Scope note: this promote covers the three
windows only; 93's global class remains fenced to the `verb-93` battery.
No red-team verdict is contradicted; R5005, sealed gates, and the adjudication
queue were not touched.
