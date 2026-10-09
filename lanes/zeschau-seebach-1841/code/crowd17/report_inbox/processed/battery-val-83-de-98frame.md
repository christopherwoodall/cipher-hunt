# Battery `val-83-de-98frame` — verdict: NULL (fence arm executed)

## Bar (verbatim, pre-registered)

> Test 83='de' under the '98 83' frame (x5: @229, @899, @932, @1062, @1785; 98='vient' LEAD); a landed 83='de' makes '98 83 86' @899 ('vient de [86-INF]') parse.
> Bars: name 83='de' iff >=2 of the 5 windows license it at battery grade; else fence

Numbered clauses:
- C1: >=2 of the 5 '98 83' windows license 83='de' at battery grade → name 83='de'.
- C2 (else-arm): fewer than 2 windows license at battery grade → fence the battery-grade licensing claim over the '98 83' frame.

## Method

Re-derived the repaired 1,847-pair / 96-type stream in-session from `data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json` (1,847 pairs confirmed). `canonical.py` never used. All five '98 83' windows located byte-exact (0-based 98-positions 227, 897, 930, 1060, 1783; 83 one index right = the claim's 1-based @229/@899/@932/@1062/@1785).

Battery grade = grammatical French parse of the window under standing values with zero ungranted assumptions. "Compatible" (no standing-value conflict) is weaker than "licenses" and does not satisfy C1.

Standing values used: 98=['verb','cls'] with 'vient' LEAD (bar presupposes); 83=['de','lead'] (conditioned LEAD, R20-109); 86=['INF','cls']; 82=['m','gt'] (pencil); 96=['par','prom']; 21=['noun','cls']; 56 class-open (registry null).

## Window-level evidence

| # | @ (1-based 83) | context | parse under 83='de' | battery-grade license? |
|---|---|---|---|---|
| 1 | 229 | `61 96 87 46 [98 83] 82 96 21` (a2_01) | "vient de m par [noun]" | NO — ungrammatical |
| 2 | 899 | `01 98 82 14 [98 83] 86 16 92` (a5_08/09) | "vient de [86-INF]" | YES |
| 3 | 932 | `61 96 48 82 [98 83] 56 69 26` (a5_10) | "vient de [56]" (56 open) | NO — 'de' untested |
| 4 | 1062 | `23 77 84 09 [98 83] 82 96 21` (a6_04) | "vient de m par [noun]" | NO — ungrammatical |
| 5 | 1785 | `48 74 65 23 [98 83] 82 96 21` (a8_09) | "vient de m par [noun]" | NO — ungrammatical |

Per-window reasoning:

- **#2 @899 (@897 0-based):** "vient de [86-INF]" is grammatical French under all-standing values (98='vient' LEAD per the bar's frame; 86 INF-class granted). No resegmentation arm eats the 83 (no standing composition license at "14 98" or "82 14"). This is the banked "1 clean @898" leg (R19-126 LEG-1). **Licenses at battery grade.**
- **#1/#4/#5 (the "98-83-82-96-21" formula ×3):** under 83='de', 82='m' (pencil GT), 96='par' (granted), the window reads "vient de m par [noun]". No grammatical French parse: "venir de" needs a place or an infinitive ("vient de me" is not a complete clause); "de me par X" has no verb for "par" to attach to; the 'vient de me parvenir' French was frame-killed (de83-adverse-restock caveat). 82='m' is banked GT and 96='par' granted, so no rescue via re-valuing neighbors — any rescue needs §7. **Do not license at battery grade.** They remain "compatible" only at the red team's weaker frame-type grade (R19-126 LEG-2, explicitly caveated "claims only the frame-type slot parses as 'de', not the French sentence").
- **#3 @932 (@930 0-based):** "vient de [56]" — 56 is class-open, so 'de' is untested here: any 83 value parses. R19-126 graded this LEG-3 "compatible, weak... not as a positive leg". **Compatible only; does not license.**

## Per-clause pass/fail

- C1: FAIL — exactly 1 of 5 windows (@899) licenses 83='de' at battery grade; 1 < 2.
- C2: FIRES — the battery-grade licensing claim over the '98 83' frame is **fenced**: the frame does not license 83='de' at battery grade in >=2 windows.

## Verdict: NULL (fence executed)

The '98 83' frame licenses 83='de' at battery grade in exactly one window (@899, "vient de [86-INF]"). The formula ×3 are ungrammatical as French at battery grade (their red-team LEG-2 status survives only at the weaker frame-type grade with the standing caveat); @932 is 'de'-untested.

## Scope

Fences ONLY the battery-grade licensing claim named in this bar. Untouched, in full:
- R20-109: conditioned 83='de' LEAD stands (11-window scope unchanged).
- R19-126 LEG-2 (formula ×3) stands at its red-team-accepted frame-type grade with its caveat — this battery tested a stricter grade and does not re-litigate it.
- R19-126 LEG-1 (1 clean @898 + conditionals) stands.
- The R20-109 carry-forward "positive legs for 83='de'" item remains open: **no new positive legs found** (consistent with R20-109).
- 98='vient' LEAD, 86 INF-class, 82='m' pencil GT, 96='par' grant, §7 — all untouched.
- No standing/red-team verdict contradicted or downgraded. R5005, sealed gates, red-team adjudication queue untouched.

## Follow-ups (all verified ABSENT from queue)

1. `de83-formula-french` (P4) — corpus test of "vient de me par"/"vient de m par" in the 1841 corpus; a zero hardens the formula ×3's ungrammaticality under 83='de' to grammaticality grade, which would force the red team to re-grade LEG-2's caveat.
2. `val-56-932-class` (P4) — name 56's class at @930 (0-based); if 56 = noun, "vient de [56-noun]" becomes a second battery-grade licenser and re-fires this bar.
3. `de83-98frame-reseg` (P4) — test word-internal resegmentation arms at the formula windows ("98 83 82" composing as a unit); if one parses, the formula ×3 leave the 'de' frame entirely.

## Bookkeeping

- Lock `code/crowd17/next-token/locks/val-83-de-98frame.lock` created 2026-10-09T20:12:31Z (agent 6cc68c96-1fef-468c-99ea-27808d54e4bd), no stale lock; deleted on completion (verified below).
- Queue `val-83-de-98frame`: pre-write assert passed (was queued/verdictless) → `status: verdict`, `verdict: {result: null, report: code/crowd17/report_inbox/battery-val-83-de-98frame.md, date: 2026-10-09}` via target-id-unique tmp `battery-queue.json.val-83-de-98frame.tmp` + atomic rename; own entry only; no downgrade.
