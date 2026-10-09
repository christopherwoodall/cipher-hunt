# Battery report: stem-14-84-retest

Target: `stem-14-84-retest` — "@84 (16 14 06 88) is 14's last verb-shaped window"
Date: 2026-10-09. Worker: stem-14-84-retest. Lock created/deleted per protocol.
Stream: repaired 1,847-pair / 96-type parse (`repaired_offsets.json` +
`upstream-ct_R5005.txt`, byte-exact per `repair_parse.py`). `canonical.py`
never touched. R5005, sealed gates, red-team adjudication queue untouched.

## Bar (verbatim, pre-registered)

"name 14's class iff @80-90 parses as subject+verb+complement under a
verb-stem 14 with 16/88 class-consistent and at most 1 stated assumption;
else fence 14's verb class lane-wide"

Numbered clauses (fixed before testing):
- C1: @80-90 (0-based) parses as subject+verb+complement with 14 a verb
  stem and 06='ent' its 3pl finite ending.
- C2: 16/88 class-consistent — 16 verb-class, 88 verb/governor-class per
  souvent-14-06-retest C2 (distributional support: "m 16" x11 clitic+verb,
  "16 pour" x4 verb+pour-infinitive).
- C3: the parse uses at most 1 stated assumption.
- C4 (else-branch): if C1-C3 fail, fence 14's verb class lane-wide.

## Window evidence (@84, row a1_02, mid-row)

Surface @80-90 (0-based), all row a1_02 (row span @70-101; no row boundary
in window):
`98 51 62 16 14 06 88 77 66 98 19`

Standing values/classes used as premises (not re-litigated):
- 98 = finite verb class (prof-98, §5 standing)
- 06 = 'ent' (red-team R17 promote)
- 88 = verb class (battery promote 2026-10-09, pending ratification;
  registry ["gov","cls"])
- 77 = 'le' (provisional)
- 19 = verb lexeme (battery promote 2026-10-09, pending ratification)
- 16 = verb class, distributionally supported (souvent-14-06-retest C2)
- 51, 62, 66 = open

Hypothesis under test: 14 = verb stem, so 06 is a finite ending by the
ent-06-host-census decision rule (06 is finite "-ent" iff its left neighbor
is a verb stem). Verb = "[14]ent" 3pl at @84-85.

Structural test of C1:
1. The verb "[14]ent" sits at @84-85. A preverbal subject must be 62 (@82)
   or 51 (@81); @83 is 16, verb-class per the bar's premise, and cannot be
   a subject.
2. 16 is interposed between any preverbal subject and the verb. Rescues:
   (a) 16 composes left with 62 ("62-16" unit) — 16 has no letter value;
       no French word statable; grammaticality undemonstrable. DEAD.
   (b) 16 composes right with 14 ("16-14-06" unit) — same defect. DEAD.
   (c) 16 = adverb — contradicts the bar's verb-class premise and 16's
       distributional profile. DEAD.
   (d) clause boundary between 16 and 14 — no byte evidence (mid-row
       a1_02, no gloss, no formula marker); the bar demands one clause. DEAD.
3. "[16] [14]ent" = finite-verb + 3pl-finite adjacency. Under 16's
   locus-level values ('a'/'est', val-91-pp-adj), "a [14]ent"/"est [14]ent"
   is a 3sg/3pl agreement mismatch — ungrammatical at any period. The
   adjacency holds under every standing 16 value; it is structural, not
   value-dependent.
4. Postverbal subject route: @86 = 88 (verb class, cannot be a nominal
   subject); "le [66]" (@87-88) would need 66 nominal, but the 16-adjacency
   defect is on the verb side and survives regardless. DEAD.
5. Complement route: @86 = 88 is verb/governor-class, not nominal — it
   cannot be the complement of "[14]ent". Reading "88 77 66" as
   "[88] le [66]" makes 88 the clause's verb, yielding two finite verbs.
   DEAD.
6. No single stated assumption about the open groups (51/62/66) dissolves
   the "16 [14]ent" adjacency: the defect is 16's position and class, both
   fixed by the bar's premises.

The souvent-skeleton ("[16] souvent [88]") is not re-litigated: 14='sou'
was killed at kill grade by spelling ("souent" != "souvent",
souvent-14-06-retest). It bears on an adverb-stem 14, not the verb-stem
claim tested here.

## Per-clause results

- C1: FAIL. No subject+verb+complement parse exists with 14 as a verb
  stem; the finite-finite "16 [14]ent" adjacency is unresolvable and no
  subject placement or complement reading survives.
- C2: consistent but insufficient — 16 verb-class and 88 verb/governor-class
  are adopted as premises; the parse fails around them, not because of them.
- C3: FAIL — even the full 1-assumption budget cannot produce a
  grammatical parse (no assumption about open groups 51/62/66 touches the
  16-adjacency).
- C4 (else-branch): FIRES. 14's verb class is fenced lane-wide.

## Adverses answered

1. "16/88 values open" — answered at class level. The failure is structural
   (finite-finite adjacency + interposition), independent of 16's or 88's
   values: no standing 16 value ('a'/'est') repairs "a/est [14]ent", and no
   88 value makes it a nominal complement under its verb/governor class.
2. "single-window evidence only" — fenced with stated cause. @84 was the
   last verb-shaped 14 window standing: @1122's verb parse died
   (stem-14-id NULL), the @1121 residual was fenced
   (ent14ent-residual-adjudicate KILL), and every other 14 window is
   verb-hostile per stem-14-id's census (@72/@178 "ce/[69] [14] [24-verb]"
   dead as stem; @623 "m [14] est"; @586 "[14] pour"; @1365/@1689
   "tout [14] [60]" verb killed in tout-frame). The lane-wide fence is the
   bar's own else-branch applied to an exhausted window set.

Recorded, not hidden: 16's global finite-verb class is itself fenced
(val-16-a-vs-est NULL; reseg-1481-98's offset-1 dissolution of @1481 is
red-team territory). The bar's "16 verb-class" premise is the
distributional one from souvent-14-06-retest C2, not the fenced global
finite claim. Even with 16 fully open, no single assumption yields a
grammatical subject+verb+complement with verb-stem 14 (16-as-subject has no
standing; 16-as-adverb contradicts "m 16" x11 / "16 pour" x4).

Residual (fenced, not litigated): row a1_02's offset is unvalidated under
the standing canonicality caveat; the seg-a1_01/reseg-1481-98 offset-1
mechanism is red-team territory.

## Verdict: NULL (fence executed)

14's verb class is fenced lane-wide with stated cause. Not kill grade:
the window does not force 14≠verb at kill grade (the souvent C1 skeleton
admitted a grammatical parse with 14 as adverb stem; the souvent value
claim, not the window, is what died). The bar's else-branch specifies a
fence. No standing verdict contradicted or downgraded; §7 intact; no
red-team verdict on 14's class exists.

## Follow-ups proposed (for supervisor queuing)

1. `val-16-84-role` (P3) — name 16's role at @83 specifically, independent
   of the fenced global finite-verb class; "62 16 [14]06" needs a 16-role
   test that does not load the finite premise.
2. `det-14-census` (P3) — test 14 as determiner-shaped at the surviving legs
   @72/@117/@178; the §7 homophony question for red team (flagged in
   stem-14-id).
3. `part-88-86` (P4) — test 88 as past participle at @86; the
   souvent-skeleton "a souvent [pp]" needs a 88-participle leg re-examined
   under the adverb-stem rival.

## Bookkeeping

Report: code/crowd17/report_inbox/battery-stem-14-84-retest.md.
Queue: stem-14-84-retest → status `verdict`, result `null`, date
2026-10-09 (temp-file + rename; pre-write assert confirmed queued/verdictless;
JSON re-validated post-write). Lock created on start, deleted on completion.
