# Battery det-385-leftedge — verdict: NULL (fence; bar's else-branch fires)

**Target:** `det-385-leftedge` (P3)
**Date:** 2026-10-09
**Worker:** battery worker (subagent 1a317d5f-b169-4d06-b56d-50fa4970afa1). Lock `locks/det-385-leftedge.lock` created on start, deleted on completion. `canonical.py` never used. R5005, sealed gate instances, red-team adjudication queue untouched.

## Bar (verbatim, pre-registered)

> "if none, the bare-NP reading stays fenced with cause"

**Numbered clauses (restated before testing):**
- C1: A battery-grade determiner candidate exists in the @385 left edge heading the '38 37 43' fragment → PROMOTE.
- C2 (else): No such candidate exists → NULL; the bare-NP reading stays fenced with cause.

## Method

Stream re-derived in-session from `code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`: 1,847 pairs / 96 types, asserts hold. All @-offsets 0-based queue convention. Indexing note: the target's "@379-383" is the 1-based lane convention; byte-exact 0-based, the left edge is @378–383 = `00 11 50 82 16 52`, and the fragment is @384–386 = `38 37 43` (row a2_07). Adopted as premises (not re-litigated): battery-tail-385-rerun-43poly NULL (bare-NP fence under the adjectival-37 frame; "52-38" unit collapse KILLed via @1343; 11="la" @379 separated by "50 82 16"); battery-val-52-38-unit KILL; val-52-630-frame PROMOTE (52 split-shaped: verb-tier "qui 52", adverb-tier "ne 52 [INF]"/"la 52", sub-lexical "t52"/"pre52"); battery-val-16-a-vs-est (16='a'/'est', both verb readings; at this window "82 16 52" = "m'a/m'est [52]").

## Window-level evidence (byte-traced)

Probe zone: @378–383 `00 11 50 82 16 52`. Wider left context @355–377 scanned for determiner-valued cells: 47="ce" @357/@363, 11="la" @358 — all 20+ cells away with intervening finite verb clauses (48-verb-stem @361/@365/@377, 62 @360) — no cross-clausal determiner heading is grammatical. The only proximate determiner-valued cell is 11 @379.

Candidate-by-candidate:

1. **00 @378** = "pour" (A9 granted). Preposition. Cannot head an NP as a determiner. EXCLUDED.
2. **11 @379** = "la" (pencil GT). Genuine determiner, but heading '38 37 43' requires spanning five cells: "la [50 82 16 52 38] 37 [43]". 82="m" is a pencil letter, so "50-82-16" is word-internal composition; the required parse stacks "50-82-16" (word), 52, 38, 37 as four prenominal modifiers before the 43 head — six stacked items with zero battery-grade evidence stream-wide for any "la"-headed span of >1 intervening cell. Additionally "52-38" unit collapse is KILLed (no stack reduction), and 16 at this window is verb-shaped ("m'a/m'est"), which a determiner cannot span. EXCLUDED with cause.
3. **50 @380** — value open (50="ver" killed; frameA-50-value NULL, "value stays open"). 82="m" word-internal inside "50 82 16" binds 50 into sub-lexical composition; no determiner arm for 50 exists in any battery or the registry. EXCLUDED (no determiner arm on record).
4. **82 @381** = "m" (pencil GT letter). Sub-lexical by definition. Cannot be a determiner. EXCLUDED.
5. **16 @382** — battery-grade readings are 'a'/'est' (both finite-verb; val-16-a-vs-est). At this very window: "82 16 52" = "m'a/m'est [52]". A finite verb cannot be a determiner. EXCLUDED with cause (locus-level verb reading).
6. **52 @383** — determiner arm unattested (parent report: adjective {même/seule} / nominal / clitic arms live; determiner never shown). val-52-630-frame (2026-10-09) confirms 52 split-shaped across verb-tier, adverb-tier, and sub-lexical tier — no determiner tier. EXCLUDED with cause.

**Result: zero battery-grade determiner candidates in the left edge.**

## Per-clause pass/fail

- **C1 — FAIL.** No candidate survives: 00 is a preposition, 82 a letter, 16 a verb at this locus, 52 has no determiner tier, 50 has no determiner arm, and 11="la" cannot span five cells at battery grade.
- **C2 — FIRES.** Per the bar: the bare-NP reading stays fenced with cause — under the adjectival-37 frame, the '38 37 43' fragment has no determiner and no battery-grade external determiner candidate; a bare NP is ungrammatical in 1841 French as a complete phrase.

## Adverses answered

- **"37-adjectival arm is the rival reading of the same bytes":** answered — the probe ran under the anchor-claim frame (37 adjectival, fragment needs an external determiner). The S5 rival reading (37="le" as determiner, determining the fragment internally) is NOT touched by this fence: if S5 holds, no external determiner was ever needed. That fork stays live in red-team venue (`s5-37-385-adjudicate` already queued). The bare-NP fence applies strictly under the adjectival-37 frame.
- **"The 43-noun premise changes everything":** answered — 43=["noun","cls"] is adopted (R20-117), but nominality of the head does not supply the missing determiner.

## Standing-state check

No red-team verdict contradicted or downgraded (R20-117 adopted; 43 nominal intact; §7 intact — no polyvalence declared). battery-adj-37-385-gate's fence and battery-val-52-38-unit's kill honored, not duplicated. R5005, sealed gates, red-team queue untouched.

## Follow-ups proposed (null → 1–3 required; all verified ABSENT from battery-queue.json)

1. `la-379-span-test` (P4) — census stream-wide whether 11="la" ever heads a span with 1–5 intervening cells; if zero, the @379→@384 five-cell span is distributionally dead, hardening this fence.
2. `det-52-arm-kill` (P3) — formal kill-grade test of 52's determiner arm (currently only "unattested"); a kill closes the last open-class candidate at @383.
3. `np-43-determiner-census` (P4) — census all 43-windows' left edges for attested determiners heading 43-NPs; calibrates what a determined 43-NP looks like stream-wide against the @385 bare-NP fence.

## Bookkeeping

- Lock `locks/det-385-leftedge.lock` created on start (agent id + 2026-10-09T17:58:30Z), deleted on completion.
- Report filed: `code/crowd17/report_inbox/battery-det-385-leftedge.md`.
- Queue: `det-385-leftedge` → status `verdict`, verdict `{"result": "null", "report": "code/crowd17/report_inbox/battery-det-385-leftedge.md", "date": "2026-10-09"}` via temp-file + rename (pre-write assert: was `queued`/verdictless; post-write JSON re-validated; own entry only; no downgrade).
