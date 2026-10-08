# Battery report: noun26-1560-pas
Date: 2026-10-08. Worker: e066ba36-c9c4-4ae9-004c8174abd7.
Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json +
data/upstream-ct_R5005.txt), parsed like code/side-keyhunt/repair_parse.py.
canonical.py NOT used. R5005 untouched. All @-offsets are repaired-stream
pair indices (26 = @1560, 30 = @1561, row a8_01).
Target id: `noun26-1560-pas` (priority 2). Inherited from the noun-26 umbrella
null (2026-10-08); the positional rule ('26 = feminine noun iff preceded by
11=la, else verb-class') is standing context, NOT re-litigated here.

## Bar (verbatim from battery-queue.json)
"state ONE parse of repaired @1560 '...fois, la [26-noun] pas' under the positional rule (clause boundary before 'pas', or elliptical matrix licensed by the 1840s register), with 'pas' accounted; or record @1560 as the adjudication-grade residual for the red team with the exact unparsable span named"

## Bar as numbered pass/fail clauses (frozen before testing)
- Clause 1: state ONE parse of "...fois, la [26-noun] pas" under the
  positional rule with a clause boundary between @1560 (26) and @1561 (30),
  and 'pas' ACCOUNTED (a stated grammatical role in a licensed construction
  on the right side, not merely fenced as an unlicensed residual).
- Clause 2: alternatively, state an elliptical matrix licensed by the 1840s
  register that accounts for 'pas' after the noun.
- Clause 3: if neither disjunct pins 'pas' at battery grade, record @1560
  as the adjudication-grade residual for the red team with the exact
  unparsable span named (null-regeneration: 1-3 follow-up targets).

## Method
Re-derived @1560 on the repaired stream: @1556..1564 =
"61 40 17 11 26 30 06 60 71" = "[61]-e fois, la [26] pas [06] [60] [71]"
(40=e banked, 17=fois granted, 11=la banked). Stream-wide censuses on the
repaired parse: n(30)=19 with full windows; n(06)=44; '30 06' x4
(@1251/@1327/@1561/@1733); '30 06 60' x2 (@1561/@1733); '26 30 06' x2
(@1250 verb-branch/@1560 noun-branch); nearest upstream 94 for @1251/@1561/
@1733. Standing values only: banked pencil, granted/promoted set per
protocol §7 (30=pas battery-promoted, 12='n' letter-promoted, 94='ne'
battery-promoted pending red-team ratification). No other values assumed;
06, 60, 71, 50 unresolved.

## Window-level evidence (new, all re-derived on the repaired stream)
1. **Boundary 26|30 is forced, not chosen.** 26=noun forced by banked
   11=la ("11 26" exactly 2x stream-wide, both "...17 11 26"). The gapless
   mid-row sequence "11 26 30" (row a8_01, no row break) leaves two
   segmentations: (S1) boundary 26|30 — left "la [26-noun]", right
   "pas [06] [60]..."; (S2) "la [26-noun] pas" as one clause — ungrammatical
   ("pas" cannot right-adjoin to a nominal; the rival "pas" = noun "step"
   needs an absent determiner). S1 is the ONLY live segmentation.
2. **No 'ne' licenses 'pas' in the 26-clause.** Nearest 94 upstream of
   @1561 is @1549, inside the closed frame "00 46 70 12 94" (00=pour
   granted, 46=que banked, 70=pre banked, 12='n' letter) in row a8_00 —
   a different clause from the a8_01 "la [26]" clause (row boundary
   @1552|1553). The re-parse rival (11 as object pronoun + participle)
   is rejected: it contradicts banked 11=la and needs a subject plus 'ne'
   that are absent from this clause.
3. **The right-side fragment "30 06 60" is attested 2x stream-wide,
   independently of the noun crux.** @1561: "30 06 60 71 50 29...";
   @1733 (a8_07): "30 06 60 12 48..." following the pas-30 battery's
   "pas 15 01 56 pas" frame. At @1733 NO noun precedes, so the fragment's
   structure does not depend on @1560's "la [26]". 'pas' is structurally
   the fragment's head — but the fragment's CONSTRUCTION is undecided.
4. **The '26 30 06' trigram is the lane's minimal pair.** @1250:
   "67 46 26 30 06 65 46" ('que [26-verb] pas [06]...', verb branch,
   no 'ne' within 15); @1560: noun branch with forced boundary. Same
   surface trigram, both branches bare of 'ne'. Neither instance has a
   'ne' licensor — the bare-'pas' anomaly is NOT @1560-specific.
5. **06's value decides the construction and is contested.** Live
   hypotheses from standing work: 06="ne" (crib_surgeon H3, ratio+bigram
   checks passed) vs 06="de" (annealer letter-output) vs 06="ent"
   (formula_hunter R4, weak). If 06=de: fragment = "pas de [60]...",
   the 1840s-licensed elliptical "[il n'y a] pas de [60]". If 06=ne:
   "pas. Ne [new clause]" — 'pas' as standalone denial + new negation.
   The battery cannot select between them on standing evidence; asserting
   either would be invention (§3). Bare-'pas' fragment licensing is
   explicitly owned by queued `ne-alone-02-74` (status: queued).

## Per-clause pass/fail
- Clause 1 (boundary parse with 'pas' accounted): FAIL at battery grade.
  The segmentation is forced (evidence 1-2), but 'pas' is only assignable
  a STRUCTURAL role (head of the twice-attested "30 06 60" fragment,
  evidence 3) — its constructional licensing is undecided (evidence 5).
  A fence with better evidence than la-frames stated, but still a fence:
  not an accounting.
- Clause 2 (elliptical matrix): FAIL. No matrix is pin-able: every
  candidate ("[ce n'est] pas", "[il n'y a] pas de [60]") requires
  06/60/71 values that are open. Stating one would invent data (§3).
- Clause 3 (record the residual): PASS. @1560 is recorded as the
  adjudication-grade residual for the red team. **Exact unparsable span:
  @1561-1563 "30 06 60"** ('pas [06] [60]') — the bare-'pas' right-side
  fragment whose constructional licensing is undecidable at battery
  level (06 value contested de/ne; bare-pas fragment licensing queued
  under ne-alone-02-74).

## Adverses answered (none ignored)
- "'la [26]' banked article forces noun": HELD. 26=noun forced by banked
  11=la; re-parse rejected (evidence 2). Not re-litigated beyond the
  window: the positional rule stands as the null's stated context.
- "'pas' after a noun is the crux": FENCED with stated cause. Boundary
  26|30 forced by grammatical necessity (evidence 1); 'pas' = head of the
  "30 06 60" fragment attested independently of the crux (@1733,
  evidence 3); the fragment's construction is the fenced remainder,
  owned by queued ne-alone-02-74, not by this target.

## Verdict: NULL — headline: red-team-level contradiction, escalated
The battery cannot overwrite either of two standing red-team verdicts in
tension at this window, so per protocol it reports the tension instead:
- R17-011 GRANT: '26 30' x4 = "[verb] pas", re-derived INCLUDING @1560.
- R17-020: the positional rule GRANTED as finding (26=noun in
  '11 (02)? 26', verb elsewhere) — assigning 26=NOUN at @1560 under
  banked 11=la; declaration HELD "pending noun26-1560-pas (the @1560
  'pas' residual)".
The only live battery-level parse (forced boundary 26|30, bare-'pas'
fragment "@1561-1563" fenced) does not adjudicate between the two grants.
Red-team adjudication required: either the R17-011 "[verb] pas" grant is
scoped to exclude @1560, or the positional rule's noun assignment at
@1560 is revised. The battery declares nothing (protocol §7 respected).

## Follow-up targets (null-regeneration)
1. noun26-1560-06-value — bar: decide 06's class ("de" vs "ne" vs other)
   on the four '30 06' windows (@1251/@1327/@1561/@1733) plus the
   06→77 bigram and 06/77 ratio evidence; 06's value selects the residual
   fragment's construction ("pas de [60]"-ellipsis vs "pas. Ne [clause]").
   Resolves the licensing of the fenced @1561-1563 span.
2. noun26-1560-1733-fragment — bar: parse the @1733 "30 06 60 12 48"
   fragment (no noun crux; 12='n'/48='e' letters give a letter-level
   foothold: "pas 06 60 n e..."); whatever construction licenses the
   @1733 fragment licenses @1561's right side. Narrower than the bare-pas
   umbrella (ne-alone-02-74).
3. noun26-trigram-minimal-pair — bar: under the positional rule, the
   '26 30 06' trigram at @1250 (verb, no 'ne' in 15) vs @1560 (noun,
   forced boundary): state the constructional difference between the two
   branches or fence it with stated cause. Tests whether the rule's two
   branches license the same surface trigram differently.

## Standing constraints observed
- §7 respected: banked/granted values only; the sole-polyvalence rule
  untouched — nothing declared; noun-26 not re-litigated (positional rule
  used as stated context only).
- No standing verdict overwritten or downgraded; no data invented; every
  number re-derived on the repaired 1,847-pair parse.
- Lock created on start (locks/noun26-1560-pas.lock), deleted on
  completion per §6.
