# Battery report: val-02-clitic

- Target id: `val-02-clitic`
- Date: 2026-10-09
- Worker: battery worker (subagent 339ea023-cf8d-4c56-acdd-b8eac00f82d7)
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py`; re-derived in-session, asserts held: 1847 pairs, 96 types). `canonical.py` never touched. R5005, sealed gates, red-team adjudication queue untouched.

## Bar (verbatim from battery-queue.json)

"test 02 as negation/clitic/adverb in the 'qui [02] [97]' slot; a forced non-verb 02 at @750 drops the qui-leg."

## Bar restated as numbered pass/fail clauses (pre-registered before testing, not modified after)

- C1: The @750 window parses as stated: 0b@746-753 on row a5_03 = `85 28 | 00 64 02 97 40 67 | 11 70 82 34 29 40`, i.e. `[85] [28] pour qui [02] [97] e et la pre m i er e`, with 67's follower 11=`la` (not infinitive-shaped) fixing 67=`et` by the positional rule; a5_03 at offset 0 and gloss-anchored, phase-solid against offset-1 rescues.
- C2: 02 in the `qui [02] [97]` slot at @750 is FORCED to a non-verb class (negation, clitic, or adverb) — every verb-class reading of 02 at @750 is excluded by stream evidence at battery grade.
- C3: A forced non-verb 02 at @750 drops the qui-leg (the leg on which 02 is the relative-clause verb after `qui`), leaving zero surviving qui-legs for 02.

## Method

1. Read BATTERY-PROTOCOL.md in full first. Created `code/crowd17/next-token/locks/val-02-clitic.lock` on start (agent id + 2026-10-09T10:45:26Z); no fresh lock for this target existed (siblings' locks only).
2. Re-derived the repaired stream in-session (byte-exact per repair_parse.py). All @-offsets below are 0-based repaired-stream indices (queue convention).
3. Tested each disjunct of the claim (negation / clitic / adverb) against the stream under standing §7 values (banked: 11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que; granted: 87=ce, 64=qui, 96=par, 17=fois, 79=tout, 00=pour, 84=on, 47=ce; kills: 94=`ne` STRONG LEAD, {48,94} homophone-set, 81=`prin`; 67 sole polyvalence with positional rule).
4. Adopted (not re-litigated) two processed battery verdicts: `val-97-verb-test` (FIN-97 killed at kill grade, 2026-10-09) and `qui-02-750-parse` (NULL; four dissolve routes fenced, standing parse `pour qui [02-verb] [97]e`, 2026-10-09).

## Window-level evidence (all byte-exact on the repaired stream)

- Target window: 0b@748-753, row a5_03: `00 64 02 97 40 67`; left context 0b@746-747 `85 28`; right context 0b@754-759 `11 70 82 34 29 40` = `la pre m i er e` (gloss-i crib, anchor). Row a5_03 offset 0. 64 and 02 on the same row, no boundary marker at the contact.
- 67 at 0b@753, follower at 0b@754 = 11=`la` (banked) — not infinitive-shaped → 67=`et` by the positional rule. Frame right edge: `[97] e et la premiere`.
- `64 02` occurs exactly 2x stream-wide (0b@608 row a4_00: `64 39 64 02 58 47 77`; 0b@749 row a5_03) — the two qui-windows. `02 97` is a stream hapax (0b@750 only).
- 02: n=17 at 0b@[128, 305, 410, 459, 495, 609, 718, 750, 858, 887, 916, 1084, 1152, 1299, 1467, 1819] (0-based; 1-based list in queue evidence matches).
- 97: n=10; FIN-97 killed at kill grade by `val-97-verb-test` (`pour`+finite ungrammatical at 0b@2/@288/@588/@1824; §7 bars the window-split rescue — 67 is the sole polyvalence). Adopted: 97 in {INF, NOM}, never finite.
- `94 02` at 0b@494-495: `42 94 02 79 88 47` = `[42] ne [02] tout [88] ce` — 02 directly AFTER `ne`.
- `84 02` at 0b@857 (`32 48 84 02 24 49`) and 0b@1151 (`33 66 84 02 00 92`) — 02 directly after 84=`on` (A15), 2 of 17 occurrences.
- 94=`ne`: n=37, 24 distinct followers; 02 follows `ne` exactly once (0b@494).

## Per-clause pass/fail

- **C1: PASS.** Window verified byte-exact as stated; gloss-anchored row a5_03, offset 0; 67=`et` by the positional rule (follower 11=`la`). Phase-solid.
- **C2: FAIL at kill grade.** Each disjunct of the claim's disjunction is excluded at battery grade on the @750 window:
  - *Negation:* excluded. 94=`ne` is STRONG LEAD (n=37); the {48,94} homophone set is killed (§7); the 1690 uniformity necessary condition for homophony fails (02 n=17 vs 94 n=37); and `94 02` at 0b@494-495 puts 02 directly after `ne` — were 02=`ne`, the resulting `ne ne` is ungrammatical, i.e. positive evidence AGAINST homophony.
  - *Clitic:* excluded. A subject clitic in `qui [02] [97]` requires a finite 97 (`pour qui [subj] [verb]`, e.g. `pour qui je travaille`) — FIN-97 is killed (adopted, kill grade), so the subject-clitic leg is dead. An object/reflexive clitic requires a verbal host — 97 in {INF, NOM} cannot host one (`*qui le [inf]`, `*qui [cl] [noun]`). Corroboration: 02 follows 84=`on` twice (0b@857, @1151); `*on [subject-clitic]` is ungrammatical, so 02 is not a subject pronoun on its global profile either.
  - *Adverb:* excluded. An adverb needs a verbal (or adjectival) host: with 97=NOM the relative clause `qui [02-adv] [97-noun]` is verbless → ungrammatical; with 97=INF the adverb would have to split `pour qui` from its infinitive (`*pour qui [adv] [inf]`) → ungrammatical at the lane's standard (same standard as the `pour`+finite kill; 1841 manner adverbs post-pose to infinitives).
  - The disjunction is exhaustive per the claim's own terms (negation/clitic/adverb). All three disjuncts excluded → the claim is false at @750. (Non-verb classes outside the claim's terms, e.g. preposition/conjunction, fare no better: `qui [prep/conj] [97]` is verbless or has nothing to join — dead on arrival; and 02-class-609 already fenced conjunction at the other windows.)
- **C3: antecedent false — inverted.** The qui-leg is not dropped; it is the SOLE surviving parse. With FIN-97 dead and every non-verb-02 disjunct excluded, the only grammatical reading is 02 as the finite verb: `pour qui [02-verb] [97]e et la premiere`, with `[97]e` nominal (feminine, 40=`e` composing leftward — via stylistic inversion `pour qui [02] [97-subj]` or `pour`-detached `qui [02-verb] [97-obj]`). Re-verified zero forced contradiction, consistent with the standing parse of `qui-02-750-parse` (whose four dissolve routes remain fenced).

## Adverses (from battery-queue.json) — answered, not ignored

- A1 ("negation `ne` blocked: 94=`ne` STRONG LEAD, no homophony evidence for 02"): CONFIRMED and hardened — homophone-set kill (§7), uniformity failure (17 vs 37), and the `94 02` @494 `ne ne` counter-evidence. Answered.
- A2 ("clitic/adverb values for 02 have zero battery-grade evidence"): CONFIRMED and strengthened — not merely zero positive evidence, but positive exclusion: every clitic/adverb disjunct needs a verbal 97, and FIN-97 is killed. Answered.
- A3 ("`qui [02-?] [97-fin]e` compatible, not forced"): SUPERSEDED on the 97 axis — `val-97-verb-test` killed FIN-97, so the 97-fin leg is no longer "compatible"; it is dead. That death is exactly what excludes the clitic/adverb disjuncts above. Answered.

## Verdict

**KILL.** C2 fails at kill grade: the @750 window, under standing §7 values and the processed FIN-97 kill, forces the claim false — every disjunct (negation/clitic/adverb) is excluded at battery grade, and the cleaner rival (02 = finite verb, `[97]e` nominal) is demonstrated on the same frame. The bar's mechanism is inverted: it is the non-verb 02 that drops, not the qui-leg.

## Standing-state check

- Consistent with `battery-02-class-609` (NULL): 02's §7 split signature (verb-selecting at the two qui-windows vs verb-excluding at @305 `@88 02 88` and @858 `on [02] faire`) is untouched — this verdict is slot-specific to @750 and declares no global class. Red-team territory respected; no red-team verdict exists on 02 or @750; nothing contradicted or downgraded.
- Adopts `battery-val-97-verb-test` FIN-97 kill (no downgrade; its NULL overall verdict stands).
- No standing verdict contradicted. §7 intact. R5005, sealed gates, red-team queue untouched.

## Follow-ups

None required — kills do not regenerate work under §4. Bookkeeping note for the supervisor: `val-97-verb-test` proposed `route-a-02-killpack` (P4) to close Route A on the 02 axis now that the 97 axis is closed; this report fulfills its @750 component (Route A is dead on both axes at this slot — 97-fin killed, 02-nonverb excluded). Do not queue a duplicate target for the @750 slot. The surviving open question — 02's split profile (verb @609/@750 vs non-verb @305/@858) — is already packaged for the red team by `battery-02-class-609`; no new target proposed here.

## Bookkeeping

- Lock `code/crowd17/next-token/locks/val-02-clitic.lock` created on start (agent id + 2026-10-09T10:45:26Z), deleted on completion.
- `battery-queue.json`: `val-02-clitic` → status `verdict`, result `kill`, date 2026-10-09 (pre-write assert confirmed `queued`/verdictless; temp-file + rename; JSON re-validated; own entry only; no downgrade).
