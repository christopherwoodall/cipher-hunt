# Battery report: adj-32

Target: `adj-32` — claim "32 predicative adjective".
Worker: worker-adj-32-f09a85d7. Date: 2026-10-08.
Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` +
`data/upstream-ct_R5005.txt`, parsed like `code/side-keyhunt/repair_parse.py`).
canonical.py never used. R5005, sealed gates, red-team adjudication queue untouched.
No data invented. @-offsets are 0-based stream indices of the 32 cell.
(A1's battery indexed the 59 cell, so its @316/@448/@1210 = my @317/@449/@1211 —
same three windows, verified.)
Lock: `code/crowd17/next-token/locks/adj-32.lock` created 2026-10-08T08:50:42Z;
no prior lockfile (no stale-lock note needed).

## Bar (verbatim, pre-registered from battery-queue.json, BEFORE testing)

"promote iff est-frames hold + 94/48 followers resolve + verb-tension adjudicated"

Numbered pass/fail clauses:

1. The est-frames hold: the three 59->32 windows parse as predicative-adjective
   frames on the repaired stream.
2. The 94/48 followers in those frames resolve: @317's 94 via the ne/expletif
   frame; @449's and @1210/@1211's 48 resolved.
3. The verb-tension is adjudicated: the two 'qui 32' windows without 'est'
   (@33, @855) re-parse cleanly, fence with stated cause, or are shown to be
   misreads.

## Method

1. Re-parsed the repaired stream from `repaired_offsets.json` +
   `data/upstream-ct_R5005.txt` with the repair_parse.py tokenizer (byte-exact
   upstream tokenization, a5_03 offset 0). Verified 1,847 pairs.
2. Census: all 13 occurrences of 32; all 59->32 bigrams; all 64->32 bigrams;
   full predecessor/successor contact profiles for 32, 94, 48, 06.
3. Parsed each 32 window ±8 with banked pencil GT (11=la, 70=pre, 82=m, 34=i,
   29=er, 40=e, 46=que), granted values (87=ce, 64=qui, 96=par, 17=fois,
   79=tout, 00=pour, 84=on, 47=ce), provisional (59=est, 77=le), battery-level
   94=ne and 12/48 letters (pending ratification — used, not re-litigated).
4. Tested each bar clause against the windows. No red-team verdict contradicted:
   A1's predicative-FRAME grant for 32 is upheld (frame, not value).

## Window-level evidence

32 census (n=13): @33, @130, @248, @257, @317, @449, @532, @855, @1176, @1211,
@1283, @1417, @1572.
Predecessors: 59x3, 64x2, 26x2, 91x2, 56x2, 74x1, 52x1.
Followers: 48x4, 94x1, 96x1, 01x1, 44x1, 43x1, 16x1, 98x1, 84x1, 28x1.

### Clause 1 — the three est-frames (59->32 x3, re-derived; A1's count holds)

- **@317** `[314]45 [315]64 [316]59 [317]32 [318]94 [319]06 [320]11` =
  "…ce(45) qui(64) est(59) 32 ne(94) [06] la(11) [92]…".
  Full: "20 17 46 84 24 37 78 45 64 59 32 94 06 11 92 60 15 63 71" =
  "[20] fois(17) que(46) on(84) en(24) [37] [78] ce(45) qui(64) est(59) 32
  ne(94) [06] la(11) [92]…". Predicative slot intact; 32 adjective-compatible.
- **@449** `[447]61 [448]59 [449]32 [450]48 [451]79 [452]17` =
  "…[61] est(59) 32 e(48) tout(79) fois(17) le(77) [60]…".
  "est [32]e toutefois" — 48 left-attaches (right-attach "e-tout"/"e-par"/"e-on"
  fails at every 32-48 window stream-wide), giving a feminine -e on 32:
  "est [adj-fém]e, toutefois, le [60]…" — grammatical.
- **@1211** `[1209]64 [1210]59 [1211]32 [1212]48 [1213]96 [1214]45` =
  "…qui(64) est(59) 32 e(48) par(96) ce(45) [36] le(77)…".
  "est [32]e. Par ce [36], le [83]…" — feminine -e on 32, clause boundary
  before "par ce" — grammatical.
- Clause-1 verdict: PASS. 59->32 x3 re-derived exactly (no phantom legs, none
  missing); all three windows adjective-compatible at the 32 slot. Consistent
  with the standing A1 frame grant (not a re-litigation of it).

### Clause 2 — the 94/48 followers

- **@449's 48 and @1211's 48: RESOLVE.** Both read as feminine/inflectional -e
  on 32 (48='e' letter, battery-promoted; word-final in all anchors
  'me'=82-48, 'ne'=12-48). "est [adj]e toutefois" / "est [adj]e. Par ce [36]…"
  parse cleanly. Caveat fenced: 'premiere' spells final -e as 40
  (70-82-34-29-40), so the 40-vs-48 distribution for inflectional -e is
  unresolved — the parse is grammatical, the spelling distribution is open
  (see follow-up 3).
- **@317's 94: DOES NOT RESOLVE — FENCED.** "est [32] ne(94) [06] la(11) [92]":
  - 94-06 is a hapax (only 1 of 37 94-followers; 94's established followers
    are 82x4 'm', 74x3, 59x3 'n'est', 52x3…).
  - Bare-ne literary reading needs 06 finite (savoir/pouvoir/oser/cesser
    class): 06 is not finite-verb-shaped (followers 77x6 'le', 00x4 'pour',
    11x4 'la', 29x4 'er'; predecessors 82x4 'm', 30x4 'pas') — FAIL.
  - Expletive-ne reading needs a subordinator or comparative: none present —
    FAIL. (No expletive-ne frame is established anywhere in lane docs; the
    adverse's "ne/expletif frame" is an untested finder hypothesis.)
  - "n'" elision + vowel-initial 06 ('ent…'): possible in principle (the
    cipher marks elision: 'm''=82-48 x4), but 06's value is open (ent-06
    queued: verb-ending vs '-ment' adverb fork) — cannot be demonstrated now.
  - Fenced with cause to follow-up 2 (gated on ent-06), not ignored.
- Clause-2 verdict: FAIL (as a pass/fail clause). The 48s resolve; the 94
  does not. The bar demands all followers resolve.

### Clause 3 — the verb-tension ('qui 32' x2, no 'est')

- **@33** `[32]64 [33]32 [34]01` = "…pas(30) [03] qui(64) 32 [01] [08] [91]
  a(39) qui(64) [41]…". "qui 32" with 64=qui (granted): 32 sits in the finite-
  verb slot. No non-verb parse survives: *"qui [adj]", *"qui [noun]" (verbless
  relative); 32-01 as one word ("[X]ci"/"[X]faisant", 01's queued fork) still
  leaves the relative verbless. 32 is verb-shaped here.
- **@855** `[854]64 [855]32 [856]48 [857]84` = "…[51] qui(64) 32 e(48) on(84)
  [02] en(24) [49]…". "qui [32]e, on [02] en [49]…" — 32-48 reads as verb stem
  + 3sg '-e' inflection ("qui [verbe], on…"), the only grammatical parse
  (64=qui and 84=on both granted unconditioned; 48 cannot right-attach).
  32 is verb-shaped here.
- Adjudication: neither window re-parses as adjectival; neither is a misread
  (grants hold). FENCED with stated cause: 32 shows verb-shaped behavior at
  @33/@855 vs adjective/participle-shaped behavior in the predicative frames —
  a dual-behavior question that needs red-team polyvalence adjudication (§7:
  67 et/veut is the sole true polyvalence; batteries do not declare a second).
  Cf. the imp-80-set precedent (inflectional-alternation evidence gathered
  for red team, not declared at battery level).
- Clause-3 verdict: FENCED, not cleanly adjudicated. The bar's "adjudicated"
  is not met at pass grade.

### Supporting / neutral windows (not bar clauses, recorded)

- @130 "la(11) [02] [26] 32 par(96)": "[noun] [adj] par" slot — adjective-
  compatible (soft agreement tension: 26 feminine-noun lead vs bare 32).
- @532 "[26] 32 [16]": same "[noun] [adj]" shape — adjective-compatible.
- @1176 "[74] 32 e(48) est(59) [37]": "[74] [32]e, est [37]" — consistent with
  the feminine -e reading; 74 open.
- @248/@257 "[91] 32 [44]/[43]": adjective-compatible, values open.
- @1283/@1572 "[56] 32 [98]/[28]": neutral, values open.
- @1417 "[52] 32 on(84) tout(79)": "[52] [32], on tout…" — clause boundary
  parse available; neutral.

## Per-clause pass/fail

1. est-frames hold: **PASS** (59->32 x3 re-derived; A1 frame grant upheld).
2. 94/48 followers resolve: **FAIL** (48s resolve as feminine -e; @317's 94
   fenced — "ne [06]" hapax, no clean ne/expletif parse, 06 open).
3. verb-tension adjudicated: **FENCED, not passed** (@33/@855 force verb-shaped
   32; dual behavior escalated — needs red-team polyvalence adjudication).

## Adverses (from queue; answered, none ignored)

1. "'qui 32' x2 verb-position tension (no 'est')": CONFIRMED as stated —
   @33 and @855 require verb-shaped 32; fenced with cause (see clause 3),
   not ignored.
2. "94/48 post-predicate slot needs the ne/expletif frame": 48s resolved
   (feminine -e); the 94's ne/expletif frame NOT demonstrated — fenced with
   cause (see clause 2), not ignored.

## Verdict: NULL

The predicative frames hold and the 48-followers resolve as feminine -e, but
the bar's clause 2 fails (@317's "ne [06]" has no clean parse — hapax bigram,
06's class open) and clause 3 cannot be adjudicated at battery level (two
windows force verb-shaped 32; declaring the needed polyvalence is a red-team
act per §7). Not promote (clauses 2–3 unmet). Not kill (no est-frame window
forces a non-adjective 32; the verb rival is not demonstrated on the
predicative frames). No standing red-team verdict contradicted — A1's frame
grant is upheld and re-derived; 94=ne / 48=e battery promotions are used, not
re-litigated.

## Follow-up targets (null regenerates work)

1. **verb-32** — "32 verb-stem battery". Narrower bar: resolve iff all 13
   windows parse under ONE verb lexeme (finite "qui 32" @33 / "qui [32]e on"
   @855; participle "est [32](e)" @317/@449/@1211; "[noun] [32]" @130/@532 as
   participle-modifier or fenced) with the @317 "ne 06" fenced or resolved;
   else state the polyvalence question for the red team with per-window
   parses. (Owns the fenced verb-tension; does not re-litigate A1's frame
   grant.)
2. **ne-06-317-gate** — "resolve @317's '94 06' hapax once ent-06 names 06".
   Gated on ent-06 (do not force). Discriminates: bare-ne + finite 06 vs
   elided "n'[06]" vs adverb-06 readings. Input bar for any future 32-value
   promotion (clause 2 of this battery).
3. **fem-e-48** — "48 as inflectional -e". Bar: decide iff 48='e' serves as
   feminine/inflectional -e (32-48 x4, 19-48 x1 @1777) vs word-final -e only
   ('me'/'ne' anchors), via the 40-vs-48 final-e distribution ('premiere' =
   …-29-40 counterpoint). Coordinate with queued verb-48 and adj-19 (shares
   the 48 slot per A1 same-or-distinct note).

## Caveats carried forward

- Conditional throughout on provisional 59='est' and battery-level (pending
  ratification) 94='ne', 48='e', 30='pas'.
- 40/48 final-'e' spelling distribution unresolved (affects follow-up 3).
- @130/@532 adjective-after-noun slots carry a soft agreement tension (26's
  feminine-noun lead vs bare 32) — values open, not verdict-grade.
- Canonicality caveat (§7) stands.
