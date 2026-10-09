# Battery report — formula-94-07-06-94

Worker: 4c18e0d3-3a6d-4d8b-85e7-e26d7c241816. Date: 2026-10-09.
Lock: `code/crowd17/next-token/locks/formula-94-07-06-94.lock` (fresh, this worker).

## Bar (verbatim, from battery-queue.json)

`resolve iff mirror frame parses under standing values or confirms anomaly with stated cause`

Numbered clauses (pre-registered BEFORE testing):

1. C1 — the mirror frame `94-07-06-94` (@771..@774) parses as ONE frame under standing values.
2. C2 — else, the window is confirmed as a genuine anomaly with a stated cause.

## Method

Parsed only the repaired 1,847-pair stream: `code/side-keyhunt/repaired_offsets.json` +
`data/upstream-ct_R5005.txt`, tokenized like `code/side-keyhunt/repair_parse.py`
(`[s[i:i+2] for i in range(o, len(s)-1, 2)]` per row offset). 1,847 pairs, 96 cells.
All @-offsets are 0-based indices into that stream. `code/side-keyhunt/canonical.py`
never used. R5005 never touched. Standing values per BATTERY-PROTOCOL.md §7:
GT 11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que; granted 87=ce, 64=qui,
96=par, 17=fois, 79=tout (A5), 00=pour (A9), 84=on (A15), 47=ce (A4);
provisional 59=est, 77=le; 80/89 verb-frames (A8, values open);
37/32/42 predicative (A1); battery-promoted 94="ne" (2026-10-07), 06="ent/ment"
(2026-10-08). Kills hold: {48,94} homophone-set, 48="est"/"ne"/"de".

## Window-level evidence

0-based stream at the claim site (row ids shown):

```
760:20 761:62 762:94 763:59 764:39 765:88 766:66 767:98
768:80 769:10 770:22 | 771:94 772:07 773:06 | 774:94 775:15 776:33 777:73 778:37 779:08 780:29 781:89 ...
row a5_03: pairs 748..773        row a5_04: pairs 774..799
```

F1 — the claim span `94 07 06 94` sits at pairs 771–774 and is a HAPAX 4-gram
(sole occurrence in 1,847 pairs). Its sub-bigrams `94 07`, `07 06`, `06 94` are
each hapax too. No frame family exists to support a frame-type reading.

F2 — FINDER MISLABEL (corrected): the queue's evidence context quotes
`@774 '94 07 06 94 15 33 73'`. The actual @774-anchored window in the repaired
stream is `94 15 33 73 37 08 29` (pairs 774–780). The quoted 7-gram
`94 07 06 94 15 33 73` is pairs 771–777 — the same @771-centered span. The two
@-labels mark the two 94s (@771 left, @774 right), not two overlapping windows.

F3 — ROW BOUNDARY between the two 94s: pair 773 is the LAST pair of manuscript
row a5_03; pair 774 is the FIRST pair of row a5_04. Exactly one row boundary
falls inside the 771–774 span, and it falls between the two 94s. Every granted
multi-pair frame checked (`94-59` @762–763, `94-82-06-06` @578–581,
`70-12-94` @347–349, `35-94-52-80-04` @1292–1296) sits inside a single row;
none spans a row boundary. Only 5 of 37 94s in the stream are adjacent to a
row boundary at all.

F4 — LEFT HALF parses independently (pairs 768–773, all row a5_03):
`80 10 22 94 07 06` = "…[80-verb, A8] [10] [22] ne [07]ent" — 94="ne"
(battery-promoted), 06="ent" (battery-promoted), 07 an open stem. A standard
negated verb with an unnamed stem. Left context confirms the neighbourhood is
ne-active: `62 94 59 39` @761–764 = "[62] n'est à" (the ne-94 battery's F-A
frame, with 39="a/à" promoted).

F5 — RIGHT HALF parses independently (pairs 774–780, all row a5_04):
`94 15 33 73 37 08 29` = "ne [15] [33] [73] [37-predicative, A1] [08] [29=er]" —
94="ne" heads a fresh clause at the row start; 29="er" GT and the 33+29 (A10)
hold frame the right edge.

F6 — 94="ne" usage here is consistent with the standing promotion and does not
touch the queued red-team split question (`redteam-94-functional-split`):
both 94s are preverbal negators, not word-final syllables.

## Per-clause pass/fail

- C1 — FAIL (kill grade): `ne [07]ent ne` cannot parse as ONE frame-type in
  French, and the span is cut by the a5_03/a5_04 row boundary between the two
  94s — each half lives in its own manuscript row and parses independently
  (F4, F5). The claim's "one frame-type" assertion is forced false by the
  window. The 4-gram is a hapax with hapax sub-bigrams (F1): no distributional
  support for a mirror formula.
- C2 — FAIL: there is no anomaly. Both halves are ordinary ne-frames under
  standing values; nothing anomalous remains to confirm with a stated cause.

Adverse "unparsed" — ANSWERED: both halves now parse (F4, F5). The mislabeled
@774 window (F2) is corrected on the record.

## Verdict

**KILL.** The "A3 mirror" is two adjacent, independent negated clauses abutting
across a manuscript row break — `…ne [07]ent | ne [15]…` — not one mirror
frame. The single-frame claim is forced false at kill grade (C1). This verdict
contradicts no standing verdict: ne-94 and ent-06 promotions are reinforced
(two more clean ne-frames, one more -ent verb); the red-team 94-split question
is untouched (both 94s preverbal).

## Optional follow-up (not mandated — kill verdict)

- `x-07-verb-stem` (priority 3): name 07 via the F4 leg — `94 07 06` =
  "ne [07]ent" makes 07 a verb-stem candidate. Bar: census all 07 windows;
  promote a stem value iff >=2 independent `[07]-ent` / `[07]-verb` frames
  parse with 07's follower profile verb-consistent; else fence 07 as open.
