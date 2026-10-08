# Battery report: fence-911-de — @911 '64-83-59' fences with stated cause under the 83='de' lead, or unconditioned 83='de' is killed

- Target: fence-911-de (priority 2; parvenir-thirds finder T2)
- Date: 2026-10-08
- Worker: ce262f4d-7ef4-4aae-9e1d-f74048089a5d
- Verdict: **null** — kill-grade failure of unconditioned 83='de' recorded at @911, escalated to the red team. No battery-level kill (lead shared with le83-window; per bar and task instruction).

## Bar (verbatim, pre-registered)

"resolve iff ONE grammatical parse covers '64-83-59' with <=1 non-granted assumption; else record kill-grade failure of unconditioned 83='de' and escalate (do not kill at battery level — the lead is shared with le83-window)"

## Bar restated as numbered pass/fail clauses

1. (Resolve) ONE grammatical parse covers the '64-83-59' trigram at @911 using at most one non-granted assumption (64='qui' is granted; 96='par' is promoted).
2. (Else) No such parse exists: record kill-grade failure of unconditioned 83='de' at @911 and escalate to the red team; do NOT kill at battery level.

## Method

Parsed the repaired stream per code/side-keyhunt/repair_parse.py
(code/side-keyhunt/repaired_offsets.json + data/upstream-ct_R5005.txt):
1,847 pairs confirmed. Never used canonical.py. Never touched R5005.
No invented data; every number below traces to the stream.

## Window-level evidence

### The target window @911 (row a5_09, mid-row: row spans @900–@923, no boundary artifact)

@903–@918: `16 88 18 55 83 54 49 64 83 59 37 96 09 02 24 49 74`

Target trigram @910/@911/@912 = `64 83 59`. Under 64='qui' (granted),
83='de' (lead under test), 59='est' (provisional): **"qui de est"** —
ungrammatical. The trigram is unique stream-wide (1 occurrence);
the 64-83 bigram and the 83-59 bigram are likewise unique.

Local frame check: @912/@913/@914 = `59 37 96` = "est [37] par" under
59='est' provisional + 96='par' promoted — one of the six A1 predicative
59->37 frames. 59='est' is load-bearing and locally coherent here,
which closes the "59 is not 'est' here" fence (see below).

### Parse attempts (all fail the <=1-non-granted-assumption bar)

- **P1 "qui de est"** (83='de' + 59='est'): 2 non-granted assumptions and
  ungrammatical — preposition "de" cannot take finite "est" as complement.
- **P2 fence adverse 1 — 59 not 'est' here**: "qui de [59]" still needs a
  nominal 59 in a partitive "qui de nous"-shaped construction. That costs
  (i) the 83='de' lead, (ii) a local nominal 59 — contradicting the
  promoted est-59-frames battery (2026-10-08) and the local 59->37 A1
  frame — and (iii) a literary partitive reading. >=2 extra non-granted
  assumptions, one contradicting standing evidence. The cheapest fence
  does not hold.
- **P3 fence adverse 2 — clause boundary between 83 and 59**:
  left clause ends "...54 49 qui de" — stranded "de" clause-finally is
  ungrammatical (French has no preposition stranding). Putting 83 in the
  right clause gives "qui | de est", equally ungrammatical. The boundary
  fence does not hold.
- **P4 syllabic 83** (cf. le611's 87-83="cède" re-read): 64-83 = "qui-de"
  is no French word; 64='qui' is granted as a word, so no composition
  is available at this window.

No grammatical parse covers '64-83-59' with <=1 non-granted assumption.
**Clause 1 FAILS. Clause 2 (else-path) is taken.**

### 15-window 83 profile (supporting context, re-derived)

83 n=15: @228 98-83-82 | @614 87-83-70 | @898 98-83-86 | @907 55-83-54 |
@911 64-83-59 | @931 98-83-56 | @1061 98-83-82 | @1161 44-83-21 |
@1171 87-83-21 | @1217 77-83-92 | @1334 39-83-86 | @1612 55-83-71 |
@1784 98-83-82 | @1829 38-83-24 | @1840 44-83-21.

- de-compatible: @228/@1061/@1784 (98-83-82 formula), @898 (98-83-86,
  'de'+INF, 86 INF-class granted), @931, @907, @1161/@1840 (owned by
  queued de-frame-44-83-21), @1612.
- Hostile to unconditioned 83='de' (5 of 15):
  - @911 "qui de est" — kill-grade failure (this battery).
  - @1217 "le de" — fenced as 83-blocker (le83-window battery, null).
  - @614/@1171 "ce de" x2 — fenced to queued frame-87-83-cede
    ('cède'-verb rival).
  - @1334 "39-83-86": 39='a' promoted; "a de [INF]" ungrammatical as
    separate words (39 word-internal possible — unfenced, new cell).
  - @1829 "38-83-24": 24 is a promoted finite verb (ne-24-profile);
    "de"+finite verb ungrammatical (new cell).

## Per-clause verdict

- Clause 1 (resolve): FAIL — no grammatical parse with <=1 non-granted
  assumption; both listed fences (59-not-'est', clause boundary) tested
  and broken.
- Clause 2 (else): TAKEN — kill-grade failure of unconditioned 83='de'
  recorded at @911 and escalated to the red team.

A window forcing the claim false is the protocol's kill grade (§4), and
@911 forces unconditioned 83='de' false conditional on 64='qui'
(granted) and 59='est' (provisional, locally coherent via the 59->37
A1 frame). Per the bar and the task instruction the kill is NOT
executed at battery level — the 83='de' lead is shared with
le83-window — so the verdict is **null with escalation**.

## Adverses answered

- "59='est' is provisional (cheapest fence: 59 not 'est' here)": TESTED —
  even dropping 59='est', "qui de [59]" needs a nominal 59 (contradicts
  the promoted est-59-frames battery) plus a partitive construction;
  >=2 extra assumptions. Fence broken, recorded above.
- "a clause boundary between 83 and 59 is the alternative fence":
  TESTED — strands "de" clause-finally (no preposition stranding in
  French). Fence broken, recorded above.

## Standing red-team check

No standing red-team verdict on 83='de' is contradicted. The le83-window
battery (2026-10-08, null) explicitly assigns kill-grade on the
unconditioned 'de' lead to this battery ("fence-911-de owns" it) and
fenced 83 as the blocker at @1217 — consistent, no overwrite.

## Follow-up targets (null regenerates work)

1. **escalate-83-de-kill** — red-team adjudication on the recorded
   kill-grade failure: unconditioned 83='de' now carries hostile cells
   at @911 (this report), @1217 (le83-window fence), @614/@1171
   (frame-87-83-cede), plus new cells @1334 and @1829. Bar: red team
   either executes the battery-level kill of unconditioned 83='de' or
   states the conditioning rule (positional? second polyvalence?) that
   saves the lead.
2. **de-83-residuals** — resolve the two newly-noted hostile cells under
   any surviving conditioned 83='de': @1334 '39-83-86' ("a de [INF]",
   39 word-internal fork open) and @1829 '83-24' ("de"+promoted finite
   verb). Bar: both windows parse or are fenced with stated cause;
   feeds the queued de-83-sweep.
3. **syll-83-de** — test 83 as syllabic '-de' (verb ending) across
   @614/@1171 (87-83, cf. 'cède') extended to @1334 (39-83):
   bar: name the host verbs with 83='-de' parsing all three windows,
   or kill the syllable fork; coordinate with queued frame-87-83-cede
   (owns the 'cède' fence).

## Lock note

locks/fence-911-de.lock created 2026-10-08T16:26:56Z, deleted on
completion. No stale lock encountered.
