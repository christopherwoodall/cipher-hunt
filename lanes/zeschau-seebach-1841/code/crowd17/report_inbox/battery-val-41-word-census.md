# Battery `val-41-word-census` — verdict: NULL

Worker: a888d1c6-430b-414d-b748-091426f1c430 · 2026-10-09T16:33:19Z start
Census of the 19 windows of 41. Decides which windows force 41 to be a
standalone word, and whether one word-class parses across all forcing
windows.

## Bar (verbatim, pre-registered)

> "name 41's word-class iff it parses across forcing windows with zero
> kill-grade contradictions"

Restated as numbered pass/fail clauses (before testing):
- C1: every forcing window enumerated — windows that FORCE standalone-word
  41, windows that only admit it, and windows that force a non-word role.
- C2: 41 parses across ALL forcing windows with zero kill-grade
  contradictions (one word-class fits every forcing window).
- C3: 41's word-class is named (licensed only if C2 passes).

## Method

Re-derived the repaired 1,847-pair / 96-type stream in-session from
`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`,
parsed like `code/side-keyhunt/repair_parse.py` (asserts held: 1847 pairs,
96 types; 0-based @-offsets). `canonical.py` never used. R5005, sealed
gates, red-team queue untouched.

Adopted premises (not re-litigated):
- §7 standings: 64='qui' (granted), 17='fois' (granted), 47='ce'
  (granted), 11='la', 85=verb-stem (A3), 67 sole true polyvalence.
- `val-41-det-windows` PROMOTE (battery grade): determiner arm at @237
  ("[98] [41-det] fois la"), values une/chaque/deux/plusieurs unforced.
- `val-41-1016` NULL + findings: 'sans' killed at kill grade (D1 "sans
  fois" 0/31.6M chars; D2 "sans sans" 0/31.6M); determiner-41
  incompatible with @1016; D3 kills det/numeral/adverb at @5.
- `41-doubling-audit` PROMOTE: the @589/@590 "41 41" doubling is
  stream-real, not an offset artifact.
- `41-1016-det-incompatibility` PROMOTE: determiner values fail at @1016
  (package delivered to the split docket).
- 24 is finite/modal per R24 (follower 41 is not 85 — the same standing
  logic that rules out 'en' for 24).
- `split-41-redteam` queued: 41's §7 split candidacy is red-team venue.
  This battery does not adjudicate it.

Terms: "forcing window" = the grammar at that window admits exactly one
role for 41 (any other role is ungrammatical). "Admit" = the window is
compatible with standalone-word 41 but does not require it.

## Window-level evidence (byte-exact, 0-based)

n(41) = 19. Full census, one row per occurrence:

| @ | row | window (pre 41 suc) | role forced |
|---|---|---|---|
| 5 | a1_00 | 47=ce **41** 06 77=le | STANDALONE forced; class adj/noun (det/num/adv killed per D3) |
| 39 | a1_01 | 64=qui **41** 01 24 | STANDALONE forced; class finite VERB ("qui" needs a finite verb) |
| 59 | a1_01 | 53 12 **41** 08 | letter-tier ("12 41"); NOT standalone |
| 91 | a1_02 | 19 **41** 98 | STANDALONE forced (token between verb-lexeme 19 and finite 98); class open, pronoun/clitic-shaped |
| 237 | a2_01 | 98 **41** 17=fois 11=la | STANDALONE forced; class DETERMINER-slot (only det/ordinal/numeral precede "fois la", 31.6M chars) |
| 444 | a2_09 | 78 **41** 10 62 | admits standalone (conditional det; needs nominal 10) |
| 489 | a2_11 | 42 **41** 20 67 | admits (fenced: predicative-42 frame, 67 polyvalent) |
| 589 | a3_02 | 97 **41** 41 09 | doubling (stream-real); kills single-word readings here |
| 590 | a4_00 | 41 **41** 09 00 | doubling (stream-real); kills single-word readings here |
| 808 | a5_05 | 24(fin) **41** 12 48 | STANDALONE forced (finite 24 forces a word boundary); right edge fenced (12 tier open) |
| 964 | a6_00 | 56 **41** 19 24 | STANDALONE forced (standalone token); class open |
| 1016 | a6_02 | 24(fin) **41** 15 66 | STANDALONE forced (finite 24 forces a word boundary); det killed, verb killed, 'sans' killed — class open (adv/prep/pron/noun) |
| 1048 | a6_04 | 85=stem **41** 88 29=er | STANDALONE forced (new word after verb stem); adverb/preposition-compatible |
| 1111 | a6_06 | 73 **41** 65 38 | admits standalone (conditional det; needs nominal 65) |
| 1472 | a7_10 | 12 **41** 53 60 | letter-tier ("12 41"); NOT standalone |
| 1499 | a7_11 | 89 **41** 74 84=on | admits standalone (conditional det; needs nominal 74) |
| 1508 | a7_11 | 56 **41** 12 61 | letter-tier ("41 12"); NOT standalone |
| 1535 | a8_00 | 73 **41** 62 06 | admits standalone (conditional det; needs nominal 62) |
| 1759 | a8_08 | 78 **41** 15 93 | admits standalone (conditional det; needs nominal 15) |

Forcing set for standalone-word 41: @5, @39, @91, @237, @808, @964,
@1016, @1048. Letter-tier: @59, @1472, @1508. Doubling: @589/@590.
Admit-only: @444, @489, @1111, @1499, @1535, @1759.

### The @808/@1016 "'en [41]'" premise — REJECTED

The queueing claim framed @808 and @1016 as "'en [41]'" windows. The
stream reads:
- @808: `53 69 24 24 41 12 48 24 65` → "[24] [41]", 24 immediately before.
- @1016: `78 47 03 24 41 15 66 91 53` → "[24] [41]", 24 immediately before.

24 is finite/modal per standing R24 (its follower 41 is not 85 — the
same logic that rules 'en' out for 24). A finite/modal verb is not the
preposition/pronoun 'en'. The windows read "[24-fin] [41]", not
"en [41]". The premise is fenced with cause: 24's standing class
contradicts the 'en' reading at both windows. What the windows DO force:
a word boundary before 41 (finite verb ends its word), so 41 is
standalone-word here with open class.

### The kill-grade contradiction

- @39 forces finite VERB: 64='qui' is granted; subject-relative "qui"
  requires an immediately following finite verb. No other class parses.
- @237 forces DETERMINER-slot: "[X] fois la" admits only
  determiners/ordinals/numerals in 31.6M chars of period French
  (promoted battery finding, adopted).

No French word-class is both finite-verb and determiner-slot. §7's
sole-polyvalence rule (67 et/veut only) blocks declaring 41 both at
battery grade. The two forcings are mutually exclusive at kill grade.

## Per-clause results

- **C1: PASS.** All 19 windows censused; 8 force standalone-word 41,
  3 force letter-tier, 2 are the stream-real doubling, 6 admit-only.
- **C2: FAIL at kill grade.** @39 forces finite verb; @237 forces
  determiner-slot. Mutually exclusive classes forced at two windows.
  Zero-contradiction condition not met.
- **C3: NOT LICENSED.** The bar names 41's word-class IFF C2 passes.
  C2 failed, so naming is not licensed at battery grade.

## Adverses

- A1 (§7 split venue R20-108/R20-082 untouched): answered by scoping.
  This battery does not adjudicate 41's split. The @39-vs-@237
  contradiction is delivered to the queued `split-41-redteam` docket as
  evidence (verb arm packaged in follow-up 1 below; determiner arm
  already packaged by `val-41-det-windows`).
- A2 (41's value open): preserved. No value named.

No standing or red-team verdict contradicted or downgraded. The
determiner arm (battery PROMOTE) and the verb forcing are both recorded
as arms of the split candidacy, not as competing battery claims.

## Verdict: NULL

41's word-class is not nameable at battery grade: two forcing windows
demand mutually exclusive classes (@39 finite verb vs @237
determiner-slot), and §7 reserves polyvalence adjudication to the red
team. Precedent (`val-41-1016`) treats unnameability as NULL, not KILL.

## Follow-ups (all verified ABSENT from battery-queue.json 2026-10-09)

1. `41-verb-arm-package` (P3) — package the verb arm for the
   split-41-redteam docket: @39 "qui [41]" (64='qui' granted,
   finite-verb-forced) plus verb-compatible windows (@91, @964, @1048)
   with per-window parse and "qui [V]" forcing counts from the period
   corpus. Mirror of what `val-41-det-windows` did for the determiner
   arm. Bar: package delivered with >=1 strong leg and corpus counts;
   else fence. Evidence: `@35..43 = 08 91 39 64 41 01 24 88 43`.
   Split-gated: fences if split-41-redteam kills the verb arm.
2. `41-808-role` (P3) — decide 41's tier at @808 (`24 24 41 12 48`):
   preceding finite 24 forces a word boundary, but follower 12
   ('n'-pending) invites a word-internal reading. Discriminating frame
   for the letter-tier boundary. Bar: standalone vs word-internal
   decided with >=2 legs; else fence. Evidence: `@804..812` above.
3. `41-05-class` (P3) — discriminate 41's class at @5 (`47=ce 41 06
   77=le`): adjective vs noun (determiner/numeral/adverb killed per D3).
   Corpus counts for "ce [adj/noun] X le"-shaped frames. Bar: class
   named with >=2 independent legs; else fence. Evidence: `@1..9 = 00
   97 51 47 41 06 77 78 18`. Split-gated.

## Scope

Decides 41's forcing census and nameability only. Untouched: all §7
standings, `val-41-det-windows` PROMOTE, `val-41-1016` NULL + W_C fence,
`41-doubling-audit` PROMOTE, `split-41-redteam` (queued), `fin-41-lexicon-r2`
(queued), `wordinternal-41-census` (queued), `val-41-40-independent`
(queued), the val-24 targets (queued), R5005, sealed gates, red-team
adjudication queue.
