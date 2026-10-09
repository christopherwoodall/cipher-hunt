# Battery verdict: laisser-85-1699

- Target: `laisser-85-1699` (battery-queue.json, priority 3, status queued)
- Claim: "test 'laisser' at @1699 ('[91] laisser [33] n'importe ou...'): can 33 compose as laisser's object/complement under standing values; kill iff no composition parses with zero new assumptions"
- Note: the queue entry's `bars` field was empty (None); the bar above is taken verbatim from the dispatch brief, pre-registered before testing.

## Bar (verbatim, pre-registered)

"kill iff no composition parses with zero ungranted assumptions"

Numbered clauses:
- C1 (kill): NO composition of 33 as laisser-85's object/complement parses with zero ungranted assumptions → KILL.
- C2 (else): some composition parses cleanly → no kill (verdict NULL; the bar carries no promote clause — a consistent parse does not name a value).

## Method

Re-derived the repaired 1,847-pair / 96-type stream in-session from
`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`
(asserts held: 1,847 pairs, 96 types). `canonical.py` never used.
Tested both composition arms (direct object; causative complement) against
standing grants: 33=INF (registry cls), 85=verb-stem (A3 frame grant),
94='ne' (STRONG LEAD), 30='pas' (prom), 29='er' (pencil GT).

## Window-level evidence

Locus byte-confirmed, row a8_06:

| offset | cell | standing value |
|---|---|---|
| @1698 | 91 | unvalued |
| @1699 | 85 | unvalued (A3 verb-stem) |
| @1700 | 33 | INF (cls) |
| @1701 | 94 | ne (STRONG LEAD) |
| @1702 | 30 | pas (prom) |
| @1703 | 20 | unvalued |
| @1704 | 62 | unvalued |
| @1705 | 94 | ne (STRONG LEAD) |
| @1706 | 88 | gov (cls) |
| @1707 | 26 | noun (prom) |
| @1708–1711 | 12 06 29 40 | n / ent / er / e |

(Note: the claim's gloss "n'importe ou" is a misread — @1701–1702 is
94+30 = "ne pas", not "n'importe". Substance unaffected.)

The "85 33" bigram is a stream hapax (only @1699 of 15 eighty-five windows).
33's followers stream-wide: 29('er') x5 (the A10 "33+29" hold), 21 x3,
16/42/79/00/46 x2… — at @1699 the follower is 94, so the A10 "-er"
composition does not apply; 33 is bare here.

## Findings

**Arm 1 — 33 as laisser's direct object: DEAD on class.**
33 is INF class (registry). Direct objects are nominal. No composition.

**Arm 2 — 33 as laisser's causative complement ("laisser [33-INF]"): FAILS
on 85's incompleteness.**
The causative parse needs 85 to surface a complete auxiliary
("laisser"/"laisse"/"laissent"/…). But 85's standing tier is verb-STEM
(A3 frame grant). Under the lane's stem+completion model — 03+29
("03 29" x3, stem conditioned on its completion), 06/86 finite/imperative
vs infinitive-complement split, 06='ent' as a pure completion cell — a
stem cell needs a completion neighbor to surface as a complete verb word.
At @1699:
- left neighbor 91 is unvalued — supplying a completion from 91 is an
  ungranted assumption;
- right neighbor 33 is the putative complement itself (INF class); it
  cannot simultaneously be 85's inflectional ending (and per A10,
  33 is itself a stem taking "-er", not an ending);
- a null-completion license for 85 is ungranted;
- waiving A3 to let 85 surface complete "laisser" contradicts a standing
  frame grant — ungranted without red-team action or kill-grade evidence.

The "03" precedent is exact: 03 is verb-stem ONLY in "03 29" (with its
completion); elsewhere it is nominal. A stem without its completion is
not a verb. 85 at @1699 has no completion neighbor, so it cannot be the
causative auxiliary, so 33 cannot be its complement — not with zero
ungranted assumptions.

No other composition exists: 85+33 cannot be one word (two stems do
not compose), and 33 cannot be 85's ending (INF class, A10).

## Per-clause pass/fail

- C1 (kill iff no clean composition): FIRES. Both arms die — object on
  class, complement on 85's uncompletable stem tier. No composition
  parses with zero ungranted assumptions.
- C2 (else): moot.

## Verdict: KILL

33 cannot compose as laisser-85's object/complement at @1699 under
standing values without ungranted assumptions.

## Scope

Kills ONLY the @1699 composition claim. Untouched:
- 'laisser' as 85's value globally — owned by queued `laisser-85-15window`
  (scores all 15 windows independently); this kill is window-specific.
- 33='laisser' — the erstem-33-id candidacy (different cell, different
  hypothesis); untouched.
- A3 (85 verb-stem), A10 (33+29), 94='ne' STRONG LEAD, all standing and
  red-team verdicts; §7 intact. No value named, no polyvalence declared.
- The @1701+ tail ("ne pas [20] [62] ne [88-gov]…") remains unparsed;
  out of this bar's scope.

Observation for supervisor: the 85-completion question is now load-bearing
for `laisser-85-15window` — 85's followers stream-wide (58x3, 01x2, 08,
82, 93, 28, 04, 41, 36, 56, 48, 33; never 29) show no "-er"-completion
neighbor at any window, so however 85 surfaces complete verb forms (if
it does) needs its own account before any 85 value can be named.

No follow-ups required (kill, not null).

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-laisser-85-1699.md`
- Queue: `laisser-85-1699` queued → `verdict`/`kill`, 2026-10-09
  (pre-write assert passed — was queued/verdictless; target-id-unique
  temp file `battery-queue.json.laisser-85-1699.tmp` + atomic rename;
  disk re-validated; own entry only; no downgrade).
- Lock `locks/laisser-85-1699.lock`: created on start
  (2026-10-09T19:18:00Z, no stale lock), deleted on completion
  (verified gone).
- R5005, sealed gates, red-team adjudication queue untouched.
- Canonical-stream caveat stands (row a8_06 offset unvalidated).
