# Battery report: nom-92-third-leg — hunt a third nominal-92 leg

- Target: `nom-92-third-leg` (priority 3)
- Date: 2026-10-09
- Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed exactly like `code/side-keyhunt/repair_parse.py`; asserts held; n(92)=22 confirmed). `canonical.py` NOT used. R5005 NOT touched.
- Lock: `code/crowd17/next-token/locks/nom-92-third-leg.lock` (created on start, deleted on completion; no stale lock)

## Bar (verbatim, pre-registered before testing)

"Promote would unblock npframe-60-1674's budget; kill of the hunt fences the budget permanently."

Numbered clauses (derived from the bar before testing; not modified after seeing data):

- **C1 (promote):** at least one of the three named candidates (@1218 "de [92]" conditional on 83="de" promoting; @356's second 92 conditional on "vient [92] ce" being licensable; @901 conditional on 16's value landing) yields a battery-grade nominal-92 leg beyond the standing two (@683, @203) → promote; unblocks npframe-60-1674's budget.
- **C2 (kill):** all three candidates fail at kill grade → kill of the hunt; npframe-60-1674's budget fenced permanently.
- **C3 (else):** verdict null with 1–3 proposed follow-ups.

## Window evidence (re-derived on the repaired stream)

- @1218: `stream[1211:1226]` = [48, 96, 45, 36, 77, **83**, **92**, 61, 24, 48, 30, 9, 20] — so @1217=83, @1218=92, @1219=61. Confirms fence-92-1218's locus.
- @356: `stream[344:368]` = [87, 1, 6, 70, 12, 94, 74, 67, 78, 40, **92**, **98**, **92**, 47, 11, 21, 62, 48, 76, 47, 78, 48, 49, 61] — so @354=92, @355=98, @356=92, @357=47. The candidate shape is `98 [92] 47` = "vient [92] ce".
- @901: `stream[890:912]` = [6, 77, 76, 1, 98, 82, 14, 98, 83, 86, **16**, **92**, 67, 16, 88, 18, 55, 83, 54, 49, 64, 83] — so @900=16, @901=92, @902=67.

Standing values spent (protocol §7): 11=la, 82=m, 46=que, 47=ce (promoted), 87=ce (promoted), 00=pour, 64=qui, 96=par, 79=tout, 59=est (provisional), 77=le (provisional); frames 85 verb-stem (A3), 80/89 verb-frames (A8), "tout me [48-verb]" (A7-L2). Kills adopted: prenne-92-noun (global 92=feminine-noun kill grade). Promotes adopted: verb-92-subset (92=verb on the verbal-governor subset, 2026-10-08), prof-92 (class profile: 2 window-level nominal-subset legs @683, @203), vient-98-name premise as superseded below. R19-124/125/128 (83="de" conditioned LEAD, 11-window scope excluding @1217). R19 98=verb class with the value "vient" demoted to lead grade.

## Candidate tests

### C1a — @1218 "de [92]": DEAD at kill grade

The candidate's stated condition was "if 83='de' promotes". R19-128 (escalate-83-de-kill) ruled in two parts: (1) unconditioned 83="de" is dead at @911 at kill grade — permanent; (2) 83="de" GRANTED AS LEAD (not promote), permanently conditioned, with the 11-window scope {@228, @898, @907, @931, @1061, @1161, @1334, @1612, @1784, @1829, @1840}. **@1217 is explicitly listed as an exclusion** ("formalized 'le de' fence"). So the precondition fails twice: 83='de' never promoted (LEAD is not battery-grade license), and even the lead's conditioned scope can never apply at @1217. The fence-92-1218 null report's conditional leg (Attempt 1: 83='de' + 92=verb) has now failed at red-team grade; the fence stands. No other nominal arm at @1218 survives: noun reading is kill-grade dead globally (prenne-92-noun; would need red-team polyvalence per §7); clause-boundary and word-internal routes fenced by fence-92-1218 (adopted, not re-run).

### C1b — @356 "vient [92] ce" (second 92): DEAD at kill grade

The shape needs 98='vient'. The vient-98-name battery promote (2026-10-08) was **superseded at R19**: 98=verb class granted, the specific value "vient" demoted to lead grade. Lead grade is not a battery-grade license. Independently, even on a granted "vient", the nominal leg dies on grammar: **venir takes no bare noun** — kill-grade per frame66-vient-80 (nom-80-census killed "vient [80-noun]" at @441, @768, @1662 on exactly this ground). "Vient [92-noun] ce" then needs 47="ce" (promoted) to rescue a postposed demonstrative after a bare noun — no license exists in 1841 French. prof-92 already fenced this window ("'vient [92] ce' ungrammatical under both") window-locally; this battery confirms the fence holds under the demoted vient lead. §7-safe: no polyvalence declared; window-level finding only.

### C1c — @901 "16 92 67": untestable — precondition unmet (gate, not kill)

The candidate's stated condition was "re-test if 16's value lands". It has not landed: `val-16-a-vs-est` verdict NULL (2026-10-09); `val-16-62-frames` still queued. 16 is unvalued everywhere; no licensed nominal parse for 92 exists at @901 independent of 16 (prof-92 fenced this window: "16 open; no licensed parse under either arm"). This is an epistemic block, not a kill: the candidate cannot be declared dead at battery grade while its triggering value is unassigned. Gate, not kill.

## Per-clause pass/fail

- **C1 (promote): FAIL.** No third nominal-92 leg nameable: @1218 kill-grade dead (R19-128 double-block), @356 kill-grade dead (demoted vient lead + venir-no-bare-noun kill), @901 untestable (16's value open).
- **C2 (kill of the hunt): FAIL.** The hunt is not killable: @901's candidate survives as a gated re-test, not a kill. The budget of npframe-60-1674 therefore cannot be permanently fenced by this hunt.
- **C3 → NULL.** Two of three named candidates are permanently dead (documented above); one stays gated.

## Verdict

**null** — the hunt fails: @1218 and @356 are dead at kill grade, @901 is gated on 16's value. npframe-60-1674's budget stays exactly where prof-92 left it (2 nominal legs, unstated-assumption budget closed). No standing or red-team verdict contradicted or downgraded: verb-92-subset's subset-scoped promote and prenne-92-noun's kill both stand untouched; §7 intact (67 sole polyvalence; no split declared). R5005, sealed gate instances, and the red-team adjudication queue untouched.

## Follow-up targets (null regenerates work; both IDs verified ABSENT from the queue)

1. **nom-92-901-gated** (P4) — re-test @901's nominal-92 leg ("16 92 67") once 16's value is named. Gate: fires on any verdict naming 16's value (e.g. val-16-62-frames or val-16-a-vs-est re-fire). Bar: name 92's class at @901 with ≤1 unstated assumption; else fence. Note: this is the hunt's sole surviving candidate.
2. **nom92-candidate-sweep** (P3) — census the remaining uncounted 92-windows for nominal-leg evidence under batteries run since prof-92's fence (2026-10-09): @321 (gated on 60's class — "la [92] [60]"); @1607 (gated on 65's class — "la [92] [65]"); @1310 (gated on 30); @1361 (gated on 13); @1453 (conditional); @1490 (gated on 39/24); @1022/@1673 (both-arms fenced — re-test only if a fencing premise shifts). Bar: name ≥1 new battery-grade nominal-92 leg among them; else fence the sweep. Rationale: the claim named only three candidates; @321/@1607 are "la [92] [X]" contacts whose blockers are value-naming gates, not kills.
