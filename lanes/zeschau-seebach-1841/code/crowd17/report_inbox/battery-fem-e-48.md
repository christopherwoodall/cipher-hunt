# Battery verdict: fem-e-48 — 2026-10-09

Worker: f3243aa7-24f2-4800-9ac8-de76b2338c73. Stream: repaired 1,847-pair parse
(`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`,
parsed per `repair_parse.py`; 1,847 pairs, 96 types re-verified).
`canonical.py` never touched. R5005, sealed gates, red-team queue untouched.
Lock `locks/fem-e-48.lock` created on start.

## Bar (verbatim from queue)

"decide iff 48='e' serves as feminine/inflectional -e (32-48 x4, 19-48 x1 @1777) vs
word-final -e only ('me'/'ne' anchors), via the 40-vs-48 final-e distribution
('premiere' = ...-29-40 counterpoint)"

Restated as numbered clauses:
- C1: In the 32-48 x4 and 19-48 x1 windows, 48 is stem-attached (inflectional),
  not the final -e of a standalone closed word like the 'me'/'ne' anchors.
- C2: The 40-vs-48 final-e distribution absorbs the 'premiere' counterpoint:
  40 and 48 occupy a conditioned split, so 48's inflectional role is not
  redundant with 40. The rival "48 is word-final -e only" fails on the same
  distribution.
- C3: Every listed adverse answered (re-parsed cleanly, fenced with stated
  cause, or shown to be a misread — not ignored): verb-48 (A7-L2 tension),
  adj-19 (shares the 48 slot per A1 same-or-distinct note).

Offset convention: @-offsets below are 0-based pair indices of the **48**
token. The brief's "19-48 @1777" is byte-equivalent to my @1778-1779 (the
brief's numbering places 19 at 1777; mine places it at 1778 — same unique
bigram, verified on the repaired stream).

## Method

Full census of 48 (n=38) and 40 (n=21) on the repaired stream: predecessor /
successor bigram inventories, overlap analysis of the two cells' final-e
environments, window-level parses of all 5 inflectional-candidate windows and
all 3 overlap windows. Standing values used: 11=la, 70=pre, 82=m, 34=i,
29=er, 40=e, 46=que (GT pencil); 87=ce, 64=qui, 96=par, 17=fois, 79="tout"
(A5), 00="pour" (A9), 84="on" (A15), 47="ce" (A4); 59=est, 77="le"
(provisional); 48="e" (R17-003, letter tier); A1 predicative frames (32/37/42).
1841 diplomatic French throughout.

## Window-level evidence

### The 5 inflectional-candidate windows (byte-verified)

| @ (48) | window | reading under standing values |
|---|---|---|
| 450 | `61 59 32 48 79 17` (a2_09) | "est 32e toutefois" — copula frame, feminine parse (fem-32e: clean) |
| 856 | `64 32 48 84 02` (a5_07) | "qui 32e on…" — morphology "32e" intact; syntax fenced (fem-32e residual, not re-litigated) |
| 1177 | `74 32 48 59 37` (a6_10) | "32e est [le] ver" — nominalized feminine subject + copula (fem-32e: clean) |
| 1212 | `59 32 48 96 45` (a7_00) | "est 32e par [ce]…" — canonical feminine passive frame (fem-32e: strongest leg) |
| 1779 | `87 64 59 19 48 74` (a8_09) | "ce qui est 19e…" — single predicative leg (adj-19: intact) |

Exactly 4 "32 48" bigrams and exactly 1 "19 48" bigram stream-wide; zero
"48 32", zero "48 19". 48 never occurs as a standalone word in any of its
38 windows — the "word+'e'" rival needs a one-letter word "e", which is
unattested and ungrammatical in French at any period.

### The 40-vs-48 final-e distribution (byte-verified)

| cell | n | predecessor set |
|---|---|---|
| 40 | 21 | 29 x9, 78 x3, 88/97/96/74/50/03/48/61/56 x1 |
| 48 | 38 | 62 x6, 12 x5, 82 x4, 32 x4, 89 x3, 78 x2, 24 x2, 42/29/86/74/96/98/76/85/11/65/71/19 x1 |

Discriminating bigrams: 29-40 x9, 78-40 x3, 32-48 x4, 19-48 x1, 89-48 x3,
82-48 x4 ('me'), 12-48 x5 ('ne'). Cross-set: 32-40 = 0, 19-40 = 0, 89-40 = 0,
82-40 = 0, 12-40 = 0, 29-48 = 1 (@542), 78-48 = 2 (@365, @1399), 48-40 = 1
(@1399), 40-48 = 0.

Critical facts:
1. **The 'premiere' counterpoint is pencil-anchored inside 40's set.** The two
   crib hits "11 70 82 34 29 40" sit at 40=@759 and 40=@1039 — both inside the
   29-40 x9 set. So 40 is the -e after -er stems **by ground truth**, and
   "32e"/"19e" are never spelled with 40 (32-40 = 0, 19-40 = 0). The
   counterpoint does not falsify 48's inflectional role; it shows a conditioned
   split: -er stems take 40, the 32/19 frames take 48.
2. **78 splits between the two** (78-40 x3 vs 78-48 x2 @365/@1399) — 78's own
   conditioned behavior, fenced as 78's venue, not this target's bar.
3. **@542 ('12 44 29 48 42 06', row a3_01)** is the sole 29-48 window: 44's
   value is open and the window is unparseable under standing values. Noted
   as residual; one data point against an otherwise disjoint distribution.
4. **@1399 ('47 78 48 40 67 77', row a7_07)** = "ce vere e [67] le": 48-40 is
   strained under 48='e'/40='e' ("veree"). Fenced with the A7-L2 tension as
   red-team venue — it tensions the letter-'e' reading of 48 at that window
   only, not the 32-48/19-48 frames.

### Adverses

**(a) verb-48 (A7-L2 stem tension).** verb-48 NULL'd on the full 38-window
contact profile and escalated the A7-L2 frame narrowing to the red team. Its
exclusive legs are @1229/@1589 ('48 29 47', strained under 48='e'). The
32-48/19-48 frames are **not** among the exclusive legs, and nothing in
verb-48's findings forces 48≠'e' at those frames — verb-48 itself records
12/38 windows as word-final letter-'e' under the standing 48='e'. FENCED
with stated cause as red-team venue (A7-L2 narrowing); no effect on this bar.

**(b) adj-19 (shares the 48 slot per A1 same-or-distinct note).** adj-19 NULL'd
with its single leg "ce qui est 19e" intact — the 19-48 morphology stands under
R17-003. The A1 note is satisfied: 19 and 32 are **distinct** cells sharing
the inflectional -e slot (ordinary French agreement morphology), not competing
values for 48. ANSWERED.

**(c) @855 residual (from fem-32e).** Verbless "qui 32e" is syntactically
unparseable under standing values but morphologically "32e" is intact at all
4 windows — the residual is syntactic, not morphological, and does not touch
48's function. FENCED per fem-32e's stated cause; not re-litigated.

## Per-clause results

- **C1: PASS.** 48 in 32-48 x4 and 19-48 x1 is stem-attached: no boundary is
  byte-evidenced between the stem and 48, 48 never stands as a lone word,
  and the frames are copular/passive ("est 32e par", "est 19e") — canonical
  feminine-agreement slots. The 'me' (82-48 x4) and 'ne' (12-48 x5) anchors
  are whole words and do not exhaust 48's function.
- **C2: PASS.** The 40-vs-48 final-e distribution shows a conditioned split:
  40 is the -e after -er stems (29-40 x9, pencil-anchored by both "première"
  crib hits) and 78 (x3); 48 is the -e after 32/19/89 and the whole-word
  final -e of 'me'/'ne'. The 'premiere' counterpoint is absorbed: "première"
  uses 40 exactly because it is a 29-stem, which is why 40 and 48 are not
  redundant. The rival "word-final -e only" fails — under it, 32-48/19-48
  would need a standalone word "e", unattested in 38 windows.
- **C3: PASS.** verb-48 fenced to red team (A7-L2 venue); adj-19 answered via
  the A1 distinct-cells note; @855 residual fenced per fem-32e.

No window forces the claim false; no cleaner rival is demonstrated on these
frames.

## Verdict: PROMOTE (function-scoped)

48 serves as feminine/inflectional -e in the 32-48 x4 and 19-48 x1 frames.
Scope is explicit:
- This promotes 48's **function** at these frames only — on top of the
  R17-003 letter-tier grant (48='e'), unchanged.
- It does **not** name 32's or 19's values (adj-32 queued; adj-19's single leg
  stands but is unpromoted). It does **not** claim 48 is exclusively
  inflectional ('me'/'ne' anchors stand). It does **not** touch the A7-L2
  frame or its exclusive legs (red-team venue). No §7 polyvalence is
  declared — 48='e' is one letter with two ordinary orthographic functions
  (word-final letter of 'me'/'ne'; inflectional suffix), not two values.
- No standing verdict is contradicted or downgraded.

## Caveats for the red team (not contradictions)

1. Row a1_01's offset-1 re-segmentation (seg-a1_01, battery-promoted) sits in
   40's set: the 29-40 window @63 is in row a1_01. If the resegmentation is
   adopted, the 29-40 count changes by one — noted, not litigated here.
2. 78 takes -e as both 48 (x2) and 40 (x3) — 78's own conditioned behavior;
   flagged for 78's value battery.
3. @542 (sole 29-48) and @1399 (78-48-40, "veree"-strained) are recorded
   residuals; neither touches the 5 inflectional frames.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-fem-e-48.md` (this file).
- `battery-queue.json`: `fem-e-48` -> status `verdict`, result `promote`
  (temp-file + rename, own entry only; pre-write assert confirmed
  queued/verdictless; JSON re-validated post-write).
- Lock `locks/fem-e-48.lock`: deleted on completion.
- No standing verdict contradicted or downgraded. `canonical.py` never used.
  R5005, sealed gates, red-team queue untouched.
