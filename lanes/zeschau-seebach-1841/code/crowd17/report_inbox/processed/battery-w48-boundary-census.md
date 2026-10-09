# Battery verdict: w48-boundary-census — 2026-10-09

Worker: 76554d77-461e-407e-9c98-b2f05207352d. Stream: repaired 1,847-pair parse
(`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`,
parsed per `repair_parse.py`; 1,847 pairs / 96 types asserted in-session).
`canonical.py` never touched. R5005, sealed gates, red-team queue untouched.
Lock `locks/w48-boundary-census.lock` created on start; deleted on completion.
@-offsets below are 0-based pair indices of the **48** token.

## Bar (verbatim, pre-registered BEFORE testing)

"classify 48's boundary (word-initial / -final / -internal) at all 38 windows
under standing values; the stem-frame survives as a general claim iff >=80%
of windows admit stem-internal 48; else scope A7-L2 to its exclusive legs or
retire it"

Numbered clauses (frozen before testing):

- C1: Classify 48's word-boundary position at all 38 windows on the repaired
  stream under standing values, with stated cause for each window.
- C2: The A7-L2 stem-frame ("48 as verb stem") survives as a GENERAL claim
  iff >=80% of the 38 windows admit stem-internal 48 — "admit" in the
  functional sense: 48 is stem-bound or stem-compatible (stem-attached
  inflection, stem head, or indeterminate with a live stem reading), NOT a
  free word-final letter of a closed word. If <80%, the frame is scoped to
  its exclusive legs (@1229/@1589) or retired.

Standing values used: 11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que (GT
pencil); 87=ce, 64=qui, 96=par, 17=fois, 79=tout, 00=pour, 84=on, 47=ce;
59=est, 77=le (provisional); 48='e', 12='n' (R17 tier); A7-L2 frame
"tout me [48-verb]" (grant); A3 85 verb-stem; A8 89 verb-frame. 1841
diplomatic French throughout.

## Method

Re-derived the repaired stream byte-exactly per `repair_parse.py`
(`repaired_offsets.json` + `data/upstream-ct_R5005.txt`): 1,847 pairs, 96
types, 38 windows of 48 — predecessor inventory re-verified in-session:
62 x6, 12 x5, 82 x4, 32 x4, 89 x3, 78 x2, 24 x2, 42/29/86/74/96/98/76/85/11/
65/71/19 x1 (matches verb-48 and fem-e-48; no drift). Each window classified
from its 7-wide context under standing values. "Admits stem-internal" = the
window's best standing-value parse places 48 as stem-bound/stem-compatible;
a window is NO iff 48 is forced to a non-stem role (free word-final letter
of a closed word, or word-initial with no stem reading). The inflectional
windows (32-48 x4, 19-48 x1) are classified per the standing fem-e-48
PROMOTE (2026-10-09): 48 is stem-attached inflectional -e there ("no
boundary is byte-evidenced between the stem and 48") — cited, not
duplicated. The 'ne' x5 census is cited from ne-census-1248 (PROMOTE).
Threshold: >=80% of 38 = >=30.4, i.e. >=31 windows.

## Window-level evidence

Context = 3 pairs each side; class = boundary position under standing
values; admit = stem-internal admitted (Y/N).

### NO — 48 forced to a non-stem role (9 windows)

| @ | context | class | cause |
|---|---|---|---|
| 126 | 66 98 **82 48** 11 02 26 (a1_03) | word-final | "me"+"la": closed clitic, word-initial successor; no elision ('la' consonant-initial) |
| 170 | 84 53 **12 48** 21 60 09 (a1_05) | word-final | "ne" closed; suc 21 open, no vowel-initial evidence for elision |
| 377 | 29 85 **82 48** 00 11 50 (a2_07) | word-final | "me"+"pour": closed clitic, word-initial successor |
| 398 | 64 79 **82 48** 06 11 45 (a2_07) | word-final | "me"+boundary (06 word-initial per verb-48); elision lead retired to x1 |
| 710 | 35 53 **12 48** 71 12 63 (a5_01) | word-final | "ne" closed; suc 71 open |
| 810 | 24 41 **12 48** 24 65 14 (a5_05) | word-final | "ne" closed; suc 24 open |
| 1076 | 98 98 **12 48** 77 78 64 (a6_05) | word-final | "ne"+"le": closed clitic, word-initial successor |
| 1525 | 24 11 **11 48** 96 87 46 (a8_00) | word-initial | "la"\|"e"\|"par": 48 word-initial after closed "la"; no coherent stem parse ("lae" not a word; "epar" not a word); residual, see caveats |
| 1737 | 06 60 **12 48** 52 86 12 (a8_07) | word-final | "ne" closed; suc 52 open |

### YES — stem-bound / stem-compatible / indeterminate (29 windows)

| @ | context | class | cause |
|---|---|---|---|
| 283 | 20 61 **42 48** 52 89 28 (a2_03) | indeterminate | 42 value open; stem reading live |
| 361 | 11 21 **62 48** 76 47 78 (a2_06) | indeterminate | 62 open; stem reading live |
| 365 | 76 47 **78 48** 49 61 70 (a2_06) | indeterminate | 78 value ungranted ("ver" is LEAD only); "vere"-kill not available under standing values |
| 426 | 47 14 **62 48** 76 42 63 (a2_09) | indeterminate | 62 open; stem reading live |
| 450 | 61 59 **32 48** 79 17 77 (a2_09) | word-final, stem-bound | "est 32e toutefois": inflectional -e, stem-attached per fem-e-48 PROMOTE |
| 542 | 12 44 **29 48** 42 06 00 (a3_01) | indeterminate | sole 29-48; residual, unparseable under standing values (fem-e-48); nothing forces a boundary role |
| 641 | 67 77 **89 48** 20 24 87 (a4_01) | word-final, stem-bound | "[89]-e": verb+ending-shaped, 48 bound to 89's verb (A8 frame) |
| 729 | 11 00 **86 48** 88 11 24 (a5_02) | indeterminate | 86 (INF class) value open; stem reading live |
| 856 | 51 64 **32 48** 84 02 24 (a5_07) | word-final, stem-bound | "qui 32e on": inflectional -e per fem-e-48 |
| 863 | 49 74 **74 48** 47 46 00 (a5_07) | indeterminate | 74 open; stem reading live |
| 872 | 87 77 **89 48** 20 74 49 (a5_07) | word-final, stem-bound | "[89]-e": verb-bound, as @641 |
| 928 | 17 61 **96 48** 82 98 83 (a5_10) | word-final, stem-bound | "pare": only grammatical parse ("par"\|"em…" is ungrammatical); 48 = inflectional -e on stem "par-" |
| 972 | 76 01 **98 48** 51 45 08 (a6_01) | indeterminate | 98 open; stem reading live |
| 987 | 01 24 **89 48** 01 76 49 (a6_01) | word-final, stem-bound | "[89]-e": verb-bound, as @641 |
| 1177 | 36 74 **32 48** 59 37 77 (a6_10) | word-final, stem-bound | "32e est": inflectional -e per fem-e-48 |
| 1212 | 64 59 **32 48** 96 45 36 (a7_00) | word-final, stem-bound | "est 32e par ce": inflectional -e per fem-e-48 |
| 1221 | 92 61 **24 48** 30 09 20 (a7_01) | indeterminate | 24 open; stem reading live |
| 1229 | 64 79 **82 48** 29 47 33 (a7_01) | word-initial, stem head | EXCLUSIVE LEG: "[48]er ce" — stem reading live and clean; "me" strained by following 29='er' (verb-48) |
| 1276 | 76 87 **76 48** 56 85 48 (a7_03) | indeterminate | 76 (verb-hood open) value open; stem reading live |
| 1279 | 48 56 **85 48** 53 61 56 (a7_03) | word-final, stem-bound | 85 = A3 verb stem; 85-48 = stem + -e, 48 stem-bound ending |
| 1316 | 36 74 **62 48** 98 15 24 (a7_04) | indeterminate | 62 open; stem reading live |
| 1350 | 73 34 **62 48** 77 78 94 (a7_05) | indeterminate | 62-48 + "le"; 62 open; stem reading live |
| 1398 | 76 47 **78 48** 40 67 77 (a7_07) | indeterminate | "78 e e": "veree"-strain depends on ungranted 78="ver" (fenced per fem-e-48); indeterminate under standing values |
| 1465 | 01 21 **62 48** 21 02 62 (a7_09) | indeterminate | 62 open; stem reading live |
| 1570 | 24 74 **62 48** 56 32 28 (a8_01) | indeterminate | 62 open; stem reading live |
| 1589 | 70 64 **65 48** 29 47 08 (a8_02) | word-initial, stem head | EXCLUSIVE LEG: "[48]er ce" — stem reading live and clean (verb-48) |
| 1614 | 55 83 **71 48** 31 76 42 (a8_03) | indeterminate | 71 open; stem reading live |
| 1658 | 37 11 **24 48** 47 98 98 (a8_04) | indeterminate | 24-48 + "ce"; 24 open; stem reading live |
| 1779 | 64 59 **19 48** 74 65 23 (a8_09) | word-final, stem-bound | "qui est 19e": inflectional -e per fem-e-48 (adj-19's leg intact) |

Check: 9 NO + 29 YES = 38. All windows accounted for.

## Count

- Admit stem-internal 48: **29/38 = 76.3%**
- Do not admit: 9/38 = 23.7% ('me' x3 clean, 'ne' x5, stranded word-initial 'e' x1 @1525)
- Bar threshold: >=80% i.e. >=31 windows. **29 < 31 — not met.**
- Robustness: flipping either judgment call (@928 "pare", @1525 stranded-'e')
  moves the count to 28/38 (73.7%) or 30/38 (78.9%) — still below 80%.
  Reaching the bar would require 31+, i.e. overturning a 'me'/'ne' window,
  none of which admits any stem reading. The outcome does not hinge on the
  close calls.

## Adverses

- **(a) Standing 48='e'.** ANSWERED — the entire census is conducted under
  R17-003 48='e'; every classification above uses it, and no window required
  any other value for 48.
- **(b) A7-L2 frame grant stands until red team narrows it.** FENCED with
  stated cause — this battery does not itself narrow or retire the grant. It
  executes the pre-registered decision rule and banks the scope outcome; the
  narrow-vs-retire ratification stays with the red team per verb-48's
  standing escalation (2026-10-08), which this result is consistent with
  (verb-48 headlined: "the frame, if it survives, is confined to its
  exclusive legs").

## Per-clause results

- **C1: PASS.** All 38 windows classified under standing values with stated
  cause each (table above).
- **C2: FIRES on the scope arm.** 29/38 = 76.3% < 80%: the stem-frame does
  NOT survive as a general claim. Per the pre-registered bar, the A7-L2
  frame is scoped to its exclusive legs (@1229 "qui tout me [48]er ce…",
  @1589 "pre qui 65 [48]er ce…") — the only two windows where the stem
  reading is live and clean — or retired, at the red team's ratification.

## Verdict: PROMOTE (census finding — promotes no value)

The 38-window boundary census is complete and byte-exact: 29/38 windows
admit stem-internal 48 (76.3%), below the 80% bar, so the A7-L2 stem-frame
does not generalize to 48 and is scoped to its exclusive legs @1229/@1589
(narrow-vs-retire ratification: red team). No value is promoted; no standing
verdict is contradicted or downgraded — verb-48's null (which proposed this
census), fem-e-48's promote (cited for the inflectional windows), and
ne-census-1248's promote (cited for 'ne' x5) all stand untouched. The
standing 48='e' is used throughout, never challenged.

## Caveats / residuals (not contradictions)

1. @1525 ("la e par", a8_00): stranded word-initial 'e' between closed "la"
   and "par" — unparseable under standing values. Recorded residual; it is a
   NO under every available reading, so it cannot move the count above the
   bar. Flagged as a possible segmentation/frame venue, not litigated here.
2. @365/@1398 (78-48): classified indeterminate because 78's value is
   ungranted ("ver" is R16-005 LEAD only). If 78="ver" were granted, the
   "vere"/"veree" kills would force a re-read of both windows.
3. @928 "pare": compositional reading (96-48 as one word); the two-word
   alternative is ungrammatical under standing values. Noted as composition,
   not as a granted value.
4. @542 (sole 29-48): residual per fem-e-48, unparseable; counted
   indeterminate (nothing forces a boundary role).

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-w48-boundary-census.md` (this file).
- `battery-queue.json`: `w48-boundary-census` -> status `verdict`, result
  `promote` (temp-file + rename, own entry only; pre-write assert confirmed
  queued/verdictless; JSON re-validated post-write).
- Lock `locks/w48-boundary-census.lock`: deleted on completion.
- No standing verdict contradicted or downgraded. `canonical.py` never used.
  R5005, sealed gates, red-team queue untouched.
