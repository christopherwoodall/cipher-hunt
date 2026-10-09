# Battery verdict: w5-pas-verb

## Bar (verbatim, pre-registered)
"name a finite verb in '[15] [01] [56]' that 'pas' @1733 negates (test 15/01 verb-hood; test 56=verb via 'qui 56' @794 and the '01 56' x2 subject+verb parallel @1653/@1731), or fence 'pas' @1733 as ungrammatical"

Restated as numbered clauses:
1. C1 — a finite verb is named among {15, 01, 56} that 'pas' @1733 negates.
2. C2 — 15's verb-hood tested.
3. C3 — 01's verb-hood tested.
4. C4 — 56's verb-hood tested via 'qui 56' @794 and '01 56' x2 @1653/@1731.

## Method
Read BATTERY-PROTOCOL.md first. Lock created on start, deleted on completion.
Stream re-derived in-session from `data/upstream-ct_R5005.txt` +
`code/side-keyhunt/repaired_offsets.json`, parsed per `repair_parse.py`
(1,847 pairs / 96 types verified). `canonical.py` never touched; R5005, sealed
gates, red-team queue untouched. 1841 diplomatic French only.
Offset note: the brief's "@" indices are 0-based stream indices of the token;
byte-identical windows verified in-session.

## Window
0b@1733 = "30", row a8_07. ±8 context (0-based indices):
`39(1726) 88(1727) 24(1728) 30(1729) 15(1730) 01(1731) 56(1732) 30(1733) 06(1734) 60(1735) 12(1736) 48(1737) 52(1738) 86(1739)`

The frame: `… 24='faire' | 30='pas' | 15 01 56 | 30='pas' 06='ent' | 60 12 48 …`.
Two bare-pas tokens: @1729 (follows 24='faire', battery-promoted) and @1733
(follows 56). Ne-drop is lane precedent (battery-w2-pas-nelicense, PROMOTE):
bare "pas" carries negation, 16/19 'pas' windows lack "ne".

## Per-clause results

- **C1 — PASS.** The finite verb negated by 'pas' @1733 is **56**
  (class-level; value open). Pas sits in immediate left contact with 56
  (the ne-drop "V pas" position), and "56 30" occurs exactly 2x stream-wide
  (@1326 0b: "…62 98 | 56 30 06 | 62 94 70…"; @1732 0b: "…15 01 56 | 30 06 | 60
  12 48…"), both times the "56 30 06" trigram — a repeated pas-negated-56 frame.
- **C2 — PASS (15 verb-hood tested, excluded at W5).** 15 n=10, all windows
  re-read: predecessors {60, 94, 41x2, 98, 79, 66, 58, 30, 61}, successors
  {63, 33x2, 66, 24, 59, 23, 01, 93x2}. No finite-verb frame puts pas @1733
  adjacent to 15 (three tokens left); "24 30 15" is faire-negated-by-pas, not
  15-verb. 15 is not the negated verb.
- **C3 — PASS (01 verb-hood tested, excluded at W5).** 01 n=28. 01 takes
  29='er' once (0b@596: "85 01 29 40" = "[85] [01]er e" — infinitive-shaped,
  not finite) and 24 x3, 06 x1, but in the W5 frame 01 sits between 15 and 56,
  two tokens from pas; nothing makes 01 the pas-adjacent finite verb here.
- **C4 — PASS.** 'qui 56': exactly 1x stream-wide, 0b@795 row a5_04
  ("…64 56 37…"), 64='qui' banked GT — relative-clause verb slot (bar's @794
  is the 1-based index of the same window). '01 56': exactly 2x stream-wide,
  0b@1654 row a8_04 ("…82 16 01 56 37…") and 0b@1732 row a8_07 (the W5
  window) — the subject+verb parallel holds (bar's @1653/@1731 are the 1-based
  indices). Bonus legs: 'que 56' x2 (46='que' banked GT): 0b@1626
  ("…33 46 56 69…" subjunctive slot) and 0b@1745 ("…82 46 56 40…").

## Adverses
None listed in the target brief.

## Fenced residuals
- "56 qui" x1 (56→64): nominal counter-signal — 56 is not uniformly verbal.
  Class claim only; no polyvalence declared (§7 intact).
- The 06 token after 30 ("56 30 06" x2): unresolved attachment; does not
  disturb the "56 pas" negation frame.
- 56's value stays open; no other window is decided here.

## Verdict: PROMOTE (finding grade)
56 is the finite verb negated by bare-'pas' @1733, class-level, value open.
No standing verdict contradicted or downgraded.

## Follow-ups
None required (promote verdict).
