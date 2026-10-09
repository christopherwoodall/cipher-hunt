# Battery verdict: pre-71-60-class

**Target claim:** name 60's class at @234/@1565 ('60 71' x2).
**Bar (verbatim):** "a nominal 60 reframes 71 as its complement/head-adjacent slot"
**Restated clauses:**
- C1: nominal 60 parses at window A (1-based @233, "21 60 71") with 71 as 60's complement or head-adjacent dependent.
- C2: nominal 60 parses at window B (1-based @1564, "30 06 60 71") with 71 as 60's complement or head-adjacent dependent.
- C3: the result coordinates with (does not preempt) queued `poly-60-redteam` and `verb-60` (verdict/null).

**Method:** read BATTERY-PROTOCOL.md first; lock `pre-71-60-class.lock` created 2026-10-09T04:28:21Z, deleted on completion. Re-derived the 1,847-pair / 96-type stream in-session from `data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json` (parsed per `repair_parse.py`; 1,847 pairs, 96 groups confirmed). `canonical.py` never touched. R5005, sealed gates, red-team queue untouched.

## Byte-verified windows

- '60 71' occurs exactly 2x stream-wide: 1-based @233 and @1564 (60 token).
- Window A, 1-based @225-242: `96 87 46 98 83 82 96 21 [60 71] 51 70 98 41 17 11 26 12` — "...vient de me par [21] [60] [71] [51] pre [98] [41] fois la..." (96='par' banked GT, 87='ce' promoted, 46='que' GT, 83='de' conditioned lead, 82='m' GT, 70='pre' GT, 17='fois' promoted, 11='la' GT). 21 is noun-class (value open). Both windows mid-row (a2_01, a8_01) — no byte evidence for a clause boundary.
- Window B, 1-based @1557-1574: `93 61 40 17 11 26 30 06 [60 71] 50 29 24 74 62 48 56 32` — "[93] [61]e fois la [26] pas ent [60] [71] [50]er [24] [74]..." (30='pas' promoted, 06='ent' granted, 29='er' GT). '21 60' occurs 4x stream-wide (@119/@172/@197/@232).
- 51 (n=6): successors {47,62,70,37,64,45} all x1. 50 (n=11): preceders include 11 x2; successors include 45 x2.

## Per-clause results

**C1: FAIL.** "par [21-noun-class] [60-noun] [71]" — bare [noun] [noun] adjacency. In 1841 French a bare N-N sequence is grammatical only as apposition (coreference, normally punctuated), a proper-name sequence (title+name / forename+surname), or a lexicalized compound (not productive). No byte evidence supports any of the three. 71 as 60's *complement*: French nominal complements require "de"/"à" — absent. 71 as *head-adjacent dependent*: the only bare-adjacency dependent of a noun is apposition — unmotivated with both values open, and name-71's two banked-contact windows (@925 "65 71 17=fois" wants a quantifier/determiner; @1337 "86 71 64=qui" wants a nominal head) do not support an appositive-71. The nominal-60 reframe does not parse at A.

**C2: FAIL.** "[26] pas ent [60-noun] [71] [50]er [24]" — the same bare N-N problem, compounded by an independently anomalous left edge: 30='pas' + 06='ent' (verbal ending) is ungrammatical ("pas" cannot take "ent"); cf. battery-spell-single-consonant (null, 2026-10-09), where the parallel "pasent" window's "passent" reading was grammatically excluded. No class of 60 rescues the window cleanly, so 60's class cannot be decided here either. The nominal-60 reframe does not parse at B.

**C3: HONORED.** Standing state: `noun-60` = verdict/kill (masculine-noun value dead) — no nominal value is on record; `verb-60` = verdict/null; `poly-60-redteam` is queued (pri 1) framing 60's class as adjective-vs-verb. A nominal-60 finding would sit outside the docket's framing; this battery's negative result is consistent with it and preempts nothing. Rival noted without preemption: verbal 60 also fails at both windows ("par"+verb ungrammatical at A without an unevidenced boundary; "pas ent [60-verb]" ungrammatical at B) — the windows are 60-class-hostile generally, which is poly-60-redteam's problem, not this battery's.

**Not kill-grade:** the failures are structural (bare N-N adjacency) but (a) 71's class is open — name-71 fenced 71 as a residual on a value-grade bar; a class-level 71=adjective (epithet) reading would reframe the right edge at both windows and was never tested; (b) window B's left edge is independently anomalous; (c) 60's class question is owned by poly-60-redteam.

## Verdict: NULL (fence executed)

The nominal-60 reframe is fenced at both '60 71' windows: no nominal value is on record, bare N-N adjacency is ungrammatical in 1841 French, and the complement/head-adjacent slot for 71 does not materialize under any standing nominal parse.

## Follow-ups proposed (for supervisor queuing)

1. `adj-60-2160` (P3) — test 60 as postposed ADJECTIVE at the four '21 60' windows (@119/@172/@197/@232): "par [21-noun] [60-adj]" epithet is grammatical; coordinate with poly-60-redteam, do not preempt.
2. `class-71-adjective` (P3) — test 71 as epithet adjective across its 7 windows: @925 "[65-noun] [71-adj] fois" is "dernière fois"-shaped; @1337 "[86] [71-adj] qui" parses with "qui" attaching to the NP; would reframe both '60 71' windows as "[60] [71-adj]".
3. `reseg-1564-pasent` (P3) — re-segment "30 06 60 71" at window B under the "pasent" findings; gates on 26/56 class.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-pre-71-60-class.md`
- Lock created on start (agent id + UTC timestamp), deleted on completion.
- `battery-queue.json`: `pre-71-60-class` → status `verdict`, result `null`, date 2026-10-09 (temp-file + rename; pre-write assert confirmed queued/verdictless; JSON re-validated post-write).
- No standing verdict contradicted or downgraded. §7 intact. No polyvalence declared.
