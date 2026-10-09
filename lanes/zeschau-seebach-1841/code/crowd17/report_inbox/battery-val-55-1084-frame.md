# Battery verdict: val-55-1084-frame

- Target: `val-55-1084-frame` (battery-queue.json, priority 3, status queued)
- Claim: "value 55 in the @1084 window ('24-V [02] 55') — the strongest remaining geometry for a 02-preposition"
- Worker: c5afc040-315e-4eea-806e-bcf7adef9d53. Date: 2026-10-09.
- Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`; asserts held: 1,847 pairs, 96 types). `canonical.py` NOT used. R5005, sealed gates, red-team queue untouched.
- All @-offsets are 0-based pair indices in the repaired stream.
- Lock: `code/crowd17/next-token/locks/val-55-1084-frame.lock` created on start (no stale lock present); deleted on completion.

## Bar (verbatim, pre-registered)

"name 55's value iff it composes a licensed preposition-complement parse at @1084 with standing values; else fence @1084 as a 02-prep leg"

**Restated as numbered pass/fail clauses (frozen before testing):**
1. **C1 (name):** name 55's value such that it composes a licensed preposition-complement parse at @1084 with standing values.
2. **C2 (else-arm):** fence @1084 as a 02-preposition leg, with stated cause.

## Method

1. Read BATTERY-PROTOCOL.md in full before testing.
2. Re-derived the repaired stream in-session; byte-confirmed the locus and row label.
3. Adopted (not re-litigated): `val-02-prep-sweep` (NULL, 2026-10-09 — parent: preposition-02 fenced stream-wide; @1084 the strongest candidate geometry but "unlicensable" because 55's class is open); R19-077 GRANT + `seg-55-61-94-letters` PROMOTE ("55+61=prend" word-unit at @576/@1167); R19-079 (55's class=verb at @1205); `val-52-55-class` PROMOTE (55 verb-class at @576/@1167; "nominal excluded at battery grade" at those loci only); `sait-veut-24-discriminator` NULL (24's value fenced as value-split; 24=["verb","cls"] registry stands); `val-03-value-census` precedent (parsing ≠ naming).

## Window-level evidence (byte-confirmed, in-session)

- **@1084 (row a6_05):** `@1083=24 @1084=02 @1085=55`, full context `@1082=89 @1083=24 @1084=02 @1085=55 @1086=81 @1087=00 @1088=33` = "[89] [24-V] [02] [55] [81] pour [33] …".
- 55's stream census (12 windows): @25, @523, @550, @576 ("prend" unit), @906, @1085, @1094, @1167 ("prend" unit), @1205 ("prend" unit), @1285, @1611, @1671. The "55 81" bigram is 5× (@25, @523, @550, @1085, @1671).
- At @1085, 55 is followed by 81 (class open), not 61 — the granted "prend" word-unit does not apply here; 55's tier at @1085 is open.

## Clause results

### C1: FAIL — 55's value is unnameable at @1084 under standing values

A "licensed preposition-complement parse" needs BOTH a licensed preposition value for 02 AND a named nominal value for 55. Both are absent:

- **02's preposition value is unlicensed:** the parent `val-02-prep-sweep` fenced preposition-02 stream-wide (8 windows kill-grade hostile, 9 unlicensable, 0 licensing). No standing verdict names any preposition value for 02.
- **55's nominal value has zero selective legs:** no agreement controller, no determiner, no complement-selectional frame at @1085 constrains 55 to any specific noun. Under the `val-03-value-census` precedent, naming one would be arbitrary (parsing ≠ naming). 55's only standing class anchors are the locus-level verb-class at the "prend" windows (@576/@1167/@1205); its global class is open (§7 red-team venue), but no battery evidence licenses a nominal value at @1085.
- A composed story ("[24] [de] [X-noun]") would invent two values (02's preposition, 55's noun) — exactly what the bar's "with standing values" condition forbids.

### C2: FIRES — @1084 fenced as a 02-preposition leg

The preposition-complement parse is not statable with standing values: 02's preposition class is fenced stream-wide (parent) and 55's complement value is unnameable here. Fence is evidentiary, locus-level: re-opens iff a standing verdict names 55's class nominal at this locus or 02's class prepositional.

## Scope

Fences only the 02-preposition leg at @1084. Untouched: the parent `val-02-prep-sweep` fence, the granted "prend" word-unit (@576/@1167/@1205), 55's split package (red-team venue), 24's verb-class and value-split fence, 81's open class (`val-81-55-collocation` still queued), §7. No standing or red-team verdict contradicted or downgraded. Canonical-stream caveat stands (68 of 70 upstream row offsets unvalidated).

## Follow-ups (all verified ABSENT from battery-queue.json; left for supervisor)

1. `val-55-nominal-census` (P4) — census 55's 12 windows for nominal-shape legs with standing values; the @1084 re-open needs a named nominal 55.
2. `val-81-55-rerun` (P4, gated) — re-arm once `val-81-55-collocation` names 81's class; a determiner-81 would constrain 55's slot at @1085.
3. `prep-02-rerun` (P4, gated) — re-test the 02-preposition class at @1084 iff the red team adjudicates 02's class.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-val-55-1084-frame.md` (this file).
- Queue: `val-55-1084-frame` → `status: verdict`, `verdict: {"result": "null", "report": "code/crowd17/report_inbox/battery-val-55-1084-frame.md", "date": "2026-10-09"}` (pre-write assert passed — was queued/verdictless; target-id-unique tmp `battery-queue.json.val-55-1084-frame.tmp` + atomic rename; disk re-validated; own entry only; no downgrade; no tmp leftover).
- Lock created on start, deleted on completion (verified gone).

## Verdict: NULL (fence executed)
