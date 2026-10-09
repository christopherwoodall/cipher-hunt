# Battery `val-31-1257-word` — verdict: NULL

**Target:** `val-31-1257-word` (P3)
**Claim:** Decide '[31]er' at @1257: infinitive vs noun vs word-internal-31.
**Date:** 2026-10-09

## Bar (verbatim, pre-registered)

"name with byte evidence or fence all three arms at the locus"

Restated as numbered pass/fail clauses:

- **C1:** Name the word: one of the three arms (infinitive / noun / word-internal-31) is established with byte evidence and zero new assumptions under standing values.
- **C2:** Otherwise, fence all three arms at the locus (each shown not to hold, with stated cause).

## Method

Re-derived the repaired 1,847-pair / 96-type stream in-session from
`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`
(parsed like `repair_parse.py`). Asserts held: 1,847 pairs, 96 types.
`canonical.py` never used. n(31)=8; "31 29" occurs exactly once (@1257);
"61 31" occurs exactly once (@1256–1257); both are stream hapaxes.

Standing values used: 06='ent' (R17-007 grant), 65 noun-class (R20-047),
46='que' (pencil GT), 29='er' (pencil GT letter cell), 69 noun-class
(R19-109 grant), 88 verb-stem (A3 frame), 11='la' (pencil GT).
Adverses adopted: 01 and 61 unvalued.

## Locus (byte-verified, row a7_02)

`@1248–1267: 67 46 26 30 06 65 46 01 61 [31] 29 69 88 01 09 11 50 46 69 88`

Reads: `[67] que [26] [30] ent [65-N] que [01] [61] [31]er [69-N] [88-V]
[01] [09] la [50] que [69-N] [88-V]`.

Note: "@1259–1260 = [69-N] [88]" is the subj-88-730 battery's leg-2
overt-subject pair (PROMOTE, battery grade, 2026-10-09): 69 is the subject
of finite-88 here. The "[31]er" token sits immediately before a
subject+finite-verb pair, inside the "que [01] [61] …" relative clause.

## Window-level evidence per arm

### Arm 1 — Infinitive "[31]er"

For 31 to be a verb stem, "[31]er" must be an infinitive, which requires a
governor. Candidates under standing values: 61 (unvalued), 01 (unvalued),
46='que'. "que" does not govern a bare infinitive in this frame (1841
French: que takes finite clauses); neither 01 nor 61 carries any standing
infinitive-governing license (61 is additionally NOT in its
premier-licensing slot here — left neighbor 01 is not a determiner cell,
per premier-61-admit-fence PROMOTE). Naming an infinitive = new assumption.

Further, 31 has battery-grade FINITE-verb class at @338 and @1647
("qui [31]" x2 — val-31-verb-test C1 PASS). An infinitive reading would make
31 both finite verb and verb stem. Per §7, 67 et/veut is the sole true
polyvalence; a finite/stem polyvalence for 31 has no red-team grant.

**Arm 1: FENCED** (conditional) — no licensed governor under standing
values; additionally requires an ungranted §7 polyvalence. Fence cause
stated; re-open is red-team polyvalence venue, not battery venue.

### Arm 2 — Noun "[31]er"

French -er nouns exist (fer, ver, hiver, berger…), but the frame
"que [01] [61] [N]" has no licensed parse under standing values: no
determiner precedes [31]er, and 01/61 are unvalued (their candidate sets —
'ain'/'ein'/'in'/'an' for 01 — contain no determiner). Naming the noun =
new assumption.

Further, as with Arm 1, a noun value for 31 would collide with its
battery-grade finite-verb legs (@338, @1647): verb/noun polyvalence,
ungranted under §7.

**Arm 2: FENCED** (conditional) — no licensed nominal parse under standing
values; additionally requires an ungranted §7 polyvalence. Same re-open
venue as Arm 1.

### Arm 3 — Word-internal-31

For 31 to be word-internal at @1257, "61 31" (or "01 61 31", with or without
29) must be one word. "61 31" is a stream hapax — no recurrence licenses
or forbids the wordhood. Scheme plausibility: word-internal cells are live
in this cipher (pencil crib "premier" = 70 82 34 29 40; ce-08-31-frame
PROMOTE has 08 word-initial in an "[08][31]" word at @1488, so 31 itself is
word-internal in at least one window). But no standing value licenses
"61 31" / "01 61 31" as a word, and nothing at the locus contradicts it.

**Arm 3: NOT FENCED** — no kill-grade contradiction available; the hapax
gives no discriminating evidence either way. This arm hinges on 61's
(future) value.

## Per-clause results

- **C1: FAIL** — no arm nameable with byte evidence and zero new assumptions.
- **C2: FAIL** — only two of three arms fenced; the word-internal arm
  cannot be fenced at kill grade on current evidence.

**Verdict: NULL.** The infinitive and noun arms are fenced (both need an
ungranted §7 polyvalence on top of unlicensed frames); the word-internal
arm survives unfenced. No standing or red-team verdict contradicted
(§5.2 does not fire); 31's finite-verb legs (@338, @1647) untouched;
val-31-finite-name's KILL (finite-value naming fenced) adopted, not
re-litigated. §7 intact. Canonical-stream caveat stands (row a7_02 offset
unvalidated).

## Follow-ups proposed (all verified ABSENT from battery-queue.json;
supervisor to queue per §4)

1. `poly-31-docket-input` (P2, gather-only) — package 31's two finite legs
   (@338, @1647) plus the @1257 polyvalence tension (finite/stem,
   verb/noun) as red-team docket input. The infinitive and noun arms at
   @1257 need a polyvalence ruling before any battery can re-open them.
   Bar: evidence package only; no naming.
2. `val-61-wordbound-1257` (P3) — when 61 receives any value/grant,
   re-test "61 31" wordhood at @1256–1257 (stream hapax). The surviving
   word-internal-31 arm hinges on this boundary.
   Bar: name the boundary (one word vs two) with zero new assumptions,
   else fence word-internal-31 at the locus.
3. `locus-1257-reseg` (P4) — test the "31 | 29" boundary alternative
   (31 standalone word + 29-initial word, e.g. finite-31 + "er…") against
   the "[31]er" word-shape presupposition shared by all three arms in this
   bar. Bar: byte-evidence for one segmentation, else fence the
   presupposition.

## Scope

Names nothing. Untouched: 31's value, 01's value, 61's value, 69's
noun-class grant, 88's value, the subj-88-730 promote (adopted as
background), R5005, sealed gates, red-team adjudication queue.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-val-31-1257-word.md`
- Queue: `val-31-1257-word` → `status: verdict`, `verdict: {result: null,
  report: code/crowd17/report_inbox/battery-val-31-1257-word.md,
  date: 2026-10-09}` (pre-write assert passed — was queued/verdictless;
  temp-file + rename; disk re-read confirms; own entry only; no downgrade)
- Lock created on start (2026-10-09T17:15:00Z, agent
  c03f9d9e-1fcc-4f2d-bda8-52ff8b4f8678), deleted on completion.
- `canonical.py` never used. No follow-ups written into battery-queue.json
  by this worker (supervisor queues per §4); own entry only.
