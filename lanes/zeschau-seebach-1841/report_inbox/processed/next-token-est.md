# Round-16 battery: est — the adjective battleground

Finder report: `code/crowd16/report_inbox/next-token-findings-est.md` (ingested 2026-10-07).
Status entering: 37/32/42 predicative frames GRANTED (round-15 A1, red-team
confirmed); 19 HOLD at 1 leg.

Standing law applied: ISLET-10 (round 10, kill-grade): 59="est" iff
pre∈{64,94,93}; unconditioned 59="est" REFUTED. Authority file:
`code/crowd10/conditioner59/classification.json` (59-cell positions as keys).
The round-15 A1 battery never checked its legs against this classification —
this battery does. This is not re-litigation: it is A1's own bar ("est=59
conditioned frame") enforced against kill-grade standing law.

---

## PRE-REGISTRATION (locked before formal tests)

**LEG-VALID bar:** a 59→X window is a VALID "est X" leg iff class(59)='EST'
in classification.json (pre∈{64,94,93}, not S5-fenced, not LEFTOVER/ESTE/
FENCED/NEUTRAL). Otherwise the leg is VOID for the predicative frame.

**FRAME bar (A1's own):** predicative-frame grant STANDS iff ≥2 valid legs;
1 valid leg → HOLD; 0 valid legs → DEMOTE to HOLD (frame unanchored — the
successor-profile compatibility (b) cannot carry the grant alone since the
bar required ALL of (a)(b)(c)).

**Double-count bar:** @1795(94-cell)/@1796(59-cell) are ONE physical window
(94-59-37); the A1 "6 + 1 negated" count is 6 unique windows, not 7.

**New-value bar (30="pas"):** LEAD-grade iff ≥2 independent legs in the
canonical ne-frames ("n'est [30]" EST + "ne [V] [30]" ESTE-or-better), with
the 19-window census queued (not run here).

**19-vs-42 ranking:** rank by count of VALID est-legs, fresh eyes, no
deference to the round-15 ordering.

**37-syllable lead:** the finder's TIER-2 reading (37 as verb-stem/syllable
from unfenced positions) is recorded as a LEAD needing its own battery;
this battery adjudicates only the leg-voiding.

---

## TESTS

`t = code/crowd16/next-token/test_est.py`.

| # | assertion | got |
|---|-----------|-----|
| 1 | class(528/624/912/1178/1443/1796) = LEFTOVER ×6 | |
| 2 | 59→37 starts = [528,624,912,1178,1443,1796]; no other | |
| 3 | P[1794:1798] = [42,94,59,37] (single physical window) | |
| 4 | class(316) = EST, class(1210) = EST, class(448) = ESTE | |
| 5 | 59→32 starts = [316,448,1210] | |
| 6 | class(463) = LEFTOVER, class(1186) = ESTE | |
| 7 | 59→42 starts = [463,1186] | |
| 8 | class(1777) = EST; 59→19 = [1777] | |
| 9 | class(559) = EST; class(1715) = ESTE | |
| 10 | 59→30 starts = [559,1715] | |
| 11 | class(763) = EST (39's leg); class(103) = EST (45's leg) | |
| 12 | EST-class keys = {103,316,559,763,1210,1777} (exactly 6) | |
| 13 | 64→32 (no 59): starts of [64,32] with P[i+1]!=59 | |
| 14 | finder tension spot: 26→32, 56→32, 91→32 counts | |

---

## VERDICT

**The finder's headline is CONFIRMED at the classification level.** Every
cipher-side number re-derived exact; the ISLET-10 classification
(`code/crowd10/conditioner59/classification.json`, kill-grade round-10 law)
was never applied to the A1 legs by the round-15 battery or its red team —
a scope gap in the round-15 adjudication, parallel to the A15 scope gap the
red team itself flagged. What follows enforces A1's OWN bar ("est=59
conditioned frame") against standing kill-grade law. This is not
re-litigation of settled kills; it is new evidence (the classification
check) applied to the A1 legs.

### Leg audit (per the LEG-VALID bar)

| X | claimed legs | valid (class=EST) | verdict |
|---|---|---|---|
| 37 | 6 + "n'est 37" @1795 | **0** — all six LEFTOVER; @1795(94-cell)/@1796(59-cell) are ONE physical window ([42,94,59,37] @1794), so A1's "6+1" was 6 unique, not 7 | **DEMOTE → HOLD** |
| 42 | 2 | **0** — @463 LEFTOVER, @1186 ESTE | **DEMOTE → HOLD** |
| 32 | 3 | **2** — @316/@1210 EST; @448 ESTE correctly excluded | **frame STANDS (3→2 legs)** |
| 19 | 1 | **1** — @1777 EST, verified genuine est-arm | **HOLD confirmed (leg verified)** |
| 30 | — | @559 EST "n'est 30" + @1715 ESTE "ne [44-59] [30]" | **NEW LEAD: 30="pas"** |
| 39 | — | @763 EST, single | predicative HOLD (candidate) |
| 45 | — | @103 EST, single | predicative HOLD (candidate) |

### Demotion rationale (37, 42)

A1's bar required ALL of (a)(b)(c); clause (a) demanded "≥2 independent
'est X' windows (est=59 conditioned frame)". For 37: zero windows satisfy
the conditioning — the grant fails its own clause (a). For 42: the bar was
"met EXACTLY (2 legs)" — both legs void (LEFTOVER + ESTE) — the grant fails
exactly. **37 and 42 are DEMOTED from "predicative frame GRANTED" to HOLD:**
the frame is unanchored, not killed (clause (c) is vacuous with zero valid
"est X" windows; the successor-profile compatibility noted in A1 survives as
unanchored distributional evidence). The round-15 red-team confirmation of A1
is superseded on these two groups by the classification evidence it did not
examine.

### 19-vs-42 ranking (fresh eyes)

**19 > 42.** 19 holds one genuine EST leg (@1777, "ce qui est 19 [48] [74]");
42 holds zero. The working board's "19 HOLD at 1 leg" is CONFIRMED and the
leg is now classification-verified (stronger than round 15's count-only
check). Full battleground ranking: **32 (2 valid, frame stands) > 19 (1
valid, hold) > 30 (ne-frame lead, 2 legs) > 39/45 (1 leg each) > 42 (0,
demoted) > 37 (0, demoted).**

### 32 — frame stands, with live tension

The two surviving legs (@316: "qui est 32 [94] [06]"; @1210: "qui est 32
[48] par", 96=par banked favoring past-participle) are the best adjective
evidence in the lane. The finder's verb-position tension is REAL and
re-derived: 64→32 direct ×2 ([32,854] bigram starts; finder cited 32-cells
[33,855] — convention note), 26→32 ×2, 56→32 ×2, 91→32 ×2, 32→48 ×4.
Tension, not kill: the adjective/verb fight for 32 goes to the class battery.

### 30="pas" — NEW LEAD (not promotion)

Two independent ne-frame legs: @559 EST "n'est 30 [67] [11]" and @1715 ESTE
"ne [44-59] [30] [64] [47]" — the two canonical "pas" slots. LEAD-grade;
the 19-window census ("26-30" ×4, "24-30" ×3 must pattern as negative-adverb
frames) is QUEUED, not run. No promotion on two legs where one is ESTE.

### 37 TIER-2 (syllable reading) — recorded as LEAD

The finder's unfenced-position reading (37 as verb-stem/syllable, "cern"-family
candidate from "en 37-78"/"qui 37-01"/"pre-37"/"er-37") is a legitimate LEAD
needing its own battery — not adjudicated here beyond the leg-voiding. Note
the finder's count slips, corrected: **37-01 ×3** @939/@1633/@1817 (not ×2 —
the round-15 A12 grant is ×3), **37-78 ×4** @312/@414/@475/@1770 (not ×2 —
the finder cited only the en-predecessor pair).

### Queued batteries

1. 37-syllable battery (unfenced positions; "cern" test vs "pre-37"/"er-37").
2. 32 adjective-vs-verb class battery (resolve the 64/26/56/91-32 tension).
3. 30="pas" 19-window census.
4. 19 predicative battery (profile vs 32; shared 48-follower).

Weakest leg for self-critique: the 32 frame now stands on exactly 2 legs
(@316/@1210) — one leg lost to ESTE reclassification would drop it to HOLD;
and both legs lean on 94/48 followers whose own values are provisional.
