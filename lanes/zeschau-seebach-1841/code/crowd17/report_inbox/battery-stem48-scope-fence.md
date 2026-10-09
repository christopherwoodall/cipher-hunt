# Battery report: stem48-scope-fence — 2026-10-09

Worker: a55c1bca-716e-4852-a081-e69f65ccf036. Stream: repaired 1,847-pair parse
(`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`,
parsed per `code/side-keyhunt/repair_parse.py`; re-derived in-session:
1,847 pairs, 96 types, n(48)=38 — matches). `canonical.py` never touched.
R5005, sealed gates, red-team queue untouched. Lock
`locks/stem48-scope-fence.lock` created on start (no pre-existing lock);
deleted on completion.

## Bar (verbatim from queue, pre-registered BEFORE testing)

"All 5 resolved; the A7-L2 frame's scope stays exactly @1229/@1589 iff none
of the 5 admits a stem parse."

Numbered clauses (frozen before adjudication):

- C1: All 5 doubtful windows (@377/@398/@928/@1398/@1525) are resolved. A
  window is resolved iff it parses under standing 48='e' with stated cause,
  or is confirmed orphan with the orphan's locus named (48 vs neighbor value).
- C2: The A7-L2 frame's scope stays exactly @1229/@1589 iff none of the 5
  admits a stem parse. "Admits a stem parse" = a complete grammatical French
  parse of the window exists under standing values with 48 as verb-stem
  (48's stem value open; licensed shapes: the A7-L2 "tout me [48-verb]"
  family; grammaticality judged under 1841 diplomatic French using only
  banked/granted/promoted values).

Standing values used: 11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que (GT
pencil); 87=ce, 64=qui, 96=par, 17=fois, 79=tout, 00=pour, 84=on, 47=ce
(allophone tier); 59=est, 77=le (provisional); 48='e' (R17-003 letter tier,
battery-promoted); 06='ent' (ent-06 promoted); A7-L2 "tout me [48-verb]"
(grant); A3 85 verb-stem (frame granted, value open). Coordination: fem-e-48
(PROMOTE 2026-10-09) cited, not duplicated; w48-boundary-census (PROMOTE
2026-10-09) window classifications cited where they touch the same windows
and independently byte-verified here; elision82-48-x1 (PROMOTE 2026-10-09)
fenced @398's "m'[48]ent" residual to this battery — decided here, §E2.

## Method

Re-derived the repaired stream byte-exactly per `repair_parse.py`. Dumped
each doubtful window with 5-pair context on each side. Tested each window
under (E) standing 48='e' and (S) 48 as verb-stem. @-offsets below are the
pair index of 48 itself.

## Evidence — the 5 windows (byte-verified)

### @377 (a2_07): `65 63 29 85 82 48 00 11 50 82 16`

Window: "…[65] [63] er [85] me pour la [50] m [16]" (29='er' banked,
00='pour' A9, 11='la' banked).

- (E): 82-48 = "me" parses cleanly (closed clitic; successor 00='pour' is
  consonant-initial, so no elision — elision82-48-x1). The window as a whole
  does not close: "[85] me pour" — the clitic "me" dangles between 85 and
  "pour", and 85's value is open (A3 verb-stem frame granted, value open),
  so 85's attachment cannot be adjudicated. The failure turns on 85, not 48.
- (S): no stem parse. The A7-L2 shape "me [48-verb]" is present (82-48) but
  48 would be a bare single-cell verb followed by granted "pour" — a bare
  stem is ungrammatical (stem48-exclusive-legs), and no infinitive leg
  follows (successor is 00, not 29).
- RESOLVED: 48='e' parses ("me"); confirmed orphan, locus = neighbor 85's
  value (open). 48 is not the problem.

### @398 (a2_07→a2_08): `34 67 64 79 82 48 06 11 45 88 53`

Window: "…[67] qui tout me ent | la [45] [88] [53]" (64='qui', 79='tout' A5,
06='ent' promoted, 11='la' banked; 06 ends row a2_07, 11 opens a2_08).

- (E): 82-48 = "me" parses cleanly as a word. The window does not close:
  06='ent' is a verb ending, not a word, and "eent" is not French (ent-06
  fenced @398-400 "eent la" as no parse). No other boundary works.
- (S): the "m'[48]ent" residual (elision82-48-x1: "live ambiguity… NOT
  decided here") is DECIDED here: it admits no grammatical parse.
  (i) "tout" as subject takes 3rd-singular agreement ("tout me plaît"-shaped),
  but "-ent" is 3rd-plural — agreement fails. (ii) "tout" as pre-verbal
  object pronoun needs an infinitive ("tout me dire"-shaped, which is what
  licenses the A7-L2 legs); "-ent" is finite — placement fails. (iii) "qui"
  with a plural antecedent could license 3pl, but "tout" still cannot sit
  pre-verbally before a finite verb. Morphological shape is live; syntax
  bars it under every standing-value assignment.
- RESOLVED: 48='e' parses ("me"); confirmed orphan, locus = 48's junction
  (neighbors 79/06/11 are all standing-clean; neither 48's letter reading
  nor its stem reading closes the window).

### @928 (a5_10): `65 71 17 61 96 48 82 98 83 56 69`

Window: "…[71] fois [61] par e m [98] [83] [56] [69]" (17='fois', 96='par'
granted).

- (E): parses. Compositional 96-48 = "pare" (3sg of "parer"-shaped verb;
  noted as composition, not a value claim — w48-boundary-census). The
  two-word alternative "par"+"e"+"m" is ungrammatical: lone "e" is not a
  French word and 82='m' is a banked cell. Remainder: "fois [61] pare
  m'[98]…" — finite "pare" with open subject [61], elided "m'" before
  open 98 (vowel-initial admissible) — grammatical shape exists. 48='e'
  is the word-final -e of "pare".
- (S): no stem parse. 96="par" is granted, so 48 cannot re-read it; 48 as
  stem head ("e m…") is a bare stem — ungrammatical.
- RESOLVED: parses under 48='e' with stated cause. (Coordination: this is
  a window-level parse, not a re-run of fem-e-48's 40-vs-48 distribution;
  fem-e-48's PROMOTE stands untouched.)

### @1398 (a7_07): `89 16 76 47 78 48 40 67 77 81 87`

Window: "…[76] ce [78] e e [67] le [81] [87]" (47='ce' allophone tier,
40='e', 77='le' provisional).

- (E): no clean parse adjudicable under standing values. 78's value is
  open ("ver" is R16-005 LEAD only, ungranted); the "veree" strain depends
  entirely on that ungranted value (fenced per fem-e-48). With 78 open,
  "ce [78] e e [67] le" cannot be closed — but 48's 'e' is unobjectionable
  as a letter; the window turns on 78.
- (S): no stem parse. No frame shape (predecessor 78 open, successor 40);
  bare stem ungrammatical.
- RESOLVED: confirmed orphan, locus = neighbor 78's value (open), not 48.

### @1525 (a8_00): `08 31 24 11 11 48 96 87 46 21 65`

Window: "…[24] la la e par ce que [21] [65]" (11='la' banked, 96='par'
granted, 87='ce', 46='que' — "par ce que" is grammatical).

- (E): no parse. 48 is stranded between closed "la" and closed "par":
  "lae" is not a word, "epar" is not a word, lone "e" is not a word.
- (S): bare stem — ungrammatical. No stem parse admitted.
- RESOLVED: confirmed orphan, locus = 48 itself (stranded word-initial 'e';
  neighbors 11/96 granted-clean). Fenced, not litigated: the "la la"
  doubling and the a8_00 row boundary are a possible re-segmentation venue
  (cf. w48-boundary-census caveat 1).

## Per-clause pass/fail

- C1: PASS. All 5 resolved. @928 parses under 48='e' ("pare",
  compositional 96-48). @377: orphan, locus = neighbor 85's value (open).
  @398: orphan, locus = 48's junction ("m'[48]ent" syntactically barred:
  "tout"-subject needs 3sg vs "-ent" 3pl; "tout"-object needs infinitive
  vs "-ent" finite). @1398: orphan, locus = neighbor 78's value (open).
  @1525: orphan, locus = 48 (stranded 'e').
- C2: PASS. None of the 5 admits a stem parse (@377: bare stem + granted
  "pour"; @398: barred per §E2; @928: 96="par" granted, bare stem;
  @1398/@1525: no frame shape, bare stem). The A7-L2 frame's scope stays
  exactly @1229/@1589 — byte-verified legs: @1229 "64 79 82 48 29 47 33"
  (a7_01), @1589 "70 64 65 48 29 47 08" (a8_02).

Adverses: none listed. No standing verdict contradicted or downgraded:
consistent with w48-boundary-census (A7-L2 scoped to its exclusive legs,
narrow-vs-retire ratification: red team) and with the standing verb-48
escalation. The A7-L2 grant itself is not narrowed here.

## Verdict: PROMOTE (fencing finding — promotes no value)

All bar clauses pass; no adverses. The 5 doubtful windows are fenced:
1 parses under 48='e' (@928 "pare"), 4 are confirmed orphans with named
loci (@377: 85's value; @398: 48's junction; @1398: 78's value; @1525: 48
itself). None of the 5 admits a stem parse, so the A7-L2 frame's scope
stays exactly its two exclusive legs @1229/@1589. No value is promoted; no
§7 constraint is touched; the red team's narrow-vs-retire ratification
remains theirs.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-stem48-scope-fence.md` (this file).
- `battery-queue.json`: `stem48-scope-fence` -> status `verdict`, result
  `promote` (temp-file + rename, own entry only; pre-write assert confirmed
  queued/verdictless; JSON re-validated post-write).
- Lock `locks/stem48-scope-fence.lock`: deleted on completion.
- No standing verdict contradicted or downgraded. `canonical.py` never used.
  R5005, sealed gates, red-team queue untouched.
