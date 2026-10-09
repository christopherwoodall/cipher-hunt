# Battery verdict: reseg-1481-98

Worker: 55e770fa-9f72-4a2a-b53a-c8c50c319cc9. Date: 2026-10-09.
Lock: `code/crowd17/next-token/locks/reseg-1481-98.lock` created 2026-10-09T05:22:49Z;
no prior lock existed; deleted on completion.

## Bar (pre-registered verbatim, from battery-queue.json)

"byte-evidenced boundary or reseg; else red-team escalation"

Adverses (queue): none.

Numbered clauses (pre-registered BEFORE testing, not modified after):

1. A byte-evidenced clause boundary exists at the @1481 locus
   ("82 16 98", 1-based @1481-1483, row a7_10) that resolves the forced
   contradiction ("m'a/m'est" + finite 98).
2. Else, a byte-evidenced re-segmentation of the locus dissolves the
   forced contradiction without introducing kill-grade violations.
3. If neither clause 1 nor clause 2 passes, escalate to the red team
   (the "24/28 fit" overcount stands unrepaired at battery grade).

"Byte-evidenced" = row boundary, pencil gloss anchor, formula marker, or a
row-global offset re-pairing that is constraint-clean against banked/granted
constraints (the seg-a1_01-constraint-sweep standard).

## Method

Read BATTERY-PROTOCOL.md first. Re-derived the repaired stream in-session
from `data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`,
parsed per `code/side-keyhunt/repair_parse.py` (1,847 pairs / 96 types
verified; `canonical.py` never used). R5005, sealed gates, red-team
adjudication queue untouched. Lane @-convention is 1-based (verified: the
doubled frame "82 16 96 82 16 64" sits at 1-based @1195-1200 = 0-based
@1194-1199).

Locus, byte-exact: 1-based @1481-1484 = "82 16 98 62" = 0-based @1480-1483,
all on row a7_10 (55 digits, canonical offset 0, stream span 0-based
1470-1496). Row digits:
`2612415360066733298216986246778424870831923924006615594`.

The forced contradiction (val-16-a-vs-est, confirmed): "82 16 98" reads
"m [16-finite-verb] [98-finite-verb]" — "m'a"/"m'est" license only
participle/adjective complements; 98 is finite-verb class-level per standing
battery verdict prof-98 (§5). Unrescuable under canonical pairing.

## Clause 1 — clause boundary: FAIL (no byte evidence)

- Row boundary: none. The full trigram sits mid-row a7_10 (row spans
  0-based 1470-1496; locus at 1480-1483).
- Pencil gloss: none on a7_10. Gloss anchors exist only at a5_03 and a8_05.
- Formula marker: none. a7_10 carries no formula-row status in REPORT.md;
  the neighboring "33-29" laisser frame is a stem frame, not a row formula.
- Standing boundary groups: none at the contact (no 96='par' stranding,
  no punctuation-like group).
- Letter-level rescues without offset change were already exhausted by
  val-16-a-vs-est ("16+98" one word = "avient"/"estvient", not French;
  "82+16" as possessive "ma" + finite verb, ungrammatical). A "16"-as-letter
  reading has no standing letter value; "98" word-internal would contradict
  prof-98 (§5-forbidden).

## Clause 2 — offset-1 re-segmentation of row a7_10: PASS

Offset-1 pairs (drop digit 0, 27 pairs):
`61 24 15 36 00 66 73 32 98 21 69 86 24 67 78 42 48 70 83 19 23 92 40 06 61 55 94`

- The contradiction DISSOLVES: digit span dp18-25 "82169862" re-pairs to
  "98 21 69 86 24". Neither "82" nor "16" occurs anywhere in the offset-1
  row. The "m'a/m'est + finite" frame is gone, not re-created elsewhere
  (no 82/16 in offset-1; no new "11+verb" or "que"-misuse patterns).
- 27/27 pairs are members of the 96-type canonical inventory (zero novel
  groups).
- Constraint sweep (seg-a1_01 standard — kill-grade = a standing value
  forced into an impossible reading):
  - GT respected: 70='pre' ("48 70 83", strained slot, value intact),
    40='e' ("92 40 06" reads "[92e] [ent...]", 06 syllabic per
    ent-06-host-census since 40 is not a verb stem), 46/11/82/34 absent.
  - Granted respected: 00='pour' ("36 00 66" = "[36-noun] pour [66]",
    grammatical); 96/79/87/64/47 absent. A15 C1-C3: no 84 in offset-1,
    vacuous.
  - Battery-promoted respected: 94='ne' (row-final "55 94" — row-final "ne"
    is canonically attested at a1_02 and a8_09, pattern not novel);
    06='ent' (syllabic at "40 06", finite-ending rule not engaged);
    98=finite-verb ("32 98 21" admits a clause boundary, the same rescue
    the seg-a1_01 sweep allowed for "fois [98] [55]" — strained, not
    forced); 48='e' letter-tier only; 24 read at class level only
    ("61 24 15", "86 24 67" with 67="et" by the positional rule —
    neither window is a gerund frame, so the queued 24-en-verb-conflict
    is not engaged).
  - Kills respected: 48 never est/ne/de; {48,94} homophone intact; no
    81/84/20/60/62/68 violations; 16=infinitive (§5 promote) untouched —
    16's absence from the row is not a contradiction; prof-98's legs are
    the 98->83 "vient de" windows, none on a7_10.
  - Splits/holds intact: 20~17, 23~26 (23 alone, fine); holds 19 / 45 A11 /
    09~92 A6 / 33+29 A10 — see costs below.
  - 67 positional rule: 67 at offset-1 idx13, follower 78 (open, not
    infinitive-shaped) → "et" reading, no violation.
- COSTS (stated, not hidden): offset-1 dissolves canonical windows cited
  by other batteries —
  - @1484 "62 46 77 84 24": the A15-C1 elision support leg loses 1 of its
    7 windows (elision-77-84 PROMOTE; the leg survives 6/7 — weakened,
    not destroyed). lon-legs-census cites it as "A15's en-arm leg".
  - @1482 "98 62 46 77 84": il-62's "que l'on" corroboration dissolves.
  - @1477 "33-29": 1 of 5 corpus "33-29" attestations dissolves (A10 hold
    intact, 4 remain; erstem-33-id's LEAD loses one data point).
  - Neutral/residual windows dissolved: a-39 @1491, noun-26 @1470
    (verb-branch residual), verb-60 V4 @1474 (null), prof-53 W10 @1473
    (null), fence-84-29-gate @1485 (fence row).
  - The A15 grant of 84='on' itself is untouched (no 84 in offset-1 either
    way); only one support-leg window is removed.

## Clause 3 — red-team escalation: NOT TRIGGERED

Clause 2 passed. Adoption of offset-1 for row a7_10 remains a red-team
adjudication act (same standing as seg-a1_01-constraint-sweep) — the
reseg is a viable battery-grade mechanism, not a declared re-pairing.
The canonicality caveat stands: a7_10's offset is one of the 68
unvalidated upstream row offsets.

## Verdict: PROMOTE (sweep finding — promotes no value, kills nothing)

Offset-1 of row a7_10 is constraint-clean across all 27 pairs: zero novel
groups, zero kill-grade violations against banked/granted constraints, and
it dissolves the @1481 forced contradiction that the finite-verb class
lead could not survive ("24/28 fit" overcount repaired at the mechanism
level). Costs are the dissolved cited windows above — headlined, the
sharpest being 1 of 7 A15-C1 elision legs. Whether to adopt offset-1 is a
red-team adjudication act.

## Standing-state check

No standing verdict contradicted or downgraded. §7 intact (no polyvalence
declared). gate-satisfiability-16-85 (16=infinitive, §5) untouched.
prof-98 untouched. A15 grant untouched. R5005, sealed gates, red-team
adjudication queue untouched. `canonical.py` never used.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-reseg-1481-98.md`
- Queue: `reseg-1481-98` → verdict/promote (temp-file + rename; pre-write
  assert confirmed queued/verdictless; JSON re-validated post-write).
- Lock created on start, deleted on completion.
