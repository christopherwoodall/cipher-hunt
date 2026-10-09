# Battery verdict: noun-97-568

- Target id: `noun-97-568`
- Claim: "Name 97's class; a verbal or determiner 97 reframes @568's left edge and re-opens the @567/568 wall."
- Date: 2026-10-09
- Worker: battery worker (subagent 8933633c-5788-47c3-9a3d-b83e10667af5)
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed like `code/side-keyhunt/repair_parse.py`). Verified in-session: 1,847 pairs, 96 types. `canonical.py` never used. R5005, sealed gates, red-team queue untouched.
- Offset note: the bar's "@568" = 1-based stream index 568 = 0-based @567 = 13 (row a3_02), per battery-value-13-third-arm's convention. "@568's left edge" = the 97|13 boundary (0b@566|@567). The "wall" = "97 13 76" (0b@566–568) with 76 noun-class.

Terms (ASD-STE100): "wall" = the "97 13 76" sequence that killed 9+ uniform-13 candidates in battery-value-13-third-arm (2026-10-09). "Reframe" = re-parse of the 97|13 boundary under a named 97 class. "Re-open" = the wall no longer kills the uniform-13 candidates it killed. "Kill grade" = a window forces the claim false under standing values.

## Bar (verbatim, pre-registered before testing)

"Named 97 class that reframes @568's left edge (verbal or determiner 97) re-opens the @567/568 wall; else the wall stands."

Numbered pass/fail clauses (restated before testing, not modified after):

1. **C1:** 97's class is named at battery grade, and the named class is verbal or determiner.
2. **C2:** the named class reframes @568's left edge (the 97|13 boundary) AND re-opens the wall — i.e. at least one wall-killed uniform-13 candidate parses under the reframe, breaking the wall's decisive-discriminator status.
3. **Verdict rule:** promote iff C1 and C2 both pass; the wall stands otherwise.

## Method

1. Read BATTERY-PROTOCOL.md first. Created `code/crowd17/next-token/locks/noun-97-568.lock` on start (agent id + 2026-10-09T11:57:00Z); no stale lock was present.
2. Re-derived the repaired stream in-session. All @-offsets below are 0-based unless marked 1b.
3. Adopted, never re-litigated: 00='pour' (A9), 46='que' (banked pencil GT), 47='ce' (A4), 40='e' (pencil GT), 80 verb-frame (A8), 86 INF-class (A9), 76 noun-class (registry: ['noun','lead']), 97 infinitive-class (battery PROMOTE frame-97-profile, 2026-10-08), 97 finite-verb KILL (battery val-97-verb-test, 2026-10-09: four "pour [97]" windows), §7 (67 et/veut sole polyvalence — no window-split rescue at battery grade).
4. 97 census re-derived byte-exact: n(97)=10 at 0b [2, 94, 288, 299, 525, 566, 588, 751, 1412, 1823]; successors all distinct x1 each: [51, 46, 09, 86, 47, 13, 41, 40, 69, 00].

## C1 — name 97's class (verbal or determiner)

**Determiner arm: FAIL at kill grade — three independent kill legs.**

A French determiner must be followed by a nominal (noun or adjective+noun). Three of 97's windows put a non-nominal in the successor slot under standing values:

- **K1 @94 (0b, row a1_02):** `41 98 81 [97] 46 29 85 08` — successor 46='que' (banked GT). Determiner + "que" is ungrammatical every period.
- **K2 @525 (0b, row a3_00):** `06 55 81 [97] 47 44 59 37` — successor 47='ce' (granted A4). Determiner + "ce" is ungrammatical every period.
- **K3 @1823 (0b, row a8_11):** `09 19 00 [97] 00 86 29 82` — successor 00='pour' (granted A9). Determiner + "pour" is ungrammatical every period.

Each leg uses only standing values; no new assumptions. A uniform determiner-97 is dead at three independent windows.

**Finite-verb arm: dead (adopted).** val-97-verb-test killed FIN-97 at kill grade ("pour"+finite ungrammatical at four windows; §7 bars a split rescue). Adopted, not re-litigated.

**Infinitive arm: live (adopted).** frame-97-profile PROMOTEd 97 as infinitive-class (seven frame-legs: "pour 97" x4 with the bare-no-article discriminator, the @1823 "pour 97 pour 86er" parallel, que-valency @94, "80 97" modal/causative @566). Adopted as the sole live verbal class for the C2 reframe test. (Note: val-97-verb-test returned an INF/NOM tie on the class question; the infinitive promote is used here as a premise for the reframe, not as a fresh uniqueness claim — no standing verdict is altered.)

**C1 verdict:** the class is determined for the bar's purposes — determiner kill-grade dead; finite verb kill-grade dead (standing); infinitive the sole live verbal class (adopted promote). C1 satisfied via the infinitive arm.

## C2 — reframe test: does infinitive-97 re-open the wall?

The reframe: 0b@565–569 = "80 [97-INF] 13 76" — the 97|13 boundary re-parses from "[97-open] | [13-head]" to "[97-INF] | [13-complement]". The wall's killer arguments are re-tested with 13 as the infinitive's complement: "[97-INF] [13-X] [76-N]" (76 = masculine noun, registry lead).

Every candidate the wall killed (all that survived the verb-follower set in battery-value-13-third-arm) is re-tested under the reframe:

| candidate X | "[97-inf] [X] [76-N]" test | result |
|---|---|---|
| 'en' (adv. pronoun) | "en" cannot precede a noun it does not replace | DEAD |
| 'y' | adverbial pronoun cannot precede a noun | DEAD |
| 'se' | reflexive clitic needs a verb to its right | DEAD |
| 'on' | subject pronoun cannot follow an infinitive | DEAD |
| 'ne' | negation needs a verb | DEAD |
| 'me/te/nous/vous' (obj. pron.) | object pronoun cannot precede a noun | DEAD |
| 'qui/que/dont' (relative) | relative pronoun needs a clause | DEAD |
| noun | "[inf] [13-N] [76-N]": infinitive's object = 13, 76 strands; bare noun–noun adjacency ungrammatical (compound rescue would contradict 76's group-level noun status) | DEAD |
| 'il/ils' (subj. pron.) | subject pronoun cannot follow an infinitive | DEAD |
| adverb | adverb cannot split verb + direct object | DEAD |

**Result: 0/10 revive.** The wall's decisive-discriminator status survives the infinitive reframe intact. The left edge re-parses, but no wall-killed candidate becomes grammatical — the wall does not re-open.

**Robustness check (nominal-97, the tie's other arm):** under "[97-N] [X] [76-N]", every candidate above is still ungrammatical (noun-13 gives three bare nouns; all others fail identically). The wall stands under every live 97 class — it is class-independent.

**Fenced, not tested:** "97-13" as one word (sub-lexical 13 under an infinitive-97 stem) would need 13 as a letter/syllable — that is the sub-lexical-13 route, explicitly fenced as red-team territory in battery-value-13-third-arm. Not available at battery grade.

**C2 verdict:** FAIL. The named verbal class reframes the edge but does not re-open the wall.

## Per-clause verdict

1. C1 (class named, verbal or determiner): PASS via the infinitive arm (determiner kill-grade dead at @94/@525/@1823; finite verb kill-grade dead, standing).
2. C2 (reframe re-opens the wall): FAIL — 0/10 wall-killed candidates revive under "[97-INF] [X] [76-N]"; wall is class-independent (robust under nominal-97 too).

## Verdict: KILL

The re-open claim is falsified at battery grade: no namable 97 class (verbal or determiner) re-opens the @567/568 wall. The wall stands — independent of 97's class naming.

## Scope of the kill (narrow)

Killed: the claim that naming 97's class (verbal or determiner) reframes @568's left edge and re-opens the wall. NOT killed and untouched:
1. 97's infinitive-class promote (frame-97-profile) — used as a premise, never challenged.
2. The INF/NOM tie (val-97-verb-test) — preserved; the C2 test does not depend on resolving it.
3. The residual 13 space: sub-lexical 13 (`letter-13-verdicts`, queued P3) and the §7 split (`split-13-redteam`, queued P2) — both red-team venue, untouched.
4. No standing or red-team verdict contradicted or downgraded; §7 intact.

Per §4, kills regenerate no follow-ups. The two queued targets above already cover the residual space; no new follow-ups are proposed.

## Bookkeeping

- Queue: `noun-97-568` → status `verdict`, result `kill`, 2026-10-09 (pre-write assert passed — was `queued`/verdictless; temp-file + rename; JSON re-validated post-write; own entry only; no downgrade).
- Lock `locks/noun-97-568.lock` created on start, deleted on completion (verified gone).
- `canonical.py` never used; R5005, sealed gates, red-team queue untouched.
