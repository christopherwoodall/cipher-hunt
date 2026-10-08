# Battery report: stem-42-verb — "42 takes 'ent' as a verb stem"

Target: `stem-42-verb`. Claim: 42 takes 'ent' as a verb stem. Date: 2026-10-08.
Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` +
`data/upstream-ct_R5005.txt`), parsed like `code/side-keyhunt/repair_parse.py`.
Never used `canonical.py`. R5005 untouched. No invented data.
@-offsets below are 1-based (lane convention; queue evidence @206/@267/@544/
@1188/@1815 matches this parse at 1-based).

Dependency: 06='ent' is battery-promoted (battery-ent-06, pending red-team
ratification). This battery tests 42's side of the 42-06 contact.

## Bar (verbatim, pre-registered)

"resolve iff 42 shows verb-class contact in >=3 of the 5 windows with the A1
predicative-frame grant left intact, or fence the stem reading with stated cause"

Numbered clauses (fixed before testing):

1. 42 shows verb-class contact in >=3 of the 5 windows (@206/@267/@544/@1188/
   @1815), i.e. the 42-06 unit parses as verb-stem + 'ent' inside a frame that
   selects or requires a finite verb (verb-governing complementizer, visible
   subject, or verb-complement such as a direct object).
2. The A1 predicative-frame grant for 42 ("est 42", 59->42 x2) is left intact:
   both windows re-derived, the grant is not re-litigated, and no clause of
   this battery downgrades it.
3. (Bar's alternative path) If clause 1 is not met, the stem reading is
   fenced with stated cause rather than promoted — this is the bar's own
   null path, not a silent rewrite.

## Method

Full census of 42 on the repaired stream: 42 n=20. All five 42-06 windows
extracted with ±12 context and parsed under standing values (banked: 11=la,
70=pre, 82=m, 34=i, 29=er, 40=e, 46=que; granted: 87=ce, 64=qui, 96=par,
17=fois, 79=tout, 00=pour, 84=on, 47=ce; provisional: 59=est, 77=le;
battery: 94=ne, 12=n, 48=e, 06=ent). 42's global contact profile taken as
adverse context (predecessors: 29 x3, 76 x3, 33 x2, 59 x2; successors: 06 x5,
98 x3, 94 x3, 16 x2, 44 x2). The two A1 windows re-derived to confirm the
grant stands.

## Window-level evidence (@-offsets, 1-based)

**W1 @206** (row a2_00): `... 87 11 92 63 [42 06] 77 44 50 88 ...`
= "cela [92] [63] [42]ent le [44] [50] ..."
- Right contact: "[42]ent le [44]" — transitive verb + "le"+noun object.
  44 is noun-shaped on independent grounds ("le 44" x2 @206/@1618-region,
  "44 pour" x3); 77='le' provisional. Most economical parse: 3pl verb
  "[42]ent" + direct object "le [44]".
- Left junction fenced (cause): no visible plural subject; "cela [92] [63]"
  region is singular ("cela") and cannot agree with 3pl "-ent"; subject must
  sit across a clause boundary or in the unresolvable "[92] [63]" span.
- Score: PASS (verb-complement contact; one stated fence on the left).

**W2 @267** (row a2_02): `... 52 33 [42 06] 73 47 11 ...`
= "[52] [33] [42]ent [73] ce la ..."
- 33 abuts 42 directly, and "33 42" occurs x2 (@267, @1504). 33 is the
  dire-set (infinitive/stem). Under 33='dire' (infinitive), "dire [42]ent"
  is ungrammatical — a conjugated verb cannot directly follow "dire".
- The grammatical rival on the same frame: "dire [42ent-noun]" (infinitive +
  noun object, "…ent"-final noun) or 33-42-06 word-internal. Either way the
  42-06 unit here is NOT verb-stem + inflection.
- Score: FAIL — fenced with cause (33's infinitive/dire contact forces a
  non-verb reading of the 42-06 unit; the 33-set adjudication itself is
  red-team-owned).

**W3 @544** (row a3_01): `... 44 29 48 [42 06] 00 46 24 47 46 ...`
= "[44]er [48] [42]ent pour(00) que(46) [24] ce(47) que(46) ..."
- Right contact: "[42]ent pour que" — "pour que" is a verb-governing
  complementizer (purpose clause, requires a subjunctive verb downstream and
  a full clause upstream). "[S] [42]ent pour que ..." parses as 3pl matrix
  verb + purpose clause. This is the strongest verb-class contact in the set.
- Noun rival considered and rejected: the lane's noun+"pour que" parallels
  (noun-43 "la 43 pour que", noun-81 "le [81] pour [INF]") both carry
  determiners; here no determiner precedes 42 (48 = 'e'/verb-48, not a
  determiner), and a bare singular noun + "pour que" is ungrammatical.
- Left junction fenced (cause): the plural subject of "[42]ent" is not
  visible in-window ("[44]er [48]" span unresolvable; possible clause
  boundary before 48). The "pour que" government itself stands regardless.
- Score: PASS (verb-class government; one stated fence on the left).

**W4 @1188** (row a6_10): `... 06 59 [42 06] 84 59 46 ...`
= "... entent est(59) [42]ent on(84) est(59) que(46) ..."
- This window IS the second A1 grant window: 59->42 @1187 ("est [42]").
  A finite 3pl verb directly after "est" is ungrammatical in one clause.
- Per bar clause 2 the A1 grant is left intact: "est [42]" stays a
  predicative frame. The 06 here is therefore word-internal to the
  predicative unit "42ent" (adjectival "-ent", "présent"/"différent"-shaped)
  or a fenced clause-boundary junction — in neither case stem + inflection.
- Score: FAIL — fenced with cause (A1 window; the grant, not the stem
  reading, owns this contact; value-vs-frame tension escalated to red team,
  see Adverses).

**W5 @1815** (row a8_10): `... 93 50 [42 06] 29 37 01 ...`
= "[93] [50] [42]ent er(29) [37] [01] ..."
- Right junction "06-29" = "ent"+"er" = "enter": the word-internal rival
  "[42]enter" ("entrer"-shaped with clerk single-r spelling, cf. the lane's
  "prenent"/"pasent" single-consonant spellings) dissolves the
  stem+inflection boundary. The clause-boundary alternative
  ("[50] [42]ent. [X]er [37-01] ...", 37-01 the A12 unit) leaves both the
  subject ([50], unknown) and the boundary unprovable in-window.
- No verb-governor, no object, no visible subject anywhere in ±12.
- Score: FAIL — fenced with cause ("enter" junction resists the boundary;
  no verb-class contact shown).

**A1 grant check (clause 2):** 59->42 re-derived x2 on the repaired stream:
@464 "59 42 96" ("est [42] par(96) pour(00) [33]") and @1187 "59 42 06"
("est [42]ent on(84) ..."). Matches the A1 evidence ("59->42 x2"). Grant
left intact; not re-litigated.

**Global adverse context (42's contact profile, n=20):** 42->94 x3
(@494/@785/@1795) sits in the subject slot before "ne" ("[56] [42] ne
est(59) [37]" @1795: 42 as subject of "n'est [37]") — nominal contact,
tensions the verb-stem value. 29->42 x3 ("er"-contact) and 76->42 x3 are
unresolved. These do not reach kill grade (subject-slot reading is an
inference; 94='ne' is battery-promoted pending ratification) but they weigh
against promotion and feed follow-up val-42-nominal.

## Per-clause pass/fail

- Clause 1 (verb-class contact in >=3 of 5 windows): FAIL — 2/5
  (W1 @206 PASS, W3 @544 PASS; W2/W4/W5 fenced with stated cause).
- Clause 2 (A1 grant left intact): PASS — both 59->42 windows re-derived,
  grant not re-litigated.
- Clause 3 (bar's null path): TAKEN — the stem reading is fenced with
  stated cause (see per-window fences above).

## Adverses

(a) "TENSIONS A1-predicative-42 (frame grant, value open)": ANSWERED, not
    ignored. The grant stands (both windows re-derived). The tension is
    real and is fenced, not resolved: a verb-stem VALUE for 42 does not sit
    in the bare predicative window @464 ("est [42] par ..."), and at @1188
    the grant owns the contact. Value-vs-frame adjudication — including any
    positional/polyvalence reading, which per §7 only the red team can
    declare (67 is the sole true polyvalence) — is ESCALATED to the red
    team as a question, not decided here.
(b) 42->94 x3 nominal contact (@494/@785/@1795, subject slot before "ne"):
    recorded as an adverse against the verb-stem value; below kill grade
    (inference-dependent); feeds follow-up val-42-nominal.
(c) Dependency: 06='ent' is battery-promoted pending red-team ratification;
    if the red team revises 06, this battery's W1/W3 legs re-open.

## Verdict

**null** — Clause 1 fails at 2/5 (bar needs >=3). The stem reading is fenced
with stated cause per the bar's own alternative path: W2 forced non-verb by
33's dire/infinitive contact, W4 owned by the intact A1 grant, W5 dissolved
by the "enter" junction rival. Not kill: W3's "[42]ent pour que" is a genuine
verb-class leg (no window forces the claim false globally, no cleaner rival
value demonstrated on the same frames), and the A1 tension is a red-team
value-vs-frame question, not a battery-level kill. No standing red-team
verdict on 42's value exists; nothing here contradicts one.

## Follow-up targets (null regenerates work; 3 proposed)

1. **subj-42-w3** (priority 2): Harden @544's subject. Test the "[44]ere"
   hypothesis: 44-29-48 as "[44]"+"er"+"e" = feminine-plural noun in
   "-ères" ("manières"/"matières"-shaped) agreeing with 3pl "[42]ent"
   (44 already noun-shaped: "le 44" x2, "44 pour" x3). Bar: name the subject
   with agreement, or fence @544's left junction; either way @544's leg is
   adjudicated clean or conditional.
2. **val-42-nominal** (priority 2): Nominal-rival battery for 42. Frames:
   "42 ne" x3 subject-slot (@494/@785/@1795, incl. "[56] [42] n'est [37]"),
   "est [42]" x2 predicative (@464/@1187), 29->42 x3, 76->42 x3.
   Bar: name ONE nominal class (noun/adjective) covering >=4 of these
   frames with <=1 fence; discriminates directly against the verb-stem
   reading.
3. **w5-enter-junction** (priority 3): Adjudicate @1815's 06-29 junction.
   Test word-internal "[42]enter" (letter-spelling, "entrer"-shaped, clerk
   single-r as in "prenent"/"pasent") vs clause boundary
   ("[50] [42]ent. [X]er [37-01] ..."). Bar: one parse with stated subject
   or boundary; else fence 42-06-29 as word-internal, dissolving the stem
   window.
