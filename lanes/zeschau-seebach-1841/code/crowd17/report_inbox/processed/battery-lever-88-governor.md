# Battery report: lever-88-governor

Target: `lever-88-governor`
Claim: "88 governs the 'lever' infinitive at @647/@1542"
Date: 2026-10-08
Worker: 773e288e-a422-445f-903e-9fdc782ae9d5
Lock note: no stale lock existed (locks/ empty at start); created locks/lever-88-governor.lock 2026-10-08T15:40:53Z, deleted on completion.

## Bar (verbatim from battery-queue.json)

"(1) 88 shows verb-frame contact at >=2 of the 88-77 windows (@86, @646, @1541) independent of the 77-78 composition; (2) @1542 '88 lever 43 pour que prenne 92' re-parses cleanly with 88 as governor and 43 nominal; (3) 88's class consistent across @646/@1541."

## Numbered clauses (fixed before testing)

1. 88 shows verb-frame contact at >=2 of the three 88-77 windows (@86, @646, @1541). The contact check must not assume 77-78 is one word ('lever'). It must hold under both the one-word and the two-word reading of 77-78.
2. The @1541 window (the bar labels it "@1542" by the parent battery's 77-start convention; the 88 itself is at @1541) re-parses cleanly as "88 lever 43 pour que prenne 92", with 88 as governor and 43 as a nominal (noun-like) object.
3. 88 has the same class (same structural role) at @646 and @1541.

Offset note: the bar's "@1542" is the parent lever-77-78 battery's window label (offset of the 77). The 88 under test is at @1541. All @-offsets below are 0-based repaired-stream pair indices. This is a labeling note, not a bar change.

## Method

Repaired 1,847-pair stream only: code/side-keyhunt/repaired_offsets.json over
data/upstream-ct_R5005.txt, parsed exactly like
code/side-keyhunt/repair_parse.py (byte-exact
`[s[i:i+2] for i in range(o, len(s)-1, 2)]`). code/side-keyhunt/canonical.py
never used. R5005 untouched. Standing values used: banked 11=la, 70=pre,
82=m, 34=i, 29=er, 40=e, 46=que; promoted 87=ce, 64=qui, 96=par, 17=fois,
79=tout, 00=pour (leg-1 class-level), 84=on, 47=ce; provisional 59=est,
77=le; battery-promoted pending ratification 94=ne (ne-94), 12=n + 48=e
letters (n-e-12-48), 06=ent (ent-06); red-team R16-005 grades 78="ver" LEAD
(not settled). Census facts re-derived from the stream, not copied.

## Window-level evidence

Census (re-derived): 88 occurs x23. 88-77 x3 at @86, @646, @1541 (matches
the brief). 88-77-78 x2 at @646, @1541 (the only two in the stream).
77-78 x7 at @7, @213, @647, @1077, @1180, @1351, @1542 (matches the parent
null). 43-00 ("43 pour") x3 at @244, @1126, @1544 (matches). 96-43
("par 43") x2 at @342, @1026 (matches). 11-52 ("la 52") x3 at @1006,
@1123, @1721. 77 occurs x44 with 15 predecessor types.

### @86 (a1_02): `84=14 85=06 [86=88] 87=77 88=66 89=98 90=19 91=41`

88's left contact is 06@85 (verb-stem class per F52-L2; 06="ent"
battery-promoted pending ratification). 88's right contact is 77-66
(the non-78 window). Under 77="le" (provisional), "88 le [66]" reads as
verb + object noun phrase: the transitive frame of a verb-class governor.
Fences: the 06-88 relation is open (verb-frame contact vs a preceding
finite verb 14-06 with a clause boundary before 88); 66 is open (object
head); 14's stemhood is open.

### @646 (a4_02): `643=24 644=87 645=61 [646=88] 647=77 648=78 649=52 650=82 651=94 652=76`

88 stands directly before 77-78, which is followed by 52 (nominal via
"la 52" x3). One-word reading: 88 governs the infinitive "lever", with
52 as its object ("[88] lever [52]"). Two-word reading: 88 stands before
"le" (77 provisional) + 78, and 78 is a ver-word (R16-005 LEAD, not
settled; "er" killed distributionally). Left context: 61 (open),
87="ce" (promoted) at @644. Tail "52 82 94 76" fenced per the parent
null (the 82-94-76 "m' ne" strain localizes to the tail, 76 open).

### @1541 (a8_00): `1539=62 1540=93 [1541=88] 1542=77 1543=78 1544=43 1545=00 1546=46 1547=70 1548=12 1549=94 1550=92`

Same 88-77-78 trigram as @646 (second of the two stream instances),
followed by 43 (nominal: "par 43" x2 with 96="par" promoted; "43 pour"
x3). Then 00="pour" (promoted) + 46="que" (banked) = "pour que".
Then 70-12-94 = "pre"+"n"+"ne" = "prenne" (70="pre" banked; 12="n" and
94="ne" battery-promoted pending ratification; composition per the
prenne-70-12-94 null). Then 92@1550: the prenne battery's "unresolvable"
subject now has a candidate — 92 as postposed subject ("pour que prenne
92", literary inversion; fenced, not asserted). Left edge "62 93 88":
93 is open (verb-93 queued); a clause boundary before 88 is fenced, with
no hard clash. Full conditional parse: "[88] [lever] [43-obj] pour que
prenne [92]". No hard contradiction.

### 88's global profile (n=23, for the follow-ups)

Successors: 77 x3, 11 ("la" banked) x2 (@730, @1514), 24 x2, 43 x1 (@42),
47 ("ce") x1 (@497: "79 88 47" = "tout 88 ce"), 19/02/20/40/53/56/10 x1.
Predecessors: 39 x2, 69 x2, 24/06/50/89/02/54/45/79/65/70 x1. Notes:
88 never directly precedes 29="er". 88-40 ("88"+"e", 40="e" banked
letter) occurs once at @334 ("88 40 03"): possibly word-internal
("[88]e[03]"), owned by FU1.

## Per-clause pass/fail

1. "Verb-frame contact at >=2 windows, independent of the 77-78
   composition": PASS (soft), 3/3 weak.
   - @646: weak pass. 88 directly precedes 77-78. One-word reading: 88
     governs the infinitive (parent null, soft at this window).
     Two-word reading: 88 precedes "le"+78, and 78 is a ver-word
     (R16-005 LEAD, unsettled). Contact holds under both readings, but
     the two-word arm leans on an unsettled lead, and 77 takes 15
     predecessor types stream-wide, so "88 le" alone does not fix 88's
     class.
   - @1541: weak pass, same fences (same trigram, second instance).
   - @86: weak pass. 88 touches 06@85 (verb-stem class per F52-L2;
     06="ent" battery-promoted pending ratification). The syntactic
     relation is open.
   - Ambiguity recorded: under a stricter reading of "independent"
     (no use of the 77-78 bigram at all), only @86 passes, giving
     1/3, which would fail the clause. The primary reading above is
     the bar's plain sense: the check must not presuppose the
     one-word composition.
2. "@1541 re-parses cleanly with 88 as governor and 43 nominal":
   PASS (soft) as a consistency check. The parse "[88] lever [43]
   pour que prenne [92]" has no hard contradiction: 43 nominal is
   well evidenced ("par 43" x2, "43 pour" x3); "pour que" uses a
   promoted value and a banked value; the "prenne" tail follows the
   prenne-70-12-94 composition with 92 as subject candidate.
   Circularity fenced: the parse assumes 88 is verb-class (the claim
   under test) and 77-78="lever" (the parent null, unsettled). This
   clause checks consistency; it does not independently confirm.
3. "88's class consistent across @646/@1541": PASS. Both windows put
   88 in the same slot: governor directly before 77-78, followed by a
   nominal object (52 at @646 via "la 52" x3; 43 at @1541). Caveat:
   n=2 and the same trigram twice, so the consistency is thin.

## Adverses answered

- "88 value fully open": FENCED with stated cause. The claim is
  relational (a governor slot), not a value claim. This battery names
  no value for 88 and promotes none. 88's value stays open.
- "@86 '88 77 [non-78]' needs integration": INTEGRATED. "14 06 88 77
  66": under 77="le" (provisional), "88 le [66]" is verb + object noun
  phrase — the transitive frame of the same verb-class 88 seen at
  @646/@1541 (there with an infinitive complement, here with a nominal
  complement). The 06@85 contact is fenced (verb-frame contact, or a
  preceding finite verb 14-06 with a clause boundary before 88).
  66 is open (object head). Not hostile to the governor claim.
- "Does not decide 77-78 by itself (governor evidence only)":
  RESPECTED. This battery does not settle the 77-78 composition. The
  parent lever-77-78 null stands untouched. No value promoted or
  killed.

## Verdict: NULL

Not promote. The three clauses pass only softly, and the passes lean
on unsettled analyses: clause 1's independence holds under the plain
reading but fails under the stricter reading, and its two main passes
are the same trigram twice; clause 2 is circular on the claim under
test and on the parent null's unsettled composition; clause 3 is thin
(n=2, same trigram). The governor claim cannot be settled while its
object (the "lever" infinitive) is itself a null — settlement is gated
on lever-77-78's follow-ups and on 88's value being named. Promoting
now would assert more than the bytes support.

Not kill. No window forces the claim false. No cleaner rival value was
demonstrated on these frames (the preposition rival — 88 as a
preposition governing the infinitive — is conceivable but
undemonstrated; it goes to FU1).

No standing red-team verdict is contradicted. R16-005's 78="ver"
grading is a LEAD, not a verdict, and is cited only as a lead with its
status stated. The parent lever-77-78 battery null is respected, not
downgraded.

## Follow-up targets (null regenerates work)

### FU1 id "governor-88-value" (priority 2)
- claim: "88's class/value is named from its 23-window profile"
- bars: "(1) 88's class named (verb? preposition? other) with >=3
  frame-legs from the profile: 88->11 x2 'la' (@730/@1514), 88->47
  'ce' (@497), 88->43 (@42), 06->88 (@85), 79->88 (@496); (2) the
  @86 '88 le 66', @334 '88 40' (word-internal '[88]e' vs word
  boundary), and @497 'tout 88 ce' windows parse under the named
  class; (3) one class stream-wide, or a positional rule stated (no
  new polyvalence without the red team)."
- evidence: "88 n=23; successors 77 x3, 11 x2, 24 x2, 43/47/19/02/20/
  40/53/56/10 x1; predecessors 39/69 x2, 24/06/50/89/02/54/45/79/65/70
  x1; 88->29 x0; preposition rival undemonstrated."
- adverses: "88 value fully open; @334 '88-40' may be word-internal;
  77's 15 predecessor types keep '88 le' class-neutral."

### FU2 id "governor-88-rerun" (priority 2)
- claim: "the governor claim re-tests cleanly once the 77-78
  composition settles"
- bars: "(1) re-run this battery's clauses 1-3 after lever-77-78's
  follow-ups (lever-213-complement, lever-lement-rival) settle the
  composition; (2) if 77-78 is not 'lever' at @647/@1542, re-state the
  governor claim against the settled frame or record kill; (3) do not
  re-litigate the composition here."
- evidence: "this report; battery-lever-77-78.md (null 2026-10-08);
  88-77-78 x2 @646/@1541 is the full stream census of the trigram."
- adverses: "gated on the parent null's follow-ups; 88's value still
  open until FU1 lands."

### FU3 id "finiteness-88-86" (priority 3)
- claim: "88's role at @86 is decided (finite verb vs infinitive)"
- bars: "(1) test whether 14-06 parses as a finite verb (06='ent'
  battery-promoted pending ratification), forcing a clause boundary
  before 88@86; (2) name 88's role at @86: finite verb ('88 le 66'
  transitive) vs infinitive after 14-06; (3) state consistency with
  the @646/@1541 governor role (same class or positional rule)."
- evidence: "@84-88 '14 06 88 77 66' (a1_02); 06='ent' (battery-ent-06,
  pending ratification); 77='le' provisional; 66 open."
- adverses: "14's stemhood open; 06='ent' not yet ratified; deciding
  finiteness does not name 88's value (FU1 owns that)."

## Constraints respected

R5005, sealed gates, and the red-team adjudication queue untouched. §7
banked/promoted/provisional/killed/split/held values respected; 67
et/veut sole polyvalence untouched (no value named, no polyvalence
claimed). No promotion recorded beyond this battery verdict (null).
canonical.py never used. No values redacted; every number traces to the
repaired stream.
