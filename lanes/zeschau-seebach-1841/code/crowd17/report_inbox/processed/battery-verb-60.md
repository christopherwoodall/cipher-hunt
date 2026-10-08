# Battery report: verb-60 (one verbal value for 60's six verbal windows)

Worker: verb-60-worker subagent (session 7bab5e08-6190-45de-a211-f3088d1).
Date: 2026-10-08.
Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json +
data/upstream-ct_R5005.txt), parsed per code/side-keyhunt/repair_parse.py.
canonical.py never used. R5005 never touched. @i = 0-based pair index.
Lock: locks/verb-60.lock created at start, no prior lock (no stale lock to note).
No red-team verdict on 60 exists — no contradiction, no escalation.

## Bar (verbatim, pre-registered before testing)

"resolve iff one verbal value (or stated positional rule) covers all six windows (@1338 'qui 60 08', @700 'ne 60 12', @995 '03 60 67', @1474 '53 60 06', @1563 '06 60 71', @1735 '06 60 12'); if the NP-frame adjective reading also holds, frame the polyvalence question for red-team declaration per §7 (67 sole true polyvalence)"

Numbered clauses (fixed before data examination):

1. (C1) One verbal VALUE is named (a specific verb or stem) such that 60
   takes that value in all six windows, with stated syllable boundaries,
   using only banked/granted/promoted values.
2. (C2, alternative) A positional rule is stated that determines 60's
   verbal value in each of the six windows (a rule that only labels
   windows "verbal" without assigning the value does not count).
3. (C3) All six windows parse grammatically under C1 (or C2), with
   @-offsets cited; open neighbors fenced with stated cause.
4. (C4, kill-check) No window forces 60 non-verbal, and no cleaner
   non-verbal rival covers the six windows.
5. (C5, conditional) If the NP-frame adjective reading also holds, the
   polyvalence question is framed for red-team declaration per §7
   (declared by the red team only, never at battery level).

## Method

Fresh parse per protocol. No prior counts trusted. Standing values used:
banked 11=la, 29=er, 46=que, 70=pre, 82=m; granted 64=qui, 96=par, 47=ce
(A4); provisional 77=le, 59=est; battery-promoted 94=ne, 12=n (letter),
48=e (letter), 06=ent (verb ending), 30=pas, 67 positional rule (67=veut
iff follower infinitive-shaped; else 67=et). Coordination: adj-60
(adjective arm) already at verdict kill 2026-10-08 — its NP-frame bar is
not duplicated here; its queued follow-ups (poly-60-redteam pri 1,
adj-frames-995-637 pri 2, participle-60 pri 2) are not duplicated either.

## Window-level evidence

V1 — @1338 'qui 60 08' (row a7_05):
@1335 86 @1336 71 @1337 64 @1338 60 @1339 08 @1340 65 @1341 64 @1342 52
Reads: "...[86-inf] [71] qui[64] [60] [08] [65] qui[64] [52]..."
64='qui' is red-team granted. A subject relative 'qui' must be followed
by a finite verb. 60 is forced verbal here (noun-60 K1, adj-60 K1 — both
kill-grade, re-derived and confirmed). The clitic rescue ("qui se [08]")
fails: 08 precedes finite verbs x3 ('08 31' x3 per stem-08 evidence), so
08 is not verb-shaped and cannot be the verb of a "qui se [V]" frame.
Value unnamed: 08 is open (stem-08 queued). Note: the '60 08' bigram
recurs once outside the six, @197 ('21 60 08 67') — same verb+08 frame,
consistent with one verb but the value stays unnamed.

V2 — @700 'ne 60 12' (row a5_01):
@698 28 @699 94 @700 60 @701 12 @702 98 @703 20
Reads: "...[28] ne[94] [60] n[12] [98]..."
94='ne' battery-promoted; 12='n' letter battery-promoted. 'ne' must be
followed by a verb: "ne [60]n [98]" with 60 a verb stem and 12='n' its
final letter (noun-60 K2, re-derived and confirmed). Value unnamed: 98
is open (n=40, profile mixed). "64-60" and "94-60" each occur exactly
once on the stream (@1337-1338, @699-700) — both verb-forcing frames
are hapax.

V3 — @995 '03 60 67' (row a6_01):
@993 30 @994 03 @995 60 @996 67 @997 11 @998 96 @999 82 @1000 33
Reads: "[30] [03] [60] et[67] la[11] par[96] m[82] [33]..."
67='et': follower @997=11='la' (banked) is not infinitive-shaped, so the
positional rule gives 'et'. Two live parses. Verbal: "[03-N] [60-V] et"
(03 noun-supported: 'le [03]' @722, 'ce [03]' x2 @1014/@1790 via granted
47='ce'). Adjectival: "[03-N] [60-adj] et" — postnominal adjective, the
normal French position (adj-60 battery notes this window SUPPORTS the
adjective arm, outside its bar). The right context "et la par me [33]"
is murky under both readings — fenced as residual, not kill-grade (it
does not force 60 non-verbal; the verbal left edge "[03] [60]" stays
available). V3 is verb-COMPATIBLE but not verb-forcing; it is the only
one of the six that is class-ambiguous.

V4 — @1474 '53 60 06' (row a7_10):
@1472 41 @1473 53 @1474 60 @1475 06 @1476 67 @1477 33 @1478 29
Reads: "[41] [53] [60] ent[06] [67] [33] [29]..."
06='ent' is battery-promoted as a verb ending. "60 06" = stem-60 +
'ent' ending: one verb word "[60]ent". 60 is forced to verb-STEM status
here (conditional on the ent-06 promotion). 67='veut' by the positional
rule: follower @1477=33, and "67-33" has x6 precedent on the stream
(@272/@1148/@1423/@1450/@1476/@1623) including the "67-33-29" x3
byte-identical stem frames ("veut [X]er", per dire-33-set) — @1477-1478
is itself "33 29" = "[X]er" infinitive. So the right edge is the clean
modal "veut [X]er". Fenced: the "[53] [60ent] veut [inf]" adjacency puts
two finite shapes side by side; it needs a clause boundary (53's value
is open — prof-53 null 2026-10-08) or a 53 re-parse. This fences the
clause, not 60's verb-hood. Value unnamed.

V5 — @1563 '06 60 71' (row a8_01):
@1560 26 @1561 30 @1562 06 @1563 60 @1564 71 @1565 50
Reads: "[26] [30] ent[06] [60] [71] [50]..."
06='ent' PRECEDES 60 here. Backward attachment ("[30]ent") is blocked:
30='pas' is battery-promoted, and pas-30's own battery parsed @1561 as
"la 26 pas 06 60" (pas-word, then "06 60" — forward attachment). So 06
attaches forward: "ent[60]" is word-initial, 60 the second syllable of
an ent-prefixed verb. Verb-compatible; value unnamed (71 open, n=7).
Note: the '60 71' bigram recurs once outside the six, @232
('21 60 71') — that instance is the vient-parvenir formula third, owned
by queued frame-vient-parvenir, not touched here.

V6 — @1735 '06 60 12' (row a8_07):
@1733 30 @1734 06 @1735 60 @1736 12 @1737 48 @1738 52
Reads: "[30] ent[06] [60] n[12] e[48] [52]..."
Same geometry as V5: 06 forward-attaches ("pas 06 60" per pas-30's
@1733 parse), so "ent[60]" is word-initial. Then "n[12] e[48]": either
one word "ent[60]ne", or "ent[60]" + "ne"(12+48 = the 'ne' word, per
n-e-12-48: "'ne'=12-48 x7") — but "ne" AFTER a verb is ungrammatical
word order, so the one-word "ent[60]ne" parse is preferred. The one
nameable candidate, 60='on' ("entonne", cf. "entonner"), is EXCLUDED on
two independent grounds: (a) it collides with granted 84='on' (A15,
§7); (b) it fails V2 ("ne onn [98]" is not a verb). Value unnamed.

## The structural finding

V1–V4 show 60 BARE (finite verb after 'qui'/'ne'/subject-NP, or stem +
'ent' suffix in V4). V5–V6 show 60 with an "ent-" PREFIX ("06 60").
No single French verb has both "[X]ent" and "ent[X]" forms for the same
monosyllabic X ([X]ent: "mentent", "vendent", "tendent", "rendent";
ent[X]: "entre", "entend", "entonne" — the X sets never coincide for one
verb). The full "ent[60]ent" trigram (06-60-06) occurs x0 on the
stream. Therefore one verbal value cannot cover all six windows: at
minimum TWO distinct verbal items share the syllable 60 (a bare-60 verb
for V1–V4 and an ent-60 verb for V5–V6), or 60 is polyvalent. A split
(two items) is not polyvalence (one item, two values): no red-team
declaration is needed to TEST the split, per the lane's split
precedents (20~17, 23~26).

## Per-clause pass/fail

- C1: FAIL. No verbal value is nameable across the six. V1/V2/V4 force
  60 verbal but leave the value open (08/98/53 open); V5/V6 force an
  ent-prefixed verb with 60 as second syllable, value unnamed; the only
  nameable candidate (60='on', "entonne") is excluded twice over.
- C2: FAIL. No positional rule determines the VALUE. A distributional
  rule ("60 verbal iff successor in {08,12,67,06,71}") merely restates
  the six windows; and the bare-60 vs ent-60 shape split means no one
  rule yields one value.
- C3: FAIL (consequence of C1/C2). Windows parsed as far as the values
  allow: V1/V2/V4 verb-forced, V3 class-ambiguous with right context
  fenced, V5/V6 verb-compatible with values unnamed.
- C4: PASS. No window forces 60 non-verbal (V1/V2/V4 force verbal;
  V3/V5/V6 are verb-compatible). No cleaner non-verbal rival covers the
  six: the noun claim was killed (noun-60, 2026-10-08) and the adjective
  single-value claim was killed (adj-60, 2026-10-08).
- C5: CONDITIONAL — the NP-frame adjective reading does NOT hold as a
  single-value claim (adj-60 killed), so this clause's antecedent is
  false. Note: adj-60's C1–C3 passed (the adjective coheres on the NP
  frames @454/@690/@1644/@1674), and adj-60 already queued
  poly-60-redteam (pri 1) for the adjective-vs-verb question. The
  polyvalence question is therefore already before the red team; this
  battery adds that the VERBAL side itself splits into two shapes, which
  poly-60-redteam should take into account. No new escalation from this
  battery (no standing red-team verdict is contradicted).

## Verdict

**null** — the six windows do not cohere under one nameable verbal
value (C1/C2 fail), but the verbal class itself is not defeated (C4
passes: V1/V2/V4 force 60 verbal; noun and adjective single-value claims
are both killed). The structural result is the bare-60 vs ent-60 shape
split, which regenerates as testable follow-ups below. Task rubric
check: not promote (no value covers all six); not kill per the brief's
kill definition (no window forces 60 non-verbal; no cleaner non-verbal
rival — both are already killed); hence null.

## Follow-ups (work regenerates; none duplicates queued targets)

1. **verb-60-bare** (priority 2): name the bare-60 verb across V1–V4
   (@1338 'qui [60] [08]', @700 'ne [60]n [98]', @995 '[03] [60] et',
   @1474 '[53] [60]ent veut [33-29]'). Bar: "name one verb with stem 60
   parsing all four frames with stated syllable boundaries, using only
   banked/granted/promoted values; 60='on' excluded (84='on' granted)."
   Evidence: this battery (V1/V2/V4 verb-forcing re-derived; V3
   verb-compatible). Adverses: 08/98/53 open; V4 '[60ent] veut [inf]'
   adjacency fenced (clause boundary or 53 re-parse needed); V3 also
   adjective-compatible (adj-60's @995 note) — coordinate, do not
   re-litigate the adjective arm.
2. **verb-60-ent** (priority 2): name the ent-60 verb across V5–V6
   (@1563 'ent[60] [71]', @1735 'ent[60]ne'). Bar: "name one
   ent-prefixed verb (ent[60]...) parsing both windows with stated
   boundaries; 60='on' ('entonne') excluded (84='on' granted; fails
   V2)." Evidence: this battery (06 forward-attachment forced by
   30='pas'; pas-30's own 'pas 06 60' parses @1561/@1733). Adverses: 71
   open; V6 'n[12] e[48]' boundary ('ent[60]ne' one word vs 'ne' word —
   one-word preferred, 'ne'-after-verb ungrammatical); the @232 '60 71'
   twin belongs to queued frame-vient-parvenir (not in scope).
3. **split-60-verbs** (priority 3): distributional split test —
   bare-60 verb (V1–V4) vs ent-60 verb (V5–V6) as two items sharing the
   syllable 60. Bar: "split iff the predecessor/successor selectional
   profiles of 60 in {V1–V4} vs {V5–V6} frames are distinguishable per
   the {33,86} split precedent (adapted); merge iff indistinguishable."
   Evidence: this battery's prefix/suffix asymmetry ('ent' suffix in
   V4 vs 'ent' prefix in V5/V6; '06 60 06' x0). Adverses: n small (4 vs
   2 windows) — underpowered, grade accordingly; a split is two items,
   not polyvalence, so §7's sole-polyvalence rule does not block the
   test (declaration only needed if one item ends up holding two
   values); coordinate with poly-60-redteam (pri 1, already queued).
