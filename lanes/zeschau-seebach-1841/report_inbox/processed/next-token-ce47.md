# Round-16 battery: ce47 — allophone VERIFICATION

Finder report: `code/crowd16/report_inbox/next-token-findings-ce47.md` (ingested 2026-10-07).
Status entering: 47="ce" GRANTED (allophone tier, round-15 A4, red-team confirmed;
@548 exception and @611 strain already handled and fenced there).

---

## PRE-REGISTRATION (locked before formal tests)

**Scope:** verification only. Nothing here can promote 47 (already granted at its
maximal tier); the question is whether any window FORCES a demote/split review.

**Break bar (value):** a window counts as a VALUE break iff 47's local profile
forces a non-"ce" reading after eliminating (i) sentence-boundary parses and
(ii) fork/provisional-conditioned alternatives. ≥1 such window → the battery
returns "BREAK — red-team demote/split review"; 0 → verification HOLDS.

**Rule-break bar (positional):** accepted as CONDITIONED iff (a) the
conditioning value is at least a lane lead (24="en" is a lead), and (b) the
window parses cleanly under the conditioned reading ("en ce que").

**Anomaly bar:** @611-style strains stay FENCED (conditional), not kills, while
≥2 clean "ce"-frames outweigh them per window — but a SECOND independent
"ce-le-ce"-shaped anomaly would escalate to a value review.

**Cluster bars:** systematic new clusters (29-47×4, qui-47×2, 47→64=0) get
re-derived counts and queued batteries; none kill 47 on their own.

---

## TESTS

`t = code/crowd16/next-token/test_ce47.py`.

| # | assertion | got |
|---|-----------|-----|
| 1 | n47 = 28 | |
| 2 | 47 windows (starts) = full 28-list | |
| 3 | 24→47 starts = [548] (single) | |
| 4 | 47→46 starts = [151, 548, 864] | |
| 5 | 47→11 starts = [269, 357, 498] | |
| 6 | 47→64 count = 0 | |
| 7 | 87→64 count = 5 | |
| 8 | 47→78 starts = [363, 818, 981, 1104, 1396] | |
| 9 | 29→47 starts = [23, 423, 1231, 1591] | |
| 10 | 64→47 starts = [1272, 1718] | |
| 11 | @611 window P[608:615] = [64,2,58,47,77,87,83] | |
| 12 | @864 window P[862:868] = [74,48,47,46,0,...] | |
| 13 | 47→33 starts = 2 | |
| 14 | 47→77 starts = [611] | |

---

## VERDICT

**No value break found — verification HOLDS.** Full 28-window census re-derived
exact; zero windows force a non-"ce" reading after eliminating boundary and
provisional-conditioned alternatives. The allophone-tier grant (round-15 A4)
stands.

**@548 positional break — CONDITIONED, already adjudicated.** The finder's
flag is consistent with A4's own grant: the bar was met on the ≤1-shift clause
with the @548 exception explicitly parsed as "en ce que" (bonus mirror frame).
Per the rule-break bar: 24="en" is a lane lead (conditioning legitimate), and
"en ce que" parses clean. The original "never after en" formulation is
SUPERSEDED by the conditioned form recorded in A4 — the finder is re-flagging
settled ground, correctly characterized.

**@611 "ce le ce" — stays FENCED.** Re-derived exact ([64,2,58,47,77,87,83]
@608). No second "ce-le-ce"-shaped anomaly in the census → no escalation per
the anomaly bar. Explanation (a) ranked first by lane law (77 is provisional
with a known adverse; 47≠"ce" would be a second polyvalence — forbidden
without killing (a)). The finder's P-battery (re-profile 77 in 47-77 vs 87-77
frames) is queued for the 77-promotion battery (red-team follow-up #2) —
it is a 77 question, not a 47 question.

**29-47 ×4 — CONFIRMED systematic, queued as battery, not a break.**
Re-derived [22,422,1230,1590] (bigram starts; finder's @23/@423/@1231/@1591
are the 47-cells — convention note). @23/@1231 = "29-47-33" ("-er ce [INF]"),
@423 = "29-47-14", @1591 = "29-47-08". "…er ce…" survives via sentence-boundary
parses; the word-internal "[stem]erce" alternative is genuinely testable via
contact profiles — queued, not verdict-bearing.

**qui-47 ×2 → "se"-rival — the strongest 47-rival on the board.**
Re-derived [1271,1717]; @1271 = [30,20,64,47,76,87,76], @1717 = [59,30,64,47,68,6,11].
"qui se [76/68]" is natural French IF 76/68 are verbal. This does NOT break the
grant (boundary parses survive), but the battery is priority: **if 76/68 profile
verbal, the positional amendment "47='se' before verbs" would be a second
polyvalence — that escalates to red-team review immediately** (lane law: 67 is
the sole true polyvalence).

**47→64 = 0/28 vs 87→64 ×5 — CONFIRMED, recorded as positional restriction.**
Not a break; the allophone's positional spec now reads: 47 mirrors 87's
frame inventory EXCEPT never after 24 (unconditioned; @548 conditioned) and
never before 64 ("ce qui" slot). Two more ad-hoc positional exceptions and
the spec starts looking like overfitting — next round should try to NAME the
conditioning rule, not list exceptions (weakest leg, see self-critique).

**P3 @864 — REAL adverse, but against 00="pour", not 47.**
Re-derived: P[861:868] = [74,74,48,47,46,0,86] = "à ce que pour [86-INF]…".
Under 00="pour" this window is broken French ("à ce que" takes a subjunctive
clause; "pour"+INF-class cannot be its subject). 47's own frame ("à ce que")
is clean. HANDOFF to the pour battery as a named adverse — this is the
cheapest decisive test of 00="pour" on the board.

Finder transcription notes (cosmetic): bigram-vs-cell convention wobbles
(@23/@423 vs [22,422] etc.); all resolve to identical physical cells.

**Queued batteries:** B1 76/68 verb-hood (decides qui-ce vs qui-se; escalation
clause above); B2 77 re-profile in 47-77 vs 87-77; B3 29-47 boundary
(word-internal "erce" test); B4 name the allophone conditioning rule.
