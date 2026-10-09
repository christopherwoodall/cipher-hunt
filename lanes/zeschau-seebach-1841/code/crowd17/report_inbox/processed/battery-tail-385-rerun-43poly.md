# Battery tail-385-rerun-43poly — verdict: NULL (fence; bar's else-branch fires)

**Target:** `tail-385-rerun-43poly` (P2)
**Date:** 2026-10-09
**Worker:** battery worker (subagent 27157b87-d4f4-4ee2-8373-5e8b09345a42). Lock `locks/tail-385-rerun-43poly.lock` created on start, deleted on completion. `canonical.py` never used. R5005, sealed gate instances, red-team adjudication queue untouched.

## Bar (verbatim, pre-registered)

> "The "[43-noun]" premise gate must clear first: re-anchor @385 once redteam-43-polyvalence adjudicates 43's nominality."

**Numbered clauses (restated before testing):**
- C1: The [43-noun] premise gate clears — redteam-43-polyvalence adjudicates 43's nominality with a grant usable as premise.
- C2: Re-anchor @385 — "@385 ('[38] 37 [43-noun]') confirms 37 in a prenominal adjective slot", decided with >=2 independent legs under the premise; else fence.

## Method

Stream re-derived in-session from `code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`: 1,847 pairs / 96 types, asserts hold. All @-offsets 0-based queue convention. Adopted as premises (not re-litigated): battery-adj-37-385-gate NULL (38 adjective-shaped at W2/W3 locus-level; determiner-38 kill-grade dead at W3; W4 fenced; the "[43-noun]" premise was battery-closed); battery-val-52-38-unit KILL (the "52-38" prenominal-adjective-unit claim is dead at kill grade via @1343); battery-la-523743-adjective NULL (the la-vote recorded unanchored; full 28-window 37 census); R20-117 (redteam-43-polyvalence REJECT, confirm R19-064).

## Window-level evidence (byte-traced)

- **C1 evidence:** R20-117: "(a) the 15 noun legs stand (R19-045's class grant unchallenged); (b) the @21 infinitive is NOT accepted as a second value — no polyvalence declared (§7 DOA)". Holding: **43=["noun","cls"]**; @21 excluded. The premise gate clears at class level.
- **@385 locus (0-based; row a2_07, mid-row):** `... 382:16 383:52 384:38 385:37 386:43 387:91 388:36`. Byte-confirmed: "52 38 37 43" at @383–386. The brief's "@385" is 1-based lane convention for the 38 cell; 0-based 38 sits at @384, 37 at @385, 43 at @386.
- **"37 43" bigram census (byte-exact, stream-wide): exactly 3×** — @385 (this window), @1125 (a6_07), @1723 (a8_07). The latter two sit inside the la-vote windows ("11 52 37 43" @1123/@1721), where 37 is unit-internal to the Type-A "52-37" adjective unit. There is exactly ONE "37 [43]" window outside the vote itself.
- **38's class (adopted):** adjective-shaped at W2/W3 (locus-level); determiner arm kill-grade dead at W3 ("65 38 30 69" — determiner before "pas" with no nominal complement, ungrammatical); W4 fenced. The available @385 parse is therefore "[38-adj] 37 [43-noun]" — 37 between an adjective-shaped item and the granted head noun, with NO determiner in the window.
- **Left edge:** "16 52" precedes 38; wider context "00 11 50 82 16 | 52 38 37 43". The only granted determiner nearby is 11="la" at @379, separated by "50 82 16" — no battery-grade reading spans it (would require six stacked prenominal modifiers with zero evidence). 52's determiner arm is unattested (adjective {même/seule} / nominal / clitic arms live; determiner never shown). The "52-38" unit collapse is KILLed, so the stack cannot be reduced to "[52-38]-adj 37 43".

## Per-clause pass/fail

- **C1 — PASS.** R20-117 adjudicates 43's nominality with the class grant intact: 43=["noun","cls"]. The premise gate clears.
- **C2 — FAIL (fence).** The anchor claim needs >=2 independent legs; at most one exists:
  - Leg candidate 1 (@385 shape): 37 directly prenominal before granted-nominal 43 with adjective-shaped left neighbor — COMPATIBLE with an adjective slot, but the fragment has no determiner (bare NP, ungrammatical in 1841 French as a complete phrase) and 38's adjective shape is locus-level, not uniform. Compatible, not confirmatory.
  - Leg candidate 2: NONE. The only other "37 43" windows (@1125, @1723) are inside the la-vote windows themselves — using them as legs is circular (they ARE the vote being re-anchored).
  - The la-523743-adjective 28-window census found no other confirmable adjective-slot window for 37 ("qui 37" @676 and "23-37-06" @183 pull verb-shaped; @51 compatible but unconfirmable).
  - Per the bar's disjunction: **fence**. The @385 re-anchor does not fire; the la-vote stays unanchored.

## Adverses answered

- **S5 standing fence (37="le" MEDIUM, round-7):** NOT decided at battery level — fenced with stated cause. Under S5, @385 reads "52 38 le [43-noun]" (37 as determiner, not adjective), which directly contradicts the anchor claim's reading; s5-foundation returned NULL on 2026-10-09, so the contradiction is live and owned by the red-team venue, not resolved here.
- **"The 43-noun premise changes everything":** answered — it changes the head-noun leg (C1 passes) but does not supply the missing determiner, does not uniformize 38's class, and does not create a second independent "37 [43-noun]" window. The gate report's two blockers were independent; only one cleared.
- **"Circularity of the la-vote windows":** answered — @1125/@1723 explicitly excluded as legs; the fence does not double-count the vote as its own anchor.

## Standing-state check

No red-team verdict contradicted or downgraded (R20-117's 43=["noun","cls"] adopted; R19-045 intact; no polyvalence declared). battery-adj-37-385-gate's fence and battery-val-52-38-unit's kill honored, not duplicated. §7 intact. R5005, sealed gates, red-team queue untouched.

## Follow-ups proposed (null → 1–3 required; all verified absent from queue)

1. `det-385-leftedge` (P3) — probe the @385 left edge ("50 82 16 52", @379–383) for a battery-grade determiner candidate heading the "38 37 43" fragment; if none, the bare-NP reading stays fenced with cause.
2. `adj-37-independent-slot` (P3) — census "37 [granted-noun-head]" prenominal windows outside the 43 family (e.g. before 65/68/69-class nouns) to supply the missing independent adjective-slot leg for 37.
3. `s5-37-385-adjudicate` (P2) — escalate to red-team venue: @385 under 37="le" (S5) vs 37-adjectival are mutually exclusive readings of the same bytes; battery cannot decide (s5-foundation NULL).

## Bookkeeping

- Lock `locks/tail-385-rerun-43poly.lock` created on start (agent id + UTC timestamp), deleted on completion.
- Report filed: `code/crowd17/report_inbox/battery-tail-385-rerun-43poly.md`.
- Queue: `tail-385-rerun-43poly` → status `verdict`, verdict `{"result": "null", "report": "code/crowd17/report_inbox/battery-tail-385-rerun-43poly.md", "date": "2026-10-09"}` via temp-file + rename (pre-write assert: was `queued`/verdictless; post-write JSON re-validated; own entry only; no downgrade).
