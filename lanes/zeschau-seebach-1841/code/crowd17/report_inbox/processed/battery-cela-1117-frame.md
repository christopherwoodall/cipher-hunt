# Battery verdict: cela-1117-frame — effect of the 'cela' promote on @1117's determiner frame

- Target: `cela-1117-frame` (priority 2)
- Claim: adjudicate the effect of battery-promoted cela-69-11-word on @1117's determiner frame
- Worker: battery-worker cela-1117-frame (agent de6ffec2-269a-4d2e-8377-c522ba96dfb8)
- Date: 2026-10-09
- Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, `repair_parse.py` tokenization). `canonical.py` never used. R5005 untouched. Sealed gates untouched. Red-team adjudication queue untouched. No invented numbers.
- Lock: `code/crowd17/next-token/locks/cela-1117-frame.lock` created 2026-10-09T07:22:28Z on start; no prior lock content was read (no stale-lock handling needed).
- Verdict: **NULL** (conditional bar; trigger pending)

## 1. Bar (verbatim from battery-queue.json)

"if '69 11'='cela' stands at @1115-1116, the 'la [88]' window dissolves and noun-88-det's bar is moot; if rejected, re-test clauses 2-4 of noun-88-det"

Numbered clauses (pre-registered BEFORE any window analysis; bar not modified after seeing data):

1. The 'cela' VALUE itself is not re-litigated here: it is red-team-owned (battery-cela-69-11-word.md, PROMOTE at battery grade). This battery adjudicates its EFFECT only.
2. Branch A — IF the 'cela' promote is RATIFIED at @1115-1116: the "la [88]" determiner frame at @1117 dissolves, and noun-88-det's bar (name one noun parsing both @402 and @1117) is moot.
3. Branch B — IF the 'cela' promote is REJECTED: clauses 2–4 of noun-88-det are re-tested.

## 2. Method

Re-derived the full stream independently (1,847 pairs / 96 types verified).
Extracted @1115-1117 on row a6_07; ran the full 88-predecessor census (n=23);
counted the "69 11" bigram stream-wide. The 'cela' value itself was NOT
tested — battery-cela-69-11-word.md is cited as the pending external input,
its bar, evidence, and locus-scope fence taken as stated. Checked the
red-team adjudication record for a ruling on battery-cela-69-11-word:
`code/crowd17/report_inbox/processed/next-token-redteam-r18.md` (dated
2026-10-08) does NOT adjudicate it — the cela battery filed 2026-10-09T02:47Z,
after the r18 docket cutoff. No later adjudication document exists. The
cela promote is therefore UNRATIFIED: neither branch's trigger has fired.
Note: the queue entry's adverses say "owned by round-18 red team"; the round
number is stale — ownership by the red team stands, the round is "next
available round," not r18. This battery touches nothing in that queue.

## 3. Window-level evidence

**W1 — @1115-1117 bytes (re-derived).** @1115=('69','a6_07'), @1116=('11','a6_07'),
@1117=('88','a6_07'); @1116's left neighbor is @1115=69, @1117's left-left is 69.
Full row a6_07 context: 63 00 66 73 41 65 38 30 **69 11 88** 70 12 06 14 06 11 52 37 43 00.

**W2 — "69 11" is stream-unique.** The bigram occurs exactly once in 1,847 pairs
(@1115-1116). n(69)=12, n(11)=45. The cela question is locus-scoped to @1116:
no other 11 position (@400, @1123, ...) is implicated, matching the cela
battery's explicit locus fence.

**W3 — 88-predecessor census (n=23, re-derived).** Predecessors: 39 x2 (@765,
@1727; 39="a" preposition), 69 x2 (@1260, @1267; 69 value open), 45 x1 (@402;
45="ce" granted A4), 11 x1 (@1117; 11="la" pencil), 17 singletons
(24,06,50,89,02,54,79,65,70,29,61,48,16,41,81,93,94). The ONLY
determiner-before-88 contacts in the stream are 45@402 and 11@1117 — the two
windows of noun-88-det's bar (matches battery-noun-88-det §2; independently
re-derived).

**W4 — The @1117 frame's single point of failure.** noun-88-det clause 2
requires @1116's 11 to be the FREE determiner "la" governing 88. The cela
battery's clause-1 reading makes @1115-1116 ONE word ("cela"), in which @1116's
11 is a word-internal syllable. One token position cannot be both
word-internal and a free determiner. The two readings are mutually exclusive
at this locus — no re-litigation of the value is needed to establish this;
it is the bar's own logical entailment.

**W5 — @402's frame is independent of the cela question.** @402's determiner
contact is 45 ("ce", granted A4) with its own left edge (@400-401 "11 45",
owned by queued ce88-leftedge-402). The cela question touches only @1116.
Under branch A, @402's "ce [88]" frame survives as the SOLE determiner-before-88
window; the 69 x2 contacts (@1260, @1267) are not determiner-governed at
battery level (69's global value fenced open; a locus-level cela promote at
@1115-1116 does not transfer to @1260/@1267).

## 4. Per-clause pass/fail

1. Red-team ownership honored, no re-litigation of 'cela': **PASS** — the
   value test was not run; battery-cela-69-11-word.md is treated as a pending
   external input throughout.
2. Branch A entailment (ratify → "la [88]" dissolves, noun-88-det bar moot):
   **PASS, CONDITIONAL** — the entailment is byte-sound and locus-scoped
   (W2, W4): if @1115-1116 is one word, @1116 cannot be the free determiner
   "la," so clause 2 of noun-88-det becomes unparseable and its iff-bar
   (requiring BOTH @402 and @1117) is moot. Fires iff the red team ratifies.
   Under this branch, 88's determiner window set shrinks to {@402} (W5).
3. Branch B pre-computation (reject → re-test clauses 2–4): **PRE-COMPUTED,
   FENCED** — the trigger (rejection) has not occurred, so no re-test was
   executed. Pre-computed outcome, carried as conditional findings:
   - Clause 2 (@1117 "la [88]"): stays CONDITIONAL. Rejection removes only
     strain (a) (cela-segmentation) of noun-88-det §3(b); strain (b) (number
     tension: "la [88-sg]" vs 3pl "70-12-06" frame, rescue ungranted) and
     strain (c) (spelling: "prenent" single-n, owned by queued
     spell-single-consonant) remain.
   - Clause 3 (one noun for both windows): re-finds FAIL. The gender clash
     is structural and cela-independent: "ce" selects masculine, "la" selects
     feminine singular; no regular French noun is both, and the epicene
     rescue is ungranted/invention. The cela question does not touch it.
   - Clause 4 (value determined by the windows): re-finds FAIL — the windows
     underdetermine any noun value; cela rejection adds no semantic hook.
   - Net under branch B: noun-88-det's verdict remains NULL. Rejection alone
     promotes nothing; it only restores clause 2 to testable-conditional.

## 5. Adverses

"do not re-litigate the 'cela' value itself — owned by round-18 red team;
coordinate, do not duplicate": HONORED. No value test on 69/11 was run.
battery-cela-69-11-word.md is cited, not duplicated; the round-number
staleness is recorded in §2 without touching any red-team material.
Coordination notes (not queue edits):
- `prennent-88-subject` already verdict/kill (2026-10-09); untouched.
- `noun-88-epicene` is queued, explicitly gated on this target: under branch
  A its gate ("both determiner frames alive") fails at its premise — see F2.
- `ce88-leftedge-402` queued; independent of this battery (owns @402's left
  edge, not @1116).

## 6. Verdict: NULL

The bar is a conditional whose trigger — red-team adjudication of
battery-cela-69-11-word — is pending. Neither branch can fire at battery
level without overstepping the adverses. This is a genuine inconclusive:
both branches are pre-computed against the bytes above, so the supervisor
can fire the correct branch the moment a ruling lands, with no re-running.
No standing verdict is contradicted (none exists on cela yet), and no
existing verdict is touched.

## 7. Recommended follow-up targets (for supervisor queueing)

F1. id: `cela-1117-frame-resume` | priority: 1
claim: "fire the pre-computed conditional branches of cela-1117-frame when the red team adjudicates battery-cela-69-11-word"
bars: "locate the red-team ruling in a processed adjudication doc; branch A (ratified): record noun-88-det's bar moot and shrink 88's determiner window set to {@402}; branch B (rejected): re-test noun-88-det clauses 2-4 carrying clause 3's gender clash as structural; the only new byte work permitted is citing the ruling"
evidence: "battery-cela-1117-frame.md §4 — both branches pre-computed, fenced on ratification"
adverses: "do not re-run the 'cela' value test; the red-team ruling is the sole trigger; never touch the red-team adjudication queue"

F2. id: `noun-88-epicene-rescope` | priority: 3
claim: "re-scope or kill noun-88-epicene if the red team ratifies 'cela', since its gate ('both determiner frames alive') fails at its premise"
bars: "on cela ratification: noun-88-epicene's two-window epicene bar is doubly moot (its gate dies with @1117's frame); decide rescope-to-single-window vs kill, without inventing values"
evidence: "battery-cela-1117-frame.md §4 branch A; noun-88-epicene queued, gated on cela-1117-frame"
adverses: "§7 sole-polyvalence rule; no invented values; this battery does not edit noun-88-epicene's queue entry"

## 8. Additional finding for the supervisor (pipeline gap, not a verdict)

battery-cela-69-11-word.md (PROMOTE, 2026-10-09) recommends follow-up
`ce69-global` (P2): test 69="ce" across all 12 windows. `ce69-global` is NOT
in `battery-queue.json` — its recommendation was ingested without queueing.
Per the lane's audit rule this is a pipeline gap; flagging it here for the
supervisor rather than queueing it myself (workers don't queue).

## Bookkeeping

- Lock `code/crowd17/next-token/locks/cela-1117-frame.lock` created
  2026-10-09T07:22:28Z, deleted on completion.
- `battery-queue.json`: `cela-1117-frame` queued → verdict/null
  (temp-file + rename; pre-write assert confirmed no prior verdict —
  entry carried status "queued", verdict null).
- R5005, sealed gate instances, red-team adjudication queue untouched.
