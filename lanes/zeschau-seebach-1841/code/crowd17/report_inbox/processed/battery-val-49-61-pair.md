# Battery `val-49-61-pair` — verdict: NULL (fence executed)

- Target id: `val-49-61-pair`
- Claim: "name 49's and 61's classes at the @365-367 trigram; the load-bearing unknown for this window."
- Date: 2026-10-09
- Worker: battery worker (subagent 9d4afe23-16b9-412d-8796-256cc4330ad2)
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py`; asserts 1847/96 held in-session). `canonical.py` never used. R5005, sealed gates, red-team queue untouched.

Terms (ASD-STE100): "frame-leg" = a window where the hypothesized class parses with zero new assumptions under standing values. "Battery grade" = the evidence standard of this pipeline.

## Bar (verbatim, pre-registered before testing)

"name 49's and 61's classes at the @365-367 trigram."

Numbered pass/fail clauses (restated before testing, not modified after):

1. **C1:** 49's class is named at @366 with ≥1 battery-grade frame-leg.
2. **C2:** 61's class is named at @367 with ≥1 battery-grade frame-leg.

Adverses (from queue): supervisor note 2026-10-09 — noun-49 fenced globally by noun-49-nonchain (fence executed, battery grade); noun option closed for 49 at @365–367.

## Method

1. Read BATTERY-PROTOCOL.md first. Created `code/crowd17/next-token/locks/val-49-61-pair.lock` on start (agent id + 2026-10-09T19:07:46Z); no prior/stale lock; will delete on completion.
2. Re-derived the repaired stream byte-exact in-session (1,847 pairs / 96 types asserted).
3. Adopted (not re-litigated) the standing 49/61 record: 49 — verb/determiner/relative-pronoun killed globally (formula-49-value), adjective killed at kill grade (adj-49-420-366), adverb fenced at [N][49][Vfin] (adv-49-653-990), noun fenced globally (noun-49-nonchain PROMOTE fence); surviving tier syllable/letter. 61 — "pren" KILLED at kill grade (seg-61-pren-polyvalence; @367 "prenpre" unreadable), adjective fenced at @645 (val-61-646-secondleg-sweep NULL), premier-family conditional at ordinal slots (premier-61-admit-fence PROMOTE), "premier pre fois" anti-leg stands at @367, 49/61/70 boundary fenced unresolvable (reseg-367-4961-bound NULL).
4. Tested each surviving arm for a positive frame-leg at the locus and stream-wide. 1841 diplomatic French throughout.

## Locus (byte-exact, 0-based, row a2_06)

`@365=48("e", prom, letter tier) @366=49(unvalued) @367=61(unvalued) @368=70("pre", gt) @369=17("fois", prom) @370=06("ent", prom)`

Left context @362–364: `76(noun,prom) 47("ce",prom) 78("ver",lead)`. Full: "…ce ver e [49] [61] pre fois ent [21-N] [65-N] [63-verb]…".

49 census: n=12, prev {48:1, 78:2, 46:1, 76:3, 29:1, 24:2, 74:1, 54:1}, fol {61:1, 74:5, 36:1, 24:2, 16:1, 64:2}.

## Per-clause results

### C1 — 49's class: FAIL (no battery-grade frame-leg)

Enumerated surviving arms for 49 at @366 (noun, adjective, verb, determiner, relative-pronoun all dead/fenced per the adopted record):

- **Letter/syllable tier (the only surviving tier):** at @366 the letter-tier reading is "48(e,letter) [49-letter] [61]" — a letter string "e[49]" with unvalued 61 beside it. Licensing it needs 49's letter VALUE named (ungranted assumption 1) and 61 resolved (ungranted assumption 2). Stream-wide, 49's contact profile has 8 distinct predecessors and 6 distinct followers with no dominant composition neighbor; the lane's letter-naming bar (cf. val-13-567, val-74-letter) needs a byte-evidenced letter value à la 40='e', which does not exist for 49. No positive frame-leg at battery grade.
- The strongest contact, "49 74" ×5, cannot supply the leg: chain-follower-class KILL fenced the single-word "49 74 74" reading, and 74's class is open.

No class nameable → C1 FAIL.

### C2 — 61's class: FAIL (no battery-grade frame-leg)

Enumerated arms for 61 at @367:

- **"pren":** kill-grade dead globally (seg-61-pren-polyvalence); @367 "prenpre" is unreadable French.
- **Adjective:** fenced at the only determiner-adjacent window (@645); @367 has no determiner host.
- **Premier-family nominal:** conditional on ordinal slots (@281, @1556); the "premier pre fois" anti-leg stands at @367 (recorded, not re-litigated).
- **Bare nominal / word-composition:** no licensed frame at "[61] pre fois ent [N] [N]" — reseg-367-4961-bound already fenced this exact boundary as unresolvable at battery grade (quadruple hapax, every segmentation arm fails on byte-grounded grammar grounds).

No class nameable → C2 FAIL.

## Verdict: NULL (fence executed)

Both naming arms fail: 49's surviving tier is letter/syllable with no positive frame-leg at @366 or stream-wide; 61's surviving arms have no positive frame-leg at @367. This is a fence, not a kill — no window forces the claim false; the failures rest on unvalued cells (a future named letter-49 value, or a nominal-61 value, could re-open the trigram). §7 intact (no split declared; 67 remains the sole polyvalence). No standing/red-team verdict contradicted or downgraded. Canonical-stream caveat stands (row a2_06 offset unvalidated).

## Follow-ups (nulls regenerate work; all verified ABSENT from battery-queue.json)

1. `letter-49-collocation` (P4) — build 49's letter-tier collocation profile across all 12 windows à la the 40='e' model; name the letter with byte evidence or fence letter-49.
2. `nominal-61-367-test` (P4) — test "[61-N]" nominal reading at @367 ("[61] pre fois ent [21-N] [65-N]"); name-or-fence with stated cause.
3. `e49-wordinitial-366` (P4) — test "e[49]" as word-initial composition at @366 under a named letter-49 value; gated on letter-49-collocation naming a value.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-val-49-61-pair.md` (this file).
- Queue: `val-49-61-pair` queued → `verdict`/`null`, 2026-10-09 (pre-write assert passed — was queued/verdictless; temp-file + rename; JSON re-validated; own entry only; no downgrade).
- Lock `code/crowd17/next-token/locks/val-49-61-pair.lock` created on start, deleted on completion (verified gone).
- R5005, sealed gates, red-team adjudication queue untouched.
