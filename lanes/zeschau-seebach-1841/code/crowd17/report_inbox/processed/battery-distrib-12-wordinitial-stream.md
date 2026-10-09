# Battery report: distrib-12-wordinitial-stream

- Target id: `distrib-12-wordinitial-stream`
- Claim: "Word-initial-12 is attested at 2/2 decided '12 16' windows; census all 23 of 12's windows for leftward composition to decide whether word-initial is the norm or the exception stream-wide"
- Date: 2026-10-09
- Worker: battery worker (subagent 23abe201-caa0-4a8b-bc27-a944e9700de5)
- Stream: repaired 1,847-pair parse (`data/upstream-ct_R5005.txt` +
  `code/side-keyhunt/repaired_offsets.json`, parsed like
  `code/side-keyhunt/repair_parse.py`). All @-offsets 0-based.
  n(12) = 23 (re-derived, asserted).
- Lock: `code/crowd17/next-token/locks/distrib-12-wordinitial-stream.lock`
  (created at start, deleted at end).

## Bar (verbatim, pre-registered before testing)

"Census all 23 of 12's windows for leftward composition ('70 12' prenne-family x3, '53 12' x4, '26 12' x4, etc.): is word-initial-12 the norm or the exception stream-wide? Gives this target's uniformity claim's distributional prior"

Numbered pass/fail clauses (restated before testing, not modified after):

1. (C1) Census all 23 windows of 12 for leftward composition, grouped
   by left-neighbor contact ('70 12' x3, '53 12' x4, '26 12' x4, and all
   remaining left neighbors), classifying each as decided-leftward,
   decided word-initial, or undecidable at battery grade.
2. (C2) Answer the norm-vs-exception question on the census: state the
   distributional prior for word-initial-12 stream-wide.

## Method

1. Re-derived the repaired parse in-session (1,847 pairs, 96 types).
   Never used `canonical.py`. R5005 untouched.
2. Enumerated all 23 windows of 12 with +-3 context.
3. Classified each window's 12 as:
   - **decided leftward**: left neighbor is a stem/fragment/letter whose
     word completes through 12 (the [stem]+n+[e/ne/ent] doubling family:
     70='pre' + 12 + 94='ne' = "prenne"; 53='don' + 12 + 48='e' = "donne";
     70 + 12 + 06='ent' = "prennent"; 40='e' + 12 + 94 = "enne").
   - **decided word-initial**: left neighbor is a complete word that
     cannot host a following 'n' (56 whole-word, battery-promote; 86 INF
     class; 98 finite-verb class), so 12 must open a new word.
   - **undecidable**: left neighbor's class is open at battery grade.
4. Verified the brief's contact counts byte-exactly before classifying.

## Census (all 23 windows, 0-based @-offsets)

### Group 1: '70 12' x3 — all decided leftward (prenne family)
- @348 (a2_05): `01 06 70 12 94 74 67` — pre+n+ne = "prenne". Leftward.
- @1119 (a6_07): `11 88 70 12 06 14 06` — pre+n+ent = "prennent". Leftward.
- @1548 (a8_00): `00 46 70 12 94 92 45` — pre+n+ne = "prenne". Leftward.

### Group 2: '53 12' x4 — all decided leftward (donne family)
- @58 (a1_01): `58 35 53 12 41 08 34` — don+n+e = "donne". Leftward.
- @169 (a1_05): `82 84 53 12 48 21 60` — don+n+e = "donne". Leftward.
- @709 (a5_01): `21 35 53 12 48 71 12` — don+n+e = "donne". Leftward.
- @1582 (a8_02): `98 24 53 12 44 00 36` — donn- stem continuation. Leftward.

### Group 3: '26 12' x4 — decided word-initial x1, undecidable x3
- @843 (a5_06): `62 94 26 12 16 00 33` — one of the two decided '12 16'
  word-initial windows. Word-initial.
- @241 (a2_01): `17 11 26 12 16 56 43` — the FENCED '12 16' window (W2).
  Undecidable (uniformity not established here; not counted either way).
- @1471 (a7_10): `62 38 26 12 41 53 60` — 26's class open. Undecidable.
- @1708 (a8_06): `94 88 26 12 06 29 40` — 26's class open (26n fence).
  Undecidable.

### Group 4: remaining left neighbors (12 windows)
- @64 (a1_01): `34 29 40 12 94 92 69` — e+n+ne = "enne" (40='e' banked,
  94='ne' lead). Leftward.
- @1430 (a7_08): `63 91 61 12 16 76 49` — second decided '12 16'
  word-initial window. Word-initial.
- @539 (a3_01): `82 16 91 12 44 29 48` — 91's class open (adjective /
  past-participle duality). Undecidable.
- @701 (a5_01): `28 94 60 12 98 20 12` — 60 is verb class (split-60-verbs
  promote); a verb word cannot host a following 'n'. Word-initial (lean:
  60's sub-lexical sharing is the caveat).
- @704 (a5_01): `12 98 20 12 66 21 35` — 20's class open (20~17 split).
  Undecidable.
- @712 (a5_01): `12 48 71 12 63 00 66` — 71's class open (§7 split
  candidate). Undecidable.
- @809 (a5_05): `24 24 41 12 48 24 65` — 41's class open (three-way split;
  letter arm does not cover this locus). Undecidable.
- @1075 (a6_05): `42 98 98 12 48 77 78` — 98 is finite-verb class
  (vient-98-name promote); "vientn" is not French. Word-initial.
- @1509 (a7_11): `86 56 41 12 61 59 39` — 41's class open. Undecidable.
- @1641 (a8_04): `74 35 56 12 33 98 60` — 56 is whole-word (battery
  promote); 12 must open a new word. Word-initial.
- @1736 (a8_07): `30 06 60 12 48 52 86` — 60 verb class; same reasoning
  as @701. Word-initial (lean).
- @1740 (a8_07): `48 52 86 12 34 94 82` — 86 INF class; an infinitive
  cannot host a following 'n'. Word-initial.

## Tally

- Decided leftward: 8 (@58, @64, @169, @348, @709, @1119, @1548, @1582)
- Decided word-initial (strong): 5 (@843, @1075, @1430, @1641, @1740)
- Decided word-initial (lean, verb-60 loci): 2 (@701, @1736)
- Undecidable at battery grade: 8 (@241 fenced, @539, @704, @712, @809,
  @1471, @1509, @1708)

Word-initial share: 5/13 = 0.38 (strong-decided only); 7/15 = 0.47
(with the two verb-60 leans). Undecided: 8/23.

## Per-clause pass/fail

1. C1 PASS — all 23 windows classified; contact counts verified
   byte-exact ('70 12' x3, '53 12' x4, '26 12' x4 match the brief).
2. C2 PASS — the distributional prior: word-initial-12 is a substantial
   minority, approximately 0.38–0.47 of decidable windows. It is NEITHER
   the norm (majority) NOR a rare exception. The decided '12 16' windows
   sit inside the word-initial minority; the fenced @241 does not move
   the share (it is undecidable, not a counter-leg).

## Adverses answered

(a) "@241 (W2) is the fenced window itself — uniformity is not
established there": treated as undecidable throughout; it contributes
to neither numerator. (b) "'70 12' x3 prenne-family shows 12 can compose
leftward": confirmed — all three verified as leftward (prenne x2,
prennent x1).

## Verdict: PROMOTE (census deliverable, battery grade)

The census is complete and the distributional prior is delivered:
word-initial-12 is a substantial minority stream-wide (0.38–0.47 of
decidable windows), neither norm nor rare exception. No standing
red-team verdict contradicted or downgraded; §7 intact.

Canonicality caveat stands: windows on a1_01 (@58, @64) sit on
phase-uncertain soil (offset-1 rival); all verdicts hold on the
canonical stream per protocol. No follow-ups required — the eight
undecided windows are owned by open class questions (26, 91, 20, 71,
41), not by this census.

## Bookkeeping

- Queue: `battery-queue.json` `distrib-12-wordinitial-stream` →
  status `verdict`, result `promote`, date 2026-10-09 (temp-file +
  rename; pre-write assert passed — was `queued`/verdictless; JSON
  re-validated; own entry only; no downgrade).
- Lock created at start, deleted on completion.
