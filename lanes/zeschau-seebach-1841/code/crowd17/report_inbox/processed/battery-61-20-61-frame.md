# Battery verdict: 61-20-61-frame

**Verdict: NULL (fence)** — no determiner/adjective value for 20 parses @279-281's
"61 20 61" sandwich. The sandwich is fenced as a 20-value residual; the failure
localizes to 20's slot, not to 61's flanking "premier" legs.

## Target

- id: `61-20-61-frame` (priority 3)
- claim: name 61 and test whether any det/adj value parses @280's "61 [20] 61" sandwich
- evidence: battery-det-20-value.md null follow-up #2
- adverses: none stated

## Bar (verbatim from battery-queue.json)

name 61, then test det/adj candidates at @280's unique sandwich; fence if none parses

## Numbered pass/fail clauses (pre-registered before testing — bar not modified after data)

1. **Clause 1 (name 61):** PASS iff 61 is named at least at window level on
   byte evidence (a global naming additionally requires overturning the standing
   val-61-contact KILL with new byte-level evidence, per §5).
2. **Clause 2 (det/adj candidates):** PASS iff some determiner/adjective value
   for 20 yields a grammatical 1841-French parse of the sandwich.
3. **Clause 3 (fence):** if no candidate parses, fence the sandwich with stated
   cause (the bar's explicit escape arm).

## Method

Read BATTERY-PROTOCOL.md §1–§8 in full before testing. Created
`code/crowd17/next-token/locks/61-20-61-frame.lock` on start (agent id +
2026-10-09T03:43 UTC); no stale lock present. Re-derived the full stream from
`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt` with
the upstream byte-exact tokenization. Verified 1,847 pairs / 96 types.
`canonical.py` never touched. R5005, sealed gates, and the red-team adjudication
queue untouched. Standing values held fixed per §7.

## Window-level evidence (all byte-verified on the repaired stream)

### Uniqueness (re-derived)

- "61 20 61" trigram: exactly **1** occurrence stream-wide, @279 (0-based;
  @280 1-based — the target's offset). "61 20" and "20 61" bigrams: 1 each
  (both this window). 61: n=18. 20: n=15. Counts match det-20-value's census.

### The sandwich window — @279-281 (row a2_03)

`... [277]91 [278]37 [279]61 [280]20 [281]61 [282]42 [283]48 [284]52 ...`

Standing values in/near the window: 37 (S5; 37='le' MEDIUM, round-7), 42
(noun-class, cls), 48='e' (letter tier, promoted), 84='on' (@276), 00='pour'
(@287). 91, 61, 20, 52 unvalued (61 locus-valued, see below).

### Clause 1 — naming 61: PARTIAL (window-level "premier"; global stays fenced)

- 61's only named value is the locus-level **"premier"** at @1556
  ("61 40 17" = "première fois", val-61-premier PROMOTE, standing).
  val-61-contact's KILL of any GLOBAL 61 value stands and is not re-litigated
  here (no new byte evidence overturning it; §5).
- At the sandwich, "premier" composes on BOTH flanks:
  - Left: "37 61" @278-279 = **"le premier"** (37='le' S5 MEDIUM; article +
    nominalized ordinal — grammatical).
  - Right: "61 42" @281-282 = **"premier [noun]"** (42=noun-class; ordinal +
    noun — grammatical).
- The sandwich's middle (20) is the sole blocker: neither flank contradicts
  "premier". Clause 1 therefore names 61 as "premier" (ordinal word) at window
  level with two clean flanking legs; no global claim is made.

### Clause 2 — det/adj candidates for 20 at the sandwich: ALL FAIL

Tested with 61="premier" on both flanks ("premier [X] premier"):

- **"chaque" / "une"** (the only @307 survivors, det-20-value c1): FAIL —
  already tested at this exact window by battery-det-20-value (c2):
  "W chaque W" / "W une W" ungrammatical for any W. Cited, not re-litigated.
- **"cette" / "plusieurs" / "deux" / "dernière"**: FAIL — ungrammatical as
  standalone values at @307 (det-20-value c1), and "premier cette premier"
  etc. are ungrammatical at the sandwich independently.
- **Structural (all other det/adj):** FAIL at the category level. No French
  determiner or adjective X yields a grammatical "premier X premier":
  determiners are strictly pre-nominal and cannot be sandwiched between two
  identical content words; no adjective construction repeats its head
  ("premier [adj] premier" is not French). The one near-miss,
  "chaque premier [noun]" (cf. "chaque premier ministre"), would require a
  clause boundary inside the sandwich plus a bare-determiner clause start —
  2+ ungranted assumptions, beyond battery grade.
- Clause 2: **FAIL** — no det/adj candidate parses.

### Clause 3 — fence: TAKEN

@279-281 is fenced as a **20-value residual**: the failure localizes to 20's
slot (the category "determiner/adjective" is structurally excluded here given
61="premier" on both flanks), not to 61's flanking legs. This is consistent
with — and feeds — the standing 20 paradox (det leg @307 vs noun legs
@760/@839/@1703), whose venue is the queued P1 `poly-20-docket` (not
re-litigated here). The sandwich does NOT force 20 non-determiner at
kill grade: that conclusion is conditional on the "premier" extension, which
is flank-supported but not proven at this window — hence fence, not kill.

## Per-clause results

1. Name 61: **PARTIAL** — "premier" (locus value) parses on both flanks
   ("le premier" / "premier [noun]"); global naming fenced per standing KILL.
2. Det/adj candidates: **FAIL** — chaque/une killed (cited); cette/plusieurs/
   deux/dernière ungrammatical; structural exclusion for the category.
3. Fence: **TAKEN** — @279-281 fenced as 20-value residual.

**Verdict: NULL (fence).** No standing verdict contradicted or downgraded.
R5005, sealed gates, red-team queue untouched.

## Follow-ups proposed (null regenerates work; none duplicate queued targets)

1. `premier-61-flank-census` (P3): census all 18 61-windows for "premier"-
   admission (determiner/article/preposition left-adjacency, noun/verb
   right-adjacency). Decides whether "premier" is 61's conditioned value or a
   one-off locus; sharpens the val-61-premier locus promote.
2. `nondet-20-sandwich` (P3): test non-det/adj roles for 20 at @279-281 —
   conjunction/preposition candidates and the one-word "61-20-61"
   re-segmentation (20 word-internal) against French phonotactics. Coordinate
   with queued `poly-20-docket`; do not duplicate it.

## Bookkeeping

- `battery-queue.json`: `61-20-61-frame` queued → verdict/null (temp-file +
  rename, own entry only, pre-write assert confirmed no prior verdict, JSON
  re-validated).
- Lock created on start, deleted on completion. No standing verdict
  contradicted or downgraded.
