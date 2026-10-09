# Battery `58-det-numeral-tension` — verdict: PROMOTE (red-team input package delivered)

Target: red-team INPUT package — the A&B frames cohere on a numeral/determiner value ('deux/plusieurs/quelques'-shaped), contradicting 58's battery-grade nominal class. Date: 2026-10-09.
Worker: agent 98e90587-5f97-4c4c-8db6-2dfe21d4ff80.
Lock: `code/crowd17/next-token/locks/58-det-numeral-tension.lock` (supervisor-created, fresh; deleted on completion).

## Bar (verbatim, pre-registered from battery-queue.json BEFORE testing)

"package the byte evidence (A&B frames, windows, counts) for red-team adjudication; battery grade cannot resolve a class conflict - gather, do not decide"

Numbered clauses (fixed BEFORE the stream census, not modified after):

- **C1 (gather):** the byte evidence for frame A — @1756 "[58] fois" (window, @-offset, counts) — is recorded in this report.
- **C2 (gather):** the byte evidence for frame B — @1695 "que [24] [85] [58] [15]" (window, @-offset, counts) — is recorded in this report.
- **C3 (package):** the package states the numeral/determiner coherence claim ('deux/plusieurs/quelques'-shaped) as the red-team input claim, with its byte support, without deciding it.
- **C4 (no decide):** no class decision is made at battery grade; the standing adverse (58's nominal class, battery PROMOTE) is fenced, not re-opened; the package is delivered to the red-team docket in this report.
- **Verdict rule:** promote iff the package is delivered to the docket; null (with 1–3 follow-ups) iff it cannot be completed. No follow-ups needed for a delivered package.

## Method

1. Read BATTERY-PROTOCOL.md §1–§8 in full first. `canonical.py` never used.
2. Re-derived the repaired 1,847-pair / 96-type stream in-session from
   `code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`,
   parsed like `code/side-keyhunt/repair_parse.py` (asserts held: 1847
   pairs, 96 types). R5005, sealed gate instances, red-team adjudication
   queue untouched.
3. Adopted premises (not re-litigated): pencil GT (11=la, 70=pre, 82=m,
   34=i, 29=er, 40=e, 46=que); granted 87=ce, 64=qui, 96=par, 17=fois,
   79="tout" (A5), 00="pour" (A9), 84="on" (A15), 47="ce" (A4); provisional
   77=le, 59=est; 85 verb-stem (A3); 45='ce' A11 HOLD (ungranted);
   58 nominal noun-class (58-complement-1695 PROMOTE, 2026-10-09 — standing
   adverse, fenced); §7 (67 et/veut sole polyvalence). 1841 diplomatic French.
4. This report is the docket package. It decides nothing.

## Window-level evidence (byte-exact, 0-based @-offsets)

### 58 census (re-derived, byte-exact)

n(58) = 7. Positions: [55, 122, 157, 610, 1202, 1695, 1756].
Predecessors: {85:3, 19:1, 35:1, 02:1, 45:1}.
Successors: {35:2, 66:1, 47:2, 15:1, 17:1}.
Zero granted-determiner (11/47/87/79/77) predecessors; zero nominal-position
determiners anywhere.

### FRAME A — @1756 "[58] fois" (row a8_08, row start 1745, in-row pair 11)

Window (±4): `@1752..1760 = 26 24 85 58 17 78 41`
Byte check: row a8_08 digits `…2624|855817|7841…` — pairs `26 24 85 58 17 78 41`;
  @1756 in-row pair 11 = raw digits "58". @1755=85 (verb-stem), @1757=17=fois (granted).
Geometry: "85 58 17" trigram — verb-stem + 58 + fois.
Corpus frequency of "85 58" bigram: 3 (@54, @1694, @1755). The @1755 instance
  is the ONLY "85 58 17" trigram in the stream.
Follower census of 17 (n(17)=15, positions
  [17,238,308,369,452,556,837,880,925,1040,1157,1289,1461,1558,1757]):
  predecessors {53:1, 41:1, 20:1, 70:1, 79:2, 34:1, 56:1, 78:1, 71:1, 40:2,
  80:1, 11:1, 58:1}.
  Determiner-shaped predecessors attested before 17: 11=la (granted, @1289
  `68 00 11 17 84 59 35`), 79="tout" (granted, @452 `32 48 79 17 77 60 65`,
  @1461 `86 66 79 17 01 21 62`), 70=pre (banked, @238 `70 98 41 17 11 26 12`).
  58 is the 13th distinct predecessor of 17 — the ONLY "58 17" adjacency in
  the stream. No granted NOMINAL value precedes 17 in this census except via
  the contested 58 slot itself.
Summary for the docket: frame A puts 58 in the immediate-pre-"fois" slot, a
  slot whose other occupants are determiner/demonstrative-shaped granted
  values (la, tout, pre).

### FRAME B — @1695 "que [24] [85] [58] [15]" (row a8_06, row start 1693, in-row pair 2)

Window (±4): `@1691..1699 = 27 46 24 85 58 15 23 91 85`
Byte check: row a8_06 digits `2485|5815|2391…` — pairs `24 85 58 15 23 91 85`;
  @1695 in-row pair 2 = raw digits[4:6] = "58". @1693=24 (conflict class,
  modal parse dead per 24-en-verb-conflict consequences), @1694=85
  (verb-stem), @1696=15.
Geometry: "85 58 15" trigram — verb-stem + 58 + 15, the same 85-governed
  complement geometry as frame A's "85 58 17".
Follower census of 15 (n(15)=10, positions
  [323,775,1017,1318,1420,1495,1696,1730,1760,1811]):
  predecessors {60:1, 94:1, 41:2, 98:1, 79:1, 66:1, 58:1, 30:1, 61:1}.
  58 is the sole "58 15" adjacency in the stream. 79="tout" (granted)
  precedes 15 once (@1420) — the same determiner-shaped type that precedes
  17 twice and 58 never.
Summary for the docket: frame B puts 58 bare between verb-stem 85 and 15,
  with 15 in a slot also occupied after the granted determiner "tout".

### FRAME C (tension side, recorded for completeness) — @1202 "ce [58]" (row a7_00, row start 1191, in-row pair 11)

Window (±4): `@1198..1206 = 16 64 29 45 58 47 43 55 61`
Byte check: row a7_00 digits `…166429|455847|435561…` — pairs
  `16 64 29 45 58 47 43 55 61`; @1202 in-row pair 11 = "58".
@1201=45 ('ce' under ungranted A11 HOLD); @1203=47=ce (granted).
"58 47" adjacency count in stream: 2 (@610, @1202).
47 census: n(47)=28; successors {78:5, 46:3, 11:3, 33:2, 03:2, 98:2, 41:1,
  01:1, 14:1, 44:1, 77:1, 91:1, 43:1, 76:1, 86:1, 08:1, 68:1}.
  58 is NOT a 47-successor (no "ce 58" at grant level).
45 census: n(45)=22, positions [14,104,262,314,332,340,401,437,478,569,574,
  603,678,697,974,983,1024,1055,1165,1201,1214,1551]; @1201 is the only
  "45 58" adjacency.
Summary for the docket: under the A11 HOLD, frame C forces a masculine
  nominal reading of 58 — disjoint from the determiner/numeral set that
  frames A∧B cohere on. Frame C itself rests on an ungranted premise.

## The numeral/determiner coherence (input claim — stated, not decided)

The A∧B pair jointly favors a numeral/indefinite-determiner value for 58
('deux/plusieurs/quelques'-shaped), with zero new assumptions:
- Frame A: "…[24] [85] [58] fois…" = "…[modal] [verb] deux fois"
  ("répéter deux fois"-shaped) — grammatical with 58 = numeral; no bare
  common noun can directly precede "fois" in 1841 French.
- Frame B: "que [24] [85] [58] [15]" = "que [modal] [verb] deux/plusieurs/
  quelques [15]" — grammatical iff @1696=15 is a (plural) noun; the same
  85-governed complement geometry as frame A.
- Corpus support: determiner-shaped granted values (11=la, 79="tout",
  70=pre) occupy the pre-17 slot; 79="tout" also occupies the pre-15 slot.
  58 occupies both slots exactly once each. This is the A∧B coherence the
  red team is asked to weigh.

## The standing adverse (fenced, not re-opened)

Adverse: "58's nominal class granted at battery grade"
(58-complement-1695 PROMOTE, 2026-10-09).
Answered by fencing: the PROMOTE stands on its own pre-registered bar and
is NOT contradicted, downgraded, or re-opened here (§5.2). This package
records the class conflict — frames A∧B's numeral/determiner coherence vs
the battery-grade nominal class — and escalates it to the red-team venue
(§7). §7 polyvalence bar intact (67 remains the sole true polyvalence;
no polyvalence declared for 58). If the red team rules against the nominal
class, that verdict is theirs to ratify — this battery takes no position.

## Per-clause results

- **C1 (frame A gathered): PASS.** @1756 window, byte check, 17-predecessor
  census (13 distinct predecessors incl. granted determiners la/tout/pre),
  "58 17" uniqueness — all recorded above.
- **C2 (frame B gathered): PASS.** @1695 window, byte check, 15-predecessor
  census, "85 58 15" geometry, "58 15" uniqueness — all recorded above.
- **C3 (coherence stated, not decided): PASS.** The numeral/determiner
  input claim and its byte support are stated in this report; the class
  conflict is recorded, not resolved.
- **C4 (no decide; adverse fenced): PASS.** No class verdict taken here;
  the standing nominal-class PROMOTE is fenced, not re-opened; the package
  is delivered to the red-team docket in this report.

## Verdict: PROMOTE (package delivered to the red-team docket)

The bar's promote condition — package the byte evidence for red-team
adjudication — is met in full. This promotion is a docket-delivery
promotion, NOT a class promotion: it does not promote any value or class
for 58, and it leaves the standing 58-complement-1695 PROMOTE untouched.
No follow-ups needed (bar: "no follow-ups needed for a delivered package").
R5005, sealed gate instances, red-team adjudication queue untouched.
Canonical-stream caveat stands (rows a8_08, a8_06, a7_00 offsets unvalidated).

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-58-det-numeral-tension.md`
  (this file).
- Queue: `58-det-numeral-tension` → status `verdict`, result `promote`,
  2026-10-09 (own entry only; temp-file + rename; JSON re-validated).
- Lock `locks/58-det-numeral-tension.lock`: deleted on completion.
