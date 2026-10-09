# Battery report: 26-class-1754

- Target id: `26-class-1754`
- Claim: "26's class decides the @1754 3-way ambiguity (gerund / modal+infinitive / pronoun+finite-85)"
- Date: 2026-10-09
- Worker: battery worker (subagent 896960d5-2b03-4b08-8366-e19d571fcb1d)
- Stream: repaired 1,847-pair parse (`data/upstream-ct_R5005.txt` +
  `code/side-keyhunt/repaired_offsets.json`, parsed byte-exact per
  `code/side-keyhunt/repair_parse.py`; 1,847 pairs / 96 types re-asserted
  in-session). `canonical.py` never used. R5005, sealed gate instances,
  red-team adjudication queue untouched. The concurrent battery
  `58-complement-1695` (58 at @1695) was not duplicated: 58's class is
  named nowhere in this report.
- Lock: `code/crowd17/next-token/locks/26-class-1754.lock` (created at
  start, 2026-10-09T07:17:30Z; no prior lock existed; deleted on
  completion).

## Bar (verbatim, pre-registered BEFORE testing)

"name 26's class with the @1754 window's 3-way ambiguity resolving to one
parse; coordinate with the noun-26 batteries, do not duplicate"

Numbered pass/fail clauses (restated before testing, not modified after):

1. **C1:** 26's class at the @1754 window is named, with the naming
   instrument and its conditions stated.
2. **C2:** The @1754 window's 3-way ambiguity (per
   battery-24-en-verb-conflict C3: (a) gerund "[26] en [85] [58]";
   (b) modal "[26-subj] [24] [85-inf] [58]"; (c) pronoun+finite
   "[26-subj] en [85-finite] [58]") resolves to exactly one surviving
   parse.
3. **C3:** The analysis coordinates with the noun-26 batteries: decided
   and stated evidence is cited, not re-litigated; no noun-26 bar is
   re-run and no noun-26 window is duplicated.

## Method

1. Re-derived the repaired stream byte-exact per `repair_parse.py`
   (1,847 pairs / 96 types asserted). All @-offsets below are 0-based
   repaired-stream pair indices.
2. Extracted the window @1748–@1760 and re-derived the full 26 census
   (n=17) with predecessors, to apply the stated positional rule at
   @1753 without re-running the noun-26 umbrella bar.
3. Applied each of the three pre-adjudicated parses to the named class.
   A parse is dead iff its stated grammatical condition fails under
   standing values (same kill logic as the parent battery:
   24-en-verb-conflict).
4. Standing inputs (cited, not re-litigated): the stated positional rule
   (26 = feminine noun iff preceded by 11=la, else verb-class;
   battery-noun-26, NULL, escalated to red team); A2 23~26 SPLIT;
   noun26-89-class (2026-10-09, PROMOTE, conditioned split; @1752's 89
   = noun arm, conditional on provisional 77='le'); 24='en' survives at
   @1754 (24-en-verb-conflict C3, 'en' parses there; @1754 is not in the
   C1 'en'-kill set); 85 verb-stem frame (A3); banked pencil values;
   provisional 77='le'.

## Window-level evidence

Target window (row a8_08, 0-based), re-derived:

| @ | 1748 | 1749 | 1750 | 1751 | 1752 | 1753 | 1754 | 1755 | 1756 | 1757 | 1758 |
|---|------|------|------|------|------|------|------|------|------|------|------|
|   | 65   | 34   | 07   | 28   | 89   | 26   | 24   | 85   | 58   | 17   | 78   |

So the 24-85 bigram is 24@1754–85@1755, with 26@1753 before it and
58@1756 after (the task's "@1756" is this same window, 58-indexed).

26 census check (n=17, re-derived; predecessors): 02@129, 84@155,
11@240, 69@406, 64@531, 39@601, 24@655, 94@842, 69@934, 24@992,
46@1250, 38@1470, 11@1560, 69@1628, 88@1707, 89@1753, 64@1769.
The only la-window predecessors are @129 ('11 02 26'), @240
('11 26'), @1560 ('11 26'). At @1753 the predecessor is 89, not 11 —
verb-branch under the stated positional rule. This matches the
umbrella's 14-window verb-branch census exactly (no new window, no
contradiction).

Parse adjudication at @1754 (24@1754, 85@1755):

- **Parse (a) gerund: "[26] en [85] [58]" — SURVIVES.** Conditions:
  26 non-nominal (verb-class named below); 24='en' pronoun must
  immediately precede a verb — 85 is A3 verb-stem, and the en85
  gerund CONFIRM is undisturbed here; @1754 is not in the C1
  'en'-kill set ({@162, @1774, @1486, @190, @643, @823}), so 'en'
  survives at this window per the parent battery's definite
  window-level finding. Full read: "[89-S?] [26-V] en [85-gérondif]
  [58-complément]". 58's complement role is consistent with the
  sister-window finding (24-en-verb-conflict C4: 58 in complement
  position at @1695); 58's class itself is the concurrent battery's
  domain and is not adjudicated here.
- **Parse (b) modal: "[26-subj] [24] [85-inf] [58]" — DEAD.** Its
  stated condition is "iff 26 nominal": the finite modal 24 needs an
  overt subject (French has no pro-drop; parent battery C2), and 26
  is the only subject candidate in the window. 26 is verb-class
  (C1), not nominal — no subject for 24. Rescue via 89 as subject
  of 24 ("[89-S] [26-V] [24-modal]"): ungrammatical — 26 is a finite
  verb between 89 and 24, and 24 cannot reach across it. Dead.
- **Parse (c) pronoun+finite: "[26-subj] en [85-finite] [58]" —
  DEAD.** Same stated condition: needs 26 nominal as subject of
  finite 85. 26 is verb-class. Dead.

Fenced with stated cause (not a live fourth parse): the
"l'en"+finite-85 variant (cf. en85's fenced ambiguity at @732)
needs the l' to elide onto the left neighbor — at @732 that was the
literal 11='la'; here the left neighbor is 26 (verb-class, value
unnamed), so the elision needs unevidenced phonetics of 26. Not
battery-grade; excluded.

## Per-clause pass/fail

1. **C1: PASS.** 26's class at @1753 = **verb-class** (verb-branch of
   the stated positional rule: left neighbor 89, not 11=la; the 3
   noun windows are all and only the la-windows @129/@240/@1560;
   14/17-window verb-branch census re-derived and matching). Naming
   instrument condition stated: the positional rule is STATED and
   escalated to the red team (battery-noun-26 NULL), not declared —
   per §7 a second polyvalence for 26 is a red-team act. This verdict
   inherits that pending status; if the red team replaces the rule,
   this verdict re-opens.
2. **C2: PASS.** Exactly one parse survives: the gerund (a). The two
   nominal-subject parses (b) and (c) die on the class assignment;
   no rescue under standing values. The 3-way resolves to one.
3. **C3: PASS.** Decided/stated evidence cited, none re-litigated:
   the positional rule (battery-noun-26), the 89 noun arm
   (noun26-89-class), the @1754 'en'-survival and parse enumeration
   (24-en-verb-conflict C3), the A3 85-frame. No noun-26 bar was
   re-run; the only new window work is the @1754 parse adjudication,
   which no noun-26 battery performed.

## Adverses answered

- "23~26 SPLIT granted (A2) — no homophone rescue via 23": ANSWERED.
  Respected throughout; no homophone rescue was attempted and 23
  plays no role in any parse. The split is untouched.

## Verdict: PROMOTE (finding grade — conditional on the stated positional rule)

26's class at the @1754 window is verb-class, and that single class
assignment resolves the window's 3-way ambiguity to one surviving
parse: the gerund "[26] en [85] [58]" ("[89-S?] [26-V] en
[85-gérondif] [58]"). The modal and pronoun+finite parses both need
26 nominal and are dead. Downstream: @1756's 58 now sits in the
complement slot of a resolved gerund frame (input to the concurrent
58-complement-1695 battery and to 24-redteam-adjudication).

Caveats (stated, not hidden): (i) the class naming is load-bearing on
the stated positional rule, which awaits red-team declaration (§7);
(ii) 26's subject slot in the surviving parse is 89 per
noun26-89-class's noun arm, conditional on provisional 77='le' — if
that arm falls, the subject is a stated residual owned by the noun-26
follow-ups, but the parse-kill conclusion (b) and (c) dead) does not
depend on it; (iii) 58's complement role is consistent-but-unadjudicated
here (concurrent battery's domain).

No follow-ups required for a promote. Natural next consumers (already
queued/running elsewhere): 24-redteam-adjudication (the 24 conflict),
58-complement-1695 (58's class), noun26-la-frames / noun26-gov-frames
(the rule's remaining queues).

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-26-class-1754.md` (this file).
- Queue: `26-class-1754` queued → verdict/promote via temp-file +
  rename, own entry only; pre-write assert confirmed no prior verdict
  (status was `queued`, verdict JSON null); JSON re-validated
  post-write; evidence and adverses preserved, new evidence appended.
- Lock deleted on completion (verified gone).
- R5005, sealed gate instances, red-team adjudication queue untouched.
- No standing or red-team verdict contradicted, downgraded, or
  re-litigated; §7 sole-polyvalence respected (rule stated, not
  declared).
