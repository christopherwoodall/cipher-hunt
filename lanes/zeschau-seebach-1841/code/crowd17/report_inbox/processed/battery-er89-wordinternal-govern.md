# Battery report: er89-wordinternal-govern

- Target id: `er89-wordinternal-govern`
- Claim: "Adjudicate word-internal vs governed-infinitive at @275/@1377/@1393/@113/@781 with a syllabary uniformity test; kill one fork."
- Date: 2026-10-09
- Worker: battery worker (subagent 199a3543-6ec3-4bce-803d-de1950fec8cb)
- Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json +
  data/upstream-ct_R5005.txt, parsed like code/side-keyhunt/repair_parse.py;
  n=1847 asserted, 96 types asserted). All @-offsets are 0-based repaired-stream indices.
  `canonical.py` never used. R5005, sealed gates, red-team adjudication queue untouched.
- Lock: code/crowd17/next-token/locks/er89-wordinternal-govern.lock (created at start,
  deleted on completion; no prior lock existed).

## Bar (verbatim, pre-registered before testing)

"Adjudicate word-internal vs governed-infinitive at @275/@1377/@1393/@113/@781 with a syllabary uniformity test; kill one fork."

Numbered pass/fail clauses (restated before testing, not modified after):

1. (C1) The syllabary uniformity test is defined and executed on the repaired
   stream: for every "29 X" contact, X's bound-morpheme vs free-word status is
   set against the contact's word-internal vs word-boundary status.
2. (C2) One fork is killed at kill grade: either a window forces it false, or
   the distributional uniformity test rejects it at the lane's standard
   (zero-counterexample uniformity, per the protocol's kill criteria).

## Method

1. Re-derived the repaired parse in-session; asserted 1,847 pairs / 96 types.
   Never used canonical.py. R5005 not touched.
2. Confirmed "29 89" occurs exactly 5x stream-wide, at 29-positions
   112/274/780/1376/1392 — i.e. exactly the five target windows
   (89 at @113/@275/@781/@1377/@1393). No other er-89 windows exist.
3. Adopted as premises (not re-litigated): 29="er" (banked), 40="e" (banked),
   47/87/45="ce" (granted), 67=et/veut (sole polyvalence), 24=finite modal
   (promoted class), 77="le" (provisional), 85=verb-stem (A3), 80=verb-class /
   determiner split (battery-grade, poly-80-x29-frame), and the parent battery
   noun26-89-class's fenced split (89: noun @640/@871/@1752, infinitive
   @222/@986/@1498).
4. Syllabary-uniformity default (lane precedent, battery-profile-52-host-word):
   each group has one phonetic identity; bound morphemes behave uniformly as
   bound, free words/stems uniformly as free.

## The syllabary uniformity test

**Question.** At "29 89" (= "er" + 89), is 89 word-internal (fork W: one word
"[G]er89") or standalone (fork G: two words "[G]er" + "[89]")?

**Test design.** Census every "29 X" bigram stream-wide (45 total, 18 distinct X).
For each X with a determinable status, set X's bound-morpheme vs free-word status
against whether "29 X" is word-internal or a word boundary under licensed parses.

**"29 X" census (byte-exact):**

| X | n | X's status | "29 X" contact |
|---|---|-----------|----------------|
| 40 | 9 | bound morpheme ('e') | word-internal ("première" 34-29-40 x2, etc.) |
| 47 | 4 | free word ('ce') | boundary |
| 87 | 3 | free word ('ce') | boundary |
| 45 | 1 | free word ('ce') | boundary |
| 67 | 2 | free word (et/veut) | boundary |
| 24 | 1 | free word (finite modal) | boundary |
| 80 | 4 | free word-level (verb/determiner) | boundary (poly-80-x29-frame: "[03]er [80]-le", "[92]er [80] fois") |
| 85 | 3 | free stem (verb-stem, A3) | boundary (a stem is word-initial by definition) |
| 42/88/60/49/74/69/37 | 1-3 each | open | ambiguous (not determinable) |
| 82 | 3 | letter-tier ('m') | excluded (letter mechanism, special) |
| 89 | 5 | **free word/stem (see below)** | **the question** |

**Uniformity result: 27/27 determinable, zero exceptions.**
"29 X" is word-internal IFF X is a bound morpheme (9/9, all X=40='e').
"29 X" is a word boundary IFF X is a free word/stem (18/18: ce x8, et/veut x2,
modal x1, 80 x4, verb-stem 85 x3).

**89's status (forced, byte-verified):**
- Free NOUN stem: @640 ("77 89 48" = "le [89]e", conditional on provisional
  77='le'), @871 (same shape, same condition), @1752 ("28 89 26 24", 89 as
  subject of finite modal 24).
- Free INFINITIVE stem: @222, @986, @1498 ("24 89", load-bearing on promoted
  24=modal class).
- Forced BOUND/syllabic at 0 of 14 windows.

89 is a free word/stem (6 forced windows), not a bound morpheme. The lane's
bound morphemes (40='e', 48='e', 01='-ci') never take free-stem lives; 89 does.

## Per-window application (all five targets)

Under the uniformity rule, since 89 is a free word, "29 89" must be a word
boundary — uniform with the 18 free-X boundaries. 89 is standalone at:

- @113 (a1_03): "67 93 29 89 68" = "et [93]er | [89] 68" (boundary after 29)
- @275 (a2_03): "67 33 29 89 84" = "et [33]er | [89] on" (boundary after 29)
- @781 (a5_04): "37 08 29 89 11" = "37 [08]er | [89] la" (boundary after 29)
- @1377 (a7_06): "00 86 29 89 84" = "pour [86]er | [89] on" (boundary after 29)
- @1393 (a7_07): "67 86 29 89 16" = "et [86]er | [89] 16" (boundary after 29)

For fork W to hold, 89 would have to be a bound morpheme fusing after "er" —
but 89 is a free stem at 6 windows, and no free word/stem in the lane's
syllabary ever fuses after "er" (0/18). The word-internal fork is rejected
at the lane's distributional standard.

Note on the "cela" counter-precedent: 11="la" is a free word with a bound life
in "cela" compounds, but that fusion is licensed by a specific grammatical
rationale ("ce"+"la" as two words is ungrammatical). No such rationale exists
for "[G]er"+"89" — governor + governed infinitive ("aller faire"-shaped) is
grammatical as two words — so no fusion pressure applies, and the "29 X"
uniformity (boundary for all free X) controls.

## Per-clause pass/fail

1. **C1 PASS** — syllabary uniformity test defined (bound-vs-free X against
   word-internal-vs-boundary "29 X") and executed on all 45 "29 X" bigrams:
   27/27 determinable contacts uniform, zero exceptions.
2. **C2 PASS** — the word-internal fork is KILLED at kill grade: the
   distributional test rejects it (89 is a free word/stem at 6 forced windows;
   "29 X" is a boundary for every free X, 18/18; 89-as-bound would be a
   unique 0/18 exception). All five target windows resolve as word boundary
   after 29; 89 is standalone at each.

## Verdict: KILL (the word-internal fork)

"29 89" is a word boundary at @113/@275/@781/@1377/@1393. 89 is standalone
at all five windows; the word-internal "[G]er89" reading is dead.

**Explicitly NOT claimed:** the governed-infinitive fork is NOT proven — it
survives as the remaining alternative (89 as standalone infinitive is
consistent with 89's established infinitive class at @222/@986/@1498), but
the governors' licensing ("[33]er"/"[86]er"/"[93]er"/"[08]er" as
bare-infinitive governors) was not demonstrated here. No value was named;
89's class split (noun vs infinitive, parent battery) is untouched; no
polyvalence declared (§7 intact: 67 et/veut remains the sole true polyvalence).

## Adverses

- None listed in the queue entry.

## Bookkeeping

- Report: code/crowd17/report_inbox/battery-er89-wordinternal-govern.md
- Queue: `battery-queue.json` → `er89-wordinternal-govern` status `verdict`,
  result `kill`, date 2026-10-09 (pre-write assert passed — was
  queued/verdictless; temp-file + rename; JSON re-validated; only this entry
  touched; no downgrade).
- Lock created on start, deleted on completion (verified gone).
- No standing or red-team verdict contradicted or downgraded; §7 intact;
  R5005, sealed gates, red-team adjudication queue untouched.
- Kill verdict — no follow-ups required per protocol (the surviving
  governed-infinitive fork's governor-licensing is already covered by live
  red-team dockets, not duplicated here).
