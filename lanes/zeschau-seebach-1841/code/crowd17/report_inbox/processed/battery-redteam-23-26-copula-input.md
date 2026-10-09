# Red-team input package: 23/26 copula question

- Target: `redteam-23-26-copula-input` (battery-queue.json, priority 2, status queued → verdict)
- Claim: package the 23/26 leg inventory as red-team input for the copula question.
- Worker: 4f101610-7d03-4515-ab39-8917f632cbc1. Date: 2026-10-09.
- Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`; asserts held: 1,847 pairs, 96 types). `canonical.py` NOT used. R5005, sealed gate instances, red-team adjudication queue untouched.
- All @-offsets are 0-based pair indices in the repaired stream.
- Lock: `code/crowd17/next-token/locks/redteam-23-26-copula-input.lock` created on start (no stale lock present); deleted on completion.

## Bar (verbatim, pre-registered)

"gather-only: legs exist, value blocked on §7 polyvalence jurisdiction; no battery-level naming"

**Restated as numbered pass/fail clauses (frozen before packaging):**
1. **C1 (gather arm):** every leg in the parent inventory is re-verified byte-exact against the repaired stream with its @-offset, window, and frame class, with no new numbers invented.
2. **C2 (jurisdiction arm):** the report names NO battery-level value for 23 or 26 and frames the decision explicitly as §7 red-team jurisdiction (polyvalence grant / homophony with provisional 59=est).
3. **C3 (context arm):** the package includes the 59 "est [pred]" comparison data (A1-following rates) as evidence-only context for the red team.

## Method

1. Read BATTERY-PROTOCOL.md in full before testing.
2. Re-derived the repaired stream in-session (1,847 pairs / 96 types asserted).
3. Byte-exact re-verification of all 11 parent-inventory legs (windows ±4, asserted cell id at the @-offset) against the stream. No deviations found — every window matches the parent table exactly.
4. Independently censused 59→A1 rates for the comparison context (59 n=27).

## Leg inventory (all windows re-verified byte-exact, 0-based @-offsets)

Notation: `X` = preceding context (4 pairs), `[N]` = the cell, followers (4 pairs). Frame classes per standing grants: A1 predicative {37,32,42}; A15 84="on"; A11 45="ce".

### Cell 23 (n=8) — 3 copula/verb legs

| @ | window (±4) | frame class |
|---|---|---|
| **182** | `14 24 87 64 [23] 37 06 00 33` | copula: "ce qui [23] [37-pred]" — 64=qui granted requires a finite verb; 37 is A1 predicative; parses with zero new assumptions |
| **679** | `64 37 77 45 [23] 09 07 00 92` | copula: 45=ce (A11); "c'est"-frame copula-23 parses with zero new assumptions |
| **1609** | `39 11 92 65 [23] 08 55 83 71` | finite verb: 65 noun-class (R20-047) subject + finite 23 + complement 08; zero new assumptions |

23 non-leg windows (no copula/verb license, retained for completeness): @136 (`56 64 21 65 [23] 91 65 13 66`, 65 is noun-class, no verb geometry); @1056 (`29 74 74 45 [23] 77 84 09 98`, "ce [23] le on" ungrammatical, 84=on subject); @1552 (`12 94 92 45 [23] 99 13 93 61`); @1697 (`24 85 58 15 [23] 91 85 33 94`, neighbors unvalued); @1782 (`19 48 74 65 [23] 98 83 82 96`, adjacent finite verbs unlicensed).

### Cell 26 (n=17) — 8 copula/verb legs

| @ | window (±4) | frame class |
|---|---|---|
| **155** | `47 46 66 84 [26] 35 58 35 93` | finite verb: 84=on (A15) requires a finite verb; zero new assumptions |
| **406** | `88 53 34 69 [26] 00 33 01 02` | finite verb: "[69-N] [26] pour" — 69 noun-class (R19-109); noun subject + finite 26 + pour-infinitive; zero new assumptions |
| **531** | `44 59 37 64 [26] 32 16 08 24` | copula: "qui [26] [32-pred]"; "qui est [pred]"; zero new assumptions |
| **601** | `29 40 03 39 [26] 96 45 93 54` | verb (weaker): "[26] par [45]" — verb + "par" agent/adjunct; grammatical but the verb class of 26 is the hypothesis under test; counted as one leg only |
| **842** | `98 20 62 94 [26] 12 16 00 33` | finite verb: "ne [26] [12]" — 94=ne (strong lead) needs a finite verb; zero new assumptions |
| **934** | `98 83 56 69 [26] 00 33 21 64` | finite verb: "[69-N] [26] pour" geometry, independent window from @406 |
| **1628** | `33 46 56 69 [26] 00 33 21 64` | finite verb: third "[69-N] [26] pour" window, independent |
| **1769** | `09 24 87 64 [26] 37 78 62 94` | copula: "qui [26] [37-pred]"; "qui est [pred]"; zero new assumptions |

26 non-leg windows (no verb license, retained for completeness): @129 (`82 48 11 02 [26] 32 96 56 64`, needs nominal 02, unvalued); @240; @655 and @992 and @1560 (killed "en Xpas" arm, `reseg-1564-26pas`, KILL 2026-10-09); @1250 (killed "que Xpas" arm, same ruling); @1470; @1707 (88 already the verb — second finite verb forced); @1753 (89 verb-frame occupies the verb slot).

## 59 comparison context (evidence only, no naming)

The only nameable value the legs support is "est", which collides with provisional 59=est under §7's sole-polyvalence rule. The red team needs the distributional comparison; this is data, not a decision.

- n59 = 27 on the repaired stream.
- 59 → A1 ({37,32,42}) windows: 11/27 (40.7%): 37 ×6, 42 ×2, 32 ×3. ("est [pred]" frame rate for the provisional incumbent.)
- 23 → A1 windows: 1/8 (@182) = 12.5%.
- 26 → A1 windows: 3/17 (@129, @531, @1769) = 17.6%.
- Note: 1690 frequency uniformity is necessary but insufficient for homophony (§7). The sibling targets `val-23-copula-gather` and `val-26-copula-gather` (both queued) gather the full 1690 uniformity data; this package supplies the leg side of the comparison.

## Clause results

1. **C1 (gather arm): PASS.** All 11 legs re-verified byte-exact against the repaired stream: 3 for cell 23 (n=8), 8 for cell 26 (n=17), with independent ±4 windows asserted at each @-offset. No invented numbers; non-leg windows listed for completeness.
2. **C2 (jurisdiction arm): PASS.** No battery-level value is named for 23 or 26 anywhere in this report. The decision — polyvalence grant, homophony with provisional 59=est, or another resolution — is §7 red-team jurisdiction exclusively. The 23~26 split holds (A2 SPLIT GRANTED; the two cells are independent — nothing here forces them to share a value).
3. **C3 (context arm): PASS.** 59 "est [pred]" comparison data included above (n59=27; 11/27 A1-following vs 1/8 and 3/17 for 23/26).

## Verdict: NULL (null-with-package, §4 gather-only)

Per §4, a gather-only null is a package, not an ending: the evidence is assembled, the block is jurisdictional (§7 polyvalence: naming "est" for 23 or 26 would create a homophone with provisional 59=est without a red-team grant; any other value would be invention). No standing verdict contradicted or downgraded. The package is complete and awaiting the red-team adjudication queue.

## Follow-up note

Per the task brief and §4, follow-ups for this null are the already-proposed siblings: `val-23-copula-gather` and `val-26-copula-gather` (both present in battery-queue.json, status queued, verdictless as of 2026-10-09). This worker proposes no additional targets — this package is the terminal input for the red-team handoff.

## Bookkeeping

- `battery-queue.json`: `redteam-23-26-copula-input` queued → verdict/null (temp-file + rename; pre-write assert passed — was queued/verdictless; JSON re-validated from disk; own entry only; no downgrade).
- Lock `locks/redteam-23-26-copula-input.lock`: created on start (no stale lock present); deleted on completion.
- R5005, sealed gate instances, red-team adjudication queue untouched.
