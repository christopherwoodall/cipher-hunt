# Battery report: class-27-independent

- Target id: `class-27-independent`
- Claim: "class 27 from its single window grammar alone (nominal/adverbial/adjunct arms armed by neighbors only); the only battery-grade way to unblock the hapax fence"
- Date: 2026-10-09
- Worker: battery worker (subagent 2da253ba-772b-4ede-b9ba-a9130bd1d0a4)
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` +
  `code/side-keyhunt/repaired_offsets.json`, parsed per
  `code/side-keyhunt/repair_parse.py`; asserts 1847 pairs / 96 types held
  in-session). `canonical.py` never used. R5005, sealed gates, red-team
  adjudication queue untouched.

Terms (ASD-STE100): "frame-leg" = a licensed grammatical frame in which the
target group occupies a class-specific slot, every element of the frame
carrying a standing lane license (granted/promoted/battery-grade) with zero
ungranted assumptions. "Hapax" = a group occurring exactly once stream-wide.

## Bar (verbatim, pre-registered before testing)

"resolve iff 27 takes one class with >=1 frame-leg at battery grade; else
fence the hapax with stated cause"

Numbered pass/fail clauses (restated before testing, not modified after):

1. **C1 (resolve arm):** 27 takes exactly one class (nominal, adverbial, or
   adjunct), supported by >=1 frame-leg at battery grade — i.e. a licensed
   frame whose other elements need zero ungranted assumptions, and the rival
   classes are excluded or unevidenced at battery grade.
2. **C2 (fence arm):** else, fence the hapax with stated cause — which arms
   survive, which die, and what assumption each survivor needs.

Adverses: none listed on target. §7 intact; no standing verdict touched.

## Method

1. Read BATTERY-PROTOCOL.md first. Created
   `code/crowd17/next-token/locks/class-27-independent.lock` on start
   (agent id + 2026-10-09T18:20Z); no prior/stale lock; deleted on completion.
2. Re-derived the repaired stream byte-exact in-session; censused group 27.
3. Adopted standing record (not re-litigated): 79="tout" granted (A5);
   94="ne" LEAD (registry ["ne","lead"]); 46="que" GT; 24 verb class-level
   (registry ["verb","cls"]; finite per ne-24-profile); 58 nominal
   class-level (registry ["nominal","cls"]); 93 verb class-level; 14="en"
   battery PROMOTE pending ratification (en14-value-tighten); 60 verb-class
   battery-grade, value open (split-60-verbs PROMOTE, finding grade);
   "tout en [60]" licensed gérondif at battery grade (gerund-60-1688
   PROMOTE, 2026-10-09); gérondif model "en [stem]", -ant unspelled
   (en85-gerund-reaudit PROMOTE); 58="ant" KILLED (ant-58-ending);
   62 value open ("il" killed R19-106/R20-125); 85/15/23 value open;
   "ne…que" bracket's verb slot empty at this locus (frame-1688-wide NULL).
4. Armed the three class hypotheses against the single window using only
   neighbor licenses.

## Locus census (byte-exact)

n(27) = **1** stream-wide: 0-based @1691, row a8_05.
±6 context: `93 62 94 79 14 60 [27] 46 24 85 58 15 23`
(@1685–1697).

The licensed matrix parse is now: "…[62] ne(94) tout(79) en(14)
[60-gérondif] [27] que(46) [24] [85]…" — the H-14 route re-opened by
gerund-60-1688 with 27 as sole open, exactly the state this target was
built for.

## Class-arm tests

### Arm N — nominal (27 = noun)

- **N1 (direct object of the gérondif):** "en [V-gér] [27-N]" ("en prenant
  [N]"). Grammatically licensed shape. Needs the ungranted assumption
  **"60's verb is transitive"** — 60's value is open and no battery-grade
  transitivity finding exists for the bare-60 item (split-60-verbs names no
  value; gerund-60-1688's "-dre family" characterization does not by
  itself license transitivity). → live, unforced, one ungranted assumption.
- **N2 (antecedent of que-relative):** "[27-N] que [24-fin]…" ("the [27]
  that [24]s"). The "ne…que" reading is dead (no finite verb between 94
  and 46), so 46=que introducing a clause must be relative or
  complementizer; with no matrix verb for a complement, relative is the
  only live reading — but it still needs 27 nominal (the conclusion under
  test) AND a matrix role for 27, which collapses to N1 (object of
  gérondif, needs 60 transitive). → not independent; same assumption.
- **N3 (subject of 24):** order is 27–46–24; 27 cannot be the que-clause
  subject across the complementizer. → dead.

Arm N: no battery-grade frame-leg (every leg needs ≥1 ungranted
assumption).

### Arm A — adverbial (27 = adverb)

- **A1 (manner adverb):** "en [V-gér] [27-adv]" ("en marchant vite").
  Grammatically licensed with zero new assumptions beyond the adopted
  gerund-60-1688 promote. → live, unforced.
- No distributional evidence exists either way (hapax). Mere grammatical
  possibility is not a battery-grade frame-leg: nothing positively
  indicates the adverb class.

Arm A: live but unevidenced; no battery-grade frame-leg.

### Arm J — adjunct (27 = adjunct / prepositional)

- **J1 (bare adjunct before que):** "…[27] que [24]…" as bare temporal /
  locative adjunct is ungrammatical without pause in 1841 French. → weak.
- **J2 (preposition heading "pour que"):** "[60-gér] [27=prep] que
  [24-subj]" ("while V-ing, so that…") is a conceivable shape, but needs
  24 subjunctive (mood open) and a second "pour"-valued cell beside
  granted 00="pour" (homophony unlicensed). → unevidenced, two
  assumptions.
- **27 as spelled -ant ending ("60"+"27"):** excluded — the adopted
  gérondif model spells "en [stem]" with -ant unspelled, and 58="ant" is
  KILLED; no license for a spelled ending. → dead.

Arm J: no battery-grade frame-leg.

## Per-clause pass/fail

1. **C1: FAIL** — 27 does not take one class. Two arms are grammatically
   live (nominal N1/N2, adverbial A1) and neither is forced: the nominal
   legs each need the ungranted "60 transitive" assumption, and the
   adverbial leg has zero positive evidence (possibility ≠ battery
   grade). No frame-leg at battery grade exists for any class.
2. **C2: FIRES (executed)** — the hapax is fenced with stated cause: a
   single window whose every class arm needs ≥1 ungranted assumption
   (nominal) or is purely possible-but-unevidenced (adverbial), with the
   adjunct arm weak-to-dead. The gerund-60-1688 promote re-opened the
   H-14 route but does not by itself class 27; 27 remains the sole open
   of the complement, exactly as the parent battery left it.

No standing or red-team verdict contradicted or downgraded; §7 intact.
Canonical-stream caveat stands (row a8_05 offset unvalidated — under a
rival offset the locus dissolves, consistent with the fence, not a
rescue).

## Verdict: NULL (fence executed)

## Follow-ups proposed (all verified ABSENT from battery-queue.json;
`val-27-1691-np` already queued — not re-proposed)

1. `trans-60-1690` (P3) — test the bare-60 verb's transitivity at @1690
   (the -dre family). A transitive-60 licenses the nominal-27
   direct-object frame ("en [V-gér] [27-N]") and gives 27 its first
   battery-grade frame-leg. Bars: transitive iff ≥2 independent
   object-taking windows at battery grade; else the N1 leg stays
   assumption-bound.
2. `que-1692-relative-test` (P3) — test whether "que [24] [85]…" at @1692
   parses as a relative clause (24 finite + mood; 85/58 as its
   dependents). A relative reading forces 27 nominal (antecedent) — the
   forcing leg this battery could not supply. Bars: relative iff the
   clause parses with zero ungranted assumptions besides 27's class.
3. `prep-27-pourque-test` (P4) — test the purpose-clause reading
   "[60-gér] [27=prep] que [24-subj]" (J2). Bars: needs 24 subjunctive
   mood licensed at battery grade; kill the arm iff 24's mood is
   incompatible or no second "pour"-valued cell is licensable.

## Bookkeeping

- Report: this file
  (`code/crowd17/report_inbox/battery-class-27-independent.md`).
- Queue: `class-27-independent` queued → `verdict`/`null`, 2026-10-09
  (pre-write assert passed — was queued/verdictless; temp-file + rename;
  JSON re-validated; own entry only; no downgrade).
- Lock `code/crowd17/next-token/locks/class-27-independent.lock` created
  on start, deleted on completion (verified gone).
- R5005, sealed gate instances, red-team adjudication queue untouched.
