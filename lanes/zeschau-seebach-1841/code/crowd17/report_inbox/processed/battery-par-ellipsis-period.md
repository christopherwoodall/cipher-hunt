# Battery verdict: par-ellipsis-period — period corpus test for complement-less "par" before "pour"

Date: 2026-10-09. Worker: battery worker (subagent 54969137-7d6b-4a55-a80c-c60aa58b3b1d).

## Bar (verbatim from battery-queue.json)

"Kill the ellipsis rescue iff no 17th–19th c. parallel exists; if a parallel exists, re-open the collocation under the ellipsis reading."

## Bar restated as numbered clauses (pre-registered before testing)

- C1: a genuine 17th–19th c. period parallel exists: complement-less "par" immediately before "pour" (the shape the ellipsis rescue needs to license "par pour" + verbal element).
- C2 (iff-branch): if no parallel exists in 33.2M chars of period + control French → KILL the ellipsis rescue.
- C3 (if-branch): if ≥1 genuine parallel exists → re-open the collocation under the ellipsis reading.

Terms: "ellipses rescue" = the rescue proposed in `seg-par-pour-96-00` (2026-10-09): complement-less "par" before "pour" explained by ellipsis of par's complement. "Parallel" = an attested French sentence where "par" appears with no overt complement directly before "pour".

## Loci (byte-confirmed on the repaired stream)

Re-derived `data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json` per `code/side-keyhunt/repair_parse.py`: 1,847 pairs, 96 types. `canonical.py` never used.

- "96 00" exactly 3× stream-wide: @47 (a1_01), @465 (a2_10), @960 (a6_00).
- Shape (adopting the sibling battery's byte-exact windows): "pas [62] **par pour** [92]", "[42] **par pour** [33=INF]", "[20] et **par pour** [86=INF]" — complement-less "par" + "pour" + verbal element in all three.

## Census method

Exact-bigram sweep `\bpar\s+pour\b` plus punctuation variants (`par[,\;:\-—–()]pour`) over the lane's period corpus (`code/side-period/corpus/`: 63 files, 31,664,431 chars, 17th–19th c. diplomatic memoirs, 1841 press, drama, prose). Generosity pass: "par" then "pour" within 3 words (222 hits, hand-classified). Control: modern French corpus (`code/crowd17/next-token/corpus-modern/`, 1,532,019 chars, 1902–1913 fiction).

## Per-clause pass/fail

- **C1 — FAIL (no parallel exists).**
  - Exact bigram "par pour": **0/31,664,431 chars** period corpus; 0 punctuation variants; 0/1,532,019 modern control.
  - The 222 "par … pour" hits: all 169 distinct between-tokens are overt complements — nouns ("par pitié pour", "par Napoléon pour", "par amour pour"), pronouns ("par elle", "par lui", "par nous"), or the frozen adverbial "par conséquent" (lexicalized complement). Zero instances of complement-less "par" directly before "pour". Ordinary grammatical French; none parallel the cipher's shape.
  - The cipher needs "par" with NO complement; every period attestation has one. The rescue has no historical license.
- **C2 — FIRES (kill branch).** The iff condition is met: no 17th–19th c. parallel in 31.7M chars (33.2M with control).
- **C3 — does not fire.** No genuine parallel, so no re-opening.

## Verdict: KILL

The ellipsis rescue is dead at battery grade: "par" never appears complement-less before "pour" in 33.2M chars of 17th–20th c. French. This kills rescue #1 of the `seg-par-pour-96-00` five-rescue set; the collocation stays fenced as a systematic residual and is NOT re-opened.

## Scope (what is NOT killed)

- The sibling's fence (`seg-par-pour-96-00` NULL) stands — no downgrade, no re-opening.
- 96="par" (granted) and 00="pour" (A9 class-level) values untouched; §7 intact.
- No standing or red-team verdict contradicted or downgraded. R5005, sealed gates, red-team queue untouched.
- Canonical-stream caveat stands (68/70 row offsets unvalidated).

## Caveats

- The corpus is print-register French (memoirs, press, drama, prose), 17th–19th c. predominance; manuscript/epistolary idiom is underrepresented.
- Zero-frequency inference: with 33.2M chars and zero hits, a licensed construction at this rarity would be an extraordinary claim; the battery treats zero as kill-grade at the lane's standard.
- Kills regenerate no follow-ups (§4).

## Bookkeeping

- Queue: `par-ellipsis-period` → status `verdict`, result `kill`, date 2026-10-09 (pre-write assert passed — was `queued`/verdictless; temp-file + rename; JSON re-validated; own entry only; no downgrade).
- Lock `locks/par-ellipsis-period.lock` created on start, deleted on completion (verified gone).
