# Battery verdict: val-42-219-queframe

- Target: `val-42-219-queframe` (battery-queue.json, priority 3, status queued)
- Claim: @219 'que [X]er [42]': the 'que' frame forces a verb before 42; test '29 42' as verb+'42-standalone' vs one word
- Source: val-42-lettertier NULL follow-up #2; queued by supervisor 2026-10-09
- Adverse: 42's tier open; do not force a classification

## Bar (verbatim, numbered)

Bar (verbatim): "identify the verb from 29's left context (no invented word); one parse must hold with stated values or fence"

- C1. Identify the verb from 29's left context using stated values only (no invented word).
- C2. One parse holds with stated values ('29 42' as verb+'42-standalone', or '29 42' as one word); else fence.

## Method

1. Read BATTERY-PROTOCOL.md first. Created `locks/val-42-219-queframe.lock` on start (agent a9374782-4d7a-431e-8e24-cba84c5e51fd, 2026-10-09T20:39:03Z); deleted on completion.
2. Re-derived the repaired stream in-session from `code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt` via the `repair_parse.py` parse function: 1,847 pairs, 96 types. `canonical.py` never used.
3. Offsets below are 0-based; the claim's "@219" is 1-based (= 0-based @218 = 29). Row offsets unvalidated (canonical-stream caveat stands).
4. Adopted (not re-litigated): pencil GT 46='que', 29='er'; provisional 59='est'; registry 24=['verb','cls']; val-42-lettertier NULL (the '29 42' one-word arm at @219 admits no er+X word); wordbound-63-29-373 ('er' standalone is a non-word; only licensed er-initial word is '29 40'='erre'); redteam-42-tier-input ('29 42'x3 has no uniform French word).

## Findings

### Locus (byte-confirmed)

0-based @216=59 @217=46 @218=29 @219=42 @220=16 @221=24 @222=89:

- 59='est' (provisional), 46='que' (pencil GT), 29='er' (pencil GT), 42=open, 16=open, 24=verb-class (registry).
- '29 42' is exactly 3x stream-wide (0-based 29 at @78, @218, @1143).

### C1 — verb identification from 29's left context: FAILS

The verb must end in 'er' at 0-based @218. Its stem material must come from the left context (@217=46, @216=59). Exhaustion under stated values:

- **A1. Verb = "46 29" one word ("quer"-final).** Requires 46 sub-lexical. 46='que' is pencil GT — banked ground truth, non-negotiable per §7; a battery cannot re-open it. Independently, the stem slot (@216=59='est') yields "estquer" — not a French word. DEAD.
- **A2. Verb = 29 alone ("er").** "er" is a non-word (adopted wordbound-63-29-373). DEAD.
- **A3. Verb = stem(@217) + "er".** @217=46='que' is a banked word, not a verb stem. DEAD.
- **A4. Elision "qu'errer" ("que"+"errer").** Parent val-42-lettertier already found "que"+"errer" ungrammatical (bare infinitive with no subject after complementizer "que"); additionally requires 42 to supply 'r' — 42's tier is open with no standing letter value, and the bar forbids invention. DEAD.
- **A5. Verb after 42 (@220=16/@221=24).** The claim requires the verb BEFORE 42; "que"+"er [42] [16]"+verb would need "er [42] [16]" to parse as subject NP or adverbial — "er" is a non-word. DEAD.

No verb is identifiable from 29's left context with stated values. C1 FAILS.

### C2 — one parse holds with stated values: FAILS → fence arm fires

- **Parse A ('29 42' = verb + '42-standalone').** Moot: no verb identified (C1 fails), so no verb+42 composition is statable. DEAD.
- **Parse B ('29 42' = one word).** Parent val-42-lettertier exhausted French "er"+X words (erreur, ermite, errer, ergot): at @219 "que"+"erreur"/"ermite" are ungrammatical (determiner missing), "que"+"errer" ungrammatical; longer "er*"-words need a determiner likewise absent. "29 42"x3 has no uniform French word (adopted redteam-42-tier-input). The only untested sub-arm, 42-as-letter-tier ("er"+[42-letter]), is blocked: 42's tier is open per the adverse and no standing letter value exists. DEAD at this window.

Neither parse holds with stated values. The bar's else-arm fires: **FENCE**.

The fence is evidentiary, not terminal: re-openable if (i) 42's tier/letter content is ever named (re-opens Parse B's letter arm), or (ii) the red team revisits 46's pencil GT at this window (re-opens A1) — both outside battery venue.

## Verdict: NULL (fence executed)

C1 FAIL / C2 fence-arm FIRES. No verb identifiable; neither '29 42' parse holds with stated values.

## Scope

- Fences only the verb-identification question at the @218–219 window. The parent val-42-lettertier NULL is not downgraded (this battery is its named successor arm); its one-word kill at this window is adopted, not re-litigated.
- Untouched: pencil GT 46='que' and 29='er' (upheld, not contradicted), 42's open tier (adverse honored — no classification forced), 24's verb class, §7 (no split declared), all standing/red-team verdicts.
- No standing or red-team verdict contradicted. Canonical-stream caveat stands.

## Follow-ups (for supervisor queuing; all verified ABSENT from battery-queue.json)

1. `val-42-219-letter` (P4) — name 42's letter content at 0-based @219; a named letter re-opens Parse B's "er"+letter arm, currently the only battery-grade path back into this window.
2. `seg-219-reseg` (P4) — test resegmentation at 0-based @217–219: "que er" is ungrammatical under standing values, so the contact is a segmentation residual pending either a named 42 or red-team action on 46.
3. `que-46-frame-census` (P4) — census all 46='que' windows for the following cell's class; determines whether @219's "que"+non-verb is an isolated anomaly or evidence the "que forces a verb" premise misdescribes the frame.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-val-42-219-queframe.md`
- Queue: `val-42-219-queframe` queued → `verdict`/`null`, 2026-10-09 (pre-write assert passed — was queued/verdictless; target-id-unique tmp `battery-queue.json.val-42-219-queframe.tmp` + rename; disk re-validated; own entry only; no downgrade)
- Lock `locks/val-42-219-queframe.lock`: created on start, deleted on completion (verified gone). R5005, sealed gates, red-team adjudication queue untouched.
