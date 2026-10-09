# Battery report: `val-97-289-det`

- Target id: `val-97-289-det`
- Claim: Name 97's class at @289. If 97 is a determiner, 09 is forced as head noun of the 'qui'-relative NP - sharpens the second nominal leg from frame-level to class-level.
- Date: 2026-10-09
- Worker: battery worker val-97-289-det (subagent 021834c6-561a-4f4e-bd52-dffb91dca1e6)
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed like `code/side-keyhunt/repair_parse.py`). Asserts held: 1,847 pairs, 96 types. `canonical.py` never used. R5005, sealed gates, red-team adjudication queue untouched.

## Bar (verbatim, pre-registered)

"name 97's class iff the @289 frame licenses it at battery grade; else fence"

Numbered pass/fail clauses (restated before testing):

1. **C1:** The @289 frame licenses naming 97's class at battery grade (a positive, selective leg for one class, with all listed adverses answered).
2. **C2:** Else fence — the class-naming (and specifically the determiner arm) is fenced with stated cause; 97's class stays open.

## Method

Read BATTERY-PROTOCOL.md first; created `locks/val-97-289-det.lock` on start (agent id + 2026-10-09T21:12:00Z, no stale lock; deleted on completion). Re-derived the repaired stream in-session. All @-offsets below are 0-based unless marked 1-based.

Offset note: the claim's "@289" is 1-based = 0-based @288 = 97. Verified byte-exact on row a2_03: `0b@287=00 288=97 289=09 290=64 291=29 292=40` = "pour [97] [09] qui er e …".

Adopted (not re-litigated): §7 standing values (00='pour' A9, 64='qui' granted, 87=ce, 47=ce, 11='la' pencil, 29='er'/40='e' letter-tier pencil GT, 69=["noun","cls"] registry, 65=["noun","cls"] registry, 86 INF-class A9, 41 finite-verb class); R20-046 (redteam-97-tie-adjudication GRANT, packaging grade: "No battery-grade class decision is possible — the tie is genuine at battery grade"; the tie survives at the four 'pour [97]' windows); the pour-window discriminator (zero 00→bare-noun windows stream-wide; 00's bare takes are verb-frame cells; the four 'pour [97]' windows @2/@288/@588/@1823 read INF-favoring); `val-97-verb-test` (97 finite-verb KILL; INF/NOM NULL tie, standing); split-09-redteam-input PROMOTE (nominal arm @915 + @289; adverbial arm @1059/@1765; single-class hypothesis kill-grade dead); noun-09-915-value NULL (parent: Leg 2 = "pour [97] [09] qui" as NP antecedent of the 'qui'-relative, with 97 class-open: "if [97] is a determiner, 09 is head noun; if [97] is a noun, 09 is modifier"). Canonical-stream caveat stands (row a2_03 offsets unvalidated).

Adverse honored: "do not name 09's value here - class-level only" — 09 worked at class level throughout; no value named.

## Findings

**C1: FAIL.** The @288 frame does not license naming 97's class at battery grade. The determiner arm — the only arm this target tests beyond the standing INF/NOM tie — has no selective leg, on four independent grounds:

**F1 — Circular premise (parent's own conditional).** The determiner arm needs 09 as noun-class head ("pour [97-det] [09-N] qui…"). But per the parent report, 09's noun-class at @289 is *conditional on 97's class*: "if [97] is a determiner, 09 is head noun; if [97] is a noun, 09 is modifier." 09 has no registry cell and no independent noun-class leg at @289. The arm's key premise assumes its conclusion — joint hypothesis, not battery-grade licensing.

**F2 — No clean 'qui'-relative verb.** The arm needs "[09] qui [finite verb]". Right context of 64='qui' @290: `29(er) 40(e) 65[noun,cls] 16 01 11(la) 78 40 97 86[INF] 91 18 89[verb-frame]…`. 29/40 are letter-tier ("er"+"e" fragments, not a verb); 65 is noun-class; 86 is INF-class (cannot head a 'qui'-relative); the nearest verb-frame (89) sits at @303, leaving a long unparsed span. No battery-grade-clean finite verb follows "qui". The relative clause the determiner arm depends on does not parse with standing values.

**F3 — Uniform determiner-97 dead on the successor profile; locus-level split is §7 venue.** 97's 10 successors (byte-exact census): 51, 46, 09, 86, 47, 13, 41, 40, 69, 00. Six cannot follow a determiner: 46='que', 86=INF-class, 47='ce', 41=finite-verb class, 40='e' (letter), 00='pour'. A uniform determiner-97 is dead at battery grade. The arm survives only as a locus-level split at @288 (and possibly @2/@1412) — and splits are §7 red-team venue, while R20-046 explicitly bars battery-grade class decisions at the 'pour [97]' windows.

**F4 — The standing INF arm is strictly stronger at this window.** "pour [97]" is a clean, complete contact licensed by 00's bare verb-frame takes and the pour-window discriminator (zero 00→bare-noun stream-wide). The determiner arm adds assumptions (09=noun, a distant relative-clause verb, a locus split) while the INF arm adds none. The frame *favors* the rival; it does not select the tested arm.

**97's only "97 [established-noun]" contact does not rescue the arm.** Successor census shows exactly one 97-window before a registry noun: @1412–1413 "97 69" (69=["noun","cls"]). But the standing parse there is the NOM arm's "[16-INF] [97-N]" object (`redteam-97-tie-adjudication` component a) — i.e., 97-as-noun, not 97-as-determiner. No "97 [noun]" window parses as determiner+noun under any standing parse.

**C2: FIRES.** The determiner-97 arm at @288 is fenced (evidentiary, re-openable): no battery-grade leg, circular key premise (F1), unparseable relative clause (F2). 97's class remains open under the standing INF/NOM tie — red-team venue per R20-046, not re-litigated here. The parent's Leg 2 stays frame-level. No standing or red-team verdict contradicted, downgraded, or re-decided; §7 intact (no split declared, no polyvalence).

Kill grade not met: the arm is unlicensed, not falsified (the pour-discriminator favors INF but a determiner is not a bare noun, so no kill).

## Verdict: NULL (fence executed per bar's else-branch)

## Follow-ups (all verified ABSENT from battery-queue.json, for supervisor)

1. **`qui-290-verb-hunt`** (P4): Locate the finite verb of the 'qui'-relative clause at 0-based @290. The determiner arm and the parent's Leg 2 both need "[09] qui [finite-V]"; the near right context (29, 40, 65-noun, 16, 01, 11…) shows no clean finite verb. A found verb constrains 09's role and re-opens the arm; a confirmed absence challenges the 'qui'-relative NP frame itself.
2. **`det-97-1412-adjudicate`** (P4): At @1412–1413, "97 69" with 69 noun-class (registry) — adjudicate determiner+noun vs the standing NOM-arm parse "[16-INF] [97-N]". This is 97's only "97 [established-noun]" contact stream-wide; it decides whether the determiner arm has ANY distributional leg.
3. **`nom09-289-convergence`** (P4): Test 09's noun-class at @289 independently of 97's class (e.g., via the 'qui'-antecedent requirement or cross-window nominal legs). Breaks the 97↔09 circularity identified in F1; an independently-named noun-09 re-opens the determiner arm.

Not duplicated: `nom09-open-windows` (P4, already queued, parent follow-up 3); `pour-97-noun-discriminator` (P3, already queued, cited in the tie package).

## Bookkeeping

- Lock `code/crowd17/next-token/locks/val-97-289-det.lock` created on start (2026-10-09T21:12:00Z, no stale lock), deleted on completion (verified gone).
- `battery-queue.json`: `val-97-289-det` queued → verdict/null, 2026-10-09 (pre-write assert passed — was queued/verdictless; own entry only; target-id-unique tmp `battery-queue.json.val-97-289-det.tmp` + atomic rename; disk re-validated; no tmp leftover; no downgrade).
- `canonical.py` never used; R5005, sealed gates, red-team adjudication queue untouched.
