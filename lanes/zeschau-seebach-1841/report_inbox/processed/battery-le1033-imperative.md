# Battery report: le1033-imperative

Date: 2026-10-08. Worker: 5afd7192-bce3-4dcf-aa91-4ea8269a662a.
Stream: repaired 1,847-pair parse (`data/upstream-ct_R5005.txt` +
`code/side-keyhunt/repaired_offsets.json`, parsed per
`code/side-keyhunt/repair_parse.py`). `canonical.py` not used. R5005 not touched.

## Pre-registered bar (verbatim from battery-queue.json)

> resolve iff 80-imperative parses consistently with A8's infinitive frames
> (inflectional, not lexical, polyvalence) AND '87 01' left context parses;
> else confirm residual

Restated as numbered pass/fail clauses (written BEFORE testing):

1. **Clause 1:** the @1033 '80 77' = imperative + 'le' reading parses
   consistently with every A8 80-frame, i.e. 80 is ONE lexeme showing
   inflectional mood alternation (infinitive / finite / imperative), not two
   lexical homographs. FAIL if any 80-window forces the imperative reading
   false or forces a lexical split.
2. **Clause 2:** the '87 01' left context at the target window parses
   grammatically (the queue's adverse: "'87 01' = 'ce [01]' currently
   unparsed"). FAIL if no grammatical parse of '87 01' is found.

Indexing note: the claim's "@1033" is 1-based. 0-based: 80 @1032, 77 @1033,
row a6_03. All @-offsets below are 0-based unless marked 1-based.

## Method

1. Recomputed the repaired parse in-session (1,847 pairs, 96 distinct groups).
2. Enumerated all 17 occurrences of 80 with ±6 context; classified each by
   mood frame: "94-52-80" (ne-pas infinitive), "87-77-80" (proclitic finite),
   "80-77" (enclitic imperative), "29-80" (post-er), "79-80" (tout-verb),
   other.
3. Enumerated all 28 occurrences of 01; tested '87 01' / '47 01' parses
   ('ceci' vs 'ce faisant' vs standalone), with the lane-granted
   "cela" = "87-11" (battery-le-77) as the structural precedent.
4. Checked the sister verb 89 for an "89 77" imperative analog.

## Window-level evidence

Target window, 0-based @1026–1042 (row a6_03):

```
@1026 96=par @1027 43 @1028 87=ce @1029 01 @1030 03 @1031 29=er
@1032 80 @1033 77=le? @1034 11=la @1035 70=pre @1036 82=m @1037 34=i
@1038 29=er @1039 40=e @1040 17=fois @1041 77=le? @1042 82=m
```

i.e. `par [43] ce [01] [03]er [80] le? la pre m i er e fois le? [82]…`
= "par [43] ce [01] [03]er, [80]-le, la première fois. Le [82]…"

### Clause 1 evidence — 80's mood frames across all 17 windows

- **Infinitive:** "94-52-80-04" ×2 @1295, @1808 ("59 35 94 52 80 04 …"):
  "…[59] [35] ne pas [80] [04]…" — "ne pas" + infinitive is the one
  unambiguous infinitive frame in French. 80 is infinitive-capable. (This is
  the genuine infinitive leg; A8's "29-80" legs are "X-er | 80", i.e. 80
  follows an -er-final word with mood open — @1156 "92-29 80 17",
  @1322 "03-29 80 08", @1596 "03-29 80 67".)
- **Finite (proclitic):** "87-77-80-09" @515–518 ("88 56 87 77 80 09 70"):
  "ce le [80] [09]" — object clitic BEFORE the verb = finite mood.
- **Imperative (enclitic):** "80-77" ×2 — @720 ("00 66 86 01 02 21 80 77 03 91",
  row a5_01) and @1032 (target). Object clitic AFTER a verb-framed group is
  grammatical ONLY as imperative ("faites-le" order); proclitic-after would
  be ungrammatical for finite/infinitive. This is the queue's own evidence
  line ("imperative+'le' is the only grammatical '[verb] le' order") and it
  checks out.
- **Sister check:** "89 77" occurs 0 times — the enclitic shape is
  80-specific, consistent with the A8 verdict that 80 and 89 are DISTINCT
  verbs (no forced class-level alternation).
- **Remaining 80 windows** (@441, @469, @565, @663, @673, @768, @1011,
  @1090, @1662) are mood-open verb frames ("tout [80]", "[98] [80]",
  "[24] [80]"…); none forces a second lexeme, none contradicts the
  imperative reading.

Inflectional vs lexical: the three moods (ne-pas infinitive, ce-le finite,
[verb]-le imperative) are exactly the paradigm of ONE French verb lexeme.
A lexical split (two homographic verbs) is unmotivated: the imperative set
is n=2, far below any distributional split test, and parsimony favors one
lexeme. **On evidence, Clause 1 passes as inflectional, not lexical.**

**Authority cap (adverse, not evidence):** §7 reserves polyvalence
declarations to the red team ("67 et/veut is the sole true polyvalence";
worker brief: "an 80 inflectional polyvalence is a red-team declaration,
not yours"). The evidence supports single-lexeme mood alternation, but I
cannot resolve/declare it. Per §5.2 this is escalated, not declared.

### Clause 2 evidence — '87 01' left context

- "87 01" occurs ×2, both as the fixed 4-gram "96 43 87 01" = "par [43] ce
  [01]": @344 ("64 96 43 87 01 06 70 12 94", row a2_05) and @1028 (target).
- "47 01" (= ce-allophone + 01) occurs ×1 @195 ("87 98 56 47 01 21 60 08 67",
  row a1_08).
- **Primary parse — "ceci":** "87-01" = "ce"+"ci" = "ceci", exactly parallel
  to the lane-granted "cela" = "87-11" (battery-le-77, @832 "01 24 87 11 77"
  = "[01] en cela, le…"). Covers all three "ce"+"01" bigrams with one
  mechanism. Target clause then reads:
  "par [43], ceci [03]er, [80]-le, la première fois"
  ("by [43], this: to-[03], [80]-it the first time") — grammatical modulo
  open values 43/03.
- **Rival parse — "ce faisant":** 01 = "faisant" (fixed expression "ce
  faisant" = "in doing so"). Also grammatical at all three bigrams
  (@344: "par [43], ce faisant, [06] pre…" needs 06 verb-shaped — open,
  not contradicted).
- **Corroborating shape:** "01 24" ×3 (@40, @828, @984) fits "ci-[24]"
  compounds (ci-dessus / ci-après / ci-joint / ci-inclus / ci-contre) under
  "ci", or participle+object ("faisant [24]") under "faisant". Both live.
- **Fenced strain:** "37 01" ×3 (@940, @1634, @1818) needs nominal 37 for
  "[37]-ci" (37's nominal status ungranted; A1 grants predicative frames) —
  or a participle-absolute "[37] faisant" under the rival. Does not touch
  the bar's window but weakens "ci" to conditional.

Bar-literal, the target's left context parses (two grammatical frames,
zero contradictions in-window). **Clause 2 passes soft/conditional** on
01's open value.

## Per-clause verdicts

1. Clause 1 (80-imperative consistent with A8 frames, inflectional):
   **PASS on evidence** — all 17 windows fit single-lexeme mood alternation;
   no window forces the claim false or forces a lexical split.
   **CAPPED on authority** — declaring it is a red-team act per §7; not
   resolved here.
2. Clause 2 ('87 01' left context parses): **PASS (soft)** — "ceci"
   (primary, cela-precedent) / "ce faisant" (rival); "37-01" ×3 fenced as
   residual strain on the "ci" value.

## Adverse disposition

- §7 polyvalence rule (67 sole true polyvalence): NOT answered — it blocks
  worker-level declaration. **Escalated to the red team as the headline.**
- "'87 01' = 'ce [01]' currently unparsed": ANSWERED — re-parsed cleanly
  two ways ("ceci" / "ce faisant"), cause stated (01's value was the
  blocker; both frames now available, both conditional on open values).

## Verdict: NULL

Per §4/§5.2: the evidence is consistent with the claim on both clauses,
but the bar's "resolve iff" cannot be satisfied on worker authority —
resolving 80's inflectional polyvalence is a red-team declaration under
§7, and the worker brief explicitly withholds it. Marking null with the
authority contradiction as the headline; escalating to the red-team
adjudication queue (this report is the escalation vehicle — no red-team
queue files touched). No existing verdict downgraded (target was "queued").

77="le" remains provisional: the imperative reading inherits that
dependency (if 77 falls, "80-77" re-opens).

## Follow-up targets (nulls regenerate work)

1. **RT-adjudication: 80 inflectional mood alternation.** Red team to
   declare or reject 80 as a single lexeme across "ne pas 80" ×2 (@1295,
   @1808), "ce le 80" (@515), "80-le" ×2 (@720, @1032). Bar: formalize the
   proclitic/enclitic "le" alternation as the mood test; kill the single-
   lexeme hypothesis iff any 80-window forces two lexemes.
2. **01-value battery: "ci" vs "faisant".** Discriminate via "01 24" ×3
   (predict 24 ∈ {dessus, après, joint, inclus, contre} for "ci"; 24 nominal
   for "faisant") and "37 01" ×3 (37 must be nominal for "[37]-ci";
   participle-absolute "[37] faisant" for the rival). Bar: one value must
   parse ≥24/28 windows with zero hard contradictions; kill the loser.
3. **Grow 80's imperative set + close the @1032 clause.** Sweep for
   "[80] [other object clitics]" beyond 77 (imperative set currently n=2);
   resolve 03's value to complete "[03]er, [80]-le, la première fois";
   test @720 ("[21] [80]-le [03]") as the second imperative window. Bar:
   ≥1 new imperative-shaped 80 window or 03-value that keeps the clause
   grammatical; kill the imperative reading iff a new "80 77"-class window
   forces a non-imperative parse.
