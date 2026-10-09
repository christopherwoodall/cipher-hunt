# Battery report: s5-verb-rival-four-windows

Target: `s5-verb-rival-four-windows`. Claim: test the transitive-verb rival
family for 37 on the four windows excluding @51's 'la tout' tail.
Date: 2026-10-09. Worker: a33be14a-a0c5-413c-9ac3-b04e8406459b (battery worker,
clean re-run — a previous attempt left an orphaned lock with no report; this
run does the full battery).
Lock `locks/s5-verb-rival-four-windows.lock` created 2026-10-09T02:46:05Z;
deleted on completion.

## Bar (verbatim, pre-registered)

"promote-rival iff ONE verb form parses 'tout V' (@51), 'V la' with
la=article+noun (noun source stated) or licit clitic (@1655), and 'V qui'
(@529/@1357/@1444) with zero contradiction on banked/promoted neighbors only;
else fence."

## Bar restated (numbered pass/fail clauses; frozen before testing)

1. ONE verb form V parses 'tout V' at @51 ("79 37") with zero contradiction on
   banked/promoted neighbors. The @52-53 '11 79' ('la tout') tail is excluded
   from this test per the claim (s5-la-tout-adjudicate's open question).
2. The same V parses 'V la' at @1655 ("37 11") — either la=article+noun (noun
   source stated) or licit object clitic — with zero contradiction on
   banked/promoted neighbors.
3. The same V parses 'V qui' at @529, @1357, AND @1444 (all three "37 64"
   windows; census confirms these are the only three on the repaired stream)
   with zero contradiction on banked/promoted neighbors.
4. No standing adverse is decided at battery level (S5 fence, §7, 'la tout'
   bound).

"Parses" means grammatical 1841 diplomatic French. "Zero contradiction on
banked/promoted neighbors only" is a floor, not a license: provisional values
(59='est', 77='le') are not protected, but re-valuing them without positive
evidence would be inventing data (§3 of the protocol) — so a parse that
requires re-valuing a provisional fails at battery grade.

## Method

Repaired 1,847-pair stream only: `code/side-keyhunt/repaired_offsets.json` +
`data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`
(stride-2 pairing per row offset; a5_03=0). Verified 1,847 pairs / 96 types
before testing. `canonical.py` never used. R5005 untouched (read-only parse).
No sealed gates, no red-team contact. Every number traces to the stream.
@-offsets are 0-based pair indices of the 37 group.

Standing values used (protocol §7): pencil GT 11=la, 70=pre, 82=m, 34=i,
29=er, 40=e, 46=que; granted/promoted 87=ce, 64=qui, 96=par, 17=fois,
79=tout (A5), 00=pour (A9), 84=on (A15), 47=ce (A4); provisional 59=est,
77=le; 94='ne' STRONG LEAD (R17-001); 67 et/veut sole polyvalence.

## Candidate selection

The bar demands ONE form covering three frame types. Constraints:
- C2 ('V la' @1655): the follower @1657 is 24 (finite-verb class), so the
  article+noun reading is dead (no noun). The only licit post-verbal "la"
  is the enclitic object pronoun, which requires the IMPERATIVE
  ("demande-la!", "prends-la!").
- C1 ('tout V' @51): bare "tout" + imperative is ungrammatical; "tout" as
  subject pronoun requires 3sg indicative ("tout demande").
- C2+C1 jointly force a verb whose 2sg imperative and 3sg indicative are the
  SAME surface form (the -er syncretism: parle/parle, demande/demande).
- C3 ('V qui'): the verb must license a "qui"-clause (indirect interrogative).
  Among syncretic -er verbs, "demander" is the unique clean licenser
  ("demande qui vient" ✓). Rivals fail: penser ("*pense qui"), offrir
  ("*offre qui"), prier ("*prie qui"); non-syncretic verbs (dire dit/dis,
  faire fait/fais, savoir sait/sache, prendre prend/prends) fail the
  one-form requirement outright.

Candidate: **"demande"** (demander). Unique best; tested below.

## Window-level evidence

W1 — 'tout V' @51 (row a1_01):
`@43-58: 43 81 30 62 96 00 92 79 37 11 79 85 58 35`
"par(96) pour(00) [92] tout(79) [demande] la(11) tout(79) [85]".
"tout demande" = "everything asks" (pronoun subject + 3sg) — grammatical.
Zero banked/promoted contradiction (79 used as granted). The @52-53 tail
excluded per claim. **Clause 1: PASS.**

W2 — 'V la' @1655 (row a8_04):
`@1647-1664: 31 10 03 38 82 16 01 56 37 11 24 48 47 98 98 80`
"m(82) [16] [01] [56] [demande] la(11) [24] e(48) ce(47) [98] [98] [80]".
Article+noun: DEAD — @1657 is 24 (verb class), no noun follows "la".
Licit clitic: "demande-la!" (imperative 2sg + enclitic object) — grammatical
as a frame.
CAVEAT (recorded, not hidden): C1 uses indicative "demande", C2 uses
imperative "demande" — same surface form, different mood. The bar says "ONE
verb form"; the form is identical, but the mood shift strains the spirit of
the requirement. Following context @1657+ ("[24] e ce [98]...") is stranded
by the imperative parse but not contradicted (no banked/promoted values
touched). **Clause 2: PASS with stated mood-shift caveat.**

W3a — 'V qui' @529 (row a3_00):
`@521-538: 77 06 55 81 97 47 44 59 37 64 26 32 16 08 24`
"ce(47) [44] [59] [demande] qui(64) [26] [32]".
Banked/promoted neighbors: 47=ce, 64=qui. 59 is provisional 'est'.
"ce [44] est demande" — "est" + finite "demande" is UNGRAMMATICAL. No
positive evidence supports re-valuing provisional 59; doing so would be
inventing data. ("qui [26] [32]" is additionally problematic: "qui" +
noun-class + verb-lexeme has no grammatical reading.) **Clause 3a: FAIL.**

W3b — 'V qui' @1357 (row a7_05):
`@1349-1366: 62 48 77 78 94 82 06 52 37 64 35 13 92 62`
"[78] ne(94) m(82) ent(06) [52] [demande] qui(64) [35] [13]".
"[52] demande qui [35]": constructible as "[52-subject] demande (3sg) qui
[35]" — "asks who [35]" — CONDITIONAL on 35 being verb-shaped (35 open, not
banked/promoted, so no contradiction; but no positive evidence either).
Left context "94 82 06" ("ne m'ent…") is messy but outside the frame.
**Clause 3b: MARGINAL — parses only conditionally (35 verb-shaped
unestablished).**

W3c — 'V qui' @1444 (row a7_09):
`@1436-1453: 82 16 24 85 01 52 68 59 37 64 77 84 59 36`
"[68] [59] [demande] qui(64) [77] on(84) [59]".
Left: "[59] demande" — same "est demande" block as @529 (59 provisional
'est'). Right: "demande qui [77]" — "qui" followed by 77 (provisional 'le'):
"qui" + "le" is ungrammatical in EVERY reading (relative "qui" takes a verb;
interrogative "qui" takes a verb; "le" is not a verb). 77 is provisional, but
there is no positive evidence it is verb-shaped. Double failure.
**Clause 3c: FAIL.**

Structural note: @529 and @1444 share the "[59] [37] qui" shape
("59-37" occurs 6× stream-wide: @529/@625/@913/@1179/@1444/@1797). Under the
standing provisional 59='est', NO finite verb can occupy 37 at these windows
— this bounds the verb family generally, not just "demande".

## Per-clause pass/fail

1. 'tout V' @51: **PASS** ("tout demande", 3sg; tail excluded).
2. 'V la' @1655: **PASS with caveat** ("demande-la" imperative+enclitic;
   article+noun dead; mood shift vs clause 1 recorded).
3. 'V qui' @529: **FAIL** ("est demande" ungrammatical under standing 59).
   'V qui' @1357: **MARGINAL** (conditional on 35 verb-shaped).
   'V qui' @1444: **FAIL** ("est demande" + "qui le" ungrammatical).
4. Adverses: S5 fence untouched (nothing decided); §7 intact (no polyvalence
   declared); 'la tout' bound respected (tail excluded, question untouched).

The bar's consequent is "promote-rival iff ...; else fence" — there is no
kill branch. Clauses 3a and 3c fail, so the fence arm fires.

## Verdict: NULL (fence)

The transitive-verb rival family, in its unique best form ("demande" — the
only transitive, "qui"-licensing verb with syncretic 2sg.imp/3sg.ind),
parses C1 and C2 (with a recorded mood-shift caveat) but fails C3 at @529
and @1444 under the standing provisional values 59='est' and 77='le'. The
family is NOT killed: the failures turn on provisional (unratified) values,
so a red-team re-valuation of 59 could revive it — that decision is
red-team territory, not battery level. @1357 remains the most verb-friendly
'V qui' window (conditional on 35).

Headline for the red team: @529 and @1444 share "[59] [37] qui"; if 59='est'
is confirmed, the finite-verb reading of 37 is dead at both windows for
EVERY verb, not just "demande".

## Adverses answered

- S5 standing fence (37='le' MEDIUM, round-7): not decided, not touched —
  this null neither promotes the rival nor disturbs the fence.
- §7 (no polyvalence at battery level): none declared; the mood-shift caveat
  is recorded as an observation, not a declaration.
- s5-la-tout-adjudicate's 'la tout' question: excluded from the @51 test per
  the claim; untouched and still bounding any future promotion.

## Follow-up targets (null regenerates work)

1. **s5-59-est-audit** (priority 2). Claim: 59='est' holds or falls at the
   six "59 37" windows (@529/@625/@913/@1179/@1444/@1797). Bars: (a) confirm
   59='est' with independent legs at @528 and @1443, or re-value 59 with
   stated positive evidence; (b) if 59='est' is confirmed, the finite-verb
   reading of 37 is dead at @529/@1444 for every verb — record the
   general bound; (c) never invent a value for 59. Evidence: this report.
   Adverses: 59 provisional (battery-level, unratified).
2. **demande-35-verbshape** (priority 2). Claim: 35 is verb-shaped, which
   would make @1357 a clean "[52] demande qui [35-verb]" leg. Bars: 35
   verb-shaped iff ≥2 windows show it taking a subject or complement;
   else fence @1357's "qui [35]". Evidence: this report (W3b).
   Adverses: 35 open, n small.
3. **qui-77-census** (priority 3). Claim: census "64 77" ×3
   (@144/@1445/@1801) — if 77 is never verb-shaped, @1444's "qui [77]"
   kills the verb reading there independently of 59. Bars: state 77's
   class from the three windows + contact profile; fence or kill the @1444
   verb leg accordingly. Evidence: this report (W3c). Adverses: 77='le'
   provisional.

## Reproducibility

All counts re-derived in-session from the repaired stream (1,847 pairs / 96
types asserted before testing): 37-64 windows exactly @529/@1357/@1444;
37-11 exactly @51/@1655; 79-37 exactly @50; 59-37 ×6; 64-77 ×3. No analysis
script retained — window dumps and censuses above are the record. No writes
outside this report, the queue edit, and the lockfile (deleted).
