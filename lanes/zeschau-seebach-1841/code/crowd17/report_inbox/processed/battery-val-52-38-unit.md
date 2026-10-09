# Battery report: val-52-38-unit — KILL

- Target id: `val-52-38-unit`
- Claim: "'52 38' forms a prenominal-adjective unit at @384/@1343 per the la-523743-adjective Type-A precedent, with 52's live adjective arm {meme/seule}."
- Date: 2026-10-09
- Worker: battery worker (subagent b009ece3-9fe6-48fc-bef5-c82648685520)
- Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json + data/upstream-ct_R5005.txt, parsed per code/side-keyhunt/repair_parse.py). Asserted in-session: 1,847 pairs, 96 unique. `canonical.py` never used. R5005, sealed gates, red-team queue untouched. No data invented.

Terms (ASD-STE100): "prenominal-adjective unit" = one adjective word (or fixed compound) that sits directly before the noun it modifies, e.g. "la [52-37] [43-noun]" (Type-A precedent). "Kill grade" = a window forces the claim false under standing values and 1841 French grammar. Offsets below are 0-based stream indices (1-based lane convention = index+1).

## Bar (verbatim from battery-queue.json)

> Test '52 38' as a prenominal-adjective unit at @384/@1343 per the la-523743-adjective Type-A precedent (52's adjective arm {meme/seule} is live).

## Bar as numbered clauses (restated before testing)

1. Parse @384 under the prenominal-adjective unit (Type-A: unit directly before its head noun).
2. Parse @1343 under the prenominal-adjective unit.
3. Name 52's value iff the unit parses at both windows with zero new assumptions; else kill the unit claim iff a window forces it false, or fence with stated cause.

## Method

1. Read BATTERY-PROTOCOL.md first. Created `code/crowd17/next-token/locks/val-52-38-unit.lock` on start (deleted on completion).
2. Re-derived the stream in-session; byte-confirmed both loci: @384 = '38' (predecessor @383 = '52'), @1343 = '38' (predecessor @1342 = '52').
3. Censused the '52 38' bigram stream-wide and profiled 38 (n=7).
4. Read the Type-A precedent report (report_inbox/processed/battery-la-523743-adjective.md) and adopted its findings as premises (not re-litigated): "52-37" fills the prenominal adjective slot before head noun 43 at @1123/@1721; 37's adjective candidacy is unanchored (NULL, clause 3 none found); @385 '52-38-37-43' noted as "compatible with adjective slot, but 38's class is open → not confirmable".

## Window-level evidence

**Bigram census (byte-exact):** '52 38' occurs exactly **2×** stream-wide — @383–384 and @1342–1343, i.e. exactly the two bar windows. The unit claim lives or dies on these two windows alone; no other window corroborates the composition.

**W1 @384 (row a2_07):** `50 82 16 | 52 38 | 37 43 91 36` — full context @375–398: `85 82 48 00 11 50 82 16 52 38 37 43 91 36 62 91 84 73 34 67 64 79 82 48`. The noun 43 follows, but **37 intervenes** between 38 and 43. For "52-38" to fill the Type-A prenominal slot before 43, 37 must be adjectival (a stacked second prenominal adjective). 37's adjective candidacy is unanchored at battery grade (la-523743-adjective NULL: no independent adjective-slot confirmation anywhere; @385 itself was listed as merely "compatible, not confirmable"). Assuming 37 adjectival here is a new assumption → clause 3's naming condition (zero new assumptions) cannot fire. As a *unit parse*, W1 is admissible only conditionally: "[52-38]-adj [37-?] 43" with 37's class fenced.

**W4 @1343 (row a7_05):** `65 64 | 52 38 | 47 86 66 73 34 62 48 77 78 94 82 06 | 52 37 64` — full context @1335–1358: `86 71 64 60 08 65 64 52 38 47 86 66 73 34 62 48 77 78 94 82 06 52 37 64`. The follower of 38 is **47 = 'ce'** (granted allophone-tier, §7 A4/A11). The window tail after the unit is `47 86 66 73 34 62 48 77 78 94 82 06` — **no noun follows the unit anywhere**. The nearest nominal, 65 (R18 noun class), stands *before* the unit (@1340). A prenominal adjective unit must precede its head noun; French licenses no adjective-before-pronoun order ("même ce", "seule ce" are ungrammatical as units). The Type-A precedent's core condition (unit directly prenominal before a head noun) is unmeetable here. **W4 forces the uniform unit claim false at kill grade.**

**38's remaining windows (n=7):** @826 `59 38 82`, @1113 `65 38 30` (determiner-38 kill-grade dead here, per target evidence), @1469 `62 38 26`, @1650 `03 38 82`, @1828 `86 29 82 38 83`. None sits in prenominal-adjective position before a noun — consistent with the bigram census finding (no corroborating composition anywhere).

## Per-clause pass/fail

1. **W1 @384 — CONDITIONAL PASS only.** Parses as a prenominal-adjective unit solely under the new assumption that 37 is adjectival at @385; 37's adjective arm is unanchored (adopted premise). Naming condition not met.
2. **W4 @1343 — FAIL at kill grade.** No head noun follows the unit; follower is the granted pronoun 'ce'. The prenominal-adjective-unit parse is ungrammatical and unrescuable.
3. **Naming — does not fire.** Zero-assumption parse unattainable (W1 needs a new assumption; W4 is kill-grade dead).

## Adverse answered

- "With the determiner arm dead, adjective-38 at @385 = three stacked prenominal adjectives with no determiner — ungrammatical bare NP — so the unit must do real work at @384/@1343." — **Answered by the W4 kill.** At W1 the unit would do the claimed work (collapsing the stack to "[52-38]-adj 37-adj 43"), but at W4 the unit does no work at all: even merged into one adjective, "[52-38] ce [86]" cannot occupy a prenominal-adjective slot with no following noun. The adverse's demand is met negatively — the unit fails to do real work where tested.

## Verdict: KILL

Clause 2 fails at kill grade: @1343 forces the claim "'52 38' forms a prenominal-adjective unit" false. The unit hypothesis is rejected as a uniform reading. Scope: kills only the "52-38"-as-prenominal-adjective-unit claim. 52's adjective arm stays live at its Type-A windows (@1123/@1721 "la [52-37] 43", adopted); 38's class stays open; the la-523743-adjective NULL verdict is untouched (not duplicated); no standing or red-team verdict contradicted or downgraded; §7 intact. Canonical-stream caveat stands (rows a2_07/a7_05 offsets unvalidated).

No follow-ups are mandated for a kill (protocol §4). Observations for the supervisor (not findings): 38's class remains the keyhole for the @384–386 residual ("52-38-37-43"); 38's 5 non-52 windows (@826/@1113/@1469/@1650/@1828) are the natural class probe once a '52-38' composition is off the table.

## Bookkeeping

- Queue: `val-52-38-unit` → status `verdict`, verdict `{"result": "kill", "report": "code/crowd17/report_inbox/battery-val-52-38-unit.md", "date": "2026-10-09"}` via temp-file + rename (pre-write assert: was `queued`/verdictless; post-write JSON re-validated; own entry only; no downgrade).
- Lock created on start (agent id + UTC timestamp), deleted on completion.
