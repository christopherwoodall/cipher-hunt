# Battery report: le14-adj60-tail

- Target id: `le14-adj60-tail`
- Claim: "14='le' (determiner) heads the frame tail under the adjective rival"
- Date: 2026-10-09
- Worker: battery worker (subagent 773b9a98-9e5d-4c47-af56-4e2542a596fe)
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py`; asserts 1847/96 held in-session). `canonical.py` never used. R5005, sealed gates, red-team adjudication queue untouched. @i = 0-based pair index unless stated.

Terms (ASD-STE100): "fence" = the reading is confined to the stated cause and cannot be used as a value leg. "Frame-dependent" = 14's value at these windows rides other ungranted items, so no value can be named here.

## Bar (verbatim, pre-registered before testing)

"resolve iff '14 60 03' @1365/@1689 parses as 'le [60-adj] [03-N]' with the '94 79' head resolved per frame-62-94-79-reparse; gated on adj-60 naming 60's adjective value; else fence 14's value as frame-dependent"

Numbered pass/fail clauses (restated before testing, not modified after):

1. **C1 (gate):** adj-60 work has NAMED 60's adjective value → the resolve arm is licensed.
2. **C2 (head):** the '94 79' head is resolved per frame-62-94-79-reparse → the tail parse can be stated without an anomalous head.
3. **C3 (fence fallback):** if C1 or C2 fails, fence 14's value as frame-dependent at these windows → NULL.

Adverses listed (queue): "'94 79' head still anomalous; adj-60 not yet run".

## Method

1. Read BATTERY-PROTOCOL.md first. Created `code/crowd17/next-token/locks/le14-adj60-tail.lock` on start (agent id + 2026-10-09T18:44:43Z); no prior/stale lock.
2. Re-derived the repaired stream byte-exact in-session (1,847 pairs / 96 types asserted).
3. Read the adj-60 family reports (`processed/battery-adj-60.md` KILL 2026-10-08; `processed/battery-adj-60-2160.md` PROMOTE 2026-10-09) and checked the queue status of `frame-62-94-79-reparse`; adopted, never re-litigated.
4. Re-censused the '14 60 03' trigram stream-wide and byte-verified both named windows.

## Window-level evidence (byte-exact, 0-based)

Window A — @1365 (0-based): `@1363=94 @1364=79 @1365=14 @1366=60 @1367=03 @1368=30`
reads "94 79 | 14 60 03 | 30 …" — the sole '14 60 03' trigram in the stream.

Window B — @1689 (0-based): `@1687=94 @1688=79 @1689=14 @1690=60 @1691=27 @1692=46`
reads "94 79 | 14 60 27 | 46 …" — this is **'14 60 27', NOT '14 60 03'**.
Stream census: the trigram '14 60 03' occurs exactly **1x** in 1,847 pairs (@1365). The bar's "two-window" premise is therefore a misread of the second window.

Both windows also host the gerund-60-1688 reading ("94 79 14 60" = "ne tout en [60]"), PROMOTEd 2026-10-09: 14='en' is battery-grade at both loci, 60='present participle of the -dre verb'. The adjective rival for 60 sits beside, not above, this reading.

## Per-clause pass/fail

### C1 — FAIL (gate not met)

`adj-60` (2026-10-08) returned KILL for the single-value adjective claim. `adj-60-2160` (2026-10-09) returned PROMOTE but its clause C3 is explicit: "**no value named for 60**, no polyvalence declared — findings are evidence only." 60's adjective VALUE is unnamed. The gate condition "adj-60 naming 60's adjective value" is therefore not satisfied. The resolve arm of the bar is not licensed.

### C2 — FAIL (head unresolved)

`frame-62-94-79-reparse` is still `status: queued` (no verdict) — the '94 79' head is unresolved at battery grade. The adverse "'94 79' head still anomalous" stands. The bar's required "with the '94 79' head resolved per frame-62-94-79-reparse" cannot be satisfied today.

### C3 — FIRES (fence executed)

With C1 and C2 failed, the bar's own fallback fires: **14's value is fenced as frame-dependent** at @1365/@1689. At the only genuine '14 60 03' window, 14's reading rides two ungranted items (60's adjective value, unnamed; the 94/79 head, unresolved) and faces a battery-grade rival (14='en' under gerund-60-1688, promoted today on these exact bytes). Naming 14='le' here would stack an unvalued adjective class on an unresolved head — not battery grade.

## Scope (stated, not hidden)

- This fences ONLY the 14='le' tail reading at these two windows as frame-dependent. It does NOT touch:
  - 14='en' battery-grade legs (en14-value-tighten; gerund-60-1688 PROMOTE on these exact windows stands),
  - 60's adjective CLASS evidence (adj-60-2160 class-level promote stands; it named no value, which is exactly the gate failure),
  - 03 nominal, 79='tout' granted, 94='ne' STRONG LEAD.
- No standing or red-team verdict is contradicted or downgraded. §7 intact (no new value named, no polyvalence touched).
- Canonical-stream caveat stands: rows a7_06/a8_05 offsets unvalidated (68/70).

## Verdict: NULL (fence executed)

The gate condition is unmet and the head is unresolved; 14's value is fenced as frame-dependent at @1365/@1689 per the bar's own fallback.

## Follow-ups (all verified ABSENT from battery-queue.json, left for supervisor)

1. `le14-dependency-rearm` (P4) — re-run the '14 60 03' tail test iff BOTH conditions clear: adj-60 (or a successor) names 60's adjective value AND frame-62-94-79-reparse resolves the '94 79' head. Bar: '14 60 03' parses as 'le [60-adj] [03-N]' with both dependencies granted.
2. `win1689-tail-60-27` (P4) — the second window is '14 60 27', not '14 60 03'; classify the '60 27' contact. Note: class-27-independent NULL'd 2026-10-09 (27's class open) — this tail cannot resolve until 27 is classed.
3. `en-vs-le-14-hapax` (P4) — discriminate 14='en' vs 14='le' at the single '14 60 03' hapax (@1365) using the '94 79 14' left frame; 14='en' now has gerund-battery legs at both loci.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-le14-adj60-tail.md` (this file).
- Queue: `le14-adj60-tail` queued → `verdict`/`null`, 2026-10-09 (pre-write assert passed — was queued/verdictless; temp-file + rename; JSON re-validated; own entry only; no downgrade).
- Lock `code/crowd17/next-token/locks/le14-adj60-tail.lock` created on start, deleted on completion (verified gone).
- R5005, sealed gate instances, red-team adjudication queue untouched.
