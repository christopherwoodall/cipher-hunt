# Battery report: val-42-nominal — "42 takes ONE nominal class across the nominal frames"

Target: `val-42-nominal`. Claim: 42 takes ONE nominal class (noun/adjective)
across the nominal frames — direct discriminator against the verb-stem
reading. Date: 2026-10-08.
Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` +
`data/upstream-ct_R5005.txt`), parsed like `code/side-keyhunt/repair_parse.py`.
Never used `canonical.py`. R5005 untouched. No invented data.
@-offsets below are 1-based (lane convention).
Note: the dispatch brief's "est [42]" offsets (@464/@1187) are off by one;
the repaired stream gives @465/@1188 (re-derived below).

## Bar (verbatim, pre-registered)

"name ONE nominal class (noun/adjective) covering >=4 of these frames with <=1 fence"

Numbered clauses (fixed before testing):

1. Name ONE nominal class (noun or adjective) for 42.
2. The class covers >=4 of the listed frame-types ('42 ne' x3, 'est [42]' x2,
   29->42 x3, 76->42 x3) — covered = parses cleanly under the class, or
   fenced with stated cause (a fenced frame is addressed, not ignored).
3. At most 1 fence in total across the coverage.

## Method

Full census of 42 on the repaired stream: 42 n=20. All 11 nominal-frame
windows extracted with ±12 context and parsed under standing values
(banked: 11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que; granted: 87=ce,
64=qui, 96=par, 17=fois, 79=tout, 00=pour, 84=on, 47=ce; provisional:
59=est, 77=le; battery: 94=ne, 12=n, 48=e, 06=ent). Frame counts
re-derived from the stream (not copied from the brief): 42->94 x3,
59->42 x2, 29->42 x3, 76->42 x3 — all exact. The A1 predicative-frame grant
is used, not re-litigated (frame only, value open).

## Window-level evidence (@-offsets, 1-based)

**Type 1 — '42 ne' subject-slot x3 (42->94):**
- @494 (a2_11): `... 64 76 [42] 94 02 79 88 ...` = "qui(64) [76] [42] ne(94)
  [02] tout(79) ..." — 42 in subject slot before "ne [02]".
- @785 (a5_04): `... 11 24 [42] 94 74 65 84 ...` = "la(11) [24] [42] ne(94)
  [74] [65] on(84) ..." — 42 in subject slot before "ne [74]".
- @1795 (a8_09): `... 00 86 56 [42] 94 59 37 ...` = "pour(00) [86] [56]
  [42] ne(94) est(59) [37]" — "[56] [42] n'est [37]": 42 is the subject of
  "n'est [37]". Strongest leg: subjects are nominal.
All three parse cleanly with 42 as a noun. Dependency noted: 94='ne' is
battery-promoted pending red-team ratification; if revised, the
subject-slot inference weakens (position before 94 stands regardless).

**Type 2 — 'est [42]' predicative x2 (59->42):**
- @465 (a2_10): `... 79 87 11 59 [42] 96 00 33 ...` = "tout(79) cela(87-11)
  est(59) [42] par(96) pour(00) [33]" — predicative noun after "est".
- @1188 (a6_10): `... 06 59 [42] 06 84 59 46 ...` = "est(59) [42]ent on(84)
  est(59) que(46)" — predicative frame (A1 grant); the 06 contact is owned
  by the grant / fenced by battery-stem-42-verb (adjectival "-ent" or
  clause-boundary), not re-litigated here.
Both parse cleanly as predicative nominals. A1 frame grant respected.

**Type 3 — 29->42 x3: FENCED (the one fence, stated cause).**
- @80 (a1_02): `... 87 11 00 11 [29] [42] 98 ...` = "cela pour(00) la(11)
  er(29) [42] [98]".
- @220 (a2_01): `... 06 59 46 [29] [42] 16 ...` = "ent(06) est(59) que(46)
  er(29) [42] [16]".
- @1145 (a6_08): `... 78 62 16 [29] [42] 98 98 ...` = "[78] [62] [16]
  er(29) [42] [98] [98]".
Cause: segmentation rival. The word-boundary parse "[X]er [42-noun]"
fails: 29='er' word-final needs a stem, but 11='la' (@80) and 46='que'
(@220) cannot form "-er" words ("laer", "quer" are not French words), so
29 cannot be word-final there. The word-internal rival "er[42]" is live:
29 is word-internal elsewhere ("29-40" x9, as in "premiere"
70-82-34-29-40; "06-29" = "enter" @1815). @1145 ("[16] 29 42", 16 open)
admits "[16]er [42-noun]" only conditionally and cannot decide the
boundary. 42's wordhood is unproven at these 3 windows; they do not test
the nominal claim. One fence, one cause, covering the type.

**Type 4 — 76->42 x3:**
- @429 (a2_09): `... 62 48 76 [42] 63 ...` = "[62] e(48) [76] [42] [63]".
- @489 (a2_11): `... 19 64 76 [42] 41 ...` = "qui(64) [76] [42] [41]".
- @1618 (a8_03): `... 31 76 [42] 44 ...` = "[31] [76] [42] [44]".
"[76] [42]" is nominal contact under every open 76-value (determiner+noun,
verb+object, noun+noun); 76 takes determiners ('le [76]' x3 / 'la [76]' x1
per frame-76-tension), so 76 is a word and "76 42" is word+word. 42 stays
nominal regardless of 76's value. Clean at class level; 76's value open.

**Class choice:** NOUN. Type 1's bare subject slot selects noun over
adjective (adjectives need substantivization + determiner to head subject
position; noun needs no extra machinery). The adjective rival is fenced as
less economical, not killed.

**Supporting context (not bar frames):** "33 42" x2 (@267/@1504,
"[inf] [42]") is nominal-consistent (infinitive + noun object or
word-internal); "42 98" x3 (@80/@1073/@1145, once without 29) shows 42
taking a stable follower across left contexts — word behavior.

## Per-clause pass/fail

- Clause 1 (name ONE nominal class): PASS — NOUN.
- Clause 2 (cover >=4 of the 4 listed frame-types): PASS — 4/4
  (T1 clean x3, T2 clean x2, T3 fenced x3, T4 clean x3).
- Clause 3 (<=1 fence): PASS — exactly 1 fence (T3, one stated cause).

## Adverses

(a) "Does not re-litigate A1's predicative-frame grant (frame only, value
    open)": ANSWERED. T2 uses the granted frame; both 59->42 windows
    re-derived (@465, @1188); no clause touches the grant.
(b) Discriminator tension (not a listed adverse, recorded for the red
    team): battery-stem-42-verb (null, 2026-10-08) found genuine verb-class
    contact on the 42-06 UNIT at @206 ("[42]ent le [44]", transitive) and
    @544 ("[42]ent pour que", verb-governing complementizer). Nominal-42
    (promoted here) + verbal "42ent" (there) = a polyvalence question, and
    per §7 only the red team can declare a second polyvalence (67 et/veut
    is the sole true polyvalence). ESCALATED to the red team: either 42 is
    polyvalent (noun / verb-stem), or the @206/@544 "42-06" legs re-read as
    word-internal. This battery does not decide it; the discrimination
    stands — the simple verb-stem reading (no polyvalence) is now fenced
    on both sides.

## Verdict

**promote** — 42 takes the nominal class NOUN across the nominal frames.
All bar clauses pass; the A1 adverse is answered. No standing red-team
verdict on 42's value is contradicted (A1 granted the frame only; the
stem-42-verb battery nulled without promoting). The 42-06 verb legs are
flagged as the open polyvalence question for red-team adjudication (see
Adverses (b)).
