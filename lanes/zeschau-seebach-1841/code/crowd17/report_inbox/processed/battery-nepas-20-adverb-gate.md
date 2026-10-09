# Battery report: nepas-20-adverb-gate

**Target:** `nepas-20-adverb-gate` (P2)
**Date:** 2026-10-09
**Verdict:** PROMOTE (the (c2) loophole is closed; inf-20-nepas's verbal-slot forcing at @1703 hardened to unconditional)

## Bar (verbatim from queue)

"KILL the adverb rescue iff 62 is non-verbal at @1703 (62='il' holds there) - hardening this battery's verbal-slot forcing to unconditional; or DEMONSTRATE 62 verbal there, which re-opens the verbal-20 question"

## Bar restated as numbered clauses

1. (C1) Kill the adverb rescue ("ne pas [20-adv] [62-inf]" at @1703) iff 62 is non-verbal at @1703.
2. (C2) If 62 is demonstrated verbal at @1703, the verbal-20 question re-opens and the kill does not fire.

## Method

Re-derived the repaired 1,847-pair / 96-type stream in-session from
`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`
(byte-exact tokenizer, 0-based; asserts held: 1,847 pairs, 96 types).
`canonical.py` never used. R5005, sealed gates, red-team queue untouched.
Lock created on start, deleted on completion.

## Window-level evidence (@-offsets are repaired-stream pair indices)

**Window @1698–1707 (row a8_06, local 11):**
`91 85 33 94 30 20 62 94 88 26` — i.e. "…[33] **ne**(94) **pas**(30) [20] [62] **ne**(94) [88] [26-noun]".

**62→94 bigram census (byte-exact):** exactly 9 windows: @100, @508, @761,
@840, @1329, @1362, @1686, @1704, @1772. @1704–1705 is one of them.

**62='il' at @1704 (demonstrated, not assumed):** `battery-collision-62-84.md`
(verdict KILL, 2026-10-08, in `report_inbox/processed/`) re-read all nine
62→94 windows under the 'il' rival, including @1704 verbatim:
`"20 62 94 88 26" = "[20] il ne [88]…" Clean.` The 'on'/'il' crossover test
(62→59 x0, 84→94 x0) resolved 84='on' unconditioned and re-read the loser's
frames as 'il ne' at all nine windows. 62 at @1704 is a subject pronoun —
non-verbal at kill grade.

**Value-independent grammatical kill:** even without 62's value, the adverb
rescue needs 62 to be an infinitive ("ne pas [20-adv] [62-inf]"). 62 is
immediately followed by 94='ne' (R17-001 STRONG LEAD) + 88 (verb-class at
battery grade: ce88-leftedge-402 PROMOTE, finiteness-88-86). An infinitive
cannot be immediately followed by the particle 'ne' — no French construction
has "[inf] ne [verb]" as one constituent. The only licensed parse of
"62 94 88" is "il ne [88-verb]" (dropped-ne is not at issue: the 'ne' is
present).

**Word-internal rescue for 62: dead.** The word-final-'ne' segmentation was
scoped by `seg-62-94-wordless6` (PROMOTE, 2026-10-09) to the 6 D3-un-attachable
windows (@101/@509/@762/@841/@1363/@1687, 94-positions). @1705 is not among
them — the attachable "il ne" read stands.

**C2 (verbal-62 demonstration):** no evidence anywhere in the stream for 62
verbal at @1704. The 62 vient-family was killed (`compound-62-vient`, KILL,
2026-10-09); 62='bien' was killed (`adv-62-bien-1482`, KILL). C2 does not fire.

## Per-clause pass/fail

1. **PASS.** 62 is non-verbal at @1703/@1704 (62='il', demonstrated at this
   window; value-independent grammatical argument corroborates). The adverb
   rescue "ne pas [20-adv] [62-inf]" is KILLED at kill grade.
2. **N/A (does not fire).** No verbal-62 demonstration; the verbal-20 question
   stays closed per `inf-20-nepas`.

## Adverses

None listed.

## Verdict: PROMOTE

The (c2) loophole from `inf-20-nepas` is closed: at @1703, "ne pas [20]"
cannot be re-read as "ne pas [20-adverb]" because its would-be governor
([62-inf]) cannot exist — 62 is 'il' here. The verbal-slot forcing at @1703
("ne pas [20-inf]" + clause boundary) is now unconditional at battery grade.

## Caveats

- a8_06 carries an unvalidated upstream row offset; verdict holds on the
  canonical stream per protocol.
- 88's verb class is battery-grade (not red-team ratified); the kill does not
  depend on it (the 'il' demonstration + value-independent grammatical
  argument suffice).
- No standing or red-team verdict contradicted or downgraded; §7 intact.

## Bookkeeping

- Lock `code/crowd17/next-token/locks/nepas-20-adverb-gate.lock` created on
  start, deleted on completion.
- `battery-queue.json`: `nepas-20-adverb-gate` queued -> verdict/promote
  (temp-file + rename; pre-write assert confirmed no prior verdict; JSON
  re-validated; only this entry touched).
- R5005, sealed gate instances, red-team adjudication queue untouched.
- Promote, not null: no follow-ups required.
