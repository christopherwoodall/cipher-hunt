# Battery verdict: qui-fol-23-26-value

- Target: `qui-fol-23-26-value` (battery-queue.json, priority 3, status queued)
- Claim: Test whether 23 or 26 can carry copula/verb value under standing values via their other stream windows.
- Worker: 3ba5198a-c218-4bac-900d-8af3b4025641. Date: 2026-10-09.
- Note: re-dispatch after a daemon restart killed the first worker; no report or queue changes existed — clean re-run.
- Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`; asserts held: 1,847 pairs, 96 types). `canonical.py` NOT used. R5005, sealed gates, red-team queue untouched.
- All @-offsets are 0-based pair indices in the repaired stream.
- Lock: `code/crowd17/next-token/locks/qui-fol-23-26-value.lock` created on start (no stale lock present); deleted on completion.

## Bar (verbatim, pre-registered)

"Name the value with >=2 independent legs, or fence the followers as non-verbal."

**Restated as numbered pass/fail clauses (frozen before testing):**
1. **C1 (name arm):** a value for 23 or 26 is NAMED with >=2 independent legs under standing values and zero new assumptions, with no standing-verdict contradiction.
2. **C2 (fence arm):** else, fence the followers as non-verbal (copula/verb readings closed stream-wide for 23 and 26).

Context: parent `qui-predicate-87-census` (NULL, 2026-10-09) found the five "87 64" followers to be 96(=par), 23, 26, 59(=est*), 77(=le*) — only @1776 ("ce qui est") licensed a qui-predicate. This battery generalizes: do 23 and 26 carry copula/verb value anywhere else on the stream?

## Method

1. Read BATTERY-PROTOCOL.md in full before testing.
2. Re-derived the repaired stream in-session; byte-exact window censuses for 23 (n=8) and 26 (n=17) with ±4 context.
3. Graded every window against a copula/verb reading under standing values only (§7): pencil GT (11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que); granted (87=ce, 64=qui, 96=par, 17=fois, 79=tout, 00=pour, 84=on, 47=ce); provisional (59=est, 77=le); frames (A1 predicative 37/32/42, A8 verb-frames 80/89, A3 verb-stem 85, A9, A15, A11).

## Clause results

### Cell 23 (n=8) — three independent copula/verb legs

| @ | window (±4) | grade |
|---|---|---|
| 136 | `56 64 21 65 [23] 91 65 13 66` | no license — 65 is noun-class (R20-047), "qui [65-N] [23]" has no licensed verb geometry |
| **182** | `14 24 87 64 [23] 37 06 00 33` | **copula leg** — "ce qui [23] [37-pred]": 64=qui granted requires a finite verb; 37 is A1 predicative; copula-23 ("qui est [pred]") parses with zero new assumptions |
| **679** | `64 37 77 45 [23] 09 07 00 92` | **copula leg** — "…ce [23] [09]": 45=ce (A11); "c'est"-frame copula-23 parses with zero new assumptions |
| 1056 | `29 74 74 45 [23] 77 84 09 98` | no license — "ce [23] le on" is ungrammatical for copula-23 (84=on subject pronoun) |
| 1552 | `12 94 92 45 [23] 99 13 93 61` | no license — "ne [92] ce [23] [99]" ungrammatical |
| **1609** | `39 11 92 65 [23] 08 55 83 71` | **finite-verb leg** — "[65-N] [23] [08]": 65 noun-class subject + finite 23 + complement 08; parses with zero new assumptions |
| 1697 | `24 85 58 15 [23] 91 85 33 94` | no license — neighbors unvalued |
| 1782 | `19 48 74 65 [23] 98 83 82 96` | no license — adjacent finite verbs unlicensed |

### Cell 26 (n=17) — eight independent copula/verb legs

| @ | window (±4) | grade |
|---|---|---|
| 129 | `82 48 11 02 [26] 32 96 56 64` | no license — "[02] [26] [32-pred]" needs a nominal 02, unvalued |
| **155** | `47 46 66 84 [26] 35 58 35 93` | **finite-verb leg** — "on [26]": 84=on (A15) requires a finite verb; zero new assumptions |
| 240 | `98 41 17 11 [26] 12 16 56 43` | no license — "la [26]" strained, 12 unvalued |
| **406** | `88 53 34 69 [26] 00 33 01 02` | **finite-verb leg** — "[69-N] [26] pour": 69 noun-class (R19-109); noun subject + finite 26 + pour-infinitive; zero new assumptions |
| **531** | `44 59 37 64 [26] 32 16 08 24` | **copula leg** — "qui [26] [32-pred]": "qui est [pred]"; zero new assumptions |
| **601** | `29 40 03 39 [26] 96 45 93 54` | **verb leg (weaker)** — "[26] par [45]": verb + "par" agent/adjunct; grammatical but the verb class of 26 is the hypothesis under test, so counted as one leg only |
| 655 | `94 76 49 24 [26] 30 03 62 16` | no verb leg — "24 26 30" is the killed "en Xpas" arm (`reseg-1564-26pas`, KILL 2026-10-09) |
| **842** | `98 20 62 94 [26] 12 16 00 33` | **finite-verb leg** — "ne [26] [12]": 94=ne (strong lead) needs a finite verb; zero new assumptions |
| **934** | `98 83 56 69 [26] 00 33 21 64` | **finite-verb leg** — same "[69-N] [26] pour" geometry as @406; independent window |
| 992 | `01 76 49 24 [26] 30 03 60 67` | no verb leg — killed "en Xpas" arm |
| 1250 | `16 00 67 46 [26] 30 06 65 46` | no verb leg — "que Xpas" killed at kill grade (`reseg-1564-26pas`) |
| 1470 | `21 02 62 38 [26] 12 41 53 60` | no license — neighbors unvalued |
| 1560 | `61 40 17 11 [26] 30 06 60 71` | no verb leg — "fois la Xpas" killed at kill grade |
| **1628** | `33 46 56 69 [26] 00 33 21 64` | **finite-verb leg** — third "[69-N] [26] pour" window; independent |
| 1707 | `20 62 94 88 [26] 12 06 29 40` | no verb leg — 88 is already the verb ("ne [88-V] [26]" forces a second finite verb) |
| 1753 | `34 07 28 89 [26] 24 85 58 17` | no verb leg — 89 verb-frame already occupies the verb slot |
| **1769** | `09 24 87 64 [26] 37 78 62 94` | **copula leg** — "qui [26] [37-pred]": "qui est [pred]"; zero new assumptions |

## Findings

- **C1 (name arm): BLOCKED, not failed on evidence.** Both followers clear the ≥2-leg bar: 23 has 3 independent legs (@182 copula, @679 copula, @1609 finite); 26 has 8 (@155, @406, @934, @1628 finite; @531, @1769 copula; @601 verb; @842 ne-verb). But the only nameable value the legs support is **"est"** — and naming it contradicts standing constraints at battery grade: 59=est is provisional (§7), and §7 fixes "67 et/veut" as the sole true polyvalence. Naming 23="est" or 26="est" would create a homophone with 59 without a red-team polyvalence grant. Any other specific French verb value would be invention (§3: no letter evidence constrains it). Per protocol §5.2, a battery does not overwrite standing verdicts — the name arm cannot fire here.
- **C2 (fence arm): FAIL.** The legs above are genuine and independent; the followers cannot be fenced as non-verbal.
- Net: both followers CARRY copula/verb value at battery grade, but the value is unnameable without a red-team polyvalence/homophony decision. This is a genuine escalation, not a stalemate: the evidence is positive (legs exist), the blocker is jurisdictional (§7).
- Adverses: none listed. The 23~26 split holds (§7) — the two cells are independent; nothing in this battery forces them to share a value.
- No standing/red-team verdict contradicted or downgraded; §7 intact; canonical-stream caveat stands.

## Verdict: NULL

Positive legs exist for both followers (3 for 23, 8 for 26); the value is unnameable at battery grade because naming "est" collides with provisional 59=est under §7's sole-polyvalence rule. Escalated to the red team per §5.2.

## Follow-ups proposed (all verified ABSENT from battery-queue.json)

1. `val-23-copula-gather` (P3) — gather the 1690 frequency-uniformity data for 23 vs 59 (homophony candidacy): corpus-rate comparison under the 1690 rule; no naming, evidence only.
2. `val-26-copula-gather` (P3) — same for 26 vs 59: the 8 legs' frames tabulated against 59's A1 "est [pred]" windows for distributional comparison.
3. `redteam-23-26-copula-input` (P2, gather-only) — package this battery's leg inventory as red-team input for the 23/26 copula question: legs exist, value blocked on §7 polyvalence jurisdiction. No battery-level naming.

## Bookkeeping

- `battery-queue.json`: `qui-fol-23-26-value` queued → verdict/null (temp-file + rename; pre-write assert passed — was queued/verdictless; JSON re-validated from disk; own entry only; no downgrade).
- Lock `locks/qui-fol-23-26-value.lock`: created on start, deleted on completion.
- R5005, sealed gates, red-team adjudication queue untouched.
