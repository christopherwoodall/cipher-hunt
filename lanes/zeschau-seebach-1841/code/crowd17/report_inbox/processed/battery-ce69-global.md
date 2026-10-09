# Battery report: ce69-global

**Target:** `ce69-global` (P2)
**Date:** 2026-10-09
**Verdict:** PROMOTE (finding grade — battery-level support for 69='ce'; actual global promotion is a red-team act)

## Bar (verbatim from queue)

"kill iff any window forces a non-'ce' value"

## Bar restated as numbered clauses

1. Test 69='ce' across all 12 windows of 69 on the repaired stream.
2. Kill iff any window forces a non-'ce' value (grammatically impossible under 69='ce' with no licensed alternative).
3. If no window fires the kill arm, the value survives at battery grade.

## Method

Read BATTERY-PROTOCOL.md first; created `locks/ce69-global.lock` (deleted on completion).
Re-derived the repaired 1,847-pair / 96-type stream in-session
(`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`,
per-row upstream tokenization `[s[i:i+2] for i in range(o, len(s)-1, 2)]`).
Asserts held: 1,847 pairs, 96 types. `canonical.py` never used.
R5005, sealed gate instances, red-team adjudication queue untouched.
n(69)=12 byte-confirmed. Followers: 26 x3 / 13 x2 / 88 x2 / 14 / 24 / 11 / 74 / 64
(matches the locus battery's re-derivation).

Standing constraints used as premises only (protocol §7): 11=la, 29=er, 46=que,
87=ce (granted), 64=qui, 00=pour, 84=on, 47=ce (A4 allophone tier), 59=est and
77=le (provisional), 92=verb class subset-scoped (R18), 21=noun class
(battery-promoted), 26=noun lead, 94=ne (R17-001 STRONG LEAD).

## Window-level evidence (0-based @-offsets)

1. **@67** `94 92 69 13 24` — ne [verb-92] **ce** [13] [24-fin]. Post-verbal "ce"
   as pronoun/object. Nothing forces non-'ce'.
2. **@177** `86 21 69 14 24` — [86] [21-noun] **ce** [14] [24]. Under the live
   clitic arm (en14-three-window PROMOTE), 14='en' gives "ce en [24]" = "c'en",
   requiring the contraction/dissolution move — the same licensed reasoning as
   the granted "cela" dissolutions, but it is a stated caveat, not a kill.
   14='le' would be ungrammatical ("ce le") but 14's determiner is fenced to
   @117 only, so no forced contradiction. **Not forced.**
3. **@405** `53 34 69 26 00` — [53] [34=i] **ce** [26-noun] pour. Clean
   determiner frame ("ce [noun]"). **Not forced.**
4. **@805** `98 53 69 24 24` — [98-fin] [53] **ce** [24-fin/modal]. Pronoun-face
   ("ce semble"-type). Clean. **Not forced.**
5. **@933** `83 56 69 26 00` — [83] [56] **ce** [26-noun] pour. Clean
   determiner frame. **Not forced.**
6. **@1115** `38 30 69 11 88` — the "cela" locus (battery PROMOTE, locus-level):
   "69 11"="cela" requires 69 to be 'ce'-class. **Supports 'ce'.**
7. **@1259** `31 29 69 88 01` — [31]er **ce** [88]. "ce" as object of an
   infinitive. Grammatical. **Not forced.**
8. **@1266** `50 46 69 88 24` — [50] que **ce** [88] [24]. "que ce [verb] [verb]"
   grammatical. **Not forced.**
9. **@1380** `84 92 69 13 24` — on [verb-92] **ce** [13] [24]. Same frame as @67.
   **Not forced.**
10. **@1413** `16 97 69 74 34` — [16] [97] **ce** [74] [34=i]. 74 is class-open;
    "ce [74]" is grammatical under either nominal-74 (determiner) or verbal-74
    (pronoun+verb). **Not forced.**
11. **@1627** `46 56 69 26 00` — que [56] **ce** [26-noun] pour. Clean determiner
    frame. **Not forced.**
12. **@1835** `59 36 69 64 22` — est(59) [36] **ce qui**(64). Textbook "ce qui".
    **Not forced.**

## Per-clause pass/fail

1. **PASS.** All 12 windows tested under 69='ce' with standing values only.
2. **Kill arm does not fire.** Zero windows force a non-'ce' value. The only
   tension is @177's 14-contact, which is resolved by the licensed
   contraction/dissolution move ("c'en") — a caveat, not a contradiction.
3. **PASS.** The value survives at battery grade.

## Homophony cost (claim asks; red team decides)

- Banked 47='ce' (A4, allophone tier, n=28) and promoted 87='ce' (n=32)
  already share the value. 69='ce' (n=12, 0.65% of stream vs 1.52%/1.73%)
  would be a third 'ce'-group — homophony, not polyvalence (polyvalence is
  one group with multiple values; 67 et/veut remains the sole true
  polyvalence). Per protocol, frequency uniformity is necessary but
  insufficient for homophony; 69's ~2.6x frequency gap is recorded as a cost,
  not a battery kill. Determiner↔pronoun is one French word (det-14-census
  doctrine), so the determiner legs (x3 "ce [26]") and pronoun legs coexist
  without a §7 declaration.

## Adverses

- "69='ce' as a global value needs red-team authority to promote; battery
  test feeds that decision." **ANSWERED.** This verdict is battery-grade
  evidence only — no registry, grid, or decode change; the global promotion
  is explicitly left to the red team. No polyvalence declared; §7 intact.
- The locus-level cela-69-11-word PROMOTE is consistent (it already required
  69 to be 'ce'-class at @1115); no standing verdict contradicted or
  downgraded.

## Load-bearing caveats

- @177's "c'en" read is a dissolution/contraction move (stated, not hidden);
  if red team rejects dissolution for 69-14, re-open this window.
- @805/@177 legs are conditional on 24=finite/modal (red-team docket
  `24-en-verb-conflict` live); under 24='en' they re-parse.
- All 12 rows carry unvalidated upstream offsets (canonicality caveat); the
  verdict holds on the canonical stream per protocol.

## Verdict: PROMOTE (finding grade)

69='ce' survives all 12 windows with zero forced contradictions: three clean
"ce [26-noun]" determiner legs, one textbook "ce qui", the pronoun-face
"ce [24]", the locus-confirmed "cela" fusion, and five further compatible
windows. Recommended as red-team input for the global-value decision.

## Bookkeeping

- Lock `code/crowd17/next-token/locks/ce69-global.lock` created on start,
  deleted on completion (verified gone).
- `battery-queue.json`: `ce69-global` queued -> verdict/promote, 2026-10-09
  (pre-write assert confirmed no prior verdict; temp-file + rename; JSON
  re-validated; only this entry touched).
- R5005, sealed gates, red-team adjudication queue untouched.
