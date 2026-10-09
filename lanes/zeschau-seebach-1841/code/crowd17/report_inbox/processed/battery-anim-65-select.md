# Battery verdict: anim-65-select

- Target: `anim-65-select` (battery-queue.json, priority 3, status queued)
- Claim: 65's animacy established via selectional restrictions: test whether any 65 window forces inanimate or animate.
- Agent: 8bde2450-eba2-4146-9fa8-ed11fcdb74c4

## Bar tested (verbatim, pre-registered)

"Name 65 animate iff >=2 windows require an animate subject/object under standing values with zero kill-grade contradictions; name inanimate iff >=2 windows force it; else fence animacy as undetermined"

Numbered clauses:
- C1: Name 65 animate iff >=2 windows require an animate subject/object under standing values with zero kill-grade contradictions.
- C2: Name 65 inanimate iff >=2 windows force it.
- C3: Else fence animacy as undetermined.

## Method

Re-derived the repaired 1,847-pair / 96-type stream in-session from
`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`
(asserts held; `canonical.py` never used). Rendered all 25 windows of 65
(n(65)=25: @135 @138 @251 @293 @372 @455 @512 @687 @724 @787 @812 @923
@1106 @1112 @1208 @1253 @1340 @1383 @1530 @1588 @1608 @1683 @1712 @1748
@1781) with standing registry values (pencil GT, promoted, class-level,
leads) plus battery-grade-but-unratified 08='t', 94='ne', 98='vient' used
only as marked. Searched every window for a frame that selectionally
restricts 65: subject of "vient" (98), object of a value-named verb,
governed by an animacy-selecting preposition, or subject/object of a
selectionally-restrictive governor.

## Findings

No window forces 65 into an animacy-selecting slot. The three candidate
windows all fail at segmentation:

1. **@512** (byte-exact: `62 94 64 98 65 88 56 87 77 80`, row a3_00):
   "[62] ne qui vient [65] [88-gov] [56]". 65 is post-verbal after
   "vient" (98, battery LEAD). A literary inverted-subject reading
   ("vient [65]") would select an animate-capable subject, but 88
   follows immediately as a governor, and the lane's own @1340 window
   shows "vient" restarting asyndetically — the adverbial/object
   readings are not excluded at battery grade. Not forcing.

2. **@1340** (byte-exact: `86 71 64 60 08 65 64 52 38 47 86`, row a7_05):
   "[86] [71] qui [60]t [65] qui [52]". The "60 08" bigram is the
   battery "vient" case (unratified, red-team venue). Even granting it,
   65 sits post-"vient" before a "qui [52]" relative — a dislocated or
   adverbial element, not the subject. Not forcing.

3. **@1781** (byte-exact: `87 64 59 19 48 74 65 23 98 83 82 96`, row a8_09):
   "ce qui est [19] e [74] [65] [23] vient de m par". 65 precedes
   "[23] vient" (23 = verb class, battery; 98 = "vient", battery LEAD).
   If 23 is a finite verb, "[65] [23]" may be subject+verb — but 65+23
   could equally be NP-internal, and "vient" may head a new clause.
   Segmentation undecided at battery grade. Not forcing.

4. **Remaining 22 windows:** 65's valued neighbors are function words
   (qui, que, la, par, pour, tout, ne, ce, on, le, m, e, er, pre, fois,
   pas, est) or class-only cells (verbs 63/92/93/24, nouns 21/43/26/36,
   governors 88). No value-named transitive verb takes 65 as object;
   no animacy-selecting preposition governs it ("par" governs 96-led
   frames elsewhere, never 65 directly); "tout [65]" (@1683) and
   "le [60] [65]" (@455) license no animacy. Zero windows force
   inanimate either.

Score: C1 0/2 (no animate-forcing window), C2 0/2 (no inanimate-forcing
window).

## Verdict: NULL (fence executed)

**Bar tested:** C1 FAIL / C2 FAIL / C3 FIRES.

65's animacy is fenced as **undetermined** at battery grade. No window
requires an animate subject/object reading and no window requires an
inanimate reading under standing values. The three "vient"-adjacent
windows (@512, @1340, @1781) are the live frontier but each dies at
segmentation, not selection.

## Scope

Fences only the animacy question. Untouched: 65's noun-class grant
(registry cls), 98='vient' LEAD, 08='t' battery case, 94='ne' STRONG
LEAD, the subclass-66-98-noun promote (66 plain noun — no 65 claim
there), §7. No standing or red-team verdict contradicted, downgraded,
or re-litigated. Canonical-stream caveat stands.

## Follow-ups proposed (§4; all verified ABSENT from battery-queue.json)

1. `subj-65-512-inversion` (P4) — adjudicate "vient [65] [88]" at @512:
   inverted subject vs adverbial/object; decides whether 65 can ever
   occupy vient's subject slot.
2. `subj-65-1781-frame` (P4) — resolve "[65] [23] vient" segmentation at
   @1781 (subject+verb vs NP-internal 65+23).
3. `obj-65-1112` (P4) — test 65 as subject of 38 at @1112
   ("[65] [38-verb] pas [69-N]"): if 38's vouloir/devoir tie resolves to
   a selectionally-restrictive verb, this becomes an animacy leg.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-anim-65-select.md`
- Queue: `anim-65-select` queued → `verdict`/`null` 2026-10-09
  (pre-write assert passed — was queued/verdictless; target-id-unique
  temp file + rename; disk re-validated; own entry only; no downgrade).
- Lock `locks/anim-65-select.lock`: created on start
  (2026-10-09T19:18:57Z, no stale lock), deleted on completion
  (verified gone).
- R5005, sealed gates, red-team adjudication queue untouched.
