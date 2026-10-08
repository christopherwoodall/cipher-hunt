# Battery report: noun26-la-frames

Date: 2026-10-08. Target id: `noun26-la-frames` (priority 2).
Stream: repaired 1,847-pair parse (`data/upstream-ct_R5005.txt` +
`code/side-keyhunt/repaired_offsets.json`, parsed byte-exact like
`code/side-keyhunt/repair_parse.py`; 96 distinct pairs). Never
canonical.py. Never R5005.
Lane @-convention: report @ = 0-based stream index - 1.
Lock: created 2026-10-08T15:41:00Z; no stale lock existed
(locks/ held only NOTE.md at creation).

## Bar (verbatim, pre-registered before testing)

"(a) @239 '41 17 11 26 12 16' = absolute 'une fois la [N]' with the
'n[16]' tail named or fenced; (b) @1559 '40 17 11 26 30 06': the 'pas'
resolved — boundary, re-parse, or the noun claim FAILS at this window
(stated, not smoothed); (c) @128 '48 11 02 26 32 96' parses as 'la
[02-adj] [26-noun] [32-adj]' (or 'la [02-26-noun] [32-adj]' — the
composition rival tested: '02 26' is 1x stream-wide, neither confirmed
nor excludable); (d) @530 'qui [26] [32]' addressed: 'qui est 32' x2 is
the control; 26='est' killed globally by @239 ('la est' ungrammatical);
(e) '26n' reading (12 = final 'n') tested at @239"

Bar copied from battery-queue.json before any stream testing.

## Bar restated as numbered pass/fail clauses

1. @239 "41 17 11 26 12 16" parses as the absolute "une fois la [N]",
   and the "n[16]" tail is named or fenced with stated cause.
2. @1559 "40 17 11 26 30 06": the "pas" is resolved by a clause
   boundary, by a re-parse, or the noun claim is recorded as FAILED at
   this window — stated plainly, not smoothed over.
3. @128 "48 11 02 26 32 96" parses as "la [02-adj] [26-noun] [32-adj]"
   or as "la [02-26-noun] [32-adj]"; the "02 26" composition rival is
   tested (1x stream-wide, neither confirmed nor excludable).
4. @530 "qui [26] [32]" is addressed: the "qui est 32" x2 control is
   shown, and 26="est" is killed globally (by @239's "la est").
5. The "26n" reading (12 = final "n") is tested at @239.

## Method

Rebuilt the stream from the two primary sources with the repair
script's byte-exact tokenizer (offset flip a5_03 1->0; 1,847 pairs;
crib "11 70 82 34 29 40" pair-aligned at 0-based 754 and 1034).
Re-derived all four bar windows by content match on the repaired
stream. Ran full censuses: 26 (17x), 41 (19x), 11 (45x), 12 (23x),
16 (28x), 40 (21x), 02 (17x), 30 (19x). Standing inputs: 11="la"
(banked), 17="fois" (granted), 96="par" (granted), 64="qui"
(promoted), 87="ce" (granted), 47="ce" (A4), 00="pour" (A9),
59="est" (provisional), 77="le" (provisional); battery-promoted
(pending red-team ratification): 30="pas", 94="ne", 12="n"/48="e"
(letters), 06="ent/ment"; 37/32/42 predicative (A1, values open);
23~26 split (A2); 67 the sole true polyvalence (§7). Cited, not
re-derived: battery noun26-pas-frames (PROMOTE), battery
noun26-gov-frames (PROMOTE), battery pas-30 (PROMOTE),
finder noun26-frames. No invented numbers; every count below is from
the repaired stream.

## Window-level evidence

### Clause 1 — @239 (0-based 240; row a2_01; ±4: "98 41 17 11 26 12 16 56 43")

"41 17 11 26" reads "[41] fois, la [26]". With 41="une" this is the
standard French absolute "une fois la [N]" ("once the [N] ...").
41="une" at this window: coherent and unfalsified. 41's full census
(19x, 17 distinct followers) shows no window forcing 41!="une":
the "41 41" doubling (0-based 589-590) spans a manuscript row boundary
(a3_02->a4_00), and doubling does not exclude article-hood at the
lane's own standard — banked 11="la" itself doubles gapless mid-row
("11 11" 1x @1522, row a7_11). Stated residual: "47 41 06" @4
("09 00 97 51 47 41 06 77 78", row a1_00) resists 41="une"
("ce"+"une" ungrammatical); 41's global value is owned by queued
`donn-41-44` (joint, not duplicated here). The @239 parse does not
depend on it.

Tail "n[16]": FENCED with stated cause. Three live readings of
"26 12 16": (i) 26-word + "n"-initial word (12="n" battery-promoted
letter) + 16; (ii) "26n" one word (12 = final "n") + 16; (iii) 26 +
"n'" elision + 16. 16's class is open (n=28; prev 82="m" x11 — the
"82 16" collocation owned by queued `frame-82-16`; next 00="pour"
x4). None of the three readings is forced. Clause 5 tests reading
(ii) specifically.

### Clause 2 — @1559 (0-based 1560; row a8_01; ±4: "61 40 17 11 26 30 06 60 71")

Left: "40 17 11 26" = "...[61]e fois, la [26]" (40="e" battery-promoted
letter; "61 40" 1x). 26 is FORCED nominal here by banked 11="la"
(T1's promoted finding; independently confirmed: "11 26" exactly 2x
stream-wide, both "...17 11 26"). The re-parse rival ("l'a" +
participle, i.e. 11 as object pronoun) is rejected: it contradicts
banked 11="la", and it needs a subject plus "ne" — both absent.

30="pas" (battery-promoted) cannot left-adjoin to a nominal 26:
"[noun] pas" is ungrammatical, and the bigram is gapless mid-row.
Resolution: CLAUSE BOUNDARY between 26 and 30, by grammatical
necessity — the bar's boundary disjunct (same fence T1 promoted;
verified independently, not copied). Supporting audit: no "ne" in
26's clause — 94@1548 (d-11) and 12@1547 (d-12) both sit inside the
"00 46 70 12 94" frame, a different clause. Right side:
"30 06 60 71 ..." = bare-"pas" fragment, "pas [06='ent/ment'] [60]".
The bare-"pas" 1840s anomaly is STATED, not smoothed, and flagged to
queued `ne-alone-02-74` (which owns bare-"ne"/bare-"pas" licensing).
Precedent for bare-"pas" fragments with boundaries: the pas-30
battery's @1729/@1733 "pas ..., pas ..." windows.

The noun claim does NOT fail at @1559: "la [26]" stands as a noun leg;
the "pas" is fenced right of the boundary.

### Clause 3 — @128 (0-based 129; row a1_03; ±4: "82 48 11 02 26 32 96 56 64")

48="e" (battery-promoted letter) is the tail of the preceding word
("82 48" = "m e"); the phrase is "la [02] [26] [32] par" (96="par"
granted). 26=verb is ungrammatical under banked 11="la": an article
cannot precede a finite verb, and no boundary is available (gapless,
mid-row). The boundary rival ("la [02]" as a complete noun phrase +
new clause) is dispreferred and stated: "11 02" is 1x stream-wide
with no independent "la [02]"-NP support.

Two live nominal parses: "la [02-adj] [26-noun] [32-adj]" and the
compound rival "la [02-26-noun] [32-adj]". Composition rival TESTED:
"02 26" exactly 1x stream-wide (@127-128) — neither confirmed nor
excludable, exactly as the bar states. 32's post-nominal adjectival
slot is consistent with the "qui est 32" controls (clause 4) and the
37/32/42 predicative grant (32's value owned by queued `adj-32`).
Either parse keeps 26 nominal.

### Clause 4 — @530 (0-based 531; rows a3_00->a3_01; ±4: "44 59 37 64 26 32 16 08")

Control re-derived: "64 59 32" ("qui est 32", 59="est" provisional)
exactly 2x stream-wide — @314 ("64 59 32 94 06", row a2_07) and @1208
("64 59 32 48 96", row a7_00).

26="est" KILLED globally. At @239, "la est" is ungrammatical under
banked 11="la". Stream-wide audit: "11 59" occurs exactly 1x, @462
("87 11 59 42 96") — and it is the closed unit "cela est [42-pred]"
(87="ce" granted; 42 inside the predicative grant), NOT article +
"est". So no "la"+"est" article reading exists anywhere; 59 already
fills the "est" slot. A third value for 26 ("est" alongside
noun/verb) has no evidence and is not posited.

@530 addressed: under the positional rule 26=verb here (preceded by
64="qui", not 11) — "...est [37], qui [26-verb] [32]..." is a
grammatical relative clause. The copula-shaped rival ("qui est 32")
is a stated non-parse because 26!="est". 32's class deferred to
`adj-32` (queued). The crux is stated, not forced.

### Clause 5 — the "26n" reading at @239

TESTED. 12="n" is battery-promoted (n-e-12-48). "26 12" exactly 4x
stream-wide: @239 ("11 26 12 16"), @841 ("94 26 12 16"), @1469
("38 26 12 41"), @1706 ("88 26 12 06"); "26 12 16" x2 (@239, @841).
At @239 the one-word reading "la [26n]" (feminine noun ending in -n)
followed by 16 is grammatical and LIVE — contact supports it and no
window forces 26 and 12 apart here. Constraint: a GLOBAL "26n" value
is excluded at @841 ("94 [26n] [16]" = "ne [noun]", ungrammatical
under battery-promoted 94="ne" — the gov-frames exclusion, cited not
re-derived). A position-dependent composition (one word at @239, two
at @841) is unparsimonious. The two-word readings (12 = "n"-initial
word; 12 = "n'" elision) remain live at @239. Global exclusion is
owned by queued `noun26-26n-exclude` (joint, not duplicated).

## Per-clause pass/fail

1. @239 absolute "une fois la [N]": PASS. Window parses cleanly;
   41="une" coherent at this window (18/19 census windows consistent;
   "47 41 06" @4 residual stated, owned by queued `donn-41-44`);
   tail "n[16]" fenced with stated cause (three live readings; 16's
   class open, owned by queued `frame-82-16`).
2. @1559 "pas" resolved: PASS via the boundary disjunct. 26 forced
   nominal by banked "la"; re-parse rejected (contradicts banked 11,
   needs absent subject+"ne"); boundary between 26 and 30 by
   grammatical necessity; bare-"pas" right side stated as residual,
   flagged to queued `ne-alone-02-74`. Noun claim survives at @1559.
3. @128 "la [02] [26] [32]": PASS. Verb-parse ungrammatical under
   banked 11 (boundary rival dispreferred, stated); both live parses
   keep 26 nominal; "02 26" composition rival tested — 1x
   stream-wide, neither confirmed nor excludable.
4. @530 "qui [26] [32]" addressed: PASS. Control "qui est 32" x2
   re-derived (@314, @1208); 26="est" killed globally (@239 "la est"
   impossible; sole "11 59" is the closed unit "cela est"); @530 =
   verb-slot under the positional rule ("qui [26-verb] [32]").
5. "26n" reading at @239: PASS (tested). Live at @239 (grammatical,
   unexcludable here); global one-word value excluded at @841;
   global exclusion owned by queued `noun26-26n-exclude`.

## Adverses (all answered, none ignored)

1. "Only 2-3 legs" — ANSWERED. Exactly 3 legs: "11 26" x2 (@239,
   @1559) + "11 02 26" x1 (@128). The claim's scope matches the
   evidence; no overclaim. The noun theory is narrow and conditioned
   — recorded as such.
2. "@1559's internal 'pas' contradiction (the war's crux)" —
   ANSWERED via clause 2: boundary fence with stated cause; 26
   nominal forced by banked "la"; bare-"pas" residual stated and
   flagged, not smoothed.
3. "noun26-pas-frames/noun26-gov-frames verb windows must be answered,
   not ignored" — ANSWERED. T1's verb windows (@654/@991/@1249 and
   the pas-side of @1559) and T3's governor windows (@154/@600/@841/
   @1706), plus the encequi-triple slot (@1768), all hold — cited
   from their promoted reports, not re-litigated. Resolution, as the
   adverse invites: the POSITIONAL RULE. Refinement recorded (goes
   beyond T1's wording): @128's "11 02 26" shows the determiner need
   not be immediately adjacent — an intervening modifier (02) is
   tolerated. Rule as refined: **26 = feminine noun iff its
   determiner phrase is headed by 11="la" (immediate: "11 26" x2; or
   via intervening 02: "11 02 26" x1); elsewhere verb-class.**
   POLYVALENCE COST (for the red team): this is a second positional
   polyvalence, in tension with §7's "67 et/veut is the sole true
   polyvalence". This battery declares no polyvalence and overwrites
   no verdict — the rule is recorded as a finding; declaration is a
   red-team act (the same referral T1 made).

## Verdict

**PROMOTE.** All five bar clauses pass on the repaired stream and
every listed adverse is answered (re-parsed cleanly or fenced with
stated cause, never ignored). The noun legs survive: "...fois, la
[26]" x2 (@239, @1559) + "la [02] [26] [32]" @128; 26 = feminine noun
where "la" (banked) is the article. The eight verb windows stand
alongside via the recorded positional rule (refined above), whose
polyvalence cost is stated for the red team. No standing red-team
verdict is contradicted: T1 explicitly deferred the la-frames to
this battery, and the refinement generalizes rather than overturns
T1's rule. (No null, so no follow-up targets are required.)

## Caveats (epistemic status, marked up front)

- 30="pas", 94="ne", 12="n"/48="e", 06="ent/ment" are
  battery-promoted, PENDING red-team ratification; 59="est" and
  77="le" are provisional. All "ne"/"pas"-dependent readings inherit
  these caveats.
- 41="une" is the bar's stipulation at @239 (coherent, 18/19 windows
  consistent); 41's global value is owned by queued `donn-41-44`.
- 16's class open (queued `frame-82-16`); 02's class open
  (adjective-shaped by position); 32's value open (queued `adj-32`);
  60/61 values open.
- Canonicality caveat stands (§7): 68 of 70 upstream row offsets
  unvalidated; offsets here are post-repair indices.
- "26n" global exclusion owned by queued `noun26-26n-exclude`;
  bare-"pas" licensing owned by queued `ne-alone-02-74`.
