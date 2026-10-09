# Battery report: noun-88-subject — test 88 as a plural NOUN subject at @1117

- Target id: `noun-88-subject` (priority 2)
- Claim: "Test 88 as a plural NOUN subject at @1117."
- Date: 2026-10-09
- Worker: subagent session 2fa232e7-7da1-4417-82ce-47b6a813d539 (parent: next-token-supervisor)
- Lock note: no pre-existing lock in `code/crowd17/next-token/locks/` at start;
  created `locks/noun-88-subject.lock` 2026-10-09T07:53:46Z, deleted on completion.
- Verdict: **KILL**

## Bar (verbatim from battery-queue.json, copied before any window analysis)

"Name a plural noun value (or noun class with two independent frame legs) that parses @1117 "@1114-1123" and @496-497 with zero contradiction on banked neighbors; else fence 88's class as open."

## Numbered clauses (fixed from the bar text before detailed testing; not modified after seeing data)

- **C1 (value branch):** name a plural noun VALUE for 88 that parses BOTH
  @1117 ("la [88]" window) and @496-497 ("tout [88]" window) with zero
  contradiction on banked neighbors (11=la, 79=tout, 70=pre).
- **C2 (class branch):** name a noun CLASS supported by TWO INDEPENDENT frame
  legs, both parsing the same two loci with zero contradiction on banked
  neighbors.
- **C3 (verdict rule):** promote iff C1 or C2 passes AND all adverses answered
  (adverses: none recorded). Kill iff a window forces the claim false at kill
  grade (a window forces the claim false, or a distributional test rejects at
  the lane's standard). Else null; a null fences 88's class as open.

## Method

Repaired 1,847-pair / 96-type stream only: `code/side-keyhunt/repaired_offsets.json`
over `data/upstream-ct_R5005.txt`, parsed exactly like
`code/side-keyhunt/repair_parse.py` (byte-exact
`[s[i:i+2] for i in range(o, len(s)-1, 2)]`; 1847 pairs / 96 types re-verified
by this worker). `code/side-keyhunt/canonical.py` never used. R5005, sealed
gate instances, and the red-team adjudication queue untouched. All @-offsets
below are 0-based repaired-stream pair indices (queue convention). The task
spec's "@766" for "est a [88]" is 1-based = 0-based @765 below.

Standing values used: banked pencil (11=la, 70=pre, 82=m, 34=i, 29=er, 40=e,
46=que); granted (79=tout A5, 47=ce A4, 87=ce, 64=qui, 96=par, 17=fois,
00=pour A9 class-level, 84=on A15, 45=ce A4 HOLD); provisional (59=est,
77=le). Battery-level (not re-litigated): 88 = VERB-CLASS class-level
(battery-governor-88-value, PROMOTE 2026-10-08); 30=pas (promoted);
94='ne' STRONG LEAD. Standing constraints per BATTERY-PROTOCOL.md §7: 67
et/veut is the sole true polyvalence — no new polyvalence may be declared at
battery level; kills hold: 48="est"/"ne"/"de".

Prior 88 verdicts consulted (not re-litigated): prennent-88-subject KILL
(2026-10-09, plural-subject arm killed at @496-497); name-88-value KILL
(2026-10-08); noun-88-det NULL (2026-10-09, gender clash @402/@1117;
@1117 "la [88]" reading CONDITIONAL on the contested cela-69-11
segmentation); 88-prep-rival PROMOTE (2026-10-09, six verb-deciding legs,
preposition rival killed); 88-1727-shape PROMOTE (2026-10-09, 88
infinitive-shaped at @1727); finiteness-88-86 PROMOTE (2026-10-09, @86 under
the transitive governor-88 frame); ce88-leftedge-402 PROMOTE (2026-10-09).

## Window-level evidence

### Locus 1 — @1117 (row a6_07, mid-row, locus 4 pairs from row start; no boundary rescue)

`@1114-1123 = 30 69 11 [88] 70 12 06 14 06 11`
Under standing values: `pas [69] la [88] pre-n-ent [14]-ent la`
= "pas [69] la [88] prennent souvent la ..." — the 70-12-06 trigram is the
3rd-plural verb frame ("prennent" per breaker-b4-1121; "prenent" under the
unproven single-n clerk spelling, queued spell-single-consonant — the 3pl
marking itself is not in doubt per prennent-88-subject).

For 88 to be the plural NOUN subject of the 3pl verb at @1118-1120, the
subject NP must be "la [88]". But @1116 = 11 = "la" is BANKED pencil ground
truth (crib "la premiere" pair-aligned twice, repair_parse.py asserts) — a
singular feminine definite article. A plural noun inside the "la [V]" NP
violates number agreement in 1841 French, unconditionally: no choice of
plural noun value V makes "la [V-plural]" grammatical. **The window forces
the claim false, independent of the value named.**

Rescue attempts, all closed:
- (a) cela-69-11-word segmentation (@1115-1116 = "cela", battery-promoted,
  pending round-18 red-team adjudication): if it stands, "la" is
  word-internal and the determiner frame dissolves — but the window then
  reads "pas cela [88] prennent souvent la", requiring a BARE plural noun
  subject, which is ungrammatical in 1841 diplomatic French (needs "les").
  Also ungranted at battery level. Closed.
- (b) "la" as object pronoun of a preceding verb + 88 subject of the next:
  no verb precedes ("pas [69]" is negation + open 69); "pas cela la"
  is itself ungrammatical. Closed.
- (c) Proper-noun value: the bar demands a PLURAL noun; proper names are
  not plural, and "la" + proper name is ungrammatical in the period.
  Closed.

### Locus 2 — @496-497 (row a2_11, mid-row; no boundary rescue)

`@492-501 = 78 42 94 02 [79] [88] 47 11 29 40`
= "[78] [42] [94] [02] tout [88] ce la er ..."
@496 = 79 = "tout" is GRANTED (A5) — bedrock. In French of any period,
including 1841 diplomatic French, "tout" + BARE plural noun is
ungrammatical (the quantifier needs "tous": "tous les X"; cf.
prennent-88-subject's identical kill of the plural-pronoun arm at this
locus). The only nominal survivors of "tout [88]" are SINGULAR
("tout homme") — which is not the claim — or adjectival. A plural noun
value for 88 is **forced false at this window too**, independent of the
value named. (The task's own evidence already records this locus as
forcing 88 != plural pronoun under §7 monovalence; the plural-noun arm
dies at the same locus.)

### Candidate noun-class frame legs (C2)

The task's evidence offered "est a [88]" @765 and "88 le" x3 as
noun-compatible. Re-derived against the stream, both are verb legs:

- **"est a [88]" (88 at @765 0-based, row a5_03; @763-765 = 59 39 88,
  also @1726-1727 = 39 88 on row a8_07):** "a" = preposition "a". In 1841
  French, "a" + bare noun requires an article ("a [art] [noun]"); "est a
  [noun]" bare is ungrammatical. 88-prep-rival (PROMOTE 2026-10-09, Leg A)
  demonstrated "est a [88-inf]" is the passive-infinitive construction and
  "vient a [88-inf]" at @1727 is infinitive-licensed — verb-deciding, not
  noun-compatible.
- **"88 le" x3 (88 at @86/@646/@1541 0-based, rows a1_02/a4_02/a8_00):**
  @86 = "14 06 [88] 77 66" = "[14]-ent [88] le [66]": under the standing
  verb-class grant this is the transitive frame (verb + direct-object NP),
  re-derived clean by finiteness-88-86 (PROMOTE, C1 PASS). As a noun, "[noun]
  le" admits no parse — an article cannot follow its noun, and there is no
  "de" for a genitive. Ungrammatical. Not a noun leg.

Distributional check (88 n=23, re-derived): predecessors 39 x2 ("a"),
69 x2, +19 singles; successors 77 x3 ("le"), 11 x2, 24 x2, +16 singles.
No predecessor is a determiner that licenses a plural noun ("la" x1 is
the agreement-violating @1117; "ce" x1 at @402 is the singular/masculine
"ce" frame that noun-88-det showed clashes with "la"). The profile offers
no noun-shaped contact beyond the two tested loci, both of which kill.

Result: **0 of 2 required noun-class frame legs exist.** The "two
independent frame legs" branch is empty — the cited frames are verb legs.

## Per-clause pass/fail

- **C1 (plural noun value): FAIL at kill grade.** No plural noun value
  parses @1117 with zero contradiction on banked 11=la ("la" + plural noun
  = number-agreement violation, unconditional on the value), and none
  parses @496-497 with zero contradiction on granted 79=tout ("tout" +
  bare plural noun ungrammatical). Two independent windows each force the
  claim false.
- **C2 (noun class, two legs): FAIL.** Zero noun-class frame legs survive:
  "est a [88]" and "88 le" x3 are verb legs under standing grants
  (88-prep-rival Leg A; finiteness-88-86 C1). Nothing to promote.
- **C3 (verdict rule): KILL.** A window forces the claim false (twice over).

## Adverses

None recorded in the queue entry. The closest standing counter-evidence —
"est a [88]" and "88 le" x3 being "noun-compatible" — was re-derived and
is answered: both are verb legs (see above), not ignored.

## Verdict: KILL

88 as a plural noun subject at @1117 is forced false by @1114-1123
("la" + plural noun agreement violation on banked 11=la) and by @496-497
("tout" + bare plural noun ungrammatical on granted 79=tout). No plural
noun value and no two noun-class frame legs survive. Consistent with
standing battery verdicts: governor-88-value (88 = VERB-CLASS, PROMOTE),
prennent-88-subject (plural-subject arm KILL), name-88-value (KILL);
§7 sole-true-polyvalence rule (67 et/veut) bars the noun reading at
battery level without red-team ratification — none sought, none needed.
No escalation: this kill contradicts no standing verdict.

No follow-ups proposed (kills do not regenerate work; nulls do).
