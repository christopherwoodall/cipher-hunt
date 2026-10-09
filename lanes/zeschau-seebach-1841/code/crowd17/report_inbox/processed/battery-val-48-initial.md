# Battery report: val-48-initial

- Target id: `val-48-initial`
- Claim: "Name 48's value at the two apparent word-initial loci (@1525 'la [48] par', @928 'par [48] m'); closes whether 48 has any standalone word-arm or is letter-tier everywhere."
- Date: 2026-10-09
- Worker: battery worker (subagent 8947b0a7-9923-4d0d-8847-0e8a81e3b1e4)
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py`; asserts 1847/96 held in-session). `canonical.py` never used. R5005, sealed gates, red-team queue untouched.
- Parent: `conj-20-642-subordinator` NULL (2026-10-09), which noted these two loci as "apparent word-initial" but did not test them.

Terms (ASD-STE100): "letter tier" = a cell spelling one letter inside a word (48='e' promoted, R17-003). "Word-initial locus" = 48 follows a granted whole word, so a word could begin at 48. "Fence" = the question is closed with stated cause; no value named.

## Bar (verbatim, pre-registered before testing)

"one value parsing both windows, or fence the initial-locus question."

Numbered pass/fail clauses (restated before testing, not modified after):

1. **C1:** One value of 48 parses BOTH @1525 ('la [48] par') and @928 ('par [48] m') as a standalone word or word-initial composition → name the value (PROMOTE).
2. **C2 (else-arm):** Fence the initial-locus question with stated cause → NULL (fence executed).

Adverses listed: none.

## Method

1. Read BATTERY-PROTOCOL.md first. Created `code/crowd17/next-token/locks/val-48-initial.lock` on start (agent id + 2026-10-09T19:07:52Z); no prior/stale lock; deleted on completion.
2. Re-derived the repaired stream byte-exact in-session (1,847 pairs / 96 types asserted).
3. Adopted standing (not re-litigated): 48='e' letter tier promoted (R17-003/A4); fem-e-48 PROMOTE (48 as feminine/inflectional -e, function-scoped); elision82-48-x1 PROMOTE ('82 48'="m'" @1229); kills 48="est"/"ne"/"de" and {48,94} homophone-set; A7-L2 "tout me [48-verb]" frame (value open); banked GT 11='la', 82='m'; granted 96='par'.
4. Ran a full 48 census (n=38) to test the claim's framing and both windows against every standing value.

## Findings

### F0 — the claim's framing is exhaustive (byte-exact)

n(48)=38 stream-wide. 48 follows a granted whole word at **exactly 2 loci**: @928 (left=96 'par') and @1525 (left=11 'la'). These are the claim's two loci — no other "apparent word-initial" 48 exists. Both loci byte-confirmed:
- @1525, row a8_00: `... 24 11 11 [48] 96 87 46 21 65 63` = "[24] la la [48] par ce que [21] [65] [63]"
- @928, row a5_10: `... 61 96 [48] 82 98 83 56 69 26` = "[61] par [48] m vient [83] [56] [69] [26]"

The "11 11" doubling at @1523–1524 is stream-unique (1/1847 bigrams).

### C1 — FAIL: no single value parses both windows

**48='e' (standing promoted value) has no licensed parse at either window:**

@1525 (neighbors 11='la' GT, 96='par' granted — both closed as words):
- standalone "e": no French word "e". Dead.
- word-initial "e"+96: contradicts the 96='par' grant. Dead at battery grade.
- word-final "la"+"e" = "lae": no French word. Dead.
- word-internal "laepar": contradicts both grants. Dead.

@928 (neighbors 96='par' granted, 82='m' GT letter):
- standalone "e": no French word. Dead.
- word-initial "em"+98: 98='vient' is LEAD (word) → "emvient" is no French word; "em" alone is no word. Dead.
- word-final "par"+"e" = "pare": contradicts the 96='par' grant. Dead at battery grade.
- word-internal "parem": no French word. Dead.

**No rival value parses both either:**
- Standalone-word 48: @1525 needs a feminine word after "la"; @928 needs a word after "par" with "m"+98 composing after it. No single French word fits both slots; 48 has no noun class standing, and the kills ("est"/"ne"/"de") remove the only plausible one-letter-word candidates. Naming a novel word value would be a second 48 value = §7 red-team venue, with zero battery-grade legs.
- Verb arm (A7-L2): "la [V] par" and "par [V]" are both ungrammatical in French. Dead at both windows.

C1 FAILS. No value named.

### C2 — FIRES: the initial-locus question is fenced

Stated cause: 48 is letter-tier ('e') everywhere it parses under standing values (R17-003; fem-e-48; elision82-48-x1). The only two windows where 48 follows a granted word — the only windows where a word-initial reading is even geometrically available — are residuals: at both, every licensed composition of 48='e' is blocked (neighbors are closed granted words; no French "e"-word, "lae", "pare", or "emvient" exists), and no rival value has battery-grade standing at either. The "word-initial" appearance is adjacency without composition, not evidence of a word arm. 48 has no standalone word-arm at battery grade: it is letter-tier everywhere it parses, and unparsed at these two loci.

## Scope

- Fences only the initial-locus/standalone-word question for 48. Untouched: 48='e' letter-tier promote (R17-003), fem-e-48 function scope, elision82-48-x1, the A7-L2 48-verb frame, all kills, §7 (67 et/veut sole polyvalence). No standing or red-team verdict contradicted, downgraded, or re-litigated.
- The two loci remain byte-secure residuals; a future red-team 48 ruling or a 98 re-value at @930 could re-open @928.
- Canonical-stream caveat stands (rows a8_00/a5_10 offsets unvalidated, 68/70).

## Verdict: NULL (fence executed)

Per lane precedent for name-or-fence bars (syll-38-value-census; conj-20-642-subordinator), the fence arm firing resolves to NULL, not KILL.

## Follow-ups (nulls regenerate work; all verified ABSENT from battery-queue.json)

1. `resid-48-1525` (P4) — resolve @1525's "11 11 48 96": the stream-unique "la la" doubling plus the uncomposable 48. Bar: test @1523's 11 as word-final (licensed re-segmentation) vs canonical-offset artifact; or fence @1525 as a double residual with stated cause.
2. `resid-48-928` (P4) — resolve @928's "96 48 82 98": test 98's value at @930. Bar: if a non-'vient' 98 licenses "em[98]" composition, name it; else fence @928 as a residual with stated cause.
3. `distrib-48-tier-census` (P4) — full 38-window tier inventory for 48 (word-final -e / inflectional -e / elision / verb-stem / residual). Bar: every window classified with stated tier, or the residual set fenced; closes "letter-tier everywhere" positively.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-val-48-initial.md` (this file).
- Queue: `val-48-initial` queued → `verdict`/`null`, 2026-10-09 (pre-write assert passed — was queued/verdictless; temp-file + rename; JSON re-validated; own entry only; no downgrade).
- Lock `code/crowd17/next-token/locks/val-48-initial.lock` created on start, deleted on completion (verified gone).
- R5005, sealed gate instances, red-team adjudication queue untouched.
