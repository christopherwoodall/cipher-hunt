# Battery report: redteam-60-vient-split-input

- Target id: `redteam-60-vient-split-input`
- Claim: gather-only red-team input: package the two-leg 'vient' case for the already-queued poly-60-redteam docket
- Date: 2026-10-09
- Worker: battery worker (subagent 478d8c78-2287-43ec-b269-1e93200c94e2)
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py`; asserts 1847/96 held in-session). `canonical.py` never used. R5005, sealed gates, red-team adjudication queue untouched.

Terms (ASD-STE100): "leg" = one independent window/frame supporting a value. "Conditioned split" = one group taking different values in different positions; §7 reserves all split declarations to the red team. "Battery grade" = the evidence standard of this pipeline. "Gather-only" = this package argues nothing; it assembles the ruling-ready input.

## Bar (verbatim, pre-registered before testing)

"deliver the package: the two-leg 'vient' case (@1338 'qui vient', @197 '[21] vient et'), the conditioned-split requirement (60='vien' at '60 08' windows vs 60=-dre-stem elsewhere), the 98 dual-spelling note, and the split-60-verbs tension. Gather only: no adjudication, no battery-level split declaration"

Numbered pass/fail clauses (restated before testing, not modified after):

1. **C1:** The package contains all four elements: (a) the two-leg 'vient' case, (b) the conditioned-split requirement, (c) the 98 dual-spelling note, (d) the split-60-verbs tension — each with byte evidence and provenance.
2. **C2:** No adjudication performed, no battery-level split declared, no standing/red-team verdict contradicted or re-litigated.

## Findings — the ruling-ready package

### (a) The two-leg 'vient' case (source: val-60-qui-relative, NULL 2026-10-09)

**Byte-verified in this session:** the bigram "60 08" is exactly **2x stream-wide** on the repaired 1,847-pair parse:
- @197: `47 01 21 [60] [08] 67 76` (row a2_00)
- @1338: `86 71 64 [60] [08] 65 64` (row a7_05)

**Leg 1 — @1338: "qui vient".** `86 71 64 [60] [08] 65 64` = "[86] [71] qui[64] [60] [08] [65] qui[64]". 64="qui" is granted; the relative pronoun forces a finite verb at 60. 08 attaches left (65 is noun-class per R20-047 grant; "t"+noun-word impossible — val-08-successor-class C3). The word is "[60t]"; the 08 battery left this "[60t]" contact explicitly unresolved, and this case resolves it as "vient" = 60("vien") + 08("t"). 65 reads as the nominal antecedent of the following "qui". Two stacked relatives, zero new assumptions beyond the 08="t" premise.

**Leg 2 — @197: "[21-N] vient, et [76-N]".** `47 01 21 [60] [08] 67 76` = "[56?] ce[47] [01] [21-N] [60] [08] et[67] [76-N] ce[87] la[11]". slot-60-at-197 PROMOTE already resolved "[21-N] [60-V] [08]" as a finite-verb slot. 08@198 → 67@199="et": "t"+"et" impossible → 08 attaches left. The word is "[60t]" = "vient". Intransitive "vient" is clean before coordinating "et": "[21] vient, et [76]…" ("21 comes, and 76…").

**Discrimination within the "Xt" 3sg set (source battery).** Transitive rivals — "dit", "écrit", "met", "sait", "tient", "vaut", "bat" — all require an obligatory complement; @197 "[21] [Xt] et" supplies none ("[21] dit et [76]" is ungrammatical). "doit" and "peut" fail selectionally (they take infinitives; 65 is noun-class). "vient" is the UNIQUE "Xt" verb grammatical at both windows.

### (b) The conditioned-split requirement (the reason this is red-team venue)

60="vien" **uniformly is kill-grade dead** (source battery A1): @995 "[03] vien et" ("vien" is not a word), @1474 "[53] vientent" (3pl is "viennent"), @1366/@1690 "tout en vien" (gérondif is "venant"; gerund-60-1688 PROMOTE), @700 "ne vien n…" (ungrammatical). So "vient" holds ONLY as 60="vien" spelled "[60]+[08='t']" at the two "60 08" windows, vs 60=-dre-stem elsewhere. That is a conditioned split — red-team venue under §7 (67 et/veut is the sole licensed polyvalence). Declaring it at battery grade is prohibited; the split is presented here, not decided.

**Load-bearing premise, flagged not hidden:** 08="t" word-internal is battery-grade, not ratified (val-08-successor-class PROMOTE, syllable-08-letter-value PROMOTE, standalone-08-wordrole KILL — all battery acts today). If 08="t" falls, "[60t]" dissolves and the -dre family ("qui répond [08]", 08 as separate element) returns for @1338/@197. The -dre family parses @995/@1474/gérondif exactly and is excluded at the two "60 08" windows ONLY under the 08="t" premise ("répondt" is ungrammatical). -dre vs "vient" are mutually exclusive pending 08's ratification and the split adjudication.

### (c) The 98 dual-spelling note

98="vient" is LEAD (unratified; R16-005 LEAD stands). Spelling "vient" again at 60+08 is **dual spelling (allography)**, not a direct contradiction of the LEAD — but 98's adjudication belongs to the red team, and the coordination between the two venues is their call. Companion target `vient-98-60-coord` (P4, queued) owns the coordination question.

### (d) The split-60-verbs tension

split-60-verbs PROMOTE (finding grade, battery): bare-60 verb (V1–V4: @1338/@700/@995/@1474) vs ent-60 verb (V5–V6) are two items sharing syllable 60. The 'vient' case **re-groups** @1338 with @197 (the other "60 08" window), cutting across the V1–V4 grouping. Battery-grade tension is recorded; the prior finding is not overridden or downgraded — both packages now sit before the red team. Companion target `dre-60-rerun` (P3, queued) names the -dre verb for the remaining bare-60 windows with @197/@1338 excluded under the 'vient' hypothesis; its queue companion `verb-60-dre` was never queued and stays unqueued (parent's prerogative).

**Pipeline note for supervisor (from val-60-qui-relative):** `seg-94-60-12` (V2 "94 60 12 98" re-segmentation) is now `verdict`/`null` with report `code/crowd17/report_inbox/battery-seg-94-60-12.md` (inbox root, unprocessed at this writing).

### Destination docket

`poly-60-redteam` (P1, queued): "RED-TEAM DECISION: 60 adjective (NP frames) vs 60 verb (kill-grade windows) polyvalence". Bar: "resolve iff red team declares 60 polyvalent (adjective/verb) with a positional rule, or assigns one class with all 18 windows parsing". This package feeds that docket. No adjudication performed here.

## Per-clause pass/fail

1. **C1 — PASS.** All four elements delivered with byte evidence and provenance (source report ids and queue target ids cited).
2. **C2 — PASS.** No split declared at battery grade; §7 intact; no standing/red-team verdict contradicted, downgraded, or re-litigated. Canonical-stream caveat stands (rows a2_00/a7_05 offsets unvalidated, 68/70).

## Verdict: NULL (gather-only)

The ruling-ready red-team input is delivered to the `poly-60-redteam` docket. Recorded as NULL per protocol §5 §2 with the venue issue as headline. No follow-ups required (gather-only package is the terminal node); the companion targets are already queued.

## Scope

- Package only. Names nothing, kills nothing, splits nothing.
- Adopted, never re-litigated: 64="qui" granted; 65 noun-class (R20-047); 67="et"; 08="t" battery-grade premise (unratified); the -dre family as the live rival elsewhere; 98="vient" LEAD; participle-60-newvalue KILL; gerund-60-1688 PROMOTE.
- Untouched: ent-60 arm (V5/V6), all §7 standing splits, the `poly-94-r17018-input` and other docket packages.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-redteam-60-vient-split-input.md` (this file).
- Queue: `redteam-60-vient-split-input` queued → `verdict`/`null`, 2026-10-09 (pre-write assert passed — was queued/verdictless; temp-file + rename; disk re-validated; own entry only; no downgrade).
- Lock `code/crowd17/next-token/locks/redteam-60-vient-split-input.lock` created on start (agent 478d8c78-2287-43ec-b269-1e93200c94e2, 2026-10-09T19:00:00Z), deleted on completion (verified gone).
- R5005, sealed gates, red-team adjudication queue untouched.
