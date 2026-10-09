# Battery `31-08-word-host` — verdict: NULL (fence executed)

## Bar (verbatim, pre-registered)

"Word named at battery grade, or fence."

## Numbered clauses

- **C1:** name the [08][31] word at @881/@1488/@1520 at battery grade (word named with ≤1 ungranted assumption).
- **C2 (else-arm):** fence with stated cause if the word cannot be named at battery grade.

Claim (from queue): "name the [08][31] word at @881/@1488/@1520 once a candidate host class is licensed."

Adverses: none listed.

## Method

1. Read `BATTERY-PROTOCOL.md` first. Lock `code/crowd17/next-token/locks/31-08-word-host.lock` created on start (agent id + UTC timestamp); no stale lock pre-existed.
2. Re-derived the repaired 1,847-pair / 96-type stream in-session per `code/side-keyhunt/repair_parse.py` (pairs asserted 1,847; types 96). `canonical.py` never used.
3. Adopted, never re-litigated: `ce-08-31-frame` PROMOTE (2026-10-09: "87 08 31" @1488 = "ce" + [08][31]-word, 08 the word's initial letter, word-internal); `stem-08-letter-probe` PROMOTE (08 word-internal letter); `08-letter-geometry` PROMOTE (08 letter-tier, initial-skewed signature; no 08 value named); registry `31 = ["VERBAL", "cls"]` (red-team banked); 08 absent from registry; 87=ce promoted; 17=fois granted; §7 (67 sole polyvalence).
4. Tested the naming claim against the three loci byte-exact on the repaired stream.

## Gate check: is a candidate host class licensed?

**YES.** `ce-08-31-frame` PROMOTE licenses the host: [08][31] is one word with 08 as its initial letter, word-internal, appearing as "fois [08][31]" (@881), "ce [08][31]" (@1488), "et [08][31]" (@1520). The gate condition is satisfied; the bar is testable unconditionally.

## Window-level evidence (0-based @-offsets, repaired stream, byte-exact)

Bigram "08 31" is exactly 3× stream-wide: @881, @1488, @1520.

- @881 (a5_08): `…78 17('fois') [08] 31 79('tout') 68…` — left neighbor 17 free word, right neighbor 79 free word.
- @1488 (a7_10): `…24 87('ce') [08] 31 92 39…` — left neighbor 87 free word, right neighbor 92 (verb-class per R19, word-class, not letter-tier).
- @1520 (a7_11): `…91 67 [08] 31 24 11…` — left neighbor 67 (='et' by positional rule: 08 is not infinitive-shaped), right neighbor 24.

Both neighbors of each [08][31] token are free-word / word-class cells; no letter-tier cell contacts the bigram on either side. **The [08][31] token is a complete two-cell word in all three windows.** The word's spelling content is: initial letter 08 + syllable 31.

## Naming attempt

- 08's letter value: **open.** 08 is absent from the banked registry; three battery-grade attempts to constrain it (`homophone-08-12-n` fenced the n-sibling; `stem-08-letter-probe` landed word-internal without a value; `val-08-31-letter` is still **queued**, not run — it is the dedicated battery for naming 08's letter inside exactly these frames).
- 31's value: **open.** The registry banks only `31 = ["VERBAL", "cls"]` (class-level); no spelling value is named. Dedicated batteries `val-31-verb-test` and `val-31-1515-noun` are still queued.
- Naming the word therefore requires ≥2 ungranted assumptions (08's letter AND the word's identity within 31's verbal frame). Battery-grade naming bars in this lane allow ≤1. No French word can be spelled from two unvalued cells at battery grade; asserting one would invent values in violation of §3.

One structural note recorded, not adjudicated: the "ce [08][31]" frame (@1488) is a determiner frame demanding a nominal/adjectival word, while 31's banked class is VERBAL. The two are reconcilable (a nominal word can contain a verbal-shaped syllable; 31's class describes the cell, not the word's head class), so no contradiction is claimed — but the reconciliation depends on 08's letter, so it belongs to the naming battery, not this one. No standing/red-team verdict is contradicted or downgraded.

## Per-clause results

- **C1 — FAIL.** The word cannot be named at battery grade: 08's letter value is open (dedicated naming battery `val-08-31-letter` still queued) and 31 carries only a class-level VERBAL grant; naming needs ≥2 ungranted assumptions.
- **C2 — FIRES.** Fence with stated cause: the word's identity is unnameable at battery grade until 08's letter (and/or 31's spelling value) is named by the already-queued dedicated batteries.

This is a fence, not a kill: nothing forces the word's identity false; the block is unvalued cells in the active docket.

## Follow-ups proposed (all verified ABSENT from battery-queue.json)

1. `val-08-31-rerun-gated` (P4) — gated re-fire of this target's bar once `val-08-31-letter` names 08's letter (or `val-31-verb-test`/`val-31-1515-noun` names 31's value): name the [08][31] word then. Bar: word named at battery grade with ≤1 remaining ungranted assumption, or fence again with stated cause.
2. `word-class-08-31-3frames` (P3) — name the [08][31] word's grammatical class jointly across the three frames ("ce X" nominal demand at @1488 vs 31's banked VERBAL class): resolve the class geometry at battery grade or fence the nominal-host arm. No value naming; red-team venue if it touches 31's banked class.
3. `spell-08-31-word` (P3) — test whether 31 can spell letter-tier content inside the [08][31] word: iff 08's letter and 31's spelling are both named elsewhere, spell one French word with ≤1 ungranted assumption; gated on both namings.

## Bookkeeping

- Queue: `31-08-word-host` → `status: verdict`, result `null`, 2026-10-09 (pre-write assert: was `queued`/verdictless — passed; temp-file + rename; JSON re-validated from disk; own entry only; no downgrade).
- Lock `locks/31-08-word-host.lock` created on start, deleted on completion (verified below).
- R5005, sealed gate instances, red-team adjudication queue untouched. No standing/red-team verdict contradicted or downgraded; §7 intact. Canonical-stream caveat stands (rows a5_08/a7_10/a7_11 offsets unvalidated).
