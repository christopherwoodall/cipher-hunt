# Battery report: val-37ent-adjective

- Target id: `val-37ent-adjective`
- Claim: Identify which '-ent' adjective '37ent' is (evident/prudent/different/...) at @183-184.
- Date: 2026-10-09
- Worker: battery worker (subagent 21a17c9c-7731-4500-b0c8-3c63d0e5e72d)
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py`; asserts 1847/96 held in-session). `canonical.py` never used. R5005, sealed gates, red-team queue untouched.

Terms (ASD-STE100): "A1" = the granted 37/32/42 predicative frames (R15-A1, confirmed R20-083). "06='ent'" = the conditional PROMOTE of 06 as the word-final suffix "-ent" (R17-007, carried R20-011). "Battery grade" = the evidence standard of this pipeline.

## Gate check

Gate trigger was the R17-007 conditional promote of 06='ent'. Verified satisfied: R20-011 records "ent-06 — DUPLICATE (R17-007 GRANT PROMOTE, conditional)". A1 confirmed standing (R20-083 DUPLICATE/CONFIRM STANDING). Gate fired; testing proceeded.

## Bar (verbatim, pre-registered before testing)

"promote iff the named '-ent' adjective parses @181-187 with the promoted 06='ent' word-final and the A1 predicative frame holds; needs a second window"

Numbered pass/fail clauses (restated before testing, not modified after):

1. **C1:** a named '-ent' adjective parses @181-187 with 06='ent' word-final and the A1 predicative frame holds → PROMOTE (joint with C2).
2. **C2:** a second window confirms the same adjective → PROMOTE (joint with C1).

Adverses listed: none.

## Method

1. Read BATTERY-PROTOCOL.md first. Created `code/crowd17/next-token/locks/val-37ent-adjective.lock` on start (agent id + 2026-10-09T18:26:36Z); no prior/stale lock.
2. Re-derived the repaired stream byte-exact in-session (1,847 pairs / 96 types asserted).
3. Adopted, never re-litigated: 64="qui" promoted; 23=verb class (23-1697-class PROMOTE, battery, today — @182 is its kill-grade "qui [23]" leg forcing finite verb); 00="pour" class-level (A9); 37/32/42 predicative frames (A1); 06='ent' conditional promote (R17-007/R20-011).
4. 1841 diplomatic French throughout.

## Findings

**Window byte-verified** (0-based @183–184, row a1_05):

```
@177=69 @178=14 @179=24 @180=87 @181=64(qui) @182=23(V) @183=37 @184=06(ent) @185=00(pour) @186=33 @187=16 @188=00 @189=66
```

**C1 analysis — the reading parses but the value is underdetermined:**

- The parse "qui [23-finite] [37-PRED] pour [33] [16]" is licensed: "qui" forces a finite verb (23's kill-grade leg), 37 takes the A1 predicative frame, 06='ent' sits word-final so "37 06" reads as one word "[Xent]" followed by "pour".
- Candidate pool is open: présent (1410 corpus hits), content (333), évident (330), différent (183), prudent (168), absent (105), urgent (99), innocent (96), violent (192), plus récent, fréquent, négligent, indulgent, éloquent — ranked by raw frequency in the 99-file period corpus.
- **No discriminator exists in the window:** 23's value is open (verb class only), 33's value is open, 16's value is open, 00's value is open at class level ("pour"). The adjective choice depends on the verb's semantics ("rendre évident" vs "sembler présent" vs "demeurer différent"), which is unvalued. No single adjective is forced. C1 FAILS — a value cannot be *named* at battery grade.

**C2 analysis — no second window exists:**

- Stream-wide census: the bigram "37 06" occurs **exactly once** (n=1/1847). @183 is a hapax spelling.
- n(37)=28; its other followers are word-level groups ({78×4, 43×3, 64×3, 01×3, 11×2, 77×2, 08×2...}) — the "06" follower is unique, so 37 has no other sub-lexical composition that could serve as a second leg for the same adjective.
- C2 FAILS by census: the bar's "needs a second window" clause cannot be met on this stream.

**Corpus consequence:** the period-corpus ranking shows the candidate field is wide and frequency-led by "présent" — but frequency is not a battery-grade naming leg, and no corpus frame can manufacture a second stream window. The underdetermination is structural.

## Per-clause pass/fail

1. **C1 — FAIL.** The "37ent" reading parses cleanly under A1 + 06='ent' word-final, but no single '-ent' adjective is forced; the value is underdetermined at battery grade.
2. **C2 — FAIL.** "37 06" is a stream-unique hapax (n=1); no second window exists.

## Verdict: NULL

The predicative "-ent adjective" reading of "37 06" is licensed and contradicts nothing, but it cannot be promoted: no adjective value can be named (C1) and no second confirming window exists (C2). The promote is blocked, not refuted.

## Scope

- Locus-level only (@183–184). Does not name 37's value, does not touch the A1 frame grant, does not touch 06='ent' (R17-007 conditional), 23=verb class, or any standing/red-team verdict. §7 intact.
- 37's other windows are untouched; the "37ent" spelling remains a live single-leg reading, not a killed one.

## Follow-ups proposed (§4, all verified ABSENT from battery-queue.json)

1. `val-23-182-semantic` (P3) — name 23's value at @182 (finite verb under "qui"); the verb's semantics ("rendre" vs "sembler" vs "demeurer") is the only byte-internal discriminator that could select the adjective.
2. `adj-ent-pour-frame-census` (P4) — corpus census: which -ent adjectives govern "pour + [NP/infinitif]" complements in 1841 French; ranks candidates for any future second leg.
3. `val-37-participle-183` (P4) — test the rival arm: 37 as past participle with "06" re-parsed (e.g., auxiliary/composition rival) at @183; closes the participle rival explicitly or re-opens the naming question.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-val-37ent-adjective.md` (this file).
- Queue: `val-37ent-adjective` queued → `verdict`/`null`, 2026-10-09 (pre-write assert passed — was queued/verdictless; temp-file + rename; JSON re-validated; own entry only; no downgrade).
- Lock `code/crowd17/next-token/locks/val-37ent-adjective.lock` created on start, deleted on completion (verified gone).
- R5005, sealed gate instances, red-team adjudication queue untouched.
