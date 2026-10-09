# Battery noun-91-nondet-windows — verdict: NULL (naming claim fenced per bar)

Target: `noun-91-nondet-windows` (P3). Date: 2026-10-09.

## Bar (verbatim, pre-registered)

"name nominal-91 iff >=1 hostile window parses as DET-less noun with zero kill-grade contradictions, else fence nominal-91 at those loci"

Numbered clauses:
- C1 (name arm): >=1 of the two hostile windows (@520, @277) parses as DET-less noun with zero kill-grade contradictions → name nominal-91.
- C2 (fence arm): else fence nominal-91 at those loci.

Adverses: R19-164 grants 91 = past participle at the two 16-91 windows (@538/@1371); the noun claim must not contradict those loci.

## Method

Re-derived the repaired 1,847-pair / 96-type stream in-session from
`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`
(parsed like `repair_parse.py`; asserts held: 1,847 pairs, 96 types).
`canonical.py` never used. Full 91 census: n(91)=21. Both hostile bigrams
are hapaxes stream-wide ("70 91" ×1 @519; "84 91" ×1 @276).

## Findings

### @277 — `29 89 84 91 37 61 20` (row a2_03)

Byte-exact window (0-based): [271]06 [272]67 [273]33 [274]29 [275]89 [276]84
[277]91 [278]37 [279]61 [280]20 [281]61 [282]42 [283]48.

- 84="on" is granted (A15, promoted tier); 37 sits in the granted
  predicative frame (A1); 33+29 is the A10 hold; 89 is a verb-frame (A8).
- Natural parse: clause boundary after 89, then "on [91] [37-pred]" —
  subject pronoun "on" + finite verb/copula-shaped 91 + predicative.
- Nominal-91 is **kill-grade contradicted** here: French "on" is
  subject-only and must be followed by a finite verb; "on" + bare noun is
  ungrammatical in 1841 French, and no appositive/vocative/determiner-less
  object license exists with the predicative 37 following. No DET-less-noun
  parse survives.
- The window affirmatively favors **verb-shaped 91** (copula-like), not
  adjudicated here.

### @520 — `80 09 70 91 77 06 55` (row a3_00)

Byte-exact window (0-based): [514]56 [515]87 [516]77 [517]80 [518]09 [519]70
[520]91 [521]77 [522]06 [523]55 [524]81 [525]97 [526]47.

- 70="pre" is pencil ground truth — a **bound syllable**, immediately
  left-adjacent to 91 ("70 91" hapax, the only occurrence stream-wide).
- A standalone-noun 91 would require the word boundary "…09-pre | 91…"
  with the bound prefix attaching left to valueless 09, followed by a
  determiner-less noun in post-verbal position ("80-V [09-pre] [91-N]
  le…") — no grammatical 1841-French license for a bare noun there.
- The economical parse is "pre[91]" as one word: 91 word-internal
  (syllable/stem tier) completing a "pre-" word. That contradicts
  standalone word-level nominal-91 at this locus. (No value named for 91;
  "premier"-style readings stay conjectural.)

### Per-clause results

- C1 (name arm): **FAIL** — neither window parses as DET-less noun;
  @277 kill-grade contradicts nominal-91; @520's bound-prefix adjacency
  blocks standalone-word 91.
- C2 (fence arm): **FIRES** — nominal-91 is fenced at @277 and @520.

## Adverse answered

R19-164's grant (91 = past participle at the 16-91 windows @538/@1371) is
locus-scoped and untouched; this fence covers @277/@520 only. No standing
or red-team verdict contradicted or downgraded. §7 intact.

## Verdict: NULL

Naming claim fenced per bar (parent `noun-91-det-frames` precedent:
fence-arm firing on a naming battery = null). The fence is locus-only:
it says nothing about 91's class at the remaining 19 windows.

## Follow-ups proposed (all verified ABSENT from battery-queue.json)

1. `verb-91-277` (P3) — test 91 as finite verb/copula at @277
   ("on [91] [37-pred]"): name the verb value with zero new assumptions,
   or fence verb-91 at the locus.
2. `syllable-91-pre-word` (P3) — test "70 91" @519-520 as a "pre+X"
   word: state 91's syllable/stem role with byte evidence, or fence the
   word-internal arm (hapax; no second instance to corroborate).
3. `participle-91-extend` (P4) — test whether R19-164's past-participle
   91 extends beyond the two 16-91 windows; kill or bound the extension.

## Scope

Locus-level fence at @277/@520 only. Untouched: 91's class/value at the
other 19 windows, the 16-91 participle grant, 84="on", the A1
predicative frame, 70="pre".

## Bookkeeping

- Stream: repaired 1,847-pair parse re-derived in-session; asserts held.
- Queue: `noun-91-nondet-windows` → status `verdict`, result `null`,
  2026-10-09 (pre-write assert passed — was queued/verdictless;
  temp-file + rename; own entry only; no downgrade).
- Lock created on start (2026-10-09T15:33:56Z), deleted on completion.
- R5005, sealed gates, red-team adjudication queue untouched.
