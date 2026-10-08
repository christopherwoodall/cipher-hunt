# Round-16 battery: pour (00) — verification + tension adjudication

Finder report: `code/crowd16/report_inbox/next-token-findings-pour.md` (ingested 2026-10-07).
Status entering: 00="pour" BANKED (round-15 A9, red-team GRANT with leg-(1)
downgrade to class-level). This battery VERIFIES; it does not re-promote
(the finder's "promotion battery" target is already-banked ground).

Corpus leg (new, run in-battery): Nesselrode v8 (the full 1841 run, era/
register-correct): standalone "pour" = 671/86,724 words (0.774%);
"pour"-syllable tokens (pour/pourquoi/pourtant/…) = 796/~134,378 syllables
(**0.592% of syllables**, crude vowel-group estimate). Cipher 00 = 55/1,847
pairs = **2.978% — ~5× the register rate.** Recorded as a MODERATE adverse
(see verdict).

---

## PRE-REGISTRATION (locked before formal tests)

**Scope:** (a) re-derive the follower census; (b) the @107 tension MUST be
addressed explicitly — verified, with its fork-conditional logic stated, and
HANDED to the forks battery (it cannot promote 00 circularly, and it cannot
resolve the 67 fork alone); (c) weigh the @1247 and @864 adverses; (d) weigh
the rate adverse.

**Bar V1 — verification CONFIRM:** follower census re-derives exact
(86×12, 33×8, 66×7, 92×6, 97×4, 11×4, 46×4, 36×3 + singletons); ≥45/55
windows clean-or-neutral under "pour"; no NEW hard adverse beyond the named
fenced ones.

**Bar V2 — @107 tension:** ADDRESSED iff (i) the window P[106:111] is
verified exact; (ii) the logic is stated: under 00="pour", the window is
grammatical iff 67="et" ("pour que la [21] et…") and ungrammatical iff
67="veut" ("pour que la [21] veut" — "pour que" demands subjunctive);
(iii) it is recorded as a FORK-CONDITIONAL datum (votes 67="et" *given*
00="pour"), queued for the forks battery. It does not independently promote
00 (that would be circular: 00's own grant leaning on a window that assumes
00).

**Bar V3 — adverses:** a single-window adverse KILLS the banked value iff it
cannot be fenced as a residual AND no re-parse survives. Otherwise FENCED
with cause (precedent: A15's R1/R2 1/25 residuals). The rate adverse is
weighed, not verdict-bearing alone.

**Bar V4 — 86's value:** NOT named here (three live candidates, three
adverses for 86="le" — the finder's honest null stands; 86 goes to its own
battery).

---

## TESTS

`t = code/crowd16/next-token/test_pour.py`.

| # | assertion | got |
|---|-----------|-----|
| 1 | n00 = 55 | |
| 2 | follower census: 86×12, 33×8, 66×7, 92×6, 97×4, 11×4, 46×4, 36×3 | |
| 3 | singletons = {34,13,20,64,44,98} ×1 each | |
| 4 | @106 window P[106:111] = [0,46,11,21,67] | |
| 5 | @1244 window P[1244:1255] = [0,33,16,0,67,46,26,30,6,65,46] | |
| 6 | @1545 window P[1545:1550] = [0,46,70,12,94] | |
| 7 | @1680 window P[1680:1685] = [0,46,79,65,13] | |
| 8 | @545 window P[545:550] = [0,46,24,47,46] | |
| 9 | @864 window P[861:868] = [74,74,48,47,46,0,86] (ce47 handoff) | |
| 10 | "00 86 56" ×4 starts | |
| 11 | "00 86 29" ×2 starts | |
| 12 | @552 window P[552:557] = [0,86,59,34,17] | |
| 13 | @667 window P[667:672] = [0,20,67,11,86] (20-paradox feed) | |
| 14 | @1287 window P[1287:1292] = [0,11,17,84,59] | |

---

## VERDICT

**V1 verification — CONFIRM.** Follower census re-derived exact (one
correction: the singleton set is {13,20,34,44,64,**67**,98} — the finder
missed 67, which is the @1247 adverse itself). All "pour que" legs
re-derived: @1545 flagship [0,46,70,12,94] ("pour que pre[12]…"), @1680
[0,46,79,65,13] ("pour que tout [65]…"), @545 [0,46,24,47,46] (fenced
strained). The twice-identical infinitive phrases re-derived: 00-33-16 ×2
(@185/@1244), 00-33-21-64-37 ×2 (@935/@1629), 00-33-79-80-06 ×2 (@466/@1087).
~50/55 windows clean-or-neutral under "pour". **00="pour" banked status
CONFIRMED** — the grant stands on the "pour que" legs + preposition-like
profile, independent of the INF morphology (A9 downgrade respected).

**V2 @107 tension — ADDRESSED (not sidestepped).** P[106:111] = [0,46,11,21,67]
verified exact. The logic, stated plainly: UNDER 00="pour", "pour que la [21]
[67]" is grammatical iff 67="et" and ungrammatical iff 67="veut" ("pour que"
demands the subjunctive; "veut" is indicative). So the window votes 67="et"
*conditional on 00="pour"* — it pressures the FORK, not 00. Recorded as a
fork-conditional datum and HANDED to the forks battery; it is not used to
promote 00 (that would be circular). If an independent battery ever confirms
67="veut" at @106, 00="pour" takes the hit instead — the direction of the
conditional is now on record.

**V3 adverses — fenced, not killing.**

(a) **@1247 (strongest single adverse):** P[1244:1255] = [0,33,16,**0**,67,46,
26,30,6,65,46] verified. The second 00 gives "pour [33-16] pour [et/veut]
que" — ungrammatical under BOTH fork values and under 00="pour". FENCED as
a 1-window residual with cause: 54/55 other windows are clean-or-neutral,
and the finder's split hypotheses (00 polyvalent vs word-internal) are
QUEUED as the residue/split battery (target #4), not findings. Note the
lane-law cost: 00-polyvalence would be a second polyvalence (67 is sole) —
the split battery must clear that bar or find the word-internal parse.

(b) **@864 (ce47 handoff):** [74,74,48,47,46,0,86] = "à ce que pour [86-INF]…"
verified. Broken under 00="pour" — but conditional also on 48's unknown
value (48="à/de"-class assumed). FENCED as a residual; it is the cheapest
decisive test of 00 on the board (one clean re-parse kills or confirms it).

(c) **Rate adverse (new, run in-battery):** 00 = 2.978% of pairs vs
Nesselrode-v8 "pour"-syllables ≈ 0.592% of syllables — **~5× the register
rate** (Guizot t1–t3: 0.77–0.79% of words; Nesselrode v7/v9/v10: 0.70–0.76%).
MODERATE adverse, weighed honestly: either this dispatch is pour-heavy at 5×
the diplomatic rate, or 00 has a second use. It does not kill (the
distributional legs dominate), but it is the strongest statistical pressure
on the "pure pour" reading and it JOINS @1247 in the split battery's docket.

**V4 86 — value NOT named** (finder's honest null stands). The three
adverses (@552 [0,86,59,34,17] "pour le est"; @866; @888) indict 86="le"
specifically, not 00 — "00 86 56" ×4 (@961/@1001/@1505/@1791) and "00 86 29"
×2 (@1374/@1824) are formula-grade "pour"-support regardless of 86's value.
86 battery queued with the constraint set.

**Feeds out:** @667 "pour [20]…" → 20-paradox battery (feminine-noun leg);
@76/@1374/@1824 "le/la + er[29]" ×3 → "l'er"-noun battery; @1545's 12 →
cross-confirms formula-tails T3 ("entrepre[12]"); @1680 predicts 65
subjunctive-shaped ("soit"-class testable).

Weakest leg for self-critique: the rate adverse + @1247 are the two most
hostile data points to "pure pour" — if the split battery finds 00's ~5
adverse windows share a contact profile distinct from the clean ~50, the
banked value needs conditioning, and the A9 grant's "preposition-like
profile" leg would have to be re-weighted.
