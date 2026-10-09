# Battery verdict: en24-cequi-1766

**Target:** `en24-cequi-1766` (P3)
**Date:** 2026-10-09
**Worker:** battery worker en24-cequi-1766 (subagent 7ffc8bc6-1bc7-4ef7-bddc-5dae64373dc1)

## Bar (verbatim, pre-registered BEFORE testing)

"Name 26's class (concerne-frame?) at @1765 under the 24='en' reading"

**Restated as numbered pass/fail clauses (fixed before testing, not modified after):**

- **C1:** Under the conditional 24='en' premise at @1766, the S3 "en ce qui [26]..." parse is the operative frame at @1766–1769 (24='en' at @1766 not kill-listed; 87='ce', 64='qui' granted).
- **C2:** 26's class at @1769 is named at battery grade — exactly one class survives with all rivals eliminated on closed grounds; else fence with stated cause.

## Method

Read BATTERY-PROTOCOL.md in full before touching anything. Created `code/crowd17/next-token/locks/en24-cequi-1766.lock` on start (agent id + 2026-10-09T21:04:11Z; no prior/stale lock), deleted on completion per protocol. Re-derived the repaired 1,847-pair / 96-type stream in-session from `data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed exactly like `code/side-keyhunt/repair_parse.py` (asserts held: 1,847 pairs, 96 types). `canonical.py` never used. R5005, sealed gate instances, red-team adjudication queue untouched.

Standing inputs (cited, not re-litigated): banked GT (11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que); granted 87=ce, 64=qui, 96=par, 17=fois, 79=tout (A5), 00=pour (A9), 84=on (A15); A1 predicative-frame grant for 37/32 (frame only, value open); A2 23~26 split; kills on 20="fois", 48="est"/"ne"/"de". Battery-grade inputs (cited, not re-litigated): 24-en-verb-conflict (en-kill set {@162,@1774,@1486,@190,@643,@823}; @1766 FENCED not killed, "possible iff 26 verb-shaped"); battery-noun-26 NULL (stated positional rule: 26 = feminine noun iff preceded by 11='la', else verb-class; escalated to red team — stated, not declared); noun26-pas-frames ("26=noun unconditioned" killed at promote grade); battery-26-class-1754 PROMOTE (finding grade, conditional on the stated positional rule — precedent for this verdict's form); battery-lon-09-reseg S3 analysis ("[24] ce qui" ungrammatical on the modal-24 reading); battery-adv-09-1059-1766-value F2 (S3 rival material, fenced).

## Window-level evidence (0-based @, byte-exact, re-derived)

Row a8_08: `@1763=77 @1764=84 @1765=09 @1766=24 @1767=87 @1768=64 @1769=26 @1770=37 @1771=78` — "l'on [09] [24] ce qui [26] [37] [78]...". The claim's "@1765" is the W2 window; 26 sits at 0-based @1769.

26 census re-derived (n=17, predecessors): 02@129, 84@155, **11@240**, 69@406, 64@531, 39@601, 24@655, 94@842, 69@934, 24@992, 46@1250, 38@1470, **11@1560**, 69@1628, 88@1707, 89@1753, **64@1769**. The only la-preceded windows are @129/@240/@1560. At @1769 the predecessor is 64='qui' — not a la-window → verb-branch under the stated positional rule.

### C1: PASS

- @1766 is NOT in the en-kill set ({@162,@1774,@1486,@190,@643,@823}, 24-en-verb-conflict C1). The parent battery explicitly fenced @1766: "'en ce qui [26]' possible iff 26 verb-shaped — noun-26 null leans against". The iff-condition is exactly this target's bar.
- 87='ce' and 64='qui' are granted; 24='en' at @1766 is the bar's own conditional premise (the 24-docket itself is red-team-queued, 24-redteam-adjudication — the condition is stated, not smuggled).
- Under that premise the S3 frame "en ce qui [26]..." is the operative reading (lon-09-reseg: on the modal-24 rival, "[24] ce qui" is ungrammatical, so the frame exists only under 'en').

### C2: PASS — 26's class at @1769 = finite verb (concerne-frame shape)

Four independent legs, zero new assumptions:

1. **Stated positional rule → verb-branch.** battery-noun-26 (umbrella, NULL, escalated): 26 = feminine noun iff preceded by 11='la', else verb-class. @1769's predecessor is 64='qui'. Verb-branch. (The rule is stated-not-declared per §7; this naming inherits that pending status — same conditional form as the 26-class-1754 PROMOTE precedent.)
2. **Umbrella window decision.** battery-noun-26 decided @1769 explicitly: "'en ce qui [26] [37]' (encequi-triple). Decided verb." Cited, not re-litigated.
3. **Corpus leg — "en ce qui" selects a finite verb exclusively.** Census of the lane's 1841 corpus (97 files): 41 "en ce qui" hits, ALL followed by a finite verb — "concerne" 12×, "touche" 5×, "regarde" 2×, "est"/"était", "appartient", "concernait"/"touchait"/"regardait", plus clitic+verb ("me concerne", "se rapporte", "le regardait"). **Zero noun followers.** The concerne-frame is not a hypothesis about this window — it is the only attested shape of the frame in the period corpus. Under the 24='en' reading, 26 MUST be finite-verb; the class is forced by the frame.
4. **Parallel-window corroboration.** The umbrella parsed the structurally parallel @531 ("qui [26] [32]") as verb-branch: "'qui' as relative-clause subject + [26-verb] + [32-adj] predicative complement". At @1769 the same skeleton recurs with 37 in the A1 predicative slot: "qui [26-verb] [37-pred]". And 37's A1 grant is compatible: 37 fills the predicative/complement slot after the finite verb with value open.

**Rivals eliminated on closed grounds:**

- **Noun:** FENCED at this window. (a) Against the stated positional rule (predecessor 64, not 11). (b) Grammatically: "en ce qui [noun] [37-pred]" strands the relative clause — "qui" already fills the subject slot, and 37's licensed class under A1 is predicative-frame, not finite verb; making 37 the clause verb would need a §7 split against A1 (red-team venue). (c) "26=noun unconditioned" already killed at promote grade by noun26-pas-frames (cited, not re-litigated).
- **Adjective / adverb / determiner / pronoun / other:** zero legs; the corpus census shows "en ce qui" admits no non-verbal follower (41/41 verbal).
- **Value 'concerne': NOT named.** Only the CLASS (finite verb) is named. The concerne-frame is the frame-shape; the value stays open (any 3sg finite verb fits: concerne/touche/regarde/est...). No value claim is made.

## Adverses

The target's `adverses` field is empty. Material unlisted adverses — answered, not ignored:

- **24-docket unresolved (24-redteam-adjudication queued):** ANSWERED by conditionality. This verdict holds ONLY under the 24='en' reading (the bar's own premise). If the red team ratifies modal-24, "[24] ce qui" is ungrammatical (lon-09-reseg S3) and this class naming re-opens.
- **Positional rule stated-not-declared (red-team venue):** ANSWERED by inheritance. Per the 26-class-1754 precedent, the naming is finding-grade conditional on the stated rule; if the red team replaces the rule, this verdict re-opens.
- **A2 23~26 split:** respected throughout; no homophone rescue attempted; 23 plays no role.
- **§7 sole polyvalence (67):** no polyvalence declared. The verb-branch assignment is locus-level under the stated rule, not a new polyvalence claim.
- **A1 predicative-frame grant for 37:** untouched. 37's class/value are not adjudicated here; the frame needs only 37's slot-membership, which A1 grants.

## Verdict: PROMOTE (finding grade — conditional)

26's class at @1769 = **finite verb** (concerne-frame shape: "en ce qui [26-fin]..."), under the 24='en' reading. This resolves the iff-condition that 24-en-verb-conflict left fenced at @1766: the 'en ce qui' parse is now licensed on the 26 side.

**Consequence for `w2-frame-24-docket-gate`:** that gate fires ONLY on red-team resolution of the 24='en' vs finite-modal docket — this verdict does not fire it. It supplies the missing half of the parent's condition: IF the red team ratifies 24='en', @1766's S3 parse is fully licensed (26 verb-shaped, confirmed here) and W2 leaves the adv-09 value-naming scope per adv-09-1059-1766-value F2. If modal-24 is ratified instead, this naming re-opens.

No follow-ups required (promote). No standing or red-team verdict contradicted, downgraded, or re-litigated. Canonical-stream caveat stands (row a8_08 offsets unvalidated).

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-en24-cequi-1766.md`
- Queue: `en24-cequi-1766` → `status: verdict`, `verdict: {result: promote, report: code/crowd17/report_inbox/battery-en24-cequi-1766.md, date: 2026-10-09}` (pre-write assert passed — was queued/verdictless; target-id-unique tmp `battery-queue.json.en24-cequi-1766.tmp` + atomic rename, no leftover; disk re-validated; own entry only; no downgrade).
- Lock: `code/crowd17/next-token/locks/en24-cequi-1766.lock` created 2026-10-09T21:04:11Z (no prior/stale lock), deleted on completion (verified gone).
- R5005, sealed gate instances, red-team adjudication queue untouched.
