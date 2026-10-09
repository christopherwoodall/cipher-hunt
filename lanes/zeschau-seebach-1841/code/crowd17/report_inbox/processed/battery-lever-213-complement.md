# Battery report: lever-213-complement

Target: `lever-213-complement`
Claim: "@213 '74 lever 06' resolves the 06-complement problem"
Date: 2026-10-08
Worker: 4e9914cd-d562-43dc-9d9a-7e79d306fc2a
Lock note: no stale lock for this id (locks/ held only sibling workers' locks at start); created locks/lever-213-complement.lock 2026-10-09T01:51:22Z, deleted on completion.

CONDITIONALITY (protocol §7): the 77-78 = "lever" composition is the CONDITIONAL
premise of this battery, inherited from the lever-77-78 NULL (2026-10-08). This
report tests the claim UNDER that premise; it does not promote, demote, or
re-open the lever composition itself, and it does not contradict that NULL
(it converges with its @213 soft-fail).

## Bar (verbatim from battery-queue.json)

"(1) ONE grammatical parse of @213-216 with 77-78='lever' and 06 complement-shaped, OR confirm the 06-59 'V-este' verb-unit forces a clause boundary after 'lever' and state whether absolute 'lever' is licensable; (2) cite F52-L2 and ISLET-10, do not re-litigate them; (3) test 06='/ɑ̃/'-adverbial and a 06-nominal islet as rival integrations"

## Numbered clauses (fixed before testing)

1. (a) ONE grammatical parse of @213-216 (actual stream offsets: 77@213,
    78@214, 06@215, 59@216 — see offset note below) exists with 77-78 = "lever"
    and 06 complement-shaped; OR (b) the 06-59 "V-este" verb-unit forces a
    clause boundary after "lever", AND the report states whether absolute
    "lever" is licensable.
2. F52-L2 and ISLET-10 are cited for what they stand for; neither is
    re-litigated.
3. Two rival integrations of 06@215 are tested and pass/fail with stated
    cause: (i) 06 = "/ɑ̃/"-adverbial; (ii) a 06-nominal islet.

Offset note: the target's evidence gloss "@213-216 '74 77 78 06 59 46'" is
anchored on the lever window's 77-cell. Re-derived byte-exact from the repaired
stream: 74@212, 77@213, 78@214, 06@215, 59@216, 46@217, 29@218, 42@219
(a2_00->a2_01). The lever-77-78 report's "@213" window text ("74@213 … 59@217")
is off by one against the repaired stream; the cells are the same physical
window. All @-offsets below are repaired-stream pair indices.

## Method

Repaired 1,847-pair stream only: code/side-keyhunt/repaired_offsets.json over
data/upstream-ct_R5005.txt, parsed byte-exact like
code/side-keyhunt/repair_parse.py (`[s[i:i+2] for i in range(o, len(s)-1, 2)]`).
code/side-keyhunt/canonical.py never used. R5005 untouched. No invented data.
Standing values used (§7): banked GT 11=la, 70=pre, 82=m, 34=i, 29=er, 40=e,
46=que; promoted 87=ce, 64=qui, 96=par, 17=fois, 79=tout, 00=pour, 84=on,
47=ce; provisional 59=est, 77=le.

## Standing citations (clause 2)

- **F52-L2** (as dissolved/refined by the 59-conditioner round-10 work; cited,
  not re-litigated): F52's leg L2 honestly FAILED on S4#1 (@216) — "«[06] est
  que» had no licensed frame"; per L2's own bar, 06 is verb-stem-class and
  NON-NOMINAL, and 06 non-nominal kills the "NP est que" cleft frame at @216.
  (code/crowd10/report_inbox/conditioner59-59battery.md, ll.29-32; ISLET10-PROPOSAL.md l.46.)
- **ISLET-10** (red-team R10: GRANT-WITH-MODIFICATION as LEAD; R11/R12: HOLDS;
  cited, not re-litigated): @216 classified ESTE in classification.json —
  "pre=06 verb-stem-class: '[06-59] que' verb+que-clause; cleft 'NP est que'
  hostile (06 non-nominal, F52-L2)". Window note (ISLET10-PROPOSAL.md):
  @213-219 = "77-78-06-[59]-46-29-42" = «le [78] [V-este] que er[42]…»
  ("que er" wrinkle: clause after «que» unparsed; core "[V] que" grammatical).
  Conditioning rule (GRANTED): 59 reads word-"est" iff pre(59) ∈ {64,94,93};
  pre(59@216)=06 is excluded — the est-arm is unavailable here. 59's value is
  conditioner59's lane; this battery uses only the granted conditioning rule.

## Window-level evidence (@-offsets, repaired stream)

### The frame
@208-224: `44 50 88 19 [74] 77 78 06 59 46 29 42 16 24 89 61 96`
Left: …44@208 50@209 88@210 19@211 | 74@212 | 77@213 78@214 | 06@215 | 59@216
| 46@217 | 29@218 42@219 16@220 24@221 89@222 …

### Slot analysis for 06@215 under the lever premise

Candidate integrations for 06@215, tested against standing lane law:

**(i) 06 as nominal complement (object) of "lever"** — FAIL (hostile).
F52-L2: 06 is verb-stem-class, non-nominal; the non-nominal classing kills the
nominal slot at exactly this window (the cleft kill). Stream-wide, only two
article-before-06 frames exist ("11-06" @270, "93-06" @1761); at @215 the left
context is 78 (under the conditional premise: "lever" itself — a verb; under
the F2 analytic rival: the "ver" stem) — no nominal-licensing frame exists
locally. Hostility is L2's standing ruling, cited not re-litigated.

**(ii) 06 as /ɑ̃/-adverbial (clause-3 rival (i))** — FAIL (tested, cause stated).
The crowd4 compositional "-ment" route needs 82-06 (82="m'" carrier); 82-06
bigrams exist at @579/@737/@1183/@1354 only — pre(06@215)=78, so the carrier
is absent. A freestanding 06=/ɑ̃/-adverbial ("[lever] …-ment") after the
infinitive would leave 59@216 unparsed: 59's only licensed arms at pre=06 are
the [06-59] ESTE verb-unit (ISLET-10, GRANTED-lead) or leftover — both exclude
a freestanding adverbial 06. The adverbial hypothesis therefore strands 59
with no licensed parse. Convergent: the ent-06 battery found ZERO clean
fork-A (adverbial) windows stream-wide.

**(iii) 06-nominal islet (clause-3 rival (ii))** — FAIL (tested, cause stated).
No standing 06-nominal islet exists anywhere in the lane; the hypothetical
integration (06 as nominal object of "lever") fails locally per (i) above and
is barred by F52-L2 standing law (cited, not re-litigated). 06's n=44 profile
is verb-stem-class end-to-end (crowd3 polyvalence demoted to PLAUSIBLE;
crowd3 red team KILLED the /mɑ̃/-specific "demand-/command-" claim; ent-06
found clean "ne mentent" x2 @578-581/@1182-1185 — verb endings, not nouns).

**(iv) 06 bound into the [06-59] "V-este" verb-unit (ISLET-10, GRANTED-lead)**
— LICENSED, and it forces a clause boundary. This is the ONLY standing-law
integration of 06@215: "...[74] lever | [06-59] que [29=er] [42]…". 06-59 is
one bisyllabic verb-unit (este-arm, n_eff=8 lane-wide); 06 cannot
simultaneously serve as lever's complement. The boundary is forced, not
optional.

### The boundary and absolute "lever"

Under (iv), "lever" stands absolute (no complement): "…[74] lever. [V-este]
que er[42]…". Is absolute "lever" licensable? NO. French "lever" is
transitive; the intransitive is pronominal ("se lever") and the absolute is
ungrammatical. No reflexive "se" is present or granted anywhere in the
lane's value set (47="ce" promoted, allophone tier; no "se" banked,
provisional, or battery-promoted). No intransitive-"lever" frame is granted
in §7 or in any battery report. The stranded-"lever" parse is therefore
ungrammatical French.

### Clause-1 verdict on this window

- Disjunct (a) — ONE grammatical parse with 77-78="lever" and 06
  complement-shaped: FAIL. Every candidate slot for 06 fails: nominal (i,
  hostile per F52-L2), adverbial (ii, strands 59), nominal islet (iii,
  nonexistent + barred). No other complement shape is licensed for 06
  (predicative frames are granted only for 37/32/42; verb-verb needs a
  preposition — none present).
- Disjunct (b) — boundary forced + licensability stated: CONFIRMED. The
  [06-59] V-este unit (ISLET-10, GRANTED-lead) forces the clause boundary
  after "lever"; absolute "lever" is NOT licensable.

Net: under the conditional lever premise, the @213-216 frame admits NO
grammatical parse. The 06-complement problem is not resolved — it is shown
to be unresolvable within standing lane law: the sole licensed 06
integration strands an ungrammatical absolute "lever".

## Per-clause pass/fail

1. **PASS on (b) / FAIL on (a) — net FAIL for the claim.** The boundary is
   confirmed forced by the ISLET-10 [06-59] V-este unit; absolute "lever" is
   not licensable; disjunct (a)'s grammatical parse does not exist. The claim
   ("resolves the 06-complement problem") is false at this window — the
   window forces the claim false.
2. **PASS.** F52-L2 and ISLET-10 cited with exact standing (above); neither
   re-litigated.
3. **PASS (both tested, both FAIL with stated cause).** 06=/ɑ̃/-adverbial:
   carrier 82 absent at @215 (82-06 only @579/@737/@1183/@1354); freestanding
   adverbial strands 59@216 (59's only licensed arm at pre=06 is the ESTE
   unit); ent-06 found zero clean fork-A windows. 06-nominal islet: no such
   islet exists; local left context (78) licenses nothing nominal; barred by
   F52-L2 standing law.

## Adverses answered

- **Strain shared with F2 ("le ver 06" identical problem) — non-discriminating:**
  CONFIRMED non-discriminating and fenced with stated cause. Under the F2
  analytic reading the frame is "le [78=ver-stem] 06 [59]…": 06 is equally
  verb-stem-class, equally non-nominal, and equally bound into the same
  [06-59] V-este unit — the integration deadlock is identical. This battery's
  kill is of the conditional claim, not of the lever-vs-F2 composition
  question; the lever-77-78 NULL (which fenced @213 as a shared-strain
  soft-fail) is untouched and convergent.
- **59's est-arm status is conditioner59's lane, not this battery's:**
  RESPECTED. 59's value was not tested, promoted, or killed; only the GRANTED
  conditioning rule (59=est iff pre∈{64,94,93}) was used to exclude the est-arm
  at pre=06. No sealed or red-team matter touched.

## No red-team contradiction

This result reinforces every standing red-team verdict it touches: ISLET-10
(GRANTED-lead, R10/R11/R12) is the mechanism that forces the boundary;
F52-L2 is cited as standing; the lever-77-78 NULL's @213 soft-fail is
convergent (this battery upgrades the shared-strain observation to a
claim-level kill); unconditioned 59="est" stays REFUTED (kill-grade, R10);
no existing verdict downgraded.

## Verdict: KILL

The claim "@213 '74 lever 06' resolves the 06-complement problem" is killed
at kill grade: the @213-216 window forces the conditional claim false —
exhaustive slot analysis of 06@215 under standing lane law admits no
complement-shaped integration (nominal: hostile per F52-L2; adverbial:
tested and failed, strands 59; nominal islet: nonexistent and barred), and
the sole licensed integration (ISLET-10 GRANTED-lead [06-59] "V-este"
verb-unit) forces a clause boundary that strands an unlicensable absolute
"lever" (French "lever" is transitive; no reflexive or intransitive frame
is banked, granted, or provisional in the lane). The 06-complement problem
is not resolved at this window; it is demonstrated unresolvable under the
lever premise. No cleaner rival value was needed or demonstrated — the
kill rests on the compositional premise's own grammar.

Note on scope: this kills the conditional claim only. It does NOT decide
whether 77-78 = "lever" (that NULL stands), does NOT decide F2, and does
NOT touch 59's value or ISLET-10's status.

## Open leads (not pre-registered follow-ups; for supervisor triage)

- L1: era gate for absolute-"lever". The unlicensability judgment is French
  grammar; the lane never ran an era-frequency gate on bare transitive verbs
  ("lever" without object vs "se lever"). A Nesselrode-v8/F33-style gate
  ("absolute lever" era-0 vs pronominal) would harden the kill — or, if era
  attests it, force a re-open. Narrow bar: count "lever"+no-object windows
  in era French.
- L2: the ISLET-10 "que er" wrinkle at @216-219 ("[V-este] que er[42]…",
  post-que clause unparsed) stays open; if the post-que clause ever parses
  with 42 as a licensable predicate, the stranded-lever reading gains a
  possible re-parse route ("lever [que-clause]"?). 42's value work owns this.
- L3: the F2 analytic twin ("le ver 06 [V-este]") inherits this exact kill —
  the 06-integration deadlock is composition-independent. If any future
  battery resolves 06's slot at @215 (e.g. a 06 value the ent-06 work has not
  yet tested), both lever-213 and the F2 frame re-open together.

## Constraints respected

R5005, sealed gate instances, and the red-team adjudication queue untouched.
§7 banked/promoted/provisional/killed/split/held values respected; 67
et/veut sole polyvalence untouched; 1690 uniformity rule untouched. No value
promoted or killed beyond this target's own claim. canonical.py never used.
