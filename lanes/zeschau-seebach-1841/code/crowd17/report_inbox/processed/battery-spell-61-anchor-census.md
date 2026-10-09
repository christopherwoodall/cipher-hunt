# Battery report: spell-61-anchor-census

- Target id: `spell-61-anchor-census`
- Claim: full spelling-composition census of all 18 61 windows to permanently fence (or re-open) spelling-anchor extensions
- Date: 2026-10-09
- Worker: battery worker (subagent 04c36165-b939-4fcf-a6da-8347603d1430)
- Stream: repaired 1,847-pair / 96-type parse re-derived in-session from `data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json` (asserts held: 1,847 pairs, 96 types). `canonical.py` never used. R5005, sealed gate instances, and the red-team adjudication queue untouched.

## Bar (verbatim, from battery-queue.json)

"census covers all 18 61 windows with byte evidence; fence iff @1556 stays the sole complete spelling-composed window"

## Numbered pass/fail clauses (pre-registered before testing, not modified after)

1. **C1:** the census covers all 18 windows of 61 with byte-exact evidence (each window's ±4 context and its letter-adjacency status).
2. **C2:** fence iff @1556 stays the SOLE complete spelling-composed window — i.e., no other 61 window composes a complete grammatical French word/phrase with adjacent valued letter-groups under standing values.

Verdict rule: **promote** iff C1 and C2 both pass (the spelling-anchor fence is confirmed); **kill** iff a second complete spelling-composed window is found (the fence claim is forced false, re-open); **null** otherwise, with 1–3 follow-ups.

## Terms used here

- **Valued letter-group**: a cell with a standing letter/syllable value — banked GT (11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que), letter-tier (12=n spelling letter; 94='ne' lead), per BATTERY-PROTOCOL.md §7 and lane usage.
- **Spelling-composed window**: 61 is immediately adjacent (bigram X-61 or 61-X) to ≥1 valued letter-group.
- **Complete spelling-composed window**: the adjacent valued letter-groups + 61 compose a complete, grammatical French word or fixed phrase under standing values with zero ungranted assumptions (the val-61-premier locus standard: "61 40 17" = "première fois").
- **Ordinal-slot admission** (premier-61-admit-fence, PROMOTE 2026-10-09): 61 admits "premier" in a conditioned determiner/noun-class slot. This is a DIFFERENT property from spelling composition and is not re-litigated here.

## Method

1. Read BATTERY-PROTOCOL.md in full before testing. Created `code/crowd17/next-token/locks/spell-61-anchor-census.lock` on start (agent id + 2026-10-09T17:13:29Z); no stale lock present.
2. Re-derived the repaired stream byte-exact per `code/side-keyhunt/repair_parse.py` (`[s[i:i+2] for i in range(o, len(s)-1, 2)]`). All @-offsets below are 0-based pair indices.
3. Adopted, never re-litigated: val-61-premier (PROMOTE, locus-level @1556 only); val-61-contact (KILL of any global 61 value); premier-61-admit-fence (conditioned ordinal-slot set @279/@281/@645/@1556); premier-61-flank-census (18-window census, NULL sharpened to one-off locus).
4. Enumerated all 61 bigrams stream-wide and all trigrams containing 61 with a letter-valued cell, byte-exact.

## Window-level evidence (all 18 windows, byte-verified)

n(61) = 18, re-derived independently (matches premier-61-flank-census). Anchor checks: "61 40" = 1 stream-wide (@1556); "40 17" = 2 (@1039 flagship, @1556); full analytic "70 82 34 29 40 17" = 1.

### Windows with NO letter-valued neighbor (12 windows — cannot be spelling anchors)

| @ | window (±2) | neighbors |
|---|---|---|
| 223 | 89 [61] 96 | 89 open; 96=par (word) |
| 279 | 37 [61] 20 | 37 predicative-class; 20 reladv-subclass |
| 281 | 20 [61] 42 | 20 reladv-subclass; 42 noun-class |
| 447 | 62 [61] 59 | 62; 59=est (provisional word) |
| 645 | 87 [61] 88 | 87=ce (granted word); 88 verb-class |
| 926 | 17 [61] 96 | 17=fois (word); 96=par (word) |
| 1206 | 55 [61] 21 | 55 verb-class; 21 noun-class |
| 1219 | 92 [61] 24 | 92 open; 24 finite-verb class |
| 1256 | 01 [61] 31 | 01 open; 31 open |
| 1281 | 53 [61] 56 | 53 open; 56 verb-class |
| 1455 | 62 [61] 21 | 62; 21 noun-class |
| 1810 | 04 [61] 15 | 04 open; 15 open |

Note: the three ordinal-slot admissions @279/@281/@645 have zero letter-valued neighbors — ordinal-slot admission does not create a spelling anchor.

### Windows WITH a letter-valued neighbor (6 windows — spelling-composed candidates)

| @ | trigram | composition | complete? |
|---|---|---|---|
| 367 | 49 [61] 70 | "premier"+"pre" (70=pre GT) | NO — "premier pre fois" fenced ungrammatical (val-61-premier); "premierpre" is not a French word |
| 577 | 55 [61] 94 | "premier"+"ne" (94='ne' lead only) | NO — "61 94 82" = "premier ne m [06]": 94 is a lead, not granted; "ne m" needs a following verb; no complete word shape |
| 1168 | 55 [61] 94 | "premier"+"ne" (94='ne' lead only) | NO — "61 94 87" = "premier ne ce": same as @577, no complete word shape |
| 1429 | 91 [61] 12 | "premier"+"n" (12=n) | NO — "premiern" is not a word; 16 unvalued; no vowel (parent's finding confirmed byte-exact) |
| 1510 | 12 [61] 59 | "n"+"premier" (12=n) | NO — "npremier" is not a word; val-61-contact Frame C forces non-nominal 61 here (clitic-class KILL stands) |
| 1556 | 93 [61] 40 | "premier"+"e" (40=e GT) + 17=fois | YES — "61 40 17" = "première fois": complete French phrase; "61 40" unique stream-wide; "40 17" flagship-identical (val-61-premier PROMOTE, standing) |

Exhaustiveness checks (byte-exact, stream-wide):
- 61 never directly neighbors 82=m, 34=i, 29=er, 46=que, or 11=la (0 occurrences each).
- The 6 letter-adjacent trigrams above are the ONLY trigrams containing 61 with a letter-valued cell.

## Per-clause results

1. **C1: PASS** — all 18 windows censused byte-exact with ±4 context; n(61)=18 confirmed; letter-adjacency enumerated exhaustively via stream-wide bigram/trigram census.
2. **C2: PASS** — @1556 is the SOLE complete spelling-composed window. The 5 other letter-adjacent windows fail completeness with stated cause each (ungrammatical / lead-only / non-word / fenced class). The fence fires.

**Verdict: PROMOTE** — the spelling-anchor fence is confirmed. Any 61 extension that requires a spelling anchor (a second window composing a complete word with valued letter-groups) is permanently fenced at battery grade. The re-open arm does not fire: no second anchor exists.

## Scope

- Confirms and sharpens val-61-premier's locus-level PROMOTE (@1556 stays the unique spelling anchor).
- Does not touch val-61-contact's KILL of any global 61 value (not re-litigated).
- Does not touch premier-61-admit-fence's conditioned ordinal-slot set (@279/@281/@645/@1556): ordinal-slot admission is a different property and is explicitly NOT a spelling anchor — none of @279/@281/@645 has a letter-valued neighbor.
- No standing or red-team verdict contradicted or downgraded; §7 intact. Adverses: none were listed.
- Canonical-stream caveat stands (68 of 70 upstream row offsets unvalidated).

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-spell-61-anchor-census.md` (this file).
- Queue: `spell-61-anchor-census` queued → verdict/promote, 2026-10-09 (pre-write assert passed — was queued/verdictless; temp-file + rename; JSON re-validated; own entry only; no downgrade).
- Lock `locks/spell-61-anchor-census.lock`: created on start, deleted on completion (verified gone).
- R5005, sealed gate instances, red-team adjudication queue untouched.
