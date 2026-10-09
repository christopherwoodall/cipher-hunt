# Battery report: stem-08-letter-probe

**Target:** `stem-08-letter-probe` — "test whether 08 is word-internal at 1b @60 ('41 08 34 29 40', the sole GT-letter contact of 08)".
**Worker:** battery worker stem-08-letter-probe (session 51500542-4828-4f74-86e8-17a3625909b5).
**Date:** 2026-10-09. **Verdict: PROMOTE** (word-internal).

## Bar (verbatim, from battery-queue.json)

"promote word-internal iff 08's letter contacts are all segmentally licensed; kill iff 08 must be a standalone word. A landed word-internal 08 kills '08 91 39' as a three-word NP and re-frames the qui-41 antecedent."

## Bar restated as numbered clauses (fixed before testing)

- **C1 (promote):** every one of 08's letter contacts — adjacencies with single-letter GT values — is segmentally licensed as a French word-internal junction → promote word-internal.
- **C2 (kill):** some window forces 08 to be a standalone word → kill.
- **Frame consequence (not a test clause):** a landed word-internal 08 kills the '08 91 39' three-word-NP parse and re-frames the qui-41 antecedent.

## Method

Read `BATTERY-PROTOCOL.md` first. Created `code/crowd17/next-token/locks/stem-08-letter-probe.lock` on start (agent id + UTC timestamp inside); no stale lock pre-existed. Stream re-derived in-session from `code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed exactly per `code/side-keyhunt/repair_parse.py`: **1,847 pairs / 96 types asserted**. `canonical.py` never used. R5005, sealed gate instances, and the red-team adjudication queue untouched. §7 standing constraints adopted, none re-litigated. Offset convention below: 0-based stream @; lane 1b @ = 0b @ + 1.

## Window-level evidence (@-offsets, repaired stream)

**Letter-value set (single letters only):** pencil GT 82='m', 34='i', 40='e' (§7 banked). No promoted or provisional value is a single letter, so no other contact counts.

**08 census confirmed: n=18.** Adjacent letter contacts — **three**, not one as the target's evidence claims. The parent census listed 40×2 as predecessors of 08 but did not class them as letter contacts; re-derivation shows they are:

1. **0b @60 (lane 1b @61; the target's "1b @60" is 0-based labeling of this same locus), row a1_01:** `41 08 34 29 40`. Junction 08→34('i'). GT tail 34-29-40 = "i er e" = the crib "premiere" tail (82-34-29-40 = "m i er e" on rows a5_03/a6_03). 08 occupies the m-slot.
2. **0b @922 (lane 1b @923), row a5_09:** `74 40 08 65 71`. Junction 40('e')→08.
3. **0b @944 (lane 1b @945), row a5_10:** `50 40 08 62 98`. Junction 40('e')→08.

No 82='m' contact anywhere. All other 15 windows' neighbors carry no single-letter value (nearest promoted neighbor: 17='fois' at @881, 47='ce' at @1592 — multi-letter words, not letter contacts).

**Segmental licensing (French word-internal junctions), per contact:**
- @60, 08→'i': **licensed.** The crib itself licenses a single letter immediately before 34='i' word-internally (82='m' in "premiere"); French C+i junctions are ubiquitous. The seg-08-ier-61 candidate letters {h, f, b, p} all sit licitly in this slot ("hier", "fière"/"bière"/"pierre"-tail) — noted, not adjudicated here.
- @922, 'e'→08: **licensed.** French word-internal e+C junctions are ubiquitous; no value assumption on 08 is needed.
- @944, 'e'→08: **licensed.** Same.

**Kill-grade scan:** no window forces a standalone-word reading of 08. The sole standalone-word rescue (08='on') is kill-grade dead under the standing on-08-homophony KILL (adopted, not re-litigated). "08 31" ×3 (before finite verbs per stem-08) admits clitic and letter arms alike — it does not force standalone.

## Per-clause results

- **C1 — PASS.** All three letter contacts are segmentally licensed as word-internal junctions. → **promote word-internal.**
- **C2 — does not fire.** No window forces 08 to be a standalone word.
- **Frame consequence — lands.** Per §7, 67 et/veut is the sole true polyvalence, so a word-internal 08 cannot also stand as a word: the '08 91 39' three-word-NP parse at 0b @35-37 is killed (trigram confirmed hapax, stream-wide count 1), and the qui-41 antecedent is re-framed — its NP needs a new head candidate. The parent target antec-08-91-39 is already NULL; this promote does not downgrade it, it re-frames its next attempt.

## Adverses answered

- **"coordinate with gated seg-08-ier-61 re-segmentation":** answered, not duplicated. This probe does not attempt the @60-67 re-segmentation. The promote supplies that target's shared premise (08 is a spelling letter at @60) and leaves its two arms ('08 34 29'='hier' vs '08 34 29 40' one word with 08∈{f,b,p}) for seg-08-ier-61 (queued, P2) to discriminate. No contradiction with its stated arms or adverses.
- **"do not re-litigate the on-08-homophony kill":** honored. The kill stands untouched; C2 was tested on independent window grounds.

## Verdict: PROMOTE (word-internal)

No standing or red-team verdict contradicted; §7 intact; stem-08 NULL not downgraded (its live 'spelling-letter' arm is the one that lands). Canonical-stream caveat: rows a1_01, a5_09, a5_10 offsets are unvalidated (68 of 70 per §7); the three contact windows inherit that caveat.

## Follow-ups

None required (promote verdict). Downstream note for the supervisor: seg-08-ier-61 (P2, queued) is now unblocked on its shared premise; the qui-41 antecedent re-frame belongs to the antecedent docket, not to this probe.

## Bookkeeping

- Report: this file (`code/crowd17/report_inbox/battery-stem-08-letter-probe.md`).
- Lock: `code/crowd17/next-token/locks/stem-08-letter-probe.lock` created on start, deleted on completion. No stale lock pre-existed.
- Queue entry `stem-08-letter-probe` updated via temp-file + rename (pre-write assert: status `queued`, verdict null — passed; post-write JSON re-validated; own entry only).
