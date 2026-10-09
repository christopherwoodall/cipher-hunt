# Battery report: formula-49-value

- Target: `formula-49-value`
- Claim: "name 49's class/value via its full contact profile (n(49)=12: 49-prev x5 of 74, plus 7 non-74 windows)"
- Date: 2026-10-09
- Worker: battery worker (subagent e7c4e948-b1c2-456f-8de0-67d0aa29d05d)
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` +
  `code/side-keyhunt/repaired_offsets.json`, parsed like
  `code/side-keyhunt/repair_parse.py`; asserts held: 1,847 pairs, 96 types).
  `canonical.py` never used. R5005, sealed gates, red-team adjudication queue
  untouched.
- Lock: `code/crowd17/next-token/locks/formula-49-value.lock` (created at start,
  deleted at end; no prior lock existed).

## Bar (verbatim from battery-queue.json, pre-registered BEFORE testing)

"name 49's class at battery grade with byte evidence, or fence 49 as class-open; a named 49 unlocks the '49 74 74' chain parse"

## Numbered pass/fail clauses (restated before testing, not modified after)

1. **C1 (name arm)** — 49's class is named at battery grade with byte evidence
   (one class fits all 12 windows with <=1 unstated assumption).
2. **C2 (fence arm)** — 49 is fenced as class-open with the surviving and dead
   legs stated.

## Adopted premises (not re-litigated)

- `noun-74-formula` NULL (2026-10-09): the '49 74 74' chains (x4) carry the
  '74 74' doubling that kills any whole-word nominal/formula head at kill
  grade; the "49 74 74" unit reading is queued as `unit-49-74-74` (not
  re-tested here). 49 and 74 both unvalued (§3 bars inventing values).
- Standing values: 46=que (GT), 47=ce (prom, A4), 48=e (prom), 40=e (GT),
  64=qui (prom), 76=masculine noun (promoted R19), 36=noun (class, R18),
  78=['ver','lead'], 93=verb-class (R19).
- R24: 24 is finite/modal verb unless its follower is 85 (then "en").

## The 12 windows (byte-exact, 0-based)

| # | pos | row | window (±4) |
|---|-----|-----|-------------|
| 1 | @366 | a2_06 | `76 47 78 48 [49] 61 70 17 06` |
| 2 | @416 | a2_08 | `84 51 37 78 [49] 74 74 46 49` (chain W1) |
| 3 | @420 | a2_08 | `49 74 74 46 [49] 36 29 47 14` (chain W1 tail: "que 49 [36-noun]") |
| 4 | @653 | a4_02 | `52 82 94 76 [49] 24 26 30 03` |
| 5 | @815 | a5_05 | `24 65 14 29 [49] 74 74 47 78` (chain W2) |
| 6 | @860 | a5_07 | `48 84 02 24 [49] 74 74 48 47` (chain W3) |
| 7 | @875 | a5_08 | `89 48 20 74 [49] 16 77 86 78` |
| 8 | @909 | a5_09 | `18 55 83 54 [49] 64 83 59 37` ("54 49 qui de") |
| 9 | @918 | a5_09 | `96 09 02 24 [49] 74 74 40 08` (chain W4) |
| 10 | @990 | a6_01 | `89 48 01 76 [49] 24 26 30 03` |
| 11 | @1433 | a7_08 | `61 12 16 76 [49] 64 52 82 16` ("76 49 qui 52") |
| 12 | @1844 | a8_11 | `83 21 67 78 [49] 74 93` (49-prev of 74, no doubling) |

Contact profile: prev {48:1, 78:2, 46:1, 76:3, 29:1, 24:2, 74:1, 54:1};
fol {61:1, 74:5, 36:1, 24:2, 16:1, 64:2}.
Byte-exact repeat: the 6-gram "76 49 24 26 30 03" occurs at 0-based @652
and @989 (49s at @653/@990) — the only repeated multi-cell frame containing
49 outside the chains. Both 24s (@654, @991) have follower 26 (not 85), so
R24 declares them finite/modal verbs.

## C1 test — class-by-class elimination

**Verb-49: DEAD at kill grade.** In the byte-identical "76 49 24 26 30 03"
windows, 76 is a promoted masculine noun and 24 is finite/modal (R24). The
frame "[N] [49-V] [V-fin]" is ungrammatical in 1841 French for every verb
form: finite (two adjacent finite verbs), infinitive (bare INF between a
noun and a finite verb), participle (unlicensed between noun and finite
verb). The x2 repetition rules out a one-off misread. Verb class globally
dead for 49.

**Determiner-49: DEAD at kill grade.** Same windows: "[76-N] [49-det]
[24-fin]" — a determiner cannot sit between a noun and a finite verb in
French. Global kill.

**Relative/interrogative-pronoun-49: DEAD at kill grade.** @909 and @1433
show "49 64" with 64=qui promoted — two adjacent relative pronouns are
ungrammatical. Global kill.

**Adverb-49: strained, not nameable.** "[76-N] [49-adv] [24-fin]" at
@653/@990 is grammatical (adverb preposed to verb), but @909 "[54] [49-adv]
qui" is hostile (adverb before a relative pronoun is ungrammatical) and
@366 "e [49-adv] [61]" needs 61 named as a verb (unvalued). Two rescues
required — over budget.

**Noun-49: strained, not nameable.** Fits @909 ("54 [49-N] qui", needs 54
as determiner/noun — 1 assumption) and @875 ("74 [49-N] 16"), but @420
"46(que) [49-N] [36-noun]" is hostile: two bare nouns after relative "que"
is ungrammatical, and @366 "48(e) [49-N] [61]" needs a story for 48='e' +
bare noun. Not battery grade.

**Adjective-49: best surviving leg, not battery grade.** @653/@990
"[76-N] [49] [24-fin]" is the canonical post-nominal adjective position,
repeated byte-exactly; @1433 "[76-N] [49] qui" is adjective-before-relative,
grammatical. But two hostile windows: @366 "48(e) [49] [61]" — 48='e' is a
promoted particle, not a noun host, so the adjective has nothing to modify;
@420 "46(que) [49] [36-noun]" — adjective before a bare noun is
ungrammatical in French. Each hostile window needs a rescue (a naming act
for 61, a re-segmentation at @420); that is 2+ unstated assumptions — over
the battery-grade budget.

No class fits all 12 windows within budget. The '49 74 74' chain parse
remains locked: it needs 49 named (this battery) AND the '74 74' doubling
resolved (`unit-49-74-74`, already queued) — the bar's unlock clause does
not fire.

**C1: FAIL.**

## C2 test — fence 49 as class-open

C1 fails; fence executes. 49 stays class-open. Standing partial results:

- Killed for 49 globally: verb, determiner, relative/interrogative pronoun
  (all at kill grade, see C1).
- Best surviving leg: adjective (hostile windows @366, @420 recorded;
  the byte-identical "76 49 24 26 30 03" x2 frame is its positive evidence).
- Strained legs: noun, adverb.
- The four chain windows plus @1844 keep 49-prev-of-74 as its dominant
  contact (5/12); the chain parse needs both this fence lifted and the
  '74 74' doubling resolved.

**C2: FIRES.**

## Verdict: NULL

No class nameable at battery grade; 49 fenced as class-open with three
classes killed and the adjective leg as the leading survivor. No standing
or red-team verdict contradicted or downgraded; §7 intact (67 sole
polyvalence); canonical-stream caveat stands.

## Adverses answered

- None listed on the target.

## Follow-up targets (nulls regenerate work; all three verified ABSENT from battery-queue.json)

1. `adj-49-420-366` (P3): resolve the adjective leg's two hostile windows —
   @366 ("48(e) 49 61": find 49 a host or kill the adjective leg) and @420
   ("46(que) 49 36-noun": test re-segmentation or a second class for 49 at
   this window). Bar: adjective-49 named iff both windows parse with <=1
   total unstated assumption; else the adjective leg is killed and the
   "76 49 24" formula needs a new class.
2. `formula-76-49-24` (P3): test the byte-identical "76 49 24 26 30 03" x2
   frame (@652/@989) as a licensed French formula — state the frame ("N
   [49] [V] …") with 1841 attestations, or fence it as an unparsed repeat.
   Bar: >=1 genuine 1841 formula attestation licenses the frame; confirmed
   zero fences it.
3. `noun-49-909-875` (P4): test the noun leg at its two cleanest windows —
   @909 ("54 49 qui": name 54's class; determiner/noun-54 licenses
   "54 [49-N] qui") and @875 ("74 49 16": 74 as host). Bar: noun-49 named
   iff both windows parse with <=1 unstated assumption; else fence the
   noun leg.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-formula-49-value.md` (this file).
- Queue: `battery-queue.json` — `formula-49-value` status `queued` ->
  `verdict`, result `null`, date 2026-10-09 (temp-file + rename; pre-write
  assert confirmed queued/verdictless; JSON re-validated post-write; only
  this entry's keys touched; no downgrade).
- Lock created at start, deleted at end (verified gone).
