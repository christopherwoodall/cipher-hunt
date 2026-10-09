# Battery verdict: sait-veut-24-discriminator

- Target: `sait-veut-24-discriminator` (battery-queue.json, priority 3, status queued)
- Claim: "Find a battery-grade discriminator between "sait" and "veut" for 24 across all 52 windows; most promising: indirect-interrogative frames ("savoir" licenses "si"/"comment"/"ou" + clause; "vouloir" licenses "que" + subjunctive)"
- Evidence (pre-registered): "null-mandated follow-up from code/crowd17/report_inbox/battery-val-24-1132-name.md"

## Bar (verbatim, pre-registered BEFORE testing)

"Name the value or fence as value-split"

Numbered clauses:
- C1: Name the value ("sait" or "veut") for 24 at battery grade across the windows.
- C2: Else fence the sait/veut value question as a value-split with stated cause.

## Method

Re-derived the repaired 1,847-pair / 96-type stream in-session from `data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json` (parsed per `repair_parse.py`; asserts held: 1,847 pairs, 96 types). `canonical.py` never used. Rendered all 52 windows of 24 with ±2 context. Applied R24 (R20-129, declared): 24='en' iff follower=85 — 5 windows (@732/@955/@1438/@1693/@1754) are 'en' and out of scope for sait/veut. Tested every frame class among the remaining 47 for sait-vs-veut discrimination, plus the claim's two "most promising" routes.

## Findings

**Scope reduction (R24):** 5/52 windows are 24='en' (follower 85). The discriminator hunt covers the 47 finite/modal windows.

**The claim's two most promising routes are untestable:**
1. **Indirect interrogatives** ("sait si/comment/ou"): ZERO "24 46" windows stream-wide, and no interrogative types ("si"/"comment"/"ou") are named anywhere in the standing records. No window, no types — untestable.
2. **"que" + subjunctive ("vouloir") vs "que" + indicative ("savoir")**: ZERO "24 46" windows stream-wide; mood is unmarked in the cipher. Untestable.

**Frame-by-frame test on all 47 finite/modal windows — "sait" and "veut" parse identically in every frame class:**

| Frame | n | "sait" | "veut" | Result |
|---|---|---|---|---|
| 24->87 ("ce"-frames) | 10 | "sait ce que/qui", "sait cela" | "veut ce que/qui", "veut cela" | identical |
| 24->82 ("m'" clitic) | 4 | clitic object | clitic object | identical |
| 24->30 ("pas") | 3 | "ne sait pas" | "ne veut pas" | identical |
| 24->89 (noun-LEAD) | 3 | noun DO | noun DO | identical |
| 24->37 (predicative A1) | 2 | both reject predicative complements | both reject | identical (both fail) |
| 24->80 (verb-frame A8) | 2 | "sait [INF]" | "veut [INF]" | identical |
| 24->26 (26 split) | 2 | noun reading | noun reading | identical |
| 24->41 (41 finite-verb cls) | 2 | both ungrammatical ("*sait vient") | both ungrammatical | identical (both fail) |
| 24->65 (65 noun-cls) | 2 | noun DO | noun DO | identical |
| 24->49 (49 unvalued) | 2 | fits | fits | identical |
| 24->48 (48='e' infl) | 2 | sub-lexical | sub-lexical | identical |
| 24->88 (88 verb-cls) | 1 | ungrammatical | ungrammatical | identical (both fail) |
| 24->56 (56 unvalued) | 1 | fits | fits | identical |
| 24->47 (47='ce') | 1 | "sait ce"/"sait cela" | "veut ce"/"veut cela" | identical |
| 24->42 (42 split) | 1 | fits | fits | identical |
| 24->24 | 1 | "*sait sait" | "*veut veut" | identical (both fail) |
| 24->06 ('ent') | 1 | "savent" 3pl | "veulent" 3pl | identical |
| 24->02 (02 finite-verb cls) | 1 | ungrammatical | ungrammatical | identical (both fail) |
| 24->77 ("le", @1132) | 1 | "sait le faire" (parent) | "veut le faire" (parent) | identical |
| 24->03 (03 split) | 1 | fits | fits | identical |
| 24->00 ("pour", @1492) | 1 | "*sait pour" ungrammatical | "veut pour" needs understood object + 66 as noun (both ungranted) | not battery-grade either way |
| 24->11 ("la", @1522) | 1 | "sait la" | "veut la" | identical |
| 24->74 (74 split) | 1 | fits | fits | identical |
| 24->53 (53 unvalued) | 1 | fits | fits | identical |

**Additional routes considered and rejected:**
- **"24 86"** (direct infinitive complement): ZERO windows stream-wide. Untestable.
- **"24 00 46"** ("pour que"): ZERO windows. Untestable.
- **Subject animacy**: both "savoir" and "vouloir" require sentient subjects (adopted from parent). No discriminator.
- **Corpus frequency**: frequency cannot name a value (val-03-value-census precedent: parsing != naming). Not a discriminator.
- **67's "veut" polyvalence**: 67="veut" (positional rule) coexisting with 24="veut" would be a homophone set (cf. 23~26, 20~17 splits) — allowed, not a discriminator.

**The single asymmetric window (@1492, "24 00") is not battery-grade:** "sait pour [66]" is ungrammatical, but "veut pour [66]" requires an understood direct object AND 66 as a noun — 66's class at @1494 is open (poly-66-split). Both readings cost ungranted assumptions; the asymmetry cannot be stated at battery grade.

## Verdict: NULL

C1 FAILS: no battery-grade discriminator selects "sait" over "veut" (or vice versa) in any of the 47 finite/modal windows. The two most promising routes from the claim have zero windows and zero named types. This is substantive inconclusiveness, not a data gap — every frame class is rendered and exhausted.

C2 FIRES: the sait/veut value question is **fenced as a value-split** — 24's finite/modal value splits "sait"/"veut", undecidable at battery grade. This joins the standing split-shaped packages (03, 09, 26, 38, 41, 42, 52, 55, 60, 66, 74, 85, 86, 91, 94, 01, 13) as red-team docket input. No polyvalence is declared (protocol §7: 67 et/veut remains the sole true polyvalence).

**Scope:** value-level only, 47 finite/modal windows. Untouched: R24 (24='en' iff follower=85), R17-009 (24 finite/modal verb class), 24=["verb","cls"] registry, the 24-en-verb-conflict red-team escalation, parent val-24-1132-name NULL, §7. No standing/red-team verdict contradicted or downgraded. Canonical-stream caveat stands (68 of 70 upstream row offsets unvalidated).

## Follow-ups proposed (§4, all verified ABSENT from battery-queue.json)

1. `sait-veut-corpus-frame` (P4, gather-only) — corpus census: in 1841 French, do "savoir" and "vouloir" differ in "ce que/qui" vs bare-"ce"/"cela" complement rates at scale? Evidence feed for the red-team 24 docket; cannot name a value (parsing != naming), but informs the split adjudication.
2. `sait-veut-que-rerun` (P4, gated) — re-arm the que-complement discriminator ("vouloir"+"que"+subjunctive vs "savoir"+"que"+indicative) iff a "24 46" window is ever licensed; currently zero stream-wide. Do not dispatch until a "24 46" window exists.

Not duplicated: `val-37-1130-frame` and `dir-24-cela-uniform` (parent's follow-ups, already queued); `cela-87-11-reseg` and `trans-24-cela-scale` (trans-24-ce-corpus follow-ups, already queued).

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-sait-veut-24-discriminator.md` (this file).
- Queue: `sait-veut-24-discriminator` queued → `verdict`/`null`, 2026-10-09 (pre-write assert passed — was queued/verdictless; target-id-unique tmp `battery-queue.json.sait-veut-24-discriminator.tmp` + atomic rename; JSON re-validated from disk; own entry only; no downgrade).
- Lock `code/crowd17/next-token/locks/sait-veut-24-discriminator.lock`: created on start (2026-10-09T21:19:19Z, no stale lock), deleted on completion (verified gone).
- R5005, sealed gates, red-team adjudication queue untouched.
