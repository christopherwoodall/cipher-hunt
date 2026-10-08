# Battery report: donne-168-708-leg — "donne" 2-window leg @168/@708

Worker: worker-agent-8ce4dc61. Date: 2026-10-08.
Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json +
data/upstream-ct_R5005.txt, parsed per code/side-keyhunt/repair_parse.py;
[tokenizer byte-exact: [s[i:i+2] for i in range(o, len(s)-1, 2)] per row]).
Lock: created locks/donne-168-708-leg.lock 2026-10-08T23:09:57Z; no prior
lock existed (fresh run, no stale-lock takeover).
Bar source: battery-queue.json target donne-168-708-leg (priority 2, status
queued at run start; confirmed). Bar copied verbatim before testing; numbered
clauses below are the same bar, not a rewrite.

## Bar (verbatim from battery-queue.json)

"leg iff 'on donne 21' and '35 donne 71' parse with 21/71 named"

## Bar as numbered clauses (pre-registered before testing)

1. "'on donne 21' @168 parses with 21 named" — the window parses
   grammatically under standing values AND a value is attached to 21.
2. "'35 donne 71' @708 parses with 71 named" — the window parses
   grammatically under standing values AND a value is attached to 71.

Adverses (from queue): "leg does not decide 53's profile; 21/71 unnamed".

## Method

Re-derived both windows fresh on the repaired stream. Re-enumerated the
53-12-48 trigram globally. Enumerated 21 (n=30), 71 (n=7), and 35 (n=10)
contact profiles fresh. Standing values used: 84="on" (A15 granted),
12="n" and 48="e" (promoted letters, n-e-12-48 battery). §7 obeyed: no new
polyvalence declared; 67 remains the sole true polyvalence. The leg does
not re-litigate prof-53 (53-12-41/44 explicitly out of scope, fenced to
queued donn-41-44); prof-53's null verdict in battery-queue.json is not
touched by this battery.

## Window-level evidence (@-offsets are pair indices on the repaired stream)

- @168 (a1_05): `... 87 11 24 82 84 | 53 12 48 | 21 60 09 87 ...`
  = "ce(87) la(11) [24] m(82) on(84) donne(53-12-48) 21 ...". Full frame
  @162-174: 24 87 11 24 82 84 53 12 48 21 60 09 87.
- @708 (a5_01): `12 66 21 35 | 53 12 48 | 71 12 63 00 ...`
  = "... 21 35 donne(53-12-48) 71 ...". Full frame @702-714:
  98 20 12 66 21 35 53 12 48 71 12 63 00.
- 53-12-48 trigram census on the repaired stream: exactly 2x, @168 and
  @708. No other instance; the leg covers the full trigram population.
- 21 (n=30): predecessors 96x3/33x3/83x3/11x2/68x2/48x2/01x2/06x2/61x2;
  successors 67x8/62x5/60x4/65x4/64x2. Object-slot instance @168 ("donne
  21"); @231 "96 21 60 71" (21-60-71 adjacency, same-row formula neighborhood).
- 71 (n=7): predecessors 60x2/63/48/65/86/83; successors 51/10/12/17/64/50/48
  — all singletons, zero repeated frame. Object-slot instance @708
  ("donne 71"); @233 "60 71 51" (60 before 71 x2/7, the only repeated contact).
- 35 (n=10): @707 is the leg subject slot; other frames "59 35 94" x2
  (@1292, @1805), "26 35 58 35 93" @156-160 (doubled), "35 56 12" @1639.
  35's class is open; the @708 leg reading requires a singular subject.

## Per-clause pass/fail

1. "'on donne 21' @168 parses with 21 named":
   - Parse half: PASS. Under 84="on" (granted) and 12="n"/48="e"
     (promoted), "84 53-12-48" reads "on donne" cleanly — compositional
     53="don"+12="n"+48="e"; no contradiction at the window. Re-derives
     prof-53 W3 (@168) on the repaired stream, independently confirmed.
   - Naming half: FAIL. 21 is unnamed in every standing battery (value
     open). Its profile (n=30, suc 67x8/62x5/60x4/65x4) supports no value
     at promote-grade; no candidate reaches >=2 independent grammatical
     frame-legs on the repaired stream. Clause 1 not met in full.
2. "'35 donne 71' @708 parses with 71 named":
   - Parse half: PASS (conditional). "35 donne 71" is grammatical provided
     35 is a singular subject and 71 a noun/direct object; nothing at the
     window or in 35's census contradicts that. Re-derives prof-53 W6
     (@708), independently confirmed.
   - Naming half: FAIL. 71 n=7, seven distinct successors, zero repeated
     frame; no value can be attached at promote-grade. Clause 2 not met in
     full.

Adverses answered/fenced:
- "leg does not decide 53's profile": ANSWERED by scope discipline — this
  battery tested only the two leg windows; prof-53's null verdict stands
  untouched; 53-12-41/44 left to queued donn-41-44. The leg's 'donne'
  reading at @168/@708 is confirmed leg-local, not a profile claim.
- "21/71 unnamed": NOT answered — 21 and 71 cannot be named at
  promote-grade on current evidence. This is the blocker; per §4 a promote
  is unavailable (not all adverses answered), and no kill-grade failure
  exists (no window forces the claim false, no cleaner rival on the same
  frames). Hence null.

## Verdict: null

Both leg windows parse cleanly under standing values (the compositional
'donne' reading re-derives independently on the repaired stream, and the
53-12-48 trigram occurs exactly twice — the two leg windows). But the
bar's naming requirement is unmet: 21 and 71 are both unnamed in the
standing record, and neither can be named at promote-grade from the data
this battery could see. Nothing contradicts a standing red-team verdict;
no verdict is downgraded; sealed gates and the adjudication queue
untouched.

No contradiction with prof-53 (battery null, W3/W6 clean re-derived).

## Follow-ups (null regenerates work)

1. **name-21-obj** (priority 2): name/class 21, the object slot at @168.
   Bar: resolve iff 21's class is stated (noun? clitic? adverb?) with >=3
   frame-legs, then a value with >=2 independent grammatical frames and
   zero contradictions. Evidence: 21 n=30 on the repaired stream;
   predecessors 96x3/33x3/83x3, successors 67x8/62x5/60x4/65x4;
   "donne 21" @168 (object slot), "21 60 71" @231. Adverses: 21's value
   open; 67-positional rule may interact via "21 67" x8.
2. **name-71** (priority 3): name 71, the object slot at @708. Bar:
   resolve iff a value is attached with >=2 frame-legs; fence as residual
   if the data stays thin. Evidence: 71 n=7; successors all singletons
   (51/10/12/17/64/50/48); "donne 71" @708; "60 71" x2 (@233, @1564).
   Adverses: thin data; value fully open.
3. **prof-35** (priority 3): name/class 35, the subject of "donne" @708 —
   if 35 proves plural, the 'donne' singular reading breaks (leg-grade
   kill path). Bar: resolve iff 35's class is stated with the @707-711
   subject slot parsing; else fence 35 as the blocker, not the leg.
   Evidence: 35 n=10; "59 35 94" x2 (@1292, @1805), "26 35 58 35 93"
   @156-160 doubled, "35 56 12" @1639. Adverses: 35's class open;
   'donne' agreement conditional on singularity.
