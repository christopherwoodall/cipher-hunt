# Battery report: vient-98-894-reaudit

- Target id: `vient-98-894-reaudit`
- Claim: "vient-98-name's promote survives stem-14-84-retest's lane-wide 14-verb fence"
- Date: 2026-10-09
- Worker: battery worker vient-98-894-reaudit (session 669024f2-8acb-4ba7-8311-1a818feca9f5)
- Stream: repaired 1,847-pair / 96-type parse (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`; n=1847 asserted). All @-offsets are 0-based repaired-stream indices. `canonical.py` never used. R5005, sealed gates, red-team adjudication queue untouched.
- Lock: `code/crowd17/next-token/locks/vient-98-894-reaudit.lock` (created at start, deleted on completion; no prior lock existed).

## Bar (verbatim, pre-registered before testing)

"Promote stands iff vient-98-name's bar clauses 1–6 pass without the @894 'vient m'[14-inf]' conditional parse and no new contradiction is introduced by the fence; else escalate to red team."

Numbered clauses (restated before testing, not modified after):

1. (C1) vient-98-name's bar clauses 1–6 all pass with the @894 'vient m'[14-inf]' conditional parse excluded (no clause may depend on 14 being a verb).
2. (C2) No new contradiction against 98='vient' is introduced by the lane-wide 14-verb fence — i.e., no 98-window forces 98≠'vient' under the fence that did not already do so before it.
3. (else) If C1 or C2 fails: mark NULL with the contradiction as headline and escalate to the red team (protocol §5).

## Method

1. Read `BATTERY-PROTOCOL.md` first; created/deleted lock per protocol.
2. Re-derived the repaired stream in-session; asserted 1,847 pairs / 96 types.
3. Read `battery-vient-98-name.md` (PROMOTE, 2026-10-08, clauses 1–7) and `battery-stem-14-84-retest.md` (NULL fence: 14's verb class fenced lane-wide — the last verb-shaped 14 window @84 failed, all other 14 windows verb-hostile; fence, not kill grade).
4. Scanned all 40 98-windows for any 14 contact (byte-exact); tested whether any vient-98-name clause 1–6 depends on a verbal 14; tested whether the fence forces 98≠'vient' at any window.

## Window-level evidence

**14-98 contact census (byte-exact):** exactly two 98-windows touch 14, one local cluster on row a5_08:

- @894: `06 77 76 01 [98] 82 14 98 83` → surface `01 98 82 14 98 83 86` @892–899 (row a5_08).
- @897: `01 98 82 [14] 98 83 86 16 92` → same cluster, `14 98 83 86` @896–899.

No other 98-window in the 40-window inventory (`[12, 19, 80, 89, 92, 124, 192, 227, 236, 355, 440, 511, 702, 767, 803, 838, 894, 897, 930, 946, 971, 1060, 1073, 1074, 1137, 1139, 1145, 1146, 1284, 1317, 1325, 1373, 1481, 1579, 1601, 1643, 1660, 1661, 1725, 1783]`, re-verified) contains a 14 within ±3. The 14-fence can therefore only affect @894/@897.

**The @894 'vient m'[14-inf]' conditional parse is dead under the fence.** stem-14-84-retest fenced 14's verb class lane-wide: the @84 window (the last verb-shaped 14 window) failed structurally, and every other 14 window is verb-hostile per stem-14-id's census. A vowel-initial infinitive 14 at @896 is a verbal-14 use and is excluded. Per the bar, this reading is dropped, not litigated.

**Clauses 1–6 re-tested without it:**

- **Clause 1 (≥2 'vient de' frame-types): PASS.** (a) Formula `98 83 82 96 21` ×3 byte-identical (@227/@1060/@1783) — no 14 involved, untouched. (b) @897 `14 98 83 86` = "[subject] vient de [86-inf]": vient-98-name's own reading already shares subject 01 ("the @897 clause then shares subject 01: '[01] vient de [86]'"), with "subject attribution (14 vs 01) fenced as underdetermined." Under the fence, the 14-as-subject arm has no live standing arm (verb class fenced; 'en'-clitic arm cannot head a subject; determiner arm licensed only at @117; 14='le' killed globally) — so the underdetermination resolves to **01 as subject**. The frame-type itself ('vient de' + [86-inf]) does not depend on any verbal 14. PASS with the subject disambiguated (stated).
- **Clause 2 (doubled-98 ×3 fenced): PASS.** @1073/@1145/@1660 — no 14. Unchanged.
- **Clause 3 (@702 "n'vient" fenced): PASS.** No 14. Unchanged.
- **Clause 4 (@1139 'pour [98]' fenced): PASS.** No 14. Unchanged.
- **Clause 5 (@930 'me vient de [56]' fenced): PASS.** No 14. Unchanged.
- **Clause 6 (@1601 '[81] me vient pour [44]' resolved): PASS.** No 14. Unchanged.

**C2 — new-contradiction sweep:** The fence constrains 14's class; the promote's claim is 98's value. At @894 (`01 98 82 14`) and @897 (`14 98 83 86`), 98 still reads "vient" (finite 3sg) — nothing in the fence challenges the finite-verb reading of 98 itself. The fence's cost localizes to 14's parse at @896: with 14 non-verbal, its live arms are the 'en' clitic (core-14-622-bank PROMOTE, en14-three-window PROMOTE) — so "01 vient m'en" becomes a **14-residual** (the clitic lacks its governor in this window), fenced for the 14 line, not re-litigated here. Critically: a 14-residual is not a 98-contradiction. No 98-window forces 98≠'vient' under the fence that did not already do so before it. **PASS.**

## Per-clause pass/fail

1. C1 (clauses 1–6 pass without the excluded parse): **PASS.** None of clauses 1–6 depended on the @894 conditional parse; clause 1b's subject resolves to 01, which the fence does not touch.
2. C2 (no new contradiction from the fence): **PASS.** The fence strains 14 at @896, not 98; 98='vient' holds at both 14-contacting windows.
3. Escalation disjunct: does not fire.

## Adverses

None listed in the queue entry.

## Verdict: PROMOTE (of the confirmation claim)

vient-98-name's promote **survives** stem-14-84-retest's lane-wide 14-verb fence. Both bar clauses pass: clauses 1–6 hold without the @894 conditional parse, and the fence introduces no new contradiction against 98='vient'. This verdict confirms the confirmation claim only — 98='vient' itself remains battery-promoted, pending red-team ratification.

## Caveats and fences (stated, not hidden)

- **14-residual at @896:** with 14's verb class fenced and its determiner arm licensed only at @117, 14 at @896 sits on the 'en'-clitic arm (battery-grade), whose governor is absent in this window. Recorded as a 14-line residual for the supervisor's follow-up queue, not a 98 contradiction.
- **83='de' lead:** clause 1b still rests on the le83-window battery's 'de' lead (NULL, C2 5/5 pass) — a standing dependency of the promote, not re-litigated here.
- **Canonicality:** row a5_08's upstream offset is unvalidated under the standing canonicality caveat; verdict holds on the canonical stream per protocol.
- **Scope note:** vient-98-name's clause 7 (zero board contradictions) was outside this bar and is unaffected by this re-audit.

## Follow-ups

None required (promote, not null). The @896 14-residual (`m'en`-frame completion at this window) is 14-line territory and may be picked up by queued 14 batteries.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-vient-98-894-reaudit.md`
- Queue: `vient-98-894-reaudit` → status `verdict`, result `promote`, date 2026-10-09 (pre-write assert confirmed queued/verdictless; temp-file + rename; JSON re-validated; only this entry touched; no downgrade)
- Lock created on start, deleted on completion. No standing or red-team verdict contradicted or downgraded; §7 intact; R5005, sealed gates, red-team queue untouched.
