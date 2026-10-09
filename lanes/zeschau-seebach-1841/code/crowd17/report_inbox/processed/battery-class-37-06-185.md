# Battery report: class-37-06-185 — 37's class at @185

- Worker: subagent 6b15dcc2-0721-4d9d-9fbc-e75142f06409
- Lock created: 2026-10-09T08:15:18Z (no prior lock present; no stale lock)
- Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` +
  `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`).
  `canonical.py` was NOT used. R5005 NOT touched. Sealed gates and the red-team
  adjudication queue NOT touched. No data invented.

## Bar (verbatim, pre-registered)

"state which class 37 takes; 06's function follows 37's class"

Numbered clauses (fixed before testing):

1. State which class 37 takes at @185: predicative adjective vs verb stem.
2. 06's function follows 37's class: if 37 is a predicative adjective, 06 is
   not 37's finite ending (it belongs to the following word / the adjective
   word); if 37 is a verb stem, 06 is its finite ending.

Claim gloss (from the queue entry, pre-registered before 06's value promoted):
"decide 37's class at @185: predicative adjective (then 06 is a word-initial
syllable) vs verb stem (then 06 may be its finite ending)". Adverses: none
listed.

## Method

1. Reparsed the repaired stream byte-exactly per `repair_parse.py` (1,847
   pairs confirmed). Located the target frame: 0-based @183=37, @184=06,
   @185=00, row a1_05.
2. Re-derived 37's contact profile (n=28) and the 37-06 / 37-29 bigram counts
   independently from the stream.
3. Applied the standing verdicts as constraints (protocol §5.2 — never
   downgrade, never contradict-and-overwrite):
   - A1 (red-team GRANT): 37 predicative frame, 6 independent "est 37" legs —
     "strongest adjective-frame group in the lane".
   - ent-06 (battery PROMOTE, 2026-10-08): 06="ent" (global value; verb-ending
     syllable, also word-initial "ent" as in "entreprenne" @346). This battery
     explicitly FENCED @184 "37-06-00" as "(same tension for 37)" — this
     target is the battery that resolves that fence.
   - qui37-rival-values (battery PROMOTE, 2026-10-08): 37-as-verb-stem
     DISTRIBUTIONALLY EXCLUDED at kill grade — 37→29 = 0/28 vs granted stems
     {33,86} = 9/57, Fisher depletion p = 0.0219. Finite verb ranked #1 only
     for the qui frames (with polyvalence pressure flagged for the red team,
     C1); adjective ranked #2, live via A1.
   - Protocol §7: 67 et/veut is the sole true polyvalence — a battery never
     declares a second.
4. Tested 06's positional function at @184 under the promoted 06="ent" value
   against the following group 00="pour" (promoted standalone word, A9).

## Window-level evidence (@-offsets, 0-based)

Target frame, row a1_05:

| @ | group | standing value |
|---|---|---|
| 179 | 24 | open |
| 180 | 87 | ce (promoted) |
| 181 | 64 | qui (promoted) |
| 182 | 23 | open (n=8) |
| 183 | 37 | predicative frame (A1 grant) |
| 184 | 06 | "ent" (promoted, ent-06) |
| 185 | 00 | pour (promoted, A9) |
| 186 | 33 | INF-class (A1) |
| 187 | 16 | open |
| 188 | 00 | pour (promoted, A9) |

Distributional facts (re-derived from the stream):
- 37: n=28. 37→06 = 1/28 — the bigram is a HAPAX, and the single instance is
  the very window under test (@183→184). No independent recurrence of 06 as
  anything attaching to 37.
- 37→29 = 0/28 (stem diagnostic; granted verb stems 33→29 = 5/25, 86→29 =
  4/32). Re-derivation matches the qui37 battery's kill-grade exclusion.
- 59→37 ("est 37"): 6 windows @528/624/912/1178/1443/1796 (A1 legs,
  re-derived exact).
- 64→37 ("qui 37"): 3 windows @675/@938/@1632 — the qui frames adjudicated by
  qui37-rival-values (finite-verb parse ranked #1 there, adjective #2;
  polyvalence pressure C1 left to the red team; this window is not a qui
  frame — its 37 is preceded by 23, not directly by "qui").
- 06: n=44. 06="ent" promoted globally (ent-06, 2026-10-08).
- 23: n=8; 64→23 hapax (@181); 23→37 hapax (@182). The 23-37-06 trigram is
  unique in the stream — the A1 note's "concerne" segmentation has no
  recurrence support and, parsed as 23-37="concer"+06, makes 37 a medial
  syllable, not a stem; it does not support the verb-stem class as stated.

Positional elimination for 06 at @184 (under promoted 06="ent"):
- Word-initial ("ent…"): the next group @185 is 00="pour", a promoted
  standalone word — "entpour" is impossible. ELIMINATED.
- Standalone word "ent": not French. ELIMINATED.
- Word-medial ("37"+"ent"+…): same "pour" blocker. ELIMINATED.
- Word-final: "37ent" is one word. ONLY VIABLE PARSE.

## Per-clause pass/fail

- **Clause 1 (state 37's class): PASS — predicative adjective.** A1's
  red-team grant stands (6 independent "est 37" legs). The rival verb-stem
  class is excluded at the lane's distributional standard by the standing
  qui37-rival-values PROMOTE (37→29 = 0/28, Fisher p = 0.0219, kill grade;
  re-derived exact here). Declaring 37 a verb stem would contradict that
  standing verdict and the §7 sole-polyvalence constraint (67). The window's
  verb-shaped alternative ("concerne") is a hapax trigram whose own best
  parse makes 37 a medial syllable, not a stem — it does not establish the
  verb-stem class as the claim states it.
- **Clause 2 (06's function follows 37's class): PASS.** 06="ent" (promoted)
  at @184 is word-final: the "-ent" of the adjective word "37ent"
  (@183–184). It is NOT 37's finite verb ending — 37 is not a verb stem
  (clause 1 + qui37 kill), and the 37-06 bigram is a hapax with no ending
  recurrence. 06's function is therefore determined by 37's class, as the
  bar requires.

**Material correction to the claim's gloss (recorded, not hidden):** the
claim was queued before 06="ent" promoted and glossed the adjective fork as
"06 is a word-initial syllable". Under the intervening promoted value,
06 at @184 is word-FINAL ("37ent", one word), not word-initial — word-initial
"ent" is positionally impossible before the promoted standalone "pour".
The class decision the bar asks for is unaffected; the mechanism is
corrected. This resolves the ent-06 battery's fenced adverse "@184
'37-06-00' (same tension for 37)" in favor of the adjective class.

## Verdict

**promote** — 37's class at @185 is the predicative adjective (A1 frame
stands); "37ent" @183–184 is one adjective word with 37 as its initial
syllable(s) and promoted 06="ent" as its final "-ent"; 06 does not function
as 37's finite verb ending. No standing verdict contradicted; no
polyvalence declared (§7 67-rule untouched); the qui37 C1 pressure point is
not decided here (this window is not a qui frame). Adverses: none were
listed.

## Follow-up leads (optional; for the supervisor — promote carries no
null mandate)

- L1 (value battery): identify "37ent" — which "-ent" predicative adjective
  (évident / prudent / différent / présent / content …)? Narrow bar:
  discriminate via 37's six "est 37" windows (@528/@624/@912/@1178/@1443/
  @1796) against -ent-adjective collocates; needs a second "37ent" window
  or a value leg, not just the hapax @183–184.
- L2 (finder/narrow battery): 23's class — n=8, sits between "qui" (@181)
  and the adjective (@183); 64→23 and 23→37 are both hapax. Test adverb vs
  pronoun vs determiner on its 8 windows.
