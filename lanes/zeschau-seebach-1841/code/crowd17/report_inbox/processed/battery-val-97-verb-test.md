# Battery report: val-97-verb-test

- Target id: `val-97-verb-test`
- Claim: "Name 97's class from its 10 windows; a forced verb-97 re-opens Route A ('qui [02] [97-fin]') for 02's qui-leg."
- Date: 2026-10-09
- Worker: battery worker (subagent 9add5bdc-23aa-40ec-b67d-cb78d802c507)
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed like `repair_parse.py`); asserts held (1847 pairs, 96 types). `canonical.py` never used. R5005, sealed gates, red-team queue untouched.

## Bar (verbatim, pre-registered before testing)

"name 97's class from its 10 windows ('97 46' que-complement, '97 47' ce-object verb legs vs '00 97' x4 infinitive frames and '80 97 13' @567); a forced verb-97 re-opens Route A with 02 as the intervenor to test."

Numbered pass/fail clauses (restated before testing, not modified after):

1. Name 97's class (finite verb / infinitive / nominal) from its 10 windows under standing values.
2. If 97 is FORCED finite verb, re-open Route A ('qui [02] [97-fin]' at 0b@749-751) with 02 as the intervenor to test.
3. All listed adverses answered (not ignored).

## Method

1. Read BATTERY-PROTOCOL.md first. Created `code/crowd17/next-token/locks/val-97-verb-test.lock` on start (agent id + 2026-10-09T10:22:29Z); no stale lock present (siblings' locks only).
2. Re-derived the 10-window census of 97 on the repaired stream (1-based @): @3 (a1_00), @95 (a1_02), @289 (a2_03), @300 (a2_04), @526 (a3_00), @567 (a3_02), @589 (a3_02), @752 (a5_03), @1413 (a7_07), @1824 (a8_11). Census matches the queue evidence exactly.
3. Tested each window for three classes under §7 standing values (banked GT: 11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que; granted: 87=ce, 64=qui, 96=par, 17=fois, 00=pour A9, 84=on A15, 47=ce A4; provisional: 59=est, 77=le; 86 INF-class A9; 67 sole polyvalence).

## Window-level evidence (all byte-exact on the repaired stream)

Legend: FIN = finite verb, INF = infinitive, NOM = nominal.

- **@3 (a1_00):** `09 00 [97] 51 47 41 06 77` (stream-initial). "pour [97]". FIN killed (pour+finite ungrammatical; §7 bars the polyvalence rescue). INF clean ("pour dire"-shaped). NOM grammatical (bare "pour [N]", "pour mémoire"-shaped) but distributionally disfavored: 00's nominal takes surface the article 4/4 in-stream ("00 11" @76/@378/@1287/@1405, verified), while "00 97" x4 never does — patterning with 00->86 x12 and 00->33 x8 (infinitive slots).
- **@95 (a1_02):** `98 81 [97] 46 29 85 08 21`. "81 [97] que er [85]…". FIN: needs 81 as subject (81's class open — 81='prin' killed, noun-81 only a queued hypothesis) AND a finite verb in the que-clause, but the tail is "que [29] [85]…" with "29 85" unlicensed as a verb under standing values ("29 85" x3 stream-wide: @96/@374/@1233; the "er-word-lexicon" target that would license word-initial "er" is still queued). INF: "dire que"-shaped que-valency (precedent: 33-46 x2, A10) — conditional on the same tail. NOM: "[81] [97-noun] que [relative]" — conditional on the same tail. All three conditional; none forced.
- **@289 (a2_03):** `00 [97] 09 64 29 40 65`. "pour [97] [09] qui [29 40 65]". FIN killed (pour+finite). INF clean ("pour [inf]"). NOM clean ("pour [N]"). The tail "[09] qui [29 40 65]" is IDENTICAL under both readings — so the earlier battery claim (les567-imperative evidence) that infinitive-97 "strands 09 and leaves qui antecedentless" at kill grade is unsound: whatever grammaticality the tail has is class-independent, and 09's qui-antecedent role is itself unproven (rel-09-290 verdict: null). @289 does NOT force nominal; it licenses INF and NOM equally. Evidence-level correction, not a verdict change.
- **@300 (a2_04):** `11 78 40 [97] 86 91 18`. "[78]e [97] [86-inf]". FIN: no frame → excluded. INF possible (INF+INF asyndeton, strained). NOM possible. Unforced.
- **@526 (a3_00):** `81 [97] 47 44 59 37 64`. "[81] [97] ce(47) [44] est(59) [37]" — "ce [44] est [37]" is a clean A1 copula clause. FIN: "[81-subj] [97-Vfin]" leaves a second clause with no conjunction → unmotivated. INF: dislocated infinitive topic ("Partir, c'est…"-shaped) — possible only if 81 is adverbial (81's class open) → strained. NOM: "[81] [97-noun]" appositive NP + copula → clean. NOM favored.
- **@567 (a3_02):** `80 [97] 13 76 45 94 52`. Imperative "[97-imp] les!" already killed (les567-imperative; 13=les killed). FIN: "[80] [97-fin]" two adjacent finite verbs → excluded. INF: needs modal/causative 80 (unlicensed; 80's value open) → strained. NOM: "[80-V] [97-N]" object → clean. NOM favored.
- **@589 (a3_02):** `00 [97] 41 41 09 00 92`. "pour [97]". FIN killed. INF clean. NOM grammatical/distributionally disfavored (same as @3).
- **@752 (a5_03):** `00 64 02 [97] 40 67 11`. "pour qui [02] [97] e [67] la". The sole verb-shaped leg ("fait [97-inf]" causative) is conditional on 02='fait', which is a fenced NULL (adv-02-858: 3 hard contradictions elsewhere), not a standing value. Unforced under standing values.
- **@1413 (a7_07):** `16 [97] 69 74 34`. 16 is infinitive-class (standing promote). "[16-inf] [97] ce(69) [74]". FIN: no frame → excluded. INF: INF+INF asyndeton → strained. NOM: INF + object NP → clean. NOM favored.
- **@1824 (a8_11):** `00 [97] 00 86 29 82`. "pour [97] pour [86-inf-er]". FIN killed. INF: parallel "pour X pour Y" with 86 in explicit infinitive form ("86 29") → strong positive leg. NOM: mixed parallelism ("pour [N] pour [INF]") → grammatical but disfavored.

## Class tally

- **FIN: KILLED at kill grade.** "pour"+finite is ungrammatical at @3/@289/@589/@1824; §7 (67 sole polyvalence) bars a window-split rescue; zero positive finite legs in the 10-window census (the @752 leg is conditional on fenced 02='fait'; the @95 leg is conditional on 81-as-subject + an unlicensed tail).
- **INF: 6 positive legs** — "pour [97]" x4 with the bare-no-article discriminator (@3/@289/@589/@1824), the @1824 parallel with explicit infinitive-form 86, the @95 "dire que"-shaped que-valency (conditional tail). Strained-but-possible at @526/@567/@1413 (conditional on 81-adverbial / modal-80 / asyndeton). Zero contradictions.
- **NOM: 3 clean favoring windows** — @526 (appositive NP + copula), @567 (V + object), @1413 (INF + object); consistent at all other windows; the @289 "force" claim corrected to conditional (see above).

## Per-clause pass/fail

1. Name 97's class: **FAIL (null).** Genuine INF/NOM tie at battery grade: INF has more positive legs (6), NOM has the cleaner favoring windows (@526/@567/@1413) plus universal consistency, and neither is forced or killed. The class cannot be named at battery grade.
2. Forced verb-97 → re-open Route A: **does not fire.** FIN-97 is kill-grade dead (clause-1 kill), so Route A ('qui [02] [97-fin]' at 0b@749-751) cannot re-open through 97. Route A stays closed on the 97 axis. (The '64 02' @608 window "qui [39] qui [02] [58] ce" has no 97 at all — Route A lives or dies at @749-751 only.)
3. Adverses answered: 97's class OPEN — confirmed and preserved (no naming attempted). '80 97 13' @567 awkward for finite 97 — confirmed; the window favors NOM, consistent with the FIN kill. Route A parse compatible-not-forced — superseded: it is now incompatible with the four pour-windows under §7.

## Verdict: NULL

The class-naming condition is unmet (INF/NOM tie), and the Route-A re-open condition fails definitively (FIN-97 killed). No standing red-team verdict contradicted (no A-series ruling names 97; §7 untouched). The queued battery verdicts frame-97-profile (promote, infinitive-class) and les567-imperative (kill, imperative) are not downgraded or altered; the @289 evidence correction is evidence-level only.

## Follow-ups proposed (nulls regenerate work; all verified absent from battery-queue.json)

1. `inf-97-567-adjudicate` (P3) — test @567 "80 97" under modal-80 vs object-noun readings; the sharpest INF/NOM discriminator (NOM clean, INF needs modal-80).
2. `nom-97-526-adverb` (P3) — test 81's class at @526; adverbial-81 revives the "Partir, c'est…" infinitive-topic reading, nominal-81 hardens NOM-97.
3. `route-a-02-killpack` (P4) — kill-grade pack closing Route A on the 02 axis (02's verb/'fait' profile), now that the 97 axis is closed.

## Bookkeeping

- Queue: `val-97-verb-test` → `verdict`/`null`, 2026-10-09 (pre-write assert: was `queued`/verdictless; temp-file + rename; JSON re-validated; own entry only; no downgrade).
- Lock `locks/val-97-verb-test.lock` created on start, deleted on completion.
- No standing/red-team verdict contradicted or downgraded; §7 intact; R5005, sealed gates, red-team queue untouched.
