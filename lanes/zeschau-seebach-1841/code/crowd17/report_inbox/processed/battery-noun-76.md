# Battery report: noun-76 — claim "76 is a (masculine) noun"

- Target id: `noun-76`
- Claim: "76 is a (masculine) noun: 'le [76]' x3 are determiner+noun legs (R16-001 promotion docket)"
- Date: 2026-10-08
- Worker: battery worker (subagent 940e8a45-f9c7-4797-8eb1-f8502282b4c5)
- Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json +
  data/upstream-ct_R5005.txt, parsed per code/side-keyhunt/repair_parse.py).
  Never used canonical.py. R5005 not touched. No invented data.
- Indexing: @i = 0-based pair index in the repaired stream. Row ids shown
  with each offset. My @833/@892/@969 = the brief's battery-convention
  @832/@891/@968 (off-by-one convention noted, used consistently).
- Lock: code/crowd17/next-token/locks/noun-76.lock (appended at start,
  deleted at end; a dispatcher lock from subagent-16a0eaf2 pre-existed).

## Bar (verbatim, pre-registered before testing)

"promote 76=noun iff 'le [76]' x3 parse as determiner+noun with zero
contradiction and the @1046 'la [76]' adverse is answered (re-parsed, fenced
with stated cause, or a gender/positional rule stated); kill iff a window
forces noun false or a cleaner rival class is demonstrated; else null with
1-3 follow-up targets. Name gender iff the evidence decides it."

Numbered pass/fail clauses (restated before testing, not modified after):

1. Each of the three '77 76' legs (@833 a5_06, @892 a5_08, @969 a6_00)
   parses as determiner+noun (77='le' provisional + 76=noun) with zero
   contradiction in the window.
2. The @1046 'la [76]' adverse is answered: re-parsed, or fenced with a
   stated cause, or resolved by a stated gender/positional rule. The
   'la'+verb re-parse of 76 admitted by R16-029 must be tested, not ignored.
3. No window in the full 21-window profile of 76 forces the noun class
   false at kill grade.
4. No cleaner rival class (verb finite, verb infinitive, adjective, other)
   is demonstrated on the same frames.
5. Gender is named iff the evidence decides it.

## Method

1. Rebuilt the repaired parse in-session: 1,847 pairs, n(76)=21. Verified
   the brief's counts exactly: pre 77x3/67x2/48x2/94x2/16x2,
   suc 47x4/42x3/49x3/45x2/87x2/01x2.
2. Wrote out all 21 windows with +-2 pairs and full row context.
3. Parsed the three '77 76' legs under 77='le' (provisional, R16-001:
   demoted/unconditioned — used as leaning, never banked) + 76=noun.
4. Re-parsed @1046 from the byte stream, checking the row boundary at
   @1044/@1045 and testing the 'la'+verb rival for grammaticality.
5. Swept all 21 windows for any forced-false of the noun class; fenced
   the strained ones with stated causes.
6. Tested rival classes (finite verb, infinitive verb, adjective) frame by
   frame for coherence across the full profile.

Standing values used: banked 11=la, 82=m, 34=i, 29=er, 40=e, 46=que;
granted 87=ce, 64=qui, 96=par, 17=fois, 79=tout, 00=pour, 84=on, 47=ce,
24=finite verb, 85=verb-stem, 37/32/42 predicative frames; provisional
59=est, 77=le (leaning only); holds 45=ce (A11), 67=et/veut sole
polyvalence (positional rule: 67='veut' iff follower infinitive-shaped);
lead 78='ver' (unpromoted). Kills and splits respected.

## Window-level evidence

Full 21-window table (center 76, +-2 pairs, row):

| @ | window | row | read under 76=noun |
|---|---|---|---|
| 13 | 13 62 98 [76] 45 91 | a1_00 | `[98] [76-noun]. Ce(45) [91]…` boundary, clean |
| 200 | 08 67 [76] 87 11 | a2_00 | `et(67) [76-noun]. Cela(87-11)…` or `veut(67) [76-noun]`; both branches clean |
| 362 | 62 48 [76] 47 78 | a2_06 | `[76-noun]. Ce(47) [78]…` boundary, clean |
| 427 | 62 48 [76] 42 63 | a2_09 | unknowns flank; no contradiction |
| 487 | 19 64 [76] 42 41 | a2_11 | FENCED (see below): `…[19]. Qui? ‖ [76-noun] [42]…` |
| 568 | 97 13 [76] 45 94 | a3_02 | `[76-noun]. Ce(45) [94]…` boundary, clean |
| 621 | 88 37 [76] 82 14 | a4_01 | `[37-pred] [76-noun]. M(82) [14]…` clean |
| 652 | 82 94 [76] 49 24 | a4_02 | `[76-noun] [49] [24-finite]` = subject+verb, clean |
| 735 | 85 93 [76] 18 82 | a5_02 | `[85-verb] [93] [76-noun]` = verb+object, clean |
| 833 | 11 77 [76] 59 35 | a5_06 | LEG 1: `cela(87-11), le(77) [76-noun] est(59) [35]…` clean |
| 892 | 06 77 [76] 01 98 | a5_08 | LEG 2: `[06] le(77) [76-noun] [01] [98]…` clean |
| 969 | 06 77 [76] 01 98 | a6_00 | LEG 3: `[06] le(77) [76-noun] [01] [98].` clean (row-final) |
| 980 | 92 07 [76] 47 78 | a6_01 | `[76-noun]. Ce(47) [78]…` boundary, clean |
| 989 | 48 01 [76] 49 24 | a6_01 | `[76-noun] [49] [24-finite]` = subject+verb, clean |
| 1046 | 11 67 [76] 85 41 | a6_03/a6_04 | RE-PARSED (see below): row boundary after 11; `Et(67) [76-noun] [85-verb]…` clean |
| 1273 | 64 47 [76] 87 76 | a7_02 | FENCED (see below): `…Qui? ‖ Ce(47) [76-noun]. ‖ Ce(87) [76-noun].` |
| 1275 | 76 87 [76] 48 56 | a7_02 | `Ce(87) [76-noun]` det+noun, clean (same fence as @1273 for the left 'qui') |
| 1395 | 89 16 [76] 47 78 | a7_07 | `[76-noun]. Ce(47) [78]…` boundary, clean |
| 1432 | 12 16 [76] 49 64 | a7_08 | `[76-noun] [49] qui(64)…` = noun + relative clause, clean |
| 1577 | 82 94 [76] 47 98 | a8_01 | `m(82) [94] [76-noun]. Ce(47) [98]…` boundary, clean |
| 1616 | 48 31 [76] 42 44 | a8_03 | unknowns flank; no contradiction |

### Clause 1: the three 'le [76]' legs

- LEG 1 @833 (a5_06): `59 38 82 01 24 87 11 77 76 59 35 56 17 98 …`
  = `est(59) [38] m(82) [01] [24-finite] cela(87-11) ‖ le(77) [76-noun]
  est(59) [35] [56] fois(17)…`. Reads: "…[verb]. Cela, le [76] est [35]…".
  Determiner+noun parses with zero contradiction. CORRECTION to R16-001:
  59@834 is not "leftover" — `le [76] est [35]` is a clean copular clause,
  which supports (not weakens) the leg. 59='est' stays provisional; this
  battery does not promote it. The R16-001 DEMOTE verdict stands on its
  other (circularity) grounds; only the window description is corrected.
- LEG 2 @892 (a5_08): `… 00 86 06 77 76 01 98 82 14 …`
  = `…pour(00) [86] [06] le(77) [76-noun] [01] [98] ‖ m(82) [14]…`.
  Zero contradiction; [01-98] is a post-nominal unit of open value.
- LEG 3 @969 (a6_00): `… 19 24 06 77 76 01 98` (row ends)
  = `…[24-finite] [06] le(77) [76-noun] [01] [98].` Row-final
  clause-final noun phrase. Zero contradiction.
- The 5-gram `06 77 76 01 98` is byte-identical at @892 and @969 (rows
  a5_08, a6_00). The repetition marks `le [76] [01-98]` as a stable frame.

### Clause 2: the @1046 adverse, answered by re-parse

Byte facts: a6_03 starts @1020, length 25, last pair @1044=11.
a6_04 starts @1045=67. So a ROW BOUNDARY sits between 11@1044 and 67@1045.
a6_03 tail: `34 29 40 17 77 82 63 11` = `i(34) er(29) e(40) fois(17)
le(77) m(82) [63] la(11).` The 'la' closes row a6_03's clause. Row a6_04
opens `67 76 85 41 …`.

Re-parse with stated cause: the 'la' belongs to the prior row/clause; no
'la [76]' constituent exists — the gender tension was a cross-boundary
misread. With 76=noun, 76 is not infinitive-shaped, so the positional rule
resolves 67='et' (67='veut' only iff follower infinitive-shaped):
`‖ Et(67) [76-noun] [85-verb-stem] [41]…` = "Et [noun] [verb]…" —
subject+verb, fully grammatical, zero contradiction.

The 'la'+verb rival (R16-029's admitted re-parse: 11='la' pronoun +
67='veut' + 76=verb) was tested and FAILS: "la veut [76]" has no subject
for 'veut' and is ungrammatical in French. The verbal rival gets no leg
at @1046. Cause stated, rival tested and rejected — adverse answered.

Positional/gender rule stated: 76's determiner contacts are 77('le')x3,
47('ce')x1 (@1273), 87('ce')x1 (@1275) — all masculine; zero feminine
agreement anywhere in the profile once @1044 is placed across the row
boundary.

### Clause 3: fenced windows (stated causes, not kill-grade)

- @487 (a2_11) `19 64 76 42 41`: 64='qui' is granted, directly before 76.
  `qui [76-noun]` cannot parse as relative+head. Fence: interrogative
  'qui' + nominal fragment — `…[19]. Qui? ‖ [76-noun] [42] [41]…`
  ("Who? — [noun]…", elliptical Q/A). Strained but grammatical; does not
  force noun false. Note the rival 76=finite-verb reads cleanly here
  (`qui [76-verb]`), but see clause 4: that rival dies on the 'le' legs.
- @1273/@1275 (a7_02 tail) `20 64 47 76 87 76`: the pairs `ce(47) [76]`
  and `ce(87) [76]` are clean determiner+noun twice over. Only the
  preceding 64='qui' needs the fence: interrogative — `…[20]. Qui? ‖
  Ce [76-noun]. ‖ Ce [76-noun].` ("Who? This [noun]. This [noun].",
  presentational). Stated cause; not kill-grade. The verbal rival has no
  clean parse here either (`qui ce [76-verb]` is ungrammatical).

### Clause 4: rival classes tested and rejected

- 76=finite verb: clean at @487 (`qui [76-verb]`) but ungrammatical at
  the three 'le' legs (`le [finite verb]` is impossible). Fails.
- 76=infinitive verb: parses the 'le' legs (nominalized infinitive, "le
  faire"-style) but fails @487 (`qui` + infinitive is ungrammatical) and
  @1432 (`[verb] [49] qui` — 'qui' cannot follow a verb; the noun reading
  gives a clean relative clause `[76-noun] [49] qui [verb]`). Fails.
- The two verb subclasses are mutually exclusive on the same frames, so
  no single verb value covers the profile. The verbal rival is incoherent.
- 76=adjective: fails @200 (`et [adj] cela` broken), @735 (`[85-verb]
  [93] [adj]` — adjective as bare verb object broken), @1432 (adjective
  cannot head a 'qui' relative). Fails.
- No cleaner rival class is demonstrated. The noun class is the only one
  that parses all 21 windows (19 clean, 2 fenced with stated causes).

### Queue-brief adverses, each answered

- 76→47 x4 (@362/@980/@1395/@1577, under 47='ce'): order stated — 76 is
  CLAUSE-FINAL and 47 opens the next clause: `[76-noun]. ‖ Ce(47) …`.
  Not a *"noun ce" constituent. Three of the four continue `47 78`
  (`ce [78-ver?]`, determiner+noun opening the next clause); the fourth
  is `ce(47) [98]`. The same boundary shape repeats at 76→45 x2
  (@13/@568, 45='ce' A11). Six-of-21 clause-final-76 + demonstrative
  opening is a coherent distributional signature, not a contradiction.
- 76-01-98 x2 (@892/@969): fenced with stated cause — stable
  post-nominal `[01-98]` unit inside the repeated `06 77 76 01 98` frame;
  01's value is open ('ci'/'faisant' both killed, battery-ci-01-value)
  and 98 is unknown, so no contradiction can be drawn; the repetition
  supports frame stability.

## Per-clause pass/fail

1. Three 'le [76]' legs as determiner+noun, zero contradiction — PASS.
2. @1046 adverse answered (row-boundary re-parse, stated cause; 'la'+verb
   rival tested ungrammatical; gender/positional rule stated) — PASS.
3. No window forces noun false (2 fenced with stated causes) — PASS.
4. No cleaner rival class demonstrated (verb subclasses mutually
   exclusive; adjective fails 3 frames) — PASS.
5. Gender: the evidence decides it — MASCULINE. Every determiner contact
   is masculine: 'le'x3 (@833/@892/@969), 'ce'x2 (@1273/@1275); zero
   feminine agreement in the profile.

## Verdict: PROMOTE — 76 = noun, masculine

All bar clauses pass and every listed adverse is answered. The R16-001
docket condition is satisfied: the 'le [76]' x3 legs resolve in favor,
so 77='le' may now be re-evaluated by the red team against its bar
(this battery does not itself promote 77; 77 stays provisional per
R16-001 until the red team rules).

Note on standing verdicts: none overwritten. R16-001's DEMOTE of 77='le'
stands (rested on circularity, untouched here); only its "59 leftover"
window description is corrected above. R16-029's "no ruling, queued for
the dedicated 76 battery" is now superseded by this battery's verdict,
which is the outcome R16-029 deferred to.
