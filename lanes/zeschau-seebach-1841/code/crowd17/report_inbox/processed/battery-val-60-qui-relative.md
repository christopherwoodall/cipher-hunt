# Battery report: val-60-qui-relative

- Target id: `val-60-qui-relative`
- Claim: Name 60 value at @1339 under "qui" (finite-verb slot); constrains the relative clause and 71 antecedent role.
- Date: 2026-10-09
- Worker: battery worker (subagent 31def0c8-731a-46b8-b366-11f4593eb3d4)
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py`; asserts 1847/96 held in-session). `canonical.py` never used. R5005, sealed gates, red-team adjudication queue untouched.
- Offset note: the brief uses 1-based @1339 (= the 60 group). This report uses the queue convention, 0-based: 60 is at @1338, preceded by 64="qui" at @1337. Same locus.

Terms (ASD-STE100): "leg" = one independent window/frame supporting the value. "Battery grade" = the evidence standard of this pipeline. "Conditioned split" = one group taking different values in different positions; §7 reserves all split declarations to the red team.

## Bar (verbatim, pre-registered before testing)

"value named with >=2 independent legs"

Numbered pass/fail clauses (restated before testing, not modified after):

1. **C1:** One specific French verb value is named for 60 at the @1338 "qui" window (finite-verb slot forced by granted 64="qui").
2. **C2:** The named value is supported by >=2 independent legs (distinct windows/frames).

Adverses (pre-registered from standing record): uniformity across all 18 60-windows (participle-60-newvalue KILL); the -dre family rival (verb-60-bare NULL); split-60-verbs' V1–V4 bare-60 grouping (PROMOTE, finding grade); 98="vient" LEAD (dual-spelling question).

## Method

1. Read BATTERY-PROTOCOL.md first. Created `code/crowd17/next-token/locks/val-60-qui-relative.lock` on start (agent id + 2026-10-09T18:28:00Z); no prior/stale lock; deleted on completion.
2. Re-derived the repaired stream byte-exact in-session (1,847 pairs / 96 types asserted).
3. Read the standing 60 record before testing; adopted, never re-litigated:
   - split-60-verbs PROMOTE (finding grade): bare-60 verb (V1–V4: @1338/@700/@995/@1474) vs ent-60 verb (V5–V6) are two items sharing syllable 60.
   - verb-60-bare NULL / verb-60-ent NULL (2026-10-08/09): no value nameable for either arm; -dre family (répondre/vendre/tendre/rendre/attendre/entendre/défendre/descendre/prétendre) parses V1/V3/V4 exactly but V2 @700 ("ne [60]n [98]") is ungrammatical for every French verb (segmentation residual).
   - participle-60-newvalue KILL: past-participle avenue closed at battery grade.
   - gerund-60-1688 PROMOTE: "tout en [60]" licensed as gérondif at @1366/@1690.
   - 08="t" word-internal, battery PROMOTE ×3 today (val-08, val-08-successor-class, syllable-08-letter-value; red-team ratification pending) — adopted as battery-grade premise per the gerund-60-1688 precedent, flagged wherever load-bearing.
4. 1841 diplomatic French throughout.

## Window-level evidence

### The locus — @1338 (row a7_05, byte-verified)

`83@1334 86@1335 71@1336 64@1337 60@1338 08@1339 65@1340 64@1341 52@1342 38@1343 47@1344`

= "[83] [86] [71] qui[64] [60] [08] [65-N] qui[64] [52] [38] ce[47]"

- 64="qui" is granted (§7 standing). A relative pronoun must be followed by a finite verb → 60 is a finite-verb slot. (Confirmed by participle-60-newvalue Leg B.)
- 71 is the antecedent of this relative clause ("71 antecedent role" per the claim).
- 08@1339: "60 08 65" — 65 is noun-class (R20-047 grant), a word; "t"+noun-word is impossible → 08 attaches left (val-08-successor-class C3). The word is "[60t]". That battery left this "[60t]" contact explicitly "unresolved" — this battery resolves it.

### The "60 08" bigram — exactly 2x stream-wide

Full-stream census: "60 08" occurs at @197 and @1338 only.

@197 (row a2_00, byte-verified): `56@193 47@194 01@195 21@196 60@197 08@198 67@199 76@200 87@201 11@202`

= "[56] ce[47] [01] [21-N] [60] [08] et[67] [76-N] ce[87] la[11]"

- slot-60-at-197 PROMOTE already resolved "[21-N] [60-V] [08]" as a finite-verb slot.
- 08@198 → 67@199="et": "t"+"et" impossible → 08 attaches left (val-08-successor-class C6 lists this window). The word is "[60t]".

### Value named: "vient" (venir, 3sg) = 60("vien") + 08("t")

**Leg 1 — @1338: "qui vient".** "qui [60t]" with [60t]="vient": the relative pronoun's finite verb, intransitive. 65 then reads as the nominal antecedent of the following "qui" (val-08-successor-class C3 independently parses "[65] qui" exactly this way): "[71] qui vient; [65] qui [52] [38] ce…" — two stacked relatives. Zero new assumptions beyond the 08="t" premise.

**Leg 2 — @197: "[21-N] vient, et [76-N]".** Intransitive "vient" is clean before coordinating "et": "[21] vient, et [76]…" ("21 comes, and 76…"). Zero new assumptions beyond the 08="t" premise.

**Discrimination within the "Xt" 3sg set.** Every French 3sg verb of shape "[60]t" was tested at both windows. Transitive rivals — "dit" (60="di"), "écrit" (60="écri"), "met" (60="me"), "sait" (60="sai"), "tient" (60="tien"), "vaut" (60="vau"), "bat" (60="ba") — all require an obligatory complement; @197 "[21] [Xt] et" supplies none ("[21] dit et [76]" is ungrammatical: "dire" without complement is not licensed outside inversion tags, and the order here is subject-verb). "doit" (60="doi") and "peut" (60="peu") fail selectionally (they take infinitives; 65 is noun-class). "vient" is the UNIQUE "Xt" verb grammatical at both windows. C1 and C2 pass at the bar level.

## Per-clause pass/fail

1. **C1 — PASS (conditional).** "vient" is named for 60 at the @1338 "qui" window, uniquely discriminated within the "Xt" set.
2. **C2 — PASS.** Two independent legs: @1338 "qui vient" and @197 "[21] vient et".

**Promotion BLOCKED — red-team venue (§7).** Naming "vient" requires a conditioned split of 60, which a battery cannot declare:

- **A1 (uniformity kill):** 60="vien" uniformly is kill-grade dead — @995 "[03] vien et" ("vien" is not a word), @1474 "[53] vientent" (3pl is "viennent", and the cipher does not merge nn across groups per the "70-12-94 prenne" fence), @1366/@1690 "tout en vien" (gérondif is "venant"), @700 "ne vien n…" (ungrammatical). So "vient" holds ONLY as 60="vien" spelled "[60]+[08='t']" at the two "60 08" windows, vs 60=-dre-stem elsewhere. That is a conditioned split: red-team venue under §7 (67 et/veut is the sole licensed polyvalence). Escalated, not declared.
- **A2 (98="vient" LEAD):** "vient" already exists at 98 (LEAD, unratified). Spelling it again at 60+08 is dual spelling (allography), not a direct contradiction of the LEAD — but the red team owns 98's adjudication; coordination flagged.
- **A3 (split-60-verbs tension):** that finding-grade PROMOTE grouped @1338 with @995/@1474 as one bare-60 item; "vient" re-groups @1338 with @197 (the other "60 08" window). Battery-grade tension recorded; the prior finding is not overridden or downgraded.
- **A4 (08="t" premise):** battery-grade, not ratified. If 08="t" falls, "[60t]" dissolves and the -dre family ("qui répond [08]", 08 as separate element) returns for @1338/@197. Load-bearing premise stated, not hidden.
- **A5 (the -dre rival):** the -dre family parses @995/@1474/gérondif exactly and is excluded at the two "60 08" windows ONLY under the 08="t" premise ("répondt" is ungrammatical). -dre vs "vient" are mutually exclusive pending 08's ratification and the split adjudication.

## Verdict: NULL (value named, promotion requires red-team split adjudication)

"vient" is named for the "[60t]" windows with two independent legs (@1338 "qui vient", @197 "[21] vient et"), resolving the "[60t]" contact the 08 battery left open and uniquely discriminating "vient" within the "Xt" set. Per protocol §5 the result is recorded as NULL with the venue issue as headline: promoting it requires a conditioned split of 60 (60="vien" at "60 08" windows vs 60=-dre-stem elsewhere), which is red-team venue under §7. Escalated to the red-team docket (poly-60-redteam, queued). No standing or red-team verdict contradicted, downgraded, or re-litigated; §7 intact. Canonical-stream caveat stands (rows a7_05/a2_00 offsets unvalidated, 68/70).

## Scope

- Names "vient" ONLY for the two "60 08" windows (@197, @1338) under the battery-grade 08="t" premise. Says nothing about 60's value elsewhere; the -dre family remains the live hypothesis for @995/@1474/gérondif.
- Does not touch: ent-60 arm (V5/V6), participle-60-newvalue KILL, gerund-60-1688 PROMOTE, 98="vient" LEAD, or any §7 standing split.
- Pipeline-gap note for supervisor: verb-60-bare's proposed follow-ups `verb-60-dre`, `seg-94-60-12`, `verb-60-er` were verified ABSENT from battery-queue.json (never queued). `dre-60-rerun` below partially covers `verb-60-dre` rescoped; `seg-94-60-12` (V2 "94 60 12 98" re-segmentation) is still unqueued.

## Follow-ups (§4; all verified ABSENT from battery-queue.json)

1. **`redteam-60-vient-split-input`** (P2, gather-only): package the two-leg "vient" case, the conditioned-split requirement, the 98 dual-spelling note, and the split-60-verbs tension as ruling-ready red-team input to the already-queued `poly-60-redteam` docket. Bar: "deliver the package; gather only, no adjudication, no battery-level split declaration."
2. **`dre-60-rerun`** (P3): name the -dre verb for the remaining bare-60 windows with the "60 08" windows excluded per this battery. Bar: "name one -dre verb (répondre/vendre/tendre/rendre/attendre/entendre/défendre/descendre/prétendre) with 60=stem parsing @995 ('[03] [60] et'), @1474 ('[53] [60]ent'), and the 'tout en [60]' gérondif windows (@1366/@1690) with stated syllable boundaries, using only banked/granted/promoted values; the @197/@1338 '60 08' windows are excluded (owned by the 'vient' hypothesis)."
3. **`vient-98-60-coord`** (P4): coordination note — if the red team ratifies 98="vient", rule on the 60+08 "vient" dual spelling (licensed allography vs forced re-parse of "[60t]").

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-val-60-qui-relative.md` (this file).
- Queue: `val-60-qui-relative` queued → `verdict`/`null`, 2026-10-09 (pre-write assert passed — was queued/verdictless; temp-file + rename; JSON re-validated; own entry only; no downgrade).
- Lock `code/crowd17/next-token/locks/val-60-qui-relative.lock` created on start, deleted on completion (verified gone).
- R5005, sealed gate instances, red-team adjudication queue untouched.
